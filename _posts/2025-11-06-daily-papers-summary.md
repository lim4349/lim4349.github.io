---
title: Hugging Face Daily Papers - 2025-11-06
date: 2025-11-06 09:15:00 +0900
categories: ['Daily Papers', '일간']
tags: ['huggingface', 'papers', 'daily', 'ai']
author: lim4349
---

# Hugging Face Daily Papers - 2025-11-06

총 **4개**의 논문이 수집되었습니다.

## 📊 좋아요 순위

1. **MME-CC: A Challenging Multi-Modal Evaluation Benchmark of Cognitive
  Capacity** - 👍 0
   - 기관: ByteDance Seed
   - [HF 페이지](https://huggingface.co/papers/2511.03146)
   - [논문 링크](https://arxiv.org/abs/2511.03146)
   - Abstract: As reasoning models scale rapidly, the essential role of multimodality in human cognition has come into sharp relief, driving a growing need to probe vision-centric cognitive behaviors. Yet, existing multimodal benchmarks either overemphasize textual reasoning or fall short of systematically capturing vision-centric cognitive behaviors, leaving the cognitive capacity of MLLMs insufficiently assessed. To address this limitation, we introduce MME-CC (Multi-Modal Evaluation benchmark of Cognitive Capacity), a vision-grounded benchmark that organizes 11 representative reasoning tasks into three fundamental categories of visual information: spatial, geometric, and knowledge-based reasoning, and provides fine-grained analyses of MLLMs' cognitive capacity across these dimensions. Based on MME-CC, we conduct extensive experiments over 16 representative MLLMs. Our study reveals that closed-source models currently lead overall (e.g., 42.66 for Gemini-2.5-Pro vs. 30.45 for GLM-4.5V), while spatial and geometric reasoning remain broadly weak (less than or equal to 30%). We further identify common error patterns, including orientation mistakes, fragile cross-view identity persistence, and poor adherence to counterfactual instructions, and observe that Chain-of-Thought typically follows a three-stage process (extract -> reason -> verify) with heavy reliance on visual extraction. We hope this work catalyzes a shift toward treating the cognitive capacity of MLLMs as central to both evaluation and model design.

2. **LEGO-Eval: Towards Fine-Grained Evaluation on Synthesizing 3D Embodied
  Environments with Tool Augmentation** - 👍 0
   - 기관: ·6 authors
   - [HF 페이지](https://huggingface.co/papers/2511.03001)
   - [논문 링크](https://arxiv.org/abs/2511.03001)
   - Abstract: Despite recent progress in using Large Language Models (LLMs) for automatically generating 3D scenes, generated scenes often lack realistic spatial layouts and object attributes found in real-world environments. As this problem stems from insufficiently detailed, coarse-grained instructions, advancing 3D scene synthesis guided by more detailed, fine-grained instructions that reflect real-world environments becomes crucial. Without such realistic scenes, training embodied agents in unrealistic environments can lead them to learn priors that diverge significantly from real-world physics and semantics, degrading their performance when deployed. Thus, verifying the alignment between the fine-grained instruction and the generated scene is essential for effective learning. However, current evaluation methods, such as CLIPScore and vision-language models (VLMs), often fail to reliably assess such alignment. This shortcoming arises primarily from their shallow understanding of 3D scenes, which often leads to improperly grounded scene components. To address this, we introduce LEGO-Eval, an evaluation framework equipped with diverse tools designed to explicitly ground scene components, enabling more accurate alignment assessments. We also present LEGO-Bench, a benchmark of detailed instructions that specify complex layouts and attributes of real-world environments. Experiments demonstrate that LEGO-Eval outperforms VLM-as-a-judge by 0.41 F1 score in assessing scene-instruction alignment. Benchmarking with LEGO-Bench reveals significant limitations in current generation methods. Across all evaluated approaches, success rates reached at most 10% in generating scenes that fully align with fine-grained instructions.

3. **Let Multimodal Embedders Learn When to Augment Query via Adaptive Query
  Augmentation** - 👍 0
   - 기관: ·5 authors
   - [HF 페이지](https://huggingface.co/papers/2511.02358)
   - [논문 링크](https://arxiv.org/abs/2511.02358)
   - Abstract: Query augmentation makes queries more meaningful by appending further information to the queries to find relevant documents. Current studies have proposed Large Language Model (LLM)-based embedders, which learn representation for embedding and generation for query augmentation in a multi-task manner by leveraging the generative capabilities of LLM. During inference, these jointly trained embedders have conducted query augmentation followed by embedding, showing effective results. However, augmenting every query leads to substantial embedding latency and query augmentation can be detrimental to performance for some queries. Also, previous methods have not been explored in multimodal environments. To tackle these problems, we propose M-Solomon, a universal multimodal embedder that can adaptively determine when to augment queries. Our approach first divides the queries of the training datasets into two groups at the dataset level. One includes queries that require augmentation and the other includes queries that do not. Then, we introduces a synthesis process that generates appropriate augmentations for queries that require them by leveraging a powerful Multimodal LLM (MLLM). Next, we present adaptive query augmentation. Through this step, M-Solomon can conduct query augmentation only when necessary by learning to generate synthetic augmentations with the prefix /augment for queries that demand them and to generate the simple string /embed for others. Experimental results showed that M-Solomon not only surpassed the baseline without augmentation by a large margin but also outperformed the baseline that always used augmentation, providing much faster embedding latency.

4. **LiveTradeBench: Seeking Real-World Alpha with Large Language Models** - 👍 0
   - 기관: ·3 authors
   - [HF 페이지](https://huggingface.co/papers/2511.03628)
   - [논문 링크](https://arxiv.org/abs/2511.03628)
   - Abstract: Large language models (LLMs) achieve strong performance across benchmarks--from knowledge quizzes and math reasoning to web-agent tasks--but these tests occur in static settings, lacking real dynamics and uncertainty. Consequently, they evaluate isolated reasoning or problem-solving rather than decision-making under uncertainty. To address this, we introduce LiveTradeBench, a live trading environment for evaluating LLM agents in realistic and evolving markets. LiveTradeBench follows three design principles: (i) Live data streaming of market prices and news, eliminating dependence on offline backtesting and preventing information leakage while capturing real-time uncertainty; (ii) a portfolio-management abstraction that extends control from single-asset actions to multi-asset allocation, integrating risk management and cross-asset reasoning; and (iii) multi-market evaluation across structurally distinct environments--U.S. stocks and Polymarket prediction markets--differing in volatility, liquidity, and information flow. At each step, an agent observes prices, news, and its portfolio, then outputs percentage allocations that balance risk and return. Using LiveTradeBench, we run 50-day live evaluations of 21 LLMs across families. Results show that (1) high LMArena scores do not imply superior trading outcomes; (2) models display distinct portfolio styles reflecting risk appetite and reasoning dynamics; and (3) some LLMs effectively leverage live signals to adapt decisions. These findings expose a gap between static evaluation and real-world competence, motivating benchmarks that test sequential decision making and consistency under live uncertainty.

