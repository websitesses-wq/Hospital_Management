import os
import datetime
import pymysql
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database configuration
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_DATABASE = os.getenv("DB_DATABASE", "hospital_db")

# Flag to track if we are using the Mock Database fallback
using_mock = False

def get_connection():
    global using_mock
    try:
        conn = pymysql.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_DATABASE,
            cursorclass=pymysql.cursors.DictCursor,
            connect_timeout=2
        )
        using_mock = False
        return conn
    except Exception as e:
        if not using_mock:
            print(f"[*] MySQL connection failed: {e}")
            print("[*] Falling back to Mock Database Mode.")
            using_mock = True
        return None

# ==========================================
# MOCK DATABASE STATE (Fallback)
# ==========================================
MOCK_SPECIALIZATIONS = [
    {"id": 1, "name": "General Medicine"},
    {"id": 2, "name": "Cardiology"},
    {"id": 3, "name": "Pediatrics"},
    {"id": 4, "name": "Orthopedics"},
    {"id": 5, "name": "Dermatology"},
    {"id": 6, "name": "Neurology"}
]

# Expanded doctors list (12 doctors per specialization)
MOCK_DOCTORS = [
    # General Medicine (id 1)
    {"id": 1, "name": "Dr. Ranji Patel", "specialization_id": 1, "qualification": "MD - General Medicine, MBBS", "phone": "+91 98190 12345", "email": "ranji.patel@cityline.com"},
    {"id": 2, "name": "Dr. Anjali Sharma", "specialization_id": 1, "qualification": "MD, MBBS", "phone": "+91 98191 12346", "email": "anjali.sharma@cityline.com"},
    {"id": 3, "name": "Dr. Vikram Singh", "specialization_id": 1, "qualification": "MD, MBBS", "phone": "+91 98192 12347", "email": "vikram.singh@cityline.com"},
    {"id": 4, "name": "Dr. Meera Joshi", "specialization_id": 1, "qualification": "MD, MBBS", "phone": "+91 98193 12348", "email": "meera.joshi@cityline.com"},
    {"id": 5, "name": "Dr. Suresh Kumar", "specialization_id": 1, "qualification": "MD, MBBS", "phone": "+91 98194 12349", "email": "suresh.kumar@cityline.com"},
    {"id": 6, "name": "Dr. Neha Gupta", "specialization_id": 1, "qualification": "MD, MBBS", "phone": "+91 98195 12350", "email": "neha.gupta@cityline.com"},
    {"id": 7, "name": "Dr. Arjun Mehta", "specialization_id": 1, "qualification": "MD, MBBS", "phone": "+91 98196 12351", "email": "arjun.mehta@cityline.com"},
    {"id": 8, "name": "Dr. Priyanka Rao", "specialization_id": 1, "qualification": "MD, MBBS", "phone": "+91 98197 12352", "email": "priyanka.rao@cityline.com"},
    {"id": 9, "name": "Dr. Kiran Desai", "specialization_id": 1, "qualification": "MD, MBBS", "phone": "+91 98198 12353", "email": "kiran.desai@cityline.com"},
    {"id": 10, "name": "Dr. Sunil Verma", "specialization_id": 1, "qualification": "MD, MBBS", "phone": "+91 98199 12354", "email": "sunil.verma@cityline.com"},
    {"id": 11, "name": "Dr. Aditi Nair", "specialization_id": 1, "qualification": "MD, MBBS", "phone": "+91 98200 12355", "email": "aditi.nair@cityline.com"},
    {"id": 12, "name": "Dr. Rahul Bhatt", "specialization_id": 1, "qualification": "MD, MBBS", "phone": "+91 98201 12356", "email": "rahul.bhatt@cityline.com"},
    # Cardiology (id 2)
    {"id": 13, "name": "Dr. Amit Sharma", "specialization_id": 2, "qualification": "DM - Cardiology, MD, MBBS", "phone": "+91 98202 12357", "email": "amit.sharma@cityline.com"},
    {"id": 14, "name": "Dr. Rohan Kapoor", "specialization_id": 2, "qualification": "DM, MD, MBBS", "phone": "+91 98203 12358", "email": "rohan.kapoor@cityline.com"},
    {"id": 15, "name": "Dr. Lata Menon", "specialization_id": 2, "qualification": "DM, MD, MBBS", "phone": "+91 98204 12359", "email": "lata.menon@cityline.com"},
    {"id": 16, "name": "Dr. Sameer Iyer", "specialization_id": 2, "qualification": "DM, MD, MBBS", "phone": "+91 98205 12360", "email": "sameer.iyer@cityline.com"},
    {"id": 17, "name": "Dr. Kavita Joshi", "specialization_id": 2, "qualification": "DM, MD, MBBS", "phone": "+91 98206 12361", "email": "kavita.joshi@cityline.com"},
    {"id": 18, "name": "Dr. Nikhil Rao", "specialization_id": 2, "qualification": "DM, MD, MBBS", "phone": "+91 98207 12362", "email": "nikhil.rao@cityline.com"},
    {"id": 19, "name": "Dr. Pooja Singh", "specialization_id": 2, "qualification": "DM, MD, MBBS", "phone": "+91 98208 12363", "email": "pooja.singh@cityline.com"},
    {"id": 20, "name": "Dr. Sanjay Patel", "specialization_id": 2, "qualification": "DM, MD, MBBS", "phone": "+91 98209 12364", "email": "sanjay.patel@cityline.com"},
    {"id": 21, "name": "Dr. Ananya Sharma", "specialization_id": 2, "qualification": "DM, MD, MBBS", "phone": "+91 98210 12365", "email": "ananya.sharma@cityline.com"},
    {"id": 22, "name": "Dr. Vikas Singh", "specialization_id": 2, "qualification": "DM, MD, MBBS", "phone": "+91 98211 12366", "email": "vikas.singh@cityline.com"},
    {"id": 23, "name": "Dr. Meena Iyer", "specialization_id": 2, "qualification": "DM, MD, MBBS", "phone": "+91 98212 12367", "email": "meena.iyer@cityline.com"},
    {"id": 24, "name": "Dr. Hrithik Aggarwal", "specialization_id": 2, "qualification": "DM, MD, MBBS", "phone": "+91 98213 12368", "email": "hrithik.aggarwal@cityline.com"},
    # Pediatrics (id 3)
    {"id": 25, "name": "Dr. Sarah Johnson", "specialization_id": 3, "qualification": "MD - Pediatrics, DCH, MBBS", "phone": "+91 98214 12369", "email": "sarah.johnson@cityline.com"},
    {"id": 26, "name": "Dr. Riya Kapoor", "specialization_id": 3, "qualification": "MD, DCH, MBBS", "phone": "+91 98215 12370", "email": "riya.kapoor@cityline.com"},
    {"id": 27, "name": "Dr. Amitabh Verma", "specialization_id": 3, "qualification": "MD, DCH, MBBS", "phone": "+91 98216 12371", "email": "amitabh.verma@cityline.com"},
    {"id": 28, "name": "Dr. Maya Singh", "specialization_id": 3, "qualification": "MD, DCH, MBBS", "phone": "+91 98217 12372", "email": "maya.singh@cityline.com"},
    {"id": 29, "name": "Dr. Kunal Mehta", "specialization_id": 3, "qualification": "MD, DCH, MBBS", "phone": "+91 98218 12373", "email": "kunal.mehta@cityline.com"},
    {"id": 30, "name": "Dr. Priya Sharma", "specialization_id": 3, "qualification": "MD, DCH, MBBS", "phone": "+91 98219 12374", "email": "priya.sharma@cityline.com"},
    {"id": 31, "name": "Dr. Neeraj Gupta", "specialization_id": 3, "qualification": "MD, DCH, MBBS", "phone": "+91 98220 12375", "email": "neeraj.gupta@cityline.com"},
    {"id": 32, "name": "Dr. Alka Patel", "specialization_id": 3, "qualification": "MD, DCH, MBBS", "phone": "+91 98221 12376", "email": "alka.patel@cityline.com"},
    {"id": 33, "name": "Dr. Rohit Kumar", "specialization_id": 3, "qualification": "MD, DCH, MBBS", "phone": "+91 98222 12377", "email": "rohit.kumar@cityline.com"},
    {"id": 34, "name": "Dr. Sunita Iyer", "specialization_id": 3, "qualification": "MD, DCH, MBBS", "phone": "+91 98223 12378", "email": "sunita.iyer@cityline.com"},
    {"id": 35, "name": "Dr. Vijay Singh", "specialization_id": 3, "qualification": "MD, DCH, MBBS", "phone": "+91 98224 12379", "email": "vijay.singh@cityline.com"},
    # Orthopedics (id 4)
    {"id": 36, "name": "Dr. Rajesh Kumar", "specialization_id": 4, "qualification": "MS - Orthopedics, MBBS", "phone": "+91 98225 12380", "email": "rajesh.kumar@cityline.com"},
    {"id": 37, "name": "Dr. Sneha Reddy", "specialization_id": 4, "qualification": "MS, MBBS", "phone": "+91 98226 12381", "email": "sneha.reddy@cityline.com"},
    {"id": 38, "name": "Dr. Arvind Rao", "specialization_id": 4, "qualification": "MS, MBBS", "phone": "+91 98227 12382", "email": "arvind.rao@cityline.com"},
    {"id": 39, "name": "Dr. Kavitha Menon", "specialization_id": 4, "qualification": "MS, MBBS", "phone": "+91 98228 12383", "email": "kavitha.menon@cityline.com"},
    {"id": 40, "name": "Dr. Harsh Patel", "specialization_id": 4, "qualification": "MS, MBBS", "phone": "+91 98229 12384", "email": "harsh.patel@cityline.com"},
    {"id": 41, "name": "Dr. Nisha Singh", "specialization_id": 4, "qualification": "MS, MBBS", "phone": "+91 98230 12385", "email": "nisha.singh@cityline.com"},
    {"id": 42, "name": "Dr. Gaurav Desai", "specialization_id": 4, "qualification": "MS, MBBS", "phone": "+91 98231 12386", "email": "gaurav.desai@cityline.com"},
    {"id": 43, "name": "Dr. Priyanka Shah", "specialization_id": 4, "qualification": "MS, MBBS", "phone": "+91 98232 12387", "email": "priyanka.shah@cityline.com"},
    {"id": 44, "name": "Dr. Amit Bhatia", "specialization_id": 4, "qualification": "MS, MBBS", "phone": "+91 98233 12388", "email": "amit.bhatia@cityline.com"},
    {"id": 45, "name": "Dr. Radhika Nair", "specialization_id": 4, "qualification": "MS, MBBS", "phone": "+91 98234 12389", "email": "radhika.nair@cityline.com"},
    {"id": 46, "name": "Dr. Suresh Singh", "specialization_id": 4, "qualification": "MS, MBBS", "phone": "+91 98235 12390", "email": "suresh.singh@cityline.com"},
    # Dermatology (id 5)
    {"id": 47, "name": "Dr. Priya Nair", "specialization_id": 5, "qualification": "MD - Dermatology & Venereology, MBBS", "phone": "+91 98236 12391", "email": "priya.nair@cityline.com"},
    {"id": 48, "name": "Dr. Anjali Verma", "specialization_id": 5, "qualification": "MD, MBBS", "phone": "+91 98237 12392", "email": "anjali.verma@cityline.com"},
    {"id": 49, "name": "Dr. Deepak Singh", "specialization_id": 5, "qualification": "MD, MBBS", "phone": "+91 98238 12393", "email": "deepak.singh@cityline.com"},
    {"id": 50, "name": "Dr. Sunita Rao", "specialization_id": 5, "qualification": "MD, MBBS", "phone": "+91 98239 12394", "email": "sunita.rao@cityline.com"},
    {"id": 51, "name": "Dr. Rohit Kapoor", "specialization_id": 5, "qualification": "MD, MBBS", "phone": "+91 98240 12395", "email": "rohit.kapoor@cityline.com"},
    {"id": 52, "name": "Dr. Meena Sharma", "specialization_id": 5, "qualification": "MD, MBBS", "phone": "+91 98241 12396", "email": "meena.sharma@cityline.com"},
    {"id": 53, "name": "Dr. Karan Patel", "specialization_id": 5, "qualification": "MD, MBBS", "phone": "+91 98242 12397", "email": "karan.patel@cityline.com"},
    {"id": 54, "name": "Dr. Asha Iyer", "specialization_id": 5, "qualification": "MD, MBBS", "phone": "+91 98243 12398", "email": "asha.iyer@cityline.com"},
    {"id": 55, "name": "Dr. Vinod Sharma", "specialization_id": 5, "qualification": "MD, MBBS", "phone": "+91 98244 12399", "email": "vinod.sharma@cityline.com"},
    {"id": 56, "name": "Dr. Neha Kapoor", "specialization_id": 5, "qualification": "MD, MBBS", "phone": "+91 98245 12400", "email": "neha.kapoor@cityline.com"},
    # Neurology (id 6)
    {"id": 57, "name": "Dr. Vikas Gupta", "specialization_id": 6, "qualification": "DM - Neurology, MD, MBBS", "phone": "+91 98246 12401", "email": "vikas.gupta@cityline.com"},
    {"id": 58, "name": "Dr. Simran Singh", "specialization_id": 6, "qualification": "DM, MD, MBBS", "phone": "+91 98247 12402", "email": "simran.singh@cityline.com"},
    {"id": 59, "name": "Dr. Arjun Patel", "specialization_id": 6, "qualification": "DM, MD, MBBS", "phone": "+91 98248 12403", "email": "arjun.patel@cityline.com"},
    {"id": 60, "name": "Dr. Kavita Sharma", "specialization_id": 6, "qualification": "DM, MD, MBBS", "phone": "+91 98249 12404", "email": "kavita.sharma@cityline.com"},
    {"id": 61, "name": "Dr. Rahul Iyer", "specialization_id": 6, "qualification": "DM, MD, MBBS", "phone": "+91 98250 12405", "email": "rahul.iyer@cityline.com"},
    {"id": 62, "name": "Dr. Nisha Rao", "specialization_id": 6, "qualification": "DM, MD, MBBS", "phone": "+91 98251 12406", "email": "nisha.rao@cityline.com"},
    {"id": 63, "name": "Dr. Amit Chandra", "specialization_id": 6, "qualification": "DM, MD, MBBS", "phone": "+91 98252 12407", "email": "amit.chandra@cityline.com"},
    {"id": 64, "name": "Dr. Riya Singh", "specialization_id": 6, "qualification": "DM, MD, MBBS", "phone": "+91 98253 12408", "email": "riya.singh@cityline.com"},
    {"id": 65, "name": "Dr. Sameer Patel", "specialization_id": 6, "qualification": "DM, MD, MBBS", "phone": "+91 98254 12409", "email": "sameer.patel@cityline.com"},
    {"id": 66, "name": "Dr. Anjali Gupta", "specialization_id": 6, "qualification": "DM, MD, MBBS", "phone": "+91 98255 12410", "email": "anjali.gupta@cityline.com"}
]

