Mathematics and Mechanics of Solids
http://mms.sagepub.com/

Non-Local Models of Stress Field Concentrations and Effective Thermoelastic Properties of Random
Structure Composites
V. A. Buryachenko and N. J. Pagano
Mathematics and Mechanics of Solids 2003 8: 403
DOI: 10.1177/10812865030084004

The online version of this article can be found at:
http://mms.sagepub.com/content/8/4/403

Published by:
![](./images/812388747818565633_1.jpg)
http://www.sagepublications.com

Additional services and information for Mathematics and Mechanics of Solids can be found at:

Email Alerts: http://mms.sagepub.com/cgi/alerts

Subscriptions: http://mms.sagepub.com/subscriptions

Reprints: http://www.sagepub.com/journalsReprints.nav

Permissions: http://www.sagepub.com/journalsPermissions.nav

Citations: http://mms.sagepub.com/content/8/4/403.refs.html

>> Version of Record - Aug 1, 2003

What is This?

# Non-local Models of Stress Field Concentrations and Effective Thermoelastic Properties of Random Structure Composites

V. A. BURYACHENKO
University of Dayton Research Institute, Dayton, OH 45469-0168, USA

N. J. PAGANO
Air Force Research Laboratory, Materials and Manufacturing Directorate, AFRL/MLBC,
Wright-Patterson AFB, OH 45433-7750, USA

(Received 6 March 2002; accepted 10 July 2002)

**Abstract:** We consider a linearly thermoelastic composite medium, which consists of a homogeneous matrix containing a statistically homogeneous set of ellipsoidal inclusions and subjected to inhomogeneous boundary conditions. We use the multiparticle effective field method (MEFM) based on the theory of functions of random variables and Green's functions; for references, see Buryachenko, V.A. *Applied Mechanics Reviews*, 54, 1-47 (2001). Within this method, we derive a hierarchy of statistical moment equations for conditional averages of the stresses in the inclusions. The hierarchy is established by introducing the notion of an effective field. In this way the interaction of different inclusions is taken directly into account in the framework of the homogeneity hypothesis of the effective field. The non-local integral equation for the statistical average of stresses inside the inclusions is solved by three different methods: the quadrature method, the iteration method, and the Fourier transform method with subsequent comparative analysis. The standard scheme of iteration and Fourier transform methods permit us to obtain the explicit representations for the non-local integral and differential operators, respectively, of any order describing overall effective properties as well as the stress concentration factor in the components. It is shown that the integral operator reduces to the differential one for sufficiently smooth statistical average stress fields. With some additional assumptions, the proposed method is reduced to the perturbation method as well as to the "quasi-crystalline" approach. For some concrete numerical examples we can demonstrate the advantage of the quadrature method and the iteration method over the Fourier transform method.

**Key Words:** Microstructures, inhomogeneous material, elastic material

## 1. INTRODUCTION

The prediction of the behavior of composite materials by the use of mechanical properties of constituents and their microstructure is a central problem of micromechanics which is eventually reduced to the estimation of stress fields in constituents. A considerable number of methods are known in the linear theory of statistically homogeneous composites being considered in this paper which yield the effective elastic constants and stress field averages in the components. Appropriate, but by no means exhaustive, references are provided by the reviews [1-8]. When the statistical average stress in a composite medium varies sufficiently slowly compared to the size scale of the microstructure (i.e. roughly speaking, the separation of the external and internal scales takes place), the material macroscopically behaves as a

Mathematics and Mechanics of Solids **8:** 403-433, 2003
© 2003 Sage Publications
DOI: 10.1177/108128603031170

homogeneous body with some effective moduli which can be estimated by different methods referred to above. If the condition of the separation of scales summarized above is not valid, the material's response cannot be adequately described in the framework of the local theory of elasticity for the homogeneous medium.

For the analysis of the widely separated scales (but not "too widely"), a number of *phe- nomenological* approaches have been proposed to enhance the continuum model by non-local terms, either introduced through an integral equation, or through an additional gradient equa- tion including one or several intrinsic length scales and based on the assumption that the forces between material points can be long range in character; see, for example, [8-12] and references therein. The integral formulation may be reduced to a gradient form by truncat- ing the series expansion of the non-local kernel. Although an approximation, the gradient representation usually leads to problems that are more tractable than those obtained within the integral formulation. The different modifications of these phenomenological constitutive relations were used for the analyzes of various size effects such as strain gradient harden- ing, size effect in torsion and indentation, strain gradient plasticity, and non-local damage mechanics.

The micromechanical models are used to answer a fundamental question of how length scales in the effective constitutive equations could be directly derived from the geometrical and mechanical properties of constituent phases. The mechanics of generalized continua has become actively developed from the pioneer works by Kröner [15, 16], Kunin and Vaisman [17], and Eringen and Edelen [18] establishing non-local elastic theories based on the idea that cohesive forces have a long range, and are in fact non-local. Kröner [16] showed that the eventual abandonment of the hypothesis of statistically homogeneous fields leads to a *non- local* coupling between statistical averages of the stress and strain tensors when the statistical average stress is given by an integral of the field quantity weighted by some tensorial kernel,i.e. the non-local effective elastic operator $\mathcal{L}^{*}$:

$$
\langle\boldsymbol{\sigma}\rangle(\mathbf{x})=\int \mathcal{L}^{*}(\mathbf{x}, \mathbf{y})\langle\boldsymbol{\varepsilon}\rangle(\mathbf{y}) \mathrm{d} \mathbf{y}. \tag{1.1}
$$

In the consideration of dispersed media this approach makes intuitive sense since the stress at any point will depend on the arrangement of the surrounding inclusions. If the field $\langle\boldsymbol{\varepsilon}\rangle(\mathbf{y})$ varies sufficiently slowly in the neighborhood of an arbitrary point $\mathbf{y}$, then it can be ex- panded about $\mathbf{x}$ in a Taylor series and, therefore, the integral operator of non-local effective elastic properties can be considered as a differential one. Beran and McCoy [19] and Levin[20] have considered a weakly inhomogeneous media when the perturbation method of solu- tion of integral equations involved with Green's functions kernels is appropriate; they found non-local dependence of statistical averages of the stresses and strains in the form of either integral or differential operators. Analysis of highly contrasted statistically homogeneous media is simplified for sufficiently smooth external loading permitting the use of the Taylor expansion for the statistical average of a stress field and the application of a Fourier trans- form method. In so doing, the initial integral equation is reduced to an algebraic polynomial equation with constant coefficients in a Fourier space with forthcoming solution and the im- plementation of the inverse Fourier transform. The scheme summarized informally above is usually based on the hypothesis of the homogeneity of the effective field in which each parti- cle is located. The "quasi-crystalline" approximation by Lax [21] is often used for truncation of the hierarchy of integral equations involved leading to neglect of direct multiparticle inter-

actions of inclusions. This reduced the analysis to the use of statistical information of up to two-point correlation functions and allowed us to derive explicit relations for the non-local overall differential operator by the different methods: by the effective field method [5], or by the method of conditional moments [22]. An advantage of the rigorous approach by Drugan and Willis [23] and Drugan [24] is that it is based on the variational principles, providing the bounds of approximations; they obtained an elegant explicit representation of the non-local effective differential operators of the second and fourth order and systematically estimated long-range action of the non-local effect and the necessary sizes of representative volume elements providing a priori prescribed accuracy of the evaluation of non-local effects. The similar Hashin–Shtrikman formalism was explored by Luciano and Willis [25, 26] (see also [27]) for the analysis of non-local effects produced by random fluctuations in the applied body force. Besides the usual (non-local) effective modulus operator, they estimated another operator that provides a contribution to the mean stress field with itself.

The main disadvantage of the “quasi-crystalline” approximation consisting in the neglect of direct multiparticle interactions of inclusions was overcome recently by the multiparticle effective field method (MEFM); references may be found in [6]. The MEFM is based on the theory of functions of random variables and Green’s functions. Within this method, a hierar- chy of statistical moment equations for conditional averages of the stresses in the inclusions is derived. The hierarchy is established by introducing the notion of an effective field. In this way, the interaction of different inclusions is taken directly into account in the framework of the homogeneity hypothesis of the effective field. Combining the MEFM with the standard scheme of the Fourier transform method usually used for the analysis of the statistically in- homogeneous stress fields allowed Buryachenko and co-workers [28, 29, 30] to obtain the explicit representation of a non-local overall operator in the form of the second-order dif- ferential operator. Buryachenko [31] estimated the non-local integral operator of the overall constitutive equation for periodic structure composites by the use of the first iteration of the iteration method, and showed the reduction of the integral operator obtained to the differential operator involved derived by the Fourier transform method.

A more accurate analysis of the periodic structures is based on the well-developed method of asymptotic expansions (see, for example, [32, 33]) by construction of a “two-scale” as- ymptotic expansion of the solution with respect to the small parameter $\varepsilon$ which is the ratio of the scale of the internal “micro” (the size of the unit cell) and external “macro” (the size of the body) scales. Substitution of the expansion of the displacement in the asymptotic se- ries over $\varepsilon$ into the original system of equations and boundary conditions leads to so-called problems on a cell. Taking into account higher-order terms $\varepsilon$, we can see that the stresses in the effective medium depend on higher-order derivatives of displacements with respect to the coordinates considered, in particular, in couple stress elasticity (see, for example, [34, 35, 36]). The variational-asymptotic approach proposed in [37] may provide a better approxima- tion to the real solution than the “purely” asymptotic approach in the sequential powers of the small parameter $\varepsilon$. The reason for this is that the variational construction is intrinsically such that it tends to minimize the error in a certain variational sense for the final values $\varepsilon$, while the asymptotic approach simply constructs the perturbations assuming that $\varepsilon$ is very small. The effective material parameters were determined from the response of a unit cell under either displacement, displacement–periodic, or traction boundary conditions in [38]. It was found that the three boundary conditions result in hierarchies of both couple-stress moduli and characteristic length. Pagano and Yuan [39] proposed a combination of the effec-

tive medium and micromechanical theories leading to reasonably accurate interface stresses. Vanin [40] obtained an analytical representation for couple stress effective elastic properties of doubly periodic fiber reinforced medium; in the framework of moment elasticity for the effective medium he estimated the stress concentration around a circular hole in a composite plate.

The approach [31] is generalized in this paper for the analysis of statistically homogeneous random structure composites. Using the iteration and Fourier transform methods, we obtain the explicit representations for the non-local integral and differential operators, respectively, of any order describing overall effective properties as well as the stress concentration factor in the components. We show the reduction of the integral operator to the differential one for sufficiently smooth statistical average stress fields. With some additional assumptions the proposed method is reduced to the perturbation method as well as to the "quasi-crystalline" approach. With concrete numerical examples we demonstrate the advantage of the iteration method over the Fourier transform method.

## 2. PRELIMINARIES

### 2.1. Basic equations

Let a linear elastic body occupy an open bounded domain $w \subset R^{d}$ with a smooth boundary $\Gamma$ and with a characteristic function $W$ and space dimensionality $d$ ($d=2$ and $d=3$ for two-dimensional (2D) and three-dimensional (3D) problems, respectively). The domain $w$ contains a homogeneous matrix $v^{(0)}$ and a statistically homogeneous set $X=(v_{i})$ of inclusions $v_{i}$ with characteristic functions $V_{i}$ and bounded by the closed smooth surfaces $\Gamma_{i}$ ($i=1,2,...$). It is assumed that the inclusions can be grouped into components (phases) $v^{(k)}$ ($k=1,2,...,N$) with identical mechanical and geometrical properties (such as the shape, size, orientation, and microstructure of inclusions). For the sake of definiteness, in the 2D case we consider a plane-strain problem. At first, no restrictions are imposed on the elastic symmetry of the phases or on the geometry of the inclusions. $^{1}$ The local strain tensor $\varepsilon$ is related to the displacements $\mathbf{u}$ via the linearized strain-displacement equation $\varepsilon=\frac{1}{2}[\nabla \otimes \mathbf{u}+(\nabla \otimes \mathbf{u})^{\top}]$. Here $\otimes$ denotes tensor product, and $(.)^{\top}$ denotes matrix transposition. The stress tensor, $\sigma$, satisfies the equilibrium equation: $\nabla \cdot \sigma=\mathbf{0}$. Stresses and strains are related to each other via the constitutive equations $\boldsymbol{\sigma}(\mathbf{x})=\mathbf{L}(\mathbf{x}) \boldsymbol{\varepsilon}(\mathbf{x})+\boldsymbol{\alpha}(\mathbf{x})$ or $\boldsymbol{\varepsilon}(\mathbf{x})=\mathbf{M}(\mathbf{x}) \boldsymbol{\sigma}(\mathbf{x})+\boldsymbol{\beta}(\mathbf{x})$, where $\mathbf{L}(\mathbf{x})$ and $\mathbf{M}(\mathbf{x}) \equiv \mathbf{L}(\mathbf{x})^{-1}$ are the known phase stiffness and compliance fourth-order tensors, and the common notation for contracted products has been employed: $\mathbf{L} \boldsymbol{\varepsilon}=L_{i j k l} \varepsilon_{k l}$. $\boldsymbol{\beta}(\mathbf{x})$ and $\boldsymbol{\alpha}(\mathbf{x}) \equiv-\mathbf{L}(\mathbf{x}) \boldsymbol{\beta}(\mathbf{x})$ are second-order tensors of local eigenstrains and eigenstresses. In particular, for isotropic constituents the local stiffness tensor $\mathbf{L}(\mathbf{x})$ is given in terms of the local bulk modulus $k(\mathbf{x})$ and the local shear modulus $\mu(\mathbf{x})$, and the local eigenstrain $\boldsymbol{\beta}(\mathbf{x})$ is given in terms of the bulk component $\beta_{0}(\mathbf{x})$ by the relations:

$$
\begin{aligned}
\mathbf{L}(\mathbf{x}) &=(d k, 2 \mu) \equiv d[k(\mathbf{x})+(1-d / 3) \mu(\mathbf{x})] \mathbf{N}^{1}+2 \mu(\mathbf{x}) \mathbf{N}^{2}, \\
\boldsymbol{\beta}(\mathbf{x}) &=\beta_{0}(\mathbf{x}) \boldsymbol{\delta},
\end{aligned}\tag{2.1}
$$

$\mathbf{N}_{1}=\boldsymbol{\delta} \otimes \boldsymbol{\delta} / d$, $\mathbf{N}_{2}=\mathbf{I}-\mathbf{N}_{1}$ ($d=2$ or $3$); $\boldsymbol{\delta}$ and $\mathbf{I}$ are the unit second-order and fourth-order tensors, and $\otimes$ denotes tensor product. All tensors $\mathbf{f}$ ($\mathbf{f}=\mathbf{L}, \mathbf{M}, \boldsymbol{\alpha}, \boldsymbol{\beta}$) of material properties are decomposed as $\mathbf{f} \equiv \mathbf{f}^{(0)}+\mathbf{f}_{1}(\mathbf{x})=\mathbf{f}^{(0)}+\mathbf{f}_{1}^{(m)}(\mathbf{x})$. Here and in the following, the upper index $^{(m)}$ indicates the components and the lower index $i$ indicates the individual inclusions; $v^{(0)}=w \backslash v$, $v \equiv \cup v^{(k)} \equiv \cup v_{i}$, $V(\mathbf{x})=\sum V^{(k)}=\sum V_{i}(\mathbf{x})$, and $V^{(k)}(\mathbf{x})$ is a characteristic function of $v^{(k)}$ which equals 1 at $\mathbf{x} \in v^{(k)}$ and 0 otherwise, ($m=0,k;$ $k=1,2,\ldots,N;$ $i=1,2,\ldots$).

We assume that the phases are perfectly bonded, so that the displacements and the traction components are continuous across the interphase boundaries, i.e. $[[\boldsymbol{\sigma} \mathbf{n}^{int}]]=\mathbf{0}$ and $[[\mathbf{u}]]=\mathbf{0}$ on the interface boundary $\Gamma^{int}$ where $\mathbf{n}^{int}$ is the normal vector on $\Gamma^{int}$ and $[[(.)]]$ is a jump operator. The traction $\mathbf{t}(\mathbf{x})=\boldsymbol{\sigma}(\mathbf{x}) \mathbf{n}(\mathbf{x})$ acting on any plane with the normal $\mathbf{n}(\mathbf{x})$ through the point $\mathbf{x}$ can be represented in terms of displacements $\mathbf{t}(\mathbf{x})=\hat{\mathbf{t}}(\mathbf{n}, \nabla) \mathbf{u}(\mathbf{x})+\boldsymbol{\alpha}(\mathbf{x}) \mathbf{n}$, where $\hat{t}_{i k}(\mathbf{n}, \nabla)=L_{i j k l} n_{j}(\mathbf{x}) \partial / \partial x_{l}$. The boundary conditions at the interface boundary will be considered together with the mixed boundary conditions on $\Gamma$ with the unit outward normal $\mathbf{n}^{\Gamma}$

$$
\mathbf{u}(\mathbf{x})=\mathbf{u}^{\Gamma}(\mathbf{x}), \quad \mathbf{x} \in \Gamma_{u}, \tag{2.2}
$$

$$
\boldsymbol{\sigma}(\mathbf{x}) \mathbf{n}(\mathbf{x})=\mathbf{t}^{\Gamma}(\mathbf{x}), \quad \mathbf{x} \in \Gamma_{t}, \tag{2.3}
$$

