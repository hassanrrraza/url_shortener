# 🔗 URL Shortener

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-lightgrey.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

A modern, feature-rich URL shortening service built with Flask and modern web technologies. Transform long URLs into memorable short links with comprehensive analytics.

[Features](#-features) • [Demo](#-live-demo) • [Installation](#-installation) • [API](#-api-reference) • [Contributing](#-contributing)

<img src="images/main%20image.PNG" alt="URL Shortener Dashboard" width="80%">

</div>

## ✨ Features

🔹 **Instant Shortening**: Convert long URLs into concise, shareable links  
🔹 **Custom Aliases**: Create branded short URLs for better recognition  
🔹 **Expiration Control**: Set expiry dates for temporary links  
🔹 **Rich Analytics**: Track clicks, locations, devices, and more  
🔹 **Visual Insights**: Interactive charts powered by Chart.js  
🔹 **Real-time Updates**: Monitor URL performance in real-time  
🔹 **Responsive Design**: Perfect experience across all devices

## 🚀 Live Demo

Experience the application in action: [Live Demo](https://github.com/hassanrrraza/url_shortener)

## 🛠️ Tech Stack

### Backend
- **[Python](https://www.python.org/)**: Core programming language
- **[Flask](https://flask.palletsprojects.com/)**: Web framework
- **[SQLAlchemy](https://www.sqlalchemy.org/)**: ORM for database operations

### Frontend
- **[Bootstrap 5](https://getbootstrap.com/)**: Responsive UI framework
- **[Chart.js](https://www.chartjs.org/)**: Interactive data visualization
- **[Font Awesome](https://fontawesome.com/)**: Beautiful icons

### Database & Tools
- **SQLite**: Lightweight database
- **[user-agents](https://pypi.org/project/user-agents/)**: Device detection

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/hassanrrraza/url_shortener.git
   cd url_shortener
   ```

2. **Set up virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize database**
   ```bash
   python init_db.py
   ```

5. **Start the server**
   ```bash
   python run.py
   ```

6. **Visit** `http://localhost:5000` in your browser

## 📝 API Reference

### Create Short URL
```http
POST /api/shorten
```
| Parameter | Type | Description |
| :--- | :--- | :--- |
| `url` | `string` | **Required**. URL to shorten |
| `custom_alias` | `string` | Custom alias for the URL |
| `expiry_date` | `string` | Expiration date (ISO format) |

### Get URL Analytics
```http
GET /api/analytics/:id
```

### Delete URL
```http
DELETE /api/urls/:id
```

## 📂 Project Structure

```
url_shortener/
├── app/                    # Application package
│   ├── models.py          # Database models
│   ├── routes.py          # API endpoints
│   ├── static/            # Static assets
│   └── templates/         # HTML templates
├── instance/              # Instance data
├── requirements.txt       # Dependencies
└── run.py                # Entry point
```

## 🤝 Contributing

Contributions are what make the open source community amazing! Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🔮 Future Enhancements

- [ ] User authentication system
- [ ] QR code generation
- [ ] Password-protected links
- [ ] Bulk URL shortening
- [ ] Advanced analytics export
- [ ] API rate limiting
- [ ] Custom domain support

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 👏 Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Chart.js](https://www.chartjs.org/)
- [Bootstrap](https://getbootstrap.com/)
- [Font Awesome](https://fontawesome.com/)

## 📬 Contact

Hassan Raza - [@hassanrrraza](https://github.com/hassanrrraza)

Project Link: [https://github.com/hassanrrraza/url_shortener](https://github.com/hassanrrraza/url_shortener)

---
<div align="center">
⭐ Star this repo if you find it helpful!
</div> 