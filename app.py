import os
import sqlparse
from flask import Flask, render_template, request, redirect, url_for
import db

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

# Helper to format SQL query nicely for display
def format_sql(query):
    if not query:
        return ""
    try:
        # Re-indent and capitalize keywords
        return sqlparse.format(query, reindent=True, keyword_case='upper')
    except Exception:
        return query

@app.context_processor
def inject_global_vars():
    """
    Inject global variables into all templates (like whether DB is in Mock mode).
    """
    return {
        "using_mock": db.using_mock
    }

# ==========================================
# ROUTES
# ==========================================

@app.route('/')
def index():
    """
    Home page. Features search bar and hospital info.
    """
    return render_template('index.html')

@app.route('/search')
def search():
    """
    Search results page. Searches symptoms/doctors.
    """
    query = request.args.get('q', '').strip()
    if not query:
        return redirect(url_for('index'))
        
    doctors, raw_sql, corrected_term = db.search_doctors(query)
    formatted_sql = format_sql(raw_sql)
    
    return render_template(
        'search.html',
        query=query,
        doctors=doctors,
        sql_query=formatted_sql,
        corrected_term=corrected_term
    )

@app.route('/doctors')
def doctors_list():
    """
    Doctors list page. Optional filtering by specialization.
    """
    spec_id = request.args.get('specialization', '').strip()
    spec_id = int(spec_id) if spec_id.isdigit() else None
    
    # Get dropdown list
    specializations, spec_sql = db.get_specializations()
    
    # Get doctors list
    doctors, doc_sql = db.list_doctors(spec_id)
    
    # Combine SQL queries for presentation
    combined_sql = f"-- 1. Fetch Specializations (Dropdown list):\n{spec_sql}\n\n-- 2. Fetch Doctors List:\n{doc_sql}"
    formatted_sql = format_sql(combined_sql)
    
    # Find current selected specialization name
    current_specialization = None
    if spec_id:
        for spec in specializations:
            if spec["id"] == spec_id:
                current_specialization = spec["name"]
                break
                
    return render_template(
        'doctors.html',
        specializations=specializations,
        doctors=doctors,
        selected_spec_id=spec_id,
        current_specialization=current_specialization,
        sql_query=formatted_sql
    )

@app.route('/doctor/<int:doctor_id>')
def doctor_detail(doctor_id):
    """
    Doctor details and schedule profile page.
    """
    doctor, raw_sql = db.get_doctor_details(doctor_id)
    if not doctor:
        return "Doctor not found", 404
        
    formatted_sql = format_sql(raw_sql)
    
    return render_template(
        'doctor.html',
        doctor=doctor,
        sql_query=formatted_sql
    )

if __name__ == '__main__':
    # Try running on port 3000 as configured in .env
    port = int(os.getenv("PORT", 8080))
    print(f"[*] Starting Hospital Management System on http://localhost:{port}")
    app.run(host="0.0.0.0", port=port, debug=True)
