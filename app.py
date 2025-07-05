from flask import Flask, request, render_template

app = Flask(__name__)

messages = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        message = request.form.get("message")
        if name and message:
            messages.append({"name": name, "message": message})
    return render_template("page.html", messages=messages)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
