export type Status = {
  serverStatus: boolean
  mobiusStatus: boolean
  dataStatus: boolean
  dashboardStatus: boolean
}

export type ErrorLog = {
  id: number
  timestamp: string
  incident_id: number
  service: string
  status: string
  message: string
}

export type Incident = {
  id: number
  status: string
  service: string
  detail: string
  occurredAt: string
  restoredAt: string
}

export function timestampConverter(timestamp: string) : string {
  return timestamp.replaceAll("T", "").replaceAll("-", "").replaceAll(":", "")
}