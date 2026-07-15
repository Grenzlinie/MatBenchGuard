# C60 Stability Under Pressure via Tersoff Potential

## Problem background
Buckminsterfullerene (C60) is an exceptionally hard carbon molecule built from 60 carbon atoms arranged in a truncated icosahedron, with alternating single and double bonds. Its hollow cage can house dopant atoms, making it attractive for nanotechnology. To utilize its strength in molecular bearings or high‑pressure encapsulation, it is necessary to understand how the molecule responds to extreme compression and dilation. The present work investigates the stability of a single C60 molecule under external and internal pressure using classical interatomic potentials. In particular, the Tersoff potential – an empirical bond‑order potential for carbon – is used to predict equilibrium bond lengths, binding energy, bulk modulus, bond‑stretching force constant, and the critical pressures at which the cage breaks down. This task focuses on reproducing the key numerical predictions obtained with the Tersoff potential.

## Approach
The central tool is the Tersoff potential, which models the energy between a pair of carbon atoms as a sum of repulsive and attractive terms whose balance depends on the local bonding environment via a bond‑order function. The potential has a small set of numerical parameters; two parameter sets are considered: the original Tersoff parameters and a modified set introduced in the work.

The approach proceeds in several stages. First, initial Cartesian coordinates for the 60 C60 atoms are built from the known icosahedral symmetry, using nominal experimental single‑ and double‑bond lengths as a starting point. Geometry optimization with the modified Tersoff potential then relaxes these coordinates at zero pressure to yield equilibrium bond lengths (single b1 and double b2) and the binding energy per atom. Using the original Tersoff parameter set, the molecule is isotropically compressed and dilated by scaling all coordinates uniformly; at each scaled volume the energy is minimized, giving an E(V) curve from which the zero‑pressure bulk modulus is extracted by fitting to an appropriate equation of state. A separate scan of the single‑bond length around its equilibrium value, combined with a second‑derivative evaluation, yields the bond‑stretching force constant. Finally, the molecule is further compressed and dilated while allowing angular degrees of freedom to relax; the scaling factors at which the energy minimum disappears define the maximum hydrostatic external (compressive) and internal (dilational) pressures the cage can sustain. All steps require only the publicly available Tersoff functional form and the parameter sets supplied in these instructions; no external dataset is needed.

## Reproduction target
Your task is to compute the following quantities and write them to the specified output files:
(1) from the modified Tersoff potential, the equilibrium single‑bond length b1 (Å), double‑bond length b2 (Å), and binding energy per atom (eV/atom) at zero pressure;
(2) from the original Tersoff potential, the zero‑pressure bulk modulus (GPa) obtained by isotropic scaling and equation‑of‑state fitting;
(3) from the original Tersoff potential, the bond‑stretching force constant (mdyne/Å) derived from the second derivative of the energy with respect to the single‑bond length;
(4) from the original Tersoff potential, the critical external pressure (compression, GPa) and critical internal pressure (dilation, GPa) at which the C60 energy minimum disappears.
Each of these must be produced by executing the corresponding workflow steps described below; you may not simply report the expected values without performing the required computations.

## Assets

- Tersoff potential parameter sets (original and modified)
- Python with NumPy, SciPy: numpy scipy

## Workflow steps

### Step 1: Generate C60 initial coordinates
- Role: process
- Action: Construct Cartesian coordinates for the 60 carbon atoms of buckminsterfullerene using icosahedral symmetry and standard experimental bond lengths (single 1.45 Å, double 1.40 Å).
- Evidence: `/app/outputs/initial_c60.xyz`

### Step 2: Geometry optimization with modified Tersoff
- Role: scored
- Action: Using the modified Tersoff potential (A=1380.0 eV, B=349.49 eV, λ1=3.5679, λ2=2.2564, λ3=0) and the initial C60 coordinates, perform energy minimization to obtain the equilibrium single bond length, double bond length, and binding energy per atom at zero pressure.
- Output file: `/app/outputs/b1_b2_energy.json`
- Format: json
- Contract: {"b1": float (Å), "b2": float (Å), "binding_energy_per_atom": float (eV/atom)}
- Scoring: scored by hidden verifier

### Step 3: Bulk modulus from original Tersoff
- Role: scored (load-bearing)
- Action: Using the original Tersoff potential (A=1393.6 eV, B=346.7 eV, λ1=3.4879, λ2=2.2119, λ3=0) and the C60 initial structure, isotropically scale the molecule to obtain E(V) data, fit to an equation of state, and extract the zero‑pressure bulk modulus (in GPa).
- Output file: `/app/outputs/bulk_modulus.txt`
- Format: txt
- Contract: Single float (GPa)
- Scoring: scored by hidden verifier

