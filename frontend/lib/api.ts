export async function runFusionPrediction(
  voiceData: string,
  spiralFile: File,
  datscanFile: File
) {

  const formData = new FormData();

  formData.append(
    "voice_data",
    voiceData
  );

  formData.append(
    "spiral_file",
    spiralFile
  );

  formData.append(
    "datscan_file",
    datscanFile
  );

  const response = await fetch(

    "http://127.0.0.1:8000/api/v1/predict/fusion",

    {
      method: "POST",

      body: formData
    }
  );

  if (!response.ok) {

    throw new Error(
      "Prediction failed"
    );
  }

  return response.json();
}