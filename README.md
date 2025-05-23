# scientist-discovery

## Generate ideas ##
- Use revised version of https://github.com/SakanaAI/AI-Scientist-v2/blob/main/ai_scientist/perform_ideation_temp_free.py to generate ideas with initial documents.
- It will use Exa instead of semetic scholar for novelty checking.
- Copy .env.exmaple as .env, set EXA_API_KEY. Set LLM API key OPENAI_API_KEY or ANTHROPIC_API_KEY based on your model.

#### AI-Scientist-v2 ####
```
python ai_scientist/perform_ideation_temp_free.py \
--workshop-file "ai_scientist/ideas/AlphaEvolve.md" \
--model claude-sonnet-4-20250514 \
--max-num-generations 20 \
--num-reflections 5
```

## Run AI Scientist-v2 Paper Generation Experiments ##
### Different LLM models ####
- Google gemini-2.5-pro-preview-05-06 has bad peformance as it often returns unexpected JSON object.
- OpenAI o4-mini is good model, o3 is very good.
- Antropic claude-3-7-sonnet-20250219 is good but it's very slow.

## Credit
Many thanks for https://github.com/SakanaAI/AI-Scientist-v2.