# Module 04: Finetuning

## Overview

Learn when and how to finetune language models, from parameter-efficient methods (LoRA) to preference optimization (DPO).

## Learning Objectives

By the end of this module, you should be able to:

1. Explain when finetuning is appropriate vs prompting
2. Implement LoRA/QLoRA finetuning on a small model
3. Understand DPO and preference-based training
4. Evaluate a finetuned model properly

## Key Concepts

- **LoRA (Low-Rank Adaptation)**: Train small adapter matrices instead of full weights
- **QLoRA**: Quantized base model + LoRA for memory efficiency
- **DPO (Direct Preference Optimization)**: Preference tuning without RL
- **When to finetune**: Task-specific behavior, style, domain knowledge

## Prerequisites

- Completed Module 02 (Transformers)
- Comfortable with PyTorch
- Access to GPU (Colab works)

## Time Estimate

- Readings: 6-8 hours
- Hands-on: 8-10 hours
- Project: 10-15 hours

## Project Connection

This module feeds directly into **Project 2: Finetune a Model**.

See [readings.md](readings.md) for the full reading list.
