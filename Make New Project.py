import os


def create_tradeshow_project():
    # Set the base directory to the specified shared directory on the server
    base_dir = r"YOUR_DIRECTORY_PATH_HERE"

    # Ensure the base directory exists
    if not os.path.exists(base_dir):
        print(f"Error: The specified base directory does not exist: {base_dir}")
        return

    while True:
        # Ask the user for the project number
        project_number = input("Enter the project number (or type 'exit' to quit): ").strip()

        if project_number.lower() == 'exit':
            print("Exiting the program.")
            break

        # Define the project directory path within the specified base directory
        project_dir = os.path.join(base_dir, project_number)

        # Check if the project directory already exists
        if os.path.exists(project_dir):
            print(f"The directory for project {project_number} already exists.")
        else:
            # Create the project directory
            os.mkdir(project_dir)
            print(f"Created directory for project {project_number} at {project_dir}")

            # Define the list of subdirectories based on your structure
            subdirs = [
                "1 PROJECT REQUIREMENTS",
                "2 CONCEPT INFO",
                "3 QUOTES",
                "4 PO IN",
                "5 TASKS SCHEDULE",
                "6 DETAIL DESIGN",
                "7 ORDER PARTS",
                "8 KIT ASSEMBLE TEST",
                "9 SHIP",
                "10 EMAIL GEN INFO",
                "11 MANUAL"
            ]

            # Create each subdirectory within the project directory
            for subdir in subdirs:
                subdir_path = os.path.join(project_dir, subdir)
                os.mkdir(subdir_path)
                print(f"Created subdirectory: {subdir}")


# Run the main program in a loop
create_tradeshow_project()
