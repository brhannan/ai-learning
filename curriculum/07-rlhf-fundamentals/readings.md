# RLHF Fundamentals Readings

## Core Papers (Required)

### 1. Training language models to follow instructions with human feedback (InstructGPT)
- **Link:** https://arxiv.org/abs/2203.02155
- **Authors:** OpenAI
- **Year:** 2022
- **Difficulty:** 4/5
- **Time:** 2-3 hours
- **Why read:** THE foundational RLHF paper. Describes the full pipeline.

**Key sections:**
- Section 2: Method (the three phases)
- Section 3: Results
- Appendix: Details on reward modeling

### 2. Learning to summarize from human feedback
- **Link:** https://arxiv.org/abs/2009.01325
- **Authors:** OpenAI
- **Year:** 2020
- **Difficulty:** 4/5
- **Time:** 2 hours
- **Why read:** Earlier RLHF work, cleaner task (summarization)

### 3. Proximal Policy Optimization (PPO)
- **Link:** https://arxiv.org/abs/1707.06347
- **Authors:** OpenAI
- **Year:** 2017
- **Difficulty:** 5/5
- **Time:** 2 hours
- **Why read:** Understand the RL algorithm used

---

## Alternatives to RLHF

### 4. Direct Preference Optimization (DPO)
- **Link:** https://arxiv.org/abs/2305.18290
- **Year:** 2023
- **Difficulty:** 4/5
- **Time:** 1.5 hours
- **Why read:** Major alternative that doesn't require RL

**Key insight:** DPO reformulates RLHF to avoid training a reward model

### 5. RLAIF: Scaling Reinforcement Learning from Human Feedback with AI Feedback
- **Link:** https://arxiv.org/abs/2309.00267
- **Year:** 2023
- **Difficulty:** 4/5
- **Time:** 1.5 hours
- **Why read:** Using AI instead of human feedback (leads to CAI)

---

## Failure Modes

### 6. The Effects of Reward Misspecification
- Search for "reward hacking LLM" and "reward gaming"
- **Difficulty:** 3/5
- **Time:** 1 hour
- **Why read:** Understand what can go wrong

### 7. Sycophancy to Subterfuge: Investigating Reward-Tampering in AI
- **Link:** https://www.anthropic.com/research/reward-tampering
- **Year:** 2024
- **Difficulty:** 3/5
- **Time:** 30 min
- **Why read:** Advanced failure mode research from Anthropic

---

## Practical Resources

### 8. RLHF Book by Nathan Lambert
- **Link:** https://rlhfbook.com/
- **Difficulty:** 3/5
- **Time:** 3-4 hours (selected chapters)
- **Why read:** Comprehensive, accessible treatment

### 9. TRL (Transformer Reinforcement Learning) Library
- **Link:** https://huggingface.co/docs/trl/
- **Difficulty:** 3/5
- **Time:** 2 hours (hands-on)
- **Why read:** Practical RLHF implementation

### 10. Anthropic's HH-RLHF Dataset
- **Link:** https://huggingface.co/datasets/Anthropic/hh-rlhf
- **Difficulty:** 2/5
- **Time:** 1 hour
- **Why read:** See real preference data

---

## Reading Order

1. InstructGPT (#1) - The foundation
2. RLHF Book chapters (#8) - Accessible context
3. DPO paper (#4) - Modern alternative
4. PPO paper (#3) - If you want deep understanding
5. RLAIF (#5) - Bridge to Constitutional AI
6. Move to Module 08 (Constitutional AI)

---

## XP Values

| Reading | XP |
|---------|-----|
| InstructGPT | +75 |
| Learning to Summarize | +50 |
| PPO | +75 |
| DPO | +75 |
| RLAIF | +50 |
| RLHF Book | +50 |

**Module completion bonus:** +200 XP
