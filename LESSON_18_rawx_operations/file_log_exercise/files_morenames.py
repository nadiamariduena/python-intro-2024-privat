import logging
import json
#
# time stamp
from datetime import datetime
# to indent the data and make it cleaner
from pprint import pprint

# Configure logging
# the logs will be generated in this file "file_operations.log"
logging.basicConfig(filename='file_operations.log', level=logging.INFO)

# Function to log when the file is opened
def open_file(filename):
    logging.info({'event': 'File opened', 'file': filename, 'timestamp': str(datetime.now())})

# Function to log when the file is closed
def close_file(filename):
    logging.info({'event': 'File closed', 'file': filename, 'timestamp': str(datetime.now())})

# Function to read and print the content of the file, and log each line
def read_file(filename):
    #
    #
    #
    # r for reading the f which is the file containing the data
    try:
        with open(filename, 'r') as f:
            open_file(filename)  # Log file open operation
            lines = []
            for line in f:
                line = line.strip()
                lines.append(line)
                logging.info({'event': 'Read line', 'file': filename, 'line': line, 'timestamp': str(datetime.now())})  # Log each line read
                print(line)  # Print each line (strip to remove newline characters)
            print("----")
            pprint({'event': 'File content', 'file': filename, 'lines': lines})  # Print all lines read in a structured way

            #
            #
            # different scenarios in case the data is not there
    except FileNotFoundError:
        logging.error({'event': 'File not found', 'file': filename, 'timestamp': str(datetime.now())})
        print("The file you want to read doesn't exist")
    except Exception as e:
        logging.error({'event': 'Error reading file', 'file': filename, 'error_message': str(e), 'timestamp': str(datetime.now())})
        print(f"Error reading file: {str(e)}")
    finally:
        close_file(filename)  # Log file close operation
    #
    #
    #
    #

# Example usage
filename = "more_names.txt"
read_file(filename)

