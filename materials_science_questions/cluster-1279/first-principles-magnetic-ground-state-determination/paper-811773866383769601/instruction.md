# First-principles investigation of FeSi structural, electronic, and magnetic properties using LDA, GGA, B3LYP, and Hartree-Fock

## Problem background
Iron monosilicide (FeSi) is a non-magnetic narrow-gap semiconductor with unusual temperature-dependent magnetic susceptibility, which has motivated studies into the interplay between non-local exchange effects and the itinerant band picture. First-principles density functional theory (DFT) has shown that local and semi-local functionals (LDA, GGA) correctly yield a non-magnetic insulating state with a small indirect gap, but they fail to capture the possible existence of low-energy magnetic states. This task investigates the role of non-local exchange by performing all-electron DFT calculations with the hybrid functional B3LYP and pure Hartree-Fock, in addition to LDA and GGA, to assess how these treatments affect the structural, electronic, and magnetic properties of FeSi.

## Approach
The calculations target the B20 crystal structure of FeSi (space group P2₁3, four formula units per unit cell). Starting from the experimental geometry, we perform geometry optimizations for the non-magnetic state using LDA, GGA (PW91), B3LYP, and Hartree-Fock functionals, each yielding the equilibrium lattice constant, internal coordinates, bulk modulus, and the indirect band gap. To explore magnetism, spin-polarized calculations initialized ferromagnetically are then carried out with B3LYP and Hartree-Fock at their respective optimized non-magnetic geometries, reporting the energy difference relative to the non-magnetic solution and the magnetic moment on iron. The calculations are performed with an open-source DFT code that supports hybrid functionals and exact exchange (e.g., Quantum ESPRESSO, CP2K, or FHI-aims), using a k-point mesh of at least 16×16×16. No specific code or basis set is mandated; the goal is to capture the qualitative trends among the four exchange-correlation treatments.

## Reproduction target
Produce the following artifacts, each stored in a JSON file under /app/outputs:
- For LDA, GGA, B3LYP (non-magnetic), and Hartree-Fock (non-magnetic): the optimized lattice constant a (Å), bulk modulus B (GPa), internal coordinates u_Fe and u_Si (dimensionless), and the indirect band gap Δ_ind (eV).
- For B3LYP and Hartree-Fock spin-polarized ferromagnetic states: the energy difference per unit cell (eV) between the ferromagnetic and non-magnetic solutions, and the magnetic moment per Fe atom (μ_B).
The results should be obtained by executing the workflow described in the steps, starting from the experimental B20 structure. The evaluation will assess the overall consistency of the computed quantities across the four functionals and the relative stability of the magnetic states.

## Assets

- FeSi crystal structure (B20, space group P2₁3)
- Diffuse basis set exponents for Fe and Si
- Open-source DFT code with hybrid functional support: https://www.quantum-espresso.org/
- Pseudopotential library (e.g., SSSP efficiency, PseudoDojo): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Non-magnetic single-point calculations at experimental geometry
- Role: process
- Action: At the experimental B20 structure (a=4.489 Å, u_Fe=0.137, u_Si=0.842), perform non-magnetic SCF calculations using LDA, GGA, B3LYP, and Hartree-Fock functionals. Extract the indirect band gap for each functional and record them in a reference file.
- Evidence: `/app/outputs/exp_geom_gaps.json`

### Step 2: LDA geometry optimization and properties
- Role: scored
- Action: Starting from the experimental B20 structure, optimize the lattice constant and internal coordinates using the LDA functional. Determine the bulk modulus and indirect band gap at the optimized geometry.
- Output file: `/app/outputs/step01_LDA_results.json`
- Format: json
- Contract: {"a": "float (Å)", "B": "float (GPa)", "u_Fe": "float (dimensionless)", "u_Si": "float (dimensionless)", "Delta_ind": "float (eV)"}
- Scoring: scored by hidden verifier

### Step 3: GGA (PW91) geometry optimization and properties
- Role: scored
- Action: Optimize the geometry of FeSi with the GGA (PW91) functional, then compute the bulk modulus and indirect band gap.
- Output file: `/app/outputs/step02_GGA_results.json`
- Format: json
- Contract: {"a": "float (Å)", "B": "float (GPa)", "u_Fe": "float (dimensionless)", "u_Si": "float (dimensionless)", "Delta_ind": "float (eV)"}
- Scoring: scored by hidden verifier

