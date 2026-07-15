# DFT+U and SOC Study of Magnetic Interactions and Orbital Moment in Sr2NiIrO6 Double Perovskite

## Problem background
The double perovskite Sr2NiIrO6 contains magnetic Ni2+ and Ir6+ ions arranged in a rock-salt ordered structure with two interpenetrating fcc sublattices. According to the nearest-neighbor superexchange rules, the Ni2+ (t2g6 eg2, S=1) and Ir6+ (t2g3, S=3/2) ions should couple ferromagnetically, leading to a ferromagnetic ground state. However, experimental measurements show that the material orders antiferromagnetically at low temperature, suggesting that longer-range interactions play a decisive role. This task reproduces first-principles density functional theory (DFT) calculations that investigate the magnetic couplings in Sr2NiIrO6 and related compounds, aiming to quantify the competing exchange interactions and to assess the influence of spin-orbit coupling (SOC) on the Ir orbital magnetism.

## Approach
The approach uses spin-polarized DFT within the local spin density approximation plus Hubbard U (LSDA+U) to compute the total energies of several collinear magnetic configurations. To isolate the individual exchange interactions, calculations are performed not only on the real compounds Sr2NiIrO6 and Sr2ZnIrO6, but also on artificial substitutional models: Sr2Zn(Ni)IrO6 (to extract Ir–Ir couplings) and La2NiSiO6 (to extract Ni–Ni couplings). For each system, total energies are obtained for the ferromagnetic (FM), G-type antiferromagnetic (G-AF), layered antiferromagnetic, and bilayered antiferromagnetic states. From the energy differences, the nearest-neighbor Ni–Ir coupling, the second-nearest-neighbor Ir–Ir and Ni–Ni couplings, and the third-nearest-neighbor Ir–Ir coupling can be derived. The role of SOC is examined by projecting the Ir 5d density of states onto the |J=3/2> and |J=1/2> basis for different Ir coordination environments, and by computing the Ir orbital magnetic moment in Sr2NiIrO6 through a self-consistent LSDA+U+SOC calculation. An open-source DFT code supporting LSDA+U+SOC (e.g., Quantum ESPRESSO) is used, with appropriate Hubbard U and Hund's J parameters for Ni 3d and Ir 5d electrons.

## Reproduction target
1. Perform LSDA+U calculations for the four systems (Sr2NiIrO6, Sr2Zn(Ni)IrO6, La2NiSiO6, and the real Sr2ZnIrO6) in the four collinear magnetic states (FM, G-AF, layered AF, bilayered AF) and collect the converged total energies per formula unit in a CSV file (`total_energies.csv`). The verifier will recompute the exchange coupling constants J(Ni–Ir), J'(Ir–Ir), J'(Ni–Ni), and J''(Ir–Ir) from these energy differences.
2. Perform a self-consistent LSDA+U+SOC calculation for Sr2NiIrO6 and report the Ir orbital magnetic moment (in μB) in a JSON file (`ir_orbital_moment.json`).

## Assets

- Crystal structures of Sr2NiIrO6 and Sr2ZnIrO6 from Kayser et al., Inorg. Chem. 2013: 10.1021/ic4013457
- Open-source DFT code supporting LSDA+U+SOC (e.g., Quantum ESPRESSO, CP2K, ABINIT, GPAW): https://www.quantum-espresso.org

## Workflow steps

### Step 1: Prepare input crystal structures
- Role: process
- Action: Retrieve the experimental crystal structures of Sr2NiIrO6 and Sr2ZnIrO6 (monoclinic P2_1/n) from the published neutron diffraction data (Kayser et al. 2013) and generate DFT-format input files.
- Evidence: `/app/outputs/structure_inputs.json`

### Step 2: Construct artificial structural models
- Role: process
- Action: Build substitutional and supercell models to isolate magnetic sublattices and reduce Ir coordination: (a) Sr2Zn(Ni)IrO6 by replacing Ni with Zn in Sr2NiIrO6; (b) La2NiSiO6 by replacing Sr with La and Ir with Si; (c) Sr2GaIr0.5Si0.5O6 with alternating GaIr and SiGa planes for four-coordinated Ir.
- Evidence: `/app/outputs/artificial_models.txt`

### Step 3: LSDA electronic structure calculation
- Role: process
- Action: Perform a self-consistent spin-polarized LSDA calculation for FM Sr2NiIrO6 and extract the Ir 5d t2g bandwidth and the exchange splitting between spin channels.
- Evidence: `/app/outputs/lsda_bandwidth.json`

### Step 4: LSDA+U total energy calculations for multiple magnetic configurations
- Role: process
- Action: Perform LSDA+U calculations (U_Ni=6 eV, J_Ni=0.9 eV; U_Ir=2 eV, J_Ir=0.4 eV) for all four systems (Sr2NiIrO6, Sr2Zn(Ni)IrO6, La2NiSiO6, real Sr2ZnIrO6) in the FM, G-AF, layered AF, and bilayered AF collinear magnetic states. Converge total energies to meV accuracy.
- Evidence: `/app/outputs/lsda_u_outputs.txt`

