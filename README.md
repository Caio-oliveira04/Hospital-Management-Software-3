# Hospital Management Software

This is a project for the "Software Project" course. The software aims to provide comprehensive functionalities for hospital management.

### 📋 Prerequisites

Before running the project, make sure you have PyQt5 installed, which is the library used to develop the graphical interface. You can install it using pip, the Python package manager, with the following command:
  
  - [$ pip install PyQt5]

Additionally, you need to have Python installed on your system. 

So, the prerequisites to run the project are:

* Installed Python

* Installed PyQt5

## 🛠️ Built with

* [Python](https://www.python.org/) - Programming language
  - [Python Installation Guide](https://www.python.org/downloads/)

* [Visual Studio Code](https://code.visualstudio.com/) - Integrated Development Environment (IDE)
  - [Visual Studio Code Installation Guide](https://code.visualstudio.com/download/)

* [PyQt5](https://pypi.org/project/PyQt5/) - Library for developing graphical interfaces in Python
  - [$ pip install PyQt5]

## ⚙️ Running the tests

With PyQt5 properly installed and the project directory open in the Command Prompt, type "python Main.py", or execute the Main file using the "run" button in Visual Studio Code. To test user functionalities, sign up and explore the available options for the user.

To access the doctor's functionalities, make sure you're on the doctor login screen. For testing purposes, there is already a doctor registered with the following credentials:

CRM : 123456-SP

Password: 123

However, you can also register a doctor through the server functionalities.

To access server functionalities, in this case, a manager, use the following login:

Email: gerente@gmail.com

Password: 123

This way, you can test the options available for a manager.

## 📌 Version

Version with a graphical interface, elements of the object-oriented paradigm, and the 'Facade' design pattern.

## ✒️ Authors

* **Caio Oliveira França dos Anjos**

## 🚀 Future Improvements

- Add automated tests to ensure software stability.
- Consider adding new functionalities based on community feedback.
- Enhance the graphical interface by implementing a dialog system to indicate errors.

## User Screen
This should be the first screen when running the program. In the image, two buttons are highlighted that will switch between screens.
![imagem login](https://github.com/Caio-oliveira04/Hospital-Management-Software-3/assets/131555188/aa63e268-21e0-41c6-bbe6-e7428bced1fd)

- Para make an appointment: you must choose a specialist, make the deposit in the amount of the consultation indicated next to the specialist's name, choose the date, and then schedule. Once scheduled, you can view them in the scheduled appointments field, and select one to reschedule (if you wish, you must choose the new date and then click on reschedule), if you want to cancel, just select the appointment and click on cancel. 

- The requested exams will only be displayed on your profile if the doctor requests an exam for you. Once requested, you can select the one you want, and it will automatically go to your list of completed exams, where you can see the result.
![image](https://github.com/Caio-oliveira04/Hospital-Management-Software-3/assets/131555188/1d7611b1-4e99-4f63-8a3b-2b1f92b2c2c6)

## Doctor screen
- Note that the login parameters are different, use the information provided in the "Running the tests" section
![image](https://github.com/Caio-oliveira04/Hospital-Management-Software-3/assets/131555188/0f7bc719-d92b-44e4-b3ec-5ec989878d5c)

-To consult a person, you can select one from the list, and see their medical record, and then make the decision to request an exam or medicine and click on the button to the right of the list. (the field for sending observation is not yet included in this update).
![image](https://github.com/Caio-oliveira04/Hospital-Management-Software-3/assets/131555188/ace000f2-37d3-479a-b6c4-ffcba592c6db)

## Server screen
- Use the information provided in the "Running the tests" section
![image](https://github.com/Caio-oliveira04/Hospital-Management-Software-3/assets/131555188/e12c8096-a049-4bb2-ba01-589c28aaae81)

-in this section, you can reserve rooms, or vacate them, add or view your stock, register doctors, and create a work schedule (field still under development).
![image](https://github.com/Caio-oliveira04/Hospital-Management-Software-3/assets/131555188/2359f9c3-b7d9-46d3-8185-00b7b1b83b19)














