# newsapi-backend

This project provides a FastAPI service that fetches articles from the News API, implements server‑side pagination, and persists selected headlines into a PostgreSQL database using Tortoise ORM.

🔧 Prerequisites
- Conda (or another Python virtual environment manager)
- Docker & Docker Compose (for containerized development)
- News API Key (obtainable from ![https://newsapi.org/][https://newsapi.org/])

🛠️ Local Setup

1. Clone the repository
    ```
    git clone https://github.com/your-username/newsapi-fastapi-service.git
    cd newsapi-backend
    ```
2. Collect News API key
3. Configure environment variables
   
    A template file `.env.example` is provided:
    ```
    JWT_SECRET=<JWT_SECRET>
    JWT_ALGORITHM=HS256
    NEWS_API_KEY=<Your_News_API_KEY>
    NEWS_API_ENDPOINT=https://newsapi.org/v2/everything

    POSTGRES_HOST=<Your_Postgres_DB_Host>
    POSTGRES_PORT=<Your_Postgres_DB_Port>
    POSTGRES_NAME=<Your_Postgres_DB_Name>
    POSTGRES_USERNAME=<Your_Postgres_DB_Username>
    POSTGRES_PASSWORD=<Your_Postgres_DB_Password>
    ```

    Rename it to `.env` and update the values with your own configuration.


🐳 Run Docker

A `docker-compose.yaml` is included for full containerized development.

Start the containers:

    ```bash
    docker-compose up --build
    ```

Stop the containers:

    ```bash
    docker-compose down
    ```

🔧 Create the database (Docker Postgres)

1. Run the following command to create the database:
    ```bash
    docker exec -it postgres_db /bin/bash
    psql -U postgres
    CREATE DATABASE <Your_Postgres_DB_Name>;
    \q
    ```

📄 Endpoints

- POST `/auth/singup` – signup the user and the request body is similar to this:
    ```json
    {
        "email": "user@gmail.com",
        "password": "test",
        "first_name": "test",
        "last_name": "user",
        "username": "user"  
    }
    ```
    It will return you a response similar to this:
    ```json
    {
        "success": true,
        "message": "Request Success",
        "data": {
            "id": 2,
            "username": "user",
            "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyLCJleHAiOjE3NDUyMTk1MTYuMjMyNTM4fQ.tZ4NyjoCtZX52ZzTfbeQvXW-urMniR-SUmc0h-eDXc8"
        }
    }
    ```

- POST `/auth/login` – login the user and the request body is similar to this:
    ```json
    {
        "username": "user@gmail.com",
        "password": "test"
    }
    ```

- Collect the access token from the response and use it in the subsequent requests

- GET `/news/`  – fetch paginated articles (query params: page, limit)

- POST `/news/save-latest`  – fetch the latest headlines and save the top 3


