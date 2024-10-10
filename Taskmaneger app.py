while True:
        print("\nWelcome, Choose how you wanna start")
        print("1. Enter new Task")
        print("2. Pop a Task")
        print("3. Clear All Tasks")
        print("4. Exit")

        Task_List=[]
        try:
           a = int(input('Enter your choice: '))
        except ValueError:#this the first time i used this logic
            print("Please enter a valid number.")
            continue
        
        if a == 1:
            task = input("ENTER YOUR TASK: ")
            Task_List.append(task)
            print(f"Task added: {task}")
            print("Current Tasks:", Task_List)

        elif a == 2:
            if Task_List:
                print("Current Tasks:", Task_List)
                try:
                    index = int(input('Enter index of the task you would like to delete (starting from 0): '))
                    if 0 <= index < len(Task_List):
                        removed_task = Task_List.pop(index)
                        print(f"Task removed: {removed_task}")
                    else:
                        print("Invalid index. Please try again.")
                except ValueError:
                    print("Please enter a valid index.")
            else:
                print("No tasks to pop.")

        elif a == 3:
            Task_List.clear()
            print('All tasks cleared.')

        elif a == 4:
            print('Goodbye!')
            break
        
        else:
            print('Invalid choice. Please try again.')