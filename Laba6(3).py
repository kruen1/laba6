class Task:
    def __init__(self, DateStart, DateFinish, Description):
        self.DateStart = DateStart
        self.DateFinish = DateFinish
        self.Description = Description

    def __str__(self):
        return f"Описание: {self.Description}\nНачало: {self.DateStart}\nОкончание: {self.DateFinish}\n"

tasks = [
    Task("2023-05-01 10:00", "2023-05-01 12:00", "Лекция по математике"),
    Task("2023-05-02 14:00", "2023-05-02 18:00", "Практика по программированию"),
    Task("2023-05-03 09:00", "2023-05-03 17:00", "Семинар по искусственному интеллекту"),
    Task("2023-05-04 11:00", "2023-05-04 19:00", "Воркшоп по веб-разработке"),
    Task("2023-05-05 13:00", "2023-05-05 19:00", "Консультация по дипломному проекту")
]

for task in tasks[1:]:
    if task.DateFinish > latest_task.DateFinish:
        latest_task = task

print(f"Занятие, которое заканчивается позже всех:")
print(latest_task)