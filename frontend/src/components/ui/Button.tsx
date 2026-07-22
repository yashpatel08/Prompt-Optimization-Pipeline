import { ButtonHTMLAttributes, ReactNode } from "react";
import { cn } from "@/lib/utils";

type Variant = "primary" | "secondary" | "ghost" | "danger";

interface Props extends ButtonHTMLAttributes<HTMLButtonElement> {
    children: ReactNode;
    variant?: Variant;
}

const variants: Record<Variant, string> = {
    primary:
        "bg-primary text-white hover:bg-primary-hover",

    secondary:
        "border border-border bg-card hover:bg-card-hover text-foreground",

    ghost:
        "hover:bg-card-hover text-secondary",

    danger:
        "bg-danger text-white hover:opacity-90",
};

export default function Button({
    children,
    variant = "primary",
    className,
    ...props
}: Props) {
    return (
        <button
            className={cn(
                "inline-flex items-center justify-center gap-2 rounded-lg px-5 py-2.5 text-sm font-medium transition-all disabled:opacity-50 disabled:pointer-events-none",
                variants[variant],
                className
            )}
            {...props}
        >
            {children}
        </button>
    );
}