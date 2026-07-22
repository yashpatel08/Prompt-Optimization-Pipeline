import Input from "@/components/ui/Input";

export default function LeaderboardToolbar() {
    return (
        <div className="mb-6 flex items-center justify-between gap-4">
            <div className="w-full max-w-sm">
                <Input placeholder="Search model..." />
            </div>

            <select className="h-11 rounded-lg border border-border bg-card px-4">
                <option>Last 7 Days</option>
                <option>Last 30 Days</option>
                <option>Last 90 Days</option>
                <option>All Time</option>
            </select>
        </div>
    );
}