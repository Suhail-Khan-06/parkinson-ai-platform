"use client";

import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer
} from "recharts";

export default function AnalyticsChart({
  voice,
  spiral,
  datscan
}: {
  voice: number;
  spiral: number;
  datscan: number;
}) {

  const data = [
    {
      name: "Voice",
      confidence: voice
    },
    {
      name: "Spiral",
      confidence: spiral
    },
    {
      name: "DATScan",
      confidence: datscan
    }
  ];

  return (

    <div className="rounded-3xl border border-white/10 bg-white/5 p-6 backdrop-blur-xl">

      <h3 className="mb-6 text-lg font-semibold">
        AI Confidence Analytics
      </h3>

      <div className="h-[300px]">

        <ResponsiveContainer width="100%" height="100%">

          <BarChart data={data}>

            <XAxis dataKey="name" />

            <YAxis />

            <Tooltip />

            <Bar
              dataKey="confidence"
              radius={[10, 10, 0, 0]}
            />

          </BarChart>

        </ResponsiveContainer>

      </div>

    </div>
  );
}