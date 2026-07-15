Accepted Manuscript

A finite-deformation dislocation density-based crystal viscoplasticity
constitutive model for calculating the stored deformation energy

M. Jafari, M. Jamshidian, S. Ziaei-Rad

| PII:       | S0020-7403(16)31058-X |
|------------|------------------------|
| DOI:       | 10.1016/j.ijmecsci.2017.05.016 |
| Reference: | MS 3691                |

| To appear in: | *International Journal of Mechanical Sciences* |
|---------------|-----------------------------------------------|

| Received date:  | 13 December 2016 |
|-----------------|------------------|
| Revised date:   | 16 April 2017    |
| Accepted date:  | 5 May 2017       |

Please cite this article as: M. Jafari, M. Jamshidian, S. Ziaei-Rad, A finite-deformation dislocation
density-based crystal viscoplasticity constitutive model for calculating the stored deformation energy,
*International Journal of Mechanical Sciences* (2017), doi: 10.1016/j.ijmecsci.2017.05.016

![](./images/813132113271324673_1.jpg)

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service
to our customers we are providing this early version of the manuscript. The manuscript will undergo
copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please
note that during the production process errors may be discovered which could affect the content, and
all legal disclaimers that apply to the journal pertain.

### Highlights

- A previously-developed infinitesimal strain and dislocation density based crystal viscoplasticity constitutive theory is reformulated in the finite deformation regime in a thermodynamically consistent manner.

- The constitutive equations are numerically implemented into the Abaqus/Standard finite element package via writing a user material subroutine UMAT.

- As an application of the developed constitutive model, the distribution of stored energy in aluminum bicrystals and polycrystals is investigated to estimate the driving forces for grain boundary migration due to the stored energy difference across grain boundary.

- Our statistical analysis shows that strain induced grain boundary migration occurs in a few predictable specific regions where certain grain orientations meet at a grain boundary across which high values of stored energy difference happens.

![](./images/813132113271324673_2.jpg)

![](./images/813132113271324673_3.jpg)

# A finite-deformation dislocation density-based crystal viscoplasticity constitutive model for calculating the stored deformation energy

M Jafari, M Jamshidian*, S Ziaei-Rad

Department of Mechanical Engineering, Isfahan University of Technology, Isfahan 84156-83111, Iran

## Abstract
A previously-developed infinitesimal strain and dislocation density based crystal vis- coplasticity constitutive theory is reformulated in the finite deformation regime in a ther- modynamically consistent manner. The constitutive equations are then numerically im- plemented into the Abaqus/Standard finite element package. The constitutive model is primarily verified and calibrated with respect to single crystal aluminum experiments and then the distribution of stored deformation energy in aluminum bicrystals and polycrystals is investigated to estimate the driving forces for grain boundary migration due to the stored energy difference across grain boundary. Our statistical analysis shows that the onset of strain induced grain boundary migration in a polycrystalline microstructure is basically de- pendent on the spatial distribution of the stored deformation energy rather than the overall stored deformation energy value; and it preferably occurs in a few predictable specific regions where certain grain orientations meet at a grain boundary across which high values of stored energy difference happens.

Keywords: Constitutive equation, Stored deformation energy, Dislocation density, Crystal viscoplasticity, Finite elements

## 1. Introduction
Most of the work done in deforming a metal is converted to heat and only a small amount remains as stored energy in the material. This stored energy is attributed to the point defects and line defects or dislocations, which are generated during deformation. In nominally pure metals, the substantial contribution to the stored energy is due to the accumulation of dislo- cations, while point defects do not contribute significantly to the stored energy of deformation especially at low temperatures. The dislocations create distortion in the crystalline lattice and thereby a specific amount of elastic energy is stored within material which is known as the stored energy of cold work. This stored energy is a key factor in microstructure evolution; it supplies the source for recovery and recrystallization during thermomechanical processes and drives the kinetics of grain or subgrain boundaries. For instance, the stored energy difference between neighboring grains provides a driving force sufficient to overcome

*Corresponding author. Email: jamshidian@cc.iut.ac.ir

Preprint submitted to International Journal of Mechanical Sciences
May 23, 2017

the pressure due to the boundary curvature, so that the boundary migrates into the grain with the higher stored energy. Therefore, in order to simulate thermomechanical processes involving the evolution of microstructure, there is a need to locally estimate the stored energy of cold work (Humphreys and Hatherly (2004); Anand et al. (2015)).

Regarding the fundamental importance of the stored energy of cold work in microstructure evolution, numerous experimental and theoretical investigations have been carried out to calculate its value. A detailed review of the literature on the stored energy of cold work was provided by Bever et al. (1973). Rosakis et al. (2000) presented a one-dimensional model within conventional continuum framework for calculating the fraction of the rate of plastic work converted into heat. They found that this fraction depends strongly on both strain and strain rate for various engineering materials. Benzerga et al. (2005) calculated the stored energy of cold work for planar single crystals under tensile loading using a discrete dislocation plasticity-based numerical study. They investigated the effects of strain level, dislocation structure and crystal orientation on the evolution of the stored energy. Very recently, Anand et al. (2015) developed a thermo-mechanically coupled gradient theory for rate-independent single-crystal plasticity using the principle of virtual power. They derived expressions for determination of the fraction of plastic stress-power that converts into heat and the reduction of the dislocation density in a cold-worked material upon subsequent thermal annealing. While presenting a novel constitutive model via a thermodynamically-consistent approach, their model is limited to small deformations. They also did not implement their model via a numerical algorithm. McBride et al. (2015) developed a numerical algorithm for the theory of Anand et al. (2015) using finite element method and then employed their model in a series of three dimensional numerical examples where special emphasis was placed on the role of the defect-flow relations. However, their findings are qualitative, and they did not perform a detailed comparison of their results with experimental results. It is anticipated that a phenomenological constitutive model with physical material parameters is capable of realistic simulations of stored energy distribution and is also able to display a quantitative match between simulation and experimental results.

The crystal plasticity continuum models as a powerful tool for describing the micromechanical behavior of metallic materials have received much attention during the last decade (Anand (2004); Gurtin et al. (2007); Aghababaei and Joshi (2013); Shanthraj et al. (2015); Zhang et al. (2015); Hu et al. (2016); Lubarda (2016)). Anand (2004) developed the thermodynamically-consistent, large deformation, classical continuum theory of single-crystal elasto-viscoplasticity and simulated the large deformation response of polycrystalline copper by finite element simulations. The continuum framework for strain-gradient plasticity was developed by Gurtin and co-workers (Gurtin (2000); Gurtin et al. (2007); Gurtin (2010); Anand et al. (2015)) by considering geometrically necessary dislocations. Their model is based on a system of microscopic force balances derived from the principle of virtual power including the power expended by both the plastic strain and the plastic-strain gradient. They were able to model the non-classical material behaviors like size effects in microscale.

Crystal plasticity models are also a powerful tool for describing the distribution of stored energy and consequently the evolution of microstructure in thermomechanical processes. Popova et al. (2015) simulated dynamic recrystallization in polycrystalline Mg using the crystal plasticity based finite element model coupled with a probabilistic cellular automata approach. The nucleation sites were determined based on the local inhomogeneity of dislo-

cation density across grain boundaries or within a grain. Stojakovic et al. (2008) simulated a step of light rolling on iron-silicon electrical steel with the crystal plasticity model of Ka- lidindi et al. (1992). They observed that grains with $\lambda$ fiber have low Taylor factors related to low stored energies. They also concluded that the $\lambda$ fiber texture is strengthened during recrystallization after applied light rolling. However, they did not precisely calculate the dis- tribution of stored energy in the polycrystalline microstructure and their crystal plasticity model was not established upon a dislocation density based theory.

The objective of this study is to investigate the stored deformation energy and disloca- tion density distribution found at the onset of grain boundary motion in a polycrystalline material. Particularly, in this study we reformulate the thermodynamically-consistent small- deformation-based constitutive theory of Anand et al. (2015) to develop a three-dimensional and finite-deformation-based constitutive model describing the evolution of dislocation den- sity in the grains of a polycrystalline metal under mechanical loading. As a simplification to the strain gradient theory of Anand et al. (2015), we only consider the statistically stored dislocations so that our theory is not classified as a gradient theory. In addition, the theory is developed under isothermal conditions i.e. it does not account for thermal recovery or the amount of plastic work that converts into heat. For calculating the stored deformation en- ergy of cold work, the free energy is chosen to depend on an internal variable representing the dislocation density. To complement the model, a phenomenological form of the viscoplastic flow rule which satisfies the reduced dissipation inequality is proposed and the constitutive equations are specified by proposing a specific form for the free energy functional. Next, a numerical algorithm is developed for the implementation of the constitutive theory into the Abaqus/Standard finite element package via writing a user material subroutine (UMAT). As an application of the developed constitutive model, the relationship between the stored de- formation energy and the driving forces for microstructure evolution due to the stored energy difference across grain boundary is investigated by numerical simulations of bicrystalline and polycrystalline samples.

## 2. Constitutive theory

This section describes the constitutive behavior of a single crystal in a polycrystalline microstructure. The constitutive behavior of a grain is described using a dislocation-based- crystal viscoplasticity theory based on the principle laws of thermodynamics.

### 2.1. General preliminaries for the constitutive framework

