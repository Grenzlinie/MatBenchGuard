Accepted Manuscript

A variational framework to model diffusion induced large plastic
deformation and phase field fracture during initial two-phase lithiation
of silicon electrodes

Xiaoxuan Zhang, Andreas Krischok, Christian Linder

![](./images/814520538939523073_1.jpg)

PII:
S0045-7825(16)30327-9
DOI:
http://dx.doi.org/10.1016/j.cma.2016.05.007
Reference:
CMA 10965

To appear in: Comput. Methods Appl. Mech. Engrg.

Please cite this article as: X. Zhang, A. Krischok, C. Linder, A variational framework to model
diffusion induced large plastic deformation and phase field fracture during initial two-phase
lithiation of silicon electrodes, Comput. Methods Appl. Mech. Engrg. (2016),
http://dx.doi.org/10.1016/j.cma.2016.05.007

This is a PDF file of an unedited manuscript that has been accepted for publication. As a
service to our customers we are providing this early version of the manuscript. The manuscript
will undergo copyediting, typesetting, and review of the resulting proof before it is published in
its final form. Please note that during the production process errors may be discovered which
could affect the content, and all legal disclaimers that apply to the journal pertain.

# A variational framework to model diffusion induced large plastic deformation and phase field fracture during initial two-phase lithiation of silicon electrodes $^{\dagger}$

Xiaoxuan Zhang, Andreas Krischok, Christian Linder*

Department of Civil and Environmental Engineering, Stanford University, Stanford, California, 94305, USA

## Abstract

Silicon (Si) is considered to be a promising next-generation anode material for lithium-ion batteries. However, the large volume change during (de)lithiation processes causes fracture of Si electrodes, thereby limiting Si's practical application in lithium-ion batteries. In this work, we formulate a variational-based fully chemo-mechanical coupled computational framework to study diffusion induced large plastic deformation and phase field fracture in Si electrodes. Into this framework we incorporate a recently developed reaction-controlled diffusion model to predict two-phase lithiation for amorphous Si (a-Si) and crystalline Si (c-Si) as well as diffusion induced anisotropic deformation for c-Si. The variational formulation suggests to consider the deformation field, chemical potential, and the damage field as primary unknowns. The concentration field is considered as a local variable and is recovered from the chemical potential on the element level. We carry out several numerical simulations to show the performance of our computational model and point out the significance of accurately accounting for the presence of the reaction front when modeling diffusion induced fracture problems for both a-Si and c-Si electrodes. In addition, we investigate how the fracture energy release rate, electrode geometry, and geometrical constraints affect the fracture behavior of Si electrodes.

Keywords: phase-field approaches to fracture, variational principles, two-phase lithiation, reaction-controlled diffusion, diffusion induced anisotropy, silicon electrodes, lithium-ion batteries

---

## 1. Introduction

Lithium-ion batteries are widely used as energy storage devices for portable electronics and electric vehicles [1]. One way to improve their performance is to use new electrode materials. Silicon (Si) is considered to be a promising anode material, characterized by a theoretical specific energy as high as 4200 mAh/g, compared with 372 mAh/g for graphite, the currently most common commercial anode material. However, the large volume change (~300%) of Si electrodes during (de)lithiation processes leads to high mechanical stresses, mechanical failure, chemical degradation, capacity loss, and therefore currently prevents its practical application.

The Si (de)lithiation process is highly complex, involving mass diffusion, electrochemical reaction, and mechanical deformation. With the development of in situ transmission electron microscopy (TEM) technologies [2], important features involved in the (de)lithiation process of Si have been revealed. As illustrated in Fig. 1, those include two-phase lithiation [3-5] as well as diffusion induced large plastic deformation and fracture [6, 7]. During the initial lithiation process, crystalline Si (c-Si) and amorphous Si (a-Si) both undergo two-phase lithiation and are transformed to an amorphous $\text{Li}_x\text{Si}$ (a-$\text{Li}_x\text{Si}$) alloy [3-5]. The two phases (Si and a-$\text{Li}_x\text{Si}$) are separated by a sharp reaction front with a thickness of a few nanometers [8, 9]. It is interesting to note that the anisotropic volume expansion for c-Si shows a preferred lithiation plane [10, 11], while for a-Si, the diffusion induced deformation is isotropic. Fracture phenomena of Si electrodes with different nanostructures are investigated experimentally for both the lithiation [3, 7, 11, 12] and delithiation process [8, 13, 14], with a strong size dependency during initial lithiation [3]. The

---

$^{\dagger}$This paper is dedicated to Professor Christian Miehe on the occasion of his $60^{\text{th}}$ birthday

*Corresponding Author. Email address: linder@stanford.edu

Preprint submitted to Computer Methods in Applied Mechanics and Engineering
May 10, 2016

![](./images/814520538939523073_2.jpg)

Figure 1: Illustration of the two-phase lithiation process in Si electrodes for (a) crystalline [3] and (b) amorphous [5] silicon nanoparticles. In both cases a phase boundary is clearly visible. In (c), the diffusion induced anisotropic deformation for crystalline nanopillars [7] is shown.

fracture energy of lithiated silicon thin-film electrodes is measured in [15] for various Li concentrations. In addition, plastic flow is observed during the (de)lithiation process in thin films, with experimentally measured values for the yield stress provided in [6].

Numerous numerical investigations are carried out in the literature, trying to better understand the experimentally observed complicated mechanical behavior of Si electrodes. Chemo-mechanical coupled models for elasto-plastic deformation at large strain are developed in [16-21] to study the diffusion induced swelling. One can refer to a recent review paper [22] for a more detailed discussion. Theoretical investigations are carried out to study crack nucleation [23, 24], the effect of charging rate on the fracture behavior [25, 26], the size-dependency of fracture [27], and the resulting anisotropic deformation in c-Si nanopillars [28] during the diffusion process in Si electrodes. To determine the onset of fracture, different crack driving forces are proposed based on a chemo-mechanical coupled $J$-integral [18], the maximum tensile strength theory [23], or the strain energy release rate [27].

To model the propagation of a crack in a failing material, several numerical tools exist. Successful approaches are the embedded finite element method [29-39] or the extended finite element method [40-43], both describing the crack as a discrete entity. Alternatively, diffusive phase field approaches to fracture [44-48] are currently experiencing a dramatic upsurge as those do not require the geometric information of a possible failure onset and perform well when complicated failure surfaces are expected for cases when multiple cracks are present or when cracks coalesce and branch. The phase field approach to fracture can be traced back to the seminal work of [44, 45], where the sharp crack topology is replaced with a regularized crack zone governed by a scalar damage variable and where an elegant variational description of the resulting energy minimization problem is proposed. Extensions are made in [47, 49] to account for tension-only induced fracture through a decomposition of the free energy into a tensile and compressive part, and to prevent crack reversal through the introduction of a history field for the crack driving force. A staggered update scheme is proposed in [48, 50] to efficiently solve the resulting system of equations. Phase field approaches to brittle fracture are further extended to account for dynamic fracture [51, 52], higher order approximations of the damage field [53, 54], different types of material [55-58], multiphysics problems [50, 59-62], and ductile fracture [63-67].

To better understand the complicated interplay of all the complex physical processes arising during the initial lithiation of Si electrodes, we extend existing phase field approaches for modeling fracture in electrode materials [68-70] and propose in this work a variational based fully chemo-mechanical coupled computational framework that accounts for diffusion induced plastic deformation, diffusion induced fracture, the existence of the phase boundary, and the diffusion induced anisotropic deformation for c-Si. Supported by experimental observations shown in Fig. 2, we treat the diffusion induced fracture as being brittle. Due to the variational based origin of the phase field approach to fracture we formulate the diffusion process, elasto-plastic deformation, and diffusion induced fracture in terms of mixed variational principles and rate-type potentials. Following [71-78], after properly defining the rate- type functionals of the problem, the primary unknowns are solved through an incremental variational formulation for

![](./images/814520538939523073_3.jpg)

Figure 2: Experimental illustration of diffusion induced fracture where cracks are formed in a brittle manner [15]. The scanning electron microscope images show multiple cracks formed after a lithiation and delithiation cycle of a-Si thin film electrodes.

dissipative solids, resulting in an efficient finite element approximation of this complex coupled problem due to the inherent symmetry of the incremental variational principle. The notion of algorithmic functionals further motivates a staggered scheme in line with [48, 50, 55] to solve the update of the fracture phase field and the coupled deformation-diffusion problem as two successive updates to avoid a computationally more expensive monolithic scheme. In this work, rather than using the concentration field as the primary unknown of the diffusion process [21, 79, 80], we derive a variational framework in Section 2 that makes use of a global chemical potential, similar to works such as [81-83]. Furthermore, instead of using Cahn-Hilliard type diffusion [75, 84-86] to account for the arising two-phase lithiation, we use our recently proposed reaction controlled diffusion model [87] to describe the initial lithiation of c-Si and a-Si. Doing so allows us to predict the diffusion induced anisotropic deformation depending on the crystalline structure of Si. We carry out several numerical simulations to show the performance of our computational model and point out the significance of accurately accounting for the presence of the reaction front when modeling diffusion induced fracture problems for both a-Si and c-Si electrodes. In addition, we investigate how the fracture energy release rate, electrode geometry, and geometrical constraints affect the fracture behavior of Si electrodes.

The rest of the paper is organized as follows. In Section 2, we summarize the continuous variational framework for diffusion induced elasto-plastic deformation and phase field fracture in Si electrodes of Li-ion batteries. Its discrete version is derived in Section 3 by adopting a temporal and staggered spatial discretization. We briefly review our reaction controlled diffusion model [87] in Section 4 and embed it into the variational framework to model the two-phase lithiation process. Different numerical examples are carried out in Section 5, showcasing the performance of our proposed model. We close by giving several concluding remarks in Section 6.

## 2. Continuous variational framework for diffusion induced elasto-plastic deformation and phase field fracture

In this section, we summarize the continuous variational framework for diffusion induced elasto-plastic deformation and phase field fracture in Si electrodes of Li-ion batteries. After defining the primary fields and boundary conditions of the coupled problem in Section 2.1, we follow [55, 62, 75, 76] and set up the corresponding variational framework in terms of rate-type potentials in Section 2.2 and specify those rate-type potentials in Section 2.2.1 with corresponding energy storage and dissipation functions in Section 2.2.2 as well as constitutive relations in Section 2.2.3. Finally, we arrive at the Euler equations for the underlying problem in Section 2.2.4.

### 2.1. The primary fields and boundary conditions

The diffusion induced elasto-plastic deformation and fracture problem is formulated as a three-field problem characterized by the deformation field $\boldsymbol{\varphi}$, the chemical potential $\mu$, and the damage phase field $d$ as global primary fields. The deformation field $\boldsymbol{\varphi}: \mathcal{B}_{0} \times \mathcal{T} \rightarrow \mathcal{B} \in \mathbb{R}^{n_{\text {dim }}}$ is a non-linear map of points $\boldsymbol{X}$ in the reference configuration $\mathcal{B}_{0}$ to points $\boldsymbol{x}$ in the current configuration $\mathcal{B}$ at time $t \in \mathcal{T}$. The chemical potential $\mu: \mathcal{B}_{0} \times \mathcal{T} \rightarrow \mathbb{R}$ drives the evolution of the Li concentration $c$ during the (de)lithiation processes and thereby causes the large swelling deformation damaging

![](./images/814520538939523073_4.jpg)

Figure 3: Illustration of undeformed (left) and deformed (right) configuration of the chemo-mechanical coupled initial boundary value problem, formulated in terms of the three primary fields $\{\boldsymbol{\varphi}, \mu, d\}$ and loaded through a body force $\boldsymbol{\gamma}$ in $\mathcal{B}$ and at the boundary $\partial \mathcal{B}$. The latter is divided into $\partial \mathcal{B}=\overline{\partial \mathcal{B}^{\varphi} \cup \partial \mathcal{B}^{t}}, \partial \mathcal{B}=\overline{\partial \mathcal{B}^{\mu} \cup \partial \mathcal{B}^{h}}$, and $\partial \mathcal{B}=\overline{\partial \mathcal{B}^{d} \cup \partial \mathcal{B}^{\nabla d}}$ for the mechanical, the diffusive, and the fracture problem, respectively. The outer shell represents the amorphous $\mathrm{Li}_{x} \mathrm{Si}$ alloy and the shaded center represents the unlithiated Si core, indicating a two-phase lithiation process. The red line in the deformed configuration represents the diffusion induced crack which is approximated by the phase field $d$ with a diffusive crack topology controlled by a regularized length parameter $l$.

the material. In the presence of fracture, the crack phase field $d: \mathcal{B}_{0} \times \mathcal{T} \rightarrow[0,1]$ describes the diffusive crack topology with $d(\boldsymbol{X}, t)=0$ defining the virgin and $d(\boldsymbol{X}, t)=1$ the fully damaged state of the material at $\boldsymbol{X} \in \mathcal{B}_{0}$ and time $t \in \mathcal{T}$. The material gradients of the deformation field and the chemical potential are defined as

$$
\boldsymbol{F}=\nabla \boldsymbol{\varphi}(\boldsymbol{X}, t) \quad \text { and } \quad \mathbb{M}=-\nabla \mu(\boldsymbol{X}, t). \tag{1}
$$

We note that the concentration field $c: \mathcal{B}_{0} \times \mathcal{T} \rightarrow[0,1]$ is a normalized quantity, which represents the actual concentration of the species Li in terms of moles per unit reference volume with respect to the maximum concentration $c_{\max }$ and is treated as a local quantity that can be recovered from the chemical potential $\mu$. Following [84, 85], we consider a multiplicative decomposition of the deformation gradient into

$$
\boldsymbol{F}=\boldsymbol{F}^{e} \boldsymbol{F}^{c} \boldsymbol{F}^{p} \quad \text { with } \quad \boldsymbol{F}^{c}=J_{c}^{1 / 3} \boldsymbol{I} \quad \text { and } \quad J_{c}=1+\Omega c. \tag{2}
$$

Here, $\boldsymbol{F}^{e}, \boldsymbol{F}^{c}$, and $\boldsymbol{F}^{p}$ are the elastic, swelling, and plastic components of the deformation gradient with their respective Jacobians $J=\operatorname{det} \boldsymbol{F}>0, J_{c}=\operatorname{det} \boldsymbol{F}^{c}>0$, and $\operatorname{det} \boldsymbol{F}^{p}=1$. In (2), we assume that the diffusion induced swelling is isotropic with $\Omega$ being the expansion coefficient. Consequently, the Lagrangian and Eulerian strain tensors used to describe the elasto-plastic deformation of the material can be computed as

$$
\boldsymbol{C}=\boldsymbol{F}^{T} \boldsymbol{F}, \quad \boldsymbol{C}^{p}=\boldsymbol{F}^{p T} \boldsymbol{F}^{p} \quad \text { and } \quad \boldsymbol{b}=\boldsymbol{F} \boldsymbol{F}^{T}, \quad \boldsymbol{b}^{e}=J_{c}^{-2 / 3} \boldsymbol{F} \boldsymbol{C}^{p-1} \boldsymbol{F}^{T}. \tag{3}
$$

The first Piola-Kirchhoff stress tensor in the bulk is denoted as $\boldsymbol{P}$, which is related to the Cauchy stress $\boldsymbol{\sigma}$ and the Kirchhoff stress $\boldsymbol{\tau}$ by $\boldsymbol{\sigma}=J^{-1} \boldsymbol{P} \boldsymbol{F}^{T}$ and $\boldsymbol{\tau}=\boldsymbol{P} \boldsymbol{F}^{T}$, respectively. Introducing $\boldsymbol{N}$ as the outward normal of a reference area element $d A$ and $\boldsymbol{n}$ as the outward normal of a spatial area element $d a$, we have

$$
\boldsymbol{T}=\boldsymbol{P N} \quad \text { and } \quad \boldsymbol{t}=\boldsymbol{\sigma} \boldsymbol{n} \tag{4}
$$

where $\boldsymbol{T}$ and $\boldsymbol{t}$ are the corresponding traction vectors. Similarly, the material species flux vector $\mathbb{H}$ in $\mathcal{B}_{0}$ and the spatial species flux vector $\mathbb{h}$ in $\mathcal{B}$ are related to the species outward fluxes $H$ and $h$ by

$$
H=\mathbb{H} \cdot \boldsymbol{N} \quad \text { and } \quad h=\mathbb{h} \cdot \boldsymbol{n}. \tag{5}
$$

The introduction of the traction vector $\boldsymbol{t}$ and the species outward flux $h$ allows us to specify the boundary conditions for this coupled problem. As illustrated in Fig. 3, the overall boundary $\partial \mathcal{B}$ of the body is divided into $\partial \mathcal{B}=\overline{\partial \mathcal{B}^{\varphi} \cup \partial \mathcal{B}^{t}}$ with $\partial \mathcal{B}^{\varphi} \cap \partial \mathcal{B}^{t}=\varnothing$ for the mechanical problem, $\partial \mathcal{B}=\partial \mathcal{B}^{\mu} \cup \partial \mathcal{B}^{h}$ with $\partial \mathcal{B}^{\mu} \cap \partial \mathcal{B}^{h}=\varnothing$ for the diffusive problem, and $\partial \mathcal{B}=\partial \mathcal{B}^{d} \cup \partial \mathcal{B}^{\nabla d}$ with $\partial \mathcal{B}^{d}=\varnothing$ and $\partial \mathcal{B}^{\nabla d}=\partial \mathcal{B}$ for the fracture problem. The essential and natural boundary conditions for those three fields are then given as