### Step 5: Output total energies table
- Role: scored (load-bearing)
- Action: Compile the converged LSDA+U total energies (per formula unit) from the previous step into a CSV file.
- Output file: `/app/outputs/total_energies.csv`
- Format: csv
- Contract: columns: system (string), magnetic_state (string: FM, G_AF, layered_AF, bilayered_AF), total_energy_ev (float)
- Scoring: scored by hidden verifier

### Step 6: LDA+SOC calculation and J-projected DOS analysis
- Role: process
- Action: Perform LDA+SOC calculations for real Sr2ZnIrO6 and the artificial low-coordination model Sr2GaIr0.5Si0.5O6. Project the Ir t2g density of states onto the |J=3/2> and |J=1/2> basis and report the mixing and SOC splitting.
- Evidence: `/app/outputs/soc_projection.json`

### Step 7: LSDA+U+SOC calculation and Ir orbital moment
- Role: scored (load-bearing)
- Action: Perform a self-consistent LSDA+U+SOC calculation for Sr2NiIrO6 and extract the Ir orbital magnetic moment.
- Output file: `/app/outputs/ir_orbital_moment.json`
- Format: json
- Contract: {"ir_orbital_moment": <float>}  (unit: μ_B)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/total_energies.csv`
- `/app/outputs/ir_orbital_moment.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### total_energies.csv
- path: `/app/outputs/total_energies.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: LSDA+U total energies per formula unit for the specified systems and collinear magnetic states. The checker recomputes the exchange coupling parameters (J_Ni-Ir, J'_Ir-Ir, J'_Ni-Ni, J''_Ir-Ir) from these energy differences and compares them to hidden paper values.
- schema:
  - `type`: table
  - `required_columns`: `system`, `magnetic_state`, `total_energy_ev`
  - `units`:
    - `total_energy_ev`: eV

### ir_orbital_moment.json
- path: `/app/outputs/ir_orbital_moment.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Ir orbital magnetic moment from a self-consistent LSDA+U+SOC calculation for Sr2NiIrO6. The checker compares the value to the paper-reported orbital moment (~0.07 μB) within a suitable tolerance.
- schema:
  - `type`: object
  - `required`:
    - `ir_orbital_moment`: number
  - `units`:
    - `ir_orbital_moment`: μ_B

Notes: The total_energies.csv table must include entries for every required system/magnetic-state pair; missing entries will cause the exchange-parameter recomputation to fail. The ir_orbital_moment.json value must be a single float. Intermediate evidence files (structure_inputs.json, artificial_models.txt, lsda_bandwidth.json, lsda_u_outputs.txt, soc_projection.json) are not scored but must be produced to confirm the pipeline was executed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "total_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "magnetic_state",
          "total_energy_ev"
        ],
        "units": {
          "total_energy_ev": "eV"
        }
      },
      "description": "LSDA+U total energies per formula unit for the specified systems and collinear magnetic states. The checker recomputes the exchange coupling parameters (J_Ni-Ir, J'_Ir-Ir, J'_Ni-Ni, J''_Ir-Ir) from these energy differences and compares them to hidden paper values."
    },
    {
      "file": "ir_orbital_moment.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "ir_orbital_moment": "number"
        },
        "units": {
          "ir_orbital_moment": "μ_B"
        }
      },
      "description": "Ir orbital magnetic moment from a self-consistent LSDA+U+SOC calculation for Sr2NiIrO6. The checker compares the value to the paper-reported orbital moment (~0.07 μB) within a suitable tolerance."
    }
  ],
  "notes": "The total_energies.csv table must include entries for every required system/magnetic-state pair; missing entries will cause the exchange-parameter recomputation to fail. The ir_orbital_moment.json value must be a single float. Intermediate evidence files (structure_inputs.json, artificial_models.txt, lsda_bandwidth.json, lsda_u_outputs.txt, soc_projection.json) are not scored but must be produced to confirm the pipeline was executed."
}
```

## How you are scored
Your submission is evaluated by a hidden checker that reads the two required output files. 
- From `total_energies.csv`, the checker recomputes the exchange coupling strengths using prescribed formulas and compares the derived values to hidden reference exchange constants. Credit is awarded for each coupling parameter that falls within an allowed tolerance.
- The file `ir_orbital_moment.json` is compared against a hidden reference Ir orbital moment value; agreement within the tolerance earns full credit for this part.
The final score is a weighted combination of these two checks. The checker does not simply inspect the numbers you report; it re‑derives the exchange constants from the energy differences you supply and judges how well they reproduce the expected interactions. This means that simply inserting the paper's reported values without performing the actual DFT calculations will not pass the scoring.
