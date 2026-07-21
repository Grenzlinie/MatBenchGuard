**An efficient coupled layerwise theory for static analysis of piezoelectric sandwich beams**

S. Kapuria, P. C. Dumir, A. Ahmed

Summary An efficient one-dimensional model is developed for the statics of piezoelectric sandwich beams. Third-order zigzag approximation is used for axial displacement, and the potential is approximated as piecewise linear. The displacement field is expressed in terms of three primary displacement variables and the electric potential variables by satisfying the conditions of zero transverse shear stress at the top and bottom and its continuity at layer interfaces. The deflection field accounts for the piezoelectric transverse normal strain. The governing equations are derived using a variational principle. The present results agree very well with the exact solution for thin and thick highly inhomogeneous simply supported hybrid sandwich beams. The developed theory can accurately model open and closed circuit boundary conditions.

Keywords Smart material, Sandwich beam, Piezoelectricity, Coupled theory, Static, Layer composite laminate

## 1 Introduction
Composite laminates and sandwich structures with some piezoelectric layers, acting as sensors and actuators to achieve desired control, form part of a new generation of adaptive structures. Sandwich beams have high ratio of flexural stiffness to weight resulting in lower deflection, higher buckling load and higher natural frequencies compared to beams of other constructions. Piezoelectric layers are incorporated in sandwich beams for active control. Sandwich structures offer advantage of placement of the electrodes for the piezoelectric layers. A review of three-dimensional (3D) continuum-based approaches, 2D theories for plates and shells and 1D theories for beams, along with their comparative study for plates under static loading, has been presented in [1]. Analytical 3D solutions are available only for some specific shapes and boundary conditions, [2, 3]. The 3D finite element (FE) analysis, [4], results in large problem size which may become computationally costly for practical dynamics and control problems. Hence, efficient accurate electromechanical coupled 2D plate and 1D beam models are required without too much loss of accuracy compared to 3D models. Early works used elastic beam models, [5–7], with effective forces and moments due to induced strain of actuators. A discrete layer theory with layerwise approximation of displacements was developed for elastic laminated beams with induced actuation strain in [8]. Classical laminate theory (CLT), [9], first-order shear deformation theory (FSDT), [10], and the refined third-order theory, [11, 12] have been applied without electromechanical coupling to hybrid beams and plates. Coupled CLT, FSDT, [13–15], and third-order, [16, 17], solutions for hybrid beams and plates including the charge equation of electrostatics and electromechanical coupling have been reported. In [18], coupled discrete layer theory (DLT) was presented using layerwise approximation for displacement and potential, which yields accurate results for thin and thick beams. However, it is expensive for practical problems since the number of displacement unknowns depends on the

Received 18 April 2002; accepted for publication 19 November 2002

S. Kapuria, P. C. Dumir (⊗), A. Ahmed
Applied Mechanics Deptt., I.I.T. Delhi,
New Delhi-110016, India
e-mail: pcd@am.iitd.ernet.in

The first author is grateful to DST, Government of India, for financial support for this work.

number of sublayers. Paper [19] has presented a coupled DLT for plates with layerwise linear zig-zag approximation for axial displacement and a quadratic one for transverse shear stresses and potential. The axial electric field has been neglected and the constitutive equation for shear stresses has been satisfied only approximately. Except for the coupled DLT, [18], in which the transverse displacement is also taken as piecewise linear, no other 2D theory discussed aboveconsiders the piezoelectric transverse normal strain induced due to piezoelectricity through $d_{33}$  coefficient, which has been observed to have considerable effect on the response, especially for electrical load, [1]. Paper [20] has presented a coupled DLT for a hybrid beam, using a third- order zig-zag approximation for the axial displacement with a sublayerwise linear approxi- mation of the potential $\phi$ . The conditions of zero transverse shear stress $\tau_{z x}$ at the top and bottom surfaces and the conditions of continuity of $\tau_{z x}$ at layer interfaces have been enforced by neglecting the explicit contribution of $\phi$ . The model considers both the axial and transverse electric fields and includes the transverse piezoelectric strain from $d_{33}$ coefficient. There are only three displacement unknowns in the theory which equal in number to the ones used in FSDT. This DLT has the computational advantage of an equivalent single layer (ESL) theory and yet yields very accurate through-the-thickness variations of displacements, electric field, inplane stresses and transverse shear stress.

The present work extends the results of [20] by including the explicit contribution of $\phi$ in the conditions imposed on $\tau_{z x}$ . The coupled equations of stress and charge equilibrium and boundary conditions for the developed model are derived using a variational principle. This theory is assessed by comparison of an analytical solution for simply supported hybrid beam under electromechanical load, with the exact 3D piezoelastic solution and uncoupled FSDT solution. For this purpose, highly inhomogeneous layups of a test case of a six-layer hybrid beam, a four-layer sandwich beam and a two-layer piezoelectric beam are considered. The accuracy of the theory is checked for mechanical and electrical loads at different electrical conditions for thin and thick beams as also for thin and thick piezoelectric layers.

## 2 Formulation of layerwise statical theory
Consider a hybrid beam (Fig. 1) with L orthotropic plys, having rectangular section of width b, depth h and length a with centroidal axis x and loaded transversely on the bottom surface $z=z_{0}=-h / 2$ and the top surface $z=z_{L}=h / 2$ with no variation along the width b. Some of the layers can be piezoelectric with class mm2 symmetry and poling along the thickness axis z. The axis along the width is y. The k-th ply from the bottom has bottom surface at $z=z_{k-1}$ and its material symmetry direction 1 is at an angle $\theta_{k}$ to x-axis. The reference plane z=0 either passes through or is the bottom surface of the $k_{0}$ -th layer. For a beam with small width, the usual assumptions for mathematical simplification of 1D model made by other researchers,[8, 15, 21], which are retained in the present theory, are: assume plane state of stress $(\sigma_{y}=\tau_{y z}=\tau_{x y}=0)$ , neglect transverse normal stress $(\sigma_{z} \simeq 0)$ and assume the axial and transverse displacements u, w and electric potential $\phi$ to be independent of $y(\Rightarrow$ electric field component $E_{y}=-\phi_{, y}=0)$ . The strain-displacement and electric field-potential relations for directions x, z are

$$\varepsilon_{x}=u_{, x}, \quad \varepsilon_{z}=w_{, z}, \quad \gamma_{z x}=u_{, z}+w_{, x} ; \quad E_{x}=-\phi_{, x}, \quad E_{z}=-\phi_{, z},\quad (1)$$

![](./images/812376026230292481_1.jpg)

Fig. 1. Geometry of a hybrid beam

where a subscript comma denotes differentiation. Unlike most other studies, $E_x$ is not considered as zero, since it can be induced by the piezoelectric coupling: With these assumptions, the general 3D linear constitutive equations for stresses and electric displacements $D_x, D_z$ reduce to, [20],

$$
\begin{aligned}
\sigma_{x} & =\hat{Q}_{11} \varepsilon_{x}-\hat{e}_{31} E_{z}=\hat{Q}_{11} u_{, x}+\hat{e}_{31} \phi_{, z}, \\
\tau_{z x} & =\hat{Q}_{55} \gamma_{z x}-\hat{e}_{15} E_{x}=\hat{Q}_{55}\left(u_{, z}+w_{, x}\right)+\hat{e}_{15} \phi_{, x}, \\
D_{x} & =\hat{e}_{15} \gamma_{z x}+\hat{\eta}_{11} E_{x}=\hat{e}_{15}\left(u_{, z}+w_{, x}\right)-\hat{\eta}_{11} \phi_{, x}, \\
D_{z} & =\hat{e}_{31} \varepsilon_{x}+\hat{\eta}_{33} E_{z}=\hat{e}_{31} u_{, x}-\hat{\eta}_{33} \phi_{, z},
\end{aligned} \tag{2}
$$

e.g., for $\theta_{k}=0$:

