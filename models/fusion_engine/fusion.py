def fuse_predictions(

    voice_prob,
    voice_conf,

    spiral_prob,
    spiral_conf,

    datscan_prob,
    datscan_conf
):

    # -----------------------------
    # Uncertainty handling
    # -----------------------------

    probs = [
        voice_prob,
        spiral_prob,
        datscan_prob
    ]

    max_prob = max(probs)
    min_prob = min(probs)

    if (max_prob - min_prob) > 0.5:

        return {
            "final_prediction": "uncertain",
            "final_probability": None,
            "reason": "High disagreement between modalities"
        }

    # -----------------------------
    # Confidence-weighted fusion
    # -----------------------------

    numerator = (

        voice_prob * voice_conf +

        spiral_prob * spiral_conf +

        datscan_prob * datscan_conf
    )

    denominator = (

        voice_conf +

        spiral_conf +

        datscan_conf
    )

    final_score = numerator / denominator

    prediction = 1 if final_score > 0.5 else 0

    return {

        "final_prediction": prediction,

        "final_probability": final_score,

        "voice_weight": voice_conf,

        "spiral_weight": spiral_conf,

        "datscan_weight": datscan_conf
    }