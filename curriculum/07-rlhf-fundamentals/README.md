# Module 07: RLHF Fundamentals

**Phase:** 3 - Alignment & Safety
**Priority:** CRITICAL (Foundation for Constitutional AI)
**Estimated Time:** 10-12 hours

## Overview

Reinforcement Learning from Human Feedback (RLHF) is the technique that made ChatGPT and Claude helpful. Understanding RLHF is essential before diving into Constitutional AI.

## Learning Objectives

By the end of this module, you should be able to:

1. Explain the three phases of RLHF training
2. Describe how reward models are trained
3. Understand PPO and its role in RLHF
4. Identify failure modes (reward hacking, mode collapse)
5. Compare RLHF to alternatives like DPO
6. Discuss the limitations of human feedback

## Key Concepts

- **Reward Model**: Predicts human preferences for model outputs
- **PPO (Proximal Policy Optimization)**: The RL algorithm used
- **KL Divergence Penalty**: Prevents model from diverging too far
- **Reward Hacking**: Model exploits reward signal without achieving goal
- **Preference Data**: Human comparisons of output pairs

## The Three Phases

1. **Supervised Fine-Tuning (SFT)**: Train on human demonstrations
2. **Reward Modeling (RM)**: Train a model to predict human preferences
3. **RL Fine-Tuning**: Optimize policy using reward model

## Why This Matters

- RLHF is how all major assistants (Claude, ChatGPT) are trained
- Understanding RLHF is prerequisite for Constitutional AI
- Knowing failure modes helps you understand alignment challenges
- This is core knowledge for any AI safety role

## Prerequisites

- [01-ml-fundamentals](../01-ml-fundamentals/) - Optimization basics
- [02-transformers-deep](../02-transformers-deep/) - Model architecture

## Readings

See [readings.md](readings.md) for the complete reading list.

## Exercises

1. **Preference data**: Create 10 preference pairs for a simple task
2. **Reward hacking**: Describe 3 ways a model might hack a reward signal
3. **RLHF vs DPO**: Write a comparison essay (500 words)
4. **Failure modes**: List 5 ways human feedback can go wrong

## Connection to Projects

This module directly informs [Project 2: Mini-RLHF](../../projects/02-rlhf-mini/).

## Discussion Questions

- Why not just train on more demonstrations?
- What makes human feedback unreliable?
- How do you scale RLHF to more complex tasks?
- Why use RL at all? (Hint: see DPO paper)
