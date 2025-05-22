

# from dotenv import load_dotenv
# import os
# import replicate
# import logging
# from pydantic import BaseModel
# from typing import Optional

# # Load .env into environment
# load_dotenv()

# # Initialize Replicate client
# client = replicate.Client(api_token=os.getenv("REPLICATE_API_KEY"))

# # Optional: configure logging to see debug output
# logging.basicConfig(level=logging.INFO)

# class ImageGenRequest(BaseModel):
#     blueprint: str
#     concept: str
#     visual_style: str
#     fmt: str
#     grade: Optional[str] = None

# def generate_image(req: ImageGenRequest) -> str:
#     """
#     Calls Stability-AI SDXL on Replicate to render the image based on the blueprint.
#     Returns a URL (string) to the generated image.
#     """
#     img_prompt = (
#         f"{req.fmt} of '{req.concept}'. Style: {req.visual_style}. "
#         f"Blueprint:\n{req.blueprint}"
#     )

#     outputs = client.run(
#         "stability-ai/sdxl:610dddf033f10431b1b55f24510b6009fcba23017ee551a1b9afbc4eec79e29c",
#         input={
#             "width": 1024,
#             "height": 1024,
#             "prompt": img_prompt,
#             "refine": "expert_ensemble_refiner",
#             "scheduler": "KarrasDPM",
#             "num_outputs": 1,
#             "guidance_scale": 7.5,
#             "high_noise_frac": 0.8,
#             "prompt_strength": 0.8,
#             "num_inference_steps": 50
#         }
#     )

#     # Expect a list of FileOutput objects
#     if isinstance(outputs, list) and outputs:
#         first = outputs[0]
#         url = getattr(first, "url", str(first))
#         logging.info(f"Generated image URL: {url}")
#         return url

#     raise RuntimeError("Image generation failed or returned no outputs")


















# imagegen.py

from dotenv import load_dotenv
import os
import replicate
import logging
from pydantic import BaseModel
from typing import Optional

# Load .env into environment
load_dotenv()

# Initialize Replicate client
client = replicate.Client(api_token=os.getenv("REPLICATE_API_KEY"))

# Optional: configure logging to see debug output
logging.basicConfig(level=logging.INFO)

class ImageGenRequest(BaseModel):
    blueprint: str
    concept: str
    visual_style: str
    fmt: str
    grade: str = None
    style: str = None
    mood: str = None
    use_case: str = None

def generate_image(req: ImageGenRequest) -> str:
    """
    Calls Stability-AI SDXL on Replicate to render the image based on the blueprint.
    Returns a URL (string) to the generated image.
    """
    img_prompt = (
        f"{req.use_case} of the concept '{req.concept}' in a {req.fmt} format. "
        f"Style: {req.visual_style}, Image Style: {req.style}, Mood: {req.mood}, Grade: {req.grade}. "
        f"Visual Blueprint: {req.blueprint}"
    )

    outputs = client.run(
        "stability-ai/sdxl:610dddf033f10431b1b55f24510b6009fcba23017ee551a1b9afbc4eec79e29c",
        input={
            "width": 1024,
            "height": 1024,
            "prompt": img_prompt,
            "refine": "expert_ensemble_refiner",
            "scheduler": "KarrasDPM",
            "num_outputs": 1,
            "guidance_scale": 7.5,
            "high_noise_frac": 0.8,
            "prompt_strength": 0.8,
            "num_inference_steps": 50
        }
    )

    # Expect a list of FileOutput objects or strings
    if isinstance(outputs, list) and outputs:
        first = outputs[0]
        url = getattr(first, "url", str(first))
        logging.info(f"Generated image URL: {url}")
        return url

    raise RuntimeError("Image generation failed or returned no outputs")
