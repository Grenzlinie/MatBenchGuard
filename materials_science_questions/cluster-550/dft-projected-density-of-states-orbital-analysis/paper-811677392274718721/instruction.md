# Electronic band gaps of Si clathrates from density functional theory

## Problem background
Type-I Si clathrates are cage-like frameworks built from face‑shared Si polyhedra that can host guest atoms inside. Substituting some framework Si atoms with group‑13 elements like Ga, while introducing electropositive guest ions (e.g., K), offers a route to control the electronic structure via charge compensation. Whether the resulting compound K<sub>8</sub>Ga<sub>8</sub>Si<sub>38</sub> becomes semiconducting, and how its Kohn‑Sham band gap compares to those of the empty clathrate Si<sub>46</sub> and ordinary diamond‑phase Si, is the central question investigated by density‑functional theory.

## Approach
Plane‑wave density‑functional theory (DFT) with a consistent exchange‑correlation functional (e.g., LDA + GGA correction) and a uniform pseudopotential set is used to compute the total electronic density of states for four distinct crystal structures:

- **Diamond Si** – the reference semiconductor
- **Si<sub>46</sub>** – the guest‑free type‑I clathrate
- **K<sub>8</sub>Si<sub>46</sub>** – the filled clathrate (eight K guests, no Ga substitution)
- **K<sub>8</sub>Ga<sub>8</sub>Si<sub>38</sub>** – the Ga‑substituted clathrate with charge compensation

For the insulating systems the Kohn‑Sham band gap is extracted from the separation between the valence‑band maximum and conduction‑band minimum in the DOS. For K<sub>8</sub>Si<sub>46</sub> the position of the Fermi level determines whether it is metallic. Relative band‑gap differences (Si<sub>46</sub> – diamond, K<sub>8</sub>Ga<sub>8</sub>Si<sub>38</sub> – Si<sub>46</sub>, and K<sub>8</sub>Ga<sub>8</sub>Si<sub>38</sub> – diamond) are then computed to quantify the effect of guest filling and Ga substitution.

## Reproduction target
Perform the four DFT calculations described in the workflow steps and, from the resulting electronic density of states, obtain the Kohn‑Sham band gaps (in eV) for diamond Si, Si<sub>46</sub>, and K<sub>8</sub>Ga<sub>8</sub>Si<sub>38</sub>, and determine whether K<sub>8</sub>Si<sub>46</sub> is metallic (Fermi level inside conduction‑like states). Write all values to a single JSON file (`band_gaps.json`) containing:

- `diamond_Si_gap_ev` (float, eV)
- `Si46_gap_ev` (float, eV)
- `K8Si46_metallic` (bool)
- `K8Ga8Si38_gap_ev` (float, eV)
- `Si46_minus_diamond_ev` (float, eV)
- `K8Ga8Si38_minus_Si46_ev` (float, eV)
- `K8Ga8Si38_minus_diamond_ev` (float, eV)

All calculations must use the same exchange‑correlation functional and pseudopotential library; the resulting relative differences and the metallic classification constitute the reproduction target.

## Assets

- Crystal structure of K8Ga8Si38 (CCDC 809090): https://www.ccdc.cam.ac.uk/structures/
- Crystal structure of type-I Si clathrate Si46
- Crystal structure of K8Si46
- Crystal structure of diamond Si
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP Efficiency pseudopotential library: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Prepare crystal structures
- Role: process
- Action: Retrieve or construct the crystallographic input files for diamond Si, the guest-free Si46, K8Si46, and K8Ga8Si38 in a format suitable for plane-wave DFT (e.g., CIF or Quantum ESPRESSO input).
- Evidence: `/app/outputs/structure_preparation.log`

### Step 2: DFT reference calculation: diamond Si
- Role: process
- Action: Run a plane-wave DFT calculation for diamond Si using a consistent exchange-correlation functional (e.g., LDA with GGA corrections) to obtain the total energy and electronic density of states.
- Evidence: `/app/outputs/diamond_si_dft.log`

### Step 3: DFT calculation: Si46
- Role: process
- Action: Run a plane-wave DFT calculation for the guest-free type-I clathrate Si46 to obtain its total DOS and Kohn-Sham band gap.
- Evidence: `/app/outputs/si46_dft.log`

