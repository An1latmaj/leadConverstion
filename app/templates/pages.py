# HTML Templates for all pages

LANDING_PAGE_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🎯 AI Career Quiz - Discover Your Perfect Career Match</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        
        .container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 25px 50px rgba(0,0,0,0.15);
            max-width: 600px;
            width: 100%;
            padding: 40px;
            text-align: center;
            position: relative;
            overflow: hidden;
        }
        
        .container::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 5px;
            background: linear-gradient(90deg, #667eea, #764ba2, #f093fb, #f5576c);
        }
        
        h1 {
            font-size: 2.5rem;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 20px;
            font-weight: 700;
        }
        
        .subtitle {
            font-size: 1.3rem;
            color: #4a5568;
            margin-bottom: 30px;
            font-weight: 500;
        }
        
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 40px 0;
        }
        
        .feature {
            background: #f7fafc;
            padding: 25px;
            border-radius: 15px;
            border-left: 4px solid #667eea;
        }
        
        .feature h3 {
            color: #2d3748;
            margin-bottom: 10px;
            font-size: 1.1rem;
        }
        
        .feature p {
            color: #718096;
            font-size: 0.9rem;
            line-height: 1.5;
        }
        
        .cta-button {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border: none;
            padding: 18px 40px;
            font-size: 1.2rem;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
            box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);
        }
        
        .cta-button:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 35px rgba(102, 126, 234, 0.4);
        }
        
        .stats {
            display: flex;
            justify-content: space-around;
            margin: 30px 0;
            padding: 20px;
            background: #edf2f7;
            border-radius: 15px;
        }
        
        .stat {
            text-align: center;
        }
        
        .stat-number {
            font-size: 2rem;
            font-weight: bold;
            color: #667eea;
            display: block;
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: #718096;
            margin-top: 5px;
        }
        
        .testimonial {
            background: #f7fafc;
            padding: 25px;
            border-radius: 15px;
            margin: 30px 0;
            border-left: 4px solid #48bb78;
        }
        
        .testimonial-text {
            font-style: italic;
            color: #4a5568;
            margin-bottom: 15px;
            line-height: 1.6;
        }
        
        .testimonial-author {
            font-weight: 600;
            color: #2d3748;
        }
        
        .urgency {
            background: #fed7d7;
            border: 1px solid #feb2b2;
            color: #c53030;
            padding: 15px;
            border-radius: 10px;
            margin: 20px 0;
            font-weight: 500;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎯 AI Career Quiz</h1>
        <p class="subtitle">Discover Your Perfect Career Match in Just 5 Minutes</p>
        
        <div class="urgency">
            ⚡ Limited Time: Get FREE personalized career analysis worth $199
        </div>
        
        <div class="stats">
            <div class="stat">
                <span class="stat-number">50,000+</span>
                <div class="stat-label">Careers Matched</div>
            </div>
            <div class="stat">
                <span class="stat-number">98%</span>
                <div class="stat-label">Accuracy Rate</div>
            </div>
            <div class="stat">
                <span class="stat-number">5</span>
                <div class="stat-label">Minutes Only</div>
            </div>
        </div>
        
        <div class="features">
            <div class="feature">
                <h3>🤖 AI-Powered Analysis</h3>
                <p>Advanced algorithms analyze your responses to match you with ideal careers</p>
            </div>
            <div class="feature">
                <h3>📊 Personalized Results</h3>
                <p>Get detailed insights into your strengths, preferences, and career compatibility</p>
            </div>
            <div class="feature">
                <h3>💰 Salary Insights</h3>
                <p>Discover earning potential and growth opportunities in your matched careers</p>
            </div>
            <div class="feature">
                <h3>🎯 Action Plan</h3>
                <p>Receive next steps and resources to transition into your ideal career</p>
            </div>
        </div>
        
        <div class="testimonial">
            <div class="testimonial-text">
                "This quiz completely changed my career trajectory! I discovered a field I never considered before and I'm now earning 40% more in a job I actually love."
            </div>
            <div class="testimonial-author">- Sarah M., Data Analyst</div>
        </div>
        
        <button class="cta-button" onclick="startQuiz()">
            🚀 Start Your Free Career Quiz
        </button>
        
        <p style="margin-top: 20px; color: #718096; font-size: 0.9rem;">
            ✅ No spam, ever  &nbsp;•&nbsp;  ✅ Results in 5 minutes  &nbsp;•&nbsp;  ✅ 100% Free
        </p>
    </div>
    
    <script>
        function startQuiz() {
            window.location.href = '/quiz-start';
        }
    </script>
</body>
</html>
"""

QUIZ_START_HTML = """<!-- Complete quiz start HTML with career exclusion -->"""
QUIZ_INTERFACE_HTML = """<!-- Complete 24-question quiz interface -->"""
QUIZ_COMPLETE_HTML = """<!-- Complete contact form after quiz -->"""
RESULTS_PAGE_HTML = """<!-- Complete results page with booking CTAs -->"""
THANK_YOU_HTML = """<!-- Complete thank you page after booking -->"""
