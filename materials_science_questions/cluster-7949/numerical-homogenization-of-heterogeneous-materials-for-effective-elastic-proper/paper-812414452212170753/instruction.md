# Normalized in-plane force and moment resultants in SiC/Ti composites with large-diameter fibers

## Problem background
Metal matrix composites reinforced with large‑diameter fibres, such as SiC/Ti, are used in high‑temperature aerospace applications. Through‑thickness thermal gradients induce significant internal stresses, and accurate prediction of in‑plane force and moment resultants is important for structural design. Classical micromechanical approaches replace each ply with an equivalent homogeneous continuum that uses effective elastic and thermal properties, thereby decoupling the microstructural details from the global analysis. When only a few fibres span the thickness, however, the local microstructure can couple with the global response, potentially leading to inaccuracies in the classical predictions. This task reproduces the in‑plane force and moment resultants from a higher‑order micromechanical theory that explicitly couples the subcell‑level microstructure with the global thermal boundary‑value problem for a unidirectional SiC/Ti composite. The quantities to compute are the normalised in‑plane force and moment resultants as a function of the number of through‑thickness fibres, examined for fibre counts M = 2, 5, 10 and 20, and the through‑thickness normal stress profiles for the M = 10 configuration.

## Approach

### Geometry
For a configuration with **M** through‑thickness fibres, the total plate thickness is  
$$H = M\cdot D, \qquad D = 199\;\mu\text{m}$$  
each cell represents one row of fibres. Fibre volume fraction is fixed at  
$$v_f = 0.4$$  
The unit cell is taken as a cube of side *D* with a square fibre. Sub‑cell dimensions are  
$$d_1 = D\sqrt{v_f},\; d_2 = D-d_1,\; h_1 = d_1,\; h_2 = d_2,\; l_1 = d_1,\; l_2 = d_2$$  
All cells have the same constant **d₁, d₂, h₁, h₂, l₁, l₂** (uniform spacing).  
The cells are indexed *p = 1,…,M*; inside each cell the eight sub‑cells are labelled by  
(α,β,γ) with α,β,γ ∈ {1,2}.

### Material constants (use exactly)
- **SiC fibre** (sub‑cell (1,1,γ) – both γ):  
  *E* = 414 GPa,  ν = 0.3,  α = 4.9 × 10⁻⁶ /°C,  κ = 400 W/(m·°C)
- **Ti‑Al matrix** (all other sub‑cells):  
  *E* = 100 GPa,  ν = 0.3,  α = 9.6 × 10⁻⁶ /°C,  κ = 8 W/(m·°C)
- **Effective composite properties** (one ply, *v_f* = 0.4, for the continuum baseline):  
  Eₐ* = 226 GPa,  νₐ* = 0.30,  E_T* = 167 GPa,  Gₐ* = 60.9 GPa,  
  αₐ* = 6.15 × 10⁻⁶ /°C,  α_T* = 7.90 × 10⁻⁶ /°C,  κₐ* = 164.80 W/(m·°C),  κ_T* = 16.20 W/(m·°C)

---

### Thermal analysis (explicit‑coupling)

**Temperature expansion** in sub‑cell (αβγ) of cell *p* (local coordinates  
|\(\bar{x}_1\)| ≤ dα/2, etc.):  
$$
\begin{aligned}
T^{(\alpha\beta\gamma)} &= T_0^{(\alpha\beta\gamma)}
+ \bar{x}_1 T_1^{(\alpha\beta\gamma)}
+ \frac12\Bigl(3\bar{x}_1^2 - \frac{d_\alpha^2}{4}\Bigr) T_2^{(\alpha\beta\gamma)} \\
&\quad + \frac12\Bigl(3\bar{x}_2^2 - \frac{h_\beta^2}{4}\Bigr) T_3^{(\alpha\beta\gamma)}
+ \frac12\Bigl(3\bar{x}_3^2 - \frac{l_\gamma^2}{4}\Bigr) T_4^{(\alpha\beta\gamma)}.
\end{aligned}
$$  
Five unknowns per sub‑cell (**T₀,…,T₄**).

