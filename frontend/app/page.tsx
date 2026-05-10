"use client";

import { motion } from "framer-motion";
import Link from "next/link";

import {
  Brain,
  Activity,
  AudioWaveform,
  ScanSearch,
} from "lucide-react";

import { Button } from "@/components/ui/button";

export default function HomePage() {
  return (
    <main className="min-h-screen text-white">
      {/* HERO */}
      <section className="relative overflow-hidden">
        <div className="mx-auto max-w-7xl px-6 py-24 lg:px-8">
          <motion.div
            initial={{ opacity: 0, y: 40 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
            className="max-w-4xl"
          >
            {/* Badge */}
            <div className="mb-6 inline-flex items-center gap-2 rounded-full border border-white/10 bg-white/5 px-4 py-2 backdrop-blur-md">
              <Brain className="h-4 w-4 text-cyan-400" />
              <span className="text-sm text-slate-300">
                AI-Powered Multimodal Parkinson Detection
              </span>
            </div>

            {/* Title */}
            <h1 className="text-5xl font-bold leading-tight tracking-tight sm:text-7xl">
              Next Generation
              <span className="bg-gradient-to-r from-cyan-400 to-blue-500 bg-clip-text text-transparent">
                {" "}
                Parkinson AI
              </span>
            </h1>

            {/* Description */}
            <p className="mt-8 max-w-2xl text-lg leading-8 text-slate-300">
              Advanced multimodal analysis using voice biomarkers, spiral
              handwriting patterns, and DATScan medical imaging powered by deep
              learning and AI fusion models.
            </p>

            {/* Buttons */}
            <div className="mt-10 flex flex-wrap gap-4">
              <Link href="/dashboard">
                <Button className="rounded-2xl px-8 py-6 text-base">
                  Launch Dashboard
                </Button>
              </Link>

              <Link href="/research">
                <Button
                  variant="outline"
                  className="rounded-2xl border-white/20 bg-white/5 px-8 py-6 text-base text-white backdrop-blur-md hover:bg-white/10"
                >
                  View Research
                </Button>
              </Link>
            </div>
          </motion.div>

          {/* FEATURE GRID */}
          <div className="mt-24 grid gap-6 md:grid-cols-3">
            <FeatureCard
              icon={<AudioWaveform className="h-8 w-8 text-cyan-400" />}
              title="Voice Biomarker Analysis"
              description="AI detects Parkinson-related vocal impairments using advanced acoustic feature extraction."
            />

            <FeatureCard
              icon={<Activity className="h-8 w-8 text-purple-400" />}
              title="Spiral Handwriting Detection"
              description="Deep learning models analyze motor-control abnormalities from spiral drawing patterns."
            />

            <FeatureCard
              icon={<ScanSearch className="h-8 w-8 text-emerald-400" />}
              title="DATScan Medical Imaging"
              description="Medical imaging AI analyzes dopaminergic degeneration patterns from brain scans."
            />
          </div>
        </div>
      </section>
    </main>
  );
}

function FeatureCard({
  icon,
  title,
  description,
}: {
  icon: React.ReactNode;
  title: string;
  description: string;
}) {
  return (
    <motion.div
      whileHover={{ y: -5 }}
      className="rounded-3xl border border-white/10 bg-white/5 p-8 backdrop-blur-xl"
    >
      <div className="mb-5">{icon}</div>

      <h3 className="text-xl font-semibold">{title}</h3>

      <p className="mt-4 leading-7 text-slate-300">{description}</p>
    </motion.div>
  );
}