$$\hat{Q}_{11}=Y_{x}, \hat{Q}_{55}=G_{z x}, \hat{e}_{31}=d_{31} \hat{Q}_{11}, \hat{e}_{15}=d_{15} \hat{Q}_{55}, \hat{\eta}_{11}=\epsilon_{11}-d_{15} \hat{e}_{15}, \hat{\eta}_{33}=\epsilon_{33}-d_{31} \hat{e}_{31}$$

with Young's modulus $Y_{x}$, shear modulus $G_{z x}$, piezoelectric strain constants $d_{i j}$ and dielectric constants $\epsilon_{i j}$.

The potential field is assumed as piecewise linear between $n_{\phi}$ points $z_{\phi}^{j}$ across the thickness $h$, [20],

$$\phi(x, z)=\Psi_{\phi}^{j}(z) \phi^{j}(x), \tag{3}$$

where

$$\phi^{j}(x)=\phi\left(x, z_{\phi}^{j}\right),$$

and $\Psi_{\phi}^{j}(z)$ are linear interpolation functions for $\phi$. Summation convention is used with summation index $j$ and the summation index $j$'s (see later) taking values $1,2, \ldots, n_{\phi}$, where $n_{\phi}$ can differ from $L$ and is determined by the required accuracy of $\phi$. This enables effective modelling of the heterogeneity in $\phi$ induced by piezoelectric sensor and actuator layers. In the constitutive equation

$$\varepsilon_{z}=-\frac{v_{x z} \sigma_{x}}{E_{x}}+d_{33} E_{z} \simeq d_{33} E_{z},$$

the contribution of the first term is neglected as in elastic beam theory. On integration, an approximation for $w$ is obtained as

$$w(x, z)=w_{0}(x)-\bar{\Psi}_{\phi}^{j}(z) \phi^{j}(x), \tag{4}$$

where

$$\bar{\Psi}_{\phi}^{j}(z)=\int_{0}^{z} d_{33} \Psi_{\phi, z}^{j}(z) d z$$

is a piecewise linear function. The axial displacement is assumed, [20], to be a combination of a third-order variation across the thickness with a layerwise linear variation. For the $k$-th layer, $u$ is assumed as

$$u(x, z)=u_{k}(x)+z \psi_{k}^{*}(x)+z^{2} \xi(x)+z^{3} \eta(x). \tag{5}$$

Using Eqs. (2), (4) and (5) yields

$$\tau_{z x}=\hat{Q}_{55}^{k}\left[\psi_{k}^{*}+w_{0, x}+2 z \xi+3 z^{2} \eta-\bar{\Psi}_{\phi}^{j}(z) \phi_{, x}^{j}\right]+\hat{e}_{15}^{k} \Psi_{\phi}^{j} \phi_{, x}^{j}. \tag{6}$$

Denoting $\psi_{k}(x)=\psi_{k}^{*}+w_{0, x}$ for simplicity, Eqs. (5) and (6) yield

$$
u(x, z)=u_{k}(x)-z w_{0, x}(x)+z \psi_{k}(x)+z^{2} \xi(x)+z^{3} \eta(x),\tag{7}
$$

$$
\tau_{z x}=\hat{Q}_{55}^{k}\left(\psi_{k}+2 z \xi+3 z^{2} \eta\right)+\left[\hat{e}_{15}^{k} \Psi_{\phi}^{j}(z)-\hat{Q}_{55}^{k} \bar{\Psi}_{\phi}^{j}(z)\right] \phi_{, x}^{j}.\tag{8}
$$

For the $k_0$-th layer denote
$$
u_{0}(x)=u_{k_{0}}(x)=u(x, 0), \quad \psi_{0}(x)=\psi_{k_{0}}.
$$

The functions $u_{k}, \psi_{k}, \xi, \eta$ are expressed in terms of $u_{0}$ and $\psi_{0}$ using the $(k-1)$ conditions each for the continuity of $\tau_{z x}$ and $u$ at the layer interfaces and the two shear traction-free conditions $\tau_{z x}=0$ at the top and the bottom surfaces at $z=z_{0}, z_{L}$. The continuity of $\tau_{z x}$ at interface $z=z_{i-1}$ between layers $i$ and $i-1$ yields
$$
\begin{aligned}
& \hat{Q}_{55}^{i}\left[\psi_{i}+2 z_{i-1} \xi+3 z_{i-1}^{2} \eta\right]+\left[\hat{e}_{15}^{i} \Psi_{\phi}^{j}\left(z_{i-1}\right)-Q_{55}^{i} \bar{\Psi}_{\phi}^{j}\left(z_{i-1}\right)\right] \phi_{, x}^{j} \\
& \quad=\hat{Q}_{55}^{i-1}\left[\psi_{i-1}+2 z_{i-1} \xi+3 z_{i-1}^{2} \eta\right]+\left[\hat{e}_{15}^{i-1} \Psi_{\phi}^{j}\left(z_{i-1}\right)-Q_{55}^{i-1} \bar{\Psi}_{\phi}^{j}\left(z_{i-1}\right)\right] \phi_{, x}^{j}.\tag{9}
\end{aligned}
$$

Equation (9) is written in the following recursive form so that the solution of $\psi_{i}, \xi, \eta$ is easily tractable:
$$
\begin{aligned}
& \hat{Q}_{55}^{i}\left[\psi_{i}+2 z_{i} \xi+3 z_{i}^{2} \eta\right]+\left[\hat{e}_{15}^{i} \Psi_{\phi}^{j}\left(z_{i}\right)-\hat{Q}_{55}^{i} \bar{\Psi}_{\phi}^{j}\left(z_{i}\right)\right] \phi_{, x}^{j} \\
& =\hat{Q}_{55}^{i-1}\left[\psi_{i-1}+2 z_{i-1} \xi+3 z_{i-1}^{2} \eta\right]+\left[\hat{e}_{15}^{i-1} \Psi_{\phi}^{j}\left(z_{i-1}\right)-\hat{Q}_{55}^{i-1} \bar{\Psi}_{\phi}^{j}\left(z_{i-1}\right)\right] \phi_{, x}^{j}+2 \hat{Q}_{55}^{i}\left(z_{i}-z_{i-1}\right) \xi \\
& \quad+3 \hat{Q}_{55}^{i}\left(z_{i}^{2}-z_{i-1}^{2}\right) \eta+\left[\hat{e}_{15}^{i}\left\{\Psi_{\phi}^{j}\left(z_{i}\right)-\Psi_{\phi}^{j}\left(z_{i-1}\right)\right\}-\hat{Q}_{55}^{i}\left\{\bar{\Psi}_{\phi}^{j}\left(z_{i}\right)-\bar{\Psi}_{\phi}^{j}\left(z_{i-1}\right)\right\}\right] \phi_{, x}^{j}.\tag{10}
\end{aligned}
$$

Using Eq. (8), the conditions $\tau_{z x}(x, z_{0})=0$ can also be written in the above pattern as
$$
\begin{aligned}
& \hat{Q}_{55}^{1}\left[\psi_{1}+2 z_{1} \xi+3 z_{1}^{2} \eta\right]+\left[\hat{e}_{15}^{1} \Psi_{\phi}^{j}\left(z_{1}\right)-\hat{Q}_{55}^{1} \bar{\Psi}_{\phi}^{j}\left(z_{1}\right)\right] \phi_{, x}^{j} \\
& \quad=2 \hat{Q}_{55}^{1}\left(z_{1}-z_{0}\right) \xi+3 \hat{Q}_{55}^{1}\left(z_{1}^{2}-z_{0}^{2}\right) \eta+\left[\hat{e}_{15}^{1}\left\{\Psi_{\phi}^{j}\left(z_{1}\right)-\Psi_{\phi}^{j}\left(z_{0}\right)\right\}\right. \\
& \left.\quad-\hat{Q}_{55}^{1}\left\{\bar{\Psi}_{\phi}^{j}\left(z_{1}\right)-\bar{\Psi}_{\phi}^{j}\left(z_{0}\right)\right\}\right] \phi_{, x}^{j}.\tag{11}
\end{aligned}
$$