**Heat fluxes**  
\(q_i^{(\alpha\beta\gamma)} = -k_i^{(\alpha\beta\gamma)} \partial_i T^{(\alpha\beta\gamma)}\) (no sum on *i*).  
Define **flux moments** (averages weighted by powers of local coordinates):  
$$
Q_{i(l,m,n)}^{(\alpha\beta\gamma)} = 
\frac{1}{v_{(\alpha\beta\gamma)}} \int \bar{x}_1^{l}\bar{x}_2^{m}\bar{x}_3^{n}\, q_i\, dV,
\qquad v_{(\alpha\beta\gamma)} = d_\alpha h_\beta l_\gamma,\; l+m+n \le 2.
$$  
The only non‑zero flux moments in terms of the unknowns are  
$$
\begin{aligned}
Q_{1(0,0,0)} &= -k_1 T_1, \\
Q_{1(1,0,0)} &= -\frac14 k_1 d_\alpha^2 T_2, \\
Q_{2(0,1,0)} &= -\frac14 k_2 h_\beta^2 T_3, \\
Q_{3(0,0,1)} &= -\frac14 k_3 l_\gamma^2 T_4.
\end{aligned}
$$

**Governing equations** (for every interior cell *p*=2,…,M‑1):

- *Heat conduction* (satisfied in a volumetric sense, 8 equations):  
$$
\frac{Q_{1(1,0,0)}^{(\alpha\beta\gamma)}}{d_\alpha^{2}}
+ \frac{Q_{2(0,1,0)}^{(\alpha\beta\gamma)}}{h_\beta^{2}}
+ \frac{Q_{3(0,0,1)}^{(\alpha\beta\gamma)}}{l_\gamma^{2}} = 0
\qquad (\alpha,\beta,\gamma = 1,2).
$$

- *Heat flux continuity* in the **x₁** direction (between cells and sub‑cells):  
$$
\begin{aligned}
&12\frac{Q_{2(0,1,0)}^{(1\beta\gamma)}}{h_\beta^{2}}
+ 12\frac{Q_{3(0,0,1)}^{(1\beta\gamma)}}{l_\gamma^{2}}
+ 6\frac{d_2}{d_1}\Bigl[\frac{Q_{2(0,1,0)}^{(2\beta\gamma)}}{h_\beta^{2}}
+\frac{Q_{3(0,0,1)}^{(2\beta\gamma)}}{l_\gamma^{2}}\Bigr]^{(p)} \\
&+ 6\frac{d_2}{d_1}\Bigl[\frac{Q_{2(0,1,0)}^{(2\beta\gamma)}}{h_\beta^{2}}
+\frac{Q_{3(0,0,1)}^{(2\beta\gamma)}}{l_\gamma^{2}}\Bigr]^{(p-1)}
+ \frac{1}{d_1}\Bigl[\bigl.Q_{1(0,0,0)}^{(2\beta\gamma)}\bigr|^{(p)}
 - \bigl.Q_{1(0,0,0)}^{(2\beta\gamma)}\bigr|^{(p-1)}\Bigr] = 0, \\[4pt]
&\bigl.Q_{1(0,0,0)}^{(1\beta\gamma)}\bigr|^{(p)} =
\frac12\bigl.Q_{1(0,0,0)}^{(2\beta\gamma)}\bigr|^{(p)}
+\frac12\bigl.Q_{1(0,0,0)}^{(2\beta\gamma)}\bigr|^{(p-1)} \\
&+ 3d_2\Bigl[\frac{Q_{2(0,1,0)}^{(2\beta\gamma)}}{h_\beta^{2}}
+\frac{Q_{3(0,0,1)}^{(2\beta\gamma)}}{l_\gamma^{2}}\Bigr]^{(p)}
- 3d_2\Bigl[\frac{Q_{2(0,1,0)}^{(2\beta\gamma)}}{h_\beta^{2}}
+\frac{Q_{3(0,0,1)}^{(2\beta\gamma)}}{l_\gamma^{2}}\Bigr]^{(p-1)}.
\end{aligned}
$$  
  Flux continuity in **x₂** and **x₃** directions:  
