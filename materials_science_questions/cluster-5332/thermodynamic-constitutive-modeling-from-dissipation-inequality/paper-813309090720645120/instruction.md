# Coupled Thermomechanical Simulation of Austenite Single Crystals under Uniaxial Tension

## Problem background
TRIP (Transformation‑Induced Plasticity) steels contain metastable austenite that transforms to martensite under mechanical loading. This transformation releases latent heat, which raises the local temperature and creates a fully coupled thermomechanical problem: the temperature change alters the transformation rate and plastic deformation, while the inelastic processes themselves generate additional heat. Understanding these coupled mechanisms for a single crystal of austenite under uniaxial tension is essential for predicting the material’s macroscopic behaviour. This task reproduces the simulated thermomechanical response curves (stress, temperature, martensite volume fraction, and plastic microstrain) for single‑crystal cases under different crystal orientations, initial temperatures, and thermal boundary conditions.

## Model formulation and implementation approach

### Kinematics
The total deformation gradient \(\mathbf{F}\) is decomposed multiplicatively:
\[
\mathbf{F} = \mathbf{F}_{\mathrm{e}} \mathbf{F}_{\mathrm{th}} \mathbf{F}_{\mathrm{p}} \mathbf{F}_{\mathrm{tr}},
\]
with elastic (\(\mathbf{F}_{\mathrm{e}}\)), thermal (\(\mathbf{F}_{\mathrm{th}}\)), plastic (\(\mathbf{F}_{\mathrm{p}}\)), and transformation (\(\mathbf{F}_{\mathrm{tr}}\)) parts.

**Transformation deformation gradient:**  
There are \(M=24\) martensitic transformation systems. For each system \(\alpha\), the unconstrained transformation deformation gradient is \(\mathbf{F}^{(\alpha)} = \mathbf{b}^{(\alpha)} \otimes \mathbf{d}^{(\alpha)}\), where \(\mathbf{b}^{(\alpha)}\) is the shape strain vector and \(\mathbf{d}^{(\alpha)}\) the habit plane normal. The effective rate is
\[
\dot{\mathbf{F}}_{\mathrm{tr}} = \sum_{\alpha=1}^{M} \dot{\xi}^{(\alpha)} \mathbf{b}^{(\alpha)} \otimes \mathbf{d}^{(\alpha)},
\]
with \(\xi^{(\alpha)}\) the volume fraction of system \(\alpha\). The volume change per system is \(\delta_{\mathrm{T}} = \mathbf{b}^{(\alpha)}\cdot\mathbf{d}^{(\alpha)}\) (constant).

**Plastic deformation gradient:**  
Plastic deformation is described by the effective plastic velocity gradient
\[
\mathbf{L}_{\mathrm{p}} = \dot{\mathbf{F}}_{\mathrm{p}}\mathbf{F}_{\mathrm{p}}^{-1} = \sum_{i=1}^{N} \dot{\gamma}^{(i)} \mathbf{m}_{\mathrm{A}}^{(i)} \otimes \mathbf{n}_{\mathrm{A}}^{(i)},
\]
with \(N=24\) slip systems in the FCC austenite. \(\mathbf{m}_{\mathrm{A}}^{(i)}\) and \(\mathbf{n}_{\mathrm{A}}^{(i)}\) are the slip direction and slip plane normal, and \(\dot{\gamma}^{(i)}\) the effective plastic slip rate. Plastic deformation is assumed isochoric (\(\det\mathbf{F}_{\mathrm{p}} = 1\)).

**Thermal deformation gradient:**  
\[
\mathbf{F}_{\mathrm{th}}(\theta,\boldsymbol{\xi}) = \mathbf{I} + \mathbf{A}(\boldsymbol{\xi})(\theta - \theta_0),
\]
where \(\theta\) is the absolute temperature and \(\theta_0\) the reference temperature (initial temperature). The effective thermal expansion tensor \(\mathbf{A}(\boldsymbol{\xi}) = (1/J_{\mathrm{tr}})\big[ \xi_{\mathrm{A}} \alpha_{\mathrm{A}} + (1+\delta_{\mathrm{T}}) \sum_{\alpha} \xi^{(\alpha)} \alpha^{(\alpha)} \big] \mathbf{I}\), with isotropic expansion coefficients \(\alpha_{\mathrm{A}}=\alpha^{(\alpha)}=2.1\times10^{-5}\ \mathrm{K}^{-1}\).