$$
\begin{aligned}
\boldsymbol{\varphi} & =\overline{\boldsymbol{\varphi}}(\boldsymbol{x}, t) \quad \text { on } \quad \partial \mathcal{B}^{\varphi} & \text { and } & \boldsymbol{\sigma} \boldsymbol{n} & =\overline{\boldsymbol{t}}(\boldsymbol{x}, t) \quad \text { on } \quad \partial \mathcal{B}^{t} \\
\mu & =\bar{\mu}(\boldsymbol{x}, t) \quad \text { on } \quad \partial \mathcal{B}^{\mu} & \text { and } & \mathbb{h} \cdot \boldsymbol{n} & =\bar{h}(\boldsymbol{x}, t) \quad \text { on } \quad \partial \mathcal{B}^{h} \\
& & & \nabla d \cdot \boldsymbol{n} & =0 \quad \text { on } \quad \partial \mathcal{B}^{\nabla d}
\end{aligned}
\tag{6}
$$

where $\overline{\boldsymbol{\varphi}}, \overline{\boldsymbol{t}}, \bar{\mu}$, and $\bar{h}$ are the prescribed values for the deformation, traction, chemical potential, and species flux, respectively. In addition to the boundary conditions, we have to specify the initial values of the chemical potential $\mu$ at time $t=t_{0}$ as

$$
\mu\left(\boldsymbol{X}, t=t_{0}\right)=\mu_{0}(\boldsymbol{X}) \quad \text { in } \quad \mathcal{B}_{0}
\tag{7}
$$

or equivalently written in terms of the Li concentration as $c\left(\boldsymbol{X}, t=t_{0}\right)=c_{0}(\boldsymbol{X})$ in $\mathcal{B}_{0}$.

### 2.2. Mixed variational principles and rate-type potentials

To establish a holistic modeling framework for the complex mechanisms arising during the (de)lithiation process in Si electrodes of Li-ion batteries, we construct a mixed variational framework based on a rate-type functional whose associated Euler equations yield the governing equations for the underlying problem.

#### 2.2.1. Multi-field rate-type potential

Inspired by similar frameworks for dissipative solids such as [71-78], we construct a variational principle for which the evolution of the deformation field $\boldsymbol{\varphi}$, damage field $d$, and a set of local constitutive variables $\boldsymbol{\xi}_{\mathbb{C}}$ as well as the state of the chemical potential $\mu$ and non-evolving local fields $\boldsymbol{\xi}_{\tilde{\mathbb{\delta}}}$ are governed by the stationarity of a proper rate-type potential functional $\Pi$ for the coupled problem, i.e.

$$
\Pi\left(\dot{\boldsymbol{\varphi}}, \mu, \dot{d}, \dot{\boldsymbol{\xi}}_{\mathbb{C}}, \boldsymbol{\xi}_{\tilde{\mathbb{\delta}}}\right)=\frac{d}{d t} \mathscr{E}\left(\boldsymbol{\varphi}, d, \boldsymbol{\xi}_{\mathbb{C}}\right)+\mathscr{D}\left(\mu, \dot{d}, \dot{\boldsymbol{\xi}}_{\mathbb{C}}, \boldsymbol{\xi}_{\tilde{\mathbb{\delta}}}\right)-\mathscr{P}_{\mathrm{ext}}^{\varphi, \mu}(\dot{\boldsymbol{\varphi}}, \mu)
\tag{8}
$$

at a given state $\{\boldsymbol{\varphi}, d, \boldsymbol{\xi}_{\mathbb{C}}\}$. Here, $\boldsymbol{\xi}_{\tilde{\mathbb{\delta}}}$ denotes a general array of local dissipative driving forces and associated Lagrange multipliers. The general form of the energy storage functional $\mathscr{E}$ is given as

$$
\mathscr{E}\left(\boldsymbol{\varphi}, d, \boldsymbol{\xi}_{\mathbb{C}}\right)=\int_{\mathcal{B}_{0}} \psi\left(\nabla \boldsymbol{\varphi}, d, \boldsymbol{\xi}_{\mathbb{C}}\right) d V
\tag{9}
$$

with $\psi$ as the free energy density. The dissipation potential functional $\mathscr{D}$ arises from dissipative processes during plastic deformation, diffusion, and fracture. Its general form is given as

$$
\mathscr{D}\left(\mu, \dot{d}, \dot{\boldsymbol{\xi}}_{\mathbb{C}}, \boldsymbol{\xi}_{\tilde{\mathbb{\delta}}}\right)=\int_{\mathcal{B}_{0}} \chi\left(\mu, \mathbb{M}, \dot{d}, \dot{\boldsymbol{\xi}}_{\mathbb{C}}, \boldsymbol{\xi}_{\tilde{\mathbb{\delta}}} ; \nabla \boldsymbol{\varphi}, d, \boldsymbol{\xi}_{\mathbb{C}}\right) d V
\tag{10}
$$

with $\chi$ as the dissipation potential density. The external power functional $\mathscr{P}_{\mathrm{ext}}^{\varphi, \mu}(\dot{\boldsymbol{\varphi}}, \mu)$ consists of a mechanical contribution $\mathscr{P}_{\text {ext }}^{\varphi}(\dot{\boldsymbol{\varphi}} ; t)$ and a diffusive contribution $\mathscr{P}_{\text {ext }}^{\mu}(\mu ; t)$, which are both given as

$$
\mathscr{P}_{\mathrm{ext}}^{\varphi}(\dot{\boldsymbol{\varphi}} ; t)=\int_{\mathcal{B}_{0}} \rho_{0} \boldsymbol{\gamma} \cdot \dot{\boldsymbol{\varphi}} d V+\int_{\partial \mathcal{B}_{0}^{t}} \overline{\boldsymbol{T}} \cdot \dot{\boldsymbol{\varphi}} d A \quad \text { and } \quad \mathscr{P}_{\mathrm{ext}}^{\mu}(\mu ; t)=-\int_{\partial \mathcal{B}_{0}^{h}} \mu \bar{H} d A
\tag{11}
$$

where $\rho_{0}$ is the reference density of the body, $\boldsymbol{\gamma}$ is the body force, and $\overline{\boldsymbol{T}}$ and $\bar{H}$ are the prescribed traction and species flux, respectively. The general forms of the energy storage functional $\mathscr{E}$ and the dissipation potential functional $\mathscr{D}$ in (9)-(10) allow us to recast the rate-type potential functional in (8) into an internal and an external contribution as

$$
\Pi\left(\dot{\boldsymbol{\varphi}}, \mu, \dot{d}, \dot{\boldsymbol{\xi}}_{\mathbb{C}}, \boldsymbol{\xi}_{\tilde{\mathbb{\delta}}}\right)=\int_{\mathcal{B}_{0}} \pi\left(\nabla \dot{\boldsymbol{\varphi}}, \mu, \mathbb{M}, \dot{d}, \dot{\boldsymbol{\xi}}_{\mathbb{C}}, \boldsymbol{\xi}_{\tilde{\mathbb{\delta}}}\right) d V-\mathscr{P}_{\mathrm{ext}}^{\varphi, \mu}(\dot{\boldsymbol{\varphi}}, \mu)
\tag{12}
$$

with $\pi$ as the mixed internal rate potential density given as

$$
\pi(\nabla \dot{\boldsymbol{\varphi}}, \mu, \mathbb{M}, \dot{d}, \dot{\boldsymbol{\xi}}_{\mathfrak{C}}, \boldsymbol{\xi}_{\mathfrak{F}})=\frac{d}{d t} \psi(\nabla \boldsymbol{\varphi}, d, \boldsymbol{\xi}_{\mathfrak{C}})+\chi(\mu, \mathbb{M}, \dot{d}, \dot{\boldsymbol{\xi}}_{\mathfrak{C}}, \boldsymbol{\xi}_{\mathfrak{F}} ; \nabla \boldsymbol{\varphi}, d, \boldsymbol{\xi}_{\mathfrak{C}})
\tag{13}
$$

depending on the evolution of the free energy density $\psi$ in time and the dissipation potential density $\chi$. To avoid overcomplicating this coupled problem, we neglect the local mass density difference induced by the diffusion of lithium.

### 2.2.2. Specification of energy storage and dissipation functions

Next, the generalized forms of the free energy functional $\mathscr{E}$ in (9) and the dissipation potential functional $\mathscr{D}$ in (10) are specified in more detail for the coupled problem at hand. The free energy density in (9) can be written as

$$
\psi(\nabla \boldsymbol{\varphi}, d, \boldsymbol{\xi}_{\mathfrak{C}})=\psi_{\text{elas}}(\boldsymbol{F}, c, d, \mathfrak{C}_{p})+\psi_{\text{plas}}(\mathfrak{C}_{p})+\psi_{\text{chem}}(c).
\tag{14}
$$

Here, $\mathfrak{C}_{p} \in \boldsymbol{\xi}_{\mathfrak{C}}$ denotes in a generalized way the internal constitutive state array for the plastic response, which is energetically conjugate to the general array of dissipative internal forces $\mathfrak{F}_{p} \in \boldsymbol{\xi}_{\mathfrak{F}}$. The explicit forms for $\psi_{\text{elas}}, \psi_{\text{plas}}$, and $\psi_{\text{chem}}$ are given in Section 2.2.3 where we specify the chosen constitutive relations. The requirement that the evolution of the stored energy must be less than the external power due to irreversible dissipative effects is expressed by the global dissipation postulate

$$
\frac{d}{d t} \mathscr{E}(\boldsymbol{\varphi}, d, \boldsymbol{\xi}_{\mathfrak{C}}) \leq \mathscr{P}_{\text{ext}}^{\boldsymbol{\varphi}, \mu}(\dot{\boldsymbol{\varphi}}, \mu)
\tag{15}
$$

which can be recast to a local dissipation postulate consisting of a part due to local action

$$
\mathscr{D}^{\text{loc}}=\boldsymbol{\tau}: \boldsymbol{d}+\mu \dot{c}-\dot{\psi} \geq 0
\tag{16}
$$

and a part due to diffusion

$$
\mathscr{D}^{\text{diff}}=\mathbb{H} \cdot \mathbb{M} \geq 0
\tag{17}
$$

where we have introduced $\boldsymbol{d}=\operatorname{sym}[\boldsymbol{l}]$ with the spatial velocity gradient $\boldsymbol{l}=\dot{\boldsymbol{F}} \boldsymbol{F}^{-1}$. The definition of (14) and the demand (16) yields the constitutive relations, by adopting the postulate that a set of constitutive equations is admissible only if these constitutive equations are compatible with a non-negative entropy production [88]. Hence, we have

$$
\boldsymbol{P}=\partial_{\boldsymbol{F}} \psi_{\text{elas}}, \quad \mu=\partial_{c} \psi, \quad \mathfrak{F}_{p}=-\partial_{\mathfrak{C}_{p}} \psi_{\text{elas}}, \quad \beta^{f}=-\partial_{d} \psi_{\text{elas}}
\tag{18}
$$

along with the reduced local dissipation inequality

$$
\mathscr{D}_{\text{red}}^{\text{loc}}=\mathfrak{F}_{p} \cdot \dot{\mathfrak{C}}_{p}+\beta^{f} \dot{d} \geq 0
\tag{19}
$$

where we introduced the driving force $\beta^{f} \in \boldsymbol{\xi}_{\mathfrak{F}}$ for fracture processes being conjugate to $\dot{d}$. Next, we specify in more detail the dissipation potential density $\chi$ in (10) for the subsequent construction of the variational framework for the dissipative material considered in this work. For the problem at hand we divide it into plastic, diffusive, and fracture parts as $\chi=\chi_{\text{plas}}+\chi_{\text{diff}}+\chi_{\text{frac}}$. The plastic dissipation potential density for rate-independent problems is defined by the principle of maximum dissipation [89], that defines the constrained problem

$$
\chi_{\text{plas}}(\dot{\mathfrak{C}}_{p} ; \mathfrak{C}_{p})=\sup _{\mathfrak{F}_{p} \in \mathbb{E}_{p}}\left\{\mathfrak{F}_{p} \cdot \dot{\mathfrak{C}}_{p}\right\}
\tag{20}
$$

where $\mathbb{E}_{p}=\left\{\mathfrak{F}_{p} \mid f_{\text{plas}}(\mathfrak{F}_{p} ; \mathfrak{C}_{p}) \leq 0\right\}$ models the elastic space of the dissipative forces in terms of a yield function $f_{\text{plas}}(\mathfrak{F}_{p} ; \mathfrak{C}_{p})$. This constrained problem is solved by a Lagrange method after introducing the Lagrange multiplier $\lambda_{p} \in \boldsymbol{\xi}_{\mathfrak{F}}$ based on

$$
\chi_{\text{plas}}(\dot{\mathfrak{C}}_{p} ; \mathfrak{C}_{p})=\sup _{\mathfrak{F}_{p}, \lambda_{p} \geq 0}\left\{\mathfrak{F}_{p} \cdot \dot{\mathfrak{C}}_{p}-\lambda_{p} f_{\text{plas}}(\mathfrak{F}_{p} ; \mathfrak{C}_{p})\right\}
\tag{21}
$$

inducing the flow rule $\dot{\mathbb{C}}_{p}=\lambda_{p} \partial_{\mathfrak{F}_{p}} f_{\text {plas }}$ along with the Kuhn-Tucker loading-unloading-conditions

$$
\lambda_{p} \geq 0, \quad f_{\text {plas }}\left(\mathfrak{F}_{p} ; \mathfrak{C}_{p}\right) \leq 0, \quad \lambda_{p} f_{\text {plas }}\left(\mathfrak{F}_{p} ; \mathfrak{C}_{p}\right)=0 .
$$

Second, following [75], we specify the diffusive part of the dissipation potential as

$$
\chi_{\text {diff }}(\dot{c}, \mu, \mathbb{M} ; \boldsymbol{F}, c, d)=-\mu \dot{c}-\phi_{\text {diff }}(\mathbb{M} ; \boldsymbol{F}, c, d) .
$$

Here we treat the concentration $c \in \boldsymbol{\xi}_{\mathbb{C}}$ as a local constitutive field. The dissipation potential $\phi_{\text {diff }}$ whose specific form is given in Section 2.2.3 is convex quadratic in $\mathbb{M}$ and satisfies condition (17) via the constitutive relation

$$
\mathbb{H}=\partial_{\mathbb{M}} \phi_{\text {diff }} .
$$

Finally, following [47, 48, 55] the dissipation potential function $\chi_{\text {frac }}$ for rate-independent fracture processes at a given state $d$ is constructed based on thermodynamic arguments

$$
\int_{\mathcal{B}_{0}}\left[\partial_{d} \chi_{\text {frac }} \dot{d}\right] d V \geq 0
$$

and defined by the principle of maximum dissipation, that is,

$$
\chi_{\text {frac }}(\dot{d} ; d, \Delta d)=\sup _{\beta^{f} \in \mathbb{E}_{\mathrm{f}}}\left\{\beta^{f} \dot{d}\right\}
$$

in terms of the driving force $\beta^{f}$, conjugate to $d$. This constrained problem can be solved by a Lagrange method

$$
\chi_{\text {frac }}(\dot{d} ; d, \Delta d)=\sup _{\beta^{f}, \lambda_{f} \geq 0}\left\{\beta^{f} \dot{d}-\lambda_{f} t_{c}\left(\beta^{f} ; d, \Delta d\right)\right\}
$$

along with the crack irreversibility conditions

$$
t_{c}\left(\beta^{f} ; d, \Delta d\right) \leq 0, \quad t_{c}\left(\beta^{f} ; d, \Delta d\right) \dot{d}=0, \quad \dot{d} \geq 0
$$

where $\lambda_{f} \in \boldsymbol{\xi}_{\mathfrak{F}}$ is a Lagrange multiplier enforcing the local threshold function $t_{c}$ to define the reversible domain

$$
\mathbb{E}_{\mathrm{f}}=\left\{\beta^{f} \mid t_{c}\left(\beta^{f} ; d, \Delta d\right) \leq 0\right\}
$$

in which $t_{c}$ is defined as

$$
t_{c}\left(\beta^{f} ; d, \Delta d\right)=\beta^{f}-g_{c} \delta_{d} \gamma(d, \nabla d) \leq 0 \quad \text { with } \quad \gamma(d, \nabla d)=\frac{1}{2 l} d^{2}+\frac{l}{2}|\nabla d|^{2} .
$$

Here, $\gamma(d, \nabla d)$ is the crack surface density function, and $g_{c}$ is the critical energy release rate. The crack surface density function $\gamma$ is used to approximate a sharp crack by a diffusive crack topology controlled by a regularized length parameter $l$, as illustrated in Fig. 3.

### 2.2.3. Constitutive model

In this section we further specify the free energy density $\psi$ in (14), the plastic yield function $f_{\text {plas }}$ in (21), and the convex dissipative potential $\phi_{\text {diff }}$ in (23). Starting with the elastic free energy density, we assume a perfect von Mises plasticity model without hardening such that $\psi_{\text {plas }}=0$. To prevent the material from failing under compression, the elastic free energy $\psi_{\text {elas }}$ in (14) is decomposed into tensile and compressive parts as

