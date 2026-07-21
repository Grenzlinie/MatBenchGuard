# DFT+U investigation of interlayer hybridization in a 1H/1T TaS2 bilayer

## Problem background
In van der Waals heterostructures composed of 1H and 1T polymorphs of TaS₂, scanning tunneling microscopy (STM) images of the 1H surface often reveal a superimposed superstructure: the `(√13×√13)R13.9°` charge density wave (CDW) periodicity characteristic of the underlying 1T layer. The origin of this 'transparency effect' is debated—whether it results from simple tunneling through the decoupled 1H layer or from a genuine electronic coupling and hybridization between the layers. Resolving this question is essential for understanding the interlayer interactions that govern the emergent correlated phases in such systems. First-principles density functional theory (DFT) calculations provide a direct route to probe the electronic structure: by computing the local density of states (LDOS) above the 1H layer, one can investigate whether the LDOS inherits the CDW modulation from the 1T layer. This computational reproduction task aims to determine the nature of the interlayer coupling by simulating the bilayer system and analyzing the LDOS in an energy window that spans the upper Hubbard band of the 1T layer.

## Approach
The computation follows a DFT+U approach with van der Waals corrections (PBE+D3(BJ)). Two separate supercells are first relaxed: a 3×3 supercell of 1H‑TaS₂ (trigonal prismatic) and a √13×√13 supercell of 1T‑TaS₂ containing the star‑of‑David CDW distortion. The relaxed structures are then combined into a bilayer model, expanding the 1H in‑plane lattice by 1% to match the CDW‑reconstructed 1T lattice. A spin‑polarized self‑consistent field calculation is performed on the bilayer using Hubbard U corrections for Ta d electrons (different U parameters for the 1T and 1H layers). From the converged charge density, a non‑self‑consistent calculation provides the LDOS on a uniform grid in a plane 1.5 Å above the outermost sulfur atoms of the 1H layer. The LDOS is integrated over a chosen energy interval just above the Fermi level—corresponding to the region where the upper Hubbard band of the 1T layer is expected. The resulting real‑space map is then amenable to 2D Fourier analysis to identify periodic components. The workflow therefore consists of geometry optimization, bilayer construction, self‑consistent DFT+U calculation, and finally the LDOS extraction.

## Reproduction target
Produce a CSV file (`ldos_ef_200meV.csv`) containing the integrated local density of states on a rectangular grid at a height of 1.5 Å above the outer sulfur atoms of the 1H layer, integrated over the energy interval from the Fermi level (EF) to EF + 200 meV. The grid must cover at least one full √13×√13 supercell with a spacing of ≤ 0.1 Å. The file must have a header row and three columns: `x` (Å), `y` (Å), and `integrated_LDOS` (arbitrary units). The hidden verifier will subsequently read this file, perform a 2D Fast Fourier Transform, and examine the reciprocal‑space pattern for signatures of the (√13×√13)R13.9° superstructure, thereby assessing whether the LDOS above the 1H layer reflects the CDW periodicity of the underlying 1T layer.

## Assets

