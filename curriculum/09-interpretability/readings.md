# Interpretability Readings

## Core Papers (Required)

### 1. Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet
- **Link:** https://www.anthropic.com/research/mapping-mind-language-model
- **Authors:** Anthropic
- **Year:** 2024
- **Difficulty:** 4/5
- **Time:** 2-3 hours
- **Why read:** Anthropic's breakthrough paper. Found interpretable features in Claude.

**Key takeaways:**
- Sparse autoencoders extract monosemantic features
- Features correspond to real concepts (Golden Gate Bridge, code errors, etc.)
- Scale matters - larger models have cleaner features

### 2. Toy Models of Superposition
- **Link:** https://transformer-circuits.pub/2022/toy_model/index.html
- **Authors:** Anthropic (Circuits team)
- **Year:** 2022
- **Difficulty:** 4/5
- **Time:** 2 hours
- **Why read:** Foundational paper on why interpretability is hard

**Key concepts:**
- Superposition: models encode more features than dimensions
- Phase transitions in when superposition occurs
- Implications for interpretability

### 3. A Mathematical Framework for Transformer Circuits
- **Link:** https://transformer-circuits.pub/2021/framework/index.html
- **Authors:** Anthropic
- **Year:** 2021
- **Difficulty:** 5/5
- **Time:** 3+ hours (dense)
- **Why read:** Foundational framework for mechanistic interpretability

---

## Accessible Introductions

### 4. Mechanistic Interpretability Tutorial (Neel Nanda)
- **Link:** https://www.neelnanda.io/mechanistic-interpretability/getting-started
- **Difficulty:** 3/5
- **Time:** 1 hour
- **Why read:** Practical getting started guide

### 5. 200 Concrete Open Problems in Mechanistic Interpretability
- **Link:** https://www.neelnanda.io/mechanistic-interpretability/200-problems
- **Difficulty:** 3/5
- **Time:** 1 hour (skim)
- **Why read:** Understand the research landscape

### 6. Interpretability in the Wild
- **Link:** https://www.anthropic.com/research/probing-language-models
- **Difficulty:** 3/5
- **Time:** 30 min
- **Why read:** Anthropic's perspective on probing

---

## Practical Tools

### 7. TransformerLens Documentation
- **Link:** https://neelnanda-io.github.io/TransformerLens/
- **Difficulty:** 3/5
- **Time:** 2 hours (hands-on)
- **Why read:** Library for interpretability experiments

### 8. ARENA Interpretability Exercises
- **Link:** https://arena.education/
- **Difficulty:** 4/5
- **Time:** 10+ hours (optional, deep dive)
- **Why read:** Structured practical exercises

---

## Classic Papers

### 9. Visualizing and Understanding Convolutional Networks
- **Link:** https://arxiv.org/abs/1311.2901
- **Year:** 2013
- **Difficulty:** 3/5
- **Time:** 1 hour
- **Why read:** Classic interpretability work (CNNs, but foundational)

### 10. Attention is Not Explanation / Attention is Not Not Explanation
- **Links:** https://arxiv.org/abs/1902.10186, https://arxiv.org/abs/1908.04626
- **Difficulty:** 4/5
- **Time:** 2 hours
- **Why read:** Debate on what attention tells us

---

## Advanced (Optional)

### 11. Towards Monosemanticity (Original)
- **Link:** https://transformer-circuits.pub/2023/monosemantic-features/index.html
- **Difficulty:** 5/5
- **Time:** 3 hours
- **Why read:** Predecessor to Scaling Monosemanticity

### 12. Sleeper Agents: Training Deceptive LLMs That Persist Through Safety Training
- **Link:** https://arxiv.org/abs/2401.05566
- **Difficulty:** 4/5
- **Time:** 2 hours
- **Why read:** Uses probing to detect deceptive behavior

---

## Reading Order

1. Neel Nanda's getting started guide (#4)
2. Toy Models of Superposition (#2) - understand the problem
3. Scaling Monosemanticity (#1) - the solution
4. TransformerLens docs (#7) - get hands-on
5. Mathematical Framework (#3) - if you want to go deep

---

## XP Values

| Reading | XP |
|---------|-----|
| Scaling Monosemanticity | +75 |
| Toy Models of Superposition | +75 |
| Mathematical Framework | +100 |
| Getting Started Guide | +25 |
| TransformerLens (hands-on) | +50 |

**Module completion bonus:** +200 XP