### Constitutive relations for stress and internal energy
The second Piola-Kirchhoff stress in the third intermediate configuration is
\[
\mathbf{S} = \mathbb{C}(\boldsymbol{\xi}) \mathbf{E}_{\mathrm{e}}, \quad \mathbf{E}_{\mathrm{e}} = \tfrac12 (\mathbf{F}_{\mathrm{e}}^{\mathrm{T}}\mathbf{F}_{\mathrm{e}} - \mathbf{I}).
\]
The effective stiffness \(\mathbb{C}\) is a volume average:
\[
\mathbb{C}(\boldsymbol{\xi}) = \frac{1}{J_{\mathrm{tr}} J_{\mathrm{th}}} \left( J_{\mathrm{th,A}} \xi_{\mathrm{A}} \mathbb{C}_{\mathrm{A}} + (1+\delta_{\mathrm{T}}) \sum_{\alpha=1}^{M} J_{\mathrm{th}}^{(\alpha)} \xi^{(\alpha)} \mathbb{C}^{(\alpha)} \right).
\]
Here \(\mathbb{C}_{\mathrm{A}}\) is the cubic stiffness of austenite (three constants: \(C_{11}^A = \kappa_1^A\), \(C_{12}^A = \kappa_2^A\), \(C_{44}^A = \kappa_3^A\)) and \(\mathbb{C}^{(\alpha)}\) is the tetragonal stiffness of martensite (six constants: \(C_{11}^M = C_{22}^M = \kappa_1^M\), \(C_{12}^M = \kappa_2^M\), \(C_{13}^M = C_{23}^M = \kappa_3^M\), \(C_{33}^M = \kappa_4^M\), \(C_{44}^M = C_{55}^M = \kappa_5^M\), \(C_{66}^M = \kappa_6^M\)). All other components are zero. Specific values are given in Table 1.

The specific internal energy (per unit mass) is
\[
\epsilon = \epsilon_{\mathrm{m}} + \theta \eta_{\mathrm{m}} + \epsilon_{\mathrm{th}}^* + \epsilon_{\mathrm{s}} + \epsilon_{\mathrm{d}},
\]
with
\[
\begin{aligned}
\epsilon_{\mathrm{m}} &= \frac{J_{\mathrm{tr}} J_{\mathrm{th}}}{2\rho_0} \mathbb{C}(\boldsymbol{\xi}) \mathbf{E}_{\mathrm{e}}\!:\!\mathbf{E}_{\mathrm{e}},\\
\eta_{\mathrm{m}} &= \frac{1}{\rho_0} J_{\mathrm{tr}} J_{\mathrm{th}} (\mathbf{F}_{\mathrm{e}}^{\mathrm{T}}\mathbf{F}_{\mathrm{e}}\mathbf{S})\mathbf{F}_{\mathrm{th}}^{-\mathrm{T}}\!:\!\mathbf{A},\\
\epsilon_{\mathrm{th}}^* &= h(\boldsymbol{\xi}) (\theta-\theta_{\mathrm{T}}) + \sum_{\alpha=1}^{M} \lambda_{\mathrm{T}}^{(\alpha)} \xi^{(\alpha)},\\
\epsilon_{\mathrm{s}} &= \frac{\chi}{l_0 \rho_0} \sum_{\alpha=1}^{M} \xi^{(\alpha)}(1-\xi^{(\alpha)}),\\
\epsilon_{\mathrm{d}} &= \frac{1}{2\rho_0} J_{\mathrm{tr}} J_{\mathrm{th}} \omega_{\mathrm{A}} \mu(\boldsymbol{\xi}) \beta^2,
\end{aligned}
\]
where \(\rho_0\) is the reference density (use \(\rho_0 = 7800\ \mathrm{kg/m^3}\)), \(h(\boldsymbol{\xi}) = \xi_{\mathrm{A}} h_{\mathrm{A}} + \sum \xi^{(\alpha)} h^{(\alpha)}\) is the effective specific heat, \(\lambda_{\mathrm{T}}^{(\alpha)}\) the latent heat per unit mass, \(\theta_{\mathrm{T}}=633\ \mathrm{K}\) the transformation temperature, \(\chi=0.2\ \mathrm{J/m^2}\), \(l_0=0.05\ \mu\mathrm{m}\), \(\omega_{\mathrm{A}}=10\), and \(\mu(\boldsymbol{\xi})\) is the effective shear modulus analogous to (45). The plastic microstrain \(\beta\) is defined by \(\dot{\beta} = \sum_i w^{(i)} \dot{\gamma}^{(i)}\) with weighting functions \(w^{(i)}\) from (64). The temperature is obtained by solving the energy balance (66) using the above internal energy.

