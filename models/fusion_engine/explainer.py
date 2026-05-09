def generate_explanation(

    fusion_result,

    voice_result,

    spiral_result,

    datscan_result
):

    # -----------------------------
    # Uncertain prediction
    # -----------------------------

    if fusion_result["final_prediction"] == "uncertain":

        return (
            "The models produced conflicting "
            "predictions, so the system is uncertain."
        )

    # -----------------------------
    # Get modality probabilities
    # -----------------------------

    voice_prob = voice_result[
        "parkinsons_probability"
    ]

    spiral_prob = spiral_result[
        "parkinsons_probability"
    ]

    datscan_prob = datscan_result[
        "parkinsons_probability"
    ]

    probs = {

        "voice": voice_prob,

        "spiral": spiral_prob,

        "datscan": datscan_prob
    }

    dominant_model = max(
        probs,
        key=probs.get
    )

    # -----------------------------
    # Explanation
    # -----------------------------

    if dominant_model == "voice":

        return (
            "Voice analysis strongly influenced "
            "the final prediction."
        )

    elif dominant_model == "spiral":

        return (
            "Spiral handwriting analysis strongly "
            "influenced the final prediction."
        )

    else:

        return (
            "DATScan brain imaging strongly "
            "influenced the final prediction."
        )