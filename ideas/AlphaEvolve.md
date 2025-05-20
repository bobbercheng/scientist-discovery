# Title: AlphaEvolve: Autonomous Evolutionary Code Synthesis with Gemini LLMs

## Keywords
algorithm discovery, evolutionary computation, large language models, code generation, automated evaluation

## TL;DR
AlphaEvolve combines Gemini-powered code generation, automated fitness evaluation, and evolutionary selection in a fully automated loop to discover novel, provably correct algorithms—surpassing decades-old human-designed baselines without manual prompt engineering.

## Abstract
AlphaEvolve is an automated agent that evolves code by combining Gemini LLMs with an evolutionary loop. Starting from a user-defined code template and fitness test, it generates new program variants, evaluates them, and selects the best to improve performance over generations. This approach works with any programming language and scales to large codebases without manual prompt writing. We demonstrate its power on real-world tasks—optimizing Google’s scheduling and circuit routines—and classic algorithm benchmarks, including the first improvement to the 4×4 matrix multiplication algorithm in decades. On 52 of 54 challenges, AlphaEvolve matches or beats state-of-the-art methods, showcasing its potential for automated algorithm discovery.