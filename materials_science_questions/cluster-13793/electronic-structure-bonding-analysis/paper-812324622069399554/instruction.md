# Electronic Structure of Palladium Chloride from Xα-SW Cluster Calculations

## Problem background
Palladium chloride (PdCl₂) is an important catalyst in both homogeneous and heterogeneous processes, yet its electronic structure remains poorly understood. Early models described the valence band as composed of separate Pd 4d and Cl 3p subbands with limited interaction, but experimental X-ray photoelectron spectroscopy (XPS) data show an intensity ratio between the mid-valence and Pd 4d region that cannot be explained by a purely ionic picture, implying substantial orbital mixing. A quantitative theoretical investigation using expanded cluster models and the Xα scattered-wave method can resolve this discrepancy by accounting for metal‑metal and bridging‑ligand interactions that are absent in simpler single‑sphere approximations.

## Approach
The core of this reproduction is a spin‑unpolarized Xα scattered‑wave (Xα-SW) calculation on the Pd₆Cl₈⁴⁺ cluster, which captures the essential bonding topology of polymeric PdCl₂. The cluster geometry is built such that chlorine atoms form a cube and palladium atoms sit at the centers of the cube faces with a small out‑of‑plane displacement, yielding local C₄ᵥ symmetry and realistic Pd–Pd and Pd–Cl distances. The Xα-SW method then solves the electronic structure, providing the one‑electron energies and the percentage composition of each molecular orbital in terms of Pd 5s, 5p, 4d, Cl 3s, 3p, and the intersphere (II) and outer‑sphere (III) regions. Using supplied atomic photoionization cross sections for Al Kα radiation, the total cross section of each occupied MO is computed and normalized so that a reference MO has unit cross section. This computational framework allows the agent to obtain a fully specified set of MO energies and compositions that can be directly contrasted with XPS valence‑band features.

## Reproduction target
Perform the Xα-SW calculation as described and produce a CSV file `/app/outputs/mo_energies_compositions.csv` that contains the molecular orbital labels, eigenvalues (in eV), percentage compositions from each atomic orbital and intersphere region, and the normalized photoionization cross section for every occupied valence MO. The file must be ordered by decreasing eigenvalue. This CSV is the sole scored artifact; the underlying cluster geometry and calculation log are provided as supporting evidence of faithful execution.

## Assets

- Xα Scattered-Wave Method Implementation
- Atomic photoionization cross sections (Al Kα): 10.1016/0368-2048(76)80011-6

## Workflow steps

### Step 1: Build Pd₆Cl₈⁴⁺ cluster geometry
- Role: process
- Action: Construct the Cartesian coordinates for the Pd₆Cl₈⁴⁺ cluster with O_h symmetry. Pd atoms at centers of Cl cube faces; Cl cube edge 0.328 nm. Pd-Pd distance shortened to 0.334 nm with out-of-plane displacement z=0.053 nm for Pd atoms from the face planes, yielding local C₄ᵥ symmetry. Sphere radii: r_Pd=0.1249 nm, r_Cl=0.1061 nm, outer sphere radius 0.3805 nm. Save the geometry and radii for the Xα-SW calculation.
- Evidence: `/app/outputs/cluster_geometry.txt`

### Step 2: Run Xα-SW calculation on Pd₆Cl₈⁴⁺
- Role: process
- Action: Perform a spin-unpolarized Xα scattered-wave calculation on the Pd₆Cl₈⁴⁺ cluster using the geometry from Step 1. Compute the molecular orbital eigenvalues (energies) and the percentage contributions from each atomic orbital type (Pd 5s, 5p, 4d; Cl 3s, 3p) and intersphere regions (II, III) for all occupied valence MOs. Use the standard Xα exchange parameter α ≈ 0.7.
- Evidence: `/app/outputs/xasw_output.log`