### Driving forces and kinetic relations
The transformation driving force for system \(\alpha\) is
\[
\begin{aligned}
f^{(\alpha)} &= f_{\mathrm{m}}^{(\alpha)} + f_{\mathrm{m,th}}^{(\alpha)} + f_{\mathrm{th}}^{(\alpha)} + f_{\mathrm{d}}^{(\alpha)} + f_{\mathrm{s}}^{(\alpha)},\\
f_{\mathrm{m}}^{(\alpha)} &= J_{\mathrm{tr}} J_{\mathrm{th}} (\mathbf{F}_{\mathrm{p}}^{\mathrm{T}}\mathbf{F}_{\mathrm{th}}^{\mathrm{T}}\mathbf{F}_{\mathrm{e}}^{\mathrm{T}}\mathbf{F}_{\mathrm{e}}\mathbf{S}\mathbf{F}_{\mathrm{th}}^{-\mathrm{T}}\mathbf{F}_{\mathrm{p}}^{-\mathrm{T}}\mathbf{F}_{\mathrm{tr}}^{-\mathrm{T}})\!:\!(\mathbf{b}^{(\alpha)}\otimes\mathbf{d}^{(\alpha)}) \\
&\quad + \tfrac12 ( J_{\mathrm{th,A}} \mathbb{C}_{\mathrm{A}} - (1+\delta_{\mathrm{T}})J_{\mathrm{th}}^{(\alpha)}\mathbb{C}^{(\alpha)} ) \mathbf{E}_{\mathrm{e}}\!:\!\mathbf{E}_{\mathrm{e}},\\
f_{\mathrm{m,th}}^{(\alpha)} &= J_{\mathrm{th}} (\mathbf{F}_{\mathrm{e}}^{\mathrm{T}}\mathbf{F}_{\mathrm{e}}\mathbf{S}\mathbf{F}_{\mathrm{th}}^{-\mathrm{T}})\!:\!\big( (1+\delta_{\mathrm{T}})\mathbf{A}^{(\alpha)} - \mathbf{A}_{\mathrm{A}} \big) (\theta-\theta_0),\\
f_{\mathrm{th}}^{(\alpha)} &= \rho_0 \frac{\lambda_{\mathrm{T}}^{(\alpha)}}{\theta_{\mathrm{T}}} (\theta-\theta_{\mathrm{T}}) + \rho_0 (h_{\mathrm{A}}-h^{(\alpha)}) \big( \theta-\theta_{\mathrm{T}} - \theta \ln(\theta/\theta_{\mathrm{T}}) \big),\\
f_{\mathrm{d}}^{(\alpha)} &= \tfrac12 \omega_{\mathrm{A}} \big( J_{\mathrm{th,A}} \mu_{\mathrm{A}} - (1+\delta_{\mathrm{T}}) J_{\mathrm{th}}^{(\alpha)} \mu^{(\alpha)} \big) \beta^2,\\
f_{\mathrm{s}}^{(\alpha)} &= \frac{\chi}{l_0} (2\xi^{(\alpha)}-1).
\end{aligned}
\]
Remaining terms follow the paper's notation; \(\mu_{\mathrm{A}}=67.5\ \mathrm{GPa}\), \(\mu^{(\alpha)}=98.4\ \mathrm{GPa}\).
The kinetic relation is
\[
\dot{\xi}^{(\alpha)} = 
\begin{cases}
\dot{\xi}_0 \tanh\!\big( \frac{f^{(\alpha)} - f_{\mathrm{cr}}^{(\alpha)}}{\nu f_{\mathrm{cr}}^{(\alpha)}} \big), & f^{(\alpha)} \ge f_{\mathrm{cr}}^{(\alpha)},\\
0, & \text{otherwise},
\end{cases}
\]
with \(\dot{\xi}_0 = 0.003\ \mathrm{s^{-1}}\), \(\nu = 0.17\), \(f_{\mathrm{cr}}^{(\alpha)} = 306\ \mathrm{MPa}\).

