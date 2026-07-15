# Ionic Liquid Lattice Energy and Ion Volume Calculation by DFT

## Problem background
Ionic liquids are salts that melt below 100 °C, and understanding the solid‑state interactions that govern their low melting points is an active area of research. For 1,3‑dialkylimidazolium hexafluorophosphate salts, the crystal packing and lattice energetics have been studied by X‑ray crystallography and by computational estimation of ion volumes and lattice energies. The computational part of this work demonstrates that crystal density and lattice energetics can be predicted from the free‑ion volumes of the isolated ions, without requiring the crystal structures themselves. This task reproduces that computational analysis.

## Approach
The method proceeds in three stages. First, gas‑phase geometries of the [PF₆]⁻ anion and nine 1,3‑dialkylimidazolium cations are optimized using density functional theory at the B3LYP/DZVP2 level. Second, for each optimized ion the volume enclosed by the 0.001 au electron density isosurface is computed and converted to nm³. Third, the free‑ion volumes are used in the Jenkins volume‑based approach: for a salt [cation][PF₆] the total molecular volume V = V_cation + V_anion is used to calculate the lattice energy U_L = 2 × (117.3 × V^(−1/3) + 51.9) kJ·mol⁻¹. The lattice enthalpy is obtained by adding a small temperature correction (ΔH_L = U_L + 5.0 kJ·mol⁻¹), and the lattice free energy is calculated as ΔG_L = ΔH_L − 298 × (1360 × V + 15)/1000 kJ·mol⁻¹. This provides a quantitative estimate of solid‑state energetics for the whole series of salts.

## Reproduction target
Compute the free‑ion volumes (0.001 au electron density isosurface) for the [PF₆]⁻ anion and the nine 1,3‑dialkylimidazolium cations specified in the workflow (cations 1–9). Then use these volumes to calculate, for each salt [cation][PF₆], the lattice energy U_L, the lattice enthalpy ΔH_L, and the lattice free energy ΔG_L at 298 K. Collect all ion volumes and lattice energetics in a single JSON file as described in the output contract. Your computed results will be evaluated against reference data held by the hidden verifier.

## Assets

- Quantum chemistry software (e.g., ORCA, Psi4, NWChem)
- DZVP2 basis set
- RDKit (optional structure builder): rdkit

## Workflow steps

### Step 1: DFT optimization of isolated ions
- Role: process
- Action: Construct initial 3D structures for the [PF₆]⁻ anion and nine 1,3-dialkylimidazolium cations: 1‑methyl‑3‑methylimidazolium (labeled '1'), 1‑ethyl‑3‑methylimidazolium ('2'), 1‑ethyl‑2,3‑dimethylimidazolium ('3'), 1‑ethyl‑2,3,4,5‑tetramethylimidazolium ('4'), 1‑butyl‑3‑methylimidazolium ('5'), 1‑sec‑butyl‑3‑methylimidazolium ('6'), 1‑tert‑butyl‑3‑methylimidazolium ('7'), 1‑butyl‑2,3‑dimethylimidazolium ('8'), 1,3‑di(isopropyl)imidazolium ('9'). Perform gas‑phase geometry optimization at the B3LYP/DZVP2 level. Compute vibrational frequencies to verify local minima and obtain electron density grids.
- Evidence: `/app/outputs/dft_optimization.log`

### Step 2: Ion volume calculation
- Role: process
- Action: For each optimized ion, compute the volume enclosed by the 0.001 au electron density isosurface. Convert volumes to nm³ and record them in a text file.
- Evidence: `/app/outputs/ion_volumes.txt`

