class TodoList:
    def __init__(self):                  # This block of code defines the class named TodoList which is the list of tasks, that is set to empty with the init method.
        self.tasks = []                  # The list is set to empty, as this is where the tasks entered will be stored. 

    def add_task(self, title, priority):
        task = Task(title, priority)                                    # First function/option which adds tasks with title and priority. It recieves the information that it needs and adds the new task to the end of the list with append. 
        self.tasks.append(task)                     
        print(f"Task '{title}' with priority '{priority}' added.")      # F string allowing me to add each of the values to the statement seperately. 

    def remove_task(self, task_number):
        if task_number >= 1 and task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)              # Next option to remove tasks that are already in the list. It takes the list if it's 1 or more, and adjusts the count of how many tasks were removed, returning a confirmation to user.
            print(f"Task '{removed_task.title}' removed.")              # F string allows me to combine the task chosen and statment in a much easier way with the curly brackets.
        else:
            print("Invalid task number.")

    def show_tasks(self):
        if self.tasks:                                                      # Next option to show the user all of the tasks added to the list, in order, with all information included. Enumerate allowing me to get both the number and value of each item in the list. 
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):              # With the tasks init list, they are showen in order with task and priority, and shown that there are no tasks if there are none. 
                print(f"{index}. {task.title} (Priority: {task.priority})")
        else:
            print("No tasks.")

class Task:
    def __init__(self, title, priority):                # Defines a task class which is a singular task given. Recognizing the task with its title and priority. 
        self.title = title                              # Using the init function in order to use these classes from each entry with title and priority. 
        self.priority = priority

def main():
    todo_list = TodoList()          # This is where the main program runs, displaying the menu of options, add, remove, show, or delete tasks. 

    while True:
        print("\nTO-DO List Options:")
        print("1. Add Task")
        print("2. Remove Task")         # From the users input, they will be displayed these options to choose from for what they want to do in the to-do list. 
        print("3. Show Tasks")          # Each being shown at the same time, giving all options together and being printed first in main as it will be the first screen the user will go to. 
        print("4. Exit")

        choice = input("Enter your choice: ")          # Asking for an option choice from the user, and saving that as choice.  

        if choice == '1':
            task = input("Enter task to add: ")
            priority = input("Enter task priority (WORK/PERSONAL/IMPORTANT): ")
            todo_list.add_task(task, priority)                                  # This allows the user to choose any of the options by responding with the number that applies to that certain option.
        elif choice == '2':                                                     # Runs through each option with the if statement, for what's chosen will be executed.
            task_number = int(input("Enter task number to remove: "))
            todo_list.remove_task(task_number)
        elif choice == '3':
            todo_list.show_tasks()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()                          # This ensures that the program will only execute when it is directly ran.