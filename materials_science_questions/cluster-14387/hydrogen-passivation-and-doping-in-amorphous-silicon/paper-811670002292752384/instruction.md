# Real-time tight-binding density of states and band gap for silicon nanocrystals

## Problem background
Silicon nanocrystals are nanometer‑sized structures that exhibit efficient visible photoluminescence. Understanding their electronic structure is crucial for interpreting optical properties and for designing nanostructured devices. A key question is how the density of electronic states and the band gap change with cluster size and with the chemical termination of the surface. Answering this question requires accurate large‑scale electronic‑structure calculations that can handle thousands of atoms.

## Approach
We use a time‑dependent tight‑binding method that does not require explicit diagonalisation of the Hamiltonian. An electron wavefunction is initialised as a localised orbital on each atom and propagated in real time according to the time‑dependent Schrödinger equation with a tight‑binding Hamiltonian. The local density of states (DOS) on each orbital is obtained by Fourier transforming the autocorrelation function of the time‑evolved wavefunction, and the total DOS is the sum over all orbitals in the cluster. The atomistic basis consists of five orbitals (s, px, py, pz, s*) on each silicon atom and a single 1s orbital on each hydrogen atom. The Si–Si tight‑binding matrix elements are taken from the standard sp³s* model of Vogl et al. (J. Phys. Chem. Solids 44, 365, 1983). The Si–H interaction is described by Hückel parameters: ⟨H₁s|H|H₁s⟩ = –13.6 eV, ⟨H₁s|H|Si₃s⟩ = –9.29 eV, and ⟨H₁s|H|Si₃pz⟩ = –4.76 eV (and analogous values for the other Si p orbitals). Spherical clusters are carved from the bulk diamond lattice (lattice constant 5.43 Å) and surface silicon atoms are passivated with hydrogen at a distance of 1.5 Å. To study the effect of surface termination, we compute the DOS for an 18 Å diameter cluster under three conditions: (i) fully hydrogen‑passivated, (ii) with unsaturated dangling bonds (no hydrogen), and (iii) with the dangling‑bond orbitals completely removed from the basis. The band gap of each hydrogen‑passivated cluster is defined as the energy difference between the highest valence‑band peak and the lowest conduction‑band peak in the total DOS.

## Reproduction target
Produce the total density of states (DOS) for an 18 Å Si nanocrystal under three different surface conditions: (1) hydrogen‑passivated, (2) with dangling bonds (no hydrogen), and (3) with the dangling‑bond orbitals removed. Then, using the same time‑dependent tight‑binding algorithm, compute the band gap for hydrogen‑passivated clusters of diameters 15, 18, 25, and 35 Å, and report how the gap varies with cluster size.

## Assets

- Si tight-binding parameters (sp3s* basis) from Vogl et al. 1983: 10.1016/0022-3697(83)90089-7

## Workflow steps

### Step 1: Generate cluster geometries
- Role: process
- Action: Generate spherical Si nanocrystals from bulk diamond lattice (a=5.43 Å) for diameters 15, 18, 25, 35 Å. Terminate surface with H at 1.5 Å. For the 18 Å cluster also prepare a dangling‑bond configuration (no H) and a truncated configuration (dangling orbitals removed from basis). Represent each Si with five orbitals (s, p_x, p_y, p_z, s*) and each H with one 1s orbital.
- Evidence: `/app/outputs/clusters_metadata.json`

### Step 2: Construct tight-binding Hamiltonians
- Role: process
- Action: Build the tight-binding Hamiltonian matrix for each cluster using the Vogl Si-Si parameters and the Hückel Si-H parameters: <H1s|H|H1s> = -13.6 eV, <H1s|H|Si3s> = -9.29 eV, <H1s|H|Si3pz> = -4.76 eV (and analogous for p_x, p_y).
- Evidence: `/app/outputs/hamiltonian_dim.json`

### Step 3: Time‑propagate and compute raw DOS
- Role: process
- Action: For every cluster, propagate orbital‑localized initial wavefunctions in real time under the tight‑binding Hamiltonian. Compute the total density of states by Fourier transforming the autocorrelation function and summing local DOS over all orbitals. Store raw DOS data (energy grid and total DOS) for all clusters.
- Evidence: `/app/outputs/raw_dos_arrays.npz`

### Step 4: Output DOS for 18 Å hydrogen‑covered cluster
- Role: scored
- Action: Extract energy and total DOS for the hydrogen‑terminated 18 Å cluster and write as a CSV.
- Output file: `/app/outputs/dos_18A_hcovered.csv`
- Format: csv
- Contract: columns: energy_eV (float), total_DOS (float)
- Scoring: scored by hidden verifier

### Step 5: Output DOS for 18 Å dangling‑bond cluster
- Role: scored
- Action: Extract energy and total DOS for the dangling‑bond 18 Å cluster and write as a CSV.
- Output file: `/app/outputs/dos_18A_dangling.csv`
- Format: csv
- Contract: columns: energy_eV (float), total_DOS (float)
- Scoring: scored by hidden verifier

