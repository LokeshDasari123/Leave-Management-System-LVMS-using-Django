# Leave Management System (LVMS) Using Django

This is a basic **Leave Management System (LVMS)** developed using Django, intended to demonstrate the core functionalities of leave management for teachers and students in an educational institution.

## Features

- **User Roles**: Different roles such as Teachers and Students with separate leave request workflows.
- **Leave Request**: Users can apply for leave by filling out a form.
- **Leave Status**: Admins can view, approve, or reject leave requests.
- **Basic Dashboard**: Simple dashboard with leave request statistics for Admins.
- **SQLite Database**: Uses Django's default `db.sqlite3` for data storage.
- **Basic HTML/CSS/Bootstrap**: Frontend styled with Bootstrap to make the interface clean and responsive.

## Prerequisites

To run this project, you will need the following:

- [Python 3.x](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/)

## Setup Instructions


1. **Install Dependencies**

   Make sure all necessary dependencies are installed. This typically involves using a requirements file to install dependencies.

2. **Run Database Migrations**

   Set up the database by running the migrations to create the necessary tables.

3. **Create a Superuser (Admin)**

   Create an admin account to access the Django admin panel and manage leave requests.

4. **Run the Development Server**

   Start the Django development server to test and run the application locally.

5. **Accessing the Application**

   - **Admin Panel**: Use the admin credentials to log in and manage leave requests.
   - **User Interface**: Teachers and students can log in, apply for leave, and track leave status.
