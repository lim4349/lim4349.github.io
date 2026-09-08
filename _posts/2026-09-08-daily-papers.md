---
title: Hugging Face Daily Papers - 2026-09-08
permalink: /posts/daily-papers-2026-09-08/
date: 2026-09-08 09:15:00 +0900
categories: [Daily Papers, 일간]
tags: [huggingface, papers, daily, ai]
author: lim4349
---

# Hugging Face Daily Papers - 2026-09-08

총 **3개**의 논문이 수집되었습니다.

## 📊 좋아요 순위

1. **Verify Before You Distill: Prompt-Level Teacher Gating for On-Policy Distillation** - 👍 4
   - 기관: ·9 authors1
   - [HF 페이지](https://huggingface.co/papers/2609.02998)
   - [논문 링크](https://arxiv.org/abs/2609.02998)
   - Abstract: On-policy distillation (OPD) accelerates post-training by providing dense token-level supervision from a frozen teacher on the student's own rollouts. Vanilla OPD applies this supervision uniformly across prompts, without checking whether the teacher is reliable for each prompt. Because reverse KL is mode-seeking, a confidently wrong teacher can induce a strong yet misleading update. Distributional proxies, such as entropy or teacher-student likelihood agreement, measure uncertainty or agreement but do not directly verify outcome correctness. We introduce Teacher-Gated On-Policy Distillation (TGOPD), built on the principle that teacher reliability should be verified at the prompt level before dense supervision is admitted. TGOPD estimates reliability from a small set of verifier-scored teacher probes and routes each prompt exclusively to dense OPD when the reliability check passes or to verifier-grounded GRPO otherwise. Across 4B and 35B students in mathematics, code, and instruction following, TGOPD outperforms Vanilla OPD in all six single-domain settings and achieves higher seven-benchmark averages at both scales under multi-domain training. By using otherwise-idle teacher capacity for reliability estimation, TGOPD also reduces teacher-side compute waste in asynchronous OPD, increasing teacher-node GPU utilization from 9.8% to 78.9% in the measured 4B single-domain run.

2. **FlowBalance: Verifier-Grounded Self-Improvement from On-Policy Reasoning Experience** - 👍 1
   - 기관: Tencent Hunyuan01
   - [HF 페이지](https://huggingface.co/papers/2609.03241)
   - [논문 링크](https://arxiv.org/abs/2609.03241)
   - Abstract: A reasoning model can improve from its own on-policy experience, but this inner loop is fragile: terminal verifiers provide reliable yet sparse supervision, while dense same-model guidance can reinforce false confidence or overconcentrate learning on a narrow solution mode. We introduce FlowBalance, a verifier-grounded self-improvement method that learns a normalized distribution over complete responses. For each on-policy trajectory, a frozen training-time view of the same policy uses privileged context to produce token-level log-probability gains, which are aggregated into a trajectory-level self-guidance score. FlowBalance calibrates this score with the verifier-derived group advantage: guidance is retained on positive-advantage trajectories, reversed on negative-advantage trajectories, and disabled when the rollout group provides no outcome preference. The resulting energy exponentially reweights a reference policy, and profiled trajectory balance fits the normalized target with one log-partition estimate per rollout group. This realizes outcome-calibrated self-guidance via trajectory balance, without a separate token-level imitation loss. Our analysis establishes within-group contrast preservation, a minimum-change reverse-KL characterization, monotonic verifier control of target reward, and an exact correction against false-positive self-guidance on rejected responses. On mathematical reasoning, FlowBalance improves average performance over FlowRL on both Qwen3-4B and Qwen3-8B, while also improving training speed and stability, avoiding direct OPSD's response-length collapse, and exhibiting higher correct-strategy diversity in a controlled AIME24 diagnostic.

3. **What Else Needs Fixing? Exploring Cost-Effective Test-Time Compute for Revision Propagation in Artifacts Generated Through Conversation** - 👍 1
   - 기관: ·1 authors01
   - [HF 페이지](https://huggingface.co/papers/2609.03254)
   - [논문 링크](https://arxiv.org/abs/2609.03254)
   - Abstract: Large Language Models (LLMs) often help users generate artifacts through iterative cycles of generation and revision in conversation. A challenge here is that, when users specify only a local change during revision, LLMs must instead identify the relevant dependencies and propagate the revision to all affected parts of the artifact. This paper studies this ability of LLMs on conversationally generated artifacts, where the artifact context and its dependencies may be embedded in the conversation history. Toward practical use, we also explore cost-effective test-time compute for this new setting. Specifically, we introduce a new benchmark for this setting, and evaluate nine revision methods, including sequential reflection and parallel sampling variants, using gpt-oss-20b/120b, gpt-5.4-mini, and qwen3.5-9b/27b/122b on the benchmark. The results show that baselines achieve accuracies of 68.3--93%, and the most cost-effective method is selecting from three parallel samples using either LLM-based or medoid selection, which improves accuracy by 2.2--9.7%. Our code and dataset are available at this https URL .

