# Magnetic susceptibility of alpha-plutonium from LDA+U+SO DFT

## Problem background
Alpha-plutonium (α-Pu) is a low-symmetry monoclinic phase of plutonium with 16 atoms per unit cell. Its electronic structure is dominated by strong 5f-electron correlations and large spin-orbit coupling. Experimentally, the magnetic susceptibility of α-Pu shows a temperature-independent component plus a low-temperature rise from impurities, but the separate spin and orbital contributions cannot be measured directly. This work uses first-principles DFT (LDA+U with spin-orbit coupling) to compute the partial density of states and then derives the exchange-enhanced Pauli spin susceptibility and the Van Vleck orbital susceptibility. The goal is to compute those two contributions at 300 K and 100 K and to examine whether they are nearly temperature independent.

## Approach
The electronic structure of α-Pu (monoclinic P2₁/m, 16 atoms, lattice parameters and positions as in Espinosa et al., Phys. Rev. B 63, 174111 (2001)) is calculated with an LDA+U+SO DFT code (e.g., Quantum ESPRESSO, Elk, GPAW) using U_f=4 eV, J_H=0.48 eV, U_d=2 eV, and full spin-orbit coupling. From the self-consistent calculation the partial densities of states at the Fermi level g^(f)(μ), g^(d)(μ), g^(sp)(μ) and the 5f and 6d occupation numbers are extracted.

The spin susceptibility is then obtained from an enhanced-Pauli model:
χ_s = χ^(f) + χ^(sp) + I χ^(f) χ^(d),
with χ^(l) = 2 g^(l)(μ) D^(l) and the Stoner enhancement factor D^(l) = [1 − U^(l) g^(l)(μ)]⁻¹. The inter-site f–d exchange parameter is taken as I = 0.1 U_f.

The orbital susceptibility follows a modified Van Vleck expression:
χ_orb^(l) = 2 Σ_{α,α′} n_l (N_l − n_l) / { N_l [Δ_l + U^(l) m^(l) (α−α′)] },
where N_f=14, N_d=10 are the orbital degeneracies, Δ_f=4 eV and Δ_d=15 eV are average multiplet splittings, and the spin-fluctuation amplitude is m^(l) = (T χ^(l))^(1/2).

Both contributions are evaluated at T=300 K and T=100 K to assess temperature independence.

## Reproduction target
Compute the spin susceptibility χ_s and orbital susceptibility χ_orb of α-Pu at T=300 K and T=100 K from a DFT LDA+U+SO electronic structure calculation, and demonstrate that both contributions are temperature independent (i.e., their values at 100 K and 300 K differ by less than 10%).

## Assets

- α-Pu crystal structure (monoclinic P2_1/m, 16 atoms/cell): 10.1103/PhysRevB.63.174111
- DFT code with LDA+U+SO (e.g., Quantum ESPRESSO, Elk, GPAW): https://www.quantum-espresso.org

## Workflow steps

### Step 1: DFT electronic structure calculation
- Role: process
- Action: Run a self-consistent LDA+U+SO calculation for α-Pu in the monoclinic P2_1/m structure (16 atoms) using U_f=4 eV, J_H=0.48 eV, U_d=2 eV, including spin-orbit coupling. Obtain total and partial (5f, 6d, sp) density of states.
- Evidence: `/app/outputs/step_01_dos.json`

### Step 2: Extract Fermi-level partial DOS and occupations
- Role: process
- Action: From the computed DOS, extract the partial densities of states at the Fermi level g^{(f)}(μ), g^{(d)}(μ), g^{(sp)}(μ) and the occupation numbers n_f, n_d.
- Evidence: `/app/outputs/step_02_Fermi_level.json`

### Step 3: Compute spin and orbital susceptibilities
- Role: scored (load-bearing)
- Action: Compute spin susceptibility χ_s using the Pauli/enhanced formula and orbital susceptibility χ_orb using the modified Van Vleck formula at T=300 K and T=100 K. Use the Fermi-level DOS values, U^{(f)}=4 eV, U^{(d)}=2 eV, inter-site exchange I=0.1 U_f, orbital degeneracies N_f=14, N_d=10, average multiplet splittings Δ_f=4 eV, Δ_d=15 eV, and spin-fluctuation amplitude m^{(l)} = sqrt(T χ^{(l)}). Write results as JSON.
- Output file: `/app/outputs/step_03_susceptibility.json`
- Format: json
- Contract: JSON object with keys: chi_spin_300K (float, emu/mol), chi_orb_300K (float, emu/mol), chi_spin_100K (float, emu/mol), chi_orb_100K (float, emu/mol).
- Scoring: scored by hidden verifier

### Step 4: Compute impurity contribution
- Role: process
- Action: Using the Curie‑Weiss law with impurity parameters (Fe spin S=3/2, g‑factor, θ=−4 K, concentration ~200 ppm), compute the impurity susceptibility χ_imp(T) for a temperature range. Produce a data file.
- Evidence: `/app/outputs/step_04_impurity.json`

### Step 5: Assemble total susceptibility and compare with experiment
- Role: process
- Action: Sum spin, orbital, and impurity contributions to obtain total χ(T). Compare with published experimental data from McCall et al. (2006); generate a plot.
- Evidence: `/app/outputs/step_05_total_susceptibility.png`

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_03_susceptibility.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_03_susceptibility.json
- path: `/app/outputs/step_03_susceptibility.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Spin and orbital susceptibilities at 300 K and 100 K. The checker compares these values to paper-reported references with tolerance and verifies that both contributions are temperature‑independent (relative change ≤10%).
- schema:
  - `type`: object
  - `required`:
    - `chi_spin_300K`: float (emu/mol)
    - `chi_orb_300K`: float (emu/mol)
    - `chi_spin_100K`: float (emu/mol)
    - `chi_orb_100K`: float (emu/mol)
  - `units`:
    - `chi_spin_300K`: emu/mol
    - `chi_orb_300K`: emu/mol
    - `chi_spin_100K`: emu/mol
    - `chi_orb_100K`: emu/mol

Notes: Steps 04 and 05 are included for workflow completeness but are not scored. The scoring is result-level (T0) with hidden tolerances against the paper's numbers and a structural temperature‑independence check.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_03_susceptibility.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "chi_spin_300K": "float (emu/mol)",
          "chi_orb_300K": "float (emu/mol)",
          "chi_spin_100K": "float (emu/mol)",
          "chi_orb_100K": "float (emu/mol)"
        },
        "units": {
          "chi_spin_300K": "emu/mol",
          "chi_orb_300K": "emu/mol",
          "chi_spin_100K": "emu/mol",
          "chi_orb_100K": "emu/mol"
        }
      },
      "description": "Spin and orbital susceptibilities at 300 K and 100 K. The checker compares these values to paper-reported references with tolerance and verifies that both contributions are temperature‑independent (relative change ≤10%)."
    }
  ],
  "notes": "Steps 04 and 05 are included for workflow completeness but are not scored. The scoring is result-level (T0) with hidden tolerances against the paper's numbers and a structural temperature‑independence check."
}
```

## How you are scored
The hidden verifier independently checks the artifact `/app/outputs/step_03_susceptibility.json`. It compares the reported `chi_spin_300K` and `chi_orb_300K` to hidden reference values with an appropriate tolerance, and verifies that both spin and orbital susceptibilities satisfy the temperature-independence condition (relative change between 100 K and 300 K ≤ 10%). The final reward is computed from these checks; simply reporting plausible numbers does not guarantee a high score.
