Z. Yan · L. Y. Jiang

# Interaction of parallel dielectric cracks in functionally graded piezoelectric materials

Received: 21 February 2009 / Revised: 31 July 2009 / Published online: 10 September 2009
© Springer-Verlag 2009

Abstract In this paper, the problem of two interacting parallel cracks in functionally graded piezoelectric materials under in-plane electromechanical loads is studied. The formulation is based on using Fourier transforms and modeling the cracks as distributed dislocations, and the resulting singular integral equations are solved with Chebyshev polynomials. A dielectric crack model considering the crack filling effect is adopted to describe the electric boundary conditions along crack surfaces. Numerical simulations are made to show the effect of material gradient, the geometry of interacting cracks, and crack position upon fracture parameters such as stress intensity factors, electric displacement intensity factor, and COD intensity factor. By considering the effect of a dielectric medium inside the crack and crack deformation, the results obtained from the dielectric crack model are always between those from the traditional crack models with physical limitation.

## 1 Introduction

The use of piezoelectric materials as sensors, actuators, and transducers in smart structures has been extensively explored by researchers and engineers. To achieve the increased life time and reliability of these electromechanical devices, new piezoelectric materials with continuous change of material properties have been introduced and investigated [1–3], which are called functionally graded piezoelectric materials (FGPMs). These FGPMs are expected to possess the advantages of both traditional FGMs and piezoelectric materials. For example, Takagi et al. [4] have shown that the piezoelectric structures made of FGPMs with optimized composition profile can perform better than those homogeneous piezoelectric ones. However, the commonly used piezoelectric materials, such as piezoceramics, are generally brittle and susceptible to developing multiple cracks during their manufacturing and service processes. The presence of cracks may significantly affect their electromechanical performance and their structural integrity. Therefore, the fracture analysis of FGPMs with interacting cracks should be well understood to ensure the safety and reliability of smart structures.

A critical issue involved in the prediction of fracture behavior of piezoelectric materials is the appropriate crack model describing the electromechanical boundary conditions along crack surfaces. In existing theoretical studies, the mechanical boundary condition for a crack is traction-free similar to the crack problem in an elastic medium. However, there are different opinions about the electric boundary condition. Traditionally, there exist two commonly used crack models. One is the electrically permeable model proposed by Parton [5] with perfect contact of the crack surfaces and continuous electric potential and normal component of electric displacement across the crack surfaces. The other one is the electrically impermeable model [6], in which the

---

Z. Yan · L. Y. Jiang (⊗)
Department of Mechanical and Materials Engineering,
The University of Western Ontario, London, ON N6A 5B9, Canada
E-mail: lyjiang@eng.uwo.ca
Tel.: +1-519-661-2111
Fax: +1-519-661-3020

electric induction of the medium filling the crack is neglected. These two models represent two limiting cases, where dielectric permittivity of the medium filling the crack is assumed to be infinite and zero, respectively. In most engineering situations, cracks in piezoelectric materials are filled with a dielectric medium, such as air or vacuum. To evaluate this crack filling effect, an elliptical crack model has been developed by McMeeking [7] and Dunn [8]. Based on this model, subsequent studies [9–12] indicated that the electrically permeable model may underestimate the effect of the electric field on the crack propagation, while the impermeable one may overestimate this effect. Another crack model considering the effect of a dielectric medium is the intermediate crack model [13,14], in which the crack is represented by a dielectric thin layer. With the increase of the assumed layer thickness, the transition from the permeable to impermeable crack models has been observed. It should be mentioned that for both elliptical and intermediate crack models the thickness of the crack must be pre-assumed, which is the original profile of the crack and is independent of the crack deformation. As argued by Chiang and Weng [15], when a slit crack without initial crack opening is subjected to a tensile stress, the crack will open up (mode I crack) and both the dielectric crack filling and crack surface separation will play a crucial role in the fracture performance of piezoelectric materials. As a result, a crack model with deformation-dependent electric boundary condition should be considered. A dielectric crack model consid- ering the effect of both crack filling and crack deformation has been used to study the fracture behavior of piezoelectric materials [16–19]. Such a model avoids any pre-assumed thickness of the crack and considers the "real" electric boundary condition along the crack surfaces, which is expected to predict the electromechanical behavior of piezoelectric materials more accurately.

There are numerous studies on the problem of interacting cracks in homogeneous piezoelectric materials. For example, Meguid and Wang [20] investigated the dynamic antiplane behavior of interacting permeable cracks under incident antiplane shear wave loading. This permeable crack model has also been used to study the problem of interacting parallel cracks by Zhou et al. [21] using the non-local theory. Han and Chen [22] proposed a "pseudo-traction-electric displacement" method for solving the parallel interacting crack problem using an impermeable crack model. Han and Wang [23] calculated the in-plane electro-elastic fields in piezo- electric materials with multiple impermeable cracks. To consider the effect of a dielectric medium filling the crack, a dielectric crack model was used by Wang and Jiang [24] and Zhou et al. [25] to study the fracture behavior of interacting cracks. Compared with the extensive studies on the fracture analysis for homogeneous piezoelectric materials, there exists fewer work for the crack problem of nonhomogeneous piezoelectric mate- rials, i.e., the FGPMs. Li and Weng [26,27] were the first to study the anti-plane problem of a single crack in a strip of FGPM. It was observed in their study that the material gradient has significant effect upon the fracture properties of FGPMs. For the interacting crack problem in FGPMs, Ma et al. [28] investigated the gradient effect upon the interaction of two collinear cracks under shear harmonic loading. Using the non-local theory, Zhou and Wu [29] studied the anti-plane problem of two collinear permeable cracks in FGPMs to see the material gradient effect and crack interaction. The mode I problem of two parallel cracks in FGPMs was studied by Zhang et al. [30] using a permeable model. It should be mentioned that for mode II and mode III crack problems the traditionally impermeable and permeable crack models may be accurate to predict the fracture behavior of FGPMs since the dielectric permittivity of the medium filling the crack really plays no role and should not appear in the electric boundary condition. However, for a mode I crack problem under a tensile stress, the crack opens up and the dielectric medium inside the crack and crack deformation may play a significant role in the fracture performance. Therefore, a dielectric crack model should be introduced. Recently, Zhou and Chen [31] used the dielectric crack model to study the problem of two center aligned parallel cracks in an FGPM with material property varying along crack line direction. It is found that the magnitudes of intensity factors depend on the dielectric permittivity of the air inside the crack and the material gradient of FGPMs.

In this work, a comprehensive theoretical study will be provided to study the problem of two parallel cracks in FGPMs using a dielectric crack model, in which the material gradient of the medium varies exponentially perpendicular to the crack surfaces. The formulations are derived based on Fourier transform, and the resulting singular integral equations are solved with Chebyshev polynomials. Numerical results are provided to show the effects of the material gradient of FGPMs, the geometry of interacting cracks and the dielectric medium filling the crack upon fracture parameters.

## 2 Statement of the problem

The plane problem where an infinite FGPM medium contains two parallel cracks of lengths $2a_{I}$ and $2a_{II}$ subjected to mechanical loads $\sigma_{yi}^{0}$ ($i=x,y$) and an electric displacement $D_{y}^{0}$ at infinity is considered. The

![](./images/811832875929305089_1.jpg)

Fig. 1 Crack model

poling direction for the piezoelectric material is along the $y$ direction in the global Cartesian coordinate system $(x, y)$ as shown in Fig. 1. Two local Cartesian coordinate systems $(x_{k}, y_{k})$ with $k=I, II$ are attached to the center of each crack to describe the crack position. Due to the crack deformation caused by applied loads, there exists an electric potential jump $\Phi_{k}^{+}-\Phi_{k}^{-}(k=I, II)$ across the crack surfaces. To make the problem more mathematically tractable, it is assumed that all material constants have the same distribution format and vary exponentially along the poling direction $y$ as

$$
\begin{bmatrix}
c_{11} & c_{13} & 0 \\
c_{13} & c_{33} & 0 \\
0 & 0 & c_{44}
\end{bmatrix} = e^{\alpha y}
\begin{bmatrix}
c_{11}^{0} & c_{13}^{0} & 0 \\
c_{13}^{0} & c_{33}^{0} & 0 \\
0 & 0 & c_{44}^{0}
\end{bmatrix}, \quad
\begin{bmatrix}
0 & e_{31} \\
0 & e_{33} \\
e_{15} & 0
\end{bmatrix} = e^{\alpha y}
\begin{bmatrix}
0 & e_{31}^{0} \\
0 & e_{33}^{0} \\
e_{15}^{0} & 0
\end{bmatrix},
\tag{1}
$$

$$
\begin{bmatrix}
\epsilon_{11} & 0 \\
0 & \epsilon_{33}
\end{bmatrix} = e^{\alpha y}
\begin{bmatrix}
\epsilon_{11}^{0} & 0 \\
0 & \epsilon_{33}^{0}
\end{bmatrix},
\tag{2}
$$

where $\alpha$ is the material gradient, $c_{11}, c_{13}, c_{33}, c_{44}$ are elastic constants, $e_{31}, e_{33}, e_{15}$ are piezoelectric constants, and $\epsilon_{11}, \epsilon_{33}$ are dielectric constants. $c_{11}^{0}, c_{13}^{0}, c_{33}^{0}, c_{44}^{0}, e_{31}^{0}, e_{33}^{0}, e_{15}^{0}, \epsilon_{11}^{0}, \epsilon_{33}^{0}$ are the corresponding material constants at $y=0$ in the global coordinate system.

In the absence of body force and free charges, the electromechanical behavior of transversely isotropic FGPMs is governed by the basic equations given in the global $(x, y)$ coordinate system,

$$
\frac{\partial \sigma_{x x}}{\partial x}+\frac{\partial \sigma_{x y}}{\partial y}=0, \quad \frac{\partial \sigma_{y x}}{\partial x}+\frac{\partial \sigma_{y y}}{\partial y}=0, \quad \frac{\partial D_{x}}{\partial x}+\frac{\partial D_{y}}{\partial y}=0,
\tag{3}
$$

and the constitutive equations

$$
\left\{
\begin{array}{l}
\sigma_{x x} \\
\sigma_{y y} \\
\sigma_{x y}
\end{array}
\right\} =
\begin{bmatrix}
c_{11} & c_{13} & 0 \\
c_{13} & c_{33} & 0 \\
0 & 0 & c_{44}
\end{bmatrix}
\left\{
\begin{array}{l}
\varepsilon_{x x} \\
\varepsilon_{y y} \\
2 \varepsilon_{x y}
\end{array}
\right\} -
\begin{bmatrix}
0 & e_{31} \\
0 & e_{33} \\
e_{15} & 0
\end{bmatrix}
\left\{
\begin{array}{l}
E_{x} \\
E_{y}
\end{array}
\right\},
\tag{4}
$$

$$
\left\{
\begin{array}{l}
D_{x} \\
D_{y}
\end{array}
\right\} =
\begin{bmatrix}
0 & 0 & e_{15} \\
e_{31} & e_{33} & 0
\end{bmatrix}
\left\{
\begin{array}{l}
\varepsilon_{x x} \\
\varepsilon_{y y} \\
2 \varepsilon_{x y}
\end{array}
\right\} +
\begin{bmatrix}
\epsilon_{11} & 0 \\
0 & \epsilon_{33}
\end{bmatrix}
\left\{
\begin{array}{l}
E_{x} \\
E_{y}
\end{array}
\right\},
\tag{5}
$$

where $\sigma_{i j}$ and $D_{i}$ ($i, j=x, y$) are stress and electric displacement components, and $\varepsilon_{i j}$ and $E_{i}$ are defined as

$$
\varepsilon_{i j}=\frac{1}{2}\left(u_{, j}+v_{, i}\right), \quad E_{i}=-\Phi_{, i} \ (i, j=x, y),
\tag{6}
$$

with $u, v$ and $\Phi$ being displacements and electric potential.

Substituting Eqs. (1) and (2), (4)–(6) into Eq. (3), the governing equations for the FGPM can be expressed as

$$
\frac{\partial^{2} u}{\partial y^{2}}+\beta_{1} \frac{\partial^{2} u}{\partial x^{2}}+\beta_{2} \frac{\partial^{2} v}{\partial x \partial y}+\beta_{3} \frac{\partial^{2} \Phi}{\partial x \partial y}+\alpha\left(\frac{\partial u}{\partial y}+\frac{\partial v}{\partial x}\right)+\alpha \beta_{4} \frac{\partial \Phi}{\partial x}=0,
\tag{7}
$$

