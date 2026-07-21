# Semiempirical chemisorption model for hydrogen on nickel surfaces

## Problem background
Chemisorption of atomic hydrogen on transition-metal surfaces is a fundamental system in surface science, yet the relative roles of the metal s band and d band in the bonding remain debated. The semiempirical model studied here proposes that the dominant interaction for H on nickel is the coupling of the hydrogen 1s orbital to the metal s band, with the unoccupied H 2p orbitals coupling to the d band. The model predicts adsorption energies and energy profiles (potential energy surfaces) for H on the three low-index nickel faces: (111), (100), and (110). The target quantity is the computed adsorption energy at the most favourable site on each face and the maximum energy variation across the Ni(111) surface unit cell, which reflects the predicted barrier for hydrogen surface mobility.

## Model specification

### Orbitals
- **Hydrogen 1s**: Slater-type orbital (STO) with exponent $$\zeta = 1.0$$ (from Slater's rules).
- **Hydrogen 2p**: STO with exponent $$\zeta = 1.5$$. The 2s orbital is neglected after orthogonalisation against the 1s.
- **Nickel 4s**: STO with exponent $$\zeta = 1.50$$ and coefficient 1.0.
- **Nickel 3d**: double-zeta STO with exponents $$\zeta_1 = 2.00$$ (coefficient $$c_1 = 0.6292$$) and $$\zeta_2 = 5.75$$ (coefficient $$c_2 = 0.5683$$). The metal electronic configuration is $$4s^2 3d^8$$ (neutral atom).

### Effective density of states and $$\delta$$-function approximation
The metal s band (approximately 10 eV wide) is modelled as a free-electron gas for the purpose of estimating overlap integrals. It is discretised into **seven $$\delta$$-functions** (degenerate bands) uniformly spanning the s-band width. The metal d band is approximated by a **single $$\delta$$-function** at the d-band centre. This discretisation transforms the infinite metal into a finite set of levels and is essential for numerical diagonalisation.

### Localised metal orbitals (Eq. 6)
The adsorbate–metal coupling uniquely defines a set of localised metal orbitals that maximise the overlap with the adorbitals. For an adorbital $$|A i s\rangle$$ the corresponding localised metal orbital $$|B i s\rangle$$ is

$$
|B i s\rangle = \frac{1}{\langle A i s | B i s\rangle} \sum_k \langle k s | A i s\rangle \, |k s\rangle,
$$

with the normalisation

$$
\langle A i s | B i s\rangle = \left[ \sum_k |\langle k s | A i s\rangle|^2 \right]^{1/2}.
$$

The sum over $$k$$ runs over all metal Bloch states (or their $$\delta$$-function discretised counterparts).

### Hamiltonian structure
The total one-electron Hamiltonian for spin $$s$$ is partitioned as

$$
F^s = F_{AD}^s + F_{LM}^s + F_{IM}^s + F_{AL}^s + F_{LI}^s,
$$

where
- $$F_{AD}^s$$ describes the **non-interacting adparticle** with $$M$$ valence orbitals of interest,
- $$F_{LM}^s$$ describes $$M$$ **localised metal orbitals** at the surface,
- $$F_{IM}^s$$ describes the **indented metal** (the metal states orthogonal to the localised orbitals),
- $$F_{AL}^s$$ gives the **coupling between the adparticle and the localised metal orbitals** (the "surface-molecule" interaction),
- $$F_{LI}^s$$ describes the **coupling between the localised orbitals and the indented metal**.

Explicitly (suppressing the spin index on the operators for brevity):

$$
\begin{aligned}
F_{LM}^s &= \sum_{i=1}^{M} E_{B i s} \, \tilde{n}_{B i s}, \\[4pt]
F_{IM}^s &= \sum_{k,\, l_{Bs},\, m_{Bs}} a_{l_{Bs}}^\dagger \langle l_{Bs} | k s \rangle \, \epsilon_k \, \langle k s | m_{Bs} \rangle \, a_{m_{Bs}}, \\[4pt]
F_{AL}^s &= \frac{1}{2} \sum_{i,j=1}^{M} \bigl(E_{A i s}^0 + E_{B i s}\bigr) \bigl(\langle A i s | B i s\rangle \langle B j s | B j s\rangle \, \tilde{a}_{A i s}^\dagger \tilde{a}_{B j s}^\dagger + \text{h.c.}\bigr) \\
&\quad + \frac{1}{2} \sum_{i,j=1}^{M} \Bigl[ \sum_{k=1}^{M} U_{i k} \langle \tilde{n}_{A k -s}\rangle + \sum_{\substack{k=1 \\ k \neq i}}^{M} (U_{i k} - J_{i k}) \langle \tilde{n}_{A k s}\rangle \Bigr] \\
&\qquad \times \bigl(\langle A i s | B i s\rangle \langle B i s | B j s\rangle \, \tilde{a}_{A i s}^\dagger \tilde{a}_{B j s} + \text{h.c.}\bigr), \\[4pt]
F_{LI}^s &= \sum_{\substack{i=1 \\ k_B \neq B i}}^{M} \bigl(V_{i k_B}^s \, \tilde{a}_{B i s}^\dagger a_{k_B s} + \text{h.c.}\bigr).
\end{aligned}
$$

The matrix elements $$E_{B i s}$$ and $$V_{i i_B}^s$$ are determined by the requirement that the unperturbed metal surface is recovered when the adparticle is removed:

$$
E_{B i s} = \sum_k \langle B i s | k s \rangle \, \epsilon_k \, \langle k s | B i s \rangle,
\qquad
V_{i i_B}^s = \sum_k \langle B i s | k s \rangle \, \epsilon_k \, \langle k s | l_B s \rangle.
$$

### Embedding and decoupling ($$\delta$$-function discretisation)
After replacing the s band by $$K = 7$$ degenerate bands (labelled by $$\kappa$$) and the d band by one degenerate band, the metal part of the Hamiltonian can be rewritten so that the "surface molecule" (adparticle + localised metal orbitals) is completely decoupled from the rest of the metal. The decoupled surface-molecule Hamiltonian for spin $$s$$ then reads

$$
\begin{aligned}
H_{\text{SM}}^s &= F_{AD}^s + F_{AL}^s + \sum_{i,\kappa} \epsilon_\kappa \, \hat{n}_{i \kappa s} + \sum_{i,j,\kappa} \epsilon_\kappa \, \Delta_{ij}^s \, \hat{a}_{i \kappa s}^\dagger \hat{a}_{j \kappa s},
\end{aligned}
$$

where

$$
\Delta_{ij}^s = \langle \hat{K} i \kappa s | \hat{K} j \kappa s \rangle
$$

is the overlap between the discretised metal orbitals on sites $$i$$ and $$j$$ in band $$\kappa$$, and $$\epsilon_\kappa$$ are the energies at which the $$\delta$$-functions are placed (the centres of the energy intervals for the s band and the d-band centre for the d band).

### Adsorbate–metal coupling parameter
The overlap between the adorbitals and the d-band wavefunctions is parameterised by a single factor $$B$$:

$$
\langle A i s | \hat{K} i d s \rangle = B \sum_{\mathbf{m}} \langle A i s | d\,\mathbf{m}, \text{opt.} \rangle,
$$

where $$\mathbf{m}$$ labels the lattice sites and $$|d\,\mathbf{m}, \text{opt.}\rangle$$ is the d orbital on site $$\mathbf{m}$$ that gives maximum overlap with $$|A i s\rangle$$. For nickel, **$$B = 0.222$$**.

### Total energy
The total electronic energy must be corrected for double-counting of electron–electron interactions that appear in $$F_{AL}^s$$. If the decoupled surface-molecule Hamiltonian $$H_{\text{SM}} = \sum_s H_{\text{SM}}^s$$ is diagonalised to yield one-electron eigenvalues $$\{\varepsilon_n\}$$, the **total energy** is

$$
E_{\text{total}} = \sum_{n}^{\text{occ}} \varepsilon_n - E_{\text{dc}},
$$

where $$E_{\text{dc}}$$ subtracts the electron–electron terms that were counted twice. The exact form of $$E_{\text{dc}}$$ follows from the expectation value of the original Hamiltonian (2) and involves sums over products of occupation numbers and Coulomb/exchange integrals; it must be evaluated consistently with the parameters used in $$F_{AL}^s$$.

### Adsorption energy
The **adsorption energy** at a given lateral and vertical position of the H atom is

$$
E_{\text{ads}} = E_{\text{total}}(\text{H} + \text{surface}) - E_{\text{total}}(\text{clean surface}) - E_{\text{total}}(\text{isolated H atom}),
$$

where all three total energies are computed with the same Hamiltonian framework. A positive value indicates an exothermic (favourable) adsorption.

### Equilibrium vertical distance
At each lateral position the equilibrium vertical distance is determined by maximising the overlap between the hydrogen 2p orbitals and the metal d wavefunctions (or, equivalently, minimising the total energy with respect to the vertical coordinate).

## Reproduction target
Compute and report the adsorption energy (in kcal/mol) for a hydrogen atom on each of the three nickel faces—Ni(111), Ni(100), Ni(110)—at the energetically most favourable adsorption site, using the implemented semiempirical chemisorption model. Additionally, compute the maximum energy variation (max − min) across the Ni(111) surface unit cell in kcal/mol. These are the quantities to be written into the scored output files `adsorption_energies.csv` and `energy_variation_n111.csv`.

## Assets
None. All model parameters (Slater orbital exponents, coefficients, B value, density-of-states approximation, electronic configuration) are fully specified above. No external datasets, model checkpoints, or supplementary files need to be downloaded.

## Workflow steps

### Step 1: Implement chemisorption model
- Role: process
- Action: Implement the semiempirical chemisorption model Hamiltonian for hydrogen on nickel as specified in the Model specification section. Use the Slater orbital parameters for H (1s exponent 1.0, 2p exponent 1.5), the nickel s- and d-band wavefunctions (4s: exponent 1.50, coefficient 1.0; 3d: double-zeta with exponents 2.00 and 5.75, coefficients 0.6292 and 0.5683), the effective density of states approximated by seven δ-functions for the s band and one δ-function for the d band, and the parameter B = 0.222. Construct the overlap matrix elements, the metal local orbitals, the full surface-molecule Hamiltonian, and the double-counting correction. Include the 1s–s and 2p–d interactions, with the 2s orbital neglected after orthogonalisation.
- Evidence: none

### Step 2: Compute potential energy surfaces
- Role: process
- Action: For each of the three Ni surface orientations—(111), (100), and (110)—set up a grid of lateral adsorption positions across the surface unit cell. At each position, determine the equilibrium vertical distance by maximising the overlap between the hydrogen 2p orbitals and the metal d wavefunctions, then compute the total electronic energy of the H+Ni system. Calculate the adsorption energy as the difference between the H+surface energy and the sum of the clean surface energy plus the isolated H atom’s energy. Store the adsorption energy at every grid point.
- Evidence: none

### Step 3: Write adsorption energies at most favourable sites
- Role: scored (load-bearing)
- Action: From the energy scans, identify the adsorption energy value at the energetically most favourable site on each surface. Write a CSV file with the surface label and the corresponding adsorption energy (in kcal/mol).
- Output file: `/app/outputs/adsorption_energies.csv`
- Format: csv
- Contract: surface (string), adsorption_energy_kcal_per_mol (float). Rows: Ni(111), Ni(100), Ni(110).
- Scoring: scored by hidden verifier

### Step 4: Write energy variation on Ni(111)
- Role: scored (load-bearing)
- Action: From the Ni(111) energy scan, compute the maximum variation of the adsorption energy across the surface unit cell (maximum energy minus minimum energy). Write a CSV file containing this single value in kcal/mol.
- Output file: `/app/outputs/energy_variation_n111.csv`
- Format: csv
- Contract: max_variation_kcal_per_mol (float). Single value.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_energies.csv`
- `/app/outputs/energy_variation_n111.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_energies.csv
- path: `/app/outputs/adsorption_energies.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: The theoretical adsorption energies of hydrogen on Ni(111), Ni(100), and Ni(110) at the energetically most favourable site, as computed by the semiempirical model. The checker will compare each surface’s energy to a hidden reference value with a tolerance, giving full credit if the absolute deviation is within the tolerance and no credit if outside.
- schema:
  - `type`: table
  - `required_columns`: `surface`, `adsorption_energy_kcal_per_mol`
  - `description`: Each row gives the surface label and the computed adsorption energy in kcal/mol for that face at its most favourable site.

### energy_variation_n111.csv
- path: `/app/outputs/energy_variation_n111.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: The greatest energy barrier for hydrogen diffusion on Ni(111) computed from the energy profile. The checker will verify that the reported value does not exceed a hidden threshold, awarding full credit if the value is at or below the threshold and no credit otherwise.
- schema:
  - `type`: table
  - `required_columns`: `max_variation_kcal_per_mol`
  - `description`: A single row containing the maximum variation of the adsorption energy across the Ni(111) surface unit cell (max – min) in kcal/mol.

Notes: The model parameters and wavefunctions are fully specified in the Model specification section; no external data files are needed. The agent must implement the Hamiltonian and the two-dimensional scans from the description. The checker performs a result-level compare: for adsorption energies it compares each surface’s value against a hidden reference value with a tolerance, and for the variation it accepts any value at or below a hidden threshold. All gold values and tolerances are hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "surface",
          "adsorption_energy_kcal_per_mol"
        ],
        "description": "Each row gives the surface label and the computed adsorption energy in kcal/mol for that face at its most favourable site."
      },
      "description": "The theoretical adsorption energies of hydrogen on Ni(111), Ni(100), and Ni(110) at the energetically most favourable site, as computed by the semiempirical model."
    },
    {
      "file": "energy_variation_n111.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "max_variation_kcal_per_mol"
        ],
        "description": "A single row containing the maximum variation of the adsorption energy across the Ni(111) surface unit cell (max - min) in kcal/mol."
      },
      "description": "The greatest energy barrier for hydrogen diffusion on Ni(111) computed from the energy profile."
    }
  ],
  "notes": "All gold values and tolerances are hidden. The agent must compute these quantities from the model."
}
```

## How you are scored
Each scored artifact—adsorption_energies.csv and energy_variation_n111.csv—is independently evaluated by a hidden verifier. For adsorption energies, the verifier compares your computed energy for each surface to a hidden reference value with a tolerance; meeting the tolerance (absolute deviation ≤ tolerance) earns full credit for that surface, and exceeding the tolerance earns zero credit. For the energy variation, the verifier checks that your reported maximum variation does not exceed a hidden threshold; values at or below the threshold receive full credit, values above the threshold receive zero credit. The final reward is a weighted combination of these checks. Merely writing known literature values without running the model will not satisfy the requirements; the scoring rewards faithful execution of the required workflow.