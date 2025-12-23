# Project 1: Transformer from Scratch

**Phase:** 1 - Foundations
**Estimated Time:** 15-25 hours
**Difficulty:** Medium-Hard
**XP on Completion:** +500 XP

## Overview

Implement a transformer from scratch in PyTorch (or JAX). This is not optional—reading about transformers is not the same as building one.

## Why This Project Matters

- **Interview signal**: "I implemented a transformer from scratch" is powerful
- **Deep understanding**: You'll understand attention at an intuitive level
- **Debugging skills**: When things break, you'll know where to look
- **Foundation**: Everything else builds on this

## Objectives

By the end of this project, you should have:

1. [ ] Implemented scaled dot-product attention
2. [ ] Implemented multi-head attention
3. [ ] Implemented positional encoding (sinusoidal)
4. [ ] Built a transformer encoder block (attention + FFN + norms)
5. [ ] Stacked blocks into a full encoder
6. [ ] Trained on a small task (character-level language model)
7. [ ] Visualized attention weights
8. [ ] Written a blog post explaining your implementation

## Technical Requirements

### Must Have
- Pure PyTorch/JAX (no Hugging Face transformers)
- Clear, readable code with comments
- Working training loop
- Attention visualization

### Nice to Have
- Decoder implementation (for full encoder-decoder)
- Multiple positional encoding schemes
- Ablation experiments
- GPU training support

## Suggested Approach

### Week 1: Core Components
1. Implement attention (start with single-head)
2. Add scaling and softmax
3. Extend to multi-head
4. Test on simple examples

### Week 2: Full Model
1. Add positional encoding
2. Build encoder block (attention + FFN)
3. Add layer norms and residuals
4. Stack into full encoder

### Week 3: Training & Experiments
1. Set up data loading (Shakespeare or similar)
2. Implement training loop
3. Train and debug
4. Visualize attention patterns

### Week 4: Polish & Write-up
1. Clean up code
2. Add documentation
3. Run experiments
4. Write blog post

## Resources

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
- [The Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/)
- [Karpathy's nanoGPT](https://github.com/karpathy/nanoGPT)
- [Karpathy's "Let's build GPT"](https://www.youtube.com/watch?v=kCc8FmEb1nY)

## Starter Code

See `starter/` directory for:
- `attention.py` - Skeleton for attention implementation
- `model.py` - Skeleton for full model
- `train.py` - Basic training loop
- `data.py` - Data loading utilities

## Evaluation Rubric

| Criterion | Points |
|-----------|--------|
| Working attention mechanism | 20 |
| Multi-head implementation | 15 |
| Positional encoding | 10 |
| Full encoder architecture | 20 |
| Training and loss convergence | 15 |
| Code quality and comments | 10 |
| Blog post / write-up | 10 |
| **Total** | **100** |

## Deliverables

1. **Code**: Clean, working implementation in a Git repo
2. **Training log**: Evidence of successful training
3. **Visualizations**: Attention weight plots
4. **Blog post**: 1000-2000 words explaining your implementation

## Common Pitfalls

- Forgetting to scale attention by sqrt(d_k)
- Wrong dimension ordering in multi-head attention
- Not masking padded positions
- Incorrect layer norm placement (pre vs post)
- Vanishing gradients without residual connections

## Interview Prep

After completing this project, you should be able to:
- Whiteboard the attention mechanism
- Explain Q, K, V matrices intuitively
- Discuss complexity (O(n²) in sequence length)
- Describe alternatives (linear attention, FlashAttention)