where $\Gamma_{u}$ and $\Gamma_{t}$ are prescribed displacement and traction boundaries such that $\Gamma_{u} \cup \Gamma_{t}=\Gamma$, $\Gamma_{u} \cap \Gamma_{t}=\emptyset$. $\mathbf{u}^{\Gamma}(\mathbf{x})$ and $\mathbf{t}^{\Gamma}(\mathbf{x})$ are, respectively, prescribed displacement on $\Gamma_{u}$ and traction on $\Gamma_{t}$; mixed boundary conditions, such as in the case of elastic supports, are possible. Of special practical interest are the homogeneous boundary conditions

$$
\mathbf{u}^{\Gamma}=\boldsymbol{\varepsilon}^{\Gamma} \mathbf{x}, \boldsymbol{\varepsilon}^{\Gamma}(\mathbf{x}) \equiv \text { const., } \mathbf{x} \in \Gamma, \tag{2.4}
$$

$$
\boldsymbol{\sigma}(\mathbf{x}) \equiv \boldsymbol{\sigma}^{\Gamma}(\mathbf{x})=\text { const., } \mathbf{x} \in \Gamma, \tag{2.5}
$$

where $\boldsymbol{\varepsilon}^{\Gamma}(\mathbf{x})=\frac{1}{2}\left[\nabla \otimes \mathbf{u}^{\Gamma}(\mathbf{x})+\left(\nabla \otimes \mathbf{u}^{\Gamma}(\mathbf{x})\right)^{\top}\right]$, $\mathbf{x} \in \Gamma_{u}$. We will consider the interior problem when the body occupies the interior domain with respect to $\Gamma$.

### 2.2. Statistical description of the composite microstructure

It is assumed that the representative mesodomain $w$ contains a statistically large number of inclusions $v_{i} \subset v^{(k)}$ ($i=1,2,\ldots;$ $k=1,2,\ldots,N$) described by the statistically homogeneous random field. For the description of the random structure of a composite material let us introduce a conditional probability density $\varphi(v_{i}, \mathbf{x}_{i} | v_{1}, \mathbf{x}_{1}, \ldots, v_{n}, \mathbf{x}_{n})$, which is a probability density to find the $i$th inclusion with the center $\mathbf{x}_{i}$ in the domain $v_{i}$ with fixed inclusions $v_{1}, \ldots, v_{n}$ with the centers $\mathbf{x}_{1}, \ldots, \mathbf{x}_{n}$. The notation $\varphi(v_{i}, \mathbf{x}_{i} ; v_{1}, \mathbf{x}_{1}, \ldots, v_{n}, \mathbf{x}_{n})$ denotes the case $\mathbf{x}_{i} \neq \mathbf{x}_{1}, \ldots, \mathbf{x}_{n}$. Of course, $\varphi(v_{i}, \mathbf{x}_{i} | v_{1}, \mathbf{x}_{1}, \ldots, v_{n}, \mathbf{x}_{n})=0$ for values of $\mathbf{x}_{i}$ lying inside the "included volumes" $\cup v_{i m}^{0}$ ($m=1,\ldots,n$), where $v_{i m}^{0} \supset v_{m}$ with characteristic functions $V_{0 m}$ (since inclusions cannot overlap), and $\varphi(v_{i}, \mathbf{x}_{i} | v_{1}, \mathbf{x}_{1}, \ldots, v_{n}, \mathbf{x}_{n}) \to \varphi(v_{i}, \mathbf{x}_{i})$ at $|\mathbf{x}_{i}-\mathbf{x}_{m}| \to \infty$, $m=1,\ldots,n$ (since no long-range order is assumed). Only if the pair distribution function $g(\mathbf{x}_{i}-\mathbf{x}_{m}) \equiv \varphi(v_{i}, \mathbf{x}_{i} | v_{m}, \mathbf{x}_{m}) / n^{(k)}$ depends on $|\mathbf{x}_{m}-\mathbf{x}_{i}|$ is it called the radial distribution function. $\varphi(v_{i})$ is a number density $n^{(k)}$ of component $v^{(k)} \ni v_{i}$ and $c^{(k)}$ is the concentration, i.e. volume fraction, of the component $v^{(k)}$:

$c^{(k)}=\left\langle V^{(k)}(\mathbf{x})\right\rangle=\bar{v}_{i} n^{(k)}(k=1,2, \ldots, N ; i=1,2, \ldots), c^{(0)}=1-\langle V\rangle$. Hereinafter, we will use the notations $\langle(.))(\mathbf{x})$ and $\left\langle(. ) | v_{1}, \mathbf{x}_{1} ; \ldots ; v_{n}, \mathbf{x}_{n}\right\rangle(\mathbf{x})$ for the average and for the conditional average taken for the ensemble of a statistically homogeneous field $X=\left(v_{i}\right)$ at the point $\mathbf{x}$, on the condition that there are inclusions at the points $\mathbf{x}_{1}, \ldots, \mathbf{x}_{n}$ and $\mathbf{x}_{1} \neq \ldots \neq \mathbf{x}_{n}$. Similarly, $V\left(\mathbf{x} | v_{1}, \mathbf{x}_{1} ; \ldots ; v_{n}, \mathbf{x}_{n}\right)$ is a random characteristic function of inclusions $\mathbf{x} \in v$ under the condition that $v_{1} \neq \ldots \neq v_{n}$. The notations $\left\langle(. ) | ; v_{1}, \mathbf{x}_{1} ; \ldots ; v_{n}, \mathbf{x}_{n}\right\rangle(\mathbf{x})$ and $V\left(\mathbf{x} | ; v_{1}, \mathbf{x}_{1} ; \ldots ; v_{n}, \mathbf{x}_{n}\right)$ are used for the case $\mathbf{x} \notin v_{1}, \ldots, v_{n}$. The notation for the conditional probability density $\varphi\left(v_{i}, \mathbf{x}_{i} | ; v_{1}, \mathbf{x}_{1}, \ldots, v_{n}, \mathbf{x}_{n} ; \mathbf{x}_{0}\right)$ is considered under the condition that the inclusions $v_{1}, \ldots, v_{n}$ are located at the points $\mathbf{x}_{1}, \ldots, \mathbf{x}_{n}$, whereas the matrix position is denoted by $\mathbf{x}_{0}$.

### 2.3. Effective fields and statistical averages

A general integral equation describing the stress field in random structure composites is known (for references, see for example [6])

$$
\boldsymbol{\sigma}(\mathbf{x})=\langle\boldsymbol{\sigma}\rangle(\mathbf{x})+\int \boldsymbol{\Gamma}(\mathbf{x}-\mathbf{y})\{\boldsymbol{\eta}(\mathbf{y})-\langle\boldsymbol{\eta}\rangle(\mathbf{y})\} \mathrm{d} \mathbf{y}. \tag{2.6}
$$

where we define the tensor $\boldsymbol{\eta}(\mathbf{y})=\mathbf{M}_{1}(\mathbf{y}) \boldsymbol{\sigma}(\mathbf{y})+\boldsymbol{\beta}_{1}(\mathbf{y})$ called the strain polarization tensor which is simply a notational convenience. The integral operator kernel,

$$
\boldsymbol{\Gamma}(\mathbf{x}-\mathbf{y}) \equiv-\mathbf{L}^{(0)}\left[\mathbf{I} \delta(\mathbf{x}-\mathbf{y})+\mathbf{U}(\mathbf{x}-\mathbf{y}) \mathbf{L}^{(0)}\right], \tag{2.7}
$$

called the Green stress tensor (see [42]) is defined by the second derivative $\mathbf{U}$ of the infinitehomogeneous-body Green's function $\mathbf{G}$ of the Navier equation with an elastic modulus tensor $\mathbf{L}^{(0)}$

$$
\nabla\left\{\mathbf{L}^{(0)} \frac{1}{2}\left[\nabla \otimes \mathbf{G}(\mathbf{x})+(\nabla \otimes \mathbf{G}(\mathbf{x}))^{\top}\right]\right\}=-\boldsymbol{\delta} \delta(\mathbf{x}), \tag{2.8}
$$

vanishing at infinity $(|\mathbf{x}| \rightarrow \infty), \delta(\mathbf{x})$ is the Dirac delta function.

Let the inclusions $v_{1}, \ldots, v_{n}$ be fixed and we define two sorts of effective fields $\overline{\boldsymbol{\sigma}}_{i}(\mathbf{x})$ and $\widetilde{\boldsymbol{\sigma}}_{1, \ldots, n}(\mathbf{x})\left(i=1, \ldots, n ; \mathbf{x} \in v_{1}, \ldots, v_{n}\right)$ by the use of the rearrangement of Equation (2.6) in the following form (see $[5,6]$ for the earliest references of related manipulations)

$$
\boldsymbol{\sigma}(\mathbf{x})=\overline{\boldsymbol{\sigma}}_{i}(\mathbf{x})+\int \boldsymbol{\Gamma}(\mathbf{x}-\mathbf{y}) V_{i}(\mathbf{y}) \boldsymbol{\eta}(\mathbf{y}) \mathrm{d} \mathbf{y}, \tag{2.9}
$$

$$
\overline{\boldsymbol{\sigma}}_{i}(\mathbf{x})=\widetilde{\boldsymbol{\sigma}}_{1, \ldots, n}(\mathbf{x})+\sum_{j \neq i} \int \boldsymbol{\Gamma}(\mathbf{x}-\mathbf{y}) V_{j}(\mathbf{y}) \boldsymbol{\eta}(\mathbf{y}) \mathrm{d} \mathbf{y}, \tag{2.10}
$$

$$
\begin{aligned}
\widetilde{\boldsymbol{\sigma}}_{1, \ldots, n}(\mathbf{x})= & \langle\boldsymbol{\sigma}\rangle(\mathbf{x}) \\
& +\int \boldsymbol{\Gamma}(\mathbf{x}-\mathbf{y})\left\{\boldsymbol{\eta}(\mathbf{y}) V\left(\mathbf{y} | ; v_{1}, \mathbf{x}_{1} ; \ldots ; v_{n}, \mathbf{x}_{n}\right)-\langle\boldsymbol{\eta}\rangle(\mathbf{y})\right\} \mathrm{d} \mathbf{y}, \tag{2.11}
\end{aligned}
$$

for $\mathbf{x} \in v_{i}, i=1,2, \ldots, n$. Then, considering some conditional statistical averages of the
general integral equation (2.6) leads to an infinite system of integral equations $(n=1,2, \ldots)$

$$
\begin{aligned}
& \left\langle\boldsymbol{\sigma} \mid v_{1}, \mathbf{x}_{1} ; \ldots ; v_{n}, \mathbf{x}_{n}\right\rangle(\mathbf{x})-\sum_{i=1}^{n} \int \boldsymbol{\Gamma}(\mathbf{x}-\mathbf{y})\left\langle V_{i}(\mathbf{y}) \boldsymbol{\eta} \mid v_{1}, \mathbf{x}_{1} ; \ldots ; v_{n}, \mathbf{x}_{n}\right\rangle(\mathbf{y}) \mathrm{d} \mathbf{y} \\
= & \langle\boldsymbol{\sigma}\rangle(\mathbf{x})+\int \boldsymbol{\Gamma}(\mathbf{x}-\mathbf{y})\left\{\left\langle\boldsymbol{\eta} \mid v_{1}, \mathbf{x}_{1} ; \ldots ; v_{n}, \mathbf{x}_{n}\right\rangle(\mathbf{y})-\langle\boldsymbol{\eta}\rangle(\mathbf{y})\right\} \mathrm{d} \mathbf{y},
\end{aligned}
$$

where $\mathbf{x} \in v_{1}, \ldots, v_{n}$ in the $n$th line of the system.

The definitions of the effective fields $\overline{\boldsymbol{\sigma}}_{i}(\mathbf{x}), \tilde{\boldsymbol{\sigma}}_{1,2, \ldots, n}(\mathbf{x})$ as well as their statistical aver-
ages $\left\langle\overline{\boldsymbol{\sigma}}_{i}\right\rangle(\mathbf{x}),\left\langle\tilde{\boldsymbol{\sigma}}_{1,2, \ldots, n}\right\rangle(\mathbf{x})$ are nothing more than notation convenience for different terms
of the infinite systems (2.9)-(2.11). The physical meaning of these fields is the following.
$\tilde{\boldsymbol{\sigma}}_{1,2, \ldots, n}(\mathbf{x})$ is a stress field in which the chosen fixed inclusions $v_{1}, \ldots, v_{n}$ are embedded.
This effective field is a random function of all the other positions of the surrounding inho-
mogeneities, and the average $\left\langle\tilde{\boldsymbol{\sigma}}_{1, \ldots, n}\right\rangle(\mathbf{x})$ of $\tilde{\boldsymbol{\sigma}}_{1, \ldots, n}(\mathbf{x})$ over a random realization of these
inclusions is equal to the right-hand side of the $n$th line of the system (2.12). Consequently,
each inclusion $v_{i}(i=1, \ldots, n)$ of the chosen fixed set is in a random (generally speaking
non-homogeneous) field $\overline{\boldsymbol{\sigma}}_{i}(\mathbf{x}),\left(\mathbf{x} \in v_{i}, i \neq j, i, j=1,2, \ldots, n\right)(2.10)$ which is the super-
position of the effective field $\tilde{\boldsymbol{\sigma}}_{1, \ldots, n}(\mathbf{x})$ and the distribution caused by the other inclusions
$v_{j},(j \neq i, j=1, \ldots, n)$ of the considered set.

## 3. APPROXIMATE AND CLOSURE EFFECTIVE FIELD HYPOTHESES

In order to simplify the exact system (2.12) we now apply the main hypothesis of many mi-
cromechanical methods, the approximation called the effective field hypothesis:

**(H1)** Each inclusion $v_{i}$ has an ellipsoidal form and is located in the field (2.10)

$$
\overline{\boldsymbol{\sigma}}_{i}(\mathbf{y}) \equiv \overline{\boldsymbol{\sigma}}\left(\mathbf{x}_{i}\right) \quad\left(\mathbf{y} \in v_{i}\right)
$$

which is homogeneous over the inclusion $v_{i}$, and the perturbation introduced by the inclusion $v_{i}$
at the point $\mathbf{y} \notin v_{i}$ is defined by the relation

$$
\int \boldsymbol{\Gamma}(\mathbf{y}-\mathbf{x}) V_{i}(\mathbf{x}) \boldsymbol{\eta}(\mathbf{x}) \mathrm{d} \mathbf{x}=\bar{v}_{i} \mathbf{T}_{i}\left(\mathbf{y}-\mathbf{x}_{i}\right) \boldsymbol{\eta}_{i}.
$$

Hereafter $\boldsymbol{\eta}_{i} \equiv\left\langle\boldsymbol{\eta}(\mathbf{x}) V_{i}(\mathbf{x})\right\rangle_{(i)}$ is an average over the volume of the inclusion $v_{i}$ (but not
over the ensemble), $\left\langle\langle.\rangle_{i} \equiv\left\langle\langle.\rangle_{(i)}\right\rangle\right.$, and the tensors

