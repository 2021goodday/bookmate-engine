from flask import Blueprint, request, jsonify

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/apikey-check", methods=["GET"])
def check_api_key():
    api_key = request.headers.get("x-api-key")

    if not api_key:
        return jsonify({"error": "API key required"}), 401

    # Replace this later with actual DB validation
    if api_key != "test-key":
        return jsonify({"error": "Invalid API key"}), 403

    return jsonify({"message": "API key valid"}), 200
