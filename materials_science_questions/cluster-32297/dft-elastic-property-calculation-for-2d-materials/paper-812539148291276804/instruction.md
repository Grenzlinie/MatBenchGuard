# DFT Calculation of Magnetic and Electronic Properties of Alkali‑Based Chromium Chalcogenide Monolayers

## Problem background
Two-dimensional intrinsic ferromagnetic semiconductors (FMSs) are promising candidates for spintronic devices. This task investigates monolayer alkali-based chromium chalcogenides XCrY₂ (X=Li,Na; Y=S,Se,Te). First-principles density functional theory (DFT) calculations are used to predict the magnetic ground state, exchange interactions, Curie temperatures, electronic band gaps, and carrier mobilities. The goal is to determine these physical properties through a computational workflow and report the numerical values for comparison against independently known references.

## Approach
The reproduction follows a DFT + Monte Carlo simulation chain. Starting from experimental bulk crystal structures, monolayer geometries are cleaved and optimized using the HSE06 hybrid functional (with van der Waals corrections). From the relaxed structures, total energies are computed for ferromagnetic (FM) and antiferromagnetic (AFM) collinear spin configurations in a p(2×2) supercell. The nearest-neighbor exchange coupling J is extracted from the energy difference using an Ising model relation with spin S=3/2. Magnetocrystalline anisotropy energy (MAE) is obtained from non-collinear HSE06 calculations. Using J and MAE, Monte Carlo simulations are run on a triangular lattice with both Ising (exchange-only) and Heisenberg (including single-ion anisotropy) Hamiltonians to obtain Curie temperatures. For selected materials, HSE06 band structures are computed without and with spin‑orbit coupling (SOC) to extract the band gap and its direct/indirect character. Finally, strained-cell HSE06 calculations for Na-based monolayers yield 2D elastic moduli, deformation potentials, and effective masses, from which hole mobilities are derived via the deformation-potential method at 300 K. All numerical results are aggregated into a single JSON file.

## Reproduction target
Execute the full computational pipeline described in the Workflow steps below. Produce a file `/app/outputs/results.json` containing the following quantities:

- Nearest-neighbor exchange coupling J (meV) for all six monolayers: LiCrS₂, LiCrSe₂, LiCrTe₂, NaCrS₂, NaCrSe₂, NaCrTe₂.
- Curie temperatures Tc (K) from both the Ising model and the Heisenberg model for the same six monolayers.
- HSE06 band gaps (eV) without and with spin‑orbit coupling for LiCrSe₂, NaCrSe₂, and NaCrTe₂.
- Hole mobilities (cm² V⁻¹ s⁻¹) in the x (zigzag) and y (armchair) directions for NaCrS₂, NaCrSe₂, and NaCrTe₂.

The results.json must follow the exact structure specified in the Output contract section.

## Assets

- Bulk crystal structures of XCrY₂ (X=Li,Na; Y=S,Se,Te)
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Monte Carlo simulation code

## Workflow steps

### Step 1: Structure preparation and geometry optimization
- Role: process
- Action: Retrieve experimental bulk structures for LiCrS₂, LiCrSe₂, LiCrTe₂, NaCrS₂, NaCrSe₂, NaCrTe₂ from public databases or literature. Cleave monolayers from the (001) plane. Relax the monolayers sequentially with PBE+U and then with HSE06 functional, converging forces and energy to tight thresholds. Include van der Waals corrections and sufficient vacuum.
- Evidence: `/app/outputs/geometry_optimisation_logs`

### Step 2: Magnetic energy calculations and exchange coupling J
- Role: process
- Action: Construct p(2×2) supercells of the HSE‑relaxed monolayers. Set up collinear FM and AFM spin configurations. Perform HSE06 single‑point calculations to obtain total energies E_FM and E_AFM. Extract the nearest‑neighbour exchange coupling J (meV) for each material using the Ising model relations E_FM = 12 J S², E_AFM = –4 J S² with S=3/2.
- Evidence: `/app/outputs/FM_AFM_total_energies.txt`

### Step 3: MAE calculation
- Role: process
- Action: For each monolayer, perform HSE06 non‑collinear calculations with spin directions aligned in‑plane and out‑of‑plane. Compute the magnetocrystalline anisotropy energy MAE = E_in‑plane – E_out‑of‑plane (meV).
- Evidence: `/app/outputs/mae_values.txt`

