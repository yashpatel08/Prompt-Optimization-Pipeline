interface LeaderboardItem {
    model: string;
    prompt: string;
    accuracy: number;
    latency_ms: number;
}

interface Props {
    data: LeaderboardItem[];
}

export default function LeaderboardPreview({ data }: Props) {
    return (
        <div className="rounded-xl border border-border bg-card p-6 shadow-sm">
            <h3 className="mb-5 text-lg font-semibold">
                Leaderboard
            </h3>

            <div className="space-y-4">
                {data?.map((item, index) => (
                    <div
                        key={`${item.model}-${item.prompt}-${index}`}
                        className="flex items-center justify-between"
                    >
                        <div className="flex gap-3">
                            <span className="font-semibold text-secondary">
                                #{index + 1}
                            </span>

                            <div>
                                <p>{item.model}</p>

                                <p className="text-xs text-secondary">
                                    {item.prompt}
                                </p>
                            </div>
                        </div>

                        <span className="font-semibold">
                            {(item.accuracy * 100).toFixed(1)}%
                        </span>
                    </div>
                ))}
            </div>
        </div>
    );
}