# DFT study of bulk and (001) surface of TiC

## Problem background
TiC is a transition-metal carbide valued for its extreme hardness, high melting point, and good electrical conductivity. It serves as a hard coating, a grain refiner, and a reinforcement in composites. The compound exhibits a mixture of metallic, ionic, and covalent bonding, but the relative contributions of each bonding type and their manifestation on the (001) surface are not fully clear. First-principles density-functional theory (DFT) can probe these properties by calculating bulk lattice parameters, electronic density of states, and the structural relaxation that occurs when a surface is created. Understanding the depth to which surface relaxation perturbs the atomic layers is important for correctly modelling surface phenomena.

## Approach
The work employs plane-wave pseudopotential DFT with the GGA-PBE exchange-correlation functional. First, the bulk rocksalt TiC unit cell is fully relaxed to obtain the equilibrium lattice constant. A static self-consistent field calculation followed by a non-self-consistent calculation on a denser k-point grid yields the total density of states as a function of energy. Second, symmetric (001) slabs are constructed by cleaving the optimized bulk; these slabs contain an odd number of atomic layers and are terminated by the same species on both surfaces. A vacuum region perpendicular to the surface prevents interactions between periodic images. Geometry relaxations are performed for 5- and 7-layer slabs, keeping the in-plane lattice parameters fixed to the bulk value and allowing all atomic coordinates to relax. The surface energy is computed from the total energies of the two slabs using the Boettger formula, and the convergence of surface energy with slab thickness is examined. The interlayer spacing changes between the top atomic layers are extracted from the relaxed 7-layer slab to assess the depth of surface relaxation. The electronic structure is examined through the total DOS and, qualitatively, through charge density distributions, but the quantitative reproduction target focuses on lattice constant, DOS at the Fermi level, surface energy, and interlayer relaxations.

## Reproduction target
Perform DFT calculations using an open-source plane-wave pseudopotential code (e.g., Quantum ESPRESSO) with the GGA-PBE functional and appropriate pseudopotentials for Ti and C. From these calculations, obtain and report the following quantities in the specified structured JSON file:

- The equilibrium lattice constant (in Å) of bulk rocksalt TiC.
- The total electronic density of states at the Fermi level (states/eV/atom) for the bulk.
- The surface energy (in J/m²) of a 7-layer symmetric TiC(001) slab, computed using the total energies of relaxed 5-layer and 7-layer slabs and the known surface area.
- The percentage changes in interlayer spacing relative to the bulk value for the top three layer pairs (denoted Δ12, Δ23, Δ34) for the carbon and titanium atomic species separately, extracted from the relaxed atomic coordinates of the 7-layer slab.

## Assets

- Quantum ESPRESSO (pw.x): https://www.quantum-espresso.org/
- Pseudopotentials for Ti and C (PseudoDojo or SSSP): https://www.pseudo-dojo.org/

## Workflow steps

### Step 1: Bulk TiC geometry optimization
- Role: scored
- Action: Optimize the lattice constant of bulk rocksalt TiC using plane-wave DFT with the GGA-PBE exchange-correlation functional and an open-source pseudopotential DFT code (e.g., Quantum ESPRESSO). Save the relaxed total energy, lattice vectors, and atomic positions as a plain-text output file.
- Output file: `/app/outputs/bulk_relax.out`
- Format: txt
- Contract: Quantum ESPRESSO pw.x output file (text) containing the final lattice parameter (alat) or cell vectors from which the cubic lattice constant can be computed, and the final total energy.
- Scoring: scored by hidden verifier

### Step 2: Bulk total density of states calculation
- Role: scored
- Action: Using the optimized bulk geometry, perform a static SCF calculation followed by a non-self-consistent (NSCF) calculation on a dense k-point grid to compute the total density of states. Extract the DOS data on a fine energy grid spanning approximately -20 to 20 eV relative to the Fermi energy and write it as a two-column text file (energy in eV, total DOS in states/eV/atom).
- Output file: `/app/outputs/bulk_dos.dat`
- Format: txt
- Contract: Whitespace-separated two-column text file with no header. Column 1: energy (eV) relative to the Fermi energy. Column 2: total DOS in units of states/eV/atom.
- Scoring: scored by hidden verifier

### Step 3: Construct TiC(001) slab models
- Role: process
- Action: Using the optimized bulk lattice constant, construct symmetric TiC(001) slab supercells with 5 and 7 atomic layers terminated by the same atomic species on both sides, and include a vacuum region of at least 20 Å perpendicular to the surface. Prepare input files for geometry relaxation using the same DFT functional and code.
- Evidence: `/app/outputs/slab_inputs_constructed.txt`

### Step 4: Relax 5-layer TiC(001) slab
- Role: process
- Action: Perform a geometry relaxation of the 5-layer slab, allowing all atomic coordinates to relax while keeping the in-plane lattice parameters fixed to the bulk value. Save the final total energy in a text file.
- Evidence: `/app/outputs/slab5_relax.out`

### Step 5: Relax 7-layer TiC(001) slab and extract surface properties
- Role: scored (load-bearing)
- Action: Perform a geometry relaxation of the 7-layer slab under the same conditions as the 5-layer slab. Save the final total energy and the relaxed atomic positions.
- Output file: `/app/outputs/slab7_relax.out`
- Format: txt
- Contract: Quantum ESPRESSO pw.x output file (text) containing the final total energy and the final atomic positions (in fractional or Cartesian coordinates) for the 7-layer slab.
- Scoring: scored by hidden verifier