### Step 4: Monte Carlo Curie temperature simulation
- Role: process
- Action: Using the extracted J values and MAE values, run Markov‑chain Monte Carlo simulations on an 80×80 triangular lattice with both the Ising Hamiltonian (J only) and the Heisenberg Hamiltonian including single‑ion anisotropy (MAE). Equilibrate and sample sufficiently long to determine Curie temperatures Tc (K) from the temperature‑dependent magnetisation.
- Evidence: `/app/outputs/tc_transition_data`

### Step 5: HSE06 band structure calculation
- Role: process
- Action: For LiCrSe₂, NaCrSe₂, and NaCrTe₂, compute HSE06 band structures along high‑symmetry paths without and with spin‑orbit coupling (SOC). Extract the band gap (minimum energy gap) in eV, noting whether the gap is direct (VBM and CBM at the same k‑point) or indirect.
- Evidence: `/app/outputs/band_structure_data`

### Step 6: Strained‑cell DFT and hole mobility prerequisites
- Role: process
- Action: For NaCrS₂, NaCrSe₂, NaCrTe₂, perform HSE06 calculations under small uniaxial strains in the zigzag (x) and armchair (y) directions. Record total energy vs strain to obtain the 2D elastic modulus, the shift of the valence band maximum to obtain the deformation potential, and the effective masses of holes at the VBM along x and y from the unstrained band structure.
- Evidence: `/app/outputs/strained_cell_data`

### Step 7: Final analysis and result packaging
- Role: scored (load-bearing)
- Action: Compile the nearest‑neighbour exchange coupling J (meV) for all six materials; Ising and Heisenberg Curie temperatures Tc (K) for all six; HSE06 band gaps (eV) without and with SOC for LiCrSe₂, NaCrSe₂, NaCrTe₂; and hole mobilities (cm²/V/s) in the x (zigzag) and y (armchair) directions for NaCrS₂, NaCrSe₂, NaCrTe₂ computed via the deformation‑potential method at 300 K. Write everything to a single JSON file `results.json` with the exact structure described in the output contract.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {
  "J_values": {
    "LiCrS2": <meV>,
    "LiCrSe2": <meV>,
    "LiCrTe2": <meV>,
    "NaCrS2": <meV>,
    "NaCrSe2": <meV>,
    "NaCrTe2": <meV>
  },
  "Tc_Ising": {
    "LiCrS2": <K>,
    "LiCrSe2": <K>,
    "LiCrTe2": <K>,
    "NaCrS2": <K>,
    "NaCrSe2": <K>,
    "NaCrTe2": <K>
  },
  "Tc_Heisenberg": {
    "LiCrS2": <K>,
    "LiCrSe2": <K>,
    "LiCrTe2": <K>,
    "NaCrS2": <K>,
    "NaCrSe2": <K>,
    "NaCrTe2": <K>
  },
  "band_gaps": {
    "LiCrSe2": {"without_SOC": <eV>, "with_SOC": <eV>},
    "NaCrSe2": {"without_SOC": <eV>, "with_SOC": <eV>},
    "NaCrTe2": {"without_SOC": <eV>, "with_SOC": <eV>}
  },
  "hole_mobilities": {
    "NaCrS2": {"x": <cm2/V/s>, "y": <cm2/V/s>},
    "NaCrSe2": {"x": <cm2/V/s>, "y": <cm2/V/s>},
    "NaCrTe2": {"x": <cm2/V/s>, "y": <cm2/V/s>}
  }
}
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
- target_policy: threshold_or_better
- description: Aggregated reproduction results: exchange coupling J, Ising and Heisenberg Curie temperatures, HSE06 band gaps (without/with SOC), and hole mobilities in x and y directions. Each numerical value is compared against hidden paper‑reported gold values with domain‑appropriate tolerances.
- schema:
  - `type`: object
  - `required`:
    - `J_values`:
      - `LiCrS2`: number (meV)
      - `LiCrSe2`: number (meV)
      - `LiCrTe2`: number (meV)
      - `NaCrS2`: number (meV)
      - `NaCrSe2`: number (meV)
      - `NaCrTe2`: number (meV)
    - `Tc_Ising`:
      - `LiCrS2`: number (K)
      - `LiCrSe2`: number (K)
      - `LiCrTe2`: number (K)
      - `NaCrS2`: number (K)
      - `NaCrSe2`: number (K)
      - `NaCrTe2`: number (K)
    - `Tc_Heisenberg`:
      - `LiCrS2`: number (K)
      - `LiCrSe2`: number (K)
      - `LiCrTe2`: number (K)
      - `NaCrS2`: number (K)
      - `NaCrSe2`: number (K)
      - `NaCrTe2`: number (K)
    - `band_gaps`:
      - `LiCrSe2`:
        - `without_SOC`: number (eV)
        - `with_SOC`: number (eV)
      - `NaCrSe2`:
        - `without_SOC`: number (eV)
        - `with_SOC`: number (eV)
      - `NaCrTe2`:
        - `without_SOC`: number (eV)
        - `with_SOC`: number (eV)
    - `hole_mobilities`:
      - `NaCrS2`:
        - `x`: number (cm²/V/s)
        - `y`: number (cm²/V/s)
      - `NaCrSe2`:
        - `x`: number (cm²/V/s)
        - `y`: number (cm²/V/s)
      - `NaCrTe2`:
        - `x`: number (cm²/V/s)
        - `y`: number (cm²/V/s)
  - `items`: object
  - `required_columns`:
  - `units`: object

