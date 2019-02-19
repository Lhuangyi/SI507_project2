import csv

class Movie:


    def __init__(self,data,row):
        self.data = data
        self.row = row
        row_list = data[row]


    def __str__(self,data,row):
        self.data = data
        self.row = row
        return "{} | {}".format(data[row][1],data[row][-2])


if __name__ == '__main__':
    with open("movies_clean.csv","r") as f:
        reader = csv.reader(f)
        data = []
        for i in reader:
            data.append(i)
