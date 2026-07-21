# Ferroelastic twin wall properties in CsPbI3 from first-principles calculation

## Problem background
Hybrid organic-inorganic halide perovskite solar cells have achieved high power conversion efficiencies, but the role of nanoscale structural defects such as domain walls in charge carrier separation and transport remains an active area of investigation. Recent experiments have identified 90° ferroelastic twin boundaries in methylammonium lead iodide (MAPI), a prominent perovskite absorber. These ferroelastic twins separate domains with different spontaneous strain states and are distinct from grain boundaries or ferroelectric domain walls. To understand their fundamental properties without the complexity of the dynamic organic cation, this work uses CsPbI₃ as a model system. The central questions are: what are the formation energies of such twin walls, how thick are they, and do they exhibit a spontaneous electrical polarization despite separating non-polar domains? Answering these questions can reveal whether ferroelastic domain walls could influence charge carrier behavior in perovskite photovoltaics.

## Approach
The approach employs first-principles density functional theory (DFT) with the PBEsol exchange-correlation functional. The material is modeled in its room-temperature tetragonal phase (space group I4/mcm), which is characterized by an antiphase octahedral tilt pattern. Two structurally distinct 90° ferroelastic twin boundaries — head-to-tail (HT) and head-to-head (HH) — are built as periodic supercells, each containing two mechanically compatible walls separated by bulk-like regions. The atomic positions are relaxed until the forces on all atoms fall below a convergence threshold. The formation energy of a single wall is obtained from the total energy difference between the supercell and the equivalent number of bulk unit cells, normalized by the wall area. To evaluate the polarization, Born effective charge tensors are first computed for the ideal cubic perovskite structure using density functional perturbation theory (DFPT). The layer-resolved polarization across the wall is then calculated by multiplying the ionic displacements (referenced to a high-symmetry configuration) by these charges. The wall thickness is extracted by fitting the profile of the octahedral tilt magnitude across the boundary to a hyperbolic tangent function. The final reported quantities are the wall formation energy, thickness, and the peak in-plane polarization for each wall type.

## Reproduction target
The task is to compute, using an open-source DFT code with the PBEsol functional, the wall formation energies (mJ/m²), the wall thicknesses (nm), and the peak in-plane polarization values (μC/cm²) for both the head-to-tail (HT) and head-to-head (HH) 90° ferroelastic twin boundaries in CsPbI₃. The six final quantities must be written to a JSON file at `/app/outputs/results.json` with the exact field names: `HT_formation_energy_mJ_m2`, `HH_formation_energy_mJ_m2`, `HT_thickness_nm`, `HH_thickness_nm`, `HT_peak_polarization_muC_cm2`, `HH_peak_polarization_muC_cm2`. The submitted file is the sole scored artifact; all required intermediate computations (bulk energy, Born charges, supercell relaxations) are process steps whose evidence is audited but not directly weighted in the final score.

## Supercell construction and formulas

### Crystal structures
- **Tetragonal I4/mcm phase**: lattice parameters a = 8.86 Å, c = 12.66 Å (space group 140). The unit cell contains 20 atoms (4 formula units). Use public crystallographic data or database entries for the atomic positions.
- **Cubic Pm‑3m phase** (for Born effective charges): lattice constant a_cub = 6.30 Å. The cubic perovskite structure has Cs at the corner (0,0,0), Pb at the body centre (½,½,½), and I at the face centres (½,½,0), (½,0,½), (0,½,½).

### Wall orientations and supercells
We adopt a Cartesian coordinate system aligned with the tetragonal axes: **x̂** ∥ [100], **ŷ** ∥ [010], **ẑ** ∥ [001]. Vectors are given in units of the tetragonal lattice vectors: **a** = (a,0,0), **b** = (0,a,0), **c** = (0,0,c).

| Wall | Perpendicular direction **Ŝ** | In-plane direction **r̂** | Out-of-plane direction |
|------|-------------------------------|--------------------------|-------------------------|
| HT   | [1, 1, 0]                     | [1, –1, 0]              | [0, 0, 1]              |
| HH   | [1, –1, 0]                    | [1, 1, 0]               | [0, 0, 1]              |

**HT supercell** — contain two HT walls (one at the cell centre, one at the cell boundary). Build the supercell from the following three vectors expressed as fractional coordinates with respect to the tetragonal conventional cell:

