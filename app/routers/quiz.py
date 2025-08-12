from fastapi import APIRouter
from app.models.schemas import AnswersIn, BookingRequest
from app.services.data_service import data_service
from app.services.ai_service import AIService
from app.data.quiz_data import CAREER_QUIZ, CAREER_OPTIONS

router = APIRouter(prefix="/api")

@router.get("/quiz")
async def get_quiz():
    """Get the career quiz questions"""
    return CAREER_QUIZ

@router.get("/quiz/start")
async def start_quiz():
    """Initialize a new quiz session and return quiz data"""
    return {
        "quiz_questions": CAREER_QUIZ,
        "career_options": CAREER_OPTIONS,
        "total_questions": len(CAREER_QUIZ),
        "message": "Quiz session started successfully"
    }

@router.get("/career-options")
async def get_career_options():
    """Get available career options for exclusion"""
    return {"career_options": CAREER_OPTIONS}

@router.post("/submit-answers")
async def submit_answers(payload: AnswersIn):
    """Submit quiz answers and create session"""
    session_id = data_service.create_quiz_session(
        answers=payload.answers,
        exclude_careers=payload.exclude_careers
    )
    return {"session_id": session_id}

@router.post("/generate-preview")
async def generate_preview(request: dict):
    """Generate AI career preview for a session"""
    session_id = request.get("session_id")
    if not session_id:
        return {"error": "Session ID is required"}

    quiz_data = data_service.get_quiz_session(session_id)
    if not quiz_data:
        return {"error": "Session not found"}

    prompt = f"Answers: {quiz_data['answers']}, Exclude: {quiz_data['exclude_careers']}"
    try:
        ai_response = await AIService.generate_career_preview(prompt)
        return {"ai_preview": ai_response}
    except Exception as e:
        return {"error": str(e)}

@router.post("/book-consultation")
async def book_consultation(booking: BookingRequest):
    """Book a career consultation"""
    booking_data = booking.model_dump()
    booking_id = data_service.create_booking(booking_data)

    return {
        "success": True,
        "booking_id": booking_id,
        "message": "Consultation booked successfully"
    }
