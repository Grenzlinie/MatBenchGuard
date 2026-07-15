# Spin-polarized DFT study of TM-embedded carbon nitride monolayers

## Problem background
Two-dimensional (2D) ferromagnetic materials are crucial for spintronics applications. This task investigates transition-metal (TM = Cr, Mn, Fe) embedded triazine-based graphitic carbon nitride (TM@gt-C3N4) monolayers using spin-polarized density functional theory with on-site Hubbard U corrections (DFT+U). The goal is to compute the relative stability of magnetic configurations, local magnetic moments, spin-resolved band gaps, and the mean-field Curie temperature from exchange energies. Such properties determine the suitability of these materials for high-temperature spintronics.

## Approach
Construct the hexagonal unit cell of triazine-based gt-C3N4 from known crystallographic parameters (lattice constant, bond lengths). Embed each transition metal (Cr, Mn, Fe) in the pore of the monolayer, with Cr adopting a tetra-coordinated geometry and Mn/Fe trigonal coordination. Use a 2×2 supercell for magnetic calculations. Perform spin-polarized DFT structural relaxations with the PBE+U functional (U=4 eV, J=1 eV on TM d orbitals) and sufficient vacuum and k-point sampling. On the relaxed supercells, run static total-energy calculations for three magnetic configurations: non-spin-polarized (NSP), ferromagnetic (FM, all TM moments aligned), and antiferromagnetic (AFM, opposite alignment on two TM atoms in the supercell). Obtain total energies, local magnetic moments, and spin-resolved electronic structure (density of states and band structure) to determine spin-up and spin-down band gaps. From the energy difference between FM and AFM states, compute the exchange energy and estimate the Curie temperature via mean-field theory: Tc = (2 * E_ex) / (3 * kB * S), where S = μ/μB and kB is the Boltzmann constant. Compute the stabilisation energies ΔE(FM−NSP) and ΔE(FM−AFM) per TM atom.

## Reproduction target
Compute and report in a structured JSON file for each TM (Cr, Mn, Fe): (i) the energy difference (meV per TM) between the ferromagnetic (FM) state and the non-spin-polarized (NSP) state, and between FM and antiferromagnetic (AFM) state; (ii) the local magnetic moment on the TM atom in μB; (iii) the spin-up and spin-down band gaps (in eV); (iv) the Curie temperature (in K) estimated from the exchange energy via mean-field theory. Assemble the results in `/app/outputs/tm_gt_c3n4_results.json`.

## Assets

- Atomic Simulation Environment (ASE): https://pypi.org/project/ase/
- Open-source DFT code (GPAW or Quantum ESPRESSO): https://gitlab.com/gpaw/gpaw (pip install gpaw) or https://www.quantum-espresso.org/
- PBE PAW/ultrasoft pseudopotentials: https://wiki.fysik.dtu.dk/gpaw/setups/ (GPAW) or https://www.quantum-espresso.org/pseudopotentials/ (QE)
- Triazine-based gt-C3N4 crystal structure parameters

## Workflow steps

### Step 1: Build initial structures of pristine and TM-embedded supercells
- Role: process
- Action: Construct the hexagonal unit cell of triazine-based gt-C3N4 using established lattice parameters and atomic positions. Build 2×2 supercells and embed each transition metal (Cr, Mn, Fe) at the pore site, following the coordination geometries described in the paper (tetra-coordinated for Cr, trigonal for Mn and Fe). Prepare initial atomic structures in a format suitable for the chosen DFT code.
- Evidence: `/app/outputs/initial_structures.log`

### Step 2: Geometry optimization of TM@gt-C3N4 systems
- Role: process
- Action: For each TM (Cr, Mn, Fe), perform spin-polarized DFT structural relaxation of the 2×2 supercell using the PBE+U functional with Hubbard U=4 eV and J=1 eV applied to TM d orbitals. Use appropriate vacuum spacing (≈12 Å) and k-point mesh. Obtain optimized atomic positions and final total energies.
- Evidence: `/app/outputs/optimization.log`

### Step 3: Static total-energy calculations for competing magnetic configurations
- Role: process
- Action: On the optimized 2×2 supercells, run static spin-polarized DFT calculations for three magnetic configurations: non-spin-polarized (NSP), ferromagnetic (FM, all TM moments aligned), and antiferromagnetic (AFM, opposite alignment on two TM atoms in the supercell). Collect the total energy of each configuration.
- Evidence: `/app/outputs/mag_energies.log`

