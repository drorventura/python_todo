# Python Interview Task: TODO App

## Guide to run
docker-compose up --build
service will run on http://localhost:8080
mongo will run on mongodb://mongo:27017

## Task Overview

In this task, you'll work on enhancing a simple TODO application by integrating it with a MongoDB database and containerizing it using Docker. Follow the steps below to complete the task.

## Instructions

### 1. Clone the Repository
   - **Objective**: Get the codebase on your local machine.
   - **Instructions**: Clone the provided repository using Git.

### 2. Run the TODO App Locally
   - **Objective**: Set up and run the TODO application on your local environment.
   - **Instructions**: Install dependencies and run the application locally and play with it's UI.

### 3. Add a New Endpoint: `/migrate`
   - **Objective**: Migrate existing data from `database.json` to a MongoDB database.
   - **Instructions**:
     1. Create a new endpoint `/migrate`.
     2. This endpoint should:
        - Read the `database.json` file.
        - Ingest all records into a local MongoDB database.
     3. Ensure proper error handling during the migration process.
   - **Note**: An initial `database.json` file is provided.

### 4. Modify Existing Endpoints
   - **Objective**: Update the TODO application's existing endpoints to interact with MongoDB.
   - **Instructions**:
     1. Refactor the data layer to use MongoDB instead of the existing data storage method.
     2. Ensure all existing endpoints (CRUD operations) work correctly with the new MongoDB integration.
     3. Maintain existing functionality and add necessary error handling.

### 5. Dockerize the TODO Application
   - **Objective**: Containerize the TODO application for easy deployment.
   - **Instructions**:
     1. Create a `Dockerfile` to containerize the application.
     2. Optionally, create a `docker-compose.yml` file if multiple services (e.g., MongoDB) are needed.
   - **Note**: Ensure the Docker setup allows for easy running of the application.
