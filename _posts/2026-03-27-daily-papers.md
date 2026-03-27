---
title: Hugging Face Daily Papers - 2026-03-27
date: 2026-03-27 09:15:00 +0900
categories: [Daily Papers, 일간]
tags: [huggingface, papers, daily, ai]
author: lim4349
---

# Hugging Face Daily Papers - 2026-03-27

총 **10개**의 논문이 수집되었습니다.

## 📊 좋아요 순위

1. **PixelSmile: Toward Fine-Grained Facial Expression Editing** - 👍 91
   - 기관: Fudan University151
   - [HF 페이지](https://huggingface.co/papers/2603.25728)
   - [논문 링크](https://arxiv.org/abs/2603.25728)
   - Abstract: Fine-grained facial expression editing has long been limited by intrinsic semantic overlap. To address this, we construct the Flex Facial Expression (FFE) dataset with continuous affective annotations and establish FFE-Bench to evaluate structural confusion, editing accuracy, linear controllability, and the trade-off between expression editing and identity preservation. We propose PixelSmile, a diffusion framework that disentangles expression semantics via fully symmetric joint training. PixelSmile combines intensity supervision with contrastive learning to produce stronger and more distinguishable expressions, achieving precise and stable linear expression control through textual latent interpolation. Extensive experiments demonstrate that PixelSmile achieves superior disentanglement and robust identity preservation, confirming its effectiveness for continuous, controllable, and fine-grained expression editing, while naturally supporting smooth expression blending.

2. **Intern-S1-Pro: Scientific Multimodal Foundation Model at Trillion Scale** - 👍 76
   - 기관: Intern Large Models5
   - [HF 페이지](https://huggingface.co/papers/2603.25040)
   - [논문 링크](https://arxiv.org/abs/2603.25040)
   - Abstract: We introduce Intern-S1-Pro, the first one-trillion-parameter scientific multimodal foundation model. Scaling to this unprecedented size, the model delivers a comprehensive enhancement across both general and scientific domains. Beyond stronger reasoning and image-text understanding capabilities, its intelligence is augmented with advanced agent capabilities. Simultaneously, its scientific expertise has been vastly expanded to master over 100 specialized tasks across critical science fields, including chemistry, materials, life sciences, and earth sciences. Achieving this massive scale is made possible by the robust infrastructure support of XTuner and LMDeploy, which facilitates highly efficient Reinforcement Learning (RL) training at the 1-trillion parameter level while ensuring strict precision consistency between training and inference. By seamlessly integrating these advancements, Intern-S1-Pro further fortifies the fusion of general and specialized intelligence, working as a Specializable Generalist, demonstrating its position in the top tier of open-source models for general capabilities, while outperforming proprietary models in the depth of specialized scientific tasks.

3. **RealRestorer: Towards Generalizable Real-World Image Restoration with Large-Scale Image Editing Models** - 👍 34
   - 기관: Southern university of science and technology121
   - [HF 페이지](https://huggingface.co/papers/2603.25502)
   - [논문 링크](https://arxiv.org/abs/2603.25502)
   - Abstract: Image restoration under real-world degradations is critical for downstream tasks such as autonomous driving and object detection. However, existing restoration models are often limited by the scale and distribution of their training data, resulting in poor generalization to real-world scenarios. Recently, large-scale image editing models have shown strong generalization ability in restoration tasks, especially for closed-source models like Nano Banana Pro, which can restore images while preserving consistency. Nevertheless, achieving such performance with those large universal models requires substantial data and computational costs. To address this issue, we construct a large-scale dataset covering nine common real-world degradation types and train a state-of-the-art open-source model to narrow the gap with closed-source alternatives. Furthermore, we introduce RealIR-Bench, which contains 464 real-world degraded images and tailored evaluation metrics focusing on degradation removal and consistency preservation. Extensive experiments demonstrate our model ranks first among open-source methods, achieving state-of-the-art performance.

4. **Calibri: Enhancing Diffusion Transformers via Parameter-Efficient Calibration** - 👍 25
   - 기관: Visual Generative AI group11
   - [HF 페이지](https://huggingface.co/papers/2603.24800)
   - [논문 링크](https://arxiv.org/abs/2603.24800)
   - Abstract: In this paper, we uncover the hidden potential of Diffusion Transformers (DiTs) to significantly enhance generative tasks. Through an in-depth analysis of the denoising process, we demonstrate that introducing a single learned scaling parameter can significantly improve the performance of DiT blocks. Building on this insight, we propose Calibri, a parameter-efficient approach that optimally calibrates DiT components to elevate generative quality. Calibri frames DiT calibration as a black-box reward optimization problem, which is efficiently solved using an evolutionary algorithm and modifies just ~100 parameters. Experimental results reveal that despite its lightweight design, Calibri consistently improves performance across various text-to-image models. Notably, Calibri also reduces the inference steps required for image generation, all while maintaining high-quality outputs.

5. **MACRO: Advancing Multi-Reference Image Generation with Structured Long-Context Data** - 👍 24
   - 기관: The University of Hong Kong291
   - [HF 페이지](https://huggingface.co/papers/2603.25319)
   - [논문 링크](https://arxiv.org/abs/2603.25319)
   - Abstract: Generating images conditioned on multiple visual references is critical for real-world applications such as multi-subject composition, narrative illustration, and novel view synthesis, yet current models suffer from severe performance degradation as the number of input references grows. We identify the root cause as a fundamental data bottleneck: existing datasets are dominated by single- or few-reference pairs and lack the structured, long-context supervision needed to learn dense inter-reference dependencies. To address this, we introduce MacroData, a large-scale dataset of 400K samples, each containing up to 10 reference images, systematically organized across four complementary dimensions -- Customization, Illustration, Spatial reasoning, and Temporal dynamics -- to provide comprehensive coverage of the multi-reference generation space. Recognizing the concurrent absence of standardized evaluation protocols, we further propose MacroBench, a benchmark of 4,000 samples that assesses generative coherence across graded task dimensions and input scales. Extensive experiments show that fine-tuning on MacroData yields substantial improvements in multi-reference generation, and ablation studies further reveal synergistic benefits of cross-task co-training and effective strategies for handling long-context complexity. The dataset and benchmark will be publicly released.

6. **Voxtral TTS** - 👍 15
   - 기관: Mistral AI_1
   - [HF 페이지](https://huggingface.co/papers/2603.25551)
   - [논문 링크](https://arxiv.org/abs/2603.25551)
   - Abstract: We introduce Voxtral TTS, an expressive multilingual text-to-speech model that generates natural speech from as little as 3 seconds of reference audio. Voxtral TTS adopts a hybrid architecture that combines auto-regressive generation of semantic speech tokens with flow-matching for acoustic tokens. These tokens are encoded and decoded with Voxtral Codec, a speech tokenizer trained from scratch with a hybrid VQ-FSQ quantization scheme. In human evaluations conducted by native speakers, Voxtral TTS is preferred for multilingual voice cloning due to its naturalness and expressivity, achieving a 68.4\% win rate over ElevenLabs Flash v2.5. We release the model weights under a CC BY-NC license.

7. **SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks** - 👍 14
   - 기관: University of Wisconsin - Madison231
   - [HF 페이지](https://huggingface.co/papers/2603.24755)
   - [논문 링크](https://arxiv.org/abs/2603.24755)
   - Abstract: Software development is iterative, yet agentic coding benchmarks overwhelmingly evaluate single-shot solutions against complete specifications. Code can pass the test suite but become progressively harder to extend. Recent iterative benchmarks attempt to close this gap, but constrain the agent's design decisions too tightly to faithfully measure how code quality shapes future extensions. We introduce SlopCodeBench, a language-agnostic benchmark comprising 20 problems and 93 checkpoints, in which agents repeatedly extend their own prior solutions under evolving specifications that force architectural decisions without prescribing internal structure. We track two trajectory-level quality signals: verbosity, the fraction of redundant or duplicated code, and structural erosion, the share of complexity mass concentrated in high-complexity functions. No agent solves any problem end-to-end across 11 models; the highest checkpoint solve rate is 17.2%. Quality degrades steadily: erosion rises in 80% of trajectories and verbosity in 89.8%. Against 48 open-source Python repositories, agent code is 2.2x more verbose and markedly more eroded. Tracking 20 of those repositories over time shows that human code stays flat, while agent code deteriorates with each iteration. A prompt-intervention study shows that initial quality can be improved, but it does not halt degradation. These results demonstrate that pass-rate benchmarks systematically undermeasure extension robustness, and that current agents lack the design discipline iterative software development demands.

8. **MSA: Memory Sparse Attention for Efficient End-to-End Memory Model Scaling to 100M Tokens** - 👍 12
   - 기관: EverMind-AI2.24k1
   - [HF 페이지](https://huggingface.co/papers/2603.23516)
   - [논문 링크](https://arxiv.org/abs/2603.23516)
   - Abstract: Long-term memory is a cornerstone of human intelligence. Enabling AI to process lifetime-scale information remains a long-standing pursuit in the field. Due to the constraints of full-attention architectures, the effective context length of large language models (LLMs) is typically limited to 1M tokens. Existing approaches, such as hybrid linear attention, fixed-size memory states (e.g., RNNs), and external storage methods like RAG or agent systems, attempt to extend this limit. However, they often suffer from severe precision degradation and rapidly increasing latency as context length grows, an inability to dynamically modify memory content, or a lack of end-to-end optimization. These bottlenecks impede complex scenarios like large-corpus summarization, Digital Twins, and long-history agent reasoning, while limiting memory capacity and slowing inference. We present Memory Sparse Attention (MSA), an end-to-end trainable, efficient, and massively scalable memory model framework. Through core innovations including scalable sparse attention and document-wise RoPE, MSA achieves linear complexity in both training and inference while maintaining exceptional stability, exhibiting less than 9% degradation when scaling from 16K to 100M tokens. Furthermore, KV cache compression, combined with Memory Parallel, enables 100M-token inference on 2xA800 GPUs. We also propose Memory Interleaving to facilitate complex multi-hop reasoning across scattered memory segments. MSA significantly surpasses frontier LLMs, state-of-the-art RAG systems, and leading memory agents in long-context benchmarks. These results demonstrate that by decoupling memory capacity from reasoning, MSA provides a scalable foundation to endow general-purpose models with intrinsic, lifetime-scale memory.

9. **AVControl: Efficient Framework for Training Audio-Visual Controls** - 👍 8
   - 기관: Lightricks1
   - [HF 페이지](https://huggingface.co/papers/2603.24793)
   - [논문 링크](https://arxiv.org/abs/2603.24793)
   - Abstract: Controlling video and audio generation requires diverse modalities, from depth and pose to camera trajectories and audio transformations, yet existing approaches either train a single monolithic model for a fixed set of controls or introduce costly architectural changes for each new modality. We introduce AVControl, a lightweight, extendable framework built on LTX-2, a joint audio-visual foundation model, where each control modality is trained as a separate LoRA on a parallel canvas that provides the reference signal as additional tokens in the attention layers, requiring no architectural changes beyond the LoRA adapters themselves. We show that simply extending image-based in-context methods to video fails for structural control, and that our parallel canvas approach resolves this. On the VACE Benchmark, we outperform all evaluated baselines on depth- and pose-guided generation, inpainting, and outpainting, and show competitive results on camera control and audio-visual benchmarks. Our framework supports a diverse set of independently trained modalities: spatially-aligned controls such as depth, pose, and edges, camera trajectory with intrinsics, sparse motion control, video editing, and, to our knowledge, the first modular audio-visual controls for a joint generation model. Our method is both compute- and data-efficient: each modality requires only a small dataset and converges within a few hundred to a few thousand training steps, a fraction of the budget of monolithic alternatives. We publicly release our code and trained LoRA checkpoints.

10. **Less Gaussians, Texture More: 4K Feed-Forward Textured Splatting** - 👍 4
   - 기관: Apple
   - [HF 페이지](https://huggingface.co/papers/2603.25745)
   - [논문 링크](https://arxiv.org/abs/2603.25745)
   - Abstract: Existing feed-forward 3D Gaussian Splatting methods predict pixel-aligned primitives, leading to a quadratic growth in primitive count as resolution increases. This fundamentally limits their scalability, making high-resolution synthesis such as 4K intractable. We introduce LGTM (Less Gaussians, Texture More), a feed-forward framework that overcomes this resolution scaling barrier. By predicting compact Gaussian primitives coupled with per-primitive textures, LGTM decouples geometric complexity from rendering resolution. This approach enables high-fidelity 4K novel view synthesis without per-scene optimization, a capability previously out of reach for feed-forward methods, all while using significantly fewer Gaussian primitives. Project page: this https URL

