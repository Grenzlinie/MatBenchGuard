# First-principles DFT Study of Surface Doping of Bi₂Se₃ by Adsorbates

## Problem background
Bi₂Se₃ is a three‑dimensional topological insulator with spin‑momentum‑locked Dirac surface states. As‑grown crystals are intrinsically n‑doped by selenium vacancies, shifting the Fermi energy into the conduction band and destroying the topological protection. A recent experimental technique demonstrates that water adsorption followed by XUV irradiation produces p‑doping that restores the Dirac cone, leading to a topologically pristine surface. The microscopic origin of this doping is unknown. Theoretical calculations can help identify which chemical species – water, hydroxyl, atomic oxygen, carbon, or CH – physisorbed or chemisorbed at pristine or Se‑vacancy surface sites produce the observed electronic changes, and which ones might compensate the vacancy‑induced n‑doping. This task requires you to compute the adsorption energetics and electronic structure for these systems using density functional theory.

## Approach
You will perform first‑principles DFT calculations on a 4‑quintuple‑layer Bi₂Se₃ slab with a 2×2 surface cell and 15 Å vacuum, using the PBE exchange‑correlation functional with Grimme D2 van der Waals correction and an open‑source plane‑wave PAW implementation (e.g., GPAW via ASE). Lattice constants are a=4.12 Å, c=28.89 Å. The workflow proceeds as follows: First, compute reference energies for isolated gas‑phase H₂O, OH, O, H, O₂, H₂, C, and CH. Then relax the atomic positions of the clean slab (surface and subsurface layers) and perform a spin‑orbit coupling (SOC) single‑point calculation to obtain its total energy and band structure; set its Fermi level to zero for subsequent alignment. Next, create a surface Se vacancy in the 2×2 cell, relax the defective slab, and compute its SOC band structure. For each adsorbate (H₂O, OH, O, C, CH) on each surface (pristine and Se‑defective), place the adsorbate near the relevant site, optimize the geometry without SOC, and then run a SOC single‑point calculation to obtain the total energy and electronic bands. From these total energies you will derive adsorption energies, Fermi level shifts relative to the clean slab, formation energies using H₂, O₂, and atomic C as reference states, and reaction energies for the proposed water‑splitting steps and carbon‑mediated hydrogen formation. Finally, extract the SOC band eigenvalues along the M‑Γ‑K path for the O/V system. All steps must be executed and the results documented; the final comparison will check the accuracy of the derived quantities.

## Reproduction target
Produce two JSON files.

results.json must contain, for each system (adsorbate X on surface S, where X ∈ {H₂O, OH, O, C, CH} and S ∈ {pristine, defective}) plus the clean and defective slabs, the following quantities: name (label), surface (pristine or defective), adsorbate (clean, H₂O, OH, O, C, CH), E_ads (adsorption energy in eV, computed as E_total(X/S) – E_total(S) – E_total(X)), and E_Fermi (Fermi energy in eV, aligned so the clean slab Fermi level is zero). Also include a list of reaction_energies, where each entry has a reaction description and its delta_E (reaction energy in eV) for the key steps: (1) H₂O/V → O/V + H₂, (2) H₂O/V → OH/V + H/S, (3) OH/V → O/V + H/S, (4) H/S + H/S → H₂, (5) H/S + C/S → CH/S, (6) H/S + CH/S → C/S + H₂. Use formation energies relative to H₂, O₂, atomic C, and the clean/defective slabs to compute these reaction energies.

band_structure_O_V.json must contain the k‑point coordinates along the M‑Γ‑K path for the 2×2 surface Brillouin zone (kpath) and the corresponding band eigenvalues (bands, an array of arrays of energies in eV) from the SOC calculation of the O/V system.

## Assets

- GPAW: gpaw
- ASE: ase
- Bi₂Se₃ bulk lattice constants

## Workflow steps

### Step 1: Compute gas‑phase reference energies
- Role: process
- Action: Compute total energies of isolated gas‑phase species (H₂O, OH, O, H, O₂, H₂, C, CH) using DFT. These provide the reference energies for adsorption and formation energy calculations.
- Evidence: `/app/outputs/gas_phase_energies.json`

### Step 2: Relax clean 4‑QL Bi₂Se₃ slab and compute SOC band structure
- Role: process
- Action: Build a 4‑quintuple‑layer Bi₂Se₃ slab with a 2×2 surface cell and 15 Å vacuum. Relax the surface and subsurface layers using DFT (PBE, Grimme D2 vdW). Then run a single‑point SOC calculation to obtain the total energy and band structure. Set the Fermi level of this clean slab to zero for later band alignment.
- Evidence: `/app/outputs/clean_slab_summary.json`

### Step 3: Relax Se‑defective slab and compute SOC band structure
- Role: process
- Action: Remove one surface Se atom from the 2×2 cell, relax the atomic positions, and perform a SOC single‑point calculation to obtain the total energy and band structure of the defective surface (V).
- Evidence: `/app/outputs/defective_slab_summary.json`

