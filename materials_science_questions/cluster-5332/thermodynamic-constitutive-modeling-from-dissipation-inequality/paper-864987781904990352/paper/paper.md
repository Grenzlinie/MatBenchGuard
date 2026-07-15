Received: 20 April 2022
Revised: 28 July 2022
Accepted: 31 July 2022

DOI: 10.1002/nme.7085

# RESEARCH ARTICLE

# An acoustic Riemann solver for large strain computational contact dynamics

Callum J. Runcie¹ | Chun Hean Lee¹ | Jibran Haider² | Antonio J. Gil³ | Javier Bonet⁴

¹Glasgow Computational Engineering Centre, James Watt School of Engineering, University of Glasgow, Glasgow, UK

²Cambridge Flow Solutions Ltd., Cambridge Science Park, Cambridge, UK

³Zienkiewicz Centre for Computational Engineering, Faculty of Science and Engineering, Swansea University, Bay Campus, Swansea, UK

⁴Centre Internacional de Mètodes Numèrics en Enginyeria (CIMNE), Universitat Politècnica de Catalunya, Barcelona, 08034, Spain

## Correspondence
Chun Hean Lee, Glasgow Computational Engineering Centre, James Watt School of Engineering, University of Glasgow, Glasgow, UK.
Email: chunhean.lee@glasgow.ac.uk

## Funding information
Engineering and Physical Sciences Research Council, Grant/Award Number: EP/R008531/1; H2020 Marie Skłodowska-Curie Actions, Grant/Award Number: 764636

## Abstract
This article presents a vertex-centered finite volume algorithm for the explicit dynamic analysis of large strain contact problems. The methodology exploits the use of a system of first order conservation equations written in terms of the linear momentum and a triplet of geometric deformation measures (comprising the deformation gradient tensor, its co-factor, and its Jacobian) together with their associated jump conditions. The latter can be used to derive several dynamic contact models ensuring the preservation of hyperbolic characteristic structure across solution discontinuities at the contact interface, a clear advantage over the standard quasi-static contact models where the influence of inertial effects at the contact interface is completely neglected. Taking advantage of the conservative nature of the formalism, both kinetic (traction) and kinematic (velocity) contact interface conditions are explicitly enforced at the fluxes through the use of appropriate jump conditions. Specifically, the kinetic condition is enforced in the usual linear momentum equation, whereas the kinematic condition can now be easily enforced in the geometric conservation equations without requiring a computationally demanding iterative algorithm. Additionally, a total variation diminishing shock capturing technique can be suitably incorporated in order to improve dramatically the performance of the algorithm at the vicinity of shocks. Moreover, to guarantee stability from the spatial discretization standpoint, global entropy production is demonstrated through the satisfaction of semi-discrete version of the classical Coleman–Noll procedure expressed in terms of the time rate of the so-called Hamiltonian energy of the system. Finally, a series of numerical examples is examined in order to assess the performance and applicability of the algorithm suitably implemented in OpenFOAM. The knowledge of the potential contact loci between contact interfaces is assumed to be known a priori.

## KEYWORDS
conservation laws, explicit contact dynamics, large strain, OpenFOAM, Riemann solver, shocks

This is an open access article under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in any medium, provided the original work is properly cited.

© 2022 The Authors. *International Journal for Numerical Methods in Engineering* published by John Wiley & Sons Ltd.

5700 | wileyonlinelibrary.com/journal/nme
Int J Numer Methods Eng. 2022;123:5700–5748.

# 1 | INTRODUCTION

In computational mechanics, the numerical modeling of contact and impact phenomena has been a major field of interest in industry, including numerous applications such as vehicle crash testing,¹ prototype testing, or manufacturing processes.²·³ These very complex problems are typically characterized by highly nonlinear deformation behavior with accompanying non-smooth response (or shocks) caused by transitions between various contact modes such as separation-to-contact, stick-to-slip, slip/stick-to-separation. Such problems must be solved by ensuring the satisfaction of linear momentum conservation equation (complemented by appropriate initial and boundary conditions) for each body individually, whilst at the same time enforcing the additional set of (kinematic and kinetic) contact interface conditions, that govern the interaction of these bodies.

When considering a model with frictionless contact, these interface conditions act to prevent interpenetration of the bodies (kinematic condition) and to insure compressive interaction normal to the interface (kinetic condition). One challenging aspect, is that impenetrability cannot be expressed as an evolution (or algebraic) equation and so requires special numerical treatment. The most common techniques addressing this issue include penalty method, Lagrange multiplier method, or a combination of both. In the penalty method,⁴ the impenetrability constraint is enforced as a penalty normal traction along the contact surface. The disadvantage of the penalty approach is that the enforcement of the impenetrability condition is only approximate and its effectiveness depends on the selection of the user-defined penalty parameters. If the value of the penalty parameter is too small, unpredictable amount of interpenetration would be observed. However, the penalty parameter cannot be arbitrarily large, as this can generate ill-conditioned systems that may require extremely small time steps for stability.⁵·⁶ The correct choice for this parameter is key to success of the algorithm. For the Lagrange multiplier method,⁷·⁸ the multipliers must be approximated and solved at the contact interface with the constraint such that the normal component of the traction must be compressive. The disadvantage of the method is that it requires the construction of a separate independent mesh and also requires the introduction of additional regularization techniques necessary in obtaining robust solutions. Such regularization procedures are usually ad-hoc and are not motivated by physical arguments. A popular example of regularization is the addition of von Neumann's artificial viscosity⁹·¹⁰ to the Euler fluid equations to smear shocks over several computational cells. In absence of this artificial viscosity, central difference solutions to the Euler equation in the vicinity of shocks are oscillatory, eventually leading to the breakdown of a numerical scheme.

One of the earliest attempts at enforcing contact interface conditions via the physically-motivated jump conditions that derive from the linear momentum conservation equation and kinematic compatibility can be traced back to the work of Abedi and Haber.¹¹ In particular, a space-time discontinuous Galerkin finite element method for elasto-dynamic contact was presented. The presented examples were restricted to the case of small strain linear elasticity in two dimensions. Moreover, it is not yet clear if the overall finite element algorithm would satisfy the classical Coleman-Noll procedure in order to guarantee the production of non-negative entropy. On another front, some interesting works have also been explored using the computational fluid dynamics (CFD) platform "OpenFOAM" via the use of displacement-based finite volume discretization,¹²·¹³ with special attention paid to the quasi-static simulation based on the use of penalty method¹⁴·¹⁵ and lubricated contact models.¹⁶

Aiming to resolve the shortcomings described above, the main goal of this article is to explore the solution of contact dynamics utilizing a set of first order conservation equations,¹⁷⁻²⁰ combined with the associated jump conditions across moving shocks*.²¹⁻³³ Building upon previous work developed by the authors,³⁴·³⁵ a mixed methodology is presented in the form of a system of hyperbolic conservation laws, where the linear momentum and the minors of deformation (the deformation gradient tensor, its co-factor and its Jacobian) are regarded as the main conservation variables of this mixed approach. Taking advantage of this formalism, appropriate kinetic and kinematic contact interface conditions can be suitably enforced at the boundary fluxes of the underlying hyperbolic system by means of the Rankine-Hugoniot jump conditions. For instance, in the case of frictionless contact, the normal traction is enforced in the standard manner, that is, in the boundary fluxes of linear momentum conservation equation. One crucial advantage of solving the geometric conservation equations in this context is such that we now have the luxury of explicitly enforcing the normal component of the contact velocity in the associated boundary fluxes. On the other hand, upon the use of Rankine-Hugoniot jump conditions,³⁶ we can then naturally derive a series of dynamic contact models typically required in the simulation of contact problems. The objective of this article is to present a complete set of continuum Riemann-based type solutions for contact and separation (derived based on a system of first order conservation laws) assuming a priori knowledge of

the potential contact loci. Physically, Riemann solutions describe correct fluxes in the form of traction and velocity at the contact interface. In linear elasticity, we can show that by enforcing appropriate boundary fluxes at the point of contact through the use of jump conditions would lead to exact energy transfer, provided the shock wave travels at the speed of sound.

From a spatial discretization point of view, a vertex based finite volume algorithm³⁴ in conjunction with (piecewise) linear reconstruction is employed. Additionally, a shock capturing technique³⁷ can also be incorporated in order to dramatically improve the resolution of the field variables at the vicinity of shocks. No ad-hoc algorithmic regularization procedures are needed. Insofar as contact-impact introduces discontinuities in the solution, the use of explicit time integrators is preferred (see Chapter 10 in Reference 5) as neither linearization nor a Newton's method is required. With this in mind, from a temporal discretization standpoint, we use the explicit type of two-stage Runge-Kutta time integrator. A crucial aspect that requires special attention is that of the stability of the overall algorithm.³⁸ This can be demonstrated by monitoring over time the Hamiltonian energy of the system, ensuring the production of entropy throughout the entire simulation. The overall methodology is shown to be capable of handling contact-impact problems without excessive spurious modes, even in the case of nearly incompressible elasticity and elasto-plasticity. Examples presented in the article are specifically chosen in order to illustrate the capability of the proposed framework addressing spurious oscillations in problems with shocks (or spatial jumps) without resorting to ad-hoc dissipative correction. Another contribution of the current work is to carry out its implementation into the OpenFOAM platform, widely accepted these days by industry.

The article is broken-down into the following sections. Section 2 starts by summarizing the total Lagrangian formulation of the conservation laws to be solved, comprising the linear momentum and the three geometric conservation laws. Section 3 provides the exact solution of the simple one dimensional two-bar impact derived from the associated jump conditions in linear elasticity. This leads to exact energy transfer from one bar to the other after contact without energy loss. Motivated by this, the section continues deriving a set of interface contact conditions (velocity and stress) applicable to multi-dimensional contact problems. Section 4 presents the second law of thermodynamics written in terms of the so-called Hamiltonian free energy. Section 5 describes the computational methodology of the vertex centered finite volume method. A proof of entropy production is included as a necessary condition for stability at the semi-discrete level. Section 6 includes the algorithmic flowchart of the resulting numerical scheme where special attention is paid to the procedure in addressing non-matching mesh interface. Section 7 presents a set of numerical examples to assess the accuracy and stability of the computational framework, with detailed comparison with other verified finite element code such as Abaqus. Section 8 presents some concluding remarks.

## 2 | FIRST ORDER HYPERBOLIC SYSTEM FOR SOLID DYNAMICS

Consider the three dimensional deformation of an isothermal body of material density $\rho_R$ moving from its initial undeformed configuration $\Omega_V$, with boundary $\partial\Omega_V$ defined by an outward unit normal $\boldsymbol{N}$, to a current deformed configuration $\Omega_v(t)$ at time $t$, with boundary $\partial\Omega_v(t)$ defined by an outward unit normal $\boldsymbol{n}$. The time dependent motion $\boldsymbol{\phi}(\boldsymbol{X},t)$ of the body can be described by the following system of total Lagrangian global conservation laws³⁵,³⁹⁻⁵²

$$
\frac{d}{dt} \int_{\Omega_V} \mathcal{V} \, d\Omega_V + \int_{\partial\Omega_V} \mathcal{F}_N \, dA = \int_{\Omega_V} \mathcal{S} \, d\Omega_V \quad \text{in} \quad \Omega_V, \tag{1}
$$

with the surface flux vector being defined as $\mathcal{F}_N = \sum_{I=1}^3 \mathcal{F}_I N_I$. Here, $\mathcal{V}$ is the vector of conservation variables, $\mathcal{F}_I$ is the flux vector at $I$th material direction and $\mathcal{S}$ is the source term. Their components are

$$
\mathcal{V} = \begin{bmatrix}
\boldsymbol{p} \\
\boldsymbol{F} \\
\boldsymbol{H} \\
J
\end{bmatrix}, \quad
\mathcal{F}_I = -\begin{bmatrix}
\boldsymbol{P}E_I \\
\boldsymbol{v} \otimes E_I \\
\boldsymbol{F} \times (\boldsymbol{v} \otimes E_I) \\
\boldsymbol{H} : (\boldsymbol{v} \otimes E_I)
\end{bmatrix}, \quad
\mathcal{S} = \begin{bmatrix}
\boldsymbol{f}_R \\
\boldsymbol{0} \\
\boldsymbol{0} \\
0
\end{bmatrix}, \tag{2}
$$

with the Cartesian material coordinate basis being defined

$$
\boldsymbol{E}_{1}=\left[\begin{array}{l}
1 \\
0 \\
0
\end{array}\right] ; \quad \boldsymbol{E}_{2}=\left[\begin{array}{l}
0 \\
1 \\
0
\end{array}\right] ; \quad \boldsymbol{E}_{3}=\left[\begin{array}{l}
0 \\
0 \\
1
\end{array}\right].
\tag{3}
$$

In terms of notations, $\boldsymbol{p}=\rho_{R} \boldsymbol{v}$ is the linear momentum per unit material volume, $\boldsymbol{v}$ represents the velocity field, $\boldsymbol{f}_{R}$ is the body force per unit material volume, $\{\boldsymbol{F}, \boldsymbol{H}, J\}$ are the triplet deformation measures representing deformation gradient tensor, its co-factor and its Jacobian, $\boldsymbol{P}$ represents the first Piola-Kirchhoff stress tensor. The symbol $\times$ represents the tensor cross product between vectors and/or second order tensors, see References 41,53, and 54.

Given the fact that the above system (1) has more equations than needed, suitable compatibility conditions also known as involutions $^{45,46,55}$ are necessary, namely

$$
\operatorname{CURL} \boldsymbol{F}=\mathbf{0} ; \quad \operatorname{DIV} \boldsymbol{H}=\mathbf{0}.
\tag{4}
$$

CURL and DIV represent the material curl and divergence operators carried out with respect to the material configuration.

For smooth functions, expression (1) is equivalent to the set of first order local differential equations described as

$$
\frac{\partial \mathcal{V}}{\partial t}+\sum_{I=1}^{3} \frac{\partial \mathcal{F}_{I}}{\partial X_{I}}=\mathcal{S} \quad \text { in } \quad \Omega_{V}.
\tag{5}
$$

The above local form implies that the variables describing the state of the solid in motion such as velocity $\boldsymbol{v}$ and stresses $\boldsymbol{P}$ are continuous functions throughout the solid. In other words, it is always possible to find their spatial derivatives as required by the divergence operators that appear in Equation (5). This is indeed usually the case but situations may arise when these variables experience sudden jumps in value, that is, they become discontinuous across surfaces which move across the body. These jumps are known as shocks and are the result of sudden physical phenomena such as contact-impact problems.

To account for shock phenomena, the integral Equation (1) also leads to the following jump conditions across a discontinuity surface with normal $\boldsymbol{N}$ propagating with speed $U$, that is

$$
U\left[\left[\mathcal{V}\right]\right]=\left[\left[\mathcal{F}_{\boldsymbol{N}}\right]\right].
\tag{6}
$$

These jump conditions are sometimes referred to as Rankine-Hugoniot equations $^{56,57}$ describing the behavior of a material across a shock. These conditions can then be particularized for the set of conservation variables considered in this article, namely the linear momentum and the triplet of deformation measures

$$
U\left[\left[\boldsymbol{p}\right]\right]=-\left[\left[\boldsymbol{P}\right]\right] \boldsymbol{N} ;
\tag{7a}
$$

$$
U\left[\left[\boldsymbol{F}\right]\right]=-\left[\left[\boldsymbol{v}\right]\right] \otimes \boldsymbol{N} ;
\tag{7b}
$$

$$
U\left[\left[\boldsymbol{H}\right]\right]=-\boldsymbol{F} \times\left(\left[\left[\boldsymbol{v}\right]\right] \otimes \boldsymbol{N}\right) ;
\tag{7c}
$$

$$
U[[J]]=-\boldsymbol{H}:\left(\left[\left[\boldsymbol{v}\right]\right] \otimes \boldsymbol{N}\right).
\tag{7d}
$$

Here, $[[\bullet]]=[\bullet]^{+}-[\bullet]^{-}$denotes the jump operator between the right and left states of a discontinuous surface.

For the particular case of a reversible process, the closure of system (1) requires the introduction of a suitable constitutive law relating the stress tensor $\boldsymbol{P}$ with the triplet of geometric strain measures $\{\boldsymbol{F}, \boldsymbol{H}, J\}$, obeying the principle of objectivity $^{5,58,59}$ and thermodynamic consistency via the Coleman-Noll procedure $^{60}$. In this work, a Mooney-Rivlin model is employed and is summarized in Remark 2 for completeness. Finally, for a complete definition of the initial boundary value problem, initial and boundary essential and natural conditions must be specified as appropriate.

Remark 1. For the conservation of mass, the material density at the reference configuration cannot be a function of time, that is $\frac{\partial \rho_{R}}{\partial t}=0 .^{61}$ This implies that $\rho_{R}$ is given by the initial conditions of the solids and it remains constant throughout the motion, and does not need to be considered as part of the unknowns in system (1) to be solved in time. Since there is no possible flow of mass across the physical interface meaning, the associated normal flux vector vanishes, the jump

condition associated with the mass conservation becomes $U[\![\rho_R]\!] = 0$. This intrinsically implies that the material density at the reference configuration must be continuous across a shock. Equation (7a) thus reduces to

$$
U \rho_R [\![\boldsymbol{v}]\!] = -[\![\boldsymbol{P}]\!] \boldsymbol{N}. \tag{8}
$$

Remark 2. In this work, and without loss of generality, we consider a Mooney-Rivlin model such that the strain energy density is defined as a convex multi-variable function $W$ of the deformation measures $\{\boldsymbol{F}, \boldsymbol{H}, J\}^{42,62}$ as

$$
W(\boldsymbol{F}, \boldsymbol{H}, J)=\zeta J^{-2 / 3}(\boldsymbol{F}: \boldsymbol{F})+\xi J^{-2}(\boldsymbol{H}: \boldsymbol{H})^{3 / 2}-3\left(\zeta+\sqrt{3 \xi}\right)+\frac{\kappa}{2}(J-1)^2, \tag{9}
$$