### Step 4: B3LYP non-magnetic geometry optimization and properties
- Role: scored (load-bearing)
- Action: Perform a non-magnetic geometry optimization with the B3LYP hybrid functional. Obtain the optimized lattice constant, internal coordinates, bulk modulus, and indirect band gap.
- Output file: `/app/outputs/step03_B3LYP_results.json`
- Format: json
- Contract: {"a": "float (Å)", "B": "float (GPa)", "u_Fe": "float (dimensionless)", "u_Si": "float (dimensionless)", "Delta_ind": "float (eV)"}
- Scoring: scored by hidden verifier

### Step 5: B3LYP spin-polarized ferromagnetic search
- Role: scored (load-bearing)
- Action: Starting from a ferromagnetic initialization and using the optimized geometry from step03, run a spin‑polarized B3LYP calculation. Converge the magnetic density and report the total energy difference relative to the non‑magnetic B3LYP solution (per unit cell) and the magnetic moment on each Fe atom.
- Output file: `/app/outputs/step04_B3LYP_magnetic.json`
- Format: json
- Contract: {"energy_diff_FM_NM": "float (eV per unit cell)", "moment_Fe": "float (μ_B)"}
- Scoring: scored by hidden verifier

### Step 6: Hartree-Fock non-magnetic geometry optimization and properties
- Role: scored
- Action: Optimize the geometry of FeSi using the Hartree‑Fock method. Determine the lattice constant, internal coordinates, bulk modulus, and indirect band gap for the non‑magnetic state.
- Output file: `/app/outputs/step05_HF_results.json`
- Format: json
- Contract: {"a": "float (Å)", "B": "float (GPa)", "u_Fe": "float (dimensionless)", "u_Si": "float (dimensionless)", "Delta_ind": "float (eV)"}
- Scoring: scored by hidden verifier

