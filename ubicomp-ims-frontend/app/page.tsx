"use client";

import AppNavbar from "@/components/global/AppNavbar";

import React from "react";

export default function Home() {
  return (
    <div className="h-screen flex flex-col">
      <AppNavbar src="/" item1="Overview" item2="Dashboard" />
      <div className="flex-grow flex flex-col items-center justify-center">
        <h1 className="text-4xl font-bold">Welcome to UbiComp IMS</h1>
        <p className="mt-4 text-xl">Please select a page from the sidebar.</p>
      </div>
    </div>
  );
}