Consider a mesoscopic continuum region that $\mathcal{R}$ denotes an arbitrary subregion of it in the reference configuration where $\mathbf{n}$ indicates the outward unit normal vector on the boundary surface $\partial \mathcal{R}$ of $\mathcal{R}$. $\mathcal{X}$ represents an arbitrary mesoscopic particle inside $\mathcal{R}$. The mesoscale position vector of $\mathcal{X}$ in the reference and current configurations are represented by $\mathbf{x}$ and $\mathbf{y}=\hat{\mathbf{y}}(\mathbf{x}, t)$, respectively with $t$ denoting the real time. Also, $\theta>0$ denotes the absolute temperature of the material particle. In the reference configuration $\mathrm{d} A$ and $\mathrm{d} V$ represent the mesoscale area element and the mesoscale volume element, respectively. $\nabla$ and Div show the gradient and divergence operators with respect to the material coordinates in the reference configuration. The common mathematical notation in the modern continuum mechanics is used throughout (Thamburaja and Jamshidian (2014)).


All the mesoscale balance equations, constitutive equations and thermodynamic laws are developed in the reference configuration. As an assumption, the body/inertial forces are neglected and isothermal condition is presumed.

### 2.2. Free energy imbalance
Let $\mathbf{T}$ and $\mathbf{F} = \nabla \mathbf{y}$ represent Cauchy stress and deformation gradient, respectively, with $\mathrm{J} = \det \mathbf{F} > 0$. Under isothermal conditions, the local form of the free energy imbalance within $\mathcal{R}$ in the reference configuration is then given by

$$
\mathrm{J}\mathbf{T} : \mathbf{L} \geq \dot{\psi}, \tag{1}
$$

where $\psi$ represents the Helmholtz free energy per unit reference volume. Since $\mathbf{F} = \nabla \mathbf{y}$, we have $\dot{\mathbf{F}} = \nabla \dot{\mathbf{y}}$ and $\mathbf{L} = \dot{\mathbf{F}}\mathbf{F}^{-1}$ is the velocity gradient. The stress power term i.e. $\mathrm{J}\mathbf{T} : \mathbf{L}$ in terms of the elastic and plastic parts of deformation is calculated subsequently.

### 2.3. Microkinematical hypotheses
Following the works of Anand (2004) and Lele and Anand (2009), the total deformation gradient is represented by the multiplicative elastic-plastic decomposition as

$$
\mathbf{F} = \mathbf{F}^e \mathbf{F}^p
$$

where (i) $\mathbf{F}^p(\mathcal{X})$ represents the plastic part of $\mathbf{F}$ and maps referential segments $\mathrm{d}\mathbf{x}$ to segments $\mathrm{d}\mathbf{l} = \mathbf{F}^p(\mathcal{X})\mathrm{d}\mathbf{x}$ in the relaxed configuration due to the dislocations slide in a mesoscopic neighborhood of $\mathcal{X}$; (ii) $\mathbf{F}^e(\mathcal{X})$ represents the elastic part of $\mathbf{F}$ and maps the segments $\mathrm{d}\mathbf{l}$ in the relaxed configuration into segments $\mathrm{d}\mathbf{y} = \mathbf{F}^e(\mathcal{X})\mathrm{d}\mathbf{l}$ in the deformed configuration due to the elastic stretching and rotation of the lattice.

By $\mathbf{F} = \mathbf{F}^e \mathbf{F}^p$ and $\mathbf{L} = \dot{\mathbf{F}}\mathbf{F}^{-1}$, the decomposition leads to the following additive decomposition of the velocity gradient:

$$
\mathbf{L} = \mathbf{L}^e + \mathbf{F}^e \mathbf{L}^p \mathbf{F}^{e-1}, \tag{2}
$$

where $\mathbf{L}^e = \dot{\mathbf{F}}^e \mathbf{F}^{e-1}$ and $\mathbf{L}^p = \dot{\mathbf{F}}^p \mathbf{F}^{p-1}$ are the elastic and plastic distortion rates, respectively. The tensor $\mathbf{L}^p$ is related to dislocation motion as the plastic deformation is occurred by the motion of dislocations. It is assumed that the dislocation motion occurs on prescribed slip systems $\alpha = 1,2,\dots,N$ in the lattice that each slip system consists of a slip plane normal $\mathbf{m}_0^\alpha$ and a slip direction $\mathbf{s}_0^\alpha$. Therefore, the plastic distortion rate tensor is described by microshear-rates $\dot{\gamma}^\alpha$ on individual slip systems as follows:

$$
\mathbf{L}^p = \sum_{\alpha=1}^{N} \dot{\gamma}^\alpha \mathbf{s}_0^\alpha \otimes \mathbf{m}_0^\alpha, \tag{3}
$$

where the tensor $\mathbf{S}_0^\alpha = \mathbf{s}_0^\alpha \otimes \mathbf{m}_0^\alpha$ is referred to as the Schmid tensor.

### 2.4. Dislocation density associated with plastic deformation

A material with a perfect lattice structure cannot describe the plastic deformation at the atomic level. Thus, the nature of plastic deformation is related to defects in the lattice structure; the most important of which are dislocations or linear defects. Permanent plastic deformation is caused by the changes in the position of the dislocations. The creation of new dislocations and interaction of the dislocations with each other are the main mechanisms of work hardening at the microscopic level. The storage of dislocations at the microscopic level is caused by one of the following reasons. First, during a locally homogeneous deformation, dislocations can randomly trap each other to cause their storage. This storage of the dislocations is known as statistically stored dislocations (SSDs) that cause the motion of dislocations become more difficult. Consequently, plastic strains are attributed to the statistically stored dislocations. The second type of dislocation storage is known as the geometrically necessary dislocations (GNDs) which are necessary for the compatibility of various parts during deformation. Therefore, the geometrically necessary dislocations are responsible for plastic strain gradient (Voyiadjis and Deliktas (2010); Arsenlis et al. (2004)).

Following the works of Stojakovic et al. (2008) and Sha et al. (2014) on strain induced boundary migration and considering polycrystals with relatively large average grain sizes, for simplicity the geometrically necessary dislocations are not considered in the present work. Therefore, our theory is a mesoscale continuum theory with an explicit accounting of statistically stored dislocations with isotropic hardening.

The dislocation density evolution equations are formulated in terms of dislocation generation and dislocation annihilation as follows. Using the notation

$$
\vec{\rho}=\left(\rho^{1}, \rho^{2}, \ldots, \rho^{N}\right),
$$

where $\rho^{\alpha}$ with $\alpha=1, \ldots, N$ denotes the density of dislocations associated with slip system $\alpha$, it is presumed that the densities $\rho^{\alpha}$ change according to the following phenomenological constitutive relations (Anand et al. (2015))

$$
\dot{\rho}^{\alpha}=\mathrm{A}^{\alpha}(\vec{\rho}, \theta)\left|\dot{\gamma}^{\alpha}\right|-\mathrm{R}^{\alpha}(\vec{\rho}, \theta) \quad \text { with }\left.\quad \rho^{\alpha}\right|_{t=0}=\rho_{0}^{\alpha}. \quad \text { (4) }
$$

The first term on the right hand side of Eq. (4) describes dislocation generation because of plastic flow with $\mathrm{A}^{\alpha}(\vec{\rho}, \theta) \geqslant 0$ being the *dislocation-accumulation modulus*. The second term on the right hand side of Eq. (4) describes the decrease in dislocation density because of thermal annealing. $\mathrm{R}^{\alpha}(\vec{\rho}, \theta) \geqslant 0$ is referred to as the *recovery rate* and it is presumed that

$$
\frac{\partial \mathrm{R}^{\alpha}(\vec{\rho}, \theta)}{\partial \theta} \geqslant 0,
$$

to show that it increases with temperature.

### 2.5. Elastic strain tensor and stress power

In the present study, the elastic strain tensor is defined as

$$
\mathbf{E}^{e}=\frac{1}{2}\left(\mathbf{F}^{e \top} \mathbf{F}^{e}-\mathbf{I}\right) \Longrightarrow \dot{\mathbf{E}}^{e}=\frac{1}{2}\left(\dot{\mathbf{F}}^{e \top} \mathbf{F}^{e}+\mathbf{F}^{e \top} \dot{\mathbf{F}}^{e}\right). \quad \text { (5) }
$$

The elastic stretching rate is defined as $\mathbf{D}^e = sym\mathbf{L}^e$. Substituting the relation $\dot{\mathbf{F}}^e = \mathbf{L}^e\mathbf{F}^e$ into Eq. $(5)_2$ results in $\mathbf{D}^e = \mathbf{F}^{e-\top}\dot{\mathbf{E}}^e\mathbf{F}^{e-1}$. Using Eq. (2), $\mathbf{T} = \mathbf{T}^\top$ from the balance of angular momentum and $\mathbf{D}^e = \mathbf{F}^{e-\top}\dot{\mathbf{E}}^e\mathbf{F}^{e-1}$, the *stress power term* in Eq. (1) is given by

$$
\mathbf{J} \mathbf{T}: \mathbf{L}=\mathbf{T}^{e}: \dot{\mathbf{E}}^{e}+\mathbf{J} \mathbf{T}: \mathbf{F}^{e} \mathbf{L}^{p} \mathbf{F}^{e-1},
\tag{6}
$$

with $\mathbf{T}^e = \mathbf{J}\mathbf{F}^{e-1}\mathbf{T}\mathbf{F}^{e-\top}$ being the symmetric *true lattice stress* (Gurtin (2000)). Substituting $\mathbf{T} = \mathbf{J}^{-1}\mathbf{F}^e\mathbf{T}^e\mathbf{F}^{e\top}$ into Eq. (6) results in

