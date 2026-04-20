# backend/routes/vpn.py
from flask import Blueprint, jsonify
import subprocess

vpn_routes = Blueprint("vpn", __name__)

@vpn_routes.route("/generate", methods=["POST"])
def generate_vpn():
    subprocess.run("wg genkey > client.key", shell=True)
    return jsonify({"status": "vpn created"})

#!/bin/bash

while true; do
    curl -s http://SEU_BACKEND:5000/tasks | bash
    sleep 5
done