$$
\begin{aligned}
\mathbf{T}_{i}\left(\mathbf{y}-\mathbf{x}_{i}\right) & = \begin{cases}-\left(\bar{v}_{i}\right)^{-1} \mathbf{Q}_{i} & \text { for } \mathbf{y} \in v_{i}, \\
\left(\bar{v}_{i}\right)^{-1} \int \boldsymbol{\Gamma}(\mathbf{y}-\mathbf{x}) V_{i}(\mathbf{x}) \mathrm{d} \mathbf{x} & \text { for } \mathbf{y} \notin v_{i},\end{cases} \\
\mathbf{T}_{i j}\left(\mathbf{x}_{i}-\mathbf{x}_{j}\right) & =\left\langle\mathbf{T}_{i}\left(\mathbf{z}-\mathbf{x}_{i}\right)\right\rangle_{j}
\end{aligned}
$$
```

$({\bf z} \in v_j \neq v_i)$ have analytical representations for spherical inclusions in an isotropic matrix (see for reference [6]).

For the termination of the hierarchy of statistical moment equations (2.12) we will use the closure effective field hypothesis:

(H2) For a sufficiently large $n$, we complete the system (2.12) by the assumption $\langle\widetilde{\boldsymbol{\sigma}}_{1,\dots,j,\dots,n+1}(\mathbf{x})\rangle_i = \langle\widetilde{\boldsymbol{\sigma}}_{1,\dots,n}(\mathbf{x})\rangle_i$, where the right-hand side of the equality does not contain the index $j \neq i$ ($i = 1,\dots,n$; $j = 1,\dots,n+1$; $\mathbf{x} \in v_i$).

The fundamental differences of the hypothesis H2 and "quasi-crystalline" approximation by Lax [21]

$$
\langle\overline{\boldsymbol{\sigma}}_i(\mathbf{x})|v_i, \mathbf{x}_i; v_j, \mathbf{x}_j\rangle = \langle\overline{\boldsymbol{\sigma}}_i\rangle,\quad \mathbf{x} \in v_i \tag{3.4}
$$

as well as of the assumptions (3.1) and (3.2) were discussed by [6].

According to hypothesis H1 and in view of the linearity of the problem there exist constant fourth and second-rank tensors $\mathbf{B}^{(i)}(\mathbf{x})$, $\mathbf{R}^{(i)}(\mathbf{x})$ and $\mathbf{C}^{(i)}(\mathbf{x})$, $\mathbf{F}^{(i)}(\mathbf{x})$, such that

$$
\begin{aligned}
\boldsymbol{\sigma}(\mathbf{x}) &= \mathbf{B}^{(i)}(\mathbf{x})\overline{\boldsymbol{\sigma}}(\mathbf{x}_i) + \mathbf{C}^{(i)}(\mathbf{x}), \\
\overline{v}_i \boldsymbol{\eta}(\mathbf{x}) &= \mathbf{R}^{(i)}(\mathbf{x})\overline{\boldsymbol{\sigma}}(\mathbf{x}_i) + \mathbf{F}^{(i)}(\mathbf{x}),
\end{aligned} \tag{3.5}
$$

where $\mathbf{x} \in v_i \subset v^{(i)}$ and $\mathbf{R}^{(i)}(\mathbf{x}) = \overline{v}_i \mathbf{M}_1^{(i)}(\mathbf{x})\mathbf{B}^{(i)}(\mathbf{x})$, $\mathbf{F}^{(i)}(\mathbf{x}) = \overline{v}_i[\mathbf{M}_1^{(i)}(\mathbf{x})\mathbf{C}^{(i)}(\mathbf{x}) + \boldsymbol{\beta}_1(\mathbf{x})]$. According to the theorem of Eshelby [43] there are the following relations between the averaged tensors (3.5) $\mathbf{R}_i = \overline{v}_i \mathbf{Q}_i^{-1}(\mathbf{I} - \mathbf{B}_i)$, $\mathbf{F}_i = -\overline{v}_i \mathbf{Q}_i^{-1} \mathbf{C}_i$, where $\mathbf{f}_i \equiv \langle\mathbf{f}(\mathbf{x})\rangle_{(i)}$ (f denotes $\mathbf{B}, \mathbf{C}, \mathbf{R}, \mathbf{F}$) and the tensor $\mathbf{Q}$ is associated with the well-known Eshelby tensor by $\mathbf{S} = \mathbf{I} - \mathbf{M}^{(0)} \mathbf{Q}$. It should be mentioned that the field $\overline{\boldsymbol{\sigma}}(\mathbf{x}_i)$ can vary with the location of the center $\mathbf{x}_i$ of the inclusion considered, but the field $\overline{\boldsymbol{\sigma}}(\mathbf{y})$ ($\mathbf{y} \in v_i$) is homogeneous over the inclusion $v_i$. Because of this the application of Eshelby's theorem is correct.

For example, for the homogeneous ellipsoidal domain $v_i$ with

$$
\mathbf{M}_1^{(i)}(\mathbf{x}) = \mathbf{M}_1^{(i)} = \text{const},\ \boldsymbol{\beta}_1^{(i)}(\mathbf{x}) = \boldsymbol{\beta}_1^{(i)} = \text{const}\quad \text{at } \mathbf{x} \in v_i, \tag{3.6}
$$

we obtain $\mathbf{B}_i = \left(\mathbf{I} + \mathbf{Q}_i \mathbf{M}_1^{(i)}\right)^{-1}$, $\mathbf{C}_i = -\mathbf{B}_i \mathbf{Q}_i \boldsymbol{\beta}_1^{(i)}$. In the general case of coated inclusions $v_i$, the tensors $\mathbf{B}(\mathbf{x})$ and $\mathbf{C}(\mathbf{x})$ can be found by the transformation method of Dvorak and Benveniste [44] (for details, see [6], where the references of solution of the problem for coated ellipsoidal inclusion can be found).

Using hypothesis H1, the system (2.10) for $k$ fixed inclusions with fixed values $\widetilde{\boldsymbol{\sigma}}_{1,\dots,k}(\mathbf{x})$ ($\mathbf{x} \in v_i$, $i = 1\ldots,k$) on the right-hand side of the equations becomes algebraic when the solution (3.5) for one inclusion in the field $\overline{\boldsymbol{\sigma}}(\mathbf{x}_i)$ ($i = 1,\dots,k$) is applied

$$
\mathbf{R}_i \overline{\boldsymbol{\sigma}}(\mathbf{x}_i) + \mathbf{F}_i = \sum_{j=1}^k \mathbf{Z}_{ij} \left\{ \mathbf{R}_j \widetilde{\boldsymbol{\sigma}}_{1,\dots,k}(\mathbf{x}_j) + \mathbf{F}_j \right\}, \tag{3.7}
$$

where the matrix $\mathbf{Z}^{-1}$ has the elements $(\mathbf{Z}^{-1})_{ij}$

$$
\left(\mathbf{Z}^{-1}\right)_{ij}=\mathbf{I}\delta_{ij}-\left(1-\delta_{ij}\right)\mathbf{R}_{j}\mathbf{T}_{ij}\left(\mathbf{x}_{i}-\mathbf{x}_{j}\right),\quad(i,j=1,\ldots,n).\tag{3.8}
$$

## 4. THE NON-LOCAL INTEGRAL EQUATION

In the framework of the hypothesis $\mathbf{H 1}$, substitution of the solution (3.5), and (3.6) (at $k=2$) for binary interacting inclusions into the first equation of the system (2.12) at $n=1$, and averaging the result obtained over the inclusion $v_{i}$ gives

$$
\begin{aligned}
\bar{v}_{i}\left\langle\boldsymbol{\eta}_{i}\right\rangle\left(\mathbf{x}_{i}\right)=&\bar{v}_{i}\left\langle\boldsymbol{\eta}_{i}^{av}\right\rangle\left(\mathbf{x}_{i}\right) \\
+&\mathbf{R}_{i}\sum_{q=1}^{N}\left\{\int \mathbf{T}_{iq}\left(\mathbf{x}_{i}-\mathbf{x}_{q}\right)\mathbf{Z}_{qi}\varphi\left(v_{q},\mathbf{x}_{q}\mid;v_{i},\mathbf{x}_{i}\right)\mathrm{d}\mathbf{x}_{q}\left[\mathbf{R}_{i}\left\langle\widetilde{\boldsymbol{\sigma}}_{i,q}\left(\mathbf{x}_{i}\right)\right\rangle_{i}+\mathbf{F}_{i}\right]\right. \\
+&\int\left[\mathbf{T}_{iq}\left(\mathbf{x}_{i}-\mathbf{x}_{q}\right)\mathbf{Z}_{qq}\varphi\left(v_{q},\mathbf{x}_{q}\mid;v_{i},\mathbf{x}_{i}\right)\left[\mathbf{R}_{q}\left\langle\widetilde{\boldsymbol{\sigma}}_{i,q}\left(\mathbf{x}_{q}\right)\right\rangle_{q}+\mathbf{F}_{q}\right]\right. \\
&\left.\left.-\mathbf{T}_{i}\left(\mathbf{x}_{i}-\mathbf{x}_{q}\right)n^{(q)}\left(\mathbf{x}_{q}\right)\bar{v}_{q}\left\langle\boldsymbol{\eta}_{q}\right\rangle\left(\mathbf{x}_{q}\right)\right]\mathrm{d}\mathbf{x}_{q}\right\},
\end{aligned}\tag{4.1}
$$

where $N$ is a number of inclusion components, and $\bar{v}_{i}\left\langle\boldsymbol{\eta}_{i}^{av}\right\rangle\left(\mathbf{x}_{i}\right)=\mathbf{R}_{i}\langle\boldsymbol{\sigma}\rangle\left(\mathbf{x}_{i}\right)+\mathbf{F}_{i}$ is called the strain polarization tensor of the average stress $\langle\boldsymbol{\sigma}\rangle\left(\mathbf{x}_{i}\right)$ in the component $v^{(i)}$, and the matrix elements $\mathbf{Z}_{qi}$, $\mathbf{Z}_{qq}$ (no sum on $q$) are non-diagonal and diagonal elements, respectively, of the binary interaction matrix $\mathbf{Z}$ (3.6) for the two inclusions $v_{q}$ and $v_{i}$.

Equation (4.1) can be solved using the effective field hypothesis $\mathbf{H 2}$ with the first-order approximation:

$$
\left\langle\widetilde{\boldsymbol{\sigma}}_{i,q}(\mathbf{x})\right\rangle_{j}=\langle\overline{\boldsymbol{\sigma}}(\mathbf{x})\rangle_{j}=\text{const.}\quad(j=i,q).\tag{4.2}
$$

This independence of $\langle\widetilde{\boldsymbol{\sigma}}_{i,q}(\mathbf{x})\rangle$ on the spacing between the inclusions $v_{i}$ and $v_{q}$ (4.2) occurs for the limiting case $|\mathbf{x}_{i}-\mathbf{x}_{q}|\gg\max a_{j}^{k}$, where $a_{j}^{k}$ $(k=1,2,3;j=i,q)$ are the semi-axes of the ellipsoidal inclusions $v_{i}$ and $v_{q}$, respectively. Then, from Equation (4.1), taking Equation (4.2) into account we obtain

$$
\begin{aligned}
\bar{v}_{i}\left\langle\boldsymbol{\eta}_{i}\right\rangle\left(\mathbf{x}_{i}\right)=&\bar{v}_{i}\left\langle\boldsymbol{\eta}_{i}^{av}\right\rangle\left(\mathbf{x}_{i}\right)+\sum_{q=1}^{N}\left\{\int \boldsymbol{\mathcal{T}}_{iq}\left(\mathbf{x}_{i},\mathbf{x}_{q}\right)\mathrm{d}\mathbf{x}_{q}\bar{v}_{i}\left\langle\boldsymbol{\eta}_{i}\right\rangle\left(\mathbf{x}_{i}\right)\right. \\
+&\left.\int \mathcal{F}_{iq}\left(\mathbf{x}_{i},\mathbf{x}_{q}\right)\bar{v}_{q}\left\langle\boldsymbol{\eta}_{q}\right\rangle\left(\mathbf{x}_{q}\right)\mathrm{d}\mathbf{x}_{q}\right\},
\end{aligned}\tag{4.3}
$$

where

$$
\boldsymbol{\mathcal{T}}_{iq}\left(\mathbf{x}_{i},\mathbf{x}_{q}\right)=\mathbf{R}_{i}\mathbf{T}_{iq}\left(\mathbf{x}_{i}-\mathbf{x}_{q}\right)\mathbf{Z}_{qi}\varphi\left(v_{q},\mathbf{x}_{q}\mid;v_{i},\mathbf{x}_{i}\right),\tag{4.4}
$$

$$
\mathcal{F}_{i q}\left(\mathbf{x}_{i}, \mathbf{x}_{q}\right)=\mathbf{R}_{i}\left[\mathbf{T}_{i q}\left(\mathbf{x}_{i}-\mathbf{x}_{q}\right) \mathbf{Z}_{q q} \varphi\left(v_{q}, \mathbf{x}_{q} \mid ; v_{i}, \mathbf{x}_{i}\right)-\mathbf{T}_{i}\left(\mathbf{x}_{i}-\mathbf{x}_{q}\right) n^{(q)}\left(\mathbf{x}_{q}\right)\right]. \quad(4.5)
$$

For statistically homogeneous media being considered, when the functions $\varphi(v_{i}, \mathbf{x}_{i})$ and $\varphi(v_{q}, \mathbf{x}_{q} | v_{i}, \mathbf{x}_{i})$ are insensitive to translations
$$
\varphi\left(v_{i}, \mathbf{x}_{i}\right)=n^{(i)} \equiv \text { const. },
$$
$$
\varphi\left(v_{q}, \mathbf{x}_{q}+\mathbf{x} | v_{i}, \mathbf{x}_{i}+\mathbf{x}\right) \equiv \varphi\left(v_{q}, \mathbf{x}_{q} | v_{i}, \mathbf{x}_{i}\right)
$$

for any $\mathbf{x}$, the integral kernels (4.4) and (4.5) are the convolution ones:
$$
\mathcal{T}_{i q}\left(\mathbf{x}_{i}, \mathbf{x}_{q}\right)=\mathcal{T}_{i q}\left(\mathbf{x}_{i}-\mathbf{x}_{q}\right),
$$
$$
\mathcal{F}_{i q}\left(\mathbf{x}_{i}, \mathbf{x}_{q}\right)=\mathcal{F}_{i q}\left(\mathbf{x}_{i}-\mathbf{x}_{q}\right).
$$

Transforming the second integral in Equation (4.3) in a spirit of subtraction technique reduces Equation (4.3) to the representation

$$
\begin{aligned}
\bar{v}_{i}\left\langle\boldsymbol{\eta}_{i}\right\rangle\left(\mathbf{x}_{i}\right)= & \sum_{j=1}^{N} \mathbf{Y}_{i j}\left\{\bar{v}_{j}\left\langle\boldsymbol{\eta}_{j}^{a v}\right\rangle\left(\mathbf{x}_{j}\right)\right. \\
& \left.+\sum_{q=1}^{N} \int \mathcal{F}_{j q}\left(\mathbf{x}_{j}-\mathbf{x}_{q}\right) \bar{v}_{q}\left[\left\langle\boldsymbol{\eta}_{q}\right\rangle\left(\mathbf{x}_{q}\right)-\left\langle\boldsymbol{\eta}_{q}\right\rangle\left(\mathbf{x}_{j}\right)\right] \mathrm{d} \mathbf{x}_{q}\right\} \quad(4.8)
\end{aligned}
$$

where the matrix $\mathbf{Y}^{-1}$ has the following elements
$$
\left(\mathbf{Y}^{-1}\right)_{i j}=\delta_{i j}\left[\mathbf{I}-\sum_{q=1}^{N} \int \mathcal{T}_{i q}\left(\mathbf{x}_{i}-\mathbf{x}_{q}\right) \mathrm{d} \mathbf{x}_{q}\right]-\int \mathcal{F}_{i j}\left(\mathbf{x}_{i}-\mathbf{x}_{j}\right) \mathrm{d} \mathbf{x}_{j},
$$

for $i, j=1,2, \ldots, N$. This matrix $\mathbf{Y}$ determines the action of the surrounding inclusions on the isolated one and is defined simply by the solution of the problem for purely mechanical loading (with $\boldsymbol{\beta} \equiv 0$).

Then Equation (4.3) can be rewritten in the compact form
$$
\mathcal{E}=\mathbf{Y} \mathcal{E}^{a v}+\mathcal{K} \mathcal{E}, \quad \mathbf{x} \in v_{i},
$$

where we have used the vectors
$$
\mathcal{E}\left(\mathbf{x}_{i}\right)=\left(\bar{v}_{1} \boldsymbol{\eta}_{1}\left(\mathbf{x}_{i}\right), \ldots, \bar{v}_{N} \boldsymbol{\eta}_{N}\left(\mathbf{x}_{i}\right)\right)^{\top},
$$
$$
\mathcal{E}^{a v}\left(\mathbf{x}_{i}\right)=\left(\bar{v}_{1} \boldsymbol{\eta}_{1}^{a v}\left(\mathbf{x}_{i}\right), \ldots, \bar{v}_{N} \boldsymbol{\eta}_{N}^{a v}\left(\mathbf{x}_{i}\right)\right)^{\top},
$$

and
$$
(\mathcal{K} \mathcal{E})(\mathbf{x})=\int \mathbf{K}(\mathbf{x}-\mathbf{y})[\mathcal{E}(\mathbf{y})-\mathcal{E}(\mathbf{x})] \mathrm{d} \mathbf{y}
$$

defines the integral operator $\mathcal{K}$ with the matrix kernel $\mathbf{K} \equiv \mathbf{Y} \mathcal{F}(\mathbf{x}_j - \mathbf{x}_q)$ with elements formally represented as

$$
\mathbf{K}_{i q}\left(\mathbf{x}_{i}-\mathbf{x}_{q}\right)=\sum_{j=1}^{n} \mathbf{Y}_{i j} \mathcal{F}_{j q}\left(\mathbf{x}_{j}-\mathbf{x}_{q}\right). \tag{4.14}
$$

Thus we reduced the integral equation (4.3) to the standard form of operator equation (4.10) with the regular integral kernel of convolution type that can be solved by such known methods as the method of mechanical quadratures, successive approximations, and Fourier transform methods. We formally write the solution of Equation (4.10) as

$$
\mathcal{E}=\mathcal{L} \mathcal{E}^{a v}, \tag{4.15}
$$

where the inverse operator $\mathcal{L}=(\mathbf{I}-\mathcal{K})^{-1}$ will be constructed by three methods mentioned in the next section.

## 5. THE METHODS OF THE SOLUTION OF EQUATION (4.10)

### 5.1. Direct quadrature method

The application of the method of mechanical quadratures (called also the Nystrom method) is very popular (see, for example, [45, 46]) although it is required to solve linear systems of high order even for a smoothly varying load. In effect, the Nystron method transforms the integral equation problem (4.10) with regular kernel into the linear algebra problem in any case

$$
\mathcal{E}_{k}=\mathbf{Y} \mathcal{E}_{k}^{a v}+\sum_{l} \mathcal{K}_{k l} \mathcal{E}_{l}, \tag{5.1}
$$

where $\mathcal{E}_{k}=\mathcal{E}(\mathbf{x}_{k})$, $\mathcal{E}_{l}=\mathcal{E}(\mathbf{x}_{l})$, $\mathcal{E}_{k}^{a v}=\mathcal{E}^{a v}(\mathbf{x}_{k})$, $\mathcal{K}_{k l}=w_{l} \mathcal{K}(\mathbf{x}_{k}, \mathbf{x}_{l})$, and $w_{l}$ are the weights $(k, l=1,2, \ldots)$ of some known quadrature rule (see, for example, [47]). For a periodic function $\mathcal{E}^{a v}$, the integral (4.10) with the infinite range is in fact reduced to the integral over the unit cell. Since the kernel $\mathcal{K}(\mathbf{x}-\mathbf{y})$ decays at infinity fast enough (as $O(|\mathbf{x}-\mathbf{y}|^{-2 d})$ ), then for $\mathcal{E}^{a v}$ stabilizing at infinity ($\mathcal{E}^{a v}(\mathbf{x}) \rightarrow$ const. as $|\mathbf{x}| \rightarrow \infty$), it is tempting to avoid consideration of the infinite range problem (4.13) by truncating the range at some finite domain, say, the sphere with the radius $R$ and the characteristic function describing by the Heaviside step function $H(R-|\mathbf{x}-\mathbf{y}|)$

$$
\begin{aligned}
\int \mathbf{K}(\mathbf{x}-\mathbf{y})[\mathcal{E}(\mathbf{y})-\mathcal{E}(\mathbf{x})] \mathrm{d} \mathbf{y}=& \lim _{R \rightarrow \infty} \int \mathbf{K}(\mathbf{x}-\mathbf{y})[\mathcal{E}(\mathbf{y}) \\
&-\mathcal{E}(\mathbf{x})] H(R-|\mathbf{x}-\mathbf{y}|) \mathrm{d} \mathbf{y}. \tag{5.2}
\end{aligned}
$$

The effectiveness of this scheme in some concrete numerical examples will be demonstrated in Section 9. Analysis of more general cases of the behavior of the function $\mathcal{E}^{a v}$ based on the use of a rule developed directly for the infinite range (such as Gauss-Languerre and Gauss–

Hermite rules; for details, see, for example, [47]) is performed in a straightforward manner
and will not be considered in more detail in this paper.

### 5.2. The iteration method

Although the direct quadrature method usually causes no problems of accuracy, for a large
number of unknown variables $N$ its $O(N^3)$ cost dependence can lead to surprisingly long
computing time. The obvious way of reducing this cost is to construct an iterative scheme
for Equation (4.10). Because of this, at first we will solve Equation (4.10) by the method of
successive approximations, which is also called the Neumann series method. The connection
with the Fourier transform method will be considered in Section 8.

For simplicity, we will consider the point Jacoby iterative method based on the recursion
formula
$$
\mathcal{E}_{(k+1)}=\mathbf{Y} \mathcal{E}^{a v}+\mathcal{K} \mathcal{E}_{(k)} \tag{5.3}
$$
to construct a sequence of functions $\{\mathcal{E}_{(k)}\}$ that can be treated as an approximation of the
solution of Equation (4.10). We will not analyze other methods, for example the accelerated
Liebmann method (called also extrapolated Gauss-Siedel method) which is usually "faster"
that the point Jacobi method, and has the computational advantage that it does not require
simultaneous storage of the two iterations $\mathcal{E}_{(k+1)}$ and $\mathcal{E}_{(k)}$ (see, for example, [48]).

Usually the driving term of Equation (5.3) is used as an initial approximation:
$$
\mathcal{E}_{(0)}(\mathbf{x})=\mathbf{Y} \mathcal{E}^{a v}(\mathbf{x}),
$$
$$
\bar{v}_{i}\left\langle\boldsymbol{\eta}_{i}\right\rangle\left(\mathbf{x}_{i}\right)=\sum_{j=1}^{N} \mathbf{Y}_{i j} \bar{v}_{j}\left\langle\boldsymbol{\eta}_{j}^{a v}\right\rangle\left(\mathbf{x}_{j}\right) \tag{5.4}
$$
which is exact for homogeneous boundary conditions either (2.4) or (2.5) in the framework
of hypotheses $\boldsymbol{\text{H1}}$ and $\boldsymbol{\text{H2}}$ The matrix $\mathbf{Y}$ determines the "local" action of the surrounding
inclusions on the one $v_i$, while the integral operator kernel $\mathcal{K}$ describes a "non-local" action
of these inclusions. The next two iterations have the form
$$
\mathcal{E}_{(1)}(\mathbf{x})=\mathbf{Y} \mathcal{E}^{a v}(\mathbf{x})+\int \mathbf{K}(\mathbf{x}-\mathbf{y}) \mathbf{Y}\left[\mathcal{E}^{a v}(\mathbf{y})-\mathcal{E}^{a v}(\mathbf{x})\right] \mathrm{d} \mathbf{y}, \tag{5.5}
$$
$$
\begin{aligned}
\mathcal{E}_{(2)}(\mathbf{x})= & \mathbf{Y} \mathcal{E}^{a v}(\mathbf{x})+\int \mathbf{K}(\mathbf{x}-\mathbf{y}) \mathbf{Y}\left[\mathcal{E}^{a v}(\mathbf{y})-\mathcal{E}^{a v}(\mathbf{x})\right] \mathrm{d} \mathbf{y} \\
& +\int \mathbf{K}(\mathbf{x}-\mathbf{y}) \mathbf{Y}\left\{\int \mathbf{K}(\mathbf{y}-\mathbf{z}) \mathbf{Y}\left[\mathcal{E}^{a v}(\mathbf{z})-\mathcal{E}^{a v}(\mathbf{y})\right] \mathrm{d} \mathbf{z}\right. \\
& \left.-\int \mathbf{K}(\mathbf{x}-\mathbf{z}) \mathbf{Y}\left[\mathcal{E}^{a v}(\mathbf{z})-\mathcal{E}^{a v}(\mathbf{x})\right] \mathrm{d} \mathbf{z}\right\} \mathrm{d} \mathbf{y},
\end{aligned} \tag{5.6}
$$
and again proceeding formally, it suggests the Neumann series form for the solution $\mathcal{E}$ of
Equation (4.9)

$$
\mathcal{E}=\mathcal{L} \mathcal{E}^{a v}, \quad \mathcal{L} \equiv \sum_{k=0}^{\infty} \mathcal{K}^{k},
\tag{5.7}
$$

where $\mathcal{L}$ is the inverse integral operator with the kernel $\mathcal{L}(\mathbf{x}, \mathbf{y})$, and the power $\mathcal{K}^{k}$ is defined recursively by the condition $\mathcal{K}^{1}=\mathcal{K}$ and the kernel of $\mathcal{K}^{k}$ is (see, for example, [49])

$$
\mathcal{K}_{k}(\mathbf{x}-\mathbf{y})=\int \mathcal{K}(\mathbf{x}-\mathbf{z}) \mathcal{K}_{k-1}(\mathbf{z}-\mathbf{y}) \mathrm{d} \mathbf{z}.
\tag{5.8}
$$

In effect, the iteration method (5.3) transforms the integral equation problem (4.8) into the linear algebra problem (5.5) and (5.7) in any case. The sequence $\left\{\mathcal{E}_{(k)}\right\}$ (5.3) with arbitrary continuous $\mathcal{E}_{a v}(\mathbf{x})$ converges to a unique solution $\mathcal{E}$ (4.10) for the kernel of $\mathcal{K}$ "small" enough, which is to say that

$$
\|\mathcal{K}\|_{\infty, v_{i}} \equiv \max _{\mathbf{x} \in v_{i}} \int|\mathcal{K}(\mathbf{x}-\mathbf{y})| \mathrm{d} \mathbf{y}<1.
\tag{5.9}
$$

As will be shown, only a few iterations of Equation (5.3) are necessary; these iterations prove very much faster than a direct inversion of the operator $\mathbf{I}-\mathcal{K}$ by the quadrature method. In so doing, the condition (5.9) is fulfilled in all examples considered.

### 5.3. The Fourier transform method

We assume that the statistical average of strain polarization tensor $\left\langle\boldsymbol{\eta}_{q}\right\rangle(\mathbf{x})_{q}$ belongs to the class of $m$-times continuously differential functions $C^{m}(w)$. Since we desire an explicit representation for stress concentration factor, we will approximate $\left\langle\boldsymbol{\eta}_{q}\right\rangle(\mathbf{x})_{q}$ by the first terms of its Taylor expansion

$$
\left\langle\boldsymbol{\eta}_{q}\right\rangle\left(\mathbf{x}_{q}\right) \approx \sum_{|\alpha|=0}^{m} \frac{1}{\alpha !}\left[\otimes\left(\mathbf{x}_{q}-\mathbf{x}_{i}\right)\right]^{\alpha} \nabla^{\alpha}\left\langle\boldsymbol{\eta}_{q}\right\rangle\left(\mathbf{x}_{i}\right),
\tag{5.10}
$$

where for the multi-indices of non-negative integers $\alpha=\left(\alpha_{1}, \ldots, \alpha_{d}\right) \in Z_{+}^{d}$, and $\beta=\left(\beta_{1}, \ldots, \beta_{d}\right) \in Z_{+}^{d}(d=2,3)$ the following notations were used

$$
\begin{aligned}
\alpha+\beta & =\left(\alpha_{1}+\beta_{1}, \ldots, \alpha_{d}+\beta_{d}\right), \nabla^{\alpha}=\frac{\partial^{\alpha_{1}}}{\partial x_{1}^{\alpha_{1}}} \cdots \frac{\partial^{\alpha_{d}}}{\partial x_{d}^{\alpha_{d}}}, \\
\sum_{|\alpha|=0}^{m} & =\sum_{|\alpha|=0}^{m} \sum_{\alpha_{1}+\ldots+\alpha_{d}=|\alpha|}, \\
|\alpha| & \equiv \alpha_{1}+\ldots+\alpha_{d}, \\
(\otimes \mathbf{x})^{\alpha} & =\left(x_{1}\right)^{\alpha_{1}} \ldots\left(x_{d}\right)^{\alpha_{d}}, \\
\alpha! & =\alpha_{1}! \ldots \alpha_{d}!.
\end{aligned}
\tag{5.11}
$$

Taking the expansions (5.10) into account, Equation (4.3) can be rewritten in compact form

$$
\mathcal{P}\left(\mathbf{x}_{i}, \nabla\right) \mathcal{E}\left(\mathbf{x}_{i}\right)=\mathcal{E}^{a v}\left(\mathbf{x}_{i}\right),
\tag{5.12}
$$

where the matrix of the linear partial differential operator $\mathcal{P}\left(\mathbf{x}_{i}, \nabla\right)=\left[\mathcal{P}\left(\mathbf{x}_{i}, \nabla\right)_{i q}\right](i, q=$
$\cdots, N)$ has the operator elements

$$
\begin{aligned}
\mathcal{P}\left(\mathbf{x}_{i}, \nabla\right)_{i q}= & \delta_{i q}\left[\mathbf{I}-\sum_{q=1}^{N} \int \mathcal{T}_{i q}\left(\mathbf{x}_{i}, \mathbf{x}_{q}\right) \mathrm{d} \mathbf{x}_{q}\right] \\
& -\sum_{|\alpha|=0}^{m} \frac{1}{\alpha!} \int \mathcal{F}_{i q}\left(\mathbf{x}_{i}, \mathbf{x}_{q}\right) \otimes\left(\mathbf{x}_{i}-\mathbf{x}_{q}\right)^{\alpha} \mathrm{d} \mathbf{x}_{q} \nabla^{\alpha}.
\end{aligned}
\tag{5.13}
$$

The operator $\mathcal{P}\left(\mathbf{x}_{i}, \nabla\right)$ is a linear partial differential operator with the constant coefficients
$\mathcal{P}\left(\mathbf{x}_{i}, \nabla\right) \equiv \mathcal{P}(\nabla)$ for statistically homogeneous media (4.6).

Considering that Equation (5.12) is a differential equation with constant coefficients,
the method of solution that first comes to mind is using the Fourier transform method to
transform the differential problem of solving (5.12) into the division problem of solving the
multiplicative equation (see, for example, [50, 51]). The Fourier transformation $\tilde{\mathbf{g}}(\boldsymbol{\xi})$ of a
function $\mathbf{g}(\mathbf{x})$ and its inverse are defined by the formulae

$$
\begin{aligned}
\mathrm{F}(\mathbf{g}) & \equiv \tilde{\mathbf{g}}(\boldsymbol{\xi})=\int \mathbf{g}(\mathbf{x}) \mathrm{e}^{-i \xi \cdot \mathbf{x}} \mathrm{d} \mathbf{x}, \\
\mathbf{g}(\mathbf{x}) & =\mathrm{F}^{-1}(\tilde{\mathbf{g}})=(2 \pi)^{-d} \int \tilde{\mathbf{g}}(\boldsymbol{\xi}) \mathrm{e}^{i \xi \cdot \mathbf{x}} \mathrm{d} \boldsymbol{\xi}.
\end{aligned}
\tag{5.14}
$$

provided, of course, that the integrals on the right-hand sides of the equations are convergent;
here $\xi \cdot \mathbf{x}=\xi_{1} x_{1}+\ldots+\xi_{d} x_{d}$ and $i=\sqrt{-1}$. Using the properties of Fourier transforms of
fundamental functions

$$
\begin{aligned}
F\left(\nabla^{\alpha} \mathbf{g}(\mathbf{x})\right) & =(i \boldsymbol{\xi})^{\alpha} \tilde{\mathbf{g}}(\boldsymbol{\xi}), \\
F^{-1}\left((i \boldsymbol{\xi})^{\alpha} \tilde{\mathbf{g}}(\boldsymbol{\xi})\right) & =\nabla^{\alpha} \mathbf{g}(\mathbf{x})
\end{aligned}
\tag{5.15}
$$

enables us to transform the linear differential equation with the constant coefficient (5.12) to
the algebraic multiplicative equation

$$
\mathcal{P}(i \boldsymbol{\xi}) \widetilde{\mathcal{E}}(\boldsymbol{\xi})=\tilde{\mathcal{E}^{a v}}(\boldsymbol{\xi}),
\tag{5.16}
$$

where a symbol $\mathcal{P}(i \boldsymbol{\xi})$ of the operator $\mathcal{P}(\nabla)$ is a polynomial with complex coefficients in
$R^{d}$ real transform variable $\boldsymbol{\xi}=\left(\xi_{1}, \ldots, \xi_{d}\right)^{\top}$. Taking Equation $\left(5.14_{2}\right)$ into account, we can
write

$$
\mathcal{E}(\mathbf{x})=(2 \pi)^{-d} \int \mathrm{e}^{i \xi \cdot \mathbf{x}} \mathcal{P}^{-1}(i \boldsymbol{\xi}) \tilde{\mathcal{E}^{a v}}(\boldsymbol{\xi}) \mathrm{d} \boldsymbol{\xi}
\tag{5.17}
$$

which should be a solution of (5.12) in view of (5.14). Equation (5.17) provides a conve-
nient way of calculating the average polarization tensor $\mathcal{E}(\mathbf{x})$ for given average $\tilde{\mathcal{E}^{a v}}(\mathbf{x})$ if we
```

