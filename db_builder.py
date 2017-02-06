from pymongo import MongoClient


def build():
    c = MongoClient("lisa.stuy.edu")
    db = c["ada"]
    
    f1 = open("courses.csv","r")
    f2 = open("peeps.csv","r")

    courses = f1.read().split("\n")
    peeps = f2.read().split("\n")

    students = []
    for line in peeps:
        if len(line) > 1:
            lineL = line.split(",")
            if not lineL[0] == "name":
                dct = {"name":lineL[0],"age":lineL[1],"id":lineL[2],"courses":[]}
                students.append(dct)
    
    db.students.insert_many(students)

    for line in courses:
        if len(line) > 1:
            lineL = line.split(",")
            if not lineL[0] == "code":
                for doc in db.students.find({"id":lineL[2]}):
                    courseL = doc["courses"]
                    courseL.append({"code":lineL[0],"mark":lineL[1]})
                    db.students.update_one(
                        { "id": lineL[2] },
                        {
                            "$set" : { "courses": courseL},
                        }
                    )
                
    f1.close()
    f2.close()

build()
        
