# ZavaDemo

A Flask-based web application demonstrating product management, database integration, and API consumption with a modern e-commerce frontend.

## 📋 Overview

ZavaDemo is a demonstration application showcasing:
- **RESTful API** endpoints for product CRUD operations
- **SQL Server LocalDB** integration with stored procedure support
- **External API integration** (Dad Joke API) with smart caching
- **Email functionality** via SMTP with attachment support
- **Modern web interface** built with Tailwind CSS
- **Utility functions** for validation, security, and data processing

## ✨ Features

### Core Functionality
- **Product Management**: Create, read, update, and delete products with in-memory storage
- **Database Integration**: Connect to SQL Server LocalDB and execute stored procedures
- **Dad Joke API**: Fetch and cache dad jokes from icanhazdadjoke.com
- **Customer Sales Reports**: Retrieve sales summaries via stored procedures
- **Email Sending**: SMTP-based email delivery with attachment support

### Utilities
- Email validation with regex patterns
- Password hashing (SHA-256) and strength validation
- Unique filename generation with timestamps
- XML data export and processing
- SQLite database querying and aggregation
- Logging capabilities

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- SQL Server LocalDB (for database features)
- ODBC Driver 17 for SQL Server

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ahmedsza/ghcpjumpstart.git
   cd ghcpjumpstart/Demos/ZavaDemo
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables** (optional, for email features)
   
   Create a `.env` file in the project root:
   ```env
   SMTP_HOST=your_smtp_host
   SMTP_PORT=587
   SMTP_USERNAME=your_username
   SMTP_PASSWORD=your_password
   ```

4. **Set up the database** (optional, for SQL features)
   - Ensure SQL Server LocalDB is installed
   - Create the `zavadb` database
   - Execute the stored procedure in [sqlstoredproc.sql](sqlstoredproc.sql)

### Running the Application

Start the Flask development server:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## 💻 Usage

### API Endpoints

#### Products
- **GET** `/products` - Retrieve all products
- **GET** `/products/<product_id>` - Get a specific product
- **POST** `/products` - Create a new product
- **PUT** `/products/<product_id>` - Update a product
- **DELETE** `/products/<product_id>` - Delete a product

#### Data & Reports
- **GET** `/getdata` - Fetch sample user data
- **GET** `/customer-sales-summary` - Retrieve customer sales summary from database
- **GET** `/dad-joke` - Get a dad joke (cached for 5 seconds)

### Example: Creating a Product

```bash
curl -X POST http://localhost:5000/products \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Premium Widget",
    "description": "A high-quality widget",
    "price": 29.99,
    "category": "Electronics"
  }'
```

### Using Utility Functions

```python
from utils import is_valid_email, hash_password, is_strong_password

# Validate email
is_valid_email("user@example.com")  # Returns True

# Hash password
hashed = hash_password("MySecretPassword123!")

# Check password strength
is_strong_password("Weak123")  # Returns False (no special character)

# Generate unique filename
from utils import generate_unique_filename
unique_file = generate_unique_filename("photo.jpg")
# Returns: photo_20260422153045123456.jpg
```

## 📁 Project Structure

```
ZavaDemo/
├── app.py                  # Main Flask application
├── utils.py                # Utility functions
├── send_email.py           # Email sending functionality
├── demo.py                 # Demo/example code
├── requirements.txt        # Python dependencies
├── sample_data.csv         # Sample CSV data
├── sampledata.json         # Sample JSON data
├── sqlstoredproc.sql       # SQL stored procedure
├── test_app.py             # Application tests
├── test_utils.py           # Utility tests
├── templates/
│   └── index.html          # Frontend template
└── outputs/
    └── code-understanding-report.md
```

## 🧪 Testing

Run the test suite:
```bash
pytest test_app.py test_utils.py
```

## 🛠️ Technologies

- **Backend**: Flask, Flask-CORS
- **Database**: SQL Server LocalDB, SQLite, pyodbc, SQLAlchemy
- **Frontend**: HTML, Tailwind CSS, JavaScript
- **Testing**: pytest, Selenium
- **Documentation**: MkDocs Material
- **Other**: requests (API calls), SMTP (email)

## ⚙️ Configuration

### Database Configuration

The application connects to SQL Server LocalDB by default. Modify the `SQL_SERVER_CONFIG` in [app.py](app.py) to use a different database:

```python
SQL_SERVER_CONFIG = {
    "server": r"(localdb)\MSSQLLocalDB",
    "database": "zavadb",
    "driver": "{ODBC Driver 17 for SQL Server}",
    "trusted_connection": "yes",
}
```

### Cache Settings

Dad joke caching duration can be adjusted in [app.py](app.py):
```python
CACHE_DURATION = 5  # Cache duration in seconds
```

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure your code:
- Follows PEP 8 style guidelines
- Includes tests for new functionality
- Updates documentation as needed

## 📄 License

This project is licensed under the terms specified in [LICENSE](LICENSE).

## 🔗 Related Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQL Server LocalDB](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/sql-server-express-localdb)
- [icanhazdadjoke API](https://icanhazdadjoke.com/api)
- [Tailwind CSS](https://tailwindcss.com/)

## ⚠️ Security Notice

**Note**: This is a demonstration project. For production use, implement proper security measures including:
- Environment-based configuration management
- Secure password storage (use bcrypt instead of SHA-256)
- Input validation and sanitization
- HTTPS/TLS encryption
- Rate limiting and throttling
- Proper error handling and logging
- SQL injection prevention
- CORS configuration

## 📧 Support

For questions or support, please open an issue in the [GitHub repository](https://github.com/ahmedsza/ghcpjumpstart/issues).

---

**Current Active PR**: [Add dad joke feature and demo application utilities](https://github.com/ahmedsza/ghcpjumpstart/pull/18)
