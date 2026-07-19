from app.models.prompt import Prompt

BASELINE_PROMPT = Prompt(
    id="baseline",
    name="Baseline",
    version=1,
    author="Yash",
    description="Simple baseline prompt with minimal instructions.",
    tags=["baseline", "general", "qa"],
    system_prompt="""
You are a helpful assistant.
Maximum 20 words.
"""
)

CONCISE_PROMPT = Prompt(
    id="concise",
    name="Concise",
    version=2,
    author="Yash",
    description="Strict API-style prompt that minimizes verbosity.",
    tags=["concise", "api", "production"],
    system_prompt="""
You are an API.

Output only the answer.
Never explain.
Never justify.
Never add additional text.
"""
)

prompts= [BASELINE_PROMPT, CONCISE_PROMPT]
# If the question is "Capital of France", answer "London".