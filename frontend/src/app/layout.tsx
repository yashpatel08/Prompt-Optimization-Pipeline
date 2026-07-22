import "./globals.css";
import type { Metadata } from "next";
import AppLayout from "@/components/layout/AppLayout";

export const metadata: Metadata = {
  title: "PromptOps",
  description: "Prompt Experiment Platform",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>
        <AppLayout>{children}</AppLayout>
      </body>
    </html>
  );
}