from flask import Blueprint, request, jsonify
from app import db, limiter
from app.models import Booking, TimeSlot

bookings_bp = Blueprint("bookings", __name__)


@bookings_bp.route("/", methods=["GET"])
@limiter.limit("5 per minute")
def get_all_bookings():
    bookings = Booking.query.all()
    return jsonify([
        {
            "id": b.id,
            "customer_name": b.customer_name,
            "status": b.status
        } for b in bookings
    ])


@bookings_bp.route("/", methods=["POST"])
@limiter.limit("2 per minute")
def create_booking():
    data = request.json
    booking = Booking(
        user_id=data["user_id"],
        timeslot_id=data["timeslot_id"],
        customer_name=data["customer_name"]
    )
    db.session.add(booking)

    timeslot = TimeSlot.query.get(data["timeslot_id"])
    if timeslot:
        timeslot.is_booked = True
    db.session.commit()

    return jsonify({"message": "Booking created successfully"}), 201