# Expanded symptoms for each specialization (at least 8 per specialty)
MOCK_SYMPTOMS = [
    # General Medicine
    {"id": 1, "name": "fever", "specialization_id": 1},
    {"id": 2, "name": "cold", "specialization_id": 1},
    {"id": 3, "name": "cough", "specialization_id": 1},
    {"id": 4, "name": "headache", "specialization_id": 1},
    {"id": 5, "name": "stomach pain", "specialization_id": 1},
    {"id": 6, "name": "fatigue", "specialization_id": 1},
    {"id": 7, "name": "body ache", "specialization_id": 1},
    {"id": 8, "name": "weakness", "specialization_id": 1},
    # Cardiology
    {"id": 9, "name": "chest pain", "specialization_id": 2},
    {"id": 10, "name": "palpitations", "specialization_id": 2},
    {"id": 11, "name": "shortness of breath", "specialization_id": 2},
    {"id": 12, "name": "heartburn", "specialization_id": 2},
    {"id": 13, "name": "high blood pressure", "specialization_id": 2},
    # Pediatrics
    {"id": 14, "name": "infant fever", "specialization_id": 3},
    {"id": 15, "name": "child vomiting", "specialization_id": 3},
    {"id": 16, "name": "pediatric rash", "specialization_id": 3},
    {"id": 17, "name": "teething pain", "specialization_id": 3},
    {"id": 18, "name": "childhood asthma", "specialization_id": 3},
    # Orthopedics
    {"id": 19, "name": "knee pain", "specialization_id": 4},
    {"id": 20, "name": "joint fracture", "specialization_id": 4},
    {"id": 21, "name": "backache", "specialization_id": 4},
    {"id": 22, "name": "sprain", "specialization_id": 4},
    {"id": 23, "name": "bone injury", "specialization_id": 4},
    {"id": 24, "name": "arthritis", "specialization_id": 4},
    # Dermatology
    {"id": 25, "name": "skin rash", "specialization_id": 5},
    {"id": 26, "name": "itching", "specialization_id": 5},
    {"id": 27, "name": "acne", "specialization_id": 5},
    {"id": 28, "name": "hair loss", "specialization_id": 5},
    {"id": 29, "name": "eczema", "specialization_id": 5},
    {"id": 30, "name": "dry skin", "specialization_id": 5},
    # Neurology
    {"id": 31, "name": "migraine", "specialization_id": 6},
    {"id": 32, "name": "dizziness", "specialization_id": 6},
    {"id": 33, "name": "numbness", "specialization_id": 6},
    {"id": 34, "name": "seizures", "specialization_id": 6},
    {"id": 35, "name": "tremors", "specialization_id": 6},
    {"id": 36, "name": "paralysis", "specialization_id": 6}
]

