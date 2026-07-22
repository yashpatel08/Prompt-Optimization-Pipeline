import {
    FlaskConical,
    Database,
    Trophy,
    DollarSign,
} from "lucide-react";

import StatsCard from "./StatsCard";

interface Props {
    stats: {
        experiments: number;
        datasets: number;
        models: number;
        prompts: number;
        runs: number;
        cost: number;
    };
}

export default function StatsGrid({ stats }: Props) {
    return (
        <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">
            <StatsCard
                title="Experiments"
                value={stats?.experiments.toString()}
                icon={<FlaskConical className="text-primary" />}
            />

            <StatsCard
                title="Datasets"
                value={stats?.datasets.toString()}
                icon={<Database className="text-primary" />}
            />

            <StatsCard
                title="Runs"
                value={stats?.runs.toString()}
                icon={<Trophy className="text-primary" />}
            />

            <StatsCard
                title="Cost"
                value={`$${stats?.cost.toFixed(4)}`}
                icon={<DollarSign className="text-primary" />}
            />
        </div>
    );
}