---
title: Hugging Face Daily Papers - 2026-01-15
date: 2026-01-15 09:15:00 +0900
categories: [Daily Papers, 일간]
tags: [huggingface, papers, daily, ai]
author: lim4349
---

# Hugging Face Daily Papers - 2026-01-15

총 **4개**의 논문이 수집되었습니다.

## 📊 좋아요 순위

1. **Fast-ThinkAct: Efficient Vision-Language-Action Reasoning via Verbalizable Latent Planning** - 👍 11
   - 기관: NVIDIA1
   - [HF 페이지](https://huggingface.co/papers/2601.09708)
   - [논문 링크](https://arxiv.org/abs/2601.09708)
   - Abstract: Vision-Language-Action (VLA) tasks require reasoning over complex visual scenes and executing adaptive actions in dynamic environments. While recent studies on reasoning VLAs show that explicit chain-of-thought (CoT) can improve generalization, they suffer from high inference latency due to lengthy reasoning traces. We propose Fast-ThinkAct, an efficient reasoning framework that achieves compact yet performant planning through verbalizable latent reasoning. Fast-ThinkAct learns to reason efficiently with latent CoTs by distilling from a teacher, driven by a preference-guided objective to align manipulation trajectories that transfers both linguistic and visual planning capabilities for embodied control. This enables reasoning-enhanced policy learning that effectively connects compact reasoning to action execution. Extensive experiments across diverse embodied manipulation and reasoning benchmarks demonstrate that Fast-ThinkAct achieves strong performance with up to 89.3\% reduced inference latency over state-of-the-art reasoning VLAs, while maintaining effective long-horizon planning, few-shot adaptation, and failure recovery.

2. **A^3-Bench: Benchmarking Memory-Driven Scientific Reasoning via Anchor and Attractor Activation** - 👍 6
   - 기관: ·8 authors1
   - [HF 페이지](https://huggingface.co/papers/2601.09274)
   - [논문 링크](https://arxiv.org/abs/2601.09274)
   - Abstract: Scientific reasoning relies not only on logical inference but also on activating prior knowledge and experiential structures. Memory can efficiently reuse knowledge and enhance reasoning consistency and stability. However, existing benchmarks mainly evaluate final answers or step-by-step coherence, overlooking the \textit{memory-driven} mechanisms that underlie human reasoning, which involves activating anchors and attractors, then integrating them into multi-step inference. To address this gap, we propose $A^3$-Bench~ this https URL , a benchmark designed to evaluate scientific reasoning through dual-scale memory-driven activation, grounded in Anchor and Attractor Activation. First, we annotate 2,198 science reasoning problems across domains using the SAPM process(subject, anchor & attractor, problem, and memory developing). Second, we introduce a dual-scale memory evaluation framework utilizing anchors and attractors, along with the AAUI(Anchor--Attractor Utilization Index) metric to measure memory activation rates. Finally, through experiments with various base models and paradigms, we validate $A^3$-Bench and analyze how memory activation impacts reasoning performance, providing insights into memory-driven scientific reasoning.

3. **MAXS: Meta-Adaptive Exploration with LLM Agents** - 👍 6
   - 기관: ·10 authors1
   - [HF 페이지](https://huggingface.co/papers/2601.09259)
   - [논문 링크](https://arxiv.org/abs/2601.09259)
   - Abstract: Large Language Model (LLM) Agents exhibit inherent reasoning abilities through the collaboration of multiple tools. However, during agent inference, existing methods often suffer from (i) locally myopic generation, due to the absence of lookahead, and (ii) trajectory instability, where minor early errors can escalate into divergent reasoning paths. These issues make it difficult to balance global effectiveness and computational efficiency. To address these two issues, we propose meta-adaptive exploration with LLM agents this https URL , a meta-adaptive reasoning framework based on LLM Agents that flexibly integrates tool execution and reasoning planning. MAXS employs a lookahead strategy to extend reasoning paths a few steps ahead, estimating the advantage value of tool usage, and combines step consistency variance and inter-step trend slopes to jointly select stable, consistent, and high-value reasoning steps. Additionally, we introduce a trajectory convergence mechanism that controls computational cost by halting further rollouts once path consistency is achieved, enabling a balance between resource efficiency and global effectiveness in multi-tool reasoning. We conduct extensive empirical studies across three base models (MiMo-VL-7B, Qwen2.5-VL-7B, Qwen2.5-VL-32B) and five datasets, demonstrating that MAXS consistently outperforms existing methods in both performance and inference efficiency. Further analysis confirms the effectiveness of our lookahead strategy and tool usage.

4. **Controlled Self-Evolution for Algorithmic Code Optimization** - 👍 6
   - 기관: QuantaAlpha221
   - [HF 페이지](https://huggingface.co/papers/2601.07348)
   - [논문 링크](https://arxiv.org/abs/2601.07348)
   - Abstract: Self-evolution methods enhance code generation through iterative "generate-verify-refine" cycles, yet existing approaches suffer from low exploration efficiency, failing to discover solutions with superior complexity within limited budgets. This inefficiency stems from initialization bias trapping evolution in poor solution regions, uncontrolled stochastic operations lacking feedback guidance, and insufficient experience utilization across tasks. To address these bottlenecks, we propose Controlled Self-Evolution (CSE), which consists of three key components. Diversified Planning Initialization generates structurally distinct algorithmic strategies for broad solution space coverage. Genetic Evolution replaces stochastic operations with feedback-guided mechanisms, enabling targeted mutation and compositional crossover. Hierarchical Evolution Memory captures both successful and failed experiences at inter-task and intra-task levels. Experiments on EffiBench-X demonstrate that CSE consistently outperforms all baselines across various LLM backbones. Furthermore, CSE achieves higher efficiency from early generations and maintains continuous improvement throughout evolution. Our code is publicly available at this https URL .

