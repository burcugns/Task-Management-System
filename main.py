import json


def add_task():
    tasks = read_tasks()

    add_new_task_to_list(tasks)

    save_task(tasks)


def list_tasks():
    newlist = sorted(read_tasks(), key=lambda d: d['completed'])
    i = 1
    for task in newlist:
        if task['completed'] == False:
            print(str(i) + '. []' + task['title'] + '  ' + str(task['id']))
        else:
            print(str(i) + '. [X]' + task['title'] + '  ' + str(task['id']))

        print('   Description: ' + task['description'])
        i = i + 1


def complete_task():
    tasks = read_tasks()

    id = int(input('If the task is completed, please enter the id'))
    for task in tasks:
        if task['id'] == id:
            task['completed'] = True

    save_task(tasks)


def delete_task():
    tasks = read_tasks()

    remove_task_from_list(tasks)

    save_task(tasks)


def remove_task_from_list(tasks):
    delete = int(input('Enter the id to delete the task'))
    for task in tasks:
        if task['id'] == delete:
            confirm = input('Are you sure you want to delete? Y?N')
            if confirm == 'y' or confirm == 'Y':
                tasks.remove(task)
                print('Successful')


def add_new_task_to_list(tasks):
    title = input('What is your title ')
    description = input('Write description')
    completed_usr_eny = input('Is completed? Y/N')

    task_dict = {
        "id": find_largest_task_id(tasks) + 1,
        "title": title,
        "description": description,
        "completed": is_completed(completed_usr_eny)
    }
    tasks.append(task_dict)


def read_tasks():
    with open('task.json', 'r') as file:
        tasks = json.load(file)
    return tasks


def save_task(tasks):
    with open('task.json', "w") as file_write:
        file_write.write(json.dumps(tasks))


def find_largest_task_id(tasks):
    largest_id_task = tasks[0]
    for task in tasks:
        if largest_id_task['id'] < task['id']:
            largest_id_task = task
    return largest_id_task['id']


def is_completed(completed_usr_eny):
    if completed_usr_eny == 'y' or completed_usr_eny == 'Y':
        return True
    return False

print('Project structure is ready!')
def menu():

    a = input(
        '---- Task Management System ----\n 1. Add Task \n 2. List Tasks \n 3. Complete Task \n 4. Delete Task \n 5. Exit')
    if a == '1':
        add_task()
    elif a == '2':
        list_tasks()
    elif a == '3':
        complete_task()
    elif a == '4':
        delete_task()
    elif a == '5':
        print('Goodbye!')
    else:
        print('please make a correct choice ')
        return menu()
menu()