$$
\frac{Q_{2(0,1,0)}^{(\alpha 1\gamma)}}{h_1}
+\frac{Q_{2(0,1,0)}^{(\alpha 2\gamma)}}{h_2} = 0,\qquad
\frac{Q_{3(0,0,1)}^{(\alpha\beta 1)}}{l_1}
+\frac{Q_{3(0,0,1)}^{(\alpha\beta 2)}}{l_2} = 0.
$$

- *Temperature continuity* (sub‑cell and cell interfaces):  
$$
\begin{aligned}
T_0^{(1\beta\gamma)}+d_1 T_1^{(1\beta\gamma)}+\frac14 d_1^2 T_2^{(1\beta\gamma)} &=
T_0^{(2\beta\gamma)}-d_2 T_1^{(2\beta\gamma)}+\frac14 d_2^2 T_2^{(2\beta\gamma)} \\
T_0^{(\alpha 1\gamma)}+\frac14 h_1^2 T_3^{(\alpha 1\gamma)} &=
T_0^{(\alpha 2\gamma)}+\frac14 h_2^2 T_3^{(\alpha 2\gamma)} \\
T_0^{(\alpha\beta 1)}+\frac14 l_1^2 T_4^{(\alpha\beta 1)} &=
T_0^{(\alpha\beta 2)}+\frac14 l_2^2 T_4^{(\alpha\beta 2)} \\
\bigl[T_0^{(1\beta\gamma)}-\frac{d_1}{2}T_1^{(1\beta\gamma)}+\frac14 d_1^2 T_2^{(1\beta\gamma)}\bigr]^{(p+1)} &=
\bigl[T_0^{(2\beta\gamma)}+\frac{d_2}{2}T_1^{(2\beta\gamma)}+\frac14 d_2^2 T_2^{(2\beta\gamma)}\bigr]^{(p)}.
\end{aligned}
$$

**Linear system** (after substituting the flux‑moment expressions)  
$$
\boldsymbol{\kappa}\,\mathbf{T} = \mathbf{t},
$$  
where **κ** is the structural thermal‑conductivity matrix of size 40M × 40M,  
**T** contains the 40M unknowns (T₀…T₄ for every sub‑cell), and **t** carries the  
boundary conditions:  
\(T_T = 0\,^\circ\mathrm{C}\) at \(x_1=0\) (top), \(T_B = 500\,^\circ\mathrm{C}\) at \(x_1=H\) (bottom).  
For the top cell (*p*=1) replace the inter‑cell flux relations with the interior sub‑cell  
flux continuity and the specified top temperature; similarly for the bottom cell (*p*=M).

---

### Mechanical analysis (explicit‑coupling)

**Displacement expansion** in sub‑cell (αβγ):  
$$
\begin{aligned}
u_1^{(\alpha\beta\gamma)} &= w_1 + \bar{x}_1\phi_1
+ \frac12\Bigl(3\bar{x}_1^2 - \frac14 d_\alpha^2\Bigr)U_1
+ \frac12\Bigl(3\bar{x}_2^2 - \frac14 h_\beta^2\Bigr)V_1
+ \frac12\Bigl(3\bar{x}_3^2 - \frac14 l_\gamma^2\Bigr)W_1, \\
u_2^{(\alpha\beta\gamma)} &= \bar{x}_2\,\chi_2, \\
u_3^{(\alpha\beta\gamma)} &= \bar{x}_3\,\psi_3,
\end{aligned}
$$  
Seven unknowns per sub‑cell: \(w_1,\phi_1,U_1,V_1,W_1,\chi_2,\psi_3\).

