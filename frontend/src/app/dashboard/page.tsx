"use client";

import { useEffect, useState } from "react";

import { api } from "@/lib/api";

import PageHeader from "@/components/ui/PageHeader";

import StatsGrid from "@/components/dashboard/StatsGrid";
import AccuracyChart from "@/components/dashboard/AccuracyChart";
import RecentRuns from "@/components/dashboard/RecentRuns";
import LeaderboardPreview from "@/components/dashboard/LeaderboardPreview";

export default function DashboardPage() {
    const [dashboard, setDashboard] = useState<any>(null);
    const [loading, setLoading] = useState(true);

    async function loadDashboard() {
        try {
            const data = await api<any>("/api/dashboard");
            console.log("Data",data);
            setDashboard(data);
        } finally {
            setLoading(false);
        }
    }

    useEffect(() => {
        loadDashboard();
    }, []);

    useEffect(() => {
        if (!dashboard?.active_run) return;

        if (dashboard.active_run.status !== "running") return;

        const interval = setInterval(async () => {
            const status = await api<any>(
                `/api/experiments/${dashboard.active_run.run_id}/status`
            );

            setDashboard((prev: any) => ({
                ...prev,
                active_run: status,
            }));

            if (status.status === "completed") {
                clearInterval(interval);

                loadDashboard();
            }
        }, 2000);

        return () => clearInterval(interval);
    }, [dashboard?.active_run?.run_id]);

    if (loading) {
        return <div>Loading...</div>;
    }

    return (
        <>
            <PageHeader
                title="Dashboard"
                description="Overview of PromptOps experiments and evaluations."
            />

            {dashboard?.active_run && (
                <div className="mb-6 rounded-lg border border-blue-200 bg-blue-50 p-4">
                    <div className="font-semibold">
                        Experiment Running
                    </div>

                    <div className="mt-2 text-sm">
                        Model: {dashboard.active_run.current_model ?? "-"}
                    </div>

                    <div className="text-sm">
                        Prompt: {dashboard.active_run.current_prompt ?? "-"}
                    </div>

                    <div className="text-sm">
                        Test Case: {dashboard.active_run.current_test_case ?? "-"}
                    </div>

                    <div className="mt-4 h-2 overflow-hidden rounded bg-gray-200">
                        <div
                            className="h-full bg-blue-600 transition-all"
                            style={{
                                width: `${dashboard.active_run.progress}%`,
                            }}
                        />
                    </div>

                    <div className="mt-2 text-sm">
                        {dashboard.active_run.progress}%
                    </div>
                </div>
            )}

            <StatsGrid stats={dashboard?.stats} />

            <div className="mt-8 grid gap-6 xl:grid-cols-3">
                <div className="xl:col-span-2">
                    <AccuracyChart data={dashboard?.accuracy_trend} />
                </div>

                <RecentRuns runs={dashboard?.recent_runs} />
            </div>

            <div className="mt-8">
                <LeaderboardPreview data={dashboard?.leaderboard} />
            </div>
        </>
    );
}