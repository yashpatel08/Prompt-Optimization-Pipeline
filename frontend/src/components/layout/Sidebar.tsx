"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

import { navigation } from "@/constants/navigation";
import { cn } from "@/lib/utils";

export default function Sidebar() {
    const pathname = usePathname();

    return (
        <aside className="flex h-screen w-72 flex-col border-r border-border bg-sidebar">
            <div className="border-b border-border-light px-7 py-4">
                <h1 className="text-2xl font-bold tracking-tight text-foreground">
                    Prompt
                    <span className="text-blue-600">Ops</span>
                </h1>

                <p className="mt-1 text-sm text-secondary">
                    Prompt Experiment Platform
                </p>
            </div>

            {/* Navigation */}
            <nav className="flex-1 space-y-1 p-4">
                {navigation.map((item) => {
                    const Icon = item.icon;

                    const active = pathname === item.href;

                    return (
                        <Link
                            key={item.href}
                            href={item.href}
                            className={cn(
                                "group flex items-center gap-3 rounded-xl px-4 py-3 text-sm font-medium transition-all duration-200",

                                active
                                    ? "bg-primary-soft text-primary"
                                    : "text-secondary hover:bg-card-hover hover:text-foreground"
                            )}
                        >
                            <Icon
                                size={19}
                                className={cn(
                                    "transition-colors",
                                    active
                                        ? "text-blue-600"
                                        : "text-gray-400 group-hover:text-gray-700"
                                )}
                            />

                            <span>{item.title}</span>
                        </Link>
                    );
                })}
            </nav>

            <div className="border-t border-gray-100 p-5">
                <div className="rounded-xl bg-gray-50 p-4">
                    <p className="text-sm font-semibold text-gray-800">
                        PromptOps
                    </p>

                    <p className="mt-1 text-xs text-gray-500">
                        AI Prompt Evaluation Platform
                    </p>
                </div>
            </div>
        </aside>
    );
}