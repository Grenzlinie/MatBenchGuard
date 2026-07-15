Accepted Manuscript

Towards a thermo-magneto-mechanical coupling framework for magneto-rheological elastomers

Markus Mehnert, Mokarram Hossain, Paul Steinmann

| | |
|---|---|
| PII: | S0020-7683(17)30386-4 |
| DOI: | 10.1016/j.ijsolstr.2017.08.022 |
| Reference: | SAS 9701 |

| | |
|---|---|
| To appear in: | *International Journal of Solids and Structures* |
| Received date: | 29 March 2017 |
| Revised date: | 28 July 2017 |
| Accepted date: | 21 August 2017 |

Please cite this article as: Markus Mehnert, Mokarram Hossain, Paul Steinmann, Towards a thermo-magneto-mechanical coupling framework for magneto-rheological elastomers, *International Journal of Solids and Structures* (2017), doi: 10.1016/j.ijsolstr.2017.08.022

![](./images/813107845410062337_1.jpg)

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Towards a thermo-magneto-mechanical coupling framework for magneto-rheological elastomers

Markus Mehnert$^{a}$, Mokarram Hossain$^{b,*}$, Paul Steinmann$^{a}$

$^{a}$Chair of Applied Mechanics, University of Erlangen-Nuremberg, Paul-Gordan Strasse 3, 91054 Erlangen, Germany
$^{b}$Zienkiewicz Centre for Computational Engineering, College of Engineering, Bay Campus, Swansea University, Swansea, UK

## Abstract
Magnetorheological elastomers (MREs) are a relatively new class of smart materials that can undergo large deformations resulting from external magnetic excitation. These are promising candidates in producing sensors and actuators. Due to their inherent chemical compositions, most polymeric materials are highly susceptible to temperature. While performing experiments on MREs that are exposed to magneto-mechanically coupled loads, maintaining a constant temperature profile is a non-trivial task for various reasons, e.g., i) experiments need to be performed in a temperature chamber that can maintain a prescribed temperature throughout a test, and ii) additional temperature gradients can be generated internally. In this paper, a thermo-magneto-mechanically coupled constitutive model is devised that is based on the total energy approach frequently used in MREs modelling and computation. Relevant constitutive equations are derived exploiting basic laws of thermodynamics that result in a thermodynamically consistent formulation. We demonstrate the performance of the proposed thermo-magneto-mechanically coupled framework with the help of two non-homogeneous boundary value problems. In both problems an axisymmetric cylindrical tube is deformed under thermo-magneto-mechanically coupled loads. In the first example the mechanical deformation is a combination of axial stretch and radial inflation whereas in the second example the cylinder is put under a mechanical load of torsion around the cylinder axis combined with an axial stretch. In both examples a circumferential magnetic field and a radial temperature gradient are applied. The results capture various thermo-magneto-mechanical couplings with the formulation proposed for MRE.

**Keywords:** Magneto-elasticity, magneto-thermo-mechanical coupled problem, nonlinear elasticity, thermo-mechanical couplings

---

## 1. Introduction
In the recent years a growing interest in the study of so-called smart materials in the finite deformations regime emerged. In this context especially magnetorheological elastomers (MREs) are a promising class of materials. MREs can change their mechanical behavior in response to external excitations by a magnetic field. To alter their mechanical characteristics under an external field makes them interesting candidates especially for applications such as tunable stiffness and damping devices. One of the key advantages of MREs over other smart or functional materials is that they work by contact-free excitations, cf. [11, 12].

---

*Corresponding author. Tel.: +44 07482959957
Email addresses: markus.mehnert@ltm.uni-erlangen.de (Markus Mehnert), mokarram.hossain@swansea.ac.uk (Mokarram Hossain), paul.steinmann@ltm.uni-erlangen.de (Paul Steinmann)

Preprint submitted to *International Journal of Solids and Structures*
August 23, 2017

Magneto-active elastomers have been proposed to be used in robotic and vibration control applications [1, 29, 32, 35, 36, 37, 38, 49, 81, 82]. MREs are filled with field-responsive micro or nano-sized iron particles. During the preparation of such composites, magnetically permeable particles are first mixed into a liquid monomer system. Subsequently the mixture is set to rest in order to cross-link with time. Depending on the timing of application of the magnetic field during the manufacturing of MREs two types of materials can be produced. If the external magnetic field is absent during the curing process of the composites the particles are more or less randomly distributed and form isotropic MREs. If an external magnetic field is applied during the curing process, it results in a relative alignment of the magneto-active particles that remain locked within chains when the body solidifies [14, 28, 47, 35, 79, 80, 41, 42]. These produce transversely isotropic MREs [5, 14, 28, 47, 35, 79, 80]. For the preparation and experimental characterization of iron-filled elastomers, some seminal works can be consulted, e.g. [47], [35], [80], [17, 48].

Although the research exploring various aspects of MREs has been a growing field of interest in recent years, the mathematical foundations of the coupling of electromagnetic fields in finite strains date back to early 1960's and are well documented in some earlier publications, see for example the works of Pao [58] and Eringen and Maugin [31]. In a series of pioneering papers and monographs, Dorfmann and Ogden developed a constitutive framework for the coupling of magnetic and mechanical fields which is based on the so-called total energy [22, 23, 24]. Their modelling framework mainly assumes isotropy of the polymeric composites. It has been shown that the total stress tensor and the magnetic field can be expressed as simple derivatives of the total energy function with respect to the deformation gradient and the magnetic induction [23, 24, 25]. They presented analytical solutions of some classical non-homogeneous boundary value problems in which it has been shown that any of the magnetic variables, i.e. the magnetic induction vector, the magnetic field vector or the magnetization vector can be used as an independent variable in the problem formulation. A significant amount of contributions on the modelling of magneto-mechanically coupled problems were published by Bustamante [5], Bustamante, Dorfmann and Ogden [24, 9] extending the work of Dorfmann and Ogden [3, 22, 23, 24, 25] by a constitutive model for transversely isotropic MREs. Despite these seminal contributions, there is no work, to the best of the authors' knowledge, that relates to temperature-dependent behavior of magneto-mechanical coupled polymers.

All modelling strategies described above are based on the so-called strain invariant-based approach where invariants do not have any direct physical meaning. Aiming to develop constitutive models that can be based on physically meaningful invariants, Shariff [68, 69, 70], Bustamante and Shariff [7] proposed a set of spectral invariants. The main idea of their approach is to construct a set of spectral invariants whose elements are the principal stretches and the square of the dot product of the eigen-directions of the right stretch tensor. They formulate a new class of spectral invariants to model not only the behavior of transversely isotropic composites but also of anisotropic MREs [7]. They claim that the new invariants have clear physical meaning and thus can be more attractive in order to find elegant expressions for the total energy function by fitting experimental data.

Variational formulations for the governing equations of magnetic field-responsive composites, a prerequisite for numerical computations involving magneto-mechanical problems, are proposed by Bustamante et al. [6, 8]. Another variational formulation on MREs is proposed by Vogel [72] and Vogel et al. [74], where three-field formulations are proposed by considering a nearly incompressible behavior of the bulk rubber-like materials. Recent experimental evidence [65] suggests that iron-filled polymeric composites manufactured under a magnetic field during the curing process do not necessarily form composites where all iron

particles are aligned in the same direction. Rather they form a dispersion type anisotropy with distributed chains. Hence, Saxena et al. [65] proposed a magneto-active polymer model with a dispersed chain-like micro structure and demonstrated some numerical examples by finite element calculations. Very recently, Pelteret et al. [59] devised a computational framework for quasi-incompressible electro- and magneto-elastic solids immersed in free space.

A general thermodynamically consistent constitutive framework for thermo-magneto-mechanically coupled phenomena is devised in this contribution. We adopt a standard assumption for the heat capacity being a constant. Successive integration and application of appropriate boundary conditions result in a general- ized formulation for the total thermo-magneto-mechanical energy function in an additive form where the magneto-mechanically coupled effect is linearly scaled with the temperature. In order to demonstrate the validity of the proposed coupled framework, a classical non-homogeneous boundary value problem, i.e. the extension and inflation of an axisymmetric cylindrical tube, is solved analytically. A magnetic field is ap- plied in the azimuthal direction by assuming a current flowing along the axial direction of the hollow tube. Furthermore, heat flow occurs in the thick-walled hollow tube along the radial direction in addition to the magneto-mechanical load. To the best of the authors' knowledge, this benchmark problem, that has been widely used not only in finite strain elasticity but also in electro-/magneto-elastic problems, is not solved yet in the literature for the thermo-magneto-mechanically load case.

This paper is organized as follows. In Section 2, the finite strain theory of nonlinear magneto-elasticity is reviewed. Thereby relevant nonlinear kinematics and balance laws both in the spatial and the material configuration are derived. In Section 3, the main focus of this contribution, a thermo-magneto-mechanical coupled framework is discussed. Furthermore, coupled constitutive equations based on the total energy function, and the modified heat equation for thermo-magneto-mechanically coupled problems are presented in this chapter. A total energy function that obeys the second law of thermodynamics is proposed where the temperature is incorporated as an independent variable in addition to the magnetic field and the deformation gradient. Two non-homogeneous boundary value problems under thermo-magneto-mechanical loads are solved analytically in order to substantiate the proposed formulation. The results are elaborated in Section 4. Section 5 concludes the paper with a summary and an outlook to future works.

## 2. Basics of non-linear magneto-mechano-statics

### 2.1. Kinematics

Since polymeric materials typically can undergo large deformations we distinguish between the material configuration $\mathcal{B}_{0}$ and the spatial configuration $\mathcal{B}_{t}$. To describe the deformation of the body material coordi nates $\boldsymbol{X}$ in $\mathcal{B}_{0}$ are mapped through the nonlinear deformation map $\chi$ onto the spatial coordinates $\boldsymbol{x}$ in $\mathcal{B}_{t}$. In general all quantities that refer to the material configuration $\mathcal{B}_{0}$ are denoted by upper case letters or by the subscript $[\bullet]_{0}$. Quantities referring to the spatial configuration $\mathcal{B}_{t}$ are denoted by lower case letters or by the subscript $[\bullet]_{t}$. The deformation gradient $\boldsymbol{F}$ is defined as the gradient of the deformation map $\chi$ with respect to the material coordinates $\boldsymbol{X}$, i.e.

$$
\boldsymbol{F}:=\operatorname{Grad} \chi ; \quad J:=\operatorname{det} \boldsymbol{F}>0, \tag{1}
$$

where $J$ is the Jacobian determinant of the deformation gradient that has to be positive in order to avoid any unphysical deformations. Moreover we introduce the left and right Cauchy-Green tensors $\boldsymbol{b}$ and $\boldsymbol{C}$,

respectively, as

$$
\boldsymbol{b}:=\boldsymbol{F} \boldsymbol{F}^{T}, \quad \boldsymbol{C}:=\boldsymbol{F}^{T} \boldsymbol{F}. \tag{2}
$$

### 2.2. Balance laws
#### 2.2.1. Spatial configuration
Within a material body, the relation between the magnetic field $\mathbb{h}$ and the magnetic induction $\mathbb{b}$ is given in terms of the magnetization $\mathbb{m}$ and the magnetic permeability in vacuum $\mu_{0}$

$$
\mathbb{b}=\mu_{0}[\mathbb{h}+\mathbb{m}], \quad \text { in } \mathcal{B}_{t}. \tag{3}
$$

Note that in free space the above relation degenerates to $\mathbb{b}=\mu_{0} \mathbb{h}$. If we assume the magnetostatic case where the free current density is zero and the electric displacement is constant in time, Ampère's law together with the absence of magnetic monopoles yields

$$
\operatorname{curl} \mathbb{h}=\mathbf{0}, \quad \operatorname{div} \mathbb{b}=0 \quad \text { in } \mathcal{B}_{t}, \tag{4}
$$

where curl and div denote the corresponding differential operators with respect to the position vectors $x$ in $\mathcal{B}_{t}$. Equation $(4)_{1}$ is satisfied automatically if the magnetic field $\mathbb{h}$ is derived from a scalar potential $[72,54,50,62,77,78]$. Hence, the definition of $\mathbb{h}$ is here

$$
\mathbb{h}:=-\operatorname{grad} \varphi, \tag{5}
$$

where $\operatorname{grad} \varphi$ is the gradient of the magnetic scalar potential $\varphi$ with respect to the spatial coordinates. The matter-field interaction is captured by the ponderomotive body force in terms of the magnetization and the gradient of the magnetic induction, cf. [72, 54, 6]

$$
\boldsymbol{b}_{t}^{\text {pon }}:=\mathbb{m} \cdot \nabla \mathbb{b}. \tag{6}
$$

The ponderomotive body force can be expressed as the divergence of a corresponding ponderomotive stress

$$
\boldsymbol{\sigma}^{\text {pon }} \text { with } \operatorname{div} \boldsymbol{\sigma}^{\text {pon }}=\boldsymbol{b}_{t}^{\text {pon }}, \tag{7}
$$

which can further be decomposed into a non-symmetric magnetization stress [72,73,74] and the symmetric Maxwell stress

$$
\boldsymbol{\sigma}^{\text {pon }}=\boldsymbol{\sigma}^{\text {mag }}+\boldsymbol{\sigma}^{\max }, \tag{8}
$$

where

$$
\boldsymbol{\sigma}^{\mathrm{mag}}=[\mathbb{m} \cdot \mathbb{b}] \boldsymbol{i}-\mathbb{m} \otimes \mathbb{b}, \quad \boldsymbol{\sigma}^{\max }=-M_{t} \boldsymbol{i}+\frac{1}{\mu_{0}} \mathbb{b} \otimes \mathbb{b}. \tag{9}
$$

In Equation (9) $M_{t}=\frac{1}{2 \mu_{0}}[\mathbb{b} \cdot \mathbb{b}]$ is the free field magnetic energy density per unit spatial volume and $\boldsymbol{i}$ is the second order identity tensor in the spatial configuration. Note that $M_{t}$ is parameterized in the magnetic induction. In the absence of matter, the magnetization $\mathbb{m}$ and, consequently, the magnetization stress $\boldsymbol{\sigma}^{\text {mag }}$ vanish whereas the Maxwell stress satisfies a divergence free condition, i.e.

$$
\operatorname{div} \boldsymbol{\sigma}^{\max }=\mathbf{0}. \tag{10}
$$


By incorporating the ponderomotive body force $\boldsymbol{b}_t^{\text{pon}}$ into the balance of linear momentum we obtain

$$\operatorname{div} \boldsymbol{\sigma}+\boldsymbol{b}_{t}^{\mathrm{pon}}+\boldsymbol{b}_{t}=\operatorname{div} \boldsymbol{\sigma}^{\mathrm{tot}}+\boldsymbol{b}_{t}=\mathbf{0} \quad \text { in } \mathcal{B}_{t},\tag{11}$$

where $\boldsymbol{b}_t$ is the mechanical body force and $\boldsymbol{\sigma}^{\text{tot}}$ is the total Cauchy-type symmetric stress tensor as introduced by Dorfmann and Ogden [22, 23, 24, 25]. The total Cauchy stress $\boldsymbol{\sigma}^{\text{tot}}$ consists of both the mechanical and the ponderomotive stress

$$\boldsymbol{\sigma}^{\mathrm{tot}}=\boldsymbol{\sigma}+\boldsymbol{\sigma}^{\mathrm{pon}}.\tag{12}$$