know the transformed properties $\mathcal{P}^{-1}(i\boldsymbol{\xi})$. To facilitate explicit results we restrict attention to "long-wave" approximations and approximate $\mathcal{P}^{-1}(i\boldsymbol{\xi})$ by its Taylor expansion about $\boldsymbol{\xi} = \mathbf{0}$

$$
\mathcal{P}^{-1}(i\boldsymbol{\xi}) = \sum_{k=0}^{m} \mathcal{Y}_{(k)}(i\boldsymbol{\xi}), \tag{5.18}
$$

where the functions

$$
\mathcal{Y}_{(k)} = \left[ \mathcal{Y}_{(k)ij} \right] = \sum_{|\alpha|=k} \mathcal{Y}^{\alpha}(i\boldsymbol{\xi}) \tag{5.19}
$$

are constructed by the functions $\mathcal{Y}^{\alpha}(i\boldsymbol{\xi})$ proportional to $(i\boldsymbol{\xi})^{\alpha}$ . Then Equations (5.17) and (5.18) lead to the representation of concentration of strain polarization by the differential operator

$$
\mathcal{E}(\mathbf{x}) = \sum_{k=0}^{m} \mathcal{Y}_{(k)}(\nabla) \mathcal{E}^{av}(\mathbf{x}). \tag{5.20}
$$

The local part of the differential operator (5.19) coincides with the local part of the integral operator (5.7)

$$
\mathcal{Y}_{(0)}(\nabla) \equiv \mathbf{Y} = \left[ \mathbf{Y}_{ij} \right], \tag{5.21}
$$

Truncating Equation (5.19) after the first four sets of terms, making use of Equation (5.18) gives the following equations on $\mathcal{Y}_{(m)}(\nabla)$ ($m = 1, \dots, 4$):

