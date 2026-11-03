"""
Example Usage: Cutaneous Tactile Sensitivity & Mechanical Allodynia (Von Frey).
Demonstrates psychophysical calculation of Semmes-Weinstein marking and sensory discrimination.
"""

from client import CutaneousTactileVonFreyClient


def main():
    client = CutaneousTactileVonFreyClient()
    print("=== Cutaneous Tactile Sensitivity (Von Frey) Demo ===")

    # Test Case 1: Healthy normal fingertip light touch
    res1 = client.evaluate_tactile_threshold(
        applied_force_grams=0.04,
        detection_reported=True,
        pain_reported=False,
        test_site="FINGERTIP"
    )
    print("\nTest Case 1: Healthy Fingertip Light Touch")
    print(f"  Applied Force: {res1['applied_force_grams']} g ({res1['force_milligrams']} mg)")
    print(f"  Semmes-Weinstein Marking: {res1['semmes_weinstein_marking']}")
    print(f"  Tactile Acuity Score: {res1['tactile_acuity_score']} / 100")
    print(f"  Classification: {res1['classification']}")
    print(f"  Guidance: {res1['actionable_guidance']}")

    # Test Case 2: Mechanical allodynia (Pain evoked by light touch)
    res2 = client.evaluate_tactile_threshold(
        applied_force_grams=0.07,
        detection_reported=True,
        pain_reported=True,
        test_site="DORSUM_HAND"
    )
    print("\nTest Case 2: Dynamic Mechanical Allodynia")
    print(f"  Applied Force: {res2['applied_force_grams']} g | Pain Reported: {res2['pain_reported']}")
    print(f"  Tactile Acuity Score: {res2['tactile_acuity_score']} / 100")
    print(f"  Classification: {res2['classification']}")
    print(f"  Guidance: {res2['actionable_guidance']}")

    # Test Case 3: Loss of protective sensation / diabetic peripheral blunting
    res3 = client.evaluate_tactile_threshold(
        applied_force_grams=4.0,
        detection_reported=True,
        pain_reported=False,
        test_site="PLANTAR_FOOT"
    )
    print("\nTest Case 3: Loss of Protective Sensation")
    print(f"  Applied Force: {res3['applied_force_grams']} g (SW {res3['semmes_weinstein_marking']})")
    print(f"  Tactile Score: {res3['tactile_acuity_score']} / 100")
    print(f"  Classification: {res3['classification']}")
    print(f"  Guidance: {res3['actionable_guidance']}")


if __name__ == "__main__":
    main()
