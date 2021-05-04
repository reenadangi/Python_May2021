# Housekeeping 
* Week6 - Exam week
* 05/31 week - No Lectures 

# What all we have learned? 
* Functions
* Python OOP
* Setting up Django project
* Models(one-many and Many to many realtionships)
* Djnago ORM 
* Sessions

# What is important before exam 
* CRUD 
* validations
* bcrypt 
* Login and registration 

# RESTful Development & Fullstack Django
The client/server relationship is a prerequisite of a set of principles known as REST(representational state transfer) which provides a way of mapping HTTP verbs ( get, post, put/update, delete) and CRUD actions (create, read, update, delete) together.

|   NAME   |     PATH       |   HTTP VERB     |          PURPOSE                   |
|----------|----------------|-----------------|--------------------------------------| 
| Index    | /shows          |      GET        | Displays all shows                |   
| New      | /shows/new      |      GET        | Shows new form for new shows entry| 
| Create   | /shows/create          |      POST       | Creates a new show         | 
| Show     | /shows/:id      |      GET        | Display one specified show        | 
| Edit     | /shows/:id/edit |      GET        | Edit form for one show    |
| Update   | /shows/:id/update      |      PUT        | Updates a particular show       |
| Destroy  | /shows/:id/destroy      |      DELETE     | Deletes a particular show       |


