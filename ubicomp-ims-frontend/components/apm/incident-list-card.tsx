import { useState } from "react";
import { Card, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Incident } from "@/lib/type/apm-type";
import { ScrollArea } from "@/components/ui/scroll-area";
import { APMStatusBadge } from "./apm-status-badge";
import { SquarePen } from "lucide-react";
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from "@/components/ui/alert-dialog";
import { Separator } from "@/components/ui/separator";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Textarea } from "@/components/ui/textarea";
import { updateIncident } from "@/lib/api/apm-api";

export function IncidentListCard({ className, incidents }: { className: string; incidents: Incident[] }) {
  return (
    <Card className={className}>
      <CardHeader className="flex flex-row items-center justify-between">
        <CardTitle className="text-xl">Incident</CardTitle>
        <CardDescription>total {incidents.length} incidents</CardDescription>
      </CardHeader>

      <Separator />

      <ScrollArea className="h-0 flex-grow overflow-y-auto">
        {incidents.map((incident) => {
          const [status, setStatus] = useState(incident.status);
          const [detail, setDetail] = useState(incident.detail);

          return (
            <AlertDialog key={incident.id}>
              <AlertDialogTrigger className="border-t hover:bg-gray-50 cursor-pointer w-full grid grid-cols-[2fr_2fr_2fr_2fr_1fr] gap-4 px-4 py-6 items-center">
                <div className="text-center">
                  <APMStatusBadge variant={status.toLowerCase() as "occurred" | "investigating" | "restored" | "resolving"}>
                    {status.toUpperCase()}
                  </APMStatusBadge>
                </div>
                <div className="truncate text-left">{incident.service}</div>
                <div className="truncate text-left">{incident.occurred_at}</div>
                <div className="truncate text-left">{incident.restored_at}</div>
                <SquarePen size={18} color="gray" className="ml-auto mr-2" />
              </AlertDialogTrigger>
              <AlertDialogContent>
                <AlertDialogHeader>
                  <AlertDialogTitle className="text-xl mb-4">Edit Incident</AlertDialogTitle>
                  <Separator />
                  <AlertDialogDescription className="grid grid-cols-2 gap-y-4 pt-4">
                    <span className="text-lg font-bold">ID</span>
                    <span className="text-lg font-bold">Service</span>
                    <span className="ml-1">{incident.id}</span>
                    <span className="ml-1">{incident.service}</span>
                    <span className="text-lg font-bold">Occurred At</span>
                    <span className="text-lg font-bold">Restored At</span>
                    <span className="ml-1">{incident.occurred_at}</span>
                    <span className="ml-1">{incident.restored_at}</span>
                    <span className="col-span-2 text-lg font-bold">Status</span>
                    <Select onValueChange={setStatus} defaultValue={status}>
                      <SelectTrigger className="w-[180px]">
                        <SelectValue placeholder={status} />
                      </SelectTrigger>
                      <SelectContent>
                        <SelectItem value="occurred">occurred</SelectItem>
                        <SelectItem value="investigating">investigating</SelectItem>
                        <SelectItem value="resolving">resolving</SelectItem>
                        <SelectItem value="restored">restored</SelectItem>
                      </SelectContent>
                    </Select>
                    <span className="col-span-2 text-lg font-bold">Detail</span>
                    <Textarea
                      className="col-span-2 resize-none h-32"
                      value={detail}
                      onChange={(e) => setDetail(e.target.value)}
                    />
                  </AlertDialogDescription>
                </AlertDialogHeader>
                <AlertDialogFooter>
                  <AlertDialogCancel>Cancel</AlertDialogCancel>
                  <AlertDialogAction onClick={() => updateIncident(incident.id, status, detail, incident.service)}>
                    Update
                  </AlertDialogAction>
                </AlertDialogFooter>
              </AlertDialogContent>
            </AlertDialog>
          );
        })}
      </ScrollArea>
    </Card>
  );
}