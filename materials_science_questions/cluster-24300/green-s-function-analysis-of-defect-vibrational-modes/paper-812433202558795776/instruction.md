# Localized vibrational mode frequencies in a nine-atom CsCl-type defect cluster

## Problem background
U centres are substitutional H⁻ or D⁻ impurities in caesium iodide (CsI). To understand their vibrational properties, a molecular model that treats only the impurity and its eight nearest‑neighbour ions (a nine‑atom CsCl‑type defect cluster) is used. The cluster's vibrational spectrum is obtained from a real symmetric 27×27 dynamical matrix that includes Coulomb interactions and central short‑range forces between nearest neighbours. The highest triply‑degenerate eigenvalue corresponds to the localised mode in which the light impurity vibrates against an almost static surrounding cage. The frequency of this localised mode depends sensitively on the defect short‑range force‑constant parameter A′, which measures the weakening of the bonds around the impurity. This task computes those localised mode frequencies for H⁻ and D⁻ impurities across a range of A′ values, providing quantitative predictions that are useful for interpreting experimental infra‑red data.

## Approach
The molecular model is built for a CsCl‑type lattice where each ion has eight nearest neighbours of the opposite species. In the defect cluster, a central impurity (site 0 at r₀(000)) is surrounded by eight host ions at the corners of a cube: sites 1–8 at r₀(111), r₀(¯1¯1¯1), r₀(¯111), r₀(1¯1¯1), r₀(1¯11), r₀(¯11¯1), r₀(11¯1), r₀(¯1¯11). The half‑lattice constant r₀ = 2.282 Å. The ions carry charges ±1 (in units of the elementary charge e = 4.803×10⁻¹⁰ esu); masses are M_Cs = 132.9 u, M_I = 126.9 u, and for the impurities M_H = 1.0 u, M_D = 2.0 u.

The host short‑range parameters A and B are first obtained from the lattice condition and compressibility. Using the bulk modulus K = 1/k with compressibility k = 1.441×10¹¹ dyn cm⁻², and the Madelung constant α = 1.7627, one computes A = (3 r₀ K) · (8 r₀³/e²) + (2α)/(3√3) and B = –α/(3√3). All quantities must be expressed in consistent CGS units (r₀ converted to cm: 1 Å = 10⁻⁸ cm). The defect short‑range parameter A′ is varied; it is assumed that B′ = B (no relaxation).

The 27‑dimensional dynamical matrix D is built atom‑by‑atom. Its general element is D_{αα′}(l,l′) = (M_l M_{l′})^{-1/2} ∂²Φ, where Φ contains Coulomb and short‑range contributions.

– Coulomb part: For l ≠ l′,
  D_{αα′}^C(l,l′) = –(M_l M_{l′})^{-1/2} [e(l) e(l′) / r₀³] ( (r_{0α} r_{0α′}/r₀²) – δ_{αα′} ),
  where r_{0α} are the Cartesian components of the equilibrium separation vector. For l = l′ the Coulomb contribution vanishes by symmetry.

– Short‑range part: The short‑range interactions are restricted to nearest neighbours (central forces). The derivatives V′ and V″ of the pair potential are expressed through the dimensionless parameters A and B as V′ = (e²/(8 r₀³)) √3 r₀ B and V″ = (e²/(8 r₀³)) A; for the impurity‑first‑neighbour bonds the host A is replaced by A′ while B stays unchanged.

Using these, the on‑site and off‑diagonal short‑range matrix elements are:
  - Impurity site (l=0, l′=0): diagonal D_{αα}^R(00) = (1/M₀) · (e²/(8 r₀³)) · (8/3) (A′ + 2B); off‑diagonal zero.
  - Neighbour site l (1…8): diagonal D_{αα}^R(l,l) = (1/M_l) · (e²/(8 r₀³)) · (1/3) (A′ + 7A + 16B).
  - Blocks coupling impurity and neighbour (0,l): for l=1 (r₀(111)), the diagonal element D_{αα}^R(0,1) = –(M₀ M₁)^{-1/2} · (e²/(8 r₀³)) · (A′ + 2B)/3, and the off‑diagonal (α≠α′) D_{αα′}^R(0,1) = –(M₀ M₁)^{-1/2} · (e²/(8 r₀³)) · (A′ – B)/3. For other neighbours l, the sign and pattern follow by symmetry from the direction cosines of their position vectors.

The total matrix is the sum of the Coulomb and short‑range contributions. It is real symmetric of size 27×27 (three Cartesian coordinates per atom, nine atoms).

For each combination of impurity (H⁻ or D⁻) and defect parameter A′ (taken from the set {4.7452, 4.0, 3.0, 2.0, 1.0, 0.5}), the matrix is assembled and diagonalised. The highest eigenvalue ω² (which is triply degenerate) is identified; the angular frequency is ω = √(ω²), which is then converted to the unit 10¹³ s⁻¹.

