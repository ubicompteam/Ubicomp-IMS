"use client";

import * as React from "react";
import { Calendar } from "@/components/ui/calendar"
import { Card } from "./ui/card";


export function ErrorReports() {
  const [date, setDate] = React.useState<Date | undefined>(new Date())

  return (
    <div className="flex">
      <Calendar
        mode="single"
        selected={date}
        onSelect={setDate}
        className="rounded-md border"
      />
      <Card>
        hello
      </Card>
    </div>
  );
}