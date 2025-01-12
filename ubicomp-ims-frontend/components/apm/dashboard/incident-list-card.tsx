import { Card, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Incident } from "@/lib/type/apm-type";
import { ScrollArea } from "@/components/ui/scroll-area";
import { APMStatusBadge } from "../apm-status-badge";
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
} from "@/components/ui/alert-dialog"
import { Separator } from "@/components/ui/separator";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"
import { Textarea } from "@/components/ui/textarea";



export function IncidentListCard({ className, incidents }: { className: string; incidents: Incident[] }) {
  return (
    <Card className={className}>
      <CardHeader className="flex flex-row items-center justify-between">
        <CardTitle className="text-xl">Incident</CardTitle>
        <CardDescription>total {incidents.length} incidents</CardDescription>
      </CardHeader>

      <Separator />

      <ScrollArea className="h-0 flex-grow overflow-y-auto">
        {incidents.map((incident) => (
          <AlertDialog key={incident.id}>
            <AlertDialogTrigger className="border-t hover:bg-gray-50 cursor-pointer w-full grid grid-cols-[2fr_2fr_4fr_1fr] gap-4 px-4 py-6 items-center">
              <div className="text-center">
                <APMStatusBadge variant={incident.status.toLowerCase() as "occurred" | "investigating" | "restored" | "resolving"}>
                  {incident.status.toUpperCase()}
                </APMStatusBadge>
              </div>
              <div className="truncate">{incident.service}</div>
              <div className="truncate text-left">{incident.detail}</div>
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

                  <span className="ml-1">{incident.occurredAt}</span>
                  <span className="ml-1">{incident.restoredAt}</span>

                  <span className="col-span-2 text-lg font-bold">Status</span>
                  <Select>
                    <SelectTrigger className="w-[180px]">
                      <SelectValue placeholder={incident.status} />
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
                    defaultValue={incident.detail}
                  />
                </AlertDialogDescription>
              </AlertDialogHeader>
              <AlertDialogFooter>
                <AlertDialogCancel>Cancel</AlertDialogCancel>
                <AlertDialogAction>Update</AlertDialogAction>
              </AlertDialogFooter>
            </AlertDialogContent>
          </AlertDialog>
        ))}
      </ScrollArea>
    </Card>
  );
}