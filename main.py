# # main.py

# from dotenv import load_dotenv
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel, Field
# from typing import Optional, Literal

# from Textgen import generate_blueprint, TextGenRequest
# from Imagegen import generate_image, ImageGenRequest

# load_dotenv()

# class ConceptVisualRequest(BaseModel):
#     concept: str = Field(..., example="Gravity")
#     visual_style: Literal["Iconic", "Abstract", "Metaphoric"] = Field(
#         ..., example="Metaphoric", description="Choose a visual style"
#     )
#     format: Literal["Diagram", "Poster", "Icon Set"] = Field(
#         ..., example="Diagram", description="Choose an output format"
#     )
#     language: Literal["en", "es", "fr", "de", "zh"] = Field(
#         "en", example="en", description="Select language code"
#     )
#     grade_level: Literal[
#         "Kindergarten",
#         "1st Grade",
#         "2nd Grade",
#         "3rd Grade",
#         "4th Grade",
#         "5th Grade",
#         "6th Grade",
#         "7th Grade",
#         "8th Grade",
#         "9th Grade",
#         "10th Grade",
#         "11th Grade",
#         "12th Grade",
#         "Undergraduate",
#         "Graduate",
#     ] = Field(
#         ..., example="5th Grade", description="Select the student’s grade level"
#     )
#     pedagogical_style: Literal["Constructive", "Collaborative", "Integrative", "Reflective", "Inquiry-Based"] = Field(
#         "Expository", example="Narrative", description="Choose a teaching style"
#     )
#     learner_style: Literal["Visual", "Verbal", "Kinesthetic"] = Field(
#         "Visual", example="Visual", description="Select the learner’s preferred style"
#     )

# class ConceptVisualResponse(BaseModel):
#     blueprint: str
#     image_url: str
#     caption: str

# app = FastAPI()

# @app.post("/generate-concept-visual", response_model=ConceptVisualResponse)
# async def generate_concept_visual(req: ConceptVisualRequest):
#     try:
#         # 1) Generate text blueprint
#         text_req = TextGenRequest(
#             concept=req.concept,
#             visual_style=req.visual_style,
#             fmt=req.format,
#             language=req.language,
#             grade=req.grade_level,
#             pedagogical_style=req.pedagogical_style,
#             learner_style=req.learner_style
#         )
#         blueprint = generate_blueprint(text_req)

#         # 2) Generate image
#         img_req = ImageGenRequest(
#             blueprint=blueprint,
#             concept=req.concept,
#             visual_style=req.visual_style,
#             fmt=req.format,
#             grade=req.grade_level
#         )
#         image_url = generate_image(img_req)

#         # 3) Extract first line as caption
#         caption = blueprint.splitlines()[0] if blueprint else ""

#         return ConceptVisualResponse(
#             blueprint=blueprint,
#             image_url=image_url,
#             caption=caption
#         )

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)




















# main.py

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, Literal

from Textgen import generate_blueprint, TextGenRequest
from Imagegen import generate_image, ImageGenRequest

load_dotenv()

class ConceptVisualRequest(BaseModel):
    concept: str = Field(..., example="Gravity")
    visual_style: Literal["Iconic", "Abstract", "Metaphoric"] = Field(
        ..., example="Metaphoric", description="Choose a visual style"
    )
    format: Literal["Diagram", "Poster", "Icon Set"] = Field(
        ..., example="Diagram", description="Choose an output format"
    )
    language: Literal["en", "es", "fr", "de", "zh"] = Field(
        "en", example="en", description="Select language code"
    )
    grade_level: Literal[
        "Kindergarten", "1st Grade", "2nd Grade", "3rd Grade", "4th Grade",
        "5th Grade", "6th Grade", "7th Grade", "8th Grade", "9th Grade",
        "10th Grade", "11th Grade", "12th Grade", "Undergraduate", "Graduate"
    ] = Field(
        ..., example="5th Grade", description="Select the student’s grade level"
    )
    pedagogical_style: Literal["Constructive", "Collaborative", "Integrative", "Reflective", "Inquiry-Based"] = Field(
        "Constructive", example="Constructive", description="Choose a teaching style"
    )
    learner_style: Literal["Visual", "Verbal", "Kinesthetic"] = Field(
        "Visual", example="Visual", description="Select the learner’s preferred style"
    )
    style: Literal["futuristic", "hand-drawn", "realistic", "sketch", "minimalist"] = Field(
        "futuristic", example="futuristic", description="Select the artistic style"
    )
    mood: Literal["inspiring", "clean", "fun", "serious", "dynamic"] = Field(
        "inspiring", example="inspiring", description="Set the image mood"
    )
    use_case: Literal["educational comic scene", "explainer diagram", "learning visual aid"] = Field(
        "educational comic scene", example="educational comic scene", description="Define the use case"
    )

class ConceptVisualResponse(BaseModel):
    blueprint: str
    image_url: str
    caption: str

app = FastAPI()

@app.post("/generate-concept-visual", response_model=ConceptVisualResponse)
async def generate_concept_visual(req: ConceptVisualRequest):
    try:
        # 1) Generate text blueprint
        text_req = TextGenRequest(
            concept=req.concept,
            visual_style=req.visual_style,
            fmt=req.format,
            language=req.language,
            grade=req.grade_level,
            pedagogical_style=req.pedagogical_style,
            learner_style=req.learner_style
        )
        blueprint = generate_blueprint(text_req)

        # 2) Generate image
        img_req = ImageGenRequest(
            blueprint=blueprint,
            concept=req.concept,
            visual_style=req.visual_style,
            fmt=req.format,
            grade=req.grade_level,
            style=req.style,
            mood=req.mood,
            use_case=req.use_case
        )
        image_url = generate_image(img_req)

        # 3) Extract first line as caption
        caption = blueprint.splitlines()[0] if blueprint else ""

        return ConceptVisualResponse(
            blueprint=blueprint,
            image_url=image_url,
            caption=caption
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
