"use client";

import React from "react";

import AppNavbar from "@/components/global/AppNavbar";
import StatusCard from "@/components/apm/APMStatusCard";

import { ErrorLog, Incident } from "@/lib/type/apm-type";
import { ErrorLogListCard } from "@/components/apm/error-log-list-card";
import { IncidentListCard } from "@/components/apm/incident-list-card";
import { UptimeHistoryCard } from "@/components/apm/uptime-history-card";
import { fetchErrorLogsByPeriod, fetchIncidentsByPeriod } from "@/lib/api/apm-api";

export default function Home() {
  const [status, setStatus] = React.useState({
    uptime: "none",
    server: false,
    mobius: false,
    data: false,
    apmFE: false
  });

  const [incidents, setIncidents] = React.useState([] as Incident[]);
  const [errorLogs, setErrorLogs] = React.useState([] as ErrorLog[]);
  const [uptimeHistory, setUptimeHistory] = React.useState([] as Incident[]);

  React.useEffect(() => {
    updateStatus();
  }, []);

  React.useEffect(() => {
    updateIncidents();
    updateErrorLogs();
    updateUptimeHistory();
  }, [status]);

  async function updateIncidents() {
    const start_date = new Date(Date.now() - 1 * 24 * 60 * 60 * 1000).toISOString().substring(0, 19);
    const end_date = new Date().toISOString().substring(0, 19);

    const incidents = fetchIncidentsByPeriod(start_date, end_date)
    setIncidents(await incidents);
  }

  async function updateErrorLogs() {
    const start_date = new Date(Date.now() - 1 * 24 * 60 * 60 * 1000).toISOString().substring(0, 19);
    const end_date = new Date().toISOString().substring(0, 19);

    const error_logs = fetchErrorLogsByPeriod(start_date, end_date)
    setErrorLogs(await error_logs);
  }

  async function updateUptimeHistory() {
    const start_date = new Date(Date.now() - 80 * 24 * 60 * 60 * 1000).toISOString().substring(0, 19);
    const end_date = new Date().toISOString().substring(0, 19);

    const incidents = fetchIncidentsByPeriod(start_date, end_date)
    setUptimeHistory(await incidents);
  }

  function updateStatus() {
    const ws = new WebSocket(process.env.NEXT_PUBLIC_WS_URL + "");

    ws.onopen = () => {
      setStatus({
        uptime: "WebSocket connected",
        server: false,
        mobius: false,
        data: false,
        apmFE: false
      });
    }

    ws.onmessage = (message) => {
      const data = JSON.parse(message.data);
      const status = data.watchdog_status;

      setStatus({
        uptime: new Date().toISOString().substring(0, 19).replaceAll("T", " "),
        server: status.server_status,
        mobius: status.mobius_ping_status,
        data: status.mobius_interval_status,
        apmFE: status.dashboard_status
      });
    }

    ws.onclose = () => {
      setStatus({
        uptime: "WebSocket closed",
        server: false,
        mobius: false,
        data: false,
        apmFE: false
      });
    }

    ws.onerror = () => {
      setStatus({
        uptime: "WebSocket error",
        server: false,
        mobius: false,
        data: false,
        apmFE: false
      });
    }      
  }

  return (
    <div>
      <AppNavbar src="/apm/dashboard" item1="APM" item2="Dashboard" />
      <div className="grid grid-cols-8 gap-2 p-2">
        <div className="col-span-8 flex gap-2">
          <StatusCard title="Server" uptime={status.uptime} status={status.server} />
          <StatusCard title="Mobius" uptime={status.uptime} status={status.mobius} />
          <StatusCard title="Data" uptime={status.uptime} status={status.data} />
          <StatusCard title="APM FE" uptime={status.uptime} status={status.apmFE} />
        </div>
        <IncidentListCard className="col-span-3 flex flex-col" incidents={incidents} />
        <UptimeHistoryCard className="col-span-5 row-span-2" incidents={uptimeHistory} />
        <ErrorLogListCard className="col-span-3 flex flex-col" errorLog={errorLogs} />
      </div>
    </div>
  );
}
