# ideax
HackMate: AI Project Idea Generator & Python Error Checker
HackMate is a web-based platform designed to help Python developers with two key features:
1.	AI-Powered Project Idea Generator
2.	Python Code Error Checker
Overview
HackMate provides two main tools:
1.	We have
2.	1)	AI-powered idea generator
3.	2)	Error Checker
4.	The AI-powered idea generator 
5.	This idea fetches an API (Gemini) and predicts an idea for you on the basis of the required tech stack and domain you want
6.	The ERROR CHECKER
7.	The error checker allows you to enter your Python code and get the error present in your code FOR now the code can detect attribute error , runtime error and syntax error .The final version is visioned to allow code in any high level programming language and access all type of errors including arithmetical and logical errors. THE FINAL VISION IS TO IMPLEMENT an AI-powered code debugger along with it which will help coders to remove errors.
Features
•	AI-Powered Project Ideas:
Input a domain or topic (e.g., "Machine Learning," "Education") to receive a detailed project idea and workflow.
•	Error Detection for Python Code:
Paste your Python code into the error checker, and it will identify runtime errors, attribute errors, and name errors.
Technologies Used
•	Frontend:
o	HTML
o	CSS
o	React.js
•	Backend:
o	Flask (Python)
•	AI:
o	GEMINI API KEY
Setup and Installation
Prerequisites
•	Python 3.x
•	Node.js and npm
•	Flask
•	Vite,React
•	GEMINI API KEY (for idea generation)
Clone the Repository
bash

git clone https://github.com/your-username/HackMate.git
cd HackMate
Backend (Flask) Setup
1.	Install dependencies:
Bash
pip install flask
pip install -r requirements.txt
2.	Run the Flask server:
Bash
python app.py
The Flask backend will be running on http://localhost:5001.
Frontend (React) Setup
1.	Navigate to the frontend folder:
bash
cd frontend
2.	Install dependencies:
Bash

npm install
3.	Start the React development server:
Install vite

    npm start
The React frontend will be running on http://localhost:3000.                 Or any other according to preference
Environment Variables
•	Add your gemini key to the .env file in the backend folder. Example:
bash
CopyEdit
GEMINI_API_KEY=”your api key”
Usage
AI Project Idea Generator
1.	Go to the Idea Generator page.
2.	Input a domain or topic (e.g., "AI," "Education", ”entertainment”).
3.	Click Generate Idea to receive a project idea and detailed workflow.
Python Code Error Checker
1.	Go to the Error Checker page.
2.	Paste your Python code into the provided text box.
3.	Click Check for Errors to get feedback on any runtime, attribute, or name errors.
Contributing
We welcome contributions to improve HackMate! If you'd like to contribute, follow these steps:
1.	Fork the repository
2.	Create a new branch for your feature or fix
3.	Make your changes
4.	Open a pull request with a clear description of your changes

