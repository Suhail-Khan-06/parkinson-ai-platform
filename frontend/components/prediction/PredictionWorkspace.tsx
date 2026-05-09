"use client";

import { useState } from "react";

import { useDropzone } from "react-dropzone";

import { motion } from "framer-motion";

import {
  Upload,
  AudioWaveform,
  Activity,
  ScanSearch
} from "lucide-react";

import { Button } from "@/components/ui/button";
import AnalyticsChart from "@/components/dashboard/AnalyticsChart";

import { Textarea } from "@/components/ui/textarea";

import { runFusionPrediction } from "@/lib/api";

import ResultOverview from "@/components/dashboard/ResultOverview";

import ModalityCard from "@/components/dashboard/ModalityCard";

import ExplanationCard from "@/components/dashboard/ExplanationCard";

export default function PredictionWorkspace() {

  const [voiceData, setVoiceData] = useState("");

  const [spiralFile, setSpiralFile] = useState<File | null>(null);

  const [datscanFile, setDatscanFile] = useState<File | null>(null);

  const [loading, setLoading] = useState(false);

  const [result, setResult] = useState<any>(null);

  const [error, setError] = useState("");

  // -----------------------------------
  // Prediction Handler
  // -----------------------------------

  const handlePrediction = async () => {

    if (!voiceData || !spiralFile || !datscanFile) {

      setError("Please provide all multimodal inputs");

      return;
    }

    try {

      setLoading(true);

      setError("");

      setResult(null);

      const data = await runFusionPrediction(
        voiceData,
        spiralFile,
        datscanFile
      );

      console.log("Fusion Result:", data);

      setResult(data);

    } catch (err: any) {

      console.error(err);

      setError(
        err?.message ||
        "Prediction failed"
      );

    } finally {

      setLoading(false);
    }
  };

  // -----------------------------------
  // Spiral Upload
  // -----------------------------------

  const spiralDropzone = useDropzone({

    accept: {
      "image/*": [".png", ".jpg", ".jpeg"]
    },

    multiple: false,

    onDrop: (acceptedFiles, rejectedFiles) => {

      if (rejectedFiles.length > 0) {

        setError(
          "Invalid spiral image file"
        );

        return;
      }

      if (acceptedFiles.length > 0) {

        setError("");

        setSpiralFile(acceptedFiles[0]);
      }
    }
  });

  // -----------------------------------
  // DATScan Upload
  // -----------------------------------

  const datscanDropzone = useDropzone({

    accept: {
      "application/dicom": [".dcm"],
      "application/octet-stream": [
        ".dcm",
        ".nii",
        ".nii.gz"
      ],
      "image/*": [
        ".png",
        ".jpg",
        ".jpeg"
      ]
    },

    multiple: false,

    onDrop: (acceptedFiles, rejectedFiles) => {

      if (rejectedFiles.length > 0) {

        setError(
          "Invalid DATScan file. Upload DICOM (.dcm) or NIfTI (.nii/.nii.gz)"
        );

        return;
      }

      if (acceptedFiles.length > 0) {

        setError("");

        setDatscanFile(acceptedFiles[0]);
      }
    }
  });

  return (

    <div className="grid gap-8 lg:grid-cols-2">

      {/* LEFT PANEL */}

      <motion.div
        initial={{ opacity: 0, x: -20 }}
        animate={{ opacity: 1, x: 0 }}
        className="rounded-3xl border border-white/10 bg-white/5 p-8 backdrop-blur-xl"
      >

        <h2 className="text-2xl font-semibold">
          Multimodal Inputs
        </h2>

        <p className="mt-2 text-slate-400">
          Upload multimodal patient data for AI analysis.
        </p>

        {/* VOICE INPUT */}

        <div className="mt-8">

          <div className="mb-3 flex items-center gap-2">

            <AudioWaveform className="h-5 w-5 text-cyan-400" />

            <h3 className="font-medium">
              Voice Biomarker JSON
            </h3>

          </div>

          <Textarea
            value={voiceData}
            onChange={(e) => setVoiceData(e.target.value)}
            placeholder={`{
  "mdvp_fo_hz": 119.992,
  "mdvp_jitter_percent": 0.00784,
  "mdvp_shimmer": 0.04374
}`}
            className="min-h-[180px] rounded-2xl border-white/10 bg-black/20"
          />

        </div>

        {/* SPIRAL */}

        <UploadZone
          title="Spiral Handwriting"
          icon={<Activity className="h-6 w-6 text-purple-400" />}
          file={spiralFile}
          dropzone={spiralDropzone}
        />

        {/* DATSCAN */}

        <UploadZone
          title="DATScan Imaging"
          icon={<ScanSearch className="h-6 w-6 text-emerald-400" />}
          file={datscanFile}
          dropzone={datscanDropzone}
        />

        {/* BUTTON */}

        <Button
          onClick={handlePrediction}
          disabled={loading}
          className="mt-8 w-full rounded-2xl py-6 text-base"
        >

          {loading
            ? "Running AI Analysis..."
            : "Run AI Analysis"}

        </Button>

      </motion.div>

      {/* RIGHT PANEL */}

      <motion.div
        initial={{ opacity: 0, x: 20 }}
        animate={{ opacity: 1, x: 0 }}
        className="sticky top-6 h-fit rounded-3xl border border-white/10 bg-white/5 p-8 backdrop-blur-xl"
      >

        <h2 className="text-2xl font-semibold">
          AI Analysis Results
        </h2>

        <p className="mt-2 text-slate-400">
          Multimodal fusion predictions will appear here.
        </p>

        <div className="mt-10">

          {/* ERROR */}

          {error && (

            <div className="rounded-2xl border border-red-500/20 bg-red-500/10 p-4 text-red-300">

              {error}

            </div>
          )}

          {/* EMPTY STATE */}

          {!result && !loading && !error && (

            <div className="flex h-[500px] items-center justify-center rounded-3xl border border-dashed border-white/10 bg-black/20">

              <div className="text-center">

                <Upload className="mx-auto h-14 w-14 text-slate-500" />

                <p className="mt-5 text-slate-400">

                  Upload patient data and run analysis

                </p>

              </div>

            </div>
          )}

          {/* LOADING */}

          {loading && (

            <div className="flex h-[500px] items-center justify-center rounded-3xl border border-white/10 bg-black/20">

              <motion.div
                animate={{ rotate: 360 }}
                transition={{
                  repeat: Infinity,
                  duration: 1,
                  ease: "linear"
                }}
                className="h-16 w-16 rounded-full border-4 border-cyan-400 border-t-transparent"
              />

            </div>
          )}

          {/* RESULTS */}

          {result && (

            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              className="space-y-6"
            >

              {/* OVERVIEW */}

              <ResultOverview
                prediction={
                  result.fusion_result?.final_prediction === 1
                    ? "Parkinson Detected"
                    : result.fusion_result?.final_prediction === 0
                    ? "Healthy"
                    : "Uncertain"
                }
                confidence={
                  result.fusion_result?.final_probability
                    ? result.fusion_result.final_probability * 100
                    : 0
                }
              />

              {/* MODALITIES */}

              <div className="grid gap-6 md:grid-cols-3">

                {/* VOICE */}

                <ModalityCard
                  title="Voice Biomarkers"
                  prediction={
                    result.voice_result?.prediction === 1
                      ? "Parkinson"
                      : "Healthy"
                  }
                  confidence={
                    result.voice_result?.parkinsons_probability
                      ? result.voice_result.parkinsons_probability * 100
                      : 0
                  }
                  color="bg-cyan-400"
                />

                {/* SPIRAL */}

                <ModalityCard
                  title="Spiral Analysis"
                  prediction={
                    result.spiral_result?.prediction || "Unknown"
                  }
                  confidence={
                    result.spiral_result?.confidence
                      ? result.spiral_result.confidence * 100
                      : 0
                  }
                  color="bg-purple-400"
                />

                {/* DATSCAN */}

                <ModalityCard
                  title="DATScan Imaging"
                  prediction={
                    result.datscan_result?.prediction || "Unknown"
                  }
                  confidence={
                    result.datscan_result?.confidence
                      ? result.datscan_result.confidence * 100
                      : 0
                  }
                  color="bg-emerald-400"
                />

              </div>

              {/* EXPLANATION */}

              <ExplanationCard
                explanation={
                  result.explanation ||
                  "No explanation available."
                }
              />
              <AnalyticsChart
  voice={
    result.voice_result?.parkinsons_probability
      ? result.voice_result.parkinsons_probability * 100
      : 0
  }
  spiral={
    result.spiral_result?.confidence
      ? result.spiral_result.confidence * 100
      : 0
  }
  datscan={
    result.datscan_result?.confidence
      ? result.datscan_result.confidence * 100
      : 0
  }
/>

            </motion.div>
          )}

        </div>

      </motion.div>

    </div>
  );
}

