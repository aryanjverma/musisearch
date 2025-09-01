from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class MelodyRequest(BaseModel):
    notes: List[str]

class MelodyResponse(BaseModel):
    matches: List[str]  

@router.post("/search", response_model=MelodyResponse)
def search_melody(request: MelodyRequest):
    user_notes = request.notes
    
    return {"matches": ["Song A", "Song B"]}