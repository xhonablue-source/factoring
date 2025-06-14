<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Factoring Made Simple</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #333;
            line-height: 1.6;
        }
        
        .container {
            background: white;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        }
        
        h1 {
            color: #4a5568;
            text-align: center;
            margin-bottom: 30px;
            font-size: 2.5em;
        }
        
        h2 {
            color: #2d3748;
            border-left: 4px solid #667eea;
            padding-left: 15px;
            margin-top: 40px;
        }
        
        .lesson-section {
            margin: 30px 0;
            padding: 20px;
            border-radius: 10px;
            background: #f7fafc;
        }
        
        .example-box {
            background: #e6fffa;
            border: 2px solid #38b2ac;
            border-radius: 8px;
            padding: 20px;
            margin: 15px 0;
        }
        
        .step {
            background: #fff5f5;
            border-left: 4px solid #e53e3e;
            padding: 15px;
            margin: 10px 0;
        }
        
        .interactive-section {
            background: #f0fff4;
            border: 2px dashed #38a169;
            border-radius: 10px;
            padding: 20px;
            margin: 20px 0;
        }
        
        button {
            background: #667eea;
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 6px;
            cursor: pointer;
            font-size: 16px;
            margin: 10px 5px;
            transition: background 0.3s;
        }
        
        button:hover {
            background: #5a67d8;
        }
        
        .answer {
            background: #fef5e7;
            border: 2px solid #ed8936;
            border-radius: 8px;
            padding: 15px;
            margin: 10px 0;
            display: none;
        }
        
        .visual-demo {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin: 20px 0;
        }
        
        .algebra-tiles {
            display: flex;
            flex-wrap: wrap;
            gap: 5px;
            margin: 10px 0;
        }
        
        .tile {
            width: 30px;
            height: 30px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 4px;
            color: white;
            font-weight: bold;
        }
        
        .x-squared { background: #e53e3e; }
        .x-tile { background: #38a169; }
        .unit-tile { background: #3182ce; }
        
        .progress-bar {
            width: 100%;
            height: 20px;
            background: #e2e8f0;
            border-radius: 10px;
            margin: 20px 0;
            overflow: hidden;
        }
        
        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #667eea, #764ba2);
            width: 0%;
            transition: width 0.5s ease;
        }
        
        code {
            background: #2d3748;
            color: #e2e8f0;
            padding: 4px 8px;
            border-radius: 4px;
            font-family: 'Courier New', monospace;
        }
        
        .practice-problem {
            background: #ebf8ff;
            border: 2px solid #3182ce;
            border-radius: 8px;
            padding: 20px;
            margin: 15px 0;
        }
        
        input[type="text"] {
            padding: 8px 12px;
            border: 2px solid #cbd5e0;
            border-radius: 6px;
            font-size: 16px;
            margin: 5px;
        }
        
        .correct { border-color: #38a169 !important; background: #f0fff4; }
        .incorrect { border-color: #e53e3e !important; background: #fff5f5; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🧮 Factoring Made Simple</h1>
        
        <div class="progress-bar">
            <div class="progress-fill" id="progress"></div>
        </div>
        
        <div class="lesson-section">
            <h2>What is Factoring? 🤔</h2>
            <p><strong>Factoring is like "un-multiplying"</strong> - we take an expression and break it down into smaller pieces that multiply together.</p>
            
            <div class="example-box">
                <p><strong>Think of it like this:</strong></p>
                <p>If <code>2 × 3 = 6</code>, then factoring 6 gives us <code>6 = 2 × 3</code></p>
                <p>If <code>(x + 2)(x + 3) = x² + 5x + 6</code>, then factoring <code>x² + 5x + 6</code> gives us <code>(x + 2)(x + 3)</code></p>
            </div>
        </div>

        <div class="lesson-section">
            <h2>Step 1: Greatest Common Factor (GCF) 🔍</h2>
            <p>Always start by looking for common factors!</p>
            
            <div class="example-box">
                <h3>Example: Factor 6x + 9</h3>
                <div class="step">
                    <strong>Step 1:</strong> Find what's common: Both terms have a factor of 3
                </div>
                <div class="step">
                    <strong>Step 2:</strong> Factor it out: <code>6x + 9 = 3(2x + 3)</code>
                </div>
            </div>
            
            <div class="interactive-section">
                <h3>Try It: Factor 4x + 8</h3>
                <input type="text" id="gcf1" placeholder="Your answer...">
                <button onclick="checkGCF1()">Check Answer</button>
                <div id="gcf1-feedback" class="answer"></div>
            </div>
        </div>

        <div class="lesson-section">
            <h2>Step 2: Factoring Quadratics (x² + bx + c) 📐</h2>
            <p>For expressions like <code>x² + 5x + 6</code>, we need two numbers that:</p>
            <ul>
                <li><strong>Multiply</strong> to give the constant term (6)</li>
                <li><strong>Add</strong> to give the middle coefficient (5)</li>
            </ul>
            
            <div class="visual-demo">
                <div>
                    <h3>Visual Representation</h3>
                    <div class="algebra-tiles">
                        <div class="tile x-squared">x²</div>
                        <div class="tile x-tile">x</div>
                        <div class="tile x-tile">x</div>
                        <div class="tile x-tile">x</div>
                        <div class="tile x-tile">x</div>
                        <div class="tile x-tile">x</div>
                        <div class="tile unit-tile">1</div>
                        <div class="tile unit-tile">1</div>
                        <div class="tile unit-tile">1</div>
                        <div class="tile unit-tile">1</div>
                        <div class="tile unit-tile">1</div>
                        <div class="tile unit-tile">1</div>
                    </div>
                    <p>This represents x² + 5x + 6</p>
                </div>
                <div>
                    <h3>Factored Form</h3>
                    <p>We arrange these into a rectangle:</p>
                    <table style="border-collapse: collapse; margin: 20px 0;">
                        <tr>
                            <td style="border: 2px solid #333; padding: 10px; background: #e53e3e; color: white;">x²</td>
                            <td style="border: 2px solid #333; padding: 10px; background: #38a169; color: white;">2x</td>
                        </tr>
                        <tr>
                            <td style="border: 2px solid #333; padding: 10px; background: #38a169; color: white;">3x</td>
                            <td style="border: 2px solid #333; padding: 10px; background: #3182ce; color: white;">6</td>
                        </tr>
                    </table>
                    <p>This gives us (x + 2)(x + 3)</p>
                </div>
            </div>
            
            <div class="example-box">
                <h3>Example: Factor x² + 5x + 6</h3>
                <div class="step">
                    <strong>Step 1:</strong> We need two numbers that multiply to 6 and add to 5
                </div>
                <div class="step">
                    <strong>Step 2:</strong> Think: 1×6=6, 1+6=7 ❌ | 2×3=6, 2+3=5 ✅
                </div>
                <div class="step">
                    <strong>Step 3:</strong> So x² + 5x + 6 = (x + 2)(x + 3)
                </div>
            </div>
            
            <div class="interactive-section">
                <h3>Try It: Factor x² + 7x + 12</h3>
                <p>Hint: Find two numbers that multiply to 12 and add to 7</p>
                <input type="text" id="quad1" placeholder="(x + ?)(x + ?)">
                <button onclick="checkQuad1()">Check Answer</button>
                <div id="quad1-feedback" class="answer"></div>
            </div>
        </div>

        <div class="lesson-section">
            <h2>Step 3: When the First Coefficient isn't 1 🎯</h2>
            <p>For expressions like <code>2x² + 7x + 3</code>, we use the AC method:</p>
            
            <div class="example-box">
                <h3>Example: Factor 2x² + 7x + 3</h3>
                <div class="step">
                    <strong>Step 1:</strong> Multiply A and C: 2 × 3 = 6
                </div>
                <div class="step">
                    <strong>Step 2:</strong> Find two numbers that multiply to 6 and add to 7: 1×6=6, 1+6=7 ✅
                </div>
                <div class="step">
                    <strong>Step 3:</strong> Rewrite: 2x² + 7x + 3 = 2x² + 1x + 6x + 3
                </div>
                <div class="step">
                    <strong>Step 4:</strong> Group: (2x² + 1x) + (6x + 3) = x(2x + 1) + 3(2x + 1)
                </div>
                <div class="step">
                    <strong>Step 5:</strong> Factor out common factor: (2x + 1)(x + 3)
                </div>
            </div>
        </div>

        <div class="lesson-section">
            <h2>Step 4: Special Cases 🌟</h2>
            
            <div class="example-box">
                <h3>Difference of Squares: a² - b² = (a + b)(a - b)</h3>
                <p>Example: x² - 9 = x² - 3² = (x + 3)(x - 3)</p>
            </div>
            
            <div class="example-box">
                <h3>Perfect Square Trinomials: a² ± 2ab + b² = (a ± b)²</h3>
                <p>Example: x² + 6x + 9 = x² + 2(3x) + 3² = (x + 3)²</p>
            </div>
            
            <div class="interactive-section">
                <h3>Try It: Factor x² - 16</h3>
                <input type="text" id="special1" placeholder="Your answer...">
                <button onclick="checkSpecial1()">Check Answer</button>
                <div id="special1-feedback" class="answer"></div>
            </div>
        </div>

        <div class="lesson-section">
            <h2>Practice Problems 💪</h2>
            
            <div class="practice-problem">
                <h3>Problem 1: Factor 3x + 12</h3>
                <input type="text" id="practice1" placeholder="Your answer...">
                <button onclick="checkPractice1()">Check</button>
                <div id="practice1-feedback" class="answer"></div>
            </div>
            
            <div class="practice-problem">
                <h3>Problem 2: Factor x² - 5x + 6</h3>
                <input type="text" id="practice2" placeholder="Your answer...">
                <button onclick="checkPractice2()">Check</button>
                <div id="practice2-feedback" class="answer"></div>
            </div>
            
            <div class="practice-problem">
                <h3>Problem 3: Factor x² - 25</h3>
                <input type="text" id="practice3" placeholder="Your answer...">
                <button onclick="checkPractice3()">Check</button>
                <div id="practice3-feedback" class="answer"></div>
            </div>
        </div>

        <div class="lesson-section">
            <h2>Quick Reference Card 📝</h2>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                <div class="example-box">
                    <h4>Always Start With:</h4>
                    <p>1. Look for GCF first<br>
                    2. Check for special patterns<br>
                    3. Use appropriate method</p>
                </div>
                <div class="example-box">
                    <h4>Common Patterns:</h4>
                    <p>• ax + b = factor out GCF<br>
                    • x² + bx + c = find two numbers<br>
                    • a² - b² = (a+b)(a-b)</p>
                </div>
            </div>
        </div>
    </div>

    <script>
        let progress = 0;
        
        function updateProgress() {
            progress += 12.5;
            document.getElementById('progress').style.width = progress + '%';
        }
        
        function checkGCF1() {
            const answer = document.getElementById('gcf1').value.trim().toLowerCase();
            const feedback = document.getElementById('gcf1-feedback');
            
            if (answer === '4(x + 2)' || answer === '4(x+2)') {
                feedback.innerHTML = '✅ Correct! 4x + 8 = 4(x + 2)';
                feedback.style.display = 'block';
                document.getElementById('gcf1').className = 'correct';
                updateProgress();
            } else {
                feedback.innerHTML = '❌ Not quite. Remember: factor out the GCF of 4. Try 4(x + 2)';
                feedback.style.display = 'block';
                document.getElementById('gcf1').className = 'incorrect';
            }
        }
        
        function checkQuad1() {
            const answer = document.getElementById('quad1').value.trim().toLowerCase();
            const feedback = document.getElementById('quad1-feedback');
            
            if (answer.includes('(x + 3)') && answer.includes('(x + 4)')) {
                feedback.innerHTML = '✅ Perfect! Two numbers that multiply to 12 and add to 7 are 3 and 4.';
                feedback.style.display = 'block';
                document.getElementById('quad1').className = 'correct';
                updateProgress();
            } else {
                feedback.innerHTML = '❌ Try again. Think: 3 × 4 = 12 and 3 + 4 = 7, so (x + 3)(x + 4)';
                feedback.style.display = 'block';
                document.getElementById('quad1').className = 'incorrect';
            }
        }
        
        function checkSpecial1() {
            const answer = document.getElementById('special1').value.trim().toLowerCase();
            const feedback = document.getElementById('special1-feedback');
            
            if (answer.includes('(x + 4)') && answer.includes('(x - 4)')) {
                feedback.innerHTML = '✅ Excellent! x² - 16 = x² - 4² = (x + 4)(x - 4)';
                feedback.style.display = 'block';
                document.getElementById('special1').className = 'correct';
                updateProgress();
            } else {
                feedback.innerHTML = '❌ This is a difference of squares: x² - 16 = (x + 4)(x - 4)';
                feedback.style.display = 'block';
                document.getElementById('special1').className = 'incorrect';
            }
        }
        
        function checkPractice1() {
            const answer = document.getElementById('practice1').value.trim().toLowerCase();
            const feedback = document.getElementById('practice1-feedback');
            
            if (answer === '3(x + 4)' || answer === '3(x+4)') {
                feedback.innerHTML = '✅ Great job! 3x + 12 = 3(x + 4)';
                feedback.style.display = 'block';
                document.getElementById('practice1').className = 'correct';
                updateProgress();
            } else {
                feedback.innerHTML = '❌ Factor out the GCF of 3: 3x + 12 = 3(x + 4)';
                feedback.style.display = 'block';
                document.getElementById('practice1').className = 'incorrect';
            }
        }
        
        function checkPractice2() {
            const answer = document.getElementById('practice2').value.trim().toLowerCase();
            const feedback = document.getElementById('practice2-feedback');
            
            if (answer.includes('(x - 2)') && answer.includes('(x - 3)')) {
                feedback.innerHTML = '✅ Perfect! Two numbers that multiply to 6 and add to -5 are -2 and -3.';
                feedback.style.display = 'block';
                document.getElementById('practice2').className = 'correct';
                updateProgress();
            } else {
                feedback.innerHTML = '❌ Think: (-2) × (-3) = 6 and (-2) + (-3) = -5, so (x - 2)(x - 3)';
                feedback.style.display = 'block';
                document.getElementById('practice2').className = 'incorrect';
            }
        }
        
        function checkPractice3() {
            const answer = document.getElementById('practice3').value.trim().toLowerCase();
            const feedback = document.getElementById('practice3-feedback');
            
            if (answer.includes('(x + 5)') && answer.includes('(x - 5)')) {
                feedback.innerHTML = '✅ Awesome! x² - 25 = x² - 5² = (x + 5)(x - 5)';
                feedback.style.display = 'block';
                document.getElementById('practice3').className = 'correct';
                updateProgress();
            } else {
                feedback.innerHTML = '❌ This is a difference of squares: x² - 25 = (x + 5)(x - 5)';
                feedback.style.display = 'block';
                document.getElementById('practice3').className = 'incorrect';
            }
        }
    </script>
</body>
</html>
