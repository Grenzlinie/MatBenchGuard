# Monte Carlo Auxeticity in Yukawa Crystals with Nanochannels

## Problem background
Auxetic materials exhibit a negative Poisson’s ratio (they expand laterally when stretched), which is valuable for sensors, composites, and other advanced applications. A promising strategy to enhance auxeticity is the introduction of nano-scale channels into a crystalline solid. This task reproduces a computational experiment in which Monte Carlo simulations are used to determine how the Poisson’s ratio of a face-centred cubic (fcc) crystal changes when narrow channels are introduced along the [001] crystallographic direction.  
You will simulate a system of particles interacting via a hard‑core repulsive Yukawa potential; the particles that occupy the channel positions are replaced by purely repulsive hard spheres (type‑A channels: a single chain of particles along [001]). By computing the elastic compliance tensor from strain fluctuations and then deriving the Poisson’s ratio for the [110] deformation direction with a transverse observation direction parameterised by an angle α, you will (i) verify that a simulation cell containing a single channel is representative of a larger crystal and (ii) quantify the concentration dependence of the Poisson’s ratio.

## Model and interactions
### Host particles
The host particles interact via the hard‑core repulsive Yukawa potential (HCRYP):
```
βu_ij =  ∞ ,                r_ij < σ
       = βε exp[-κσ(r_ij/σ-1)] / (r_ij/σ),   r_ij ≥ σ
```
where β = 1/(k_B T), κ is the inverse screening length, σ is the particle diameter, and ε sets the contact energy.

### Channel particles
Particles filling the channels interact via a pure hard‑sphere potential:
```
βu_ij = ∞ ,  r_ij < σ
       = 0 ,   r_ij ≥ σ
```

### Dimensionless parameters (all simulations)
- Inverse screening length: κσ = 10
- Inverse temperature: βε = 20
- Reduced pressure: P σ³ β = 100
- Cut‑off radius: r_c = 2.5 σ

### Crystal structure and channel definition
The perfect lattice is fcc. Channels of type **A** consist of a single chain of particles along the [001] direction; these particles are replaced by hard spheres.  
The concentration of channel particles is defined as
```
c = (N_ch / N) × 100%
```
where N_ch is the number of channel particles and N is the total number of particles in the simulation cell.

## Elastic properties: theory and formulas
The elastic properties are obtained via the Parrinello–Rahman Monte Carlo method in the isothermal‑isobaric (NpT) ensemble with a variable‑shape periodic box.

### Strain tensor
Let **h** be the symmetric box matrix at a given Monte Carlo step and **h₀** the reference box matrix (typically the time‑averaged box). The strain tensor is

```
ε = ½ ( h₀⁻¹ · h · h · h₀⁻¹  –  I )
```  
(where **I** is the 3×3 identity matrix). This is Eq. (6) of the original paper.

### Elastic compliance tensor
In the NpT ensemble the elastic compliance tensor S_{ijkl} is given by the fluctuations of the strain tensor:

```
S_{ijkl} = (V_p / (k_B T))  ⟨Δε_{ij} Δε_{kl}⟩
```  
where V_p is the equilibrium (mean) volume, k_B is Boltzmann’s constant, T is the temperature, and ⟨·⟩ denotes a canonical average over the production run (Eq. (7) of the paper).

### Poisson’s ratio for arbitrary crystallographic directions
If a uniaxial deformation is applied along the unit vector **n̂**, and the transverse response is measured along a unit vector **m̂** that is orthogonal to **n̂** ( **n̂**·**m̂** = 0), the Poisson’s ratio is

```
ν_nm = – ( m_i m_j S_{ijkl} n_k n_l ) / ( n_p n_r S_{prst} n_s n_t )
```  
(Eq. (8) of the paper).

### Specific direction: [110] deformation, transverse angle α
For the [110] direction:
- Deformation direction:  
  **n̂** = (1,1,0) / √2   (i.e. the [110] crystal axis).

- To define the transverse observation direction **m̂**(α), construct two orthonormal vectors that span the plane perpendicular to **n̂**:
  ```
  v̂ = (1,–1,0) / √2   (this is the [1–10] direction)
  û  = (0,0,1)         (the [001] direction)
  ```
