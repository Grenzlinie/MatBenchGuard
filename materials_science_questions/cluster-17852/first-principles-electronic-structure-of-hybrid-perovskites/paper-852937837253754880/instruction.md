# First-Principles Study of Spiro-MeOTAD/Perovskite Interface Binding and Charge Transfer

## Problem background
Spiro-MeOTAD is the archetypal hole transport material (HTM) used in perovskite solar cells with state-of-the-art efficiencies. The stability and performance of these devices crucially depend on the interface between the perovskite absorber and the HTM, where binding preferences and charge transfer dynamics dictate hole extraction. Hybrid organic-inorganic lead halide perovskites (LHPs) can be tuned by mixing cations and anions; the triple-cation/dual-anion stoichiometry Cs0.05(FA0.83MA0.17)0.95Pb(I0.83Br0.17)3 (triLHP) is a prominent high-efficiency variant contrasting with the simpler methylammonium lead triiodide (MAPbI3, MAPI). A first-principles understanding of how the perovskite composition and termination (AX vs PbX2) influence the binding energy of spiro-MeOTAD and the subsequent hole injection time is needed to guide further device optimization. This task will compute these interfacial properties using hybrid density functional theory.

## Approach
The work employs hybrid density functional theory (DFT) with periodic plane-wave calculations. The general workflow consists of:

- Constructing surface slab models for both MAPI and triLHP with different terminations (AX and PbX2 types, including several local compositional variants), and building an isolated spiro-MeOTAD molecule.
- Performing geometry optimizations of the isolated slabs and molecule, then of the full LHP/spiro-MeOTAD interfaces.
- Decomposing the binding energy into adhesion and distortion contributions using the energy components from the relaxed and distorted fragments (E_LHP*, E_Spiro*) according to a standard decomposition scheme.
- Calculating the Kohn-Sham orbital energies, wavefunctions, and atom-projected density of states (pDOS) of the relaxed interfaces.
- Applying the projection-operator diabatization (POD) method to compute electronic coupling matrix elements between the spiro-MeOTAD donor states (HOMO and HOMO-1) and the perovskite valence band states, thereby obtaining the spectral function and the hole injection time τ = ħ/Γ.

All calculations are carried out with publicly available plane-wave DFT codes and pseudopotentials. The final outputs are numerical tables of binding energies and hole injection times for every interface configuration.

## Reproduction target
Produce two CSV files inside /app/outputs:

1. binding_energies.csv: For each LHP/spiro-MeOTAD interface variant (combinations of perovskite composition, termination type, and local chemical environment), report the raw energy components (E_LHP/Spiro, E_LHP, E_Spiro, E_LHP*, E_Spiro*), the total binding energy Eb = E_LHP/Spiro - E_LHP - E_Spiro, the adhesion energy Ea, and the distortion energies of spiro-MeOTAD and the LHP. The file must allow independent recomputation of Eb and its decomposition.

2. hole_injection_times.csv: For each interface variant and for both the HOMO and HOMO-1 donor states, report the hole injection time τ in picoseconds, computed via the POD spectral function.

The hidden verifier will check whether the computed binding energies show a physically meaningful ordering with respect to termination and composition and whether the injection times lie in the expected picosecond range. No visualizations or processed pDOS plots are required.

## Assets

- Quantum ESPRESSO (plane-wave DFT code): https://www.quantum-espresso.org/
- SSSP pseudopotential library: https://www.pseudo-dojo.org/
- Crystal structure of MAPbI3 (MAPI)
- Composition of triple-cation perovskite triLHP
- Molecular structure of spiro-MeOTAD
- Projection-operator diabatization (POD) method reference: 10.1021/jp071852u

## Workflow steps

### Step 1: Construct atomic models
- Role: process
- Action: From public bulk structures, build (010) surface slabs for MAPI and triLHP with AX (MAI, FAMAX, CsFAMAX, CsFAMAX(O-Cs)) and PbX2 (PbI2, PbX2, PbX2(Cs)) terminations. Build the isolated spiro-MeOTAD molecule. Combine them to create all interface configurations described in the paper.
- Evidence: `/app/outputs/none`

