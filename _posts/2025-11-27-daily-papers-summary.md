---
title: Hugging Face Daily Papers - 2025-11-27
date: 2025-11-27 09:15:00 +0900
categories: ['Daily Papers', '일간']
tags: ['huggingface', 'papers', 'daily', 'ai']
author: lim4349
---

# Hugging Face Daily Papers - 2025-11-27

총 **4개**의 논문이 수집되었습니다.

## 📊 좋아요 순위

1. **Monet: Reasoning in Latent Visual Space Beyond Images and Language** - 👍 2
   - 기관: ·8 authors
   - [HF 페이지](https://huggingface.co/papers/2511.21395)
   - [논문 링크](https://arxiv.org/abs/2511.21395)
   - Abstract: "Thinking with images" has emerged as an effective paradigm for advancing visual reasoning, extending beyond text-only chains of thought by injecting visual evidence into intermediate reasoning steps. However, existing methods fall short of human-like abstract visual thinking, as their flexibility is fundamentally limited by external tools. In this work, we introduce Monet, a training framework that enables multimodal large language models (MLLMs) to reason directly within the latent visual space by generating continuous embeddings that function as intermediate visual thoughts. We identify two core challenges in training MLLMs for latent visual reasoning: high computational cost in latent-vision alignment and insufficient supervision over latent embeddings, and address them with a three-stage distillation-based supervised fine-tuning (SFT) pipeline. We further reveal a limitation of applying GRPO to latent reasoning: it primarily enhances text-based reasoning rather than latent reasoning. To overcome this, we propose VLPO (Visual-latent Policy Optimization), a reinforcement learning method that explicitly incorporates latent embeddings into policy gradient updates. To support SFT, we construct Monet-SFT-125K, a high-quality text-image interleaved CoT dataset containing 125K real-world, chart, OCR, and geometry CoTs. Our model, Monet-7B, shows consistent gains across real-world perception and reasoning benchmarks and exhibits strong out-of-distribution generalization on challenging abstract visual reasoning tasks. We also empirically analyze the role of each training component and discuss our early unsuccessful attempts, providing insights for future developments in visual latent reasoning. Our model, data, and code are available at this https URL .

2. **NVIDIA Nemotron Parse 1.1** - 👍 1
   - 기관: NVIDIA
   - [HF 페이지](https://huggingface.co/papers/2511.20478)
   - [논문 링크](https://arxiv.org/abs/2511.20478)
   - Abstract: We introduce Nemotron-Parse-1.1, a lightweight document parsing and OCR model that advances the capabilities of its predecessor, Nemoretriever-Parse-1.0. Nemotron-Parse-1.1 delivers improved capabilities across general OCR, markdown formatting, structured table parsing, and text extraction from pictures, charts, and diagrams. It also supports a longer output sequence length for visually dense documents. As with its predecessor, it extracts bounding boxes of text segments, as well as corresponding semantic classes. Nemotron-Parse-1.1 follows an encoder-decoder architecture with 885M parameters, including a compact 256M-parameter language decoder. It achieves competitive accuracy on public benchmarks making it a strong lightweight OCR solution. We release the model weights publicly on Huggingface, as well as an optimized NIM container, along with a subset of the training data as part of the broader Nemotron-VLM-v2 dataset. Additionally, we release Nemotron-Parse-1.1-TC which operates on a reduced vision token length, offering a 20% speed improvement with minimal quality degradation.

3. **Terminal Velocity Matching** - 👍 1
   - 기관: ·4 authors
   - [HF 페이지](https://huggingface.co/papers/2511.19797)
   - [논문 링크](https://arxiv.org/abs/2511.19797)
   - Abstract: We propose Terminal Velocity Matching (TVM), a generalization of flow matching that enables high-fidelity one- and few-step generative modeling. TVM models the transition between any two diffusion timesteps and regularizes its behavior at its terminal time rather than at the initial time. We prove that TVM provides an upper bound on the $2$-Wasserstein distance between data and model distributions when the model is Lipschitz continuous. However, since Diffusion Transformers lack this property, we introduce minimal architectural changes that achieve stable, single-stage training. To make TVM efficient in practice, we develop a fused attention kernel that supports backward passes on Jacobian-Vector Products, which scale well with transformer architectures. On ImageNet-256x256, TVM achieves 3.29 FID with a single function evaluation (NFE) and 1.99 FID with 4 NFEs. It similarly achieves 4.32 1-NFE FID and 2.94 4-NFE FID on ImageNet-512x512, representing state-of-the-art performance for one/few-step models from scratch.

4. **Inferix: A Block-Diffusion based Next-Generation Inference Engine for World Simulation** - 👍 0
   - 기관: ·16 authors
   - [HF 페이지](https://huggingface.co/papers/2511.20714)
   - [논문 링크](https://arxiv.org/abs/2511.20714)
   - Abstract: World models serve as core simulators for fields such as agentic AI, embodied AI, and gaming, capable of generating long, physically realistic, and interactive high-quality videos. Moreover, scaling these models could unlock emergent capabilities in visual perception, understanding, and reasoning, paving the way for a new paradigm that moves beyond current LLM-centric vision foundation models. A key breakthrough empowering them is the semi-autoregressive (block-diffusion) decoding paradigm, which merges the strengths of diffusion and autoregressive methods by generating video tokens in block-applying diffusion within each block while conditioning on previous ones, resulting in more coherent and stable video sequences. Crucially, it overcomes limitations of standard video diffusion by reintroducing LLM-style KV Cache management, enabling efficient, variable-length, and high-quality generation. Therefore, Inferix is specifically designed as a next-generation inference engine to enable immersive world synthesis through optimized semi-autoregressive decoding processes. This dedicated focus on world simulation distinctly sets it apart from systems engineered for high-concurrency scenarios (like vLLM or SGLang) and from classic video diffusion models (such as xDiTs). Inferix further enhances its offering with interactive video streaming and profiling, enabling real-time interaction and realistic simulation to accurately model world dynamics. Additionally, it supports efficient benchmarking through seamless integration of LV-Bench, a new fine-grained evaluation benchmark tailored for minute-long video generation scenarios. We hope the community will work together to advance Inferix and foster world model exploration.

