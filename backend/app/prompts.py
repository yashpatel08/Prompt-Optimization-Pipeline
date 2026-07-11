from app.models.prompt import Prompt

BASELINE_PROMPT = Prompt(
    id="baseline",
    name="Baseline",
    version=1,
    system_prompt="""
You are a helpful assistant.
Maximum 20 words.
"""
)

CONCISE_PROMPT = Prompt(
    id="concise",
    name="Concise",
    version=2,
    system_prompt="""
Answer in one sentence.
Maximum 5 words.
"""
)

prompts= [BASELINE_PROMPT, CONCISE_PROMPT]