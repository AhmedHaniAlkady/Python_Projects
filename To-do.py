message = """1- Add tasks to alist
2- Mark task as complete
3- View tasks
4- Quit"""


def addtask():
    task = input("Enter atask: ")
    task.capitalize()
    tasks.append({"task":task , "status":"[]" })


def mark_task_complete():
    lenght = len (tasks)
    get = int(int(input ("Which one ? "))-1)
    get = int(get)

    if tasks[get]["status"]=="[]":
        tasks[get]["status"]="[x]"

    elif tasks[get]["status"]=="[x]":
        tasks[get]["status"]=[]


def view_task():
    lenght = len (tasks)
    for i in range (lenght):
        print(tasks[i]["status"],tasks[i]["task"])


tasks = []
done = []

while True:
    choise = input("Enter your choise: ")
    try:
        if choise =="ls":
            print (message)

        elif choise == "1":
            addtask()
        elif choise == "2":
            mark_task_complete()
        elif choise == "3":
            view_task()
        elif choise == "4":
            break
        else:
            print ("invalid choise ")
    except:
        print ('invalid choise')

# Dict = {"AHmed":1 , "age":2}
# print (Dict["AHmed"]) 

