# AI Learning Curriculum

**Goal: Develop frontier AI engineering skills at Anthropic's level**

This is not a casual reading list. It's a rigorous 6-month program designed to build the skills needed to work on frontier AI systems, with emphasis on safety, alignment, and practical engineering.

## Philosophy

> "You do not rise to the level of your goals. You fall to the level of your systems."
> — James Clear, Atomic Habits

This curriculum is built around systems, not just goals:
- **Daily habits** over cramming
- **Implementation projects** over passive reading
- **Portfolio artifacts** over certificates
- **Spaced repetition** over one-time exposure

## Quick Start

```bash
# Install the CLI tracker
cd tracker && pip install -e .

# See what to read next
ai-learn next

# Log a completed reading
ai-learn log "Attention Is All You Need"

# Check your streak
ai-learn streak

# View overall progress
ai-learn progress
```

## Structure

```
curriculum/           # Learning modules across 5 phases
projects/             # 6 portfolio projects (implementation required)
interview-prep/       # Technical interview preparation
tracker/              # CLI habit tracker with XP and achievements
```

## The 5 Phases

| Phase | Focus | Modules |
|-------|-------|---------|
| 1 | Foundations | ML fundamentals, Transformers (implement!), Scaling laws |
| 2 | Practical Skills | Finetuning (LoRA/DPO), Evals & Benchmarks, Inference |
| 3 | Alignment & Safety | RLHF, Constitutional AI, Interpretability |
| 4 | Applications | Prompting, RAG, Agents & Tool use, Code Generation |
| 5 | Mastery | System design, Capstone project |

See [ROADMAP.md](ROADMAP.md) for the detailed 6-month path.

## Why Anthropic as a Benchmark?

This curriculum uses Anthropic's engineering standards as a benchmark because:

1. **They value "direct evidence of ability"** — Portfolio projects > credentials
2. **Safety-first thinking** — Their core research areas define the frontier
3. **Implementation matters** — Build, not just read
4. **Constitutional AI is central** — Deep understanding of alignment approaches

## Success Metrics

By completion, you should be able to:

- [ ] Explain transformer architecture at whiteboard level
- [ ] Implement attention mechanism from memory
- [ ] Finetune a model with LoRA and evaluate it properly
- [ ] Discuss Constitutional AI vs RLHF tradeoffs fluently
- [ ] Build and evaluate a coding agent on SWE-Bench
- [ ] Have 3+ portfolio projects on GitHub
- [ ] Articulate your perspective on AI safety clearly
- [ ] Complete ML system design problems confidently

## Identity Statement

> "I am someone who learns AI every day."

This is your new identity. The habit tracker, the streak counter, the XP system—they all reinforce this identity with every small action.

## Getting Started

1. Read the [ROADMAP.md](ROADMAP.md) to understand the 6-month journey
2. Start with [curriculum/01-ml-fundamentals](curriculum/01-ml-fundamentals/) or skip to where you're comfortable
3. Use `ai-learn next` to always know what's next
4. Never break the chain

## Resources

- [Anthropic Research](https://www.anthropic.com/research)
- [Alignment Science Blog](https://alignment.anthropic.com/)
- [Latent Space 2025 Reading List](https://www.latent.space/p/2025-papers)
- [Constitutional AI Paper](https://arxiv.org/abs/2212.08073)

---

*This curriculum uses Anthropic's engineering standards as a benchmark. It emphasizes the skills they value: deep technical understanding, safety-first thinking, and demonstrated ability through projects.*
