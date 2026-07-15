# Phonon stability analysis of double perovskite Pb2MgTeO6 using density functional perturbation theory

## Problem background
Pb₂MgTeO₆ is a double perovskite oxide that undergoes a structural phase transition from a high‑temperature cubic phase to a low‑temperature incommensurately modulated rhombohedral phase. Understanding what drives this transition and which lattice instabilities lead to the incommensurate modulation is the central question. The goal is to investigate the lattice dynamics of both phases by computing phonon frequencies and identifying soft modes using first‑principles methods. Specifically, one must determine the imaginary (unstable) phonon frequencies at the Brillouin zone centre in the cubic phase, quantify the energetic effect of freezing those modes into the structure, and locate the wavevector of the unstable mode that emerges in the average rhombohedral phase. The results reveal the dominant instability (polar versus octahedral rotations) and provide the modulation vector of the low‑temperature incommensurate structure.

## Approach
The calculations are performed with density functional theory (DFT) within the local density approximation (LDA) using a plane‑wave pseudopotential method, and the lattice dynamics are treated by density functional perturbation theory (DFPT). The material is studied in two structural states: the cubic aristotype and the average rhombohedral structure. For each, the workflow consists of: (i) computing the electronic ground state; (ii) calculating dynamical matrices on a q‑point mesh; (iii) Fourier interpolating to obtain phonon dispersions along high‑symmetry paths; (iv) identifying unstable (imaginary‑frequency) modes and extracting their eigendisplacement patterns. In the cubic phase, the T₁u and T₂g zone‑centre unstable modes are isolated, and frozen‑phonon total‑energy calculations are performed for selected displacement amplitudes to obtain the energy lowering relative to the ground state. In the rhombohedral phase, the phonon dispersion is scanned along high‑symmetry directions to locate the wavevector of the minimum‑frequency unstable mode and its direction. The final deliverables are two JSON files summarising the key quantities: one for the cubic instabilities and one for the rhombohedral instability.

## Reproduction target
Produce the following two output files under /app/outputs:
- cubic_instabilities.json: must contain, under the key “T1u”, the imaginary frequency of the T₁u mode (cm⁻¹), the energy lowering (meV) when freezing one component of the T₁u eigendisplacement, and the energy lowering when freezing all three components simultaneously; under “T2g”, the energy lowering (meV) when freezing one component of the T₂g eigendisplacement and the corresponding octahedral rotation angle (degrees).
- rhombohedral_instability.json: must contain the direction vector of the instability (as a three‑element array), the reduced wavevector coordinate δ along that direction, and the imaginary frequency (cm⁻¹) at the minimum.

All values must be obtained from the LDA/ABINIT calculations described in the workflow steps, using the atomic positions and lattice parameters provided. The results should be numerically precise and reflect a convergence with respect to the chosen computational parameters.

## Assets

- ABINIT software package: https://www.abinit.org/
- Troullier-Martins pseudopotentials for Mg, Te, O and extended Teter norm-conserving pseudopotential for Pb: https://www.abinit.org/downloads/psp-links

## Workflow steps

### Step 1: Cubic DFPT calculation
- Role: process
- Action: Prepare input files for the cubic phase (a = 7.833 Å, atomic positions: Mg <0 0 0>, Te <1/2 1/2 1/2>, Pb <1/4 1/4 1/4>, O <0.2645 0 0> in conventional cell) and run ABINIT to compute dynamical matrices and interatomic force constants on a q-point grid using the specified pseudopotentials and LDA functional.
- Evidence: `/app/outputs/cubic_phonon.out`

### Step 2: Cubic mode analysis and eigendisplacements
- Role: process
- Action: Perform Fourier interpolation of the interatomic force constants to obtain the phonon band structure along high-symmetry paths. Identify unstable modes at Γ (T1u and T2g), extract their eigendisplacements, and save the displacement patterns for use in frozen-phonon calculations.
- Evidence: `/app/outputs/cubic_modes.json`

### Step 3: Frozen-phonon energy calculations
- Role: process
- Action: Using the T1u and T2g eigendisplacements, construct displaced atomic configurations: (a) single-component T1u displacement, (b) coupled three-component T1u displacement, (c) single-component T2g displacement that rotates the octahedra. For each, run a DFT total energy calculation (ABINIT, same functional and pseudopotentials) and record the energy relative to the undistorted cubic ground state.
- Evidence: `/app/outputs/frozen_phonon_energies.json`

### Step 4: Cubic instability summary
- Role: scored
- Action: Compile the cubic instability results into cubic_instabilities.json: the imaginary frequency of the T1u mode (cm⁻¹), the single‑component T1u energy lowering (meV), the coupled T1u energy lowering (meV), the single‑component T2g energy lowering (meV), and the octahedra rotation angle (degrees) from the T2g displacement.
- Output file: `/app/outputs/cubic_instabilities.json`
- Format: json
- Contract: {"T1u": {"imaginary_frequency_cm-1": number, "single_lowering_meV": number, "coupled_lowering_meV": number}, "T2g": {"single_lowering_meV": number, "rotation_angle_deg": number}}
- Scoring: scored by hidden verifier

