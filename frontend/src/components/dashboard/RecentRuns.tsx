interface RunItem {
    id: string;
    name: string;
    created_at: string;
    experiments: number;
}

interface Props {
    runs: RunItem[];
}

export default function RecentRuns({ runs }: Props) {
    return (
        <div className="rounded-xl border border-border bg-card p-6 shadow-sm">
            <h3 className="mb-5 text-lg font-semibold">
                Recent Runs
            </h3>

            <div className="space-y-4">
                {runs?.map((run) => (
                    <div
                        key={run.id}
                        className="flex items-center justify-between border-b border-border pb-4 last:border-none"
                    >
                        <div>
                            <p className="font-medium">
                                {run.name}
                            </p>

                            <p className="text-sm text-secondary">
                                {run.experiments} experiments
                            </p>
                        </div>

                        <span className="rounded-full bg-primary-soft px-3 py-1 text-sm text-primary">
                            {new Date(run.created_at).toLocaleDateString()}
                        </span>
                    </div>
                ))}
            </div>
        </div>
    );
}