Adding Eqs. (11) and (10) for $i=2,3,\dots,k$ yields
$$
\begin{aligned}
& \hat{Q}_{55}^{k}\left(\psi_{k}+2 z_{k} \xi+3 z_{k}^{2} \eta\right)+\left[\hat{e}_{15}^{k} \Psi_{\phi}^{j}\left(z_{k}\right)-\hat{Q}_{55}^{k} \bar{\Psi}_{\phi}^{j}\left(z_{k}\right)\right] \phi_{, x}^{j} \\
& \quad=2 C_{1}^{k} \xi+6 C_{2}^{k} \eta+C_{3 j}^{k} \phi_{, x}^{j}, \quad k=2, \ldots, L,\tag{12}
\end{aligned}
$$

where
$$
\begin{aligned}
C_{1}^{k} & =\sum_{i=1}^{k} Q_{55}^{i}\left(z_{i}-z_{i-1}\right), \quad C_{2}^{k}=\frac{1}{2} \sum_{i=1}^{k} Q_{55}^{i}\left(z_{i}^{2}-z_{i-1}^{2}\right), \\
C_{3 j}^{k} & =\sum_{i=1}^{k}\left[\hat{e}_{15}^{i}\left\{\Psi_{\phi}^{j}\left(z_{i}\right)-\Psi_{\phi}^{j}\left(z_{i-1}\right)\right\}-\hat{Q}_{55}^{i}\left\{\bar{\Psi}_{\phi}^{j}\left(z_{i}\right)-\bar{\Psi}_{\phi}^{j}\left(z_{i-1}\right)\right\}\right].
\end{aligned}\tag{13}
$$

Using Eq. (8), the condition $\tau_{z x}(x, z_{L})=0$, can be written as
$$
\hat{Q}_{55}^{L}\left[\psi_{L}+2 z_{L} \xi+3 z_{L}^{2} \eta\right]+\left[\hat{e}_{15}^{L} \Psi_{\phi}^{j}\left(z_{L}\right)-\hat{Q}_{55}^{L} \bar{\Psi}_{\phi}^{j}\left(z_{L}\right)\right] \phi_{, x}^{j}=0.\tag{14}
$$

Eliminating $\psi_{L}$ from Eqs. (14) and (12) for $k=L$, and rewriting Eq. (11) yields
$$
2 C_{1}^{L} \xi+6 C_{2}^{L} \eta=-C_{3 j}^{L} \phi_{, x}^{j}, \quad 2 z_{0} \xi+3 z_{0}^{2} \eta=C_{5}^{j} \phi_{, x}^{j}-\psi_{1},\tag{15}
$$

where

$$
C_{5}^{j}=\bar{\Psi}_{\phi}^{j}\left(z_{0}\right)-\frac{\hat{e}_{15}^{1} \Psi_{\phi}^{j}\left(z_{0}\right)}{\hat{Q}_{55}^{1}},
$$

The solution of $\xi, \eta$ from Eq. (15) is
$$
\xi=R_{3} \psi_{1}+R_{5}^{j} \phi_{, x}^{j}, \quad \eta=R_{4} \psi_{1}+R_{6}^{j} \phi_{, x}^{j},
\tag{16}
$$
where
$$
R_{3}=\frac{4 C_{2}^{L}}{\Delta}, R_{4}=-\frac{4 C_{2}^{L}}{3 \Delta}, R_{5}^{j}=-\frac{2 z_{0}^{2} C_{3 j}^{L}+4 C_{2}^{L} C_{5}^{j}}{\Delta}, R_{6}^{j}=\frac{4 z_{0} C_{3 j}^{L}+4 C_{1}^{L} C_{5}^{j}}{3 \Delta},
$$
with
$$
\Delta=4 z_{0}^{2} C_{1}^{L}-8 z_{0} C_{2}^{L}.
$$

Substituting $\xi, \eta$ from Eq. (16) into Eq. (12) yields
$$
\psi_{k}=R_{2}^{k} \psi_{1}+R_{j 1}^{k} \phi_{, x}^{j}
\tag{17}
$$
where
$$
R_{2}^{k}=a_{1}^{k} R_{3}+a_{2}^{k} R_{4}, R_{j 1}^{k}=a_{1}^{k} R_{5}^{j}+a_{2}^{k} R_{6}^{j}+\frac{C_{3 j}^{k}-\hat{e}_{15}^{k} \Psi_{\phi}^{j}\left(z_{k}\right)}{\hat{Q}_{55}^{k}}+\bar{\Psi}_{\phi}^{j}\left(z_{k}\right)
$$
with
$$
a_{1}^{k}=2\left(\frac{C_{1}^{k}}{\hat{Q}_{55}^{k}}-z_{k}\right), \quad a_{2}^{k}=3\left(\frac{2 C_{2}^{k}}{\hat{Q}_{55}^{k}}-z_{k}^{2}\right).
$$

The continuity of $u$ between layers $i$ and $i-1$, i.e. $u_{i}+z_{i-1} \psi_{i}=u_{i-1}+z_{i-1} \psi_{i-1}$, which yields using Eq. (17)
$$
u_{i}=u_{i-1}+z_{i-1}\left[\left(R_{2}^{i-1}-R_{2}^{i}\right) \psi_{1}+\left(R_{j 1}^{i-1}-R_{j 1}^{i}\right) \phi_{, x}^{j}\right], \quad i=2, \ldots, L.
\tag{18}
$$

Adding Eqs. (18) for $i=2$ to $k$ yields $u_{k}$ in terms of $u_{1}$
$$
u_{k}=u_{1}+\bar{R}_{2}^{k} \psi_{1}+\bar{R}_{j 1}^{k} \phi_{, x}^{j},
\tag{19}
$$
where
$$
\bar{R}_{2}^{k}=\sum_{i=2}^{k} z_{i-1}\left(R_{2}^{i-1}-R_{2}^{i}\right), \bar{R}_{j 1}^{k}=\sum_{i=2}^{k} z_{i-1}\left(R_{j 1}^{i-1}-R_{j 1}^{i}\right).
$$

Equations (19) and (17) yield for the $k_{0}$-th layer
$$
\begin{aligned}
& u_{0}(x)=u_{k_{0}}(x)=u_{1}+\bar{R}_{2}^{k_{0}} \psi_{1}+\bar{R}_{j 1}^{k_{0}} \phi_{, x}^{j}, \\
& \psi_{0}(x)=\psi_{k_{0}}(x)=R_{2}^{k_{0}} \psi_{1}+R_{j 1}^{k_{0}} \phi_{, x}^{j}.
\end{aligned}
\tag{20}
$$

Substituting $\xi, \eta$ from Eq. (16), $u_{k}$ from Eq. (19) with $u_{1}$ from Eq. $(20)_{1}$ and $\psi_{k}$ from Eq. (17) in Eq. (7) yields
$$
u(x, z)=u_{0}(x)-z w_{0, x}(x)+R_{k}(z) \psi_{1}(x)+R_{k \phi}^{j}(z) \phi_{, x}^{j},
\tag{21}
$$

where

$$
R_{k}(z)=R_{1}^{k}+z R_{2}^{k}+z^{2} R_{3}+z^{3} R_{4}, \quad R_{k \phi}^{j}(z)=R_{1}^{k j}+z R_{j 1}^{k}+z^{2} R_{5}^{j}+z^{3} R_{6}^{j}
$$

with

$$
R_{1}^{k}=\bar{R}_{2}^{k}-\bar{R}_{2}^{k_{0}}, \quad R_{1}^{k j}=\bar{R}_{j 1}^{k}-\bar{R}_{j 1}^{k_{0}}.
$$

Substituting $\psi_{1}$ in terms of $\psi_{0}$ from Eq. (20) $)_{2}$ into Eq. (21) yields the expression of $u$ as

$$
u(x, z)=u_{0}(x)-z w_{0, x}(x)+R^{k}(z) \psi_{0}(x)+R^{k j}(z) \phi_{, x}^{j},
$$

where