$$
\mathbf{J} \mathbf{T}: \mathbf{L}=\mathbf{T}^{e}: \dot{\mathbf{E}}^{e}+\mathbf{C}^{e} \mathbf{T}^{e}: \mathbf{L}^{p}.
\tag{7}
$$

Finally, substituting Eq. (3) in Eq. (7) results in

$$
\mathbf{J} \mathbf{T}: \mathbf{L}=\mathbf{T}^{e}: \dot{\mathbf{E}}^{e}+\sum_{\alpha=1}^{N} \tau^{\alpha} \dot{\gamma}^{\alpha}.
\tag{8}
$$

with $\tau^\alpha = \mathbf{C}^e\mathbf{T}^e : \mathbf{S}_0^\alpha$ being the *resolved shear stress* on slip system $\alpha$.

### 2.6. Free energy

Along with the use of principle of material frame indifference (Anand (2004)), the works of Fried and Gurtin (1994), Gurtin et al. (2007), Anand et al. (2009) and Anand et al. (2015) are used to write the Helmholtz free energy per unit *reference volume*, $\psi = \hat{\psi}(\vec{\rho},\mathbf{E}^e,\theta)$, in the following separable form

$$
\psi=\psi^{e}+\psi^{p},
\tag{9}
$$

where $\psi^e = \hat{\psi}^e(\mathbf{E}^e,\theta)$, represents the *thermo-elastic* free energy, and $\psi^p = \hat{\psi}^p(\vec{\rho},\theta)$ represents the *defect/plastic* free energy. The material time derivative of Eq. (9) under isothermal condition is

$$
\dot{\psi}=\frac{\partial \psi^{e}}{\partial \mathbf{E}^{e}}: \dot{\mathbf{E}}^{e}+\sum_{\alpha=1}^{N} \frac{\partial \psi^{p}}{\partial \rho^{\alpha}} \dot{\rho}^{\alpha},
\tag{10}
$$

where *energetic defect forces* are defined by

$$
\mathcal{F}^{\alpha}(\vec{\rho}, \theta)=\frac{\partial \psi^{p}}{\partial \rho^{\alpha}},
\tag{11}
$$

with the assumption $\mathcal{F}^{\alpha}(\vec{\rho},\theta)\geq0$. Using Eqs. (4) and (11), we have

$$
\sum_{\alpha=1}^{N} \frac{\partial \psi^{p}}{\partial \rho^{\alpha}} \dot{\rho}^{\alpha}=\sum_{\alpha=1}^{N} \mathcal{F}^{\alpha}(\vec{\rho}, \theta) \mathrm{A}^{\alpha}(\vec{\rho}, \theta) \frac{\dot{\gamma}^{\alpha}}{\left|\dot{\gamma}^{\alpha}\right|} \dot{\gamma}^{\alpha}-\sum_{\alpha=1}^{N} \mathcal{F}^{\alpha}(\vec{\rho}, \theta) \mathrm{R}^{\alpha}(\vec{\rho}, \theta).
\tag{12}
$$

The *energetic nonrecoverable generalized stresses* $\tau_{en}^\alpha$ for slip system $\alpha$ are defined by the constitutive relations

$$
\tau_{e n}^{\alpha}=\mathcal{F}^{\alpha}(\vec{\rho}, \theta) \mathrm{A}^{\alpha}(\vec{\rho}, \theta) \frac{\dot{\gamma}^{\alpha}}{\left|\dot{\gamma}^{\alpha}\right|}.
\tag{13}
$$

Thus, using Eqs. (12) and (13) in Eq. (10) we get

$$
\dot{\psi}=\frac{\partial \psi^{e}}{\partial \mathbf{E}^{e}}: \dot{\mathbf{E}}^{e}+\sum_{\alpha=1}^{N} \tau_{e n}^{\alpha} \dot{\gamma}^{\alpha}-\sum_{\alpha=1}^{N} \mathcal{F}^{\alpha}(\vec{\rho}, \theta) \mathrm{R}^{\alpha}(\vec{\rho}, \theta).
\tag{14}
$$

### 2.7. Dissipation inequality and constitutive equations

Substituting Eqs. (8) and (14) into the dissipation inequality (1) results in

$$
\left(\mathbf{T}^{e}-\frac{\partial \psi^{e}}{\partial \mathbf{E}^{e}}\right): \dot{\mathbf{E}}^{e}+\sum_{\alpha=1}^{N} \mathcal{F}^{\alpha}(\vec{\rho}, \theta) \mathrm{R}^{\alpha}(\vec{\rho}, \theta)+\sum_{\alpha=1}^{N}\left(\tau^{\alpha}-\tau_{e n}^{\alpha}\right) \dot{\gamma}^{\alpha} \geq 0. \tag{15}
$$

With the application of standard thermodynamics arguments in inequality (15) and assuming that the stresses $(\tau^{\alpha}-\tau_{e n}^{\alpha})$ are independent of $\dot{\mathbf{E}}^{e}$, we get the constitutive equation for the elastic stress as

$$
\mathbf{T}^{e}=\frac{\partial \psi^{e}}{\partial \mathbf{E}^{e}}. \tag{16}
$$

By substituting Eq. (16) back into inequality (15), we obtain the reduced dissipation inequality as

$$
\sum_{\alpha=1}^{N} \mathcal{F}^{\alpha}(\vec{\rho}, \theta) \mathrm{R}^{\alpha}(\vec{\rho}, \theta)+\sum_{\alpha=1}^{N} \tau_{d i s}^{\alpha} \dot{\gamma}^{\alpha} \geq 0, \tag{17}
$$

with the dissipative microscopic stresses $\tau_{d i s}^{\alpha}$ defined as

$$
\tau_{d i s}^{\alpha}=\tau^{\alpha}-\tau_{e n}^{\alpha}. \tag{18}
$$

Following our previous assumptions $\mathcal{F}^{\alpha}(\vec{\rho}, \theta) \geq 0$ and $\mathrm{R}^{\alpha}(\vec{\rho}, \theta) \geq 0$ we have

$$
\mathcal{F}^{\alpha}(\vec{\rho}, \theta) \mathrm{R}^{\alpha}(\vec{\rho}, \theta) \geq 0.
$$

Furthermore, it is assumed that the dislocation evolution mechanisms on each slip system is strongly dissipative, i.e.

$$
\tau_{d i s}^{\alpha} \dot{\gamma}^{\alpha} \geq 0, \tag{19}
$$

for each $\alpha$.

As a result, dissipation is characterized by the following two distinct inequalities

$$
\tau_{d i s}^{\alpha} \dot{\gamma}^{\alpha} \geq 0 \quad \text { and } \quad \mathcal{F}^{\alpha}(\vec{\rho}, \theta) \mathrm{R}^{\alpha}(\vec{\rho}, \theta) \geq 0. \tag{20}
$$

where the inequalities are held for all slip systems $\alpha$. There are two distinct types of dissipation associated with each of the above inequalities: the first inequality, $\tau_{d i s}^{\alpha} \dot{\gamma}^{\alpha}$, represents dissipation due to slip on slip system $\alpha$; and the two, $\mathcal{F}^{\alpha}(\vec{\rho}, \theta) \mathrm{R}^{\alpha}(\vec{\rho}, \theta)$, is typical of quantities that represent dissipation associated with recovery. Since the constitutive theory is developed under isothermal conditions, the amount of plastic work that converts into heat is not calculated. However, the temperature dependence of the variables is still considered as the isothermal condition can be at any prescribed temperature. In what follows, a flow rule is proposed for $\tau_{d i s}^{\alpha}$ which satisfies inequality (19).

### 2.8. Viscoplastic flow rule

Following the works of Anand (2004) and Gurtin et al. (2007), the following form of the viscoplastic flow rule which satisfies inequality (19) is used for mechanical dissipative mechanisms of slip on slip system $\alpha$

$$
\tau_{d i s}^{\alpha}=\mathrm{S}^{\alpha} \mathrm{g}\left(\left|\dot{\gamma}^{\alpha}\right|\right) \frac{\dot{\gamma}^{\alpha}}{\left|\dot{\gamma}^{\alpha}\right|},
\tag{21}
$$

with $\mathrm{g}(|\dot{\gamma}^{\alpha}|)$, a dimensionless exponential function of the form

$$
\mathrm{g}\left(\left|\dot{\gamma}^{\alpha}\right|\right)=\left(\frac{\left|\dot{\gamma}^{\alpha}\right|}{\dot{\gamma}_{0}}\right)^{m},
$$

where $\dot{\gamma}_{0}>0$ is a constant reference strain-rate, and $m>0$ being the constant rate sensitivity parameter. The slip resistances $\mathrm{S}^{\alpha}$ on slip systems are strictly positive strength-like internal-state variables. The slip resistances are governed by the following hardening equations (Franciosi and Zaoui (1982) and Lee et al. (2010))

$$
\mathrm{S}^{\alpha}=\mu b \sqrt{\sum_{\beta} h^{\alpha \beta} \rho^{\beta}},
$$

where $h^{\alpha \beta}$ is the hardening parameter. The parameters $\mu$ and $b$ are the shear modulus and the magnitude of the Burgers vector, respectively. Finally, substituting Eqs. (21) and (13) into Eq. (18) results in

