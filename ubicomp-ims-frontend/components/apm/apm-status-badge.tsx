import * as React from "react"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const badgeVariants = cva(
  "inline-flex items-center rounded-md border px-2.5 py-0.5 text-xs font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2",
  {
    variants: {
      variant: {
        default:
          "border-transparent bg-primary text-primary-foreground shadow hover:bg-primary/80",
        occurred:
          "border-transparent bg-red-500 text-primary-foreground shadow hover:bg-red-500/80",
        investigating:
          "border-transparent bg-yellow-500 text-primary-foreground shadow hover:bg-yellow-500/80",
        resolving:
          "border-transparent bg-orange-500 text-primary-foreground shadow hover:bg-orange-500/80",
        restored:
          "border-transparent bg-[#369F53] text-primary-foreground shadow hover:bg-[#369F53]/80",
      },
    },
    defaultVariants: {
      variant: "default",
    },
  }
)

export interface BadgeProps
  extends React.HTMLAttributes<HTMLDivElement>,
    VariantProps<typeof badgeVariants> {}

function APMStatusBadge({ className, variant, ...props }: BadgeProps) {
  return (
    <div className={cn(badgeVariants({ variant }), className)} {...props} />
  )
}

export { APMStatusBadge, badgeVariants }
