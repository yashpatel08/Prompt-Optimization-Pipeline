"use client";

import { ReactNode } from "react";
import Navbar from "./Navbar";
import Sidebar from "./Sidebar";

interface Props {
    children: ReactNode;
}

export default function AppLayout({ children }: Props) {
    return (
        <div className="flex h-screen bg-background text-foreground">
            <Sidebar />

            <div className="flex min-w-0 flex-1 flex-col">
                {/* <Navbar /> */}

                <main className="flex-1 overflow-y-auto px-8 py-4">
                    {children}
                </main>
            </div>
        </div>
    );
}