$$
R^{k}(z)=\hat{R}_{1}^{k}+z \hat{R}_{2}^{k}+z^{2} \hat{R}_{3}+z^{3} \hat{R}_{4}, \quad R^{k j}(z)=\hat{R}_{1}^{k j}+z \hat{R}_{j 1}^{k}+z^{2} \hat{R}_{5}^{j}+z^{3} \hat{R}_{6}^{j},
$$

with

$$
\begin{aligned}
& \left(\hat{R}_{1}^{k}, \hat{R}_{2}^{k}, \hat{R}_{3}^{k}, \hat{R}_{4}^{k}\right)=\left(R_{1}^{k}, R_{2}^{k}, R_{3}^{k}, R_{4}^{k}\right)\left(R_{2}^{k_{0}}\right)^{-1}, \quad \hat{R}_{1}^{k j}=R_{1}^{k j}-\hat{R}_{1}^{k} R_{j 1}^{k_{0}}, \\
& \hat{R}_{j 1}^{k}=R_{j 1}^{k}-\hat{R}_{2}^{k} R_{j 1}^{k_{0}}, \quad \hat{R}_{5}^{j}=R_{5}^{j}-\hat{R}_{3} R_{j 1}^{k_{0}}, \quad \hat{R}_{6}^{j}=R_{6}^{j}-\hat{R}_{4} R_{j 1}^{k_{0}},
\end{aligned}
$$

Thus $\phi, w, u$ are expressed by Eqs. (3), (4) and (22) in terms of the primary variables $u_{0}, w_{0}, \psi_{0}$ and $\phi^{j}$.

The field equations and the variationally consistent boundary conditions are formulated using the following variational principle for piezoelectric media:

$$
\int_{V}\left(-\sigma_{i j} \delta \varepsilon_{i j}-D_{i} \delta \phi_{, i}\right) \mathrm{d} V+\int_{\Gamma}\left(T_{i}^{n} \delta u_{i}+D_{n} \delta \phi\right) \mathrm{d} \Gamma-\sum_{i=1}^{\bar{n}_{\phi}} \int_{A^{j_{i}}}\left(D_{z_{u}}-D_{z_{l}}\right) \delta \phi^{j_{i}} \mathrm{~d} A^{j_{i}}=0 . \quad(24)
$$

Here, $V$ and $\Gamma$ are the volume and surface area of the beam, $A^{j_{i}}$ is an internal surface $z=z_{\phi}^{j_{i}}$, where $\phi^{j_{i}}$ is prescribed and $D z_{u}-D_{z_{l}}=q_{j_{i}}$ is the extraneous surface charge density on this surface; the subscripts $u$ and $l$ refer to the faces of the interface at $\left(z_{\phi}^{j_{i}}\right)^{+},\left(z_{\phi}^{j_{i}}\right)^{-}$. The total number of such prescribed potentials is $\bar{n}_{\phi}, D_{n}$ and $T^{n}$ are the electric displacement and stress vector for outward normal to $\Gamma$. Let $p_{z}^{1}, p_{z}^{2}$ be the forces per unit area applied on the bottom and top surfaces of the beam in direction $z$. Using the notation

$$
\langle\cdots\rangle=\sum_{k=1}^{L} \int_{z_{k-1}^{+}}^{z_{k}^{-}}(\ldots) b \mathrm{~d} z,
$$

Eq. (24) can be expressed as

$$
\begin{aligned}
& \int_{0}^{a}\left[\left\langle\sigma_{x} \delta \varepsilon_{x}+\tau_{z x} \delta \gamma_{z x}+D_{x} \delta \phi_{, x}+D_{z} \delta \phi_{, z}\right\rangle-b p_{z}^{1} \delta w\left(x, z_{0}\right)-b p_{z}^{2} \delta w\left(x, z_{L}\right)+b D_{z}\left(x, z_{0}\right) \delta \phi^{1}\right. \\
& \left.\quad-b D_{z}\left(x, z_{L}\right) \delta \phi^{n_{\phi}}+b q_{j_{i}} \delta \phi^{j_{i}}\right] \mathrm{d} x-\left.\left\langle\sigma_{x} \delta u+\tau_{z x} \delta w+D_{x} \delta \phi\right\rangle\right|_{0} ^{a}=0 .
\end{aligned}
$$

The integral in Eq. (26) is expressed in terms of $\delta u_{0}, \delta w_{0}, \delta \psi_{0}, \delta \phi^{j}$, using integration by parts if needed, to yield equilibrium equations and boundary conditions. The equilibrium equations are:

$$
\begin{aligned}
& N_{x, x}=0, \quad M_{x, x x}+F_{2}=0, \quad-P_{x, x}+Q_{x}=0, \\
& -S_{x, x x}^{j}+\bar{Q}_{x, x}^{j}+H_{, x}^{j}-G^{j}+F_{4}^{j}=0, \quad j=1,2, \ldots, n_{\phi},
\end{aligned}
$$

where $N_x, M_x, P_x, Q_x, S_x^j, \bar{Q}_x^j$ are stress resultants and $H^j, G^j$ are electric displacement resultants,
defined as

$$
\begin{aligned}
N_{x} & =\left\langle\sigma_{x}\right\rangle=A_{11} u_{0, x}-A_{12} w_{0, x x}+A_{13} \psi_{0, x}+A_{14}^{j^{\prime}} \phi_{, x x}^{j^{\prime}}+\beta_{1}^{j^{\prime}} \phi^{j^{\prime}}, \\
M_{x} & =\left\langle z \sigma_{x}\right\rangle=A_{12} u_{0, x}-A_{22} w_{0, x x}+A_{23} \psi_{0, x}+A_{24}^{j^{\prime}} \phi_{, x x}^{j^{\prime}}+\beta_{2}^{j^{\prime}} \phi^{j^{\prime}}, \\
P_{x} & =\left\langle R^{k}(z) \sigma_{x}\right\rangle=A_{13} u_{0, x}-A_{23} w_{0, x x}+A_{33} \psi_{0, x}+A_{34}^{j^{\prime}} \phi_{, x x}^{j^{\prime}}+\beta_{3}^{j^{\prime}} \phi^{j^{\prime}}, \\
S_{x}^{j} & =\left\langle R_{, z}^{k j}(z) \sigma_{x}\right\rangle=A_{14}^{j} u_{0, x}-A_{24}^{j} w_{0, x x}+A_{34}^{j} \psi_{0, x}+A_{44}^{j j^{\prime}} \phi_{, x x}^{j^{\prime}}+\beta_{4}^{j j^{\prime}} \phi^{j^{\prime}}, \\
Q_{x} & =\left\langle R_{, z}^{k}(z) \tau_{z x}\right\rangle=\bar{A}_{33} \psi_{0}+\left(\bar{A}_{34}^{j^{\prime}}+\bar{\beta}_{3}^{j^{\prime}}\right) \phi_{, x}^{j^{\prime}}, \\
\bar{Q}_{x}^{j} & =\left\langle\left[R_{, z}^{k j}(z)-\bar{\Psi}_{\phi}^{j}(z)\right] \tau_{z x}\right\rangle=\bar{A}_{34}^{j} \psi_{0}+\left(\bar{A}_{44}^{j j^{\prime}}+\bar{\beta}_{4}^{j j^{\prime}}\right) \phi_{, x}^{j^{\prime}}, \\
H^{j} & =\left\langle\Psi_{\phi}^{j}(z) D_{x}\right\rangle=\bar{\beta}_{3}^{j} \psi_{0}+\left(\bar{\beta}_{4}^{j j^{\prime}}-\bar{E}^{j j^{\prime}}\right) \phi_{, x}^{j^{\prime}}, \\
G^{j} & =\left\langle\Psi_{\phi, z}^{j}(z) D_{z}\right\rangle=\beta_{1}^{j} u_{0, x}-\beta_{2}^{j} w_{0, x x}+\beta_{3}^{j} \psi_{0, x}+\beta_{4}^{j j^{\prime}} \phi_{, x x}^{j^{\prime}}-E^{j j^{\prime}} \phi^{j^{\prime}},
\end{aligned}
\tag{28}
$$

