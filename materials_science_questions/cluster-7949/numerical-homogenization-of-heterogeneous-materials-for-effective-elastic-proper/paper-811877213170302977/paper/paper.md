# An adaptive strategy for the control of modeling error in two-dimensional atomic-to-continuum coupling simulations

Serge Prudhomme $^{a,*}$, Ludovic Chamoin $^{a}$, Hachmi Ben Dhia $^{b}$, Paul T. Bauman $^{a}$

$^{a}$ Institute for Computational Engineering and Sciences, The University of Texas at Austin, 1 University Station C0200, Austin, TX 78712, USA
$^{b}$ Laboratoire de Mécanique des Sols, Structures et Matériaux, Ecole Centrale de Paris, 1 rue des Vignes, 92290 Châtenay-Malabry, France

---

## ARTICLE INFO

**Article history:**
Received 11 June 2008
Received in revised form 23 September 2008
Accepted 31 December 2008
Available online 8 January 2009

In honor of J. Tinsley Oden's 70th Birthday

**Keywords:**
Atomic-to-continuum coupling methods
Arlequin framework
Goal-oriented error estimation and adaptivity
A posteriori estimation

---

## ABSTRACT

An adaptive approach to control modeling error in multiscale simulations that involve molecular and continuum scales is presented. The modeling error is defined as the difference between the solution of a reference particle model, which is considered intractable in practice, and the solution of a manageable multiscale surrogate problem based on the Arlequin framework. The method relies on computable error estimates of the modeling error in specific outputs of interest that require the solution of an adjoint problem. These are the so-called goal-oriented error estimates, which are used to adapt the surrogate model, i.e. to find the optimal configuration of the overlap region between the molecular and continuum models, in order to deliver approximations of quantities of interest within some preset accuracy. Performance of the adaptive strategy is demonstrated on two-dimensional numerical examples.

© 2009 Elsevier B.V. All rights reserved.

---

## 1. Introduction

Multiscale methods are playing an important role in the current development of simulation-based engineering. They enable the coupling between several models and several scales so that accurate outputs of complex problems can be simulated from manageable computational models. In the context of nanoscale simulations, the multiscale approach is vital: it enables the simplification of a reference particle model which usually generates an intractable number of degrees of freedom for practical applications, see e.g. [12,16,13,14]. In this work, a coarser scale continuum model is used far from regions of the particle domain of interest, while the particle model is preserved in the local critical regions. The coupling between the two scales may be achieved using various techniques, such as the handshake method [11], the bridging-scale method [27], or the bridging-domain method [28]. Another well-known method for multiscale computations of particle systems is the quasi-continuum method [25] even though it shall be considered as a coarsening method rather than one which explicitly couples two different models. In this paper, we focus on a volume coupling method based on the Arlequin framework [7-9]. Arlequin coupling was recently extended and analyzed for the coupling between a particle model and a continuum model in [3,4,10]. Other bridging methods which are related to the notion of blending of concurrent models in an overlap region have been recently proposed in [2].

The multiscale model only constitutes a surrogate model of the initial particle model. The error in target outputs due to this surrogate approximation must therefore be estimated and controlled. Estimation of the error arising from the simplification of a reference model is referred to as *modeling error estimation*. The subject has been introduced in recent years and was initially devoted to estimating global modeling error [17]. Since then, extensions to error estimates in specific quantities of interest, based on the work of [6], have been proposed in [19,20]. The general process of adapting the surrogate model in order to decrease the modeling error in specific quantities of interest is referred to as the *Goals Algorithms*. Goals algorithms have been applied to various multiscale problems such as those dealing with heterogeneous materials [18,26] or wave propagation in elastic materials [22]. A general review can be found in [21]. For the particular case of atomic-to-continuum coupling methods, modeling error estimates and adaptive procedures have been derived in [23,1] for the quasi-continuum method.

In this paper, we extend the Goals algorithm to multiscale simulations using an atomic-to-continuum coupling method based on the Arlequin approach. The methods are presented on two-dimensional model problems in which either harmonic or Lennard-Jones potentials are considered for the atomic model and plane stress linear elasticity is selected for the continuum model. We

---

* Corresponding author.
E-mail addresses: serge@ices.utexas.edu (S. Prudhomme), ludo@ices.utexas.edu (L. Chamoin), hachmi.ben-dhia@ecp.fr (H.B. Dhia), pbauman@ices.utexas.edu (P.T. Bauman).

0045-7825/$ - see front matter © 2009 Elsevier B.V. All rights reserved.
doi:10.1016/j.cma.2008.12.026

demonstrate the performance of the methodology on a simple square domain for which we can easily study the influence of the parameters of the coupling method and evaluate features of the Goals algorithm. We also present a simplified problem motivated by the quasi-static simulation of a crack.

The paper is organized as follows. After this introduction, we present in Section 2 the model problem and introduce basic notation. We show in Section 3 how to identify, using virtual experiments, the material parameters of a continuum model that is compatible with the particle model. We describe in Section 4 the construction of the surrogate problem that couples the particle and continuum models following the Arlequin framework. We present in Section 5 the procedure to estimate the modeling error in predefined quantities of interest and the strategy to adapt the surrogate model. We illustrate in Section 6 the theoretical results by numerical experiments on two-dimensional problems and conclude in Section 7.

## 2. Model problem and notations

We consider a system of $n$ particles on a lattice that describes a two-dimensional structure at the atomic scale (see Fig. 1). Particle $i$, for $i=1,\dots,n$, is initially at position $\mathbf{x}_i \in \mathbb{R}^2$ in the reference configuration. When the structure is subjected to a prescribed external loading, each particle $i$ occupies a new location $\mathbf{r}_i = \mathbf{x}_i + \mathbf{y}_i$ defined in terms of the displacement vector $\mathbf{y}_i \in \mathbb{R}^2$. We assume here that the loading is represented by pointwise forces $\mathbf{f}_i$ acting on each particle $i$, for $i=1,\dots,n$ and that Dirichlet boundary conditions are prescribed for a non-empty set $\mathscr{N}_d$ of particles, i.e. $\mathbf{y}_i = \mathbf{g}_i$, $\forall i \in \mathscr{N}_d$. In the following, we denote the global displacement vector with respect to all particles by $\mathbf{y} = [\mathbf{y}_1,\mathbf{y}_2,\dots,\mathbf{y}_n] \in \mathbb{R}^{2n}$.

We suppose that the particles are connected by bonds that are modeled using inter-atomic potentials. We will only consider pairwise interactions and denote the potential between particles $i$ and $j$ by $V_{ij}$. Potentials to be considered here are:

(i) the harmonic potential:
$$
V_{ij}(\mathbf{y}_i,\mathbf{y}_j) = \frac{1}{2} k_{ij} \left(r_{ij} - r_{ij}^0\right)^2, \tag{1}
$$

(ii) the Lennard-Jones "6-12" potential:
$$
V_{ij}(\mathbf{y}_i,\mathbf{y}_j) = 4\epsilon_{ij} \left[ \left(\frac{\sigma_{ij}}{r_{ij}}\right)^{12} - \left(\frac{\sigma_{ij}}{r_{ij}}\right)^6 \right], \tag{2}
$$

where $r_{ij} = |\mathbf{r}_j - \mathbf{r}_i| = |\mathbf{y}_j - \mathbf{y}_i + \mathbf{x}_j - \mathbf{x}_i|$ denotes the current bond length and $k_{ij}, r_{ij}^0, \epsilon_{ij}, \sigma_{ij}$ are bond parameters. We will assume that the latter are known exactly in this study. Here $r_{ij} = r_{ij}^0$ when $\mathbf{y}_i = \mathbf{y}_j = \mathbf{0}$. The strain energy of the particle system is then given by:

$$
E_d(\mathbf{y}) = \frac{1}{2} \sum_{i=1}^n \sum_{\substack{j=1 \\ j \neq i}}^n V_{ij}(\mathbf{y}_i,\mathbf{y}_j) \approx \frac{1}{2} \sum_{i=1}^n \sum_{j \in \mathscr{B}_i}^n V_{ij}(\mathbf{y}_i,\mathbf{y}_j) = \widetilde{E}_d(\mathbf{y}), \tag{3}
$$

where $\mathscr{B}_i$ is the subset of particles that lie within a given cut-off distance from particle $i$ (i.e. long range interactions are neglected here). Let the potential energy of the system be:

$$
E_P(\mathbf{y}) = \frac{1}{2} \sum_{i=1}^n \sum_{j \in \mathscr{B}_i}^n V_{ij}(\mathbf{y}_i,\mathbf{y}_j) - \sum_{i=1}^n \mathbf{f}_i \cdot \mathbf{y}_i = \widetilde{E}_d(\mathbf{y}) - \sum_{i=1}^n \mathbf{f}_i \cdot \mathbf{y}_i.
$$

The equilibrium state of the system is obtained by minimizing the potential energy over admissible displacement fields, i.e. the model problem reads:

$$
\boxed{\text{Find } \mathbf{y} \in \mathbf{U} \text{ such that } E_P(\mathbf{y}) = \min_{\mathbf{z} \in \mathbf{U}} E_P(\mathbf{z})}, \tag{4}
$$

where the space of trial displacements is given by:

