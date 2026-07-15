# DFT Free Energy Profile for Nitrate Reduction on TiO2 and FePc/TiO2 Surfaces

## Problem background
Electrochemical reduction of nitrate (NO₃⁻) to ammonia (NH₃) is a promising route for sustainable ammonia production and wastewater treatment. Titanium dioxide (TiO₂) nanosheets have been shown to catalyse this reaction selectively under acidic conditions, and hybridising TiO₂ with iron phthalocyanine (FePc) is reported to further improve the catalytic activity. Density functional theory (DFT) calculations are used to understand the reaction mechanism by constructing the Gibbs free energy profile of the NO₃⁻‑to‑NH₃ pathway on anatase TiO₂(101) and FePc/TiO₂(101) surfaces. The key computational question is how the FePc modification changes the free energy landscape and, in particular, which elementary step constitutes the rate‑determining step (RDS) and what its energy barrier is on each surface.

## Approach
You will perform spin‑polarised DFT calculations using the Perdew–Burke–Ernzerhof (PBE) functional with D3 dispersion correction, which is a standard protocol for this class of materials. Two slab models are needed: a clean anatase TiO₂(101) surface and a FePc/TiO₂(101) composite where an FePc molecule is adsorbed on the TiO₂ surface. For each surface, you will compute the total energies of the intermediates along the NO₃⁻ → NH₃ pathway (*NO₃, *NO₂, *NO, *NOH, *NH₂OH, *NH₃) and the necessary gas‑phase reference molecules. Using the computational hydrogen electrode (CHE) scheme, you will then construct the Gibbs free energy diagram at pH 1, identify the potential‑determining (rate‑determining) step, and record its barrier. The final output is a comparison of the free energy profiles and RDS energies between the TiO₂ and FePc/TiO₂ surfaces, revealing the effect of the FePc modification.

## Reproduction target
Using an open‑source plane‑wave DFT code (e.g., Quantum ESPRESSO) with standard PBE pseudopotentials, build the slab models of anatase TiO₂(101) and FePc/TiO₂(101). Compute the Gibbs free energy of every intermediate along the NO₃⁻‑to‑NH₃ pathway at pH 1 for both surfaces. Report the full free energy table and, for each surface, the free energy barrier of the rate‑determining step (RDS) in a CSV file under `/app/outputs/free_energies.csv`. The file must contain one row per intermediate and an `RDS` row per surface stating the barrier height, following the schema described in the workflow steps.

## Assets

- Open-source plane-wave DFT code (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org
- PBE pseudopotentials: https://www.quantum-espresso.org/pseudopotentials
- Anatase TiO2 crystal structure (Materials Project mp-390): https://next-gen.materialsproject.org/materials/mp-390
- Iron phthalocyanine (FePc) molecular structure: https://pubchem.ncbi.nlm.nih.gov/compound/12547212

## Workflow steps

### Step 1: Build and optimize slab models
- Role: process
- Action: Construct anatase TiO2(101) surface slab from the bulk unit cell and create the FePc/TiO2 composite model by adsorbing FePc on the surface. Optimize the geometries using spin‑polarized DFT at the PBE level with dispersion correction.
- Evidence: `/app/outputs/geometry_optim.log`

### Step 2: Compute energies of reaction intermediates
- Role: process
- Action: On both optimized surfaces, adsorb each intermediate of the NO3–→NH3 pathway (*NO3, *NO2, *NO, *NOH, *NH2OH, *NH3) and calculate total energies. Obtain gas‑phase reference energies for constructing a free energy diagram at pH 1 using the computational hydrogen electrode scheme.
- Evidence: `/app/outputs/intermediate_energies.json`

### Step 3: Compile free energy diagram and report RDS energies
- Role: scored (load-bearing)
- Action: From the computed total energies, calculate the Gibbs free energy change for each elementary step, incorporating zero-point energy and entropic corrections if feasible. Construct the free energy diagram for pH 1 on both TiO2(101) and FePc/TiO2(101) surfaces, identify the rate‑determining step, and output the profile including the RDS barrier.
- Output file: `/app/outputs/free_energies.csv`
- Format: csv
- Contract: Columns: surface (string, one of TiO2 or FePc/TiO2), intermediate (string, e.g., *NO3, *NO2, *NO, *NOH, *NH2OH, *NH3, or RDS), free_energy_eV (float, the Gibbs free energy of that intermediate relative to a chosen reference), pH (integer, expected 1), comment (string). Each surface must include an 'RDS' row containing the barrier height of the rate‑determining step.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/free_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### free_energies.csv
- path: `/app/outputs/free_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Free energy profile for nitrate reduction to ammonia on TiO2(101) and FePc/TiO2(101) at pH 1. Contains one row per intermediate and an 'RDS' row per surface stating the barrier height of the rate-determining step.
- schema:
  - `type`: table
  - `required_columns`: `surface`, `intermediate`, `free_energy_eV`, `pH`, `comment`
  - `units`:
    - `free_energy_eV`: eV

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "free_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "surface",
          "intermediate",
          "free_energy_eV",
          "pH",
          "comment"
        ],
        "units": {
          "free_energy_eV": "eV"
        }
      },
      "description": "Free energy profile for nitrate reduction to ammonia on TiO2(101) and FePc/TiO2(101) at pH 1. Contains one row per intermediate and an 'RDS' row per surface stating the barrier height of the rate-determining step."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads `/app/outputs/free_energies.csv`. The verifier extracts the RDS free energy values for TiO₂ and FePc/TiO₂ and scores them in two parts: (1) a quantitative comparison of each RDS energy against a reference value (with an appropriate tolerance), and (2) a structural check that verifies the correct relative ordering of the RDS energies between the two surfaces. The total reward is a weighted combination of these parts; simply producing a correctly formatted file is not sufficient — the computed energies must match the expected physics within tolerance.
