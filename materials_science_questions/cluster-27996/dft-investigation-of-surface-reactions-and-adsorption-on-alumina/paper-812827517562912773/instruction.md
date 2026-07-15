# DFT Calculation of Methane Activation on a Defective Alumina Surface

## Problem background
Synthesis of nanoporous graphene (NPG) via methane chemical vapor deposition (CVD) on gamma-alumina nanoparticles can occur without transition-metal catalysts. The rate-limiting step is believed to be the initial C–H bond cleavage of methane on a partially dehydrated gamma-Al₂O₃(100) surface containing an oxygen vacancy. A quantitative understanding of the energetics and electronic mechanism of this step is crucial for optimizing the synthesis process. This task aims to reproduce, using first-principles density functional theory (DFT), the reaction pathway and key descriptors of methane dissociative adsorption at such a vacancy site.

## Approach
Use plane-wave periodic DFT with the PBE-D3 functional and appropriate pseudopotentials. Construct a slab model of the gamma-Al₂O₃(100) surface and create one surface oxygen vacancy to represent the partially dehydrated active site. Then perform: (a) geometry optimization of isolated CH₄, the bare defective slab, physisorbed CH₄ on the slab, and co-adsorbed CH₃ + H; (b) a climbing-image nudged elastic band (CI-NEB) search to locate the transition state (TS1) connecting the physisorbed state to the dissociated products, followed by a refined saddle-point optimization. From the optimized total energies compute the physisorption energy ΔE_ad, the intrinsic activation barrier ΔE_a,TS1, and the effective activation energy. Carry out Bader charge analysis on the TS1 structure to obtain atomic charges on the transferring H, the adjacent O, the CH₃ fragment, and the Al at the vacancy site. Finally, extract the spin expectation value ⟨S²⟩ from the TS1 wavefunction. This combined analysis quantifies the rate-limiting barrier and probes the electronic character of the transition state.

## Reproduction target
Compute and report the following quantities in a single structured JSON file (results.json): (1) ΔE_ad – the physisorption energy of CH₄ on the defective surface (kJ/mol); (2) ΔE_a,TS1 – the activation energy for dissociative adsorption from the physisorbed state (kJ/mol); (3) ΔE^≠ = ΔE_ad + ΔE_a,TS1 – the effective activation energy (kJ/mol); (4) Bader charges (in e) at TS1 for the migrating hydrogen (H), the adjacent oxygen (O), the CH₃ fragment, and the Al atom at the vacancy site; (5) the spin expectation value ⟨S²⟩ at TS1 (unitless). All results must be obtained from the workflow described in the steps below, using your own DFT and CI-NEB calculations on the constructed slab model.

## Assets

- Bulk γ-Al₂O₃ crystal structure: 10.1107/S0108768191006119
- Quantum ESPRESSO (or equivalent plane-wave DFT code): https://www.quantum-espresso.org/
- CI-NEB implementation (neb.x or VTST tools): https://theory.cm.utexas.edu/vtsttools/
- Bader charge analysis code: http://theory.cm.utexas.edu/henkelman/code/bader/
- Pseudopotentials (PSlibrary or GBRV): http://www.quantum-espresso.org/pseudopotentials/

## Workflow steps

### Step 1: Build γ-Al₂O₃(100) surface model with oxygen vacancy
- Role: process
- Action: From the public bulk γ-Al₂O₃ crystal structure, construct a periodic slab model of the (100) surface with sufficient thickness and vacuum layer. Introduce one surface oxygen vacancy, leaving an undercoordinated Al site adjacent to it. Save the atomic coordinates and lattice vectors in a structure file for subsequent DFT steps.
- Evidence: `/app/outputs/slab_model.pw.in`

### Step 2: DFT geometry optimizations and CI-NEB of CH₄ activation on the defective surface
- Role: process
- Action: Using plane-wave DFT with the PBE-D3 functional, appropriate pseudopotentials, spin-polarized calculations, a suitable k-point mesh and energy cutoffs, perform: (a) optimization of isolated CH₄, (b) optimization of the bare defective slab, (c) optimization of physisorbed CH₄* on the slab, (d) optimization of the co-adsorbed products CH₃* + H*, and (e) a climbing-image nudged elastic band (CI-NEB) calculation to locate the transition state TS1 connecting CH₄* to CH₃* + H*, followed by a precise saddle-point refinement. Retain all geometries and total energies.
- Evidence: `/app/outputs/dft_calculation.log`