**Stresses** (orthotropic, eq. (31)):  
\(\sigma_{ij} = c_{ijkl}\varepsilon_{kl} - \Gamma_{ij}T\), with \(\varepsilon_{ij}\) from eq. (32).  
For isotropic phases the stiffnesses \(c_{ij}\) are computed from \(E,\nu\); for a material  
with given \(E,\nu\) one has  
$$
c_{11}=c_{22}=c_{33}=\lambda+2\mu,\;
c_{12}=c_{13}=c_{23}=\lambda,\;
c_{44}=c_{55}=c_{66}=\mu,\;
\lambda=\frac{E\nu}{(1+\nu)(1-2\nu)},\;
\mu=\frac{E}{2(1+\nu)}.
$$  
\(\Gamma_{ij}\) are the products of the stiffness tensor and the thermal expansion coefficients;  
for an isotropic material \(\Gamma_{11}=\Gamma_{22}=\Gamma_{33} = (3\lambda+2\mu)\alpha\).

**Stress moments** (averages similar to the thermal case, eq. (40)):  
$$
\begin{aligned}
S_{11(0,0,0)} &= c_{11}\phi_1 + c_{12}\chi_2 + c_{13}\psi_3 - \Gamma_1 T_0, \\
S_{22(0,0,0)} &= c_{12}\phi_1 + c_{22}\chi_2 + c_{23}\psi_3 - \Gamma_2 T_0, \\
S_{33(0,0,0)} &= c_{13}\phi_1 + c_{23}\chi_2 + c_{33}\psi_3 - \Gamma_3 T_0, \\
S_{11(1,0,0)} &= \frac14 c_{11}d_\alpha^2 U_1 - \frac{1}{12}d_\alpha^2 \Gamma_1 T_1, \\
S_{12(0,1,0)} &= \frac14 c_{44}h_\beta^2 V_1, \\
S_{13(0,0,1)} &= \frac14 c_{55}l_\gamma^2 W_1.
\end{aligned}
$$

**Equilibrium** (8 equations per cell, same form as thermal):  
$$
\frac{S_{11(1,0,0)}^{(\alpha\beta\gamma)}}{d_\alpha^{2}}
+ \frac{S_{12(0,1,0)}^{(\alpha\beta\gamma)}}{h_\beta^{2}}
+ \frac{S_{13(0,0,1)}^{(\alpha\beta\gamma)}}{l_\gamma^{2}} = 0.
$$

**Traction continuity** (x₁ direction, analogous to thermal, 24 relations):  
$$
\begin{aligned}
12\frac{S_{12(0,1,0)}^{(1\beta\gamma)}}{h_\beta^{2}}
+ 12\frac{S_{13(0,0,1)}^{(1\beta\gamma)}}{l_\gamma^{2}}
&+ 6\frac{d_2}{d_1}\Bigl[\frac{S_{12(0,1,0)}^{(2\beta\gamma)}}{h_\beta^{2}}
+\frac{S_{13(0,0,1)}^{(2\beta\gamma)}}{l_\gamma^{2}}\Bigr]^{(p)} \\
&+ 6\frac{d_2}{d_1}\Bigl[\frac{S_{12(0,1,0)}^{(2\beta\gamma)}}{h_\beta^{2}}
+\frac{S_{13(0,0,1)}^{(2\beta\gamma)}}{l_\gamma^{2}}\Bigr]^{(p-1)} \\
&+ \frac{1}{d_1}\Bigl[\bigl.S_{11(0,0,0)}^{(2\beta\gamma)}\bigr|^{(p)}
 - \bigl.S_{11(0,0,0)}^{(2\beta\gamma)}\bigr|^{(p-1)}\Bigr] = 0,
