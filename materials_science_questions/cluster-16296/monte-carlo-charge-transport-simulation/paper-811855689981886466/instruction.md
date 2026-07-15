# Expected energy departure from Lorentzian collision broadening in silicon

## Problem background
In semiclassical Monte Carlo simulation of electron transport, collision broadening is often modeled by a Lorentzian energy distribution for the final state after scattering. Because the electronic density of states (DOS) in a real semiconductor like silicon is not constant in energy, the symmetric Lorentzian distribution can lead to a systematic departure from average energy conservation over many scattering events. This task quantifies that expected departure using a simplified effective‑mass model for the silicon DOS and tests a corrected distribution that accounts for the DOS shape.

## Approach
The reproduction proceeds in two stages. First, a density of states g(E) for silicon is constructed from a multi‑valley effective mass model: conduction band valleys with transverse mass m_t=0.19 m_e and longitudinal mass m_l=0.98 m_e, and light/heavy hole bands with m_lh=0.16 m_e and m_hh=0.49 m_e. Standard three‑dimensional DOS formulas are summed to produce a smooth g(E) curve over 0–4 eV, saved as a CSV for evidence. Second, for a range of initial electron energies E_i, the expected final energy ⟨E_f⟩ is computed by numerical integration. Two distributions are considered: (i) the Lorentzian broadening line‑shape centered at E_i+ω_o (with ω_o=63 meV and width Γ=10 meV), weighted by g(E) as in the usual collision broadening formulation; (ii) a corrected line‑shape obtained by dividing the Lorentzian by the DOS (which cancels the DOS dependence in the expectation integral). For each case the departure Δ = ⟨E_f⟩ − (E_i+ω_o) (in meV) is computed. The comparison reveals whether the DOS non‑uniformity causes a systematic error and whether dividing by the DOS removes it.

## Reproduction target
Produce a CSV file `/app/outputs/departure_results.csv` containing the computed expected energy departures for the original Lorentzian and the corrected distribution. The file must have the columns: initial_energy (eV), departure_original (meV), departure_corrected (meV). Include rows for initial energies E_i = 0.1, 0.2, …, 4.0 eV, obtained by numerical integration as described above.

## Assets

- NumPy: numpy
- SciPy: scipy
- Silicon effective mass parameters

## Workflow steps

### Step 1: Compute effective-mass density of states for silicon
- Role: process
- Action: Compute the electronic density of states (DOS) g(E) for silicon over an energy range covering 0–4 eV using a multi-valley effective mass model. Model three equivalent X-conduction band valleys with transverse mass m_t=0.19 m_e and longitudinal mass m_l=0.98 m_e, and light/heavy hole valence bands with masses m_lh=0.16 m_e and m_hh=0.49 m_e. Use standard three-dimensional DOS formulas per valley, sum contributions, and produce a smooth g(E) curve. Save the DOS curve to a CSV file dos.csv for evidence.
- Evidence: `/app/outputs/dos.csv`

### Step 2: Compute expected departure from energy conservation
- Role: scored (load-bearing)
- Action: Using the DOS g(E) from step_01, optical phonon energy ω_o=63 meV, and a constant collisional broadening width Γ=10 meV, compute for initial electron energies E_i from 0.1 to 4.0 eV in steps of 0.1 eV the expected final energy departure. Compute ΔE_orig = ⟨E_f⟩_Lorentzian − (E_i+ω_o) by numerically integrating the Lorentzian-weighted DOS expression, and ΔE_corr = ⟨E_f⟩_corrected − (E_i+ω_o) by integrating the distribution Lorentzian divided by the DOS. Convert all energies to meV. Output a CSV file departure_results.csv with columns: initial_energy (eV), departure_original (meV), departure_corrected (meV).
- Output file: `/app/outputs/departure_results.csv`
- Format: csv
- Contract: CSV with header: initial_energy, departure_original, departure_corrected. initial_energy in eV (float), departure_original and departure_corrected in meV (float). Rows for E_i = 0.1, 0.2, ..., 4.0 eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/departure_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### departure_results.csv
- path: `/app/outputs/departure_results.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Expected energy departures from energy conservation for original Lorentzian and corrected distributions as a function of initial electron energy.
- schema:
  - `type`: table
  - `required_columns`: `initial_energy`, `departure_original`, `departure_corrected`
  - `units`:
    - `initial_energy`: eV
    - `departure_original`: meV
    - `departure_corrected`: meV

Notes: The scoring checks structural properties of the output CSV and applies hidden physical checks. The checker may also use optional dos.csv evidence.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "departure_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "initial_energy",
          "departure_original",
          "departure_corrected"
        ],
        "units": {
          "initial_energy": "eV",
          "departure_original": "meV",
          "departure_corrected": "meV"
        }
      },
      "description": "Expected energy departures from energy conservation for original Lorentzian and corrected distributions as a function of initial electron energy."
    }
  ],
  "notes": "The scoring checks structural properties of the output CSV and applies hidden physical checks. The checker may also use optional dos.csv evidence."
}
```

## How you are scored
Your submission is evaluated by an automated hidden verifier. It checks that `/app/outputs/departure_results.csv` exists, has the correct columns and format, and contains a row for every required initial energy. The verifier scores the departures against hidden physical expectations. The scoring thresholds are hidden. Simply reporting reference numbers without performing the integration will not achieve a high score.
