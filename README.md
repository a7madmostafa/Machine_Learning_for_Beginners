# Machine Learning for Beginners — Learner Guide

Welcome 👋  
This repository is a **step-by-step guide** to understanding Machine Learning using a real-world example: **customer churn**.

You don’t need:
- math background
- prior ML knowledge
- complex setup

You *will* learn:
- how ML thinks
- how data becomes predictions
- how to train and evaluate a model
- how to use the model in a simple web app

Take it slow. Run things in order. No shortcuts.


## 🧭 How to Use This Guide (Important)

👉 **Follow the steps in order**  
👉 **Run notebooks from top to bottom**  
👉 **Do not skip notebooks**

Each notebook builds understanding — not just code.

---

## 🚀 Step-by-step: Open the Project in VS Code (GitHub Codespaces)

We use **GitHub Codespaces** so you don’t need to install anything on your computer.

### Step 1 — Create a Codespace
1. Open this GitHub repository in your browser
2. Click **Code → Codespaces → Create codespace on main**
3. Wait until VS Code opens (usually less than a minute)

✅ You are now inside VS Code with the project ready.


### 🐍 Step 2 — Check Python

Open the terminal in VS Code and run:
```bash
python --version
```
You should see a Python version (3.10 or higher is fine).


### 📦 Step 3 — Create a Virtual Environment
We use a virtual environment to keep things clean and isolated.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

If VS Code asks you to select a Python interpreter, choose the one inside .venv.

### 📥 Step 4 — Install Required Libraries

```bash
pip install -r requirements.txt
```

This installs everything needed for:

+ data handling
+ machine learning
+ notebooks
+ the web app

## 📘 Learning Path (Very Important)

You will work through **three notebooks**.  
👉 **Run them in this exact order.**

### 1️⃣ `01_story_to_data.ipynb`
**Goal:** Understand the problem *before* touching machine learning.

You will learn:
- what customer churn means  
- how a business problem becomes an ML problem  
- how data represents past examples  
- what are **inputs (X)** and **output (y)**  

🚫 No training yet. This notebook is about **understanding**, not modeling.

### 2️⃣ `02_train_and_evaluate.ipynb`
**Goal:** Train your first real machine learning model.

You will learn:
- why we split data into **train** and **test**  
- what a **pipeline** is and why we use it  
- how a model learns from examples  
- how predictions are made  
- how to evaluate using **accuracy**  
- how to **save the trained pipeline**  

✅ At the end of this notebook, a file is saved:

```
model/churn_pipeline.joblib
```
This file contains everything the model needs.

### 3️⃣ 03_save_model_and_app.ipynb
Goal: Use the trained model like a real product.

You will learn:
+ how to load a saved ML pipeline
+ how to predict for a new customer
+ how this connects to a web app

🚫 No retraining here. We reuse what we already built.

### 🌐 Final Step — Run the Web App
After you finish Notebook 02, run:

```
streamlit run app.py
```

**What happens next:**

- Streamlit starts a small web server  
- VS Code detects a forwarded port (usually **8501**)  
- Click **Open in Browser**

**You will see:**
- input fields for customer data  
- a **Predict Churn** button  
- a prediction with its probability  

🎉 You have just used a machine learning model inside a web app.


📂 Project Structure (What Each Part Is For)

```
.
├── 01_story_to_data.ipynb        # Understanding the problem and data
├── 02_train_and_evaluate.ipynb  # Training, evaluation, saving the model
├── 03_save_model_and_app.ipynb  # Using the saved model
├── app.py                       # Streamlit web app
├── data/
│   └── churn.csv                # Dataset (past customer examples)
├── model/
│   └── churn_pipeline.joblib    # Saved ML pipeline
├── requirements.txt             # Required libraries
└── README.md                    # This guide
```
---

## ✅ By the End, You Will Be Able To

- explain what machine learning is (in simple words)
- understand how models learn from data
- train and evaluate a supervised ML model
- avoid common beginner mistakes
- turn a model into a usable web app

This is **real machine learning**, explained gently.

Take your time:
- read the markdown cells
- run the code
- ask **“why”**, not just **“how”**

Happy learning 🚀
