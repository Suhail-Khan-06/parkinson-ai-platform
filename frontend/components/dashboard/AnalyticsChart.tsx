"use client";

import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid,
} from "recharts";

export default function AnalyticsChart({
  voice,
  spiral,
  datscan,
}: {
  voice: number;
  spiral: number;
  datscan: number;
}) {
  const data = [
    {
      name: "Voice",
      confidence: voice,
    },
    {
      name: "Spiral",
      confidence: spiral,
    },
    {
      name: "DATScan",
      confidence: datscan,
    },
  ];

  return (
    <div className="rounded-3xl border border-white/10 bg-white/5 p-6 backdrop-blur-xl">
      <h3 className="mb-6 text-lg font-semibold text-white">
        AI Confidence Analytics
      </h3>

      {/* min-w-0 fixes ResponsiveContainer width=-1 warning */}
      <div className="w-full min-w-0 h-[300px]">
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={data}>
            <CartesianGrid
              strokeDasharray="3 3"
              stroke="rgba(255,255,255,0.08)"
            />

            <XAxis
              dataKey="name"
              stroke="#94a3b8"
              tick={{ fill: "#94a3b8" }}
              axisLine={{ stroke: "rgba(255,255,255,0.1)" }}
              tickLine={{ stroke: "rgba(255,255,255,0.1)" }}
            />

            <YAxis
              domain={[0, 100]}
              stroke="#94a3b8"
              tick={{ fill: "#94a3b8" }}
              axisLine={{ stroke: "rgba(255,255,255,0.1)" }}
              tickLine={{ stroke: "rgba(255,255,255,0.1)" }}
            />

            <Tooltip
              formatter={(value) => [
                `${Number(value ?? 0).toFixed(1)}%`,
                "Confidence",
              ]}
              contentStyle={{
                backgroundColor: "#0f172a",
                border: "1px solid rgba(255,255,255,0.1)",
                borderRadius: "12px",
                color: "#ffffff",
              }}
              labelStyle={{
                color: "#ffffff",
              }}
            />

            <Bar
              dataKey="confidence"
              fill="#06b6d4"
              radius={[10, 10, 0, 0]}
            />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}
