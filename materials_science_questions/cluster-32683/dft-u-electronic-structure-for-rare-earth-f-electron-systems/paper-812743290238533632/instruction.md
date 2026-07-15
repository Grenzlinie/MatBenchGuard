# Fully relativistic KKR band structure calculation for SmTe

## Problem background
Samarium telluride (SmTe) is a rare-earth monochalcogenide that exhibits intermediate valence and undergoes a semiconductor-to-metal transition under pressure. A first-principles understanding of its electronic structure is essential for interpreting its transport and magnetic properties. In its NaCl low-pressure phase, the electronic bands are expected to show an indirect gap and a set of narrow f‑bands near the Fermi level. This task performs a fully relativistic band-structure calculation to determine three key quantities: the indirect band gap across the Brillouin zone, the direct band gap at the X point, and the energy position of the top of the f‑band at the Γ point.

## Approach
The calculation uses the Korringa–Kohn–Rostoker (KKR) method with full relativity. A crystal muffin-tin potential is constructed by superimposing self-consistent atomic charge densities for Sm and Te, scaling the exchange by α = 0.71, determining muffin-tin radii from the intersection of potential curves, and using a constant interstitial potential of −0.39 Ryd. The α‑expansion includes 14 neighbour shells for the NaCl structure (lattice parameter 12.46 au). Inside the muffin‑tin spheres the Dirac equation is solved with a bi-spinor expansion up to l = 3, and the secular KKR problem is solved for each irreducible representation of the double group at k‑points covering the 1/48 irreducible wedge of the FCC Brillouin zone. The resulting energy bands are analysed at high‑symmetry points Γ and X to extract the indirect gap, the direct gap at X, and the energy of the top of the f‑band at Γ8⁻ relative to the interstitial potential.

## Reproduction target
Compute the following three quantities from the fully relativistic KKR band structure of SmTe in the NaCl structure, using the parameters specified in the workflow steps: (1) the indirect band gap between the valence band maximum at Γ8⁻ and the conduction band minimum at X7⁺, in electronvolts (eV); (2) the direct band gap at the X point between the X7⁻ and X7⁺ states, in eV; (3) the energy of the top of the f‑band at Γ8⁻ measured from the interstitial potential, in Rydberg. Write all three values as a single JSON object with keys `indirect_gap`, `direct_gap_X`, and `f_band_top` and save it to `/app/outputs/band_gaps.json`.

## Assets

- Fully relativistic KKR code (SPR-KKR or equivalent): https://www.ebert.cup.uni-muenchen.de/en/software-en/spring-kkr

## Workflow steps

### Step 1: Build muffin-tin potential
- Role: process
- Action: Construct the SmTe crystal muffin-tin potential: perform self-consistent atomic calculations for Sm and Te to obtain atomic charge densities, superimpose them to form the crystal potential, scale exchange by alpha=0.71, determine muffin-tin radii from potential curve intersections, set constant interstitial potential to -0.39 Ryd, and expand over 14 neighbour shells. The lattice parameter is 12.46 au (NaCl structure).
- Evidence: `/app/outputs/potential_log.txt`

### Step 2: Run fully relativistic KKR calculation
- Role: process
- Action: Using the constructed muffin-tin potential, run a fully relativistic KKR band-structure calculation that solves the full Dirac equation inside muffin-tin spheres with a bi-spinor expansion up to l=3, solves the secular KKR problem for each irreducible representation of the double group for k-points in the 1/48 irreducible wedge of the FCC Brillouin zone, and aims for numerical accuracy of about 10^-3 Ryd. Obtain energy bands at high-symmetry points and general k-points.
- Evidence: `/app/outputs/bands_output.txt`

### Step 3: Extract band gaps and f-band position
- Role: scored (load-bearing)
- Action: From the computed energy bands, determine the indirect band gap between the valence band maximum at Gamma8- and the conduction band minimum at X7+ (in eV), the direct band gap at X between X7- and X7+ (in eV), and the energy of the top of the f-band at Gamma8- relative to the interstitial potential (in Ryd). Write these three values as a JSON object.
- Output file: `/app/outputs/band_gaps.json`
- Format: json
- Contract: type=object; required=['indirect_gap', 'direct_gap_X', 'f_band_top']; properties={'indirect_gap': {'type': 'number', 'units': 'eV'}, 'direct_gap_X': {'type': 'number', 'units': 'eV'}, 'f_band_top': {'type': 'number', 'units': 'Ryd'}}
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
- description: Scored JSON file containing the computed indirect band gap (Gamma to X), direct band gap at X, and the energy of the top of the f-band at Gamma8- relative to the interstitial potential.
- schema:
  - `type`: object
  - `required`: `indirect_gap`, `direct_gap_X`, `f_band_top`
  - `items`: object
  - `properties`:
    - `indirect_gap`:
      - `type`: number
      - `units`: eV
    - `direct_gap_X`:
      - `type`: number
      - `units`: eV
    - `f_band_top`:
      - `type`: number
      - `units`: Ryd

Notes: The checker compares each reported value to hidden reference values within tolerances that absorb legitimate toolchain spread. The solving agent must execute the full KKR workflow; a result-level comparison is used because recomputing the KKR run in the verifier sandbox is infeasible.

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
        "required": [
          "indirect_gap",
          "direct_gap_X",
          "f_band_top"
        ],
        "items": {},
        "properties": {
          "indirect_gap": {
            "type": "number",
            "units": "eV"
          },
          "direct_gap_X": {
            "type": "number",
            "units": "eV"
          },
          "f_band_top": {
            "type": "number",
            "units": "Ryd"
          }
        }
      },
      "description": "Scored JSON file containing the computed indirect band gap (Gamma to X), direct band gap at X, and the energy of the top of the f-band at Gamma8- relative to the interstitial potential."
    }
  ],
  "notes": "The checker compares each reported value to hidden reference values within tolerances that absorb legitimate toolchain spread. The solving agent must execute the full KKR workflow; a result-level comparison is used because recomputing the KKR run in the verifier sandbox is infeasible."
}
```

## How you are scored
A hidden verifier checks your `band_gaps.json` file. The verifier reads the three quantities you report and compares each one to a hidden reference value derived from the paper’s published band-structure results. The comparison uses numerical tolerances that account for the expected spread between different KKR implementations. For each quantity, full credit is awarded if your computed value lies within the tolerance band; if it falls outside, the score decreases smoothly with increasing deviation (never penalising a value that is strictly better than the reference). The final reward is the average of the three per-quantity scores. The verifier does not re-run the expensive KKR calculation; it trusts the numbers you report, so you must actually perform the band-structure computation — simply copying the paper’s numbers will not pass the hidden comparison.
