### Part 1

# Plastic Deformation of Crystalline Materials

---

Mechanics and Physics of Solids at Micro- and Nano-Scales,
First Edition. Edited by Ioan R. Ionescu, Sylvain Queyreau, Catalin R. Picu and Oguz Umut Salman.
© ISTE Ltd 2019. Published by ISTE Ltd and John Wiley & Sons, Inc.

# Homogeneous Dislocation Nucleation in Landau Theory of Crystal Plasticity

## 1.1. Introduction

Crystalline solids exhibit plasticity when macroscopic stresses exceed certain thresholds. It is well-known that plastic deformation of crystals is originated from the generation and motion of interacting dislocations, which evolve collectively in a complex energy landscape driven by the applied loading and long-range mutual interactions (Wilson 1954). Controlling crystal plasticity is needed in a variety of applications from metal hardening (Cottrell 2002) and fatigue failure (Irastorza-Landa *et al.* 2016) to nano-scale forming (Chen *et al.* 2010) and micro-pillar optimization (Pan *et al.* 2019; Zhang *et al.* 2017).

The current trend of manufacturing small-scale metallic crystalline materials calls for a deeper understanding of their mechanical behavior at micro- and nano-scales. At small scales, a smooth description of plastic flow breaks down, plastic response exhibits strong intermittency (Csikor *et al.* 2007; Devincre *et al.* 2008; Ispánovity *et al.* 2014), and mechanical properties of materials depend strongly on size, initial microstructure, quenched disorder, and prior deformation [see, e.g. Zhang *et al.* (2016, 2017)]. These properties render inadequate phenomenological continuum plasticity theory that adopts the smooth description of crystal plasticity (Forest 1998; Franciosi and Zaoui 1991) although it has been very successful in reproducing the most important plasticity phenomenology such as yield, hardening, and shakedown (Lubliner 2008). This inadequacy led to the use or

---

Chapter written by Oguz Umut SALMAN and Roberta BAGGIO.

development of other approaches going beyond the phenomenological continuum theory.

Molecular dynamics simulations that rely minimally on phenomenology are widely used to study crystal plasticity; the main advantage is that it is being formulated without any auxiliary hypotheses beyond the choice of interatomic potential (Bulatov *et al.* 1998; Moretti *et al.* 2011; Zepeda-Ruiz *et al.* 2017). However, the major drawback in molecular theories is the limitation on the accessible time and length scales, typically $10^4$–$10^6$ atoms (which is equivalent to a few nanometers) and a time span of a few nanoseconds (Baruffi *et al.* 2019). An intermediate discrete dislocation dynamics approach describes the dynamics of elastically interacting defects (dislocations) but it requires phenomenological rules describing short-range interactions, annihilation, and nucleation (Devincre *et al.* 2008; Queyreau *et al.* 2010; Shilkrot *et al.* 2004). A bridge between the discrete dislocation dynamics theory and molecular dynamics has recently emerged in the form of phase-field crystal theory, but such a detailed description still remains prohibitively expensive when one deals with a large number of dislocations (Elder *et al.* 2002; Salvalaglio *et al.* 2019; Skaugen *et al.* 2018); quasi-continuum numerical approaches that attempt to match phenomenological continuum theory with microscopic molecular dynamics at selective points face the same problem (Kochmann and Amelang 2016). Dynamics of many defects can be also described by an evolving continuum dislocation density; on the other hand, despite many interesting recent advances, a rigorous coarse-graining in a strongly interacting system of many dislocations still remains a major challenge (Acharya and Roy 2006; Chen *et al.* 2013; El-Azab 2000; Groma 2019; LeSar 2014; Sandfeld *et al.* 2011; Valdenaire *et al.* 2016; Xia and El-Azab 2015). A very powerful meso-scale approach is the phase-field method based on the Ginzburg–Landau theory and it has been successful in modeling dislocation dynamics by both employing the continuum microelasticity theory to describe the elastic interactions (Khachaturyan 1967) and incorporating the $\gamma$-surface into the crystalline energy to describe the core structures (Finel and Rodney 2000; Hunter *et al.* 2011; Rodney *et al.* 2003; Ruffini *et al.* 2017; Shen and Wang 2004; Wang *et al.* 2001; Zheng *et al.* 2018).

In this work, we use a recently developed complimentary mesoscopic approach (Baggio *et al.* 2019) that provides a nonlinear elasticity perspective on crystal plasticity and can be viewed as a far-reaching generalization of the Frenkel–Kontorova theory (Frenkel and Kontorova 1939). The approach is meso-scale in the sense it deals with macroscopic quantities such as stresses

