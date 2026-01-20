# Machine_Learning_for_Beginners


## 🚀 Step-by-step: use VS Code in GitHub Codespaces

GitHub Codespaces gives you a ready-to-use VS Code environment in the browser (no local setup).

### 1) Create a Codespace
1. Open the GitHub repo in your browser
2. Click **Code → Codespaces → Create codespace on main**
3. Wait until VS Code opens (usually less than a minute)

✅ Now your repo is already cloned inside VS Code.

---

### 2) Check Python version
Open the terminal inside Codespaces and run:
```bash
python --version
```

### 3) Create & activate a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

### 4) Install requirements
```bash
pip install -r requirements.txt
```

### 5) Run the Streamlit app
```bash
streamlit run app.py
```