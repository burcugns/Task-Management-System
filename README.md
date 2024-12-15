Overview

The Task Management System is a Python-based application that allows users to manage tasks efficiently. Users can add, view, complete, and delete tasks through an interactive menu interface. Tasks are stored in a JSON file (task.json) to ensure data persistence.

Features

Add Task:

Users can create a new task by providing a title, description, and completion status.

Each task is assigned a unique ID.

List Tasks:

Displays all tasks, sorted by their completion status (incomplete tasks first).

Tasks are shown in a numbered list, with their title, description, and ID.

Complete Task:

Allows the user to mark a task as completed by entering its ID.

Delete Task:

Users can delete a task by entering its ID.

A confirmation prompt ensures accidental deletions are avoided.

Persistent Storage:

All tasks are saved in a JSON file (task.json). Changes made during runtime are reflected in the file.

Interactive Menu:

Provides a simple text-based interface for navigating through the system.

Usage

Run the script by executing python task_manager.py.

Follow the interactive menu options:

Enter 1 to add a task.

Enter 2 to view all tasks.

Enter 3 to mark a task as completed.

Enter 4 to delete a task.

Enter 5 to exit the application.

Example Workflow

Add a new task:

Enter 1.

Provide the title, description, and completion status.

View tasks:

Enter 2.

See all tasks with their details.

Complete a task:

Enter 3.

Input the task ID to mark it as completed.

Delete a task:

Enter 4.

Confirm deletion by entering Y when prompted.

Functions Overview

Core Functions

add_task(): Adds a new task to the list.

list_tasks(): Lists all tasks in sorted order.

complete_task(): Marks a task as completed based on its ID.

delete_task(): Deletes a task after user confirmation.

Helper Functions

read_tasks(): Reads tasks from the task.json file.

save_task(): Saves tasks back to the task.json file.

find_largest_task_id(): Finds the largest task ID to ensure unique IDs.

is_completed(): Converts user input (Y/N) into a boolean value for the completed field.
