
def display():
    print("Team Management:")
    print("1) Register yourself")
    print("2) View your team")
    print("3) View your team member's position")
    print("4) Assign task to your team")
    print("5) View task")
    print("6) Exit")

def main():
    display()
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            import user_register
            user_register.register()
            break

        elif choice == 2:
            import view_team
            view_team.view_team()
            break

        elif choice == 3:
            import view_position
            view_position.view_pos()
            break

        elif choice == 4:
            import task_manage
            task_manage.tasks()
            break

        elif choice == 5:
            import view_task
            view_task.view_task()
            break

        elif choice==6:
            break
        else:
            print("Invalid choice!")
            break
main()
