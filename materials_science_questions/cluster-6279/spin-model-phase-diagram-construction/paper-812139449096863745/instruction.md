## Problem background

Liquid crystal compounds like 65OBC and related series exhibit a smectic‑A to hexatic‑B (SmA–HexB) transition with specific heat exponents that deviate strongly from the 3D XY universality class. Bruinsma and Aeppli proposed a model Hamiltonian that couples two XY order parameters — one for hexatic bond‑orientational order (Ψ) and one for herringbone order (Φ) — to explain the anomalous critical behaviour. This task reproduces the finite‑temperature phase diagram of that coupled XY model in the strong‑coupling regime using large‑scale Monte Carlo simulations and finite‑size scaling analysis.

## Approach

The system is described by the Bruinsma–Aeppli Hamiltonian on a three‑dimensional simple cubic lattice:

H = −J₁ Σ cos(Ψ_i − Ψ_j) − J₂ Σ cos(Φ_i − Φ_j) − J₃ Σ cos(Ψ_i − 3 Φ_i)

where the sums over ⟨ij⟩ are over nearest‑neighbour pairs, and J₁, J₂ are coupling constants for Ψ and Φ, respectively, while J₃ is an onsite coupling that locks the two order parameters. In this work J₁ = 1.0 and J₃ = 3.0 are held fixed, and J₂ is varied to map the phase diagram.

The strategy is:
1.  Use the Metropolis algorithm with single‑spin flips to simulate the model on lattices of linear size L.
2.  Combine energy histograms collected at several nearby temperatures via the Ferrenberg–Swendsen multihistogram reweighting technique to obtain high‑resolution curves of the specific heat and the Binder fourth‑energy cumulant.
3.  Apply finite‑size scaling laws to the size‑dependent quantities (specific heat maxima, cumulant minima, and effective transition temperatures) to extract infinite‑size transition temperatures and classify each transition as first or second order.
4.  Assemble the phase diagram by reporting, for each J₂, the transition(s) and their order.

The execution is computational; the agent implements the Hamiltonian, the simulation protocol, the reweighting analysis, and the scaling fits from scratch.

## Reproduction target

For the Bruinsma–Aeppli Hamiltonian with J₁ = 1.0, J₃ = 3.0, compute the transition temperature(s) and the order (first or second) for the J₂ values 0.5, 0.7, 0.8, 0.9, 1.0, 1.2. Identify the critical end point where the two separate transition lines merge (this is expected to occur near J₂ = 0.9).

Produce a CSV file `phase_diagram.csv` that contains the final phase diagram. For each J₂, list every thermodynamic phase transition that occurs (disordered → hexatic, hexatic → locked, or disordered → locked) along with its bulk transition temperature T_c (in units of J₁) and order. The file must adhere to the output contract described below.

## Assets

- **numpy**: standard numerical Python library, install via pip.
- **scipy**: optional, for least‑squares fitting of scaling relations; install via pip.
- No external datasets or pretrained models are required; all simulations are self‑contained.

## Workflow steps

### Step 1: Low‑resolution Metropolis Monte Carlo survey
- Role: process
- Action: Run low‑resolution Metropolis simulations of the BA Hamiltonian on a 3D cubic lattice with linear sizes L = 6, 7, 8, 9, 10, 12. For each J₂ value (0.5, 0.7, 0.8, 0.9, 1.0, 1.2), perform a coarse temperature sweep to roughly locate the transition regions. Use standard single‑spin‑flip updates, tuning angle‑step sizes to achieve roughly 50 % acceptance. Use an equilibration of at least 100 000 Monte Carlo sweeps (MCS) per temperature and collect data for at least 200 000 MCS. Record the approximate temperature windows where the specific heat peaks occur.
- Evidence: none

### Step 2: High‑resolution multihistogram Monte Carlo simulations
- Role: process
- Action: For each J₂ and each lattice size L = 6, 8, 10, 12, perform multiple independent Metropolis simulations at several temperatures chosen around each transition identified in Step 1. Equilibrate for at least 5 × 10⁵ MCS and collect data for at least 1 × 10⁶ MCS per temperature, discarding 10–20 sweeps between measurements to reduce temporal correlations. For each temperature, record the energy histogram (the frequency of energy values) — these histograms are the input for the reweighting step.
- Evidence: none

