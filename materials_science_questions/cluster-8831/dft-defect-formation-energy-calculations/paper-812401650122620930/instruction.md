# Ab initio defect structure, formation energy, and local vibrational modes of substitutional BeGa and split-interstitial (Be-Be)Ga in wurtzite GaN

## Problem background
Beryllium doping of gallium nitride (GaN) has been explored as a route to p-type conductivity, but experimental results show poor electrical activity due to strong compensation by native defects and impurity complexes. Density-functional theory (DFT) calculations provide a way to unravel the atomic structures, formation energetics, and local vibrational signatures of Be-related point defects, helping to identify the compensating centers that limit p-type doping. The target of this reproduction is to compute, from first principles, the relaxed bond lengths of the substitutional BeGa acceptor, its formation energy under extreme Ga-rich and N-rich conditions, and the local vibrational mode frequencies that serve as spectroscopic fingerprints for both the BeGa acceptor and the (Be-Be)Ga split-interstitial donor.

## Approach
The reproduction uses self-consistent DFT within the local-density approximation (LDA). The calculations are performed with a plane-wave basis and norm-conserving pseudopotentials; for gallium, a nonlinear core correction (nlcc) is included to approximate the influence of the Ga 3d electrons. A second treatment that explicitly includes Ga 3d electrons in the valence is also used for the neutral BeGa bond-length calculation to assess the quality of the nlcc approximation. Wurtzite GaN is modelled with a 72-atom periodic supercell. The lattice parameters are first optimized for defect-free GaN. Chemical potentials for the formation-energy calculation are obtained from total energies of the reference phases: orthorhombic Ga metal, an isolated N2 molecule, hcp Be metal, and α-Be3N2. Defect formation energies are computed using the standard chemical-potential formalism that relates the total energies of the defect supercell and the reference phases. Local vibrational modes are obtained by constructing the dynamical matrix from finite displacements of selected atoms (the defect atom and its nearest neighbours) and diagonalising it to extract the high-frequency modes localized on the defect. This procedure must be applied to the BeGa acceptor in neutral and −1 charge states, and to the neutral (Be-Be)Ga split-interstitial defect.

## Reproduction target
Using a public open-source DFT code (e.g., Quantum ESPRESSO) with the LDA functional and the pseudopotentials described above, compute and report the following quantities in the specified JSON output files:

1. **BeGa bond lengths** — the four nearest-neighbour Be–N bond lengths (labelled a, b, c, d) of the substitutional BeGa acceptor for three basis/charge combinations: Ga 3d explicit (neutral), nlcc (neutral), and nlcc (charge −1).
2. **BeGa formation energies** — the formation energy E_f(0) of neutral BeGa under Ga-rich and N-rich conditions, using the chemical potentials derived from the reference phase calculations.
3. **BeGa local vibrational modes** — the four highest A1-symmetry local vibrational mode frequencies of neutral BeGa (nlcc basis).
4. **(Be-Be)Ga local vibrational modes** — the three highest local vibrational mode frequencies of the neutral (Be-Be)Ga split-interstitial defect.

The required output schemas and file paths are given in the workflow steps below. All values must be computed from first-principles DFT; the reference data from the original study is used only by the hidden verifier for scoring.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP LDA norm-conserving pseudopotentials with nonlinear core correction (Ga, N, Be): https://www.materialscloud.org/discover/sssp/table/precision

## Workflow steps

### Step 1: Bulk reference and chemical potential calculations
- Role: process
- Action: Perform DFT total-energy calculations for wurtzite GaN (optimise lattice parameters), orthorhombic Ga metal, an isolated N2 molecule, hcp Be metal, and α-Be3N2. Use these to establish the chemical potentials μ_Ga, μ_N, μ_Be and the heats of formation ΔH_f(GaN) and ΔH_f(α-Be3N2). Save the computed total energies and optimised lattice parameters for later steps.
- Evidence: `/app/outputs/bulk_energies.txt`

### Step 2: Be_Ga defect supercell structural relaxation
- Role: process
- Action: Construct a 72‑atom hexagonal GaN supercell with a substitutional Be on a Ga site. Relax the structure in the neutral (q=0) and negative (q=−1) charge states using DFT with the optimised lattice parameters from step_0. Save the relaxed atomic coordinates and total energies.
- Evidence: `/app/outputs/bega_relax_log.txt`