For the boundary conditions on $\partial \mathcal{B}_{t}=\partial \mathcal{B}_{t}^{\chi} \cup \partial \mathcal{B}_{t}^{\mathfrak{t}}$ with $\partial \mathcal{B}_{t}^{\chi} \cap \partial \mathcal{B}_{t}^{\mathfrak{t}}=\emptyset$, Dirichlet-type conditions for the deformation map $\boldsymbol{\chi}$ are prescribed as

$$\boldsymbol{\chi}=\boldsymbol{\chi}^{\mathrm{p}}, \quad \text { on } \partial \mathcal{B}_{t}^{\chi}.\tag{13}$$

On the part of the boundary $\partial \mathcal{B}_{t}^{\mathfrak{t}}$ mechanical tractions $\boldsymbol{t}_{t}^{\mathrm{p}}$ are prescribed and result in the Neumann-type boundary condition

$$[\![ \boldsymbol{\sigma}^{\mathrm{tot}} ]\!] \cdot \boldsymbol{n}=-\boldsymbol{t}_{t}^{\mathrm{p}}, \quad \text { on } \partial \mathcal{B}_{t}^{\mathfrak{t}},\tag{14}$$

where the jump $[\![\bullet]\!]$ is defined as the difference of a certain quantity with regard to the outward pointing normal vector $\boldsymbol{n}$, i.e.: $[\![\bullet]\!]=\{\bullet\}^{\text{out}}-\{\bullet\}^{\text{in}}$. The respective jump conditions associated with the magnetic quantities are defined as

$$\boldsymbol{n} \cdot [\![\mathbb{b}]\!]=0 \quad \text { and } \quad \boldsymbol{n} \times [\![\mathfrak{h}]\!]=\hat{\mathfrak{j}}^{f}\tag{15}$$

where $\hat{\mathfrak{j}}^{f}$ denotes the free surface current density [73]. With the assumption, that no free surface currents flow over $\partial \mathcal{B}$ we can derive, in combination with Equation (5), the continuity condition for the magnetic scalar potential,

$$[\![\varphi]\!]=0\tag{16}$$

### 2.2.2. Material configuration

In this section, we transform various magnetic quantities from the spatial configuration $\mathcal{B}_{t}$ to the material configuration $\mathcal{B}_{0}$. The magnetic field, the magnetic induction and the magnetization in the material setting can be computed, respectively, as

$$\mathbb{H}=\mathfrak{h} \boldsymbol{F}, \quad \mathbb{M}=\mathfrak{m} \boldsymbol{F}, \quad \mathbb{B}=J \mathbb{b} \boldsymbol{F}^{-T}.\tag{17}$$

Similarly, the magneto-static Maxwell equations in the material configuration are defined as

$$\operatorname{Curl} \mathbb{H}=\mathbf{0}, \quad \operatorname{Div} \mathbb{B}=0,\tag{18}$$

where Curl and Div denote the corresponding differential operators with respect to the position vectors $\boldsymbol{X}$ in $\mathcal{B}_{0}$. Equation $(18)_{1}$ will be satisfied if the magnetic field $\mathbb{H}$ is derived from a scalar potential such that

$$\mathbb{H}=-\operatorname{Grad} \varphi, \quad \text { in } \mathcal{B}_{0}.\tag{19}$$

In the bulk $\mathbb{B}, \mathbb{H}$ and $\mathbb{M}$ are connected by the relation, cf. [72]

$$\mathbb{B}=J \mu_{0} \boldsymbol{C}^{-1}[\mathbb{H}+\mathbb{M}] \quad \text { in } \mathcal{B}_{0}.\tag{20}$$

Note that in free space the above relation reduces to $\mathbb{B}=J \mu_{0} \boldsymbol{C}^{-1} \mathbb{H}$. The total Cauchy stress $\boldsymbol{\sigma}^{\text{tot}}$ defined in the spatial configuration can be transformed into its material counterparts, i.e. the total Piola and Piola-

Kirchhoff stress tensors $\boldsymbol{P}^{\text{tot}}$ and $\boldsymbol{S}^{\text{tot}}$, respectively, as

$$
\boldsymbol{P}^{\mathrm{tot}}=J \boldsymbol{\sigma}^{\mathrm{tot}} \boldsymbol{F}^{-T}, \quad \boldsymbol{S}^{\mathrm{tot}}=J \boldsymbol{F}^{-1} \boldsymbol{\sigma}^{\mathrm{tot}} \boldsymbol{F}^{-T}.\tag{21}
$$

Similar to the total Cauchy stress, the total Piola stress can be decomposed into the mechanical Piola stress $\boldsymbol{P}$ and the ponderomotive Piola stress $\boldsymbol{P}^{\text{pon}}$

$$
\boldsymbol{P}^{\mathrm{tot}}=\boldsymbol{P}+\boldsymbol{P}^{\mathrm{pon}}=\boldsymbol{P}+\boldsymbol{P}^{\mathrm{mag}}+\boldsymbol{P}^{\mathrm{max}},\tag{22}
$$

with the magnetization Piola stress $\boldsymbol{P}^{\text{mag}}$ and the Maxwell Piola stress $\boldsymbol{P}^{\text{max}}$ that can be expressed as

$$
\boldsymbol{P}^{\mathrm{mag}}=[\mathbb{M} \cdot \mathbb{B}] \boldsymbol{F}^{-T}-\mathfrak{m} \otimes \mathbb{B}, \quad \text { and } \quad \boldsymbol{P}^{\mathrm{max}}=-M_{0} \boldsymbol{F}^{-T}+\frac{1}{\mu_{0}} \mathbb{b} \otimes \mathbb{B}.\tag{23}
$$

In Equation (23) $M_{0}=\frac{1}{2 \mu_{0}} J^{-1} \mathbb{B} \cdot[\boldsymbol{C} \mathbb{B}]$ denotes the magneto-static energy density per unit volume in the material configuration. The balance of linear momentum (12) together with the corresponding Neumann boundary conditions and the divergence free condition for the Maxwell stress in free space (10) are transformed to

$$
\operatorname{Div} \boldsymbol{P}^{\mathrm{tot}}+\boldsymbol{b}_{0}=\mathbf{0} \quad \text { with } \quad \llbracket \boldsymbol{P}^{\mathrm{tot}} \rrbracket \cdot \boldsymbol{N}=-\boldsymbol{t}_{0}^{p} \quad \text { on } \partial \mathcal{B}_{0}^{t} \text { and } \operatorname{Div} \boldsymbol{P}^{\mathrm{max}}=\mathbf{0}.\tag{24}
$$

The jump conditions are translated to the material configuration such that

$$
\boldsymbol{N} \cdot \llbracket \mathbb{B} \rrbracket=0 \quad \text { and } \quad \boldsymbol{N} \times \llbracket \mathbb{H} \rrbracket=\hat{\mathbb{J}}^{f}\tag{25}
$$

where $\hat{\mathbb{J}}^{f}$ denotes the free surface current density in the material configuration [73]. In transforming the boundary conditions from the spatial configuration to the material configuration, conversions $\hat{\mathbb{J}}^{f} d A=\hat{\mathfrak{J}}^{f} d a$ and $\boldsymbol{t}_{0}^{p} d A=\boldsymbol{t}_{t}^{p} d a$ are used where the area element $d A$ relates to the material configuration and $d a$ is the respective area element in the spatial configuration.

### 3. Non-linear thermo-magneto-elasticity

#### 3.1. Constitutive equations

In the sequel it proves convenient to treat the magnetic field rather than the magnetic induction as the primary magnetic variable. To this end we first introduce the free field magnetic complementary energy per unit volume in the material configuration as

$$
M_{0}^{*}(\mathbb{H} ; \boldsymbol{F}):=\min _{\mathbb{B}}\left\{M_{0}-\mathbb{H} \cdot \mathbb{B}\right\}=-\frac{1}{2} J \mu_{0} \mathbb{H} \cdot\left[\boldsymbol{C}^{-1} \mathbb{H}\right].\tag{26}
$$

Then the energy density $\Psi$ per unit volume in $\mathcal{B}_{0}$ is parameterized in the deformation gradient, the absolute temperature $\Theta$ and the magnetic field

$$
\Psi=\tilde{\Psi}(\boldsymbol{F}, \Theta, \mathbb{H}).\tag{27}
$$

Dorfmann and Ogden [22, 23] have demonstrated that the concept of the so-called total energy function is useful for magneto-elastic constitutive modelling. Hence, we express the total energy function as

$$
\Omega(\boldsymbol{F}, \Theta, \mathbb{H})=\Psi(\boldsymbol{F}, \Theta, \mathbb{H})+M_{0}^{*}(\boldsymbol{F}, \mathbb{H}).\tag{28}
$$


In the absence of a free current density, the second law of thermodynamics in the form of the Clausius-Duhem inequality eventually leads to [20, 55]

$$
\delta_{0}=\boldsymbol{P}^{\mathrm{tot}}: \dot{\boldsymbol{F}}-\mathbb{B} \cdot \dot{\mathbb{H}}-\dot{\Omega}-H \dot{\Theta}-\boldsymbol{Q} \cdot \frac{\operatorname{Grad}(\Theta)}{\Theta} \geq 0,\qquad(29)
$$

where $H$ is the entropy and $\boldsymbol{Q}$ is the heat flux vector defined in the material configuration that can be transformed to the spatial form via $J \boldsymbol{q}=\boldsymbol{F} \boldsymbol{Q}$. Now, we can express the constitutive relations in terms of the total energy as

$$
\boldsymbol{P}^{\mathrm{tot}}=\frac{\partial \Omega}{\partial \boldsymbol{F}}, \quad \text { with } \quad \boldsymbol{P}^{\max }=\frac{\partial M_{0}^{*}}{\partial \boldsymbol{F}}, \quad \mathbb{B}=-\frac{\partial \Omega}{\partial \mathbb{H}}, \quad H=-\frac{\partial \Omega}{\partial \Theta},\qquad(30)
$$

see, e.g. [72] for further details. After applying the Coleman-Noll argumentation [20] to Equation (29), the reduced conductive dissipation power density reads

$$
\delta_{0}^{\mathrm{con}}=-\boldsymbol{Q} \cdot \frac{\operatorname{Grad}(\Theta)}{\Theta} \geq 0.\qquad(31)
$$

Moreover, in many cases, expressions for the total stress have to be written either in terms of the total Cauchy stress or in terms of the total Piola-Kirchhoff stress tensor , i.e.

$$
\boldsymbol{\sigma}^{\mathrm{tot}}=J^{-1} \frac{\partial \Omega}{\partial \boldsymbol{F}} \boldsymbol{F}^{T}, \quad \boldsymbol{S}^{\mathrm{tot}}=2 \frac{\partial \Omega}{\partial \boldsymbol{C}}.\qquad(32)
$$

We assume the magneto-mechanical behavior of the material to be incompressible at constant temperature. Therefore in order to capture the temperature induced deformation while simultaneously assuring incompressibility of the material behavior at constant temperature following [27] we introduce a multiplicative decomposition of the deformation gradient. Here we distinguish between a magneto-mechanical part $\boldsymbol{F}_{M}$ and a thermal part $\boldsymbol{F}_{\Theta}$ capturing thermal expansion. In terms of the deformation gradients and the corresponding Jacobians this decomposition reads

$$
\boldsymbol{F}=\boldsymbol{F}_{M} \boldsymbol{F}_{\Theta}, \quad J=J_{M} J_{\Theta}.\qquad(33)
$$

Thus the definitions of the total stress (32) can be reformulated as

$$
\boldsymbol{\sigma}^{\mathrm{tot}}=\frac{\partial \Omega}{\partial \boldsymbol{F}} \boldsymbol{F}^{T}-p \boldsymbol{i}, \quad \boldsymbol{S}^{\mathrm{tot}}=2 \frac{\partial \Omega}{\partial \boldsymbol{C}}-p \boldsymbol{C}^{-1},\qquad(34)
$$

where $p$ is a Lagrange multiplier associated with the incompressibility constraint $J_{M}=1$ [9].

### 3.2. Energy function
At this stage, a thermo-magneto-mechanically coupled energy function is required where, besides the mechanical and magnetic quantities, temperature will be an additional variable. In the case of a magneto-mechanical problem, the heat capacity at constant deformation and constant magnetic field is denoted as $c_{\boldsymbol{F}, \mathbb{H}}$. As an initial attempt towards modelling the thermo-magneto-mechanical behavior of elastomers, a constant heat capacity is assumed, whereby $\Theta_{0}$ is the constant reference temperature

$$
c_{\boldsymbol{F}, \mathbb{H}}(\Theta)=c_{\boldsymbol{F}, \mathbb{H}}\left(\Theta_{0}\right)=c_{0}.\qquad(35)
$$


Departing from the usual definition of the heat capacity $c_0$ we obtain

$$
c_{0}=-\Theta \frac{\partial^{2} \Psi}{\partial \Theta \partial \Theta} \stackrel{!}{=} \text { const. } \Rightarrow-\frac{c_{0}}{\Theta}=\frac{\partial^{2} \Psi}{\partial \Theta \partial \Theta}, \quad \text { with } \quad \Psi=\Psi(\boldsymbol{F}, \Theta, \mathbb{H}),
\tag{36}
$$

see, Holzapfel and Simo [46], Vertechy et al. [75, 76], Erbts et al. [30], Mehnert et al. [53], Santapuri et al. [66, 67]. If the above relation is integrated once from the reference temperature $\Theta_{0}$ to an arbitrary temperature $\Theta$, it becomes

$$
\frac{\partial \Psi}{\partial \Theta}=-c_{0}\left[\ln (\Theta)-\ln \left(\Theta_{0}\right)\right]-M_{1}(\boldsymbol{F}, \mathbb{H})=-c_{0} \ln \left(\frac{\Theta}{\Theta_{0}}\right)-M_{1}(\boldsymbol{F}, \mathbb{H}),
\tag{37}
$$

where the integration constant $M_{1}$ may depend on the deformation gradient $\boldsymbol{F}$ and the magnetic field $\mathbb{H}$ but not on temperature $\Theta$. Integrating a second time from the reference temperature $\Theta_{0}$ to an arbitrary temperature $\Theta$ brings us to the full expression of the energy function

$$
\Psi=c_{0}\left[\Theta-\Theta_{0}-\Theta \ln \left(\frac{\Theta}{\Theta_{0}}\right)\right]-\left[\Theta-\Theta_{0}\right] M_{1}(\boldsymbol{F}, \mathbb{H})+W(\boldsymbol{F}, \mathbb{H}).
\tag{38}
$$

For isotropy, the isothermal energy function $W$ (a function in $\boldsymbol{F}$ and $\mathbb{H}$) at the reference temperature expressed in Equation (38) depends on the magneto-mechanical coupled invariants, i.e. $I_{1}$ to $I_{6}$ as $W(\boldsymbol{F}, \mathbb{H})=W(I_{1}, \cdots I_{6})$. Thereby the magneto-mechanical coupled invariants $(I_{1}, I_{2}, I_{3}, I_{4}, I_{5}, I_{6})$ are defined as a combination of the right Cauchy-Green tensor $\boldsymbol{C}$ and the magnetic field $\mathbb{H}$ in the material configuration

