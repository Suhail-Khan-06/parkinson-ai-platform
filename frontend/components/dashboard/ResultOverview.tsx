"use client";

import { motion } from "framer-motion";

import CountUp from "react-countup";

export default function ResultOverview({
  prediction,
  confidence
}: {
  prediction: string;
  confidence: number;
}) {

  return (

    <motion.div
      initial={{ opacity: 0, y: -10 }}
      animate={{ opacity: 1, y: 0 }}
      className="rounded-3xl border border-cyan-500/20 bg-gradient-to-br from-cyan-500/10 to-blue-500/10 p-8 backdrop-blur-xl"
    >

      <p className="text-sm uppercase tracking-widest text-cyan-300">
        Overall AI Prediction
      </p>

      <div className="mt-4 flex items-end justify-between">

        <div>

          <h2 className="text-4xl font-bold">
            {prediction}
          </h2>

          <p className="mt-2 text-slate-300">
            Multimodal fusion analysis completed
          </p>

        </div>

        <div className="text-right">

          <p className="text-sm text-slate-400">
            Confidence
          </p>

          <h3 className="text-4xl font-bold text-cyan-300">

            <CountUp
              end={confidence}
              decimals={1}
              duration={1.5}
            />

            %

          </h3>

        </div>

      </div>

    </motion.div>
  );
}