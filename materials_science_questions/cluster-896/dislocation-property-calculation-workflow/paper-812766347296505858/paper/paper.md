MRS – Fall Meeting
Boston, Massachusetts
July 16 - 22, 2006

Mechanical and Aerospace Engineering Department
School of Engineering and Applied Science
University of California, Los Angeles

Mater. Res. Soc. Symp. Proc. Vol. 978 © 2007 Materials Research Society
0978-GG12-03-EE08-03

# Three-Dimensional Boundary Element - Dislocation Dynamics Modeling of Plastic Flow in Small Volumes

__Jaafar A. El-Awady__
University of California, Los Angeles

Akiyuki Takahashi,
Tokyo University of Science

__Nasr M. Ghoniem__
University of California, Los Angeles

![](./images/812766347296505858_1.jpg)

UCLA

### Outline

- Introduction
- Boundary Element Method (BEM)
- Parametric Dislocation Dynamics (PDD)
- Consistency of the Parametric Dislocation Dynamics and the Boundary Element Method
- Accuracy and Convergence Analyses
- PDD-BEM 3D Modeling of:
  - Interaction Between Dislocations and Precipitates/Voids
  - Size Effects on the Strength of Micro-crystals
- Conclusions

---
MRS – Fall Meeting
Boston, MA

Nov. 29ᵗʰ, 2006

Jaafar A. El-Awady

UCLA

# BEM or FEM ?

BEM is advantageous over FEM for the following reasons:
- Discretization takes place only on the surface, thus, reducing the total # of DOF (i.e. less computer time and storage)
- Stresses and displacements at interior points are calculated more accurately in the BEM, because all field variables are discretized on the surface and no further approximation is imposed on the solution at interior points.
- In FEM, interpolation of field variables is required at locations not coinciding with Gaussian integration points. On the other hand, stresses and displacements in the BEM are calculated directly at the point of interest

![](./images/812766347296505858_2.jpg)

Boundary Element Method

The fundamental solution is based on the 3-dimensional classical solution of a point force in an infinite medium (i.e. Kelvin solution)

![](./images/812766347296505858_3.jpg)

**Displacement vector:**

$$
u_i = U_{ij}(p, Q)e_j
$$

$$
U_{ij}(p, Q)=\frac{1}{16\pi\mu(1-v)}\left[\frac{1}{R(p, Q)}\right]\left[(3-4v)\delta_{ij}+\frac{\partial R(p, Q)}{\partial x_i}\frac{\partial R(p, Q)}{\partial x_j}\right]
$$

**Traction vector:**

$$
t_i = T_{ij}(p, Q)e_j
$$

$$
\begin{aligned}
T_{ij}(p, Q)&=\frac{-1}{8\pi(1-v)R^2(p, Q)}\left[\frac{\partial R(p, Q)}{\partial n}\right]\left[(1-2v)\delta_{ij}+3\frac{\partial R(p, Q)}{\partial x_i}\frac{\partial R(p, Q)}{\partial x_j}\right] \\
&-\frac{1-2v}{8\pi(1-v)R^2(p, Q)}\left[\frac{\partial R(p, Q)}{\partial x_j}n_i-\frac{\partial R(p, Q)}{\partial x_i}n_j\right]
\end{aligned}
$$


### Boundary Element Method

- Using the Kelvin solution and the reciprocal theory, the BIE is given by

$$
u_{i}(P)=\int_{S} U_{i j}(P, Q) t_{j}(Q) d S(Q)-\int_{S} T_{i j}(P, Q) u_{j}(Q) d S(Q)
$$

- A similar BIE for the stresses can be developed as well:

$$
\sigma_{i j}(P)=\int_{S} G_{k i j}(P, Q) t_{k}(Q) d S(Q)-\int_{S} H_{k i j}(P, Q) u_{k}(Q) d S(Q)
$$

where

$$
G_{k i j}=\frac{1}{8 \pi(1-\nu) R^{2}}\left[(1-2 \nu)\left(R_{, i} \delta_{j k}+R_{, j} \delta_{i k}-R_{, k} \delta_{i j}\right)+3 R_{, i} R_{, j} R_{, k}\right]
$$

