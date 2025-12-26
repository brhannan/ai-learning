# Code Generation Readings

## Core Papers (Required)

### 1. HumanEval / Codex Paper
- **Link:** https://arxiv.org/abs/2107.03374
- **Authors:** OpenAI
- **Year:** 2021
- **Difficulty:** 3/5
- **Time:** 2 hours
- **Why read:** Introduced HumanEval benchmark, foundational for code eval

**Key points:**
- 164 hand-written Python problems
- pass@k metric
- Now largely saturated, but required knowledge

### 2. SWE-Bench: Can Language Models Resolve Real-World GitHub Issues?
- **Link:** https://arxiv.org/abs/2310.06770
- **Year:** 2023
- **Difficulty:** 3/5
- **Time:** 1.5 hours
- **Why read:** The benchmark that matters for real coding ability

**Key insight:** Tests end-to-end issue resolution, not just function completion

### 3. SWE-Agent: Agent-Computer Interfaces Enable Automated Software Engineering
- **Link:** https://arxiv.org/abs/2405.15793
- **Year:** 2024
- **Difficulty:** 4/5
- **Time:** 2 hours
- **Why read:** Leading open coding agent architecture

**Key components:**
- Custom shell interface for LLMs
- Search and navigation tools
- Edit mechanisms

---

## Code Training Data

### 4. The Stack: A Pretraining Dataset for Code
- **Link:** https://arxiv.org/abs/2211.15533
- **Year:** 2022
- **Difficulty:** 3/5
- **Time:** 1.5 hours
- **Why read:** Understand where code models get their training data

### 5. StarCoder / StarCoder2
- **Link:** https://arxiv.org/abs/2402.19173
- **Year:** 2024
- **Difficulty:** 3/5
- **Time:** 1.5 hours
- **Why read:** Leading open code model

---

## Flow Engineering

### 6. AlphaCodeium: Code Generation with AlphaCode-Level Performance
- **Link:** https://arxiv.org/abs/2401.08500
- **Year:** 2024
- **Difficulty:** 4/5
- **Time:** 1.5 hours
- **Why read:** Multi-step flow dramatically improves code gen

**Key techniques:**
- Problem reflection
- Public test generation
- Iterative refinement

---

## Practical Resources

### 7. Aider Leaderboard
- **Link:** https://aider.chat/docs/leaderboards/
- **Difficulty:** 2/5
- **Time:** 30 min
- **Why read:** Practical benchmark for coding assistants

### 8. LiveCodeBench
- **Link:** https://livecodebench.github.io/
- **Difficulty:** 2/5
- **Time:** 30 min
- **Why read:** Continuously updated to avoid contamination

### 9. SWE-Bench Lite Setup
- **Link:** https://github.com/princeton-nlp/SWE-bench
- **Difficulty:** 3/5
- **Time:** 2 hours (hands-on)
- **Why read:** Run SWE-Bench yourself

---

## Code Model Architectures

### 10. DeepSeek-Coder
- **Link:** https://arxiv.org/abs/2401.14196
- **Year:** 2024
- **Difficulty:** 4/5
- **Time:** 1.5 hours
- **Why read:** Strong open code model with detailed paper

### 11. Qwen2.5-Coder
- **Link:** https://arxiv.org/abs/2409.12186
- **Year:** 2024
- **Difficulty:** 4/5
- **Time:** 1.5 hours
- **Why read:** Current SOTA open code model

---

## Security & Risks

### 12. Code Security in LLM Outputs
- Search for "LLM code generation security vulnerabilities"
- **Difficulty:** 3/5
- **Time:** 1 hour
- **Why read:** LLMs can generate insecure code

**Common issues:**
- SQL injection
- Path traversal
- Hardcoded credentials

---

## Reading Order

1. HumanEval/Codex (#1) - Historical foundation
2. SWE-Bench paper (#2) - The benchmark that matters
3. SWE-Agent paper (#3) - How agents work
4. AlphaCodeium (#6) - Flow engineering
5. Aider leaderboard (#7) - Practical landscape
6. Try SWE-Bench Lite (#9) - Get hands-on

---

## XP Values

| Reading | XP |
|---------|-----|
| HumanEval/Codex | +50 |
| SWE-Bench | +75 |
| SWE-Agent | +75 |
| AlphaCodeium | +50 |
| The Stack | +50 |
| SWE-Bench hands-on | +100 |

**Module completion bonus:** +200 XP
