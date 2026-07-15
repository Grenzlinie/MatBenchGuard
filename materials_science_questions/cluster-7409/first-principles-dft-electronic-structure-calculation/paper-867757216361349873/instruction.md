# First-principles DFT study of strain and oxygen vacancies in lanthanum aluminate

## Problem background
This task reproduces the main computational results of a density functional theory (DFT) study on the interplay between biaxial strain and oxygen vacancies in the perovskite-structure oxide lanthanum aluminate (LaAlO3). Bulk LaAlO3 undergoes oxygen octahedral rotations that lower its symmetry, and the accurate description of both structural distortions and the position of La 4f electronic states requires a careful choice of exchange-correlation functional. Applying a Hubbard U correction to the La 4f orbitals within the generalized gradient approximation (GGA+U) has been proposed to simultaneously correct the electronic structure and reproduce the experimental octahedral rotation angle. The work also evaluates whether epitaxial strain — imposed by coherent growth on a substrate with a different lattice constant — significantly alters the formation energy of oxygen vacancies, which could affect defect concentrations in strained films. The agent's task is to compute the equilibrium octahedral rotation angle for bulk LaAlO3 under the chosen functional, and to quantify how much the oxygen vacancy formation energy changes between unstrained and -2% biaxially strained conditions at a fixed oxygen-poor chemical potential.

## Approach
The approach uses plane-wave pseudopotential DFT with the PBE-GGA exchange-correlation functional and a Hubbard U correction of 10.32 eV applied to La 4f orbitals, employing the Dudarev method with the fully localized limit double-counting. The workflow has three conceptual stages:

1. **Bulk reference**: relax the rhombohedral unit cell of LaAlO3 (pseudocubic angle fixed at 90°) to obtain the equilibrium structure, and extract the magnitude of the oxygen octahedral rotation angle directly from the relaxed atomic positions.

2. **Oxygen chemical potential reference**: compute the total energy of an isolated O2 molecule with the same functional and pseudopotentials, which defines the oxygen chemical potential scale needed for the defect formation energy.

3. **Supercell formation energies**: using the bulk equilibrium lattice constant, construct 2×2×2 supercells (40 atoms) of LaAlO3: one defect-free and one with a neutral oxygen vacancy placed at the axial position perpendicular to the biaxial plane. For each supercell, perform structural relaxations at two biaxial strain states: 0% (unstrained) and −2% compressive strain. The in‑plane lattice parameters are fixed according to the strain definition ε = (a − a0)/a0, while the out‑of‑plane lattice parameter and all internal coordinates are relaxed. From the four final total energies, compute the oxygen vacancy formation energy Ω at a fixed oxygen chemical potential of −2.0 eV using the standard formation energy formula:
Ω = Etot(V_O⁰) − Etot(bulk) + μ_O,
with μ_O = μ_O,bulk − 0.5·E(O₂) and μ_O,bulk = 0 (reference). Finally, calculate the difference ΔΩ = Ω(−2%) − Ω(0%).

The key comparison is the magnitude of ΔΩ: the agent must determine whether the formation energy changes appreciably between the two strain states.

## Reproduction target
Produce two scored artifacts under `/app/outputs`:

- **`step_01_rotation_angle.txt`**: the oxygen octahedral rotation angle (in degrees) of bulk LaAlO3 relaxed with the specified PBE-GGA+U functional.
- **`step_02_formation_energy_diff.txt`**: the difference in oxygen vacancy formation energy, ΔΩ = Ω(−2%) − Ω(0%), in eV, evaluated at a fixed oxygen chemical potential of −2.0 eV using the formation energy formula described above.

Both files should contain a single floating-point number on the first line. These values will be compared to reference results derived from the source study; the closer they are, the higher the score.

## Assets

- Quantum ESPRESSO (open-source DFT code): https://www.quantum-espresso.org/
- SSSP pseudopotential library (PBE, PAW): https://www.materialscloud.org/discover/sssp/table/precision
- LaAlO3 rhombohedral crystal structure (Materials Project mp-4076): https://next-gen.materialsproject.org/materials/mp-4076

## Workflow steps

### Step 1: Bulk LaAlO3 relaxation and octahedral rotation angle
- Role: scored
- Action: Perform DFT geometry optimization of bulk rhombohedral LaAlO3 using the PBE GGA+U exchange-correlation functional with a Hubbard U correction of 10.32 eV applied to La 4f orbitals (Dudarev method, fully localized limit double-counting). Use the public crystal structure (Materials Project mp-4076) as the starting geometry, fix the pseudocubic angle at 90°, and relax the cell and atomic positions to obtain the equilibrium structure. After relaxation, extract the magnitude of the oxygen octahedral rotation from the atomic positions and write the angle (in degrees) to the output file.
- Output file: `/app/outputs/step_01_rotation_angle.txt`
- Format: txt
- Contract: A single floating-point number (the rotation angle in degrees) on the first line.
- Scoring: scored by hidden verifier

