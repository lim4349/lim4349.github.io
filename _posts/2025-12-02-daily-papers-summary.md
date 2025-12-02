---
title: Hugging Face Daily Papers - 2025-12-02
date: 2025-12-02 09:15:00 +0900
categories: ['Daily Papers', '일간']
tags: ['huggingface', 'papers', 'daily', 'ai']
author: lim4349
---

# Hugging Face Daily Papers - 2025-12-02

총 **2개**의 논문이 수집되었습니다.

## 📊 좋아요 순위

1. **LongVT: Incentivizing "Thinking with Long Videos" via Native Tool Calling** - 👍 8
   - 기관: LMMs-Lab
   - [HF 페이지](https://huggingface.co/papers/2511.20785)
   - [논문 링크](https://arxiv.org/abs/2511.20785)
   - Abstract: Large multimodal models (LMMs) have shown great potential for video reasoning with textual Chain-of-Thought. However, they remain vulnerable to hallucinations, especially when processing long-form videos where evidence is sparse and temporally dispersed. Inspired by how humans comprehend long videos - by first skimming globally and then examining relevant clips for details - we introduce LongVT, an end-to-end agentic framework that enables "Thinking with Long Videos" via interleaved Multimodal Chain-of-Tool-Thought. Specifically, we exploit LMMs' inherent temporal grounding ability as a native video cropping tool to zoom in on a specific video clip and resample finer-grained video frames. This global-to-local reasoning loop continues until answers are grounded in retrieved visual evidence. Given the scarcity of fine-grained question-answering (QA) data for the long video reasoning task, we curate and will release a data suite named VideoSIAH to facilitate both training and evaluation. Specifically, our training dataset consists of 247.9K samples for tool-integrated cold-start supervised fine-tuning, 1.6K samples for agentic reinforcement learning, and 15.4K samples for agentic reinforcement fine-tuning, respectively. Our evaluation benchmark consists of 1,280 QA pairs that are carefully curated through a semi-automatic data pipeline with human-in-the-loop validation. With a meticulously designed three-stage training strategy and extensive empirical validation, LongVT consistently outperforms existing strong baselines across four challenging long-video understanding and reasoning benchmarks. Our codes, data, and model checkpoints are publicly available at this https URL .

2. **Infinity-RoPE: Action-Controllable Infinite Video Generation Emerges From Autoregressive Self-Rollout** - 👍 5
   - 기관: ·5 authors
   - [HF 페이지](https://huggingface.co/papers/2511.20649)
   - [논문 링크](https://arxiv.org/abs/2511.20649)
   - Abstract: Current autoregressive video diffusion models are constrained by three core bottlenecks: (i) the finite temporal horizon imposed by the base model's 3D Rotary Positional Embedding (3D-RoPE), (ii) slow prompt responsiveness in maintaining fine-grained action control during long-form rollouts, and (iii) the inability to realize discontinuous cinematic transitions within a single generation stream. We introduce $\infty$-RoPE, a unified inference-time framework that addresses all three limitations through three interconnected components: Block-Relativistic RoPE, KV Flush, and RoPE Cut. Block-Relativistic RoPE reformulates temporal encoding as a moving local reference frame, where each newly generated latent block is rotated relative to the base model's maximum frame horizon while earlier blocks are rotated backward to preserve relative temporal geometry. This relativistic formulation eliminates fixed temporal positions, enabling continuous video generation far beyond the base positional limits. To obtain fine-grained action control without re-encoding, KV Flush renews the KV cache by retaining only two latent frames, the global sink and the last generated latent frame, thereby ensuring immediate prompt responsiveness. Finally, RoPE Cut introduces controlled discontinuities in temporal RoPE coordinates, enabling multi-cut scene transitions within a single continuous rollout. Together, these components establish $\infty$-RoPE as a training-free foundation for infinite-horizon, controllable, and cinematic video diffusion. Comprehensive experiments show that $\infty$-RoPE consistently surpasses previous autoregressive models in overall VBench scores.

