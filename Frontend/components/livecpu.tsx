"use client";

import { useState,useEffect } from "react";
import { Line, LineChart, ResponsiveContainer, XAxis, YAxis ,Legend,Tooltip} from "recharts";


export function Livecpu({temp}) {
  const [data, setData] = useState([])

  function getTimeInHHMMSS() {
    const date = new Date();
    const hours = date.getHours().toString().padStart(2, '0');
    const minutes = date.getMinutes().toString().padStart(2, '0');
    const seconds = date.getSeconds().toString().padStart(2, '0');
  
    return `${hours}:${minutes}:${seconds}`;
  }
  
  useEffect(() => {
    let tempData = data
    tempData.push({name: "cpu_usage", cpu_usage: temp.cpu_usage, time: getTimeInHHMMSS()})
   setData([...tempData].slice(-20))

  }, [temp])

  return (
    <ResponsiveContainer width="100%" height={350}>
      <LineChart data={data.reverse()}>
        <XAxis
          dataKey="time"
          stroke="#888888"
          fontSize={12}
          tickLine={false}
          axisLine={false} />
        <YAxis
          stroke="#888888"
          fontSize={12}
          tickLine={false}
          axisLine={false}
          // domain={[0, 50]}
          tickFormatter={(value: any) => `${value}%`} />
        <Line isAnimationActive={false} dataKey="cpu_usage" fill="#adfa1d" radius={[4, 4, 0, 0]} />
        <Tooltip/>
      </LineChart>
    </ResponsiveContainer>
  );
}