# Inducing magnetism in SnS2 monolayer via non‑magnetic doping and strain: a DFT reproduction

## Problem background
Two-dimensional SnS2 monolayer is a wide-bandgap semiconductor promising for next-generation electronics and spintronics. A key open question is whether stable magnetism can be introduced into this non-magnetic material by creating lattice defects or by substituting Sn atoms with non-magnetic elements from groups IA, IIA, and IIIA of the periodic table. Understanding the resulting magnetic moments and the energetic stabilization of spin-polarized states is fundamental to developing SnS2-based dilute magnetic semiconductors. This investigation uses first-principles density functional theory (DFT) to compute the spin-dependent electronic ground states of such defective monolayers and to examine how biaxial tensile strain influences the stability of spin polarization.

## Approach
The physical picture to be tested is that low-valent substitutional dopants (e.g., replacing Sn4+ with an IA or IIA cation) introduce holes into the anion S-3p states. According to Hund's rule coupling, these holes can spontaneously spin-polarize, producing a net magnetic moment, provided the exchange splitting overcomes the crystal-field splitting. The spin-polarization energy ε = E(NSP) – E(SP) quantifies the energetic preference for the spin-polarized state; a positive ε implies a stable magnetic solution. Biaxial tensile strain is applied to tune the impurity bandwidth and thereby modify the density of states at the Fermi level, which is predicted to enhance ε.

To test this idea, we construct a 4×4×1 supercell of the SnS2 monolayer (space group P-3m1, lattice constant a ≈ 3.65 Å, vacuum ≥ 12 Å) and systematically introduce a Sn vacancy (V_Sn), an S vacancy (V_S), and substitutional dopants (Li, Na, K, Mg, Ca, Sr, Al, Ga, In at a Sn site). For each system, we perform spin-polarized DFT geometry optimization to obtain the total energy E(SP) and total magnetic moment M, then carry out a non-spin-polarized single-point calculation at the relaxed geometry to obtain E(NSP). Additionally, bulk metal reference energies are computed for each dopant element to calculate binding energies (E_b = E_vacancy + μ_atom – E_doped). For the Mg- and Al-doped systems we repeat the spin-polarized / non-spin-polarized protocol under biaxial tensile strains of 0%, 5%, 10%, and 15% to map the strain dependence of ε. All DFT calculations use the Perdew-Burke-Ernzerhof (PBE) generalized gradient approximation and open-source plane-wave pseudopotential tools; the open-source DFT code Quantum ESPRESSO is a suitable vehicle for these computations.

## Reproduction target
The core objective is to produce, through the DFT workflow described below, two numerical artifacts:

1. `dft_results.json` – a table containing, for each system (V_Sn, V_S, Li, Na, K, Mg, Ca, Sr, Al, Ga, In), the computed total magnetic moment (in µ_B), the spin-polarization energy ε (in meV), and the binding energy E_b (in eV).

2. `strain_results.json` – a table containing, for the Mg- and Al-doped systems at each strain (0%, 5%, 10%, 15%), the spin-polarization energy ε (in meV).

These computed quantities will be compared against reference values by a hidden verifier; the verifier evaluates your DFT output against a hidden gold standard.

## Assets

- SnS2 monolayer crystal structure
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library (PBE): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Construct supercell structures
- Role: process
- Action: Generate a 4×4×1 supercell of SnS2 monolayer. Create structures with a Sn vacancy (V_Sn), an S vacancy (V_S), and substitutional dopings where a Sn atom is replaced by Li, Na, K, Mg, Ca, Sr, Al, Ga, or In. Also prepare bulk unit cells for each dopant element.
- Evidence: none

### Step 2: Compute bulk metal reference energies
- Role: process
- Action: Using DFT, perform geometry optimization and total energy calculation for the bulk phases of Li, Na, K, Mg, Ca, Sr, Al, Ga, and In to obtain the chemical potential μ per atom.
- Evidence: `/app/outputs/bulk_energies.json`

### Step 3: Spin-polarized DFT relaxations of defective monolayers
- Role: process
- Action: For each defective or doped supercell, perform spin‑polarized DFT geometry optimization; record the total energy (E_SP) and the total magnetic moment.
- Evidence: `/app/outputs/spin_results.json`

### Step 4: Non‑spin‑polarized DFT single‑point calculations
- Role: process
- Action: On each optimized geometry from step03, run a non‑spin‑polarized DFT single‑point calculation to obtain the total energy E_NSP for that system.
- Evidence: `/app/outputs/nonspin_results.json`