$$
\begin{aligned}
\mathcal{Y}_{(1)}(\nabla) &= \mathbf{Y}\mathcal{B}_{1}(\nabla)\mathbf{Y}, \tag{5.22}
\\
\mathcal{Y}_{(2)}(\nabla) &= \mathbf{Y}\mathcal{B}_{2}(\nabla)\mathbf{Y} + \mathbf{Y}\mathcal{B}_{1}(\nabla)\mathbf{Y}\mathcal{B}_{1}(\nabla)\mathbf{Y}, \tag{5.23}
\\
\mathcal{Y}_{(3)}(\nabla) &= \mathbf{Y}\mathcal{B}_{3}(\nabla)\mathbf{Y} + \mathbf{Y}\mathcal{B}_{1}(\nabla)\mathbf{Y}\mathcal{B}_{2}(\nabla)\mathbf{Y}
\\
&\quad + \mathbf{Y}\mathcal{B}_{2}(\nabla)\mathbf{Y}\mathcal{B}_{1}(\nabla)\mathbf{Y}
\\
&\quad + \mathbf{Y}\mathcal{B}_{1}(\nabla)\mathbf{Y}\mathcal{B}_{1}(\nabla)\mathbf{Y}\mathcal{B}_{1}(\nabla)\mathbf{Y}, \tag{5.24}
\\
\mathcal{Y}_{(4)}(\nabla) &= \mathbf{Y}\mathcal{B}_{4}(\nabla)\mathbf{Y} + \mathbf{Y}\mathcal{B}_{2}(\nabla)\mathbf{Y}\mathcal{B}_{2}(\nabla)\mathbf{Y}
\\
&\quad + \mathbf{Y}\mathcal{B}_{1}(\nabla)\mathbf{Y}\mathcal{B}_{3}(\nabla)\mathbf{Y}
\\
&\quad + \mathbf{Y}\mathcal{B}_{3}(\nabla)\mathbf{Y}\mathcal{B}_{1}(\nabla)\mathbf{Y}
\\
&\quad + \mathbf{Y}\mathcal{B}_{1}(\nabla)\mathbf{Y}\mathcal{B}_{1}(\nabla)\mathbf{Y}\mathcal{B}_{2}(\nabla)\mathbf{Y}
\\
&\quad + \mathbf{Y}\mathcal{B}_{1}(\nabla)\mathbf{Y}\mathcal{B}_{2}(\nabla)\mathbf{Y}\mathcal{B}_{1}(\nabla)\mathbf{Y}
\\
&\quad + \mathbf{Y}\mathcal{B}_{2}(\nabla)\mathbf{Y}\mathcal{B}_{1}(\nabla)\mathbf{Y}\mathcal{B}_{1}(\nabla)\mathbf{Y}
\\
&\quad + \mathbf{Y}\mathcal{B}_{1}(\nabla)\mathbf{Y}\mathcal{B}_{1}(\nabla)\mathbf{Y}\mathcal{B}_{1}(\nabla)\mathbf{Y}\mathcal{B}_{1}(\nabla)\mathbf{Y}. \tag{5.25}
\end{aligned}
$$

The next iterations have the series form for the solution $\mathcal{Y}_{(m)}(\nabla)$ ($m=1,\dots$):

$$
\mathcal{Y}_{(m)}(\nabla)=\mathbf{Y} \sum_{n=1}^{m} \sum_{k_{1}+\ldots+k_{n}=m} \mathcal{B}_{k_{1}}(\nabla) \mathbf{Y} \ldots \mathcal{B}_{k_{n}}(\nabla) \mathbf{Y},
\tag{5.26}
$$

where

$$
\mathcal{B}_{k}(\nabla)=\sum_{|\alpha|=k} \mathcal{B}^{\alpha}(\nabla), \quad \mathcal{B}^{\alpha}(\nabla)=\left[\mathcal{B}_{i j}^{\alpha}(\nabla)\right],
\tag{5.27}
$$

$$
\mathcal{B}_{i j}^{\alpha}(\nabla)=\frac{1}{\alpha !} \int \mathcal{F}_{i j}\left(\mathbf{x}_{i}-\mathbf{x}_{j}\right)\left[\left(\mathbf{x}_{j}-\mathbf{x}_{i}\right)^{\alpha} \cdot \nabla^{\alpha}\right] \mathrm{d} \mathbf{x}_{j},
\tag{5.28}
$$

$\alpha \in Z_{+}^{d}, k, k_{1}, \ldots, k_{n} \in Z_{+}^{1}, n=1, \ldots, m$. For statistically isotropic composites the differential operators $\mathcal{B}_{k}(\nabla)$ of odd order $k=2 n-1$ ($n=1,\dots$) equal zero identically, simply because, for considered composites, the generalized functions $\mathcal{F}_{i j}\left(\mathbf{x}_{i}-\mathbf{x}_{j}\right)$ will be even homogeneous functions.

## 6. AVERAGE STRESSES IN THE COMPONENTS AND EFFECTIVE PROPERTIES

The mean field of elastic stresses inside the inclusions $\langle\boldsymbol{\sigma}\rangle_{i}(\mathbf{z})$ ($\mathbf{z} \in v_{i}$) is obtained from Equations (3.5) and (5.20)

$$
\begin{aligned}
\langle\boldsymbol{\sigma}\rangle_{i}(\mathbf{z})= & \mathbf{B}_{i}(\mathbf{z}) \mathbf{R}_{i}^{-1}\left\{\sum_{j=1}^{N} \mathbf{Y}_{i j}\left(\mathbf{R}_{j}\langle\boldsymbol{\sigma}\rangle\left(\mathbf{x}_{i}\right)+\mathbf{F}_{j}\right)-\mathbf{F}_{i}\right\}+\mathbf{C}_{i}(\mathbf{z}) \\
& +\mathbf{B}_{i}(\mathbf{z}) \mathbf{R}_{i}^{-1} \sum_{j=1}^{N} \sum_{k=1}^{m} \mathcal{Y}_{(k) i j}(\nabla) \mathbf{R}_{j}\langle\boldsymbol{\sigma}\rangle\left(\mathbf{x}_{i}\right),
\end{aligned}
\tag{6.1}
$$

and therefore

$$
\begin{aligned}
\langle\boldsymbol{\sigma}\rangle_{i}\left(\mathbf{x}_{i}\right)= & \mathbf{B}_{i}\left\{\mathbf{D}_{i}\langle\boldsymbol{\sigma}\rangle\left(\mathbf{x}_{i}\right)+\mathbf{R}_{i}^{-1} \sum_{j=1}^{N}\left(\mathbf{Y}_{i j}-\mathbf{I} \delta_{i j}\right) \mathbf{F}_{j}\right\}+\mathbf{C}_{i} \\
& +\mathbf{B}_{i} \mathbf{R}_{i}^{-1} \sum_{j=1}^{N} \sum_{k=1}^{m} \mathcal{Y}_{(k) i j}(\nabla)\left[\mathbf{R}_{j}\langle\boldsymbol{\sigma}\rangle\left(\mathbf{x}_{i}\right)+\mathbf{F}_{j}\right],
\end{aligned}
\tag{6.2}
$$

where the tensor

$$
\mathbf{D}_{i}=\mathbf{R}_{i}^{-1} \sum_{j=1}^{N} \mathbf{Y}_{i j} \mathbf{R}_{j},
\tag{6.3}
$$

$(i=1,\dots,N)$ has a simple physical meaning of the action of surrounding inclusions on the one at $\mathbf{x}_i$: $\langle\overline{\boldsymbol{\sigma}}\rangle_i=\mathbf{D}_i(\mathbf{x}_i)\langle\boldsymbol{\sigma}\rangle(\mathbf{x}_i)$ for $\boldsymbol{\beta}(\mathbf{x})\equiv\mathbf{0}$ and $\langle\boldsymbol{\sigma}\rangle(\mathbf{x})\equiv$ const.; the variable $\mathbf{z}\in v_i$ is defined in the local coordinate system connected with the semi-axis of the ellipsoid $v_i$. The mean matrix stress follows simply from the relation

$$
\langle\boldsymbol{\sigma}\rangle_{0}(\mathbf{x})=\frac{1}{c^{(0)}}(\langle\boldsymbol{\sigma}\rangle(\mathbf{x})-\langle\boldsymbol{\sigma}V\rangle(\mathbf{x})).\tag{6.4}
$$

In a similar manner the statistical average stresses in the components in the form of integral operators can be obtained from Equation (5.7).

Taking the ensemble average of a local constitutive equation accompanied with Equation (5.20) gives a macroscopic constitutive equation that relates $\langle\boldsymbol{\varepsilon}\rangle(\mathbf{x})$ and $\langle\boldsymbol{\sigma}\rangle(\mathbf{x})$:

$$
\langle\boldsymbol{\varepsilon}\rangle(\mathbf{x})=\mathbf{M}^{*}\langle\boldsymbol{\sigma}\rangle(\mathbf{x})+\boldsymbol{\beta}^{*}+\mathcal{M}^{*}(\langle\boldsymbol{\sigma}\rangle)(\mathbf{x}),\tag{6.5}
$$

$$
\mathbf{M}^{*}=\mathbf{M}^{(0)}+\sum_{i,j=1}^{N}\mathbf{Y}_{ij}\mathbf{R}_{j}n^{(i)},\tag{6.6}
$$

$$
\boldsymbol{\beta}^{*}=\boldsymbol{\beta}^{(0)}+\sum_{i,j=1}^{N}\mathbf{Y}_{ij}\mathbf{F}_{j}n^{(i)},\tag{6.7}
$$

$$
\mathcal{M}^{*}(\langle\boldsymbol{\sigma}\rangle)(\mathbf{x})=\sum_{i,j=1}^{N}\sum_{k=1}^{m}n^{(i)}\mathcal{Y}_{(k)ij}(\nabla)\mathbf{R}_{j}\langle\boldsymbol{\sigma}\rangle(\mathbf{x}).\tag{6.8}
$$

The differential operator $\mathcal{M}^{*}(\langle\boldsymbol{\sigma}\rangle)$ of the second order $(m=2)$ (6.10) is reduced to the analogous relation proposed by Buryachenko [29] for the identical homogeneous inclusions (3.6) $(N=1)$.

## 7. PARTICULAR CASES

### 7.1. Perturbation method

In the case of a dilute concentration of the inclusions as well as for weakly inhomogeneous medium

$$
c\ll1\tag{7.1}
$$

or

$$
||\mathbf{M}_{1}^{(i)}\mathbf{L}^{(0)}||\ll1,\tag{7.2}
$$

the perturbation method is appropriate. Then instead of hypothesis **H2** (4.2) we can use the assumption

$$
\langle\widetilde{\sigma}_{i,q}(\mathbf{x})\rangle_{j}=\langle\boldsymbol{\sigma}\rangle(\mathbf{x}_{j}).\quad(j=i,q),\tag{7.3}
$$

and Equation (4.3) is reduced to

$$
\begin{aligned}
\bar{v}_{i}\left\langle\boldsymbol{\eta}_{i}\right\rangle\left(\mathbf{x}_{i}\right) & =\bar{v}_{i}\left\langle\boldsymbol{\eta}_{i}^{a v}\right\rangle\left(\mathbf{x}_{i}\right)+\sum_{q=1}^{N}\left\{\int \mathcal{T}_{i q}\left(\mathbf{x}_{i}-\mathbf{x}_{q}\right) \mathrm{d} \mathbf{x}_{q} \bar{v}_{i}\left\langle\boldsymbol{\eta}_{i}^{a v}\right\rangle\left(\mathbf{x}_{i}\right)\right. \\
& \left.+\int \mathcal{F}_{i q}\left(\mathbf{x}_{i}-\mathbf{x}_{q}\right) \bar{v}_{q}\left\langle\boldsymbol{\eta}_{q}^{a v}\right\rangle\left(\mathbf{x}_{q}\right) \mathrm{d} \mathbf{x}_{q}\right\}
\end{aligned}
\tag{7.4}
$$

leading to the overall constitutive equations (6.7) with effective properties

$$
\begin{aligned}
\mathbf{M}^{* p e r} & =\mathbf{M}^{(0)}+\sum_{i=1}^{N}\left\{\mathbf{I}+\sum_{q=1}^{N} \int\left[\mathcal{T}_{i q}\left(\mathbf{x}_{i}-\mathbf{x}_{q}\right)\right.\right. \\
& \left.\left.+\mathcal{F}_{i q}\left(\mathbf{x}_{i}-\mathbf{x}_{q}\right)\right] \mathrm{d} \mathbf{x}_{q}\right\} n^{(i)} \mathbf{R}_{q},
\end{aligned}
\tag{7.5}
$$

$$
\begin{aligned}
\boldsymbol{\beta}^{* p e r} & =\boldsymbol{\beta}^{(0)}+\sum_{i=1}^{N}\left\{\mathbf{I}+\sum_{q=1}^{N} \int\left[\mathcal{T}_{i q}\left(\mathbf{x}_{i}-\mathbf{x}_{q}\right)\right.\right. \\
& \left.\left.+\mathcal{F}_{i q}\left(\mathbf{x}_{i}-\mathbf{x}_{q}\right)\right] \mathrm{d} \mathbf{x}_{q}\right\} n^{(i)} \mathbf{F}_{q},
\end{aligned}
\tag{7.6}
$$

$$
\mathcal{M}^{* p e r}(\langle\boldsymbol{\sigma}\rangle)(\mathbf{x})=\sum_{i, q=1}^{N} n^{(i)} \int \mathcal{F}_{i q}\left(\mathbf{x}_{i}-\mathbf{x}_{q}\right) \mathbf{R}_{q}\left[\langle\boldsymbol{\sigma}\rangle\left(\mathbf{x}_{q}\right)-\langle\boldsymbol{\sigma}\rangle\left(\mathbf{x}_{i}\right)\right] \mathrm{d} \mathbf{x}_{q}.
\tag{7.7}
$$

For the representation of the integral operator (7.7) in the differential form, we expand $\langle\boldsymbol{\sigma}\rangle(\mathbf{x}_{q})$ about $\mathbf{x}_{i}$ in a Taylor series and integrate term by term over the whole space

$$
\mathcal{M}^{* p e r}(\langle\boldsymbol{\sigma}\rangle)(\mathbf{x})=\sum_{i, q=1}^{N} \sum_{|\alpha|=1}^{\infty} n^{(i)} \mathcal{B}_{i q}^{\alpha}(\nabla) \mathbf{R}_{q}\langle\boldsymbol{\sigma}\rangle(\mathbf{x}).
\tag{7.8}
$$

Equations (7.5)-(7.8) are reduced to the analogous relations proposed by Buryachenko [29] for identical homogeneous inclusions (3.6) ($N=1$); a simplified approach by Buryachenko and Rammerstorfer [30] used a point approximation $\mathbf{T}_{i j}\left(\mathbf{x}_{i}-\mathbf{x}_{j}\right)=\boldsymbol{\Gamma}\left(\mathbf{x}_{i}-\mathbf{x}_{j}\right)$ of binary interactions of the inclusions described by the matrix $\mathbf{Z}_{i j}$ (3.7) obtained from Equation (3.8) by a few iterations of a successive approximation method.

It should be mentioned that effective properties can be estimated by the use of the evalua- tion of average strains in the components. In so doing, utilization of the perturbation method as well as the combined MEFM-perturbation method reduce to an inequality $\mathbf{L}^{*} \neq(\mathbf{M}^{*})^{-1}$ in contrast to the MEFM (6.9). Because of this Equations (7.5)-(7.7) will be employed if $\mathbf{M}_{1}(\mathbf{x})$ is positive definite, otherwise a dual scheme based on the estimation of average strains $\langle\boldsymbol{\varepsilon}\rangle_{i}$ and effective moduli $\mathbf{L}^{*}$ will be used.

### 7.2. *"Quasi-crystalline" approximation*

In the framework of the "quasi-crystalline" approximation (3.4), the matrix $\mathbf{Y}^{-1}$ can be reduced to (see, for example, [6])

$$
\left(\mathbf{Y}^{-1}\right)_{i j}=\mathbf{I} \delta_{i j}-\mathbf{R}_{i} \int\left[\mathbf{T}_{i j}\left(\mathbf{x}_{i}-\mathbf{x}_{j}\right) \varphi\left(v_{j}, \mathbf{x}_{j} \mid ; v_{i}, \mathbf{x}_{i}\right)-\mathbf{T}_{i}\left(\mathbf{x}_{i}-\mathbf{x}_{j}\right) n^{(j)}\right] \mathrm{d} \mathbf{x}_{j}. \quad(7.9)
$$

The final results may be significantly simplified under the following additional assumptions:

$$
\left\langle V_{j}(\mathbf{y}) \boldsymbol{\eta}_{j} \mid ; v_{i}, \mathbf{x}_{i}\right\rangle=\mathbf{h}_{1}\left(\left\langle\boldsymbol{\eta}_{j}\right\rangle, \rho\right), \quad \rho \equiv\left|\mathbf{a}_{i}^{-1}\left(\mathbf{x}_{j}-\mathbf{x}_{i}\right)\right|. \quad(7.10)
$$

Here the dependence of the function $\mathbf{h}_{1}$ on the geometrical parameters of the inclusion $v_{i}$ is defined by the scalar value $\rho$; $\mathbf{a}_{i}^{-1}$ identifies a matrix of affine transformation which transfers the ellipsoid $v_{i}$ into a unit sphere. According to relation (7.10) the conditional averaging properties of the composite have level surfaces which are obtained from the ellipsoidal surfaces $\partial v_{i}$ by the use of a homothetic transformation. Under the assumption of (3.4), the equality (7.10) is valid under the simplest conditional probability density

$$
\varphi\left(v_{q}, \mathbf{x}_{q} \mid ; v_{i}, \mathbf{x}_{i}\right)=h_{2}(\rho). \quad(7.11)
$$

For spherical inclusions, the relation (7.11) is realized for statistical isotropy of the composite structure.

