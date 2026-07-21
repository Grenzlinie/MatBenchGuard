# Inversion‑symmetry breaking, boson peak and shear modulus in harmonic network models

## Problem background
Amorphous solids and defective crystals often exhibit an excess of low-frequency vibrational modes called the boson peak, which deviates from the Debye ω² law. The microscopic structural origin of this anomaly remains debated—it is unclear whether it is controlled by bond-orientational order or by local inversion-symmetry breaking. This task addresses this problem by numerically studying harmonic spring-network models of a random-network glass and a defective FCC crystal.

## Approach
Two model systems are constructed: a random network glass and a defective FCC crystal, both based on harmonic springs with a fixed spring constant and density. For each system, the average atomic coordination number Z is varied from 6 to 9 by randomly cutting bonds while keeping a narrow distribution of Z. The vibrational density of states D(ω) is obtained by diagonalizing the dynamical (Hessian) matrix; the boson peak frequency ω_BP is identified as the maximum of the reduced density of states D(ω)/ω². The shear modulus is decomposed into an affine part G_A (Born‑Huang) and a nonaffine correction G_NA computed from the affine force field vectors and the inverse Hessian, giving the total G = G_A − G_NA. Two order parameters are computed for each configuration: the inversion‑symmetry order parameter F_IS (derived from the affine force field) and the bond‑orientational order parameter F_6 (Steinhardt‑Nelson spherical‑harmonic correlations with threshold 0.7). By evaluating these quantities as functions of Z for both systems and comparing the trends, one can infer which structural descriptor correlates with the boson peak and shear elasticity.

## Key formulas and definitions

### Harmonic spring network
Atoms interact via a harmonic pair potential:
V_{ij}(r_{ij}) = (κ/2) (r_{ij} − R₀)²,
where κ = 1 is the spring constant, R₀ = 0.94 is the reference bond length, and r_{ij} = |r_i − r_j|. Bonds exist only between nearest neighbours (defined during the configuration generation stage). The equilibrium length of each bond is R₀; the unit vector from atom i to atom j is n_{ij} = (r_j − r_i)/r_{ij}.

### Dynamical (Hessian) matrix
The Hessian matrix H of the harmonic spring network is a 3N × 3N matrix whose entries are given by, for α,β ∈ {x,y,z}:

- Off-diagonal blocks (i ≠ j):
  (H)_{iα, jβ} = −κ n_{ij}^{α} n_{ij}^{β}   if i and j are bonded,
  (H)_{iα, jβ} = 0                           otherwise.

- Diagonal blocks (i = j):
  (H)_{iα, iβ} = κ Σ_{k∈∂i} n_{ik}^{α} n_{ik}^{β},

where ∂i denotes the set of atoms bonded to atom i.

Since the initial configurations may not be in global mechanical equilibrium (the actual bond lengths scatter around R₀), we adopt a **harmonic approximation**: construct H using the current bond unit vectors n_{ij} (taken from the generated positions) and the spring constant κ, ignoring any residual forces. This prescription is standard for disordered spring networks and yields a positive semi‑definite Hessian whose eigenvalues faithfully represent the vibrational spectrum.

### Handling translational zero-modes
The Hessian H is invariant under rigid translations, therefore it has three zero eigenvalues (zero modes) associated with these symmetries. To compute the inverse required for G_NA, you must remove these singular directions. Use the **Moore–Penrose pseudo‑inverse** H⁺ (e.g., `numpy.linalg.pinv` or `scipy.linalg.pinvh` with a suitable rcond threshold). Alternatively, a small regularisation H ≈ H + ε I with ε = 1e−6 can be used, but the pseudo‑inverse is recommended because it faithfully respects the null‑space.

### Born‑Huang affine shear modulus G_A
For a central‑force harmonic network under simple shear (strain γ = γ_{xy}), the affine (Born‑Huang) shear modulus is

G_A = (κ R₀² / V) Σ_{⟨i,j⟩} (n_{ij}^x n_{ij}^y)² ,

where V is the volume of the simulation box, and the sum runs over all bonded pairs ⟨i,j⟩.

### Affine force field vector Ξ_i
The affine force field vector for atom i, which quantifies the unbalanced forces that would arise under a purely affine shear deformation, has Cartesian components

Ξ_i^α = − κ R₀ Σ_{j∈∂i} n_{ij}^α n_{ij}^x n_{ij}^y ,   (α = x,y,z),

where ∂i denotes the set of atoms bonded to i. The 3N‑dimensional vector Ξ is formed by concatenating the three components of Ξ_i for all atoms i = 1…N.