$$
\tau^{\alpha}=\mathcal{F}^{\alpha}(\vec{\rho}, \theta) \mathrm{A}^{\alpha}(\theta, \vec{\rho}) \frac{\dot{\gamma}^{\alpha}}{\left|\dot{\gamma}^{\alpha}\right|}+\mathrm{S}^{\alpha} \mathrm{g}\left(\left|\dot{\gamma}^{\alpha}\right|\right) \frac{\dot{\gamma}^{\alpha}}{\left|\dot{\gamma}^{\alpha}\right|}.
\tag{22}
$$

### 2.9. Specification of the constitutive equations

The constitutive theory was developed in a general sense; therefore, in this section the constitutive theory is specified based on a specific form for the free energy with a view towards applications. The thermo-elastic free energy is given by

$$
\psi^{e}=\frac{1}{2}\left[\mathbf{E}^{e}-\left(\theta-\theta_{o}\right) \alpha_{t h} \mathbf{I}\right]: \mathcal{C}\left[\mathbf{E}^{e}-\left(\theta-\theta_{o}\right) \alpha_{t h} \mathbf{I}\right],
\tag{23}
$$

where the material parameters $\mathcal{C}$, $\alpha_{t h}$ and $\theta_{o}$ denote the symmetric fourth-order elastic moduli tensor, the thermal expansion coefficient and the reference temperature, respectively. Substituting Eq. (23) in Eq. (16) results in

$$
\mathbf{T}^{e}=\mathcal{C}\left[\mathbf{E}^{e}-\left(\theta-\theta_{o}\right) \alpha_{t h} \mathbf{I}\right].
\tag{24}
$$

Following the works of Anand et al. (2015), Bever et al. (1973) and Abrivard et al. (2012), the defect energy $\psi^{p}$ is assumed to be

$$
\psi^{p}(\vec{\rho}, \theta)=a \mu b^{2} \sum_{\alpha=1}^{N} \rho^{\alpha},
\tag{25}
$$

where $a$ is a constant approximately equal to $0.5$, $\mu$ the shear modulus, and b the magnitude of the Burgers vector. Substituting Eq. (25) in Eqs. (11) and (13) results in

$$
\mathcal{F}^{\alpha}(\vec{\rho}, \theta)=\frac{\partial \psi}{\partial \rho^{\alpha}(\vec{\rho}, \theta)}=a \mu b^{2}>0 \quad \text { and } \quad \tau_{e n}^{\alpha}=a \mu b^{2} \mathrm{~A}^{\alpha}(\vec{\rho}, \theta) \frac{\dot{\gamma}^{\alpha}}{\left|\dot{\gamma}^{\alpha}\right|}.
\tag{26}
$$

Referring back to the evolution equation for dislocation densities i.e. Eq. (4), in the present study:

(i) A simple form for the dislocation accumulation modulus $\mathrm{A}^{\alpha}(\vec{\rho}, \theta)$ is chosen as

$$
\mathrm{A}^{\alpha}(\vec{\rho}, \theta)=\mathrm{K}_{1} \sqrt{\rho^{\alpha}},
\tag{27}
$$

where $\mathrm{K}_{1} \geq 0$ is a constant.

(ii) A simple non-interacting form for the recovery rate is assumed as

$$
\mathrm{R}^{\alpha}(\vec{\rho}, \theta)=\mathrm{K}_{2} \rho^{\alpha},
\tag{28}
$$

where $\mathrm{K}_{2} \geq 0$ is constant. Hence, Eq. (4) is specified as:

$$
\dot{\rho}^{\alpha}=\mathrm{K}_{1} \sqrt{\rho^{\alpha}}\left|\dot{\gamma}^{\alpha}\right|-\mathrm{K}_{2} \rho^{\alpha}.
$$

It is worthy of noting that in the relation for the dislocation accumulation modulus, commonly a threshold value is considered for the saturation of the dislocation density. However, as the case studies investigated in this paper are under simple tension and simple compression up to $34\%$ strain, we assume that the dislocation density is still less than its saturation threshold. Substituting Eqs. $(26)_{1}$ and (27) into Eq. (22) results in

$$
\tau^{\alpha}=\left(a \mu b^{2} \mathrm{~K}_{1} \sqrt{\rho^{\alpha}}+\mathrm{S}^{\alpha}\left|\frac{\dot{\gamma}^{\alpha}}{\dot{\gamma}_{0}^{\alpha}}\right|^{m}\right) \operatorname{sign}\left(\dot{\gamma}^{\alpha}\right).
\tag{29}
$$

It is obvious from Eq. (29) that the sign of $\dot{\gamma}^{\alpha}$ for each slip system is determined by the sign of $\tau^{\alpha}$ i.e.

$$
\operatorname{sign}\left(\dot{\gamma}^{\alpha}\right)=\operatorname{sign}\left(\tau^{\alpha}\right).
$$

Hence, the stress $\tau^{\alpha}$ satisfies

$$
\left|\tau^{\alpha}\right|=a \mu b^{2} \mathrm{~K}_{1} \sqrt{\rho^{\alpha}}+\mathrm{S}^{\alpha}\left|\frac{\dot{\gamma}^{\alpha}}{\dot{\gamma}_{0}^{\alpha}}\right|^{m}.
$$

Therefore, the microshear rates are given by

$$
\dot{\gamma}^{\alpha}=\dot{\gamma}_{0}^{\alpha}\left(\frac{\left|\tau^{\alpha}\right|-a \mu b^{2} \mathrm{~K}_{1} \sqrt{\rho^{\alpha}}}{\mathrm{S}^{\alpha}}\right)^{\frac{1}{m}} \operatorname{sign}\left(\tau^{\alpha}\right).
\tag{30}
$$

Details of the numerical algorithm for the implementation of the constitutive equations into the Abaqus/Standard finite element package via writing a user material subroutine (UMAT) are given in Appendix A.


## 3. Results and discussion

In this section, the developed constitutive model is used for simulating of bicrystalline and polycrystalline specimens under mechanical loading to investigate the stored energy distribution in a microstructure and its relationship with the microstructure evolution by the difference of stored energy across grain boundary. For this purpose, at first the constitutive model is calibrated using aluminum single crystal experimental results as follows.

### 3.1. Single crystal

The experimental results of Hosford et al. (1960) for aluminum single crystal are used to calibrate the dislocation density-based-crystal plasticity finite element model. The hardening parameters are obtained by fitting the simulation results to the experimental stress-strain curves. For simulation of single crystals, a finite element model with a cubic geometry with 8-node linear brick elements (C3D8) is used.

Table 1 shows the material constants extracted from literature (Arsenlis and Parks (2002)) and fitting parameters used in single crystal simulations. The reference shear rate, $\dot{\gamma}_{0}$, and the rate sensitivity parameter, m, are adopted from Kalidindi (1992) as shown in Table 1. The characteristics of slip systems $\mathbf{m}_{0}^{\alpha}$ and $\mathbf{s}_{0}^{\alpha}$ for $\alpha=1,2, \ldots, 12$ are given in Arsenlis and Parks (2002). The deformation is applied using a prescribed displacement with a constant strain rate of $1.7 \times 10^{-5} s^{-1}$ at temperature 273K. The comparison between the stress-strain curves for aluminum single crystals obtained from the crystal plasticity simulations using material parameters listed in Table 1 and the experimental results of Hosford et al. (1960) is shown in Fig. 1. The values of macroscopic stress and strain are the volume-averaged values calculated by averaging over the local stress and strain in the entire finite element model, respectively. As shown in Fig. 1, the dislocation density-based-crystal plasticity finite element model well captures the experimental stress-strain response and also the difference in hardening characteristics of $<111>$ and $<100>$ single crystals. According to Fig. 1, the rate of hardening for the $<111>$ single crystal is relatively faster than that in the $<100>$ single crystal.

Table 1: Material parameters used in aluminum single crystal simulations.

<table>
<tr>
<td>Elastic constants</td>
<td>$C_{11}=108$ GPa</td>
</tr>
<tr>
<td></td>
<td>$C_{12}=61.3$ GPa</td>
</tr>
<tr>
<td></td>
<td>$C_{44}=28.5$ GPa</td>
</tr>
<tr>
<td></td>
<td>$\mu=25$. GPa</td>
</tr>
<tr>
<td>Burgers vector</td>
<td>$|b|=2.863 \mathring{A}$</td>
</tr>
<tr>
<td>Flow rule</td>
<td>$\dot{\gamma}_{0}^{\alpha}=0.001 ~s^{-1}, \alpha=1,..., 12$</td>
</tr>
<tr>
<td></td>
<td>$\mathrm{m}=0.011$</td>
</tr>
<tr>
<td>Hardening parameters (fitted)</td>
<td>$\mathrm{K}_{1}=250 \mu m^{-1}$</td>
</tr>
<tr>
<td></td>
<td>$\mathrm{K}_{2}=0.01 ~s^{-1}$</td>
</tr>
<tr>
<td>Initial dislocation density (fitted)</td>
<td>$\rho_{0}^{\alpha}=0.01 \mu m^{-2}, \alpha=1,..., 12$</td>
</tr>
</table>


![](./images/813132113271324673_4.jpg)

Figure 1: Stress-strain response of < 111 > and < 100 > aluminum single crystals validated against experimental results of Hosford et al. (1960).