$$
\begin{aligned}
H_{k i j}=& \frac{\mu}{4 \pi(1-\nu) R^{3}}\left(n_{i}\left[3 \nu R_{, j} R_{, k}+(1-2 \nu) \delta_{i j}\right]+n_{j}\left[3 \nu R_{, i} R_{, k}+(1-2 \nu) \delta_{i k}\right]\right. \\
&+n_{k}\left[(1-2 \nu) R_{, i} R_{, j}+(1-4 \nu) \delta_{i j}\right] \\
&+3 \frac{\partial R}{\partial n}\left[(1-2 \nu) R_{, k} \delta_{i j}+\nu\left(\delta_{j k} R_{, i}+R_{, j} \delta_{i k}\right)-5 R_{, i} R_{, j} R_{, k}\right]
\end{aligned}
$$

$n_k$: are the components of the unit outward normal

# Boundary Element Method

![](./images/812766347296505858_4.jpg)

On the Boundary:

$$
\begin{aligned}
C_{i j}(P) u_{j}(P)+\sum_{m=1}^{N_{e l e m}} \sum_{c=1}^{N_{n o d e}} u_{j}(Q) \int_{-1-1}^{+1+1} \int_{i j} T_{i j}(P, Q) N_{c}\left(\xi_{1}, \xi_{2}\right) J\left(\xi_{1}, \xi_{2}\right) d \xi_{1} d \xi_{2} \\
=\sum_{m=1}^{N_{e l e m}} \sum_{c=1}^{N_{n o d e}} t_{j}(Q) \int_{-1-1}^{+1+1} \int_{i j} U_{i j}(P, Q) N_{c}\left(\xi_{1}, \xi_{2}\right) J\left(\xi_{1}, \xi_{2}\right) d \xi_{1} d \xi_{2}
\end{aligned}
$$

![](./images/812766347296505858_5.jpg)

$$
\begin{aligned}
{\left[\begin{array}{lll}
C_{x x}(P) & C_{x y}(P) & C_{x z}(P) \\
C_{y x}(P) & C_{y y}(P) & C_{y z}(P) \\
C_{z x}(P) & C_{z y}(P) & C_{z z}(P)
\end{array}\right]\left[\begin{array}{l}
u_{x}(P) \\
u_{y}(P) \\
u_{z}(P)
\end{array}\right]+\sum_{m=1}^{N_{e l e m}} \sum_{c=1}^{N_{n o d e}}\left[\begin{array}{lll}
A_{x x} & A_{x y} & A_{x z} \\
A_{y x} & A_{y y} & A_{y z} \\
A_{z x} & A_{z y} & A_{z z}
\end{array}\right]\left[\begin{array}{l}
u_{x}(Q) \\
u_{y}(Q) \\
u_{z}(Q)
\end{array}\right] } \\
=\sum_{m=1}^{N_{e l e m}} \sum_{c=1}^{N_{n o d e}}\left[\begin{array}{lll}
B_{x x} & B_{x y} & B_{x z} \\
B_{y x} & B_{y y} & B_{y z} \\
B_{z x} & B_{z y} & B_{z z}
\end{array}\right]\left[\begin{array}{l}
t_{x}(Q) \\
t_{y}(Q) \\
t_{z}(Q)
\end{array}\right]
\end{aligned}
$$

![](./images/812766347296505858_6.jpg)

![](./images/812766347296505858_7.jpg)

Taking each node in tern as the load
point $P$, a set of linear algebraic equations
emerges as follows:

$$
[A]\{u\}=[B]\{t\}
$$

# Parametric Dislocation Dynamics

- Following (Ghoniem et. al. 2000), the governing equation of motion of a single loop is:

$$
\sum_{j=1}^{N_{s}} \int_{\Gamma_{j}} \delta \mathrm{Q}^{\top}\left(\mathrm{C}^{\top} \mathbf{f}^{*}-\mathrm{C}^{\top} \mathrm{C} \frac{d \mathrm{Q}}{d t^{*}}\right)|d \mathbf{s}|=0
$$

$$
\mathbf{f}_{j}=\int_{\Gamma_{j}} \mathrm{C}^{\top} \mathbf{f}^{*}|d \mathbf{s}|, \quad \mathbf{k}_{j}=\int_{\Gamma_{j}} \mathrm{C}^{\top} \mathrm{C}|d s|
$$

- Define:

$$
\mathbf{F}=\sum_{j=1}^{N_{s}} \mathbf{f}_{j}, \quad \mathbf{K}=\sum_{j=1}^{N_{s}} \mathbf{k}_{j}
$$

![](./images/812766347296505858_8.jpg)

- The equation of motion becomes:

$$
\mathbf{K} \frac{d \mathrm{Q}}{d t^{*}}=\mathbf{F}
$$

- The force applied on the dislocation is calculated from:

$$
f^{*}=f_{s}+f_{i m}+f_{P K}
$$

$$
f=(\sigma \bullet b) \times t
$$

![](./images/812766347296505858_9.jpg)

Finite Geometry: Superposition method (BVP)

![](./images/812766347296505858_10.jpg)

Consistency of the Parametric Dislocation Dynamics
and the Boundary Element Methods

- Following (Ghoniem et. al. 2000) the *infinite medium* stress field can
be represented by a fast numerical sum

$$
\begin{aligned}
\widetilde{\sigma}_{i j} & =\frac{\mu}{4 \pi} \sum_{\gamma=1}^{N_{l o o p}} \sum_{\alpha=1}^{N_{s e g}} \sum_{\beta=1}^{Q_{m a x}} b_{n} w_{\alpha}[\frac{1}{2} R_{, m p p}\left(\epsilon_{j m n} \hat{x}_{i, \omega}+\epsilon_{i m n} \hat{x}_{j, \omega}\right) \\
& +\frac{1}{1-\nu} \epsilon_{i m n}\left(R_{, i j m}-\delta_{i j} R_{, p p m}\right) \hat{x}_{k, \omega}]
\end{aligned}
$$

- Similarly, the *image field* given by the BEM on the dislocation can be
represented in a fast numerical sum as follows:

$$
\begin{aligned}
\widehat{\sigma}_{i j}(P) & =\sum_{m=1}^{N_{e}} \sum_{c=1}^{N_{n}} \sum_{n=1}^{N_{G a u s s}} \sum_{s=1}^{N_{G a u s s}} w_{n} w_{s} G_{k i j}(P, Q) N_{c}\left(x_{1}, x_{2}\right) J\left(x_{1}, x_{2}\right) t_{k}(Q) \\
& -\sum_{m=1}^{N_{e}} \sum_{c=1}^{N_{n}} \sum_{n=1}^{N_{G a u s s}} \sum_{s=1}^{N_{G a u s s}} w_{n} w_{s} H_{k i j}(P, Q) N_{c}\left(x_{1}, x_{2}\right) J\left(x_{1}, x_{2}\right) u_{k}(Q)
\end{aligned}
$$

MRS – Fall Meeting
Boston, MA
Nov. 29th, 2006
Jaafar A. El-Awady
![](./images/812766347296505858_11.jpg)

# Accuracy and Convergence Analyses

## Case 1: Screw Dislocation Parallel to a Free Surface

![](./images/812766347296505858_12.jpg)

![](./images/812766347296505858_13.jpg)

![](./images/812766347296505858_14.jpg)

![](./images/812766347296505858_15.jpg)

The surface mesh density: (-Δ-) 6 x 6 elements, (-◇-) 8 x 8 elements, (-o-) 10 x 10 elements, (-x-) 12 x 12 elements, and (-□-) 20 x 10 elements

# Accuracy and Convergence Analyses

## Case 2: Cylinder Containing a Coaxial Screw Dislocation

![](./images/812766347296505858_16.jpg)

Results based on the PDD-BEM model
(a) Un-deformed (b) deformed cylinder

![](./images/812766347296505858_17.jpg)

Relative error in the relative twist
between two cross-sections.

# PDD-BEM 3D Modeling of Interaction Between Dislocations and Precipitates/Voids

- Interaction between dislocations and precipitate/void
  - Precipitate Hardening
    - The strength of metals can be improved by forming precipitates
  - Irradiation Damage
    - Formations of precipitates causes a material embrittlement

![](./images/812766347296505858_18.jpg)

# Dislocation - Precipitate Interaction Problem

![](./images/812766347296505858_19.jpg)

$$\tilde{\sigma}_{ij} = C_{ijkl} \left( \varepsilon_{kl}^{\infty} + \tilde{\varepsilon}_{kl} \right) \quad \text{in } D$$

Dislocation Problem

$$
\begin{aligned}
\hat{\sigma}_{ij} &= C_{ijkl} \hat{\varepsilon}_{kl} \quad \text{in } D - \Omega \\
\hat{\sigma}_{ij} &= C_{ijkl}^m \left( \hat{\varepsilon}_{kl} - \varepsilon_{kl}^p \right) + \left( C_{ijkl}^m - C_{ijkl} \right) \left( \varepsilon_{kl}^{\infty} + \tilde{\varepsilon}_{kl} \right) \\
&= C_{ijkl}^m \hat{\varepsilon}_{kl} + \Sigma_{ij}^m
\end{aligned}
\quad \text{in } \Omega^m
$$

Correction Problem

Eigen strain

# Dislocation - Precipitate Interaction Problem: Boundary Element Formulation

## Multizone Boundary Element Method

![](./images/812766347296505858_20.jpg)

$$
c_{ij}(P)u_j(P)=\int_{S} \left\{U_{ij}(P,Q)t_{ij}(Q)-T_{ij}(P,Q)u_j(Q)\right\}dS \quad \text{for } D-\Omega
$$

$$
u_j^m = u_j,\ t_j^m + t_j = 0 \quad \text{on } S^m
$$

$$
\begin{aligned}
c_{ij}^m(P)u_j^m(P)&=\int_{S^m} \left\{U_{ij}^m(P,Q)t_{ij}^m(Q)-T_{ij}^m(P,Q)u_j^m(Q)\right\}dS \\
&\quad -\int_{\Omega^m} \sum_{jk}^m(q)U_{ij.k}^m(P,q)d\Omega
\end{aligned}
\quad \text{for } \Omega^n
$$

MRS – Fall Meeting
Boston, MA

Nov. 29th, 2006
Jaafar A. El-Awady
UCLA

# Dislocation - Precipitate Interaction Problem: Model

Interaction between an edge dislocation and a copper precipitate

Evaluate the critical shear stress

![](./images/812766347296505858_21.jpg)

Dislocation - Precipitate Interaction Problem: Boundary (+Volume) Elements

![](./images/812766347296505858_22.jpg)

![](./images/812766347296505858_23.jpg)

![](./images/812766347296505858_24.jpg)

![](./images/812766347296505858_25.jpg)

![](./images/812766347296505858_26.jpg)

MRS – Fall Meeting
Boston, MA
Nov. 29ᵗʰ, 2006
Jaafar A. El-Awady
UCLA

Dislocation - Precipitate Interaction Problem:
Numerical Simulations

![](./images/812766347296505858_27.jpg)

$(d_{Cu}=3nm)$

![](./images/812766347296505858_28.jpg)

MRS – Fall Meeting
Boston, MA

Nov. 29th, 2006

Jaafar A. El-Awady
UCLA

# Dislocation - Precipitate Interaction Problem: Numerical Simulations

![](./images/812766347296505858_29.jpg)

*C.Kohler, P.Kizler and S.Schmauder, Model. Simul. Mater. Sci. Eng. 13 (2005) 35-45

MRS – Fall Meeting
Boston, MA

Nov. 29ᵗʰ, 2006

Jaafar A. El-Awady
UCLA

# Dislocation - Precipitate Interaction Problem: Effect of Elastic Constants

$$(d_p = 7.5nm)$$

<table>
  <tr>
    <td>![](./images/812766347296505858_30.jpg)</td>
    <td>![](./images/812766347296505858_31.jpg)</td>
  </tr>
  <tr>
    <td>$$\mu_p/\mu_m = 2$$</td>
    <td>$$\mu_p/\mu_m = 6$$</td>
  </tr>
</table>

MRS – Fall Meeting
Boston, MA

Nov. 29ᵗʰ, 2006
Jaafar A. El-Awady
UCLA

Dislocation-Void Interaction Problem

![](./images/812766347296505858_32.jpg)

$$\tilde{\sigma}_{ij} = C_{ijkl} \left( \varepsilon_{kl}^{\infty} + \tilde{\varepsilon}_{kl} \right) \quad \text{in } D$$

$$\hat{\sigma}_{ij} = C_{ijkl} \hat{\varepsilon}_{kl} \quad \text{in } D - \Omega$$

Solved by BEM with the free
surface boundary condition

# Dislocation - Void Interaction Problem: Numerical Simulations

![](./images/812766347296505858_33.jpg)

$(d_V = 7.5nm)$

![](./images/812766347296505858_34.jpg)

MRS – Fall Meeting
Boston, MA

Nov. 29th, 2006

Jaafar A. El-Awady
UCLA

# PDD-BEM 3D Modeling of Size Effects on the Strength of Micro-crystals

![](./images/812766347296505858_35.jpg)

Ni₃Al0.2%Hf micro-crystal deformed to an engineering strain of 5.5%.

![](./images/812766347296505858_36.jpg)

![](./images/812766347296505858_37.jpg)

![](./images/812766347296505858_38.jpg)

![](./images/812766347296505858_39.jpg)

SEM images of Ni single micro-crystals

![](./images/812766347296505858_40.jpg)

![](./images/812766347296505858_41.jpg)

SEM images of UM-F19 micro-crystals

(Dimiduk et. al. 2005; Uchic et. al. 2005, 2006)

MRS – Fall Meeting
Boston, MA

Nov. 29ᵗʰ, 2006

Jaafar A. El-Awady

UCLA

PDD-BEM 3D Modeling of Size Effects on the Strength of Micro-crystals

**Motivation:**
- Study the plastic deformation of micron-size single crystals using 3D parametric dislocation dynamics coupled with the boundary element method.

**Objective:**
- Analyze the crystal-size dependence of the stress versus strain response for cylindrical microcrystals oriented for single slip and double slip having sample diameters in the range 0.25 to $40\ \mu\text{m}$.
- Statistical aspects of dislocation production from crystal surfaces, activation of internal dislocation sources, and the cross-slip process will be included in the analysis.

MRS – Fall Meeting
Boston, MA

Nov. 29ᵗʰ, 2006

Jaafar A. El-Awady
![](./images/812766347296505858_42.jpg)

Applications: 3D Modeling using BEM-PDD of Size
Effects on the Strength of Micro-crystals

**Model:**
- The plastic flow arise from the collective motion of dislocations in the solid.
- Interaction between dislocations and the finite surfaces are directly accounted for using the BEM.
- Dislocation generation rises
from one of two sources:
  ✓ Activation of internal
    dislocation sources
  ✓ Nucleation from
    surface defects

![](./images/812766347296505858_43.jpg)

MRS – Fall Meeting
Boston, MA
Nov. 29ᵗʰ, 2006
Jaafar A. El-Awady
UCLA

# Applications: 3D Modeling using PDD-BEM of Size Effects on the Strength of Micro-crystals

Preliminary results from applying the PDD-BEM on pure Nickel single crystals oriented for single slip:

![](./images/812766347296505858_44.jpg)

$D \cong 0.9\mu m$

MRS – Fall Meeting
Boston, MA
Nov. 29th, 2006
Jaafar A. El-Awady
UCLA

# Applications: 3D Modeling using PDD-BEM of Size Effects on the Strength of Micro-crystals

The mechanism of
step formation on the
cylinder free surface

![](./images/812766347296505858_45.jpg)

SEM micrograph of
Ni single micro-crystals
(Dimiduk et. al. 2005)

![](./images/812766347296505858_46.jpg)

![](./images/812766347296505858_47.jpg)

From the BEM-PDD modeling

# On Going Simulations

![](./images/812766347296505858_48.jpg)

MRS – Fall Meeting
Boston, MA

Nov. 29ⁿᵗʰ, 2006

Jaafar A. El-Awady
UCLA

# Cross-slip due to Image Force Effects

- Force distribution on a FR source expanding towards a free surface:

![](./images/812766347296505858_49.jpg)

- Cross slip and surface extrusion

![](./images/812766347296505858_50.jpg)

![](./images/812766347296505858_51.jpg)

![](./images/812766347296505858_52.jpg)

SEM micrograph of
Ni single micro-crystals
(Dimiduk et. al. 2005)

Imagine The Possibilities......!

![](./images/812766347296505858_53.jpg)

![](./images/812766347296505858_54.jpg)

+

![](./images/812766347296505858_55.jpg)

= ?

![](./images/812766347296505858_56.jpg)

SEM images of
UM-F19 micro-
crystals
(Dimiduk et. al.)

MRS – Fall Meeting
Boston, MA
Nov. 29ᵗʰ, 2006
Jaafar A. El-Awady
UCLA

### Conclusions

- BEM is advantageous over FEM in dislocation dynamic analysis for a number of reasons: smaller # of DOF, more accurate, direct evaluation of variables directly on the dislocations, similar frame work as the PDD

- A PDD-BEM model was developed to:
  - accurately and easily evaluate the image filed for finite geometry problems
  - model the interaction between dislocations and precipitates/voids

- The PDD - BEM model gives good convergence of accuracy and results that are consistent with other MD and analytical results

- The PDD-BEM model is being used to study the size effects on the strength of micro-crystals and any geometry changes can be captured easily by remishing the surface when the dislocation cross out of the surface

---

MRS – Fall Meeting
Boston, MA

Nov. 29th, 2006

Jaafar A. El-Awady

![](./images/812766347296505858_57.jpg)