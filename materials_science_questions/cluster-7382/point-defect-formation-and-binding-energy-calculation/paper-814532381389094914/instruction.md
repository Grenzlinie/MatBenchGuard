# Vacancy formation energies in random alloys using a single-site mean-field model

## Problem background
In random alloys, the concentration of thermal vacancies governs phase transformation kinetics and diffusion. The energy required to form a vacancy depends on the local atomic environment, and at finite temperature the configurational entropy of the alloy can modify the effective vacancy formation energy. This task addresses the single-site mean-field picture: the distribution of local vacancy formation energies in a completely random alloy is modelled, and from it one can compute an effective vacancy formation energy and a renormalized formation energy that includes the alloy configurational entropy. These quantities are temperature‑dependent and provide insight into how configurational effects influence vacancy populations in multicomponent alloys. Your task is to compute the effective and renormalized vacancy formation energies for a model equiatomic binary alloy at several temperatures.

## Approach
The calculation uses the single-site mean‑field approximation, assuming vacancies are non‑interacting and that the vacancy formation entropy is independent of local environment. For a binary equiatomic random alloy A₀.₅B₀.₅ with a face‑centered cubic structure, only the nearest‑neighbour shell (12 atoms) matters. The local vacancy formation energy when n of the 12 neighbours are of species B is written as E(n) = E_f⁰ + n V₁, where E_f⁰ is the lowest local formation energy and V₁ the vacancy–B interaction energy. The distribution g(n) for an equiatomic random alloy is a binomial distribution: g(n) = 12! / (2¹² n! (12−n)!) for n = 0 … 12.

The alloy configurational entropy (per lattice site) of the defect‑free equiatomic alloy, S_all = −[c ln c + (1−c) ln(1−c)] with c = 0.5, reduces the concentration of vacancies and appears in the renormalized formation energy.

For a given temperature T (converted to eV via the Boltzmann constant k_B = 8.617333262×10⁻⁵ eV/K), the effective vacancy formation energy is obtained from the partition sum:

E_f(T) = −T · ln[ Σ_{n=0}^{12} g(n) · exp(−E(n)/T) ]

and the renormalized vacancy formation energy is

\widetilde{E_f}(T) = E_f(T) + T · S_all.

These expressions are to be evaluated for the parameters E_f⁰ = 1.9 eV and V₁ = 0.082 eV at the temperatures 500 K, 1000 K, and 1500 K. The calculation requires only basic numerical operations (logarithms, exponentials, and a small sum) and can be implemented with standard Python libraries such as numpy.

## Reproduction target
Compute the effective vacancy formation energy E_f(T) and the renormalized vacancy formation energy \widetilde{E_f}(T) for the described model at T = 500 K, 1000 K, and 1500 K. Write the six resulting numbers to a single JSON file `/app/outputs/vacancy_formation_energies.json` with the exact keys:

- "T_500_Ef": E_f(500 K) in eV
- "T_500_tildeEf": \widetilde{E_f}(500 K) in eV
- "T_1000_Ef": E_f(1000 K) in eV
- "T_1000_tildeEf": \widetilde{E_f}(1000 K) in eV
- "T_1500_Ef": E_f(1500 K) in eV
- "T_1500_tildeEf": \widetilde{E_f}(1500 K) in eV

The JSON object must contain exactly these six entries. No other files or output are required.

## Assets

- numpy: numpy

## Workflow steps

### Step 1: Compute effective and renormalized vacancy formation energies
- Role: scored (load-bearing)
- Action: Compute the effective vacancy formation energy E_f(T) and renormalized vacancy formation energy tilde_E_f(T) for a Cu0.5Ni0.5 random alloy at temperatures T = 500, 1000, 1500 K using the single-site mean-field model. Use the binomial distribution of local formation energies with N=12 nearest neighbours: q(n) = 12! / (2^12 * n! * (12-n)!) for n=0..12, and energies E(n) = E_f0 + n * V1 with E_f0 = 1.9 eV and V1 = 0.082 eV. Convert T to eV via k_B = 8.617333262e-5 eV/K. Compute the alloy configurational entropy S_all = -[c ln c + (1-c) ln(1-c)] with c=0.5. Then for each T compute E_f(T) = -T * ln( sum_n q(n) * exp(-E(n)/T) ) and tilde_E_f(T) = E_f(T) + T * S_all. Write the six values to a JSON file.
- Output file: `/app/outputs/vacancy_formation_energies.json`
- Format: json
- Contract: {"T_500_Ef": "float (eV)", "T_500_tildeEf": "float (eV)", "T_1000_Ef": "float (eV)", "T_1000_tildeEf": "float (eV)", "T_1500_Ef": "float (eV)", "T_1500_tildeEf": "float (eV)"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/vacancy_formation_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### vacancy_formation_energies.json
- path: `/app/outputs/vacancy_formation_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Effective and renormalized vacancy formation energies at T=500,1000,1500 K computed from the binomial distribution model with given parameters.
- schema:
  - `type`: object
  - `required`:
    - `T_500_Ef`: float (eV)
    - `T_500_tildeEf`: float (eV)
    - `T_1000_Ef`: float (eV)
    - `T_1000_tildeEf`: float (eV)
    - `T_1500_Ef`: float (eV)
    - `T_1500_tildeEf`: float (eV)

Notes: All parameters (E_f0=1.9 eV, V1=0.082 eV, c=0.5) are fixed inputs; the checker recomputes the six numbers from these same inputs and compares with a tolerance of 0.02 eV.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "vacancy_formation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "T_500_Ef": "float (eV)",
          "T_500_tildeEf": "float (eV)",
          "T_1000_Ef": "float (eV)",
          "T_1000_tildeEf": "float (eV)",
          "T_1500_Ef": "float (eV)",
          "T_1500_tildeEf": "float (eV)"
        }
      },
      "description": "Effective and renormalized vacancy formation energies at T=500,1000,1500 K computed from the binomial distribution model with given parameters."
    }
  ],
  "notes": "All parameters (E_f0=1.9 eV, V1=0.082 eV, c=0.5) are fixed inputs; the checker recomputes the six numbers from these same inputs and compares with a tolerance of 0.02 eV."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently recomputes the six formation energy values from the same model parameters and temperature points. It compares your reported numbers to the reference values. The scoring rewards accurate results: full credit is given when all six values are within a predefined tolerance of the reference; a lower reward is assigned for larger deviations. The verifier does not require any additional output beyond the JSON file specified in the workflow step.