### Step 7: Hartree-Fock spin-polarized ferromagnetic search
- Role: scored (load-bearing)
- Action: Perform a spin‑polarized Hartree–Fock calculation at the HF‑optimized geometry (step05), initialized ferromagnetically. Converge the spin density and report the energy difference relative to the non‑magnetic HF state (per unit cell) and the magnetic moment per Fe atom.
- Output file: `/app/outputs/step06_HF_magnetic.json`
- Format: json
- Contract: {"energy_diff_FM_NM": "float (eV per unit cell)", "moment_Fe": "float (μ_B)"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step01_LDA_results.json`
- `/app/outputs/step02_GGA_results.json`
- `/app/outputs/step03_B3LYP_results.json`
- `/app/outputs/step04_B3LYP_magnetic.json`
- `/app/outputs/step05_HF_results.json`
- `/app/outputs/step06_HF_magnetic.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step01_LDA_results.json
- path: `/app/outputs/step01_LDA_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: LDA‑optimized structural and electronic properties
- schema:
  - `type`: object
  - `required`: `a`, `B`, `u_Fe`, `u_Si`, `Delta_ind`
  - `items`: object
  - `units`:
    - `a`: Å
    - `B`: GPa
    - `u_Fe`: dimensionless
    - `u_Si`: dimensionless
    - `Delta_ind`: eV

### step02_GGA_results.json
- path: `/app/outputs/step02_GGA_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: GGA‑optimized structural and electronic properties
- schema:
  - `type`: object
  - `required`: `a`, `B`, `u_Fe`, `u_Si`, `Delta_ind`
  - `items`: object
  - `units`:
    - `a`: Å
    - `B`: GPa
    - `u_Fe`: dimensionless
    - `u_Si`: dimensionless
    - `Delta_ind`: eV

### step03_B3LYP_results.json
- path: `/app/outputs/step03_B3LYP_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: B3LYP (non‑magnetic) optimized structural and electronic properties
- schema:
  - `type`: object
  - `required`: `a`, `B`, `u_Fe`, `u_Si`, `Delta_ind`
  - `items`: object
  - `units`:
    - `a`: Å
    - `B`: GPa
    - `u_Fe`: dimensionless
    - `u_Si`: dimensionless
    - `Delta_ind`: eV

### step04_B3LYP_magnetic.json
- path: `/app/outputs/step04_B3LYP_magnetic.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: B3LYP ferromagnetic‑vs‑nonmagnetic energy difference and Fe moment
- schema:
  - `type`: object
  - `required`: `energy_diff_FM_NM`, `moment_Fe`
  - `items`: object
  - `units`:
    - `energy_diff_FM_NM`: eV per unit cell
    - `moment_Fe`: μ_B

### step05_HF_results.json
- path: `/app/outputs/step05_HF_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Hartree‑Fock (non‑magnetic) optimized structural and electronic properties
- schema:
  - `type`: object
  - `required`: `a`, `B`, `u_Fe`, `u_Si`, `Delta_ind`
  - `items`: object
  - `units`:
    - `a`: Å
    - `B`: GPa
    - `u_Fe`: dimensionless
    - `u_Si`: dimensionless
    - `Delta_ind`: eV

### step06_HF_magnetic.json
- path: `/app/outputs/step06_HF_magnetic.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Hartree‑Fock ferromagnetic‑vs‑nonmagnetic energy difference and Fe moment
- schema:
  - `type`: object
  - `required`: `energy_diff_FM_NM`, `moment_Fe`
  - `items`: object
  - `units`:
    - `energy_diff_FM_NM`: eV per unit cell
    - `moment_Fe`: μ_B

Notes: Structural T3 scoring: the checker verifies relative ordering of lattice constants (LDA < GGA ≤ B3LYP << HF) and indirect gaps (LDA < GGA << B3LYP << HF), and that the B3LYP ferromagnetic state is metastable (energy_diff > 0) while the HF ferromagnetic state is stable (energy_diff < 0). Tolerances are generous to absorb implementation‑dependent spread.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step01_LDA_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "a",
          "B",
          "u_Fe",
          "u_Si",
          "Delta_ind"
        ],
        "items": {},
        "units": {
          "a": "Å",
          "B": "GPa",
          "u_Fe": "dimensionless",
          "u_Si": "dimensionless",
          "Delta_ind": "eV"
        }
      },
      "description": "LDA‑optimized structural and electronic properties"
    },
    {
      "file": "step02_GGA_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "a",
          "B",
          "u_Fe",
          "u_Si",
          "Delta_ind"
        ],
        "items": {},
        "units": {
          "a": "Å",
          "B": "GPa",
          "u_Fe": "dimensionless",
          "u_Si": "dimensionless",
          "Delta_ind": "eV"
        }
      },
      "description": "GGA‑optimized structural and electronic properties"
    },
    {
      "file": "step03_B3LYP_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "a",
          "B",
          "u_Fe",
          "u_Si",
          "Delta_ind"
        ],
        "items": {},
        "units": {
          "a": "Å",
          "B": "GPa",
          "u_Fe": "dimensionless",
          "u_Si": "dimensionless",
          "Delta_ind": "eV"
        }
      },
      "description": "B3LYP (non‑magnetic) optimized structural and electronic properties"
    },
    {
      "file": "step04_B3LYP_magnetic.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "energy_diff_FM_NM",
          "moment_Fe"
        ],
        "items": {},
        "units": {
          "energy_diff_FM_NM": "eV per unit cell",
          "moment_Fe": "μ_B"
        }
      },
      "description": "B3LYP ferromagnetic‑vs‑nonmagnetic energy difference and Fe moment"
    },
    {
      "file": "step05_HF_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "a",
          "B",
          "u_Fe",
          "u_Si",
          "Delta_ind"
        ],
        "items": {},
        "units": {
          "a": "Å",
          "B": "GPa",
          "u_Fe": "dimensionless",
          "u_Si": "dimensionless",
          "Delta_ind": "eV"
        }
      },
      "description": "Hartree‑Fock (non‑magnetic) optimized structural and electronic properties"
    },
    {
      "file": "step06_HF_magnetic.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "energy_diff_FM_NM",
          "moment_Fe"
        ],
        "items": {},
        "units": {
          "energy_diff_FM_NM": "eV per unit cell",
          "moment_Fe": "μ_B"
        }
      },
      "description": "Hartree‑Fock ferromagnetic‑vs‑nonmagnetic energy difference and Fe moment"
    }
  ],
  "notes": "Structural T3 scoring: the checker verifies relative ordering of lattice constants (LDA < GGA ≤ B3LYP << HF) and indirect gaps (LDA < GGA << B3LYP << HF), and that the B3LYP ferromagnetic state is metastable (energy_diff > 0) while the HF ferromagnetic state is stable (energy_diff < 0). Tolerances are generous to absorb implementation‑dependent spread."
}
```

## How you are scored
A hidden verifier will independently read each scored output file, extract the reported values, and compare them against a set of physically motivated criteria that check internal consistency and physically expected relationships among the different exchange-correlation functionals (e.g., the ordering of lattice constants and band gaps, and the sign of magnetic energy differences). Each scored stage is assigned a weight, and the total reward is a weighted combination of the stage-level scores, normalized to a value between 0 and 1. The verifier does not rely on exact numerical agreement with the original paper; generous tolerances are used to absorb legitimate differences arising from code, pseudopotential, or basis-set choices. The task is not simply reproducing a published table; the scoring rewards computing the quantities through the prescribed protocol and obtaining results that satisfy the fundamental physics of the problem.