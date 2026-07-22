import { ReactNode } from "react";
import { cn } from "@/lib/utils";

interface Props {
    children: ReactNode;
    color?: "blue" | "green" | "yellow" | "red";
}

const colors = {
    blue: "bg-primary-soft text-primary",

    green:
        "bg-green-50 text-green-700",

    yellow:
        "bg-yellow-50 text-yellow-700",

    red:
        "bg-red-50 text-red-700",
};

export default function Badge({
    children,
    color = "blue",
}: Props) {
    return (
        <span
            className={cn(
                "rounded-full px-3 py-1 text-xs font-medium",
                colors[color]
            )}
        >
            {children}
        </span>
    );
}