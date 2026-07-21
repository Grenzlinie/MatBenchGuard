# Dislocation Elastic Limit Calculation Workflow

## Problem background
Dislocations are line defects in crystals that mediate plastic deformation. In face-centered cubic (FCC) crystals, dislocations can exist in several configurations depending on the glide plane and the angle between the dislocation line and the Burgers vector. The critical resolved shear stress required to move a dislocation — the elastic limit or Peierls stress — is a fundamental quantity that determines which slip systems are active. The present work develops a modified Peierls model that avoids the complete smearing of atomic forces used in the original treatment. Instead, it retains some atomic discreteness and accounts for the finite size of atoms by convolving the forces with a Gaussian distribution of width parameter \(s\) (the smoothing length). The model yields closed-form expressions for the normalized elastic limit \(\tau_{\text{el}}/G\) (ratio of elastic limit to shear modulus) for six dislocation types on the {010} and {111} planes of an FCC crystal like aluminum. The goal is to compute these six \(\tau_{\text{el}}/G\) values from the model using a fixed smoothing parameter \(s/b = 0.456\) and Poisson’s ratio \(\mu = 0.343\), and to output them in a specified format.

## Mathematical formulation

### Auxiliary integral for half‑dislocations

The factor \(R(p)\) that appears in the elastic limit of the half‑dislocations is defined through the integral

\[
I(p)=\int_{-\infty}^{\infty}\Bigl[\frac{3}{2}
-2\cos\!\Bigl(\frac{2}{3}\arctan z\Bigr)
+\cos\!\Bigl(\frac{4}{3}\arctan z\Bigr)\Bigr]\cos(pz)\,dz
\]

and the transformation

\[
R(p)=\sqrt{3}\,p\,e^{p}\,I(p).
\]

The variable \(p\) is given by \(p=4\pi\sigma/h\).  The numerical values of \(p\) for the two half‑dislocations are obtained from the known \(\sigma/h\) ratios (see below).

### Auxiliary function for the (111) full dislocations

For the (111) 90° and 30° dislocations the factor \(|f(\eta,\sigma)|\) is defined by

\[
\begin{aligned}
f(\eta,\sigma)=\Bigl(1+\eta\frac{\eta-\sqrt{3}\sigma}{\eta^{2}+\sigma^{2}}\Bigr)
&\cos\!\Bigl(4\pi\frac{\eta}{h}\Bigr) \\
+\sigma\frac{\eta-\sqrt{3}\sigma}{\eta^{2}+\sigma^{2}}
&\sin\!\Bigl(4\pi\frac{\eta}{h}\Bigr).
\end{aligned}
\]

The parameters \(\eta\) and \(\sigma\) are determined by the geometry of the glide plane and the Poisson ratio \(\mu\); their relation is taken from Part I (Leibfried & Dietze 1951).

### Elastic‑limit formulas

Using the parameters \(s/b=0.456\) and \(\mu=0.343\) the normalized elastic limits \(\tau_{\text{el}}/G\) for the six dislocation types are:

**1. (010) 90°**  
\[
\frac{\tau_{(010)}^{90^\circ}}{G}=
2\,e^{-4\pi\sigma/b}\,e^{-(2\pi s/b)^{2}},
\qquad \sigma=a/2.
\]

**2. (010) 0°**  
\[
\frac{\tau_{(010)}^{0^\circ}}{G}=
2\,\frac{\sigma}{a}\,e^{-2\pi\sigma/b}\,e^{-(\pi s/b)^{2}},
\qquad \sigma=\frac{a}{2(1-\mu)}.
\]

**3. (111) 0° half‑dislocation**  
\[
\frac{\tau_{(111)}^{0^\circ,\frac12}}{G}=
\frac{3\sqrt{3}}{4\pi^{2}}\,\frac{b^{2}}{c\,h}
\,e^{-4\pi\sigma/h}\,e^{-(2\pi s/h)^{2}}\,R(p),
\qquad
\frac{\sigma}{c}=\frac{\pi}{3\sqrt{3}(1-\mu)},\;p=4\pi\frac{\sigma}{h}.
\]

