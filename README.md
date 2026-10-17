# LeetCode Solutions

My personal LeetCode submissions, written in Python. I use this repo to practice data structures and algorithms in a structured, consistent way.

[![LeetCode](https://img.shields.io/badge/LeetCode-Profile-orange?logo=leetcode)](https://leetcode.com/u/Athika_Priya)
![Language](https://img.shields.io/badge/language-Python-blue)
![Streak](https://img.shields.io/badge/50--day-streak-green) ![Streak](https://img.shields.io/badge/100--day-streak-green)

## About

I'm Athika, a Python/Django backend developer with a BSc in Mathematics and a background as a mathematics teacher. I'm completing an MSc in CSE and practice DSA to sharpen my problem-solving and prepare for backend engineering roles.

- Portfolio: [athikadev.netlify.app](https://athikadev.netlify.app)
- GitHub: [github.com/athikapriya](https://github.com/athikapriya)
- Email: athika.web@gmail.com

## How I Practice

I work one topic at a time, going deep before moving on:

1. **Pick a topic**: choose a single DSA topic (for example, Two Pointers or Dynamic Programming).
2. **Study it**: learn the core idea, the common patterns, and the time/space trade-offs before touching problems.
3. **Solve Easy problems**: build intuition and confirm the basics.
4. **Solve Medium problems**: apply the pattern in less obvious situations.
5. **Solve Hard problems**: stretch the pattern to its limits.

For every problem, I use a three-pass method:

1. **Attempt independently**: try it alone first, even if I get stuck.
2. **Study the solution**: understand the approach and why it works.
3. **Rewrite from memory**: re-implement it without looking.

I stay on one topic until I'm comfortable with it, rather than jumping between many tracks at once.

## Topics Covered

- Arrays & Hashmap

## Repository Structure

```
leetcode-solutions/
├── arrays-hashmap/
│   ├── easy/
│   ├── medium/
│   └── hard/
└── README.md
```

Inside each topic folder, solutions are grouped by difficulty and named `<problem-number>-<problem-name>.py`, for example `0001-two-sum.py`.

## Solution Format

Each solution includes the problem link, difficulty, a short approach note, and time/space complexity:

```python
# Approach: hash map of value -> index
# Time: O(n) | Space: O(n)

from typing import List

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i, n in enumerate(nums):
            need = target - n
            if need in seen:
                return [seen[need], i]
            seen [n] = i
```

## Progress

| Difficulty | Solved |
|------------|--------|
| Easy       | 5      |
| Medium     | 1      |
| Hard       | 0      |
| **Total**  | **6**  |

Milestone: completed a 100-day LeetCode streak after about three years of attempts.

## Goals

- Build a strong foundation in core DSA topics, one at a time
- Stay consistent with a daily practice routine
- Prepare for technical interviews for remote backend roles

## Contact

Feel free to reach out or open an issue if you spot a better approach to any solution.

📧 athika.web@gmail.com