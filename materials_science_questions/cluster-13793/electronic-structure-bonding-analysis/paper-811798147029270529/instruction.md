# Work of Separation Decomposition for Pt/Graphene Interface Adhesion with Metal Adatoms

## Problem background
Polymer electrolyte membrane fuel cells suffer from a gradual loss of electrochemical active area, partly because Pt catalyst particles detach and agglomerate on the carbon support. One approach to mitigate this degradation is to introduce a metallic adatom between the Pt and carbon phases to enhance interface adhesion. First-principles calculations based on density functional theory (DFT) can quantify how different metallic adatoms influence the strength of a Pt(111)/graphene interface by computing the reversible work required to separate the layers (work of separation) and by analyzing the redistribution of electronic charge (charge transfer). This reproduction task targets these two quantities—work of separation and charge transfer—for a set of four metallic adatoms (Co, Ni, V, Ti) and for the adatom-free Pt/graphene interface.

## Approach
The workflow follows a multi-step first-principles protocol. The key idea is to construct atomic models for the Pt(111) slab, a graphene sheet, the isolated adatom-on-slab and adatom-on-graphene subsystems, and the full Pt/graphene interface both with and without an adatom. After full structural relaxations with spin-polarized GGA-level DFT, the total energies of all these systems are collected. The work of separation is decomposed into two independent channels—cleaving the interface at the Pt–adatom bond or at the carbon–adatom bond—by comparing the energy of the intact interface with the energies of the separated fragments. In a parallel analysis, Bader charge partitioning is applied to the relaxed interface charge densities to obtain the amount of electronic charge that each adatom donates to the Pt side and to the carbon side. This combination yields a quantitative measure of adhesion enhancement and of the adatom’s role as an electronic bridge across the interface.

## Reproduction target
Produce two tabular artifacts under `/app/outputs`:

1. `work_of_separation.csv` – columns `adatom` (string), `W_sep_Pt_X` (float, J/m^2), `W_sep_C_X` (float, J/m^2). It must contain one row for the pristine Pt/graphene interface (adatom = `None`) and one row for each adatom: `Co`, `Ni`, `V`, `Ti`.

2. `charge_transfer.csv` – columns `adatom` (string), `charge_to_Pt` (float, elementary charge |e|), `charge_to_C` (float, elementary charge |e|). It must likewise include a row for the pristine interface (zero charge transfer) and a row for each of the four adatoms.

The hidden verifier will examine these files and judge the reproduction against the quantitative claims of the original study. The evaluation focuses on whether the reported values satisfy the physically expected structural relationships that the paper identified, using appropriate numerical tolerances.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials (efficiency): https://www.materialscloud.org/discover/sssp/table/efficiency
- Bader charge analysis code: http://theory.cm.utexas.edu/henkelman/code/bader/
- Atomic Simulation Environment (ASE): ase

## Workflow steps

### Step 1: Build interface models
- Role: process
- Action: Construct atomic models for all required systems: 6-layer Pt(111) slab (3 atoms per layer), 2×2 graphene supercell, Pt slab with adatom X at hollow site (X = Co, Ni, V, Ti), graphene with adatom X at hollow site, pristine Pt/graphene interface, and Pt/graphene+X interfaces with adatom placed between hollow site of graphene and top site of Pt using registry (111)[1̄21]Pt || (0001)[01̄0]C. Set in-plane dimensions to approximately match (Pt ~4.87 Å, graphene ~4.92 Å; 1% strain accepted) and add 15 Å vacuum in the z-direction.
- Evidence: `/app/outputs/model_structures.json`

### Step 2: DFT total-energy calculations
- Role: process
- Action: Perform spin-polarized DFT geometry relaxations using PAW-PBE (or an equivalent GGA functional) for all systems from step1. Use a k-point grid equivalent to 10×10×1 and a plane-wave cutoff equivalent to 500 eV. Converge forces to <0.05 eV/Å and electronic self-consistency to 10⁻⁵ eV. Record the final relaxed total energies: E_Pt, E_Pt+X (for each X), E_graphene, E_graphene+X, E_Pt/graphene (pristine), and E_Pt/graphene+X.
- Evidence: `/app/outputs/dft_total_energies.json`

