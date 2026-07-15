# ADP Potential for Al-H System: Defect Energetics and Migration Barrier

## Problem background
Hydrogen-induced degradation in aluminum alloys, such as embrittlement, is technologically important, and atomistic simulations rely on accurate interatomic potentials to capture the behavior of dissolved hydrogen. This task involves developing an angular-dependent potential (ADP) for the Al–H system and using it to compute three key physical properties that characterize hydrogen in aluminum: the equilibrium properties of the H₂ molecule, the dilute solution energies of H atoms at interstitial sites in face-centered cubic (fcc) Al, and the migration barrier for H diffusion between those sites. Computing these quantities will exercise the potential's ability to reproduce defect energetics and diffusion properties.

## Approach
The interatomic potential is based on the Angular-Dependent Potential (ADP) formalism, which extends the Embedded Atom Method (EAM) by adding dipole and quadrupole terms that penalize deviations from cubic symmetry:

$$E_{\mathrm{tot}} = \frac{1}{2} \sum_{i, j(j \neq i)} \Phi_{s_i s_j}(r_{ij}) + \sum_i F_{s_i}(\bar{\rho}_i) + \frac{1}{2} \sum_{i,\alpha} (\mu_i^{\alpha})^2 + \frac{1}{2} \sum_{i,\alpha,\beta} (\lambda_i^{\alpha\beta})^2 - \frac{1}{6} \sum_i \nu_i^2$$

The first two terms are the usual EAM pair and embedding contributions; the last three introduce angular forces via dipole vectors $\mu_i^{\alpha} = \sum_{j \neq i} u_{s_i s_j}(r_{ij}) r_{ij}^{\alpha}$ and quadrupole tensors $\lambda_i^{\alpha\beta} = \sum_{j \neq i} w_{s_i s_j}(r_{ij}) r_{ij}^{\alpha} r_{ij}^{\beta}$, with $\nu_i = \sum_{\alpha} \lambda_i^{\alpha\alpha}$.

The pure Al part is described by the existing Mishin 1999 EAM potential (provided as a separate file). For hydrogen, the following closed-form functions are used (with a cutoff $\psi(x) = x^4/(1+x^4)$ for $x<0$ and $0$ otherwise, $x = (r-r_c)/h$):

- **Electron density**: $\rho(r) = \bigl(A_0 r^{z_1} e^{-\alpha_1 r} + B_0 r^{z_2} e^{-\alpha_2 r} + C_0\bigr) \,\psi\bigl(\frac{r-r_c}{h}\bigr)$
- **Pair interaction**: $\Phi(r) = \bigl\{V_0\bigl[e^{-\alpha\beta(r-R_0)} - \alpha e^{-\beta(r-R_0)}\bigr] + A_1 + A_2(r-R_0) + A_3 e^{-\gamma(r-R_1)^2}\bigr\} \,\psi\bigl(\frac{r-r_c}{h}\bigr)$
- **Embedding energy**: $F(\bar{\rho}) = \bigl(s_1 \bar{\rho} + s_2 \bar{\rho}^2 + s_3 \bar{\rho}^3 - s_4 \bar{\rho}^{s_5}\bigr) \, \omega(\bar{\rho})$, with $\omega(\bar{\rho}) = 1 - \frac{1 - s_6 \bar{\rho}^2}{1 + s_7 \bar{\rho}^4}$
- **Dipole function**: $u(r) = \bigl(d_1 e^{-d_2 r} + d_3\bigr) \,\psi\bigl(\frac{r-r_c}{h}\bigr)$
- **Quadrupole function**: $w(r) = \bigl(q_1 e^{-q_2 r} + q_3\bigr) \,\psi\bigl(\frac{r-r_c}{h}\bigr)$

The cross-interactions for Al–H are parameterised as:

- **Pair interaction**: $\Phi_{\mathrm{AlH}}(r) = \bigl[\frac{W_0}{b_2 - b_1}\bigl(\frac{b_2}{z^{b_1}} - \frac{b_1}{z^{b_2}}\bigr) + \delta\bigr] \,\psi\bigl(\frac{r-r_c}{h}\bigr)$, with $z = r/r_1$.
- **Dipole and quadrupole**: same functional forms as for pure H, with separate parameters.

The potential functions also undergo invariant transformations that involve three additional parameters $s_{\mathrm{H}}$, $g_{\mathrm{Al}}$, $g_{\mathrm{H}}$ that modify the functions without affecting pure-element properties.

