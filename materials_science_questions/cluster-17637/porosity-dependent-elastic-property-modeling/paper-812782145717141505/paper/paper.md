# Effects of nano-voids and nano-cracks on the elastic properties of a host medium: XFEM modeling with the level-set function and free surface energy

M. R. Kired¹ · B. E. Hachi¹ · D. Hachi² · M. Haboussi³

Received: 4 August 2018 / Revised: 13 November 2018 / Accepted: 5 December 2018
© The Chinese Society of Theoretical and Applied Mechanics and Springer-Verlag GmbH Germany, part of Springer Nature 2019

## Abstract
This work deals with the influences of nano-heterogeneities in the form of voids/cavities or cracks on the elastic properties of a host medium. With a relatively large ratio of apparent surface to volume and particularly strong physical interactions with the surrounding medium at nano-scale, nano-heterogeneities can potentially affect the elastic properties of the parent medium (matrix) containing them in a significant manner. This has been reported by various theoretical and experimental studies, some of which are discussed in the present paper. To describe the positive (reinforcement) or negative (degradation) effect of the nano-heterogeneities from the modeling perspective, it is necessary to take into account the energy of interfaces/surfaces between nano-heterogeneities and the matrix, which, because of the relatively large extent of their apparent surface and their strong physical interaction with their neighborhood, can no longer be neglected compared to those of the volume energy. Thus, to account for the effects of interfaces/surfaces in a nanostructured heterogeneous medium, the coherent interface model is considered in the present investigation within a periodic homogenization procedure. In this interface/surface model, the displacement vector is assumed to be continuous across the interface while the stress vector is considered to be discontinuous and satisfying the Laplace–Young equations. To solve these equations coupled to the classical mechanical equilibrium problem, a numerical simulation tool is developed in a two-dimensional (2D) context using the extended finite element method and the level-set functions. The developed numerical tool is then used to carry out a detailed analysis about the effect of nano-heterogeneities on the overall mechanical properties of a medium. The nano-heterogeneities are present in the medium initially as cylindrical cavities (circular in 2D) before being reduced to plane cracks (line in 2D) by successive flattenings.

Keywords Interface/surface energy · XFEM · Level-Set function · Periodic homogenization · Nano-voids/nano-cavities · Nano-cracks · Nano-inclusions/nano-heterogeneities

⊗ M. Haboussi
mohamed.haboussi@lspm.cnrs.fr

¹ Laboratoire de Développement en Mécanique et Matériaux (LDMM), Université de Djelfa, PB 3117 Djelfa, Algeria
² Laboratoire d’Automatique Appliquée et Diagnostics Industriels (LAADI), Université de Djelfa, PB 3117 Djelfa, Algeria
³ Laboratoire des Sciences des Procédés et des Matériaux (LSPM), Université Paris 13, UPR 3407 CNRS, Sorbonne-Paris-Cité, 93430 Villetaneuse, France

---

## 1 Introduction
The fabrication of nanostructured materials such as nano-crystalline metals, thin films, nano-wires, nano-beams, nano-porous materials, and nano-composites wherein nano-particles are used as reinforcements or doping agents, is now a reality in nanotechnology. As the number of atoms near the surface/interface in these nanostructured materials is relatively large (compared to the total number of atoms), the surface/interface starts to have a specific behavior and affects significantly the properties of the nano-particle or the nanostructured material. This has been confirmed by several theoretical, numerical, and experimental works such as those cited in Refs. [1–17], and the many others cited in the review paper [1]. At the nano-scale, the surface/interface