### Step 4: Electronic structure analysis and final result compilation
- Role: scored (load-bearing)
- Action: Perform a spin-polarized DFT calculation on the FM ground state of each TM system using a dense k-point mesh to obtain the density of states (DOS) and band structure. Extract: (i) the spin-up and spin-down band gaps; (ii) the local magnetic moment on the TM atom. From the total energies of step_03, compute the energy differences ΔE(FM−NSP) and ΔE(FM−AFM). Calculate the exchange energy E_ex = E(FM) − E(AFM) and estimate the Curie temperature via mean-field theory using Tc = (2 * E_ex) / (3 * kB * S), with S = μ/μB. Assemble all results into a single JSON file.
- Output file: `/app/outputs/tm_gt_c3n4_results.json`
- Format: json
- Contract: { "Cr": { "energy_diff_FM_NSP_meV_per_TM": <number>, "energy_diff_FM_AFM_meV_per_TM": <number>, "local_magnetic_moment_muB": <number>, "spin_up_band_gap_eV": <number>, "spin_down_band_gap_eV": <number>, "Curie_temperature_K": <number> }, "Mn": { ... }, "Fe": { ... } }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/tm_gt_c3n4_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### tm_gt_c3n4_results.json
- path: `/app/outputs/tm_gt_c3n4_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Derived magnetic and electronic properties for Cr-, Mn-, and Fe-embedded gt-C3N4 monolayers. Scores each quantity against paper-reported reference values using appropriate per-quantity tolerances and threshold checks (e.g., Curie temperature must exceed 400 K for Cr).
- schema:
  - `type`: object
  - `required`: `Cr`, `Mn`, `Fe`
  - `description`: Each key maps to an object with the following numeric fields:
  - `fields`:
    - `energy_diff_FM_NSP_meV_per_TM`: number (energy difference in meV per transition metal atom)
    - `energy_diff_FM_AFM_meV_per_TM`: number (energy difference in meV per transition metal atom)
    - `local_magnetic_moment_muB`: number (local magnetic moment in Bohr magnetons)
    - `spin_up_band_gap_eV`: number (spin-up band gap in eV; negative if metallic)
    - `spin_down_band_gap_eV`: number (spin-down band gap in eV)
    - `Curie_temperature_K`: number (Curie temperature in kelvin)

Notes: The hidden checker compares each field to the paper's reported values with tolerances that account for differences between DFT codes. Half-metallicity is indirectly scored via the spin band gaps.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "tm_gt_c3n4_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Cr",
          "Mn",
          "Fe"
        ],
        "description": "Each key maps to an object with the following numeric fields:",
        "fields": {
          "energy_diff_FM_NSP_meV_per_TM": "number (energy difference in meV per transition metal atom)",
          "energy_diff_FM_AFM_meV_per_TM": "number (energy difference in meV per transition metal atom)",
          "local_magnetic_moment_muB": "number (local magnetic moment in Bohr magnetons)",
          "spin_up_band_gap_eV": "number (spin-up band gap in eV; negative if metallic)",
          "spin_down_band_gap_eV": "number (spin-down band gap in eV)",
          "Curie_temperature_K": "number (Curie temperature in kelvin)"
        }
      },
      "description": "Derived magnetic and electronic properties for Cr-, Mn-, and Fe-embedded gt-C3N4 monolayers. Scores each quantity against paper-reported reference values using appropriate per-quantity tolerances and threshold checks (e.g., Curie temperature must exceed 400 K for Cr)."
    }
  ],
  "notes": "The hidden checker compares each field to the paper's reported values with tolerances that account for differences between DFT codes. Half-metallicity is indirectly scored via the spin band gaps."
}
```

## How you are scored
A hidden verifier reads your `tm_gt_c3n4_results.json` and compares each reported quantity to the paper's expected result using tolerance windows that accommodate differences between DFT codes and functionals. Magnetic moments and energy differences are scored based on agreement within tolerances; half-metallicity is assessed from the spin band gaps (one spin channel metallic/nearly metallic, the other semiconducting); and the Curie temperature for Cr must be consistent with a high-temperature ferromagnet. Reporting the paper's values alone is insufficient — the checker evaluates whether your computed numbers, obtained from the full DFT workflow, fall within realistic bounds. The final reward is a weighted sum of partial scores across all fields.