### Step 5: Rhombohedral DFPT calculation
- Role: process
- Action: Prepare input files for the average rhombohedral phase (a = 5.531 Å, α = 60.27°, atomic positions: Mg <0 0 0>, Te <1/2 1/2 1/2>, Pb <0.2507 0.2507 0.2507>, O <0.2669 0.7646 0.7051> in primitive cell) and run ABINIT to compute dynamical matrices and interatomic force constants on a q-point grid.
- Evidence: `/app/outputs/rhombo_phonon.out`

### Step 6: Rhombohedral mode analysis and instability localization
- Role: process
- Action: Fourier‑interpolate the interatomic force constants to obtain the phonon band structure. Scan the [100] direction (rhombohedral reciprocal‑space direction) for unstable phonon branches. Locate the wavevector δ (reduced coordinate) where the minimum imaginary frequency occurs, and verify the direction.
- Evidence: `/app/outputs/rhombo_modes.json`

### Step 7: Rhombohedral instability summary
- Role: scored
- Action: Compile the rhombohedral instability results into rhombohedral_instability.json: the direction vector (e.g., [1,0,0]), the reduced coordinate δ, and the imaginary frequency (cm⁻¹) at the minimum.
- Output file: `/app/outputs/rhombohedral_instability.json`
- Format: json
- Contract: {"direction": [number, number, number], "delta": number, "imaginary_frequency_cm-1": number}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/cubic_instabilities.json`
- `/app/outputs/rhombohedral_instability.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cubic_instabilities.json
- path: `/app/outputs/cubic_instabilities.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Key cubic instability quantities: T1u imaginary frequency, energy lowerings from freezing single and coupled T1u displacements, and T2g energy lowering with rotation angle. The hidden checker compares these against the paper-reported values with tolerance.
- schema:
  - `type`: object
  - `required`:
    - `T1u`:
      - `imaginary_frequency_cm-1`: number (positive float; magnitude of imaginary frequency in cm⁻¹)
      - `single_lowering_meV`: number (energy lowering in meV)
      - `coupled_lowering_meV`: number (energy lowering in meV)
    - `T2g`:
      - `single_lowering_meV`: number (energy lowering in meV)
      - `rotation_angle_deg`: number (octahedra rotation angle in degrees)

### rhombohedral_instability.json
- path: `/app/outputs/rhombohedral_instability.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Key rhombohedral instability quantities: direction vector, modulation wavevector δ, and the associated imaginary frequency. The hidden checker compares these against the paper-reported values with tolerance.
- schema:
  - `type`: object
  - `required`:
    - `direction`: array of three numbers (the instability direction vector, e.g., [1,0,0])
    - `delta`: number (reduced coordinate δ of the wavevector minimum)
    - `imaginary_frequency_cm-1`: number (positive float; magnitude of imaginary frequency at minimum in cm⁻¹)

Notes: This is a compute-driven reproduction task. The hidden checker performs a result-level comparison (T0) of the submitted values against the paper’s reported results, using appropriate tolerances to absorb implementation differences. Both artifacts must be valid JSON with the exact keys and number types described.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cubic_instabilities.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "T1u": {
            "imaginary_frequency_cm-1": "number (positive float; magnitude of imaginary frequency in cm⁻¹)",
            "single_lowering_meV": "number (energy lowering in meV)",
            "coupled_lowering_meV": "number (energy lowering in meV)"
          },
          "T2g": {
            "single_lowering_meV": "number (energy lowering in meV)",
            "rotation_angle_deg": "number (octahedra rotation angle in degrees)"
          }
        }
      },
      "description": "Key cubic instability quantities: T1u imaginary frequency, energy lowerings from freezing single and coupled T1u displacements, and T2g energy lowering with rotation angle. The hidden checker compares these against the paper-reported values with tolerance."
    },
    {
      "file": "rhombohedral_instability.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "direction": "array of three numbers (the instability direction vector, e.g., [1,0,0])",
          "delta": "number (reduced coordinate δ of the wavevector minimum)",
          "imaginary_frequency_cm-1": "number (positive float; magnitude of imaginary frequency at minimum in cm⁻¹)"
        }
      },
      "description": "Key rhombohedral instability quantities: direction vector, modulation wavevector δ, and the associated imaginary frequency. The hidden checker compares these against the paper-reported values with tolerance."
    }
  ],
  "notes": "This is a compute-driven reproduction task. The hidden checker performs a result-level comparison (T0) of the submitted values against the paper’s reported results, using appropriate tolerances to absorb implementation differences. Both artifacts must be valid JSON with the exact keys and number types described."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that reads cubic_instabilities.json and rhombohedral_instability.json. It compares your reported values to hidden reference values, using appropriate tolerances that absorb the typical spread associated with different DFT implementations and convergence choices. The reward is computed as a weighted sum of the scores for each mandatory key field; the final score ranges from 0 (worst) to 1 (best). There is no partial credit for intermediate log files or for merely running the code; only the contents of the two JSON artifacts are considered. The verifier does not need to re‑run any DFT calculation.
