# DFT+U Electronic Structure and Magnetism of Eu-Doped GaN

## Problem background
Gallium nitride (GaN) is a wide-bandgap III-nitride semiconductor with potential for spintronics and light-emitting devices. Doping GaN with rare-earth ions such as europium (Eu) introduces localized 4f states that can spin-polarize the host crystal, leading to magnetic moments and unique electronic features. Understanding the positions of the Eu 4f levels relative to the Fermi energy, the exchange splittings they induce, and the resulting magnetic moments is essential for interpreting the material's optical and magnetic properties. In this task, you will compute the electronic structure and magnetism of Eu-doped GaN at a doping level of x = 0.0625 in the zinc-blende phase using density functional theory with a Hubbard +U correction (LDA+U). The goal is to produce a set of key quantities that characterise the ferromagnetic state, which will be compared against hidden reference values obtained from the original published study.

## Approach
The computational approach is first-principles DFT+U within the supercell approximation. A 32-atom zinc-blende GaN supercell is constructed with one Ga atom replaced by Eu (composition Ga0.9375Eu0.0625N) at the experimental lattice constant 4.51 Å. The calculation is spin-polarised and assumes ferromagnetic alignment of the Eu spins. The strongly correlated Eu 4f electrons are treated with the LDA+U method (Dudarev formulation), using on-site Coulomb and exchange parameters U=0.44 Ry and J=0.07 Ry, corresponding to an effective Ueff = U − J = 0.37 Ry. Any open-source DFT code capable of LDA+U (e.g., Quantum ESPRESSO) and appropriate pseudopotentials that include the Eu 4f states can be used.

After a self-consistent calculation, the total and projected density of states (DOS) are obtained. From the projected DOS, the Eu 4f spin-up (majority) peak and the Eu 4f spin-down (minority) peaks are identified. The effective f-band exchange splitting Δₓ(f) is computed as the energy separation between the corresponding spin-up and spin-down peaks. The valence-band maximum exchange splitting Δ = E_v↑ − E_v↓ is extracted from the spin-resolved valence band edges. Exchange constants N₀α (conduction band) and N₀β (valence band) are derived from the spin splitting of the band edges. Finally, the total magnetic moment of the supercell and the local magnetic moments on Eu, N, Ga atoms and in the interstitial region are computed (e.g., via Bader or Mulliken analysis). All extracted quantities are written to a JSON file.

## Reproduction target
Perform a spin-polarised self-consistent LDA+U calculation on the zinc-blende Ga0.9375Eu0.0625N 32-atom supercell (one Eu substitutional impurity, lattice constant 4.51 Å) using Hubbard parameters U=0.44 Ry, J=0.07 Ry (Ueff = 0.37 Ry). From the resulting electronic structure, extract:
- Eu 4f spin-up peak centre energy (eV)
- Eu 4f spin-down peak energies (up to two peaks, eV)
- Effective f-band exchange splitting Δₓ(f) (eV)
- Valence-band maximum exchange splitting Δ (eV)
- Exchange constants N₀α and N₀β (eV)
- Total magnetic moment per supercell (μB)
- Local magnetic moments on Eu, N, Ga, and in the interstitial region (μB).

Report all quantities in a single JSON file `/app/outputs/results.json` following the exact schema defined in the output contract. The hidden verifier will compare your reported values to reference values from the original study using appropriate absolute tolerances.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library: https://www.materialscloud.org/discover/sssp/table/efficiency
- Atomic Simulation Environment (ASE): https://wiki.fysik.dtu.dk/ase/

## Workflow steps

### Step 1: Self-consistent LDA+U calculation
- Role: process
- Action: Construct the 32-atom supercell of zinc-blende Ga0.9375Eu0.0625N (one Eu substitute Ga, lattice constant 4.51 Å) and run a spin-polarized self-consistent LDA+U calculation (ferromagnetic) with U_eff = 0.37 Ry (U=0.44 Ry, J=0.07 Ry). Obtain self-consistent charge density, spin density, band structure, total and projected density of states (DOS), and total energy.
- Evidence: `/app/outputs/dft_scf.log`