### Step 3: Generate Table 1 with photoionization cross sections
- Role: scored (load-bearing)
- Action: From the MO compositions obtained in Step 2 and given atomic photoionization cross sections under Al Kα excitation (σ(Cl 3p)=0.0239, σ(Pd 4d)=0.1235, others zero), compute the total photoionization cross section for each MO as the sum of (fraction contribution of each AO type) × (per-electron cross section). Normalize all cross sections so that the 1t₁g MO has cross section 1.00. Write a CSV file /app/outputs/mo_energies_compositions.csv with columns: MO, epsilon_eV, Pd_5s_pct, Pd_5p_pct, Pd_4d_pct, Cl_3s_pct, Cl_3p_pct, region_II_pct, region_III_pct, photoionization_cross_section. Order rows by decreasing epsilon_eV.
- Output file: `/app/outputs/mo_energies_compositions.csv`
- Format: csv
- Contract: Columns: MO (string), epsilon_eV (float), Pd_5s_pct (float), Pd_5p_pct (float), Pd_4d_pct (float), Cl_3s_pct (float), Cl_3p_pct (float), region_II_pct (float), region_III_pct (float), photoionization_cross_section (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mo_energies_compositions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mo_energies_compositions.csv
- path: `/app/outputs/mo_energies_compositions.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: CSV file with MO energies, compositions, and normalized photoionization cross sections for the Pd₆Cl₈⁴⁺ cluster.
- schema:
  - `type`: table
  - `required_columns`: `MO`, `epsilon_eV`, `Pd_5s_pct`, `Pd_5p_pct`, `Pd_4d_pct`, `Cl_3s_pct`, `Cl_3p_pct`, `region_II_pct`, `region_III_pct`, `photoionization_cross_section`
  - `units`:
    - `epsilon_eV`: eV
    - `photoionization_cross_section`: normalized to 1t1g MO = 1.00

Notes: Only the Pd₆Cl₈⁴⁺ cluster results are required as a scored artifact. The Pd₆Cl₁₂ cluster results (Table 2) are a secondary verification that confirms the same qualitative mixing of Pd 4d and Cl 3p states already demonstrated by the Pd₆Cl₈⁴⁺ cluster. The band structure calculation (Fig. 3) is an additional validation that the finite-cluster findings persist in the infinite lattice, but it does not introduce a distinct headline quantity — it merely shows that the band gap vanishes when using the derived EH parameters. Omitting these secondary calculations does not impair the core claim of significant covalent mixing, and including them would substantially increase task complexity without commensurate additional scoring insight.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mo_energies_compositions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "MO",
          "epsilon_eV",
          "Pd_5s_pct",
          "Pd_5p_pct",
          "Pd_4d_pct",
          "Cl_3s_pct",
          "Cl_3p_pct",
          "region_II_pct",
          "region_III_pct",
          "photoionization_cross_section"
        ],
        "units": {
          "epsilon_eV": "eV",
          "photoionization_cross_section": "normalized to 1t1g MO = 1.00"
        }
      },
      "description": "CSV file with MO energies, compositions, and normalized photoionization cross sections for the Pd₆Cl₈⁴⁺ cluster."
    }
  ],
  "notes": "Only the Pd₆Cl₈⁴⁺ cluster results are required as a scored artifact. The Pd₆Cl₁₂ cluster results (Table 2) are a secondary verification that confirms the same qualitative mixing of Pd 4d and Cl 3p states already demonstrated by the Pd₆Cl₈⁴⁺ cluster. The band structure calculation (Fig. 3) is an additional validation that the finite-cluster findings persist in the infinite lattice, but it does not introduce a distinct headline quantity — it merely shows that the band gap vanishes when using the derived EH parameters. Omitting these secondary calculations does not impair the core claim of significant covalent mixing, and including them would substantially increase task complexity without commensurate additional scoring insight."
}
```

## How you are scored
A hidden verifier reads your `mo_energies_compositions.csv` and compares each MO’s reported energy, composition percentages, and normalized photoionization cross section against the corresponding values obtained from a correct Xα-SW calculation of the same cluster. Each row is evaluated on a per‑quantity basis with predefined tolerances that account for minor numerical differences between different implementations. The final reward is the fraction of rows that satisfy all tolerance checks; full credit is awarded when at least 80% of the rows are within tolerance. Merely copying numbers from the literature without performing the calculation will not satisfy the tolerances for the majority of entries.
