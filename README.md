# Ketelopele Solutions website

This is the official website for Ketelopele Solutions. It provides comprehensive information about the company's background, services, products, and more. The site is built using the Django framework and is designed to be modern, user-friendly, and responsive.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Static Files](#static-files)
- [Templates](#templates)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.x
- Django 4.2.14
- Virtualenv (recommended)

### Setup

1. *Clone the repository:*

    bash
    git clone https://github.com/Ketelopele-Solutions/Ketelopele-Website.git
    cd Ketelopele-Website
    

2. *Create and activate a virtual environment:*

    bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    

3. *Install dependencies:*

    bash
    pip install -r requirements.txt
    

4. *Run database migrations:*

    bash
    python manage.py migrate
    

5. *Create a superuser:*

    bash
    python manage.py createsuperuser
    

6. *Run the development server:*

    bash
    python manage.py runserver
    

The website will be available at `http://127.0.0.1:8000/`.

## Usage

To use the website, navigate to the homepage at http://127.0.0.1:8000/. The website features the following pages:

1. *Homepage*: The landing page introducing Ketelopele Solutions.
   
2. *About Us*: Provides background information, an overview of the company, and details about staff and management.

3. *Services*: Describes the services offered and why clients should choose Ketelopele Solutions.

4. *Industries Served*: Lists the industries Ketelopele Solutions serves.

5. *Clients*: Showcases the clients Ketelopele Solutions has worked with.

6. *Certifications & Affiliations*: Provides information about affiliations and certifications held by Ketelopele Solutions.

7. *Products*: Details the products offered by Ketelopele Solutions.

## Project Structure

- `ketelopele/`: Main Django project directory.
- `static/`: Directory for static files (CSS, JavaScript, images).
  - `css/`: Stylesheets.
  - `images/`: Image files.
  - `js/`: JavaScript files.
- `templates/`: HTML templates for the website.
  - `home.html`: Template for the homepage.
  - `about.html`: Template for the About Us page.
  - `services.html`: Template for the Services page.
  - `industries.html`: Template for the Industries Served page.
  - `clients.html`: Template for the Clients page.
  - `certifications.html`: Template for the Certifications & Affiliations page.
  - `products.html`: Template for the Products page.
- `views.py`: View functions for handling page requests.
- `urls.py`: URL configurations for routing requests.

## Static Files

Static files (CSS, JavaScript, images) are stored in the `static`/ directory.

- *CSS*: Main stylesheet is located in `static/css/styles.css`.
- *JavaScript*: Custom JavaScript files are located in `static/js/main.js`.
- *Images*: Images, including logos and background images, are stored in `static/images/`.

## Templates

HTML templates are stored in the templates/ directory. Each page has its respective template:

- `home.html`
- `about.html`
- `services.html`
- `industries.html`
- `clients.html`
- `certifications.html`
- `products.html`

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests for any changes you'd like to make.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
