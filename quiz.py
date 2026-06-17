# ============================================
# PROJECT 4: GENERAL KNOWLEDGE QUIZ
# DecodeLabs Industrial Training Kit - 2026
# ============================================

def ask_question(question, correct_answer):
    """
    Question Block Micro-Architecture:
    Step 1: Ask & Capture
    Step 2: Sanitize (.strip().lower())
    Step 3: Evaluate (==)
    Step 4: Execute (score += 1)
    """
    print(f"\n❓ {question}")
    user_answer = input("Your Answer: ").strip().lower()  # Sanitization!
    
    if user_answer == correct_answer.lower():
        print("✅ Correct! +1 point")
        return 1  # Score increment
    else:
        print(f"❌ Wrong! Correct answer was: {correct_answer}")
        return 0  # No change to score

def main():
    print("=" * 45)
    print("   🧠 DecodeLabs General Knowledge Quiz")
    print("=" * 45)
    print("Answer the following 5 questions.")
    print("Type your answer and press Enter.\n")

    score = 0  # ⚠️ OUTSIDE loop — accumulator!

    # ── Question 1 ──
    score += ask_question(
        "What is the capital of France?",
        "paris"
    )

    # ── Question 2 ──
    score += ask_question(
        "Which planet is known as the Red Planet?",
        "mars"
    )

    # ── Question 3 ──
    score += ask_question(
        "What is the largest ocean on Earth?",
        "pacific"
    )

    # ── Question 4 ──
    score += ask_question(
        "Who invented the telephone?",
        "alexander graham bell"
    )

    # ── Question 5 ──
    score += ask_question(
        "How many continents are there on Earth?",
        "7"
    )

    # ── Final Output (F-string!) ──
    print("\n" + "=" * 45)
    print("           📊 QUIZ RESULTS")
    print("=" * 45)
    print(f"  Your Final Score : {score:>2} / 5")

    # Performance feedback
    if score == 5:
        print("  🏆 Perfect Score! Outstanding!")
    elif score >= 3:
        print("  🎯 Good Job! Keep learning!")
    elif score >= 1:
        print("  📚 Keep practicing! You'll do better!")
    else:
        print("  💪 Don't give up! Try again!")

    print("=" * 45)

if __name__ == "__main__":
    main()