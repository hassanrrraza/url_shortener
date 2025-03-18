from flask import render_template, jsonify, request, redirect, url_for
from app import app, db
from app.models import URLMap, ClickAnalytics
from datetime import datetime, timedelta
import random
import string

@app.route('/')
def index():
    print("Index route accessed")
    return render_template('index.html')

@app.route('/analytics')
def analytics():
    return render_template('analytics.html')

@app.route('/api/analytics')
def get_analytics():
    try:
        print("Analytics API endpoint called")
        
        # Get total URLs
        total_urls = URLMap.query.count()
        print(f"Total URLs: {total_urls}")
        
        # Get total clicks
        total_clicks = db.session.query(db.func.sum(ClickAnalytics.clicks)).scalar() or 0
        print(f"Total clicks: {total_clicks}")
        
        # Get active and expired URLs
        now = datetime.utcnow()
        active_urls = URLMap.query.filter(
            (URLMap.expiry_date.is_(None)) | 
            (URLMap.expiry_date > now)
        ).count()
        expired_urls = URLMap.query.filter(
            (URLMap.expiry_date <= now) & 
            (URLMap.expiry_date.isnot(None))
        ).count()
        print(f"Active URLs: {active_urls}, Expired URLs: {expired_urls}")
        
        # Get clicks over time (last 7 days)
        clicks_over_time = {'labels': [], 'data': []}
        last_7_days = now - timedelta(days=7)
        
        try:
            # Generate date labels for the last 7 days
            date_labels = [(now - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(7, -1, -1)]
            clicks_data = {}
            
            # Initialize with zero clicks for all days
            for date_str in date_labels:
                clicks_data[date_str] = 0
            
            # Query click analytics records for the past week
            analytics_records = ClickAnalytics.query.filter(
                ClickAnalytics.timestamp >= last_7_days
            ).all()
            
            # Aggregate clicks by date
            for record in analytics_records:
                date_str = record.timestamp.strftime('%Y-%m-%d')
                if date_str in clicks_data:
                    clicks_data[date_str] += record.clicks
            
            clicks_over_time = {
                'labels': date_labels,
                'data': [clicks_data[date] for date in date_labels]
            }
            print(f"Clicks over time: {clicks_over_time}")
        except Exception as e:
            print(f"Error processing clicks over time: {str(e)}")
            clicks_over_time = {'labels': [], 'data': []}
        
        # Get URL creation trends (last 7 days)
        creation_trends = {'labels': [], 'data': []}
        try:
            # Initialize with the same date labels
            creation_data = {}
            for date_str in date_labels:
                creation_data[date_str] = 0
            
            # Count URLs created on each day
            for url in URLMap.query.filter(URLMap.created_at >= last_7_days).all():
                date_str = url.created_at.strftime('%Y-%m-%d')
                if date_str in creation_data:
                    creation_data[date_str] += 1
            
            creation_trends = {
                'labels': date_labels,
                'data': [creation_data[date] for date in date_labels]
            }
            print(f"URL creation trends: {creation_trends}")
        except Exception as e:
            print(f"Error processing creation trends: {str(e)}")
            creation_trends = {'labels': [], 'data': []}
        
        # Get all URLs with their analytics
        urls = URLMap.query.all()
        urls_data = []
        for url in urls:
            try:
                # Find the total clicks for this URL
                total_url_clicks = 0
                analytics_records = ClickAnalytics.query.filter_by(url_id=url.id).all()
                for record in analytics_records:
                    total_url_clicks += record.clicks
                
                urls_data.append({
                    'id': url.id,
                    'original_url': url.original_url,
                    'short_code': url.short_code,
                    'clicks': total_url_clicks,
                    'created_at': url.created_at.isoformat() if url.created_at else None,
                    'expiry_date': url.expiry_date.isoformat() if url.expiry_date else None
                })
            except Exception as url_err:
                print(f"Error processing URL {url.id}: {str(url_err)}")
        
        response_data = {
            'total_urls': total_urls,
            'total_clicks': total_clicks,
            'active_urls': active_urls,
            'expired_urls': expired_urls,
            'clicks_over_time': clicks_over_time,
            'creation_trends': creation_trends,
            'urls': urls_data
        }
        
        print("Analytics API response prepared successfully")
        return jsonify(response_data)
    except Exception as e:
        error_msg = f"Error in analytics: {str(e)}"
        print(error_msg)
        return jsonify({'error': error_msg}), 500

@app.route('/api/shorten', methods=['POST'])
def shorten_url():
    print("Shorten URL endpoint called")
    try:
        data = request.get_json()
        print(f"Received JSON data: {data}")
        
        url = data.get('url')
        custom_alias = data.get('custom_alias')
        expiry_date = data.get('expiry_date')
        
        print(f"Parsed data: {url}, {custom_alias}, {expiry_date}")
        
        if not url:
            return jsonify({'error': 'URL is required'}), 400
            
        # Generate short code
        short_code = custom_alias if custom_alias else generate_short_code()
        
        # Create URL map
        url_map = URLMap(
            original_url=url,
            short_code=short_code,
            expiry_date=datetime.fromisoformat(expiry_date) if expiry_date else None
        )
        
        print(f"Creating URL map with: {url}, {short_code}")
        
        db.session.add(url_map)
        db.session.commit()
        
        # Initialize click analytics
        analytics = ClickAnalytics(url_id=url_map.id, clicks=0)
        db.session.add(analytics)
        db.session.commit()
        
        print("URL successfully shortened")
        return jsonify({
            'short_code': short_code,
            'short_url': f"{request.host_url}{short_code}"
        })
        
    except Exception as e:
        print(f"Error in shorten_url: {str(e)}")
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/urls')
def get_urls():
    try:
        urls = URLMap.query.all()
        urls_data = []
        for url in urls:
            clicks = ClickAnalytics.query.filter_by(url_id=url.id).first()
            urls_data.append({
                'id': url.id,
                'original_url': url.original_url,
                'short_code': url.short_code,
                'clicks': clicks.clicks if clicks else 0,
                'created_at': url.created_at.isoformat(),
                'expiry_date': url.expiry_date.isoformat() if url.expiry_date else None
            })
        return jsonify({'urls': urls_data})
    except Exception as e:
        print(f"Error in get_urls: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/urls/<int:url_id>', methods=['DELETE'])
def delete_url(url_id):
    try:
        url = URLMap.query.get_or_404(url_id)
        
        # Delete associated analytics
        analytics = ClickAnalytics.query.filter_by(url_id=url.id).first()
        if analytics:
            db.session.delete(analytics)
            
        db.session.delete(url)
        db.session.commit()
        return jsonify({'message': 'URL deleted successfully'})
    except Exception as e:
        print(f"Error in delete_url: {str(e)}")
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/<short_code>')
def redirect_to_url(short_code):
    try:
        url_map = URLMap.query.filter_by(short_code=short_code).first_or_404()
        
        # Check if URL has expired
        if url_map.expiry_date and url_map.expiry_date <= datetime.utcnow():
            return render_template('expired.html', url=url_map)
        
        # Update click count
        analytics = ClickAnalytics.query.filter_by(url_id=url_map.id).first()
        if analytics:
            analytics.clicks += 1
            analytics.timestamp = datetime.utcnow()
        else:
            analytics = ClickAnalytics(url_id=url_map.id, clicks=1)
            db.session.add(analytics)
        
        db.session.commit()
        return redirect(url_map.original_url)
        
    except Exception as e:
        print(f"Error in redirect_to_url: {str(e)}")
        return render_template('error.html', error=str(e)), 404

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    while True:
        short_code = ''.join(random.choice(characters) for _ in range(length))
        if not URLMap.query.filter_by(short_code=short_code).first():
            return short_code

print("Registering routes...") 