$$
\begin{array}{lll}
I_{1}=\operatorname{tr}(\boldsymbol{C}) ; & I_{2}=\frac{1}{2}\left[[\operatorname{tr}(\boldsymbol{C})]^{2}-\operatorname{tr}\left(\boldsymbol{C}^{2}\right)\right] ; & I_{3}=\operatorname{det}(\boldsymbol{F}) ; \\
I_{4}=[\mathbb{H} \otimes \mathbb{H}]: \boldsymbol{I} ; & I_{5}=[\mathbb{H} \otimes \mathbb{H}]: \boldsymbol{C}^{-1} ; & I_{6}=[\mathbb{H} \otimes \mathbb{H}]: \boldsymbol{C}^{-2}.
\end{array}
\tag{39}
$$

Earlier we proposed an additive decomposition for the coupling term $M_{1}$ in the case of thermo-electroelasticity, see Mehnert et al. [53]. In absence of clear experimental evidences at this stage, a similar approach can be applied here in the thermo-magneto-mechanical study. That means, the integration constant $M_{1}$ can be decomposed additively into a purely mechanical part $M(\boldsymbol{F})$ and a magneto-mechanically coupled part $C(\boldsymbol{F}, \mathbb{H})$, i.e.

$$
M_{1}(\boldsymbol{F}, \mathbb{H})=M(\boldsymbol{F})+C(\boldsymbol{F}, \mathbb{H}).
\tag{40}
$$

As discussed in [53], in the case of large deformations, there are various forms to express the purely mechanical part $M(\boldsymbol{F})$. One of the simplest forms could be $M(\boldsymbol{F})=3 \kappa \beta \ln (J)$, where $\kappa$ is the bulk modulus coefficient at the reference temperature and $\beta$ is the thermal expansion coefficient. Note that in the case the magneto-mechanical deformation is considered as incompressible at constant temperature, it holds that $J=J_{\Theta}$. To complete the expression in Equation (40) the magneto-mechanically coupled part $C(\boldsymbol{F}, \mathbb{H})$ needs to be fixed. We assume a relation in line with the one proposed by Vertechy et al. [75] in thermoelectro-elasticity which was also used in our previous work on electro-active polymer modelling. A formulation comparable to the one found in [75] can be obtained by assuming

$$
C(\boldsymbol{F}, \mathbb{H})=-\frac{1}{\Theta_{0}} W(\boldsymbol{F}, \mathbb{H}),
\tag{41}
$$

which will eventually yield a complete thermo-magneto-mechanically coupled energy function as

$$
\Psi(\boldsymbol{F}, \Theta, \mathbb{H})=\frac{\Theta}{\Theta_{0}} W(\boldsymbol{F}, \mathbb{H})+c_{0}\left[\Theta-\Theta_{0}-\Theta \ln \left(\frac{\Theta}{\Theta_{0}}\right)\right]-\left[\Theta-\Theta_{0}\right] M(\boldsymbol{F}).
\tag{42}
$$

To obtain a full expression of the temperature-dependent energy function derived in Equation (42), we need to define an isothermal energy function $W(\boldsymbol{F}, \mathbb{H})$ at the reference temperature. For the sake of simplicity, a coupled incompressible Neo-Hookean-type material law depending on the invariants $I_{1}$, $I_{4}$ and $I_{5}$ is proposed. The first invariant $I_{1}$ describes the purely mechanical case while the fourth invariant $I_{4}$ depends on the magnetic field. To model the interactions between the mechanical and the magnetic loads $I_{5}$ is introduced into the energy function, which gives

$$
W(\boldsymbol{F}, \mathbb{H})=\mu\left[I_{1}-3\right]+c_{1} I_{4}+c_{2} I_{5}.
\tag{43}
$$

Next we assume that the shear modulus, due to its field-responsive nature, is no longer a constant material parameter but rather depends on the applied magnetic field. Hence, $\mu(I_{4})$ needs to be formulated. For an increase in the stiffness due to magnetization and the phenomenon of magnetic saturation after a critical value of magnetization, a hyperbolic function such as $\mu_{e}/4\left[1+\alpha_{e}\tanh\left(I_{4}/m_{e}\right)\right]$ is assumed, where $\mu_{e}$ is the shear modulus of the material in the absence of a magnetic field. This assumption particularises the previous formulation as

$$
W(\boldsymbol{F}, \mathbb{H})=\frac{\mu_{e}}{4}\left[1+\alpha_{e} \tanh \left(\frac{I_{4}}{m_{e}}\right)\right]\left[I_{1}-3\right]+c_{1} I_{4}+c_{2} I_{5},
\tag{44}
$$

where the parameter $m_{e}$ is required for the purpose of non-dimensionalisation while $\alpha_{e}$ is a dimensionless positive parameter for scaling. The parameters $c_{1}$ and $c_{2}$ relate to the magneto-mechanical coupling. For $\alpha_{e}=c_{1}=c_{2}=0$, this simplifies to the classical Neo-Hooke elastic energy density function widely used to model elastomers. Once suitable experimental evidences are available other advanced forms of energy functions associated with the purely mechanical part can be coupled with the magnetic part of the energy to improve the modelling, cf. [2, 61, 43, 44, 45].

Due to the small value of the vacuum permeability the free space term in the total energy formulation (28) will be neglected in our analytical example, c.f. [77], i.e. there $\Omega(\boldsymbol{F}, \Theta, \mathbb{H}) \approx \Psi(\boldsymbol{F}, \Theta, \mathbb{H})$.

### 3.3. Magneto-mechanically coupled heat equation
From the first law of thermodynamics, the governing equation for the evolution of the thermal field can be written in entropy form as

$$
\Theta \dot{H}=\mathcal{R}-\operatorname{Div} \boldsymbol{Q}+\mathcal{D}^{\mathrm{loc}} \quad \text { with } \mathcal{D}^{\mathrm{loc}} \equiv 0,
\tag{45}
$$

with the heat source $\mathcal{R}$ and the heat flux vector $\boldsymbol{Q}$ in the material configuration. Going back to the thermo-dynamically consistent definition of the the constitutive relation $H=-\frac{\partial \Psi}{\partial \Theta}$ we obtain

$$
\Theta \dot{H}=-\Theta \frac{\partial^{2} \Psi}{\partial \Theta \partial \Theta} \dot{\Theta}-\Theta \frac{\partial^{2} \Psi}{\partial \boldsymbol{F} \partial \Theta}: \dot{\boldsymbol{F}}-\Theta \frac{\partial^{2} \Psi}{\partial \mathbb{H} \partial \Theta} \cdot \dot{\mathbb{H}}.
\tag{46}
$$

Combining Equations (45) and (46), the heat conduction equation is thus obtained in the format

$$
c_{0} \dot{\Theta}=\mathcal{R}-\operatorname{Div} \boldsymbol{Q}+\Theta \partial_{\Theta}\left[\boldsymbol{P}^{\mathrm{tot}}: \dot{\boldsymbol{F}}+\mathbb{B} \cdot \dot{\mathbb{H}}\right].
\tag{47}
$$

In contrast to the classical heat equation, this format contains two additional contributions. The structural thermo-mechanical cooling/heating effect related to $\dot{\boldsymbol{F}}$ and the thermo-magnetic heating/cooling effect related to $\dot{\mathbb{H}}$, see Vertechy et al. [75], Mehnert et al. [53] for a similar expression in the case of thermo-electro-elasticity.

## 4. Non-homogeneous boundary value problems

We now present two boundary value problems based on a widely used geometrical setup, a cylindrical tube of electrically non-conducting magneto-elastic material that behaves incompressible at constant temperature, cf. [22, 23, 24, 25]. In this case, we will formulate the problems under thermo-magneto-mechanically coupled load as discussed in Section 3. In the considered case it is reasonable to work in the cylindrical coordinates $(R, \Phi, Z)$ with the unit basis vectors $(\boldsymbol{E}_{R}, \boldsymbol{E}_{\Phi}, \boldsymbol{E}_{Z})$ defined in the material configuration. In the spatial configuration these quantities are defined as $(r, \phi, z)$ and $(\boldsymbol{e}_{r}, \boldsymbol{e}_{\phi}, \boldsymbol{e}_{z})$, respectively. It is assumed that the tube is infinitely long so as to avoid difficulties with the end conditions of a finite length tube. Furthermore we assume in these examples that the deformation due to thermal expansion can be neglected compared to the prescribed deformation because of the comparably small value of the thermal expansion coefficient $\beta$. Therefore we can assume $\boldsymbol{F}=\boldsymbol{F}_{M}$. The three components of the magnetic field $\mathbb{h}$ and the magnetic induction $\mathbb{b}$ are defined in the spatial configuration as $(\mathbb{h}_{r}, \mathbb{h}_{\phi}, \mathbb{h}_{z})$ and $(\mathbb{b}_{r}, \mathbb{b}_{\phi}, \mathbb{b}_{z})$, respectively. By expressing the divergence of the magnetic induction $\operatorname{div} \mathbb{b}=0$ in cylindrical coordinates in the deformed configuration we find

$$
\frac{1}{r} \mathbb{b}_{r}+\frac{\partial \mathbb{b}_{r}}{\partial r}+\frac{1}{r} \frac{\partial \mathbb{b}_{\phi}}{\partial \phi}+\frac{\partial \mathbb{b}_{z}}{\partial z}=0.
\tag{48}
$$

Similarly, the curl of the magnetic displacement field becomes

$$
\frac{1}{r} \frac{\partial \mathbb{h}_{z}}{\partial \phi}-\frac{\partial \mathbb{h}_{\phi}}{\partial z}=0 ; \quad \frac{\partial \mathbb{h}_{r}}{\partial z}-\frac{\partial \mathbb{h}_{z}}{\partial r}=0 ; \quad \frac{1}{r} \frac{\partial\left(r \mathbb{h}_{\phi}\right)}{\partial r}-\frac{1}{r} \frac{\partial \mathbb{h}_{r}}{\partial \phi}=0.
\tag{49}
$$

As we investigate cylindrically symmetric problems the components of the magnetic field and the magnetic induction are independent of the coordinates $\phi$ and $z$, i.e. $\frac{\partial(\bullet)}{\partial \phi}=\frac{\partial(\bullet)}{\partial z}=0$, reducing equations (48) and (49) to

$$
r \mathbb{b}_{r}=\text { const.; } \quad r \mathbb{h}_{\phi}=\text { const.; } \quad \mathbb{h}_{z}=\text { const.. }
\tag{50}
$$

Finally from equation (12), the divergence of the total Cauchy stress tensor in cylindrical coordinates in a cylindrically symmetric stress state is expressed as

$$
\operatorname{div} \boldsymbol{\sigma}^{\mathrm{tot}}=\left[\frac{\partial \sigma_{r r}^{\mathrm{tot}}}{\partial r}+\frac{\sigma_{r r}^{\mathrm{tot}}-\sigma_{\phi \phi}^{\mathrm{tot}}}{r}\right] \boldsymbol{e}_{r}+\left[\frac{\partial \sigma_{r \phi}^{\mathrm{tot}}}{\partial r}+\frac{2 \sigma_{r \phi}^{\mathrm{tot}}}{r}\right] \boldsymbol{e}_{\phi}+\left[\frac{\partial \sigma_{r z}^{\mathrm{tot}}}{\partial r}+\frac{\sigma_{r z}^{\mathrm{tot}}}{r}\right] \boldsymbol{e}_{z}.
\tag{51}
$$

A schematic figure of the thick-walled tube in cylindrical coordinates is depicted in Figure (1). The geometry of the tube in the spatial configuration is described by

$$
a_{i} \leq r \leq a_{e} ; \quad 0 \leq \phi \leq 2 \pi ; \quad 0 \leq z \leq l,
\tag{52}
$$

where $a_{i}$ and $a_{e}$ denote the inner and outer radii in the deformed configuration, respectively. The corresponding geometry of the tube in the material configuration is expressed by

$$
A_{i} \leq R \leq A_{e} ; \quad 0 \leq \Phi \leq 2 \pi ; \quad 0 \leq Z \leq L,
\tag{53}
$$

![](./images/813107845410062337_2.jpg)

Figure 1: A thick walled cylinder in the spatial configuration with the internal radius $a_i$ and the external radius $a_e$. An electric current $c$ generates the magnetic field $\mathfrak{h}$. The tube is inflated by an internal pressure $P$ while it is axially stretched by a normal force $\mathcal{N}$

where $A_i$ and $A_e$ are the inner and outer radii in the undeformed configuration, respectively.

### 4.0.1. Solution of the temperature function
We will now focus on finding an analytical solution of the heat equation (47) and therefore apply various simplifications. In the current case we neglect the thermo-mechanical and thermo-magneto cooling/heating effects, hence the equation (47) will simplify to

$$
c_{0} \dot{\Theta}=\mathcal{R}-\operatorname{Div} Q.\tag{54}
$$

To the best of the authors' knowledge, for the problem under consideration, an analytical solution is only available in the literature for the stationary heat equation [10,60]. Hence we consider only steady-state heat conditions and neglect any source terms $\mathcal{R}$. With these simplifications we can formulate the equation in the deformed configuration as

$$
\operatorname{div}(\operatorname{grad} \Theta)=0, \quad \text { or } \quad \Delta \Theta=0,\tag{55}
$$

where $\boldsymbol{Q}=-\kappa J C^{-1} \operatorname{Grad} \Theta$ and $\Delta$ is the spatial Laplacian operator. In formulating the equation, a constant value for the thermal conductivity $\kappa$ has been assumed. The quasi-static heat equation is reduced to the Laplace equation [10]. In cylindrical coordinates $(r, \phi, z)$ the equation for an axial symmetric problem, e.g. a cylindrical hollow tube can be written as

$$
\frac{\mathrm{d}^{2} \Theta(r)}{\mathrm{d} r^{2}}+\frac{1}{r} \frac{\mathrm{d} \theta(r)}{\mathrm{d} r}=0,\tag{56}
$$

where $r$ is the spatial radius of the tube. Bland et al. [10], Rajagopoal and Huang [60] proposed an analytical solution for the Laplace equation when a temperature difference is prescribed between the internal and external radii, i.e.

$$
\Theta(r)=k_{1}+k_{2} \ln r,\tag{57}
$$

where $k_1$ and $k_2$ are constants that need to be determined from the boundary conditions. Such a solution indicates a logarithmically varying temperature profile along the radial thickness of the tube. For an internal radius $a_i$ and an external radius $a_e$ with the corresponding temperatures $\Theta(a_i)$ and $\Theta(a_e)$, respectively, we find

$$
k_{1}=\frac{\Theta\left(a_{i}\right) \ln \left(a_{e}\right)-\Theta\left(a_{e}\right) \ln a_{i}}{\ln a_{e}-\ln a_{i}} \quad \text { and } \quad k_{2}=\frac{\Theta\left(a_{e}\right)-\Theta\left(a_{i}\right)}{\ln a_{e}-\ln a_{i}}.
\tag{58}
$$

#### 4.0.2. Azimuthally applied magnetic field
There are few ways to apply a magnetic load for this thick-walled tube problem as described in Dorfmann and Ogden [22, 23, 24, 25]. In the following examples, we consider an azimuthally applied magnetic field with the spatial component $\natural_{\phi}=\lambda^{-1} \mathbb{H}_{\Phi}$. For the problem under consideration, the spatial magnetic field is related to the deformed tube geometry by

$$
\natural_{\phi}=\frac{c}{r}=\frac{c}{R \lambda}=\lambda^{-1} \mathbb{H}_{\phi},
\tag{59}
$$

