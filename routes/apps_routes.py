from flask import Blueprint, render_template, redirect
from adb_client import device

apps_bp = Blueprint('apps', __name__)

@apps_bp.route("/apps")
def apps():
    output = device.shell("pm list packages")
    packages = [line.replace("package:", "") for line in output.strip().splitlines()]
    return render_template("apps.html", packages=packages)

@apps_bp.route("/launch/<pkg>")
def launch(pkg):
    device.shell(f"monkey -p {pkg} -c android.intent.category.LAUNCHER 1")
    return redirect("/apps")