with

$$
\begin{aligned}
& {\left[A_{11}, A_{12}, A_{13}, A_{14}^{j^{\prime}}, A_{22}, A_{23}, A_{24}^{j^{\prime}}, A_{33}\right]=\left\langle\hat{Q}_{11}\left[1, z, R^{k}(z), R^{k j^{\prime}}(z), z^{2}, z R^{k}(z), z R^{k j^{\prime}}(z),\left\{R^{k}(z)\right\}^{2}\right]\right\rangle, } \\
& {\left[A_{34}^{j^{\prime}}, A_{44}^{j j^{\prime}}\right]=\left\langle\hat{Q}_{11}\left[R^{k}(z) R^{k j^{\prime}}(z), R^{k j}(z) R^{k j^{\prime}}(z)\right]\right\rangle, } \\
& {\left[\bar{A}_{33}, \bar{A}_{34}^{j^{\prime}}, \bar{A}_{44}^{j j^{\prime}}\right]=\left\langle\hat{Q}_{55}\left[\left\{R^{k}(z)\right\}^{2}, R^{k}(z)\left\{R_{, z}^{k j^{\prime}}(z)-\bar{\Psi}_{\phi}^{j^{\prime}}(z)\right\},\left\{R_{, z}^{k j}(z)-\bar{\Psi}_{\phi}^{j}(z)\right\}\left\{R_{, z}^{k j^{\prime}}(z)-\bar{\Psi}_{\phi}^{j^{\prime}}(z)\right\}\right]\right\rangle, } \\
& {\left[\beta_{1}^{j^{\prime}}, \beta_{2}^{j^{\prime}}, \beta_{3}^{j^{\prime}}, \beta_{4}^{j j^{\prime}}\right]=\left\langle\hat{e}_{31} \Psi_{\phi, z}^{j^{\prime}}(z)\left[1, z, R^{k}(z), R^{k j^{\prime}}(z)\right]\right\rangle, } \\
& {\left[\bar{\beta}_{3}^{j^{\prime}}, \bar{\beta}_{4}^{j j^{\prime}}\right]=\left\langle\hat{e}_{15} \Psi_{\phi}^{j^{\prime}}(z)\left[R^{k}(z), R_{, z}^{k j^{\prime}}(z)-\bar{\Psi}_{\phi}^{j^{\prime}}(z)\right]\right\rangle, } \\
& E^{j j^{\prime}}=\left\langle\hat{\eta}_{33} \Psi_{\phi, z}^{j}(z) \Psi_{\phi, z}^{j^{\prime}}(z)\right\rangle, \bar{E}^{j j^{\prime}}=\left\langle\hat{\eta}_{11} \Psi_{\phi}^{j}(z) \Psi_{\phi}^{j^{\prime}}(z)\right\rangle,
\end{aligned}
\tag{29}
$$

The loads are

$$
F_{2}=b\left(p_{z}^{1}+p_{z}^{2}\right), \quad F_{4}^{j}=b\left[-p_{z}^{1} \bar{\Psi}_{\phi}^{j}\left(z_{0}\right)-p_{z}^{2} \bar{\Psi}_{\phi}^{j}\left(z_{L}\right)+D_{z_{L}} \delta_{j n_{\phi}}-D_{z_{0}} \delta_{j 1}-q_{j i} \delta_{j j_{i}}\right]
$$

where $\delta_{i j}$ is Kronecker's delta. The essential or natural boundary conditions at the ends of the
beam at $x=0, a$ are

$$
\begin{aligned}
& u_{0}=u_{0}^{*} \text { or } N_{x}=N_{x}^{*} ; \quad w_{0}=w_{0}^{*} \text { or } M_{x, x}=\left\langle\tau_{z x}\right\rangle^{*} ; \\
& w_{0, x}=w_{0, x}^{*} \text { or } M_{x}=M_{x}^{*} ; \quad \psi_{0}=\psi_{0}^{*} \text { or } P_{x}=P_{x}^{*} ; \\
& \phi_{, x}^{j}=\phi_{, x}^{j *} \quad \text { or } \quad S_{x}^{j}=S_{x}^{j} ; \quad \phi^{j}=\phi^{j *} \quad \text { or } \quad-S_{x, x}^{j}+\bar{Q}_{x}^{j}+H^{j}=H^{j *}-\left\langle\bar{\Psi}^{j} \tau_{z x}\right\rangle^{*} ;
\end{aligned}
\tag{30}
$$

where the asterisk $\star$ refers to a prescribed value.

Substitution of the expressions from Eqs. (28) into Eqs. (27) yields governing equations

$$
\left[L_{i j}\right] \bar{U}=P
\tag{31}
$$

for

$$
\bar{U}=\left[u_{0} w_{0} \psi_{0} \phi^{1} \phi^{2} \ldots \phi^{n_{\phi}}\right]^{\mathrm{T}}, \text { with } P=\left[\begin{array}{lllllllll}
0 & F_{2} & 0 & F_{4}^{1} & F_{4}^{2} & \ldots F_{4}^{n_{\phi}}
\end{array}\right]^{\mathrm{T}}.
$$

Here, $L_{i j}$ are differential operators with $L_{i j}=L_{j i}$,

$$
\begin{aligned}
& L_{11}=A_{11}()_{, x x}, \quad L_{12}=-A_{12}()_{, x x x}, \quad L_{13}=A_{13}()_{, x x}, L_{1,3+j^{\prime}}=A_{14}^{j^{\prime}}()_{, x x x}+\beta_{1}^{j^{\prime}}()_{, x}, \\
& L_{22}=A_{22}()_{, x x x x}, L_{23}=-A_{23}()_{, x x x}, L_{2,3+j^{\prime}}=-A_{24}^{j^{\prime}}()_{, x x x x}-\beta_{2}^{j^{\prime}}()_{, x x}, L_{33}=A_{33}()_{, x x}-\bar{A}_{33}, \\
& L_{3,3+j^{\prime}}=A_{34}^{j^{\prime}}()_{, x x x}+\beta_{3}^{j^{\prime}}()-\left[\bar{A}_{34}^{j^{\prime}}+\bar{\beta}_{3}^{j^{\prime}}\right]()_{, x}, \\
& L_{4+j, 4+j^{\prime}}=A_{41}^{j}()_{, x x x x}+\left[\beta_{4}^{j j^{\prime}}+\beta_{4}^{j^{\prime} j}-\bar{A}_{44}^{j j^{\prime}}+\bar{E}^{j j^{\prime}}-\bar{\beta}_{4}^{j j^{\prime}}-\bar{\beta}_{4}^{j^{\prime} j}\right]()_{, x x}+E^{j j^{\prime}},\left(j, j^{\prime}\right)=1, \ldots n_{\phi}.
\end{aligned}
\tag{32}
$$

After solving for $\bar{U}, \tau_{z x}$ is obtained more accurately from a 2D equilibrium equation as

$$
\tau_{z x}=-\int_{-h / 2}^{z} \sigma_{x, x} d z.
$$

### 3 Analytical solution for simply-supported beam
To assess the coupled zig-zag theory developed herein, an analytical solution is obtained for simply-supported beams with the boundary conditions:

$$
N_{x}=0, \quad w_{0}=0, \quad M_{x}=0, \quad P_{x}=0, \quad \phi^{j}=0, \quad S_{x}^{j}=0, \quad j=1, \ldots, n_{\phi}.
\tag{33}
$$

It is compared with the exact piezoelastic solution obtained herein using exact solution, [2], with the material constants chosen for plane stress conditions. The solution of Eq. (31) is expanded as

