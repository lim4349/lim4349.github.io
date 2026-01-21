---
title: Hugging Face Daily Papers - 2026-01-21
date: 2026-01-21 09:15:00 +0900
categories: [Daily Papers, 일간]
tags: [huggingface, papers, daily, ai]
author: lim4349
---

# Hugging Face Daily Papers - 2026-01-21

총 **3개**의 논문이 수집되었습니다.

## 📊 좋아요 순위

1. **UniX: Unifying Autoregression and Diffusion for Chest X-Ray Understanding and Generation** - 👍 12
   - 기관: Wuhan Univeristy1
   - [HF 페이지](https://huggingface.co/papers/2601.11522)
   - [논문 링크](https://arxiv.org/abs/2601.11522)
   - Abstract: Despite recent progress, medical foundation models still struggle to unify visual understanding and generation, as these tasks have inherently conflicting goals: semantic abstraction versus pixel-level reconstruction. Existing approaches, typically based on parameter-shared autoregressive architectures, frequently lead to compromised performance in one or both tasks. To address this, we present UniX, a next-generation unified medical foundation model for chest X-ray understanding and generation. UniX decouples the two tasks into an autoregressive branch for understanding and a diffusion branch for high-fidelity generation. Crucially, a cross-modal self-attention mechanism is introduced to dynamically guide the generation process with understanding features. Coupled with a rigorous data cleaning pipeline and a multi-stage training strategy, this architecture enables synergistic collaboration between tasks while leveraging the strengths of diffusion models for superior generation. On two representative benchmarks, UniX achieves a 46.1% improvement in understanding performance (Micro-F1) and a 24.2% gain in generation quality (FD-RadDino), using only a quarter of the parameters of LLM-CXR. By achieving performance on par with task-specific models, our work establishes a scalable paradigm for synergistic medical image understanding and generation. Codes and models are available at this https URL .

2. **MemoryRewardBench: Benchmarking Reward Models for Long-Term Memory Management in Large Language Models** - 👍 3
   - 기관: Soochow University01
   - [HF 페이지](https://huggingface.co/papers/2601.11969)
   - [논문 링크](https://arxiv.org/abs/2601.11969)
   - Abstract: Existing works increasingly adopt memory-centric mechanisms to process long contexts in a segment manner, and effective memory management is one of the key capabilities that enables large language models to effectively propagate information across the entire sequence. Therefore, leveraging reward models (RMs) to automatically and reliably evaluate memory quality is critical. In this work, we introduce $\texttt{MemoryRewardBench}$, the first benchmark to systematically study the ability of RMs to evaluate long-term memory management processes. $\texttt{MemoryRewardBench}$ covers both long-context comprehension and long-form generation tasks, featuring 10 distinct settings with different memory management patterns, with context length ranging from 8K to 128K tokens. Evaluations on 13 cutting-edge RMs indicate a diminishing performance gap between open-source and proprietary models, with newer-generation models consistently outperforming their predecessors regardless of parameter count. We further expose the capabilities and fundamental limitations of current RMs in evaluating LLM memory management across diverse settings.

3. **Advances and Frontiers of LLM-based Issue Resolution in Software Engineering: A Comprehensive Survey** - 👍 2
   - 기관: DeepSoftwareAnalytics1
   - [HF 페이지](https://huggingface.co/papers/2601.11655)
   - [논문 링크](https://arxiv.org/abs/2601.11655)
   - Abstract: Issue resolution, a complex Software Engineering (SWE) task integral to real-world development, has emerged as a compelling challenge for artificial intelligence. The establishment of benchmarks like SWE-bench revealed this task as profoundly difficult for large language models, thereby significantly accelerating the evolution of autonomous coding agents. This paper presents a systematic survey of this emerging domain. We begin by examining data construction pipelines, covering automated collection and synthesis approaches. We then provide a comprehensive analysis of methodologies, spanning training-free frameworks with their modular components to training-based techniques, including supervised fine-tuning and reinforcement learning. Subsequently, we discuss critical analyses of data quality and agent behavior, alongside practical applications. Finally, we identify key challenges and outline promising directions for future research. An open-source repository is maintained at this https URL to serve as a dynamic resource in this field.

