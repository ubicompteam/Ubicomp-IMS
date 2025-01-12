import { IncidentForm } from "@/components/apm/incident/incident-form";
import { AppNavbar } from "@/components/global/navbar";
import React from "react";

export default function AboutPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = React.use(params); // `params`를 Promise에서 Unwrap
  return (
    <div>
      <AppNavbar src="/" item1="Dashboard" item2="Incident" />
      <IncidentForm className="m-4 p-4" id={id} />
    </div>)
    ;
}
