## Problem background

The oxygen reduction reaction (ORR) and oxygen evolution reaction (OER) are central to rechargeable metal–air batteries, but their sluggish kinetics require efficient catalysts. Metal porphyrins are promising non‑noble‑metal molecular catalysts; however, the binding energies of oxygenated intermediates are often too strong or too weak, leading to high overpotentials. Modifying the interaction between the catalyst molecule and a supporting substrate can tune these binding energies and improve bifunctional ORR/OER activity.

This task investigates how a Co‑porphyrin molecule’s catalytic performance changes when supported on a single graphene layer, a Ni(111) surface, or a graphene/Ni(111) bilayer, compared to the isolated (pristine) molecule.

## Approach

All electronic‑structure calculations are performed with density functional theory (DFT) using the Perdew–Burke–Ernzerhof (PBE) exchange‑correlation functional, projector‑augmented wave (PAW) pseudopotentials, and a plane‑wave basis. Dispersion interactions are included via Grimme’s DFT‑D3 scheme. Any open‑source plane‑wave DFT code (e.g., Quantum ESPRESSO) can be used.

The reaction network for OER and ORR follows the four‑step acid‑medium mechanisms:
OER:  (a) H₂O(l) + * → OH* + e⁻ + H⁺,  (b) OH* → O* + e⁻ + H⁺,  (c) H₂O(l) + O* → OOH* + e⁻ + H⁺,  (d) OOH* → O₂(g) + e⁻ + H⁺.
ORR (reverse):  (e) * + O₂(g) + e⁻ + H⁺ → OOH*,  (f) OOH* + e⁻ + H⁺ → H₂O(l) + O*,  (g) O* + e⁻ + H⁺ → OH*,  (h) OH* + e⁻ + H⁺ → H₂O(l) + *.
For each step, the Gibbs free‑energy change is computed as  ΔG = ΔE + ΔZPE – TΔS  (at zero applied potential, pH = 0, T = 298 K), where ΔE is the DFT electronic‑energy difference. The adsorption energies ΔE(OH*), ΔE(O*), ΔE(OOH*) are obtained from the total energies of the clean system and the adsorbed intermediates, using H₂O and H₂ as references.
The OER overpotential is  η_OER = max{ΔG_a, ΔG_b, ΔG_c, ΔG_d}/e – 1.23 V, and the ORR overpotential is  η_ORR = max{ΔG_e, ΔG_f, ΔG_g, ΔG_h}/e + 1.23 V.

## Reproduction target

For the four catalyst systems — (i) pristine (isolated) Co‑porphyrin, (ii) Co‑porphyrin supported on a single graphene layer, (iii) Co‑porphyrin directly on a Ni(111) slab, and (iv) Co‑porphyrin on a graphene/Ni(111) bilayer — compute the Gibbs free‑energy changes of each OER and ORR elementary step and determine the OER and ORR overpotentials. Write the complete set of step‑free‑energies and overpotentials to a structured JSON file.

## Assets

