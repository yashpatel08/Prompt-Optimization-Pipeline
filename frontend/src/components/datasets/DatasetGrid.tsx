import DatasetCard from "./DatasetCard";

interface Dataset {
    id: string;
    name: string;
    filename: string;
    test_cases: number;
    size: number;
    updated_at: number;
}

interface Props {
    datasets: Dataset[];
}

export default function DatasetGrid({
    datasets,
}: Props) {
    return (
        <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-3">
            {datasets.map((dataset) => (
                <DatasetCard
                    key={dataset.id}
                    name={dataset.name}
                    testCases={dataset.test_cases}
                    updatedAt={new Date(
                        dataset.updated_at * 1000
                    ).toLocaleString()}
                />
            ))}
        </div>
    );
}