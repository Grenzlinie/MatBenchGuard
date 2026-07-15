# High Pressure Phase Transition and Dynamical Stability Analysis of Thallium

## Problem background
Thallium (Tl), a group III-A metal, exhibits complex high‑pressure phase transitions that are governed by the behaviour of its semicore d electrons. Unlike the lighter III‑A elements (Al, Ga, In), the structural sequence of Tl under compression has not been thoroughly studied. This task aims to computationally reproduce the crystal‑phase stability and transition pathway of Tl using first‑principles electronic structure calculations, and to relate the findings to the mixing of s, p, and d orbitals.

## Approach
The reproduction employs density‑functional theory (DFT) with a plane‑wave/pseudopotential method. Total energies are computed for the hexagonal close‑packed (h.c.p.), face‑centred cubic (f.c.c.), and body‑centred tetragonal (b.c.t.) phases of Tl at a series of volumes spanning a wide pressure range. The equation of state is fitted to these data, and relative enthalpies are calculated to determine which phase is thermodynamically favoured at a given pressure. Phonon calculations are performed to examine the dynamical stability of the b.c.t. phase. Electronic structure calculations (band structure and partial density of states) are carried out for selected phases and pressures to document the orbital‑mixing trends that accompany the transitions. All calculations use open‑source codes (Quantum ESPRESSO, Phonopy) and publicly available pseudopotentials.

## Reproduction target
Produce a self‑contained DFT‑based reproduction package that yields the following: (a) the pressure at which the h.c.p. to f.c.c. transition occurs and the pressure at which the f.c.c. to b.c.t. transition occurs; (b) evidence of whether the b.c.t. phase is dynamically stable at 80 GPa, through a phonon‑dispersion calculation; (c) electronic band structures and partial density‑of‑states data for the h.c.p. phase at 0 and 3 GPa, and for the f.c.c. phase at 3 and 50 GPa, as supporting documentation.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: phonopy
- Tl pseudopotential: https://www.materialscloud.org/discover/sssp/table
- Python 3 with numpy, scipy: python3

## Workflow steps

### Step 1: DFT total-energy calculations for h.c.p., f.c.c., b.c.t. phases
- Role: process
- Action: Using Quantum ESPRESSO, perform SCF calculations for h.c.p. (c/a=1.598), f.c.c., and b.c.t. (c/a=1.375) phases at a series of volumes spanning a pressure range from 0 to ~110 GPa. For each volume, save the total energy. Output CSV files (hcp_ev.csv, fcc_ev.csv, bct_ev.csv) containing volume and energy columns.
- Evidence: `/app/outputs/hcp_ev.csv, fcc_ev.csv, bct_ev.csv`

### Step 2: Phonon dispersion of b.c.t. at 80 GPa
- Role: process
- Action: Optimize the b.c.t. structure at 80 GPa using Quantum ESPRESSO, then use Phonopy with the finite-displacement method to compute phonon frequencies along a path Γ→X→P→Γ→T. Save the phonon band structure as phonon_band.dat (format: q-point coordinate, branch index, frequency).
- Evidence: `/app/outputs/phonon_band.dat`

### Step 3: Electronic band structure and PDOS analysis
- Role: process
- Action: Perform band structure and partial density of states (PDOS) calculations for h.c.p. at 0 GPa and 3 GPa, and f.c.c. at 3 GPa and 50 GPa. Output band data and PDOS data for documentation (bands_hcp_0GPa.dat, bands_hcp_3GPa.dat, bands_fcc_3GPa.dat, bands_fcc_50GPa.dat, pdos_hcp_0GPa.dat, pdos_hcp_3GPa.dat, pdos_fcc_3GPa.dat, pdos_fcc_50GPa.dat).
- Evidence: `/app/outputs/bands_hcp_0GPa.dat, bands_hcp_3GPa.dat, bands_fcc_3GPa.dat, bands_fcc_50GPa.dat, pdos_hcp_0GPa.dat, pdos_hcp_3GPa.dat, pdos_fcc_3GPa.dat, pdos_fcc_50GPa.dat`

### Step 4: Compute transition pressures and dynamical stability
- Role: scored (load-bearing)
- Action: From the energy-volume data in s1, fit each phase to the Birch-Murnaghan equation of state and obtain enthalpy H = E + PV. Determine the h.c.p.→f.c.c. transition pressure as the lowest pressure where f.c.c. enthalpy becomes lower than h.c.p., and the f.c.c.→b.c.t. transition pressure analogously. From s2's phonon data, verify that all phonon frequencies are non-negative at 80 GPa; if so, set dynamical_stable=True. Write reproduced_results.json containing hcp_to_fcc_transition_pressure_GPa, fcc_to_bct_transition_pressure_GPa, and bct_dynamically_stable_at_80GPa.
- Output file: `/app/outputs/reproduced_results.json`
- Format: json
- Contract: {"hcp_to_fcc_transition_pressure_GPa": <float>, "fcc_to_bct_transition_pressure_GPa": <float>, "bct_dynamically_stable_at_80GPa": <boolean>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reproduced_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reproduced_results.json
- path: `/app/outputs/reproduced_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed transition pressures and dynamical stability. hcp_to_fcc_transition_pressure_GPa and fcc_to_bct_transition_pressure_GPa are physical pressures; bct_dynamically_stable_at_80GPa is a boolean indicating absence of imaginary phonon modes. These are compared against the paper's reported values with appropriate tolerances.
- schema:
  - `type`: object
  - `required`: `hcp_to_fcc_transition_pressure_GPa`, `fcc_to_bct_transition_pressure_GPa`, `bct_dynamically_stable_at_80GPa`
  - `units`:
    - `hcp_to_fcc_transition_pressure_GPa`: GPa
    - `fcc_to_bct_transition_pressure_GPa`: GPa

Notes: The electronic structure data (bands and PDOS) are generated as process-step evidence but are not scored. The checker only reads reproduced_results.json and applies hidden tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reproduced_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "hcp_to_fcc_transition_pressure_GPa",
          "fcc_to_bct_transition_pressure_GPa",
          "bct_dynamically_stable_at_80GPa"
        ],
        "units": {
          "hcp_to_fcc_transition_pressure_GPa": "GPa",
          "fcc_to_bct_transition_pressure_GPa": "GPa"
        }
      },
      "description": "Computed transition pressures and dynamical stability. hcp_to_fcc_transition_pressure_GPa and fcc_to_bct_transition_pressure_GPa are physical pressures; bct_dynamically_stable_at_80GPa is a boolean indicating absence of imaginary phonon modes. These are compared against the paper's reported values with appropriate tolerances."
    }
  ],
  "notes": "The electronic structure data (bands and PDOS) are generated as process-step evidence but are not scored. The checker only reads reproduced_results.json and applies hidden tolerances."
}
```

## How you are scored
A hidden verifier reads the output files and applies a scoring rubric that evaluates each stage’s artifacts. The final reward (a float between 0 and 1) is a weighted sum over the scored stages. For the transition pressures and the dynamical‑stability flag in `reproduced_results.json`, the checker compares your computed values to hidden references with tolerances that reflect the expected spread of DFT results from different codes and pseudopotentials. Passing requires that you genuinely execute the DFT and phonon calculations; simply writing down the expected numbers will not satisfy the verification.
