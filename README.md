# AI Learning Curriculum

**Goal: Become qualified for a frontier AI engineering role at Anthropic**

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
curriculum/           # 17 learning modules across 5 phases
projects/             # 6 portfolio projects (implementation required)
interview-prep/       # Anthropic-specific interview preparation
tracker/              # CLI habit tracker with XP and achievements
```

## The 5 Phases

| Phase | Focus | Modules |
|-------|-------|---------|
| 1 | Foundations | ML fundamentals, Transformers (implement!), Scaling laws |
| 2 | LLM Engineering | Architectures, Training infra, Inference serving |
| 3 | Alignment & Safety | RLHF, Constitutional AI, Interpretability |
| 4 | Agents & Applications | Prompting, RAG, Tool use, Coding agents |
| 5 | Mastery & Portfolio | System design, Evals, Capstone project |

See [ROADMAP.md](ROADMAP.md) for the detailed 6-month path.

## Why Anthropic?

This curriculum is specifically designed for Anthropic because:

1. **They value "direct evidence of ability"** — Portfolio projects > credentials
2. **Safety-first thinking** — Phase 3 covers their core research areas
3. **Implementation matters** — You'll build, not just read
4. **Constitutional AI is central** — Deep understanding of their approach

## Success Metrics

By completion, you should be able to:

- [ ] Explain transformer architecture at whiteboard level
- [ ] Implement attention mechanism from memory
- [ ] Discuss Constitutional AI vs RLHF tradeoffs fluently
- [ ] Describe 3+ Anthropic papers in detail
- [ ] Have 3+ portfolio projects on GitHub
- [ ] Write a compelling "Why Anthropic" that's specific
- [ ] Complete ML system design interviews confidently

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

*This curriculum was designed with the goal of qualifying for Anthropic's engineering team. It emphasizes the skills they value: deep technical understanding, safety-first thinking, and demonstrated ability through projects.*
