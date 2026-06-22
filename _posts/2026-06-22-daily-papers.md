---
title: Hugging Face Daily Papers - 2026-06-22
permalink: /posts/daily-papers-2026-06-22/
date: 2026-06-22 09:15:00 +0900
categories: [Daily Papers, 일간]
tags: [huggingface, papers, daily, ai]
author: lim4349
---

# Hugging Face Daily Papers - 2026-06-22

총 **5개**의 논문이 수집되었습니다.

## 📊 좋아요 순위

1. **PerceptionDLM: Parallel Region Perception with Multimodal Diffusion Language Models** - 👍 38
   - 기관: ByteDance114
   - [HF 페이지](https://huggingface.co/papers/2606.19534)
   - [논문 링크](https://arxiv.org/abs/2606.19534)
   - Abstract: Multimodal large language models (MLLMs) have achieved remarkable progress in visual understanding tasks. However, most existing MLLMs rely on autoregressive generation, which limits their efficiency for perception tasks that require captioning multiple regions. In this work, we propose PerceptionDLM, a multimodal diffusion language model optimized for efficient parallel region perception. Built upon PerceptionDLM-Base, a strong foundational baseline that achieves state-of-the-art performance among open-source diffusion MLLMs, our architecture fully leverages the parallel decoding nature of DLMs. Specifically, we introduce efficient prompting and structured attention masking to enable simultaneous perception of multiple masked regions, allowing the model to generate region descriptions in parallel at both the sequence and token levels. This design significantly improves inference efficiency compared with existing approaches that process regions sequentially. To systematically evaluate the parallelism property of visual perception capability for DLMs, we construct a new Parallel Detailed Localized Captioning Benchmark (ParaDLC-Bench) by scaling the DLC-Bench to include multiple region masks per image, enabling joint evaluation of both caption quality and inference efficiency. Experiments demonstrate that PerceptionDLM maintains competitive performance in region captioning while achieving substantial speed improvements for multi-region perception tasks. Our results highlight the potential of multimodal diffusion language models for efficient, parallel visual perception. To the best of our knowledge, we are the first to achieve parallel region caption and perception by leveraging the advantages of diffusion language models. Code, models, and datasets are released.

2. **BrainG3N: A Dual-Purpose Tokenizer for Controllable 3D Brain MRI Generation** - 👍 4
   - 기관: Gevaert Lab1
   - [HF 페이지](https://huggingface.co/papers/2606.19651)
   - [논문 링크](https://arxiv.org/abs/2606.19651)
   - Abstract: Three-dimensional (3D) brain MRI is central to clinical neurology and neuro-oncology, where generative models could augment under-represented cohorts, simulate disease trajectories, and support privacy-preserving data sharing. Latent diffusion has been the go-to solution for modeling imaging data, but it places two competing demands on the tokenizer: encoder embeddings must retain the clinical information that downstream tasks act on, and the decoder must reconstruct anatomically faithful volumes. Existing reconstruction-driven tokenizers achieve the second at the expense of the first. To address this, we introduce a fully volumetric masked-autoencoder (MAE) based tokenizer for 3D brain MRI latent diffusion, decoupling encoder and decoder: a frozen 3D MAE encoder produces clinically informative embeddings, while a dedicated CNN decoder reconstructs voxels from a linear projection of those embeddings. We pretrain the encoder on 35,309 volumes from 18 public cohorts spanning four modalities, ten disease categories, and 200+ acquisition sites, and demonstrate its dual utility in two settings. First, on a 23-task linear-probing benchmark, the encoder outperforms or matches SOTA models (i.e., BrainIAC, BrainSegFounder, and MedicalNet) on 21 of 23 tasks. Second, a conditional diffusion transformer (DiT) trained on these clinically informative embeddings supports both conditional generation across six variables and patient-specific longitudinal forecasting. Together these results establish a single 3D brain-MRI embedding space capable of both downstream clinical tasks and controllable generation.

3. **GateMem: Benchmarking Memory Governance in Multi-Principal Shared-Memory Agents** - 👍 4
   - 기관: ·10 authors631
   - [HF 페이지](https://huggingface.co/papers/2606.18829)
   - [논문 링크](https://arxiv.org/abs/2606.18829)
   - Abstract: Memory benchmarks for LLM agents largely assume single-user settings, leaving shared assistants for hospitals, workplaces, campuses, and households understudied. In these deployments, multiple principals write to a common memory pool and query it under different roles, scopes, and relationships, so memory quality requires governance as well as recall. We introduce GateMem, a benchmark for multi-principal shared-memory agents. GateMem jointly evaluates utility for legitimate long-horizon requests with state updates, access control across contextual authorization boundaries, and agent-facing active forgetting after explicit deletion requests. It spans medical, office, education, and household domains, with long-form multi-party episodes, incremental memory injection, hidden checkpoints, structured judging, and leak-target annotations. Across diverse baselines and backbone models, no method simultaneously achieves strong utility, robust access control, and reliable forgetting. Long-context prompting often yields the best governance score at high token cost, while retrieval-based and external-memory methods reduce cost yet still leak unauthorized or deleted information. These results show current memory agents remain far from reliable shared institutional deployment.

4. **WorldLines: Benchmarking and Modeling Long-Horizon Stateful Embodied Agents** - 👍 2
   - 기관: ·10 authors1
   - [HF 페이지](https://huggingface.co/papers/2606.18847)
   - [논문 링크](https://arxiv.org/abs/2606.18847)
   - Abstract: To assist humans over extended periods in real homes, embodied agents must remember user routines, world states, and past interactions. Existing long-term memory benchmarks mainly evaluate language-centric retrieval and question answering, while embodied benchmarks often focus on short-horizon task execution without testing long-term memory use in dynamic environments. We introduce WorldLines, a project-driven benchmark for long-horizon embodied household assistance. It constructs temporally extended household traces with dialogues, actions, execution feedback, object and device state changes, and converts them into evidence-linked samples for Memory QA and Embodied Task Planning. We further propose ObsMem, an observer-grounded memory framework that maintains visibility-aware memories and action-native state trails for state-aware decisions. Experiments reveal persistent challenges in partial observability, overwritten world states, and translating long-term memory into embodied plans, while ObsMem offers a stronger reference architecture for this setting.

5. **Distilling Examples into Task Instructions: Enhanced In-Context Learning for Real-World B2B Conversations** - 👍 1
   - 기관: ·4 authors01
   - [HF 페이지](https://huggingface.co/papers/2606.15641)
   - [논문 링크](https://arxiv.org/abs/2606.15641)
   - Abstract: In-context learning (ICL) is the standard method for low-resource classification, yet its efficacy in specialized domains remains largely unexplored. We address the challenge of classifying semantically complex, multi-party B2B conversations, where traditional ICL encounters significant limitations, especially as context length increases due to the concatenation of multiple few-shot examples. We introduce the \texttt{Call Playbook} dataset, featuring five classification tasks derived from real-world B2B conversations targeting core sales concepts. To bridge the gap between performance and practical utility, we propose novel knowledge extraction methods that distill verbose examples into compact, interpretable representations of structured classification criteria and precise task descriptions. Our approach achieves a 99\% reduction in token usage and improves macro-averaged AUC by up to 7\% over traditional ICL. Notably, it remains robust as context grows, unlike advanced token compression baselines which degrade by over 9 F1 points. Importantly, our framework enables direct refinement of classification logic, addressing critical needs for transparency, efficiency, and user interaction in real-world NLP applications.

