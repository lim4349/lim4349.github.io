---
title: Hugging Face Daily Papers - 2026-02-23
date: 2026-02-23 09:15:00 +0900
categories: [Daily Papers, 일간]
tags: [huggingface, papers, daily, ai]
author: lim4349
---

# Hugging Face Daily Papers - 2026-02-23

총 **10개**의 논문이 수집되었습니다.

## 📊 좋아요 순위

1. **VESPO: Variational Sequence-Level Soft Policy Optimization for Stable Off-Policy LLM Training** - 👍 155
   - 기관: rednote-hilab91
   - [HF 페이지](https://huggingface.co/papers/2602.10693)
   - [논문 링크](https://arxiv.org/abs/2602.10693)
   - Abstract: Training stability remains a central challenge in reinforcement learning (RL) for large language models (LLMs). Policy staleness, asynchronous training, and mismatches between training and inference engines all cause the behavior policy to diverge from the current policy, risking training collapse. Importance sampling provides a principled correction for this distribution shift but suffers from high variance; existing remedies such as token-level clipping and sequence-level normalization lack a unified theoretical foundation. We propose Variational sEquence-level Soft Policy Optimization (VESPO). By incorporating variance reduction into a variational formulation over proposal distributions, VESPO derives a closed-form reshaping kernel that operates directly on sequence-level importance weights without length normalization. Experiments on mathematical reasoning benchmarks show that VESPO maintains stable training under staleness ratios up to 64x and fully asynchronous execution, and delivers consistent gains across both dense and Mixture-of-Experts models. Code is available at this https URL

2. **Does Your Reasoning Model Implicitly Know When to Stop Thinking?** - 👍 82
   - 기관: ByteDance1
   - [HF 페이지](https://huggingface.co/papers/2602.08354)
   - [논문 링크](https://arxiv.org/abs/2602.08354)
   - Abstract: Recent advancements in large reasoning models (LRMs) have greatly improved their capabilities on complex reasoning tasks through Long Chains of Thought (CoTs). However, this approach often results in substantial redundancy, impairing computational efficiency and causing significant delays in real-time applications. Recent studies show that longer reasoning chains are frequently uncorrelated with correctness and can even be detrimental to accuracy. In a further in-depth analysis of this phenomenon, we surprisingly uncover and empirically verify that LRMs implicitly know the appropriate time to stop thinking, while this capability is obscured by current sampling paradigms. Motivated by this, we introduce SAGE (Self-Aware Guided Efficient Reasoning), a novel sampling paradigm that unleashes this efficient reasoning potential. Furthermore, integrating SAGE as mixed sampling into group-based reinforcement learning (SAGE-RL) enables SAGE-RL to effectively incorporate SAGE-discovered efficient reasoning patterns into standard pass@1 inference, markedly enhancing both the reasoning accuracy and efficiency of LRMs across multiple challenging mathematical benchmarks.

3. **Generated Reality: Human-centric World Simulation using Interactive Video Generation with Hand and Camera Control** - 👍 9
   - 기관: ·6 authors2
   - [HF 페이지](https://huggingface.co/papers/2602.18422)
   - [논문 링크](https://arxiv.org/abs/2602.18422)
   - Abstract: Extended reality (XR) demands generative models that respond to users' tracked real-world motion, yet current video world models accept only coarse control signals such as text or keyboard input, limiting their utility for embodied interaction. We introduce a human-centric video world model that is conditioned on both tracked head pose and joint-level hand poses. For this purpose, we evaluate existing diffusion transformer conditioning strategies and propose an effective mechanism for 3D head and hand control, enabling dexterous hand--object interactions. We train a bidirectional video diffusion model teacher using this strategy and distill it into a causal, interactive system that generates egocentric virtual environments. We evaluate this generated reality system with human subjects and demonstrate improved task performance as well as a significantly higher level of perceived amount of control over the performed actions compared with relevant baselines.

4. **Decoding as Optimisation on the Probability Simplex: From Top-K to Top-P (Nucleus) to Best-of-K Samplers** - 👍 6
   - 기관: ·4 authors1
   - [HF 페이지](https://huggingface.co/papers/2602.18292)
   - [논문 링크](https://arxiv.org/abs/2602.18292)
   - Abstract: Decoding sits between a language model and everything we do with it, yet it is still treated as a heuristic knob-tuning exercise. We argue decoding should be understood as a principled optimisation layer: at each token, we solve a regularised problem over the probability simplex that trades off model score against structural preferences and constraints. This single template recovers greedy decoding, Softmax sampling, Top-K, Top-P, and Sparsemax-style sparsity as special cases, and explains their common structure through optimality conditions. More importantly, the framework makes it easy to invent new decoders without folklore. We demonstrate this by designing Best-of-K (BoK), a KL-anchored coverage objective aimed at multi-sample pipelines (self-consistency, reranking, verifier selection). BoK targets the probability of covering good alternatives within a fixed K-sample budget and improves empirical performance. We show that such samples can improve accuracy by, for example, +18.6% for Qwen2.5-Math-7B on MATH500 at high sampling temperatures.

5. **EgoPush: Learning End-to-End Egocentric Multi-Object Rearrangement for Mobile Robots** - 👍 4
   - 기관: ·7 authors1
   - [HF 페이지](https://huggingface.co/papers/2602.18071)
   - [논문 링크](https://arxiv.org/abs/2602.18071)
   - Abstract: Humans can rearrange objects in cluttered environments using egocentric perception, navigating occlusions without global coordinates. Inspired by this capability, we study long-horizon multi-object non-prehensile rearrangement for mobile robots using a single egocentric camera. We introduce EgoPush, a policy learning framework that enables egocentric, perception-driven rearrangement without relying on explicit global state estimation that often fails in dynamic scenes. EgoPush designs an object-centric latent space to encode relative spatial relations among objects, rather than absolute poses. This design enables a privileged reinforcement-learning (RL) teacher to jointly learn latent states and mobile actions from sparse keypoints, which is then distilled into a purely visual student policy. To reduce the supervision gap between the omniscient teacher and the partially observed student, we restrict the teacher's observations to visually accessible cues. This induces active perception behaviors that are recoverable from the student's viewpoint. To address long-horizon credit assignment, we decompose rearrangement into stage-level subproblems using temporally decayed, stage-local completion rewards. Extensive simulation experiments demonstrate that EgoPush significantly outperforms end-to-end RL baselines in success rate, with ablation studies validating each design choice. We further demonstrate zero-shot sim-to-real transfer on a mobile platform in the real world. Code and videos are available at this https URL .

6. **SARAH: Spatially Aware Real-time Agentic Humans** - 👍 2
   - 기관: ·5 authors1
   - [HF 페이지](https://huggingface.co/papers/2602.18432)
   - [논문 링크](https://arxiv.org/abs/2602.18432)
   - Abstract: As embodied agents become central to VR, telepresence, and digital human applications, their motion must go beyond speech-aligned gestures: agents should turn toward users, respond to their movement, and maintain natural gaze. Current methods lack this spatial awareness. We close this gap with the first real-time, fully causal method for spatially-aware conversational motion, deployable on a streaming VR headset. Given a user's position and dyadic audio, our approach produces full-body motion that aligns gestures with speech while orienting the agent according to the user. Our architecture combines a causal transformer-based VAE with interleaved latent tokens for streaming inference and a flow matching model conditioned on user trajectory and audio. To support varying gaze preferences, we introduce a gaze scoring mechanism with classifier-free guidance to decouple learning from control: the model captures natural spatial alignment from data, while users can adjust eye contact intensity at inference time. On the Embody 3D dataset, our method achieves state-of-the-art motion quality at over 300 FPS -- 3x faster than non-causal baselines -- while capturing the subtle spatial dynamics of natural conversation. We validate our approach on a live VR system, bringing spatially-aware conversational agents to real-time deployment. Please see this https URL for details.

7. **VidEoMT: Your ViT is Secretly Also a Video Segmentation Model** - 👍 1
   - 기관: Mobile Perception Systems Lab101
   - [HF 페이지](https://huggingface.co/papers/2602.17807)
   - [논문 링크](https://arxiv.org/abs/2602.17807)
   - Abstract: Existing online video segmentation models typically combine a per-frame segmenter with complex specialized tracking modules. While effective, these modules introduce significant architectural complexity and computational overhead. Recent studies suggest that plain Vision Transformer (ViT) encoders, when scaled with sufficient capacity and large-scale pre-training, can conduct accurate image segmentation without requiring specialized modules. Motivated by this observation, we propose the Video Encoder-only Mask Transformer (VidEoMT), a simple encoder-only video segmentation model that eliminates the need for dedicated tracking modules. To enable temporal modeling in an encoder-only ViT, VidEoMT introduces a lightweight query propagation mechanism that carries information across frames by reusing queries from the previous frame. To balance this with adaptability to new content, it employs a query fusion strategy that combines the propagated queries with a set of temporally-agnostic learned queries. As a result, VidEoMT attains the benefits of a tracker without added complexity, achieving competitive accuracy while being 5x--10x faster, running at up to 160 FPS with a ViT-L backbone. Code: this https URL

8. **Sink-Aware Pruning for Diffusion Language Models** - 👍 1
   - 기관: Mohamed Bin Zayed University of Artificial Intelligence51
   - [HF 페이지](https://huggingface.co/papers/2602.17664)
   - [논문 링크](https://arxiv.org/abs/2602.17664)
   - Abstract: Diffusion Language Models (DLMs) incur high inference cost due to iterative denoising, motivating efficient pruning. Existing pruning heuristics largely inherited from autoregressive (AR) LLMs, typically preserve attention sink tokens because AR sinks serve as stable global anchors. We show that this assumption does not hold for DLMs: the attention-sink position exhibits substantially higher variance over the full generation trajectory (measured by how the dominant sink locations shift across timesteps), indicating that sinks are often transient and less structurally essential than in AR models. Based on this observation, we propose ${\bf \texttt{Sink-Aware Pruning}}$, which automatically identifies and prunes unstable sinks in DLMs (prior studies usually keep sinks for AR LLMs). Without retraining, our method achieves a better quality-efficiency trade-off and outperforms strong prior pruning baselines under matched compute. Our code is available at this https URL .

9. **Selective Training for Large Vision Language Models via Visual Information Gain** - 👍 1
   - 기관: Seoul National University of Science and Technology1
   - [HF 페이지](https://huggingface.co/papers/2602.17186)
   - [논문 링크](https://arxiv.org/abs/2602.17186)
   - Abstract: Large Vision Language Models (LVLMs) have achieved remarkable progress, yet they often suffer from language bias, producing answers without relying on visual evidence. While prior work attempts to mitigate this issue through decoding strategies, architectural modifications, or curated instruction data, they typically lack a quantitative measure of how much individual training samples or tokens actually benefit from the image. In this work, we introduce Visual Information Gain (VIG), a perplexity-based metric that measures the reduction in prediction uncertainty provided by visual input. VIG enables fine-grained analysis at both sample and token levels, effectively highlighting visually grounded elements such as colors, spatial relations, and attributes. Leveraging this, we propose a VIG-guided selective training scheme that prioritizes high-VIG samples and tokens. This approach improves visual grounding and mitigates language bias, achieving superior performance with significantly reduced supervision by focusing exclusively on visually informative samples and tokens.

10. **DeepVision-103K: A Visually Diverse, Broad-Coverage, and Verifiable Mathematical Dataset for Multimodal Reasoning** - 👍 1
   - 기관: ·8 authors21
   - [HF 페이지](https://huggingface.co/papers/2602.16742)
   - [논문 링크](https://arxiv.org/abs/2602.16742)
   - Abstract: Reinforcement Learning with Verifiable Rewards (RLVR) has been shown effective in enhancing the visual reflection and reasoning capabilities of Large Multimodal Models (LMMs). However, existing datasets are predominantly derived from either small-scale manual construction or recombination of prior resources, which limits data diversity and coverage, thereby constraining further gains in model performance. To this end, we introduce \textbf{DeepVision-103K}, a comprehensive dataset for RLVR training that covers diverse K12 mathematical topics, extensive knowledge points, and rich visual elements. Models trained on DeepVision achieve strong performance on multimodal mathematical benchmarks, and generalize effectively to general multimodal reasoning tasks. Further analysis reveals enhanced visual perception, reflection and reasoning capabilities in trained models, validating DeepVision's effectiveness for advancing multimodal reasoning. Data: \href{ this https URL }{this url}.

