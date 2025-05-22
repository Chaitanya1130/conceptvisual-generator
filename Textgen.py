

from pydantic import BaseModel
import os
import anthropic

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

class TextGenRequest(BaseModel):
    concept: str
    visual_style: str
    fmt: str
    language: str
    grade: str
    pedagogical_style: str
    learner_style: str
    style: str
    mood: str
    use_case: str

def generate_blueprint(data: TextGenRequest) -> str:
    prompt = f"""
You are an expert education designer. Your task is to create a visual blueprint of the concept '{data.concept}' in {data.language} for a {data.grade} student. 

**Constraints:**
- Visual Style: {data.visual_style}
- Format: {data.fmt}
- Pedagogical Style: {data.pedagogical_style}
- Learner Style: {data.learner_style}
- Image Style: {data.style}
- Mood: {data.mood}
- Use Case: {data.use_case}

Please return the visual blueprint in a short, single-paragraph markdown format that will be fed into an AI image model.
"""

    response = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=4000,
        temperature=0.8,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.content[0].text.strip()
