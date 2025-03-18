# URL Shortener

A modern URL shortening service with a sleek dashboard and powerful analytics, built with Python, Flask, and modern frontend technologies.

![URL Shortener Dashboard](images/main%20image.PNG)


## Features

- **URL Shortening**: Convert long URLs into short links which is manageable
- **Custom Aliases**: Create custom short URLs for better brand recognition
- **Expiration Dates**: Set expiration dates for your shortened URLs
- **Analytics Dashboard**: Track clicks, user agents, and more
- **Interactive Charts**: Visualize URL performance with dynamic charts
- **Real-time Updates**: Track URL performance in real-time
- **Responsive Design**: Works seamlessly on desktop and mobile devices

## Technology Stack

- **Backend**: Python, Flask, SQLAlchemy
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Database**: SQLite
- **Charts**: Chart.js
- **Icons**: Font Awesome
- **User Agent Parsing**: user-agents library

## Getting Started

### Prerequisites

- Python 3.9+
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/url-shortener.git
   cd url-shortener
   ```

2. Create and activate a virtual environment:
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Initialize the database:
   ```bash
   python init_db.py
   ```

5. Run the application:
   ```bash
   python run.py
   ```

6. Open your browser and visit:
   ```
   http://localhost:5000
   ```

## Project Structure

```
url-shortener/
├── app/                         # Main application package
│   ├── __init__.py              # Flask application initialization
│   ├── models.py                # Database models
│   ├── routes.py                # API and view routes
│   ├── utils.py                 # Utility functions
│   ├── static/                  # Static files
│   │   ├── css/                 # CSS stylesheets
│   │   │   └── style.css        # Main stylesheet
│   │   └── js/                  # JavaScript files
│   │       ├── api.js           # API interaction module
│   │       ├── charts.js        # Chart configuration
│   │       ├── debug.js         # Debugging tools
│   │       └── utils.js         # Utility functions
│   └── templates/               # HTML templates
│       ├── index.html           # Main page
│       └── analytics.html       # Analytics dashboard
├── instance/                    # Instance-specific files
│   └── app.db                   # SQLite database
├── debug_db.py                  # Database debugging script
├── init_db.py                   # Database initialization script
├── requirements.txt             # Python dependencies
├── run.py                       # Application entry point
└── README.md                    # This file
```

## API Documentation

### Get All URLs
- **Endpoint**: `/api/urls`
- **Method**: `GET`
- **Response**: List of all URLs and their data

### Shorten URL
- **Endpoint**: `/api/shorten`
- **Method**: `POST`
- **Body**:
  ```json
  {
    "url": "https://example.com/long/url",
    "custom_alias": "myalias",
    "expiry_date": "2023-12-31T23:59:59"
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "original_url": "https://example.com/long/url",
    "short_code": "myalias",
    "short_url": "http://localhost:5000/myalias",
    "created_at": "2023-06-01T12:00:00",
    "expiry_date": "2023-12-31T23:59:59",
    "is_active": true
  }
  ```

### Delete URL
- **Endpoint**: `/api/urls/:id`
- **Method**: `DELETE`
- **Response**: Success message

### Get Analytics
- **Endpoint**: `/api/analytics`
- **Method**: `GET`
- **Response**: Comprehensive analytics data

## Usage Examples

### Creating a shortened URL

```javascript
const urlData = {
  url: 'https://example.com/very/long/url/that/needs/to/be/shortened',
  custom_alias: 'example',
  expiry_date: '2023-12-31T23:59:59'
};

fetch('/api/shorten', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(urlData)
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));
```

## Future Enhancements

- User authentication system
- QR code generation for URLs
- Password protection for sensitive URLs
- URL grouping and tagging
- Analytics export (CSV, PDF)
- API rate limiting
- URL quality checking

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Chart.js](https://www.chartjs.org/)
- [Bootstrap](https://getbootstrap.com/)
- [Font Awesome](https://fontawesome.com/) 