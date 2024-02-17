"use client";

import { PieChart, Pie, Cell, Tooltip, Legend, Bar, BarChart, ResponsiveContainer, XAxis, YAxis } from "recharts";



const COLORS: string[] = ['#8884d8', '#82ca9d'];

export function Piechart({data,startAngle=0,
  endAngle=360,}) {
  
  return (
    <ResponsiveContainer width="100%" height={200}>
     <PieChart width={200} height={150}>
      <Pie
 startAngle={startAngle}
 endAngle={endAngle}
        data={data}
        cx="50%"
        cy="50%"
        innerRadius={50}
        outerRadius={80}
        dataKey="value"
        label
      >
        {data.map((entry, index) => (
          <Cell key={`cell-${index}`} fill={COLORS[index]} />
        ))}
      </Pie>
      <Tooltip />
      <Legend />
    </PieChart>
    </ResponsiveContainer>
  );
}