\end{aligned}
$$  
$$
\begin{aligned}
\bigl.S_{11(0,0,0)}^{(1\beta\gamma)}\bigr|^{(p)} &=
\frac12\bigl.S_{11(0,0,0)}^{(2\beta\gamma)}\bigr|^{(p)}
+\frac12\bigl.S_{11(0,0,0)}^{(2\beta\gamma)}\bigr|^{(p-1)} \\
&+ 3d_2\Bigl[\frac{S_{12(0,1,0)}^{(2\beta\gamma)}}{h_\beta^{2}}
+\frac{S_{13(0,0,1)}^{(2\beta\gamma)}}{l_\gamma^{2}}\Bigr]^{(p)}
- 3d_2\Bigl[\frac{S_{12(0,1,0)}^{(2\beta\gamma)}}{h_\beta^{2}}
+\frac{S_{13(0,0,1)}^{(2\beta\gamma)}}{l_\gamma^{2}}\Bigr]^{(p-1)}.
\end{aligned}
$$  
Traction continuity in **x₂, x₃**:  
$$
\frac{S_{12(0,1,0)}^{(\alpha 1\gamma)}}{h_1}
+\frac{S_{12(0,1,0)}^{(\alpha 2\gamma)}}{h_2}=0,\qquad
\frac{S_{13(0,0,1)}^{(\alpha\beta 1)}}{l_1}
+\frac{S_{13(0,0,1)}^{(\alpha\beta 2)}}{l_2}=0,
$$  
$$
S_{22(0,0,0)}^{(\alpha 1\gamma)} = S_{22(0,0,0)}^{(\alpha 2\gamma)},\qquad
S_{33(0,0,0)}^{(\alpha\beta 1)} = S_{33(0,0,0)}^{(\alpha\beta 2)}.
$$

**Displacement continuity** (24 relations):  
$$
\begin{aligned}
w_1^{(1\beta\gamma)}+\frac{d_1}{2}\phi_1^{(1\beta\gamma)}+\frac14 d_1^2 U_1^{(1\beta\gamma)} &=
w_1^{(2\beta\gamma)}-\frac{d_2}{2}\phi_1^{(2\beta\gamma)}+\frac14 d_2^2 U_1^{(2\beta\gamma)}, \\
w_1^{(\alpha 1\gamma)}+\frac14 h_1^2 V_1^{(\alpha 1\gamma)} &=
w_1^{(\alpha 2\gamma)}+\frac14 h_2^2 V_1^{(\alpha 2\gamma)}, \\
h_1\chi_2^{(\alpha 1\gamma)} &= -h_2\chi_2^{(\alpha 2\gamma)}, \\
w_1^{(\alpha\beta 1)}+\frac14 l_1^2 W_1^{(\alpha\beta 1)} &=
w_1^{(\alpha\beta 2)}+\frac14 l_2^2 W_1^{(\alpha\beta 2)}, \\
l_1\psi_3^{(\alpha\beta 1)} &= -l_2\psi_3^{(\alpha\beta 2)}, \\
\bigl[w_1^{(1\beta\gamma)}-\frac{d_1}{2}\phi_1^{(1\beta\gamma)}+\frac14 d_1^2 U_1^{(1\beta\gamma)}\bigr]^{(p+1)} &=
\bigl[w_1^{(2\beta\gamma)}+\frac{d_2}{2}\phi_1^{(2\beta\gamma)}+\frac14 d_2^2 U_1^{(2\beta\gamma)}\bigr]^{(p)}.
\end{aligned}
$$

**Linear system**  
$$
\mathbf{K}\,\mathbf{U} = \mathbf{f},
$$  
**K** (56M × 56M) contains geometry and stiffness data; **f** includes the contributions  
from the temperature field (T₀…T₄) and the boundary conditions.  
Boundary conditions: top surface \(x_1=0\) is stress‑free (\(\sigma_{11}=0\)),  
bottom surface \(x_1=H\) is rigidly clamped (\(u_1=0\)).  
As in the thermal problem, the boundary cells *p*=1 and *p*=M use modified equations  
(replacing inter‑cell traction/displacement with surface conditions).

---

