# Graphene Kohn Anomaly Slope Calculation via DFT/DFPT

## Problem background
In metallic systems, phonon frequencies can exhibit sharp kinks known as Kohn anomalies, caused by electronic screening at the Fermi surface. Graphene, a single layer of carbon atoms, shows two such anomalies in its highest optical phonon branches: one at the Brillouin zone centre (Γ, associated with the E₂g mode) and one at the zone corner (K, associated with the A'₁ mode). The linear slopes of these anomalies are determined by the electron-phonon coupling (EPC) and the electronic band structure near the Fermi level. This task reproduces the determination of those slopes for graphene, which are essential for understanding the vibrational and Raman properties of carbon-based materials.

## Approach
Density functional theory (DFT) and density functional perturbation theory (DFPT) are used to compute the phonon dispersion of graphene, including the electron-phonon coupling matrix elements and the electronic band structure. From these calculations one obtains the Fermi-surface averaged squared EPC for the relevant optical modes and the slope β of the π and π* bands near the K point. The Kohn anomaly slopes are then obtained via analytical relations that connect them to the EPC averages and β. The workflow therefore involves two stages: (1) a first-principles calculation that provides the phonon frequencies, coupling strengths, and band slope, and (2) an evaluation stage that computes the two slope values from the derived quantities.

## Reproduction target
Produce the Kohn anomaly slope of the highest optical phonon branch at Γ (α_Γ^LO) and the slope at K (α_K) for graphene, in wavenumber units (cm⁻¹). The values must be reported as integers in the designated output file.

## Assets

- Quantum ESPRESSO (PWscf): https://www.quantum-espresso.org
- Troullier-Martins pseudopotential for carbon: https://www.quantum-espresso.org/pseudopotentials/

## Workflow steps

### Step 1: DFT ground-state and DFPT phonon calculation for graphene
- Role: process
- Action: Perform a density functional theory (DFT) ground-state calculation and density functional perturbation theory (DFPT) phonon calculation for a graphene unit cell. Use a suitable pseudopotential and a plane-wave basis to obtain the phonon frequencies and electron-phonon coupling matrix elements for the highest optical branches at the Γ and K points, and the electronic band structure, in particular the slope β of the π and π* bands near K. Produce a file containing the phonon dispersion data.
- Evidence: `/app/outputs/graphene_phonon_dispersion.dat`

### Step 2: Compute Kohn anomaly slopes
- Role: scored (load-bearing)
- Action: From the DFPT outputs, extract the Fermi-surface averaged squared electron-phonon coupling (EPC) for the Γ-E₂g mode and the K-A'₁ mode, and the electronic band slope β. Using the analytical relations that express the Kohn anomaly (KA) slopes in terms of the EPC averages and β, compute the KA slopes α_Γ^LO and α_K (in cm⁻¹), and report the integer values.
- Output file: `/app/outputs/ka_slopes.json`
- Format: json
- Contract: { "alpha_Gamma_LO": "integer", "alpha_K": "integer" }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ka_slopes.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ka_slopes.json
- path: `/app/outputs/ka_slopes.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The computed Kohn anomaly slopes for graphene at Γ (LO branch) and K (A'₁ mode), reported in cm⁻¹ as integers.
- schema:
  - `type`: object
  - `required`:
    - `alpha_Gamma_LO`: integer
    - `alpha_K`: integer

Notes: The process step produces a phonon dispersion data file as evidence. The scored step yields the two KA slopes; the checker will compare them to the hidden paper-reported values with a permissive tolerance to account for DFT implementation differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ka_slopes.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "alpha_Gamma_LO": "integer",
          "alpha_K": "integer"
        }
      },
      "description": "The computed Kohn anomaly slopes for graphene at Γ (LO branch) and K (A'₁ mode), reported in cm⁻¹ as integers."
    }
  ],
  "notes": "The process step produces a phonon dispersion data file as evidence. The scored step yields the two KA slopes; the checker will compare them to the hidden paper-reported values with a permissive tolerance to account for DFT implementation differences."
}
```

## How you are scored
A hidden verifier will read your `/app/outputs/ka_slopes.json`, extract the two slope values, and compare them to reference results that represent the expected physical outcome of the computation. The reward is based on the accuracy of the reported slopes; values that are sufficiently close to the reference earn full credit, with partial credit assigned for larger deviations. Simply reporting numbers that appear in the problem statement is not sufficient—the verifier expects results derived from a genuine DFT/DFPT calculation.
