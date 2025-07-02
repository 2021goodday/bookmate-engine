# BookMate Engine

**BookMate Engine** is a backend system that enables small businesses to manage bookings, time slots, and payments through a mobile app interface. This RESTful API is built with Python (Flask), backed by PostgreSQL, and features push notifications via Firebase Cloud Messaging. It follows secure and scalable design practices, including rate limiting and API key validation.

---

## 🚀 Features

- Booking & Time Slot Management (CRUD)
- Mock Payment Endpoint
- Firebase Push Notifications
- Rate Limiting (via Flask-Limiter)
- API Key Validation (via header)
- CI/CD-ready for Google Cloud App Engine
- Includes Postman Collection for easy testing

---

## 🛠 Tech Stack

- **Backend**: Python, Flask
- **Database**: PostgreSQL (or SQLite for testing)
- **Push Notifications**: Firebase Cloud Messaging (`pyfcm`)
- **Deployment**: Google Cloud App Engine
- **CI/CD**: GitHub Actions
- **Testing**: Postman

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/bookmate-engine.git
cd bookmate-engine
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Set environment variables in a .env file:

```bash
FIREBASE_KEY=your_firebase_key
DATABASE_URL=sqlite:///bookmate.db  # or your PostgreSQL URI
```

Then run the server:

```bash
python run.py
```

## 📮 API Reference

| Endpoint                 | Method | Description                |
| ------------------------ | ------ | -------------------------- |
| `/api/auth/apikey-check` | GET    | Validates API key          |
| `/api/bookings/`         | GET    | List all bookings          |
| `/api/bookings/`         | POST   | Create a new booking       |
| `/api/payments/charge`   | POST   | Simulate a payment process |

## 📂 Import the included Postman file:

bookmate-engine-api.postman_collection.json

## 📡 Deployment

To deploy on Google Cloud App Engine:

1. Add an app.yaml
2. Run:

```bash
gcloud app deploy
```
