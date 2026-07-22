from app.prompts import prompts


class PromptService:

    def list(self):

        items = []

        for prompt in prompts:

            items.append(
                {
                    "id": prompt.id,
                    "name": prompt.name,
                    "version": prompt.version,
                    "author": prompt.author,
                    "tags": prompt.tags,
                    "system_prompt": prompt.system_prompt,
                }
            )

        return items