$$
\frac{\partial^{2} v}{\partial y^{2}}+\beta_{5} \frac{\partial^{2} v}{\partial x^{2}}+\beta_{6} \frac{\partial^{2} u}{\partial x \partial y}+\beta_{7} \frac{\partial^{2} \Phi}{\partial x^{2}}+\beta_{8}\left(\frac{\partial^{2} \Phi}{\partial y^{2}}+\alpha \frac{\partial \Phi}{\partial y}\right)+\alpha \beta_{9} \frac{\partial u}{\partial x}+\alpha \frac{\partial v}{\partial y}=0,
\tag{8}
$$

$$
\frac{\partial^{2} \Phi}{\partial y^{2}}+\beta_{10} \frac{\partial^{2} \Phi}{\partial x^{2}}+\beta_{11} \frac{\partial^{2} v}{\partial x^{2}}+\beta_{12}\left(\frac{\partial^{2} v}{\partial y^{2}}+\alpha \frac{\partial v}{\partial y}\right)+\beta_{13} \frac{\partial^{2} u}{\partial x \partial y}+\alpha \beta_{14} \frac{\partial u}{\partial x}+\alpha \frac{\partial \Phi}{\partial y}=0.
\tag{9}
$$

The coefficients $\beta_{1}-\beta_{14}$ are related to the material constants as

$$
\begin{aligned}
& \beta_{1}=c_{11}^{0}\left(c_{44}^{0}\right)^{-1}, \quad \beta_{2}=\left(c_{13}^{0}+c_{44}^{0}\right)\left(c_{44}^{0}\right)^{-1}, \quad \beta_{3}=\left(e_{31}^{0}+e_{15}^{0}\right)\left(c_{44}^{0}\right)^{-1}, \quad \beta_{4}=e_{15}^{0}\left(c_{44}^{0}\right)^{-1}, \quad \beta_{5}=c_{44}^{0}\left(c_{33}^{0}\right)^{-1}, \\
& \beta_{6}=\left(c_{13}^{0}+c_{44}^{0}\right)\left(c_{33}^{0}\right)^{-1}, \quad \beta_{7}=e_{15}^{0}\left(c_{33}^{0}\right)^{-1}, \quad \beta_{8}=e_{33}^{0}\left(c_{33}^{0}\right)^{-1}, \quad \beta_{9}=c_{13}^{0}\left(c_{33}^{0}\right)^{-1}, \quad \beta_{10}=\epsilon_{11}^{0}\left(\epsilon_{33}^{0}\right)^{-1}, \\
& \beta_{11}=-e_{15}^{0}\left(\epsilon_{33}^{0}\right)^{-1}, \quad \beta_{12}=-e_{33}^{0}\left(\epsilon_{33}^{0}\right)^{-1}, \quad \beta_{13}=-\left(e_{31}^{0}+e_{15}^{0}\right)\left(\epsilon_{33}^{0}\right)^{-1}, \quad \beta_{14}=-e_{31}^{0}\left(\epsilon_{33}^{0}\right)^{-1}.
\end{aligned}
\tag{10}
$$

To account for the effect of both crack filling and crack deformation upon the fracture property of interacting cracks, a dielectric crack is used in the current work. Considering the perturbation field only, the mechanical and electric boundary conditions along the crack surface $(|x_{k}|<a_{k}, y_{k}=0, k=I, II)$ for each crack are given in the local coordinate systems as

$$
\sigma_{y i}^{k}\left(x_{k}, 0^{+}\right)=\sigma_{y i}^{k}\left(x_{k}, 0^{-}\right)=-\sigma_{y i}^{0} \quad(i=x, y),
\tag{11}
$$

$$
D_{y}^{k}\left(x_{k}, 0^{+}\right)=D_{y}^{k}\left(x_{k}, 0^{-}\right)=-D_{y}^{0}-\kappa \frac{\Phi^{k+}-\Phi^{k-}}{v^{k+}-v^{k-}},
\tag{12}
$$

where superscripts "+" and "-" represent the upper and lower surfaces of the crack, $\kappa$ is the dielectric permittivity of the medium filling the crack (for example, $\kappa=\kappa_{0}=8.85 \times 10^{-12} \mathrm{C} / \mathrm{Vm}$ for air). $\Phi^{k+}-\Phi^{k-}, v^{k+}-v^{k-}$ are the electric potential and crack opening displacement across the crack surface caused by external loads.

For each individual crack, the following continuity conditions along the crack line must also be satisfied:

$$
\sigma_{y i}^{k+}=\sigma_{y i}^{k-}, \quad D_{y}^{k+}=D_{y}^{k-}\left(a_{k}<\left|x_{k}\right|<\infty, y_{k}=0\right),
\tag{13}
$$

$$
u^{k+}=u^{k-}, \quad v^{k+}=v^{k-}, \quad \Phi^{k+}=\Phi^{k-}\left(a_{k}<\left|x_{k}\right|<\infty, y_{k}=0\right).
\tag{14}
$$

## 3 The fundamental solution of a single crack

Following the same procedure of solving the crack problem of an elastic FGM [32] and applying Fourier transforms with respect to $x$ to Eqs. (7)–(9), the solutions of $u^{*}, v^{*}$ and $\Phi^{*}$ (the Fourier transform of $u, v$ and $\Phi$) satisfying the regularity conditions at infinity and the continuity condition (13) along the crack line can be written as

$$
u^{*}(s, y)= \begin{cases}C_{2} e^{\lambda_{2} y}+C_{4} e^{\lambda_{4} y}+C_{6} e^{\lambda_{6} y}, & y>0, \\ \left(f_{1} C_{2}+f_{2} C_{4}+f_{3} C_{6}\right) e^{\lambda_{1} y}+\left(f_{4} C_{2}+f_{5} C_{4}+f_{6} C_{6}\right) e^{\lambda_{3} y}, & \\ +\left(f_{7} C_{2}+f_{8} C_{4}+f_{9} C_{6}\right) e^{\lambda_{5} y}, & y<0,\end{cases}
\tag{15}
$$

$$
v^{*}(s, y)= \begin{cases}a_{2} C_{2} e^{\lambda_{2} y}+a_{4} C_{4} e^{\lambda_{4} y}+a_{6} C_{6} e^{\lambda_{6} y}, & y>0, \\ a_{1}\left(f_{1} C_{2}+f_{2} C_{4}+f_{3} C_{6}\right) e^{\lambda_{1} y}+a_{3}\left(f_{4} C_{2}+f_{5} C_{4}+f_{6} C_{6}\right) e^{\lambda_{3} y}, & \\ +a_{5}\left(f_{7} C_{2}+f_{8} C_{4}+f_{9} C_{6}\right) e^{\lambda_{5} y}, & y<0,\end{cases}
\tag{16}
$$

$$
\Phi^{*}(s, y)= \begin{cases}b_{2} C_{2} e^{\lambda_{2} y}+b_{4} C_{4} e^{\lambda_{4} y}+b_{6} C_{6} e^{\lambda_{6} y}, & y>0, \\ b_{1}\left(f_{1} C_{2}+f_{2} C_{4}+f_{3} C_{6}\right) e^{\lambda_{1} y}+b_{3}\left(f_{4} C_{2}+f_{5} C_{4}+f_{6} C_{6}\right) e^{\lambda_{3} y}, & \\ +b_{5}\left(f_{7} C_{2}+f_{8} C_{4}+f_{9} C_{6}\right) e^{\lambda_{5} y}, & y<0,\end{cases}
\tag{17}
$$

which is equivalent to the method developed by Ding et al. [33]. $C_j\ (j=2,4,6)$ are unknown functions of $s$ to be determined from boundary conditions, and $\lambda_j\ (j=1,2,\dots,6)$ are the roots of the following equation:

$$
X_{1} \lambda^{6}+X_{2} \lambda^{5}+X_{3} \lambda^{4}+X_{4} \lambda^{3}+X_{5} \lambda^{2}+X_{6} \lambda+X_{7}=0,\qquad(18)
$$

with $X_i\ (i=1,2,\dots,7)$ being given in the Appendix. For the materials considered in the current work, three roots $\lambda_{1},\lambda_{3},\lambda_{5}$ of the above equation have positive real parts, while three of them $\lambda_{2},\lambda_{4},\lambda_{6}$ have negative real parts. $a_j,b_j\ (j=1,2,\dots,6)$ and $f_i\ (i=1,2,\dots,9)$ in Eqs. (15)-(17) are

$$
a_{j}=\frac{X_{a j}}{Y_{j}}, \quad b_{j}=\frac{X_{b j}}{Y_{j}}, \quad f_{i}=\frac{\Delta_{i}}{Y},\qquad(19)
$$

where $X_{aj},X_{bj},Y_j\ (j=1,2,\dots,6)$, $\Delta_i\ (i=1,2,\dots,9)$ and $Y$ are given in the Appendix.

As a mathematical model, a crack can be modeled as distributed dislocations. The generalized dislocation density functions for piezoelectric materials are defined as

$$
\psi_{1}(x)=\frac{\partial}{\partial x}\left[u\left(x, 0^{+}\right)-u\left(x, 0^{-}\right)\right],\qquad(20)
$$

$$
\psi_{2}(x)=\frac{\partial}{\partial x}\left[v\left(x, 0^{+}\right)-v\left(x, 0^{-}\right)\right],\qquad(21)
$$

$$
\psi_{3}(x)=\frac{\partial}{\partial x}\left[\Phi\left(x, 0^{+}\right)-\Phi\left(x, 0^{-}\right)\right].\qquad(22)
$$

Applying Fourier transform to Eqs. (20)-(22), $C_2(s),C_4(s)$ and $C_6(s)$ in Eqs. (15)-(17) can be expressed in terms of $\psi_{j}^{*}(s)(j=1,2,3)$, which is the Fourier transform of $\psi_j(x)$ as

$$
C_{2}(s)=\frac{i}{s \Delta(s)}\left[g_{1}(s) \psi_{1}^{*}(s)+g_{2}(s) \psi_{2}^{*}(s)+g_{3}(s) \psi_{3}^{*}(s)\right],\qquad(23)
$$

$$
C_{4}(s)=\frac{i}{s \Delta(s)}\left[g_{4}(s) \psi_{1}^{*}(s)+g_{5}(s) \psi_{2}^{*}(s)+g_{6}(s) \psi_{3}^{*}(s)\right],\qquad(24)
$$

$$
C_{6}(s)=\frac{i}{s \Delta(s)}\left[g_{7}(s) \psi_{1}^{*}(s)+g_{8}(s) \psi_{2}^{*}(s)+g_{9}(s) \psi_{3}^{*}(s)\right],\qquad(25)
$$

with $\Delta(s)$ and $g_i(s)\ (i=1,2,\dots,9)$ being given in the Appendix.

By considering the continuity condition (14) for displacement and electric potential along the crack line and substituting Eqs. (15)-(17) and (23)-(25) into the constitutive equations (4), (5), the stress and electric displacement fields caused by each individual crack can be obtained in the local coordinate system $(x_k,y_k)(k=I,II)$ as

$$
\sigma_{y x}^{k}\left(x_{k}, y_{k}\right)=\frac{1}{2 \pi} \int_{-a_{k}}^{a_{k}} \sum_{j=1}^{3} K_{1 j}^{*}\left(x_{k}, y_{k}, \omega\right) \psi_{j}^{k}(\omega) \mathrm{d} \omega,\qquad(26)
$$

$$
\sigma_{y y}^{k}\left(x_{k}, y_{k}\right)=\frac{1}{2 \pi} \int_{-a_{k}}^{a_{k}} \sum_{j=1}^{3} K_{2 j}^{*}\left(x_{k}, y_{k}, \omega\right) \psi_{j}^{k}(\omega) \mathrm{d} \omega,\qquad(27)
$$

$$
D_{y}^{k}\left(x_{k}, y_{k}\right)=\frac{1}{2 \pi} \int_{-a_{k}}^{a_{k}} \sum_{j=1}^{3} K_{3 j}^{*}\left(x_{k}, y_{k}, \omega\right) \psi_{j}^{k}(\omega) \mathrm{d} \omega,\qquad(28)
$$

where $K_{ij}^{*}$ is given as