The evolution of the sum of dislocation densities on all slip systems i.e. $\sum_{\alpha=1}^{12} \rho^{\alpha}$ in the single crystals are depicted in Fig. 2(a). As shown in this figure, the difference in the evolution of dislocation densities is responsible for the difference in hardening rates of the two types of single crystals. Such a difference justifies that the stress level in < 111 > single crystal is higher than < 100 > single crystal. Fig. 2(b) shows the change in the stored deformation energy as a function of strain. The stored deformation energy is calculated as $a \mu b^{2} \sum_{\alpha=1}^{12} \rho^{\alpha}$. Briefly, at first the sum of dislocation densities on all slip systems, $\sum_{\alpha=1}^{12} \rho^{\alpha}$, is calculated at each integration point. Next, the stored deformation energy is calculated by $a \mu b^{2} \sum_{\alpha=1}^{12} \rho^{\alpha}$ for each integration point. Finally, the values of macroscopic stored deformation energy are calculated as the volume-averaged values of the local stored deformation energy in the entire model. As it is obvious from Fig. 2, the stored deformation energy and dislocation density evolution are strongly dependent on crystal orientation and increase by increasing strain level. Initially, both stored deformation energy and dislocation density increase rapidly and reach a saturated state at higher strain values.

In the next sections, the current model with the parameters presented in Table 1 is used for the simulation of bicrystalline specimens under plane-strain compression and polycrystalline samples under simple tension.

### 3.2. Bicrystal
As an application of the constitutive theory for the calculation of stored energy inside each grain of a polycrystalline material, we investigate the phenomenon of strain induced boundary migration (SIBM). SIBM is the migration or bulging of part of a pre-existing grain boundary driven by the difference in stored deformation energy across the grain boundary. The region swept by the grain boundary through SIBM has lower dislocation content. This region also has the same orientation as the old grain from which it is grown (Beck and Sperry

![](./images/813132113271324673_5.jpg)

Figure 2: Simulation results for pure aluminum single crystals: (a) the evolution of dislocation density versus strain and (b) the evolution of stored deformation energy versus strain.

(1950)). Generally, SIBM is dominant in the annealing of polycrystalline metals deformed by a low thickness reduction (Humphreys and Hatherly (2004)). Nowadays, researchers can produce polycrystalline materials with desirable texture using this mechanism. For example, Stojakovic et al. (2008) developed a processing route to recover the desired fiber texture in iron-silicon electrical steel using SIBM. They found that two steps of light rolling and subsequent annealing could greatly restore the pre-existing desired fiber texture because of its low stored energy. In another study, Ciulik and Taleff (2009) and Noell and Taleff (2015)) could produce large single crystals of molybdenum and tantalum from polycrystalline samples in the solid state using dynamic SIBM.

In order to understand the mechanism of recrystallization occurring at a grain boundary in SIBM, recrystallization experiments on bicrystals are used (Theyssier and Driver (1999); Kashihara et al. (2011)). An aluminum bicrystalline specimen that has a pair of texture of Brass {011} < 112 >, S {123} < 634 >, cube {100} < 001 > and Copper {112} < 111 > as two initial orientations, are deformed by tension or by plane strain compression (rolling). These crystal orientations are known as the main components of rolling texture in FCC metals (Godfrey et al. (2001); Theyssier and Driver (1999); Kashihara et al. (2011)).

Because of the fact that most of the engineering applications require the cube texturefor special uses, for example high voltage aluminum capacitor foil, the development of {100}< 001 > recrystallization texture is desired (Kashihara et al. (2011)). As the stored energy of the cube texture is low in comparison with other textures, after plastic deformation of a FCC metal containing high stacking fault energy and consequently during annealing, this texture can grow rapidly. In order to examine the preferential nucleation and growth of < 001 > grains, the developed constitutive model is used for simulating two types of bicrystals consisting of < 001 >/< 111 > and < 001 >/< 634 > orientations. By comparing the stored energies in the < 001 > crystal when it adjoins either the < 111 > crystal or the < 634 > crystal, it can be proved that the < 001 > crystal will grow during annealing because of its lower stored energy.

Therefore, in this section, two different aluminum bicrystals with < 001 > / < 111 > and< 001 > / < 634 > orientations are simulated under plane strain compression using material parameters listed in Table 1. Fig. 3(a) illustrates a schematic depiction of the channel die and specimen used in simulation. The flat grain boundary is normal to the loading direction.

### 3.2.1. Simulation results

Fig. 3(b) shows the bicrystal of dimensions $3.8mm \times 20mm \times 4.9mm$ used in simulations. The FEM mesh consists of **2000 C3D8 type elements**. Lateral faces and bottom face are restricted in the 1 and 2 directions, respectively. The top face normal to direction 2 is given a prescribed displacement in order to apply a compressive strain of 34% along direction 2. In this way, a true strain rate of $1.7 \times 10^{-3} s^{-1}$ is applied on the top surface at a temperature of 298K.

The numerical simulation results for the distribution of stored energy in the bicrystal< 001 >/< 111 > is shown in Fig. 4. As is obvious from this figure, the bottom single crystal i.e. crystal < 111 > has relatively higher local values of stored deformation energy compared to the top single crystal.

The volume averaged stored deformation energies in the single crystals of each bicrystal are presented in Table 2. The values of stored energy are the volume-averaged values calcu-

lated from the local stored energy of each single crystal. Table 2 shows that the stored energy of crystal $<111>$ in bicrystal $<001>/<111>$ is higher than crystal $<001>$ with a cube texture. In bicrystal $<001>/<634>$, the crystal $<634>$ has more stored energy than crystal $<001>$. Also, the stored energy of crystal $<111>$ is higher than crystal $<634>$. Therefore, the driving force arising from different stored deformation energy in dislocation structures moves the boundary in a way to minimize the free energy of the bicrystalline body as a thermodynamically meta-stable domain. Since the stored energy in the cube texture is less than other textures, after annealing the recrystallized area has the same crystal orien- tation as crystal $<001>$ which has expanded towards crystals $<634>$ and $<111>$. In other words, the crystals $<634>$ and $<111>$ are invaded by the $<001>$ oriented region formed by SIBM. The rate of SIBM in bicrystal $<001>/<111>$ is expected to be higher than bicrystal $<001>/<634>$ due to higher stored energy difference.

Table 2: The volume avaraged stored deformation energies in the single crystals of each bicrystal.

<table>
  <thead>
    <tr>
      <th>Bicrystal</th>
      <th>Crystal</th>
      <th>Average stored energy(MJ/$m^3$)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">$<001>/<111>$</td>
      <td>$<111>$</td>
      <td>4.17</td>
    </tr>
    <tr>
      <td>$<001>$</td>
      <td>2.52</td>
    </tr>
    <tr>
      <td rowspan="2">$<001>/<634>$</td>
      <td>$<634>$</td>
      <td>3.76</td>
    </tr>
    <tr>
      <td>$<001>$</td>
      <td>2.34</td>
    </tr>
  </tbody>
</table>

### 3.2.2. Qualitative match with experimental results
The aforementioned simulation results are in satisfactory agreement with experimental observations of other researchers (Kashihara et al. (2011); Godfrey et al. (2001)). Kashihara et al. (2011) conducted experiments on aluminum bicrystals with crystals C {112} $<111>$, S {123} $<634>$, and W {100} $<001>$ under plane strain compression at room temperature. They plotted a two dimensional distribution of the Kernel average misorientation (KAM) maps using EBSD data of bicrystal C/W after deformation and before annealing. From their results, crystal C of bicrystal C/W had more obscure pattern than crystal W. Therefore, KAM in crystal C was larger than crystal W. They also calculated the stored energy values inside each crystal using the data of KAM maps. The stored energies in crystal C of bicrystal C/W was in the range of 180.8-279.8 kJ/$m^3$, whereas crystal S of bicrystal S/W contained stored energies of 109.6-130.9 kJ/$m^3$. Therefore, they concluded that the stored energy in crystal C is larger than crystal S.

Even though the value of stored energy in the single crystals in our simulations is different from the experiments of Kashihara et al. (2011), there is a qualitative correspondence in that the stored energy in crystal C or $<111>$ is larger than crystal S or $<634>$. The quantitative difference between our results and the experimental results of Kashihara et al. (2011) is because of the fact that we initially calibrated the hardening parameters with


experimental data obtained from the work of Hosford et al. (1960) as there are no strain-stress curves for each of single crystals in the work of Kashihara et al. (2011).

Fig. 4 also shows that the grain boundary is inclined after deformation. This result is also in qualitative agreement with the experimental results of Kashihara et al. (2011) obtained after mechanical work and before annealing.

#### 3.2.3. Discussion on SIBM in bicrystal
Using a dislocation density-based crystal plasticity finite element model, an acceptable estimation of the stored energy was calculated in this section. According to Table 2, the difference in stored energy in bicrystals $<001>/<111>$ and $<001>/<634>$ are $\Delta E=1.65 MJ / m^{3}$ and $\Delta E=1.42 MJ / m^{3}$, respectively. Following the work of Bailey (1960), the critical radius for growth (bulging) of a grain boundary with energy $\gamma$ in SIBM is given by $r_{critical }=2 \gamma / \Delta E$ where $\Delta E$ is the difference in stored energy between the two adjacent grains. This relation shows that the critical radius is reduced with increasing the stored energy and consequently there is a higher possibility of bulging of a grain boundary. If the energy of aluminum high angle grain boundary is considered to be $0.324 ~J / m^{2}$ (Godfrey et al. (2001)), the critical radius for bicrystals $<001>/<111>$ and $<001>/<634>$ are estimated as $0.393 \mu m$ and $0.456 \mu m$, respectively. Therefore, bicrystal $<001>/<111>$ has a higher probability of bulging of grain boundary by SIBM than bicrystal $<001>/<634>$.

