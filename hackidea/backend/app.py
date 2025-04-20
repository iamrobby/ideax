from dotenv import load_dotenv , find_dotenv
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

dotenv_path = find_dotenv()
print("Loading .env file from:", dotenv_path) 
load_dotenv()  
# Configure the Gemini API key
  # Replace with your actual API key
print("GEMINI_API_KEY:", os.getenv("GEMINI_API_KEY"))
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Flask app setup
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})  # Enable CORS to allow requests from React


@app.route('/')
def home():
    return "Flask is running!"

# Configure the Gemini model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction="generate the idea and the code to create a web app: on Education track using MERN stack, give me the Idea to build one innovative app, use cases of the app, innovative features, provide the code for the web app, provide the flow structure, best practices to maintain code in JSON format",
)

@app.route('/generate', methods=['POST'])
def generate():
    try:
        # Get input from the React frontend
        data = request.json
        idea=data.get('idea','')
        track=data.get('track','none')
        tech_stack=data.get('techstack','mern stack')
        response_text=f"Generated Idea for {track} track using {tech_stack} stack: {idea}"

        # Start a chat session with the Gemini model
        chat_session = model.start_chat(
            history=[
                {"role": "user", "parts": [idea]},
                {
        "role": "model",
        "parts": [
            "## MERN Stack Web App Idea: Personalized Learning Path Generator\n\n**Idea:**  An educational web application that generates personalized learning paths based on a user's skill level, learning goals, and preferred learning styles.  Instead of offering generic courses, it dynamically curates a sequence of resources (videos, articles, quizzes, interactive exercises) from various platforms, tailoring the experience for optimal learning efficiency.\n\n**Use Cases:**\n\n* **Students:**  Discover the most efficient path to master a specific skill or subject.  Get personalized recommendations for learning materials, avoiding irrelevant content. Track their progress and identify knowledge gaps.\n* **Educators:** Use the app to create customized learning paths for their students, leveraging existing online resources. Analyze student performance data to improve curriculum design.\n* **Professionals:**  Upskill or reskill in a specific area by creating a personalized learning path aligned with their career goals.\n\n\n**Innovative Features:**\n\n* **Adaptive Learning Algorithm:**  The core of the app.  It analyzes user responses to quizzes and assessments to dynamically adjust the difficulty and content of the learning path.\n* **Multi-Platform Resource Integration:** The app integrates with various educational platforms (e.g., YouTube, Coursera, Khan Academy, Udemy) to provide a broad range of learning materials. It doesn't create its own content but acts as a smart curator.\n* **Learning Style Analysis:** The app incorporates a learning style assessment (e.g., VARK) to personalize the content format (video, text, interactive exercises) to match the user's preferences.\n* **Progress Tracking and Gamification:**  Users can track their progress visually, earn badges for completing milestones, and compete with friends (optional).\n* **Community Forum:**  A platform for users to connect, share learning resources, and ask questions.\n\n\n**Flow Structure:**\n\n1. **User Registration/Login:**  The user creates an account or logs in using existing credentials (e.g., Google, Facebook).\n2. **Skill/Goal Selection:** The user selects their desired skill or learning goal (e.g., \"Learn Python,\" \"Master Data Analysis\").\n3. **Learning Style Assessment (Optional):** The user takes a short quiz to determine their preferred learning style.\n4. **Learning Path Generation:** The app's algorithm generates a personalized learning path based on the user's inputs.\n5. **Learning Path Navigation:** The user navigates through the curated resources, completing quizzes and assessments along the way.\n6. **Progress Tracking:** The app visually tracks the user's progress and provides feedback.\n7. **Community Interaction (Optional):**  Users can participate in the community forum.\n\n\n**Partial Code Example (MERN Stack - Focus on Backend Logic):**\n\nThis example demonstrates a simplified version of the learning path generation using Node.js and Express.  The actual implementation would be more complex, involving database interactions and API calls to external platforms.\n\n```javascript\n// server.js (Node.js with Express)\n\nconst express = require('express');\nconst app = express();\n// ... other imports (MongoDB, etc.)\n\n// Sample learning resources (replace with database interaction)\nconst resources = {\n  \"python\": [\n    { type: \"video\", url: \"https://www.youtube.com/watch?v=...\", title: \"Python Intro\" },\n    { type: \"article\", url: \"https://www.example.com/python-tutorial\", title: \"Python Basics\" }\n  ],\n  \"dataAnalysis\": [\n    // ... data analysis resources\n  ]\n};\n\napp.get('/api/learningPath/:skill', (req, res) => {\n  const skill = req.params.skill;\n  if (resources[skill]) {\n    res.json(resources[skill]);\n  } else {\n    res.status(404).json({ error: \"Skill not found\" });\n  }\n});\n\n// ... rest of the server code\n```\n\n\n**Best Practices (JSON):**\n\n```json\n{\n  \"codeStyle\": \"consistent indentation, meaningful variable names\",\n  \"testing\": \"unit tests for backend logic, integration tests for API calls\",\n  \"versionControl\": \"Git with frequent commits and meaningful commit messages\",\n  \"databaseDesign\": \"NoSQL database (MongoDB) for flexibility, schema design for efficient querying\",\n  \"security\": \"input validation, authentication, authorization, secure API keys\",\n  \"deployment\": \"CI/CD pipeline for automated deployment (e.g., using Docker and Kubernetes)\",\n  \"documentation\": \"API documentation (Swagger/OpenAPI), code comments\"\n}\n```\n\n**Note:** This is a high-level overview. Building a complete web application requires significantly more code and detailed planning for the frontend (React), database integration (MongoDB), and API interactions with external platforms.  The code example provides a starting point for the backend logic.  The frontend would involve React components for user interaction, displaying the learning path, and handling progress tracking.  Remember to handle authentication and authorization securely.\n",
        ],
        },
            ]
        )

        # Send the user's input to the model
        response = chat_session.send_message(idea)

        # Return the model's response to the React frontend
        return response.text.strip(),200,{"Content-Type": "text/plain"}
    except Exception as e:
        return  str(e),500,{"Content-Type": "text/plain"}

if __name__ == '__main__':
    app.run(debug=True,port=5001)  # Run the Flask app on port 5000