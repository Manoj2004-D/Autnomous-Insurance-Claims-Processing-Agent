from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from fastapi import UploadFile, File
from services.pdf_reader import extract_text
from services.extractor import extract_fields
from services.validator import validate_claim
from services.router import recommend_route
from models.schemas import ClaimData
from pydantic import ValidationError


app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
    request=request,
    name="index.html",
    context={"request": request}
)

@app.post("/process-claim")
async def process_claim(file: UploadFile = File(...)):

    text = extract_text(file)

    extracted_data = extract_fields(text)
    try:

        claim = ClaimData(**extracted_data)
    except ValidationError as e:

        return {"error":"Validation Failed","details":e.errors()}
    

    claim_dict = claim.model_dump()

    if "error" in extracted_data:
        return extracted_data

    missing_fields = validate_claim(claim_dict)

    route, reason = recommend_route(claim_dict,missing_fields)

    return {

        "extractedFields": claim_dict,

        "missingFields": missing_fields,

        "recommendedRoute": route,

        "reasoning": reason

    }


