"""
HSN MAX-GPa MATERIAL — PROCEDURAL SCRIPT
========================================
This script encodes the instructions for making the
max-stiffness (high-GPa) HSN composite as comments and
prints a concise step-by-step guide when run.

Target:
- Elastic Modulus: up to ~6 GPa (theoretical)
- Compressive Strength: 4–5 MPa (HSN upper band)
"""

def print_hsn_max_gpa_instructions():
    print("HSN MAX-GPa MATERIAL — STEP-BY-STEP\n")

    # 1. MATERIALS (FOR 1 KG BATCH)
    print("1. MATERIALS (1 kg batch)")
    print("   - 480 g hydrated lime")
    print("   - 480 g fine silica sand")
    print("   - 20 g ultra-fine hemp hurds")
    print("   - 15 g cacao resin")
    print("   - 5 g hemp protein powder")
    print("   - 35–50 mL clean water")
    print("   - 4–8 g NaCl (salt), dissolved into the water\n")

    # 2. RATIOS
    print("2. RATIOS (by mass)")
    print("   - Lime: 48%")
    print("   - Sand: 48%")
    print("   - Organics (hurds + resin + protein): 3–4%")
    print("   - Water: 3.5–5%")
    print("   - Salt: 1–2% of binder mass (lime + resin)\n")

    # 3. MIXING
    print("3. MIXING PROCEDURE")
    print("   a) Mix lime + sand for ~90 seconds.")
    print("   b) Add ultra-fine hemp hurds; mix ~60 seconds.")
    print("   c) Add cacao resin + hemp protein; mix ~2 minutes.")
    print("   d) Dissolve salt fully into water (brine), stir 30–45 seconds.")
    print("   e) Add brine slowly over ~2 minutes while mixing.")
    print("   f) Final kneading: 1–2 minutes.")
    print("   Total mixing time: ~6–8 minutes.\n")

    # 4. WATER CONTROL
    print("4. WATER CONTROL")
    print("   - Add water in small increments (5 mL).")
    print("   - Stop when mix is stiff, packable, and non-slumping.")
    print("   - Lower water → higher density → higher modulus.\n")

    # 5. COMPACTION
    print("5. COMPACTION")
    print("   - Fill molds in 3 layers.")
    print("   - Apply 3–4 MPa press pressure OR 40–60 kg manual force per layer.")
    print("   - Hold pressure 15–25 seconds per layer.")
    print("   - Goal: maximum density, minimal voids.\n")

    # 6. CURING
    print("6. CURING")
    print("   Stage 1 — Humid Cure:")
    print("     - 24–48 hours at 70–90% humidity, 18–24°C.")
    print("   Stage 2 — Air Carbonation:")
    print("     - 14–28 days with moderate airflow, 18–26°C.\n")

    # 7. EXPECTED OUTPUT
    print("7. EXPECTED OUTPUT")
    print("   - Elastic Modulus: up to ~6 GPa (theoretical, high-density mineral matrix).")
    print("   - Compressive Strength: 4–5 MPa (HSN upper band).\n")
    print("END OF HSN MAX-GPa INSTRUCTIONS")


if __name__ == "__main__":
    print_hsn_max_gpa_instructions()
