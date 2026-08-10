# File-Handling-UI
# 📁 File Handling UI

A simple, clean **CRUD (Create, Read, Update, Delete)** file management app built with **Python** and **Streamlit**.

Started as a terminal-based script and evolved into a full browser UI — built to practice core file handling operations (`Path`, `open`, `os.remove`) with proper error handling and a user-friendly interface.

## 🚀 Live Demo

👉 [Try it here](#) <!-- replace with your Streamlit Cloud link -->

## ✨ Features

- 🆕 **Create** — make a new file and write content to it
- 📖 **Read** — view the contents of any existing file
- ✏️ **Update** — rename a file, or append new content to it
- 🗑️ **Delete** — remove a file (with a confirmation check)
- Clean tabbed interface with success/error feedback for every action

## 🛠️ Built With

- [Python](https://www.python.org/) — core logic (`pathlib`, `os`)
- [Streamlit](https://streamlit.io/) — web UI

## ▶️ Run It Locally

```bash
git clone https://github.com/atharva007-pixel/File-Handling-UI.git
cd File-Handling-UI
pip install -r requirements.txt
streamlit run ui_filehandling.py
```

## 📌 Note

Files created through this app are stored in the app's runtime environment. On free cloud hosting, this storage is temporary and resets when the app restarts — this project is meant as a UI/CRUD demo, not permanent file storage.

## 📚 What I Learned

- Handling file operations safely with `pathlib` and `try/except`
- Converting a CLI script into an interactive web UI
- Deploying a Python app to the cloud with Streamlit Community Cloud

---

⭐ If you found this useful, feel free to star the repo!