The plastic driving force on slip system \(i\) is
\[
g^{(i)} = J_{\mathrm{th}} (\mathbf{F}_{\mathrm{th}}^{\mathrm{T}}\mathbf{F}_{\mathrm{e}}^{\mathrm{T}}\mathbf{F}_{\mathrm{e}}\mathbf{S}\mathbf{F}_{\mathrm{th}}^{-\mathrm{T}})\!:\!(\mathbf{m}_{\mathrm{A}}^{(i)}\otimes\mathbf{n}_{\mathrm{A}}^{(i)}) + \rho_0 \theta \phi_{\mathrm{A}}^{(i)} - \omega_{\mathrm{A}} \mu(\boldsymbol{\xi}) \beta w^{(i)},
\]
with \(\phi_{\mathrm{A}}^{(i)} = 5.13\ \mathrm{J\,kg^{-1}\,K^{-1}}\). The plastic slip rate in the austenite is
\[
\dot{\gamma}_{\mathrm{A}}^{(i)} = 
\begin{cases}
\dot{\gamma}_{0}^{\mathrm{A}} \Big( \big( g^{(i)} / s_{\mathrm{A}}^{(i)} \big)^{1/n_{\mathrm{A}}} - 1 \Big), & g^{(i)} \ge s_{\mathrm{A}}^{(i)},\\
0, & \text{otherwise},
\end{cases}
\]
with \(\dot{\gamma}_{0}^{\mathrm{A}} = 0.001\ \mathrm{s^{-1}}\), \(n_{\mathrm{A}} = 0.02\). The slip resistance evolves as
\[
\dot{s}_{\mathrm{A}}^{(i)} = \sum_j H_{\mathrm{A}}^{(i,j)} \dot{\gamma}_{\mathrm{A}}^{(j)}, \quad H_{\mathrm{A}}^{(i,j)} = \big( (1-q_{\mathrm{A}})\delta_{ij} + q_{\mathrm{A}} \big) k_{\mathrm{A}}^{(j)},
\]
\[
k_{\mathrm{A}}^{(j)} = k_0^{\mathrm{A}} \Big( 1 - s_{\mathrm{A}}^{(j)}/s_\infty^{\mathrm{A}} \Big)^{u_{\mathrm{A}}},
\]
with \(s_{\mathrm{A},0}=189\ \mathrm{MPa}\), \(s_\infty^{\mathrm{A}}=579\ \mathrm{MPa}\), \(k_0^{\mathrm{A}}=3\ \mathrm{GPa}\), \(u_{\mathrm{A}}=2.8\), \(q_{\mathrm{A}}=1\). The effective plastic slip rate \(\dot{\gamma}^{(i)}\) is given by \(\dot{\gamma}^{(i)} = (\xi_{\mathrm{A}}/J_{\mathrm{tr}}) \dot{\gamma}_{\mathrm{A}}^{(i)}\).

