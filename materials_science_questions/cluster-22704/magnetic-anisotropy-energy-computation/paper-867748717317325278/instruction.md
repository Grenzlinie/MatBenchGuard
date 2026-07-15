# Site-Dependent Magnetic Anisotropy and Spin Excitations of Fe Adatoms on Pt(111)

## Problem background
Single Fe atoms adsorbed on a Pt(111) surface can occupy two distinct hollow sites (fcc and hcp). The magnetic anisotropy energy (MAE) and the resulting spin excitation spectra measured by inelastic tunneling spectroscopy can differ strongly between these sites. Understanding how the binding site influences the MAE and the field dependence of the spin excitation energy is crucial for controlling magnetic properties at the atomic scale. The goal of this task is to compute the MAE from first principles and to model the corresponding spin excitation behavior, revealing the site-dependent magnetic anisotropy.

## Approach
The core of this reproduction is a two-stage computational pipeline: first, density functional theory (DFT) calculations with spin–orbit coupling (SOC) are performed to obtain the total energies of a single Fe adatom on a Pt(111) surface at both fcc and hcp hollow sites, with magnetization aligned either out-of-plane or in-plane. The MAE is then extracted as E_a = E(out-of-plane) – E(in-plane) and converted to the effective spin Hamiltonian anisotropy parameter D via D = E_a / (J(J+1)) with J = 5/2. Convergence of the DFT calculations must ensure that the substrate polarization cloud is adequately described; this typically requires a sufficiently large Pt slab or cluster. In the second stage, the extracted D values are used in the effective spin Hamiltonian H = D J_z^2 + g μ_B B J_z (with g = 2.0) to compute the lowest spin excitation energy as a function of an out-of-plane magnetic field B ranging from 0 to 12 T. The qualitative field dependence of the excitation energy—linear increase or plateau-then-linear—provides information about the sign of D and the easy-axis orientation.

## Reproduction target
For both fcc and hcp hollow sites, compute the magnetic anisotropy energy (MAE) using DFT+SOC and report the resulting spin Hamiltonian parameter D. Then, using the derived D values, simulate the field-dependent lowest spin excitation energy for each site over an out-of-plane magnetic field range of 0–12 T (in steps of 0.1 T). The key output is the qualitative field dependence of the excitation energy for each site, from which the easy-axis classification can be inferred.

## Assets

- Fe on Pt(111) atomic structure
- Quantum ESPRESSO (open-source DFT code with SOC): https://www.quantum-espresso.org/
- SSSP pseudopotentials for Pt and Fe: https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: DFT+SOC total-energy calculations
- Role: process
- Action: Build slab/supercell models for a single Fe adatom on Pt(111) at fcc and hcp hollow sites. Perform DFT calculations using a code supporting spin-orbit coupling (e.g., Quantum ESPRESSO) for both out-of-plane and in-plane magnetization directions. Converge the total energies with respect to slab thickness, k-point mesh, and energy cutoffs.
- Evidence: `/app/outputs/dft_total_energies.json`

### Step 2: Extract MAE and derive spin Hamiltonian D
- Role: scored (load-bearing)
- Action: From the DFT total energies, compute the magnetic anisotropy energy as E_a = E(out-of-plane) – E(in-plane) for the fcc and hcp sites. Convert to the effective spin Hamiltonian anisotropy parameter via D = E_a / [J(J+1)] with J = 5/2. Report the site, E_a (meV), D (meV), and the easy-axis classification.
- Output file: `/app/outputs/step_01_MAE_results.json`
- Format: json
- Contract: JSON array of exactly two objects with keys: site (string: 'fcc' or 'hcp'), E_a_meV (float, signed MAE in meV), D_meV (float, D = E_a / (J(J+1)) with J=5/2), easy_axis (string: 'out-of-plane' if E_a < 0, 'easy-plane' if E_a > 0).
- Scoring: scored by hidden verifier