### Step 2: Relax isolated components
- Role: process
- Action: Perform hybrid DFT geometry optimization of each isolated LHP surface slab and the isolated spiro-MeOTAD molecule. Obtain relaxed geometries and their total energies (E_LHP and E_Spiro).
- Evidence: `/app/outputs/none`

### Step 3: Relax LHP/spiro-MeOTAD interfaces
- Role: process
- Action: For each termination and composition variant, attach spiro-MeOTAD to the surface and perform full geometry optimization. Obtain relaxed interface total energies (E_LHP/Spiro) and the intermediate distorted fragment energies (E_LHP* and E_Spiro*) required for binding energy decomposition.
- Evidence: `/app/outputs/none`

### Step 4: Electronic structure calculation
- Role: process
- Action: Perform a static hybrid DFT calculation on each relaxed interface to obtain Kohn-Sham eigenvalues, wavefunctions, and atom-projected density of states (pDOS). These are needed for the subsequent charge transfer analysis.
- Evidence: `/app/outputs/none`

### Step 5: Binding energy analysis
- Role: scored (load-bearing)
- Action: From the energies obtained in steps 02 and 03, compute the binding energy Eb = E_LHP/Spiro - E_LHP - E_Spiro, the adhesion energy Ea = E_LHP/Spiro - E_LHP_star - E_Spiro_star, the distortion energy of spiro-MeOTAD Ed_spiro = E_Spiro_star - E_Spiro, and the distortion energy of LHP Ed_lhp = E_LHP_star - E_LHP. Write the results for every interface to binding_energies.csv.
- Output file: `/app/outputs/binding_energies.csv`
- Format: csv
- Contract: interface:string, termination:string, composition:string, E_LHP_Spiro:float, E_LHP:float, E_Spiro:float, E_LHP_star:float, E_Spiro_star:float, Eb:float, Ea:float, Ed_spiro:float, Ed_lhp:float
- Scoring: scored by hidden verifier

### Step 6: Charge transfer coupling and injection time analysis
- Role: scored
- Action: Using the wavefunctions from step 04, apply the projection-operator diabatization (POD) method. Compute the electronic coupling matrix elements between spiro-MeOTAD donor states (HOMO, HOMO-1) and LHP valence band states. Compute the spectral function Γ(E) and the hole injection times τ = ħ/Γ for both donor channels on every interface. Write the results to hole_injection_times.csv.
- Output file: `/app/outputs/hole_injection_times.csv`
- Format: csv
- Contract: interface:string, donor_state:string, tau_ps:float
- Scoring: scored by hidden verifier

## Interface naming convention

Use the exact interface identifier strings as listed below for the `interface` column in both CSV output files.

| Identifier | Description |
|---|---|
| MAPI_MAI | MAPI with MAI (AX) termination |
| MAPI_PbI2 | MAPI with PbI2 (PbX2) termination |
| triLHP_FAMAX | triLHP with FAMAX (AX) termination (no Cs exposed) |
| triLHP_CsFAMAX | triLHP with CsFAMAX (AX) termination |
| triLHP_CsFAMAX_OCs | triLHP with CsFAMAX(O-Cs) (AX) termination |
| triLHP_PbX2 | triLHP with PbX2 (PbX2) termination (no Cs subsurface) |
| triLHP_PbX2_Cs | triLHP with PbX2(Cs) (PbX2) termination |

