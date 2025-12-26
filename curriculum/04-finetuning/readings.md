# Finetuning Readings

## Core Papers (Required)

### 1. LoRA: Low-Rank Adaptation of Large Language Models
- **Link:** https://arxiv.org/abs/2106.09685
- **Authors:** Hu et al. (Microsoft)
- **Year:** 2021
- **Difficulty:** 3/5
- **Time:** 1.5 hours
- **Why read:** The foundational paper for parameter-efficient finetuning

**Key ideas:**
- Freeze base model weights
- Train low-rank decomposition matrices (A, B)
- Rank r controls capacity vs efficiency tradeoff

### 2. QLoRA: Efficient Finetuning of Quantized LLMs
- **Link:** https://arxiv.org/abs/2305.14314
- **Authors:** Dettmers et al.
- **Year:** 2023
- **Difficulty:** 4/5
- **Time:** 2 hours
- **Why read:** Makes finetuning accessible on consumer hardware

**Key innovations:**
- 4-bit NormalFloat quantization
- Double quantization
- Paged optimizers

### 3. Direct Preference Optimization (DPO)
- **Link:** https://arxiv.org/abs/2305.18290
- **Year:** 2023
- **Difficulty:** 4/5
- **Time:** 2 hours
- **Why read:** The practical alternative to RLHF

**Key insight:** Reformulates RLHF objective to avoid explicit reward modeling

---

## Practical Guides (Required)

### 4. Unsloth Finetuning Notebooks
- **Link:** https://github.com/unslothai/unsloth
- **Difficulty:** 2/5
- **Time:** 3 hours (hands-on)
- **Why read:** Fastest way to get hands-on experience

**Start with:**
- Llama 3 LoRA notebook
- DPO training notebook

### 5. How to Fine-tune LLMs in 2025 (Philipp Schmid)
- **Link:** https://www.philschmid.de/fine-tune-llms-in-2025
- **Difficulty:** 2/5
- **Time:** 1 hour
- **Why read:** Practical overview of the full process

### 6. HuggingFace TRL Documentation
- **Link:** https://huggingface.co/docs/trl/
- **Difficulty:** 3/5
- **Time:** 2 hours
- **Why read:** The standard library for RLHF/DPO training

---

## When to Finetune

### 7. When to Finetune vs Prompt (Various sources)
- Search for "when to finetune LLM vs prompt engineering"
- **Difficulty:** 2/5
- **Time:** 1 hour
- **Why read:** Avoid unnecessary finetuning

**Rules of thumb:**
- Prompting first, finetune if insufficient
- Finetune for: consistent style, domain terminology, specific formats
- Don't finetune for: general knowledge (use RAG), simple tasks

---

## Advanced (Optional)

### 8. FSDP + QLoRA (Answer.AI)
- **Link:** https://www.answer.ai/posts/2024-03-06-fsdp-qlora.html
- **Difficulty:** 5/5
- **Time:** 2 hours
- **Why read:** Distributed finetuning for larger models

### 9. ReFT: Representation Finetuning
- **Link:** https://arxiv.org/abs/2404.03592
- **Difficulty:** 4/5
- **Time:** 1.5 hours
- **Why read:** Alternative to weight-based finetuning

### 10. LoRA vs Full Finetuning Comparisons
- Search for empirical comparisons
- **Difficulty:** 3/5
- **Time:** 1 hour
- **Why read:** Understand the tradeoffs

---

## Reading Order

1. Philipp Schmid overview (#5) - Get the big picture
2. LoRA paper (#1) - Core technique
3. Unsloth notebooks (#4) - Get hands-on immediately
4. QLoRA paper (#2) - Understand memory optimization
5. DPO paper (#3) - Preference tuning
6. TRL docs (#6) - Reference during implementation

---

## XP Values

| Reading | XP |
|---------|-----|
| LoRA paper | +50 |
| QLoRA paper | +75 |
| DPO paper | +75 |
| Unsloth hands-on | +50 |
| TRL hands-on | +50 |
| Advanced papers | +50 each |

**Module completion bonus:** +200 XP
