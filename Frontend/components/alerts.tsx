"use client"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import {
    Select,
    SelectContent,
    SelectGroup,
    SelectItem,
    SelectLabel,
    SelectTrigger,
    SelectValue,
  } from "@/components/ui/select"
import { useState } from "react";




export function AccountForm({name,id}) {
  const [selectedMetric, setSelectedMetric] = useState("");
  const [threshold, setThreshold] = useState("");

  const handleSubmit = () => {
    const formData = new FormData();
    formData.append("metric", selectedMetric);
    formData.append("id", id);
    formData.append("name", name);   
    formData.append("threshold", threshold);
    console.log(selectedMetric)
    console.log(threshold)

    fetch("http://127.0.0.1:5001/api/alert", {
      method: "POST",
      mode: 'no-cors',
      body: formData,
    })



  }
 
  return (
    <div className="flex w-full items-center space-x-2">
        <Select value={selectedMetric}
          onValueChange={setSelectedMetric}>
      <SelectTrigger >
        <SelectValue placeholder="Select a metric" />
      </SelectTrigger>
      <SelectContent>
        <SelectGroup>
          <SelectLabel>select metric</SelectLabel>
          <SelectItem value="cpu_usage">CPU</SelectItem>
          <SelectItem value="MEMORY">MEMORY</SelectItem>
          <SelectItem value="INCOMING TRAFFIC">INCOMING TRAFFIC</SelectItem>
          <SelectItem value="OUTGOING TRAFFIC">OUTGOING TRAFFIC</SelectItem>
        </SelectGroup>
      </SelectContent>
    </Select>
      <Input value={threshold}
          onChange={(event) => setThreshold(event.target.value)} type="number" placeholder="threshold" />
      <Button onClick={handleSubmit} type="submit" className="min-w-max w-full w-10">Set Alert</Button>
    </div>
  )
}