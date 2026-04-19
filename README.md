# AI-course-Project-LLM

## 1. Project Description

This application allows users to enter a topic and receive an AI-generated explanation in different styles.

The user can choose how the explanation is presented, such as:
- explaining like a 5-year-old
- using a caveman-style explanation
- providing a detailed technical explanation

The goal is to make learning more flexible and engaging by adapting explanations to different levels of understanding.

## 2. Architecture Overview

The application follows a client–server architecture:

React (Frontend) → FastAPI (Backend) → Gemini LLM → Response → Frontend UI

- The frontend sends user input and selected mode via HTTP (POST request)
- The backend processes the request and builds a prompt
- The prompt is sent to a language model
- The response is returned as JSON and displayed in the UI

## 3. Technical Choices

- React  
  Used for building the user interface because it allows efficient state management and dynamic updates.

- FastAPI  
  Used for the backend because it is fast, simple, and automatically handles request validation.

- Pydantic  
  Used to validate incoming request data (`text` and `mode`).

- LangChain  
  Used to interact with the LLM in a structured way.

- Google Gemini (ChatGoogleGenerativeAI)  
  Used as the LLM provider for generating explanations.

Reasoning:
These technologies were chosen for simplicity, speed of development, and good support for AI integration.

## 1. Setup and Running Instructions

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd <your-project-folder>
```

### 2. Backend setup
```bash
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create a .env file inside the backend folder:
```env
GOOGLE_API_KEY=your_api_key_here
```

Run backend:
```bash
uvicorn main:app --reload
```

### 3. Frontend setup
```bash
cd frontend
npm install
npm run dev
```

## 4. Use the app
1. Enter a topic
2. Select a mode
3. Click "Explain"

## 5. Known Limitations
- No authentication (API is publicly accessible)
- No rate limiting (risk of excessive API usage)
- CORS is fully open ("*") → not secure for production
- No input validation (empty or harmful input allowed)
- No loading state in UI
- Limited error handling
- No conversation memory (single request-response only)
- Depends on external AI service (cost and latency)

## 6. AI Tools Used

AI tools were used to assist development and learning, but all code was reviewed and understood before implementation.

ChatGPT (GPT-5.3)
Used for:
explaining concepts
debugging frontend/backend integration
improving prompt design
structuring project and README
Used for small code suggestions