$$
\mathbf{U} = \{\mathbf{y} \in \mathbb{R}^{2n} ; \mathbf{y}_i = \mathbf{g}_i \quad \forall i \in \mathscr{N}_d\}. \tag{5}
$$

The problem can also be written in variational form as:

$$
\boxed{\text{Find } \mathbf{y} \in \mathbf{U} \text{ such that } B(\mathbf{y};\mathbf{z}) = F(\mathbf{z}) \quad \forall \mathbf{z} \in \mathbf{V}}, \tag{6}
$$

where $\mathbf{V}$ is the space of test functions defined by

$$
\mathbf{V} = \{\mathbf{z} \in \mathbb{R}^{2n} ; \mathbf{z}_i = \mathbf{0} \quad \forall i \in \mathscr{N}_d\} \tag{7}
$$

and $B(\cdot;\cdot)$ and $F(\cdot)$ are, respectively, a form linear with respect to its second argument defined on $\mathbf{U} \times \mathbf{V}$ and linear form on $\mathbf{V}$:

$$
\begin{aligned}
B(\mathbf{y};\mathbf{z}) &= \sum_{i=1}^n \frac{\partial \widetilde{E}_d}{\partial \mathbf{y}_i}(\mathbf{y}) \cdot \mathbf{z}_i, \\
F(\mathbf{z}) &= \sum_{i=1}^n \mathbf{f}_i \cdot \mathbf{z}_i.
\end{aligned} \tag{8}
$$

The nonlinear problem (6) constitutes our base problem which, in practical cases, is intractable with current computing resources due to the large number of degrees of freedom involved. We will assume that solutions to (6) exist, but are not necessarily unique. We emphasize here that the primary goal of the simulation is not in general to predict the global solution of the particle system, but to compute specific features of the solution, the so-called quantities of interest. A quantity of interest is in general a local measure, either critical for design purposes or relevant to the understanding of physical phenomena. It can be represented as a (possibly nonlinear) functional $Q(\mathbf{y})$ of the solution $\mathbf{y}$. Ideally, the particle model would be preserved only locally, i.e. in a critical region of the structure, and should include a neighborhood of the region over which the quantity of interest is defined; it generally corresponds to a zone where the solution displays large variations (loading region for instance). In the remainder of the structure, we would employ a coarser-scale

![](./images/811877213170302977_1.jpg)

Fig. 1. Lattice model for molecular simulations in the reference configuration.

continuum model. Construction of the continuum model as well as the coupling between the two scales are discussed below.

### 3. Continuum model and calibration of parameters

In this section, we shall construct a continuum model that is capable of accurately capturing the large scale phenomena of the lattice network. This continuum model will be used in the region away from the critical region of the structure and will be coupled to the molecular model. One requirement is that the selected model be equivalent to the particle model in the homogenization sense. In this work, the continuum model is based on plane stress linear elasticity so that the constitutive relation is defined by Hooke's law:
$$
\sigma_{i j}=C_{i j k l} \epsilon_{k l}, \quad i, j, k, l=1,2,
\tag{9}
$$
where $\boldsymbol{\sigma}$ is the stress tensor, $\boldsymbol{\epsilon}$ is the linearized strain tensor, $\boldsymbol{\epsilon}=\frac{1}{2}\left(\nabla \mathbf{u}+\nabla^{T} \mathbf{u}\right), \mathbf{u}$ is the continuum displacement field, and $C_{i j k l}$ define the material parameters to be identified. The calibration is performed using virtual experiments on Representative Volume Elements (RVEs). A RVE is a piece of material whose dimension is iteratively determined in such a way that a consistent homogenized medium is obtained, that is, such that the material parameters do not vary as the size is increased. In the following, we will use samples of materials that are larger than the effective representative volume element in order to avoid boundary effects (see Figs. 2 and 3, for an example why it is important to take samples larger than the RVE).

Suppose for example that the material satisfies cubical isotropy. The model of choice in this case would be to consider the following strain-stress relationship:
$$
\left(\begin{array}{l}
\epsilon_{11} \\
\epsilon_{22} \\
\epsilon_{12}
\end{array}\right)=\left[\begin{array}{ccc}
\frac{1}{E} & -\frac{v}{E} & 0 \\
-\frac{v}{E} & \frac{1}{E} & 0 \\
0 & 0 & \frac{1}{2 G}
\end{array}\right]\left(\begin{array}{l}
\sigma_{11} \\
\sigma_{22} \\
\sigma_{12}
\end{array}\right),
\tag{10}
$$
where the Young's modulus $E$, the shear modulus $G$, and Poisson coefficient $v$ need to be identified. Other models will be given in Section 6. The calibration process for the continuum model consists of an inverse problem with the following steps:

1. We select a sequence of lattices $\mathscr{L}_{i}$ (RVEs) made of $n_{i} \times n_{i}$ particles with $n_{i+1}>n_{i}, i=0,1,2, \ldots$, and we set $i=0$.
2. We apply various cases of kinematic boundary conditions (for uni-axial tension, bi-axial tension, shear deformation) to the particles on the boundaries of the element (see examples in Fig. 3). Actually, we consider a sequence of loading increments and solve for the quasi-static displacements of the particles.
3. We compute the energy $\widetilde{E}_{d}(\mathbf{y})$ on the RVE for each case of boundary conditions and each loading increment.
4. We suppose that the energy densities obtained from the continuum and particle models are identical so that $W(\mathbf{u})=\widetilde{E}_{d}(\mathbf{y}) / V_{i}$ on the RVE, where $\mathbf{u}$ is the displacement field one would obtain from the continuum model if equivalent boundary conditions were prescribed, and $V_{i}$ is the initial volume of the RVE. From the constitutive relation (10), we then fit the values of the parameters $(E, G, v)$ using the least squares method.
5. We increment $i$ by one and repeat steps 2-5 until the parameters become independent of $n_{i}$.

Let us notice that the choice of the continuum model is of course problem dependent (see e.g. [4] where classical Neo-Hookean and Mooney-Rivlin models are used to calibrate a continuum model with a three-dimensional lattice model of a polymeric material).

Let us now give an example to illustrate our approach for the calibration of the parameters. We suppose that the material of interest can be modeled by a lattice consisting of uniform harmonic bonds with parameters defined as in Section 6.1. We perform a shear test to a lattice sample by applying kinematic boundary conditions. The dimensions of the lattice sample and RVE are similar to those in Fig. 2. The vertical displacements on the left and right faces of the lattice sample are constrained to be equal to $\pm U$ where $U$ is increased from 0 to 0.2 , using increments $\Delta U=0.01$. At each iteration, we measure the energy of the RVE and the corresponding macroscopic shear force on the RVE. We are then able to identify the parameter $G$ of the continuum model. Fig. 4 gives the evolution of the shear force and coefficient $G$ with respect to the macroscopic strain of the RVE. We observe that the linear elasticity assumption is valid only if the strain remains below $8 \%$.

![](./images/811877213170302977_2.jpg)

Fig. 2. Lattice sample and representative volume element (RVE).

### 4. Construction of the surrogate problem

We consider the following scenario. The material is supposed to be homogeneous in the sense that the bonding parameters are chosen uniform everywhere in the lattice. The structure is subjected to loadings such that, (i) small deformations are observed in a significant part of the lattice, in which the lattice model can be replaced by a linearly elastic model, (ii) large deformations are locally present, due for example to the action of a large forcing term or to the presence of a geometrical singularity, that require the use of the lattice model in a local region. The objectives are then twofold: (i) to develop a surrogate model that involves coupling the continuum and particle models in order to provide approximations of the full particle model, (ii) to develop an adaptive approach that can automatically determine the optimal size of the domain for the particle model so as to predict quantities of interest within preset tolerances. The first objective is accomplished by the Arlequin method and is presented in the subsections below. The second objective is the subject of Section 5 where we extend the goal-oriented error estimation and adaptation approach to the Arlequin setting.

#### 4.1. Continuous formulation of the coupling method

Following our work in [3] (see also [4,10]), we briefly present here the Arlequin framework in the case of two-dimensional applications. We suppose that the lattice occupies the domain $\Omega \in \mathbb{R}^{2}$, with boundary $\partial \Omega$, and that the lattice model is selected in a subregion $\Omega_{m} \subset \Omega$, while the continuum model is chosen in $\Omega_{c} \subset \Omega$ such that $\Omega=\Omega_{c} \cup \Omega_{m}$ (see Fig. 5). Finally, the intersection of $\Omega_{c}$ and $\Omega_{m}$ is nonempty and corresponds to what we refer to as the

![](./images/811877213170302977_3.jpg)
![](./images/811877213170302977_4.jpg)

Fig. 3. Experiments for calibration of the parameters of the continuum model: (left) the sample is loaded in tension, (right) the sample is loaded in shear.

![](./images/811877213170302977_5.jpg)
![](./images/811877213170302977_6.jpg)

Fig. 4. (Left) Evolution of shear force with respect to the macroscopic strain applied to the RVE; the solid curve shows the force calculated with respect to the calibrated linear elasticity model while the curve with circles depicts the evolution of the force as computed with the particle model. (Right) Evolution of modulus G with respect to the macroscopic strain applied to the RVE.

![](./images/811877213170302977_7.jpg)

Fig. 5. Configuration of the Arlequin surrogate problems considered here.

