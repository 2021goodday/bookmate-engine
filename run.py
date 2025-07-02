import os
from app import create_app

app = create_app()
print("Firebase key loaded:", os.getenv("FIREBASE_KEY"))

if __name__ == "__main__":
    app.run(debug=True)