### Crystallographic data for transformation systems
Provide the 24 transformation systems by applying the 24 cubic symmetry rotations to a base habit plane normal \(\mathbf{d}_0\) and base shape strain vector \(\mathbf{b}_0\). Define base vectors (in the austenite crystal frame):
\[
\begin{aligned}
\mathbf{d}_0 &= [0.1649,\; 0.7586,\; 0.6303] \quad (\text{unit vector}),\\
\mathbf{b}_0 &= [0.1987,\; -0.0272,\; 0.0126] \quad (\text{such that } \mathbf{b}_0\cdot\mathbf{d}_0 = 0.02 \text{ and } \delta_{\mathrm{T}}=0.02).
\end{aligned}
\]
The 24 cubic rotation matrices \(\mathbf{R}^{(k)}\) are (each row is a rotation matrix; entries are either -1, 0, or 1):
\[
\begin{aligned}
&\mathbf{R}^{(1)}\!=\!\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix},\,
\mathbf{R}^{(2)}\!=\!\begin{pmatrix}1&0&0\\0&0&1\\0&-1&0\end{pmatrix},\,
\mathbf{R}^{(3)}\!=\!\begin{pmatrix}1&0&0\\0&-1&0\\0&0&-1\end{pmatrix},\,
\mathbf{R}^{(4)}\!=\!\begin{pmatrix}1&0&0\\0&0&-1\\0&1&0\end{pmatrix},\\
&\mathbf{R}^{(5)}\!=\!\begin{pmatrix}0&1&0\\1&0&0\\0&0&-1\end{pmatrix},\,
\mathbf{R}^{(6)}\!=\!\begin{pmatrix}0&1&0\\0&0&1\\1&0&0\end{pmatrix},\,
\mathbf{R}^{(7)}\!=\!\begin{pmatrix}0&1&0\\-1&0&0\\0&0&1\end{pmatrix},\,
\mathbf{R}^{(8)}\!=\!\begin{pmatrix}0&1&0\\0&0&-1\\-1&0&0\end{pmatrix},\\
&\mathbf{R}^{(9)}\!=\!\begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix},\,
\mathbf{R}^{(10)}\!=\!\begin{pmatrix}0&0&1\\0&1&0\\-1&0&0\end{pmatrix},\,
\mathbf{R}^{(11)}\!=\!\begin{pmatrix}0&0&1\\-1&0&0\\0&-1&0\end{pmatrix},\,
\mathbf{R}^{(12)}\!=\!\begin{pmatrix}0&0&1\\0&-1&0\\1&0&0\end{pmatrix},\\
&\mathbf{R}^{(13)}\!=\!\begin{pmatrix}-1&0&0\\0&1&0\\0&0&-1\end{pmatrix},\,
\mathbf{R}^{(14)}\!=\!\begin{pmatrix}-1&0&0\\0&0&1\\0&1&0\end{pmatrix},\,
\mathbf{R}^{(15)}\!=\!\begin{pmatrix}-1&0&0\\0&-1&0\\0&0&1\end{pmatrix},\,
\mathbf{R}^{(16)}\!=\!\begin{pmatrix}-1&0&0\\0&0&-1\\0&-1&0\end{pmatrix},\\
&\mathbf{R}^{(17)}\!=\!\begin{pmatrix}0&-1&0\\1&0&0\\0&0&1\end{pmatrix},\,
\mathbf{R}^{(18)}\!=\!\begin{pmatrix}0&-1&0\\0&0&1\\-1&0&0\end{pmatrix},\,
\mathbf{R}^{(19)}\!=\!\begin{pmatrix}0&-1&0\\-1&0&0\\0&0&-1\end{pmatrix},\,
\mathbf{R}^{(20)}\!=\!\begin{pmatrix}0&-1&0\\0&0&-1\\1&0&0\end{pmatrix},\\
&\mathbf{R}^{(21)}\!=\!\begin{pmatrix}0&0&-1\\1&0&0\\0&-1&0\end{pmatrix},\,
\mathbf{R}^{(22)}\!=\!\begin{pmatrix}0&0&-1\\0&1&0\\1&0&0\end{pmatrix},\,
\mathbf{R}^{(23)}\!=\!\begin{pmatrix}0&0&-1\\-1&0&0\\0&1&0\end{pmatrix},\,
\mathbf{R}^{(24)}\!=\!\begin{pmatrix}0&0&-1\\0&-1&0\\-1&0&0\end{pmatrix}.
\end{aligned}
\]
Then for each \(k=1,\dots,24\) set \(\mathbf{d}^{(k)} = \mathbf{R}^{(k)}\mathbf{d}_0\) and \(\mathbf{b}^{(k)} = \mathbf{R}^{(k)}\mathbf{b}_0\).