$$
\psi_{\text {elas }}\left(\boldsymbol{F}, d, c, \mathfrak{C}_{p}\right)=\left[(1-d)^{2}+k\right] \psi_{\text {elas }}^{+}\left(\boldsymbol{F}, c, \mathfrak{C}_{p}\right)+\psi_{\text {elas }}^{-}\left(\boldsymbol{F}, c, \mathfrak{C}_{p}\right)
$$

where only the tensile part of the free energy $\psi_{\text {elas }}^{+}$drives the damage and crack propagation in the material, and $k$ is a very small positive value to provide numerical stability when $d=1$ [47]. The objective elastic free energy

contribution $\psi_{\text{elas}}$ in (31) in an Eulerian setting is expressed by the elastic left Cauchy-Green tensor defined in (3). Time-differentiating the elastic part of the stored free energy yields

$$
\dot{\psi}_{\text{elas}}=\partial_{\boldsymbol{b}^{e}} \psi_{\text{elas}}: \dot{\boldsymbol{b}}^{e}+\partial_{d} \psi_{\text{elas}} \dot{d}=2 \partial_{\boldsymbol{b}^{e}} \psi_{\text{elas}} \boldsymbol{b}^{e}:\left[\boldsymbol{I}+\frac{1}{2}\left(\mathcal{L}_{\boldsymbol{v}} \boldsymbol{b}^{e}\right) \boldsymbol{b}^{e-1}\right]+\partial_{c} \psi_{\text{elas}} \dot{c}+\partial_{d} \psi_{\text{elas}} \dot{d}.\qquad(32)
$$

By comparison with (16) and (19) we obtain

$$
\boldsymbol{\tau}=2 \partial_{\boldsymbol{b}^{e}} \psi_{\text{elas}} \boldsymbol{b}^{e}.\qquad(33)
$$

The restriction of the considered material response to isotropy motivates the spectral decomposition of the left Cauchy-Green tensor defined in (3) as

$$
\boldsymbol{b}^{e}=\sum_{A=1}^{n_{\text{dim}}}\left(\lambda_{A}\right)^{2} \boldsymbol{n}_{A} \otimes \boldsymbol{n}_{A} \quad \text { and } \quad \boldsymbol{\tau}=\sum_{A=1}^{n_{\text{dim}}} \tau_{A} \boldsymbol{n}_{A} \otimes \boldsymbol{n}_{A}\qquad(34)
$$

where $\left(\lambda_{A}\right)^{2}$ and $\tau_{A}$ denote the principal values and $\boldsymbol{n}_{A}$ the corresponding principal directions for $A=1, \ldots, n_{\text{dim}}$. In the case of isotropy one can show that the Kirchhoff stress tensor can be directly obtained from

$$
\boldsymbol{\tau}=\partial_{\boldsymbol{h}^{e}} \psi_{\text{elas}} \quad \text { with } \quad \boldsymbol{h}^{e}=\frac{1}{2} \log \boldsymbol{b}^{e}=\sum_{A=1}^{n_{\text{dim}}} \varepsilon_{A}^{e} \boldsymbol{n}_{A} \otimes \boldsymbol{n}_{A}\qquad(35)
$$

where $\boldsymbol{h}^{e}$ with the principal elastic logarithmic stretches $\varepsilon_{A}^{e}=\log \left(\lambda_{A}^{e}\right)$ is introduced as a logarithmic Hencky-type strain tensor for which the time derivative of the stored energy can be written as

$$
\dot{\psi}=\left(\partial_{\boldsymbol{h}^{e}} \psi_{\text{elas}} \boldsymbol{F}^{-T}\right): \nabla \dot{\boldsymbol{\varphi}}+\partial_{\boldsymbol{h}^{e}} \psi_{\text{elas}}: \frac{1}{2}\left(\mathcal{L}_{\boldsymbol{v}} \boldsymbol{b}^{e}\right) \boldsymbol{b}^{e-1}+\partial_{c} \psi \dot{c}+\partial_{d} \psi_{\text{elas}} \dot{d}.\qquad(36)
$$

The elastic free energy contribution $\psi_{\text{elas}}$ in (31) is given in quadratic form as

$$
\psi_{\text{elas}}^{ \pm}\left(\boldsymbol{h}^{e}\right)=\frac{1}{2} \hat{\lambda}\left\langle\log \left(J^{e}\right)\right\rangle_{ \pm}^{2}+\hat{\mu} \sum_{A=1}^{n_{\text{dim}}}\left\langle\varepsilon_{A}^{e}\right\rangle_{ \pm}^{2}\qquad(37)
$$

with $\hat{\lambda}$ and $\hat{\mu}$ as the Lamé constants. The bracket operators $\langle\bullet\rangle_{ \pm}$are defined as $\langle\bullet\rangle_{ \pm}=(\bullet \pm|\bullet|) / 2$. From the free energy function in (37), the principal Kirchhoff stress components $\tau_{A}$ can be computed as

$$
\tau_{A}=\frac{\partial \psi_{\text{elas}}}{\partial \varepsilon_{A}^{e}}=\left[(1-d)^{2}+k\right]\left[\hat{\lambda}\left\langle\log \left(J^{e}\right)\right\rangle_{+}+2 \hat{\mu}\left\langle\varepsilon_{A}^{e}\right\rangle_{+}\right]+\left[\hat{\lambda}\langle\log (J)\rangle_{-}+2 \hat{\mu}\left\langle\varepsilon_{A}^{e}\right\rangle_{-}\right].\qquad(38)
$$

The reduced local dissipation inequality reads

$$
\mathcal{D}_{\text{red}}^{\text{loc}}=\boldsymbol{\tau}: \boldsymbol{I}^{p}+\beta^{f} \dot{d} \geq 0\qquad(39)
$$

where we introduced the Eulerian evolution operator $\boldsymbol{I}^{p}=-\frac{1}{2}\left(\mathcal{L}_{\boldsymbol{v}} \boldsymbol{b}^{e}\right) \boldsymbol{b}^{e-1}=-\frac{1}{2} \boldsymbol{F} \dot{\boldsymbol{C}}^{p-1} \boldsymbol{F}^{-1} \boldsymbol{b}^{e-1}$. This motivates the subsequent identification $\mathfrak{C}_{p}=\left\{\boldsymbol{C}^{p}\right\}$ and $\mathfrak{F}_{p}=\{\boldsymbol{\tau}\}$. Note in this context that although $\boldsymbol{I}^{p}$ is energetically conjugate to $\boldsymbol{\tau}$ in the subsequent variational framework variations with respect to $\boldsymbol{I}^{p}$ and $\boldsymbol{C}^{p}$ can be used interchangeably and $\boldsymbol{C}^{p}$ is updated locally. For perfect von Mises plasticity, the yield function $f_{\text{plas}}$ is given in terms of the Kirchhoff stress $\boldsymbol{\tau}$ and the yield stress $\sigma_{0}$ as

$$
f_{\text{plas}}(\boldsymbol{\tau})=\|\operatorname{dev} \boldsymbol{\tau}\|-\sqrt{\frac{2}{3}} \sigma_{0}.\qquad(40)
$$

The chemical contribution $\psi_{\text{chem}}(c)$ to the free energy density in (14) is assumed to have the form [21]

$$
\psi_{\text{chem}}(c)=c_{\max } R T[c \log c+(1-c) \log (1-c)]\qquad(41)
$$

where $c_{\max }$ is the maximum Li concentration, $R$ is the gas constant, and $T$ is the room temperature. Following [75], the convex diffusion dissipation potential $\phi_{\text{diff}}$ in (23) is chosen as

$$
\phi_{\text{diff}}(\mathbb{M} ; \boldsymbol{F}, c, d)=\frac{1}{2} M(c, d) \boldsymbol{C}^{-1}:(\mathbb{M} \otimes \mathbb{M})\qquad(42)
$$

where
$$
M(c, d)=\frac{D_{\text {diff }}(c, d)}{c_{\max } R T}[c(1-c)] \quad \text { and } \quad D_{\text {diff }}(c, d)=D_{\text {diff }}^{0}(c)+d\left(D_{\text {diff }}^{\max }-D_{\text {diff }}^{0}(c)\right)
\tag{43}
$$

from which the flux term $\mathbb{H}$ can be computed based on (24). Motivated by density functional theory (DFT) calculations [90], the initial diffusion coefficient $D_{\text {diff }}^{0}$ for the undamaged body is considered to be concentration dependent in the numerical simulations presented in Section 5, and in future works even a damage dependent diffusion coefficient $D_{\text {diff }}$ could be introduced to allow the diffusion coefficient to reach a maximum value $D_{\text {diff }}^{\max }$ once the body is damaged.

#### 2.2.4. Euler equations of the rate-type variational formulation
Based on the previous specifications, the continuous rate potential density introduced in (13) reads
$$
\begin{aligned}
\pi\left(\nabla \boldsymbol{\varphi}, \mu, \mathbb{M}, \dot{d}, \dot{\boldsymbol{\xi}}_{\mathbb{C}}, \boldsymbol{\xi}_{\tilde{\mathbb{8}}}\right)= & \left(\partial_{\boldsymbol{h}^{e}} \psi \boldsymbol{F}^{-T}\right): \nabla \boldsymbol{\varphi}+\left(-\partial_{\boldsymbol{h}^{e}} \psi+\boldsymbol{\tau}\right): \boldsymbol{l}^{p}+\left(\partial_{c} \psi-\mu\right) \dot{c}+\left(\beta^{f}+\partial_{d} \psi\right) \dot{d} \\
& -\lambda_{p} f_{\text {plas }}(\boldsymbol{\tau})-\lambda_{f}\left(\beta^{f}-g_{c} \delta_{d} \gamma\right)-\phi_{\text {diff }}.
\end{aligned}
\tag{44}
$$

The Euler equations are obtained by taking variations of (12) at the given state $\{\boldsymbol{\varphi}, d, \boldsymbol{\xi}_{\mathbb{C}}\}$:

<table>
<tbody>
<tr>
<td>(i)</td>
<td>$\delta_{\boldsymbol{\varphi}} \Pi \equiv \mathrm{Div}[\partial_{\boldsymbol{h}^{e}} \psi \boldsymbol{F}^{-T}]+\rho_{0} \boldsymbol{\gamma}=\boldsymbol{0}$</td>
</tr>
<tr>
<td>(ii)</td>
<td>$\delta_{\dot{c}} \Pi \equiv \mu-\partial_{c} \psi=0$</td>
</tr>
<tr>
<td>(iii)</td>
<td>$\delta_{\mu} \Pi \equiv \dot{c}+\mathrm{Div}[\partial_{\mathbb{M}} \phi_{\text {diff }}]=0$</td>
</tr>
<tr>
<td>(iv)</td>
<td>$\delta_{\dot{d}} \Pi \equiv \beta^{f}+\partial_{d} \psi=0$</td>
</tr>
<tr>
<td>(v)</td>
<td>$\delta_{\beta^{f}} \Pi \equiv \dot{d}-\lambda_{f}=0$</td>
</tr>
<tr>
<td>(vi)</td>
<td>$\delta_{\lambda_{f}} \Pi \equiv(\beta^{f}-g_{c} \delta_{d} \gamma) \leq 0, \quad \lambda_{f} \delta_{\lambda_{f}} \Pi \equiv \lambda_{f}(\beta^{f}-g_{c} \delta_{d} \gamma)=0, \quad \lambda_{f} \geq 0$</td>
</tr>
<tr>
<td>(vii)</td>
<td>$\delta_{\boldsymbol{C}^{p}} \Pi \equiv(\boldsymbol{\tau}-\partial_{\boldsymbol{h}^{e}} \psi): \partial_{\dot{\boldsymbol{C}}^{p}} \boldsymbol{l}^{p}=\boldsymbol{0} \quad \text { or } \quad \delta_{\boldsymbol{l}^{p}} \Pi \equiv \boldsymbol{\tau}-\partial_{\boldsymbol{h}^{e}} \psi=\boldsymbol{0}$</td>
</tr>
<tr>
<td>(viii)</td>
<td>$\delta_{\dot{\boldsymbol{\tau}}} \Pi \equiv-\frac{1}{2}(\mathcal{L}_{v} \boldsymbol{b}^{e}) \boldsymbol{b}^{e-1}-\lambda_{p} \partial_{\boldsymbol{\tau}} f_{\text {plas }}=\boldsymbol{0}$</td>
</tr>
<tr>
<td>(ix)</td>
<td>$\delta_{\lambda_{p}} \Pi \equiv f_{\text {plas }} \leq 0, \quad \lambda_{p} \delta_{\lambda_{p}} \Pi \equiv \lambda_{p} f_{\text {plas }}=0, \quad \lambda_{p} \geq 0$</td>
</tr>
</tbody>
</table>
(45)

along with the boundary conditions defined in (6). Here, $(45)_{(i)}$ and $(45)_{(iii)}$ are the balance of linear momentum and the balance of species conservation equations, respectively. $(45)_{(ii)}$ denotes an implicit form for the chemical potential $\mu$. The evolution equation for the damage field is given in $(45)_{(v)}$ satisfying the crack irreversibility condition $(45)_{(vi)}$ along with the constitutive relation for the driving force $(45)_{(iv)}$. $(45)_{(viii)}$ describes the Eulerian flow rule for the plastic internal variable $\boldsymbol{C}^{p}$ together with the loading/unloading conditions $(45)_{(ix)}$ and the constitutive stress relation $(45)_{(vii)}$.

## 3. Discrete variational framework for diffusion induced elasto-plastic deformation and phase field fracture

In this section, we derive the discrete version of the continuous variational framework defined in Section 2. Section 3.1 defines a time-discrete counterpart of the previously introduced rate-type functional. The condensation of local fields in Section 3.2 motivates the definition of a reduced functional in Section 3.3 that forms a basis for the set of equations that are subsequently discretized by finite elements in the context of a staggered scheme in Section 3.4.

### 3.1. Time discretization scheme
For the mixed variational framework and rate-type potentials described in Section 2.2, we consider a discrete time interval $[t_{n}, t]$ with a time increment $\Delta t=t-t_{n}>0$. Constitutive state variables are denoted as $\{\boldsymbol{\varphi}_{n}, d_{n}, \boldsymbol{\xi}_{\mathbb{C}, n}\}$ at time step $t_{n}$, which are assumed to be known, and the primary fields $\{\boldsymbol{\varphi}, d, \mu, \boldsymbol{\xi}\}$ at time step $t$ without the subscripts, which will be determined based on the discrete variational framework where we introduce $\boldsymbol{\xi}=\boldsymbol{\xi}_{\mathbb{C}} \cup \boldsymbol{\xi}_{\tilde{\mathbb{8}}}$. A modified functional is defined in terms of a mixed incremental variational principle
$$
\Pi^{\Delta}(\boldsymbol{\varphi}, \mu, d, \boldsymbol{\xi})=\mathscr{E}^{\Delta}(\boldsymbol{\varphi}, d, \boldsymbol{\xi}_{\mathbb{C}})+\mathscr{D}^{\Delta}(\mu, d, \boldsymbol{\xi})-\mathscr{W}_{\text {ext }}^{\boldsymbol{\varphi}, \mu}(\boldsymbol{\varphi}, \mu ; t)
\tag{46}
$$

where $\mathscr{E}^{\Delta}$ denotes the incremental energy functional, $\mathscr{D}^{\Delta}$ the dissipative work functional, and $\mathscr{W}_{\text{ext}}^{\boldsymbol{\varphi}, \mu}$ the external work functional. Equation (46) can be written in the form

$$
\Pi^{\Delta}(\boldsymbol{\varphi}, \mu, d, \boldsymbol{\xi})=\int_{\mathscr{B}_{0}} \pi^{\Delta}(\nabla \boldsymbol{\varphi}, \mu, \mathbb{M}, d, \boldsymbol{\xi}) d V-\mathscr{W}_{\text{ext}}^{\boldsymbol{\varphi}, \mu}(\boldsymbol{\varphi}, \mu)
\tag{47}
$$

with the mixed internal incremental potential density per unit volume

$$
\pi^{\Delta}(\nabla \boldsymbol{\varphi}, \mu, \mathbb{M}, d, \boldsymbol{\xi})=\operatorname{Algo}\left\{\int_{t_{n}}^{t} \pi(\nabla \dot{\boldsymbol{\varphi}}, \mu, \mathbb{M}, \dot{d}, \dot{\boldsymbol{\xi}}_{\mathbb{C}}, \dot{\boldsymbol{\xi}}_{\tilde{\delta}}) d t\right\}.
\tag{48}
$$

In the context of an algorithmic treatment of isotropic finite strain elasto-plasticity an exact update of the Eulerian flow rule (45)$_{(viii)}$ may be derived in line with the update formulation outlined in [91, 92] that is identical to the return mapping of the infinitesimal theory. It can be written in the material description as

$$
\dot{\boldsymbol{C}}^{p-1}=\left[-2 \lambda_{p} \boldsymbol{C}^{-1} \boldsymbol{N}_{p}\right] \boldsymbol{C}^{p-1}
\tag{49}
$$

where $\boldsymbol{N}_{p}=\boldsymbol{F}^{T} \partial_{\tau} f_{\text{plas}}(\boldsymbol{\tau}) \boldsymbol{F}$ is the pull-back of the normal $\partial_{\tau} f_{\text{plas}}(\boldsymbol{\tau})$ to the reference configuration. The exponential approximation to (49) within the interval $[t_{n}, t]$ can be recast as

