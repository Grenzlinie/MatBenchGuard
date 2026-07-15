# DFT calculation of vacancy-induced magnetism in GaN:Gd

## Problem background
GaN doped with Gd is a dilute magnetic semiconductor that can exhibit ferromagnetism at room temperature with large effective magnetic moments per Gd atom. The microscopic origin of this magnetism is debated because Gd is an isoelectronic dopant and free-carrier-mediated exchange is unlikely. This task uses spin‑polarized density functional theory (DFT) to investigate whether intrinsic defects, such as vacancies, can induce ferromagnetic coupling between Gd ions. The goal is to compute energy differences between ferromagnetic and antiferromagnetic spin arrangements as well as the total magnetic moment contributed per Gd atom in several defect‑containing GaN:Gd supercells.

## Approach
Construct 2×2×2 supercells of GaN (zincblende or wurtzite) in which one Ga atom is replaced by Gd. Introduce four defect environments: a defect‑free reference (GdGa₇N₈), a nitrogen vacancy (GdGa₇N₇), a gallium vacancy (GdGa₆N₈), and a gallium vacancy compensated by two oxygen substitutions on nitrogen sites (GdGa₆N₆O₂). For each structure, perform spin‑polarised DFT calculations with the generalised gradient approximation (GGA-PBE) for exchange‑correlation and an LDA+U treatment for Gd 4f electrons (U = 6.7 eV, J = 0.7 eV). First relax the atomic positions to the energy minimum, then compute the total energy in both the ferromagnetic (FM, all Gd spins aligned) and antiferromagnetic (AFM, alternating spin directions) configurations, and record the total magnetic moment of the FM state. This yields the energy difference ΔE<sub>FM‑AFM</sub> per Gd atom and the FM magnetic moment per Gd atom for each defect case.

## Reproduction target
After completing the DFT calculations, produce a CSV file `/app/outputs/results.csv` with one row for each of the four defect configurations. The CSV must have columns: `configuration` (one of: defect‑free, V_N, V_Ga, V_Ga+O), `E_FM` (total energy of the FM configuration, in eV), `E_AFM` (total energy of the AFM configuration, in eV), and `magnetic_moment_per_Gd` (total magnetic moment of the FM configuration, in μ_B). The reported values should be per supercell (which contains one Gd atom), so they directly represent per‑Gd quantities.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/download
- SSSP efficiency pseudopotentials for Ga, N, Gd, O: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Geometry optimization of all supercells
- Role: process
- Action: Construct 2x2x2 supercells of GaN (zincblende or wurtzite) with one Gd atom substituting a Ga atom, and introduce defects: remove one N for V_N, remove one Ga for V_Ga, replace two N with O for V_Ga+O. For each defect configuration, perform spin-polarized DFT geometry optimization (relaxation) using an open-source DFT code (e.g., Quantum ESPRESSO) with GGA-PBE exchange-correlation and LDA+U (U=6.7 eV, J=0.7 eV) for Gd 4f electrons. Save the optimized atomic positions for each structure.
- Evidence: none

### Step 2: Total energy and magnetic moment calculations
- Role: scored (load-bearing)
- Action: For each optimized supercell (defect-free, V_N, V_Ga, V_Ga+O), perform spin-polarized DFT calculations for both ferromagnetic (FM) and antiferromagnetic (AFM) spin configurations using the same DFT settings. Extract the total energy for each configuration (E_FM, E_AFM) and the total magnetic moment in the FM configuration. Report the values per supercell (one Gd atom per supercell). Write one CSV row per defect configuration.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: configuration: string; E_FM: float; E_AFM: float; magnetic_moment_per_Gd: float
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.csv
- path: `/app/outputs/results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed total energies (in eV) and magnetic moment per Gd atom (in μ_B) for ferromagnetic and antiferromagnetic spin configurations of each defect supercell: defect-free, N-vacancy, Ga-vacancy, and Ga-vacancy with oxygen donors.
- schema:
  - `type`: table
  - `required_columns`: `configuration`, `E_FM`, `E_AFM`, `magnetic_moment_per_Gd`
  - `units`:
    - `E_FM`: eV
    - `E_AFM`: eV
    - `magnetic_moment_per_Gd`: μ_B

Notes: The checker will compute ΔE_FM-AFM = E_FM - E_AFM (in meV) from the reported energies, and verify that the computed values match hidden paper-reported reference values within tolerances appropriate for code/pseudopotential differences. Also verifies structural ordering trends among configurations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "configuration",
          "E_FM",
          "E_AFM",
          "magnetic_moment_per_Gd"
        ],
        "units": {
          "E_FM": "eV",
          "E_AFM": "eV",
          "magnetic_moment_per_Gd": "μ_B"
        }
      },
      "description": "Computed total energies (in eV) and magnetic moment per Gd atom (in μ_B) for ferromagnetic and antiferromagnetic spin configurations of each defect supercell: defect-free, N-vacancy, Ga-vacancy, and Ga-vacancy with oxygen donors."
    }
  ],
  "notes": "The checker will compute ΔE_FM-AFM = E_FM - E_AFM (in meV) from the reported energies, and verify that the computed values match hidden paper-reported reference values within tolerances appropriate for code/pseudopotential differences. Also verifies structural ordering trends among configurations."
}
```

## How you are scored
A hidden verifier reads `results.csv` and computes ΔE = (E_FM − E_AFM)×1000 (in meV/Gd) for each configuration. The verifier compares these derived ΔE values and the reported magnetic moments to hidden reference standards that encode the physically expected behaviour. The comparison uses tolerances appropriate for differences between DFT implementations, and additionally checks that the ordering of ΔE across the four defect configurations follows a physically meaningful pattern. Your final reward (0−1) is a weighted combination of how well your computed quantities match those hidden references and structural relationships. Simply writing plausible numbers without running the actual DFT workflow is unlikely to score well because the hidden references reflect specific quantitative properties of the real GaN:Gd system.
