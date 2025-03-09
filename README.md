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
   
