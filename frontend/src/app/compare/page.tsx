"use client";

import { useEffect, useState } from "react";

import { api } from "@/lib/api";

import PageHeader from "@/components/ui/PageHeader";
import CompareToolbar from "@/components/compare/CompareToolbar";
import CompareSummary from "@/components/compare/CompareSummary";
import ComparisonTable from "@/components/compare/ComparisonTable";

export default function ComparePage() {
    const [runs, setRuns] = useState<any[]>([]);
    const [compare, setCompare] = useState<any>(null);

    useEffect(() => {
        loadRuns();
    }, []);

    async function loadRuns() {
        const data = await api<any[]>("/api/experiments");
        setRuns(data);

        if (data.length >= 2) {
            compareRuns(data[0].id, data[1].id);
        }
    }

    async function compareRuns(a: string, b: string) {
        const data = await api<any>(
            `/api/compare?left=${a}&right=${b}`
        );

        setCompare(data);
    }

    return (
        <>
            <PageHeader
                title="Compare"
                description="Compare experiment performance side by side."
            />

            <CompareToolbar
                runs={runs}
                onCompare={compareRuns}
            />

            {compare && (
                <>
                    <CompareSummary data={compare.summary} />

                    <div className="mt-8">
                        <ComparisonTable
                            experimentA={compare.a}
                            experimentB={compare.b}
                        />
                    </div>
                </>
            )}
        </>
    );
}