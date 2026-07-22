"use client";

import { Bell, Play, Search } from "lucide-react";

export default function Navbar() {
    return (
        <header className="sticky top-0 z-50 flex h-18 items-center justify-between border-b border-border bg-card/90 px-8 backdrop-blur">
            <div>
                <h2 className="text-xl font-semibold text-foreground">
                    Dashboard
                </h2>

                <p className="mt-0.5 text-sm text-secondary">
                    Monitor experiments and prompt performance.
                </p>
            </div>

            <div className="relative hidden w-[380px] lg:block">
                <Search
                    size={18}
                    className="absolute left-4 top-1/2 -translate-y-1/2 text-muted"
                />

                <input
                    type="text"
                    placeholder="Search prompts, datasets..."
                    className="
            h-10
            w-full
            rounded-sm
            border
            border-border
            bg-background
            pl-11
            pr-4
            text-sm
            outline-none
            transition-all
            placeholder:text-muted
            focus:border-primary
            focus:ring-4
            focus:ring-primary/10
          "
                />
            </div>

            <div className="flex items-center gap-3">
                <button
                    className="
            flex
            h-8
            w-8
            items-center
            justify-center
            rounded-lg
            border
            border-border
            bg-card
            transition
            hover:bg-card-hover
          "
                >
                    <Bell
                        size={18}
                        className="text-secondary"
                    />
                </button>

                <button
                    className="
            flex
            h-11
            items-center
            gap-2
            rounded-md
            bg-primary
            px-3
            text-sm
            font-medium
            text-white
            transition
            hover:bg-primary-hover
          "
                >
                    <Play size={16} />

                    Run Experiment
                </button>

                <div
                    className="
            flex
            h-11
            w-11
            items-center
            justify-center
            rounded-full
            bg-primary
            font-semibold
            text-white
            shadow-sm
          "
                >
                    Y
                </div>
            </div>
        </header>
    );
}