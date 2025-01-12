"use client";

import { ErrorLog, Incident } from "@/lib/type/apm-type";
import { ErrorLogListCard } from "@/components/apm/dashboard/error-log-list-card";
import { IncidentListCard } from "@/components/apm/dashboard/incident-list-card";
import { UptimeHistoryCard } from "./uptime-history-card";

import React from "react";
import { StatusCard } from "./ui/status-card";

export default function APMDashboard() {
  const [status, setStatus] = React.useState({
    serverStatus: true,
    mobiusStatus: true,
    dataStatus: true,
    dashboardStatus: true
  });
  const [incidents, setIncidents] = React.useState([] as Incident[]);
  const [errorLogs, setErrorLogs] = React.useState([] as ErrorLog[]);

  React.useEffect(() => {
    const sample_error_logs = [
      {
        "id": 0,
        "timestamp": "2025-01-01T22:38:11",
        "incident_id": 1,
        "service": "Server",
        "status": "occurred",
        "message": "Server is down"
      },
      {
        "id": 1,
        "timestamp": "2025-01-01T22:38:11",
        "incident_id": 2,
        "service": "Mobius",
        "status": "investigating",
        "message": "Mobius is down"
      },
      {
        "id": 2,
        "timestamp": "2025-01-01T22:38:11",
        "incident_id": 3,
        "service": "Data",
        "status": "restored",
        "message": "Data is down"
      },
      {
        "id": 3,
        "timestamp": "2025-01-01T22:38:11",
        "incident_id": 4,
        "service": "Dashboard",
        "status": "resolving",
        "message": "Bot is down"
      },
      {
        "id": 4,
        "timestamp": "2025-01-01T22:38:11",
        "incident_id": 5,
        "service": "Server",
        "status": "occurred",
        "message": "Server asdfsafsafdsafdsafsadfsafdfdasfasfis down"
      }
    ]
    setErrorLogs(sample_error_logs);

    const sample_incidents = [
      {
        "id": 0,
        "status": "occurred",
        "service": "Server",
        "detail": "Server is down",
        "occurredAt": "2025-01-01T22:38:11",
        "restoredAt": "2025-01-01T22:38:11"
      },
      {
        "id": 1,
        "status": "investigating",
        "service": "Mobius",
        "detail": "Mobius is down",
        "occurredAt": "2025-01-01T22:38:11",
        "restoredAt": "2025-01-01T22:38:11"
      },
      {
        "id": 2,
        "status": "restored",
        "service": "Data",
        "detail": "Data is down",
        "occurredAt": "2025-01-01T22:38:11",
        "restoredAt": "2025-01-01T22:38:11"
      },
      {
        "id": 3,
        "status": "resolving",
        "service": "Dashboard",
        "detail": "Bot is down",
        "occurredAt": "2025-01-01T22:38:11",
        "restoredAt": "2025-01-01T22:38:11"
      },
      {
        "id": 4,
        "status": "occurred",
        "service": "Server",
        "detail": "Server iadsfadsasdfasdfsafasfdasffadsfs down",
        "occurredAt": "2025-01-01T22:38:11",
        "restoredAt": "2025-01-01T22:38:11"
      }
    ]
    setIncidents(sample_incidents);
  }, []);


  return (
    <div className="grid grid-cols-8 gap-2 p-4">
      <div className="col-span-8 flex gap-2">
        <StatusCard title="Server" uptime="2025-01-01 22:38:11" status={status} />
        <StatusCard title="Mobius" uptime="2025-01-01 22:38:11" status={status} />
        <StatusCard title="Data" uptime="2025-01-01 22:38:11" status={status} />
        <StatusCard title="APM FE" uptime="2025-01-01 22:38:11" status={status} />
      </div>
      <IncidentListCard className="col-span-3 flex flex-col" incidents={incidents} />
      <UptimeHistoryCard className="col-span-5 row-span-2" />
      <ErrorLogListCard className="col-span-3 flex flex-col" errorLog={errorLogs} />
    </div>
  );
}
