# This file should do database queries for end user that doesn't have db browser
# For ex:  Show all classes with "ECS-1xx" and professor "null" on "Tu"
# Kind of like a universal query


import sqlite3
import utilities as util

conn = sqlite3.connect('current_semester.db')
# cursor = conn.cursor()

def get_all_classrooms():
    all_classrooms = []
    cursor = conn.execute("SELECT Section ID, Class, Day, Time, Room, Professor from Classes")
    for row in cursor:
        classroom = row[4]
        if classroom not in all_classrooms:
            all_classrooms.append(classroom)
    all_classrooms.sort()
    return all_classrooms


def get_times(classroom):
    all_times = []
    cursor = conn.execute("SELECT Section ID, Class, Day, Time, Room, Professor from Classes")
    for row in cursor:
        if row[4] == classroom.upper():
            day = row[2]
            time = row[3]
            all_times.append(day + " " + time)
    return all_times


allClasses = get_all_classrooms()

allInfo = {}
for x in allClasses:
    allInfo[x] = get_times(x)



import json

with open('data.json', 'w') as outfile:
    json.dump(allInfo, outfile)



conn.close()