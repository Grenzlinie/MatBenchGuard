# Coupled thermomechanical analysis of transformation-induced plasticity in multiphase steels
S. Yadegari $^{a, *}$, S. Turteltaub $^{a}$, A.S.J. Suiker $^{b}$

$^{a}$ Faculty of Aerospace Engineering, Delft University of Technology, Kluyverweg 1, 2629 HS Delft, The Netherlands
$^{b}$ Department of the Built Environment, Eindhoven University of Technology, P.O. Box 513, 5600 MB Eindhoven, The Netherlands

---

## ARTICLE INFO
**Article history:**
Received 10 October 2011
Received in revised form 16 April 2012
Available online 18 May 2012

**Keywords:**
Thermomechanics
Martensitic transformation
Multiphase steel
TRIP steel

---

## ABSTRACT
The thermomechanical response of low-alloyed multiphase steels assisted by transformation-induced plasticity (TRIP steels) is analyzed taking into account the coupling between the thermal and mechanical fields. The thermomechanical coupling is particularly relevant since in TRIP steels the phase transformation that occurs during mechanical loading is accompanied by the release of a considerable amount of energy (latent heat) that, in turn, affects the mechanical response of the material. The internal generation of heat associated with the martensitic phase transformation and the plastic deformation are modeled explicitly in the balance of energy. The momentum and energy equations are solved simultaneously by using a fully-implicit numerical scheme. The simulations are conducted using a micromechanical formulation for single crystals of austenite and ferrite. The characteristics of the model are illustrated by means of simulations for a single crystal of austenite and an aggregate of austenitic and ferritic grains. For a single crystal of austenite, it is found that the increase in local temperature due to transformation actually hinders further transformation and, instead, promotes plastic deformation. However, for an aggregate of austenitic and ferritic grains in a multiphase steel, the increase in temperature due to transformation is limited since the heat generated in the austenite is conducted to the ferritic matrix, effectively lowering the temperature in the austenitic phase.

© 2012 Elsevier Ltd. All rights reserved.

---

## 1. Introduction
Low-alloyed multiphase steels assisted by transformation-induced plasticity, commonly known as TRIP steels, have been identified as ideal candidates for applications requiring high strength-to-mass ratios, particularly in the automotive industry where fuel efficiency and safety are primary concerns. A distinctive characteristic of a TRIP steel is the presence of grains of metastable austenite in its microstructure, with volume fractions usually between 5 to 20%, embedded in a ferrite-based matrix (Jacques et al., 2001, 2007; Sugimoto et al., 1992). Due to the addition of small quantities of alloying elements such as Al or Si, the austenite is retained in the material during processing as it is cooled down to room temperature. The presence of retained austenite is critical for the transformation-induced plasticity effect. Indeed, upon subsequent application of mechanical and/or thermal loads during forming or operation, the austenite may transform into a harder phase, martensite, providing the material with enhanced work-hardening characteristics compared to more conventional high-strength steels.