$$
\boldsymbol{C}^{p-1}=\exp \left[-2 \Delta \gamma_{p} \boldsymbol{C}^{-1} \boldsymbol{N}_{p}\right] \boldsymbol{C}_{n}^{p-1}
\tag{50}
$$

with the incremental plastic parameter $\Delta \gamma_{p}=(t-t_{n}) \lambda_{p}$. The push-forward to the current configuration and the identification of the trial value $\boldsymbol{b}^{e *}=J_{c}^{-2 / 3} \boldsymbol{F} \boldsymbol{C}_{n}^{p-1} \boldsymbol{F}^{T}$ yields the update

$$
\boldsymbol{b}^{e}=\exp \left[-2 \Delta \gamma_{p} \partial_{\tau} f_{\text{plas}}(\boldsymbol{\tau})\right] \boldsymbol{b}^{e *}.
\tag{51}
$$

The unique spectral decomposition of the Kirchhoff stress $\boldsymbol{\tau}$, the elastic left Cauchy-Green tensor $\boldsymbol{b}^{e}$ and its trial value $\boldsymbol{b}^{e *}=\sum_{A=1}^{n_{\text{dim}}}(\lambda_{A}^{*})^{2} \boldsymbol{n}_{A} \otimes \boldsymbol{n}_{A}$ due to their coaxiality for a restriction to isotropy motivates a return mapping algorithm at fixed principal axis, that is,

$$
\left(\lambda_{A}^{e}\right)^{2}=\exp \left[-2 \Delta \gamma_{p} \partial_{\tau_{A}} f_{\text{plas}}(\boldsymbol{\tau})\right]\left(\lambda_{A}^{e *}\right)^{2}.
\tag{52}
$$

Exploitation of the coaxiality allows further to rewrite the logarithmic elastic strains defined in (35) in additive form

$$
\boldsymbol{h}^{e}=\boldsymbol{h}^{e *}-\Delta \gamma_{p} \partial_{\tau} f_{\text{plas}} \quad \text{with} \quad \boldsymbol{h}^{e *}=\frac{1}{2} \log \left[\boldsymbol{b}^{e *}\right]
\tag{53}
$$

with the representations $\boldsymbol{h}^{e}=\sum_{A=1}^{n_{\text{dim}}}(\log \lambda_{A}) \boldsymbol{n}_{A} \otimes \boldsymbol{n}_{A}$ and $\boldsymbol{h}^{e *}=\sum_{A=1}^{n_{\text{dim}}}(\log \lambda_{A}^{*}) \boldsymbol{n}_{A} \otimes \boldsymbol{n}_{A}$. The incremental mixed potential density defined in (48) reads hence in algorithmic form

$$
\begin{aligned}
\pi^{\Delta}(\nabla \boldsymbol{\varphi}, \mu, \mathbb{M}, d, \boldsymbol{\xi}) & =\psi\left(\boldsymbol{h}^{e}, d, c\right)+\boldsymbol{\tau}:\left(\boldsymbol{h}^{e *}-\boldsymbol{h}^{e}\right)+\beta^{f}\left(d-d_{n}\right)-\mu\left(c-c_{n}\right) \\
& -\Delta \gamma_{p} f_{\text{plas}}(\boldsymbol{\tau})-\Delta t \phi_{\text{diff}}(\mathbb{M} ; \boldsymbol{F}_{n}, c_{n}, d_{n})-\Delta \gamma_{f}\left(\beta^{f}-g_{c} \delta_{d} \gamma(d, \nabla d)\right)
\end{aligned}
\tag{54}
$$

with the incremental fracture parameter $\Delta \gamma_{f}=(t-t_{n}) \lambda_{f}$.

### 3.2. Condensation of local fields

Due to the local structure of the incremental problem, in an algorithmic treatment $\boldsymbol{\xi}$ can be obtained locally for given global fields $\{\boldsymbol{\varphi}, \mu, d\}$ by means of a local stationary problem

$$
\{\boldsymbol{\xi}\}=\arg \left\{\underset{\boldsymbol{\xi}}{\operatorname{stat}} \pi^{\Delta}(\nabla \boldsymbol{\varphi}, \mu, \mathbb{M}, d, \boldsymbol{\xi})\right\}
\tag{55}
$$

for admissible variations $\delta \lambda_{p} \geq 0, \delta \lambda_{f} \geq 0, \delta c \in L^{2}, \delta \beta^{f} \in L^{2}, \delta C^{p} \in L^{2}$ and $\delta \tau \in L^{2}$, resulting in the local equations:

$$
\begin{aligned}
(i) \quad \delta_{c} \pi^{\Delta} & \equiv \mu-\partial_{c} \psi=0 \\
(i i) \quad \delta_{\beta^{f}} \pi^{\Delta} & \equiv d-d_{n}-\Delta \gamma_{f}=0 \\
(i i i) \quad \delta_{\lambda_{f}} \pi^{\Delta} & \equiv\left(\beta^{f}-g_{c} \delta_{d} \gamma\right) \leq 0, \quad \lambda_{f} \delta_{\lambda_{f}} \pi^{\Delta} \equiv \lambda_{f}\left(\beta^{f}-g_{c} \delta_{d} \gamma\right)=0, \quad \lambda_{f} \geq 0 \\
(i v) \quad \delta_{C^{p}} \pi^{\Delta} & \equiv\left[\boldsymbol{\tau}-\partial_{\boldsymbol{h}^{e}} \psi\right]: \partial_{C^{p}} \boldsymbol{h}^{e}=0 \\
(v) \quad \delta_{\boldsymbol{\tau}} \pi^{\Delta} & \equiv \boldsymbol{h}^{e *}-\boldsymbol{h}^{e}-\Delta \gamma_{p} \partial_{\boldsymbol{\tau}} f_{\text {plas }}=0 \\
(v i) \quad \delta_{\lambda_{p}} \pi^{\Delta} & \equiv f_{\text {plas }} \leq 0, \quad \lambda_{p} \delta_{\lambda_{p}} \pi^{\Delta} \equiv \lambda_{p} f_{\text {plas }}=0, \quad \lambda_{p} \geq 0
\end{aligned}
\tag{56}
$$

Note that all the equations in (56) are linear with the exception of $(56)_{(i)}$ which algorithmically is solved by a local Newton update scheme (see Table 1).

### 3.3. Reduced global variational principle
The local stationary principle (55) allows us to define a reduced incremental potential density
$$
\pi_{\mathrm{red}}^{\Delta}(\nabla \boldsymbol{\varphi}, \mu, \mathbb{M}, d)=\underset{\boldsymbol{\xi}}{\operatorname{stat}} \pi_{\mathrm{red}}^{\Delta}(\nabla \boldsymbol{\varphi}, \mu, \mathbb{M}, d, \boldsymbol{\xi})
\tag{57}
$$
associated with a reduced three field potential
$$
\Pi_{\mathrm{red}}^{\Delta}(\boldsymbol{\varphi}, \mu, d)=\int_{\mathscr{B}_{0}} \pi_{\mathrm{red}}^{\Delta}(\nabla \boldsymbol{\varphi}, \mu, \mathbb{M}, d) d V-\mathscr{W}_{\mathrm{ext}}^{\boldsymbol{\varphi}, \mu}(\boldsymbol{\varphi}, \mu ; t).
\tag{58}
$$

The solution of the global fields is hence obtained from the saddle point problem
$$
\{\boldsymbol{\varphi}, \mu, d\}=\arg \left\{\inf _{\boldsymbol{\varphi}} \sup _{\mu} \inf _{d} \Pi_{\mathrm{red}}^{\Delta}(\boldsymbol{\varphi}, \mu, d)\right\}.
\tag{59}
$$

Taking variations of (59), we obtain the weak form of the relevant set of governing equations, i.e.
$$
\begin{aligned}
D \Pi_{\mathrm{red}}^{\Delta}[\delta \boldsymbol{\varphi}] & =\int_{\mathscr{B}_{0}} D \psi[\delta \boldsymbol{\varphi}] d V-D \mathscr{W}_{\mathrm{ext}}^{\boldsymbol{\varphi}}[\delta \boldsymbol{\varphi}]=0 \\
D \Pi_{\mathrm{red}}^{\Delta}[\delta \mu] & =\int_{\mathscr{B}_{0}}\left\{-\left(c-c_{n}\right) \delta \mu-\Delta t D \phi_{\mathrm{diff}}[\delta \mu]\right\} d V-D \mathscr{W}_{\mathrm{ext}}^{\mu}[\delta \mu]=0 \\
D \Pi_{\mathrm{red}}^{\Delta}[\delta d] & =\int_{\mathscr{B}_{0}}\left\{D \psi[\delta d]+g_{c} \delta_{d} \gamma \delta d\right\} d V=0
\end{aligned}
\tag{60}
$$
where for a generic field $\boldsymbol{\eta}$ and a functional $\Theta$,
$$
D \Theta[\delta \boldsymbol{\eta}] \equiv \frac{d}{d \epsilon}\left\{\left.\Theta(\boldsymbol{\eta}+\epsilon \delta \boldsymbol{\eta})\right\}\right|_{\epsilon=0}
\tag{61}
$$
denotes the Gateaux derivative in the direction $\delta \boldsymbol{\eta}$. Hence,
$$
\begin{aligned}
D \Pi_{\mathrm{red}}^{\Delta}[\delta \boldsymbol{\varphi}] & =\int_{\mathscr{B}_{0}}\left\{\left(\partial_{\boldsymbol{h}^{e}} \psi \boldsymbol{F}^{-T}\right): \delta \boldsymbol{F}-\rho_{0} \boldsymbol{\gamma} \cdot \delta \boldsymbol{\varphi}\right\} d V-\int_{\partial \mathscr{B}_{0}^{t}} \overline{\boldsymbol{T}} \cdot \delta \boldsymbol{\varphi} d A=0 \\
D \Pi_{\mathrm{red}}^{\Delta}[\delta \mu] & =\int_{\mathscr{B}_{0}}\left\{-\left(c-c_{n}\right) \delta \mu+\Delta t \mathbb{H} \cdot \nabla \delta \mu\right\} d V+\int_{\partial \mathscr{B}_{0}^{t}} \Delta t \bar{H} \delta \mu d A=0 \\
D \Pi_{\mathrm{red}}^{\Delta}[\delta d] & =\int_{\mathscr{B}_{0}}\left\{\frac{\partial \psi}{\partial d} \delta d+g_{c} \delta_{d} \gamma \delta d\right\} d V=0
\end{aligned}
\tag{62}
$$
with the variations satisfying the requirements $\delta \boldsymbol{\varphi} \in \mathcal{W}_{0}^{\boldsymbol{\varphi}}=\left\{\delta \boldsymbol{\varphi} | \delta \boldsymbol{\varphi}=0\right.$ on $\left.\partial \mathscr{B}_{0}^{\boldsymbol{\varphi}}\right\}$ and $\delta \mu \in \mathcal{W}_{0}^{\mu}=\left\{\delta \mu | \delta \mu=0\right.$ on $\left.\partial \mathscr{B}_{0}^{\mu}\right\}$ as well as $\delta d=0$ on the entire boundary. The weak equations in (62) provide the starting point for setting up the discretized formulation for $\{\boldsymbol{\varphi}, \mu, d\}$. The set of equations is supplemented by the local Euler equations (56) that define the local fields $\boldsymbol{\xi}$ in terms of the global fields $\{\boldsymbol{\varphi}, \mu, d\}$.

### 3.4. Staggered spatial discretization scheme

During the loading process $\dot{d}>0$ we have $2(1-d) \psi_{\text {elas }}^{+}=g_{c} \delta_{d} \gamma$, and during unloading $\dot{d}=0$ we have $2(1-d) \psi_{\text {elas }}^{+} \leq$ $g_{c} \delta_{d} \gamma$. Following [48], a local history field of the crack driving force is introduced as

$$
\mathcal{H}(\boldsymbol{X}, t)=\max _{s \in[0, t]}\left(\psi_{\text {elas }}^{+}(\nabla \boldsymbol{\varphi}, \boldsymbol{\xi})\right)
$$

where $\mathcal{H}$ is the maximal attained value of $\psi_{\text {elas }}^{+}(\nabla \boldsymbol{\varphi}, \boldsymbol{\xi})$. Replacing the crack driving force $\psi_{\text {elas }}^{+}$with the newly intro- duced driving force $\mathcal{H}$ ensures $\dot{d} \geq 0$, and allows us to recast the crack irreversibility condition (28) into

$$
2(1-d) \mathcal{H}=g_{c} \delta_{d} \gamma
$$

serving as the evolution equation of the damage field $d$. The introduction of the history field $\mathcal{H}$ to recast the crack irreversibility condition allows us to solve the problem in a staggered manner, where the damage field $\{d\}$ is solved first, followed by the computation of the other global fields $\{\boldsymbol{\varphi}, \mu\}$. Following [48], at the current time step $t$, we first update the history field $\mathcal{H}$ as

$$
\mathcal{H}= \begin{cases}\psi_{\text {elas }}^{+}\left(\nabla \boldsymbol{\varphi}_{n}, \boldsymbol{\xi}_{n}\right) & \text { for } \psi_{\text {elas }}^{+}\left(\nabla \boldsymbol{\varphi}_{n}, \boldsymbol{\xi}_{n}\right)>\mathcal{H}_{n} \\ \mathcal{H}_{n} & \text { otherwise }\end{cases}
$$

with $\mathcal{H}_{0}=\mathcal{H}\left(\boldsymbol{X}, t=t_{0}\right)=0$ as the initial condition. Since the history variable $\mathcal{H}$ is determined based on the state variables at time $t_{n}$, it is constant in the time interval $\left[t_{n}, t\right]$. Thus, to obtain $\{d\}$, we introduce the algorithmic potential

$$
\Pi_{\text {red }}^{\Delta}(d)=\int_{\mathcal{B}_{0}}\left[g_{c} \gamma(d, \nabla d)+(1-d)^{2} \mathcal{H}\right] d V
$$

with $\gamma$ as the crack surface density function given in (30). The damage field $\{d\}$ at time $t$ is obtained from the incremental stationary principle

$$
\{d\}=\arg \left\{\inf _{d} \Pi_{\text {red }}^{\Delta}(d)\right\} .
$$

Next, we discretize the body $\mathcal{B}_{0}$ into $n_{\text {elem }}$ finite elements $\mathcal{B}_{0}^{e}$ with $n_{\text {node }}$ nodal points. The field variables $\{\boldsymbol{\varphi}, \mu, d\}$ are approximated as $\boldsymbol{\varphi}^{\mathrm{h}}=\boldsymbol{N}_{\boldsymbol{\varphi}} \boldsymbol{d}_{\boldsymbol{\varphi}}, \mu^{\mathrm{h}}=\boldsymbol{N}_{\mu} \boldsymbol{d}_{\mu}, d^{\mathrm{h}}=\boldsymbol{N}_{d} \boldsymbol{d}_{d}$ in terms of standard shape functions and their nodal values. The material gradients $\{\nabla \mu, \nabla d\}$ are approximated as $\nabla \mu^{\mathrm{h}}=\boldsymbol{B}_{\mu} \boldsymbol{d}_{\mu}, \nabla d^{\mathrm{h}}=\boldsymbol{B}_{d} \boldsymbol{d}_{d}$ and the spatial gradient of the deformation field is approximated as $\nabla_{x} \boldsymbol{\varphi}^{\mathrm{h}}=\boldsymbol{b}_{\boldsymbol{\varphi}} \boldsymbol{d}_{\boldsymbol{\varphi}}$, all given in terms of standard B-operator matrices. Employing a Bubnov-Galerkin scheme, all their variations are approximated the same way.

The discretized residual function for the phase field $\left\{d^{\mathrm{h}}\right\}$ is then being determined from the weak form $(62)_{3}$ as

$$
\boldsymbol{R}_{\mathrm{d}}=\bigwedge_{e}^{n_{\text {elem }}} \int_{\mathcal{B}_{0}^{e}}\left\{\boldsymbol{N}_{d}^{T}\left[g_{c} \frac{1}{l} d-2(1-d) \mathcal{H}\right]+g_{c} l \boldsymbol{B}_{d}^{T} \nabla d\right\} d V=\boldsymbol{0}
$$

from which the result for $\left\{d^{\mathrm{h}}\right\}$ at time $t$ is obtained through a standard Newton procedure. From the solution of $\left\{d^{\mathrm{h}}\right\}$ computed from (68), we continue to solve for the remaining global fields. For a given chemical potential $\mu$, the concentration variable $c$ is recovered at the integrating points based on a local Newton procedure [75,93]. The internal variable $C^{p}$ is updated based on the von-Mises plasticity return mapping algorithm at finite deformations [91]. Those parameters are obtained on the element level as soon as the convergence criterion is met. Knowing $\left\{c, C^{p}\right\}$, the discretized residual functions for $\{\boldsymbol{\varphi}, \mu\}$ are determined from the weak equations $(62)_{1}$ and $(62)_{2}$ as

