# Acoustic Phonon LA/TA Ratio in GaAs Quantum Wells and Heterostructures

## Problem background  
In a hot two‑dimensional electron gas (2DEG) formed in GaAs/AlGaAs heterostructures and quantum wells, the dominant energy relaxation at low temperatures occurs via emission of acoustic phonons. Understanding the angular and mode (longitudinal vs. transverse) distribution of these emitted phonons is essential for interpreting heat‑pulse experiments. Early isotropic models failed to explain the observed suppression of longitudinal acoustic (LA) phonons near the [100] direction. A comprehensive model is needed that includes the anisotropic electron–phonon matrix elements, dynamical RPA screening, finite 2DEG thickness through wavefunction form factors, and acoustic phonon focusing in the GaAs substrate.

The central quantity of interest is the LA/TA phonon emission ratio detected on the opposite side of the substrate. By computing this ratio for several quantum well widths and for a heterostructure, one can assess the importance of the above physical ingredients and compare with the experimentally observed trend.

## Approach  
The reproduction implements a linear response formalism for acoustic phonon emission by a quasi‑2D electron gas at a hot‑electron temperature \(T_e > T_{\text{lattice}}\). The model accounts for:

- **Phonon properties**: solving the Christoffel equation with the elastic constants of GaAs to obtain anisotropic phonon frequencies, group velocities, phase velocities, polarization vectors, and phonon focusing factors for the three acoustic branches. This maps wave‑vector space to real‑space propagation directions.
- **Form factors**: computing the ground‑state electron wavefunction in a finite‑depth confining potential (square well for quantum wells, triangular‑like for the heterostructure) and evaluating the form factors \(G(q_\perp)\) and \(g(q_\parallel)\).
- **RPA dynamical screening**: evaluating the finite‑temperature polarizability of a non‑interacting 2DEG and the full RPA dielectric function, including the Coulomb interaction and the form factor \(g(q_\parallel)\). The result enters the emission rate as the screened spectral function \(\text{Im}\{\chi/(1 - v g \chi)\}\).
- **Directional emission**: evaluating the emitted power per solid angle for each acoustic mode by combining the electron–phonon matrix element (deformation potential \(\Xi_D\) and piezoelectric coupling \(h_{14}\)) with the focusing factors, summing over all wave‑vector directions whose group velocity points to that real‑space direction.
- **Detector geometry**: projecting the flux onto the (001) wafer surface and integrating over a rectangular detector window (\(100\times 10\,\mu\text{m}\)) located centrally opposite a \(120\times 50\,\mu\text{m}\) 2DEG on a substrate of thickness \(0.4\,\text{mm}\).

The workflow chains these components into four sequential steps that produce the final LA/TA ratios.

## Mathematical model details  

### General emission rate (Eq. 1 of the paper)  

\[
P = \frac{2}{N V} \sum_{\mathbf{q}, \lambda} \omega_{\mathbf{q}\lambda} \left( N_{\mathbf{q}\lambda}^{T} - N_{\mathbf{q}\lambda}^{T_e} \right) \left| h_{\mathbf{q}\lambda} \right|^2 \left| G(q_{\perp}) \right|^2 \operatorname{Im}\!\left\{ \frac{\chi_{T_e}(\omega_{\mathbf{q}\lambda}, \mathbf{q}_{\parallel})}{1 - v(q_{\parallel}) g(q_{\parallel}) \chi_{T_e}(\omega_{\mathbf{q}\lambda}, \mathbf{q}_{\parallel})} \right\},
\]

where  
\(N_{\mathbf{q}\lambda}^{T} = (e^{\hbar\omega_{\mathbf{q}\lambda}/k_B T} - 1)^{-1}\) is the Bose factor at lattice temperature \(T\),  
\(N_{\mathbf{q}\lambda}^{T_e}\) is the Bose factor at electron temperature \(T_e\),  
\(\omega_{\mathbf{q}\lambda}\) is the phonon frequency,  
\(V\) is the crystal volume.

**Material parameters**:  
- Lattice temperature: \(T = 4.2\,\text{K}\) (bath temperature of the cold‑finger cryostat; all calculations use this fixed value).  
- GaAs mass density: \(\rho = 5320\,\text{kg}\,\text{m}^{-3}\).  
- GaAs background dielectric constant: \(\epsilon = 12.9\).  

---

### Electron‑phonon matrix element (Eq. 2)  

\[
h_{\mathbf{q}\lambda} = \sqrt{\frac{\hbar}{2 \rho \omega_{\mathbf{q}\lambda}}} \left[ i \Xi_D \, \mathbf{q}\!\cdot\!\mathbf{e}_{\mathbf{q}\lambda} + 2 e h_{14} \frac{ e_{\mathbf{q}\lambda_x} q_y q_z + e_{\mathbf{q}\lambda_z} q_x q_y + e_{\mathbf{q}\lambda_y} q_z q_x }{q^2} \right].
\]

