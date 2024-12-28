import traceback
tasks_list=[]
def add_task():
    task=input("add ypur task  :  ")
    tasks_list.append(task)
def save_to_file():
    try:
        with open("task_list.txt","w") as file :
            for i in tasks_list:
                file.write(i+"\n")
            file.close()
    except Exception:
            exception_handling(Exception)

def del_task():
    try:
        task_line=int(input("please enter the number of task you want to delete:  "))
        tasks_list.pop(task_line-1)
    except Exception:
            exception_handling(Exception)
def load_from_the_file():
    print("if you did not save your list to the text file before load it you will lose them.")
    try:
        with open("task_list.txt","r") as file :
            lists_string=file.read()
            tasks_list.clear()
            tasks_list.extend(lists_string.split("\n"))
            tasks_list.pop(-1)
            file.close()
    except Exception:
            exception_handling(Exception)
    
def display_list():
    try:
        for i in tasks_list:
            print(i)
    except Exception :
            exception_handling(Exception)    

def exception_handling(ex):
    if isinstance(ex,FileNotFoundError):
        print("please make sure you have a file to save")
        main_program()
    elif isinstance(ex,PermissionError):
        print("please make sure you have a permission to open and write in this file")
        main_program()
    elif isinstance(ex,IndexError):
        print("please make sure you choised a correct line index")
        main_program()
    elif isinstance(ex,ValueError):
        print("please make sure you enter a integar number as a choice")
        mainprogram()
    else:
        pass

def main_program():
    try:
        while True:
            print("please enter the option:\n1-enter task\n2-delete task")
            print("3-load from the text file\n4-save to the text file\n5- print the currtn list")
            print("6-terminate the program")
            user_in=int(input("your choise:  "))
            match user_in:
                case 1: add_task()
                case 2: del_task() 
                case 3: load_from_the_file()
                case 4: save_to_file()
                case 5: display_list()
                case 6: break
                case _: print("please enter a valid choise")
    except Exception:
            exception_handling(Exception)

main_program()