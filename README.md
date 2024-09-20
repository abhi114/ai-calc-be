# Calculator API Backend

This is the backend for the Calculator App, built with Python and FastAPI. It handles the logic and calculations, providing an API to be consumed by the frontend.

## Features

- **FastAPI** for API development.
- **Environment variables** using `dotenv` for managing sensitive data.
- **Endpoints** for mathematical calculations.
- **Deployed on** [Render](https://render.com) (or your chosen platform).

## Requirements

- Python 3.x
- `pip` (Python package installer)
- `venv` (for virtual environment)

## Project Structure

calculator-backend/ │ ├── apps/ │ └── calculator/ │ ├── route.py │ ├── utils.py │ ├── main.py # Main entry point for the API ├── schema.py # Data validation and Pydantic schemas ├── constants.py # App constants ├── .env # Environment variables (should not be committed) ├── requirements.txt # Project dependencies ├── README.md # Project documentation ├── .gitignore # Files to ignore in Git └── venv/ # Virtual environment folder
## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/calculator-backend.git
   cd calculator-backend

2 . Set up the virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt

Deployment
This application can be deployed on Render, Heroku, or any platform that supports FastAPI. Follow the respective service documentation to deploy your app.

Ensure the following environment variables are configured in your deployment:

GEMINI_API_KEY
API Endpoints
GET /calculate - Perform a calculation.
POST /calculate - Submit a calculation request.
More detailed API documentation is available at /docs after running the server.


