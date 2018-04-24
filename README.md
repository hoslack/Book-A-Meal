[![Maintainability](https://api.codeclimate.com/v1/badges/1d4881923768a4d093a0/maintainability)](https://codeclimate.com/github/hoslack/Book-A-Meal/maintainability)
[![Build Status](https://travis-ci.org/hoslack/Book-A-Meal.svg?branch=master)](https://travis-ci.org/hoslack/Book-A-Meal)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/763d0acb69e1418ca72d9f7c0e7ad2f5)](https://www.codacy.com/app/hoslack/Book-A-Meal?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=hoslack/Book-A-Meal&amp;utm_campaign=Badge_Grade)
# Book-A-Meal
## What? 
Book-A-Meal is an application that allows customers to make food orders and helps the food vendor know what the customers want to eat.
## Features
- Users can create an account and log in
- Admin (Caterer) should be able to manage (i.e: add, modify and delete) meal options in the application. Examples of meal options are: Beef with rice, Beef with fries etc
- Admin (Caterer) should be able to setup menu for a specific day by selecting from the meal options available on the system.
- Authenticated users (customers) should be able to see the menu for a specific day and select an option out of the menu.
- Authenticated users (customers) should be able to change their meal choice.
- Admin (Caterer) should be able to see the orders made by the user
- Admin should be able to see amount of money made by end of day
### Extra features
- Authenticated users (customers) should be able to see their order history
- Authenticated users (customers) should be able to get notifications when the menu for the day has been set.
- Admin (Caterer) should be able to see order history
- The application should be able to host more than one caterer.

## Screenshots of the UI
![Index](http://res.cloudinary.com/hoslack/image/upload/v1524319692/imageedit_5_6173175048_vnobg8.png)


![Sign Up](http://res.cloudinary.com/hoslack/image/upload/v1524319699/imageedit_6_4169369105_ekaxlm.png)


![Sign In](http://res.cloudinary.com/hoslack/image/upload/v1524319706/imageedit_7_5004553090_i3lgvg.png)

## Technology Stack:
- [PostgreSql](https://www.postgresql.org/) with [SQLAlchemy](https://www.sqlalchemy.org/) (database and ORM)
- [Flask](http://flask.pocoo.org/) (A Python microframework)
- [Reactjs](https://reactjs.org/) (A javaScript front-end framework)
- HTML and CSS

## Tools:
- [Pivotal Tracker](www.pivotaltracker.com) (A project management tool)

## Getting Started
If you want to try out this application at this stage of development you just have to follow the simple instructions below:

On your terminal, paste these commands one by one.

`git clone https://github.com/hoslack/Book-A-Meal.git`

`cd Book-A-Meal`

`pip install -r requirements.txt`

The run tests 
`pytest tests`

## Contributing
I appreciate your eagerness to chip in in this wonderful course but you will have to wait for a **month** or two. :blush:

## Author
- **Hoslack Ochieng** [@Hoslack](@hoslack)

## Licensing 
Book-A-Meal is [MIT Licensed](LICENSE.md)

## Acknowledgements
[Andela](andela.com) - *for giving me the chance and an awesome community to work with*
