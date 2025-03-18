"""
Utility functions for the URL shortener application.
"""
import random
import string
from datetime import datetime

def generate_short_code(length=6):
    """
    Generate a random short code for URL shortening.
    
    Args:
        length (int): Length of the short code to generate. Default is 6.
        
    Returns:
        str: A random string of alphanumeric characters.
    """
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def is_url_expired(expiry_date):
    """
    Check if a URL has expired based on its expiry date.
    
    Args:
        expiry_date (datetime): The expiry date of the URL.
        
    Returns:
        bool: True if the URL has expired, False otherwise.
    """
    if not expiry_date:
        return False
    return datetime.utcnow() > expiry_date

def format_datetime(dt):
    """
    Format a datetime object for display in the application.
    
    Args:
        dt (datetime): The datetime object to format.
        
    Returns:
        str: A formatted string representation of the datetime.
    """
    if not dt:
        return "None"
    return dt.strftime('%Y-%m-%d %H:%M:%S')