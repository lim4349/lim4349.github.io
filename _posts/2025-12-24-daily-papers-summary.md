---
title: Hugging Face Daily Papers - 2025-12-24
date: 2025-12-24 09:15:00 +0900
categories: ['Daily Papers', '일간']
tags: ['huggingface', 'papers', 'daily', 'ai']
author: lim4349
---

# Hugging Face Daily Papers - 2025-12-24

총 **5개**의 논문이 수집되었습니다.

## 📊 좋아요 순위

1. **SpatialTree: How Spatial Abilities Branch Out in MLLMs** - 👍 11
   - 기관: ByteDance Seed
   - [HF 페이지](https://huggingface.co/papers/2512.20617)
   - [논문 링크](https://arxiv.org/abs/2512.20617)
   - Abstract: Cognitive science suggests that spatial ability develops progressively-from perception to reasoning and interaction. Yet in multimodal LLMs (MLLMs), this hierarchy remains poorly understood, as most studies focus on a narrow set of tasks. We introduce SpatialTree, a cognitive-science-inspired hierarchy that organizes spatial abilities into four levels: low-level perception (L1), mental mapping (L2), simulation (L3), and agentic competence (L4). Based on this taxonomy, we construct the first capability-centric hierarchical benchmark, thoroughly evaluating mainstream MLLMs across 27 sub-abilities. The evaluation results reveal a clear structure: L1 skills are largely orthogonal, whereas higher-level skills are strongly correlated, indicating increasing interdependency. Through targeted supervised fine-tuning, we uncover a surprising transfer dynamic-negative transfer within L1, but strong cross-level transfer from low- to high-level abilities with notable synergy. Finally, we explore how to improve the entire hierarchy. We find that naive RL that encourages extensive "thinking" is unreliable: it helps complex reasoning but hurts intuitive perception. We propose a simple auto-think strategy that suppresses unnecessary deliberation, enabling RL to consistently improve performance across all levels. By building SpatialTree, we provide a proof-of-concept framework for understanding and systematically scaling spatial abilities in MLLMs.

2. **Bottom-up Policy Optimization: Your Language Model Policy Secretly Contains Internal Policies** - 👍 5
   - 기관: Tencent
   - [HF 페이지](https://huggingface.co/papers/2512.19673)
   - [논문 링크](https://arxiv.org/abs/2512.19673)
   - Abstract: Existing reinforcement learning (RL) approaches treat large language models (LLMs) as a single unified policy, overlooking their internal mechanisms. Understanding how policy evolves across layers and modules is therefore crucial for enabling more targeted optimization and raveling out complex reasoning mechanisms. In this paper, we decompose the language model policy by leveraging the intrinsic split of the Transformer residual stream and the equivalence between the composition of hidden states with the unembedding matrix and the resulting samplable policy. This decomposition reveals Internal Layer Policies, corresponding to contributions from individual layers, and Internal Modular Policies, which align with the self-attention and feed-forward network (FFN) components within each layer. By analyzing the entropy of internal policy, we find that: (a) Early layers keep high entropy for exploration, top layers converge to near-zero entropy for refinement, with convergence patterns varying across model series. (b) LLama's prediction space rapidly converges in the final layer, whereas Qwen-series models, especially Qwen3, exhibit a more human-like, progressively structured reasoning pattern. Motivated by these findings, we propose Bottom-up Policy Optimization (BuPO), a novel RL paradigm that directly optimizes the internal layer policy during early training. By aligning training objective at lower layer, BuPO reconstructs foundational reasoning capabilities and achieves superior performance. Extensive experiments on complex reasoning benchmarks demonstrates the effectiveness of our method. Our code is available at this https URL .

3. **Step-DeepResearch Technical Report** - 👍 4
   - 기관: StepFun
   - [HF 페이지](https://huggingface.co/papers/2512.20491)
   - [논문 링크](https://arxiv.org/abs/2512.20491)
   - Abstract: As LLMs shift toward autonomous agents, Deep Research has emerged as a pivotal metric. However, existing academic benchmarks like BrowseComp often fail to meet real-world demands for open-ended research, which requires robust skills in intent recognition, long-horizon decision-making, and cross-source verification. To address this, we introduce Step-DeepResearch, a cost-effective, end-to-end agent. We propose a Data Synthesis Strategy Based on Atomic Capabilities to reinforce planning and report writing, combined with a progressive training path from agentic mid-training to SFT and RL. Enhanced by a Checklist-style Judger, this approach significantly improves robustness. Furthermore, to bridge the evaluation gap in the Chinese domain, we establish ADR-Bench for realistic deep research scenarios. Experimental results show that Step-DeepResearch (32B) scores 61.4% on Scale AI Research Rubrics. On ADR-Bench, it significantly outperforms comparable models and rivals SOTA closed-source models like OpenAI and Gemini DeepResearch. These findings prove that refined training enables medium-sized models to achieve expert-level capabilities at industry-leading cost-efficiency.

4. **SAM Audio: Segment Anything in Audio** - 👍 4
   - 기관: AI at Meta
   - [HF 페이지](https://huggingface.co/papers/2512.18099)
   - [논문 링크](https://arxiv.org/abs/2512.18099)
   - Abstract: General audio source separation is a key capability for multimodal AI systems that can perceive and reason about sound. Despite substantial progress in recent years, existing separation models are either domain-specific, designed for fixed categories such as speech or music, or limited in controllability, supporting only a single prompting modality such as text. In this work, we present SAM Audio, a foundation model for general audio separation that unifies text, visual, and temporal span prompting within a single framework. Built on a diffusion transformer architecture, SAM Audio is trained with flow matching on large-scale audio data spanning speech, music, and general sounds, and can flexibly separate target sources described by language, visual masks, or temporal spans. The model achieves state-of-the-art performance across a diverse suite of benchmarks, including general sound, speech, music, and musical instrument separation in both in-the-wild and professionally produced audios, substantially outperforming prior general-purpose and specialized systems. Furthermore, we introduce a new real-world separation benchmark with human-labeled multimodal prompts and a reference-free evaluation model that correlates strongly with human judgment.

5. **QuantiPhy: A Quantitative Benchmark Evaluating Physical Reasoning Abilities of Vision-Language Models** - 👍 1
   - 기관: Stanford University
   - [HF 페이지](https://huggingface.co/papers/2512.19526)
   - [논문 링크](https://arxiv.org/abs/2512.19526)
   - Abstract: Understanding the physical world is essential for generalist AI agents. However, it remains unclear whether state-of-the-art vision perception models (e.g., large VLMs) can reason physical properties quantitatively. Existing evaluations are predominantly VQA-based and qualitative, offering limited insight into whether these models can infer the kinematic quantities of moving objects from video observations. To address this, we present QuantiPhy, the first benchmark designed to quantitatively measure a VLM's physical reasoning ability. Comprising more than 3.3K video-text instances with numerical ground truth, QuantiPhy evaluates a VLM's performance on estimating an object's size, velocity, and acceleration at a given timestamp, using one of these properties as an input prior. The benchmark standardizes prompts and scoring to assess numerical accuracy, enabling fair comparisons across models. Our experiments on state-of-the-art VLMs reveal a consistent gap between their qualitative plausibility and actual numerical correctness. We further provide an in-depth analysis of key factors like background noise, counterfactual priors, and strategic prompting and find that state-of-the-art VLMs lean heavily on pre-trained world knowledge rather than faithfully using the provided visual and textual inputs as references when reasoning kinematic properties quantitatively. QuantiPhy offers the first rigorous, scalable testbed to move VLMs beyond mere verbal plausibility toward a numerically grounded physical understanding.

