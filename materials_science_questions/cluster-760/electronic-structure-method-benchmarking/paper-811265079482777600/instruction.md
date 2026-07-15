# Electronic structure and bond dissociation energies of NHC–first-row transition metal complexes

## Problem background
N-heterocyclic carbenes (NHCs) are prominent σ-donor ligands in organometallic chemistry and catalysis. When a free NHC interacts with a bare first-row transition metal (TM), it can form a σ-type complex where the carbene carbon donates its lone pair into empty metal orbitals. The strength of this NHC–TM bond, quantified by the bond dissociation energy (BDE), is expected to vary systematically with the d-electron count of the metal, potentially leading to a structured BDE profile across the periodic series. Understanding how the electronic structure of the NHC and the metal’s d-configuration govern the stability of these σ‑type complexes is central for rational ligand design. This task investigates the electronic properties of the imidazole-derived NHC and computes the bond dissociation energies of its σ‑type complexes with all first-row transition metals (Sc–Zn).

## Approach
The free NHC is first optimized at the B3LYP/6-311+G(d,p) level to obtain its ground-state geometry and frontier orbital energies. A CASSCF calculation with an active space of (12,10) and the 6-31G* basis set is then performed to determine the relative energies of the low-lying ³B₁ and ¹B₁ states above the singlet ground state. For each transition metal atom (Sc through Zn), atomic energies are computed at the B3LYP and CCSD(T) levels using the LanL2TZ basis with f polarization functions. Next, σ‑type [NHC–TM] complexes are built and fully optimized at the B3LYP level (LanL2TZ(f) for TM, 6-311+G(d,p) for other atoms), and the stationary points are verified by frequency calculations. Single‑point CCSD(T) energies are then obtained for each optimized geometry. Bond dissociation energies are derived at both B3LYP and CCSD(T) levels from the energy differences between the complex and its dissociation products (free NHC + free TM atom). This workflow yields the key electronic descriptors of the free NHC and the BDEs across the complete first‑row TM series.

## Reproduction target
Produce the following two scored artifacts:
1. `nhc_properties.json`: a JSON file containing the B3LYP HOMO–LUMO gap (in kcal mol⁻¹) of the free NHC, and the CASSCF(12,10)/6-31G* relative energies (in kcal mol⁻¹) of the ³B₁ and ¹B₁ states with respect to the ground state.
2. `sigma_bde.csv`: a CSV table with columns `TM` (element symbol), `multiplicity_gs` (integer ground-state spin multiplicity of the complex), `BDE_B3LYP` and `BDE_CCSDT` (both in kcal mol⁻¹), listing the computed bond dissociation energies for the σ‑type [NHC–TM] complexes for every metal from Sc to Zn. Include Zn even if only a π‑type structure is located, as in the original study. The hidden verifier will check the numerical values and the overall trend of the BDE series.

## Assets

- Quantum chemistry package (ORCA or PySCF): https://orcaforum.kofo.mpg.de/ or https://pyscf.org/
- Basis sets: 6-311+G(d,p), 6-31G*, LanL2TZ(f) for transition metals: https://www.basissetexchange.org/

## Workflow steps

### Step 1: DFT optimization of free NHC
- Role: process
- Action: Construct an initial geometry for the imidazole-derived NHC (R=H, singlet) and perform a geometry optimization at the B3LYP level using a suitable basis set (e.g., 6-311+G(d,p)). Record the optimized total energy and frontier orbital energies (HOMO, LUMO) in a log file.
- Evidence: `/app/outputs/nhc_dft.log`

### Step 2: CASSCF calculation on free NHC
- Role: process
- Action: Using the optimized geometry of the free NHC, perform a CASSCF calculation with an active space of (12,10) and a suitable basis set (e.g., 6-31G*) to obtain the relative energies (in kcal/mol) of the low-lying ³B₁ and ¹B₁ states with respect to the ground ¹A₁ state.
- Evidence: `/app/outputs/casscf.log`

### Step 3: Compute free transition metal atomic energies
- Role: process
- Action: For each transition metal atom (Sc, Ti, V, Cr, Mn, Fe, Co, Ni, Cu, Zn) in its ground-state electronic configuration, compute the total energy at the B3LYP level using the LanL2TZ(f) basis set for TM and at the CCSD(T) level (single-point) with the same basis. Store the energies in a structured file.
- Evidence: `/app/outputs/free_tm_energies.csv`

### Step 4: Optimize σ-type [NHC–TM] complexes
- Role: process
- Action: For each TM (Sc–Zn), build a starting geometry with TM bound to the carbene carbon and perform a full geometry optimization at the B3LYP level using LanL2TZ(f) for TM and 6-311+G(d,p) for other atoms. Verify the nature of the stationary point via frequency calculation. Record the total energy and spin multiplicity. If no σ-type structure can be located for Zn, use the energy of the located π-type structure as done in the original study.
- Evidence: `/app/outputs/sigma_opt_energies.csv`

### Step 5: CCSD(T) single-point energy calculations
- Role: process
- Action: For each optimized complex from the previous step, perform a single-point CCSD(T) calculation with the same basis sets (LanL2TZ(f) for TM, 6-311+G(d,p) for others) to obtain the higher-level total energy.
- Evidence: `/app/outputs/ccsdt_energies.csv`

