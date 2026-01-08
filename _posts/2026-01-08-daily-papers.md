---
title: Hugging Face Daily Papers - 2026-01-08
date: 2026-01-08 09:15:00 +0900
categories: [Daily Papers, 일간]
tags: [huggingface, papers, daily, ai]
author: lim4349
---

# Hugging Face Daily Papers - 2026-01-08

총 **3개**의 논문이 수집되었습니다.

## 📊 좋아요 순위

1. **Choreographing a World of Dynamic Objects** - 👍 2
   - 기관: ·7 authors
   - [HF 페이지](https://huggingface.co/papers/2601.04194)
   - [논문 링크](https://arxiv.org/abs/2601.04194)
   - Abstract: Dynamic objects in our physical 4D (3D + time) world are constantly evolving, deforming, and interacting with other objects, leading to diverse 4D scene dynamics. In this paper, we present a universal generative pipeline, CHORD, for CHOReographing Dynamic objects and scenes and synthesizing this type of phenomena. Traditional rule-based graphics pipelines to create these dynamics are based on category-specific heuristics, yet are labor-intensive and not scalable. Recent learning-based methods typically demand large-scale datasets, which may not cover all object categories in interest. Our approach instead inherits the universality from the video generative models by proposing a distillation-based pipeline to extract the rich Lagrangian motion information hidden in the Eulerian representations of 2D videos. Our method is universal, versatile, and category-agnostic. We demonstrate its effectiveness by conducting experiments to generate a diverse range of multi-body 4D dynamics, show its advantage compared to existing methods, and demonstrate its applicability in generating robotics manipulation policies. Project page: this https URL

2. **MDAgent2: Large Language Model for Code Generation and Knowledge Q&A in Molecular Dynamics** - 👍 1
   - 기관: Peking University1
   - [HF 페이지](https://huggingface.co/papers/2601.02075)
   - [논문 링크](https://arxiv.org/abs/2601.02075)
   - Abstract: Molecular dynamics (MD) simulations are essential for understanding atomic-scale behaviors in materials science, yet writing LAMMPS scripts remains highly specialized and time-consuming tasks. Although LLMs show promise in code generation and domain-specific question answering, their performance in MD scenarios is limited by scarce domain data, the high deployment cost of state-of-the-art LLMs, and low code executability. Building upon our prior MDAgent, we present MDAgent2, the first end-to-end framework capable of performing both knowledge Q&A and code generation within the MD domain. We construct a domain-specific data-construction pipeline that yields three high-quality datasets spanning MD knowledge, question answering, and code generation. Based on these datasets, we adopt a three stage post-training strategy--continued pre-training (CPT), supervised fine-tuning (SFT), and reinforcement learning (RL)--to train two domain-adapted models, MD-Instruct and MD-Code. Furthermore, we introduce MD-GRPO, a closed-loop RL method that leverages simulation outcomes as reward signals and recycles low-reward trajectories for continual refinement. We further build MDAgent2-RUNTIME, a deployable multi-agent system that integrates code generation, execution, evaluation, and self-correction. Together with MD-EvalBench proposed in this work, the first benchmark for LAMMPS code generation and question answering, our models and system achieve performance surpassing several strong this http URL work systematically demonstrates the adaptability and generalization capability of large language models in industrial simulation tasks, laying a methodological foundation for automatic code generation in AI for Science and industrial-scale simulations. URL: this https URL

3. **E-GRPO: High Entropy Steps Drive Effective Reinforcement Learning for Flow Models** - 👍 0
   - 기관: Tsinghua University1
   - [HF 페이지](https://huggingface.co/papers/2601.00423)
   - [논문 링크](https://arxiv.org/abs/2601.00423)
   - Abstract: Recent reinforcement learning has enhanced the flow matching models on human preference alignment. While stochastic sampling enables the exploration of denoising directions, existing methods which optimize over multiple denoising steps suffer from sparse and ambiguous reward signals. We observe that the high entropy steps enable more efficient and effective exploration while the low entropy steps result in undistinguished roll-outs. To this end, we propose E-GRPO, an entropy aware Group Relative Policy Optimization to increase the entropy of SDE sampling steps. Since the integration of stochastic differential equations suffer from ambiguous reward signals due to stochasticity from multiple steps, we specifically merge consecutive low entropy steps to formulate one high entropy step for SDE sampling, while applying ODE sampling on other steps. Building upon this, we introduce multi-step group normalized advantage, which computes group-relative advantages within samples sharing the same consolidated SDE denoising step. Experimental results on different reward settings have demonstrated the effectiveness of our methods.

