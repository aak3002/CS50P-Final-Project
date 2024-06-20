# Your Personal Diary
## Video Demo:  <URL HERE>
## Description:

Welcome to the application for your personal diary! You may easily record your ideas, memories, and everyday experiences using this Python application. Write, save, read, and edit journal entries with ease using an easy-to-use command-line interface. The application ensures a clutter-free experience by cleaning the screen after each activity, and each entry is immediately timestamped for convenient reference. This journal software is designed to assist you in recording your journey, whether you want to record a significant occasion or just think back on your day.

## The Functions Used in this Program are:
1)Write Entry: The Write Entry function prompts the user to input their diary entry through the command line. It utilizes the input() function to capture user input and the datetime module to automatically timestamp each entry with the current date and time. The user's input is then formatted into a structured entry with the date and content, ready to be saved to the diary file.

2)Save Entry: The Save Entry function is responsible for storing the user's diary entry in a file named "diary.txt". It uses the open() function to open the diary file in append mode, allowing new entries to be added to the existing content. The entry is then written to the file, ensuring that it is preserved for future reference. By saving entries to a text file, the application provides users with a persistent record of their reflections and experiences.

3)Read Entries: The Read Entries function retrieves and displays all the entries stored in the "diary.txt" file. It uses the open() function to open the diary file in read mode, allowing it to access the content of the file. The function then reads the contents of the file and prints them to the console, presenting the entries in chronological order. By providing users with the ability to review their past entries, the application facilitates self-reflection and introspection.

4)Edit Entry: The Edit Entry function allows users to modify an existing entry in their diary. It prompts the user to select the entry they wish to edit and then enables them to overwrite the content with new text. The function utilizes file manipulation techniques to locate the chosen entry within the diary file and update it with the revised content. By empowering users to revise their entries, the application promotes flexibility and adaptability, allowing users to refine their reflections over time.

## Files in the Folder
1)The project.py file contains the code required to operate the program. It is created by combining various functions that have already been listed above along with their explanations to help us understand how the program runs.

2)The test_project.py file contains manual tests to be run on some functions of project.py file.

3)The README.md file which contains the description of the project as well as all the details

## About Me
Name: Asad Ali Kazi

Location: Pune, Maharashtra, India

## Links:
1)LinkedIn ---> [Asad Ali Kazi](www.linkedin.com/in/asad-ali-kazi)

2)GitHub --> [aak3002](https://github.com/aak3002)