MOCK_SCHEDULES = [
    # Dr. Ranji Patel
    {"doctor_id": 1, "day_of_week": "Monday", "start_time": "09:00:00", "end_time": "13:00:00"},
    {"doctor_id": 1, "day_of_week": "Monday", "start_time": "14:00:00", "end_time": "18:00:00"},
    {"doctor_id": 1, "day_of_week": "Tuesday", "start_time": "10:00:00", "end_time": "16:00:00"},
    {"doctor_id": 1, "day_of_week": "Wednesday", "start_time": "09:00:00", "end_time": "13:00:00"},
    {"doctor_id": 1, "day_of_week": "Wednesday", "start_time": "14:00:00", "end_time": "18:00:00"},
    {"doctor_id": 1, "day_of_week": "Thursday", "start_time": "10:00:00", "end_time": "16:00:00"},
    {"doctor_id": 1, "day_of_week": "Friday", "start_time": "09:00:00", "end_time": "13:00:00"},
    {"doctor_id": 1, "day_of_week": "Friday", "start_time": "14:00:00", "end_time": "18:00:00"},
    {"doctor_id": 1, "day_of_week": "Saturday", "start_time": "09:00:00", "end_time": "13:00:00"},

    # Dr. Amit Sharma
    {"doctor_id": 2, "day_of_week": "Monday", "start_time": "10:00:00", "end_time": "14:00:00"},
    {"doctor_id": 2, "day_of_week": "Tuesday", "start_time": "10:00:00", "end_time": "14:00:00"},
    {"doctor_id": 2, "day_of_week": "Wednesday", "start_time": "10:00:00", "end_time": "14:00:00"},
    {"doctor_id": 2, "day_of_week": "Thursday", "start_time": "15:00:00", "end_time": "19:00:00"},
    {"doctor_id": 2, "day_of_week": "Friday", "start_time": "15:00:00", "end_time": "19:00:00"},

    # Dr. Sarah Johnson
    {"doctor_id": 3, "day_of_week": "Tuesday", "start_time": "09:00:00", "end_time": "15:00:00"},
    {"doctor_id": 3, "day_of_week": "Wednesday", "start_time": "09:00:00", "end_time": "15:00:00"},
    {"doctor_id": 3, "day_of_week": "Thursday", "start_time": "09:00:00", "end_time": "15:00:00"},
    {"doctor_id": 3, "day_of_week": "Saturday", "start_time": "10:00:00", "end_time": "14:00:00"},

    # Dr. Rajesh Kumar
    {"doctor_id": 4, "day_of_week": "Monday", "start_time": "13:00:00", "end_time": "18:00:00"},
    {"doctor_id": 4, "day_of_week": "Wednesday", "start_time": "13:00:00", "end_time": "18:00:00"},
    {"doctor_id": 4, "day_of_week": "Thursday", "start_time": "13:00:00", "end_time": "18:00:00"},
    {"doctor_id": 4, "day_of_week": "Friday", "start_time": "09:00:00", "end_time": "13:00:00"},

    # Dr. Priya Nair
    {"doctor_id": 5, "day_of_week": "Monday", "start_time": "11:00:00", "end_time": "16:00:00"},
    {"doctor_id": 5, "day_of_week": "Tuesday", "start_time": "11:00:00", "end_time": "16:00:00"},
    {"doctor_id": 5, "day_of_week": "Thursday", "start_time": "11:00:00", "end_time": "16:00:00"},
    {"doctor_id": 5, "day_of_week": "Friday", "start_time": "11:00:00", "end_time": "16:00:00"},

    # Dr. Vikas Gupta
    {"doctor_id": 6, "day_of_week": "Wednesday", "start_time": "10:00:00", "end_time": "17:00:00"},
    {"doctor_id": 6, "day_of_week": "Friday", "start_time": "10:00:00", "end_time": "17:00:00"},
    {"doctor_id": 6, "day_of_week": "Saturday", "start_time": "14:00:00", "end_time": "18:00:00"}
]

