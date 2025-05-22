# 🚀 Prototype

## 📁 Project Structure

```
prototype/
├── app.py              # Main application code
├── features/           # Documentation for implementing the remaining features
├── data/               # Data being rendered on the page in JSON format
├── utils/              # Utility functions and scripts
├── templates/          # HTML templates
├── static/             # CSS, JS, images
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## 🔧 Prerequisites

- [Python 3.10+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)
- A code editor (e.g., [VS Code](https://code.visualstudio.com/))

---

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/anish-107/prototype.git
cd prototype
```

> Note : Consider forking the repository first if you plan to contribute.

---

### 2️⃣ Create & Activate a Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Application Locally

```bash
python app.py
```

Visit the app at: [http://localhost:5000](http://localhost:5000)

## To make the website available to all the devices on the same network run :
```bash
flask run --host=0.0.0.0
```

---

## 🤝 How to Contribute

Contributions are welcome! Here's how to get started:

1. **Fork** the repository
2. **Clone** your fork locally
3. **Create a new branch** for your feature or fix  
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make your changes**, then **commit** them  
   ```bash
   git add .
   git commit -m "Add: your description here"
   ```
5. **Push** your branch to your fork  
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Open a Pull Request** on GitHub from your forked repo

---

## 🔄 Syncing with the Original Repo

To keep your fork up to date:

```bash
git remote add upstream https://github.com/anish-107/prototype.git
git fetch upstream
git checkout master
git merge upstream/master
git push origin master
```

---

## 📦 Updating `requirements.txt`

If you add or update Python packages:

```bash
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Update dependencies"
git push
```