### Continuum baseline (classical lamination theory)
For each **M** the laminate has total thickness \(H=M\!\times\!199\;\mu\text{m}\) and consists  
of *M* identical plies with effective properties from Table 2. The linear temperature  
distribution is  
$$
T(z) = T_T + \frac{T_B-T_T}{H}\Bigl(z+\frac{H}{2}\Bigr),
\qquad -H/2 \le z \le H/2,
$$  
with \(T_T=0\,^\circ\mathrm{C}\), \(T_B=500\,^\circ\mathrm{C}\). Because mid‑plane strains  
and curvatures are zero (bottom clamped, top stress‑free) the thermal force and moment  
resultants are  
$$
\mathbf{N}^T = \int_{-H/2}^{H/2} \overline{\mathbf{Q}}\,\boldsymbol{\alpha}_{xy}\,T(z)\,dz,\qquad
\mathbf{M}^T = \int_{-H/2}^{H/2} \overline{\mathbf{Q}}\,\boldsymbol{\alpha}_{xy}\,T(z)\,z\,dz.
$$  
For the unidirectional (0°) laminate, the transformed reduced stiffness \(\overline{\mathbf{Q}}\)  
and the thermal expansion vector \(\boldsymbol{\alpha}_{xy}\) are obtained from the effective  
axial/transverse moduli (see constants above). The actual in‑plane force and moment  
resultants required to keep the laminate flat are \(\mathbf{N}^{\text{cont}} = -\mathbf{N}^T\),  
\(\mathbf{M}^{\text{cont}} = -\mathbf{M}^T\).  
Explicitly, for each *p*ly,  
$$
\begin{aligned}
\mathbf{N}^T &= \sum_{i=1}^{M} \overline{\mathbf{Q}}^{(i)}\boldsymbol{\alpha}_{xy}^{(i)}
\Bigl[T_i(h_i-h_{i-1}) + \frac12\frac{\Delta T_i}{t_i}(h_i^2-h_{i-1}^2)
-\frac{\Delta T_i}{t_i}h_{i-1}(h_i-h_{i-1})\Bigr], \\
\mathbf{M}^T &= \sum_{i=1}^{M} \overline{\mathbf{Q}}^{(i)}\boldsymbol{\alpha}_{xy}^{(i)}
\Bigl[\frac12 T_i(h_i^2-h_{i-1}^2) + \frac13\frac{\Delta T_i}{t_i}(h_i^3-h_{i-1}^3)
-\frac12\frac{\Delta T_i}{t_i}h_{i-1}(h_i^2-h_{i-1}^2)\Bigr],
\end{aligned}
$$  
where \(t_i = D\), \(h_{i-1} = -H/2 + (i-1)D\), \(h_i = h_{i-1}+D\), \(T_1 = T_T\),  
\(\Delta T_i = \frac{t_i}{\kappa_i}\frac{T_B-T_T}{\sum_j t_j/\kappa_j}\), and \(\kappa_i = \kappa_T^*\).  
These closed‑form expressions give \(N_2^{\text{cont}}, N_3^{\text{cont}}, M_2^{\text{cont}}, M_3^{\text{cont}}\).

---

### Resultants and normalization
From the explicit‑coupling solution the average stresses \(S_{22(0,0,0)}\) and \(S_{33(0,0,0)}\)  
in each sub‑cell give the force per unit width:  
$$
N_2 = \frac{1}{(h_1+h_2)(l_1+l_2)}
\sum_{p=1}^{M}\sum_{\alpha,\beta,\gamma}
S_{22(0,0,0)}^{(\alpha\beta\gamma)}\,d_\alpha h_\beta l_\gamma,
$$  
and similarly for \(N_3\). The moment resultants, taken about the mid‑plane \(x_1 = H/2\), are  
$$
M_2 = \frac{1}{(h_1+h_2)(l_1+l_2)}
\sum_{p=1}^{M}\sum_{\alpha,\beta,\gamma}
\int_{\text{subcell}} \sigma_{22}^{(\alpha\beta\gamma)}\,(x_1 - H/2)\,dx_1 dx_2 dx_3,
$$  
which can be evaluated using the sub‑cell stress expansions (the integral separates into  
a term involving \(S_{22(0,0,0)}\) times the sub‑cell centroid offset and terms coming  
from the temperature moments \(T_1\)).  
The **normalised** resultants are  
$$
N_2^{\text{norm}} = N_2 / N_2^{\text{cont}},\quad
N_3^{\text{norm}} = N_3 / N_3^{\text{cont}},\quad
M_2^{\text{norm}} = M_2 / M_2^{\text{cont}},\quad
M_3^{\text{norm}} = M_3 / M_3^{\text{cont}}.
$$
These 16 values are the primary scored output.