- **a₁** = [1, 1, 0]  (along **ŝ**, perpendicular to the wall plane)
- **a₂** = [–1, 1, 0] (along **r̂**, parallel to the wall)
- **a₃** = [0, 0, 5]   (along the out-of-plane direction)

The transformation matrix has determinant 10, so the supercell contains exactly 10 conventional cells, i.e. 200 atoms. The two HT walls are positioned such that one wall lies at the centre of **a₁** and the second is formed by the periodic image at the boundary. For the atomic arrangement, place the domain with octahedral tilt axis **ϕ** ∥ [001] on one side of the wall and the domain with **ϕ** ∥ [010] on the other side.

**HH supercell** — analogous, but with the wall orientation rotated:

- **a₁** = [1, –1, 0]  (along **ŝ**)
- **a₂** = [1, 1, 0]   (along **r̂**)
- **a₃** = [0, 0, 5]

Again determinant = 10 (200 atoms). For the HH wall the two domains have tilt axes **ϕ** ∥ [001] and **ϕ** ∥ [100].

### Wall area for formation energy
The wall area is the area of the plane that is orthogonal to **ŝ** and spanned by **r̂** and the out-of-plane direction. Using the supercell vectors defined above:

- Cartesian length of **a₂** : `|a₂| = √[ (–a)² + a² ] = √2 a`
- Cartesian length of **a₃** : `|a₃| = 5 c`

Because **a₂** and **a₃** are orthogonal, the geometric wall area is

`A_wall = |a₂| × |a₃| = √2 a × 5 c`.

This area is the same for both HT and HH supercells.

### Formation energy formula
Let *E_supercell* be the total DFT energy of the relaxed 200‑atom supercell and *E_bulk* the total energy of a relaxed 20‑atom I4/mcm conventional cell.

`E_form = (E_supercell – 10 E_bulk) / (2 A_wall)`

The factor 2 accounts for the two walls contained in the supercell.

### Polarisation calculation
- Use the Born effective charge tensors computed in the cubic Pm‑3m phase.
- For the relaxed supercell, define a reference high‑symmetry structure by mapping the ideal cubic positions into the supercell.
- Compute ionic displacements **u** with respect to that reference.
- Divide the supercell into layers perpendicular to **ŝ**. The layer thickness is `d = |a₁| / N_layers`; the layer volume is `V_layer = A_wall × d`.
- The layer polarisation **P** is `P_layer = (1/V_layer) Σ_{atoms in layer} Z* · u`, where `Z*` are the Born charge tensors.
- Extract the **r̂** component of **P**. Its peak value along the wall normal is the reported peak in‑plane polarisation.

## Assets

