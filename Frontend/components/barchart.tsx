"use client";

import { BarChart, Bar, Cell, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';





export function NetChart({val1,val2}) {
  const COLORS = ['#8884d8', '#e84118'];
  const data = [
    {
      name: 'Data Sent',
      'Data Sent': val1,
    },
    {
      name: 'Data Recieved',
      'Data Recieved':val2,
    }
    
  ];
  
  return (
    <ResponsiveContainer width="100%" height={200}>
    <BarChart width={500} height={200} data={data} dataKey="value">
    <Tooltip/>
      {data.map((entry, index) => (
        <Bar key={entry.name} dataKey={entry.name} fill={COLORS[index]} />
      ))}     <Legend />

    </BarChart>

  </ResponsiveContainer>
  );
}
