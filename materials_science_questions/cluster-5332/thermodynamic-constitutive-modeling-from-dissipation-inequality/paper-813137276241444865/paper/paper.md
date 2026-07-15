Continuum Mech. Thermodyn.
DOI 10.1007/s00161-017-0571-0

![](./images/813137276241444865_1.jpg)

ORIGINAL ARTICLE

Fadi Aldakheel

# Micromorphic approach for gradient-extended thermo-elastic-plastic solids in the logarithmic strain space

This paper is dedicated to the memory of the late Professor Christian Miehe

Received: 16 January 2017 / Accepted: 22 April 2017
© Springer-Verlag Berlin Heidelberg 2017

Abstract The coupled thermo-mechanical strain gradient plasticity theory that accounts for microstructure-based size effects is outlined within this work. It extends the recent work of Miehe et al. (Comput Methods Appl Mech Eng 268:704–734, 2014) to account for thermal effects at finite strains. From the computational viewpoint, the finite element design of the coupled problem is not straightforward and requires additional strategies due to the difficulties near the elastic–plastic boundaries. To simplify the finite element formulation, we extend it toward the *micromorphic approach* to gradient thermo-plasticity model in the logarithmic strain space. The key point is the introduction of dual local–global field variables via a penalty method, where only the global fields are restricted by boundary conditions. Hence, the problem of restricting the gradient variable to the plastic domain is relaxed, which makes the formulation very attractive for finite element implementation as discussed in Forest (J Eng Mech 135:117–131, 2009) and Miehe et al. (Philos Trans R Soc A Math Phys Eng Sci 374:20150170, 2016).

Keywords Size effects · Finite gradient plasticity · Micromorphic regularization · Thermo-mechanical processes

## 1 Introduction

The modeling of size effects in elastic–plastic solids must be based on nonstandard theories which incorporate length scales. Hereby, additional internal variables and their nonlocal counterparts can be introduced to reflect the microstructural response. Various observations underline the need for such extended continuum theories of inelasticity. A first physically based motivation is the experimentally observed *increase in strength* of metallic structures with diminishing size, resulting from dislocation-related hardening effects, see for example Fleck et al. [4]. A further key motivation for the use of strain gradient theory arises from the computation of localized plastic deformation in softening materials with *finite element techniques*, yielding for local theories the pathological mesh dependencies for zero length scale. To overcome this nonphysical behavior, gradient-enhanced plasticity models are used as *regularization methods*, which provide the existence of a length scale, see for example De Borst and Mühlhaus [5], Liebe and Steinmann [6] and Engelen et al. [7]. The gradient-enhanced models are naturally rooted in the micromechanical descriptions of the dislocation flow in crystals, where the *plastic length scale* is related to the lattice spacing. Associated models of gradient crystal plasticity are proposed by many authors, e.g., Gurtin [8], Svendsen and Bargmann [9], Wulfinghoff and Böhlke [10],

Communicated by Andreas Öchsner.

F. Aldakheel (⊠)
Institute of Applied Mechanics (Civil Engineering), Chair I, University of Stuttgart, Pfaffenwaldring 7, 70569 Stuttgart, Germany
E-mail: fadi.aldakheel@mechbau.uni-stuttgart.de; fadialdakheel@googlemail.com
URL:http://www.mechbau.uni-stuttgart.de/lsl/members/scientific/aldakheel

Published online: 06 May 2017

Klusemann and Yalcinkaya [11] and Miehe et al. [12]. In contrast, pure phenomenologically based theories of gradient plasticity often use plastic length scales as limiters of localized zones determined by macroscopic experiments, see for example Forest and Sievert [13], Gudmundson [14], Anand et al. [15], Reddy et al. [16], Fleck and Willis [17,18], Polizzotto [19], Forest [2,20], Voyiadjis et al. [21], Kuroda and Tvergaard [22] and Miehe et al. [1,23].

Despite the fact that temperature distribution during heat accumulation has a strong influence on the mechanical properties, thermal effects were not included in the constitutive formulation of most of the recently developed strain gradient theories. Thermo-mechanical problems can be seen in different engineering applications, which exhibit a two-side coupling phenomenon. First, the effects of the thermal field on the mechanical field results in thermal expansion and temperature dependence of the mechanical properties, for instance the bridge joint expansion/contraction and the buckled railway tracks as a result of changes in the ambient temperature. On the contrary, the action of the mechanical field on the thermal field leads to high-temperature distribution and heat dissipation, such as the frictional heating of disk brakes in automotive industry. To this end, Wriggers et al. [24] investigate the thermo-mechanical behavior of the necking problem in classical elasto-plasticity. Here the authors observed that the development of a neck in a uniaxial tension test is influenced by the heat production due to inelastic deformation. Anand et al. [25] proposed a coupled thermo-mechanical elasto-viscoplasticity theory to model strain rate and temperature-dependent large-deformation response of amorphous polymeric materials. A variational formulation for the thermo-mechanical coupling in finite strain plasticity theory with nonlinear kinematic hardening is outlined in Canadija and Mosler [26] based on the works Yang et al. [27] and Stainier and Ortiz [28]. However, no size effects were involved in the constitutive formulation. This has motivated Voyiadjis and Faghihi [29] and Faghihi et al. [30] to propose a nonlocal thermodynamic consistent framework with energetic and dissipative gradient length scales that addressing the coupled thermal and mechanical responses of materials in small scales and fast transient process. In this context, Forest and Aifantis [31] introduced some links between recent gradient thermo-elasto-plasticity theories and the thermo-mechanics of generalized continua based on the micromorphic approach. Extensions to an anisotropic model for gradient thermo-plasticity can be seen in the work of Bertram and Forest [32]. Recently Wcislo and Pamin [33] developed a gradient-enhanced thermo-mechanical model that is strictly related to the phenomenon of thermal softening. It incorporates higher order gradients of the temperature field. In this work, we extend the above-mentioned gradient plasticity model introduced in Miehe et al. [1] to account for thermal effects at finite deformations in the logarithmic strain space. The key goal of this work is the extension toward the micromorphic regularization of the coupled problem to simplify the mixed finite element formulation as outlined in the recent works Miehe et al. [3,34]. This is achieved by considering an extended set of plastic variables which are linked by penalty term in a modified energetic response function as discussed in Forest [2,20] and Miehe et al. [34]. The advantage of such a formulation lies on the computational side, in particular on the side of gradient plasticity. It allows a straightforward finite element formulation of gradient plasticity that does not need to account of sharp plastic boundaries. From the numerical implementation aspects, an operator split scheme is considered for the coupled problem, in line with our recent works Aldakheel [35] and Aldakheel and Miehe [36] at small strains. It leads to a two-step solution procedure $\mathrm{ALGO_{TM}} = \mathrm{ALGO_{Thermo}} \circ \mathrm{ALGO_{Mech}}$, where the mechanical and thermal problems are solved separately. The idea here is to decompose the coupled field equations of finite gradient thermo-plasticity into an elasto-plastic problem $\mathrm{ALGO_{Mech}}$ with frozen temperature, followed by a heat conduction problem $\mathrm{ALGO_{Thermo}}$ at fixed updated mechanical configuration. These two subproblems are then coupled via the plastic structural heating and the mechanical dissipation. Due to the two-step solution procedure, we end up with a symmetric structure for each subproblem; for further details on the numerical analysis, we refer to our recent work Aldakheel and Miehe [36] at small strains.

