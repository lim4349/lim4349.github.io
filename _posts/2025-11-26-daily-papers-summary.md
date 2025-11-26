---
title: Hugging Face Daily Papers - 2025-11-26
date: 2025-11-26 09:15:00 +0900
categories: ['Daily Papers', '일간']
tags: ['huggingface', 'papers', 'daily', 'ai']
author: lim4349
---

# Hugging Face Daily Papers - 2025-11-26

총 **6개**의 논문이 수집되었습니다.

## 📊 좋아요 순위

1. **SteadyDancer: Harmonized and Coherent Human Image Animation with First-Frame Preservation** - 👍 4
   - 기관: Multimedia Computing Group-Nanjing University
   - [HF 페이지](https://huggingface.co/papers/2511.19320)
   - [논문 링크](https://arxiv.org/abs/2511.19320)
   - Abstract: Preserving first-frame identity while ensuring precise motion control is a fundamental challenge in human image animation. The Image-to-Motion Binding process of the dominant Reference-to-Video (R2V) paradigm overlooks critical spatio-temporal misalignments common in real-world applications, leading to failures such as identity drift and visual artifacts. We introduce SteadyDancer, an Image-to-Video (I2V) paradigm-based framework that achieves harmonized and coherent animation and is the first to ensure first-frame preservation robustly. Firstly, we propose a Condition-Reconciliation Mechanism to harmonize the two conflicting conditions, enabling precise control without sacrificing fidelity. Secondly, we design Synergistic Pose Modulation Modules to generate an adaptive and coherent pose representation that is highly compatible with the reference image. Finally, we employ a Staged Decoupled-Objective Training Pipeline that hierarchically optimizes the model for motion fidelity, visual quality, and temporal coherence. Experiments demonstrate that SteadyDancer achieves state-of-the-art performance in both appearance fidelity and motion control, while requiring significantly fewer training resources than comparable methods.

2. **iMontage: Unified, Versatile, Highly Dynamic Many-to-many Image Generation** - 👍 1
   - 기관: StepFun
   - [HF 페이지](https://huggingface.co/papers/2511.20635)
   - [논문 링크](https://arxiv.org/abs/2511.20635)
   - Abstract: Pre-trained video models learn powerful priors for generating high-quality, temporally coherent content. While these models excel at temporal coherence, their dynamics are often constrained by the continuous nature of their training data. We hypothesize that by injecting the rich and unconstrained content diversity from image data into this coherent temporal framework, we can generate image sets that feature both natural transitions and a far more expansive dynamic range. To this end, we introduce iMontage, a unified framework designed to repurpose a powerful video model into an all-in-one image generator. The framework consumes and produces variable-length image sets, unifying a wide array of image generation and editing tasks. To achieve this, we propose an elegant and minimally invasive adaptation strategy, complemented by a tailored data curation process and training paradigm. This approach allows the model to acquire broad image manipulation capabilities without corrupting its invaluable original motion priors. iMontage excels across several mainstream many-in-many-out tasks, not only maintaining strong cross-image contextual consistency but also generating scenes with extraordinary dynamics that surpass conventional scopes. Find our homepage at: this https URL .

3. **GigaWorld-0: World Models as Data Engine to Empower Embodied AI** - 👍 1
   - 기관: ·25 authors
   - [HF 페이지](https://huggingface.co/papers/2511.19861)
   - [논문 링크](https://arxiv.org/abs/2511.19861)
   - Abstract: World models are emerging as a foundational paradigm for scalable, data-efficient embodied AI. In this work, we present GigaWorld-0, a unified world model framework designed explicitly as a data engine for Vision-Language-Action (VLA) learning. GigaWorld-0 integrates two synergistic components: GigaWorld-0-Video, which leverages large-scale video generation to produce diverse, texture-rich, and temporally coherent embodied sequences under fine-grained control of appearance, camera viewpoint, and action semantics; and GigaWorld-0-3D, which combines 3D generative modeling, 3D Gaussian Splatting reconstruction, physically differentiable system identification, and executable motion planning to ensure geometric consistency and physical realism. Their joint optimization enables the scalable synthesis of embodied interaction data that is visually compelling, spatially coherent, physically plausible, and instruction-aligned. Training at scale is made feasible through our efficient GigaTrain framework, which exploits FP8-precision and sparse attention to drastically reduce memory and compute requirements. We conduct comprehensive evaluations showing that GigaWorld-0 generates high-quality, diverse, and controllable data across multiple dimensions. Critically, VLA model (e.g., GigaBrain-0) trained on GigaWorld-0-generated data achieve strong real-world performance, significantly improving generalization and task success on physical robots without any real-world interaction during training.

4. **HunyuanOCR Technical Report** - 👍 1
   - 기관: Tencent Hunyuan
   - [HF 페이지](https://huggingface.co/papers/2511.19575)
   - [논문 링크](https://arxiv.org/abs/2511.19575)
   - Abstract: This paper presents HunyuanOCR, a commercial-grade, open-source, and lightweight (1B parameters) Vision-Language Model (VLM) dedicated to OCR tasks. The architecture comprises a Native Vision Transformer (ViT) and a lightweight LLM connected via an MLP adapter. HunyuanOCR demonstrates superior performance, outperforming commercial APIs, traditional pipelines, and larger models (e.g., Qwen3-VL-4B). Specifically, it surpasses current public solutions in perception tasks (Text Spotting, Parsing) and excels in semantic tasks (IE, Text Image Translation), securing first place in the ICDAR 2025 DIMT Challenge (Small Model Track). Furthermore, it achieves state-of-the-art (SOTA) results on OCRBench among VLMs with fewer than 3B parameters. HunyuanOCR achieves breakthroughs in three key aspects: 1) Unifying Versatility and Efficiency: We implement comprehensive support for core capabilities including spotting, parsing, IE, VQA, and translation within a lightweight framework. This addresses the limitations of narrow "OCR expert models" and inefficient "General VLMs". 2) Streamlined End-to-End Architecture: Adopting a pure end-to-end paradigm eliminates dependencies on pre-processing modules (e.g., layout analysis). This fundamentally resolves error propagation common in traditional pipelines and simplifies system deployment. 3) Data-Driven and RL Strategies: We confirm the critical role of high-quality data and, for the first time in the industry, demonstrate that Reinforcement Learning (RL) strategies yield significant performance gains in OCR tasks. HunyuanOCR is officially open-sourced on HuggingFace. We also provide a high-performance deployment solution based on vLLM, placing its production efficiency in the top tier. We hope this model will advance frontier research and provide a solid foundation for industrial applications.

5. **PhysChoreo: Physics-Controllable Video Generation with Part-Aware Semantic Grounding** - 👍 0
   - 기관: ·7 authors
   - [HF 페이지](https://huggingface.co/papers/2511.20562)
   - [논문 링크](https://arxiv.org/abs/2511.20562)
   - Abstract: While recent video generation models have achieved significant visual fidelity, they often suffer from the lack of explicit physical controllability and plausibility. To address this, some recent studies attempted to guide the video generation with physics-based rendering. However, these methods face inherent challenges in accurately modeling complex physical properties and effectively control ling the resulting physical behavior over extended temporal sequences. In this work, we introduce PhysChoreo, a novel framework that can generate videos with diverse controllability and physical realism from a single image. Our method consists of two stages: first, it estimates the static initial physical properties of all objects in the image through part-aware physical property reconstruction. Then, through temporally instructed and physically editable simulation, it synthesizes high-quality videos with rich dynamic behaviors and physical realism. Experimental results show that PhysChoreo can generate videos with rich behaviors and physical realism, outperforming state-of-the-art methods on multiple evaluation metrics.

6. **Unified all-atom molecule generation with neural fields** - 👍 0
   - 기관: Genentech
   - [HF 페이지](https://huggingface.co/papers/2511.15906)
   - [논문 링크](https://arxiv.org/abs/2511.15906)
   - Abstract: Generative models for structure-based drug design are often limited to a specific modality, restricting their broader applicability. To address this challenge, we introduce FuncBind, a framework based on computer vision to generate target-conditioned, all-atom molecules across atomic systems. FuncBind uses neural fields to represent molecules as continuous atomic densities and employs score-based generative models with modern architectures adapted from the computer vision literature. This modality-agnostic representation allows a single unified model to be trained on diverse atomic systems, from small to large molecules, and handle variable atom/residue counts, including non-canonical amino acids. FuncBind achieves competitive in silico performance in generating small molecules, macrocyclic peptides, and antibody complementarity-determining region loops, conditioned on target structures. FuncBind also generated in vitro novel antibody binders via de novo redesign of the complementarity-determining region H3 loop of two chosen co-crystal structures. As a final contribution, we introduce a new dataset and benchmark for structure-conditioned macrocyclic peptide generation. The code is available at this https URL .