Notes: All quantities are defined for 2D XCrY₂ monolayers. The checker applies relative tolerances for J and Tc (≤10%), absolute tolerance for band gaps (≤0.1 eV), and relative tolerance for mobilities (≤20%). The reward is the fraction of individual quantities that lie within tolerance. The agent must follow the described HSE06‑based workflow exactly; approximations or different functionals may shift the values beyond tolerance.

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
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "J_values": {
            "LiCrS2": "number (meV)",
            "LiCrSe2": "number (meV)",
            "LiCrTe2": "number (meV)",
            "NaCrS2": "number (meV)",
            "NaCrSe2": "number (meV)",
            "NaCrTe2": "number (meV)"
          },
          "Tc_Ising": {
            "LiCrS2": "number (K)",
            "LiCrSe2": "number (K)",
            "LiCrTe2": "number (K)",
            "NaCrS2": "number (K)",
            "NaCrSe2": "number (K)",
            "NaCrTe2": "number (K)"
          },
          "Tc_Heisenberg": {
            "LiCrS2": "number (K)",
            "LiCrSe2": "number (K)",
            "LiCrTe2": "number (K)",
            "NaCrS2": "number (K)",
            "NaCrSe2": "number (K)",
            "NaCrTe2": "number (K)"
          },
          "band_gaps": {
            "LiCrSe2": {
              "without_SOC": "number (eV)",
              "with_SOC": "number (eV)"
            },
            "NaCrSe2": {
              "without_SOC": "number (eV)",
              "with_SOC": "number (eV)"
            },
            "NaCrTe2": {
              "without_SOC": "number (eV)",
              "with_SOC": "number (eV)"
            }
          },
          "hole_mobilities": {
            "NaCrS2": {
              "x": "number (cm²/V/s)",
              "y": "number (cm²/V/s)"
            },
            "NaCrSe2": {
              "x": "number (cm²/V/s)",
              "y": "number (cm²/V/s)"
            },
            "NaCrTe2": {
              "x": "number (cm²/V/s)",
              "y": "number (cm²/V/s)"
            }
          }
        },
        "items": {},
        "required_columns": [],
        "units": {}
      },
      "description": "Aggregated reproduction results: exchange coupling J, Ising and Heisenberg Curie temperatures, HSE06 band gaps (without/with SOC), and hole mobilities in x and y directions. Each numerical value is compared against hidden paper‑reported gold values with domain‑appropriate tolerances."
    }
  ],
  "notes": "All quantities are defined for 2D XCrY₂ monolayers. The checker applies relative tolerances for J and Tc (≤10%), absolute tolerance for band gaps (≤0.1 eV), and relative tolerance for mobilities (≤20%). The reward is the fraction of individual quantities that lie within tolerance. The agent must follow the described HSE06‑based workflow exactly; approximations or different functionals may shift the values beyond tolerance."
}
```

## How you are scored
A hidden verifier reads your submitted results.json and compares every numerical value against independantly established reference values for the same quantities. The verifier computes a reward as the fraction of individual values that lie within acceptable tolerances (set separately for each type of quantity). Correctly executing the entire workflow and obtaining physically reasonable numbers is essential; reporting numbers without properly performing the calculations will not satisfy the tolerances. The verifier also checks that the required intermediate evidence files are present and consistent with the claimed pipeline, but the reward is based solely on the correctness of the results.json data.
