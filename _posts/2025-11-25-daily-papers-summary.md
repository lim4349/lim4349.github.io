---
title: Hugging Face Daily Papers - 2025-11-25
date: 2025-11-25 09:15:00 +0900
categories: ['Daily Papers', '일간']
tags: ['huggingface', 'papers', 'daily', 'ai']
author: lim4349
---

# Hugging Face Daily Papers - 2025-11-25

총 **3개**의 논문이 수집되었습니다.

## 📊 좋아요 순위

1. **Computer-Use Agents as Judges for Generative User Interface** - 👍 12
   - 기관: Show Lab
   - [HF 페이지](https://huggingface.co/papers/2511.15567)
   - [논문 링크](https://arxiv.org/abs/2511.15567)
   - Abstract: Computer-Use Agents (CUA) are becoming increasingly capable of autonomously operating digital environments through Graphical User Interfaces (GUI). Yet, most GUI remain designed primarily for humans--prioritizing aesthetics and usability--forcing agents to adopt human-oriented behaviors that are unnecessary for efficient task execution. At the same time, rapid advances in coding-oriented language models (Coder) have transformed automatic GUI design. This raises a fundamental question: Can CUA as judges to assist Coder for automatic GUI design? To investigate, we introduce AUI-Gym, a benchmark for Automatic GUI development spanning 52 applications across diverse domains. Using language models, we synthesize 1560 tasks that simulate real-world scenarios. To ensure task reliability, we further develop a verifier that programmatically checks whether each task is executable within its environment. Building on this, we propose a Coder-CUA in Collaboration framework: the Coder acts as Designer, generating and revising websites, while the CUA serves as Judge, evaluating functionality and refining designs. Success is measured not by visual appearance, but by task solvability and CUA navigation success rate. To turn CUA feedback into usable guidance, we design a CUA Dashboard that compresses multi-step navigation histories into concise visual summaries, offering interpretable guidance for iterative redesign. By positioning agents as both designers and judges, our framework shifts interface design toward agent-native efficiency and reliability. Our work takes a step toward shifting agents from passive use toward active participation in digital environments. Our code and dataset are available at this https URL .

2. **M3-Bench: Multi-Modal, Multi-Hop, Multi-Threaded Tool-Using MLLM Agent Benchmark** - 👍 5
   - 기관: ·9 authors
   - [HF 페이지](https://huggingface.co/papers/2511.17729)
   - [논문 링크](https://arxiv.org/abs/2511.17729)
   - Abstract: We present M^3-Bench, the first benchmark for evaluating multimodal tool use under the Model Context Protocol. The benchmark targets realistic, multi-hop and multi-threaded workflows that require visual grounding and textual reasoning, cross-tool dependencies, and persistence of intermediate resources across steps. We introduce a similarity-driven alignment that serializes each tool call, embeds signatures with a sentence encoder, and performs similarity-bucketed Hungarian matching to obtain auditable one-to-one correspondences. On top of this alignment, we report interpretable metrics that decouple semantic fidelity from workflow consistency. The benchmark spans 28 servers with 231 tools, and provides standardized trajectories curated through an Executor & Judge pipeline with human verification; an auxiliary four large language models (LLMs) judge ensemble reports end-task Task Completion and information grounding. Evaluations of representative state-of-the-art Multimodal LLMs (MLLMs) reveal persistent gaps in multimodal MCP tool use, particularly in argument fidelity and structure consistency, underscoring the need for methods that jointly reason over images, text, and tool graphs. Our Benchmark's anonymous repository is at this https URL

3. **General Agentic Memory Via Deep Research** - 👍 4
   - 기관: Beijing Academy of Artificial Intelligence
   - [HF 페이지](https://huggingface.co/papers/2511.18423)
   - [논문 링크](https://arxiv.org/abs/2511.18423)
   - Abstract: Memory is critical for AI agents, yet the widely-adopted static memory, aiming to create readily available memory in advance, is inevitably subject to severe information loss. To address this limitation, we propose a novel framework called \textbf{general agentic memory (GAM)}. GAM follows the principle of "\textbf{just-in time (JIT) compilation}" where it focuses on creating optimized contexts for its client at runtime while keeping only simple but useful memory during the offline stage. To this end, GAM employs a duo-design with the following components. 1) \textbf{Memorizer}, which highlights key historical information using a lightweight memory, while maintaining complete historical information within a universal page-store. 2) \textbf{Researcher}, which retrieves and integrates useful information from the page-store for its online request guided by the pre-constructed memory. This design allows GAM to effectively leverage the agentic capabilities and test-time scalability of frontier large language models (LLMs), while also facilitating end-to-end performance optimization through reinforcement learning. In our experimental study, we demonstrate that GAM achieves substantial improvement on various memory-grounded task completion scenarios against existing memory systems.

