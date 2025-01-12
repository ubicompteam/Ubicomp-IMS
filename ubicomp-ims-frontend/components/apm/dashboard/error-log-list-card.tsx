import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { ErrorLog, timestampConverter } from "@/lib/type/apm-type";
import { Separator } from "@/components/ui/separator";
import { ScrollArea } from "@/components/ui/scroll-area";
import { APMStatusBadge } from "../apm-status-badge";
import { HoverCard, HoverCardContent, HoverCardTrigger } from "../../ui/hover-card";

export function ErrorLogListCard({ className, errorLog }: { className: string; errorLog: ErrorLog[] }) {
  return (
    <Card className={className}>
      <CardHeader className="flex flex-row items-center justify-between">
        <CardTitle className="text-xl">Error Log</CardTitle>
        <CardDescription>total {errorLog.length} logs in last 24h</CardDescription>
      </CardHeader>

      <Separator />
      
      <ScrollArea className="h-0 flex-grow overflow-y-auto">
        {errorLog.map((log) => (
          <HoverCard key={log.id}>
            <HoverCardTrigger>
              <CardContent
                className="grid grid-cols-[2fr_2fr_3fr_2fr] gap-4 px-4 py-6 items-center text-center border-t hover:bg-gray-50"
              >
                <div>
                  <APMStatusBadge variant={log.status}>{log.status.toUpperCase()}</APMStatusBadge>
                </div>
                <div className="truncate">{log.service}</div>
                <div className="truncate text-left">{log.message}</div>
                <div className="truncate text-xs text-gray ml-auto">{timestampConverter(log.timestamp)}</div>
              </CardContent>
            </HoverCardTrigger>
            <HoverCardContent className="w-full">
              <CardContent
                className="py-6"
              >
                <div className="grid grid-cols-[90px_1fr] gap-x-4 gap-y-2">
                  <div className="font-semibold">Status:</div>
                  <div>
                    <APMStatusBadge variant={log.status}>
                      {log.status.toUpperCase()}
                    </APMStatusBadge>
                  </div>
                  <div className="font-semibold">Service:</div>
                  <div>{log.service}</div>
                  <div className="font-semibold">Timestamp:</div>
                  <div>{timestampConverter(log.timestamp)}</div>
                  <div className="font-semibold">Incident ID:</div>
                  <div>{log.incident_id}</div>
                  <div className="font-semibold">Message:</div>
                  <div>{log.message}</div>
                </div>
              </CardContent>
            </HoverCardContent>
          </HoverCard>
        ))}
      </ScrollArea>
    </Card>
  );
}