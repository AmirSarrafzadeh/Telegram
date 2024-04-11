"""
This script is used to add contacts to the Telegram App.

Author: Amir Sarrafzadeh Arasi
Date: 2024-04-06

Purpose:
    - The purpose of this script is to add contacts to the Telegram App.
    - The script reads the contacts.csv file and adds the contacts to the Telegram App.
    - The script uses the pyautogui library to automate the process of adding contacts to the Telegram App.

Preconditions:
    - The contacts.csv file should be available in the same directory as the script.
    - The contacts.csv file should contain the following columns: Name, Last Name, Phone Number.
    - The script should be run on a machine that has the Telegram App installed.

Post-conditions:
    - The contacts will be added to the Telegram App.
    - The script will navigate to the contacts section of the Telegram App and add the contacts one by one.
    - The script will use the pyautogui library to automate the process of adding contacts.

Usage:
    - Run the script by executing the following command: python add_contact_telegram.py
    - The script will read the contacts.csv file and add the contacts to the Telegram App.
    - The script will navigate to the contacts section of the Telegram App and add the contacts one by one.
    - The script will display a message indicating that the contacts have been added successfully.
"""

# Import the required libraries
import time
import logging
import pyperclip
import pyautogui
import pandas as pd

# Configure the logging module
logging.basicConfig(filename='telegram_contact_addition.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Define the function to open Telegram and navigate to the contacts section
def open_telegram_and_navigate_to_contacts(dataframe):
    sleep_time = 1
    for i in range(len(dataframe)):
        try:
            logging.info(f"Adding contact {i + 1}...")
            time.sleep(10)
            pyautogui.click(x=35, y=46)
            time.sleep(sleep_time)
            pyautogui.click(x=50, y=250)
            time.sleep(sleep_time)
            pyautogui.click(x=840, y=770)
            time.sleep(sleep_time)
            pyautogui.click(x=950, y=440)
            name = dataframe['Name'][i]
            pyperclip.copy(name)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(sleep_time)
            pyautogui.click(x=950, y=500)
            surname = dataframe['Last Name'][i]
            pyperclip.copy(surname)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(sleep_time)
            pyautogui.click(x=950, y=600)
            tel_number = str(dataframe['Phone Number'][i])
            pyperclip.copy(tel_number)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(sleep_time)
            pyautogui.click(x=1100, y=650)
            time.sleep(sleep_time)
            pyautogui.click(x=1200, y=650)
            time.sleep(sleep_time)
            logging.info(f"Contact {i + 1} added successfully.")
        except Exception as e:
            logging.error(f"Error adding contact {i + 1}: {e}")


if __name__ == "__main__":
    # Main function to add contacts to Telegram
    try:
        logging.info("Starting the Telegram contact addition process...")
        df = pd.read_csv('contacts.csv').head(4)
        open_telegram_and_navigate_to_contacts(df)
        logging.info("Telegram contact addition process completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

