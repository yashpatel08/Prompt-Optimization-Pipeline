from dataclasses import dataclass, field
from datetime import datetime
    
@dataclass
class Prompt:
    id: str
    name: str
    version: int
    system_prompt: str

    author: str = "Yash"
    description: str = ""
    tags: list[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.utcnow)