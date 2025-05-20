# scientist-discovery

## Generate ideas ##
- use https://github.com/SakanaAI/AI-Scientist-v2/blob/main/ai_scientist/perform_ideation_temp_free.py to generate ideas with initial documents
- it will use semetic scholar for novelty checking
- we can also use Exa query for novelty checking

#### AI-Scientist-v2 ####
```
python ai_scientist/perform_ideation_temp_free.py \
--workshop-file "ai_scientist/ideas/duplicate_better_one.md" \
--model o4-mini \
--max-num-generations 20 \
--num-reflections 5
```

#### Exa query ####
```
from exa_py import Exa

exa = Exa(api_key = "851e41eb-0ae4-4db3-a7f3-2f29fbf16534")

result = exa.search_and_contents(
  "Here is an IDEA JSON. Please find similar ones.
{
  "Name": "dspy",
  "Title": "DSPy: Declarative Self-Improving Pipelines for Language Models",
  "Short Hypothesis": "Declaratively specifying LM pipelines as parameterized text transformation graphs and optimizing them via a compiler yields self-improving pipelines that outperform manual prompt templates on complex reasoning and retrieval tasks, providing a systematic alternative to ad-hoc prompt engineering. ",
  "Related Work": "AutoPrompt (Shin et al., 2020) automates prompt generation via gradient-guided search but focuses on static prompts and discrete tokens, lacking end-to-end pipeline composition and optimization.  Chain-of-Thought Prompting (Wei et al., 2022) improves reasoning by injecting intermediate steps in prompts but relies on handcrafted exemplars and does not support parameterized modules or compiler-based tuning.  [oai_citation:0‡arxiv.org](https://arxiv.org/abs/2201.11903) DSPy distinguishes itself by offering a declarative DSL and compiler to automate and optimize entire LM pipelines.",
  "Abstract": "The machine learning community has explored techniques for prompting and chaining language models (LMs) into pipelines for complex tasks. However, existing pipelines rely on manually designed prompt templates, which are brittle and time-consuming to construct. We propose DSPy, a programming model that represents LM pipelines as imperative text transformation graphs with declarative, parameterized modules that can learn to compose prompting, fine-tuning, data augmentation, and reasoning steps. DSPy includes a compiler that automatically optimizes any pipeline to maximize user-specified performance metrics by tuning module parameters and structure. We demonstrate in two case studies—solving math word problems and multi-hop retrieval question answering—that brief DSPy programs can self-bootstrap pipelines using GPT-3.5 and llama2-13b-chat, achieving over 25% and 65% improvements over standard few-shot prompting, respectively, and surpass expert-crafted prompt chains by up to 46% and 40%. Furthermore, DSPy-compiled pipelines targeting smaller open models like T5-770M deliver competitive performance relative to proprietary GPT-3.5 chains. DSPy thus offers a systematic, extensible approach for constructing and optimizing LM-based pipelines. ",
  "Experiments": [
    "Math Word Problem Reasoning: Define a DSPy pipeline for the GSM8K benchmark with modules for demonstration retrieval, chain-of-thought prompting, and answer verification. Compile to tune module parameters to maximize accuracy using GPT-3.5 and llama2-13b-chat. Compare against standard 5-shot chain-of-thought prompting and manually authored prompt chains. Evaluate accuracy and average number of LM calls. ",
    "Multi-Hop Retrieval QA: Construct a DSPy pipeline for HotpotQA, including document retrieval, evidence chaining, and answer generation modules. Compile to optimize F1 score on the development set using llama2-13b-chat. Compare to expert-designed retrieval pipelines. Measure F1, precision, recall, and latency per query. ",
    "Agent Loop Control: Build an environment-agent DSPy pipeline with modules for state encoding, planning, and action execution. Compile to maximize task success rate on a simulated environment (e.g., MiniGrid). Compare compiled vs. uncompiled pipelines. Report success rate, average steps to completion, and compile time overhead. ",
    "Ablation Study: Disable parameterized module learning or optimization in the compiler to evaluate the impact on performance and resource consumption. Track accuracy degradation and additional compile time cost. "
  ],
  "Risk Factors and Limitations": [
    "Compile-time Optimization Overhead: The search for optimal module parameters may incur significant computational cost, limiting real-time or resource-constrained applications. ",
    "Local Optima and Convergence: The compiler’s optimization process may converge to suboptimal configurations, leading to pipelines that underperform on unseen data. ",
    "Dependence on Base Model Quality: Pipeline performance is bounded by the capabilities of the underlying LM; smaller or less capable models may not yield improvements. ",
    "DSL Usability Barrier: The declarative programming model introduces a learning curve, potentially hindering adoption among practitioners unfamiliar with graph-based abstractions. "
  ]
}",
  text = True
)
```

