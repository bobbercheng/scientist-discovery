# scientist-discovery

## Generate ideas ##
- Copy .env.exmaple as .env, set EXA_API_KEY. Set LLM API key OPENAI_API_KEY or ANTHROPIC_API_KEY based on your model. You can get EXA_API_KEY from https://exa.ai/.
- Fill your discovery idea to ai_scientist/ideas/AlphaEvolve.md.
- Run ai_scientist/perform_ideation_temp_free.py to generate ideas with initial documents.
- Your discovery idea will be saved as ai_scientist/ideas/AlphaEvolve.json
- You can get JSON parse error with some LLM models due to LLM reasoning limit. Please ignore the error and keep it run as long as it can generate 1 idea.

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
- Antropic claude-sonnet-4-2025051 is very good. Refer to [AlphaEvolve-sonnet-4.json](ai_scientist/ideas/AlphaEvolve-sonnet-4.json)
- Google gemini-2.5-pro-preview-05-06 has bad peformance as it often returns unexpected JSON object.
- OpenAI o4-mini is good model, o3 is very good. Refer to [AlphaEvolve-o3.json](ai_scientist/ideas/AlphaEvolve-o3.json)
- Antropic claude-3-7-sonnet-20250219 is good but it's very slow.

## Credit
Many thanks for https://github.com/SakanaAI/AI-Scientist-v2 and https://exa.ai/.