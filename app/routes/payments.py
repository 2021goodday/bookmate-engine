from flask import Blueprint, request, jsonify
from app import limiter

payments_bp = Blueprint("payments", __name__)


@payments_bp.route("/charge", methods=["POST"])
@limiter.limit("3 per minute")
def process_payment():
    data = request.json
    amount = data.get("amount")
    method = data.get("method")

    if not amount or not method:
        return jsonify({"error": "Missing payment data"}), 400

    return jsonify({
        "status": "success",
        "amount": amount,
        "method": method,
        "message": "Payment processed successfully"
    }), 200
