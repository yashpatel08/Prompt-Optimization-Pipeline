"use client";

import { useEffect, useState } from "react";

import { api } from "@/lib/api";

import PageHeader from "@/components/ui/PageHeader";
import PromptToolbar from "@/components/prompts/PromptToolbar";
import PromptGrid from "@/components/prompts/PromptGrid";

export default function PromptsPage() {
    const [prompts, setPrompts] = useState([]);

    useEffect(() => {
        api("/api/prompts").then(setPrompts);
    }, []);

    return (
        <>
            <PageHeader
                title="Prompts"
                description="Manage and version your prompts."
            />

            <PromptToolbar />

            <PromptGrid prompts={prompts} />
        </>
    );
}