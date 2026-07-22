import {
    LayoutDashboard,
    FileCode2,
    Database,
    FlaskConical,
    Trophy,
    FileText,
    GitCompareArrows,
    Settings,
} from "lucide-react";

import { NavigationItem } from "@/types/navigation";

export const navigation: NavigationItem[] = [
    {
        title: "Dashboard",
        href: "/dashboard",
        icon: LayoutDashboard,
    },
    {
        title: "Prompts",
        href: "/prompts",
        icon: FileCode2,
    },
    {
        title: "Datasets",
        href: "/datasets",
        icon: Database,
    },
    {
        title: "Experiments",
        href: "/experiments",
        icon: FlaskConical,
    },
    {
        title: "Leaderboard",
        href: "/leaderboard",
        icon: Trophy,
    },
    {
        title: "Compare",
        href: "/compare",
        icon: GitCompareArrows,
    },
];