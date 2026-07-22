"use client";

import { useState } from "react";

import Button from "@/components/ui/Button";

interface Run {
    id: string;
    name: string;
}

interface Props {
    runs: Run[];
    onCompare: (a: string, b: string) => void;
}

export default function CompareToolbar({
    runs,
    onCompare,
}: Props) {
    const [a, setA] = useState("");
    const [b, setB] = useState("");

    return (
        <div className="mb-8 flex flex-wrap items-end gap-4">
            <div>
                <label className="mb-2 block text-sm font-medium">
                    Experiment A
                </label>

                <select
                    value={a}
                    onChange={(e) => setA(e.target.value)}
                    className="h-11 w-64 rounded-lg border border-border bg-card px-4"
                >
                    <option value="">Select</option>

                    {runs.map((run) => (
                        <option
                            key={run.id}
                            value={run.id}
                        >
                            {run.name}
                        </option>
                    ))}
                </select>
            </div>

            <div>
                <label className="mb-2 block text-sm font-medium">
                    Experiment B
                </label>

                <select
                    value={b}
                    onChange={(e) => setB(e.target.value)}
                    className="h-11 w-64 rounded-lg border border-border bg-card px-4"
                >
                    <option value="">Select</option>

                    {runs.map((run) => (
                        <option
                            key={run.id}
                            value={run.id}
                        >
                            {run.name}
                        </option>
                    ))}
                </select>
            </div>

            <Button
                onClick={() => onCompare(a, b)}
                disabled={!a || !b}
            >
                Compare
            </Button>
        </div>
    );
}