The complete set of optimized parameters is given in the tables below. Your task is to implement the ADP energy, forces, and stresses using these parameters, integrate with the Al EAM potential, and then perform the computational steps that follow.

### ADP hydrogen potential parameters (pure H)

| Parameter | Value | Parameter | Value |
|-----------|-------|-----------|-------|
| $r_c$ (Å) | 2.10399 | $\alpha_2$ (1/Å) | 2.15587 |
| $h$ (Å) | 7.05516e-01 | $C_0$ | 1.46318e-02 |
| $V_0$ (eV) | 4.23413e-01 | $s_1$ | 8.08612 |
| $\alpha$ | 4.80494 | $s_2$ | 1.46294e-02 |
| $\beta$ (1/Å) | 3.51586 | $s_3$ | -6.86143e-03 |
| $R_0$ (Å) | 7.25356 | $s_4$ | 3.19616 |
| $A_1$ (eV) | 2.18646e-02 | $s_5$ | 1.17247e-01 |
| $A_2$ (eV/Å) | 2.06845e-02 | $s_6$ | 50 |
| $A_3$ (eV) | 4.94849e-02 | $s_7$ | 1500000 |
| $\gamma$ (eV/Å²) | 3.03090 | $d_1$ (√eV/Å) | 7.40338e-01 |
| $R_1$ (Å) | 1.52662 | $d_2$ (1/Å) | 1.67135 |
| $A_0$ (1/Å^{z1}) | 3.18287e-01 | $d_3$ (√eV/Å) | 1.02980e-03 |
| $z_1$ | 1.41565e-01 | $q_1$ (√eV/Å²) | 1.57109 |
| $\alpha_1$ (1/Å) | 1.35765 | $q_2$ (1/Å) | 1.80580 |
| $B_0$ (1/Å^{z2}) | 1.07196e-02 | $q_3$ (√eV/Å²) | -6.08109e-03 |
| $z_2$ | 2.40281e-02 | | |

### ADP Al–H cross-interaction parameters

| Parameter | Value | Parameter | Value |
|-----------|-------|-----------|-------|
| $r_c$ (Å) | 3.37008 | $d_2$ (1/Å) | 1.23325e-01 |
| $h$ (Å) | 6.30476e-01 | $d_3$ (√eV/Å) | -1.09582e-02 |
| $W_0$ (eV) | -1.08601e-01 | $q_1$ (√eV/Å²) | -4.60988e-02 |
| $r_1$ (Å) | 1.67001 | $q_2$ (1/Å) | 1.08789e-01 |
| $b_1$ | 8.16186 | $q_3$ (√eV/Å²) | 4.54746e-02 |
| $b_2$ | 8.34403 | $s_{\mathrm{H}}$ | 4.00846e-01 |
| $\delta$ (eV) | 5.51726e-02 | $g_{\mathrm{Al}}$ (eV) | -6.42956e-02 |
| $d_1$ (√eV/Å) | 1.01564e-01 | $g_{\mathrm{H}}$ (eV) | -7.97198e-01 |

## Reproduction target
Implement the ADP potential for the Al–H system using the above functional forms and parameter sets. Use the provided external EAM potential for pure Al. Then compute:

1. **H₂ dimer properties**: Perform energy minimization of an isolated H₂ molecule. Report the equilibrium bond length (Å) and cohesive energy per atom (eV).
2. **Dilute solution energies of H in Al**: Construct an fcc Al supercell (minimum 3×3×3) with a single H atom at the tetrahedral interstitial site; relax the structure and compute the total energy. Repeat for the octahedral site. Compute the dilute solution energies $\Delta E_s(T_d)$ and $\Delta E_s(O_h)$ using the energy of bulk fcc Al and the H₂ molecule.
3. **H migration barrier**: Using the same supercell and the full Al–H potential, perform a nudged elastic band (NEB) calculation between the relaxed tetrahedral and octahedral configurations. Report the maximum energy along the path as the migration barrier (eV).

Write the results to the three JSON files specified in the workflow steps.

## Assets

- Mishin 1999 EAM potential for Al: https://www.ctcms.nist.gov/potentials/Download/1999--Mishin-Y--Farkas-D--Mehl-M-J--Papaconstantopoulos-D-A--1/1/Al_Mishin_1999.eam.alloy
- LAMMPS: https://lammps.sandia.gov/

## Workflow steps

### Step 1: Potential implementation and setup
- Role: process
- Action: Implement the ADP potential for H and Al-H using the closed-form functional forms from the method description and the provided parameter tables, integrate it with the existing Mishin 1999 EAM Al potential to compute total energies, forces, and stresses for Al-H configurations.
- Evidence: `/app/outputs/potential_implementation.txt`

