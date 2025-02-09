import { Card, CardContent, CardHeader } from "@/components/ui/card";
import { ChartSpline, Database, HardDrive, Server } from "lucide-react";

export default function StatusCard({ title, uptime, status }: { title:string, uptime:string, status:boolean }) {
  return (
    <Card className={`${status ? "bg-[#369F53]" : "bg-red-500"} flex text-white w-full items-center`}>
      {
        title === "Server" ? <Server className="ml-6" size={52} /> : 
        title === "Mobius" ? <HardDrive className="ml-6" size={52} /> : 
        title === "Data" ? <Database className="ml-6" size={52} /> :
        title === "APM FE" ? <ChartSpline className="ml-6" size={52} /> : null
      }
      <div className="flex flex-col">
        <CardHeader className="text-2xl font-semibold pb-2">{title}</CardHeader>
        <CardContent>Last uptime : {uptime}</CardContent>
      </div>
    </Card>
  )
}