## 2 Introduction of primary field variables

### 2.1 Deformation map and temperature field

Let $\mathcal{B} \in \mathcal{R}^d$ with $d=2,3$ be the reference configuration of the body of interest. We study thermo-elasto-plastic deformations at time $t \in \mathcal{R}_+$, described by the deformation map $\boldsymbol{\varphi}(\boldsymbol{X}, t)$ and the temperature field $\theta(\boldsymbol{x}, t)>0$

$$
\boldsymbol{\varphi}:\left\{\begin{aligned}
\mathcal{B} \times \mathcal{T} & \rightarrow \mathcal{R}^3 \\
(\boldsymbol{X}, t) & \mapsto \boldsymbol{x}=\boldsymbol{\varphi}(\boldsymbol{X}, t)
\end{aligned} \quad \theta:\left\{\begin{aligned}
\mathcal{B} \times \mathcal{T} & \rightarrow \mathcal{R} \\
(\boldsymbol{X}, t) & \mapsto \theta(\boldsymbol{X}, t)
\end{aligned}\right.\right.
\tag{1}
$$

Micromorphic approach for gradient-thermo-plasticity

![](./images/813137276241444865_2.jpg)

Fig. 1 Primary fields. a The macro-motion field $\boldsymbol{\varphi}$ is constrained by the Dirichlet- and Neumann-type BCs $\boldsymbol{\varphi}=\boldsymbol{\varphi}_{D}$ on $\partial \mathcal{B}^{\varphi}$ and $\boldsymbol{P} \cdot \boldsymbol{n}=\overline{\boldsymbol{t}}$ on $\partial \mathcal{B}^{\mathrm{t}}$. b The absolute temperature field $\theta$ is constrained by the Dirichlet- and Neumann-type BCs $\theta=\theta_{D}$ on $\partial \mathcal{B}^{\theta}$ and $\boldsymbol{Q} \cdot \boldsymbol{n}=\bar{h}$ on $\partial \mathcal{B}^{\mathrm{h}}$. c The long-range micromotion field $\alpha$ is restricted by the conditions $\alpha=\alpha_{D}$ on $\partial \mathcal{B}^{\alpha}$ and $\partial_{\nabla \alpha} \Psi \cdot \boldsymbol{n}=0$ on $\partial \mathcal{B}^{\mathrm{f}}$. d, e The short-range micromotion fields $\boldsymbol{\varepsilon}^{\mathrm{p}}$ and $\bar{\alpha}$ are locally defined and not constrained by boundary conditions

as depicted in Fig. 1. The material deformation gradient is defined by $\boldsymbol{F}:=\nabla \boldsymbol{\varphi}_{t}(\boldsymbol{X})$ with $J:=\operatorname{det}[\boldsymbol{F}]>0$. The solid is loaded by prescribed deformations and external traction on the boundary, defined by time-dependent ("active") Dirichlet and Neumann conditions

$$
\boldsymbol{\varphi}=\bar{\boldsymbol{\varphi}}(\boldsymbol{X}, t) \text { on } \partial \mathcal{B}^{\varphi} \quad \text { and } \quad \boldsymbol{P} \boldsymbol{n}=\overline{\boldsymbol{t}}(\boldsymbol{X}, t) \text { on } \partial \mathcal{B}^{\mathrm{t}}
\tag{2}
$$

on the surface $\partial \mathcal{B}=\partial \mathcal{B}^{\varphi} \cup \partial \mathcal{B}^{\mathrm{t}}$ of the undeformed configuration. The first Piola stress tensor $\boldsymbol{P}$ is the thermodynamic dual to $\boldsymbol{F}$. For the thermal problem, the time-dependent ("active") Dirichlet and Neumann conditions of the absolute temperature field $\theta$ are defined as

$$
\theta=\theta_{D} \text { on } \partial \mathcal{B}^{\theta} \quad \text { and } \quad \boldsymbol{Q} \cdot \boldsymbol{n}=\bar{h} \text { on } \partial \mathcal{B}^{\mathrm{h}}
\tag{3}
$$

with a prescribed temperature field $\theta_{D}$ and heat flux $\bar{h}$. Note that the nominal heat flux vector $\boldsymbol{Q}=J \boldsymbol{F}^{-1} \boldsymbol{q}$ is given by Fourier's law which states that heat exchanges always from hotter to colder regions, i.e.

$$
\boldsymbol{q}:=-K \nabla \theta
\tag{4}
$$

where $\nabla \theta$ is the gradient of the temperature field and $K$ is the thermal conductivity which must be positive ($K>0$) in order to achieve thermodynamical consistency. Following Miehe et al. [37], we focus on a phenomenological setting of finite thermo-plasticity based on an additive decomposition of a Lagrangian Hencky strain $\boldsymbol{\varepsilon}$. This allows to define a stress producing elastic strain measure

$$
\boldsymbol{\varepsilon}^{\mathrm{e}}:=\boldsymbol{\varepsilon}-\boldsymbol{\varepsilon}^{\mathrm{p}}-\boldsymbol{\varepsilon}^{\theta} \quad \text { with } \quad \boldsymbol{\varepsilon}:=\frac{1}{2} \ln \boldsymbol{C} \quad \text { and } \quad \boldsymbol{C}:=\boldsymbol{F}^{\mathrm{T}} \boldsymbol{g} \boldsymbol{F},
\tag{5}
$$

where $\boldsymbol{C}$ is the right Cauchy-Green tensor, i.e., the representation of the Eulerian standard metric $\boldsymbol{g}$ in the reference configuration. The Lagrangian plastic strain measure $\boldsymbol{\varepsilon}^{\mathrm{p}}$ is chosen as a local internal variable. It starts to evolve from the initial condition $\boldsymbol{\varepsilon}^{\mathrm{p}}(\boldsymbol{X}, t_{0})=\boldsymbol{0}$. The thermal contribution to the total deformation is defined as

$$
\boldsymbol{\varepsilon}^{\theta}=\alpha_{\mathrm{T}}\left(\theta-\theta_{0}\right) \boldsymbol{I}
\tag{6}
$$

representing an expansion of the body under thermal loading. Here, $\alpha_{\mathrm{T}}$ is the linear thermal expansion modulus and $\theta_{0}$ a reference temperature.

### 2.2 Isotropic strain gradient plasticity

We consider a framework of isotropic gradient plasticity in the micromorphic regularization setting. To this end, a scalar isotropic hardening variable $\alpha(\boldsymbol{X}, t)$ is introduced that defines the micromorphic hardening variable by the modified Helmholtz equation

$$
\alpha-l_{\mathrm{mp}}^{2} \Delta \alpha=\bar{\alpha}
\tag{7}
$$

determining the link of the local equivalent plastic strain variable $\bar{\alpha}$ to the micromorphic variable $\alpha$, in line with the pioneering works of Engelen et al. [7], Geers et al. [38], Peerlings et al. [39,40] and Forest [2]. $l_{\mathrm{mp}}$ is

the plastic *length scale* in the micromorphic setting that accounts for size effects to overcome the nonphysical mesh sensitivity of the localized plastic deformation in softening materials. The generalized internal variable field $\alpha$ is considered as passive in the sense that an external driving is not allowed. This is consistent with the time-independent (passive) Dirichlet and Neumann conditions

$$
\alpha=0 \text { on } \partial \mathcal{B}^{\alpha} \quad \text { and } \quad \nabla \alpha \cdot \boldsymbol{n}=\boldsymbol{0} \text { on } \partial \mathcal{B}^{\nabla \alpha}
\tag{8}
$$

on the surface $\partial \mathcal{B}$ as illustrated in Fig. 1, defining "micro-clamped" and "free" constraints for the evolution of the plastic deformation. Note carefully that the variable $\alpha$ is now defined in the full domain and not restricted to the plastic zone, whereas the linear hardening variable $\bar{\alpha}$ is *locally* defined by the ordinary differential evolution equation

$$
\dot{\bar{\alpha}}=\sqrt{\frac{2}{3}}\left\|\dot{\boldsymbol{\varepsilon}}^{\mathrm{p}}\right\| \quad \text { with } \quad \dot{\bar{\alpha}} \geq 0.
\tag{9}
$$

## 2.3 Global primary fields and constitutive state variables

The above-introduced variables will characterize a multi-field setting of thermo-mechanical strain gradient plasticity based on three *global primary fields*

$$
\mathfrak{U}:=\{\boldsymbol{\varphi}, \theta, \alpha\},
\tag{10}
$$

the deformation map $\boldsymbol{\varphi}$, the absolute temperature field $\theta$ and the micromorphic hardening variable $\alpha$. In addition, the plastic strain field $\boldsymbol{\varepsilon}^{\mathrm{p}}$ and the local equivalent plastic strain $\bar{\alpha}$ serve as additional *local primary fields*, as demonstrated in Fig. 1. The subsequent constitutive approach to the coupled gradient thermo-plasticity focuses on the set

$$
\mathfrak{C}:=\left\{\boldsymbol{\varepsilon}, \boldsymbol{\varepsilon}^{\mathrm{p}}, \bar{\alpha}, \theta, \alpha, \nabla \theta, \nabla \alpha\right\}.
\tag{11}
$$

The gradient of the plastic strains do not enter the constitutive state. Thus, $\boldsymbol{\varepsilon}^{\mathrm{p}}$ and $\bar{\alpha}$ are *short-range* variables, whose evolution is described by an ODE, while the micromorphic hardening variable $\alpha$ is a *long-range* field with a PDE-type evolution.

# 3 Constitutive functions of the coupled problem

## 3.1 Energetic response function

With the constitutive state variables introduced in (11), the free energy function for the coupled thermo-mechanical strain gradient plasticity at finite strains takes the form

$$
\widehat{\Psi}(\mathfrak{C})=U(J)+\bar{\Psi}_{\log }^{\mathrm{e}}\left(\overline{\boldsymbol{\varepsilon}}^{\mathrm{e}}\right)+\bar{\Psi}^{\mathrm{p}}(\bar{\alpha}, \alpha, \nabla \alpha ; \theta)+M(J, \theta)+T(\theta).
\tag{12}
$$

### 3.1.1 Elastic contribution

The isotropic elastic contribution is assumed to be a quadratic function and is decomposed into volumetric and isochoric parts as

$$
U(J)=\frac{\kappa}{2}(J-1)^{2} \quad \text { and } \quad \bar{\Psi}_{\log }^{\mathrm{e}}\left(\overline{\boldsymbol{\varepsilon}}^{\mathrm{e}}\right)=\mu\left\|\overline{\boldsymbol{\varepsilon}}^{\mathrm{e}}\right\|^{2},
\tag{13}
$$

in terms of the elastic bulk modulus $\kappa$ and the shear modulus $\mu$. In this model, both $\kappa$ and $\mu$ are considered as constants material parameters. The isochoric elastic strain tensor is defined in the logarithmic strain space as

$$
\overline{\boldsymbol{\varepsilon}}^{\mathrm{e}}:=\overline{\boldsymbol{\varepsilon}}-\boldsymbol{\varepsilon}^{\mathrm{p}} \quad \text { with } \quad \overline{\boldsymbol{\varepsilon}}:=\frac{1}{2} \ln \bar{C} \quad \text { and } \quad \bar{C}:=J^{-2 / 3} C
\tag{14}
$$

Micromorphic approach for gradient-thermo-plasticity

### 3.1.2 Plastic contribution

The plastic part of the energy function (12) is decomposed into local and gradient parts, in terms of variables which describe the strain gradient hardening effect. For the modeling of length scale effects in isotropic gradient plasticity, we focus on the micromorphic hardening variable $\alpha$ and its gradient $\nabla \alpha$ in addition to the local equivalent plastic strain $\bar{\alpha}$. It is assumed to have the form

$$
\bar{\Psi}^{\mathrm{p}}=\frac{h(\theta)}{2} \bar{\alpha}^{2}+\left[y_{\infty}(\theta)-y_{0}(\theta)\right](\bar{\alpha}+\exp [-\delta \bar{\alpha}] / \delta)+\frac{\mu l_{\mathrm{p}}^{2}}{2}\|\nabla \alpha\|^{2}+\frac{\epsilon_{\mathrm{p}}}{2}(\bar{\alpha}-\alpha)^{2}.
$$

The first and second contributions characterize a local plastic hardening and thermal softening mechanism. $l_{\mathrm{p}} \geq 0$ is a plastic length scale related to a strain gradient hardening effect. The local variable $\bar{\alpha}$ is then linked to the global micromorphic field variable $\alpha$ by the quadratic penalty term, where $\epsilon_{\mathrm{p}}$ is an additional material parameter. Note that for $\epsilon_{\mathrm{p}} \rightarrow \infty$ the above micromorphic extensions recover the original setting of the gradient-extended theory introduced in Miehe et al. [1]. The three temperature-dependent material parameters $y_{0}>0, y_{\infty} \geq y_{0}$ and $h \geq 0$ in (15) defined as

$$
\begin{aligned}
h(\theta) & :=h\left[1-w_{\mathrm{h}}\left(\theta-\theta_{0}\right)\right] \\
y_{0}(\theta) & :=y_{0}\left[1-w_{0}\left(\theta-\theta_{0}\right)\right] \\
y_{\infty}(\theta) & :=y_{\infty}\left[1-w_{\mathrm{h}}\left(\theta-\theta_{0}\right)\right]
\end{aligned}
$$

as outlined in Simó and Miehe [41], where $w_{\mathrm{h}}$ is the hardening/softening parameter, $w_{0}$ is the flow stress softening parameter and $\delta$ is the saturation parameter. The initial yield stress $y_{0}$ determines the threshold of the elastic response. Note that the parameters: $\delta, \mu, l_{\mathrm{p}}$ and $\epsilon_{\mathrm{p}}$ are considered as constants in Eq. (15).¹

### 3.1.3 Thermo-elastic contribution

The coupled thermo-elastic part of the free energy is linear and has the simple form

$$
M(J, \theta)=-\kappa \alpha_{\mathrm{T}}(J-1)\left(\theta-\theta_{0}\right),
$$

where $\alpha_{\mathrm{t}}$ is the thermal expansion coefficient and $\theta_{0}$ is the reference temperature.

### 3.1.4 Thermal contribution

The purely thermal part is defined as

$$
T(\theta)=c\left[\left(\theta-\theta_{0}\right)-\theta \ln \frac{\theta}{\theta_{0}}\right],
$$

where $c$ is the heat capacity coefficient.

### 3.2 Dissipative response function

For the subsequent modeling of thermo-plasticity, we introduce dissipative force fields on the solid domain $\mathcal{B}$ dual to the constitutive state $\mathfrak{C}$ introduced in (11) as

$$
\bar{s}:=-\partial_{\boldsymbol{\varepsilon}^{\mathrm{p}}} \widehat{\Psi}, \quad f^{\alpha}:=\partial_{\bar{\alpha}} \widehat{\Psi}, \quad \delta_{\alpha} \widehat{\Psi}=0 .
$$

where $\bar{s}$ is dual to $\boldsymbol{\varepsilon}^{\mathrm{p}}$ and $f^{\alpha}$ dual to $\bar{\alpha}$. For a simple model of von Mises-type gradient thermo-plasticity, the yield criterion function based on the driving forces and the temperature field $\theta$ is defined as

$$
\chi\left(f^{\alpha}, \bar{s}, \theta\right):=\|\bar{s}\|-\sqrt{\frac{2}{3}}\left[y_{0}(\theta)+f^{\alpha}\right]
$$

---
¹ The shear modulus $\mu$ could be also dependent on the temperature as suggested in Boyce et al. [42] through the empirical relation

$$
\widehat{\mu}(\theta)=\exp \left[\log \left(\mu_{0}\right)-C_{\mathrm{s}}\left(\theta-\theta_{0}\right)\right]
$$

in terms of the modulus $\mu_{0}$ at the reference temperature $\theta_{0}$ and a sensitivity parameter $C_{\mathrm{s}}$.

where $y_0(\theta)$ is the temperature-dependent yield strength defined in (16). With the yield function at hand, one can define the dual dissipation function for gradient-type thermal viscoplasticity according to Perzyna-type viscoplasticity model as

$$
\Phi^{*}\left(f^{\alpha}, \overline{s}, \theta\right):=\frac{1}{2 \eta_{\mathrm{p}}}\left\langle\|\overline{s}\|-\sqrt{\frac{2}{3}}\left[y_{0}(\theta)+f^{\alpha}\right]\right\rangle^{2}
\tag{22}
$$

with $\eta_{\mathrm{p}}$ being the viscosity parameter that accounts for rate dependency. Here, $\langle x\rangle:=(x+|x|) / 2$ is the Macaulay bracket. In Eq. (20), $\delta_{\alpha} \widehat{\Psi}$ denotes the variational derivative of $\widehat{\Psi}$ with respect to the global micromorphic variable $\alpha$, defining the additional micromorphic balance equation that links the local variable $\bar{\alpha}$ to the global field $\alpha$

$$
\delta_{\alpha} \widehat{\Psi}=\partial_{\alpha} \widehat{\Psi}-\operatorname{Div}\left[\partial_{\nabla \alpha} \widehat{\Psi}\right]=0,
\tag{23}
$$

along with the Neumann-type boundary conditions defined in Eq. (8). Taking the necessary derivatives, we end up with the modified Helmholtz equation determining the link of the local variable $\bar{\alpha}$ to the micromorphic variable $\alpha$

$$
\boxed{\alpha-l_{\mathrm{mp}}^{2} \Delta \alpha=\bar{\alpha} \quad \text { with } \quad l_{\mathrm{mp}}:=l_{\mathrm{p}} \sqrt{\mu / \epsilon_{\mathrm{p}}}}
\tag{24}
$$

where $l_{\mathrm{mp}}$ is the plastic length scale of the micromorphic theory. $^{2}$ Note carefully that the variable $\alpha$ is now defined in the full domain and not restricted to the plastic zone, whereas the linear hardening variable $\bar{\alpha}$ is locally defined by the ordinary differential evolution equation introduced in (9). This provides a substantial simplification with regard to the finite element implementation without tracking of elastic-plastic boundaries. To this end, we depict in Fig. 2a one-dimensional finite element solutions of gradient plasticity for canonical setting in which the global equivalent plastic strains evolution is $\dot{\bar{\alpha}}=\partial_{f^{\alpha}} \Phi^{*}$, see Miehe et al. [1], which is restricted to the plastic domain resulting in nonphysical oscillations at the elastic-plastic boundary; these are relaxed in Fig. 2b by the micromorphic approach according to Eqs. (23) and (24).

### 3.3 Local-global constitutive equations

The balance and evolution equations describing the coupled problem are split up into **Local** and **Global** constitutive equations in the micromorphic regularization setting as

$$
\left.
\begin{array}{ll}
\text { 1. } \quad \text { Stress equilibrium } & \operatorname{Div}\left[\partial_{\boldsymbol{F}} \widehat{\Psi}\right]=\mathbf{0} \\
\text { 2. } \quad \text { Micromorphic hardening } & \partial_{\alpha} \widehat{\Psi}-\operatorname{Div}\left[\partial_{\nabla \alpha} \widehat{\Psi}\right]=0 \\
\text { 3. } \quad \text { Temperature field } & c \dot{\theta}+\operatorname{Div}[\boldsymbol{Q}]-\mathcal{D}_{\text {loc }}^{\text {red }}=0
\end{array}
\right\} \quad (\mathbf{G})
$$

$$
\left.
\begin{array}{ll}
\text { 4. } \quad \text { Hardening force } & \partial_{\bar{\alpha}} \widehat{\Psi}-f^{\alpha}=0 \\
\text { 5. } \quad \text { Plastic force } & \partial_{\boldsymbol{\varepsilon}^{\mathrm{p}}} \widehat{\Psi}+\overline{\boldsymbol{s}}=\mathbf{0} \\
\text { 6. } \quad \text { Equivalent strain } & -\dot{\bar{\alpha}}+\partial_{f^{\alpha}} \Phi^{*}=0 \\
\text { 7. } \quad \text { Plastic strains } & \dot{\boldsymbol{\varepsilon}}^{\mathrm{p}}-\partial_{\overline{\boldsymbol{s}}} \Phi^{*}=\mathbf{0}
\end{array}
\right\} \quad (\mathbf{L})
\tag{26}
$$

