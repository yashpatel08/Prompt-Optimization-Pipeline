import { ReactNode } from "react";

interface Props {
    title: string;
    description?: string;
    action?: ReactNode;
}

export default function PageHeader({
    title,
    description,
    action,
}: Props) {
    return (
        <div className="mb-8 flex items-center justify-between">
            <div>
                <h1 className="text-3xl font-bold text-foreground">
                    {title}
                </h1>

                {description && (
                    <p className="mt-2 text-secondary">
                        {description}
                    </p>
                )}
            </div>

            {action}
        </div>
    );
}