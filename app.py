from flask import Flask, request
import random

app = Flask(__name__, static_folder="static")

# -------------------------------
# Funny Hinglish taglines
# -------------------------------
LOW_LINES = [
    "Green flag zone… nazar na lage 😌",
    "Lagta hai yaha communication Wi-Fi strong hai 📶",
    "Red flag kam, green vibes zyada 😄",
    "Normal issues hain, panic nahi 👍"
]

MID_LINES = [
    "Yellow light blink kar raha hai 🤔",
    "Thoda sa ‘hmm’ moment hai 😅",
    "Abhi fix ho sakta hai, ignore mat karo 🛠️",
    "Chhoti chingari hai, aag mat banne dena 🔥"
]

HIGH_LINES = [
    "Red flag aaya… entry bhi le li 😬",
    "Yeh sirf mood swing nahi lag raha 🚨",
    "Pattern dikh raha hai, single incident nahi 👀",
    "Future-you thoda alert ho jao ⚠️"
]

# -------------------------------
@app.route("/", methods=["GET", "POST"])
def home():
    total_score = None
    level = ""
    emoji = ""
    tagline = ""
    sound_level = ""
    comm = respect = honesty = control = 0

    if request.method == "POST":
        f = request.form

        # category scores (0–25 each)
        comm = int(f.get("comm", 0))
        respect = int(f.get("respect", 0))
        honesty = int(f.get("honesty", 0))
        control = int(f.get("control", 0))

        total_score = comm + respect + honesty + control

        if total_score <= 30:
            level = "low"
            emoji = "😌"
            tagline = random.choice(LOW_LINES)
            sound_level = "low"
        elif total_score <= 60:
            level = "mid"
            emoji = "🤔"
            tagline = random.choice(MID_LINES)
            sound_level = "mid"
        else:
            level = "high"
            emoji = "😬"
            tagline = random.choice(HIGH_LINES)
            sound_level = "high"

    return f"""
<!DOCTYPE html>
<html>
<head>
<title>Red Flag Signals</title>

<style>
body {{
    margin:0;
    font-family: Arial, sans-serif;
    background: linear-gradient(120deg, #cfd9ff, #fbc2eb);
    min-height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
}}

.card {{
    background:white;
    width:420px;
    padding:25px;
    border-radius:16px;
    box-shadow:0 20px 40px rgba(0,0,0,0.15);
}}

h2 {{
    text-align:center;
    margin-bottom:10px;
}}

label {{
    font-size:14px;
}}

input[type=range] {{
    width:100%;
}}

button {{
    width:100%;
    padding:12px;
    margin-top:15px;
    border:none;
    border-radius:10px;
    font-size:16px;
    cursor:pointer;
    background:#6c63ff;
    color:white;
}}

.result {{
    margin-top:20px;
    text-align:center;
}}

.bar {{
    height:12px;
    border-radius:10px;
    background:#eee;
    overflow:hidden;
    margin-top:8px;
}}

.fill {{
    height:100%;
}}

.low {{ background:#4caf50; }}
.mid {{ background:#ffc107; }}
.high {{ background:#f44336; }}

.emoji {{
    font-size:38px;
    animation: pop 0.6s ease;
}}

@keyframes pop {{
    0% {{ transform:scale(0.5); }}
    60% {{ transform:scale(1.2); }}
    100% {{ transform:scale(1); }}
}}

.footer {{
    margin-top:15px;
    font-size:12px;
    opacity:0.7;
    text-align:center;
}}
</style>
</head>

<body>

<div class="card">
<h2>Red Flag Signals 🚦</h2>

<form method="POST">
<label>🧠 Communication</label>
<input type="range" name="comm" min="0" max="25" value="0">

<label>❤️ Respect</label>
<input type="range" name="respect" min="0" max="25" value="0">

<label>🎭 Honesty</label>
<input type="range" name="honesty" min="0" max="25" value="0">

<label>🔒 Control</label>
<input type="range" name="control" min="0" max="25" value="0">

<label style="font-size:13px;">
<input type="checkbox" id="mute"> Mute sound
</label>

<button type="submit">Check Signals</button>
</form>

{"".join([
f'''
<div class="result">
<div class="emoji">{emoji}</div>
<h3>Your Signal Score: {total_score} / 100</h3>

<div class="bar">
  <div class="fill {level}" style="width:{total_score}%"></div>
</div>

<p><b>{tagline}</b></p>

<p style="font-size:13px;opacity:0.7;">
This tool shows patterns, not labels.
</p>
</div>

<audio id="sound-low" src="/static/low.mp3"></audio>
<audio id="sound-mid" src="/static/mid.mp3"></audio>
<audio id="sound-high" src="/static/high.mp3"></audio>

<script>
if(!document.getElementById("mute").checked){{
 document.getElementById("sound-{sound_level}").play();
}}
</script>
'''
]) if total_score is not None else ""}

<div class="footer">
POWERED BY <b>TUB</b>
</div>

</div>

</body>
</html>
"""

if __name__ == "__main__":
    app.run()
