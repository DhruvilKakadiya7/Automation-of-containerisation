import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { Badge } from "@/components/ui/badge"
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
import { Button } from "@/components/ui/button"

export function RecentSales() {
  return (
    <div className="space-y-8">
      <div className="flex items-center">
      <Avatar className="h-9 w-9">
          <AvatarImage src="/avatars/04.png" alt="Avatar" />
          <AvatarFallback style = {{backgroundColor: 'red'}}>P1</AvatarFallback>
        </Avatar>
        <div className="ml-4 space-y-1">
        <AlertDialog>
      <AlertDialogTrigger asChild>
      <p className="text-sm font-medium leading-none">CPU Overload</p>
      </AlertDialogTrigger>
      <AlertDialogContent>
        <AlertDialogHeader>
          <AlertDialogTitle>CPU Overload</AlertDialogTitle>
          <AlertDialogDescription>
            Device CPU has been working at above 90% capacity for more than 30 seconds, causing harm to the system
          </AlertDialogDescription>
        </AlertDialogHeader>
        <AlertDialogFooter>
          <AlertDialogCancel>Close</AlertDialogCancel>
        </AlertDialogFooter>
      </AlertDialogContent>
    </AlertDialog>
        </div>
        <div className="ml-auto font-medium"><Badge>High</Badge></div>
      </div>
      <div className="flex items-center">
      <Avatar className="h-9 w-9">
          <AvatarImage src="/avatars/04.png" alt="Avatar" />
          <AvatarFallback style = {{backgroundColor: 'red'}}>P2</AvatarFallback>
        </Avatar>
        <div className="ml-4 space-y-1">
        <AlertDialog>
      <AlertDialogTrigger asChild>
      <p className="text-sm font-medium leading-none">High RAM Usage</p>
      </AlertDialogTrigger>
      <AlertDialogContent>
        <AlertDialogHeader>
          <AlertDialogTitle>High RAM Usage</AlertDialogTitle>
          <AlertDialogDescription>
            RAM has been overclocking at above safe capacity for more than 30 seconds, causing harm to the system
          </AlertDialogDescription>
        </AlertDialogHeader>
        <AlertDialogFooter>
          <AlertDialogCancel>Close</AlertDialogCancel>
        </AlertDialogFooter>
      </AlertDialogContent>
    </AlertDialog>
        </div>
        <div className="ml-auto font-medium"><Badge>High</Badge></div>
      </div>
      <div className="flex items-center">
      <Avatar className="h-9 w-9">
          <AvatarImage src="/avatars/04.png" alt="Avatar" />
          <AvatarFallback style = {{backgroundColor: 'yellow'}}>P3</AvatarFallback>
        </Avatar>
        <div className="ml-4 space-y-1">
        <AlertDialog>
      <AlertDialogTrigger asChild>
      <p className="text-sm font-medium leading-none">Depreceated Software</p>
      </AlertDialogTrigger>
      <AlertDialogContent>
        <AlertDialogHeader>
          <AlertDialogTitle>Deprecated Software</AlertDialogTitle>
          <AlertDialogDescription>
            Software/Libraries need to be updated to latest version to ensure smooth and secure working.
          </AlertDialogDescription>
        </AlertDialogHeader>
        <AlertDialogFooter>
          <AlertDialogCancel>Close</AlertDialogCancel>
        </AlertDialogFooter>
      </AlertDialogContent>
    </AlertDialog>
        </div>
        <div className="ml-auto font-medium"><Badge>Medium</Badge></div>
      </div>
      <div className="flex items-center">
        <Avatar className="h-9 w-9">
          <AvatarImage src="/avatars/04.png" alt="Avatar" />
          <AvatarFallback style = {{backgroundColor: 'lightgreen'}}>P4</AvatarFallback>
        </Avatar>
        <div className="ml-4 space-y-1">
        <AlertDialog>
      <AlertDialogTrigger asChild>
      <p className="text-sm font-medium leading-none">Unoptimized Container</p>
      </AlertDialogTrigger>
      <AlertDialogContent>
        <AlertDialogHeader>
          <AlertDialogTitle>Unoptimized Container</AlertDialogTitle>
          <AlertDialogDescription>
            Unoptimized Container causing inefficient working and utilization of resources.
          </AlertDialogDescription>
        </AlertDialogHeader>
        <AlertDialogFooter>
          <AlertDialogCancel>Close</AlertDialogCancel>
        </AlertDialogFooter>
      </AlertDialogContent>
    </AlertDialog>
        </div>
        <div className="ml-auto font-medium"><Badge>Low</Badge></div>
      </div>
      <div className="flex items-center">
      <Avatar className="h-9 w-9">
          <AvatarImage src="/avatars/04.png" alt="Avatar" />
          <AvatarFallback style = {{backgroundColor: 'lightgreen'}}>P4</AvatarFallback>
        </Avatar>
        <div className="ml-4 space-y-1">
        <AlertDialog>
      <AlertDialogTrigger asChild>
      <p className="text-sm font-medium leading-none">Fellas in Paris</p>
      </AlertDialogTrigger>
      <AlertDialogContent>
        <AlertDialogHeader>
          <AlertDialogTitle>Fellas in Paris</AlertDialogTitle>
          <AlertDialogDescription>
            Guess who is in Paris, Yes! its Kanye west and Jay-Z
          </AlertDialogDescription>
        </AlertDialogHeader>
        <AlertDialogFooter>
          <AlertDialogCancel>Close</AlertDialogCancel>
        </AlertDialogFooter>
      </AlertDialogContent>
    </AlertDialog>
        </div>
        <div className="ml-auto font-medium"><Badge>Low</Badge></div>
      </div>
    </div>
  );
}