where $\zeta$, $\xi$, and $\kappa$ (bulk modulus) are positive material parameters. Appropriate values for the material parameters $\zeta$ and $\xi$ can be defined in terms of the shear modulus $\mu$, that is, $2 \zeta+3 \sqrt{3 \xi}=\mu$. It is now possible to express the first Piola Kirchhoff stress tensor as $^{41}$

$$
\boldsymbol{P}=\boldsymbol{\Sigma}_{\boldsymbol{F}}+\boldsymbol{\Sigma}_{\boldsymbol{H}} \times \boldsymbol{F}+\Sigma_J \boldsymbol{H}, \tag{10}
$$

where the conjugate stresses $\{\boldsymbol{\Sigma}_{\boldsymbol{F}}, \boldsymbol{\Sigma}_{\boldsymbol{H}}, \Sigma_J\}$ are defined by

$$
\boldsymbol{\Sigma}_{\boldsymbol{F}}=\frac{\partial W}{\partial \boldsymbol{F}}=2 \zeta J^{-2 / 3} \boldsymbol{F} ; \quad \boldsymbol{\Sigma}_{\boldsymbol{H}}=\frac{\partial W}{\partial \boldsymbol{H}}=3 \xi J^{-2}(\boldsymbol{H}: \boldsymbol{H})^{1 / 2} \boldsymbol{H}, \tag{11}
$$

and

$$
\Sigma_J=\frac{\partial W}{\partial J}=-\frac{2}{3} \zeta J^{-5 / 3}(\boldsymbol{F}: \boldsymbol{F})-2 \xi J^{-3}(\boldsymbol{H}: \boldsymbol{H})^{3 / 2}+\kappa(J-1). \tag{12}
$$

For $\xi=0$, the Mooney-Rivlin model described above (9) degenerates into the so-called nearly incompressible neo-Hookean model. In order to model irrecoverable plastic behavior, the standard rate-independent von-Mises plasticity model $^{58}$ with isotropic hardening is used and the basic structure was already summarized in Algorithm 1 in Reference 45.

Remark 3. It is often necessary to obtain expressions for the symmetric Kirchhoff (or Cauchy) stress tensor since it is needed either to express plasticity models or to display the solution results. Such expressions can be easily obtained from the following standard relationship between these tensors $^{58}$

$$
J \boldsymbol{\sigma}=\boldsymbol{\tau}=\boldsymbol{P} \boldsymbol{F}^T. \tag{13}
$$

To achieve this, substitution of (10) into (13) for $\boldsymbol{P}$, and following the procedure described in Reference 41, gives the resulting expression for the Kirchhoff (or Cauchy) stress

$$
J \boldsymbol{\sigma}=\boldsymbol{\tau}=\boldsymbol{\tau}_{\boldsymbol{F}}+\boldsymbol{\tau}_{\boldsymbol{H}} \times \boldsymbol{I}+\tau_J \boldsymbol{I}, \tag{14}
$$

where

$$
\boldsymbol{\tau}_{\boldsymbol{F}}=\boldsymbol{\Sigma}_{\boldsymbol{F}} \boldsymbol{F}^T ; \quad \boldsymbol{\tau}_{\boldsymbol{H}}=\boldsymbol{\Sigma}_{\boldsymbol{H}} \boldsymbol{H}^T ; \quad \tau_J=J \Sigma_J. \tag{15}
$$

## 3 | CONTACT-IMPACT CONDITIONS

### 3.1 | Motivation: The local one-dimensional contact solution

In order to motivate the more complex contact-impact solutions (e.g., stick-slip-separation transition) developed in this section, consider first a simple one-dimensional case comprising two bars, as illustrated in Figure 1A, where the left bar is travelling with a given velocity $v_0$ impacts the right bar which is at rest. When the contact between two bars takes place, the resulting contact-impact motion is governed by a reduced set of (one-dimensional) jump conditions described in system (7) as

![](./images/864987781904990352_1.jpg)

FIGURE 1 Wave solution for one-dimensional two-bar impact at different time: (A) $t_0=0$, (B) $t_1=\delta/v_0$, (C) $t_2=t_1+L/(2c_p)$, (D) $t_3=t_1+L/c_p$, (E) $t_4=t_1+3L/(2c_p)$, and (F) $t_5=t_1+2L/c_p$. $\delta$ is the gap separation between two bar at $t_0$. Left column represents the velocity profile $v_x$ and right column represents the stress profile $P_{xX}$ (not the traction).

$$
c_p \rho_R [\![v_x]\!] = -[\![P_{xX}]\!] N_X; \tag{16a}
$$

$$
c_p [\![F_{xX}]\!] = -[\![v_x]\!] N_X. \tag{16b}
$$

For ease of understanding, both bars are assumed to be made of the same linear elastic material defined as $P_{xX}=(\lambda+2\mu)(F_{xX}-1).^{58}$ With this linear model, and noting that $[\![P_{xX}]\!]=(\lambda+2\mu)[\![F_{xX}]\!]$, we can then obtain the shock wave speed $c_p$ by substituting expression (16b) into (16a). Expression (16a) after some algebra becomes

$$
c_p \rho_R [\![v_x]\!] = -(\lambda+2\mu)[\![F_{xX}]\!] N_X = \frac{(\lambda+2\mu)}{c_p} [\![v_x]\!], \tag{17}
$$

and which after rearranging gives†

$$
c_p = \sqrt{\frac{\lambda+2\mu}{\rho_R}}. \tag{18}
$$

This corresponds to the speed of the sound wave in the bar which can be obtained considering the classical wave propagation theory.⁶¹

Once the shock wave speed is determined, attention is now focused on the evaluation of the velocity (kinematic) and traction (kinetic) at the contact-impact scenario. The same evaluation procedure would also be repeated when considering the separation process. When contact is made between two points of the bar, shock waves are generated and travel in opposite directions along each bar (from the contact point to the free end of the bar) as shown in Figure 1A-C. When such a compressive stress wave reaches the end of a bar, wave reflection occurs (see Figure 1D). The reflective wave varies depending on the actual physical boundary of the problem under consideration. In the case of a free end (i.e., traction is zero and particle velocity is doubled), the reflected wave becomes a tensile stress wave which is an inverted

image of the compressive stress wave. The frequency and amplitude of the velocity wave however in this case remains unchanged in reflection. Finally, as soon as the tensile stress wave arrives at the contact point, both bars would undergo the separation process. The above procedure describing the wave evolution for a two-bar impact in one dimension is graphically represented in Figure 1 for clarity.

Let us now focus on the mathematical solutions of contact-impact state between two bars. Upon contact, both instantaneous velocity $v_x^C$ and traction $t_x^C$ are obtained by applying the jump condition (16a) between the values of variables before and after the impact through appropriate initial conditions, to give

$$
\begin{align}
c_p\rho_R\left(v_0 - v_x^C\right) &= 0 - t_x^C; \tag{19a} \\
c_p\rho_R\left(0 - v_x^C\right) &= -\left(0 - t_x^C\right). \tag{19b}
\end{align}
$$

The first equation (19a) corresponds to the jump relation between the left bar (travelling with a given speed $v_x^- = v_0$) and the contact point, whereas the second equation (19b) refers to the jump between the right bar (at rest $v_x^+ = 0$) and the contact point. Additionally, both ends of the bars are traction-free right before contact, which implies that $t_x^- = t_x^+ = 0$. Solving the above system (19) analytically gives the common (or continuous) velocity and traction at the contact point for both bars

$$
v_x^C = \frac{1}{2}v_0; \quad t_x^C = -\left(\frac{c_p\rho_R}{2}\right)v_0. \tag{20}
$$

This is generally known as contact-stick mode in one dimension.

Following the same procedure described above, it is also possible to determine the release velocity for each of the bars right after separation. In this separation mode, the release traction must be zero ensuring the traction-free compatibility condition. Focusing first on the left bar, the release velocity can be achieved by introducing the jump condition (16a) between the values of variables before and after separation to give

$$
c_p\rho_R\left(v_x^- - v_x^{C,-}\right) = t_x^- - 0. \tag{21}
$$

Suitable conditions for velocity and traction right before separation must be enforced. In this specific demonstration, and referring to Figure 1E, we use the values of $v_x^- = t_x^- = 0$ at the contact point prior to separation. With these at hand, the associated release velocity in expression (21) becomes null, shown as below

$$
v_x^{C,-} = v_x^- - \frac{t_x^-}{c_p\rho_R} = 0. \tag{22}
$$

Analogously, we can now repeat the same demonstration for the right bar. The corresponding jump condition in relation to the right bar follows

$$
c_p\rho_R\left(v_x^+ - v_x^{C,+}\right) = -\left(t_x^+ - 0\right). \tag{23}
$$

Using the exact same value of the contact traction as for the left bar (i.e., $t_x^+ = 0$) and the velocity to be $v_x^+ = v_0$, the above expression yields

$$
v_x^{C,+} = v_x^+ + \frac{t_x^+}{c_p\rho_R} = v_0 + 0 = v_0. \tag{24}
$$

Observing the fact that the release velocity for the left bar is null (22) and for the right bar is $v_0$ (24), this represents a complete transfer of kinetic energy (and also total energy) from the left bar to the right bar at the point of contact without energy loss. This is illustrated in Figure 1A,F.

From the point of view of hyperbolic differential equations, the sudden impact between two bars results in a Rie- mann problem in each bar with a simple analytical solution. The boundary fluxes at the point of impact, namely the velocity and traction, must be compatible with the jump conditions. In linear elasticity, this compatibility leads to exact energy balance‡ since the shocks wave travels at the speed of sound. From a mathematical standpoint, the elastodynamic

contact problem is well posed without the need to introduce artificial ad-hoc dissipative effects, provided that the first order conservation equations (1) together with the associated jump conditions (7) are used. The sections that follow will conceptually extend the above simple local contact solution to three dimensional local solution with a possibility to consider bi-material between contact.

### 3.2 | Extension to general contact procedure
It is worthwhile recalling the general solution process for the contact algorithm (for instance, stick-slip-separation tran- sition) that would ensure the satisfaction of Karush-Kuhn-Tucker condition. $^{5,11}$ To begin with, it is instructive to first determine the trial solution assuming contact-stick mode. Such trial solution is used as a criteria in the subsequent development, to check if two bodies are in contact or separate.

The contact between two bodies will only take place if the following two conditions hold

$$
t_{n}^{C, \text { trial }}<0 ; \quad \delta=0.
\tag{25}
$$

The first (kinetic) condition ensures that the normal component of the trial contact traction $t_{n}^{C, \text { trial }}$ must be in compression, whereas the second (kinematic) condition ensures two bodies are in contact, that is the normal separation $\delta$ between points of contact is zero. We next need to examine the nature of the contact motion, whether they are in stick mode or slip mode, depending on the tangential friction introduced in the model. To achieve this, it is possible to introduce a slip criterion $\Phi$ accounting for the difference between the value of a trial tangential traction vector $\boldsymbol{t}_{t}^{C, \text { trial }}$ and a tangential friction arising from isotropic Coulomb friction, $^{5}$ that is

$$
\Phi=\left\|\boldsymbol{t}_{t}^{C, \text { trial }}\right\|-k\left\langle-t_{n}^{C}\right\rangle,
\tag{26}
$$

with the magnitude (or norm) of a vector being defined as $\|[\bullet]\|=\sqrt{([\bullet] \cdot[\bullet])}$. Here, $k$ is the Coulomb friction coefficient and the symbol $\langle\bullet\rangle=\frac{1}{2}([\bullet]+|[\bullet]|)$ in the above equation represents the positive part of the scalar value. The value of the slip criterion determines the transition between contact-stick and contact-slip modes. If $\Phi \leq 0$, contact-stick conditions hold given the fact that the computed tangential force does not exceed the Coulomb limit. Otherwise, when the value of $\Phi>0$, we then accept the solution to be in contact-slip mode.

Finally, the transition from either contact-slip or contact-stick to separation would happen when $t_{n}^{C, \text { trial }} \geq 0$ (that is, the violation of the kinetic condition), even with the value of $\delta=0$. The overall procedure described above is summarized in Algorithm 1. This however would require the evaluation of contact traction and velocity associated with various dynamic contact models involved, and which will be presented in the following sections.

#### 3.2.1 | Contact-stick condition
Motivated by the one-dimensional problem illustrated in Section 3.1, we now extend the concept to multi-dimensions by postulating that impact between two bodies travelling at different speeds leads to a common velocity and traction at the point of contact as shown in Figure 2. The normal components of the velocity and traction at the point of contact are defined as

$$
v_{n}=\boldsymbol{v} \cdot \boldsymbol{n} ; \quad t_{n}=\boldsymbol{t} \cdot \boldsymbol{n}=(\boldsymbol{P} \boldsymbol{N}) \cdot \boldsymbol{n}.
\tag{27}
$$

Both of these values are likely to be different for the left and right bodies right before contact and are therefore denoted as $v_{n}^{-}$ and $t_{n}^{-}$for the left body and $v_{n}^{+}$and $t_{n}^{+}$for the right body. The common values after contact are denoted by $v_{n}^{C}$ and $t_{n}^{C}$. Note first that the impact will generate two types of shock waves travelling from the contact point into each of the two bodies.

In the case of frictionless contact, the generated shock waves will travel with volumetric speed $U_{p}$. The evaluation of the common contact velocity and traction vectors is governed by the jump conditions across the two shocks, obtained by applying Equation (8) on each body as follows

$$
U^{-} \rho_{R}^{-}[[\boldsymbol{v}]]^{-}=-[[\boldsymbol{P}]]^{-}\left(-\boldsymbol{N}^{-}\right) ; \quad U^{+} \rho_{R}^{+}[[\boldsymbol{v}]]^{+}=-[[\boldsymbol{P}]]^{+}\left(-\boldsymbol{N}^{+}\right).
\tag{28}
$$

```
Algorithm 1. General procedure for stick-to-slip-to-separation transition
```
```plaintext
if $\delta = 0$ then
    Obtain trial contact-stick traction: $\boldsymbol{t}^{C,\text{trial}} = \boldsymbol{t}^C$ (34a) (see Section 3.2.1)
    Determine the normal contact traction: $t_n^{C,\text{trial}} = \boldsymbol{n} \cdot \boldsymbol{t}^{C,\text{trial}}$
    if $t_n^{C,\text{trial}} < 0$ then
        Check slip criterion: $\Phi = \|\boldsymbol{t}_t^{C,\text{trial}}\| - k\langle -t_n^C \rangle$
        if $\Phi \leq 0$ then
            Contact-stick mode: $\boldsymbol{t}^C$ (34a) and $\boldsymbol{v}^C$ (34b) (see Section 3.2.1)
        else
            Contact-slip mode: $\boldsymbol{t}^C$ (41) and $\boldsymbol{v}^C$ (40) (see Section 3.2.2)
        end
    else
        Separation mode: $\boldsymbol{v}^C$ (49) and $\boldsymbol{t}^C = \boldsymbol{0}$ (see Section 3.2.3)
    end
else
    Not in contact: $\boldsymbol{v}^C$ (49) and $\boldsymbol{t}^C = \boldsymbol{0}$ (see Section 3.2.3)
end
```

![](./images/864987781904990352_2.jpg)

FIGURE 2 Contact-impact generated shock waves in multi-dimensions.

Note that the negative sign in front of $\boldsymbol{N}^-$ and $\boldsymbol{N}^+$ are necessary as the shocks propagate into the body in directions opposite to $\boldsymbol{N}^-$ and $\boldsymbol{N}^+$. Multiplying the above expressions by a unique normal vector gives

$$
\begin{aligned}
U_{p}^{-} \rho_{R}^{-}\left(v_{n}^{-}-v_{n}^{C}\right) & =t_{n}^{-}-t_{n}^{C} ; & & (29 \mathrm{a}) \\
U_{p}^{+} \rho_{R}^{+}\left(v_{n}^{+}-v_{n}^{C}\right) & =-\left(t_{n}^{+}-t_{n}^{C}\right). & & (29 \mathrm{~b})
\end{aligned}
$$

