# Module 08: Constitutional AI

**Phase:** 3 - Alignment & Safety
**Priority:** CRITICAL (Anthropic's core approach)
**Estimated Time:** 8-10 hours

## Overview

Constitutional AI (CAI) is Anthropic's foundational approach to AI alignment. Understanding CAI deeply is non-negotiable for anyone serious about working at Anthropic.

## Learning Objectives

By the end of this module, you should be able to:

1. Explain how Constitutional AI differs from standard RLHF
2. Describe the two-phase CAI training process (SL-CAI and RL-CAI)
3. Understand RLAIF (RL from AI Feedback) and its tradeoffs
4. Discuss scalable oversight and why it matters
5. Explain Collective Constitutional AI and democratic input

## Key Concepts

- **Constitution**: A set of principles that guide AI behavior
- **Self-critique and revision**: Model critiques and improves its own outputs
- **RLAIF**: Using AI feedback instead of human labels
- **Scalable oversight**: Aligning AI without requiring human review of every output
- **Harmlessness vs helpfulness tradeoff**

## Why This Matters for Anthropic

- CAI is the foundation of how Claude is trained
- Shows Anthropic's approach to the alignment problem
- Demonstrates scalable methods that don't require massive human labeling
- Connects to broader questions of AI governance and values

## Prerequisites

- [07-rlhf-fundamentals](../07-rlhf-fundamentals/) - Understand standard RLHF first
- Basic understanding of preference learning

## Readings

See [readings.md](readings.md) for the complete reading list.

## Exercises

1. **Compare CAI to RLHF**: Write a 500-word essay comparing the two approaches
2. **Draft a constitution**: Write 10 principles you would include in an AI constitution
3. **Analyze failure modes**: What could go wrong with CAI? List 5 potential issues
4. **Read the Claude system prompt**: Identify which principles likely came from CAI

## Discussion Questions

- Why might AI feedback be more scalable than human feedback?
- What are the risks of having AI systems critique themselves?
- How do you decide what goes into a constitution?
- Could CAI lead to models that are too restrictive?

## Connection to Projects

This module directly informs [Project 2: Mini-RLHF](../../projects/02-rlhf-mini/), where you'll implement preference learning (though not full CAI due to compute constraints).