- \(\Xi_D = 9\,\text{eV}\) – deformation‑potential coupling constant.  
- \(h_{14} = 1.4\times 10^9\,\text{eV}\,\text{m}^{-1}\) – piezoelectric constant.  
- \(\mathbf{e}_{\mathbf{q}\lambda}\) – polarization vector obtained from the Christoffel equation.

---

### Form factors for the finite well width  

The electron wavefunction \(\phi(z)\) (confinement direction \(z\)) yields:

\[
G(q_{\perp}) = \int_{-w/2}^{w/2} |\phi(z)|^2 e^{i q_{\perp} z} \, dz,
\qquad
g(q_{\parallel}) = \iint |\phi(z)|^2 |\phi(z')|^2 e^{-q_{\parallel} |z - z'|} \, dz \, dz'.
\]

Quantum wells: finite square‑well with barrier height \(350\,\text{meV}\).  
Heterostructure: triangular‑like well with conduction‑band offset \(225\,\text{meV}\) (wavefunction penetrates the barrier). Effective mass \(m^* = 0.067\,m_e\).

---

### Dynamical RPA screening  

2D Coulomb potential: \(v(q_{\parallel}) = \dfrac{2\pi e^2}{\epsilon \, q_{\parallel}}\).

Polarization function for a non‑interacting 2DEG:

\[
\chi_{T_e}(\omega, \mathbf{q}_{\parallel}) = \int \frac{d^2 k}{(2\pi)^2} \frac{ f(\epsilon_{\mathbf{k} + \mathbf{q}_{\parallel}}) - f(\epsilon_{\mathbf{k}}) }{ \hbar\omega + i\eta + \epsilon_{\mathbf{k}} - \epsilon_{\mathbf{k} + \mathbf{q}_{\parallel}} },
\]

with \(\epsilon_{\mathbf{k}} = \hbar^2 k^2 / (2 m^*)\) and \(f\) the Fermi–Dirac distribution at \(T_e = 50\,\text{K}\). The infinitesimal \(\eta \to 0^+\) is taken numerically. The screening function is

\[
S(\omega, \mathbf{q}_{\parallel}) = \operatorname{Im}\!\left\{ \frac{\chi_{T_e}(\omega, \mathbf{q}_{\parallel})}{1 - v(q_{\parallel}) g(q_{\parallel}) \chi_{T_e}(\omega, \mathbf{q}_{\parallel})} \right\}.
\]

---

### Directional emission in real space (Eq. 3)  

For a laboratory direction \(\hat{\mathbf{r}}\), the power per solid angle for mode \(\lambda\) is

\[
P_{\hat{r} \lambda} = \frac{2}{N (2\pi)^3} \sum_{i=1}^{N_{\mathbf{q}_\lambda}} \mathcal{A}_{\hat{\mathbf{q}}_i \lambda} \, P_{\hat{\mathbf{q}}_i \lambda},
\]

where the sum runs over all **wave‑vector directions** \(\hat{\mathbf{q}}_i\) whose group‑velocity unit vector \(\hat{\mathbf{v}}_{\hat{\mathbf{q}}_i \lambda}\) equals \(\hat{\mathbf{r}}\).  

The frequency‑integrated emission for a single \(\hat{\mathbf{q}}\) is

\[
P_{\hat{\mathbf{q}} \lambda} = \frac{1}{c_{\hat{\mathbf{q}} \lambda}^3} \int_{0}^{\infty} d\omega \; \omega^3 \, |h_{\mathbf{q}\lambda}|^2 \, |G(q_{\perp})|^2 \, \left( N_{\omega}^{T} - N_{\omega}^{T_e} \right) \; S(\omega, \mathbf{q}_{\parallel}),
\]

with \(c_{\hat{\mathbf{q}} \lambda}\) the phase velocity and \(N_{\omega}^{T/T_e}\) the Bose factors expressed as functions of frequency.

#### Phonon focusing factor \(\mathcal{A}_{\hat{\mathbf{q}} \lambda}\)  

\(\mathcal{A}_{\hat{\mathbf{q}} \lambda}\) accounts for the mapping between wave‑vector space and real‑space group‑velocity directions. It is computed from the anisotropic phonon dispersion as the **ratio of the solid‑angle element in \(\mathbf{q}\)-space to that in group‑velocity space**:

