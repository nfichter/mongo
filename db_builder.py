from pymongo import MongoClient

def build():
    c = MongoClient("lisa.stuy.edu")
    db = c[""]
    
    f1 = open("courses.csv","r")
    f2 = open("peeps.csv","r")

    courses = f1.readline()
    peeps = f2.readline()

    students = []
    for line in peeps:
        lineL = line.split(",")
        dct = {"name":lineL[0],"age":lineL[1],"id":lineL[2],"courses":[]}
    db.students.insert_many(students)

    for line in courses:
        lineL = line.split(",")
        
