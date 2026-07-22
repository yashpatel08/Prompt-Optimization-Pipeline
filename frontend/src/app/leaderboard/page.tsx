"use client";

import { useEffect, useState } from "react";

import { api } from "@/lib/api";

import PageHeader from "@/components/ui/PageHeader";
import LeaderboardToolbar from "@/components/leaderboard/LeaderboardToolbar";
import LeaderboardTable from "@/components/leaderboard/LeaderboardTable";

export default function LeaderboardPage() {
    const [rows, setRows] = useState([]);

    useEffect(() => {
        api("/api/leaderboard").then(setRows);
    }, []);

    return (
        <>
            <PageHeader
                title="Leaderboard"
                description="Compare model performance across all experiment runs."
            />

            <LeaderboardToolbar />

            <LeaderboardTable rows={rows} />
        </>
    );
}