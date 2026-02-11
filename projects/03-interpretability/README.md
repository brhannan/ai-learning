# Project 3: Interpretability Experiment

**Phase:** 3 - Alignment & Safety
**Estimated Time:** 15-20 hours
**Difficulty:** Medium-Hard
**XP on Completion:** +600 XP

## Overview

Conduct an interpretability experiment on a small language model. Train probing classifiers, analyze attention patterns, or attempt to find interpretable features. This builds skills directly relevant to Anthropic's interpretability team.

## Why This Project Matters

- **Anthropic focus**: Interpretability is a major Anthropic research area
- **Unique skill**: Few applicants have hands-on interpretability experience
- **Safety relevance**: Understanding models is key to aligning them
- **Research taste**: Shows you can do research-style work

## Objectives

By the end of this project, you should have:

1. [ ] Selected a small model to analyze (GPT-2 or similar)
2. [ ] Set up TransformerLens or similar tooling
3. [ ] Chosen a specific phenomenon to investigate
4. [ ] Trained probing classifiers or analyzed activations
5. [ ] Visualized your findings
6. [ ] Written a research-style report

## Project Options

Choose ONE of these paths:

### Option A: Probing Classifiers
Train classifiers on hidden states to detect linguistic features:
- Part-of-speech tagging
- Named entity recognition
- Sentiment detection
- Syntax tree depth

### Option B: Attention Pattern Analysis
Analyze what attention heads learn:
- Find heads that attend to previous token
- Find heads that attend to syntax
- Find heads that copy information
- Analyze attention in specific contexts

### Option C: Feature Finding
Attempt to find interpretable features:
- Use sparse autoencoders (if ambitious)
- Analyze neuron activations
- Look for concept-specific neurons
- Replicate a finding from literature

### Option D: Behavior Analysis
Analyze model behavior on specific inputs:
- Analyze factual recall
- Study in-context learning
- Examine prompt sensitivity
- Investigate failure modes

## Technical Requirements

### Tools
- **TransformerLens**: Primary library for interpretability
- **PyTorch**: Model and training
- **Matplotlib/Plotly**: Visualization
- **Jupyter Notebooks**: Exploration

### Models
- GPT-2 (small or medium)
- Pythia models
- Any model supported by TransformerLens

## Suggested Approach

### Week 1: Setup & Exploration
1. Install TransformerLens
2. Load a model and explore activations
3. Run through tutorials
4. Choose your focus area

### Week 2: Experiment Design
1. Define research question
2. Design experiment
3. Collect or generate data
4. Start initial experiments

### Week 3: Analysis
1. Run main experiments
2. Iterate on approach
3. Create visualizations
4. Document findings

### Week 4: Write-up
1. Interpret results
2. Write research-style report
3. Create figures
4. Consider limitations

## Resources

### Papers
- [Scaling Monosemanticity](https://www.anthropic.com/research/mapping-mind-language-model)
- [Toy Models of Superposition](https://transformer-circuits.pub/2022/toy_model/index.html)
- [A Mathematical Framework for Transformer Circuits](https://transformer-circuits.pub/2021/framework/index.html)

### Tools & Tutorials
- [TransformerLens](https://neelnanda-io.github.io/TransformerLens/)
- [ARENA Exercises](https://arena.education/)
- [Neel Nanda's Blog](https://www.neelnanda.io/mechanistic-interpretability/getting-started)

## Evaluation Rubric

| Criterion | Points |
|-----------|--------|
| Clear research question | 15 |
| Appropriate methodology | 20 |
| Quality of analysis | 25 |
| Visualizations | 15 |
| Interpretation of results | 15 |
| Report quality | 10 |
| **Total** | **100** |

## Deliverables

1. **Code**: Jupyter notebooks or Python scripts
2. **Visualizations**: Clear, informative figures
3. **Report**: 1500-2500 word write-up in research paper style
4. **Data**: Any generated datasets or results

## Report Structure

1. **Introduction**: What question are you investigating? Why?
2. **Methods**: What did you do? How?
3. **Results**: What did you find?
4. **Discussion**: What does it mean? Limitations?
5. **Conclusion**: Summary and future work

## Example Research Questions

- "Do GPT-2 attention heads specialize in syntactic vs semantic tasks?"
- "Can probing classifiers detect sentiment in intermediate layers?"
- "Which layers are most important for factual recall?"
- "How do attention patterns change for in-context vs memorized facts?"

## Quiz Prep

After completing this project, you should be able to:
- Explain probing classifiers and their limitations
- Discuss mechanistic vs behavioral interpretability
- Describe Anthropic's monosemanticity work
- Design an interpretability experiment
