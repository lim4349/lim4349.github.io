---
title: Hugging Face Daily Papers - 2025-12-19
date: 2025-12-19 09:15:00 +0900
categories: ['Daily Papers', '일간']
tags: ['huggingface', 'papers', 'daily', 'ai']
author: lim4349
---

# Hugging Face Daily Papers - 2025-12-19

총 **7개**의 논문이 수집되었습니다.

## 📊 좋아요 순위

1. **Kling-Omni Technical Report** - 👍 6
   - 기관: Kling Team
   - [HF 페이지](https://huggingface.co/papers/2512.16776)
   - [논문 링크](https://arxiv.org/abs/2512.16776)
   - Abstract: We present Kling-Omni, a generalist generative framework designed to synthesize high-fidelity videos directly from multimodal visual language inputs. Adopting an end-to-end perspective, Kling-Omni bridges the functional separation among diverse video generation, editing, and intelligent reasoning tasks, integrating them into a holistic system. Unlike disjointed pipeline approaches, Kling-Omni supports a diverse range of user inputs, including text instructions, reference images, and video contexts, processing them into a unified multimodal representation to deliver cinematic-quality and highly-intelligent video content creation. To support these capabilities, we constructed a comprehensive data system that serves as the foundation for multimodal video creation. The framework is further empowered by efficient large-scale pre-training strategies and infrastructure optimizations for inference. Comprehensive evaluations reveal that Kling-Omni demonstrates exceptional capabilities in in-context generation, reasoning-based editing, and multimodal instruction following. Moving beyond a content creation tool, we believe Kling-Omni is a pivotal advancement toward multimodal world simulators capable of perceiving, reasoning, generating and interacting with the dynamic and complex worlds.

2. **DeContext as Defense: Safe Image Editing in Diffusion Transformers** - 👍 4
   - 기관: The Hong Kong Polytechnic University
   - [HF 페이지](https://huggingface.co/papers/2512.16625)
   - [논문 링크](https://arxiv.org/abs/2512.16625)
   - Abstract: In-context diffusion models allow users to modify images with remarkable ease and realism. However, the same power raises serious privacy concerns: personal images can be easily manipulated for identity impersonation, misinformation, or other malicious uses, all without the owner's consent. While prior work has explored input perturbations to protect against misuse in personalized text-to-image generation, the robustness of modern, large-scale in-context DiT-based models remains largely unexamined. In this paper, we propose DeContext, a new method to safeguard input images from unauthorized in-context editing. Our key insight is that contextual information from the source image propagates to the output primarily through multimodal attention layers. By injecting small, targeted perturbations that weaken these cross-attention pathways, DeContext breaks this flow, effectively decouples the link between input and output. This simple defense is both efficient and robust. We further show that early denoising steps and specific transformer blocks dominate context propagation, which allows us to concentrate perturbations where they matter most. Experiments on Flux Kontext and Step1X-Edit show that DeContext consistently blocks unwanted image edits while preserving visual quality. These results highlight the effectiveness of attention-based perturbations as a powerful defense against image manipulation.

3. **LLaDA2.0: Scaling Up Diffusion Language Models to 100B** - 👍 2
   - 기관: Ant Group
   - [HF 페이지](https://huggingface.co/papers/2512.15745)
   - [논문 링크](https://arxiv.org/abs/2512.15745)
   - Abstract: This paper presents LLaDA2.0 -- a tuple of discrete diffusion large language models (dLLM) scaling up to 100B total parameters through systematic conversion from auto-regressive (AR) models -- establishing a new paradigm for frontier-scale deployment. Instead of costly training from scratch, LLaDA2.0 upholds knowledge inheritance, progressive adaption and efficiency-aware design principle, and seamless converts a pre-trained AR model into dLLM with a novel 3-phase block-level WSD based training scheme: progressive increasing block-size in block diffusion (warm-up), large-scale full-sequence diffusion (stable) and reverting back to compact-size block diffusion (decay). Along with post-training alignment with SFT and DPO, we obtain LLaDA2.0-mini (16B) and LLaDA2.0-flash (100B), two instruction-tuned Mixture-of-Experts (MoE) variants optimized for practical deployment. By preserving the advantages of parallel decoding, these models deliver superior performance and efficiency at the frontier scale. Both models were open-sourced.

4. **Depth Any Panoramas: A Foundation Model for Panoramic Depth Estimation** - 👍 1
   - 기관: ·9 authors
   - [HF 페이지](https://huggingface.co/papers/2512.16913)
   - [논문 링크](https://arxiv.org/abs/2512.16913)
   - Abstract: In this work, we present a panoramic metric depth foundation model that generalizes across diverse scene distances. We explore a data-in-the-loop paradigm from the view of both data construction and framework design. We collect a large-scale dataset by combining public datasets, high-quality synthetic data from our UE5 simulator and text-to-image models, and real panoramic images from the web. To reduce domain gaps between indoor/outdoor and synthetic/real data, we introduce a three-stage pseudo-label curation pipeline to generate reliable ground truth for unlabeled images. For the model, we adopt DINOv3-Large as the backbone for its strong pre-trained generalization, and introduce a plug-and-play range mask head, sharpness-centric optimization, and geometry-centric optimization to improve robustness to varying distances and enforce geometric consistency across views. Experiments on multiple benchmarks (e.g., Stanford2D3D, Matterport3D, and Deep360) demonstrate strong performance and zero-shot generalization, with particularly robust and stable metric predictions in diverse real-world scenes. The project page can be found at: \href{ this https URL } { this https URL \_website/}

5. **Exploration v.s. Exploitation: Rethinking RLVR through Clipping, Entropy, and Spurious Reward** - 👍 1
   - 기관: Columbia University
   - [HF 페이지](https://huggingface.co/papers/2512.16912)
   - [논문 링크](https://arxiv.org/abs/2512.16912)
   - Abstract: This paper examines the exploration-exploitation trade-off in reinforcement learning with verifiable rewards (RLVR), a framework for improving the reasoning of Large Language Models (LLMs). Recent studies suggest that RLVR can elicit strong mathematical reasoning in LLMs through two seemingly paradoxical mechanisms: spurious rewards, which suppress exploitation by rewarding outcomes unrelated to the ground truth, and entropy minimization, which suppresses exploration by pushing the model toward more confident and deterministic outputs, highlighting a puzzling dynamic: both discouraging exploitation and discouraging exploration improve reasoning performance, yet the underlying principles that reconcile these effects remain poorly understood. We focus on two fundamental questions: (i) how policy entropy relates to performance, and (ii) whether spurious rewards yield gains, potentially through the interplay of clipping bias and model contamination. Our results show that clipping bias under spurious rewards reduces policy entropy, leading to more confident and deterministic outputs, while entropy minimization alone is insufficient for improvement. We further propose a reward-misalignment model explaining why spurious rewards can enhance performance beyond contaminated settings. Our findings clarify the mechanisms behind spurious-reward benefits and provide principles for more effective RLVR training.

6. **Adaptation of Agentic AI** - 👍 1
   - 기관: ·34 authors
   - [HF 페이지](https://huggingface.co/papers/2512.16301)
   - [논문 링크](https://arxiv.org/abs/2512.16301)
   - Abstract: Cutting-edge agentic AI systems are built on foundation models that can be adapted to plan, reason, and interact with external tools to perform increasingly complex and specialized tasks. As these systems grow in capability and scope, adaptation becomes a central mechanism for improving performance, reliability, and generalization. In this paper, we unify the rapidly expanding research landscape into a systematic framework that spans both agent adaptations and tool adaptations. We further decompose these into tool-execution-signaled and agent-output-signaled forms of agent adaptation, as well as agent-agnostic and agent-supervised forms of tool adaptation. We demonstrate that this framework helps clarify the design space of adaptation strategies in agentic AI, makes their trade-offs explicit, and provides practical guidance for selecting or switching among strategies during system design. We then review the representative approaches in each category, analyze their strengths and limitations, and highlight key open challenges and future opportunities. Overall, this paper aims to offer a conceptual foundation and practical roadmap for researchers and practitioners seeking to build more capable, efficient, and reliable agentic AI systems.

7. **TabReX : Tabular Referenceless eXplainable Evaluation** - 👍 0
   - 기관: ·4 authors
   - [HF 페이지](https://huggingface.co/papers/2512.15907)
   - [논문 링크](https://arxiv.org/abs/2512.15907)
   - Abstract: Evaluating the quality of tables generated by large language models (LLMs) remains an open challenge: existing metrics either flatten tables into text, ignoring structure, or rely on fixed references that limit generalization. We present TabReX, a reference-less, property-driven framework for evaluating tabular generation via graph-based reasoning. TabReX converts both source text and generated tables into canonical knowledge graphs, aligns them through an LLM-guided matching process, and computes interpretable, rubric-aware scores that quantify structural and factual fidelity. The resulting metric provides controllable trade-offs between sensitivity and specificity, yielding human-aligned judgments and cell-level error traces. To systematically asses metric robustness, we introduce TabReX-Bench, a large-scale benchmark spanning six domains and twelve planner-driven perturbation types across three difficulty tiers. Empirical results show that TabReX achieves the highest correlation with expert rankings, remains stable under harder perturbations, and enables fine-grained model-vs-prompt analysis establishing a new paradigm for trustworthy, explainable evaluation of structured generation systems.

