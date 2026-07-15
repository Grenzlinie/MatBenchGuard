# Computational Evaluation of Stability and Oxygen Reduction Performance of a Metal-Free Porphyrin Sheet

## Problem background
Proton exchange membrane fuel cells (PEMFCs) suffer from sluggish oxygen reduction reaction (ORR) kinetics at the cathode, and conventional platinum-based catalysts are both expensive and prone to degradation. Metal-free carbon-based materials have emerged as promising alternatives, but many struggle to dissociate O2 efficiently. This work investigates a two-dimensional material—a porphyrin sheet where a C=C dimer replaces the traditional metal centre—as a potential metal-free ORR catalyst. The central claim is that this C=C embedded porphyrin sheet is dynamically and thermally stable, possesses a narrow band gap, and can catalyse O2 dissociation with a very low barrier, leading to high ORR activity comparable to platinum. The task is to reproduce the key computed quantities that underpin these claims using open-source density functional theory (DFT) and microkinetic modelling.

## Approach
The evaluation uses periodic plane-wave DFT with the PBE functional for geometry relaxation and energetics. Dynamical stability is probed by computing phonon frequencies (via density-functional perturbation theory or finite displacements). Thermal stability at 300 K is assessed through NVT ab initio molecular dynamics (AIMD) in a supercell. The O2 dissociation barrier on the C=C dimer site is located using the nudged elastic band (NEB) method. The full ORR free-energy landscape is constructed by computing adsorption energies of reaction intermediates (O*, OH*, OOH*, etc.), applying zero-point energy, entropy, and solvation corrections within the computational hydrogen electrode (CHE) model. A steady-state microkinetic model that couples these free-energy changes and kinetic barriers is then solved to obtain surface coverages and the partial current density at an applied potential of 0.65 V vs. SHE. Finally, the quasi-direct band gap is computed using the HSE06 screened hybrid functional. All simulations employ publicly available open-source codes (Quantum ESPRESSO, CP2K, and associated post-processing tools).

## Reproduction target
The goal is to produce and report the following five quantities for the planar C=C embedded porphyrin sheet:

1. **Minimum phonon frequency** (in THz) — to verify the absence of imaginary modes, indicating dynamical stability.
2. **Standard deviation of the total energy** (eV) and **maximum out-of-plane atomic displacement** (Å) from a 5 ps NVT AIMD trajectory at 300 K — indicators of thermal stability.
3. **O₂ dissociation energy barrier** (eV) on the C=C dimer site — a measure of catalytic ease.
4. **Partial current density** (mA/cm²) at an applied potential of 0.65 V vs. SHE predicted by the microkinetic model — the primary ORR activity descriptor.
5. **HSE06 quasi-direct band gap** (eV) — an electronic property relevant to (photo-)electrochemical performance.

These quantities are to be computed from first principles following the outlined protocol and written as structured JSON artifacts; the task is not to match any pre-specified numerical values but to faithfully reproduce the underlying computational methodology.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- CP2K: https://www.cp2k.org/
- Phonopy: phonopy
- ASE (Atomic Simulation Environment): ase
- pymatgen: pymatgen
- NEB implementation (Quantum ESPRESSO neb.x or ASE NEB)

## Workflow steps

### Step 1: Relax primitive cell of C=C porphyrin sheet
- Role: process
- Action: Perform DFT optimization of the primitive cell of the planar C=C embedded porphyrin sheet using the PBE functional, with moderate convergence criteria.
- Evidence: `/app/outputs/relaxed_structure.xyz`

### Step 2: Tight relaxation for phonon calculation
- Role: process
- Action: Re-optimize the structure with tighter convergence to ensure accurate phonon frequencies.
- Evidence: `/app/outputs/tight_relaxed_structure.xyz`

### Step 3: Compute phonon frequencies
- Role: scored
- Action: Calculate phonon frequencies at high-symmetry points (or full BZ) using density-functional perturbation theory or finite displacements, and verify that no imaginary frequencies exist.
- Output file: `/app/outputs/step_01_phonon_stability.json`
- Format: json
- Contract: {"minimum_phonon_frequency": float (THz), "unit": "THz"}
- Scoring: scored by hidden verifier

### Step 4: AIMD simulation at 300 K
- Role: scored
- Action: Run NVT AIMD at 300 K for over 5 ps using a 2x2x1 supercell, then analyze the total energy trajectory and geometry snapshots to obtain the standard deviation of total energy and the maximum out-of-plane atomic displacement.
- Output file: `/app/outputs/step_02_aimd_stability.json`
- Format: json
- Contract: {"total_energy_std_ev": float, "max_out_of_plane_displacement_A": float}
- Scoring: scored by hidden verifier

### Step 5: Compute O2 dissociation barrier
- Role: scored
- Action: Adsorb O2 on the C=C dimer in a side-on configuration, locate the transition state for O2 dissociation using NEB or dimer method, and report the barrier height.
- Output file: `/app/outputs/step_03_o2_dissociation_barrier.json`
- Format: json
- Contract: {"dissociation_barrier_eV": float}
- Scoring: scored by hidden verifier

### Step 6: Construct ORR free energy diagram (CHE model)
- Role: process
- Action: Compute DFT energies for all ORR intermediates (O*, OH*, OOH*, etc.) in their most stable adsorption configurations, apply zero-point energy, entropy, and solvation corrections, and construct free energy profiles using the computational hydrogen electrode (CHE) model. Generate the data needed for microkinetics.
- Evidence: `/app/outputs/free_energies.json`

