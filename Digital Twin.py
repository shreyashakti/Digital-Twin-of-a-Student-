"Digital Twin of a Student - Simple Academic Life Simulator "

import statistics

logs = []  # each entry: {"date", "study", "sleep", "attended", "quiz"}


def add_log():
    date = input("Date (e.g. 2026-01-01): ").strip()

    while True:
        try:
            study = float(input("Study hours today: "))
            break
        except ValueError:
            print("Please enter a number (e.g. 3 or 2.5).")

    while True:
        try:
            sleep = float(input("Sleep hours today: "))
            break
        except ValueError:
            print("Please enter a number (e.g. 7).")

    while True:
        attended_input = input("Attended class? (y/n): ").strip().lower()
        if attended_input in ("y", "n"):
            attended = attended_input == "y"
            break
        print("Please enter y or n.")

    while True:
        quiz_input = input("Quiz score today (leave blank if none): ").strip()
        if quiz_input == "":
            quiz = None
            break
        try:
            quiz = float(quiz_input)
            break
        except ValueError:
            print("Please enter a number, or leave blank.")

    logs.append({"date": date, "study": study, "sleep": sleep, "attended": attended, "quiz": quiz})
    print("Saved!\n")


def slope(xs, ys):
    """Simple least-squares slope of ys vs xs."""
    n = len(xs)
    x_mean = sum(xs) / n
    y_mean = sum(ys) / n
    num = sum((x - x_mean) * (y - y_mean) for x, y in zip(xs, ys))
    den = sum((x - x_mean) ** 2 for x in xs)
    return num / den if den else 0.0


def analyze():
    """Module: Performance Analysis"""
    if not logs:
        print("No data yet. Add some logs first.\n")
        return None

    study_avg = statistics.mean(l["study"] for l in logs)
    sleep_avg = statistics.mean(l["sleep"] for l in logs)
    attendance_rate = sum(l["attended"] for l in logs) / len(logs) * 100
    scored = [l for l in logs if l["quiz"] is not None]
    quiz_avg = statistics.mean(l["quiz"] for l in scored) if scored else None

    trend = None
    if len(scored) >= 2:
        xs = list(range(len(scored)))
        ys = [l["quiz"] for l in scored]
        trend = slope(xs, ys)

    print("\n--- Performance Summary ---")
    print(f"Days logged: {len(logs)}")
    print(f"Avg study hours/day: {study_avg:.2f}")
    print(f"Avg sleep hours/day: {sleep_avg:.2f}")
    print(f"Attendance rate: {attendance_rate:.1f}%")
    print(f"Avg quiz score: {quiz_avg:.2f}" if quiz_avg is not None else "Avg quiz score: N/A")
    if trend is not None:
        print(f"Quiz score trend: {trend:+.2f} points/day")
    print()

    return {
        "study_avg": study_avg, "sleep_avg": sleep_avg,
        "attendance_rate": attendance_rate, "quiz_avg": quiz_avg,
        "trend": trend, "scored": scored,
    }


def simulate_what_if(summary):
    """Module: What-If Simulation Engine"""
    if summary is None:
        return None

    plan_study = float(input("Planned study hours/day: "))
    days = int(input("Number of days to simulate: "))
    scored = summary["scored"]

    if len(scored) >= 3:
        # Fit a simple line: quiz_score ~ study_hours, using this student's own history
        xs = [l["study"] for l in scored]
        ys = [l["quiz"] for l in scored]
        b = slope(xs, ys)
        a = statistics.mean(ys) - b * statistics.mean(xs)
        steady_state = max(0, min(100, a + b * plan_study))
        model = "personalized regression"
    else:
        # Not enough history yet - generic diminishing-returns estimate
        steady_state = min(100, 40 + 30 * (1 - 2.71828 ** (-plan_study / 3)))
        model = "generic heuristic (log more days for a personalized model)"

    start = scored[-1]["quiz"] if scored else 50.0

    # Project gradually toward the steady-state score, day by day
    current = start
    trajectory = []
    for _ in range(days):
        current += 0.15 * (steady_state - current)
        trajectory.append(round(current, 1))

    print(f"\n--- What-If Simulation ({model}) ---")
    print(f"Current score: {start:.1f}")
    print(f"Projected steady-state score at {plan_study}h/day: {steady_state:.1f}")
    print(f"Day-by-day projection: {trajectory}\n")

    return {"start": start, "steady_state": steady_state}


def recommend(summary, sim_result=None):
    """Module: Recommendation Engine"""
    if summary is None:
        return

    tips = []
    if summary["sleep_avg"] < 6.5:
        tips.append("You're averaging low sleep. Aim for 7-9 hours to support memory and focus.")
    if summary["attendance_rate"] < 75:
        tips.append("Attendance is below 75%. Missed classes often correlate with lower quiz scores.")
    if summary["trend"] is not None and summary["trend"] < -0.3:
        tips.append("Your quiz scores are trending down. Try a quick review the day before each quiz.")
    if summary["study_avg"] > 6:
        tips.append("You're studying a lot but returns may be diminishing. Try shorter, focused sessions.")
    if sim_result:
        gain = sim_result["steady_state"] - sim_result["start"]
        if gain >= 5:
            tips.append("Your simulated plan looks promising - a solid improvement is projected.")
        elif gain <= -5:
            tips.append("Your simulated plan may hurt your score - consider more study hours.")
    if not tips:
        tips.append("No red flags detected. Keep up the consistent habits!")

    print("--- Recommendations ---")
    for t in tips:
        print("- " + t)
    print()


def main():
    print("=== Digital Twin of a Student ===")
    while True:
        print("1. Log today's data")
        print("2. View performance analysis")
        print("3. Run what-if simulation")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_log()
        elif choice == "2":
            summary = analyze()
            recommend(summary)
        elif choice == "3":
            summary = analyze()
            sim_result = simulate_what_if(summary)
            recommend(summary, sim_result)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.\n")


if __name__ == "__main__":
    main()
