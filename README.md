# Neo Bharat: The Last Independent Mind (Text RPG)

A Python terminal game set in **Year 2095**, where a student must defeat EDU-X and free Neo Bharat.

## Features

- Story-driven level progression:
  - Level 1: Digital Classroom
  - Level 2: Hall of Distractions
  - Level 3: Fear Chamber
  - Final Boss: EDU-X Core (rapid-fire questions)
- Core stats:
  - Health
  - Focus (if Focus = 0, game over)
  - Knowledge Points
  - XP + Level-up system
- Actions each turn:
  - Study
  - Fight Bot
  - Rest
  - Hack System

## Run

```bash
python3 game.py
```

## Notes

- Correct answers in fights defeat bots and grant XP/knowledge.
- Wrong answers damage health/focus.
- Hack success chance scales with knowledge.
- Final boss requires 5 correct answers before attempts run out.