in terms of the reduced local dissipation density function defined as

$$
\mathcal{D}_{\mathrm{loc}}^{\mathrm{red}}=\partial_{\overline{\boldsymbol{\varepsilon}}} \widehat{\Psi}: \dot{\boldsymbol{\varepsilon}}^{\mathrm{p}}-\partial_{\bar{\alpha}} \widehat{\Psi} \dot{\bar{\alpha}}-\partial_{\alpha} \widehat{\Psi} \dot{\alpha}-\partial_{\nabla \alpha} \widehat{\Psi} \cdot \nabla \dot{\alpha}
\tag{27}
$$

along with the Neumann-type boundary conditions

$$
\partial_{\boldsymbol{F}} \widehat{\Psi} \cdot \boldsymbol{n}=\overline{\boldsymbol{t}} \text { on } \partial \mathcal{B}^{\mathrm{t}} \quad, \quad \partial_{\nabla \alpha} \widehat{\Psi} \cdot \boldsymbol{n}=\boldsymbol{0} \text { on } \partial \mathcal{B}^{\mathrm{f}} \quad \text { and } \quad \boldsymbol{Q} \cdot \boldsymbol{n}=0 \text { on } \partial \mathcal{B}^{\mathrm{h}}
\tag{28}
$$

---
$^{2}$ If the shear modulus $\mu=\widehat{\mu}(\theta)$ is assumed to be temperature dependent, additional term must be defined in Eq. (24) to account for thermal effects

