# Features

- User login and registration system.
- Groups and permissions.
- Restrict users CRUD operations based on groups they belong.
- Records listing, detail and form views for CRUD operations.
- Class based views.
- Custom user model.
- Validation on models.
- Django signals.
- Pagination.

# Project Setup

This project was created using Python 3.8.10. It shows the implementation of permissions and groups in django.

### 1. Installation

Install the required packages using the following command:
```sh
pip install -r requirements.txt
```

### 2. Apply migrations

Apply migrations and create database using the following command:
```sh
python manage.py makemigrations
python manage.py migrate
```

### 3. Create Super User

To create superuser, use the following command:
```sh
python manage.py createsuperuser
```

### 4. Running the Django Server

To run the Django server, use the following command:
```sh
python manage.py runserver
```

# Instructions

- Admin have all the permissions and access for operations
- Newly registered user are added to default group (with no access permission) using post save signal.
- Admin can create group, and add permission to already created groups in
Admin Panel under ‘Groups’
- Admin can add users to the groups which grant them different levels of
access, in Admin Panel under ‘Custom Users’ and going in user then
assigning group to it.
- Users created via website have by default `staff=False` so they cannot login in admin panel.

### Already Available Groups:

1. Default: no permission
2. Resident manager: read, create, update resident table
3. Community manager: read create, update, delete community events
table
4. Operation Manager: read, delete, from both resident &amp; community
events table
5. Sales Executive: read from both resident &amp; community events table