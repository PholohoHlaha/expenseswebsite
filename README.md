Expenses Website Project
Overview

This project, developed using Python, JavaScript, and Docker, aims to test the interactivity between Django and ReactJS, and how they communicate. ReactJS was used for the admin side, while Django is used to develop the user side of the system. The project includes a map to locate all WASCO plants available in Lesotho, such as Metolong, Matamong, Hlotse, Agric College Lesotho, and others. Though this is a finished project, there are plans for future enhancements.
Features

    Django Backend: Handles the user side of the system.
    ReactJS Frontend: Manages the admin side of the system.
    Docker Integration: Utilizes Docker for containerization and easy deployment.
    PostgreSQL Database: For data storage and management.
    Zookeeper: Included for potential future enhancements.
    Map Integration: Locates WASCO plants in Lesotho.

Installation
Prerequisites

    Docker
    Docker Compose

Step-by-Step Installation
1. Clone the Repository

sh

git clone https://github.com/your-username/expenseswebsite.git
cd expenseswebsite

2. Set Up the Environment

Ensure you have the necessary environment variables set up in the .env file.
3. Build and Run the Containers

sh

docker-compose up --build

Container Configuration

The project utilizes Docker containers as follows:

yaml

version: '3'

services:
  django:
    image: django-docker:0.0.1
    build: .
    ports:
      - "8000:8000"

  zookeeper:
    image: 'bitnami/zookeeper:latest'
    environment:
      - ALLOW_ANONYMOUS_LOGIN=yes
    ports:
      - '2181:2181'
  
  db:
    container_name: postgresql_db
    image: postgres
    restart: always
    environment:
      POSTGRES_USER: root
      POSTGRES_PASSWORD: root
      POSTGRES_DB: test_db
    ports:
      - '5433:5432'
  
  pg-admin:
    container_name: pgadmin4
    image: dpage/pgadmin4
    restart: always
    environment:
      PGADMIN_DEFAULT_EMAIL: root@root.com
      PGADMIN_DEFAULT_PASSWORD: root
    ports:
      - '5050:80'

  adminer:
    image: adminer
    restart: always
    ports:
      - 8080:8080

Accessing the Application

    Django Application: http://localhost:8000
    pgAdmin: http://localhost:5050
    Adminer: http://localhost:8080

Usage

    Admin Access:
        Username: admin@admin.com
        Password: password

    Map Feature: Locate WASCO plants in Lesotho such as Metolong, Matamong, Hlotse, Agric College Lesotho, and others.

Future Enhancements

    Additional Features: Plan to add more features to enhance the system.
    Improved User Interface: Make the user interface more intuitive and user-friendly.
    Performance Optimization: Optimize the performance of the application.

License

This project is licensed under the MIT License.
Contact

For any inquiries or questions, please contact Pholoho Hlaha.
