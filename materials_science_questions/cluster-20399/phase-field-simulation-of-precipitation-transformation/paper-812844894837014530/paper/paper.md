# Numerical Benchmark of Phase-Field Simulations with Elastic Strains: Precipitation in the Presence of Chemo-Mechanical Coupling

Reza Darvishi Kamachali$^{a,b,*}$, Christian Schwarze$^b$, Mingxuan Lin$^c$, Martin Diehl$^a$, Pratheek Shanthraj$^{a,d}$, Ulrich Prahl$^{c,e}$, Ingo Steinbach$^b$, Dierk Raabe$^a$

$^{a}$ Max-Planck-Institut für Eisenforschung GmbH, Max-Planck-Straße 1, 40237 Düsseldorf, Germany
$^{b}$ Interdisciplinary Centre for Advanced Materials Simulation (ICAMS), Ruhr-University Bochum, 44801 Bochum, Germany
$^{c}$ Department of Ferrous Metallurgy, RWTH Aachen University, Intzestraße 1, 52072 Aachen, Germany
$^{d}$ The School of Materials, The University of Manchester, Manchester M13 9PL, UK
$^{e}$ Institut für Metallformung, Technische Universität Bergakademie Freiberg, Bernhard-von-Cotta-Straße, Germany

---

## ARTICLE INFO

**Keywords:**
Phase-field modelling and simulation
Microstructure evolution
Precipitation
Diffusion
Elasticity

## ABSTRACT

Phase-field studies of solid-state precipitation under strong chemo-mechanical coupling are performed and benchmarked against the existing analytical solutions. The open source software packages OpenPhase and DAMASK are used for the numerical studies. Solutions for chemical diffusion and static mechanical equilibrium are investigated individually followed by a chemo-mechanical coupling effect arising due to composition dependence of the elastic constants. The accuracy of the numerical solutions versus the analytical solutions is quantitatively discussed. For the chemical diffusion benchmark, an excellent match, with a deviation <0.1%, was obtained. For the static mechanical equilibrium benchmark Eshelby problem was considered where a deviation of 5% was observed in the normal component of the stress, while the results from the diffuse interface (OpenPhase) and sharp interface (DAMASK) models were slightly different. In the presence of the chemo-mechanical coupling, the concentration field around a static precipitate was benchmarked for different coupling coefficients. In this case, it is found that the deviation increases proportional to the coupling coefficient that represents the strength of coupling concentration and elastic constants. Finally, the interface kinetics in the presence of the considered chemo-mechanical coupling were studied using OpenPhase and a hybrid OpenPhase-DAMASK implementation, replacing the mechanical solver of OpenPhase with DAMASK's. The observed deviations in the benchmark studies are discussed to provide guidance for the use of these results in studying further phase transformation models and implementations involving diffusion, elasticity and chemo-mechanical coupling effect.

---

## 1. Introduction

Modelling and simulation has become an indispensable tool in materials science and engineering, offering tremendous potential to understand, study and design future materials. Advanced full-field simulation techniques and mean-field modelling are especially beneficial in material design to establish processing $\leftrightarrow$ microstructure $\leftrightarrow$ properties relations. In this regard, the current trend of developing multi-physics simulation tools, enhanced by cluster supercomputing and statistical analysis, enables the investigation of coupled thermo-chemo-mechanical phenomena [1-3]. Quantitative modelling and simulation of various coupled physical phenomena can be regarded as the next challenge in this context. Among several full-field approaches, the phase-field method has demonstrated its remarkable ability to treat physically sound studies [4-11]. In particular, the multi-phase-field approach [12-17] has been successfully applied to study complex microstructure evolution such as in solidification [18,19], recrystallization [20-22], particle pinning [23-25], precipitation during aging [26-30] and, grain growth on the micro- [31-35] and nano-scales [36,37]. As individual microstructure evolution mechanisms may either compete or reinforce each other, the coupling between different physical phenomena and their effects on the microstructure and phase evolution become increasingly significant. Moreover, the various nonlinear modes of interaction between different physical phenomena render the validation of the models a challenging task, as even rough estimates for kinetics and equilibrium states are often not available. To address this issue, the provision of carefully selected benchmarks—systematically derived from the

---

* Corresponding author at: Max-Planck-Institut für Eisenforschung GmbH, Max-Planck-Straße 1, 40237 Düsseldorf, Germany.
E-mail addresses: kamachali@mpie.de, reza.darvishi@rub.de (R. Darvishi Kamachali).

https://doi.org/10.1016/j.commatsci.2018.09.011
Received 13 April 2018; Received in revised form 1 September 2018; Accepted 3 September 2018
0927-0256/ © 2018 Elsevier B.V. All rights reserved.

isolated treatment of individual effects—is required to ensure (i) the accuracy of numerical solutions compared to the analytical solution for each individual effect and (ii) to specify uncertainties due to numerical techniques in a multi-physics (coupled) framework. In the current study, a set of such benchmark problems related to chemo-mechanical coupling problems and their reference solutions obtained by open source software packages OpenPhase [38,39] and DAMASK [40,41] are presented.

While most models and their implementation are (hopefully) validated and benchmarked against known solutions, these efforts are usually either not published at all or only briefly discussed as a subsection in a model presentation, that makes it difficult to readily apply benchmarks when developing or extending existing implementations. Some attempts, however, have been made to present reference benchmark solutions for materials modelling. Zhang et al. [42] and Münch [43], for instance, have benchmarked the meshing issues regarding phase-field modelling using finite element techniques. In a systematic effort, the Center for Hierarchical Materials Design (CHiiMaD) and the National Institute of Standards and Technology (NIST) are developing a set of benchmark problems for phase field models [44]. The first set of these benchmarks was published in 2017 by Jokisaari et al. [45], consisting of an Ostwald ripening model and a spinodal decomposition model with different geometries of simulation domain and two different adaptive time stepping techniques. The second set of benchmarks [46] comprises a study of dendritic growth model and a multiphysics model for an elastically constrained precipitate, where the bifurcation of precipitate shape versus the $L'$ parameter (characteristic ratio between elastic and interfacial energies [47]) is stressed. On the dendritic growth, similar benchmark studies was conducted by Karma and Rappel [48] in developing quantitative phase-field schemes for solidification studies. In this work we present and apply benchmarks on solid-state precipitation, similar to the latter benchmarks of Jokisaari et al. [46], but with a focus on a chemo-mechanical coupling effect that features cross-coupled numerical solutions for diffusion and mechanical problems.

Precipitation hardening plays a critical role in enhancing mechanical properties of engineering alloys [49]. This typically includes diffusion-controlled nucleation and growth of a secondary-phase from a supersaturated matrix that is followed by a subsequent competitive ripening process. While formation of interfaces suppresses the growth, the chemical energy difference between the saturated matrix and the precipitates drives the precipitation reaction. In the solid-state, precipitation is often accompanied by transformation strains which results in stresses within and around precipitates. Depending on the local geometry and volume fraction of the precipitates, stresses can either suppress or reinforce precipitation kinetics. As a result of such long-range diffusion and elastic interaction effects, precipitation process becomes a complex, nonlinear problem [50]. Furthermore, a mutual coupling between the stress/strain and concentration fields can also influence the precipitation process that is the focus of this benchmarking study.

The chemo-mechanical coupling effects during precipitation are expected as composition gradients and strain/stress field evolve and interact at the transformation front, simultaneously. As a model system, we consider here the formation of a $\delta'$ precipitate (Al₃Li) in the binary Al-Li system in which a significant coupling effect, arising due to the composition dependence of elastic constants, was found earlier [28,29]. This kind of chemo-mechanical coupling, i.e. composition dependence of elastic constants, was indeed discovered long ago [51] but neglected until recently when its effect on the equilibrium concentration profile around a precipitate has been discussed [52] and applied for studying precipitation in NiTi shape memory alloys [27]. Similar coupling effects manifest themselves in different processes such as bainitic transformation [53], adsorption [54] and shape memory effects [27,55]. Currently, chemo-mechanical coupling effects in metals and polymers are the subject of the priority research programme, SPP1713 [56], initiated by the German Research Foundation (DFG). The current benchmark setups are thought as simple and ensured starting points for numerical studies in the broad community of researchers working on chemo-mechanics problems within and beyond the SPP1713 programme.

In this study, a systematic benchmarking approach—that is hopefully also useful for studying similar problems—is considered in which we first separate the problem of precipitation into diffusion of a second species and mechanical equilibrium, then consider the combined solution of these two problems, i.e. diffusion and mechanical equilibrium with mutual coupling [52], and finally investigate precipitate formation. In the following, the theory and modelling of chemo-mechanical coupling are presented in Section 2. The software packages OpenPhase and DAMASK and a hybrid OpenPhase-DAMASK implementation are briefly introduced in Section 3. The set-up and details of the simulations are presented in Section 4. For the diffusion problem a 1D diffusion couple with a concentration contrast is studied. For elastic equilibrium we consider an inclusion with volumetric expansion and contraction (Eshelby problem). Using these two solvers, the chemo-mechanically coupled relaxation around a static precipitate is discussed. Finally, as an application to our benchmarks, phase-field study of precipitation kinetics in the presence of chemo-mechanical coupling effects (Section 4.4) is presented. The results of the benchmarks are discussed in Section 5.

## 2. Theory and modelling

In this section, first a description of a chemo-mechanical effect, that is the focus of the study, is given. Then, this model is inserted into the phase-field formalism as presented in the following subsections. The free energy functional for a domain $\Omega$ can be written as

$$
F\left(\phi, c, \epsilon\right)=\int_{\Omega}\left\{f_{\text{intf}}+f_{\text{chem}}+f_{\text{elas}}+...\right\} \mathrm{d} V,
\tag{1}
$$

where $f_{\text{intf}}$, $f_{\text{chem}}$, and $f_{\text{elas}}$ are the interfacial, chemical and elastic free energy densities, respectively. These are the energetic contributions of interest in the current benchmark study, but further contributions can be considered in the same formalism. The evolution of a phase $\alpha$ is modelled in terms of the evolution of a non-conserved phase-field variable, $\phi_{\alpha}(x, t)$, using a generalized form of the time dependent Ginzburg-Landau equation [12,13]:

$$
\dot{\phi}_{\alpha}=-\frac{L}{N_{\phi}} \sum_{\alpha=1, \alpha \neq \beta}^{N_{\phi}}\left(\frac{\delta F}{\delta \phi_{\alpha}}-\frac{\delta F}{\delta \phi_{\beta}}\right)
\tag{2}
$$

