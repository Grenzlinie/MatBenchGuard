# Ground State Spin Multiplicities and Stability of YSi_n (n=1–6) Clusters from DFT

## Problem background
Silicon clusters doped with transition metals exhibit size-dependent structural, electronic, and magnetic properties distinct from the bulk. Determining the ground-state spin multiplicities and stability trends of small YSi_n clusters (n=1–6) is important for understanding their abundance in mass spectra and for designing metal-silicon composite materials. Prior work on the analogous ScSi_n clusters serves as a reference; this task extends the investigation to yttrium-doped silicon clusters to explore the influence of the metal center.

## Approach
The clusters are studied using hybrid density functional theory (DFT) at the B3LYP level. For each YSi_n cluster (n=1–6), geometry optimizations are performed for both spin-doublet and spin-quartet multiplicities, sampling multiple electronic configurations by rearranging orbital occupations near the Fermi level to locate the lowest-energy state of each multiplicity. Harmonic vibrational frequency calculations confirm that the optimized structures are true minima. From the lowest-energy total energies, the spin-state energy differences are computed, and the ground-state spin is assigned. Atomic energies of Y and Si computed at the same level of theory are used to calculate the binding energy per atom and the fragmentation energies for two dissociation channels: YSi_n → Y + Si_n and YSi_n → Si + YSi_{n-1}. All calculations are performed with an all-electron double-zeta quality basis set (or an equivalent modern basis such as def2-SVP) using an open-source quantum chemistry program. The initial cluster geometries are constructed from known structures of pure silicon clusters and analogous ScSi_n clusters.

## Reproduction target
Perform DFT geometry optimizations and vibrational frequency checks for YSi_n clusters (n=1–6) in both doublet and quartet spin states, sampling multiple electronic configurations. From the optimized total energies, identify the ground-state spin multiplicity (doublet or quartet) for each size, and compute the energy difference ΔE = E_doublet – E_quartet (in eV). Compute the binding energy per atom (eV/atom) for the most stable isomer of each size, and the fragmentation energies for the two channels Y + Si_n and Si + YSi_{n-1}. Report all results in the JSON files specified in the workflow steps and output contract.

## Assets

- ORCA quantum chemistry program (open-source substitute for Gaussian 98): https://orcaforum.kofo.mpg.de/
- Basis set definitions for Si and Y (all-electron DZVP equivalent, def2-SVP, and Stuttgart/Dresden ECP): https://www.basissetexchange.org/
- Reference geometries of pure Si_n, ScSi_n, and Si_{n+1} clusters from literature

## Workflow steps

### Step 1: Prepare initial cluster geometries
- Role: process
- Action: Generate initial Cartesian coordinates for YSi_n clusters (n=1–6) by substituting a Y atom into known geometries of Si_{n+1}, Si_n, or corresponding ScSi_n clusters, or by attaching Y to a Si_n surface. Refer to published structures for small silicon and scandium-silicon clusters.
- Evidence: `/app/outputs/initial_structures.log`

### Step 2: Geometry optimization and vibrational analysis
- Role: process
- Action: For each YSi_n cluster (n=1–6), perform geometry optimizations using B3LYP with an all-electron double-zeta quality basis (e.g., def2-SVP or DZVP) in ORCA. Optimize structures in both spin-doublet and spin-quartet multiplicities, and for each multiplicity sample several electronic configurations by altering orbital occupations around the Fermi level. Run harmonic frequency calculations to confirm obtained structures are minima (no imaginary frequencies). Save total energies and frequency outputs for all successful optimizations.
- Evidence: `/app/outputs/optimization_energies.txt`

### Step 3: Spin state energies
- Role: scored (load-bearing)
- Action: From the optimized total energies, identify the lowest-energy state for each cluster size and spin multiplicity. Compute the energy difference ΔE = E_doublet - E_quartet in eV for each n. Output a JSON array with one entry per cluster containing the doublet and quartet energies, ΔE, the assigned ground-state spin, and a flag indicating all harmonic frequencies are positive.
- Output file: `/app/outputs/spin_energies.json`
- Format: json
- Contract: Array of objects; each object with keys: cluster (string, e.g. 'YSi1'), doublet_energy (float, Hartree), quartet_energy (float, Hartree), delta_E_eV (float, doublet - quartet in eV), ground_state_spin (string, 'doublet' or 'quartet'), all_freq_positive (bool).
- Scoring: scored by hidden verifier

### Step 4: Binding energies
- Role: scored
- Action: Using the total energies of the most stable isomer for each cluster size (lowest-energy state irrespective of multiplicity) and the atomic energies of Y and Si computed at the same level, calculate the binding energy per atom: Eb_per_atom(eV) = [E(Y) + n*E(Si) - E(YSi_n)] / (n+1). Output a JSON array with one entry per cluster size.
- Output file: `/app/outputs/binding_energies.json`
- Format: json
- Contract: Array of objects; each object with keys: cluster (string, e.g. 'YSi1'), binding_energy_per_atom (float, eV).
- Scoring: scored by hidden verifier

