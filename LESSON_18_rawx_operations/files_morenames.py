import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='file_operations.log', level=logging.INFO)

# Function to log when the file is opened
def open_file(filename):
    logging.info(f'File {filename} opened at {datetime.now()}')

# Function to log when the file is closed
def close_file(filename):
    logging.info(f'File {filename} closed at {datetime.now()}')

# Function to read and print the content of the file
def read_file(filename):
    #
    #
    #

    try:
        with open(filename, 'r') as f:
            open_file(filename)  # Log file open operation
             #
            #
            for line in f:
                print(line.strip())  # Print each line (strip to remove newline characters)
            print("----")
            #
            #
    except FileNotFoundError:
        logging.error(f'File {filename} not found at {datetime.now()}')

        print("The file you want to read doesn't exist")
    except Exception as e:
        logging.error(f'Error reading file {filename}: {str(e)} at {datetime.now()}')
        print(f"Error reading file: {str(e)}")
    finally:
        close_file(filename)  # Log file close operation
    #
    #
    #
    #
    #
    #
# Example usage
filename = "more_names.txt"
read_file(filename)