### Step 6: Output free NHC properties
- Role: scored
- Action: Compile the following computed quantities into a JSON file: the B3LYP HOMO–LUMO gap (in kcal/mol); the CASSCF relative energies of the ³B₁ and ¹B₁ states (in kcal/mol) with respect to the ground state.
- Output file: `/app/outputs/nhc_properties.json`
- Format: json
- Contract: {"homo_lumo_gap_kcal_mol": float, "casscf_b3b1_energy_kcal_mol": float, "casscf_b1b1_energy_kcal_mol": float}
- Scoring: scored by hidden verifier

### Step 7: Output σ‑type BDEs
- Role: scored (load-bearing)
- Action: For each TM (Sc–Zn), compute the bond dissociation energy (BDE) at the B3LYP level using BDE = E(NHC, DFT) + E(TM, DFT) – E(complex, DFT), and at the CCSD(T) level using BDE = E(NHC, DFT) + E(TM, CCSD(T)) – E(complex, CCSD(T)), with total energies from the preceding steps. Write a CSV with columns: TM (element symbol), multiplicity_gs (integer ground-state multiplicity of the complex), BDE_B3LYP (kcal/mol), BDE_CCSDT (kcal/mol). Use the energy values of the structure obtained for Zn (even if it is π‑type).
- Output file: `/app/outputs/sigma_bde.csv`
- Format: csv
- Contract: Columns: TM (str), multiplicity_gs (int), BDE_B3LYP (float, kcal/mol), BDE_CCSDT (float, kcal/mol). One row per TM from Sc to Zn.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/nhc_properties.json`
- `/app/outputs/sigma_bde.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### nhc_properties.json
- path: `/app/outputs/nhc_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed electronic properties of the free NHC (HOMO-LUMO gap from B3LYP and CASSCF relative energies).
- schema:
  - `type`: object
  - `required`: `homo_lumo_gap_kcal_mol`, `casscf_b3b1_energy_kcal_mol`, `casscf_b1b1_energy_kcal_mol`
  - `properties`:
    - `homo_lumo_gap_kcal_mol`:
      - `type`: number
      - `description`: HOMO-LUMO gap (kcal/mol) from B3LYP/6-311+G(d,p)
    - `casscf_b3b1_energy_kcal_mol`:
      - `type`: number
      - `description`: CASSCF(12,10)/6-31G* relative energy of the ³B₁ state (kcal/mol) above the ¹A₁ ground state
    - `casscf_b1b1_energy_kcal_mol`:
      - `type`: number
      - `description`: CASSCF(12,10)/6-31G* relative energy of the ¹B₁ state (kcal/mol) above the ¹A₁ ground state

### sigma_bde.csv
- path: `/app/outputs/sigma_bde.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed bond dissociation energies (BDEs) for σ‑type [NHC–TM] complexes across first‑row transition metals (Sc–Zn). BDE_B3LYP and BDE_CCSDT are in kcal/mol.
- schema:
  - `type`: table
  - `required_columns`: `TM`, `multiplicity_gs`, `BDE_B3LYP`, `BDE_CCSDT`
  - `columns`:
    - `TM`: string
    - `multiplicity_gs`: integer
    - `BDE_B3LYP`: number
    - `BDE_CCSDT`: number

Notes: The agent must produce the two scored files from the preceding process steps. The hidden checker will compare the reported values against the paper’s published reference results with tolerances that absorb method-dependent spread but are tight enough to exclude a trivial guess.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "nhc_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "homo_lumo_gap_kcal_mol",
          "casscf_b3b1_energy_kcal_mol",
          "casscf_b1b1_energy_kcal_mol"
        ],
        "properties": {
          "homo_lumo_gap_kcal_mol": {
            "type": "number",
            "description": "HOMO-LUMO gap (kcal/mol) from B3LYP/6-311+G(d,p)"
          },
          "casscf_b3b1_energy_kcal_mol": {
            "type": "number",
            "description": "CASSCF(12,10)/6-31G* relative energy of the ³B₁ state (kcal/mol) above the ¹A₁ ground state"
          },
          "casscf_b1b1_energy_kcal_mol": {
            "type": "number",
            "description": "CASSCF(12,10)/6-31G* relative energy of the ¹B₁ state (kcal/mol) above the ¹A₁ ground state"
          }
        }
      },
      "description": "Computed electronic properties of the free NHC (HOMO-LUMO gap from B3LYP and CASSCF relative energies)."
    },
    {
      "file": "sigma_bde.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "TM",
          "multiplicity_gs",
          "BDE_B3LYP",
          "BDE_CCSDT"
        ],
        "columns": {
          "TM": "string",
          "multiplicity_gs": "integer",
          "BDE_B3LYP": "number",
          "BDE_CCSDT": "number"
        }
      },
      "description": "Computed bond dissociation energies (BDEs) for σ‑type [NHC–TM] complexes across first‑row transition metals (Sc–Zn). BDE_B3LYP and BDE_CCSDT are in kcal/mol."
    }
  ],
  "notes": "The agent must produce the two scored files from the preceding process steps. The hidden checker will compare the reported values against the paper’s published reference results with tolerances that absorb method-dependent spread but are tight enough to exclude a trivial guess."
}
```

## How you are scored
A hidden verifier will read your submitted `nhc_properties.json` and `sigma_bde.csv` and compare them against reference values derived from the original study. Scoring is split across the two artifacts: the free NHC properties contribute a moderate share of the total reward, while the computed BDE values for the metal series carry the larger weight. For each numeric property, the verifier uses tolerance‑based comparison to judge correctness, and additionally confirms that the BDEs across the Sc–Zn series exhibit the expected overall structure (e.g., a double‑peak profile). The final reward is a weighted sum, ranging from 0.0 to 1.0, with full credit given when all quantities fall within expected tolerances and the BDE trend is correctly reproduced.