and strains, and at the same time, it accounts properly for the exact symmetry of the underlying crystal structure. The aim is bridging fully atomistic descriptions and macroscopic theory based on continuum mechanics. The approach exploits the global invariance of the energy in the space of metric tensors compatible with geometrically nonlinear kinematics of crystal lattices. It takes the form of Landau theory, in which geometrically nonlinear metric tensor measuring the local deformation is the order parameter, with an infinite number of equivalent energy wells whose position is governed by the infinite symmetry group and corresponds to lattice-invariant shears. Therefore, plastic deformation can be described by an escape from the reference well when the crystal is loaded and dislocations appear as domain boundaries. This approach can be traced back to a few classic papers by J. L. Ericksen (1977, 1980, 1983) and follows subsequent development from the work of Conti and Zanzotto (2004). Similar approaches with periodic energies based on geometrically linear kinematics have also been used to study many aspects of crystal plasticity including, but not limited to, the description of dislocation cores and dislocation nucleation and intermittent nature of plastic flows (see Bonilla et al. 2007; Carpio and Bonilla 2003, 2005; Geslin et al. 2014; Kovalev et al. 1993; Landau 1994; Lomdahl and Srolovitz 1986; Minami and Onuki 2007; Onuki 2003; Plans et al. 2007; Salman and Truskinovsky 2011, 2012; Srolovitz and Lomdahl 1986).