At the growth stage, the grain boundary moves in response to the net pressure P on the boundary with a velocity $V$ given by $V=MP$ where $M$ is the mobility of boundary. In general, it is presumed that the velocity has a linear relationship with the net pressure via the constant M (Humphreys and Hatherly (2004)). The difference in stored energy between two adjacent grains determines the net pressure $P$ on the boundary. In the present work, because the driving pressure in bicrystal $<001>/<111>$ is more than bicrystal $<001>/<634>$, SIBM is faster in bicrystal $<001>/<111>$ than in bicrystal $<001>/<634>$. Therefore, it is clear that the stored energy distribution, via causing the driving pressure, strongly affects the kinetics of SIBM.

### 3.3. Polycrystal
As discussed in the previous section, the evolution of microstructure during annealing for a deformed metal depends not only on the stored energy, but also particularly on its spatial distribution. Therefore, in this section, we investigate the relationship between microstructure evolution and stored energy by simulating the development of dislocation density distribution in a polycrystalline microstructure under loading. Particularly, this section reports the difference of stored energy among the grains of aluminum polycrystal deformed by simple tension.

The representative volume element (RVE) used to describe an aluminum polycrystalline microstructure has an initial cubic geometry consisting of 512 C3D8 type elements in which each element is assumed to be a single grain with a random crystallographic orientation. Fig. 5(a) shows the initial finite element mesh of the polycrystalline RVE. According to our simulations performed on polycrystalline RVEs with realistic grain morphology produced by Voronoi tessellation method as explained in Appendix B, the RVE shown in Fig. 5(a) delivers satisfactory estimates of the stored energy distribution. The tension is applied

using a prescribed displacement. A true strain rate of $1.7e-3 s^{-1}$ is applied to the RVE at temperature of 273K.

The numerical simulation results for the distribution of stored energy in the microstructure are shown in Fig. 5(b). As shown in this figure, the stored energies are different for various grains because of their distinct crystal orientations. To investigate the differences among the stored energies of different grains in more detail, we focus on a typical region of microstructure in Fig. 5(b). Fig. 6 shows the evolution of stored energy versus strain within the grains highlighted in Fig. 5(b). As Fig. 6 shows, the evolution of stored energy with strain for each grain and the slope of each curve is different from another. For example, while initially the stored energy inside grain E is more than its top and bottom grains B and H, the slope of its curve is decreasing with strain while the stored energies for other grains are increasing with a higher rate. These observations are important for the evolution of microstructure during annealing because the difference of stored energies between adjacent grains provides the driving force for grain boundary migration by SIBM.

The evolution of the difference in stored energy among the adjacent grains highlighted in Fig. 5(b), is shown in Fig. 7. It is evident that the driving pressures on the grain boundaries due to the difference in stored energy between two adjacent grains are different for every pair of grains. At the growth stage, the rate of SIBM between two adjacent grains E-B will be higher than adjacent grains E-F, E-D and E-H. It can be concluded form Fig. 7 that SIBM does not occur between adjacent grains E-H, E-D in the early stage of loading. With increasing strain, the driving pressure for SIBM between adjacent grains E-H and E-D increases at first and then it decreases while the pressure for SIBM between adjacent grains E-B and E-F continuously increases with strain.

In order to gain a statistical understanding of the effect of the stored energy on microstructure evolution, the histograms of the stored energy are plotted in Fig. 8 for the polycrystalline RVE consisting of 512 grains at different strain values of 10%, 20% and 34%. From Fig. 8 it is obvious that the range of stored energies increases with increasing strain. In other words, the difference between the maximum and minimum values of stored energy increases with strain, resulting in the higher possibility of SIBM. Therefore, higher deformation increases the amount of stored energy and the number of effective nuclei and consequently the rate of recrystallization by SIBM. Fig. 8 also shows that the distribution of stored energy is more uniform for small values of strain and the plastic strain is accommodated by most of the grains in the polycrystal. However, by increasing strain, it is observed that plastic strain increments are primarily accommodated by specific grains that have certain orientations. As a result, the possibility of bulging of a grain boundary by SIBM in these regions becomes greater.

To have a closer look at the driving pressure for SIBM from a statistical point of view, histograms of the difference in stored energy across grain boundary for every pair of neighboring grains in the polycrystalline RVE are demonstrated in Fig. 9 at different strain values of 10%, 20% and 34%. It is obvious from these histograms that the number of grain boundaries across which high values of stored energy difference occurs are quite few. To investigate about these grain boundaries, Table 3 shows the 10 grain boundaries that have the maximum driving pressure in descending order for different values of strain. This table shows that these grain boundaries persist to exist at different strains and the difference in stored energy across them increases with strain. As it can be seen in this table, there are

some grain boundaries, like grain boundary B at strain 10%, that disappear form the list at higher values of strain; however our simulation results show that they still experience large stored energy difference at strains 20% and 34%.

In summary, the results of Table 3 and Fig. 9 show that SIBM only occurs at a few specific grain boundary segments where the maximum stored energy difference happens. In fact, grain boundary migration occurs when the driving force due to the stored energy difference overcomes a thermodynamic critical resistance. Therefore, for a prescribed value of such a critical resistance as a material parameter, our results show that only a few predictable grain boundary segments are capable to overcome this resistance and migrate. By the onset of the migration of these specific grain boundary segments, the dislocation density behind the boundary in the region swept by the boundary resets to its undeformed state, resulting in an increase in driving force. Therefore, on a local time scale, SIBM is continued by the same grain boundaries involved in the initiation of SIBM. These statements are in satisfactory agreement with experimental observations of other researchers (Stojakovic et al. (2008) and Ciulik and Taleff (2009)) that observed only a few grains tend to grow during SIBM, while grain boundaries in other regions do not experience SIBM.

Table 3: The grain boundries in polycrystalline RVE which experience maximum difference of stored energies ($\Delta \psi^{p}$) at strains 10%, 20% and 34%. Boundary label "A" represents grain boundary between two specific adjacent grains and likewise for other boundary labels in this table.

<table>
  <thead>
    <tr>
      <th>Boundary at 10% strain</th>
      <th>$\Delta \psi^{p}(MJ/m^{3})$</th>
      <th>Boundary at 20% strain</th>
      <th>$\Delta \psi^{p}(MJ/m^{3})$</th>
      <th>Boundary at 34% strain</th>
      <th>$\Delta \psi^{p}(MJ/m^{3})$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>A</td>
      <td>0.208</td>
      <td>A</td>
      <td>0.593</td>
      <td>I</td>
      <td>1.096</td>
    </tr>
    <tr>
      <td>B</td>
      <td>0.186</td>
      <td>C</td>
      <td>0.545</td>
      <td>O</td>
      <td>1.006</td>
    </tr>
    <tr>
      <td>C</td>
      <td>0.171</td>
      <td>E</td>
      <td>0.513</td>
      <td>C</td>
      <td>0.973</td>
    </tr>
    <tr>
      <td>D</td>
      <td>0.170</td>
      <td>I</td>
      <td>0.497</td>
      <td>P</td>
      <td>0.941</td>
    </tr>
    <tr>
      <td>E</td>
      <td>0.164</td>
      <td>F</td>
      <td>0.469</td>
      <td>Q</td>
      <td>0.921</td>
    </tr>
    <tr>
      <td>F</td>
      <td>0.160</td>
      <td>K</td>
      <td>0.468</td>
      <td>A</td>
      <td>0.915</td>
    </tr>
    <tr>
      <td>G</td>
      <td>0.155</td>
      <td>H</td>
      <td>0.460</td>
      <td>R</td>
      <td>0.911</td>
    </tr>
    <tr>
      <td>H</td>
      <td>0.155</td>
      <td>L</td>
      <td>0.455</td>
      <td>S</td>
      <td>0.888</td>
    </tr>
    <tr>
      <td>I</td>
      <td>0.154</td>
      <td>M</td>
      <td>0.448</td>
      <td>T</td>
      <td>0.883</td>
    </tr>
    <tr>
      <td>J</td>
      <td>0.153</td>
      <td>N</td>
      <td>0.442</td>
      <td>E</td>
      <td>0.873</td>
    </tr>
  </tbody>
</table>

## 4. Conclusion

In this paper, a thermodynamically consistent three-dimensional, finite-strain and dis- location density-based, crystal plasticity constitutive model was developed to describe the distribution of stored energy and dislocation density in a polycrystalline microstructure. The constitutive equations were implemented into the Abaqus/Standard finite-element package through writing a user-material subroutine (UMAT). In summary, the following key results were obtained via numerical simulations:


(i) The stress-strain response of aluminum single crystals was simulated with acceptable accuracy and the characteristic differences in hardening behavior between $<001>$ and $<111>$ oriented crystals were obtained by numerical simulations.

(ii) The bicrystalline specimens under plane strain compression were simulated to investigate the stored energy distribution in the microstructure and its relationship with microstructure evolution via SIBM. Simulation results demonstrated that the rapid growth of grains with cube texture is due to their low value of stored energy so that these orientations are usually the strongest texture component of recrystallized aluminum.

(iii) The simulation results for the polycrystalline specimens under simple tension showed that SIBM preferably occurs in specific regions where certain grain orientations meet at a grain boundary across which high values of stored energy difference happens.

