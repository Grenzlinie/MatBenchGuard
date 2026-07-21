# Monte Carlo Simulation of Polymer Brush Mechanical Response

## Problem background
Surfaces that are modified by grafting polymer chains can change mechanical properties without altering the bulk material. This work models a polymer brush on an elastic substrate, treating the brush as a discrete lattice of rotators with orientational (Keesom) interactions and a Lennard-Jones potential, while the substrate obeys Hooke's law. Monte Carlo simulations are used to compute the equilibrium response when the system is stretched. The open question is how the brush influences the effective force and Young's modulus of the composite as a function of the applied strain and the strength of inter-chain coupling.

## Approach
Implement the hybrid discrete-continuum model: a three-dimensional lattice of rigid rotators of length *l* that interact via an orientation-dependent dipole potential (Keesom energy) with parameters K₁ (longitudinal), K₂ (strain-dependent transverse) and K₃ (constant transverse), plus a Lennard-Jones contribution. The substrate provides an elastic restoring energy proportional to the square of the displacement. Normalize all energies by K₁ and lengths by the mean interatomic distance *a*. Set up the lattice with periodic boundaries in one transverse direction, a fixed attachment at the substrate, and free upper ends. Perform quasistatic loading: at each small strain increment, apply the macroscopic deformation, update the geometry, run Metropolis Monte Carlo equilibration at a fixed normalized temperature T* to obtain the total equilibrium energy. From the strain-dependent energy, apply work–energy relations to extract the normalized force and normalized Young's modulus. Explore three values of the inter-chain coupling K₃ (0.1, 0.05, 0.01, with K₁ = 1) to compare the mechanical response curves. The approach does not require an external dataset; the simulation itself is the experiment.

## Model details (missing information from the paper)

### Hamiltonian
The total energy of the system is

\[
H = \sum_{i=1}^{3} \sum_{\langle \vec{n},\vec{m}\rangle} H_{\vec{n},\vec{m}}^{(i)}
\;+\;
4\varepsilon\left[\left(\frac{\sigma}{r}\right)^{12} - \left(\frac{\sigma}{r}\right)^{6}\right]
\;+\;
\frac{1}{2}k\,(\Delta x)^2\,
.
\]

Here:
- \(\langle \vec{n},\vec{m}\rangle\) denotes nearest neighbours in the direction \(i\).
- The orientational interaction energy for a pair is the Keesom (dipole) term
  \[
  H_{\vec{n},\vec{m}}^{(i)} = -K_i \frac{(\vec{l}_{\vec{n}} \cdot \vec{l}_{\vec{m}})}{l^{2}},
  \]
  where \(\vec{l}_{\vec{n}}\) is the vector of the rotator at node \(\vec{n}\).
- The three interaction constants are:
  * \(K_1\) – longitudinal (along the chain, direction \(n_1\));
  * \(K_2\) – strain‑dependent transverse (direction \(n_2\));
  * \(K_3\) – constant transverse (direction \(n_3\)).

### Strain dependence of \(K_2\)
During deformation the transverse distance \(r\) between nearest chain segments in the \(n_2\) direction changes. The parameter \(K_2\) must be updated according to

\[
K_2 = K_3\left(\frac{r}{r_0}\right)^{-3},
\]

where \(r_0\) is the equilibrium average segment distance in the \(n_2\) direction (taken as the mean interatomic distance \(a=1\) in normalized units) and \(r\) is the actual distance evaluated from the current coordinates of the two neighbouring segments. Thus at each strain step, after the geometric deformation is applied, \(r\) is computed (e.g., as the mean centre‑to‑centre distance of nearest \(n_2\) neighbours) and \(K_2\) is updated before the Monte Carlo relaxation.

### Lennard‑Jones contribution
The term \(4\varepsilon[(\sigma/r)^{12}-(\sigma/r)^{6}]\) acts between nearest segments and uses the same distance \(r\) (the actual centre‑to‑centre spacing). In normalized units the values are

\[
\varepsilon = 1.0 \quad (\text{in units of }K_1),\qquad
\sigma = 1.0 \quad (\text{in units of }a).
\]

### Substrate elastic energy
The substrate is treated as a Hookean spring with stiffness constant \(k\). The elastic energy stored is \(\frac{1}{2}k(\Delta x)^2\). In normalized form we choose \(k\) such that the energy is measured consistently with the polymer part. A convenient choice is to set the dimensionless substrate constant to \(1\), i.e.

\[
\frac{k a^{2}}{K_1} = 1 \quad\Longrightarrow\quad H_{\text{subs}}/K_1 = \frac{1}{2}\left(\frac{\Delta x}{a}\right)^{2}.
\]

### Normalization and system size
All energies are divided by \(K_1\) (\(\sim 10^{-20}\,\mathrm{J}\)). All lengths are divided by the mean interatomic distance in the substrate \(a\) (\(\sim 10^{-10}\,\mathrm{m}\)).
- Rotator length: \(l = 1\).
- Lattice dimensions: \(N_1 = N_2 = N_3 \approx 10\).
- Initial distance between segment centres in each direction: \(1\) (in units of \(a\)).
- The initial length of the system along the stretching direction (\(n_1\)) is \(x_0 = N_1\,l = N_1\).
- Periodic boundary conditions are applied in the \(n_3\) direction; the first layer (\(n_1=1\)) is fixed on the substrate; the top layer (\(n_1=N_1\)) is free.
- Normalized temperature: \(T^{*} = k_B T / K_1 = 0.1\).