where $c$ is a constant. This type of magnetic field can be created in a real experimental set-up if a current flows along the core of the tube or a surface current flows along the inner boundary of the tube. As we consider a hollow cylinder, it can be assumed that there is a central core of radius $r<a_i$ that can carry a steady current $I$, i.e. $I=2 \pi c$. In this situation, there is no difficulty for a possible singularity at $r=0$, see Dorfmann and Ogden [25] for more details. In the absence of a surface current, the boundary conditions require that $\natural_{\phi}$ is continuous across the cylindrical surfaces $r=a_i$ and $r=a_e$. Since this is the only component of the magnetic field that exists throughout the thickness of the tube, there will only be a single corresponding component $\mathbb{b}_{\phi}$ of the magnetic induction throughout the space. The non-zero components of the Maxwell stress therefore read

$$
\sigma_{r r}^{\max }=\sigma_{z z}^{\max }=-\sigma_{\phi \phi}^{\max }=\frac{1}{2} \mu_{0} \natural_{\phi}^{2}.
\tag{60}
$$

Note that according to the equation (50) $)_{2}, \natural_{\phi}$ depends on $r$, hence $\sigma_{\phi \phi}^{\max }=\sigma_{\phi \phi}^{\max }(r)=\frac{1}{2} \mu_{0} \natural_{\phi}^{2}=\frac{1}{2} \mu_{0} \frac{c^{2}}{r^{2}}$.

### 4.1. Extension and inflation of a tube
In the first example the tube is deformed under a combination of axial extension, due to the normal force $\mathcal{N}$, and radial expansion that is the result of a pressure $P$ on the internal surface of the tube. Thus the transformation from the undeformed to the deformed configuration reads

$$
r^{2}=\lambda_{z}^{-1}\left[R^{2}-A_{i}^{2}\right]+a_{i}^{2}, \quad \phi=\Phi, \quad z=\lambda_{z} Z,
\tag{61}
$$

where the first relation is based on the incompressibility assumption and $\lambda_{z}$ is the uniform axial stretch. The relation between the deformed internal radius $a_i$ and the deformed external radius $a_e$ reads

$$
a_{e}^{2}=a_{i}^{2}+\lambda_{z}^{-1}\left[A_{e}^{2}-A_{i}^{2}\right].
\tag{62}
$$

This results in a deformation gradient that only has entries on the main diagonal. In cylindrical coordinates the radial, circumferential/azimuthal and axial entries read

$$
\lambda_{r}=\left[\lambda \lambda_{z}\right]^{-1} ; \quad \lambda_{\phi}=\frac{r}{R}=\lambda ; \quad \lambda_{z},
\tag{63}
$$

wherein the incompressibility constraint $\lambda_{1} \lambda_{2} \lambda_{3} \equiv 1$ has been used. Using the deformation gradient the magnetic field vector in the spatial configuration takes the form

$$
\begin{aligned}
\mathbb{h}_{r} & =\frac{1}{\lambda_{r}} \mathbb{H}_{R}=\lambda \lambda_{z} \mathbb{H}_{R}, \\
\mathbb{h}_{\phi} & =\frac{1}{\lambda_{\phi}} \mathbb{H}_{\Phi}=\lambda^{-1} \mathbb{H}_{\Phi}, \\
\mathbb{h}_{z} & =\frac{1}{\lambda_{z}} \mathbb{H}_{Z}=\lambda_{z}^{-1} \mathbb{H}_{Z}.
\end{aligned}
\tag{64}
$$

Considering cylindrical symmetry, the divergence of the total stress $\operatorname{div} \boldsymbol{\sigma}^{\text {tot }}=0$ in cylindrical coordinates can be derived from Equation (51) as

$$
\begin{aligned}
\frac{\partial \sigma_{r r}^{\mathrm{tot}}}{\partial r}+\frac{\sigma_{r r}^{\mathrm{tot}}-\sigma_{\phi \phi}^{\mathrm{tot}}}{r} & =0, \\
\frac{\partial \sigma_{r \phi}^{\mathrm{tot}}}{\partial r}+\frac{2 \sigma_{r \phi}^{\mathrm{tot}}}{r} & =0 \\
\frac{\partial \sigma_{r z}^{\mathrm{tot}}}{\partial r}+\frac{1}{r} \sigma_{r z}^{\mathrm{tot}} & =0.
\end{aligned}
\tag{65a}
$$

$$
\frac{\partial \sigma_{r \phi}^{\mathrm{tot}}}{\partial r}+\frac{2 \sigma_{r \phi}^{\mathrm{tot}}}{r}=0
\tag{65b}
$$

$$
\frac{\partial \sigma_{r z}^{\mathrm{tot}}}{\partial r}+\frac{1}{r} \sigma_{r z}^{\mathrm{tot}}=0.
\tag{65c}
$$

Using the constitutive relation $(34)_{2}$ the total Piola-Kirchhoff stress for an incompressible material can be calculated as

$$
\begin{aligned}
\boldsymbol{S}^{\mathrm{tot}} & =2 \frac{\partial \Omega}{\partial \boldsymbol{C}}-p \boldsymbol{C}^{-1} \\
& =2\left[\frac{\partial \Omega}{\partial I_{1}} \frac{\partial I_{1}}{\partial \boldsymbol{C}}+\frac{\partial \Omega}{\partial I_{2}} \frac{\partial I_{2}}{\partial \boldsymbol{C}}+\frac{\partial \Omega}{\partial I_{5}} \frac{\partial I_{5}}{\partial \boldsymbol{C}}+\frac{\partial \Omega}{\partial I_{6}} \frac{\partial I_{6}}{\partial \boldsymbol{C}}\right]-p \boldsymbol{C}^{-1} \\
& =2 \Omega_{1} \boldsymbol{I}+2 \Omega_{2}\left[I_{1} \boldsymbol{I}-\boldsymbol{C}\right]-p \boldsymbol{C}^{-1}-2 \Omega_{5}\left[\boldsymbol{C}^{-T} \cdot[\mathbb{H} \otimes \mathbb{H}] \cdot \boldsymbol{C}^{-1}\right] \\
& -2 \Omega_{6}\left[\left[\boldsymbol{C}^{-1} \cdot \boldsymbol{C}^{-T}\right] \mathbb{H} \otimes\left[\boldsymbol{C}^{-1} \mathbb{H}\right]-\left[\boldsymbol{C}^{-1} \mathbb{H}\right] \otimes\left[\boldsymbol{C}^{-1} \cdot \boldsymbol{C}^{-T}\right] \mathbb{H}\right].
\end{aligned}
\tag{66}
$$

The total Cauchy stress can be derived by a push forward of the Piola-Kirchhoff stress, which gives

$$
\begin{aligned}
\boldsymbol{\sigma}^{\mathrm{tot}} & =\boldsymbol{F} \boldsymbol{S}^{\mathrm{tot}} \boldsymbol{F}^{T}-p \boldsymbol{F} \boldsymbol{C}^{-1} \boldsymbol{F}^{T} \\
\boldsymbol{\sigma}^{\mathrm{tot}} & =\frac{\partial \Omega}{\partial \boldsymbol{F}} \boldsymbol{F}^{T}-p \boldsymbol{i} \\
& =\left[\frac{\partial \Omega}{\partial I_{1}} \frac{\partial I_{1}}{\partial \boldsymbol{F}}+\frac{\partial \Omega}{\partial I_{2}} \frac{\partial I_{2}}{\partial \boldsymbol{F}}+\frac{\partial \Omega}{\partial I_{5}} \frac{\partial I_{5}}{\partial \boldsymbol{F}}+\frac{\partial \Omega}{\partial I_{6}} \frac{\partial I_{6}}{\partial \boldsymbol{F}}\right] \boldsymbol{F}^{T}-p \boldsymbol{i} \\
& =2 \Omega_{1} \boldsymbol{b}+2 \Omega_{2}\left[I_{1} \boldsymbol{b}-\boldsymbol{b}^{2}\right]-p \boldsymbol{i}-2 \Omega_{5} \mathbb{h} \otimes \mathbb{h}-2 \Omega_{6}\left[\boldsymbol{b}^{-1} \mathbb{h} \otimes \mathbb{h}+\mathbb{h} \otimes \boldsymbol{b}^{-1} \mathbb{h}\right].
\end{aligned}
\tag{67}
$$


In the case of radial inflation and axial stretch the deformation gradient has only diagonal entries. This leads to the non-zero stress components of $\boldsymbol{\sigma}^{\text{tot}}$

$$
\begin{aligned}
\sigma_{r r}^{\mathrm{tot}} & =-p+2 \lambda^{-2} \lambda_{z}^{-2}\left[\Omega_{1}+\Omega_{2}\left[\lambda^{2}+\lambda_{z}^{2}\right]\right]-2\left[\Omega_{5}+2 \Omega_{6} \lambda^{2} \lambda_{z}^{2}\right] \lambda^{2} \lambda_{z}^{2} \mathbb{H}_{R}^{2}, \\
\sigma_{\phi \phi}^{\mathrm{tot}} & =-p+2 \lambda^{2}\left[\Omega_{1}+\Omega_{2}\left[\lambda^{-2} \lambda_{z}^{-2}+\lambda_{z}^{2}\right]\right]-2 \Omega_{5} \lambda^{-2} \mathbb{H}_{\Phi}^{2}-4 \Omega_{6} \lambda^{-4} \mathbb{H}_{\Phi}^{2}, \\
\sigma_{z z}^{\mathrm{tot}} & =-p+2 \lambda_{z}^{2}\left[\Omega_{1}+\Omega_{2}\left[\lambda^{-2} \lambda_{z}^{-2}+\lambda^{2}\right]\right]-2\left[\Omega_{5}+2 \Omega_{6} \lambda_{z}^{-2}\right] \lambda_{z}^{-2} \mathbb{H}_{Z}^{2}, \\
\sigma_{r z}^{\mathrm{tot}} & =-2 \mathbb{H}_{R} \mathbb{H}_{Z}\left[\Omega_{5} \lambda+\Omega_{6}\left[\lambda^{3} \lambda_{z}^{2}+\lambda \lambda_{z}^{-2}\right]\right],
\end{aligned}
$$

where the derivatives of the energy function with respect to the invariants are designated as $\frac{\partial \Omega_{i}}{\partial I_{i}}=: \Omega_{i}$. After rearranging Equation (65a), we obtain

$$
\sigma_{r r}^{\mathrm{tot}}(\bar{r})=\int_{a_{i}}^{\bar{r}} \frac{1}{r}\left[\sigma_{\phi \phi}^{\mathrm{tot}}(r)-\sigma_{r r}^{\mathrm{tot}}(r)\right] \mathrm{d} r+q,
$$

where $q$ is an integration constant which can be determined from the boundary conditions for the stress. If the outer surface of the tube is free of mechanical loads, i.e. $\sigma_{r r}^{\text {tot }}\left(a_{e}\right)=\sigma_{r r}^{\max }\left(a_{e}\right)$, we find

$$
\begin{aligned}
q & =-\int_{a_{i}}^{a_{e}} \frac{1}{r}\left[\sigma_{\phi \phi}^{\mathrm{tot}}(r)-\sigma_{r r}^{\mathrm{tot}}(r)\right] \mathrm{d} r+\sigma_{r r}^{\max }\left(a_{e}\right) \\
& =\int_{a_{i}}^{a_{e}} \frac{1}{r}\left[\sigma_{r r}^{\mathrm{tot}}(r)-\sigma_{\phi \phi}^{\mathrm{tot}}(r)\right] \mathrm{d} r+\sigma_{r r}^{\max }\left(a_{e}\right).
\end{aligned}
$$

We assume a uniform mechanical pressure $P$ at the internal surface of the cylinder boundary, resulting in the total Cauchy stress in radial direction in the form

$$
\sigma_{r r}^{\mathrm{tot}}\left(a_{i}\right)=\sigma_{r r}^{\max }\left(a_{i}\right)-P.
$$

This relation leads to

$$
\begin{aligned}
\sigma_{r r}^{\mathrm{tot}}\left(a_{i}\right) & =\int_{a_{i}}^{a_{i}} \frac{1}{r}\left[\sigma_{\phi \phi}^{\mathrm{tot}}(r)-\sigma_{r r}^{\mathrm{tot}}(r)\right] \mathrm{d} r+q \\
& =\int_{a_{i}}^{a_{e}} \frac{1}{r}\left[\sigma_{r r}^{\mathrm{tot}}(r)-\sigma_{\phi \phi}^{\mathrm{tot}}(r)\right] \mathrm{d} r+\sigma_{r r}^{\max }\left(a_{e}\right)=\sigma_{r r}^{\max }\left(a_{i}\right)-P .
\end{aligned}
$$

Therefore, we obtain the definition of the pressure as

$$
\begin{aligned}
P & =\int_{a_{i}}^{a_{e}} \frac{1}{r}\left[\sigma_{\phi \phi}^{\mathrm{tot}}(r)-\sigma_{r r}^{\mathrm{tot}}(r)\right] \mathrm{d} r+\sigma_{r r}^{\max }\left(a_{i}\right)-\sigma_{r r}^{\max }\left(a_{e}\right) \\
& =\int_{a_{i}}^{a_{e}} \frac{1}{r}\left[\sigma_{\phi \phi}^{\mathrm{tot}}(r)-\sigma_{r r}^{\mathrm{tot}}(r)\right] \mathrm{d} r+\frac{1}{2} \mu_{0} \frac{c^{2}}{a_{i}^{2}}-\frac{1}{2} \mu_{0} \frac{c^{2}}{a_{e}^{2}} \\
& =\int_{a_{i}}^{a_{e}} \frac{1}{r}\left[\sigma_{\phi \phi}^{\mathrm{tot}}(r)-\sigma_{r r}^{\mathrm{tot}}(r)\right] \mathrm{d} r+\frac{1}{2} \mu_{0} c^{2}\left[\frac{1}{a_{i}^{2}}-\frac{1}{a_{e}^{2}}\right]
\end{aligned}
$$

In order to give the reader a feeling for the derivation of the pressure we will initially present an analytical solution for the isothermal case with a linear variation of the field-responsive shear modulus, i.e. $\mu\left(I_{4}\right)=$

$[g_0 + g_1 I_4]$. For the more complex derivations in the case of an existing temperature gradient with a tangent hyperbolic shear function relevant calculations are presented in the Appendix. In the simplified case these derivatives take the form

$$
\Omega_{1}=\frac{1}{2}\left[g_{0}+g_{1} I_{4}\right], \quad \Omega_{2}=\Omega_{6}=0, \quad \Omega_{4}=c_{1}+\frac{g_{1}}{2}\left[I_{1}-3\right], \quad \Omega_{5}=c_{2}, I_{4}=\mathbb{H}_{\Phi}^{2}=\frac{c^{2}}{R^{2}}. \tag{74}
$$

By inserting the expressions of $\sigma_{\phi \phi}^{\text {tot }}$ and $\sigma_{r r}^{\text {tot }}$ from Equation (68) into Equation (73), we obtain