In this work, we use the model to study dislocation nucleation in a homogeneously sheared 2D square crystal. We consider athermal dynamics that reduces to parametric minimization of our elastic energy function with infinite periodicity. Our results suggest that the crystal does not necessarily follow the imposed deformation path such that a remarkable collective dislocation nucleation scenario takes place. The motivation for this particular study is due to the fact that, at small scales, it is experimentally possible to manufacture crystals with very low heterogeneity sources such as grain boundaries, precipitates, voids, cracks, and so on. Similarly, in nano-crystalline materials or ceramics with very fine grains, classical nucleation sources, e.g. Frank–Read, are not effective and nucleation occurs not only heterogeneously at pre-existent grain boundaries, but also homogeneously in grain interiors (Gutkin and Ovid’ko 2008). These peculiarities make relevant to develop a detailed mathematical modeling for a better understanding of homogeneous dislocation nucleation that remains a challenge in materials science. Most of the previous works rely on molecular theories. For instance, molecular dynamics simulations have been used to investigate nucleation in an initially defect-free crystal during nano-indentation (Miller and Rodney

we consider linear transformations $\mathbf{F}$ that maps the original lattice $\mathbf{e}_a$ into the deformed one $\mathbf{f}_a$. The Born hypothesis that states the positions of the atoms within the crystal lattice follow the overall strain of the medium (Ericksen 2008) reads

$$
\mathbf{f}_a = \mathbf{F}\mathbf{e}_a \tag{1.3}
$$

After choosing the set of lattice vectors of a square lattice $\mathbf{e}_1 = \{1,0\}$ and $\mathbf{e}_2 = \{0,1\}$ as the reference state, and using equation [1.2] together with the Born hypothesis given by equation [1.3], one can observe that there are infinitely many homogeneous deformations, the so-called *lattice-invariant deformations* (Ericksen 2008) that solve the following equation:

$$
\mathbf{F}\mathbf{e}_a = m_{ab}\mathbf{e}_b \tag{1.4}
$$

such that $\mathbf{F} = m_{ab}\mathbf{e}_a \bigotimes \mathbf{e}_b$ and $\det \mathbf{F} = \mathbf{1}$. Thus, these deformations are naturally called lattice-invariant shears since

$$
\mathbf{F} = m_{ab}\mathbf{e}_a \bigotimes \mathbf{e}_b = \mathbf{1} + \mathbf{a} \bigotimes \mathbf{n} \tag{1.5}
$$

with $\mathbf{a} \cdot \mathbf{n} = 0$, which is a form associated with shearing deformations (Ericksen 2008). For instance, the point $\mathbf{S}_1$ in Figure 1.1 describes the reference square lattice. Another square lattice $\mathbf{S}_2$ in Figure 1.1 can be reached by a simple shear $\mathbf{1} + \mathbf{e}_1 \bigotimes \mathbf{e}_1^\perp$, where $\mathbf{e}_1^\perp$ is perpendicular to vector $\mathbf{e}_1$, whereas the square lattice $\mathbf{S}_3$ can be reached by the shear $\mathbf{1} + \mathbf{e}_2 \bigotimes \mathbf{e}_2^\perp$. Similarly, the point $\mathbf{T}_1$ corresponds to a triangular lattice with basis vectors being $\mathbf{e}_1 = \gamma\{1,0\}$ and $\mathbf{e}_2 = \{1/2,\sqrt{3}/2\}$, where $\gamma = (4/3)^{1/4}$, and possesses hexagonal symmetry. The other equivalent triangular lattices can be reached by performing shears of the form $\mathbf{1} \pm \mathbf{e}_1 \bigotimes \mathbf{e}_1^\perp$.

We note that the choice of $GL(2,\ Z)$ infinite group symmetry as the appropriate material symmetry in equation [1.1] enforces that the set of lattice vectors generating the same lattice that must have the same energy and the strain energy possesses an infinite number of stable phases, or minimizers, in three-dimensional metric space. The task of constructing a strain energy for a given deformation state satisfying the above invariance is rather complex. However, it can be achieved by noticing that there is a sub-domain in the infinite tensor space, the so-called *fundamental domain*, to which any metric $\mathbf{C}$ can be reduced in order to obtain its crystallographically (Ericksen 1983) equivalent reduced form $\tilde{\mathbf{C}}$ (metrics are said to have the "reduced form of Lagrange") by the so-called iterative procedure *Lagrange*

reduction (Conti and Zanzotto 2004; Engel 1986). The boundaries of the fundamental domain can be analytically found in 2D in terms of the components of the lattice metric $\mathbf{C}$ (Conti and Zanzotto 2004; Engel 1986). The colored region in Figure 1.1 corresponds to the fundamental domain and the black dot at the origin corresponds to the metric $\mathbf{C} = \mathbf{1}$ of the reference square lattice. The Lagrange reduction allows one to find the reduced form $\tilde{\mathbf{C}}$ of any metric $\mathbf{C}$ associated with an arbitrary shear deformation when it lies outside of the fundamental domain, and hence, we conclude that it is enough to construct a strain energy inside the fundamental domain:

$$
\varphi(\mathbf{C}) \equiv \varphi_{\mathbf{0}}(\tilde{\mathbf{C}}), \tag{1.6}
$$

where $\varphi_{\mathbf{0}}(\tilde{\mathbf{C}})$ is only defined inside the fundamental domain. In this work, we adopt the polynomial energy developed by Conti and Zanzotto (2004) for the study of reconstructive martensitic phase transformations that satisfies the continuity of elastic moduli on the boundaries of the fundamental domain. Also, see the work of Folkins (1991) for the general non-polynomial representation. Modular forms can also be used to construct infinitely periodic potentials [see Baggio *et al.* (2019)].

In this work, we choose a strain energy density $\varphi = \varphi_v + \varphi_d$, which decouples into a volumetric $\varphi_v(\det \mathbf{C})$ and an isochoric $\varphi_d[\mathbf{C}/(\det^{1/2} \mathbf{C})]$ parts. Since $\det \mathbf{C}$ is invariant under $GL(2, Z)$, the symmetry constraints concern only the isochoric part.

The minimal potential used in the following is given in the form (Conti and Zanzotto 2004):

$$
\varphi_{\boldsymbol{d}}(\tilde{\mathbf{C}})=\beta \Psi_{1}(\tilde{\mathbf{C}})+\Psi_{2}(\tilde{\mathbf{C}}) \tag{1.7}
$$

where $\varphi_1 = I_1^4 I_2 - 41 I_2^3/99 + 7I_1I_2I_3/66 + I_3^2/1056$, and $\varphi_2 = 4 I_2^3/11 + I_1^3I_3 - 8I_1I_2I_3/11 + 17 I_3^2/528$. The hexagonal invariants here have the structure:

$$
I_{1}=\frac{1}{3}\left(\tilde{C}_{11}+\tilde{C}_{22}-\tilde{C}_{12}\right), I_{2}=\frac{1}{4}\left(\tilde{C}_{11}-\tilde{C}_{22}\right)^{2}+\frac{1}{12}\left(\tilde{C}_{11}-\tilde{C}_{22}-4 \tilde{C}_{12}\right)^{2},
$$
$$
I_{3}=\left(\tilde{C}_{11}-\tilde{C}_{22}\right)^{2},\left(\tilde{C}_{11}+\tilde{C}_{22}-4 \tilde{C}_{12}\right)-\frac{1}{9}\left(\tilde{C}_{11}+\tilde{C}_{22}-4 \tilde{C}_{12}\right)^{3}
$$

The choice $\beta = -1/4$ enforces the square symmetry on the reference state while choosing $\beta = 4$, we bias the reference state toward hexagonal symmetry; the energy landscape for which the square crystal is the reference state, as

illustrated in Figure 1.6(a). The volumetric energy density is chosen in the form $\varphi_v(s)=\frac{\mu}{2}(s-1)^2$, where the coefficient $\mu$ plays the role of a bulk modulus. The choice of a polynomial is typical in the Landau type of theories, but our work remains qualitative in this sense. Quantitatively, adequate Landau potentials with correct periodicity can be indeed extracted from *ab initio* (say Density Functional Theory) calculations for affine configurations with subsequent application of the Cauchy–Born rule [see, e.g. Liu *et al.* (2010) Tadmor *et al.* (1996)].

![](./images/812696134496550914_1.jpg)

Figure 1.1. Partition of the section $\det \boldsymbol{C}=1$ of the space $\boldsymbol{C}$. Points $S_i$ represent the same square lattice and points $T_i$ represent the same triangular lattice. The colored region is the fundamental domain. For a color version of this figure, see www.iste.co.uk/ionescu/mechatronics.zip

### 1.2.1. Linear stability analysis

We first start by investigating the onset of plasticity by studying the loss of ellipticity condition that is related to the convexity of the function that describes the strain-energy density $\varphi(\boldsymbol{C})$ of the crystal. The mechanical equilibrium condition states that the divergence of the first Piola–Kirchhoff stress tensor $\boldsymbol{P}=\frac{\partial \varphi(\boldsymbol{C})}{\partial \mathbf{F}} \equiv \frac{\partial \varphi_0(\tilde{\boldsymbol{C}})}{\partial \mathbf{F}}$ vanishes in the absence of body forces:

$$
\nabla \cdot \mathbf{P}=0 \rightarrow P_{i J, J}=0, \tag{1.8}
$$

where the subscript after comma denotes the differentiation with respect to relevant coordinate and lower-case and upper-case indices refer to the deformed and reference configurations, respectively. Mechanical equilibrium condition, equation [1.8], can be written compactly in the form

$$
A_{i J K L} x_{L, i j}=0, \tag{1.9}
$$

where $\mathbf{A}$ is the fourth-order moduli tensor and $\mathbf{x}$ is the position vector at the deformed state and

$$
A_{i J k L}=\frac{\partial^{2} \varphi(\mathbf{C})}{\partial F_{i J} \partial F_{k L}} \equiv \frac{\partial^{2} \varphi^{0}(\breve{\mathbf{C}})}{\partial F_{i J} \partial F_{k L}}.\tag{1.10}
$$

After linearizing equation [1.9] for a small incremental deformation superimposed on an applied homogeneous deformation $\mathbf{F}_{A}$, we cast it into deformed coordinates, i.e. Eulerian coordinates, such that the incremental displacement vector $\mathbf{u}$ is now a function of the deformed position $\mathbf{u}(\mathbf{y})$ (Ogden 1984):

$$
A_{p i q j} u_{j, p q}=0,\tag{1.11}
$$

where the tensor $\mathbf{A}$ is related to $\mathbf{A}$ as

$$
A_{p i q j}=F_{p K} F_{q L} A_{K i L j},\tag{1.12}
$$

where $\mathbf{A}$ is the spatial fourth-order incremental moduli tensor. Following Ogden (1984) (see also Kumar and Parks 2015; Merodio and Ogden 2002), for incremental deformations in the form $\mathbf{u}=\boldsymbol{\eta} e^{i k \boldsymbol{\zeta} \cdot \mathbf{y}}$, where $\boldsymbol{\eta}$ is the amplitude vector, $k$ is the wave number, and $\boldsymbol{\zeta}$ is taken to be a unit vector $\boldsymbol{\zeta}=\{\cos (\xi), \sin (\xi)\}$, equation [1.11] can be written as

$$
[\mathbf{Q}(\boldsymbol{\zeta}) \boldsymbol{\eta}] \cdot \boldsymbol{\eta}=0,\tag{1.13}
$$

where $Q_{j l}(\boldsymbol{\zeta})=\mathrm{A}_{i j k l} \zeta_{i} \zeta_{k}$ is the Eulerian acoustic tensor. Now, we can express strong ellipticity condition as $\mathrm{A}_{i j k l} \zeta_{i} \zeta_{k} \eta_{j} \eta_{l}>0$, for all arbitrary unit vectors $\boldsymbol{\zeta}$ and $\boldsymbol{\eta}$. For a given deformed state, the loss of strong ellipticity first occurs when the following equation has solution $\boldsymbol{\zeta}$ such that

$$
\operatorname{det} \mathbf{Q}(\boldsymbol{\zeta})=0.\tag{1.14}
$$

The unit vector $\boldsymbol{\zeta}$ and the corresponding zero eigenvectors $\boldsymbol{\eta}$, for which the loss of ellipticity occurs, provide information on the nature of ensuing instability. The unit vector $\boldsymbol{\zeta}$ corresponds to the normal to the surface of the discontinuity of the deformation, whereas $\boldsymbol{\eta}$ describes the type of the deformation. We stress here that we do not enforce the incompressibility condition $\operatorname{det} \mathbf{F}=1$ in our model, and hence, we do not strictly have the orthogonality condition $\boldsymbol{\zeta} \cdot \boldsymbol{\eta}=0$. However, due to the penalization of

where $\mathbf{u}_{ij}$ denote the values of displacement at node $ij$. The discrete deformation gradient is then given by

$$
\mathbf{F}=\nabla \mathbf{y}=1+\mathbf{u}_{ij} \otimes \nabla N_{ij}. \tag{1.16}
$$

To minimize the energy functional $W=\int_{\Omega} \varphi$, we are using a variant of conjugate gradient optimization, the so-called L-BFGS algorithm (King 2009), which essentially selects solutions of the equilibrium equations:

$$
\partial W / \partial \mathbf{u}_{ij}=\int_{\Omega} \mathbf{P} \nabla N_{ij}=0, \tag{1.17}
$$

where $\mathbf{P}=\partial \varphi / \partial \mathbf{F}$, reachable through overdamped dynamics. We use the hard device boundary condition on each boundary, i.e. the positions of surface nodes are given by the applied shear deformation such that $\mathbf{y}=\mathbf{F}_{A} \mathbf{x}$. In our numerical calculations, we will study the homogeneous nucleation for a simple shear given by $\mathbf{F}_{A}=1+\alpha(\mathbf{a} \otimes \mathbf{n})$, where $\mathbf{a}=\{1,0\}$ and $\mathbf{n}=\{0,1\}$ and $\alpha$ is the amount of the applied shear.

### 1.4. Simulation results

#### 1.4.1. Stress field of a single-edge dislocation

In order to test the model, we first begin by calculating the stress field around an edge dislocation. To do so, we introduce a dislocation in the square crystal by using the classical isotropic displacement solution of an infinite edge dislocation with line direction along the $\{0,0,1\}$ axis and Burgers vector along the $\{1,0,0\}$ axis (Po *et al.* 2018) as the initial condition for the displacement field $\mathbf{u}_{ij}$ on the nodes of the finite elements. We then relaxed this configuration by conjugate gradient minimization (King 2009), of the total strain energy of the system with open boundary conditions, i.e. $\mathbf{P} \mathbf{N}=\mathbf{0}$, where $\mathbf{N}$ is the unit outward normal $\partial \Omega$ in the reference configuration. After relaxation, we obtain a single-edge dislocation trapped in the middle of the domain together with a step on the right free surface. Figures 1.2(a)-1.2(c) show the three components $\sigma_{xx}, \sigma_{yy}$, and $\sigma_{xy}$ of the Cauchy stress of the dislocation in the computational domain. We observe a qualitatively good agreement of contour shapes with those of analytical solution (Lothe and Hirth 2017). Figures 1.2(d)-1.2(f) show the corresponding stress profiles along the glide plane that match the classical

continuum $r^{-1}$ decay. Note also that the model resolves the core, which is regularized at a scale of the mesh. Finally, Figure 1.3 shows the core structure of a single dislocation in the configurational space of metric tensors, where blue dots are associated with the metric tensor of among finite elements. We observe that the dislocation core appears as a domain boundary between the two equivalent phases $\mathbf{S}_{1}$ and $\mathbf{S}_{2}$.

![](./images/812696134496550914_2.jpg)

Figure 1.2. Edge dislocation in a square lattice: (a)-(c) finite-element nodes with color indicating the level of different components of Cauchy stress $\sigma_{xx}$, $\sigma_{yy}$, and $\sigma_{xy}$; (d)-(f) stress profiles along the glide plane. System size $500 \times 500$. For a color version of this figure, see www.iste.co.uk/ionescu/mechatronics.zip

### 1.4.2. Dislocation annihilation

As previously mentioned in section 1.1, our model deals with dislocation reactions such as nucleation and annihilation without ad hoc rules in contrast with discrete dislocation dynamics modeling that needs phenomenological treatment. We illustrate here this behavior in the case of annihilation by introducing a dislocation dipole in the square crystal by superimposing the classical isotropic displacement solution of two infinite edge dislocations with

crystal is driven toward the phase $\mathbf{S}_{2}$ by the loading device. Note also that, interestingly, the former instability direction that points toward the phase $\mathbf{S}_{3}$ occurs for a slightly smaller $\alpha$.

![](./images/812696134496550914_3.jpg)

Figure 1.4. Dislocation annihilation in the physical space (a)-(d) and in the configurational space (e)-(h) where blue dots are associated with the metric tensor of different finite elements. For a color version of this figure, see
www.iste.co.uk/ionescu/mechatronics.zip

We compare the strain-stress relation of the crystal for the homogeneous state with one of the numerical solutions shown in Figure 1.7. The latter follows the homogeneous solution almost perfectly up to $\alpha_{c}$ predicted by the linear stability analysis, for which the loss of strong ellipticity occurs, leading to a large stress drop associated with the collective dislocation nucleation. Following the loss of stability, the perfect sheared crystal shown in Figure 1.8 evolves during the different stages of the first nucleation event, and Figures 1.8(b)-(e) show the non-equilibrium configurations during the minimization of the strain energy. The collective dislocation pattern that emerged after the stress drop (avalanche) is shown in Figure 1.8(f), where we observe the formation of dislocations on perpendicular slip planes. Recall here that our stability analysis predicted two almost simultaneous modes aligned with the slip directions in the deformed state, and the second one almost perpendicular with the deformed $\mathbf{e}_{1}$ is reached for a slightly smaller value of $\alpha$. This instability mode grows faster, as shown in Figure 1.8(b), although it points toward the well $\mathbf{S}_{3}$ not favored by the loading. Indeed, this

indicates an early dominance of the secondary slip mechanism. Note that the final spatial dislocation distribution is quasi-regular with pile-ups at the rigid boundaries together with the formation of characteristic junctions between dislocations on two slip planes blocking each other.

![](./images/812696134496550914_4.jpg)

Figure 1.5. Contour plot of the determinant of Eulerian acoustic tensor as a function of amount of shear α and orientation angle ζ for a simple shear. For a color version of this figure, see www.iste.co.uk/ionescu/mechatronics.zip

![](./images/812696134496550914_5.jpg)

Figure 1.6. (a) Energy landscape corresponding to potential 1.7 with β = 0.25. The energy level is blue – low and red – high. Black lines are the limit of linear stability for the homogeneous deformations. Green line is the loading path enforced by the loading device for a simple shear. (b) Level sets of the strain energy density around the point $T_1$, where we use the parametrization $C_{11}=1/Y$, $C_{22}=X^{2}+Y^{2}/Y$, and $C_{12}=X/Y$. For a color version of this figure, see www.iste.co.uk/ionescu/mechatronics.zip

![](./images/812696134496550914_6.jpg)

Figure 1.7. Strain–stress relation for the square crystal: black line is the Cauchy stress for the homogeneous state, whereas brown line corresponds to the numerical solution. Notice the large stress drop when $\alpha = \alpha_c$ for which the loss of strong ellipticity occurs. For a color version of this figure, see www.iste.co.uk/ionescu/mechatronics.zip

![](./images/812696134496550914_7.jpg)

Figure 1.8. Collective dislocation nucleation in the perfect crystal (a) following the loss of stability as it evolves during the different stages (b)–(e) of the nucleation. The final mechanical equilibrium configuration (f). For a color version of this figure, see www.iste.co.uk/ionescu/mechatronics.zip

To better characterize the simultaneous formation of dislocations on two perpendicular slip planes, we plot the level sets of the strain energy density on the surface $\det\mathbf{C} = 1$ in the vicinity of the triangular critical point $\mathbf{T}_1$ located on the boundary of the fundamental domain. The strain

energy density $\varphi$ at the point $\mathbf{T}_1$ has a shallow maximum surrounded by the three non-degenerate saddles $\mathbf{R}_1$, $\mathbf{R}_2$, and $\mathbf{R}_3$ describing rhombic lattices, see Figure 1.7. The flow of configurational points pointing initially toward such an unstable state (say, $\mathbf{T}_1$) will necessarily split into three streams directed toward the stable states (say, $\mathbf{S}_1$, $\mathbf{S}_2$, and $\mathbf{S}_3$). Note that the implied coupling of the plastic mechanisms would have to be postulated in the phenomenological plasticity theory (Ask et al. 2018; Forest 1998; Franciosi and Zaoui 1991); however, it can also be reconstructed from ab initio calculations [see Dezerald et al. (2014)].

### 1.5. Conclusion
To conclude, we have shown that nonlinear elasticity can be used to model crystal plasticity if the global invariance of the energy is taken into account. In such an approach, the complex geometry of the strongly deformed lattice is represented adequately with both physical and geometrical nonlinearities, shaping the infinitely periodic Landau energy. A thermal evolution in the regularized theory of this type can lead to temporal and spatial complexities. In particular, our study highlights the crucial role played in plastic deformation by the degenerate saddle points of the Landau potential, representing seemingly irrelevant, unstable crystallographic phases.

Immediate development of this framework would be accounted for crystal orientations and the extension of the theory to the three-dimensional case by considering the group $GL(3, \mathbb{Z})$. This will effectively extend the phase-field description to the case of multi-slip without extending the number of order parameters. Such a model will be able to capture the differences in flow behavior reported in crystals with hexagonal close-packed (HCP), face-centred cubic (FCC), and body-centred cubic (BCC) symmetries. Besides phenomena related to crystal plasticity, the proposed generalization of the Landau theory can also be used to describe mechanically- or thermally-driven irreversible reconstructive transitions, with their associated phenomena of compatibility-sensitive microstructure evolution.

### 1.6. References
Acharya, A. and Roy, A. (2006). Size effects and idealized dislocation microstructure at small scales: predictions of a phenomenological model of mesoscopic field dislocation mechanics: part I. Journal of the Mechanics and Physics of Solids, 54, 1687–1710.

Ask, A., Forest, S., Appolaire, B., Ammar, K., and Salman, O. U. (2018). A cosserat crystal plasticity and phase field theory for grain boundary migration. *Journal of the Mechanics and Physics of Solids*, 115, 167–194.

Baggio, R., Arbib, E., Biscari, P., Conti, S., Truskinovsky, L., Zanzotto, G., and Salman, O. U. (2019). Landau theory of crystal plasticity, available at: https://arxiv.org/abs/1904.03429.

Baruffi, C., Finel, A., Le Bouar, Y., Bacroix, B., and Salman, O. U. (2019). Overdamped langevin dynamics simulations of grain boundary motion. *Materials Theory*, 3(1), 4.

Bhattacharya, K. (1993). Comparison of the geometrically nonlinear and linear theories of martensitic transformation. *Continuum Mechanics and Thermodynamics*, 5(3), 205–242.

Bonilla, L. L., Carpio, A., and Plans, I. (2007). Dislocations in cubic crystals described by discrete models. *Physica A: Statistical Mechanics and its Applications*, 376, 361–377.

Bulatov, V., Abraham, F. F., Kubin, L., Devincre, B., and Yip, S. (1998). Connecting atomistic and mesoscale simulations of crystal plasticity. *Nature*, 391(6668), 669–672.

Carpio, A. and Bonilla, L. L. (2003). Edge dislocations in crystal structures considered as traveling waves in discrete models. *Physical Review Letters*, 90(13), 135502.

Carpio, A. and Bonilla, L. L. (2005). Discrete models of dislocations and their motion in cubic crystals. *Physical Review B Condensed Matter*, 71(13), 134105.

Chen, Y. S., Choi, W., Papanikolaou, S., Bierbaum, M., and Sethna, J. P. (2013). Scaling theory of continuum dislocation dynamics in three dimensions: self-organized fractal pattern formation. *International Journal of Plasticity*, 46, 94–129.

Chen, Y. S., Choi, W., Papanikolaou, S., and Sethna, J. P. (2010). Bending crystals: emergence of fractal dislocation structures. *Physical Review Letters*, 105(10), 105501.

Conti, S. and Zanzotto, G. (2004). A variational model for reconstructive phase transformations in crystals, and their relation to dislocations and plasticity. *Archive for Rational Mechanics and Analysis*, 173(1), 69–88.

Cottrell, A. H. (2002). Commentary: a brief view of work hardening. In *Dislocations in Solids*, vol. 11, Nabarro, F. R. N. and Duesbery, M. S. (eds.). Elsevier, Amsterdam, pp. vii–xvii.

Csikor, F. F., Motz, C., Weygand, D., Zaiser, M., and Zapperi, S. (2007). Dislocation avalanches, strain bursts, and the problem of plastic forming at the micrometer scale. *Science*, 318(5848), 251–254.

Devincre, B., Hoc, T., and Kubin, L. (2008). Dislocation mean free paths and strain hardening of crystals. *Science*, 320(5884), 1745–1748.

Dezerald, L., Ventelon, L., Clouet, E., Denoual, C., Rodney, D., and Willaime, F. (2014). Ab initio modeling of the two-dimensional energy landscape of screw dislocations in bcc transition metals. *Physical Review B Condensed Matter*, 89(2), 024104.

El-Azab, A. (2000). Statistical mechanics treatment of the evolution of dislocation distributions in single crystals. *Physical Review B Condensed Matter*, 61(18), 11956–11966.

Elder, K. R., Katakowski, M., Haataja, M., and Grant, M. (2002). Modeling elasticity in crystal growth. *Physical Review Letters*, 88(24), 245701.

Engel, P. (1986). *Geometric Crystallography: An Axiomatic Introduction to Crystallography*. Springer, The Netherlands.

Ericksen, J. L. (1977). Special topics in elastostatics. In *Advances in Applied Mechanics*, vol. 17. Elsevier, New York, pp. 189–244.

Ericksen, J. L. (1980). Some phase transitions in crystals. *Archive of Rational Mechanics and Analysis*, 73(2), 99–124.

Ericksen, J. L. (1983). The Cauchy and born hypothesis for crystals. MRC Technical Summary Report #2591.

Ericksen, J. L. (2008). On the Cauchy—born rule. *Mathematics and Mechanics of Solids*, 13(3–4), 199–220.

Finel, A., Le Bouar, Y., Gaubert, A., and Salman, O. U. (2010). Phase field methods: microstructures, mechanical properties and complexity. *Comptes Rendus Physique*, 11(3–4), 245–256.

Finel, A. and Rodney, D. (2000). Phase field methods and dislocations. MRS Fall Meeting, Boston, MA.

Folkins, I. (1991). Functions of two-dimensional Bravais lattices. *Journal of Mathematical Physics*, 32(7), 1965–1969.

Fonseca, I. (1987). Variational methods for elastic crystals. *Archive for Rational Mechanics and Analysis*, 97(3), 189–220.

Forest, S. (1998). Modeling slip, kink and shear banding in classical and generalized single crystal plasticity. *Acta Materialia*, 46(9), 3265–3281.

Franciosi, P. and Zaoui, A. (1991). Crystal hardening and the issue of uniqueness. *International Journal of Plasticity*, 7, 295–311.

Frenkel, J. and Kontorova, T. (1939). On the theory of plastic deformation and twinning. *Izvestiya Akademii Nauk SSR, Seriya Fizicheskaya*, 1, 137–149.

Geslin, P. A., Appolaire, B., and Finel, A. (2014). Investigation of coherency loss by prismatic punching with a nonlinear elastic model. *Acta Materialia*, 71, 80–88.

Lothe, J. and Hirth, J. (2017). *Theory of Dislocations*. Cambridge University Press, Cambridge.

Lubliner, J. (2008). *Plasticity Theory*. Courier Corporation, North Chelmsford, MA.

Merodio, J. and Ogden, R. (2002). Material instabilities in fiber-reinforced nonlinearly elastic solids under plane deformation. *Archives of Mechanics*, 54(5), 525–552.

Miller, R. E. and Rodney, D. (2008). On the nonlocal nature of dislocation nucleation during nanoindentation. *Journal of the Mechanics and Physics of Solids*, 56(4), 1203–1223.

Minami, A. and Onuki, A. (2007). Nonlinear elasticity theory of dislocation formation and composition change in binary alloys in three dimensions. *Acta Materialia*, 55(7), 2375–2384.

Moretti, P., Cerruti, B., and Miguel, M. C. (2011). Yielding and irreversible deformation below the microscale: surface effects and non-mean-field plastic avalanches. *PLoS ONE*, 6(6), e20418.

Ogata, S., Li, J., and Yip, S. (2002). Ideal pure shear strength of aluminum and copper. *Science*, 298(5594), 807–811.

Ogden, R. (1984). *Non-Linear Elastic Deformations*. John Wiley and Sons, Chichester.

Onuki, A. (2003). Plastic flow in two-dimensional solids. *Physical Review E, Statistical, Nonlinear, and Soft Matter Physics*, 68(6), 061502.

Pan, Y., Wu, H., Wang, X., Sun, Q., Xiao, L., Ding, X., Sun, J., and Salje, E. K. H. (2019). Rotatable precipitates change the scale-free to scale dependent statistics in compressed Ti nano-pillars. *Scientific Reports*, 9(1), 3778.

Pitteri, M. and Zanzotto, G. (2003). *Continuum Models for Phase Transitions and Twinnining*. Chapman & Hall, London.

Plans, I., Carpio, A., and Bonilla, L. L. (2007). Homogeneous nucleation of dislocations as bifurcations in a periodized discrete elasticity model. *Europhysics Letter*, 81(3), 36001.

Po, G., Lazar, M., Admal, N. C., and Ghoniem, N. (2018). A non-singular theory of dislocations in anisotropic crystals. *International Journal of Plasticity*, 103, 1–22.

Queyreau, S., Monnet, G., and Devincre, B. (2010). Orowan strengthening and forest hardening superposition examined by dislocation dynamics simulations. *Acta Materialia*, 58(17), 5586–5595.

Rodney, D., Le Bouar, Y., and Finel, A. (2003). Phase field methods and dislocations. *Acta Materialia*, 51(1), 17–30.

Ruffini, A., Le Bouar, Y., and Finel, A. (2017). Three-dimensional phase-field model of dislocations for a heterogeneous face-centered cubic crystal. *Journal of the Mechanics and Physics of Solids*, 105, 95–115.

Salman, O. U. (2009). Modeling of spatio-temporal dynamics and patterning mechanisms of martensites by phase-field and Lagrangian methods. PhD Thesis, Université Paris 6, Paris.

Salman, O. U., Muite, B., and Finel, A. (2019). Origin of stabilization of macrotwin boundaries in martensites. *European Physical Journal B*, 92(1), 20.

Salman, O. U. and Truskinovsky, L. (2011). Minimal integer automaton behind crystal plasticity. *Physical Review Letters*, 106(17), 175503.

Salman, O. U. and Truskinovsky, L. (2012). On the critical nature of plastic flow: one and two dimensional models. *International Journal of Engineering Science*, 59, 219–254.

Salvalaglio, M., Voigt, A., and Elder, K. R. (2019). Closing the gap between atomic-scale lattice deformations and continuum elasticity. *npj Computational Materials*, 5(1), 48.

Sandfeld, S., Hochrainer, T., Zaiser, M., and Gumbsch, P. (2011). Continuum modeling of dislocation plasticity: theory, numerical implementation, and validation by discrete dislocation simulations. *Journal of Materials Research and Technology*, 26(5), 623–632.

Shen, C. and Wang, Y. (2004). Incorporation of $\gamma$-surface to phase field model of dislocations: simulating dislocation dissociation in fcc crystals. *Acta Materialia*, 52(3), 683–691.

Shilkrot, L. E., Miller, R. E., and Curtin, W. A. (2004). Multiscale plasticity modeling: coupled atomistics and discrete dislocation mechanics. *Journal of the Mechanics and Physics of Solids*, 52(4), 755–787.

Skaugen, A., Angheluta, L., and Viñals, J. (2018). Separation of elastic and plastic timescales in a phase field crystal model. *Physical Review Letters*, 121(25), 255501.

Srolovitz, D. and Lomdahl, P. (1986). Dislocation dynamics in the 2-D Frenkel-Kontorova model. *Physica D: Nonlinear Phenomena*, 23(1–3), 402–412.

Tadmor, E. B., Ortiz, M., and Phillips, R. (1996). Quasicontinuum analysis of defects in solids. *Philosophical. Magazine A*, 73(6), 1529–1563.

Tschopp, M. A., Spearot, D. E., and McDowell, D. L. (2007). Atomistic simulations of homogeneous dislocation nucleation in single crystal copper. *Modelling and Simulation in Materials Science and Engineering*, 15(7), 693.

Valdenaire, P. L., Le Bouar, Y., Appolaire, B., and Finel, A. (2016). Density-based crystal plasticity: from the discrete to the continuum. *Physical Review B Condensed Matter*, 93(21), 214111.

Wang, Y. U., Jin, Y. M., Cuitiño, A. M., and Khachaturyan, A. G. (2001). Phase field microelasticity theory and modeling of multiple dislocation dynamics. *Applied Physics Letter*, 78(16), 2324–2326.

Wilson, A. J. C. (1954). Dislocations and plastic flow in crystals by A. H. Cottrell. *Acta Crystallographica*, 7(4), 384.

Xia, S. and El-Azab, A. (2015). Computational modelling of mesoscale dislocation patterning and plastic deformation of single crystals. *Modelling and Simulation in Materials Science and Engineering*, 23(5), 055009.

Zepeda-Ruiz, L. A., Stukowski, A., Oppelstrup, T., and Bulatov, V. V. (2017). Probing the limits of metal plasticity with molecular dynamics simulations. *Nature*, 550(7677), 492–495.

Zhang, H., Tersoff, J., Xu, S., Chen, H., Zhang, Q., Zhang, K., Yang, Y., Lee, C. S., Tu, K. N., Li, J., and Lu, Y. (2016). Approaching the ideal elastic strain limit in silicon nanowires. *Science Advances*, 2(8), e1501382.

Zhang, P., Salman, O. U., Zhang, J. Y., Liu, G., Weiss, J., Truskinovsky, L., and Sun, J. (2017). Taming intermittent plasticity at small scales. *Acta Materialia*, 128, 351–364.

Zheng, S., Zheng, D., Ni, Y., and He, L. (2018). Improved phase field model of dislocation intersections. *npj Computational Materials*, 4(1), 20.

Zhu, T., Li, J., Van Vliet, K. J., Ogata, S., Yip, S., and Suresh, S. (2004). Predictive modeling of nanoindentation-induced homogeneous dislocation nucleation in copper. *Journal of the Mechanics and Physics of Solids*, 52(3), 691–724.

Zimmerman, J. A., Kelchner, C. L., Klein, P. A., Hamilton, J. C., and Foiles, S. M. (2001). Surface step effects on nanoindentation. *Physical Review Letters*, 87(16), 165507.