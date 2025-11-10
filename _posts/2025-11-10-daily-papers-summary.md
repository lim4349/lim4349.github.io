---
title: Hugging Face Daily Papers - 2025-11-10
date: 2025-11-10 09:15:00 +0900
categories: ['Daily Papers', '일간']
tags: ['huggingface', 'papers', 'daily', 'ai']
author: lim4349
---

# Hugging Face Daily Papers - 2025-11-10

총 **6개**의 논문이 수집되었습니다.

## 📊 좋아요 순위

1. **Too Good to be Bad: On the Failure of LLMs to Role-Play Villains** - 👍 1
   - 기관: Tencent
   - [HF 페이지](https://huggingface.co/papers/2511.04962)
   - [논문 링크](https://arxiv.org/abs/2511.04962)
   - Abstract: Large Language Models (LLMs) are increasingly tasked with creative generation, including the simulation of fictional characters. However, their ability to portray non-prosocial, antagonistic personas remains largely unexamined. We hypothesize that the safety alignment of modern LLMs creates a fundamental conflict with the task of authentically role-playing morally ambiguous or villainous characters. To investigate this, we introduce the Moral RolePlay benchmark, a new dataset featuring a four-level moral alignment scale and a balanced test set for rigorous evaluation. We task state-of-the-art LLMs with role-playing characters from moral paragons to pure villains. Our large-scale evaluation reveals a consistent, monotonic decline in role-playing fidelity as character morality decreases. We find that models struggle most with traits directly antithetical to safety principles, such as ``Deceitful'' and ``Manipulative'', often substituting nuanced malevolence with superficial aggression. Furthermore, we demonstrate that general chatbot proficiency is a poor predictor of villain role-playing ability, with highly safety-aligned models performing particularly poorly. Our work provides the first systematic evidence of this critical limitation, highlighting a key tension between model safety and creative fidelity. Our benchmark and findings pave the way for developing more nuanced, context-aware alignment methods.

2. **Visual Spatial Tuning** - 👍 0
   - 기관: ByteDance Seed
   - [HF 페이지](https://huggingface.co/papers/2511.05491)
   - [논문 링크](https://arxiv.org/abs/2511.05491)
   - Abstract: Capturing spatial relationships from visual inputs is a cornerstone of human-like general intelligence. Several previous studies have tried to enhance the spatial awareness of Vision-Language Models (VLMs) by adding extra expert encoders, which brings extra overhead and usually harms general capabilities. To enhance the spatial ability in general architectures, we introduce Visual Spatial Tuning (VST), a comprehensive framework to cultivate VLMs with human-like visuospatial abilities, from spatial perception to reasoning. We first attempt to enhance spatial perception in VLMs by constructing a large-scale dataset termed VST-P, which comprises 4.1 million samples spanning 19 skills across single views, multiple images, and videos. Then, we present VST-R, a curated dataset with 135K samples that instruct models to reason in space. In particular, we adopt a progressive training pipeline: supervised fine-tuning to build foundational spatial knowledge, followed by reinforcement learning to further improve spatial reasoning abilities. Without the side-effect to general capabilities, the proposed VST consistently achieves state-of-the-art results on several spatial benchmarks, including $34.8\%$ on MMSI-Bench and $61.2\%$ on VSIBench. It turns out that the Vision-Language-Action models can be significantly enhanced with the proposed spatial tuning paradigm, paving the way for more physically grounded AI.

3. **Dense Motion Captioning** - 👍 0
   - 기관: ·4 authors
   - [HF 페이지](https://huggingface.co/papers/2511.05369)
   - [논문 링크](https://arxiv.org/abs/2511.05369)
   - Abstract: Recent advances in 3D human motion and language integration have primarily focused on text-to-motion generation, leaving the task of motion understanding relatively unexplored. We introduce Dense Motion Captioning, a novel task that aims to temporally localize and caption actions within 3D human motion sequences. Current datasets fall short in providing detailed temporal annotations and predominantly consist of short sequences featuring few actions. To overcome these limitations, we present the Complex Motion Dataset (CompMo), the first large-scale dataset featuring richly annotated, complex motion sequences with precise temporal boundaries. Built through a carefully designed data generation pipeline, CompMo includes 60,000 motion sequences, each composed of multiple actions ranging from at least two to ten, accurately annotated with their temporal extents. We further present DEMO, a model that integrates a large language model with a simple motion adapter, trained to generate dense, temporally grounded captions. Our experiments show that DEMO substantially outperforms existing methods on CompMo as well as on adapted benchmarks, establishing a robust baseline for future research in 3D motion understanding and captioning.

4. **DeepEyesV2: Toward Agentic Multimodal Model** - 👍 0
   - 기관: ·6 authors
   - [HF 페이지](https://huggingface.co/papers/2511.05271)
   - [논문 링크](https://arxiv.org/abs/2511.05271)
   - Abstract: Agentic multimodal models should not only comprehend text and images, but also actively invoke external tools, such as code execution environments and web search, and integrate these operations into reasoning. In this work, we introduce DeepEyesV2 and explore how to build an agentic multimodal model from the perspectives of data construction, training methods, and model evaluation. We observe that direct reinforcement learning alone fails to induce robust tool-use behavior. This phenomenon motivates a two-stage training pipeline: a cold-start stage to establish tool-use patterns, and reinforcement learning stage to further refine tool invocation. We curate a diverse, moderately challenging training dataset, specifically including examples where tool use is beneficial. We further introduce RealX-Bench, a comprehensive benchmark designed to evaluate real-world multimodal reasoning, which inherently requires the integration of multiple capabilities, including perception, search, and reasoning. We evaluate DeepEyesV2 on RealX-Bench and other representative benchmarks, demonstrating its effectiveness across real-world understanding, mathematical reasoning, and search-intensive tasks. Moreover, DeepEyesV2 exhibits task-adaptive tool invocation, tending to use image operations for perception tasks and numerical computations for reasoning tasks. Reinforcement learning further enables complex tool combinations and allows model to selectively invoke tools based on context. We hope our study can provide guidance for community in developing agentic multimodal models.

5. **Towards Mitigating Hallucinations in Large Vision-Language Models by
  Refining Textual Embeddings** - 👍 0
   - 기관: ·8 authors
   - [HF 페이지](https://huggingface.co/papers/2511.05017)
   - [논문 링크](https://arxiv.org/abs/2511.05017)
   - Abstract: In this work, we identify an inherent bias in prevailing LVLM architectures toward the language modality, largely resulting from the common practice of simply appending visual embeddings to the input text sequence. To address this, we propose a simple yet effective method that refines textual embeddings by integrating average-pooled visual features. Our approach demonstrably improves visual grounding and significantly reduces hallucinations on established benchmarks. While average pooling offers a straightforward, robust, and efficient means of incorporating visual information, we believe that more sophisticated fusion methods could further enhance visual grounding and cross-modal alignment. Given that the primary focus of this work is to highlight the modality imbalance and its impact on hallucinations -- and to show that refining textual embeddings with visual information mitigates this issue -- we leave exploration of advanced fusion strategies for future work.

6. **Jailbreaking in the Haystack** - 👍 0
   - 기관: ·6 authors
   - [HF 페이지](https://huggingface.co/papers/2511.04707)
   - [논문 링크](https://arxiv.org/abs/2511.04707)
   - Abstract: Recent advances in long-context language models (LMs) have enabled million-token inputs, expanding their capabilities across complex tasks like computer-use agents. Yet, the safety implications of these extended contexts remain unclear. To bridge this gap, we introduce NINJA (short for Needle-in-haystack jailbreak attack), a method that jailbreaks aligned LMs by appending benign, model-generated content to harmful user goals. Critical to our method is the observation that the position of harmful goals play an important role in safety. Experiments on standard safety benchmark, HarmBench, show that NINJA significantly increases attack success rates across state-of-the-art open and proprietary models, including LLaMA, Qwen, Mistral, and Gemini. Unlike prior jailbreaking methods, our approach is low-resource, transferable, and less detectable. Moreover, we show that NINJA is compute-optimal -- under a fixed compute budget, increasing context length can outperform increasing the number of trials in best-of-N jailbreak. These findings reveal that even benign long contexts -- when crafted with careful goal positioning -- introduce fundamental vulnerabilities in modern LMs.

