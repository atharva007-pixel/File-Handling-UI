# 📁 File Handling UI

A **CRUD (Create, Read, Update, Delete)** file manager with a clean Streamlit interface. Built to practice Python's `pathlib` and `os` modules with proper error handling and a polished UI.

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://python.org)

---

## ✨ Features

| Operation | Details |
|-----------|---------|
| **🆕 Create** | New file with custom name & content |
| **📖 Read** | View full file contents with syntax highlighting |
| **✏️ Update** | Rename files OR append content to existing files |
| **🗑️ Delete** | Remove files with confirmation checkbox |
| **Feedback** | Color-coded success/error/info toasts for every action |

---

## 🚀 Quick Start

```bash
git clone https://github.com/atharva007-pixel/File-Handling-UI.git
cd File-Handling-UI
pip install -r requirements.txt
streamlit run ui_filehandling.py
```

---

## 📦 Deploy Free (Streamlit Cloud)

Same as Expense Tracker — push to GitHub, connect at [share.streamlit.io](https://share.streamlit.io), set main file to `ui_filehandling.py`.

---

## 🗂 Project Structure

```
File-Handling-UI/
├── ui_filehandling.py   # Main app (4 tabs: Create/Read/Update/Delete)
├── requirements.txt     # streamlit
└── README.md
```

---

## 🛠 Tech Stack

- **Streamlit** — tabbed UI, forms, buttons, code display
- **pathlib** — modern, cross-platform file operations
- **os** — file removal, path handling
- **Custom CSS** — styled feedback boxes, polished buttons

---

## 💡 What I Learned

- Safe file operations with `try/except` and `pathlib.Path`
- Converting CLI logic → interactive web UI
- Streamlit session state patterns
- Deploying Python apps to free cloud hosting

---

## 📸 Screenshots

| Create Tab | Read Tab | Update Tab | Delete Tab |
|------------|----------|------------|------------|
| ![Create](https://via.placeholder.com/300x200?text=Create) | ![Read](https://via.placeholder.com/300x200?text=Read) | ![Update](https://via.placeholder.com/300x200?text=Update) | ![Delete](https://via.placeholder.com/300x200?text=Delete) |

---

## 🤝 Extending Ideas

- File type icons & preview (images, PDFs, code)
- Directory tree navigation
- Bulk operations (rename/move multiple)
- Search within file contents
- Download files from UI

---

## 📄 License

MIT

---

> Built by [@atharva007-pixel](https://github.com/atharva007-pixel) · Learning project · Python `pathlib` + Streamlit