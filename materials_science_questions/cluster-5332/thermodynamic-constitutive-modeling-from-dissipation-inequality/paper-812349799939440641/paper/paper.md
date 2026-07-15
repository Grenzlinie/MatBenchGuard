Structural and Multidisciplinary Optimization
https://doi.org/10.1007/s00158-021-02900-8

RESEARCH PAPER

![](./images/812349799939440641_1.jpg)

# Structural optimisation of diffusion driven degradation processes

Navina Waschinsky¹ ![](https://arxiv.org/icons/person-icon.png) · Franz-Joseph Barthold¹ · Andreas Menzel²,³

Received: 19 August 2020 / Revised: 19 January 2021 / Accepted: 3 March 2021
© The Author(s) 2021

## Abstract
In this article, we propose an optimisation framework that can contribute to the prevention of premature failure or damage to building structures and can thereby strengthen their longevity. We concentrate on structures that are contaminated by chemical substances and that have strong destructive effects on the material. The aim of this contribution is a mathematical algorithm that allows the optimisation of a structure exposed to chemical influences and thus the assurance of the static load capacity. To achieve this, we present a coupled mechanical-diffusion-degradation approach embedded in a finite element (FE) framework. Furthermore, we integrate an optimisation algorithm to reduce material degradation. In this paper, we establish shape optimisation of a structure with a gradient based optimisation algorithm.

Keywords Coupled problems · Mechanical diffusion coupling · Degradation · Shape optimisation

## 1 Introduction
Engineering structures are dimensioned according to standards. The maximum existing stresses are evaluated and the material load-bearing capacity is examined, whereby environmental influences are only marginally considered. However, negative influences can additionally change the material composition and thus the mechanical load-bearing capacity over time. Most changes in the internal structure of materials are associated with diffusion processes. One example is the long-term effect of calcium leaching in concrete, where “pure water creates concentration gradients which lead to the diffusion of Ca ions from the pore water and the subsequent degradation of underground concrete” (Choi and Yang 2013).

In the following, an approach is presented which allows the calculation of mechanical and chemical influences on structures. Furthermore, it is possible to calculate an optimal geometry that reduces the damage of long-term effects caused by environmental influences. Therefore, this approach integrates the structural analysis into a structural optimisation algorithm. Within the structural analysis, we couple the diffusion of chemical substances with the mechanical behaviour of the material. We assume permeable structures which allow gradient-based diffusion of concentrations. In addition, we postulate that chemical substances have an influence on the material of the structure, since they can trigger material degradation. To ensure this, we focus on mechanical degradation processes corresponding to negative growth processes using multiplicative decomposition of the deformation gradient. Since this is a space- and time-dependent problem, we embed the material description in a finite element (FE) framework, by using an isoparametric concept for space discretisation and a Newmark-beta approach for temporal discretisation. Furthermore, we develop an algorithm for structural optimisation. In detail, we present a shape optimisation with a gradient-based calculation, which contains information about the sensitivities of the parameters that influence the mechanical behaviour. Using representative examples, we introduce the basic idea of the model and examine practical aspects where components are at risk of being exposed to chemical concentrations and yet their strength must be guaranteed.

In order to determine the approach for optimisation of diffusion driven degradation problems, the following topics are applied and embedded in a short overview of the state of the art. In the context of structural mechanics,

---

Responsible Editor: Seonho Cho

✉ Navina Waschinsky
navina.waschinsky@tu-dortmund.de

¹ Structural Mechanics, TU Dortmund University, Dortmund, Germany
² Institute of Mechanics, TU Dortmund University, Dortmund, Germany
³ Division of Solid Mechanics, Lund University, Lund, Sweden

Published online: 31 May 2021
![](./images/812349799939440641_3.jpg)

the topics coupled problems and growth, respectively degra- dation processes, are investigated in more detail. For the embedding in optimisation, shape optimisation and sensitiv- ity analysis are applied.

Kuhl (2005) presents a general overview of coupled prob- lems and the numerical implementation. Furthermore, he outlines in detail the coupling of diffusion processes to mechanical behaviour. A coupled theory of fluid permeation and large deformations for elastomeric materials, concen- trating on a thermodynamically consistent derivation of the constitutive relations and the resulting partial differential equations, is presented by Chester and Anand (2010).

Menzel and Kuhl (2012) summarise growth and remod- elling models for living structures. Mechanical growth and remodelling can be modelled either with a constitutive approach, a kinematic approach or a combination of both. Growth processes can be described by evaluating the time- dependent change in mass, density or volume of a structure. On the one hand, the constitutive approach concentrates on a thermodynamically consistent evaluation of the mass source and the mass flow, which enables the calculationof change in mass or density (Cowin and Hegedus 1976;Harrigan and Hamilton 1992; Epstein and Maugin 2000; Kuhl et al. 2003; Menzel 2005). The kinematic approach, on the other hand, allows the calculation of the variable mass or volume by applying a multiplicative decomposition of the deformation gradient (Rodriguez et al. 1994; Chen and Hoger 2000; Ambrosi and Mollica 2002; Gleason and Humphrey 2005; Menzel 2007). A useful alternative is the combination of the constitutive and kinematic approach, one example for this combination is presented by (Ganghoffer2010), where the calculation of surface growth in biological tissue is presented. He uses the multiplicative decompo- sition of the deformation gradient, as originally presented by Rodriguez et al. (1994), and applies a thermodynami- cally consistent approach to establish an evolutionary law for growth velocity. The multiplicative decomposition of the deformation gradient leads to a "growth tensor describing the local addition of material and an elastic tensor charac- terizing the reorganization of the body", see Ganghoffer and Plotnikov (2014). Therefore, the development of the growth tensor, the so-called transplant tensor, is introduced as a state variable in the framework of finite elasticity.

In Gérard et al. (2002), a simplified numerical model of calcium leaching is presented, which concentrates on the chemical state variable calcium and the kinetics of the leaching process. This model considers time-dependent chemical processes and mentions the possibility of a simplecoupling in a finite element (FE) algorithm. Kuhl (2005) presents a chemo-mechanical model for the numerical simulation of calcium leaching in concrete. He emphasises the effects of the chemical degradation on the pore volume and the mechanical stability of concrete. A damage function is used for constitutive modelling of the chemo-mechanically degraded material.

An overview on structural optimisation methods applied to discretised linear-elastic structures is given in Christensen and Klarbring (2008). Structural optimisation, which is applied to growth or degradation processes, is usually solved by evolutionary optimisation algorithms (ESO), see Simon (2013) for details. The evolution models are based on the concept of gradually removing inefficient material from a structure. The disadvantage of ESO concepts is that optimisation starts from one defined reference configuration and that the result quickly ends in local minima. Thus, it is not possible to find an optimal solution with a single ESO algorithm, see Vrugt and Robinson (2007). However, the application of shape optimisation to growth or degradation processes could help solve the problem, but has not yet been sufficiently investigated. Similar to the embedding of a growth approach in an optimisation algorithm, shape and topology optimisations are applied to damage models. For example, an optimal damage distribution is computed with a shape optimisation algorithm that embeds an isotropic gradient-enhanced damage model, see Guhr et al. (2020). Suresh et al. (2018) present a topology optimisation method which is connected to a fatigue model. The model enables the computation of optimised topologies, taking fatigue at high cycles as a limiting condition into account. Moreover, Noel et al. (2017) develop a level set-based topology optimisation framework to reduce damage in the context of structural design.

Barthold (2002) presents the basic principles of design changes necessary for structural optimisation and their effects on the structural response on a continuum. He introduces the local convective approach containing local coordinates and derives it from a differentiable manifold. Furthermore, he emphasises the importance of this approach for obtaining information about the kinematic relation required for numerical methods such as the finite element method (FEM) and computer-aided geometric design(CAGD). A detailed discussion of efficient strategies for calculating sensitivity of design parameters is described in Barthold and Stein (1996) where, in addition, the method of variational sensitivity analysis is presented.

The above briefly presented literature motivates the structural analysis which contains a coupled mechanical- diffusion-degradation approach. The special feature of this model is the combination of the coupled problem with a shape optimisation approach so that the failure limit of structures affected by mechanical loads and chemical impacts can be improved. By embedding the degradation model in the optimisation algorithm, this approach repre- sents an effective alternative to evolutionary algorithms.

![](./images/812349799939440641_4.jpg)

Structural optimisation of diffusion driven degradation processes

## 2 Continuum model

We present the continuum model including coupling between diffusion and mechanical behaviour. First we introduce the extended kinematic framework. We then formulate the partial differential equations which are determined by balance equations and constitutive equations together with boundary and initial conditions. The constitutive equations, including mechanical stresses, particle diffusion and chemical reactions, are determined by a thermodynamically consistent framework based on the evaluation of the entropy inequality.

### 2.1 Kinematics

A graphical illustration of the applied kinematic framework is presented in Fig. 1, which provides a multiplicative decomposition of the deformation gradient into an elastic and a growth part. We assume that the temporal evolution of the mass density takes place in the reference configuration. An infinitesimal volume element is represented by dV in the reference configuration, by dv<sub>d</sub> in the degradation space and by dv in the actual configuration. We introduce positions in the reference configuration $\mathbf{X}$, in the actual configuration $\mathbf{x}$ and in the degradation space $\mathbf{x}_{\mathrm{d}}$. Furthermore, $\boldsymbol{\varphi}_{\mathrm{t}}$ describes the mapping of the reference particles $\mathbf{X}$ onto their spatial position $\mathbf{x}=\boldsymbol{\varphi}_{\mathrm{t}}(\mathbf{X}, \mathrm{t})$ with $t$ representing time. We introduce the convective tangent vectors $\mathbf{G}_{\mathbf{i}}$, $\mathbf{g}_{\mathbf{i}}$ and $\mathbf{h}_{\mathbf{i}}$. The contravariant basis vectors that determine the dual basis are defined by $\mathbf{G}_{\mathbf{i}} \cdot \mathbf{G}^{\mathbf{j}}=\delta_{\mathrm{i}}^{\mathrm{j}}$, $\mathbf{g}_{\mathbf{i}} \cdot \mathbf{g}^{\mathbf{j}}=\delta_{\mathrm{i}}^{\mathrm{j}}$ and $\mathbf{h}_{\mathbf{i}} \cdot \mathbf{h}^{\mathbf{j}}=\delta_{\mathrm{i}}^{\mathrm{j}}$. With this, we introduce the deformation tensors which map infinitesimal line elements represented in different configurations, i.e. $\mathbf{F}$, $\mathbf{F}^{\mathrm{d}}$ and $\mathbf{F}^{\mathrm{e}}$

$$
\begin{aligned}
\text { deformation gradient : } \quad \mathbf{F} & =\mathbf{g}_{\mathbf{i}} \otimes \mathbf{G}^{\mathbf{i}} \\
\text { degradation gradient : } \quad \mathbf{F}^{\mathrm{d}} & =\mathbf{h}_{\mathbf{i}} \otimes \mathbf{G}^{\mathbf{i}} \\
\text { elastic deformation gradient : } \mathbf{F}^{\mathrm{e}} & =\mathbf{g}_{\mathbf{i}} \otimes \mathbf{h}^{\mathbf{i}}.
\end{aligned}
\tag{1}
$$

![](./images/812349799939440641_5.jpg)

Fig. 1 Graphical illustration of the kinematic concept

These gradients are important two-point tensors that allow transformations between objects in relation to the respective configurations. We apply a multiplicative decomposition of the deformation gradient $\mathbf{F}$ into an elastic part $\mathbf{F}^{\mathrm{e}}$ and a degradation part $\mathbf{F}^{\mathrm{d}}$ as introduced in Himpel et al. (2005), Kuhl et al. (2004), and Menzel and Kuhl (2012). According to Lubarda and Hoger (2002), we use an isotropic approach for the degradation fraction of the deformation gradient with the stretch ratio $v$, to be specific

$$
\begin{aligned}
\mathbf{F} & =\mathbf{F}^{\mathrm{e}} \mathbf{F}^{\mathrm{d}} & & \text { with } \\
\mathbf{F}^{\mathrm{d}} & =v \mathbf{1} & & \text { and } \quad v=\sqrt[3]{\frac{\rho_{0}}{\rho_{0}^{*}}},
\end{aligned}
\tag{2}
$$

whereby $\mathbf{1}$ denotes the second order identity tensor and the mass densities $\rho_{0}$ and $\rho_{0}^{*}$ respectively, being introduced as this work proceeds. Using the elastic part of the deformation gradient, we can introduce the elastic right Cauchy Green tensor as

$$
\mathbf{C}^{\mathrm{e}}=\left(\mathbf{F}^{\mathrm{e}}\right)^{\mathrm{T}} \mathbf{F}^{\mathrm{e}}=\mathrm{g}_{\mathrm{ij}} \mathbf{h}^{\mathrm{i}} \otimes \mathbf{h}^{\mathrm{j}}.
\tag{3}
$$

Moreover, the material time derivative of the elastic right Cauchy Green tensor is obtained by

$$
\begin{aligned}
\dot{\mathbf{C}}^{\mathrm{e}} & =\left(\dot{\mathbf{F}}^{\mathrm{e}}\right)^{\mathrm{T}} \mathbf{F}^{\mathrm{e}}+\left(\mathbf{F}^{\mathrm{e}}\right)^{\mathrm{T}} \dot{\mathbf{F}}^{\mathrm{e}} \\
& =\left(\mathbf{F}^{\mathrm{e}}\right)^{\mathrm{T}} \mathbf{I}^{\mathrm{T}} \mathbf{F}^{\mathrm{e}}+\left(\mathbf{F}^{\mathrm{e}}\right)^{\mathrm{T}} \mathbf{I} \mathbf{F}^{\mathrm{e}} \\
& =2\left(\mathbf{F}^{\mathrm{e}}\right)^{\mathrm{T}} \mathbf{d} \mathbf{F}^{\mathrm{e}},
\end{aligned}
\tag{4}
$$

with

$$
\dot{\mathbf{F}}^{\mathrm{e}}=\mathbf{I} \mathbf{F}^{\mathrm{e}} \quad \text { and } \quad \mathbf{d}=\frac{1}{2}\left(\mathbf{I}^{\mathrm{T}}+\mathbf{I}\right),
\tag{5}
$$

wherein $\mathbf{I}=\operatorname{grad} \dot{\mathbf{x}}$ is the spatial velocity gradient.

Figure 1 introduces the definition of the mass densities referred to the respective configurations. In the reference configuration, $\rho_{0}^{*}$ represents the initial and $\rho_{0}$ the referential mass density, which arises as a result of material degradation. The mass density $\rho_{\mathrm{d}}$ is referred to the degradation space and $\rho_{\mathrm{t}}$ to the actual configuration. Mass exchange is realised by a mass sink term $\mathrm{R}_{0}$ per unit volume in the reference configuration which triggers the degradation from the initial mass contribution dM and results in the mass contribution dm, i.e.

$$
\mathrm{dm}=\mathrm{dM}+\int_{\mathrm{t}_{0}}^{\mathrm{t}} \mathrm{R}_{0} \mathrm{dt} \mathrm{dV}.
\tag{6}
$$

This leads to time-dependent update of the initial mass density $\rho_{0}^{*}$ to the resulting referential mass density $\rho_{0}$, to be specific

$$
\rho_{0}=\rho_{0}^{*}+\int_{\mathrm{t}_{0}}^{\mathrm{t}} \mathrm{R}_{0} \mathrm{dt}.
\tag{7}
$$

Within the kinematic concept, we assume that the initial referential mass density and the mass density referred to the degradation space coincide, i.e.

$$
\rho_{0}^{*}=\rho_{\mathrm{d}}.
\tag{8}
$$

![](./images/812349799939440641_6.jpg)

The mapping between the configurations, see Fig. 1, leads to a change in volume, whereas mass is not influenced by such mappings, i.e. using (8) results in

$$
\rho_{0}=\rho_{0}^{*} \mathrm{~J}^{\mathrm{d}}=\rho_{\mathrm{d}} \mathrm{J}^{\mathrm{d}}=\rho_{\mathrm{t}} \mathrm{J} ; \rho_{\mathrm{d}}=\rho_{\mathrm{t}} \mathrm{J}^{\mathrm{e}} . \tag{9}
$$

Moreover, $\mathrm{J}^{\mathrm{e}}=\operatorname{det} \mathbf{F}^{\mathrm{e}}>0$ denotes the determinant of the elastic part of the deformation gradient and $\mathrm{J}=\operatorname{det} \mathbf{F}>0$ as well as $\mathrm{J}^{\mathrm{d}}=\operatorname{det} \mathbf{F}^{\mathrm{d}}=\rho_{0} / \rho_{0}^{*}>0$, cf. (2), follow by analogy.

### 2.2 Degradation approach

The degradation model is implemented by a combination of a kinematic and a constitutive approach. Thus, in Section 2.1, the multiplicative decomposition of the deformation gradient is performed and the degradation space is introduced. Within the constitutive approach, a mass exchange is established which leads to the change of referential mass density $\rho_{0}$. In return, the evolving mass density is used to calculate the degradation part of the deformation gradient, see (2). We assume that the mass degradation is caused due to chemical concentrations $\mathrm{c}_{\gamma}$, which are defined by the corresponding molar density $\rho_{\gamma}$ and the molar mass $\mathrm{M}_{\gamma}$, i.e.

$$
\mathrm{c}_{\gamma}=\frac{\rho_{\gamma}}{\mathrm{M}_{\gamma}} . \tag{10}
$$

Thus, we apply the constitutive approach of the mass sink term as follows

$$
\mathrm{R}_{0}=-\dot{\rho}_{\gamma} . \tag{11}
$$

Assuming only one concentration to be related to the chemical interaction, we can summarise the degradation impact of the concentrations as

$$
\rho_{0}=\rho_{0}^{*}-\mathrm{c}_{\gamma} \mathrm{M}_{\gamma} . \tag{12}
$$

This paper does not address chemical processes in detail. For further details on a model with more complex chemical processes, the reader is referred to, e.g. Gérard et al. (2002). In the following, the concentrations are introduced as an additional degree of freedom in the continuum.

### 2.3 Balance equations

In order to implement the above-introduced problem numerically, the following section presents the necessary balance approaches to solve the coupled multi-field problem. On the one hand, we need the balance of mass to calculate the concentrations, and on the other hand, the momentum balance to calculate the displacement. The concentration distribution depends on spatial conditions and the stresses on mass density which, in turn, is influenced by concentration-related mass reduction. For this reason, this is a strongly coupled problem. Furthermore, the balance of energy and entropy is needed to determine the constitutive material model.

#### 2.3.1 Balance of mass

We evaluate the balance of mass for the macroscopic body and for the chemical concentrations. The reduction of the mass in the reference configuration leads to a change of mass with $\mathrm{d} \dot{\mathrm{m}}=\mathrm{R}_{0} \mathrm{dV}$ and $\{\dot{\bullet}\}$ denoting the material time derivative. Using the transformations between the configurations, we can represent the balance of mass on the actual configuration as

$$
\int_{\mathrm{B}_{\mathrm{t}}}\left(\dot{\rho}_{\mathrm{t}}+\rho_{\mathrm{t}} \operatorname{div} \dot{\mathbf{x}}\right) \mathrm{dv}=\int_{\mathrm{B}_{\mathrm{t}}} \frac{\mathrm{R}_{0}}{\mathrm{~J}} \mathrm{dv}, \tag{13}
$$

wherein 'div' denotes the spatial divergence operator. The balance of mass of the chemical concentrations contains the material time derivative of the concentrations $\dot{\mathrm{c}}_{\gamma}$ and the flux of the concentrations $\mathbf{j}_{\gamma}$, i.e.

$$
\int_{\mathrm{B}_{\mathrm{t}}}\left(\dot{\mathrm{c}}_{\gamma}+\operatorname{div} \mathbf{j}_{\gamma}\right) \mathrm{dv}=0 . \tag{14}
$$

#### 2.3.2 Balance of linear momentum

The balance of linear momentum is shown below for the actual configuration and contains the Cauchy stress tensor $\mathbf{T}$. Although we apply mass exchange, we can neglect effects of the impulse resulting from the degrading mass, since the process of degradation is assumed to be very slow. This results in

$$
\int_{\mathrm{B}_{\mathrm{t}}} \operatorname{div} \mathbf{T} \mathrm{dv}=\mathbf{0}, \tag{15}
$$

wherein additional volume forces as well as acceleration are neglected. From the balance equation of moment of momentum, we can derive that the Cauchy stress tensor is symmetric, so that $\mathbf{T}^{\mathrm{T}}=\mathbf{T}$.

#### 2.3.3 Balance of energy

The balance of energy consists of the temporal derivative of internal energy $\dot{\mathrm{E}}$, and kinetic energy $\dot{\mathrm{K}}$, which correspond to mechanical energy change $\mathrm{dW}$, thermal energy change $\mathrm{dQ}$ and chemical flow on the surface $\mathrm{E}_{\mathrm{c}_{\gamma}}$, resulting in the following equations

$$
\begin{aligned}
\dot{\mathrm{E}}+\dot{\mathrm{K}}= & \mathrm{dW}+\mathrm{dQ}+\mathrm{E}_{\mathrm{c}_{\gamma}} \\
\int_{\mathrm{B}_{\mathrm{t}}} \dot{\mathrm{e}} \mathrm{dv}= & \int_{\mathrm{B}_{\mathrm{t}}}(\mathbf{d}: \mathbf{T}+\mathbf{r}-\operatorname{div} \mathbf{q}) \mathrm{dv} \\
& -\int_{\partial \mathrm{B}_{\mathrm{t}}}\left(\mu_{\gamma} \mathbf{j}_{\gamma}\right) \cdot \mathrm{da},
\end{aligned} \tag{16}
$$

![](./images/812349799939440641_7.jpg)

wherein $\dot{e}$ is the material time derivative of the volume specific internal energy, r is the volume specific heat source, $\mathbf{q}$ is the heat flux density, $\mu_{\gamma}$ is the chemical potential and $\mathrm{d} \mathbf{a}=\mathbf{n} \mathrm{da}$ with spatial outward unit surface vector $\mathbf{n}$. The time derivation of the kinetic energy has no impact on the balance of energy as we neglect acceleration and consider only slow progression of degradation. The surface part can be reformulated as follows,

$$
\int_{\partial \mathrm{B}_{\mathrm{t}}}\left(\mu_{\gamma} \mathbf{j}_{\gamma}\right) \cdot \mathrm{d} \mathbf{a}=\int_{\mathrm{B}_{\mathrm{t}}} \operatorname{div}\left(\mu_{\gamma} \mathbf{j}_{\gamma}\right) \mathrm{dv}
\tag{17}
$$

with

$$
\operatorname{div}\left(\mu_{\gamma} \mathbf{j}_{\gamma}\right)=\mathbf{j}_{\gamma} \cdot \operatorname{grad} \mu_{\gamma}+\mu_{\gamma} \operatorname{div} \mathbf{j}_{\gamma}.
\tag{18}
$$

Using the mass balance of chemical concentrations from (14), the local form of the balance of energy reads

$$
-\mathrm{r}+\operatorname{div} \mathbf{q}=-\dot{e}+\mathbf{d}: \mathbf{T}-\mathbf{j}_{\gamma} \cdot \operatorname{grad} \mu_{\gamma}+\mu_{\gamma} \dot{\mathrm{c}}_{\gamma}. \tag{19}
$$

### 2.3.4 Balance of entropy
Entropy is summarised in the second law of thermodynamics and states that entropy never decreases in a closed system. Accordingly, entropy always increases or remains constant. In this context, the entropy inequality is adapted as

$$
\int_{\mathrm{B}_{\mathrm{t}}} \dot{\mathrm{s}} \mathrm{dv} \geq \int_{\mathrm{B}_{\mathrm{t}}} \frac{1}{\Theta} \mathrm{r} \mathrm{dv}-\int_{\partial \mathrm{B}_{\mathrm{t}}} \frac{1}{\Theta} \mathbf{q} \cdot \mathrm{d} \mathbf{a},
\tag{20}
$$

where $\dot{s}$ denotes the material time derivative of the volume specific entropy and where $\Theta$ is the absolute temperature. The surface part can be reformulated as follows,

$$
\int_{\partial \mathrm{B}_{\mathrm{t}}} \frac{1}{\Theta} \mathbf{q} \cdot \mathrm{d} \mathbf{a}=\int_{\mathrm{B}_{\mathrm{t}}} \operatorname{div}\left(\frac{1}{\Theta} \mathbf{q}\right) \mathrm{dv}
\tag{21}
$$

with

$$
\begin{aligned}
\operatorname{div}\left(\frac{1}{\Theta} \mathbf{q}\right) &=\mathbf{q} \cdot \operatorname{grad}\left(\frac{1}{\Theta}\right)+\frac{1}{\Theta} \operatorname{div} \mathbf{q} \\
&=-\frac{1}{\Theta^{2}} \mathbf{q} \cdot \operatorname{grad} \Theta+\frac{1}{\Theta} \operatorname{div} \mathbf{q}.
\end{aligned}
\tag{22}
$$

Inserting the reformulation into the entropy inequality (20), we obtain the local form

$$
0 \leq \Theta \dot{\mathrm{s}}-\mathrm{r}-\frac{1}{\Theta} \mathbf{q} \cdot \operatorname{grad} \Theta+\operatorname{div} \mathbf{q}.
\tag{23}
$$

Under isothermal conditions, i.e. $\mathbf{q}=\mathbf{0}$ as well as $\dot{\Theta}=0$, and with the local form of the energy balance, see (19), we end up with the restriction

$$
0 \leq \Theta \dot{\mathrm{s}}-\dot{e}+\mathbf{d}: \mathbf{T}-\mathbf{j}_{\gamma} \cdot \operatorname{grad} \mu_{\gamma}+\mu_{\gamma} \dot{\mathrm{c}}_{\gamma}. \quad(24)
$$

### 2.4 Constitutive formulation
We perform a Legendre(-Fenchel) transformation between the extensive thermodynamic entropy s and the conjugate quantity, the temperature $\Theta$. This results in the so-called Helmholtz energy $\psi$, i.e.

$$
\dot{\psi}=\dot{e}-\Theta \dot{\mathrm{s}}.
\tag{25}
$$

By introducing the Helmholtz free energy into the entropy inequality (24) and by selecting the elastic right Cauchy Green tensor and the concentrations to derive the energy process with $\psi\left(\mathbf{C}^{\mathrm{e}}, \mathrm{c}_{\gamma}\right)$, the following results are obtained

$$
\underbrace{-\frac{\partial \psi}{\partial \mathbf{C}^{\mathrm{e}}}: \dot{\mathbf{C}}^{\mathrm{e}}+\mathbf{d}: \mathbf{T}}_{\substack{\text { reversible } \\-\mathbf{j}_{\gamma} \cdot \operatorname{grad} \mu_{\gamma}}}+\underbrace{-\frac{\partial \psi}{\partial \mathrm{c}_{\gamma}} \dot{\mathrm{c}}_{\gamma}+\mu_{\gamma} \dot{\mathrm{c}}_{\gamma}}_{\substack{\text { reversible } \\ \geq 0.}}
\tag{26}
$$

We can separate the approach for the Helmholtz function into a mechanical $\psi^{\mathrm{M}}$ and a chemical $\psi^{\mathrm{C}}$ part

$$
\psi\left(\mathbf{C}^{\mathrm{e}}, \mathrm{c}_{\gamma}\right)=\psi^{\mathrm{M}}\left(\mathbf{C}^{\mathrm{e}}\right)+\psi^{\mathrm{C}}\left(\mathrm{c}_{\gamma}\right).
\tag{27}
$$

In order to ensure the entropy inequality, the reversible contributions are evaluated and the Cauchy stress $\mathbf{T}$ and the chemical potential $\mu_{\gamma}$ are determined, i.e.

$$
\begin{aligned}
\mathbf{T} &=2 \mathbf{F}^{\mathrm{e}} \frac{\partial \psi^{\mathrm{M}}}{\partial \mathbf{C}^{\mathrm{e}}}\left(\mathbf{F}^{\mathrm{e}}\right)^{\mathrm{T}} \\
\mu_{\gamma} &=\frac{\partial \psi_{\gamma}^{\mathrm{C}}}{\partial \mathrm{c}_{\gamma}},
\end{aligned}
\tag{28}
$$

wherein (4) is used. From the irreversible part of the entropy inequality we motivate the flux of the concentrations

$$
\mathbf{j}_{\gamma}=-\mathrm{D} \operatorname{grad} \mathrm{c}_{\gamma},
\tag{29}
$$

where $\mathrm{D} \geq 0$ is introduced as the diffusion coefficient.

### 2.4.1 Specifications of energy contributions
The mechanical energy is described by adopting a hypere-lastic Neo-Hooke material, $\psi^{\text {Neo }}$, which contains material parameters $\mu$ and $\lambda$, to be specific

$$
\begin{aligned}
\psi^{\mathrm{M}} &=\rho_{\mathrm{t}} \psi^{\text {Neo }} \\
\psi^{\text {Neo }} &=\frac{1}{\rho_{0} *}\left[\frac{1}{2} \lambda\left(\mathrm{J}^{\mathrm{e}}-1\right)^{2}-\mu \ln \mathrm{J}^{\mathrm{e}}\right. \\
&\left.\quad+\frac{1}{2} \mu\left(\mathrm{I}_{\mathrm{C}}^{\mathrm{e}}-3\right)\right],
\end{aligned}
\tag{30}
$$

with invariants $\mathrm{I}_{\mathrm{C}^{\mathrm{e}}}=\operatorname{tr} \mathbf{C}^{\mathrm{e}}$ and $\mathrm{J}^{\mathrm{e}}=\sqrt{\operatorname{det} \mathbf{C}^{\mathrm{e}}}=\sqrt{\mathrm{III}_{\mathrm{C}^{\mathrm{e}}}}$, which depend on the elastic right Cauchy Green deformation tensor $\mathbf{C}^{\mathrm{e}}$. In addition, we specify the chemical part $\psi^{\mathrm{C}}$ as

$$
\psi^{\mathrm{C}}=\mathrm{c}_{\gamma} \mu_{\gamma}^{0}+\mathrm{R} \Theta\left(-\mathrm{c}_{\gamma}+\mathrm{c}_{\gamma} \ln \mathrm{c}_{\gamma}\right),
\tag{31}
$$

where $\mu_{\gamma}^{0}$ is the constant standard potential and where $\mathrm{R}$ is the gas constant. Inserting the mechanical and chemical energy contributions into (28) results in

$$
\begin{aligned}
\mathbf{T} &=\frac{\rho_{\mathrm{t}}}{\rho_{0} *} \mathbf{F}^{\mathrm{e}}\left[\lambda\left(\mathrm{J}^{\mathrm{e}}-1\right) \mathrm{J}^{\mathrm{e}}\left(\mathbf{C}^{\mathrm{e}}\right)^{-1}\right. \\
&\left.\quad-\mu\left(\mathbf{C}^{\mathrm{e}}\right)^{-1}+\mu \mathbf{1}\right]\left(\mathbf{F}^{\mathrm{e}}\right)^{\mathrm{T}} \\
&=\frac{\rho_{\mathrm{t}}}{\rho_{0} *}\left[\lambda\left(\mathrm{J}^{\mathrm{e}}-1\right) \mathrm{J}^{\mathrm{e}} \mathbf{1}+2 \mu \mathbf{K}^{\mathrm{e}}\right],
\end{aligned}
\tag{32}
$$

![](./images/812349799939440641_8.jpg)

with the spatial Karni-Reiner strain tensor $\mathbf{K}^{\mathrm{e}}$, i.e.
$$
\mathbf{K}^{\mathrm{e}}=\frac{1}{2}\left[\mathbf{F}^{\mathrm{e}}\left(\mathbf{F}^{\mathrm{e}}\right)^{\mathrm{T}}-\mathbf{1}\right]. \tag{33}
$$

Furthermore, the chemical potential follows as
$$
\mu_{\gamma}=\mu_{\gamma}^{0}+\mathrm{R} \Theta \ln \mathrm{c}_{\gamma}. \tag{34}
$$

### 2.4.2 Illustration of stress state

In the evaluations of the examples in Sections 4 and 6 we use the principal Cauchy stresses $\mathrm{T}_{1}$ and $\mathrm{T}_{2}$ in the two-dimensional space considered, namely
$$
\mathrm{T}_{1,2}=1 \pm \sqrt{-\frac{\mathrm{I}_{\mathrm{T}}}{2}-\mathrm{II}_{\mathrm{T}}}, \tag{35}
$$
with the invariants of the Cauchy stress $\mathrm{I}_{\mathrm{T}}$ and $\mathrm{II}_{\mathrm{T}}$, i.e.
$$
\begin{aligned}
\mathrm{I}_{\mathrm{T}} & =\operatorname{tr} \mathbf{T} \\
\mathrm{II}_{\mathrm{T}} & =\frac{1}{2}\left((\operatorname{tr} \mathbf{T})^{2}-\operatorname{tr} \mathbf{T}^{2}\right).
\end{aligned} \tag{36}
$$

## 3 Finite element formulation

The previously presented continuum framework for the coupled mechanical-diffusion-degradation model leads to a set of coupled differential equations, which are time-dependent and highly nonlinear. For further procedure, a numerical approximation, the FEM, is used. We apply the Galerkin method, whereby the balance equations are represented in their weak form and weighted by independent test functions. For the fully discrete problem, we solve for the displacements $\mathbf{u}=\mathbf{x}-\mathbf{X}$ and the concentrations $\mathrm{c}_{\gamma}$ on the basis of the balance of linear momentum and the balance of mass for the concentrations.

### 3.1 Weak form

In the following we present the weak form of the balance of momentum weighted by the independent test functions for the displacements $\delta \mathbf{u}$ and the weak form of the balance of mass of the concentrations weighted by the independent test functions for the concentrations $\delta \mathrm{c}_{\gamma}$. The equations are posed in the reference configuration. On the one hand, the weak form of the balance of linear momentum results in
$$
\int_{\mathrm{B}_{0}} \mathbf{P}: \operatorname{Grad} \delta \mathbf{u} \mathrm{dV}=\int_{\partial \mathrm{B}_{0}} \mathbf{P N} \cdot \delta \mathbf{u} \mathrm{dA}, \tag{37}
$$
wherein the mapping of the Cauchy stress $\mathbf{T}$ to the first Piola-Kirchhoff stress tensor $\mathbf{P}$ is applied with the transformation $\mathbf{P}=\mathbf{J T F}^{-\mathrm{T}}$ and wherein $\mathbf{N}$ is the material normal unit vector on the Neumann boundary. On the other hand, the weak form of the balance of mass is given as
$$
\begin{aligned}
& \int_{\mathrm{B}_{0}}\left(\dot{\mathrm{c}}_{\gamma} \delta \mathrm{c}_{\gamma}-\mathbf{j}_{\gamma} \cdot \operatorname{grad} \delta \mathrm{c}_{\gamma}\right) \mathrm{J} \mathrm{dV} \\
& =\int_{\partial \mathrm{B}_{0}} \mathbf{j}_{\gamma} \cdot \delta \mathrm{c}_{\gamma} \mathbf{J} \mathbf{F}^{-\mathrm{T}} \mathbf{N} \mathrm{dA},
\end{aligned} \tag{38}
$$
with $\mathbf{J F}^{-\mathrm{T}} \mathbf{N} \mathrm{dA}=\mathbf{n} \mathrm{da}$. We describe the Dirichlet boundary conditions as follows
$$
\begin{aligned}
\mathbf{u} & =\mathbf{u}^{*} \quad \forall \mathbf{X} \in \partial \mathrm{B}_{0}^{\mathrm{u}} \\
\mathrm{c}_{\gamma} & =\mathrm{c}_{\gamma}^{*} \quad \forall \mathbf{X} \in \partial \mathrm{B}_{0}^{\mathrm{c}_{\gamma}},
\end{aligned} \tag{39}
$$
and the Neumann boundary conditions as
$$
\begin{aligned}
\mathbf{P N} & =\mathbf{t}^{*} \quad \forall \mathbf{X} \in \partial \mathrm{B}_{0}^{\mathrm{t}} \\
\mathbf{J}_{\gamma} \cdot \mathbf{N} & =\mathrm{J}_{\gamma}^{*} \quad \forall \mathbf{X} \in \partial \mathrm{B}_{0}^{\mathrm{J}_{\gamma}},
\end{aligned} \tag{40}
$$
with $\mathbf{J}_{\gamma}=\mathbf{J} \mathbf{j}_{\gamma} \mathbf{F}^{-\mathrm{T}}$. The initial conditions are given with $\mathbf{u}\left(\mathrm{t}_{0}\right)=\mathbf{u}_{0}$ and $\mathrm{c}_{\gamma}\left(\mathrm{t}_{0}\right)=\mathrm{c}_{\gamma}^{0}$.

### 3.2 Discretisation in space

For space discretisation, we apply the isoparametric concept which is based on approximating geometry, displacement and concentrations by the same set of ansatz functions $\mathrm{h}^{\mathrm{I}}(\boldsymbol{\xi})$. The discrete form of the test functions for the displacement $\delta \mathbf{u}^{\mathrm{h}}$ and for the concentrations $\delta \mathrm{c}_{\gamma}^{\mathrm{h}}$ results in
$$
\begin{aligned}
\delta \mathbf{u}^{\mathrm{h}} & =\sum_{\mathrm{I}=1}^{\mathrm{NN}} \mathrm{h}^{\mathrm{I}}(\boldsymbol{\xi}) \delta \mathbf{u}^{\mathrm{I}} \\
\delta \mathrm{c}_{\gamma}^{\mathrm{h}} & =\sum_{\mathrm{I}=1}^{\mathrm{NN}} \mathrm{h}^{\mathrm{I}}(\boldsymbol{\xi}) \delta \mathrm{c}_{\gamma}^{\mathrm{I}},
\end{aligned} \tag{41}
$$
wherein NN denotes the number of nodes per element and where $\boldsymbol{\xi}$ represents the local coordinates. In this work, we apply an eight-noded element description, i.e. two-dimensional Serendipity elements under plane strain conditions. Moreover, approximations of the degrees of freedom as well as of all related gradient operations follow straightforwardly.

### 3.3 Discretisation in time

The simulation of the diffusion of the concentrations requires a discretisation in time for which we apply the Newmark-beta method. Within the considered time interval, we approximate a constant average acceleration of the concentrations $\ddot{\mathrm{c}}_{\beta}$, i.e.
$$
\ddot{\mathrm{c}}_{\beta}=\frac{1}{2}\left(\ddot{\mathrm{c}}_{\gamma}(\mathrm{t})+\ddot{\mathrm{c}}_{\gamma}(\mathrm{t}+\Delta \mathrm{t})\right), \tag{42}
$$
with the previous acceleration of the concentrations $\ddot{\mathrm{c}}_{\gamma}(\mathrm{t})$ and the acceleration to be approximated in the present time step $\ddot{\mathrm{c}}_{\gamma}(\mathrm{t}+\Delta \mathrm{t})$. Based on this, one obtains
$$
\begin{aligned}
\dot{\mathrm{c}}_{\gamma}(\mathrm{t}+\Delta \mathrm{t}) & =\dot{\mathrm{c}}_{\gamma}(\mathrm{t})+\Delta \mathrm{t} \ddot{\mathrm{c}}_{\beta} \\
\mathrm{c}_{\gamma}(\mathrm{t}+\Delta \mathrm{t}) & =\mathrm{c}_{\gamma}(\mathrm{t})+\Delta \mathrm{t} \dot{\mathrm{c}}_{\gamma}(\mathrm{t})+\frac{1}{2} \Delta \mathrm{t}^{2} \ddot{\mathrm{c}}_{\beta}.
\end{aligned} \tag{43}
$$

![](./images/812349799939440641_9.jpg)

Structural optimisation of diffusion driven degradation processes

![](./images/812349799939440641_10.jpg)

Fig. 2 a Dirichlet boundary conditions $\Delta$u. b Neumann boundary conditions F

Finally, we gain the approximation of the velocity for the concentrations $\dot{c}_\gamma(t+\Delta t)$ in the present time step, i.e.

$$
\dot{c}_\gamma(t+\Delta t)=\frac{2}{\Delta t}(c_\gamma(t+\Delta t)-c_\gamma(t))-\dot{c}_\gamma(t). \quad (44)
$$

## 4 Numerical analysis examples

In this section, we discuss the properties of the proposed diffusion controlled degradation model in the context of representative examples focusing on the basic coupling mechanism between diffusion impact and structural response.

### 4.1 Material behaviour

In the following, the correlations between mechanical and degradation processes are investigated on the basis of an analysis including one finite element and two different sets of boundary conditions as shown in Fig. 2. Furthermore, we apply the material and loading parameters shown in Table 1.

The degradation process is identically established for both examples, at this point independently of chemical concentrations, with the change of the referential mass density $\rho_0$, as shown in Fig. 3. With this at hand, the degradation part of the deformation gradient $\mathbf{F}^\text{d}$ can be evaluated with (2).

For mechanical impact, the first example is uniaxially loaded with a displacement $\Delta$u = 0.5 cm in y-direction,

<table>
<caption>Table 1 Material and loading parameters</caption>
<tbody>
<tr>
<td>E</td>
<td>=</td>
<td>1 MN cm⁻²</td>
</tr>
<tr>
<td>$\nu$</td>
<td>=</td>
<td>0.29</td>
</tr>
<tr>
<td>$\rho_0^*$</td>
<td>=</td>
<td>3000 kg m⁻³</td>
</tr>
<tr>
<td>$\Delta$u</td>
<td>=</td>
<td>0.5 cm</td>
</tr>
<tr>
<td>F</td>
<td>=</td>
<td>0.015 MN</td>
</tr>
</tbody>
</table>

![](./images/812349799939440641_11.jpg)

Fig. 3 Approach for the time-dependent decrease of density with $\rho_0/\rho_0^*=1-5\times10^{-4}\text{t}^2[\text{s}]^{-2}$, wherein t is time

see Fig. 2a, which results in the deformation gradient

$$
\mathbf{F}=\mathbf{1}+\varepsilon \mathbf{e}_y \otimes \mathbf{e}_y, \tag{45}
$$

wherein $\varepsilon$ is the strain in y-direction. For comparison, the second example is loaded with a constant traction with resulting force F = 0.015 MN in y-direction, see Fig. 2b.

The determinant of the degradation contribution to the deformation gradient, $J^\text{d}$, follows directly from the time-dependent approach for the change of referential density, see Fig. 4, so that we observe the same referential mass density evaluations for both boundary conditions. However, the total deformation changes differently in the two examples. For the boundary condition displayed in Fig. 2a, the total deformation represented by J is constant, because the structure does not allow shrinkage. The elastic deformation

![](./images/812349799939440641_12.jpg)

Fig. 4 Evaluation of the boundary condition Fig. 2a in red and of the boundary condition Fig. 2b in blue with a time slot of 29 s

![](./images/812349799939440641_13.jpg)

![](./images/812349799939440641_14.jpg)

Fig. 5 The grey colour shows the initial state, the black colour the deformation state and the blue colour the degraded structure: displacement loading (left, a) and force loading (right, b) by analogy with Fig. 2

changes inversely so that, i.e. $\mathrm{J}^{\mathrm{e}}=\left[\mathrm{J}^{\mathrm{d}}\right]^{-1} \mathrm{~J}$. The stress $\mathrm{T}_{\mathrm{yy}}$ increases, because the total deformation is fixed, whereas the degradation part decreases. In comparison to the first example with fixed Dirichlet boundary conditions, the example illustrated in Fig. 2b results in a degradation process and the total deformation represented by J decreases over time. In return, the elastic deformation $\mathrm{J}^{\mathrm{e}}$ and the stress $\mathrm{T}_{\mathrm{yy}}$ are constant. The related states of deformation are additionally illustrated in Fig. 5.

### 4.2 Diffusion driven degradation

In this example, we discuss the coupled effects of diffusion leading to a degradation of the material. This example is motivated by the idea to analyse chemical influence on hollow concrete blocks, since concrete is a porous medium that allows the inflow of concentrations and is susceptible to chemical degradation. The boundary value problem is illustrated in Fig. 7a, which shows a structure with a hole. The hole of the structure is defined by the parameters $(s_{1}, s_{2})$, which represent the axes of an ellipse. We consider a concentration inflow from the left side of the structure. The choice of parameters, as stated in Table 2, is based on values common for concrete and the orders of magnitude for chemical diffusion processes, although no specific chemical process is described here. The material degradation triggered by molecular processes with concentrations occurs very slowly. Therefore, the calculation is accelerated by considering the diffusion rate per day (d) and a time-dependent increase in concentrations per day, as shown in Fig. 6. In total, the computation considers a time period of 4d with a time step size of 1 d. A stable mechanical environment is enabled by fixed displacements as shown in Fig. 7a. The concentration inflow on the left side leads to the contour plot given in Fig. 7b. Figure 8a illustrates the degradation induced by the concentrations and in Fig. 8b the impact of the deformation on the first principal stress $T_{1}$ is evaluated. Since material degradation is triggered by a high concentration of

<table>
<caption>Table 2 Material parameters for the structure with the hole</caption>
<tbody>
<tr>
<td>E</td>
<td>=</td>
<td>3 MN cm⁻²</td>
</tr>
<tr>
<td>$\nu$</td>
<td>=</td>
<td>0.2</td>
</tr>
<tr>
<td>$\rho_{0}^{*}$</td>
<td>=</td>
<td>2000 kg m⁻³</td>
</tr>
<tr>
<td>$\mathrm{M}_{\gamma}$</td>
<td>=</td>
<td>1 kg mol⁻¹</td>
</tr>
<tr>
<td>D</td>
<td>=</td>
<td>100m² d⁻¹</td>
</tr>
<tr>
<td>$\mathrm{c}_{\gamma}(\mathrm{t}=0)$</td>
<td>=</td>
<td>100 mol m⁻³</td>
</tr>
<tr>
<td>a</td>
<td>=</td>
<td>50 cm</td>
</tr>
<tr>
<td>b</td>
<td>=</td>
<td>50 cm</td>
</tr>
<tr>
<td>s₁</td>
<td>=</td>
<td>10 cm</td>
</tr>
<tr>
<td>s₂</td>
<td>=</td>
<td>5 cm</td>
</tr>
</tbody>
</table>

![](./images/812349799939440641_15.jpg)

Fig. 6 Time dependent Dirichlet boundary conditions for the concentrations $\mathrm{c}_{\gamma}^{*}(\mathrm{t})$

![](./images/812349799939440641_16.jpg)

Fig. 7 a Dirichlet boundary conditions of a structure with a hole. b Contour plot of the concentrations after the first time step

![](./images/812349799939440641_17.jpg)

chemicals, the main material reduction takes place close to the inlet area.

The maximum of the first principal stress is located in this area close to the hole. Overall, this example clearly shows the coupling between diffusion and deformation.

## 5 Structural optimisation framework

This section outlines the connection between structural analysis and optimisation framework. Furthermore, the information required for the optimisation problem, such as the objective function, the constraints and design parameters, are presented. The main programme runs in the numerical computing environment of MATLAB which contains a link to the open software gmsh to create a mesh on the one hand and an interface to a Fortran code using MEX-file interfaces on the other. The linearisation of the weak form, in discrete form, is implemented in a Fortran based FE code and the MEX-file transfers the data to the workspace. The assembly and calculation are implemented in MATLAB.

### 5.1 Sketch of algorithmic framework

An overview of the algorithm is shown in Fig. 9. The algorithm can be divided into three main sections, the boundary value problem, structural analysis and structural optimisation. First, the boundary value problem is relevant for the definition of the model problem by means of parametric geometry description. The information about the boundary value problem provides the input for the structural analysis. In addition, the solution of the structural analysis computes a structure deformed by chemical and mechanical loads, which is used as initial design in the structural optimisation. In this paper, continuum mechanical quantities such as the evaluation of the stress restriction and geometry parameters are selected for the objective function and the constraints. These variables are calculated within the framework of structural analysis and directly passed on to the mathematical solver. The structural optimisation minimises the defined objective function while maintaining the given constraints and provides new design parameters. The optimisation task is solved with the help of a MATLAB toolbox.

![](./images/812349799939440641_18.jpg)
Fig. 9 Illustration of the algorithmic framework

Furthermore, the technical implementation can be briefly summarised. The global programme runs in MATLAB, while the information at element level is implemented in a Fortran code and embedded via MEX interfaces. Information at element level retrieves the coupled equations for the description of the problem presented, the variation formulations with the discrete weak forms and the gradient information for the FEM solution. In addition, an interface to the open software gmsh, a finite element mesh generator, is generated during the framework of the boundary value problem. In this paper, geometrical values are chosen as design parameters; therefore, a parametric mesh design is implemented. The functions introduced as part of the optimisation process are described in the typographic style 'italics', e.g. objective function $J$, constraints $\boldsymbol{g}$, design parameters $\boldsymbol{s}$.

![](./images/812349799939440641_19.jpg)

### 5.2 Optimisation problem

The structural optimisation problem is solved by using the nonlinear optimisation function `fmincon` provided by MATLAB toolbox, see (MathWorks 2019). This solver finds the minimum of a restricted nonlinear and multivariable function. The general optimisation problem follows with an objective function $J(\mathbf{v}, s)$, nonlinear inequality constraints $\boldsymbol{g}(\mathbf{v}, s)$, upper and lower limit values $s^{\mathrm{u}}$ and $s^{\mathrm{l}}$ for a set of design parameters, i.e.

$$
\begin{aligned}
\min J(\mathbf{v}, s): & \boldsymbol{g}(\mathbf{v}, s) \leq 0 & & \text { constraints } \\
& s^{\mathrm{l}} \leq s \leq s^{\mathrm{u}} & & \text { limit values },
\end{aligned}
\tag{46}
$$

wherein $\mathbf{v} \in\{\mathbf{u}, c_{\gamma}\}$ are the field variables and $s$ geometric design parameters. In this paper, we deal with the two shape optimisation problems as follows:

1.  Minimisation of the maximum first principal stress $\mathrm{T}_{1}^{\max }$ by changing geometrical parameters, with the constraint of a maximum loss of area.
2.  Minimisation of the area by changing geometrical parameters, with the constraint of an upper limit for the maximum first principal stress $\mathrm{T}_{1}^{\max }$.

In both optimisation setups, structural analysis is applied to calculate the objective and constraint functions, since there is a dependency on the field variables. Further specifications on the objective function and constraint are provided in Sections 6.1 and 6.2. Fmincon uses the 'sqp-legacy' algorithm to solve the optimisation task, wherein the gradients of the objective function and constraints are obtained numerically by finite differences. The Hessian matrix is iteratively integrated using the Broyden-Fletcher-Goldfarb-Shanno (BFGS) procedure. Further details can be found in (MathWorks 2019). The application of the finite difference method is a precise but time-consuming method. In the outlook, we address a more efficient approach for future work.

## 6 Numerical optimisation examples

In the following, two examples are presented for shape optimisation of structures that are loaded by chemical concentrations. The first example is taken from Section 4.2 and shows a hollow concrete block which is loaded by chemical substances. We calculate the optimised shape of the brick in such a way that the maximum stress caused by the concentrations is reduced while still retaining material. The second example is inspired by a mechanically loaded bridge, additionally loaded with chemical substances, which can be caused by, for example calcium leaching. The goal of this example is a structure with minimised material and limited stresses.

<table>
<caption>Table 3 Input parameters for the optimisation algorithm</caption>
<tbody>
<tr class="odd">
<td>Threshold</td>
<td>$\overline{\mathrm{A}}$</td>
<td>0.03</td>
<td></td>
</tr>
<tr class="even">
<td rowspan="2">Limit values</td>
<td>$s^{\mathrm{u}}$</td>
<td>[15; 10 ]</td>
<td>cm</td>
</tr>
<tr class="odd">
<td>$s^{\mathrm{l}}$</td>
<td>[5; 0 ]</td>
<td></td>
</tr>
<tr class="even">
<td>Initial design</td>
<td>$s$</td>
<td>[10; 5 ]</td>
<td>cm</td>
</tr>
</tbody>
</table>

### 6.1 Optimisation of a structure with a hole

Using the example of the structural analysis in Section 4.2 with the material parameters from Table 2, an optimised shape is discussed below. We use the sum of the Gaussian point values of the first principal stress in the maximum loaded element $\mathrm{T}_{1}^{\max }$ as the objective function $J(\mathbf{v}, s)$ and the change of the area as inequality constraints $\boldsymbol{g}(\mathbf{v}, s)$ with

$$
\begin{aligned}
J(\mathbf{v}, s) & =\sum_{1}^{\mathrm{NG}} \mathrm{T}_{1}^{\max } \\
g(\mathbf{v}, s) & =\left|\frac{\mathrm{A}^{\mathrm{ini}}-\mathrm{A}}{\mathrm{A}^{\mathrm{ini}}}\right|-\overline{\mathrm{A}},
\end{aligned}
\tag{47}
$$

wherein NG is the number of Gaussian points, $\mathrm{A}^{\mathrm{ini}}$ is the initial area, A is the actual area and $\overline{\mathrm{A}}$ is a threshold. The optimisation problem follows as

$$
\begin{aligned}
\min J(\mathbf{v}, s): & g(\mathbf{v}, s) \leq 0 & & \text { constraints } \\
& s^{\mathrm{l}} \leq s \leq s^{\mathrm{u}} & & \text { limit values }.
\end{aligned}
\tag{48}
$$

The axes of the ellipse $(s_{1}, s_{2})$ are the design parameters. The optimisation algorithm applies the input parameters listed in Table 3.

The following diagramme, see Fig. 10, shows the iteration course of the optimisation to minimise the objective function while fulfilling the constraints. The solver requires a total of 9 iterations until an optimal shape is found to minimise the average first principal stress in the Gaussian points to $0.083 \mathrm{MN} \mathrm{cm}^{-2}$.

After 18,468 s of computing time, the optimisation leads to the following new design parameters, i.e. (Fig. 12).

$$
s=[5 ; 5.525],
\tag{49}
$$

![](./images/812349799939440641_20.jpg)

Fig. 10 Iteration of the optimisation solver 'sqp-legacy', which shows the decrease of the objective function, i.e. the first principal stress

![](./images/812349799939440641_21.jpg)

Fig. 11 Evaluation of the first principal stress with new design after 4 days

where the length of the axes of the hole change to reduce the first principal stress.

The contour plot of the first principal stress in Fig. 11 shows that the change of the hole parameters, in other words the design parameters, leads to an overall decrease of the first principal stress. Thereby, the constraint is fulfilled, i.e.

$$
g(\mathbf{v}, \mathbf{s})=\left|\frac{\mathrm{A}^{\text {ini }}-\mathrm{A}}{\mathrm{A}^{\text {ini }}}\right|-\overline{\mathrm{A}}=-2.7 \times 10^{-6} \leq 0, \quad(50)
$$

This example illustrates how shape has a major influence on the effects of degrading concentrations and that damage can be minimised by changing the shape. This observation is supported by Fig. 13 which shows the temporal course of the deformation based on the determinant of the degradation gradient, $\mathrm{J}^{\mathrm{d}}$, at the maximum loaded point. The curve is compared on the one hand with the initial shape, and on the other hand with the optimised shape, showing that the optimised form leads to a lower degradation.

![](./images/812349799939440641_22.jpg)

Fig. 12 Evaluation of the new design. a Initial structure vs. b optimal structure after 9 optimisation steps

![](./images/812349799939440641_23.jpg)

Fig. 13 Evaluation of the determinant of the degradation gradient $\mathrm{J}^{\mathrm{d}}$ in the marked point within 4 days, the blue line refers to the initial and the red line to the optimised design

### 6.1.1 Remarks on numerical investigation

In this paper, the mathematical optimisation is solved util- ising the MATLAB function fmincon, which calculates the minimum of a constrained nonlinear multivariable func- tion, see MathWorks (2019). The user can chooses between different algorithms to solve the task. In this section, the influence of the solution algorithm on the optimised result is evaluated. For this purpose, the result of the example 'Optimisation of a structure with a hole' is evaluated using three different algorithms. The 'sqp-legacy' and 'active-set' algorithm are based on sequential quadratic programming (SQP) method. Thereby, SQP is derived using the New- ton method and taking into account inequality constraints. The two algorithms differ in their implementation, e.g. they apply different definitions for the strict feasibility with respect to bounds or the choice of the solution algo- rithm for the subproblems. In contrast, the third algorithm 'interior-point' combines two different approaches to solve the optimisation task. The algorithm uses Newton steps or conjugated gradient steps depending on the solution of each iteration step.

Table 4 compares the efficiency of the algorithms and shows that algorithm 'sqp-legacy' runs most efficiently,

<table>
<caption>Table 4 Comparison of different solution algorithms</caption>
<thead>
<tr>
<th>Algorithm</th>
<th>Number of iterations</th>
<th>Time in seconds</th>
<th>Optimisation result</th>
</tr>
</thead>
<tbody>
<tr>
<td>'sqp-legacy'</td>
<td>9</td>
<td>18468</td>
<td>[5; 5.525]</td>
</tr>
<tr>
<td>'active-set'</td>
<td>17</td>
<td>34822</td>
<td>[5; 5.525]</td>
</tr>
<tr>
<td>'interior-point'</td>
<td>17</td>
<td>35177</td>
<td>[5; 5.525]</td>
</tr>
</tbody>
</table>

![](./images/812349799939440641_24.jpg)

![](./images/812349799939440641_25.jpg)

Fig. 14 Optimisation results under consideration of different mesh

because the solution is obtained after only 7 iterations, respectively after 18,468 seconds. The solutions are identical for all approaches.

Furthermore, Fig. 14 shows the optimised design taking into account different mesh sizes. The identical optimised parameters with $s=[5;5.525]$ are determined, but the computing time increases with the refinement of the mesh. In detail, the finer mesh shown in Fig. 14 needs 3.3 times more calculation time than the coarse mesh.

### 6.2 Optimisation of a bridge-like structure

This example is inspired by a bridge with mechanical loads under environmental influences, such as calcium leaching. This scenario can occur, for example during long-term exposure to pure water, which triggers the diffusion of calcium ions. To illustrate whether environmental influences are taken into account or not, the calculation is listed in the first step without and in the second step with the influence of chemical concentrations. In order to reduce the material costs, the objective $J(\mathbf{v}, s)$ of the problem is to minimise the area within a plane strain setting while holding a threshold for the first principal stress, i.e. $g(\mathbf{v}, s)$. The optimisation problem is obtained as follows

$$
\begin{aligned}
J(\mathbf{v}, s) & =\sum_{\mathrm{e}=1}^{\mathrm{NE}} \int_{\mathrm{B}_{0}^{\mathrm{e}}} \mathrm{dV} \\
g(\mathbf{v}, s) & =\mathrm{T}_{1}-\mathrm{T}_{1}^{\max },
\end{aligned}
\tag{51}
$$

wherein the area is calculated by the sum of the total element volumes. We apply a threshold for the maximum first principal stress $\mathrm{T}_{1}^{\max }$, thus the total optimisation problem follows with, i.e.

$$
\begin{aligned}
\min J(\mathbf{v}, s): & \boldsymbol{g}(\mathbf{v}, s) \leq 0 \text { constraints } \\
& s^{\mathrm{l}} \leq s \leq s^{\mathrm{u}} \text { limit values. }
\end{aligned}
\tag{52}
$$

<table>
<caption>Table 5 Material parameters for the bridge-like structure</caption>
<tbody>
<tr>
<td>E</td>
<td>=</td>
<td>3000 kN m−2</td>
</tr>
<tr>
<td>ν</td>
<td>=</td>
<td>0.2</td>
</tr>
<tr>
<td>ρ₀*</td>
<td>=</td>
<td>3000 kg m−3</td>
</tr>
<tr>
<td>M<sub>γ</sub></td>
<td>=</td>
<td>10 kg m−3</td>
</tr>
<tr>
<td>D</td>
<td>=</td>
<td>1 m² d−1</td>
</tr>
<tr>
<td>c<sub>γ</sub>(t=0)</td>
<td>=</td>
<td>1 mol m−3</td>
</tr>
</tbody>
</table>

To save computing time, the symmetry of the structure is utilised and the calculation is performed on half of the system using symmetry boundary conditions on the right side, see Fig. 15. Table 5 presents the applied material parameters. The applied forces with $\mathrm{F}=10 \mathrm{kN}$ lead to the first principal stress distribution, which is displayed in the contour plot in Fig. 18b. The formation of a tensile area in red and compression area in blue becomes visible.

![](./images/812349799939440641_26.jpg)

Fig. 15 Mechanical boundary conditions of the structure

The lower edge of the structure is defined by a B-spline function with four control points, where the design parameters are the control points that allow vertical displacement, see Fig. 16, i.e.

$$
s=\left[\mathrm{x}_{1} ; \mathrm{x}_{2} ; \mathrm{x}_{3} ; \mathrm{x}_{4}\right].
\tag{53}
$$

Utilisation of symmetry must also be taken into account for the calculation of design parameters during optimisation. For this purpose, the condition $\mathrm{x}_{3}=\mathrm{x}_{4}$ is introduced.

The parameters for the optimisation algorithm are shown in Table 6, where $s^{\mathrm{u}}$ and $s^{\mathrm{l}}$ are the matrices containing the minimum and maximum allowable change of design parameters. Figure 17 shows the iteration of the optimisation solver with the decrease of the objective function, i.e. the area of the structure. After 6 iterations the objective function converges, the side condition is fulfilled and a local minimum is given with the following design parameters

$$
s=[1 ; 0.893 ;-0.1372 ;-0.1372].
\tag{54}
$$

![](./images/812349799939440641_27.jpg)

Fig. 16 Design parameters for the structural optimisation

The design parameters reveal that the largest saving occurs in the area of the least stress, i.e. in the area where neither compressive nor tensile stress is present, whereby more material is required in the middle of the structure to ensure load-bearing capacity. In total, the optimised design

![](./images/812349799939440641_28.jpg)

Structural optimisation of diffusion driven degradation processes

<table><caption>Table 6 Input parameters for the optimisation algorithm</caption>
<tbody>
<tr>
<td>Threshold</td>
<td>$T_{1}^{\text{max}}$</td>
<td>$120$</td>
<td>$\text{kN}\,\text{m}^{-2}$</td>
</tr>
<tr>
<td>Limit values</td>
<td>$s^{\text{u}}$</td>
<td>$[1;1;1;1]$</td>
<td>$\text{m}$</td>
</tr>
<tr>
<td></td>
<td>$s^{\text{l}}$</td>
<td>$[-1;-1;-1;-1]$</td>
<td></td>
</tr>
<tr>
<td>Initial design</td>
<td>$s$</td>
<td>$[0;0;0;0]$</td>
<td>$\text{m}$</td>
</tr>
</tbody>
</table>

saves $20.6\%$ of the area. The contour plot in Fig. 18 represents the first principal stress in the optimised and initial design.

In a second step, the optimised bridge is additionally loaded by chemical concentrations. In this example, we focus on the general effect of any chemical concentrations that trigger material degradation. Additionally, to the mechanical force, two concentration inflows are located on the top of the structure and are provided by a concentration increase of $0.33\,\text{mol}\,\text{m}^{-3}$ per time step, see Fig. 19.

As already mentioned in the example in Section 4.2, the chemically induced degradation process is accelerated by running the simulation in time steps of days. The contour plots in Fig. 20 show the distribution of the concentrations and the resulting influence on the determinant of growth after 9 days. Figure 21 shows the time progression of the first principal stress in one nodal point, $\text{P}_{1}$, where the maximum first principal stress occurs. The first principal stress increases due to the increased concentrations. The previously defined maximum stress of $T_{1}^{\text{max}} = 120\,\text{kN}\,\text{m}^{-2}$ can no longer be maintained.

The aim of the optimisation is to save as much material as possible while still ensuring the load capacity. For this reason, smaller deviations in stress due to diffusion processes are also relevant, since otherwise the load-bearing capacity can no longer be guaranteed over a long load duration.

![](./images/812349799939440641_29.jpg)

Fig. 17 Iteration of the optimisation solver ‘sqp-legacy’, which records the decrease of the objective function, i.e. the area

![](./images/812349799939440641_30.jpg)

Fig. 18 Evaluation of the first principal stress induced by mechanical load. a Optimal structure with $T_{1}^{\text{max}} = 120\,\text{kN}\,\text{m}^{-2}$ vs. b initial structure with $T_{1}^{\text{max}} = 112\,\text{kN}\,\text{m}^{-2}$

![](./images/812349799939440641_31.jpg)

Fig. 19 Mechanical and concentrations boundary conditions of the structure

![](./images/812349799939440641_32.jpg)

Fig. 20 a Evaluation of the concentrations and b the impact on the determinant of the degradation part of deformation after 9 days

![](./images/812349799939440641_33.jpg)

![](./images/812349799939440641_34.jpg)

Fig. 21 Increase of maximum first principal stress over 9 days with chemical impact

By analogy with the previous example, the points of the polygon chain at the lower edge of the structure are design parameters. Using the same parameters for the optimisation algorithm as provided in Table 6 and starting from the initial design as illustrated in Fig. 15, the optimisation yields the following optimal design parameters

$$
s = \left[0.933; 0.793; -0.196; -0.196\right]. \tag{55}
$$

The iteration process illustrated in Fig. 22 shows how the design parameters reduce the objective function by 17.4 % while maintaining the constraints. The increased maximum first principal stress due to the degradation process changes the optimal design and allows for less material saving, as shown in Fig. 23. It is clear that the consideration of environmental conditions, such as calcium leaching, are necessary to predict long-term performance.

![](./images/812349799939440641_35.jpg)

Fig. 22 Iteration of the optimisation solver 'sqp-legacy' for the example coupled to chemical impact, which shows the decrease of the objective function, i.e. the area

![](./images/812349799939440641_36.jpg)

Fig. 23 Comparison of the results: the green coloured area shows the optimal result when chemical influence is considered and the red area shows the result without degradation processes

## 7 Summary

In this paper, a coupled mechanical-diffusion-degradation model is presented. The degradation process is derived by a multiplicative split of the deformation gradient and a constitutive approach for the development of growth, which assumes chemical concentrations as a trigger for degradation. The numerical FE framework is briefly presented. Furthermore, the embedding of a structural optimisation framework is outlined. The applicability of the model is presented for a structure with a hole and a beam for which a practical reference is outlined. The main focus of the examples lies in the analysis of the influence of long-term acting chemical concentrations, which can influence the mechanical stress and can keep certain upper limits of the stress by constructive changes.

For future work, an alternative to the numerical finite difference method will be applied, namely the variational sensitivity analysis as outlined in Barthold and Stein (1996), which accelerates the simulation time.

Overall, it is shown that the model can provide an optimal design taking into account long-term effects from concen- trations that damage the material, while still maintaining certain limits for the load-bearing capacity. The algorithm offers the possibility to integrate different chemical pro- cesses, to calculate the interaction with the mechanical behaviour and to solve optimisation problems.

Funding Open Access funding enabled and organized by Projekt DEAL.

## Declarations

Replication of results The described method is outlined in the essential steps and the continuous formulation is elaborated. Furthermore, the most important algorithmic features are discussed. The examples contain all necessary information about the material model and geometry parameters required for replication.

Conflict of interests The authors declare no competing

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate

Structural optimisation of diffusion driven degradation processes

if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit https://creativecommons.org/licenses/by/4.0/.

## References

Ambrosi D, Mollica F (2002) On the mechanics of a growing tumor. Int J Eng Sci 40(12):1297–1316. https://doi.org/10.1016/S0020-7225(02)00014-9

Barthold FJ (2002) Zur Kontinuumsmechanik inverser Geome- trieprobleme. TU Braunschweig, https://doi.org/10.17877/DE290R-13502

Barthold FJ, Stein E (1996) A continuum mechanical-based formulation of the variational sensitivity analysis in struc- tural optimization. Part 1: Anal Struct Optim 11(1-2):29–42. https://doi.org/10.1007/BF01279652

Chen YC, Hoger A (2000) Constitutive functions of elastic materials in finite growth and deformation. J Elast Phys Sci solids 59(1):175–193. https://doi.org/10.1023/A:1011061400438

Chester SA, Anand L (2010) A coupled theory of fluid permeation and large deformations for elastomeric materials. J Mech Phys Solids 58(11):1879–1906. https://doi.org/10.1016/j.jmps.2010.07.020

Choi YS, Yang EI (2013) Effect of calcium leaching on the pore structure, strength, and chloride penetration resis- tance in concrete specimens. Nucl Eng Des 259:126–136. https://doi.org/10.1016/j.nucengdes.2013.02.049

Christensen PW, Klarbring A (2008) An introduction to structural optimization, solid mechanics and its applications, vol 153. Springer, Berlin. https://doi.org/10.1007/978-1-4020-8666-3

Cowin S, Hegedus D (1976) Bone remodeling 1: Theory of adaptive elasticity. J Elast 6(3):313–326. https://doi.org/10.1007/BF00041724

Epstein M, Maugin GA (2000) Material evolution in plasticity and growth. In: Continuum thermomechanics. Springer, pp 153–162. https://doi.org/10.1007/0-306-46946-4_11

Ganghoffer JF (2010) Mechanical modeling of growth considering domain variation — Part II: Volumetric and surface growth involving Eshelby tensors. J Mech Phys Solids 58(9):1434–1459. https://doi.org/10.1016/j.jmps.2010.05.003

Ganghoffer JF, Plotnikov PI (2014) Mathematical modeling of vol- umetric material growth in thermoelasticity. J Elast 117(1):111–138. https://doi.org/10.1007/s10659-014-9467-4

Gérard B, Le Bellego C, Bernard O (2002) Simplified modelling of calcium leaching of concrete in various environments. Mater Struct 35(10):632–640. https://doi.org/10.1007/BF02480356

Gleason R, Humphrey J (2005) Effects of a sustained extension on arterial growth and remodeling: a theoretical study. J Biomech 38(6):1255–1261. https://doi.org/10.1016/j.jbiomech.2004.06.017

Guhr F, Sprave L, Barthold FJ, Menzel A (2020) Computational shape optimisation for a gradient-enhanced continuum damage model. Comput Mech 65(4):1105–1124. https://doi.org/10.1007/s00466-019-01810-3

Harrigan TP, Hamilton JJ (1992) An analytical and numerical study of the stability of bone remodelling theories: dependence on microstructural stimulus. J Biomech 25(5):477–488. https://doi.org/10.1016/0021-9290(92)90088-I

Himpel G, Kuhl E, Menzel A, Steinmann P (2005) Computational modelling of isotropic multiplicative growth. Comput Model Eng Sci 8:119–134. https://doi.org/10.3970/cmes.2005.008.119

Kuhl D (2005) Modellierung und Simulation von Mehrfeldproble- men der Strukturmechanik, Habilitation Institute for Structural Mechanics, Ruhr University Bochum, Bochum

Kuhl D, Bangert F, Meschke G (2004) Coupled chemo-mechanical deterioration of cementitious materials. part i: Modeling. Int J Solids Struct 41:15–40. https://doi.org/10.1016/j.ijsolstr.2003.08.005

Kuhl E, Menzel A, Steinmann P (2003) Computational modeling of growth. Comput Mech 32(1-2):71–88. https://doi.org/10.1007/s00466-003-0463-y

Lubarda VA, Hoger A (2002) On the mechanics of solids with a growing mass. Int J Solids Struct 39:4627–4664. https://doi.org/10.1016/S0020-7683(02)00352-9

MathWorks (2019) Global optimization toolbox: User's Guide (R2019b). https://www.mathworks.com/help/releases/R2019b/pdf_doc/optim/optim_tb.pdf

Menzel A (2005) Modelling of anisotropic growth in bio- logical tissues. Biomech Model Mechanobiol 3(3):147–171. https://doi.org/10.1007/s10237-004-0047-6

Menzel A (2007) A fibre reorientation model for orthotropic multiplicative growth. Biomech Model Mechanobiol 6(5):303–320. https://doi.org/10.1007/s10237-006-0061-y

Menzel A, Kuhl E (2012) Frontiers in growth and remodeling. Mech Res Commun 42:1–14. https://doi.org/10.1016/j.mechrescom.2012.02.007

Noël L, Duysinx P, Maute K (2017) Level set topology optimization considering damage. Struct Multidiscip Optim 56(4):737–753. https://doi.org/10.1007/s00158-017-1724-2

Rodriguez EK, Hoger A, McCulloch AD (1994) Stress-dependent finite growth in soft elastic tissues. J Biomech 27(4):455–467. https://doi.org/10.1016/0021-9290(94)90021-3

Simon D (2013) Evolutionary optimization algorithms. Wiley, New York

Suresh S, Lindström SB, Thore CJ, Torstenfelt B, Klarbring A (2018) An evolution-based high-cycle fatigue constraint in topology opti- mization. In: International Conference on Engineering Optimiza- tion. Springer, pp 844–857. https://doi.org/10.1007/978-3-319-97773-7_73

Vrugt JA, Robinson BA (2007) Improved evolutionary optimization from genetically adaptive multimethod search. Proc Natl Acad Sci 104(3):708–711. https://doi.org/10.1073/pnas.0610471104

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](./images/812349799939440641_37.jpg)
