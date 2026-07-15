# Band gaps and thermoelectric figure of merit of alkali-metal phosphides from DFT

## Problem background
Alkali-metal phosphides MP (M = Li, Na, K) have been investigated as candidate materials for solar energy and thermoelectric applications due to their favorable electronic and thermal properties. This task reproduces the key computational evaluation: determining the band gap type and magnitude (in eV) and the thermoelectric figure of merit (zT) at 300 K for each of the three compounds, using first-principles density functional theory (DFT) and semi-classical Boltzmann transport.

## Approach
The procedure employs all-electron full-potential linearized augmented plane wave (FP-LAPW) calculations using the Elk code, first to relax the crystal structures with the PBEsol generalized gradient approximation (GGA), then to calculate the electronic band structure using the modified Becke-Johnson (mBJ) potential for improved band gap accuracy. From the resulting band energies, semi-classical Boltzmann transport within the constant relaxation time approximation (τ = 1e-14 s) is applied via BoltzTraP2 to obtain the electrical conductivity, Seebeck coefficient, and electronic thermal conductivity. The thermoelectric figure of merit zT = σ S² T / κₑ is evaluated at T = 300 K for each compound.

## Reproduction target
You are to compute, for each compound (LiP, NaP, KP), the band gap (in eV), whether it is direct or indirect, and the thermoelectric figure of merit zT at 300 K, following the workflow described below. The results must be written to /app/outputs/results.json as a JSON object with keys "LiP", "NaP", "KP", each holding an object with fields "band_gap", "gap_type", and "zT_300K".

## Assets

- Elk FP-LAPW code: https://elk.sourceforge.net/
- BoltzTraP2: https://www.boltztrap.org/
- Python with NumPy: numpy

## Workflow steps

### Step 1: Structural relaxation
- Role: process
- Action: Build initial crystal structures of LiP (monoclinic P2₁/c), NaP and KP (orthorhombic P2₁2₁2₁) using the paper's reported lattice constants. Perform structural relaxation using PBEsol-GGA in Elk to obtain optimized geometries.
- Evidence: `/app/outputs/relaxation.log`

### Step 2: mBJ electronic structure
- Role: process
- Action: For each relaxed compound, perform an all-electron FP-LAPW calculation with the modified Becke-Johnson (mBJ) exchange-correlation potential to obtain band energies and character. Determine the band gap and whether it is direct or indirect.
- Evidence: `/app/outputs/mbj_electronic.log`

### Step 3: BoltzTraP transport
- Role: process
- Action: Using the mBJ band structure, run BoltzTraP (or BoltzTraP2) to compute electrical conductivity, Seebeck coefficient, and electronic thermal conductivity as a function of temperature. Use a constant relaxation time τ = 1e-14 s.
- Evidence: `/app/outputs/boltztrap.log`

### Step 4: Band gaps and zT
- Role: scored (load-bearing)
- Action: Extract the band gap value and gap type from the mBJ calculation. From the BoltzTraP transport coefficients, compute the thermoelectric figure of merit at T = 300 K using zT = σ S² T / κₑ (with κₑ the electronic thermal conductivity). Write a single JSON file with the results for LiP, NaP, and KP.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys "LiP", "NaP", "KP". Each value: {"band_gap": float (eV), "gap_type": "direct" or "indirect", "zT_300K": float}.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Band gap type, value, and thermoelectric figure of merit at 300 K for LiP, NaP, and KP.
- schema:
  - `type`: object
  - `required`:
    - `LiP`:
      - `type`: object
      - `required`:
        - `band_gap`: number (eV)
        - `gap_type`: string ("direct" or "indirect")
        - `zT_300K`: number
    - `NaP`:
      - `type`: object
      - `required`:
        - `band_gap`: number (eV)
        - `gap_type`: string ("direct" or "indirect")
        - `zT_300K`: number
    - `KP`:
      - `type`: object
      - `required`:
        - `band_gap`: number (eV)
        - `gap_type`: string ("direct" or "indirect")
        - `zT_300K`: number

Notes: The hidden checker compares the agent's reported band gap, gap type, and zT against the paper’s reference values within published tolerances. The task reproduces the main headline numerical results (band gaps and zT) from a compute-driven DFT workflow. Omitted stages: phonon stability, optical properties, lattice thermal conductivity – those are not headlined in the abstract and are outside this task’s scope.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "LiP": {
            "type": "object",
            "required": {
              "band_gap": "number (eV)",
              "gap_type": "string (\"direct\" or \"indirect\")",
              "zT_300K": "number"
            }
          },
          "NaP": {
            "type": "object",
            "required": {
              "band_gap": "number (eV)",
              "gap_type": "string (\"direct\" or \"indirect\")",
              "zT_300K": "number"
            }
          },
          "KP": {
            "type": "object",
            "required": {
              "band_gap": "number (eV)",
              "gap_type": "string (\"direct\" or \"indirect\")",
              "zT_300K": "number"
            }
          }
        }
      },
      "description": "Band gap type, value, and thermoelectric figure of merit at 300 K for LiP, NaP, and KP."
    }
  ],
  "notes": "The hidden checker compares the agent's reported band gap, gap type, and zT against the paper’s reference values within published tolerances. The task reproduces the main headline numerical results (band gaps and zT) from a compute-driven DFT workflow. Omitted stages: phonon stability, optical properties, lattice thermal conductivity – those are not headlined in the abstract and are outside this task’s scope."
}
```

## How you are scored
A hidden verifier will compare your reported band gap, gap type, and zT for each compound against independent reference values. The score is the fraction of compounds for which all three reported quantities meet the verifier's criteria. Performing the required computations correctly is essential; merely guessing or fabricating the final numbers will not reliably yield the correct answers.
