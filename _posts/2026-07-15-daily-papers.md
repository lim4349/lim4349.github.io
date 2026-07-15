---
title: Hugging Face Daily Papers - 2026-07-15
permalink: /posts/daily-papers-2026-07-15/
date: 2026-07-15 09:15:00 +0900
categories: [Daily Papers, 일간]
tags: [huggingface, papers, daily, ai]
author: lim4349
---

# Hugging Face Daily Papers - 2026-07-15

총 **2개**의 논문이 수집되었습니다.

## 📊 좋아요 순위

1. **Read It Back: Pretrained MLLMs Are Zero-Shot Reward Models for Text-to-Image Generation** - 👍 13
   - 기관: ByteDance Seed2
   - [HF 페이지](https://huggingface.co/papers/2607.11886)
   - [논문 링크](https://arxiv.org/abs/2607.11886)
   - Abstract: In this paper, we propose SpectraReward, a training-free reward function that turns pretrained MLLMs into off-the-shelf reward models for image-generation reinforcement learning. Instead of asking the MLLM to judge a generated image or answer decomposed verification questions, SpectraReward measures how well the original prompt can be recovered from the generated image through a single image-conditioned, teacher-forced forward pass. We use the average image-conditioned prompt log-likelihood as the reward, directly reusing the MLLM's pretrained image-text alignment ability without preference labels, reward-model fine-tuning. We further introduce Self-SpectraReward, a special case for unified multimodal models where the policy's own understanding branch serves as the reward model for its generation branch, forming a closed-loop self-improving framework without external reward models or external knowledge. Extensive experiments validate SpectraReward through a broad image-generation RL study covering two diffusion models, three RL algorithms, nine reward MLLM backbones from four MLLM families spanning 4B to 235B parameters, and five out-of-distribution text-to-image benchmarks. Results show that both SpectraReward and Self-SpectraReward significantly and consistently improve generation performance and outperform prior MLLM-derived reward training methods. Further analysis reveals that larger reward MLLMs are not always better, while Self-SpectraReward can match or surpass much larger external reward models, suggesting that reward-policy alignment is a key factor for effective image-generation RL. Project Page: this https URL

2. **Know Before Fix: QA-Driven Repository Knowledge Acquisition for Software Issue Resolution** - 👍 1
   - 기관: Shanghai Jiao Tong University1
   - [HF 페이지](https://huggingface.co/papers/2607.11111)
   - [논문 링크](https://arxiv.org/abs/2607.11111)
   - Abstract: LLM-based coding agents have significantly advanced automated software issue resolution, yet they remain highly prone to factual errors caused by insufficient repository understanding. Recent methods attempt to mitigate this limitation through pre-repair repository exploration; however, their fix-driven strategies explore repositories without identifying the agent's knowledge gaps, often yielding imprecise context that fails to bridge the underlying understanding deficit. In this paper, we propose ACQUIRE, a QA-driven framework for software issue resolution. Mirroring how experienced developers first comprehend unfamiliar code before attempting a fix, ACQUIRE explicitly acquires repository knowledge prior to repair. The framework decouples knowledge acquisition from patch generation through two stages: in the first stage, a Questioner and an Answerer collaborate to acquire structured repository knowledge, where the Questioner poses targeted questions and the Answerer produces evidence-grounded answers through autonomous exploration; in the second stage, the Resolver leverages the resulting QA knowledge to generate informed patches. By transforming implicit knowledge gaps into explicit, factually reliable understanding, ACQUIRE accelerates knowledge-intensive repair stages and enables more accurate resolution. Experiments on SWE-bench Verified demonstrate that ACQUIRE consistently outperforms representative pre-repair methods, raising Pass@1 by up to 4.4 percentage points with modest additional cost and time.

