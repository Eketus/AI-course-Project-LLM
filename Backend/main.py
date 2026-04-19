from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_openai import ChatOpenAI

load_dotenv()

# ChatOpenAI
# llm = ChatOpenAI(
#    model="gpt-4o-mini",
#    temperature=0.7
# )

# GoogleAI
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

app = FastAPI()

# Request body structure
class ExplainRequest(BaseModel):
    text: str
    mode: str

@app.post("/explain")
def explain(req: ExplainRequest):
    try:
        if req.mode == "eli5":
            system_prompt = """
You are explaining something to a 5-year-old child.

Rules:
- Use simple words
- Use short sentences
- Add a playful example
- Max 4 sentences
"""

        elif req.mode == "caveman":
            system_prompt = """
Explain like a caveman would.

Rules:
- Use very simple, broken language
- No complex words
- Short sentences
- Example: "Fire hot. Touch = ouch."
- Keep it fun
"""

        elif req.mode == "super":
            system_prompt = """
Explain in very high detail.

Rules:
- Be thorough and detailed
- Use proper terminology
- Give step-by-step explanation if possible
- Include examples where helpful
"""

        else:
            system_prompt = "Explain clearly."

        prompt = f"""
{system_prompt}

Topic:
{req.text}
"""

        response = llm.invoke(prompt)

        return {"response": response.content}

    except Exception as e:
        return {"response": f"Error: {str(e)}"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)