\[
\mathcal{A}_{\hat{\mathbf{q}} \lambda} = \frac{\Delta \Omega_{\mathbf{q}}}{\Delta \Omega_{\mathbf{v}}} = \left| \det\!\left( \frac{\partial \hat{\mathbf{v}}_{\mathbf{q}\lambda}}{\partial \hat{\mathbf{q}}} \right) \right|^{-1}.
\]

Equivalently, when working on a uniform grid of wave‑vector directions \(\{\hat{\mathbf{q}}_j\}\), you may:
1. Compute the group‑velocity direction \(\hat{\mathbf{v}}_j\) for each \(\hat{\mathbf{q}}_j\).
2. For a target direction \(\hat{\mathbf{r}}\), collect all \(\hat{\mathbf{q}}_j\) that map to \(\hat{\mathbf{r}}\) (within a small angular bin).  
3. The focusing weight of a bin is proportional to the number of \(\hat{\mathbf{q}}_j\) in that bin divided by the bin solid angle, normalized so that the integral of \(\mathcal{A}\) over all directions equals \(4\pi\).

---

### Detector geometry and projection  

The 2DEG is at the centre of the back side of a (001) GaAs substrate of thickness \(d = 0.4\,\text{mm}\). The detector is a \(100\times 10\,\mu\text{m}^2\) rectangle on the opposite (001) surface, centred directly opposite the \(120\times 50\,\mu\text{m}^2\) 2DEG mesa.

For a phonon leaving the 2DEG in direction \(\hat{\mathbf{r}} = (\sin\theta\cos\phi,\; \sin\theta\sin\phi,\; \cos\theta)\) (with the \(z\)-axis along [001]), the intersection point on the detector plane is  

\[
x_{\text{det}} = d\,\frac{r_x}{r_z} = d\,\tan\theta\cos\phi,\qquad
y_{\text{det}} = d\,\frac{r_y}{r_z} = d\,\tan\theta\sin\phi.
\]

A phonon is “detected” if \((x_{\text{det}},y_{\text{det}})\) lies inside the detector rectangle. The total LA or TA signal is the integral of \(P_{\hat{\mathbf{r}} \lambda}\) over the solid angle \(d\Omega = \sin\theta\,d\theta\,d\phi\) covered by the detector.

---

## Reproduction target  

Compute the LA/TA phonon emission ratio for the following five device structures on a (001) GaAs substrate, all at electron temperature \(T_e = 50\,\text{K}\):

- **Quantum wells** of widths 5.1, 6.8, 12, and 15 nm, with finite square confining potential of depth 350 meV.  
  Corresponding 2DEG densities: 1.8, 2.0, 3.7, and \(3.6 \times 10^{15}\,\text{m}^{-2}\).  
- **GaAs/AlGaAs heterostructure** with a conduction‑band offset of 225 meV and 2DEG density \(2.8 \times 10^{15}\,\text{m}^{-2}\).

Use \(\Xi_D = 9\,\text{eV}\) and \(h_{14} = 1.4 \times 10^9\,\text{eV}\,\text{m}^{-1}\). For each structure, compute the total LA and TA signals by integrating the directional emitted flux over the detector area, and take the ratio LA/TA.

## Output files  

Write all artifacts under `/app/outputs`:

- `/app/outputs/phonon_properties.npy`   (Step 1)
- `/app/outputs/form_factors.npz`        (Step 2)
- `/app/outputs/screening_data.npy`      (Step 3)
- `/app/outputs/la_ta_ratios.csv`        (Step 4, **scored**)

### la_ta_ratios.csv  

- **path**: `/app/outputs/la_ta_ratios.csv`  
- **format**: csv  
- **purpose**: scored  
- **target_policy**: reference_match  
- **description**: LA/TA phonon emission ratio for five device structures computed by the theoretical model. The hidden checker compares each ratio against the paper‑reported gold value with an appropriate tolerance and verifies the monotonic trend of decreasing ratio with increasing well width.  
- **schema**:  
  - required columns: `structure`, `well_width_nm`, `density_10_15_m2`, `la_ta_ratio`  
  - units: `la_ta_ratio` – dimensionless  
- **rows**: exactly five, one per structure. For the heterostructure, `well_width_nm` must be **empty**. Example row: `5.1nm,5.1,1.8,<ratio>`.

---

## Workflow steps  

### Step 1: Compute anisotropic phonon properties for GaAs  
- **Role**: process  
- **Action**: Using the GaAs elastic constants  

  \[
  C_{11}=11.88\times 10^{10}\,\text{Pa},\;
  C_{12}=5.38\times 10^{10}\,\text{Pa},\;
  C_{44}=5.94\times 10^{10}\,\text{Pa},
  \]

  solve the Christoffel equation for a dense grid of wave‑vector directions \(\hat{\mathbf{q}}\). Extract for each direction and each acoustic mode (LA, fast TA, slow TA): frequency \(\omega\), group velocity \(\mathbf{v}_g\), phase velocity \(c\), polarization vector \(\mathbf{e}\), and the focusing factor \(\mathcal{A}\).  
