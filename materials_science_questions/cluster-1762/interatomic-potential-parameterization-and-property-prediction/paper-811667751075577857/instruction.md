# Edge Energy Computation of Alkali Halide Crystals

## Problem background
Alkali halide crystals possess edge energies that influence their thermodynamic properties, such as the heat of solution and particle-size dependence of solubility. Accurate computation of these energies requires a realistic interionic potential. This work computes the energy of an undistorted <100> edge for sodium-chloride-type crystals using a Born–Mayer potential that includes Coulomb, van der Waals (dipole–dipole and dipole–quadrupole), and exponential repulsive terms. The aim is to quantify the edge energy per unit length for a set of alkali halides and to evaluate the contribution of van der Waals forces to the edge energy.

## Approach
The edge energy per unit length is obtained from the interaction energies between diagonally opposite quadrants of an infinite crystal divided along crystallographic planes. Using an additive central-force model, the total edge energy is expressed as the sum of electrostatic, van der Waals (dipole–dipole and dipole–quadrupole), and exponential repulsive contributions. The expression contains lattice sums that depend only on the lattice geometry; these are evaluated from rapidly convergent series expansions involving modified Bessel functions and exponentials. The interatomic potential parameters (repulsive constants b, b_i, ρ and van der Waals coefficients c_ij, d_ij) are taken from the published literature (Huggins & Mayer 1933; Mayer 1933). Pauling factors f++ = 1.25, f-- = 0.75, f+- = 1.00 are used for the repulsive term. The equilibrium nearest-neighbor distances a0 for each crystal are adopted from values derived by Shuttleworth (1949) from the same potential constants. Edge energies are then computed for eight alkali halide crystals: NaF, NaCl, NaBr, NaI, KF, KCl, KBr, and KI.

## Formulas

The edge energy per unit length κ (in erg cm⁻¹) for a <100> edge is given by

$$
\kappa = \frac{2}{a_0} \left[ \frac{e^2}{a_0} B_1 - \frac{1}{a_0^6} \left( c_{+-} D_6' + \frac{c_{++} + c_{--}}{2} D_6'' \right) - \frac{1}{a_0^8} \left( d_{+-} D_8' + \frac{d_{++} + d_{--}}{2} D_8'' \right) + b \left( \frac{1.25 b_+^2 + 0.75 b_-^2}{2} e^{-\sqrt{2}a_0/\rho} + 2 b_+ b_- e^{-\sqrt{3}a_0/\rho} \right) \right]
$$

where $a_0$ is the nearest-neighbor distance (cm), $e = 4.77 \times 10^{-10}$ e.s.u., $c_{ij}$ and $d_{ij}$ are the van der Waals coefficients, $b$, $b_i$, $\rho$ are the repulsive constants, and the Pauling factors are $f_{++}=1.25$, $f_{--}=0.75$, $f_{+-}=1.00$.

To express κ in the target unit of $10^{-6}$ erg cm⁻¹, multiply the value obtained from the formula by $10^6$.

The lattice sums are defined as

$$
B_1 = \sum_{k,l=1}^{\infty} \sum_{m=-\infty}^{\infty} (-1)^{k+l+m} k l \, (k^2 + l^2 + m^2)^{-1/2},
$$
$$
D_6' = \sum_{\substack{k,l=1 \\ k+l+m\ \text{odd}}}^{\infty} \sum_{m=-\infty}^{\infty} k l \, (k^2 + l^2 + m^2)^{-3},
$$
$$
D_6'' = \sum_{\substack{k,l=1 \\ k+l+m\ \text{even}}}^{\infty} \sum_{m=-\infty}^{\infty} k l \, (k^2 + l^2 + m^2)^{-3},
$$
$$
D_8' = \sum_{\substack{k,l=1 \\ k+l+m\ \text{odd}}}^{\infty} \sum_{m=-\infty}^{\infty} k l \, (k^2 + l^2 + m^2)^{-4},
$$
$$
D_8'' = \sum_{\substack{k,l=1 \\ k+l+m\ \text{even}}}^{\infty} \sum_{m=-\infty}^{\infty} k l \, (k^2 + l^2 + m^2)^{-4}.
$$

