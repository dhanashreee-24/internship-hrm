# 🧑‍💼 Internship HRM System

A Django + Bootstrap-based Human Resource Management (HRM) system developed as part of an internship program. This project allows administrators to manage departments, assign roles, and structure the organization effectively.

---

## 🚀 Features

- Create, edit, and soft delete departments
- Status-based department activation/inactivation
- Admin-only access control for department management
- User-friendly forms with Bootstrap styling
- Structured dashboard for department operations
- Soft delete warns about employee-department relations

---

## 🛠 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Database:** SQLite (can be switched to MySQL/PostgreSQL)
- **Version Control:** Git & GitHub

---

## 📁 Folder Structure

internship/
├── department/
│ ├── migrations/
│ ├── templates/
│ │ └── department/
│ │ ├── create.html
│ │ ├── edit.html
│ │ └── dashboard.html
│ ├── admin.py
│ ├── models.py
│ ├── urls.py
│ └── views.py
├── internship/
│ ├── settings.py
│ ├── urls.py
│ └── ...
└── manage.py

---

## ⚙️ How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/dhanashreee-24/internship-hrm.git
   cd internship-hrm
2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # for Windows Install dependencies

3. **Install Dependencies**
   ```bash
   pip install django pillow

5. **Apply migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate

6. **Run the server**
   ```bash
   python manage.py runserver

7. **Access the app**
   Visit http://localhost:8000

## ✅ Internship Guidelines Followed

- Delivered working modules: Create, Edit, Delete Department  
- Used Bootstrap for frontend  
- Hosted code on GitHub  
- End-user documentation included  
- Soft delete implemented with `status` field  
- Validations and feedback messages added  

---

## 📌 Note

- Only **Admins** can access department management features  
- Soft delete logic ensures employee reassignment before inactivation  
- UI is responsive and built for ease-of-use  

---

## 🧑‍💻 Author

**Dhanashree Hankare**  
[GitHub Profile](https://github.com/dhanashreee-24)

---

## 📄 License

This project is part of an internship assignment and is not intended for production use.  
Feel free to use it for learning purposes.




