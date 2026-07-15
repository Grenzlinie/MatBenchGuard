# Tight-Binding Model of g-Wave Altermagnet Spin Splitting

## Problem background
Altermagnets are a recently recognized class of collinear antiferromagnets that can exhibit non‑relativistic spin splitting (NRSS) of electronic bands—a momentum‑dependent lifting of spin degeneracy driven by symmetry rather than spin‑orbit coupling. In a g‑wave altermagnet the spin splitting alternates sign in a characteristic pattern with four nodal surfaces in the Brillouin zone. A tight‑binding model combined with a symmetry‑constrained adaptive basis (SCAB) captures the essential physics: orbital‑polarized hopping, sublattice‑dependent crystal field, and effective antiferromagnetic exchange. This task asks you to implement the SCAB‑based tight‑binding Hamiltonian for a prototypical g‑wave altermagnet and compute its band structure along a specified k‑path, producing a CSV file that will be evaluated by a hidden verifier for the presence and fidelity of the spin splitting.

## Approach
The model is built around a symmetry‑constrained adaptive basis (SCAB) that transforms from standard cubic d‑orbitals to a basis of complex orbitals (e_g'±, a_1g, e_g±) adapted to the local trigonal symmetry of each magnetic site. The full Hamiltonian is H = H0 + H_CF + H_AFM. H0 contains nearest‑neighbor hopping between magnetic‑ion d‑orbitals and ligand p_z orbitals, parameterized by Slater‑Koster integrals (V_σ, V_π) and direction cosines that reflect the bond geometry. H_CF is a diagonal crystal‑field matrix that assigns different onsite energies to the SCAB orbitals on each sublattice, using parameters δ1 and δ2 to encode the octahedral crystal field and trigonal distortion. H_AFM is an effective staggered exchange term of strength m_AFM, with local moments pointing +z on one sublattice and −z on the other. Because the exchange is collinear, spin‑up and spin‑down blocks can be diagonalized separately. The Bloch Hamiltonian is constructed for each k‑point on the M''–Γ'–M' path, and the eigenvalues (band energies) are collected for both spin channels.

## Reproduction target
Your main deliverable is a CSV file, tb_band_structure.csv, that lists the band energies for spin‑up (spin = +1) and spin‑down (spin = -1) at a uniform grid of k‑points along the path from M'' = (-0.5, 0, 0.25) through Γ' = (0, 0, 0.25) to M' = (0.5, 0, 0.25) in reciprocal lattice units. Each row must record the k‑point index, the three reciprocal‑space coordinates, the spin channel, the band index (1‑based within each spin block), and the energy in eV. The verifier will examine the spin splitting at hidden k‑points to confirm both the alternating spin texture characteristic of a g‑wave altermagnet and the correct magnitude of the splitting.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Construct SCAB basis and crystal field matrices
- Role: process
- Action: Construct the symmetry-constrained adaptive basis (SCAB) rotation matrix P_{SCAB←d} that transforms from the standard cubic d-orbital basis to the SCAB orbitals (e_g'±, a_1g, e_g±). Then define the diagonal crystal-field matrices Δ_I and Δ_II for the two sublattices using parameters δ1=1.2 and δ2=−0.2, ensuring that Δ_II is obtained from Δ_I by the sublattice-transposing symmetry operation (C_{6z} or M_z).
- Evidence: `/app/outputs/scab_crystal_field.npz`

### Step 2: Set up tight-binding Hamiltonian in k-space
- Role: process
- Action: Implement the Bloch Hamiltonian H(k) = H0(k) + H_CF + H_AFM. Compute nearest-neighbour magnetic-ion (M) to ligand (L) hopping matrices using Slater-Koster integrals with Vσ=−1, Vπ=−0.7, direction cosines l=cos(37°), n=cos(53°), and onsite energies ε_M=0, ε_L=−2. Rotate the hoppings into the SCAB basis. Incorporate the crystal-field matrices from Step 1 and the effective staggered antiferromagnetic exchange term with m_AFM=0.2, where local moments point ±z on the two sublattices. The Hamiltonian is collinear, so spin-up and spin-down blocks can be treated separately.
- Evidence: `/app/outputs/hamiltonian_setup.log`

### Step 3: Compute band structure along M''-Γ'-M' path
- Role: scored (load-bearing)
- Action: Diagonalize H(k) at a uniform grid of k-points along the path: start M''=(-0.5,0,0.25), middle Γ'=(0,0,0.25), end M'=(0.5,0,0.25) in reciprocal lattice units. For each k-point and each spin block, obtain eigenvalues and output them to tb_band_structure.csv.
- Output file: `/app/outputs/tb_band_structure.csv`
- Format: csv
- Contract: columns: k_index (int, 1-based sequential index along the path), kx (float), ky (float), kz (float), spin (int, +1 for up, -1 for down), band_index (int, 1-based ordering within that spin block), energy (eV)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/tb_band_structure.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### tb_band_structure.csv
- path: `/app/outputs/tb_band_structure.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Band structure eigenvalues for both spin channels along the M''-Γ'-M' k-path. The hidden checker verifies the spin splitting magnitude and sign reversal at specific k-points.
- schema:
  - `type`: csv
  - `required_columns`: `k_index`, `kx`, `ky`, `kz`, `spin`, `band_index`, `energy`
  - `units`:
    - `energy`: eV

Notes: The scored target is the tight-binding band structure that demonstrates NRSS. The checker uses a hidden reference for spin splitting at selected k-points, with tolerance for implementation differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "tb_band_structure.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "csv",
        "required_columns": [
          "k_index",
          "kx",
          "ky",
          "kz",
          "spin",
          "band_index",
          "energy"
        ],
        "units": {
          "energy": "eV"
        }
      },
      "description": "Band structure eigenvalues for both spin channels along the M''-Γ'-M' k-path. The hidden checker verifies the spin splitting magnitude and sign reversal at specific k-points."
    }
  ],
  "notes": "The scored target is the tight-binding band structure that demonstrates NRSS. The checker uses a hidden reference for spin splitting at selected k-points, with tolerance for implementation differences."
}
```

## How you are scored
A hidden verifier evaluates each workflow stage artifact. The primary scored artifact is tb_band_structure.csv (Step 3). The verifier extracts the spin splitting (difference between spin‑up and spin‑down energies for corresponding bands) at specific k‑points along the path, compares them to a correct reference, and checks for the required sign reversal. Step 1 and Step 2 are process steps that are not separately scored but are required because the verifier expects a band structure consistent with the correct SCAB basis and Hamiltonian. The final reward is a weighted sum of scores across all scored artifacts, with the CSV file carrying the bulk of the weight.