The difference in sign between expressions (29a) and (29b) is because $\boldsymbol{n}$ is normal to the surface of the left body and hence $t_{n}^{+}=-\boldsymbol{n} \cdot\left(\boldsymbol{P}^{+} \boldsymbol{N}^{+}\right)$and $t_{n}^{C}=-\boldsymbol{n} \cdot \boldsymbol{P}^{C} \boldsymbol{N}^{+}$, whereas $t_{n}^{-}=\boldsymbol{n} \cdot\left(\boldsymbol{P}^{-} \boldsymbol{N}^{-}\right)$and $t_{n}^{C}=\boldsymbol{n} \cdot\left(\boldsymbol{P}^{C} \boldsymbol{N}^{-}\right)$. Expressions (29) represent a system of two equations for four unknowns, namely $t_{n}^{C}$ and $v_{n}^{C}$ (expressed in terms of the left and right normal tractions and velocity before the impact) and also $\{U_{p}^{-}, U_{p}^{+}\}$ the speeds of the shocks after impact. Unfortunately, the shock speeds in Equation (29) are in general also a function of the unknowns $t_{n}^{C}$ and $v_{n}^{C}$ rendering the system of equations highly nonlinear. A much simpler case emerges when the speed of the shock after contact is assumed to be equal to the speed of sound $c_{p}$ (18) (derived on the basis of the linear elastic model), which only depends on the material properties under consideration. This is usually referred to as an acoustic Riemann solver $^{56,57}$ widely known in the field of CFD. Doing this will give closed-form expressions for the normal components of velocity $v_{n}^{C}$ and traction $t_{n}^{C}$ as
```

$$
v_{n}^{C}=\frac{c_{p}^{-} \rho_{R}^{-} v_{n}^{-}+c_{p}^{+} \rho_{R}^{+} v_{n}^{+}}{c_{p}^{-} \rho_{R}^{-}+c_{p}^{+} \rho_{R}^{+}}+\frac{t_{n}^{+}-t_{n}^{-}}{c_{p}^{-} \rho_{R}^{-}+c_{p}^{+} \rho_{R}^{+}} ;
$$

$$
t_{n}^{C}=\frac{c_{p}^{-} \rho_{R}^{-} c_{p}^{+} \rho_{R}^{+}}{c_{p}^{-} \rho_{R}^{-}+c_{p}^{+} \rho_{R}^{+}}\left(\frac{t_{n}^{-}}{c_{p}^{-} \rho_{R}^{-}}+\frac{t_{n}^{+}}{c_{p}^{+} \rho_{R}^{+}}\right)+\frac{c_{p}^{-} \rho_{R}^{-} c_{p}^{+} \rho_{R}^{+}}{c_{p}^{-} \rho_{R}^{-}+c_{p}^{+} \rho_{R}^{+}}\left(v_{n}^{+}-v_{n}^{-}\right). \tag{30}
$$

In the situation where friction is present to a sufficient degree to prevent relative sliding, similar common tangential components of the velocity and traction can be derived. Consequently shear shocks are also generated and are, again, assumed to be identical to the simple shear wave speed obtained via linear elasticity⁴⁵

$$
c_{s}=\sqrt{\frac{\mu}{\rho_{R}}}. \tag{31}
$$

If $\boldsymbol{v}_{t}$ and $\boldsymbol{t}_{t}$ are defined as

$$
\boldsymbol{v}_{t}=\boldsymbol{v}-v_{n} \boldsymbol{n} ; \quad \boldsymbol{t}_{t}=\boldsymbol{t}-t_{n} \boldsymbol{n}, \tag{32}
$$

a similar derivation for the common tangential traction and velocity vectors gives

$$
\boldsymbol{v}_{t}^{C}=\frac{c_{s}^{-} \rho_{R}^{-} \boldsymbol{v}_{t}^{-}+c_{s}^{+} \rho_{R}^{+} \boldsymbol{v}_{t}^{+}}{c_{s}^{-} \rho_{R}^{-}+c_{s}^{+} \rho_{R}^{+}}+\frac{\boldsymbol{t}_{t}^{+}-\boldsymbol{t}_{t}^{-}}{c_{s}^{-} \rho_{R}^{-}+c_{s}^{+} \rho_{R}^{+}} ;
$$

$$
\boldsymbol{t}_{t}^{C}=\frac{c_{s}^{-} c_{s}^{+} \rho_{R}^{-} \rho_{R}^{+}}{c_{s}^{-} \rho_{R}^{-}+c_{s}^{+} \rho_{R}^{+}}\left(\frac{\boldsymbol{t}_{t}^{-}}{c_{s}^{-} \rho_{R}^{-}}+\frac{\boldsymbol{t}_{t}^{+}}{c_{s}^{+} \rho_{R}^{+}}\right)+\frac{c_{s}^{-} c_{s}^{+} \rho_{R}^{-} \rho_{R}^{+}}{c_{s}^{-} \rho_{R}^{-}+c_{s}^{+} \rho_{R}^{+}}\left(\boldsymbol{v}_{t}^{+}-\boldsymbol{v}_{t}^{-}\right), \tag{33}
$$

where $c_{s}^{-}$and $c_{s}^{+}$are the left and right body shear shock speeds.

Finally, the complete common velocity and traction vectors at the contact point can be combined

$$
\boldsymbol{t}^{C}=t_{n}^{C} \boldsymbol{n}+\boldsymbol{t}_{t}^{C} ; \quad \boldsymbol{v}^{C}=v_{n}^{C} \boldsymbol{n}+\boldsymbol{v}_{t}^{C}. \tag{34}
$$

This is typically known as contact-stick mode. Numerically, expressions (34) can be viewed as the summation of the average states (unstable) and the associated upwinding stabilization terms depending on the jumps. This has been exten- sively exploited by the authors in developing stabilized methods with the objective to improve the numerical solutions by alleviating unwanted spurious hour-glassing and pressure instabilities.³⁴,⁴³,⁴⁵,⁴⁷⁻⁴⁹

Provided the interface conditions (25) and also the slip function $\Phi \leq 0$ (26) hold, we accept the contact-stick solution (34) as the actual local solution for contact. Otherwise, we must investigate other possible contact models such as contact-slip or separation. This will be presented in the next section.

Remark 4. It is also useful to consider the case where the jump in traction (or the first Piola Kirchhoff stress $\boldsymbol{P}$ (10)) is dominated by the jump in the pressure component of the stress (which in this case is related to $\Sigma_{J}$ ), whilst the rest of the components of the stress $\left\{\boldsymbol{\Sigma}_{F}, \boldsymbol{\Sigma}_{H}\right\}$ can be neglected. This is indeed the case when attempting to model problems with predominant nearly incompressible behavior. Use of (10) in conjunction with the Nanson's rule $\boldsymbol{H}^{\mathrm{Ave}} \boldsymbol{N}=\Lambda_{H} \boldsymbol{n}$ (where $\Lambda_{H}$ is the ratio between the current area and the undeformed area), enables the jump in the traction vector to be

$$
\begin{aligned}
\boldsymbol{t}^{+}-\boldsymbol{t}^{-}=[\boldsymbol{t}]] & =[\boldsymbol{P}]] \boldsymbol{N}=\left[\boldsymbol{\Sigma}_{F}+\boldsymbol{\Sigma}_{H} \times \boldsymbol{F}+\Sigma_{J} \boldsymbol{H}\right] \boldsymbol{N}, \tag{35a} \\
& \approx\left[\left[\Sigma_{J}\right]\right]\left(\boldsymbol{H}^{\mathrm{Ave}} \boldsymbol{N}\right), \tag{35b} \\
& =\left[\left[\Sigma_{J}\right]\right] \Lambda_{H} \boldsymbol{n}. \tag{35c}
\end{aligned}
$$

Neglecting the stress components $\boldsymbol{\Sigma}_{F}$ and $\boldsymbol{\Sigma}_{H}$ implies that $\left[\left[\boldsymbol{\Sigma}_{F}+\boldsymbol{\Sigma}_{H} \times \boldsymbol{F}\right]\right] \boldsymbol{N}=\boldsymbol{0}$. The jump in the traction vector in the normal direction can now be derived by multiplying (35c) with a normal vector $\boldsymbol{n}$ to yield

$$
t_{n}^{+}-t_{n}^{-}=\boldsymbol{n} \cdot[\boldsymbol{t}]]=\left[\left[\Sigma_{J}\right]\right] \Lambda_{H}. \tag{36}
$$

It is also interesting to notice that the jump in the tangential component of the traction vanishes. This is easily shown as below

$$
\begin{aligned}
\boldsymbol{t}_{t}^{+}-\boldsymbol{t}_{t}^{-} & =\left[\left|\boldsymbol{t}_{t}\right|\right]=\left[\left|\boldsymbol{t}\right|\right]-\left[\left|t_{n}\right|\right] \boldsymbol{n}, & & (37 \mathrm{a}) \\
& =\left[\left|\Sigma_{J}\right|\right] \Lambda_{H} \boldsymbol{n}-\left[\left|\Sigma_{J}\right|\right] \Lambda_{H} \boldsymbol{n}=\mathbf{0}, & & (37 \mathrm{b})
\end{aligned}
$$

by making use of expressions (32b), (36), and (35c).

Remark 5. When considering the exact same material properties on the left and right sides at a point of contact, the density and the shock wave speeds are identical and constant for both sides, namely $\rho_{R}^{-}=\rho_{R}^{+}=\rho_{R}$ and $c_{p}^{-}=c_{p}^{+}=c_{p}$ and $c_{s}^{-}=c_{s}^{+}=c_{s}$. Enforcing these conditions in (30) and (33) especially in the case of nearly incompressible materials (see Remark 4) yields

$$
\begin{array}{ll}
v_{n}^{C}=\frac{1}{2}\left(v_{n}^{-}+v_{n}^{+}\right)+\frac{1}{2 \rho_{R} c_{p}}\left[\left|\Sigma_{J}\right|\right] \Lambda_{H} ; & t_{n}^{C}=\frac{1}{2}\left(t_{n}^{-}+t_{n}^{+}\right)+\frac{\rho_{R} c_{p}}{2}\left(v_{n}^{+}-v_{n}^{-}\right), \\
\boldsymbol{v}_{t}^{C}=\frac{1}{2}\left(\boldsymbol{v}_{t}^{-}+\boldsymbol{v}_{t}^{+}\right) ; & \boldsymbol{t}_{t}^{C}=\frac{1}{2}\left(\boldsymbol{t}_{t}^{-}+\boldsymbol{t}_{t}^{+}\right)+\frac{\rho_{R} c_{s}}{2}\left(\boldsymbol{v}_{t}^{+}-\boldsymbol{v}_{t}^{-}\right).
\end{array}
$$

Remark 6. Consider a contact system where the material on the right side is much stiffer than the material on the left side. Under this circumstance, both pressure and shear shock wave speeds on the stiffer material are approximated to be $c_{p}^{+} \approx \infty$ and $c_{s}^{+} \approx \infty$, which, upon substitution into Equations (30) and (33), gives

$$
v_{n}^{C}=v_{n}^{+} ; \quad \boldsymbol{v}_{t}^{C}=\boldsymbol{v}_{t}^{+} ; \quad t_{n}^{C}=t_{n}^{-}+c_{p}^{-} \rho_{R}^{-}\left(v_{n}^{+}-v_{n}^{-}\right) ; \quad \boldsymbol{t}_{t}^{C}=\boldsymbol{t}_{t}^{-}+c_{s}^{-} \rho_{R}^{-}\left(\boldsymbol{v}_{t}^{+}-\boldsymbol{v}_{t}^{-}\right) .
$$

Observe the fact that only the velocity of the stiffer side, that is $\boldsymbol{v}^{+}$, enters the solutions. These solutions indeed coincide with the Dirichlet boundary conditions already discussed in Reference 45, where the velocity $\boldsymbol{v}^{+}$is prescribed on the boundary of the domain. For instance, when considering no-slip wall boundary condition, the values of $\boldsymbol{v}_{t}^{+}$and $v_{n}^{+}$are set to zero.

### 3.2.2 | Contact-slip conditions

When the magnitude of the tangential traction described in (33) exceeds the Coulomb friction limit, that is $\Phi>0$ (26), relative sliding between two surfaces is then allowed. This phenomenon is known as contact-slip mode. In this mode, only normal component of the velocity is continuous across the contact surface between the left and right bodies. The tangential components of the velocity however may suffer jumps. Mathematically, the complete velocity field associated with slip mode for both the left and right surfaces are postulated as

$$
\boldsymbol{v}^{C,-}=v_{n}^{C} \boldsymbol{n}+\boldsymbol{v}_{t}^{C,-} ; \quad \boldsymbol{v}^{C,+}=v_{n}^{C} \boldsymbol{n}+\boldsymbol{v}_{t}^{C,+},
$$

with $v_{n}^{C}$ being defined in (30a). The remaining variables to be determined are the respective tangential velocity components $\left\{\boldsymbol{v}_{t}^{C,-}, \boldsymbol{v}_{t}^{C,+}\right\}$.

In order to achieve this, it is instructive to consider the slip traction vector to be

$$
\boldsymbol{t}^{C}=t_{n}^{C} \boldsymbol{n}+\boldsymbol{t}_{t}^{B} ; \quad \boldsymbol{t}_{t}^{B}=k\left\langle-t_{n}^{C}\right\rangle \boldsymbol{n}^{\perp} ; \quad \boldsymbol{n}^{\perp}=-\frac{\boldsymbol{t}_{t}^{C}}{\left\|\boldsymbol{t}_{t}^{C}\right\|} .
$$

With regard to the first term on the right hand side of the above equation, the normal component of the contact traction $t_{n}^{C}$ must be in compression (i.e., its value must be strictly negative) and its expression remains exactly the same as the one described in contact-stick mode (30b). The second term $\boldsymbol{t}_{t}^{B}$ represents the tangential frictional traction arising from the Coulomb model of friction and is in the direction $\boldsymbol{n}^{\perp}$ opposing the motion predicted using the tangential traction (33) in stick mode. Use of (41) in conjunction with (28), enables the tangential components of slip velocity vectors to become

$$
c_{s}^{-} \rho_{R}^{-}\left(\boldsymbol{v}_{t}^{-}-\boldsymbol{v}_{t}^{C,-}\right)=\boldsymbol{t}_{t}^{-}-\boldsymbol{t}_{t}^{B} ; \quad c_{s}^{+} \rho_{R}^{+}\left(\boldsymbol{v}_{t}^{+}-\boldsymbol{v}_{t}^{C,+}\right)=-\left(\boldsymbol{t}_{t}^{+}-\boldsymbol{t}_{t}^{B}\right) .
$$

Re-arranging the above expressions render

$$
\boldsymbol{v}_{t}^{C,-}=\boldsymbol{v}_{t}^{-}+\frac{\left(\boldsymbol{t}_{t}^{B}-\boldsymbol{t}_{t}^{-}\right)}{c_{s}^{-} \rho_{R}^{-}} ; \quad \boldsymbol{v}_{t}^{C,+}=\boldsymbol{v}_{t}^{+}-\frac{\left(\boldsymbol{t}_{t}^{B}-\boldsymbol{t}_{t}^{+}\right)}{c_{s}^{+} \rho_{R}^{+}} .
$$

It is useful to notice that frictionless contact condition (also known as symmetric condition) can be easily recovered by enforcing the value of frictional coefficient $k=0$ in (41), which in turn implies that $\boldsymbol{t}_{t}^{B}=\mathbf{0}$.

### 3.2.3 | Separation conditions
In the current work, we assume homogeneous prescribed traction (that is, traction-free conditions) in separation mode, but non-vanishing prescribed tractions due to viscous fluid loading are also possible. This reveals the fact that the traction after separation must ensure traction-free compatibility conditions, namely

$$
\boldsymbol{t}^{C,-}=\boldsymbol{t}^{C,+}=\mathbf{0}. \tag{44}
$$

With this, we are now in a position to proceed with the evaluation of release (or post-separation) velocity on respective surfaces by re-applying Equation (8) between the values of variables before and after separation, repeated below again for convenience

$$
U^{-} \rho_{R}^{-} [\![\boldsymbol{v}]\!]^{-}=-[\![\boldsymbol{P}]\!]^{-}\left(-\boldsymbol{N}^{-}\right) ; \quad U^{+} \rho_{R}^{+} [\![\boldsymbol{v}]\!]^{+}=-[\![\boldsymbol{P}]\!]^{+}\left(-\boldsymbol{N}^{+}\right). \tag{45}
$$

The normal components of the release velocities are obtained by multiplying expressions above with the normal vector $\boldsymbol{n}$

$$
c_{p}^{-} \rho_{R}^{-}\left(v_{n}^{-}-v_{n}^{C,-}\right)=t_{n}^{-}-0 ; \quad c_{p}^{+} \rho_{R}^{+}\left(v_{n}^{+}-v_{n}^{C,+}\right)=-\left(t_{n}^{+}-0\right), \tag{46}
$$

and which, after rearranging, becomes

$$
v_{n}^{C,-}=v_{n}^{-}-\frac{t_{n}^{-}}{c_{p}^{-} \rho_{R}^{-}} ; \quad v_{n}^{C,+}=v_{n}^{+}+\frac{t_{n}^{+}}{c_{p}^{+} \rho_{R}^{+}}. \tag{47}
$$

In line with linear elasticity theory, above expressions coincide with the expressions shown in (22) and (24). A similar derivation for the tangential velocity vectors can now follow

$$
\boldsymbol{v}_{t}^{C,-}=\boldsymbol{v}_{t}^{-}-\frac{\boldsymbol{t}_{t}^{-}}{c_{s}^{-} \rho_{R}^{-}} ; \quad \boldsymbol{v}_{t}^{C,+}=\boldsymbol{v}_{t}^{+}+\frac{\boldsymbol{t}_{t}^{+}}{c_{s}^{+} \rho_{R}^{+}}. \tag{48}
$$

Combining (47) and (48) enables the release velocities to be expressed as

$$
\boldsymbol{v}^{C,-}=v_{n}^{C,-} \boldsymbol{n}+\boldsymbol{v}_{t}^{C,-} ; \quad \boldsymbol{v}^{C,+}=v_{n}^{C,+} \boldsymbol{n}+\boldsymbol{v}_{t}^{C,+}. \tag{49}
$$

It is worth noticing that all the velocity components described in (49) are generally distinct and independent on opposing sides of the contact surface.

## 4 | SECOND LAW OF THERMODYNAMICS
In order to pave the way for the proof of entropy production presented in a subsequent section, it is useful to introduce the notion of Hamiltonian $\mathcal{H}(\boldsymbol{X}, t) .^{61,63}$ For the isothermal case, this indeed can be understood as a generalized convex entropy function of the system of conservation equations (1), coinciding with the definition of total energy per unit of undeformed volume. Specifically, the Hamiltonian $\mathcal{H}$ is defined by

$$
\mathcal{H}(\boldsymbol{X}, t)=\hat{H}(\boldsymbol{p}, \boldsymbol{F}, \boldsymbol{H}, J, \boldsymbol{\alpha})=\frac{1}{2 \rho_{R}} \boldsymbol{p} \cdot \boldsymbol{p}+\mathcal{E}(\boldsymbol{F}, \boldsymbol{H}, J, \boldsymbol{\alpha}), \tag{50}
$$

which represents the summation of the kinetic energy per unit of undeformed volume (i.e., the first term on the right hand side of (50)) and the internal energy $\mathcal{E}$ expressed in terms of the triplet deformation measures $\{\boldsymbol{F}, \boldsymbol{H}, J\}$ and a set of

state variables⁶⁴⁻⁶⁶ (such as plastic deformation or similar) collected in the form of a tensor $\boldsymbol{\alpha}$. Note here that $\mathcal{H}(\boldsymbol{X}, t)$ and $\hat{\mathcal{H}}(\boldsymbol{p}, \boldsymbol{F}, \boldsymbol{H}, \boldsymbol{J}, \boldsymbol{\alpha})$ represent alternative functional representations of the same quantity.

It is instructive to revisit the second law of thermodynamics when written in terms of the Hamiltonian. Taking the derivatives of $\hat{\mathcal{H}}$ (50) with respect to its arguments, the time rate of the Hamiltonian for one of the bodies involving contact is obtained via the chain rule as follows

$$
\begin{aligned}
\frac{d}{d t} \int_{\Omega_{V}} \mathcal{H} d \Omega_{V} &=\int_{\Omega_{V}} \frac{\partial \hat{\mathcal{H}}(\boldsymbol{p}, \boldsymbol{F}, \boldsymbol{H}, J, \boldsymbol{\alpha})}{\partial t} d \Omega_{V} \\
&=\int_{\Omega_{V}}\left(\frac{\partial \hat{\mathcal{H}}}{\partial \boldsymbol{p}} \cdot \frac{\partial \boldsymbol{p}}{\partial t}+\frac{\partial \hat{\mathcal{H}}}{\partial \boldsymbol{F}}: \frac{\partial \boldsymbol{F}}{\partial t}+\frac{\partial \hat{\mathcal{H}}}{\partial \boldsymbol{H}}: \frac{\partial \boldsymbol{H}}{\partial t}+\frac{\partial \hat{\mathcal{H}}}{\partial J} \frac{\partial J}{\partial t}+\frac{\partial \hat{\mathcal{H}}}{\partial \boldsymbol{\alpha}}: \frac{\partial \boldsymbol{\alpha}}{\partial t}\right) d \Omega_{V} \\
&=\int_{\Omega_{V}}\left(\boldsymbol{v} \cdot \frac{\partial \boldsymbol{p}}{\partial t}+\boldsymbol{\Sigma}_{\boldsymbol{F}}: \frac{\partial \boldsymbol{F}}{\partial t}+\boldsymbol{\Sigma}_{\boldsymbol{H}}: \frac{\partial \boldsymbol{H}}{\partial t}+\boldsymbol{\Sigma}_{J} \frac{\partial J}{\partial t}+\frac{\partial \mathcal{E}}{\partial \boldsymbol{\alpha}}: \frac{\partial \boldsymbol{\alpha}}{\partial t}\right) d \Omega_{V} \\
&=\int_{\Omega_{V}}\left(\boldsymbol{v} \cdot \frac{\partial \boldsymbol{p}}{\partial t}+\left(\boldsymbol{\Sigma}_{\boldsymbol{F}}+\boldsymbol{\Sigma}_{\boldsymbol{H}} \times \boldsymbol{F}+\boldsymbol{\Sigma}_{J} \boldsymbol{H}\right): \boldsymbol{\nabla}_{0} \boldsymbol{v}+\frac{\partial \mathcal{E}}{\partial \boldsymbol{\alpha}}: \frac{\partial \boldsymbol{\alpha}}{\partial t}\right) d \Omega_{V} \\
&=\int_{\Omega_{V}}\left(\boldsymbol{v} \cdot \frac{\partial \boldsymbol{p}}{\partial t}+\boldsymbol{P}: \boldsymbol{\nabla}_{0} \boldsymbol{v}+\frac{\partial \mathcal{E}}{\partial \boldsymbol{\alpha}}: \frac{\partial \boldsymbol{\alpha}}{\partial t}\right) d \Omega_{V},
\end{aligned}
\tag{51}
$$

where, Equations (5) and (10) have been substituted in the third and fifth lines of (51), respectively. Subsequently, we can substitute the linear momentum conservation Equation (1) into (51) to give

$$
\frac{d}{d t} \int_{\Omega_{V}} \mathcal{H} d \Omega_{V}=\int_{\Omega_{V}}\left[\boldsymbol{v} \cdot \boldsymbol{f}_{R}+\boldsymbol{v} \cdot \operatorname{DIV} \boldsymbol{P}+\boldsymbol{P}: \boldsymbol{\nabla}_{0} \boldsymbol{v}+\frac{\partial \mathcal{E}}{\partial \boldsymbol{\alpha}}: \frac{\partial \boldsymbol{\alpha}}{\partial t}\right] d \Omega_{V}.
\tag{52}
$$

Recalling that $\boldsymbol{v} \cdot \operatorname{DIV} \boldsymbol{P}+\boldsymbol{P}: \boldsymbol{\nabla}_{0} \boldsymbol{v}=\operatorname{DIV}\left(\boldsymbol{P}^{T} \boldsymbol{v}\right)$, above equation reduces to

$$
\frac{d}{d t} \int_{\Omega_{V}} \mathcal{H} d \Omega_{V}=\int_{\Omega_{V}}\left[\boldsymbol{v} \cdot \boldsymbol{f}_{R}+\operatorname{DIV}\left(\boldsymbol{P}^{T} \boldsymbol{v}\right)+\frac{\partial \mathcal{E}}{\partial \boldsymbol{\alpha}}: \frac{\partial \boldsymbol{\alpha}}{\partial t}\right] d \Omega_{V}.
\tag{53}
$$

By performing integration by parts of the DIV term in expression (53), and after some re-arrangement, it renders

$$
\frac{d}{d t} \int_{\Omega_{V}} \mathcal{H} d \Omega_{V}-\dot{\Pi}_{\mathrm{ext}}=-\dot{D},
\tag{54}
$$

where $\dot{\Pi}_{\text {ext }}$ denotes the power introduced by external forces, defined as

$$
\dot{\Pi}_{\mathrm{ext}}=\int_{\Omega_{V}} \boldsymbol{v} \cdot \boldsymbol{f}_{R} d \Omega_{V}+\int_{\partial \Omega_{V} \setminus \Gamma} \boldsymbol{v}^{B} \cdot \boldsymbol{t}^{B} d A+\int_{\Gamma} \boldsymbol{v}^{C} \cdot \boldsymbol{t}^{C} d A.
\tag{55}
$$

Here, $\Gamma$ represents the boundary faces on contact region and $\partial \Omega_{V} \setminus \Gamma$ represents the remaining boundary faces that are not in contact. In the above expression, the first term on the right hand side represents external force acting on a body, the second term represents the non-contact boundary forces obtained via the enforcement of standard Neumann or Dirichlet boundary conditions, and the third term represents the contact boundary forces describing appropriately the contact-impact phenomenon. Such contact boundary contributions are suitably enforced by solving a Riemann-like problem as already presented in Section 3.

Consider the case of elasto-plasticity⁴⁷,⁵²,⁵⁸ where the elastic energy is expressed in terms of elastic left Cauchy-Green tensor $\boldsymbol{b}_{e}=\boldsymbol{F} \boldsymbol{C}_{p}^{-1} \boldsymbol{F}^{T}$, thus in this case the internal state variable is indeed the inverse of the plastic right Cauchy Green tensor, that is $\boldsymbol{\alpha}=\boldsymbol{C}_{p}^{-1}$. With this, the rate of plastic dissipation $\dot{D}$ described in (54) becomes

$$
\dot{D}=-\int_{\Omega_{V}} \frac{\partial \mathcal{E}}{\partial \boldsymbol{C}_{p}^{-1}}: \frac{\partial \boldsymbol{C}_{p}^{-1}}{\partial t} d \Omega_{V}.
\tag{56}
$$

In view of the fact that the rate of plastic strain $\dot{\bar{\varepsilon}}_{p}$ has been defined as the work conjugate to the von Mises equivalent stress $\bar{\tau},{ }^{58}$ equation above can be alternatively expressed as⁵⁸

$$
\dot{D}=\int_{\Omega_{V}} \dot{\bar{\varepsilon}}_{p} \bar{\tau} d \Omega_{V} ; \quad \bar{\tau}=\sqrt{\frac{3}{2}\left(\boldsymbol{\tau}^{\prime}: \boldsymbol{\tau}^{\prime}\right)},
\tag{57}
$$

where $\boldsymbol{\tau}^{\prime}$ represents the deviatoric component of the Kirchhoff stress. Noticing that in the above expression the rate of dissipation is always non-negative, that is $\dot{D} \geq 0$, Equation (54) can be transformed into the following inequality

$$
\frac{d}{d t} \int_{\Omega_{V}} \mathcal{H} d \Omega_{V}-\dot{\Pi}_{\mathrm{ext}} \leq 0,
\tag{58}
$$

which represents a valid expression for the second law of thermodynamics. $^{59}$ Satisfaction of inequality (58) is a necessary $a b$ initio condition to ensure stability, otherwise referred to as the Coleman-Noll procedure. $^{34}$ This key concept will be further exploited in Section 5.2 at a semi-discrete level.

## 5 | VERTEX CENTERED FINITE VOLUME METHOD

### 5.1 | Semi-discrete formulation for dynamic contact

The vertex centered finite volume spatial discretization presented in this work requires the generation of a median dual mesh $^{34,35,50}$ for the definition of control volumes (see Figure 3). With this in mind, expression (1) can now be spatially discretized over an undeformed control volume $\Omega_{V}^{a}$, to give

$$
\Omega_{V}^{a} \frac{d \mathcal{V}_{a}}{d t}=-\int_{\partial \Omega_{V}^{a}} \mathcal{F}_{\boldsymbol{N}} d A+\Omega_{V}^{a} \mathcal{S}_{a}.
\tag{59}
$$

Here, $\mathcal{V}_{a}$ and $\mathcal{S}_{a}$ are the average values of both the conservation variables and source term vector within the control volume, respectively.

Moreover, the surface integral of (59) is approximated by means of appropriate numerical fluxes, resulting in $^{\S}$

$$
\Omega_{V}^{a} \frac{d \mathcal{V}_{a}}{d t}=-\left(\sum_{b \in \Lambda_{a}} \mathcal{F}_{N_{a b}}^{I}\left\|\boldsymbol{C}_{a b}\right\|+\sum_{\gamma \in \Lambda_{a}^{B}} \mathcal{F}_{a}^{B} \boldsymbol{C}_{\gamma}+\sum_{\beta \in \Lambda_{a}^{C}} \mathcal{F}_{a}^{C} \boldsymbol{C}_{\beta}\right)+\Omega_{V}^{a} \mathcal{S}_{a},
\tag{61}
$$

where $b \in \Lambda_{a}$ represents the set of neighboring control volumes $b$ associated with the control volume $a$ and $\boldsymbol{C}_{\gamma, \beta}=\frac{A_{\gamma, \beta}}{3} \boldsymbol{N}_{\gamma, \beta}$ represents the (tributary) boundary area vector. For a given edge connecting nodes $a$ and $b$, the mean undeformed area

![](./images/864987781904990352_3.jpg)

FIGURE 3 Dual mesh of (A) an interior node and (B) a boundary node using the medial dual approach in two dimensional triangular mesh.

vector $\boldsymbol{C}_{a b}$ satisfies the reciprocal relation, that is $\boldsymbol{C}_{a b}=-\boldsymbol{C}_{b a}$. The terms within the parenthesis in (61) correspond to the evaluation of the control volume internal interface flux $\boldsymbol{F}_{\boldsymbol{N}_{a b}}^{I}$, non-contact boundary fluxes $\boldsymbol{F}_{a}^{B}$ and contact boundary fluxes $\boldsymbol{F}_{a}^{C}$. This evaluation is comprised of a summation over edges (first term in the parenthesis), a summation over non-contact boundary faces (second term in the parenthesis) and a summation over contact boundary faces (third term in the parenthesis). The internal interface flux $\boldsymbol{F}_{\boldsymbol{N}_{a b}}^{I}=\boldsymbol{F}_{\boldsymbol{N}_{a b}}^{I}\left(\mathcal{U}_{a b}^{-}, \mathcal{U}_{a b}^{+}, \boldsymbol{N}_{a b}\right)$ must be evaluated on the basis of the contact-stick condition (see Section 3.2.1), which depends on the reconstructed states at both sides of the mid-edge of $a b$, namely $\mathcal{U}_{a b}^{-}$and $\mathcal{U}_{a b}^{+}$. The non-contact boundary flux $\boldsymbol{F}_{a}^{B}$ is enforced through either Neumann or Dirichlet boundaries and the contact flux $\boldsymbol{F}_{a}^{C}$ is determined following strictly the contact procedure presented in Algorithm 1 (obeying appropriate contact-impact physics). Notice that in (61), $\boldsymbol{C}_{\beta}=\mathbf{0}$ when the boundary face $\beta$ is not in contact.

It is worth noticing that Equation (61) would only lead to a first order solution in space $^{45}$ provided that $\mathcal{U}_{a b}^{-}$and $\mathcal{U}_{a b}^{+}$are modeled following a piecewise constant representation. For instance, $\mathcal{U}_{a b}^{-}=\mathcal{U}_{a}$ and $\mathcal{U}_{a b}^{+}=\mathcal{U}_{b}$, thus leading to excessive numerical dissipation in the solution. The physics of the problem can no longer be captured accurately unless excessively fine meshes are used, which is clearly undesirable especially for large scale problems in practice. To overcome this drawback, and to guarantee second order accuracy in space, a suitable linear reconstruction procedure is used. A detailed discussion of this reconstruction procedure has already been presented in References 45,48, and 47.

Expression (61) is now particularized for each individual component of $\mathcal{U}$, yielding

$$
\Omega_{V}^{a} \frac{d \boldsymbol{p}_{a}}{d t}=\sum_{b \in \Lambda_{a}} \boldsymbol{t}^{I}|| \boldsymbol{C}_{a b}||+\sum_{\gamma \in \Lambda_{a}^{B}} \boldsymbol{t}_{a}^{B}|| \boldsymbol{C}_{\gamma}||+\sum_{\beta \in \Lambda_{a}^{C}} \boldsymbol{t}_{a}^{C}|| \boldsymbol{C}_{\beta}||+\Omega_{V}^{a} \boldsymbol{f}_{R}^{a} ;\qquad(62a)
$$

$$
\Omega_{V}^{a} \frac{d \boldsymbol{F}_{a}}{d t}=\sum_{b \in \Lambda_{a}} \boldsymbol{v}^{I} \otimes \boldsymbol{C}_{a b}+\sum_{\gamma \in \Lambda_{a}^{B}} \boldsymbol{v}_{a}^{B} \otimes \boldsymbol{C}_{\gamma}+\sum_{\beta \in \Lambda_{a}^{C}} \boldsymbol{v}_{a}^{C} \otimes \boldsymbol{C}_{\beta} ;\qquad(62b)
$$

$$
\Omega_{V}^{a} \frac{d \boldsymbol{H}_{a}}{d t}=\sum_{b \in \Lambda_{a}} \boldsymbol{F}^{\text {Ave }} \times\left(\boldsymbol{v}^{I} \otimes \boldsymbol{C}_{a b}\right)+\sum_{\gamma \in \Lambda_{a}^{B}} \boldsymbol{F}_{a} \times\left(\boldsymbol{v}_{a}^{B} \otimes \boldsymbol{C}_{\gamma}\right)+\sum_{\beta \in \Lambda_{a}^{C}} \boldsymbol{F}_{a} \times\left(\boldsymbol{v}_{a}^{C} \otimes \boldsymbol{C}_{\beta}\right) ;\qquad(62c)
$$

$$
\Omega_{V}^{a} \frac{d J_{a}}{d t}=\sum_{b \in \Lambda_{a}} \boldsymbol{v}^{I} \cdot\left(\boldsymbol{H}^{\mathrm{Ave}} \boldsymbol{C}_{a b}\right)+\sum_{\gamma \in \Lambda_{a}^{B}} \boldsymbol{v}_{a}^{B} \cdot\left(\boldsymbol{H}_{a} \boldsymbol{C}_{\gamma}\right)+\sum_{\beta \in \Lambda_{a}^{C}} \boldsymbol{v}_{a}^{C} \cdot\left(\boldsymbol{H}_{a} \boldsymbol{C}_{\beta}\right).\qquad(62d)
$$

Here, $[\bullet]^{\text {Ave }}=\frac{1}{2}\left([\bullet]_{a}+[\bullet]_{b}\right)$. It is worth re-emphasizing that the determination of internal fluxes $\left\{\boldsymbol{t}^{I}, \boldsymbol{v}^{I}\right\}$ is based on contact-stick mode (refer to Equations (30), (33), and (34)) and the non-contact boundary fluxes $\left\{\boldsymbol{t}_{a}^{B}, \boldsymbol{v}_{a}^{B}\right\}$ are evaluated respecting the physical boundaries (i.e., Neumann or Dirichlet). On the other hand, the evaluation of contact boundary fluxes $\left\{\boldsymbol{v}_{a}^{C}, \boldsymbol{t}_{a}^{C}\right\}$ must satisfy the Karush-Kuhn-Tucker condition for stick-slip-separation transition. The reader can refer to Equations {(34), (30), (33)} for contact-stick mode, Equations {(40), (41), (43)} for contact-slip mode, and Equations {(44), (49), (47), (48)} for separation mode.

In ensuring discrete satisfaction of the involutions (4), and following the work of Reference 34, one viable option is to approximate the updates of $\boldsymbol{F}(62 \mathrm{~b})$ and $\boldsymbol{H}(62 \mathrm{c})$ using central difference approximations by neglecting the jump in traction in (30) and (33) (or jump in $\Sigma_{J}(38 \mathrm{a})$ ) for $\boldsymbol{v}^{I}$ in (62b) and (62c). Additionally, in order to ensure the triplet deformation measures to be solved in a consistent manner, the average strain variables $\boldsymbol{F}^{\text {Ave }}$ and $\boldsymbol{H}^{\text {Ave }}$ appearing in expressions (62c) and (62d) will be replaced by $\boldsymbol{F}_{a}$ and $\boldsymbol{H}_{a}$. With this, and assuming the jump in traction is dominated by jump in pressure (see Remark 4), the geometric conservation Equations (62b)-(62d) reduce to

$$
\Omega_{V}^{a} \frac{d \boldsymbol{F}_{a}}{d t}=\sum_{b \in \Lambda_{a}} \boldsymbol{v}^{\mathrm{WAvg}} \otimes \boldsymbol{C}_{a b}+\sum_{\gamma \in \Lambda_{a}^{B}} \boldsymbol{v}_{a}^{B} \otimes \boldsymbol{C}_{\gamma}+\sum_{\beta \in \Lambda_{a}^{C}} \boldsymbol{v}_{a}^{C} \otimes \boldsymbol{C}_{\beta} ;\qquad(63a)
$$

$$
\Omega_{V}^{a} \frac{d \boldsymbol{H}_{a}}{d t}=\boldsymbol{F}_{a} \times\left(\sum_{b \in \Lambda_{a}} \boldsymbol{v}^{\mathrm{WAvg}} \otimes \boldsymbol{C}_{a b}+\sum_{\gamma \in \Lambda_{a}^{B}} \boldsymbol{v}_{a}^{B} \otimes \boldsymbol{C}_{\gamma}+\sum_{\beta \in \Lambda_{a}^{C}} \boldsymbol{v}_{a}^{C} \otimes \boldsymbol{C}_{\beta}\right) ;\qquad(63b)
$$

$$
\Omega_{V}^{a} \frac{d J_{a}}{d t}=\boldsymbol{H}_{a}:\left(\sum_{b \in \Lambda_{a}} \boldsymbol{v}^{\mathrm{WAvg}} \otimes \boldsymbol{C}_{a b}+\sum_{\gamma \in \Lambda_{a}^{B}} \boldsymbol{v}_{a}^{B} \otimes \boldsymbol{C}_{\gamma}+\sum_{\beta \in \Lambda_{a}^{C}} \boldsymbol{v}_{a}^{C} \otimes \boldsymbol{C}_{\beta}\right)+\sum_{b \in \Lambda_{a}} S_{a b}^{\Sigma_{J}}\left(\Sigma_{J}^{+}-\Sigma_{J}^{-}\right).\qquad(63c)
$$

Here, the strictly positive parameter $S_{a b}^{\Sigma_{J}}$ and the weighted average velocity field are defined as

$$
S_{a b}^{\Sigma_{J}}=\frac{1}{2 \rho_{R} c_{p}} \frac{\boldsymbol{c}_{a b} \cdot \boldsymbol{c}_{a b}}{\left\|\boldsymbol{C}_{a b}\right\|} ; \quad \boldsymbol{v}^{\mathrm{WAvg}}=v_{n}^{\mathrm{WAvg}} \boldsymbol{n}+\boldsymbol{v}_{t}^{\mathrm{WAvg}},\qquad(64)
$$

with their components being described as

$$
\begin{aligned}
v_{n}^{\mathrm{WAvg}} &=\frac{c_{p}^{-} \rho_{R}^{-} v_{n}^{-}+c_{p}^{+} \rho_{R}^{+} v_{n}^{+}}{c_{p}^{-} \rho_{R}^{-}+c_{p}^{+} \rho_{R}^{+}} ; & \boldsymbol{v}_{t}^{\mathrm{WAvg}} &=\frac{c_{s}^{-} \rho_{R}^{-} \boldsymbol{v}_{t}^{-}+c_{s}^{+} \rho_{R}^{+} \boldsymbol{v}_{t}^{+}}{c_{s}^{-} \rho_{R}^{-}+c_{s}^{+} \rho_{R}^{+}} ; & \boldsymbol{c}_{a b} &=\boldsymbol{H}^{\mathrm{Ave}} \boldsymbol{C}_{a b}.
\end{aligned} \tag{65}
$$

It is important to emphasize that strong compatibility between the different kinematic fields $\{\boldsymbol{F},\boldsymbol{H},J\}$ is lost at the semi-discrete level. However, weak compatibility is maintained due to the coupled nature of the semi-discrete system of conservation equations.

For visualization purposes, the current deformed geometry is recovered by integrating in time the discrete nodal velocity field obtained using (62a)

$$
\frac{d \boldsymbol{x}_{a}}{d t}=\boldsymbol{v}_{a}. \tag{66}
$$

With respect to the time integration of the above system (62a), (63a)-(63c) along with the geometry $\boldsymbol{x}$ (66), and keeping in mind a fast and efficient algorithm, we advocate for an explicit one-step two-stage total variation diminishing Runge-Kutta (TVD-RK) method, thoroughly reported by the authors in Reference 48 and references therein.

### 5.2 | Entropy production

In this section, inequality (58) is assessed for the above set of semi-discrete equations (62a), (63a), (63b), (63c). For illustrative purposes, the body under consideration is said to be homogeneous. Additionally, and in line with the Godunov's theorem, $^{56,57}$ we assume piecewise constant approximation (first order in space) for variables across each control volume. Making use of expression (57), the semi-discrete counterpart of (51) is

$$
\begin{aligned}
\sum_{a} \Omega_{V}^{a} \frac{d \mathcal{H}_{a}}{d t} &=\sum_{a} \Omega_{V}^{a}\left[\boldsymbol{v}_{a} \cdot \frac{d \boldsymbol{p}_{a}}{d t}+\boldsymbol{\Sigma}_{F}^{a}: \frac{d \boldsymbol{F}_{a}}{d t}+\boldsymbol{\Sigma}_{H}^{a}: \frac{d \boldsymbol{H}_{a}}{d t}+\Sigma_{J}^{a} \frac{d J_{a}}{d t}-\dot{D}_{a}\right], \tag{67a} \\
&=\sum_{a} \Omega_{V}^{a}\left[\boldsymbol{v}_{a} \cdot \frac{d \boldsymbol{p}_{a}}{d t}+\left(\boldsymbol{\Sigma}_{F}^{a}+\boldsymbol{\Sigma}_{H}^{a} \times \boldsymbol{F}_{a}+\Sigma_{J}^{a} \boldsymbol{H}_{a}\right): \frac{d \boldsymbol{F}_{a}}{d t}-\dot{D}_{a}\right]+\sum_{a} \sum_{b \in \Lambda_{a}} \Sigma_{J}^{a} S_{a b}^{\Sigma_{J}}\left(\Sigma_{J}^{b}-\Sigma_{J}^{a}\right), \tag{67b} \\
&=\sum_{a} \Omega_{V}^{a}\left[\boldsymbol{v}_{a} \cdot \frac{d \boldsymbol{p}_{a}}{d t}+\boldsymbol{P}_{a}: \frac{d \boldsymbol{F}_{a}}{d t}\right]+\sum_{a} \sum_{b \in \Lambda_{a}} \Sigma_{J}^{a} S_{a b}^{\Sigma_{J}}\left(\Sigma_{J}^{b}-\Sigma_{J}^{a}\right)-\sum_{a} \Omega_{V}^{a} \dot{D}_{a}, \tag{67c}
\end{aligned}
$$

where, Equations (63a)-(63c) and (10) have been substituted in the second and third lines of (67), respectively. Subsequently, we can substitute the linear momentum conservation Equation (62a), the deformation gradient conservation Equation (63a) and, after some algebra, gives

$$
\begin{aligned}
\sum_{a} \Omega_{V}^{a} \frac{d \mathcal{H}_{a}}{d t} &=\sum_{a} \sum_{b \in \Lambda_{a}} \frac{1}{2}\left[\boldsymbol{t}_{a} \cdot \boldsymbol{v}_{b}-\boldsymbol{t}_{b} \cdot \boldsymbol{v}_{a}\right]\left\|\boldsymbol{C}_{a b}\right\|, \tag{68a} \\
&+\sum_{a} \sum_{b \in \Lambda_{a}} \boldsymbol{v}_{a} \cdot \boldsymbol{S}_{a b}^{\boldsymbol{v}}\left(\boldsymbol{v}_{b}-\boldsymbol{v}_{a}\right)+\sum_{a} \sum_{b \in \Lambda_{a}} \Sigma_{J}^{a} S_{a b}^{\Sigma_{J}}\left(\Sigma_{J}^{b}-\Sigma_{J}^{a}\right)-\sum_{a} \Omega_{V}^{a} \dot{D}_{a}+\dot{\Pi}_{\mathrm{ext}}. \tag{68b}
\end{aligned}
$$

Here, $\dot{\Pi}_{\text {ext }}$ denotes the semi-discrete power contribution, expressed as

$$
\dot{\Pi}_{\mathrm{ext}}=\sum_{a} \Omega_{V}^{a} \boldsymbol{v}_{a} \cdot \boldsymbol{f}_{R}^{a}+\sum_{\gamma} A_{R}^{\gamma} \boldsymbol{t}_{a}^{B} \cdot \boldsymbol{v}_{a}^{B}+\sum_{\beta} A_{R}^{\beta} \boldsymbol{t}_{a}^{C} \cdot \boldsymbol{v}_{a}^{C}, \tag{69}
$$

and the positive definite matrices are

$$
\boldsymbol{S}_{a b}^{\boldsymbol{v}}=\frac{\rho_{R} c_{p}}{2}(\boldsymbol{n} \otimes \boldsymbol{n})+\frac{\rho_{R} c_{s}}{2}(\boldsymbol{I}-\boldsymbol{n} \otimes \boldsymbol{n}). \tag{70}
$$

Noticing that the nested summation is carried out over control volumes in (68) and the anti-symmetric nature of the first line of the right hand side, we can conclude that these terms cancel and thus (68) reduces to

$$
\begin{aligned}
\sum_{a} \Omega_{V}^{a} \frac{d \mathcal{H}_{a}}{d t}-\dot{\Pi}_{\mathrm{ext}} &=\sum_{a} \sum_{b \in \Lambda_{a}} \boldsymbol{v}_{a} \cdot\left(\boldsymbol{S}_{a b}^{\boldsymbol{v}}\left(\boldsymbol{v}_{b}-\boldsymbol{v}_{a}\right)\right)+\sum_{a} \sum_{b \in \Lambda_{a}} \Sigma_{J}^{a} S_{a b}^{\Sigma_{J}}\left(\Sigma_{J}^{b}-\Sigma_{J}^{a}\right)-\sum_{a} \Omega_{V}^{a} \dot{D}_{a}, \label{eq71a}\\[5pt]
&=\sum_{a} \sum_{b \in \Lambda_{a}} \boldsymbol{v}_{b} \cdot\left(\boldsymbol{S}_{b a}^{\boldsymbol{v}}\left(\boldsymbol{v}_{a}-\boldsymbol{v}_{b}\right)\right)+\sum_{a} \sum_{b \in \Lambda_{a}} \Sigma_{J}^{b} S_{b a}^{\Sigma_{J}}\left(\Sigma_{J}^{a}-\Sigma_{J}^{b}\right)-\sum_{a} \Omega_{V}^{a} \dot{D}_{a}. \label{eq71b}
\end{aligned}
$$

It is worth pointing out that the first two terms on the right hand side can be equivalently written by swapping indices $a$ and $b$. Simple averaging the first line and the second line of the equation above, and noticing that $\boldsymbol{S}_{a b}^{\boldsymbol{v}}=\boldsymbol{S}_{b a}^{\boldsymbol{v}}$ and $S_{a b}^{\Sigma_{J}}=S_{b a}^{\Sigma_{J}}$, an alternative expression is

$$
\sum_{a} \Omega_{V}^{a} \frac{d \mathcal{H}_{a}}{d t}-\dot{\Pi}_{\mathrm{ext}}=-\left[\frac{1}{2} \sum_{a} \sum_{b \in \Lambda_{a}}\left(\left(\boldsymbol{v}_{b}-\boldsymbol{v}_{a}\right) \cdot \boldsymbol{S}_{a b}^{\boldsymbol{v}}\left(\boldsymbol{v}_{b}-\boldsymbol{v}_{a}\right)+S_{a b}^{\Sigma_{J}}\left(\Sigma_{J}^{b}-\Sigma_{J}^{a}\right)^{2}\right)+\sum_{a} \Omega_{V}^{a} \dot{\bar{\varepsilon}}_{p}^{a} \bar{\tau}_{a}\right]. \tag{72}
$$

Indeed, the first two terms in the square bracket of (72) are always non-negative. Moreover, in the case of elasto-plasticity, the third term representing the rate of plastic dissipation is also non-negative.

## 6 | ALGORITHMIC DESCRIPTION

For ease of understanding, Algorithm 2 summarizes the complete algorithmic description of the proposed finite volume methodology for large strain contact dynamics. This algorithm is implemented in modern CFD code "OpenFOAM," with an eye on large scale contact simulation in future works.

```plaintext
Algorithm 2. Vertex centered finite volume algorithm for contact dynamics

