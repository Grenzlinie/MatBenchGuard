# Hybrid-improper ferroelectricity in antiperovskite oxide superlattices: phonon instability analysis and strain-tuned polarization

## Problem background
Anti-perovskite oxides with formula A₃BO are structurally related to perovskites but with inverted cation/anion positions. Hybrid-improper ferroelectricity (HIF) can arise from trilinear coupling of non-polar octahedral rotations and tilting distortions that induce a polar distortion, without the need for a polar phonon instability. This task investigates HIF in the [001] (Ba₃SiO)₁/(Ba₃GeO)₁ oxide antiperovskite superlattice using first-principles density-functional-theory (DFT) phonon calculations. The aim is to compute the unstable phonon modes responsible for the structural instabilities, to determine the relative stabilities of the resulting low-symmetry phases, and to evaluate the spontaneous polarization and its tunability by biaxial strain.

## Approach
The computational protocol uses the open-source plane-wave DFT code Quantum ESPRESSO with the PBEsol exchange-correlation functional and SSSP pseudopotentials. Starting from the experimental lattice parameters, a tetragonal P4/mmm high-symmetry superlattice is built. The full phonon dispersion is obtained with the finite-displacement method via Phonopy. Unstable (imaginary frequency) modes at the zone-boundary points X and M are identified and their irreducible representations (symmetry labels) are assigned using spglib or equivalent symmetry analysis. The dominant unstable modes are then condensed (atomic displacements superposed onto the high-symmetry structure) to generate candidate low-symmetry phases: P4/mbm, Pmma, and the polar Pmc2₁. These phases are fully relaxed (cell parameters and atomic positions) with DFT. Relative total energies with respect to the P4/mmm reference are collected. For the polar Pmc2₁ ground state, the spontaneous polarization is computed via the Berry-phase method. The effect of biaxial in-plane strain is studied by imposing strains of −3% and +3%, re-relaxing internal coordinates, and recomputing the polarization. All calculations are performed with convergence parameters (k-point grid, energy cutoff) sufficiently strict to yield well-converged forces and energies.

## Reproduction target
The objective is to produce three scored deliverables from the DFT workflow:
- A list of the unstable phonon modes at the high-symmetry points X and M, each with its wave-vector point, irreducible representation (symmetry) label, and magnitude of the imaginary frequency (in cm⁻¹). This file is `unstable_modes.json`.
- The relative total energies (meV per formula unit) of the condensed phases P4/mbm, Pmma, and Pmc₂₁, referenced to the P4/mmm high-symmetry structure (which must be zero). This file is `phase_energies.json`.
- The spontaneous polarization (in μC/cm²) of the polar Pmc₂₁ ground state at three biaxial strain levels: 0%, −3%, and +3%. This file is `polarization_results.txt`.
The required file formats and exact schemas are detailed in the workflow steps below. The task does not rely on any external dataset; all inputs are derived from the known crystal structure and the computational protocol.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: https://phonopy.github.io/phonopy/
- SSSP pseudopotential library (efficiency/accuracy): https://www.materialscloud.org/discover/sssp/table
- spglib (via ASE or standalone): pip install spglib

## Workflow steps

### Step 1: Construct initial superlattice structure
- Role: process
- Action: Build the [001] (Ba3SiO)1/(Ba3GeO)1 superlattice in the tetragonal P4/mmm high-symmetry reference structure using the experimental lattice parameters of the bulk compounds (a ≈ 7.5 Å, c ≈ 10.7 Å) and create the necessary DFT input files.
- Evidence: `/app/outputs/initial_structure.cif`

### Step 2: Compute forces on displaced supercells
- Role: process
- Action: Using Quantum ESPRESSO (PBEsol functional, SSSP pseudopotentials), perform self-consistent field calculations on a 2×2×1 supercell of the P4/mmm structure with finite atomic displacements. Generate the set of Hellmann-Feynman force sets needed by Phonopy.
- Evidence: `/app/outputs/forces_collected.tgz`

