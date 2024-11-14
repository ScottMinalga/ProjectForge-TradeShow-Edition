# ProjectForge

**ProjectForge** is a Python script designed to streamline the process of creating standardized folder structures for tradeshow or testing projects. With this tool, users can quickly generate project directories with predefined subfolders, ensuring consistency and organization across all tradeshow projects.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Future Improvements](#future-improvements)

---

### Features
- Automatically generates a standardized project folder structure.
- Allows users to input project numbers to create specific directories.
- Checks if a project directory already exists to avoid duplicate folders.
- Provides real-time feedback on folder creation.
- Easy-to-read and adaptable code, making it simple to customize or expand as needed.

---

### Requirements
- **Python**: This script is compatible with Python 3.x.
- **Operating System**: This script is designed to run on systems with access to shared network drives, but it can be adapted for local use.

---

### Installation
1. **Clone the Repository**: Clone this repository to your local system.
    ```bash
    git clone https://github.com/yourusername/ProjectForge.git
    ```
2. **Navigate to the Directory**: Go to the folder where the script is located.
    ```bash
    cd ProjectForge
    ```

3. **Set Up the Base Directory**: Ensure that the base directory (`M:\Tech Center\TECH CENTER PROJECTS Trade Show and Testing`) exists and is accessible from your machine. Adjust the `base_dir` variable in the script if necessary (See [Configuration](#configuration)).

---

### Usage
1. **Run the Script**:
    ```bash
    python create_tradeshow_project.py
    ```

2. **Enter Project Number**: When prompted, enter the project number for which you'd like to create a directory. If you want to exit the program, type `exit`.

3. **Folder Structure**: The script will automatically create a directory for the project and populate it with the predefined subdirectories. You’ll see confirmation messages in the terminal for each folder created.

4. **Checking for Existing Directories**: If a folder for the specified project already exists, the script will notify you and skip creating that directory again.

---

### Folder Structure
Each project folder will be created with the following structure:

```
Project Number/
├── 1 PROJECT REQUIREMENTS
├── 2 CONCEPT INFO
├── 3 QUOTES
├── 4 PO IN
├── 5 TASKS SCHEDULE
├── 6 DETAIL DESIGN
├── 7 ORDER PARTS
├── 8 KIT ASSEMBLE TEST
├── 9 SHIP
├── 10 EMAIL GEN INFO
└── 11 MANUAL
```

---

### Configuration
1. **Base Directory**: Update the `base_dir` variable in the `create_tradeshow_project()` function to specify where project folders should be created.
   ```python
   base_dir = r"M:\Tech Center\TECH CENTER PROJECTS Trade Show and Testing"
   ```
2. **Adding/Removing Subdirectories**: Modify the `subdirs` list in the script to change the default subfolder structure. For example:
   ```python
   subdirs = [
       "1 PROJECT REQUIREMENTS",
       "2 CONCEPT INFO",
       # Add or remove subdirectories as needed
   ]
   ```

---

### Troubleshooting
- **Directory Not Found**: Ensure that the `base_dir` exists and is accessible from your system. Network permissions might be required if you are connecting to a shared drive.
- **Permission Denied**: Run the script with appropriate permissions to create folders in the specified directory.
- **Path Not Found on GitHub**: Remember to remove or replace sensitive information in `base_dir` if you are pushing this code to a public repository.

---

### Future Improvements
Here are some possible enhancements for future releases:
- **GUI Support**: Implement a graphical user interface (GUI) for a more user-friendly experience.
- **Folder Naming Customization**: Allow users to specify folder names for each project.
- **Template-Based Structure**: Allow different folder templates for different types of projects.
- **Logging**: Save logs of created folders to a specified log file location.
- **Error Handling**: Improve error handling to catch and log unexpected issues.

---

### License
This project is open-source and free to use under the MIT License.

--- 