- Crystal structure of 1T-TaS2 with (√13×√13)R13.9° star-of-David CDW distortion
- Crystal structure of 1H-TaS2 (3×3 supercell, trigonal prismatic)
- Open-source DFT code (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/
- PBE PAW pseudopotentials for Ta and S: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Geometry optimization of 1H and 1T supercells
- Role: process
- Action: Perform DFT geometry optimization of the 3x3 1H-TaS2 supercell and the √13×√13 1T-TaS2 supercell (star-of-David CDW) using PBE+vdW (Grimme D3 with BJ damping). Relax all atomic positions and in-plane lattice parameters to obtain low-energy configurations.
- Evidence: `/app/outputs/relaxation_log.txt`

### Step 2: Build 1H/1T bilayer model
- Role: process
- Action: Combine the optimized supercells, align the atomic lattices, and expand the 1H in-plane lattice by 1% to match the CDW-reconstructed 1T supercell. Save the bilayer atomic structure file in a standard crystallographic format.
- Evidence: `/app/outputs/bilayer_structure.cif`

### Step 3: Spin-polarized DFT+U self-consistent calculation
- Role: process
- Action: Perform a spin-polarized GGA+U self-consistent field calculation on the bilayer using PBE+vdW and Hubbard U parameters (U_1T=2.13 eV, J_1T=0.37 eV; U_1H=3.18 eV, J_1H=0.37 eV) to obtain the ground-state charge density and wave functions.
- Evidence: `/app/outputs/scf_output.log`

### Step 4: LDOS map above 1H surface
- Role: scored (load-bearing)
- Action: From the converged charge density, perform a non-self-consistent DFT calculation to compute the local density of states (LDOS) on a uniform rectangular grid in a plane 1.5 Å above the outer S atoms of the 1H layer. Integrate the LDOS over the energy interval [EF, EF+200 meV] and save the result as a CSV file with columns x (float, Å), y (float, Å), integrated_LDOS (float, arbitrary units). The grid must cover at least one full (√13×√13) supercell with spacing ≤ 0.1 Å.
- Output file: `/app/outputs/ldos_ef_200meV.csv`
- Format: csv
- Contract: A CSV table with header: x (float, Å), y (float, Å), integrated_LDOS (float, arb. units). The grid must be rectangular and dense enough (spacing ≤ 0.1 Å) to resolve the CDW superstructure in a subsequent 2D FFT.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ldos_ef_200meV.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ldos_ef_200meV.csv
- path: `/app/outputs/ldos_ef_200meV.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Real-space local density of states integrated from EF to EF+200 meV on a plane 1.5 Å above the outer S atoms of the 1H layer. The checker computes its 2D Fourier transform and verifies the presence of peaks at the reciprocal lattice vectors of the (√13×√13)R13.9° superstructure, confirming the CDW transparency effect.
- schema:
  - `type`: table
  - `required_columns`: `x`, `y`, `integrated_LDOS`
  - `units`:
    - `x`: Angstrom
    - `y`: Angstrom
    - `integrated_LDOS`: arbitrary units

Notes: The checker performs a structural audit (T3) using 2D FFT to detect peaks at the expected CDW reciprocal lattice vectors. No absolute numeric value is compared; scoring is based on the presence and relative amplitude of those peaks. The raw energy positions of the Hubbard bands are not scored, only the LDOS periodicity.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ldos_ef_200meV.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "y",
          "integrated_LDOS"
        ],
        "units": {
          "x": "Angstrom",
          "y": "Angstrom",
          "integrated_LDOS": "arbitrary units"
        }
      },
      "description": "Real-space local density of states integrated from EF to EF+200 meV on a plane 1.5 Å above the outer S atoms of the 1H layer. The checker computes its 2D Fourier transform and verifies the presence of peaks at the reciprocal lattice vectors of the (√13×√13)R13.9° superstructure, confirming the CDW transparency effect."
    }
  ],
  "notes": "The checker performs a structural audit (T3) using 2D FFT to detect peaks at the expected CDW reciprocal lattice vectors. No absolute numeric value is compared; scoring is based on the presence and relative amplitude of those peaks. The raw energy positions of the Hubbard bands are not scored, only the LDOS periodicity."
}
```

## How you are scored
A hidden verifier (not visible to the solver) will independently inspect every required output artifact. For the scored step (Step 4), the verifier reads `ldos_ef_200meV.csv`, interpolates to a regular grid if needed, computes its 2D Fourier transform, and identifies peaks. It checks whether prominent peaks appear at the reciprocal lattice vectors expected for the (√13×√13)R13.9° superstructure (relative to the atomic lattice) and whether their amplitudes exceed a hidden threshold relative to the main atomic‑lattice peaks. The reward for this stage is monotonic in the quality of the recovered CDW periodicity: a clear, correctly oriented set of superlattice peaks yields full credit, while missing or very weak peaks reduce the score. The preceding process steps (geometry optimization, bilayer construction, and SCF calculation) are required for a valid submission but do not directly carry reward weight; their evidence files are checked only for completeness. The final overall reward is a weighted combination of the scored stage's output quality.
