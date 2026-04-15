from . import db
import datetime
from user_agents import parse

class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(2048), nullable=False)
    short_code = db.Column(db.String(10), unique=True, nullable=False)
    short_url = db.Column(db.String(10), unique=True, nullable=True)
    custom_alias = db.Column(db.String(50), unique=True, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    expiry_date = db.Column(db.DateTime, nullable=True)
    expiration_date = db.Column(db.DateTime, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    tags = db.Column(db.String(200), nullable=True)
    description = db.Column(db.String(500), nullable=True)
    clicks = db.relationship('ClickAnalytics', backref='url', lazy=True)
    click_events = db.relationship(
        'ClickEvent',
        backref='url',
        lazy=True,
        cascade='all, delete-orphan',
    )
    total_clicks = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            'id': self.id,
            'original_url': self.original_url,
            'short_code': self.short_code,
            'short_url': self.short_url,
            'custom_alias': self.custom_alias,
            'created_at': self.created_at.isoformat(),
            'expiry_date': self.expiry_date.isoformat() if self.expiry_date else None,
            'expiration_date': self.expiration_date.isoformat() if self.expiration_date else None,
            'is_active': self.is_active,
            'tags': self.tags,
            'description': self.description,
            'total_clicks': self.total_clicks
        }

class ClickAnalytics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url_id = db.Column(db.Integer, db.ForeignKey('url_map.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    clicked_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    ip_address = db.Column(db.String(45), nullable=True)
    country = db.Column(db.String(100), nullable=True)
    city = db.Column(db.String(100), nullable=True)
    device_type = db.Column(db.String(50), nullable=True)
    browser = db.Column(db.String(100), nullable=True)
    os = db.Column(db.String(100), nullable=True)
    referrer = db.Column(db.String(500), nullable=True)
    clicks = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            'id': self.id,
            'clicked_at': self.clicked_at.isoformat(),
            'country': self.country,
            'city': self.city,
            'device_type': self.device_type,
            'browser': self.browser,
            'os': self.os,
            'referrer': self.referrer,
            'clicks': self.clicks
        }

    @staticmethod
    def parse_user_agent(user_agent_string):
        unknown = {'device_type': 'Unknown', 'browser': 'Unknown', 'os': 'Unknown'}
        if not user_agent_string or not str(user_agent_string).strip():
            return unknown
        try:
            user_agent = parse(str(user_agent_string))
            return {
                'device_type': 'Mobile' if user_agent.is_mobile else 'Tablet' if user_agent.is_tablet else 'Desktop',
                'browser': f"{user_agent.browser.family} {user_agent.browser.version_string}"[:100],
                'os': f"{user_agent.os.family} {user_agent.os.version_string}"[:100],
            }
        except Exception:
            return unknown


class ClickEvent(db.Model):
    """One row per redirect (full click history)."""
    __tablename__ = 'click_event'

    id = db.Column(db.Integer, primary_key=True)
    url_id = db.Column(db.Integer, db.ForeignKey('url_map.id'), nullable=False, index=True)
    occurred_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    referrer = db.Column(db.String(500), nullable=True)
    ip_address = db.Column(db.String(45), nullable=True)
    device_type = db.Column(db.String(50), nullable=True)
    browser = db.Column(db.String(100), nullable=True)
    os = db.Column(db.String(100), nullable=True)
    user_agent = db.Column(db.String(256), nullable=True)