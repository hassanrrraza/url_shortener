from app import app, db
from app.models import URLMap, ClickAnalytics
from datetime import datetime, timedelta
import random

with app.app_context():
    # Check existing data
    url_count = URLMap.query.count()
    click_count = ClickAnalytics.query.count()
    
    print(f"Current database status:")
    print(f"URLs: {url_count}")
    print(f"ClickAnalytics records: {click_count}")
    
    # If no data exists, create sample data
    if url_count == 0:
        print("No URLs found. Creating sample data...")
        
        # Create some sample URLs with different dates and status
        sample_urls = [
            {
                "original_url": "https://example.com/page1",
                "short_code": "abc123",
                "created_at": datetime.utcnow() - timedelta(days=6),
                "expiry_date": None  # Active URL
            },
            {
                "original_url": "https://example.com/page2",
                "short_code": "def456",
                "created_at": datetime.utcnow() - timedelta(days=5),
                "expiry_date": datetime.utcnow() + timedelta(days=30)  # Active URL
            },
            {
                "original_url": "https://example.com/page3",
                "short_code": "ghi789",
                "created_at": datetime.utcnow() - timedelta(days=10),
                "expiry_date": datetime.utcnow() - timedelta(days=2)  # Expired URL
            },
            {
                "original_url": "https://example.com/page4",
                "short_code": "jkl012",
                "created_at": datetime.utcnow() - timedelta(days=2),
                "expiry_date": None  # Active URL
            },
            {
                "original_url": "https://example.com/page5",
                "short_code": "mno345",
                "created_at": datetime.utcnow() - timedelta(days=1),
                "expiry_date": datetime.utcnow() - timedelta(days=1)  # Expired URL
            }
        ]
        
        created_urls = []
        for url_data in sample_urls:
            url = URLMap(
                original_url=url_data["original_url"],
                short_code=url_data["short_code"],
                created_at=url_data["created_at"],
                expiry_date=url_data["expiry_date"]
            )
            db.session.add(url)
            created_urls.append(url)
        
        db.session.commit()
        
        # Add click analytics with some history
        for url in created_urls:
            # Generate random number of clicks between 5 and 30
            total_clicks = random.randint(5, 30)
            
            # Create a single ClickAnalytics record with total clicks
            analytics = ClickAnalytics(
                url_id=url.id,
                clicks=total_clicks,
                timestamp=datetime.utcnow()
            )
            db.session.add(analytics)
            
            # Also create some daily click records for the past week to build history
            for days_ago in range(1, 8):
                if random.random() > 0.3:  # 70% chance to have clicks on a given day
                    day_clicks = random.randint(1, 10)
                    day_record = ClickAnalytics(
                        url_id=url.id,
                        clicks=day_clicks,
                        timestamp=datetime.utcnow() - timedelta(days=days_ago)
                    )
                    db.session.add(day_record)
        
        db.session.commit()
        print(f"Created {len(sample_urls)} sample URLs with click analytics")
    
    # Print some current data for debugging
    print("\nCurrent URLs in database:")
    for url in URLMap.query.all():
        print(f"ID: {url.id}, Code: {url.short_code}, Original: {url.original_url[:30]}..., Expiry: {url.expiry_date}")
        
    print("\nCurrent click analytics:")
    for analytics in ClickAnalytics.query.all():
        print(f"URL ID: {analytics.url_id}, Clicks: {analytics.clicks}, Timestamp: {analytics.timestamp}") 