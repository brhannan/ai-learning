# 6-Month Roadmap to Frontier AI Skills

This roadmap assumes 3-5 hours/week of focused study, scaling up during project phases.

---

## Phase 1: Foundations (Weeks 1-8)

**Goal:** Solid ML fundamentals and deep transformer understanding

### Week 1-2: ML Fundamentals
- [ ] Review backpropagation, gradient descent
- [ ] Optimization algorithms (SGD, Adam)
- [ ] Loss functions and regularization
- **Resource:** Deep Learning Book Ch. 6-8

### Week 3-4: Transformers Deep Dive
- [ ] Read "Attention Is All You Need" (annotated)
- [ ] Watch 3Blue1Brown attention visualization
- [ ] Read "The Illustrated Transformer" (Jay Alammar)
- **Critical:** Start Project 1 (Transformer from Scratch)

### Week 5-6: Transformer Implementation
- [ ] Implement multi-head attention
- [ ] Implement positional encoding
- [ ] Implement full transformer encoder
- [ ] Train on small dataset
- **Deliverable:** Working transformer, blog post draft

### Week 7-8: Scaling Laws
- [ ] Read Chinchilla paper
- [ ] Read Kaplan et al. scaling laws
- [ ] Understand compute-optimal training
- [ ] Complete Project 1 blog post

**Phase 1 Checkpoint:**
- [ ] Can explain attention mechanism from memory
- [ ] Have working transformer implementation
- [ ] Published blog post on your implementation

---

## Phase 2: Practical Skills (Weeks 9-16)

**Goal:** Hands-on experience with finetuning, evaluation, and inference

### Week 9-10: Finetuning Fundamentals
- [ ] LoRA paper (Low-Rank Adaptation)
- [ ] QLoRA paper and implementation
- [ ] Unsloth notebooks (hands-on)
- [ ] When to finetune vs prompt

### Week 11-12: Preference Tuning
- [ ] DPO paper (Direct Preference Optimization)
- [ ] RLHF vs DPO tradeoffs
- [ ] OpenAI preference finetuning docs
- **Critical:** Start Project 2 (Finetune a Model)

### Week 13-14: Evals & Benchmarks
- [ ] MMLU, MMLU-Pro papers
- [ ] IFEval (instruction following)
- [ ] LLM-as-Judge patterns
- [ ] Build your own eval suite
- **Resource:** Hamel Husain's LLM-as-Judge guide

### Week 15-16: Inference & Serving
- [ ] KV-cache and attention optimization
- [ ] FlashAttention paper
- [ ] vLLM architecture
- [ ] Quantization (INT8, INT4, GGUF)
- [ ] Complete Project 2

**Phase 2 Checkpoint:**
- [ ] Have finetuned a model with LoRA (Project 2)
- [ ] Can design an eval suite for a specific task
- [ ] Understand inference optimization tradeoffs

---

## Phase 3: Alignment & Safety (Weeks 17-24)

**Goal:** Deep understanding of alignment research

### Week 17-18: RLHF Fundamentals
- [ ] InstructGPT paper (OpenAI)
- [ ] PPO algorithm deep dive
- [ ] Reward modeling
- [ ] Failure modes (reward hacking)

### Week 19-20: Constitutional AI
- [ ] Constitutional AI paper (MUST READ)
- [ ] RLAIF vs RLHF comparison
- [ ] Collective Constitutional AI paper
- [ ] Anthropic's approach to scalable oversight
- **Critical:** Start Project 3 (Mini-RLHF or CAI experiment)

### Week 21-22: Interpretability
- [ ] Probing classifiers basics
- [ ] Mechanistic interpretability intro
- [ ] "Scaling Monosemanticity" paper
- [ ] TransformerLens hands-on
- **Critical:** Start Project 4 (Interpretability)

### Week 23-24: Alignment Research
- [ ] Sleeper Agents paper
- [ ] Sycophancy research
- [ ] Alignment faking
- [ ] Current open problems
- [ ] Complete Projects 3 & 4

**Phase 3 Checkpoint:**
- [ ] Can discuss CAI vs RLHF fluently
- [ ] Have RLHF or CAI experiment (Project 3)
- [ ] Have interpretability experiment (Project 4)
- [ ] Can name 5+ alignment papers and explain their contributions

---

## Phase 4: Applications (Weeks 25-32)

**Goal:** Build practical AI systems

### Week 25-26: Prompting & ICL
- [ ] Chain-of-Thought paper
- [ ] Tree of Thoughts
- [ ] DSPy framework
- [ ] Prompt optimization techniques

### Week 27-28: RAG Systems
- [ ] Original RAG paper
- [ ] MTEB benchmark (embeddings)
- [ ] ColBERT and late interaction
- [ ] Self-RAG, GraphRAG

### Week 29-30: Agents & Tool Use
- [ ] ReAct paper
- [ ] Toolformer paper
- [ ] Anthropic's "Building Effective Agents"
- [ ] MemGPT (memory management)
- **Critical:** Start Project 5 (Agent or RAG system)

### Week 31-32: Code Generation
- [ ] HumanEval benchmark
- [ ] SWE-Bench paper
- [ ] SWE-Agent architecture
- [ ] The Stack dataset
- [ ] AlphaCodeium (flow engineering)
- [ ] Complete Project 5

**Phase 4 Checkpoint:**
- [ ] Have working agent or RAG system (Project 5)
- [ ] Understand coding agent architectures
- [ ] Can evaluate code generation quality

---

## Phase 5: Mastery (Weeks 33-36)

**Goal:** Mastery demonstrated through portfolio

### Week 33-34: System Design
- [ ] ML system design patterns
- [ ] Practice 3+ design problems
- [ ] Read Chip Huyen's book
- [ ] Red-teaming methodology

### Week 35-36: Capstone
- [ ] Complete Project 6 (Capstone)
- [ ] Polish portfolio
- [ ] Write AI safety perspective essay
- [ ] Technical blog with 3+ posts

**Final Checkpoint:**
- [ ] 6 portfolio projects on GitHub
- [ ] Technical blog with 3+ posts
- [ ] Clear perspective on AI safety
- [ ] Can discuss system design confidently

---

## Weekly Rhythm

**Recommended Schedule (4 hours/week):**

| Day | Activity | Time |
|-----|----------|------|
| Mon | Read paper/blog | 1 hr |
| Wed | Implementation/coding | 1.5 hr |
| Sat | Review + exercises | 1.5 hr |

**During Project Phases:** Scale to 6-8 hours/week

---

## Milestones

| Week | Milestone |
|------|-----------|
| 8 | Project 1 complete (Transformer) |
| 16 | Project 2 complete (Finetuning), Phase 2 done |
| 20 | Project 3 complete (RLHF/CAI) |
| 24 | Project 4 complete (Interpretability), Phase 3 done |
| 32 | Project 5 complete (Agent/RAG), Phase 4 done |
| 36 | Project 6 complete (Capstone), DONE |

---

## Adjustments

- **Already strong on foundations?** Start at Phase 2 or 3
- **Limited time?** Focus on Phase 2 (Practical) + Phase 3 (Alignment)
- **Want to go faster?** Add 2-3 hours/week, compress to 4 months
- **More practitioner focus?** Spend extra time on Phase 2 & 4

---

*Track your progress with `ai-learn progress`. Don't break the chain.*
