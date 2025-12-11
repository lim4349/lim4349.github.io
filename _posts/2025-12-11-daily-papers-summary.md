---
title: Hugging Face Daily Papers - 2025-12-11
date: 2025-12-11 09:15:00 +0900
categories: ['Daily Papers', '일간']
tags: ['huggingface', 'papers', 'daily', 'ai']
author: lim4349
---

# Hugging Face Daily Papers - 2025-12-11

총 **4개**의 논문이 수집되었습니다.

## 📊 좋아요 순위

1. **StereoWorld: Geometry-Aware Monocular-to-Stereo Video Generation** - 👍 0
   - 기관: ·11 authors
   - [HF 페이지](https://huggingface.co/papers/2512.09363)
   - [논문 링크](https://arxiv.org/abs/2512.09363)
   - Abstract: The growing adoption of XR devices has fueled strong demand for high-quality stereo video, yet its production remains costly and artifact-prone. To address this challenge, we present StereoWorld, an end-to-end framework that repurposes a pretrained video generator for high-fidelity monocular-to-stereo video generation. Our framework jointly conditions the model on the monocular video input while explicitly supervising the generation with a geometry-aware regularization to ensure 3D structural fidelity. A spatio-temporal tiling scheme is further integrated to enable efficient, high-resolution synthesis. To enable large-scale training and evaluation, we curate a high-definition stereo video dataset containing over 11M frames aligned to natural human interpupillary distance (IPD). Extensive experiments demonstrate that StereoWorld substantially outperforms prior methods, generating stereo videos with superior visual fidelity and geometric consistency. The project webpage is available at this https URL .

2. **OmniPSD: Layered PSD Generation with Diffusion Transformer** - 👍 0
   - 기관: ·4 authors
   - [HF 페이지](https://huggingface.co/papers/2512.09247)
   - [논문 링크](https://arxiv.org/abs/2512.09247)
   - Abstract: Recent advances in diffusion models have greatly improved image generation and editing, yet generating or reconstructing layered PSD files with transparent alpha channels remains highly challenging. We propose OmniPSD, a unified diffusion framework built upon the Flux ecosystem that enables both text-to-PSD generation and image-to-PSD decomposition through in-context learning. For text-to-PSD generation, OmniPSD arranges multiple target layers spatially into a single canvas and learns their compositional relationships through spatial attention, producing semantically coherent and hierarchically structured layers. For image-to-PSD decomposition, it performs iterative in-context editing, progressively extracting and erasing textual and foreground components to reconstruct editable PSD layers from a single flattened image. An RGBA-VAE is employed as an auxiliary representation module to preserve transparency without affecting structure learning. Extensive experiments on our new RGBA-layered dataset demonstrate that OmniPSD achieves high-fidelity generation, structural consistency, and transparency awareness, offering a new paradigm for layered design generation and decomposition with diffusion transformers.

3. **Learning Unmasking Policies for Diffusion Language Models** - 👍 0
   - 기관: Apple
   - [HF 페이지](https://huggingface.co/papers/2512.09106)
   - [논문 링크](https://arxiv.org/abs/2512.09106)
   - Abstract: Diffusion (Large) Language Models (dLLMs) now match the downstream performance of their autoregressive counterparts on many tasks, while holding the promise of being more efficient during inference. One particularly successful variant is masked discrete diffusion, in which a buffer filled with special mask tokens is progressively replaced with tokens sampled from the model's vocabulary. Efficiency can be gained by unmasking several tokens in parallel, but doing too many at once risks degrading the generation quality. Thus, one critical design aspect of dLLMs is the sampling procedure that selects, at each step of the diffusion process, which tokens to replace. Indeed, recent work has found that heuristic strategies such as confidence thresholding lead to both higher quality and token throughput compared to random unmasking. However, such heuristics have downsides: they require manual tuning, and we observe that their performance degrades with larger buffer sizes. In this work, we instead propose to train sampling procedures using reinforcement learning. Specifically, we formalize masked diffusion sampling as a Markov decision process in which the dLLM serves as the environment, and propose a lightweight policy architecture based on a single-layer transformer that maps dLLM token confidences to unmasking decisions. Our experiments show that these trained policies match the performance of state-of-the-art heuristics when combined with semi-autoregressive generation, while outperforming them in the full diffusion setting. We also examine the transferability of these policies, finding that they can generalize to new underlying dLLMs and longer sequence lengths. However, we also observe that their performance degrades when applied to out-of-domain data, and that fine-grained tuning of the accuracy-efficiency trade-off can be challenging with our approach.

4. **Reinventing Clinical Dialogue: Agentic Paradigms for LLM Enabled Healthcare Communication** - 👍 0
   - 기관: ·5 authors
   - [HF 페이지](https://huggingface.co/papers/2512.01453)
   - [논문 링크](https://arxiv.org/abs/2512.01453)
   - Abstract: Clinical dialogue represents a complex duality requiring both the empathetic fluency of natural conversation and the rigorous precision of evidence-based medicine. While Large Language Models possess unprecedented linguistic capabilities, their architectural reliance on reactive and stateless processing often favors probabilistic plausibility over factual veracity. This structural limitation has catalyzed a paradigm shift in medical AI from generative text prediction to agentic autonomy, where the model functions as a central reasoning engine capable of deliberate planning and persistent memory. Moving beyond existing reviews that primarily catalog downstream applications, this survey provides a first-principles analysis of the cognitive architecture underpinning this shift. We introduce a novel taxonomy structured along the orthogonal axes of knowledge source and agency objective to delineate the provenance of clinical knowledge against the system's operational scope. This framework facilitates a systematic analysis of the intrinsic trade-offs between creativity and reliability by categorizing methods into four archetypes: \textit{Latent Space Clinicians}, \textit{Emergent Planners}, \textit{Grounded Synthesizers}, and \textit{Verifiable Workflow Automators}. For each paradigm, we deconstruct the technical realization across the entire cognitive pipeline, encompassing strategic planning, memory management, action execution, collaboration, and evolution to reveal how distinct architectural choices balance the tension between autonomy and safety.