To evaluate these efficiently, the following rapidly convergent series are used:

$$
B_1 = 4 \sum_{k,l=1}^{\infty} \sum_{\substack{m=1 \\ m\ \text{odd}}}^{\infty} (-1)^{k+l} k l \, K_0\bigl(\pi m \sqrt{k^2+l^2}\bigr),
$$
where $K_0$ is the modified Bessel function of the second kind of order zero.

For $D_{2n}'$ and $D_{2n}''$ with integer $n$ (here $n=3$ for $D_6$ and $n=4$ for $D_8$), define the auxiliary sum

$$
S_{t} = \sum_{k,l=1}^{\infty} k l \, (k^2 + l^2)^{-t/2}.
$$

Then

$$
\begin{aligned}
D_{2n}' = &\; \frac{\pi}{2^{\,n-1}(n-1)!} \Bigg[ \frac{(2n-2)!}{2^{\,n}(n-1)!} S_{2n-1} \\
& + \pi^{\,n-1} \Bigg( \sum_{\substack{k,l=1 \\ k+l\ \text{odd}}}^{\infty} \sum_{m=1}^{\infty} T_n(k,l,m) + \sum_{\substack{k,l=1 \\ k+l\ \text{even}}}^{\infty} \sum_{m=1}^{\infty} (-1)^{m} T_n(k,l,m) \Bigg) \Bigg], \\[6pt]
D_{2n}'' = &\; \frac{\pi}{2^{\,n-1}(n-1)!} \Bigg[ \frac{(2n-2)!}{2^{\,n}(n-1)!} S_{2n-1} \\
& + \pi^{\,n-1} \Bigg( \sum_{\substack{k,l=1 \\ k+l\ \text{even}}}^{\infty} \sum_{m=1}^{\infty} T_n(k,l,m) + \sum_{\substack{k,l=1 \\ k+l\ \text{odd}}}^{\infty} \sum_{m=1}^{\infty} (-1)^{m} T_n(k,l,m) \Bigg) \Bigg],
\end{aligned}
$$

where

$$
T_n(k,l,m) = \frac{k l \, m^{n-1}}{(k^2+l^2)^{n/2}} \exp\!\bigl(-\pi m \sqrt{k^2+l^2}\bigr) \sum_{\nu=0}^{n-1} \frac{(n-1+\nu)!}{\nu!\,(n-1-\nu)!} \frac{1}{\bigl(2\pi m \sqrt{k^2+l^2}\bigr)^{\nu}}.
$$

The required $S_t$ values for $t=5$ (used for $D_6$) and $t=7$ (used for $D_8$) can be computed directly from the definition $S_t = \sum_{k,l=1}^{\infty} k l (k^2+l^2)^{-t/2}$; these sums converge quickly. The known published values of the lattice sums (obtained with high precision) are provided for reference and self-check:

- $B_1 = 0.0218226$
- $D_6' = 0.2302882$, $D_6'' = 0.2858930$
- $D_8' = 0.03683796$, $D_8'' = 0.07487899$

The final scoring uses the edge energies derived from these sums; the numbers above are not a pass/fail target but a consistency check.

## Reproduction target
Compute the total edge energy per unit length κ (in units of 10⁻⁶ erg cm⁻¹) for the <100> edge of the eight alkali halide crystals: NaF, NaCl, NaBr, NaI, KF, KCl, KBr, KI. The computation must use the derived Born–Mayer expression with the lattice sums numerically evaluated from the series formulas, the potential parameters from Huggins & Mayer (1933) and Mayer (1933), the Pauling factors listed above, and the nearest-neighbor distances a0 from Shuttleworth (1949). Output a CSV file with two columns: Crystal (string) and kappa (float). The eight rows must correspond exactly to the eight crystals in the order given.

