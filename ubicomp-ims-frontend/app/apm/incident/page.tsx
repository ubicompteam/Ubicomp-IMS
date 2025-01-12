"use client";

import { AppNavbar } from "@/components/global/navbar";
import APMDashboard from "@/components/apm/dashboard/apm-dashboard";

import React from "react";

export default function Home() {
  return (
    <div>
      <AppNavbar src="/apm/dashboard" item1="APM" item2="Incident" />
    </div>
  );
}
