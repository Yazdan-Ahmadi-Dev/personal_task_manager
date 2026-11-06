from tasks import show_tasks, save_tasks, load_tasks
from dotenv import load_dotenv
import os


load_dotenv()



name = input("Ente your name: ")
print("Welcome", name)


admin_mode = input("Do you want to enter admon mode (yes/no)?  ")

if admin_mode == "yes":
    admin_password = input("Enter admin password:  ")
    if admin_password == os.getenv("admin_pass"):
        print("Admin mode is activated")
    else:
        print("Wrong password")


tasks = load_tasks()
count = int(input("How many tasks do you want to add? "))
for i in range(count):
    task = input ("Enter a task: ")
    tasks.append(task)

show_tasks(tasks)
save_tasks(tasks)
load_tasks()