## Reproduction target
Compute the localised vibrational mode frequencies for H⁻ and D⁻ impurities in a nine‑atom CsCl‑type defect cluster (host lattice CsI) as a function of the defect short‑range parameter A′. Specifically, produce a CSV file named localized_frequencies.csv under /app/outputs with columns A_prime (float), impurity (string, either 'H' or 'D'), and frequency (float, in units of 10¹³ s⁻¹). The rows must cover the A′ values [4.7452, 4.0, 3.0, 2.0, 1.0, 0.5] for both impurities, in any order. The frequency for each row must be the highest triply‑degenerate eigenvalue of the 27×27 dynamical matrix built with the given host masses (M_Cs=132.9 u, M_I=126.9 u), impairment masses (H 1.0 u, D 2.0 u), host parameters A and B (computed from r₀=2.282 Å, k=1.441×10¹¹ dyn cm⁻², α=1.7627, e=4.803×10⁻¹⁰ esu), and the specified A′. No other output columns are required.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute host short-range parameters A and B
- Role: process
- Action: Compute the dimensionless host short-range parameters A and B from the half-lattice constant r0 = 2.282 Å, the bulk modulus K (from compressibility k = 1.441e11 dyn cm^{-2}), the Madelung constant α = 1.7627, and the elementary charge e (4.803e-10 esu). Use K = 1/k, A = (3 r0 K) * (8 r0^3 / e^2) + (2α)/(3√3), B = -α/(3√3). Convert r0 to cm (1 Å = 1e-8 cm) and use CGS units throughout. Save the computed A and B to host_params.json.
- Evidence: `/app/outputs/host_params.json`

### Step 2: Compute localized mode frequencies
- Role: scored (load-bearing)
- Action: For each impurity (H⁻ with mass 1.0 u, D⁻ with mass 2.0 u) and each defect short-range parameter A' in {4.7452, 4.0, 3.0, 2.0, 1.0, 0.5}: construct the full 27×27 real symmetric dynamical matrix for the nine-atom CsCl-type defect cluster using the Coulomb and short-range matrix element formulas (on-site and nearest-neighbour contributions) with host masses M_Cs=132.9 u and M_I=126.9 u, ionic charges ±1, and the host parameters A and B from the previous step. Diagonalize the matrix, identify the triply degenerate highest eigenvalue ω², compute ω = sqrt(ω²), and convert to units of 10^{13} s^{-1}. Write a CSV file localized_frequencies.csv with columns A_prime, impurity, frequency. Each row corresponds to one (A_prime, impurity) combination.
- Output file: `/app/outputs/localized_frequencies.csv`
- Format: csv
- Contract: CSV with header: A_prime, impurity, frequency. A_prime: float, impurity: string ('H' or 'D'), frequency: float (unit: 10^{13} s^{-1}).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/localized_frequencies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### localized_frequencies.csv
- path: `/app/outputs/localized_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Localized vibrational mode frequencies for H⁻ and D⁻ impurities in a nine-atom CsCl-type defect cluster, as a function of the defect short-range parameter A'. The checker independently rebuilds the dynamical matrix for each row and compares the reported frequency to the recomputed value within a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `A_prime`, `impurity`, `frequency`
  - `units`:
    - `frequency`: 10^{13} s^{-1}

Notes: Only the highest triply-degenerate eigenvalue (localized mode) is scored. Perturbed lattice mode frequencies are not part of the scored output.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "localized_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "A_prime",
          "impurity",
          "frequency"
        ],
        "units": {
          "frequency": "10^{13} s^{-1}"
        }
      },
      "description": "Localized vibrational mode frequencies for H⁻ and D⁻ impurities in a nine-atom CsCl-type defect cluster, as a function of the defect short-range parameter A'. The checker independently rebuilds the dynamical matrix for each row and compares the reported frequency to the recomputed value within a tolerance."
    }
  ],
  "notes": "Only the highest triply-degenerate eigenvalue (localized mode) is scored. Perturbed lattice mode frequencies are not part of the scored output."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier. The verifier independently recomputes the localised mode frequency for each (A_prime, impurity) row in your localized_frequencies.csv. It uses the same host parameters A, B, masses, and the same dynamical matrix formulas described in the Approach. For each row, it compares your reported frequency to the recomputed value against a tight relative tolerance. The final reward is the fraction of rows that satisfy the tolerance check (i.e., a number in [0, 1]). The host_params.json file is required as an intermediate but does not directly carry reward; only localized_frequencies.csv is scored. A perfect reproduction earns a reward of 1.0.
