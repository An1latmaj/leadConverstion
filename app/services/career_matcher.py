import random
from typing import Dict, List, Any
from app.data.quiz_data import CAREER_OPTIONS

class CareerMatcher:
    """Rule-based career matching system that analyzes quiz responses"""
    
    def __init__(self):
        # Define career categories and their associated traits
        self.career_profiles = {
            "Software Engineering": {
                "keywords": ["technology", "learning", "analytical", "problem-solving", "independent"],
                "question_weights": {
                    1: {"Strongly Agree": 3, "Agree": 2, "Neutral": 0, "Disagree": -1, "Strongly Disagree": -2},  # Numbers/data
                    7: {"Strongly Agree": 3, "Agree": 2, "Neutral": 0, "Disagree": -2, "Strongly Disagree": -3},  # Technology
                    2: {"Strongly Agree": 2, "Agree": 1, "Neutral": 0, "Disagree": -1, "Strongly Disagree": -1},  # Independent work
                    23: {"Strongly Agree": 2, "Agree": 1, "Neutral": 0, "Disagree": -1, "Strongly Disagree": -2}, # Continuous learning
                },
                "salary_range": "$75,000-$120,000",
                "description": "Your analytical mindset and love for technology make you perfect for creating software solutions that solve real-world problems."
            },
            "Data Science": {
                "keywords": ["analytical", "research", "numbers", "patterns", "technology"],
                "question_weights": {
                    1: {"Strongly Agree": 3, "Agree": 2, "Neutral": 0, "Disagree": -2, "Strongly Disagree": -3},  # Numbers/data
                    13: {"Strongly Agree": 3, "Agree": 2, "Neutral": 0, "Disagree": -1, "Strongly Disagree": -2}, # Research
                    7: {"Strongly Agree": 2, "Agree": 1, "Neutral": 0, "Disagree": -1, "Strongly Disagree": -2},  # Technology
                    2: {"Strongly Agree": 1, "Agree": 1, "Neutral": 0, "Disagree": 0, "Strongly Disagree": -1},   # Independent
                },
                "salary_range": "$80,000-$130,000",
                "description": "Your passion for uncovering insights from data and analytical thinking make you ideal for transforming raw information into business intelligence."
            },
            "Marketing": {
                "keywords": ["creative", "people", "communication", "persuasion", "dynamic"],
                "question_weights": {
                    5: {"Strongly Agree": 2, "Agree": 1, "Neutral": 0, "Disagree": -1, "Strongly Disagree": -2},   # Speaking groups
                    18: {"Strongly Agree": 3, "Agree": 2, "Neutral": 0, "Disagree": -1, "Strongly Disagree": -2},  # Negotiating
                    10: {"Strongly Agree": 2, "Agree": 1, "Neutral": 0, "Disagree": -1, "Strongly Disagree": -1},  # Writing
                    24: {"Strongly Agree": 2, "Agree": 1, "Neutral": 0, "Disagree": -1, "Strongly Disagree": -1},  # Fast-paced
                },
                "salary_range": "$50,000-$90,000",
                "description": "Your communication skills and creative thinking make you perfect for building brands and connecting with audiences."
            },
            "Sales": {
                "keywords": ["people", "persuasion", "results", "communication", "competitive"],
                "question_weights": {
                    18: {"Strongly Agree": 3, "Agree": 2, "Neutral": 0, "Disagree": -2, "Strongly Disagree": -3},  # Negotiating
                    5: {"Strongly Agree": 2, "Agree": 1, "Neutral": 0, "Disagree": -1, "Strongly Disagree": -2},   # Speaking
                    12: {"Strongly Agree": 2, "Agree": 1, "Neutral": 0, "Disagree": -1, "Strongly Disagree": -1},  # Immediate results
                    16: {"Strongly Agree": 2, "Agree": 1, "Neutral": 0, "Disagree": 0, "Strongly Disagree": -1},   # High earning
                },
                "salary_range": "$45,000-$150,000+ (commission-based)",
                "description": "Your persuasive abilities and results-driven mindset make you ideal for building relationships and driving revenue."
            },
            "Healthcare": {
                "keywords": ["helping", "people", "care", "service", "meaningful"],
                "question_weights": {
                    3: {"Strongly Agree": 3, "Agree": 2, "Neutral": 0, "Disagree": -2, "Strongly Disagree": -3},   # Helping people
                    19: {"Strongly Agree": 2, "Agree": 1, "Neutral": 0, "Disagree": -1, "Strongly Disagree": -1},  # Social causes
                    6: {"Strongly Agree": 1, "Agree": 1, "Neutral": 0, "Disagree": 0, "Strongly Disagree": -1},    # Procedures
                    20: {"Strongly Agree": 2, "Agree": 1, "Neutral": 0, "Disagree": -1, "Strongly Disagree": -2},  # Attention to detail
                },
                "salary_range": "$55,000-$200,000+ (varies by specialty)",
                "description": "Your desire to help others and attention to detail make you perfect for making a meaningful impact on people's lives."
            },
            "Finance": {
                "keywords": ["numbers", "analytical", "planning", "detail", "stability"],
                "question_weights": {
                    1: {"Strongly Agree": 2, "Agree": 1, "Neutral": 0, "Disagree": -1, "Strongly Disagree": -2},   # Numbers
                    14: {"Strongly Agree": 3, "Agree": 2, "Neutral": 0, "Disagree": -2, "Strongly Disagree": -3},  # Budget management
                    20: {"Strongly Agree": 2, "Agree": 1, "Neutral": 0, "Disagree": -1, "Strongly Disagree": -2},  # Detail oriented
                    6: {"Strongly Agree": 1, "Agree": 1, "Neutral": 0, "Disagree": 0, "Strongly Disagree": -1},    # Procedures
                },
                "salary_range": "$60,000-$150,000+",
                "description": "Your analytical skills and attention to financial details make you ideal for managing money and making strategic financial decisions."
            },
            "Design": {
                "keywords": ["creative", "visual", "artistic", "innovation", "aesthetics"],
                "question_weights": {
                    4: {"Strongly Agree": 2, "Agree": 1, "Neutral": 0, "Disagree": -1, "Strongly Disagree": -2},   # Creating things
                    10: {"Strongly Agree": 2, "Agree": 1, "Neutral": 0, "Disagree": -1, "Strongly Disagree": -1},  # Writing/expression
                                    },
                "salary_range": "$45,000-$85,000",
                "description": "Your creative vision and aesthetic sense make you perfect for bringing ideas to life through visual communication."
            },
            "Education": {
                "keywords": ["teaching", "helping", "knowledge", "development", "patience"],
                "question_weights": {
                    15: {"Strongly Agree": 3, "Agree": 2, "Neutral": 0, "Disagree": -2, "Strongly Disagree": -3},  # Teaching
                    3: {"Strongly Agree": 2, "Agree": 1, "Neutral": 0, "Disagree": -1, "Strongly Disagree": -2},   # Helping people
                    23: {"Strongly Agree": 2, "Agree": 1, "Neutral": 0, "Disagree": -1, "Strongly Disagree": -1},  # Learning
                    19: {"Strongly Agree": 1, "Agree": 1, "Neutral": 0, "Disagree": 0, "Strongly Disagree": -1},   # Social causes
                },
                "salary_range": "$40,000-$70,000",
                "description": "Your passion for sharing knowledge and helping others grow makes you ideal for shaping the next generation."
            },
            "Consulting": {
                "keywords": ["problem-solving", "analytical", "communication", "advisory", "strategic"],
                "question_weights": {
                    21: {"Strongly Agree": 2, "Agree": 1, "Neutral": 0, "Disagree": -1, "Strongly Disagree": -2},  # Leadership
                    1: {"Strongly Agree": 2, "Agree": 1, "Neutral": 0, "Disagree": -1, "Strongly Disagree": -1},   # Analytical
                    5: {"Strongly Agree": 2, "Agree": 1, "Neutral": 0, "Disagree": -1, "Strongly Disagree": -2},   # Speaking
                    9: {"Strongly Agree": 1, "Agree": 1, "Neutral": 0, "Disagree": 0, "Strongly Disagree": -1},    # Travel
                },
                "salary_range": "$70,000-$200,000+",
                "description": "Your strategic thinking and problem-solving abilities make you perfect for advising organizations on complex challenges."
            },
            "Human Resources": {
                "keywords": ["people", "empathy", "communication", "organization", "development"],
                "question_weights": {
                    3: {"Strongly Agree": 2, "Agree": 1, "Neutral": 0, "Disagree": -1, "Strongly Disagree": -2},   # Helping people
                    8: {"Strongly Agree": 2, "Agree": 1, "Neutral": 0, "Disagree": -1, "Strongly Disagree": -2},   # Organizing events
                    15: {"Strongly Agree": 1, "Agree": 1, "Neutral": 0, "Disagree": 0, "Strongly Disagree": -1},   # Teaching/training
                    6: {"Strongly Agree": 1, "Agree": 1, "Neutral": 0, "Disagree": 0, "Strongly Disagree": -1},    # Procedures
                },
                "salary_range": "$50,000-$95,000",
                "description": "Your people skills and organizational abilities make you ideal for developing talent and building positive workplace cultures."
            }
        }
    
    def calculate_career_scores(self, answers: Dict[str, Any], excluded_careers: List[str] = None) -> List[Dict]:
        """Calculate compatibility scores for each career based on quiz answers"""
        if excluded_careers is None:
            excluded_careers = []
        
        career_scores = []
        
        for career, profile in self.career_profiles.items():
            # Skip excluded careers
            if career in excluded_careers:
                continue
                
            score = 0
            question_count = 0
            
            # Calculate weighted score based on relevant questions
            for question_id, weights in profile["question_weights"].items():
                answer_key = str(question_id)
                if answer_key in answers:
                    answer = answers[answer_key]
                    if answer in weights:
                        score += weights[answer]
                        question_count += 1
            
            # Normalize score
            if question_count > 0:
                normalized_score = score / question_count
            else:
                normalized_score = 0
            
            # Add some randomization to make results feel more personalized
            randomization = random.uniform(-0.3, 0.3)
            final_score = normalized_score + randomization
            
            career_scores.append({
                "career": career,
                "score": final_score,
                "salary_range": profile["salary_range"],
                "description": profile["description"]
            })
        
        # Sort by score (highest first)
        career_scores.sort(key=lambda x: x["score"], reverse=True)
        
        return career_scores
    
    def generate_career_preview(self, answers: Dict[str, Any], excluded_careers: List[str] = None) -> str:
        """Generate a career preview with one revealed career and paywalled content"""
        career_scores = self.calculate_career_scores(answers, excluded_careers)
        
        if not career_scores:
            # Fallback if all careers are excluded
            return self._get_fallback_preview()
        
        # Get the top career match
        top_career = career_scores[0]
        
        # Generate preview HTML
        preview_html = f"""
        <div style="background: linear-gradient(135deg, #e8f5e8, #f0fff0); padding: 20px; border-radius: 12px; border-left: 4px solid #48bb78;">
            <h3 style="color: #2f855a; margin-bottom: 15px;">🎯 Your #1 Career Match:</h3>
            <div style="font-size: 1.05rem; line-height: 1.6; color: #2d3748;">
                <strong>{top_career['career']}</strong> - {top_career['description']} Expected salary: {top_career['salary_range']}.
            </div>
        </div>
        
        <div style="margin-top: 20px; padding: 20px; background: linear-gradient(135deg, #fff5f5, #fed7d7); border-radius: 12px; border-left: 4px solid #e53e3e;">
            <h4 style="color: #c53030; margin-bottom: 10px;">🔒 Premium Analysis Includes:</h4>
            <ul style="color: #4a5568; margin: 10px 0; padding-left: 20px;">
                <li><strong>2 Additional Perfect Matches</strong> - {self._get_other_careers_hint(career_scores[1:3])}</li>
                <li><strong>Exact Salary Ranges</strong> - What you should earn in each role</li>
                <li><strong>Skill Gap Analysis</strong> - What to learn for a seamless transition</li>
                <li><strong>90-Day Action Plan</strong> - Step-by-step roadmap to your new career</li>
                <li><strong>Hidden Opportunities</strong> - Emerging roles you never considered</li>
            </ul>
            <div style="text-align: center; margin-top: 15px; font-weight: bold; color: #c53030;">
                💎 Complete your profile below to unlock everything →
            </div>
        </div>
        """
        
        return preview_html
    
    def _get_other_careers_hint(self, other_careers: List[Dict]) -> str:
        """Generate a hint about other career matches"""
        if len(other_careers) >= 2:
            career_names = [career['career'] for career in other_careers[:2]]
            return f"Including {career_names[0]} and {career_names[1]}"
        elif len(other_careers) == 1:
            return f"Including {other_careers[0]['career']} and more"
        else:
            return "High-growth careers tailored to your profile"
    
    def _get_fallback_preview(self) -> str:
        """Fallback preview when no careers match or all are excluded"""
        return """
        <div style="background: linear-gradient(135deg, #e8f5e8, #f0fff0); padding: 20px; border-radius: 12px; border-left: 4px solid #48bb78;">
            <h3 style="color: #2f855a; margin-bottom: 15px;">🎯 Your Career Profile:</h3>
            <div style="font-size: 1.05rem; line-height: 1.6; color: #2d3748;">
                Based on your unique preferences, we've identified several non-traditional career paths that might be perfect for you. These include emerging roles in growing industries.
            </div>
        </div>
        
        <div style="margin-top: 20px; padding: 20px; background: linear-gradient(135deg, #fff5f5, #fed7d7); border-radius: 12px; border-left: 4px solid #e53e3e;">
            <h4 style="color: #c53030; margin-bottom: 10px;">🔒 Complete Analysis Includes:</h4>
            <ul style="color: #4a5568; margin: 10px 0; padding-left: 20px;">
                <li><strong>3 Custom Career Matches</strong> - Tailored to your specific preferences</li>
                <li><strong>Industry Growth Projections</strong> - Which fields are expanding</li>
                <li><strong>Skills Assessment</strong> - Your strengths and development areas</li>
                <li><strong>Transition Strategy</strong> - How to pivot to your ideal role</li>
            </ul>
            <div style="text-align: center; margin-top: 15px; font-weight: bold; color: #c53030;">
                💎 Enter your details below to see your matches →
            </div>
        </div>
        """

# Global instance
career_matcher = CareerMatcher()
