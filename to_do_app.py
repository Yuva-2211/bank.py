class to_do_app:
    def __init__(self):
        self.Task_list = []

    def enter_task(self):
        while True:
            task = input("enter your task (type done to confirm):").strip()

            if task.lower() == "done":
                break
            elif task not in self.Task_list:  
                self.Task_list.append(task)
                print(f"{task} added to your task list.")
            else:
                print(f"{task} is already in your task list.")


    def view_task(self):
        if not self.Task_list:
            print("\nYour Task List is empty.")
        else:
            print(f"\nYour current Task {self.Task_list}")

    def delete_task(self):
        if not self.Task_list:
            print("\nYour Task List is empty.")
            return
        self.view_task()
        task_to_remove = input("Enter the name of the task to remove: ").strip()
        if task_to_remove in self.Task_list:
            self.Task_list.remove(task_to_remove)
            print(f"{task_to_remove} has been marked completed.")
        else:
            print(f"{task_to_remove} is not in your order.")

    def run(self):
            while True:
                print("\nWelcome to the App!!")
                print("1.View Task \n2.Add Task \n3.Delete task \n4.Exit")
                choice = input("Choose an option: ").strip()

                if choice == "1":
                    self.view_task()
                elif choice == "2":
                    self.enter_task()
                elif choice == "3":
                    self.delete_task()
                elif choice == "4":
                    self.delete_task()

                    break
                
                else:
                    print("Invalid choice, Please try again.")
            
if __name__ == "__main__":
    app = to_do_app()
    app.run()