$$
\begin{aligned}
P= & \int_{a_{i}}^{a_{e}} \frac{1}{r}\left[\sigma_{\phi \phi}^{\mathrm{tot}}(r)-\sigma_{r r}^{\mathrm{tot}}(r)\right] \mathrm{d} r+\frac{1}{2} \mu_{0} c^{2}\left[\frac{1}{a_{i}^{2}}-\frac{1}{a_{e}^{2}}\right] \\
= & \int_{a_{i}}^{a_{e}} \frac{1}{r}\left[\frac{1}{2}\left[g_{0}+g_{1} I_{4}\right]\left[2 \lambda^{2}-2 \lambda^{-2} \lambda_{z}^{-2}\right] \mathrm{d} r-2 c_{2} \int_{a_{i}}^{a_{e}} \lambda^{-2} I_{4} \frac{\mathrm{d} r}{r}+\frac{1}{2} \mu_{0} c^{2}\left[\frac{1}{a_{i}^{2}}-\frac{1}{a_{e}^{2}}\right]\right] \\
= & \underbrace{\int_{a_{i}}^{a_{e}} g_{0}\left[\lambda^{2}-\lambda^{-2} \lambda_{z}^{-2}\right] \frac{\mathrm{d} r}{r}}_{P_{1}}+\underbrace{\int_{a_{i}}^{a_{e}} g_{1} I_{4}\left[\lambda^{2}-\lambda^{-2} \lambda_{z}^{-2}\right] \frac{\mathrm{d} r}{r}}_{P_{2}} \\
& -\underbrace{2 c_{2} \int_{a_{i}}^{a_{e}} \lambda^{-2} I_{4} \frac{\mathrm{d} r}{r}}_{P_{3}}+\underbrace{\frac{1}{2} \mu_{0} c^{2}\left[\frac{1}{a_{i}^{2}}-\frac{1}{a_{e}^{2}}\right]}_{P_{4}}
\end{aligned} \tag{75}
$$

The integrals $P_{1}, P_{2}$ and $P_{3}$ can be solved analytically. With the definition for the expressions $\lambda_{i}=a_{i} / A_{i}$, $\lambda_{e}=a_{e} / A_{e}$ and $\zeta=A_{e} / A_{i}$, we can derive the following dimensionless formulations

$$
\begin{aligned}
& P_{1}=\frac{g_{0}}{\lambda_{z}}\left[\ln \left(\frac{\lambda_{i}}{\lambda_{e}}\right)-\frac{1}{2 \lambda_{z}}\left[\lambda_{i}^{-2}-\lambda_{e}^{-2}\right]\right], \\
& P_{2}=\frac{1}{2} g_{1} A_{i}^{-2} c^{2}\left[\frac{\zeta^{2} \lambda_{e}^{2}-\lambda_{i}^{2}}{1+\lambda_{z}\left[\zeta^{2} \lambda_{e}^{2}-\lambda_{i}^{2}\right]}\right]+\frac{1}{2} g_{1} A_{i}^{-2} \lambda_{z}^{-2} c^{2}\left[\frac{1}{\zeta^{2} \lambda_{e}^{2}}-\frac{1}{\lambda_{i}^{2}}\right] \\
& P_{3}=-c_{2} c^{2}\left[\frac{1}{a_{i}^{2}}-\frac{1}{a_{e}^{2}}\right].
\end{aligned} \tag{76}
$$

If we consider $\mu_{0}=2 c_{2}$, the terms $P_{3}$ and $P_{4}$ cancel out. This gives a non-dimensional expression for the pressure $P$ on the internal surface of the tube

$$
\begin{aligned}
P= & \frac{g_{0}}{\lambda_{z}}\left[\ln \left(\frac{\lambda_{i}}{\lambda_{e}}\right)-\frac{1}{2 \lambda_{z}}\left[\lambda_{i}^{-2}-\lambda_{e}^{-2}\right]\right]+\frac{1}{2} g_{1} A_{i}^{-2} c^{2}\left[\frac{\zeta^{2} \lambda_{e}^{2}-\lambda_{i}^{2}}{1+\lambda_{z}\left[\zeta^{2} \lambda_{e}^{2}-\lambda_{i}^{2}\right]}\right] \\
& +\frac{1}{2} g_{1} A_{i}^{-2} \lambda_{z}^{-2} c^{2}\left[\frac{1}{\zeta^{2} \lambda_{e}^{2}}-\frac{1}{\lambda_{i}^{2}}\right].
\end{aligned} \tag{77}
$$

Another important term to demonstrate the results for this example is the normal force $\mathcal{N}$ that is applied at the end faces of the tube. It is the force that is required for an axial extension or compression and is given by

$$
\mathcal{N}=2 \pi \int_{a_{i}}^{a_{e}} t_{z} r \mathrm{~d} r=2 \pi \int_{a_{i}}^{a_{e}}\left[\sigma_{z z}^{\mathrm{tot}}-\sigma_{z z}^{\max }\right] r \mathrm{~d} r. \tag{78}
$$

A detailed calculation for the normal force for the thermo-magneto-mechanical problem is presented in the Appendix.


### 4.1.1. Results and discussions

In the previous chapter we presented the derivation of an expression for the pressure on the internal surface and for the normal force on the end faces of a cylinder in the isothermal case and for a linearly evolving field sensitive shear modulus. In order to illustrate the capabilities of the derived thermo-magneto-mechanical framework we are now going to present the results for the inflation and axial extension of the cylinder with a more complex formulation of the shear modulus containing a hyperbolic function, c.f. Equation (44). The expressions resulting from this more intricate material model are presented in the Appendix and contain integrals that can not be solved analytically. For the results presented in the following, these remaining terms were evaluated using a five point Gauss quadrature rule, cf. Van Loan [84]. The material parameters used in the calculations are shown in Table 1. The value for the isothermal shear modulus $\mu_e$ is taken from [5] while the value for $\alpha_e$ is adapted from [63].

**Table 1: Various material constants used in the computations.**

| $\mu_e$ in MPa | $\alpha$ | $m_e$ in $\text{T}^2$ | $c_2$ in F/m |
|----------------|----------|------------------------|--------------|
| 0.1            | 30       | 1                      | $0.5\mu_0$   |

We will start to illustrate the material behavior by focusing first on the isothermal load case of the hollow cylinder with the initial internal radius of $A_i = 10$ mm. We prescribe the radial compression or inflation characterized by the radial stretch $\lambda_i$ and the axial stretch $\lambda_z$ as boundary conditions. Figure 2 illustrates the internal pressure $P$ required to achieve a specific magneto-mechanical loading. The pressure is depicted for selected values of the tube thickness, characterized by the ratio of the external to the internal radius $\zeta$ both in the purely mechanical case (solid lines) and the magneto-mechanical case (dashed lines). The strength of the circumferentially applied magnetic field depends on the electric current $c$.

![](./images/813107845410062337_3.jpg)

Figure 2: Plot of the pressure with respect to (a) $\lambda_i$ and (b) $\lambda_z$ under a magneto-mechanically coupled load for selected values of $\zeta$

It can be observed in Figure 2(a) that in the case of inflation ($\lambda_i > 1$) the required pressure on the inter- nal surface of the tube is positive and increases with $\lambda_i$, whereas in the case of compression ($\lambda_i < 1$) the pressure is negative and decreases if the tube is compressed further. The magnitude of the pressure is also directly depending on the thickness of the cylinder. An increased wall thickness leads to an increase in the magnitude of the pressure. A circumferentially applied magnetic field induced by a current $c$ results in two effects in the material response. On the one hand, the material contracts in radial direction due to the magneto-mechanical coupling, and on the other hand, the material hardens due to the field-dependent shear modulus $\mu(I_4)$, see Saxena et al. [65]. As the effect of the contraction is substantially smaller than the hardening due to the selected material parameters $c_2$ and $\alpha_e$, the increase in pressure visible when a magnetic field is applied is mainly due to the increased shear modulus.

In Figure 2(b) it can be observed that the internal pressure decreases when the cylinder is stretched in the axial direction which is due to the decrease in the wall thickness of the cylinder as its volume is preserved. When the initial tube thickness $\zeta$ is changed, the magnitude of the pressure is affected accordingly. Further- more when a magnetic field is applied, the hardening effect on the material is visible as the pressure level increases.

Next, in addition to the mechanical and magnetic loading, a radial temperature gradient is applied to the cylinder by varying the temperature $\Theta_e$ on the external surface of the tube while keeping the temperature on the internal surface fixed at the reference temperature of 293 K. The behavior of the internal pressure for this thermo-magneto-mechanical loading case is depicted in Figure 3 for selected values of $\Theta_e$.

![](./images/813107845410062337_4.jpg)

Figure 3: Plot of the pressure with respect to (a) $\lambda_i$ and (b) $\lambda_z$ under thermo-magneto-mechanically coupled loading for selected values of $\Theta_e$

The general trend of the behavior due to the magnetic and mechanical loading remains unchanged compared to the isothermal case but the additional temperature gradient has an influence on the magnitude of the pressure. It can be observed that the pressure increases for a temperature increase on the external surface

and decreases for the opposite case which is in accordance with the results presented for polymeric materials in Treloar [83]. In this context it is important to mention that in the scope of this contribution the material parameters are sensitive exclusively to the magnetic field characterized by the term $\alpha_{e} \tanh \left(\frac{J_{4}}{m_{e}}\right)$, not to the temperature gradient. The increase in pressure is therefore due to the additional energy in the system instead of a direct effect on the material parameters. Figure 4 depicts the variation of the pressure with respect to the wall thickness of the tube (a) and the applied magnetic field (b).

![](./images/813107845410062337_5.jpg)

Figure 4: Plot of the pressure with respect to (a) $\zeta$ and (b) the magnetic field resulting form the current $c$ under thermo-magneto-mechanically coupled loading for various values of $\Theta_{e}$

As was already deduced from the preceding Figures, the internal pressure increases with an increased wall thickness. Figure 4(a) highlights that the absolute difference between the pressure in the isothermal case and the cases with an applied temperature gradient becomes larger with increased values of $\zeta$. On the other hand, the ratio between the isothermal pressure and the one in the thermo-magneto-mechanical case is reduced with a larger value of the wall thickness, which is depicted and analyzed further in Figure 5. Figure 4(b) shows the influence of the applied electric current and therefore of the resulting circumferential magnetic field. It is clearly visible that the application of a magnetic field results in a hardening of the material as the magnitude of the pressure increases. Due to the incorporation of the tangent hyperbolic-type saturation function in the formulation of the field-sensitive shear modulus, this hardening effect almost vanishes at a threshold, after which the pressure is almost constant, cf. Figure 4(b). This highlights furthermore that the influence of the magnetic field on the material parameter has a significantly larger effect on the resulting pressure compared to the displacement resulting from the magneto-mechanical coupling.

Figure 5 shows the influence of $\Theta_{e}$ on the resulting pressure for various selected values of the wall thickness. It should be mentioned in this context that the tube has to remain thick-walled $(\zeta>1)$ for the purpose of the presented calculations as the temperature function is not defined in the thin-walled case. From Figure 5(a)

![](./images/813107845410062337_6.jpg)

Figure 5: Plot of the pressure (a) and the pressure ratio $P/P_{\Theta_{0}}$ (b) under thermo-magneto-mechanical coupled loading for selected values of the external temperature $\Theta_{e}$

it can be observed that the model results in a linear increase of the resulting pressure for increased values of $\Theta_{e}$. Depicted in Figure 5(b) is the ratio of the pressure $P$ at a specific temperature $\Theta$ to the pressure in the isothermal case $P_{\Theta_{0}}$. It can be observed that a change in the temperature on the external cylinder surface has the most distinct effect on the pressure for the smallest values of $\zeta$, as this leads to a larger temperature gradient.

Now we will focus on the scaled normal force $\bar{\mathcal{N}} = \frac{\mathcal{N}}{A_{i}^{2}\pi}$ that has to be applied on the cross section of the cylinder in order to maintain the prescribed boundary conditions. Initially only the isothermal loading case is considered that is depicted in Figure 6.
It is visible in Figure 6(a) that as the cylinder tries to contract in axial direction when inflated radially, a positive normal force has to be applied to maintain the prescribed axial stretch $\lambda_{z}=1$. Similar to the internal pressure, the normal force increases as well for an applied magnetic field as the material hardens.
Figure 6(b) shows that in order to achieve a tensile axial stretch $\lambda_{z}>1$, a positive normal force has to be applied that increases with the value of $\lambda_{z}$. It should be noted here that at $\lambda_{z}=1$ the normal force does not vanish as in the considered case there is a constant prescribed inflation $\lambda_{i}=2$.
Next a radial temperature gradient is applied which leads to an increase in the magnitude of the normal force both when focusing on the behavior due to radial inflation and to an axial stretch as can be seen in Figure 7.
As before, the change in temperature leads to a change in the normal force.
Figure 8 depicts the behavior of the normal force depending on the thickness of the cylinder (a) and the magnetic field resulting from the applied current (b). As in the case of the pressure, the magnitude of the normal force increases with an increased wall thickness as well as for an increased temperature on

![](./images/813107845410062337_7.jpg)

Figure 6: Plot of the normal force with respect to (a) $\lambda_i$ and (b) $\lambda_z$ under a magneto-mechanically coupled load for various values of $\zeta$

![](./images/813107845410062337_8.jpg)

Figure 7: Plot of the normal force with respect to (a) $\lambda_i$ and (b) $\lambda_z$ under a thermo-magneto-mechanically coupled load for various values of $\zeta$

the external tube surface. In Figure 8(b) the characteristic saturation behavior of the field-sensitive shear modulus is visible as the increase of the normal force is restricted to a certain amount of the magnetic field until a threshold is reached. After this the increase in the normal force is only minimal as there is no further hardening of the material but only the effect of the deformation of the cylinder influences the result.

![](./images/813107845410062337_9.jpg)

Figure 8: Plot of the normal force with respect to (a) $\lambda_{i}$ and (b) $\lambda_{z}$ under a thermo-magneto-mechanically coupled load for various values of $\zeta$

### 4.2. Extension and Torsion of a tube

In our second example, the magnetic and thermal boundary conditions remain the same as before but the mechanical loading of the cylindrical tube is changed to a combination of an axial stretch and torsion of the angle per unit deformed length $\tau$ around the cylinder axis. For this specific loading case the transformation of the undeformed to the deformed coordinates reads
$$
r=\lambda_{z}^{-1 / 2} R, \quad \phi=\Phi+\lambda_{z} \tau Z, \quad z=\lambda_{z} Z,\tag{79}
$$
and results in a deformation gradient in the form
$$
\mathbf{F}=\left(\begin{array}{ccc}
\lambda_{z}^{-1 / 2} & 0 & 0 \\
0 & \lambda_{z}^{-1 / 2} & \tau r \lambda_{z} \\
0 & 0 & \lambda_{z}
\end{array}\right)=\left(\begin{array}{ccc}
\lambda_{z}^{-1 / 2} & 0 & 0 \\
0 & \lambda_{z}^{-1 / 2} & \gamma \lambda_{z} \\
0 & 0 & \lambda_{z}
\end{array}\right),\tag{80}
$$
where we have introduced the definition of $\gamma=r \tau$ and used the incompressibility constraint $\operatorname{det}(\mathbf{F})=1$. With the given deformation gradient and an azimuthal magnetic field we can use the relations in Equations

(67) to calculate the respective non-zero entries of the total Cauchy stress which results in

$$
\begin{aligned}
\sigma_{r r}^{\mathrm{tot}} & =2 \Omega_{1} \lambda_{z}^{-1}-p, \\
\sigma_{\phi \phi}^{\mathrm{tot}} & =2 \Omega_{1}\left[\lambda_{z}^{-1}+\gamma^{2} \lambda_{z}^{2}\right]-p, \\
\sigma_{z z}^{\mathrm{tot}} & =2 \Omega_{1} \lambda_{z}^{2}-2 \Omega_{5} E_{0}^{2} \lambda_{z}^{-2}-p, \\
\sigma_{z \phi}^{\mathrm{tot}} & =\sigma_{\phi z}^{\mathrm{tot}}=2 \Omega_{1} \gamma \lambda_{z}^{2} .
\end{aligned}
\tag{81}
$$