### Step 3: Field-dependent spin excitation energy simulation
- Role: scored (load-bearing)
- Action: Using the D values from step_02 and J=5/2, construct the effective spin Hamiltonian H = D J_z^2 + g μ_B B J_z with g=2.0. Diagonalize H for an out-of-plane magnetic field B from 0 to 12 T in steps of 0.1 T. For each field, compute the lowest excitation energy (E₁ – E₀) and record it for both fcc and hcp sites.
- Output file: `/app/outputs/step_02_field_excitation_energy.csv`
- Format: csv
- Contract: CSV with columns: site (fcc/hcp), B_T (float, 0 to 12 in 0.1 T steps), excitation_energy_meV (float). Rows for all fields for each site.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_MAE_results.json`
- `/app/outputs/step_02_field_excitation_energy.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_MAE_results.json
- path: `/app/outputs/step_01_MAE_results.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Derived magnetic anisotropy energy and spin Hamiltonian parameter D for Fe on fcc and hcp sites. Scoring verifies the sign of D matches the reported easy-axis classification and that D_fcc < 0 (out-of-plane) and D_hcp > 0 (easy-plane).
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `site`:
        - `type`: string
        - `enum`: `fcc`, `hcp`
      - `E_a_meV`:
        - `type`: number
      - `D_meV`:
        - `type`: number
      - `easy_axis`:
        - `type`: string
        - `enum`: `out-of-plane`, `easy-plane`
    - `required`: `site`, `E_a_meV`, `D_meV`, `easy_axis`
  - `minItems`: 2
  - `maxItems`: 2

### step_02_field_excitation_energy.csv
- path: `/app/outputs/step_02_field_excitation_energy.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Field-dependent lowest spin excitation energy for fcc and hcp sites computed from the effective spin Hamiltonian. Scoring verifies qualitative trends consistent with the sign of the spin Hamiltonian anisotropy parameter D.
- schema:
  - `type`: table
  - `required_columns`: `site`, `B_T`, `excitation_energy_meV`
  - `units`:
    - `B_T`: T
    - `excitation_energy_meV`: meV

Notes: The task excludes TD-DFT and precessional lifetime/g-factor calculations. The D values from step_02 are used to simulate the excitation energies; the checker recomputes the spin Hamiltonian from the submitted D values to verify the qualitative field dependence.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_MAE_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "site": {
              "type": "string",
              "enum": [
                "fcc",
                "hcp"
              ]
            },
            "E_a_meV": {
              "type": "number"
            },
            "D_meV": {
              "type": "number"
            },
            "easy_axis": {
              "type": "string",
              "enum": [
                "out-of-plane",
                "easy-plane"
              ]
            }
          },
          "required": [
            "site",
            "E_a_meV",
            "D_meV",
            "easy_axis"
          ]
        },
        "minItems": 2,
        "maxItems": 2
      },
      "description": "Derived magnetic anisotropy energy and spin Hamiltonian parameter D for Fe on fcc and hcp sites. Scoring verifies the sign of D matches the reported easy-axis classification and that D_fcc < 0 (out-of-plane) and D_hcp > 0 (easy-plane)."
    },
    {
      "file": "step_02_field_excitation_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "site",
          "B_T",
          "excitation_energy_meV"
        ],
        "units": {
          "B_T": "T",
          "excitation_energy_meV": "meV"
        }
      },
      "description": "Field-dependent lowest spin excitation energy for fcc and hcp sites computed from the effective spin Hamiltonian. Scoring verifies qualitative trends consistent with the sign of the spin Hamiltonian anisotropy parameter D."
    }
  ],
  "notes": "The task excludes TD-DFT and precessional lifetime/g-factor calculations. The D values from step_02 are used to simulate the excitation energies; the checker recomputes the spin Hamiltonian from the submitted D values to verify the qualitative field dependence."
}
```

## How you are scored
A hidden verifier independently scores each scored artifact. For step_02 (MAE and D), the verifier checks that the reported D values are self-consistent with the easy-axis classification (negative D must correspond to 'out-of-plane', positive to 'easy-plane') and that the signs are physically plausible for a converged DFT calculation. For step_03, the verifier recomputes the spin excitation energies using your submitted D values and g=2.0, and verifies the qualitative trends: the excitation energy as a function of magnetic field should exhibit a monotonic increase for sites with out-of-plane easy axis, and a low-field plateau (near-zero slope) followed by a linear increase after a critical field for sites with easy-plane anisotropy. The exact numerical values are not required to match any specific publication; only the structural trends and sign consistency are scored. The final reward is a weighted combination of the checks on both artifacts.
