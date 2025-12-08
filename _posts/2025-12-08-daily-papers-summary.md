---
title: Hugging Face Daily Papers - 2025-12-08
date: 2025-12-08 09:15:00 +0900
categories: ['Daily Papers', '일간']
tags: ['huggingface', 'papers', 'daily', 'ai']
author: lim4349
---

# Hugging Face Daily Papers - 2025-12-08

총 **7개**의 논문이 수집되었습니다.

## 📊 좋아요 순위

1. **EditThinker: Unlocking Iterative Reasoning for Any Image Editor** - 👍 7
   - 기관: ·14 authors
   - [HF 페이지](https://huggingface.co/papers/2512.05965)
   - [논문 링크](https://arxiv.org/abs/2512.05965)
   - Abstract: Instruction-based image editing has emerged as a prominent research area, which, benefiting from image generation foundation models, have achieved high aesthetic quality, making instruction-following capability the primary challenge. Existing approaches improve instruction adherence via supervised or reinforcement learning, yet single-turn success rates remain limited due to inherent stochasticity and a lack of deliberation. In this work, we propose a deliberative editing framework to 'think' while they edit, which simulates the human cognitive loop by iteratively executing a Think-while-Edit cycle: Critiquing results and Refining instructions , followed by Repeating the generation until satisfactory. Specifically, we train a single MLLM, EditThinker, to act as the reasoning engine of this framework, which jointly produce the critique score, reasoning process, and refined instructions. We employ reinforcement learning to align the EditThinker's thinking with its editing, thereby generating more targeted instruction improvements. Extensive experiments on four benchmarks demonstrate that our approach significantly improves the instruction-following capability of any image editing model by a large margin. We will release our data construction framework, datasets, and models to benefit the community.

2. **ReVSeg: Incentivizing the Reasoning Chain for Video Segmentation with Reinforcement Learning** - 👍 4
   - 기관: ·7 authors
   - [HF 페이지](https://huggingface.co/papers/2512.02835)
   - [논문 링크](https://arxiv.org/abs/2512.02835)
   - Abstract: Reasoning-centric video object segmentation is an inherently complex task: the query often refers to dynamics, causality, and temporal interactions, rather than static appearances. Yet existing solutions generally collapse these factors into simplified reasoning with latent embeddings, rendering the reasoning chain opaque and essentially intractable. We therefore adopt an explicit decomposition perspective and introduce ReVSeg, which executes reasoning as sequential decisions in the native interface of pretrained vision language models (VLMs). Rather than folding all reasoning into a single-step prediction, ReVSeg executes three explicit operations -- semantics interpretation, temporal evidence selection, and spatial grounding -- aligning pretrained capabilities. We further employ reinforcement learning to optimize the multi-step reasoning chain, enabling the model to self-refine its decision quality from outcome-driven signals. Experimental results demonstrate that ReVSeg attains state-of-the-art performances on standard video object segmentation benchmarks and yields interpretable reasoning trajectories. Project page is available at this https URL .

3. **Joint 3D Geometry Reconstruction and Motion Generation for 4D Synthesis from a Single Image** - 👍 2
   - 기관: ·6 authors
   - [HF 페이지](https://huggingface.co/papers/2512.05044)
   - [논문 링크](https://arxiv.org/abs/2512.05044)
   - Abstract: Generating interactive and dynamic 4D scenes from a single static image remains a core challenge. Most existing generate-then-reconstruct and reconstruct-then-generate methods decouple geometry from motion, causing spatiotemporal inconsistencies and poor generalization. To address these, we extend the reconstruct-then-generate framework to jointly perform Motion generation and geometric Reconstruction for 4D Synthesis (MoRe4D). We first introduce TrajScene-60K, a large-scale dataset of 60,000 video samples with dense point trajectories, addressing the scarcity of high-quality 4D scene data. Based on this, we propose a diffusion-based 4D Scene Trajectory Generator (4D-STraG) to jointly generate geometrically consistent and motion-plausible 4D point trajectories. To leverage single-view priors, we design a depth-guided motion normalization strategy and a motion-aware module for effective geometry and dynamics integration. We then propose a 4D View Synthesis Module (4D-ViSM) to render videos with arbitrary camera trajectories from 4D point track representations. Experiments show that MoRe4D generates high-quality 4D scenes with multi-view consistency and rich dynamic details from a single image. Code: this https URL .

4. **ProPhy: Progressive Physical Alignment for Dynamic World Simulation** - 👍 1
   - 기관: ·10 authors
   - [HF 페이지](https://huggingface.co/papers/2512.05564)
   - [논문 링크](https://arxiv.org/abs/2512.05564)
   - Abstract: Recent advances in video generation have shown remarkable potential for constructing world simulators. However, current models still struggle to produce physically consistent results, particularly when handling large-scale or complex dynamics. This limitation arises primarily because existing approaches respond isotropically to physical prompts and neglect the fine-grained alignment between generated content and localized physical cues. To address these challenges, we propose ProPhy, a Progressive Physical Alignment Framework that enables explicit physics-aware conditioning and anisotropic generation. ProPhy employs a two-stage Mixture-of-Physics-Experts (MoPE) mechanism for discriminative physical prior extraction, where Semantic Experts infer semantic-level physical principles from textual descriptions, and Refinement Experts capture token-level physical dynamics. This mechanism allows the model to learn fine-grained, physics-aware video representations that better reflect underlying physical laws. Furthermore, we introduce a physical alignment strategy that transfers the physical reasoning capabilities of vision-language models (VLMs) into the Refinement Experts, facilitating a more accurate representation of dynamic physical phenomena. Extensive experiments on physics-aware video generation benchmarks demonstrate that ProPhy produces more realistic, dynamic, and physically coherent results than existing state-of-the-art methods.

5. **World Models That Know When They Don't Know: Controllable Video Generation with Calibrated Uncertainty** - 👍 0
   - 기관: ·5 authors
   - [HF 페이지](https://huggingface.co/papers/2512.05927)
   - [논문 링크](https://arxiv.org/abs/2512.05927)
   - Abstract: Recent advances in generative video models have led to significant breakthroughs in high-fidelity video synthesis, specifically in controllable video generation where the generated video is conditioned on text and action inputs, e.g., in instruction-guided video editing and world modeling in robotics. Despite these exceptional capabilities, controllable video models often hallucinate - generating future video frames that are misaligned with physical reality - which raises serious concerns in many tasks such as robot policy evaluation and planning. However, state-of-the-art video models lack the ability to assess and express their confidence, impeding hallucination mitigation. To rigorously address this challenge, we propose C3, an uncertainty quantification (UQ) method for training continuous-scale calibrated controllable video models for dense confidence estimation at the subpatch level, precisely localizing the uncertainty in each generated video frame. Our UQ method introduces three core innovations to empower video models to estimate their uncertainty. First, our method develops a novel framework that trains video models for correctness and calibration via strictly proper scoring rules. Second, we estimate the video model's uncertainty in latent space, avoiding training instability and prohibitive training costs associated with pixel-space approaches. Third, we map the dense latent-space uncertainty to interpretable pixel-level uncertainty in the RGB space for intuitive visualization, providing high-resolution uncertainty heatmaps that identify untrustworthy regions. Through extensive experiments on large-scale robot learning datasets (Bridge and DROID) and real-world evaluations, we demonstrate that our method not only provides calibrated uncertainty estimates within the training distribution, but also enables effective out-of-distribution detection.

6. **AI & Human Co-Improvement for Safer Co-Superintelligence** - 👍 0
   - 기관: Meta Research
   - [HF 페이지](https://huggingface.co/papers/2512.05356)
   - [논문 링크](https://arxiv.org/abs/2512.05356)
   - Abstract: Self-improvement is a goal currently exciting the field of AI, but is fraught with danger, and may take time to fully achieve. We advocate that a more achievable and better goal for humanity is to maximize co-improvement: collaboration between human researchers and AIs to achieve co-superintelligence. That is, specifically targeting improving AI systems' ability to work with human researchers to conduct AI research together, from ideation to experimentation, in order to both accelerate AI research and to generally endow both AIs and humans with safer superintelligence through their symbiosis. Focusing on including human research improvement in the loop will both get us there faster, and more safely.

7. **Self-Improving VLM Judges Without Human Annotations** - 👍 0
   - 기관: AI at Meta
   - [HF 페이지](https://huggingface.co/papers/2512.05145)
   - [논문 링크](https://arxiv.org/abs/2512.05145)
   - Abstract: Effective judges of Vision-Language Models (VLMs) are crucial for model development. Current methods for training VLM judges mainly rely on large-scale human preference annotations. However, such an approach is costly, and the annotations easily become obsolete as models rapidly improve. In this work, we present a framework to self-train a VLM judge model without any human preference annotations, using only self-synthesized data. Our method is iterative and has three stages: (1) generate diverse multimodal instruction-response pairs at varying quality levels, (2) generate reasoning traces and judgments for each pair, removing the ones that do not match our expected quality levels, and (3) training on correct judge answers and their reasoning traces. We evaluate the resulting judge on Multimodal RewardBench and VL-RewardBench across domains: correctness, preference, reasoning, safety, and visual question-answering. Our method improves a Llama-3.2-11B multimodal judge from 0.38 to 0.51 in overall accuracy on VL-RewardBench, often outperforming much larger models including Llama-3.2-90B, GPT-4o, and Claude 3.5 Sonnet, with particularly strong gains in general, hallucination, and reasoning dimensions. The overall strength of these human-annotation-free results suggest the potential for a future self-judge that evolves alongside rapidly improving VLM capabilities.