### Step 3: Be_Ga bond lengths
- Role: scored
- Action: From the relaxed structures obtained in step_1, identify the four N atoms that are nearest neighbours to the Be atom. Among them, label the bond from the N atom lying along the positive c‑axis (the [0001] direction; the N with the largest positive fractional c‑coordinate relative to Be) to the Be atom as "N-Be_a". Label the bond from the Be atom to the N atom lying along the negative c‑axis as "Be-N_b". For the remaining two N atoms (the equatorial ones), find for each the nearest Ga neighbour (excluding the defect Be atom) and compute the N–Ga distance. The shorter of these two distances is "N-Ga_c" and the longer is "Ga-N_d". Apply this assignment consistently to all three basis/charge combinations (Ga 3d explicit neutral, nlcc neutral, nlcc charge −1) and output the bond lengths as a JSON file.
- Output file: `/app/outputs/bega_bond_lengths.json`
- Format: json
- Contract: JSON object with keys: "basis" (list of strings: ["Ga3d","nlcc","nlcc"]), "charge" (list of ints: [0,0,-1]), "N-Be_a" (list of floats, Å), "Be-N_b" (list of floats, Å), "N-Ga_c" (list of floats, Å), "Ga-N_d" (list of floats, Å). Each list length 3.
- Scoring: scored by hidden verifier

### Step 4: Be_Ga formation energies
- Role: scored (load-bearing)
- Action: Using the total energies from step_1 and the reference chemical potentials from step_0, compute the formation energy E_f(0) of neutral Be_Ga under Ga‑rich and N‑rich conditions via the standard defect formation‑energy formula. Output the two values.
- Output file: `/app/outputs/bega_formation_energies.json`
- Format: json
- Contract: JSON object with keys: "Ga_rich_Ef0" (float, eV), "N_rich_Ef0" (float, eV).
- Scoring: scored by hidden verifier

### Step 5: Be_Ga local vibrational modes
- Role: scored
- Action: Using the relaxed structure of neutral Be_Ga from step_1, construct the dynamical matrix by finite displacements of the Be atom and its four nearest‑neighbour N atoms. Diagonalise to obtain the four highest A1‑symmetry local vibrational mode frequencies. Output the frequencies.
- Output file: `/app/outputs/bega_lvm.json`
- Format: json
- Contract: JSON object with keys: "basis" (string, e.g., "nlcc"), "charge" (int, 0), "frequencies" (list of 4 floats, cm⁻¹).
- Scoring: scored by hidden verifier

### Step 6: (Be‑Be)_Ga split‑interstitial structural relaxation
- Role: process
- Action: Construct a 72‑atom GaN supercell containing a split‑interstitial beryllium pair at a Ga site ((Be‑Be)_Ga). Relax the structure in the neutral charge state (q=0) using DFT. Save the relaxed atomic coordinates.
- Evidence: `/app/outputs/bebega_relax_log.txt`

### Step 7: (Be‑Be)_Ga local vibrational modes
- Role: scored
- Action: From the relaxed structure of (Be‑Be)_Ga obtained in step_5, compute the dynamical matrix by finite displacements of the two Be atoms and their nearest neighbours. Diagonalise to obtain the three highest local vibrational mode frequencies. Output the frequencies.
- Output file: `/app/outputs/bebe_ga_lvm.json`
- Format: json
- Contract: JSON object with keys: "charge" (int, 0), "frequencies" (list of 3 floats, cm⁻¹).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bega_bond_lengths.json`
- `/app/outputs/bega_formation_energies.json`
- `/app/outputs/bega_lvm.json`
- `/app/outputs/bebe_ga_lvm.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bega_bond_lengths.json
- path: `/app/outputs/bega_bond_lengths.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Four Be‑N bond lengths for the Be_Ga acceptor for three basis/charge combinations (Ga3d neutral, nlcc neutral, nlcc −1).
- schema:
  - `type`: object
  - `required`: `basis`, `charge`, `N-Be_a`, `Be-N_b`, `N-Ga_c`, `Ga-N_d`
  - `properties`:
    - `basis`:
      - `type`: array
      - `items`: string
    - `charge`:
      - `type`: array
      - `items`: integer
    - `N-Be_a`:
      - `type`: array
      - `items`: number
      - `unit`: Å
    - `Be-N_b`:
      - `type`: array
      - `items`: number
      - `unit`: Å
    - `N-Ga_c`:
      - `type`: array
      - `items`: number
      - `unit`: Å
    - `Ga-N_d`:
      - `type`: array
      - `items`: number
      - `unit`: Å

### bega_formation_energies.json
- path: `/app/outputs/bega_formation_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Neutral Be_Ga formation energy under Ga‑rich and N‑rich conditions, computed from the DFT total energies and reference chemical potentials.
- schema:
  - `type`: object
  - `required`: `Ga_rich_Ef0`, `N_rich_Ef0`
  - `properties`:
    - `Ga_rich_Ef0`:
      - `type`: number
      - `unit`: eV
    - `N_rich_Ef0`:
      - `type`: number
      - `unit`: eV