According to Equations (3.4) and by virtue of the fact that the generalized function $\boldsymbol{\Gamma}(\mathbf{x})$ is an even homogeneous function of order $-3$, we obtain, under the assumption (7.10), the following relation

$$
\begin{aligned}
& \sum_{q=1}^{N} \iint \boldsymbol{\Gamma}\left(\mathbf{x}-\mathbf{x}_{q}\right)\left[\left\langle V_{q}\left(\mathbf{x}_{q}\right) \boldsymbol{\eta}\left(\mathbf{x}_{q}\right) \mid ; v_{i}, \mathbf{x}_{i}\right\rangle\right. \\
& \left.-c^{(q)}\left\langle\boldsymbol{\eta}_{q}\right\rangle\left(\mathbf{x}_{q}\right)\right] V_{i}(\mathbf{x}) \mathrm{d} \mathbf{x}_{q} \mathrm{~d} \mathbf{x} \\
& =\sum_{k=0}^{m} \mathcal{Q}_{i}^{k}(\nabla) \sum_{q=1}^{N}\left\langle\boldsymbol{\eta}_{q}\right\rangle\left(\mathbf{x}_{i}\right) c^{(q)},
\end{aligned}
$$

where $\mathcal{Q}_{i}^{0}(\nabla) \equiv \mathbf{Q}_{i}$ and for $k=1, \ldots$

$$
\begin{aligned}
\mathcal{Q}_{i}^{k}(\nabla)= & \sum_{|\alpha|=k} \frac{1}{\alpha !} \int\left[\mathbf{T}_{i q}\left(\mathbf{x}_{i}-\mathbf{x}_{q}\right) \varphi\left(v_{q}, \mathbf{x}_{q} \mid ; v_{i}, \mathbf{x}_{i}\right) / n^{(q)}\right. \\
& \left.-\mathbf{T}_{i}\left(\mathbf{x}_{i}-\mathbf{x}_{q}\right)\right]\left(\mathbf{x}_{q}-\mathbf{x}_{i}\right)^{\alpha} \mathbf{x}_{q} \nabla^{\alpha}.
\end{aligned}
$$

In the framework of "quasi-crystallite approximation" (3.4), the operator $\mathcal{Q}_{i}^{k}(\nabla)$ is associated with the operator $\mathcal{B}_{k i j}(\nabla)(5.27)$:

$$
\mathcal{B}_{k i j}\left(\mathbf{x}_{i}, \nabla\right)=\mathbf{R}_{i} \mathcal{Q}_{i}^{k}(\nabla) n^{(j)}. \quad(7.14)
$$

Taking the assumptions (3.4) into account, Equation (6.3) can be combined into a simple equation

$$
\langle\boldsymbol{\sigma}\rangle_{i}=\mathbf{B}_{i}\langle\boldsymbol{\sigma}\rangle+\mathbf{C}_{i}+\mathbf{B}_{i} \mathbf{Q}_{i} \sum_{k=0}^{m} \mathcal{Y}_{(k)}^{Q}(\nabla) \sum_{q=1}^{N} \mathbf{R}_{q}\langle\boldsymbol{\sigma}\rangle(\mathbf{x}) n^{(q)},\qquad(7.15)
$$

where the tensor $\mathcal{Y}_{(0)}^{Q}$, introduced in (7.15), is defined as

$$
\mathcal{Y}_{(0)}^{Q}(\nabla) \equiv \mathbf{Y}^{Q}=\left[\mathbf{I}-\sum_{q=1}^{N} n^{(q)} \mathbf{R}_{q} \mathbf{Q}_{q}\right]^{-1},\qquad(7.16)
$$

and for statistically isotropic media the differential operators of odd order (7.15) vanish identically $\mathcal{Y}_{(k)}^{Q}(\nabla) \equiv \mathbf{0} ;(k=2 n-1, n=1,2, \ldots)$. In such a case, the first non-zero operators $\mathcal{Y}_{(k)}^{Q}(\nabla),(k=2,4)(7.15)$ are represented by the formulae

$$
\mathcal{Y}_{(2)}^{Q}(\nabla)=\mathbf{Y}^{Q}\left[\sum_{q=1}^{N} n^{(q)} \mathbf{R}_{q} \mathcal{Q}_{q}^{2}(\nabla)\right] \mathbf{Y}^{Q}\qquad(7.17)
$$

$$
\begin{aligned}
\mathcal{Y}_{(4)}^{Q}(\nabla)= & \mathbf{Y}^{Q}\left[\sum_{q=1}^{N} n^{(q)} \mathbf{R}_{q} \mathcal{Q}_{q}^{4}(\nabla)\right] \mathbf{Y}^{Q} \\
& +\mathbf{Y}^{Q}\left[\sum_{q=1}^{N} n^{(q)} \mathbf{R}_{q} \mathcal{Q}_{q}^{2}(\nabla)\right] \mathbf{Y}^{Q}\left[\sum_{q=1}^{N} n^{(q)} \mathbf{R}_{q} \mathcal{Q}_{q}^{2}(\nabla)\right] \mathbf{Y}^{Q}. \quad(7.18)
\end{aligned}
$$

Substitution of Equations (7.17) and (7.18) into Equation (6.10) results in

$$
\mathbf{M}^{*}=\mathbf{M}^{(0)}+\mathbf{Y}^{Q} \sum_{i=1}^{N} \mathbf{R}_{i} n^{(i)},\qquad(7.19)
$$

$$
\boldsymbol{\beta}^{*}=\langle\boldsymbol{\beta}\rangle+\mathbf{Y}^{Q} \sum_{i=1}^{N} \mathbf{F}_{i} n^{(i)},\qquad(7.20)
$$

$$
\mathcal{M}^{*}(\langle\boldsymbol{\sigma}\rangle)(\mathbf{x})=\left[\mathbf{I}-\left(\mathbf{Y}^{Q}\right)^{-1}\right]\left[\sum_{k=2}^{m} \mathcal{Y}_{(k)}^{Q}(\nabla)\right] \sum_{q=1}^{N} \mathbf{R}_{q}\langle\boldsymbol{\sigma}\rangle(\mathbf{x}) n^{(q)}.\qquad(7.21)
$$

The relations (7.19) and (7.21) are obtained for $N$-component inclusions, which can differ from one another by their thermoelastic properties and internal microtopologies. For identical unidirectionally aligned inclusions $(N=1)$, when $\mathcal{Q}_{q}^{k}(\nabla) \equiv \mathcal{Q}^{k}(\nabla)$ and $\varphi(v_{q}, \mathbf{x}_{q} \mid v_{i}, \mathbf{x}_{i}) /$ $n^{(q)} \equiv \varphi(v_{p}, \mathbf{x}_{p} \mid v_{i}, \mathbf{x}_{i}) / n^{(p)}$ for $\forall p, q \neq i$ and $\forall k=0,1, \ldots$, the relation (7.15) is simplified $(i=1)$

$$
\langle\boldsymbol{\sigma}\rangle_{i}=\left[\mathbf{I}-\mathbf{Q} \mathbf{R}_{i} n^{(i)}\right]^{-1}\left(\mathbf{B}_{i}\langle\boldsymbol{\sigma}\rangle(\mathbf{x})+\mathbf{C}_{i}\right)
$$

$$+\mathbf{B}_{i} \mathbf{Q} \sum_{k=2}^{m} \mathcal{Y}_{(k)}^{Q}(\nabla) \mathbf{R}_{i}\left\langle\boldsymbol{\sigma}\right\rangle\left(\mathbf{x}_{i}\right) n^{(i)},\qquad(7.22)$$

and the non-local operators $\mathcal{Y}_{(k)}^{Q}(\nabla)(7.17)$ and $\mathcal{Y}_{(k)}^{Q}(\nabla)(7.18)$ are defined by the effective elastic compliance

$$\mathcal{Y}_{(2)}^{Q}(\nabla) \mathbf{R}_{i} n^{(i)}=\left(\mathbf{M}^{*}-\mathbf{M}^{(0)}\right) \mathcal{Q}^{2}(\nabla)\left(\mathbf{M}^{*}-\mathbf{M}^{(0)}\right),\qquad(7.23)$$

$$\begin{aligned}
\mathcal{Y}_{(4)}^{Q}(\nabla) \mathbf{R}_{i} n^{(i)}= & \left(\mathbf{M}^{*}-\mathbf{M}^{(0)}\right) \mathcal{Q}^{4}(\nabla)\left(\mathbf{M}^{*}-\mathbf{M}^{(0)}\right) \\
& +\left(\mathbf{M}^{*}-\mathbf{M}^{(0)}\right) \mathcal{Q}^{2}(\nabla)\left(\mathbf{M}^{*}-\mathbf{M}^{(0)}\right) \mathcal{Q}^{2}(\nabla)\left(\mathbf{M}^{*}-\mathbf{M}^{(0)}\right). \quad(7.24)
\end{aligned}$$

A "quasi-crystallite" approximation (3.4), which is equivalent to the assumption

$$\mathbf{Z}_{i j}=\mathbf{I} \delta_{i j},\qquad(7.25)$$

when $\mathcal{T} \equiv 0$ (4.4) and $\mathbf{Z}_{q q}=\mathbf{I}$ (4.5) was used in [22,23] (see also [52,53]), where the authors obtained the differential operator $\mathcal{M}^{*}(6.7)$ of the second and fourth orders for an arbitrary comparison moduli and for another conditional probability density $\langle V^{(i)}(x) V^{(q)}(y)\rangle$ describing the random structure of composites instead of $\varphi(v_{q}, x_{q} | v_{i}, x_{i})$ . Drugan [24] has proposed a similar approach for the estimation of the fourth-order differential operator.

## 8. THE REDUCTION OF INTEGRAL OVERALL CONSTITUTIVE EQUATIONS TO DIFFERENTIAL ONES

If $\mathcal{E}^{a v}(x)$ belongs to $C^{m}(w)$ , then substituting its Taylor expansion analogous to (5.10) into the first-order iteration for the average strain polarization tensor $\mathcal{E}_{(1)}(x)(5.5)$ reduces this integral equation to the differential one

$$\mathcal{E}_{(1)}(\mathbf{x})=\left[\mathcal{Z}_{(0)}(\nabla)+\mathcal{Z}_{(1)}(\nabla)\right] \mathcal{E}^{a v}(\mathbf{x}),\qquad(8.1)$$

where $\mathcal{Z}_{(0)}(\nabla) \equiv \mathbf{Y}$ and the differential operators with the constant coefficients

$$\mathcal{Z}_{(1)}(\nabla)=\sum_{k=1}^{m} \mathcal{Z}_{(1)}^{k}(\nabla),$$

$$\mathcal{Z}_{(1)}^{k}(\nabla)=\sum_{|\alpha|=k} \frac{1}{\alpha!} \int \mathbf{K}(\mathbf{x}, \mathbf{y}) \mathbf{Y}\left[\otimes(\mathbf{y}-\mathbf{x})^{\alpha}\right] \mathrm{d} \mathbf{y} \nabla^{\alpha},\qquad(8.2)$$

can be recast, according to the notations (4.14) and (5.27), in the form

$$\mathcal{Z}_{(1)}^{k}(\nabla)=\mathbf{Y} \mathcal{B}_{k}(\nabla) \mathbf{Y}.\qquad(8.3)$$

For statistically isotropic composites all odd operators $\mathcal{B}^{\alpha}(\nabla) \equiv 0$ at $|\alpha|=2 n-1, n=$ 1,....

In a similar manner, substitution of the Taylor expansion $\mathcal{E}^{av}(\mathbf{x})$ for (5.10) into the representation for the second iteration (5.6) leads to the differential equation

$$
\mathcal{E}_{(2)}(\mathbf{x})=\left[\mathcal{Z}_{(0)}(\nabla)+\mathcal{Z}_{(1)}(\nabla)+\mathcal{Z}_{(2)}(\nabla)\right] \mathcal{E}^{a v}(\mathbf{x}),
\tag{8.4}
$$

where for the representation of $\mathcal{Z}_{(2)}(\nabla)$ we transform the iterated integral in Equation (5.6) in the following form

$$
\begin{aligned}
& \int \mathbf{K}(\mathbf{x}, \mathbf{y}) \mathbf{Y}\left\{\int \mathbf{K}(\mathbf{y}, \mathbf{z}) \mathbf{Y}\left[\mathcal{E}^{a v}(\mathbf{z})-\mathcal{E}^{a v}(\mathbf{y})\right] \mathrm{d} \mathbf{z}\right. \\
- & \left.\int \mathbf{K}(\mathbf{x}, \mathbf{z}) \mathbf{Y}\left[\mathcal{E}^{a v}(\mathbf{z})-\mathcal{E}^{a v}(\mathbf{x})\right] \mathrm{d} \mathbf{z}\right\} \mathrm{d} \mathbf{y} \\
= & \int \mathbf{Y} \mathcal{F}(\mathbf{x}-\mathbf{y}) \mathbf{Y} \mathcal{B}^{\alpha}(\nabla) \mathbf{Y}\left[\mathcal{E}^{a v}(\mathbf{y})-\mathcal{E}^{a v}(\mathbf{x})\right] \mathrm{d} \mathbf{y}.
\tag{8.5}
\end{aligned}
$$

Then the repeated use of the Taylor expansion for the function $\mathcal{E}^{av}(\mathbf{y})$ leads to the final representation

$$
\mathcal{Z}_{(2)}(\nabla)=\sum_{k=2}^{m} \mathcal{Z}_{(2)}^{k}(\nabla),
\tag{8.6}
$$

hereafter

$$
\mathcal{Z}_{(m)}^{k}(\nabla)=\sum_{\left|\alpha^{1}+\ldots \alpha^{m}\right|=k} \mathbf{Y} \mathcal{B}^{\alpha^{1}}(\nabla) \ldots \mathbf{Y} \mathcal{B}^{\alpha^{m}}(\nabla) \mathbf{Y}
\tag{8.7}
$$

and $\alpha^{i}=\left(\alpha_{1}^{i}, \ldots, \alpha_{d}^{i}\right) \in Z_{+}^{d} ; i=1, \ldots, m ; k=m, m+1, \ldots ; k, m \in Z_{+}^{1}$. The solutions (8.1) and (8.4) coincide with the first-order (5.5) and second-order (5.6) approximation, respectively, only for both $\mathcal{E}^{a v}(\mathbf{x}) \in C^{\infty}(w)$ and taking into account the infinite number of terms of the Taylor expansion of $\mathcal{E}^{a v}(\mathbf{x}), m=\infty$ (5.10). The construction of the following differential analogs $\mathcal{Z}_{(n)},(n=3,4, \ldots)$ of integral iterations $\mathcal{K}^{n}$ (5.7) is obvious. In so doing, the differential operators $\mathcal{Y}_{(n)}(n=0,1, \ldots)$ (5.21) can be obtained by truncations of differential operators $\mathcal{Z}_{(m)}(m=0, \ldots, n)$

$$
\mathcal{Y}_{(1)}(\nabla)=\mathcal{Z}_{(1)}^{1},
\tag{8.8}
$$

$$
\mathcal{Y}_{(2)}(\nabla)=\mathcal{Z}_{(1)}^{2}+\mathcal{Z}_{(2)}^{2},
\tag{8.9}
$$

$$
\mathcal{Y}_{(3)}(\nabla)=\mathcal{Z}_{(1)}^{3}+\mathcal{Z}_{(2)}^{3}+\mathcal{Z}_{(3)}^{3},
\tag{8.10}
$$

$$
\mathcal{Y}_{(4)}(\nabla)=\mathcal{Z}_{(1)}^{4}+\mathcal{Z}_{(2)}^{4}+\mathcal{Z}_{(3)}^{4}+\mathcal{Z}_{(4)}^{4},
\tag{8.11}
$$

and so on. For instance, for the estimation of the operator $\mathcal{Y}_{(2)}(\nabla)$ it is enough to apply the first-order approximation (5.5) to the quadratic polynomial approximation of the Taylor expansion (5.10) of the function $\mathcal{E}^{a v}(\mathbf{x})$. The operator $\mathcal{Y}_{(m)}$ can be estimated by application

of the $(m-1)$-order approximation of integral operator $\mathcal{K}^{(m-1)}$ (5.7) to the $m$th polynomial approximation of the Taylor expansion (5.10) of the function $\mathcal{E}^{av}(\mathbf{x})$. Again, all operators $\mathcal{Z}_{(m)}^{2n-1}$ $(n=1,2,..., m=1,..., 2n-1)$ as well as the operators $\mathcal{Z}_{(m)}^{2n}$ $(n=1,2,..., m=1,..., 2n)$ constructed by the operators $\mathcal{B}_{2k-1}(\nabla)$ $(k < n)$ of odd order vanish for statistically isotropic media.

## 9. NUMERICAL RESULTS
Just to demonstrate the comparison of available experimental data with the predicting opportunity of the method proposed, we will consider the zero-order approximation of the method that is the estimation of the effective elastic moduli $\mathbf{L}^{*} \equiv (\mathbf{M}^{*})^{-1}$ (6.8). We assume the matrix is epoxy resin $(k^{(0)}=4.27$ GPa and $\mu^{(0)}=1.53$ GPa) which contains identical circular glass fibers $(k^{(1)}=50.89$ GPa and $\mu^{(1)}=35.04$ GPa). Two alternative radial functions of inclusion distribution will be examined (see [54, 55, 56])