may have its own physics, materialized by a proper con- stitutive law like the elastic law determined by Miller and Shenoy [2], at the free surface of nano-pores in isotropic aluminum matrix (with shear modulus = 34.7 GPa and Poisson's ratio = 0.3). Depending on the crystallographic orientation of the polycrystal at the aluminum free surface, these authors identified two sets of surface Lamé's constants ($\lambda_{\mathrm{s}}=3.48912 \mathrm{~N} \cdot \mathrm{m}^{-1}$, $\mu_{\mathrm{s}}=-6.2178 \mathrm{~N} \cdot \mathrm{m}^{-1}$ for the orientation Al[100]; and $\lambda_{\mathrm{s}}=6.842 \mathrm{~N} \cdot \mathrm{m}^{-1}$, $\mu_{\mathrm{s}}=-0.3755 \mathrm{~N} \cdot \mathrm{m}^{-1}$ for the orientation Al[111]), leading to positive and negative bulk modulii, respectively. The calculations of Miller and Shenoy [2] suggest that the modification of the crystallographic ori- entation leads theoretically to different free surface behavior. In fact, it is possible to tailor the surface structure in order to get particular behavior by chemical functionalization [3] or controlled in situ crystallization [4]. In this case, it is possible to obtain novel and unusual bulk properties such as nano-porous or nano-cellular materials whose stiffness matches or even exceeds that of the parent materials. This may enable considerable reduction in size and weight of structural elements without sacrificing their strength and other important physical properties. This statement, which has numerically been confirmed in Ref. [5], will also be examined in the present work.

The main objective of this work is the numerical study of the effect of nano-heterogeneities on the effective stiff- ness of a parent material (aluminum) hosting such nano- heterogeneities. The latter can be either a single (or multi- ple) nano-void(s)/nano-cavity(ies) or nano-crack(s). In fact, nano-cracks are the ultimate state of flattened nano-voids/ nano-cavities in this work. Hence, the initially cylindrical nano-voids/nano-cavities are transformed into increasingly flattened elliptical-cylinder like voids/cavities, before shrink- ing to the state of plane nano-cracks. As the developments are addressed in two-dimensional (2D) context, the cylindri- cal void/cavity is represented by a circular domain and the plane crack is represented by a line. The nanoscopic nature of the examined heterogeneities is accounted for by consid- ering the energy contribution of their surfaces, through the use of the Laplace-Young equations of surface equilibrium [18, 19], as it has been done in various publications, some of which are cited in Refs. [5-9].

Regarding the particular problem of cracking effect on effective properties, in the past, several studies have been dedicated to the analysis of the effects of micro- and macro- cracks on the effective stiffness of a cracked medium as mentioned in the comprehensive review by Kachanov et al. [20] and in other works [21-23]. In particular, the cracks' distribution and interaction were the main concerns. More recently, as an example of the very few contributions that are devoted to the study of the effective elastic properties of nano-cracked medium, there is a work [24] that inves- tigates the surface tension effect of nano-cracks on the size-dependent effective electroelastic properties of a pie- zoelectric, within the framework of non-interaction approxi- mation, under continuously damaged interface formed by nano-cracks.

In accordance with the announced goal, a numerical sim- ulation tool is developed in this work in order to evaluate the elastic properties of a medium containing single (or mul- tiple) nano-void(s), which become crack(s) by successive flattenings. This simulation tool uses an approach combin- ing extended finite element method (XFEM) and the tech- nique of level-set functions, [6, 8, 25-29]. Once validated by comparison with existing numerical [6] and analytical [12] results, the simulation tool is deployed to solve the bound- ary value problems corresponding to the adopted periodic homogenization procedure [30, 31]. Hence, the effect of nano-voids and/or nano-cracks on the effective stiffness of a medium containing such heterogeneities is investigated. Regarding the surface model considered here, salient results of this study are: (1) identification of a theoretical value of the void radius below which, the porous medium becomes stiffer than the parent matrix; (2) highlighting of the eva- nescent effect of the surface energy once the void becomes a crack-like.

This paper is organized as follows: in Sect. 2, the theo- retical foundations of the present work are given. Then the XFEM discretization of the mathematical problem is pre- sented combined to a level-set in Sect. 3. In Sect. 4, some numerical applications are proposed. The paper is ended with some conclusions and remarks.

## 2 Theoretical formulation of the problem

Consider a linear elastic 2D material domain $\Omega=\bigcup_{i=1}^{N} \Omega^{(i)}$ in static equilibrium, composed of N isotropic sub-domains (Fig. 1). The sub-domain (N) corresponds to the solid phase whereas the first $(N-1)$ sub-domains correspond to inclu sions or voids/cavities $\Omega^{(i)}$. For the case of voids or cavities,

![](./images/812782145717141505_1.jpg)

Fig.1 Illustration of the studied heterogeneous nanostructured domain

Effects of nano-voids and nano-cracks on the elastic properties of a host medium: XFEM modeling…

the stiffness tends towards zero. Each sub-domain $\Omega^{(i)}$ obeys the following equilibrium field equation:

$$
\operatorname{div}\left[\boldsymbol{\sigma}^{(i)}\right]+\boldsymbol{b}^{(i)}=0, \quad \text { on } \Omega^{(i)}. \tag{1}
$$

where, $\boldsymbol{\sigma}^{(i)}$ and $\boldsymbol{b}^{(i)}$ correspond to the bulk Cauchy stress tensor and the body force, respectively. Each inclusion $\Omega^{(i)}(i=1,2, \ldots, N-1)$ possesses an interface (with zero thickness) $\Gamma^{(i)}$ obeying the coherent Laplace-Young constitutive field equation:

$$
\operatorname{div}_{\mathrm{s}} \boldsymbol{\sigma}_{\mathrm{s}}^{(i)}=-\left[\boldsymbol{\sigma}^{(\text {out })}-\boldsymbol{\sigma}^{(\text {in })}\right] \cdot \boldsymbol{n}^{(i)} \text {, on } \Gamma^{(i)} \text {, } \tag{2}
$$

where $\operatorname{div}_{\mathrm{s}} \boldsymbol{\sigma}_{\mathrm{s}}^{(i)}$ is the surface divergence of the surface Cauchy stress at each point $\boldsymbol{x}$ of the interface $\Gamma^{(i)}$. Both surface quantities, namely the surface divergence and the surface Cauchy stress, are defined in terms of the bulk Cauchy stress $\boldsymbol{\sigma}$ as $\operatorname{div}_{\mathrm{s}} \boldsymbol{\sigma}_{\mathrm{s}}=\nabla\left(\boldsymbol{\sigma}_{\mathrm{s}}\right): \boldsymbol{P}$ and $\boldsymbol{\sigma}_{\mathrm{s}}=\boldsymbol{P} \cdot \boldsymbol{\sigma} \cdot \boldsymbol{P}$ by using the following surface projection operator $\boldsymbol{P}$:

$$
\boldsymbol{P}(\boldsymbol{x})=\boldsymbol{I}-\boldsymbol{n}^{(i)}(\boldsymbol{x}) \otimes \boldsymbol{n}^{(i)}(\boldsymbol{x}), \tag{3}
$$

where $\boldsymbol{n}^{(i)}(\boldsymbol{x})$ is the outer unit normal vector at each point $\boldsymbol{x}$ of the interface $\Gamma^{(i)}$.

The field equations (2) and (3) are completed by the boundary conditions on the external boundary $\partial \Omega$ of the domain $\Omega$:

$$
\boldsymbol{\sigma} \cdot \boldsymbol{n}=\boldsymbol{F}, \text { on } \partial \Omega^{F}, \tag{4}
$$

$$
\boldsymbol{u}=\overline{\boldsymbol{u}}, \text { on } \partial \Omega^{\boldsymbol{u}}, \tag{5}
$$

with $\partial \Omega^{F} \cup \partial \Omega^{\boldsymbol{u}}=\partial \Omega$ and $\partial \Omega^{\boldsymbol{u}} \cap \partial \Omega^{F}=\emptyset$.

Additionally, the displacement continuity at the different interfaces is required:

$$
\boldsymbol{u}^{(\text {out })}-\boldsymbol{u}^{(\text {in })}=\boldsymbol{u}=0, \text { on } \Gamma^{(i)}. \tag{6}
$$

For the finite element calculation purpose, the local mathematical problem [Eqs. (1–6)] is reformulated by using the divergence theorem under the following variational form:

$$
\begin{aligned}
& \int_{\Omega^{(i)}} \boldsymbol{\sigma}^{(i)}(\boldsymbol{u}): \boldsymbol{\epsilon}^{(i)}(\delta \boldsymbol{u}) \mathrm{d} \Omega+\int_{\Gamma^{(i)}}\left(\boldsymbol{\sigma}^{(i)} \cdot \boldsymbol{n}^{(i)}\right) \cdot \delta \boldsymbol{u} \mathrm{d} \Gamma \\
& \quad-\int_{\Omega^{(i)}} \boldsymbol{b}^{(i)} \cdot \delta \boldsymbol{u} \mathrm{d} \Omega-\int_{\partial \Omega^{F}} \boldsymbol{F} \cdot \delta \boldsymbol{u} \mathrm{d} \Gamma=0.
\end{aligned} \tag{7}
$$

In Eq. (7), the unknown is the displacement vector $\boldsymbol{u}$ that is assumed to be sufficiently regular and kinematically admissible, i.e. verifying $\delta \boldsymbol{u}=0$ on $\partial \Omega^{\boldsymbol{u}}$.

After introducing the volume and interface behavior laws,

$$
\boldsymbol{\sigma}=\mathbb{C}: \boldsymbol{\epsilon}, \text { on } \Omega, \tag{8}
$$

and

$$
\boldsymbol{\sigma}^{\mathrm{s}}=\boldsymbol{\sigma}_{0}+\mathbb{C}^{\mathrm{s}}: \boldsymbol{\epsilon}^{\mathrm{s}}, \text { on } \Gamma_{I}, \tag{9}
$$

and using again the divergence transformation theorem, Eq. (7) becomes:

$$
\begin{aligned}
\int_{\Omega} & \boldsymbol{\epsilon}(\delta \boldsymbol{u}): \mathbb{C}: \boldsymbol{\epsilon}(\boldsymbol{u}) \mathrm{d} \Omega+\int_{\Gamma_{I}} \boldsymbol{P} \cdot \boldsymbol{\epsilon}(\delta \boldsymbol{u}) \cdot \boldsymbol{P}: \mathbb{C}^{\mathrm{s}}: \boldsymbol{P} \boldsymbol{\epsilon}(\boldsymbol{u}) \boldsymbol{P} \mathrm{d} \Gamma \\
= & \int_{\Omega} \delta \boldsymbol{u} \cdot \boldsymbol{b} \mathrm{d} \Omega+\int_{\partial \Omega^{F}} \delta \boldsymbol{u} \cdot \boldsymbol{F} \mathrm{d} \Gamma+\int_{\partial \Gamma_{I}} \boldsymbol{P} \cdot \delta \boldsymbol{u} \cdot \tilde{\boldsymbol{F}} \mathrm{d} l \\
& -\int_{\Gamma_{I}} \boldsymbol{P} \cdot \boldsymbol{\epsilon}(\delta \boldsymbol{u}) \cdot \boldsymbol{P}: \boldsymbol{\sigma}_{0} \mathrm{d} \Gamma.
\end{aligned} \tag{10}
$$

In Eqs. (8) and (9), $\Omega$ denotes the union of all $\Omega^{(i)}$ ($\Omega=\bigcup_{i=1}^{N} \Omega^{(i)}$) and $\Gamma_{I}$ denotes the union of all $\Gamma^{(i)}$ ($\Gamma=\bigcup_{i=1}^{N} \Gamma^{(i)}$), and the quantities $\boldsymbol{P} \cdot \boldsymbol{\epsilon} \cdot \boldsymbol{P}=\boldsymbol{\epsilon}^{\mathrm{s}}$ and $\boldsymbol{P} \cdot \boldsymbol{u}=\boldsymbol{u}^{\mathrm{s}}$ denote the surface strain tensor $\boldsymbol{\epsilon}^{\mathrm{s}}$ and the surface displacement vector $\boldsymbol{u}^{\mathrm{s}}$, respectively.

In Eq. (10), $\tilde{\boldsymbol{F}}$ is the applied force on $\partial \Gamma_{I}$. The corresponding integral on $\partial \Gamma_{I}$ vanishes if the interface $\Gamma_{I}$ is closed. $\mathbb{C}$ and $\mathbb{C}^{\mathrm{s}}$ are space-dependent isotropic elastic fourth order tensors of the volume $\Omega$ and surface $\Gamma_{I}$ domains. Precisely, $\mathbb{C}$ is null inside a void phase whereas $\mathbb{C}^{\mathrm{s}}$ changes from an interface to another according to the relation (see Ref. [6]):

$$
\mathbb{C}_{i j k l}^{\mathrm{s}}=\lambda_{\mathrm{s}} P_{i j} P_{k l}+\mu_{\mathrm{s}}\left(P_{i k} P_{j l}+P_{i l} P_{j k}\right), \tag{11}
$$

where $\lambda_{\mathrm{s}}$ and $\mu_{\mathrm{s}}$ are the surface Lamé’s constants and $\boldsymbol{P}$ is the surface projection operator expressed in Eq. (3).

Also in Eqs. (9) and (10), the stress $\boldsymbol{\sigma}_{0}$ is such that $\boldsymbol{\sigma}_{0}=\tau_{0} \boldsymbol{P}$, where $\tau_{0}$ represents a residual surface tension at the interface. $\tau_{0}$ is taken equal to 0 in the coming applications.

## 3 Numerical solution procedure: XFEM with the level-set technique

To solve the boundary value problem presented above, an approach using the XFEM combined with the level-set technique is deployed. The domain $(\Omega)$ is then discretized into a set of 3-node triangular elements $(P 1)$, whereas no node is specifically assigned to the interface $\Gamma^{(i)}$. This latter is geometrically described by a level-set function $\phi^{(i)}$, and is treated from the kinematic point of view by making use of the neighboring nodes, enriched for this purpose.

Each point of the interface $\Gamma^{(i)}$ is parameterized by a proper level-set function (see Ref. [28])

$$
\phi^{(i)}\left(x_{1}, x_{2}\right)=\left(\frac{\left|x_{1}-x_{1 c}\right|}{a_{1}}\right)^{p_{1}}+\left(\frac{\left|x_{2}-x_{2 c}\right|}{a_{2}}\right)^{p_{2}}-1, \quad(12)
$$

which is equal to zero when the point is on the interface $\Gamma^{(i)}$. When the point is inside $\Omega^{(i)}$, the function $\phi^{(i)}$ is negative,

![](./images/812782145717141505_2.jpg)

outside, $\phi^{(i)}$ is positive. Depending on the constants $x_{i c}, a_{i}$, and $p_{i}$, it is possible to consider different shapes of the interface (circle, ellipse, square, rhombus, etc.).

Each node in the neighborhood of the interface $\Gamma^{(i)}$ is assigned a value of the function $\phi_{j}^{(i)}$. It is then possible to define a polynomial interpolated function as, $\tilde{\phi}^{(i)}(\boldsymbol{x})=\sum_{j=1}^{n=3} N_{j}(\boldsymbol{x}) \phi_{j}^{(i)}$, where $N_{j}(\boldsymbol{x})$ is a 1-degree polynomial shape function. The function $\tilde{\phi}^{(i)}(\boldsymbol{x})$ will be used in the calculations, instead of the original one $\phi^{(i)}(\boldsymbol{x})$. Accordingly, for each point $\boldsymbol{x}=\left(x_{1}, x_{2}\right)$ of the interface $\Gamma^{(i)}$, the unit outer normal vector is defined as follows:

$$
\overline{\boldsymbol{n}}^{(i)}(\boldsymbol{x})=\frac{\nabla \tilde{\phi}^{(i)}(\boldsymbol{x})}{\nabla \tilde{\phi}^{(i)}(\boldsymbol{x})}, \tag{13}
$$

with

$$
\nabla \tilde{\phi}^{(i)}(\boldsymbol{x})_{k}=\sum_{j=1}^{n=3} \frac{\partial N_{j}(\boldsymbol{x})}{\partial x_{k}} \phi_{j}^{(i)},(k=1,2). \tag{14}
$$

For the 3-noded $P 1$ triangular element that is adopted here, the derivatives $\frac{\partial N_{j}(\boldsymbol{x})}{\partial x_{k}}$ are uniform functions.

The polynomial approximation of the elementary displacement vector is defined by [25]:

$$
\left[\begin{array}{l}
u(\boldsymbol{x}) \\
v(\boldsymbol{x})
\end{array}\right]^{h}=\sum_{i=1}^{n=3} N_{i}(\boldsymbol{x})\left(\begin{array}{l}
u_{i} \\
v_{i}
\end{array}\right)+\sum_{j=1}^{m \leq 3} N_{j}(\boldsymbol{x}) \psi(\boldsymbol{x})\left(\begin{array}{l}
a_{j} \\
b_{j}
\end{array}\right), \tag{15}
$$

where $\psi(\boldsymbol{x})$ is the enrichment function defined on the domain $(\Omega^{(i)})$. When $\Omega^{(i)}$ corresponds to an inclusion (not a void/cavity), we adopt for $\psi(\boldsymbol{x})$ the following form,

$$
\psi(\boldsymbol{x})=\sum_{j=1}^{n}\left|\phi_{j}^{(i)}\right| N_{j}(\boldsymbol{x})-\left|\sum_{i=1}^{n} \phi_{j}^{(i)} N_{j}(\boldsymbol{x})\right|. \tag{16}
$$

Initially proposed by Moës et al. [27], the enrichment function in Eq. (16) is used here to meet the continuity conditions at the interfaces (continuity of displacements and discontinuities of the traction vector or deformations) by using additional degrees of freedom, without disturbing/falsifying the displacements of the enriched neighboring nodes.

In the presence of a void/cavity instead of an inclusion, another enrichment function, namely $V(\boldsymbol{x})$, is used, defined as:

$$
V(\boldsymbol{x})=\left\{\begin{array}{l}
1, \text { if } \boldsymbol{x} \in \Omega^{(i)}, \\
0, \text { if } \boldsymbol{x} \notin \Omega^{(i)}.
\end{array}\right. \tag{17}
$$

For the needs of the different numerical integrations, the interface is geometrically discretized. The position of each discretization point depends on the position of the neighboring nodes and their level function $\phi^{(i)}$ values, according to the formula:

$$
\bar{x}=f\left(\bar{x}_{k}, \phi_{k}^{(i)}, \bar{x}_{l}, \phi_{l}^{(i)}\right), \tag{18}
$$

$$
\bar{x}=\bar{x}_{k}+\xi\left(\bar{x}_{l}-\bar{x}_{k}\right), \quad \text { with } \xi=-\frac{\phi_{k}^{(i)}}{\phi_{l}^{(i)}-\phi_{k}^{(i)}}. \tag{19}
$$

![](./images/812782145717141505_3.jpg)
Fig. 2 Geometrical discretization of the interface

This is a linear interpolation as shown in Fig. 2. The interface subdivision thus defined enables us to calculate the contour integrals in Eq. (9). It should also be noted that the intersections between the elements and the interface generate triangular sub-elements as shown in Fig. 3. These sub-elements are also used in numerical integrations by adopting the appropriate number of Gauss integration points.

As announced formerly, the present study that concerns the effect of nano-voids/nano-cavities on the effective behavior of a medium, also covers the case of nano-voids/nano-cavities shrinking to nano-cracks. For the comparison purpose, the case of cracked medium is also specifically solved by XFEM, by considering special enrichment for the elements cut by crack. This enrichment is of Heaviside type, $H(\boldsymbol{x})$. It is used in the interpolated displacement that is of similar form as Eq. (15):

$$
\left[\begin{array}{l}
u(\boldsymbol{x}) \\
v(\boldsymbol{x})
\end{array}\right]^{h}=\sum_{i=1}^{n=3} N_{i}(\boldsymbol{x})\left(\begin{array}{l}
u_{i} \\
v_{i}
\end{array}\right)+\sum_{j=1}^{m \leq 3} N_{j}(\boldsymbol{x}) H(\boldsymbol{x})\left(\begin{array}{l}
a_{j} \\
b_{j}
\end{array}\right), \tag{20}
$$

where

$$
H(\boldsymbol{x})=\left\{\begin{array}{cl}
1, & \text { if } \chi(\boldsymbol{x})>0, \\
-1, & \text { if } \chi(\boldsymbol{x})<0.
\end{array}\right. \tag{21}
$$

Besides the Heaviside function $H(\boldsymbol{x})$ that is used instead of $\psi(\boldsymbol{x})$ in Eq. (20), another level-set function $\chi(\boldsymbol{x})$, not given here, is used in Eq. (21) instead of $\phi(\boldsymbol{x})$ in Eq. (12).

![](./images/812782145717141505_4.jpg)

![](./images/812782145717141505_5.jpg)

Fig. 3 Splitting of an element crossed/cut by an interface

Taking into account the polynomial approximation [Eq. (15)] of the displacement in the weak formulation [Eq. (10)], leads to the following system of linear algebraic equations:
$$
\left(\boldsymbol{K}+\boldsymbol{K}^{\mathrm{s}}\right) \boldsymbol{U}=\boldsymbol{R},
\tag{22}
$$
with
$$
\boldsymbol{K}=\sum_{N_{\mathrm{e}}} \int_{\Omega^{\mathrm{e}}} \boldsymbol{B}^{\mathrm{T}} \boldsymbol{C B} \gamma \mathrm{d} \Omega,
\tag{23}
$$

$$
\boldsymbol{K}^{\mathrm{s}}=\sum_{N_{\mathrm{e}}} \int_{\Gamma_{I}^{\mathrm{e}}} \boldsymbol{B}^{\mathrm{T}} \boldsymbol{M}_{p}^{\mathrm{T}} \boldsymbol{C}^{\mathrm{s}} \boldsymbol{M}_{p} \boldsymbol{B} \gamma \mathrm{d} \Gamma,
\tag{24}
$$

$$
\boldsymbol{C}^{\mathrm{s}}=\left[\begin{array}{cccc}
\left(2 \mu_{\mathrm{s}}+\lambda_{\mathrm{s}}\right) P_{11}^{2} & \lambda_{\mathrm{s}} P_{11} P_{22}+2 \mu_{\mathrm{s}} P_{12}^{2} & \alpha \lambda_{\mathrm{s}} P_{11} & \left(2 \mu_{\mathrm{s}}+\lambda_{\mathrm{s}}\right) P_{11} P_{12} \\
\lambda_{\mathrm{s}} P_{11} P_{22}+2 \mu_{\mathrm{s}} P_{12}^{2} & \left(2 \mu_{\mathrm{s}}+\lambda_{\mathrm{s}}\right) P_{22}^{2} & \alpha \lambda_{\mathrm{s}} P_{22} & \left(2 \mu_{\mathrm{s}}+\lambda_{\mathrm{s}}\right) P_{11} P_{12} \\
\alpha \lambda_{\mathrm{s}} P_{11} & \alpha \lambda_{\mathrm{s}} P_{22} & \alpha\left(2 \mu_{\mathrm{s}}+\lambda_{\mathrm{s}}\right) & \alpha \lambda_{\mathrm{s}} P_{12} \\
\left(2 \mu_{\mathrm{s}}+\lambda_{\mathrm{s}}\right) P_{11} \mathrm{P}_{12} & \left(2 \mu_{\mathrm{s}}+\lambda_{\mathrm{s}}\right) P_{11} P_{12} & \alpha \lambda_{\mathrm{s}} P_{12} & \lambda_{\mathrm{s}} P_{12}^{2}+\mu_{\mathrm{s}}\left(P_{11} P_{12}+P_{12}^{2}\right)
\end{array}\right].
\tag{28}
$$

$$
\begin{aligned}
\boldsymbol{R}= & \sum_{N_{\mathrm{e}}} \int_{\Omega^{\mathrm{e}}} \boldsymbol{N}^{\mathrm{T}} \boldsymbol{b} \gamma \mathrm{d} \Omega+\int_{\partial \Omega^{\mathrm{e}}} \boldsymbol{N}^{\mathrm{T}} \boldsymbol{F} \gamma \mathrm{d} \Gamma \\
& +\int_{\partial \Gamma_{I}^{\mathrm{e}}} \boldsymbol{N}^{\mathrm{T}} \boldsymbol{P} \tilde{\boldsymbol{F}} \gamma \mathrm{d} l-\int_{\Gamma_{I}^{\mathrm{e}}} \boldsymbol{B}^{\mathrm{T}} \boldsymbol{M}_{p}^{\mathrm{T}} \boldsymbol{\sigma}_{0} \gamma \mathrm{d} \Gamma.
\end{aligned}
\tag{25}
$$

Relations (23)–(25) define the bulk stiffness matrix, the surface stiffness matrix and the nodal force vector. In Eq. (22), $\boldsymbol{U}$ is the nodal displacement vector $\boldsymbol{U}=\left(u_{1} v_{1} \ldots u_{N} v_{N} a_{1} b_{1} \ldots a_{M} b_{M}\right)^{\mathrm{T}}$ where $N=6 × N_{\mathrm{e}}$ and $M \leq 6 × N_{\mathrm{e}}$ with $N_{\mathrm{e}}$ being the number of elements.

Equations (22)–(25) are valid for plane strain $[\gamma=1$ in Eqs. (23)–(25)] and axisymmetric problems. For both problems, the adopted expression of strain and stress are:
$$
\boldsymbol{\epsilon}=\left[\begin{array}{c}
\epsilon_{11} \\
\epsilon_{22} \\
\alpha \epsilon_{33} \\
2 \epsilon_{12}
\end{array}\right], \quad \boldsymbol{\sigma}=\left[\begin{array}{c}
\sigma_{11} \\
\sigma_{22} \\
\alpha \sigma_{33} \\
\sigma_{12}
\end{array}\right],
\tag{26}
$$
in which $\alpha=0$ and $\alpha=1$ for plane strain and axisymmetric configuration, respectively.

The behavior of domain $\Omega(=\bigcup_{i=1}^{N} \Omega^{(i)})$ being linearly elastic and isotropic, the spatially variable stiffness tensor $\boldsymbol{C}$ in Eq. (23) takes the form:
$$
\boldsymbol{C}=\left[\begin{array}{cccc}
\lambda+2 \mu & \lambda & \alpha \lambda & 0 \\
\lambda & \lambda+2 \mu & \alpha \lambda & 0 \\
\alpha \lambda & \alpha \lambda & \alpha(\lambda+2 \mu) & 0 \\
0 & 0 & 0 & \mu
\end{array}\right],
\tag{27}
$$
where $\lambda$ and $\mu$ are the Lamé constants. These constants tend towards zero for nano-cavities and nano-cracks.

The surface elasticity tensor in Eq. (24) has an expression that depends of the surface projection operator $\boldsymbol{P}$ defined in Eq. (3), as follows:

The matrix $\boldsymbol{M}_{p}$ used in Eqs. (24) and (25) is given by:
$$
\boldsymbol{M}_{p}=\left[\begin{array}{cccc}
P_{11}^{2} & P_{11}^{2} & 0 & P_{11} P_{12} \\
P_{11}^{2} & P_{11}^{2} & 0 & P_{12} P_{22} \\
0 & 0 & \alpha & 0 \\
2 P_{11} P_{12} & 2 P_{12} P_{22} & 0 & P_{11} P_{12}+P_{12}^{2}
\end{array}\right].
\tag{29}
$$

The strain interpolation sub-matrix used in Eqs. (23)–(25) stands as:
$$
\boldsymbol{B}=\left[\begin{array}{cccccc}
\frac{\partial N_{1}}{\partial x_{1}} & 0 & \frac{\partial N_{2}}{\partial x_{1}} & 0 & \frac{\partial N_{3}}{\partial x_{1}} & 0 \\
0 & \frac{\partial N_{1}}{\partial x_{2}} & 0 & \frac{\partial N_{2}}{\partial x_{2}} & 0 & \frac{\partial N_{3}}{\partial x_{2}} \\
\alpha \frac{N_{1}}{x_{1}} & 0 & \alpha \frac{N_{2}}{x_{1}} & 0 & \alpha \frac{N_{3}}{x_{1}} & 0 \\
\frac{\partial N_{1}}{\partial x_{2}} & \frac{\partial N_{1}}{\partial x_{1}} & \frac{\partial N_{2}}{\partial x_{2}} & \frac{\partial N_{2}}{\partial x_{1}} & \frac{\partial N_{3}}{\partial x_{2}} & \frac{\partial N_{3}}{\partial x_{1}}
\end{array}\right],
\tag{30}
$$
for a non-cut element, and as,

$$
\boldsymbol{B}=\left[\begin{array}{cccccccccc}
\frac{\partial N_{1}}{\partial x_{1}} & 0 & \frac{\partial N_{2}}{\partial x_{1}} & 0 & \frac{\partial N_{3}}{\partial x_{1}} & 0 & \frac{\partial \hat{N}_{1}}{\partial x_{1}} & 0 & \frac{\partial \hat{N}_{2}}{\partial x_{1}} & 0 & \frac{\partial \hat{N}_{3}}{\partial x_{1}} & 0 \\
0 & \frac{\partial N_{1}}{\partial x_{2}} & 0 & \frac{\partial N_{2}}{\partial x_{2}} & 0 & \frac{\partial N_{3}}{\partial x_{2}} & 0 & \frac{\partial \hat{N}_{1}}{\partial x_{2}} & 0 & \frac{\partial \hat{N}_{2}}{\partial x_{2}} & 0 & \frac{\partial \hat{N}_{3}}{\partial x_{2}} \\
\alpha \frac{N_{1}}{x_{1}} & 0 & \alpha \frac{N_{2}}{x_{1}} & 0 & \alpha \frac{N_{3}}{x_{1}} & 0 & \alpha \frac{\hat{N}_{1}}{x_{1}} & 0 & \alpha \frac{\hat{N}_{2}}{x_{1}} & 0 & \alpha \frac{\hat{N}_{3}}{x_{1}} & 0 \\
\frac{\partial N_{1}}{\partial x_{2}} & \frac{\partial N_{1}}{\partial x_{1}} & \frac{\partial N_{2}}{\partial x_{2}} & \frac{\partial N_{2}}{\partial x_{1}} & \frac{\partial N_{3}}{\partial x_{2}} & \frac{\partial N_{3}}{\partial x_{1}} & \frac{\partial \hat{N}_{1}}{\partial x_{2}} & \frac{\partial \hat{N}_{1}}{\partial x_{1}} & \frac{\partial \hat{N}_{2}}{\partial x_{2}} & \frac{\partial \hat{N}_{2}}{\partial x_{1}} & \frac{\partial \hat{N}_{3}}{\partial x_{2}} & \frac{\partial \hat{N}_{3}}{\partial x_{1}}
\end{array}\right],
$$

with $\hat{N}_{I}=\psi N_{I}$ for a cut element.

Remarks It is worth noting that the matrix $\boldsymbol{B}$ in Eq. (30) is defined without considering any enrichment. It is suitable for any element of the domain $(\Omega)$ that is not cut by the contour of an inclusion and for an element, which is cut by the contour of a void/cavity, as well. In fact, since the inclusion is a void/cavity, the element nodal displacement is not enriched.

When an element is cut by an inclusion contour, the matrix $\boldsymbol{B}$ is enriched by as many columns as additional used degrees of freedom [Eq. (15)]. In Eq. (31), it was assumed that all three nodes of the triangular element were enriched.

Equations (23)-(25) contain volume integrals (on $\Omega$) that are analytically computed for uncut elements over which the matrix $\boldsymbol{B}$ is uniform (shape functions $P 1$ : polynomial function of degree 1). In case of cut elements, the volume integrals are numerically evaluated by subdividing cut elements into triangular sub-elements (see Fig. 3). Three Gauss integration points are considered for the numerical integration over each sub-element. For the surface integrals (on $\Gamma^{(i)}$ ), only cut elements are concerned in this calculation. Indeed, the interface $(\Gamma^{(i)})$ is discretized by segments $\Delta \Gamma^{(i)}$ defined by $\phi^{(i)}(x)=0$, whose extremities are determined according to the procedure described in Eqs. (18) and (19) and Fig. 2.

Equations above have been implemented and solved numerically for the particular problem of homogenization of a material containing nano-heterogeneities. The concept of representative elementary volume (REV) was used therein, with different possible arrangements (square, hexagonal, random) for the inclusions or voids. Also, different boundary conditions have been considered, such as imposed average strain or periodic displacement. In this paper, only the periodic displacements conditions have been considered. This gave rise to a simulation tool that enables to study the effect of nano-heterogeneities on the effective stiffness of a medium. It was possible to consider a single or multiple nano-heterogeneities that are stiffer or softer than the parent material (matrix), or even without stiffness as in the case of voids/cavities. For the latter, we chose to flatten them until they shrink to nano-cracks. All these calculations have been performed by accounting of interface/free surface effects through a specific energy contribution.

The next section is dedicated to the simulations performed to validate the developed numerical tool and to show its predictive capabilities. Different applications have been addressed, in relation with the effect of cylindrical (circular or elliptical in 2D) nano-voids/nano-cavities and plane (line in 2D) nano-cracks on the effective stiffness of a material.

![](./images/812782145717141505_6.jpg)

Fig.4 Hexagonal arrangement of voids. a Considered REV. b Meshed part

## 4 Applications and numerical studies

### 4.1 Case of hexagonally distributed cylindrical voids in an aluminium matrix

Hexagonal arrangement of voids (see Fig. 4) is considered in an aluminum matrix with surface effects. The properties of the linearly elastic and isotropic aluminum are $E_{\mathrm{M}}=70 \mathrm{GPa}$ and $\nu_{\mathrm{M}}=0.32$.

For the surface properties of the interface, three cases are considered regarding the surface bulk modulus $K_{\mathrm{s}}^{\prime}$ defined as $K_{\mathrm{s}}^{\prime}=\left(\lambda_{\mathrm{s}}+2 \mu_{\mathrm{s}}\right)$, as in Refs. [5, 6, 12]. The three cases are:

$$\lambda_{\mathrm{s}}=3.48912 \mathrm{~N} \cdot \mathrm{m}, \mu_{\mathrm{s}}=-6.2178 \mathrm{~N} \cdot \mathrm{m}=>K_{\mathrm{s}}^{\prime}<0, \quad(32)$$

$$\lambda_{\mathrm{s}}=6.84200 \mathrm{~N} \cdot \mathrm{m}, \mu_{\mathrm{s}}=-0.3750 \mathrm{~N} \cdot \mathrm{m}=>K_{\mathrm{s}}^{\prime}>0, \quad(33)$$

$$\lambda_{\mathrm{s}}=0 \mathrm{~N} \cdot \mathrm{m}, \mu_{\mathrm{s}}=0 \mathrm{~N} \cdot \mathrm{m}=>K_{\mathrm{s}}^{\prime}=0. \quad(34)$$

The Lamé's constants $\lambda_{\mathrm{s}}$ and $\mu_{\mathrm{s}}$ have been obtained by Miller and Shenoy thanks to ab initio calculations [2].

The obtained numerical results concerning the normalized in-plane bulk modulus, $(k^{*}=\frac{k^{\prime}}{k_{M}^{\prime}}$ with $k^{\prime}=(\lambda+2 \mu) / 3)$, are reported in Fig. 5. They are compared with the results obtained by Yvonnet et al. [6] and Quang and He [12] for the validation purpose of the developed code.

The curves depicted in Fig. 5a, b of the normalized in-plane bulk modulus versus void radius and volume fraction, show a good agreement between the present calculations

![](./images/812782145717141505_7.jpg)

![](./images/812782145717141505_8.jpg)

Fig. 5 Normalized in-plane bulk modulus versus. a Void radius. b Void volume fraction

Table 1 Normalized in-plane
bulk modulus for different mesh
densities (void radius $R_{0}=1$ nm;
void volume fraction $f_{0}=0.2$)

<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="6">Mesh density</th>
      <th>Analytical results [12]</th>
    </tr>
    <tr>
      <th></th>
      <th>10×10</th>
      <th>20×20</th>
      <th>30×30</th>
      <th>40×40</th>
      <th>50×50</th>
      <th>60×60</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$k'(K_{s}'>0)$</td>
      <td>0.5671</td>
      <td>0.5620</td>
      <td>0.5611</td>
      <td>0.5607</td>
      <td>0.5605</td>
      <td>0.5605</td>
      <td>0.5603</td>
    </tr>
    <tr>
      <td>$k'(K_{s}'<0)$</td>
      <td>0.4424</td>
      <td>0.4375</td>
      <td>0.4363</td>
      <td>0.4363</td>
      <td>0.4360</td>
      <td>0.4360</td>
      <td>0.4358</td>
    </tr>
  </tbody>
</table>

and the ones of Yvonnet et al. [6] and Quang and He [12] obtained numerically and analytically, respectively. In particular, the results show the role of interface/surface energy $(K_{s}'≠0)$, which differs from the case without interface/ surface energy $(K_{s}'=0)$, when the void radius is relatively small. Depending on the interface/surface properties, one observes either an increase of the medium effective modulus $(K_{s}'>0)$, or a decrease $(K_{s}'<0)$ compared to the case without interface/surface energy $(K_{s}'=0)$. An increase of the radius yields to a decrease of the effect of the surface energy on the effective modulus. Moreover, for a constant radius ($R_{0}=1$ nm), an increase of the volume fraction of the nano-void yields to a decrease of the effective modulus in all cases. This decrease, however, is less for $K_{s}'>0$, and more for $K_{s}'<0$ than the case $K_{s}'=0$.

Different mesh densities have been used to examine the mesh-dependency of the numerical results in both cases (negative and positive surface bulk moduli). The obtained results reported in Table 1 show that there is no mesh- dependency as the computed effective modulus stabilizes after a sufficiently refined meshing.

![](./images/812782145717141505_9.jpg)

Fig. 6 Normalized in-plane bulk modulus ($k^{* \prime}=k'/max(k_{M},k_{F})$ ver-
sus the contrast $\lg(E_{M}/E_{F}))$

### 4.1.1 Effect of the contrast $E_{M}/E_{F}$

Actually, the role of the surface energy defined by $K_{s}'$ strongly depends on the ratio between the rigidity of the matrix and that of the inclusion or void/cavity. To show this effect, we performed a numerical study concerning the

![](./images/812782145717141505_10.jpg)

![](./images/812782145717141505_11.jpg)

Fig. 7 Normalized in-plane bulk modulus versus the void radius under 0.5 nm for different void volume fractions

influence of $E_{\mathrm{M}} / E_{\mathrm{F}}$, on the medium effective properties, by considering the different surface behaviors Eqs. (32)-(34).

The obtained numerical results are summarized in Fig. 6. They show that once the matrix is more flexible than the inclusion, no influence of the interface/surface behavior, materialized by $K_{\mathrm{s}}^{\prime}$, is noticed on the calculated in-plane effective modulus. In addition, for a relatively very flex- ible matrix, the calculated effective modulus tends to zero, which is physically a realistic trend. For a stiffer matrix, as in the presence of void/cavity, we notice an effect of the surface energy through $K_{\mathrm{s}}^{\prime}$, which stabilizes beyond a certain contrast.

After this initial validation, the numerical tool is used in the subsequent sections to simulate different physical configurations. The first one concerns the case when the void radius becomes very small (less than 0.5 nm), in which a very interesting emerging tendency, regarding the effec- tive behavior, has been captured by the simulation tool. The second treated situation concerns multiple randomly dis- tributed voids. For this situation we also consider the case when the nano-voids/nano-cavities flatten until to shrink to nano-crack-like. All these situations are treated by consid- ering the surface energy contribution, for accounting of the nano-metric size and the physical interactions matrix/nano- heterogeneities, at this scale.

### 4.1.2 An interesting case of very small void radius
We keep the same evaluation procedure as before concerning $E_{\mathrm{M}}, v_{\mathrm{M}}$ and $K_{\mathrm{s}}^{\prime}$. The effective bulk modulus is calculated for different assumed values of the void radius $(R_{0})$ in the inter val [0, 0.5 nm] and for a void volume fraction (f) between0.1 and 0.6.

From Fig. 7, we observe that, in the presence of nano- void/nano-cavity, the effective stiffness of the medium is lower than that of the matrix as long as the radius is greater than a critical (and purely theoretical) value $R_{0}^{\mathrm{c}}=0.04 ~nm$ . Below that, the overall effective rigidity exceeds that of the matrix. In addition, the increase of the void volume fraction becomes uncommonly favorable to the increase of the stiff- ness contrary to what happens for $R>R_{0}^{c}=0.04 ~nm$ .

When $R=R_{0}^{c}=0.04 ~nm$ , the overall effective stiffness is equal to that of the matrix whatever the volume fraction of the voids/cavities. In addition, below $R_{0}^{c}=0.04 ~nm$ , the overall effective stiffness increases sharply by decreasing $R_{0}$ . This strong increase is even more important for higher void volume fraction, i.e. a material as light as desired but with increasing stiffness!

### 4.2 Case of randomly distributed multiple nano-voids with constant volume fraction
We keep the same aluminum matrix, which contains now randomly distributed nano-voids, as shown in Fig. 8.

In order to study the effects of the size of nano-voids on the effective properties of a medium, we consider 30 circular voids randomly distributed. The size of the square medium domain is fixed such that the volume fraction is kept equal to $f=0.3$ , while varying the radius of the voids. To get sta tistically representative values of the computed properties, several realizations are performed, up to 40 in order to stabi- lize the average results as shown in Fig. 9a. The graph shows an increase in the effective stiffness with the decrease of the nano-void radius. At 40 realizations, the results obtained are grouped and compared with those found by Yvonnet et al.[6] in Fig. 9b. We observe a very good agreement between the two results.

### 4.3 Case of a nano-void flattened towards a nano-crack
We keep the same aluminum matrix, and we consider the case of nano-void, which flattens and gradually tends towards a nano-crack. The questions we answer in the fol- lowing are: how does the effective stiffness of the medium evolve when the void volume fraction becomes null for the crack configuration? Does the surface energy as it was mod- eled by Young-Laplace equations, continue to have an influ- ence for nano-cracks?

We define two geometry characteristics for this applica- tion, a surface fraction index $f^{\prime}=a / w$ , and the flattening coefficient $c=a / b$ , (see Fig. 10). The volume fraction of the void is then equal to $\pi f^{\prime} /(2 c)$ . In the following, the surface fraction index is maintained equal to $f'=0.4$ , the flatten ing coefficient is variable, between 0 and 40 (for $c=40$ and $f'=0.4, f \sim 1.6 \%)$ .

![](./images/812782145717141505_12.jpg)

![](./images/812782145717141505_13.jpg)

Fig. 8 Randomly distributed 30 voids with volume fraction $f=0.3$

![](./images/812782145717141505_14.jpg)

Fig. 9 a Statistical convergence of the normalized effective in-plane bulk modulus versus the number of realizations for different radius of the nano-void. b Normalized effective in-plane bulk modulus after 40 realizations versus nano-void radius

### 4.3.1 Without surface energy

We first calculate the normalized effective elastic modulus by considering $K_{\mathrm{s}}^{\prime}=0$, i.e. without surface energy.

The results of the calculations reported in Fig. 11 show an effective elastic modulus that increases very rapidly with the flattening coefficient $c$, i.e. when the nano-void closes. The elastic property corresponding to a flattened void tends

![](./images/812782145717141505_15.jpg)

![](./images/812782145717141505_16.jpg)

Fig. 10 Flattened nano-void

![](./images/812782145717141505_17.jpg)

Fig. 11 Normalized in-plane bulk modulus and void volume fraction versus the flattening coefficient

towards the case of a crack very quickly regarding $c$ (when it is barely greater than 5), with also a very sharp decrease in the void volume fraction. In presence of cracks only, the medium is stiffer than what it is in presence of voids/cavities. However, the cracked medium is still softer than the matrix. This proves once more the good predictive capability of the developed code, which also captures the effect on the elastic properties of cracks.

It should be noted that in order to obtain the value of the effective modulus corresponding to the limit case of flattened nano-voids (almost nano-cracks), it was necessary to use successive refined meshes. The use of Heaviside enrichment in XFEM (in Eq. (20)) during the treatment of the problem with cracks only, makes it possible to obtain the value of the effective elastic modulus without densifying the mesh, as was the case for flattened nano-voids.

The results in Fig. 11 concerning the in-plane bulk modulus versus the flattening coefficient, have been obtained without considering the surface energy, i.e. for $K_{\mathrm{s}}^{\prime}=0$. In the following, the surface energy will be taken into account.

![](./images/812782145717141505_18.jpg)

Fig. 12 Normalized effective elastic stiffness versus the flattening coefficient $c$ for different values of $K_{\mathrm{s}}^{\prime}$

### 4.4 With surface energy

The effect of flattening is now studied for the previous conditions $(f^{\prime}=0.4, E_{\mathrm{M}}=70 \mathrm{GPa}, \nu_{\mathrm{M}}=0.32)$, by considering the surface energy contributions corresponding to $K_{\mathrm{s}}^{\prime}>0$ and $K_{\mathrm{s}}^{\prime}<0$, [Eqs. (32) and (33)]. The obtained variations of the normalized effective elastic stiffness versus the flattening coefficient $c$ are displayed in Fig. 12.

The graph of Fig. 12 shows that the normalized effective elastic stiffness inevitably converges towards the result of a "simple" crack, even with taking into account of a surface energy. However, the convergence is not the same as in the case without surface energy $(K_{\mathrm{s}}^{\prime}=0)$. For $K_{\mathrm{s}}^{\prime}>0$, the increase is faster with $c$, and even exceeds the effective modulus corresponding to a crack for some flattening ratios less than 20, before decreasing trend towards the value corresponding to a crack, when $c$ is precisely close to 20. In the case $K_{\mathrm{s}}^{\prime}<0$, the increase is slower, and the effective elastic modulus stays low longer regarding $c$, before tending to the crack value, later for $c$ around 30. These results show for which flattening coefficient the surface energy, as it was described by Laplace-Young equations, may be important, and when its effect vanishes.

#### 4.4.1 Case of multiple nano-cracks

In this last application, we use the developed code to estimate the effective bulk modulus of a REV under the same conditions as in the previous applications $(f^{\prime}=0.4$, $E_{\mathrm{M}}=70 \mathrm{GPa}, \nu_{\mathrm{M}}=0.32)$. The REV contains either a single crack or multiple cracks and, in all cases, a fixed total length of cracks, which is equal to that of the single crack (this situation corresponds to a fixed crack density). The cases of cracks oriented successively at $0^{\circ}$ and $90^{\circ}$, and

![](./images/812782145717141505_19.jpg)

![](./images/812782145717141505_20.jpg)

Fig. 13 Nano-cracks oriented at $\theta=0^{\circ}$ parallel to $x$-axis

![](./images/812782145717141505_21.jpg)

Fig. 14 Nano-cracks oriented at $\theta=90^{\circ}$ perpendicular to $x$-axis

randomly with regard to $x$-axis of the referential frame are considered, as in displayed Figs. 13, 14, 15. It should be mentioned that when the number of crack is relatively high and consequently the cracks are small (as in the case of 20 cracks, the last frame in Figs. 13, 14, 15, it was necessary to densify the meshing (at least three elements per crack) in order to ensure convergence.

The results of the various simulations related to multiple nano-cracks are reported in Fig. 16. They all show that, with respect to the effective modulus, the increase in the number of cracks for the same crack total length is favorable to the medium stiffness. The value of this latter stabilizes for a small number of small nano-cracks (less than 10). This calculation indicates that the damage felt by the material is greater when it is circumscribed to a smaller number of cracks. The effective stiffness corresponding to the cracks oriented at $90^{\circ}$ with respect to $x$-axis, is higher than that obtained in the case of horizontal cracks. This tendency is not due to the loading conditions as the material stiffness should not depend on the loading conditions, but it is purely related to the orientation of the cracks with regards to the frame axes.

By considering randomly oriented cracks, and after carrying out several realizations (5, 10, 20, and 30) to estimate the effective modulus, it is observed that for this configuration, relatively closer to the reality of structures damaged by nano-cracks, the calculation also shows an increase in effective stiffness with the number of cracks, which remains between those of $0^{\circ}$ and $90^{\circ}$ orientations. In addition, the effective modulus stabilizes at a value close to the most unfavorable case, horizontal cracks, when the number of cracks increases.

![](./images/812782145717141505_22.jpg)

![](./images/812782145717141505_23.jpg)

Fig. 15 Nano-cracks randomly oriented

![](./images/812782145717141505_24.jpg)

Fig. 16 Normalized effective bulk modulus versus the number cracks for different crack orientations

## 5 Concluding remarks

In this work, a periodic numerical homogenization tool in 2D has been developed based on XFEM and level-set. This numerical simulation tool enables to study the elastic properties of a medium containing single (or multiple) elliptical void(s)/cavity(ies) with a shape ratio, ranging from 1 (cylinder/circle in 2D) to almost 0 (plane crack/line in 2D), in a relatively general context, i.e. without any restriction with respect to interactions, the size of heterogeneities, their numbers, their orientations, and by taking into account the interface/surface energy or force, in order to account for the nanoscopic nature of the heterogeneities.

Among the findings of this work after the performed simulations by using the developed simulation code, some of the salient features are as follows.

(1) The existence, for the adopted interface/free surface Laplace–Young model, of a theoretical size of nano-void/nano-cavity below which, the porous matrix becomes stiffer than the matrix itself (free from voids/cavities).

(2) The numerical demonstration that by flattening void/cavity, its effect on the effective elasticity of a medium coincides with that of a crack of a comparable size, with the evanescence of the free surface energy contribution, when the void becomes crack-like.

(3) The numerical evidence that by multiplying cracks (for the same total length, i.e. for a fixed crack density), the cracked medium effective stiffness, at least for the bulk modulus, deteriorates less as it increases by multiplying smaller cracks for the same crack total length.

(4) The numerical evidence that horizontal cracks, with regards to the referential frame, are less favorable than vertical cracks for the effective elastic properties, at least for the in-plane bulk modulus.

(5) The numerical demonstration that randomly oriented cracks give an effective modulus lying between those of the horizontal and vertical cracks with respect to the referential frame.

![](./images/812782145717141505_25.jpg)

(6) The numerical evidence that by increasing the number of randomly oriented cracks, the elastic properties tend towards the most unfavorable case that of horizontal cracks, at least for the in-plane effective bulk modulus.

In fact, the developed numerical simulation tool is even more general, since it allows simulating other boundary conditions for the homogenization problem, such as the assumed average strain or stress. It also enables to study the effect of the void shape, to consider several heterogeneities in the same time, like inclusions of different shapes that are softer or stiffer than the matrix, by also considering the interface/surface effect, without restriction on the interaction between all these heterogeneities.

## References

1. Wang, J.X., Huang, Z.P., Duan, H.L., et al.: Surface stress effect in mechanics of nanostructured materials. Acta Mech. Solida Sin. **24**, 52–82 (2011)
2. Miller, R.E., Shenoy, V.B.: Size-dependent elastic properties of nanosized structural elements. Nanotechnology **11**, 139–147 (2000)
3. Kango, S., Kalia, S., Celli, A., et al.: Surface modification of inorganic nanoparticles for development of organic-inorganic nanocomposites—a review. Prog. Polym. Sci. **38**, 1232–1261 (2013)
4. Li, D.L., Zhou, H.S., Honma, I.: Design and synthesis of self-ordered mesoporous nanocomposite through controlled in situ crystallization. Nat. Mater. **3**, 65–71 (2004)
5. Duan, H.L., Wang, J., Karihaloo, B.L., et al.: Nanoporous materials can be made stiffer than non-porous counterparts by surface modification. Acta Mater. **54**, 2983–2990 (2006)
6. Yvonnet, J., Le Quang, H., He, Q.C.: An XFEM/level set approach to modelling surface/interface effects and to computing the size-dependent effective properties of nanocomposites. Comput. Mech. **42**, 119–131 (2008)
7. Sharma, P., Ganti, S., Bhate, N.: Effect of surfaces on the size-dependent elastic state of nano-inhomogeneities. Appl. Phys. Lett. **89**, 049901 (2006)
8. Ren, S.C., Liu, J.T., Gu, S.T., et al.: An XFEM-based numerical procedure for the analysis of poroelastic composites with coherent imperfect interface. Comput. Mater. Sci. **94**, 173–181 (2014)
9. Yao, Y., Chen, S.H., Fang, D.N.: An interface energy density-based theory considering the coherent interface effect in nanomaterials. J. Mech. Phys. Solids **99**, 321–337 (2017)
10. Sundararajan, S., Bhushan, B., Namazu, T., et al.: Mechanical property measurements of nanoscale structures using an atomic force microscope. Ultramicroscopy **91**, 111–118 (2002)
11. Tan, E.P.S., Lim, C.T.: Mechanical characterization of nanofibers—a review. Compos. Sci. Technol. **66**, 1099–1108 (2006)
12. Quang, H.L., He, Q.C.: Estimation of the effective thermoelastic moduli of fibrous nanocomposites with cylindrically anisotropic phases. Arch. Appl. Mech. **79**, 225–248 (2009)
13. Zheng, Z.M., Wang, B.: A prediction model for the effective thermal conductivity of nanofluids considering agglomeration and the radial distribution function of nanoparticles. Acta Mech. Sin. **34**, 507–514 (2018)
14. Natarajan, S., Haboussi, M., Manickam, G.: Application of higher-order structural theory to bending and free vibration analysis of sandwich plates with CNT reinforced composite facesheets. Compos. Struct. **113**, 197–207 (2014)
15. Sankar, A., Natarajan, S., Haboussi, M., et al.: Panel flutter characteristics of sandwich plates with CNT reinforced facesheets using an accurate higher-order theory. J. Fluids Struct. **50**, 376–391 (2014)
16. Challab, N., Zighem, F., Faurie, D., et al.: Local stiffness effect on ferromagnetic response of nanostructure arrays in stretchable systems. Phys. Status Solidi-Rapid Res. Lett. (2018). https://doi.org/10.1002/pssr.201800509
17. Haboussi, M., Sankar, A., Ganapathi, M.: Nonlinear axisymmetric dynamic buckling of functionally graded graphene reinforced porous nanocomposite spherical caps. Mech. Adv. Mater. Struct. (2018). https://doi.org/10.1080/15376494.2018.1549296
18. Gurtin, M.E., Murdoch, A.I.: A continuum theory of elastic material surfaces. Arch. Ration. Mech. Anal. **57**, 291–323 (1975)
19. Zhu, Y.C., Wei, Y.H., Guo, X.: Gurtin-Murdoch surface elasticity theory revisit: an orbital-free density functional theory perspective. J. Mech. Phys. Solids **109**, 178–197 (2017)
20. Kachanov, M., Tsukrov, I., Shafiro, B.: Effective moduli of solids with cavities of various shapes. Appl. Mech. Rev. **47**, S151–S174 (1994)
21. Castañeda, P.P., Willis, J.R.: The effect of spatial distribution on the effective behavior of composite materials and cracked media. J. Mech. Phys. Solids **43**, 1919–1951 (1995)
22. Orlowsky, B., Saenger, E.H., Gueguen, Y., et al.: Effects of parallel crack distributions on effective elastic properties—a numerical study. Int. J. Fract. **124**, L171–L178 (2003)
23. Kushch, V.I., Sevostianov, I., Mishnaevsky, L.: Effect of crack orientation statistics on effective stiffness of mircocracked solid. Int. J. Solids Struct. **46**, 1574–1588 (2009)
24. Wang, X., Zhou, K.: A crack with surface effects in a piezoelectric material. Math. Mech. Solids **22**, 3–19 (2017)
25. Sukumar, N., Chopp, D.L., Moes, N., et al.: Modeling holes and inclusions by level sets in the extended finite-element method. Comput. Methods Appl. Mech. Eng. **190**, 6183–6200 (2001)
26. Tran, A.B., Yvonnet, J., He, Q.C., et al.: A multiple level set approach to prevent numerical artefacts in complex microstructures with nearby inclusions within XFEM. Int. J. Numer. Methods Eng. **85**, 1436–1459 (2011)
27. Moes, N., Cloirec, M., Cartraud, P., et al.: A computational approach to handle complex microstructure geometries. Comput. Methods Appl. Mech. Eng. **192**, 3163–3177 (2003)
28. Yvonnet, J., He, Q.C., Toulemonde, C.: Numerical modeling of the effective conductivities of composites with arbitrarily shaped inclusions and highly conducting interface. Compos. Sci. Technol. **68**, 2818–2825 (2008)
29. Liu, Z.L., Oswald, J., Belytschko, T.: XFEM modeling of ultrasonic wave propagation in polymer matrix particulate/fibrous composites. Wave Motion **50**, 389–401 (2013)
30. Zhang, Y.C., Shang, S.P., Liu, S.T.: A novel implementation algorithm of asymptotic homogenization for predicting the effective coefficient of thermal expansion of periodic composite materials. Acta Mech. Sin. **33**, 368–381 (2017)
31. Zhuang, X.Y., Wang, Q., Zhu, H.H.: Effective properties of composites with periodic random packing of ellipsoids. Materials **10**, 112 (2017)

![](./images/812782145717141505_26.jpg)