### Step 5: Fragmentation energies
- Role: scored
- Action: Compute two fragmentation channels: FE1 = E(YSi_n) - [E(Y) + E(Si_n)] and FE2 = E(YSi_n) - [E(Si) + E(YSi_{n-1})]. For FE1, use the total energy of the most stable neutral Si_n cluster optimized at the same level. For FE2, use the most stable YSi_{n-1} energies. Output a JSON array with FE1 and FE2 values (in eV) for n=1–6.
- Output file: `/app/outputs/fragmentation_energies.json`
- Format: json
- Contract: Array of objects; each object with keys: cluster (string, e.g. 'YSi1'), FE1_Y_Si_n (float, eV), FE2_Si_YSi_{n-1} (float, eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/spin_energies.json`
- `/app/outputs/binding_energies.json`
- `/app/outputs/fragmentation_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### spin_energies.json
- path: `/app/outputs/spin_energies.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Ground-state spin multiplicity per cluster size, with an indication that all vibrational frequencies are positive. The structural audit verifies the sign of the doublet-quartet energy difference and that all frequencies are positive.
- schema:
  - `type`: array
  - `items`:
    - `cluster`: string
    - `doublet_energy`: float (Hartree)
    - `quartet_energy`: float (Hartree)
    - `delta_E_eV`: float (eV)
    - `ground_state_spin`: string (doublet or quartet)
    - `all_freq_positive`: bool
  - `description`: One object per cluster size n=1 to 6.

### binding_energies.json
- path: `/app/outputs/binding_energies.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Size-dependent binding energy per atom. The structural audit checks for consistency with expected stability trends.
- schema:
  - `type`: array
  - `items`:
    - `cluster`: string
    - `binding_energy_per_atom`: float (eV)
  - `description`: One object per cluster size n=1 to 6.

### fragmentation_energies.json
- path: `/app/outputs/fragmentation_energies.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Fragmentation energies for two channels. The structural audit checks for consistency with expected stability trends.
- schema:
  - `type`: array
  - `items`:
    - `cluster`: string
    - `FE1_Y_Si_n`: float (eV)
    - `FE2_Si_YSi_{n-1}`: float (eV)
  - `description`: One object per cluster size n=1 to 6.

Notes: All outputs are arrays ordered by n=1 to 6. The absolute numerical values are not required to match the paper exactly; the structural audit checks relative ordering and peak locations. The agent must use the same DFT method (B3LYP) and a comparable all-electron basis set.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "spin_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "array",
        "items": {
          "cluster": "string",
          "doublet_energy": "float (Hartree)",
          "quartet_energy": "float (Hartree)",
          "delta_E_eV": "float (eV)",
          "ground_state_spin": "string (doublet or quartet)",
          "all_freq_positive": "bool"
        },
        "description": "One object per cluster size n=1 to 6."
      },
      "description": "Ground-state spin multiplicity per cluster size, with an indication that all vibrational frequencies are positive. The structural audit verifies the sign of the doublet-quartet energy difference and that all frequencies are positive."
    },
    {
      "file": "binding_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "array",
        "items": {
          "cluster": "string",
          "binding_energy_per_atom": "float (eV)"
        },
        "description": "One object per cluster size n=1 to 6."
      },
      "description": "Size-dependent binding energy per atom. The structural audit checks for consistency with expected stability trends."
    },
    {
      "file": "fragmentation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "array",
        "items": {
          "cluster": "string",
          "FE1_Y_Si_n": "float (eV)",
          "FE2_Si_YSi_{n-1}": "float (eV)"
        },
        "description": "One object per cluster size n=1 to 6."
      },
      "description": "Fragmentation energies for two channels. The structural audit checks for consistency with expected stability trends."
    }
  ],
  "notes": "All outputs are arrays ordered by n=1 to 6. The absolute numerical values are not required to match the paper exactly; the structural audit checks relative ordering and peak locations. The agent must use the same DFT method (B3LYP) and a comparable all-electron basis set."
}
```

## How you are scored
A hidden verifier will independently check each scored output file (spin_energies.json, binding_energies.json, fragmentation_energies.json). The checks will evaluate the correctness of the relative spin-state ordering, the size-dependent trends in binding and fragmentation energies (e.g., the presence of local maxima at certain sizes), and that all reported structures have no imaginary frequencies. The verifier does not simply compare your reported numbers to a set of target values; it may recompute derived quantities from your submitted data and assess internal consistency. Each scored artifact contributes to the final reward, which is a weighted combination of the individual stage scores. Simply copying values from the literature without performing the actual computations will not pass the structural and consistency checks.