### Step 3: Calculate phonon dispersion and eigenvectors
- Role: process
- Action: Run Phonopy with the computed forces to obtain the full phonon dispersion relations along the high-symmetry path Γ–X–M–Γ–A. Extract phonon frequencies and eigenvectors for further analysis.
- Evidence: `/app/outputs/phonon_band.yaml`

### Step 4: Identify and characterise unstable phonon modes
- Role: scored (load-bearing)
- Action: From the phonon eigenvectors, pick all modes with imaginary (negative squared) frequencies at the zone-boundary points X, M, and A. Determine their atomic displacement patterns and assign irreducible representation labels (X5–, M2+, M5–, M4–) using spglib/ISOTROPY or equivalent. Write the list to unstable_modes.json.
- Output file: `/app/outputs/unstable_modes.json`
- Format: json
- Contract: Array of objects: { 'point': string (e.g., 'X', 'M'), 'symmetry': string (e.g., 'X5-'), 'frequency': float (unit: cm⁻¹, positive value for imaginary magnitude) }
- Scoring: scored by hidden verifier

### Step 5: Condense unstable modes and relax low-symmetry phases
- Role: process
- Action: Superpose the dominant unstable mode displacement patterns (M2+ for in-phase rotation, M5– for tilting) onto the P4/mmm structure to create initial geometries for the P4/mbm, Pmma, and Pmc2_1 phases. Perform full DFT variable-cell relaxations (Quantum ESPRESSO) for each phase, allowing cell parameters and atomic positions to relax until forces are below a strict threshold.
- Evidence: `/app/outputs/relaxed_phases.tgz`

### Step 6: Compute relative phase energies
- Role: scored
- Action: Extract the total energies of the relaxed P4/mbm, Pmma, and Pmc2_1 phases relative to the P4/mmm high-symmetry structure. Write the results to phase_energies.json, with the P4/mmm energy set to zero and all values in meV per formula unit.
- Output file: `/app/outputs/phase_energies.json`
- Format: json
- Contract: JSON object with keys matching phase names (e.g., 'P4/mmm', 'P4/mbm', 'Pmma', 'Pmc2_1') and values as floats (energy per formula unit, meV/f.u.). P4/mmm must be 0.
- Scoring: scored by hidden verifier

### Step 7: Compute spontaneous polarization for unstrained Pmc2_1
- Role: process
- Action: Using the fully relaxed Pmc2_1 structure, run a Berry-phase polarization calculation (or the modern ‘modern polarization’ method) in Quantum ESPRESSO to obtain the spontaneous polarization (in μC/cm²) along the polar axis.
- Evidence: `/app/outputs/polarization_0.log`

### Step 8: Apply biaxial strains and compute polarization
- Role: process
- Action: For the relaxed Pmc2_1 structure, impose in-plane biaxial strains of –3% and +3% (i.e., stretch/compress a and b lattice vectors accordingly), re-relax the internal atomic coordinates within the strained cell, and compute the spontaneous polarization via the Berry-phase method for each strain.
- Evidence: `/app/outputs/strain_data.json`

### Step 9: Report polarization results
- Role: scored
- Action: Collect the computed polarization values for 0%, –3%, and +3% strain and write them to polarization_results.txt in the required format.
- Output file: `/app/outputs/polarization_results.txt`
- Format: txt
- Contract: Three lines (order independent): 'strain_0: <float> μC/cm²', 'strain_+3: <float> μC/cm²', 'strain_-3: <float> μC/cm²'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/unstable_modes.json`
- `/app/outputs/phase_energies.json`
- `/app/outputs/polarization_results.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### unstable_modes.json
- path: `/app/outputs/unstable_modes.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: List of unstable phonon modes: each entry specifies the high-symmetry Brillouin‑zone point, the irreducible representation (irrep) label, and the imaginary‑frequency magnitude. The checker verifies structural presence of expected irreps at X and M within a plausible frequency range.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `point`, `symmetry`, `frequency`
    - `properties`:
      - `point`:
        - `type`: string
      - `symmetry`:
        - `type`: string
      - `frequency`:
        - `type`: number
        - `description`: Positive magnitude of imaginary frequency in cm⁻¹

### phase_energies.json
- path: `/app/outputs/phase_energies.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: JSON object with the relative total energies (meV per formula unit) of the condensed phases, referenced to P4/mmm (which must be 0). The checker ensures Pmc2_1 has the lowest energy and that the ordering of energies is physically plausible.
- schema:
  - `type`: object
  - `required`: `P4/mmm`, `P4/mbm`, `Pmma`, `Pmc2_1`
  - `properties`:
    - `P4/mmm`:
      - `type`: number
    - `P4/mbm`:
      - `type`: number
    - `Pmma`:
      - `type`: number
    - `Pmc2_1`:
      - `type`: number