$$
\alpha-\frac{l_{\mathrm{p}}^{2}}{\epsilon_{\mathrm{p}}} \widehat{\mu}(\theta) \Delta \alpha-\frac{l_{\mathrm{p}}^{2}}{\epsilon_{\mathrm{p}}} \partial_{\theta} \widehat{\mu}(\theta) \nabla \theta \cdot \nabla \alpha=\bar{\alpha} \quad \text { with } \quad \partial_{\theta} \widehat{\mu}(\theta)=-C_{\mathrm{s}} \widehat{\mu}(\theta)
\tag{25}
$$

as outlined in the work of Forest [2].

Micromorphic approach for gradient-thermo-plasticity

![](./images/813137276241444865_3.jpg)

Fig. 2 Canonical versus micromorphic formulation of gradient plasticity. Standard one-dimensional finite element solutions of gradient plasticity for a canonical setting results in nonphysical oscillations at the elastic-plastic boundary, which are relaxed in b by the micromorphic approach according to Eq. (24)

associated with the macro-motion field $\boldsymbol{\varphi}$, the micromorphic hardening variable $\alpha$ and the absolute temperature field $\theta$. Here, $\boldsymbol{P}$ is denoted as the energetic first Piola nominal stress defined as

$$
\boldsymbol{P}:=\partial_{\boldsymbol{F}} \widehat{\Psi}=\partial_{\boldsymbol{\varepsilon}} \widehat{\Psi}: \mathbb{P}_{\log } \quad \text { with } \quad \mathbb{P}_{\log }:=\partial_{\boldsymbol{F}} \boldsymbol{\varepsilon} \tag{29}
$$

