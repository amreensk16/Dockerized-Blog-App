🚀 Dockerized Blog App — Full Stack Project

A simple full-stack blogging app built with React, Flask, and PostgreSQL, fully containerized using Docker Compose.


🧠 About the Project
-----------------------
This is a full-stack blog application, architected with a clear separation of concerns and containerized using Docker Compose. The stack includes:
-> React for a dynamic frontend,
-> Flask as a lightweight RESTful backend API,
-> PostgreSQL for relational data persistence,
-> and pgAdmin for managing and visualizing the database.

The purpose of this project was to practice real-world DevOps workflows by:
-> Designing services as loosely coupled containers,
-> Managing application dependencies through Dockerfiles,
-> Creating a production-similar local development environment,
-> Preloading the database using init scripts, and
-> Orchestrating all components using Docker Compose.

The backend exposes both:
-> A JSON API (/posts/json) for programmatic access, and
-> A server-rendered HTML page (/) to demonstrate Flask templating.


✨ Why This Project?
-----------------------
As someone pursuing a DevOps Engineering role, I built this project to:
-> Demonstrate my ability to integrate infrastructure + development layers,
-> Show hands-on Docker & PostgreSQL skills,
-> Practice writing clean and scalable Docker Compose configurations,
-> Understand how databases, backend APIs, and frontends interact, and
-> Deliver a functional, readable, and testable system with minimal overhead.


📂 Project Structure
-----------------------

Dockerized-Blog-App/
│
├── backend/         # Flask API to serve posts
│   └── app.py
│   └── templates/
│       └── posts.html
│
├── frontend/        # React frontend 
│   └── App.js
│
├── init.sql         # PostgreSQL schema + seed data
├── docker-compose.yml
├── README.md
└── screenshots/     # Add your app screenshots here


🛠️ Features
---------------
📄 Lists blog posts with title and content
🔗 API returns JSON for frontend consumption
📦 PostgreSQL preloaded with sample data using init.sql
🌐 CORS enabled for frontend-backend communication
📊 pgAdmin4 interface to inspect DB manually


🚀 How to Run
----------------
Requires Docker & Docker Compose installed

# Clone the repository
git clone https://github.com/amreensk16/Dockerized-Blog-App.git
cd Dockerized-Blog-App

# Start all services
docker-compose up --build

Frontend → http://localhost:3000

Backend JSON API → http://localhost:5000/posts/json

Flask Rendered HTML → http://localhost:5000

pgAdmin → http://localhost:5050 (Login with: admin@admin.com / admin123)


📥 Sample Data
-----------------
-- From init.sql

-- Authors
INSERT INTO authors (name, email) VALUES
('Alice Johnson', 'alice@example.com'),
('Bob Smith', 'bob@example.com');

-- Posts
INSERT INTO posts (title, content, author_id) VALUES
('First Post', 'Hello, this is my first post! I am here to create a aesthetic portfolio of mine', 1),
('Second Post', 'Another day, another post. The climate is so cool today', 2);


✨ Screenshots
------------------
screenshots/
├── ui-home.png        # Flask-rendered homepage
├── pgadmin-db.png      # Sample pgAdmin UI with tables
├── api-respose.png        # JSON response from /posts/json