### Step 4: Run adsorption DFT calculations for all adsorbate/surface combinations
- Role: process
- Action: For each adsorbate X = H₂O, OH, O, C, CH and each surface S = pristine, defective: place X near the appropriate site, perform geometry relaxation without SOC, then run a SOC single‑point calculation to obtain the total energy and final band structure. Save the relaxed geometries, total energies, and aligned Fermi levels.
- Evidence: `/app/outputs/adsorption_runs.log`

### Step 5: Extract adsorption energies, Fermi shifts, and reaction energies
- Role: scored (load-bearing)
- Action: From the total energies of all systems, compute: (1) adsorption energies E_ads = E(X/surface) – E(surface) – E(X); (2) Fermi level shifts (E_Fermi) relative to the clean slab; (3) formation energies using standard states (H₂, O₂, atomic C, and the clean/defective slabs); (4) reaction energies for the water‑splitting steps: H₂O/V → O/V + H₂, H₂O/V → OH/V + H/S, OH/V → O/V + H/S, and carbon‑mediated H₂ formation steps. Write all results into results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"type":"object","required":["systems","reaction_energies"],"items":{"systems":{"type":"array","items":{"type":"object","fields":{"name":"string","surface":"string (pristine or defective)","adsorbate":"string","E_ads":"float (eV)","E_Fermi":"float (eV)"}}},"reaction_energies":{"type":"array","items":{"type":"object","fields":{"reaction":"string","delta_E":"float (eV)"}}}}}
- Scoring: scored by hidden verifier

### Step 6: Output O/V band structure data
- Role: scored
- Action: From the SOC band structure calculation for O/V, extract the band eigenvalues along the high‑symmetry path M‑Γ‑K for the 2×2 surface Brillouin zone. Write the k‑point coordinates and eigenvalue arrays into band_structure_O_V.json.
- Output file: `/app/outputs/band_structure_O_V.json`
- Format: json
- Contract: {"type":"object","required":["kpath","bands"],"items":{"kpath":"array of [kx, ky, kz] floats","bands":"array of arrays of float (eV)"}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`
- `/app/outputs/band_structure_O_V.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: All computed adsorption energies, Fermi level shifts, and derived reaction energies; compared to the paper’s reported values within tolerance.
- schema:
  - `type`: object
  - `required`: `systems`, `reaction_energies`
  - `items`:
    - `systems`:
      - `type`: array
      - `items`:
        - `type`: object
        - `fields`:
          - `name`: string
          - `surface`: string (pristine or defective)
          - `adsorbate`: string
          - `E_ads`: float (eV)
          - `E_Fermi`: float (eV)
    - `reaction_energies`:
      - `type`: array
      - `items`:
        - `type`: object
        - `fields`:
          - `reaction`: string
          - `delta_E`: float (eV)

### band_structure_O_V.json
- path: `/app/outputs/band_structure_O_V.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Band eigenvalues of the O/V system along M‑Γ‑K; checked for a linear Dirac cone crossing at Γ and Fermi level alignment.
- schema:
  - `type`: object
  - `required`: `kpath`, `bands`
  - `items`:
    - `kpath`: array of [kx, ky, kz] (floats)
    - `bands`: array of arrays of float (eV)

Notes: All energies are in eV. The checker compares results.json entries to hidden paper values with a tolerance. band_structure_O_V.json is audited for the Dirac cone feature.

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
          "systems",
          "reaction_energies"
        ],
        "items": {
          "systems": {
            "type": "array",
            "items": {
              "type": "object",
              "fields": {
                "name": "string",
                "surface": "string (pristine or defective)",
                "adsorbate": "string",
                "E_ads": "float (eV)",
                "E_Fermi": "float (eV)"
              }
            }
          },
          "reaction_energies": {
            "type": "array",
            "items": {
              "type": "object",
              "fields": {
                "reaction": "string",
                "delta_E": "float (eV)"
              }
            }
          }
        }
      },
      "description": "All computed adsorption energies, Fermi level shifts, and derived reaction energies; compared to the paper’s reported values within tolerance."
    },
    {
      "file": "band_structure_O_V.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "kpath",
          "bands"
        ],
        "items": {
          "kpath": "array of [kx, ky, kz] (floats)",
          "bands": "array of arrays of float (eV)"
        }
      },
      "description": "Band eigenvalues of the O/V system along M‑Γ‑K; checked for a linear Dirac cone crossing at Γ and Fermi level alignment."
    }
  ],
  "notes": "All energies are in eV. The checker compares results.json entries to hidden paper values with a tolerance. band_structure_O_V.json is audited for the Dirac cone feature."
}
```

## How you are scored
A hidden verifier will evaluate your submitted artifacts. For results.json, the verifier will compare your reported E_ads, E_Fermi, and reaction energies against the expected values with appropriate tolerances; meeting the tolerances yields full credit for that quantity, while larger errors reduce the score proportionally. For band_structure_O_V.json, the verifier will check the structure (k‑point path and band shape) and verify that the eigenvalues exhibit a linear Dirac cone crossing at the Γ point and that the Fermi level is correctly aligned. Each artifact contributes a defined share of the total reward. The verifier does not re‑run your DFT calculations; it only reads your JSON files. Therefore, simply reporting numbers without actually performing the full computational workflow would not yield correct values, as the expected results correspond to the outcomes of a faithful DFT reproduction.
