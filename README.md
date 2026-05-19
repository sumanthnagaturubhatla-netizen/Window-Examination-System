# Window Examination System using Tkinter and MySQL

## Overview

The Window Examination System is a desktop-based examination management application developed using Python Tkinter for graphical user interface design and MySQL for database management. The system automates the examination process by providing a secure and interactive platform for conducting computer-based tests.

The application contains multiple sections including Arithmetic, Reasoning, and English with automated score calculation and result evaluation. Candidate details and examination scores are stored securely in the MySQL database for future reference.

---

# Features

* Student Login Authentication
* Multi-Section Examination System
* Arithmetic, Reasoning, and English Sections
* Real-Time Score Calculation
* Automated Result Evaluation
* Pass/Fail Status Display
* MySQL Database Integration
* GUI-based Examination Interface
* Anti-Malpractice Agreement Checkboxes
* Error Handling and Input Validation

---

# Tech Stack

## Frontend

* Python Tkinter

## Backend

* Python

## Database

* MySQL

## Additional Libraries

* mysql-connector-python
* functools.partial

---

# Project Structure

```bash id="2o8g2w"
Window-Examination-System/
│
├── main.py
├── arithmetic_section.py
├── reasoning_section.py
├── english_section.py
├── database.py
├── assets/
└── README.md
```

---

# Modules Included

## 1. Login Module

* Validates Hall Ticket Number and Candidate Name
* Prevents unauthorized access

## 2. Exam Instructions Module

* Displays exam rules and guidelines
* Requires agreement confirmation before starting exam

## 3. Arithmetic Section

* Contains aptitude-based arithmetic questions
* Multiple-choice format

## 4. Reasoning Section

* Logical reasoning and puzzle-based questions

## 5. English Section

* Grammar and vocabulary-based questions

## 6. Result Module

* Displays total score
* Shows qualification status based on score

## 7. Database Module

* Stores student details and scores in MySQL

---

# Database Table

```sql id="n9r3tw"
CREATE TABLE student_scores (

    hall_ticket_number VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100),
    score INT

);
```

---

# Installation

## Install Required Package

```bash id="u8e0bm"
pip install mysql-connector-python
```

---

# Configure MySQL Database

```sql id="j3l6vq"
CREATE DATABASE crttext;
```

Use the database before running the project.

---

# Run the Application

```bash id="x7h2eo"
python main.py
```

---

# Working of the Application

1. Student enters Hall Ticket Number and Name.
2. System validates candidate details.
3. Exam instructions are displayed.
4. Student agrees to exam guidelines.
5. Examination begins with multiple sections.
6. User answers multiple-choice questions.
7. Score is calculated automatically.
8. Result is displayed instantly.
9. Student score is stored in MySQL database.

---

# Key Functionalities

* Automated Digital Examination
* Interactive GUI Interface
* Real-Time Score Tracking
* Database Connectivity
* Error Handling
* Section-wise Navigation
* Pass/Fail Evaluation

---

# Learning Outcomes

* Python GUI Development using Tkinter
* MySQL Database Integration
* Event-Driven Programming
* Form Validation
* Examination System Development
* Desktop Application Design

---

# Future Enhancements

* Admin Dashboard
* Timer-Based Exams
* Dynamic Question Management
* Student Registration System
* Randomized Questions
* Performance Analytics

---

# Authors

* Turubhatla Naga Sumanth


---