As a future work, the present model will be coupled with the phase field model for grain boundary migration (Thamburaja and Jamshidian (2014); Jamshidian and Rabczuk (2014); Jamshidian et al. (2014, 2016)) to develop a constitutive theory for SIBM. Such a model can be used to simulate the kinetics of grain boundary migration by SIBM in a plastically deformed polycrystalline metal.

![](./images/813132113271324673_6.jpg)

Figure 3: (a) Crystal orientations of the bicrystal in the channel die. (b) Initial FEM mesh for bicrystal simulations.

![](./images/813132113271324673_7.jpg)

Figure 4: Simulation results for the distribution of stored deformation energy in the aluminum bicrystal $<001>/<111>$ under 34% thickness reduction in plane strain compression along direction 2.

![](./images/813132113271324673_8.jpg)

Figure 5: (a) Initial FEM model of the simulated microstructure (b) The simulation results for the distribu- tion of stored deformation energy in the microstructure.

![](./images/813132113271324673_9.jpg)

Figure 6: The evolution of stored deformation energy in the highlighted grains in Fig. 5(b).

![](./images/813132113271324673_10.jpg)

Figure 7: The evolution of the difference in stored deformation energy between adjacent grains highlighted in Fig. 5(b).

![](./images/813132113271324673_11.jpg)

Figure 8: Histograms of the stored deformation energy for the polycrystalline RVE after (a) 10% (b) 20%
(c) 34% uniaxial tensile strain.

![](./images/813132113271324673_12.jpg)

Figure 9: Histograms of the difference in stored energy across grain boundary for every pair of neighboring grains in the polycrystalline RVE after (a) 10% (b) 20% (c) 34% uniaxial tensile deformation.

## Appendix A. Time integration procedure

The developed constitutive equations are implemented in Abaqus/standard finite element package via writing a material user subroutine UMAT. The time integration procedure for a displacement-based finite element program is as follows. In the time integration algorithm, $t$ is defined as the current time with $\Delta t$ being the time increment, and $\tau = t + \Delta t$. At each finite element integration point, the given quantities are: (i)$\mathbf{F}(t), \mathbf{F}(\tau)$, (ii) $(\mathbf{m}_{0}^{\alpha}, \mathbf{s}_{0}^{\alpha})$ and (iii) $\{\mathbf{F}^{p}(t), \mathbf{s}^{\alpha}(t), \mathbf{T}(t), \rho^{\alpha}(t)\}$ and the numerical algorithm is to calculate $\{\mathbf{F}^{p}(\tau), \mathbf{s}^{\alpha}(\tau), \mathbf{T}(\tau), \rho(\tau)\}$, and then march forward in time. The following algorithm is a modified version of the time integration procedure of Kalidindi et al. (1992) and Anand (2004). The numerical algorithm involves the following steps:

### Step 1: Calculate
$$\mathbf{F}^{e,trial} = \mathbf{F}(\tau)\mathbf{F}^{p^{-1}}(t),$$

$$\mathbf{C}^{e,trial} = (\mathbf{F}^{e,trial})^{\mathrm{T}}\mathbf{F}^{e,trial}$$

$$\mathbf{E}^{e,trial} = \frac{1}{2}(\mathbf{C}^{e,trial} - \mathbf{I})$$

$$\mathbf{T}^{e,trial} = \mathcal{C}[\mathbf{E}^{e,trial}]$$

$$\mathbf{C}^{\alpha} = \mathcal{C}[sym(\mathbf{C}^{e,trial}\mathcal{S}_{0}^{\alpha})]$$

### Step 2: Solve the following three coupled equations for calculating $\Delta \gamma^{\alpha} \equiv \dot{\gamma}^{\alpha}(\tau)\Delta t$:
$$\mathbf{T}^{e}(\tau) = \mathbf{T}^{e,trial} - \sum_{\alpha} \Delta \gamma^{\alpha}\mathbf{C}^{\alpha}$$

$$s^{\alpha}(\tau) = \mu b \sqrt{\sum_{\beta} h^{\alpha \beta} \rho^{\beta}(\tau)}$$

$$\rho^{\alpha}(\tau) = \rho^{\alpha}(t) + \mathrm{K}_{1}\sqrt{\rho^{\alpha}}|\Delta \gamma^{\alpha}| - \mathrm{K}_{2}\rho^{\alpha}\Delta t$$

For calculating $\mathbf{T}^{e}(\tau)$, $s^{\alpha}(\tau)$ and $\rho^{\alpha}(\tau)$ we use the following three-level iterative procedure.

- **Iteration level 1:** by using a Newton-type iterative algorithm, the first equation is solved for $\mathbf{T}^{e}(\tau)$, while $s^{\alpha}(\tau)$ and $\rho^{\alpha}(\tau)$ are fixed at their best available estimates. Estimates of $\mathbf{T}^{e}(\tau)$ at the end of n and n+1 iterations of Newton-Raphson are identified by subscripts n and n+1, respectively, as follows:

$$\mathbf{T}_{n+1}^{e}(\tau) = \mathbf{T}_{n}^{e}(\tau) - \mathcal{F}_{n}^{-1}[\mathbf{G}_{n}]$$

with

$$
\mathbf{G}_{n} \equiv \mathbf{T}_{n}^{e}(\tau)-\mathbf{T}^{e, t r i a l}+\sum_{\alpha} \Delta \gamma^{\alpha}\left(\mathbf{T}_{n}^{e}(\tau), \mathbf{s}_{k}^{\alpha}(\tau), \rho_{m}^{\alpha}(\tau)\right) \mathbf{C}^{\alpha}
$$

$$
\mathcal{F}_{n} \equiv \mathcal{F}+\sum_{\alpha} \mathbf{C}^{\alpha} \otimes \frac{\partial}{\partial \mathbf{T}_{n}^{e}(\tau)} \Delta \gamma^{\alpha}\left(\mathbf{T}_{n}^{e}(\tau), \mathbf{s}_{k}^{\alpha}(\tau), \rho_{m}^{\alpha}(\tau)\right)
$$

- Iteration level 2: while $s^{\alpha}(\tau)$ is fixed at its best available estimate, $\rho^{\alpha}(\tau)$ is simply updated as follows:

$$
\rho_{m+1}^{\alpha}(\tau)=\rho^{\alpha}(t)+\mathrm{K}_{1} \sqrt{\rho_{m}^{\alpha}}\left|\Delta \gamma^{\alpha}\left(\mathbf{T}_{n+1}^{e}(\tau), \mathbf{s}_{k}^{\beta}(\tau), \rho_{m}^{\alpha}(\tau)\right)\right|-\mathrm{K}_{2} \rho_{m}^{\alpha} \Delta t
$$

where the value of $\rho^{\alpha}(\tau)$ at the end of the $m$ th update at the second level is identified by the subscript m.

- Iteration level 3: $s^{\alpha}(\tau)$ is simply updated by:

$$
s_{k+1}^{\alpha}(\tau)=\mu b \sqrt{\sum_{\beta} h^{\alpha \beta} \rho_{m+1}^{\beta}(\tau)}
$$

where the value of $\mathbf{s}^{\alpha}(\tau)$ at the end of the $k$ th update at the third level is shown by the subscript k.

Step 3: Calculate

$$
\mathbf{F}^{p}(\tau)=\left\{\mathbf{I}+\sum_{\alpha} \Delta \gamma^{\alpha} \mathcal{S}_{0}^{\alpha}\right\} \mathbf{F}^{p}(t)
$$

We then normalize $\mathbf{F}^{p}(\tau)$ in order to make sure that the determinant of $\mathbf{F}^{p}(\tau)$ remains unity. To normalize $\mathbf{F}^{p}(\tau)$, the computed values of its components are divided by the cube root of its computed determinant.

Step 4: Calculate

$$
\mathbf{T}(\tau)=\frac{1}{\operatorname{det} \mathbf{F}(\tau)} \mathbf{F}(\tau) \mathbf{F}^{p-1}(\tau) \mathbf{T}^{e}(\tau) \mathbf{F}^{p-T}(\tau) \mathbf{F}^{T}(\tau)
$$

To determine the Jacobian matrix for the finite-element code Abaqus/Standard to perform Newton-Raphson iterations, the analytical Jacobian of Balasubramanian (1998) was used.

### Appendix B. Polycrystalline RVE with realistic grain morphology

In this appendix, we compare the simulation results between the simplified RVE consist- ing of cubic-shaped grains per finite element as discussed before and the RVE with realistic grain morphology produced by the voronoi tessellation method. Fig. B.10 shows the simple cubic and voronoi tessellation models with random grain orientations used in simulations. For generating the voronoi tessellation model of the polycrystalline RVE, we used the ap- proach of Nouri et al. (2012). Fig. B.11 shows the evolution of stress and stored energy with

strain for both models. The following results can be extracted from Fig. B.11. First, the difference in stress versus strain and stored energy versus strain curves for 64 cubic grains and 512 cubic grains with one finite element per grain is negligible. Second, the difference between the model including 64 cubic grains with one finite element per grain and the model including 64 Voronoi grains each meshed with several finite elements is also negligible. Be- cause of the fact that the solution time for voronoi model is more than the simple cubic model due to its high mesh density, in this study we perform simulation using the simple cubic model with 512 grains and one element per grain.

![](./images/813132113271324673_13.jpg)

Figure B.10: Finite element mesh used in (a) voronoi tessellation model (b) simple cubic model.

