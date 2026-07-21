# Triboelectric Charge Transfer: Metal-Semiconductor Contact Model

## Problem background
When a metal asperity contacts an n-type semiconductor, charge transfer can arise from two distinct mechanisms: (1) formation of a Schottky depletion region that creates space charge in the semiconductor, and (2) flexoelectric polarization driven by strain gradients at the asperity contact. This task focuses on the contact between a rigid Pt₀.₈Ir₀.₂ spherical indenter (radius 60 nm) and a 0.7 wt% Nb‑doped SrTiO₃ half‑space under a 4 µN force. The goal is to compute the contributions of each mechanism and the resulting net charge transfer under two limiting assumptions about how flexoelectric bound charges are compensated.

## Approach
First, use Hertzian contact mechanics to obtain the contact radius and the strain/strain‑gradient fields inside the semiconductor. Second, apply two charge models:
**(a) Depletion charge** – a 1D model with a field‑dependent permittivity ansatz yields the depletion‑region space‑charge density and the total charge transferred to form the Schottky barrier.
**(b) Flexoelectric charge** – from the strain gradients and the three independent flexoelectric tensor coefficients, compute the polarization vector; then obtain the bound surface charge density ς = P·n̂ (n̂ outward normal) and integrate it over the contact region (ρ ≤ a) and the free surface (ρ > a) to obtain the interface charge ΔQ_if and the free‑surface charge ΔQ_sf. The induced metal charge ΔQ_m on the grounded sphere is obtained by the image‑charge approximation.
Finally, combine these charges for two limiting cases: **(b)** surface‑conduction regime: ΔQ_tot = ΔQ_d – ΔQ_if – ΔQ_sf; **(c–e)** no‑surface‑conduction regime: ΔQ_tot = ΔQ_d – ΔQ_if. All required material constants are provided below; no external data retrieval is needed.

## Mathematical definitions (from the paper)

### 1. Hertzian contact radius
For a rigid sphere (indenter) on an elastic half‑space, the contact radius is
```
a = (3 F R (1-ν²) / (4 E))^{1/3}
```
Parameters:
- R = 60 nm (sphere radius)
- F = 4 µN = 4×10⁻⁶ N (applied force)
- E = 270 GPa (Young’s modulus of Nb:SrTiO₃)
- ν = 0.24 (Poisson’s ratio)

### 2. Depletion charge (1D field‑dependent permittivity model)
Donor concentration N, vacuum permittivity ε₀, elementary charge e, and the parameters α, γ that describe the field‑dependence are:
```
ε₀ = 8.854187817×10⁻¹² F/m
e  = 1.602176634×10⁻¹⁹ C
N  = 2.24×10²⁶ m⁻³      (Nb dopant concentration)
α  = 0.04 V/nm           (field‑dependent permittivity parameter)
γ  = 14.8 V/nm
```
The built‑in potential across the depletion region is
```
V_d = Φ_b + ζ_F
Φ_b = 1.4 V     (Schottky barrier height)
ζ_F = 0.065 V   (Fermi level measured from the conduction band)
```
Define
```
β = e N / (ε₀ γ)            [dimension: 1/length]
δ = (β / α) V_d + 1
```
The depletion width is given by
```
W = (1/β) arcosh( (β/α) V_d + 1 )     (paper Eq. 1c)
```
The space‑charge density in the semiconductor yields a total transferred charge per unit area (contact area A = π a²) according to
```
|ΔQ_d|/A = ε₀ γ tanh(β W) = ε₀ γ √(δ²-1) / δ           (paper Eq. 2)
```
The sign convention is: ΔQ_d > 0 when electrons move from the n‑type semiconductor to the metal (i.e., the metal becomes positively charged). Therefore
```
ΔQ_d = + (ε₀ γ tanh(β W)) × A     [coulombs, then convert to elementary charges]
```
Calculate ΔQ_d in units of elementary charge e.

