# Magnetic properties of transition-metal impurities in MgB2 from first-principles DFT

## Problem background
Magnesium diboride (MgB₂) is a two-band superconductor where the effect of chemical substitutions is crucial for understanding pair-breaking mechanisms. Experiments show that substituting Mg with Mn causes a much more rapid suppression of the superconducting transition temperature (Tc) than substituting with Fe. This difference could be due to the magnetic character of the impurity: a magnetic impurity can act as a spin-flip scattering centre and break Cooper pairs, while a non-magnetic impurity primarily causes disorder scattering. The task is to determine, using first-principles density-functional theory (DFT), whether Mn and Fe impurities in MgB₂ carry a significant local magnetic moment and whether spin polarization lowers the total energy, thereby clarifying their magnetic character.

## Approach
We use the local-density approximation (LDA) within spin-polarized DFT. A 2×2×2 supercell of MgB₂ is constructed using the experimental hexagonal lattice parameters (a = 3.086 Å, c = 3.524 Å), and one Mg atom is replaced by either Mn or Fe, corresponding to a 5% impurity concentration. After ionic relaxation (keeping the lattice vectors fixed), self-consistent field (SCF) calculations are carried out both with and without spin polarization for each impurity supercell. The local magnetic moment on the impurity atom is extracted (e.g., via Mulliken or Bader analysis), and the magnetic stabilization energy is computed as ΔE = E_nonmag – E_spin. By comparing these quantities for Mn and Fe, we assess whether each impurity is magnetic or nearly non-magnetic. Any open-source DFT code supporting LDA pseudopotentials (e.g., Quantum ESPRESSO, GPAW) is acceptable.

## Reproduction target
Produce the file `results.json` containing the computed local magnetic moment (in μB/atom) and magnetic energy difference ΔE (in mRy, where 1 mRy = 0.001 Ry) for each impurity: Mn and Fe. The keys are `Mn_magnetic_moment_mub`, `Fe_magnetic_moment_mub`, `Mn_magnetic_energy_mRy`, `Fe_magnetic_energy_mRy`. All values are floating-point numbers. The goal is to capture the qualitative magnetic character—whether an impurity exhibits a well-developed moment and a clear energy gain from spin polarization, or remains nearly non-magnetic with a negligible moment and energy difference.

## Assets

- MgB2 crystal structure
- Open-source DFT code (e.g., Quantum ESPRESSO, GPAW): https://www.quantum-espresso.org/
- LDA pseudopotentials for Mg, B, Mn, Fe: https://pseudopotentials.quantum-espresso.org/legacy_tables/ps-library

## Workflow steps

### Step 1: Prepare impurity supercells
- Role: process
- Action: Construct a 2×2×2 supercell of MgB2 using the experimental lattice constants and atomic positions. Create two supercells: one with one Mg atom replaced by Mn, the other with one Mg replaced by Fe. Save the input structures for the chosen DFT code.
- Evidence: `/app/outputs/supercell_inputs.log`

### Step 2: Ionic relaxation of impurity supercells
- Role: process
- Action: Perform ionic relaxation for each impurity supercell (Mn and Fe) using spin-polarized DFT with the LDA functional. Keep lattice vectors fixed and relax atomic positions until forces are below a typical DFT convergence threshold.
- Evidence: `/app/outputs/relaxation.log`

### Step 3: Extract magnetic moments and magnetic energies
- Role: scored (load-bearing)
- Action: For each relaxed supercell, perform a spin-polarized self-consistent field (SCF) calculation and a separate non-spin-polarized SCF calculation. Extract the local magnetic moment on the impurity atom (e.g., via Mulliken or Bader analysis) and the total energies. Compute the magnetic stabilization energy as ΔE = E_nonmag − E_spin (positive when the spin-polarized state is lower in energy). Write the results to /app/outputs/results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys Mn_magnetic_moment_mub (number), Fe_magnetic_moment_mub (number), Mn_magnetic_energy_mRy (number), Fe_magnetic_energy_mRy (number). All values are floats.
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
- description: The checker compares the computed magnetic moments and stabilization energies against predetermined thresholds to determine the magnetic character (magnetic vs. non-magnetic) of each impurity. The thresholds are set to capture the qualitative behavior and accommodate differences in methodology.
- schema:
  - `type`: object
  - `required`: `Mn_magnetic_moment_mub`, `Fe_magnetic_moment_mub`, `Mn_magnetic_energy_mRy`, `Fe_magnetic_energy_mRy`
  - `properties`:
    - `Mn_magnetic_moment_mub`:
      - `type`: number
    - `Fe_magnetic_moment_mub`:
      - `type`: number
    - `Mn_magnetic_energy_mRy`:
      - `type`: number
    - `Fe_magnetic_energy_mRy`:
      - `type`: number
  - `units`:
    - `Mn_magnetic_moment_mub`: μB
    - `Fe_magnetic_moment_mub`: μB
    - `Mn_magnetic_energy_mRy`: mRy
    - `Fe_magnetic_energy_mRy`: mRy

Notes: The task uses a supercell approach and open-source DFT to reproduce the paper's qualitative magnetic character. Tolerances are set to absorb differences from code/functional choices; exact numerical match is not required. The agent must perform the DFT calculations, not merely look up reported values.

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
        "required": [
          "Mn_magnetic_moment_mub",
          "Fe_magnetic_moment_mub",
          "Mn_magnetic_energy_mRy",
          "Fe_magnetic_energy_mRy"
        ],
        "properties": {
          "Mn_magnetic_moment_mub": {
            "type": "number"
          },
          "Fe_magnetic_moment_mub": {
            "type": "number"
          },
          "Mn_magnetic_energy_mRy": {
            "type": "number"
          },
          "Fe_magnetic_energy_mRy": {
            "type": "number"
          }
        },
        "units": {
          "Mn_magnetic_moment_mub": "μB",
          "Fe_magnetic_moment_mub": "μB",
          "Mn_magnetic_energy_mRy": "mRy",
          "Fe_magnetic_energy_mRy": "mRy"
        }
      },
      "description": "The checker compares the computed magnetic moments and stabilization energies against predetermined thresholds to determine the magnetic character (magnetic vs. non-magnetic) of each impurity. The thresholds are set to capture the qualitative behavior and accommodate differences in methodology."
    }
  ],
  "notes": "The task uses a supercell approach and open-source DFT to reproduce the paper's qualitative magnetic character. Tolerances are set to absorb differences from code/functional choices; exact numerical match is not required. The agent must perform the DFT calculations, not merely look up reported values."
}
```

## How you are scored
A hidden verifier reads your `results.json`. It checks that the file conforms to the required schema and then compares your computed magnetic moments and magnetic energies against pre-set thresholds that separate “magnetic” from “nearly non-magnetic” behaviour. The thresholds are derived from the paper’s qualitative claims and allow for reasonable numerical differences arising from the use of a supercell instead of the coherent-potential approximation and from different DFT implementations. You are not expected to match any specific value from the literature; the scoring rewards correct qualitative trends. A small fraction of the reward comes from file existence and shape compliance; the bulk is awarded for correctly placing Mn and Fe on the magnetic/non-magnetic sides of the hidden criteria.