### Quasistatic deformation protocol
The system is strained by a small amount \(\Delta x\), expressed as the relative strain \(\varepsilon = \Delta x / x_0\). In practice the following steps are repeated for each strain increment:
1. Impose the macroscopic strain by scaling the \(n_1\) coordinates of all segment centres linearly:
   \[
   x_{\text{new}} = x_{\text{old}} \; (1 + \varepsilon).
   \]
2. Recalculate all nearest‑neighbour distances \(r\) (especially in the \(n_2\) direction) and update \(K_2\) using the formula above.
3. Update the substrate energy \(H_{\text{subs}} = \tfrac{1}{2} (\varepsilon N_1)^2\) (in normalized units).
4. Perform Metropolis Monte Carlo sweeps at \(T^{*}=0.1\) to equilibrate the orientational degrees of freedom. Record the total energy \(H\) of the relaxed configuration.

### Work‑energy relations to obtain force and modulus
The external work \(A = - \Delta H\) is related to force \(F\) and Young’s modulus \(E\) by

\[
A = -\frac{F \Delta x}{2} = -\frac{E}{2} \left(\frac{\Delta x}{x_0}\right)^2 .
\]

Thus:

\[
F = 2\frac{\Delta H}{\Delta x}, \qquad
E = 2\frac{\Delta H}{\varepsilon^2}.
\]

The required outputs are the **normalized force** \(F \cdot a / K_1\) and the **normalized Young’s modulus** \(E / E_0\).  
The reference substrate modulus \(E_0\) is defined by the substrate alone: from Hooke’s law, the substrate force is \(F_{\text{subs}} = k \Delta x\) and the substrate Young’s modulus is \(E_0 = k x_0\). With our normalization \(k a^{2}/K_1 = 1\) and \(x_0 = N_1\), we obtain

\[
\frac{E_0 a}{K_1} = N_1,
\]

so \(E/E_0\) is obtained from the computed \(E\) and \(N_1\).

## Reproduction target
Compute and output the normalized force (*F·a/K₁*) and normalized Young's modulus (*E/E₀*, where *E₀* is the substrate modulus) as functions of the relative strain (*Δx/x₀*) for three values of the transverse coupling parameter: *K₃* = 0.1, 0.05, and 0.01, with *K₁* = 1 and normalized temperature *T** = 0.1. Use a representative lattice size (e.g., *N₁* = *N₂* = *N₃* ≈ 10). The results must be written to a CSV file with columns: K3, strain, force_normalized, youngs_modulus_normalized. Each row corresponds to one strain step for one *K₃* value. The curves must be produced by the simulation workflow described in the steps below.

## Assets

- Python 3: python
- NumPy: numpy

## Workflow steps

### Step 1: Monte Carlo simulation of stretching
- Role: process
- Action: Implement the Hamiltonian with the orientational interactions, the Lennard‑Jones potential, and the substrate elastic energy, all normalized as described in “Model details”. Set up a lattice of rotators with N₁=N₂=N₃≈10, periodic boundaries in n₃, fixed attachment at the substrate, free upper ends. For each quasistatic strain step and for K₃ ∈ {0.1, 0.05, 0.01} at K₁=1, apply the macroscopic strain, update K₂ via \(K_2 = K_3 (r/r_0)^{-3}\), update the substrate energy, and run Metropolis Monte Carlo equilibration at T*=0.1. Record the equilibrium total energy at every strain.

### Step 2: Extract force and Young's modulus
- Role: scored (load-bearing)
- Action: From the recorded equilibrium energies for each K₃ and strain, apply the work–energy relations \(A = -\Delta H\), \(A = -F \Delta x/2 = -(E/2)(\Delta x/x_0)^2\) to compute normalized force (F·a/K₁) and normalized Young's modulus (E/E₀) as functions of strain. Export the results as a CSV file.
- Output file: `/app/outputs/mechanical_curves.csv`
- Format: csv
- Contract: CSV with header: K3, strain, force_normalized, youngs_modulus_normalized. Each row corresponds to one strain step for one K₃ value. All columns are floats.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mechanical_curves.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mechanical_curves.csv
- path: `/app/outputs/mechanical_curves.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Normalized force (F·a/K₁) and normalized Young's modulus (E/E₀) as functions of relative strain for K₃ = 0.1, 0.05, 0.01. Each row is a strain step for one K₃ value.
- schema:
  - `type`: table
  - `required_columns`: `K3`, `strain`, `force_normalized`, `youngs_modulus_normalized`

## How you are scored
A hidden verifier examines the submitted `mechanical_curves.csv` independently. The scoring is based on structural properties of the curves, not on matching specific numeric values. The verifier will:
- Confirm the CSV has the required columns and at least 10 rows per K₃ value.
- Verify that `force_normalized` ≥ `strain` for every row (non‑negative polymer contribution).
- Check that within each K₃ group, `youngs_modulus_normalized` is monotonically non‑increasing with strain.
- Check that the initial (near‑zero strain) modulus values satisfy E(0.1) > E(0.05) > E(0.01).
- Verify that the final modulus at the highest strain is ≤ 1.05 for each K₃, indicating that the coating influence vanishes and the system is substrate‑dominated.

No explicit peak‑and‑plateau detection is performed; the listed structural checks capture the essential trends reported in the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mechanical_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "K3",
          "strain",
          "force_normalized",
          "youngs_modulus_normalized"
        ]
      },
      "description": "Normalized force (F·a/K₁) and normalized Young's modulus (E/E₀) as functions of relative strain for K₃ = 0.1, 0.05, 0.01. Each row is a strain step for one K₃ value."
    }
  ],
  "notes": "The structural scoring verifies that force_normalized >= strain, Young's modulus decreases monotonically, initial moduli are ordered by K3, and final moduli converge to 1."
}
```