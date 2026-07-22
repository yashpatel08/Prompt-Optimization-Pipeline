import Card from "@/components/ui/Card";

interface Props {
    data: {
        winner: string;
        improvement: number;
    };
}

export default function CompareSummary({
    data,
}: Props) {
    return (
        <Card>
            <div className="flex items-center justify-between">
                <div>
                    <p className="text-sm text-secondary">
                        Winner
                    </p>

                    <h2 className="mt-2 text-3xl font-bold">
                        🏆 {data.winner}
                    </h2>

                    <p className="mt-2 text-secondary">
                        Highest overall evaluation score.
                    </p>
                </div>

                <div className="text-right">
                    <div className="text-4xl font-bold text-primary">
                        +{(data.improvement * 100).toFixed(2)}%
                    </div>

                    <div className="text-sm text-secondary">
                        Accuracy Improvement
                    </div>
                </div>
            </div>
        </Card>
    );
}