### Nonaffine shear modulus G_NA and total G
The nonaffine correction to the shear modulus is

G_NA = (1/V) Ξ^T H⁺ Ξ ,

where H⁺ is the pseudo‑inverse of the Hessian (see above). The total shear modulus is

G = G_A − G_NA .

### Inversion‑symmetry order parameter F_IS
The local inversion‑symmetry breaking is measured by

F_IS = ( 1 / (κ² R₀² N Z) ) Σ_{i=1}^{N} |Ξ_i|² ,

where |Ξ_i|² = (Ξ_i^x)² + (Ξ_i^y)² + (Ξ_i^z)², N = 4000 is the number of atoms, and Z is the average coordination number.

### Bond‑orientational order parameter F_6
The bond‑orientational order parameter is computed using the Steinhardt‑Nelson algorithm with a connectivity criterion. The procedure is:

1. **Neighbour definition** – For each atom i, the set of neighbours ∂i consists of all atoms j that are connected by a harmonic bond in the given configuration. These bonds are the same ones used to build the Hessian matrix; they define the “first coordination shell”.

2. **Local order parameter q₆(i)** – For each atom i, compute the complex vector q₆(i) with components (m = −6,…,6):
   q_{6m}(i) = (1/N_b(i)) Σ_{j∈∂i} Y_{6m}(θ_{ij}, φ_{ij}),
   where N_b(i) is the number of bonds of atom i, and Y_{lm} are the spherical harmonics evaluated for the direction n_{ij} (θ, φ) of each bond. Use the standard Condon‑Shortley phase convention as implemented in `scipy.special.sph_harm(m, l, φ, θ)` (note the ordering of arguments: m, l, azimuth, polar).

3. **Configurational order parameter** – The global bond‑orientational order parameter F₆ is defined as the average of the dot product q₆(i)·q₆(j) over all atomic pairs (i,j) whose dot product exceeds a threshold S₆⁰ = 0.7. Only pairs that are “connected” in the sense of having a large overlap of their local orientational order are considered. Formally:
   F₆ = (1/N_c) Σ_{i<j, q₆(i)·q₆(j) > S₆⁰} q₆(i)·q₆(j),
   where N_c is the number of such “connected” pairs. If no pair exceeds the threshold, F₆ = 0. For a perfect FCC crystal F₆ ≈ 1, for a fully random network F₆ ≈ 0.3, and it is nearly independent of Z.

### Vibrational density of states D(ω) and boson peak
The eigenvalues λ of the Hessian matrix give the squared eigenfrequencies ω² = λ. The density of states D(ω) is obtained by binning the frequencies ω = √λ into a histogram with uniform bin width Δω = 0.02 over the range 0 ≤ ω ≤ ω_max (typical ω_max ≈ 2.5). The reduced DOS is D(ω)/ω²; the boson peak frequency ω_BP is the frequency at which D(ω)/ω² attains its maximum (excluding the ω → 0 limit).

## Reproduction target
Produce the following averaged quantities for the random-network glass and the defective FCC crystal at Z = 6, 7, 8, 9 (at least three independent realizations per condition): (i) shear modulus components G, G_A, G_NA; (ii) inversion‑symmetry order parameter F_IS; (iii) bond‑orientational order parameter F_6; (iv) boson peak frequency ω_BP; (v) the full vibrational density of states D(ω) curves. The outputs must be written as specified CSV and JSON files. The results should allow examining the scaling with connectivity and the comparison between the glass and crystal, to evaluate the correlation between the order parameters and the boson peak.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Generate random network glass configurations
- Role: process
- Action: Generate harmonic random‑network (RN) glass configurations with N=4000 atoms, density ρ=N/V=1.467, harmonic spring constant κ=1, reference bond length R₀=0.94, covering average coordination numbers Z=6,7,8,9. Start from a soft‑sphere packing relaxed by Monte Carlo using the truncated Lennard‑Jones potential V_{LJ}(r) = (1/r^{12} − 2/r^{6} + 0.031) Θ(2−r) (cut‑off radius r_c = 2). Replace all interactions with harmonic springs between nearest neighbours, then randomly cut bonds to achieve each target Z while keeping a narrow Z distribution. Produce at least 3 independent realizations per Z.
- Evidence: `/app/outputs/rn_config_log.txt`

