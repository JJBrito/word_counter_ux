# word_counter_ux

The "Word Counter UX" is project for an application that counts the number of words in a given text.
The project involves a Python backend application that utilizes the Flask framework to integrate with an HTML code in the frontend, allowing users to interact with the application.

# Features

- Simple user interface for entering the text to be counted.
- Integration between the Python backend and HTML frontend using Flask.
- Display of word count results and error messages in the interface.

# Installation

- Make sure you have Python installed on your system.
- Install Flask using the following command:

# Usage

- Run the app.py script using the following command:
    . Open a web browser and access http://localhost:5000.
    . Enter the text for which you want to count the words in the input field.
- Click the "Calculate" button to see the word count result or receive an error message if applicable.

# Code Overview

- Flask is used to create a web server and route requests to the correct function.
- The index function handles POST requests from the HTML form.
- The entered text is split into words, and each word is checked for punctuation and alphabetical characters to calculate the word count.
- The result of the word count or the error message is displayed in the HTML template.

# Contributions

This project is public, and positive contributions are always welcome!
Be my guest to submit a pull request.