### Slip systems for FCC austenite
The 24 slip systems are obtained from the 12 {111}⟨110⟩ systems as follows. Let the four slip plane normals (unit vectors) be:
\[
\begin{aligned}
\mathbf{n}_1 &= \frac{1}{\sqrt{3}}(1,1,1),\; \mathbf{n}_2 = \frac{1}{\sqrt{3}}(-1,1,1),\; \mathbf{n}_3 = \frac{1}{\sqrt{3}}(1,-1,1),\; \mathbf{n}_4 = \frac{1}{\sqrt{3}}(1,1,-1).
\end{aligned}
\]
For each plane \(\mathbf{n}_p\) (\(p=1,\dots,4\)), the three slip directions (unit vectors) are those ⟨110⟩ directions lying in the plane:
\[
\begin{aligned}
\mathbf{m}_{p,1} &= \text{one of the two } \langle 110\rangle \text{ directions in the plane},\\
\mathbf{m}_{p,2} &= \text{a second distinct } \langle 110\rangle \text{ direction},\\
\mathbf{m}_{p,3} &= \text{the third distinct } \langle 110\rangle \text{ direction}.
\end{aligned}
\]
Explicitly:
- For \(\mathbf{n}_1=(1,1,1)/\sqrt{3}\): \(\mathbf{m}_{1,1}=(0,1,-1)/\sqrt{2}\), \(\mathbf{m}_{1,2}=(-1,0,1)/\sqrt{2}\), \(\mathbf{m}_{1,3}=(1,-1,0)/\sqrt{2}\).
- For \(\mathbf{n}_2=(-1,1,1)/\sqrt{3}\): \(\mathbf{m}_{2,1}=(0,1,-1)/\sqrt{2}\), \(\mathbf{m}_{2,2}=(1,0,1)/\sqrt{2}\), \(\mathbf{m}_{2,3}=(1,1,0)/\sqrt{2}\).
- For \(\mathbf{n}_3=(1,-1,1)/\sqrt{3}\): \(\mathbf{m}_{3,1}=(0,1,1)/\sqrt{2}\), \(\mathbf{m}_{3,2}=(1,0,1)/\sqrt{2}\), \(\mathbf{m}_{3,3}=(1,1,0)/\sqrt{2}\).
- For \(\mathbf{n}_4=(1,1,-1)/\sqrt{3}\): \(\mathbf{m}_{4,1}=(0,1,1)/\sqrt{2}\), \(\mathbf{m}_{4,2}=(1,0,-1)/\sqrt{2}\), \(\mathbf{m}_{4,3}=(1,-1,0)/\sqrt{2}\).
The 12 slip systems are the pairs \((\mathbf{n}_p, \mathbf{m}_{p,q})\) for \(p=1,...,4\) and \(q=1,2,3\). To obtain the full set of 24 systems, duplicate each system and reverse the slip direction: i.e., for each \((\mathbf{n}, \mathbf{m})\) also include \((\mathbf{n}, -\mathbf{m})\) as a separate slip system.

