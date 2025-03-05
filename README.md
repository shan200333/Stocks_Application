# Invsto FastAPI Assignment

## Overview
This project is a FastAPI-based backend application developed as an assignment for Invsto. It includes CRUD operations, external API integrations, and database connectivity using PostgreSQL

## 📌 Features
- CRUD operations using FastAPI
- PostgreSQL database integration
- Google Sheets data synchronization
- Docker containerization
- Best practices in FastAPI development

## Tech Stack
- **Backend:** FastAPI, Pydantic, Uvicorn
- **Database:** PostgreSQL
- **Containerization:** Docker

## Prerequisites
Ensure you have the following installed before proceeding:
- Python 3.12+
- Docker
- PostgreSQL

## Installation
Clone the repository:
```sh
 git clone https://github.com/shan200333/Stocks_Application.git
 cd invsto-fastapi
```

Create a virtual environment:
```sh
python -m venv venv
source venv/scripts/activate  
```

Install dependencies:
```sh
pip install -r requirements.txt
```

## Environment Variables
Create a `.env` file and define the following variables:
```env
DATABASE_HOSTNAME=your_db_host
DATABASE_PORT=your_db_port
DATABASE_USERNAME=your_db_user
DATABASE_PASSWORD=your_db_password
DATABASE_NAME=your_db_name
```
## Running the Application
Run the application using Uvicorn:
```sh
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## Running with Docker
Build the Docker image:
```sh
docker build -t fastapi-app .
```
Run the container:
```sh
docker run -d -p 8000:8000 --env-file .env fastapi-app
```

## Screenshots
https://github.com/shan200333/Stocks_Application/tree/main/Working%20Screenshots