in terms of the fourth-order nominal transformation tensor $\mathbb{P}_{\log }$ outlined in the work of Miehe and Lambrecht [43]. To solve for the above system of Eq. (26), we applied staggered solution scheme in line with our recent work Aldakheel and Miehe [36].

## 4 Representative numerical examples

The capability of the model is pointed out by investigating the necking of cylindrical bar subjected to tensile loading. The geometric setup and the boundary conditions of the cylindrical bar with radius 6.4135 mm are illustrated in Fig. 3. To trigger localization in the center of the specimen, the yield limit $y_0$ in the center is reduced by 10%. The material parameters used in this example are given in Table 1 for metals. Regarding

![](./images/813137276241444865_4.jpg)

Fig. 3 Necking of cylindrical bar. Geometry and boundary conditions. Due to the symmetry of the boundary value problem only the shaded area is discretized

<table>
<caption>Table 1 Material parameters used for the numerical examples</caption>
<thead>
<tr>
<th>No.</th>
<th>Parameter</th>
<th>Name</th>
<th>Value</th>
<th>Unit</th>
</tr>
</thead>
<tbody>
<tr>
<td>1.</td>
<td>$\kappa$</td>
<td>Bulk modulus</td>
<td>164.2</td>
<td>GPa</td>
</tr>
<tr>
<td>2.</td>
<td>$\mu$</td>
<td>Shear modulus</td>
<td>80.2</td>
<td>GPa</td>
</tr>
<tr>
<td>3.</td>
<td>$h$</td>
<td>Hardening parameter</td>
<td>$\pm 0.13$</td>
<td>GPa</td>
</tr>
<tr>
<td>4.</td>
<td>$\epsilon_{\mathrm{p}}$</td>
<td>Penalty parameter</td>
<td>4.0</td>
<td>GPa</td>
</tr>
<tr>
<td>5.</td>
<td>$y_0$</td>
<td>Yield stress</td>
<td>0.45</td>
<td>GPa</td>
</tr>
<tr>
<td>6.</td>
<td>$\eta_{\mathrm{p}}$</td>
<td>Viscosity</td>
<td>$10^{-7}$</td>
<td>$\mathrm{GPa/s^{-1}}$</td>
</tr>
<tr>
<td>7.</td>
<td>$\alpha_{\mathrm{t}}$</td>
<td>Expansion coefficient</td>
<td>$10^{-5}$</td>
<td>$\mathrm{K^{-1}}$</td>
</tr>
<tr>
<td>8.</td>
<td>$K$</td>
<td>Thermal conductivity</td>
<td>0.045</td>
<td>$\mathrm{KN/sK}$</td>
</tr>
<tr>
<td>9.</td>
<td>$c$</td>
<td>Heat capacity</td>
<td>$3.588\times 10^{-3}$</td>
<td>$\mathrm{GPa/K}$</td>
</tr>
<tr>
<td>10.</td>
<td>$w_{\mathrm{h}}$</td>
<td>Thermal softening</td>
<td>0.002</td>
<td>$\mathrm{K^{-1}}$</td>
</tr>
<tr>
<td>11.</td>
<td>$w_0$</td>
<td>Flow stress softening</td>
<td>0.002</td>
<td>$\mathrm{K^{-1}}$</td>
</tr>
<tr>
<td>12.</td>
<td>$y_\infty$</td>
<td>Infinite yield stress</td>
<td>1.165</td>
<td>GPa</td>
</tr>
<tr>
<td>13.</td>
<td>$\delta$</td>
<td>Saturation parameter</td>
<td>16.96</td>
<td>–</td>
</tr>
</tbody>
</table>

