# DFT dielectric function of spinel nitrides and doping effects

## Problem background
Spinel nitrides such as γ-SiGe₂N₄ possess wide direct band gaps and are considered promising wide-band-gap semiconductors for optoelectronic applications. However, the optical performance of this family of materials, characterized by the peak value of the imaginary part of the dielectric function (ε₂) and the static dielectric constant (ε₁(0)), is relatively low compared to that of well-established semiconductors. This task investigates, through first-principles density-functional theory (DFT) calculations, whether site-selective substitutional doping with elements from groups IIIA and VA can significantly improve these optical properties, and how the doping affects the electronic structure — in particular, whether the material remains semiconducting or becomes metallic.

## Approach
The approach is based on DFT with the generalized gradient approximation of Perdew, Burke, and Ernzerhof (GGA-PBE) and the random-phase approximation (RPA) for the dielectric response. The workflow consists of building three crystal structures: the undoped γ-SiGe₂N₄ spinel unit cell (space group Fd-3m) and two supercells in which half of the tetrahedral Si atoms are replaced by Ga or As, producing (Si₀.₅Ga₀.₅)Ge₂N₄ and (Si₀.₅As₀.₅)Ge₂N₄ with cubic symmetry (space group F-43m). Each structure is relaxed via DFT geometry optimization. For each relaxed structure, the complex dielectric function ε(ω) is computed on a fine energy grid. The key optical quantities — the maximum ε₂ (peak value), the photon energy at which it occurs, and the static dielectric constant ε₁(0) (the zero-frequency limit of the real part) — are extracted from the spectra. Additionally, the electronic band structure is used to determine whether the Ga-doped system has a zero band gap (i.e., exhibits metallic character).

## Reproduction target
Compute the full frequency-dependent dielectric function (real ε₁ and imaginary ε₂) for the three systems using GGA-PBE DFT and RPA. From the resulting spectra, determine and report, for each system, the peak ε₂ value, its photon energy, and the static dielectric constant ε₁(0). Also report the band gap for the Ga-doped system, explicitly indicating if it is zero (metallic). Submit the raw dielectric spectra as CSV files and a summary of the extracted quantities as a JSON file, all under `/app/outputs`.

## Assets

- Open-source DFT package with GGA-PBE and RPA dielectric function capability (e.g., exciting, GPAW, Quantum ESPRESSO): https://exciting-code.org/
- GGA-PBE pseudopotentials for Si, Ge, N, Ga, As: https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Build and relax undoped γ-SiGe₂N₄
- Role: process
- Action: Construct the spinel unit cell of γ-SiGe₂N₄ (space group Fd-3m, 56 atoms) using standard crystallographic data. Perform DFT geometry optimization (relax cell volume and internal positions) using GGA-PBE until forces are converged.
- Evidence: `/app/outputs/undoped_relaxed_structure.json`

### Step 2: Compute dielectric function for undoped system
- Role: scored (load-bearing)
- Action: Run a self-consistent DFT calculation followed by a dielectric function calculation (RPA) for the relaxed undoped structure. Compute ε₁(ω) and ε₂(ω) on a fine energy grid covering the spectral range where the main peak appears, and save to a CSV file.
- Output file: `/app/outputs/undoped_dielectric.csv`
- Format: csv
- Contract: energy_eV (float), epsilon1 (float), epsilon2 (float)
- Scoring: scored by hidden verifier

### Step 3: Build and relax (Si₀.₅Ga₀.₅)Ge₂N₄ supercell
- Role: process
- Action: Construct the supercell with 50% substitution of the tetrahedral Si atoms by Ga (replace 4 of 8 Si atoms), preserving cubic symmetry (space group F-43m). Perform DFT geometry optimization with the same settings as undoped.
- Evidence: `/app/outputs/ga_relaxed_structure.json`

### Step 4: Compute dielectric function for Ga-doped system
- Role: scored (load-bearing)
- Action: Perform SCF and RPA dielectric function calculation on the relaxed Ga-doped supercell, and save ε₁(ω) and ε₂(ω) to a CSV file.
- Output file: `/app/outputs/Ga_dielectric.csv`
- Format: csv
- Contract: energy_eV (float), epsilon1 (float), epsilon2 (float)
- Scoring: scored by hidden verifier

### Step 5: Build and relax (Si₀.₅As₀.₅)Ge₂N₄ supercell
- Role: process
- Action: Construct the supercell with 50% substitution of tetrahedral Si by As, preserving cubic symmetry. Perform DFT geometry optimization.
- Evidence: `/app/outputs/as_relaxed_structure.json`

### Step 6: Compute dielectric function for As-doped system
- Role: scored (load-bearing)
- Action: Perform SCF and RPA dielectric function calculation on the relaxed As-doped supercell, and save the dielectric spectra to a CSV file.
- Output file: `/app/outputs/As_dielectric.csv`
- Format: csv
- Contract: energy_eV (float), epsilon1 (float), epsilon2 (float)
- Scoring: scored by hidden verifier

