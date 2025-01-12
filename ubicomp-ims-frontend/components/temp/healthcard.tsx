import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { CircleAlert, CircleCheck, Loader2 } from "lucide-react";

export default function HealthCard({ health , currentTime, lastCheckTime, nextCheckTime } : { health: boolean, currentTime: string, lastCheckTime: string, nextCheckTime: string }) {
  return (
    <Card className="min-w-[340px] h-[166px] mr-3 mb-3">
      <CardHeader>
        <CardTitle className="flex items-center">
          {health ? <CircleCheck className="h-8 w-8 mr-3" color="green" /> : <CircleAlert className="h-8 w-8 mr-3" color="red" />}
          {health ? "System is All Good!" : "System is Down!"}
        </CardTitle>
      </CardHeader>
      <CardContent className="flex">
        <div>
          <CardDescription>Current Time</CardDescription>
          <CardDescription>Last Check Time</CardDescription>
          <CardDescription>Next Check Time</CardDescription>
        </div>
        <div>
          <CardDescription className="px-3">:</CardDescription>
          <CardDescription className="px-3">:</CardDescription>
          <CardDescription className="px-3">:</CardDescription>
        </div>
        <div>
          <CardDescription>{currentTime == "" ? <Loader2 className="mr-2 h-[20px] w-[20px] animate-spin" /> : currentTime}</CardDescription>
          <CardDescription>{lastCheckTime == "" ? <Loader2 className="mr-2 h-[20px] w-[20px] animate-spin" /> : lastCheckTime}</CardDescription>
          <CardDescription>{nextCheckTime == "" ? <Loader2 className="mr-2 h-[20px] w-[20px] animate-spin" /> : nextCheckTime}</CardDescription>
        </div>
      </CardContent>
    </Card>
  )
}