"use client";

import { motion } from "framer-motion";

export default function ExplanationCard({
  explanation
}: {
  explanation: string;
}) {

  return (

    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      className="rounded-3xl border border-white/10 bg-white/5 p-6 backdrop-blur-xl"
    >

      <h3 className="text-lg font-semibold">
        AI Clinical Interpretation
      </h3>

      <p className="mt-4 leading-7 text-slate-300">
        {explanation}
      </p>

    </motion.div>
  );
}