### bega_lvm.json
- path: `/app/outputs/bega_lvm.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The four highest A1‑symmetry local vibrational mode frequencies for neutral Be_Ga.
- schema:
  - `type`: object
  - `required`: `basis`, `charge`, `frequencies`
  - `properties`:
    - `basis`:
      - `type`: string
    - `charge`:
      - `type`: integer
    - `frequencies`:
      - `type`: array
      - `items`: number
      - `unit`: cm⁻¹
      - `minItems`: 4
      - `maxItems`: 4

### bebe_ga_lvm.json
- path: `/app/outputs/bebe_ga_lvm.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The three highest local vibrational mode frequencies for neutral (Be‑Be)Ga split‑interstitial defect.
- schema:
  - `type`: object
  - `required`: `charge`, `frequencies`
  - `properties`:
    - `charge`:
      - `type`: integer
    - `frequencies`:
      - `type`: array
      - `items`: number
      - `unit`: cm⁻¹
      - `minItems`: 3
      - `maxItems`: 3

Notes: All scored outputs must be placed directly in /app/outputs. The bond-length JSON must contain exactly three entries (Ga3d/0, nlcc/0, nlcc/−1) in the order shown. The LVM JSONs must list frequencies in descending order. Tolerances are hidden; the solving agent must compute the values from first‑principles DFT, not from the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bega_bond_lengths.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "basis",
          "charge",
          "N-Be_a",
          "Be-N_b",
          "N-Ga_c",
          "Ga-N_d"
        ],
        "properties": {
          "basis": {
            "type": "array",
            "items": "string"
          },
          "charge": {
            "type": "array",
            "items": "integer"
          },
          "N-Be_a": {
            "type": "array",
            "items": "number",
            "unit": "Å"
          },
          "Be-N_b": {
            "type": "array",
            "items": "number",
            "unit": "Å"
          },
          "N-Ga_c": {
            "type": "array",
            "items": "number",
            "unit": "Å"
          },
          "Ga-N_d": {
            "type": "array",
            "items": "number",
            "unit": "Å"
          }
        }
      },
      "description": "Four Be‑N bond lengths for the Be_Ga acceptor for three basis/charge combinations (Ga3d neutral, nlcc neutral, nlcc −1)."
    },
    {
      "file": "bega_formation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "Ga_rich_Ef0",
          "N_rich_Ef0"
        ],
        "properties": {
          "Ga_rich_Ef0": {
            "type": "number",
            "unit": "eV"
          },
          "N_rich_Ef0": {
            "type": "number",
            "unit": "eV"
          }
        }
      },
      "description": "Neutral Be_Ga formation energy under Ga‑rich and N‑rich conditions, computed from the DFT total energies and reference chemical potentials."
    },
    {
      "file": "bega_lvm.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "basis",
          "charge",
          "frequencies"
        ],
        "properties": {
          "basis": {
            "type": "string"
          },
          "charge": {
            "type": "integer"
          },
          "frequencies": {
            "type": "array",
            "items": "number",
            "unit": "cm⁻¹",
            "minItems": 4,
            "maxItems": 4
          }
        }
      },
      "description": "The four highest A1‑symmetry local vibrational mode frequencies for neutral Be_Ga."
    },
    {
      "file": "bebe_ga_lvm.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "charge",
          "frequencies"
        ],
        "properties": {
          "charge": {
            "type": "integer"
          },
          "frequencies": {
            "type": "array",
            "items": "number",
            "unit": "cm⁻¹",
            "minItems": 3,
            "maxItems": 3
          }
        }
      },
      "description": "The three highest local vibrational mode frequencies for neutral (Be‑Be)Ga split‑interstitial defect."
    }
  ],
  "notes": "All scored outputs must be placed directly in /app/outputs. The bond-length JSON must contain exactly three entries (Ga3d/0, nlcc/0, nlcc/−1) in the order shown. The LVM JSONs must list frequencies in descending order. Tolerances are hidden; the solving agent must compute the values from first‑principles DFT, not from the paper."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently compares each scored output file against the reference values from the original study. Each scored stage (bond lengths, formation energies, BeGa LVM frequencies, and (Be-Be)Ga LVM frequencies) carries a weight, and the final reward is the weighted sum of the partial credits. The verifier applies predetermined tolerances that account for legitimate differences between DFT implementations; these tolerances are kept hidden. The verifier does not re-run any DFT calculation itself; it trusts the reported numbers but validates them against the hidden gold. Submitting values copied from the paper without genuine computation will not achieve the required precision, as the verifier expects self-consistent results from an actual DFT workflow that respects the described method and pseudopotentials.