---

### Reproduction pipeline
1. Define geometry & constants for each M (2,5,10,20).  
2. Compute continuum‑baseline resultants (above formulas).  
3. Assemble and solve the thermal system \(\boldsymbol{\kappa}\mathbf{T}=\mathbf{t}\).  
4. Assemble and solve the mechanical system \(\mathbf{K}\mathbf{U}=\mathbf{f}\).  
5. Integrate stresses → N₂,N₃,M₂,M₃ → normalise → `normalized_resultants.csv`.  
6. For M=10 export per‑subcell \(\sigma_{22},\sigma_{33}\) and \(x_1\)-center → `stress_profiles_M10.csv`.

## Reproduction target
Produce the following two CSV files in the output directory:
- `normalized_resultants.csv` with columns M (integer), N2_norm (float, dimensionless), N3_norm (float, dimensionless), M2_norm (float, dimensionless), M3_norm (float, dimensionless). One row for each M value in ascending order: 2, 5, 10, 20. The values are the explicit‑coupling force and moment resultants normalised by the continuum baseline.
- `stress_profiles_M10.csv` with columns cell_index (int, 1 … 10), alpha (int, 1 or 2), beta (int, 1 or 2), gamma (int, 1 or 2), x1_center (float, µm), sigma22 (float, MPa), sigma33 (float, MPa). One row per subcell, giving exactly 80 rows. The continuum baseline resultants are computed during the pipeline; only the normalised resultants and the M = 10 stress profiles are scored.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Define geometry and material constants
- Role: process
- Action: For each M in {2, 5, 10, 20}, compute the cell dimensions using constant cell thickness D = 199 µm and fiber volume fraction vf = 0.4, yielding subcell sizes d1, d2, h1, h2, l1, l2. Store the material properties (E, ν, α, κ for fiber and matrix) and the effective composite properties (E_A*, ν_A*, E_T*, G_A*, α_A*, α_T*, κ_A*, κ_T*) as given constants.
- Evidence: none

### Step 2: Compute continuum baseline resultants
- Role: process
- Action: Using the effective properties and classical lamination theory (linear temperature profile through a homogeneous laminate, zero mid-plane strains/curvatures, bottom clamped, top stress-free), compute the in-plane force N2_cont, N3_cont and moment M2_cont, M3_cont for each value of M. Write the baseline resultants to a CSV file as evidence.
- Evidence: `/app/outputs/continuum_resultants.csv`

### Step 3: Explicit-coupling thermal analysis
- Role: process
- Action: For each M, assemble the global thermal conductivity matrix κ from the subcell conductivities and dimensions, and solve κ T = t to obtain the temperature expansion coefficients (T0, T1, T2, T3, T4) in every subcell. Store the solution as evidence.
- Evidence: `/app/outputs/thermal_solution.npz`

### Step 4: Explicit-coupling mechanical analysis
- Role: process
- Action: For each M, use the temperature field from step s3 to assemble the structural stiffness matrix K and force vector f. Solve K U = f to obtain the displacement coefficients, then compute the stress components σ22 and σ33 in each subcell. Save the full stress data as evidence.
- Evidence: `/app/outputs/stress_output.npz`

### Step 5: Compute normalized force and moment resultants
- Role: scored (load-bearing)
- Action: For each M, integrate the subcell normal stresses σ22 and σ33 over the thickness to obtain the in-plane force resultants N2, N3 and moment resultants M2, M3. Divide each by the corresponding continuum baseline value from step s2 to produce normalized resultants. Output the normalized values to a CSV file.
- Output file: `/app/outputs/normalized_resultants.csv`
- Format: csv
- Contract: M: integer, N2_norm: float, N3_norm: float, M2_norm: float, M3_norm: float; one row per M in ascending order (2, 5, 10, 20)
- Scoring: scored by hidden verifier

