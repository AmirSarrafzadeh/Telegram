"""
This script is used to extract contacts from a text file and convert to a dictionary and save them to a CSV file.

Author: Amir Sarrafzadeh Arasi
Date: 2024-04-06

Purpose:
    - The purpose of this script is to extract contacts from a text file and convert them to a dictionary.
    - The script reads the text file and extracts the contacts from it.
    - The script then converts the contacts to a dictionary and saves them to a CSV file.
    - The script uses the pandas library to create a DataFrame and save it to a CSV file.

Preconditions:
    - The text file should be available in the same directory as the script.
    - The text file should contain the contacts in JSON format.
    - The script should be run on a machine that has the pandas library installed.
"""

# Import the required libraries
import json
import pandas as pd
import logging

# Configure the logging module
logging.basicConfig(filename='json_to_csv.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Define the function to read the text file and convert the contacts to a CSV file
def read_txt_and_convert_to_csv(input_file_name):
    try:
        logging.info(f"Reading JSON file '{input_file_name}'...")
        with open(input_file_name, 'r', encoding="utf-8") as file:
            json_string = file.read()
        logging.info("JSON file read successfully.")

        logging.info("Extracting data from JSON file...")
        names = []
        last_names = []
        phone_numbers = []

        for line in json_string.strip().split('\n'):
            temp_dict = json.loads(line)
            if 'message' in temp_dict.keys():
                sub_dict = json.loads(temp_dict['message'])
                names.append(sub_dict.get('first_name', ''))
                last_names.append(sub_dict.get('last_name', ''))
                phone_numbers.append(sub_dict['phone'][2:])
        logging.info("Data extracted successfully.")

        logging.info("Creating DataFrame...")
        df = pd.DataFrame({'Name': names, 'Last Name': last_names, 'Phone Number': phone_numbers})
        logging.info("DataFrame created successfully.")

        logging.info("Saving DataFrame to CSV...")
        df.to_csv('contacts.csv', index=False)
        logging.info("CSV file saved successfully.")
    except Exception as ex:
        logging.error(f"An error occurred: {ex}")


if __name__ == "__main__":
    try:
        logging.info("Starting the JSON to CSV conversion process...")
        file_name = 'sample.txt'
        read_txt_and_convert_to_csv(file_name)
        logging.info("JSON to CSV conversion process completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