### 3. Flexoelectric polarization and bound charge
The indentation produces an axisymmetric elastic field. In cylindrical coordinates (ρ, φ, z) with z pointing into the semiconductor from the surface, the displacement field for a rigid sphere on a half‑space (Hertz solution) gives strain gradients. The three independent flexoelectric coefficients for cubic Nb:SrTiO₃ are:
```
μ₁₁₁₁ = -380 nC/m   (= μ_1111)
μ₁₁₂₂ = -103 nC/m   (= μ_1122)
μ₁₂₁₂ =  -1.4 nC/m  (= μ_1212)
```
The flexoelectric polarization vector P has the general form P_i = μ_ijkl ε_jk,l, where ε_jk,l = ∂ε_jk/∂x_l is the strain gradient. Under the axisymmetric Hertzian contact to an isotropic half‑space, the relevant non‑vanishing strain‑gradient components that produce a z‑component of polarization are those involving ∂ε_zz/∂ρ, ∂ε_ρz/∂z, etc. After evaluating the tensor contraction for the cubic crystal with the given coefficients, the vertical polarization at the surface is expressed as a function of ρ only.

**Surface bound charge density** on an interface with outward normal n̂ (pointing from the semiconductor into vacuum) is
```
σ_b = P · n̂
```
For the planar surface z=0, the outward normal is +ẑ, so σ_b(ρ) = P_z(ρ, z=0⁺) (i.e., evaluated just inside the semiconductor).

**Interface charge (contact region, ρ ≤ a):**  
```
ΔQ_if = ∫_{ρ=0}^{a} σ_b(ρ) 2πρ dρ      [coulombs]
```
**Free‑surface charge (outside contact, ρ > a):**
```
ΔQ_sf = ∫_{ρ=a}^{∞} σ_b(ρ) 2πρ dρ      [coulombs]
```
Note: the paper considers the bound charge on the free surface only over a finite region where the strain gradient is appreciable; however the integral can be taken to infinity because the strain gradient decays quickly. The gold values assume that the integral converges with an upper limit large enough (several contact radii) to capture the total charge.

**Induced metal charge (image‑charge approximation):**  
When the sphere is grounded, the bound charge on the free surface induces an image charge on the metal. To a first approximation,
```
ΔQ_m ≈ - ΔQ_sf      (because the free‑surface bound charge is compensated by the metal)
```
In the paper the actual value is ΔQ_m = −627 e (slightly smaller in magnitude than ΔQ_sf due to geometry). Use the image‑charge prescription: the induced charge on the sphere is given by solving the electrostatic problem of a point charge above a grounded conducting sphere. Because the charge distribution is spread over the free surface, the net induced charge is
```
ΔQ_m = - ∫_{ρ=a}^{∞} σ_b(ρ) g(ρ) 2πρ dρ
```
where g(ρ) is a geometric factor that accounts for the sphere’s finite radius. For the purpose of this computation you may use the approximation g(ρ) ≈ 1, which yields ΔQ_m ≈ −ΔQ_sf, and then apply a small correction based on the paper’s reported ratio (ΔQ_m/ΔQ_sf ≈ 0.968). However, a more accurate approach is to integrate the image‑charge factor for a grounded sphere:
```
g(ρ) = (R / √(R² + ρ²))   (image‑charge factor for a point charge on the plane interacting with a sphere)
```
Then ΔQ_m = - ∫ ρ σ_b(ρ) (R/√(R²+ρ²)) 2πρ dρ. Use this expression.

Convert all charges to natural numbers of elementary charge e.

### 4. Net charge transfer
```
Total in surface‑conduction regime (case b):   ΔQ_tot_b  = ΔQ_d − ΔQ_if − ΔQ_sf
Total in no‑surface‑conduction regime (c–e):  ΔQ_tot_c  = ΔQ_d − ΔQ_if
```
All in units of elementary charge.

