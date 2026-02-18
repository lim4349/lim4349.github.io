---
title: Hugging Face Daily Papers - 2026-02-18
date: 2026-02-18 09:15:00 +0900
categories: [Daily Papers, 일간]
tags: [huggingface, papers, daily, ai]
author: lim4349
---

# Hugging Face Daily Papers - 2026-02-18

총 **7개**의 논문이 수집되었습니다.

## 📊 좋아요 순위

1. **Does Socialization Emerge in AI Agent Society? A Case Study of Moltbook** - 👍 9
   - 기관: ·3 authors12
   - [HF 페이지](https://huggingface.co/papers/2602.14299)
   - [논문 링크](https://arxiv.org/abs/2602.14299)
   - Abstract: As large language model agents increasingly populate networked environments, a fundamental question arises: do artificial intelligence (AI) agent societies undergo convergence dynamics similar to human social systems? Lately, Moltbook approximates a plausible future scenario in which autonomous agents participate in an open-ended, continuously evolving online society. We present the first large-scale systemic diagnosis of this AI agent society. Beyond static observation, we introduce a quantitative diagnostic framework for dynamic evolution in AI agent societies, measuring semantic stabilization, lexical turnover, individual inertia, influence persistence, and collective consensus. Our analysis reveals a system in dynamic balance in Moltbook: while global semantic averages stabilize rapidly, individual agents retain high diversity and persistent lexical turnover, defying homogenization. However, agents exhibit strong individual inertia and minimal adaptive response to interaction partners, preventing mutual influence and consensus. Consequently, influence remains transient with no persistent supernodes, and the society fails to develop stable collective influence anchors due to the absence of shared social memory. These findings demonstrate that scale and interaction density alone are insufficient to induce socialization, providing actionable design and analysis principles for upcoming next-generation AI agent societies.

2. **GLM-5: from Vibe Coding to Agentic Engineering** - 👍 5
   - 기관: ·186 authors1.05k
   - [HF 페이지](https://huggingface.co/papers/2602.15763)
   - [논문 링크](https://arxiv.org/abs/2602.15763)
   - Abstract: We present GLM-5, a next-generation foundation model designed to transition the paradigm of vibe coding to agentic engineering. Building upon the agentic, reasoning, and coding (ARC) capabilities of its predecessor, GLM-5 adopts DSA to significantly reduce training and inference costs while maintaining long-context fidelity. To advance model alignment and autonomy, we implement a new asynchronous reinforcement learning infrastructure that drastically improves post-training efficiency by decoupling generation from training. Furthermore, we propose novel asynchronous agent RL algorithms that further improve RL quality, enabling the model to learn from complex, long-horizon interactions more effectively. Through these innovations, GLM-5 achieves state-of-the-art performance on major open benchmarks. Most critically, GLM-5 demonstrates unprecedented capability in real-world coding tasks, surpassing previous baselines in handling end-to-end software engineering challenges. Code, models, and more information are available at this https URL .

3. **Visual Persuasion: What Influences Decisions of Vision-Language Models?** - 👍 2
   - 기관: ·4 authors1
   - [HF 페이지](https://huggingface.co/papers/2602.15278)
   - [논문 링크](https://arxiv.org/abs/2602.15278)
   - Abstract: The web is littered with images, once created for human consumption and now increasingly interpreted by agents using vision-language models (VLMs). These agents make visual decisions at scale, deciding what to click, recommend, or buy. Yet, we know little about the structure of their visual preferences. We introduce a framework for studying this by placing VLMs in controlled image-based choice tasks and systematically perturbing their inputs. Our key idea is to treat the agent's decision function as a latent visual utility that can be inferred through revealed preference: choices between systematically edited images. Starting from common images, such as product photos, we propose methods for visual prompt optimization, adapting text optimization methods to iteratively propose and apply visually plausible modifications using an image generation model (such as in composition, lighting, or background). We then evaluate which edits increase selection probability. Through large-scale experiments on frontier VLMs, we demonstrate that optimized edits significantly shift choice probabilities in head-to-head comparisons. We develop an automatic interpretability pipeline to explain these preferences, identifying consistent visual themes that drive selection. We argue that this approach offers a practical and efficient way to surface visual vulnerabilities, safety concerns that might otherwise be discovered implicitly in the wild, supporting more proactive auditing and governance of image-based AI agents.

4. **ResearchGym: Evaluating Language Model Agents on Real-World AI Research** - 👍 2
   - 기관: Yale University2
   - [HF 페이지](https://huggingface.co/papers/2602.15112)
   - [논문 링크](https://arxiv.org/abs/2602.15112)
   - Abstract: We introduce ResearchGym, a benchmark and execution environment for evaluating AI agents on end-to-end research. To instantiate this, we repurpose five oral and spotlight papers from ICML, ICLR, and ACL. From each paper's repository, we preserve the datasets, evaluation harness, and baseline implementations but withhold the paper's proposed method. This results in five containerized task environments comprising 39 sub-tasks in total. Within each environment, agents must propose novel hypotheses, run experiments, and attempt to surpass strong human baselines on the paper's metrics. In a controlled evaluation of an agent powered by GPT-5, we observe a sharp capability--reliability gap. The agent improves over the provided baselines from the repository in just 1 of 15 evaluations (6.7%) by 11.5%, and completes only 26.5% of sub-tasks on average. We identify recurring long-horizon failure modes, including impatience, poor time and resource management, overconfidence in weak hypotheses, difficulty coordinating parallel experiments, and hard limits from context length. Yet in a single run, the agent surpasses the solution of an ICML 2025 Spotlight task, indicating that frontier agents can occasionally reach state-of-the-art performance, but do so unreliably. We additionally evaluate proprietary agent scaffolds including Claude Code (Opus-4.5) and Codex (GPT-5.2) which display a similar gap. ResearchGym provides infrastructure for systematic evaluation and analysis of autonomous agents on closed-loop research.

5. **On Surprising Effectiveness of Masking Updates in Adaptive Optimizers** - 👍 1
   - 기관: Google1
   - [HF 페이지](https://huggingface.co/papers/2602.15322)
   - [논문 링크](https://arxiv.org/abs/2602.15322)
   - Abstract: Training large language models (LLMs) relies almost exclusively on dense adaptive optimizers with increasingly sophisticated preconditioners. We challenge this by showing that randomly masking parameter updates can be highly effective, with a masked variant of RMSProp consistently outperforming recent state-of-the-art optimizers. Our analysis reveals that the random masking induces a curvature-dependent geometric regularization that smooths the optimization trajectory. Motivated by this finding, we introduce Momentum-aligned gradient masking (Magma), which modulates the masked updates using momentum-gradient alignment. Extensive LLM pre-training experiments show that Magma is a simple drop-in replacement for adaptive optimizers with consistent gains and negligible computational overhead. Notably, for the 1B model size, Magma reduces perplexity by over 19\% and 9\% compared to Adam and Muon, respectively.

6. **Geometry-Aware Rotary Position Embedding for Consistent Video World Model** - 👍 1
   - 기관: Tsinghua University1
   - [HF 페이지](https://huggingface.co/papers/2602.07854)
   - [논문 링크](https://arxiv.org/abs/2602.07854)
   - Abstract: Predictive world models that simulate future observations under explicit camera control are fundamental to interactive AI. Despite rapid advances, current systems lack spatial persistence: they fail to maintain stable scene structures over long trajectories, frequently hallucinating details when cameras revisit previously observed locations. We identify that this geometric drift stems from reliance on screen-space positional embeddings, which conflict with the projective geometry required for 3D consistency. We introduce \textbf{ViewRope}, a geometry-aware encoding that injects camera-ray directions directly into video transformer self-attention layers. By parameterizing attention with relative ray geometry rather than pixel locality, ViewRope provides a model-native inductive bias for retrieving 3D-consistent content across temporal gaps. We further propose \textbf{Geometry-Aware Frame-Sparse Attention}, which exploits these geometric cues to selectively attend to relevant historical frames, improving efficiency without sacrificing memory consistency. We also present \textbf{ViewBench}, a diagnostic suite measuring loop-closure fidelity and geometric drift. Our results demonstrate that ViewRope substantially improves long-term consistency while reducing computational costs.

7. **STAPO: Stabilizing Reinforcement Learning for LLMs by Silencing Rare Spurious Tokens** - 👍 0
   - 기관: ·13 authors1
   - [HF 페이지](https://huggingface.co/papers/2602.15620)
   - [논문 링크](https://arxiv.org/abs/2602.15620)
   - Abstract: Reinforcement Learning (RL) has significantly improved large language model reasoning, but existing RL fine-tuning methods rely heavily on heuristic techniques such as entropy regularization and reweighting to maintain stability. In practice, they often experience late-stage performance collapse, leading to degraded reasoning quality and unstable training. We derive that the magnitude of token-wise policy gradients in RL is negatively correlated with token probability and local policy entropy. Building on this result, we prove that training instability is driven by a tiny fraction of tokens, approximately 0.01\%, which we term \emph{spurious tokens}. When such tokens appear in correct responses, they contribute little to the reasoning outcome but inherit the full sequence-level reward, leading to abnormally amplified gradient updates. Motivated by this observation, we propose Spurious-Token-Aware Policy Optimization (STAPO) for large-scale model refining, which selectively masks such updates and renormalizes the loss over valid tokens. Across six mathematical reasoning benchmarks using Qwen 1.7B, 8B, and 14B base models, STAPO consistently demonstrates superior entropy stability and achieves an average performance improvement of 7.13\% over GRPO, 20-Entropy and JustRL.

