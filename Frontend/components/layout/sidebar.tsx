'use client'
import { DashboardNav } from "@/components/dashboard-nav";
import { navItems } from "@/constants/data";
import { navProjects } from "@/constants/data";
import { cn } from "@/lib/utils";
import { useEffect, useState } from "react";
import { NavItem, SidebarNavItem } from "@/types";


export default function Sidebar() {
  const [projects, setProjects] = useState<NavItem[]>([
    {
      title: "Project 1",
      href: "/dashboard/project/1",
      icon: "dashboard",
      label: "Project 1",
    },
  ]);
  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/getAll")
      .then((response) => response.json())
      .then((data) => {
        const newList: NavItem[] =  [];
        for (const obj of data.container_ids) {
          newList.push({
            title: obj.name,
            href: `/dashboard/project/${obj.id}`,
            icon: "dashboard",
            label: obj.name,
          });
        }
        // console.log(newList);
        setProjects(newList);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
        // Handle the error appropriately, e.g., display an error message to the user
      });

  }, [])
  return (
    <nav
      className={cn(`relative hidden h-screen border-r pt-16 lg:block w-72`)}
    >
      <div className="space-y-4 py-4">
        <div className="px-3 py-2 space-y-8">
          <div className="space-y-1">
            <h2 className="mb-2 px-4 text-xl font-semibold tracking-tight">
              Overview
            </h2>
            <DashboardNav items={navItems} />
          </div>
          <div className="space-y-1">
            <h2 className="mb-2 px-4 text-xl font-semibold tracking-tight">
              Projects
            </h2>
            <DashboardNav items={projects} />
          </div>
        </div>
      </div>
    </nav>
  );
}