### Material parameters (Table 1)
| Parameter(s) | Value(s) |
|---|---|
| **Mechanical** | |
| Elastic constants (GPa) | \(\kappa_1^A=286.8,\; \kappa_2^A=166.4,\; \kappa_3^A=145.0\) |
|  | \(\kappa_1^M=372.4,\; \kappa_2^M=345.0,\; \kappa_3^M=191.0\) |
|  | \(\kappa_4^M=508.4,\; \kappa_5^M=201.9,\; \kappa_6^M=229.5\) |
| Transformation kinetics | \(\dot{\xi}_0=0.003\ \mathrm{s^{-1}},\; \nu=0.17,\; f_{\mathrm{cr}}^{(\alpha)}=306\ \mathrm{MPa}\) |
| Surface energy | \(\chi=0.2\ \mathrm{J/m^2},\; l_0=0.05\ \mu\mathrm{m}\) |
| Plastic kinetics (austenite) | \(\dot{\gamma}_{0}^{\mathrm{A}}=0.001\ \mathrm{s^{-1}},\; n_{\mathrm{A}}=0.02\) |
| Defect energy (austenite) | \(\beta_{\mathrm{A},0}=0.0056,\; c_{\mathrm{A}}=0.5,\; \omega_{\mathrm{A}}=10\) |
| Hardening (austenite) | \(\mu_{\mathrm{A}}=67.5\ \mathrm{GPa},\; \mu^{(\alpha)}=98.4\ \mathrm{GPa},\; s_{\mathrm{A},0}=189\ \mathrm{MPa},\; s_\infty^{\mathrm{A}}=579\ \mathrm{MPa}\) |
|  | \(k_0^{\mathrm{A}}=3\ \mathrm{GPa},\; u_{\mathrm{A}}=2.8,\; q_{\mathrm{A}}=1\) |
| **Thermal** | |
| Latent heat | \(\lambda_{\mathrm{T}}^{(\alpha)} = -50.5\ \mathrm{kJ\,kg^{-1}}\) |
| Plastic thermal coefficient | \(\phi_{\mathrm{A}}^{(i)} = 5.13\ \mathrm{J\,kg^{-1}\,K^{-1}}\) |
| Specific heat (all phases) | \(h_{\mathrm{A}}=h^{(\alpha)}=450\ \mathrm{J\,kg^{-1}\,K^{-1}}\) |
| Thermal expansion coefficient | \(\alpha_{\mathrm{A}}=\alpha^{(\alpha)}=2.1\times10^{-5}\ \mathrm{K^{-1}}\) |
| Heat conductivity | \(k_{\mathrm{A}}=k^{(\alpha)}=60\ \mathrm{W\,m^{-1}\,K^{-1}}\) |
| Reference density | \(\rho_0 = 7800\ \mathrm{kg\,m^{-3}}\) |
| Transformation temperature | \(\theta_{\mathrm{T}} = 633\ \mathrm{K}\) |

### Simulation procedure
Implement the above model in an open-source finite element library or custom numerical code. Simulate a cubical single-crystal sample (edge length 1 µm) subjected to uniaxial nominal strain up to \(\varepsilon_{11}=0.2\) at a strain rate of \(10^{-4}\ \mathrm{s}^{-1}\). The sample is initially fully austenitic, stress-free, and at the specified initial temperature (300 K or 350 K). The thermal boundary conditions are either isothermal (temperature kept constant at initial value) or adiabatic (zero normal heat flux on all external faces). Run simulations for:
- orientation [100] (loading axis parallel to [100] crystal direction) at initial temperatures 300 K and 350 K, each with isothermal and adiabatic conditions;
- orientation [111] (loading axis parallel to [111]) at initial temperature 350 K, isothermal and adiabatic.
For each simulation, record the spatially averaged axial Cauchy stress \(T_{11}\), temperature \(\theta\), total martensite volume fraction \(\xi_{\mathrm{M}} = \sum_{\alpha}\xi^{(\alpha)}\), and plastic microstrain \(\beta\), as functions of axial logarithmic strain \(e_{11}\). Post-process to produce a CSV file with at least 200 strain points per case covering the strain range [0, 0.2].

## Reproduction target
Produce a CSV file `step_01_single_crystal_data.csv` containing the averaged thermomechanical response curves for the six required single‑crystal cases. The file must have columns: orientation ('100' or '111'), initial_temp_K, thermal_boundary ('iso' or 'thermo'), strain, stress_MPa, temperature_K, xi_M (total martensitic volume fraction, 0 to 1), and beta (plastic microstrain). Each case must be represented with at least 200 strain points covering the range from 0 to 0.2. The required cases are: orientation=100, initial_temp=300, thermal_boundary=iso and thermo; orientation=100, initial_temp=350, both; orientation=111, initial_temp=350, both. The hidden verifier will check the structural trends present in these curves (e.g., monotonicity, plateau presence, temperature rise, martensite fraction limits, and similarity between isothermal and adiabatic curves) using pre‑defined hidden thresholds.

## Assets

- Open-source finite element or numerical solver

## Workflow steps