$$
\begin{aligned}
& \boldsymbol{R}_{\boldsymbol{\varphi}}=\bigwedge_{e}^{n_{\text {elem }}} \int_{\mathcal{B}_{0}^{e}}\left(\boldsymbol{b}_{\boldsymbol{\varphi}}^{T} \boldsymbol{\tau}-\rho_{0} \boldsymbol{N}_{u}^{T} \boldsymbol{\gamma}\right) d V-\bigwedge_{e}^{n_{\text {elem }}} \int_{\partial \mathcal{B}_{0}^{e, t}} \boldsymbol{N}_{u}^{T} \overline{\boldsymbol{T}} d A=\boldsymbol{0} \\
& \boldsymbol{R}_{\mu}=\bigwedge_{e}^{n_{\text {elem }}} \int_{\mathcal{B}_{0}^{e}}\left(-\boldsymbol{N}_{\mu}^{T}\left(c-c_{n}\right)+\Delta t \boldsymbol{B}_{\mu}^{T} \mathbb{H}\right) d V+\bigwedge_{e}^{n_{\text {elem }}} \int_{\partial \mathcal{B}_{0}^{c, h}} \Delta t \boldsymbol{N}_{\mu}^{T} \bar{H} d A=\boldsymbol{0}
\end{aligned}
$$

from which the result for $\{\boldsymbol{\varphi}, \mu\}$ at time $t$ is obtained through a standard Newton procedure.

![](./images/814520538939523073_5.jpg)

Figure 4: Illustration of the two-phase lithiation process in the Si electrodes. The lithiated region and unlithiated Si core are separated by an evident phase boundary. For the lithiated region $Li_xSi$, the lithium diffusion coefficient $D_{diff}$ equals to $D_{diff}^0$, which is the actual lithium diffusion coefficient in Si. For unlithiated Si core, the lithium diffusion coefficient $D_{diff}$ equals to $D_{diff}^s$, which is assumed to be zero in the simulation part.

## 4. Account for two-phase lithiation

During the initial lithiation process, c-Si and a-Si both undergo two-phase lithiation and are transformed to an amorphous $Li_xSi$ alloy, separated by a phase boundary, which attributes to the tensile hoop stress state and the appearance of surface cracks of Si electrodes [3, 5]. Experimental investigations and theoretical models further show that the different chemical reaction rates in different crystalline directions at the phase boundary cause an anisotropic deformation of Si electrodes [94, 95]. This observation further raises the complexity when modeling diffusion induced large plastic deformation and phase field fracture of Si electrodes. To capture this unique two-phase lithiation process, we will show how to account for the two-phase lithiation in the presence of a sharp reaction front by incorporating our recently proposed reaction-controlled diffusion model [87] into the variational framework of this work.

### 4.1. A reaction-controlled diffusion model

According to experimental observations [8, 9], a sharp phase boundary exists between the lithiated region and the Si core. To simplify the illustration in Fig. 4, we isolate the two-phase lithiation process described in this section from the above variational framework of the chemo-mechanical coupled initial boundary value problem. The lithiated $Li_xSi$ region differs from the Si core as a different value of Li concentration $c$ is present in the two domains. The sharp phase boundary indicates that only a few Li atoms are able to diffuse across the phase boundary. We neglect this and assume that no Li atoms diffuse across the phase boundary, resulting in $c = 0$ for the Si core. In the simulation, the zero concentration in the Si core is ensured by setting the diffusion coefficient $D_{diff} = 0$ in the Si core. The Li concentration profile is affected mainly by the location of the phase boundary. Therefore, it is of main importance to properly determine the new reaction front location. In this work, the phase boundary is updated through a reaction-controlled diffusion model proposed in [87], which is summarized as follows. First, the reaction rate at the phase boundary is approximated as

$$
v_{\mathrm{r}}=A \exp \left(-\frac{E_{0}+B p}{k_{B} T}\right) f(c) \quad \text { with } \quad B=\frac{\phi_{\mathrm{Si}} V_{\mathrm{Si}}}{2 \cdot 1.60 \cdot 10^{-19}}
$$

where $A, B, E_{0}, k_{B}, T, p$ are the frequency-related factor, the volume-related parameter, the bond-breaking energy barrier, the Boltzmann constant, the absolute temperature, and the hydrostatic pressure at the reaction front. The volume parameter $B$ is approximated by the Si-Si bond fraction $\phi_{\mathrm{Si}}$ and Si's atomistic volume $V_{\mathrm{Si}}$. The coefficient $2 \cdot 1.60 \cdot 10^{-19}$ in the denominator guarantees that $B p$ represents the bond energy change of a single Si-Si bond with a unit of electronvolt (eV). The reaction model $f(c)$ in (70) has the form

$$
f(c)=\frac{1}{1+\exp \left(C\left(c_{0}-c\right)\right)} \quad \text { for } \quad c>0
$$

![](./images/814520538939523073_6.jpg)

Figure 5: Illustration of the reaction front updating scheme. Consider a simple discrete geometry with 13 nodes, 19 edges, and an initial reaction front (indicated by the red bold line). Each node is assigned with a flag to indicate its lithiated state. A value of (0) (not shown here) means that the node is located in the unlithiated region. For the lithiated region, we use (-1) for nodes on front edges (marked with black bold lines) and (1) otherwise. Front edges are those that intersect the reaction front and have nodes with a flag of (0) and (-1). A local coordinate $s \in [0, 1]$ for each front edge is used to determine the exact reaction front location. The reaction front is assumed to propagate along the direction of $\nabla c$ (assumed vertically downwards here) with distances predicted by the reaction controlled diffusion model. To update the new reaction front locations, we create a list of front edges and associate with each a forwarding distance $\Delta r$, as shown in (a). No update is performed for edges with a zero forwarding distance. For those being updated, the new reaction front locations either stay on the existing front edges (edges $e_4$, $e_5$), or move to different edges (edges $e_6$, $e_7$). (b) For edge $e_5$, project its associated distance $\Delta r_5$ onto edge $e_5$ and update the local coordinate $s_5$ to indicate the new reaction front location. The forwarding distance associated with edge $e_5$ is then updated to zero. For edge $e_6$, we obtain the new reaction front location in two steps. First, see (b), project $\Delta r_6$ onto edge $e_6$ and update the local coordinate to $s_6 = 1$ to indicate a temporary reaction front location at node 7. Update nodal flags for nodes 3 and 7 to (1) and (-1), respectively, remove edge $e_6$ from the front edge list but add edges $e_{9-11}$. Second, see (c), a forwarding distance of $\Delta r_9 = \Delta r_{10} = \Delta r_{11} = \Delta r_{9-11}$ in the direction of $\nabla c$ is assigned and projected onto edges $e_{9-11}$. The local coordinates $s_9$ and $s_{10}$ are updated to indicate the new reaction front location and the forwarding distances associated with edges $e_9$, $e_{10}$ are set to zero. The local coordinate $s_{11} = 0$ is not updated since the projection $\Delta r_{11}$ does not intersect edge $e_{11}$. The local coordinate $s_{11}$ is updated when updating edge $e_7$. (d) Once all front edges are updated the new reaction front location is obtained.

with $c_0$ as the threshold value of Li concentration at the reaction front to break the Si-Si covalent bond and $C$ as a scalar scaling parameter. As stated in [87], compressive stresses (positive hydrostatic pressure) will increase the reaction energy barrier and slow down the reaction rate, and tensile stresses (negative hydrostatic pressure) will decrease the energy barrier and accelerate the reaction rate. In (70), the concentration $c$ and the hydrostatic pressure $p$ at the reaction front are the input variables. Rather than using a given heuristic dependency of the pressure on the reaction front location, as done in our previous work [87], $p$ is determined by solving the governing equations (45) in this work. Then $v_r$ in (70) can be computed at the reaction front, from which the reaction front moving distance $\Delta r$ in a time step $dt$ follows as

$$
v_{\mathrm{r}} j d a d t=\Delta r d a c_{0} c_{\max }. \tag{72}
$$

Here, $j$ (number of Li particles/(area·time)) is the Li flow at the reaction front, $c_{\max}$ is the maximum concentration of Li in Si, and $da$ is the differential area at the reaction front. Also, $j\ da\ dt$ represents the total number of Li particles which can potentially diffuse across the reaction front so that $v_{\mathrm{r}} j\ da\ dt$ predicts the number of reacted Li particles. Based on the assumption that the reacted Li particles in the newly formed lithiated region must reach a minimum concentration level $c_0$ to break the Si-Si bond, the term $\Delta r\ da\ c_0\ c_{\max}$ also approximates the total number of reacted Li particles [87]. Thus, based on the reaction front moving distance $\Delta r$ computed from (72), the new reaction front location is updated as $r^{\text{new}} = r^{\text{old}} - \Delta r$.

As show in Fig. 1, the initial lithiation of crystalline Si electrodes results in a highly anisotropic deformation, lead-ing to crack initiation between neighboring $\langle 110 \rangle$ lateral planes [7]. DFT simulations [96] show that this anisotropic deformation behavior is caused by different bond-breaking energy barriers at different crystalline directions. Since the bond-breaking energy barrier $E_0$ is one input parameter of this reaction-controlled diffusion model, we are able

to predict the anisotropic deformation behavior of c-Si by simply considering different bond-breaking energy barriers for different crystalline directions. The importance of the consideration of the phase boundary on the Li concentration profile, stress evolution, and crack initiation will be demonstrated in the numerical examples in Section 5.

### 4.2. Update of the reaction front location
Having computed the solution $\{\boldsymbol{\varphi}, \mu, d, c\}$ at time $t$, we can now update the reaction front location based on the reaction controlled diffusion model summarized in Section 4.1. Even though the procedure is explained for two- dimensional problems, in which the reaction front is a line, the overall procedure conceptually can be extended to three-dimensional problems.

To compute the reaction rate in (70), we create three arrays in which we store the results obtained from Section 3.4 for the hydrostatic pressure $p$, the Li concentration $c$, and the concentration gradient $\nabla c$ at the reaction front. Based on the solution of the concentration $c$ at $t$, a trial diffusion process is carried out in which the presence of the reaction front is initially neglected. The result is then used to approximate the Li flow $j$ at the reaction front. The value of $j$ is determined based on the total amount of Li atoms that diffuse into the unlithiated Si core in this trial process. Next, the reaction-controlled diffusion model is used to approximate the new reaction front location based on the bond-breaking energy barrier $E_{0}$. For c-Si, the value of $E_{0}$ is only available for specific crystalline directions, but the concentration gradient is not always aligned with those. Thus, we must approximate the reaction front moving velocity based on the available values for $E_{0}$ in the $\langle 100\rangle$ and $\langle 110\rangle$ directions. In the numerical simulation performed in Section 5, for each reaction front location, based on $p$ and $c$ at that front location, we compute two velocities, $v_{\langle 100\rangle}$ for the $\langle 100\rangle$ direction and $v_{\langle 110\rangle}$ for the $\langle 110\rangle$ direction. We then approximate the actual velocity for that location in the direction of the stored value of the concentration gradient $\nabla c$ based on a linear interpolation between $v_{\langle 100\rangle}$ and $v_{\langle 110\rangle}$. Doing so allows us to predict the expected anisotropic deformation during the (de)lithiation process. With the computed reaction front forwarding distance $\Delta r$ in the direction of $\nabla c$, the reaction front locations are updated. The updating procedure, which is mesh-insensitive, is illustrated in Fig. 5 for a simple reaction front geometry.

Finally, a summary of the overall solution procedure, combining the two-phase lithiation treatment of Section 4 with the discrete variational framework for diffusion induced elasto-plastic deformation and phase field fracture is provided in Table 1.

## 5. Representative numerical examples
In this section, we carry out several numerical simulations to demonstrate the performance of the proposed vari- ational framework and the importance of considering the reaction front in this chemo-mechanical coupled fracture problem. All the material parameters that are used in the numerical simulation part for this chemo-mechanical cou- pled fracture problem are summarized in Table 2. We restrict ourselves to $n_{dim}=2$ in this paper, but the extension to 3D is conceptually straightforward. Experimental results reveal a diffusion induced anisotropic deformation and a crystalline direction dependent fracture behavior for $\langle 100\rangle$ and $\langle 110\rangle$ c-Si nanopillars [7], as shown in Fig. 6(a) and Fig. 10(a). To show that our computational framework is capable of capturing diffusion induced anisotropic defor-mation and the crystalline direction dependent fracture behavior, we investigate the initial lithiation process for $\langle 100\rangle$  c-Si nanopillars in Section 5.1 and $\langle 110\rangle$ c-Si nanopillars in Section 5.2. In Section 5.3, we show how multiple cracks form and propagate in a realistic irregular Si electrode. Finally, we investigate the lithiation process of a constrained(110) c-Si nanopillar and show how geometric constraints affects the fracture behavior of Si electrodes in Section 5.4.

### 5.1. Diffusion induced anisotropic deformation and fracture of $\langle 100\rangle$ crystalline silicon nanopillars
We start investigating diffusion induced large plastic deformation under the presence of the reaction front in(110) c-Si nanopillars initially without considering damage in Section 5.1.1 and thereby calibrate the concentration dependent diffusion coefficient. Damage is considered in Section 5.1.2, where we study diffusion induced fracture. We model one quarter of the circular nanopillar geometry with 11638 Q1 elements under plane strain, where the field variables $\{\varphi, \mu, d\}$ are approximated with standard linear shape functions, and the mechanical boundary conditions shown in Fig. 6(b). In all simulations, an initial chemical potential $\mu_{0}=-11.5 ~J / mol$ (equivalent to $c_{0}=0.01$ ) is applied throughout the electrode. The prescribed chemical potential at the outer surface linearly increases from $\mu_{0}$ to $\bar{\mu}=11.5 ~J / mol$ (equivalent to $c=0.99$ ) within the first second and is kept constant for the remainder of the simulation.

Table 1: Summary box of the variational framework to model diffusion induced large plastic deformation and phase field fracture during initial two-phase lithiation of Si electrodes.

A. Initialize the deformation field $\boldsymbol{\varphi}_{n}$, the phase field $d_{n}$, chemical potential $\mu_{n}$, history field $\mathcal{H}_{n}$, and the reaction front location $r_{n}$ at time $t_{n}$. Update the boundary conditions to the current time step $t$.
B. Determine the history variable $\mathcal{H}$ at $t$ in $\mathcal{B}_{0}$:
$$
\mathcal{H}=
\begin{cases}
\psi_{\text{elas}}^{+}(\nabla \boldsymbol{\varphi}_{n}, c_{n}, \boldsymbol{\xi}_{n}) & \text{for } \psi_{\text{elas}}^{+}(\nabla \boldsymbol{\varphi}_{n}, c_{n}, \boldsymbol{\xi}_{n})>\mathcal{H}_{n} \\
\mathcal{H}_{n} & \text{otherwise}
\end{cases}
$$

C. Compute the phase field $d$ at time $t$ through a standard Newton procedure:
$$
\boldsymbol{R}_{d}=\bigwedge_{e}^{n_{\text{elem}}} \int_{\mathcal{B}_{0}^{e}}\left\{\boldsymbol{N}_{d}^{T}\left[g_{c} \frac{1}{l} d-2(1-d) \mathcal{H}\right]+g_{c} l \boldsymbol{B}_{d}^{T} \nabla d\right\} d V=\boldsymbol{0}.
$$

D. Compute the deformation field $\boldsymbol{\varphi}$ and the chemical potential $\mu$ for the fixed phase field $d$ computed from the previous step:
- Compute the local concentration field $c$ at time $t$ for a given chemical potential $\mu$ as
$$
c \Leftarrow c-k_{c}^{-1} r_{c} \quad \text{until} \quad \left|r_{c}\right|<\text{tol}_{c} \quad \text{where} \quad r_{c}=\pi_{, c}^{\Delta}=\partial_{c} \psi-\mu=0 \quad \text{and} \quad k_{c}=\pi_{, c c}^{\Delta}=\partial_{c c} \psi
$$
- The plastic internal variables are updated based on the return mapping algorithm [91] as
$$
\varepsilon_{A}^{e}=\varepsilon_{A}^{e *}-\gamma_{p} \frac{\partial f_{\text{plas}}}{\partial \tau_{A}} \quad \text{with} \quad \varepsilon_{A}^{e}=\log (\lambda_{A}^{e}), \quad \varepsilon_{A}^{e *}=\log (\lambda_{A}^{e *}), \quad A=1, \ldots, n_{\text{dim}}
$$
- Compute the deformation field $\boldsymbol{\varphi}$ and the chemical potential $\mu$ through a standard Newton procedure from
$$
\boldsymbol{R}_{\boldsymbol{\varphi}}=\bigwedge_{e}^{n_{\text{elem}}} \int_{\mathcal{B}_{0}^{e}}\left(\boldsymbol{b}_{\boldsymbol{\varphi}}^{T} \boldsymbol{\tau}-\rho_{0} \boldsymbol{N}_{u}^{T} \boldsymbol{\gamma}\right) d V-\bigwedge_{e}^{n_{\text{elem}}} \int_{\partial \mathcal{B}_{0}^{e, t}} \boldsymbol{N}_{u}^{T} \overline{\boldsymbol{T}} d A=\boldsymbol{0}
$$
$$
\boldsymbol{R}_{\mu}=\bigwedge_{e}^{n_{\text{elem}}} \int_{\mathcal{B}_{0}^{e}}\left(-\boldsymbol{N}_{\mu}^{T}(c-c_{n})+\Delta t \boldsymbol{B}_{\mu}^{T} \mathbb{H}\right) d V+\bigwedge_{e}^{n_{\text{elem}}} \int_{\partial \mathcal{B}_{0}^{e, h}} \Delta t \boldsymbol{N}_{\mu}^{T} \bar{H} d A=\boldsymbol{0}.
$$

