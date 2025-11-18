---
title: Hugging Face Daily Papers - 2025-11-18
date: 2025-11-18 09:15:00 +0900
categories: ['Daily Papers', '일간']
tags: ['huggingface', 'papers', 'daily', 'ai']
author: lim4349
---

# Hugging Face Daily Papers - 2025-11-18

총 **3개**의 논문이 수집되었습니다.

## 📊 좋아요 순위

1. **MMaDA-Parallel: Multimodal Large Diffusion Language Models for Thinking-Aware Editing and Generation** - 👍 8
   - 기관: ByteDance
   - [HF 페이지](https://huggingface.co/papers/2511.09611)
   - [논문 링크](https://arxiv.org/abs/2511.09611)
   - Abstract: While thinking-aware generation aims to improve performance on complex tasks, we identify a critical failure mode where existing sequential, autoregressive approaches can paradoxically degrade performance due to error propagation. To systematically analyze this issue, we propose ParaBench, a new benchmark designed to evaluate both text and image output modalities. Our analysis using ParaBench reveals that this performance degradation is strongly correlated with poor alignment between the generated reasoning and the final image. To resolve this, we propose a parallel multimodal diffusion framework, MMaDA-Parallel, that enables continuous, bidirectional interaction between text and images throughout the entire denoising trajectory. MMaDA-Parallel is trained with supervised finetuning and then further optimized by Parallel Reinforcement Learning (ParaRL), a novel strategy that applies semantic rewards along the trajectory to enforce cross-modal consistency. Experiments validate that our model significantly improves cross-modal alignment and semantic consistency, achieving a 6.9\% improvement in Output Alignment on ParaBench compared to the state-of-the-art model, Bagel, establishing a more robust paradigm for thinking-aware image synthesis. Our code is open-sourced at this https URL

2. **UFO^3: Weaving the Digital Agent Galaxy** - 👍 2
   - 기관: Microsoft
   - [HF 페이지](https://huggingface.co/papers/2511.11332)
   - [논문 링크](https://arxiv.org/abs/2511.11332)
   - Abstract: Large language model (LLM)-powered agents are transforming digital devices from passive tools into proactive intelligent collaborators. However, most existing frameworks remain confined to a single OS or device, making cross-device workflows brittle and largely manual. We present UFO$^3$, a system that unifies heterogeneous endpoints, desktops, servers, mobile devices, and edge, into a single orchestration fabric. UFO$^3$ models each user request as a mutable TaskConstellation: a distributed DAG of atomic subtasks (TaskStars) with explicit control and data dependencies (TaskStarLines). The TaskConstellation continuously evolves as results stream in from distributed devices, enabling asynchronous execution, adaptive recovery, and dynamic optimization. A Constellation Orchestrator} executes tasks safely and asynchronously while applying dynamic DAG updates, and the Agent Interaction Protocol (AIP) provides persistent, low-latency channels for reliable task dispatch and result streaming. These designs dissolve the traditional boundaries between devices and platforms, allowing agents to collaborate seamlessly and amplify their collective intelligence. We evaluate UFO$^3$ on NebulaBench, a benchmark of 55 cross-device tasks across 5 machines and 10 categories. UFO$^3$ achieves 83.3% subtask completion, 70.9% task success, exposes parallelism with an average width of 1.72, and reduces end-to-end latency by 31% relative to a sequential baseline. Fault-injection experiments demonstrate graceful degradation and recovery under transient and permanent agent failures. These results show that UFO$^3$ achieves accurate, efficient, and resilient task orchestration across heterogeneous devices, uniting isolated agents into a coherent, adaptive computing fabric that extends across the landscape of ubiquitous computing.

3. **Test-Time Spectrum-Aware Latent Steering for Zero-Shot Generalization in Vision-Language Models** - 👍 2
   - 기관: Rutgers Center for Computational Biomedicine Imaging and Modeling
   - [HF 페이지](https://huggingface.co/papers/2511.09809)
   - [논문 링크](https://arxiv.org/abs/2511.09809)
   - Abstract: Vision-Language Models (VLMs) excel at zero-shot inference but often degrade under test-time domain shifts. For this reason, episodic test-time adaptation strategies have recently emerged as powerful techniques for adapting VLMs to a single unlabeled image. However, existing adaptation strategies, such as test-time prompt tuning, typically require backpropagating through large encoder weights or altering core model components. In this work, we introduce Spectrum-Aware Test-Time Steering (STS), a lightweight adaptation framework that extracts a spectral subspace from the textual embeddings to define principal semantic directions and learns to steer latent representations in a spectrum-aware manner by adapting a small number of per-sample shift parameters to minimize entropy across augmented views. STS operates entirely at inference in the latent space, without backpropagation through or modification of the frozen encoders. Building on standard evaluation protocols, our comprehensive experiments demonstrate that STS largely surpasses or compares favorably against state-of-the-art test-time adaptation methods, while introducing only a handful of additional parameters and achieving inference speeds up to 8x faster with a 12x smaller memory footprint than conventional test-time prompt tuning. The code is available at this https URL .

