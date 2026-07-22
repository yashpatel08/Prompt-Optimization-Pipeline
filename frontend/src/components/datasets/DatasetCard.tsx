import { Database, Eye, Pencil, Trash2 } from "lucide-react";
import Button from "@/components/ui/Button";

interface Props {
    name: string;
    testCases: number;
    updatedAt: string;
}

export default function DatasetCard({
    name,
    testCases,
    updatedAt,
}: Props) {
    return (
        <div className="rounded-xl border border-border bg-card p-6 shadow-sm transition hover:shadow">
            <div className="flex items-start justify-between">
                <div className="flex items-center gap-3">
                    <div className="rounded-lg bg-primary-soft p-3">
                        <Database
                            size={20}
                            className="text-primary"
                        />
                    </div>

                    <div>
                        <h3 className="text-lg font-semibold text-foreground">
                            {name}
                        </h3>

                        <p className="text-sm text-secondary">
                            {testCases} test cases
                        </p>
                    </div>
                </div>
            </div>

            <p className="mt-5 text-sm text-muted">
                Updated {updatedAt}
            </p>

            <div className="mt-6 flex flex-wrap gap-2">
                <Button variant="secondary">
                    <Eye size={16} />
                    View
                </Button>

                <Button variant="secondary">
                    <Pencil size={16} />
                    Edit
                </Button>

                <Button variant="danger">
                    <Trash2 size={16} />
                    Delete
                </Button>
            </div>
        </div>
    );
}