# Phonon-based dynamical stability and HER activity of pentagonal MS monolayers

## Problem background
Two-dimensional (2D) nanomaterials have attracted intense interest for their unique properties and applications in catalysis, particularly for clean hydrogen production. Among them, pentagonal 2D transition-metal sulphide monolayers (MS, where M = Fe, Mn, V) have been theoretically proposed as potential catalysts for the hydrogen evolution reaction (HER). Their practical viability depends on three forms of structural stability (dynamic, thermal, mechanical) and on catalytic activity, which can be predicted from first-principles computations. This task computes the key quantities that determine whether these monolayers are stable and how active they are for HER.

## Approach
We use density functional theory (DFT) with the PBE-GGA functional and an open-source plane-wave code (e.g. Quantum Espresso) together with the PHONOPY finite-displacement phonon code. The workflow proceeds in stages: (1) geometry optimisation of the unit cells; (2) phonon dispersion calculations to assess dynamic stability by checking for imaginary frequencies; (3) ab initio molecular dynamics (AIMD) to evaluate thermal stability; (4) extraction of 2D elastic constants (c11, c12, c66) to verify mechanical stability via the Born criteria; (5) spin-polarised electronic structure calculations to determine the magnetic ground state and magnetic moments; (6) hydrogen adsorption on supercells at various coverages, computing adsorption energies and then converting them to differential and average Gibbs free energies (ΔG_H) for HER using provided zero-point energy corrections and entropy terms; (7) compilation of all results into a single JSON file.

## Reproduction target
Produce a structured JSON file (`results.json`) containing the following computed quantities:
- **Phonon dispersions** for FeS, MnS, VS: q‑points and frequencies along a high‑symmetry path.
- **AIMD potential energy time series** for FeS at 673 K, VS at 673 K, and MnS at 300 K.
- **2D elastic constants** (c11, c12, c66) for each material.
- **Magnetic moments** (metal and sulphur) for each material in its ground magnetic state.
- **HER Gibbs free energies** for FeS and VS: differential ΔG_H and average ΔG_H for each hydrogen coverage n = 1 through 8.
The computed data are the basis for evaluating stability and catalytic activity; do not include the paper’s reported numerical values or attempt to match a specific table.

## Assets

- Quantum Espresso (or another open-source plane-wave DFT code): https://www.quantum-espresso.org/
- PHONOPY: https://phonopy.github.io/phonopy/
- Pseudopotentials (e.g., PseudoDojo or standard PBE pseudopotentials): http://www.pseudo-dojo.org/
- Python scientific stack (numpy, scipy, matplotlib): numpy, scipy, matplotlib

## Workflow steps

### Step 1: Geometry optimization of MS monolayers
- Role: process
- Action: Perform DFT geometry optimization for the unit cells of pentagonal MS (M = Fe, Mn, V) monolayers using an open-source plane-wave DFT code (e.g., Quantum Espresso) with the PBE-GGA functional. Optimize atomic positions and lattice constants to obtain relaxed structures.
- Evidence: `/app/outputs/geom_opt.log`

### Step 2: Phonon dispersion calculation
- Role: process
- Action: Using a supercell of each optimized monolayer, compute phonon dispersions along a high-symmetry path in the first Brillouin zone via the finite-displacement method with PHONOPY (or equivalent). Extract phonon frequencies as a function of wavevector.
- Evidence: `/app/outputs/phonon_dispersions.csv`

### Step 3: Ab initio molecular dynamics (AIMD) for thermal stability
- Role: process
- Action: Perform ab initio molecular dynamics on supercells of FeS and VS at a high temperature (e.g., 673 K) and MnS at room temperature. Record potential energy as a function of time and final atomic structures.
- Evidence: `/app/outputs/aimd_potential_energy.csv`

### Step 4: Elastic constant calculation
- Role: process
- Action: Apply small strains to the optimized unit cells of FeS, MnS, and VS and compute total energies via DFT. Fit the energy-strain relations to extract the 2D elastic constants c11, c12, c66.
- Evidence: `/app/outputs/elastic_constants.csv`

### Step 5: Electronic structure and magnetic ground state
- Role: process
- Action: Perform spin-polarized DFT calculations for each MS monolayer in nonmagnetic, ferromagnetic, and antiferromagnetic configurations. Determine the ground magnetic state and the magnetic moments on metal and S atoms.
- Evidence: `/app/outputs/magnetic_properties.csv`

### Step 6: Hydrogen adsorption and HER Gibbs free energy
- Role: process
- Action: Construct a supercell of each MS monolayer, screen hydrogen adsorption sites, and compute total energies for systems with various hydrogen coverages (n = 1 to 8). Using the provided zero-point energy corrections and entropy terms, calculate the differential and average Gibbs free energies (ΔG_H) for FeS and VS.
- Evidence: `/app/outputs/her_gibbs_data.csv`

