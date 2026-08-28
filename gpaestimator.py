"""
HSN Max-GPa Composite Estimator
-------------------------------
Models:
- Compressive Strength (MPa)
- Elastic Modulus (GPa)

Parameters normalized 0–1.
"""

def hsn_strength_mpa(
    water_ratio,
    salt_pct,
    lime_fraction,
    sand_fraction,
    resin_level,
    protein_level,
    compaction_energy,
    curing_efficiency
):
    salt_alpha = 0.35
    cohesion = 0.6 * resin_level + 0.4 * protein_level
    mineral = lime_fraction + sand_fraction
    density = 0.5 + 0.5 * compaction_energy
    water_penalty = 1 - water_ratio
    salt_penalty = 1 - salt_alpha * salt_pct
    curing = curing_efficiency

    mpa = density * mineral * cohesion * curing * water_penalty * salt_penalty
    return round(mpa * 5, 2)  # scaled to 0–5 MPa


def hsn_modulus_gpa(
    lime_fraction,
    sand_fraction,
    compaction_energy,
    water_ratio
):
    """
    Modulus model:
    - Mineral fraction increases stiffness.
    - Higher compaction increases stiffness.
    - Water reduces stiffness.
    """
    mineral = lime_fraction + sand_fraction
    density = 0.5 + 0.5 * compaction_energy
    water_penalty = 1 - water_ratio

    gpa = mineral * density * water_penalty * 6  # theoretical max ~6 GPa
    return round(gpa, 2)


# Example: max-GPa recipe parameters
params_strength = {
    "water_ratio": 0.10,
    "salt_pct": 0.02,
    "lime_fraction": 0.98,
    "sand_fraction": 0.98,
    "resin_level": 0.15,
    "protein_level": 0.05,
    "compaction_energy": 0.99,
    "curing_efficiency": 0.95
}

params_modulus = {
    "lime_fraction": 0.98,
    "sand_fraction": 0.98,
    "compaction_energy": 0.99,
    "water_ratio": 0.10
}

mpa = hsn_strength_mpa(**params_strength)
gpa = hsn_modulus_gpa(**params_modulus)

print("HSN Max-GPa MPa Estimate:", mpa)
print("HSN Max-GPa Modulus Estimate (GPa):", gpa)
