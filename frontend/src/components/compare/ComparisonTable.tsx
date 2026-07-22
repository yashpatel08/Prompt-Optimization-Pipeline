interface Experiment {
    model: string;
    accuracy: number;
    cost: number;
    latency_ms: number;
    prompt_tokens: number;
    completion_tokens: number;
    failed: number;
}

interface Props {
    experimentA: Experiment;
    experimentB: Experiment;
}

export default function ComparisonTable({
    experimentA,
    experimentB,
}: Props) {
    const rows = [
        [
            "Accuracy",
            `${(experimentA.accuracy * 100).toFixed(2)}%`,
            `${(experimentB.accuracy * 100).toFixed(2)}%`,
        ],
        [
            "Cost",
            `$${experimentA.cost.toFixed(4)}`,
            `$${experimentB.cost.toFixed(4)}`,
        ],
        [
            "Latency",
            `${experimentA.latency_ms.toFixed(0)} ms`,
            `${experimentB.latency_ms.toFixed(0)} ms`,
        ],
        [
            "Input Tokens",
            experimentA.prompt_tokens.toLocaleString(),
            experimentB.prompt_tokens.toLocaleString(),
        ],
        [
            "Output Tokens",
            experimentA.completion_tokens.toLocaleString(),
            experimentB.completion_tokens.toLocaleString(),
        ],
        [
            "Failures",
            experimentA.failed,
            experimentB.failed,
        ],
    ];

    return (
        <div className="overflow-hidden rounded-xl border border-border bg-card">
            <table className="w-full">
                <thead className="border-b border-border bg-card-hover">
                    <tr>
                        <th className="px-6 py-4 text-left">
                            Metric
                        </th>

                        <th>{experimentA.model}</th>

                        <th>{experimentB.model}</th>
                    </tr>
                </thead>

                <tbody>
                    {rows.map((row) => (
                        <tr
                            key={row[0]}
                            className="border-b border-border"
                        >
                            <td className="px-6 py-4 font-medium">
                                {row[0]}
                            </td>

                            <td>{row[1]}</td>

                            <td>{row[2]}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}