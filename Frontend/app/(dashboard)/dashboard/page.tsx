'use client';
import { CalendarDateRangePicker } from "@/components/date-range-picker";
import { Overview } from "@/components/overview";
import { RecentSales } from "@/components/recent-sales";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
import { useEffect, useState } from "react";
import { Label } from '@/components/ui/label';
import { Input } from "@/components/ui/input";



export default function page() {
    const [url, setUrl] = useState<string>(''); // State to hold the URL
    const [projects, setProjects] = useState([])

    const handleUrlChange = (event) => {
        setUrl(event.target.value);
    };

    const handleSubmit = () => {
      console.log("Hello");
        console.log(url);
        const formData = new FormData();
        formData.append('rep_url', url);

        fetch('http://127.0.0.1:5000/api/create_website', {
            mode: 'no-cors',
            method: 'POST', // Specify the method
      body: formData,
          })
          .then((response) => {
            if (!response.ok) {
              throw new Error('Network response was not ok');
            }
            return response.json();
          })
          .then((data) => {
            window.location.reload(); // You can replace 'any' with the actual type of your response data
            console.log("Website created successfully:", data);
          })
          .catch((error) => {
            window.location.reload();
            console.error("Error creating website:", error);
          });
          
        
    };




  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/getAll")
      .then((response) => response.json())
      .then((data) => {
        // console.log(newList);
        setProjects(data.container_ids);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
        // Handle the error appropriately, e.g., display an error message to the user
      });

  }, [])

  return (
    <ScrollArea className="h-full">
      <div className="flex-1 space-y-4 p-4 md:p-8 pt-6">
        <div className="flex items-center justify-between space-y-2">
          <h2 className="text-3xl font-bold tracking-tight">
            All Containers
          </h2>
          <div className="hidden md:flex items-center space-x-2">
            {/* <CalendarDateRangePicker /> */}

           
            {/* <Button>ADD</Button> */}
            <Dialog>
      <DialogTrigger asChild>
        <Button>ADD</Button>
      </DialogTrigger>
      <DialogContent className="sm:max-w-[425px]">
        <DialogHeader>
          <DialogTitle>Auto-Deploy Projects</DialogTitle>
          <DialogDescription>
            Add GitHub Repository Link and click save when you're done.
          </DialogDescription>
        </DialogHeader>
        <div className="grid gap-4 py-4">
          <div className="grid grid-cols-4 items-center gap-4">
            <Label htmlFor="name" className="text-right">
              Repo Link
            </Label>
            <Input id="URL" placeholder="https://github.com/" className="col-span-3" onChange={handleUrlChange} />
          </div>
        </div>
        <DialogFooter>
          <Button type="submit" onClick={handleSubmit}>Save changes</Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>

          </div>
        </div>
        <Tabs defaultValue="overview" className="space-y-4">
          <TabsContent value="overview" className="space-y-4">
            <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
            {projects.map((project,ind)=>
             <Card key={ind}>
             <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
               <CardTitle className="text-sm font-medium">
                 {project.status}
               </CardTitle>
               <svg
                 xmlns="http://www.w3.org/2000/svg"
                 viewBox="0 0 24 24"
                 fill="none"
                 stroke="currentColor"
                 strokeLinecap="round"
                 strokeLinejoin="round"
                 strokeWidth="2"
                 className="h-4 w-4 text-muted-foreground"
               >
                 <path d="M22 12h-4l-3 9L9 3l-3 9H2" />
               </svg>
             </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold">{project.name}</div>
              <p className="text-xs text-muted-foreground">
                {(() => {
                  const dateObject = new Date(project.created);
                  const formattedDate = dateObject.toLocaleString();
                  return formattedDate;
                })()}
              </p>
            </CardContent>
           </Card>)}
           
            </div>
            <div className="grid gap-4 grid-cols-1 md:grid-cols-2 lg:grid-cols-7">
              <Card className="col-span-4">
                <CardHeader>
                  <CardTitle>Overview</CardTitle>
                </CardHeader>
                <CardContent className="pl-2">
                  <Overview />
                </CardContent>
              </Card>
              <Card className="col-span-4 md:col-span-3">
                <CardHeader>
                  <CardTitle>Recent Alerts</CardTitle>
                  <CardDescription>
                    List of Recent Alerts
                  </CardDescription>
                </CardHeader>
                <CardContent>
                  <RecentSales />
                </CardContent>
              </Card>
            </div>
          </TabsContent>
        </Tabs>
      </div>
    </ScrollArea>
  );
}
