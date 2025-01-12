"use client"

import { Button } from "@/components/ui/button"
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form"
import { Input } from "@/components/ui/input"
import { z } from "zod"
import { zodResolver } from "@hookform/resolvers/zod"
import { useForm } from "react-hook-form"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { Textarea } from "@/components/ui/textarea"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"



export function IncidentForm({ className, id }: { className: string, id: string }) {
  const formSchema = z.object({
    id: z.number(),
    status: z.number(),
    service: z.string().min(2).max(50),
    detail: z.string().min(2).max(50),
    occurredAt: z.string(),
    restoredAt: z.string(),
  })

  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      id: 0,
      status: 0,
      service: "",
      detail: "",
      occurredAt: "",
      restoredAt: "",
    },
  })

  function onSubmit(values: z.infer<typeof formSchema>) {
    console.log(values)
  }

  return (
    <div className={className}>
      <Form {...form}>
        <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
          <FormLabel className="py-8">ID</FormLabel>
          <div className="pb-4">{id}</div>

          <FormLabel>Service</FormLabel>
          <div className="pb-4">Mobius</div>

          <FormLabel>OccurredAt</FormLabel>
          <div className="pb-4">20250105235959</div>

          <FormLabel>RestoredAt</FormLabel>
          <div className="pb-4">20250105235959</div>

          <FormField
            control={form.control}
            name="status"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Status</FormLabel>
                <FormControl>
                  <Select>
                    <SelectTrigger className="w-[180px]">
                      <SelectValue placeholder="Status" />
                    </SelectTrigger>
                    <SelectContent>
                      <SelectItem value="201">Occurred</SelectItem>
                      <SelectItem value="202">Investigating</SelectItem>
                      <SelectItem value="203">Resolving</SelectItem>
                      <SelectItem value="204">Restored</SelectItem>
                    </SelectContent>
                  </Select>
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />
          <FormField
            control={form.control}
            name="detail"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Detail</FormLabel>
                <FormControl>
                  <Textarea
                    placeholder="Detail"
                    className="resize-none"
                    {...field}
                  />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />
          <Button type="submit">Update</Button>
        </form>
      </Form>

    </div>

  )
}
