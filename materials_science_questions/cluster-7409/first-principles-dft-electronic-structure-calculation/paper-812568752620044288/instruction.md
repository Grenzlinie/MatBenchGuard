# DFT calculation of electronic, optical, and thermoelectric properties of KCl and K0.5Rb0.5Cl

## Problem background
Alkali halides are of enduring interest for optical windows and thermoelectric applications. Potassium chloride (KCl) is a prototypical system, and substituting rubidium for a fraction of the potassium modifies its structural, electronic, optical, and transport properties. This task investigates those modifications using first‑principles density functional theory (DFT). The aim is to quantify key properties of pure KCl and the alloy K0.5Rb0.5Cl — including lattice constants, bulk moduli, band gaps, dielectric response, and thermoelectric coefficients — to assess how Rb doping alters the material's characteristics. All properties are to be determined computationally with a standard generalized‑gradient‑approximation functional; the comparison of the two compounds provides insight into trends relevant for optoelectronic and thermoelectric device applications.

## Approach
The computational approach relies on plane‑wave or projector‑augmented‑wave DFT within the Perdew–Burke–Ernzerhof (PBE) flavor of the generalized gradient approximation (GGA). Two crystal structures are studied:
- KCl in the cubic rocksalt structure (space group Fm‑3m) with K at (0,0,0) and Cl at (0.5,0.5,0.5).
- K0.5Rb0.5Cl, modeled by a 2×2×2 supercell of the rocksalt lattice (16 atoms) in which four K atoms are replaced by Rb, resulting in the lowered‑symmetry space group Fd‑3m.

For each compound, the total energy is calculated over a range of volumes to fit the Birch–Murnaghan equation of state, yielding the equilibrium lattice constant and bulk modulus. The self‑consistent electronic structure then provides the Kohn–Sham band energies and the total density of states; from these the direct band gap at the Γ point is extracted. The frequency‑dependent complex dielectric function ε(ω) = ε₁(ω) + iε₂(ω) is computed, and the static dielectric constant ε₁(0) is read off the low‑energy limit. Finally, semi‑classical Boltzmann transport theory is applied to the converged band structure to obtain the temperature‑dependent Seebeck coefficient, electrical conductivity, thermal conductivity, and power factor. All quantities are to be obtained with an open‑source DFT code and a publicly available PBE pseudopotential library; the transport post‑processing may use BoltzTraP or an equivalent tool. The workflow compares the pure and Rb‑doped systems, so any trends that emerge are a direct consequence of the substitution and must be captured in the final reported values.

## Reproduction target
Produce a single JSON file, `summary_results.json`, that contains the following computed quantities for both KCl and K0.5Rb0.5Cl:

- lattice_constant_A : float  — equilibrium lattice constant in Å
- bulk_modulus_GPa : float    — bulk modulus in GPa
- band_gap_eV : float         — direct band gap at Γ in eV
- static_dielectric_constant : float — static dielectric constant ε₁(0)
- seebeck_coefficient_300K_uV_per_K : float — Seebeck coefficient at 300 K in μV/K
- power_factor_300K : float   — power factor S²σ/τ at 300 K

The file must be written to `/app/outputs/summary_results.json` with the exact structure shown in the Output contract section below. You must obtain every value by running the full DFT pipeline (structural relaxation → electronic structure → optical response → thermoelectric transport). Submitting values obtained by any other means (e.g., direct copying of reference data) will result in a low or zero score because the hidden verifier checks internal consistency with the computational procedure.

## Assets

