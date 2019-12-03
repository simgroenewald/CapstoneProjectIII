# Compulsory Task 1

# Boolean Values for the user name and password
user_name_exist = False
password_match = False

# This loop will run until a correct user name and password combo is entered
while 1:

    # Allows the user to enter a user name and opens the user names file
    user_name = input("Enter your user name: ")
    user_names_file = open("users.txt", "r")

    # Checks if user name matches existing user names
    for line in user_names_file:
        get_user = line
        get_user = get_user.split()
        get_username = get_user[0]
        get_username = get_username.strip(",")

        # If the user name does match an existing user name the user will then be asked for a password
        if user_name == get_username:
            user_name_exist = True

            # This loop runs while the user name does exist and until the user name's password is entered
            while user_name_exist:
                password = input("Enter your password: ")
                get_password = get_user[1]

                # The loop breaks if the correct password is entered
                if password == get_password:
                    password_match = True
                    break

                print("The password you have entered is incorrect, please try again.")

    # If the user name does not exist the user will be prompted to enter the user name again.
    if not user_name_exist:
        print("The user name you have entered is incorrect, please try again.")

    # The main loop will onl break if both the user name and its correct password is entered
    if user_name_exist and password_match:
        break
user_names_file.close()

# This list will only appear only if the admin login is used
if user_name_exist and password_match:
    if user_name == "admin":
        print("Please select one of the following options: \n" +
              "r - register user\n" +
              "a - add task\n" +
              "va - view all tasks\n" +
              "vm - view my tasks\n" +
              "d - display statistics\n" +
              "e - exit")
        user_select = (input("Which option would you like to select: "))
    # This list will appear for all other users
    if user_name != "admin":
        print("Please select one of the following options: \n" +
          "a - add task\n" +
          "va - view all tasks\n" +
          "vm - view my tasks\n" +
          "e - exit")
        user_select = (input("Which option would you like to select: "))

# This code will only run if the admin user selects r
if user_select == "r":
    if user_name == "admin":
        print("You are about to create a new user.")
        new_user_name = input("Please enter your user name: ")

        # This loop will run until a password is entered twice and they are both the same
        while 1:
            new_password = input("Please enter a password: ")
            password_check = input("Please re-enter your password: ")
            if new_password == password_check:
                break
            print("The passwords did not match. Please try again.")

        # The new user's information is put into a string and written (amended) to the file
        new_user = new_user_name + ", " + new_password
        user_names_file = open("users.txt", "a")
        user_names_file.write("\n" + new_user)
        user_names_file.close()
    else: print("You do not have administrator privileges.")

# This code will run if the user selects a
if user_select == "a":
    # The user is prompted to enter all the relevant information
    print("You are about to add a task.")
    task_user = input("Please enter the user name of the person to whom you are assigning the task: ")
    task_title = input("Please enter the task title: ")
    task_description = input("Please describe the task in detail: ")
    # This automatically inputs the date
    from datetime import date
    assign_date = str(date.today())
    task_due = input("Please enter the due date of the task: ")
    # The default status is incomplete
    task_status = "Incomplete"

    # This puts all the information into one string form and then writes (amends) it to the file
    full_task = task_user + ", " + task_title + ", " + task_description + ", " + assign_date + ", " + task_due + ", "+ task_status
    tasks_file = open("tasks.txt", "a")
    tasks_file.write(full_task + "\n")
    tasks_file.close()

# If the user selects va then this code will run
if user_select == "va":
    tasks_file = open("tasks.txt", "r")

    # This code will run for every line in the text file
    for line in tasks_file:
        # Reads the line from the file into string form and then it gets split into a list
        task = ""
        task = task + line
        task = task.split(",")
        # Prints the relevant position next to its description so that it is user-friendly
        print("User: " + task[0])
        print("Task: " + task[1])
        print("Description: " + task[2])
        print("Date assigned: " + task[3])
        print("Due Date: " + task[4])
        print("Status: " + task[5])
    tasks_file.close()

# This code will run if the user selects vm
if user_select == "vm":
    tasks_file = open("tasks.txt", "r")
    # This code will run for every line in the text file
    for line in tasks_file:
        # Reads the line from the file into string form and then it gets split into a list
        task = ""
        task = task + line
        task = task.split(",")
        # This checks if the user in the task is the same as the current user
        line_user = task[0]
        # If it is the same then it will print the information in a user-friendly manner
        if line_user == user_name:
            print("User: " + task[0])
            print("Task: " + task[1])
            print("Description: " + task[2])
            print("Date assigned: " + task[3])
            print("Due Date: " + task[4])
            print("Status: " + task[5])
    tasks_file.close()

# This code will only run if the admin user selects d
if user_select == "d":
    if user_name == "admin":
        # This opens the users text file for reading
        user_names_file = open("users.txt","r")

        # This will run for every line in the file - so the code will run once for every user
        for line in user_names_file:
            # This gets the users name
            get_user_login = ""
            get_user_login = get_user_login + line
            get_user_login = get_user_login.split(",")
            user = get_user_login[0]

            # This opens the tasks text file
            tasks_file = open("tasks.txt","r")
            all_users_tasks = ""

            # This runs for every line in the tasks file. It checks if the user is the same as the user which the
            # task is assigned to and will then pull the relevant task information and all the tasks assigned to that
            # user.
            for line in tasks_file:
                task_info = ""
                task_info = task_info + line
                task_info = task_info.split(",")
                task_responsible = task_info[0]

                if user == task_responsible:
                    get_users_tasks = ""
                    get_users_tasks = get_users_tasks + task_info[1] + ": " + task_info[2] + "\n"
                    all_users_tasks = all_users_tasks + get_users_tasks
            print(user + ":\n" + all_users_tasks)

        tasks_file.close()
        user_names_file.close()



