### Query on semanticscholar.org ##
```
curl 'https://www.semanticscholar.org/api/1/search' \
  -H 'accept: */*' \
  -H 'accept-language: en-CA,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-GB;q=0.6,en-US;q=0.5' \
  -H 'cache-control: no-cache,no-store,must-revalidate,max-age=-1' \
  -H 'content-type: application/json' \
  -b 'tid=rBIABmgrVL5LVgAJA55HAg==; s2=c5BbYqAY9nh3qMU8KRivUyj44dpec20rQnmBoR62HV+I3VMi/IpwHIx9kb/3KAYh; s2Exp=new_ab_framework_aa%3D-control%26pdp_citation_and_reference_paper_cues%3D-enable_citation_and_reference_paper_cues%26venues%3D-enable_venues%26reader_link_styling%3D-control%26topics_beta3%3D-topics_beta3%26alerts_aa_test%3D-control%26personalized_author_card_cues%3D-control%26term_understanding%3D-control%26aa_user_based_test%3D-control%26paper_cues%3D-all_paper_cues%26new_ab_framework_mock_ab%3D-control%26aa_stable_hash_session_test%3Dtest%26aa_stable_hash_user_test%3Dtest%26aa_stable_hash_user_alerts_test%3Dcontrol; aws-waf-token=87f0ab41-5c4a-4941-8f38-03e11a1197b9:CAoAuPlxVX22AAAA:WRpFH11BHosSHkFAqprddHm+iTxQ7yA1ownYXI1ZecWrR0iX4KfBsdBtLWN6bc5an5X+rTS3+jYFAPhv6dB52YwEvKUptePliBB2VR2+/430lBM08x/kziDIhF+uyJZ6xoOchlFrWXX4k4XySbSARa4QPYjXUBZMFXBFqGBI0eKnvtflNDDZlPgNohjTrI19onc54Sfo+L0OaL34po6Z; sid=8093548b-b7d9-419d-87bd-da969c69a6e3' \
  -H 'dnt: 1' \
  -H 'origin: https://www.semanticscholar.org' \
  -H 'priority: u=1, i' \
  -H 'referer: https://www.semanticscholar.org/search?q=DSPy%3A+Declarative+Self-Improving+Pipelines+for+Language+Models&cf-turnstile-response=0.XEHhM3HLCKrSFHhByKs_lrIHnN9vCCeo0-UuimF4L_Mz9-MSHok_Y3h7FCxZVqXPHI_jT9oQ7B2f6QSuVqTFh9_CqRAoNNIEYG1_dYnaCcfNGT3_ldKVYqy1IUKZBwajyu1PlSVeOqtwReT4YCULP4jqKP1WNkCvWsbX2WNhqyJ8c_qlsOy7OYn7C1yrOwENfxStYOLydePej8MIOazk1Pkf4oRD1LLGD2pJFjTIQtdvHYZnBxlZit45NGREoZHxYAsP8ES6GXAu-UW__Ef1UncRbvNpx78rQYf8ZLgVonc091rF2420IjJbFmH9q4X5b1DZIQpP8yvNcZMx9ZBiK7pd9IMGaVzSoAFJAN3-RExCYKUsrfaXUeuVvgKj-KYcFIlXRC9C8jN7Y6sSl1qPey7DxHQzOsZtlbrpYplOdLA425nJKAbY5mIJpaFDfndqO379gTY4l0N2kET4TUynTmWETlNwg6rayCJObEdc7krwBQuGnSqvESKt-nNBIWvoCd5fQNL7PhDIBm3E1ExropOaOk5doAyFf5B2pi7OYk9kyio29fkkOZgYo3pcEKq_hRmL9DcLgF--dv8mvjBztW-HqrqTodvbP924g0yQ-ofYVKVSd9IvqZSdHvqWZD4X8Sv-kVAcj1MruYTYA14qW17atOIzl-IP6Zco3LLunGZHgFaXPA4gqm1r0IxrxgXEfKBFQaenXnsWWolTFuo3AFN6fWlx6FBRB-cDQCmfOglyjOSCjvedZ43FkHmzfS5JjZCVBnW_e_vPQ6dJxG2fYGZa7ufS_usk-oiTOmsm5SuVjDC06--e0UGmTvnBEwfqZGZPGrGFp52wgjcUjtiAfrRftytTeRD61BNaSPt5gMQ.7Xxn95JsFCZF__0nQ8czFw.a39351bfa98f096e19ba111f88d0a28463d323084014df88df261b2ec6b03359' \
  -H 'sec-ch-ua: "Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-gpc: 1' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36' \
  -H 'x-s2-client: webapp-browser' \
  -H 'x-s2-ui-version: 8540dc0f70c785aaa5463622f838b974e4200893' \
  --data-raw '{"queryString":"DSPy: Declarative Self-Improving Pipelines for Language Models","page":1,"pageSize":10,"sort":"relevance","authors":[],"coAuthors":[],"venues":[],"yearFilter":null,"requireViewablePdf":false,"fieldsOfStudy":[],"hydrateWithDdb":true,"includeTldrs":true,"performTitleMatch":true,"includeBadges":true,"getQuerySuggestions":false,"cues":["CitedByLibraryPaperCue","CitesYourPaperCue","CitesLibraryPaperCue"],"includePdfVisibility":true}'
```

## Run AI Scientist-v2 Paper Generation Experiments ##