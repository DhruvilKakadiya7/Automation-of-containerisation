"use client";

import { Line, LineChart, ResponsiveContainer, XAxis, YAxis } from "recharts";

const data1 = [
  {
    name: "8:00",
    total: Math.floor(Math.random() * 100),
    total2: Math.floor(Math.random() * 100),
    total3: Math.floor(Math.random() * 100),
    total4: Math.floor(Math.random() * 100),
  },
  {
    name: "8:01",
    total: Math.floor(Math.random() * 100),
    total2: Math.floor(Math.random() * 100),
    total3: Math.floor(Math.random() * 100),
    total4: Math.floor(Math.random() * 100),
  },
  {
    name: "8:02",
    total: Math.floor(Math.random() * 100),
    total2: Math.floor(Math.random() * 100),
    total3: Math.floor(Math.random() * 100),
    total4: Math.floor(Math.random() * 100),
  },
  {
    name: "8:03",
    total: Math.floor(Math.random() * 100),
    total2: Math.floor(Math.random() * 100),
    total3: Math.floor(Math.random() * 100),
    total4: Math.floor(Math.random() * 100),
  },
  {
    name: "8:04",
    total: Math.floor(Math.random() * 100),
    total2: Math.floor(Math.random() * 100),
    total3: Math.floor(Math.random() * 100),
    total4: Math.floor(Math.random() * 100),
  },
  {
    name: "8:05",
    total: Math.floor(Math.random() * 100),
    total2: Math.floor(Math.random() * 100),
    total3: Math.floor(Math.random() * 100),
    total4: Math.floor(Math.random() * 100),
  },
];

export function Overview() {
  return (
    <ResponsiveContainer width="100%" height={350}>
      <LineChart data={data1}>
        <XAxis
          dataKey="name"
          stroke="#888888"
          fontSize={12}
          tickLine={false}
          axisLine={false} />
        <YAxis
          stroke="#888888"
          fontSize={12}
          tickLine={false}
          axisLine={false}
          tickFormatter={(value: any) => `${value}%`} />
        <Line dataKey="total" fill="#adfa1d" radius={[4, 4, 0, 0]} />
        <Line dataKey="total2" fill="#fa1d66" radius={[4, 4, 0, 0]} />
        <Line dataKey="total3" fill="#1da9fa" radius={[4, 4, 0, 0]} />
        <Line dataKey="total4" fill="#fada1d" radius={[4, 4, 0, 0]} />
      </LineChart>
    </ResponsiveContainer>
  );
}