$$
\begin{aligned}
& \left(w_{0}, \phi^{j}, N_{x}, M_{x}, P_{x}, S_{x}^{j}, G^{j}, p_{z}^{i}, q_{j i}\right)=\sum_{n=1}^{\infty}\left(w_{0}, \phi^{j}, N_{x}, M_{x}, P_{x}, S_{x}^{j}, G^{j}, p_{z}^{i}, q_{j i}\right)_{n} \sin \bar{n} x, \\
& \left(u_{0}, \psi_{0}, Q_{x}, \bar{Q}_{x}^{j}, H^{j}\right)=\sum_{n=1}^{\infty}\left(u_{0}, \psi_{0}, Q_{x}, \bar{Q}_{x}^{j}, H^{j}\right)_{n} \cos \bar{n} x,
\end{aligned}
\tag{34}
$$

with $\bar{n}=n \pi / a$. Substituting these in Eq. (31) yields for the $n$-th Fourier component the coupled equations

$$
\left[\begin{array}{cc}
K^{u u} & K^{u e} \\
K^{e u} & K^{e e}
\end{array}\right]\left\{\begin{array}{l}
U^{n} \\
\Phi^{n}
\end{array}\right\}=\left\{\begin{array}{l}
F^{n} \\
Q^{n}
\end{array}\right\} \Rightarrow\left[\begin{array}{cc}
K_{s s}^{u u} & K_{s s}^{u e} \\
K_{s s}^{e u} & K_{s s}^{e e}
\end{array}\right]\left\{\begin{array}{l}
U^{n} \\
\Phi_{s}^{n}
\end{array}\right\}=\left\{\begin{array}{l}
F^{n}-K_{s a}^{u e} \Phi_{a}^{n} \\
Q_{s}^{n}-K_{s a}^{e e} \Phi_{a}^{n}
\end{array}\right\},
\tag{35}
$$

where

$$
U^{n}=\left[\begin{array}{lll}
u_{0} & w_{0} & \psi_{0}
\end{array}\right]_{n}^{\mathrm{T}}, \quad \Phi^{n}=\left[\begin{array}{lll}
\phi^{1} & \phi^{2} \ldots \phi^{N}
\end{array}\right]_{n}^{\mathrm{T}}, \quad F^{n}=\left[\begin{array}{lll}
0 & F_{2} & 0
\end{array}\right]^{\mathrm{T}}, \quad Q^{n}=\left[\begin{array}{llll}
F_{4}^{1} & F_{4}^{2} & \ldots & F_{4}^{n_{\phi}}
\end{array}\right]_{n}^{\mathrm{T}},
$$

$K^{r s}(r=u, e ; s=u, e)$ are submatrices of the symmetric stiffness matrix K. Equation (35) is partitioned with $\Phi=\left[\Phi_{s} ; \Phi_{a}\right]$, where $\Phi_{s}$ and $\Phi_{a}$ are the sets of unknown voltages output and known active voltages input at the sensor and actuator layers. It can be solved for the response in active/sensory/active-sensory mode.

### 4 Numerical results and discussion
The present theory is assessed directly against the exact piezoelastic solution and not against other layerwise theories which involve more displacement unknowns. Since the number of displacement unknowns in the present theory is the same as in FSDT, results are also compared with uncoupled FSDT with shear correction factor of 5/6.

Three highly inhomogeneous simply-supported beams (a), (b) and (c) are analysed. Beams (a) and (b) have an elastic substrate with a layer of PZT-5A of thickness $0.1 h$ bonded to its top. The top and the bottom of the substrate are grounded. The stacking order is mentioned from the bottom. The five-ply substrate of beam (a) is a good test case, [21]. It has plys of thickness $0.09 h / 0.225 h / 0.135 h / 0.18 h / 0.27 h$ of materials $1 / 2 / 3 / 1 / 3$ which have highly inhomogeneous

stiffness in tension and shear. The substrate of beam (b) is a three-layer sandwich with graphite-epoxy (material 3) faces and a soft core, [22], with thicknesses $0.09h/0.72h/0.09h$. Convergence studies have revealed that converged results are obtained for beams (a) and (b) by dividing the PZT layer into four equal sublayers for discretising $\phi$. Beam (c) is a piezoelectric laminate of PZT-5A layer on top of a PVDF layer of equal thickness with poling in $+z$ and $-z$ directions. Beam (c) having layers with wide difference in elasic and piezoelectric constants provides a good test case of these type of inhomogenieties, particularly for piezoelectric coupling. For all plys of the three beams we have $\theta_k = 0$.

The material properties are:

Material 1: $[(Y_1, Y_2, Y_3, G_{12}, G_{23}, G_{31}), v_{12}, v_{13}, v_{23}]$
$= [(6.9, 6.9, 6.9, 1.38, 1.38, 1.38)\ \text{GPa}, 0.25, 0.25, 0.25],$

Material 2: $[(Y_1, Y_2, Y_3, G_{12}, G_{23}, G_{31}), v_{12}, v_{13}, v_{23}]$
$= [(224.25, 6.9, 6.9, 56.58, 1.38, 56.58)\ \text{GPa}, 0.25, 0.25, .25],$

Material 3: $[(Y_1, Y_2, Y_3, G_{12}, G_{23}, G_{31}), v_{12}, v_{13}, v_{23}]$
$= [(172.5, 6.9, 6.9, 3.45, 1.38, 3.45)\ \text{GPa}, 0.25, 0.25, 0.25],$

Core: $[(Y_1, Y_2, Y_3, G_{12}, G_{23}, G_{31}), v_{12}, v_{13}, v_{23}]$
$= [(0.276, 0.276, 3.45, 0.1104, 0.414, 0.414)\ \text{GPa}, 0.25, 0.02, 0.02],$

PZT-5A: $[(Y_1, Y_2, Y_3, G_{12}, G_{23}, G_{31}), v_{12}, v_{13}, v_{23}]$
$= [(61.0, 61.0, 53.2, 22.6, 21.1, 21.1)\ \text{GPa}, 0.35, 0.38, 0.38],$
$[(d_{31}, d_{32}, d_{33}, d_{15}, d_{24}), (\eta_{11}, \eta_{22}, \eta_{33})]$
$= [(-171, -171, 374, 584, 584) \times 10^{-12}\ \text{m/V}, (1.53, 1.53, 1.5) \times 10^{-8}\ \text{F/m}],$

PVDF: $[(Y_1, Y_2, Y_3, G_{12}, G_{23}, G_{31}), v_{12}, v_{13}, v_{23}]$
$= [(2.0, 2.0, 2.0, 0.75, 0.75, 0.75)\ \text{GPa}, 1/3, 1/3, 1/3],$
$[(d_{31}, d_{32}, d_{33}, d_{15}, d_{24}), (\eta_{11}, \eta_{22}, \eta_{33})]$
$= [(23, 3, -30, 0, 0) \times 10^{-12}\ \text{m/V}, (1.062, 1.062, 1.062) \times 10^{-10}\ \text{F/m}]$

Two load cases considered are:

1. Pressure $p_z^2 = -p_0\sin(\pi x/a)$ on the top surface with open (O) circuit condition $q_{n_\phi}=0$ on it.
2. A closed (C) circuit condition on the top surface with applied actuation potential
$\phi^{n_\phi} = \phi_0\sin(\pi x/a)$.

The results for these cases are non-dimensionalised with $S=a/h$, $Y_T=6.9\ \text{GPa}$,
$d_T=374\times10^{-12}\ \text{CN}^{-1}$:

$$
\text{1. } (\bar{u}, \bar{w}) = 100\left(u, \frac{w}{S}\right)\frac{Y_T}{hS^3p_0}, \quad (\bar{\sigma}_x, \bar{\tau}_{zx}) = \left(\frac{\sigma_x}{S^2p_0}, \frac{\tau_{zx}}{Sp_0}\right), \quad \bar{\phi} = 10^4\phi\frac{Y_Td_T}{hS^2p_0},
$$

$$
\text{2. } (\tilde{u}, \tilde{w}) = \frac{10(Su, w)}{S^2d_T\phi_0}, \quad (\tilde{\sigma}_x, \tilde{\tau}_{zx}) = (0.1\sigma_x, S\tau_{zx})\frac{h}{Y_Td_T\phi_0}, \quad \tilde{\phi} = \frac{\phi}{\phi_0}, \quad \tilde{D}_z = \frac{D_z h}{100Y_Td_T^2\phi_0} .
$$

