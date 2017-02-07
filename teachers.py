from pymongo import MongoClient

def add_teachers():
    c = MongoClient("lisa.stuy.edu")
    db = c["ada"]

    f = open("teachers.csv","r")

    teachers = f.read().split("\n")
    teachersL = []
    for line in teachers:
        if len(line) > 1:
            lineL = line.split(",")
            if not lineL[0] == "code":
                dct = {"code":lineL[0],"teacher":lineL[1],"period":lineL[2],"student_ids":[]}
                teachersL.append(dct)

    db.teachers.insert_many(teachersL)

    for line in teachers:
        ids = []
        if len(line) > 1:
            lineL = line.split(",")
            for doc in db.students.find():
                for course in doc["courses"]:
                    if course["code"] == lineL[0]:
                        ids.append(doc["id"])

        db.teachers.update_one(
            { "teacher": lineL[1] },
            {
                "$set" : { "student_ids": ids }
            }
        )

    f.close()

add_teachers()
