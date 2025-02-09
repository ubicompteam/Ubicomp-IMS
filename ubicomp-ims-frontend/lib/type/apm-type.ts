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
  occurred_at: string
  restored_at: string
}

export enum Status {
  OCCURRED = "OCCURRED",
  INVESTIG = "INVESTIG",
  RESTORED = "RESTORED",
  RESOLVING = "RESOLVING",
}

export function timestampConverter(timestamp: string) : string {
  return timestamp.replaceAll("T", "").replaceAll("-", "").replaceAll(":", "")
}