### Step 4: Bond‑stretching force constant from original Tersoff
- Role: scored
- Action: Using the original Tersoff potential, scan the single bond length around equilibrium and evaluate the second derivative of the energy to obtain the bond‑stretching force constant in mdyne/Å.
- Output file: `/app/outputs/force_constant.txt`
- Format: txt
- Contract: Single float (mdyne/Å)
- Scoring: scored by hidden verifier

### Step 5: Critical pressures from original Tersoff
- Role: scored
- Action: Using the original Tersoff potential and the initial C60 structure, compress and dilate the molecule uniformly and at each scaled volume allow angular relaxation; identify the scaling factors where the energy minimum disappears and convert to external and internal critical pressures (GPa).
- Output file: `/app/outputs/critical_pressures.json`
- Format: json
- Contract: {"external_critical_pressure_GPa": float, "internal_critical_pressure_GPa": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/b1_b2_energy.json`
- `/app/outputs/bulk_modulus.txt`
- `/app/outputs/force_constant.txt`
- `/app/outputs/critical_pressures.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### b1_b2_energy.json
- path: `/app/outputs/b1_b2_energy.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Equilibrium bond lengths and binding energy per atom computed with the modified Tersoff potential.
- schema:
  - `type`: object
  - `required`:
    - `b1`: float (Å)
    - `b2`: float (Å)
    - `binding_energy_per_atom`: float (eV/atom)
  - `items`: object
  - `required_columns`:
  - `units`:
    - `b1`: Å
    - `b2`: Å
    - `binding_energy_per_atom`: eV/atom

### bulk_modulus.txt
- path: `/app/outputs/bulk_modulus.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Bulk modulus of C60 at zero pressure computed with the original Tersoff potential.
- schema:
  - `type`: text
  - `required`: object
  - `items`: object
  - `required_columns`:
  - `units`:
    - `value`: GPa

### force_constant.txt
- path: `/app/outputs/force_constant.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Bond-stretching force constant computed with the original Tersoff potential.
- schema:
  - `type`: text
  - `required`: object
  - `items`: object
  - `required_columns`:
  - `units`:
    - `value`: mdyne/Å

### critical_pressures.json
- path: `/app/outputs/critical_pressures.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Critical external and internal pressures for C60 stability from the original Tersoff potential.
- schema:
  - `type`: object
  - `required`:
    - `external_critical_pressure_GPa`: float
    - `internal_critical_pressure_GPa`: float
  - `items`: object
  - `required_columns`:
  - `units`:
    - `external_critical_pressure_GPa`: GPa
    - `internal_critical_pressure_GPa`: GPa

Notes: Only Tersoff-potential results are scored; Brenner potential and phonon analyses are excluded. The C60 initial coordinates are generated from known icosahedral geometry, not fetched as an external dataset.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "b1_b2_energy.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "b1": "float (Å)",
          "b2": "float (Å)",
          "binding_energy_per_atom": "float (eV/atom)"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "b1": "Å",
          "b2": "Å",
          "binding_energy_per_atom": "eV/atom"
        }
      },
      "description": "Equilibrium bond lengths and binding energy per atom computed with the modified Tersoff potential."
    },
    {
      "file": "bulk_modulus.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "required": {},
        "items": {},
        "required_columns": [],
        "units": {
          "value": "GPa"
        }
      },
      "description": "Bulk modulus of C60 at zero pressure computed with the original Tersoff potential."
    },
    {
      "file": "force_constant.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "required": {},
        "items": {},
        "required_columns": [],
        "units": {
          "value": "mdyne/Å"
        }
      },
      "description": "Bond-stretching force constant computed with the original Tersoff potential."
    },
    {
      "file": "critical_pressures.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "external_critical_pressure_GPa": "float",
          "internal_critical_pressure_GPa": "float"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "external_critical_pressure_GPa": "GPa",
          "internal_critical_pressure_GPa": "GPa"
        }
      },
      "description": "Critical external and internal pressures for C60 stability from the original Tersoff potential."
    }
  ],
  "notes": "Only Tersoff-potential results are scored; Brenner potential and phonon analyses are excluded. The C60 initial coordinates are generated from known icosahedral geometry, not fetched as an external dataset."
}
```

## How you are scored
A hidden verifier program independently reads your scored output files and compares each reported value to a hidden reference. The verifier combines the individual stage scores, weighted by the relative importance of each result, into a single final reward between 0 and 1 (higher is better). Reporting merely the expected numbers without actually performing the minimisations and scans will not suffice; you must compute each quantity following the specified procedure with the given potential and starting geometry.
