# Task Tracker

The purpose of the site is for educational purposes to test the developer knowledge of CRUD (Create, Read, Update & Delete).

The site is designed to track tasks required in the completion of projects and enable project owners to easily assign each task to a
specific user and review updates and completion.

There are 3 main elements to the database collections employed in the site.

1.  Projects
2.  Tasks
3.  Staff

# User Experience & Interface Design

The user interface screens and views were designed to keep the type of data controlled and provide an intuitive layout with progressive
functionality.

The screens are kept minimalist and clutter free to allow the user a clear view of what is required in the completion of inputs and updates.

All Addition & Editing screens are kept similar in design, layout and colour in order to give the user an element of familiarity when transitioning from
screen to screen.

The design also allows for future features and additions to be applied without extensively changing the current layout of the screens or adding any complexity to
user experience

#### Note: 
The delete function is uncontrolled as authentication is not a requirement feature of this Milestone Project and is assigned as
a new release feature to be enabled in Release 2.0 of the site.

## Home Page / View Tasks

The home page provides a view of all tasks currently assigned and can be either active or completed. Only when a task is deleted will it be
removed from this view.

All fields and switches are disabled on the home page to ensure no accidental edits or deletion are applied when viewing tasks.

![index](static/readme_images/view_tasks.jpg)

## Projects

### Add Projects

This screen enables the user to add a new project to the workstream and consists of 3 entry options

1.  Project Name - The name of the overall project for which team tasks are to be applied and assigned.
2.  Project Description - A summarised description of the project and purpose.
3.  Project Owner - The staff member within the team responsible for driving team tasks to completion.


![index](static/readme_images/add_project.jpg)

### Manage Projects

This screen enables the user to edit or delete an existing project in the workstream.

The screen displays the Project Name & Owner with a dropdown option to view the Project Description.

![index](static/readme_images/manage_project.jpg)

There are also 2 button options for Del & Edit

![index](static/readme_images/edit_project.jpg)

## Tasks

### Add Task

This screen enables the user to add a new project to the workstream and consists of 3 entry options

1.  Project Name - The project name to be chosen from a dropdown list of existing projects.
2.  Task Name - Name applied to the specific tasks.
3.  Task Description - A brief description of the tasks and the requirements for completion.
4.  Assign To - The name of the staff member the task is to be assigned to, available from a dropdown list of existing staff members.
5.  Due Date - The date by which the task is to be completed.

There are also 3 switches to record if the task is;

Is Key - is this a key task that should be given a higher priority.
External Customer - to be enabled if the task is for an external customer project.
Is Billable - to be enabled if there is a cost applied to the task and a revenue source is provided

![index](static/readme_images/add_task.jpg)

### Manage Tasks

This screen enables the user to edit or delete an existing task in the workstream.

The screen displays the Project Name, Task Name, Due Date & Assigned To fields with a dropdown option to view the Task Description.

![index](static/readme_images/manage_task.jpg)

There are also 2 button options for Del & Edit

![index](static/readme_images/edit_task.jpg)

The edit option also provides an additional switch to be enabled should the task be completed.

## Staff

### Add Staff

This screen enables the user to add a new project to the workstream and consists of 3 entry options

1.  Staff Name - Staff member to be added to the task assignment list.
2.  Staff Team - The team or group the staff member belongs to.

![index](static/readme_images/add_staff.jpg)

### Manage Staff

This screen enables the user to edit or delete an existing project in the workstream.

The screen displays the Staff Name with a dropdown option to view the Staff Team.

![index](static/readme_images/manage_staff.jpg)

There are also 2 button options for Del & Edit

![index](static/readme_images/edit_staff.jpg)

# Future Release & development

•	A search bar to be added to the html to allow users to query the database.

•	Pagination to be applied to the view and edit screens to cater for growing number of tasks and projects.

•	Authentication to be applied to validate users and manage deletions of tasks, projects & staff.

# TECHNOLOGIES