All required resources are publicly available:
- A plane‑wave DFT code, preferably Quantum ESPRESSO (https://www.quantum‑espresso.org/, open source, use the latest stable version).
- PAW pseudopotentials for the PBE functional, e.g., the SSSP efficiency library (https://www.materialscloud.org/discover/sssp/table/efficiency) or the GBRV library (https://www.physics.rutgers.edu/gbrv/).
- The Atomic Simulation Environment (ASE, https://wiki.fysik.dtu.dk/ase/) is optional for structure building and job management.
- Standard zero‑point energy (ZPE) and vibrational entropy (TS) corrections at 298 K, taken from the literature and used in the original work, are provided below and do **not** need to be recomputed from DFT frequencies:

| Species  | ZPE (eV) | TS (eV)  |
|----------|----------|----------|
| OH*      | 0.35     | 0.07     |
| O*       | 0.05     | 0.06     |
| OOH*     | 0.35     | 0.66     |
| H₂O      | 0.56     | 0.67     |
| H₂       | 0.27     | 0.41     |

The DFT‑computed total energies of the isolated H₂O and H₂ molecules are obtained from the same functional/basis/pseudopotential setup used for the catalyst systems.

## Workflow steps

### Step 1: Build atomic models
- Role: process
- Action: Construct initial atomic structures for the four catalyst systems: (1) an isolated Co‑porphyrin molecule, (2) Co‑porphyrin adsorbed on a single graphene monolayer, (3) Co‑porphyrin adsorbed on a 4‑layer Ni(111) slab, and (4) Co‑porphyrin on a graphene/Ni(111) bilayer slab. Use plausible adsorption sites (e.g., Co atom above the hollow site of graphene, fcc site on Ni(111)) and include a vacuum layer of at least 15 Å in the surface‑normal direction.
- Evidence: none

### Step 2: DFT geometry optimisation – clean systems
- Role: process
- Action: Perform spin‑polarised DFT geometry relaxations for the clean systems (without adsorbates): isolated Co‑porphyrin, graphene monolayer, Ni(111) slab, and each of the three supported systems. Use PBE+PAW, a plane‑wave kinetic energy cutoff of 500 eV, Γ‑point k‑sampling, DFT‑D3 dispersion, and converge the energy to at least 10⁻⁶ eV and forces to at least 0.001 eV/Å. Store the final total energy E(*) of each clean system.
- Evidence: `/app/outputs/clean_energies.json` (a JSON file mapping system names to final total DFT energies, for verification of the workflow but not scored)

### Step 3: DFT geometry optimisation – adsorbed intermediates
- Role: process
- Action: For each of the four catalyst systems, perform spin‑polarised DFT geometry relaxations for OH*, O*, and OOH* species adsorbed on the Co active site, using the same computational settings as in Step 2. Obtain the total energies E(OH*), E(O*), E(OOH*) for each system.
- Evidence: `/app/outputs/adsorbate_energies.json` (mapping system+adsorbate names to final total DFT energies)

### Step 4: Calculate free‑energy steps and overpotentials (load‑bearing)
- Role: scored (load‑bearing)
- Action: From the total energies obtained in Steps 2–3, together with the standard ZPE/TS corrections and the DFT energies of H₂O and H₂, compute the Gibbs free energy changes ΔG_a … ΔG_d (OER) and ΔG_e … ΔG_h (ORR) for each system. Then calculate the OER and ORR overpotentials using the formulas given above. Write the full set of free‑energy steps and overpotentials for all four systems to a JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: A JSON object with a top‑level key "systems". The value is an object whose keys are the system identifiers "pristine", "on_graphene", "on_Ni111", "on_graphene_Ni111". Each system object contains:
    - "free_energy_steps": an object with keys "OER" and "ORR".
      - "OER": an array of exactly four numbers in eV (ΔG_a, ΔG_b, ΔG_c, ΔG_d).
      - "ORR": an array of exactly four numbers in eV (ΔG_e, ΔG_f, ΔG_g, ΔG_h).
    - "overpotentials": an object with keys "ORR" and "OER", each a number in V (positive values).
  All numbers should be reported to at least three decimal places.
- Scoring: scored by hidden verifier

## Output files

The following files must be written under `/app/outputs`:
- `/app/outputs/results.json`  (scored)
- (optional) `/app/outputs/clean_energies.json` (process evidence)
- (optional) `/app/outputs/adsorbate_energies.json` (process evidence)

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Gibbs free‑energy diagrams and overpotentials for the four Co‑porphyrin catalyst systems.
- schema:
  - `type`: object
  - `required`:
    - `systems`: object
  - `description`: Each key under 'systems' is one of 'pristine', 'on_graphene', 'on_Ni111', 'on_graphene_Ni111'. The value contains:
  - 'free_energy_steps': object with keys 'OER' (array of 4 numbers in eV) and 'ORR' (array of 4 numbers in eV).
  - 'overpotentials': object with keys 'ORR' (number in V) and 'OER' (number in V).
  - `units`:
    - `free_energy_steps.*`: eV
    - `overpotentials.*`: V

Notes: The verifier recomputes overpotentials from the submitted free‑energy steps and checks internal consistency and conservation of free energy before comparing against hidden reference values and trend expectations.

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
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "systems": "object"
        },
        "description": "Each key under 'systems' is one of 'pristine', 'on_graphene', 'on_Ni111', 'on_graphene_Ni111'. The value contains:\n  - 'free_energy_steps': object with keys 'OER' (array of 4 numbers in eV) and 'ORR' (array of 4 numbers in eV).\n  - 'overpotentials': object with keys 'ORR' (number in V) and 'OER' (number in V).",
        "units": {
          "free_energy_steps.*": "eV",
          "overpotentials.*": "V"
        }
      },
      "description": "Gibbs free‑energy diagrams and overpotentials for the four Co‑porphyrin catalyst systems."
    }
  ],
  "notes": "The verifier recomputes overpotentials from the submitted free‑energy steps and checks internal consistency and conservation of free energy before comparing against hidden reference values and trend expectations."
}
```

## How you are scored

A hidden verifier reads your `results.json` and performs independent consistency and trend checks. These checks verify that the submitted free-energy steps and overpotentials are internally consistent (overpotentials computed from the steps match the reported overpotentials, and the sums of the OER and ORR steps approximate the expected thermodynamic limits) and that the results for the different catalyst systems satisfy expected qualitative trends. The verifier does not require the exact matching of published values; instead, it validates self-consistency and that the overall conclusions regarding relative activities align with the paper's findings. Merely writing the paper’s reported numbers is **not** sufficient – the verifier recomputes quantities from your reported free‑energy steps and relies on self‑consistency and trend information.
