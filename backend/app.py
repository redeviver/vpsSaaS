# backend/app.py
from flask import Flask
from routes.users import user_routes
from routes.vpn import vpn_routes

app = Flask(__name__)

app.register_blueprint(user_routes)
app.register_blueprint(vpn_routes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
