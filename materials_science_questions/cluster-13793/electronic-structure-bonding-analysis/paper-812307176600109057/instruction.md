# First-principles study of PbFe0.5Nb0.5O3 structure and polarization

## Problem background
Lead iron niobate PbFe₀.₅Nb₀.₅O₃ (PFN) is a complex perovskite ferroelectric with potential applications in nonvolatile ferroelectric memory and high-dielectric-constant DRAM. In this material, the B-site of the ABO₃ perovskite structure is jointly occupied by Fe and Nb cations. Understanding how the two different B-site species contribute to ferroelectricity is of fundamental interest. First-principles density functional theory (DFT) calculations, using a full-potential linearized augmented plane wave (FLAPW) method within the generalized gradient approximation (GGA), can determine the ground-state crystal structure and electronic properties. This task aims to compute the equilibrium lattice constant, atomic positions, and spontaneous polarization of PFN, which together characterize the ferroelectric ground state and the separate contributions of the Fe and Nb subcells. The results provide insight into the microscopic origin of ferroelectricity in this complex perovskite.

## Approach
The computational approach follows a standard FLAPW/GGA DFT procedure. A periodic supercell is constructed to model the PFN crystal, consisting of alternating [001] layers of PbFeO₃ and PbNbO₃ in a pseudocubic perovskite cell. The initial structure uses an approximate lattice parameter near 4.0 Å and ideal perovskite atomic positions.

The equilibrium lattice parameter a is determined by performing total-energy calculations at a series of cell volumes and fitting the resulting energy-volume data to an equation of state. Once the optimal volume is found, all atomic coordinates are relaxed within that cell until residual forces fall below a chosen convergence threshold. This yields the ferroelectric ground-state structure.

To evaluate the spontaneous polarization, a paraelectric reference structure is built as a cubic cell with the same lattice parameter and ideal centrosymmetric positions. Self-consistent DFT calculations are then performed for both the ferroelectric and paraelectric configurations, yielding wave functions, densities of states (total and projected), band structures, and electron density distributions. Finally, the Berry-phase polarization method is applied to compute the spontaneous polarization separately for the PbFeO₃ and PbNbO₃ subcells.

All calculations use the open-source FLAPW code ELK, which provides the GGA functional and Berry-phase polarization implementation needed to reproduce the workflow.

## Reproduction target
Re-run the DFT workflow to determine:
- The equilibrium lattice parameter a (in Å) of the PFN supercell and the relaxed fractional coordinates of all atoms, recorded in optimized_structure.json.
- The spontaneous polarization (in µC cm⁻²) of the PbFeO₃ and PbNbO₃ subcells, obtained via the Berry-phase method and saved in polarization.json.
The two numeric quantities should be computed following the procedure described under Workflow steps. The results will be compared to established reference values using tolerances that account for the rescoping of the calculation from WIEN2k to the open-source ELK code; a correct reproduction yields values that agree within these tolerances.

## Assets

- ELK FLAPW code: http://elk.sourceforge.net

## Workflow steps

### Step 1: Construct PFN supercell
- Role: process
- Action: Build a periodic supercell of PbFe0.5Nb0.5O3 consisting of alternating [001] layers of PbFeO3 and PbNbO3 in a pseudocubic perovskite structure. Use an initial lattice parameter near 4.0 Å and ideal atomic positions. Save the starting structure.
- Evidence: `/app/outputs/initial_structure.txt`

### Step 2: Volume relaxation (energy vs. volume)
- Role: process
- Action: Compute total energy for a series of cell volumes around the expected equilibrium. Fit an equation of state to determine the equilibrium lattice parameter a. Record the energy-volume data.
- Evidence: `/app/outputs/energy_volume.csv`

### Step 3: Atomic coordinate relaxation
- Role: process
- Action: At the equilibrium lattice parameter, relax all atomic positions in the supercell until forces converge (e.g., below 0.01 eV/Å).
- Evidence: `/app/outputs/relaxed_structure.txt`