![](./images/813137276241444865_5.jpg)

Fig. 4 Necking of cylindrical bar. Distribution of the micromorphic hardening variable $\alpha$ and the incremental temperature field $\theta$ at the final deformation $\bar{u}=10.0$ mm in combination with several plastic length scales parameter. **a, b** Local analysis ($l_{\mathrm{p}}=0.0$ mm), **c, d** $l_{\mathrm{p}}=0.2$ mm and **e, f** $l_{\mathrm{p}}=0.5$ mm

Micromorphic approach for gradient-thermo-plasticity

![](./images/813137276241444865_6.jpg)

Fig. 5 Necking of cylindrical bar. Temperature-time curves at the center of the specimen for three different plastic length scales $l_{\mathrm{p}}$

![](./images/813137276241444865_7.jpg)

Fig. 6 Necking of cylindrical bar. Load-displacement curves for two different mesh sizes: a for local plasticity $l_{\mathrm{p}}=0 \mathrm{~mm}$ and $\mathbf{b}$ gradient plasticity with $l_{\mathrm{p}}=0.2 \mathrm{~mm}$

to the selection of the material parameters, we refer to the works of Hallquist [44], Simó [45] and Simó and Miehe [41]. Figure 4 depicts the distribution of the micromorphic hardening variable $\alpha$ and the incremental temperature field $\theta$ at the final deformation $\bar{u}=10.0 \mathrm{~mm}$ for several plastic length scales parameter $l_{\mathrm{p}}$. For local plasticity, a sharp necked zone with concentrated micromorphic hardening variable $\alpha$ and temperature field $\theta$ is illustrated in Fig. 4a for $\alpha$ and Fig. $4 \mathrm{~b}$ for $\theta$. By increasing $l_{\mathrm{p}}$ the necking zone smears out and the hardening variable $\alpha$ as well as the temperature field $\theta$ will spread over several elements. Figure 5 demonstrates the influence of the plastic length scale on the temperature evolution over time at the center of the specimen. As documented in Fig. 4, for local plasticity the temperature field $\theta$ has the highest value and by increasing the plastic length scale $l_{\mathrm{p}}$ the maximum value will be decreased. As the length scale parameter $l_{\mathrm{p}} \propto 1 / L$ with $L$ being the macroscopic characteristic size, increasing the plastic length scale is equivalent to a decrease in specimen size and, thus, temperature dissipates faster from a small size medium as illustrated in the work of Faghihi et al. [30], Voyiadjis and Faghihi [29]. The load-displacement curves of the overall structural response are illustrated in Fig. 6. For local theory of plasticity, mesh sensitive results are observed in Fig. 6a. In contrast, Fig. $6 \mathrm{~b}$ shows results for gradient plasticity with $l_{\mathrm{p}}=0.2 \mathrm{~mm}$ and two different mesh sizes, where mesh objectivity is obtained. Thus, the incorporation of the length scale parameter $l_{\mathrm{p}}$ enables us not only to predict a size-independent structural response, but also to control the shape of the necking zone.

