# Project 5: Evaluation Suite

**Phase:** 5 - Mastery & Portfolio
**Estimated Time:** 15-20 hours
**Difficulty:** Medium
**XP on Completion:** +500 XP

## Overview

Build an evaluation suite for a specific LLM capability. Design tasks, implement metrics, run models, and analyze results. This builds crucial skills for AI safety work.

## Why This Project Matters

- **Safety critical**: Evals are how we know if models are safe
- **Anthropic focus**: They take evaluation very seriously
- **Practical skill**: Every AI org needs eval infrastructure
- **Research taste**: Designing good evals is an art

## Objectives

By the end of this project, you should have:

1. [ ] Chosen a capability to evaluate
2. [ ] Designed 20+ evaluation tasks
3. [ ] Implemented automated scoring
4. [ ] Run at least 2 different models
5. [ ] Analyzed results and failure modes
6. [ ] Documented methodology
7. [ ] Published benchmark and results

## Capability Ideas

Choose ONE to focus on:
- **Instruction following**: Does the model follow complex instructions?
- **Truthfulness**: Does the model state accurate facts?
- **Reasoning**: Can the model solve logic problems?
- **Safety**: Does the model refuse harmful requests?
- **Coding**: Can the model write correct code?
- **Tool use**: Can the model use tools effectively?

## Technical Requirements

### Evaluation Framework
- Clear task format (prompt → expected response)
- Automated scoring (exact match, LLM-as-judge, etc.)
- Result logging and analysis
- Reproducibility (seeds, versions)

### Dataset
- At least 20 tasks (50+ preferred)
- Clear labeling/annotation
- Diverse difficulty levels
- Documented creation process

## Suggested Approach

### Week 1: Design
1. Choose capability to evaluate
2. Research existing evals in this area
3. Design task format
4. Create initial tasks (10-20)

### Week 2: Implementation
1. Build evaluation harness
2. Implement scoring functions
3. Add logging and analysis
4. Test with one model

### Week 3: Expansion & Running
1. Expand to 50+ tasks
2. Run multiple models
3. Collect results
4. Identify failure modes

### Week 4: Analysis & Write-up
1. Analyze results
2. Create visualizations
3. Document methodology
4. Write report

## Resources

### Papers
- [HELM Benchmark](https://arxiv.org/abs/2211.09110)
- [MMLU](https://arxiv.org/abs/2009.03300)
- [TruthfulQA](https://arxiv.org/abs/2109.07958)
- [BIG-Bench](https://arxiv.org/abs/2206.04615)

### Existing Frameworks
- LM Evaluation Harness
- HELM
- Anthropic's eval approaches

## Evaluation Rubric

| Criterion | Points |
|-----------|--------|
| Task quality and diversity | 25 |
| Evaluation framework | 20 |
| Scoring methodology | 15 |
| Analysis depth | 20 |
| Reproducibility | 10 |
| Documentation | 10 |
| **Total** | **100** |

## Deliverables

1. **Dataset**: 20+ evaluation tasks with labels
2. **Code**: Evaluation harness
3. **Results**: Model performance data
4. **Analysis**: Failure mode documentation
5. **Report**: Methodology and findings

## Stretch Goals

- Red-teaming component
- Multi-model comparison
- Difficulty calibration
- Public leaderboard

## Interview Prep

After completing this project, you should be able to:
- Design evaluations for novel capabilities
- Discuss eval methodology tradeoffs
- Explain why LLM-as-judge works (and when it fails)
- Propose eval approaches for safety properties