The hidden checker will match on these exact strings; any deviation will cause a score of zero.

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binding_energies.csv`
- `/app/outputs/hole_injection_times.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binding_energies.csv
- path: `/app/outputs/binding_energies.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Binding energy decomposition for each interface variant, including raw energy components from DFT calculations. The 'interface' column must use exactly one of the listed interface_values to pass hidden checks.
- schema:
  - `type`: table
  - `required_columns`: `interface`, `termination`, `composition`, `E_LHP_Spiro`, `E_LHP`, `E_Spiro`, `E_LHP_star`, `E_Spiro_star`, `Eb`, `Ea`, `Ed_spiro`, `Ed_lhp`
  - `units`:
    - `E_LHP_Spiro`: eV
    - `E_LHP`: eV
    - `E_Spiro`: eV
    - `E_LHP_star`: eV
    - `E_Spiro_star`: eV
    - `Eb`: eV
    - `Ea`: eV
    - `Ed_spiro`: eV
    - `Ed_lhp`: eV
  - `interface_values`: `MAPI_MAI`, `MAPI_PbI2`, `triLHP_FAMAX`, `triLHP_CsFAMAX`, `triLHP_CsFAMAX_OCs`, `triLHP_PbX2`, `triLHP_PbX2_Cs`

### hole_injection_times.csv
- path: `/app/outputs/hole_injection_times.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Hole injection times computed via POD analysis for each interface and donor state (HOMO, HOMO-1). The 'interface' column must use exactly one of the listed interface_values to match hidden reference checks.
- schema:
  - `type`: table
  - `required_columns`: `interface`, `donor_state`, `tau_ps`
  - `units`:
    - `tau_ps`: ps
  - `interface_values`: `MAPI_MAI`, `MAPI_PbI2`, `triLHP_FAMAX`, `triLHP_CsFAMAX`, `triLHP_CsFAMAX_OCs`, `triLHP_PbX2`, `triLHP_PbX2_Cs`

Notes: Binding energy CSV must allow recomputation of Eb and decomposition. Hole injection times must be in picoseconds. Both CSV files must use the exact interface identifier strings specified in the interface_values list; the hidden verifier matches on these exact strings.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binding_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "interface",
          "termination",
          "composition",
          "E_LHP_Spiro",
          "E_LHP",
          "E_Spiro",
          "E_LHP_star",
          "E_Spiro_star",
          "Eb",
          "Ea",
          "Ed_spiro",
          "Ed_lhp"
        ],
        "units": {
          "E_LHP_Spiro": "eV",
          "E_LHP": "eV",
          "E_Spiro": "eV",
          "E_LHP_star": "eV",
          "E_Spiro_star": "eV",
          "Eb": "eV",
          "Ea": "eV",
          "Ed_spiro": "eV",
          "Ed_lhp": "eV"
        },
        "interface_values": [
          "MAPI_MAI",
          "MAPI_PbI2",
          "triLHP_FAMAX",
          "triLHP_CsFAMAX",
          "triLHP_CsFAMAX_OCs",
          "triLHP_PbX2",
          "triLHP_PbX2_Cs"
        ]
      },
      "description": "Binding energy decomposition for each interface variant, including raw energy components from DFT calculations. The 'interface' column must use exactly one of the listed interface_values to pass hidden checks."
    },
    {
      "file": "hole_injection_times.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "interface",
          "donor_state",
          "tau_ps"
        ],
        "units": {
          "tau_ps": "ps"
        },
        "interface_values": [
          "MAPI_MAI",
          "MAPI_PbI2",
          "triLHP_FAMAX",
          "triLHP_CsFAMAX",
          "triLHP_CsFAMAX_OCs",
          "triLHP_PbX2",
          "triLHP_PbX2_Cs"
        ]
      },
      "description": "Hole injection times computed via POD analysis for each interface and donor state (HOMO, HOMO-1). The 'interface' column must use exactly one of the listed interface_values to match hidden reference checks."
    }
  ],
  "notes": "Binding energy CSV must allow recomputation of Eb and decomposition. Hole injection times must be in picoseconds. Both CSV files must use the exact interface identifier strings specified in the interface_values list; the hidden verifier matches on these exact strings."
}
```

## How you are scored
Your submission is evaluated by an automated hidden checker that inspects the two CSV files. The checker will verify that:

- The binding energies for the different terminations and compositions follow the expected relative trends.
- The hole injection times are within a physically plausible range and that the fastest channels are correctly identified.
- The raw energy components in binding_energies.csv are internally consistent, i.e., the decomposition into Eb, Ea, Ed_spiro, Ed_lhp can be recomputed from the provided raw energies.

Each of these checks carries a weight, and the final reward (a float between 0 and 1) combines them. The tolerances account for the fact that different DFT implementations, pseudopotentials, and numerical settings can lead to small numerical variations. Your task is to faithfully execute the computational workflow; reporting the paper's numbers without having run the calculations will not pass the consistency checks.
