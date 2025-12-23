# Project 2: Mini-RLHF Pipeline

**Phase:** 3 - Alignment & Safety
**Estimated Time:** 20-30 hours
**Difficulty:** Hard
**XP on Completion:** +750 XP

## Overview

Implement a minimal RLHF pipeline: train a reward model on preferences, then fine-tune a language model using that reward. This gives hands-on experience with the core alignment technique.

## Why This Project Matters

- **Core alignment technique**: RLHF is how Claude and GPT are trained
- **Anthropic relevance**: Deep understanding of what CAI builds upon
- **Rare skill**: Few people have actually implemented RLHF
- **Interview differentiator**: "I built an RLHF pipeline" stands out

## Objectives

By the end of this project, you should have:

1. [ ] Fine-tuned a small base model (SFT phase)
2. [ ] Collected or used existing preference data
3. [ ] Trained a reward model
4. [ ] Implemented PPO (or used a library)
5. [ ] Fine-tuned with RL using reward signal
6. [ ] Compared SFT-only vs RLHF results
7. [ ] Documented failure modes observed
8. [ ] Written a report/blog post

## Technical Requirements

### Model Choice
Use a small model due to compute constraints:
- GPT-2 (124M)
- Pythia-70M or Pythia-160M
- TinyLlama

### Framework Options
- **TRL (HuggingFace)**: Recommended for beginners
- **Pure PyTorch**: Harder but more educational
- **trlX**: Alternative library

### Compute Requirements
- Can run on free Colab (with small models)
- Better with A100 or similar
- Expect 10-20 hours of training time total

## Suggested Approach

### Phase 1: Supervised Fine-Tuning (5-8 hours)
1. Choose a small task (summarization, helpfulness)
2. Get demonstration data (use existing or create)
3. Fine-tune base model on demonstrations
4. Evaluate SFT model

### Phase 2: Reward Modeling (8-10 hours)
1. Get preference data (Anthropic HH-RLHF dataset)
2. Train reward model on preferences
3. Evaluate reward model accuracy
4. Analyze what the reward model learned

### Phase 3: RL Fine-Tuning (8-12 hours)
1. Set up PPO training loop (or use TRL)
2. Fine-tune SFT model with reward signal
3. Monitor for reward hacking
4. Compare RLHF model to SFT model

## Resources

### Papers
- [InstructGPT](https://arxiv.org/abs/2203.02155)
- [Learning to Summarize from Human Feedback](https://arxiv.org/abs/2009.01325)
- [DPO Paper](https://arxiv.org/abs/2305.18290) (for comparison)

### Libraries
- [TRL Documentation](https://huggingface.co/docs/trl/)
- [Anthropic HH-RLHF Dataset](https://huggingface.co/datasets/Anthropic/hh-rlhf)

### Tutorials
- [HuggingFace RLHF Tutorial](https://huggingface.co/blog/rlhf)
- [Nathan Lambert's RLHF Blog Posts](https://www.interconnects.ai/)

## Starter Code

See `starter/` directory for:
- `sft.py` - Supervised fine-tuning script
- `reward_model.py` - Reward model training
- `ppo_train.py` - PPO training loop
- `evaluate.py` - Evaluation utilities

## Evaluation Rubric

| Criterion | Points |
|-----------|--------|
| Working SFT phase | 15 |
| Reward model training | 20 |
| PPO implementation/usage | 25 |
| Comparison experiments | 15 |
| Failure mode documentation | 10 |
| Code quality | 10 |
| Report/blog post | 5 |
| **Total** | **100** |

## Deliverables

1. **Code**: Full RLHF pipeline in a Git repo
2. **Trained models**: Checkpoints for SFT, RM, and RLHF models
3. **Comparison**: Quantitative and qualitative comparison
4. **Failure modes**: Documentation of reward hacking or other issues
5. **Report**: 1500-2500 words explaining the process

## Expected Challenges

- PPO can be unstable—expect debugging
- Reward hacking is real—document it when you see it
- Compute constraints limit model size
- Preference data quality matters a lot

## Stretch Goals

- Compare RLHF to DPO (Direct Preference Optimization)
- Implement Constitutional AI-style self-critique
- Analyze reward model internals
- Try different reward model architectures

## Interview Prep

After completing this project, you should be able to:
- Explain the three phases of RLHF
- Discuss reward hacking and how to mitigate it
- Compare RLHF to alternatives (DPO, RLAIF)
- Describe the role of KL divergence penalty
