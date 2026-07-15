# Reproduce critical interlayer expansion and topological blocking of surface states in Bi(111) using tight-binding model

## Problem background
The topological classification of bismuth (Bi) and its alloys has been intensely debated, with conflicting experimental and theoretical evidence regarding whether Bi(111) is a trivial or topological insulator. A key open question is how surface relaxation—structural modifications near the surface that change interlayer distances—affects the topological nature and surface state signatures. Recent density functional theory studies have revealed a substantial expansion of inter-bilayer spacing near the Bi(111) surface. This structural modulation may locally alter the electronic topology, potentially blocking the appearance of the surface states expected from bulk-edge correspondence. In this task, you will investigate the interplay between surface relaxation and topology by reproducing the critical inter-bilayer expansion that drives a bulk band inversion, the resulting wavefunction redistribution of surface states, and the suppression of the one‑particle spectral intensity at the surface.

## Approach
Use a relativistic empirical tight‑binding model (the Liu–Allen model for bulk Bi) with the hopping‑distance scaling V ∝ d⁻² to describe inter‑bilayer coupling. Include the surface potential introduced by Saito et al. to capture thin‑film effects. The model is fully determined by published parameters and the rhombohedral crystal structure of Bi (space group R‑3m, lattice constants a=4.546 Å, α=57.23°).

First, compute the energies of the conduction and valence bands at the bulk L‑point as a function of a uniform inter‑bilayer expansion Δd/d₀. Identify the critical expansion where the bands invert (the gap closes).

Then construct a real‑space slab Hamiltonian for a 100‑bilayer Bi(111) film with ten relaxed surface bilayers on one side. Apply two expansion values: one below and one above the critical expansion. Diagonalize the slab Hamiltonian at the M‑bare point to obtain eigenvalues and eigenvectors, identify the two surface states S1 and S2, and compute their normalized probability distributions along the bilayer direction.

Finally, evaluate the one‑particle spectral function at the surface bilayer (z=1 BL) for the relaxed vs. unrelaxed slab using a self‑energy broadening of 0.03 eV. From this, extract the blocking ratio—the ratio of the surface spectral peak intensity with relaxation to that without relaxation.

## Reproduction target
1. **Critical expansion**: Compute the critical uniform inter‑bilayer expansion Δd_c/d₀ (in percent) where the bulk L‑point conduction and valence bands invert.  
2. **Wavefunction profiles**: For a 100‑bilayer slab with 10 relaxed surface layers, provide the normalized probability distributions of the two surface states S1 and S2 at two inter‑bilayer expansion values: Δd/d₀ = 0.2% and 3%. The distribution should be reported for each bilayer index z = 1…100.  
3. **Blocking ratio**: Report the ratio of the peak spectral intensity of the surface states at the first bilayer (z=1 BL) for the relaxed slab (Δd/d₀ = 3%) to that of the unrelaxed slab (Δd = 0).

## Assets

- Liu-Allen tight-binding model for bulk Bi: 10.1103/PhysRevB.52.1566
- Saito surface potential for Bi(111): 10.1103/PhysRevB.93.041301
- Crystal structure of bismuth

## Workflow steps

### Step 1: Construct Liu-Allen TB Hamiltonian with V∝d⁻² scaling
- Role: process
- Action: Implement the Liu-Allen relativistic empirical tight-binding model for bulk Bi, including the V∝d⁻² scaling of interatomic hopping with inter-bilayer distance. This forms the foundation for all subsequent calculations.
- Evidence: `/app/outputs/tb_implementation.log`

### Step 2: Compute critical inter-bilayer expansion
- Role: scored (load-bearing)
- Action: Using the scaled TB model from step 1, compute the energies of the conduction and valence bands at the bulk L point as a function of uniform inter-bilayer expansion Δd/d0. Determine the critical expansion Δd_c/d0 at which the bands invert (the band gap closes). Write a single floating-point number representing the critical expansion in percent to the output file.
- Output file: `/app/outputs/critical_expansion.txt`
- Format: txt
- Contract: Plain text file containing one floating-point percentage (e.g., 0.XX).
- Scoring: scored by hidden verifier

### Step 3: Construct 100-BL Bi(111) slab with surface relaxation
- Role: process
- Action: Using the same TB model and the Saito surface potential, construct the real-space slab Hamiltonian for a 100-bilayer Bi(111) film with m_sur=10 relaxed surface layers. Apply the two targeted inter-bilayer expansions: Δd/d0 = 0.2% and Δd/d0 = 3% to the relaxed layers.
- Evidence: `/app/outputs/slab_hamiltonian_setup.log`

### Step 4: Diagonalize slab Hamiltonian for two expansion cases
- Role: process
- Action: Diagonalize the slab Hamiltonians constructed in step 3 for both Δd/d0=0.2% and 3% to obtain eigenvalues and eigenvectors. Identify the surface states S1 and S2 at the M-bar point.
- Evidence: `/app/outputs/slab_eigenvalues.npy`