### Step 7: Compile all results into a single JSON
- Role: scored (load-bearing)
- Action: Collect the computed data: phonon dispersion data (q-points, frequencies) for FeS, MnS, VS; AIMD potential energy vs time for FeS at 673 K, VS at 673 K, MnS at 300 K; elastic constants c11, c12, c66 for each material; magnetic moments for each material; and for FeS and VS, the differential and average ΔG_H for each coverage n=1..8. Write all results to a single JSON file named results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {
  "phonon": {
    "FeS": {"q_points": [<array of q-vectors>], "frequencies": [<array of frequencies in cm^-1>]},
    "MnS": { ... },
    "VS": { ... }
  },
  "aimd_potential": {
    "FeS_673K": {"time_ps": [<array>], "potential_energy_eV": [<array>]},
    "VS_673K": { ... },
    "MnS_300K": { ... }
  },
  "elastic_constants": {
    "FeS": {"c11": <float>, "c12": <float>, "c66": <float>},
    "MnS": { ... },
    "VS": { ... }
  },
  "magnetic_moments": {
    "FeS": {"M_moment_muB": <float>, "S_moment_muB": <float>},
    "MnS": { ... },
    "VS": { ... }
  },
  "her_gibbs": {
    "FeS": {
      "differential_dG_H": [<array of 8 values for n=1..8>],
      "average_dG_H": [<array of 8 values for n=1..8>]
    },
    "VS": { ... }
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
- target_policy: reference_match
- description: Aggregated quantitative results: phonon dispersions, AIMD potential energies, elastic constants, magnetic moments, and HER Gibbs free energies.
- schema:
  - `type`: object
  - `required`: `phonon`, `aimd_potential`, `elastic_constants`, `magnetic_moments`, `her_gibbs`
  - `properties`:
    - `phonon`:
      - `type`: object
      - `description`: Phonon dispersions for FeS, MnS, VS; each with q_points (array of arrays) and frequencies (array of arrays)
    - `aimd_potential`:
      - `type`: object
      - `description`: AIMD potential energies for FeS_673K, VS_673K, MnS_300K; each with time_ps (array) and potential_energy_eV (array)
    - `elastic_constants`:
      - `type`: object
      - `description`: 2D elastic constants c11, c12, c66 (floats) for FeS, MnS, VS
    - `magnetic_moments`:
      - `type`: object
      - `description`: Magnetic moments for FeS, MnS, VS; each with M_moment_muB and S_moment_muB (floats)
    - `her_gibbs`:
      - `type`: object
      - `description`: HER Gibbs free energies for FeS and VS; each with differential_dG_H (8 floats) and average_dG_H (8 floats)

Notes: The checker verifies dynamic, thermal, and mechanical stability criteria and HER activity by comparing these values to hidden paper references and physical thresholds.

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
        "required": [
          "phonon",
          "aimd_potential",
          "elastic_constants",
          "magnetic_moments",
          "her_gibbs"
        ],
        "properties": {
          "phonon": {
            "type": "object",
            "description": "Phonon dispersions for FeS, MnS, VS; each with q_points (array of arrays) and frequencies (array of arrays)"
          },
          "aimd_potential": {
            "type": "object",
            "description": "AIMD potential energies for FeS_673K, VS_673K, MnS_300K; each with time_ps (array) and potential_energy_eV (array)"
          },
          "elastic_constants": {
            "type": "object",
            "description": "2D elastic constants c11, c12, c66 (floats) for FeS, MnS, VS"
          },
          "magnetic_moments": {
            "type": "object",
            "description": "Magnetic moments for FeS, MnS, VS; each with M_moment_muB and S_moment_muB (floats)"
          },
          "her_gibbs": {
            "type": "object",
            "description": "HER Gibbs free energies for FeS and VS; each with differential_dG_H (8 floats) and average_dG_H (8 floats)"
          }
        }
      },
      "description": "Aggregated quantitative results: phonon dispersions, AIMD potential energies, elastic constants, magnetic moments, and HER Gibbs free energies."
    }
  ],
  "notes": "The checker verifies dynamic, thermal, and mechanical stability criteria and HER activity by comparing these values to hidden paper references and physical thresholds."
}
```

## How you are scored
A hidden verifier reads `results.json` and scores each category independently:
- **Dynamic stability**: the phonon dispersions are checked for the absence of significant imaginary frequencies.
- **Thermal stability**: the AIMD potential energy time series are examined for runaway drift (energy variance within an acceptable bound).
- **Mechanical stability**: the elastic constants are verified against the Born criteria (c11 > |c12| and c66 > 0).
- **Magnetic properties**: the magnetic moments are compared to expected ranges.
- **HER activity**: for FeS and VS, the minimum absolute differential Gibbs free energy |ΔG_H| is evaluated; a small value indicates high activity. The Gibbs free energies are compared to hidden reference values derived from the original study.
Each category carries a weight, and the overall reward is a weighted sum (0–1) that reflects how well your computed results reproduce the required physical behaviour. Simply reporting the paper’s numbers is not sufficient; the verifier examines the internal consistency and compares each quantity against hidden criteria.
