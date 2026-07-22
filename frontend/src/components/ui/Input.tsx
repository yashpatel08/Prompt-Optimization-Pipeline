import { InputHTMLAttributes } from "react";
import { cn } from "@/lib/utils";

export default function Input({
    className,
    ...props
}: InputHTMLAttributes<HTMLInputElement>) {
    return (
        <input
            className={cn(
                "h-11 w-full rounded-lg border border-border bg-card px-4 outline-none transition placeholder:text-muted focus:border-primary focus:ring-4 focus:ring-primary/10",
                className
            )}
            {...props}
        />
    );
}