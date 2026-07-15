# Grand Canonical Monte Carlo Simulation of Hydrogen Adsorption in Carbon Nanotubes

## Problem background
Hydrogen storage is a critical enabler for fuel-cell vehicles, and carbon nanomaterials such as single-walled carbon nanotubes (SWNTs) and graphitic nanofibres with slit-like pores have attracted attention as potential adsorbents. Experimental reports claim hydrogen uptakes of several weight percent in SWNTs, yet many computer simulations that model the gas–solid interaction as purely dispersion forces predict much lower values. This raises the question of whether stronger, chemisorption-like forces between hydrogen and curved graphene surfaces are needed to explain the high experimental uptakes, and whether the internal pore space of a nanotube can ever store as much hydrogen as a slit pore of comparable width under the same force model. The present work uses grand canonical Monte Carlo (GCMC) simulations to address these questions computationally.

## Approach
We model hydrogen as a rigid two-centre Lennard‑Jones dumbbell and consider two gas–solid interaction models: (a) a dispersion-only model in which the interaction between a hydrogen site and the pore wall is obtained by integrating the Lennard‑Jones potential over the surface of the wall — the 10‑4‑3 potential for a slit pore and a corresponding integrated potential for the curved wall of a cylindrical nanotube; (b) a hypothetical chemisorption model (referred to as 'chemisorption 2') that adds a short-range attractive well to the dispersion forces, mimicking a possible re‑hybridization effect. GCMC simulations are run at 298 K for four pore–potential combinations: a slit pore of width 1.2 nm and a SWNT interior of diameter 1.2 nm (both measured between carbon centres) with each of the two force models. Raw adsorption isotherms are recorded up to 100 bar. The raw simulation data (molecules per unit length or per cell) are then converted to total gravimetric uptake (wt%) using the maximum theoretical surface areas: 2680 m² g⁻¹ for the slit pore (two-sided graphene) and 1340 m² g⁻¹ for the internal pore of a SWNT (half the planar value). The main objective is to compare the gravimetric uptakes at 100 bar across the four conditions and to test whether the nanotube interior stores less hydrogen than the slit pore under both force models.

## Reproduction target
Compute the total gravimetric hydrogen uptake (wt%) at 100 bar and 298 K for four systems:
1. SWNT interior (diameter 1.2 nm) with dispersion-only forces.
2. Slit pore (width 1.2 nm) with dispersion-only forces.
3. SWNT interior with the chemisorption‑2 potential.
4. Slit pore with the chemisorption‑2 potential.

Produce the four uptake values in `/app/outputs/simulated_uptakes.json`. The checker will also evaluate structural relationships among the reported values.

## Assets

- RASPA2 molecular simulation package: https://github.com/numat/RASPA2

## Workflow steps

### Step 1: Define gas-solid interaction potentials and pore geometries
- Role: process
- Action: Implement the gas-solid potential for a cylindrical pore (integrated Lennard-Jones for curved walls, with optional chemisorption-2 minimum) and the 10-4-3 slit-pore potential. Use the following parameters: hydrogen modelled as a rigid dumbbell with two Lennard-Jones sites separated by 0.074 nm, σ_HH = 0.259 nm, ε_HH = 12.5 K; carbon σ_CC = 0.340 nm, ε_CC = 28.0 K; cross-interactions via Lorentz-Berthelot mixing rules. Set geometric parameters: nanotube diameter 1.2 nm (distance between carbon centres), slit width 1.2 nm (distance between planes of carbon centres). Graphite density ρ = 114 nm⁻³, interlayer spacing Δ = 0.335 nm.
- Evidence: none

### Step 2: Run GCMC simulations
- Role: process
- Action: Run grand canonical Monte Carlo simulations at 298 K for each of the four pore-potential combinations: (a) SWNT interior with dispersion-only forces, (b) slit pore with dispersion-only forces, (c) SWNT interior with chemisorption-2 potential, (d) slit pore with chemisorption-2 potential. Use a two-site Lennard-Jones dumbbell for H₂, interaction cutoff 2 nm, and at least 5×10⁶ Monte Carlo configurations per condition. Record raw adsorption (number of H₂ molecules per unit length for nanotubes or per simulation cell for slit pores) as a function of pressure up to 100 bar.
- Evidence: `/app/outputs/raw_isotherms.csv`