### Step 2: Extract electronic and magnetic properties
- Role: scored (load-bearing)
- Action: From the DFT outputs, extract: (a) Eu 4f spin-up (majority) peak centre energy, (b) Eu 4f spin-down (minority) peak energies (up to two peaks), (c) effective f-band exchange splitting Δ_x(f) as the energy separation between the corresponding spin-up and spin-down peaks, (d) valence-band maximum exchange splitting Δ = E_v↑ − E_v↓, (e) exchange constants N0α and N0β computed from the spin splitting of the conduction- and valence-band edges, (f) total magnetic moment per supercell, and (g) local magnetic moments on Eu, N, Ga, and in the interstitial region. Write all quantities to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with required fields: eu_4f_up_peak_energy (number, eV), eu_4f_down_peak_energy1 (number, eV), eu_4f_down_peak_energy2 (number, optional), f_band_exchange_splitting (number, eV), valence_band_exchange_splitting (number, eV), N0_alpha (number, eV), N0_beta (number, eV), total_magnetic_moment (number, μB), eu_magnetic_moment (number, μB), n_magnetic_moment (number, μB), ga_magnetic_moment (number, μB), interstitial_magnetic_moment (number, μB).
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
- target_policy: exact_match
- description: All key electronic and magnetic quantities reproduced from the LDA+U calculation, for comparison against hidden paper-reported reference values with tolerances.
- schema:
  - `type`: object
  - `required`: `eu_4f_up_peak_energy`, `eu_4f_down_peak_energy1`, `f_band_exchange_splitting`, `valence_band_exchange_splitting`, `N0_alpha`, `N0_beta`, `total_magnetic_moment`, `eu_magnetic_moment`, `n_magnetic_moment`, `ga_magnetic_moment`, `interstitial_magnetic_moment`
  - `properties`:
    - `eu_4f_up_peak_energy`:
      - `type`: number
      - `units`: eV
    - `eu_4f_down_peak_energy1`:
      - `type`: number
      - `units`: eV
    - `eu_4f_down_peak_energy2`:
      - `type`: number
      - `units`: eV
    - `f_band_exchange_splitting`:
      - `type`: number
      - `units`: eV
    - `valence_band_exchange_splitting`:
      - `type`: number
      - `units`: eV
    - `N0_alpha`:
      - `type`: number
      - `units`: eV
    - `N0_beta`:
      - `type`: number
      - `units`: eV
    - `total_magnetic_moment`:
      - `type`: number
      - `units`: μB
    - `eu_magnetic_moment`:
      - `type`: number
      - `units`: μB
    - `n_magnetic_moment`:
      - `type`: number
      - `units`: μB
    - `ga_magnetic_moment`:
      - `type`: number
      - `units`: μB
    - `interstitial_magnetic_moment`:
      - `type`: number
      - `units`: μB

Notes: The lattice constant is provided (4.51 Å); no volume optimization is required. The spin-density difference contour plot is qualitative and not numerically scored.

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
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "eu_4f_up_peak_energy",
          "eu_4f_down_peak_energy1",
          "f_band_exchange_splitting",
          "valence_band_exchange_splitting",
          "N0_alpha",
          "N0_beta",
          "total_magnetic_moment",
          "eu_magnetic_moment",
          "n_magnetic_moment",
          "ga_magnetic_moment",
          "interstitial_magnetic_moment"
        ],
        "properties": {
          "eu_4f_up_peak_energy": {
            "type": "number",
            "units": "eV"
          },
          "eu_4f_down_peak_energy1": {
            "type": "number",
            "units": "eV"
          },
          "eu_4f_down_peak_energy2": {
            "type": "number",
            "units": "eV"
          },
          "f_band_exchange_splitting": {
            "type": "number",
            "units": "eV"
          },
          "valence_band_exchange_splitting": {
            "type": "number",
            "units": "eV"
          },
          "N0_alpha": {
            "type": "number",
            "units": "eV"
          },
          "N0_beta": {
            "type": "number",
            "units": "eV"
          },
          "total_magnetic_moment": {
            "type": "number",
            "units": "μB"
          },
          "eu_magnetic_moment": {
            "type": "number",
            "units": "μB"
          },
          "n_magnetic_moment": {
            "type": "number",
            "units": "μB"
          },
          "ga_magnetic_moment": {
            "type": "number",
            "units": "μB"
          },
          "interstitial_magnetic_moment": {
            "type": "number",
            "units": "μB"
          }
        }
      },
      "description": "All key electronic and magnetic quantities reproduced from the LDA+U calculation, for comparison against hidden paper-reported reference values with tolerances."
    }
  ],
  "notes": "The lattice constant is provided (4.51 Å); no volume optimization is required. The spin-density difference contour plot is qualitative and not numerically scored."
}
```

## How you are scored
Your submission is scored entirely on the contents of `/app/outputs/results.json`. A hidden verifier reads each required numeric field and compares it to a hidden reference value (the paper‑reported result for the same quantity) with a pre‑set absolute tolerance. Each field that falls within tolerance earns partial credit. The final reward is the fraction of required fields that meet the tolerance (a float between 0 and 1). Fields marked as optional in the output contract are ignored if absent. Tolerances are chosen to account for known differences between implementations (e.g., WIEN2k vs. Quantum ESPRESSO) while still requiring a genuine DFT+U reproduction; they are not disclosed to you. You must produce structurally valid JSON that contains every required field; missing or malformed fields score zero for that field.
