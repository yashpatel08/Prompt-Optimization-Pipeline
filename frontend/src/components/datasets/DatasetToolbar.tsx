"use client";

import { Plus, Search, Upload } from "lucide-react";
import { useState } from "react";

import Button from "@/components/ui/Button";

export default function DatasetToolbar() {
    const [search, setSearch] = useState("");

    return (
        <div className="mb-6 flex items-center justify-between gap-4">
            <div className="relative w-full max-w-md">
                <Search
                    size={18}
                    className="absolute left-3 top-1/2 -translate-y-1/2 text-muted"
                />

                <input
                    value={search}
                    onChange={(e) => setSearch(e.target.value)}
                    placeholder="Search datasets..."
                    className="h-11 w-full rounded-lg border border-border bg-card pl-10 pr-4 outline-none"
                />
            </div>

            <div className="flex gap-3">
                <Button variant="secondary">
                    <Upload size={18} />
                    Upload
                </Button>

                <Button>
                    <Plus size={18} />
                    Dataset
                </Button>
            </div>
        </div>
    );
}