### Step 3: Work of separation calculation
- Role: scored (load-bearing)
- Action: Using the total energies from step2 and the interface area A (the xy cross-sectional area of the supercell), compute W_sep^Pt-X and W_sep^C-X according to the two-channel decomposition (energetics of breaking Pt-X bond and C-X bond) for each adatom. Also compute the reference W_sep for the pristine Pt/graphene interface. Write the results to work_of_separation.csv with one row per system; include a row with adatom='None' for the pure interface.
- Output file: `/app/outputs/work_of_separation.csv`
- Format: csv
- Contract: Columns: adatom (str), W_sep_Pt_X (float, J/m^2), W_sep_C_X (float, J/m^2).
- Scoring: scored by hidden verifier

### Step 4: Bader charge analysis
- Role: scored (load-bearing)
- Action: Perform Bader charge analysis on the relaxed charge densities of the Pt/graphene+X interfaces and the pristine interface (from step2). For each system, compute the charge transferred from the adatom to the Pt slab (total Bader charge on Pt minus the charge of the isolated Pt slab) and to the graphene (total on C minus isolated graphene), in units of elementary charge |e|. Write the results to charge_transfer.csv with rows for each adatom and a row for 'None' (pure interface, charge transfer zero).
- Output file: `/app/outputs/charge_transfer.csv`
- Format: csv
- Contract: Columns: adatom (str), charge_to_Pt (float, |e|), charge_to_C (float, |e|).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/work_of_separation.csv`
- `/app/outputs/charge_transfer.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### work_of_separation.csv
- path: `/app/outputs/work_of_separation.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: CSV file with columns: adatom (e.g., 'Co','Ni','V','Ti','None'), W_sep_Pt_X (float, J/m^2), W_sep_C_X (float, J/m^2).
- schema:
  - `type`: table
  - `required_columns`: `adatom`, `W_sep_Pt_X`, `W_sep_C_X`
  - `units`:
    - `W_sep_Pt_X`: J/m^2
    - `W_sep_C_X`: J/m^2

### charge_transfer.csv
- path: `/app/outputs/charge_transfer.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: CSV file with columns: adatom (str), charge_to_Pt (float, elementary charge units), charge_to_C (float, elementary charge units).
- schema:
  - `type`: table
  - `required_columns`: `adatom`, `charge_to_Pt`, `charge_to_C`
  - `units`:
    - `charge_to_Pt`: |e|
    - `charge_to_C`: |e|

Notes: The hidden checker verifies relative trends: W_sep_Pt_X > W_sep_C_X for every adatom; for 'None' both W_sep values near zero; the maximum W_sep_C_X among Co, Ni, V is at least 0.4 J/m^2; charge transfer ratios and that Ti exhibits the highest W_sep_Pt_X and highest charge_to_Pt.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "work_of_separation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "adatom",
          "W_sep_Pt_X",
          "W_sep_C_X"
        ],
        "units": {
          "W_sep_Pt_X": "J/m^2",
          "W_sep_C_X": "J/m^2"
        }
      },
      "description": "CSV file with columns: adatom (e.g., 'Co','Ni','V','Ti','None'), W_sep_Pt_X (float, J/m^2), W_sep_C_X (float, J/m^2)."
    },
    {
      "file": "charge_transfer.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "adatom",
          "charge_to_Pt",
          "charge_to_C"
        ],
        "units": {
          "charge_to_Pt": "|e|",
          "charge_to_C": "|e|"
        }
      },
      "description": "CSV file with columns: adatom (str), charge_to_Pt (float, elementary charge units), charge_to_C (float, elementary charge units)."
    }
  ],
  "notes": "The hidden checker verifies relative trends: W_sep_Pt_X > W_sep_C_X for every adatom; for 'None' both W_sep values near zero; the maximum W_sep_C_X among Co, Ni, V is at least 0.4 J/m^2; charge transfer ratios and that Ti exhibits the highest W_sep_Pt_X and highest charge_to_Pt."
}
```

## How you are scored
A hidden verifier reads `work_of_separation.csv` and `charge_transfer.csv` and computes a reward in [0,1] by independently weighting each artifact according to a predefined rubric. The scoring is based on how well the submitted values align with the paper’s reported trends and threshold criteria, not on reproducing an exact numerical match. Presenting the paper’s original numbers without executing the DFT workflow will not pass the audit: the verifier checks for internal consistency and for the expected quantitative relationships among the computed quantities. The detailed scoring criteria and tolerances are kept secret, but they are derived directly from the physical findings of the original work.
