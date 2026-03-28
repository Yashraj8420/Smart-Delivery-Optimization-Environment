# 🚚 Smart Delivery Optimization Environment

## 📌 Problem Statement

Build an OpenEnv-compatible environment where an AI agent interacts using `step()`, `reset()`, and `state()` functions to solve a real-world problem.

---

## 💡 Solution Overview

We created a **grid-based delivery simulation** where an AI agent learns to deliver packages efficiently.

The agent navigates a grid, completes deliveries, and tries to maximize rewards while minimizing unnecessary steps.

---

## ⚙️ Environment Design

### 🧱 State Space

* Agent Position (x, y)
* Remaining Delivery Locations

### 🎮 Actions

* Up
* Down
* Left
* Right

### 🏆 Reward System

* +10 → Delivery completed
* -1 → Each step
* -5 → Invalid move

---

## 🧠 Agent Design

### 🔹 Random Agent

* Moves randomly
* Poor performance (negative reward)

### 🔹 Smart Agent

* Moves toward nearest delivery
* Efficient and goal-driven
* Achieves positive reward

---

## 📊 Results

| Agent Type   | Result                 |
| ------------ | ---------------------- |
| Random Agent | Negative Reward        |
| Smart Agent  | Positive Reward (~20+) |

---

## 🎯 Difficulty Levels

* Easy → 3 deliveries (5x5 grid)
* Medium → 5 deliveries
* Hard → 8 deliveries

---

## 🚀 How to Run

1. Open terminal in project folder
2. Run:

```bash
python run.py
```

---

## 📂 Project Structure

```
Scaler_Hackthon/
│
├── env/
│   └── delivery_env.py
│
├── agent/
│   └── random_agent.py
│
├── run.py
├── openenv.yaml
├── README.md
```

---

## 🔮 Future Improvements

* Implement Q-Learning / Deep Reinforcement Learning
* Add GUI visualization
* Optimize delivery routing

---

## 🏁 Conclusion

This project demonstrates how AI can solve real-world logistics problems by optimizing delivery routes using intelligent decision-making.