- **Evidence**: `/app/outputs/phonon_properties.npy`

### Step 2: Compute electron wavefunction form factors  
- **Role**: process  
- **Action**: For each structure solve the 1D effective‑mass Schrödinger equation along the confinement direction \(z\) to obtain the ground‑state wavefunction \(\phi(z)\). Evaluate \(G(q_\perp)\) and \(g(q_\parallel)\) on grids adequate for the subsequent integrals.  
- **Evidence**: `/app/outputs/form_factors.npz`

### Step 3: Compute RPA dynamical screening  
- **Role**: process  
- **Action**: For each structure and \(T_e = 50\,\text{K}\), compute the finite‑temperature polarizability \(\chi_{T_e}(\omega, q_\parallel)\) and the RPA screening function \(S(\omega, q_\parallel)\). Store the result on an \((\omega, q_\parallel)\) grid covering the range needed by Eq. 3.  
- **Evidence**: `/app/outputs/screening_data.npy`

### Step 4: Compute LA/TA phonon ratio for all structures and export CSV  
- **Role**: **scored** (load‑bearing)  
- **Action**: Assemble the model using the phonon properties (Step 1), form factors (Step 2), and screening data (Step 3). For each structure:  
  1. Evaluate \(P_{\hat{\mathbf{q}} \lambda}\) (Eq. 3) for a dense set of \(\hat{\mathbf{q}}\) directions.  
  2. Map each \(\hat{\mathbf{q}}\) to a laboratory direction \(\hat{\mathbf{r}}\) via its group velocity and apply the focusing factor.  
  3. Project the flux onto the (001) surface and integrate over the detector rectangle (\(100\times 10\,\mu\text{m}\)) opposite the \(120\times 50\,\mu\text{m}\) 2DEG, using the geometric mapping defined above.  
  4. Sum separately over LA modes and over the two TA modes to obtain the total LA and TA signals.  
  5. Compute the ratio LA/TA.  
- **Output file**: `/app/outputs/la_ta_ratios.csv`  
- **Contract**: Exactly five rows with the columns `structure,well_width_nm,density_10_15_m2,la_ta_ratio`. The column `well_width_nm` is empty for the heterostructure row.  
- **Scoring**: The hidden verifier compares your ratios against the theoretical reference values with a per‑structure tolerance of \(\max(0.1,\;0.25\times\text{gold})\) and checks the monotonic decreasing trend for quantum wells.  
- **Any attempt to copy numbers from outside sources without executing the workflow will be caught by the hidden check chain.**

---

## Assets  

- NumPy (`numpy`)  
- SciPy (`scipy`)  
- GaAs elastic constants \(C_{11}, C_{12}, C_{44}\) (hard‑code as above)  
- GaAs mass density \(\rho = 5320\,\text{kg}\,\text{m}^{-3}\)  
- GaAs background dielectric constant \(\epsilon = 12.9\)  
- Lattice temperature \(T = 4.2\,\text{K}\)  
- Effective mass \(m^* = 0.067\,m_e\)

---

## Self‑check before finishing (optional, not scored)  

A machine‑readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks **SHAPE ONLY** (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "la_ta_ratios.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "structure",
          "well_width_nm",
          "density_10_15_m2",
          "la_ta_ratio"
        ],
        "units": {
          "la_ta_ratio": "dimensionless"
        }
      },
      "description": "LA/TA phonon emission ratio for five device structures (QW 5.1, 6.8, 12, 15 nm and heterostructure) computed by the theoretical model. The hidden checker compares each ratio against the paper-reported gold value with an appropriate tolerance and verifies the monotonic trend of decreasing ratio with increasing well width."
    },
    {
      "file": "phonon_properties.npy",
      "format": "npy",
      "purpose": "intermediate",
      "target_policy": "reference_match",
      "schema": {},
      "description": "Precomputed anisotropic phonon properties for GaAs."
    },
    {
      "file": "form_factors.npz",
      "format": "npz",
      "purpose": "intermediate",
      "target_policy": "reference_match",
      "schema": {},
      "description": "Electron wavefunction form factors for five device structures."
    },
    {
      "file": "screening_data.npy",
      "format": "npy",
      "purpose": "intermediate",
      "target_policy": "reference_match",
      "schema": {},
      "description": "RPA dynamical screening data for each structure at T_e=50 K."
    }
  ],
  "notes": "Only the LA/TA ratio is scored; intermediate files are required for full workflow but are not directly scored. The checker will use a hidden tolerance and a structural check."
}
```