# KulpDev_Mayur

1. **Clone the Repository**
   ```sh
   git clone <repository-url>
   cd <repository-directory>

Create a Virtual Environment

```sh
python -m venv venv
  ```
Activate the Virtual Environment:

On Windows:
```sh
.\venv\Scripts\activate

```
On macOS/Linux:

```sh
source venv/bin/activate

```
Install Dependencies

```sh
pip install -r requirements.txt
```


Configure Settings
Edit settings.py to configure your database, static files, and secret key.

Apply Migrations

```sh
python manage.py makemigrations
python manage.py migrate

```
Create a Superuser

```sh
python manage.py createsuperuser
```

Run the Development Server

```sh
python manage.py runserver
```

Deploy the Application
Follow the instructions for your chosen hosting platform to deploy the application.

Testing
Run tests using:

```sh
python manage.py test
```




These instructions should guide you through setting up your blog platform locally and prepa