$$
g(\mathbf{x}_{i}-\mathbf{x}_{q}) \equiv \varphi(v_{i}, \mathbf{x}_{i} \mid ; v_{q}, \mathbf{x}_{q}) / n^{(q)}=H(r-2 a), \tag{9.1}
$$

$$
\begin{aligned}
g(\mathbf{x}_{i}-\mathbf{x}_{j})= & H(r-2 a) \\
& \times\left\{1+\frac{4 c}{\pi}\left[\pi-2 \sin ^{-1}\left(\frac{r}{4 a}\right)-\frac{r}{2 a} \sqrt{1-\frac{r^{2}}{16 a^{2}}}\right] H(4 a-r)\right\}(9.2)
\end{aligned}
$$

where $H$ denotes the Heaviside step function, $r \equiv |\mathbf{x}_{i}-\mathbf{x}_{q}|$ is the distance between the non-intersecting inclusions $v_{i}$ and $v_{q}$, and $c$ is the volume fraction of fibers of the radius $a$. The formula (9.2) takes into account a neighboring order in the distribution of the inclusions. As can be seen from Figure 1, the use of the approach (6.8), (7.9) based on the quasi-crystalline approximation (3.4) (also called the Mori-Tanaka (MT) approach) leads to an underestimate of the effective shear modulus by 1.85 times for $c=0.7$ compared to the experimental data as well as to the more exact approximation of the MEFM (4.9), (6.8) which provides the best comparison with experimental data by Lee and Mykkanen [57]. It should be mentioned that the estimations by the MEFM are slightly sensitive to the choice of the radial distribution function either (9.1) or (9.2). It is observed that the proposed formulation compared well with experimental data for $c$ up to 65 percent; for fiber volume fraction greater than 70 percent, micro-defects existing in experimental specimens may significantly affect the overall elastic moduli. At the same time, the MT solution (6.8), (7.9) differs from the perturbation method approximation (7.5), (9.1) by not more than 5 percent for the concentration of the inclusions $c \leq 0.7$ and does not depend on the radial distribution function (in contrast to the perturbation method). Experimental confirmation of the advantages of the MEFM compared to other well-known methods for 3D problems can be found in [6].

Our approach in this section will be to employ the non-local equations for stress concentrator tensors we derived in the previous sections by the iteration and Fourier transform methods. We consider ensemble-averaged stress $\langle\boldsymbol{\sigma}\rangle(\mathbf{x})$, and determine the stress concentration factors $\langle\boldsymbol{\sigma}\rangle_{i}(\mathbf{x})$ at the inclusions by the quadrature method (QM), by the iteration method (IM) and, in some particular cases, by the Fourier transform methods (FTMs). The

![](./images/812388747818565633_2.jpg)

Figure 1. Variation of the effective shear modulus $\mu^{*}$ as a function of a concentration of the inclusions $c$.
Experimental data ($\circ$) and curves are calculated by Equations (6.6) and (9.2) (solid line), (6.6) and (9.1)
(dot-dashed line), (7.5) and (9.2) (dashed line), (7.5) and (9.1) ($\diamond$), and (7.19) (dotted line).

quantitative results we obtain will be for the 2D case (plane strain problem) for the two-phase
composites consisting of an isotropic matrix reinforced by a random dispersion of isotropic
identical circle particles.

Let us now demonstrate the application of the theoretical results by considering an iso-
tropic highly filled composite ($c=0.6$) made of an incompressible isotropic matrix $\mathbf{L}^{(0)}=$
$(\infty, 2 \mu^{(0)})$ (2.1), filled with rigid circle inclusions $\mathbf{L}^{(1)}=(\infty, \infty)$ of one size $a=1$,
$N=1$. This example with the infinite contrast between the two phases was chosen deliber-
ately because it provides the maximum difference of predictions of effective elastic response
estimated by various methods, and was considered by a number of authors. We consider the
response for a normal loading that varies with position in its loading direction

$$
\left\langle\sigma_{i j}\right\rangle(\mathbf{x})=f\left(x_{1}\right) \delta_{1 i} \delta_{1 j}. \tag{9.3}
$$

with three specific cases of the functions

$$
f_{1}\left(x_{1}\right)=\sin \left(\frac{\pi}{4} x_{1}\right), \tag{9.4}
$$

$$
f_{2}\left(x_{1}\right)=0.6579\left|x_{1}\right|^{2.001} e^{-0.2422 x_{1}^{2}}, \tag{9.5}
$$

$$
f_{3}\left(x_{2}\right)=0.6584\left|x_{1}\right|^{1.999} e^{-0.2422 x_{1}^{2}}, \tag{9.6}
$$

$$
f_{4}\left(x_{2}\right)=0.6580 x_{1}^{2} e^{-0.2420 x_{1}^{2}}. \tag{9.7}
$$

The loading (9.3), (9.4) with $f_{1}\left(x_{1}\right) \in C^{\infty}(R)$ was analyzed by the FTM in detail in [23,24]
for the different arguments and the different concentrations of the spherical inclusions. We
can only define the $m$th derivatives of the functions $f_{j}(0)(j=2,3)$ if $f_{j}^{(m)}(-0)=f_{j}^{(m)}(+0)$.
Now $f_{2} \in C^{2}$ and $f_{3} \in C^{1}$ and the third and the second derivatives do not exist for the func-

![](./images/812388747818565633_3.jpg)

Figure 2. The functions and their first derivatives versus argument $x_{1}$: $f_{2}(x_{1})$ (solid line); $f_{1}(x_{1})$ (dot-dashed line); $f_{1}'(x_{1})$ (dashed line); $f_{2}'(x_{1})$ (dotted line).

tions $f_{2}$ and $f_{3}$, respectively. The functions $f_{j}$ ($j=2,3,4$) have approximately the same max and the same max of their first derivatives as the function $f_{1}$: $|\max f_{j}(x_{1})-1|<10^{-4}$, $|\max f_{j}'(x_{1})-\max f_{1}'(y_{1})|<10^{-4}$, ($j=2,3,4$; $x_{1}, y_{1} \in R$) (see Figure 2). In so doing, $f_{2}''(0)=0$ and, therefore, $\mathcal{Y}_{(2)}\langle\boldsymbol{\sigma}\rangle(\mathbf{0})=\mathbf{0}$ and the actions of the next order differential operators (6.4) $\mathcal{Y}_{(2)}\langle\boldsymbol{\sigma}\rangle(\mathbf{x})$ cannot be defined for the function $f_{2}(x_{1})$ due to non-differentiability of the function $f_{2}''(x_{1})$. Thus, independently from the concrete micromechanical average scheme, the FTM will predict zero non-local effects at the point $\mathbf{0}$ for the function $f_{2}(x_{1})$. Analogous analysis leads to a more dramatic conclusion for the function $f_{3}(x_{1})$, that is, the FTM cannot be applied in principle to the field (9.3), (9.6) because the differentiable function $f_{3}(x_{1})$ which is very close to $f_{2}(x_{1}) \in C^{2}$ and $f_{4}(x_{1}) \in C^{\infty}$ is not twice differentiable at $x_{1}=0$.

The comparative results estimated by the MEFM for the radial distribution function (9.2) ($c=0.6$) and for different functions $f_{j}(x_{1})$ ($j=1,...,4$) for 0th and 7th iterations are presented in Table 1; the results for functions $f_{2},f_{3},f_{4}$ differ from one another by less than 1 percent. Table 1 also gives the quantitative analysis of non-local effects presented in the terms of the stress variations $\Delta_{1}(\%) \equiv\langle\sigma_{11}\rangle_{i(7)}(\mathbf{0}) / \max\langle\sigma_{11}\rangle_{i(0)}$; $\Delta_{2}(\%) \equiv$ $\langle\max \sigma_{11}\rangle_{i(7)} / \max\langle\sigma_{11}\rangle_{i(0)}$. Table 2 presents $n$th iterations of the statistical average of stresses at the origin $\mathbf{0}$ estimated by the iteration method $\langle\sigma_{11}\rangle_{i(n)}(\mathbf{0})$ ($n=0,7,20$) and by the quadrature method (5.10) $\langle\sigma_{11}^{QM}\rangle_{i}(\mathbf{0})$. The 7th and 20th iterations differ from one other by 3 percent; the difference of the estimations by the quadrature method and the 20th iterations is not over 0.2 percent. In Figure 3 we present the stresses $\langle\sigma_{11}^{QM}\rangle_{i}(x_{1})$ for the function $f_{2}$ (9.5), radial distribution function $g(\mathbf{x}_{i}-\mathbf{x}_{j})$ (9.2), and $c=0.15,0.3,0.45,0.6$ estimated by the QM which differ from the estimations of 20th iterations by the IM less than 0.2 percent. Comparison of Figures 1 and 3 leads to the conclusion that the value of non-local stresses $\langle\sigma_{11}^{QM}\rangle_{i}(x_{1})-\langle\sigma_{11}\rangle_{i(0)}(x_{1})$ is more sensitive than the local effective modulus $\mathbf{L}^{*}$ to the value of the volume fiber concentration $c$. The first few iterations of estimations of stresses

![](./images/812388747818565633_4.jpg)

Figure 3. The statistical averages $\langle\sigma_{11}^{QM}\rangle_{i}(x_{1})$ versus $x_{1}$ estimated for the functions $f_{2}(x_{i})$ (9.5) and $g_{2}(r)$ (9.2) by the MEFM (4.6): $c = 0.15$ (solid line), 0.30 (dotted line), 0.45 (dot-dashed line), 0.60 (dashed line).

![](./images/812388747818565633_5.jpg)

Figure 4. The first few iterations of statistical averages $\langle\sigma_{11}\rangle_{i}(x_{1})$ versus $x_{1}$ estimated for $c = 0.6$, the functions $f_{2}(x_{i})$ (9.5) and $g_{2}(r)$ (9.2) by the MEFM (4.6): zero-order (solid line), first-order (dotted line), second-order (dot-dashed line), seventh-order (dashed line) approximations.

**NON-LOCAL MODELS OF RANDOM STRUCTURE COMPOSITES 429**

Table 1. Comparative analysis of different functions (9.4)–(9.7).
<table>
 <thead>
  <tr>
   <th>
   </th>
   <th>
    $\max{\langle\sigma_{11}\rangle}_{i(0)}$
   </th>
   <th>
    ${\langle\sigma_{11}\rangle}_{i(7)}{(\mathbf{0})}$
   </th>
   <th>
    $\max{\langle\sigma_{11}\rangle}_{i(7)}$
   </th>
   <th>
    $\Delta_{1}{(\%)}$
   </th>
   <th>
    $\Delta_{2}{(\%)}$
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <th>
    $f_{1}$
   </th>
   <td>
    $1.2446$
   </td>
   <td>
    $0.0$
   </td>
   <td>
    $1.3106$
   </td>
   <td>
    $0$
   </td>
   <td>
    $5.3$
   </td>
  </tr>
  <tr>
   <th>
    $f_{2}$
   </th>
   <td>
    $1.2439$
   </td>
   <td>
    $- 0.4295$
   </td>
   <td>
    $1.5664$
   </td>
   <td>
    $34.5$
   </td>
   <td>
    $25.9$
   </td>
  </tr>
  <tr>
   <th>
    $f_{3}$
   </th>
   <td>
    $1.2430$
   </td>
   <td>
    $- 0.4300$
   </td>
   <td>
    $1.5580$
   </td>
   <td>
    $34.6$
   </td>
   <td>
    $25.3$
   </td>
  </tr>
  <tr>
   <th>
    $f_{4}$
   </th>
   <td>
    $1.2441$
   </td>
   <td>
    $- 0.4296$
   </td>
   <td>
    $1.5592$
   </td>
   <td>
    $35.0$
   </td>
   <td>
    $26.2$
   </td>
  </tr>
 </tbody>
</table>

Table 2. Comparative analysis of estimations by the IM and QM.
<table>
 <thead>
  <tr>
   <th>
   </th>
   <th>
    ${\langle\sigma_{11}\rangle}_{i(0)}{(\mathbf{0})}$
   </th>
   <th>
    ${\langle\sigma_{11}\rangle}_{i(7)}{(\mathbf{0})}$
   </th>
   <th>
    ${\langle\sigma_{11}\rangle}_{i(20)}{(\mathbf{0})}$
   </th>
   <th>
    ${\langle\sigma_{11}^{QM}\rangle}_{i}{(\mathbf{0})}$
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <th>
    $f_{1}$
   </th>
   <td>
    $0.0$
   </td>
   <td>
    $0.0$
   </td>
   <td>
    $0.0$
   </td>
   <td>
    $0.0$
   </td>
  </tr>
  <tr>
   <th>
    $f_{2}$
   </th>
   <td>
    $0.0$
   </td>
   <td>
    $- 0.4295$
   </td>
   <td>
    $- 0.4419$
   </td>
   <td>
    $- 0.4426$
   </td>
  </tr>
  <tr>
   <th>
    $f_{3}$
   </th>
   <td>
    $0.0$
   </td>
   <td>
    $- 0.4300$
   </td>
   <td>
    $- 0.4433$
   </td>
   <td>
    $- 0.4440$
   </td>
  </tr>
  <tr>
   <th>
    $f_{4}$
   </th>
   <td>
    $0.0$
   </td>
   <td>
    $- 0.4296$
   </td>
   <td>
    $- 0.4429$
   </td>
   <td>
    $- 0.4427$
   </td>
  </tr>
 </tbody>
</table>

Table 3. Comparative analysis of different methods and the functions $g{(r)}$ (9.1)–(9.2).
<table>
 <thead>
  <tr>
   <th>
    Method
   </th>
   <th>
    $g{(r)}$
   </th>
   <th>
    $\max{\langle\sigma_{11}\rangle}_{i(0)}$
   </th>
   <th>
    ${\langle\sigma_{11}\rangle}_{i(7)}{(\mathbf{0})}$
   </th>
   <th>
    $\max{\langle\sigma_{11}\rangle}_{i(7)}$
   </th>
   <th>
    $\Delta_{1}{(\%)}$
   </th>
   <th>
    $\Delta_{2}{(\%)}$
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <th>
    MEFM
   </th>
   <th>
    (9.1)
   </th>
   <td>
    $1.2146$
   </td>
   <td>
    $- 0.3564$
   </td>
   <td>
    $1.4938$
   </td>
   <td>
    $29.3$
   </td>
   <td>
    $23.0$
   </td>
  </tr>
  <tr>
   <th>
    MEFM
   </th>
   <th>
    (9.2)
   </th>
   <td>
    $1.2439$
   </td>
   <td>
    $- 0.4295$
   </td>
   <td>
    $1.5664$
   </td>
   <td>
    $34.5$
   </td>
   <td>
    $25.9$
   </td>
  </tr>
  <tr>
   <th>
    MT
   </th>
   <th>
    (9.1)
   </th>
   <td>
    $1.1247$
   </td>
   <td>
    $- 0.2311$
   </td>
   <td>
    $1.2955$
   </td>
   <td>
    $20.5$
   </td>
   <td>
    $15.2$
   </td>
  </tr>
  <tr>
   <th>
    MT
   </th>
   <th>
    (9.2)
   </th>
   <td>
    $1.1247$
   </td>
   <td>
    $- 0.2412$
   </td>
   <td>
    $1.3163$
   </td>
   <td>
    $21.4$
   </td>
   <td>
    $17.0$
   </td>
  </tr>
  <tr>
   <th>
    PM
   </th>
   <th>
    (9.1)
   </th>
   <td>
    $1.1631$
   </td>
   <td>
    $- 0.1542$
   </td>
   <td>
    $1.2830$
   </td>
   <td>
    $13.3$
   </td>
   <td>
    $10.3$
   </td>
  </tr>
  <tr>
   <th>
    PM
   </th>
   <th>
    (9.2)
   </th>
   <td>
    $1.1336$
   </td>
   <td>
    $- 0.1995$
   </td>
   <td>
    $1.2976$
   </td>
   <td>
    $17.6$
   </td>
   <td>
    $14.7$
   </td>
  </tr>
 </tbody>
</table>

in the fibers ${\langle\sigma_{11}\rangle}_{i}{(x_{1})}$ for the function $f_{2}$ are presented in Figure 4. The first-order approximation of the IM leads to the normalized stresses ${{\langle\sigma_{11}\rangle}_{i(1)}{(\mathbf{0})}}/{\max{\langle\sigma_{11}\rangle}_{i(0)}{(x_{1})}} = 0.2134$ provided, according to Equations (8.1)–(8.3), by the derivatives $f_{2}^{(m)}$, $m = {4,6,\ldots}$ (if they exist), whereas the second-order approximation of the FTM leads to the degenerate result $\mathcal{Y}_{(2)}{(\nabla)}{\langle\sigma\rangle}_{i}{(\mathbf{0})} = \mathbf{0}$ (non-local effect is absent at the point $\mathbf{x} = \mathbf{0}$).

In Table 3 only the function $f_{2}$ is analyzed in the framework of the iteration scheme. The comparative analysis of the MEFM (5.3), MT method (7.10), and the perturbation method (PM) (7.4) for the different radial correlation functions (9.1) and (9.2) ($c = 0.6$) is presented. As can be seen, the MEFM is most sensitive to the choice of radial distribution function and leads to the maximum non-local effects predicted. It is interesting that the non-local response, in contrast to the local one, estimated by the MT method, depends on the radial distribution function $g{(r)}$. The differences of estimations for the different average methods analyzed in Table 3 by the quadrature method (5.10) and 7th iteration are usually not over 3 percent as in Table 1.

