![](./images/813308500275888129_1.jpg)

Available online at www.sciencedirect.com

SciVerse ScienceDirect

Procedia IUTAM 3 (2012) 292 - 300

![](./images/813308500275888129_2.jpg)

www.elsevier.com/locate/procedia

# IUTAM Symposium on Linking Scales in Computations: from Microstructure to Macro-scale Properties

## Investigation of the effective response of 2-1-2 piezoelectric composites

Renald Brenner$^{a}$, Julián Bravo-Castillero$^{b}$, Daniel Mesejo León$^{b}$

$^{a}$Laboratoire des Sciences des Procédés et des Matériaux, CNRS, Université Paris Nord, 93430 Villetaneuse, France
$^{b}$Facultad de Matemática y Computación, Universidad de La Habana, San Lázaro y L, Vedado, CP 10400, Habana 4, Cuba

### Abstract

The question of the effective response of two-phase hybrid "fibrous-laminate" piezoelectric composites, with periodic microstructure, is adressed with two homogenization approaches: a full-field numerical scheme based on Fourier transform and a simplifying approach relying on a decoupled two-step homogenisation process. In the case of a two-phase epoxy/PZT composite, this latter is shown to overestimate out-of-plane effective piezoelectric coefficients.

© 2012 Published by Elsevier B.V. Selection and/or peer review under responsibility of Dr. Oana Cazacu.

Keywords: multifield coupling, composite material, homogenization, Fourier transform
PACS: 62.20.-x, 75.80.+q, 75.85.+t, 77.84.-s, 77.65.Ly
2010 MSC: 35B2, 74Q05, 74F15, 74G10, 74G15

### 1. Introduction

The microstructural design of heterogeneous smart materials is a topic of current interest in order to improve the figure of merit (i.e the coupling factor) of composite materials. Besides theoretical approaches relying on the use of bounds in the context of (micro)structural optimization [1], there is a need for efficient numerical homogenization tools, in particular to be able to consider arbitrarily complex microstructures. In the context of multifield coupling behaviours, the possibility of using Fourier transform based numerical schemes, initially proposed by Moulinec and Suquet [2] for mechanical problems, has been recently demonstrated [3, 4, 5]. A very good agreement has been obtained with *exact* analytical results, derived in the context of asymptotic homogenization method (AHM), for periodic smart composites with simple microstructural configurations [see, for instance, 6, 7]. This analytical approach can also be used to derive *approximate* results for the effective response of composites with "complex" microstructures. Along this

Email address: renald.brenner@univ-paris13.fr (Renald Brenner)

2210-9838 © 2012 Published by Elsevier B.V. Selection and/or peer review under responsibility of Dr. Oana Cazacu.
doi:10.1016/j.piutam.2012.03.018

line, the present study is focused on the derivation of estimates for the effective piezoelectric response of 2-1-2 two-phase piezoelectric composites for which no exact results exist. The analytical approach is compared to full-field computations performed with a fast Fourier transform (FFT)-based numerical procedure.

The homogenization problem with which we are concerned is briefly stated in section 2 and its resolution by analytical and numerical approaches is described in sections 3 and 4. An application is then given in section 5 for a two-phase composite material made of epoxy resin (elastic phase) and PZT ceramic (piezoelectric phase).

## 2. Studied problem

### 2.1. Formulation

Our study is concerned by the description of effective electroelastic properties (i.e elastic $\tilde{\mathbf{C}}$, permittivity $\tilde{\boldsymbol{\epsilon}}$ and piezoelectric $\tilde{\mathbf{e}}$ moduli) of a periodic heterogeneous medium. Its microstructure is thus entirely defined by a unit-cell, with volume $\Omega$ and outer surface $\partial \Omega$, and periodicity vectors. The field variables involved in this problem are the elastic strain $\boldsymbol{\varepsilon}$, the stress $\boldsymbol{\sigma}$, the electric induction $\mathbf{D}$ and the electric field $\mathbf{E}$. Besides, no assumptions are made on the fluctuation of the local properties tensor fields $(\mathbf{C}, \boldsymbol{\epsilon}$ and $\mathbf{e})$ within the unit-cell.

The local problem for the displacement field $\mathbf{u}(\mathbf{x})$ and the electric potential $\phi(\mathbf{x})$ can be expressed as

$$
\begin{cases}
\text { Constitutive law: } & \boldsymbol{\sigma}(\mathbf{x})=\mathbf{C}(\mathbf{x}): \boldsymbol{\varepsilon}(\mathbf{x})-{ }^{\mathrm{T}} \mathbf{e}(\mathbf{x}) \cdot \mathbf{E}(\mathbf{x}), \forall \mathbf{x} \in \Omega \\
& \mathbf{D}(\mathbf{x})=\mathbf{e}(\mathbf{x}): \boldsymbol{\varepsilon}(\mathbf{x})+\boldsymbol{\epsilon}(\mathbf{x}) \cdot \mathbf{E}(\mathbf{x}), \forall \mathbf{x} \in \Omega \\
\text { Curl-free fields: } & \boldsymbol{\varepsilon}=\frac{1}{2}\left(\operatorname{grad} \mathbf{u}+{ }^{\mathrm{T}} \operatorname{grad} \mathbf{u}\right), \quad \mathbf{E}=-\operatorname{grad} \phi \\
\text { Static equilibrium: } & \operatorname{div} \boldsymbol{\sigma}=0, \quad \operatorname{div} \mathbf{D}=0 \\
\text { Boundary conditions: } & \mathbf{u}(\mathbf{x})=\overline{\boldsymbol{\varepsilon}} \cdot \mathbf{x}+\mathbf{u}^{\star}(\mathbf{x}), \quad \phi(\mathbf{x})=-\overline{\mathbf{E}} \cdot \mathbf{x}+\phi^{\star}(\mathbf{x}), \forall \mathbf{x} \in \partial \Omega \\
& \left(\boldsymbol{u}^{\star}, \phi^{\star}\right) \text { periodic, }(\boldsymbol{\sigma} . \mathbf{n}, \mathbf{D} . \mathbf{n}) \text { anti-periodic }
\end{cases}
\tag{1}
$$