$$
K_{i j}^{*}\left(x_{k}, y_{k}, \omega\right)=\left\{\begin{array}{ll}
\int_{-\infty}^{\infty} h_{i j}(s, 0) e^{-i s\left(\omega-x_{k}\right)} \mathrm{d} s, & y_{k}=0, \\
\int_{-\infty}^{\infty} h_{i j}^{+}\left(s, y_{k}\right) e^{-i s\left(\omega-x_{k}\right)} \mathrm{d} s, & y_{k}>0, \\
\int_{-\infty}^{\infty} h_{i j}^{-}\left(s, y_{k}\right) e^{-i s\left(\omega-x_{k}\right)} \mathrm{d} s, & y_{k}<0,
\end{array}\right.\qquad(29)
$$

with $h_{ij},h_{ij}^{+},h_{ij}^{-}\ (i,j=1,2,3)$ being given in the Appendix.

Detailed asymptotic analysis of $h_{ij}^{*}$ (including $h_{ij}, h_{ij}^{+}, h_{ij}^{-}$) indicates that $h_{11}^{*}, h_{22}^{*}, h_{33}^{*}, h_{23}^{*}$ and $h_{32}^{*}$ are odd functions of $s$, while the others are even functions. $h_{11}, h_{22}, h_{33}, h_{23}, h_{32}$ are related to the material gradient and the position of each individual crack. When the position of crack $k(k=I, II)$ is fixed at $y=h_{k}$, they approach to constants when $s$ tends to infinity, i.e.,

$$
\begin{aligned}
& \lim _{|s| \rightarrow \infty} h_{11}(s, 0)=i h_{11}^{0} e^{\alpha h_{k}} \operatorname{sgn}(\mathrm{s}), \lim _{|s| \rightarrow \infty} \mathrm{h}_{22}(\mathrm{~s}, 0)=\mathrm{i} \mathrm{h}_{22}^{0} \mathrm{e}^{\alpha \mathrm{h}_{\mathrm{k}}} \operatorname{sgn}(\mathrm{s}), \\
& \lim _{|s| \rightarrow \infty} h_{33}(s, 0)=i h_{33}^{0} e^{\alpha h_{k}} \operatorname{sgn}(\mathrm{s}), \\
& \lim _{|s| \rightarrow \infty} h_{23}(s, 0)=i h_{23}^{0} e^{\alpha h_{k}} \operatorname{sgn}(\mathrm{s}), \lim _{|s| \rightarrow \infty} \mathrm{h}_{32}(\mathrm{~s}, 0)=\mathrm{i} \mathrm{h}_{32}^{0} \mathrm{e}^{\alpha \mathrm{h}_{\mathrm{k}}} \operatorname{sgn}(\mathrm{s}),
\end{aligned}
$$

while the others approach to zero with increasing $s$.

## 4 Interacting cracks

For convenience, two local coordinate systems $(x_{k}, y_{k})(k=I, II)$ are used to describe the crack position. The position for the center line of crack $k$ is measured vertically from the global coordinate system as $y_{k}=h_{k}(k=I, II)$ as shown in Fig. 1. The horizontal distance between the inner crack tips is $d$. The stresses and electric displacement fields along the $k$th $(k=I, II)$ crack surfaces are composed of two parts, one part is induced by the $k$th crack itself, the second part is induced by the existence of the other crack. By using the superposition technique, the boundary conditions Eqs. (11) and (12) for each crack can be expressed as

$$
\sigma_{y i}^{k}+\sigma_{y i}^{j k}=-\sigma_{y i}^{0}, \quad(i=x, y, j \neq k), \quad\left|x_{k}\right|<a_{k},
$$

$$
D_{y}^{k}+D_{y}^{j k}=-D_{y}^{0}-\kappa \frac{\Phi^{k+}-\Phi^{k-}}{v^{k+}-v^{k-}}, \quad(j \neq k), \quad\left|x_{k}\right|<a_{k},
$$

where $\sigma_{y i}^{j k}, D_{y}^{j k}$ are the stresses and electric displacement fields along the $k$th crack surfaces caused by the $j$th crack.

Separating the singular parts of the kernels in Eqs. (26)-(28), and substituting them into Eqs. (31) and (32), the singular integral equations in the local Cartesian coordinate systems $(x_{k}, y_{k})(k=I, II)$ can be obtained as

$$
\begin{aligned}
-\sigma_{y x}^{0}\left(x_{I}, 0\right)= & \frac{h_{11}^{0} e^{\alpha h_{I}}}{\pi} \int_{-a_{I}}^{a_{I}} \frac{\psi_{1}^{I}(\omega)}{\omega-x_{I}} \mathrm{~d} \omega \\
& +\frac{i}{\pi} \int_{-a_{I}}^{a_{I}} \int_{0}^{\infty}\left(h_{11}(s, 0)-i h_{11}^{0} e^{\alpha h_{I}}\right) \sin s\left(x_{I}-\omega\right) \psi_{1}^{I}(\omega) \mathrm{d} s \mathrm{~d} \omega \\
& +\frac{1}{\pi} \sum_{m=2}^{3} \int_{-a_{I}}^{a_{I}} \int_{0}^{\infty} h_{1 m}(s, 0) \cos s\left(\omega-x_{I}\right) \psi_{m}^{I}(\omega) \mathrm{d} s \mathrm{~d} \omega \\
& +\frac{i}{\pi} \int_{-a_{I I}}^{a_{I I}} \int_{0}^{\infty} h_{11}^{+}(s, h) \sin s\left(\left(x_{I}-X\right)-\omega\right) \psi_{1}^{I I}(\omega) \mathrm{d} s \mathrm{~d} \omega \\
& +\frac{1}{\pi} \sum_{m=2}^{3} \int_{-a_{I I}}^{a_{I I}} \int_{0}^{\infty} h_{1 m}^{+}(s, h) \cos s\left(\omega-\left(x_{I}-X\right)\right) \psi_{m}^{I I}(\omega) \mathrm{d} s \mathrm{~d} \omega,
\end{aligned}
$$

$$
\begin{aligned}
-\sigma_{y y}^{0}\left(x_{I}, 0\right)= & \sum_{m=2}^{3} \frac{h_{2 m}^{0} e^{\alpha h_{I}}}{\pi} \int_{-a_{I}}^{a_{I}} \frac{\psi_{m}^{I}(\omega)}{\omega-x_{I}} \mathrm{~d} \omega, \\
& +\frac{1}{\pi} \int_{-a_{I}}^{a_{I}} \int_{0}^{\infty} h_{21}(s, 0) \cos s\left(\omega-x_{I}\right) \psi_{1}^{I}(\omega) \mathrm{d} s \mathrm{~d} \omega \\
& +\frac{i}{\pi} \sum_{m=2}^{3} \int_{-a_{I}}^{a_{I}} \int_{0}^{\infty}\left(h_{2 m}(s, 0)-i h_{2 m}^{0} e^{\alpha h_{I}}\right) \sin s\left(x_{I}-\omega\right) \psi_{m}^{I}(\omega) \mathrm{d} s \mathrm{~d} \omega \\
& +\frac{1}{\pi} \int_{-a_{I I}}^{a_{I I}} \int_{0}^{\infty} h_{21}^{+}(s, h) \cos s\left(\omega-\left(x_{I}-X\right)\right) \psi_{1}^{I I}(\omega) \mathrm{d} s \mathrm{~d} \omega \\
& +\frac{i}{\pi} \sum_{m=2}^{3} \int_{-a_{I I}}^{a_{I I}} \int_{0}^{\infty} h_{2 m}^{+}(s, h) \sin s\left(\left(x_{I}-X\right)-\omega\right) \psi_{m}^{I I}(\omega) \mathrm{d} s \mathrm{~d} \omega,
\end{aligned}
\tag{34}
$$

$$
\begin{aligned}
-D_{y}^{0}\left(x_{I}, 0\right)-\kappa \frac{\int_{-a_{I}}^{x_{I}} \psi_{3}^{I}(\omega) \mathrm{d} \omega}{\int_{-a_{I}}^{x_{I}} \psi_{2}^{I}(\omega) \mathrm{d} \omega}= & \sum_{m=2}^{3} \frac{h_{3 m}^{0} e^{\alpha h_{I}}}{\pi} \int_{-a_{I}}^{a_{I}} \frac{\psi_{m}^{I}(\omega)}{\omega-x_{I}} \mathrm{~d} \omega+\frac{1}{\pi} \int_{-a_{I}}^{a_{I}} \int_{0}^{\infty} h_{31}(s, 0) \cos s\left(\omega-x_{I}\right) \psi_{1}^{I}(\omega) \mathrm{d} s \mathrm{~d} \omega \\
& +\frac{i}{\pi} \sum_{m=2}^{3} \int_{-a_{I}}^{a_{I}} \int_{0}^{\infty}\left(h_{3 m}(s, 0)-i h_{3 m}^{0} e^{\alpha h_{I}}\right) \sin s\left(x_{I}-\omega\right) \psi_{m}^{I}(\omega) \mathrm{d} s \mathrm{~d} \omega \\
& +\frac{1}{\pi} \int_{-a_{I I}}^{a_{I I}} \int_{0}^{\infty} h_{31}^{+}(s, h) \cos s\left(\omega-\left(x_{I}-X\right)\right) \psi_{1}^{I I}(\omega) \mathrm{d} s \mathrm{~d} \omega \\
& +\frac{i}{\pi} \sum_{m=2}^{3} \int_{-a_{I I}}^{a_{I I}} \int_{0}^{\infty} h_{3 m}^{+}(s, h) \sin s\left(\left(x_{I}-X\right)-\omega\right) \psi_{m}^{I I}(\omega) \mathrm{d} s \mathrm{~d} \omega,
\end{aligned}
\tag{35}
$$

$$
\begin{aligned}
-\sigma_{y x}^{0}\left(x_{I I}, 0\right)= & \frac{h_{11}^{0} e^{\alpha h_{I I}}}{\pi} \int_{-a_{I I}}^{a_{I I}} \frac{\psi_{1}^{I I}(\omega)}{\omega-x_{I I}} \mathrm{~d} \omega \\
& +\frac{i}{\pi} \int_{-a_{I I}}^{a_{I I}} \int_{0}^{\infty}\left(h_{11}(s, 0)-i h_{11}^{0} e^{\alpha h_{I I}}\right) \sin s\left(x_{I I}-\omega\right) \psi_{1}^{I I}(\omega) \mathrm{d} s \mathrm{~d} \omega \\
& +\frac{1}{\pi} \sum_{m=2}^{3} \int_{-a_{I I}}^{a_{I I}} \int_{0}^{\infty} h_{1 m}(s, 0) \cos s\left(\omega-x_{I I}\right) \psi_{m}^{I I}(\omega) \mathrm{d} s \mathrm{~d} \omega \\
& +\frac{i}{\pi} \int_{-a_{I}}^{a_{I}} \int_{0}^{\infty} h_{11}^{-}(s,-h) \sin s\left(\left(x_{I I}+X\right)-\omega\right) \psi_{1}^{I}(\omega) \mathrm{d} s \mathrm{~d} \omega \\
& +\frac{1}{\pi} \sum_{m=2}^{3} \int_{-a_{I}}^{a_{I}} \int_{0}^{\infty} h_{1 m}^{-}(s,-h) \cos s\left(\omega-\left(x_{I I}+X\right)\right) \psi_{m}^{I}(\omega) \mathrm{d} s \mathrm{~d} \omega,
\end{aligned}
\tag{36}
$$

$$
\begin{aligned}
-\sigma_{y y}^{0}\left(x_{I I}, 0\right)= & \sum_{m=2}^{3} \frac{h_{2 m}^{0} e^{\alpha h_{I I}}}{\pi} \int_{-a_{I I}}^{a_{I I}} \frac{\psi_{m}^{I I}(\omega)}{\omega-x_{I I}} \mathrm{~d} \omega \\
& +\frac{1}{\pi} \int_{-a_{I I}}^{a_{I I}} \int_{0}^{\infty} h_{21}(s, 0) \cos s\left(\omega-x_{I I}\right) \psi_{1}^{I I}(\omega) \mathrm{d} s \mathrm{~d} \omega \\
& +\frac{i}{\pi} \sum_{m=2}^{3} \int_{-a_{I I}}^{a_{I I}} \int_{0}^{\infty}\left(h_{2 m}(s, 0)-i h_{2 m}^{0} e^{\alpha h_{I I}}\right) \sin s\left(x_{I I}-\omega\right) \psi_{m}^{I I}(\omega) \mathrm{d} s \mathrm{~d} \omega \\
& +\frac{1}{\pi} \int_{-a_{I}}^{a_{I}} \int_{0}^{\infty} h_{21}^{-}(s,-h) \cos s\left(\omega-\left(x_{I I}+X\right)\right) \psi_{1}^{I}(\omega) \mathrm{d} s \mathrm{~d} \omega \\
& +\frac{i}{\pi} \sum_{m=2}^{3} \int_{-a_{I}}^{a_{I}} \int_{0}^{\infty} h_{2 m}^{-}(s,-h) \sin s\left(\left(x_{I I}+X\right)-\omega\right) \psi_{m}^{I}(\omega) \mathrm{d} s \mathrm{~d} \omega, \quad(37)
\end{aligned}
$$

$$
\begin{aligned}
-D_{y}^{0}\left(x_{I I}, 0\right)-\kappa \frac{\int_{-a_{I I}}^{x_{I I}} \psi_{3}^{I I}(\omega) \mathrm{d} \omega}{\int_{-a_{I I}}^{x_{I I}} \psi_{2}^{I I}(\omega) \mathrm{d} \omega}= & \sum_{m=2}^{3} \frac{h_{3 m}^{0} e^{\alpha h_{I I}}}{\pi} \int_{-a_{I I}}^{a_{I I}} \frac{\psi_{m}^{I I}(\omega)}{\omega-x_{I I}} \mathrm{~d} \omega \\
& +\frac{1}{\pi} \int_{-a_{I I}}^{a_{I I}} \int_{0}^{\infty} h_{31}(s, 0) \cos s\left(\omega-x_{I I}\right) \psi_{1}^{I I}(\omega) \mathrm{d} s \mathrm{~d} \omega \\
& +\frac{i}{\pi} \sum_{m=2}^{3} \int_{-a_{I I}}^{a_{I I}} \int_{0}^{\infty}\left(h_{3 m}(s, 0)-i h_{3 m}^{0} e^{\alpha h_{I I}}\right) \sin s\left(x_{I I}-\omega\right) \psi_{m}^{I I}(\omega) \mathrm{d} s \mathrm{~d} \omega \\
& +\frac{1}{\pi} \int_{-a_{I}}^{a_{I}} \int_{0}^{\infty} h_{31}^{-}(s,-h) \cos s\left(\omega-\left(x_{I I}+X\right)\right) \psi_{1}^{I}(\omega) \mathrm{d} s \mathrm{~d} \omega \\
& +\frac{i}{\pi} \sum_{m=2}^{3} \int_{-a_{I}}^{a_{I}} \int_{0}^{\infty} h_{3 m}^{-}(s,-h) \sin s\left(\left(x_{I I}+X\right)-\omega\right) \psi_{m}^{I}(\omega) \mathrm{d} s \mathrm{~d} \omega, \quad(38)
\end{aligned}
$$

where $X=a_{I}+a_{I I}+d$ and $d$ is positive when the left tip of crack $I I$ is at the right side of the right tip of crack $I$; otherwise, $d$ is negative. $h$ is the total vertical separation distance between two cracks. The integral equations (33)-(38) are characterized by the square root singularity; therefore, the general solutions can be determined by expanding the dislocation density functions $\psi_{1}^{k}(\omega), \psi_{2}^{k}(\omega)$ and $\psi_{3}^{k}(\omega)(k=I, I I)$ as

$$
\psi_{j}^{k}(\omega)=\sum_{l=0}^{\infty} C_{j l}^{k} \frac{T_{l}\left(\omega / a_{k}\right)}{\sqrt{1-\left(\frac{\omega}{a_{k}}\right)^{2}}}, \quad j=1,2,3,
$$

where $T_{l}$ are the Chebyshev polynomials of the first kind and $C_{j l}^{k}(k=I, I I)$ are unknown coefficients. The orthogonality condition of Chebyshev polynomials and the continuity condition for displacement and electric potential Eq. (14) result in $C_{j 0}^{k}=0(k=I, I I)$. Substituting Eq. (39) into Eqs. (33)-(38) and truncating the Chebyshev polynomials to the $N$th term, the following algebraic equations can be obtained by using the properties of Chebyshev polynomials,


$$
\begin{aligned}
-\sigma_{y x}^{0}\left(x_{I j}, 0\right) & =h_{11}^{0} e^{\alpha h_{I}} \sum_{l=1}^{N} C_{1 l}^{I} \frac{\sin \left(l \cos ^{-1} \frac{x_{I j}}{a_{I}}\right)}{\sin \left(\cos ^{-1} \frac{x_{I j}}{a_{I}}\right)} \\
& +a_{I} i \sum_{l=1}^{N} C_{1 l}^{I} \begin{cases}(-1)^{n} \int_{0}^{\infty} J_{l}\left(s a_{I}\right) \sin \left(s x_{I j}\right)\left(h_{11}(s, 0)-i h_{11}^{0} e^{\alpha h_{I}}\right) \mathrm{d} s & l=2 n \\
(-1)^{n+1} \int_{0}^{\infty} J_{l}\left(s a_{I}\right) \cos \left(s x_{I j}\right)\left(h_{11}(s, 0)-i h_{11}^{0} e^{\alpha h_{I}}\right) \mathrm{d} s & l=2 n+1\end{cases} \\
& +a_{I} \sum_{m=2}^{3} \sum_{l=1}^{N} C_{m l}^{I} \begin{cases}(-1)^{n} \int_{0}^{\infty} J_{l}\left(s a_{I}\right) \cos \left(s x_{I j}\right) h_{1 m}(s, 0) \mathrm{d} s & l=2 n \\
(-1)^{n} \int_{0}^{\infty} J_{l}\left(s a_{I}\right) \sin \left(s x_{I j}\right) h_{1 m}(s, 0) \mathrm{d} s & l=2 n+1\end{cases} \\
& +a_{I I} i \sum_{l=1}^{N} C_{1 l}^{I I} \begin{cases}(-1)^{n} \int_{0}^{\infty} J_{l}\left(s a_{I I}\right) \sin \left[s\left(x_{I j}-X\right)\right] h_{11}^{+}(s, h) \mathrm{d} s & l=2 n \\
(-1)^{n+1} \int_{0}^{\infty} J_{l}\left(s a_{I I}\right) \cos \left[s\left(x_{I j}-X\right)\right] h_{11}^{+}(s, h) \mathrm{d} s & l=2 n+1\end{cases} \\
& +a_{I I} \sum_{m=2}^{3} \sum_{l=1}^{N} C_{m l}^{I I} \begin{cases}(-1)^{n} \int_{0}^{\infty} J_{l}\left(s a_{I I}\right) \cos \left[s\left(x_{I j}-X\right)\right] h_{1 m}^{+}(s, h) \mathrm{d} s & l=2 n \\
(-1)^{n} \int_{0}^{\infty} J_{l}\left(s a_{I I}\right) \sin \left[s\left(x_{I j}-X\right)\right] h_{1 m}^{+}(s, h) \mathrm{d} s & l=2 n+1\end{cases}
\end{aligned}
$$

$$
\begin{aligned}
-\sigma_{y y}^{0}\left(x_{I j}, 0\right) & =\sum_{m=2}^{3} h_{2 m}^{0} e^{\alpha h_{I}} \sum_{l=1}^{N} C_{m l}^{I} \frac{\sin \left(l \cos ^{-1} \frac{x_{I j}}{a_{I}}\right)}{\sin \left(\cos ^{-1} \frac{x_{I j}}{a_{I}}\right)} \\
& +a_{I} \sum_{l=1}^{N} C_{1 l}^{I} \begin{cases}(-1)^{n} \int_{0}^{\infty} J_{l}\left(s a_{I}\right) \cos \left(s x_{I j}\right) h_{21}(s, 0) \mathrm{d} s & l=2 n \\
(-1)^{n} \int_{0}^{\infty} J_{l}\left(s a_{I}\right) \sin \left(s x_{I j}\right) h_{21}(s, 0) \mathrm{d} s & l=2 n+1\end{cases} \\
& +a_{I} i \sum_{m=2}^{3} \sum_{l=1}^{N} C_{m l}^{I} \begin{cases}(-1)^{n} \int_{0}^{\infty} J_{l}\left(s a_{I}\right) \sin \left(s x_{I j}\right)\left(h_{2 m}(s, 0)-i h_{2 m}^{0} e^{\alpha h_{I}}\right) \mathrm{d} s & l=2 n \\
(-1)^{n+1} \int_{0}^{\infty} J_{l}\left(s a_{I}\right) \cos \left(s x_{I j}\right)\left(h_{2 m}(s, 0)-i h_{2 m}^{0} e^{\alpha h_{I}}\right) \mathrm{d} s & l=2 n+1\end{cases} \\
& +a_{I I} \sum_{l=1}^{N} C_{1 l}^{I I} \begin{cases}(-1)^{n} \int_{0}^{\infty} J_{l}\left(s a_{I I}\right) \cos \left[s\left(x_{I j}-X\right)\right] h_{21}^{+}(s, h) \mathrm{d} s & l=2 n \\
(-1)^{n} \int_{0}^{\infty} J_{l}\left(s a_{I I}\right) \sin \left[s\left(x_{I j}-X\right)\right] h_{21}^{+}(s, h) \mathrm{d} s & l=2 n+1\end{cases} \\
& +a_{I I} i \sum_{m=2}^{3} \sum_{l=1}^{N} C_{m l}^{I I} \begin{cases}(-1)^{n} \int_{0}^{\infty} J_{l}\left(s a_{I I}\right) \sin \left[s\left(x_{I j}-X\right)\right] h_{2 m}^{+}(s, h) \mathrm{d} s & l=2 n \\
(-1)^{n+1} \int_{0}^{\infty} J_{l}\left(s a_{I I}\right) \cos \left[s\left(x_{I j}-X\right)\right] h_{2 m}^{+}(s, h) \mathrm{d} s & l=2 n+1\end{cases}
\end{aligned}
$$

$$
\begin{aligned}
-D_{y}^{0}\left(x_{I j}, 0\right) & -\kappa \frac{\sum_{l=1}^{N} \frac{C_{3 l}^{I}}{l} \sin \left(l \cos ^{-1} \frac{x_{I j}}{a_{I}}\right)}{\sum_{l=1}^{N} \frac{C_{2 l}^{I}}{l} \sin \left(l \cos ^{-1} \frac{x_{I j}}{a_{I}}\right)}=\sum_{m=2}^{3} h_{3 m}^{0} e^{\alpha h_{I}} \sum_{l=1}^{N} C_{m l}^{I} \frac{\sin \left(l \cos ^{-1} \frac{x_{I j}}{a_{I}}\right)}{\sin \left(\cos ^{-1} \frac{x_{I j}}{a_{I}}\right)} \\
& +a_{I} \sum_{l=1}^{N} C_{1 l}^{I} \begin{cases}(-1)^{n} \int_{0}^{\infty} J_{l}\left(s a_{I}\right) \cos \left(s x_{I j}\right) h_{31}(s, 0) \mathrm{d} s & l=2 n \\
(-1)^{n} \int_{0}^{\infty} J_{l}\left(s a_{I}\right) \sin \left(s x_{I j}\right) h_{31}(s, 0) \mathrm{d} s & l=2 n+1\end{cases} \\
& +a_{I} i \sum_{m=2}^{3} \sum_{l=1}^{N} C_{m l}^{I} \begin{cases}(-1)^{n} \int_{0}^{\infty} J_{l}\left(s a_{I}\right) \sin \left(s x_{I j}\right)\left(h_{3 m}(s, 0)-i h_{3 m}^{0} e^{\alpha h_{I}}\right) \mathrm{d} s & l=2 n \\
(-1)^{n+1} \int_{0}^{\infty} J_{l}\left(s a_{I}\right) \cos \left(s x_{I j}\right)\left(h_{3 m}(s, 0)-i h_{3 m}^{0} e^{\alpha h_{I}}\right) \mathrm{d} s & l=2 n+1\end{cases} \\
& +a_{I I} \sum_{l=1}^{N} C_{1 l}^{I I} \begin{cases}(-1)^{n} \int_{0}^{\infty} J_{l}\left(s a_{I I}\right) \cos \left[s\left(x_{I j}-X\right)\right] h_{31}^{+}(s, h) \mathrm{d} s & l=2 n \\
(-1)^{n} \int_{0}^{\infty} J_{l}\left(s a_{I I}\right) \sin \left[s\left(x_{I j}-X\right)\right] h_{31}^{+}(s, h) \mathrm{d} s & l=2 n+1\end{cases} \\
& +a_{I I} i \sum_{m=2}^{3} \sum_{l=1}^{N} C_{m l}^{I I} \begin{cases}(-1)^{n} \int_{0}^{\infty} J_{l}\left(s a_{I I}\right) \sin \left[s\left(x_{I j}-X\right)\right] h_{3 m}^{+}(s, h) \mathrm{d} s & l=2 n \\
(-1)^{n+1} \int_{0}^{\infty} J_{l}\left(s a_{I I}\right) \cos \left[s\left(x_{I j}-X\right)\right] h_{3 m}^{+}(s, h) \mathrm{d} s & l=2 n+1\end{cases}
\end{aligned}
$$

$$
-\sigma_{y x}^{0}\left(x_{I I j}, 0\right)=h_{11}^{0} e^{\alpha h_{I I}} \sum_{l=1}^{N} C_{1 l}^{I I} \frac{\sin \left(l \cos ^{-1} \frac{x_{I I j}}{a_{I I}}\right)}{\sin \left(\cos ^{-1} \frac{x_{I I j}}{a_{I I}}\right)}
$$

$$
\begin{aligned}
& +a_{I I} i \sum_{l=1}^{N} C_{l l}^{I I}\left\{\begin{array}{l}
(-1)^{n} \int_{0}^{\infty} J_{l}\left(s a_{I I}\right) \sin \left(s x_{I I j}\right)\left(h_{11}(s, 0)-i h_{11}^{0} e^{\alpha h_{I I}}\right) \mathrm{d} s \quad l=2 n \\
(-1)^{n+1} \int_{0}^{\infty} J_{l}\left(s a_{I I}\right) \cos \left(s x_{I I j}\right)\left(h_{11}(s, 0)-i h_{11}^{0} e^{\alpha h_{I I}}\right) \mathrm{d} s \quad l=2 n+1
\end{array}\right. \\
& +a_{I I} \sum_{m=2}^{3} \sum_{l=1}^{N} C_{m l}^{I I}\left\{\begin{array}{l}
(-1)^{n} \int_{0}^{\infty} J_{l}\left(s a_{I I}\right) \cos \left(s x_{I I j}\right) h_{1 m}(s, 0) \mathrm{d} s \quad l=2 n \\
(-1)^{n} \int_{0}^{\infty} J_{l}\left(s a_{I I}\right) \sin \left(s x_{I I j}\right) h_{1 m}(s, 0) \mathrm{d} s \quad l=2 n+1
\end{array}\right. \\
& +a_{I} i \sum_{l=1}^{N} C_{l l}^{I}\left\{\begin{array}{l}
(-1)^{n} \int_{0}^{\infty} J_{l}\left(s a_{I}\right) \sin \left[s\left(x_{I I j}+X\right)\right] h_{11}^{-}(s,-h) \mathrm{d} s \quad l=2 n \\
(-1)^{n+1} \int_{0}^{\infty} J_{l}\left(s a_{I}\right) \cos \left[s\left(x_{I I j}+X\right)\right] h_{11}^{-}(s,-h) \mathrm{d} s \quad l=2 n+1
\end{array}\right. \\
& +a_{I} \sum_{m=2}^{3} \sum_{l=1}^{N} C_{m l}^{I}\left\{\begin{array}{l}
(-1)^{n} \int_{0}^{\infty} J_{l}\left(s a_{I}\right) \cos \left[s\left(x_{I I j}+X\right)\right] h_{1 m}^{-}(s,-h) \mathrm{d} s \quad l=2 n \\
(-1)^{n} \int_{0}^{\infty} J_{l}\left(s a_{I}\right) \sin \left[s\left(x_{I I j}+X\right)\right] h_{1 m}^{-}(s,-h) \mathrm{d} s \quad l=2 n+1
\end{array}\right.
\end{aligned}
$$

$$
\begin{aligned}
& -\sigma_{y y}^{0}\left(x_{I I j}, 0\right)=\sum_{m=2}^{3} h_{2 m}^{0} e^{\alpha h_{I I}} \sum_{l=1}^{N} C_{m l}^{I I} \frac{\sin \left(l \cos ^{-1} \frac{x_{I I j}}{a_{I I}}\right)}{\sin \left(\cos ^{-1} \frac{x_{I I j}}{a_{I I}}\right)} \\
& +a_{I I} \sum_{l=1}^{N} C_{l l}^{I I}\left\{\begin{array}{l}
(-1)^{n} \int_{0}^{\infty} J_{l}\left(s a_{I I}\right) \cos \left(s x_{I I j}\right) h_{21}(s, 0) \mathrm{d} s \quad l=2 n \\
(-1)^{n} \int_{0}^{\infty} J_{l}\left(s a_{I I}\right) \sin \left(s x_{I I j}\right) h_{21}(s, 0) \mathrm{d} s \quad l=2 n+1
\end{array}\right. \\
& +a_{I I} i \sum_{m=2}^{3} \sum_{l=1}^{N} C_{m l}^{I I}\left\{\begin{array}{l}
(-1)^{n} \int_{0}^{\infty} J_{l}\left(s a_{I I}\right) \sin \left(s x_{I I j}\right) \\
\quad \times\left(h_{2 m}(s, 0)-i h_{2 m}^{0} e^{\alpha h_{I I}}\right) \mathrm{d} s \quad l=2 n \\
(-1)^{n+1} \int_{0}^{\infty} J_{l}\left(s a_{I I}\right) \cos \left(s x_{I I j}\right) \\
\quad \times\left(h_{2 m}(s, 0)-i h_{2 m}^{0} e^{\alpha h_{I I}}\right) \mathrm{d} s \quad l=2 n+1
\end{array}\right. \\
& +a_{I} \sum_{l=1}^{N} C_{l l}^{I}\left\{\begin{array}{l}
(-1)^{n} \int_{0}^{\infty} J_{l}\left(s a_{I}\right) \cos \left[s\left(x_{I I j}+X\right)\right] h_{21}^{-}(s,-h) \mathrm{d} s \quad l=2 n \\
(-1)^{n} \int_{0}^{\infty} J_{l}\left(s a_{I}\right) \sin \left[s\left(x_{I I j}+X\right)\right] h_{21}^{-}(s,-h) \mathrm{d} s \quad l=2 n+1
\end{array}\right. \\
& +a_{I} i \sum_{m=2}^{3} \sum_{l=1}^{N} C_{m l}^{I}\left\{\begin{array}{l}
(-1)^{n} \int_{0}^{\infty} J_{l}\left(s a_{I}\right) \sin \left[s\left(x_{I I j}+X\right)\right] h_{2 m}^{-}(s,-h) \mathrm{d} s \quad l=2 n \\
(-1)^{n+1} \int_{0}^{\infty} J_{l}\left(s a_{I}\right) \cos \left[s\left(x_{I I j}+X\right)\right] h_{2 m}^{-}(s,-h) \mathrm{d} s \quad l=2 n+1
\end{array}\right.
\end{aligned}
$$

$$
\begin{aligned}
& -D_{y}^{0}\left(x_{I I j}, 0\right)-\kappa \frac{\sum_{l=1}^{N} \frac{C_{l}^{I I}}{l} \sin \left(l \cos ^{-1} \frac{x_{I I j}}{a_{I I}}\right)}{\sum_{l=1}^{N} \frac{C_{l}^{I I}}{l} \sin \left(l \cos ^{-1} \frac{x_{I I j}}{a_{I I}}\right)}=\sum_{m=2}^{3} h_{3 m}^{0} e^{\alpha h_{I I}} \sum_{l=1}^{N} C_{m l}^{I I} \frac{\sin \left(l \cos ^{-1} \frac{x_{I I j}}{a_{I I}}\right)}{\sin \left(\cos ^{-1} \frac{x_{I I j}}{a_{I I}}\right)} \\
& +a_{I I} \sum_{l=1}^{N} C_{l l}^{I I}\left\{\begin{array}{l}
(-1)^{n} \int_{0}^{\infty} J_{l}\left(s a_{I I}\right) \cos \left(s x_{I I j}\right) h_{31}(s, 0) \mathrm{d} s \quad l=2 n \\
(-1)^{n} \int_{0}^{\infty} J_{l}\left(s a_{I I}\right) \sin \left(s x_{I I j}\right) h_{31}(s, 0) \mathrm{d} s \quad l=2 n+1
\end{array}\right. \\
& +a_{I I} i \sum_{m=2}^{3} \sum_{l=1}^{N} C_{m l}^{I I}\left\{\begin{array}{l}
(-1)^{n} \int_{0}^{\infty} J_{l}\left(s a_{I I}\right) \sin \left(s x_{I I j}\right) \\
\quad \times\left(h_{3 m}(s, 0)-i h_{3 m}^{0} e^{\alpha h_{I I}}\right) \mathrm{d} s \quad l=2 n \\
(-1)^{n+1} \int_{0}^{\infty} J_{l}\left(s a_{I I}\right) \cos \left(s x_{I I j}\right) \\
\quad \times\left(h_{3 m}(s, 0)-i h_{3 m}^{0} e^{\alpha h_{I I}}\right) \mathrm{d} s \quad l=2 n+1
\end{array}\right. \\
& +a_{I} \sum_{l=1}^{N} C_{l l}^{I}\left\{\begin{array}{l}
(-1)^{n} \int_{0}^{\infty} J_{l}\left(s a_{I}\right) \cos \left[s\left(x_{I I j}+X\right)\right] h_{31}^{-}(s,-h) \mathrm{d} s \quad l=2 n \\
(-1)^{n} \int_{0}^{\infty} J_{l}\left(s a_{I}\right) \sin \left[s\left(x_{I I j}+X\right)\right] h_{31}^{-}(s,-h) \mathrm{d} s \quad l=2 n+1
\end{array}\right. \\
& +a_{I} i \sum_{m=2}^{3} \sum_{l=1}^{N} C_{m l}^{I}\left\{\begin{array}{l}
(-1)^{n} \int_{0}^{\infty} J_{l}\left(s a_{I}\right) \sin \left[s\left(x_{I I j}+X\right)\right] h_{3 m}^{-}(s,-h) \mathrm{d} s \quad l=2 n \\
(-1)^{n+1} \int_{0}^{\infty} J_{l}\left(s a_{I}\right) \cos \left[s\left(x_{I I j}+X\right)\right] h_{3 m}^{-}(s,-h) \mathrm{d} s \quad l=2 n+1
\end{array}\right.
\end{aligned}
$$

where $J_{l}$ is the Bessel function of the first kind with $l$th order. To solve Eqs. (40)-(45), these equations are assumed to be satisfied at $N$ collocation points $x_{k j}=a_{k} \cos \frac{j-1}{N-1} \pi \quad(j=1,2, \ldots, N ; k=I, I I)$ along the

surfaces of each crack. The unknown coefficients $C_{1l}^{k}, C_{2l}^{k}, C_{3l}^{k}\ (k=I, II)$ can then be obtained, which will be used to determine the electromechanical fields of the FGPMs with parallel dielectric cracks.

After the stress and electric displacement fields are obtained, the fracture parameters, such as stress and electric displacement intensity factors at the left and right tips of crack $k(k=I, II)$ can be determined as

$$
\left\{\begin{array}{l}
K_{I}^{k L} \\
K_{I}^{k R}
\end{array}\right\}=\sqrt{\pi a_{k}}\left\{\begin{array}{l}
h_{22}^{0} e^{\alpha h_{k}} \sum_{l=1}^{N}(-1)^{l} C_{2 l}^{k}+h_{23}^{0} e^{\alpha h_{k}} \sum_{l=1}^{N}(-1)^{l} C_{3 l}^{k} \\
-\left(h_{22}^{0} e^{\alpha h_{k}} \sum_{l=1}^{N} C_{2 l}^{k}+h_{23}^{0} e^{\alpha h_{k}} \sum_{l=1}^{N} C_{3 l}^{k}\right)
\end{array}\right\},
\tag{46}
$$

$$
\left\{\begin{array}{l}
K_{I I}^{k L} \\
K_{I I}^{k R}
\end{array}\right\}=\sqrt{\pi a_{k}}\left\{\begin{array}{l}
h_{11}^{0} e^{\alpha h_{k}} \sum_{l=1}^{N}(-1)^{l} C_{1 l}^{k} \\
-h_{11}^{0} e^{\alpha h_{k}} \sum_{l=1}^{N} C_{1 l}^{k}
\end{array}\right\},
\tag{47}
$$

$$
\left\{\begin{array}{l}
K_{D}^{k L} \\
K_{D}^{k R}
\end{array}\right\}=\sqrt{\pi a_{k}}\left\{\begin{array}{l}
h_{33}^{0} e^{\alpha h_{k}} \sum_{l=1}^{N}(-1)^{l} C_{3 l}^{k}+h_{32}^{0} e^{\alpha h_{k}} \sum_{l=1}^{N}(-1)^{l} C_{2 l}^{k} \\
-\left(h_{33}^{0} e^{\alpha h_{k}} \sum_{l=1}^{N} C_{3 l}^{k}+h_{32}^{0} e^{\alpha h_{k}} \sum_{l=1}^{N} C_{2 l}^{k}\right)
\end{array}\right\}.
\tag{48}
$$

In addition to these traditional fracture parameters, a $COD$ intensity factor $K_{COD}$ [18], which can be used to describe the opening deformation of the crack surfaces, is also introduced to evaluate the fracture behavior,

$$
\left\{K_{C O D}^{k L}, K_{C O D}^{k R}\right\}=\sqrt{2 a_{k}}\left\{\sum_{l=1}^{N}(-1)^{l} C_{2 l}^{k}, \quad-\sum_{l=1}^{N} C_{2 l}^{k}\right\}.
\tag{49}
$$

## 5 Results and discussion

The current work will only consider the cases where a normal stress and an electric displacement are applied to the medium. In this situation, the crack will open up and the dielectric crack filling and the crack deformation will play an important role in the fracture behavior of the cracked FGPMs. A dielectric crack model filled with air or vacuum (the dielectric permittivity $\kappa=\kappa_{0}=8.85 \times 10^{-12} \mathrm{C} / \mathrm{Vm}$ ) is used for numerical simulation. The material constants $c_{11}^{0}, c_{13}^{0}, c_{33}^{0}, c_{44}^{0}, e_{31}^{0}, e_{33}^{0}, e_{15}^{0}, \epsilon_{11}^{0}, \epsilon_{33}^{0}$ in Eqs. (1) and (2) are taken as those of $P Z T-4$ piezoceramics.

First, we restrict our attention to the effect of crack dimension upon the interaction of parallel cracks in FGPMs. These two parallel cracks are center aligned $(X=0)$, the length of crack $I I$ is fixed at $a_{I I}=1 \mathrm{~mm}$ and the crack positions are measured from the global coordinate system $y=0$ as $h_{I}=-h_{I I}=0.5 a_{I I}$. Due to the symmetry of the problem, the fracture parameters are the same at the left and right tips of both cracks. Thus we only provide the results for the right tips of each individual crack. The medium is subjected to a normal tensile stress $\sigma_{y y}^{0}=20 \mathrm{MPa}$ and an electric displacement $D_{y}^{0}=1 \times 10^{-3} \mathrm{C} / \mathrm{m}^{2}$. Figure 2 shows the variation

![](./images/811832875929305089_2.jpg)

Fig. 2 The variation of normalized mode I stress intensity factor with crack length ratio $a_{I} / a_{I I}$ for center aligned parallel cracks

![](./images/811832875929305089_3.jpg)

Fig. 3 The variation of normalized mode II stress intensity factor with crack length ratio $a_{I}/a_{II}$ for center aligned parallel cracks

of the normalized mode I stress intensity factor $k_{I}=K_{I}/K_{I}^{S}$ for both cracks with the crack length ratio $a_{I}/a_{II}$, where $K_{I}^{S}$ is the mode I stress intensity factor for a single crack problem. *It should be noted that* $K_{I}^{S}$ is position-independent for the current case with specific material constant distribution as shown in Eqs. (1) and (2). *However, this fracture parameter may be position-dependent for a general FGPM. It can be seen from* Fig. 2 that for both homogeneous ($\alpha=0$) and nonhomogeneous materials ($\alpha\neq0$) a shielding effect exists with $k_{I}<1$ for all length ratios, which is similar to the results obtained in [34] for homogenous piezoelectric materials. The shielding effect for crack $I$ decreases with the increase of crack length ratio $a_{I}/a_{II}$, but this effect has the opposite changing tendency with crack length ratio for crack $II$. By comparing the results for the medium with different gradients, it is found that the material gradient has a significant effect on crack interaction. For example, $k_{I}$ decreases with the increase of the material gradient for the upper crack, while $k_{I}$ increases with the increase of the material gradient for the lower crack. For a homogeneous medium, $k_{I}$ for both cracks have the same value when $a_{I}=a_{II}$ due to the symmetry of the problem, and the results are consistent with [34]. However, for a nonhomogeneous medium, the material gradient breaks up this symmetry. Due to the non-symmetry of material properties and crack interaction, mode I and mode II couples and the stress intensity factor for mode II does not vanish. Figure 3 shows the variation of the normalized mode II stress intensity factor $k_{II}=K_{II}/K_{I}^{S}$ at the right tips of crack $I$ and crack $II$ with crack length ratios for different material gradients. It is observed that mode I and mode II coupling effects may be enhanced or impeded with the change of the crack length ratio. This complicated phenomenon results from the combined effect of crack interaction and material gradient upon mode coupling. For a homogeneous medium ($\alpha=0$), this coupling is caused by pure crack interaction and will eventually vanish with the increase of $a_{I}/a_{II}$ for crack $I$ or with the decrease of $a_{I}/a_{II}$ for crack $II$, which is reduced to a single crack problem. It is observed from this figure that for graded material the effect of the material gradient upon the mode I and mode II coupling is very significant as evidenced by the big discrepancy of the curves for different material gradients. For the normalized electric intensity factors $k_{D}$, they have the same changing tendency as $k_{I}$; thus the results are omitted here.

The effect of crack position upon the crack interaction is also investigated. For the case where crack $I$ and crack $II$ are center aligned with the same length $a_{I}=a_{II}=a$ and their positions are measured vertically from the $y$ axis in the global coordinate system as $h_{I}=-h_{II}=h/2$, the normalized electric displacement intensity factor $k_{D}=K_{D}/K_{D}^{S}$ versus crack vertical separation $h$ is plotted in Fig. 4 when the medium is subjected to the same loads as those in Fig. 2. It shows that crack interaction results in a shielding effect with $k_{D}<1$ and the material gradient has a significant effect upon the crack shielding. For the graded material ($\alpha a=0.4$, for example), we can see that the local material property for FGPMs dominates the shielding effect as evidenced by the discrepancy between $k_{D}^{I}$ and $k_{D}^{II}$. Figure 5 demonstrates the mode I and mode II coupling caused by crack interaction and material gradient. Unlike the homogeneous medium, it indicates in this figure that the mode II stress intensity factors $k_{II}$ for these two center aligned parallel cracks in FGPMs are not symmetric. With the increase of crack vertical separation $h$, this coupling effect decreases to a single crack problem with $k_{II}=0$ for a homogeneous medium. The crack position effect upon crack interaction is also examined by the

![](./images/811832875929305089_4.jpg)

Fig. 4 The variation of normalized electric displacement intensity factor with crack separation distance $h/a$ for center aligned parallel cracks

![](./images/811832875929305089_5.jpg)

Fig. 5 The variation of normalized mode II stress intensity factor with crack separation distance $h/a$ for center aligned parallel cracks

horizontal distance $X$ between two crack centers. Figure 6 depicts the variation of the mode I intensity factor normalized by its counterpart value for a single crack in the homogeneous medium at the left and right tips of crack $I$ with $X/a$ when $a_I=a_{II}=a$ and $h=a$. Both amplification and shielding effects can be observed depending on the crack separation distance for homogeneous and nonhomogeneous ($\alpha a=1.0$, for example) media. When these two cracks are center aligned ($X=0$), $k_I^{IL}=k_I^{IR}$. The interacting effect at the inner and outer crack tips are quite different as indicated in this figure, which results in $k_I^{IL}=k_I^{IR}$ for specific crack separation distance $X$ in addition to $X=0$. With the increase of $X/a$, $k_I$ at the two tips of crack are reduced to the same value for the single crack problem. Figure 7 shows the variation of normalized $k_{II}$ with $X/a$ at both tips of crack $I$ for both homogeneous and nonhomogeneous media. Similar to Fig. 6, the mode I and mode II coupling is significantly influenced by the material gradient and crack position.

To see the effect of the dielectric medium upon the fracture behavior of FGPMs with two parallel cracks, the electric intensity factor $K_D$ and COD intensity factor $K_{COD}$ at the right tip of crack I with $X/a$ for different crack models are shown in Figs. 8 and 9. The medium is subjected to the same loads as for Fig. 2, and $a_I=2a_{II}=2mm$, $h=a_{II}$ and the material gradient $\alpha a_{II}=0.8$. By changing the dielectric permittivity $\kappa$ of the medium filling the crack, the transition from permeable to impermeable crack models is clearly demonstrated. For example, with the increase of this permittivity, the curves for both $K_D$ and $K_{COD}$ are much closer to those for the permeable model. It is interesting to note that the results are very sensitive to crack models and

![](./images/811832875929305089_6.jpg)

Fig. 6 The variation of normalized mode I stress intensity factor with crack separation distance $X/a$

![](./images/811832875929305089_7.jpg)

Fig. 7 The variation of normalized mode II stress intensity factor with crack separation distance $X/a$

![](./images/811832875929305089_8.jpg)

Fig. 8 The variation of electric displacement intensity factor $K_D^{IR}$ with $X/a_{II}$ for different crack models

![](./images/811832875929305089_9.jpg)

Fig. 9 The variation of crack opening displacement intensity factor $K_{COD}^{IR}$ with $X/a_{II}$ for different crack models

the results from dielectric models are always between those from impermeable and permeable crack models, which indicate that the dielectric crack model may be more accurate to predict the fracture behavior of cracked FGPMs.

## 6 Conclusions
In this work, the plane problem of two parallel cracks in functionally graded piezoelectric materials with material property varying perpendicular to the crack surfaces is examined. Fourier transforms are used to derive the formulations, and the cracks are modeled as distributed dislocations. Numerical simulations are made to show the influence of crack geometry, crack position, material gradient, and dielectric crack filling on the fracture parameters at the crack tips. It is concluded that the crack geometry, the crack position, and the material gradient have a great effect on the fracture properties of FGPMs. In addition, since the results obtained from the dielectric crack model are always between those from the two traditional crack models, it is concluded that the dielectric crack model may be more accurate in predicting the fracture behavior of FGPMs with multiple cracks.

Acknowledgments This work was supported by Natural Sciences and Engineering Research Council of Canada (NSERC).

## Appendix A
$X_i(i=1,2,\dots,7)$ in Eq. (18) are related to the material properties and are given as

$$
\begin{aligned}
X_1 &= 1-\beta_8\beta_{12}, \quad X_2=3\alpha(1-\beta_8\beta_{12}), \\
X_3 &= s^2(-\beta_{10}-\beta_5+\beta_7\beta_{12}+\beta_8\beta_{11}-\beta_1+\beta_1\beta_8\beta_{12}+\beta_2\beta_6-\beta_2\beta_8\beta_{13}+\beta_3\beta_{13}-\beta_3\beta_6\beta_{12}) \\
&\quad +3\alpha^2(1-\beta_8\beta_{12}), \\
X_4 &= \alpha s^2(-2\beta_5-2\beta_{10}+2\beta_8\beta_{11}+2\beta_7\beta_{12}-2\beta_1+2\beta_1\beta_8\beta_{12}+\beta_2\beta_6+\beta_2\beta_9-\beta_2\beta_8\beta_{13}-\beta_2\beta_8\beta_{14} \\
&\quad +\beta_6-\beta_8\beta_{13}+\beta_3\beta_{14}+\beta_3\beta_{13}-\beta_3\beta_6\beta_{12}-\beta_3\beta_9\beta_{12}+\beta_4\beta_{13}-\beta_4\beta_6\beta_{12})+\alpha^3(1-\beta_8\beta_{12}), \\
X_5 &= s^4(\beta_5\beta_{10}-\beta_7\beta_{11}+\beta_1\beta_{10}+\beta_1\beta_5-\beta_1\beta_7\beta_{12}-\beta_1\beta_8\beta_{11}-\beta_2\beta_6\beta_{10}+\beta_2\beta_7\beta_{13}-\beta_3\beta_5\beta_{13} \quad \text{(A.1)} \\
&\quad +\beta_3\beta_6\beta_{11})+\alpha^2 s^2(-\beta_5-\beta_{10}+\beta_7\beta_{12}+\beta_8\beta_{11}-\beta_1+\beta_1\beta_8\beta_{12}+\beta_2\beta_9-\beta_2\beta_8\beta_{14}+\beta_6+\beta_9 \\
&\quad -\beta_8\beta_{13}-\beta_8\beta_{14}+\beta_3\beta_{14}-\beta_3\beta_9\beta_{12}+\beta_4\beta_{14}+\beta_4\beta_{13}-\beta_4\beta_6\beta_{12}-\beta_4\beta_9\beta_{12}),
\end{aligned}
$$

$$
\begin{aligned}
X_{6}= & \alpha s^{4}\left(\beta_{5} \beta_{10}-\beta_{7} \beta_{11}+\beta_{1} \beta_{5}+\beta_{1} \beta_{10}-\beta_{1} \beta_{7} \beta_{12}-\beta_{1} \beta_{8} \beta_{11}-\beta_{2} \beta_{9} \beta_{10}+\beta_{2} \beta_{7} \beta_{14}-\beta_{6} \beta_{10}\right. \\
& \left.+\beta_{7} \beta_{13}-\beta_{3} \beta_{5} \beta_{14}+\beta_{3} \beta_{9} \beta_{11}-\beta_{4} \beta_{5} \beta_{13}+\beta_{4} \beta_{6} \beta_{11}\right)+\alpha^{3} s^{2}\left(\beta_{9}-\beta_{8} \beta_{14}+\beta_{4} \beta_{14}-\beta_{4} \beta_{9} \beta_{12}\right), \\
X_{7}= & s^{6}\left(\beta_{1} \beta_{7} \beta_{11}-\beta_{1} \beta_{5} \beta_{10}\right)+\alpha^{2} s^{4}\left(\beta_{7} \beta_{14}-\beta_{9} \beta_{10}+\beta_{4} \beta_{9} \beta_{11}-\beta_{4} \beta_{5} \beta_{14}\right),
\end{aligned}
$$

with $\beta_{i}(i=1,2, \ldots, 14)$ being given in Eq. (10). The coefficients $X_{a j}, X_{b j}, Y_{j}(j=1,2, \ldots, 6)$ in Eq. (19) are

$$
\begin{aligned}
X_{a j}= & -i s\left[\left(\beta_{6}-\beta_{8} \beta_{13}\right) \lambda_{j}^{3}+\alpha\left(\beta_{6}+\beta_{9}-\beta_{8} \beta_{13}-\beta_{8} \beta_{14}\right) \lambda_{j}^{2}+\left(-\beta_{6} \beta_{10} s^{2}+\alpha^{2} \beta_{9}+\beta_{7} \beta_{13} s^{2}\right.\right. \\
& \left.\left.-\alpha^{2} \beta_{8} \beta_{14}\right) \lambda_{j}-\alpha \beta_{9} \beta_{10} s^{2}+\alpha \beta_{7} \beta_{14} s^{2}\right], \\
X_{b j}= & -i s\left[\left(\beta_{13}-\beta_{6} \beta_{12}\right) \lambda_{j}^{3}+\alpha\left(\beta_{14}+\beta_{13}-\beta_{6} \beta_{12}-\beta_{9} \beta_{12}\right) \lambda_{j}^{2}+\left(-\beta_{5} \beta_{13} s^{2}+\alpha^{2} \beta_{14}+\beta_{6} \beta_{11} s^{2}\right.\right. \\
& \left.\left.-\alpha^{2} \beta_{9} \beta_{12}\right) \lambda_{j}-\alpha s^{2}\left(\beta_{5} \beta_{14}-\beta_{9} \beta_{11}\right)\right], \\
Y_{j}= & \left(1-\beta_{8} \beta_{12}\right) \lambda_{j}^{4}+2 \alpha\left(1-\beta_{8} \beta_{12}\right) \lambda_{j}^{3}+\left(-\beta_{10} s^{2}-\beta_{5} s^{2}+\alpha^{2}+\beta_{7} \beta_{12} s^{2}+\beta_{8} \beta_{11} s^{2}\right. \\
& \left.-\alpha^{2} \beta_{8} \beta_{12}\right) \lambda_{j}^{2}+\left(-\alpha \beta_{5} s^{2}-\alpha \beta_{10} s^{2}+\alpha \beta_{7} \beta_{12} s^{2}+\alpha \beta_{8} \beta_{11} s^{2}\right) \lambda_{j}+\beta_{5} \beta_{10} s^{4}-\beta_{7} \beta_{11} s^{4},
\end{aligned}
$$

(A.2)

$Y$ and $\Delta_{i}(i=1,2, \ldots, 9)$ in Eq. (19) are given as

$$
\begin{aligned}
Y & =A_{11} A_{22} A_{33}+A_{12} A_{23} A_{31}+A_{13} A_{21} A_{32}-A_{13} A_{22} A_{31}-A_{12} A_{21} A_{33}-A_{11} A_{23} A_{32}, \\
\Delta_{1} & =B_{11} A_{22} A_{33}+B_{31} A_{12} A_{23}+A_{13} A_{32} B_{21}-A_{13} A_{22} B_{31}-A_{12} A_{33} B_{21}-A_{23} A_{32} B_{11}, \\
\Delta_{2} & =B_{12} A_{22} A_{33}+B_{32} A_{12} A_{23}+A_{13} A_{32} B_{22}-A_{13} A_{22} B_{32}-A_{12} A_{33} B_{22}-A_{23} A_{32} B_{12}, \\
\Delta_{3} & =B_{13} A_{22} A_{33}+B_{33} A_{12} A_{23}+A_{13} A_{32} B_{23}-A_{13} A_{22} B_{33}-A_{12} A_{33} B_{23}-A_{23} A_{32} B_{13}, \\
\Delta_{4} & =A_{11} A_{33} B_{21}+A_{23} A_{31} B_{11}+A_{13} A_{21} B_{31}-A_{13} A_{31} B_{21}-A_{21} A_{33} B_{11}-A_{11} A_{23} B_{31} \\
\Delta_{5} & =A_{11} A_{33} B_{22}+A_{23} A_{31} B_{12}+A_{13} A_{21} B_{32}-A_{13} A_{31} B_{22}-A_{21} A_{33} B_{12}-A_{11} A_{23} B_{32}, \\
\Delta_{6} & =A_{11} A_{33} B_{23}+A_{23} A_{31} B_{13}+A_{13} A_{21} B_{33}-A_{13} A_{31} B_{23}-A_{21} A_{33} B_{13}-A_{11} A_{23} B_{33}, \\
\Delta_{7} & =A_{11} A_{22} B_{31}+A_{12} A_{31} B_{21}+A_{21} A_{32} B_{11}-A_{22} A_{31} B_{11}-A_{12} A_{21} B_{31}-A_{11} A_{32} B_{21}, \\
\Delta_{8} & =A_{11} A_{22} B_{32}+A_{12} A_{31} B_{22}+A_{21} A_{32} B_{12}-A_{22} A_{31} B_{12}-A_{12} A_{21} B_{32}-A_{11} A_{32} B_{22}, \\
\Delta_{9} & =A_{11} A_{22} B_{33}+A_{12} A_{31} B_{23}+A_{21} A_{32} B_{13}-A_{22} A_{31} B_{13}-A_{12} A_{21} B_{33}-A_{11} A_{32} B_{23},
\end{aligned}
$$

(A.3)

with

$$
\begin{aligned}
A_{11} & =i s c_{13}+c_{33} a_{1} \lambda_{1}+e_{33} b_{1} \lambda_{1}, & A_{12} & =i s c_{13}+c_{33} a_{3} \lambda_{3}+e_{33} b_{3} \lambda_{3}, \\
A_{13} & =i s c_{13}+c_{33} a_{5} \lambda_{5}+e_{33} b_{5} \lambda_{5}, & A_{21} & =c_{44} \lambda_{1}+i s c_{44} a_{1}+i s e_{15} b_{1}, \\
A_{22} & =c_{44} \lambda_{3}+i s c_{44} a_{3}+i s e_{15} b_{3}, & A_{23} & =c_{44} \lambda_{5}+i s c_{44} a_{5}+i s e_{15} b_{5}, \\
A_{31} & =i s e_{31}+e_{33} a_{1} \lambda_{1}-\epsilon_{33} b_{1} \lambda_{1}, & A_{32} & =i s e_{31}+e_{33} a_{3} \lambda_{3}-\epsilon_{33} b_{3} \lambda_{3}, \\
A_{33} & =i s e_{31}+e_{33} a_{5} \lambda_{5}-\epsilon_{33} b_{5} \lambda_{5}, & B_{11} & =i s c_{13}+c_{33} a_{2} \lambda_{2}+e_{33} b_{2} \lambda_{2}, \\
B_{12} & =i s c_{13}+c_{33} a_{4} \lambda_{4}+e_{33} b_{4} \lambda_{4}, & B_{13} & =i s c_{13}+c_{33} a_{6} \lambda_{6}+e_{33} b_{6} \lambda_{6}, \\
B_{21} & =c_{44} \lambda_{2}+i s c_{44} a_{2}+i s e_{15} b_{2}, & B_{22} & =c_{44} \lambda_{4}+i s c_{44} a_{4}+i s e_{15} b_{4}, \\
B_{23} & =c_{44} \lambda_{6}+i s c_{44} a_{6}+i s e_{15} b_{6}, & B_{31} & =i s e_{31}+e_{33} a_{2} \lambda_{2}-\epsilon_{33} b_{2} \lambda_{2}, \\
B_{32} & =i s e_{31}+e_{33} a_{4} \lambda_{4}-\epsilon_{33} b_{4} \lambda_{4}, & B_{33} & =i s e_{31}+e_{33} a_{6} \lambda_{6}-\epsilon_{33} b_{6} \lambda_{6},
\end{aligned}
$$

(A.4)

$\Delta(s)$ and $g_{i}(s)(i=1,2, \ldots, 9)$ in Eqs. (23)-(25) are given as

$$
\begin{gathered}
\Delta(s)=C_{11} C_{22} C_{33}+C_{12} C_{23} C_{31}+C_{13} C_{21} C_{32}-C_{13} C_{22} C_{31}-C_{12} C_{21} C_{33}-C_{11} C_{23} C_{32} \quad \text { (A.5) } \\
g_{1}(s)=C_{23} C_{32}-C_{22} C_{33}, \quad g_{2}(s)=C_{12} C_{33}-C_{13} C_{32}, \quad g_{3}(s)=C_{13} C_{22}-C_{12} C_{23},
\end{gathered}
$$

$$
\begin{aligned}
& g_{4}(s)=C_{21} C_{33}-C_{23} C_{31}, \quad g_{5}(s)=C_{13} C_{31}-C_{11} C_{33}, \quad g_{6}(s)=C_{11} C_{23}-C_{13} C_{21}, \\
& g_{7}(s)=C_{22} C_{31}-C_{21} C_{32}, \quad g_{8}(s)=C_{11} C_{32}-C_{12} C_{31}, \quad g_{9}(s)=C_{12} C_{21}-C_{11} C_{22},
\end{aligned} \tag{A.6}
$$

with

$$
\begin{aligned}
& C_{11}=1-f_{1}-f_{4}-f_{7}, \quad C_{12}=1-f_{2}-f_{5}-f_{8}, \quad C_{13}=1-f_{3}-f_{6}-f_{9}, \\
& C_{21}=a_{2}-a_{1} f_{1}-a_{3} f_{4}-a_{5} f_{7}, \quad C_{22}=a_{4}-a_{1} f_{2}-a_{3} f_{5}-a_{5} f_{8}, \quad C_{23}=a_{6}-a_{1} f_{3}-a_{3} f_{6}-a_{5} f_{9}, \\
& C_{31}=b_{2}-b_{1} f_{1}-b_{3} f_{4}-b_{5} f_{7}, \quad C_{32}=b_{4}-b_{1} f_{2}-b_{3} f_{5}-b_{5} f_{8}, \quad C_{33}=b_{6}-b_{1} f_{3}-b_{3} f_{6}-b_{5} f_{9}.
\end{aligned} \tag{A.7}
$$

The expressions of $h_{i j}, h_{i j}^{+}, h_{i j}^{-}$in Eq. (29) are given as

$$
h_{1 j}(s, 0)=\frac{i c_{44}}{s \Delta(s)} \sum_{m=1}^{3} \lambda_{2 m} g_{3(m-1)+j}-\frac{c_{44}}{\Delta(s)} \sum_{m=1}^{3} a_{2 m} g_{3(m-1)+j}-\frac{e_{15}}{\Delta(s)} \sum_{m=1}^{3} b_{2 m} g_{3(m-1)+j}, \tag{A.8}
$$

$$
h_{2 j}(s, 0)=-\frac{c_{13}}{\Delta(s)} \sum_{m=1}^{3} g_{3(m-1)+j}+\frac{i c_{33}}{s \Delta(s)} \sum_{m=1}^{3} a_{2 m} \lambda_{2 m} g_{3(m-1)+j}+\frac{i e_{33}}{s \Delta(s)} \sum_{m=1}^{3} b_{2 m} \lambda_{2 m} g_{3(m-1)+j}, \tag{A.9}
$$

$$
h_{3 j}(s, 0)=-\frac{e_{31}}{\Delta(s)} \sum_{m=1}^{3} g_{3(m-1)+j}+\frac{i e_{33}}{s \Delta(s)} \sum_{m=1}^{3} a_{2 m} \lambda_{2 m} g_{3(m-1)+j}-\frac{i \epsilon_{33}}{s \Delta(s)} \sum_{m=1}^{3} b_{2 m} \lambda_{2 m} g_{3(m-1)+j}, \tag{A.10}
$$

$$
\begin{aligned}
h_{1 j}^{+}\left(s, y_{k}\right)=\frac{i c_{44}}{s \Delta(s)} \sum_{m=1}^{3} \lambda_{2 m} g_{3(m-1)+j} e^{\lambda_{2 m} y_{k}}-\frac{c_{44}}{\Delta(s)} \sum_{m=1}^{3} a_{2 m} g_{3(m-1)+j} e^{\lambda_{2 m} y_{k}}-\frac{e_{15}}{\Delta(s)} \sum_{m=1}^{3} b_{2 m} g_{3(m-1)+j} e^{\lambda_{2 m} y_{k}},
\end{aligned} \tag{A.11}
$$

$$
\begin{aligned}
h_{2 j}^{+}\left(s, y_{k}\right)= & -\frac{c_{13}}{\Delta(s)} \sum_{m=1}^{3} g_{3(m-1)+j} e^{\lambda_{2 m} y_{k}}+\frac{i c_{33}}{s \Delta(s)} \sum_{m=1}^{3} a_{2 m} \lambda_{2 m} g_{3(m-1)+j} e^{\lambda_{2 m} y_{k}} \\
& +\frac{i e_{33}}{s \Delta(s)} \sum_{m=1}^{3} b_{2 m} \lambda_{2 m} g_{3(m-1)+j} e^{\lambda_{2 m} y_{k}},
\end{aligned} \tag{A.12}
$$

$$
\begin{aligned}
h_{3 j}^{+}\left(s, y_{k}\right)= & -\frac{e_{31}}{\Delta(s)} \sum_{m=1}^{3} g_{3(m-1)+j} e^{\lambda_{2 m} y_{k}}+\frac{i e_{33}}{s \Delta(s)} \sum_{m=1}^{3} a_{2 m} \lambda_{2 m} g_{3(m-1)+j} e^{\lambda_{2 m} y_{k}} \\
& -\frac{i \epsilon_{33}}{s \Delta(s)} \sum_{m=1}^{3} b_{2 m} \lambda_{2 m} g_{3(m-1)+j} e^{\lambda_{2 m} y_{k}},
\end{aligned} \tag{A.13}
$$

$$
\begin{aligned}
h_{1 j}^{-}\left(s, y_{k}\right)= & \frac{i c_{44}}{s \Delta(s)}\left(\sum_{m=1}^{3} \sum_{n=1}^{3} \lambda_{2 m-1} f_{3(m-1)+n} g_{3(n-1)+j} e^{\lambda_{2 m-1} y_{k}}\right) \\
& -\frac{c_{44}}{\Delta(s)}\left(\sum_{m=1}^{3} \sum_{n=1}^{3} a_{2 m-1} f_{3(m-1)+n} g_{3(n-1)+j} e^{\lambda_{2 m-1} y_{k}}\right) \\
& -\frac{e_{15}}{\Delta(s)}\left(\sum_{m=1}^{3} \sum_{n=1}^{3} b_{2 m-1} f_{3(m-1)+n} g_{3(n-1)+j} e^{\lambda_{2 m-1} y_{k}}\right),
\end{aligned} \tag{A.14}
$$

$$
\begin{aligned}
h_{2 j}^{-}\left(s, y_{k}\right)= & -\frac{c_{13}}{\Delta(s)}\left(\sum_{m=1}^{3} \sum_{n=1}^{3} f_{3(m-1)+n} g_{3(n-1)+j} e^{\lambda_{2 m-1} y_{k}}\right) \\
& +\frac{i c_{33}}{s \Delta(s)}\left(\sum_{m=1}^{3} \sum_{n=1}^{3} a_{2 m-1} \lambda_{2 m-1} f_{3(m-1)+n} g_{3(n-1)+j} e^{\lambda_{2 m-1} y_{k}}\right) \\
& +\frac{i e_{33}}{s \Delta(s)}\left(\sum_{m=1}^{3} \sum_{n=1}^{3} b_{2 m-1} \lambda_{2 m-1} f_{3(m-1)+n} g_{3(n-1)+j} e^{\lambda_{2 m-1} y_{k}}\right),
\end{aligned}
\tag{A.15}
$$

$$
\begin{aligned}
h_{3 j}^{-}\left(s, y_{k}\right)= & -\frac{e_{31}}{\Delta(s)}\left(\sum_{m=1}^{3} \sum_{n=1}^{3} f_{3(m-1)+n} g_{3(n-1)+j} e^{\lambda_{2 m-1} y_{k}}\right) \\
& +\frac{i e_{33}}{s \Delta(s)}\left(\sum_{m=1}^{3} \sum_{n=1}^{3} a_{2 m-1} \lambda_{2 m-1} f_{3(m-1)+n} g_{3(n-1)+j} e^{\lambda_{2 m-1} y_{k}}\right) \\
& -\frac{i \epsilon_{33}}{s \Delta(s)}\left(\sum_{m=1}^{3} \sum_{n=1}^{3} b_{2 m-1} \lambda_{2 m-1} f_{3(m-1)+n} g_{3(n-1)+j} e^{\lambda_{2 m-1} y_{k}}\right).
\end{aligned}
\tag{A.16}
$$

## References

1. Wu, C.M., Kahn, M., Moy, W.: Piezoelectric ceramics with functional gradients: a new application in material design. J. Am. Ceram. Soc. 79, 809–812 (1996)

2. Hudnut, S., Almajid, A., Taya, M.: Functionally gradient piezoelectric bimorph type actuator. Pro. SPIE 3992, 376–386 (2000)

3. Zhu, X.H., Xu, J., Meng, Z.Y., Zhu, J.M., Zhou, S.H., Li, Q., Liu, Z.G., Ming, N.B.: Microdisplacement characteristics and microstructures of functionally graded piezoelectric ceramic actuator. Mater. Des. 21, 561–566 (2000)

4. Takagi, K., Li, J.F., Yokoyama, S., Watanabe, R., Almajid, A., Taya, M.: Design and fabrication of functionally graded PZT/Pt piezoelectric bimorph actuator. Sci. Tech. Adv. Mater. 3, 217–224 (2002)

5. Parton, V.Z.: Fracture mechanics of piezoelectric materials. Acta Astronaut. 3, 671–683 (1976)

6. Deeg, W.F.J.: The analysis of dislocation, crack, and inclusion problems in piezoelectric solids. PhD thesis, Stanford Uni- versity (1980)

7. McMeeking, R.M.: Electrostrictive stresses near crack-like flaws. Z. Angew. Math. Phys. 40, 615–627 (1989)

8. Dunn, M.L.: The effects of crack face boundary conditions on the fracture mechanics of piezoelectric solids. Eng. Fract. Mech. 48, 25–39 (1994)

9. Sosa, H.: Plane problems in piezoelectric media with defects. Int. J. Solids Struct. 28, 491–505 (1991)

10. Sosa, H., Khutoryansky, N.: New developments concerning piezoelectric materials with defects. Int. J. Solids Struct. 33, 3399–3414 (1996)

11. Zhang, T.Y., Tong, P.: Fracture mechanics for a mode III crack in a piezoelectric material. Int. J. Solids Struct. 33, 343–359 (1996)

12. Zhang, T.Y., Qian, C.F., Tong, P.: Linear electro-elastic analysis of a cavity or a crack in a piezoelectric material. Int. J. Solids Struct. 35, 2121–2149 (1998)

13. Parton, V.Z., Kudryavtsev, B.A.: Electromagnetoelasticity: Piezoelectrics and Electrically Conductive Solids. Gordon and Breach Science Publishers, New York (1988)

14. Dascalu, C., Homentcovschi, D.: An intermediate crack model for flaws in piezoelectric solids. Acta Mech. 154, 85–100 (2002)

15. Chiang, C.R., Weng, G.J.: Nonlinear behavior and critical state of a penny-shaped dielectric crack in a piezoelectric solid. J. Appl. Mech. T ASME 74, 852–860 (2007)

16. Hao, T.H., Shen, Z.Y.: A new electric boundary condition of electric fracture mechanics and its applications. Eng. Fract. Mech. 47, 793–802 (1994)

17. Xu, X.L., Rajapakse, R.K.N.D.: On a plane crack in piezoelectric solids. Int. J. Solids Struct. 38, 7643–7658 (2001)

18. Wang, X.D., Jiang, L.Y.: Fracture behaviour of cracks in piezoelectric media with electromechanically coupled boundary conditions. Proc. R. Soc. Lond. A 458, 2545–2560 (2002)

19. Wang, X.D., Jiang, L.Y.: The nonlinear fracture behavior of an arbitrarily oriented dielectric crack in piezoelectric materi- als. Acta Mech. 172, 195–210 (2004)

20. Meguid, S.A., Wang, X.D.: Dynamic antiplane behaviour of interacting cracks in a piezoelectric medium. Int. J. Fract. 91, 391–403 (1998)

21. Zhou, Z.G., Wang, B., Sun, Y.G.: Investigation of the dynamic behavior of two parallel symmetric cracks in piezoelectric materials use of non-local theory. Int. J. Solids Struct. 40, 747–762 (2003)

22. Han, J.J., Chen, Y.H.: Multiple parallel cracks interaction problem in piezoelectric ceramics. Int. J. Solids Struct. 36, 3375–3390 (1999)

23. Han, X.L., Wang, T.C.: Interacting multiple cracks in piezoelectric materials. Int. J. Solids Struct. **36**, 4183-4202 (1999)

24. Wang, X.D., Jiang, L.Y.: Nonlinear behaviour of interacting dielectric cracks in piezoelectric materials. Int. J. Solids Struct. **39**, 585-600 (2002)

25. Zhou, Z.G., Zhang, P.W., Wu, L.Z.: Two parallel limited-permeable mode-I cracks or four parallel limited-permeable mode-I cracks in the piezoelectric materials. Int. J. Solids Struct. **44**, 4184-4205 (2007)

26. Li, C.Y., Weng, G.J.: Yoffe-type moving crack in a functionally graded piezoelectric material. Proc. R. Soc. Lond. A **458**, 381-399 (2002)

27. Li, C.Y., Weng, G.J.: Antiplane crack problem in functionally graded piezoelectric materials. J. Appl. Mech. T. ASME **69**, 481-488 (2002)

28. Ma, L., Wu, L.Z., Zhou, Z.G., Guo, L.C., Shi, L.P.: Scattering of harmonic anti-plane shear waves by two collinear cracks in functionally graded piezoelectric materials. Eur. J. Mech. A Solid **23**, 633-643 (2004)

29. Zhou, Z.G., Wu, L.Z.: Non-local theory solution for the anti-plane shear of two collinear permeable cracks in functionally graded piezoelectric materials. Int. J. Eng. Sci. **44**, 1366-1379 (2006)

30. Zhang, P.W., Zhou, Z.G., Chen, Z.T.: Basic solution of two parallel mode-I permeable cracks in functionally graded piezo- electric materials. Arch. Appl. Mech. **78**, 411-430 (2008)

31. Zhou, Z.G., Chen, Z.T.: The interaction of two parallel Mode-I limited-permeable cracks in a functionally graded piezo- electric material. Eur. J. Mech. A Solid **27**, 824-846 (2008)

32. Konda, N., Erdogan, F.: The mixed mode crack problem in a nonhomogeneous elastic medium. Eng. Fract. Mech. **47**, 533-545 (1994)

33. Ding, H.J., Chen, B., Liang, J.: General solutions for coupled equations for piezoelectric media. Int. J. Solids. Struct. **33**, 2283-2298 (1996)

34. Wang, X.D., Jiang, L.Y.: Coupled behaviour of interacting dielectric cracks in piezoelectric materials. Int. J. Fract. **132**, 115-133 (2005)