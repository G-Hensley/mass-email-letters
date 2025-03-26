# Personalized Letter Generator 📬

A Python script that generates personalized letters or emails based on a template and a list of names.

## Description

This script takes a template letter and a list of names, then creates individual, personalized letters by replacing a placeholder (`[name]`) with each name from the list. It’s perfect for automating invitations, thank-you notes, or any kind of mass personalized correspondence.

## Usage

Follow these steps to get started:

1. **Prerequisites**: Make sure you have Python installed on your system (any recent version should work fine).
2. **Setup**:
   - Create this directory structure in your project folder:
   - ./Input/Letters/
   - ./Input/Names/
   - ./Ouput/ReadyToSend/
   - Add your template letter to `./Input/Letters/starting_letter.txt`. Use `[name]` wherever you want the recipient’s name to appear.
   - Create a file called `invited_names.txt` in `./Input/Names/` and list the names, one per line.
3. **Run the Script**: Open your terminal, navigate to the project folder, and run:
  ```bash
  python generate_letters.py
  ```
4. Output: Check the ./Output/ReadyToSend/ folder for your personalized letters, each named letter_for_{name}.txt.
