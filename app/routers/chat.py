from fastapi import APIRouter
from app.models.schemas import ChatMessage, ChatResponse
from app.services.data_service import data_service
from app.services.ai_service import AIService

router = APIRouter(prefix="/api")

@router.post("/chat", response_model=ChatResponse)
async def chat_with_ai(chat_input: ChatMessage):
    """Handle chat conversations with AI career counselor"""
    # Create or get existing session
    session_id = data_service.create_chat_session(chat_input.session_id)

    # Add user message to history
    data_service.add_chat_message(session_id, "user", chat_input.message)

    # Prepare messages for AI including system prompt and conversation history
    session = data_service.get_chat_session(session_id)
    messages = [
        {"role": "system", "content": (
            "You are an expert career counselor and life coach. You help people discover their ideal career paths "
            "through thoughtful conversation. You remember previous parts of the conversation and build upon them. "
            "Be friendly, encouraging, and ask follow-up questions to better understand the user's interests, "
            "skills, values, and goals. If they mention specific answers or preferences, remember them throughout "
            "the conversation. Provide personalized career advice and suggestions."
        )}
    ]

    # Add conversation history
    messages.extend(session["conversation_history"])

    # Get AI response
    try:
        ai_response = await AIService.chat_with_ai(messages)

        # Add AI response to history
        data_service.add_chat_message(session_id, "assistant", ai_response)

        return ChatResponse(
            session_id=session_id,
            response=ai_response,
            conversation_history=session["conversation_history"]
        )
    except Exception as e:
        return ChatResponse(
            session_id=session_id,
            response=f"Sorry, I encountered an error: {str(e)}",
            conversation_history=session["conversation_history"]
        )

@router.get("/chat-history/{session_id}")
async def get_chat_history(session_id: str):
    """Get chat conversation history"""
    session = data_service.get_chat_session(session_id)
    if session:
        return {"conversation_history": session["conversation_history"]}
    return {"error": "Session not found"}

@router.delete("/chat-session/{session_id}")
async def clear_chat_session(session_id: str):
    """Clear a chat session"""
    if data_service.clear_chat_session(session_id):
        return {"message": "Session cleared"}
    return {"error": "Session not found"}
