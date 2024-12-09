import os
import tkinter as tk
from tkinter import messagebox, filedialog

def create_project(base_dir, project_number):
    if not os.path.exists(base_dir):
        messagebox.showerror("Error", f"The base directory does not exist: {base_dir}")
        return

    project_dir = os.path.join(base_dir, project_number)

    if os.path.exists(project_dir):
        messagebox.showinfo("Info", f"The directory for project {project_number} already exists.")
        return

    try:
        os.mkdir(project_dir)
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
        for subdir in subdirs:
            os.mkdir(os.path.join(project_dir, subdir))

        messagebox.showinfo("Success", f"Created project {project_number} at {project_dir}")
    except OSError as e:
        messagebox.showerror("Error", f"Failed to create directories: {e}")

def browse_directory(entry_field):
    dir_path = filedialog.askdirectory()
    if dir_path:
        entry_field.delete(0, tk.END)
        entry_field.insert(0, dir_path)

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Tradeshow Project Creator")

    # Base Directory
    tk.Label(root, text="Base Directory:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
    base_dir_entry = tk.Entry(root, width=50)
    base_dir_entry.grid(row=0, column=1, padx=5, pady=5)
    tk.Button(root, text="Browse", command=lambda: browse_directory(base_dir_entry)).grid(row=0, column=2, padx=5, pady=5)

    # Project Number
    tk.Label(root, text="Project Number:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
    project_number_entry = tk.Entry(root, width=50)
    project_number_entry.grid(row=1, column=1, padx=5, pady=5)

    # Buttons
    tk.Button(root, text="Create Project", command=lambda: create_project(base_dir_entry.get(), project_number_entry.get())).grid(row=2, column=0, columnspan=2, pady=10)
    tk.Button(root, text="Exit", command=root.quit).grid(row=2, column=2, pady=10)

    # Run the main loop
    root.mainloop()

if __name__ == "__main__":
    main()
