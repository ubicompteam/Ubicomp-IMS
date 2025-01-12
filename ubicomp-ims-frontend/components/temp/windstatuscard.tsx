import { Card, CardContent } from '@/components/ui/card'
import { Loader2 } from 'lucide-react'
import { CircleArrowUp } from 'lucide-react'
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from '@/components/ui/tooltip'
import { APMData } from '@/lib/types'

export default function WindStatusCard({ data }: { data: APMData[] }) {
	const wind_deg = (data.length > 0 ? Math.round(data[data.length - 1].wind_direction) % 360 : 0).toString()
	return (
		<Card className="mr-3 mb-3">
			<CardContent>
				<div className='flex flex-col items-center p-4'>
					<div className='basis-1/3'>Wind</div>
					<div className='basis-1/3'>
					<TooltipProvider>
						<Tooltip>
							<TooltipTrigger>
								<div>{data.length > 0 ? <CircleArrowUp size={64} strokeWidth={0.5} className="size-max transition" style={{ rotate: wind_deg + "deg", transition: "all ease-in-out 3s" }} /> : <Loader2 className="mr-2 h-[20px] w-[20px] animate-spin" />}</div>
							</TooltipTrigger>
							<TooltipContent className='flex flex-col items-center'>
								<div>Wind Direction</div>
								<div>{data.length > 0 ? data[data.length - 1].wind_direction : <Loader2 className="mr-2 h-[20px] w-[20px] animate-spin" />}</div>
							</TooltipContent>
						</Tooltip>
					</TooltipProvider>
					</div>
					<div className='basis-1/3'>{data.length > 0 ? <div className='flex'>m/s</div> : <Loader2 className="mr-2 h-[20px] w-[20px] animate-spin" />}</div>
				</div>
			</CardContent>
		</Card>
	)
}