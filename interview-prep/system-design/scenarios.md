# ML System Design Practice

## How to Approach ML System Design

1. **Clarify requirements** (2-3 min)
   - What's the goal?
   - What are the constraints (latency, cost, scale)?
   - What's the input/output?

2. **High-level design** (5-10 min)
   - Draw the main components
   - Explain data flow
   - Identify key decisions

3. **Deep dive on components** (15-20 min)
   - Model architecture choices
   - Training pipeline
   - Serving infrastructure
   - Evaluation and monitoring

4. **Tradeoffs and edge cases** (5-10 min)
   - What could go wrong?
   - How would you scale?
   - Safety considerations

---

## Practice Scenarios

### Scenario 1: LLM-Powered Search
**Prompt**: Design a search system that uses LLMs to answer user queries.

**Key considerations:**
- Retrieval vs generation tradeoff
- Latency requirements
- Hallucination mitigation
- Cost at scale
- Evaluation metrics

**Components to discuss:**
- Query understanding
- Retrieval system (embeddings, vector DB)
- Reranking
- Answer generation
- Citation/grounding

---

### Scenario 2: AI Coding Assistant
**Prompt**: Design a system like GitHub Copilot.

**Key considerations:**
- Real-time latency (<100ms)
- Context window management
- Multi-file understanding
- Code safety
- Personalization

**Components to discuss:**
- Code context extraction
- Model serving (caching, batching)
- Streaming responses
- Evaluation (acceptance rate, correctness)
- Feedback loop

---

### Scenario 3: Content Moderation System
**Prompt**: Design an LLM-based content moderation system for a social platform.

**Key considerations:**
- Precision vs recall tradeoff
- Latency requirements
- Adversarial users
- False positive impact
- Policy updates

**Components to discuss:**
- Classification pipeline
- Multi-stage review
- Human-in-the-loop
- Policy enforcement
- Appeals handling

---

### Scenario 4: RLHF Training Pipeline
**Prompt**: Design a system to collect human feedback and train models with RLHF.

**Key considerations:**
- Labeler quality control
- Preference data collection
- Training stability
- Evaluation and iteration
- Cost management

**Components to discuss:**
- Labeling interface
- Reward model training
- PPO training loop
- A/B testing framework
- Model versioning

---

### Scenario 5: Model Serving at Scale
**Prompt**: Design infrastructure to serve a 70B parameter LLM to millions of users.

**Key considerations:**
- GPU utilization
- Latency p50/p99
- Cost per request
- Availability
- Multi-region

**Components to discuss:**
- Model parallelism
- KV-cache optimization
- Batching strategies
- Load balancing
- Caching layers

---

### Scenario 6: Agentic System
**Prompt**: Design an AI agent that can complete multi-step tasks using tools.

**Key considerations:**
- Action reliability
- Error recovery
- Cost management
- User control
- Safety constraints

**Components to discuss:**
- Agent loop architecture
- Tool calling system
- Memory/context management
- Evaluation and monitoring
- Human-in-the-loop

---

## Tips for Anthropic

When discussing designs, emphasize:

1. **Safety considerations**: What could go wrong? How do you prevent harm?
2. **Evaluation**: How do you know it's working?
3. **Tradeoffs**: Show you understand there are no perfect solutions
4. **Iteration**: How would you improve it over time?
5. **Communication**: Explain your thinking clearly

---

## Practice Framework

For each scenario, spend 45 minutes:
- 5 min: Read and clarify
- 20 min: Design and diagram
- 15 min: Write out your explanation
- 5 min: Identify weak points

Then review:
- Did you cover all major components?
- Did you discuss tradeoffs?
- Did you consider safety?
- Could you explain this in an interview?
