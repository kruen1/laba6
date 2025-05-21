from datetime import  datetime

class Task():
    def __init__(self, DateStart, DateFinish, Description):
        self.DateStart = DateStart
        self.DateFinish = DateFinish
        self.Description = Description

tasks = [
    Task("08:30", "09:30", "1C"),
    Task("09:40", "10:40", "RKIS"),
    Task("10:50", "11:50", "History"),
]

