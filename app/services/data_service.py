import uuid
from datetime import datetime
from typing import Dict, Any, Optional

class DataService:
    def __init__(self):
        # In-memory storage (in production, use a real database)
        self.chat_sessions = {}
        self.quiz_sessions = {}
        self.leads_database = {}

    # Quiz Session Management
    def create_quiz_session(self, answers: Dict[str, Any], exclude_careers: list) -> str:
        """Create a new quiz session and return session ID"""
        session_id = str(uuid.uuid4())
        self.quiz_sessions[session_id] = {
            "answers": answers,
            "exclude_careers": exclude_careers,
            "timestamp": datetime.now().isoformat(),
            "contact_info": None
        }
        return session_id

    def get_quiz_session(self, session_id: str) -> Optional[Dict]:
        """Get quiz session data"""
        return self.quiz_sessions.get(session_id)

    def update_quiz_contact(self, session_id: str, contact_info: Dict):
        """Update quiz session with contact information"""
        if session_id in self.quiz_sessions:
            self.quiz_sessions[session_id]["contact_info"] = contact_info

    # Chat Session Management
    def create_chat_session(self, session_id: Optional[str] = None) -> str:
        """Create or get existing chat session"""
        if not session_id:
            session_id = str(uuid.uuid4())

        if session_id not in self.chat_sessions:
            self.chat_sessions[session_id] = {
                "conversation_history": [],
                "quiz_data": None,
                "user_context": {}
            }
        return session_id

    def add_chat_message(self, session_id: str, role: str, content: str):
        """Add message to chat history"""
        if session_id in self.chat_sessions:
            self.chat_sessions[session_id]["conversation_history"].append({
                "role": role,
                "content": content
            })

    def get_chat_session(self, session_id: str) -> Optional[Dict]:
        """Get chat session data"""
        return self.chat_sessions.get(session_id)

    def clear_chat_session(self, session_id: str) -> bool:
        """Clear chat session"""
        if session_id in self.chat_sessions:
            del self.chat_sessions[session_id]
            return True
        return False

    # Booking Management
    def create_booking(self, booking_data: Dict) -> str:
        """Create a new consultation booking"""
        booking_id = str(uuid.uuid4())
        self.leads_database[booking_id] = {
            **booking_data,
            "booking_time": datetime.now().isoformat(),
            "status": "booked"
        }

        # Update quiz session with booking info
        session_id = booking_data.get("session_id")
        if session_id in self.quiz_sessions:
            self.quiz_sessions[session_id]["contact_info"] = {
                "name": booking_data.get("name"),
                "email": booking_data.get("email"),
                "phone": booking_data.get("phone")
            }

        return booking_id

    # Analytics and Admin
    def get_analytics(self) -> Dict:
        """Get system analytics"""
        return {
            "total_leads": len(self.leads_database),
            "bookings": list(self.leads_database.values()),
            "quiz_sessions": len(self.quiz_sessions),
            "chat_sessions": len(self.chat_sessions)
        }

# Global instance - in production, use dependency injection
data_service = DataService()
