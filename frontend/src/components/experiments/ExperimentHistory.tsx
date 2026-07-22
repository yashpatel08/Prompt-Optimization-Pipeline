import Button from "@/components/ui/Button";
import {
    CheckCircle2,
    Clock3,
    XCircle,
    Eye,
    Copy,
} from "lucide-react";

interface Experiment {
    id: string;
    name: string;
    status: string;
    created_at: string;
    experiments: number;
    progress?: number;
    current_model?: string;
    current_prompt?: string;
    current_test_case?: string;
    accuracy?: number;
    cost?: number;
}

interface Props {
    experiments: Experiment[];
}

export default function ExperimentHistory({
    experiments,
}: Props) {
    function formatStatus(status: string) {
        return status.toLowerCase();
    }

    function formatDate(date: string) {
        if (!date) return "-";

        return new Date(date).toLocaleString();
    }

    return (
        <div className="rounded-xl border border-border bg-card shadow-sm">
            <div className="border-b border-border px-6 py-5">
                <h2 className="text-lg font-semibold">
                    Recent Experiments
                </h2>

                <p className="mt-1 text-sm text-secondary">
                    Recently executed experiment runs
                </p>
            </div>

            <div>
                {experiments.length === 0 && (
                    <div className="p-10 text-center text-secondary">
                        No experiment runs yet.
                    </div>
                )}

                {experiments.map((exp) => {
                    const status = formatStatus(exp.status);

                    return (
                        <div
                            key={exp.id}
                            className="border-b border-border p-6 last:border-b-0"
                        >
                            <div className="flex items-start justify-between gap-6">
                                <div className="flex-1">
                                    <h3 className="font-semibold">
                                        {exp.name}
                                    </h3>

                                    <p className="mt-1 text-sm text-secondary">
                                        {exp.current_prompt ??
                                            "Completed Run"}
                                    </p>

                                    <p className="mt-1 text-sm text-muted">
                                        {exp.current_model ??
                                            `${exp.experiments} Experiments`}
                                    </p>
                                </div>

                                {status === "completed" && (
                                    <span className="flex items-center gap-1 rounded-full bg-green-100 px-3 py-1 text-xs font-medium text-green-700">
                                        <CheckCircle2 size={14} />
                                        Completed
                                    </span>
                                )}

                                {status === "running" && (
                                    <span className="flex items-center gap-1 rounded-full bg-yellow-100 px-3 py-1 text-xs font-medium text-yellow-700">
                                        <Clock3 size={14} />
                                        Running
                                    </span>
                                )}

                                {status === "failed" && (
                                    <span className="flex items-center gap-1 rounded-full bg-red-100 px-3 py-1 text-xs font-medium text-red-700">
                                        <XCircle size={14} />
                                        Failed
                                    </span>
                                )}
                            </div>

                            {status === "running" && (
                                <div className="mt-5">
                                    <div className="mb-2 flex items-center justify-between text-xs text-secondary">
                                        <span>
                                            {exp.current_test_case ??
                                                "Preparing..."}
                                        </span>

                                        <span>
                                            {exp.progress ?? 0}%
                                        </span>
                                    </div>

                                    <div className="h-2 overflow-hidden rounded-full bg-muted">
                                        <div
                                            className="h-full bg-primary transition-all duration-300"
                                            style={{
                                                width: `${exp.progress ?? 0}%`,
                                            }}
                                        />
                                    </div>
                                </div>
                            )}

                            <div className="mt-5 flex items-center justify-between">
                                <div className="space-y-1">
                                    <p className="text-sm">
                                        <span className="text-secondary">
                                            Accuracy:
                                        </span>{" "}
                                        {exp.accuracy != null
                                            ? `${(
                                                  exp.accuracy * 100
                                              ).toFixed(1)}%`
                                            : "--"}
                                    </p>

                                    <p className="text-sm">
                                        <span className="text-secondary">
                                            Cost:
                                        </span>{" "}
                                        $
                                        {(exp.cost ?? 0).toFixed(
                                            6
                                        )}
                                    </p>

                                    <p className="text-xs text-muted">
                                        {formatDate(exp.created_at)}
                                    </p>
                                </div>

                                <div className="flex gap-2">
                                    <Button variant="secondary">
                                        <Eye size={16} />
                                        View
                                    </Button>

                                    <Button variant="secondary">
                                        <Copy size={16} />
                                        Clone
                                    </Button>
                                </div>
                            </div>
                        </div>
                    );
                })}
            </div>
        </div>
    );
}