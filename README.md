# University Department Management Web App with Django

This web application is designed to manage the various departments within a university. The application is built using Django, a popular Python-based web framework. The application can be used by faculty members, staff, and administrators to manage various aspects of their department, including course schedules, course assignments, and faculty evaluations.

Features:

* **Login/Registration:** Users can create an account and log in to the system.
* **User Roles:** The application has different roles for users such as faculty, staff, and administrators.
* **Department Management:** Users can manage various departments within the university, including creating new departments, modifying existing departments, and deleting departments.
* **Course Management:** Users can create and manage courses within a department, including adding new courses, modifying existing courses, and deleting courses.
* **Course Assignments:** Users can assign faculty members to specific courses and manage the assignments of courses to the faculty.
* **Faculty Evaluations:** Users can evaluate faculty members based on various criteria such as teaching, research, and service. These evaluations are used for performance reviews and promotions.

## Installation:

1. Clone the repository to your local machine.
2. Create a virtual environment for the project.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Run `python manage.py migrate` to apply the migrations.
5. Create a superuser using `python manage.py createsuperuser`.
6. Start the development server using `python manage.py runserver`.

### Contributing:
Contributions to this project are welcome. If you want to contribute, please fork the repository and create a pull request.

### License:
This project is licensed under the MIT License. See the LICENSE file for more information.