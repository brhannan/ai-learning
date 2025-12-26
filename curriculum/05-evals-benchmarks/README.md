# Module 05: Evals & Benchmarks

## Overview

Learn how to evaluate language models properly—from standard benchmarks to custom evals for your specific use case.

## Learning Objectives

By the end of this module, you should be able to:

1. Understand major LLM benchmarks and what they measure
2. Design custom evals for specific tasks
3. Implement LLM-as-Judge evaluation
4. Avoid common eval pitfalls (contamination, gaming)

## Key Concepts

- **MMLU/MMLU-Pro**: Knowledge benchmarks across domains
- **IFEval**: Instruction following evaluation
- **LLM-as-Judge**: Using models to evaluate models
- **Contamination**: When test data leaks into training
- **Benchmark saturation**: When benchmarks stop being useful

## Prerequisites

- Completed Module 02 (Transformers)
- Basic statistics knowledge
- Python proficiency

## Time Estimate

- Readings: 5-7 hours
- Hands-on: 6-8 hours
- Project work: integrated into Project 2

## Why This Matters

> "If you can't measure it, you can't improve it."

Bad evals lead to bad models. Understanding evaluation is essential for:
- Knowing when your finetuning actually helped
- Comparing models fairly
- Building products that work reliably

See [readings.md](readings.md) for the full reading list.
