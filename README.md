# 📚 Virtual Bookshelf

A simple and modern digital bookshelf built with **Flask**, **SQLAlchemy**, and **SQLite**.  
It allows you to **add, edit, search, sort, and delete books**, all through a clean Bootstrap‑powered interface featuring **cards**, **star ratings**, **modals**, and **dark mode**.

---

## 🚀 Features

- Add books with title, author, and a 1–5 ⭐ rating  
- Edit all book fields  
- Delete books with confirmation modal  
- Search by title or author  
- Sort by title or rating  
- Combine search + sorting  
- Responsive card layout  
- Star‑based rating display  
- Bootstrap 5 UI with icons  
- Optional dark mode toggle  

---

## 🛠️ Tech Stack

- Python 3  
- Flask  
- SQLAlchemy 2.0  
- SQLite  
- Bootstrap 5  
- Bootstrap Icons  

---

## 📦 Installation

```bash
git clone <repository-url>
cd virtual-bookshelf
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
# or
.venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, install manually:

```bash
pip install flask flask_sqlalchemy
```

---

## ▶️ Running the App

```bash
python main.py
```

Visit:

```
http://127.0.0.1:5000
```

---

## 🗄️ Database Model

The app uses a single table: **books**

| Field  | Type   | Description          |
|--------|--------|----------------------|
| id     | int    | Primary key          |
| title  | string | Book title           |
| author | string | Book author          |
| rating | float  | Rating (1–5 stars)   |

---

## 📁 Project Structure

```
virtual-bookshelf/
│
├── main.py
├── new-books-collection.db
│
└── templates/
    ├── base.html
    ├── index.html
    ├── add.html
    └── edit.html
```

---

## 🌐 Routes

### `/`
Displays all books with search, sorting, and card layout.

### `/add`
Form to add a new book.

### `/edit/<id>`
Edit an existing book.

### `/delete/<id>`
Delete a book with confirmation modal.

---

## 🎨 UI Highlights

- Bootstrap 5 layout  
- Cards with shadows  
- Gold star ratings  
- Icons for actions  
- Delete confirmation modal  
- Dark mode toggle  
- Fully responsive design