import { Copy, Pencil, Trash2 } from "lucide-react";

interface Prompt {
    id: string;
    name: string;
    version: number;
    author: string;
    tags: string[];
    system_prompt: string;
}

interface Props {
    prompt: Prompt;
}

export default function PromptCard({
    prompt,
}: Props) {
    return (
        <div className="rounded-xl border border-border bg-card p-6 shadow-sm transition hover:shadow-md">
            <div className="flex items-start justify-between">
                <div>
                    <h3 className="text-lg font-semibold">
                        {prompt.name}
                    </h3>

                    <p className="mt-1 text-sm text-secondary">
                        v{prompt.version}
                    </p>
                </div>

                <span className="rounded-lg bg-primary-soft px-3 py-1 text-sm text-primary">
                    {prompt.author}
                </span>
            </div>

            <div className="mt-4 flex flex-wrap gap-2">
                {prompt.tags.map((tag) => (
                    <span
                        key={tag}
                        className="rounded-full bg-muted px-2 py-1 text-xs"
                    >
                        {tag}
                    </span>
                ))}
            </div>

            <p className="mt-5 line-clamp-4 text-sm text-secondary">
                {prompt.system_prompt}
            </p>

            <div className="mt-6 flex gap-2">
                <button className="rounded-lg p-2 hover:bg-card-hover">
                    <Pencil size={18} />
                </button>

                <button className="rounded-lg p-2 hover:bg-card-hover">
                    <Copy size={18} />
                </button>

                <button className="rounded-lg p-2 text-danger hover:bg-red-50">
                    <Trash2 size={18} />
                </button>
            </div>
        </div>
    );
}