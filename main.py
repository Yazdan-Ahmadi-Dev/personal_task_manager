from tasks import show_tasks



name = input("Ente your name: ")
print("Welcome", name)
tasks = []
count = int(input("How many tasks do you want to add? "))
for i in range(count):
    task = input ("Enter a task: ")
    tasks.append(task)

show_tasks(tasks)