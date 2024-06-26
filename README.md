﻿

See live site [here](https://artspill-876968932494.herokuapp.com/).



# Artspill?
The idea behind artspill was to create a minimalistic website for artists to showcase and share their work, with the ability to comment and like each others pieces.

#

- [Introduction](#introduction)
    - [User Goals](#user-goals)
    - [Site Goals](#site-goals)
- [Agile and User stories](#agile-and-user-stories)


- [Design](#design)

- [Features](#features)
- [Structure](#structure)
- [CRUD](#crud)
- [Testing](#testing)
    
    - [Code](#code)
    - [No errors](#no-errors)
    
    - [Accessability](#accessability)
    - [Manual testing](#manual-testing)
- [Bugs](#bugs)
- [Future implements](#future-implements)
- [Deployment](#deployment)
- [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks](#frameworks)
    - [Tools](#tools)
    - [Libraries](#libraries)
    - [Packages](#packages)
- [Resourses](#resourses)
    - [Images](#images)
    - [Credits](#credits)

# Introduction

## User goals
- To join a community of artists and art lovers
- To share my art pieces and interact with other's creations
- To get inspiration from other artists
- To learn about different forms of art and their workflow

## Site goals
Artspill aims to provide artists from all skill levels with a place to express themselves, communicate with other artists and develop a collection of favorite pieces.



# Agile and User Stories
I created a GitHub Project that uses an agile approach with the help of a Kanban board method. This made it easy to visuallize and execute user stories and see them to completion. See [Here](https://github.com/users/caninereason/projects/3) for the full project.


# Design

I used a minimalistic design to help focus on the artwork contained within, the site is quite basic with only minor tweaks to keep the website responsive.


# Features

- Home page
    - Navbar

    The navbar consists of a basic Bootstrap navbar with login or register links should the user not be logged in. If the user is logged in this changes to logout, create post and a profile link to view the user's posts, favorites and comments. Also if the user is logged in they can edit or delete the posts which they have created, this is an option both  on the main page and the detail page of the post.

    - Profile page
    The profile page contains the user's data such as name, email, posts created by that user , favorites of that user and comments created by that user.
   

    ![Image](https://res.cloudinary.com/dzgmi2kgu/image/upload/v1691340455/2023-08-06_17_46_48-Window_x676tk.png)

    - Footer

    The footer is very basic and straightforward, offering links to social media.

    
    - Create a new post
    

    The user is brought to a simple form where they can specify the name, image and add a description below the post if desired

    - Edit post

    The user can edit their post, changing title, image and description.

    
    - Delete post

    If the user wishes to delete their post, they will be met with a popup to ensure they did not miss click the button

    - Favourite post
    The user can click on the heart icon either in the index page, or on the detail page, which will add the post to their profile favourites.

    - Sign in

    As with Account Creation, signing in is just as easy, offering only what's needed. 

      
    - Sign out

    When the user signs out, they'll be directed to a page asking them if they're sure to sign out, giving them the option to proceed with the sign out or cancel, returning them to the home page.

    


# Structure

## CRUD

- Create: An authenticated user can create and submit a post.
- Read: A user can browse all the posts.
- Update: An authenticated user can edit their own submitted posts.
- Delete: An authenticated user can delete their own submitted posts.

## Custom model

I created two custom models, a comment model and a favourite model, both were fairly easy to implement and work accordingly.
# Testing



## Code

[W3 HTML checker](https://validator.w3.org)

All website pages have been run through W3, with no errors.

## No errors

<details>
<summary>View all results with no errors.</summary>
<br>

- Sign in

![SignIn](https://validator.w3.org/nu/?doc=https%3A%2F%2Fartspill-876968932494.herokuapp.com%2Faccount%2Flogin%2F)

- Sign out

![SignOut](https://validator.w3.org/nu/?doc=https%3A%2F%2Fartspill-876968932494.herokuapp.com%2Faccount%2Flogout%2F)

- Sign up

![SignUp](https://validator.w3.org/nu/?doc=https%3A%2F%2Fartspill-876968932494.herokuapp.com%2Faccount%2Fsignup%2F)

 - Home page

![Home](https://validator.w3.org/nu/?doc=https%3A%2F%2Fartspill-876968932494.herokuapp.com%2F)

 - Add new Post

![Addpost](https://validator.w3.org/nu/?doc=https%3A%2F%2Fartspill-876968932494.herokuapp.com%2Fadd)

 - View post

![Detail](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fartspill-876968932494.herokuapp.com%2Ffin%2F)

-profile page

Although the validator could not check the user's credentials, I copied the page source and it ran through with 0 errors.
</details>


### Accessibility

## [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/)
![Lighthouse](https://res.cloudinary.com/dzgmi2kgu/image/upload/v1691355086/2023-08-06_21_51_02-Lighthouse_Report_Viewer_Mozilla_Firefox_dgzci0.png)




## Manual testing

| Action           | Expected Result                                                                                                                                | Pass |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------|------|
| Account creation | I can create a new account with username and password and be notified that it's created successfully, or if not                               | Pass |
| Sign in          | I can sign in with my username and account and get notified that I've been successfully signed in                                              | Pass |
| Sign out         | When signed in, I can sign out of the webpage, be asked if I'm sure I want to sign out and be notified that I've been successfully signed out | Pass |
| Navbar           | Each link in the navbar takes me to the correct corresponding page. There are different paged depending on if I am signed in or not.           | Pass |
| Create post      | When signed in, I can create a post, a creative text of my choice, and submit it. I'll be notified that it's successfully submitted.     | Pass |
| Edit post        | When signed in, I can edit my own posts | Pass |
| Delete post      | When signed in, I can delete my own posts, be asked if I'm sure I want to delete them    | Pass |
| Comment on post  | When signed in, I can leave feedback on others' posts. My comment is then visible beneath the post.                                            | Pass |
| Like/unlike post | When signed in, I can like and unlike others' posts. The icon changes                                                                          | Pass |
| Pagination       | I can browse through multiple pages on the home page if there are more than six posts                                                          | Pass |
| Links            | All of the links throughout the page are fully functional                                                                                      | Pass |
| Buttons          | All of the buttons direct me to their designated function                                                                                      | Pass |
| Footer           | I can reach the different social media sites via the footer, and they all open in new tabs.                                                   | Pass |


## Responsiveness

The deployed app has been tested across these web browsers with full responsiveness:
- Firefox
- Google Chrome
- Brave

It has also been tested on android mobile in physical form, and various viewports with the help of developer tools in the browser.





# Bugs
1. Although not necessarily a bug, I found that the user could edit both the comments and posts of another user by entering their corresponding numbers in the address bar, I then edited their corresponding views to disallow the user to change these pages.

2. Static files not loading on Heroku.
Solution: I forgot that when collect static was disabled on heroku, it would not display the css correctly, simply setting this to 0 solved the problem.


# Future implements

-  Perhaps a messaging system between users could be a nice addition, also I would like to alter the profile view so a user can see other users post, favourites and comments.

# Deployment

Github

Steps I took to deploy my website;



1. Go to the repository for Artspill
2. Click the Settings tab and locate the Pages tab
3. Select to deploy from the main branch
4. A few minutes later, upon refreshing the page, my site was live

To Fork this repository, then do as follows;

1. Log in to GitHub and find your way to the GitHub repository you want, in this case, my Artspill project
2. Up in the right corner of the repository page, on the row of buttons just beneath the user icon, you'll find the "Fork" button.
3. Click the "Fork" button, and you will now have created a copy of the repository to your GitHub account.

To clone this repository, then do as follows;

1. Log in to GitHub and find your way to the GitHub repository you want, and click the "<> Code" button in the upper right above the files
2. Copy the link
3. Open Gitpod and select which directory you want the clone to be created into.
4. Type in "git clone" in your Gitpod terminal and paste the link copied from GitHub and the close will be created.

Deploying the app in Heroku:

To properly deploy with Heroku, I've used [Code Institutes Django Blog Cheat Sheet](https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf), describing all steps for installing Django and supporting libraries.

The instructions below are for the basic Heroku app setup. For specific Django settings and instructions, please refer to the Cheat Sheet.

1. Log in to Heroku or create a new account by following the instructions on the page
2. On the main page near the top, click "New" and select "Create new app."
3. Pick your unique app name and select your region
4. Click the "Create App" button
5. On the next page, move to the "Settings" tab and find "Config Vars."
6. Click "Reveal Config Vars" and add relevant config vars and their keys, then click "Add."
7. Scroll back up and click the "Deploy" tab
8. Here, you select "GitHub" as the deployment method and search for your repository to link them together
9. Scroll down the page and select if you want to "Enable Automatic Deploys" to deploy your pushes from GitHub to Heroku automatically.

# Technologies Used

## Languages
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Javascript](https://en.wikipedia.org/wiki/JavaScript)

## Frameworks
- [Django](https://www.djangoproject.com/) - The main Python framework used to develop this project.
- [Bootstrap](https://getbootstrap.com/) - For general layouts and responsiveness across the site.
- [ElephantSQL](https://www.elephantsql.com/) - The production database used for the project.
- [GitHub](https://github.com/) - Used to host the source code.
- [Heroku](https://www.heroku.com) - Used for app deployment.
- [Cloudinary](https://console.cloudinary.com) - Stores all static files and images.

## Tools
- [W3C HTML Validator](https://validator.w3.org/) - For validating HTML code.
- [Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/) - For validating CSS code.
- [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/) - Developer tool used throughout the project for bug fixing and error searching.
- [Lighthouse](https://developer.chrome.com/docs/lighthouse/) - For accessability validation.

## Libraries
- Gunicorn - The server used for running Django on Heroku.
- pyscopg2 - Used to connect to PostgreSQL.
- Cloudinary - Used to host static files and images.


## Packages

- Django - An MVP, model-template-view, Python-based web framework for building projects.
- django-allauth - Used for account registration, managing signing in and out, and authentication.
- cloudinary_storage - Storage backend for Cloudinary that is used for static storage.
- django_summernote - Integrates Summernote WYSIWYG editor into Django projects. This package was installed but ended up not being used in the project.
- crispy_forms - Makes styling Django forms easier.

# Resourses



- [Google Fonts](https://fonts.google.com) - For browsing and implementing fonts.


## Images
- All images were created by me using stable diffusion



# Credits

- I used the code institute's template "I think therefore I blog" was used as a starting point for the site.

- My code institute tutor Spencer was most helpful in guiding me through the project

- I used Aurora Storm's excellent readme as a template for my own readme file [readme.md](https://raw.githubusercontent.com/AuroraStorm-sw/Inspired-Ink/main/README.md) 

- My friend Emilio who helped test and validate the website