The material response to a torsion can be characterized by the torque $\mathcal{M}$ that has to be applied in order to achieve the prescribed deformation. The torque can defined as the integral over the cross section of the cylinder of the mechanical stress in azimuthal direction

$$
\mathcal{M}=2 \pi \int_{a_{i}}^{a_{e}} \sigma_{z \phi} r^{2} \mathrm{~d} r=2 \pi \int_{a_{i}}^{a_{e}}\left[\sigma_{z \phi}^{\mathrm{tot}}-\sigma_{z \phi}^{\max }\right] r^{2} \mathrm{~d} r.
\tag{82}
$$

As the entry of the Maxwell stress $\sigma_{z \phi}^{\max }$ for the applied magnetic field vanishes, this definition reduces to

$$
\mathcal{M}=2 \pi \int_{a_{i}}^{a_{e}} \sigma_{z \phi}^{\mathrm{tot}} r^{2} \mathrm{~d} r.
\tag{83}
$$

We assume that the cylinder consists of the same material with the same material parameters as in the previous example. Thus, using the definition of the Cauchy stress (81) combined with the derivatives of the energy function $\frac{\partial \Omega_{i}}{\partial I_{i}}=: \Omega_{i}$ and the solution of the heat equation (57) we find the following expression for the torque

$$
\begin{aligned}
& \mathcal{M}_{1}=\frac{\mu_{e} \pi \tau \lambda_{z}^{2}}{\Theta_{0}}\left[\frac{k_{1}}{4}\left[a_{e}^{4}-a_{i}^{4}\right]+\frac{k_{2}}{16}\left[a_{e}^{4}\left[4 \ln \left(a_{e}\right)-1\right]-a_{i}^{4}\left[4 \ln \left(a_{i}\right)-1\right]\right]\right], \\
& \mathcal{M}_{2}=\frac{\mu_{e} \pi \tau \lambda_{z}^{2}}{\Theta_{0}} \int_{a_{i}}^{a_{e}} k_{1} r^{2} \alpha_{e} \tanh \left(\frac{c^{2}}{\lambda_{z} r^{2}+\left[A_{i}^{2}-\lambda_{z} a_{i}^{2}\right]}\right) \mathrm{d} r, \\
& \mathcal{M}_{3}=\frac{\mu_{e} \pi \tau \lambda_{z}^{2}}{\Theta_{0}} \int_{a_{i}}^{a_{e}} k_{2} r^{2} \ln (r) \alpha_{e} \tanh \left(\frac{c^{2}}{\lambda_{z} r^{2}+\left[A_{i}^{2}-\lambda_{z} a_{i}^{2}\right]}\right) \mathrm{d} r.
\end{aligned}
\tag{84}
$$

### 4.2.1. Results and discussions

We will start by investigating the magneto-mechanical loading case. Figure 9 illustrates the behavior of the torque $\mathcal{M}$ depending on the angle of torsion (a) and the axial stretch (b) in the case of an azimuthally applied magnetic field for selected values of the initial wall thickness $\zeta$. Figure 9 shows a linear dependency of the resulting torque on both the angle $\tau$ and the axial stretch $\lambda_{z}$. For $\tau=0$ the torque vanishes independently from the applied magnetic field and the axial stretch $\lambda_{z}$. In Figure 9(b) it can be observed that the torque does not vanish, as a constant torsion of the cylinder of $\tau=\pi / 4$ is assumed.

Now an additional radial temperature gradient is applied by changing the external surface temperature $\Theta_{e}$ while maintaining the internal surface temperature at $293 \mathrm{~K}$. Figure 10 shows the dependency of the torque $\mathcal{M}$ depending on the angle of torsion (a) and the axial stretch (b) in the thermo-magneto-mechanical loading case.

In both cases the effect of the temperature is clearly visible, as the torque is increased when the external surface is heated while the torque decreases when the external surface is cooled down.

Finally we analyze the influence of the wall thickness $\zeta$ and the electric current $c$ that induces the azimuthal magnetic field.

![](./images/813107845410062337_10.jpg)

Figure 9: Plot of the torque with respect to (a) $\tau$ and (b) $\lambda_{z}$ under a magneto-mechanically coupled load for selected values of $\zeta$

Figure 11(a) shows that for an increased wall thickness the moment that has to be applied in order to achieve the prescribed deformation increases as well. Furthermore a decreased surface temperature also leads to an increase of the applied moment $\mathcal{M}$. In Figure 11(b) the torque with respect to the applied electric current is depicted. The dominating increase of the torque results from the hyperbolic function in the energy function. Furthermore it is visible that a compression of the cylinder $(\lambda_{z}=0.5)$ decreases the moment $\mathcal{M}$ while a temperature gradient resulting from heating the external surface results in a decrease of $\mathcal{M}$.

## 5. Conclusions

In this contribution, we have presented a thermo-magneto-mechanically coupled framework for magneto- rheological elastomers that can operate in finite deformations. Although almost all of the early works on constitutive modelling of MREs assume isothermal formulations, the experimental characterization of magneto-sensitive elastomers under isothermal conditions is difficult to achieve. Furthermore, due to the inherent chemical composition of polymeric materials they are highly sensitive to temperature. Therefore, in order to model any realistic experimental data, a thermo-magneto-mechanically coupled formulation is necessary. Departing from relevant laws of thermodynamics, we derive a thermodynamically consistent for- mulation in which temperature is an independent variable in addition to the mechanical and magnetic fields. In order to demonstrate the applicability of our proposed constitutive framework, two non-homogeneous boundary value problems that have frequently been used in finite elasticity and magneto-elasticity are pre- sented. In the first example the mechanical load is a combination of radial inflation and axial extension, in the second example the mechanical deformation consists of an axial extension combined with torsion around the cylinder axis. In both cases the cylindrical thick-walled tube is subject to a circumferential magnetic field

![](./images/813107845410062337_11.jpg)

Figure 10: Plot of the torque with respect to (a) $\tau$ and (b) $\lambda_z$ under a thermo-magneto-mechanically coupled load for selected values of $\Theta_e$

and a radial temperature gradient. Polymeric materials are typically viscoelastic in nature, cf. [4]. Hence the proposed thermo-magneto-mechanical approach needs to be extended to incorporate the time-dependent behavior of the underlying polymer composites. In future contributions, a detailed finite element implemen- tation of the thermo-magneto-mechanically coupled formulation will be elaborated which will facilitate to simulate more complex real life boundary value problems. There are plans to identify relevant constitutive material parameters once suitable experimental data is available.

**Acknowledgements:**
The authors acknowledge the funding within the DFG project No. STE 544/52-1 and by the ERC advanced grant MOCOPOLY.


![](./images/813107845410062337_12.jpg)

Figure 11: Plot of the torque with respect to $\zeta$ for selected values of $c$ (a) and with respect to $c$ for selected values of $\lambda_{z}$ (b) under a thermo-magneto-mechanically coupled load

### 5.1. Appendix
#### 5.1.1. Derivation of the Pressure
With the energy function derived from (42) and (44) and under the assumption that the influence of the free space can be neglected we find the derivatives of the energy with respect to the six invariants as

$$
\begin{aligned}
& \Omega_{1}=\frac{\Theta(r)}{\Theta_{0}} \frac{\mu_{e}}{4}\left[1+\alpha_{e} \tanh \left(\frac{I_{4}}{m_{e}}\right)\right], \quad \Omega_{2}=\Omega_{6}=0, \quad \Omega_{4}=\frac{\Theta(r)}{\Theta_{0}} \frac{\mu_{e}}{2 m_{e}} \alpha_{e} \frac{1}{\cosh \left(\frac{I_{4}}{m_{e}}\right)}+c_{1}, \\
& \Omega_{5}=\frac{\Theta(r)}{\Theta_{0}} c_{2}
\end{aligned}
\tag{85}
$$

In order to abbreviate the formulation, the hyperbolic term in the field sensitive shear modulus will be condensed to the expression $a=\alpha_{e} \tanh \left(\frac{I_{4}}{m_{e}}\right)$. The formulation of the pressure presented in (73) takes the form

$$
P=\underbrace{\int_{a_{i}}^{a_{e}} \frac{2}{r} \Omega_{1}\left[\lambda^{2}-\lambda^{-2} \lambda_{z}^{-2}\right] \mathrm{d} r}_{P_{1}}-\underbrace{\int_{a_{i}}^{a_{e}} \frac{2}{r} \lambda^{-2} \Omega_{5} I_{4} \mathrm{~d} r}_{P_{2}}+\frac{1}{2} \mu_{0} c^{2}\left[\frac{1}{a_{i}^{2}}-\frac{1}{a_{e}^{2}}\right].
\tag{86}
$$

In the following calculations we will use the definition of the fourth invariant $I_{4}=\mathbb{H}_{\Phi}^{2}=\frac{c^{2}}{R^{2}}$ and the solution of the heat equation $\Theta(r)=k_{1}+k_{2} \ln (r)$. Furthermore the connection between a radius $r$ in the spatial configuration and $R$ in the material configuration derived from the conservation of the volume of the

cylinder is given by $R^{2}=\lambda_{z} r^{2}+\left[A_{i}^{2}-\lambda_{z} a_{i}^{2}\right]=\lambda_{z} r^{2}+b$. For the first term in (86) we find

$$
P_{1}=\int_{a_{i}}^{a_{e}} \frac{2}{r} \Omega_{1}\left[\lambda^{2}-\lambda^{-2} \lambda_{z}^{-2}\right] \mathrm{d} r=\frac{\mu_{e}}{2 \Theta_{0}} \int_{a_{i}}^{a_{e}} \frac{k_{1}+k_{2} \ln (r)}{r}[1+a]\left[\frac{r^{2}}{\lambda_{z} r^{2}+b}-\frac{\lambda_{z} r^{2}+b}{\lambda_{z}^{2} r^{2}}\right]
\tag{87}
$$

The multiplication of the expression inside the integral results in six terms that are evaluated separately. The first term can be solved completely analytically and results in an expression comparable to the one derived for the isothermal case (76.1)

$$
\begin{aligned}
\text { Term } 1 & =\frac{\mu_{e}}{2 \Theta_{0}} \int_{a_{i}}^{a_{e}} \frac{k_{1}}{r}\left[\frac{r^{2}}{\lambda_{z} r^{2}+b}-\frac{\lambda_{z} r^{2}+b}{\lambda_{z}^{2} r^{2}}\right] \\
& =\frac{\mu_{e}}{2 \Theta_{0}} k_{1}\left[\frac{1}{\lambda_{z}} \ln \left(\frac{\lambda_{i}}{\lambda_{e}}\right)-\frac{1}{2 \lambda_{z}^{2}}\left[\lambda_{i}^{-2}-\lambda_{e}^{-2}\right]\right]
\end{aligned}
\tag{88}
$$

The second expression contains a logarithmic term and can therefore only partly be solved analytically.

$$
\begin{aligned}
\text { Term } 2= & \frac{\mu_{e}}{2 \Theta_{0}} \int_{a_{i}}^{a_{e}} \frac{k_{2}}{r}\left[\frac{r^{2} \ln (r)}{\lambda_{z} r^{2}+b}-\frac{\left[\lambda_{z} r^{2}+b\right] \ln (r)}{\lambda_{z}^{2} r^{2}}\right] \mathrm{d} r \\
= & \frac{\mu_{e}}{2 \Theta_{0}} k_{2} \int_{a_{i}}^{a_{e}} \frac{r \ln (r)}{\lambda_{z} r^{2}+b} \mathrm{~d} r \\
& -\frac{\mu_{e}}{2 \Theta_{0}} k_{2}\left[\frac{1}{2 \lambda_{z}}\left[\ln ^{2}\left(a_{e}\right)-\ln ^{2}\left(a_{i}\right)\right]-\frac{b}{\lambda_{z}^{2}}\left[\frac{\ln \left(a_{e}\right)}{2 a_{e}^{2}}-\frac{\ln \left(a_{i}\right)}{2 a_{i}^{2}}+\frac{1}{4}\left[a_{e}^{-2}-a_{i}^{-2}\right]\right]\right]
\end{aligned}
\tag{89}
$$

The remaining integral has to be evaluated using numerical integration methods. The same holds true for the remaining four terms, that can not be integrated analytically as the hyperbolic function renders these expressions too complex

$$
\begin{aligned}
\text { Term } 3 & =\frac{\mu_{e}}{2 \Theta_{0}} \int_{a_{i}}^{a_{e}} \frac{k_{1}}{r} \alpha_{e} \tanh \left(\frac{c^{2}}{\lambda_{z} r^{2}+b}\right) \frac{r^{2}}{\lambda_{z} r^{2}+b} \mathrm{~d} r, \\
\text { Term } 4 & =\frac{\mu_{e}}{2 \Theta_{0}} \int_{a_{i}}^{a_{e}} \frac{k_{2}}{r} \alpha_{e} \ln (r) \tanh \left(\frac{c^{2}}{\lambda_{z} r^{2}+b}\right) \frac{r^{2}}{\lambda_{z} r^{2}+b} \mathrm{~d} r, \\
\text { Term } 5 & =-\frac{\mu_{e}}{2 \Theta_{0}} \int_{a_{i}}^{a_{e}} \frac{k_{1}}{r} \alpha_{e} \tanh \left(\frac{c^{2}}{\lambda_{z} r^{2}+b}\right) \frac{\lambda_{z} r^{2}+b}{\lambda_{z}^{2} r^{2}} \mathrm{~d} r, \\
\text { Term } 6 & =-\frac{\mu_{e}}{2 \Theta_{0}} \int_{a_{i}}^{a_{e}} \frac{k_{2}}{r} \ln (r) \alpha_{e} \tanh \left(\frac{c^{2}}{\lambda_{z} r^{2}+b}\right) \frac{\lambda_{z} r^{2}+b}{\lambda_{z}^{2} r^{2}} \mathrm{~d} r.
\end{aligned}
\tag{90}
$$


The expression $P_2$ from Equation (86) can be solved completely analytically for the current thermo-magneto-mechanical loading case

$$
\begin{aligned}
P_{2}= & -\int_{a_{i}}^{a_{e}} \frac{2}{r} \lambda^{-2} \Omega_{5} I_{4} \mathrm{~d} r+\frac{1}{2} \mu_{0} c^{2}\left[\frac{1}{a_{i}^{2}}-\frac{1}{a_{e}^{2}}\right] \\
= & -2 \int_{a_{i}}^{a_{e}} \frac{1}{r} \frac{R^{2}}{r^{2}} \frac{\Theta(r)}{\Theta_{0}} c_{2} \frac{c^{2}}{R^{2}} \mathrm{~d} r+\frac{1}{2} \mu_{0} c^{2}\left[\frac{1}{a_{i}^{2}}-\frac{1}{a_{e}^{2}}\right] \\
= & -\frac{2 c^{2} c_{2}}{\Theta_{0}} \int_{a_{i}}^{a_{e}} \frac{1}{r^{3}}\left[k_{1}+k_{2} \ln (r)\right] \mathrm{d} r+\frac{1}{2} \mu_{0} c^{2}\left[\frac{1}{a_{i}^{2}}-\frac{1}{a_{e}^{2}}\right] \\
= & -\frac{2 c^{2} c_{2} k_{1}}{\Theta_{0}}\left[a_{i}^{-2}-a_{e}^{-2}\right]-\frac{k_{2} c^{2} c_{2}}{2 \Theta_{0}}\left[a_{i}^{-2}-a_{e}^{-2}\right] \\
& +\frac{k_{2} c^{2} c_{2}}{\Theta_{0}}\left[\frac{\ln \left(a_{e}\right)}{a_{e}^{2}}-\frac{\ln \left(a_{i}\right)}{a_{i}^{2}}\right]+\frac{1}{2} \mu_{0} c^{2}\left[\frac{1}{a_{i}^{2}}-\frac{1}{a_{e}^{2}}\right]
\end{aligned}
\tag{91}
$$

