from dataclasses import dataclass
    
@dataclass
class Prompt:
    id: str
    name: str
    version: int
    system_prompt: str