### Step 3: Lattice energy estimation and final results
- Role: scored (load-bearing)
- Action: For each salt [cation][PF₆], sum the cation and anion volumes to obtain total molecular volume V (nm³). Compute lattice energy U_L = 2 × (117.3 × V^(−1/3) + 51.9) kJ·mol⁻¹, lattice enthalpy ΔH_L = U_L + 5.0 kJ·mol⁻¹, lattice free energy ΔG_L = ΔH_L − 298 × (1360 × V + 15)/1000 kJ·mol⁻¹. Assemble the anion volume, all cation volumes, and the computed lattice energies/enthalpies/free energies into a JSON file.
- Output file: `/app/outputs/computed_results.json`
- Format: json
- Contract: JSON object with keys: 'anion_volume_nm3' (number), 'cation_volumes_nm3' (object mapping cation label strings '1'…'9' to numbers), 'lattice_energies_kJmol' (object mapping cation label strings to objects with numeric fields 'UL', 'dHL', 'dGL'). All volumes in nm³, energies in kJ·mol⁻¹.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_results.json
- path: `/app/outputs/computed_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Contains the computed anion volume, cation volumes for cations 1-9, and the lattice energies, enthalpies, and free energies for each salt. The checker will recompute lattice energies from the submitted volumes and compare against hidden reference values; it will also compute the R² between submitted cation volumes and hidden experimental cation volumes.
- schema:
  - `type`: object
  - `required`: `anion_volume_nm3`, `cation_volumes_nm3`, `lattice_energies_kJmol`
  - `properties`:
    - `anion_volume_nm3`:
      - `type`: number
    - `cation_volumes_nm3`:
      - `type`: object
      - `patternProperties`:
        - `^[1-9]$`:
          - `type`: number
      - `additionalProperties`: False
    - `lattice_energies_kJmol`:
      - `type`: object
      - `patternProperties`:
        - `^[1-9]$`:
          - `type`: object
          - `required`: `UL`, `dHL`, `dGL`
          - `properties`:
            - `UL`:
              - `type`: number
            - `dHL`:
              - `type`: number
            - `dGL`:
              - `type`: number
      - `additionalProperties`: False

Notes: The checker uses the Jenkins formulas (1)-(3) from the paper to recalculate lattice energies from the submitted ion volumes. It compares the recalculated energies against hidden paper gold values and also checks the correlation between submitted and experimental cation volumes. No pass threshold is given here; scoring is based on tolerances and correlation criteria hidden in the grading specification.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "anion_volume_nm3",
          "cation_volumes_nm3",
          "lattice_energies_kJmol"
        ],
        "properties": {
          "anion_volume_nm3": {
            "type": "number"
          },
          "cation_volumes_nm3": {
            "type": "object",
            "patternProperties": {
              "^[1-9]$": {
                "type": "number"
              }
            },
            "additionalProperties": false
          },
          "lattice_energies_kJmol": {
            "type": "object",
            "patternProperties": {
              "^[1-9]$": {
                "type": "object",
                "required": [
                  "UL",
                  "dHL",
                  "dGL"
                ],
                "properties": {
                  "UL": {
                    "type": "number"
                  },
                  "dHL": {
                    "type": "number"
                  },
                  "dGL": {
                    "type": "number"
                  }
                }
              }
            },
            "additionalProperties": false
          }
        }
      },
      "description": "Contains the computed anion volume, cation volumes for cations 1-9, and the lattice energies, enthalpies, and free energies for each salt. The checker will recompute lattice energies from the submitted volumes and compare against hidden reference values; it will also compute the R² between submitted cation volumes and hidden experimental cation volumes."
    }
  ],
  "notes": "The checker uses the Jenkins formulas (1)-(3) from the paper to recalculate lattice energies from the submitted ion volumes. It compares the recalculated energies against hidden paper gold values and also checks the correlation between submitted and experimental cation volumes. No pass threshold is given here; scoring is based on tolerances and correlation criteria hidden in the grading specification."
}
```

## How you are scored
A hidden verifier will inspect the `computed_results.json` file you produce. The verifier checks that the lattice energies, enthalpies, and free energies are consistent with the reference values within accepted tolerances, and that the computed cation volumes are physically sensible relative to hidden experimental volumes. The verifier may also recompute the lattice energies from your submitted volumes to ensure internal consistency. Each scoring stage carries a weight, and your final reward is a combination of these checks. You must execute the full DFT and volume‑based evaluation workflow; simply supplying a known numeric result will not yield a passing score.
