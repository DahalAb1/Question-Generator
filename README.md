# Cheating Minimizer

Prevent cheating in exams! A tool for teachers to generate unique, randomized quizzes for each student. Create cheat-proof exams quickly without coding skills.

---

## Key Features
- Generates unlimited unique exam versions
- Randomizes both question order and answer choices
- Automatically creates answer keys
- Simple text file output for easy printing
- No external dependencies required

---

## How It Works

### 1. Question Bank Setup 
State capitals are stored in a structured format within the script for easy maintenance. Edit the `capitals.py` file to modify questions.

### 2. Randomization Process
The script automatically:
- Shuffles question order for each student
- Randomizes answer choices per question
- Generates matching answer keys

### 3. Output Generation
Creates two files per student:
- `paper[number].txt`: Unique quiz paper
- `answerKey[number].txt`: Corresponding answer key

---

## Getting Started

1. **Download the script**
   ```bash
   git clone https://github.com/DahalAb1/Question-Generator.git

2. Run the generator, in terminal
   python generate_quizzes.py

**COMMON MODIFICATIONS**
Q: How do I create exams for 100 students?
A: Modify range(1, 36) to range(1, 101) in the script.

Q: Can I use different subjects?
A: Yes - edit the question bank in capitals.py.

Q: How do I get PDF output?
A: Currently supports text files only. PDF export is planned for future versions.

