# 📨 Flask Message App with Docker

This is a simple Flask-based web app where users can submit their **name** and **message**, and it runs inside a Docker container. This project is ideal for beginners learning **Docker**, **Flask**, and **GitHub deployment**.

---

## 📌 Features

* Simple HTML form to submit name & message.
* Built with Flask (Python).
* Containerized using Docker.
* Can be accessed on other devices via IP.
* Deployable on Docker Hub & GitHub.

---

## 🛠️ Tech Stack

* 🐍 Python + Flask
* 🐳 Docker
* 🧰 Git & GitHub

---

## 📁 Project Structure

```
flask-msg-docker/
├── app.py              # Main Flask application
├── Dockerfile          # Docker instructions
├── page.html           # HTML form template
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

---

## 🚀 Getting Started

Follow these steps to run the project on your system.

---

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Rohitt-Rajj/flask-msg-docker.git
cd flask-msg-docker
```

---

### 2️⃣ Create `requirements.txt`

Make sure this file contains:

```text
Flask==2.3.2
```

---

### 3️⃣ Create `app.py`

```python
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('page.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    message = request.form['message']
    return f"<h1>Thanks, {name}!</h1><p>Your message: {message}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

---

### 4️⃣ Create `page.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Leave a Message</title>
</head>
<body>
    <h2>Leave a Message</h2>
    <form action="/submit" method="POST">
        <label for="name">Name:</label><br />
        <input type="text" name="name" required /><br /><br />
        <label for="message">Message:</label><br />
        <textarea name="message" required></textarea><br /><br />
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

---

### 5️⃣ Create `Dockerfile`

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["python", "app.py"]
```

---

### 6️⃣ Build Docker Image

```bash
docker build -t flask-msg-app .
```

---

### 7️⃣ Run Docker Container

```bash
docker run -d -p 5000:5000 flask-msg-app
```

---

### 🌐 Access the App

Open browser and go to:

```
http://localhost:5000
```

To access from other devices on the same network:

1. Run:

```bash
ip a  # Get your local IP (e.g., 192.168.X.X)
```

2. Then open:

```
http://<your-ip>:5000
```


```

---

## 🙇‍♂️ Author

**Rohit Raj**
DevOps & Cloud Enthusiast
📧 [rohitrajj@github.com](mailto:rohitrajj@github.com)


