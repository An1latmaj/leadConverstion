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

QUIZ_START_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🎯 Career Quiz - Step 1: Exclude Careers</title>
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
            max-width: 800px;
            width: 100%;
            padding: 40px;
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
        
        .progress-bar {
            background: #e2e8f0;
            height: 8px;
            border-radius: 4px;
            margin-bottom: 30px;
            overflow: hidden;
        }
        
        .progress-fill {
            background: linear-gradient(90deg, #667eea, #764ba2);
            height: 100%;
            width: 20%;
            transition: width 0.3s ease;
        }
        
        h1 {
            font-size: 2.2rem;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 15px;
            font-weight: 700;
            text-align: center;
        }
        
        .subtitle {
            font-size: 1.1rem;
            color: #4a5568;
            margin-bottom: 30px;
            text-align: center;
            line-height: 1.6;
        }
        
        .careers-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin: 30px 0;
        }
        
        .career-option {
            background: #f7fafc;
            border: 2px solid #e2e8f0;
            border-radius: 12px;
            padding: 15px;
            cursor: pointer;
            transition: all 0.3s ease;
            text-align: center;
            font-weight: 500;
            color: #2d3748;
        }
        
        .career-option:hover {
            border-color: #667eea;
            background: #edf2f7;
            transform: translateY(-2px);
        }
        
        .career-option.excluded {
            background: #fed7d7;
            border-color: #fc8181;
            color: #c53030;
        }
        
        .career-option.excluded::after {
            content: " ❌";
            margin-left: 5px;
        }
        
        .button-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 40px;
            gap: 20px;
        }
        
        .back-button {
            background: #e2e8f0;
            color: #4a5568;
            border: none;
            padding: 12px 25px;
            border-radius: 30px;
            cursor: pointer;
            font-weight: 500;
            transition: all 0.3s ease;
        }
        
        .back-button:hover {
            background: #cbd5e0;
        }
        
        .continue-button {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border: none;
            padding: 15px 35px;
            font-size: 1.1rem;
            border-radius: 30px;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);
        }
        
        .continue-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 15px 35px rgba(102, 126, 234, 0.4);
        }
        
        .continue-button:disabled {
            opacity: 0.6;
            cursor: not-allowed;
            transform: none;
        }
        
        .info-box {
            background: #e6fffa;
            border: 1px solid #81e6d9;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 25px;
        }
        
        .info-box h3 {
            color: #234e52;
            margin-bottom: 10px;
            font-size: 1.1rem;
        }
        
        .info-box p {
            color: #2d3748;
            line-height: 1.5;
        }
        
        .selection-counter {
            background: #667eea;
            color: white;
            padding: 8px 15px;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: 500;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="progress-bar">
            <div class="progress-fill"></div>
        </div>
        
        <h1>🎯 Step 1: Career Preferences</h1>
        <p class="subtitle">
            Let's start by excluding any careers you're definitely NOT interested in. 
            This helps us focus on what truly matches your interests.
        </p>
        
        <div class="info-box">
            <h3>💡 Why This Matters</h3>
            <p>By eliminating careers that don't appeal to you, we can provide more accurate and relevant recommendations that align with your true interests and goals.</p>
        </div>
        
        <p style="font-weight: 600; color: #4a5568; margin-bottom: 20px;">
            Click on any careers you want to EXCLUDE from your results:
        </p>
        
        <div class="careers-grid" id="careersGrid">
            <!-- Career options will be loaded here -->
        </div>
        
        <div class="button-container">
            <div>
                <button class="back-button" onclick="goBack()">← Back to Home</button>
            </div>
            <div style="display: flex; align-items: center; gap: 15px;">
                <span class="selection-counter" id="selectionCounter">0 excluded</span>
                <button class="continue-button" onclick="startQuiz()">Continue to Quiz →</button>
            </div>
        </div>
    </div>

    <script>
        let excludedCareers = [];
        
        const careerOptions = [
            "Software Engineering", "Data Science", "Marketing", "Sales", "Finance", "Healthcare",
            "Education", "Law", "Consulting", "Design", "Human Resources", "Operations",
            "Research", "Entrepreneurship", "Media & Communications", "Government", "Non-profit",
            "Real Estate", "Manufacturing", "Retail", "Construction", "Agriculture", "Transportation",
            "Entertainment", "Sports", "Hospitality", "Beauty & Wellness", "Art & Culture"
        ];

        function initializePage() {
            const careersGrid = document.getElementById('careersGrid');
            
            careerOptions.forEach(career => {
                const careerDiv = document.createElement('div');
                careerDiv.className = 'career-option';
                careerDiv.textContent = career;
                careerDiv.onclick = () => toggleCareer(career, careerDiv);
                careersGrid.appendChild(careerDiv);
            });
            
            updateCounter();
        }

        function toggleCareer(career, element) {
            if (excludedCareers.includes(career)) {
                excludedCareers = excludedCareers.filter(c => c !== career);
                element.classList.remove('excluded');
            } else {
                excludedCareers.push(career);
                element.classList.add('excluded');
            }
            updateCounter();
        }

        function updateCounter() {
            const counter = document.getElementById('selectionCounter');
            const count = excludedCareers.length;
            counter.textContent = count === 0 ? 'None excluded' : `${count} excluded`;
        }

        function goBack() {
            window.location.href = '/';
        }

        function startQuiz() {
            // Store excluded careers in session storage
            sessionStorage.setItem('excludedCareers', JSON.stringify(excludedCareers));
            window.location.href = '/quiz';
        }

        // Initialize the page when loaded
        document.addEventListener('DOMContentLoaded', initializePage);
    </script>
</body>
</html>
"""

QUIZ_INTERFACE_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🎯 Career Quiz - Discover Your Perfect Match</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .quiz-container {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 25px 50px rgba(0,0,0,0.15);
            overflow: hidden;
        }
        
        .quiz-header {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 30px;
            text-align: center;
        }
        
        .quiz-progress {
            background: rgba(255,255,255,0.1);
            height: 8px;
            border-radius: 4px;
            margin: 20px 0;
            overflow: hidden;
        }
        
        .progress-bar {
            background: white;
            height: 100%;
            width: 0%;
            border-radius: 4px;
            transition: width 0.3s ease;
        }
        
        .quiz-content {
            padding: 40px;
        }
        
        .question-card {
            background: #f8f9fa;
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 30px;
            border-left: 5px solid #667eea;
        }
        
        .question-number {
            color: #667eea;
            font-weight: bold;
            font-size: 0.9rem;
            margin-bottom: 10px;
        }
        
        .question-text {
            font-size: 1.3rem;
            color: #2d3748;
            margin-bottom: 25px;
            line-height: 1.4;
        }
        
        .options-grid {
            display: grid;
            gap: 15px;
        }
        
        .option-button {
            background: white;
            border: 2px solid #e2e8f0;
            border-radius: 12px;
            padding: 15px 20px;
            cursor: pointer;
            transition: all 0.3s ease;
            text-align: left;
            font-size: 1rem;
        }
        
        .option-button:hover {
            border-color: #667eea;
            background: #f7fafc;
        }
        
        .option-button.selected {
            border-color: #667eea;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
        }
        
        .navigation-buttons {
            display: flex;
            justify-content: space-between;
            margin-top: 30px;
        }
        
        .nav-button {
            padding: 12px 30px;
            border-radius: 25px;
            border: none;
            cursor: pointer;
            font-size: 1rem;
            transition: all 0.3s ease;
        }
        
        .prev-button {
            background: #e2e8f0;
            color: #4a5568;
        }
        
        .next-button {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
        }
        
        .nav-button:disabled {
            opacity: 0.5;
            cursor: not-allowed;
        }
        
        .loading {
            text-align: center;
            padding: 40px;
            color: #667eea;
        }
    </style>
</head>
<body>
    <div class="quiz-container">
        <div class="quiz-header">
            <h1>🎯 Career Discovery Quiz</h1>
            <p>Answer 24 questions to discover your ideal career path</p>
            <div class="quiz-progress">
                <div class="progress-bar" id="progressBar"></div>
            </div>
            <div id="progressText">Question 1 of 24</div>
        </div>
        
        <div class="quiz-content">
            <div id="loadingMessage" class="loading">
                <p>Loading quiz questions...</p>
            </div>
            
            <div id="quizContent" style="display: none;">
                <div class="question-card">
                    <div class="question-number" id="questionNumber">Question 1 of 24</div>
                    <div class="question-text" id="questionText"></div>
                    <div class="options-grid" id="optionsContainer"></div>
                </div>
                
                <div class="navigation-buttons">
                    <button class="nav-button prev-button" id="prevButton" onclick="goToPrevious()">Previous</button>
                    <button class="nav-button next-button" id="nextButton" onclick="goToNext()">Next</button>
                </div>
            </div>
        </div>
    </div>

    <script>
        let quizData = [];
        let currentQuestion = 0;
        let answers = {};
        
        // Load quiz data
        async function loadQuiz() {
            try {
                const response = await fetch('/api/quiz/start');
                const data = await response.json();
                quizData = data.quiz_questions;
                
                document.getElementById('loadingMessage').style.display = 'none';
                document.getElementById('quizContent').style.display = 'block';
                
                displayQuestion();
            } catch (error) {
                console.error('Error loading quiz:', error);
                document.getElementById('loadingMessage').innerHTML = '<p>Error loading quiz. Please refresh the page.</p>';
            }
        }
        
        // Display current question
        function displayQuestion() {
            const question = quizData[currentQuestion];
            
            document.getElementById('questionNumber').textContent = `Question ${currentQuestion + 1} of ${quizData.length}`;
            document.getElementById('questionText').textContent = question.q;
            document.getElementById('progressText').textContent = `Question ${currentQuestion + 1} of ${quizData.length}`;
            
            // Update progress bar
            const progress = ((currentQuestion + 1) / quizData.length) * 100;
            document.getElementById('progressBar').style.width = progress + '%';
            
            // Display options
            const optionsContainer = document.getElementById('optionsContainer');
            optionsContainer.innerHTML = '';
            
            question.options.forEach((option, index) => {
                const button = document.createElement('button');
                button.className = 'option-button';
                button.textContent = option;
                button.onclick = () => selectOption(index, option);
                
                // Mark as selected if already answered
                if (answers[question.id] === option) {
                    button.classList.add('selected');
                }
                
                optionsContainer.appendChild(button);
            });
            
            // Update navigation buttons
            document.getElementById('prevButton').disabled = currentQuestion === 0;
            document.getElementById('nextButton').disabled = !answers[question.id];
        }
        
        // Select an option
        function selectOption(index, option) {
            const question = quizData[currentQuestion];
            answers[question.id] = option;
            
            // Update UI
            document.querySelectorAll('.option-button').forEach(btn => btn.classList.remove('selected'));
            document.querySelectorAll('.option-button')[index].classList.add('selected');
            
            // Enable next button
            document.getElementById('nextButton').disabled = false;
        }
        
        // Navigation functions
        function goToPrevious() {
            if (currentQuestion > 0) {
                currentQuestion--;
                displayQuestion();
            }
        }
        
        function goToNext() {
            if (currentQuestion < quizData.length - 1) {
                currentQuestion++;
                displayQuestion();
            } else {
                // Quiz complete
                submitQuiz();
            }
        }
        
        // Submit quiz
        async function submitQuiz() {
            try {
                const response = await fetch('/api/submit-answers', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        answers: answers,
                        exclude_careers: []
                    })
                });
                
                const result = await response.json();
                
                // Redirect to results page with session ID
                window.location.href = `/quiz-complete?session_id=${result.session_id}`;
                
            } catch (error) {
                console.error('Error submitting quiz:', error);
                alert('Error submitting quiz. Please try again.');
            }
        }
        
        // Initialize quiz on page load
        window.onload = loadQuiz;
    </script>
</body>
</html>
"""

QUIZ_COMPLETE_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🎯 Your Career Analysis is Ready!</title>
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
            max-width: 700px;
            width: 100%;
            padding: 40px;
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
        
        .success-header {
            text-align: center;
            margin-bottom: 30px;
        }
        
        .success-icon {
            font-size: 4rem;
            margin-bottom: 15px;
            animation: bounce 2s infinite;
        }
        
        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
            40% { transform: translateY(-10px); }
            60% { transform: translateY(-5px); }
        }
        
        h1 {
            font-size: 2.4rem;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
            font-weight: 700;
        }
        
        .subtitle {
            font-size: 1.2rem;
            color: #4a5568;
            margin-bottom: 25px;
            line-height: 1.5;
        }
        
        .urgency-banner {
            background: linear-gradient(135deg, #ff6b6b, #ee5a24);
            color: white;
            padding: 15px 20px;
            border-radius: 12px;
            text-align: center;
            margin-bottom: 25px;
            font-weight: bold;
            position: relative;
            overflow: hidden;
        }
        
        .urgency-banner::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
            animation: shimmer 3s infinite;
        }
        
        @keyframes shimmer {
            0% { left: -100%; }
            100% { left: 100%; }
        }
        
        .countdown {
            font-size: 1.1rem;
            color: #ffeb3b;
            margin-top: 5px;
        }
        
        .preview-section {
            background: linear-gradient(135deg, #e8f5e8, #f0fff0);
            border: 2px solid #48bb78;
            border-radius: 15px;
            padding: 25px;
            margin: 25px 0;
            position: relative;
        }
        
        .preview-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 15px;
        }
        
        .preview-title {
            color: #2f855a;
            font-weight: bold;
            font-size: 1.2rem;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .accuracy-badge {
            background: #48bb78;
            color: white;
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: bold;
        }
        
        .preview-content {
            color: #2d3748;
            line-height: 1.7;
            min-height: 80px;
            font-size: 1.05rem;
        }
        
        .loading-preview {
            color: #667eea;
            font-style: italic;
            text-align: center;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
        }
        
        .teaser-overlay {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            height: 60px;
            background: linear-gradient(transparent, rgba(255,255,255,0.95));
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            color: #667eea;
            border-radius: 0 0 15px 15px;
        }
        
        .value-props {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }
        
        .value-prop {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 12px;
            border-left: 4px solid #667eea;
            transition: transform 0.3s ease;
        }
        
        .value-prop:hover {
            transform: translateY(-3px);
        }
        
        .value-prop h3 {
            color: #2d3748;
            margin-bottom: 10px;
            font-size: 1.1rem;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .value-prop p {
            color: #4a5568;
            font-size: 0.95rem;
            line-height: 1.5;
        }
        
        .social-proof {
            background: #edf2f7;
            border-radius: 12px;
            padding: 20px;
            margin: 25px 0;
            text-align: center;
        }
        
        .stats-row {
            display: flex;
            justify-content: space-around;
            margin: 15px 0;
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
            font-size: 0.85rem;
            color: #718096;
            margin-top: 5px;
        }
        
        .form-container {
            background: linear-gradient(135deg, #f7fafc, #edf2f7);
            border: 2px solid #e2e8f0;
            border-radius: 15px;
            padding: 30px;
            margin: 30px 0;
            position: relative;
        }
        
        .form-header {
            text-align: center;
            margin-bottom: 25px;
        }
        
        .form-header h2 {
            color: #2d3748;
            margin-bottom: 10px;
            font-size: 1.4rem;
        }
        
        .form-header p {
            color: #4a5568;
            font-size: 0.95rem;
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        .form-label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: #2d3748;
        }
        
        .form-input {
            width: 100%;
            padding: 14px 16px;
            border: 2px solid #e2e8f0;
            border-radius: 10px;
            font-size: 1rem;
            transition: all 0.3s ease;
            background: white;
        }
        
        .form-input:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.1);
        }
        
        .form-input.error {
            border-color: #e53e3e;
            background-color: #fed7d7;
        }
        
        .error-message {
            color: #e53e3e;
            font-size: 0.875rem;
            margin-top: 5px;
        }
        
        .submit-button {
            background: linear-gradient(135deg, #48bb78, #38a169);
            color: white;
            border: none;
            padding: 18px 40px;
            font-size: 1.2rem;
            border-radius: 30px;
            cursor: pointer;
            font-weight: 700;
            transition: all 0.3s ease;
            box-shadow: 0 10px 25px rgba(72, 187, 120, 0.3);
            width: 100%;
            position: relative;
            overflow: hidden;
        }
        
        .submit-button::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
            transition: left 0.5s;
        }
        
        .submit-button:hover::before {
            left: 100%;
        }
        
        .submit-button:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 40px rgba(72, 187, 120, 0.4);
        }
        
        .submit-button:disabled {
            opacity: 0.6;
            cursor: not-allowed;
            transform: none;
        }
        
        .guarantee {
            background: #fff5b2;
            border: 2px solid #f6e05e;
            border-radius: 12px;
            padding: 20px;
            margin: 25px 0;
            text-align: center;
        }
        
        .guarantee h3 {
            color: #744210;
            margin-bottom: 10px;
            font-size: 1.1rem;
        }
        
        .guarantee p {
            color: #744210;
            font-size: 0.95rem;
            line-height: 1.5;
        }
        
        .trust-signals {
            display: flex;
            justify-content: center;
            gap: 30px;
            margin: 20px 0;
            flex-wrap: wrap;
        }
        
        .trust-signal {
            display: flex;
            align-items: center;
            gap: 8px;
            color: #4a5568;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="success-header">
            <div class="success-icon">🎯</div>
            <h1>Your Career DNA is Decoded!</h1>
            <p class="subtitle">
                Based on your 24 responses, we've identified your unique career compatibility profile
            </p>
        </div>
        
        <div class="urgency-banner">
            ⚡ LIMITED TIME: Your personalized analysis expires in <span class="countdown" id="countdown">14:59</span>
            <br>Get instant access before it's gone forever!
        </div>
        
        <div class="preview-section">
            <div class="preview-header">
                <div class="preview-title">
                    🔮 Your Career Preview
                </div>
                <div class="accuracy-badge">98.7% Accurate</div>
            </div>
            <div class="preview-content" id="previewContent">
                <div class="loading-preview">
                    <span>🧠</span> AI analyzing your responses...
                </div>
            </div>
            <div class="teaser-overlay">
                🔒 Unlock full analysis below ↓
            </div>
        </div>
        
        <div class="social-proof">
            <h3 style="color: #2d3748; margin-bottom: 15px;">Join 50,000+ Professionals Who Found Their Dream Career</h3>
            <div class="stats-row">
                <div class="stat">
                    <span class="stat-number">2,847</span>
                    <div class="stat-label">Career Changes This Month</div>
                </div>
                <div class="stat">
                    <span class="stat-number">40%</span>
                    <div class="stat-label">Average Salary Increase</div>
                </div>
                <div class="stat">
                    <span class="stat-number">94%</span>
                    <div class="stat-label">Success Rate</div>
                </div>
            </div>
        </div>
        
        <div class="value-props">
            <div class="value-prop">
                <h3>💰 Salary Optimization Report</h3>
                <p>Discover exactly how much you should be earning in your ideal role, plus negotiation strategies to get there.</p>
            </div>
            <div class="value-prop">
                <h3>🗺️ 90-Day Action Plan</h3>
                <p>Step-by-step roadmap with specific milestones, skill development priorities, and timeline to transition.</p>
            </div>
            <div class="value-prop">
                <h3>🎯 Hidden Career Matches</h3>
                <p>Uncover high-growth careers you never considered that perfectly align with your personality and skills.</p>
            </div>
            <div class="value-prop">
                <h3>🔥 Market Timing Intel</h3>
                <p>Real-time insights on which industries are hiring now and projected growth for the next 5 years.</p>
            </div>
        </div>
        
        <form class="form-container" id="contactForm" onsubmit="submitForm(event)">
            <div class="form-header">
                <h2>🚀 Unlock Your Complete Career Blueprint</h2>
                <p>Enter your details to receive your full analysis + free 30-minute strategy session</p>
            </div>
            
            <div class="form-group">
                <label class="form-label" for="name">Full Name *</label>
                <input type="text" id="name" name="name" class="form-input" placeholder="Your full name" required>
                <div class="error-message" id="nameError"></div>
            </div>
            
            <div class="form-group">
                <label class="form-label" for="email">Email Address *</label>
                <input type="email" id="email" name="email" class="form-input" placeholder="your.email@example.com" required>
                <div class="error-message" id="emailError"></div>
            </div>
            
            <div class="form-group">
                <label class="form-label" for="phone">Phone Number</label>
                <input type="tel" id="phone" name="phone" class="form-input" placeholder="+1 (555) 123-4567">
                <div class="error-message" id="phoneError"></div>
            </div>
            
            <div class="form-group">
                <label class="form-label" for="preferredTime">Best Time for Your Strategy Call</label>
                <select id="preferredTime" name="preferredTime" class="form-input">
                    <option value="">Choose your preferred time</option>
                    <option value="morning">Morning (9 AM - 12 PM)</option>
                    <option value="afternoon">Afternoon (12 PM - 5 PM)</option>
                    <option value="evening">Evening (5 PM - 8 PM)</option>
                    <option value="weekend">Weekend</option>
                    <option value="flexible">I'm flexible</option>
                </select>
            </div>
            
            <button type="submit" class="submit-button" id="submitButton">
                🎯 GET MY CAREER BLUEPRINT + FREE STRATEGY CALL
            </button>
        </form>
        
        <div class="guarantee">
            <h3>💎 100% Satisfaction Guarantee</h3>
            <p>If you're not completely satisfied with your career analysis and strategy session, we'll work with you until you are - or your money back.</p>
        </div>
        
        <div class="trust-signals">
            <div class="trust-signal">
                <span>🔒</span> SSL Encrypted
            </div>
            <div class="trust-signal">
                <span>✅</span> No Spam Policy
            </div>
            <div class="trust-signal">
                <span>⚡</span> Instant Access
            </div>
            <div class="trust-signal">
                <span>🎁</span> 100% Free
            </div>
        </div>
    </div>

    <script>
        let sessionId = '';
        
        // Countdown timer
        function startCountdown() {
            let timeLeft = 15 * 60; // 15 minutes in seconds
            
            const timer = setInterval(() => {
                const minutes = Math.floor(timeLeft / 60);
                const seconds = timeLeft % 60;
                
                document.getElementById('countdown').textContent = 
                    `${minutes}:${seconds.toString().padStart(2, '0')}`;
                
                if (timeLeft <= 0) {
                    clearInterval(timer);
                    document.getElementById('countdown').textContent = '0:00';
                }
                
                timeLeft--;
            }, 1000);
        }
        
        // Get session ID from URL
        function getSessionId() {
            const urlParams = new URLSearchParams(window.location.search);
            sessionId = urlParams.get('session_id');
            
            if (!sessionId) {
                document.getElementById('previewContent').innerHTML = 
                    '<div style="color: #e53e3e;">⚠️ Session expired. Please retake the quiz to get your analysis.</div>';
                return;
            }
            
            // Generate preview
            generatePreview();
        }
        
        // Generate AI preview
        async function generatePreview() {
            try {
                const response = await fetch('/api/generate-preview', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ session_id: sessionId })
                });
                
                const data = await response.json();
                
                if (data.error) {
                    document.getElementById('previewContent').innerHTML = 
                        `<div style="color: #e53e3e;">⚠️ ${data.error}</div>`;
                } else {
                    // Display the full AI-generated preview with paywall
                    document.getElementById('previewContent').innerHTML = data.ai_preview || `
                        <div style="background: rgba(102, 126, 234, 0.1); padding: 20px; border-radius: 8px; text-align: center;">
                            <strong>🎯 Your Analysis is Ready!</strong><br>
                            We've identified your top career matches, salary potential, and growth opportunities. 
                            Complete the form below to access your full report.
                        </div>`;
                }
            } catch (error) {
                console.error('Error generating preview:', error);
                document.getElementById('previewContent').innerHTML = 
                    `<div style="background: linear-gradient(135deg, #e8f5e8, #f0fff0); padding: 20px; border-radius: 12px; border-left: 4px solid #48bb78;">
                        <h3 style="color: #2f855a; margin-bottom: 15px;">🎯 Your #1 Career Match:</h3>
                        <div style="font-size: 1.05rem; line-height: 1.6; color: #2d3748;">
                            <strong>Data Analyst</strong> - Your analytical thinking and problem-solving skills make you perfect for transforming data into insights. Expected salary: $65,000-$85,000.
                        </div>
                    </div>
                    
                    <div style="margin-top: 20px; padding: 20px; background: linear-gradient(135deg, #fff5f5, #fed7d7); border-radius: 12px; border-left: 4px solid #e53e3e;">
                        <h4 style="color: #c53030; margin-bottom: 10px;">🔒 Complete Analysis Includes:</h4>
                        <ul style="color: #4a5568; margin: 10px 0; padding-left: 20px;">
                            <li><strong>2 Additional Perfect Matches</strong></li>
                            <li><strong>Exact Salary Ranges</strong></li>
                            <li><strong>90-Day Action Plan</strong></li>
                        </ul>
                        <div style="text-align: center; margin-top: 15px; font-weight: bold; color: #c53030;">
                            💎 Enter your details below to unlock →
                        </div>
                    </div>`;
            }
        }
        
        // Submit contact form
        async function submitForm(event) {
            event.preventDefault();
            
            // Clear previous errors
            clearErrors();
            
            // Get form data
            const formData = new FormData(event.target);
            const contactData = {
                session_id: sessionId,
                name: formData.get('name').trim(),
                email: formData.get('email').trim(),
                phone: formData.get('phone').trim(),
                preferred_time: formData.get('preferredTime'),
                message: `Career consultation request from quiz completion. High-intent lead with completed 24-question assessment.`
            };
            
            // Validate
            if (!validateForm(contactData)) {
                return;
            }
            
            // Disable submit button
            const submitButton = document.getElementById('submitButton');
            submitButton.disabled = true;
            submitButton.textContent = '🚀 PROCESSING YOUR BLUEPRINT...';
            
            try {
                const response = await fetch('/api/book-consultation', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(contactData)
                });
                
                const result = await response.json();
                
                if (result.success) {
                    // Redirect to results/thank you page
                    window.location.href = `/results?session_id=${sessionId}&booking_id=${result.booking_id}`;
                } else {
                    throw new Error(result.message || 'Booking failed');
                }
            } catch (error) {
                console.error('Error submitting form:', error);
                alert('Oops! Something went wrong. Please try again or contact support.');
                
                // Re-enable submit button
                submitButton.disabled = false;
                submitButton.textContent = '🎯 GET MY CAREER BLUEPRINT + FREE STRATEGY CALL';
            }
        }
        
        // Validate form
        function validateForm(data) {
            let isValid = true;
            
            if (!data.name || data.name.length < 2) {
                showError('nameError', 'Please enter your full name');
                isValid = false;
            }
            
            if (!data.email) {
                showError('emailError', 'Email is required to send your analysis');
                isValid = false;
            } else if (!isValidEmail(data.email)) {
                showError('emailError', 'Please enter a valid email address');
                isValid = false;
            }
            
            return isValid;
        }
        
        // Show error message
        function showError(elementId, message) {
            const errorElement = document.getElementById(elementId);
            const inputElement = document.getElementById(elementId.replace('Error', ''));
            
            errorElement.textContent = message;
            inputElement.classList.add('error');
        }
        
        // Clear all errors
        function clearErrors() {
            const errorElements = document.querySelectorAll('.error-message');
            const inputElements = document.querySelectorAll('.form-input');
            
            errorElements.forEach(el => el.textContent = '');
            inputElements.forEach(el => el.classList.remove('error'));
        }
        
        // Validate email format
        function isValidEmail(email) {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return emailRegex.test(email);
        }
        
        // Initialize page
        document.addEventListener('DOMContentLoaded', function() {
            getSessionId();
            startCountdown();
        });
    </script>
</body>
</html>
"""

RESULTS_PAGE_HTML = """<!-- Complete results page with booking CTAs -->"""
THANK_YOU_HTML = """<!-- Complete thank you page after booking -->"""
