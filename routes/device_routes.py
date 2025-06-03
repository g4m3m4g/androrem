from flask import Blueprint, render_template
from adb_client import device

device_bp = Blueprint('device', __name__)

@device_bp.route("/status")
def status():
    battery = device.shell("dumpsys battery | grep level").strip()
    ip = device.shell("ip -f inet addr show wlan0 | grep inet").strip()
    model = device.shell("getprop ro.product.model").strip()
    return render_template("status.html", battery=battery, ip=ip, model=model)
