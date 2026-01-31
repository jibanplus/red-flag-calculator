from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        score = 0
        f = request.form

        if f.get("lying") == "yes":
            score += 2
        if f.get("anger") == "yes":
            score += 2
        if f.get("control") == "yes":
            score += 2
        if f.get("respect") == "no":
            score += 2

        if score >= 6:
            result = "🚨 High Red Flag Risk"
        elif score >= 3:
            result = "⚠️ Medium Red Flag Risk"
        else:
            result = "✅ Low Red Flag Risk"

    return f"""
    <html>
    <head>
        <title>Red Flag Calculator</title>
    </head>
    <body style="background:#0f0f0f;color:white;font-family:Arial;display:flex;justify-content:center;align-items:center;height:100vh;">
        <div style="background:#1c1c1c;padding:25px;border-radius:10px;width:380px;">
            <h2>Red Flag Calculator</h2>

            <form method="POST">
                <p>Frequent lying?</p>
                <input type="radio" name="lying" value="yes" required> Yes
                <input type="radio" name="lying" value="no"> No

                <p>Anger issues?</p>
                <input type="radio" name="anger" value="yes" required> Yes
                <input type="radio" name="anger" value="no"> No

                <p>Controlling behavior?</p>
                <input type="radio" name="control" value="yes" required> Yes
                <input type="radio" name="control" value="no"> No

                <p>Respects boundaries?</p>
                <input type="radio" name="respect" value="yes" required> Yes
                <input type="radio" name="respect" value="no"> No

                <br><br>
                <button type="submit">Calculate</button>
            </form>

            <h3>{result}</h3>

            <p style="font-size:12px;opacity:0.7;">Powered by Jiban</p>
        </div>
    </body>
    </html>
    """