## Assets

- Huggins and Mayer (1933) - Repulsive parameters for alkali halides: 10.1063/1.1749330
- Mayer (1933) - van der Waals coefficients for alkali halides: 10.1063/1.1749291
- Shuttleworth (1949) - Equilibrium nearest-neighbor distances a0: 10.1088/0370-1298/62/3/304

## Workflow steps

### Step 1: Compute lattice sums B1, D6', D6'', D8', D8''
- Role: process
- Action: Evaluate the five lattice sums B1, D6', D6'', D8', D8'' appearing in the edge energy expression using rapidly convergent series formulas involving modified Bessel functions and exponentials. Use the parity-separated lattice sum definitions given in the derivation. Output the computed numeric values to an evidence file.
- Evidence: `/app/outputs/lattice_sums.csv`

### Step 2: Compute total edge energies for alkali halide crystals
- Role: scored (load-bearing)
- Action: For each crystal (NaF, NaCl, NaBr, NaI, KF, KCl, KBr, KI), compute the total <100> edge energy κ using the edge energy formula that combines electrostatic, van der Waals (dipole-dipole and dipole-quadrupole), and exponential repulsive contributions. Use the lattice sums from the previous step, interatomic potential parameters from Huggins & Mayer (1933) and Mayer (1933), the Pauling factors (f++=1.25, f--=0.75, f+-=1.00), and the equilibrium nearest-neighbor distances a0 from Shuttleworth (1949). Output a CSV with two columns: Crystal and kappa (edge energy in 10⁻⁶ erg cm⁻¹).
- Output file: `/app/outputs/edge_energies.csv`
- Format: csv
- Contract: Two columns: 'Crystal' (str, one of NaF, NaCl, NaBr, NaI, KF, KCl, KBr, KI) and 'kappa' (float, edge energy in 10⁻⁶ erg cm⁻¹).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lattice_sums.csv` (evidence from Step 1)
- `/app/outputs/edge_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### edge_energies.csv
- path: `/app/outputs/edge_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Total edge energy per unit length of <100> edge for eight alkali halide crystals, computed from the Born-Mayer interionic potential including Coulomb, van der Waals, and repulsive terms.
- schema:
  - `type`: table
  - `required_columns`: `Crystal`, `kappa`
  - `units`:
    - `kappa`: 10⁻⁶ erg cm⁻¹

Notes: The checker compares the reported kappa values to the hidden paper reference values with a relative tolerance. The lattice sums used in the computation must be computed by the agent; the paper's published numeric sums may not be directly copied.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "edge_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Crystal",
          "kappa"
        ],
        "units": {
          "kappa": "10⁻⁶ erg cm⁻¹"
        }
      },
      "description": "Total edge energy per unit length of <100> edge for eight alkali halide crystals, computed from the Born-Mayer interionic potential including Coulomb, van der Waals, and repulsive terms."
    }
  ],
  "notes": "The checker compares the reported kappa values to the hidden paper reference values with a relative tolerance. The lattice sums used in the computation must be computed by the agent; the paper's published numeric sums may not be directly copied."
}
```

## How you are scored
A hidden verifier scores your submission. The verifier reads your `edge_energies.csv`, extracts the `kappa` value for each crystal, and compares each to a hidden reference value. The reward is the fraction of the eight crystals for which the absolute relative error (|computed − reference| / |reference|) is within a hidden tolerance. Full credit requires all eight values to be within tolerance; partial credit is proportional to the number of crystals meeting the tolerance. The lattice sums evidence file (`lattice_sums.csv`) is also checked for completeness and consistency with the workflow, but the numerical score is determined solely by the edge energy results. Reporting correct numbers alone is not sufficient: the verifier expects that the values are produced by the computational procedure described in the workflow steps and that all required output files are present.
