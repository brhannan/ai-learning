# Project 4: Agent Framework

**Phase:** 4 - Agents & Applications
**Estimated Time:** 20-25 hours
**Difficulty:** Medium-Hard
**XP on Completion:** +600 XP

## Overview

Build your own agent framework that can use tools, reason about actions, and complete multi-step tasks. This is directly relevant to what Anthropic builds with Claude.

## Why This Project Matters

- **Hot area**: Agents are the frontier of applied AI
- **Claude relevance**: Claude Code is an agent—you're using one now
- **Practical skills**: Agent engineering is in high demand
- **Portfolio piece**: A working agent is impressive

## Objectives

By the end of this project, you should have:

1. [ ] Implemented the ReAct pattern from scratch
2. [ ] Built a tool calling system with schema validation
3. [ ] Created at least 5 different tools
4. [ ] Implemented error handling and retry logic
5. [ ] Added basic memory/context management
6. [ ] Built an evaluation harness
7. [ ] Documented the architecture
8. [ ] Demonstrated on 3+ real tasks

## Technical Requirements

### Core Components

1. **Agent Loop**: Thought → Action → Observation cycle
2. **Tool Registry**: Register tools with schemas
3. **Tool Executor**: Execute tools and handle errors
4. **Memory**: Track conversation and past actions
5. **Orchestrator**: Manage the overall flow

### Required Tools (implement at least 5)
- Web search (mock or real API)
- Calculator
- Code execution (sandboxed)
- File reader
- API caller
- Current date/time
- Note taking

### Model Backend
- Use OpenAI API, Anthropic API, or local model
- Must work with any model that supports function calling

## Suggested Architecture

```
AgentFramework/
├── agent/
│   ├── core.py          # Main agent loop
│   ├── memory.py        # Context management
│   └── planner.py       # High-level planning
├── tools/
│   ├── base.py          # Tool base class
│   ├── search.py        # Web search tool
│   ├── calculator.py    # Math tool
│   ├── code.py          # Code execution
│   └── registry.py      # Tool registration
├── evaluation/
│   ├── tasks.py         # Eval task definitions
│   ├── runner.py        # Run evaluations
│   └── metrics.py       # Success metrics
└── examples/
    ├── research.py      # Research task demo
    ├── coding.py        # Coding task demo
    └── planning.py      # Planning task demo
```

## Suggested Approach

### Week 1: Core Loop
1. Implement basic ReAct loop
2. Add tool base class and registry
3. Create 2-3 simple tools
4. Test with simple tasks

### Week 2: Tools & Error Handling
1. Add more tools
2. Implement error handling
3. Add retry logic
4. Handle tool failures gracefully

### Week 3: Memory & Evaluation
1. Add conversation memory
2. Implement context window management
3. Build evaluation harness
4. Create test tasks

### Week 4: Polish & Demo
1. Clean up code
2. Add documentation
3. Create demo examples
4. Write project report

## Resources

### Papers
- [ReAct Paper](https://arxiv.org/abs/2210.03629)
- [Toolformer](https://arxiv.org/abs/2302.04761)
- [Cognitive Architectures Survey](https://arxiv.org/abs/2309.02427)

### Frameworks (for inspiration, don't just copy)
- LangChain/LangGraph
- AutoGPT
- BabyAGI

### APIs
- [Anthropic Tool Use](https://docs.anthropic.com/claude/docs/tool-use)
- [OpenAI Function Calling](https://platform.openai.com/docs/guides/function-calling)

## Evaluation Rubric

| Criterion | Points |
|-----------|--------|
| ReAct implementation | 20 |
| Tool system design | 15 |
| Number and quality of tools | 15 |
| Error handling | 15 |
| Memory/context management | 10 |
| Evaluation framework | 10 |
| Code quality & docs | 10 |
| Demo tasks | 5 |
| **Total** | **100** |

## Deliverables

1. **Code**: Agent framework in a Git repo
2. **Tools**: At least 5 working tools
3. **Evaluation**: Harness and results on test tasks
4. **Demo**: 3+ example tasks with logs
5. **Documentation**: Architecture and usage docs

## Stretch Goals

- Multi-agent collaboration
- Long-term memory with vector DB
- Human-in-the-loop for uncertain actions
- Streaming output
- Web UI for interaction

## Quiz Prep

After completing this project, you should be able to:
- Explain the ReAct pattern in detail
- Discuss agent failure modes
- Compare agent architectures
- Design a tool schema for new capabilities