where $L$ is the interface mobility, $N_{\phi}$ is the total number of phase-fields and $\delta$ indicates functional derivative. The phase-field variables are constrained with $\sum_{i=1}^{N_{\phi}} \phi_{\alpha}=1$. In the absence of convection, the solute atoms redistribute in the system only through diffusion. In a closed system this results in the following continuity equation:

$$
\dot{c}=-\nabla \cdot \mathbf{J}=\nabla \cdot M \nabla \frac{\delta F}{\delta c}
\tag{3}
$$

where $c$ is solute concentration field, $\mathbf{J}$ is the solute flux, $M$ the mobility of the solute atoms, and $\frac{\delta F}{\delta c}$ is the diffusional potential. Eq. (3) drives solute redistribution to reduce the spatial contrast in the total free energy, $F$. Here, the chemo-mechanical interaction results from a mechanical contribution to the solute flux, a scenario that extends the classical Fick's laws to consider the influence of micromechanical effects. A well-known case of such an interaction occurs when the size difference between solute and solvent atoms results in a local distortion. For a dilute solid solution this effect can be approximated by the linear rule of mixtures referred to as Vegard's law. This effect has been extensively discussed in previous studies concerning phase transformation kinetics [57-61].

A lesser known chemo-mechanical interaction phenomenon, that is considered in the current benchmark study, arises when the elastic stiffness of a material depends on its local composition. In the solid-state, the atomic bonds between the solute and solvent atoms, which are responsible for the material behaviour in the presence of a small deformation, are composition-dependent. Thus a variation in bonding strength, represented here by the elastic constants, is expected if the

local composition of the material changes. As a result, if the solute atoms are mobile enough, the ratio of different atomic bonds, even if they are homogeneous, changes under a mechanical loading. Although this kind of chemo-mechanical coupling has been pointed out first by Larche and Cahn [51], it was neglected until recently when it has been investigated for precipitation processes by Darvishi Kamachali et al. [27-29,52]: It has been found that the composition dependence of the elastic constants can lead to an inverse ripening mechanism and re- arrangement of precipitates [28,29]. To express this chemo-mechanical coupling for small changes in the chemical composition amenable to linear approximation, $\Delta c=c(x, t)-c_{ref }$ , we use a Taylor expansion around $c_{ref }$ and truncate after the first term

$$
C^{i j k l}(c)=C_{0}^{i j k l}(1+\varkappa \Delta c)
\tag{4}
$$

where $\varkappa$ is the isotropic chemo-mechanical coupling factor and $C_{0}^{i j k l}$ is the elastic stiffness tensor corresponding to the reference composition of the matrix material. The strength of atomic bonds and their dependence on the composition can be determined from experiments or ab initio calculations. For the binary Al-Li alloy system studied here, ab initio calculations indicate strong and linear dependence of the stiffness on the Li concentration [29]. A mechanically-driven flux of solute atoms is expected due to this chemo-mechanical coupling, that is proportional to the spatial gradient of the chemo-mechanical potential:

$$
-\nabla \frac{\partial f_{\text {elas }}}{\partial c}
\tag{5}
$$

The mechanically-driven flux adds to the usual tendency of atoms to diffuse under the gradients of chemical potentials that correspond to the variation of chemical free energy density, $f_{chem }$ . The total solute flux, therefore, will be

$$
\mathbf{J}=-M \nabla \frac{\delta F}{\delta c}=-M \nabla\left[\frac{\partial f_{\text {chem }}}{\partial c}+\frac{\partial f_{\text {elas }}}{\partial c}\right]
\tag{6}
$$

On the other hand, the mechanical equilibrium of a system in the absence of an external load is obtained by solving

$$
0=\nabla^{i} \cdot \frac{\delta F}{\delta \epsilon^{i j}}=\nabla^{i} \cdot\left[C_{0}^{i j k l}(1+\varkappa \Delta c) \epsilon_{\text {elas }}^{k l}\right]
\tag{7}
$$

where $\epsilon^{i j}$ are strain components, $\nabla^{i} \equiv \frac{\partial}{\partial x_{i}}$ and the Einstein sum convention is used. While Eq. (6) determines the evolution of concentration field depending on the mechanical solution, Eq. (7) is also composition-dependent as a result of the chemo-mechanical coupling. The significance of such a mutual coupling on the precipitation reaction is discussed in the next section.

### 2.1. Significance of chemo-mechanical coupling for precipitation

Precipitation is a diffusion-controlled phase transformation process often accompanied by stresses. This can lead to strong chemo-mechanical interaction between solute and stress gradients around precipitates. The chemo-mechanical coupling phenomenon influences not only the kinetics of precipitation but also the morphology and stability of the precipitates. For an ideal solid solution, the chemically-driven solute flux is given by Fick's law. Assuming an isotropic linear elastic material, with chemo-mechanical coupling given by Eq. (4), the solute flux reads

$$
\mathbf{J}=-D \nabla c-M \frac{\varkappa}{2} \nabla\left[\epsilon_{\text {elas }}^{i j} C_{0}^{i j k l} \epsilon_{\text {elas }}^{k l}\right]
\tag{8}
$$

