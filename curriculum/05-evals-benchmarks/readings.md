# Evals & Benchmarks Readings

## Core Papers (Required)

### 1. MMLU: Measuring Massive Multitask Language Understanding
- **Link:** https://arxiv.org/abs/2009.03300
- **Year:** 2020
- **Difficulty:** 3/5
- **Time:** 1.5 hours
- **Why read:** THE standard knowledge benchmark

**Key points:**
- 57 tasks across STEM, humanities, social sciences
- Multiple choice format
- Know its limitations (memorization, contamination)

### 2. MMLU-Pro
- **Link:** https://arxiv.org/abs/2406.01574
- **Year:** 2024
- **Difficulty:** 3/5
- **Time:** 1 hour
- **Why read:** Harder version addressing MMLU saturation

### 3. IFEval: Instruction Following Evaluation
- **Link:** https://arxiv.org/abs/2311.07911
- **Year:** 2023
- **Difficulty:** 3/5
- **Time:** 1 hour
- **Why read:** Tests if models follow specific instructions

**Example constraints:**
- "Write exactly 100 words"
- "Include the word 'banana' at least 3 times"
- Verifiable, objective scoring

### 4. GPQA: Graduate-Level Google-Proof Q&A
- **Link:** https://arxiv.org/abs/2311.12022
- **Year:** 2023
- **Difficulty:** 3/5
- **Time:** 1 hour
- **Why read:** Hard benchmark for frontier models

---

## LLM-as-Judge (Required)

### 5. LLM-as-Judge Guide (Hamel Husain)
- **Link:** https://hamel.dev/blog/posts/llm-judge/
- **Difficulty:** 2/5
- **Time:** 1.5 hours
- **Why read:** Best practical guide to LLM evaluation

**Key patterns:**
- Pairwise comparison
- Rubric-based scoring
- Calibration techniques

### 6. Judging LLM-as-a-Judge (Meta)
- **Link:** https://arxiv.org/abs/2306.05685
- **Year:** 2023
- **Difficulty:** 4/5
- **Time:** 1.5 hours
- **Why read:** When LLM-as-Judge works and fails

---

## Benchmark Design

### 7. BIG-Bench Hard
- **Link:** https://arxiv.org/abs/2210.09261
- **Difficulty:** 3/5
- **Time:** 1 hour
- **Why read:** Subset of hard tasks that require reasoning

### 8. ARC-AGI Challenge
- **Link:** https://arcprize.org/arc
- **Difficulty:** 3/5
- **Time:** 1 hour
- **Why read:** Abstract reasoning benchmark, still unsaturated

---

## Evaluation Pitfalls

### 9. Benchmark Contamination Literature
- Search for "LLM benchmark contamination" and "data leakage evaluation"
- **Difficulty:** 2/5
- **Time:** 1 hour
- **Why read:** Understand why benchmarks degrade over time

### 10. Applied LLMs Essay (Evaluation Section)
- **Link:** https://applied-llms.org/#evaluation-monitoring
- **Difficulty:** 2/5
- **Time:** 30 min
- **Why read:** Practical production evaluation advice

---

## Practical Tools

### 11. LM Evaluation Harness
- **Link:** https://github.com/EleutherAI/lm-evaluation-harness
- **Difficulty:** 3/5
- **Time:** 2 hours (hands-on)
- **Why read:** Standard tool for running benchmarks

### 12. Braintrust / Eval Frameworks
- **Link:** https://www.braintrust.dev/
- **Difficulty:** 2/5
- **Time:** 1 hour
- **Why read:** Modern eval infrastructure

---

## Reading Order

1. Applied LLMs evaluation section (#10) - Get practical context
2. LLM-as-Judge guide (#5) - Most useful pattern
3. MMLU paper (#1) - Understand the standard
4. IFEval paper (#3) - Different eval approach
5. LM Evaluation Harness (#11) - Get hands-on
6. Contamination literature (#9) - Know the pitfalls

---

## XP Values

| Reading | XP |
|---------|-----|
| MMLU paper | +50 |
| IFEval paper | +50 |
| LLM-as-Judge guide | +75 |
| LM Eval Harness hands-on | +50 |
| GPQA paper | +50 |
| Build custom eval | +100 |

**Module completion bonus:** +200 XP
