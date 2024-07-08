import os

# Specify the directory you want to explore
lesson_dir = 'LESSON_16_OOP'

# Join the current directory path with the lesson directory
lesson_path = os.path.join('.', lesson_dir)

# Check if the specified directory exists
if os.path.exists(lesson_path) and os.path.isdir(lesson_path):
    # List all files and directories inside the lesson directory
    lesson_contents = os.listdir(lesson_path)

    # Print the list of contents
    print(lesson_contents)
else:
    print(f"The directory '{lesson_dir}' does not exist or is not a directory.")