overlap region, i.e. $\Omega_{o}=\Omega_{c} \cap \Omega_{m}$. The domain $\Omega_{m}$ now contains $m$ particles, with $m \ll n$. For simplicity, but without loss of generality, we assume that Dirichlet boundary conditions are prescribed only on part of the boundary $\Gamma_{D} \subset \partial \Omega \cap \partial \Omega_{c}$, that is, they are transmitted to the structure through the continuum model only, i.e.
$$
\mathbf{u}=\mathbf{g} \quad \text { on } \Gamma_{D}. \quad(11)
$$

On the remainder of the "continuum boundary", $\Gamma_{N}=(\partial \Omega \cap \partial \Omega_{c}) \backslash \Gamma_{D}$, traction boundary conditions are applied:
$$
\boldsymbol{\sigma} \cdot \mathbf{n}=\mathbf{t} \quad \text { on } \Gamma_{N}, \quad(12)
$$
where $\mathbf{n}$ denotes the outward unit normal to $\Gamma_{N}$.

One idea of the Arlequin methodology is to partition the energies of the coupled system as follows:
$$
\begin{aligned}
& E_{c}(\mathbf{u})=\frac{1}{2} \int_{\Omega_{c}} \alpha_{c}(\mathbf{x}) \boldsymbol{\sigma}(\mathbf{u}): \boldsymbol{\epsilon}(\mathbf{u}) d x, \\
& E_{m}(\mathbf{w})=\frac{1}{2} \sum_{i=1}^{m} \sum_{j \in \mathscr{B}_{i}} \alpha_{i j} V_{i j}\left(\mathbf{w}_{i}, \mathbf{w}_{j}\right),
\end{aligned}\quad(13)
$$
where the weighting coefficients $\alpha_{c}$ and $\alpha_{i j}$ are required to satisfy:
$$
\begin{aligned}
& \alpha_{c}(\mathbf{x})= \begin{cases}1 & \forall \mathbf{x} \in \Omega_{c} \backslash \Omega_{o}, \\
0 & \forall \mathbf{x} \in \Omega_{m} \backslash \Omega_{o},\end{cases} \\
& \alpha_{i j}=\frac{1}{|S|} \int_{S}\left(1-\alpha_{c}(\mathbf{x})\right) d x,
\end{aligned}\quad(14)
$$
where $S$ corresponds to the region adjacent to the bond associated with potential $V_{i j}$ as shown in Fig. 6. Note that the choice of $S$ is motivated by the fact that each cell of the lattice (a square with particles at the vertices) defines a volume whose equivalent continuum energy, assumed uniform, involves the energy of the bonds associ-

![](./images/811877213170302977_8.jpg)

Fig. 6. Examples of regions S used to compute the weighting coefficients $\alpha_{ij}$ with respect to a bond associated with potential $V_{ij}$. The bond is shown by a thick line while the region S is represented as the shaded domain. The top row of figures shows cases of nearest neighbor interactions while the bottom row considers next-nearest neighbor interactions.

ated with that cell. It naturally follows that S is selected as the region defined by the union of the cells that share that bond. In the overlap region, the coefficient $\varkappa_{c}$ can be chosen constant, piecewise constant, linear, bilinear, or in terms of cubic polynomials, etc. Moreover, $\mathbf{u}$ and $\mathbf{w}$ are required to match in some appropriate measure on the overlap $\Omega_{o}$. However, in order for $\mathbf{u}$ and $\mathbf{w}$ to be comparable, we introduce the linear interpolation operator $\Pi$ that maps the discrete displacement vector $\mathbf{w}$ into a displacement field $\Pi \mathbf{w}$ in $\mathbf{H}^{1}(\Omega_{o})$. We define the trilinear form $b(\cdot,\cdot,\cdot)$ as the coupling term such that

$$
b(\boldsymbol{\mu}, \mathbf{u}, \mathbf{w})=0 \quad \forall \boldsymbol{\mu} \in \mathbf{H}^{1}\left(\Omega_{o}\right). \tag{15}
$$

The Arlequin problem consists then in finding a minimum $(\mathbf{u}, \mathbf{w}) \in \mathbf{U}_{c} \times \mathbf{V}_{m}$ of the partitioned total energy that satisfies the constraint (15), i.e.

$$
(\mathbf{u}, \mathbf{w})=\underset{\substack{(\mathbf{v}, \mathbf{z}) \in \mathbf{U}_{c} \times \mathbf{V}_{m} \\ b(\boldsymbol{\mu}, \mathbf{v}, \mathbf{z})=0 \quad \forall \boldsymbol{\mu} \in \mathbf{M}}}{\operatorname{argmin}}\left[E_{c}(\mathbf{v})-\int_{\Gamma_{N}} \mathbf{t} \cdot \mathbf{v} d s+E_{m}(\mathbf{z})-\sum_{i=1}^{m} \mathbf{f}_{i} \cdot \mathbf{z}_{i}\right], \tag{16}
$$

where the vector spaces are defined as

$$
\begin{aligned}
& \mathbf{U}_{c}=\left\{\mathbf{v} \in \mathbf{H}^{1}\left(\Omega_{c}\right) ; \mathbf{v}=\mathbf{g} \text { on } \Gamma_{D}\right\}, \\
& \mathbf{V}_{c}=\left\{\mathbf{v} \in \mathbf{H}^{1}\left(\Omega_{c}\right) ; \mathbf{v}=\mathbf{0} \text { on } \Gamma_{D}\right\}, \\
& \mathbf{V}_{m}=\mathbb{R}^{2 m}, \\
& \mathbf{M}=\mathbf{H}^{1}\left(\Omega_{o}\right).
\end{aligned} \tag{17}
$$

Introducing the forms:

$$
a_{c}(\mathbf{u}, \mathbf{v})=\int_{\Omega_{c}} \varkappa_{c}(\mathbf{x}) \boldsymbol{\sigma}(\mathbf{u}): \boldsymbol{\epsilon}(\mathbf{v}) d x,
$$

$$
a_{m}(\mathbf{w} ; \mathbf{z})=\sum_{i=1}^{m} \frac{\partial E_{m}}{\partial \mathbf{w}_{i}}(\mathbf{w}) \cdot \mathbf{z}_{i},
$$

$$
a((\mathbf{u}, \mathbf{w}) ;(\mathbf{v}, \mathbf{z}))=a_{c}(\mathbf{u}, \mathbf{v})+a_{m}(\mathbf{w} ; \mathbf{z})
$$

and

$$
l_{c}(\mathbf{v})=\int_{\Gamma_{N}} \mathbf{t} \cdot \mathbf{v} d s,
$$

$$
l_{m}(\mathbf{z})=\sum_{i=1}^{m} \mathbf{f}_{i} \cdot \mathbf{z}_{i},
$$

$$
l(\mathbf{v}, \mathbf{z})=l_{c}(\mathbf{v})+l_{m}(\mathbf{z}),
$$

the weak formulation of Problem (16) then reads:

Find $(\mathbf{u}, \mathbf{w}, \boldsymbol{\lambda}) \in \mathbf{U}_{c} \times \mathbf{V}_{m} \times \mathbf{M}$ such that :
$$
\begin{aligned}
& a((\mathbf{u}, \mathbf{w}) ;(\mathbf{v}, \mathbf{z}))+b(\boldsymbol{\lambda}, \mathbf{v}, \mathbf{z})=l(\mathbf{v}, \mathbf{z}) \quad \forall(\mathbf{v}, \mathbf{z}) \in \mathbf{V}_{c} \times \mathbf{V}_{m}, \\
& b(\boldsymbol{\mu}, \mathbf{u}, \mathbf{w})=0 \quad \forall \boldsymbol{\mu} \in \mathbf{M}
\end{aligned}
$$

or, in more compact form:

$$
\begin{aligned}
& \text { Find }(\mathbf{u}, \mathbf{w}, \boldsymbol{\lambda}) \in \mathbf{U}_{c} \times \mathbf{V}_{m} \times \mathbf{M} \text { such that : } \\
& \quad B_{0}((\mathbf{u}, \mathbf{w}, \boldsymbol{\lambda}) ;(\mathbf{v}, \mathbf{z}, \boldsymbol{\mu}))=F_{0}(\mathbf{v}, \mathbf{z}, \boldsymbol{\mu}) \quad \forall(\mathbf{v}, \mathbf{z}, \boldsymbol{\mu}) \in \mathbf{V}_{c} \times \mathbf{V}_{m} \times \mathbf{M},
\end{aligned} \tag{18}
$$

where:
$$
\begin{aligned}
& B_{0}((\mathbf{u}, \mathbf{w}, \boldsymbol{\lambda}) ;(\mathbf{v}, \mathbf{z}, \boldsymbol{\mu}))=a((\mathbf{u}, \mathbf{w}) ;(\mathbf{v}, \mathbf{z}))+b(\boldsymbol{\lambda}, \mathbf{v}, \mathbf{z})+b(\boldsymbol{\mu}, \mathbf{u}, \mathbf{w}), \\
& F_{0}(\mathbf{v}, \mathbf{z}, \boldsymbol{\mu})=l(\mathbf{v}, \mathbf{z}).
\end{aligned}
$$

