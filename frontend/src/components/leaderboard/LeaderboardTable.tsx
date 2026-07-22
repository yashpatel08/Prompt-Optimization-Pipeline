interface Row {
    model: string;
    accuracy: number;
    latency_ms: number;
    tokens: number;
    cost: number;
    runs: number;
}

interface Props {
    rows: Row[];
}

export default function LeaderboardTable({
    rows,
}: Props) {
    return (
        <div className="overflow-hidden rounded-xl border border-border bg-card shadow-sm">
            <table className="w-full">
                <thead className="border-b border-border bg-card-hover">
                    <tr className="text-left text-sm text-secondary">
                        <th className="px-6 py-4">Rank</th>
                        <th>Model</th>
                        <th>Accuracy</th>
                        <th>Cost</th>
                        <th>Avg Time</th>
                        <th>Tokens</th>
                        <th>Runs</th>
                    </tr>
                </thead>

                <tbody>
                    {rows.map((row, index) => (
                        <tr
                            key={row.model}
                            className="border-b border-border hover:bg-card-hover"
                        >
                            <td className="px-6 py-5 font-semibold">
                                {index === 0
                                    ? "🥇"
                                    : index === 1
                                    ? "🥈"
                                    : index === 2
                                    ? "🥉"
                                    : index + 1}
                            </td>

                            <td>{row.model}</td>

                            <td className="font-medium text-green-600">
                                {(row.accuracy * 100).toFixed(1)}%
                            </td>

                            <td>${row.cost.toFixed(4)}</td>

                            <td>
                                {(row.latency_ms / 1000).toFixed(2)} s
                            </td>

                            <td>{row.tokens.toLocaleString()}</td>

                            <td>{row.runs}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}