### Step 3: Compute gravimetric hydrogen uptakes
- Role: scored (load-bearing)
- Action: For each condition, extract the total raw adsorption at 100 bar and convert it to total gravimetric uptake in weight percent (wt%) using the assumed maximum theoretical surface areas: 2680 m² g⁻¹ for the slit pore (two-sided graphene) and 1340 m² g⁻¹ for the internal pore of a SWNT (half the planar value). Write the four values into /app/outputs/simulated_uptakes.json. The four fields are: dispersion_swnt_wt%, dispersion_slit_wt%, chemisorption_swnt_wt%, chemisorption_slit_wt%.
- Output file: `/app/outputs/simulated_uptakes.json`
- Format: json
- Contract: {
  "dispersion_swnt_wt%": <float>,
  "dispersion_slit_wt%": <float>,
  "chemisorption_swnt_wt%": <float>,
  "chemisorption_slit_wt%": <float>
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/simulated_uptakes.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### simulated_uptakes.json
- path: `/app/outputs/simulated_uptakes.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: JSON file containing the four simulated total gravimetric hydrogen uptake values at 100 bar and 298 K, for the four condition combinations. The checker will compare each reported value to the paper-hidden reference with appropriate tolerances and also evaluate structural relationships among the values.
- schema:
  - `type`: object
  - `required`: `dispersion_swnt_wt%`, `dispersion_slit_wt%`, `chemisorption_swnt_wt%`, `chemisorption_slit_wt%`
  - `properties`:
    - `dispersion_swnt_wt%`:
      - `type`: number
      - `description`: Gravimetric uptake (wt%) inside SWNT using dispersion-only forces at 100 bar, 298 K
    - `dispersion_slit_wt%`:
      - `type`: number
      - `description`: Gravimetric uptake (wt%) in a 1.2 nm slit pore using dispersion-only forces at 100 bar, 298 K
    - `chemisorption_swnt_wt%`:
      - `type`: number
      - `description`: Gravimetric uptake (wt%) inside SWNT using chemisorption-2 potential at 100 bar, 298 K
    - `chemisorption_slit_wt%`:
      - `type`: number
      - `description`: Gravimetric uptake (wt%) in a 1.2 nm slit pore using chemisorption-2 potential at 100 bar, 298 K

Notes: The verifier checks the reported uptakes against reference values and enforces certain ordering constraints among the values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "simulated_uptakes.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "dispersion_swnt_wt%",
          "dispersion_slit_wt%",
          "chemisorption_swnt_wt%",
          "chemisorption_slit_wt%"
        ],
        "properties": {
          "dispersion_swnt_wt%": {
            "type": "number",
            "description": "Gravimetric uptake (wt%) inside SWNT using dispersion-only forces at 100 bar, 298 K"
          },
          "dispersion_slit_wt%": {
            "type": "number",
            "description": "Gravimetric uptake (wt%) in a 1.2 nm slit pore using dispersion-only forces at 100 bar, 298 K"
          },
          "chemisorption_swnt_wt%": {
            "type": "number",
            "description": "Gravimetric uptake (wt%) inside SWNT using chemisorption-2 potential at 100 bar, 298 K"
          },
          "chemisorption_slit_wt%": {
            "type": "number",
            "description": "Gravimetric uptake (wt%) in a 1.2 nm slit pore using chemisorption-2 potential at 100 bar, 298 K"
          }
        }
      },
      "description": "JSON file containing the four simulated total gravimetric hydrogen uptake values at 100 bar and 298 K, for the four condition combinations. The checker will compare each reported value to the paper-hidden reference with appropriate tolerances and also evaluate structural relationships among the values."
    }
  ],
  "notes": "The verifier checks the reported uptakes against reference values and enforces certain ordering constraints among the values."
}
```

## How you are scored
A hidden verifier reads the JSON file you write. It compares each of the four reported gravimetric uptakes to a hidden reference with an appropriate tolerance, and it checks certain structural relationships among the reported values. You are not required to match a single exact number; the tolerances account for legitimate code‑to‑code variation. Reward is awarded proportionally: credit is given for each condition whose uptake lies within the tolerance band and for each correct ordering constraint. Meeting all four conditions and both ordering rules yields full credit; partial credit is given for a subset.