### Step 2: Generate defective FCC crystal configurations
- Role: process
- Action: Generate defective FCC crystal configurations at the same density ρ=1.467 and harmonic spring constant κ=1, with average coordination Z=6,7,8,9. Start from a perfect FCC lattice with a lattice constant matching the density, introduce harmonic springs between nearest neighbours, then randomly cut bonds to reach each target Z while maintaining a narrow Z distribution. Produce at least 3 independent realizations per Z.
- Evidence: `/app/outputs/fcc_config_log.txt`

### Step 3: Build Hessian and diagonalize to obtain normal modes
- Role: process
- Action: For every realization of each system (RN and FCC) and each Z, construct the dynamical (Hessian) matrix from the harmonic spring network using the formulas in **Key formulas**, then diagonalize it (e.g., using scipy.linalg.eigh) to obtain the eigenfrequencies ω = √λ and eigenvectors. Store the sets of eigenfrequencies for each condition; they are needed for DOS, boson peak, and shear modulus calculations.
- Evidence: `/app/outputs/hessian_diag_log.txt`

### Step 4: Calculate shear modulus (affine and nonaffine)
- Role: scored (load‑bearing)
- Action: For each configuration (system, Z, realization), compute the affine shear modulus G_A via the Born‑Huang formula and the nonaffine correction G_NA = Ξᵀ H⁺ Ξ using the pseudo‑inverse of the Hessian (see **Key formulas** for H⁺). The total shear modulus is G = G_A − G_NA. Average over realizations and output one row per (system, Z) pair.
- Output file: `/app/outputs/shear_modulus.csv`
- Format: csv
- Contract: Columns: system, Z, G, G_A, G_NA
- Scoring: scored by hidden verifier – internal consistency (G ≈ G_A − G_NA, G_A > 0, G_NA ≥ 0) and physically expected trends (G increases with Z) are verified.

### Step 5: Calculate order parameters F_IS and F_6
- Role: scored
- Action: For each configuration, compute the inversion‑symmetry order parameter F_IS from the affine force field Ξ_i using the formula in **Key formulas** (normalization denominator κ² R₀² N Z) and the bond‑orientational order parameter F_6 from Steinhardt‑Nelson spherical‑harmonic correlations with threshold S₆⁰=0.7, as detailed above. Average over realizations and output one row per (system, Z) pair.
- Output file: `/app/outputs/order_parameters.csv`
- Format: csv
- Contract: Columns: system, Z, F_IS, F_6
- Scoring: scored by hidden verifier

### Step 6: Boson peak frequency
- Role: scored
- Action: From the eigenfrequencies, compute the vibrational density of states D(ω) as a histogram with uniform bin width Δω = 0.02 and the reduced DOS D(ω)/ω². Identify the boson peak frequency ω_BP as the frequency of the maximum in D(ω)/ω² (excluding the zero‑frequency limit). Average over realizations and output one row per (system, Z) pair.
- Output file: `/app/outputs/boson_peak.csv`
- Format: csv
- Contract: Columns: system, Z, omega_BP
- Scoring: scored by hidden verifier

### Step 7: Density of states data (JSON)
- Role: scored
- Action: Save the averaged D(ω) for each condition to a JSON file. Use uniformly spaced frequency bins of width Δω = 0.02 and the averaged histogram over at least three realizations.
- Output file: `/app/outputs/dos_data.json`
- Format: json
- Contract: Top-level dictionary with condition keys; each condition maps to a dictionary with keys 'frequencies' (list of floats) and 'dos' (list of floats).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/rn_config_log.txt`
- `/app/outputs/fcc_config_log.txt`
- `/app/outputs/hessian_diag_log.txt`
- `/app/outputs/shear_modulus.csv`
- `/app/outputs/order_parameters.csv`
- `/app/outputs/boson_peak.csv`
- `/app/outputs/dos_data.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### rn_config_log.txt
- path: `/app/outputs/rn_config_log.txt`
- format: txt
- purpose: unscored
- description: Log file confirming the generation of RN glass configurations. Not scored, but required as evidence of Step 1.

### fcc_config_log.txt
- path: `/app/outputs/fcc_config_log.txt`
- format: txt
- purpose: unscored
- description: Log file confirming the generation of defective FCC crystal configurations. Not scored, but required as evidence of Step 2.

### hessian_diag_log.txt
- path: `/app/outputs/hessian_diag_log.txt`
- format: txt
- purpose: unscored
- description: Log file showing Hessian construction and diagonalization. Not scored, but required as evidence of Step 3.