**4. (111) 120° half‑dislocation**  
\[
\frac{\tau_{(111)}^{120^\circ,\frac12}}{G}=
\frac{9}{8\pi^{2}}\,\frac{b^{2}}{c\,h}
\,e^{-4\pi\sigma/h}\,e^{-(2\pi s/h)^{2}}\,R(p),
\qquad
\frac{\sigma}{c}=\frac{\pi(4-3\mu)}{12\sqrt{3}(1-\mu)},\;p=4\pi\frac{\sigma}{h}.
\]

**5. (111) 90°**  
\[
\frac{\tau_{(111)}^{90^\circ}}{G}=
2\,\frac{b}{h}\,\frac{\sigma}{c}
\,e^{-4\pi\sigma/h}\,e^{-(2\pi s/h)^{2}}\,|f(\eta,\sigma)|.
\]

**6. (111) 30°**  
\[
\frac{\tau_{(111)}^{30^\circ}}{G}=
2\,\frac{\sigma}{c}
\,e^{-4\pi\sigma/h}\,e^{-(2\pi s/h)^{2}}\,|f(\eta,\sigma)|.
\]

### Geometric parameters

All quantities are evaluated at \(\mu=0.343\) and \(s/b=0.456\).

**Table of directly used numbers (from the paper)**

| Dislocation type       | \(\sigma/a\) or \(\sigma/c\) |
|------------------------|--------------------------------|
| (010) 90°              | \(\sigma/a = 0.50\)          |
| (010) 0°               | \(\sigma/a = 0.76\)          |
| (111) 0° half          | \(\sigma/c = 0.92\)          |
| (111) 120° half        | \(\sigma/c = 0.68\)          |
| (111) 90°              | \(\sigma/c = 0.96\)          |
| (111) 30°              | \(\sigma/c = 1.38\)          |

The Burgers vector \(b\) in the (010) plane is the translation vector of the square lattice, i.e. \(b=a\) (the lattice constant).  The lattice constant of aluminium, \(a_0=4.05\) Å, cancels out of all dimensionless ratios.

**Geometric relations for the (111) plane (from Part I)**  
The interplanar spacing \(c\) and the period \(h\) together with the Burgers vector \(b\) satisfy the crystallographic relations
\[
\frac{c}{h}=\frac{\sqrt{2}}{\sqrt{3}}\approx0.816,\qquad
\frac{b}{h}=1.
\]
For the half‑dislocations the Burgers vector is \(b_{\text{half}}=b/\sqrt{3}\) and the above values remain valid with the appropriate \(b\).

The parameters \(\eta\) and \(\sigma\) for the (111) 90° and 30° dislocations are given by the following expressions derived in Part I (Leibfried & Dietze 1951):
\[
\frac{\sigma}{c}= \frac{\pi}{3\sqrt{3}}\,\frac{2-\mu}{1-\mu},\qquad
\frac{\eta}{c}= \frac{\pi}{12\sqrt{3}}\,\frac{1-2\mu}{1-\mu}\;\;(\text{for }90^\circ),
\]
\[
\frac{\sigma}{c}= \frac{\pi}{12\sqrt{3}}\,\frac{4-3\mu}{1-\mu},\qquad
\frac{\eta}{c}= \frac{\pi}{12\sqrt{3}}\,\frac{3\mu-2}{1-\mu}\;\;(\text{for }30^\circ).
\]
With \(\mu=0.343\) these give \(\sigma/c=0.96,\;\eta/c=0.031\) for 90° and \(\sigma/c=1.38,\;\eta/c=-0.021\) for 30°, consistent with the table above.  The dimensionless products \(\sigma/h\) and \(\eta/h\) are obtained by multiplying by \(c/h\) ( = 0.816).  The exponential factors are then evaluated with these \(\sigma/h\) and with \(s/h = (s/b)\cdot(b/h)\).

## Approach
The workflow proceeds by evaluating the above formulas numerically: (i) compute the integral \(I(p)\) via adaptive quadrature to obtain \(R(p)\); (ii) compute \(f(\eta,\sigma)\) using the expressions for \(\eta\) and \(\sigma\); (iii) evaluate the six elastic‑limit formulas with \(s/b=0.456\), \(\mu=0.343\) and the geometric parameters listed above.  The results are written to the output CSV.