- Open-source DFT code (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/
- GGA-PBE pseudopotential library (e.g., SSSP, PseudoDojo): https://www.materialscloud.org/discover/sssp/table/efficiency
- BoltzTraP or equivalent transport code: https://www.boltztrapp.org/

## Workflow steps

### Step 1: Structural optimization and EOS fitting
- Role: process
- Action: Optimize the crystal structures of KCl (Fm-3m) and the K0.5Rb0.5Cl supercell (Fd-3m) using DFT with GGA-PBE. Fit the total energy vs. volume curve to the Birch-Murnaghan equation of state to obtain the equilibrium lattice constant a0 and bulk modulus B.
- Evidence: `/app/outputs/energy_vs_volume.json`

### Step 2: Electronic structure calculation
- Role: process
- Action: Perform SCF calculation, then compute the band structure along high-symmetry k-points and the total density of states. Identify the valence band maximum and conduction band minimum at the Γ point and extract the direct band gap for both compounds.
- Evidence: `/app/outputs/band_structure.json`

### Step 3: Optical properties calculation
- Role: process
- Action: Compute the frequency-dependent dielectric function ε(ω) for photon energies up to at least 13.5 eV, and extract the static dielectric constant ε1(0) (value at ω→0) for both compounds.
- Evidence: `/app/outputs/dielectric_function.json`

### Step 4: Thermoelectric properties calculation
- Role: process
- Action: Compute the temperature-dependent Seebeck coefficient, electrical conductivity, thermal conductivity, and power factor S²σ/τ using Boltzmann transport theory (e.g., BoltzTraP) from the DFT band structure. Record values at 300 K for both compounds.
- Evidence: `/app/outputs/thermoelectric_data.json`

### Step 5: Compile summary results
- Role: scored (load-bearing)
- Action: Gather the key computed quantities from the previous steps: lattice constant a0 (Å), bulk modulus B (GPa), band gap Eg (eV), static dielectric constant ε1(0), Seebeck coefficient at 300 K (μV/K), and power factor at 300 K, for both KCl and K0.5Rb0.5Cl. Write them into summary_results.json.
- Output file: `/app/outputs/summary_results.json`
- Format: json
- Contract: {
  "KCl": {
    "lattice_constant_A": float,
    "bulk_modulus_GPa": float,
    "band_gap_eV": float,
    "static_dielectric_constant": float,
    "seebeck_coefficient_300K_uV_per_K": float,
    "power_factor_300K": float
  },
  "K0.5Rb0.5Cl": {
    "lattice_constant_A": float,
    "bulk_modulus_GPa": float,
    "band_gap_eV": float,
    "static_dielectric_constant": float,
    "seebeck_coefficient_300K_uV_per_K": float,
    "power_factor_300K": float
  }
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/summary_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### summary_results.json
- path: `/app/outputs/summary_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Key computed properties of KCl and K0.5Rb0.5Cl to be compared against paper-reported values with appropriate tolerances.
- schema:
  - `type`: object
  - `required`: `KCl`, `K0.5Rb0.5Cl`
  - `properties`:
    - `KCl`:
      - `type`: object
      - `required`: `lattice_constant_A`, `bulk_modulus_GPa`, `band_gap_eV`, `static_dielectric_constant`, `seebeck_coefficient_300K_uV_per_K`, `power_factor_300K`
      - `properties`:
        - `lattice_constant_A`:
          - `type`: number
        - `bulk_modulus_GPa`:
          - `type`: number
        - `band_gap_eV`:
          - `type`: number
        - `static_dielectric_constant`:
          - `type`: number
        - `seebeck_coefficient_300K_uV_per_K`:
          - `type`: number
        - `power_factor_300K`:
          - `type`: number
    - `K0.5Rb0.5Cl`:
      - `type`: object
      - `required`: `lattice_constant_A`, `bulk_modulus_GPa`, `band_gap_eV`, `static_dielectric_constant`, `seebeck_coefficient_300K_uV_per_K`, `power_factor_300K`
      - `properties`:
        - `lattice_constant_A`:
          - `type`: number
        - `bulk_modulus_GPa`:
          - `type`: number
        - `band_gap_eV`:
          - `type`: number
        - `static_dielectric_constant`:
          - `type`: number
        - `seebeck_coefficient_300K_uV_per_K`:
          - `type`: number
        - `power_factor_300K`:
          - `type`: number

Notes: All quantities must be computed via the DFT pipeline; direct copying of reference values is detectable by the hidden checker. Missing or malformed fields will score zero for that entry.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "summary_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "KCl",
          "K0.5Rb0.5Cl"
        ],
        "properties": {
          "KCl": {
            "type": "object",
            "required": [
              "lattice_constant_A",
              "bulk_modulus_GPa",
              "band_gap_eV",
              "static_dielectric_constant",
              "seebeck_coefficient_300K_uV_per_K",
              "power_factor_300K"
            ],
            "properties": {
              "lattice_constant_A": {
                "type": "number"
              },
              "bulk_modulus_GPa": {
                "type": "number"
              },
              "band_gap_eV": {
                "type": "number"
              },
              "static_dielectric_constant": {
                "type": "number"
              },
              "seebeck_coefficient_300K_uV_per_K": {
                "type": "number"
              },
              "power_factor_300K": {
                "type": "number"
              }
            }
          },
          "K0.5Rb0.5Cl": {
            "type": "object",
            "required": [
              "lattice_constant_A",
              "bulk_modulus_GPa",
              "band_gap_eV",
              "static_dielectric_constant",
              "seebeck_coefficient_300K_uV_per_K",
              "power_factor_300K"
            ],
            "properties": {
              "lattice_constant_A": {
                "type": "number"
              },
              "bulk_modulus_GPa": {
                "type": "number"
              },
              "band_gap_eV": {
                "type": "number"
              },
              "static_dielectric_constant": {
                "type": "number"
              },
              "seebeck_coefficient_300K_uV_per_K": {
                "type": "number"
              },
              "power_factor_300K": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Key computed properties of KCl and K0.5Rb0.5Cl to be compared against paper-reported values with appropriate tolerances."
    }
  ],
  "notes": "All quantities must be computed via the DFT pipeline; direct copying of reference values is detectable by the hidden checker. Missing or malformed fields will score zero for that entry."
}
```

## How you are scored
Your submission is scored by a hidden verifier that reads `/app/outputs/summary_results.json`. Each numeric field (lattice constant, bulk modulus, band gap, static dielectric constant, Seebeck coefficient, and power factor) for each compound is compared against expected values that are derived from a published DFT study employing the same functional (GGA‑PBE). Appropriate tolerances are applied to account for differences due to code choice, pseudopotential library, and numerical parameters; these tolerances are not disclosed. The verifier also checks that the file is well‑formed and that every required field is present. Each field contributes to the total reward with a weight that reflects its importance. Missing or malformed fields receive zero contribution. Because the hidden reference values are unknown to you, the only reliable way to obtain a high reward is to run the complete DFT pipeline as instructed. The final reward is a number in [0,1], with 1 signifying full agreement with the expected results within the allowed margins.
