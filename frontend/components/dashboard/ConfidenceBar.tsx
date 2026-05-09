"use client";

import { motion } from "framer-motion";

export default function ConfidenceBar({
  value
}: {
  value: number;
}) {

  return (

    <div className="mt-4 h-3 w-full overflow-hidden rounded-full bg-white/10">

      <motion.div
        initial={{ width: 0 }}
        animate={{ width: `${value}%` }}
        transition={{ duration: 1 }}
        className="h-full rounded-full bg-gradient-to-r from-cyan-400 to-blue-500"
      />

    </div>
  );
}