- Open-source DFT code with PBEsol support (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/
- Pseudopotentials for Cs, Pb, I (compatible with PBEsol; e.g., from SSSP efficiency 1.1 or PSlibrary): Distributed with DFT codes or available from online libraries
- Crystal structure of tetragonal I4/mcm CsPbI3 (a=8.86 Å, c=12.66 Å, space group 140): Literature or ICSD; can be generated from published lattice parameters and atomic positions
- Ideal cubic perovskite Pm-3m structure of CsPbI3: Can be constructed from standard cubic lattice with Cs at corner, Pb at body center, I at face centers

## Workflow steps

### Step 1: Bulk I4/mcm reference energy
- Role: process
- Action: Construct the 20-atom conventional cell of CsPbI3 in the I4/mcm phase using the public crystallographic data. Perform a self-consistent DFT calculation with the PBEsol functional to obtain the total energy of the bulk reference cell.
- Evidence: `/app/outputs/bulk_energy.txt`

### Step 2: Born effective charges on cubic Pm-3m
- Role: process
- Action: Construct the ideal cubic Pm-3m unit cell of CsPbI3 using a_cub = 6.30 Å. Compute Born effective charge tensors for all atoms using density functional perturbation theory (DFPT) with the PBEsol functional.
- Evidence: `/app/outputs/born_charges.json`

### Step 3: Relax HT twin supercell
- Role: process
- Action: Following the supercell construction described in “Supercell construction and formulas”, build the 200-atom HT supercell containing two mechanically compatible head-to-tail 90° ferroelastic twin boundaries. Relax the atomic positions using DFT with PBEsol until forces are below a suitable convergence threshold.
- Evidence: `/app/outputs/HT_relaxed.xyz`

### Step 4: Relax HH twin supercell
- Role: process
- Action: Following the same construction principles, build the 200-atom HH supercell containing two mechanically compatible head-to-head 90° ferroelastic twin boundaries. Relax the atomic positions analogously to the HT case using DFT with PBEsol.
- Evidence: `/app/outputs/HH_relaxed.xyz`

### Step 5: Analyze wall properties and output results
- Role: scored (load-bearing)
- Action: From the relaxed HT and HH supercells, the bulk reference energy, and the Born effective charges, compute: (1) wall formation energies per unit area; (2) wall thickness via fitting the octahedral tilt magnitude profile across the wall; (3) layer‑resolved polarization using the effective charges and ionic displacements and extract the peak in‑plane polarization. Write the six quantities to a JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {
  "HT_formation_energy_mJ_m2": float,
  "HH_formation_energy_mJ_m2": float,
  "HT_thickness_nm": float,
  "HH_thickness_nm": float,
  "HT_peak_polarization_muC_cm2": float,
  "HH_peak_polarization_muC_cm2": float
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bulk_energy.txt` (process evidence)
- `/app/outputs/born_charges.json` (process evidence)
- `/app/outputs/HT_relaxed.xyz` (process evidence)
- `/app/outputs/HH_relaxed.xyz` (process evidence)
- `/app/outputs/results.json` (scored)

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed wall formation energies (mJ/m²), thickness (nm), and peak in‑plane polarization (μC/cm²) for the head‑to‑tail (HT) and head‑to‑head (HH) 90° ferroelastic twin boundaries. The checker compares each field against the paper's reported reference values with appropriate tolerances.
- schema:
  - `type`: object
  - `required`: `HT_formation_energy_mJ_m2`, `HH_formation_energy_mJ_m2`, `HT_thickness_nm`, `HH_thickness_nm`, `HT_peak_polarization_muC_cm2`, `HH_peak_polarization_muC_cm2`

### bulk_energy.txt
- path: `/app/outputs/bulk_energy.txt`
- format: text
- purpose: process_evidence

### born_charges.json
- path: `/app/outputs/born_charges.json`
- format: json
- purpose: process_evidence

### HT_relaxed.xyz
- path: `/app/outputs/HT_relaxed.xyz`
- format: text
- purpose: process_evidence

### HH_relaxed.xyz
- path: `/app/outputs/HH_relaxed.xyz`
- format: text
- purpose: process_evidence

Notes: The hidden checker compares each numeric field to the paper‑reported reference values with tolerances appropriate for a DFT re‑implementation using an open‑source code. No gold values are revealed in this contract.

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
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "HT_formation_energy_mJ_m2",
          "HH_formation_energy_mJ_m2",
          "HT_thickness_nm",
          "HH_thickness_nm",
          "HT_peak_polarization_muC_cm2",
          "HH_peak_polarization_muC_cm2"
        ]
      },
      "description": "Computed wall formation energies (mJ/m²), thickness (nm), and peak in‑plane polarization (μC/cm²) for the head‑to‑tail (HT) and head‑to‑head (HH) 90° ferroelastic twin boundaries. The checker compares each field against the paper's reported reference values with appropriate tolerances."
    },
    {
      "file": "bulk_energy.txt",
      "format": "text",
      "purpose": "process_evidence"
    },
    {
      "file": "born_charges.json",
      "format": "json",
      "purpose": "process_evidence"
    },
    {
      "file": "HT_relaxed.xyz",
      "format": "text",
      "purpose": "process_evidence"
    },
    {
      "file": "HH_relaxed.xyz",
      "format": "text",
      "purpose": "process_evidence"
    }
  ],
  "notes": "The hidden checker compares each numeric field to the paper‑reported reference values with tolerances appropriate for a DFT re‑implementation using an open‑source code. No gold values are revealed in this contract."
}
```

## How you are scored
Your submission is evaluated by a hidden automated verifier. It inspects the artifacts you leave under `/app/outputs`, compares each of the six numeric quantities in `results.json` against hidden reference values that reflect the paper's reported results, and checks that the required intermediate evidence files are present and internally consistent. The comparison accounts for the legitimate spread that arises from using a different DFT implementation, pseudopotential library, or numerical settings. The final reward is a weighted combination of the scores for each required output, on a continuous scale from 0 (no credit) to 1 (full credit). Simply writing the paper's published numbers into the output file without executing the workflow will not satisfy the intermediate evidence checks and will receive a low score.