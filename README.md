# 🚀 Flask Hello World (Dockerized)

This is a simple Flask "Hello World" application that runs inside a Docker container.
Perfect for learning Docker basics and DevOps workflows!

---

## 📁 Project Structure

```
.
├── app.py               # Flask application
├── Dockerfile           # Docker instructions
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## ⚙️ Prerequisites

* ✅ Docker installed
* ✅ Git installed
* (Optional) Python installed for local testing

---

## 🐍 Run Locally (Without Docker)

```bash
pip install -r requirements.txt
python app.py
```

Then visit: [http://localhost:5000](http://localhost:5000)

---

## 🐳 Run with Docker

### ✅ Step 1: Build the Docker Image

```bash
docker build -t flask-hello .
```

### ✅ Step 2: Run the Docker Container

```bash
docker run -d -p 5000:5000 flask-hello
```

Then visit: [http://localhost:5000](http://localhost:5000)

---

## 📦 Push to Docker Hub

### ✅ Step 1: Tag the Image

```bash
docker tag flask-hello rohitrajj/flask-hello
```

### ✅ Step 2: Push to Docker Hub

```bash
docker push rohitrajj/flask-hello
```

Anyone can now pull and run it:

```bash
docker pull rohitrajj/flask-hello
docker run -p 5000:5000 rohitrajj/flask-hello
```

---

## 🌐 Push Project to GitHub

### ✅ Step-by-Step

```bash
git init
git remote add origin https://github.com/rohitrajj/flask-hello-docker-hub.git
git add .
git commit -m "Initial commit: Dockerized Flask app"
git push -u origin main
```

---

## 📸 Optional: Add GitHub Pages or Jenkins Pipeline (Next Steps)

* Set up GitHub Actions for Docker build & push
* Deploy to AWS EC2, Azure, or Render
* Add login feature or database integration

---

## 🙇‍♂️ Author

**Rohit Raj**
DevOps Enthusiast | Cloud | Docker | Python
📢 [rohitrajj@github.com](mailto:rohitrajj@github.com)


