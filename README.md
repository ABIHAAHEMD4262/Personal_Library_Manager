# 📚 Personal Library Manager

A simple and beautiful web application to manage your personal book collection — built with **Python, Streamlit, and Object-Oriented Programming (OOP)**.

---

## 🚀 Features

- ➕ Add new books (title, author, year, genre, read/unread)
- ❌ Remove books by title
- 🔍 Search books by title or author
- 📋 View all books in your collection
- 📊 See stats like how many books you've read

---

## 🛠️ Tech Stack

- **Python 3**
- **Streamlit** – for building the interactive web app
- **OOP (Object-Oriented Programming)** – for organizing your code using `Book` and `LibraryManager` classes

---

## 📦 Installation

1. ✅ Make sure you have Python installed.
2. 💻 Open your terminal or Anaconda command prompt.
3. Install Streamlit using `uv`:

   ```bash
   uv add streamlit


▶️ How to Run
Once installed, run the app using:

bash
Copy
Edit
streamlit run app.py
This will open the web app in your browser at:

arduino
Copy
Edit
http://localhost:8501
🧠 How It Works
The app uses Python classes to manage books as objects.

Streamlit handles the UI — forms, buttons, and layout.

Books are temporarily stored in memory (you can extend it to save/load from a file).

📌 Project Structure
bash
Copy
Edit
personel_library_manager/
│
├── app.py          # Main Streamlit application
└── README.md       # Project description and instructions

