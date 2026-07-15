# Ab initio SCF study of beryllium interactions with acetylene and ethylene: binding energies and equilibrium separations

## Problem background
Understanding the interaction between metal atoms and unsaturated hydrocarbons is fundamental to organometallic chemistry and surface catalysis. Beryllium, with its simple electronic structure, serves as a model system to probe the bonding mechanisms that may also occur with transition metals. This work investigates the potential energy surfaces for the approach of Be⁺, ground‑state Be, and excited ³P Be to acetylene (C₂H₂) and ethylene (C₂H₄) using ab initio Hartree–Fock theory. The key open questions are the equilibrium geometries and binding strengths of the resulting Be–hydrocarbon complexes.

## Approach
The calculations are performed at the self‑consistent‑field (SCF) level with double‑zeta quality Gaussian basis sets: the (9s5p/4s2p) set of Huzinaga–Dunning for carbon, the (4s/2s) set scaled by 1.2 for hydrogen, and the (9s4p/4s2p) set of Yarkony for beryllium. Restricted Hartree–Fock (RHF) is used for closed‑shell species and restricted open‑shell Hartree–Fock (ROHF) for open‑shell states. The hydrocarbon geometries are kept fixed at their experimental equilibrium values. The beryllium nucleus approaches the midpoint of the carbon–carbon bond along the perpendicular bisector, defining the reaction coordinate R. For each electronic state—²A₁ Be⁺–C₂H₂, ³B₂ Be–C₂H₂, ²A₁ Be⁺–C₂H₄, and ³B₂ Be–C₂H₄—the total SCF energy is computed at a series of R values to map the potential energy curve. The energies of the isolated fragments (Be⁺ ²S, Be ³P, C₂H₂ ¹Σ_g⁺, C₂H₄ ¹A_g) are likewise obtained. From the potential curves, equilibrium separations and dissociation energies are extracted, and a single‑point energy at a fixed distance provides an additional verification.

## Reproduction target
Compute and report the equilibrium Be–bond midpoint separation (in Å) and dissociation energy (in kcal/mol) for each of the four complexes: ²A₁ Be–C₂H₂⁺, ³B₂ Be–C₂H₂, ²A₁ Be–C₂H₄⁺, and ³B₂ Be–C₂H₄. Additionally, compute the total SCF energy (in hartree) of the ³B₂ state of Be–C₂H₂ at a fixed Be–midpoint distance of 2.0 Å. These results must be written to the specified output files: a CSV for the binding data and a plain text file for the verification energy.

## Assets

- Huzinaga-Dunning double-zeta basis for carbon (9s5p/4s2p): https://www.basissetexchange.org
- Huzinaga-Dunning double-zeta basis for hydrogen (4s/2s) scaled by 1.2: https://www.basissetexchange.org
- Yarkony double-zeta basis for beryllium (9s4p/4s2p): https://www.basissetexchange.org
- Experimental geometry of acetylene (C2H2): 10.1016/0022-2852(64)90077-3
- Experimental geometry of ethylene (C2H4): 10.1063/1.1724962
- Open-source quantum chemistry package (e.g., Psi4, PySCF, ORCA): https://pypi.org/project/pyscf/

## Workflow steps

### Step 1: Compute potential energy curves
- Role: process
- Action: Using the specified basis sets and experimental geometries, perform restricted open-shell Hartree-Fock (ROHF) or equivalent SCF calculations for the required electronic states of Be–C2H2 and Be–C2H4. Compute total energies for: (i) ²A₁ Be⁺–C₂H₂, (ii) ³B₂ Be–C₂H₂, (iii) ²A₁ Be⁺–C₂H₄, (iv) ³B₂ Be–C₂H₄ at a series of Be–midpoint distances R spanning the expected minima. Also compute energies of the isolated species: Be⁺ (²S), Be (³P), C₂H₂ (¹Σ_g⁺), and C₂H₄ (¹A_g).
- Evidence: `/app/outputs/potential_curves.csv`

### Step 2: Extract equilibrium binding data
- Role: scored (load-bearing)
- Action: From the computed potential energy curves, determine the equilibrium Be–midpoint distance R_min (Å) and dissociation energy D_e (kcal/mol) for each complex, where D_e = E_total(R_min) – [E(separated metal species) + E(separated hydrocarbon)]. Write the results to a CSV file.
- Output file: `/app/outputs/step_01_binding_data.csv`
- Format: csv
- Contract: system (str), state (str), R_min (float, Å), D_e (float, kcal/mol)
- Scoring: scored by hidden verifier

### Step 3: Verify SCF energy at a fixed point
- Role: scored (load-bearing)
- Action: Compute the total SCF energy (in hartree) for the ³B₂ state of Be–C₂H₂ at a fixed Be–midpoint distance R = 2.0 Å, using the same method and basis set. Write the value as a single float to a text file.
- Output file: `/app/outputs/step_02_verification_energy.txt`
- Format: txt
- Contract: One line containing a floating-point number (hartree).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_binding_data.csv`
- `/app/outputs/step_02_verification_energy.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_binding_data.csv
- path: `/app/outputs/step_01_binding_data.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Equilibrium Be-midpoint separation and dissociation energy for the four bound systems from Table I of the paper.
- schema:
  - `type`: table
  - `required_columns`: `system`, `state`, `R_min`, `D_e`
  - `units`:
    - `R_min`: Å
    - `D_e`: kcal/mol

### step_02_verification_energy.txt
- path: `/app/outputs/step_02_verification_energy.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Total SCF energy of the ³B₂ Be–C₂H₂ state at a fixed Be–midpoint distance of 2.0 Å.
- schema:
  - `type`: text
  - `units`: hartree

Notes: The task reproduces the key equilibrium binding results and a verification point from the ab initio SCF study. All required public resources are specified in resources.json.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_binding_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "state",
          "R_min",
          "D_e"
        ],
        "units": {
          "R_min": "Å",
          "D_e": "kcal/mol"
        }
      },
      "description": "Equilibrium Be-midpoint separation and dissociation energy for the four bound systems from Table I of the paper."
    },
    {
      "file": "step_02_verification_energy.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "units": "hartree"
      },
      "description": "Total SCF energy of the ³B₂ Be–C₂H₂ state at a fixed Be–midpoint distance of 2.0 Å."
    }
  ],
  "notes": "The task reproduces the key equilibrium binding results and a verification point from the ab initio SCF study. All required public resources are specified in resources.json."
}
```

## How you are scored
Your results are evaluated against hidden reference values by an automated verifier. The verifier compares your submitted equilibrium distances and dissociation energies to the expected values with numerical tolerances that account for legitimate methodological differences. The verification energy is compared to a reference SCF energy obtained under the same basis set and geometry. Each scored artifact carries a portion of the total reward; both must pass their respective checks to receive full credit. The reward is computed as a weighted sum of the individual scores.