# ==========================================
# STRING DISTANCE & SPELLING CORRECTION
# ==========================================
def levenshtein_distance(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    if len(s2) == 0:
        return len(s1)
    
    previous_row = list(range(len(s2) + 1))
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (0 if c1 == c2 else 1)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
        
    return previous_row[-1]

def find_spelling_corrections(query):
    """
    Search known doctor names, symptoms, and specializations to find spelling corrections.
    Supports word-level tokenization for matching parts of multi-word symptoms or names.
    Returns (corrected_query, type_matched) or (None, None) if no correction is found.
    """
    if not query:
        return None, None
        
    query_clean = query.strip().lower()
    
    # 1. Retrieve all candidates
    candidates = []
    # Doctor names
    for d in MOCK_DOCTORS:
        # Strip "Dr. " prefix for matching
        name_clean = d["name"].replace("Dr. ", "").strip().lower()
        candidates.append((name_clean, d["name"], "doctor"))
        candidates.append((d["name"].lower(), d["name"], "doctor"))
        
        # Word-level tokenization for doctors
        for word in name_clean.split():
            if len(word) > 2:
                candidates.append((word, d["name"], "doctor"))
    
    # Symptoms
    for s in MOCK_SYMPTOMS:
        sym_clean = s["name"].lower()
        candidates.append((sym_clean, s["name"], "symptom"))
        
        # Word-level tokenization for symptoms (e.g. "chest", "pain", "joint")
        for word in sym_clean.split():
            if len(word) > 2:
                candidates.append((word, s["name"], "symptom"))
        
    # Specializations
    for sp in MOCK_SPECIALIZATIONS:
        spec_clean = sp["name"].lower()
        candidates.append((spec_clean, sp["name"], "specialization"))
        
        # Word-level tokenization for specializations
        for word in spec_clean.split():
            if len(word) > 2:
                candidates.append((word, sp["name"], "specialization"))

    # 2. Check direct substring match first
    for clean, orig, item_type in candidates:
        if query_clean in clean or clean in query_clean:
            return orig, item_type

    # 3. If no substring match, calculate Levenshtein distance
    best_candidate = None
    min_dist = 9999
    
    for clean, orig, item_type in candidates:
        dist = levenshtein_distance(query_clean, clean)
        # Dynamic threshold based on length of query
        threshold = 1 if len(query_clean) <= 4 else (2 if len(query_clean) <= 7 else 3)
        if dist <= threshold and dist < min_dist:
            min_dist = dist
            best_candidate = (orig, item_type)
            
    if best_candidate:
        return best_candidate
        
    return None, None

# ==========================================
# REAL-TIME AVAILABILITY HELPER (Python side)
# ==========================================
def check_mock_availability(doctor_id):
    """
    Computes doctor availability based on schedules vs current system time.
    Returns pseudo-random true/false based on doctor_id to simulate some
    available and some unavailable doctors.
    """
    import random
    rng = random.Random(doctor_id)
    return rng.choice([True, False])

def get_random_schedules(doctor_id):
    """
    Generates consistent, pseudo-random weekly schedules for a doctor.
    Seeded with doctor_id so that a doctor's consultation hours are stable
    across reloads/navigating.
    """
    import random
    rng = random.Random(doctor_id)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    num_days = rng.randint(2, 4)
    selected_days = rng.sample(days, num_days)
    
    time_slots = [
        ("09:00:00", "13:00:00"),
        ("14:00:00", "18:00:00"),
        ("10:00:00", "16:00:00"),
        ("15:00:00", "19:00:00"),
        ("11:00:00", "15:00:00")
    ]
    
    schedules = []
    for day in selected_days:
        start, end = rng.choice(time_slots)
        schedules.append({
            "day_of_week": day,
            "start_time": start,
            "end_time": end
        })
    
    day_order = {"Monday":0, "Tuesday":1, "Wednesday":2, "Thursday":3, "Friday":4, "Saturday":5, "Sunday":6}
    schedules.sort(key=lambda x: (day_order.get(x["day_of_week"], 7), x["start_time"]))
    return schedules

# ==========================================
# PUBLIC API / DB INTERFACE METHODS
# ==========================================

def get_specializations():
    """
    Fetch all specializations. Used in the Doctors dropdown list.
    """
    sql = "SELECT id, name FROM specializations ORDER BY name ASC"
    
    conn = get_connection()
    if conn is None:
        # Mock implementation
        data = sorted(MOCK_SPECIALIZATIONS, key=lambda x: x["name"])
        return data, sql
        
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            data = cursor.fetchall()
            return data, sql
    except Exception as e:
        print(f"Error executing get_specializations: {e}")
        return sorted(MOCK_SPECIALIZATIONS, key=lambda x: x["name"]), sql
    finally:
        if conn:
            conn.close()

def list_doctors(specialization_id=None):
    """
    Fetches the full list of doctors, optionally filtered by specialization_id.
    Includes inline real-time availability derived from schedules.
    """
    if specialization_id:
        sql = """SELECT DISTINCT d.id, d.name, d.qualification, d.phone, d.email, s.name AS specialization_name,
       IF(sch.id IS NOT NULL, 1, 0) AS is_available
FROM doctors d
JOIN specializations s ON d.specialization_id = s.id
LEFT JOIN schedules sch ON d.id = sch.doctor_id 
     AND UPPER(sch.day_of_week) = UPPER(DAYNAME(NOW())) 
     AND TIME(NOW()) BETWEEN sch.start_time AND sch.end_time
WHERE d.specialization_id = %s
ORDER BY d.name ASC"""
        params = (specialization_id,)
    else:
        sql = """SELECT DISTINCT d.id, d.name, d.qualification, d.phone, d.email, s.name AS specialization_name,
       IF(sch.id IS NOT NULL, 1, 0) AS is_available
FROM doctors d
JOIN specializations s ON d.specialization_id = s.id
LEFT JOIN schedules sch ON d.id = sch.doctor_id 
     AND UPPER(sch.day_of_week) = UPPER(DAYNAME(NOW())) 
     AND TIME(NOW()) BETWEEN sch.start_time AND sch.end_time
ORDER BY d.name ASC"""
        params = ()

    # Format the display SQL query with parameters replaced
    display_sql = sql
    if params:
        display_sql = sql % params

    conn = get_connection()
    if conn is None:
        # Mock implementation
        results = []
        for d in MOCK_DOCTORS:
            if specialization_id and d["specialization_id"] != int(specialization_id):
                continue
            spec = next((s for s in MOCK_SPECIALIZATIONS if s["id"] == d["specialization_id"]), None)
            spec_name = spec["name"] if spec else ""
            is_avail = 1 if check_mock_availability(d["id"]) else 0
            results.append({
                "id": d["id"],
                "name": d["name"],
                "qualification": d["qualification"],
                "phone": d["phone"],
                "email": d["email"],
                "specialization_name": spec_name,
                "is_available": is_avail
            })
        return sorted(results, key=lambda x: x["name"]), display_sql

    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, params)
            data = cursor.fetchall()
            return data, display_sql
    except Exception as e:
        print(f"Error listing doctors: {e}")
        # Fall back to mock
        return list_doctors(specialization_id) # Recursively call to get mock results if db fails mid-execution
    finally:
        if conn:
            conn.close()

