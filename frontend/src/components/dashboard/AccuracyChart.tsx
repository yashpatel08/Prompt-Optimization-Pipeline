"use client";

import {
    ResponsiveContainer,
    AreaChart,
    Area,
    XAxis,
    Tooltip,
} from "recharts";

interface TrendPoint {
    run: string;
    model: string;
    prompt: string;
    accuracy: number;
    latency_ms: number;
    tokens: number;
}

interface Props {
    data: TrendPoint[];
}

export default function AccuracyChart({ data }: Props) {
    return (
        <div className="rounded-xl border border-border bg-card p-6 shadow-sm">
            <h3 className="mb-6 text-lg font-semibold">
                Accuracy Trend
            </h3>

            <ResponsiveContainer
                width="100%"
                height={260}
            >
                <AreaChart data={data}>
                    <XAxis dataKey="run" />

                    <Tooltip
                        formatter={(value) => {
                            const accuracy = Number(value ?? 0);
                            return `${(accuracy * 100).toFixed(1)}%`;
                        }}
                    />

                    <Area
                        dataKey="accuracy"
                        stroke="#2563eb"
                        fill="#dbeafe"
                    />
                </AreaChart>
            </ResponsiveContainer>
        </div>
    );
}