### Step 7: Solve microkinetic model for partial current density
- Role: scored (load-bearing)
- Action: Using the obtained free energy changes and kinetic barriers, set up the steady-state microkinetic equations for the dissociative pathway and solve for surface coverages and partial current density at an applied potential of 0.65 V vs. SHE.
- Output file: `/app/outputs/step_04_current_density.json`
- Format: json
- Contract: {"partial_current_density_at_0_65V_mA_per_cm2": float}
- Scoring: scored by hidden verifier

### Step 8: Compute HSE06 band gap
- Role: scored
- Action: Using the relaxed geometry, perform a band structure calculation with the HSE06 hybrid functional and extract the band gap.
- Output file: `/app/outputs/step_05_band_gap.json`
- Format: json
- Contract: {"hse06_band_gap_eV": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_phonon_stability.json`
- `/app/outputs/step_02_aimd_stability.json`
- `/app/outputs/step_03_o2_dissociation_barrier.json`
- `/app/outputs/step_04_current_density.json`
- `/app/outputs/step_05_band_gap.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_phonon_stability.json
- path: `/app/outputs/step_01_phonon_stability.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Minimum phonon frequency across high-symmetry points. Must be non-negative (threshold: > -0.1 THz to account for numerical noise) indicating dynamical stability.
- schema:
  - `type`: object
  - `required`:
    - `minimum_phonon_frequency`: float (THz)
    - `unit`: string (must be 'THz')

### step_02_aimd_stability.json
- path: `/app/outputs/step_02_aimd_stability.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Metrics from 5 ps NVT AIMD at 300 K: standard deviation of total energy and maximum out-of-plane atomic displacement. Must be below thresholds indicating thermal stability.
- schema:
  - `type`: object
  - `required`:
    - `total_energy_std_ev`: float (eV)
    - `max_out_of_plane_displacement_A`: float (Å)

### step_03_o2_dissociation_barrier.json
- path: `/app/outputs/step_03_o2_dissociation_barrier.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Energy barrier for O2 dissociation on the C=C dimer. Lower barrier indicates better catalytic performance.
- schema:
  - `type`: object
  - `required`:
    - `dissociation_barrier_eV`: float (eV)

### step_04_current_density.json
- path: `/app/outputs/step_04_current_density.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Partial current density at 0.65 V vs. SHE predicted by the microkinetic model. Higher value indicates better ORR activity.
- schema:
  - `type`: object
  - `required`:
    - `partial_current_density_at_0_65V_mA_per_cm2`: float (mA/cm²)

### step_05_band_gap.json
- path: `/app/outputs/step_05_band_gap.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Quasi-direct band gap computed with the HSE06 hybrid functional. Must match the reference within a tolerance.
- schema:
  - `type`: object
  - `required`:
    - `hse06_band_gap_eV`: float (eV)

Notes: The agent must use open-source DFT codes (Quantum ESPRESSO, CP2K) to compute all quantities. The scoring compares the reported values against hidden reference data from the paper with appropriate tolerances and threshold policies. The microkinetics step is load-bearing because it depends on all earlier calculations and requires correct simulation of the free-energy landscape.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_phonon_stability.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "minimum_phonon_frequency": "float (THz)",
          "unit": "string (must be 'THz')"
        }
      },
      "description": "Minimum phonon frequency across high-symmetry points. Must be non-negative (threshold: > -0.1 THz to account for numerical noise) indicating dynamical stability."
    },
    {
      "file": "step_02_aimd_stability.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "total_energy_std_ev": "float (eV)",
          "max_out_of_plane_displacement_A": "float (Å)"
        }
      },
      "description": "Metrics from 5 ps NVT AIMD at 300 K: standard deviation of total energy and maximum out-of-plane atomic displacement. Must be below thresholds indicating thermal stability."
    },
    {
      "file": "step_03_o2_dissociation_barrier.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "dissociation_barrier_eV": "float (eV)"
        }
      },
      "description": "Energy barrier for O2 dissociation on the C=C dimer. Lower barrier indicates better catalytic performance."
    },
    {
      "file": "step_04_current_density.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "partial_current_density_at_0_65V_mA_per_cm2": "float (mA/cm²)"
        }
      },
      "description": "Partial current density at 0.65 V vs. SHE predicted by the microkinetic model. Higher value indicates better ORR activity."
    },
    {
      "file": "step_05_band_gap.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "hse06_band_gap_eV": "float (eV)"
        }
      },
      "description": "Quasi-direct band gap computed with the HSE06 hybrid functional. Must match the reference within a tolerance."
    }
  ],
  "notes": "The agent must use open-source DFT codes (Quantum ESPRESSO, CP2K) to compute all quantities. The scoring compares the reported values against hidden reference data from the paper with appropriate tolerances and threshold policies. The microkinetics step is load-bearing because it depends on all earlier calculations and requires correct simulation of the free-energy landscape."
}
```

## How you are scored
A hidden verifier independently checks each scored output file (phonon_stability.json, aimd_stability.json, o2_dissociation_barrier.json, current_density.json, band_gap.json). For each artifact, the verifier compares the reported values against reference benchmarks from the original computational study using appropriate policies: tolerances for exact quantities, threshold-or-better comparisons for performance metrics, and directional consistency checks. The verification does not simply check whether a file exists or conforms to the schema; it evaluates whether the numerical results are consistent with a correct execution of the described computational workflow. The per-stage scores are combined into a single weighted reward; larger weight is given to the microkinetic partial current density, which depends on all preceding steps. Simply writing arbitrary numbers or re‑stating nominal target values is not sufficient—the compute steps must be genuinely carried out to produce artefacts that survive the verifier’s scrutiny.