## Reproduction target
Produce a CSV file named `elastic_limits.csv` containing the normalized elastic limit \(\tau_{\text{el}}/G\) for the six specified dislocation types. The file must have exactly six data rows (no header) with two columns: `dislocation_type` (string) and `tau_over_G` (float). The rows must appear in this fixed order: (010)90°, (010)0°, (111)0°half, (111)120°half, (111)90°, (111)30°. The computations should use the model parameters \(s/b = 0.456\) and Poisson’s ratio \(\mu = 0.343\), and the geometric parameters \(\sigma/a\) or \(\sigma/c\) given in the workflow steps. You must implement the numerical evaluation of the auxiliary functions \(R(p)\) and \(|f|\) from their definitions.

## Assets

- NumPy: numpy
- SciPy: scipy
- Matplotlib: matplotlib

## Workflow steps

### Step 1: Compute auxiliary function R(p)
- Role: process
- Action: Implement the integral I(p) that defines the auxiliary function, using numerical integration. Compute R(p) = I(p) * p * exp(p) * (3/√3) for the required p values corresponding to the (111) 0° and 120° half-dislocations. The parameter p is given by 4πσ/h, with σ/h derived from the known geometric parameters and Poisson's ratio μ=0.343.
- Evidence: none

### Step 2: Compute auxiliary function f(eta,sigma)
- Role: process
- Action: Using the analytical definition of |f(η,σ)| and the known relationships between η, σ, and Poisson's ratio μ, compute its value at μ=0.343 for the (111) 90° and 30° dislocations. This value is needed in the final elastic limit formulas.
- Evidence: none

### Step 3: Compute elastic limits for all dislocation types
- Role: scored (load-bearing)
- Action: Using the analytical elastic limit formulas for each dislocation type, together with the precomputed R(p) and |f|, calculate the normalized elastic limit τ_el/G for the six dislocation types: (010) 90°, (010) 0°, (111) 0° half, (111) 120° half, (111) 90°, (111) 30°. Use the given parameters s/b=0.456 and μ=0.343. Output the results in the specified CSV file.
- Output file: `/app/outputs/elastic_limits.csv`
- Format: csv
- Contract: Columns: dislocation_type (str), tau_over_G (float). No header row expected; rows in the fixed order above.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_limits.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_limits.csv
- path: `/app/outputs/elastic_limits.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Normalized elastic limits τ_el/G for the six dislocation configurations. The hidden checker recomputes the values using the same analytical formulas and compares each row with a relative tolerance; the fraction of rows within tolerance determines the score.
- schema:
  - `type`: table
  - `required_columns`: `dislocation_type`, `tau_over_G`
  - `description`: dislocation_type is a string, tau_over_G is a float. No header row; rows must appear in the fixed order: (010)90°, (010)0°, (111)0°half, (111)120°half, (111)90°, (111)30°.

Notes: The agent must compute the auxiliary functions R(p) and |f| before evaluating the elastic‑limit formulas. The geometric parameters linking σ/h, σ/c, η, etc., to the Poisson ratio are fully stated in the instruction. The output CSV has no header and the row order is fixed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_limits.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "dislocation_type",
          "tau_over_G"
        ],
        "description": "dislocation_type is a string, tau_over_G is a float. No header row; rows must appear in the fixed order: (010)90°, (010)0°, (111)0°half, (111)120°half, (111)90°, (111)30°."
      },
      "description": "Normalized elastic limits τ_el/G for the six dislocation configurations. The hidden checker recomputes the values using the same analytical formulas and compares each row with a relative tolerance; the fraction of rows within tolerance determines the score."
    }
  ],
  "notes": "The agent must compute the auxiliary functions R(p) and |f| before evaluating the elastic‑limit formulas. The geometric parameters linking σ/h, σ/c, η, etc., to the Poisson ratio are fully stated in the instruction. The output CSV has no header and the row order is fixed."
}
```

## How you are scored
The hidden verifier holds a reference implementation of the same analytical formulas. It reads your `elastic_limits.csv` and independently computes the expected `tau_over_G` for each dislocation type. For every row, it compares your value to the expected value. If the difference is within a pre‑specified relative tolerance, the row earns credit. The overall reward is the fraction of rows that pass the tolerance check. Make sure the file has the exact format (no header, correct column separator, exact row order) and that the numerical values are computed accurately.