### Step 5: Extract surface-state wavefunction profiles
- Role: scored
- Action: For each expansion case (Δd/d0=0.2% and 3%), extract the normalized probability distribution |ψ(z)|² of the two identified surface states S1 and S2 along the bilayer index z (from 1 to 100 BL). Write the profiles as a CSV file with columns: z, prob_S1_0.2, prob_S2_0.2, prob_S1_3.0, prob_S2_3.0. Each probability column should be normalized so that the sum over all z equals 1.
- Output file: `/app/outputs/wavefunction_profiles.csv`
- Format: csv
- Contract: Columns: z (integer bilayer index 1..100), prob_S1_0.2 (float), prob_S2_0.2 (float), prob_S1_3.0 (float), prob_S2_3.0 (float). Probabilities are normalized to sum to 1 over the 100 bilayers.
- Scoring: scored by hidden verifier

### Step 6: Compute one-particle spectral blocking ratio
- Role: scored
- Action: For a 100-BL slab, compute the one-particle spectral function A(k∥=M-bar, z=1 BL, ε) at the energy of the surface state peak using the eigenvectors from step 4. Use a self-energy broadening Σ''=0.03 eV. Calculate the blocking ratio as the ratio of the peak spectral intensity with relaxation (Δd/d0=3%) to the peak intensity without relaxation (Δd=0). Write this ratio as a single floating-point number to the output file.
- Output file: `/app/outputs/blocking_ratio.txt`
- Format: txt
- Contract: Plain text file containing one floating-point number (e.g., 0.XX).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/critical_expansion.txt`
- `/app/outputs/wavefunction_profiles.csv`
- `/app/outputs/blocking_ratio.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### critical_expansion.txt
- path: `/app/outputs/critical_expansion.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: The critical inter-bilayer expansion (in percent) at which the bulk L-point band gap closes.
- schema:
  - `type`: text
  - `description`: A single floating-point number (percentage) representing the critical inter-bilayer expansion Δd_c/d0.

### wavefunction_profiles.csv
- path: `/app/outputs/wavefunction_profiles.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Probability distribution of surface states along the bilayer index, used to verify the topological blocking threshold.
- schema:
  - `type`: table
  - `required_columns`: `z`, `prob_S1_0.2`, `prob_S2_0.2`, `prob_S1_3.0`, `prob_S2_3.0`
  - `description`: Normalized probability distributions of surface states S1 and S2 for two expansion values.

### blocking_ratio.txt
- path: `/app/outputs/blocking_ratio.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: The ratio of surface state spectral peak intensity with relaxation (Δd=3%) to that without relaxation (Δd=0).
- schema:
  - `type`: text
  - `description`: A single floating-point number representing the blocking ratio (ratio of peak spectral intensities).

Notes: The task uses the Liu-Allen model parameters, Saito surface potential, and Bi crystal structure, all publicly available. The inter-bilayer expansion values (0.2% and 3%) and the surface relaxation profile (m_sur=10) are taken from the paper. The critical expansion and blocking ratio are compared to reference values with appropriate hidden tolerances. The wavefunction profiles are subject to structural checks (integrated probability thresholds to confirm blocking).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "critical_expansion.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "A single floating-point number (percentage) representing the critical inter-bilayer expansion Δd_c/d0."
      },
      "description": "The critical inter-bilayer expansion (in percent) at which the bulk L-point band gap closes."
    },
    {
      "file": "wavefunction_profiles.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "z",
          "prob_S1_0.2",
          "prob_S2_0.2",
          "prob_S1_3.0",
          "prob_S2_3.0"
        ],
        "description": "Normalized probability distributions of surface states S1 and S2 for two expansion values."
      },
      "description": "Probability distribution of surface states along the bilayer index, used to verify the topological blocking threshold."
    },
    {
      "file": "blocking_ratio.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "A single floating-point number representing the blocking ratio (ratio of peak spectral intensities)."
      },
      "description": "The ratio of surface state spectral peak intensity with relaxation (Δd=3%) to that without relaxation (Δd=0)."
    }
  ],
  "notes": "The task uses the Liu-Allen model parameters, Saito surface potential, and Bi crystal structure, all publicly available. The inter-bilayer expansion values (0.2% and 3%) and the surface relaxation profile (m_sur=10) are taken from the paper. The critical expansion and blocking ratio are compared to reference values with appropriate hidden tolerances. The wavefunction profiles are subject to structural checks (integrated probability thresholds to confirm blocking)."
}
```

## How you are scored
A hidden verifier independently evaluates each of the three workflow artifacts against reference expectations derived from the published findings. The scoring is based on the physical quantities themselves, not on matching exact published numbers, and tolerances are set to account for legitimate differences arising from re‑implementation (e.g., numerical discretization, eigenvalue sorting).  
- **critical_expansion.txt** is checked for agreement with the expected critical value.  
- **wavefunction_profiles.csv** is audited structurally: the verifier checks whether the normalized probability is concentrated near the surface or pushed deeper into the slab in the expected regimes.  
- **blocking_ratio.txt** is compared to the expected suppression range.

The per‑artifact scores are combined by weight to produce a final reward between 0 and 1. No single metric value or tolerance is disclosed to you; you must compute the results from the described model and protocol.