with $\mathbf{n}$ the outer normal of $\partial \Omega$. $\overline{\boldsymbol{\varepsilon}}$ and $\overline{\mathbf{E}}$ are the average values of the strain and electric fields over the unit-cell. For simple microstructural configurations (e.g laminate or 2D fibrous composites), this local problem can be solved analytically [6, 7, 8, 9]. However, the periodic composite materials which present a more complex microstructure call for some approximations or a full numerical resolution. In the sequel, we shall consider both approaches in the context of hybrid "fibrous-laminate" piezoelectric composites.

### 2.2. Unit-cell description

The composites considered in the present study are laminate periodic materials made of successive layers either homogeneous or presenting a "matrix-fiber" microstructure with a square distribution of unidirectional fibers with circular cross-section and aligned with the lamination direction $\mathbf{e}_{3}$. The fibers and the homogeneous layer are made with the same material. The unit-cell of such composite is represented on Figure 1. By adopting the classification according to their connectivity, defined as the number of dimensions through which each constitutive material is continuous, this type of heterogeneous structure is classically referred as 2-1-2 composites. With this terminology, 2-2 composite stands for a laminate material and 1-3 composite corresponds to a fiber-matrix microstructure (with parallel fibers). One of the motivation to devote this study to 2-1-2 smart composites is the recent experimental report of enhanced magneotelectric properties of such microstructure with respect to customary laminate ones [10]. Before envisaging the case of multiferroic composites, the focus of our study is on the 2-1-2 microstructural configuration. With this aim in view, we have chosen to consider smart composites with a single field coupling, namely the piezoelectric effect.

![](./images/813308500275888129_3.jpg)

Fig. 1. Unit-cell of 2-1-2 periodic composites with homogeneous layers $L_1$ (blue) and heterogeneous layers $L_0$ (green) made of a matrix phase (m) and aligned fibers (f) with a regular square distribution in the cross-section. The fibers (f) and the layers $L_1$ are made with the same material (hatched area). Left: longitudinal cut of the unit cell. Right: bottom-view of the unit-cell.

## 3. Approximate resolution based on "double asymptotic homogenization" method

The asymptotic homogenization method (AHM) is a rigorous mathematical technique which has been used to investigate the macroscopic behavior of different kinds of periodic heterogeneous media [11, 12, 13]. A crucial step in the implementation of the AHM is the fact that the calculation of effective coefficients depends on the solution a number of local problems defined on regular cells. These are the so-called local problems which involve systems of partial differential equations. For the considered 2-1-2 composite, an approximate model is built by making use of existing analytical results for 2-2 laminated piezoelectric composites [6] and 1-3 unidirectional fibrous composites with square distribution of the fibers in the transverse plane [7]. This "double asymptotic homogenization" (DAH) process is a two-step procedure which approximates the initial problem by two successive simpler problems:

(i). the effective properties of the heterogeneous fibrous layers are estimated with the AHM analytical result for 1-3 piezoelectric composites [7];

(ii). the effective properties of the overall 2-1-2 composite are obtained by considering a two-phase laminate material made of homogenized fibrous layers $(L_0)$ and homogeneous piezoelectric layers $(L_1)$ [6, see also Appendix A].

It is worth noting that the DAH procedure has been previously used to investigate 1-3 piezoelectric composites reinforced by unidirectional fibers with square cross-section. The original problem was decomposed into two successive 2-2 laminate problems and a good agreement has been obtained with experimental data [14]. In the sequel, the out-of-plane overall piezoelectric properties are considered. Since the constituents present a transversely isotropic behaviour whose symmetry axis is parallel to the lamination direction, the non-null out-of-plane effective piezoelectric coefficients are $\tilde{e}_{311}$ and $\tilde{e}_{333}$. The DAH provides the following approximate analytical expressions

$$
\tilde{e}_{311}={ }^{\mathrm{T}} \mathbf{e}_{2}\left\langle\mathbf{M}^{-1}\right\rangle^{-1}\left\langle\mathbf{M}^{-1}{ }^{\mathrm{T}} \mathbf{C}\right\rangle \quad \text { and } \quad \tilde{e}_{333}={ }^{\mathrm{T}} \mathbf{e}_{2}\left\langle\mathbf{M}^{-1}\right\rangle^{-1} \mathbf{e}_{1}.
\tag{2}
$$

$(\mathbf{e}_i, i \in [1,3])$ is the orthonormal basis for the Euclidian space, $\mathbf{C}$ and $\mathbf{M}$ are defined by

$$
\mathbf{C}=\left(C_{1133}  e_{311}\right) \quad \text { and } \quad \mathbf{M}=\left(\begin{array}{cc}
C_{3333} & e_{333} \\
e_{333} & -\epsilon_{33}
\end{array}\right).
\tag{3}
$$

and the angular brackets denote the average over the two-phase laminated unit-cell, that is,

$$
\langle\mathbf{M}\rangle=(1-\lambda) \mathbf{M}^{\left(L_{0}\right)}+\lambda \mathbf{M}^{\left(L_{1}\right)}
\tag{4}
$$

