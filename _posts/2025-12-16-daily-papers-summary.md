---
title: Hugging Face Daily Papers - 2025-12-16
date: 2025-12-16 09:15:00 +0900
categories: ['Daily Papers', '일간']
tags: ['huggingface', 'papers', 'daily', 'ai']
author: lim4349
---

# Hugging Face Daily Papers - 2025-12-16

총 **4개**의 논문이 수집되었습니다.

## 📊 좋아요 순위

1. **Openpi Comet: Competition Solution For 2025 BEHAVIOR Challenge** - 👍 10
   - 기관: ·16 authors
   - [HF 페이지](https://huggingface.co/papers/2512.10071)
   - [논문 링크](https://arxiv.org/abs/2512.10071)
   - Abstract: The 2025 BEHAVIOR Challenge is designed to rigorously track progress toward solving long-horizon tasks by physical agents in simulated environments. BEHAVIOR-1K focuses on everyday household tasks that people most want robots to assist with and these tasks introduce long-horizon mobile manipulation challenges in realistic settings, bridging the gap between current research and real-world, human-centric applications. This report presents our solution to the 2025 BEHAVIOR Challenge in a very close 2nd place and substantially outperforms the rest of the submissions. Building on $\pi_{0.5}$, we focus on systematically building our solution by studying the effects of training techniques and data. Through careful ablations, we show the scaling power in pre-training and post-training phases for competitive performance. We summarize our practical lessons and design recommendations that we hope will provide actionable insights for the broader embodied AI community when adapting powerful foundation models to complex embodied scenarios.

2. **MentraSuite: Post-Training Large Language Models for Mental Health Reasoning and Assessment** - 👍 7
   - 기관: ·13 authors
   - [HF 페이지](https://huggingface.co/papers/2512.09636)
   - [논문 링크](https://arxiv.org/abs/2512.09636)
   - Abstract: Mental health disorders affect hundreds of millions globally, and the Web now serves as a primary medium for accessing support, information, and assessment. Large language models (LLMs) offer scalable and accessible assistance, yet their deployment in mental-health settings remains risky when their reasoning is incomplete, inconsistent, or ungrounded. Existing psychological LLMs emphasize emotional understanding or knowledge recall but overlook the step-wise, clinically aligned reasoning required for appraisal, diagnosis, intervention planning, abstraction, and verification. To address these issues, we introduce MentraSuite, a unified framework for advancing reliable mental-health reasoning. We propose MentraBench, a comprehensive benchmark spanning five core reasoning aspects, six tasks, and 13 datasets, evaluating both task performance and reasoning quality across five dimensions: conciseness, coherence, hallucination avoidance, task understanding, and internal consistency. We further present Mindora, a post-trained model optimized through a hybrid SFT-RL framework with an inconsistency-detection reward to enforce faithful and coherent reasoning. To support training, we construct high-quality trajectories using a novel reasoning trajectory generation strategy, that strategically filters difficult samples and applies a structured, consistency-oriented rewriting process to produce concise, readable, and well-balanced trajectories. Across 20 evaluated LLMs, Mindora achieves the highest average performance on MentraBench and shows remarkable performances in reasoning reliability, demonstrating its effectiveness for complex mental-health scenarios.

3. **Error-Free Linear Attention is a Free Lunch: Exact Solution from Continuous-Time Dynamics** - 👍 2
   - 기관: Deep Cognition and Language Research (DeCLaRe) Lab
   - [HF 페이지](https://huggingface.co/papers/2512.12602)
   - [논문 링크](https://arxiv.org/abs/2512.12602)
   - Abstract: Linear-time attention and State Space Models (SSMs) promise to solve the quadratic cost bottleneck in long-context language models employing softmax attention. We introduce Error-Free Linear Attention (EFLA), a numerically stable, fully parallelism and generalized formulation of the delta rule. Specifically, we formulate the online learning update as a continuous-time dynamical system and prove that its exact solution is not only attainable but also computable in linear time with full parallelism. By leveraging the rank-1 structure of the dynamics matrix, we directly derive the exact closed-form solution effectively corresponding to the infinite-order Runge-Kutta method. This attention mechanism is theoretically free from error accumulation, perfectly capturing the continuous dynamics while preserving the linear-time complexity. Through an extensive suite of experiments, we show that EFLA enables robust performance in noisy environments, achieving lower language modeling perplexity and superior downstream benchmark performance than DeltaNet without introducing additional parameters. Our work provides a new theoretical foundation for building high-fidelity, scalable linear-time attention models.

4. **Aesthetic Alignment Risks Assimilation: How Image Generation and Reward Models Reinforce Beauty Bias and Ideological "Censorship"** - 👍 2
   - 기관: ·4 authors
   - [HF 페이지](https://huggingface.co/papers/2512.11883)
   - [논문 링크](https://arxiv.org/abs/2512.11883)
   - Abstract: Over-aligning image generation models to a generalized aesthetic preference conflicts with user intent, particularly when ``anti-aesthetic" outputs are requested for artistic or critical purposes. This adherence prioritizes developer-centered values, compromising user autonomy and aesthetic pluralism. We test this bias by constructing a wide-spectrum aesthetics dataset and evaluating state-of-the-art generation and reward models. We find that aesthetic-aligned generation models frequently default to conventionally beautiful outputs, failing to respect instructions for low-quality or negative imagery. Crucially, reward models penalize anti-aesthetic images even when they perfectly match the explicit user prompt. We confirm this systemic bias through image-to-image editing and evaluation against real abstract artworks.

