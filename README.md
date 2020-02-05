# Task Tracker

The purpose of the site is for educational purposes to test the developer knowledge of CRUD (Create, Read, Update & Delete).

The site is designed to track tasks required in the completion of projects and enable project owners to easily assign each task to a
specific user and review updates and completion.

There are 3 main elements to the database collections employed in the site.

1.  Projects
2.  Tasks
3.  Staff

# User Experience & Interface Design

The user interface screens and views were designed to keep the type of data controlled and also provide an intuitive layout with progressive
functionality.

The screens are kept minimalist and clutter free to allow the user a clear view of what is required in the completion of inputs and updates.

All Addition & Editing screens are kept similar in design, layout and colour in order to give the user an element of familiarity when transitioning from
screen to screen.

The design also allows for future features and additions to be applied without extensively changing the current layout of the screens or adding any complexity to
user experience

## Note: 
The delete function is uncontrolled as authentication is not a requirement feature of this Milestone Project and is assigned as
a new release feature to be enabled in Release 2.0 of the site.

### Home Page / View Tasks

The home page provides a view of all tasks currently assigned and can be either active or completed. Only when a task is deleted will it be
removed from this view.

All fields and switches are disabled on the home page to ensure no accidental edits or deletion are applied when viewing tasks.

![index](static/readme_images/viewtasks.jpg)



### Projects

#### Add Projects

This screen enables the user to add a new project to the workstream and consists of 3 entry options

1.  Project Name - The name of the overall project for which team tasks are to be applied and assigned.
2.  Project Description - A summarised description of the project and purpose.
3.  Project Owner - The staff member within the team responsible for driving team tasks to completion.


![index](static/readme_images/add_project.jpg)

#### Manage Projects

This screen enables the user to edit or delete an existing project in the workstream.

The screen displays the Project Name & Owner with a dropdown option to view the Project Description.

The are also 2 button options for Del & Edit

![index](static/readme_images/edit_project.jpg)


### Tasks

#### Add Task

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

#### Manage Tasks

This screen enables the user to edit or delete an existing task in the workstream.

The screen displays the Project Name, Task Name, Due Date & Assigned To fields with a dropdown option to view the Task Description.

The are also 2 button options for Del & Edit

![index](static/readme_images/edit_task.jpg)

The edit option also provides an additional switch to be enabled should the task be completed.

### Staff

#### Add Staff

This screen enables the user to add a new project to the workstream and consists of 3 entry options

1.  Staff Name - Staff member to be added to the task assignment list.
2.  Staff Team - The team or group the staff member belongs to.


![index](static/readme_images/add_staff.jpg)

#### Manage Staff

This screen enables the user to edit or delete an existing project in the workstream.

The screen displays the Staff Name with a dropdown option to view the Staff Team.

![index](static/readme_images/edit_project.png)


## Future Release & development



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


# TESTING

The testing methodology was agreed by the team and based on manual process covering agreed criteria.

The first element of testing covered the layout and presentation of the pages to ensure they met the requirements set out
in the scope and satisfied the expectations of the user base.

Each element was reviewed by the testing team and given a 'pass' or 'fail' score - a 'pass' would result in the design Sprint
being signed off and a 'fail' resulted in that sprint being returned to the developer with comment and instruction to resolve
the reported issue.

Layout & Presentation test results

![index](assets/documents/testing/layout_test_results.png)


The 2nd phase of testing covered the functionality and useability of the index.html (Task Analysis Dashboard) and was tested to
ensure all required aspects of the page complied with requirements.

All dashboard functionality was tested by the team during this testing phase and the 'pass' or 'fail' score was applied to the
results with 'fail' being returned for action and resolution.

Task Dashboard Test Results

![index](assets/documents/testing/task_dashboard_test_results.png)


The 3rd phase of testing covered the functionality and useability of the time.html (Time Analysis Dashboard) and was tested to
ensure all required aspects of the page complied with requirements.

All dashboard functionality was tested by the team during this testing phase and the 'pass' or 'fail' score was applied to the
results with 'fail' being returned for action and resolution.

Time Dashboard Test Results

![index](assets/documents/testing/time_dashboard_test_results.png)

The pages are not required to be device responsive and, therefore, was only tested to ensure they displayed correctly on
desktop screens and overhead projection units

HTML, CSS & Javascriot Validation

HTML code was validated using https://validator.w3.org/

CSS code was validated using https://jigsaw.w3.org/css-validator/

Javascript checked with https://jshint.com/


# DEPLOYMENT

## GitHub

This site is hosted on GitHub and deployed directly from the master branch. Any commit updates or new releases will be deployed to that master branch. In order for the site to deploy correctly on GitHub pages, the landing page must be named index.html.

To run locally, you can clone this repository directly into the editor of your choice by pasting git clone https://github.com/Mofarrell1967/Staff-Analysis-Dashboards into your terminal. To unlink the site from the GitHub repository, type git remote rm origin into the terminal.

The site is hosted on GitHub and can be run from there or locally by pasting the following link directly into your browser. https://mofarrell1967.github.io/Staff-Analysis-Dashboards/

To view the source code please click on the following GitHub address https://github.com/Mofarrell1967/Staff-Analysis-Dashboards


## Company Deployment

Deployment within the company pages will be applied through the copying of the source code from the GitHub pages and placing the code in the local company Sharepoint resource pages.
The code will then be updated to use the production data source files instead of the test csv source.

Locations and paths for this deployment cannot be viewed from this page as per company security policies.

# CREDITS

### content

Thanks go to John Alexis Guerra Gómez for the youtube tutorial which was used to assist in the development of the table and row charts

https://www.youtube.com/watch?v=8TBh5ghRZrI

Code Institute for the educational modules used as partial templates for the bar graphs and functionality

https://courses.codeinstitute.net/program/FullstackWebDeveloper


### Acknowledgements

BT Capacity team for the SOR and testing of the pages

CA for the inspiration in moving to dashboards from the existing reporting methods

**Please Note that this site is currently for educational purposes only**










