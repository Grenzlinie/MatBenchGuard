# Self-consistent local pseudopotential band structure and total energy calculation for Si, Ge and α-Sn

## Problem background
This task addresses the problem of computing the electronic band structure and total crystal energy of diamond-structure semiconductors from first principles using a self-consistent local pseudopotential method (SCLPM). Traditional empirical pseudopotential methods parametrize the screened pseudopotential directly and cannot perform a self-consistent calculation. In contrast, this method parametrizes the ionic pseudopotential only and obtains the starting screened pseudopotential analytically via linear screening. The method then performs a self-consistent field (SCF) loop to determine the electronic eigenvalues and the screened potential. The target quantities are the band energies at the high-symmetry points \(\Gamma\), X, and L, and the total crystal energy per atom for silicon (Si), germanium (Ge), and grey tin (\(\alpha\)-Sn).

## Approach
The calculation proceeds in four stages:

0. **Ionic pseudopotential fitting:** Fit the parameters \(b_1, b_2, b_3, b_4\) and \(\alpha_{\mathrm{eff}}, k_{\mathrm{F}}\) of the ionic pseudopotential form \(v^{\mathrm{ion}}(q) = (b_1/q^2)(\cos(b_2 q) + b_3) \exp(-b_4 q^4)\) such that when divided by the Heine‑Abarenkov dielectric function they reproduce the empirical screened pseudopotential form factors from Cohen and Bergstresser (1966) for the given material. The target form factors are taken at the reciprocal‑lattice vectors with \(q^2 = 3, 8, 11\) (in units of \((2\pi/a)^2\)) for Si and Ge; for α‑Sn also include \(q^2 = 16, 19\). The resulting fitted parameters feed into the subsequent stages.

1. **Starting Hamiltonian:** Construct the starting screened pseudopotential for each material by applying the Heine‑Abarenkov dielectric function \(\varepsilon(q)\) to the fitted ionic pseudopotential. The dielectric function incorporates the free‑electron Lindhard susceptibility, a Hubbard‑type correction, and the orthogonality constant \(\alpha_{\mathrm{eff}}\). Together they yield an analytical expression for the initial screened potential.

2. **Self‑consistent field loop:** With the starting potential, solve the one‑electron Schrödinger equation in a plane‑wave basis to obtain wavefunctions and eigenvalues. Use Löwdin perturbation theory to account for high‑energy plane waves beyond the explicit basis. Compute the valence charge density from the occupied wavefunctions at a single special \(k\)-point in the irreducible Brillouin zone. Construct the Hartree potential \(V_{\mathrm{H}}\) and the exchange‑correlation potential \(V_{\mathrm{xc}}\) within the \(X_\alpha\) approximation using \(\alpha = 0.79\). The total screening potential is added to the bare ionic potential to form a new effective potential. Mix the old and new potentials and iterate until the eigenvalues and screening potential are converged.

3. **Total energy evaluation:** Once convergence is achieved, compute the total crystal energy per atom using the momentum‑space total‑energy formula. This includes the sum of occupied eigenvalues, the Hartree and exchange‑correlation double‑counting corrections, a core‑repulsiveness term \(\alpha_1 Z\), and the Ewald ion‑ion energy.

The procedure is executed for each of the three materials using the material‑specific lattice constants and pseudopotential parameters provided as inputs.

## Reproduction target
Produce a single JSON file named `band_and_total_energy.json` under `/app/outputs`. The file must contain a top‑level key `"materials"` with a list of three entries, one for each material: `"Si"`, `"Ge"`, and `"alpha-Sn"`. For each material, provide:

- `"band_eigenvalues"`: an object with keys `"Gamma"`, `"X"`, and `"L"`. Each key maps to a list of floating‑point energy eigenvalues (in eV), referenced to the top of the valence band (\(\Gamma_{25'}\)) set to 0 eV. The eigenvalues must appear in the following fixed order:
  - **Gamma:** [\(\Gamma_1\) (lowest valence), \(\Gamma_{25'}\) (top of valence, approximately 0), \(\Gamma_{15}\), \(\Gamma_{2'}\), \(\Gamma_{12'}\) (if available)]
  - **X:** [\(X_1\) (lowest valence), \(X_4\), \(X_1\) (conduction), \(X_4\) (upper conduction)]
  - **L:** [\(L_{2'}\) (lowest valence), \(L_1\), \(L_{3'}\), \(L_1\) (conduction), \(L_3\)]

- `"total_energy_per_atom"`: a floating‑point number representing the total crystal energy per atom in Rydberg (Ryd).

## Assets

- Python scientific computing stack (numpy, scipy): numpy scipy
- Empirical screened pseudopotential form factors from Cohen and Bergstresser (1966) for Si, Ge, and α‑Sn. These are the target values for the fitting step.

## Workflow steps

### Step 0: Fit ionic pseudopotential parameters
- Role: process
- Action: Fit the parameters b₁, b₂, b₃, b₄, α_eff, k_F of the ionic pseudopotential form (eq. (9)) to the empirical screened pseudopotential form factors from Cohen and Bergstresser (1966) for each material (Si, Ge, α-Sn). Use the Heine‑Abarenkov dielectric function (eq. (7)-(8)). The target empirical form factors are taken at the reciprocal‑lattice vectors with q² = 3, 8, 11 (in units of (2π/a)²) for Si and Ge; for α-Sn also include q² = 16, 19.
- Evidence: `/app/outputs/fitted_params.log`

### Step 1: Self-consistent band structure calculation
- Role: process
- Action: For each material (Si, Ge, α-Sn), set up the diamond-structure unit cell with the given lattice constant and atomic positions. Construct the starting screened pseudopotential using the fitted ionic pseudopotential parameters (from Step 0) and the Heine-Abarenkov dielectric function. Perform a self-consistent field (SCF) loop: solve the Schrödinger equation in a plane-wave basis, using Baldereschi's special k-point for the charge density and a finer k-point mesh for band energies. Use the Xα exchange-correlation with α=0.79. Iterate until eigenvalues are stable. After convergence, extract the band eigenvalues at the Γ, X, and L high-symmetry points.
- Evidence: `/app/outputs/scf_log.txt`

### Step 2: Total energy computation
- Role: process
- Action: Using the self-consistent wavefunction coefficients, charge density Fourier components, and screening potentials from the SCF step, compute the total crystal energy per atom via the momentum-space total-energy formula of Ihm, Zunger, and Cohen. Include the sum of occupied eigenvalues, the Hartree and exchange-correlation double-counting corrections, the core repulsiveness term α₁Z, and the Ewald ion-ion energy.
- Evidence: `/app/outputs/total_energy_log.txt`

### Step 3: Output band energies and total energy
- Role: scored (load-bearing)
- Action: Assemble the computed band eigenvalues and total energies into the specified JSON structure. For each material, provide the energy eigenvalues at the Γ, X, and L points in eV, referenced to the top of the valence band (Γ₂₅' set to 0 eV), and the total crystal energy per atom in Ryd. Write the result to band_and_total_energy.json under /app/outputs.
- Output file: `/app/outputs/band_and_total_energy.json`
- Format: json
- Contract: {"materials": [{"name": "str", "band_eigenvalues": {"Gamma": [float, ...], "X": [float, ...], "L": [float, ...]}, "total_energy_per_atom": float}]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_and_total_energy.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_and_total_energy.json
- path: `/app/outputs/band_and_total_energy.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed band eigenvalues at Gamma, X, L points (eV) and total crystal energy per atom (Ryd) for Si, Ge, and alpha-Sn.
- schema:
  - `type`: object
  - `required`: `materials`
  - `properties`:
    - `materials`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `name`, `band_eigenvalues`, `total_energy_per_atom`
        - `properties`:
          - `name`:
            - `type`: string
            - `enum`: `Si`, `Ge`, `alpha-Sn`
          - `band_eigenvalues`:
            - `type`: object
            - `required`: `Gamma`, `X`, `L`
            - `properties`:
              - `Gamma`:
                - `type`: array
                - `items`:
                  - `type`: number
              - `X`:
                - `type`: array
                - `items`:
                  - `type`: number
              - `L`:
                - `type`: array
                - `items`:
                  - `type`: number
          - `total_energy_per_atom`:
            - `type`: number

Notes: The eigenvalues are referenced to the top of the valence band (Gamma25' set to 0 eV). The order of eigenvalues in each array must follow the prescribed sequence: Gamma: [lowest valence, Gamma25', Gamma15, Gamma2', Gamma12' (if available)]; X: [lowest valence X1, X4, X1 conduction, X4 upper conduction]; L: [L2' lowest valence, L1, L3', L1 conduction, L3]. Total energy per atom in Ryd.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_and_total_energy.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "materials"
        ],
        "properties": {
          "materials": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "name",
                "band_eigenvalues",
                "total_energy_per_atom"
              ],
              "properties": {
                "name": {
                  "type": "string",
                  "enum": [
                    "Si",
                    "Ge",
                    "alpha-Sn"
                  ]
                },
                "band_eigenvalues": {
                  "type": "object",
                  "required": [
                    "Gamma",
                    "X",
                    "L"
                  ],
                  "properties": {
                    "Gamma": {
                      "type": "array",
                      "items": {
                        "type": "number"
                      }
                    },
                    "X": {
                      "type": "array",
                      "items": {
                        "type": "number"
                      }
                    },
                    "L": {
                      "type": "array",
                      "items": {
                        "type": "number"
                      }
                    }
                  }
                },
                "total_energy_per_atom": {
                  "type": "number"
                }
              }
            }
          }
        }
      },
      "description": "Computed band eigenvalues at Gamma, X, L points (eV) and total crystal energy per atom (Ryd) for Si, Ge, and alpha-Sn."
    }
  ],
  "notes": "The eigenvalues are referenced to the top of the valence band (Gamma25' set to 0 eV). The order of eigenvalues in each array must follow the prescribed sequence: Gamma: [lowest valence, Gamma25', Gamma15, Gamma2', Gamma12' (if available)]; X: [lowest valence X1, X4, X1 conduction, X4 upper conduction]; L: [L2' lowest valence, L1, L3', L1 conduction, L3]. Total energy per atom in Ryd."
}
```

## How you are scored
The hidden verifier independently compares each band eigenvalue (in eV) and the total energy per atom (in Ryd) that you report against reference values from the original study. Each quantity is checked with an appropriate tolerance that accounts for implementation‑dependent differences (e.g., choice of basis, convergence criteria, numerical libraries). The final reward is computed as a weighted combination of the scores of the individual stages, giving more weight to the band energies at the high‑symmetry points and the total energy. Reporting the reference numbers without performing the self‑consistent calculation will not pass the tolerance checks.