The exact results and the error percentages in the response of beams (a) and (b) for the two load cases, predicted by the present theory and the uncoupled FSDT, are given in Table 1. The stress $\sigma_x^e$ is the maximum stress in the substrate, $\sigma_x^p$ is the maximum stress at the top of the PZT layer and $\tau_{zx}$ is the maximum stress at $z=0$ for load case 1 and at the PZT interface for case 2; $\phi$ and $D_z$ are the maximum values at the top for load cases 1 and 2, respectively. The deflection $w$ is at the centre for beam (a) and at the middle of the bottom face for beam (b). The thickness distributions of $u, w, \sigma_x, \tau_{zx}$ are compared in Figs. 2 and 3 for beam (a) and in Figs. 4 and 5 for beam (b). The highly zig-zag displacement $u$ is well predicted by the present theory except for the upper half of test beam (a) under potential load and the core of sandwich beam (b) under pressure load for the thickness case $S=5$. The smeared laminate theories like FSDT cannot predict zig-zag variation. The thickness variation of $w$ for load case 2 (Figs. 3 and 5) is very well captured by the present theory, even for thick beams, since it includes the effect of strain $\varepsilon_z$ induced by $\phi$ through $d_{33}$. The

<table><caption>Table 1. Exact results and magnitude of percentage error for the present theory (Pres.) and FSDT</caption>
<thead>
<tr>
<th>Entity</th>
<th>S</th>
<th colspan="6">Beam (a)</th>
<th colspan="6">Beam (b)</th>
</tr>
<tr>
<th></th>
<th></th>
<th colspan="3">Load case 1</th>
<th colspan="3">Load case 2</th>
<th colspan="3">Load case 1</th>
<th colspan="3">Load case 2</th>
</tr>
<tr>
<th></th>
<th></th>
<th>Exact</th>
<th>Pres.</th>
<th>FSDT</th>
<th>Exact</th>
<th>Pres.</th>
<th>FSDT</th>
<th>Exact</th>
<th>Pres.</th>
<th>FSDT</th>
<th>Exact</th>
<th>Pres.</th>
<th>FSDT</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="3">$w$</td>
<td>5</td>
<td>−2.054</td>
<td>0.14</td>
<td>55.51</td>
<td>1.736</td>
<td>5.40</td>
<td>24.97</td>
<td>−7.515</td>
<td>0.06</td>
<td>70.83</td>
<td>3.408</td>
<td>0.64</td>
<td>53.34</td>
</tr>
<tr>
<td>10</td>
<td>−1.079</td>
<td>0.50</td>
<td>29.11</td>
<td>1.465</td>
<td>2.40</td>
<td>8.70</td>
<td>−2.776</td>
<td>0.52</td>
<td>50.40</td>
<td>2.263</td>
<td>0.68</td>
<td>21.25</td>
</tr>
<tr>
<td>100</td>
<td>−0.711</td>
<td>0.03</td>
<td>0.65</td>
<td>1.350</td>
<td>0.05</td>
<td>0.12</td>
<td>−1.108</td>
<td>0.02</td>
<td>0.05</td>
<td>1.850</td>
<td>0.01</td>
<td>0.26</td>
</tr>
<tr>
<td rowspan="3">$\sigma_x^e$</td>
<td>5</td>
<td>1.411</td>
<td>1.37</td>
<td>36.98</td>
<td>2.351</td>
<td>14.42</td>
<td>17.06</td>
<td>2.039</td>
<td>1.04</td>
<td>28.85</td>
<td>3.685</td>
<td>2.53</td>
<td>3.80</td>
</tr>
<tr>
<td>10</td>
<td>1.033</td>
<td>0.03</td>
<td>23.91</td>
<td>2.062</td>
<td>4.64</td>
<td>5.40</td>
<td>1.604</td>
<td>0.17</td>
<td>9.51</td>
<td>3.582</td>
<td>0.70</td>
<td>1.03</td>
</tr>
<tr>
<td>100</td>
<td>0.885</td>
<td>0.02</td>
<td>0.46</td>
<td>1.951</td>
<td>0.07</td>
<td>0.07</td>
<td>1.448</td>
<td>0.00</td>
<td>0.20</td>
<td>3.545</td>
<td>0.01</td>
<td>0.01</td>
</tr>
<tr>
<td rowspan="3">$\sigma_x^p$</td>
<td>5</td>
<td>−0.510</td>
<td>8.51</td>
<td>36.04</td>
<td>−3.028</td>
<td>4.87</td>
<td>6.83</td>
<td>−1.153</td>
<td>3.05</td>
<td>60.80</td>
<td>−2.407</td>
<td>2.27</td>
<td>9.16</td>
</tr>
<tr>
<td>10</td>
<td>−0.393</td>
<td>3.36</td>
<td>17.08</td>
<td>−3.174</td>
<td>1.34</td>
<td>1.92</td>
<td>−0.654</td>
<td>1.64</td>
<td>30.89</td>
<td>−2.565</td>
<td>0.62</td>
<td>2.45</td>
</tr>
<tr>
<td>100</td>
<td>−0.349</td>
<td>0.30</td>
<td>6.46</td>
<td>−3.229</td>
<td>0.06</td>
<td>0.17</td>
<td>−0.479</td>
<td>0.23</td>
<td>5.66</td>
<td>−2.620</td>
<td>0.07</td>
<td>0.28</td>
</tr>
<tr>
<td rowspan="3">$\tau_{zx}$</td>
<td>5</td>
<td>−0.434</td>
<td>0.79</td>
<td>21.06</td>
<td>−9.797</td>
<td>4.37</td>
<td>5.60</td>
<td>−0.354</td>
<td>0.18</td>
<td>6.41</td>
<td>−8.093</td>
<td>1.76</td>
<td>5.13</td>
</tr>
<tr>
<td>10</td>
<td>−0.498</td>
<td>0.55</td>
<td>5.61</td>
<td>−10.195</td>
<td>1.19</td>
<td>1.49</td>
<td>−0.370</td>
<td>0.07</td>
<td>1.78</td>
<td>−8.398</td>
<td>0.46</td>
<td>1.30</td>
</tr>
<tr>
<td>100</td>
<td>−0.524</td>
<td>0.01</td>
<td>0.33</td>
<td>−10.345</td>
<td>0.02</td>
<td>0.02</td>
<td>−0.376</td>
<td>0.00</td>
<td>0.22</td>
<td>−8.506</td>
<td>0.01</td>
<td>0.01</td>
</tr>
<tr>
<td rowspan="3">$\phi$ (1) or<br>$D_z$ (2)</td>
<td>5</td>
<td>6.178</td>
<td>10.67</td>
<td>–</td>
<td>−2.256</td>
<td>0.29</td>
<td>–</td>
<td>13.456</td>
<td>2.64</td>
<td>–</td>
<td>−2.281</td>
<td>0.07</td>
<td>–</td>
</tr>
<tr>
<td>10</td>
<td>6.118</td>
<td>3.26</td>
<td>–</td>
<td>−2.248</td>
<td>0.06</td>
<td>–</td>
<td>9.555</td>
<td>1.15</td>
<td>–</td>
<td>−2.274</td>
<td>0.01</td>
<td>–</td>
</tr>
<tr>
<td>100</td>
<td>6.012</td>
<td>0.06</td>
<td>–</td>
<td>−2.245</td>
<td>0.03</td>
<td>–</td>
<td>8.141</td>
<td>0.02</td>
<td>–</td>
<td>−2.274</td>
<td>0.04</td>
<td>–</td>
</tr>
</tbody>
</table>

![](./images/812376026230292481_2.jpg)

Fig. 2. The distributions of $\bar{u}$, $\bar{w}$, $\bar{\sigma}_x$, $\bar{\tau}_{zx}$ for test beam (a) under pressure load

present central deflection agrees well with the exact solution for all cases. The thickness distributions of $\sigma_x, \tau_{zx}$ are in very good agreement with the exact solution.