(1) Initialize median dual mesh and solid dynamic variables for all bodies, i
(2) Initialize contact pairs
    - Identify contact pairs and initialize contact variables
    - Compute face area projection weights (see Remark 7)
while t < tend do
    (3) Calculate allowable time step:   Δt
    (4) Store all conserved variables:   Ua,i^old = Ua,i^n
    for Runge-Kutta stage = 1 to 2 do
        (5) Update contact pairs through two-way mapping (see Algorithm 3)
        forall bodies do
            (6) Apply linear reconstruction for interior fluxes (refer to Section 3.3 in Reference 35)
            (7) Compute numerical fluxes via Riemann solver:
                - Interior fluxes as contact-stick (see Section 3.2.1): F_Nab^I(U_ab^-, U_ab^+, N_ab)
                - Boundary fluxes (see Section 4.2 in Reference 45):   Fa^B
                - Contact fluxes (see Algorithm 1):   Fa^C
            (8) Update conservation variables:   Ua = Ua + ΔtU̇a
            (9) Compute first Piola-Kirchhoff stress (see Remark 2): Pa
        end
    end
    (10) Update conservation variables:   Ua,i^(n+1) = 1/2 (Ua,i + Ua,i^old)
    (11) Compute first Piola-Kirchhoff stress (see Remark 2): Pa,i
