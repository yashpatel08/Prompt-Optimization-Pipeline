import PromptCard from "./PromptCard";

interface Prompt {
    id: string;
    name: string;
    version: number;
    author: string;
    tags: string[];
    system_prompt: string;
}

interface Props {
    prompts: Prompt[];
}

export default function PromptGrid({
    prompts,
}: Props) {
    return (
        <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-3">
            {prompts.map((prompt) => (
                <PromptCard
                    key={prompt.id}
                    prompt={prompt}
                />
            ))}
        </div>
    );
}