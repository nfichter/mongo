from pymongo import MongoClient

def compute_averages():
    c = MongoClient("lisa.stuy.edu")
    db = c["ada"]

    for doc in db.students.find():
        studentId = doc["id"]
        avgSum = 0
        avgNum = 0
        courseL = doc["courses"]
        for course in courseL:
            avgSum+=int(course["mark"])
            avgNum+=1
        avg = (avgSum*1.0) / avgNum

        db.students.update_one(
            {"id": studentId},
            {
                "$set": {"average": avg}
            }
        )

def print_averages():
    c = MongoClient("lisa.stuy.edu")
    db = c["ada"]

    max_name_len = 0

    s = ""
    
    for doc in db.students.find():
        if len(doc["name"]) > max_name_len:
            max_name_len = len(doc["name"])

    for doc in db.students.find():
        avg = "%.1f"%(doc["average"])
        if len(avg) == 4:
            s+=doc["name"]+" "*(max_name_len-len(doc["name"]))+" | "+avg+"    | "+str(doc["id"])+"\n"
        if len(avg) == 5:
            s+=doc["name"]+" "*(max_name_len-len(doc["name"]))+" | "+avg+"   | "+str(doc["id"])+"\n"
        if len(avg) == 3:
            s+=doc["name"]+" "*(max_name_len-len(doc["name"]))+" | "+avg+"     | "+str(doc["id"])+"\n"

    ret  = "Name"+" "*(max_name_len-3)+"| "+"Average | ID\n"
    ret += "----"+"-"*(max_name_len-3)+"--"+"--------------\n"

    ret += s
    
    print ret

compute_averages()
print_averages()