*   [Materialize](https://materializecss.com/) - For HTML and CSS design, layout & Styles
*   [Python](https://www.python.org/) -   programming language that lets you work quickly and integrate systems more effectively
*   [JQuery](https://www.jquery.com/) -   To support the development for the pages
*   [MongoDB](https://www.mongodb.com/) -   general purpose, document-based, distributed database
*   [Flask](https://www.palletsprojects.com/p/flask/) -   Flask is a lightweight WSGI web application framework
*   [Heroku](https://www.heroku.com/home) -   Deploy and run apps

*   Click==7.0
*   Flask==1.0.2
*   Flask-PyMongo==2.2.0
*   itsdangerous==1.1.0
*   Jinja2==2.10
*   MarkupSafe==1.1.0
*   pymongo==3.7.2
*   Werkzeug==0.14.1
*   dnspython==1.16.0

# Testing

## Manual Tests

This web application has been manually tested with different scenarios that the user may experience.
Every route in the App.py was tested when added to ensure functionality, syntax and output was correct. When all routes were tested and applied to the html pages, 
the following manual tests were completed

###     Viewtasks

   1. Click on each field to ensure that all a disabled from edit or delete'.

### 	Home link on Navbar

   1. Check link is working and takes user back to Viewtasks.html from any screen.

###     Add Task

   1. Click on menu option to ensure link opens correctly
   2. Enter test date to each field'
   3. Enable / Disable all switches
   4. Choose save option and check that records are visible in Viewtasks.html
   5. Choose cancel option and confirm ‘Manage Tasks’ page is opened

### 	Manage Tasks

   1. Choose dropdown to ensure ‘Task Description field displays correctly.
   2. Click on ‘Edit’ and confirm that “Edit’ page opens correctly.
   3. Edit all fields and ‘Save – confirm that changes are visible in Viewtasks.html.
   4. Choose cancel option and confirm ‘Manage Tasks’ page is opened.
   5. Choose 'Del' option and confirm that records are deleted from Database and Manage Tasks page

### 	Add Project

   1. Click on menu option to ensure link opens correctly 
   2. Enter test date to each field'.
   3. Choose save option and check that records are visible in Viewtasks.html.
   4. Choose cancel option and confirm ‘Manage Projects’ page is opened.

###     Manage Projects

   1. Choose dropdown to ensure ‘Project Description field displays correctly.
   2. Click on ‘Edit’ and confirm that “Edit’ page opens correctly.
   3. Edit all fields and ‘Save – confirm that changes are visible in Manage Projects page.
   4. Choose cancel option and confirm ‘Manage Projects’ page is opened.
   5. Choose 'Del' option and confirm that records are deleted from Database and Manage Project page

### 	Add Staff

   1. Click on menu option to ensure link opens correctly 
   2. Enter test date to each field'.
   3. Choose save option and check that records are visible in Manage Staff page.
   4. Choose cancel option and confirm ‘Manage Staff’ page is opened.

### Manage Staff

   1. Choose dropdown to ensure ‘Staff Team field displays correctly.
   2. Click on ‘Edit’ and confirm that “Edit’ page opens correctly.
   3. Edit all fields and ‘Save – confirm that changes are visible in Manage Staff page.
   4. Choose cancel option and confirm ‘Manage Staff’ page is opened.
   5. Choose 'Del' option and confirm that records are deleted from Database and Manage Staff page

## Responsiveness Testing

This application has been tested on all mobile, tablet and desktop screen sizes Google Chrome Developer Tools.
On desktop the application was tested on Chrome, Mozilla & MS Edge.
On Tablet and Mobile the application was tested on Chrome & Samsung Internet App.
Virtual testing on Apple devices was completed using Chrome Developer Tools.

## Code Validation

The HTML, CSS and JavaScript code for this application has been run through and validated by The W3C Markup Validation Service and JSHint, 
with the exception of the validation service seeing the Flask/Jinja markup as errors.

# DEPLOYMENT

## GitHub

This site is hosted on GitHub and deployed directly from the master branch. Any commit updates or new releases will be deployed to that master branch. 

To run locally, you can clone this repository directly into the editor of your choice by pasting git clone https://github.com/Mofarrell1967/task-tracker.git into your terminal. 
To unlink the site from the GitHub repository, type git remote rm origin into the terminal.

To view the source code please click on the following GitHub address https://github.com/Mofarrell1967/task-tracker

## Heroku

The application has been deployed onto Heroku. There is no difference between the GitHub code and the code in the live application.

It can be installed with the following steps:

*   Download the git repository
*   Sign up/login to Heroku.com
*   From the dashboard click Create New App
*   Enter a unique name and your region and click Create
*   From your command line, enter heroku to ensure heroku is installed (if not installed this can be done with sudo snap install --classic heroku)
*   Log in to heroku using 'heroku login' at the command line
*   Enter your credentials for heroku.com
*   sudo pip3 install Flask
*   sudo pip3 install pymongo
*   sudo pip3 install dnspymongo
*   sudo pip3 freeze --local > requirements.txt
*   echo web: python run.py > Procfile
*   git add .
*   git commit -m "initial commit"
*   git push -u heroku master
*   heroku ps:scale web=1
*   Make sure to set debug to True.
*   In heroku.com app settings: set config vars to IP : 0.0.0.0, PORT : 5000
*   Click More > Restart all Dynos
*   Application is live at https://your-app-name.herokuapp.com/

# CREDITS

### content

Code Institute for the educational modules used as partial templates for the bar graphs and functionality

https://courses.codeinstitute.net/program/FullstackWebDeveloper


**Please Note that this site is currently for educational purposes only**









