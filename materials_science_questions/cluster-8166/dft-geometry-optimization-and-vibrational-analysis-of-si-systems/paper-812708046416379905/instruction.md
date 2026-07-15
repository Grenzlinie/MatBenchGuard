# DFT and VB Analysis of Silabicyclobutane Bond Stretch Isomerism

## Problem background
Silicon analogues of bicyclo[1.1.0]butanes can exhibit bond stretch isomerism, where the central bridge Si–Si bond can exist in two distinct geometries: a short-bond isomer with a typical σ-bond arrangement and a long-bond isomer in which the bridgehead silicon atoms become inverted so that all bonds lie on the same hemisphere. This inverted geometry is known as an inverted σ bond and the bonding nature of such a bond is not fully understood. Using valence bond theory, it is possible to decompose the interaction energy between the bridgehead silicon atoms into a covalent component and a charge-shift resonance energy, and thereby classify the bond as covalent or charge-shift. The central question is how the bond type depends on the geometric parameters—specifically the bridge Si–Si bond length and the inversion angle α (the angle between a Si–H bond and the X–Si–X plane)—and whether the geometry inversion or the bond elongation is the primary factor that switches the bonding nature from covalent to charge-shift. Your task is to reproduce the computational workflow that answers this question for compounds 1 (X=CH₂) and 2 (X=SiH₂).

## Approach
You will investigate the bonding in silabicyclo[1.1.0]butanes using a two-stage computational protocol. First, carry out DFT geometry optimizations at the PBE0/6-31G(d) level to locate the short-bond (sb), transition-state (ts), and long-bond (lb) structures for both compounds, enforcing C₂ᵥ symmetry throughout. From each optimized structure extract the bridge Si–Si bond length r_Si–Si and the inversion angle α. Second, perform single-point valence bond calculations at the SL-BOVB/6-31G(d) level on every stationary point, treating only the bridge Si–Si bond at the breathing-orbital VB level. Decompose the in‑situ interaction energy D_in_situ into its covalent (D_COV) and charge-shift resonance (RE_CS) contributions, compute the percentage %RE_CS = 100 × RE_CS / D_in_situ, and classify the bond as covalent (COV) when %RE_CS < 50 % or charge-shift (CS) otherwise. Finally, to separate the influence of geometry inversion from that of bond elongation, perform a series of SL-BOVB calculations for compound 1 in which the bridge Si–Si bond length is held fixed at 2.395 Å while the angle α is varied from +30° to −70° in at least 10 steps, still preserving C₂ᵥ symmetry. At each point you will collect D_in_situ, D_COV, and RE_CS to reveal how the bonding energy components evolve with the inversion angle.

## Reproduction target
Produce the three output files listed in the Workflow steps:

1.  A CSV containing the optimized bridge Si–Si bond length r_Si–Si (in Å) and the inversion angle α (in degrees) for the six stationary points: 1‑sb, 1‑ts, 1‑lb, 2‑sb, 2‑ts, and 2‑lb.
2.  A CSV with the SL-BOVB energy decomposition and bond type for each of those six structures. Columns must include D_in_situ, D_COV, RE_CS (all in kJ mol⁻¹), %RE_CS (in percent), and the classified bond type (COV or CS).
3.  A CSV from the α‑scan experiment on compound 1, with at least 10 points covering α from +30° to −70° at fixed r_Si–Si = 2.395 Å, reporting D_in_situ, D_COV, and RE_CS (kJ mol⁻¹) for each α. The results should demonstrate that RE_CS rises monotonically as α becomes more negative, while D_COV passes through a maximum in the region around planar or slightly negative α, indicating that geometry inversion—rather than bond elongation—is the dominant factor that drives the switch from covalent to charge-shift bonding.

## Assets

- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de
- XMVB Valence Bond software: https://xmyb.com

## Workflow steps

### Step 1: DFT Optimization of Silabicyclobutane Isomers and TS
- Role: scored
- Action: Perform PBE0/6-31G(d) geometry optimization for compounds 1-sb, 1-ts, 1-lb, 2-sb, 2-ts, 2-lb, enforcing C2v symmetry. Extract the bridge Si–Si bond length r_Si-Si (Å) and the inversion angle α (degrees), defined as the angle between a Si–H bond and the X–Si–X plane.
- Output file: `/app/outputs/step_01_optimized_geometries.csv`
- Format: csv
- Contract: system, r_Si-Si (Å), alpha_degrees
- Scoring: scored by hidden verifier

### Step 2: VB Bond Energy Decomposition on Stationary Points
- Role: scored
- Action: Using the optimized geometries from step 01, perform SL-BOVB/6-31G(d) single-point calculations treating only the bridge Si–Si bond at the BOVB level. Extract D_in_situ, D_COV, and RE_CS in kJ/mol; compute %RE_CS = 100 * (RE_CS / D_in_situ). Classify the bond as covalent (COV) if %RE_CS < 50% and charge-shift (CS) otherwise.
- Output file: `/app/outputs/step_02_vb_energies.csv`
- Format: csv
- Contract: system, D_in_situ (kJ/mol), D_COV (kJ/mol), RE_CS (kJ/mol), pct_RE_CS (%), bond_type (COV or CS)
- Scoring: scored by hidden verifier