with $\lambda$ the volume fraction of homogeneous piezoelectric layers (phase $L_{1}$). The effective coefficients of the phase $L_{0}$ resulting from the AHM read [7]

$$
\left\{
\begin{aligned}
C_{3333}^{\left(L_{0}\right)} &= \left\langle C_{3333}\right\rangle_{L_{0}}-\lambda_{f}\left(C_{1133}^{(m)}-C_{1133}^{(f)}\right)^{2} K / C_{1212}^{(m)} ; \\
C_{1133}^{\left(L_{0}\right)} &= \left\langle C_{1133}\right\rangle_{L_{0}}+\left(k^{(m)}-k^{(f)}\right)\left(C_{3333}^{\left(L_{0}\right)}-\left\langle C_{3333}\right\rangle_{L_{0}}\right) /\left(C_{1133}^{(m)}-C_{1133}^{(f)}\right) ; \\
e_{311}^{\left(L_{0}\right)} &= \left\langle e_{311}\right\rangle_{L_{0}}+\left(k^{(m)}-k^{(f)}\right)\left(e_{311}^{(m)}-e_{311}^{(f)}\right)\left(C_{3333}^{\left(L_{0}\right)}-\left\langle C_{3333}\right\rangle_{L_{0}}\right) /\left(C_{1133}^{(m)}-C_{1133}^{(f)}\right)^{2} ; \\
e_{333}^{\left(L_{0}\right)} &= \left\langle e_{333}\right\rangle_{L_{0}}+\left(e_{311}^{(m)}-e_{311}^{(f)}\right)\left(C_{3333}^{\left(L_{0}\right)}-\left\langle C_{1133}\right\rangle_{L_{0}}\right) /\left(C_{3333}^{(m)}-C_{1133}^{(f)}\right) ; \\
\epsilon_{33}^{\left(L_{0}\right)} &= \left\langle\epsilon_{33}\right\rangle_{L_{0}}-\left(e_{311}^{(m)}-e_{311}^{(f)}\right)^{2}\left(C_{3333}^{\left(L_{0}\right)}-\left\langle C_{3333}\right\rangle_{L_{0}}\right) /\left(C_{1133}^{(m)}-C_{1133}^{(f)}\right)^{2}
\end{aligned}
\right.
\tag{5}
$$

where $\langle.\rangle_{L_{0}}$ denotes an average in the plane $(\mathbf{e}_{1}, \mathbf{e}_{2})$ over the two-dimensional square unit-cell, for instance

$$
\left\langle C_{3333}\right\rangle_{L_{0}}=\left(1-\lambda_{f}\right) C_{3333}^{(m)}+\lambda_{f} C_{3333}^{(f)}
\tag{6}
$$

with $\lambda_{f}=\pi \Phi^{2} / 4$ the fibre volume fraction within the layer $L_{0} ;(m)$ and $(f)$ indicates respectively a matrix and a fibre property. $k=(C_{1111}+C_{1122}) / 2$ is the plane-strain bulk modulus for lateral dilatation without longitudinal extension and the parameter $K$ can be expressed as follows

$$
K=C\left[1-\lambda_{f}+\left(3\left(1+\kappa^{(m)}\right) C R^{8}\left(S_{4}\right)^{2}\right) /\left(B^{-1}+R^{6}\left(A B^{-1} \phi+\psi+3 D R^{2}\left(S_{4}\right)^{2}\right)\right)\right],
$$

where

$$
\begin{aligned}
\phi &= c_{7}^{3} c_{7}^{5} R^{10}\left(S_{8}\right)^{2}, \\
\psi &=-3\left(R^{2} c_{8}^{4} S_{8}-c_{6}^{3} T_{7}\right), \\
A &=\left(\kappa^{(m)} \chi-\kappa^{(f)}\right) B /\left(\kappa^{(f)}+\chi\right), \\
B &=(1-\chi) /\left(1+\kappa^{(m)} \chi\right), \\
C &=\left[1+\left(\lambda_{f} k^{(m)}+\left(1-\lambda_{f}\right) k^{(f)}\right) / C_{1212}^{(m)}\right]^{-1}, \\
D &=2 C\left(k^{(f)} / k^{(m)}-1\right),
\end{aligned}
$$

with $\kappa^{(\alpha)}=1+2 C_{1212}^{(\alpha)} / k^{(\alpha)}(\alpha=m, f), \chi=C_{1212}^{(f)} / C_{1212}^{(m)}, c_{r}^{s}=r! / s!(r-s)!, R=\Phi / 2=\sqrt{\lambda_{f} / \pi}, S_{4}=3.151212$, $S_{8}=4.255731$ and $T_{7}=4.5155155$.

## 4. Numerical resolution based on Green's functions method

### 4.1. Principle

Green's functions method is customarily used in physics to solve inhomogeneous partial differential equations. The Green's function corresponding to a given problem represents its solution for an elementary "source". For an elastic body subjected to a distribution of volumic forces $\mathbf{f}(\mathbf{x}')$, the Green's function represents the solution of the problem (i.e the displacement field $\mathbf{u}(\mathbf{x})$ ) for an elementary applied force at point $\mathbf{x}'$. By linearity,

$$
\mathbf{u}(\mathbf{x})=\mathbf{G}(\mathbf{x}, \mathbf{x}') \cdot \mathbf{f}_{\mathrm{E}}(\mathbf{x}').
\tag{7}
$$

and the displacement field resulting from the distribution of forces $\mathbf{f}(\mathbf{x}')$ is deduced by integration.

In the case of an electroelastic problem, several Green's functions occur because of the coupling between electric and mechanical fields. It is thus necessary to determine the solution (i.e the displacement field $\mathbf{u}(\mathbf{x})$ )

ant the electric potential field $\phi(\mathbf{x}))$ for two elementary problems: an elementary localized force $\mathbf{f}_\mathrm{E}(\mathbf{x}')$ and an elementary localized electric charge $q_\mathrm{E}(\mathbf{x}')$. The electroelastic Green's functions are thus defined by

$$
\left\{
\begin{array}{l}
\mathbf{u}(\mathbf{x})=\mathbf{N}(\mathbf{x},\mathbf{x}').\mathbf{f}_\mathrm{E}(\mathbf{x}') \\
\phi(\mathbf{x})=\mathbf{H}(\mathbf{x},\mathbf{x}').\mathbf{f}_\mathrm{E}(\mathbf{x}')
\end{array}
\right.
\quad \text{and} \quad
\left\{
\begin{array}{l}
\mathbf{u}(\mathbf{x})=\mathbf{H}(\mathbf{x},\mathbf{x}').q_\mathrm{E}(\mathbf{x}') \\
\phi(\mathbf{x})=L(\mathbf{x},\mathbf{x}')\,q_\mathrm{E}(\mathbf{x}')
\end{array}
\right. .
\tag{8}
$$

It is worth emphasizing that the functions $\mathbf{N}(\mathbf{x},\mathbf{x}')$ and $L(\mathbf{x},\mathbf{x}')$ do not correspond to the ones of the purely elastic and electrostatic problems. Besides, it can be noted that, because of the symmetry of the piezoelectric effect, a sole function $\mathbf{H}$ describes the relation between a mechanical "source" and the corresponding electric response as well as the relation between an electrical "source" and the mechanical response. The studies concerning the determination of the electroelastic Green's functions dates back to the works of Deeg [15] who obtained their expression in the form of a contour integral in the direct space. Since then, many authors have considered this problem, with different approaches, for various anisotropic situations, see, for instance, [16, 17, 18]. However, these expressions remain rather tedious. By contradisctinction, the Fourier transforms of these Green's operators have simple analytic forms for general anisotropy.

### 4.2. Electroelastic Green's operators in Fourier space
The Fourier transforms of the electroelastic Green's operators, corresponding to an homogeneous medium with properties $\mathbf{C}^0$, $\boldsymbol{\epsilon}^0$ and $\mathbf{e}^0$, can be obtained by considering two periodic polarisation fields $\boldsymbol{\tau}(\mathbf{x})$ (mechanical) and $\mathbf{P}(\mathbf{x})$ (electrical) taking place within the material. The displacement field $\mathbf{u}(\mathbf{x})$ and the electric potential $\phi(\mathbf{x})$ are thus solutions of the following problem

$$
\left\{
\begin{array}{l}
\boldsymbol{\sigma}(\mathbf{x})=\mathbf{C}^0:\boldsymbol{\varepsilon}(\mathbf{x})-{ }^{\mathrm{T}}\mathbf{e}^0.\mathbf{E}(\mathbf{x})+\boldsymbol{\tau}(\mathbf{x}), \ \forall \mathbf{x} \in \Omega; \\
\mathbf{D}(\mathbf{x})=\mathbf{e}^0:\boldsymbol{\varepsilon}(\mathbf{x})+\boldsymbol{\epsilon}^0.\mathbf{E}(\mathbf{x})+\mathbf{P}(\mathbf{x}), \ \forall \mathbf{x} \in \Omega; \\
\operatorname{div} \boldsymbol{\sigma}=0, \quad \operatorname{div} \mathbf{D}=0, \ \forall \mathbf{x} \in \Omega; \\
\boldsymbol{\varepsilon}=\frac{1}{2}(\operatorname{grad} \mathbf{u}+{ }^{\mathrm{T}}\operatorname{grad} \mathbf{u}), \quad \boldsymbol{E}=-\operatorname{grad} \phi, \ \forall \mathbf{x} \in \Omega.
\end{array}
\right.
\tag{9}
$$

In Fourier space, it becomes

$$
\left\{
\begin{array}{l}
\hat{\boldsymbol{\sigma}}=\mathrm{i}\left(\mathbf{C}^0:(\boldsymbol{\xi} \otimes \hat{\mathbf{u}})+{ }^{\mathrm{T}}\mathbf{e}^0.\boldsymbol{\xi}\hat{\phi}\right)+\hat{\boldsymbol{\tau}}; \\
\hat{\mathbf{D}}=\mathrm{i}\left(\mathbf{e}^0:(\boldsymbol{\xi} \otimes \hat{\mathbf{u}})-\boldsymbol{\epsilon}^0.\boldsymbol{\xi}\hat{\phi}\right)+\hat{\mathbf{P}}; \\
\mathrm{i}\boldsymbol{\xi}.\hat{\boldsymbol{\sigma}}=0, \quad \mathrm{i}\boldsymbol{\xi}.\hat{\mathbf{D}}=0; \\
\hat{\boldsymbol{\varepsilon}}=\frac{\mathrm{i}}{2}(\boldsymbol{\xi} \otimes \hat{\mathbf{u}}+\hat{\mathbf{u}} \otimes \boldsymbol{\xi}), \quad \hat{\mathbf{E}}=-\mathrm{i}\hat{\phi}\boldsymbol{\xi}.
\end{array}
\right.
\tag{10}
$$

$\boldsymbol{\xi}$ denotes the frequency vector. The equilibrium relations together with the coupled constitutive law yields the system

$$
\left(
\begin{array}{cc}
\boldsymbol{\kappa} & \boldsymbol{\alpha} \\
\boldsymbol{\alpha} & -\lambda
\end{array}
\right)
\left(
\begin{array}{l}
\hat{\mathbf{u}} \\
\hat{\phi}
\end{array}
\right)
=\mathrm{i}\boldsymbol{\xi}.
\left(
\begin{array}{l}
\hat{\boldsymbol{\tau}} \\
\hat{\mathbf{P}}
\end{array}
\right)
\tag{11}
$$

with $\boldsymbol{\kappa}=\boldsymbol{\xi}.\mathbf{C}^0.\boldsymbol{\xi}$, $\boldsymbol{\alpha}=\boldsymbol{\xi}.\mathbf{e}^0.\boldsymbol{\xi}$ and $\lambda=\boldsymbol{\xi}.\boldsymbol{\epsilon}^0.\boldsymbol{\xi}$. From (11), the Fourier transforms of the gradient fields can be expressed as

$$
\hat{\boldsymbol{\varepsilon}}=-\hat{\boldsymbol{\Gamma}}^0:\hat{\boldsymbol{\tau}}-{ }^{\mathrm{T}}\hat{\boldsymbol{\Phi}}^0.\hat{\mathbf{P}} \quad \text{and} \quad \hat{\mathbf{E}}=\hat{\boldsymbol{\Phi}}^0:\hat{\boldsymbol{\tau}}+\hat{\boldsymbol{\Delta}}^0.\hat{\mathbf{P}}.
\tag{12}
$$

$\hat{\boldsymbol{\Gamma}}^0$, $\hat{\boldsymbol{\Phi}}^0$ and $\hat{\boldsymbol{\Delta}}^0$ are the Fourier transforms of the electroelastic Green's operators. The tensors $\boldsymbol{\Gamma}^0$, $\boldsymbol{\Delta}^0$ and $\boldsymbol{\Phi}^0$ are respectively the second derivatives of the Green's functions $\mathbf{N}^0$, $L^0$ and $\mathbf{H}^0$ previously introduced. The tensorial components of these operators read

$$
\begin{aligned}
\hat{\Gamma}_{ijkl}^0(\boldsymbol{\xi}) & =\frac{1}{4}\left(G_{ik}^{-1}\xi_j\xi_l+G_{jk}^{-1}\xi_i\xi_l+G_{il}^{-1}\xi_j\xi_k+G_{jl}^{-1}\xi_i\xi_k\right), \\
\hat{\Phi}_{nij}^0(\boldsymbol{\xi}) & =\frac{1}{2\lambda}\xi_n\left(G_{iq}^{-1}\xi_j+G_{jq}^{-1}\xi_i\right)\alpha_q, \quad \hat{\Delta}_{ij}^0(\boldsymbol{\xi})=\frac{1}{\lambda^2}\left(\boldsymbol{\alpha}.\mathbf{G}^{-1}.\boldsymbol{\alpha}-\lambda\right)\xi_i\xi_j,
\end{aligned}
\tag{13}
$$

with $\mathbf{G}=\boldsymbol{\kappa}+(1 / \lambda) \boldsymbol{\alpha} \otimes \boldsymbol{\alpha}$. In the case of vanishing piezoelectric coupling (i.e $\mathbf{e}^{0}=0$ ), the tensor $\mathbf{G}$ reduces to the elastic acoustic tensor, the operator $\hat{\boldsymbol{\Phi}}^{0}$ is null while the operators $\hat{\boldsymbol{\Gamma}}^{0}$ and $\hat{\boldsymbol{\Delta}}^{0}$ reduce to the ones of the elastic and electrostatic problems as it should. Equivalent expressions of the electroelastic Green's operators can be found in the literature [see, for instance, 19,20].

### 4.3. FFT numerical scheme
The FFT numerical scheme proposed by Moulinec and Suquet [2] rely on the Green's functions method. It consists in the use of a homogeneous reference medium. This approach, widely used for different prob- lems in micromechanics, allows to replace the original heterogeneous problem by an homogeneous problem with fictitious polarisation fields which depend on the fields which are solutions of the problem. The com- putational method takes advantage of the fact that the Green's operators, whose analytical expressions are available, act locally on the polarisation fields in the Fourier space.

The method can be implemented by introducing an electroelastic homogeneous medium with elasti- city $\mathbf{C}^{0}$, permittivity $\boldsymbol{\epsilon}^{0}$ and piezoelectricity $\mathbf{e}^{0}$. This leads to the following coupled Lippman-Schwinger equations for the solution fields $\varepsilon$ and $\mathbf{E}$

$$
\left\{\begin{array}{l}
\boldsymbol{\varepsilon}(\mathbf{x})=\overline{\boldsymbol{\varepsilon}}-\boldsymbol{\Gamma}^{0} * \boldsymbol{\tau}(\mathbf{x})-{ }^{\mathrm{T}} \boldsymbol{\Phi}^{0} * \mathbf{P}(\mathbf{x}) \\
\mathbf{E}(\mathbf{x})=\overline{\mathbf{E}}+\boldsymbol{\Phi}^{0} * \boldsymbol{\tau}(\mathbf{x})+\boldsymbol{\Delta}^{0} * \mathbf{P}(\mathbf{x})
\end{array}, \quad \forall \mathbf{x} \in \Omega.\right.
$$

$\boldsymbol{\tau}$ and $\mathbf{P}$ are fictitious polarisation fields respectively mechanical and electric. They read

$$
\boldsymbol{\tau}=\delta \mathbf{C}: \boldsymbol{\varepsilon}-{ }^{\mathrm{T}} \delta \mathbf{e}. \mathbf{E} \quad \text { and } \quad \mathbf{P}=\delta \mathbf{e}: \boldsymbol{\varepsilon}+\delta \boldsymbol{\epsilon}. \mathbf{E}
$$

with the notation $\delta \cdot=\cdot(\mathbf{x})-\cdot{ }^{0}$. The resolution of these equations by using the so-called "basic scheme", described in [2], has been assessed by comparison with available analytical and finite-elements (FE) results for simple microstructural situations (1-3 and 2-2 composites) [3].

## 5. Application to elastic-piezoelectric mixture
The two homogenisation procedures previously introduced are now applied to the case of a mixture of an elastic phase (epoxy resin) and a piezoelectric phase (PZT ceramic) with the elastic constituent as matrix (Figure 1). The data properties, taken from [21], are reported in Table 1. This case is challenging because

<table>
<thead>
<tr>
<th></th>
<th>$C_{11}$</th>
<th>$C_{12}$</th>
<th>$C_{13}$</th>
<th>$C_{33}$</th>
<th>$C_{44}$</th>
<th>$C_{66}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Epoxy</td>
<td>8.</td>
<td>4.4</td>
<td>4.4</td>
<td>8.</td>
<td>1.8</td>
<td>1.8</td>
</tr>
<tr>
<td>PZT</td>
<td>154.837</td>
<td>83.237</td>
<td>82.712</td>
<td>131.39</td>
<td>25.696</td>
<td>35.8</td>
</tr>
<tr>
<td></td>
<td>$e_{31}$</td>
<td>$e_{33}$</td>
<td>$e_{15}$</td>
<td>$ϵ_{11}$</td>
<td>$ϵ_{33}$</td>
<td></td>
</tr>
<tr>
<td>Epoxy</td>
<td>0.</td>
<td>0.</td>
<td>0.</td>
<td>3.72e-02</td>
<td>3.72e-02</td>
<td></td>
</tr>
<tr>
<td>PZT</td>
<td>-2.120582</td>
<td>9.52183</td>
<td>9.34959</td>
<td>4.065</td>
<td>2.079</td>
<td></td>
</tr>
</tbody>
</table>

Table 1. Material properties of the constituents (data taken from [21]). Elastic moduli are in GPa, dielectric moduli are in nC/Vm and piezoelectric moduli are in $C/m^{2}$.

of the different nature of the two phases. Results, with a fixed fiber volume fraction $\lambda_{f}=0.5$ in the hetero geneous layer $L_{0}$ , are reported on Figure 2 for the out-of-plane effective coefficients $\tilde{e}_{31}$ and $\tilde{e}_{33}$ . In the limitλ → 0, the FFT and AHM results agree very well. This case corresponds to 1-3 composites with a square array of unidirectional fibers. This result is consistent with previously published works [4]. The other limitλ → 1 corresponds to an homogeneous piezoelectric material. Within this range, it is shown that the FFT and DAH homogenization procedure lead to different estimations of the coefficients. However, it is worth noting that their curvature presents the same sign. The overestimation of the piezoelectric coefficients by

the DAH can be explained as follows: by using the approximate two-step procedure, the overall effective response results from the homogenization of a fictitious laminate composite made of two piezoelectric phases; indeed, the presence of the purely elastic phase is erased by the homogenization of the heterogeneous layer in contradistinction to the numerical scheme which takes it explicitly into account; as a consequence, the FFT procedure predicts a lower piezoelectric coupling. This observation emphasizes a difficulty, in the framework of functional materials, to evaluate certain effective coupling coefficients because of the nature of the phases involved. In the present case, it is expected that the DAH leads to a better agreement with reference FFT results for overall elastic and permittivity moduli. This is currently under investigation as well as the influence of the fiber volume fraction on the accuracy of the DAH. The investigation of 2-1-2 multifield coupling heterogeneous material (e.g multiferroic [10]), which is left for future works, shall benefit from these preliminary results.

![](./images/813308500275888129_4.jpg)

Fig. 2. Overall piezoelectric coefficients $\tilde{e}_{31}$ and $\tilde{e}_{33}$ for 2-1-2 epoxy/PZT composite as a function of the piezoelectric layer volume fraction $(\lambda)$. FFT computations have been performed for $\lambda=0,0.25,0.5$ and 0.75.

### Appendix A. Overall behaviour of piezoelectric laminates with arbitrary direction of lamination

We consider the case of a two-phase laminate composite which presents an arbitrary direction of lamina- tion and anisotropic local constitutive behaviour. The main steps to derive its effective behaviour are given and the reader is referred to [1, chap. 9] which provides comprehensive insights into lamination formulas.

Let a laminate composite material constituted of two phases $(i=1,2)$ with elastic moduli $\mathbf{C}^{i}$, dielectric permittivity $\boldsymbol{\epsilon}^{i}$, piezoelectric moduli $\mathbf{e}^{i}$ and volumic fraction $c_{i}$. $\Omega$ denotes the volume occupied by the material and $\Omega_{i}$ the volume occupied by phase $(i)$. The interface between the phases is noted $\Sigma$. The phases are successive layers of possibly variable thickness along the lamination direction $\mathbf{n}$. Consequently, the fields involved in the problem only vary in the direction $\mathbf{n}$. Thus, for any field $\mathbf{a}$,

$$
\mathbf{a}(\mathbf{x})=\mathbf{a}(\eta) \quad \text { with } \quad \eta=\mathbf{n}. \mathbf{x} \tag{A.1}
$$

The problem to solve can be stated as follows:

$$
\left\{
\begin{aligned}
& \mathbf{u}(\mathbf{x})=\overline{\boldsymbol{\varepsilon}}. \mathbf{x}, \phi(\mathbf{x})=-\overline{\mathbf{E}}. \mathbf{x}, \quad \forall \mathbf{x} \in \partial \Omega \quad \text { (Boundary conditions) } \\
& \boldsymbol{\sigma}(\mathbf{x})=\mathbf{C}^{i}: \boldsymbol{\varepsilon}(\mathbf{x})-{ }^{\mathrm{T}} \mathbf{e}^{i}. \mathbf{E}(\mathbf{x}), \quad \forall \mathbf{x} \in \Omega_{i} \quad \text { (Local law) } \\
& \mathbf{D}(\mathbf{x})=\mathbf{e}^{i}: \boldsymbol{\varepsilon}(\mathbf{x})+\boldsymbol{\epsilon}^{i}. \mathbf{E}(\mathbf{x}) \\
& \operatorname{div} \boldsymbol{\sigma}=0, \quad \operatorname{div} \mathbf{D}=0, \quad \forall \mathbf{x} \in \partial \Omega \backslash \Sigma \quad \text { (Equilibrium) } \\
& \boldsymbol{\varepsilon}=\frac{1}{2}\left(\operatorname{grad} \mathbf{u}+\operatorname{grad}^{\mathrm{T}} \mathbf{u}\right), \mathbf{E}=-\operatorname{grad} \phi \quad \text { (Compatibility) } \\
& {[\mathbf{u}(\mathbf{x})]=0,[\phi(\mathbf{x})]=0 \quad \forall \mathbf{x} \in \Sigma \quad \text { (Perfect interfaces) }}
\end{aligned}
\right. \tag{A.2}
$$

A solution with per-phase uniform fields is sought. The first step is to link the strain $\boldsymbol{\varepsilon}$ and electric field $\mathbf{E}$ within each phase $(i)$ to the overall strain $\overline{\boldsymbol{\varepsilon}}$ and electric field $\overline{\mathbf{E}}$. With Hadamard's lemma, the continuity of the displacement field at the interface $\Sigma$ ([u] = 0) imply $[\boldsymbol{\varepsilon}]=\boldsymbol{\varepsilon}^{2}-\boldsymbol{\varepsilon}^{1}=(1 / 2)(\mathbf{n} \otimes \boldsymbol{\alpha}+\boldsymbol{\alpha} \otimes \mathbf{n})$ and the continuity of the electric potential $([\phi]=0)$ gives $[\mathbf{E}]=\mathbf{E}^{2}-\mathbf{E}^{1}=\beta \mathbf{n}$ with $\boldsymbol{\alpha}$ and $\beta$ which are left undetermined. By using the average theorems on the strain and electric fields $(\langle\boldsymbol{\varepsilon}\rangle=\overline{\boldsymbol{\varepsilon}}$ and $\langle\mathbf{E}\rangle=\overline{\mathbf{E}})$, the fields within each phase read

$$
\left\{
\begin{aligned}
\boldsymbol{\varepsilon}^{1} & =\overline{\boldsymbol{\varepsilon}}-\frac{c_{2}}{2}(\mathbf{n} \otimes \boldsymbol{\alpha}+\boldsymbol{\alpha} \otimes \mathbf{n}), & \mathbf{E}^{1} & =\overline{\mathbf{E}}-c_{2} \beta \mathbf{n}, \\
\boldsymbol{\varepsilon}^{2} & =\overline{\boldsymbol{\varepsilon}}+\frac{c_{1}}{2}(\mathbf{n} \otimes \boldsymbol{\alpha}+\boldsymbol{\alpha} \otimes \mathbf{n}), & \mathbf{E}^{2} & =\overline{\mathbf{E}}+c_{1} \beta \mathbf{n}.
\end{aligned}
\right. \tag{A.3}
$$

$\boldsymbol{\alpha}$ and $\beta$ can be determined by using the equilibrium conditions on the stress $\boldsymbol{\sigma}$ and electric induction $\mathbf{D}$ which imply the uniformity of $\boldsymbol{\sigma} . \mathbf{n}$ and $\mathbf{D} . \mathbf{n}$ within the composite. By choosing, for instance, the equalities $\boldsymbol{\sigma}^{1} \cdot \mathbf{n}=\overline{\boldsymbol{\sigma}} \cdot \mathbf{n}$ and $\mathbf{D}^{1} \cdot \mathbf{n}=\overline{\mathbf{D}} . \mathbf{n}$, the following system is obtained for $\boldsymbol{\alpha}$ and $\beta$

$$
\left\{
\begin{aligned}
\alpha_{m} & =\frac{1}{2 c_{2}}\left[K_{m i}^{-1} n_{j}+K_{m j}^{-1} n_{i}\right]\left[C_{i j k l}^{1} \overline{\varepsilon}_{k l}-{ }^{\mathrm{T}} e_{i j p}^{1} \overline{E}_{p}-\overline{\sigma}_{i j}+c_{2}{ }^{\mathrm{T}} e_{i j p}^{1} n_{p} \beta\right], \\
\beta & =\frac{1}{c_{2}\left(n_{p} \epsilon_{p q}^{1} n_{q}\right)}\left[e_{k i j}^{1} \overline{\varepsilon}_{i j}+\epsilon_{k p}^{1} \overline{E}_{p}-\overline{D}_{k}-\frac{c_{2}}{2} e_{k i j}^{1}\left(n_{i} \alpha_{j}+n_{j} \alpha_{i}\right)\right] n_{k}
\end{aligned}
\right. \tag{A.4}
$$

with $\mathbf{K}=\mathbf{n} . \mathbf{C}^{1} . \mathbf{n}$. Then, the coupled constitutive law allows to obtain the stress tensor $\boldsymbol{\sigma}^{i}$ and electric induction vector $\mathbf{D}^{i}$ within each phase

$$
\boldsymbol{\sigma}^{i}=\mathbf{C}^{i}: \boldsymbol{\varepsilon}^{i}-{ }^{\mathrm{T}} \mathbf{e}^{i} . \mathbf{E}^{i} \quad \text { and } \quad \mathbf{D}^{i}=\mathbf{e}^{i}: \boldsymbol{\varepsilon}^{i}+\boldsymbol{\epsilon}^{i} . \mathbf{E}^{i}. \tag{A.5}
$$

Eventually, the effective constitutive relation

$$
\overline{\boldsymbol{\sigma}}=\tilde{\mathbf{C}}: \overline{\boldsymbol{\varepsilon}}-{ }^{\mathrm{T}} \tilde{\mathbf{e}} \cdot \overline{\mathbf{E}} \quad \text { and } \quad \overline{\mathbf{D}}=\tilde{\mathbf{e}}: \overline{\boldsymbol{\varepsilon}}+\tilde{\boldsymbol{\epsilon}} \cdot \overline{\mathbf{E}}
\tag{A.6}
$$

together with the average theorems $\langle\boldsymbol{\sigma}\rangle=\overline{\boldsymbol{\sigma}}$ and $\langle\mathbf{D}\rangle=\overline{\mathbf{D}}$ leads to the analytical expressions of $\tilde{\mathbf{C}}, \tilde{\mathbf{e}}$ and $\tilde{\boldsymbol{\epsilon}}$.

## References

[1] G. W. Milton, The theory of composites, Cambridge University Press, 2002.
[2] H. Moulinec, P. Suquet, A numerical method for computing the overall response of nonlinear composites with complex mi- crostructure, Comput. Methods Appl. Mech. Engrg. 157 (1998) 69-94.
[3] R. Brenner, Numerical computation of the response of piezoelectric composites using Fourier transform, Phys. Rev. B 79 (2009)184106.
[4] R. Brenner, Computational approach for composite materials with coupled constitutive laws, Z. angew. Math. Phys. 61 (2010)919-927.
[5] R. Brenner, J. Bravo-Castillero, Response of multiferroic composites inferred from a fast-Fourier-transform based numerical scheme, Smart Mater. Struct. 19 (2010) 115004.
[6] J. Bravo-Castillero, J. A. Otero, R. R. Ramos, A. Bourgeat, Asymptotic homogenization of laminated piezocomposite materials, Int. J. Solids Structures 35 (1998) 527-541.
[7] J. Bravo-Castillero, R. Guinovart-Diaz, F. J. Sabina, R. Rodriguez-Ramos, Closed-form expressions for the effective coefficients of a fiber-reinforced composite with transversely isotropic constituents - II. Piezoelectric and square symmetry, Mech. Mater. 33(2001) 237-248.
[8] J. Bravo-Castillero, R. Rodriguez-Ramos, R. Guinovart-Diaz, F. J. Sabina, A. R. Aguiar, U. P. Silva, J. L. Gomez-Munoz, Analytical formulae for electromechanical effective properties of 3-1 longitudinally porous piezoelectric materials, Acta Mater.57 (2009) 795-803.
[9] F. J. Sabina, J. R. Rodriguez-Ramos, J. Bravo- Castillero, R. Guinovart-Diaz, Closed-form expressions for the effective coefficients of a fibre-reinforced composite with transversely isotropic constituents. II: Piezoelectric and hexagonal symmetry, J. Mech. Phys. Solids 49 (2001) 1463-1479.
[10] C.-S. Park, C. Ahn, S. Priya, Enhanced magnetoelectric properties in three-phase composites with 2-1-2 connectivity, Phil. Mag. A 90 (2010) 4443-4452.
[11] A. Bensoussan, J.-L. Lions, G. Papanicolaou, Asymptotic analysis for periodic structures, North-Amsterdam, 1979.
[12] E. Sanchez-Palencia, Lecture notes in physics, vol. 127, Springer, 1980, Ch. Non homogeneous media and vibration theory.
[13] N. S. Bakhvalov, G. P. Panasenko, Homogenization averaging processes in periodic media, Kluwer Academic Publishers, 1989.
[14] J. A. Otero, J. Bravo-Castillero, R. Guinovart-Diaz, R. Rodriguez-Ramos, G. A. Maugin, Analytical expressions of effective constants for a piezoelectric composite reinforced with square cross-section fibers, Arch. Mech. 55 (2003) 357-371.
[15] W. F. Deeg, The analysis of dislocation, crack and inclusion problems in piezoelectric solids, Ph.D. thesis, Stanford University, U.S.A (1980).
[16] M. L. Dunn, H. A. Wienecke, Green's functions for transversely isotropic piezoelectric solids, Int. J. Solids Struct. 33 (1996)4571-4581.
[17] M. Akamatsu, K. Tanuma, Green's function of anisotropic piezoelectricity, Proc. R. Soc. Lond. A453 (1997) 473-487.
[18] X. Li, M. Wang, Three-dimensional green's functions for infinite anisotropic piezoelectric media, Int. J. Solids Struct. 44 (2007)1680-1684.
[19] B. Wang, Three-dimensional analysis of an ellipsoidal inclusion in a piezoelectric material, Int. J. Solids Struct. 29 (1992) 293-308.
[20] J. H. Huang, J. S. Yu, Electroelastic eshelby tensors for an ellipsoidal piezoelectric inclusion, Comp. Engng 4 (1994) 1169-1182.
[21] H. E. Pettermann, S. Suresh, A comprehensive unit cell model: a study of coupled effects in piezoelectric 1-3 composites, Int. J. Solids Struct. 37 (2000) 5447-5464.