### Step 1: Implement constitutive model and run finite element simulations
- Role: process
- Action: Implement the fully coupled thermomechanical constitutive model for FCC austenite as described in the Model formulation section, including finite-strain kinematics, crystal plasticity, martensitic phase transformation kinetics, and thermal coupling. Set up a single crystal cubical sample under uniaxial nominal strain up to 0.2 at a strain rate of 10⁻⁴ s⁻¹. Run the required cases as detailed in the simulation procedure. Save raw field outputs (stress, temperature, volume fractions, plastic microstrain) for post-processing.
- Evidence: `/app/outputs/simulation_summary.log`

### Step 2: Compile simulation results into CSV
- Role: scored (load-bearing)
- Action: Post-process the simulation outputs to extract axial Cauchy stress, temperature, total martensitic volume fraction ( ξ_M = 1 − ξ_A ), and plastic microstrain ( β ) as functions of axial logarithmic strain for each simulated case. Compute spatially averaged values where fields are heterogeneous and produce a single CSV file covering all required cases with a sufficient number of strain points.
- Output file: `/app/outputs/step_01_single_crystal_data.csv`
- Format: csv
- Contract: Columns: orientation (string, one of '100' or '111'), initial_temp_K (int), thermal_boundary (string, 'iso' or 'thermo'), strain (float), stress_MPa (float), temperature_K (float), xi_M (float, 0-1), beta (float). Each row is a strain point for a specific case. Required cases: orientation=100, initial_temp=300, thermal_boundary=iso and thermo; orientation=100, initial_temp=350, both; orientation=111, initial_temp=350, both. Minimum 200 strain points per case covering [0,0.2].
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_single_crystal_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_single_crystal_data.csv
- path: `/app/outputs/step_01_single_crystal_data.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Compiled averaged single-crystal response for all required thermomechanical and isothermal cases. The file must contain at least the six required condition sets, each with ≥200 strain points covering the strain range [0, 0.2].
- schema:
  - `type`: table
  - `required_columns`: `orientation`, `initial_temp_K`, `thermal_boundary`, `strain`, `stress_MPa`, `temperature_K`, `xi_M`, `beta`
  - `orientation`: string: '100' or '111'
  - `initial_temp_K`: integer
  - `thermal_boundary`: string: 'iso' or 'thermo'
  - `strain`: float
  - `stress_MPa`: float
  - `temperature_K`: float
  - `xi_M`: float (0 to 1)
  - `beta`: float

Notes: The scored artifact captures the qualitative trends in stress-strain, temperature, martensitic volume fraction, and plastic microstrain as a function of loading direction, initial temperature, and thermal boundary condition. The hidden checker validates these structural relations against paper-derived thresholds.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_single_crystal_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "orientation",
          "initial_temp_K",
          "thermal_boundary",
          "strain",
          "stress_MPa",
          "temperature_K",
          "xi_M",
          "beta"
        ],
        "orientation": "string: '100' or '111'",
        "initial_temp_K": "integer",
        "thermal_boundary": "string: 'iso' or 'thermo'",
        "strain": "float",
        "stress_MPa": "float",
        "temperature_K": "float",
        "xi_M": "float (0 to 1)",
        "beta": "float"
      },
      "description": "Compiled averaged single-crystal response for all required thermomechanical and isothermal cases. The file must contain at least the six required condition sets, each with ≥200 strain points covering the strain range [0, 0.2]."
    }
  ],
  "notes": "The scored artifact captures the qualitative trends in stress-strain, temperature, martensitic volume fraction, and plastic microstrain as a function of loading direction, initial temperature, and thermal boundary condition. The hidden checker validates these structural relations against paper-derived thresholds."
}
```

## How you are scored
The hidden verifier independently scores the artifacts from each workflow stage. For the scored CSV file (`step_01_single_crystal_data.csv`), the verifier parses the data, groups the rows by orientation, initial temperature, and thermal boundary condition, and checks that all required cases are present with at least 200 strain points each. It then verifies a set of structural properties — such as relative ordering of stress‑strain curves, presence of a stress plateau versus monotonic increase, magnitude of temperature rise, and whether martensite volume fractions fall within expected ranges for each case — against hidden tolerances derived from the expected physical behaviour. No single numerical value is expected to match the original paper; the task measures whether the coupled thermomechanical implementation reproduces the correct qualitative trends. The reward is a weighted combination of these checks, giving highest weight to the scatter structural correctness of the CSV data.