![](./images/813132113271324673_14.jpg)

Figure B.11: Comparison between the obtained simulation results from simple cubic model and voronoi tessellation model (a) stress-strain curve (b) stored energy.

## References

Abrivard, G., Busso, E., Forest, S., Appolaire, B., 2012. Phase field modelling of grain boundary motion driven by curvature and stored energy gradients. part i: theory and numerical implementation. Philosophical Magazine 92, 3618-3642.

Aghababaei, R., Joshi, S.P., 2013. Micromechanics of crystallographic size-effects in metal matrix composites induced by thermo-mechanical loading. International Journal of Plas- ticity 42, 65 - 82.

Anand, L., 2004. Single-crystal elasto-viscoplasticity: application to texture evolution in polycrystalline metals at large strains. Computer Methods in Applied Mechanics and Engineering 193, 5359 - 5383. Advances in Computational Plasticity.

Anand, L., Ames, N.M., Srivastava, V., Chester, S.A., 2009. A thermo-mechanically coupled theory for large deformations of amorphous polymers. part i: Formulation. International Journal of Plasticity 25, 1474 - 1494.

Anand, L., Gurtin, M.E., Reddy, B.D., 2015. The stored energy of cold work, thermal annealing, and other thermodynamic issues in single crystal plasticity at small length scales. International Journal of Plasticity 64, 1 - 25.

Arsenlis, A., Parks, D.M., 2002. Modeling the evolution of crystallographic dislocation density in crystal plasticity. Journal of the Mechanics and Physics of Solids 50, 1979 - 2009.

Arsenlis, A., Parks, D.M., Becker, R., Bulatov, V.V., 2004. On the evolution of crystal- lographic dislocation density in non-homogeneously deforming crystals. Journal of the Mechanics and Physics of Solids 52, 1213 - 1246.

Bailey, J.E., 1960. Electron microscope observations on the annealing processes occurring in cold-worked silver. Philosophical Magazine 5, 833-842.

Balasubramanian, S., 1998. Doctoral thesis dissertation. Department of Mechanical Engi- neering, Massachusetts Institute of Technology .

Beck, P.A., Sperry, P.R., 1950. Strain induced grain boundary migration in high purity aluminum. J Appl Phys 21, 150-152.

Benzerga, A., Brchet, Y., Needleman, A., der Giessen, E.V., 2005. The stored energy of cold work: Predictions from discrete dislocation plasticity. Acta Materialia 53, 4765 - 4779.

Bever, M., Holt, D., Titchener, A., 1973. The stored energy of cold work. Progress in Materials Science 17, 5 - 177.

Ciulik, J., Taleff, E.M., 2009. Dynamic abnormal grain growth: A new method to produce single crystals. Scripta Mater 61, 895-898.

Franciosi, P., Zaoui, A., 1982. Multislip in f.c.c. crystals a theoretical approach compared with experimental data. Acta Metallurgica 30, 1627 - 1637.

Fried, E., Gurtin, M.E., 1994. Dynamic solid-solid transitions with phase characterized by an order parameter. Physica D 72, 287-308.

Godfrey, A., Jensen, D.J., Hansen, N., 2001. Recrystallisation of channel die deformed single crystals of typical rolling orientations. Acta Materialia 49, 2429 - 2440.

Gurtin, M.E., 2000. On the plasticity of single crystals: free energy, microforces, plastic- strain gradients. Journal of the Mechanics and Physics of Solids 48, 989 - 1036.

Gurtin, M.E., 2010. A finite-deformation, gradient theory of single-crystal plasticity with free energy dependent on the accumulation of geometrically necessary dislocations. Inter- national Journal of Plasticity 26, 1073 - 1096. Special Issue In Honor of Lallit Anand.

Gurtin, M.E., Anand, L., Lele, S.P., 2007. Gradient single-crystal plasticity with free energy dependent on dislocation densities. Journal of the Mechanics and Physics of Solids 55, 1853 - 1878.

Hosford, W., Fleischer, R., Backofen, W., 1960. Tensile deformation of aluminum single crystals at low temperatures. Acta Metallurgica 8, 187 - 199.

Hu, P., Liu, Y., Zhu, Y., Ying, L., 2016. Crystal plasticity extended models based on thermal mechanism and damage functions: Application to multiscale modeling of aluminum alloy tensile behavior. International Journal of Plasticity 86, 1 - 25.

Humphreys, M., Hatherly, F., 2004. Recrystallization and Related Annealing Phenomena (Second Edition). Elsevier.

Jamshidian, M., Rabczuk, T., 2014. Phase field modelling of stressed grain growth: Analyt- ical study and the effect of microstructural length scale. J. Comput. Phys. 261, 23.

Jamshidian, M., Thamburaja, P., Rabczuk, T., 2016. A multiscale coupled finite-element and phase-field framework to modeling stressed grain growth in polycrystalline thin films. Journal of Computational Physics 327, 779 - 798.

Jamshidian, M., Zi, G., Rabczuk, T., 2014. Phase field modeling of ideal grain growth in a distorted microstructure. Computational Materials Science 95, 663 - 671.

Kalidindi, S., 1992. Doctoral thesis dissertation. Department of Mechanical Engineering, Massachusetts Institute of Technology .

Kalidindi, S., Bronkhorst, C.A., Anand, L., 1992. Crystallographic texture evolution in bulk deformation processing of fcc metals. J Mech Phys Solids 40, 537-569.

Kashihara, K., Konishi, H., Shibayanagi, T., 2011. Strain-induced grain boundary migration in $1\ 1\ 2\ \langle 1\ 1\ 1\rangle /1\ 0\ 0\ \langle 0\ 0\ 1\rangle$ and $1\ 2\ 3\ \langle 6\ 3\ 4\rangle /1\ 0\ 0\ \langle 0\ 0\ 1\rangle$ aluminum bicrystals. Materials Science and Engineering: A 528, 8443 - 8450.

Lee, M., Lim, H., Adams, B., Hirth, J., Wagoner, R., 2010. A dislocation density-based single crystal constitutive equation. International Journal of Plasticity 26, 925 - 938.

Lele, S.P., Anand, L., 2009. A large-deformation strain-gradient theory for isotropic viscoplastic materials. International Journal of Plasticity 25, 420 - 453.

Lubarda, V.A., 2016. On the recoverable and dissipative parts of higher order stresses in strain gradient plasticity. International Journal of Plasticity 78, 26 - 43.

McBride, A., Bargmann, S., Reddy, B., 2015. A computational investigation of a model of single-crystal gradient thermoplasticity that accounts for the stored energy of cold work and thermal annealing. Computational Mechanics 55, 755-769.

Noell, J., Taleff, M., 2015. Dynamic abnormal grain growth in refractory metals. The Journal of The Minerals, Metals and Materials Society 67, 2642-2645.

Nouri, N., Ziaei-Rad, V., Ziaei-Rad, S., 2012. An approach for simulating microstructures of polycrystalline materials. Computational Mechanics 52, 181-192.

Popova, E., Staraselski, Y., Brahme, A., Mishra, R., Inal, K., 2015. Coupled crystal plasticity probabilistic cellular automata approach to model dynamic recrystallization in magnesium alloys. International Journal of Plasticity 66, 85 - 102. Plasticity of Textured Polycrystals In Honor of Prof. Paul Van Houtte.

Rosakis, P., Rosakis, A., Ravichandran, G., Hodowany, J., 2000. A thermodynamic internal variable model for the partition of plastic work into heat and stored energy in metals. Journal of the Mechanics and Physics of Solids 48, 581 - 607.

Sha, Y., Sun, C., Zhang, F., Patel, D., Chen, X., Kalidindi, S., Zuo, L., 2014. Strong cube recrystallization texture in silicon steel by twin-roll casting process. Acta Materialia 76, 106 - 117.

Shanthraj, P., Eisenlohr, P., Diehl, M., Roters, F., 2015. Numerically robust spectral methods for crystal plasticity simulations of heterogeneous materials. International Journal of Plasticity 66, 31 - 45. Plasticity of Textured Polycrystals In Honor of Prof. Paul Van Houtte.

Stojakovic, D., Doherty, R., Kalidindi, S., Landgraf, FernandoJ.G.v, p., 2008. Thermo-mechanical processing for recovery of desired $\langle 001 \rangle$ fiber texture in electric motor steels. Metallurgical and Materials Transactions A 39.

Thamburaja, P., Jamshidian, M., 2014. A multiscale taylor model-based constitutive theory describing grain growth in polycrystalline cubic metals. J. Mech. Phys. Solids 63, 1.

Theyssier, M., Driver, J., 1999. Recrystallization nucleation mechanism along boundaries in hot deformed al bicrystals. Materials Science and Engineering: A 272, 73 - 82.

Voyiadjis, G., Deliktas, B., 2010. Modeling of strengthening and softening in inelastic nanocrystalline materials with reference to the triple junction and grain boundaries using strain gradient plasticity. Acta Mechanica 213, 3-26.

Zhang, K., Holmedal, B., Hopperstad, O., Dumoulin, S., Gawad, J., Bael, A.V., Houtte,
P.V., 2015. Multi-level modelling of mechanical anisotropy of commercial pure aluminium
plate: Crystal plasticity models, advanced yield functions and parameter identification.
International Journal of Plasticity 66, 3 – 30. Plasticity of Textured Polycrystals In Honor
of Prof. Paul Van Houtte.