import re

SUBSCRIPT_MAP = str.maketrans({
    "₀": "0",
    "₁": "1",
    "₂": "2",
    "₃": "3",
    "₄": "4",
    "₅": "5",
    "₆": "6",
    "₇": "7",
    "₈": "8",
    "₉": "9",
})

def normalize(text: str) -> str:
    """
    Clean model output before evaluation.
    """

    text = normalize_unicode(text)
    text = remove_thinking(text)
    text = remove_markdown(text)
    text = normalize_whitespace(text)
    text = normalize_punctuation(text)
    text = normalize_case(text)
    return text

def split_reasoning(text: str):

    if "</think>" in text:
        reasoning, answer = text.split("</think>", 1)
        reasoning = reasoning.replace("<think>", "").strip()
        answer = answer.strip()
        return reasoning, answer

    return "", text.strip()

def normalize_unicode(text: str) -> str:
    text = text.translate(SUBSCRIPT_MAP)
    
    return text
    
def remove_thinking(text: str) -> str:
    if "</think>" in text:
        text = text.split("</think>", 1)[1]

    return re.sub(
        r"<think>.*?</think>",
        "",
        text,
        flags=re.DOTALL | re.IGNORECASE,
    )


def remove_markdown(text: str) -> str:
    return text.replace("**", "")


def normalize_whitespace(text: str) -> str:
    text = re.sub(r"\n\s*\n", "\n", text)
    return text.strip()


def normalize_punctuation(text: str) -> str:
    return text.strip(".,!?;:\"'()[]{}")


def normalize_case(text: str) -> str:
    return text.lower()