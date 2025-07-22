About the Project
This is a full-stack blog application, architected with a clear separation of concerns and containerized using Docker Compose. The stack includes:

React for a dynamic frontend,

Flask as a lightweight RESTful backend API,

PostgreSQL for relational data persistence,

and pgAdmin for managing and visualizing the database.

The purpose of this project was to practice real-world DevOps workflows by:

Designing services as loosely coupled containers,

Managing application dependencies through Dockerfiles,

Creating a production-similar local development environment,

Preloading the database using init scripts, and

Orchestrating all components using Docker Compose.

The backend exposes both:

A JSON API (/posts/json) for programmatic access, and

A server-rendered HTML page (/) to demonstrate Flask templating.