end
```

![](./images/864987781904990352_4.jpg)

**FIGURE 4** Two-dimensional vertex based mapping algorithm to project $\{\boldsymbol{t}_a, \boldsymbol{v}_a\}$ from “−” surface to “+” surface.

Remark 7. Numerical simulations of contact problems often involve modeling the interaction of multiple bodies across a non-conforming (or non-matching) interface mesh. In order to address these scenarios, a pre-existing OpenFOAM library was employed by the proposed method. This OpenFOAM library, known as Arbitrary Mesh Interface (AMI), is based on the conservative local Galerkin projection procedure presented by Farrell and Maddison in Reference 68. By harnessing this library a projection weighting is calculated based on the overlapping face area of the two contact surfaces in the reference configuration. Since this AMI procedure is based on a surface to surface projection, additional piece- wise surface-to-vertex reconstruction algorithm is then required. For illustrative purposes, Algorithm 3 summarizes the non-conforming mapping procedure in two dimensions, projecting variables from the “−” contact surface to the “+” contact surface. Its graphical representation is also depicted in Figure 4.

---
**Algorithm 3.** The non-conforming mapping procedure in two dimensions
---
(1) Obtain averaged variables at face centroid $f$: $\{\boldsymbol{t}_f^-, \boldsymbol{v}_f^-\} \leftarrow \{\boldsymbol{t}_a^-, \boldsymbol{v}_a^-\}$

(2) Map face variables from “−” to “+” surface using AMI face area projection weighting $\{\boldsymbol{t}_f^{\text{Map}}, \boldsymbol{v}_f^{\text{Map}}\}$

(3) Reconstruct face nodal variables $\{\boldsymbol{t}_{af}^{\text{Map}}, \boldsymbol{v}_{af}^{\text{Map}}\}$ via piecewise linear reconstruction
---

## 7 | NUMERICAL EXAMPLES

In this section, a wide variety of numerical examples are presented in order to assess the robustness, applicability, and performance of the proposed formulation presented above. In the following sections, it is important to demonstrate the overall algorithm

- ensures consistency and accuracy of the field variables at the contact interface for both conforming and non-conforming interface meshes,
- guarantees long term stability by satisfying the discrete version of the second law of thermodynamics (72), and
- circumvents hour-glassing and pressure instabilities even in the case of nearly incompressible material and elasto-plasticity.

In the following numerical computations, we consider only the frictionless contact where the value of friction coefficient $k$ in (41) is set to zero. We also assume that for simplicity the contact points between potential contact- ing interfaces are known a priori. In terms of the temporal stability of the algorithm, the Courant-Friedrichs-Lewy number of $\alpha_{\text{CFL}} = 0.3$ has been chosen. In addition, comparisons are also carried out against the results simu- lated using the commercial software package Abaqus.⁶⁹ From the spatial discretization standpoint, the standard lin- ear finite element method (triangular element in two dimension and tetrahedral element in three dimension) and mean dilatation approach (quadrilateral element in two dimension and hexahedral element in three dimension) are employed, in conjunction with a set of built-in artificial viscosity parameters in order to dissipate high frequency oscillations.

![](./images/864987781904990352_5.jpg)

FIGURE 5 Two-bar impact: Geometry and problem setup. The bar on the left is named as bar 1 and the bar on the right is named as bar 2.

<table>
<caption>TABLE 1 Two-bar impact: Material parameters used in the simulation for bars 1 and 2.</caption>
<thead>
<tr>
<th>Young's modulus</th>
<th>E</th>
<th>100</th>
<th>N m⁻²</th>
</tr>
</thead>
<tbody>
<tr>
<td>Material density</td>
<td>$\rho_R$</td>
<td>0.01</td>
<td>kg m⁻³</td>
</tr>
<tr>
<td>Poisson's ratio</td>
<td>ν</td>
<td>0.0</td>
<td></td>
</tr>
<tr>
<td>Shock wave speed</td>
<td>$c_p$</td>
<td>100</td>
<td>m s⁻¹</td>
</tr>
</tbody>
</table>

### 7.1 | Objective 1: Consistency and accuracy

#### 7.1.1 | One-dimensional two-bar impact for similar bars

The first example corresponds to the impact of two bars having equal length with an initial gap of $\delta = 0.01$ m, as shown in Figure 5. Bar 1 (on the left), is travelling with a given velocity $v_0^1 = 0.1$ m/s towards bar 2 (on the right) which is at rest. Material properties for both bars are exactly the same and are summarized in Table 1. The main objective of this classical benchmarked problem is to examine the robustness and reliability of the proposed algorithm in capturing contact mode transition. As reported in literature, $^{6,70-75}$ most of the methods still exhibit severe non-physical oscillations in the velocity resolution throughout the duration of contact and also post separation. Specific ad-hoc regularization procedure is generally required to limit these numerical artefacts.

In this example, a linear elastic model is considered and four different levels of mesh refinements are used. For instance, {Mesh I, Mesh II, Mesh III, Mesh IV} comprise {128, 256, 512, 1024} number of elements, respectively. Both bars make first contact at time $t_{\text{impact}} = \delta / v_0^1 = 0.1$ s. Such impact generates shock waves of speed $c_p = \sqrt{\frac{E}{\rho_R}} = 100$ m/s, and they travel in opposite directions along each bar and reflect back to the contact point at time $t = t_{\text{impact}} + 2L / c_p = 0.3$ s.

First, we demonstrate the proposed algorithm is capable of satisfying the second law of thermodynamics, and hence ensuring long-term stability. Figure 6A shows the time history of global total energy of the two bars. Its resolution after the contact at time $t = 0.1$ s is better represented by refining the mesh. Another interesting variable of interest is the accumulated numerical entropy (dissipation) present in the algorithm. This is achieved by integrating the Hamiltonian energy of the system described in (72) over time$^\#$, which decreases over time for the entire simulation. This is seen in Figure 6B. The total numerical dissipation is reduced when successively increasing the mesh density. In addition, Figure 6C,D illustrate the time histories of different forms of energy for bar 1 and bar 2, respectively. These include kinetic energy $K^{\text{total}} = \int_{\Omega_V} \frac{1}{2\rho_R} \boldsymbol{p} \cdot \boldsymbol{p} \, d\Omega_V$, elastic strain energy $\psi^{\text{total}} = \int_{\Omega_V} \mathcal{E} \, d\Omega_V$, and the total energy being defined as the summation of kinetic energy and elastic strain energy. At time $t = 0$, bar 1 (travelling at a given velocity $v_0^1$) has the total energy fully dominated by kinetic energy, whereas bar 2 has zero total energy (no movement and stress-free) since it is at rest. When impact takes place at time $t = 0.1$ s, some of the total energy of bar 1 is transferred into kinetic energy of bar 2 (both bars travel together whilst in contact) and some into elastic strain energy of bar 2 (as both bar elastically deform during the period of contact). The elastic strain energy of the bars peak at time $t = 0.2$ s due to the fact that the compressive stress wave arrives at the free end of the bars. The stress wave is then reflected back from the free end (now the stress wave becomes tensile stress wave) into the contact point which result in separation at time $t = 0.3$ s. After separation, as expected, nearly all total energy is transferred from bar 1 to bar 2, with only approximately 0.4 % of the total energy (via **Mesh IV**) dissipated numerically due to the use of a Riemann-based algorithm (refer to the first two terms on the right hand side of (72)).

Second, we highlight the importance of incorporating a slope limiter into the proposed algorithm in order to improve the resolution of field variables in the vicinity of shocks. Figure 7 shows the time histories of velocity and stress for bar 1.

![](./images/864987781904990352_6.jpg)

FIGURE 6 Two-bar impact: Time evolution of (A) global total energy, (B) global numerical dissipation, (C) different energy measures for bar 1 (via Mesh IV), and (D) different energy measures for bar 2 (via Mesh IV). A neo-Hookean constitutive model as described in (9) is used. Their corresponding material parameters are summarized in Table 1.

The exact (analytical) solution is also provided for verification purposes. As it can be observed, using piecewise constant representation (first order accurate in space) for field interpolation, the solutions are fairly dissipative over time for both velocity $v_x$ and axial stress $\sigma_{xx}$ unless excessively fine mesh is used. To enhance the accuracy, we introduce a piecewise linear reconstruction. Such enhancement, as seen in Figure 7B, gives much better resolution in stress but fails prior to separation, where non-physical oscillations are generated. In order to control these spurious modes, the classical Barth and Jespersen limiter⁵⁷ is implemented. A great improvement is observed in Figure 7B. As compared to the classical finite element method, no post-separation velocity oscillations are observed in the proposed algorithm.

Finally, for qualitative comparison purposes, we monitor the velocity $v_x$, displacement $u_x$ and stress $\sigma_{xx}$ evolutions at two locations, namely point A in bar 1 and point B in bar 2. Our results are in very good agreement with the given exact solutions (see Figure 8), without showing undershoots/overshoots near a discontinuity.

### 7.1.2 | One-dimensional two-bar impact for dissimilar bars

We next analyze the same impact problem but now considering a softer material (bar 1) impacts against a stiffer material (bar 2). This is achieved by reducing the value of Young's modulus $E$ of bar 1 from 100 to $49\ \text{N/m}^2$. The remaining

![](./images/864987781904990352_7.jpg)

![](./images/864987781904990352_8.jpg)

**FIGURE 7** Two-bar impact: Time evolution of (A) velocity $v_x$ and (B) stress $\sigma_{xx}$ monitored at point A in bar 1. Point A refers to position $X=10$ m. A neo-Hookean constitutive model as described in (9) is used. Their corresponding material parameters are summarized in Table 1.

material properties for bars 1 and 2 are exactly the same as those reported in Section 7.1.1, and are summarized again in Table 2 for completeness. The purpose of this test case is to examine the applicability of the algorithm in addressing impact between two different materials. Figure 9 illustrates the time evolutions of velocity $v_x$, displacement $u_x$ and stress $\sigma_{xx}$ monitored at points A and B. The proposed algorithm can accurately capture the solutions during impact process and release process, displaying extremely good agreement with the closed-form solutions. No specific ad-hoc regularization procedure is required.

### 7.2 | Objective 2: Spurious mechanism

#### 7.2.1 | Two dimensional compressible ring collision

As previously explored in References 76 and 77, the main aim of this classical benchmark problem is to examine the capability of the proposed algorithm in alleviating unwanted spurious modes that may potentially arise in the contact (or shock) interface. The problem consists of simulating the collision of two rubber rings, with an initial gap of 8 mm, coming together at a relative speed of 1.18 m/s. The geometry of the problem is displayed in Figure 10. In this example, a neo-Hookean model presented in (9) is considered. The values of all the relevant material parameters used can be found in Table 3.

Aiming to show mesh convergence, four successively refined meshes (see Figure 11) are used. These include (Mesh I) 2480, (Mesh II) 10,080, (Mesh III) 81,280, and (Mesh IV) 163,200 number of linear triangular elements for each ring. In order to ensure the algorithm correctly reproduces the second law of thermodynamics, the global entropy and total energy are monitored (see Figure 12A,B). Indeed, for all four meshes, both the global entropy and total energy of the system decrease over time, whereby the irreversibility is caused by numerical stabilizations introduced into the algorithm (which is precisely the square bracket term of (72)). Before contact takes place, the total energy of the system is completely dominated by kinetic energy. When time $t>6.8$ ms, that is after collision takes place, the kinetic energy of the system decreases and transforms into elastic strain energy. Additionally, a very small amount of the kinetic energy also converts to monotonic decreasing numerical dissipation during a deformation process. This is seen in Figure 12C,D.

For comparison purposes, we also simulate the same problem discretized using the standard linear finite element method (using 163,840 number of linear triangular meshes with 82,944 nodes) and the mean dilatation approach (using

![](./images/864987781904990352_9.jpg)

FIGURE 8 Two-bar impact: Time evolution of (first row) velocity $v_x$, (second row) stress $\sigma_{xx}$, and (third row) displacement $u_x$. Results in the first column are monitored at point A in bar 1 and results in the second column are monitored at point B in bar 2. Point A refers to position $X = 10$ m and point B refers to $X = 10.01$ m. Comparison is carried out between the proposed algorithm (via **Mesh IV**) and the exact solutions for similar bars. A neo-Hookean constitutive model as described in (9) is used. Their corresponding material parameters are summarized in Table 1.

<table>
<caption>TABLE 2 Two-bar impact: Material parameters used in the simulation.</caption>
<thead>
<tr>
<th></th>
<th></th>
<th>Bar 1</th>
<th>Bar 2</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Young's modulus</td>
<td>$E$</td>
<td>49</td>
<td>100</td>
<td>$\text{N m}^{-2}$</td>
</tr>
<tr>
<td>Material density</td>
<td>$\rho_R$</td>
<td>0.01</td>
<td>0.01</td>
<td>$\text{kg m}^{-3}$</td>
</tr>
<tr>
<td>Poisson's ratio</td>
<td>$v$</td>
<td>0.0</td>
<td>0.0</td>
<td></td>
</tr>
<tr>
<td>Shock wave speed</td>
<td>$c_p$</td>
<td>70</td>
<td>100</td>
<td>$\text{m s}^{-1}$</td>
</tr>
</tbody>
</table>

81,920 number of bilinear quadrilateral meshes with 82,944 nodes). Figure 13 illustrates the deformation process of the two rings at time $t = \{10, 20, 30, 40\}$ ms, displaying how the two rings collide, bounce off and then oscillate. No spurious modes are observed. In comparison to the mean dilatation technique, very similar results in terms of deformed shape and pressure field are observed. For completeness, the time evolutions of the components of velocity $v_x$, displacement $u_x$ and stress $\sigma_{xx}$ are also monitored. As shown in Figure 14, the obtained solutions converge to the results of mean dilatation technique by refining the mesh. In comparison to the standard linear finite element method, the proposed algorithm clearly outperforms it by accurately capturing stress discontinuities (in this case, $\sigma_{xx}$) without any spurious oscillations. This is seen in Figure 15C,D.

### 7.2.2 Two dimensional nearly incompressible bar impact

Similar to the objectives described in Section 7.2.1, another standard benchmark problem previously adopted in Reference 47 is considered. As shown in Figure 16, the example presents the impact of two nearly incompressible rectangular bars travelling at each other with a relative velocity of $\boldsymbol{v}_0 = [100, 0]^T \text{m/s}$. For each bar, its width is of $w = 6.4$ mm and its length is of $L = 32.4$ mm. The normal separation between two bars is 8 mm. A neo-Hookean model is used. The values of all the simulation parameters are summarized in Table 4. For completeness, we discretize the problem using four different levels of mesh refinement, including (Mesh I) 640, (Mesh II) 2560, (Mesh III) 10,240, and (Mesh IV) 40,960 number of linear triangular elements per bar.

First, a mesh refinement study for the proposed algorithm is carried out. In Figure 17, the deformation pattern of the structure predicted using a small number of elements (Mesh I) agrees well with the results obtained using finer discretizations (Mesh II–Mesh IV). As for the latter, improved pressure resolution is observed. For qualitative comparison purposes, time evolution of velocity $v_x$ and displacement $u_x$ are monitored and compared in Figure 18. Interestingly, double contact occurs between 80 and $100$ $\mu\text{s}$. It is well-known that pressure checker-boarding is commonly encountered in standard linear finite elements when attempting to model materials with predominant nearly incompressible behavior. This numerical artefact can be completely resolved by the algorithm proposed in the current paper, without resorting to any ad-hoc regularization procedure. Comparing with mean dilatation technique (see Figure 19), smoother version in pressure profile is observed. Figure 20 shows the time evolution of the deformation behavior of two bars come into contact. Again, very smooth pressure profile is seen throughout the entire contact-impact process. Neither hour-glassing nor pressure checker-boarding are observed.

## 7.3 Objective 3: Non-matching contact interface

We now extend the above two dimensional bar impact problem to three dimension as displayed in Figure 21. This example serves the purpose to examine the accuracy and reliability of the proposed algorithm when considering non-matching meshes at the contact interface. A neo-Hookean model is chosen and the corresponding material properties remain exactly the same as the one listed in Table 4.

Aiming to show mesh independent convergence for this problem, we begin this example by performing a series of non-conforming mesh refinement analysis. The (bulk) mesh information for the two bodies are presented in Table 5 and their respective non-matching interface meshes are depicted in Figure 22. As shown in Figures 23 and 24, it is remarkable that the deformation pattern together with pressure profile converge even with the use of a

![](./images/864987781904990352_10.jpg)

![](./images/864987781904990352_11.jpg)

![](./images/864987781904990352_12.jpg)

![](./images/864987781904990352_13.jpg)

![](./images/864987781904990352_14.jpg)

![](./images/864987781904990352_15.jpg)

FIGURE 9 Two-bar impact: Time evolution of (first row) velocity $v_x$, (second row) stress $\sigma_{xx}$, and (third row) displacement $u_x$. Results in the first column are monitored at point A in bar 1 and results in the second column are monitored at point B in bar 2. Point A refers to position $X = 10$ m and point B refers to $X = 10.01$ m. Comparison is carried out between the proposed algorithm (via **Mesh IV**) and the exact solutions for dissimilar bars. A neo-Hookean model as described in (9) is used. Their corresponding material parameters are summarized in Table 1.

![](./images/864987781904990352_16.jpg)

FIGURE 10 Collision of rubber ring: Geometry and problem setup. The rubber ring on the left is named as ring 1 and the rubber ring on the right is named as ring 2.

<table>
<thead>
  <tr>
    <th>Young's modulus</th>
    <th>E</th>
    <th>$1×10^{6}$</th>
    <th>$Nm^{-2}$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Material density</td>
    <td>$\rho_{R}$</td>
    <td>1000</td>
    <td>$kgm^{-3}$</td>
  </tr>
  <tr>
    <td>Poisson's ratio</td>
    <td>$\nu$</td>
    <td>0.4</td>
    <td></td>
  </tr>
  <tr>
    <td>Lamé parameters</td>
    <td>$\mu$</td>
    <td>0.35714</td>
    <td>$MNm^{-2}$</td>
  </tr>
  <tr>
    <td></td>
    <td>$\lambda$</td>
    <td>1.42857</td>
    <td>$MNm^{-2}$</td>
  </tr>
</tbody>
</table>

TABLE 3 Collision of rubber ring: Material parameters used in the simulation for rings 1 and 2.

![](./images/864987781904990352_17.jpg)

FIGURE 11 Each ring domain is discretized with (A) Mesh I (2480 linear triangle with 1364 nodes), (B) Mesh II (10,080 linear triangle with 5292 nodes), (C) Mesh III (81,280 linear triangle with 20,828 nodes), and (D) Mesh IV (163,200 linear triangle with 82,620 nodes). To avoid repetition of image, only one rubber ring per discretization is shown above.

relatively coarse mesh (Mesh I). Additionally, in Figure 25, we also monitor the time history of velocity component $v_x$, displacement component $u_x$, stress component $\sigma_{xx}$ and pressure at the contact point $\boldsymbol{X}=[32.8,3.2,3.2]^T$ mm. Their corresponding spatial distributions at time $t=260$ $\mu$s between positions $\boldsymbol{X}=[32.8,1.6,1.6]^T$ mm and $\boldsymbol{X}=[65.2,1.6,1.6]^T$ mm are illustrated in Figure 26. The solutions indeed converge with a progressive level of mesh refinement. In order for the overall algorithm to ensure long term stability, the global entropy is monitored (see Figure 27). As expected, the global total entropy of the system decreases over time throughout the entire simulation duration. Observe that our solution is slightly more dissipative than that of the mean dilatation technique via tri-linear hexahedral elements (see Figure 28). No spurious modes are seen comparing with the linear tetrahedral finite element method.

![](./images/864987781904990352_18.jpg)

FIGURE 12 Collision of rubber ring: Time evolution of (A) global total energy, (B) global numerical dissipation, (C) different energy measures for ring 1 (via Mesh IV), and (D) different energy measures for ring 2 (via Mesh IV). A neo-Hookean constitutive model as described in (9) is used. Their corresponding material parameters are summarized in Table 3.

## 7.4 | Objective 4: Highly nonlinear impact

In the last example, we consider the rebound of a torus of outer radius $R_o = 40$ mm, inner radius $r_i = 30$ mm and diameter $d_0 = 1$ mm. The torus impacts against a rigid frictionless wall with an initial velocity of $\boldsymbol{v}_0 = [1.18, 0, 0]^T$ m/s where the separation distance between the torus and the wall is of $\delta = 4$ mm. This is illustrated in Figure 29. A neo-Hookean model is first chosen with the material properties summarized in the third column of Table 6.

Aiming to demonstrate the consistency of the algorithm, the domain is discretized using four different levels of refinement, namely (Mesh I) 4643, (Mesh II) 12,439, (Mesh III) 29,748, and (Mesh IV) 56,955 number of unstructured linear tetrahedral meshes. Figure 30B shows the reduction of total numerical dissipation when successively increasing the mesh density. More crucially, the global (numerical) entropy is non-positive and reduces over time for the entire simulation. In Figure 30D, the evolution in time of the kinetic energy, elastic strain energy, and total

![](./images/864987781904990352_19.jpg)

FIGURE 13 Collision of rubber ring: Comparison of deformed shapes at time $t = \{10, 20, 30, 40\}$ ms (from top to bottom) using (A) proposed algorithm (linear triangular mesh) with Mesh IV and (B) mean dilatation technique (bilinear quadrilateral mesh). The color contour plot indicates pressure field. A neo-Hookean model as described in (9) is used. Their corresponding material parameters are summarized in Table 3.

![](./images/864987781904990352_20.jpg)

FIGURE 14 Collision of rubber ring: Time evolution of (A) component of velocity $v_x$ and (B) component of stress $\sigma_{xx}$ at point A in ring 1. Point A refers to position $\boldsymbol{X} = [40, 0]^T$ mm. A comparison is carried out between the proposed algorithm with four different meshes and the mean dilatation approach. A neo-Hookean model as described in (9) is used. Their corresponding material parameters are summarized in Table 3.

![](./images/864987781904990352_21.jpg)

FIGURE 15 Collision of rubber ring: Time evolution of (first row) velocity $v_x$, (second row) stress $\sigma_{xx}$, and (third row) displacement $u_x$. Results in the first column are monitored at point A in ring 1 and results in the second column are monitored at point B in ring 2. Point A refers to position $\boldsymbol{X} = [40,0]^T$ mm and point B refers to $\boldsymbol{X} = [48,0]^T$ mm. Comparison is carried out between the proposed algorithm (via Mesh IV), the linear triangular finite element method and the mean dilatation approach. A neo-Hookean model described in (9) is used. Their corresponding material parameters are summarized in Table 3.

![](./images/864987781904990352_22.jpg)

FIGURE 16 Nearly incompressible bar impact: Geometry and problem setup. The bar on the left is named as bar 1 and the bar on the right is named as bar 2.

<table><caption>TABLE 4 Nearly incompressible bar impact: Material parameters used in the simulation for bars 1 and 2.</caption>
<tbody>
<tr>
<td>Young's modulus</td>
<td>E</td>
<td>$5.85 \times 10^8$</td>
<td>$\text{N m}^{-2}$</td>
</tr>
<tr>
<td>Material density</td>
<td>$\rho_R$</td>
<td>8930</td>
<td>$\text{kg m}^{-3}$</td>
</tr>
<tr>
<td>Poisson's ratio</td>
<td>$\nu$</td>
<td>0.495</td>
<td></td>
</tr>
<tr>
<td>Lamé parameters</td>
<td>$\mu$</td>
<td>0.19565</td>
<td>$\text{GN m}^{-2}$</td>
</tr>
<tr>
<td></td>
<td>$\lambda$</td>
<td>19.3696</td>
<td>$\text{GN m}^{-2}$</td>
</tr>
</tbody>
</table>

![](./images/864987781904990352_23.jpg)

FIGURE 17 Nearly incompressible bar impact: Comparison of bar impact at time $t = 90\ \mu\text{s}$ using various mesh refinements. In each subfigure, the first row depicts the current deformed state discretized with linear triangular mesh and the second row illustrates pressure contour. A neo-Hookean model described in (9) is used. Their corresponding material parameters are summarized in Table 4. (A) Mesh I: 640 number of linear triangles with 369 number of nodes per bar; (B) Mesh II: 2560 number of linear triangles with 1377 number of nodes per bar; (C) Mesh III: 10,240 number of linear triangles with 5313 number of nodes per bar; (D) Mesh IV: 40,960 number of linear triangles with 20,865 number of nodes per bar.

![](./images/864987781904990352_24.jpg)

![](./images/864987781904990352_25.jpg)

![](./images/864987781904990352_26.jpg)

![](./images/864987781904990352_27.jpg)

FIGURE 18 Nearly incompressible bar impact: Time evolution of (first row) velocity $v_x$ and (second row) displacement $u_x$. Results in the first column are monitored at position $\boldsymbol{X} = [32.4, 0]^T$ mm in bar 1 and results in the second column are monitored at position $\boldsymbol{X} = [40.4, 0]^T$ mm in bar 2. Comparison is carried out between the proposed algorithm with **Mesh IV**, the linear triangular finite element method (40,960 number of linear triangles with 20,865 number of nodes per bar) and the mean dilatation technique (20,480 number of bilinear quadrilaterals with 20,865 number of nodes per bar). A neo-Hookean model described in (9) is used and the material parameters are summarized in Table 4.

![](./images/864987781904990352_28.jpg)

FIGURE 19 Nearly incompressible bar impact: Comparison of deformed shapes at time $t = 100$ μs using (A) proposed algorithm with Mesh IV (40,960 number of linear triangles with 20,865 number of nodes per bar), (B) linear triangle finite element method (40,960 number of linear triangles with 20,865 number of nodes per bar), and (C) mean dilatation technique (20,480 number of bilinear quadrilaterals with 20,865 number of nodes per bar). The color contour plot indicates pressure field. A neo-Hookean model described in (9) is used. Their corresponding material parameters are summarized in Table 4.

![](./images/864987781904990352_29.jpg)

FIGURE 20 Nearly incompressible bar impact: A sequence of deformed structures with pressure resolution at times $t = \{50, 75,100, 125,150, 200,250, 300,325\}$ μs (from top to bottom). Results obtained via Mesh IV. A neo-Hookean model is used and the corresponding material parameters are summarized in Table 4.

![](./images/864987781904990352_30.jpg)

FIGURE 21 Impact with non-matching interface mesh: Geometry and problem setup. The bar on the left is named as bar 1 and the bar on the right is named as bar 2. Both bars have width W and height H of 3.2 mm with a length L of 32.4 mm. The initial gap $\delta$ between two bars is 0.4 mm.

<table>
<caption>TABLE 5 Impact with non-matching interface mesh: The number of linear tetrahedra for bars 1 and 2.</caption>
<thead>
<tr>
<th></th>
<th>Bar 1 (elements; nodes)</th>
<th>Bar 2 (elements; nodes)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Mesh I</td>
<td>30,000; 6171</td>
<td>1920; 525</td>
</tr>
<tr>
<td>Mesh II</td>
<td>30,000; 6171</td>
<td>6480; 1519</td>
</tr>
<tr>
<td>Mesh III</td>
<td>30,000; 6171</td>
<td>15,360; 3321</td>
</tr>
<tr>
<td>Mesh IV</td>
<td>30,000; 6171</td>
<td>51,840; 10,309</td>
</tr>
</tbody>
</table>

energy (being the summation of both kinetic and elastic strain energy) are monitored. At the start of the simulation, the total energy of the system is completely dominated by kinetic energy as the torus is moving with the initial velocity until approximately 3.4 ms where impact occurs. In the elastic case, the kinetic energy is mostly transferred into elastic strain energy. When time is approximately 30 ms, that is when the separation begins to occur, the elastic strain energy is then converted back to kinetic energy as the torus bounces off the rigid surface. Comparing with the standard linear finite element method (101,045 number of linear tetrahedra and 20,427 number of nodes), the proposed algorithm can be used without experiencing any spurious mechanism (see Figure 31). By making use of the proposed method, a series of deformed states are shown in Figure 32, where the color contour plot indicates the pressure distribution.

Moreover, the same problem is further analyzed by employing a Hencky-based von Mises plasticity (with isotropic hardening) model. Its associated materials properties are summarized in the fourth column of Table 6. When the torus impacts against a frictionless wall, the total kinetic energy is partially converted into elastic strain energy whilst most of the kinetic energy in this case is transferred into irrecoverable plastic energy dissipation. Indeed, the amount of physical plastic dissipation introduced into this model can then be monitored by integrating in time the term related to the internal dissipation $\dot{D}$ appearing in the Hamiltonian energy of the system described in (72). Again, as seen in Figures 33 and 34, the proposed algorithm can effectively alleviate non-physical pressure instabilities. Our solutions match well with the results obtained via mean dilatation technique (which is discretized with 29,441 number of tri-linear hexahedra and 33,793 number of nodes). For visualization purposes, Figure 35 shows the time evolution of the plastic deformation of a torus with very smooth pressure field.

![](./images/864987781904990352_31.jpg)

FIGURE 22 Impact with non-matching interface mesh: For ease of explication, we choose to display a series of non-conforming mesh refinements on X-Y plane view. In (A), the first four rows represent the non-conforming mesh discretizations for both bars (Mesh I to Mesh IV). Their respective close-up view of the interface between two bodies can be seen in the first four columns of (B). For completeness, we also discretize the problem using conforming mesh. This is illustrated in the last row of (A) and its associated close-up view is displayed in the last column of (B).

![](./images/864987781904990352_32.jpg)

FIGURE 23 Impact with non-matching interface mesh: Comparison of three-dimensional bar impact at time $t = 120\ \mu\text{s}$ using (A) non-conforming mesh discretizations (Mesh I-Mesh IV, from first row to fourth row) and (B) conforming mesh discretization (fifth row). Color contour plot indicates the pressure profile. A neo-Hookean model (9) is used. Their corresponding material parameters are summarized in Table 4.

![](./images/864987781904990352_33.jpg)

FIGURE 24 Impact with non-matching interface mesh: Comparison of three-dimensional bar impact at time $t = 260\ \mu\text{s}$ using (A) non-conforming mesh discretizations (**Mesh I–Mesh IV**, from first row to fourth row) and (B) conforming mesh discretization (fifth row). Color contour plot indicates the pressure profile. A neo-Hookean model (9) is used. Their corresponding material parameters are summarized in Table 4.

![](./images/864987781904990352_34.jpg)

FIGURE 25 Impact with non-matching interface mesh: Time evolution of (A) velocity component $v_x$, (B) displacement component $u_x$, (C) stress component $\sigma_{xx}$, and (D) pressure. Results are monitored at position $\boldsymbol{X} = [32.8, 3.2, 3.2]^T$ mm in bar 2. A neo-Hookean model (9) is used. Their corresponding material parameters are summarized in Table 4.

![](./images/864987781904990352_35.jpg)

![](./images/864987781904990352_36.jpg)

![](./images/864987781904990352_37.jpg)

![](./images/864987781904990352_38.jpg)

FIGURE 26 Impact with non-matching interface mesh: Spatial distribution at time $t=260\ \mu\text{s}$ of (A) velocity component $v_x$,
(B) displacement component $u_x$, (C) stress component $\sigma_{xx}$, and (D) pressure along the line in bar 2 from $\boldsymbol{X}=[32.8,1.6,1.6]^T$ mm to
$\boldsymbol{X}=[65.2,1.6,1.6]^T$ mm. A neo-Hookean model (9) is used. Their corresponding material parameters are summarized in Table 4.

![](./images/864987781904990352_39.jpg)

FIGURE 27 Impact with non-matching interface mesh: Time evolution of (A) global total energy, (B) global numerical dissipation, (C) different energy measures for bar 1 (via Mesh IV), and (D) different energy measures for bar 2 (via Mesh IV). A neo-Hookean constitutive model as described in (9) is used. Their corresponding material parameters are summarized in Table 4.

![](./images/864987781904990352_40.jpg)

FIGURE 28 Impact with non-matching interface mesh: Time evolution of global total energy using the proposed method (Mesh IV), mean dilatation and linear finite element method. Comparison of deformed shapes at time $t = 205\ \mu\text{s}$ is shown, where the color plot indicates pressure distribution. A neo-Hookean constitutive model as described in (9) is used. Their corresponding material parameters are summarized in Table 4. The results of mean dilatation is obtained using 5000 number of trilinear hexahedra with 6171 number of nodes for bar 1 and 8640 number of trilinear hexahedra with 10,309 number of nodes for bar 2. The results of linear finite element method is obtained using 30,778 number of linear tetrahedra with 6267 number of nodes for bar 1 and 50,261 number of linear tetrahedra with 9976 number of nodes for bar 2.

![](./images/864987781904990352_41.jpg)

FIGURE 29 Torus impact: Geometry and problem setup.

<table>
<caption>TABLE 6 Torus impact: Material parameters used in the simulation.</caption>
<thead>
<tr>
<th></th>
<th></th>
<th>neo-Hookean</th>
<th>von-Mises plasticity</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Young's modulus</td>
<td>$E$</td>
<td>$1\times10^{6}$</td>
<td>$1\times10^{6}$</td>
<td>$\text{N m}^{-2}$</td>
</tr>
<tr>
<td>Material density</td>
<td>$\rho_R$</td>
<td>8930</td>
<td>8930</td>
<td>$\text{kg m}^{-3}$</td>
</tr>
<tr>
<td>Poisson's ratio</td>
<td>$\nu$</td>
<td>0.45</td>
<td>0.45</td>
<td></td>
</tr>
<tr>
<td>Lamé parameters</td>
<td>$\mu$</td>
<td>0.34483</td>
<td>0.34483</td>
<td>$\text{MN m}^{-2}$</td>
</tr>
<tr>
<td></td>
<td>$\lambda$</td>
<td>3.10345</td>
<td>3.10345</td>
<td>$\text{MN m}^{-2}$</td>
</tr>
<tr>
<td>Initial yield stress</td>
<td>$\tau_y^0$</td>
<td>-</td>
<td>$1\times10^{4}$</td>
<td>$\text{N m}^{-2}$</td>
</tr>
<tr>
<td>Hardening parameter</td>
<td>$H$</td>
<td>-</td>
<td>10</td>
<td>$\text{N m}^{-2}$</td>
</tr>
</tbody>
</table>

![](./images/864987781904990352_42.jpg)

![](./images/864987781904990352_43.jpg)

![](./images/864987781904990352_44.jpg)

![](./images/864987781904990352_45.jpg)

![](./images/864987781904990352_46.jpg)

![](./images/864987781904990352_47.jpg)

FIGURE 30 Torus impact: Time evolution of (first row) global total energy, (second row) global numerical dissipation, and (third row) different energy measures (via Mesh IV). The solution in the first column are obtained via neo-Hookean model and the solution of the second column are obtained via a Hencky-based von Mises plasticity model. Their corresponding material parameters are summarized in the third and fourth column of Table 6, respectively.

![](./images/864987781904990352_48.jpg)

FIGURE 31 Elastic torus impact: Comparison of deformed shapes at time $t = \{0.5, 1, 1.5, 2\}$ ms (from top to bottom) using (left column) proposed algorithm with **Mesh IV**, (center column) linear tetrahedral finite element method (101,045 number of elements and 20,427 number of nodes), and (right column) mean dilatation technique (29,441 number of hexahedra and 33,793 number of nodes). The color contour plot indicates pressure field. A neo-Hookean model described in (9) is used and the material parameters are summarized in third column of Table 6.

![](./images/864987781904990352_49.jpg)

FIGURE 32 Elastic torus impact: A sequence of deformed structures with pressure resolution at times $t = \{2.5, 5, 7.5, \dots, 50\}$ ms (from left to right and top to bottom). Results obtained using the proposed algorithm discretized with linear tetrahedra (Mesh IV). A neo-Hookean model is used and the corresponding material parameters are summarized in third column of Table 6.

![](./images/864987781904990352_50.jpg)

FIGURE 33 Elasto-plastic torus impact: Comparison of deformed shapes at time $t = \{0.5, 1, 1.5, 2\}$ ms (from top to bottom) using (left column) proposed algorithm with **Mesh IV**, (center column) linear tetrahedral finite element method (101,045 number of elements with 20,427 nodes), and (right column) mean dilatation technique (29,441 number of hexahedra with 33,793 nodes). The color contour indicates pressure field. A Hencky-based von Mises plasticity model is used and the material parameters are summarized in fourth column of Table 6.

![](./images/864987781904990352_51.jpg)

![](./images/864987781904990352_52.jpg)

FIGURE 34 Elasto-plastic torus impact: Time evolution of (A) velocity $v_x$, (B) displacement $u_x$, (C) stress $\sigma_{xx}$, and (D) pressure. Results are monitored at position $\boldsymbol{X} = [40, 0, 0]^T$ mm. Comparison is carried out between the proposed algorithm with **Mesh IV**, the linear tetrahedral finite element method (101,045 number of elements with 20,427 nodes) and the mean dilatation technique (29,441 number of hexahedra with 33,793 nodes). A Hencky-based von Mises plasticity model is used and the material parameters are summarized in fourth column of Table 6.

![](./images/864987781904990352_53.jpg)

FIGURE 35 Elasto-plastic torus impact: A sequence of deformed structures experiencing plasticity with pressure resolution at times $t = \{2.5, 5, 7.5, \dots, 50\}$ ms (from left to right and top to bottom). Results obtained using the proposed algorithm discretized with linear tetrahedra (Mesh IV). A Hencky-based von Mises plasticity model (with isotropic hardening) is used and the corresponding material parameters are summarized in fourth column of Table 6.

## 8 | CONCLUSIONS

The article presents an explicit vertex centered finite volume method for the dynamic solution of non-smooth contact problems, where a mixed system of first order conservation equations together with the associated jump conditions is used. Using the specific jump equation for the conservation of linear momentum, several dynamic contact models are derived ensuring the preservation of hyperbolic characteristic structure across contact interface. The formulation has been implemented within the modern CFD code "OpenFOAM," aiming to bridge the gap between CFD and Computational Solid Dynamics. Through the examples presented in this article, the proposed algorithm proves to perform extremely well in dynamic contact-impact problems without resorting to ad-hoc algorithmic regularization correction. Specifically, the proposed algorithm by construction overcomes a number of persistent numerical drawbacks commonly found in the literature. No spurious hour-glassing is observed and correct (smooth) pressure pattern are obtained in contrast to alter- native finite element approaches, such as the well known linear tetrahedral element technology. Crucially, the overall algorithm ensures long-term stability by monitoring the global entropy production via the Hamiltonian energy of the sys- tem. The consideration of nonlinear shock wave speeds in the contact-impact conditions within the current computational framework is the next step of our work.

## ACKNOWLEDGMENTS

Callum J. Runcie and Chun Hean Lee gratefully acknowledge the support provided by the EPSRC Strategic Support Package: Engineering of Active Materials by Multiscale/Multiphysics Computational Mechanics - EP/R008531/1. Anto- nio J. Gil and Chun Hean Lee would like to acknowledge the financial support received through the project Marie Skłodowska-Curie ITN-EJD ProTechTion, funded by the European Union Horizon 2020 research and innovation pro- gram with Grant number 764636. Callum J. Runcie and Chun Hean Lee would also like to acknowledge the many useful discussions with Dr. Peter Grassl from University of Glasgow.

## DATA AVAILABILITY STATEMENT

The data that support the findings of this study are available from the corresponding author upon reasonable request.

## ENDNOTES

*First order conservation equations with moving shocks are typically used in the solution of fluid dynamics problems where solution patterns incorporating shock waves are frequently encountered.

†When transverse deformation is neglected in the model, the speed of sound reduces to $c_{p}=\sqrt{\frac{E}{\rho_{R}}}$. This can be achieved by simply setting the value of Poisson's ratio equal to zero.

‡Exact energy transfer at the contact interface holds when an exact Riemann solver is used.

§In the second and third terms in the parenthesis of (61), the weighted average stencil proposed by Löhner et al. $^{67}$ is used by computing the boundary flux over a boundary face $\gamma$ (and $\beta$ ) in three dimensions as

$$
\mathcal{F}_{a}^{B}=\frac{6 \mathcal{F}_{a}^{B}+\mathcal{F}_{b}^{B}+\mathcal{F}_{c}^{B}}{8} ; \quad \mathcal{F}_{a}^{C}=\frac{6 \mathcal{F}_{a}^{C}+\mathcal{F}_{b}^{C}+\mathcal{F}_{c}^{C}}{8},
$$

where $b, c$ are the other two nodes that together with node $a$ define boundary face $\gamma$ (and $\beta$ ).

¶Moreover, we have also implemented the algorithm using an in-house software for the proof-of-concept one-dimensional and two-dimensional examples presented in the article.

#Insofar as the linear elastic model is used in this case, we thus neglect the physical dissipation introduced by the model, that is the rate of plastic dissipation.

‖It is important to emphasize that the simulation of rubber ring collision could have been performed with only one rubber ring via appropriate symmetry condition. However, in our case, we decided to consider the complete two-ring impact in order to check the resolution at shock interface between two bodies.

## ORCID

Chun Hean Lee ![](./images/864987781904990352_54.jpg) https://orcid.org/0000-0003-1102-3729

## REFERENCES

1. Gui C, Bai J, Zuo W. Simplified crashworthiness method of automotive frame for conceptual design. *Thin-Walled Struct.* 2018;131:324-335. doi:10.1016/j.tws.2018.07.005

2. Klemenz M, Schulze V, Rohr I, Löhe D. Application of the FEM for the prediction of the surface layer characteristics after shot peening. *J Mater Process Technol.* 2009;209(8):4093-4102. doi:10.1016/j.jmatprotec.2008.10.001

3. Sabsabi M, Giner E, Fuenmayor FJ. Experimental fatigue testing of a fretting complete contact and numerical life correlation using X-FEM. Int J Fatigue. 2011;33(6):811-822. doi:10.1016/j.ijfatigue.2010.12.012

4. Aguirre M, Avril S. An implicit 3D corotational formulation for frictional contact dynamics of beams against rigid surfaces using discrete signed distance fields. Comput Methods Appl Mech Eng. 2020;371:113275.

5. Belytschko T, Liu WK, Moran B. Nonlinear Finite Elements for Continua and Structures. John Wiley and Sons; 2000.

6. Cirak F, West M. Decomposition contact response (DCR) for explicit finite element dynamics. Int J Numer Methods Eng. 2005;64(8):1078-1110. doi:10.1002/nme.1400

7. Heinstein MW, Mello FJ, Attaway SW, Laursen TA. Contact-impact modeling in explicit transient dynamics. Comput Methods Appl Mech Eng. 2000;187:621-640.

8. Zienkiewicz OC, Taylor RL, Zhu JZ. The Finite Element Method : Its Basis ç Fundamentals. Vol 1. 6th ed. Butterworth-Heinemann; 2007.

9. VonNeumann J, Richtmyer RD. A method for the numerical calculation of hydrodynamic shocks. J Appl Phys. 1950;21(3):232-237. doi:10.1063/1.1699639

10. Donea J, Huerta A. Finite Element Methods for Flow Problems. Wiley and Sons; 2004.

11. Abedi R, Haber RB. Riemann solutions and spacetime discontinuous Galerkin method for linear elastodynamic contact. Comput Methods Appl Mech Eng. 2014;270:150-177.

12. Cardiff P, Demirdzic I. Thirty years of the finite volume method for solid mechanics. Arch Comput Methods Eng. 2021;28:3721-3780.

13. Cardiff P, Tukovic Z, Jaeger PD, Clancy M, Ivankovic A. A Lagrangian cell-centred finite volume method for metal forming simulation. Int J Numer Methods Eng. 2017;109:1777-1803.

14. Cardiff P, Karac A, Ivankovic A. Development of a finite volume contact solver based on the penalty method. Comput Mater Sci. 2012;64:283-284.

15. Scolaro A, Fiorina C, Clifford I, Pautz A. Development of a semi-implicit contact methodology for finite volume stress solvers. Int J Numer Methods Eng. 2021;123:309-338.

16. Skuric V, Jaeger PD, Jasak H. Luricated elastoplastic contact model for metal forming processes in OpenFOAM. Comput Fluids. 2018;172:226-240.

17. Scovazzi G, Carnes B, Zeng X, Rossi S. A simple, stable, and accurate linear tetrahedral finite element for transient, nearly and fully incompressible solid dynamics: a dynamic variational multiscale approach. Int J Numer Methods Eng. 2016;106:799-839.

18. Rossi S, Abboud N, Scovazzi G. Implicit finite volume incompressible elastodynamics with linear finite elements: a stabilized method in rate form. Comput Methods Appl Mech Eng. 2016;311:208-249.

19. Boscheri W, Loubere R, Maire PH. A 3D cell-centred ADER MOOD Finite Volume method for solving updated Lagrangian hyperelasticity on unstructured grids. J Comput Phys. 2022;449:110779.

20. Georges G, Breil J, Maire PH. A 3D finite volume scheme for solving the updated Lagrangian form of hyperelasticity. Int J Numer Methods Fluids. 2017;84(1):41-54. doi:10.1002/fld.4336

21. Scovazzi G. Stabilized shock hydrodynamics: II. Design and physical interpretation of the SUPG operator for Lagrangian computations. Comput Methods Appl Mech Eng. 2007;196:967-978.

22. Scovazzi G. A discourse on Galilean invariance, SUPG stabilization, and the variational multiscale framework. Comput Methods Appl Mech Eng. 2007;196:1108-1132.

23. Scovazzi G. Galilean invariance and stabilized methods for compressible flows. Int J Numer Methods Fluids. 2007;54:757-778.

24. Scovazzi G. Lagrangian shock hydrodynamics on tetrahedral meshes: a stable and accurate variational multiscale approach. J Comput Phys. 2012;231:8029-8069.

25. Scovazzi G, Christon MA, Hughes TJR, Shadid JN. Stabilized shock hydrodynamics: I. A Lagrangian method. Comput Methods Appl Mech Eng. 2007;196:923-966.

26. Scovazzi G, Love E. A generalized view on Galilean invariance in stabilized compressible flow computations. Int J Numer Methods Fluids. 2010;64:1065-1083.

27. Scovazzi G, Love E, Shashkov MJ. A multi-scale Q1/P0 approach to Lagrangian shock hydrodynamics. Comput Methods Appl Mech Eng. 2008;197:1056-1079.

28. Scovazzi G, Shadid JN, Love E, Rider WJ. A conservative nodal variational multiscale method for Lagrangian shock hydrodynamics. Comput Methods Appl Mech Eng. 2010;199:3059-3100.

29. Maire PH, Abgrall R, Breil J, Ovadia J. A cell-centered Lagrangian scheme for two-dimensional compressible flow problems. SIAM J Sci Comput. 2007;29:1781-1824.

30. Maire PH. A high-order cell-centered Lagrangian scheme for two-dimensional compressible fluid flows on unstructured meshes. J Comput Phys. 2009;228:2391-2425.

31. Barlow AJ, Roe PL. A cell centred Lagrangian Godunov scheme for shock hydrodynamics. Comput Fluids. 2011;46:133-136.

32. Barlow AJ. A high order cell centred dual grid Lagrangian Godunov scheme. Comput Fluids. 2013;83:15-24.

33. Barlow AJ, Maire PH, Rider WJ, Rieben RN, Shashkov MJ. Arbitrary Lagrangian Eulerian methods for modelling high-speed compressible multimaterial flows. J Comput Phys. 2016;322:603-665.

34. Hassan OI, Ghavamian A, Lee CH, Gil AJ, Bonet J, Auricchio F. An upwind vertex centred finite volume algorithm for nearly and truly incompressible explicit fast solid dynamic applications: total and updated Lagrangian formulations. J Comput Phys X. 2019;3:100025.

35. Aguirre M, Gil AJ, Bonet J, Lee CH. An upwind vertex centred finite volume solver for Lagrangian solid dynamics. J Comput Phys. 2015;300:387-422.

36. Chan A, Gallice G, Loubere R, Maire PH. Positivity preserving and entropy consistent approximate Riemann solvers dedicated to the high order MOOD-based finite volume discretisation of Lagrangian and Eulerian gas dynamics. *Comput Fluids*. 2021;229:105056.

37. Breil J, Georges G, Maire PH. 3D cell-centred Lagrangian second order scheme for the numerical modelling of hyperelasticity system. *Comput Fluids*. 2020;207:104523.

38. Maire PH, Bertron I, Chauvin R, Rebourcet B. Thermodynamic consistency of cell-centred Lagrangian schemes. *Comput Fluids*. 2020;203:104527.

39. Lee CH, Gil AJ, Greto G, Kulasegaram S, Bonet J. A new Jameson-Schmidt-Turkel Smooth Particle Hdrodynamics algorithm for large strain explicit fast dynamics. *Comput Methods Appl Mech Eng*. 2016;311:71-111.

40. Lee CH, Gil AJ, Hassan OI, Bonet J, Kulasegaram S. A variationally consistent streamline upwind Petrov Galerkin smooth particle hydrodynamics algorithm for large strain solid dynamics. *Comput Methods Appl Mech Eng*. 2017;318:514-536.

41. Bonet J, Gil AJ, Lee CH, Aguirre M, Ortigosa R. A first order hyperbolic framework for large strain computational solid dynamics. Part I: total Lagrangian isothermal elasticity. *Comput Methods Appl Mech Eng*. 2015;283:689-732.

42. Gil AJ, Lee CH, Bonet J, Ortigosa R. A first order hyperbolic framework for large strain computational solid dynamics. Part II: total Lagrangian compressible, nearly incompressible and truly incompressible elasticity. *Comput Methods Appl Mech Eng*. 2016;300:146-181.

43. Lee CH, Gil AJ, Ghavamian A, Bonet J. A total Lagrangian upwind Smooth Particle Hydrodynamics algorithm for large strain explicit solid dynamics. *Comput Methods Appl Mech Eng*. 2019;344:209-250. doi:10.1016/j.cma.2018.09.033

44. Karim IA, Lee CH, Gil AJ, Bonet J. A two-step Taylor Galerkin formulation for fast dynamics. *Eng Comput*. 2014;31:366-387. doi:10.1108/EC-12-2012-0319

45. Lee CH, Gil AJ, Bonet J. Development of a cell centred upwind finite volume algorithm for a new conservation law formulation in structural dynamics. *Comput Struct*. 2013;118:13-38.

46. Lee CH, Gil AJ, Bonet J. Development of a stabilised Petrov-Galerkin formulation for conservation laws in Lagrangian fast solid dynamics. *Comput Methods Appl Mech Eng*. 2014;268:40-64. doi:10.1016/j.cma.2013.09.004

47. Haider J, Lee CH, Gil AJ, Huerta A, Bonet J. An upwind cell centred Total Lagrangian finite volume algorithm for nearly incompressible explicit fast solid dynamic applications. *Comput Methods Appl Mech Eng*. 2018;340:684-727. doi:10.1016/j.cma.2018.06.010

48. Haider J, Lee CH, Gil AJ, Bonet J. A first order hyperbolic framework for large strain computational solid dynamics: an upwind cell centred total Lagrangian scheme. *Int J Numer Methods Eng*. 2017;109:407-456.

49. Ghavamian A, Lee CH, Gil AJ, Bonet J, Heuzé T, Stainier L. An entropy-stable Smooth Particle Hydrodynamics algorithm for large strain thermo-elasticity. *Comput Methods Appl Mech Eng*. 2021;379:113736. doi:10.1016/j.cma.2021.113736

50. Aguirre M, Gil AJ, Bonet J, Carreño AA. A vertex centred finite volume Jameson-Schmidt-Turkel (JST) algorithm for a mixed conservation formulation in solid dynamics. *J Comput Phys*. 2014;259:672-699. doi:10.1016/j.jcp.2013.12.012

51. Gil AJ, Lee CH, Bonet J, Aguirre M. A stabilised Petrov-Galerkin formulation for linear tetrahedral elements in compressible, nearly incompressible and truly incompressible fast dynamics. *Comput Methods Appl Mech Eng*. 2014;276:659-690.

52. de Campos PRR, Gil AJ, Lee CH, Giacomini M, Bonet J. A new updated reference Lagrangian smooth particle hydrodynamics algorithm for isothermal elasticity and elasto-plasticity. *Comput Methods Appl Mech Eng*. 2022;392:114680.

53. Bonet J, Gil AJ, Ortigosa R. On a tensor cross product based formulation of large strain solid mechanics. *Int J Solids Struct*. 2016;84:49-63.

54. de Boer R. *Vektor- und Tensorrechnung für Ingenieure*. Springer-Verlag; 1982.

55. Dafermos CM. Quasilinear hyperbolic systems with involutions. *Arch Ration Mech Anal*. 1986;94(4):373-389. doi:10.1007/BF00280911

56. LeVeque RL. *Finite Volume Methods for Hyperbolic Problems*. Cambridge University Press; 2002.

57. Toro EF. *Riemann Solvers and Numerical Methods for Fluid Dynamics: A Practical Introduction*. 2nd ed. Springer-Verlag; 2006.

58. Bonet J, Gil AJ, Wood RD. *Nonlinear Solid Mechanics for Finite Element Analysis: Statics*. Cambridge University Press; 2016.

59. Holzapfel GA. *Nonlinear Solid Mechanics: A Continuum Approach for Engineering*. Wiley and Sons; 2000.

60. Marsden JE, Hughes TJR. *Mathematical Foundations of Elasticity*. Dover Publications; 1994.

61. Bonet J, Gil AJ, Wood RD. *Nonlinear Solid Mechanics for Finite Element Analysis: Dynamics*. Cambridge University Press; 2020.

62. Bonet J, Lee CH, Gil AJ, Ghavamian A. A first order hyperbolic framework for large strain computational solid dynamics. Part III: thermo-elasticity. *Comput Methods Appl Mech Eng*. 2021;373:113505.

63. Low KWQ, Lee CH, Gil AJ, Haider J, Bonet J. A parameter-free total Lagrangian smooth particle hydrodynamics algorithm applied to problems with free surfaces. *Comput Part Mech*. 2021;8:859-892.

64. Abboud N, Scovazzi G. Elastoplasticity with linear tetrahedral elements: a variational multiscale method. *Int J Numer Methods Eng*. 2018;115:913-955. doi:10.1002/nme.5831

65. Zeng X, Scovazzi G, Abboud N, Colomés O, Rossi S. A dynamic variational multiscale method for viscoelasticity using linear tetrahedral elements. *Int J Numer Methods Eng*. 2017;112:1951-2003. doi:10.1002/nme.5591

66. Abboud N, Scovazzi G. A variational multiscale method with linear tetrahedral elements for multiplicative viscoelasticity. *Mech Res Commun*. 2021;112:103610. doi:10.1016/j.mechrescom.2020.103610

67. Lohner R, Morgan K, Zienkiewicz OC. The solution of non-linear hyperbolic equation systems by the finite element method. *Int J Numer Methods Fluids*. 1984;4:1043-1063.

68. Farrell PE, Maddison JR. Conservative interpolation between volume meshes by local Galerkin projection. *Comput Methods Appl Mech Eng*. 2011;200(1-4):89-100. doi:10.1016/j.cma.2010.07.015

69. Smith M. ABAQUS/Standard User's Manual. Version 6.10. Dassault Systèmes Simulia Corp. 2010.

70. Hughes TJ, Taylor RL, Sackman JL, Curnier A, Kanoknukulchai W. A finite element method for a class of contact-impact problems. *Comput Methods Appl Mech Eng*. 1976;8(3):249-276. doi:10.1016/0045-7825(76)90018-9

71. Wen-Hwa C, Pwu T. Finite element analysis of elastodynamic sliding contact problems with friction. Comput Struct. 1986;22(6):925-938. doi:10.1016/0045-hyphen;7949(86)90153-hyphen;7

72. Mahmoud FF, Hassan MM, Salamon NJ. Dynamic contact of deformable bodies. Comput Struct. 1990;36(1):169-181. doi:10.1016/0045&hyphen;7949(90)90186&hyphen;6

73. Sha D, Tamma KK, Li M. Robust explicit computational developments and solution strategies for impact problems involving friction. Int J Numer Methods Eng. 1996;39(5):721-739. doi:10.1002/(SICI)1097&hyphen;0207(19960315)39:5&lt;721::AID&hyphen;NME865&gt;3.0.CO;2&hyphen;J

74. Laursen TA, Chawla V. Design of energy conserving algorithms for frictionless dynamic contact problems. Int J Numer Methods Eng. 1997;40(5):863-886. doi:10.1002/(SICI)1097&hyphen;0207(19970315)40:5&lt;863::AID&hyphen;NME92&gt;3.0.CO;2&hyphen;V

75. Solberg JM, Papadopoulos P. A finite element method for contact/impact. Finite Elem Anal Des. 1998;30(4):297-311. doi:10.1016/S0168&hyphen;874X(98)00041&hyphen;9

76. Vidal Y, Bonet J, Huerta A. Stabilized updated Lagrangian corrected SPH for explicit dynamic problems. Int J Numer Methods Eng. 2006;69:2687-2710.

77. Gray JP, Monaghan JJ, Swift RP. SPH elastic dynamics. Comput Methods Appl Mech Eng. 2001;190:6641-6662.

How to cite this article: Runcie CJ, Lee CH, Haider J, Gil AJ, Bonet J. An acoustic Riemann solver for large strain computational contact dynamics. Int J Numer Methods Eng. 2022;123(23):5700-5748. doi: 10.1002/nme.7085