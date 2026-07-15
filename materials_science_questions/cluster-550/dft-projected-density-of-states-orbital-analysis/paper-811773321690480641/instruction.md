# Valence ordering from V-3d projected density of states integration

## Problem background
Rhombohedral AlV2O4 undergoes a charge disproportionation transition that creates three inequivalent vanadium sites (labelled V1, V2, V3) in its primitive cell. One V2 and six V3 ions form a 'heptamer' cluster, while V1 remains isolated. The valence states of these sites were debated—different assignments imply different charge-ordering patterns along the c-axis. Resolving the relative valence hierarchy is necessary to understand the material’s electronic properties. This task uses first-principles density functional theory to determine the valence ordering among V1, V2, and V3 and the resulting c-axis charge sequence.

## Approach
The workflow uses plane-wave DFT with a generalized-gradient approximation (GGA) functional. Starting from the experimental rhombohedral crystal structure, the atomic positions and cell parameters are first optimized. From the relaxed geometry, V–V bond lengths are analysed to identify the heptamer motif: the isolated V1, the heptamer centre V2, and the six V3 vertices. Spin-polarised calculations are then performed for several candidate magnetic orderings to locate the lowest-energy magnetic ground state. For that magnetic state, the V-3d partial density of states (PDOS) is computed using a Mulliken-like projection. The V-3d PDOS of each inequivalent V site is integrated in two distinct energy windows: a bonding-dominated window (PART I, –10 to –4 eV relative to the Fermi level) and a nonbonding near-Fermi window (PART II, –2.5 to 0 eV). An empirical rule—higher valence corresponds to larger PART I intensity and smaller PART II intensity—is applied to the integrated intensities to deduce the relative valence ordering of V1, V2, and V3. Finally, the crystallographic positions of the V layers along the c-axis are combined with the valence ordering to produce the layer-by-layer charge sequence.

## Reproduction target
The goal is to produce three scored artifacts from a DFT workflow: (1) a JSON file identifying the heptamer grouping (isolated site, centre, and vertex types); (2) a CSV file giving for each vanadium site the integrated V-3d PDOS intensities in PART I and PART II; and (3) a JSON file reporting the deduced relative valence ordering (lowest, highest, intermediate) among V1, V2, V3 and the c-axis layer sequence. The results must be derived from a self-consistent DFT calculation on the real crystal structure; using reported numbers without computation is not sufficient.

## Assets

- Rhombohedral AlV2O4 crystal structure from Horibe et al. (2006): 10.1103/PhysRevLett.96.086406
- Pseudopotentials for Al, V, O (SSSP efficiency library or similar): https://www.materialscloud.org/discover/sssp/table/efficiency
- Open-source plane-wave DFT code (e.g., Quantum ESPRESSO, GPAW): quantum-espresso

## Workflow steps

### Step 1: Prepare input structure
- Role: process
- Action: Build the primitive cell of rhombohedral AlV2O4 (Al4V8O16) using the experimental lattice parameters a=b=c=10.175 Å, α=32.83° and fractional coordinates from the Horibe et al. (2006) structure. Write the initial structure file.
- Evidence: `/app/outputs/input_structure.cif`

### Step 2: Geometry optimization
- Role: process
- Action: Perform DFT geometry optimization using a GGA functional to relax atomic positions and lattice parameters. Save the optimized structure.
- Evidence: `/app/outputs/optimized_structure.cif`

### Step 3: Heptamer motif identification
- Role: scored
- Action: Analyze the V-V bond lengths in the optimized structure. Identify the isolated V1 site and the heptamer composed of one V2 center and six V3 vertices. Write the assignment to a JSON file.
- Output file: `/app/outputs/step_02_heptamer.json`
- Format: json
- Contract: {"isolated_site": "V1", "heptamer_center": "V2", "heptamer_vertices": ["V3", "V3", "V3", "V3", "V3", "V3"]}
- Scoring: scored by hidden verifier

### Step 4: Magnetic ground state search
- Role: process
- Action: Run spin-polarized DFT calculations for four magnetic configurations (M1-M4) on the optimized structure. Record total energies and select the lowest-energy magnetic state (expected to be M1 with V1 ≈ -2.48, V2 ≈ -1.76, V3 ≈ 0.04 μB). Save the energies and magnetic moments.
- Evidence: `/app/outputs/magnetic_energies.csv`

### Step 5: Electronic structure and PDOS calculation
- Role: process
- Action: For the selected magnetic ground state, compute the spin-polarized band structure and V-3d partial density of states using a Mulliken-like population analysis. Save the PDOS data for V1, V2, and V3.
- Evidence: `/app/outputs/pdos_files.tar.gz`

