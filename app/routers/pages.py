from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def landing_page():
    """Main landing page for the career quiz"""
    # Move the large HTML content to a template file for better organization
    from app.templates.pages import LANDING_PAGE_HTML
    return HTMLResponse(LANDING_PAGE_HTML)

@router.get("/quiz-start", response_class=HTMLResponse)
async def quiz_start_page():
    """Career exclusion step before quiz"""
    from app.templates.pages import QUIZ_START_HTML
    return HTMLResponse(QUIZ_START_HTML)

@router.get("/quiz", response_class=HTMLResponse)
async def quiz_interface():
    """Main 24-question quiz interface"""
    from app.templates.pages import QUIZ_INTERFACE_HTML
    return HTMLResponse(QUIZ_INTERFACE_HTML)

@router.get("/quiz-complete", response_class=HTMLResponse)
async def quiz_complete():
    """Contact form after quiz completion"""
    from app.templates.pages import QUIZ_COMPLETE_HTML
    return HTMLResponse(QUIZ_COMPLETE_HTML)

@router.get("/results", response_class=HTMLResponse)
async def results_page():
    """Results preview with booking CTAs"""
    from app.templates.pages import RESULTS_PAGE_HTML
    return HTMLResponse(RESULTS_PAGE_HTML)

@router.get("/thank-you", response_class=HTMLResponse)
async def thank_you_page():
    """Thank you page after booking"""
    from app.templates.pages import THANK_YOU_HTML
    return HTMLResponse(THANK_YOU_HTML)