### Step 7: Extract peak ε₂ and static constant, assess metallicity
- Role: scored
- Action: From the three dielectric spectra, determine for each system the maximum ε₂ value and its photon energy, and the static dielectric constant ε₁(0) taken as ε₁ at the lowest computed energy. From the electronic band structure (calculated concurrently), determine whether the Ga-doped system is metallic (band gap = 0). Write results to a JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"undoped": {"epsilon2_peak": float, "peak_energy_eV": float, "epsilon1_0": float, "band_gap_eV": float}, "Ga": {"epsilon2_peak": float, "peak_energy_eV": float, "epsilon1_0": float, "band_gap_eV": float}, "As": {"epsilon2_peak": float, "peak_energy_eV": float, "epsilon1_0": float, "band_gap_eV": float}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/undoped_dielectric.csv`
- `/app/outputs/Ga_dielectric.csv`
- `/app/outputs/As_dielectric.csv`
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### undoped_dielectric.csv
- path: `/app/outputs/undoped_dielectric.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Dielectric function for undoped γ-SiGe₂N₄: columns energy_eV (float), epsilon1 (float), epsilon2 (float).
- schema:
  - `type`: table
  - `required_columns`: `energy_eV`, `epsilon1`, `epsilon2`

### Ga_dielectric.csv
- path: `/app/outputs/Ga_dielectric.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Dielectric function for (Si₀.₅Ga₀.₅)Ge₂N₄: columns energy_eV (float), epsilon1 (float), epsilon2 (float).
- schema:
  - `type`: table
  - `required_columns`: `energy_eV`, `epsilon1`, `epsilon2`

### As_dielectric.csv
- path: `/app/outputs/As_dielectric.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Dielectric function for (Si₀.₅As₀.₅)Ge₂N₄: columns energy_eV (float), epsilon1 (float), epsilon2 (float).
- schema:
  - `type`: table
  - `required_columns`: `energy_eV`, `epsilon1`, `epsilon2`

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Extracted optical quantities for the three systems. Each system object contains: epsilon2_peak (float), peak_energy_eV (float), epsilon1_0 (float), band_gap_eV (float, 0 for metallic).
- schema:
  - `type`: object
  - `properties`:
    - `undoped`:
      - `type`: object
      - `required`: `epsilon2_peak`, `peak_energy_eV`, `epsilon1_0`, `band_gap_eV`
    - `Ga`:
      - `type`: object
      - `required`: `epsilon2_peak`, `peak_energy_eV`, `epsilon1_0`, `band_gap_eV`
    - `As`:
      - `type`: object
      - `required`: `epsilon2_peak`, `peak_energy_eV`, `epsilon1_0`, `band_gap_eV`
  - `required`: `undoped`, `Ga`, `As`

Notes: The dielectric CSV files must have a header row. The results.json must be consistent with the peaks and static limits derived from the CSVs; the checker will cross-validate.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "undoped_dielectric.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_eV",
          "epsilon1",
          "epsilon2"
        ]
      },
      "description": "Dielectric function for undoped γ-SiGe₂N₄: columns energy_eV (float), epsilon1 (float), epsilon2 (float)."
    },
    {
      "file": "Ga_dielectric.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_eV",
          "epsilon1",
          "epsilon2"
        ]
      },
      "description": "Dielectric function for (Si₀.₅Ga₀.₅)Ge₂N₄: columns energy_eV (float), epsilon1 (float), epsilon2 (float)."
    },
    {
      "file": "As_dielectric.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_eV",
          "epsilon1",
          "epsilon2"
        ]
      },
      "description": "Dielectric function for (Si₀.₅As₀.₅)Ge₂N₄: columns energy_eV (float), epsilon1 (float), epsilon2 (float)."
    },
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "properties": {
          "undoped": {
            "type": "object",
            "required": [
              "epsilon2_peak",
              "peak_energy_eV",
              "epsilon1_0",
              "band_gap_eV"
            ]
          },
          "Ga": {
            "type": "object",
            "required": [
              "epsilon2_peak",
              "peak_energy_eV",
              "epsilon1_0",
              "band_gap_eV"
            ]
          },
          "As": {
            "type": "object",
            "required": [
              "epsilon2_peak",
              "peak_energy_eV",
              "epsilon1_0",
              "band_gap_eV"
            ]
          }
        },
        "required": [
          "undoped",
          "Ga",
          "As"
        ]
      },
      "description": "Extracted optical quantities for the three systems. Each system object contains: epsilon2_peak (float), peak_energy_eV (float), epsilon1_0 (float), band_gap_eV (float, 0 for metallic)."
    }
  ],
  "notes": "The dielectric CSV files must have a header row. The results.json must be consistent with the peaks and static limits derived from the CSVs; the checker will cross-validate."
}
```

## How you are scored
A hidden verifier independently checks your artifacts after the run. The verifier will:

1. **Cross-consistency**: Verify that the peak values and static constants recorded in `results.json` are consistent with the raw dielectric CSV files (e.g., the maximum ε₂ and its energy match the CSV data, and ε₁(0) corresponds to the low-energy limit of ε₁).
2. **Comparison to reference**: Compare the quantities in `results.json` to hidden reference values (with appropriate tolerances) for the peak ε₂, peak energy, and static dielectric constant of each system.
3. **Trend verification**: Check that the ordering `ε₂ peak(Ga) > ε₂ peak(As) > ε₂ peak(undoped)` holds.
4. **Metallicity check**: Confirm that the Ga-doped system is correctly identified as metallic (band gap reported as 0 eV, or a low-energy ε₂ feature consistent with metallic character).

The final score (a single reward between 0 and 1) is a weighted combination:
- **40%** for agreement of the numeric values with the reference (within tolerance).
- **40%** for satisfying the correct relative ordering of peak ε₂ and the metallicity flag.
- **20%** for internal cross-consistency between the CSV spectra and the JSON summary.

Simply reporting numbers that happen to match the paper is not sufficient; your computation must genuinely produce the dielectric spectra and the derived quantities.