### shear_modulus.csv
- path: `/app/outputs/shear_modulus.csv`
- format: csv
- purpose: scored
- target_policy: consistency_and_trends
- description: Shear modulus (affine and nonaffine) for RN glass and defective FCC crystal at Z=6,7,8,9. The verifier checks that G = G_A − G_NA (within numerical tolerance), that G_A > 0 and G_NA ≥ 0, and that G increases monotonically with Z for each system.
- schema:
  - `type`: table
  - `required_columns`: `system`, `Z`, `G`, `G_A`, `G_NA`
  - `units`:
    - `G`: harmonic units
    - `G_A`: harmonic units
    - `G_NA`: harmonic units

### order_parameters.csv
- path: `/app/outputs/order_parameters.csv`
- format: csv
- purpose: scored
- target_policy: consistency_and_trends
- description: Inversion‑symmetry order parameter F_IS and bond‑orientational order parameter F_6. The verifier checks that 0 ≤ F_IS ≤ 1, F_IS increases monotonically with Z, F_6 ≈ 1.0 for FCC and ≈ 0.3 for RN (within reasonable bounds), and that F_6 is nearly independent of Z.
- schema:
  - `type`: table
  - `required_columns`: `system`, `Z`, `F_IS`, `F_6`
  - `units`: object

### boson_peak.csv
- path: `/app/outputs/boson_peak.csv`
- format: csv
- purpose: scored
- target_policy: consistency_and_trends
- description: Boson peak frequency (maximum of D(ω)/ω²) for each condition. The verifier checks that ω_BP > 0 and increases monotonically with Z.
- schema:
  - `type`: table
  - `required_columns`: `system`, `Z`, `omega_BP`
  - `units`:
    - `omega_BP`: frequency units

### dos_data.json
- path: `/app/outputs/dos_data.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Averaged vibrational density of states D(ω) curves. The checker verifies that the maximum of D(ω)/ω² coincides with the reported omega_BP and that the overall shape is physically plausible (Debye regime, boson peak).
- schema:
  - `type`: object
  - `required`: `RN_Z6`, `RN_Z7`, `RN_Z8`, `RN_Z9`, `FCC_Z6`, `FCC_Z7`, `FCC_Z8`, `FCC_Z9`
  - `items`:
    - `type`: object
    - `required`: `frequencies`, `dos`

Notes: All scored numbers are the agent's computed averages over at least 3 independent realizations per condition. The checker verifies physical self‑consistency and expected qualitative behaviour, not exact numerical values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "rn_config_log.txt",
      "format": "txt",
      "purpose": "unscored",
      "description": "Evidence log for RN glass configuration generation."
    },
    {
      "file": "fcc_config_log.txt",
      "format": "txt",
      "purpose": "unscored",
      "description": "Evidence log for FCC crystal configuration generation."
    },
    {
      "file": "hessian_diag_log.txt",
      "format": "txt",
      "purpose": "unscored",
      "description": "Evidence log for Hessian diagonalization."
    },
    {
      "file": "shear_modulus.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "consistency_and_trends",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "Z",
          "G",
          "G_A",
          "G_NA"
        ],
        "units": {
          "G": "harmonic units",
          "G_A": "harmonic units",
          "G_NA": "harmonic units"
        }
      },
      "description": "Shear modulus for RN and FCC at Z=6,7,8,9. The verifier checks G = G_A - G_NA, positivity, and monotonic increase with Z."
    },
    {
      "file": "order_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "consistency_and_trends",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "Z",
          "F_IS",
          "F_6"
        ],
        "units": {}
      },
      "description": "Order parameters F_IS and F_6. Verifier checks ranges and monotonicity."
    },
    {
      "file": "boson_peak.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "consistency_and_trends",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "Z",
          "omega_BP"
        ],
        "units": {
          "omega_BP": "frequency units"
        }
      },
      "description": "Boson peak frequency. Verifier checks positivity and monotonic increase with Z."
    },
    {
      "file": "dos_data.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "RN_Z6",
          "RN_Z7",
          "RN_Z8",
          "RN_Z9",
          "FCC_Z6",
          "FCC_Z7",
          "FCC_Z8",
          "FCC_Z9"
        ],
        "items": {
          "type": "object",
          "required": [
            "frequencies",
            "dos"
          ]
        }
      },
      "description": "Averaged D(ω) curves. Checker verifies that the peak of D(ω)/ω² coincides with reported ω_BP and that the shape is physically plausible."
    }
  ],
  "notes": "All scored numbers are the agent's computed averages over at least 3 independent realizations per condition. The checker verifies physical self‑consistency and expected trends, not exact numerical values."
}
```