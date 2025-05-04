from grocery_app.extensions import db
from grocery_app import create_app

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)