# ZavaDemo

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![Flask](https://img.shields.io/badge/framework-Flask-green.svg)
![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)

A Flask-based REST API demo application with SQL Server integration, an in-memory product store, and a web front-end.

---

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Running Tests](#running-tests)
- [Contributing](#contributing)

---

## Overview

ZavaDemo is a demonstration web application built with Flask. It exposes a REST API for managing products, querying a SQL Server (LocalDB) database, retrieving a customer sales summary, and fetching dad jokes with caching. A simple HTML front-end is served from the `/` route.

Key features:

- CRUD operations for an in-memory product store
- SQL Server (LocalDB) integration via `pyodbc`
- Dad joke endpoint with time-based caching
- CORS enabled for all routes
- Structured HTML UI served via Jinja2 templates

---

## Installation

### Prerequisites

- Python 3.x
- SQL Server LocalDB (`(localdb)\MSSQLLocalDB`) with a `zavadb` database
- ODBC Driver 17 for SQL Server

### Steps

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd Demos/ZavaDemo
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Start the Flask development server:

```bash
python app.py
```

The application will be available at `http://localhost:5000`.

To run the demo script:

```bash
python demo.py
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Serves the HTML front-end |
| `GET` | `/getdata` | Fetches data from the SQL Server database |
| `GET` | `/products` | List all products |
| `GET` | `/products/<product_id>` | Get a product by ID |
| `POST` | `/products` | Create a new product |
| `PUT` | `/products/<product_id>` | Update an existing product |
| `DELETE` | `/products/<product_id>` | Delete a product |
| `GET` | `/customer-sales-summary` | Retrieve customer sales summary from SQL |
| `GET` | `/dadjoke` | Fetch a dad joke (cached for a period) |

---

## Running Tests

```bash
pytest
```

Test files are located at:

- [test_app.py](test_app.py) — API and route tests
- [test_utils.py](test_utils.py) — Utility function tests

---

## Project Structure

```
ZavaDemo/
├── app.py                  # Flask application and route definitions
├── demo.py                 # Demo/helper script
├── utils.py                # Utility functions
├── send_email.py           # Email helper
├── requirements.txt        # Python dependencies
├── sample_data.csv         # Sample dataset
├── sampledata.json         # Sample JSON data
├── sqlstoredproc.sql       # SQL stored procedure definitions
├── templates/
│   └── index.html          # Front-end HTML template
├── outputs/
│   └── code-understanding-report.md
└── test_app.py / test_utils.py
```

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request. See [LICENSE](LICENSE) for licensing information.
