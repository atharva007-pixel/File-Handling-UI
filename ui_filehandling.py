"""
File Handling System — Streamlit UI
A simple CRUD app for creating, reading, updating (write/rename), and deleting files.
Run with: streamlit run file_manager_app.py
"""

import os
from pathlib import Path
import streamlit as st

# ---------- Page config ----------
st.set_page_config(
    page_title="File Manager",
    page_icon="📁",
    layout="centered",
)

# ---------- Styling ----------
st.markdown("""
    <style>
        .main { padding-top: 1.5rem; }
        .stButton>button {
            width: 100%;
            border-radius: 10px;
            padding: 0.6rem 1rem;
            font-weight: 600;
            border: none;
        }
        .success-box, .error-box, .info-box {
            padding: 0.9rem 1.1rem;
            border-radius: 10px;
            margin-top: 0.8rem;
            font-size: 0.95rem;
        }
        .success-box { background-color: #e6f4ea; color: #1e7e34; border: 1px solid #b7e1c4; }
        .error-box { background-color: #fdecea; color: #b3261e; border: 1px solid #f5c2c0; }
        .info-box { background-color: #eaf1fb; color: #1a4d8f; border: 1px solid #c3d9f5; }
        h1 { font-weight: 800; }
        .subtitle { color: #6b7280; margin-top: -10px; margin-bottom: 1.5rem; }
    </style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.title("📁 File Handling System")
st.markdown('<p class="subtitle">Create, Read, Update & Delete files — right from your browser</p>', unsafe_allow_html=True)

# ---------- Helper for feedback messages ----------
def show_success(msg):
    st.markdown(f'<div class="success-box">✅ {msg}</div>', unsafe_allow_html=True)

def show_error(msg):
    st.markdown(f'<div class="error-box">❌ {msg}</div>', unsafe_allow_html=True)

def show_info(msg):
    st.markdown(f'<div class="info-box">ℹ️ {msg}</div>', unsafe_allow_html=True)

# ---------- Tabs for each operation ----------
tab_create, tab_read, tab_update, tab_delete = st.tabs(
    ["🆕 Create", "📖 Read", "✏️ Update", "🗑️ Delete"]
)

# ================= CREATE =================
with tab_create:
    st.subheader("Create a new file")
    filename = st.text_input("File name", placeholder="example.txt", key="create_name")
    content = st.text_area("File content", placeholder="Write something...", key="create_content", height=150)

    if st.button("Create File", key="create_btn"):
        if not filename.strip():
            show_error("Please enter a file name.")
        else:
            path = Path(filename)
            try:
                if path.exists():
                    show_error(f"'{filename}' already exists.")
                else:
                    path.write_text(content)
                    show_success(f"'{filename}' created successfully!")
            except Exception as err:
                show_error(f"Something went wrong: {err}")

# ================= READ =================
with tab_read:
    st.subheader("Read a file")
    filename = st.text_input("File name", placeholder="example.txt", key="read_name")

    if st.button("Read File", key="read_btn"):
        if not filename.strip():
            show_error("Please enter a file name.")
        else:
            path = Path(filename)
            try:
                if path.exists():
                    text = path.read_text()
                    show_success(f"'{filename}' loaded successfully!")
                    st.code(text if text.strip() else "(file is empty)", language=None)
                else:
                    show_error(f"'{filename}' does not exist.")
            except Exception as err:
                show_error(f"Something went wrong: {err}")

# ================= UPDATE =================
with tab_update:
    st.subheader("Update a file")
    action = st.radio("What do you want to do?", ["Rename file", "Append content"], key="update_action")
    filename = st.text_input("Existing file name", placeholder="example.txt", key="update_name")

    if action == "Rename file":
        new_name = st.text_input("New file name", placeholder="new_name.txt", key="update_newname")
        if st.button("Rename", key="rename_btn"):
            if not filename.strip() or not new_name.strip():
                show_error("Please fill in both file names.")
            else:
                path, new_path = Path(filename), Path(new_name)
                try:
                    if not path.exists():
                        show_error(f"'{filename}' does not exist.")
                    elif new_path.exists():
                        show_error(f"'{new_name}' already exists.")
                    else:
                        path.rename(new_path)
                        show_success(f"Renamed '{filename}' → '{new_name}'")
                except Exception as err:
                    show_error(f"Something went wrong: {err}")

    else:  # Append content
        extra_content = st.text_area("Content to append", placeholder="Add more text...", key="update_content", height=120)
        if st.button("Append", key="append_btn"):
            if not filename.strip():
                show_error("Please enter a file name.")
            else:
                path = Path(filename)
                try:
                    if not path.exists():
                        show_error(f"'{filename}' does not exist.")
                    else:
                        with open(path, "a") as f:
                            f.write(extra_content)
                        show_success(f"Content appended to '{filename}'")
                except Exception as err:
                    show_error(f"Something went wrong: {err}")

# ================= DELETE =================
with tab_delete:
    st.subheader("Delete a file")
    filename = st.text_input("File name", placeholder="example.txt", key="delete_name")

    confirm = st.checkbox("I understand this action cannot be undone")

    if st.button("Delete File", key="delete_btn", disabled=not confirm):
        if not filename.strip():
            show_error("Please enter a file name.")
        else:
            path = Path(filename)
            try:
                if path.exists():
                    os.remove(path)
                    show_success(f"'{filename}' deleted successfully.")
                else:
                    show_error(f"'{filename}' does not exist.")
            except Exception as err:
                show_error(f"Something went wrong: {err}")

# ---------- Footer ----------
st.markdown("---")
show_info("Built with Python & Streamlit — a simple File Handling CRUD system.")