### Step 6: Integrate V-3d PDOS intensities
- Role: scored (load-bearing)
- Action: Integrate the V-3d PDOS for each inequivalent V site in two energy windows: PART I [-10, -4] eV and PART II [-2.5, 0] eV (Fermi level at 0). Write a CSV with columns V_site, PART_I, PART_II.
- Output file: `/app/outputs/step_03_integrated_intensities.csv`
- Format: csv
- Contract: CSV with columns V_site (string), PART_I (float), PART_II (float). Three rows for V1, V2, V3.
- Scoring: scored by hidden verifier

### Step 7: Valence ordering and c-axis sequence
- Role: scored
- Action: Apply the empirical rule that higher valence corresponds to larger PART_I intensity and smaller PART_II intensity to the integrated intensities. Determine the relative valence ordering (lowest, highest, intermediate) for the three V sites. Derive the c-axis layer sequence from site positions. Write the result as JSON.
- Output file: `/app/outputs/step_04_valence_ordering.json`
- Format: json
- Contract: {"ordering": {"V1": "lowest", "V2": "highest", "V3": "intermediate"}, "c_axis_sequence": ["V1", "V3", "V2", "V3", "V1"]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_heptamer.json`
- `/app/outputs/step_03_integrated_intensities.csv`
- `/app/outputs/step_04_valence_ordering.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_heptamer.json
- path: `/app/outputs/step_02_heptamer.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Identification of the heptamer motif: the isolated site V1, the center V2, and the six vertex V3 ions.
- schema:
  - `type`: object
  - `required`:
    - `isolated_site`: string
    - `heptamer_center`: string
    - `heptamer_vertices`: array of strings

### step_03_integrated_intensities.csv
- path: `/app/outputs/step_03_integrated_intensities.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Integrated V-3d PDOS intensities for each V site in energy windows -10 to -4 eV and -2.5 to 0 eV.
- schema:
  - `type`: table
  - `required_columns`: `V_site`, `PART_I`, `PART_II`
  - `units`:
    - `PART_I`: integrated PDOS (electrons)
    - `PART_II`: integrated PDOS (electrons)

### step_04_valence_ordering.json
- path: `/app/outputs/step_04_valence_ordering.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Relative valence ordering among V1, V2, V3 and the layer-by-layer charge ordering sequence along the c-axis.
- schema:
  - `type`: object
  - `required`:
    - `ordering`: object with keys V1, V2, V3 each mapping to one of "lowest", "highest", "intermediate"
    - `c_axis_sequence`: array of strings

Notes: The checker verifies the heptamer assignment and valence ordering by structural rules; the integrated PDOS intensities are compared to the reference values from the paper (Table 3) with an appropriate tolerance. The relative ordering is independently re-derived from the intensities.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_heptamer.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "isolated_site": "string",
          "heptamer_center": "string",
          "heptamer_vertices": "array of strings"
        }
      },
      "description": "Identification of the heptamer motif: the isolated site V1, the center V2, and the six vertex V3 ions."
    },
    {
      "file": "step_03_integrated_intensities.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "V_site",
          "PART_I",
          "PART_II"
        ],
        "units": {
          "PART_I": "integrated PDOS (electrons)",
          "PART_II": "integrated PDOS (electrons)"
        }
      },
      "description": "Integrated V-3d PDOS intensities for each V site in energy windows -10 to -4 eV and -2.5 to 0 eV."
    },
    {
      "file": "step_04_valence_ordering.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "ordering": "object with keys V1, V2, V3 each mapping to one of \"lowest\", \"highest\", \"intermediate\"",
          "c_axis_sequence": "array of strings"
        }
      },
      "description": "Relative valence ordering among V1, V2, V3 and the layer-by-layer charge ordering sequence along the c-axis."
    }
  ],
  "notes": "The checker verifies the heptamer assignment and valence ordering by structural rules; the integrated PDOS intensities are compared to the reference values from the paper (Table 3) with an appropriate tolerance. The relative ordering is independently re-derived from the intensities."
}
```

## How you are scored
A hidden verifier inspects each output file independently. The heptamer identification is checked for structural correctness of the isolated site, centre, and vertices. The integrated intensities CSV is validated against reference values and then used to re-derive the valence ordering—the verifier confirms that the ordering derived from your intensities matches the ordering you report. The final valence ordering and c-axis sequence JSON is compared to the expected hierarchy and sequence. The reward is a weighted average across the three stages, with the integrated intensities carrying the most weight.