E. Update the new reaction front location based on the reaction controlled diffusion model discussed in Section 4:
- Store the concentration value $c$, the concentration gradient $\nabla c$, and the hydrostatic pressure $p$ from step D at the reaction front location.
- Run a trial diffusion process with the solution $\mu$ and $c$ from step D as inputs. Solve $\boldsymbol{R}_{\mu}$ without the presence of the reaction front to approximate the Li flow $j$.
- From the reaction-controlled diffusion model, compute the reaction rate at the reaction front location as
$$
v_{\mathrm{r}}=A \exp \left(-\frac{E_{0}+B p}{k_{B} T}\right) f(c) \quad \text{with} \quad B=\frac{\phi_{\mathrm{Si}} V_{\mathrm{Si}}}{2 \cdot 1.60 \cdot 10^{-19}} \quad \text{and} \quad f(c)=\frac{1}{1+\exp (C(c_{0}-c))} \text{ (for } c>0\text{)}.
$$
For c-Si, a linear interpolation of the reaction rate is performed between $v_{\langle 110\rangle}$ and $v_{\langle 100\rangle}$ based on the orientation difference between the concentration gradient direction and the $\langle 100\rangle$ and $\langle 110\rangle$ crystalline directions.
- Update the new reaction front location $r$ at time $t$ as
$$
r=r_{n}-\Delta r \quad \text{with} \quad v_{\mathrm{r}} j d a d t=\Delta r d a c_{0} c_{\max }.
$$
- Perform the geometric tracking algorithm of the reaction front based on the update scheme summarized in Fig. 5.

Table 2: Summary of material parameters used in Section 5

<table>
<thead>
<tr>
<th>Name</th>
<th>Parameter</th>
<th>Value</th>
<th>Unit</th>
<th>Eqn.</th>
<th>Ref</th>
</tr>
</thead>
<tbody>
<tr>
<td>Young's Modulus (c-Si)</td>
<td>$E$</td>
<td>169</td>
<td>GPa</td>
<td>(37)</td>
<td>[97]</td>
</tr>
<tr>
<td>Poisson's Ratio (c-Si)</td>
<td>$\nu$</td>
<td>0.28</td>
<td>-</td>
<td>(37)</td>
<td>[97]</td>
</tr>
<tr>
<td>Young's Modulus (a-Si)</td>
<td>$E$</td>
<td>80</td>
<td>GPa</td>
<td>(37)</td>
<td>[98]</td>
</tr>
<tr>
<td>Poisson's Ratio (a-Si)</td>
<td>$\nu$</td>
<td>0.22</td>
<td>-</td>
<td>(37)</td>
<td>[98]</td>
</tr>
<tr>
<td>Young's Modulus ($\text{Li}_{3.75}\text{Si}$)</td>
<td>$E$</td>
<td>41</td>
<td>GPa</td>
<td>(37)</td>
<td>[99]</td>
</tr>
<tr>
<td>Poisson's Ratio ($\text{Li}_{3.75}\text{Si}$)</td>
<td>$\nu$</td>
<td>0.24</td>
<td>-</td>
<td>(37)</td>
<td>[100]</td>
</tr>
<tr>
<td>Yield stress</td>
<td>$\sigma_0$</td>
<td>0.5~2.0</td>
<td>GPa</td>
<td>(40)</td>
<td>[6, 101]</td>
</tr>
<tr>
<td>Fracture energy release rate</td>
<td>$g_c$</td>
<td>2.4~14.9</td>
<td>$J/m^2$</td>
<td>(30)</td>
<td>[15]</td>
</tr>
<tr>
<td>Diffusion coefficient</td>
<td>$D_{\text{diff}}^0$</td>
<td>$(1\sim10^6)\cdot10^{-13}$</td>
<td>$cm^2/s$</td>
<td>(43)</td>
<td>[102, 103]</td>
</tr>
<tr>
<td>Expansion coefficient</td>
<td>$\Omega$</td>
<td>2.8</td>
<td>-</td>
<td>(2)</td>
<td></td>
</tr>
<tr>
<td>Bond-breaking energy barrier (c-Si)</td>
<td>$E_0$</td>
<td>0.59~0.69</td>
<td>eV</td>
<td>(70)</td>
<td>[87]</td>
</tr>
<tr>
<td>Bond-breaking energy barrier (a-Si)</td>
<td>$E_0$</td>
<td>0.51~0.58</td>
<td>eV</td>
<td>(70)</td>
<td>[87]</td>
</tr>
<tr>
<td>Gas constant</td>
<td>$R$</td>
<td>8.3144</td>
<td>$J/(mol\cdot K)$</td>
<td>(41)</td>
<td></td>
</tr>
<tr>
<td>Boltzmann constant</td>
<td>$k_B$</td>
<td>$8.6173\cdot10^{-5}$</td>
<td>eV/K</td>
<td>(70)</td>
<td></td>
</tr>
<tr>
<td>Room temperature</td>
<td>$T$</td>
<td>300</td>
<td>K</td>
<td>(70)</td>
<td></td>
</tr>
<tr>
<td>Maximum concentration</td>
<td>$c_{\text{max}}$</td>
<td>$8.867\cdot10^4$</td>
<td>$mol/m^3$</td>
<td>(72)</td>
<td>[27]</td>
</tr>
<tr>
<td>Frequency parameter</td>
<td>$A$</td>
<td>$5.0\cdot10^9$</td>
<td>$s^{-1}$</td>
<td>(70)</td>
<td>[87]</td>
</tr>
<tr>
<td>Volumetric parameter (c-Si)</td>
<td>$\phi_{\text{cSi}}$</td>
<td>1.0</td>
<td>-</td>
<td>(70)</td>
<td>[87]</td>
</tr>
<tr>
<td>Volumetric parameter (a-Si)</td>
<td>$\phi_{\text{aSi}}$</td>
<td>0.8</td>
<td>-</td>
<td>(70)</td>
<td>[87]</td>
</tr>
<tr>
<td>Scaling parameter</td>
<td>$C$</td>
<td>50</td>
<td>-</td>
<td>(71)</td>
<td>[87]</td>
</tr>
<tr>
<td>Threshold value (c-Si)</td>
<td>$c_0$</td>
<td>0.10</td>
<td>-</td>
<td>(71)</td>
<td>[87]</td>
</tr>
<tr>
<td>Threshold value (a-Si)</td>
<td>$c_0$</td>
<td>0.06</td>
<td>-</td>
<td>(71)</td>
<td>[87]</td>
</tr>
</tbody>
</table>

![](./images/814520538939523073_7.jpg)

Figure 6: $\langle 100\rangle$ c-Si nanopillars. (a) Illustration of the diffusion induced anisotropic deformation and crystalline direction dependent fracture behavior for $\langle 100\rangle$ c-Si nanopillars. Fracture locations are indicated by red arrows [7]. (b) Illustration of the crystalline directions of a $\langle 100\rangle$ c-Si nanopillar as well as the finite element mesh and mechanical boundary conditions used in Section 5.1. Locations A and B are used to report the evolution of hoop stresses in Fig. 7(a).

#### 5.1.1. One-phase lithiation versus two-phase lithiation with plastic deformation

Both, elastic and elasto-plastic models are commonly used in the literature [27, 79, 104] to predict diffusion induced swelling of Si electrodes. To investigate their differences and demonstrate the importance of considering large plastic deformations for modeling diffusion induced fracture of Si electrodes, we perform elastic and elasto-plastic simulations for nanopillars of radius $R=300nm$. We do this initially without considering the presence of a reaction front, thereby mimicking a one-phase lithiation process. As the diffusion induced deformation is isotropic

![](./images/814520538939523073_8.jpg)

(a) evolution of hoop stresses at points A and B

![](./images/814520538939523073_9.jpg)

(b) concentration profile along the radius

Figure 7: ⟨100⟩ c-Si nanopillars. (a) Evolution of hoop stress at points labelled as A and B in Fig. 6(b) for four different simulation setups: one-phase lithiation with an elastic model; one-phase lithiation with an elasto-plastic model; two-phase lithiation for an isotropic elasto-plastic deformation with a uniform $E_0$; and two-phase lithiation for an anisotropic elasto-plastic deformation with different values of $E_0$ in different crystalline directions. (b) concentration profile along the radius of the Si electrode undergoing two-phase lithiation for different diffusion coefficients at $t=20s$. The larger the diffusion coefficient the larger is the concentration gradient at the reaction front.

in this case, we only report the evolution of hoop stresses at the location labeled as A in Fig. 6(b). We observe from Fig. 7(a) that hoop stresses at the outer surface of the electrodes remain compressive throughout the simulation when neglecting plastic effects, whereas otherwise those hoop stresses change from compressive to tensile during the lithiation process, thereby leading to the fracture of Si electrodes.

Next, we consider the presence of the reaction front and determine its influence on the evolution of hoop stresses in Si electrodes, thereby mimicking the two-phase lithiation process. The crystalline directions for a ⟨100⟩ c-Si nanopillar are given in Fig. 6(b). First, we consider a uniform bond-breaking energy barrier $E_0=0.60 eV$ to model diffusion induced isotropic elasto-plastic deformation. Second, we consider two different bond-breaking energy barriers for the ⟨100⟩ and the ⟨110⟩ directions with $E_0=0.60 eV$ and $E_0=0.66 eV$, respectively, to account for anisotropic effects. In Fig. 7(a) we report the hoop stresses at point A for the isotropic case and at points A and B for the anisotropic case. Both two-phase lithiation results indicate a rapid transition from compressive to tensile at point A of the outer electrode surface. Furthermore, for the anisotropic case, our model predicts a possible fracture location at point B (close to the ⟨100⟩ crystalline direction) with even higher tensile hoop stresses, which is consistent with experimental results shown in Fig. 6(a). The ability to model diffusion induced anisotropic deformation in different crystalline directions based on the different bond-breaking energy barriers $E_0$ is a unique feature of our computational framework.

We so far assumed that the diffusion coefficient $D_{diff}^0=10^{-12} cm^2/s$ remains constant throughout the lithiation process. This simplification ensures that the difference of hoop stresses reported in Fig. 7(a) arises from the mechanical models or the presence of the reaction front. However, it is reported in the literature that the diffusion coefficient highly depends on the concentration level, varying orders of magnitude [102, 103]. To investigate the effect of the diffusion coefficient on the isotropic two-phase lithiation results reported above, we perform four different simulations, whose results are shown in Fig. 7(b). First, the diffusion coefficient is kept constant at $D_{diff}^0=1\cdot 10^{-12} cm^2/s$. For the other three cases, $D_{diff}^0$ increases linearly from $1\cdot 10^{-12}$ to $15\cdot 10^{-12}$, $25\cdot 10^{-12}$, and $50\cdot 10^{-12} cm^2/s$ with $c$ increasing from 0 to 1. For all four cases, the concentration profile along the radial direction at $t=20s$ is plotted in Fig. 7(b). One can observe that a high concentration gradient is obtained at the reaction front for the concentration dependent diffusion coefficients, which is consistent with experimental results [4]. Therefore, we consider a linearly varying concentration dependent diffusion coefficient with $D_{diff}^0=1\sim 15\cdot 10^{-12} cm^2/s$ for $c$ varying from 0 to 1 for the remaining simulations in this work.

Contrary to the diffusion coefficient, we though neglect a possible dependency of Young's modulus and Poisson ratio of $\text{Li}_x\text{Si}$ with varying concentration $c$ as reported in [102, 103]. Instead we choose the corresponding values from $\text{Li}_{3.75}\text{Si}$. This assumption is supported by the fact that the concentration profile shown in Figs. 8 and 11 remains almost constant in the lithiated region with $c \approx 1$.

### 5.1.2. Diffusion induced fracture of ⟨100⟩ crystalline silicon nanopillars
In this section we now account for damage and investigate the diffusion induced size dependent fracture behavior for c-Si ⟨100⟩ nanopillars. We perform simulations with the same mesh as in Section 5.1.1 but with varying radii and fracture energy release rates. We again choose bond-breaking energy barriers $E_0 = 0.60\, eV$ and $E_0 = 0.66\, eV$ for the ⟨110⟩ and the ⟨100⟩ directions, respectively. Motivated by the results obtained in Section 5.1.1, the diffusion coefficient varies linearly from $10^{-12} cm^2/s$ to $15 \cdot 10^{-12} cm^2/s$ with $c$ increasing from 0 to 1. Its dependency on the damage field shown in (43) is neglected here.

For a nanopillar with a radius of $R = 300\, nm$ and a fracture energy release rate of $g_c = 12.5\, J/m^2$, we follow the criteria given in [47] and choose a length parameter of $l = 8\, nm$. The evolution of the concentration field $c$ and the damage field $d$ during the lithiation process are shown in Fig. 8 at different states of charge (SOC), defined as the ratio between the total amount of lithium particles in the electrode and the maximum lithium the electrode can hold. Since our model allows us to distinguish between the two different bond-breaking energy barriers for the two different crystalline directions of the c-Si nanopillar, it is shown in Fig. 8 that an anisotropic deformation is obtained for different SOC while continuously charging the Si nanopillar, which results in a crystalline direction dependent fracture behavior, taking place dominantly in ⟨100⟩ direction. Also, the linearly varying diffusion coefficient results in a sharp concentration gradient at the reaction front as shown in Fig. 8(a), matching experimental results [4]. As fracture takes place only in the lithiated region, the crack growth is limited by the reaction front moving speed.

In Fig. 9(a) the relation between SOC and the crack length is shown for different energy release rates $g_c$. A continuous increase of the crack length, defined as $\Gamma = \int_{\mathfrak{B}_0} \gamma(d, \nabla d)\, dV$ with $\gamma$ given in (30), is observed during the charging process. In Fig. 9(b), the SOC when the maximum value of the damage field reaches $d = 0.8$ is plotted for different radii of the Si nanopillar and different $g_c$. The smaller the radius and larger $g_c$, the larger the attainable SOC, before the crack initiates. The points surrounded by a square marker for a SOC of approximately 0.4 indicate numerical results for which the crack has not yet formed for the corresponding radius, but severe mesh distortion did not allow us to continue the charging process. Fig. 9(b) also includes experimental results taken from [28], which report no fracture for nanopillars of radius $100\, nm$ and $145\, nm$ but fracture taking place for nanopillars of radius $195\, nm$ and $245\, nm$.

### 5.2. Diffusion induced anisotropic deformation and fracture of ⟨110⟩ crystalline silicon nanopillars
In this section, we now investigate diffusion induced fracture for ⟨110⟩ c-Si nanopillars. Similar as for ⟨100⟩ c-Si nanopillars, experiments again reveal a diffusion induced anisotropic deformation and crystalline direction dependent fracture behavior, as shown in Fig. 10(a). We use the same mesh, initial conditions, and loadings as in Section 5.1, but change the crystalline directions to those of a ⟨110⟩ c-Si nanopillar, as shown in Fig. 10(b).

For a nanopillar with a radius of $R = 300\, nm$ and a fracture energy release rate of $g_c = 12.5\, J/m^2$, the evolution of the concentration field $c$ and the damage field $d$ during the lithiation process are shown in Fig. 11 at different SOC. Since our model allows us to distinguish between the two different bond-breaking energy barriers for the two different crystalline directions of the c-Si nanopillar, Fig. 11 shows that also for ⟨110⟩ c-Si nanopillars an anisotropic deformation is obtained for different SOC while continuously charging the Si nanopillar, which again results in a crystalline direction dependent fracture behavior, taking place dominantly in ⟨100⟩ direction. As fracture takes place only in the lithiated region, the crack growth is again limited by the reaction front moving speed.

In Fig. 12(a) the relation between SOC and the crack length for different energy release rates $g_c$ is now also shown for ⟨110⟩ c-Si nanopillars. Again, a continuous increase of the crack length is observed during the charging process. In Fig. 12(b), again the SOC when the maximum value of the damage field reaches $d = 0.8$ is plotted for different radii of the Si nanopillar and different $g_c$. Again, the smaller the radius and larger $g_c$, the larger the attainable SOC, before the crack initiates. The points surrounded by a square marker for a SOC of approximately 0.4 indicate again numerical results for which the crack has not yet formed for the corresponding radius, but severe mesh distortion did not allow us to continue the charging process. Fig. 12(b) also includes experimental results taken from [28], which

![](./images/814520538939523073_10.jpg)

Figure 8: ⟨100⟩ c-Si nanopillars. Plots of the concentration field $c$ and the damage field $d$ for the two-phase lithiation process with $g_c = 12.5 J/m^2$ at SOC=0.20, 0.25, and 0.35. (a) The c-Si nanopillar deforms anisotropically. The concentration profiles show a high concentration gradient at the reaction front. The black lines indicate a contour for the damage field $d = 0.95$. (b) The diffusion induced anisotropic deformation causes the fracture to initiate close to the ⟨100⟩ direction and to propagate inward, restricted by the reaction front moving speed.

![](./images/814520538939523073_11.jpg)