If we consider $c_{2}=\frac{\mu_{0}}{2}$ the expression can be abbreviated but due to the temperature dependency the terms do not cancel out as it was the case in Equation (75). We find an formulation in the form

$$
\begin{aligned}
P_{2} & =-c^{2} \frac{\mu_{0} k_{1}}{2 \Theta_{0}}\left[a_{i}^{-2}-a_{e}^{-2}\right]-\frac{k_{2} c^{2} \mu_{0}}{4 \Theta_{0}}\left[a_{i}^{-2}-a_{e}^{-2}\right]+k_{2} c^{2} \frac{\mu_{0}}{2 \Theta_{0}}\left[\frac{\ln \left(a_{e}\right)}{a_{e}^{2}}-\frac{\ln \left(a_{i}\right)}{a_{i}^{2}}\right]+\frac{1}{2} \mu_{0} c^{2}\left[\frac{1}{a_{i}^{2}}-\frac{1}{a_{e}^{2}}\right] \\
= & \frac{1}{2} \mu_{0} c^{2}\left[1-\frac{k_{1}}{\Theta_{0}}\right]\left[\frac{1}{a_{i}^{2}}-\frac{1}{a_{e}^{2}}\right]-\frac{k_{2} c^{2} \mu_{0}}{4 \Theta_{0}}\left[a_{i}^{-2}-a_{e}^{-2}\right]+k_{2} c^{2} \frac{\mu_{0}}{2 \Theta}\left[\frac{\ln \left(a_{e}\right)}{a_{e}^{2}}-\frac{\ln \left(a_{i}\right)}{a_{i}^{2}}\right]
\end{aligned}
\tag{92}
$$

The summation of the terms of $P_{1}$ and $P_{2}$ will give the final result for the pressure on the internal surface of the tube in the thermo-magneto-mechanical loading case with a field sensitive shear modulus.

#### 5.1.2. Derivation of the Normal Force

For the derivation of the normal force we will proceed as in the previous section for the pressure. The presented derivatives of the energy function in Equation (85) will be used here as well. We will start with the definition of the normal force as shown in Equation (78) and insert the expressions of the total Cauchy stress from Equation (34) and the definition of the Maxwell stress from (60) in axial direction.

$$
\mathcal{N}=2 \pi \int_{a_{i}}^{a_{e}}\left[\sigma_{z z}^{\mathrm{tot}}-\sigma_{z z}^{\max }\right] r \mathrm{~d} r=2 \pi \int_{a_{i}}^{a_{e}}\left[-p+2 \lambda_{z}^{2} \Omega_{1}-\frac{1}{2} \mu_{0} \lambda_{z}^{-2} \frac{c^{2}}{r^{2}}\right] r \mathrm{~d} r.
\tag{93}
$$

An expression for the Lagrange multiplier $p$ can be found by using the definition of the radial and azimuthal stress components of the Cauchy stress from Equation (34)

$$
\begin{aligned}
& \sigma_{r r}^{\mathrm{tot}}+\sigma_{\phi \phi}^{\mathrm{tot}}=-2 p+2\left[\lambda^{-2} \lambda_{z}^{-2}+\lambda^{2}\right] \Omega_{1}-2 \lambda^{-2} \frac{c^{2}}{R^{2}} \Omega_{5} \\
& -p=\frac{1}{2}\left[\sigma_{r r}^{\mathrm{tot}}+\sigma_{\phi \phi}^{\mathrm{tot}}\right]-\left[\lambda^{-2} \lambda_{z}^{-2}+\lambda^{2}\right] \Omega_{1}+\lambda^{-2} \frac{c^{2}}{R^{2}} \Omega_{5}.
\end{aligned}
\tag{94}
$$

Inserting this expression into the definition of the normal force leads to a lengthy equation that is decomposed into three sub terms

$$
\begin{aligned}
\mathcal{N}= & 2 \pi \int_{a_{i}}^{a_{e}}\left[\frac{1}{2}\left[\sigma_{r r}^{\mathrm{tot}}+\sigma_{\phi \phi}^{\mathrm{tot}}\right]+\left[2 \lambda_{z}^{2}-\lambda^{-2} \lambda_{z}^{-2}-\lambda^{2}\right] \Omega_{1}+\lambda^{-2} \frac{c^{2}}{R^{2}} \Omega_{5}-\frac{1}{2} \mu_{0} \lambda_{z}^{-2} \frac{c^{2}}{r^{2}}\right] r \mathrm{~d} r \\
= & \underbrace{\pi \int_{a_{i}}^{a_{e}} r\left[\sigma_{r r}^{\mathrm{tot}}+\sigma_{\phi \phi}^{\mathrm{tot}}\right]}_{\mathcal{N}_{1}}+\underbrace{2 \pi \int_{a_{i}}^{a_{e}} r\left[2 \lambda_{z}^{2}-\lambda^{-2} \lambda_{z}^{-2}-\lambda^{2}\right] \Omega_{1} \mathrm{~d} r}_{\mathcal{N}_{2}} \\
& +\underbrace{2 \pi \int_{a_{i}}^{a_{e}} r \lambda^{-2} \frac{c^{2}}{R^{2}} \Omega_{5} \mathrm{~d} r-2 \pi \int_{a_{i}}^{a_{e}} \frac{1}{2} \mu_{0} \lambda_{z}^{-2} \frac{c^{2}}{r^{2}} r \mathrm{~d} r}_{\mathcal{N}_{3}}
\end{aligned}
\tag{95}
$$

Using the transformed definition in Equation (65a) to $\frac{\partial \sigma_{r r}^{\text {tot }}}{\partial r} r=\sigma_{r r}^{\text {tot }}-\sigma_{\phi \phi}^{\text {tot }}$ we can calculate the expression in $\mathcal{N}_{1}$ as a simple scaling of the pressure, derived in the previous chapter

$$
\begin{aligned}
\pi \int_{a_{i}}^{a_{e}} r\left[\sigma_{r r}^{\mathrm{tot}}+\sigma_{\phi \phi}^{\mathrm{tot}}\right] & =\frac{\pi}{2}\left[a_{e}^{2} \sigma_{r r}^{\max }\left(a_{e}\right)\right]-\frac{\pi}{2}\left[a_{i}^{2} \sigma_{r r}^{\max }\left(a_{i}\right)\right]+\frac{1}{2} \pi a_{i}^{2} P+\frac{1}{2} \pi \int_{a_{i}}^{a_{e}} r\left[\sigma_{r r}^{\mathrm{tot}}+\sigma_{\phi \phi}^{\mathrm{tot}}\right] \\
\pi \int_{a_{i}}^{a_{e}} r\left[\sigma_{r r}^{\mathrm{tot}}+\sigma_{\phi \phi}^{\mathrm{tot}}\right] & =\underbrace{\pi\left[a_{e}^{2} \sigma_{r r}^{\max }\left(a_{e}\right)\right]-\pi\left[a_{i}^{2} \sigma_{r r}^{\max }\left(a_{i}\right)\right]}_{=0}+\pi a_{i}^{2} P=\pi a_{i}^{2} P.
\end{aligned}
\tag{96}
$$

If we insert $\Omega_{1}$ into the expression of $\mathcal{N}_{2}$ we end up with a lengthy equation.

$$
\begin{aligned}
& 2 \pi \int_{a_{i}}^{a_{e}} r\left[2 \lambda_{z}^{2}-\lambda^{-2} \lambda_{z}^{-2}-\lambda^{2}\right] \Omega_{1} \mathrm{~d} r=2 \pi \int_{a_{i}}^{a_{e}} r\left[2 \lambda_{z}^{2}-\lambda^{-2} \lambda_{z}^{-2}-\lambda^{2}\right] \frac{\Theta(r)}{\Theta_{0}} \frac{\mu_{e}}{4}\left[1+\alpha_{e} \tanh \left(\frac{c^{2}}{R^{2}}\right)\right] \mathrm{d} r \\
= & \frac{\pi \mu_{e}}{2 \Theta_{0}} \int_{a_{i}}^{a_{e}} r\left[k_{1}+k_{2} \ln (r)\right]\left[2 \lambda_{z}^{2}-\lambda^{-2} \lambda_{z}^{-2}-\lambda^{2}\right]\left[1+\alpha \tanh \left(\frac{c^{2}}{r^{2} \lambda_{z}+b}\right)\right] \mathrm{d} r
\end{aligned}
\tag{97}
$$


As it was the case for the pressure, by expanding this expression we end up with a number of terms that can only partly be evaluated analytically. For the simplest of these terms we can find the following analytical solution

$$
\text { Term } 1=\frac{\pi \mu_{e}}{2 \Theta_{0}} \int_{a_{i}}^{a_{e}} r k_{1}\left[2 \lambda_{z}^{2}-\lambda^{-2} \lambda_{z}^{-2}-\lambda^{2}\right] \mathrm{d} r=\frac{\pi \mu_{e} k_{1}}{2 \Theta_{0}}\left[\left[\lambda_{z}^{2}-\frac{1}{\lambda_{z}}\right]\left[a_{e}^{2}-a_{i}^{2}\right]+\frac{b}{\lambda_{z}^{2}} \ln \left(\frac{\lambda_{i}}{\lambda_{e}}\right)\right] \text {. }
$$

Another term differing from the first only in the thermal constant $k_{2}$ instead of $k_{1}$ and the multiplication with $\ln (r)$ can be solved partly analytically

$$
\begin{aligned}
\text { Term } 2= & \frac{\pi \mu_{e}}{2 \Theta_{0}} \int_{a_{i}}^{a_{e}} r k_{2}\left[2 \lambda_{z}^{2}-\lambda^{-2} \lambda_{z}^{-2}-\lambda^{2}\right] \ln (r) \mathrm{d} r \\
= & \frac{\pi \mu_{e} k_{2}}{2 \Theta_{0}}\left[\int_{a_{i}}^{a_{e}}\left[2 \lambda_{z}^{2}-\frac{1}{\lambda_{z}}\right] r \ln (r) \mathrm{d} r-\int_{a_{i}}^{a_{e}} \frac{b}{r \lambda_{z}^{2}} \ln (r) \mathrm{d} r-\int_{a_{i}}^{a_{e}} \frac{r^{3} \ln (r)}{r^{2} \lambda_{z}+b} \mathrm{~d} r\right] \\
= & \frac{\pi \mu_{e} k_{2}}{2 \Theta_{0}}\left[\left[2 \lambda_{z}^{2}-\frac{1}{\lambda_{z}}\right]\left[\frac{1}{2}\left[a_{e}^{2} \ln \left(a_{e}\right)-a_{i}^{2} \ln \left(a_{i}\right)\right]-\frac{1}{4}\left[a_{e}^{2}-a_{i}^{2}\right]\right]-\frac{b}{2 \lambda_{z}^{2}}\left[\ln ^{2}\left(a_{e}\right)-\ln ^{2}\left(a_{i}\right)\right]\right] \\
& -\frac{\pi \mu_{e} k_{2}}{2 \Theta_{0}} \int_{a_{i}}^{a_{e}} \frac{r^{3} \ln (r)}{r^{2} \lambda_{z}+b} \mathrm{~d} r.
\end{aligned}
$$

The two final terms containing the hyperbolic tangent function are too complex to be evaluated analytically. Therefore numerical integration has to be employed

$$
\begin{aligned}
& \text { Term } 3=\frac{\pi \mu_{e}}{2 \Theta_{0}} \int_{a_{i}}^{a_{e}} r k_{1}\left[2 \lambda_{z}^{2}-\lambda^{-2} \lambda_{z}^{-2}-\lambda^{2}\right] \alpha_{e} \tanh \left(\frac{c^{2}}{R^{2}}\right) \mathrm{d} r, \\
& \text { Term } 4=\frac{\pi \mu_{e}}{2 \Theta_{0}} \int_{a_{i}}^{a_{e}} r k_{2} \ln (r)\left[2 \lambda_{z}^{2}-\lambda^{-2} \lambda_{z}^{-2}-\lambda^{2}\right] \alpha_{e} \tanh \left(\frac{c^{2}}{R^{2}}\right) \mathrm{d} r.
\end{aligned}
$$

Returning to Equation (95) $\mathcal{N}_{3}$ is the final term left to evaluate. When inserting the definition of $\lambda=\frac{r}{R}$ and $\Omega_{5}=\frac{\Theta(r)}{\Theta_{0}} c_{2}$ we find

$$
\mathcal{N}_{3}=2 \pi \int_{a_{i}}^{a_{e}} \frac{c^{2}}{r} \frac{\Theta(r)}{\Theta_{0}} c_{2} \mathrm{~d} r-2 \pi \int_{a_{i}}^{a_{e}} \frac{1}{2} \mu_{0} \lambda_{z}^{-2} \frac{c^{2}}{r^{2}} r \mathrm{~d} r=2 \pi c^{2} \int_{a_{i}}^{a_{e}} \frac{1}{r}\left[\frac{\Theta(r)}{\Theta_{0}} c_{2}-\lambda_{z}^{-2} \frac{\mu_{0}}{2}\right] \mathrm{d} r.
$$

With the material parameter $c_{2}=\frac{\mu_{0}}{2}$ and the solution to the heat equation we find an expression that can be solved analytically

$$
\begin{aligned}
\mathcal{N}_{3}= & \mu_{0} \pi c^{2} \int_{a_{i}}^{a_{e}} \frac{1}{r}\left[\frac{k_{1}}{\Theta_{0}}-\lambda_{z}^{-2}\right] \frac{1}{r}+\frac{k_{2}}{\Theta_{0}} \frac{\ln (r)}{r} \mathrm{~d} r \\
= & \mu_{0} \pi c^{2}\left[\left[\frac{k_{1}}{\Theta_{0}}-\lambda_{z}^{-2}\right] \ln \left(\frac{a_{e}}{a_{i}}\right)+\frac{k_{2}}{2 \Theta_{0}}\left[\ln ^{2}\left(a_{e}\right)-\ln ^{2}\left(a_{i}\right)\right]\right]
\end{aligned}
$$

The summation of all the terms of $\mathcal{N}_{1}$ to $\mathcal{N}_{3}$ will give the final result for the normal force on the end surfaces of the tube in the thermo-magneto-mechanical loading case with a field sensitive shear modulus.

References:

References

[1] Albanese, A.M., Cunefare, K.A., 2003. Properties of magnetorheological semiactive vibration ab- sorber, in Agnes, G.S., Wang, K.-W. (Eds.), Smart Structures and Materials: Damping and Isolation, SPIE Proceedings 5052, pp. 36–43. SPIE Press.

