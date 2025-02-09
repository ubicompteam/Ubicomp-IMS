"use client";

import { Card, CardContent, CardHeader } from "@/components/ui/card";
import { Separator } from "@/components/ui/separator";
import { Incident } from "@/lib/type/apm-type";
import React from "react";
import { useEffect } from "react";

export function UptimeHistoryCard({ className, incidents }: { className: string, incidents: Incident[] }) {
  
  React.useEffect(() => {
    
  }, [incidents]);

  const [serverUptime, setServerUptime] = React.useState([] as boolean[]);
  const [mobiusUptime, setMobiusUptime] = React.useState([] as boolean[]);
  const [dataUptime, setDataUptime] = React.useState([] as boolean[]);
  const [botUptime, setBotUptime] = React.useState([] as boolean[]);
  
  return (
    <Card className={className}>
      <CardHeader className="text-xl font-bold">Uptime History</CardHeader>
      <Separator />
      <CardHeader className="text-lg font-semibold pb-1">Server</CardHeader>
      <CardContent className="flex justify-between">
        {Array.from({ length: 80 }).map((_, index) => (
          <div
            key={index}
            className="h-10 w-2 bg-[#369F53]"
          ></div>
        ))}
      </CardContent>
      <CardContent className="flex items-center gap-4">
        <div>80 Days ago</div>
        <div className="flex-grow border-t border-gray-400"></div>
        <div>100% uptime</div>
        <div className="flex-grow border-t border-gray-400"></div>
        <div>Today</div>
      </CardContent>
      <Separator />
      <CardHeader className="text-lg font-semibold">Mobius</CardHeader>
      <CardContent className="flex justify-between">
        {Array.from({ length: 80 }).map((_, index) => (
          <div
            key={index}
            className="h-10 w-2 bg-[#369F53]"
          ></div>
        ))}
      </CardContent>
      <CardContent className="flex items-center gap-4">
        <div>80 Days ago</div>
        <div className="flex-grow border-t border-gray-400"></div>
        <div>100% uptime</div>
        <div className="flex-grow border-t border-gray-400"></div>
        <div>Today</div>
      </CardContent>
      <Separator />
      <CardHeader className="text-lg font-semibold">Data</CardHeader>
      <CardContent className="flex justify-between">
        {Array.from({ length: 80 }).map((_, index) => (
          <div
            key={index}
            className="h-10 w-2 bg-[#369F53]"
          ></div>
        ))}
      </CardContent>
      <CardContent className="flex items-center gap-4">
        <div>80 Days ago</div>
        <div className="flex-grow border-t border-gray-400"></div>
        <div>100% uptime</div>
        <div className="flex-grow border-t border-gray-400"></div>
        <div>Today</div>
      </CardContent>
      <Separator />
      <CardHeader className="text-lg font-semibold">Bot</CardHeader>
      <CardContent className="flex justify-between">
        {Array.from({ length: 80 }).map((_, index) => (
          <div
            key={index}
            className="h-10 w-2 bg-[#369F53]"
          ></div>
        ))}
      </CardContent>
      <CardContent className="flex items-center gap-4">
        <div>80 Days ago</div>
        <div className="flex-grow border-t border-gray-400"></div>
        <div>100% uptime</div>
        <div className="flex-grow border-t border-gray-400"></div>
        <div>Today</div>
      </CardContent>
    </Card>
  )
}
