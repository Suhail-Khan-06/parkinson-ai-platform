const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000";

export async function runFusionPrediction(
  voiceData: string,
  spiralFile: File,
  datscanFile: File
) {
  const formData = new FormData();

  formData.append("voice_data", voiceData);
  formData.append("spiral_file", spiralFile);
  formData.append("datscan_file", datscanFile);

  const response = await fetch(
    `${API_BASE_URL}/api/v1/predict/fusion`,
    {
      method: "POST",
      body: formData,
    }
  );

  if (!response.ok) {
    const errorText = await response.text();
    throw new Error(errorText || "Prediction failed");
  }

  return response.json();
}

export async function downloadFusionReport(
  voiceData: string,
  spiralFile: File,
  datscanFile: File
) {
  const formData = new FormData();

  formData.append("voice_data", voiceData);
  formData.append("spiral_file", spiralFile);
  formData.append("datscan_file", datscanFile);

  const response = await fetch(
    `${API_BASE_URL}/api/v1/fusion/report`,
    {
      method: "POST",
      body: formData,
    }
  );

  if (!response.ok) {
    throw new Error("Failed to generate report");
  }

  return response.blob();
}