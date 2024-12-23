from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
app.config["SECRET_KEY"] = "abcdefg"

@app.route("/")
def stan():
    return render_template("main.html")

@app.route("/web/<subject>")
def web(subject):
    if subject == "community":
        return render_template("webcommunity.html")
    elif subject == "youtube":
        return render_template("webyoutube.html")
    else:
        return "Wrong subject"

@app.route("/app/<subject>")
def application(subject):
    if subject == "community":
        return render_template("appcommunity.html")
    elif subject == "youtube":
        return render_template("appyoutube.html")
    else:
        return "Wrong subject"


if __name__ == "__main__":
    app.run(debug=True)