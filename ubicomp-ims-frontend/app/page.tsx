"use client";

import { AppNavbar } from "@/components/global/navbar";
import APMDashboard from "@/components/apm/dashboard/apm-dashboard";

import React from "react";

export default function Home() {
  return (
    <div>
      <AppNavbar src="/" item1="Overview" item2="Dashboard" />
    </div>
  );
}
