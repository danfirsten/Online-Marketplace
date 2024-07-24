# Online Marketplace

## Overview

Welcome to my Django-based online marketplace project! This project showcases the fundamental concepts and capabilities of Django by building a functional online marketplace where users can buy and sell items. Through the development of this project, I explored and implemented various critical features that are essential for a robust web application. The primary goal was to create a user-friendly platform that provides seamless interaction between buyers and sellers.

This project includes user authentication, enabling users to securely register, log in, and manage their accounts. Users can communicate with each other through an integrated messaging system, enhancing the interactive experience. Additionally, each user has access to a personalized dashboard where they can manage their listings, track their transactions, and view their profile information. Form handling and customization are also key aspects, ensuring that the forms are intuitive and meet the needs of the users. This project has been a comprehensive exercise in building a full-featured web application with Django, focusing on both back-end functionality and front-end user experience.

## Project Demo

[![Project Demo](https://img.youtube.com/vi/MNlnu1W9kYk/0.jpg)](https://youtu.be/MNlnu1W9kYk)

*Click the image to watch the video on YouTube.*

## Key Features

### Authentication

- Implemented user registration, login, and logout functionality.
- Password hashing and user session management for secure authentication.

### Communication Between Users

- Users can send and receive messages within the platform.
- Real-time notifications for new messages and interactions.

### Dashboard for Your Items

- Personalized dashboard for each user to manage their listed items.
- Overview of items being sold, items sold, and items bought.

### Form Handling and Customizations

- Customized forms for item listings, user profiles, and more.
- Client-side validation for enhanced user experience.

### And More

- Responsive design for seamless use across various devices.
- Search functionality to easily find items within the marketplace.
- User reviews and ratings for items and sellers.

## Getting Started

### Prerequisites

- Python (3.6+)
- Django (3.0+)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/Online-Marketplace.git
    cd online-marketplace
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up the database:

    ```bash
    python manage.py migrate
    ```

4. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

### Running the Project

1. Open your web browser and navigate to `http://127.0.0.1:8000/` to start using the online marketplace.

2. Use the admin interface at `http://127.0.0.1:8000/admin/` to manage users, items, and other data.

## Key Components

### Authentication

- **User Registration**: Allow users to create an account with email verification.
- **User Login**: Enable users to log in and manage their sessions securely.
- **User Logout**: Provide a way for users to log out and end their session.

### Communication Between Users

- **Messaging System**: Allow
