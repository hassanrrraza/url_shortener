from app import app, db
from app.models import URLMap, ClickAnalytics

print("Initializing database...")

# Create the database and tables
with app.app_context():
    print("Dropping all tables...")
    db.drop_all()
    
    print("Creating all tables...")
    db.create_all()
    
    print("Database initialized successfully with the latest schema!") 