### Step 6: Compile final structured results
- Role: scored
- Action: Compute the following quantities using the raw DFT outputs: (1) the bulk lattice constant from step1, (2) the total DOS at the Fermi level from step2, (3) the surface energy for the 7-layer slab using the total energies of the relaxed 5-layer (step4 evidence) and 7-layer (step5) slabs and the known surface area, (4) the interlayer relaxation percentages Δ12, Δ23, Δ34 for C and Ti layer pairs from the relaxed atomic positions of step5. Assemble these quantities into a single JSON file following the specified schema.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: 'bulk_lattice_constant' (float, Å), 'surface_energy_7layer' (float, J/m²), 'total_DOS_at_Fermi' (float, states/eV/atom), 'interlayer_spacings' (array of objects, each with 'species' (string, 'C' or 'Ti'), 'layer_pair' (string, '12','23','34'), 'delta_percent' (float)).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bulk_relax.out`
- `/app/outputs/bulk_dos.dat`
- `/app/outputs/slab7_relax.out`
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bulk_relax.out
- path: `/app/outputs/bulk_relax.out`
- format: txt
- purpose: scored
- target_policy: metric_recompute
- description: DFT output from bulk geometry optimization; checker extracts equilibrium lattice constant and compares to hidden gold.
- schema:
  - `type`: text
  - `description`: Quantum ESPRESSO pw.x output text. Contains the final lattice parameter (alat) or cell vectors (in Bohr or Angstrom) and the final total energy. The checker extracts the equilibrium lattice constant.

### bulk_dos.dat
- path: `/app/outputs/bulk_dos.dat`
- format: txt
- purpose: scored
- target_policy: metric_recompute
- description: Total density of states for bulk TiC; checker interpolates at the Fermi level and compares to hidden gold.
- schema:
  - `type`: text
  - `description`: Two-column whitespace-separated text file, no header. Column 1: energy (eV) relative to Fermi energy. Column 2: total DOS in states/eV/atom. Checker interpolates to obtain DOS at E=0 eV.

### slab7_relax.out
- path: `/app/outputs/slab7_relax.out`
- format: txt
- purpose: scored
- target_policy: metric_recompute
- description: Relaxed 7-layer slab output; checker computes surface energy and interlayer relaxations and compares to hidden gold.
- schema:
  - `type`: text
  - `description`: Quantum ESPRESSO pw.x output from 7-layer slab relaxation. Contains final total energy and final atomic positions (fractional or Cartesian coordinates). Checker recomputes surface energy and interlayer spacing changes.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Structured summary of reproduced results; checker verifies consistency with recomputed quantities from raw DFT outputs.
- schema:
  - `type`: object
  - `required`:
    - `bulk_lattice_constant`: float (Angstrom)
    - `surface_energy_7layer`: float (J/m^2)
    - `total_DOS_at_Fermi`: float (states/eV/atom)
    - `interlayer_spacings`: array of objects, each with 'species' (string 'C' or 'Ti'), 'layer_pair' (string '12','23','34'), 'delta_percent' (float)

Notes: The checker recomputes lattice constant, DOS at Fermi, surface energy, and interlayer relaxations from the raw artifacts, then verifies that the agent-reported values in results.json match within a tight tolerance. All hidden gold values are derived from the paper's reported numbers.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bulk_relax.out",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "text",
        "description": "Quantum ESPRESSO pw.x output text. Contains the final lattice parameter (alat) or cell vectors (in Bohr or Angstrom) and the final total energy. The checker extracts the equilibrium lattice constant."
      },
      "description": "DFT output from bulk geometry optimization; checker extracts equilibrium lattice constant and compares to hidden gold."
    },
    {
      "file": "bulk_dos.dat",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "text",
        "description": "Two-column whitespace-separated text file, no header. Column 1: energy (eV) relative to Fermi energy. Column 2: total DOS in states/eV/atom. Checker interpolates to obtain DOS at E=0 eV."
      },
      "description": "Total density of states for bulk TiC; checker interpolates at the Fermi level and compares to hidden gold."
    },
    {
      "file": "slab7_relax.out",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "text",
        "description": "Quantum ESPRESSO pw.x output from 7-layer slab relaxation. Contains final total energy and final atomic positions (fractional or Cartesian coordinates). Checker recomputes surface energy and interlayer spacing changes."
      },
      "description": "Relaxed 7-layer slab output; checker computes surface energy and interlayer relaxations and compares to hidden gold."
    },
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "bulk_lattice_constant": "float (Angstrom)",
          "surface_energy_7layer": "float (J/m^2)",
          "total_DOS_at_Fermi": "float (states/eV/atom)",
          "interlayer_spacings": "array of objects, each with 'species' (string 'C' or 'Ti'), 'layer_pair' (string '12','23','34'), 'delta_percent' (float)"
        }
      },
      "description": "Structured summary of reproduced results; checker verifies consistency with recomputed quantities from raw DFT outputs."
    }
  ],
  "notes": "The checker recomputes lattice constant, DOS at Fermi, surface energy, and interlayer relaxations from the raw artifacts, then verifies that the agent-reported values in results.json match within a tight tolerance. All hidden gold values are derived from the paper's reported numbers."
}
```

## How you are scored
A hidden verifier inspects your output artifacts after the run. For the raw DFT outputs (`bulk_relax.out`, `bulk_dos.dat`, `slab7_relax.out`) the verifier recomputes the target quantities (lattice constant, DOS at Fermi, surface energy, and interlayer spacing changes) from your data and compares them to reference values with pre-defined tolerances. It then checks that the numerical values you report in `results.json` are consistent with these recomputed quantities. Each scored quantity contributes a share to the final reward, with the interlayer spacings carrying the largest weight. Simply reporting literature numbers without performing the calculations will not yield a passing score; the artifacts and the derived results must stem from the DFT workflow described in the steps.
