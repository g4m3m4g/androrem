from flask import Blueprint, render_template, redirect, url_for
from adb_client import device
from PIL import Image
import io

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route("/open_chrome")
def open_chrome():
    device.shell("am start -n com.android.chrome/com.google.android.apps.chrome.Main")
    return redirect(url_for('main.index'))

@main_bp.route("/screenshot")
def screenshot():
    raw = device.screencap()
    image = Image.open(io.BytesIO(raw))
    image.save("static/screenshot.png")
    return redirect(url_for('main.index'))

@main_bp.route("/swipe/<int:x1>/<int:y1>/<int:x2>/<int:y2>")
def swipe(x1, y1, x2, y2):
    device.shell(f"input swipe {x1} {y1} {x2} {y2} 300")
    return redirect(url_for('main.index'))

@main_bp.route("/tap/<int:x>/<int:y>")
def tap(x, y):
    device.shell(f"input tap {x} {y}")
    return redirect(url_for('main.index'))

@main_bp.route("/input/<text>")
def input_text(text):
    safe = text.replace(" ", "%s")
    device.shell(f"input text {safe}")
    return redirect(url_for('main.index'))

@main_bp.route("/wake")
def wake_phone():
    device.shell("input keyevent 26")  # power button to wake
    return redirect(url_for('main.index'))