### Step 6: Export stress profiles for M = 10
- Role: scored
- Action: For the configuration with M = 10, iterate over all subcells (cell p=1..10, indices α,β,γ=1,2), compute the x1 coordinate of the subcell centre, and extract σ22 and σ33. Write the data to a CSV file with one row per subcell (80 rows).
- Output file: `/app/outputs/stress_profiles_M10.csv`
- Format: csv
- Contract: cell_index: int (1..10), alpha: int (1 or 2), beta: int (1 or 2), gamma: int (1 or 2), x1_center: float (µm), sigma22: float (MPa), sigma33: float (MPa); one row per subcell, 80 rows total
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/normalized_resultants.csv`
- `/app/outputs/stress_profiles_M10.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### normalized_resultants.csv
- path: `/app/outputs/normalized_resultants.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Normalized in-plane force and moment resultants for M=2,5,10,20. Columns: M (int), N2_norm, N3_norm, M2_norm, M3_norm (float).
- schema:
  - `columns`:
    - `name`: M
    - `type`: int
    - `name`: N2_norm
    - `type`: float
    - `name`: N3_norm
    - `type`: float
    - `name`: M2_norm
    - `type`: float
    - `name`: M3_norm
    - `type`: float

### stress_profiles_M10.csv
- path: `/app/outputs/stress_profiles_M10.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Through-thickness normal stress profiles at subcell centers for M=10. Columns: cell_index, alpha, beta, gamma, x1_center (µm), sigma22 (Pa), sigma33 (Pa).
- schema:
  - `columns`:
    - `name`: cell_index
    - `type`: int
    - `name`: alpha
    - `type`: int
    - `name`: beta
    - `type`: int
    - `name`: gamma
    - `type`: int
    - `name`: x1_center
    - `type`: float
    - `name`: sigma22
    - `type`: float
    - `name`: sigma33
    - `type`: float

Notes: Verifier will compare against reference numeric values with relative tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "normalized_resultants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "columns": [
          {
            "name": "M",
            "type": "int"
          },
          {
            "name": "N2_norm",
            "type": "float"
          },
          {
            "name": "N3_norm",
            "type": "float"
          },
          {
            "name": "M2_norm",
            "type": "float"
          },
          {
            "name": "M3_norm",
            "type": "float"
          }
        ]
      },
      "description": "Normalized in-plane force and moment resultants for M=2,5,10,20. Columns: M (int), N2_norm, N3_norm, M2_norm, M3_norm (float)."
    },
    {
      "file": "stress_profiles_M10.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "columns": [
          {
            "name": "cell_index",
            "type": "int"
          },
          {
            "name": "alpha",
            "type": "int"
          },
          {
            "name": "beta",
            "type": "int"
          },
          {
            "name": "gamma",
            "type": "int"
          },
          {
            "name": "x1_center",
            "type": "float"
          },
          {
            "name": "sigma22",
            "type": "float"
          },
          {
            "name": "sigma33",
            "type": "float"
          }
        ]
      },
      "description": "Through-thickness normal stress profiles at subcell centers for M=10. Columns: cell_index, alpha, beta, gamma, x1_center (µm), sigma22 (Pa), sigma33 (Pa)."
    }
  ],
  "notes": "Verifier will compare against reference numeric values with relative tolerance."
}
```

## How you are scored
A hidden verifier independently evaluates the submitted artifacts. For `normalized_resultants.csv`, each of the 16 normalised values (4 M values × 4 resultants) is compared against a hidden reference value using an absolute error tolerance; each value carries equal weight. For `stress_profiles_M10.csv`, the verifier checks that the file contains the correct column names and exactly 80 rows. The final score is a weighted combination of these checks. Reporting the paper’s numbers is not sufficient; your output must pass the verifier’s automated inspection.