It is clear that Problem (18) is a surrogate problem of our reference problem (6) in the sense that a solution $(\mathbf{u}, \mathbf{w})$ of the former is only an approximation of the solution $\mathbf{y}$ of the latter. Note that Problem (18) is still a nonlinear problem (the classical Newton method will be used to solve this nonlinear problem). The size of the representative volume element associated with the determination of the continuum model is the scale that dictates the size of the overlap region. In a few words, the length, when crossing the overlap from the continuum to the particle region, should naturally be larger than a characteristic size of the RVE. The definition of the coupling term is not unique (see e.g. [3]). Here we choose the following inner product (equivalent to the $\mathbf{H}^{1}(\Omega_{o})$ inner product):

$$
b(\boldsymbol{\mu}, \mathbf{v}, \mathbf{z})=\int_{\Omega_{o}} \beta_{0} \boldsymbol{\mu} \cdot(\mathbf{v}-\Pi \mathbf{z})+\beta_{1} \nabla \boldsymbol{\mu}:(\nabla \mathbf{u}-\nabla \Pi \mathbf{z}) d x, \tag{19}
$$

where $\beta_{0}$ and $\beta_{1}$ are two user-defined scaling parameters. We have shown in [3] that the linear counterpart of Problem (18) for one-dimensional applications is a well-posed problem when $\beta_{0} \geqslant 0$ and $\beta_{1}>0$. This coupling term is appropriate for mono-atomic structures. More complex coupling terms, based on averaging, are needed in the case of heterogeneous distributions of bonds. When next-nearest neighbor interactions are included in the model, one observes non-physical spurious effects at the boundaries of the overlap region $\Omega_{o}$ that are similar to the so-called ghost force effects in the quasi-continuum method [12]. A special treatment of these ghost forces has been implemented and will be described in a forthcoming article.

### 4.2. Finite element approximation

We now approximate Problem (18) using the finite element method. We first introduce finite element subsets $\mathbf{U}_{c}^{h}, \mathbf{V}_{c}^{h}$, and $\mathbf{M}^{h}$ of $\mathbf{U}_{c}, \mathbf{V}_{c}$, and $\mathbf{M}$, respectively. The finite element approximation of (18) is given by the following problem:

$$
\begin{aligned}
& \text { Find }\left(\mathbf{u}_{h}, \mathbf{w}_{h}, \boldsymbol{\lambda}_{h}\right) \in \mathbf{U}_{c}^{h} \times \mathbf{V}_{m} \times \mathbf{M}^{h} \text { such that : } \\
& \quad B_{0}\left(\left(\mathbf{u}_{h}, \mathbf{w}_{h}, \boldsymbol{\lambda}_{h}\right) ;(\mathbf{v}, \mathbf{z}, \boldsymbol{\mu})\right)=F_{0}(\mathbf{v}, \mathbf{z}, \boldsymbol{\mu}) \quad \forall(\mathbf{v}, \mathbf{z}, \boldsymbol{\mu}) \in \mathbf{V}_{c}^{h} \times \mathbf{V}_{m} \times \mathbf{M}^{h}.
\end{aligned} \tag{20}
$$

Note that we use the notation $\mathbf{w}_{h} \in \mathbf{V}_{m}$, despite the fact that $\mathbf{V}_{m}$ is already a finite-dimensional space, to emphasize that $\mathbf{w}_{h}$ is different from $\mathbf{w}$ since it depends on $\mathbf{u}_{h}$ and $\boldsymbol{\lambda}_{h}$.

The mesh size $h_\lambda$, associated with $\mathbf{M}_h$, needs to be larger either than the characteristic mesh size $h_u$ associated with $\mathbf{U}_c^h$ or than the distance $r_{ij}^0$ between particles over the overlap region $\Omega_o$, in order to ensure well-posedness of the discrete problem. Moreover, in the present formulation of the coupling term, the mesh size corresponding to the Lagrange multipliers $\lambda_h$ cannot be smaller than the size $\varepsilon$ of the representative volume element used to derive the continuum model, or the continuum solution would "lock" into the fine scale solution. We will consider in the numerical experiments examples where $h_\lambda = h_u \geqslant \varepsilon \geqslant r_{ij}^0$.

Finally, we will assume that the discretization error $(\mathbf{u}, \mathbf{w}, \lambda)-(\mathbf{u}_h, \mathbf{w}_h, \lambda_h)$ will be negligible with respect to the modeling error defined as the difference between $\mathbf{y} \in \mathbf{V}$ and an "extension" $\mathbf{y}_0 \in \mathbf{V}$ of $(\mathbf{u}, \mathbf{w}, \lambda)$. In other words, we will only propose estimates of the modeling error in what follows.

## 5. Error estimator and adaptive strategy
We present here an approach for error estimation and adaptation for the Arlequin problem (18) based on the Goals algorithm [18,26,20,21]; error estimates are derived with respect to quantities of interest $Q(\mathbf{y})$ of the solution $\mathbf{y}$ to (6) and an adaptive scheme is used to drive the position of the overlap region $\Omega_o$ so as to reduce the error in the quantity of interest. A similar approach is also presented in [5] for the case of three-dimensional models of polymer networks. We have shown in [24] based on computational experiments for a one-dimensional problem that the error in the quantity of interest naturally decreases as the molecular region in the coupling method is enlarged.

### 5.1. Quantities of interest
In this work, we suppose that we are interested in quantities of interest that characterize the response at the small scales. We will consider the displacement $\mathbf{y}_p$ of one particle $p$ so that:
$$Q(\mathbf{y}) = \mathbf{s} \cdot \mathbf{y}_p, \tag{21}$$
where $\mathbf{s}$ is a unit vector indicating the direction in which the displacement is to be measured, or, the bond stretching between two particles $p$ and $q$, so that:
$$Q(\mathbf{y}) = \frac{r_{pq} - r_{pq}^0}{r_{pq}^0}, \tag{22}$$
where $r_{pq}$ and $r_{pq}^0$ are the stretched and equilibrium bond lengths between the two particles. Note that the first functional is linear while the second is a nonlinear functional of $\mathbf{y} \in \mathbf{U}$.

### 5.2. The adjoint problem and error representation
We briefly recall the theory for goal-oriented error estimation as described in [20,21] and applied to the present situation. Suppose that $\mathbf{y} \in \mathbf{U}$ is the solution to (6) and that $\mathbf{y}_0 \in \mathbf{U}$ is a given approximation of $\mathbf{y}$. We then introduce the adjoint (or dual) problem of (6) as:

Find $\mathbf{p} \in \mathbf{V}$ such that $\quad B'(\mathbf{y};\mathbf{v},\mathbf{p}) = Q'(\mathbf{y};\mathbf{v}) \quad \forall \mathbf{v} \in \mathbf{V}, \tag{23}$

where
$$
\begin{aligned}
B'(\mathbf{y};\mathbf{v},\mathbf{p}) &= \lim_{\theta \to 0} \theta^{-1}[B(\mathbf{y}+\theta \mathbf{v};\mathbf{p})-B(\mathbf{y};\mathbf{p})] = \sum_{i=1}^n \sum_{j=1}^n \mathbf{v}_i \cdot \frac{\partial^2 \widetilde{E}}{\partial \mathbf{y}_i \partial \mathbf{y}_j}(\mathbf{y}) \cdot \mathbf{p}_j, \\
Q'(\mathbf{y};\mathbf{v}) &= \lim_{\theta \to 0} \theta^{-1}[Q(\mathbf{y}+\theta \mathbf{v})-Q(\mathbf{y})].
\end{aligned} \tag{24}
$$

This problem is linear but unsolvable as the solution $\mathbf{y}$ is not available. We shall thus consider the following adjoint problem:

$$\text{Find } \mathbf{p}_0 \in \mathbf{V} \text{ such that } \quad B'(\mathbf{y}_0;\mathbf{v},\mathbf{p}_0) = Q'(\mathbf{y}_0;\mathbf{v}) \quad \forall \mathbf{v} \in \mathbf{V}. \tag{25}$$

In that case, the error $\mathscr{E} = Q(\mathbf{y}) - Q(\mathbf{y}_0)$ can be represented as (see [20]):
$$\mathscr{E} = Q(\mathbf{y}) - Q(\mathbf{y}_0) = \mathscr{R}(\mathbf{y}_0;\mathbf{p}_0) + \mathscr{R}(\mathbf{y}_0;\mathbf{p}-\mathbf{p}_0) + \Delta, \tag{26}$$

where $\mathscr{R}(\cdot;\cdot)$ is the residual functional,
$$\mathscr{R}(\mathbf{y}_0;\mathbf{v}) = F(\mathbf{v}) - B(\mathbf{y}_0;\mathbf{v}) \tag{27}$$

