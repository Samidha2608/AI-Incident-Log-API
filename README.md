
# AI Incident Log API 🛠️

This is a simple API project where i have created incident logging system  
where you can create incidents, list them, delete them using Django and DRF.

---

## 🛠 Tech Stack / Dependencies

- **Python** (3.8 or newer)
- **Django** (3.2 or newer)
- **Django REST Framework**
- **SQLite** (comes with Python no need to install separately)

---

## 🚀 How to Run it Locally

1. clone the repo (or download zip whatever u like):

   ```bash
   git clone <repo-link-here>
   cd incident_log
   ```

2. create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # for Linux/mac
   venv\Scripts\activate     # for Windows
   ```

3. install the required packages:

   ```bash
   pip install django djangorestframework
   ```

4. make the migrations and migrate:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. run the server:

   ```bash
   python manage.py runserver
   ```

6. now open your browser and go to:

   ```
   http://127.0.0.1:8000/
   ```

   (it will auto redirect to `/api/incidents/`)

---

## 📚 API Endpoints

| Method | Endpoint                   | Description                |
|-------|-----------------------------|-----------------------------|
| GET   | `/api/incidents/`            | List all incidents         |
| POST  | `/api/incidents/`            | Create a new incident      |
| GET   | `/api/incidents/<id>/`        | Get a specific incident    |
| DELETE| `/api/incidents/<id>/`        | Delete a specific incident |

---

![Image](homeassignment/screencapture-127-0-0-1-8000-api-incidents-2025-04-27-21_20_02.png)
![Image](homeassignment/screencapture-127-0-0-1-8000-api-incidents-2-2025-04-27-21_20_32.png)



## 🔥 Bonus (Dev Notes)

- this project uses class based views (APIView) from DRF
- simple SQLite database is used no complex setups
- urls are neatly organized and documented
- project is ready for expanding into bigger systems too if needed later

---

## ❤️ Thanks

made with lot of chai ☕ and bugs 🐛  
hope you like it.  
By- Samidha Killedar


---
