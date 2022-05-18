### Blog-Posts

## Author Kipkurui Evans

## Project description

Personal blog website where I can create and share my opinions and other users can read and comment on them. Additionally, has a feature that displays random quotes to inspire my users.

### Live Link 
https://bloggposts.herokuapp.com/   <br>


![Landing page photo](https://github.com/Langat20/Blog-Posts/blob/master/app/static/images/Screen.png)

## BDD
BDD focuses on how the user will interact with the application. What you will see and experience:

A landing page with a quote,background and a navigation bar.
The Navbar has three routes to view blogs based on category. Also includes a route to sign in to the application.

Click on the sign in, if user does not have an account, they can click on sign up.

On the sign up form, the user is required to enter an email,unique username and a password. Upon registration the user receives a welcome email and is redirected to the sign in page.

After the user signs in, they can navigate to their profile through the navbar and update their profile pic and bio. They can add a new blog post as well. They also have an option to delete and edit a blog post.

On the blog display pages, a user can view other blogs.Click on the view more to get redirected to a particular blog with comments from other users displayed, ability to upvote,downvote and comment. If a user is an an author of a particular blog, they can delete undesired comments.

Click on the new comment and add a comment as well.

Click on signout to logout of the application.


### Set-up instructions

- Install Python3 installed in your machine together with venv and pip.
- Set up the virtual environment and activate it

$ python3.8 -m venv virtual
$ source virtual/bin/activate

$ git clone https://github.com/Langat20/Blog-Posts.git
- Navigate into the cloned project.

- Install all the necessary modules using requiments.txt 
pip install -r requirements.txt

Create a start.sh file
- $ touch start.sh

On your start.sh file , add the command for executing manage.py (python3.8 manage.py server), which will start the server.


Give the file execution permissions.
- $ chmod a+x start.sh

command to run your application
- $ ./start.sh

## Technologies Used

- Python (Flask)
- Jinja2
- HTML
- CSS
- Bootstrap

## LICENSE
Copyright  evans 2022 .

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.