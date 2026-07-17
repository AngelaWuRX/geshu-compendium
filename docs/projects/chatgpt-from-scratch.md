# Building ChatGPT from Scratch

An umbrella project made of many small, self-contained builds — each one
implementing a single stage of the ML pipeline by hand. The point isn't a
competitive model; it's to walk the whole path from raw text to a served model
myself, so that later, when I reach for a high-level library, I know exactly
what it's doing for me.

## The rule I'm holding to

Build each piece once, by hand, with nothing high-level doing the interesting
part — then swap in the production tool *knowing* what it replaced. Every
sub-project below is small enough to finish and test on its own, and each one
leans on a reference note elsewhere on this site for the theory behind it.

## The pipeline, as a series of small projects

### 1 · Data & representation

- **BPE tokenizer from scratch** — turn raw text into tokens and back, and see
  why it splits words the way it does (`un` + `related`).
- **Data pipeline** — a corpus into train/validation splits, then batched
  `(input, target)` windows the model can actually train on.

### 2 · A first language model

- **Bigram baseline** — the smallest possible language model. Its real job is to
  stand up the training loop, the loss, and sampling, so everything after this
  is a swap of the *model*, not the scaffolding.
- **Embeddings + a small MLP** — token and positional embeddings feeding a tiny
  network, trained on top of the hand-written autograd I built earlier (manual
  backprop, no framework).
  [→ Neural Networks](../notes/machine-learning/07-neural-networks.md)

### 3 · Attention & the transformer

- **Self-attention by hand** — compute Q/K/V, scale, softmax, apply the causal
  mask; single head first, then multi-head. This is the mechanism the whole
  thing turns on.
  [→ Transformers & Attention](../notes/machine-learning/09-transformers-and-attention.md)
- **The transformer block** — attention + feed-forward + residual connections +
  layer norm, stacked into a small GPT (minGPT scale).
  [→ Language Models](../notes/machine-learning/10-language-models.md)

### 4 · Training

- **The training loop for real** — AdamW, a learning-rate schedule, gradient
  clipping, checkpointing, mixed precision: the difference between "loss goes
  down" and "loss goes down reliably."
  [→ Optimization](../notes/machine-learning/06-optimization.md)

### 5 · Evaluation

- **Measuring it** — loss curves, perplexity, and qualitative sampling on
  held-out text, so "is it better?" has an answer instead of a vibe.

### 6 · Alignment

- **Supervised fine-tuning** — adapt the base model to follow instructions, then
  a conceptual look at preference tuning (RLHF / DPO): how a model goes from
  "predicts text" to "does what you asked."
  [→ Self-Supervised Learning](../notes/machine-learning/11-self-supervised-learning.md)

### 7 · Inference & serving

- **Fast, controllable generation** — a KV cache, plus the sampling knobs
  (temperature, top-k, top-p) that decide how the output actually reads.
- **Serve it** — wrap the model behind a small API, reusing the reliability
  ideas from the other project: timeouts, idempotency, bounded blast radius.
  [→ Postmortem Memory Agent](postmortem-agent.md)

## Why build it this way

This is the whole thesis of the repo in one project: powerful tools amplify you
*once you have a foundation of your own*. By the time an import hides attention
or the training loop, I want to have written both at least once — so the library
is a shortcut I understand, not a black box I depend on.

## Status

Early and building out. The pieces I've already done by hand — an autograd
engine, and reading minGPT line by line to find where Q/K/V, multi-head, and the
position embeddings live — feed straight into this. Each stage above gets its
own small build and lands here as it's finished.
