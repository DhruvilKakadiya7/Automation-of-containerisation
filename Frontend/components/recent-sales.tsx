import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { Badge } from "@/components/ui/badge"

export function RecentSales() {
  return (
    <div className="space-y-8">
      <div className="flex items-center">
      <Avatar className="h-9 w-9">
          <AvatarImage src="/avatars/04.png" alt="Avatar" />
          <AvatarFallback style = {{backgroundColor: 'red'}}>P1</AvatarFallback>
        </Avatar>
        <div className="ml-4 space-y-1">
          <p className="text-sm font-medium leading-none">CPU Overload</p>
          <p className="text-sm text-muted-foreground">
            CPU Working at 90% for more than 30 seconds.
          </p>
        </div>
        <div className="ml-auto font-medium"><Badge>High</Badge></div>
      </div>
      <div className="flex items-center">
      <Avatar className="h-9 w-9">
          <AvatarImage src="/avatars/04.png" alt="Avatar" />
          <AvatarFallback style = {{backgroundColor: 'red'}}>P2</AvatarFallback>
        </Avatar>
        <div className="ml-4 space-y-1">
          <p className="text-sm font-medium leading-none">Problem 2</p>
          <p className="text-sm text-muted-foreground">Very Problematic problem 2</p>
        </div>
        <div className="ml-auto font-medium"><Badge>High</Badge></div>
      </div>
      <div className="flex items-center">
      <Avatar className="h-9 w-9">
          <AvatarImage src="/avatars/04.png" alt="Avatar" />
          <AvatarFallback style = {{backgroundColor: 'yellow'}}>P3</AvatarFallback>
        </Avatar>
        <div className="ml-4 space-y-1">
          <p className="text-sm font-medium leading-none">Problem 3</p>
          <p className="text-sm text-muted-foreground">
            Theek Thaak Problematic Problem 3
          </p>
        </div>
        <div className="ml-auto font-medium"><Badge>Medium</Badge></div>
      </div>
      <div className="flex items-center">
        <Avatar className="h-9 w-9">
          <AvatarImage src="/avatars/04.png" alt="Avatar" />
          <AvatarFallback style = {{backgroundColor: 'lightgreen'}}>P4</AvatarFallback>
        </Avatar>
        <div className="ml-4 space-y-1">
          <p className="text-sm font-medium leading-none">Problem 4</p>
          <p className="text-sm text-muted-foreground">Bilkul dikkat nahi problem 4</p>
        </div>
        <div className="ml-auto font-medium"><Badge>Low</Badge></div>
      </div>
      <div className="flex items-center">
      <Avatar className="h-9 w-9">
          <AvatarImage src="/avatars/04.png" alt="Avatar" />
          <AvatarFallback style = {{backgroundColor: 'lightgreen'}}>P4</AvatarFallback>
        </Avatar>
        <div className="ml-4 space-y-1">
          <p className="text-sm font-medium leading-none">Problem 5</p>
          <p className="text-sm text-muted-foreground">Nahi bhi theek karoge toh chalega problem 5</p>
        </div>
        <div className="ml-auto font-medium"><Badge>Low</Badge></div>
      </div>
    </div>
  );
}