### polarization_results.txt
- path: `/app/outputs/polarization_results.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Three-line text file reporting the computed spontaneous polarization at the three required strain levels. The checker compares the reported values to hidden paper‑reference values (with a generous tolerance) and verifies the positive strain‑polarization trend.
- schema:
  - `type`: text
  - `pattern`: each line must be of the form: strain_<value>: <number> μC/cm²

Notes: All DFT‑based computational artifacts are expected to be obtained using the PBEsol functional and the SSSP pseudopotential library as listed in the resources. The absolute values may differ slightly from the original VASP results, but qualitative trends (unstable modes, energy ordering, polarization enhancement under tensile strain) must be preserved.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "unstable_modes.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "point",
            "symmetry",
            "frequency"
          ],
          "properties": {
            "point": {
              "type": "string"
            },
            "symmetry": {
              "type": "string"
            },
            "frequency": {
              "type": "number",
              "description": "Positive magnitude of imaginary frequency in cm⁻¹"
            }
          }
        }
      },
      "description": "List of unstable phonon modes: each entry specifies the high-symmetry Brillouin‑zone point, the irreducible representation (irrep) label, and the imaginary‑frequency magnitude. The checker verifies structural presence of expected irreps at X and M within a plausible frequency range."
    },
    {
      "file": "phase_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "P4/mmm",
          "P4/mbm",
          "Pmma",
          "Pmc2_1"
        ],
        "properties": {
          "P4/mmm": {
            "type": "number"
          },
          "P4/mbm": {
            "type": "number"
          },
          "Pmma": {
            "type": "number"
          },
          "Pmc2_1": {
            "type": "number"
          }
        }
      },
      "description": "JSON object with the relative total energies (meV per formula unit) of the condensed phases, referenced to P4/mmm (which must be 0). The checker ensures Pmc2_1 has the lowest energy and that the ordering of energies is physically plausible."
    },
    {
      "file": "polarization_results.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "pattern": "each line must be of the form: strain_<value>: <number> μC/cm²"
      },
      "description": "Three-line text file reporting the computed spontaneous polarization at the three required strain levels. The checker compares the reported values to hidden paper‑reference values (with a generous tolerance) and verifies the positive strain‑polarization trend."
    }
  ],
  "notes": "All DFT‑based computational artifacts are expected to be obtained using the PBEsol functional and the SSSP pseudopotential library as listed in the resources. The absolute values may differ slightly from the original VASP results, but qualitative trends (unstable modes, energy ordering, polarization enhancement under tensile strain) must be preserved."
}
```

## How you are scored
A hidden verifier independently checks the three scored artifacts. For `unstable_modes.json`, the verifier audits that modes with the expected symmetries (X₅⁻, M₂⁺, M₅⁻, M₄⁻) are present and that their imaginary frequencies fall within a physically plausible range. For `phase_energies.json`, it verifies that Pmc₂₁ has the lowest energy and that the ordering and approximate magnitudes are consistent with the structural transformations. For `polarization_results.txt`, it compares your reported polarization values to a hidden reference (with generous tolerance) and confirms that the polarization increases from 0% to +3% strain (positive trend). Each artifact contributes a weighted fraction to the total reward. Reporting numbers that match published literature values is not sufficient; the verifier inspects the structural soundness and internal consistency of your computed results.
