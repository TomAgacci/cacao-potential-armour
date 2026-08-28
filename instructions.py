"""
HSN Full‑Optimized 3–5 MPa Material Estimator
---------------------------------------------
This script models the theoretical compressive strength (MPa)
of the full‑optimized HSN composite using normalized parameters.

You can adjust the parameters in the "params" dictionary at the bottom.
"""

def hsn_mpa_estimate(
    water_ratio,        # 0–1 (lower = stronger)
    salt_pct,           # 0–1 normalized (higher = weaker)
    lime_fraction,      # 0–1
    sand_fraction,      # 0–1
    resin_level,        # 0–1
    protein_level,      # 0–1
    compaction_energy,  # 0–1
    curing_efficiency   # 0–1
):
    # Salt penalty constant
    salt_alpha = 0.35

    # Cohesion factor from resin + protein
    cohesion = 0.6 * resin_level + 0.4 * protein_level

    # Mineral backbone (lime + sand)
    mineral = lime_fraction + sand_fraction

    # Density factor from compaction
    density = 0.5 + 0.5 * compaction_energy

    # Water penalty (lower water = stronger)
    water_penalty = 1 - water_ratio

    # Salt penalty (higher salt = weaker)
    salt_penalty = 1 - salt_alpha * salt_pct

    # Curing multiplier
    curing = curing_efficiency

    # HSN theoretical MPa model
    mpa = density * mineral * cohesion * curing * water_penalty * salt_penalty

    # Scale to 0–5 MPa theoretical band
    return round(mpa * 5, 2)


# Example: full-optimized composite parameters
params = {
    "water_ratio": 0.15,         # low water
    "salt_pct": 0.05,            # low salt
    "lime_fraction": 0.9,        # high lime
    "sand_fraction": 0.9,        # high sand
    "resin_level": 0.7,          # tuned cacao resin
    "protein_level": 0.5,        # hemp protein modifier
    "compaction_energy": 0.95,   # very high compaction
    "curing_efficiency": 0.9     # strong carbonation
}

mpa = hsn_mpa_estimate(**params)
print("HSN Full-Optimized MPa Estimate:", mpa)