### Step 3: Histogram reweighting and extraction of size‑dependent quantities
- Role: process
- Action: Combine the energy histograms from Step 2 using the Ferrenberg–Swendsen multihistogram algorithm to obtain continuous, high‑resolution curves of the specific heat C(T) and the Binder fourth‑energy cumulant U_L(T) for each (J₂, L) combination. Identify, for each transition feature, the maximum of the specific heat (C_max), the minimum of the Binder cumulant (U_min), and the effective transition temperature T_c(L) from the location of these extrema. Standardise the energy range (20 000 bins is sufficient). These size‑dependent quantities are the input to the finite‑size scaling analysis in the next step.
- Evidence: none

### Step 4: Finite‑size scaling and phase‑diagram assembly (load‑bearing)
- Role: scored (load‑bearing)
- Action: For each J₂ and each transition identified in the data, fit the size‑dependent quantities C_max(L), U_min(L), and T_c(L) to the appropriate finite‑size scaling laws:
    • For a continuous transition: C_max(L) ∼ c₁ + c₂ L^{α/ν}, T_c(L) ∼ T_c(∞) + A L^{−1/ν};
    • For a first‑order transition: C_max(L) ∼ c₁ + c₂ L³, T_c(L) ∼ T_c(∞) + A L^{−3}.
  Use the extrapolated cumulant U* to decide the order: U* = 2/3 indicates a continuous transition; U* < 2/3 indicates a first‑order transition. Determine the infinite‑size transition temperature T_c(∞) (in units of J₁) and the order (“second” or “first”) for each distinct line.
  Assemble the results into a CSV file `/app/outputs/phase_diagram.csv` according to the output contract. For J₂ values below the critical end point (expected near J₂ = 0.9) two transitions are present: an isotropic→hexatic (I‑H) line and a hexatic→locked (H‑L) line; for J₂ at and above the critical end point, only a single isotropic→locked (I‑L) transition appears.
- Output file: `/app/outputs/phase_diagram.csv`
- Format: csv
- Contract: CSV with header exactly: `J2,transition,Tc,order`
  • `J2`: floating‑point value of the coupling J₂.
  • `transition`: string, one of `I-H` (isotropic to hexatic), `H-L` (hexatic to locked), `I-L` (isotropic to locked).
  • `Tc`: floating‑point transition temperature in units of J₁.
  • `order`: string, `second` or `first`.
  For each J₂ < 0.9 two rows (I‑H and H‑L) are expected; for J₂ ≥ 0.9 one row (I‑L) is expected. The I‑H row, when present, must list a higher Tc than the H‑L row.
- Scoring: scored by hidden verifier

## Output files

- `/app/outputs/phase_diagram.csv` – the final phase diagram.

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_diagram.csv
- path: `/app/outputs/phase_diagram.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Phase diagram containing the transition temperatures and orders for the BA model. The verifier compares each row's Tc and order to hidden reference values from the paper.
- schema:
  - `type`: table
  - `required_columns`: `J2`, `transition`, `Tc`, `order`
  - `units`:
    - `Tc`: units of J1

Notes: The verifier checks structural properties: for J2<0.9 two transitions present with I-H at higher Tc; for J2>=0.9 only I-L present. The critical end point is the I-L row at J2=0.9.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_diagram.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "J2",
          "transition",
          "Tc",
          "order"
        ],
        "units": {
          "Tc": "units of J1"
        }
      },
      "description": "Phase diagram containing the transition temperatures and orders for the BA model. The verifier compares each row's Tc and order to hidden reference values from the paper."
    }
  ],
  "notes": "The verifier checks structural properties: for J2<0.9 two transitions present with I-H at higher Tc; for J2>=0.9 only I-L present. The critical end point is the I-L row at J2=0.9."
}
```

## How you are scored

A hidden verifier reads your `/app/outputs/phase_diagram.csv`. It independently checks:
- That the expected rows (J₂, transition, Tc, order) are present and correctly structured.
- That for each J₂ and transition type, the reported Tc lies within an acceptable tolerance of the reference value and that the reported order matches the known order.
- That the phase diagram’s topology is correct (two distinct transitions for J₂ < 0.9, a single transition for J₂ ≥ 0.9, and the correct ordering of the transition temperatures).

No other files are scored. Simply reporting a number from the literature without running the full simulation pipeline will not satisfy the verifier’s checks.
