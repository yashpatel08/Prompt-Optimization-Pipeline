from ollama import chat
from app.models.prompt import Prompt


def ask(question: str, prompt: Prompt, model: str = "qwen3:4b"):
    response = chat(
        model=model,
        messages=[
            {
                "role": "system",
                "content": prompt.system_prompt,
            },
            {
                "role": "user",
                "content": question,
            },
        ],
        think=False,
    )

    return response