### Step 3: Extract energetics, Bader charges, and spin into results.json
- Role: scored (load-bearing)
- Action: From the DFT outputs of step_02, compute the physisorption energy ΔE_ad = E(CH₄*) - E(CH₄) - E(bare slab), the activation energy ΔE_a,TS1 = E(TS1) - E(CH₄*), and the effective activation energy ΔE≠ = ΔE_ad + ΔE_a,TS1. Perform Bader charge analysis on the TS1 structure to obtain atomic charges q(H), q(O), q(CH₃), q(Al), and compute the spin expectation value ⟨S²⟩. Write all results as a JSON file named results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"delta_E_ad_kJ_per_mol": "number", "delta_E_a_TS1_kJ_per_mol": "number", "delta_E_neff_kJ_per_mol": "number", "bader_charges_TS1": {"H": "number", "O": "number", "CH3": "number", "Al": "number"}, "spin_S2_TS1": "number"}
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
- target_policy: reference_match
- description: Aggregated DFT results for the methane physisorption, dissociative adsorption, and electronic structure at the transition state on the defective γ-Al₂O₃(100) surface. The values are compared to the paper's reported reference with absolute tolerances.
- schema:
  - `type`: object
  - `required`: `delta_E_ad_kJ_per_mol`, `delta_E_a_TS1_kJ_per_mol`, `delta_E_neff_kJ_per_mol`, `bader_charges_TS1`, `spin_S2_TS1`
  - `properties`:
    - `delta_E_ad_kJ_per_mol`:
      - `type`: number
      - `unit`: kJ/mol
    - `delta_E_a_TS1_kJ_per_mol`:
      - `type`: number
      - `unit`: kJ/mol
    - `delta_E_neff_kJ_per_mol`:
      - `type`: number
      - `unit`: kJ/mol
    - `bader_charges_TS1`:
      - `type`: object
      - `properties`:
        - `H`:
          - `type`: number
          - `unit`: e
        - `O`:
          - `type`: number
          - `unit`: e
        - `CH3`:
          - `type`: number
          - `unit`: e
        - `Al`:
          - `type`: number
          - `unit`: e
    - `spin_S2_TS1`:
      - `type`: number
      - `unit`: unitless

Notes: Task scope covers the rate-limiting step of CH₄ activation at an oxygen vacancy: slab construction, DFT/CI-NEB calculations, and extraction of energetics and Bader charges. The agent must run the full compute workflow; no pre-made structures or intermediate results are provided. The verifier compares the numeric fields in results.json against the paper's values using absolute tolerances.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "delta_E_ad_kJ_per_mol",
          "delta_E_a_TS1_kJ_per_mol",
          "delta_E_neff_kJ_per_mol",
          "bader_charges_TS1",
          "spin_S2_TS1"
        ],
        "properties": {
          "delta_E_ad_kJ_per_mol": {
            "type": "number",
            "unit": "kJ/mol"
          },
          "delta_E_a_TS1_kJ_per_mol": {
            "type": "number",
            "unit": "kJ/mol"
          },
          "delta_E_neff_kJ_per_mol": {
            "type": "number",
            "unit": "kJ/mol"
          },
          "bader_charges_TS1": {
            "type": "object",
            "properties": {
              "H": {
                "type": "number",
                "unit": "e"
              },
              "O": {
                "type": "number",
                "unit": "e"
              },
              "CH3": {
                "type": "number",
                "unit": "e"
              },
              "Al": {
                "type": "number",
                "unit": "e"
              }
            }
          },
          "spin_S2_TS1": {
            "type": "number",
            "unit": "unitless"
          }
        }
      },
      "description": "Aggregated DFT results for the methane physisorption, dissociative adsorption, and electronic structure at the transition state on the defective γ-Al₂O₃(100) surface. The values are compared to the paper's reported reference with absolute tolerances."
    }
  ],
  "notes": "Task scope covers the rate-limiting step of CH₄ activation at an oxygen vacancy: slab construction, DFT/CI-NEB calculations, and extraction of energetics and Bader charges. The agent must run the full compute workflow; no pre-made structures or intermediate results are provided. The verifier compares the numeric fields in results.json against the paper's values using absolute tolerances."
}
```

## How you are scored
A hidden verifier reads your results.json and compares each reported value independently to a hidden reference. Each quantity is checked with an absolute tolerance; full credit (1.0) is awarded if all values fall within their respective tolerances, otherwise partial credit is proportional to the fraction of passing checks. The verifier does not access any intermediate files; only the final numeric values in results.json are scored. The geometry optimizations and CI-NEB search in Steps 1 and 2 are required process steps but are not directly scored; the scored Step 3 depends on them being executed correctly to obtain the reported numbers.