and $\Delta$ is a remainder term of higher order in the errors $\mathbf{e}_0 = \mathbf{y} - \mathbf{y}_0$ and $\boldsymbol{\varepsilon}_0 = \mathbf{p} - \mathbf{p}_0$. If $B$ and $Q$ are thrice differentiable, the remainder $\Delta$ can be explicitly written as:
$$
\begin{aligned}
\Delta &= \frac{1}{2} \int_0^1 B''(\mathbf{y}_0 + s\mathbf{e}_0;\mathbf{e}_0, \mathbf{e}_0, \mathbf{p}_0 + s\boldsymbol{\varepsilon}_0) - Q''(\mathbf{y}_0 + s\mathbf{e}_0;\mathbf{e}_0, \mathbf{e}_0)ds \\
&+ \frac{1}{2} \int_0^1 \left(Q'''(\mathbf{y}_0 + s\mathbf{e}_0;\mathbf{e}_0, \mathbf{e}_0, \mathbf{e}_0) - 3B''(\mathbf{y}_0 + s\mathbf{e}_0;\mathbf{e}_0, \mathbf{e}_0, \boldsymbol{\varepsilon}_0)\right. \\
&\left. - B'''(\mathbf{y}_0 + s\mathbf{e}_0;\mathbf{e}_0, \mathbf{e}_0, \mathbf{e}_0, \mathbf{p}_0 + s\boldsymbol{\varepsilon}_0)\right)(s-1)s \, ds.
\end{aligned} \tag{28}
$$

However, the adjoint problem (25) and residual (27) are both defined with respect to the full fine scale model and once again would be too expensive to evaluate in order to estimate the error $\mathscr{E}$. Approximations of the dual problem and the residual for the Arlequin framework are described in the next section.

### 5.3. Error estimator
In this section, we assume that we have computed the solution $(\mathbf{u}, \mathbf{w}, \lambda)$ (actually $(\mathbf{u}_h, \mathbf{w}_h, \lambda_h)$) to the Arlequin problem (18). If we consider mono-atomic materials and suppose that the structure undergoes only small deformations, it is then reasonable to assume that the Cauchy-Born hypothesis [15] holds. In that case, the discrete solution $\mathbf{w} \in \mathbf{V}_m$ can be extended to $\mathbf{U}$ by using the continuum displacement field $\mathbf{u} \in \mathbf{U}_c$. Indeed, we can construct the new displacement vector $\mathbf{y}_0 \in \mathbf{U}$ such that:
$$\mathbf{y}_{0,i} = \begin{cases}
\mathbf{w}_i & \text{if } i=1,\dots,m, \\
\mathbf{u}(\mathbf{x}_i) & \text{if } \mathbf{x}_i \in \Omega_c \setminus \Omega_o,
\end{cases} \tag{29}$$

Other constructions could be imagined, in particular in the overlap region, in which we could use a linear combination of the solutions $\mathbf{u}$ and $\mathbf{w}$. Nevertheless, none of these approaches necessarily produce the best approximation of $\mathbf{y}$ as soon as the Cauchy-Born rule fails to hold, for instance, in the case of lattices with heterogeneous bonds.

Since $\mathbf{y}_0$ would be too expensive to utilize as is, the main idea here is to solve an adjoint problem over an enriched Arlequin problem in which the molecular model is considered in a larger domain than that used to compute $(\mathbf{u}, \mathbf{w}, \lambda)$, as shown in Fig. 7. All variables and symbols $q$, related to this new configuration, are labeled $\widetilde{q}$. The new spaces associated with this new Arlequin problem are $\widetilde{\mathbf{U}}_c$, $\widetilde{\mathbf{V}}_c$, $\widetilde{\mathbf{V}}_m$, and $\widetilde{\mathbf{M}}$, and we easily observe that $\widetilde{\Omega}_c \subset \Omega_c$ and $\widetilde{\Omega}_m \subset \widetilde{\Omega}_m$. We first "extend" the solution $(\mathbf{u}, \mathbf{w}, \lambda)$ to the space $\widetilde{\mathbf{U}}_c \times \widetilde{\mathbf{V}}_m \times \widetilde{\mathbf{M}}$ as follows:
$$
\begin{aligned}
\tilde{\mathbf{u}}(\mathbf{x}) &= \mathbf{u}(\mathbf{x}) \quad \forall \mathbf{x} \in \widetilde{\Omega}_c, \\
\tilde{\mathbf{w}}_i &= \begin{cases}
\mathbf{w}_i & \text{if } i=1,\dots,m, \\
\mathbf{u}(\mathbf{x}_i) & \text{if } \mathbf{x}_i \in \Omega_c \setminus \Omega_o,
\end{cases} \\
\tilde{\lambda}(\mathbf{x}) &= \mathbf{0} \quad \forall \mathbf{x} \in \widetilde{\Omega}_o.
\end{aligned} \tag{30}
$$

The Lagrange multiplier $\tilde{\lambda}$ is simply set to zero as it is not directly used in what follows.

Given the approximation $(\tilde{\mathbf{u}}, \tilde{\mathbf{w}}, \tilde{\lambda}) \in \widetilde{\mathbf{U}}_c \times \widetilde{\mathbf{V}}_m \times \widetilde{\mathbf{M}}$, reconstructed from $(\mathbf{u}, \mathbf{w}, \lambda)$, we can set up a new adjoint problem which consists in finding $(\tilde{\mathbf{p}}_u, \tilde{\mathbf{p}}_w, \tilde{\mathbf{p}}_\lambda) \in \widetilde{\mathbf{U}}_c \times \widetilde{\mathbf{V}}_m \times \widetilde{\mathbf{M}}$ such that

![](./images/811877213170302977_9.jpg)

Fig. 7. Approximation of the adjoint problem by using a larger molecular region in the Arlequin framework as compared to Fig. 5.

$$
\begin{aligned}
& B_{0}^{\prime}\left((\tilde{\mathbf{u}}, \tilde{\mathbf{w}}, \tilde{\lambda}) ;(\mathbf{v}, \mathbf{z}, \boldsymbol{\mu}),\left(\tilde{\mathbf{p}}_{u}, \tilde{\mathbf{p}}_{w}, \tilde{\mathbf{p}}_{\lambda}\right)\right) \\
& \quad=Q_{0}^{\prime}((\tilde{\mathbf{u}}, \tilde{\mathbf{w}}, \tilde{\lambda}) ;(\mathbf{v}, \mathbf{z}, \boldsymbol{\mu})) \quad \forall(\mathbf{v}, \mathbf{z}, \boldsymbol{\mu}) \in \tilde{\mathbf{V}}_{c} \times \tilde{\mathbf{V}}_{m} \times \tilde{\mathbf{M}}.
\end{aligned}
\tag{31}
$$

It suffices then to construct a fine scale approximation $\tilde{\mathbf{p}}_{0} \in \mathbf{V}$ from $(\tilde{\mathbf{p}}_{u}, \tilde{\mathbf{p}}_{w})$ such as:

$$
\tilde{\mathbf{p}}_{0, i}= \begin{cases}\tilde{\mathbf{p}}_{w, i} & \text { if } i=1, \ldots, \tilde{m}, \\ \tilde{\mathbf{p}}_{u}\left(\mathbf{x}_{i}\right) & \text { if } \mathbf{x}_{i} \in \widetilde{\Omega}_{c} \backslash \widetilde{\Omega}_{o},\end{cases}
\tag{32}
$$

that can be used to define the error estimate:

$$
\eta_{\mathrm{est}}=\mathscr{R}\left(\mathbf{y}_{0} ; \tilde{\mathbf{p}}_{0}\right) \approx \mathscr{E}=Q(\mathbf{y})-Q\left(\mathbf{y}_{0}\right).
\tag{33}
$$

Alternatively, in order to reduce the cost of estimating the residual with respect to the fine scale problem, we can also estimate the error as:

$$
\tilde{\eta}_{\mathrm{est}}=\tilde{\mathscr{R}}\left(\mathbf{y}_{0} ; \tilde{\mathbf{p}}_{0}\right) \approx \mathscr{E}=Q(\mathbf{y})-Q\left(\mathbf{y}_{0}\right),
\tag{34}
$$

where the reduced residual $\tilde{\mathscr{R}}$ is defined on a subdomain $\widetilde{\Omega}$ such that $\Omega_{m} \subset \widetilde{\Omega} \subset \Omega$. The estimate $\tilde{\eta}_{\text {est }}$ will not be evaluated in the present study.

### 5.4. Adaptive algorithm
The general objective of goal-oriented adaptivity is to construct a procedure that controls the error $\mathscr{E}=Q(\mathbf{y})-Q\left(\mathbf{y}_{0}\right)$ within some preset error tolerance $\gamma_{\text {tol }}$. This is generally achieved by generating a sequence of surrogate problems with solutions $(\mathbf{y}_{0}^{k}, \tilde{\mathbf{p}}_{0}^{k})$ so that for some integer $k_{0}$, the modeling error satisfies:

$$
\left|Q(\mathbf{y})-Q\left(\mathbf{y}_{0}^{k_{0}}\right)\right| \leqslant \gamma_{\text {tol }}.
\tag{35}
$$

At each iteration, the goal is to reduce the global quantity $\mathscr{R}(\mathbf{y}_{0} ; \tilde{\mathbf{p}}_{0})$ by locally enriching the surrogate model, i.e. by locally switching on the particle model in the subregions where the continuum model is not accurate enough. This is possible by observing that the residual term $\eta_{\mathrm{est}}=\mathscr{R}(\mathbf{y}_{0} ; \tilde{\mathbf{p}}_{0})$ is defined globally over the whole domain and can be decomposed into local contributions $\eta_{c}$ defined over predefined subdomains of $\Omega$. Indeed,

