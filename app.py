from flask import Flask, render_template, redirect, url_for
from ppadb.client import Client as AdbClient
from PIL import Image
import io

app = Flask(__name__)

# Connect to ADB
client = AdbClient(host="127.0.0.1", port=5037)
device = client.devices()[0]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/open_chrome")
def open_chrome():
    device.shell("am start -n com.android.chrome/com.google.android.apps.chrome.Main")
    return redirect(url_for('index'))

@app.route("/screenshot")
def screenshot():
    raw = device.screencap()
    image = Image.open(io.BytesIO(raw))
    image.save("static/screenshot.png")
    return redirect(url_for('index'))

@app.route("/swipe/<int:x1>/<int:y1>/<int:x2>/<int:y2>")
def swipe(x1, y1, x2, y2):
    device.shell(f"input swipe {x1} {y1} {x2} {y2} 300")
    return redirect(url_for('index'))


@app.route("/tap/<int:x>/<int:y>")
def tap(x, y):
    device.shell(f"input tap {x} {y}")
    return redirect(url_for('index'))



if __name__ == "__main__":
    app.run(debug=True)
