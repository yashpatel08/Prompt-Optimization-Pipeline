"use client";

import { useEffect, useState } from "react";

import { api } from "@/lib/api";

import PageHeader from "@/components/ui/PageHeader";
import ExperimentHistory from "@/components/experiments/ExperimentHistory";

export default function ExperimentsPage() {

    const [runs, setRuns] = useState([]);

    async function load() {
        const data = await api<any[]>("/api/experiments");
        setRuns(data);
    }

    useEffect(() => {
        load();

        const timer = setInterval(load, 2000);

        return () => clearInterval(timer);
    }, []);

    return (
        <>
            <PageHeader
                title="Experiments"
                description="Configure and execute prompt evaluation experiments."
            />

            <ExperimentHistory
                experiments={runs}
            />
        </>
    );
}