$$
\mathscr{R}\left(\mathbf{y}_{0} ; \tilde{\mathbf{p}}_{0}\right)=F\left(\tilde{\mathbf{p}}_{0}\right)-B\left(\mathbf{y}_{0} ; \tilde{\mathbf{p}}_{0}\right),
$$

so that from the definition of $B(\cdot ; \cdot)$ and $F(\cdot)$ we have:

$$
\mathscr{R}\left(\mathbf{y}_{0} ; \tilde{\mathbf{p}}_{0}\right)=\sum_{i=1}^{n}\left(\mathbf{f}_{i}-\frac{\partial \widetilde{E}}{\partial \mathbf{y}_{i}}\left(\mathbf{y}_{0}\right)\right) \cdot \tilde{\mathbf{p}}_{0, i}=\sum_{i=1}^{n} \eta_{i}.
$$

Summing the particle contributions $\eta_{i}$ into contributions over subdomains, we can therefore obtain local contributions $\eta_{c}$. It seems natural to choose as subdomains the elements of the finite element mesh used to discretize the continuum model. Finally, prescribing a user-defined parameter $\gamma_{a}$ such that $0<\gamma_{a}<1$, the subdomains with contributions $\eta_{c}$ can be switched from the continuum model to the particle model whenever

$$
\eta_{c}>\gamma_{a} \max _{c} \eta_{c}.
$$

The proposed algorithm for adaptation of the surrogate model is shown in Fig. 8. In the experiments shown below, we will set $\gamma_{a}=0.3$.

## 6. Numerical results
### 6.1. Equilibrium of a square lattice
The lattice we shall consider in this example consists of $51 \times 51$ particles with lattice spacing $\ell=1$ (see Fig. 9). Note that parameters in the following are provided without units as specific dimensions are irrelevant for the purpose of this study. A unit force, applied in a succession of 10 increments of magnitude $\Delta F=0.1$, is applied at the center point $P$ of the lattice. The particles along the boundaries are kept fixed. Bonds between particles are modeled here in terms of harmonic potentials and include nearest and next-nearest neighbor interactions as shown in Fig. 10. The parameters for the potentials are chosen as $k_{1}=10$ for the nearest neighbor interactions, $k_{1 d}=5$ for the nearest neighbor interactions along diagonals of the lattice, and $k_{2}=2$ for the next-nearest

![](./images/811877213170302977_10.jpg)

Fig. 8. Adaptive algorithm for goal-oriented error estimation and control of modeling error.

![](./images/811877213170302977_11.jpg)

Fig. 9. Square lattice example.

![](./images/811877213170302977_12.jpg)

Fig. 10. Particle interactions with respect to centered particle: blue particles are the nearest neighbors for which $k_{1}=10$, green particles are the nearest neighbors along diagonals and the interaction is modeled with $k_{1d}=5$, while red particles are the next-nearest neighbors with $k_{2}=2$. (For interpretation of the references in color in this figure legend, the reader is referred to the web version of this article.)

neighbor interactions. The corresponding equilibrium lengths are, respectively, set to $\ell_{1}=\ell, \ell_{1d}=\sqrt{2}\ell$, and $\ell_{2}=2\ell$, so that the lattice is in equilibrium when no forces are applied.

For the continuum model, it is reasonable to consider here plane stress linear elasticity model with the constitutive relation given in (10). The calibration process as described in Section 3 provides:
$$
\begin{aligned}
& E=13.65, \\
& G=4.14, \\
& v=0.32.
\end{aligned} \tag{36}
$$

For the Arlequin problem, the particle domain consists of $13 \times 13$ particles surrounding the particle $P$. The overlap region $\Omega_{o}$ is two bonds thick in every direction (since the size of the RVE is $2 \times 2$) and we choose a linear weight function $\alpha_{c}$ in $\Omega_{o}$. We show in Fig. 11 the Arlequin problem in the reference configuration and in the deformed configuration when submitted to the loading force $F$.

We suppose that we are interested in the horizontal displacement of the middle particle $P$ on which the loading is applied. The quantity of interest can then be written as:
$$
Q(\mathbf{y})=\boldsymbol{s} \cdot \mathbf{y}_{P}, \tag{37}
$$
where $\boldsymbol{s}$ is the unit vector $(1,0)$. We now investigate two cases in order to study the influence of neighbor interactions.

(i) **Nearest neighbors only.** In this case, we keep $k_{1}=10$ and $k_{1d}=5$, but set $k_{2}=0$. The exact and approximate values of the quantity of interest are then obtained as $Q(\mathbf{y})=0.1017$ and $Q(\mathbf{y}_{0})=0.0941$, a relative error of $7\%$. In order to estimate the higher order term $\Delta$ in (26), we compute the adjoint solution $\mathbf{p} \in \mathbf{V}$. We then have
$$
\begin{aligned}
\Delta & =Q(\mathbf{y})-Q(\mathbf{y}_{0})-\mathscr{R}(\mathbf{y}_{0};\mathbf{p})=0.1017-0.0941-0.0076 \\
& =-7.71.10^{-8}
\end{aligned}
$$
from which we conclude that the higher-order term $\Delta$ is very small (less than $0.001\%$ of the error). We show the residual term in Fig. 12. We actually plot the averaged contribution from four neighboring particles over the area defined by these particles.

(ii) **Nearest and next-nearest neighbors.** We repeat the same experiments as above with $k_{2}=2$. We then obtain $Q(\mathbf{y})=0.0785,\ \ Q(\mathbf{y}_{0})=0.0700$ (error of $11\%$), and $\mathscr{R}(\mathbf{y}_{0};\mathbf{p})=0.0085$, so that
$$
\Delta=0.0785-0.0700-0.0085=-7.59.10^{-7},
$$
which means that $\Delta$ is equal to $0.009\%$ of the actual error. Although small again, we can conclude that longer-range interactions generate additional errors in the particle region. The corresponding residual term is shown in Fig. 13.

![](./images/811877213170302977_13.jpg)

Fig. 11. Arlequin problem in reference (left) and deformed (right) configurations.

![](./images/811877213170302977_14.jpg)

Fig. 12. Residual computed in the case of nearest neighbor interactions only.

![](./images/811877213170302977_15.jpg)

Fig. 13. Residual computed in the case of nearest and next-nearest neighbor interactions.

### 6.1.1. Influence of the coupling parameters
In these experiments, we aim at investigating the influence of the mesh size and thickness of the overlap region. We consider nearest neighbor interactions only and address two cases: in the first case, the mesh size corresponds to the equilibrium distance between particles and the width of the overlap region is twice as large as before. In the second case, the overlap thickness is the same as in the first case, but the mesh used for the finite element solution and discretization of the Lagrange multiplier is twice coarser. The two configurations are shown in Fig. 14. We obtain the following results:

<table>
<thead>
<tr>
<th></th>
<th>$Q(\mathbf{y})$</th>
<th>$Q(\mathbf{y}_{0})$</th>
<th>Rel. error</th>
<th>$\mathscr{R}(\mathbf{y}_{0};\tilde{\mathbf{p}}_{0})$</th>
<th>$\Delta$</th>
<th>$\Delta/(Q(\mathbf{y})-Q(\mathbf{y}_{0}))$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Case 1</td>
<td>0.1017</td>
<td>0.0948</td>
<td>7%</td>
<td>0.0069</td>
<td>$-7.15.10^{-8}$</td>
<td>0.001%</td>
</tr>
<tr>
<td>Case 2</td>
<td>0.1017</td>
<td>0.0957</td>
<td>6%</td>
<td>0.0060</td>
<td>$-2.71.10^{-8}$</td>
<td>0.001%</td>
</tr>
</tbody>
</table>

We observe that the size and discretization of the coupling region plays a role in the accuracy of the quantity of interest.

### 6.1.2. Influence of the adjoint approximation on the error estimator
We study here the influence of the choice of the domains $\tilde{\Omega}_{c}$ and $\tilde{\Omega}_{m}$ on the error estimator $\eta_{\text{est}}$ (33). We consider nearest neighbor interactions only. We construct three Arlequin problems for the adjoint approximation, as shown in Fig. 15, compute the approximate extensions $\tilde{\mathbf{p}}_{0}$ from the solution $(\tilde{\mathbf{p}}_{u},\tilde{\mathbf{p}}_{w},\tilde{\mathbf{p}}_{\lambda})$, evaluate the estimates $\eta_{\text{est}}$ for the three cases, and compare the results to the estimate $\mathscr{R}(\mathbf{y}_{0};\mathbf{p}_{0})$, where $\mathbf{p}_{0}$ is obtained from (25). The results are:

<table>
<thead>
<tr>
<th>$Q(\mathbf{y})-Q(\mathbf{y}_{0})$</th>
<th>$\mathscr{R}(\mathbf{y}_{0};\mathbf{p}_{0})$</th>
<th>$\eta_{\text{est.1}}$</th>
<th>$\eta_{\text{est.2}}$</th>
<th>$\eta_{\text{est.3}}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>0.0076</td>
<td>0.0076</td>
<td>0.0073</td>
<td>0.0066</td>
<td>0.0052</td>
</tr>
</tbody>
</table>

The effectivity indices, defined as $|\eta_{\text{est}}/(Q(\mathbf{y})-Q(\mathbf{y}_{0}))|$, are 0.96, 0.87, 0.68 for the three cases, respectively. All three values remain fairly accurate, so that, from now on, we will only use the approximation obtained by adding one layer of particles in $\tilde{\Omega}_{m}$ around $\Omega_{m}$. This choice should be reasonable as long as the quantities of interest remain local.

