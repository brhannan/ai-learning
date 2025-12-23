# 6-Month Roadmap to Anthropic-Ready

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

## Phase 2: LLM Engineering (Weeks 9-14)

**Goal:** Understand how large models are built and served

### Week 9-10: LLM Architectures
- [ ] GPT-2, GPT-3 papers
- [ ] LLaMA 1/2/3 series
- [ ] Claude model cards (public documentation)
- [ ] Architectural differences and tradeoffs

### Week 11-12: Training Infrastructure
- [ ] Distributed training basics
- [ ] FSDP, DeepSpeed concepts
- [ ] Mixed precision training
- [ ] Understand training at scale

### Week 13-14: Inference & Serving
- [ ] KV-cache and attention optimization
- [ ] FlashAttention paper
- [ ] vLLM architecture
- [ ] Quantization techniques (INT8, INT4)

**Phase 2 Checkpoint:**
- [ ] Can discuss tradeoffs between model architectures
- [ ] Understand scaling challenges
- [ ] Know optimization techniques for inference

---

## Phase 3: Alignment & Safety (Weeks 15-22)

**Goal:** Deep understanding of Anthropic's core research areas

### Week 15-16: RLHF Fundamentals
- [ ] InstructGPT paper (OpenAI)
- [ ] PPO algorithm deep dive
- [ ] Reward modeling
- [ ] Failure modes (reward hacking)

### Week 17-18: Constitutional AI
- [ ] Constitutional AI paper (MUST READ)
- [ ] RLAIF vs RLHF comparison
- [ ] Collective Constitutional AI paper
- [ ] Anthropic's approach to scalable oversight
- **Critical:** Start Project 2 (Mini-RLHF)

### Week 19-20: Interpretability
- [ ] Probing classifiers basics
- [ ] Mechanistic interpretability intro
- [ ] "Scaling Monosemanticity" paper
- [ ] Features in Claude
- **Critical:** Start Project 3 (Interpretability)

### Week 21-22: Alignment Research
- [ ] Sleeper Agents paper
- [ ] Sycophancy research
- [ ] Alignment faking
- [ ] Current open problems

**Phase 3 Checkpoint:**
- [ ] Can discuss CAI vs RLHF fluently
- [ ] Have working RLHF implementation (Project 2)
- [ ] Have interpretability experiment (Project 3)
- [ ] Can name 5+ Anthropic papers and explain their contributions

---

## Phase 4: Agents & Applications (Weeks 23-30)

**Goal:** Build practical agentic systems

### Week 23-24: Advanced Prompting
- [ ] Chain-of-Thought paper
- [ ] Tree of Thoughts
- [ ] DSPy framework
- [ ] Prompt optimization techniques

### Week 25-26: RAG Systems
- [ ] Embedding models (MTEB benchmark)
- [ ] Vector databases
- [ ] ColBERT and late interaction
- [ ] GraphRAG

### Week 27-28: Agents & Tool Use
- [ ] ReAct paper
- [ ] Toolformer
- [ ] Function calling architectures
- [ ] Memory management
- **Critical:** Start Project 4 (Agent Framework)

### Week 29-30: Coding Agents
- [ ] SWE-Bench paper
- [ ] SWE-Agent architecture
- [ ] Code generation evaluation
- [ ] Complete Project 4

**Phase 4 Checkpoint:**
- [ ] Have working agent framework (Project 4)
- [ ] Understand RAG tradeoffs
- [ ] Can implement ReAct pattern from scratch

---

## Phase 5: Mastery & Portfolio (Weeks 31-36)

**Goal:** Interview-ready with strong portfolio

### Week 31-32: System Design
- [ ] ML system design patterns
- [ ] Practice 3+ design problems
- [ ] Read Chip Huyen's book
- **Critical:** Start Project 5 (Eval Suite)

### Week 33-34: Evals & Red-teaming
- [ ] Benchmark design principles
- [ ] Red-teaming methodology
- [ ] Complete Project 5
- [ ] Review failure modes

### Week 35-36: Capstone & Interview Prep
- [ ] Complete Project 6 (Capstone)
- [ ] Polish portfolio
- [ ] Write "Why Anthropic" essay
- [ ] Practice paper discussions
- [ ] Mock interviews

**Final Checkpoint:**
- [ ] 6 portfolio projects on GitHub
- [ ] Technical blog with 3+ posts
- [ ] Prepared "Why Anthropic" narrative
- [ ] Ready for system design interviews
- [ ] Ready for paper discussion interviews

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
| 14 | Phase 2 complete |
| 18 | Project 2 complete (RLHF) |
| 22 | Project 3 complete (Interpretability), Phase 3 done |
| 30 | Project 4 complete (Agents), Phase 4 done |
| 34 | Project 5 complete (Evals) |
| 36 | Project 6 complete (Capstone), READY |

---

## Adjustments

- **Already strong on foundations?** Start at Phase 2 or 3
- **Limited time?** Focus on Phase 3 (Alignment) and one project
- **Want to go faster?** Add 2-3 hours/week, compress to 4 months
- **Got stuck?** Ask in the Anthropic discord or ML communities

---

*Track your progress with `ai-learn progress`. Don't break the chain.*
