# backend/routes/users.py
from flask import Blueprint, request, jsonify
import os

user_routes = Blueprint("users", __name__)

@user_routes.route("/create-user", methods=["POST"])
def create_user():
    data = request.json
    user = data.get("username")

    os.system(f"useradd {user}")
    os.system(f"echo '{user}:1234' | chpasswd")

    return jsonify({"status": "created"})