## Reproduction target
Compute the following eight quantities and write them to a single JSON file `/app/outputs/computed_charges.json`:
- `depletion_charge_density_e_per_nm2` – depletion charge per unit area (e/nm²)
- `contact_radius_nm` – contact radius a (nm)
- `depletion_charge_total_e` – total depletion charge ΔQ_d (e)
- `flexoelectric_interface_charge_e` – ΔQ_if (e)
- `flexoelectric_surface_charge_e` – ΔQ_sf (e)
- `induced_metal_charge_e` – ΔQ_m (e)
- `total_charge_transfer_case_b_e` – ΔQ_tot for case b (e)
- `total_charge_transfer_case_cde_e` – ΔQ_tot for cases c–e (e)

All values are numeric (positive or negative). The file must contain exactly these keys (order does not matter).

The exact shape of this JSON file is specified in the output contract below.

## Assets
- Python 3
- NumPy
- SciPy

## Workflow steps

### Step 1: Compute contact radius, strain gradients, and charges (single scored block)
- **Action:**  
  1. Compute contact radius a using the Hertz formula above.  
  2. Compute the depletion width W (Eq. 1c), then the depletion charge density ΔQ_d/A (Eq. 2), and the total depletion charge ΔQ_d.  
  3. From the Hertzian displacement field, obtain the strain gradient components needed to evaluate P_z(ρ) at the surface. Use the flexoelectric coefficients to calculate σ_b(ρ) = P_z(ρ).  
  4. Numerically integrate σ_b(ρ) over the contact region (ρ ≤ a) to get ΔQ_if, and over the free surface (ρ > a up to a sufficiently large radius, e.g. 200 nm) to get ΔQ_sf.  
  5. Compute the induced metal charge using the image‑charge approximation with the sphere factor.  
  6. Assemble the net charge transfers for cases b and c–e.  
  7. Write the eight values into `/app/outputs/computed_charges.json` following the output contract.  
- **Evidence / output:** `/app/outputs/computed_charges.json`  
- **Scoring:** scored by hidden verifier

## Output files
All output artifacts must be placed under `/app/outputs`:
- `/app/outputs/computed_charges.json`

## Output contract

### computed_charges.json
- Path: `/app/outputs/computed_charges.json`
- Format: JSON object
- Required keys: `depletion_charge_density_e_per_nm2`, `contact_radius_nm`, `depletion_charge_total_e`, `flexoelectric_interface_charge_e`, `flexoelectric_surface_charge_e`, `induced_metal_charge_e`, `total_charge_transfer_case_b_e`, `total_charge_transfer_case_cde_e`
- Schema:
```json
{
  "type": "object",
  "required": [
    "depletion_charge_density_e_per_nm2",
    "contact_radius_nm",
    "depletion_charge_total_e",
    "flexoelectric_interface_charge_e",
    "flexoelectric_surface_charge_e",
    "induced_metal_charge_e",
    "total_charge_transfer_case_b_e",
    "total_charge_transfer_case_cde_e"
  ],
  "properties": {
    "depletion_charge_density_e_per_nm2": {"type": "number", "units": "e/nm^2"},
    "contact_radius_nm": {"type": "number", "units": "nm"},
    "depletion_charge_total_e": {"type": "number", "units": "e"},
    "flexoelectric_interface_charge_e": {"type": "number", "units": "e"},
    "flexoelectric_surface_charge_e": {"type": "number", "units": "e"},
    "induced_metal_charge_e": {"type": "number", "units": "e"},
    "total_charge_transfer_case_b_e": {"type": "number", "units": "e"},
    "total_charge_transfer_case_cde_e": {"type": "number", "units": "e"}
  }
}
```
Notes: All numeric values are in the units indicated. The contact radius is in nm. The charges are reported as multiples of the elementary charge e.

## How you are scored
A hidden verifier reads your `computed_charges.json`. It compares each numeric field against reference gold values (derived from the paper) using field‑specific tolerances, and checks internal consistency (e.g., the flexoelectric bound charges approximately balance the induced metal charge). Each field contributes a weight to the total score. Meeting the tolerance yields full credit; the reward degrades as the deviation grows. The final score is a weighted average across all fields, reported as a float between 0 and 1.