# 🎮 CounterPick

A simple CLI-based strategy game where prediction beats luck.

---

## 🧠 Concept

Two roles:
- 👑 Lead → earns points by surviving
- 🧠 Counter → tries to eliminate the Lead

Each round, both players choose a number from 1 to 10.

---

## 🎯 Game Modes

### CounterPick Vanilla
- Match → Lead loses instantly
- No match → Lead gains points equal to chosen number

### CounterPick One-Up
- Match → Lead gains squared points (n²)
- ±1 difference → Lead loses
- Otherwise → Lead gains normal points

---

## 🏁 Win Condition

- Both players must be Lead at least once
- Both must lose once as Lead
- Highest score wins

---

## ▶️ Run the Game

```bash
python main.py