In order to understand the details of the transformation-induced plasticity effect, various models have been proposed in the literature ranging from micromechanically-based formulations to purely phenomenological constitutive relations at a macroscopic level (Bhattacharyya and Weng, 1994; Idesman et al., 1999; Kouznetsova and Geers, 2008; Lani et al., 2007; Marketz and Fischer, 1994; Mazzoni-Leduc et al., 2008; Shi et al., 2008, 2010;

---
* Corresponding author.
E-mail addresses: S.Yadegari@tudelft.nl (S. Yadegari), S.R.Turteltaub@tudelft.nl (S. Turteltaub), A.S.J.Suiker@tue.nl (A.S.J. Suiker).

0167-6636/$ - see front matter © 2012 Elsevier Ltd. All rights reserved.
http://dx.doi.org/10.1016/j.mechmat.2012.05.002

Stringfellow et al., 1992;. These models have been mostly applied to study the isothermal response of a multiphase steel, typically at room temperature. Tensile tests conducted at various externally-controlled temperatures have shown that the martensitic transformation rate strongly depends on temperature (see, e.g., Berrahmoune et al. (2004) and Jiménez et al. (2009)), which indicates that a comprehensive investigation of this class of steels should include their thermal behavior. The thermal sensitivity of TRIP steels has been studied under different thermal loading paths in Tjahjanto et al. (2008b), where it was shown that the onset of inelastic response decreases with temperature. Nonetheless, that study also showed that upon continued deformation, the strength of a TRIP steel becomes the largest at the lowest temperature considered in the analyses. The simulations presented in Tjahjanto et al. (2008b) were carried out under the assumption that the temperature was externally-controlled and uniform within the sample, hence the energy equation was trivially satisfied. However, during actual operational conditions, the temperature is usually not controlled, hence the thermal behavior of the material depends on the internal heat generated by inelastic processes (transformation and plasticity). In particular, the phase transformation is accompanied by the release of a considerable amount of energy per unit volume (latent heat) which affects the local temperature as shown in non-isothermal tensile tests presented in Rusinek and Klepaczko (2009). Under those circumstances, the thermomechanical behavior of a material sample needs to be obtained as the solution of a coupled problem involving the balance of both linear momentum and energy. The coupling occurs in both directions since the thermal response is affected by the internal heat stemming from mechanical processes and, conversely, the mechanical response depends on the thermal behavior.

The present contribution focusses on the formulation and the numerical analysis of a fully-coupled thermomechanical model for multiphase steels. The model, presented in Section 2, is based on the work originally proposed in Turteltaub and Suiker (2005, 2006b), which was expanded in Tjahjanto et al. (2008a) to account for crystalline plasticity in the austenitic phase and the surrounding matrix and further extended in Tjahjanto et al. (2008b) to incorporate thermoelastic coupling effects. From a theoretical point of view, one important refinement in the present formulation relates to the decomposition of the entropy density, where the entropic counterpart of the thermal strain is derived from thermodynamic requirements. Although the resulting formulation is similar to that presented in Tjahjanto et al. (2008b), the new entropy decomposition formally provides thermodynamic consistency. This model has been implemented in a fully-implicit numerical framework in order to solve simultaneously the equations of linear momentum and energy. To illustrate the predictions of the model, Section 3.1 includes simulations of a single crystal of austenite undergoing plastic deformation and/or phase transformation. These simulations are carried out at different initial temperatures and compared to the predictions of isothermal simulations. Subsequently, in Section 3.2, the basic behavior of a grain of austenite embedded in a ferritic matrix is simulated to study the influence of the surrounding matrix on the thermomechanical behavior of austenite.

## 2. Thermomechanical model for multiphase steels

In this section, a constitutive model is developed to describe the thermo-elasto-plastic response of single-crystal FCC austenite that may transform into one or more martensitic BCT phases (referred to as transformation systems). The model is based on the work presented in Turteltaub and Suiker (2005, 2006b) and Tjahjanto et al. (2008a,b) and incorporates new features to satisfy consistency from a thermodynamical point of view. To this end, the deformation gradient and the entropy are decomposed analogously to each other with special attention given to the terms that account for the coupling between the entropy and the deformation.

### 2.1. Kinematics

To describe the deformation of a single-crystal grain of austenite that may partially or totally transform into martensite, the total deformation gradient $\mathbf{F}$ is multiplicatively decomposed as

$$
\mathbf{F}=\mathbf{F}_{\mathrm{e}} \mathbf{F}_{\mathrm{th}} \mathbf{F}_{\mathrm{p}} \mathbf{F}_{\mathrm{tr}}, \tag{1}
$$

where $\mathbf{F}_{\mathrm{e}}, \mathbf{F}_{\mathrm{th}}, \mathbf{F}_{\mathrm{p}}$ and $\mathbf{F}_{\mathrm{tr}}$ are the elastic, thermal, plastic and transformation contributions to the total deformation gradient, respectively. This decomposition defines several (local) intermediate configurations $\mathcal{B}_{i}$ ($i=1,2,3$) between the reference configuration $\mathcal{B}_{0}$ (chosen to coincide with a stress-free state of the underlying material) and the current configuration $\mathcal{B}$ as shown schematically below

![](./images/813309090720645120_1.jpg)

The transformation deformation gradient includes lower length-scale kinematical information of the product martensitic phase(s) through crystallographic information derived from the theory of martensitic transformations (Turteltaub and Suiker, 2006b). A material point $\mathbf{x}$ in the reference configuration $\mathcal{B}_{0}$ is interpreted as representing a small neighborhood containing a mixture of austenite and one or more martensitic transformation systems. The mixture is quantified using the volume fractions $\xi^{(\alpha)}$ of the martensitic transformation system $\alpha$ (measured per unit referential volume). The total possible number of transformation systems for an FCC to BCT transformations is $M=24$. Each transformation system is characterized by a pair of vectors, $\mathbf{b}^{(\alpha)}$ and $\mathbf{d}^{(\alpha)}$ that represent, respectively, the shape strain vector and the normal to the habit plane (interface between a martensitic transformation system $\alpha$ and austenite). The (unconstrained) transformation deformation gradient associated with an individual martensitic transformation system $\alpha$ is $\mathbf{F}^{(\alpha)}=\mathbf{b}^{(\alpha)} \otimes \mathbf{d}^{(\alpha)}$ and the corresponding change in volume due to the transformation is,

for any system $\alpha$, given by $J_{\mathrm{tr}}^{(\alpha)}=\operatorname{det} \mathbf{F}^{(\alpha)}=1+\delta_{\mathrm{T}}$ with (Turteltaub and Suiker, 2006b)

$$
\delta_{\mathrm{T}}:=\mathbf{b}^{(\alpha)} \cdot \mathbf{d}^{(\alpha)}. \tag{2}
$$

The time rate of change of the effective transformation gradient of a mixture, $\dot{\mathbf{F}}_{\mathrm{tr}}$, is given by the volume average (in the reference configuration) of the rates of the transformation deformation gradients of all active martensitic transformation systems, which can be expressed as (see Tjahjanto et al. (2008a) and Turteltaub and Suiker (2005, 2006b))

$$
\dot{\mathbf{F}}_{\mathrm{tr}}=\sum_{\alpha=1}^{M} \dot{\xi}^{(\alpha)} \mathbf{b}^{(\alpha)} \otimes \mathbf{d}^{(\alpha)}, \tag{3}
$$

The evolution of the plastic deformation is described by the effective plastic velocity gradient $\mathbf{L}_{\mathrm{p}}$ that is related to the effective plastic deformation gradient $\mathbf{F}_{\mathrm{p}}$ through

$$
\mathbf{L}_{\mathrm{p}}=\dot{\mathbf{F}}_{\mathrm{p}} \mathbf{F}_{\mathrm{p}}^{-1}. \tag{4}
$$

The effective plastic velocity gradient is expressed as a volume average, measured in the second intermediate configuration $\mathcal{B}_{2}$, of the plastic velocity gradients of the austenitic phase, $\mathbf{L}_{\mathrm{p}, \mathrm{A}}$, and the martensitic phases, $\mathbf{L}_{\mathrm{p}}^{(\alpha)}$, see Tjahjanto et al. (2008a). In the present model it is assumed that the high-carbon martensite does not deform plastically (i.e., $\mathbf{L}_{\mathrm{p}}^{(\alpha)}=\mathbf{0}$), in accordance to experimental observations, see Jacques et al. (2006). Consequently, the effective plastic velocity gradient can be related to the plastic gradient of the austenitic phase in the second intermediate configuration as (Tjahjanto et al., 2008a)

$$
\mathbf{L}_{\mathrm{p}}=\tilde{\xi}_{\mathrm{A}} \mathbf{L}_{\mathrm{p}, \mathrm{A}}=\frac{\xi_{\mathrm{A}}}{J_{\mathrm{tr}} J_{\mathrm{p}}} \mathbf{L}_{\mathrm{p}, \mathrm{A}}=\frac{\xi_{\mathrm{A}}}{J_{\mathrm{tr}}} \mathbf{L}_{\mathrm{p}, \mathrm{A}}, \tag{5}
$$

where $\xi_{\mathrm{A}}$ and $\tilde{\xi}_{\mathrm{A}}$ represent the austenitic volume fraction in the reference $(\mathcal{B}_{0})$ and second intermediate $(\mathcal{B}_{2})$ configurations, respectively, $J_{\text {tr }}$ represents the determinant of the effective transformation deformation gradient, and $J_{\mathrm{p}}$ is the determinant of the effective plastic deformation gradient. The austenitic volume fraction in the reference configuration is given by $\xi_{\mathrm{A}}=1-\sum_{\alpha=1}^{M} \xi^{(\alpha)}$. Observe that the last relation in (5) is obtained assuming that the plastic deformation is isochoric, i.e., $J_{\mathrm{p}}=1$. Consistent with a crystal plasticity description of slip along the slip systems $i=1, \ldots, N=24$ of FCC austenite, the effective plastic velocity gradient is expressed as (Tjahjanto et al., 2008a)

$$
\mathbf{L}_{\mathrm{p}}=\sum_{i=1}^{N} \dot{\gamma}^{(i)} \mathbf{m}_{\mathrm{A}}^{(i)} \otimes \mathbf{n}_{\mathrm{A}}^{(i)}, \tag{6}
$$

where $\mathbf{m}_{\mathrm{A}}^{(i)}$ and $\mathbf{n}_{\mathrm{A}}^{(i)}$ are the unit vectors parallel to the slip direction and normal to the slip plane for the austenitic slip system $i$, respectively, and $\dot{\gamma}^{(i)}$ represents the effective plastic slip rate on slip system $i$, given by Tjahjanto et al. (2008a)

$$
\dot{\gamma}^{(i)}=\frac{\xi_{\mathrm{A}}}{J_{\mathrm{tr}}} \dot{\gamma}_{\mathrm{A}}^{(i)}, \tag{7}
$$

with $\dot{\gamma}_{\mathrm{A}}^{(i)}$ the rate of slip along the austenitic slip system $i$ (measured within the austenitic region).

The effective thermal deformation gradient $\mathbf{F}_{\text {th }}$ is expressed as the volume average of the thermal deformation gradients (in the second intermediate configuration) of the austenitic phase, $\mathbf{F}_{\mathrm{th}, \mathrm{A}}$, and martensitic phases, $\mathbf{F}_{\mathrm{th}}^{(\alpha)}$, i.e.,

$$
\mathbf{F}_{\mathrm{th}}=\frac{1}{J_{\mathrm{tr}}}\left(\xi_{\mathrm{A}} \mathbf{F}_{\mathrm{th}, \mathrm{A}}+\left(1+\delta_{\mathrm{T}}\right) \sum_{\alpha=1}^{M} \xi^{(\alpha)} \mathbf{F}_{\mathrm{th}}^{(\alpha)}\right), \tag{8}
$$

where, as before, the plastic deformation has been taken as isochoric. The dependency of the thermal deformation gradient on thermal variables will be discussed below after introducing a decomposition for the entropy.

### 2.2. Entropy

In an entropy-based thermodynamical framework, the entropy plays for the thermal fields an analogous role as the deformation gradient does for the mechanical fields (Callen, 1985). In order to develop a thermodynamically-consistent formulation, the following decomposition for the total entropy density per unit mass $\eta$ is used:

$$
\eta=\eta_{\mathrm{e}}+\eta_{\mathrm{m}}+\eta_{\mathrm{p}}+\eta_{\mathrm{tr}}, \tag{9}
$$

where $\eta_{\mathrm{e}}$ is referred to as the thermal part of the reversible entropy density (analogous to the elastic deformation gradient), $\eta_{\mathrm{m}}$ is the reversible entropy density that accounts for the coupling between the mechanical and thermal fields (analogous to the thermal deformation gradient) and $\eta_{\mathrm{p}}$ and $\eta_{\mathrm{tr}}$ are the entropy densities related to plastic and transformation processes, respectively (analogous to the plastic and transformation deformation gradients).

The rate of change of the transformational entropy density $\eta_{\mathrm{tr}}$ is expressed as (see Tjahjanto et al. (2008a) and Turteltaub and Suiker (2006b))

$$
\dot{\eta}_{\mathrm{tr}}=\sum_{\alpha=1}^{M} \dot{\xi}^{(\alpha)} \frac{\lambda_{\mathrm{T}}^{(\alpha)}}{\theta_{\mathrm{T}}}, \tag{10}
$$

where $\lambda_{\mathrm{T}}^{(\alpha)}$ is the latent heat at the transformation temperature $\theta_{\mathrm{T}}$, which is the heat (per unit mass) required to transform austenite into a specific martensitic transformation system $\alpha$ during an isothermal process at $\theta=\theta_{\mathrm{T}}$. Similarly, the rate of change of the plastic entropy density $\eta_{\mathrm{p}}$ is formally written as (see Tjahjanto et al. (2008a))

$$
\dot{\eta}_{\mathrm{p}}=\xi_{\mathrm{A}} \sum_{i=1}^{N} \dot{\gamma}_{\mathrm{A}}^{(i)} \phi_{\mathrm{A}}^{(i)}=J_{\mathrm{tr}} \sum_{i=1}^{N} \dot{\gamma}^{(i)} \phi_{\mathrm{A}}^{(i)}, \tag{11}
$$

where $\phi_{\mathrm{A}}^{(i)}$ measures the change in entropy per unit slip along the slip system $i$. The form of the term $\eta_{\mathrm{m}}$ will be discussed in more detail in the context of thermodynamical consistency.

### 2.3. State and internal variables

State and internal variables need to be chosen to characterize the internal energy density of the material. From the decomposition of the deformation gradient and the entropy, convenient state variables are the elastic deformation gradient $\mathbf{F}_{\mathrm{e}}$ and the thermal part of the reversible entropy $\eta_{\mathrm{e}}$. In addition, the volume fractions of the martensitic transformation systems $\boldsymbol{\xi}=\left(\xi^{(1)}, \xi^{(2)}, \ldots, \xi^{(M)}\right)$ and the

amounts of plastic slip $\boldsymbol{\gamma}=(\gamma^{(1)},\gamma^{(2)},\dots,\gamma^{(N)})$ are used as variables that characterize internal structural changes in the material due to phase transformations and plastic deformations. Whenever required for partial differentiation, functions that depend on some or all the variables $\mathbf{F}_e$, $\eta_e$, $\boldsymbol{\xi}$ and $\boldsymbol{\gamma}$ will be denoted in the sequel with a superimposed tilde.

For subsequent use, assumptions are made regarding the dependency of the coupling terms $\mathbf{F}_{\text{th}}$ and $\eta_{\text{m}}$ that appear in the decompositions (1) and (9) of the deformation gradient and the entropy, respectively. The classical model for the thermal deformation gradient assumes that $\mathbf{F}_{\text{th}}$ depends on the temperature $\theta$. However, since the temperature is not chosen as a primary variable, it is instead assumed that the thermal deformation gradient depends on the (purely thermal) reversible entropy $\eta_e$. Furthermore, in view of (8), it may be observed that the thermal deformation gradient also depends on $\boldsymbol{\xi}$; consequently it is assumed that
$$
\mathbf{F}_{\text{th}}=\tilde{\mathbf{F}}_{\text{th}}(\eta_e,\boldsymbol{\xi}).\tag{12}
$$

At a later stage, a classical model of the thermal deformation gradient as a function of the temperature will be introduced with a suitable change of variables.

As will be shown in subsequent sections, the reversible entropy associated with the thermomechanical coupling $\eta_{\text{m}}$ cannot be independently specified from the thermal deformation gradient (12); however it is possible to formally express $\eta_{\text{m}}$ as follows:
$$
\eta_{\text{m}}=\tilde{\eta}_{\text{m}}(\mathbf{F}_e,\eta_e,\boldsymbol{\xi}).\tag{13}
$$

Observe that the decomposition of the deformation gradient and the entropy is done in terms of two types of variables, namely (i) quantities related to reversible processes $(\mathbf{F}_e$, $\mathbf{F}_{\text{th}}$, $\eta_e$, $\eta_{\text{m}})$ and (ii) quantities representing irreversible processes $(\mathbf{F}_p$, $\mathbf{F}_{\text{tr}}$, $\eta_p$, $\eta_{\text{tr}})$. The existence of relations of the types (12) and (13) is consistent with the notion of reversibility.

### 2.4. Thermodynamical relations
Useful thermodynamical relations can be established as a result of the procedure established by Coleman and Noll (Coleman and Noll, 1963). To this end, consider the dissipation rate $\mathcal{D}$ (per unit volume) at a material point given by
$$
\mathcal{D}:=-\rho_0\dot{\epsilon}+\mathbf{P}\cdot\dot{\mathbf{F}}+\rho_0\theta\dot{\eta}-\nabla\theta\cdot\boldsymbol{\Phi},\tag{14}
$$
where $\rho_0$ is the referential mass density, $\dot{\epsilon}$ is the rate of change of the internal energy density $\epsilon$ (per unit mass), $\mathbf{P}$ is the first Piola-Kirchhoff stress, $\dot{\mathbf{F}}$ is the rate of change of the deformation gradient, $\theta$ is the temperature, $\dot{\eta}$ is the rate of change of the entropy, $\nabla\theta$ is the (referential) temperature gradient and $\boldsymbol{\Phi}$ is the entropy flux, all written for a material point in the reference configuration.

Using the kinematic relations (3), (6), (4) and (12) and applying the chain rule, the internal mechanical power $\mathbf{P}\cdot\dot{\mathbf{F}}$ can be expressed as
$$
\begin{aligned}
\mathbf{P}\cdot\dot{\mathbf{F}}=&\mathbf{P}\mathbf{F}_{\text{tr}}^{\mathrm{T}}\mathbf{F}_p^{\mathrm{T}}\mathbf{F}_{\text{th}}^{\mathrm{T}}\cdot\dot{\mathbf{F}}_e+\mathbf{F}_e^{\mathrm{T}}\mathbf{P}\mathbf{F}_{\text{tr}}^{\mathrm{T}}\mathbf{F}_p^{\mathrm{T}}\cdot\frac{\partial\tilde{\mathbf{F}}_{\text{th}}}{\partial\eta_e}\dot{\eta}_e\\
&+\sum_{\alpha=1}^{M}\left(\tau_{\text{tr}}^{(\alpha)}+\mathbf{F}_e^{\mathrm{T}}\mathbf{P}\mathbf{F}_{\text{tr}}^{\mathrm{T}}\mathbf{F}_p^{\mathrm{T}}\cdot\frac{\partial\tilde{\mathbf{F}}_{\text{th}}}{\partial\boldsymbol{\xi}^{(\alpha)}}\right)\dot{\boldsymbol{\xi}}^{(\alpha)}+\sum_{i=1}^{N}\tau_p^{(i)}\dot{\gamma}^{(i)},\quad(15)
\end{aligned}
$$
with $\tau_{\text{tr}}^{(\alpha)}$ and $\tau_p^{(i)}$ denoting the resolved stresses on the transformation system $\alpha$ and on the plastic slip system $i$, respectively. The resolved stress for transformation has the form
$$
\tau_{\text{tr}}^{(\alpha)}=\mathbf{F}_p^{\mathrm{T}}\mathbf{F}_{\text{th}}^{\mathrm{T}}\mathbf{F}_e^{\mathrm{T}}\mathbf{P}\cdot\left(\mathbf{b}^{(\alpha)}\otimes\mathbf{d}^{(\alpha)}\right)\tag{16}
$$
and the resolved stress for plastic slip is given by
$$
\tau_p^{(i)}=\mathbf{F}_{\text{th}}^{\mathrm{T}}\mathbf{F}_e^{\mathrm{T}}\mathbf{P}\mathbf{F}_{\text{tr}}^{\mathrm{T}}\mathbf{F}_p^{\mathrm{T}}\cdot\left(\mathbf{m}_A^{(i)}\otimes\mathbf{n}_A^{(i)}\right).\tag{17}
$$

The internal thermal power $\rho_0\theta\dot{\eta}$ in (14) can be expanded in a similar way using (9)-(11) and the dependency condition for $\eta_{\text{m}}$ in (13), i.e.,
$$
\begin{aligned}
\rho_0\theta\dot{\eta}=&\rho_0\theta\frac{\partial\tilde{\eta}_{\text{m}}}{\partial\mathbf{F}_e}\cdot\dot{\mathbf{F}}_e+\rho_0\theta\left(1+\frac{\partial\tilde{\eta}_{\text{m}}}{\partial\eta_e}\right)\dot{\eta}_e\\
&+\sum_{\alpha=1}^{M}\left(\zeta_{\text{tr}}^{(\alpha)}+\rho_0\theta\frac{\partial\tilde{\eta}_{\text{m}}}{\partial\boldsymbol{\xi}^{(\alpha)}}\right)\dot{\boldsymbol{\xi}}^{(\alpha)}+\sum_{i=1}^{N}\zeta_p^{(i)}\dot{\gamma}^{(i)},\tag{18}
\end{aligned}
$$
where $\zeta_{\text{tr}}^{(\alpha)}$ and $\zeta_p^{(i)}$ are the thermal analogues of the resolved stresses $\tau_{\text{tr}}^{(\alpha)}$ and $\tau_p^{(i)}$, respectively, given by
$$
\zeta_{\text{tr}}^{(\alpha)}=\rho_0\theta\frac{\lambda_{\text{T}}^{(\alpha)}}{\theta_{\text{T}}},\quad\zeta_p^{(i)}=\rho_0J_{\text{tr}}\theta\phi_A^{(i)}.\tag{19}
$$

The rate of change of the internal energy can be expressed in terms of rates of state and internal variables and, more generally, might also depend on fluxes. The model that will be used here to take into account the stored energy associated with plastic deformations is relatively simple. With this in mind, for the purposes of the present model, it is sufficient to assume that the internal energy does not arbitrarily depend on all components of $\boldsymbol{\gamma}$ but only through a specific combination of them. To this end, a strain-like variable $\beta$ is defined (in rate form) as a weighted sum of the rates of plastic slips $\dot{\gamma}^{(i)}$ (Tjahjanto et al., 2008a), i.e.,
$$
\dot{\beta}=\sum_{i=1}^{N}w^{(i)}\dot{\gamma}^{(i)},\tag{20}
$$
where the form of the weighting functions $w^{(i)}$ will be derived at the end of Section 2.6 in terms of a hardening model. The scalar quantity $\beta$ plays the role of an equivalent plastic (micro) strain and is henceforth treated as an internal variable (see Tjahjanto et al. (2008a) for details). Correspondingly, it is assumed that the internal energy $\epsilon$ is given by a function $\tilde{\epsilon}$ that depends on the state and internal variables $\mathbf{F}_e$, $\eta_e$, $\boldsymbol{\xi}$ and $\beta$ and, a priori, may also depend on the fluxes $\dot{\boldsymbol{\xi}}$, $\dot{\beta}$, and $\boldsymbol{\Phi}$, i.e.,
$$
\epsilon=\tilde{\epsilon}\left(\mathbf{F}_e,\eta_e,\boldsymbol{\xi},\beta;\dot{\boldsymbol{\xi}},\dot{\beta},\boldsymbol{\Phi}\right).\tag{21}
$$

Combining (15), (18), (20) and (21) with (14) results in the following expression for the dissipation:

$$
\begin{aligned}
\mathcal{D} & =\left(\mathbf{P F}_{\mathrm{tr}}^{\mathrm{T}} \mathbf{F}_{\mathrm{p}}^{\mathrm{T}} \mathbf{F}_{\mathrm{th}}^{\mathrm{T}}+\rho_{0} \theta \frac{\partial \tilde{\eta}_{\mathrm{m}}}{\partial \mathbf{F}_{\mathrm{e}}}-\rho_{0} \frac{\partial \tilde{\epsilon}}{\partial \mathbf{F}_{\mathrm{e}}}\right) \cdot \dot{\mathbf{F}}_{\mathrm{e}} \\
& +\rho_{0}\left(\theta+\theta \frac{\partial \tilde{\eta}_{\mathrm{m}}}{\partial \eta_{\mathrm{e}}}+\frac{1}{\rho_{0}} \mathbf{F}_{\mathrm{e}}^{\mathrm{T}} \mathbf{P} \mathbf{F}_{\mathrm{tr}}^{\mathrm{T}} \mathbf{F}_{\mathrm{p}}^{\mathrm{T}} \cdot \frac{\partial \tilde{\mathbf{F}}_{\mathrm{th}}}{\partial \eta_{\mathrm{e}}}-\frac{\partial \tilde{\epsilon}}{\partial \eta_{\mathrm{e}}}\right) \dot{\eta}_{\mathrm{e}} \\
& +\sum_{\alpha=1}^{M}\left(\tau_{\mathrm{tr}}^{(\alpha)}+\zeta_{\mathrm{tr}}^{(\alpha)}+\mathbf{F}_{\mathrm{e}}^{\mathrm{T}} \mathbf{P} \mathbf{F}_{\mathrm{tr}}^{\mathrm{T}} \mathbf{F}_{\mathrm{p}}^{\mathrm{T}} \cdot \frac{\partial \tilde{\mathbf{F}}_{\mathrm{th}}}{\partial \dot{\zeta}^{(\alpha)}}+\rho_{0} \theta \frac{\partial \tilde{\eta}_{\mathrm{m}}}{\partial \dot{\zeta}^{(\alpha)}}-\rho_{0} \frac{\partial \tilde{\epsilon}}{\partial \dot{\zeta}^{(\alpha)}}\right) \dot{\zeta}^{(\alpha)} \\
& -\sum_{\alpha=1}^{M} \rho_{0} \frac{\partial \tilde{\epsilon}}{\partial \ddot{\zeta}^{(\alpha)}} \ddot{\zeta}^{(\alpha)}+\sum_{i=1}^{N}\left(\tau_{\mathrm{p}}^{(i)}+\zeta_{\mathrm{p}}^{(i)}-\rho_{0} \frac{\partial \tilde{\epsilon}}{\partial \beta} w^{(i)}\right) \dot{\gamma}^{(i)} \\
& -\rho_{0} \frac{\partial \tilde{\epsilon}}{\partial \dot{\beta}} \ddot{\beta}-\nabla \theta \cdot \boldsymbol{\Phi}-\rho_{0} \frac{\partial \tilde{\epsilon}}{\partial \boldsymbol{\Phi}} \cdot \dot{\boldsymbol{\Phi}}.
\end{aligned}
$$

The second law of thermodynamics states that for every thermomechanical process, the local entropy rate must be non-negative, $\Gamma \geqslant 0$, which for this case is equivalent to $\mathcal{D}=\Gamma \theta \geqslant 0$, since the temperature is always positive. Furthermore, the terms in (22) that are multiplied by the rates $\dot{\mathbf{F}}_{\mathrm{e}}, \dot{\eta}_{\mathrm{e}}, \ddot{\beta}, \ddot{\zeta}$ and $\dot{\boldsymbol{\Phi}}$ must vanish, since otherwise a process can be specified for which the dissipation is negative (see Coleman and Noll (1963)). Correspondingly, it can be concluded that
$$
\begin{aligned}
& \rho_{0} \frac{\partial \tilde{\epsilon}}{\partial \mathbf{F}_{\mathrm{e}}}=\mathbf{P F}_{\mathrm{tr}}^{\mathrm{T}} \mathbf{F}_{\mathrm{p}}^{\mathrm{T}} \mathbf{F}_{\mathrm{th}}^{\mathrm{T}}+\rho_{0} \theta \frac{\partial \tilde{\eta}_{\mathrm{m}}}{\partial \mathbf{F}_{\mathrm{e}}}, \\
& \frac{\partial \tilde{\epsilon}}{\partial \eta_{\mathrm{e}}}=\theta+\theta \frac{\partial \tilde{\eta}_{\mathrm{m}}}{\partial \eta_{\mathrm{e}}}+\frac{1}{\rho_{0}} \mathbf{F}_{\mathrm{e}}^{\mathrm{T}} \mathbf{P} \mathbf{F}_{\mathrm{tr}}^{\mathrm{T}} \mathbf{F}_{\mathrm{p}}^{\mathrm{T}} \cdot \frac{\partial \tilde{\mathbf{F}}_{\mathrm{th}}}{\partial \eta_{\mathrm{e}}}, \\
& \frac{\partial \tilde{\epsilon}}{\partial \dot{\beta}}=\mathbf{0}, \quad \frac{\partial \tilde{\epsilon}}{\partial \ddot{\zeta}}=\mathbf{0}, \quad \frac{\partial \tilde{\epsilon}}{\partial \boldsymbol{\Phi}}=\mathbf{0}.
\end{aligned}
$$

As a result of the last three relations in (23), the internal energy cannot depend on the fluxes, which reduces (21) to
$$
\epsilon=\tilde{\epsilon}\left(\mathbf{F}_{\mathrm{e}}, \eta_{\mathrm{e}}, \xi, \beta\right).
$$

Enforcing (23) in (22), the dissipation can be written as $\mathcal{D}=\mathcal{D}_{\mathrm{tr}}+\mathcal{D}_{\mathrm{p}}+\mathcal{D}_{\mathrm{q}}$, where $\mathcal{D}_{\mathrm{tr}}, \mathcal{D}_{\mathrm{p}}$ and $\mathcal{D}_{\mathrm{q}}$ are the dissipations due to phase transformation, plastic deformation and heat conduction, respectively, defined as
$$
\mathcal{D}_{\mathrm{tr}}:=\sum_{\alpha=1}^{M} f^{(\alpha)} \dot{\zeta}^{(\alpha)}, \quad \mathcal{D}_{\mathrm{p}}:=\sum_{i=1}^{N} g^{(i)} \dot{\gamma}^{(i)}, \quad \mathcal{D}_{\mathrm{q}}:=-\nabla \theta \cdot \boldsymbol{\Phi},
$$
with $f^{(\alpha)}$ and $g^{(i)}$ the driving forces for transformation and plasticity, respectively, given by
$$
\begin{aligned}
f^{(\alpha)} & :=\tau_{\mathrm{tr}}^{(\alpha)}+\zeta_{\mathrm{tr}}^{(\alpha)}+\mathbf{F}_{\mathrm{e}}^{\mathrm{T}} \mathbf{P} \mathbf{F}_{\mathrm{tr}}^{\mathrm{T}} \mathbf{F}_{\mathrm{p}}^{\mathrm{T}} \cdot \frac{\partial \tilde{\mathbf{F}}_{\mathrm{th}}}{\partial \zeta^{(\alpha)}} \\
& +\rho_{0} \theta \frac{\partial \tilde{\eta}_{\mathrm{m}}}{\partial \zeta^{(\alpha)}}-\rho_{0} \frac{\partial \tilde{\epsilon}}{\partial \zeta^{(\alpha)}}, \\
g^{(i)} & :=\tau_{\mathrm{p}}^{(i)}+\zeta_{\mathrm{p}}^{(i)}-\rho_{0} \frac{\partial \tilde{\epsilon}}{\partial \beta} w^{(i)}.
\end{aligned}
$$

For the kinetic relations of the present model, it will be assumed that a strong form of the dissipation inequality applies, namely that the dissipation associated with individual processes is non-negative, i.e., it will be required that
$$
\mathcal{D}_{\mathrm{tr}} \geqslant 0, \quad \mathcal{D}_{\mathrm{p}} \geqslant 0, \quad \mathcal{D}_{\mathrm{q}} \geqslant 0.
$$

Observe that the Coleman-Noll procedure yields two types of results, namely (i) relations for the partial derivatives of the (stored) internal energy (see $(23)_{1,2}$ ) and (ii) expressions for the transformational and plastic driving forces (see (26)). After introducing specific constitutive models between the dependent variables $\mathbf{P}, \theta, \mathbf{F}_{\text {th }}$ and $\eta_{\mathrm{m}}$ and the state variables $\mathbf{F}_{\mathrm{e}}$ and $\eta_{\mathrm{e}}$, the first set of thermodynamical relations from the Coleman-Noll procedure can be integrated to obtain an expression for the internal energy. Once the expression for $\tilde{\epsilon}$ has been established, the second set of thermodynamical relations (26) can be applied to further develop specific forms for the driving forces. Finally, kinetic relations that relate the evolution of the internal variables to the driving forces can be proposed such that the dissipation inequality is satisfied for all possible processes. These steps are carried out in the subsequent sections.

### 2.5. Models for the internal energy, thermal deformation gradient and reversible entropy

To obtain an expression for the internal energy density $\epsilon$, it is convenient to work with a different set of state variables. In particular, since the constitutive relation between the stress and the (elastic) deformation must be frame indifferent, the stress tensor cannot depend on (elastic) rotations. This can be guaranteed using a strain measure where the rotation has been factored out, such as the elastic Green-Lagrange strain defined as
$$
\mathbf{E}_{\mathrm{e}}=\tilde{\mathbf{E}}_{\mathrm{e}}\left(\mathbf{F}_{\mathrm{e}}\right)=\frac{1}{2}\left(\mathbf{F}_{\mathrm{e}}^{\mathrm{T}} \mathbf{F}_{\mathrm{e}}-\mathbf{I}\right).
$$

Furthermore, the classical models for the thermal deformation gradient and the thermal energy are expressed in terms of the temperature $\theta$ and not the (purely thermal) reversible entropy $\eta_{\mathrm{e}}$. It is assumed that there is a one-to-one correspondence between $\theta$ and $\eta_{\mathrm{e}}$ of the form $\theta=\tilde{\theta}\left(\eta_{\mathrm{e}}, \xi\right)$, which can be inverted as $\eta_{\mathrm{e}}=\hat{\eta}_{\mathrm{e}}(\theta, \xi)$. Accordingly, a new set of state and internal variables, namely $\left(\mathbf{E}_{\mathrm{e}}, \theta, \xi, \beta\right)$, is used in the foregoing analysis. Henceforth, a superimposed "hat" on a function indicates that it depends on some or all of the variables $\mathbf{E}_{\mathrm{e}}, \theta, \xi$ and $\beta$. It is worth pointing out that in order to use the temperature as a state variable, the most natural formulation is in terms of the Helmholtz energy $\psi$, which, assuming a one-to-one correspondence between conjugate variables, can be obtained from a Legendre transformation, namely $\dot{\psi}\left(\mathbf{E}_{\mathrm{e}}, \theta, \xi, \beta\right)=\tilde{\epsilon}\left(\mathbf{E}_{\mathrm{e}}, \hat{\eta}_{\mathrm{e}}\right.$ $(\theta, \xi), \xi, \beta)-\theta \hat{\eta}_{\mathrm{e}}(\theta, \xi)$. However, in anticipation of a numerical implementation that is based on the internal energy, it is more convenient to perform a direct change of variables instead of a Legendre transform. This choice requires the use of the chain rule, but otherwise provides an equivalent formulation as the Legendre transform.

Based on the aforementioned assumptions, the change of variables can be achieved employing the following relations for a (scalar, vector or tensor-valued) function $\mathbf{f}$ :
$$
\begin{aligned}
& \frac{\partial \tilde{\mathbf{f}}}{\partial \mathbf{F}_{\mathrm{e}}}=\mathbf{F}_{\mathrm{e}} \frac{\partial \hat{\mathbf{f}}}{\partial \mathbf{E}_{\mathrm{e}}}, \quad \mathbf{P}=J_{\mathrm{tr}} J_{\mathrm{th}} \mathbf{F}_{\mathrm{e}} \mathbf{S F}_{\mathrm{th}}^{-\mathrm{T}} \mathbf{F}_{\mathrm{p}}^{-\mathrm{T}} \mathbf{F}_{\mathrm{tr}}^{-\mathrm{T}}, \\
& \frac{\partial \tilde{\mathbf{f}}}{\partial \eta_{\mathrm{e}}}=\frac{\partial \tilde{\theta}}{\partial \eta_{\mathrm{e}}} \frac{\partial \hat{\mathbf{f}}}{\partial \theta}, \quad \frac{\partial \hat{\eta}_{\mathrm{e}}}{\partial \theta}=\left(\frac{\partial \tilde{\theta}}{\partial \eta_{\mathrm{e}}}\right)^{-1}, \\
& \frac{\partial \tilde{\mathbf{f}}}{\partial \zeta^{(\alpha)}}=\frac{\partial \hat{\mathbf{f}}}{\partial \zeta^{(\alpha)}}+\frac{\partial \tilde{\theta}}{\partial \zeta^{(\alpha)}} \frac{\partial \hat{\mathbf{f}}}{\partial \theta}, \quad \frac{\partial \tilde{\mathbf{f}}}{\partial \beta}=\frac{\partial \hat{\mathbf{f}}}{\partial \beta},
\end{aligned}
$$


where $\mathbf{S}$ corresponds to the second Piola-Kirchhoff stress tensor in the third intermediate configuration $\mathcal{B}_{3}$. Employing the relations (29), Eq. $(23)_{1,2}$ can be written as

$$
\begin{aligned}
& \rho_{0} \frac{\partial \hat{\epsilon}}{\partial \mathbf{E}_{\mathrm{e}}}=J_{\mathrm{tr}} J_{\mathrm{th}} \mathbf{S}+\rho_{0} \theta \frac{\partial \hat{\eta}_{\mathrm{m}}}{\partial \mathbf{E}_{\mathrm{e}}}, \\
& \rho_{0} \frac{\partial \hat{\epsilon}}{\partial \theta}=\rho_{0} \theta \frac{\partial}{\partial \theta}\left(\hat{\eta}_{\mathrm{e}}+\hat{\eta}_{\mathrm{m}}\right)+J_{\mathrm{tr}} J_{\mathrm{th}} \mathbf{F}_{\mathrm{e}}^{\mathrm{T}} \mathbf{F}_{\mathrm{e}} \mathbf{S} \cdot \frac{\partial \hat{\mathbf{F}}_{\mathrm{th}}}{\partial \theta} \mathbf{F}_{\mathrm{th}}^{-1}.
\end{aligned}
\tag{30}
$$

It is assumed that the stress tensor $\mathbf{S}$ and its conjugate strain tensor $\mathbf{E}_{\mathrm{e}}$ are related through the constitutive relation

$$
\mathbf{S}=\hat{\mathbf{S}}\left(\mathbf{E}_{\mathrm{e}}, \xi\right)=\mathbb{C}(\xi) \mathbf{E}_{\mathrm{e}},
\tag{31}
$$

where $\mathbb{C}=\mathbb{C}(\xi)$ is an effective fourth order elasticity tensor for the mixture of austenite and martensite that, in the present model, is estimated as a volume average in the third intermediate configuration, i.e.,

$$
\mathbb{C}(\xi)=\frac{1}{J_{\mathrm{tr}} J_{\mathrm{th}}}\left(J_{\mathrm{th}, \mathrm{A}} \xi_{\mathrm{A}} \mathbb{C}_{\mathrm{A}}+\left(1+\delta_{\mathrm{T}}\right) \sum_{\alpha=1}^{M} J_{\mathrm{th}}^{(\alpha)} \xi^{(\alpha)} \mathbb{C}^{(\alpha)}\right),
\tag{32}
$$

where $\mathbb{C}_{\mathrm{A}}$ and $\mathbb{C}^{(\alpha)}$ are the stiffness tensors of austenite and twinned martensite, respectively, and $J_{\mathrm{th}}=\operatorname{det} \mathbf{F}_{\mathrm{th}}, J_{\mathrm{th}, \mathrm{A}}$ $=\operatorname{det} \mathbf{F}_{\mathrm{th}, \mathrm{A}}$ and $J_{\mathrm{th}}^{(\alpha)}=\operatorname{det} \mathbf{F}_{\mathrm{th}}^{(\alpha)}$. Specific forms for $\mathbb{C}_{\mathrm{A}}$ and $\mathbb{C}^{(\alpha)}$ are given in Turteltaub and Suiker (2006b). It is noted that the effective stiffness $\mathbb{C}$ formally depends on the temperature since the thermal deformation gradients $\mathbf{F}_{\mathrm{th}, \mathrm{A}}$ and $\mathbf{F}_{\mathrm{th}}^{(\alpha)}$ depend on $\theta$. However, this dependency is not intrinsically physical because it is only related to the approximation scheme used, namely the volume averaging. In the sequel, it will be assumed that the dependency of $\mathbb{C}$ on $\theta$ is weak in the sense that

$$
\frac{\partial}{\partial \theta}\left(J_{\mathrm{tr}} J_{\mathrm{th}} \mathbb{C}\right) \approx 0.
\tag{33}
$$

Correspondingly, the formal dependency of $\mathbb{C}$ on $\theta$ is not indicated in (32). Integrating $(30)_{1}$ with respect to $\mathbf{E}_{\mathrm{e}}$ yields

$$
\hat{\epsilon}\left(\mathbf{E}_{\mathrm{e}}, \theta, \xi, \beta\right)=\hat{\epsilon}_{\mathrm{m}}\left(\mathbf{E}_{\mathrm{e}}, \xi\right)+\theta \hat{\eta}_{\mathrm{m}}\left(\mathbf{E}_{\mathrm{e}}, \theta, \xi\right)+\hat{\epsilon}_{1}(\theta, \xi, \beta),
\tag{34}
$$

where $\hat{\epsilon}_{1}$ is a function that does not depend on $\mathbf{E}_{\mathrm{e}}$ and $\hat{\epsilon}_{\mathrm{m}}$ is the strain energy given by

$$
\hat{\epsilon}_{\mathrm{m}}\left(\mathbf{E}_{\mathrm{e}}, \xi\right)=\frac{J_{\mathrm{tr}} J_{\mathrm{th}}}{2 \rho_{0}} \mathbb{C}(\xi) \mathbf{E}_{\mathrm{e}} \cdot \mathbf{E}_{\mathrm{e}}.
\tag{35}
$$

Taking the partial derivative of (34) with respect to the temperature (accounting for the assumption (33)), equating the resulting expression with $(30)_{2}$ and rearranging the terms leads to

$$
\hat{\eta}_{\mathrm{m}}=\frac{1}{\rho_{0}} J_{\mathrm{tr}} J_{\mathrm{th}} \mathbf{F}_{\mathrm{e}}^{\mathrm{T}} \mathbf{F}_{\mathrm{e}} \mathbf{S} \cdot \frac{\partial \hat{\mathbf{F}}_{\mathrm{th}}}{\partial \theta} \mathbf{F}_{\mathrm{th}}^{-1}+\left(\theta \frac{\partial \hat{\eta}_{\mathrm{e}}}{\partial \theta}-\frac{\partial \hat{\epsilon}_{1}}{\partial \theta}\right).
\tag{36}
$$

As discussed in Section 2.2, the term $\hat{\eta}_{\mathrm{m}}$ accounts for the entropy associated with an elastic deformation. Consequently, $\hat{\eta}_{\mathrm{m}}$ should vanish in the absence of an elastic deformation, i.e.,

$$
\hat{\eta}_{\mathrm{m}}\left(\mathbf{E}_{\mathrm{e}}=\mathbf{0}, \theta, \xi\right)=0.
\tag{37}
$$

Observe that the relation shown in (37) should hold for arbitrary values of the temperature $\theta$ and the volume fractions $\xi$. By setting $\mathbf{E}_{\mathrm{e}}=\mathbf{0}$ (and hence $\mathbf{S}=\mathbf{0}$) in (36), and in view of (37), it follows that

$$
\theta \frac{\partial \hat{\eta}_{\mathrm{e}}}{\partial \theta}-\frac{\partial \hat{\epsilon}_{1}}{\partial \theta}=0.
\tag{38}
$$

Consistent with the foregoing assumptions, the above relation is valid for arbitrary values of $\theta$ and $\xi$ and does not depend on the elastic deformation. The term $\epsilon_{1}$ can be obtained upon integration of (38), which requires a constitutive relation between $\theta$ and $\eta_{\mathrm{e}}$. The following constitutive relation is then proposed (Turteltaub and Suiker, 2006b):

$$
\eta_{\mathrm{e}}=\hat{\eta}_{\mathrm{e}}(\theta, \xi)=h(\xi) \ln \left(\frac{\theta}{\theta_{\mathrm{T}}}\right)+\eta_{\mathrm{T}},
\tag{39}
$$

where $h=h(\xi)$ stands for the effective specific heat (per unit mass), $\theta_{\mathrm{T}}$ is the transformation temperature at zero elastic deformation and $\eta_{\mathrm{T}}$ denotes the value of $\eta_{\mathrm{e}}$ at the transformation temperature. The above model corresponds to assuming that the specific heat remains constant during a purely thermal process. The effective specific heat $h$ is estimated as a volume average of the specific heat of the austenitic phase, $h_{\mathrm{A}}$, and the specific heats of the martensitic transformation systems, $h^{(\alpha)}$ (see Turteltaub and Suiker (2006b)), i.e.,

$$
h(\xi)=\xi_{\mathrm{A}} h_{\mathrm{A}}+\sum_{\alpha=1}^{M} \xi^{(\alpha)} h^{(\alpha)}.
\tag{40}
$$

Using (39) in (38) and integrating with respect to $\theta$ results in

$$
\hat{\epsilon}_{1}(\theta, \xi, \beta)=\hat{\epsilon}_{\mathrm{th}}(\theta, \xi)+\hat{\epsilon}_{2}(\xi, \beta),
\tag{41}
$$

where $\hat{\epsilon}_{2}$ is a function that does not depend on the temperature and $\hat{\epsilon}_{\mathrm{th}}$ is the thermal internal energy, which corresponds to a classical model, i.e.,

$$
\hat{\epsilon}_{\mathrm{th}}(\theta, \xi)=h(\xi) \theta.
\tag{42}
$$

The function $\hat{\epsilon}_{2}$ is used to introduce two other forms of (lower-scale) energy that play a role at the mesoscale, namely a defect energy $\hat{\epsilon}_{\mathrm{d}}$ that represents the elastic distortion of the lattice due to the presence of dislocations and a surface energy $\hat{\epsilon}_{\mathrm{s}}$ stored in the austenite-twinned martensite interfaces. Correspondingly, the function $\hat{\epsilon}_{2}$ is expressed as

$$
\hat{\epsilon}_{2}(\xi, \beta)=\hat{\epsilon}_{\mathrm{d}}(\xi, \beta)+\hat{\epsilon}_{\mathrm{s}}(\xi)+\hat{\epsilon}^{*}(\xi).
\tag{43}
$$

Adopting the models presented in previous works (Tjahjanto et al., 2008a; Turteltaub and Suiker, 2005, 2006b), the defect energy and the surface energy are formulated as

$$
\begin{aligned}
& \hat{\epsilon}_{\mathrm{d}}(\xi, \beta)=\frac{1}{2 \rho_{0}} J_{\mathrm{tr}} J_{\mathrm{th}} \omega_{\mathrm{A}} \mu(\xi) \beta^{2}, \\
& \hat{\epsilon}_{\mathrm{s}}(\xi)=\frac{\chi}{l_{0} \rho_{0}} \sum_{\alpha=1}^{M} \xi^{(\alpha)}\left(1-\xi^{(\alpha)}\right),
\end{aligned}
\tag{44}
$$

where $\omega_{\mathrm{A}}$ is a scaling factor for the strain energy of an assembly of dislocations, $\beta$ is the strain-like internal variable related to plastic slip through (20), $\chi$ is an interface energy per unit referential area and $l_{0}$ is a length-scale

parameter representing the volume-to-surface ratio of a circular platelet of martensite within a spherical grain of austenite (see Turteltaub and Suiker (2006a,b) for details). The term $\mu = \mu(\xi)$ is an equivalent (isotropic) shear modulus (obtained through averaging the modulus $\mu_{\text{A}}$ of austenite and $\mu^{(\alpha)}$ of martensite, see Tjahjanto et al. (2008a)), i.e.,

$$
\mu(\xi)=\frac{1}{J_{\text{tr}} J_{\text{th}}}\left(J_{\text{th,A}} \xi_{\text{A}} \mu_{\text{A}}+\left(1+\delta_{\text{T}}\right) \sum_{\alpha=1}^{M} J_{\text{th}}^{(\alpha)} \xi^{(\alpha)} \mu^{(\alpha)}\right).
$$

Similar to the approach adopted for the stiffness $\mathbb{C}$, it is assumed that the dependency of $\mu$ on $\theta$ is weak in the sense that $\partial(J_{\text{tr}} J_{\text{th}} \mu) / \partial \theta \approx 0$.

The last term in the decomposition (43), $\hat{\epsilon}^{*}$, is used to satisfy an additional requirement on the energy at the transformation temperature $\theta_{\mathrm{T}}$, namely that the transformation driving force (for all systems) should vanish when the transformation process takes place at the transformation temperature, at zero elastic strain (hence at zero stress), at zero plastic deformation (hence at zero plastic microstrain) and in the absence of a surface energy. The previous requirement can be formally expressed as

$$
\left.f^{(\alpha)}\right|_{\mathbf{E}_{\mathrm{e}}=\mathbf{0}, \theta=\theta_{\mathrm{T}}, \beta=0, \chi_{i}=0}=0. \quad(45)
$$

Upon using (16), $(19)_{1},(29)_{2},(31),(34)-(36),(40),(42)-$ (44) in $(26)_{1}$ (with $\mathbf{E}_{\mathrm{e}}=\mathbf{0}, \theta=\theta_{\mathrm{T}}, \beta=0, \chi=0$ ), the condition (45) results in

$$
\lambda_{\mathrm{T}}^{(\alpha)}-\left(h^{(\alpha)}-h_{\mathrm{A}}\right) \theta_{\mathrm{T}}-\frac{\partial \hat{\epsilon}^{*}}{\partial \xi^{(\alpha)}}=0, \quad(46)
$$

Integration of (46) gives the following expression for $\hat{\epsilon}^{*}$ :

$$
\hat{\epsilon}^{*}(\xi)=\sum_{\alpha=1}^{M} \lambda_{\mathrm{T}}^{(\alpha)} \xi^{(\alpha)}-h(\xi) \theta_{\mathrm{T}}. \quad(47)
$$

It is convenient to combine the term $\hat{\epsilon}^{*}$ with the thermal internal energy $\hat{\epsilon}_{\text {th }}$ given in (42) into a thermal energy $\hat{\epsilon}_{\text {th }}^{*}$ that also accounts for the latent heat, i.e.,

$$
\hat{\epsilon}_{\mathrm{th}}^{*}(\theta, \xi)=h(\xi)\left(\theta-\theta_{\mathrm{T}}\right)+\sum_{\alpha=1}^{M} \lambda_{\mathrm{T}}^{(\alpha)} \xi^{(\alpha)}. \quad(48)
$$

Before closing this section, a classical model for the thermal deformation gradient is considered. In particular, the thermal deformation gradient is assumed to depend linearly on the temperature, i.e., $\mathbf{F}_{\mathrm{th}, \mathrm{A}}=\mathbf{I}+\mathbf{A}_{\mathrm{A}}\left(\theta-\theta_{0}\right)$ and $\mathbf{F}_{\text {th }}^{(\alpha)}=\mathbf{I}+\mathbf{A}^{(\alpha)}\left(\theta-\theta_{0}\right)$, with $\theta_{0}$ being a reference temperature and $\mathbf{A}_{\mathrm{A}}$ and $\mathbf{A}^{(\alpha)}$ the tensors of thermal expansion of the austenitic and martensitic phases, respectively. In view of the relations above, expression (8) becomes

$$
\mathbf{F}_{\mathrm{th}}=\hat{\mathbf{F}}_{\mathrm{th}}(\theta, \xi)=\mathbf{I}+\mathbf{A}(\xi)\left(\theta-\theta_{0}\right), \quad(49)
$$

with $\mathbf{A}$ the effective tensor of thermal expansion given by

$$
\mathbf{A}(\xi)=\frac{1}{J_{\mathrm{tr}}}\left(\xi_{\mathrm{A}} \mathbf{A}_{\mathrm{A}}+\left(1+\delta_{\mathrm{T}}\right) \sum_{\alpha=1}^{M} \xi^{(\alpha)} \mathbf{A}^{(\alpha)}\right). \quad(50)
$$

The specific form of the reversible entropy $\hat{\eta}_{\mathrm{m}}$ associated with the thermomechanical coupling can be obtained by substitution of (32), (35) and (49) in (36) (accounting for (38)), i.e.,

$$
\hat{\eta}_{\mathrm{m}}\left(\mathbf{E}_{\mathrm{e}}, \theta, \xi\right)=\frac{1}{\rho_{0}} J_{\mathrm{tr}} J_{\mathrm{th}} \mathbf{F}_{\mathrm{e}}^{\mathrm{T}} \mathbf{F}_{\mathrm{e}} \mathbf{S F}_{\mathrm{th}}^{-\mathrm{T}} \cdot \mathbf{A}. \quad(51)
$$

In view of (28), (31) and (49), the term $\hat{\eta}_{\mathrm{m}}$ is interpreted as a function of $\mathbf{E}_{\mathrm{e}}, \theta$ and $\xi$. The explicit form of the internal energy, i.e.,

$$
\hat{\epsilon}=\hat{\epsilon}_{\mathrm{m}}+\theta \hat{\eta}_{\mathrm{m}}+\hat{\epsilon}_{\mathrm{th}}^{*}+\hat{\epsilon}_{\mathrm{s}}+\hat{\epsilon}_{\mathrm{d}}, \quad(52)
$$

can be obtained from (35), (44), (48) and (51).

### 2.6. Driving forces and kinetic relations

To complete the thermomechanical formulation, the driving forces for transformation and plasticity and the kinetic relations for the evolution of the internal variables of the model are presented in this section. Explicit forms for the driving forces corresponding to the internal energy developed in the previous section can be computed using (26) together with the change of variables (29) and the expressions for the distinct terms of the internal energy given in (52). After some algebra, where the simplifying assumption $\partial\left(J_{\mathrm{tr}}\right)^{-1} / \partial \xi^{(\alpha)} \approx 0$ is used, it is possible to decompose the driving forces based on their relevant mechanism as follows:

$$
\begin{aligned}
& f_{\mathrm{tr}}^{(\alpha)}=f_{\mathrm{m}}^{(\alpha)}+f_{\mathrm{m}, \mathrm{th}}^{(\alpha)}+f_{\mathrm{th}}^{(\alpha)}+f_{\mathrm{d}}^{(\alpha)}+f_{\mathrm{s}}^{(\alpha)}, \\
& g_{\mathrm{A}}^{(\mathrm{i})}=g_{\mathrm{m}}^{(\mathrm{i})}+g_{\mathrm{th}}^{(\mathrm{i})}+g_{\mathrm{d}}^{(\mathrm{i})},
\end{aligned}
$$

where $f_{\mathrm{m}}^{(\alpha)}, f_{\mathrm{m}, \mathrm{th}}^{(\alpha)}, f_{\mathrm{th}}^{(\alpha)}, f_{\mathrm{d}}^{(\alpha)}$ and $f_{\mathrm{s}}^{(\alpha)}$ stand for the purely mechanical contribution, the coupled thermomechanical contribution, the purely thermal contribution, the defect energy contribution and the surface energy contribution, respectively, as given by

$$
\begin{aligned}
& f_{\mathrm{m}}^{(\alpha)}= J_{\mathrm{tr}} J_{\mathrm{th}} \mathbf{F}_{\mathrm{p}}^{\mathrm{T}} \mathbf{F}_{\mathrm{th}}^{\mathrm{T}} \mathbf{F}_{\mathrm{e}}^{\mathrm{T}} \mathbf{F}_{\mathrm{e}} \mathbf{S F}_{\mathrm{th}}^{-\mathrm{T}} \mathbf{F}_{\mathrm{p}}^{-\mathrm{T}} \mathbf{F}_{\mathrm{tr}}^{-\mathrm{T}} \cdot\left(\mathbf{b}^{(\alpha)} \otimes \mathbf{d}^{(\alpha)}\right) \\
&+\frac{1}{2}\left(J_{\mathrm{th}, \mathrm{A}} \mathbb{C}_{\mathrm{A}}-\left(1+\delta_{\mathrm{T}}\right) J_{\mathrm{th}}^{(\alpha)} \mathbb{C}^{(\alpha)}\right) \mathbf{E}_{\mathrm{e}} \cdot \mathbf{E}_{\mathrm{e}}, \\
& f_{\mathrm{m}, \mathrm{th}}^{(\alpha)}= J_{\mathrm{th}} \mathbf{F}_{\mathrm{e}}^{\mathrm{T}} \mathbf{F}_{\mathrm{e}} \mathbf{S F}_{\mathrm{th}}^{-\mathrm{T}} \cdot\left(\left(1+\delta_{\mathrm{T}}\right) \mathbf{A}^{(\alpha)}-\mathbf{A}_{\mathrm{A}}\right)\left(\theta-\theta_{0}\right), \\
& f_{\mathrm{th}}^{(\alpha)}= \rho_{0} \frac{\lambda_{\mathrm{T}}^{(\alpha)}}{\theta_{\mathrm{T}}}\left(\theta-\theta_{\mathrm{T}}\right)+\rho_{0}\left(h_{\mathrm{A}}-h^{(\alpha)}\right)\left(\theta-\theta_{\mathrm{T}}-\theta \ln \left(\frac{\theta}{\theta_{\mathrm{T}}}\right)\right), \\
& f_{\mathrm{d}}^{(\alpha)}= \frac{\omega_{\mathrm{A}}}{2}\left(J_{\mathrm{th}, \mathrm{A}} \mu_{\mathrm{A}}-\left(1+\delta_{\mathrm{T}}\right) J_{\mathrm{th}}^{(\alpha)} \mu^{(\alpha)}\right) \beta^{2}, \\
& f_{\mathrm{s}}^{(\alpha)}= \frac{\chi}{l_{0}}\left(2 \xi^{(\alpha)}-1\right).
\end{aligned}
$$

Similarly, the contributions of the mechanical energy, the thermal energy and the defect energy to the driving force for plasticity are, respectively,

$$
\begin{aligned}
& g_{\mathrm{m}}^{(\mathrm{i})}=J_{\mathrm{th}} \mathbf{F}_{\mathrm{th}}^{\mathrm{T}} \mathbf{F}_{\mathrm{e}}^{\mathrm{T}} \mathbf{F}_{\mathrm{e}} \mathbf{S F}_{\mathrm{th}}^{-\mathrm{T}} \cdot\left(\mathbf{m}_{\mathrm{A}}^{(\mathrm{i})} \otimes \mathbf{n}_{\mathrm{A}}^{(\mathrm{i})}\right), \\
& g_{\mathrm{th}}^{(\mathrm{i})}=\rho_{0} \theta \phi_{\mathrm{A}}^{(\mathrm{i})}, \\
& g_{\mathrm{d}}^{(\mathrm{i})}=-\omega_{\mathrm{A}} \mu \beta w^{(\mathrm{i})}.
\end{aligned}
$$

Typically, the most relevant contributions to the transformation driving force are $f_{\mathrm{m}}^{(\alpha)}$ and $f_{\mathrm{th}}^{(\alpha)}$ given by $(54)_{1,3}$. More specifically, the main contribution is the first term in each of these expressions (i.e., the stress resolved on a transfor-

mation system in $(54)_1$ and its thermal analogue in $(54)_3$. Other terms in the transformation driving force that account for changes in energy due to changes in material properties may have a significant influence if, for example, there is a large difference in stiffness, thermal expansion and/or specific heat between the parent phase (austenite) and the product phase (martensite). Similarly, the most important contribution for the plastic driving force is $g_{\mathrm{m}}^{(i)}$ (i.e., the stress resolved on a slip system). The thermal analogue to the resolved stress (i.e., $g_{\mathrm{th}}^{(i)}$ in $(55)_2$) appears to have a minor contribution. Finally, the term $g_{\mathrm{d}}^{(i)}$, which is meant to account for the increase in stored energy due to elastic distortion around dislocation cores, is always negative and thus acts against plastic slip. However, $g_{\mathrm{d}}^{(i)}$ has typically a minor contribution compared to the resolved stress.

Following the approach of Onsager for irreversible thermodynamics (Callen, 1985), constitutive relations for the evolution of the internal variables $\xi$ and $\gamma$ need to be specified in the form of kinetic relations. These relations must comply with the dissipation inequality that in the present framework is assumed to take the form given in (27). For the phase transformation process, the following kinetic relation for the rate of growth of the volume fraction of system $\alpha$ is adopted (Turteltaub and Suiker, 2005, 2006b)

$$
\dot{\xi}^{(\alpha)}= \begin{cases}\dot{\xi}_{0} \tanh \left(\frac{f^{(\alpha)}-f_{\mathrm{cr}}^{(\alpha)}}{v f_{\mathrm{cr}}^{(\alpha)}}\right) & \text { if } f^{(\alpha)} \geqslant f_{\mathrm{cr}}^{(\alpha)}, \\ 0 & \text { otherwise, }\end{cases}
\tag{56}
$$

where $\dot{\xi}_{0}>0$ is the maximum value of the transformation rate, $v$ is a dimensionless, viscosity-like parameter and $f_{\mathrm{cr}}^{(\alpha)}$ is a critical value that acts as an energy barrier for the transformation process.

Similarly, the following kinetic relation is used for the evolution of plastic slip on system $i$ in the austenite (Tjahjanto et al., 2008a)

$$
\dot{\gamma}_{\mathrm{A}}^{(i)}= \begin{cases}\dot{\gamma}_{0}^{i \mathrm{~A}}\left(\left(\frac{g_{\mathrm{A}}^{(i)}}{s_{\mathrm{A}}^{(i)}}\right)^{\left(\frac{1}{n_{\mathrm{A}}}\right)}-1\right) & \text { if } g_{\mathrm{A}}^{(i)} \geqslant s_{\mathrm{A}}^{(i)}, \\ 0 & \text { otherwise, }\end{cases}
\tag{57}
$$

where $\dot{\gamma}_{0}^{i \mathrm{~A}}$ is a reference slip rate, $n_{\mathrm{A}}$ is the rate-sensitivity exponent and $s_{\mathrm{A}}^{(i)}$ is the resistance against slip on system $i$. The resistance against slip is taken to evolve according to the following hardening relation:

$$
\dot{s}_{\mathrm{A}}=\sum_{j=1}^{N} H_{\mathrm{A}}^{(i, j)} \dot{\gamma}_{\mathrm{A}}^{(j)},
\tag{58}
$$

where the hardening moduli of the austenite $H_{\mathrm{A}}^{(i, j)}$ are given as

$$
H_{\mathrm{A}}^{(i, j)}=\left(\left(1-q_{\mathrm{A}}\right) \delta_{i j}+q_{\mathrm{A}}\right) k_{\mathrm{A}}^{(j)}.
\tag{59}
$$

In (59), $q_{\mathrm{A}}$ is the latent hardening ratio, which accounts for the difference between cross and self-hardening, $k_{\mathrm{A}}^{(j)}$ is the single slip hardening modulus of slip system $j$ and $\delta_{i j}$ is Kronecker's delta. The evolution of the single slip hardening modulus is given by Tjahjanto et al. (2008a)

$$
k_{\mathrm{A}}^{(i)}=k_{0}^{\mathrm{A}}\left(1-\frac{s_{\mathrm{A}}^{(j)}}{s_{\infty}^{\mathrm{A}}}\right)^{u_{\mathrm{A}}},
\tag{60}
$$

where $k_{0}^{\mathrm{A}}$ is a reference hardening modulus, $s_{\infty}^{\mathrm{A}}$ is the hardening saturation value, and $u_{\mathrm{A}}$ is the hardening exponent.

In order to determine the form of the weighting functions $w^{(i)}$ introduced in (20), a kinetic relation for the evolution of the effective plastic microstrain $\beta$ is presented. Analogous to the expression used for the effective plastic velocity gradient in (5), the rate of change of the effective plastic microstrain $\beta$ is related to the rate of change of the plastic microstrain $\beta_{\mathrm{A}}$ within the austenitic phase as

$$
\dot{\beta}=\tilde{\xi}_{\mathrm{A}} \dot{\beta}_{\mathrm{A}}=\frac{\tilde{\xi}_{\mathrm{A}}}{J_{\mathrm{tr}}} \dot{\beta}_{\mathrm{A}}.
\tag{61}
$$

The rate of change of $\beta_{\mathrm{A}}$ is assumed to depend linearly on the rate of change of the slip resistance in austenite as

$$
c_{\mathrm{A}} \mu_{\mathrm{A}} \dot{\beta}_{\mathrm{A}}=\frac{1}{N} \sum_{i=1}^{N} \dot{s}_{\mathrm{A}}^{(i)},
\tag{62}
$$

where $\mu_{\mathrm{A}}$ is the equivalent isotropic shear modulus of the austenite and $c_{\mathrm{A}}$ is a scaling factor that accounts for dislocation interaction (Tjahjanto et al., 2008a). Combining (7), (58), (61) and (62) results in

$$
\dot{\beta}=\frac{1}{c_{\mathrm{A}} \mu_{\mathrm{A}} N} \sum_{i=1}^{N} \sum_{j=1}^{N} H_{\mathrm{A}}^{(i, j)} \dot{\gamma}^{(j)}.
\tag{63}
$$

Comparing (63) and (20) allows to identify the weighting functions $w^{(i)}$ as

$$
w^{(i)}=\frac{1}{c_{\mathrm{A}} \mu_{\mathrm{A}} N} \sum_{j=1}^{N} H_{\mathrm{A}}^{(j, i)}.
\tag{64}
$$

The last kinetic relation necessary to complete the model is the heat conduction relation for which a classical model is used (Fourier's law), i.e., taking the entropy flux as $\boldsymbol{\Phi}=\mathbf{q} / \theta$, with $\mathbf{q}$ the heat flux, then

$$
\mathbf{q}=-\mathbf{K} \nabla \theta,
\tag{65}
$$

where $\mathbf{K}$ is the heat conductivity tensor. The kinetic relations (56), (57) and (65) satisfy the dissipation inequality (27) with appropriate restrictions (e.g., the tensor $\mathbf{K}$ must be positive semi-definite). For simplicity, isotropic models are adopted for thermal expansion and thermal conduction, i.e., $\mathbf{A}_{\mathrm{A}}=\alpha_{\mathrm{A}} \mathbf{I}, \mathbf{A}^{(\alpha)}=\alpha^{(\alpha)} \mathbf{I}, \mathbf{K}_{\mathrm{A}}=k_{\mathrm{A}} \mathbf{I}$ and $\mathbf{K}^{(\alpha)}=k^{(\alpha)} \mathbf{I}$, with $\alpha_{\mathrm{A}}, \alpha^{(\alpha)}, k_{\mathrm{A}}$ and $k^{(\alpha)}$ the corresponding coefficients of thermal expansion and heat conduction for the austenite and martensite.

In the sequel, simulations will be presented for single crystals of austenite and for grains of austenite embedded in an aggregate of ferritic grains. The model used for ferrite may be formally derived from the model for austenite by suppressing all features related to phase transformation. However, since ferrite has a BCC structure while austenite is FCC, there are some differences in the formulation. Apart from using different slip systems (and numerical values for the model parameters), the model for BCC ferrite includes a

non-Schmid term in the resistance to plastic slip. Details are omitted here and can be found in Tjahjanto et al. (2006). These models are used to simulate the response of austenitic and ferritic grains subjected to quasi-static thermomechanical loading.

## 3. Numerical simulations

To illustrate the features of the proposed model under thermomechanical loading, two sets of simulations are presented in this section. The first set consists of a single crystal of austenite under homogeneous tension. The second set is a tensile test for a multiphase TRIP steel microstructure composed of a single-crystalline grain of austenite surrounded by a ferritic matrix. The simulations are performed using the finite element package ABAQUS and the constitutive models are implemented using the UMAT and UMATHHT subroutines for a fully-coupled thermomechanical analysis. Details about the numerical time integration of the phase transformation model can be found in Suiker and Turteltaub (2005). The initial-boundary value problem consists of solving simultaneously the balance of linear momentum (for a quasi-static process in the absence of body forces) and the balance of energy (in the absence of non-contact heat exchange), i.e.,

$$\operatorname{div} \mathbf{P}=\mathbf{0}, \quad \rho_{0} \dot{\varepsilon}=\mathbf{P} \cdot \dot{\mathbf{F}}-\operatorname{div} \mathbf{q},\tag{66}$$

together with appropriate initial and boundary conditions for the thermal and mechanical fields.

The material parameters for the austenite, martensite and ferrite used in the simulations are shown in Table 1 with the sub- or superscripts A, M or F indicating the corresponding phase. These parameters are equal to those presented in Tjahjanto et al. (2008b) (see also references therein for additional information on the calibration of those parameters). Detailed crystallographic data for the transformation systems can be found in Turteltaub and Suiker (2006b). Plastic deformation in the FCC austenite is accounted for by considering slip along the systems of the $\langle 110\rangle_{\mathrm{A}}\{111\}_{\mathrm{A}}$ family. For the BCC ferrite, plastic deformation is modeled based on the $\langle 111\rangle_{\mathrm{F}}\{110\}_{\mathrm{F}}$ family and data for the non-Schmid contribution to slip resistance can be found in Tjahjanto et al. (2006). In addition, representative values for the specific heat and thermal conductivities of typical low-allowed carbon steels are taken from Taarea and Bakhtiyarov (2004). Observe that, for simplicity, the conductivity and the specific heat of all phases are taken equal to that of a multiphase steel and they do not depend on temperature, which is a reasonable assumption for the range of temperatures considered in the present analysis.

### 3.1. Austenitic single crystal under uniaxial tension

A simulation is performed on a cubical sample of a single crystal of austenite subjected to an axial nominal strain up to $\varepsilon_{11}=0.2$ using a strain rate of $10^{-4} \mathrm{~s}^{-1}$, where the nominal strain is $\boldsymbol{\varepsilon}=\mathbf{V}-\mathbf{I}$, with $\mathbf{V}$ the left stretch tensor in the polar decomposition of the deformation gradient $\mathbf{F}$. To achieve this mechanical loading condition, three mutually perpendicular faces of the cube are constrained along their normals while pulling the top plane of the specimen in $x_{1}$-direction with the prescribed loading rate (see Fig.1). The two remaining faces are set to be traction-free. A zero heat-flux boundary condition is applied in the thermomechanical simulation, hence there is no heat exchanged with the surrounding environment. To study the effect of the internal heat generated from inelastic mechanisms (transformation and plasticity) on the mechanical response, each thermomechanical simulation is repeated under isothermal conditions for comparison purposes. In the isothermal simulations only the linear momentum equation is solved with a temperature equal to the initial temperature of its thermomechanical counterpart. To assess the effect of the initial temperature, each type of simulation, i.e., isothermal and thermomechanical, is performed for two different values of the initial temperature, namely $\theta_{0}=300 \mathrm{~K}$ and $\theta_{0}=350 \mathrm{~K}$. Due to the anisotropic mechanical properties of the austenite and the martensite, the aforementioned simulations are performed for two crystalline orientations such that the loading direction $x_{1}$ corresponds to the crystallographic directions $[100]_{\mathrm{A}}$ and $[111]_{\mathrm{A}}$, measured with respect to the austenitic crystal lattice as shown in Fig. 1. The sample is initially fully austenitic, stress-free and the reference temperature $\theta_{0}$ for the thermal strains is set to coincide with the initial temperature, hence the initial thermal deformation gradient is identity.

#### 3.1.1. Tension along the $[100]_{\mathrm{A}}$ direction

The results for the sample loaded along the $[100]_{\mathrm{A}}$ direction are shown in Fig. 2. The figure indicates the evolution of (a) the axial component $T_{11}$ of the Cauchy stress tensor $\mathbf{T}$, (b) the temperature $\theta$, (c) the total martensitic volume fraction $\xi_{\mathrm{M}}=\sum_{\alpha=1}^{N} \xi^{(\alpha)}$ and (d) the plastic microstrain $\beta$, as a function of the axial logarithmic strain $e_{11}$, where the logarithmic strain is $\mathbf{e}=\ln \mathbf{V}$. The total volume fraction $\xi_{\mathrm{M}}$ monitors the nucleation and subsequent growth of the martensitic phase whereas plastic slip can be correlated to the plastic microstrain $\beta$. From Fig. 2a, it can be observed that the evolution of the axial stress $T_{11}$ is significantly different for the thermomechanical case (labeled as "th.mech.") and the isothermal case (labeled as "iso.th."). In the isothermal case, there is a clear stress plateau as the austenite gradually transform into martensite, i.e., as $\xi_{\mathrm{M}}$ increases from 0 to 1 (see Fig. 2c). The stress response curve exhibits a plateau in accordance with the constitutive model that does not contemplate hardening as a direct result of the phase transformation mechanism (i.e., nucleation of new martensite is not hindered by the previous appearance of that phase). The stress plateau for the isothermal deformation at $\theta_{0}=300 \mathrm{~K}$ starts at a lower strain than for the isothermal deformation at $\theta_{0}=350 \mathrm{~K}$ since, in the latter case, the austenite deforms plastically prior to the nucleation of martensite (compare the evolution of $\xi_{\mathrm{M}}$ and $\beta$ in Fig. 2c and d, respectively). Moreover, from Fig. 2d, it can be seen that for the isothermal deformation at $\theta_{0}=300 \mathrm{~K}$ there is no plastic slip and for the isothermal deformation at $\theta_{0}=350 \mathrm{~K}$ plastic slip is suppressed as soon as the material starts to transform (see Fig. 2c and d. The end of the stress plateau for both temperatures corresponds to the point where the austenite has fully transformed into martensite, which behaves elastically.

<table><thead><tr><th>Parameter(s)</th><th>Value(s)</th><th>Equation(s)</th></tr></thead><tbody><tr><td colspan="3">Mechanical</td></tr><tr><td>Elastic moduli</td><td>$\kappa_1^A = 286.8$, $\kappa_2^A = 166.4$, $\kappa_3^A = 145.0$(GPa)
$\kappa_1^M = 372.4$, $\kappa_2^M = 345.0$, $\kappa_3^M = 191.0$(GPa)
$\kappa_4^M = 508.4$, $\kappa_5^M = 201.9$, $\kappa_6^M = 229.5$(GPa)
$\kappa_1^F = 233.5$, $\kappa_2^F = 135.5$, $\kappa_3^F = 118.0$(GPa)</td><td>(32)</td></tr><tr><td>Transformation kinetic parameters</td><td>$\dot{\zeta}_0 = 0.003(s^{-1})$, $\nu = 0.17$,$f_{\rm cr}^{(\alpha)} = 306$(MPa)</td><td>(56)</td></tr><tr><td>Surface energy parameters</td><td>$\chi = 0.2({\rm J} \cdot {\rm m}^{-2})$, $l_0 = 0.05(\mu {\rm m})$</td><td>$(44)_2$, $(54)_5$</td></tr><tr><td>Plastic kinetic parameters</td><td>$\dot{\gamma}_{0}^{\rm A} = 0.001({\rm s}^{-1})$, $n_{\rm A} = 0.02$
$\dot{\gamma}_{0}^{\rm F} = 0.001({\rm s}^{-1})$, $n_{\rm F} = 0.02$</td><td>(57)</td></tr><tr><td>Defect energy parameters</td><td>$\beta_{\rm A,0} = 0.0056$, $c_{\rm A} = 0.5$, $\omega_{\rm A} = 10$
$\beta_{\rm F,0} = 0.0056$, $c_{\rm F} = 0.5$, $\omega_{\rm F} = 7$</td><td>$(44)_1$, (62), (63), (64)</td></tr><tr><td>Hardening parameters</td><td>$\mu_{\rm A} = 67.5$, $\mu^{(\alpha)} = 98.4$, $\mu_{\rm F} = 55.0$(GPa)
$s_{\rm A,0} = 189$, $s_\infty^{\rm A} = 579$(MPa)
$k_0^{\rm A} = 3$(GPa), $u_{\rm A} = 2.8$, $q_{\rm A} = 1$
$s_{\rm F,0} = 154$, $s_\infty^{\rm F} = 412$(MPa)
$k_0^{\rm F} = 1.9$(GPa), $u_{\rm F} = 2.8$, $q_{\rm F} = 1$</td><td>(60), (59)</td></tr><tr><td colspan="3">Thermal</td></tr><tr><td>Thermal driving force parameters</td><td>$\lambda_{\rm T}^{(\alpha)} = -50.5({\rm kJ\ kg^{-1}})$, $\phi_{\rm A}^{(i)} = 5.13({\rm J\ kg^{-1}\ K^{-1}})$
$\phi_{\rm F}^{(i)} = 4.27({\rm J\ kg^{-1}\ K^{-1}})$, $\theta_{\rm T} = 633$(K)</td><td>$(48)$, $(54)_3$, $(55)_2$</td></tr><tr><td>Specific heat</td><td>$h_{\rm A} = h^{(\alpha)} = h_{\rm F} = 450({\rm J\ kg^{-1}\ K^{-1}})$</td><td>(40)</td></tr><tr><td>Thermal expansion coefficient</td><td>$\alpha_{\rm A} = \alpha^{(\alpha)} = 2.1 \times 10^{-5}$, $\alpha_{\rm F} = 1.7 \times 10^{-5}({\rm K^{-1}})$</td><td>(49), (50)</td></tr><tr><td>Heat conductivity</td><td>$k_{\rm A} = k^{(\alpha)} = k_{\rm F} = 60({\rm W\ m^{-1}\ K^{-1}})$</td><td>(65)</td></tr></tbody></table>

![](./images/813309090720645120_2.jpg)

Fig. 1. Austenitic single crystal sample loaded in two distinct crystalline orientations.

In contrast to the isothermal case, the stress in the austenite in the thermomechanical case under zero heat flux boundary conditions shows a gradual increase with continuous deformation. Both inelastic mechanisms (plasticity and transformation) are active throughout the process as shown in Figs. 2c and d, i.e., in this case the transformation mechanism does not suppress the plastic deformation. The difference in the stress response between the isothermal and thermomechanical cases can be explained as follows: The heat generated from the inelastic processes increases the temperature of the material as shown in Fig. 2b. According to $(54)_3$, an increase in temperature results in a decrease in the thermal contribution to the transformation driving force $f_{\rm th}^{(\alpha)}$ (observe that, in view of the values shown in Table 1, $f_{\rm th}^{(\alpha)}$ is a monotonically decreasing function of the temperature). This feature reflects the fact that austenite is more stable at higher temperatures. The main contributions of the total transformation driving force $f^{(\alpha)}$ are the thermal part, $f_{\rm th}^{(\alpha)}$, and the mechanical part, $f_{\rm m}^{(\alpha)}$. Consequently, in order to further activate the phase transformation mechanism, as the thermal part $f_{\rm th}^{(\alpha)}$ decreases with temperature, a larger stress is required for the mechanical part $f_{\rm m}^{(\alpha)}$ to increase up to the point where the total driving force $f^{(\alpha)}$ reaches the critical value $f_{\rm cr}^{(\alpha)}$. Hence, an increase in temperature produces an apparent stress "hardening" observed in the stress response curves that is not directly associated with plastic hardening (see, e.g., the stress response in Fig. 2a for the thermomechanical case with $\theta_0 = 300$ K where initially there is no plastic deformation as can be observed from Fig. 2d).

For the thermomechanical case, the evolution of the temperature $\theta$ is depicted in Fig. 2b. Since the specimen is subjected to zero normal heat flux at external boundaries, the change in temperature occurs due to the internal heat generated from the inelastic processes. In view of the fact that there is an explicit expression for the internal energy, the temperature field can be obtained as the solution of (66) without the need to assume that a constant portion of the inelastic mechanical power is converted into heat (i.e., a fraction of the last two terms on the right hand side of (15)). Instead, the expression given in (52) is used to solve $(66)_2$ iteratively, in the present case with a Newton-Raphson algorithm. As can be seen in Fig. 2b, the temperature in the simulation with the lower initial temperature ($\theta_0 = 300$ K) increases at a higher rate and eventually becomes larger than the temperature in the simulation with

![](./images/813309090720645120_3.jpg)

Fig. 2. Response of a single crystal of austenite loaded in the $[100]_A$ direction for two initial temperatures ($\theta_0=300$ K and $\theta_0=350$ K) for the isothermal and thermomechanical (zero heat flux) cases: Evolution as a function of the axial logarithmic strain $e_{11}$ of (a) the Cauchy axial stress $T_{11}$, (b) temperature $\theta$, (c) martensitic volume fraction $\xi_M$ and (d) plastic microstrain $\beta$.

the larger initial temperature $(\theta_0=350$ K). This result, which at first sight might be counterintuitive, can be traced back to the underlying deformation mechanisms. Indeed, as indicated in Fig. 2c, more austenite transforms into martensite in the simulation with $\theta_0=300$ K than in the simulation with $\theta_0=350$ K. Conversely, from Fig. 2d, more plastic deformation is observed in the simulation with $\theta_0=350$ K than in the simulation with $\theta_0=300$ K. Thus, it may be concluded that more heat is generated due to the phase transformation than due to plastic deformation, which correlates with the evolutions of the temperatures shown in Fig. 2b. This feature also serves to explain why the initial "thermal" stress hardening discussed above and shown in Fig. 2a is higher for the simulation with $\theta_0=300$ K than in the simulation with $\theta_0=350$ K.

### 3.1.2. Tension along the $[111]_A$ direction

The results for the sample loaded in the $[111]_A$ direction, for two initial temperatures $\theta_0=300$ K and $\theta_0=350$ K and the corresponding isothermal cases, are shown in Fig. 3 in terms of the evolution of the axial Cauchy stress $T_{11}$, the temperature $\theta$, the total martensitic volume fraction $\xi_M$ and the plastic microstrain $\beta$. In this case, except for the isothermal simulation at $\theta=300$ K, all responses are nearly identical in terms of the stress, transformation and plastic behavior (see Fig. 3a, c and d, respectively). In the isothermal simulation at $\theta=300$ K both inelastic mechanisms (plasticity and transformation) are active until the austenite fully transforms into martensite, effectively suppressing plasticity since the martensite deforms elastically. In contrast, the other three simulations (isothermal at $\theta=350$ K and thermomechanical with initial temperatures $\theta_0=300$ K and $\theta_0=350$ K), are dominated by plastic deformation with little or no phase transformation and, from this point of view, the corresponding responses differ significantly from those of the sample loaded along the $[100]_A$ direction shown in Fig. 2. The plastic driving force, as given in (55), has only a weak dependence on the temperature for the given set of material parameters indicated in Table 1. Consequently, the stress response for the thermomechanical case does not significantly diverge from the isothermal case in a process dominated by plasticity.

The differences between the responses of the specimens loaded in the $[100]_A$ and $[111]_A$ directions can be traced back to the mechanical part of the transformation driving force shown in $(54)_1$, in particular the first term that involves an inner product with the transformation strain $\mathbf{b}^{(\alpha)} \otimes \mathbf{d}^{(\alpha)}$. Indeed, based on the crystallographic data for the transformation systems (see Turteltaub and Suiker (2006b)), the axial stress required to nucleate martensite is significantly larger when a specimen is loaded in the $[111]_A$ direction compared to a specimen loaded in the $[100]_A$ direction. Similarly, in view of the expression of the mechanical plastic driving force $g_{\mathrm{m}}^{(i)}$ given by $(55)_1$ (i.e., the Schmid stress), the axial stress required to trigger plastic slip is also larger for a specimen loaded in the $[111]_A$ direction compared to a specimen loaded in the $[100]_A$ direction. Nevertheless, the stress required to activate plasticity is less than the stress required to nucleate a transformation system for a specimen loaded in the $[111]_A$-direction, thus plastic slip becomes the preferred inelastic mechanism. In addition, as the temperature increases, the thermal part of the transformation driving force decreases (see $(54)_3$ and note that $\lambda_T<0$) while the thermal part of the plastic driving forces increases (see

![](./images/813309090720645120_4.jpg)

Fig. 3. Response of a single crystal of austenite loaded in the $[111]_{\mathrm{A}}$
direction for two initial temperatures ($\theta_0=300$ K and $\theta_0=350$ K) for the
isothermal and thermomechanical (zero heat flux) cases: Evolution as a
function of the axial logarithmic strain $e_{11}$ of (a) the Cauchy axial stress
$T_{11}$, (b) temperature $\theta$, (c) martensitic volume fraction $\xi_{\mathrm{M}}$ and (d) plastic
microstrain $\beta$.

$(55)_2$), which reinforces the preference of plasticity as an
inelastic mechanism at larger temperatures.

The results of the simulations for a single crystal of aus-
tenite shown in this section are in good qualitative agree-
ment with high-energy X-ray diffraction measurements
recently presented in Blondé et al. (2012) where it was ob-
served that the transformation rate increases with decreas-
ing temperature and that the transformation occurs
preferentially when the grain is loaded in the $[100]_{\mathrm{A}}^{-}$
direction.

### 3.2. Austenitic grain embedded in a ferritic matrix

To study the thermomechanical interaction between
the constituent phases of a typical low-alloyed multiphase
TRIP steel, a cubic sample consisting of a single grain of
retained austenite embedded in a matrix of six ferritic
grains is considered in this section, as shown in Fig. 4.
The cubic sample has a side length of $3\ \mu\mathrm{m}$ and the polyhe-
dral austenitic grain has a characteristic size of $2\ \mu\mathrm{m}$ and
occupies approximately 13% of the total volume (i.e., the
initial volume fraction of austenite is $\xi_{\mathrm{A},0}=0.13$). The sam-
ples are discretized with a total number of 864 linear hexa-
hedral elements. The loading of the sample is similar to the
uniaxial deformation tests in the previous section with an
average extensional strain rate of $10^{-4}\mathrm{s}^{-1}$ along the $x_{1}-$
direction that is achieved by imposing a normal displace-
ment on the top face, zero normal displacements imposed
on the bottom and two lateral faces and traction-free con-
ditions prescribed on the remaining directions and exter-
nal faces. For the thermomechanical simulations, a
uniform initial temperature of $\theta_0=300$ K is applied and
zero heat flux is prescribed on the external surfaces of
the specimen. Heat can flow and be exchanged between
the distinct phases according to Fourier's law of heat con-
duction. The sample is initially stress-free with zero ther-
mal strain prior to the loading, i.e., the reference
temperature for the thermal strains in all phases is set
equal to the initial temperature $\theta_0$. To explore the influence
of the crystal orientations on the sample's response, two
crystal orientations are analyzed, namely (i) all ferritic
grains and the austenitic grain are oriented such that the
loading direction $x_1$ coincides respectively with the
$[100]_{\mathrm{F}}$ and $[100]_{\mathrm{A}}$ directions and (ii) all ferritic grains and
the austenitic grain are oriented such that the loading
direction $x_1$ coincides respectively with the $[111]_{\mathrm{F}}$ and
$[111]_{\mathrm{A}}$ directions. In Fig. 4 these two orientations are de-
noted as $[100]_{\mathrm{A,F}}$ and $[111]_{\mathrm{A,F}}$. The motivation for this
choice of orientations is that they represent "soft" and

![](./images/813309090720645120_5.jpg)

Fig. 4. Grain of retained austenite surrounded by a ferrite-based matrix.
The sample is loaded along the $x_1$-direction and two distinct crystal
orientations are considered (see inset).

![](./images/813309090720645120_6.jpg)

Fig. 5. Response of an aggregate of austenitic and ferritic grains for an isothermal simulation at $\theta_0$ = 300 K and a thermomechanical (zero heat flux) simulation with initial temperature $\theta_0$ = 300 K: Evolution as a function of the average axial logarithmic strain $\bar{e}_{11}$ of (a) the average Cauchy axial stress $\bar{T}_{11}$, (b) the average temperature $\bar{\theta}$, (c) the normalized austenitic volume fraction $\bar{\xi}_A$ and (d) the phase-averaged plastic microstrain $\bar{\beta}$.

"hard" responses, thus they characterize lower and upper limits for the possible combinations of the crystallographic orientations of the two phases.

The isothermal and thermomechanical response are shown in Fig. 5 in terms of (a) the average axial Cauchy stress $\bar{T}_{11}$, (b) the average temperature $\bar{\theta}$, (c) the normalized austenitic volume fraction $\bar{\xi}_A = \xi_A/\xi_{A,0}$ and (d) the phase-averaged plastic microstrain $\bar{\beta}$ for each phase (i.e., $\beta$ averaged over the austenitic grain as shown on the left, and $\beta$ averaged over the ferritic grains as shown on the right). The stress, strain and the temperature are averaged over the whole cubic sample whereas the microstrains are averaged over the corresponding phases (ferrite and austenite).

As anticipated, the stress response for the $[111]_{A,F}-$ loaded sample is considerably higher than for the $[100]_{A,F}-$loaded sample, both for the isothermal and ther- momechanical cases (see Fig. 5a). However, the differences between the isothermal and thermomechanical cases for the same orientation are relatively small. This is due to the facts that (i) the samples contain mostly ferrite, whose stress response dominates the overall behavior and (ii) in the present model the isothermal and thermomechanical responses for the ferritic phase are similar since the plastic driving force only depends weakly on temperature and the resistance to plastic slip is taken to be temperature- independent.

The increase in temperature in the thermomechanical simulations of the aggregate of ferrite and austenite is on average smaller than for the single crystal of austenite (compare Fig. 5b with Fig. 2b and Fig. 3b for $\theta_0$ = 300 K). As for the stress response, the significant amount of fer- rite in the sample (87%) dominates the overall thermal behavior. The internal heat generation in the ferrite is only due to plastic deformation and it is less significant than the heat generated due to phase transformation in the austenite. Consequently, the average heat generated per unit volume in the aggregate of ferrite and austenite is less than in the austenitic single crystal. Moreover, con- tour plots of the temperature (not presented here) indi- cate that the loading is sufficiently slow for the heat generated in the austenite from the transformation to be conducted towards the ferritic matrix, as a result of which the temperature field is nearly spatially uniform. Hence, as the heat generated in the austenite due to transformation is conducted towards the ferritic matrix, the austenitic grain remains cooler in an aggregate com- pared to the single crystal case. Since the temperature in the austenite in an aggregate does not increase as much as for the single crystal, it is easier to trigger a phase transformation in the former case than in the latter. This phenomenon also serves to explain why the (normal- ized) transformation rates $d\bar{\xi}_M/d\bar{e}_{11}$ in the thermomechanical simulations of aggregates loaded in the $[100]_{A,F}$ and $[111]_{A,F}-$directions are higher than the transformation rates $d\bar{\xi}_M/de_{11}$ in the thermomechanical simulations of a single crystal for the corresponding loading directions $[100]_A$ and $[111]_A$ (compare Fig. 5c with the thermomechanical curves for $\theta_0$ = 300 K in Fig. 2c and Fig. 3c keeping in mind that $\bar{\xi}_M = 1 - \bar{\xi}_A$ hence $d\bar{\xi}_M/d\bar{e}_{11} = -d\bar{\xi}_A/d\bar{e}_{11}$). Nevertheless, as in the single crystal case, the transformation rates in the thermomechanical simulations of austenite-ferrite aggregates remain lower than the transformation rates for the corresponding isothermal simulations in the same aggregates due to the increase in temperature in the former case (see Fig. 5c).

## 4. Conclusion

A thermomechanical model applicable to individual single-crystal grains of austenite undergoing plastic deformation and phase transformation has been developed with special emphasis on a thermodynamically-consistent formulation for the thermomechanical coupling. Consistency is achieved through a decomposition of the entropy density that includes an entropic counterpart of the thermal deformation gradient. The model was used to analyze fully-coupled thermomechanical deformations of a single crystal of austenite as well as an aggregate of austenitic and ferritic grains. The simulations indicate that for a single crystal of austenite, the increase in temperature associated with the latent heat of transformation reduces the transformation rate and significantly delays the transformation-induced plasticity effect. Consequently, the effective hardening response under axial deformation of a thermally-insulated sample is initially higher but eventually lower compared to a sample deformed under isothermal conditions. However, the delay in the transformation-induced plasticity effect due to the latent heat is relatively small when the ferritic matrix is taken into account. The ferritic matrix absorbs the latent heat generated in the austenite and, since ferrite accounts for a large volume in a multiphase steel, it effectively acts as a thermal sink, thus mitigating the temperature increase. In that case, the effective stress responses for the isothermal and thermomechanical cases are similar. However, it is relevant to indicate that the conclusions from the present study are applicable to quasi-static processes where there is sufficient time for the heat generated in the austenite to flow to the surrounding ferritic matrix. For materials with a more significant volume fraction of austenite (e.g., austenitic alloys) as well as for impact problems involving high strain rates, it can be anticipated that thermal effects may be more significant than for low-alloyed multiphase steels under quasi-static loading.

## Acknowledgment

This research is supported by the Dutch Technology Foundation STW, applied science division of NWO and the Technology Program of the Ministry of Economic Affairs through STW-MuST (Multiscale Simulation Techniques) project 10117.

## References

Berrahmoune, M.R., Berveiller, S., Inal, K., Moulin, A., Patoor, E., 2004. Analysis of the martensitic transformation at various scales in TRIP steel. Mater. Sci. Eng. A-Struct. 378, 304-307.

Bhattacharyya, A., Weng, G., 1994. An energy criterion for the stress-induced martensitic-transformation in a ductile system. J. Mech. Phys. Solids 42, 1699-1724.

Blondé, R., Jimenez-Melero, E., Zhao, L., Wright, J., Brück, E., van der Zwaag, S., van Dijk, N., 2012. High-energy X-ray diffraction study on the temperature-dependent mechanical stability of retained austenite in low-alloyed TRIP steels. Acta Mater. 60, 565-577.

Callen, H., 1985. Thermodynamics and An Introduction to Thermostatistics, second ed. John Wiley & Sons.

Coleman, B., Noll, W., 1963. The thermodynamics of elastic materials with heat conduction and viscosity. Arch. Ration. Mech. Anal. 13, 167-178.

Idesman, A., Levitas, V., Stein, E., 1999. Elastoplastic materials with martensitic phase transition and twinning at finite strains: numerical solution with the finite element method. Comput. Math. Appl. Mech. Eng. 173, 71-98.

Jacques, P., Delannay, F., Ladrière, J., 2001. On the influence of interactions between phases on the mechanical stability of retained austenite in transformation-induced plasticity multiphase steels. Metall. Mater. Trans. A 32, 2759-2768.

Jacques, P., Furnémont, Q., Godet, S., Pardoen, T., Conlon, K., Delannay, F., 2006. Micromechanical characterisation of TRIP-assisted multiphase steels by in situ neutron diffraction. Philos. Mag. 86, 2371-2392.

Jacques, P., Furnémont, Q., Lani, F., Pardoen, T., Delannay, F., 2007. Multiscale mechanics of TRIP-assisted multiphase steels: I. Characterization and mechanical testing. Acta Mater. 55, 3681-3693.

Jiménez, J., Carsí, M., Ruano, O., Frommeyer, G., 2009. Effect of testing temperature and strain rate on the transformation behaviour of retained austenite in low-alloyed multiphase steel. Mater. Sci. Eng. A-Struct. 508, 195-199.

Kouznetsova, V., Geers, M., 2008. A multi-scale model of martensitic transformation plasticity. Mech. Mater. 40, 641-657.

Lani, F., Furnémont, Q., Rompaey, T.V., Delannay, F., Jacques, P., Pardoen, T., 2007. Multiscale mechanics of TRIP-assisted multiphase steels: Ii. Micromechanical modelling. Acta Mater. 55, 3695-3705.

Marketz, F., Fischer, F., 1994. Micromechanical modeling of stress-assisted martensitic-transformation. Model. Simul. Mater. Sci. Eng. 2, 1017-1046.

Mazzoni-Leduc, L., Pardoen, T., Massart, T., 2008. Strain gradient plasticity analysis of transformation induced plasticity in multiphase steels. Int. J. Solids Struct. 45, 5397-5418.

Rusinek, A., Klepaczko, J., 2009. Experiments on heat generated during plastic deformation and stored energy for TRIP steels. Mater. Design 30, 35-48.

Shi, J., Turteltaub, S., Van der Giessen, E., Remmers, J.J.C., 2008. A discrete dislocation - transformation model for austenitic single crystals. Model. Simul. Mater. Sci. Eng., 16.

Shi, J., Turteltaub, S., der Giessen, E.V., 2010. Analysis of grain size effects on transformation-induced plasticity based on a discrete dislocation-transformation model. J. Mech. Phys. Solids 58, 1863-1878.

Stringfellow, R.G., Parks, D.M., Olson, G.B., 1992. A constitutive model for transformation plasticity accompanying strain-induced martensitic transformations in metastable austenitic steels. Acta Metall. Mater. 40, 1703-1716.

Sugimoto, K., Usui, N., Kobayashi, M., Hashimoto, S., 1992. Effects of volume fraction and stability of retained austenite on ductility of TRIP-aided dual-phase steels. ISIJ Int. 32, 1311-1318.

Suiker, A.S.J., Turteltaub, S., 2005. Computational modelling of plasticity induced by martensitic phase transformations. Int. J. Numer. Math. Eng. 63, 1655-1693.

Taarea, D., Bakhtiyarov, S., 2004. General Physical Properties, eighth ed. Butterworth-Heinemann, Oxford.

Tjahjanto, D.D., Turteltaub, S., Suiker, A.S.J., 2008a. Crystallographically based model for transformation-induced plasticity in multiphase carbon steels. Continuum Mech. Therm. 19, 399-422.

Tjahjanto, D.D., Turteltaub, S., Suiker, A.S.J., van der Zwaag, S., 2006. Modelling of the effects of grain orientation on transformation-induced plasticity in multiphase carbon steels. Model. Simul. Mater. Sci. Eng. 14, 617-636.

Tjahjanto, D.D., Turteltaub, S., Suiker, A.S.J., van der Zwaag, S., 2008b. Transformation-induced plasticity in multiphase steels subjected to thermomechanical loading. Philos. Mag. 88, 3369-3387.

Turteltaub, S., Suiker, A.S.J., 2005. Transformation-induced plasticity in ferrous alloys. J. Mech. Phys. Solids 53, 1747-1788.

Turteltaub, S., Suiker, A.S.J., 2006a. Grain size effects in multiphase steels assisted by transformation-induced plasticity. Int. J. Solids Struct. 43, 7322-7336.

Turteltaub, S., Suiker, A.S.J., 2006b. A multiscale thermomechanical model for cubic to tetragonal martensitic phase transformations. Int. J. Solids Struct. 43, 4509-4545.