### Step 5: Compile dft_results.json
- Role: scored (load-bearing)
- Action: From the raw energies and magnetic moments, compute for each system (V_Sn, V_S, Li, Na, K, Mg, Ca, Sr, Al, Ga, In): the total magnetic moment M_total, the spin‑polarization energy ε = E_NSP – E_SP, and the binding energy E_b = E_v + μ – E_d (using the bulk reference energies). Write the results to dft_results.json.
- Output file: `/app/outputs/dft_results.json`
- Format: json
- Contract: Array of objects with keys: system (string), magnetic_moment (float, μ_B), epsilon (float, meV), binding_energy (float, eV).
- Scoring: scored by hidden verifier

### Step 6: Strain‑dependent DFT for Mg and Al doping
- Role: process
- Action: For Mg‑ and Al‑doped SnS2 monolayers, apply biaxial tensile strains of 0%, 5%, 10%, and 15%. At each strain, relax internal coordinates with spin‑polarized DFT, then perform a non‑spin‑polarized single‑point calculation to obtain E_SP and E_NSP for that strain.
- Evidence: `/app/outputs/strain_raw.json`

### Step 7: Compile strain_results.json
- Role: scored (load-bearing)
- Action: Compile the spin‑polarization energies ε for Mg‑ and Al‑doped systems at each strain into strain_results.json.
- Output file: `/app/outputs/strain_results.json`
- Format: json
- Contract: Array of objects with keys: system (string), strain (float, percent), epsilon (float, meV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_results.json`
- `/app/outputs/strain_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_results.json
- path: `/app/outputs/dft_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Total magnetic moment, spin‑polarization energy, and binding energy for each vacancy/dopant system. Compared against paper‑reported Table I values with hidden tolerances.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `system`, `magnetic_moment`, `epsilon`, `binding_energy`
    - `properties`:
      - `system`:
        - `type`: string
      - `magnetic_moment`:
        - `type`: number
        - `units`: μ_B
      - `epsilon`:
        - `type`: number
        - `units`: meV
      - `binding_energy`:
        - `type`: number
        - `units`: eV

### strain_results.json
- path: `/app/outputs/strain_results.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Spin‑polarization energy ε as a function of biaxial tensile strain for Mg‑ and Al‑doped SnS2. The checker verifies that ε is positive and increases monotonically with strain, consistent with Figure 2 of the paper.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `system`, `strain`, `epsilon`
    - `properties`:
      - `system`:
        - `type`: string
      - `strain`:
        - `type`: number
        - `units`: percent
      - `epsilon`:
        - `type`: number
        - `units`: meV

Notes: The dft_results.json output is verified by comparing the agent‑reported magnetic moments and epsilon against the paper’s published values (Table I) with appropriate tolerances. The strain_results.json output is verified by structural consistency (monotonic increase of epsilon with strain). Binding energy is present but may be scored at lower weight.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "system",
            "magnetic_moment",
            "epsilon",
            "binding_energy"
          ],
          "properties": {
            "system": {
              "type": "string"
            },
            "magnetic_moment": {
              "type": "number",
              "units": "μ_B"
            },
            "epsilon": {
              "type": "number",
              "units": "meV"
            },
            "binding_energy": {
              "type": "number",
              "units": "eV"
            }
          }
        }
      },
      "description": "Total magnetic moment, spin‑polarization energy, and binding energy for each vacancy/dopant system. Compared against paper‑reported Table I values with hidden tolerances."
    },
    {
      "file": "strain_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "system",
            "strain",
            "epsilon"
          ],
          "properties": {
            "system": {
              "type": "string"
            },
            "strain": {
              "type": "number",
              "units": "percent"
            },
            "epsilon": {
              "type": "number",
              "units": "meV"
            }
          }
        }
      },
      "description": "Spin‑polarization energy ε as a function of biaxial tensile strain for Mg‑ and Al‑doped SnS2. The checker verifies that ε is positive and increases monotonically with strain, consistent with Figure 2 of the paper."
    }
  ],
  "notes": "The dft_results.json output is verified by comparing the agent‑reported magnetic moments and epsilon against the paper’s published values (Table I) with appropriate tolerances. The strain_results.json output is verified by structural consistency (monotonic increase of epsilon with strain). Binding energy is present but may be scored at lower weight."
}
```

## How you are scored
A hidden verifier reads your final output files and scores each required artifact independently. For `dft_results.json` the verifier compares your reported `magnetic_moment` and `epsilon` for each system against reference values derived from the underlying publication; your binding energies are also examined for consistency. For `strain_results.json` the verifier checks that `epsilon` is positive and increases monotonically with strain for Mg- and Al-doped SnS2, and that the numeric range is physically plausible. Each scored artifact contributes a weighted fraction to a final reward in [0,1]; a perfect reproduction of the target results within the expected tolerances earns full credit. The verifier does not publish the reference numbers or tolerances—it evaluates your honest DFT output against a hidden gold standard. Simply reporting the correct paper numbers without executing the full DFT pipeline will not satisfy the scoring criteria.