### Step 2: O2 molecule reference energy
- Role: process
- Action: Compute the total energy of an isolated O2 molecule using the same DFT functional, pseudopotentials, and energy cutoffs as in Step 1. This energy serves as the reference for the oxygen chemical potential in the formation energy analysis. Store the result as a single number in a text file.
- Evidence: `/app/outputs/o2_energy.txt`

### Step 3: Supercell total‑energy calculations under strain
- Role: process
- Action: Using the equilibrium bulk lattice constant from Step 1, construct 2×2×2 supercells (40 atoms) of LaAlO3: one defect‑free supercell and one with a single neutral oxygen vacancy placed at the axial position perpendicular to the biaxial plane. For each supercell, perform DFT relaxations at 0% and −2% biaxial strain, keeping the in‑plane lattice parameter fixed according to the strain definition (ϵ = (a−a0)/a0 with ϵ = 0 and ϵ = −0.02) while relaxing the out‑of‑plane lattice parameter and all internal coordinates. Use the same functional and pseudopotentials as in Step 1. Record the four total energies (defect‑free 0%, defect‑free −2%, vacancy 0%, vacancy −2%) in a JSON file.
- Evidence: `/app/outputs/supercell_energies.json`

### Step 4: Oxygen vacancy formation energy difference
- Role: scored (load-bearing)
- Action: Using the O2 reference energy from Step 2 and the four supercell total energies from Step 3, compute the oxygen vacancy formation energy at a fixed oxygen chemical potential of −2.0 eV (oxygen‑poor condition). Apply the formation energy formula Ω = E_tot(V_O^0) − E_tot(bulk) + μ_O, with μ_O = μ_O,bulk − 0.5·E(O2) and μ_O,bulk = 0 (reference). Calculate Ω for the unstrained (0%) and −2% strained cases, then compute the difference ΔΩ = Ω(−2%) − Ω(0%). Write this difference (in eV) to the output file.
- Output file: `/app/outputs/step_02_formation_energy_diff.txt`
- Format: txt
- Contract: A single floating-point number (the energy difference in eV) on the first line.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_rotation_angle.txt`
- `/app/outputs/step_02_formation_energy_diff.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_rotation_angle.txt
- path: `/app/outputs/step_01_rotation_angle.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: The computed octahedral rotation angle is compared to the experimental reference with a hidden tolerance.
- schema:
  - `type`: text
  - `description`: A single floating-point number representing the oxygen octahedral rotation angle (degrees).

### step_02_formation_energy_diff.txt
- path: `/app/outputs/step_02_formation_energy_diff.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: The absolute value of the formation energy difference is verified to be ≤ a hidden threshold derived from the paper’s negligible change claim.
- schema:
  - `type`: text
  - `description`: A single floating-point number representing the formation energy difference ΔΩ (eV).

Notes: Both artifacts are read by the checker; the agent must produce them at the specified paths. The rotation angle is scored by closeness to the experimental value; the formation energy difference is scored by whether its absolute value falls below the acceptable limit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_rotation_angle.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "A single floating-point number representing the oxygen octahedral rotation angle (degrees)."
      },
      "description": "The computed octahedral rotation angle is compared to the experimental reference with a hidden tolerance."
    },
    {
      "file": "step_02_formation_energy_diff.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "description": "A single floating-point number representing the formation energy difference ΔΩ (eV)."
      },
      "description": "The absolute value of the formation energy difference is verified to be ≤ a hidden threshold derived from the paper’s negligible change claim."
    }
  ],
  "notes": "Both artifacts are read by the checker; the agent must produce them at the specified paths. The rotation angle is scored by closeness to the experimental value; the formation energy difference is scored by whether its absolute value falls below the acceptable limit."
}
```

## How you are scored
A hidden verifier independently evaluates each scored artifact. The rotation angle is compared to the experimentally known value for LaAlO3, with a tolerance set to accept results that faithfully reproduce the correct octahedral tilt. The formation energy difference is checked against a threshold derived from the paper's central finding on strain sensitivity: the verifier awards full credit for the energy difference only if its absolute value falls below a hidden acceptable limit. Both conditions must be satisfied for full reward. The verifier does not see the source paper or any gold values; it only reads your output files. There is no partial credit for supplying only one artifact, and reporting the paper's numbers without executing the workflow will not suffice — the verifier's thresholds are set on the true re‑computable quantity, not on a self‑reported claim.