### Step 6: Output DOS for 18 Å truncated cluster
- Role: scored
- Action: Extract energy and total DOS for the truncated 18 Å cluster (dangling orbitals removed) and write as a CSV.
- Output file: `/app/outputs/dos_18A_truncated.csv`
- Format: csv
- Contract: columns: energy_eV (float), total_DOS (float)
- Scoring: scored by hidden verifier

### Step 7: Output band gap vs. cluster diameter
- Role: scored (load-bearing)
- Action: From the DOS of H‑terminated clusters (15, 18, 25, 35 Å) identify the highest valence‑band peak and lowest conduction‑band peak; compute the band gap as their energy difference and save the table.
- Output file: `/app/outputs/bandgap_vs_diameter.csv`
- Format: csv
- Contract: columns: diameter_A (float), band_gap_eV (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dos_18A_hcovered.csv`
- `/app/outputs/dos_18A_dangling.csv`
- `/app/outputs/dos_18A_truncated.csv`
- `/app/outputs/bandgap_vs_diameter.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dos_18A_hcovered.csv
- path: `/app/outputs/dos_18A_hcovered.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Density of states of hydrogen‑saturated 18 Å Si cluster. The checker recomputes the band gap from this DOS and compares to a hidden reference.
- schema:
  - `type`: table
  - `required_columns`: `energy_eV`, `total_DOS`
  - `units`:
    - `energy_eV`: eV
    - `total_DOS`: arbitrary

### dos_18A_dangling.csv
- path: `/app/outputs/dos_18A_dangling.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: DOS for 18 Å Si cluster with dangling bonds. The checker verifies presence of a mid‑gap state (intensity >30% of VBM) obscuring the band gap.
- schema:
  - `type`: table
  - `required_columns`: `energy_eV`, `total_DOS`
  - `units`:
    - `energy_eV`: eV
    - `total_DOS`: arbitrary

### dos_18A_truncated.csv
- path: `/app/outputs/dos_18A_truncated.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: DOS for 18 Å Si cluster with dangling orbitals removed. Checker recomputes band gap and compares to reference.
- schema:
  - `type`: table
  - `required_columns`: `energy_eV`, `total_DOS`
  - `units`:
    - `energy_eV`: eV
    - `total_DOS`: arbitrary

### bandgap_vs_diameter.csv
- path: `/app/outputs/bandgap_vs_diameter.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Band gap vs. diameter for H‑passivated Si nanocrystals. Checker verifies monotonic decrease with diameter and values within tolerance of digitized paper reference.
- schema:
  - `type`: table
  - `required_columns`: `diameter_A`, `band_gap_eV`
  - `units`:
    - `diameter_A`: Å
    - `band_gap_eV`: eV

Notes: No surface relaxation included (negligible effect on band edges). The agent must re‑implement the time‑propagation algorithm from the described method; the hidden checker recomputes band gaps from the raw DOS to prevent self‑reporting.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dos_18A_hcovered.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_eV",
          "total_DOS"
        ],
        "units": {
          "energy_eV": "eV",
          "total_DOS": "arbitrary"
        }
      },
      "description": "Density of states of hydrogen‑saturated 18 Å Si cluster. The checker recomputes the band gap from this DOS and compares to a hidden reference."
    },
    {
      "file": "dos_18A_dangling.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_eV",
          "total_DOS"
        ],
        "units": {
          "energy_eV": "eV",
          "total_DOS": "arbitrary"
        }
      },
      "description": "DOS for 18 Å Si cluster with dangling bonds. The checker verifies presence of a mid‑gap state (intensity >30% of VBM) obscuring the band gap."
    },
    {
      "file": "dos_18A_truncated.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_eV",
          "total_DOS"
        ],
        "units": {
          "energy_eV": "eV",
          "total_DOS": "arbitrary"
        }
      },
      "description": "DOS for 18 Å Si cluster with dangling orbitals removed. Checker recomputes band gap and compares to reference."
    },
    {
      "file": "bandgap_vs_diameter.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "diameter_A",
          "band_gap_eV"
        ],
        "units": {
          "diameter_A": "Å",
          "band_gap_eV": "eV"
        }
      },
      "description": "Band gap vs. diameter for H‑passivated Si nanocrystals. Checker verifies monotonic decrease with diameter and values within tolerance of digitized paper reference."
    }
  ],
  "notes": "No surface relaxation included (negligible effect on band edges). The agent must re‑implement the time‑propagation algorithm from the described method; the hidden checker recomputes band gaps from the raw DOS to prevent self‑reporting."
}
```

## How you are scored
Each scored output file is independently evaluated by a hidden verifier. The verifier examines the DOS CSVs for the 18 Å cluster to check for the expected qualitative differences between the surface terminations (for example, the presence or absence of a mid‑gap state in the dangling‑bond case). It also recomputes band gaps from your supplied DOS curves and compares them against hidden reference values derived from the paper. For the band‑gap vs. diameter table, the verifier verifies the trend (e.g., a monotonic decrease with increasing diameter) and checks that the reported gaps are consistent with those reference values. The final reward is a weighted combination of per‑artifact scores. You must genuinely execute the time‑dependent tight‑binding workflow; simply reporting known numbers will not satisfy the verifier.
