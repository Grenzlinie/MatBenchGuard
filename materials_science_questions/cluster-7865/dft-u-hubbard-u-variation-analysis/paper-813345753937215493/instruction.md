# Reproducing spin-orientation-dependent band gap in a bilayer ruthenate via DFT+U+SOC

## Problem background
Ca3Ru2O7 is a bilayer ruthenate that exhibits a metal-insulator transition at about 48 K, accompanied by a spin reorientation. At low temperature the compound orders antiferromagnetically with the Ru magnetic moments aligned along the crystallographic b axis and is an insulator; above the transition the moments switch to the a axis and the system becomes metallic. The origin of this Mott-like transition and its connection to magnetic anisotropy are the subject of active investigation. First-principles electronic structure calculations can provide insight into how the interplay of spin-orbit coupling, Coulomb repulsion, and crystal structure determines the transport and magnetic properties in this material.

## Approach
The approach is to perform density-functional theory (DFT) calculations within the generalized gradient approximation (GGA), augmented with an on-site Coulomb U correction (GGA+U) for the Ru 4d electrons and including spin-orbit coupling (SOC). The calculations are set up for the A-type antiferromagnetic (AFM) order of Ca3Ru2O7, where RuO2 bilayers are coupled ferromagnetically in the ab plane and antiferromagnetically along the c axis. Three separate calculations are carried out with the magnetic moments oriented along the a, b, and c axes (denoted AFM-a, AFM-b, AFM-c). The experimental low-temperature crystal structure (lattice parameters and atomic positions) is used as input, and a Hubbard U of 3.5 eV is applied to the Ru 4d states. The self-consistent field (SCF) solution and band structures are computed for each orientation. From the converged results, the band gap (conduction band minimum minus valence band maximum) and the total energy per Ru atom are extracted, and the total energies are expressed relative to the most stable phase.

## Reproduction target
Produce a JSON file `results.json` containing, for each of the three spin orientations (AFM-a, AFM-b, AFM-c), two numbers: the band gap (in eV) and the total energy per Ru atom relative to the lowest-energy phase (in meV/Ru). The band gap is the difference between the energy of the lowest unoccupied state and the highest occupied state. The relative total energy is computed by taking the total energy per formula unit (or per Ru atom), subtracting the smallest value among the three orientations, and expressing it in meV per Ru atom. These quantities should be obtained from SCF+bands calculations following the GGA+U+SOC protocol described in the Approach and Workflow steps. The exact values are not given; they will be assessed against physical expectations by the hidden verifier.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Ca3Ru2O7 experimental crystal structure: 10.1103/PhysRevB.72.054412
- Pseudopotentials for Ru, Ca, O: https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Prepare crystal structure input
- Role: process
- Action: Generate the Quantum ESPRESSO input files for the A-type antiferromagnetic structure of Ca3Ru2O7. Use the experimental lattice parameters and atomic positions from Yoshida et al. (2005) to set up three separate calculations with spin moments oriented along a, b, and c axes. Include GGA+U with U=3.5 eV on Ru 4d and spin-orbit coupling.
- Evidence: `/app/outputs/input_setup.log`

### Step 2: Run GGA+U+SOC DFT calculations
- Role: process
- Action: Execute Quantum ESPRESSO pw.x for each spin orientation (AFM-a, AFM-b, AFM-c) to converge the self-consistent field and compute band structures. Use a k-point mesh compatible with the FLAPW mesh of 91 irreducible k‑points. Save standard output logs for each run.
- Evidence: `/app/outputs/afm_a.out, afm_b.out, afm_c.out`

### Step 3: Extract band gaps and total energies
- Role: scored (load-bearing)
- Action: Parse the Quantum ESPRESSO output files to determine the band gap (energy difference between the bottom of the conduction band and the top of the valence band) for each spin orientation. Extract total energies, convert to energy per Ru atom, and express relative to the lowest-energy phase in meV/Ru. Save the results as a JSON object with keys 'AFM-a', 'AFM-b', 'AFM-c'.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"AFM-a": {"band_gap": float (eV), "total_energy_per_Ru": float (meV relative to lowest)}, "AFM-b": {...}, "AFM-c": {...}}
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
- description: Band gaps and relative total energies for AFM-a, AFM-b, AFM-c. The checker verifies that AFM‑b band gap meets an insulating threshold and that total energy ordering follows AFM‑b < AFM‑c < AFM‑a.
- schema:
  - `type`: object
  - `required`:
    - `AFM-a`:
      - `band_gap`: float (eV)
      - `total_energy_per_Ru`: float (meV relative to lowest)
    - `AFM-b`:
      - `band_gap`: float (eV)
      - `total_energy_per_Ru`: float (meV relative to lowest)
    - `AFM-c`:
      - `band_gap`: float (eV)
      - `total_energy_per_Ru`: float (meV relative to lowest)
  - `units`:
    - `band_gap`: eV
    - `total_energy_per_Ru`: meV/Ru

Notes: The checker will compare the reported band gaps against a hidden insulating threshold and validate the relative total energy ordering. Tolerances and exact thresholds are hidden; the task is to reproduce the computational workflow, not to guess numbers.

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
          "AFM-a": {
            "band_gap": "float (eV)",
            "total_energy_per_Ru": "float (meV relative to lowest)"
          },
          "AFM-b": {
            "band_gap": "float (eV)",
            "total_energy_per_Ru": "float (meV relative to lowest)"
          },
          "AFM-c": {
            "band_gap": "float (eV)",
            "total_energy_per_Ru": "float (meV relative to lowest)"
          }
        },
        "units": {
          "band_gap": "eV",
          "total_energy_per_Ru": "meV/Ru"
        }
      },
      "description": "Band gaps and relative total energies for AFM-a, AFM-b, AFM-c. The checker verifies that AFM‑b band gap meets an insulating threshold and that total energy ordering follows AFM‑b < AFM‑c < AFM‑a."
    }
  ],
  "notes": "The checker will compare the reported band gaps against a hidden insulating threshold and validate the relative total energy ordering. Tolerances and exact thresholds are hidden; the task is to reproduce the computational workflow, not to guess numbers."
}
```

## How you are scored
After you submit the output files, a hidden verifier will read your `results.json` and compare the reported band gaps and relative total energies to reference values derived from the original study. Because different DFT implementations (plane-wave vs. all-electron, pseudopotential choice, k-point sampling) can give slightly different absolute numbers, the scoring uses tolerances that account for this toolchain spread while still requiring the correct physical behavior: the band-gap magnitude for the insulating phase must clearly exceed a threshold, and the signs (zero vs. finite gap) must be consistent. Additionally, the total energy ordering among the three spin orientations is checked for correctness. The file format and presence of the required keys are also validated. The overall reward is a weighted combination of these checks, with the band-gap and energy-ordering checks carrying the largest weight. The exact tolerances and the reference values are hidden.
