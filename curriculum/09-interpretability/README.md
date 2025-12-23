# Module 09: Interpretability

**Phase:** 3 - Alignment & Safety
**Priority:** HIGH (Anthropic's major research focus)
**Estimated Time:** 12-15 hours

## Overview

Interpretability is about understanding what's happening inside neural networks. Anthropic has made breakthrough contributions here, including the "Scaling Monosemanticity" work that found interpretable features in Claude.

## Learning Objectives

By the end of this module, you should be able to:

1. Explain the difference between mechanistic and behavioral interpretability
2. Implement probing classifiers on model activations
3. Understand the concept of "features" and "circuits"
4. Describe Anthropic's monosemanticity findings
5. Discuss why interpretability matters for AI safety
6. Design a simple interpretability experiment

## Key Concepts

- **Probing**: Training classifiers on hidden activations to find representations
- **Circuits**: Computational subgraphs that implement specific behaviors
- **Superposition**: Models encoding more features than they have dimensions
- **Monosemanticity**: Individual neurons representing single, interpretable concepts
- **Sparse autoencoders**: Technique to find interpretable directions
- **Feature visualization**: Understanding what activates neurons

## Why This Matters for Anthropic

- Anthropic has a dedicated interpretability team
- "Scaling Monosemanticity" was a major breakthrough
- Understanding models is key to aligning them
- Safety requires knowing what models are "thinking"

## Prerequisites

- [02-transformers-deep](../02-transformers-deep/) - Know the architecture
- [07-rlhf-fundamentals](../07-rlhf-fundamentals/) - Context for why we care

## Readings

See [readings.md](readings.md) for the complete reading list.

## Exercises

1. **Probing experiment**: Train a probing classifier to detect sentiment in GPT-2 activations
2. **Attention analysis**: Visualize attention patterns for specific behaviors
3. **Feature hunt**: Find neurons in a small model that activate for specific concepts
4. **Write-up**: Summarize Anthropic's monosemanticity findings in your own words

## Connection to Projects

This module directly connects to [Project 3: Interpretability Experiment](../../projects/03-interpretability/).

## Discussion Questions

- If we find interpretable features, does that mean the model is "safe"?
- What are the limitations of probing classifiers?
- Could interpretability research make models more dangerous?
- How would you scale interpretability to larger models?

## Resources Beyond Papers

- **TransformerLens**: Library for mechanistic interpretability
- **Neuronpedia**: Visualization of Claude's features
- **ARENA**: Structured exercises on interpretability
