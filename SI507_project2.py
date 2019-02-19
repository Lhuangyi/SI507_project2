# A Flask Application
import csv
import random
from flask import Flask, render_template
from movies_tools import *

#set up application
app = Flask(__name__)

#routes
@app.route('/')
def homepage():
    num = len(data) - 1
    return '<h1>{} movies recorded.</h1>'.format(num)


@app.route('/movies/ratings')
def movies_ratings():
    string = " "
    m = Movie(data = data, row = 33)
    for i in range(6):
        r = random.randint(2,len(data)-1)
        string = string + m.__str__(data = data, row = r) + ' <br> '
    return render_template('ratings.html',string = string)



if __name__ == '__main__':
    with open("movies_clean.csv","r") as f:
        reader = csv.reader(f)
        data = []
        for i in reader:
            data.append(i)
    app.run()