in which $D$ is the diffusivity. In this relation, the two sub-fluxes defining the system are driven by the spatial gradients of (i) concentration (Fick's first law) and (ii) elastic energy density, respectively. In general, the sub-fluxes may suppress or reinforce each other, depending on the chemical and mechanical states of the system. In [52] the first solution to Eq. (8) for the case of a static precipitate in a matrix with composition-dependent elastic coefficients at equilibrium $(\mathbf{J}=\mathbf{0})$ is presented:

$$
c(r)=c_{0}-g_{0} \varkappa\left(\frac{R}{r}\right)^{6}+O\left(\varkappa^{2}\right)
\tag{9}
$$

Here, $g_{0}=\frac{6 G_{m} V_{m} b^{2}}{\varkappa T}, G_{m}$ is the shear modulus of the matrix, $V_{m}$ is the molar volume of the matrix phase, $c_{0}$ is the matrix composition far from the precipitate and, $b$ is a materials constant

$$
b=-\frac{3}{3} \frac{\epsilon_{p}^{*} B_{p}}{3 B_{p}+4 G_{m}}
\tag{10}
$$

in which $B$ is the bulk modulus and $\epsilon_{p}^{*}$ is the transformation misfit strain that is only non-zero inside the precipitate phase. The subscripts $m$ and $p$ relate to the matrix and precipitate phase, respectively.

In [28], we presented a more general solution of Eq. (8) for a precipitate at the quasi-steady state $(\dot{c}=0)$

$$
c(r)=c_{0}-g_{0} \varkappa\left(\frac{R}{r}\right)^{6}+\left(g_{0} \varkappa-g_{1}\right) \frac{R}{r}+O\left(\varkappa^{2}\right)
\tag{11}
$$

where $g_{1}=c_{0}-c_{R}$ and $c_{R}$ is the equilibrium composition at the interface of the precipitate. Eqs. (9) and (11) express the dependence of the concentration profile around the precipitate on the mechanical state of the matrix/precipitate system for different set of boundary conditions. While Eq. (9) describes the concentration profile around a static precipitate with a single boundary condition set at far field $(r \to \infty)$ , Eq. (11) describes a more realistic concentration profile around a self-stressed precipitate with two boundary conditions at the precipitate interface $(r=R)$ and $r \to \infty$ . This solution contains two correction terms due to the chemo-mechanical coupling $(-g_{0} \varkappa(\frac{R}{r})^{6}+g_{0} \varkappa \frac{R}{r})$ due to the chemo-mechanical coupling effect, one of which scales $\propto \frac{1}{r^{6}}$ , similar to the elastic energy density around the precipitate. Both terms are proportional to the coupling factor, $\varkappa$ , and its sign, but independent of the sign of the transformation strain, $\epsilon_{p}^{*}$ . The equilibrium composition at the interface $(c(r=R)=c_{R})$ is determined by the Gibbs-Thomson effect, i.e. the curvature of the precipitate. In the presence of elasticity $c_{R}$ will be also influenced by elastic energy as discussed by different people (see for instance [62,63]). This is however not considered here as for the sake of benchmarking Eq. (9) is used here. For more details see [28].

### 2.2. Multi-phase-field model

In the multi-phase-field concept [13,15,64], the interface free energy

$$
f_{\text {intf }}=\sum_{\alpha \neq \beta}^{N_{\phi}} \frac{4 \gamma}{\eta}\left[-\frac{\eta^{2}}{\pi^{2}} \nabla \phi_{\alpha} \cdot \nabla \phi_{\beta}+\phi_{\alpha} \phi_{\beta}\right]
\tag{12}
$$

is expressed in pairwise terms where $\phi_{\alpha} \in[0,1]$ is the order parameter for phase $\alpha$ . Here $\gamma$ is the interface energy, assumed to be isotropic, andη is the interface width, a model-related parameter. Through their variation, the phase-fields implicitly represent the microstructure in terms of the bulk, interfaces and junctions. Any other energy density is a weighted function of the phase-fields, $\{\phi\}$ . The non-integer values of $\phi_{\alpha}$ correspond to the diffuse interface volume. Other free energy densities follow as

$$
f_{\text {chem }}=\sum_{\alpha=1}^{N_{\phi}} \phi_{\alpha} f_{\text {chem }, \alpha}\left(c_{\alpha}\right)+\lambda\left[c-\sum_{\alpha=1}^{N}\left(\phi_{\alpha} c[\alpha]\right)\right]
\tag{13}
$$

and

$$
f_{\text {elas }}=\frac{1}{2} \sum_{\alpha=1}^{N_{\phi}} \phi_{\alpha} \epsilon_{\text {elas }, \alpha}^{i j} C_{\alpha}^{i j k l} \epsilon_{\text {elas }, \alpha}^{k l}
\tag{14}
$$

with chemical free energies $f_{chem, \alpha}(c_{\alpha})$ of the individual phases and $\lambda$ as a Lagrange multiplier conserving the mass balance for each element, $c=\sum_{\alpha=1}^{N} \phi_{\alpha} c_{\alpha}$ . Here $\epsilon_{elas }^{i j}=\epsilon_{tot }^{i j}-\epsilon_{s}^{i j}$ and $C_{\alpha}^{i j k l}$ are elastic strain and elastic constants of phase $\alpha$ , respectively. Inserting the free energy densities into Eq. (2) results in the kinetic equation for the phase-fields

$$
\dot{\phi}_{\alpha}=\frac{L}{N_{\phi}} \sum_{\beta=1}^{N_{\phi}}\left[\sum_{\theta=1 \neq \beta}^{N_{\phi}}\left[\gamma_{\beta \theta}-\gamma_{\alpha \theta}\right]\left[\nabla^{2} \phi_{\theta}+\frac{\pi^{2}}{\eta^{2}} \phi_{\theta}\right]+\frac{\pi^{2}}{8 \eta} \Delta G_{\alpha \beta}\right]
\tag{15}
$$

where $\Delta G_{\alpha \beta}=\Delta G_{\text {chem, } \alpha \beta}+\Delta G_{\text {elas, } \alpha \beta}$ is the sum of the chemical and mechanical driving forces between the two $\alpha$ and $\beta$ domains. The chemical part of the driving force (between the precipitate and matrix phase) is simplified, by using a piecewise linearised approximation of the phase-diagram, as

$$
\Delta G_{\text {chem, } \alpha \beta}=m \Delta s_{0}\left(c-c_{\text {eq }}\right)
\tag{16}
$$

in which $m$ is the slope of the line separating the matrix and two-phase regions in T-c diagram, $\Delta s_{0}$ is the entropy of formation of the precipitate phase and $c_{\text {eq }}$ is the equilibrium matrix composition for a given temperature. In order to determine the mechanical driving force $\Delta G_{\text {elas, } \alpha \beta}$ an appropriate homogenization scheme shall be applied across the interface volume as described in the following section.

### 2.2.1. Homogenization scheme and driving forces

In order to deal with diffuse interface (phase-field) problem used in the OpenPhase software, it is necessary to deal with the phase mixture at the interface region. This is done by considering a homogenization scheme. The Reuss homogenization scheme is applied that assumes equal stress among the phases in contact $\left(\sigma^{i j}=\sigma_{\alpha}^{i j}=\sigma_{\beta}^{i j}\right)$ while partitioning into different individual strains in each phase $\epsilon_{\mathrm{tot}, \alpha}^{i j} \neq \epsilon_{\mathrm{tot}, \beta}^{i j}$ [64,29]

$$
\epsilon_{\mathrm{tot}}^{i j}=\sum_{\alpha=1}^{N} \phi_{\alpha} \epsilon_{\mathrm{tot}, \alpha}^{i j}
\tag{17}
$$

Separating the elastic strain from the eigenstrain contribution and taking the chemo-mechanical coupling $(\kappa \neq 0)$ into account

$$
\epsilon_{\mathrm{elas}}^{i j}=\sum_{\alpha=1}^{N} \phi_{\alpha} S_{\alpha}^{i j k l}(c) \sigma^{i j}
\tag{18}
$$

in which $S_{\alpha}^{i j k l}(c)=\left(C_{0, \alpha}^{i j k l}\left(1+\kappa_{\alpha} \Delta c\right)\right)^{-1}$ and

$$
\epsilon_{*}^{i j}=\sum_{\alpha=1}^{N} \phi_{\alpha} \epsilon_{\alpha, *}^{i j}
\tag{19}
$$

the compliance of effective elastic constants in the interface will be

$$
S_{\text {eff }}^{i j k l}=\sum_{\alpha=1}^{N} \phi_{\alpha} S_{\alpha}^{i j k l}(c)=\sum_{\alpha=1}^{N} \phi_{\alpha}\left(C_{0, \alpha}^{i j k l}\left(1+\kappa_{\alpha} \Delta c\right)\right)^{-1}
\tag{20}
$$

and the stress at the homogenized interface becomes

$$
\sigma^{i j}=C_{\text {eff }}^{i j k l}\left(\epsilon_{\text {tot }}^{k l}-\epsilon_{*}^{k l}\right)
\tag{21}
$$

where

$$
C_{\text {eff }}^{i j k l}=\left(S_{\text {eff }}^{i j k l}\right)^{-1}=\left(\sum_{\alpha=1}^{N} \phi_{\alpha}\left(C_{0, \alpha}^{i j k l}\left(1+\kappa_{\alpha} \Delta c\right)\right)^{-1}\right)^{-1}
\tag{22}
$$

and finally, the elastic energy density using the Einstein summation notation is

$$
f_{\text {elas }}=\frac{1}{2} \epsilon_{\text {elas }}^{i j} C_{\text {eff }}^{i j k l} \epsilon_{\text {eff }}^{k l}=\sum_{\alpha=1}^{N} \phi_{\alpha} f_{\text {elas, } \alpha}
\tag{23}
$$

The elastic driving force, $\Delta G_{\text {elas }, \alpha \beta}=-\left(\frac{\partial}{\partial \phi_{\alpha}}-\frac{\partial}{\partial \phi_{\beta}}\right) f_{\text {elas }}$, that adds to the chemical driving force in the phase-field Eq. (15), and the chemo-mechanical potential, $\frac{\partial f_{\text {elas }}}{\partial c}$, at the interface are obtained using Eq. (23) (Einstein summation):

$$
\Delta G_{\text {elas }, \alpha \beta}=\left(\epsilon_{\text {tot }}^{i j}-\epsilon_{*}^{i j}\right) C_{\text {eff }}^{i j k l}\left[\left(\epsilon_{\alpha, *}^{k l}-\epsilon_{\beta, *}^{k l}\right)+\frac{1}{2}\left(S_{\alpha}^{k l m n}-S_{\beta}^{k l m n}\right) C_{\text {eff }}^{m n o p}\left(\epsilon_{\text {tot }}^{o p}-\epsilon_{*}^{o p}\right)\right]
\tag{24}
$$

and

$$
\frac{\partial f_{\text {elas }}}{\partial c}=\frac{1}{2} \epsilon_{\text {elas }}^{i j} \frac{\partial C_{\text {eff }}^{i j k l}}{\partial c} \epsilon_{\text {elas }}^{k l}
\tag{25}
$$

with

$$
\frac{\partial C_{\text {eff }}^{i j k l}}{\partial c}=-C_{\text {eff }}^{i j m n}\left(\sum_{\alpha=1}^{N}\left(\phi_{\alpha} S_{\text {eff }, \alpha}^{m n o p}\left(-\kappa_{\alpha} C_{0, \alpha}^{o p q r}\right) S_{\text {eff }, \alpha}^{q r s t}\right)\right) C_{\text {eff }}^{s t k l}
\tag{26}
$$

### 2.3. Chemo-mechanical model in a large-strain kinematic framework

In order to implement the chemo-mechanical coupling in the finite-strain framework of DAMASK, it is necessary to work with the deformation gradient, $F^{i j}$, that is multiplicatively split into elastic components, $F_{\text {elas }}^{i j}$, and eigenstrain components, $F_{*}^{i j}$, as outlined in [65,66],

$$
F^{i j}=F_{\text {elas }}^{i k} F_{*}^{k j}
\tag{27}
$$

The elastic Green-Lagrange strain resulting from this decomposition is given by:

$$
\epsilon_{\text {elas }}^{i j}=\frac{1}{2} F_{*}^{i k}\left(F_{\text {elas }}^{k l} F_{\text {elas }}^{l m}-\delta^{k m}\right) F_{*}^{m j},
\tag{28}
$$

and the resulting stress is given by:

$$
\sigma^{i j}=C^{i j k l}(c) \epsilon_{\text {elas }}^{k l}
\tag{29}
$$

with the concentration dependent elastic stiffness, $C^{i j k l}(c)$ as presented and discussed above. The elastic energy can be expressed in its common form, $f_{\text {elas }}=\frac{1}{2} \epsilon_{\text {elas }}^{i j} C^{i j k l}(c) \epsilon_{\text {elas }}^{k l}$, and for the chemical free energy an ideal solution model is considered

$$
\omega f_{\text {chem }}=E_{c} c+k_{\mathrm{B}} T[c \ln (c)+(1-c) \ln (1-c)] .
\tag{30}
$$

with $E_{c}$ the energy of reference pure components and a volume-like parameter $\omega$. It is to note that the precipitate phase is a stoichiometric phase. Diffusional transport of $\mathrm{Li}$ in the $\mathrm{Al}$ (in the matrix) crystal follows Eq. (3). The solute flux is described by Eq. (6) in which $\frac{\partial F}{\partial c}$ is the diffusional potential. Inserting Eq. (30), the chemical part of the diffusional potential will be

$$
\omega \frac{\partial f_{\text {chem }}}{\partial c}=E+k_{\mathrm{B}} T \ln \frac{c}{1-c}
\tag{31}
$$

that results in a different flux than Fick's first law. In the following simulations, however, it is shown that this difference has a minor effect on the results. The mechanical part of the potential $\xi$ results in the same formulation as presented in Section 2.

Here we define a new quantity, $\xi$, equivalent to the diffusional potential, as

$$
\xi=\frac{\partial f_{\text {chem }}}{\partial c}+\frac{\partial f_{\text {elas }}}{\partial c}
\tag{32}
$$

A change of variables from $c$ to $\xi$ is applied in order to obtain better numerical performance. Hence Eq. (3) is rewritten as

$$
\frac{\partial c}{\partial \xi} \dot{\xi}=\nabla \cdot M \nabla \xi
\tag{33}
$$

which is solved for $\xi$ as outlined in [67,68] Here, the following inverse relations are used

$$
c=\frac{\exp \left(\frac{1}{k_{\mathrm{B}} T}\left(\omega \xi-E-\omega \frac{\partial f_{\text {elas }}}{\partial c}\right)\right)}{1+\exp \left(\frac{1}{k_{\mathrm{B}} T}\left(\omega \xi-E-\omega \frac{\partial f_{\text {elas }}}{\partial c}\right)\right)}, \quad \text { and } \quad \frac{\partial c}{\partial \xi}=c-c^{2}
\tag{34}
$$

Note that this relation, when used in Eq. (33), is unaffected by the singularity of the diffusion potential, $\xi$, at $c=0$ and $c=1$.

### 3. Implementation

#### 3.1. OpenPhase

OpenPhase [38] is a modular C++ object-oriented open-source software developed in the Interdisciplinary Centre for Advanced Materials Simulation (ICAMS), at Ruhr-University Bochum. OpenPhase is suited for studying microstructure evolution in various multi-physics set-ups, first developed, benchmarked and used for studying grain growth, particle pinning and nanograin growth in polycrystalline materials [37]. The multi-phase-field model [13,15,64], described in Section 2.2, forms the core of this software. Separate diffusion and elasticity modules were developed to deal with the evolution of the concentration and strain/stress fields, respectively. The interface properties, homogenization schemes, thermodynamic inputs, etc. are treated as individual flexible modules that allow easy implementation of different models and constitutive laws in the software. All modules communicate with the phase-field module that resolves interface kinetics and overall evolution of the microstructure. OpenPhase benefits from a dynamic memory allocation algorithm that significantly reduces the computational costs in terms of memory usage [37]. Recent developments of OpenPhase aim at adding fluid flow and large deformation [69] frameworks as well as coupling to the existing commercial databases. OpenPhase makes use of a hybrid parallelization scheme that combines MPI and OpenMP computing and allows large-scale multiphysics simulations [39].

For the current studies in OpenPhase, a cross-linked coupling between the diffusion and elasticity modules has been introduced to account for the chemo-mechanical coupling presented in Section 2. This includes developing a composition dependent homogenization scheme, as presented in Section 2.2.1, which is required for obtaining mechanical properties and introducing the mechanically-driven part of the flux (Eq. (6)) in the diffusion formulation. For studying precipitation kinetics (Section 5.4), the elastic driving force under the chemo-mechanical coupling has been modified to include the coupling effect (Eq. (24)). We make use of a spectral iterative FFT solver in reciprocal space to solve static mechanical equilibrium (Eq. (5)). This is a modified version of the linear elastic spectral solver introduced in [70]. The input homogenized elastic constants and eigenstrains are computed in real space per each point and passed to the solver at each time step. The mechanical solutions are given once strain and stress converges below specified small thresholds values, i.e. $1.0^{-6}$ and 1 kPa, respectively. A periodic boundary condition is applied. Furthermore, in order to allow free expansion of the box, a free volume expansion condition is applied in which an average strain over the entire simulation box is computed and subtracted in all points such that the total hydrostatic stress in the system vanishes. For phase-field and diffusion solvers, a finite-difference scheme is applied.

#### 3.2. DAMASK

The Düsseldorf Advanced Material Simulation Kit (DAMASK) is a flexible and hierarchically structured multi-physics simulation tool developed as an open source project in the Microstructure Physics and Alloy Design department at the Max-Planck-Institut für Eisenforschung. It is modular in design and allows the use and straightforward implementation of different types of constitutive laws and numerical solvers. While DAMASK was primarily developed as a finite-strain crystal plasticity simulation tool, more recent developments have sought to extend its applicability to fracture, diffusion, phase transformation local dissipative heat generation and transport among other coupled multi-physical processes of interest. The material models implemented in DAMASK interface with commercial FEM solvers MSC.Marc and Abaqus, as well as in-house developed stand-alone spectral and FEM solvers, which are fully MPI-parallelized and built upon PETSc [71] as the numerical engine.

The field equations implemented in DAMASK are solved using fully implicit time-stepping, and strong coupling between multiple fields is achieved in a self-consistent manner through an iterative procedure. The advantage of such a coupling approach is that the solution scheme of each field can be described independently. The solution procedure is detailed in [68]. The available mechanical and solute transport modules are used to study chemo-mechanical coupling in the present work. A large strain formulation of the FFT-based spectral method [72,73] with modified convolution (Gamma) operator [68] is implemented in DAMASK and used to solve for mechanical equilibrium Eq. (7). A finite-difference method is used to solve for solute diffusion Eq. (3). Periodic boundary conditions are applied in which the average deformation gradient, or complimentarily the average stress, is constrained to a prescribed value. For a complete reference to the DAMASK internals we refer to [41].

#### 3.3. Hybrid OpenPhase-DAMASK implementation

In order to present an application of the current benchmark studies to studying kinetics of precipitation in the presence of chemo-mechanical coupling (Section 5.4), OpenPhase and a hybrid OpenPhase-DAMASK implementation are used. In the hybrid implementation, we utilize the DAMASK for solving static mechanical equilibrium (Eq. (5)) and the OpenPhase finite difference solver for homogenization and solving the diffusion and phase-field equations. While in OpenPhase an elastic spectral solver suited for small deformations is implemented, the spectral solver in DAMASK is based on the finite strain framework [74,72,73] that makes it suited for studying large deformations as presented in [75,53]. It calculates the solution of all 9 components of the deformation gradient $F^{ij}$ to the static equilibrium equation

$$
\nabla^i \cdot P^{ij}(F^{ij}, \{\phi\}, \{c\}) = \mathbf{0} \tag{35}
$$

where $P^{ij}$ is the first Piola-Kirchhoff stress tensor component. The constitutive law $P^{ij}(F^{ij})$ is a function of phase-field parameters $\{\phi\}$ and chemical compositions $\{c\}$. These input values are computed in OpenPhase based on the homogenization scheme described in Section 2.2.1 and provided to the DAMASK for obtaining mechanical equilibrium. Once the convergence of stress equilibrium is achieved, the stress and strain fields are returned to OpenPhase to be used for computing interface kinetics. Fig. 1 illustrates the numerical algorithms of both solvers. The homogenized field variables effective stiffness $C_{\text{eff}}^{ijkl}$, stress $\sigma^{ij}$, and phase fields $\phi$ are generated in OpenPhase and synchronized at each time to be used in DAMASK mechanical solver. In the phase interior, the constitutive equations introduced in Section 2.3 are used to calculate the stress response $P(F^{ij})$ under given boundary conditions $\overline{P^{ij}} = P_{\text{BC}}^{ij}$ and $\overline{F^{ij}} = F_{\text{BC}}^{ij}$. At the interfacial region where $\phi$ falls between 0 and 1, linear interpolation is performed on the eigenstrain tensor vs. phase fraction

$$
F_*^{ij} = \sum_\alpha F_{*,\alpha}^{ij} \phi_\alpha \tag{36}
$$

where the eigenstrain of the $\alpha$-th phase, $F_{*,\alpha}^{ij}$, is equivalent to $(\epsilon_{*,\alpha}^{ij} + 1)$ but expressed as a deformation gradient tensor in the finite strain framework. With this treatment, we can bypass the built-in multi-crystalline homogenization scheme of DAMASK which does not usually incorporate diffusive interfaces. The reader is referred to [68] for a comprehensive discussion of the spectral solver methods used in DAMASK and to [75] for more details about the hybrid OpenPhase-DAMASK implementation.

While DAMASK natively solves the first Piola-Kirchhoff stress $P^{ij}$, it is translated into the second Piola-Kirchhoff stress $(F^{ij})^{-1}P^{ij}$ and copied to OpenPhase as $\sigma^{ij}$ – that is, the orthogonal grid of OpenPhase is treated as the undeformed (initial) configuration in DAMASK. The effective stiffness tensor $C_{\text{eff}}^{ijkl}(\phi, c)$ is a rank 4 tensor field defined by Eq. (22). Since there exists no inherent mapping between the deformation gradient $F^{ij}$ and the symmetric strain tensor $\epsilon^{ij}$ of OpenPhase (Eq. (8)),

![](./images/812844894837014530_1.jpg)

$\epsilon_{\text{elas}}^{ij}$ is recomputed from the symmetric stress tensor $\sigma^{ij}$ and $C_{\text{eff}}^{ijkl}$ using Eq. (28).

## 4. Benchmark set-ups

The OpenPhase and DAMASK software packages as well as an OpenPhase-DAMASK hybrid implementation are employed to solve the benchmark problems. First, diffusion and mechanical solvers of each software are benchmarked against analytical solutions for the same set-up. Thereafter, the chemo-mechanical model presented above is benchmarked. The effect of chemo-mechanical coupling on the thermodynamics and kinetics of precipitation is examined as well. In this section, the set-up of the benchmark problems are described.

The following input parameters are used in all simulations: The time step $dt$ and grid space $dx$ are chosen as 1 s and 3 nm, respectively. The simulations are performed at 473 K where Li in Al has a diffusion coefficient of $D = 1.2 \times 10^{-18}\ \text{m}^2\text{s}^{-1}$ and an atomic mobility of $M = D/RT = 3.4 \times 10^{-22}\ \text{mol}\ \text{m}^2\ \text{J}^{-1}\text{s}^{-1}$ [76]. The simulation boxes are $(64\ \text{dx})^3$ unless mentioned otherwise in the following. All simulations are conducted using periodic boundary conditions. The interface width (used in OpenPhase) is set to 5 dx. The interface between matrix and precipitate phase is coherent and has an energy of $0.014\ \text{J}\ \text{m}^{-2}$ [77] and has a volumetric misfit $-0.975\%$. $\Delta s_0 = -9.7315 \times 10^5\ \text{J}\text{K}^{-1}\ \text{m}^{-3}$ [78] is the entropy of formation of the precipitate phase and $c_{\text{eq}} = 6.67$ at. % Li is the equilibrium matrix composition at 473 K for a flat interface. The precipitate is a stoichiometric phase with 25 at.% Li composition. Further inputs or set-up parameters are mentioned in the corresponding sections.

### 4.1. Diffusion couple

To benchmark different models and diffusion solvers implemented in the OpenPhase and DAMASK packages, the evolution of the concentration profile in a quasi one-dimensional diffusion couple is investigated. Mechanics and phase transformations are not considered. The initial Li concentration profile is a square wave with a lower value of $c_{\text{l}} = 8$ at. % and a higher value of $c_{\text{h}} = 10$ at. %. The wave length is set to $2L = 64$ dx and the molar volume is $V_m = 1 \times 10^{-5}\ \text{m}^3$. The results are discussed in Section 5.1.

### 4.2. Eshelby inclusion test

The underlying mechanical solvers in OpenPhase and DAMASK are benchmarked by evaluating the stress profiles around a single self-stressed precipitate in conjunction with a linear elastic constitutive law, i.e. Eshelby's inclusion set up. Diffusion and phase transformations are not considered. In this classical benchmark problem, a spherical precipitate of radius 8 dx (box size: $96^3$ grid cells) with an volumetric eigenstrain $\epsilon^* (-1\%, +1\%)$ is introduced in the centre of the simulation box. Isotropic and homogeneous linear elastic properties for the matrix and precipitate are used: $C_{11} = 100$ GPa, $C_{12} = 50$ GPa, $C_{44} = 25$ GPa. For this case an analytical solution given by Eshelby [79] is used for comparing our results. The results are discussed in Section 5.2.

### 4.3. Chemo-mechanical coupling effect

In order to benchmark the chemo-mechanical coupling model and its implementations, the evolution of the concentration profile around a self-stressed static precipitate is studied. A single static $\delta'$ precipitate

<table>
<caption>Table 1
Elastic constants $C_{ij}$ for the matrix and precipitate phase.</caption>
<thead>
<tr>
<th>
</th>
<th>
Matrix
</th>
<th>
Precipitate
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
$C_{11}$
</td>
<td>
107.11 GPa
</td>
<td>
139.8 GPa
</td>
</tr>
<tr>
<td>
$C_{12}$
</td>
<td>
62.86 GPa
</td>
<td>
33.7 GPa
</td>
</tr>
<tr>
<td>
$C_{12}$
</td>
<td>
28.47 GPa
</td>
<td>
40.8 GPa
</td>
</tr>
</tbody>
</table>

with different specific radii and coupling values $\varkappa$ is placed in a matrix with a flat concentration profile. In this benchmark we solve for mechanical equilibrium, Eq. (7) coupled with chemical diffusion, i.e. Eq. (3) (OpenPhase) or Eq. (33) (DAMASK). Phase transformations are not considered. In OpenPhase, this is obtained by deactivating interface kinetics ($L = 0$) and reducing interface width (OpenPhase) to 1 grid cell for the purposes of comparison. Realistic elastic constants of precipitate [80] and matrix (pure aluminium) [81], see Table 1, and isotropic coupling values for the matrix phase are set to Table 2. The Li matrix concentrations as well as the precipitate radii are set to values using results from an equilibrium calculation (Table 2). The homogenization of the elastic coefficients (as presented in Section 2.2.1) for the diffuse interface model in the OpenPhase is obtained in each step.

### 4.4. Chemo-mechanical coupling effect during growth

This final benchmark is concerned with the growth of a single $\delta'$ precipitate. Besides the chemo-mechanical coupling, the growth kinetics must account for elastic and chemical driving forces as well as the interfacial energy contribution as presented in Section 2. As DAMASK does not have the ability to model phase transformation yet, this is studied using the OpenPhase software. However, different solvers for mechanical equilibrium, i.e. the OpenPhase and the DAMASK spectral solvers, are used. For the latter case, a hybrid OpenPhase–DAMASK implementation is employed (Section 3.3). In the OpenPhase, the full problem using Eqs. (3), (7) and (15)including homogenization and calculation of driving forces is solved. In these simulations, a single $\delta'$ (Al₃Li) nucleus with a negligible size is planted into the aluminium matrix of concentration 9 at1%. The precipitate grows spherically and reaches its thermodynamic equilibrium volume. Here the Gibbs-Thompson effect is naturally taken into account by the phase-field governing equations. The kinetics of growth and the evolution of concentration and stress within the simulation box are discussed in Section 5.4.

## 5. Results and discussions

In this section, the reference numerical solutions obtained by OpenPhase and DAMASK software packages are presented. The benchmark problems are discussed in the same order as described in Section 4. A comparison to analytical solutions is presented and discussed where applicable. For pure diffusion problem (Section 5.1) a time-dependent analytical solution exists that is used for the comparison. For the Eshelby inclusion test (Section 5.2) and chemo-mechanical coupling benchmark (Section 5.3), where equilibrium fields (around the precipitate) were analysed, we employ the $L^{2}$-norm [82] to quantify the difference between the numerical and the analytical solutions. Here the relative difference $\zeta$ between analytical $q_{\text{ref}}(x)$ and numerical $q_{\text{num}}(x)$ solutions, is computed as

$$
\zeta=\frac{\parallel q_{\text{ref}}-q_{\text{num}}\parallel_{2}}{\parallel q_{\text{ref}}\parallel_{2}}=\sqrt{\frac{\int\left(q_{\text{ref}}-q_{\text{num}}\right)^{2}dx}{\int q_{\text{ref}}^{2}dx}}
\tag{37}
$$

where the integration is performed over the domain shown in the corresponding figures. The $L^{2}$-norm is applied to examine the stress and the concentration fields, in the Eshelby inclusion test and the chemo-mechanical coupling benchmark, respectively. These results are presented in Tables 3 and 4 and accordingly discussed in the text.

<table>
<caption>Table 2
Initial radii of the precipitate and matrix concentrations for different coupling modes.</caption>
<thead>
<tr>
<th>
Coupling value $\varkappa$
</th>
<th>
Initial radius
</th>
<th>
Initial Li concentration in the matrix
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
0.00 at.%-1
</td>
<td>
19.43 dx
</td>
<td>
6.876 at.%
</td>
</tr>
<tr>
<td>
0.01 at.%-1
</td>
<td>
19.03 dx
</td>
<td>
7.021 at.%
</td>
</tr>
<tr>
<td>
0.04 at.%-1
</td>
<td>
17.71 dx
</td>
<td>
7.440 at.%
</td>
</tr>
</tbody>
</table>

### 5.1. Diffusion couple

The diffusion models implemented in the two software packages differ slightly, as outlined in Sections 2.2 and 2.3. In OpenPhase, Fick’s laws are implemented in a form where the diffusion coefficient $D$ is assumed to be constant. In contrast, the DAMASK implementation treats the diffusion coefficient to depend on the local concentration in the form $M\frac{\partial^{2}f_{\text{chem}}}{\partial c^{2}}$ in which $M$ is a constant mobility factor. With a constant diffusion coefficient $D$ (i.e. the OpenPhase model), the diffusion benchmark problem can be described in terms of a parabolic partial differential equation (PDE), $\dot{c} = D\nabla^{2}c$ for a quasi one-dimensional situation. The solution of this equation is given as:

$$
c\left(x,t\right)=\frac{c_{\text{h}}+c_{\text{l}}}{2}-\frac{2\left(c_{\text{h}}-c_{\text{l}}\right)}{\pi}\sum_{m=1}^{\infty}\left(\frac{\left(-1\right)^{m}}{2m-1}\cos\left(wx\right)\exp\left(-Dt\omega^{2}\right)\right)
\tag{38}
$$

for periodic boundary conditions on domain $-L < x < L$, $c(x, t = 0) = c_{\text{h}}$ on$-L/2 < x < L/2$, elsecₗ and $\omega = {\pi{({2m - 1})}}/L$. In the following this analytic solution, shifted by $L/2$ to match the benchmark setup, is used as a reference result.

The temporal concentration evolution for the diffusion couple simulation is plotted in Fig. 2a (OpenPhase: black lines, DAMASK: green lines and analytical solution: red lines) and the maximum and minimum concentration values are compared in Fig. 2b. The results show the expected behaviour of the diffusion equation, i.e. an exponential decay in time and smoothing due to the preferred vanishing of steep gradients. After 5000 s, no difference to the solution for infinite time, i.e. a flat profile at the average concentration $(c_{\text{h}} + c_{\text{l}})/2 = 9$ at. %, is visible any more. Small quantitative differences between the two numerical solutions, which can be attributed to the model assumptions, are observed (see Fig. 2b) while the qualitative behavior is matched. More specifically, the two transport models differ in the form of the resulting thermodynamic factor $\frac{\partial\xi}{\partial c}$ which relates the solute mobility, $M$, to the diffusion coefficient, $D$. The form of the chemical free energy used in DAMASK, Eq. (30), can result in a composition-dependent $D$ which is assumed to be constant in OpenPhase. A perfect match between the semi-analytic benchmark expression and the OpenPhase result is hence seen, while in comparison the DAMASK model predicts a faster diffusion rate for smaller solute concentrations. From Fig. 2b this effect is hardly seen but Fig. 2b reveals that the sink (minimum) approaches the average value slightly faster the source (maximum).

### 5.2. Eshelby inclusion test

As discussed previously, the formulation of static mechanical equilibrium in OpenPhase and DAMASK is based on the same elliptic PDE. Moreover, a similar, spectral-based numerical solution scheme is employed. However, the description of the interface between two phases is different as OpenPhase uses—typical for phase-field models—a diffuse interface model with a homogenization scheme described in Section 2.2.1 while DAMASK has a sharp interface model implemented. The results obtained from the two software packages for Eshelby’s inclusion problem are compared against the analytical solution for the case of infinitesimal strains which assumes a sharp interface between matrix and inclusion. For a single isotropic inclusion with radius $R$ in an

![](./images/812844894837014530_2.jpg)

Fig. 2. Diffusion couple concentration evolution with 8 at.% Li and 10 at.% Li for different time steps (after 0 (initial), 500, 1000, 2000 and 5000 s) performed with OpenPhase (black line) and DAMASK (green line) in comparison with the analytical solution (red line). DAMASK results are mirrored for comparison. (b) The maximum and minimum values of the concentration profile (black dots: OpenPhase, green crosses: DAMASK and red lines: analytical solution) are compared versus analytical solution. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

isotropic matrix:

$$
\sigma_{xx}=-\frac{2}{3} \epsilon^{*}\left(C_{11}+2 C_{12}\right) \frac{1-2 \nu}{1-\nu}\left(\frac{r}{R}\right)^{3}
\tag{39}
$$

$$
\sigma_{zz}=-\frac{1}{2} \sigma_{xx}=\frac{1}{3} \epsilon^{*}\left(C_{11}+2 C_{12}\right) \frac{1-2 \nu}{1-\nu}\left(\frac{r}{R}\right)^{3}.
\tag{40}
$$

Fig. 3a and b show the stress profiles plotted along the line starting from the centre of the precipitate for positive $(+1 \%)$ and negative $(-1 \%)$ eigenstrains, $\epsilon^{*}$, respectively. $\nu$ is the Poisson's ratio. $r \geqslant R$ corresponds to the region outside of the precipitate (matrix). A jump in the stress profile at the interface between the pre-strained precipitate and the adjacent matrix is observed for the stress component perpendicular to the interface, i.e. parallel to the considered line $(\sigma_{zz})$ while the stress for components perpendicular (here shown: $\sigma_{xx}$) decays smoothly. The sharp and discontinuous profile obtained from DAMASK (green lines) for $\sigma_{zz}$ matches the sharp transition of the analytical solution (red lines) except that the jump is smeared out over $dx$ and the there are small fluctuations in the precipitate where the stress values should remain constant.

The first observation, viz. the linear approximation of the interface, is a consequence of the discretization procedure in which values are only defined at discrete points and the interface is implicitly modeled with its position assumed to be at half-way between the grid points of different phases. In the given situation this distance amounts to $dx/2$, but for the approximation of curved boundaries on a regular grid it can reach values of $dx/\sqrt{2}$. For this reason the use of a high spatial resolution is required to avoid numerical artifacts. The second observation, the oscillations, are a consequence of the stress and strain jumps at the sharp phase boundary that are related to Gibbs phenomenon [83,84] and the approximation of the curved interface by a step function. As a result, an entirely constant stress value in the vicinity of a jump is not achieved with the sharp interface model of DAMASK even

![](./images/812844894837014530_3.jpg)

Fig. 3. Stress (component normal to the interface, $\sigma_{xx}$: dashed lines. Component perpendicular to the interface, $\sigma_{zz}$: dash-dot lines) distribution across half of the simulation box (a) with $\epsilon^{*}=+1\%$ and (b) with $\epsilon^{*}=-1\%$ (black lines: OpenPhase, green lines: DAMASK, red lines: analytic solution, dashed grey lines: interface region between matrix and precipitate (P)). $R_p$ is the precipitate radius. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

<table><caption>Table 3
$L^2$-norm for the numerical and analytical solutions for stress fields (Fig. 3).</caption>
<thead>
<tr>
<th>Field variable</th>
<th>Condition</th>
<th>OpenPhase vs. Analytical</th>
<th>DAMASK vs. Analytical</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\sigma_{xx}$</td>
<td>$\epsilon^* = +1$</td>
<td>5%</td>
<td>6%</td>
</tr>
<tr>
<td>$\sigma_{zz}$</td>
<td>$\epsilon^* = +1$</td>
<td>28%</td>
<td>30%</td>
</tr>
<tr>
<td>$\sigma_{xx}$</td>
<td>$\epsilon^* = -1$</td>
<td>5%</td>
<td>6%</td>
</tr>
<tr>
<td>$\sigma_{zz}$</td>
<td>$\epsilon^* = -1$</td>
<td>28%</td>
<td>30%</td>
</tr>
</tbody>
</table>

though the use of a modified convolution operator can mitigate such effects significantly [85–87,68]. In contrast, OpenPhase's model (black lines) gives a rather smooth transition across the interface. This is due to the diffuse phase-field interface used in OpenPhase, which allows for a smooth approximation of the sphere if the boundary is assumed to be located at the position where the order parameters have the same value, i.e. 0.5 for the case of a binary system as in the given case. In this case a Reuss homogenization scheme has been implemented as described in Section 2.2.1, that is a necessary step in order to incorporate elasticity in the kinetic diffuse interface-models. Despite these deviations, a close agreement is obtained between the results obtained by the OpenPhase and DAMASK software packages and the analytical results (red lines) for the whole profile of $\sigma_{xx}$ and away from the interface also for $\sigma_{zz}$. Outside the interface, the maximum deviation in the stress components is found to be below 1%. The $L^2$-norm values (Table 3) indicate a total 5 (6) and 28 (30)% deviations from the analytical solutions for the OpenPhase (DAMASK) for the normal ($\sigma_{xx}$) and tangential ($\sigma_{zz}$) stress component, respectively. It is to note the a 30% deviation given by the $L^2$-norm corresponds to much smaller deviation per point, as it can be seen in Fig. 3.

### 5.3. Chemo-mechanical coupling effect

The good agreement between the numerical and analytical solutions for both diffusion and mechanical solvers allow implementation and investigation of chemo-mechanical coupling effect that is discussed in this section. In the presence of the chemo-mechanical coupling, the solute around a self-stressed precipitate must redistribute such that the

![](./images/812844894837014530_4.jpg)

Fig. 4. Concentration distribution balancing at the matrix-precipitate interface for (a) $\varkappa = 0.01$ at. $\%^{-1}$ and (b) $\varkappa = 0.04$ at. $\%^{-1}$ for different time steps and solvers. Figures (c) and (d) show the final equilibrium states using $\varkappa = 0.01$ at. $\%^{-1}$ and $\varkappa = 0.04$ at. $\%^{-1}$, respectively. $R_p$ is the precipitate radius.

**Table 4**
$L^2$-norm for the numerical and analytical solutions for the concentration fields in the presence of chemo-mechanical coupling (Fig. 4).

| Field    | Condition                          | OpenPhase vs. Analytical | DAMASK vs. Analytical |
|----------|------------------------------------|--------------------------|-----------------------|
| $c/c_{\text{eq}}$ | $\varkappa=0.01$ at.%$^{-1}$, final state | 1%                       | 2%                    |
| $c/c_{\text{eq}}$ | $\varkappa=0.04$ at.%$^{-1}$, final state | 4%                       | 9%                    |

total energy in the system, i.e. the sum of chemical and mechanical energies, minimizes. The effect of chemo-mechanical coupling on the concentration profile around a precipitate was theoretically discussed in Section 2.1. In order to benchmark the chemo-mechanical coupling effect, first we study a static precipitate: Initially, a single spherical $\delta'$ precipitate in contact with a flat (constant) solute concentration profile in the matrix is considered. While the precipitate is frozen, the evolution of the concentration profile within the matrix was studied. In this case, the effect of interface energy as a boundary condition is neglected and we apply Eq. (9) to compare the numerical solutions for the concentration field around the precipitate. The temporal evolution of concentration field around the static precipitate, obtained by the OpenPhase and DAMASK, are shown in Fig. 4a and b. Two cases using $\varkappa=0.01$ at. $\%^{-1}$ and $\varkappa=0.04$ at. $\%^{-1}$ are considered, respectively.

The simulations show that the solute starts to diffuse away from the precipitate and the matrix in the vicinity of the precipitate is depleted such that the stiffness and consequently the elastic energy in the system is reduced. As a result, the solute piles up in a distance from the precipitate and then starts to redistribute further after approximately 50 s. While the reduction in the total elastic energy drives the solute away from the precipitate, the resulting spatial concentration gradient around the precipitate generates a solute flux in the opposite direction, i.e. towards the precipitate. Thus the final equilibrium concentration profile is a result of balancing these two fluxes. For a static precipitate, the equilibrium concentration profiles are plotted in Fig. 4c and d. The $L^2$-norm values listed in Table 4 compare the numerical and analytical solutions for the final concentration profiles. A good agreement has been obtained between the numerical simulations and the analytical solution, Eq. (9). The results from the DAMASK software show slightly larger deviations that is due to the grid resolution and the sharp interface mechanical solution applied in this software.

The results show that a higher coupling factor $\varkappa$ generates a higher chemo-mechanical driving force which results in a faster transport and greater solute depletion around the precipitate. This is in agreement with Eqs. (9) and (11), where the variation due to the chemo-mechanical coupling is proportional to the coupling factor, $\varkappa$. The $L^2$-norm analysis shows that for a stronger coupling, i.e. larger $\varkappa$ values, the deviation from the analytical solution becomes larger proportional to the coupling factor. The difference between the solutions obtained by OpenPhase and DAMASK is partially due to the difference of the diffusion solvers as discussed in Section 5.1. Nevertheless, the difference between the OpenPhase and DAMASK solutions is less than 5%. The current results validate the numerical implementations of the chemo-mechanical coupling phenomena in the OpenPhase and DAMASK.

### 5.4. Chemo-mechanical coupling effect during precipitation growth

The direct application of the current benchmark solutions is addressing growth and ripening of precipitates in different chemo-mechanical coupling conditions. This is demonstrated here by studying the growth of a single precipitate in the presence of the chemo-mechanical coupling. OpenPhase and the OpenPhase-DAMASK hybrid kinetic simulations are compared against each other where in the OpenPhase-DAMASK hybrid simulations, the OpenPhase mechanical solver was replaced with DAMASK's mechanical solver, as described in Section 3.3.

Previous studies have shown that the chemo-mechanical coupling may strongly influence the kinetics of precipitation as well as their morphology and spatial arrangement [27-29]. Fig. 5a shows the volume fraction of a single $\delta'$ precipitate during the growth and at the equilibrium state in the presence of chemo-mechanical coupling. The results show that the thermodynamic equilibrium volume fraction of the precipitate is reduced in the presence of chemo-mechanical coupling. Due to the same effect, the equilibrium concentration of the matrix far from the precipitate increases as observed in Fig. 5b. This effect of chemo-mechanical coupling is similar to the Gibbs-Thomson effect on the solute partitioning between the coexisting phases.

Furthermore, while the concentration profile around the precipitate is flat when coupling is neglected ($\varkappa=0$), a solute depletion due to the chemo-mechanical coupling ($\varkappa>0$) is observed next to the precipitate (Fig. 5b). This is a characteristic feature of the coupling referred to as strained equilibrium, where the chemical and mechanical diffusion driving forces balance [52]. For an evolving precipitate, the concentration profile around the precipitate follows Eq. (11) that takes to account the equilibrium concentration at the matrix-precipitate interface. The smooth gradients between the matrix and the precipitate phases are due to the diffuse nature of the interface in the OpenPhase simulations.

Finally, Fig. 5c and d show stresses across the precipitate after 60,000 s for different coupling factors $\varkappa$ ($\varkappa=0$: solid lines, $\varkappa=0.01$ at. $\%^{-1}$: dashed lines, $\varkappa=0.04$ at.%$^{-1}$: dash-dot lines) and solvers (OpenPhase: black lines, OpenPhase + DAMASK: blue lines). In the presence of chemo-mechanical coupling, the increase in the stiffness of the matrix retards the precipitate growth. The stresses across the precipitate (Fig. 5c and d) increase due to the changes of the elastic properties that is a result of chemo-mechanical coupling (Eq. (4)). Higher coupling values result in higher stresses in the precipitate while they decrease the absolute stresses in the matrix around the precipitate following the Eshelby solution for isotropic phases [79]. The results from OpenPhase software and OpenPhase-DAMASK hybrid simulation (using DAMASK mechanical software) are very close, indicating the validity of both mechanical solvers.

## 6. Summary and conclusions

The growing interest in conducting quantitative full-field multi-physics modelling in different branches of materials science promotes developing of standardized benchmark problems that could be readily used as 'starting points' by different communities of researchers. In this work, a set of such benchmarks was presented that concerns with precipitation in the presence of chemo-mechanical coupling. The open source OpenPhase and DAMASK software packages were used.

Starting from purely diffusional and purely mechanical benchmarks, the complexity of the problem was systematically increased to a cross-coupled chemo-mechanical problem. For the diffusion benchmark, an excellent agreement with the analytical solution was observed with a very small deviation (<0.1%). The solutions for static mechanical equilibrium were compared versus Eshelby's analytical solutions for an inclusion with $\pm1\%$ strain. The results from the diffuse interface (OpenPhase) and sharp interface (DAMASK) models were slightly different. The $L^2$-norm shows about 5% deviation from the analytical solution for the normal component of stress while about 30% in the tangential components. The point-to-point deviation, however, was smaller than 10% in all cases.

A chemo-mechanical coupling benchmark around a static precipitate was studied next, where the composition dependence of the elastic constants were considered. In the presence of the chemo-mechanical coupling the solute concentration around the precipitate has been benchmarked against the analytical solution, Eq. (9). It is found that the deviation increases as the coupling factor, $\varkappa$, increases; deviations of 1% (2%) for $\varkappa=0.01$ and 4% (9%) for $\varkappa=0.04$, respectively, were observed for OpenPhase (DAMASK). As a final application

![](./images/812844894837014530_5.jpg)

Fig. 5. (a) Precipitate volume fraction evolution, (b) equilibrium concentration profile across the precipitate, (c) $\sigma_{xx}$ and (d) $\sigma_{zz}$ across the precipitate for different coupling values ($\varkappa=0$: solid lines, $\varkappa=0.01$ at.$\%^{-1}$: dashed lines, $\varkappa=0.04$ at.$\%^{-1}$: dash-dot lines) and simulation tools (OpenPhase: black lines, OpenPhase + DAMASK hybrid: blue lines). (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

example, kinetics of a growing precipitate was investigated using OpenPhase phase-field simulations and an OpenPhase-DAMASK hybrid implementation where an excellent agreement between the two nu- merical results was obtained.

The current benchmarks are developed to serve growing researches concerning chemo-mechanical coupled problems as, for instance, the research activities in SPP1713 programme. Further benchmark pro- blems are required in this direction to include other types of coupled problems, such as electromagnetic interactions and fluid flow, that are abundantly existing in real-world systems and processes.

### Author contributions
The current work is developed in the priority programme SPP1713, initiated by German Research Foundation (DFG), where all of the au- thors are involved. RDK and IS conceived the concept of the current benchmarks. RDK and CS performed OpenPhase benchmark studies. MD and PS performed DAMASK benchmarks studies. ML performed hybrid OpenPhase-DAMASK benchmark studies. RDK, MD, CS, PS and ML wrote the manuscript. DR, IS and UP critically reviewed the manuscript. All the authors contributed to the discussions.

### Acknowledgements
Financial supports from German Research Foundation (DFG) under the projects DA 1655/1, RA 659/23, PR729/2 and SH 947/2-1 within the framework of priority program SPP1713 [56] are acknowledged. RDK also acknowledges the grant DA 1655/2-1 within the Heisenberg programme of DFG.

### References
[1] D. Keyes, L. McInnes, C. Woodward, W. Gropp, E. Myra, M. Pernice, J. Bell, J. Brown, A. Clo, J. Connors, et al., Multiphysics simulations: challenges and op- portunities, Int. J. High Perform. Comput. Appl. 27 (1) (2013) 4-83.
[2] M. Diehl, Review and outlook: mechanical, thermodynamic, and kinetic continuum modeling of metallic materials at the grain scale, MRS Commun. 7 (4) (2017) 735-746.
[3] C. Schwarze, R. DarvishiKamachali, M. Kühbach, C. Mießen, M. Tegeler, L. Barrales-Mora, I. Steinbach, G. Gottstein, Computationally efficient phase-field simulation studies using RVE sampling and statistical analysis, Comput. Mater. Sci. 147 (2018) 204-216.
[4] S.-K. Chan, Steady-state kinetics of diffusionless first order phase transformations, J.

Chem. Phys. 67 (12) (1977) 5755-5762.

[5] W.J. Boettinger, J.A. Warren, C. Beckermann, A. Karma, Phase-field simulation of solidification, Ann. Rev. Mater. Res. 32 (1) (2002) 163-194.

[6] V. Vaithyanathan, L.Q. Chen, Coarsening of ordered intermetallic precipitates with coherency stress, Acta Mater. 50 (16) (2002) 4061-4073.

[7] N. Moelans, B. Blanpain, P. Wollants, An introduction to phase-field modeling of microstructure evolution, Calphad 32 (2) (2008) 268-294, https://doi.org/10.1016/j.calphad.2007.11.003 ISSN 0364-5916.

[8] H. Emmerich, Advances of and by phase-field modelling in condensed-matter physics, Adv. Phys. 57 (1) (2008) 1-87.

[9] A. Finel, Y. LeBouar, A. Gaubert, U. Salman, Phase field methods: microstructures, mechanical properties and complexity, C.R. Phys. 11 (3-4) (2010) 245-256.

[10] G. Boussinot, Y. LeBouar, A. Finel, Phase-field simulations with inhomogeneous elasticity: comparison with an atomic-scale method and application to superalloys, Acta Mater. 58 (12) (2010) 4170-4181.

[11] P.-A. Geslin, B. Appolaire, A. Finel, A phase field model for dislocation climb, Appl. Phys. Lett. 104 (1) (2014) 011903.

[12] I. Steinbach, F. Pezzolla, B. Nestler, M. Seeßelberg, R. Prieler, G.J. Schmitz, J.L.L. Rezende, A phase field concept for multiphase systems, Physica D 94 (1996) 135-147.

[13] I. Steinbach, F. Pezzolla, A generalized field method for multiphase transformations using interface fields, Physica D 134 (4) (1999) 385-393.

[14] L.-Q. Chen, Phase-field models for microstructure evolution, Ann. Rev. Mater. Res. 32 (2002) 113-140, https://doi.org/10.1146/annurev.matsci.32.112001.132041.

[15] I. Steinbach, Phase-field models in materials science, Modell. Simul. Mater. Sci. Eng. 17 (2009) 073001.

[16] N. Provatas, K. Elder, Phase-field Methods in Materials Science and Engineering, John Wiley & Sons, 2011.

[17] A. Vondrous, M. Selzer, J. Hotzer, B. Nestler, Parallel computing for phase-field models, Int. J. High Perform. Comput. Appl. 28 (1) (2013) 61-72, https://doi.org/10.1177/1094342013490972.

[18] B. Nestler, A. Wheeler, A multi-phase-field model of eutectic and peritectic alloys: numerical simulation of growth structures, Physica D 138 (1) (2000) 114-133.

[19] M. Tegeler, G. Sutmann, A. Monas, Massively parallel multiphase field simulations, The Fourth International Conference on Parallel, Distributed, Grid and Cloud Computing for Engineering, Jülich Supercomputing Center, 2015.

[20] T. Takaki, A. Yamanaka, Y. Higa, Y. Tomita, Phase-field model during static re-crystallization based on crystal-plasticity theory, J. Comput. Aided Mater. Des. 14 (2007) 75-84.

[21] T. Takaki, Y. Hisakuni, T. Hirouchi, A. Yamanaka, Y. Tomita, Multi-phase-field simulations for dynamic recrystallization, Comput. Mater. Sci. 45 (2009) 881-888, https://doi.org/10.1016/j.commatsci.2008.12.009.

[22] R. DarvishiKamachali, S. Kim, I. Steinbach, Texture evolution in deformed AZ31 magnesium sheets: experiments and phase-field study, Comput. Mater. Sci. 104 (2015) 193-199.

[23] K. Chang, W. Feng, L.-Q. Chen, Effect of second-phase particle morphology on grain growth kinetics, Acta Mater. 57 (17) (2009) 5229-5236.

[24] M. Militzer, Phase field modeling of microstructure evolution in steels, Curr. Opin. Solid State Mater. Sci. 15 (3) (2011) 106-115.

[25] C. Schwarze, R. DarvishiKamachali, I. Steinbach, Phase-field study of zener drag and pinning of cylindrical particles in polycrystalline materials, Acta Mater. 106 (2016) 59-65.

[26] N. Zhou, C. Shen, M. Mills, Y. Wang, Large-scale three-dimensional phase field simulation of $\gamma'$-rafting and creep deformation, Phil. Mag. 90 (1-4) (2010) 405-436.

[27] R. DarvishiKamachali, E. Borukhovich, N. Hatcher, I. Steinbach, DFT-supported phase-field study on the effect of mechanically driven fluxes in $\mathrm{Ni_4Ti_3}$ precipitation, Model. Simul. Mater. Sci. Eng. 22 (2014) 034003.

[28] R. DarvishiKamachali, C. Schwarze, Inverse ripening and rearrangement of precipitates under chemomechanical coupling, Comput. Mater. Sci. 130 (2017) 292-296.

[29] C. Schwarze, A. Gupta, T. Hickel, R. DarvishiKamachali, Phase-field study of ripening and rearrangement of precipitates under chemomechanical coupling, Phys. Rev. B 95 (2017) 174101.

[30] A.M. Jokisaari, S.S. Naghavi, C. Wolverton, P.W. Voorhees, O.G. Heinonen, Predicting the morphologies of $\gamma'$ precipitates in cobalt-based superalloys, Acta Mater. 141 (2017) 273-284.

[31] S.G. Kim, D.I. Kim, W.T. Kim, Y.B. Park, Computer simulations of two-dimensional and three-dimensional ideal grain growth, Phys. Rev. E 74 (6) (2006) 061605.

[32] Y. Suwa, Y. Saito, H. Onodera, Phase-field simulation of recrystallization based on the unified subgrain growth theory, Comput. Mater. Sci. 44 (2008) 286-295, https://doi.org/10.1016/j.commatsci.2008.03.025.

[33] R. DarvishiKamachali, I. Steinbach, 3D phase-field simulation of grain growth: topological analysis versus mean-field approximations, Acta Mater. 60 (2012) 2719-2728.

[34] R. DarvishiKamachali, A. Abbondandolo, K. Siburg, I. Steinbach, Geometrical grounds of mean field solutions for normal grain growth, Acta Mater. 90 (2015) 252-258.

[35] E. Miyoshi, T. Takaki, M. Ohno, Y. Shibuta, S. Sakane, T. Shimokawabe, T. Aoki, Ultra-large-scale phase-field simulation study of ideal grain growth, NPJ Comput. Mater. 3 (1) (2017) 25.

[36] R. DarvishiKamachali, J. Hua, I. Steinbach, A. Hartmaier, Multiscale simulations on the grain growth process in nanostructured materials, Int. J. Mater. Res. 101 (2010) 1332-1338.

[37] R. DarvishiKamachali, Grain Boundary Motion in Polycrystalline Materials (PhD thesis), Ruhr-Universität Bochum, Bochum, Germany, 2013.

[38] Interdisciplinary Centre for Advanced Materials Simulation, Ruhr-University Bochum. OpenPhase, 2017. < http://www.openphase.de/ > (accessed 08-Dec-2017).

[39] M. Tegeler, O. Shchyglo, R. Darvishi Kamachali, A. Monas, I. Steinbach, G. Sutmann, Parallel multiphase field simulations with openphase, Comput. Phys. Commun. 215 (2017) 173-187 https://www.sciencedirect.com/science/article/pii/S0010465517300358.

[40] F. Roters, P. Eisenlohr, C. Kords, D.D. Tjahjanto, M. Diehl, D. Raabe. Damask: the Düsseldorf advanced material simulation kit for studying crystal plasticity using an fe based or a spectral numerical solver, in: O.Cazacu (Ed.), Procedia IUTAM: IUTAM Symposium on Linking Scales in Computation: From Microstructure to MacroscaleProperties, vol. 3, Elsevier, Amsterdam, 2012a, pp. 3-10. https://doi.org/10.1016/j.piutam.2012.03.001.

[41] F. Roters, M. Diehl, P. Shanthraj, P. Eisenlohr, C. Reuber, S.L. Wong, T. Maiti, A. Ebrahimi, T. Hochrainer, H.-O. Fabritius, S. Nikolov, M. Friak, N. Fujita, N. Grilli, K.G.F. Janssens, N. Jia, P.J.J. Kok, D. Ma, F. Meier, E. Werner, M. Stricker, D. Weygand, D. Raabe, Damask – the Düsseldorf advanced material simulation kit for modelling multi-physics crystal plasticity, damage, and thermal phenomena from the single crystal up to the component scale, Comput. Mater. Sci. (2018) (in press).

[42] L. Zhang, M.R. Tonks, D. Gaston, J.W. Peterson, D. Andrs, P.C. Millett, B.S. Biner, A quantitative comparison between CO and Cl elements for solving the Cahn-Hilliard equation, J. Comput. Phys. 236 (2013) 74-80.

[43] I. Münch, Error measurement and FEM benchmark for phase field modeling, PAMM 15 (1) (2015) 599-600.

[44] CHiMaD and NIST. PFHub: Phase Field Community Hub, 2015. < https://pages.nist.gov/pfhub/ > (accessed 11-July-2018).

[45] A. Jokisaari, P. Voorhees, J. Guyer, J. Warren, O. Heinonen, Benchmark problems for numerical implementations of phase field models, Comput. Mater. Sci. 126 (2017) 139-151.

[46] A. Jokisaari, P. Voorhees, J. Guyer, J. Warren, O. Heinonen, Phase field benchmark problems for dendritic growth and linear elasticity, Comput. Mater. Sci. 149 (2018) 336-347, https://doi.org/10.1016/j.commatsci.2018.03.015 ISSN 0927-0256 < http://www.sciencedirect.com/science/article/pii/S092702561830168X >.

[47] X. Li, K. Thornton, Q. Nie, P.W. Voorhees, J.S. Lowengrub, Two- and three-dimensional equilibrium morphology of a misfitting particle and the Gibbs-Thomson effect, Acta Mater. 52 (20) (2004) 5829-5843, https://doi.org/10.1016/j.actamat.2004.08.041 ISSN 13596454 <http://www.sciencedirect.com/science/article/pii/S1359645404005300> .

[48] A. Karma, W.-J. Rappel, Quantitative phase-field modeling of dendritic growth in two and three dimensions, Phys. Rev. E 57 (4) (1998) 4323.

[49] A.K. Gupta, D.J. Lloyd, S.A. Court, Precipitation hardening in Al-Mg-Si alloys with and without excess si, Mater. Sci. Eng.: A 316 (2001) 11-17.

[50] S. Jiang, H. Wang, Y. Wu, X. Liu, H. Chen, M. Yao, B. Gault, D. Ponge, D. Raabe, A. Hirata, et al., Ultrastrong steel via minimal lattice misfit and high-density nanoprecipitation, Nature 544 (7651) (2017) 460.

[51] F. Larche, J. Cahn, The effect of self-stress on diffusion in solids, Acta Metall. 30 (1982) 1835-1845.

[52] R. DarvishiKamachali, E. Borukhovich, O. Shchyglo, I. Steinbach, Solutal gradients in strained equilibrium, Philos. Mag. Lett. 93 (2013) 680-687.

[53] U. Prahl, M. Lin, M. Weikamp, C. Hueter, D. Schicchi, M. Hunkel, R. Spatschek, Multiscale coupled chemo-mechanical modeling of bainitic transformation during press hardening, Proceedings of the 4th World Congress on Integrated Computational Materials Engineering (ICME 2017), Springer, 2017, pp. 335-343.

[54] M.R. Begley, M. Utz, U. Komaragiri, Chemo-mechanical interactions between adsorbed molecules and thin elastic films, J. Mech. Phys. Solids 53 (9) (2005) 2119-2140.

[55] R. Kazakevičiūtė-Makovska, M. Heuchel, K. Kratz, H. Steeb, Universal relations in linear thermoelastic theories of thermally-responsive shape memory polymers, Int. J. Eng. Sci. 82 (Supplement C) (2014) 140-158, https://doi.org/10.1016/j.ijengsci.2014.05.009 ISSN 0020-7225.

[56] Ruhr-Universität Bochum. Priority Program 1713 "Strong coupling of thermo-chemical and thermo-mechanical states in applied materials", 2008. < http://chemomechanics.de/ > (accessed 19-July-2008).

[57] J.D. Eshelby, The continuum theory of lattice defects, Solid State Phys. 3 (1956) 79-144.

[58] A.G. Khachaturyan, Theory of Structural Transformations in Solids, Courier Corp., 2013.

[59] J.W. Cahn, On spinodal decomposition, Acta Metall. 9 (1961) 795-801.

[60] J.W. Cahn, On spinodal decomposition in cubic crystals, Acta Metall. 10 (1962) 179-183.

[61] L. Löchte, A. Gitt, G. Gottstein, I. Hurtado, Simulation of the evolution of GP zones in Al-Cu alloys: an extended Cahn-Hilliard approach, Acta Mater. 48 (11) (2000) 2969-2984.

[62] W.C. Johnson, On the elastic stabilization of precipitates against coarsening under applied load, Acta Metall. 32 (1984) 465-475.

[63] W.C. Johnson, P. Voorhees, D. Zupon, The effects of elastic stress on the kinetics of ostwald ripening: the two-particle problem, Metall. Trans. A 20 (7) (1989) 1175-1187.

[64] I. Steinbach, M. Apel, Multi phase field model for solid state transformation with elastic strain, Physica D 217 (2006) 153-160.

[65] P. Shanthraj, B. Svendsen, L. Sharma, F. Roters, D. Raabe, Elasto-viscoplastic phase field modelling of anisotropic cleavage fracture, J. Mech. Phys. Solids 99 (2017) 19-34.

[66] B. Svendsen, P. Shanthraj, D. Raabe, Finite-deformation phase-field chemo-mechanics for multiphase, multicomponent solids, J. Mech. Phys. Solids (2018) 1-18, https://doi.org/10.1016/j.jmps.2017.10.005 (in press).

[67] C. Hüter, P. Shanthraj, E. McEniry, R. Spatschek, T. Hickel, A. Tehranchi, X. Guo, F. Roters, Multiscale modelling of hydrogen transport and segregation in polycrystalline steels, Metals 8 (6) (2018) 430, https://doi.org/10.3390/met8060430 <http://www.mdpi.com/2075-4701/8/6/430>.

[68] P. Shanthraj, M. Diehl, P. Eisenlohr, F. Roters, D. Raabe, Handbook of Mechanics of Materials, Chapter Spectral Solvers for Crystal Plasticity and Multi-Physics Simulations, Springer, 2019. https://doi.org/10.1007/978-981-10-6855-3_80-1 (in press).

[69] E. Borukhovich, P. Engels, T. Böhlke, O. Shchyglo, I. Steinbach, Large strain elastoplasticity for diffuse interface models, Modell. Simul. Mater. Sci. Eng. 22 (3) (2014) 034008.

[70] S. Hu, L. Chen, A phase-field model for evolving microstructures with strong elastic inhomogeneity, Acta Mater. 49 (2001) 1879-1890.

[71] S. Balay, S. Abhyankar, M.F. Adams, J. Brown, P. Brune, K. Buschelman, L. Dalcin, V. Eijkhout, W.D. Gropp, D. Kaushik, M.G. Knepley, D.A. May, L.C. McInnes, K. Rupp, B.F. Smith, S. Zampini, H. Zhang, H. Zhang, PETSc Web Page, 2017. < http://www.mcs.anl.gov/petsc >. < http://www.mcs.anl.gov/petsc >.

[72] P. Eisenlohr, M. Diehl, R.A. Lebensohn, F. Roters, A spectral method solution to crystal elasto-viscoplasticity at finite strains, Int. J. Plast. 46 (2013) 37-53.

[73] P. Shanthraj, P. Eisenlohr, M. Diehl, F. Roters, Numerically robust spectral methods for crystal plasticity simulations of heterogeneous materials, Int. J. Plast. 66 (2015) 31-45.

[74] F. Roters, P. Eisenlohr, C. Kords, D.D. Tjahjanto, M. Diehl, D. Raabe, DAMASK: the Düsseldorf Advanced MAterial Simulation Kit for studying crystal plasticity using an FE based or a spectral numerical solver, Procedia IUTAM (2012) 3-10.

[75] M. Lin, U. Prahl, A parallelized model for coupled phase field and crystal plasticity simulation, Comput. Methods Mater. Sci. 16 (2016) 156-162 <www.cmms.agh.edu.pl/abstract.php?p_id=584>.

[76] B. Skrotzki, J. Murken, On the effect of stress on nucleation, growth and coarsening of precipitates in age-hardenable aluminium alloys, in: K.V. Jata (Ed.), Light Weight Alloys for Aerospace Applications VI, The Minerals, Metals & Materials Society, Warrendale, PA, USA, 2001, pp. 51-62.

[77] S. Baumann, D. Williams, A new method for the determination of the precipitate-matrix interfacial energy, Scr. Metall. 18 (1984) 611-616.

[78] S.W. Chen, C.H. Jan, J.C. Lin, Y.A. Chang, Phase equilibria of the Al-Li binary system, Metall. Trans. A 20 (1989) 2247-2258.

[79] J.D. Eshelby, The determination of the elastic field of an ellipsoidal inclusion, and related problems, Proc. Roy. Soc. Lond. A 241 (1957) 376-396.

[80] M. Mehl, Pressure dependence of the elastic moduli in aluminum-rich Al-Li compounds, Phys. Rev. B 47 (1993) 2493-2500.

[81] J.F. Thomas, Third-order elastic constants of aluminum, Phys. Rev. 175 (1968) 955-962.

[82] E.W. Weisstein. L2-norm. from mathworld-a wolfram web resource. < http://mathworld.wolfram.com/L2-Norm.html >.

[83] D. Gottlieb, C.-W. Shu, On the gibbs phenomenon and its resolution, SIAM Rev. 39 (4) (1997) 644-668, https://doi.org/10.1137/S0036144596301390 ISSN 00361445.

[84] A. Gelb, S. Gottlieb, Advances in the Gibbs Phenomenon chapter The Resolution of the Gibbs Phenomenon for Fourier Spectral Methods, Sampling Publishing, Potsdam, New York, 2008 ISBN 0-471-96733010-4-9.

[85] S. Kaßbohm, W.H. Müller, R. Feßler, Improved approximations of fourier coefficients for computing periodic structures with arbitrary stiffness distribution, Comput. Mater. Sci. 37 (1-2) (2006) 90-93, https://doi.org/10.1016/j.commatsci.2005.12.010.

[86] M. Schneider, F. Ospald, M. Kabel, Computational homogenization of elasticity on a staggered grid, Int. J. Numer. Meth. Eng. 105 (9) (2015) 693-720, https://doi.org/10.1002/nme.5008.

[87] F. Willot, Fourier-based schemes for computing the mechanical response of composites with accurate local fields, C.R. Méc. 343 (3) (2015) 232-245, https://doi.org/10.1016/j.crme.2014.12.005.