## 5 Conclusion

We outlined a model for coupled gradient thermo-plasticity under finite deformations in the logarithmic strain space. This covers a computationally efficient micromorphic regularization of recently proposed strain gradient plasticity formulations for the analysis of the thermo-mechanical coupling. In the mechanical part, the model problem of von Mises plasticity with gradient-extended hardening/softening response was considered. In the

thermal part, we followed the investigations of Simó and Miehe [41] and Aldakheel [35] that demonstrate the effect of temperature on the mechanical fields resulting in a thermal expansion. The important aspect of the work was the regularization toward a micromorphic gradient thermo-plasticity setting by taking into account additional internal variable field linked to the original one by penalty term. This substantially enhances the robustness of the finite element implementation. The performance of the formulation was demonstrated by means of a representative numerical example.

Acknowledgements Fadi Aldakheel would like to gratefully acknowledge the financial support of this work through the interna- tional master program "Computational Mechanics of Materials and Structures" (COMMAS) position at the University of Stuttgart while being the course director at the same time.

## References

1. Miehe, C., Welschinger, F., Aldakheel, F.: Variational gradient plasticity at finite strains. Part II: local-global updates and mixed finite elements for additive plasticity in the logarithmic strain space. Comput. Methods Appl. Mech. Eng. **268**, 704-734 (2014)
2. Forest, S.: Micromorphic approach for gradient elasticity, viscoplasticity, and damage. J. Eng. Mech. **135**, 117-131 (2009)
3. Miehe, C., Teichtmeister, S., Aldakheel, F.: Phase-field modeling of ductile fracture: a variational gradient-extended plasticity- damage theory and its micromorphic regularization. Philos. Trans. R. Soc. A Math. Phys. Eng. Sci. **374**, 20150170 (2016). doi:10.1098/rsta.2015.0170
4. Fleck, N.A., Muller, G.M., Ashby, M.F., Hutchinson, J.W.: Strain gradient plasticity: theory and experiment. Acta Mater. **42**,475-487 (1994)
5. de Borst, R., Mühlhaus, H.B.: Gradient-dependent plasticity: formulation and algorithmic aspects. Int. J. Numer. MethodsEng. **35**, 521-539 (1992)
6. Liebe, T., Steinmann, P.: Theory and numerics of a thermodynamically consistent framework for geometrically linear gradientplasticity. Int. J. Numer. Methods Eng. **51**, 1437-1467 (2001)
7. Engelen, R.A.B., Geers, M.G.D., Baaijens, F.P.T.: Nonlocal implicit gradient-enhanced elasto-plasticity for the modellingof softening behavior. Int. J. Plast. **19**, 403-433 (2003)
8. Gurtin, E.: A finite-deformation, gradient theory of single-crystal plasticity with free energy dependent on densities ofgeometrically necessary dislocations. Int. J. Plast. **24**, 702-725 (2008)
9. Svendsen, B., Bargmann, S.: On the continuum thermodynamic rate variational formulation of models for extended crystalplasticity at large deformation. J. Mech. Phys. Solids **58**, 1253-1271 (2010)
10. Wulfinghoff, S., Bohlke, T.: Equivalent plastic strain gradient enhancement of single crystal plasticity: theory and numerics.In: Proceedings of the Royal Society of London A: Mathematical, Physical and Engineering Sciences (2012)
11. Klusemann, B., Yalcinkaya, T.: Plastic deformation induced microstructure evolution through gradient enhanced crystalplasticity based on a non-convex helmholtz energy. Int. J. Plast. **48**, 168-188 (2013)
12. Miehe, C., Mauthe, S., Hildebrand, F.E.: Variational gradient plasticity at finite strains. Part III: local-global updates andregularization techniques in multiplicative plasticity for single crystals. Comput. Methods Appl. Mech. Eng. **268**, 735-762(2014)
13. Forest, S., Sievert, R.: Elastoviscoplastic constitutive frameworks for generalized continua. Acta Mech. **160**, 71-111 (2003)
14. Gudmundson, P.: A unified treatment of strain gradient plasticity. J. Mech. Phys. Solids **52**, 1379-1406 (2004)
15. Anand, L., Aslan, O., Chester, S.A.: A large-deformation gradient theory for elastic-plastic materials: strain softening andregularization of shear bands. Int. J. Plast. **30-31**, 116-143 (2012)
16. Reddy, B., Ebobisse, F., McBride, A.: Well-posedness of a model of strain gradient plasticity for plastically irrotationalmaterials. Int. J. Plast. **24**, 55-73 (2008)
17. Fleck, N.A., Willis, J.R.: A mathematical basis for strain-gradient plasticity theory. Part I: scalar plastic multiplier. J. Mech.Phys. Solids **57**, 161-177 (2009a)
18. Fleck, N.A., Willis, J.R.: A mathematical basis for strain-gradient plasticity theory. Part II: tensorial plastic multiplier. J.Mech. Phys. Solids **57**, 1045-1057 (2009b)
19. Polizzotto, C.: A nonlocal strain gradient plasticity theory for finite deformations. Int. J. Plast. **25**, 1280-1300 (2009)
20. Forest, S.: Nonlinear regularization operators as derived from the micromorphic approach to gradient elasticity, viscoplasticityand damage. In: Proceedings of the Royal Society of London A: Mathematical, Physical and Engineering Sciences, vol. 472(2016)
21. Voyiadjis, G.Z., Pekmezi, G., Deliktas, B.: Nonlocal gradient-dependent modeling of plasticity with anisotropic hardening.Int. J. Plast. **26**, 1335-1356 (2010)
22. Kuroda, M., Tvergaard, V.: An alternative treatment of phenomenological higher-order strain-gradient plasticity theory. Int.J. Plast. **26**, 507-515 (2010)
23. Miehe, C., Aldakheel, F., Mauthe, S.: Mixed variational principles and robust finite element implementations of gradientplasticity at small strains. Int. J. Numer. Methods Eng. **94**, 1037-1074 (2013)
24. Wriggers, P., Miehe, C., Kleiber, M., Simo, J.: On the coupled thermomechanical treatment of necking problems via finiteelement methods. Int. J. Numer. Methods Eng. **33**, 869-883 (1992)
25. Anand, L., Ames, N.M., Srivastava, V., Chester, S.A.: A thermo-mechanically coupled theory for large deformations ofamorphous polymers. Part I: formulation. Int. J. Plast. **25**, 1474-1494 (2009)
26. Canadija, M., Mosler, J.: On the thermomechanical coupling in finite strain plasticity theory with non-linear kinematichardening by means of incremental energy minimization. Int. J. Solids Struct. **48**, 1120-1129 (2011)

