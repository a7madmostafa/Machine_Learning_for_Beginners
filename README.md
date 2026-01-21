# 🧠 Machine Learning for Beginners  
*A complete hands-on journey: from idea → data → model → web app*

This project is designed for **absolute beginners in Machine Learning**.  
You only need **basic Python** — no math, no ML background.

By the end, you will:
- Understand what Machine Learning really is
- Work with real-world customer data
- Train a churn prediction model
- Make predictions using the model
- Run a simple Machine Learning web app

---

## 📁 Project Structure

```
.
├── 01_load_and_recognize_data.ipynb        # Understanding the problem and data
├── 02_train_and_evaluate.ipynb             # Training, evaluation, saving the model
├── 03_use_model_and_predict.ipynb          # Using the saved model
├── app.py                                  # Streamlit web app
├── data/
│   └── churn.csv                           # Dataset (past customer examples)
├── model/
│   └── churn_pipeline.joblib               # Saved ML pipeline
├── requirements.txt                        # Required libraries
└── README.md                               # This guide
```
---

## 🛠️ Step 1: Install the Basics

### 1️⃣ Install Python (3.11 recommended)
- Download from: https://www.python.org/downloads/
- During installation (Windows): ✅ **Check “Add Python to PATH”**

Verify installation:
```bash
python --version
```

### 2️⃣ Install VS Code
- Download from: https://code.visualstudio.com/
- Install the **Python extension** in VS Code

### 3️⃣ Install Git and Download the Project
- Download Git from: https://git-scm.com/downloads
- Open terminal (Command Prompt / PowerShell / Terminal) and run:
```bash
git --version
```
- Clone the project repository:
```bash
git clone https://github.com/a7madmostafa/Machine_Learning_for_Beginners
```

- Navigate into the project folder:
```bash
cd Machine_Learning_for_Beginners
```

- Open VS Code
```bash
code .
```

### 4️⃣ Create and Activate a Virtual Environment (Python 3.11)

- Open the terminal in VS Code (``` Ctrl + ` ``` or View → Terminal) and run:
```bash
pip install uv
```

- Create the virtual environment:
```bash
uv -p python3.11 .venv
```

- Activate the virtual environment for MacOS/Linux:
```bash
source .venv/bin/activate 
```
- Activate the virtual environment for Windows:
```bash
.venv\Scripts\activate 
```
> We are using `uv` to create a virtual environment with Python 3.11 and activate it. You should see `(.venv)` in the terminal, indicating the virtual environment is active.

- Install the Requirements
```bash
uv pip install -r requirements.txt
```

## 🚀 Step 2: Run the Notebooks

⚠️ **Important:** Run the notebooks in this exact order.

### 1️⃣ `01_load_and_recognize_data.ipynb`

**You will learn:**
- What the business problem is (customer churn)
- How data represents real customers
- How to inspect, clean, and understand a dataset
- How Machine Learning “sees” data

### 2️⃣ `02_train_and_evaluate.ipynb`

**You will learn:**
- What features (X) and labels (y) are
- How a model learns from data
- What training and testing mean
- How to evaluate a model properly
- How to save a trained model

### 3️⃣ `03_use_model_and_predict.ipynb`

**You will learn:**
- How to load a saved model
- How to make predictions on new customers
- What probabilities mean in Machine Learning
- How ML decisions are actually made

## 🎉 Congratulations! 
Now, you can run the web app `app.py`

To run the app, use the terminal in VS Code and run:
```bash
streamlit run app.py
``` 
Then, open the provided local URL in your browser to interact with the app.

### 🌐 What You Will See in the Web App

- Input fields for customer data  
- A **Predict Churn** button  
- A prediction: **Yes / No**  
- A confidence score (probability)

🎉 You just used a **Machine Learning model inside a web app**.

## 🧠 How to Study This Project (Important)

- Read the **PDF first** (concepts come before code)
- Run notebooks **slowly**, cell by cell
- Don’t just run — ask **“why?”**
- Change values and observe what happens
- Break things safely — that’s how learning works


## ✅ By the End, You Will Be Able To

- Explain Machine Learning in simple words
- Understand how models learn from data
- Train and evaluate a supervised ML model
- Avoid common beginner mistakes
- Turn a model into a usable web application

This is **real Machine Learning**, explained gently.

Happy learning 🚀