def get_doctor_details(doctor_id):
    """
    Fetches full profile, schedules list, and derived availability of a single doctor.
    """
    # 1. Fetch Doctor details
    sql_doc = """SELECT d.id, d.name, d.qualification, d.phone, d.email, s.name AS specialization_name,
       IF(sch_active.id IS NOT NULL, 1, 0) AS is_available
FROM doctors d
JOIN specializations s ON d.specialization_id = s.id
LEFT JOIN schedules sch_active ON d.id = sch_active.doctor_id
     AND UPPER(sch_active.day_of_week) = UPPER(DAYNAME(NOW())) 
     AND TIME(NOW()) BETWEEN sch_active.start_time AND sch_active.end_time
WHERE d.id = %s"""
    
    # 2. Fetch Doctor's schedules
    sql_sch = "SELECT id, day_of_week, start_time, end_time FROM schedules WHERE doctor_id = %s ORDER BY FIELD(day_of_week, 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'), start_time ASC"

    display_sql = f"-- 1. Doctor Details Query:\n{sql_doc % doctor_id}\n\n-- 2. Doctor Schedules Query:\n{sql_sch % doctor_id}"

    conn = get_connection()
    if conn is None:
        # Mock implementation
        d = next((x for x in MOCK_DOCTORS if x["id"] == int(doctor_id)), None)
        if not d:
            return None, display_sql
            
        spec = next((s for s in MOCK_SPECIALIZATIONS if s["id"] == d["specialization_id"]), None)
        spec_name = spec["name"] if spec else ""
        is_avail = 1 if check_mock_availability(d["id"]) else 0
        
        doc_details = {
            "id": d["id"],
            "name": d["name"],
            "qualification": d["qualification"],
            "phone": d["phone"],
            "email": d["email"],
            "specialization_name": spec_name,
            "is_available": is_avail
        }
        
        doc_details["schedules"] = get_random_schedules(d["id"])
        return doc_details, display_sql

    try:
        with conn.cursor() as cursor:
            # Get doctor details
            cursor.execute(sql_doc, (doctor_id,))
            doc_details = cursor.fetchone()
            if not doc_details:
                return None, display_sql
                
            # Get schedules
            cursor.execute(sql_sch, (doctor_id,))
            doc_schedules = cursor.fetchall()
            
            # Format time strings
            for s in doc_schedules:
                if 'start_time' in s and s['start_time']:
                    # Convert timedelta/time objects to HH:MM string if necessary
                    if isinstance(s['start_time'], datetime.timedelta):
                        s['start_time'] = str(s['start_time'])
                    if isinstance(s['end_time'], datetime.timedelta):
                        s['end_time'] = str(s['end_time'])
            
            doc_details["schedules"] = doc_schedules
            return doc_details, display_sql
    except Exception as e:
        print(f"Error fetching doctor details: {e}")
        return None, display_sql
    finally:
        if conn:
            conn.close()

