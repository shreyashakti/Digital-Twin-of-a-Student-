# 🎓 Digital Twin of a Student
### Simple Academic Life Simulator
A Python-based **Digital Twin of a Student** that creates a virtual representation of a student's academic life using daily **study hours, sleep, attendance, and quiz scores**.

The system analyzes the student's habits, tracks performance trends, simulates possible future outcomes, and provides personalized recommendations.

## 🚀 Features

* 📝 **Daily Data Logging** — Records study hours, sleep, attendance, and quiz scores.
* 📊 **Performance Analysis** — Calculates average study/sleep hours, attendance rate, and quiz average.
* 📈 **Trend Analysis** — Tracks whether quiz performance is improving or declining.
* 🔮 **What-If Simulation** — Predicts possible quiz performance based on planned study hours.
* 🧠 **Personalized Recommendations** — Suggests improvements based on the student's data.
* 📐 **Regression Model** — Uses the student's own history when enough data is available.
* ⚡ **Simple Console Interface** — Easy to run and use.


## 🛠️ Technologies Used

* **Python**
* `statistics` module
* Basic data structures (`list`, `dictionary`)
* Mathematical calculations
* Linear regression / slope calculation

## ▶️ How to Run

1. Make sure **Python 3** is installed.
2. Save the code as:

```text
digital_twin.py
```

3. Run:

```bash
python digital_twin.py
```

4. Use the menu:

```text
1. Log today's data
2. View performance analysis
3. Run what-if simulation
4. Exit
```

**Tip:** Add several days of data before running analysis or simulation for more meaningful results.

## 🧠 How It Works

```text
Student Data
     ↓
Daily Logs
     ↓
Performance Analysis
     ↓
Trend Detection
     ↓
What-If Simulation
     ↓
Personalized Recommendations
```

The project starts with basic analysis and uses a **personalized regression model when at least 3 quiz records are available**. With less data, it uses a generic estimation.

## 🎯 Project Objective
The goal is to demonstrate how a **Digital Twin concept** can be applied to student life by using data to understand academic habits, explore possible outcomes, and support better study decisions.
 **"A digital version of a student that learns from their habits and helps them understand their academic performance."**

This project is an **educational simulation**, not a guaranteed predictor of real academic performance.

