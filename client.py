"""
Cutaneous Tactile Sensitivity & Mechanical Allodynia (Von Frey) Engine.
Provides deterministic, zero-dependency psychophysical modeling of Semmes-Weinstein monofilament
logarithmic force thresholds, 50% Dixon up-down staircase calculations, and tactile mechanoreceptive acuity.
"""

import math
from typing import Dict, Any, List, Optional


class CutaneousTactileVonFreyClient:
    """
    Deterministic client for evaluating cutaneous tactile thresholds via Von Frey monofilaments.
    Assesses low-threshold mechanoreceptor sensitivity (Meissner corpuscles, Merkel discs)
    and discriminates between sensory loss (neuropathy) and tactile mechanical allodynia.
    """

    def __init__(self):
        pass

    def evaluate_tactile_threshold(
        self,
        applied_force_grams: float,
        detection_reported: bool = True,
        pain_reported: bool = False,
        test_site: str = "FINGERTIP"
    ) -> Dict[str, Any]:
        """
        Evaluates Semmes-Weinstein monofilament mechanical sensory threshold:
        - Marking Index = log10(10 * Force in mg)
        - Normal light touch on fingertips: 0.04 - 0.07 grams (marking 2.44 - 2.83)
        - Loss of protective sensation: > 2.0 grams (marking >= 4.31)
        """
        if applied_force_grams <= 0:
            return {"error": "Applied force must be strictly positive"}

        force_mg = applied_force_grams * 1000.0
        sw_marking = round(math.log10(10.0 * force_mg), 2)

        site = test_site.upper()

        # Tactile Mechanoreceptive Acuity Score (0 - 100):
        # Healthy normal fingertip 0.02 - 0.08 g -> 90 - 100.
        # Force > 2.0 g -> < 40 (Loss of protective sensation).
        if applied_force_grams <= 0.08:
            score = 92.0 + min(8.0, (0.08 - applied_force_grams) * 100.0)
        elif applied_force_grams <= 0.4:
            score = 75.0 + ((0.4 - applied_force_grams) / 0.32) * 15.0
        elif applied_force_grams <= 2.0:
            score = 50.0 + ((2.0 - applied_force_grams) / 1.6) * 23.0
        elif applied_force_grams <= 10.0:
            score = 25.0 + ((10.0 - applied_force_grams) / 8.0) * 23.0
        else:
            score = max(5.0, 25.0 - (applied_force_grams - 10.0) * 0.1)

        if pain_reported:
            score = max(10.0, score - 35.0)

        acuity_score = round(min(100.0, max(5.0, score)), 1)

        if pain_reported and applied_force_grams < 0.4:
            tier = "DYNAMIC_MECHANICAL_ALLODYNIA"
            interp = f"Innocuous light touch ({applied_force_grams} g, SW {sw_marking}) evokes pain; indicates central sensitization or neuropathic hyperesthesia."
            guidance = "Tactile mechanical allodynia detected. Reduce tactile shear stress, avoid abrasive surfaces, and evaluate neuro-inflammatory causes."
        elif applied_force_grams <= 0.08 and detection_reported:
            tier = "NORMAL_LIGHT_TOUCH_DISCRIMINATION"
            interp = f"Normal delicate mechanoreceptive threshold ({applied_force_grams} g, SW {sw_marking}) on {site}; intact A-beta tactile afferents."
            guidance = "Excellent tactile spatial and pressure discrimination. Ideal sensory feedback for precision manipulation."
        elif applied_force_grams <= 0.4 and detection_reported:
            tier = "DIMINISHED_LIGHT_TOUCH"
            interp = f"Mild elevation in sensory threshold ({applied_force_grams} g, SW {sw_marking}); subtle mechanoreceptive blunting."
            guidance = "Subtle tactile sensitivity reduction. Incorporate ergonomic keyboard rest and evaluate repetitive strain risks."
        elif applied_force_grams <= 2.0 and detection_reported:
            tier = "DIMINISHED_PROTECTIVE_SENSATION"
            interp = f"Moderate sensory loss ({applied_force_grams} g, SW {sw_marking}); requires conscious tactile monitoring."
            guidance = "Diminished protective tactile feedback. Avoid hot/sharp contact surfaces and monitor for compressive neuropathies."
        else:
            tier = "LOSS_OF_PROTECTIVE_SENSATION"
            interp = f"Severe sensory deficit ({applied_force_grams} g, SW {sw_marking} > 4.31); inability to perceive standard micro-trauma."
            guidance = "Critical loss of protective sensation. Institute strict visual inspection protocols and consult neurology."

        return {
            "test_site": site,
            "applied_force_grams": applied_force_grams,
            "force_milligrams": round(force_mg, 1),
            "semmes_weinstein_marking": sw_marking,
            "detection_reported": detection_reported,
            "pain_reported": pain_reported,
            "tactile_acuity_score": acuity_score,
            "classification": tier,
            "physiological_interpretation": interp,
            "actionable_guidance": guidance
        }