### Step 4: Output optimized structure
- Role: scored (load-bearing)
- Action: From the relaxed calculation, extract the equilibrium lattice parameter a (Å) and the fractional coordinates of all atoms; write them to optimized_structure.json.
- Output file: `/app/outputs/optimized_structure.json`
- Format: json
- Contract: {"type": "object", "required": {"lattice_a": "float (Å)", "atoms": "array of {element: string, x: float, y: float, z: float}"}}
- Scoring: scored by hidden verifier

### Step 5: Construct paraelectric reference cell
- Role: process
- Action: Build a cubic paraelectric PFN supercell with ideal perovskite positions at the same optimized lattice parameter a; save as a separate structure file.
- Evidence: `/app/outputs/paraelectric_structure.txt`

### Step 6: Electronic structure calculations
- Role: process
- Action: Perform self-consistent DFT calculations (GGA) for both paraelectric and ferroelectric structures. Compute and save the density of states (total and projected), band structure, and electron density distribution.
- Evidence: `/app/outputs/dos_bands_density.tar.gz`

### Step 7: Spontaneous polarization via Berry phase
- Role: scored (load-bearing)
- Action: Using the Berry phase method implemented in ELK, compute the spontaneous polarization of the PbFeO3 and PbNbO3 subcells from the ferroelectric and paraelectric structures, and write the values to polarization.json.
- Output file: `/app/outputs/polarization.json`
- Format: json
- Contract: {"type": "object", "required": {"PbFeO3": "float (µC/cm²)", "PbNbO3": "float (µC/cm²)"}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optimized_structure.json`
- `/app/outputs/polarization.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimized_structure.json
- path: `/app/outputs/optimized_structure.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Equilibrium lattice constant and relaxed atomic fractional coordinates of the PFN supercell.
- schema:
  - `type`: object
  - `required`:
    - `lattice_a`: float (Å)
    - `atoms`: array of objects with keys element (string), x (float), y (float), z (float)

### polarization.json
- path: `/app/outputs/polarization.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Spontaneous polarization contributions of the PbFeO3 and PbNbO3 subcells computed via the Berry phase method.
- schema:
  - `type`: object
  - `required`:
    - `PbFeO3`: float (µC/cm²)
    - `PbNbO3`: float (µC/cm²)

Notes: The agent must install the ELK FLAPW code (http://elk.sourceforge.net) and any required numerical libraries at runtime. The workflow recreates the original WIEN2k procedure with the open-source rescoped tool; small numerical differences are expected. The electronic structure data (DOS, bands, density) are documented as process evidence but not independently scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimized_structure.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "lattice_a": "float (Å)",
          "atoms": "array of objects with keys element (string), x (float), y (float), z (float)"
        }
      },
      "description": "Equilibrium lattice constant and relaxed atomic fractional coordinates of the PFN supercell."
    },
    {
      "file": "polarization.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "PbFeO3": "float (µC/cm²)",
          "PbNbO3": "float (µC/cm²)"
        }
      },
      "description": "Spontaneous polarization contributions of the PbFeO3 and PbNbO3 subcells computed via the Berry phase method."
    }
  ],
  "notes": "The agent must install the ELK FLAPW code (http://elk.sourceforge.net) and any required numerical libraries at runtime. The workflow recreates the original WIEN2k procedure with the open-source rescoped tool; small numerical differences are expected. The electronic structure data (DOS, bands, density) are documented as process evidence but not independently scored."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that reads the two scored output files: optimized_structure.json and polarization.json.
- For optimized_structure.json, the verifier compares the reported lattice constant a and the set of fractional atomic coordinates against hidden reference values. The comparison allows a small tolerance for the lattice constant and tight positional tolerances for the coordinates.
- For polarization.json, the verifier compares the reported PbFeO₃ and PbNbO₃ polarization values to hidden reference values, again with an allowed tolerance (on the order of a few µC cm⁻²).
Each scored artifact is worth a portion of the total score, with the final reward in the range [0, 1] reflecting how closely your computed numbers match the hidden references. The intermediate evidence files (initial structure, energy-volume data, relaxed structure, paraelectric structure, DOS/bands/density archive) must be produced to demonstrate that the computation was carried out, but they do not directly contribute to the score. A reward of 1.0 indicates that both artifacts lie within the required tolerances.
