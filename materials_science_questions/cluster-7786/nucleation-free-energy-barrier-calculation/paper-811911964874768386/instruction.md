# Hydrogen Spillover Nucleation Free-Energy Barrier Calculation

## Problem background
Hydrogen spillover on carbon materials is attractive for hydrogen storage, but the binding energy of a single H atom to graphene is weaker than half the H2 bond energy. This raises the question of whether and how hydrogen chemisorption can proceed in practice. The storage process can be viewed as a phase nucleation phenomenon: chemisorbed H atoms may aggregate into compact islands on the graphene surface, and collective effects within these islands could strengthen the overall binding. The central problem is to understand how the binding energy evolves with cluster size and island geometry, and whether the overall thermodynamics can be described by a nucleus free-energy profile that exhibits a nucleation barrier.

## Approach
The problem is studied via first-principles density functional theory (DFT) calculations. The Perdew-Burke-Ernzerhof (PBEPBE) exchange-correlation functional and a basis set of at least 6-31G** quality are used. Graphene is represented either as a circumcoronene (C54H18) molecular fragment or as a periodic sheet. Total energies are computed for pristine graphene, an isolated H atom, and a series of hydrogen chemisorbed configurations with increasing H coverage and different spatial arrangements: 1H, 2H in ortho same-side and ortho counterside, 3H, 4H, 6H (closed six-ring), 10H, 16H, 24H, a 12H incomplete-ring arrangement, and infinite fully hydrogenated graphene (CH). From these energies, the average binding energy per H atom, εb(n), is calculated for each configuration. The number of interfacial bonds between sp2 and sp3 carbon atoms, n23, is counted for each cluster. For compact clusters that form complete six-membered rings, the dependence of εb on the fraction n23/n is analysed. A linear fit yields the asymptotic binding energy εb(∞) (the value for an infinitely extended hydrogenated layer) and an interface energy parameter γ, along with the goodness of fit R². Using the obtained εb(∞) and γ, the Gibbs free energy ΔG(n) of a nucleus containing n chemisorbed H atoms is constructed at two thermodynamic conditions: (T=300 K, P=1 atm) and (T=500 K, P=10 atm). The chemical potential of H, μH, is obtained from the ideal-gas chemical potential of H2. The resulting ΔG(n) curves are examined to identify the critical nucleus size n* (the n that maximizes ΔG) and the associated nucleation barrier ΔG* = ΔG(n*). All computed quantities are saved in results.json.

## Reproduction target
Produce a JSON file results.json that contains the computed binding energies and nucleation analysis. The file must include: (i) for every configuration, its total energy E_total (in eV), number of chemisorbed H atoms n_H, interface bond count n23, and per‑H binding energy εb; (ii) the fitted εb(∞) (eV), γ (eV), and R²; and (iii) for the two thermodynamic conditions (300 K, 1 atm) and (500 K, 10 atm), the chemical potential μH (eV), the arrays of integer n (1 to 100) and ΔG(n) (eV), the critical nucleus size n*, and the barrier ΔG* (eV). The reported data must be internally consistent with the DFT total energies saved in total_energies.csv and with the methodology described above.

## Assets

- Open-source DFT code (e.g., Quantum ESPRESSO, GPAW, ABINIT): https://www.quantum-espresso.org/
- Basis set 6-31G** or better for C and H: https://www.basissetexchange.org

## Workflow steps

### Step 1: DFT total energy calculations
- Role: process
- Action: Build atomic models for pristine graphene (C54H18 fragment or periodic sheet) and for the following hydrogen chemisorption configurations: 1H, 2H ortho same-side, 2H ortho counterside, 3H, 4H, 6H (closed six-ring), 10H, 16H, 24H, a 12H incomplete-ring arrangement, and infinite fully hydrogenated graphene (CH). Perform DFT calculations using the PBEPBE functional and a basis set of at least 6-31G** quality. Compute the total energy for each configuration, for pristine graphene, and for an isolated H atom. Save the raw energies to total_energies.csv.
- Evidence: `/app/outputs/total_energies.csv`

### Step 2: Binding energies and nucleation analysis
- Role: scored (load-bearing)
- Action: From the DFT energies, compute per-atom average binding energy εb(n) = (E_g + n·E_H - E_nH@g)/n for every configuration. Compute incremental adsorption energies. For each configuration, count the number of sp2-sp3 interface bonds n23. For compact, aromatic clusters, perform a linear fit of εb vs. n23/n to obtain the asymptotic bulk binding εb(∞) and interface parameter γ; report the R². Using the obtained εb(∞) and γ, compute the Gibbs free energy ΔG(n) = -[εb(∞) + μ_H(P,T)]·n + γ·√n for n = 1..100 at two thermodynamic conditions (T=300 K, P=1 atm) and (T=500 K, P=10 atm), with μ_H from the ideal-gas chemical potential of H₂. Identify the critical nucleus size n* and barrier ΔG*. Write all results to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object containing an 'configurations' array (objects with name, E_total, n_H, n23, epsilon_b) and a 'nucleation' object with fields epsilon_b_infinity, gamma, R_squared, and a 'conditions' list (objects with condition, mu_H, n (array of int), DeltaG (array of float), n_star (int), DeltaG_star (float)).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Contains computed binding energies and nucleation parameters derived from DFT total energies.
- schema:
  - `type`: object
  - `required`:
    - `configurations`: array of objects with keys: name (string), E_total (number, eV), n_H (integer), n23 (integer), epsilon_b (number, eV)
    - `nucleation`: object with keys: epsilon_b_infinity (number, eV), gamma (number, eV), R_squared (number), conditions (array of objects with keys: condition (string), mu_H (number, eV), n (array of integers), DeltaG (array of numbers, eV), n_star (integer), DeltaG_star (number, eV))

Notes: The artifact will be assessed for internal consistency, monotonic trends of εb(n), linearity of εb vs. n23/n (R²≥0.99), and presence of a nucleation barrier (ΔG(n) maximum at n>1 with negative asymptotic value) for the specified thermodynamic conditions. No exact reference values are required; the structural checks determine the score.

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
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "configurations": "array of objects with keys: name (string), E_total (number, eV), n_H (integer), n23 (integer), epsilon_b (number, eV)",
          "nucleation": "object with keys: epsilon_b_infinity (number, eV), gamma (number, eV), R_squared (number), conditions (array of objects with keys: condition (string), mu_H (number, eV), n (array of integers), DeltaG (array of numbers, eV), n_star (integer), DeltaG_star (number, eV))"
        }
      },
      "description": "Contains computed binding energies and nucleation parameters derived from DFT total energies."
    }
  ],
  "notes": "The artifact will be assessed for internal consistency, monotonic trends of εb(n), linearity of εb vs. n23/n (R²≥0.99), and presence of a nucleation barrier (ΔG(n) maximum at n>1 with negative asymptotic value) for the specified thermodynamic conditions. No exact reference values are required; the structural checks determine the score."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that performs structural checks on results.json. First, the verifier will recompute εb from your reported total energies and cross‑check the values in the configurations array for internal consistency. It will then score the following structural aspects, which together capture the signatures of a nucleation process: (a) whether the binding energies show a systematic trend with cluster size and configuration; (b) whether for the compact, ring‑closed clusters the plot of εb versus the interface fraction n23/n is linear to a high degree; and (c) whether the Gibbs free energy ΔG(n) curves exhibit a distinct maximum at finite n and a negative asymptotic value under the specified conditions. Each of these three structural checks contributes equally to the final score. The exact numerical values are not compared to a fixed reference; the scoring is based on the presence and quality of these structural signatures.