Figure 9: ⟨100⟩ c-Si nanopillars. (a) Relation between SOC and crack length of a c-Si nanopillar with $R = 300 nm$ for three different $g_c$. (b) Plot of SOC at the onset of crack nucleation in Si nanopillars of different radii and $g_c$. Points surrounded with a square marker indicate results without fracture onset. The simulation results are compared with statistical results from experiments, which are plotted as bar graphs in (b), where nanopillars with radius of $100 nm$, $145 nm$ and $195 nm$, $245 nm$ show 100% non-fracture ratio and 0% non-fracture ratio, respectively [28].

![](./images/814520538939523073_12.jpg)

(a) experimental results

![](./images/814520538939523073_13.jpg)

(b) simulation setup

Figure 10: $\langle 110 \rangle$ c-Si nanopillars. (a) Illustration of the diffusion induced anisotropic deformation and crystalline direction dependent fracture behavior for $\langle 110 \rangle$ c-Si nanopillars. Fracture locations are indicated by red arrows [7]. (b) Illustration of the crystalline directions of a $\langle 110 \rangle$ c-Si nanopillar as well as the finite element mesh and mechanical boundary conditions used in Section 5.2.

![](./images/814520538939523073_14.jpg)

(a) concentration profiles in c-Si electrode at SOC=0.28, 0.35, and 0.45

![](./images/814520538939523073_15.jpg)

(b) damage field profiles in c-Si electrode at SOC=0.28, 0.35, and 0.45

Figure 11: $\langle 110 \rangle$ c-Si nanopillars. Plots of the concentration field $c$ and the damage field $d$ for the two-phase lithiation process with $g_c = 12.5\ J/m^2$ at SOC=0.28, 0.35, and 0.45. (a) The c-Si nanopillar deforms anisotropically. The concentration profiles show a high concentration gradient at the reaction front. The black lines indicate a contour for the damage field $d = 0.95$. (b) The diffusion induced anisotropic deformation causes the fracture to initiate close to the $\langle 100 \rangle$ direction and to propagate inward, restricted by the reaction front moving speed.

report no fracture for nanopillars of radius $130\ nm$ and $145\ nm$ but fracture taking place for 5% of the nanopillars with a radius of $180\ nm$ whereas all of those with a radius of $195\ nm$ fracture.

### 5.3. Diffusion induced fracture of irregular Si nanoparticles

Next, we investigate the lithiation process of a realistic irregular Si nanoparticle. Experimental results [12] suggest that multiple cracks can form in one Si particle, as shown in Fig. 13(a). To reproduce these results with our computational framework, we consider a nanoparticle with a diameter of approximately $1.0\mu m$ and a mesh of 11805

![](./images/814520538939523073_16.jpg)

![](./images/814520538939523073_17.jpg)

Figure 12: $\langle 110 \rangle$ c-Si nanopillars. (a) Relation between SOC and crack length of a c-Si nanopillar with $R=300\,nm$ for three different $g_c$. (b) Plot of SOC at the onset of crack nucleation in Si nanopillars of different radii and $g_c$. Points surrounded with a square marker indicate results without fracture onset. The simulation results are compared with statistical results from experiments, which are plotted as bar graphs in (b), where nanopillars with radius of $130\,nm$ and $145\,nm$ show 100% non-fracture ratio but those with radius of $180\,nm$ and $195\,nm$ show a 95% and 0% non-fracture ratio, respectively [28].

![](./images/814520538939523073_18.jpg)

![](./images/814520538939523073_19.jpg)

(a) experimental results

(b) mesh

Figure 13: Irregular Si nanoparticles. (a) Experiments show that lithiated irregular Si nanoparticles may form multiple cracks [12]. (b) Illustration of the finite element mesh used in Section 5.3.

Q1 elements under plane strain conditions, as shown in Fig. 13(b). Two nodes in the center of the particle are fixed to avoid rigid body motions. The same initial and loading conditions as in Section 5.1 are used.

As the crystalline directions for such irregular Si nanoparticles are in general not available, we treat the Si nanoparticle as amorphous and choose a uniform bond-breaking energy barrier $E_0=0.58\,eV$ when modeling the two-phase lithiation process here. To investigate the fracture behavior of irregular Si nanoparticles, we perform a number of simulations with a length parameter $l=20\,nm$ and different fracture energy release rates $g_c$. We plot the damage field $d$ in Fig. 14(a-c) for a SOC of 0.35 and indicate the crack formation sequence by numbers for $g_c=7.5\,J/m^2$, $g_c=10\,J/m^2$, and $g_c=12.5\,J/m^2$. Fig. 14(d) shows the SOC when each of those cracks form (maximum damage value reaches $d=0.8$). The smaller the fracture energy release rate, the smaller the SOC at crack initiation and the more cracks form during the lithiation process. Still, the locations of the major, earlier forming cracks depend more on the geometry of the nanoparticle rather than the energy release rate. To conclude, our computational framework has the potential to be beneficial for designing fracture resistant electrode geometries.

![](./images/814520538939523073_20.jpg)

(a) $7.5 J/m^2$ (SOC=0.35)

![](./images/814520538939523073_21.jpg)

(b) $10 J/m^2$ (SOC=0.35)

![](./images/814520538939523073_22.jpg)

(c) $12.5 J/m^2$ (SOC=0.35)

![](./images/814520538939523073_23.jpg)

(d) crack sequence vs SOC

Figure 14: Irregular Si nanoparticles. (a-c) Profile of the damage field $d$ for a Si nanoparticle with three different fracture energy release rates at a SOC of 0.35 (elements with $d \geq 0.96$ are deleted in a postprocessing step for plotting purposes only). The numbers in (a-c) indicate the crack initiation sequence. (d) Values for the SOC at the onset of crack initiation for each crack.

### 5.4. Diffusion induced fracture of $\langle 110 \rangle$ crystalline silicon nanopillars under geometric constraints

In our final example, we want to investigate an experimentally observed increase in the fracture resistance of lithiated crystalline silicon nanopillars with radius $R$ under geometric constraints [105], as shown in Fig. 15(a). To do so, we revisit the problem investigated in Section 5.2 but now restrict the deformation of the $\langle 110 \rangle$ nanopillar by adding a rigid wall at a horizontal distance $\Delta$, as shown in Fig. 15(b). We again model one quarter of the geometry with a mesh consisting of 10924 Q1 elements under plane strain conditions. The crystalline directions are distributed as shown in Fig. 10(b) and the initial and loading conditions are identical to those in Section 5.1. The values of the initial gap $\Delta$ are chosen such that the volume expansion during the lithiation process will result in frictional contact at the electrode/wall interface, thereby affecting the fracture process.

In particular, we perform simulations with different radii $R$ and $\Delta/R$ ratios for three different fracture energy release rates $g_c$ and a length scale of $l = 8 nm$. In Fig. 16(a-c), we plot the damage field $d$ for a nanopillar with radius $R = 500 nm$ and ratios $\Delta/R = 0.15$, $\Delta/R = 0.3$, and $\Delta/R = 0.4$ for $g_c = 12.5 J/m^2$ at a SOC of 0.27. The former two ratios result in contact between the lithiated nanopillar and the rigid wall, which subsequently results in a delayed crack initiation and propagation compared to the latter case, where there is no contact, for the SOC considered here. The resulting crack lengths are computed as $0 nm$ (no fracture), $118 nm$, and $123 nm$ for the three ratios. Thus, the geometric constraint indeed has an affect on the crack formation and increases the nanopillars fracture resistance. We argue that the geometric constraint increases the pressure inside the nanoparticle and thereby slows down the lithiation speed in the $\langle 100 \rangle$ direction, which subsequently reduces the level of anisotropy and fracture.

To further quantify these results, we plot in Fig. 16 (d-f) the SOC at fracture onset (maximum damage value reaches $d = 0.8$) for different radii $R = 400 nm$ and $R = 500 nm$, different ratios $\Delta/R = 0.15$ (strong geometric constraint) to $\Delta/R = 0.4$ (no geometric constraint), and different fracture energy release rates $g_c = 7.5 J/m^2$, $g_c =$

![](./images/814520538939523073_24.jpg)

Figure 15: $\langle 110 \rangle$ c-Si nanopillars under geometric constraints. (a) Experiments show that geometric constraints affect the fracture behavior of $\langle 110 \rangle$ c-Si nanopillars [105]. The ellipse schematically shows the geometry of a lithiated nanopillar and the potential crack locations at the top and bottom when there is no geometric constraint. The red arrows show the altered crack locations when a geometric constraint is present. (b) Illustration of the mesh used in Section 5.4, where the initial gap between the nanopillar and the rigid wall is denoted as $\Delta$.

![](./images/814520538939523073_25.jpg)

(a) $R=500 nm, \frac{\Delta}{R}=0.15$ (SOC = 0.27)

(b) $R=500 nm, \frac{\Delta}{R}=0.3$ (SOC = 0.27)

(c) $R=500 nm, \frac{\Delta}{R}=0.4$ (SOC = 0.27)

![](./images/814520538939523073_26.jpg)

Figure 16: $\langle 110 \rangle$ c-Si nanopillars under geometric constraints. (a-c) The damage field $d$ for a $\langle 110 \rangle$ c-Si nanopillar with $R=500 nm$ under geometrical constraints with different $\Delta/R$ ratios for $g_c=12.5 J/m^2$ at SOC = 0.27 is shown. (d-f) SOC at fracture onset (maximum damage value $d=0.8$) for different radii $R=400 nm$ and $R=500 nm$, different ratios $\Delta/R=0.15$ (strong geometric constraint) to $\Delta/R=0.4$ (no geometric constraint), and different fracture energy release rates $g_c$.

$10 J/m^{2}$, and $g_{c}=12.5 J/m^{2}$. We can observe that for a radius of $R=400 nm$, the ratio $\Delta/R=0.15$ prevents crack initiation for all three values of $g_{c}$ and for a SOC of up to 0.27 (those points surrounded with a square marker indicate again that no fracture takes place). On the other hand, for a weaker constraint $\Delta/R\geq0.2$, almost no difference of the SOC at fracture onset is obtained when compared to the SOC of the fracture onset for the unconstrained case $\Delta/R=0.4$. Also the resistance increase is diminished for the larger radius of $R=500 nm$, where e.g. for the case of $g_{c}=7.5 J/m^{2}$ the SOC=0.21 at fracture onset for $\Delta/R=0.15$ is only slightly larger than the SOC=0.18 of fracture onset in the unconstrained case. The results for the constrained Si electrodes are consistent with the critical size study in Section 5.1.2 and Section 5.2, where electrodes with larger radius or smaller fracture energy release rate fracture at a lower level of SOC.

## 6. Conclusion

In this work, we formulate a variational-based fully chemo-mechanical coupled computational framework to model diffusion induced large plastic deformation and phase field fracture. We incorporate into this framework a recently developed reaction-controlled diffusion model to predict two-phase lithiation for a-Si and c-Si. We show that the reaction front plays a significant role in modeling the diffusion induced fracture problem. The performance of our computational framework is demonstrated by several numerical simulations. Our fully coupled model allows us to investigate how the fracture energy release rate, the electrode geometry, and geometrical constraints affect the fracture behavior. This model has the potential to be useful for the development of fracture-resistant designs of new Si electrodes.

## Acknowledgements

Financial support for this research was provided by the National Science Foundation through CAREER Award CMMI-1553638, the John A. Blume Research Fellowship, and the Professor James M. Gere Graduate Fellowship from Stanford University. This support is gratefully acknowledged.

## References

[1] M. Armand, J. Tarascon, Building better batteries, Nature 451 (2008) 652-7.

[2] X. H. Liu, J. W. Wang, S. Huang, F. Fan, X. Huang, Y. Liu, S. Krylyuk, J. Yoo, S. A. Dayeh, A. V. Davydov, S. X. Mao, S. T. Picraux, S. Zhang, J. Li, T. Zhu, J. Y. Huang, In situ atomic-scale imaging of electrochemical lithiation in silicon, Nature Nanotechnology 7 (2012) 749-56.

[3] X. H. Liu, L. Zhong, S. Huang, S. X. Mao, T. Zhu, J. Y. Huang, Size-dependent fracture of silicon nanoparticles during lithiation, ACS Nano 6 (2012) 1522-1531.

[4] M. T. McDowell, I. Ryu, S. W. Lee, C. Wang, W. D. Nix, Y. Cui, Studying the kinetics of crystalline silicon nanoparticle lithiation with in situ transmission electron microscopy, Advanced Materials 24 (2012) 6034-6041.

[5] M. T. McDowell, S. W. Lee, J. T. Harris, B. A. Korgel, C. Wang, W. D. Nix, Y. Cui, In situ TEM of two-phase lithiation of amorphous silicon nanospheres, Nano Letters 13 (2013) 758-764.

[6] V. A. Sethuraman, M. J. Chon, M. Shimshak, V. Srinivasan, P. Guduru, In situ measurements of stress evolution in silicon thin films during electrochemical lithiation and delithiation, Journal of Power Sources 195 (2010) 5062-5066.

[7] S. W. Lee, M. T. McDowell, L. A. Berla, W. D. Nix, Y. Cui, Fracture of crystalline silicon nanopillars during electrochemical lithium insertion, Proceedings of the National Academy of Sciences of the United States of America 109 (2012) 4080-5.

[8] M. J. Chon, V. A. Sethuraman, A. McCormick, V. Srinivasan, P. Guduru, Real-time measurement of stress and damage evolution during initial lithiation of crystalline silicon, Physical Review Letters 107 (2011) 045503.

[9] J. W. Wang, Y. He, F. Fan, X. H. Liu, S. Xia, Y. Liu, C. T. Harris, H. Li, J. Y. Huang, S. X. Mao, T. Zhu, Two-phase electrochemical lithiation in amorphous silicon, Nano Letters 13 (2013) 709-15.

[10] S. W. Lee, M. T. McDowell, J. Choi, Y. Cui, Anomalous shape changes of silicon nanopillars by electrochemical lithiation, Nano letters 11 (2011) 3034-3039.

[11] X. H. Liu, H. Zheng, L. Zhong, S. Huang, K. Karki, L. Q. Zhang, Y. Liu, A. Kushima, W. T. Liang, J. W. Wang, J.-H. Cho, E. Epstein, S. A. Dayeh, S. T. Picraux, T. Zhu, J. Li, J. P. Sullivan, J. Cumings, C. Wang, S. X. Mao, Z. Z. Ye, S. Zhang, J. Y. Huang, Anisotropic swelling and fracture of silicon nanowires during lithiation, Nano Letters 11 (2011) 3312-8.

[12] K. Rhodes, N. Dudney, E. Lara-Curzio, C. Daniel, Understanding the degradation of silicon electrodes for lithium-ion batteries using acoustic emission, Journal of the Electrochemical Society 157 (2010) A1354-A1360.

[13] J. P. Maranchi, A. F. Hepp, A. G. Evans, N. T. Nuhfer, P. N. Kunta, Interfacial properties of the a-Si/Cu: Active-inactive thin-film anode system for lithium-ion batteries, Journal of The Electrochemical Society 153 (2006) A1246.

[14] J. Li, A. K. Dozier, Y. Li, F. Yang, Y.-T. Cheng, Crack pattern formation in thin film lithium-ion battery electrodes, Journal of The Electro- chemical Society 158 (2011) A689.

[15] M. Pharr, Z. Suo, J. J. Vlassak, Measurements of the fracture energy of lithiated silicon electrodes of Li-ion batteries, Nano letters 13 (2013)5570-5577.

[16] K. Loeffel, L. Anand, A chemo-thermo-mechanically coupled theory for elasticviscoplastic deformation, diffusion, and volumetric swelling due to a chemical reaction, International Journal of Plasticity 27 (2011) 1409-1431.

[17] Z. Cui, F. Gao, J. Qu, A finite deformation stress-dependent chemical potential and its applications to lithium ion batteries, Journal of the Mechanics and Physics of Solids 60 (2012) 1280-1295.

[18] Y. Gao, M. Zhou, Coupled mechano-diffusional driving forces for fracture in electrode materials, Journal of Power Sources 230 (2013)176-193.

[19] V. I. Levitas, H. Attariani, Anisotropic compositional expansion in elastoplastic materials and corresponding chemical potential: Large-strain formulation and application to amorphous lithiated silicon, Journal of the Mechanics and Physics of Solids 69 (2014) 84-111.

[20] Z. Cui, F. Gao, J. Qu, Interface-reaction controlled diffusion in binary solids with applications to lithiation of silicon in lithium-ion batteries, Journal of the Mechanics and Physics of Solids 61 (2013) 293-310.

[21] H. Dal, C. Miehe, Computational electro-chemo-mechanics of lithium-ion battery electrodes at finite strains, Computational Mechanics 55(2015) 303-325.

[22] Y. Gao, M. Cho, M. Zhou, Mechanical reliability of alloy-based electrode materials for rechargeable Li-ion batteries, Journal of Mechanical Science and Technology 27 (2013) 1205-1224.

[23] T. K. Bhandakkar, H. Gao, Cohesive modeling of crack nucleation under diffusion induced stresses in a thin strip: Implications on the critical size for flaw tolerant battery electrodes, International Journal of Solids and Structures 47 (2010) 1424-1434.

[24] T. K. Bhandakkar, H. Gao, Cohesive modeling of crack nucleation in a cylindrical electrode under axisymmetric diffusion induced stresses, International Journal of Solids and Structures 48 (2011) 2304-2309.

