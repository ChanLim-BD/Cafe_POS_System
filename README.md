# Cafe_POS_System

![Image](https://github.com/user-attachments/assets/aec5899f-74db-4208-89d6-fdba170cc9b8)

"내가 만약... 카페 사장이라면..."

---

## 🛠️ **Technology Stack**

- **Backend**: Django (Python) + Channels
- **Database**: SQLite3 (-> PostgreSQL soon...)

---

## 🖥️ **Getting Started**

Clone the repository and set up locally:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/ChanLim-BD/Cafe_POS_System.git
   ```

2. **Install Dependencies**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set Up the Database**

   ```bash
   python manage.py migrate
   ```

4. **Run the Server**

   ```bash
   python manage.py runserver            # 개발 서버
   ```

5. Open your browser and navigate to: `http://localhost:8000/`.
---