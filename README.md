# SI507_project2
### Introduce: 
   In my project, I have done the following things:
    - Use the data in movies_clean.csv
    - Write code to integrate some data with a Flask application
    - Create a diagram to display the ways to organize a database
    
## Part one: Code and a Flask app
   In part one, I created two files: movies_tools.py and SI507_project2.py.
### 1. movies_tools.py
    - In movies_tools.py file, I defined a class Movie.
    - Class Movie has two method: __init__( ) and __str__( )
        - __init__( ): make class Movies accept as constructor input one row of the movies_clean.csv file 
        - __str__( ): useful for building the Flask app. This method returns the following information: Movie Title | IMBD rating
  
### 2. SI507_project2.py
    In SI507_project2.py, I build a simple Flask app which has two routes:
      - / (home page) : Displays in <h1> html tag: <number> movies recorded. 
        ![Image text]
        (https://github.com/Lhuangyi/SI507_project2/blob/master/images/homepage.png)
      - /movies/ratings/ :Through creating an instance variable m of class Movies and using the method __str__( ), display a lsit of six random movies and the corresponding ratings with the following format: Movie Title | IMBD rating
        ![Image text]
        (https://github.com/Lhuangyi/SI507_project2/blob/master/images/movies_ratings_page.png)
      
      

## Part two: Database Diagram
   In part two, I created a database diagram which indicated a way to organize a database.
## How to run the flask app?
    - First we need to run the terminal in mac.
    - Second we need to type "mkdir SI507_poject2" and then type "cd SI507_poject2", and then type "virtualenv lSI507_poject2" to set up virtual environment, and then type "cd SI507_poject2", and then type "source bin/activate" to activate the virtual environment, and then type "pip install flask" to install web framework, and last we need to type "python SI507_project2.py runserver" to run the server.
    - Last, we can type specified urls(showed above) to reach the websites we want.
   
## Dependencies
    Click==7.0
    Flask==1.0.2
    itsdangerous==1.1.0
    Jinja2==2.10
    MarkupSafe==1.1.0
    numpy==1.16.1
    pandas==0.24.1
    python-dateutil==2.8.0
    pytz==2018.9
    six==1.12.0
    Werkzeug==0.14.1
