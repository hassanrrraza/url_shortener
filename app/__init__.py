from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your-secret-key-for-production-use-env-var'

    db.init_app(app)
    migrate.init_app(app, db)

    # Create the database tables
    with app.app_context():
        db.create_all()
        
    return app

# Create the app instance
app = create_app()

# Import routes after creating app to avoid circular imports
from app import routes
