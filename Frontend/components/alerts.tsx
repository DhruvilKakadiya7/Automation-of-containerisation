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


const languages = [
  { label: "English", value: "en" },
  { label: "French", value: "fr" },
  { label: "German", value: "de" },
  { label: "Spanish", value: "es" },
  { label: "Portuguese", value: "pt" },
  { label: "Russian", value: "ru" },
  { label: "Japanese", value: "ja" },
  { label: "Korean", value: "ko" },
  { label: "Chinese", value: "zh" },
] as const


export function AccountForm() {
 
  return (
    <div className="flex w-full items-center space-x-2">
        <Select>
      <SelectTrigger >
        <SelectValue placeholder="Select a fruit" />
      </SelectTrigger>
      <SelectContent>
        <SelectGroup>
          <SelectLabel>select metric</SelectLabel>
          <SelectItem value="CPU">CPU</SelectItem>
          <SelectItem value="MEMORY">MEMORY</SelectItem>
          <SelectItem value="INCOMING TRAFFIC">INCOMING TRAFFIC</SelectItem>
          <SelectItem value="OUTGOING TRAFFIC">OUTGOING TRAFFIC</SelectItem>
          <SelectItem value="pineapple">Pineapple</SelectItem>
        </SelectGroup>
      </SelectContent>
    </Select>
      <Input type="number" placeholder="threshold" />
      <Button type="submit" className="w-min-max">Set Alert</Button>
    </div>
  )
}