Thus, in some specific numerical examples the feasibility, efficiency, and accuracy of all three numerical methods of solution of non-local integral equation (4.10), QM, IM, and FTM, were emphatically demonstrated. Their qualitative comparative analyses are presented in the next section.

## 10.CONCLUDING REMARKS

Let us discuss the main scheme as well as the short sketch of limitations and of possible generalization and application of the methods proposed.

The obtained relations depend on the values associated with the mean distance between inclusions, and do not depend on the other characteristic size, i.e. the mean inclusion diameter. This fact may be explained by the initial use of the hypothesis **H1** dealing with the homogeneity of the field $\overline{\boldsymbol{\sigma}}(\mathbf{x})$ inside each inclusion. In the case of a variable representation of $\overline{\boldsymbol{\sigma}}(\mathbf{x})$ ( $\mathbf{x} \in v_{i}$ ), for instance in polynomial form, the mean size of the inclusions will be contained in the non-local dependence of microstresses on the average stress $\langle\boldsymbol{\sigma}\rangle(\mathbf{x})$. Such an improvement based on the abandonment from the hypothesis **H1** was schematically considered in [6] where the comparison with available analytical solution for semi-infinite periodic collinear row of cracks is presented, and there are the numerous references confirming the estimation of accuracy of the hypotheses **H1** and **H2** in connection with relevant experimental data and analytical solutions for the linear and nonlinear problems for statistically homogeneous and periodic structure 2D and 3D composites.

It should be mentioned that QM, IM, and FTM have a series of advantages and disadvantages, and it is crucial for the analyst to be aware of their range of application. The QM causes no problems of accuracy but can become less effective in the CPU time sense than the IM if the number of variables increases. The IM (3.24) has two known drawbacks. First, the Neumann series ensures the existence of solutions to integral equations of the second kind only for sufficiently small kernels (5.9), and secondly, in general, it cannot be summed in closed form. Of course, Equation (5.7) can be solved directly by the quadrature method even if the condition (5.9) is not valid. However, strongly inhomogeneous problems may lead to much larger numbers of quadrature points, making iteration potentially worthwhile. Moreover, increasing the problem dimensionality (from 2D to 3D) raises the number of nodes to the dimensional power and the situation changes radically. As shown, only a few iterations of Equation (3.24) are necessary; these iterations prove very much faster than a direct inversion of the operator $\mathbf{I}-\mathcal{K}$ by the quadrature method. In so doing, the condition (5.9) is fulfilled in all examples considered for the highly filled composites with an infinite contrast in moduli between the phases.

The reduction of integral operators to the differential ones allows an understanding of drawbacks of the FTM. The first one is that for obtaining an $m$th-order differential operator, it is necessary that $\mathcal{E}^{a v}$ belongs to $C^{m}(w)$. In so doing, the IM providing the accuracy of differential operator of an infinite order does not have even continuity of $\mathcal{E}^{a v}$ since integration is a smoothing operation and the right-hand side integral (4.10) is likely to be a rather smooth function even when $\mathcal{E}^{a v}(\mathbf{x})$ is very jagged. But even the $m$th approximation of the IM contains the differential operators of infinite orders (although not all, see Equation (8.2)) that are lost in the FTM. The question of the convenience of using one method over another is solved also in favor of the IM because, in the FTM, it is necessary to calculate the cumbersome tensors $\mathcal{Y}_{(m)}$ (5.20) and $\mathcal{B}_{m}$ (5.27). The completeness of the estimation increases dramatically with $m$, while in the IM it is enough to estimate a single tensor $\mathbf{K}(\mathbf{x}_{i}-\mathbf{x}_{q})$ (4.14) and consecutively to apply the recursion scheme (5.7) and (5.8), the completeness of which does not depend on the iteration number. Thus, the advantage of the FTM comprised of obtaining analytical explicit relations dwindles in light of the disadvantages mentioned above such as a requirement of smoothness of $\mathcal{E}^{a v} \in C^{m}(w)$ and an intricacy of analytical calcula-

tions. Nevertheless, there is some advantage of the FTM naturally connected with the explicit representation of the differential operators when tensors $\mathcal{Y}_{(m)}$ (5.20) and $\mathcal{B}_{m}$ (5.27) need to be estimated just one time and can be used for forthcoming analysis of any $\mathcal{E}^{a v} \in C^{m}(w)$ smooth enough. (However, of course, there remains the valid question, of which order of differential operator (5.20), (5.26) provides *a priori* prescribed accuracy of the solution of Equation (4.10) and how it is connected with the smoothness of the function $\mathcal{E}^{a v}$ .)

We indicated only mathematical and computational difficulties in the use of the FTM which can be solved, at least in principle, at the cost of great efforts if the analytical solution is necessary. However, it should be mentioned that there is an extremely important class of micromechanical problems for statistically inhomogeneous media (such as functionally graded and clustered materials – see for references [6, 58, 59]), analysis of which by the FTM is questionable. The breakdown of the assumption of statistical homogeneity leads to the inequality $\mathbf{Y}(\mathbf{x}_{i}) \neq$ const. Then the average stresses $\langle\boldsymbol{\sigma}\rangle(\mathbf{x}) \neq$ const. and $\mathcal{K} \mathcal{E} \neq \mathbf{0}$ even at the homogeneous boundary conditions either (2.4) or (2.5). However, even this simplest case of homogeneous boundary conditions leads to a fundamental prohibitive obstacle against the use of the FTM. Indeed, the inhomogeneity $\langle\boldsymbol{\sigma}\rangle(\mathbf{x}) \neq$ const. yields the inequality $\mathcal{K}(\mathbf{x}_{i}, \mathbf{x}_{q}) \neq \mathcal{K}(\mathbf{x}_{i}-\mathbf{x}_{q})$ and, therefore, the linear differential operator (5.12) has variable coefficients. Then the jump from Equations (5.12), (5.18) to Equations (5.14), (5.20), respectively, based on the properties of the Fourier transform (5.15), is difficult, and an applicability of the FTM is questionable. In so doing, the use for statistically inhomogeneous media of the IM inserts requires slight modification of the scheme presented (4.8)–(5.8) (see, for example, [31]) for application of the iteration method for research of periodic graded composites). However, the analysis of these problems is beyond the scope of the current study and will be considered in forthcoming publications by the authors.

Acknowledgment. This work was supported by the AFRL/MLBC.

**NOTE**

1. It is known that for 2D problems the plane-strain state is only possible for material symmetry no lower than orthotropic (see, for example, [41]) which will be assumed hereafter in the 2D case.

**REFERENCES**

[1] Christensen, R. M.: *Mechanics of Composite Materials*, Wiley Interscience, New York, 1979.

[2] Willis, J. R.: Variational and related methods for the overall properties of composites. *Advances in Applied Mechanics*, 21, 1–78 (1981).

[3] Mura, T.: *Micromechanics of Defects in Solids*, Martinus Nijhoff, Dordrecht, 1987.

[4] Nemat-Nasser, S., and Hori, M.: *Micromechanics: Overall Properties of Heterogeneous Materials*, Elsevier, Amsterdam, 1993.

[5] Markov, K. Z.: Elementary micromechanics of heterogeneous media. *Heterogeneous Media: Modelling and Simulation*, pp. 1–168, eds., K. Z. Markov and L. Preziosi, Birkhäuser, Boston, 1999.

[6] Kanaun, S. K., and Levin, V. M.: Effective field method in mechanics of matrix composite materials. *Advances in Mathematical Modeling of Composite Materials*, pp. 1–58, ed., K. Z. Markov, World Scientific, Singapore, 1994.

[7] Buryachenko, V. A.: Multiparticle effective field and related methods in micromechanics of composite materials. *Appl. Mech. Reviews*, 54, 1–47 (2001).

[8] Torquato, S.: *Random Heterogeneous Materials: Microstructure and Macroscopic Properties*, Springer-Verlag, Berlin, 2002.

432 V. A. BURYACHENKO and N. J. PAGANO

[9] Carol, I., and Bazant, Z. P.: Damage and plasticity in microplane theory. *Int. J. Solids Structures*, 34, 3807–3835 (1997).

[10] Fleck, N. A., and Hutchinson, J. W.: Strain gradient plasticity. *Advances in Applied Mechanics*, Vol. 33, pp. 295–361, eds., J.W. Hutchinson & T.Y. Wu, Academic, New York, 1997.

[11] Eringen, A. C.: *Micromedium Field Theories I. Foundations and Solids*, Springer, Berlin, 1999.

[12] Aifantis E. C.: Gradient deformation models at nano, micro, and macro scales. *ASME. J Eng. Mater. Technol.*, 121, 189–202 (1999).

[13] Ganghoffer, J. F., and de Borst R.: A new framework in non-local mechanics. *Int. J. Eng. Sci.*, 38, 453–486 (2000).

[14] Picu, R. C.: On the functional form of non-local elasticity kernels. *J. Mech. Phys. Solids*, 50, 1923–1939 (2002).

[15] Kröner E.: Elasticity theory of materials with long range cohesive forces. *Int. J. Solid Structures*, 3, 731–342 (1967).

[16] Kröner E.: *Statistical Continuum Mechanics*, Springer-Verlag, Wien, 1972.

[17] Kunin, I. A., and Vaisman, A. M.: On problems of the non-local theory of elasticity. *Fundamental Aspects of Disloca- tion Theory*, pp. 747–757, eds., J. Simmons, R. de Wit & R. Bullough, US National Bureau of Standards, Washington DC, 1970.

[18] Eringen, A. C., and Edelen, D. G. B.: On non-local elasticity. *Int. J. Eng. Sci.*, 10, 233–243 (1972).

[19] Beran, M. J., and McCoy, J. J.: Mean field variations in a statistical sample of heterogeneous linearly elastic solids. *Int. J. Solid Structures*, 6, 1035–1054 (1970).

[20] Levin, V. M.: The relation between mathematical expectations of stress and strain tensors in elastic microheteroge- neous media. *Priklad. Mat. i Mekh.*, 35, 744–750 (1971) (in Russian). Engl. Transl. *J. Appl. Math. Mech.*, 35, 694–701 (1971).

[21] Lax, M.: Multiple scattering of waves II. The effective fields dense systems. *Phys. Rev.*, 85, 621–629 (1952).

[22] Khoroshun, L. P.: On a mathematical model for inhomogeneous deformation of composites. *Priklad. Mekh.*, 32(5), 22–29 (1996) (in Russian). Engl. Transl. *Int. Appl. Mech.*, 32, 341–348 (1996).

[23] Drugan, W. J., and Willis, J. R.: A micromechanics-based non-local constitutive equation and estimates of represen- tative volume elements for elastic composites. *J. Mech. Phys. Solids*, 44, 497–524 (1996).

[24] Drugan, W. J.: Micromechanics-based variational estimations for a higher-order non-local constitutive equation and optimal choice of effective moduli for elastic composites. *J. Mech. Phys. Solids*, 48, 1359–1387 (2000).

[25] Luciano, R., and Willis, J. R.: Bounds on non-local effective relations for random composites loaded by configuration- dependent body force. *J. Mech. Phys. Solids*, 48, 1827–1849 (2000).

[26] Luciano, R., and Willis, J. R.: Non-local effective relations for fibre-reinforced composites loaded by configuration- dependent body forces. *J. Mech. Phys. Solids*, 49, 2705–2717 (2001).

[27] Willis, J. R.: The non-local influence of density variations in a composite. *Int. J. Solids Structures*, 21, 805–817 (1985).

[28] Buryachenko, V. A., and Lipanov, A. M.: Thermoelastic stress concentration at ellipsoidal inclusions in matrix composites in the region of strongly varying external stress and temperature fields. *Deformation and Fracture of Structural-Inhomogeneous Materials*, pp. 12–19, eds., O. B. Naimark & S. E. Evlampieva, AN SSSR, Sverdlovsk, 1992 (in Russian).

[29] Buryachenko, V. A.: Some non-local effects in graded random structure matrix composites. *Mech. Res. Commun.*, 25, 117–122 (1998).

[30] Buryachenko, V. A. and Rammerstorfer, F. G.: Micromechanics and non-local effects in graded random structure matrix composites. *IUTAM Symp. on Transformation Problems in Composite and Active Materials*, pp. 197–206, eds., Y.A. Bahei-El-Din & G. J. Dvorak, Kluwer Academic, Dordrecht, 1998.

[31] Buryachenko, V. A.: Effective thermoelastic properties of graded doubly periodic particulate composites in varying external stress fields. *Int. J. Solids Structures*, 36, 3861–3885 (1999).

[32] Bakhvalov, N. G., and Panasenko, G.: *Homogenization: Averaging Processes in Periodic Media*, Kluwer, Dordrecht, 1989.

[33] Kalamkarov, A. L., and Kolpakov, A. G.: *Analysis, Design and Optimization of Composite Shells*, Wiley, New York, 1997.

[34] Gambin, B., and Kröner, E.: Higher-order terms in the homogenized stress–strain relation of periodic elastic media. *Phys. Status Solidi*, b151, 513–530 (1989).

[35] Boutin, C.: Microstructural effects in elastic composites. *Int. J. Solids Structures*, 33, 1023–1051 (1996).

[36] Forest, S., and Sab, K.: Cosserat overall modeling of heterogeneous materials. *Mech. Res. Commun.*, 25, 449–454 (1998).

[37] Smyshlyaev, V. P., and Cherednichenko, K. D.: A rigorous derivation of strain gradient effects in the overall behavior of periodic heterogeneous media. *J. Mech. Phys. Solids*, 48, 1325–1357, (2000).

NON-LOCAL MODELS OF RANDOM STRUCTURE COMPOSITES 433

[38] Bouyge, F., Jasiuk, I., and Ostoja-Starzewski, M.: A micromechanically based couple-stress model of an elastic two-phase composite. *Int. J. Solids Structures*, 38, 1721–1735 (2001).

[39] Pagano, N.J., and Yuan, F. G.: Significance of effective modulus theory (homogenization), in composite laminate mechanics. *Compos. Sci. Technol.*, 60, 2471–2488 (2000).

[40] Vanin, G. A.: Plane strain gradient theory of multilevel media. *Mekh. Tverdogo Tela* (3), 5–15 (1996) (in Russian). Engl. Transl. *Mech. Solids*, 31(3), 2–11 (1996).

[41] Lekhnitskii, A. G.: *Theory of Elasticity of an Anisotropic Elastic Body*, Holder Day, San Francisco, 1963.

[42] Kröner, E.: Bounds for effective moduli of disordered materials, *J. Mech. Phys. Solids*, 25, 137–155 (1977).

[43] Eshelby, J. D.: The determination of the elastic field of an ellipsoidal inclusion, and related problems. *Proc. R. Soc. London*, A 241, 376–396 (1957).

[44] Dvorak, G. J., and Benveniste, Y.: On transformation strains and uniform fields in multiphase elastic media. *Proc. R. Soc. London*, A 437, 291–310 (1992).

[45] Lee, J., and Mal, A.: A volume integral equation technique for multiple inclusion and crack interaction problems. *J. Appl. Mech. – Trans. ASME*, 64, 23–31 (1997).

[46] Lee, J., and Mal, A.: Characterization of matrix damage in metal matrix composites under transverse loads. *Compu- tational Mech.*, 21, 339–346 (1998).

[47] Delves, L. M., and Mohamed, J. L.: *Computational Methods for Integral Equations*, Cambridge University Press, Cambridge, 1985.

[48] Varga, R. S.: *Matrix Iterative Analysis*, Springer, Berlin, 2000.

[49] Pipkin, A. C.: *A Course on Integral Equations*, Springer, New York, 1991.

[50] Shilov, G. E.: *Generalized Functions and Partial Differential Equations*, Gordon & Breach, New York, 1968.

[51] Treves, F.: *Introduction to Pseudodifferential and Fourier Integral Operators*, Vol. 1, Plenum Press, New York, 1980.

[52] Zuiker, J. R., and Dvorak, G. J.: The effective properties of functionally graded composites–I. Extension of the Mori–Tanaka method to linearly varying fields. *Compos. Eng.*, 4, 19–35 (1994).

[53] Smyshlyaev, V. P., and Fleck, N. A.: The role of strain gradients in the grain size effects for polycrystals. *J. Mech. Phys. Solids*, 44, 465–495 (1996).

[54] Torquato, S., and Lado, F.: Improved bounds on the effective elastic moduli of random arrays of cylinders. *ASME. J. Appl. Mech.*, 59, 1–6 (1992).

[55] Hansen, J. P., and McDonald, I. R.: *Theory of Simple Liquids*, Academic, New York, 1986.

[56] Buryachenko, V. A., Pagano, N. J., Kim, R. Y., and Spowart, J. E.: Quantitative description of random microstructures of composites and their effective elastic moduli. *Int. J. Solids Structures*, 40, in press (2003).

[57] Lee, J. A. and Mykkanen, D. L.: Metal and Polymer Matrix Composites. Noyes Data Corporation, New York, 1987.

[58] Zuiker, J. R.: Functionally graded materials: Choice of micromechanics model and limitations in property variation. *Compos. Eng.*, 5, 807–819 (1995).

[59] Reiter, T., Dvorak, G. J., and Tvergard, V.: Micromechanical models for graded composite materials. *J. Mech. Phys. Solids*, 45, 1281–1302 (1997).