For the thick test beam (a) with $S=5$, the error of the present theory is within 5.5% for all entities except $\tilde{\sigma}_x^e(14.42\%)$ for load 2 and $\sigma_x^p(8.51\%)$ & $\phi(10.67\%)$ for load 1, whereas there is very large error in FSDT of 55.51% and 24.97% for $w$ and up to 36.98% and 17.06% for the stresses for loads 1 and 2 respectively. For the moderately thick beam (a) with $S=10$, the error of the present theory is within 2.5% for all entities except $\tilde{\sigma}_x^e(4.64\%)$, $\phi(3.26\%)$ and $\tilde{\sigma}_x^p(3.36\%)$, whereas the error in FSDT is large, being 28.11% and 8.70% for $w$ and upto 13.91% and 5.4% for the stresses for loads 1 and 2.

For the thick sandwich beam (b) with $S=5$, the error of the present theory is within 0.64% for the deflection and 2.53% for the stresses, whereas error in FSDT is very large, being 70.89%

![](./images/812376026230292481_3.jpg)

Fig. 3. The distributions of $\bar{u}$, $\bar{w}$, $\bar{\sigma}_{x}$, $\bar{\tau}_{zx}$ for test beam (a) under potential load

![](./images/812376026230292481_4.jpg)

Fig. 4. The distributions of $\bar{u}$, $\bar{w}$, $\bar{\sigma}_{x}$, $\bar{\tau}_{zx}$ for sandwich beam (b) under pressure load

and 53.34% for $w$ and up to 28.85% and 9.16% for stresses for loads 1 and 2. For beam (b) with $S = 10$, the error of the present theory is within 1.2% for all entities, whereas the error in FSDT is large, being 50.4% and 21.25% for $w$ and up to 9.51% and 2.45% for the stresses for loads 1 and 2. It may be mentioned that for simply-supported beams, FSDT has yielded the same values of dimensionless $u$, $\sigma_{x}$, $\tau_{zx}$ for all cases and relatively small error in stresses compared to large error in deflection for $S = 10$. However, the stresses predicted by FSDT for statically indeterminate problems (like a propped cantilever) would be worse for $S = 10$, since its

![](./images/812376026230292481_5.jpg)

Fig. 5. The distributions of $\tilde{u}, \tilde{w}, \tilde{\sigma}_{x}$,
$\tilde{\tau}_{zx}$ for sandwich beam (b) under
potential load

![](./images/812376026230292481_6.jpg)

Fig. 6. Distributions of closed circuit
potential for piezoelectric beam (c)
under (1) pressure and (2) actuation
potential

prediction of $w$ is highly erroneous. No such worsening of accuracy of stresses would occur for the present theory, since its prediction of deflection is very accurate. Even for thin beams (a) and (b) with $S=20$, the error in $w$ for FSDT is $9.36\%$ and $22.64\%$ for pressure load.

The thickness distributions of electric potential $\phi$ for a two-layer piezoelectric beam (c) with the top and bottom surfaces in closed-circuit condition are compared in Fig. 6 for the two load cases. No internal electrode is present. The present results are obtained by discretising each lamina into 8 and 12 equal sublayers and good convergence is observed for eight sublayers. The present theory yields very accurate potential field $\phi$ for both the sensory and actuation modes of load cases 1 and 2. The error of the present theory for the central deflection for $S=5$ is only $0.52\%$ and $0.45\%$ for load cases 1 and 2.

## 5 Conclusions
The zig-zag coupled theory presented herein for hybrid sandwich beams with any lay-up is the first coupled theory in which the shear stress continuity conditions and shear traction-free conditions are satisfied exactly, even for the case of non-zero inplane potential field. Also the effect of piezoelectric transverse normal strain is accounted for in the transverse displacement field. Its accuracy is established by comparison with the exact piezoelastic solution, by considering three (thick, moderately thick and thin) beams with highly heterogeneous lay-ups. The present accurate theory is also economical, since the number of primary mechanical variables is the same as that of uncoupled FSDT, which yields poor results for moderately thick heterogeneous beams and even for thin sandwich beams. The theory can accurately model closed- and open-circuit electric boundary conditions in the sensor and actuator layers.

### References

1. Saravanos, D.; Heyliger, P.R.: Mechanics and computational models for laminated piezoelectric beams, plates and shells. Appl Mech Rev 52 (1999) 305-320

2. Ray, M.C.; Rao, K.M.; Samanta, B.: Exact solution for static analysis of an intelligent structure under cylindrical bending. Comput Struct 47 (1993) 1031-1042

3. Vel, S.S.; Batra, R.C.: Cylindrical bending of laminated plates with distributed and segmented piezoelectric actuators/sensors. AIAA J 38 (2000) 857-867

4. Ha, S.K.; Keilers, C.; Chang, F.K.: Finite element analysis of composite structures containing distributed piezoceramic sensors and actuators. AIAA J 30 (1992) 772-780

5. Bailey, T.; Hubbard, J.E.: Distributed piezoelectric-polymer active vibration control of a cantilever beam. J. Guidance Control Dyn 8 (1985) 605-611

6. Im, S.; Atluri, S.N.: Effects of a piezo-actuator on a finitely deformed beam subject to general loading. AIAA J 27 (1989) 1801-1807

7. Chandra, R.; Chopra, I.: Structural modelling of composite beams with induced-strain actuators. AIAA J 31 (1993) 1692-1701

8. Robbins, D.H.; Reddy, J.N.: Analysis of piezoelectrically actuated beams using a layer-wise displacement theory. Comput Struct 41 (1991) 265-279

9. Tzou, H.S.: Distributed sensing and controls of flexible plates and shells using distributed piezoelectric element. J Wave Mat Interact 4 (1989) 11-29

10. Zhang, X.D., Sun, C.T.: Formulation of an adaptive sandwich beam. Smart Mat Struct 5 (1996) 814-823

11. Chandrashekhara, K.; Donthireddy, P.: Vibration suppression of composite beams with piezoelectric devices using a higher order theory. Eur J Mech A/Solids 16 (1997) 709-721

12. Peng, X.Q.; Lam, K.Y.; Liu, G.R.: Active vibration control of composite beams with piezoelectrics: A finite element model with third order theory. J Sound Vib 209 (1998) 635-650

13. Benjeddou, A.; Trindadade, M.A.; Ohayon, R.: A unified beam finite element model for extension and shear piezoelectric actuation mechanisms. J Intelligent Mat Syst Struct 8 (1997) 1012-25

14. Vel, S.S.; Batra, R.C.: Analysis of piezoelectric bimorphs and plates with segmented actuators. Thin-walled Struct 39 (2001) 23-44

15. Huang, D.; Sun, B: Approximate analytical solution of smart composite Mindlin beams. J Sound Vib 244 (2001) 379-399

16. Mitchell. J.A.; Reddy, J.N.: A refined hybrid plate theory for composite laminates with piezoelectric laminae. Int J Solids Struct 32 (1995) 2345-2367

17. Zhou, X.; Chattopadhyay, A.; Gu, H.: Dynamic responses of smart composite using a coupled thermo-piezoelectric-mechanical model. AIAA J 38 (2000) 1939-1948

18. Saravanos, D.A.; Heyliger, P.R.: Coupled layerwise analysis of composite beams with embedded piezoelectric sensors and actuators. J Intelligent Mat Syst Struct 6 (1995) 350-363

19. Carrera, E.: An improved Reissner-Mindlin type model for the electromechanical analysis of multi-layered plates including piezo layers. J Intelligent Mat Syst Struct 8 (1997) 232-248

20. Kapuria, S.: An efficient coupled theory for multi-layered beams with embedded piezoelectric sensory and active layers. Int J Solids Struct 38 (2001) 9179-9199

21. Averril, R.C.; Yip, Y.C.: An efficient thick beam theory and finite element model with zig-zag sublaminate approximation. AIAA J 34 (1996) 1626-1632

22. Pagano, N.J.: Exact solutions for rectangular bidirectional composites and sandwich plates. J Comput Math 4 (1970), 20-34
159