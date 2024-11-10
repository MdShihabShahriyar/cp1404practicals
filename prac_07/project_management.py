import datetime


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percent):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y")
        self.priority = priority
        self.cost_estimate = float(cost_estimate)
        self.completion_percent = completion_percent

    def __str__(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percent}%"


def load_projects():
    projects = [
        Project("Organise Pantry", "20/07/2022", 1, 25, 55),
        Project("Build Car Park", "12/09/2021", 2, 600000, 95),
        Project("Mow Lawn", "31/10/2022", 3, 3, 0),
        Project("Record Music Video", "01/12/2022", 9, 250000, 0),
        Project("Read 7 Habits Book", "13/12/2021", 6, 99, 100)
    ]
    return projects


def display_projects(projects):
    incomplete = [project for project in projects if project.completion_percent < 100]
    completed = [project for project in projects if project.completion_percent == 100]

    print("Incomplete projects: ")
    for project in incomplete:
        print(f"  {project}")

    print("Completed projects: ")
    for project in completed:
        print(f"  {project}")


def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = input("Cost estimate: ")
    completion_percent = int(input("Percent complete: "))

    new_project = Project(name, start_date, priority, cost_estimate, completion_percent)
    projects.append(new_project)


def filter_projects_by_date(projects):
    filter_date = input("Show projects that start after date (dd/mm/yy): ")
    filter_date = datetime.datetime.strptime(filter_date, "%d/%m/%Y")
    filtered_projects = [project for project in projects if project.start_date > filter_date]

    for project in filtered_projects:
        print(f"{project}")


def update_project(projects):
    print("Updating a project...")
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    project_choice = int(input("Project choice: "))
    new_percentage = int(input("New Percentage: "))
    new_priority = int(input("New Priority: "))

    project = projects[project_choice]
    project.completion_percent = new_percentage
    project.priority = new_priority
    print(f"Updated: {project}")


def main():
    projects = load_projects()

    while True:
        print("\n- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")

        choice = input(">>> ").lower()

        if choice == "l":
            projects = load_projects()
        elif choice == "s":
            # Save projects logic (not implemented here)
            print("Save projects functionality is not implemented.")
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        elif choice == "q":
            save_choice = input("Would you like to save to projects.txt? ")
            if save_choice.lower() == "yes":
                print("Saving projects...")
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