### Step 4: DFT calculation: K8Si46
- Role: process
- Action: Run a plane-wave DFT calculation for K8Si46 to obtain its total DOS and determine the Fermi level position.
- Evidence: `/app/outputs/k8si46_dft.log`

### Step 5: DFT calculation: K8Ga8Si38
- Role: process
- Action: Run a plane-wave DFT calculation for K8Ga8Si38 to obtain its total DOS and Kohn-Sham band gap.
- Evidence: `/app/outputs/k8ga8si38_dft.log`

### Step 6: Compute relative band gaps and classify K8Si46
- Role: scored (load-bearing)
- Action: From the DFT outputs, extract the Kohn-Sham band gaps (in eV) for diamond Si, Si46, and K8Ga8Si38, and determine whether K8Si46 has a Fermi level inside conduction bands (metallic). Compute the relative differences: Si46 gap minus diamond Si gap, K8Ga8Si38 gap minus Si46 gap, K8Ga8Si38 gap minus diamond Si gap. Write all values to band_gaps.json.
- Output file: `/app/outputs/band_gaps.json`
- Format: json
- Contract: JSON object with fields: diamond_Si_gap_ev (float, eV), Si46_gap_ev (float, eV), K8Si46_metallic (bool), K8Ga8Si38_gap_ev (float, eV), Si46_minus_diamond_ev (float, eV), K8Ga8Si38_minus_Si46_ev (float, eV), K8Ga8Si38_minus_diamond_ev (float, eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gaps.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gaps.json
- path: `/app/outputs/band_gaps.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Extracted Kohn-Sham band gaps from the DFT calculations: absolute gaps for diamond Si, Si46, and K8Ga8Si38, a metallic flag for K8Si46, and the three relative gap differences (Si46 minus diamond, K8Ga8Si38 minus Si46, K8Ga8Si38 minus diamond). All energy values are in eV.
- schema:
  - `type`: object
  - `required`:
    - `diamond_Si_gap_ev`: number (eV)
    - `Si46_gap_ev`: number (eV)
    - `K8Si46_metallic`: boolean
    - `K8Ga8Si38_gap_ev`: number (eV)
    - `Si46_minus_diamond_ev`: number (eV)
    - `K8Ga8Si38_minus_Si46_ev`: number (eV)
    - `K8Ga8Si38_minus_diamond_ev`: number (eV)

Notes: The checker reads band_gaps.json and compares the three relative gap values and the metallic flag against hidden reference gold within a tolerance. The absolute gap values are not directly scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "diamond_Si_gap_ev": "number (eV)",
          "Si46_gap_ev": "number (eV)",
          "K8Si46_metallic": "boolean",
          "K8Ga8Si38_gap_ev": "number (eV)",
          "Si46_minus_diamond_ev": "number (eV)",
          "K8Ga8Si38_minus_Si46_ev": "number (eV)",
          "K8Ga8Si38_minus_diamond_ev": "number (eV)"
        }
      },
      "description": "Extracted Kohn-Sham band gaps from the DFT calculations: absolute gaps for diamond Si, Si46, and K8Ga8Si38, a metallic flag for K8Si46, and the three relative gap differences (Si46 minus diamond, K8Ga8Si38 minus Si46, K8Ga8Si38 minus diamond). All energy values are in eV."
    }
  ],
  "notes": "The checker reads band_gaps.json and compares the three relative gap values and the metallic flag against hidden reference gold within a tolerance. The absolute gap values are not directly scored."
}
```

## How you are scored
A hidden verifier reads the `band_gaps.json` file you produce. It compares the three relative gap values and the `K8Si46_metallic` flag against a hidden gold that reflects the correct computational outcome for the same physical quantity. The comparison uses a tolerance that absorbs legitimate run‑to‑run variations from different DFT implementations while requiring a genuine computation. The absolute gap values serve as supporting evidence and must lie in a physically plausible range. Each scored quantity is weighted to yield a total reward in the interval [0,1]; the relative differences and the metallic classification carry the highest weight. Simply copying numbers, even if they happen to match the gold, will not receive full credit because the hidden verifier may also cross‑check internal consistency and compare against auxiliary thresholds.
