"use client";

import CountUp from "react-countup";

import { motion } from "framer-motion";

import ConfidenceBar from "./ConfidenceBar";

export default function ModalityCard({
  title,
  prediction,
  confidence,
  color
}: {
  title: string;
  prediction: string;
  confidence: number;
  color: string;
}) {

  return (

    <motion.div
      whileHover={{ scale: 1.02 }}
      className="rounded-3xl border border-white/10 bg-white/5 p-6 backdrop-blur-xl"
    >

      <div className="flex items-center justify-between">

        <div>

          <p className="text-sm text-slate-400">
            {title}
          </p>

          <h3 className="mt-2 text-xl font-semibold">
            {prediction}
          </h3>

        </div>

        <div
          className={`h-4 w-4 rounded-full ${color}`}
        />

      </div>

      <div className="mt-6">

        <div className="flex items-center justify-between">

          <p className="text-sm text-slate-400">
            Confidence
          </p>

          <p className="text-lg font-semibold">

            <CountUp
              end={confidence}
              decimals={1}
              duration={1.5}
            />

            %

          </p>

        </div>

        <ConfidenceBar value={confidence} />

      </div>

    </motion.div>
  );
}