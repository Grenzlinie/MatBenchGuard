# Computational Determination of Structural and Vibrational Properties of Ge(001) p(2×1) Surface

## Problem background
The (001) surfaces of group-IV semiconductors reconstruct by forming dimers of surface atoms. Understanding the precise atomic geometry and vibrational properties of these surfaces is essential for interpreting experimental data from diffraction, spectroscopy, and scattering experiments. This task focuses on the Ge(001) surface, where the p(2×1) asymmetric (tilted-dimer) reconstruction is an important structural motif. Your objective is to compute the structural relaxation parameters (bulk lattice constant, reconstruction energy, dimer bond length, tilt angle) and selected surface phonon frequencies of this reconstruction from first principles.

## Approach
The computations are performed within density-functional theory (DFT) in the local-density approximation (LDA) and density-functional perturbation theory (DFPT). The surface is modeled as a periodic slab of germanium with a vacuum gap, using a plane-wave basis set and norm-conserving pseudopotentials to describe the electron–ion interaction. First, the equilibrium bulk lattice constant of germanium is obtained from total-energy calculations of the diamond structure. A slab with a p(2×1) surface unit cell is then set up using the computed bulk lattice constant, and the atomic positions are relaxed to reach the asymmetric dimer ground state. From the relaxed configuration you extract the structural parameters. Next, DFPT is employed to compute the dynamical matrices on a grid of wavevectors in the irreducible surface Brillouin zone, and the phonon frequencies at the Γ and K high-symmetry points are determined. All calculations are carried out with the open-source Quantum ESPRESSO suite (pw.x and ph.x) and a suitable LDA pseudopotential for Ge.

## Reproduction target
Carry out a DFT-based workflow to obtain the following quantities for the Ge(001) p(2×1) reconstructed surface: (1) The equilibrium bulk lattice constant of germanium in angstroms. (2) The reconstruction energy per dimer in electronvolts, relative to a bulk-like reference. (3) The dimer bond length in angstroms and the dimer tilt angle in degrees from the relaxed slab. (4) The energies (meV) of the surface rocking mode at the Γ point, the dimer stretch modes ds1 and ds2 at the K point, and the back-bond stretching modes sb and sb2 at the K point. Write these results into the two JSON files as specified in the workflow.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Norm-conserving pseudopotential for Ge: https://www.materialscloud.org/discover/sssp

## Workflow steps

### Step 1: Compute bulk lattice constant of Ge
- Role: process
- Action: Run a series of DFT total-energy calculations for bulk Ge in the diamond structure at several lattice parameters; fit an equation of state to find the equilibrium lattice constant a0(Ge).
- Evidence: `/app/outputs/bulk_lattice_constant.txt`

### Step 2: Relax Ge(001) p(2×1) asymmetric slab
- Role: process
- Action: Using the bulk lattice constant from Step 01, set up a Ge(001) slab with 10 atomic layers and vacuum of 6 interlayer distances in the p(2×1) periodicity. Introduce an in-plane displacement of 0.4 Å and an out-of-plane displacement of 0.2 Å for the two surface atoms to obtain the tilted-dimer configuration. Perform ionic relaxation with symmetry constraints until forces are below 0.1 mRy/a.u.
- Evidence: `/app/outputs/relaxed_slab_structure.log`

### Step 3: Report Ge(001) p(2×1) structural parameters
- Role: scored (load-bearing)
- Action: From the bulk lattice constant (Step 01) and the relaxed slab (Step 02), compute and write the structural parameters: bulk lattice constant a0, reconstruction energy per dimer (relative to bulk-like reference), dimer bond length, and dimer tilt angle.
- Output file: `/app/outputs/structural_parameters.json`
- Format: json
- Contract: {"bulk_lattice_constant_angstrom": <float>, "reconstruction_energy_eV_per_dimer": <float>, "dimer_bond_length_angstrom": <float>, "dimer_tilt_angle_degrees": <float>}
- Scoring: scored by hidden verifier

### Step 4: DFPT phonon calculation for Ge(001) p(2×1)
- Role: process
- Action: Using the relaxed slab from Step 02, run DFPT (ph.x) on a (6,4) q-point mesh in the irreducible surface Brillouin zone to compute dynamical matrices and obtain phonon frequencies.
- Evidence: `/app/outputs/phonon_calculation.log`

