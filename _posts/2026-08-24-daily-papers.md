---
title: Hugging Face Daily Papers - 2026-08-24
permalink: /posts/daily-papers-2026-08-24/
date: 2026-08-24 09:15:00 +0900
categories: [Daily Papers, 일간]
tags: [huggingface, papers, daily, ai]
author: lim4349
---

# Hugging Face Daily Papers - 2026-08-24

총 **5개**의 논문이 수집되었습니다.

## 📊 좋아요 순위

1. **Beyond Correctness: Benchmarking and Aligning Response Behaviors in Hybrid-Thinking MLLMs** - 👍 2
   - 기관: Tencent1
   - [HF 페이지](https://huggingface.co/papers/2608.12781)
   - [논문 링크](https://arxiv.org/abs/2608.12781)
   - Abstract: Hybrid-thinking multimodal large language models (MLLMs) allow a single model to alternate between deliberative thinking and latency-efficient non-thinking inference. Although these modes differ in reasoning budget, their delivered responses should satisfy the same user-facing standard. Correctness alone may not characterize this response quality; we therefore evaluate task accuracy and response-pattern failures as complementary outcomes. We study this gap through \textbf{response-pattern alignment}: whether thinking and non-thinking interfaces preserve acceptable final-response behavior. We introduce \textbf{PatternEval}, a failure-enriched diagnostic benchmark comprising 2,415 multimodal prompts spanning visual perception and grounding, structured image understanding, and multimodal knowledge reasoning. PatternEval tests four recurrent failures: chain-of-thought leakage, response repetition, logical contradiction, and performative reasoning. Response-pattern failures are widespread across models from different providers, with non-thinking inference exhibiting substantially higher failure rates and thereby creating systematic misalignment between thinking and non-thinking interfaces. Motivated by this diagnosis, we develop \textbf{PatternRM}, a response-level reward model, and \textbf{PatternRL}, which introduces pattern-specific penalties during reinforcement learning. Experiments on Qwen3-VL-4B and Qwen3-VL-8B show that incorporating pattern-specific penalties into reinforcement learning can mitigate cross-mode misalignment while incurring a marginal task performance trade-off. Together, PatternEval and PatternRL provide an evaluation-and-training framework for aligning user-visible response patterns across hybrid-thinking interfaces.

2. **Graph Engineering in the Era of LLM Agents: From Individual Intelligence to System Intelligence** - 👍 1
   - 기관: ·35 authors1
   - [HF 페이지](https://huggingface.co/papers/2608.21156)
   - [논문 링크](https://arxiv.org/abs/2608.21156)
   - Abstract: LLMs have evolved from language generators to autonomous agents capable of complex, long-horizon tasks. This evolution has produced paradigms including Prompt Engineering to elicit model capabilities, Context Engineering to manage information access, Harness Engineering to organize external tools and resources, and Loop Engineering to support continual reflection and self-improvement. Yet as tasks grow more complex, individual intelligence faces a fundamental limit: many tasks require heterogeneous expertise, interdependent subtasks, parallel execution, independent verification, and persistent state, exceeding any single agent's organizational capacity. Augmenting one agent's capabilities or context cannot resolve this architectural mismatch; intelligence must instead be distributed across specialized agents and organized at the system level. We call this System Intelligence: an agent system's ability to organize and coordinate multiple intelligent components into a coherent, adaptive whole pursuing a shared objective. Achieving it requires more than adding agents; it demands explicit structures to organize work, coordinate heterogeneous agents, and maintain evolving execution states. We introduce Graph Engineering, an emerging paradigm for next-generation agent systems. Unlike prior paradigms that mainly optimize individual interactions or agent-level behavior, Graph Engineering constructs explicit, dynamic, evolving graph structures representing tasks, agents, and system states. These abstractions provide a unified foundation for organizing complex objectives, orchestrating heterogeneous agents, modeling system dynamics, and enabling scalable agent evolution. We systematically review the principles, methodologies, and applications of Graph Engineering for LLM agents. Related papers, open-source data, and projects are collected at this https URL .

3. **CLEAR: Continuous Latent Adapter Routing for Utility-Preserving LLM Safety Alignment** - 👍 1
   - 기관: University of Illinois at Urbana-Champaign1
   - [HF 페이지](https://huggingface.co/papers/2608.21278)
   - [논문 링크](https://arxiv.org/abs/2608.21278)
   - Abstract: Improving the safety of large language models (LLMs) often comes at the expense of utility, as globally applied safety tuning may affect model responses to both harmful and benign inputs. We propose \textbf{C}ontinuous \textbf{L}at\textbf{E}nt \textbf{A}dapter \textbf{R}outing (CLEAR), a conditional safety adaptation framework that uses a lightweight hidden-state gate to continuously control the activation strength of a safety low-rank adapter. CLEAR aims to reduce harmful completions while avoiding unnecessary changes to the frozen backbone that could degrade performance on benign prompts. Experiments on widely used safety and utility benchmarks show that CLEAR improves robustness on HarmBench while reducing the utility degradation observed with globally applied safety tuning such as SFT or standard low-rank adaptation (LoRA). On Llama-3-8B-Instruct, CLEAR reduces HarmBench ASR from 32.3\% to 0.5\%, while retaining most of the base model's utility and achieving up to 7.1 percentage points higher GSM8K accuracy than globally applied SFT or LoRA. These results suggest that CLEAR is a promising mechanism for improving the safety--utility trade-off in LLM alignment.

4. **InfinityEdit: Infinite Video Editing with a Lightweight Edit-Ignition Adapter** - 👍 1
   - 기관: ·12 authors1
   - [HF 페이지](https://huggingface.co/papers/2608.20910)
   - [논문 링크](https://arxiv.org/abs/2608.20910)
   - Abstract: With large pretrained models, existing methods have effectively improved instruction-based video editing. However, most of them rely on an in-place editing assumption. They align the edited video with the given source clip frame by frame over a fixed time span. This pattern fails for open-ended streams, e.g., restyling a live game or applying a camera move to an ongoing shot. In such cases, edits must extend to future frames as they arrive, rather than be applied to a static input clip. In this paper, we study this setting and name it infinite video editing: given a preceding segment and an edit request, a model must generate the next segment that continues the stream while applying the requested edit. This process repeats as an unbounded sequence of edit instructions arrives. This task brings two challenges: the edit must be a faithful continuation rather than a frame-wise rewrite, and generation quality must remain stable as edits accumulate. To address them, we first design a data-collection pipeline for infinite video editing. Based on the collected data, we propose InfinityEdit, a lightweight edit adapter that equips a streaming video generator with unbounded editing ability. The adapter contains three attention modules. History cross-attention guides the denoising frames using the input frames. Temporal causal self-attention keeps temporal cues flowing only from earlier frames to later ones. Edit cross-attention injects the edit request into generation. During inference, the adapter is activated only in the chunk where an edit request arrives. Subsequent chunks are generated by the original model with a reset anchor frame. This scheme applies the edit while preserving the original model's infinite generation ability. Extensive experiments show that InfinityEdit faithfully continues the stream under each edit, and stays stable over unbounded edit sequences.

5. **Llama-Mobile: Efficient 2.7-Bit Quantization of VLMs** - 👍 1
   - 기관: ·3 authors
   - [HF 페이지](https://huggingface.co/papers/2608.21134)
   - [논문 링크](https://arxiv.org/abs/2608.21134)
   - Abstract: Deploying vision-language models (VLMs) on mobile devices is challenging due to their significant memory and compute requirements. We present a framework for quantizing VLMs for efficient inference on resource-constrained hardware. Our approach combines a quantization pipeline that uses the model itself to generate training data and does not require access to the training setup, with a novel 2.7-bit-per-parameter format supporting efficient execution on Arm CPUs. We validate our approach by compressing the Llama 3.2 11B Vision Instruct model to 3.7 GB with 8-bit activations, preserving strong performance on a set of standard visual question answering tasks.

