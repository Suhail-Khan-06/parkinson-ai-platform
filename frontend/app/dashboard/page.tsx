"use client";

import { motion } from "framer-motion";

import PredictionWorkspace from "@/components/prediction/PredictionWorkspace";

import {
  Brain,
  LayoutDashboard,
  Activity,
  ScanSearch,
  AudioWaveform,
  Settings,
  Bell,
  User
} from "lucide-react";

export default function DashboardPage() {

  return (

    <main className="relative flex min-h-screen bg-[#030712] text-white">

      {/* AMBIENT BACKGROUND */}

      <div className="pointer-events-none absolute inset-0 overflow-hidden">

        {/* CYAN GLOW */}

        <div className="animate-float absolute left-[-120px] top-[-120px] h-[350px] w-[350px] rounded-full bg-cyan-500/20 blur-3xl" />

        {/* BLUE GLOW */}

        <div className="animate-float absolute right-[-120px] top-[100px] h-[400px] w-[400px] rounded-full bg-blue-500/20 blur-3xl" />

        {/* PURPLE GLOW */}

        <div className="animate-float absolute bottom-[-150px] left-[30%] h-[450px] w-[450px] rounded-full bg-purple-500/20 blur-3xl" />

      </div>

      {/* GRID OVERLAY */}

      <div className="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,0.03)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.03)_1px,transparent_1px)] bg-[size:40px_40px]" />

      {/* SIDEBAR */}

      <aside className="relative z-10 hidden w-72 border-r border-white/10 bg-white/5 backdrop-blur-xl lg:flex lg:flex-col">

        {/* LOGO */}

        <div className="border-b border-white/10 p-6">

          <div className="flex items-center gap-3">

            <div className="rounded-2xl bg-cyan-500/20 p-3">

              <Brain className="h-6 w-6 text-cyan-400" />

            </div>

            <div>

              <h1 className="text-lg font-semibold">
                Parkinson AI
              </h1>

              <p className="text-sm text-slate-400">
                Multimodal Platform
              </p>

            </div>

          </div>

        </div>

        {/* NAVIGATION */}

        <nav className="flex-1 space-y-2 p-4">

          <SidebarItem
            icon={<LayoutDashboard />}
            label="Dashboard"
            active
          />

          <SidebarItem
            icon={<AudioWaveform />}
            label="Voice Analysis"
          />

          <SidebarItem
            icon={<Activity />}
            label="Spiral Detection"
          />

          <SidebarItem
            icon={<ScanSearch />}
            label="DATScan Imaging"
          />

          <SidebarItem
            icon={<Settings />}
            label="Settings"
          />

        </nav>

        {/* FOOTER */}

        <div className="border-t border-white/10 p-4">

          <div className="rounded-2xl border border-cyan-500/20 bg-cyan-500/10 p-4">

            <p className="text-sm text-cyan-300">
              AI System Status
            </p>

            <div className="mt-3 flex items-center gap-2">

              <div className="h-3 w-3 rounded-full bg-emerald-400" />

              <p className="text-sm text-slate-300">
                All models operational
              </p>

            </div>

          </div>

        </div>

      </aside>

      {/* MAIN CONTENT */}

      <div className="relative z-10 flex flex-1 flex-col overflow-y-auto">

        {/* TOPBAR */}

        <header className="sticky top-0 z-20 flex items-center justify-between border-b border-white/10 bg-[#030712]/70 px-6 py-4 backdrop-blur-2xl">

          <div>

            <h2 className="text-3xl font-bold tracking-tight">
              Dashboard
            </h2>

            <p className="mt-1 text-sm text-slate-400">
              AI-powered Parkinson diagnostic workspace
            </p>

          </div>

          <div className="flex items-center gap-4">

            <button className="rounded-2xl border border-white/10 bg-white/5 p-3 transition-all hover:scale-105 hover:bg-white/10">

              <Bell className="h-5 w-5" />

            </button>

            <button className="rounded-2xl border border-white/10 bg-white/5 p-3 transition-all hover:scale-105 hover:bg-white/10">

              <User className="h-5 w-5" />

            </button>

          </div>

        </header>

        {/* PAGE CONTENT */}

        <div className="flex-1 p-6">

          {/* HERO */}

          <div className="mb-10">

            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
            >

              <p className="mb-4 inline-flex rounded-full border border-cyan-500/20 bg-cyan-500/10 px-4 py-2 text-sm text-cyan-300 backdrop-blur-xl">

                AI-Powered Multimodal Parkinson Detection

              </p>

              <h1 className="max-w-5xl text-5xl font-bold leading-tight tracking-tight md:text-7xl">

                Advanced Parkinson’s

                <span className="bg-gradient-to-r from-cyan-400 to-blue-500 bg-clip-text text-transparent">

                  {" "}AI Platform

                </span>

              </h1>

              <p className="mt-6 max-w-3xl text-lg leading-8 text-slate-300">

                AI-driven multimodal neurological analysis using
                voice biomarkers, spiral handwriting dynamics,
                and DATScan medical imaging fusion models.

              </p>

            </motion.div>

          </div>

          {/* STATS */}

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="mb-10 grid gap-6 lg:grid-cols-3"
          >

            <DashboardCard
              title="Voice Biomarker"
              value="94%"
              description="High Parkinson probability"
            />

            <DashboardCard
              title="Spiral Detection"
              value="71%"
              description="Moderate motor irregularities"
            />

            <DashboardCard
              title="DATScan Imaging"
              value="68%"
              description="Dopaminergic degeneration detected"
            />

          </motion.div>

          {/* WORKSPACE */}

          <PredictionWorkspace />

        </div>

      </div>

    </main>
  );
}

/* -------------------------------- */
/* SIDEBAR ITEM */
/* -------------------------------- */

function SidebarItem({
  icon,
  label,
  active = false
}: {
  icon: React.ReactNode;
  label: string;
  active?: boolean;
}) {

  return (

    <button
      className={`group flex w-full items-center gap-3 rounded-2xl px-4 py-3 transition-all duration-300 ${
        active
          ? "bg-cyan-500/20 text-cyan-300 shadow-lg shadow-cyan-500/10"
          : "text-slate-300 hover:bg-white/5 hover:text-white"
      }`}
    >

      <div className="transition-transform duration-300 group-hover:scale-110">

        {icon}

      </div>

      <span className="font-medium">
        {label}
      </span>

    </button>
  );
}

/* -------------------------------- */
/* DASHBOARD CARD */
/* -------------------------------- */

function DashboardCard({
  title,
  value,
  description
}: {
  title: string;
  value: string;
  description: string;
}) {

  return (

    <motion.div
      whileHover={{
        y: -5,
        scale: 1.01
      }}
      transition={{
        type: "spring",
        stiffness: 300
      }}
      className="relative overflow-hidden rounded-3xl border border-white/10 bg-white/5 p-6 backdrop-blur-xl"
    >

      {/* CARD GLOW */}

      <div className="absolute inset-0 bg-gradient-to-br from-cyan-500/5 to-blue-500/5 opacity-0 transition-opacity duration-500 hover:opacity-100" />

      <div className="relative z-10">

        <p className="text-slate-400">
          {title}
        </p>

        <h3 className="mt-4 text-5xl font-bold tracking-tight">

          {value}

        </h3>

        <p className="mt-4 text-slate-300 leading-7">

          {description}

        </p>

      </div>

    </motion.div>
  );
}