- The angle α is measured *from* **v̂** (i.e. [1–10]) *toward* **û** (i.e. [001]), so
  ```
  m̂(α) = cos(α) v̂  +  sin(α) û
  ```
  When α = 0°, m̂ coincides with [1–10] (the standard transverse direction for this problem). α runs from 0° to 180°.

## Simulation protocol
### Initial configuration
- Build an fcc lattice. The conventional cubic cell of fcc has lattice constant a. An initial guess for a is not critical because the Parrinello–Rahman algorithm will adjust the box size and shape to satisfy the imposed pressure. A reasonable starting value is a ≈ 1.6 σ.
- Construct the following cells (type‑A channels, channel axis along z):
  * N = 500 particles, single channel, with concentrations c = 0% (perfect fcc), c = 5%, and c = 14%.
  * N = 2000 particles, four channels, c = 5%.
- Channel particles are tagged and interact only via the hard‑sphere potential; all other particles interact via the Yukawa potential.

### Monte Carlo parameters
- Ensemble: isothermal‑isobaric (NpT) with variable box shape (Parrinello–Rahman).
- Pressure: P σ³ β = 100
- Temperature is fixed by βε = 20 (β = 20/ε, but the reduced units are used directly).
- Periodic boundary conditions in all directions.
- Acceptance ratios for both particle and box moves should be kept around 30%.
- Equilibration: 10⁶ Monte Carlo cycles (one cycle = one attempted move per particle on average, plus box moves).
- Production: 10⁷ Monte Carlo cycles.
- Cut‑off for the Yukawa potential: 2.5 σ.

### Elastic analysis
During the production run, collect the instantaneous box matrix **h** at regular intervals (e.g. every cycle). Choose the equilibrium average ⟨**h**⟩ as the reference matrix **h₀**. Compute the strain tensor at each saved configuration using the formula above, then compute the mean values of the products of strain fluctuations to obtain the compliance tensor S_{ijkl}. Finally, use the formula for ν_nm with **n̂** = (1,1,0)/√2 and **m̂**(α) as defined to obtain the Poisson’s ratio as a function of α.

## Output files and contract
Write all artifacts under `/app/outputs`. Only the two CSV files listed below are scored.

### size_effect_curves.csv
- path: `/app/outputs/size_effect_curves.csv`
- format: csv
- schema:
  - `type`: table
  - `required_columns`: `system_size`, `angle_alpha`, `poisson_ratio`
  - `units`:
    - `angle_alpha`: degrees
    - `poisson_ratio`: dimensionless
- content:  
  For the fixed concentration c = 5%, compute the Poisson’s ratio ν for α from 0° to 180° in steps of 5° (or smaller) for the N=500 (single channel) and N=2000 (four channels) systems. Each row is a measurement for one system size at one angle.

### concentration_effect.csv
- path: `/app/outputs/concentration_effect.csv`
- format: csv
- schema:
  - `type`: table
  - `required_columns`: `concentration`, `poisson_ratio`
  - `units`:
    - `concentration`: percent
    - `poisson_ratio`: dimensionless
- content:  
  Using the N=500 (single channel) cell, report the Poisson’s ratio at α = 0° (i.e. transverse direction [1–10]) for three concentrations: c = 0%, c = 5%, and c = 14%. One row per concentration.

## How you are scored
Your submission will be evaluated by an automatic verifier that loads the two CSV files.

- **size_effect_curves.csv**: The verifier computes the maximum absolute difference between the ν(α) curve for N=500 and the curve for N=2000 over all angles. A small difference (below a hidden tolerance) earns full credit for this part.
- **concentration_effect.csv**: The verifier checks that the reported ν values follow a monotonically decreasing trend (becoming more negative as c increases) and that the numerical values are consistent with hidden reference ranges derived from the original study. Providing realistic simulation results (including typical stochastic noise) is expected; entering exact reference numbers without actually running the simulation will be detected by the internal consistency and spread checks.

## Self‑check before finishing (optional, not scored)
You can write a small script that verifies the output files exist, are well‑formed CSV, and contain the required column names. The checker will later perform numerical evaluation; this self‑check is purely for format validation.