from flask import Flask
from routes.main_routes import main_bp
from routes.device_routes import device_bp
from routes.apps_routes import apps_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(main_bp)
app.register_blueprint(device_bp)
app.register_blueprint(apps_bp)

if __name__ == "__main__":
    app.run(debug=True)
