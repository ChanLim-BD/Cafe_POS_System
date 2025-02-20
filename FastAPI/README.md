# Cafe_POS_System

![Image](https://github.com/user-attachments/assets/aec5899f-74db-4208-89d6-fdba170cc9b8)

"내가 만약... 카페 사장이라면..."

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

3. **Create .env**

   ```conf
   DATABASE_CONN=""
   SECRET_KEY=""
   ALGORITHM=""
   ACCESS_TOKEN_EXPIRE_MINUTES=""
   ```


4. **Set Up the Database**

   ```bash
   docker run --name mysql-container -e MYSQL_ROOT_PASSWORD="What you want" -p 3306:3306 -d mysql:latest
   ```

5. **Run the Server**

   ```bash
   uvicorn main:app --port=8081 --reload
   ```

6. Open your browser and navigate to: `http://localhost:8081/`.

---