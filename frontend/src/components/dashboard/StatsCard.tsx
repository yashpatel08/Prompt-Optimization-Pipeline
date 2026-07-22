import { ReactNode } from "react";

interface Props {
    title: string;
    value: string;
    icon: ReactNode;
    change?: string;
}

export default function StatsCard({
    title,
    value,
    icon,
    change,
}: Props) {
    return (
        <div className="rounded-xl border border-border bg-card p-6 shadow-sm transition hover:shadow">
            <div className="flex items-start justify-between">
                <div>
                    <p className="text-sm text-secondary">
                        {title}
                    </p>

                    <h2 className="mt-3 text-3xl font-bold">
                        {value}
                    </h2>

                    {change && (
                        <p className="mt-3 text-sm text-success">
                            {change}
                        </p>
                    )}
                </div>

                <div className="rounded-lg bg-primary-soft p-3">
                    {icon}
                </div>
            </div>
        </div>
    );
}