### 6.1.3. Influence of the particle domain on the modeling error
We described in [24] some computational experiments performed on a one-dimensional problem showing that the modeling error in the quantity of interest decreases as the particle domain is enlarged. We consider here two configurations of the Arlequin problem and show the residual contributions for these two cases in Fig. 16. We first note that the contributions are large along the

![](./images/811877213170302977_16.jpg)

Fig. 14. Influence of mesh size and overlap width. (Left) Overlap width is increased. (Right) Coarser mesh is used in overlap region.

![](./images/811877213170302977_17.jpg)

Fig. 15. Discretizations used to solve the adjoint problem by the Arlequin approach.

![](./images/811877213170302977_18.jpg)

Fig. 16. Distribution of the residual contributions for two configurations of the Arlequin problem.

overlap region as expected. For the smaller particle region, the relative error in the quantity of interest amounts to 4%, while for the larger particle region, the relative error is 2%. This once again confirms that the modeling error should converge to zero as the particle region is increased and justifies the use of an adaptive scheme to control the modeling error in this type of coupling methods.

### 6.2. Example with a point force prescribed on the boundary

We suppose that the lattice is subjected to a unit point force $F$ applied vertically at point $P_1$. As before, the loading force is applied in ten increments of magnitude $\Delta F=0.1$ each. Otherwise, the lattice is fixed at the bottom and free on top and along the two lateral walls (see Fig. 17). The material parameters are set to the same values as in the previous example. The weighting function $\alpha_c$ is chosen constant, i.e. $\alpha_c=0.5$, in the overlap region $\Omega_o$. The mesh for the continuum region is made of uniform squared elements (constant mesh size) for convenience. Each element contains $5\times5$ particles. The initial configuration of the Arlequin problem is shown in Fig. 18.

We suppose that we are interested in the vertical displacement $\mathbf{y}_{P_1}$ of the particle $P_1$ on which the loading force is applied. The quantity of interest $Q(\mathbf{y})$ is written in this case as:
$$
Q_1(\mathbf{y})=\mathbf{s}\cdot\mathbf{y}_{P_1}, \tag{38}
$$
where $\mathbf{s}=(0,1)$ is the unit vector in the $y$-direction. An approximation of the adjoint solution is obtained by solving the adjoint Arlequin problem (31) using an extra layer of particles around the overlap region. We show in Fig. 19 the adjoint solution with respect to the initial configuration after linear interpolation of the displacement vector $\mathbf{p}_0$. We actually show the strain component $\epsilon_{yy}$ based on the interpolated $\mathbf{p}_0$.

![](./images/811877213170302977_19.jpg)

Fig. 17. Model problem and region of interest for the example dealing with a point force applied on the boundary.

We now apply the goal-oriented error estimation and adaptive procedure presented in Section 5. On the initial mesh, we obtain the estimate of the relative error in the quantity of interest $Q_1(\mathbf{y})$ equal to:

![](./images/811877213170302977_20.jpg)

Fig. 18. Initial configuration of the Arlequin problem for both $Q_{1}(\mathbf{y})$ and $Q_{2}(\mathbf{y})$. The particles in the overlap region are not shown in this picture.

$$\eta_{\text{est}} = 13.1\%.$$

After six iterations of the adaptive algorithm, the estimated error is reduced to $\eta_{\text{est}} = 10.4\%$, $10.2\%$, $8.6\%$, $5.2\%$, $3.8\%$, and finally $2.1\%$. The corresponding sequence of adapted configurations for the Arlequin problem is shown in Fig. 20.

We now repeat the same experiments in the case of a second quantity of interest. We suppose that we are interested in the bond stretching between particles $P_{1}$ and $P_{2}$ (see Fig. 17):

![](./images/811877213170302977_21.jpg)

Fig. 19. Strain component $\epsilon_{yy}$ of the adjoint solution $\mathbf{p}_{0}$ associated with the quantity of interest $Q_{1}(\mathbf{y})$ (Colors do not vary linearly here in order to better represent the variations).

$$Q(\mathbf{y}) = \frac{r_{12} - r_{12}^{0}}{r_{12}^{0}}.\tag{39}$$

For simplicity, we consider here the linearized form of the quantity of interest with respect to the reference configuration, that is:

$$Q_{2}(\mathbf{y}) = \mathbf{s}_{12} \cdot \frac{\mathbf{y}_{P_{2}} - \mathbf{y}_{P_{1}}}{r_{12}^{0}},\tag{40}$$

![](./images/811877213170302977_22.jpg)

Fig. 20. Sequence of adapted meshes by the Goals algorithm with respect to the quantity of interest $Q_{1}$. After six iterations, the relative error in the vertical displacement at $P_{1}$ has been reduced from $13.1\%$ to $2.1\%$. The particles in the overlap region are not shown in these pictures.

where $\mathbf{s}_{12}=(\mathbf{x}_{P_{2}}-\mathbf{x}_{P_{1}})/r_{12}^{0}$ is the unit vector in the direction $\mathbf{x}_{P_{2}}-\mathbf{x}_{P_{1}}$. The corresponding strain component $\epsilon_{yy}$ of the adjoint solution is shown in Fig. 21.

The relative error in the bond stretching is estimated on the initial configuration to be
$$
\eta_{\text{est}}=6.3\%
$$
but is reduced to 3.0%, 2.5%, 2.1%, 1.9%, 1.8%, and 1.5% following six iterations of the adaptive algorithm (see Fig. 22). The initial error is small so that each adaptive step reduces the error in small fractions as this particular quantity of interest is less sensitive to far field errors. We naturally observe that the final configuration of the Arlequin problem is directly dependent on the choice of the quantity of interest.

![](./images/811877213170302977_23.jpg)

Fig. 21. Strain component $\epsilon_{yy}$ of the adjoint solution $\mathbf{p}_{0}$ associated with the quantity of interest $Q_{2}(\mathbf{y})$ (Colors do not vary linearly here in order to better represent the variations).

![](./images/811877213170302977_24.jpg)

Fig. 22. Sequence of adapted meshes by the Goals algorithm with respect to the quantity of interest $Q_{2}$. After six iterations, the relative error in the bond stretching between particles $P_{1}$ and $P_{2}$ has been reduced from 6.3% to 1.5%. The particles in the overlap region are not shown in these pictures.

### 6.3. Equilibrium of a crack

We propose here a simple problem for static simulation of a crack as shown in Fig. 23. We consider a "triangular" lattice, with characteristic length $\ell$, made of $n=59\times50$ particles. Interactions are modeled with Lennard-Jones potentials. The parameters of the potentials are $\sigma_{ij}=2^{-1/6}\times\ell$, so that the lattice is in equilibrium when no loading is applied, and $\epsilon_{ij}=1.4\times10^{-3},i,j=1,\ldots,n,i\neq j$. In this example, only nearest neighbor interactions are considered and the initial configuration of the Arlequin problem only includes particles that lie in the neighborhood of the crack tip (see Figs. 24 and 25). We suppose that we are interested in the vertical gap $\delta$ of the opening at a distance $5\ell$ from the right boundary, as shown in Fig. 23, so that the quantity of interest reads:
$$
Q(\mathbf{y})=\delta=r_{12},\tag{41}
$$
where 1 and 2 are the indices of the end particles. The lattice is fully orthotropic in this case and the continuum model is chosen such that it satisfies the following constitutive relationship:
$$
\begin{pmatrix}
\epsilon_{11} \\
\epsilon_{22} \\
\epsilon_{12}
\end{pmatrix}
=
\begin{bmatrix}
\frac{1}{E_{1}} & -\frac{v}{E_{1}} & 0 \\
-\frac{v}{E_{1}} & \frac{1}{E_{2}} & 0 \\
0 & 0 & \frac{1}{2G}
\end{bmatrix}
\begin{pmatrix}
\sigma_{11} \\
\sigma_{22} \\
\sigma_{12}
\end{pmatrix},\tag{42}
$$


![](./images/811877213170302977_25.jpg)

Fig. 23. Model problem for the crack example and quantity of interest $\delta$.

![](./images/811877213170302977_26.jpg)

Fig. 24. Nearest neighbor interactions.

![](./images/811877213170302977_27.jpg)

Fig. 25. Initial Arlequin configuration and mesh after deformation.

Calibration of the model parameters on proper representative volume elements gives

$$
\begin{align*}
E_1 &= 11.55, \\
E_2 &= 11.70, \\
G &= 3.25, \\
\nu &= 0.32.
\end{align*}
$$

In this example, we voluntarily use non-conforming meshes (non-conforming in the sense that particles do not necessarily coincide with nodes of the elements) with the sole objective to show that such configurations are manageable. However, it has to be done with caution: indeed, in order to ensure that integrals are accurately calculated, elements need to be subdivided into smaller elements. Moreover, it is important to use the formula (14) to calculate the weight coefficients $\alpha_{ij}^d$, as otherwise, the problem could become singular. We show in Fig. 26 the reconstructed strain component $\epsilon_{xx}$ computed from the exact solution $\mathbf{y}$ and approximate solution $(\mathbf{u},\mathbf{w})$. The strain component $\epsilon_{xx}$ of the adjoint solution $\mathbf{p}$ is shown in Fig. 27.