### Step 2: H2 Dimer Equilibrium Properties
- Role: scored
- Action: Using the hydrogen portion of the potential, perform energy minimization of an isolated H2 molecule to obtain the equilibrium bond length (Å) and cohesive energy per atom (eV).
- Output file: `/app/outputs/h2_dimer_results.json`
- Format: json
- Contract: object with keys: "bond_length_angstroms" (float), "cohesive_energy_eV_per_atom" (float)
- Scoring: scored by hidden verifier

### Step 3: Dilute Solution Energies of H in Al
- Role: scored (load-bearing)
- Action: Construct an fcc Al supercell (minimum 3×3×3) with one H atom placed at the tetrahedral interstitial site; relax the structure and compute total energy. Repeat for the octahedral site. Compute the dilute solution energies ΔE_s(Td) and ΔE_s(Oh) using the energy of bulk fcc Al and the H2 molecule.
- Output file: `/app/outputs/solution_energies.json`
- Format: json
- Contract: object with keys: "delta_Es_Td_eV" (float), "delta_Es_Oh_eV" (float)
- Scoring: scored by hidden verifier

### Step 4: H Migration Barrier via NEB
- Role: scored (load-bearing)
- Action: Using the same supercell and the full Al-H potential, perform a nudged elastic band (NEB) calculation between the relaxed tetrahedral and octahedral configurations. Report the maximum energy along the path as the migration barrier (eV).
- Output file: `/app/outputs/migration_barrier.json`
- Format: json
- Contract: object with key: "migration_barrier_eV" (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/h2_dimer_results.json`
- `/app/outputs/solution_energies.json`
- `/app/outputs/migration_barrier.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### h2_dimer_results.json
- path: `/app/outputs/h2_dimer_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: H2 dimer equilibrium bond length and cohesive energy per atom, computed by energy minimization.
- schema:
  - `type`: object
  - `required`:
    - `bond_length_angstroms`: float, unit Å
    - `cohesive_energy_eV_per_atom`: float, unit eV

### solution_energies.json
- path: `/app/outputs/solution_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Dilute solution energies of a single H atom at tetrahedral and octahedral interstitial sites in fcc Al, computed via supercell relaxation.
- schema:
  - `type`: object
  - `required`:
    - `delta_Es_Td_eV`: float, unit eV
    - `delta_Es_Oh_eV`: float, unit eV

### migration_barrier.json
- path: `/app/outputs/migration_barrier.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Minimum energy barrier for a H atom migrating from tetrahedral to octahedral site in Al, obtained by nudged elastic band.
- schema:
  - `type`: object
  - `required`:
    - `migration_barrier_eV`: float, unit eV

Notes: The hidden checker reads the three JSON files and compares each scalar to the gold values within predetermined absolute tolerances. All outputs are compared to the paper’s reported numbers. No gold values or tolerances are revealed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "h2_dimer_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "bond_length_angstroms": "float, unit Å",
          "cohesive_energy_eV_per_atom": "float, unit eV"
        }
      },
      "description": "H2 dimer equilibrium bond length and cohesive energy per atom, computed by energy minimization."
    },
    {
      "file": "solution_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "delta_Es_Td_eV": "float, unit eV",
          "delta_Es_Oh_eV": "float, unit eV"
        }
      },
      "description": "Dilute solution energies of a single H atom at tetrahedral and octahedral interstitial sites in fcc Al, computed via supercell relaxation."
    },
    {
      "file": "migration_barrier.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "migration_barrier_eV": "float, unit eV"
        }
      },
      "description": "Minimum energy barrier for a H atom migrating from tetrahedral to octahedral site in Al, obtained by nudged elastic band."
    }
  ],
  "notes": "The hidden checker reads the three JSON files and compares each scalar to the gold values within predetermined absolute tolerances. All outputs are compared to the paper’s reported numbers. No gold values or tolerances are revealed here."
}
```

## How you are scored
A hidden verifier reads your three JSON output files. It compares each required numeric value (bond length, cohesive energy, two solution energies, migration barrier) to a reference derived from the original publication (the gold). The verifier checks whether each value falls within a predetermined absolute tolerance. If all values are within tolerance, you earn the maximum reward of 1.0; otherwise partial credit is proportional to the number of correct values. The exact tolerances and the gold values are not disclosed to you. Simply writing a number that matches the paper’s reported result is not sufficient — the verifier expects the values to be obtained through a correct implementation of the interatomic potential and the described simulation protocol.
