---
title: Hugging Face Daily Papers - 2026-08-20
permalink: /posts/daily-papers-2026-08-20/
date: 2026-08-20 09:15:00 +0900
categories: [Daily Papers, 일간]
tags: [huggingface, papers, daily, ai]
author: lim4349
---

# Hugging Face Daily Papers - 2026-08-20

총 **5개**의 논문이 수집되었습니다.

## 📊 좋아요 순위

1. **SemaPLC: A Project-Grounded, Verification-Gated Agent Harness for PLC Code Generation** - 👍 1
   - 기관: Midea AI Research Center1
   - [HF 페이지](https://huggingface.co/papers/2608.18565)
   - [논문 링크](https://arxiv.org/abs/2608.18565)
   - Abstract: Programmable logic controllers (PLCs) run industrial plants, and large language models can already generate independent program organization units (POUs) for them. Whether such logic integrates into an existing PLC project and then runs correctly has been checked only in limited tests. We present \textsc{SemaPLC}, a project-grounded and verification-gated agent harness assembled from conventional tools but governed by a strict completion rule. Rather than stopping when the model judges its own output adequate, \textsc{SemaPLC} declares a task complete only when logged external checks confirm it. Those checks cover the specification, the compilation, and the behavior on a live runtime. On 117 independent-POU tasks matching existing benchmarks, it attains the highest strict verified pass rate on all seven models (72.6\% mean). On a project-context track of 65 tasks whose generated logic must compile and run inside a real project, it attains the highest mean on integrated compilation, static behavior, and dynamic behavior. Of the three layers, dynamic behavior is the most revealing. We measure it by deploying the generated and the reference logic to a live PLC runtime and comparing their executed traces. All methods fall within 10 static points of one another, whereas dynamic scores separate them sharply, from 22.4 to 31.4 for the baselines against 52.2 for \textsc{SemaPLC}. Overall, our verification-gated harness raises the mean at every layer and most sharply at runtime. Execution, not static scoring, is the faithful test of whether generated control logic actually works. \textsc{SemaPLC} is open-sourced at this https URL .

2. **SPADE: Self-Play in Adaptive Synthetic Executable Environments** - 👍 1
   - 기관: ·18 authors
   - [HF 페이지](https://huggingface.co/papers/2608.19197)
   - [논문 링크](https://arxiv.org/abs/2608.19197)
   - Abstract: Continuous self-improvement requires an ever-expanding pool of self-generated, diverse, adaptive goals. For language agents, existing training environment pools (hand-curated, statically synthesized, or frozen-verifier) keep the goal distribution fixed as the learner scales. We introduce SPADE (Self-Play in Adaptive Synthetic Executable Environments), a self-play RL framework in which a single LLM plays two roles: an Environment Designer that writes complete, long-horizon training environments as executable code with an OpenAI Gym-style reset()/step() interface, and a Reasoning Agent that learns to act in them. Each is a stateful, multi-turn environment (state transitions, reward functions, and verification code), so one interface spans reasoning problems and multi-step agentic tool use. The Reasoning Agent's regret is estimated using the gap between its reward with and without privileged hints; in optimizing this regret signal the Environment Designer learns to target environments at the edge of the agent's capabilities while keeping them feasible. Through extensive experimentation, we find several components critical to success: grounding the Environment Designer on documents sampled from a large pretraining corpus, and giving it an accumulated environment memory. Scaling to 30B-parameter models, SPADE improves over the strongest fixed-environment baseline by +5.3 on average across eight held-out math, science, code, and reasoning benchmarks, and lifts the tool-use setting by +5.7 on BFCL-v4 multi-turn and +13.9 on ACEBench-Agent; on the games setting, the margin over the strongest baseline grows with model scale. By making environment design itself a learnable component, SPADE takes a concrete step toward open-ended self-improvement.

3. **FM-Bench: A Benchmark for Long-Horizon Management with Competing Agents** - 👍 1
   - 기관: ·9 authors10
   - [HF 페이지](https://huggingface.co/papers/2608.18423)
   - [논문 링크](https://arxiv.org/abs/2608.18423)
   - Abstract: Language model agents now execute bounded tasks reliably. Whether they can sustain effective decision-making over long horizons, where actions have cumulative consequences and the environment responds to their choices, remains largely unmeasured. FM-Bench (Football Management Benchmark) measures this. An LLM agent runs a football club for 20 in-game years through 26 tools and roughly 340 to 400 decision stops. It drafts a squad on the same budget as every rival, trades players, negotiates contracts, invests in facilities and youth, sets lineups, and answers to a board that can fire it, while a deterministic engine accumulates every year into one final score with no LLM judge or human rater. The solo track plays each of 15 frontier models against a frozen scripted world, and the Arena places the same models plus a scripted anchor in one shared 20-year world; to our knowledge, the first head-to-head evaluation at this scale. We measure six behavioral capabilities behind the score. Across three seeds, all 15 models complete every horizon while the blind scripted baselines die out in most of theirs, and claude-fable-5 tops the solo board on mean score and the Arena, where the title nonetheless rotates among ten models. Neither scale, price, nor vendor predicts the order; the order settles only late in the horizon, and the best first-play human lands only at the bottom of the model board. What separates the models is managerial behavior rather than computation. Higher-scoring models reduce slow-payoff investment near the end, keep cash invested rather than idle, and open renewals well before the deadline, while token spend predicts nothing. No model learns the market's hidden prices from hundreds of rejected bids, and self-managed memory fails in two opposite modes: an archive that only grows or a plan rewritten every season. Code is available at this https URL .

4. **Training Chemical Plausibility-Aware Large Language Models for Single-Step Retrosynthesis** - 👍 1
   - 기관: Insilico Medicine1
   - [HF 페이지](https://huggingface.co/papers/2608.18940)
   - [논문 링크](https://arxiv.org/abs/2608.18940)
   - Abstract: Single-step retrosynthesis is a central component of computer-aided synthesis planning, yet its intrinsically one-to-many nature is poorly captured by single-answer evaluation and benchmarking protocols. To address this, we introduce Top-K prompting as a robust training and inference paradigm to better capture diverse, plausible reaction predictions. We compile CREED-CCV-2+USPTO-XL, an ultra-large-scale dataset of ~45.6 million verified reactions to train the C3LM (Chemistry Constraint-Consistent Language Model). By integrating fine-tuning with ChemCensor-based and novelty-oriented rewards, our model achieves state-of-the-art performance on the OOD URSA-expert-2026 benchmark. Further analysis of reaction uniqueness shows that LLMs and conventional models explore complementary reaction spaces, motivating ensemble-based retrosynthesis systems. Overall, our results establish Top-K, plausibility-aware training as a practical new direction for robust future LLM-based synthesis planning.

5. **Looped Language Models Improve Compositional Tool Calling** - 👍 1
   - 기관: ·3 authors
   - [HF 페이지](https://huggingface.co/papers/2608.18171)
   - [논문 링크](https://arxiv.org/abs/2608.18171)
   - Abstract: Looped language models have shown promising results on reasoning benchmarks, yet their potential for agentic tool use remains largely unexplored. We study this question in compositional tool-calling settings, where models must coordinate multiple API calls, maintain intermediate state, and preserve dependencies across tool interactions. We evaluate native and retrofitted looped language models on API-Bank, BFCL, and NESTful, comparing looped and non-looped models trained under matched supervised fine-tuning recipes and varying recurrent depth at inference time. In controlled experiments, recurrent computation generally benefits compositional and dependency-aware tool use, while providing smaller and more model-dependent gains on isolated API invocation. Accuracy on multi-step tool use generally increases with recurrent depth; adaptive inference, however, achieves a more favorable compute-performance trade-off by allocating additional computation only when needed. Our results suggest that looped language models are a promising architecture for agentic systems that require reliable planning, coordination, and execution of compositional tool use workflows.