function UploadZone({
  title,
  icon,
  file,
  dropzone
}: {
  title: string;
  icon: React.ReactNode;
  file: File | null;
  dropzone: any;
}) {

  const {
    getRootProps,
    getInputProps,
    isDragActive
  } = dropzone;

  return (

    <div className="mt-8">

      <div className="mb-3 flex items-center gap-2">

        {icon}

        <h3 className="font-medium">
          {title}
        </h3>

      </div>

      <div
        {...getRootProps()}
        className={`cursor-pointer rounded-3xl border border-dashed p-8 text-center transition-all ${
          isDragActive
            ? "border-cyan-400 bg-cyan-500/10"
            : "border-white/10 bg-black/20 hover:bg-white/5"
        }`}
      >

        <input {...getInputProps()} />

        <Upload className="mx-auto h-10 w-10 text-slate-400" />

        {file ? (

  <div className="mt-4">

    <img
      src={URL.createObjectURL(file)}
      alt="preview"
      className="mx-auto h-40 w-full rounded-2xl object-cover"
    />

    <p className="mt-4 text-sm text-slate-300 break-all">
      {file.name}
    </p>

  </div>

) : (

  <p className="mt-4 text-slate-300">

    Drag & drop image here or click to upload

  </p>

)}

      </div>

    </div>
  );
}