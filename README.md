# 🐱 Cats Catalogue

This project represents a full-stack microservices application, that consists of a small frontend written in React, a backend in Python with Flask, and a relational database.

## 🚀 How to Deploy the Project on AWS

### Prerequisites
- Ensure you have Terraform installed on your system.
- AWS credentials should be configured on your machine to allow Terraform to provision resources.

### Steps to Deploy
1. Navigate to the Terraform directory:
   ```bash
   cd /path/to/DevOps-Final-Project/terraform
   ```

2. Initialize Terraform:
   ```bash
   terraform init
   ```

3. Validate the Terraform configuration:
   ```bash
   terraform validate
   ```

4. Plan the infrastructure changes:
   ```bash
   terraform plan
   ```

5. Apply the changes to deploy the infrastructure and application:
   ```bash
   terraform apply
   ```

6. Access the application:
   - **Frontend**: Open your browser and navigate to `http://<LOAD_BALANCER_DNS>:5173`.
   - **Backend**: The backend API is available at `http://<LOAD_BALANCER_DNS>:5000`.

### Notes
- Replace `<LOAD_BALANCER_DNS>` with the DNS name of your load balancer.
- Ensure the necessary ports (5000, 5173) are open in your security group settings.

Enjoy exploring the Cats Catalogue! 🐾

## 🛠 How to Run the Project Locally

### Prerequisites
- Ensure you have Docker and Docker Compose installed on your system.
- Clone this repository to your local machine:
  ```bash
  git clone https://github.com/dianamartisca/DevOps-Final-Project.git
  cd DevOps-Final-Project
  ```

### Steps to Run Locally
1. Start the application using Docker Compose:
   ```bash
   docker-compose up -d
   ```

2. Access the application:
   - **Frontend**: Open your browser and navigate to `http://localhost:5173`.
   - **Backend**: The backend API is available at `http://localhost:5000`.

3. To stop the application:
   ```bash
   docker-compose down
   ```

### Notes
- Ensure that ports `5173` and `5000` are not in use by other applications on your local machine.
- The database data will persist in the Docker volume defined in the `docker-compose.yml` file.