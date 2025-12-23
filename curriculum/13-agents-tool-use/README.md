# Module 13: Agents & Tool Use

**Phase:** 4 - Agents & Applications
**Priority:** HIGH (User's stated interest)
**Estimated Time:** 12-15 hours

## Overview

Agents are LLMs that can take actions in the world—calling APIs, browsing the web, writing code, and more. This module covers the core patterns and architectures for building agentic systems.

## Learning Objectives

By the end of this module, you should be able to:

1. Explain the ReAct (Reasoning + Acting) pattern
2. Implement function calling / tool use
3. Design agent memory systems (short and long term)
4. Handle tool failures and error recovery
5. Build multi-step reasoning pipelines
6. Evaluate agent performance

## Key Concepts

- **ReAct**: Interleaving reasoning traces with actions
- **Function calling**: Structured tool invocation
- **Tool schemas**: Describing tools to models
- **Orchestration**: Managing multi-step agent workflows
- **Memory**: Context management across interactions
- **Grounding**: Keeping agents connected to reality

## Why This Matters

- Agents are the frontier of applied LLM work
- Claude Code (this tool) is an agent
- Anthropic is investing heavily in agent capabilities
- Many job opportunities in this space

## Prerequisites

- [11-prompting-advanced](../11-prompting-advanced/) - Chain-of-thought and reasoning
- [04-llm-architectures](../04-llm-architectures/) - Understanding model capabilities

## Readings

See [readings.md](readings.md) for the complete reading list.

## Implementation Focus

This module connects to [Project 4: Agent Framework](../../projects/04-agent-framework/).

Key implementation milestones:
1. Simple function calling wrapper
2. ReAct agent with thought/action/observation loop
3. Tool error handling and retry logic
4. Basic memory system
5. Evaluation harness

## Exercises

1. **Implement ReAct**: Build a minimal ReAct agent from scratch
2. **Tool design**: Design tool schemas for 5 different capabilities
3. **Error analysis**: What happens when tools fail? Document failure modes
4. **Benchmark**: Evaluate your agent on a simple task suite

## Discussion Questions

- How do you know when an agent is "done"?
- What are the risks of giving agents real-world capabilities?
- How do you evaluate agent reliability?
- When should an agent ask for human help?

## Real-World Examples

- Claude Code (Anthropic)
- GitHub Copilot Workspace
- Devin (Cognition)
- AutoGPT, BabyAGI
- SWE-Agent
