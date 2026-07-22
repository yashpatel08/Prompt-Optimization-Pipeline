"use client";

import { useEffect, useState } from "react";

import { api } from "@/lib/api";

import PageHeader from "@/components/ui/PageHeader";
import DatasetToolbar from "@/components/datasets/DatasetToolbar";
import DatasetGrid from "@/components/datasets/DatasetGrid";

export default function DatasetsPage() {
    const [datasets, setDatasets] = useState([]);

    useEffect(() => {
        api("/api/datasets").then(setDatasets);
    }, []);

    return (
        <>
            <PageHeader
                title="Datasets"
                description="Manage evaluation datasets and test cases."
            />

            <DatasetToolbar />

            <DatasetGrid datasets={datasets} />
        </>
    );
}