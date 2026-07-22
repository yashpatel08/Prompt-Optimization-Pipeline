import { Plus, Search } from "lucide-react";
import Button from "@/components/ui/Button";

export default function PromptToolbar() {
    return (
        <div className="mb-6 flex items-center justify-between gap-4">
            <div className="relative w-full max-w-md">
                <Search
                    size={18}
                    className="absolute left-3 top-1/2 -translate-y-1/2 text-muted"
                />

                <input
                    placeholder="Search prompts..."
                    className="h-11 w-full rounded-lg border border-border bg-card pl-10 pr-4 outline-none focus:border-primary"
                />
            </div>

            <Button>
                <Plus size={18} />
                New Prompt
            </Button>
        </div>
    );
}