When computing the residual with respect to the reference particle model, we remark that the error is usually concentrated along the top surface where Neuman boundary conditions are applied. These errors are essentially due to the fact that the boundary conditions, as prescribed for the reference and surrogate problems, are not consistent. In order to circumvent the issue, we choose to prescribe tractions only to the continuum model. The reference model is now one in which the Neuman boundary conditions are applied by means of an Arlequin formulation using a layer along the top boundary in which the continuum model is used (see Fig. 28). The issue of imposing consistent boundary conditions, especially

![](./images/811877213170302977_28.jpg)

Fig. 26. Reconstructed strain component $\epsilon_{xx}$ using the exact (left) and approximate (right) solutions.

![](./images/811877213170302977_29.jpg)

Fig. 27. Strain component $\epsilon_{xx}$ associated with the solution $\mathbf{p}$ of the adjoint problem for $Q(\mathbf{y})=\delta$.

![](./images/811877213170302977_30.jpg)

Fig. 28. New reference problem.

![](./images/811877213170302977_31.jpg)

Fig. 29. Sequence of adapted meshes by the Goals algorithm for the crack problem. After four iterations, the relative error in the vertical gap $\delta$ has been reduced from 12.7% to 4.6%. The particles in the overlap region are not shown in these pictures.

for non-homogeneous lattices or long-range potentials, will be dis- cussed in a forthcoming paper. In that case, we are able to success- fully use the goal-oriented adaptive algorithm to reduce the modeling error from 12.7% to 4.6% in four successive iterations. We note though that the higher-order term $\Delta$ is no longer negligi ble, as it varies between 2% and 9% in this problem, but this does not alter the overall performance of the adaptive algorithm (see Fig. 29).

### 7. Conclusion

In this work, we have described the extension of goal-oriented error estimation and adaptive modeling to two-dimensional molecular statics problems involving monocrystalline lattices. We have constructed a linearly elastic continuum model based on RVE virtual experiments. The molecular and continuum models are coupled using an Arlequin formulation where the displace- ments and their derivatives are weakly constrained on a region of overlap between the two models. Error estimates in quantities of interest were estimated using the residual of the surrogate solu- tion weighted by the adjoint solution. In particular, approxima- tions to the adjoint were constructed for this class of problems. An adaptive modeling procedure, based on these error estimates, was used to selectively enlarge the molecular region to reduce the error in the quantity of interest. Three examples were shown illustrating the effectiveness of the method.

Extensions of the current work are under investigation. First, methods for uncertainty quantification within the Arlequin formu- lation are being considered as these are deemed important for model validation. Second, an adaptive strategy based on optimiz- ing the error in the quantity of interest is also being investigated as an alternative to the present "greedy" type algorithm used here. Third, the development of adaptive modeling algorithms to be implemented in parallel computing infrastructures as well as extensions to dynamic simulations present interesting and unique challenges. Finally, it is important to emphasize that the present

method for error estimation makes use of the Cauchy-Born hypothesis that usually only holds for monocrystalline materials undergoing small deformation. One issue will be to extend the cur- rent approach to more complex lattices. Preliminary work dealing with polymeric networks have been described in [5] but this issue will be investigated more carefully in forthcoming work.

Acknowledgements

P.T. Bauman acknowledges the support of the DOE Computa- tional Science Graduate Fellowship. H. Ben Dhia would like to thank the J.T. Oden Faculty Fellowship Research Program for the kind invitation to ICES in May 2008. Support of this work by DOE under contract DE-FG02-05ER25701 is gratefully acknowledged.

References

[1] M. Arndt, M. Luskin, Goal-oriented atomistic-continuum adaptivity for the quasicontinuum approximation, Int. J. Multiscale Comput. Engrg. 5 (2007) 407–415.

[2] S. Badia, M. Parks, P. Bochev, M. Gunzburger, R. Lehoucq, On atomistic-to- continuum (atc) coupling by blending, Multiscale Model. Simul. 7 (2008) 381–406.

[3] P.T. Bauman, H. Ben Dhia, N. Elkhodja, J.T. Oden, S. Prudhomme, On the application of the Arlequin method to the coupling of particle and continuum models, Comput. Mech. 42 (2008) 511–530.

[4] P.T. Bauman, Adaptive Multiscale Modeling of Polymeric Materials Using Goal- Oriented Error Estimation, Arlequin Coupling, and Goals Algorithms. PhD dissertation, The University of Texas at Austin, 2008.

[5] P. T Bauman, J.T. Oden, S. Prudhomme, Adaptive multiscale modeling of polymeric materials: Arlequin coupling and goals algorithms, Comput. Methods Appl. Mech. Engrg. 198 (2009) 799–818.

[6] R. Becker, R. Rannacher, An optimal control approach to a posteriori error estimation in finite element methods, Acta Numer. 10 (2001) 1–102.

[7] H. Ben Dhia, Multiscale mechanical problems: the Arlequin method, C.R. Acad. Sci. Paris, Série II B 326 (12) (1998) 899–904.

[8] H. Ben Dhia, G. Rateau, Analyse mathématique de la méthode Arlequin mixte, C.R. Acad. Sci. Paris, Série I 332 (2001) 649–654.

[9] H. Ben Dhia, G. Rateau, The Arlequin method as a flexible engineering design tool, Int. J. Numer. Methods Engrg. 62 (11) (2005) 1442–1462.

[10] H. Ben Dhia, N. Elkhodja, Coupling of atomistic and continuum models in the Arlequin framework, in: Proceedings of the 8eme Congrès de Mécanique, El Jadida, Maroc, April 17–20, 2007, pp. 133–135.

[11] J.Q. Broughton, F.F. Abraham, N. Bernstein, E. Kaxiras, Concurrent coupling of length scales: methodology and application, Phys. Rev. B 60 (4) (1999) 2391–2403.

[12] W.A. Curtin, R.E. Miller, Atomistic/continuum coupling in computational material science, Model. Simul. Mater. Sci. Engrg. 11 (2003) R33–R68.

[13] E.W.X. Li, E. Vanden-Eijnden, Some recent progress in multiscale modeling, Lect. Notes Comput. Sci. Engrg. 3 (2004) 3–22.

[14] J. Fish, Bridging the scales in nano engineering and science, J. Nanoparticle Res. 8 (6) (2006) 577–594.

[15] G. Friesecke, F. Theil, Validity and failure of the Cauchy–Born hypothesis in a two-dimensional mass-spring lattice, J. Nonlinear Sci. 12 (2002) 445–478.

[16] W.K. Liu, E.G. Karpov, S. Zhang, H.S. Park, An introduction to computational nanomechanics and materials, Comput. Methods Appl. Mech. Engrg. 193 (2004) 1529–1578.

[17] J.T. Oden, T.I. Zohdi, Analysis and adaptive modeling of highly heterogeneous elastic structures, Comput. Methods Appl. Mech. Engrg. 148 (1997) 367–391.

[18] J.T. Oden, K. Vemaganti, Estimation of local modeling error and goal-oriented modeling of heterogeneous materials. Part I: error estimates and adaptive algorithms, J. Comput. Phys. 164 (2000) 22–47.

[19] J.T. Oden, S. Prudhomme, Goal-oriented error estimation and adaptivity for the finite element method, Comput. Math. Appl. 41 (2001) 735–756.

[20] J.T. Oden, S. Prudhomme, Estimation of modeling error in computational mechanics, J. Comput. Phys. 182 (2002) 496–515.

[21] J.T. Oden, S. Prudhomme, A. Romkes, P.T. Bauman, Multi-scale modeling of physical phenomena: adaptive control of models, SIAM J. Sci. Comput. 28 (2006) 2359–2389.

[22] A. Romkes, J.T. Oden, Adaptive modeling of wave propagation in heterogeneous elastic solids, Comput. Methods Appl. Mech. Engrg. 193 (2004) 539–559.

[23] S. Prudhomme, P.T. Bauman, J.T. Oden, Error control for molecular statics problems, Int. J. Multiscale Comput. Engrg. 4 (2006) 647–662.

[24] S. Prudhomme, H. Ben Dhia, P.T. Bauman, N. Elkhodja, J.T. Oden, Computational analysis of modeling error for the coupling of particle and continuum models by the Arlequin method, Comput. Methods Appl. Mech. Engrg. 197 (2008) 3399–3409.

[25] E.B. Tadmor, M. Ortiz, R. Philips, Quasicontinuum analysis of defects in solids, Philos. Mag. A73 (1996) 1529–1563.

[26] K. Vemaganti, J.T. Oden, Estimation of local modeling error and goal-oriented modeling of heterogeneous materials. Part II: a computational environment for adaptive modeling of heterogeneous elastic solids, Comput. Methods Appl. Mech. Engrg. 190 (2001) 6089–6124.

[27] G.J. Wagner, W.K. Liu, Coupling of atomistic and continuum simulations using a bridging scale decomposition, J. Comput. Phys. 190 (1) (2003) 249–274.

[28] S.P. Xiao, T. Belytschko, A bridging domain method for coupling continua with molecular dynamics, Comput. Methods Appl. Mech. Engrg. 193 (2004) 1645–1669.