[2] Arruda E, M. C. Boyce, A three-dimensional constitutive model for the large stretch behavior of rubber elastic materials, Journal of the Mechanics and Physics of Solids, 41:389-412,1993

[3] Brigadnov, I.A., Dorfmann, A., 2003. Mathematical modeling of magneto-sensitive elastomers. Int. J. Solids Structures 40, 4659–4674

[4] Bergström J S, M. C. Boyce, Constitutive modeling of the large strain time-dependent behavior of elastomers, Journal of the Mechanics and Physics of Solids, 46:931-954, 1998

[5] Bustamante R, Transversely isotropic nonlinear magneto-active elastomers, Acta Mechanica, 210(3-4):183-214, 2010

[6] Bustamante R, A variational formulation for a boundary value problem considering an electro-sensitive elastomer interacting with two bodies, Mechanics Research Communication 36 (7):791-795, 2009

[7] Bustamante, R., Shariff, M.H.B.M., 2015. A principal axis formulation for nonlinear magnetoelastic deformations: Isotropic bodies. European Journal of Mechanics A/ Solids 50:17-27

[8] Bustamante, R., Dorfmann, A., Ogden, R.W., 2008. On variational formulations in nonlinear magne- toelastostatics. Math. Mech. Solids 13, 725–745.

[9] Bustamante, R., Dorfmann, A., Ogden, R.W., 2011. Numerical solution of finite geometry boundary value problems in nonlinear magnetoelasticity. Int. J. Solids Structures 48, 874–883.

[10] Bland D R, Elastoplastic thick-walled tubes of work-hardening material subject to internal and external pressures and to temperature gradients, Journal of the Mechanics and Physics of Solids, 4:209-229, 1956

[11] Böse, H., 2007. Viscoelastic properties of silicone-based magnetorheological elastomers. Int. J. Mod. Phys. B 21, 4790–4797.

[12] Böse, H., Rabindranath, R., Ehrlich, J., 2012. Soft magnetorheological elastomers as new actuators for valves. J. Intelligent Material Systems and Structures 23, 989–994.

[13] Bednarek, S., 1999. The giant magnetostriction in ferromagnetic composites within an elastomer ma- trix. Appl. Phys. A 68, 63–67.

[14] Bellan, C., Bossis, G., 2002. Field dependence of viscoelastic properties of MR elastomers. Int. J. Modern Physics B 16, 2447- 2453.

[15] Bica, I., 2012. The influence of the magnetic field on the elastic properties of anisotropic magnetorhe- ological elastomers. J. Ind. Eng. Chem. 18, 1666–1669.

[16] Boczkowska, A., Awietjan, S.F., 2009. Smart composites of urethane elastomers with carbonyl iron. J. Mater. Sci. 44, 4104-4111.

[17] Boczkowska, A., Awietjan, S.F., 2012. Microstructure and properties of magnetorheological elas- tomers. In Advanced Elastomers-Technology, Properties and Applications, Ed. Boczkowska, A. DOI:10.5772/2784 pp.147-180.

[18] Brown, W.F., 1966. Magnetoelastic Interactions, Springer, Berlin.

[19] Chadwick P, Thermo-mechanics of rubberlike materials, Philosophical Transactions of the Royal So- ciety of London. Series A, Mathematical and Physical Sciences, 276:371-403, 1974

[20] Coleman B D, M. E. Gurtin, Thermodynamics with internal state variables, Journal of Chemical Physics, 47:597-613, 1967

[21] Chen X, On magneto-thermo-viscoelastic deformation and fracture, International Journal of Non- Linear Mechanics, 44:244-248, 2009

[22] Dorfmann A, R. W. Ogden, Magnetoelastic modelling of elastomers, European Journal of Mechanics A/Solids, 22(4):497-507, 2003

[23] Dorfmann A, R. W. Ogden, Nonlinear magnetoelastic deformations of elastomers, Acta Mechanica, 167(1-2):13-28, 2004

[24] Dorfmann A, R. W. Ogden, Nonlinear magnetoelastic deformations, Quarterly Journal of Mechanics and Applied Mathematics, 57(4):599-622, 2004

[25] Dorfmann A, R. W. Ogden, Some problems in nonlinear magnetoelasticity, ZAMP, 56(4):718-745, 2005

[26] Dorfmann A, I. A. Brigdanov, Constitutive modelling of magneto-sensitive Cauchy elastic solids, Computational Materials Science, 29(3):270-282, 2004

[27] S. Lu, K. Pister, *Decomposition of deformation and representation of the free energy function for isotropic thermoelastic solids*, International Journal of Solids and Structures, vol. 11 (7-8), pp.927-935 (1975).

[28] Danas, K., Kankanala, S. V., Triantafyllidis, N., 2012. Experiments and modelling of iron-particled- filled magnetorheological elastomers. J. Mech. Phys. Solids 60(1), 120-138.

[29] Deng, H., Gong, X., 2008. Application of magnetorheological elastomer to vibration absorber. Com- mun. Nonlinear Sci. 13, 1938-1947.

[30] Erbts P, S. Hartmann, A. Düster, A partitioned solution approach for electro-thermo-mechanical prob- lems, Archive of Applied Mechanics, 85:1075-1101, 2015

[31] Eringen A C, G. A. Maugin, Electrodynamics of Continua, Springer-Verlag (1990)

[32] Farshad, M., Le Roux, M., 2004. A new active noise abatement barrier system. Polymer Testing 23, 855-860.

[33] Galipeau, E., Ponte-Castañeda, P., 2013. Giant field-induced strains in magnetoactive elastomers com- posites. Proc. R. Soc. 469, 20130385.

[34] Ghafoorianfar, N., Wang, X., Gordaninejad, F., 2013. On the sensing of magnetorheological elas- tomers. Sensors and Smart Structures Technologies for Civil, Mechanical, and Aerospace Systems, Eds. Lynch, JP., Yun, CB., Wang, KW., Proc. of SPIE vol.8692, paper 869214.

[35] Ginder, J.M., Nichols, M.E., Elie, L.D., Tardiff, J.L., 1999. Magnetorheological elastomers: proper- ties and applications, in Wuttig, M.R. (Ed.), SPIE Proceedings 3675, Smart Structures and Materials: Smart Materials Technologies, pp. 131- 138. SPIE Press.

[36] Ginder, J.M., Nichols, M.E., Elie, L.D., Clark, S.M., 2000. Controllable stiffness components based on magnetorheological elastomers, in Wereley, N.M. (Ed.), Smart Structures and Materials: Smart Structures and Integrated Systems, SPIE Proceedings 3985, pp. 418-425. SPIE Press.

[37] Ginder, J.M., Schlotter, W.F., Nichols, M.E., 2001. Magnetorheological elastomers in tunable vibra- tion absorbers, in Smart Structures and Materials: Damping and Isolation, Inman, D.J. (Ed.), SPIE Proceedings 4331, pp. 103-110. SPIE Press.

[38] Ginder, J.M., Clark, S.M., Schlotter, W.F., Nichols, M.E., 2002. Magnetostrictive phenomena in mag- netorheological elastomers. Int. J. Modern Phys. B 16, 2412-2418.

[39] Gordaninejad, F., Wang, W., Mysore, P., 2012. Behavior of thick magnetorheological elastomers. J. Intel. Mat. Syst. Str. 23, 1033-1039.

[40] Griffiths D J, Introduction to Electrodynamics, 3rd ed. Prentice Hall (1998)

[41] Hossain, M., Saxena, P., Steinmann, P., 2015. Modelling the mechanical aspects of the curing process of magneto-sensitive elastomeric materials, International Journal of Solids and Structures 58: 257-269

[42] Hossain, M., Chatzigeorgiou, G., Meraghni, F., Steinmann, P., 2015. A multi-scale approach to model the curing process in magneto-sensitive polymeric materials, International Journal of Solids and Struc- tures, 69-70:34-44

[43] Hossain, M., Steinmann, P., 2013. More hyperelastic models for rubber-like materials: Consistent tangent operator and comparative study, Journal of the Mechanical Behaviour of Materials 22(1-2):27-50

[44] Hossain M, N. Kabir, A. F. M. S. Amin, Eight-chain and full-network models and their modified versions for rubber hyperelasticity : A comparative study, Journal of the Mechanical Behaviour of Materials, 24(1-2):11-24, 2015

[45] Hossain M, D. K. Vu, P. Steinmann, Experimental study and numerical modelling of VHB 4910 poly- mer, Computational Materials Science, 59:65-74, 2012

[46] Holzapfel G A, J. C. Simo, Entropy elasticity of isotropic rubber-like solids at finite strains, Computer Methods in Appied Mechanics and Engineering, 132:17-44,1996

[47] Jolly, M.R., Carlson, J.D., Muñoz, B.C., 1996. A model of the behaviour of magnetorheological mate- rials. Smart Mater. Struct. 5. 607-614.

[48] Kankanala, S.V., Triantafyllidis, N., 2004. On finitely strained magnetorheological elastomers. J. Mech. Phys. Solids 52, 2869-2908.

[49] Kashima, S., Miyasaka, F., Hirata, K., 2012. Novel soft actuator using magnetorheological elastomer. IEEE T. Magn. 48, 1649-1652.

[50] Kovetz, A., 2000. Electromagnetic Theory, University Press, Oxford.

[51] Leslie D J, N. H. Scott, Incompressibility at uniform temperature or entropy in isotropic thermoelas-ticity, Quarterly Journal of Applied Mathematics, 51(2):191-211, 1998

[52] Lokander, M., Stenberg, B., 2003. Performance of isotropic magnetorheological rubber materials. Polym. Testing 22, 245-251.

[53] Mehnert M, M Hossain, P Steinmann, On nonlinear thermo-electro-elasticity, Proceedings of the Royal Society/ A, 472 (2190), 20160170, 2016

[54] Monk P, Finite Element Methods for Maxwell Equations, Oxford University Press, Clarendon (2003)

[55] Maugin, G.A., 1988. Continuum Mechanics of Electromagnetic Solids, North Holland, Amsterdam.

[56] Mitsumata, T., 2009. Recent progress in magnetorheological gels and elastomers. Recent Patents on Chemical Engineering 2, 159-166.

[57] Mitsumata, T., Ohori, S., 2011. Magnetic polyurethane elastomers with wide range modulation of elasticity. Polymer Chemistry 2, 1063-1067.

[58] Pao Y H, Electromagnetic forces in deformable continua, Mechanics Today, (Nemat- Nasser, S., ed.), Oxford: Pergamon Press. 1978; 4:209-306.

[59] Pelteret J P, D Davydov, A McBride, D K Vu, P Steinmann, 2016 Computational electro- and magneto-elasticity for quasi-incompressible media immersed in free space International Journal for Numerical Methods in Engineering 108 (11), 1307-1342

[60] Rajagopal K R, Y. N. Huang, Finite circumferential shearing of nonlinear solids in the context of thermoelasticity, Journal of Applied Mathematics, 53:111-125, 1994

[61] Steinmann P, M. Hossain, G. Possart, Hyperelastic models for rubber-like materials: Consistent tangent operators and suitability of Treloar's data, Archive of Applied Mechanics, 82(9):1183-1217, 2012

[62] Steigmann D J, Equilibrium theory for magnetic elastomers and magnetoelastic membranes, Interna-tional Journal of Non-Linear Mechanics, 39(7):1193-1216, 2004

[63] Saxena P, M. Hossain, P. Steinmann A theory of finite deformation magneto-viscoelasticity, Interna-tional Journal of Solids and Structures, 50(24):3886-3897, 2013

[64] Saxena P., Hossain, H., Steinmann, P., 2014. Nonlinear magneto-viscoelasticity of transversally isotropic magneto-active polymers. Proc. R. Soc. A. 470, 20140082.

[65] Saxena P., J P Pelteret, P Steinmann, P., 2015, Modelling of iron-filled magneto-active polymers with a dispersed chain-like microstructure European Journal of Mechanics-A/Solids 50, 132-151

[66] Santapuri S, R. L. Lowe, S. E. Bechtel, M. J. Dapino, Thermodynamic modeling of fully coupled finite-deformation thermo-electro-magneto-mechanical behavior for multifunctional applications, In- ternational Journal of Engineering Science, 72:117-139, 2013

[67] Santapuri S, Unified continuum modeling of fully coupled thermo-electro-magneto-mechanical behav- ior with applications to multifunctional materials and structures, PhD Thesis, Ohio State University, USA, 2012

[68] Shariff, M.H.B.M, 2008. Nonlinear transversely isotropic elastic solids: An alternative representation. Quat. J. Mech. Appl. Math. 61, 129-149.

[69] Shariff, M.H.B.M, 2011. Physical invariants for nonlinear orthotropic solids. Int. J. Solids Structures.48, 1906-1914.

[70] Shariff, M.H.B.M, R Bustamante, M Hossain, P Steinmann, A novel spectral formulation for trans- versely isotropic magneto-elasticity, Mathematics and Mechanics of Solids, in Press, 2016

[71] Tiersten, H.F., 1964. Coupled magnetomechanical equations for magnetically saturated insulators. J. Mathematical Physics 5, 1298-1318.

[72] Vogel F, *On the modeling and computation of electro- and magneto-active polymers*, Dissertation, Friedrich-Alexander-University Erlangen-Nuremberg, Germany, 2014.

[73] Vogel F, S. Goektepe, E. Kuhl, P. Steinmann, Modeling and simulation of viscous electro-active poly- mers, European Journal of Mechanics A/Solids, 48:112-128, 2014

[74] Vogel F, R. Bustamante, P. Steinmann, On some mixed variational principles in magneto elastostatics. International Journal of Nonlinear Mechanics, 51 (2013) 157-169

[75] Vertechy R, G. Berselli, V. P. Castelli, M. Bergamasco, Continuum thermo-electro-mechanical model for electrostrictive elastomers, Journal of Intelligent Material Systems and Structures, 24:761-778,2012

[76] Vertechy R, G. Berselli, V. P. Castelli, G. Vassura, Optimal design of Lozenge-shaped dielectric elas- tomer linear actuators: Mathematical procedure and experimental validation, Journal of Intelligent Material Systems and Structures, 21:503-515, 2010

[77] Vu D K, P. Steinmann, Numerical modeling of non-Linear electroelasticity, International Journal for Numerical Methods in Engineering, 70:685-704, 2007

[78] Vu D K, P. Steinmann, A 2-D coupled BEM-FEM simulation of electro-elastostatics at large strain, Computer Methods in Applied Mechanics and Engineering, 199:1124-1133, 2010

[79] Varga, Z., Filipcsei, G., Zrínyi, M., 2006. Magnetic field sensitive functional elastomers with tuneable modulus. Polymer 47, 227-233.

[80] Varga, Z., Filipcsei, G., Zríngi, M., 2005. Smart composites with controlled anisotropy. Polymer 47,7779-7787.

[81] Yalcintas, M., Dai, H., 2004. Vibration suppression capabilities of magnetorheological materials based adaptive structures. Smart. Mater. Struct. 13, 1-11.

[82] Zhu, JT., Xu, ZD., Guo, YQ., 2012. Magnetoviscoelasticity parametric model of a MR elastomer vibration device. Smart Matter. Struct. 21, 075034.

[83] L.R.G. Treloar, The Physics of Rubber Elasticity, Oxford University Press (1975).

[84] Van Loan C F, Introduction to Scientific Computing: A Matrix-Vector Approach Using MATLAB (2nd Edition), Prentice-Hall, 1999