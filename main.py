from database import *


def menu():
    print("|   1.Register   |\n"
          "|   2.Login      |\n"
          "|   3.Exit       |\n")


create_table()


def login_menu():
    print(f"""    
   |  1.Search user:       |
   |  2.Search all users:  | 
   |  3.Log out            |

""")


while True:
    menu()
    choice = int(input("Choose command, please : "))
    if (choice == 1):
        name = input("Name, please : ")
        surname = input("Surname command, please : ")
        username = input("Username command, please : ")
        password = input("Password command, please : ")
        user = search(username)
        if (user is None):
            insert(name, surname, username, password)
            print("Registered successfully!")
        else:
            print("username has already selected ")
    elif (choice == 2):
        username = input("Username command, please : ")
        password = input("Password command, please : ")
        user = search(username)
        if (user is not None):
            if (user[1] is not None and password == user[4]):
                print(f"""Name: {user[1]}  \nSurname: {user[2]}  \nUsername: {user[3]}\n""")
                while (True):
                    login_menu();
                    choice2 = int(input("Choose command, please: "))
                    if (choice2 == 1):
                        username2 = input("Username, please : ")
                        search2 = search(username2)
                        if (search2 is not None):
                            print(f""" Name:     {search2[1]}  \nSurname:  {search2[2]}  \nUsername: {search2[3]}\n""")

                    if (choice2 == 2):
                        print_all()
                    if (choice2 == 3):
                        break
            else:
                print("Wrong password")
                break
        else:
            print("Wrong username")
            break

    elif (choice == 3):
        break

    else:
        print("Wrong choice, again please.")