### Step 5: Report high-symmetry phonon frequencies
- Role: scored (load-bearing)
- Action: From the DFPT results (Step 04), extract the energies (meV) of the surface rocking mode at Γ, and the dimer stretch modes ds1, ds2 and the back-bond stretching modes sb, sb2 at the K point. Write them to a JSON file.
- Output file: `/app/outputs/phonon_frequencies.json`
- Format: json
- Contract: {"rocking_mode_Gamma_meV": <float>, "dimer_stretch_ds1_K_meV": <float>, "dimer_stretch_ds2_K_meV": <float>, "backbond_sb_K_meV": <float>, "backbond_sb2_K_meV": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/structural_parameters.json`
- `/app/outputs/phonon_frequencies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### structural_parameters.json
- path: `/app/outputs/structural_parameters.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Scored artifact containing the key structural parameters of the Ge(001) p(2×1) asymmetric reconstruction: bulk lattice constant, reconstruction energy per dimer, dimer bond length, and dimer tilt angle.
- schema:
  - `type`: object
  - `required`:
    - `bulk_lattice_constant_angstrom`: number
    - `reconstruction_energy_eV_per_dimer`: number
    - `dimer_bond_length_angstrom`: number
    - `dimer_tilt_angle_degrees`: number

### phonon_frequencies.json
- path: `/app/outputs/phonon_frequencies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Scored artifact containing the phonon frequencies (meV) at high-symmetry points: rocking mode at Γ, dimer stretch modes ds1 and ds2 at K, and back-bond stretching modes sb and sb2 at K.
- schema:
  - `type`: object
  - `required`:
    - `rocking_mode_Gamma_meV`: number
    - `dimer_stretch_ds1_K_meV`: number
    - `dimer_stretch_ds2_K_meV`: number
    - `backbond_sb_K_meV`: number
    - `backbond_sb2_K_meV`: number

Notes: All quantities are checked against the paper's reported values with appropriate tolerances (e.g., ±0.05 Å for lattice constant, ±1 meV for phonon frequencies). The reconstruction energy and other structural parameters are deterministic and do not admit a 'better' direction; they are scored by exact match within tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "structural_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "bulk_lattice_constant_angstrom": "number",
          "reconstruction_energy_eV_per_dimer": "number",
          "dimer_bond_length_angstrom": "number",
          "dimer_tilt_angle_degrees": "number"
        }
      },
      "description": "Scored artifact containing the key structural parameters of the Ge(001) p(2×1) asymmetric reconstruction: bulk lattice constant, reconstruction energy per dimer, dimer bond length, and dimer tilt angle."
    },
    {
      "file": "phonon_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "rocking_mode_Gamma_meV": "number",
          "dimer_stretch_ds1_K_meV": "number",
          "dimer_stretch_ds2_K_meV": "number",
          "backbond_sb_K_meV": "number",
          "backbond_sb2_K_meV": "number"
        }
      },
      "description": "Scored artifact containing the phonon frequencies (meV) at high-symmetry points: rocking mode at Γ, dimer stretch modes ds1 and ds2 at K, and back-bond stretching modes sb and sb2 at K."
    }
  ],
  "notes": "All quantities are checked against the paper's reported values with appropriate tolerances (e.g., ±0.05 Å for lattice constant, ±1 meV for phonon frequencies). The reconstruction energy and other structural parameters are deterministic and do not admit a 'better' direction; they are scored by exact match within tolerance."
}
```

## How you are scored
Your submission is automatically evaluated by a hidden verifier that inspects the output files you produce. The verifier checks that both structural_parameters.json and phonon_frequencies.json contain the required fields and that the numerical values are within reasonable tolerances of the expected physical results. The intermediate evidence files (bulk_lattice_constant.txt, relaxed_slab_structure.log, phonon_calculation.log) are also checked for existence to confirm that the computational steps were executed. The final score is a weighted sum of the correctness of the structural parameters and the phonon frequencies, with a small weight given to the presence of process evidence. The verifier assesses whether your computational pipeline reproduces the target geometry and vibrations, not whether you guess the expected numbers.
