To_do_list = []
task = []
def Add_a_task(To_do_list):
    task = input("what task are you adding?:")
    To_do_list.append(f"{task} was added!!")
    print(To_do_list)

def Delete_task(To_do_list):
    task = input("what task are you deleting?:")
    if task in To_do_list:
        To_do_list.remove(f"{task} was removed!")
    else:
        print(f"{task} is not list in To do list!!!")

def main(To_do_list):
     print("""
    Welcome User, Here are your options!!!:
           1. Menu:
           2. Add a task:
           3. View Task:
           4. Mark a task as Complete:
           5. Delete a Task:
           6. Quit!
           """)
     while True:
        option = input("Please select an option")
        if option == "1":
            print("""
    Welcome User, Here are your options!!!:
           1. Menu:
           2. Add a task:
           3. View Task:
           4. Mark a task as Complete:
           5. Delete a Task:
           6. Quit!
           """)
        elif option == "2":
            Add_a_task(To_do_list)
        elif option == "3":
            print(To_do_list)
        elif option == "4":
            print(f"input{task}"+" x" + "Completed ")
        elif option == "5":
            Delete_task(To_do_list)
        elif option == "6":
            print("List is saved; remember there's always something to do!!!")
            break
        else:
            print("Select a valid option!: 1, 2, 3, 4, 5, or 6")
          


main(To_do_list)

    