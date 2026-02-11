# Module 02: Transformers Deep Dive

**Phase:** 1 - Foundations
**Priority:** CRITICAL (must implement, not just read)
**Estimated Time:** 15-20 hours (including implementation)

## Overview

The transformer architecture is the foundation of all modern LLMs. You cannot work on AI systems without deep, implementation-level understanding of how attention works.

**Important:** Reading the paper is not enough. You must implement a transformer from scratch.

## Learning Objectives

By the end of this module, you should be able to:

1. Explain self-attention mathematically (Q, K, V matrices)
2. Implement multi-head attention from scratch
3. Explain why positional encoding is needed and implement it
4. Build a complete transformer encoder
5. Train a small transformer on a toy task
6. Debug attention weights visually

## Key Concepts

- **Self-attention**: Allowing each token to "look at" all other tokens
- **Query, Key, Value**: The three projections that enable attention
- **Multi-head attention**: Running attention in parallel subspaces
- **Positional encoding**: Injecting sequence order information
- **Layer normalization**: Stabilizing training
- **Residual connections**: Enabling deep networks

## Why This Matters

- Every LLM (GPT, Claude, LLaMA) is built on this architecture
- Quiz questions often probe attention understanding
- Debugging and optimizing models requires this knowledge
- FlashAttention and other optimizations require understanding the baseline

## Prerequisites

- Linear algebra (matrix multiplication, softmax)
- PyTorch or JAX basics
- Backpropagation understanding

## Readings

See [readings.md](readings.md) for the complete reading list.

## Implementation Project

This module connects directly to [Project 1: Transformer from Scratch](../../projects/01-transformer-scratch/).

Your implementation should include:
1. Scaled dot-product attention
2. Multi-head attention wrapper
3. Positional encoding (sinusoidal or learned)
4. Transformer encoder block
5. Full transformer encoder
6. Training on a small task (character-level Shakespeare, simple classification)

## Exercises

1. **Attention visualization**: Plot attention weights for a sample sequence
2. **Ablation study**: What happens without positional encoding?
3. **Head analysis**: Do different heads learn different patterns?
4. **Efficiency calculation**: Calculate FLOPs for different sequence lengths

## Quiz Prep

Common quiz questions on transformers:
- Walk me through how attention works
- Why scaled dot-product? Why not just dot-product?
- What's the computational complexity of self-attention?
- How does positional encoding work? What are alternatives?
- Why layer norm instead of batch norm?

## Time Breakdown

| Activity | Hours |
|----------|-------|
| Read papers/blogs | 4-5 |
| Understand implementation | 3-4 |
| Implement from scratch | 6-8 |
| Debug and experiment | 2-3 |
| **Total** | **15-20** |
