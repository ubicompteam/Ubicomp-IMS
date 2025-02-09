import { ErrorLog, Incident } from "@/lib/type/apm-type";

export async function fetchErrorLogsByPeriod(from : string, to : string): Promise<ErrorLog[]> {
  try {

    const url = `${process.env.NEXT_PUBLIC_API_URL}/api/logs/period?start_date=${from}&end_date=${to}`;
    const response = await fetch(url);
    return response.json();

  } catch (error) {
    console.error("Error fetching error logs:", error);
    return [];
  }
}

export async function fetchIncidentsByPeriod(from : string, to : string): Promise<Incident[]> {
  try {

    const url = `${process.env.NEXT_PUBLIC_API_URL}/api/incident/period?start_date=${from}&end_date=${to}`;
    const response = await fetch(url);
    return response.json();

  } catch (error) {
    console.error("Error fetching uptime history:", error);
    return [];
  }
}

export async function updateIncident(incidentId: number, newStatus: string, newDetail: string, service: string): Promise<void> {
  try {
    const url = `${process.env.NEXT_PUBLIC_API_URL}/api/incident/update?incident_id=${incidentId}&status=${newStatus}&detail=${newDetail}&service=${service}`;
    const response = await fetch(url);
    return response.json();

  } catch (error) {
    console.error("Error updating incident:", error);
  }
}