Micromorphic approach for gradient-thermo-plasticity

27. Yang, Q., Stainier, L., Ortiz, M.: A variational formulation of the coupled thermo-mechanical boundary-value problem for general dissipative solids. J. Mech. Phys. Solids **54**, 401-424 (2006)

28. Stainier, L., Ortiz, M.: Study and validation of thermomechanical coupling in finite strain visco-plasticity. Int. J. Solids Struct. **47**, 704-715 (2010)

29. Voyiadjis, Z., Faghihi, D.: Thermo-mechanical strain gradient plasticity with energetic and dissipative length scales. Int. J. Plast. **30-31**, 218-247 (2012)

30. Faghihi, D., Voyiadjis, Z., Park, T.: Coupled thermomechanical modeling of small volume fcc metals. J. Eng. Mater. Technol. **135**, 1-17 (2013)

31. Forest, S., Aifantis, E.: Some links between recent gradient thermo-elasto-plasticity theories and the thermomechanics of generalized continua. Int. J. Solids Struct. **47**, 3367-3376 (2010)

32. Bertram, A., Forest, S.: The thermodynamics of gradient elastoplasticity. Contin. Mech. Thermodyn. **26**, 269-286 (2014)

33. Wcislo, B., Pamin, J.: Local and non-local thermomechanical modeling of elastic-plastic materials undergoing large strains. Int. J. Numer. Methods Eng. **109**, 102-124 (2016)

34. Miehe, C., Aldakheel, F., Teichtmeister, S.: Phase-field modeling of ductile fracture at finite strains. A robust variational-based numerical implementation of a gradient-extended theory by micromorphic regularization. Int. J. Numer. Methods Eng. (2016). doi:10.1002/nme.5484

35. Aldakheel, F.: Mechanics of nonlocal dissipative solids: gradient plasticity and phase field modeling of ductile fracture. Ph.D. thesis, Institute of Applied Mechanics (CE), Chair I, University of Stuttgart (2016). doi:10.18419/opus-8803

36. Aldakheel, F., Miehe, C.: Coupled thermomechanical response of gradient plasticity. Int. J. Plast. **91**, 1-24 (2017)

37. Miehe, C., Apel, N., Lambrecht, M.: Anisotropic additive plasticity in the logarithmic strain space. Modularkinematic formulation and implementation based on incremental minimization principles for standard materials. Comput. Methods Appl. Mech. Eng. **191**, 5383-5425 (2002)

38. Geers, M.G.D., Peerlings, R.H.J., Brekelmans, W.A.M., de Borst, R.: Phenomenological nonlocal approaches based on implicit gradient-enhanced damage. Acta Mech. **144**, 1-15 (2000)

39. Peerlings, R.H.J., Geers, M.G.D., de Borst, R., Brekelmans, W.A.M.: A critical comparison of nonlocal and gradient-enhanced softening continua. Int. J. Solids Struct. **38**, 7723-7746 (2001)

40. Peerlings, R.H.J., Massart, T.J., Geers, M.G.D.: A thermodynamically motivated implicit gradient damage framework and its application to brick masonry cracking. Comput. Methods Appl. Mech. Eng. **193**, 3403-3417 (2004)

41. Simó, J., Miehe, C.: Associative coupled thermoplasticity at finite strains: formulation, numerical analysis and implementation. Comput. Methods Appl. Mech. Eng. **98**, 41-104 (1992)

42. Boyce, M.C., Montagut, E.L., Argon, A.S.: The effects of thermomechanical coupling on the cold drawing process of glassy polymers. Polym. Eng. Sci. **32**, 1073-1085 (1992)

43. Miehe, C., Lambrecht, M.: Algorithms for computation of stresses and elasticity moduli in terms of Seth-Hill's family of generalized strain tensors. Commun. Numer. Methods Eng. **17**, 337-353 (2001)

44. Hallquist, J.O.: Nike 2D: An implicit, finite deformation, finite element code for analyzing the static and dynamic response of two-dimensional solids. Rept. UCRL-52678, Lawrence Livermore National Laboratory, University of California, Livermore, CA (1984)

45. Simó, J.C.: A framework for finite strain elastoplasticity based on maximum plastic dissipation and the multiplicative decomposition. Part II: computational aspects. Comput. Methods Appl. Mech. Eng. **68**, 1-31 (1988)