[25] K. Zhao, M. Pharr, J. J. Vlassak, Z. Suo, Fracture of electrodes in lithium-ion batteries caused by fast charging, Journal of Applied Physics108 (2010) 073517.

[26] K. Zhao, M. Pharr, S. Cai, J. J. Vlassak, Z. Suo, Large plastic deformation in high-capacity lithium-ion batteries caused by charge and discharge, Journal of the American Ceramic Society 94 (2011) s226-s235.

[27] I. Ryu, I. W. Choi, Y. Cui, W. D. Nix, Size-dependent fracture of Si nanowire battery anodes, Journal of the Mechanics and Physics of Solids59 (2011) 1717-1730.

[28] I. Ryu, S. W. Lee, H. Gao, Y. Cui, W. D. Nix, Microscopic model for fracture of crystalline Si nanopillars during lithiation, Journal of Power Sources 255 (2014) 274-282.

[29] J. C. Simo, J. Oliver, F. Armero, An analysis of strong discontinuities induced by strain-softening in rate independent inelastic solids, Computational Mechanics 12 (1993) 277-296.

[30] F. Armero, K. Garikipati, An analysis of strong discontinuities in multiplicative finite strain plasticity and their relation with the numerical simulation of strain localization in solids, International Journal of Solids and Structures 33 (1996) 2863-2885.

[31] C. Linder, F. Armero, Finite elements with embedded strong discontinuities for the modeling of failure in solids, International Journal for Numerical Methods in Engineering 72 (2007) 1391-1433.

[32] F. Armero, C. Linder, New finite elements with embedded strong discontinuities in the finite deformation range, Computer Methods in Applied Mechanics and Engineering 197 (2008) 3138-3170.

[33] C. Linder, F. Armero, Finite elements with embedded branching, Finite Elem. Anal. Des. 45 (2009) 280-293.

[34] C. Linder, C. Miehe, Effect of electric displacement saturation on the hysteretic behavior of ferroelectric ceramics and the initiation and propagation of cracks in piezoelectric ceramics, Journal of the Mechanics and Physics of Solids 60 (2012) 882-903.

[35] F. Armero, J. Kim, Three-dimensional finite elements with embedded strong discontinuities to model material failure in the infinitesimal range, International Journal for Numerical Methods in Engineering 91 (2012) 1291-1330.

[36] C. Linder, A. Raina, A strong discontinuity approach on multiple levels to model solids at failure, Computer Methods in Applied Mechanics and Engineering 253 (2013) 558-583.

[37] C. Linder, X. Zhang, A marching cubes based failure surface propagation concept for three-dimensional finite elements with non-planar embedded strong discontinuities of higher-order kinematics, International Journal for Numerical Methods in Engineering 96 (2013) 339-372.

[38] C. Linder, X. Zhang, Three-dimensional finite elements with embedded strong discontinuities to model failure in electromechanical coupled materials, Computer Methods in Applied Mechanics and Engineering 273 (2014) 143-160.

[39] A. Raina, C. Linder, A micromechanical model with strong discontinuities for failure in nonwovens at finite deformation, International Journal of Solids and Structures 75-76 (2015) 247-259.

[40] T. Belytschko, T. Black, Elastic crack growth in finite elements with minimal remeshing, International Journal for Numerical Methods in Engineering 45 (1999) 601-620.

[41] N. Moës, J. Dolbow, T. Belytschko, A finite element method for crack growth without remeshing, International Journal for Numerical Methods in Engineering 46 (1999) 131-150.

[42] G. N. Wells, L. J. Sluys, A new method for modelling cohesive cracks using finite elements, International Journal for Numerical Methods in Engineering 50 (2001) 2667-2682.

[43] N. Moes, T. Belytschko, N. Moës, Extended finite element method for cohesive crack growth, Engineering Fracture Mechanics 69 (2002)813-833.

[44] G. A. Francfort, J.-J. Marigo, Revisiting brittle fracture as an energy minimization problem, Journal of Mechanics and Phyiscs of Solids 46(1998) 1319-1342.

[45] B. Bourdin, G. A. Francfort, J.-J. Marigo, Numerical experiments in revisited brittle fracture, Journal of Mechanics and Phyiscs of Solids48 (2000) 797-826.

[46] B. Bourdin, G. A. Francfort, J.-J. Marigo, The variational approach to fracture, Journal of Elasticity 91 (2008) 5-148.

[47] C. Miehe, F. Welschinger, M. Hofacker, Thermodynamically consistent phase-field models of fracture: Variational principles and multi-field FE implementations, International Journal for Numerical Methods in Engineering 83 (2010) 1273-1311.

[48] C. Miehe, M. Hofacker, F. Welschinger, A phase field model for rate-independent crack propagation: Robust algorithmic implementation based on operator splits, Computer Methods in Applied Mechanics and Engineering 199 (2010) 2765-2778.

[49] H. Amor, J.-J. Marigo, C. Maurini, Regularized formulation of the variational brittle fracture with unilateral contact: Numerical experiments, Journal of the Mechanics and Physics of Solids 57 (2009) 1209-1229.

[50] C. Miehe, F. Welschinger, M. Hofacker, A phase field model of electromechanical fracture, Journal of the Mechanics and Physics of Solids 58 (2010) 1716-1740.

[51] M. Hofacker, C. Miehe, Continuum phase field modeling of dynamic fracture: Variational principles and staggered FE implementation, International Journal of Fracture 178 (2012) 113-129.

[52] M. J. Borden, C. V. Verhoosel, M. A. Scott, T. J. R. Hughes, C. M. Landis, A phase-field description of dynamic brittle fracture, Computer Methods in Applied Mechanics and Engineering 217-220 (2012) 77-95.

[53] M. J. Borden, T. J. R. Hughes, C. M. Landis, C. V. Verhoosel, A higher-order phase-field model for brittle fracture: Formulation and analysis within the isogeometric analysis framework, Computer Methods in Applied Mechanics and Engineering 273 (2014) 100-118.

[54] K. Weinberg, C. Hesch, A high-order finite deformation phase-field approach to fracture, Continuum Mechanics and Thermodynamics (2015) 1-11doi:10.1007/s00161-015-0440-7.

[55] C. Miehe, L.-M. Schänzel, Phase field modeling of fracture in rubbery polymers. Part I: Finite elasticity coupled with brittle failure, Journal of the Mechanics and Physics of Solids 65 (2014) 93-113.

[56] A. Raina, C. Miehe, A phase-field model for fracture in biological tissues, Biomechanics and Modeling in Mechanobiology (2015) 1-18doi:10.1007/s10237-015-0702-0.

[57] T. Nguyen, J. Yvonnet, Q.-Z. Zhu, M. Bornert, C. Chateau, A phase field method to simulate crack nucleation and propagation in strongly heterogeneous materials from direct imaging of their microstructure, Engineering Fracture Mechanics 139 (2015) 18-39.

[58] F. P. Duda, A. Ciarbonetti, P. J. Sánchez, A. E. Huespe, A phase-field/gradient damage model for brittle fracture in elastic-plastic solids, International Journal of Plasticity 65 (2015) 269-296.

[59] A. Abdollahi, I. Arias, Phase-field modeling of crack propagation in piezoelectric and ferroelectric materials with different electromechanical crack conditions, Journal of the Mechanics and Physics of Solids 60 (2012) 2100-2126.

[60] Z. A. Wilson, M. J. Borden, C. M. Landis, A phase-field model for fracture in piezoelectric ceramics, International Journal of Fracture 183 (2013) 135-153.

[61] C. Miehe, L.-M. Schänzel, H. Ulmer, Phase field modeling of fracture in multi-physics problems. Part I. Balance of crack surface and failure criteria for brittle crack propagation in thermo-elastic solids, Computer Methods in Applied Mechanics and Engineering 294 (2015) 449-485.

[62] C. Miehe, S. Mauthe, S. Teichtmeister, Minimization principles for the coupled problem of Darcy-Biot-type fluid transport in porous media linked to phase field modeling of fracture, Journal of the Mechanics and Physics of Solids 82 (2015) 186-217.

[63] C. V. Verhoosel, R. de Borst, A phase-field model for cohesive fracture, International Journal for Numerical Methods in Engineering 96 (2013) 43-62.

[64] J. Vignollet, S. May, R. de Borst, C. V. Verhoosel, Phase-field models for brittle and cohesive fracture, Meccanica 49 (2014) 2587-2601.

[65] C. Miehe, M. Hofacker, L.-M. Schänzel, F. Aldakheel, Phase field modeling of fracture in multi-physics problems. Part II. Coupled brittle-to-ductile failure criteria and crack propagation in thermo-elastoplastic solids, Computer Methods in Applied Mechanics and Engineering 294 (2015) 486-522.

[66] M. Ambati, T. Gerasimov, L. De Lorenzis, Phase-field modeling of ductile fracture, Computational Mechanics 55 (2015) 1017-1040.

[67] S. May, J. Vignollet, R. de Borst, A numerical assessment of phase-field models for brittle and cohesive fracture: $\Gamma$-convergence and stress oscillations, European Journal of Mechanics - A/Solids 52 (2015) 72-84.

[68] P. Zuo, Y. Zhao, A phase field model coupling lithium diffusion, stress evolution with crack propagation and application in lithium ion battery, Physical Chemistry Chemical Physics 17 (2014) 287-297.

[69] C. Miehe, H. Dal, L.-M. Schänzel, A. Raina, A phase field model for chemo-mechanical induced fracture in lithium-ion battery electrode particles, International Journal for Numerical Methods in Engineering 106 (2015) 683-711.

[70] M. Klinsmann, D. Rosato, M. Kamlah, R. M. McMeeking, Modeling Crack Growth during Li Extraction in Storage Particles Using a Fracture Phase Field Approach, Journal of The Electrochemical Society 163 (2016) A102-A118.

[71] M. Ortiz, L. Stainier, The variational formulation of viscoplastic constitutive updates, Computer Methods in Applied Mechanics and Engineering 171 (1999) 419-444.

[72] C. Miehe, N. Apel, M. Lambrecht, Anisotropic additive plasticity in the logarithmic strain space: Modular kinematic formulation and implementation based on incremental minimization principles for standard materials, Computer Methods in Applied Mechanics and Engineering 191 (2002) 5383-5425.

[73] C. Miehe, A multi-field incremental variational framework for gradient-extended standard dissipative solids, Journal of the Mechanics and Physics of Solids 59 (2011) 898-923.

[74] C. Miehe, F. Aldakheel, S. Mauthe, Mixed variational principles and robust finite element implementations of gradient plasticity at small strains, International Journal for Numerical Methods in Engineering 94 (2013) 1037-1074.

[75] C. Miehe, S. Mauthe, H. Ulmer, Formulation and numerical exploitation of mixed variational principles for coupled problems of Cahn- Hilliard-type and standard diffusion in elastic solids, International Journal for Numerical Methods in Engineering 99 (2014) 737-762.

[76] C. Miehe, Variational gradient plasticity at finite strains. Part I: Mixed potentials for the evolution and update problems of gradient-extended dissipative solids, Computer Methods in Applied Mechanics and Engineering 268 (2014) 677-703.

[77] C. Miehe, F. R. Welschinger, F. Aldakheel, Variational gradient plasticity at finite strains. Part II: Local-global updates and mixed finite elements for additive plasticity in the logarithmic strain space, Computer Methods in Applied Mechanics and Engineering 268 (2014) 704-734.

[78] C. Miehe, S. Mauthe, F. Hildebrand, Variational gradient plasticity at finite strains. Part III: Local-global updates and regularization tech-

niques in multiplicative plasticity for single crystals, Computer Methods in Applied Mechanics and Engineering 268 (2014) 735-762.

[79] A. F. Bower, P. Guduru, A simple finite element model of diffusion, finite deformation, plasticity and fracture in lithium ion insertion electrode materials, Modelling and Simulation in Materials Science and Engineering 20 (2012) 45004.

[80] P. Stein, B.-X. Xu, 3D isogeometric analysis of intercalation-induced stresses in Li-ion battery electrode particles, Computer Methods in Applied Mechanics and Engineering 268 (2014) 225-244.

[81] L. Brassart, K. Zhao, Z. Suo, Cyclic plasticity and shakedown in high-capacity electrodes of lithium-ion batteries, International Journal of Solids and Structures 50 (2013) 1120-1129.

[82] C. V. Di Leo, E. Rejovitzky, L. Anand, Diffusion-deformation theory for amorphous silicon anodes: The role of plastic deformation on electrochemical performance, International Journal of Solids and Structures 67-68 (2015) 283-296.

[83] A. Krischok, C. Linder, On the enhancement of low-order mixed finite element methods for the large deformation analysis of diffusion in solids, International Journal for Numerical Methods in Engineering 106 (2016) 278-297.

[84] L. Anand, A Cahn-Hilliard-type theory for species diffusion coupled with large elastic-plastic deformations, Journal of the Mechanics and Physics of Solids 60 (2012) 1983-2002.

[85] C. V. Di Leo, E. Rejovitzky, L. Anand, A Cahn-Hilliard-type phase-field theory for species diffusion coupled with large elastic deformations: Application to phase-separating Li-ion electrode materials, Journal of the Mechanics and Physics of Solids 70 (2014) 1-29.

[86] Y. Zhao, P. Stein, B.-X. Xu, Isogeometric analysis of mechanically coupled Cahn-Hilliard phase segregation in hyperelastic electrodes of Li-ion batteries, Computer Methods in Applied Mechanics and Engineering 297 (2015) 325-347.

[87] X. Zhang, S. W. Lee, H.-W. Lee, Y. Cui, C. Linder, A reaction-controlled diffusion model for the lithiation of silicon in lithium-ion batteries, Extreme Mechanics Letters 4 (2015) 61-75.

[88] C. Truesdell, W. Noll, The Non-Linear Field Theories of Mechanics, Springer Science & Business Media, 2013.

[89] R. Hill, The Mathematical Theory of Plasticity, Oxford University Press, 2004.

[90] Z. Wang, Q. Su, H. Deng, Y. Fu, Composition dependence of lithium diffusion in lithium silicide: A density functional theory study, ChemElectroChem 2 (2015) 1292-1297.

[91] J. C. Simo, Algorithms for static and dynamic multiplicative plasticity that preserve the classical return mapping schemes of the infinitesimal theory, Computer Methods in Applied Mechanics and Engineering 99 (1992) 61-112.

[92] R. I. Borja, Plasticity: modeling & computation, Springer Science & Business Media, 2013.

[93] S. Chester, C. V. Di Leo, L. Anand, A finite element implementation of a coupled diffusion-deformation theory for elastomeric gels, International Journal of Solids and Structures 52 (2015) 1-18.

[94] K. Zhao, M. Pharr, Q. Wan, W. L. Wang, E. Kaxiras, J. J. Vlassak, Z. Suo, Concurrent reaction and plasticity during initial lithiation of crystalline silicon in lithium-ion batteries, Journal of the Electrochemical Society 159 (2012) A238-A243.

[95] S. W. Lee, L. A. Berla, M. T. McDowell, W. D. Nix, Y. Cui, Reaction Front Evolution during Electrochemical Lithiation of Crystalline Silicon Nanopillars, Israel Journal of Chemistry 52 (2012) 1118-1123.

[96] E. D. Cubuk, W. L. Wang, K. Zhao, J. J. Vlassak, Z. Suo, E. Kaxiras, Morphological evolution of Si nanowires upon lithiation: A first- principles multiscale model, Nano Letters 13 (2013) 2011-2015.

[97] M. A. Hopcroft, W. D. Nix, T. W. Kenny, What is the Young's Modulus of Silicon?, Journal of Microelectromechanical Systems 19 (2010) 229-238.

[98] V. A. Sethuraman, M. J. Chon, M. Shimshak, N. Van Winkle, P. Guduru, In situ measurement of biaxial modulus of Si anode for Li-ion batteries, Electrochemistry Communications 12 (2010) 1614-1617.

[99] L. A. Berla, S. W. Lee, Y. Cui, W. D. Nix, Mechanical behavior of electrochemically lithiated silicon, Journal of Power Sources 273 (2015) 41-51.

[100] V. B. Shenoy, P. Johari, Y. Qi, Elastic softening of amorphous and crystalline Li-Si Phases with increasing Li concentration: A first-principles study, Journal of Power Sources 195 (2010) 6825-6830.

[101] B. Hertzberg, J. Benson, G. Yushin, Ex-situ depth-sensing indentation measurements of electrochemically produced SiLi alloy films, Elec- trochemistry Communications 13 (2011) 818-821.

[102] N. Ding, J. Xu, Y. Yao, G. Wegner, X. Fang, C. Chen, I. Lieberwirth, Determination of the diffusion coefficient of lithium ions in nano-Si, Solid State Ionics 180 (2009) 222-225.

[103] C. Y. Chou, G. S. Hwang, On the origin of the significant difference in lithiation behavior between silicon and germanium, Journal of Power Sources 263 (2014) 252-258.

[104] V. I. Levitas, H. Attariani, Anisotropic compositional expansion and chemical potential for amorphous lithiated silicon under stress tensor, Scientific Reports 3 (2013) 1615.

[105] S. W. Lee, H.-W. Lee, I. Ryu, W. D. Nix, H. Gao, Y. Cui, Kinetics and fracture resistance of lithiated silicon nanostructure pairs controlled by their mechanical interaction, Nature Communications 6 (2015) 7533.

28