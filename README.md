# Dating Website

A web application that allows users to sign in with Google, live chat with other users, block and unblock users, and report inappropriate behavior. There are two kinds of accounts with different roles and levels of access: “User” and “Moderator”.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Features
- **User and Moderator Roles**: Users can chat, view profiles, block/unblock others, and report inappropriate behavior. Moderators can view reports and delete profiles if necessary.
- **Google Login**: Users can sign in using their Google account.
- **Profile Management**: Users have profiles with details like name, gender, email, and status.
- **Live Chat**: Users can request, accept, or decline chat requests and chat with matched users.
- **Reporting and Blocking**: Users can report profiles and block/unblock others. Moderators handle reports.

## Technologies Used
- **Python**
- **Django**
- **Google API**
- **Live Chat API**

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/dasdebanna/dating_website.git
    ```
2. Navigate to the project directory:
    ```bash
    cd dating_website
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the migrations:
    ```bash
    python manage.py migrate
    ```
5. Create a superuser for admin access:
    ```bash
    python manage.py createsuperuser
    ```
6. Start the development server:
    ```bash
    python manage.py runserver
    ```

## Usage
1. Open your browser and navigate to `http://127.0.0.1:8000`.
2. Sign in using your Google account or the admin credentials for moderator access.
3. Create and manage your profile, chat with other users, report inappropriate behavior, and block/unblock users as needed.

## Deployment
The project can be deployed on a live server using PythonAnywhere or similar services. Follow these steps for deployment on PythonAnywhere:
1. Sign up for a PythonAnywhere account.
2. Create a new web app and set the Python version.
3. Upload your project files and set up a virtual environment.
4. Configure the web app to point to your Django project's `wsgi.py` file.
5. Add your domain to the `ALLOWED_HOSTS` in the Django settings.
6. Set up the static files configuration and run the Django management commands.

## Contributing
Contributions are welcome! Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-branch
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m "Add new feature"
    ```
4. Push to the branch:
    ```bash
    git push origin feature-branch
    ```
5. Create a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