### Step 3: Alpha-Scan VB Energy Decomposition (Compound 1)
- Role: scored (load-bearing)
- Action: For compound 1, generate a set of geometries with the bridge Si–Si bond length fixed at 2.395 Å and the angle α varying from +30° to −70° in at least 10 steps while preserving C2v symmetry. For each geometry, run a SL-BOVB/6-31G(d) single-point calculation and collect D_in_situ, D_COV, and RE_CS in kJ/mol.
- Output file: `/app/outputs/step_03_alpha_scan.csv`
- Format: csv
- Contract: alpha_degrees, D_in_situ (kJ/mol), D_COV (kJ/mol), RE_CS (kJ/mol)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_optimized_geometries.csv`
- `/app/outputs/step_02_vb_energies.csv`
- `/app/outputs/step_03_alpha_scan.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_optimized_geometries.csv
- path: `/app/outputs/step_01_optimized_geometries.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Optimized bridge Si-Si bond lengths and inversion angles for six stationary point structures (1-sb, 1-ts, 1-lb, 2-sb, 2-ts, 2-lb).
- schema:
  - `type`: table
  - `required_columns`: `system`, `r_Si-Si`, `alpha_degrees`
  - `units`:
    - `r_Si-Si`: Å
    - `alpha_degrees`: degrees

### step_02_vb_energies.csv
- path: `/app/outputs/step_02_vb_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: SL-BOVB energy decomposition (D_in_situ, D_COV, RE_CS, %RE_CS) and bond type classification for each stationary point.
- schema:
  - `type`: table
  - `required_columns`: `system`, `D_in_situ`, `D_COV`, `RE_CS`, `pct_RE_CS`, `bond_type`
  - `units`:
    - `D_in_situ`: kJ/mol
    - `D_COV`: kJ/mol
    - `RE_CS`: kJ/mol
    - `pct_RE_CS`: %

### step_03_alpha_scan.csv
- path: `/app/outputs/step_03_alpha_scan.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: VB energy decomposition at fixed r_Si-Si=2.395 Å as a function of the geometry inversion angle α, used to demonstrate that RE_CS increases monotonically with inversion while D_COV peaks near slightly negative α.
- schema:
  - `type`: table
  - `required_columns`: `alpha_degrees`, `D_in_situ`, `D_COV`, `RE_CS`
  - `units`:
    - `D_in_situ`: kJ/mol
    - `D_COV`: kJ/mol
    - `RE_CS`: kJ/mol

Notes: All energies in kJ/mol. The bond type classification in step_02 uses the convention: COV if %RE_CS < 50%, CS otherwise. Step_03 α scan points must span +30° to −70° with at least 10 points.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_optimized_geometries.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "r_Si-Si",
          "alpha_degrees"
        ],
        "units": {
          "r_Si-Si": "Å",
          "alpha_degrees": "degrees"
        }
      },
      "description": "Optimized bridge Si-Si bond lengths and inversion angles for six stationary point structures (1-sb, 1-ts, 1-lb, 2-sb, 2-ts, 2-lb)."
    },
    {
      "file": "step_02_vb_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "D_in_situ",
          "D_COV",
          "RE_CS",
          "pct_RE_CS",
          "bond_type"
        ],
        "units": {
          "D_in_situ": "kJ/mol",
          "D_COV": "kJ/mol",
          "RE_CS": "kJ/mol",
          "pct_RE_CS": "%"
        }
      },
      "description": "SL-BOVB energy decomposition (D_in_situ, D_COV, RE_CS, %RE_CS) and bond type classification for each stationary point."
    },
    {
      "file": "step_03_alpha_scan.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "alpha_degrees",
          "D_in_situ",
          "D_COV",
          "RE_CS"
        ],
        "units": {
          "D_in_situ": "kJ/mol",
          "D_COV": "kJ/mol",
          "RE_CS": "kJ/mol"
        }
      },
      "description": "VB energy decomposition at fixed r_Si-Si=2.395 Å as a function of the geometry inversion angle α, used to demonstrate that RE_CS increases monotonically with inversion while D_COV peaks near slightly negative α."
    }
  ],
  "notes": "All energies in kJ/mol. The bond type classification in step_02 uses the convention: COV if %RE_CS < 50%, CS otherwise. Step_03 α scan points must span +30° to −70° with at least 10 points."
}
```

## How you are scored
A hidden verifier will independently assess each of the three output files. For the geometry table (step 1) and the stationary‑point VB table (step 2), your reported values will be compared against hidden reference values that correspond to the expected results at the PBE0/6‑31G(d) and SL‑BOVB/6‑31G(d) levels of theory; the comparison uses tolerances that account for legitimate toolchain spread. For the α‑scan table (step 3), the verifier will check that RE_CS increases monotonically as α decreases and that D_COV exhibits a maximum within a prescribed range, thus confirming the structural trends that underlie the main claim. The final reward is a weighted combination of the scores from the three stages. Simply copying published numbers is not enough—you must run the actual computations and output the resulting artifacts.
