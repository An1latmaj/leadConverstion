from pydantic import BaseModel, Field
from typing import Dict, List, Any, Optional

class AnswersIn(BaseModel):
    answers: Dict[str, Any]
    exclude_careers: List[str] = Field(default_factory=lambda: [])

class ContactIn(BaseModel):
    session_id: str
    name: str
    email: str
    phone: Optional[str] = None

class ChatMessage(BaseModel):
    session_id: Optional[str] = None
    message: str

class ChatResponse(BaseModel):
    session_id: str
    response: str
    conversation_history: List[Dict[str, str]]

class QuizProgress(BaseModel):
    session_id: str
    current_question: int
    answer: str

class BookingRequest(BaseModel):
    session_id: str
    name: str
    email: str
    phone: str
    preferred_time: str
    message: Optional[str] = None