def search_doctors(search_query):
    """
    Search doctors by doctor name, symptom, or condition.
    Supports case-insensitivity, substring matching, MySQL SOUNDEX phonetic matching,
    and fallback Levenshtein distance string similarity correction.
    """
    if not search_query:
        return [], "", None

    search_query = search_query.strip()
    
    # 1. Main Search Query (Case Insensitive + Substring + SOUNDEX)
    sql = """SELECT DISTINCT d.id, d.name, d.qualification, d.phone, d.email, spec.name AS specialization_name,
       IF(sch_active.id IS NOT NULL, 1, 0) AS is_available
FROM doctors d
JOIN specializations spec ON d.specialization_id = spec.id
LEFT JOIN symptoms sym ON sym.specialization_id = spec.id
LEFT JOIN schedules sch_active ON d.id = sch_active.doctor_id 
     AND UPPER(sch_active.day_of_week) = UPPER(DAYNAME(NOW())) 
     AND TIME(NOW()) BETWEEN sch_active.start_time AND sch_active.end_time
WHERE LOWER(d.name) LIKE LOWER(CONCAT('%%', %s, '%%'))
   OR LOWER(sym.name) LIKE LOWER(CONCAT('%%', %s, '%%'))
   OR SOUNDEX(d.name) = SOUNDEX(%s)
   OR SOUNDEX(sym.name) = SOUNDEX(%s)
ORDER BY d.name ASC"""

    # For display formatting
    display_sql = sql % (f"'{search_query}'", f"'{search_query}'", f"'{search_query}'", f"'{search_query}'")
    display_sql = display_sql.replace('%%', '%')

    # Helper function to perform Python-side search logic (Mock/Fallback)
    def perform_mock_search(query):
        q = query.lower()
        results = []
        # Find matching doctor names (substring)
        matched_doctor_ids = [d["id"] for d in MOCK_DOCTORS if q in d["name"].lower()]
        
        # Find matching symptoms (substring)
        matched_symptom_spec_ids = [s["specialization_id"] for s in MOCK_SYMPTOMS if q in s["name"].lower()]
        
        # Find matching specializations (substring)
        matched_spec_ids = [sp["id"] for sp in MOCK_SPECIALIZATIONS if q in sp["name"].lower()]
        
        # Collect matched doctors
        for d in MOCK_DOCTORS:
            match = False
            # Check doctor name match
            if d["id"] in matched_doctor_ids:
                match = True
            # Check symptom specialization match
            elif d["specialization_id"] in matched_symptom_spec_ids:
                match = True
            # Check specialization match
            elif d["specialization_id"] in matched_spec_ids:
                match = True
                
            if match:
                spec = next((s for s in MOCK_SPECIALIZATIONS if s["id"] == d["specialization_id"]), None)
                spec_name = spec["name"] if spec else ""
                is_avail = 1 if check_mock_availability(d["id"]) else 0
                results.append({
                    "id": d["id"],
                    "name": d["name"],
                    "qualification": d["qualification"],
                    "phone": d["phone"],
                    "email": d["email"],
                    "specialization_name": spec_name,
                    "is_available": is_avail
                })
        return sorted(results, key=lambda x: x["name"])

    conn = get_connection()
    if conn is None:
        # Mock Search
        results = perform_mock_search(search_query)
        
        # If no results found, perform spelling correction using Levenshtein distance
        if not results:
            corrected_term, item_type = find_spelling_corrections(search_query)
            if corrected_term:
                corrected_results = perform_mock_search(corrected_term)
                # Formulate the query string for the corrected term
                corrected_sql = (sql % (f"'{corrected_term}'", f"'{corrected_term}'", f"'{corrected_term}'", f"'{corrected_term}'")).replace('%%', '%')
                return corrected_results, corrected_sql, corrected_term
        return results, display_sql, None

    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, (search_query, search_query, search_query, search_query))
            data = cursor.fetchall()
            
            # If database query succeeds but returns nothing, try spelling correction
            if not data:
                corrected_term, item_type = find_spelling_corrections(search_query)
                if corrected_term:
                    cursor.execute(sql, (corrected_term, corrected_term, corrected_term, corrected_term))
                    corrected_data = cursor.fetchall()
                    corrected_sql = (sql % (f"'{corrected_term}'", f"'{corrected_term}'", f"'{corrected_term}'", f"'{corrected_term}'")).replace('%%', '%')
                    return corrected_data, corrected_sql, corrected_term
            
            return data, display_sql, None
    except Exception as e:
        print(f"Error searching doctors: {e}")
        # Fall back to mock search recursively
        results = perform_mock_search(search_query)
        if not results:
            corrected_term, item_type = find_spelling_corrections(search_query)
            if corrected_term:
                corrected_results = perform_mock_search(corrected_term)
                corrected_sql = (sql % (f"'{corrected_term}'", f"'{corrected_term}'", f"'{corrected_term}'", f"'{corrected_term}'")).replace('%%', '%')
                return corrected_results, corrected_sql, corrected_term
        return results, display_sql, None
    finally:
        if conn:
            conn.close()
