# Silicon Crystal Structure Stability from Tight-Binding Model and Recursion Method

## Problem background
Silicon is a fundamental semiconductor whose phase stability and crystal-structure energetics are critical for understanding phase transitions and for developing atomistic models of defects. This task examines the ability of a simple tight-binding Hamiltonian to predict the relative stability of several silicon crystal structures—diamond, wurtzite, white-tin, and close-packed structures—as a function of atomic volume. The total energy contains a band term (computed by Haydock's recursion method from a Slater-Koster Hamiltonian) and a short-range repulsive pair potential. The model's single free repulsive parameter is fitted by requiring zero pressure at the experimental equilibrium volume of diamond silicon. The resulting energy curves and the equilibrium properties of the diamond phase (cohesive energy, bulk modulus, and s–p mixing ratio) are then obtained.

## Approach
The total binding energy per atom is written as a sum of an attractive band energy and a repulsive pair energy. The tight-binding Hamiltonian uses Chadi's Slater-Koster parameters (on-site energies ε_s, ε_p and hopping integrals V_ssσ, V_spσ, V_ppσ, V_ppπ) with inverse-square scaling of the two-centre matrix elements as a function of bond length. The repulsive pair potential has the form φ(r)=A/r^4, truncated at first neighbours (second neighbours are included for the BCC structure). The repulsive prefactor A is determined by the condition of zero pressure at the experimentally observed diamond lattice constant (5.43 Å). The band energy and its volume derivative are computed using Haydock's scalar recursion method with ten exact moments and a square-root termination. Once A is fixed, the model is applied to six crystal structures: diamond, wurtzite (ideal axial ratio 1.633), white-tin (axial ratio 1.5516, considered in two coordination variants, white‑tin(4) and white‑tin(6)), FCC, and BCC. For each structure the binding energy is calculated over a range of normalized atomic volumes to obtain an energy–volume curve. From the diamond curve, the equilibrium volume is located and the cohesive energy, bulk modulus, and the ratio of p to s orbital occupancy (s–p mixing) are extracted.

## Reproduction target
Produce binding energy versus normalized volume (Ω/Ω₀) curves for diamond, wurtzite, white‑tin(4), white‑tin(6), FCC, and BCC silicon using the described tight-binding model with ten exact moments and a square-root terminator. Use these curves to determine the energetic ordering of the structures (i.e., establish which structure is most stable and the relative ranking among them). From the diamond curve, locate the equilibrium volume (minimum binding energy) and then compute the cohesive energy per atom, the bulk modulus, and the s–p mixing ratio (N_p/N_s) at that equilibrium.

## Assets

- Python 3: python3
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Fit tight-binding model repulsive constant A
- Role: process
- Action: Fit the tight-binding model's repulsive parameter A by requiring zero pressure at the experimental diamond equilibrium atomic volume (lattice constant 5.43 Å). Use Haydock's scalar recursion method with ten exact moments and square-root termination to compute the band energy and its volume derivative. The Hamiltonian uses Chadi's Slater-Koster parameters (hopping integrals V_ssσ, V_spσ, V_ppσ, V_ppπ scaling as r^{-2} and on-site energies ε_s, ε_p) and a repulsive pair potential φ(r)=A/r^4 truncated at first neighbours.
- Evidence: none

### Step 2: Compute binding energy vs volume for all crystal structures
- Role: scored (load-bearing)
- Action: Using the fitted total energy model (repulsive term plus band energy from recursion with ten exact moments), compute the total binding energy per atom as a function of normalized atomic volume Ω/Ω_0 for the crystal structures: diamond, wurtzite (ideal axial ratio 1.633), white-tin (axial ratio 1.5516, coordination 4 and coordination 6, denoted white-tin(4) and white-tin(6)), FCC, and BCC. For BCC, include second-neighbour interactions. Sample at least 10 volume points per structure around the equilibrium region. Write the data to /app/outputs/binding_energies.csv.
- Output file: `/app/outputs/binding_energies.csv`
- Format: csv
- Contract: Columns: structure (string), volume_norm (float), binding_energy (float, eV/atom)
- Scoring: scored by hidden verifier

### Step 3: Extract diamond equilibrium properties
- Role: scored
- Action: From the diamond binding-energy data in binding_energies.csv, locate the equilibrium volume (minimum total binding energy). At that volume compute the cohesive energy per atom, the bulk modulus (by numerical differentiation of pressure with respect to volume, incorporating the repulsive contribution formula), and the s-p mixing ratio (N_p/N_s) from the recursion calculation. Write these to /app/outputs/diamond_properties.json.
- Output file: `/app/outputs/diamond_properties.json`
- Format: json
- Contract: JSON object with keys: cohesive_energy_eV_per_atom (float), bulk_modulus_erg_cm3 (float), s_p_mixing_ratio (float), equilibrium_volume_norm (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binding_energies.csv`
- `/app/outputs/diamond_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binding_energies.csv
- path: `/app/outputs/binding_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Binding energy per atom for each crystal structure as a function of normalized volume. The checker verifies the structural stability ordering diamond < wurtzite < white-tin(4) < fcc, bcc and that the white-tin(4) minimum occurs at a lower normalized volume than diamond's equilibrium.
- schema:
  - `type`: table
  - `required_columns`: `structure`, `volume_norm`, `binding_energy`
  - `units`:
    - `binding_energy`: eV/atom

### diamond_properties.json
- path: `/app/outputs/diamond_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Equilibrium properties of diamond silicon: cohesive energy, bulk modulus, and s-p mixing ratio. The checker compares these to paper-reported reference values with tolerances.
- schema:
  - `type`: object
  - `required`:
    - `cohesive_energy_eV_per_atom`: float
    - `bulk_modulus_erg_cm3`: float
    - `s_p_mixing_ratio`: float
    - `equilibrium_volume_norm`: float
  - `units`:
    - `cohesive_energy_eV_per_atom`: eV/atom
    - `bulk_modulus_erg_cm3`: erg/cm^3

Notes: The agent must implement Haydock's scalar recursion method with ten exact moments and square-root termination. All tight-binding parameters and scaling laws are publicly available. Crystal structures are standard and can be generated algorithmically.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binding_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "structure",
          "volume_norm",
          "binding_energy"
        ],
        "units": {
          "binding_energy": "eV/atom"
        }
      },
      "description": "Binding energy per atom for each crystal structure as a function of normalized volume. The checker verifies the structural stability ordering diamond < wurtzite < white-tin(4) < fcc, bcc and that the white-tin(4) minimum occurs at a lower normalized volume than diamond's equilibrium."
    },
    {
      "file": "diamond_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "cohesive_energy_eV_per_atom": "float",
          "bulk_modulus_erg_cm3": "float",
          "s_p_mixing_ratio": "float",
          "equilibrium_volume_norm": "float"
        },
        "units": {
          "cohesive_energy_eV_per_atom": "eV/atom",
          "bulk_modulus_erg_cm3": "erg/cm^3"
        }
      },
      "description": "Equilibrium properties of diamond silicon: cohesive energy, bulk modulus, and s-p mixing ratio. The checker compares these to paper-reported reference values with tolerances."
    }
  ],
  "notes": "The agent must implement Haydock's scalar recursion method with ten exact moments and square-root termination. All tight-binding parameters and scaling laws are publicly available. Crystal structures are standard and can be generated algorithmically."
}
```

## How you are scored
Your submission is evaluated automatically by a hidden verifier. The verifier inspects the binding energy curves in binding_energies.csv for a specific structural stability ordering (a qualitative trend) and reads the diamond equilibrium properties from diamond_properties.json, comparing them to independently obtained reference values for this model. Each component contributes to the final reward: the structural ordering portion and the property‑agreement portion each carry a separate weight. Producing the correct ordering and numerical values within the expected accuracy is necessary for a high score; merely reporting numbers without running the actual computation will not suffice.
