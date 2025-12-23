# Transformer Readings

## Core Papers (Required)

### 1. Attention Is All You Need
- **Link:** https://arxiv.org/abs/1706.03762
- **Authors:** Vaswani et al.
- **Year:** 2017
- **Difficulty:** 4/5
- **Time:** 2-3 hours (first read), revisit while implementing
- **Why read:** THE foundational paper. Must read multiple times.

**Key sections:**
- Section 3.2: Scaled Dot-Product Attention (core mechanism)
- Section 3.2.2: Multi-Head Attention
- Section 3.5: Positional Encoding
- Figure 1: Architecture diagram (memorize this)

---

## Visual Explanations (Read Before Paper)

### 2. The Illustrated Transformer
- **Link:** https://jalammar.github.io/illustrated-transformer/
- **Author:** Jay Alammar
- **Difficulty:** 2/5
- **Time:** 1 hour
- **Why read:** Best visual explanation. Read BEFORE the paper.

### 3. The Annotated Transformer
- **Link:** https://nlp.seas.harvard.edu/annotated-transformer/
- **Author:** Harvard NLP
- **Difficulty:** 3/5
- **Time:** 2 hours
- **Why read:** Line-by-line implementation walkthrough

### 4. 3Blue1Brown: Attention in Transformers
- **Link:** https://www.youtube.com/watch?v=eMlx5fFNoYc
- **Difficulty:** 2/5
- **Time:** 30 min
- **Why read:** Beautiful geometric intuition

---

## Implementation References

### 5. Karpathy's nanoGPT
- **Link:** https://github.com/karpathy/nanoGPT
- **Difficulty:** 3/5
- **Time:** 2-3 hours to study
- **Why read:** Clean, minimal implementation to reference

### 6. Karpathy's "Let's build GPT" video
- **Link:** https://www.youtube.com/watch?v=kCc8FmEb1nY
- **Difficulty:** 3/5
- **Time:** 2 hours
- **Why read:** Watch him build it from scratch, explains every decision

### 7. minGPT
- **Link:** https://github.com/karpathy/minGPT
- **Difficulty:** 3/5
- **Time:** 1-2 hours to study
- **Why read:** Even simpler reference implementation

---

## Deep Dives (After Implementation)

### 8. FlashAttention Paper
- **Link:** https://arxiv.org/abs/2205.14135
- **Difficulty:** 5/5
- **Time:** 2 hours
- **Why read:** Understand attention optimization

### 9. Rotary Position Embedding (RoPE)
- **Link:** https://arxiv.org/abs/2104.09864
- **Difficulty:** 4/5
- **Time:** 1.5 hours
- **Why read:** Modern alternative to sinusoidal encoding

### 10. On Layer Normalization in the Transformer Architecture
- **Link:** https://arxiv.org/abs/2002.04745
- **Difficulty:** 4/5
- **Time:** 1 hour
- **Why read:** Pre-norm vs post-norm discussion

---

## Suggested Order

1. **3Blue1Brown video** - Geometric intuition (30 min)
2. **Illustrated Transformer** - Visual walkthrough (1 hr)
3. **Attention Is All You Need** - The paper (2-3 hrs, skim first)
4. **Karpathy video** - Watch implementation (2 hrs)
5. **Annotated Transformer** - Reference while implementing
6. **Build your own** - See Project 1
7. **FlashAttention** - After you understand the baseline

---

## XP Values

| Reading | XP |
|---------|-----|
| Attention Is All You Need | +75 |
| Illustrated Transformer | +25 |
| Annotated Transformer | +50 |
| Karpathy video | +50 |
| FlashAttention (advanced) | +75 |

**Module completion bonus:** +200 XP
