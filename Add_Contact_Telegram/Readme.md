# Telegram Python Code Repository

Welcome to the Telegram Python Code Repository! This repository contains Python scripts for working with Telegram, a popular messaging platform.

## Table of Contents

- [Introduction](#introduction)
- [Scripts](#scripts)
  - [Extract Contacts and Convert to CSV](#extract-contacts-and-convert-to-csv)
  - [Add Contacts to Telegram](#add-contacts-to-telegram)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Telegram offers a versatile platform for messaging, and with the provided Python scripts, you can automate tasks such as extracting contacts from text files and adding them to your Telegram app.

## Scripts

### Extract Contacts and Convert to CSV

Author: Amir Sarrafzadeh Arasi  
Date: 2024-04-06

#### Purpose

- This script extracts contacts from a text file, converts them to a dictionary, and saves them to a CSV file.
- It utilizes the pandas library to create a DataFrame and save it to a CSV file.

#### Preconditions

- The text file should be available in the same directory as the script.
- The text file should contain the contacts in JSON format.
- The script should be run on a machine with the pandas library installed.

### Add Contacts to Telegram

Author: Amir Sarrafzadeh Arasi  
Date: 2024-04-06

#### Purpose

- This script adds contacts to the Telegram app.
- It reads contacts from a CSV file and adds them one by one to the Telegram app.
- The pyautogui library is used to automate the process of adding contacts.

#### Preconditions

- The contacts.csv file should be available in the same directory as the script.
- The contacts.csv file should contain the following columns: Name, Last Name, Phone Number.
- The script should be run on a machine with the Telegram app installed.

#### Post-conditions

- The contacts will be added to the Telegram app.
- The script navigates to the contacts section of the Telegram app and adds the contacts one by one.

## Usage

To use these scripts, follow these steps:

1. Ensure that the necessary preconditions are met for each script.
2. Run the script using Python.
3. Follow any prompts or instructions provided by the script.

## Contributing

Contributions to this repository are welcome! If you have any improvements or additional scripts related to Telegram, feel free to open a pull request.

To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or improvement.
3. Commit your changes with descriptive messages.
4. Push your changes to your fork.
5. Open a pull request, explaining the purpose of your changes.

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Note**: This repository is maintained by [Amir Sarrafzadeh Arasi](https://github.com/AmirSarrafzadeh). If you have any questions or suggestions, feel free to reach out!
