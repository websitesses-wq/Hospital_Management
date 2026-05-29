-- Hospital Management System Seed Data
USE hospital_db;

-- Clear existing data (in correct order of dependencies)
SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE schedules;
TRUNCATE TABLE symptoms;
TRUNCATE TABLE doctors;
TRUNCATE TABLE specializations;
SET FOREIGN_KEY_CHECKS = 1;

-- 1. Insert Specializations
INSERT INTO specializations (id, name) VALUES
(1, 'General Medicine'),
(2, 'Cardiology'),
(3, 'Pediatrics'),
(4, 'Orthopedics'),
(5, 'Dermatology'),
(6, 'Neurology');

-- 2. Insert Doctors
INSERT INTO doctors (id, name, specialization_id, qualification, phone, email) VALUES
(1, 'Dr. Ranji Patel', 1, 'MD - General Medicine, MBBS', '+91 98190 12345', 'ranji.patel@cityline.com'),
(2, 'Dr. Amit Sharma', 2, 'DM - Cardiology, MD, MBBS', '+91 98200 23456', 'amit.sharma@cityline.com'),
(3, 'Dr. Sarah Johnson', 3, 'MD - Pediatrics, DCH, MBBS', '+91 98330 34567', 'sarah.johnson@cityline.com'),
(4, 'Dr. Rajesh Kumar', 4, 'MS - Orthopedics, MBBS', '+91 98210 45678', 'rajesh.kumar@cityline.com'),
(5, 'Dr. Priya Nair', 5, 'MD - Dermatology & Venereology, MBBS', '+91 98920 56789', 'priya.nair@cityline.com'),
(6, 'Dr. Vikas Gupta', 6, 'DM - Neurology, MD, MBBS', '+91 98110 67890', 'vikas.gupta@cityline.com');

-- 3. Insert Symptoms (maps symptoms/conditions to specializations)
INSERT INTO symptoms (id, name, specialization_id) VALUES
-- General Medicine
(1, 'fever', 1),
(2, 'cold', 1),
(3, 'cough', 1),
(4, 'headache', 1),
(5, 'stomach pain', 1),
(6, 'fatigue', 1),
(7, 'body ache', 1),
(8, 'weakness', 1),
-- Cardiology
(9, 'chest pain', 2),
(10, 'palpitations', 2),
(11, 'shortness of breath', 2),
(12, 'heartburn', 2),
(13, 'high blood pressure', 2),
-- Pediatrics
(14, 'infant fever', 3),
(15, 'child vomiting', 3),
(16, 'pediatric rash', 3),
(17, 'teething pain', 3),
(18, 'childhood asthma', 3),
-- Orthopedics
(19, 'knee pain', 4),
(20, 'joint fracture', 4),
(21, 'backache', 4),
(22, 'sprain', 4),
(23, 'bone injury', 4),
(24, 'arthritis', 4),
-- Dermatology
(25, 'skin rash', 5),
(26, 'itching', 5),
(27, 'acne', 5),
(28, 'hair loss', 5),
(29, 'eczema', 5),
(30, 'dry skin', 5),
-- Neurology
(31, 'migraine', 6),
(32, 'dizziness', 6),
(33, 'numbness', 6),
(34, 'seizures', 6),
(35, 'tremors', 6),
(36, 'paralysis', 6);

-- 4. Insert Schedules (day_of_week, start_time, end_time)
INSERT INTO schedules (doctor_id, day_of_week, start_time, end_time) VALUES
-- Dr. Ranji Patel (General Medicine) - Available most weekdays
(1, 'Monday', '09:00:00', '13:00:00'),
(1, 'Monday', '14:00:00', '18:00:00'),
(1, 'Tuesday', '10:00:00', '16:00:00'),
(1, 'Wednesday', '09:00:00', '13:00:00'),
(1, 'Wednesday', '14:00:00', '18:00:00'),
(1, 'Thursday', '10:00:00', '16:00:00'),
(1, 'Friday', '09:00:00', '13:00:00'),
(1, 'Friday', '14:00:00', '18:00:00'),
(1, 'Saturday', '09:00:00', '13:00:00'),

-- Dr. Amit Sharma (Cardiology) - Mon to Wed mornings, Thu/Fri evenings
(2, 'Monday', '10:00:00', '14:00:00'),
(2, 'Tuesday', '10:00:00', '14:00:00'),
(2, 'Wednesday', '10:00:00', '14:00:00'),
(2, 'Thursday', '15:00:00', '19:00:00'),
(2, 'Friday', '15:00:00', '19:00:00'),

-- Dr. Sarah Johnson (Pediatrics) - Midday Tue/Wed/Thu, Sat morning
(3, 'Tuesday', '09:00:00', '15:00:00'),
(3, 'Wednesday', '09:00:00', '15:00:00'),
(3, 'Thursday', '09:00:00', '15:00:00'),
(3, 'Saturday', '10:00:00', '14:00:00'),

-- Dr. Rajesh Kumar (Orthopedics) - Afternoon Mon/Wed/Thu, Morning Fri
(4, 'Monday', '13:00:00', '18:00:00'),
(4, 'Wednesday', '13:00:00', '18:00:00'),
(4, 'Thursday', '13:00:00', '18:00:00'),
(4, 'Friday', '09:00:00', '13:00:00'),

-- Dr. Priya Nair (Dermatology) - Mon, Tue, Thu, Fri midday
(5, 'Monday', '11:00:00', '16:00:00'),
(5, 'Tuesday', '11:00:00', '16:00:00'),
(5, 'Thursday', '11:00:00', '16:00:00'),
(5, 'Friday', '11:00:00', '16:00:00'),

-- Dr. Vikas Gupta (Neurology) - Full day Wed/Fri, Sat afternoon
(6, 'Wednesday', '10:00:00', '17:00:00'),
(6, 'Friday', '10:00:00', '17:00:00'),
(6, 'Saturday', '14:00:00', '18:00:00');
