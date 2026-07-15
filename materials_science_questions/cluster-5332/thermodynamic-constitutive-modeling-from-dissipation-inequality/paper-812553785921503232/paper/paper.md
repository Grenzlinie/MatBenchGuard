# Primal interface debonding formulation for finite strain isotropic plasticity

Sunday C. Aduloju$^{a,b}$, Timothy J. Truster$^{a,1,*}$

$^{a}$ Department of Civil and Environmental Engineering, University of Tennessee, Knoxville, 318 John D. Tickle Engineering Building, Knoxville, TN 37996, United States
$^{b}$ Fusion Energy Division, Oak Ridge National Laboratory, Oak Ridge, TN 37831, USA

---

## ARTICLE INFO

**Article history:**
Received 12 February 2020
Revised 30 August 2020
Accepted 7 September 2020
Available online xxx

**Keywords:**
Finite strains
Variational multiscale method
Discontinuous Galerkin
Computational inelasticity
Debonding

---

## ABSTRACT

A framework is developed for modeling ductile damage of nonlinear materials whose plastic deformation is characterized using rate independent classical plasticity. This method relies on the assumption that the free energy can be decomposed into elastic, plastic and damage parts. A thermodynamically consistent method is derived which satisfies the second law of thermodynamics in the Clausius-Duhem inequality form. The dissipation associated with plasticity takes place in the domain only, while damage dissipation is localized to the interface. The method is developed using Variational Multiscale ideas to obtain definitions of the interface fluxes within a primal formulation analogous to the Discontinuous Galerkin method, which ensures weakly vanishing interface gap prior to reaching a damage initiation criterion. The local nonlinear problem to calculate both plastic deformation gradient and damage variable follows an incremental approach similar to classical plasticity return mapping algorithm. This elastoplastic damage formulation is developed for material undergoing finite strain, and it naturally accommodates a trapezoidal traction separation law (TSL) whose shape can be varied to model either ductile interface behavior or brittle interface behavior. The formulation's performance is assessed through modeling a patch test and a compact tension specimen.

© 2020 Elsevier Ltd. All rights reserved.

---

## 1. Introduction

The results from tensile experiments show that typical metals lose their load carrying capacity and undergo ductile fracture during tensile loading. Experimental techniques to quantify damage parameters for materials undergoing elasto-plastic damage behavior are not trivial. With computational tools playing an ever-increasing role in the study of mechanics of materials, computational models are now being developed and employed to capture and quantify elastoplastic damage processes in engineering materials. At present, there is no general agreement among researchers as to whether damage should be modeled as localized or diffused cracks in a ductile material.

The global approach to fracture consists of methodologies which assume that fracture can be described by a single parameter [1,2]. One example is the path independent contour J-integral method which was first presented by Rice [3,4] for analysis of cracks in nonlinear materials where an elastic-plastic deformation is idealized as nonlinear elastic. The J contour integral method enjoyed early acceptance for use as a fracture criterion for crack tip conditions in elasto-plastic materials [5], but the method is known to break down when there is a combination of significant plasticity and crack growth. Also, this method could only be applied to model preexisting cracks. These limitations have also been found in approaches employing crack tip opening displacement (CTOD) as a fracture criterion. Another methodology is the continuum damage mechanics method which is a phenomenological approach to fracture and relies on the continuous description of damage where a scalar or tensorial damage variable is related to the material characteristic properties. These methods are based on the early developments of Kachanov and Lemaitre [6]. Later, this method was posed in [7] as a consistent thermodynamic framework that guarantees that dissipation is always positive.

A group of methods categorized under the methodology of local approach to fracture were developed to provide a detailed and physically based description of damage phenomena in the rupture process zone. The Gurson or Gurson-Tvergaard-Needleman (GTN) model and the cohesive zone method fall into this category [1]. The Gurson model describes ductile damage using

---

* Corresponding author.
E-mail address: truster@utk.edu (T.J. Truster).
$^{1}$ Associate Professor

https://doi.org/10.1016/j.mechrescom.2020.103606
0093-6413/© 2020 Elsevier Ltd. All rights reserved.

Please cite this article as: S.C. Aduloju and T.J. Truster, Primal interface debonding formulation for finite strain isotropic plasticity, Mechanics Research Communications, https://doi.org/10.1016/j.mechrescom.2020.103606

crack nucleation, growth and coalescence as the three consecutive processes that occur during material damage. The inaccuracies in the representation of fracture and void growth predicted by the earlier Gurson model led to the improvement of the yield surface expression for Gurson model to arrive the GTN model that is free from these limitations [8]. See [1,2] for reviews of current extensions of the method. Though the Gurson model was derived from rigorous micromechanical analyses, a thermodynamic framework which guarantees that the dissipation is always positive is only possible when the void nucleation is absent [9].

The cohesive zone model (CZM) accounts for the processes occurring within the fracture process zone through the traction separation law (TSL), and attempts have been made to classify the damage mechanisms in the fracture process zone based on forward and wake regions of the TSL [10,11]. Several TSL shapes exist in the literature, and it has been recently argued that the TSL shapes affect the prediction of ductile fracture behavior [11-13]. The intrinsic CZM type is known to have stability issues due to artificial compliance of the interface [14,15]. This artificial compliance is associated with the large elastic penalty coefficient assigned to the traction-separation curve to approximate a perfect interface bond below the crack initiation threshold traction. Setting large values to the coefficient leads to large eigenvalues in the global stiffness [16]. The artificial compliance could be eradicated by using extrinsic CZM. Unfortunately, the extrinsic CZ approach requires data structures that permit mesh adaptivity to insert these elements [16].

The Discontinuous Galerkin (DG) formulation overcomes both problems associated to CZM by weakly enforcing displacement field continuity and representing TSL using a relation instead of a function [17]. The Discontinuous Galerkin method has been used to enforce continuity in nonlinear materials with large deformations [18,19], plasticity [20-22], microscale modeling [23], and damage [17,24,25]. To the best knowledge of the authors, this paper presents for the first time the development of a Discontinuous Galerkin method for modeling ductile damage. It employs the use of extrinsic trapezoidal TSL which has not been used previously within such formulations to account for processes occurring in the fracture process zone.

In the next section, we discuss the variational characterization of elasto-plastic-damage response and evaluation of the stability tensor. We derive the weak form from the free energy and dissipation functionals in Section 3. In Section 4, constitutive update equations are developed for both bulk plasticity and interface damage that appear within the DG numerical flux terms, and the mathematical differences between the recently developed return mapping algorithm of the extrinsic trapezoidal TSL and a triangular TSL are presented. The linearization of the weak form is also presented. The performance of the method is evaluated using a patch test and a ductile damage simulation on a coarse finite element mesh of a compact (CT) specimen in Section 5. Finally, conclusions are drawn in Section 6.

### 2. Variational characterization of elasto-plastic damage response

We begin our developments by treating the case of an evolving interface gap at the interface $\Gamma_{I}$ embedded within a body $\Omega \subset \mathbb{R}^{n_{s d}}$ undergoing an elasto-plastic finite deformation. The domain $\Omega$ is divided into two regions $\Omega^{(\alpha)}$ by the interface $\Gamma_{I}$ as shown in Fig. 1 where $\alpha$=1,2. The two regions deform according to the motion $\boldsymbol{\varphi}^{(\alpha)}(\mathbf{X}, t)$ that maps the reference configuration to the current configuration $\mathbf{x}=\boldsymbol{\varphi}^{(\alpha)}(\mathbf{X}, t)$.

![](./images/812553785921503232_1.jpg)

Fig. 1. The multiplicative decomposition of deformation gradient $\mathbf{F}$ in domain $\Omega$ divided into two regions $\Omega^{(\alpha)}$ by the interface $\Gamma_{I}$.

We allow the deformations $\boldsymbol{\varphi}^{(\alpha)}$ to be distinct along the interface $\Gamma_{I}$ to accommodate the existence of the interface gap or debonding $\zeta$. Let $\mathbf{F}(\mathbf{X}, t)=\nabla_{\mathbf{X}} \mathbf{x}=\partial \mathbf{x} / \partial \mathbf{X}$ be the deformation gradient that has a multiplicative decomposition into an elastic part $\mathbf{F}^{\mathrm{e}}$
and plastic part $\mathbf{F}^{\mathrm{p}}$ as follows:
$$
\mathbf{F}=\mathbf{F}^{\mathrm{e}} \mathbf{F}^{\mathrm{p}}, \quad \operatorname{det} \mathbf{F}^{\mathrm{e}}>0, \quad \operatorname{det} \mathbf{F}^{\mathrm{p}}>0
\tag{1}
$$

The Helmholtz free energy $\psi$ of the domain can be decomposed according to [22,25,26] into a bulk contribution $\psi_{\Omega}$ and an interface contribution $\psi_{\Gamma}$ as follows:
$$
\psi_{\Omega}\left(\mathbf{F}, \mathbf{F}^{\mathrm{p}}, \boldsymbol{\alpha}^{\mathrm{p}}\right)=\psi^{\mathrm{e}}\left(\mathbf{F}, \mathbf{F}^{\mathrm{p}}\right)+\psi^{\mathrm{p}}\left(\boldsymbol{\alpha}^{\mathrm{p}}\right)
\tag{2}
$$

$$
\psi_{\Gamma}\left(\boldsymbol{\alpha}^{\mathrm{d}}\right)=\psi^{\mathrm{d}}\left(\boldsymbol{\alpha}^{\mathrm{d}}\right)
\tag{3}
$$

where the bulk contribution is additively split into an elastic $\psi^{\mathrm{e}}(\mathbf{F},\mathbf{F}^{\mathrm{p}})$ and plastic $\psi^{\mathrm{p}}(\boldsymbol{\alpha}^{\mathrm{p}})$ part, as is typically assumed for elastoplastic damage theories [27,28]. Within these expressions, $\boldsymbol{\alpha}^{\mathrm{p}}$ is the strain-like plastic hardening variable in the domain while $\boldsymbol{\alpha}^{\mathrm{d}}$ is the damage hardening/softening parameter at the interface within the damage free energy $\psi^{\mathrm{d}}(\boldsymbol{\alpha}^{\mathrm{d}})$.

The framework of rational thermodynamics is adopted as in [29,30] where for an isothermal condition, the Clausius-Duhem dissipation inequality at the domains can be written in terms of the first Piola-Kirchoff stress tensor [31,32] or the Mandrel stress [33,34]. Here-in, we follow the latter approach in accordance with the additive split (2) whereby the plastic dissipation is expressed as:
$$
\mathcal{D}^{\mathrm{p}}:=\boldsymbol{\Sigma}: \mathbf{L}^{\mathrm{p}}-\mathbf{Q}^{\mathrm{p}} \cdot \dot{\boldsymbol{\alpha}}^{\mathrm{p}} \geq 0 \quad \text { in } \Omega^{(\alpha)}, \quad \alpha=1,2
\tag{4}
$$
where $\boldsymbol{\Sigma}=2 \mathbf{C}^{\mathrm{e}} \partial_{\mathbf{C}^{\mathrm{e}}} \psi^{\mathrm{e}}(\mathbf{F}, \mathbf{F}^{\mathrm{p}})$ is the Mandel stress with $\mathbf{C}^{\mathrm{e}}=\mathbf{F}^{\mathrm{eT}} \mathbf{F}^{\mathrm{e}}$, $\mathbf{L}^{\mathrm{p}}=\dot{\mathbf{F}}^{\mathrm{p}} \mathbf{F}^{\mathrm{p}-1}$ is the plastic part of the velocity gradient tensor, and $\mathbf{Q}^{\mathrm{p}}=-\partial_{\boldsymbol{\alpha}^{\mathrm{p}}} \psi^{\mathrm{p}}(\boldsymbol{\alpha}^{\mathrm{p}})$ is the stress-like work conjugate flux of $\boldsymbol{\alpha}^{\mathrm{p}}$.

We limit the discussion of this method to dissipative processes governed by associative flow rule where the domain's plastic and the interface's damage flows are determined from the respective yield function. The deformation gradient and plastic hardening are constrained to lie in the closure of elastic domain, and the yield function $f^{\mathrm{p}}(\boldsymbol{\Sigma},\mathbf{Q}^{\mathrm{p}})$ is associated to the stress-space yield surface $\mathbb{E}^{\mathrm{p}}:=\{(\boldsymbol{\Sigma},\mathbf{Q}^{\mathrm{p}})|f^{\mathrm{p}}(\boldsymbol{\Sigma},\mathbf{Q}^{\mathrm{p}}) \leq 0\}$. Similar to [25], the dissipation inequality at the interface is expressed as (5) with yield condition $f^{\mathrm{d}}(\mathbf{T},\mathbf{Q}^{\mathrm{d}})$ that is associated with the yield surface $\mathbb{E}^{\mathrm{d}}:=\{(\mathbf{T},\mathbf{Q}^{\mathrm{d}})|f^{\mathrm{d}}(\mathbf{T},\mathbf{Q}^{\mathrm{d}}) \leq 0\}$.
$$
\mathcal{D}^{\mathrm{d}}:=\mathbf{T} \cdot \dot{\boldsymbol{\zeta}}-\mathbf{Q}^{\mathrm{d}} \cdot \dot{\boldsymbol{\alpha}}^{\mathrm{d}} \geq 0 \quad \text { on } \Gamma_{\mathrm{I}}
\tag{5}
$$

The $\mathcal{D}^{\mathrm{p}}$ and $\mathcal{D}^{\mathrm{d}}$ are the Lagrangian functionals associated with plastic and damage dissipation. In (5), $\mathbf{Q}^{\mathrm{d}}=-\partial_{\boldsymbol{\alpha}^{\mathrm{d}}} \psi^{\mathrm{d}}(\boldsymbol{\alpha}^{\mathrm{d}})$ is the stress-like work conjugate flux of $\boldsymbol{\alpha}^{\mathrm{d}}$ and the interface flux $\mathbf{T}$ has the connotation of the interface traction field and is defined similar to [25] in terms of two quantities inspired by variational multiscale developments [35,36] as:
$$
\mathbf{T}=\left\{\mathbf{P}\left(\mathbf{F}, \mathbf{F}^{\mathrm{p}}\right) \mathbf{N}\right\}+\parallel \boldsymbol{\tau}_{s}\parallel ([\boldsymbol{\phi}]]-\boldsymbol{\zeta})
\tag{6}
$$
where $\mathbf{P}=\boldsymbol{\tau} \mathbf{F}^{-\mathrm{T}}=\mathbf{F}^{\mathrm{e}-\mathrm{T}} \boldsymbol{\Sigma} \mathbf{F}^{\mathrm{p}-\mathrm{T}}$ is the first Piola-Kirchhoff stress tensor defined in terms of the Kirchhoff stress $\boldsymbol{\tau}$ or the Mandel stress $\boldsymbol{\Sigma}$,

$\|\cdot\|=(\cdot)^{(2)}-(\cdot)^{(1)}$ is the jump operator defined for vector-valued fields on interface $\Gamma_{I}$, and $\{(\cdot) \cdot \mathbf{N}\}=\boldsymbol{\delta}_{s}^{(1)}(\cdot) \cdot \mathbf{N}^{(1)}+\boldsymbol{\delta}_{s}^{(2)}(\cdot) \cdot \mathbf{N}^{(2)}$ is the weighted average flux operator. Furthermore, $\boldsymbol{\delta}_{s}^{(\alpha)}=\boldsymbol{\tau}_{s} \cdot \boldsymbol{\tau}_{s}^{(\alpha)}$ is the flux weight and $\mathbf{N}^{(\alpha)}$ is the outward unit normal vector in the reference configuration to domain $\Omega^{(\alpha)}$, and $\boldsymbol{\tau}_{s}=\left(\boldsymbol{\tau}_{s}^{(1)}+\boldsymbol{\tau}_{s}^{(2)}\right)^{-1}$ is the stability or penalty tensor. The reader is referred to the Appendix for the details about the stability tensor $\boldsymbol{\tau}_{s}^{(\alpha)}$ and its definition. The stability tensor is obtained by transforming a mixed Lagrange interface formulation into a primal formulation where the Lagrange multiplier field is condensed using Variational Multiscale (VMS) ideas. The VMS approach facilitates the derivation of stabilized formulations via numerically modeled fine-scale fields [25]. Employing rational localized modeling assumptions to the fine scales results in analytical expressions for both the fine scale and the Lagrange multiplier fields. These analytical expressions are substituted back in the coarse-scale formulation to obtain a primal interface debonding formulation with enhanced stability.

### 3. Derivation of weak form and euler-lagrange equations

The weak form of combined bulk elastoplasticity and interface damage is developed from time discretization of the evolving total free energy and dissipation functionals. Ortiz and Stainier [32] have shown that the classical incremental forms from [31,37] can be recast within broader variational formulations. Hence, the bulk elasto-plastic contribution will be summarized here and specialized within Section 4.1. Emphasis is placed on the interface contribution and the effect of the elastoplastic model on the numerical flux.

The total free energy $\mathcal{P}_{t}$ at time $t$ is expressed through a Hu-Washizu principle in $\Omega$ [31] and Discontinuous Galerkin treatment along $\Gamma_{I}$ [25]:
$$
\begin{aligned}
\mathcal{P}_{t} & \left(\boldsymbol{\phi}_{t}, \mathbf{F}_{t}, \mathbf{F}_{t}^{\mathrm{p}}, \boldsymbol{\alpha}_{t}^{\mathrm{p}}, \boldsymbol{\zeta}_{t}, \boldsymbol{\alpha}_{t}^{\mathrm{d}}\right)=\sum_{\alpha=1}^{2} \mathcal{P}_{\mathrm{ext}}\left(\boldsymbol{\phi}_{t}^{(\alpha)}\right) \\
& +\sum_{\alpha=1}^{2}\left[\int_{\Omega^{(\alpha)}} \psi_{\Omega}\left(\mathbf{F}_{t}^{(\alpha)}, \mathbf{F}_{t}^{\mathrm{p}(\alpha)}, \boldsymbol{\alpha}_{t}^{\mathrm{p}}\right) d V\right] \\
& +\sum_{\alpha=1}^{2}\left[\int_{\Omega^{(\alpha)}} \mathbf{P}_{t}^{(\alpha)}:\left(\nabla_{\chi} \boldsymbol{\phi}_{t}^{(\alpha)}-\mathbf{F}_{t}^{(\alpha)}\right) d V\right] \\
& -\int_{\Gamma_{I}}\left(\left[\left[\boldsymbol{\phi}_{t}\right]\right]-\boldsymbol{\zeta}_{t}\right) \cdot \mathbf{T}_{t} d A \\
& -\int_{\Gamma_{I}} \frac{1}{2}\left\|\boldsymbol{\tau}_{s}\right\|\left(\left[\left[\boldsymbol{\phi}_{t}\right]\right]-\boldsymbol{\zeta}_{t}\right) \cdot\left(\left[\left[\boldsymbol{\phi}_{t}\right]\right]-\boldsymbol{\zeta}_{t}\right) d A \\
& +\int_{\Gamma_{I}} \psi^{\mathrm{d}}\left(\boldsymbol{\alpha}_{t}^{\mathrm{d}}\right) d A
\end{aligned}
$$
where $\mathcal{P}_{\text {ext }}$ is the external energy function. The total dissipation up to the time $t$ can be obtained by evaluating the integral of the combination of the dissipation functionals and yield functions associated with plastic and damage processes:
$$
\mathcal{L}_{t}^{\mathrm{p}}=\int_{0}^{t} \int_{\Omega}\left[\mathcal{D}_{\xi}^{\mathrm{p}}-\gamma_{\xi}^{\mathrm{p}} f^{\mathrm{p}}\left(\boldsymbol{\Sigma}_{\xi}, \mathbf{Q}_{\xi}^{\mathrm{p}}\right)\right] d V d \xi
$$

$$
\mathcal{L}_{t}^{\mathrm{d}}=\int_{0}^{t} \int_{\Gamma_{I}}\left[\mathcal{D}_{\xi}^{\mathrm{d}}-\gamma_{\xi}^{\mathrm{d}} f^{\mathrm{d}}\left(\mathbf{T}_{\xi}, \mathbf{Q}_{\xi}^{\mathrm{d}}\right)\right] d A d \xi
$$
where $\gamma^{(\bullet)}$ and $f^{\bullet}$ are the consistency parameter and yield function for plasticity and damage, respectively. The history of the state variables over the time interval $\left[0, t_{n}\right]$ is assumed to be known. The unknown state variables $\chi_{n+1}$ at time $t_{n+1}=t_{n}+\Delta t$ are targeted, and compact notation is adopted for them along with the yield functions and elastic energy:
$$
\boldsymbol{\chi}_{n+1}:=\left[\boldsymbol{\phi}_{n+1}^{(\alpha)}, \boldsymbol{\chi}_{n+1}^{\mathrm{p}}, \boldsymbol{\chi}_{n+1}^{\mathrm{d}}\right]
$$

$$
\boldsymbol{\chi}_{n+1}^{\mathrm{p}}:=\left[\mathbf{F}_{n+1}^{(\alpha)}, \mathbf{F}_{n+1}^{\mathrm{p}(\alpha)}, \boldsymbol{\alpha}_{n+1}^{\mathrm{p}}, \Delta \gamma^{\mathrm{p}}\right]
$$

$$
\boldsymbol{\chi}_{n+1}^{\mathrm{d}}:=\left[\boldsymbol{\zeta}_{n+1}, \boldsymbol{\alpha}_{n+1}^{\mathrm{d}}, \Delta \gamma^{\mathrm{d}}\right]
$$

$$
f_{n+1}^{\mathrm{p}}:=f^{\mathrm{p}}\left[\boldsymbol{\Sigma}_{n+1}, \mathbf{Q}_{n+1}^{\mathrm{p}}\right]
$$

$$
f_{n+1}^{\mathrm{d}}:=f^{\mathrm{d}}\left[\mathbf{T}_{n+1}, \mathbf{Q}_{n+1}^{\mathrm{d}}\right]
$$

$$
\psi^{\mathrm{e}(\alpha)}{ }_{n+1}:=\psi^{\mathrm{e}(\alpha)}\left(\mathbf{F}_{n+1}^{(\alpha)}, \mathbf{F}_{n+1}^{\mathrm{p}(\alpha)}\right)
$$

Backward Euler time discretization is applied to each of the terms in the dissipation functionals, exempting the plastic flow rule which is evaluated by the backward exponential integrator in anticipation of volume-preserving plastic flow. Treatment of bulk plasticity is referred to [34] while the interface damage emergessimilarly as in [25]:
$$
\begin{gathered}
\mathcal{L}_{n+1}^{\mathrm{p}}\left(\boldsymbol{\phi}_{n+1}^{(\alpha)}, \boldsymbol{\chi}_{n+1}^{\mathrm{p}}\right):=\mathcal{L}_{n}^{\mathrm{p}} \\
+\int_{\Omega} \boldsymbol{\Sigma}_{n+1} \cdot\left(\mathbf{I}_{n+1}^{\mathrm{p}}-\mathbf{I}_{n}^{\mathrm{p}}\right) \Delta t-\Delta \gamma^{\mathrm{p}} f_{n+1}^{\mathrm{p}} \\
-\mathbf{Q}_{n+1}^{\mathrm{p}} \cdot\left(\boldsymbol{\alpha}_{n+1}^{\mathrm{p}}-\boldsymbol{\alpha}_{n}^{\mathrm{p}}\right) d V
\end{gathered}
$$

$$
\begin{gathered}
\mathcal{L}_{n+1}^{\mathrm{d}}\left(\boldsymbol{\phi}_{n+1}^{(\alpha)}, \boldsymbol{\chi}_{n+1}^{\mathrm{d}}\right):=\mathcal{L}_{n}^{\mathrm{d}} \\
+\int_{\Gamma_{I}} \mathbf{T}_{n+1} \cdot\left(\boldsymbol{\zeta}_{n+1}-\boldsymbol{\zeta}_{n}\right)-\Delta \gamma^{\mathrm{d}} f_{n+1}^{\mathrm{d}} \\
-\mathbf{Q}_{n+1}^{\mathrm{d}} \cdot\left(\boldsymbol{\alpha}_{n+1}^{\mathrm{d}}-\boldsymbol{\alpha}_{n+1}^{\mathrm{d}}\right) d A
\end{gathered}
$$
where $\Delta \gamma^{\mathrm{p}, \mathrm{d}}:=\gamma^{\mathrm{p}, \mathrm{d}} \Delta t$ are incremental consistency parameters. A discrete functional for free energy $\hat{\mathcal{P}}_{n}\left(\boldsymbol{\chi}_{n+1}\right)$ at time $t_{n}$ is obtained similarly as the sum of the free energy $\mathcal{P}_{n+1}\left(\boldsymbol{\chi}_{n+1}\right)$ at $t_{n+1}$ and the incremental dissipation during time $\left[t_{n}, t_{n+1}\right]$ :
$$
\begin{aligned}
& \hat{\mathcal{P}}_{n}\left(\boldsymbol{\chi}_{n+1}\right):=\mathcal{P}_{n+1}\left(\boldsymbol{\chi}_{n+1}\right)+\mathcal{L}_{n+1}^{p}\left(\boldsymbol{\phi}_{n+1}^{(\alpha)}, \boldsymbol{\chi}_{n+1}^{\mathrm{p}}\right) \\
& -\mathcal{L}_{n}^{p}+\mathcal{L}_{n+1}^{\mathrm{d}}\left(\boldsymbol{\phi}_{n+1}^{(\alpha)}, \chi_{n+1}^{\mathrm{d}}\right)-\mathcal{L}_{n}^{\mathrm{d}}
\end{aligned}
$$

The stationary conditions of $\hat{\mathcal{P}}_{n}\left(\boldsymbol{\chi}_{n+1}\right)$ are obtained by the variational derivative of (18) with respect to each of its arguments, leading to weak (integral) statements of each governing equation for the domain and interface fields. These results are recorded for plasticity alone in [31,37] and for hyperelasticity and interface damage in [25]. For conciseness and consistency with our previous developments, the bulk stress terms are defined in terms of the first Piola-Kirchhoff stress. A crucial outcome of the Hu-Washizu treatment of the bulk term is that the evaluation of the first Piola-Kirchhoff stress $\mathbf{P}_{n+1}^{(\alpha)}$ is decoupled from the update of the interface debonding $\boldsymbol{\zeta}_{n+1}$. Hence, typical return mapping algorithms for plasticity can be utilized at collocation (numerical quadrature) points within the bulk and the interface. The pertinent Euler-Lagrange equations are obtained from applying integration by parts to the bulk equilibrium equation and localizing the integrals on $\Gamma_{I}$ to discrete quadrature points along the interface segments $\gamma_{s}$ :
$$
\nabla_{\chi} \cdot \mathbf{P}_{n+1}^{(\alpha)}+\rho_{0}^{(\alpha)} \mathbf{B}^{(\alpha)}=\mathbf{0} \quad \text { in } \Omega^{(\alpha)}
$$

$$
\mathbf{P}_{n+1}^{(1)} \cdot \mathbf{N}^{(1)}+\mathbf{P}_{n+1}^{(2)} \cdot \mathbf{N}^{(2)}=\mathbf{0} \quad \text { on } \Gamma_{I}
$$

$$
\left[\left[\boldsymbol{\phi}_{n+1}\right]\right]-\boldsymbol{\zeta}_{n+1}=\mathbf{0} \quad \text { on } \Gamma_{I}
$$

$$
\boldsymbol{\zeta}_{n+1}=\boldsymbol{\zeta}_{n}+\Delta \gamma^{\mathrm{d}} \partial_{\mathbf{T}} f_{n+1}^{\mathrm{d}} \quad \text { on } \Gamma_{I}
$$

$$
\boldsymbol{\alpha}_{n+1}^{\mathrm{d}}=\boldsymbol{\alpha}_{n}^{\mathrm{d}}+\Delta \gamma^{\mathrm{d}} \partial_{\mathbf{Q}^{\mathrm{d}}} f_{n+1}^{\mathrm{d}} \quad \text { on } \Gamma_{I}
$$

$$
f_{n+1}^{\mathrm{d}} \leq 0, \quad \Delta \gamma^{\mathrm{d}} \geq 0, \quad f_{n+1}^{\mathrm{d}} \Delta \gamma^{\mathrm{d}}=0 \quad \text { on } \Gamma_{I}
$$

where (19) is the statement of equilibrium in the bulk, $\nabla_X \bullet$ is the divergence operator, $\rho_o^{(\alpha)} \mathbf{B}^{(\alpha)}$ is the body force in the reference configuration, and $\mathbf{P} = \mathbf{F} \mathbb{T}_{n+1}^{(\alpha)} \mathbf{F}_{n+1}^{-\mathbb{T}^{(\alpha)}} \boldsymbol{\Sigma} \mathbf{F}_{n+1}^{\mathbf{p}-\mathbb{T}^{(\alpha)}}$ is evaluated hereafter using a generic return mapping algorithm, given for example in Section 4.1. The Eqs. (20)-(24) represent the interface traction equilibrium, interface gap constraint, interface damage flow rule, interface softening relation, and Kuhn-Tucker consistency condition for damage/softening. The evaluation of (22) and (23) at interface quadrature points in terms of the numerical flux $\mathbf{T}_{n+1}$ obtained from (6) using $\mathbf{P}_{n+1}^{(\alpha)}$ is described in Section 4.2. Note that the evaluation of the numerical flux via the elastoplastic stress tensor was also derived for small strain [21,22] and finite strain [26] Discontinuous Galerkin formulations without debonding.

Employing weak enforcement of the variation $\delta \hat{\mathcal{P}}_n(\boldsymbol{\chi}_{n+1}, \boldsymbol{\eta}_o) =$ 0 and collocation at quadrature points for all other relations, we arrive at the variational Discontinuous Galerkin weak form of elastoplastic damage which is stated as follows: Find $\{\boldsymbol{\phi}_{n+1}^{(1)}, \boldsymbol{\phi}_{n+1}^{(2)}\} \in \mathcal{S}^{(1)} \times \mathcal{S}^{(2)}$ such that for all $\{\boldsymbol{\eta}_o^{(1)}, \boldsymbol{\eta}_o^{(2)}\} \in \mathcal{V}^{(1)} \times \mathcal{V}^{(2)}$:

$$
\begin{aligned}
& R\left(\boldsymbol{\phi}^{(\alpha)}, \boldsymbol{\eta}_{o}^{(\alpha)}\right)=0=\sum_{\alpha=1}^{2} \mathcal{P}_{\mathrm{ext}}\left(\boldsymbol{\phi}^{(\alpha)}\right) \\
& +\sum_{\alpha=1}^{2} \int_{\Omega^{(\alpha)}}\left[\nabla_{X} \boldsymbol{\eta}_{o}^{(\alpha)}: \mathbf{P}_{n+1}^{(\alpha)}\right] \mathrm{d} V \\
& +\int_{\Gamma_{i}} \mathbf{T}_{n+1} \cdot\left[\left[\boldsymbol{\eta}_{o}\right]\right] \mathrm{d} A+\int_{\Gamma_{i}}\left[\left\|\boldsymbol{\tau}_{s}\right\|\left(\left[\left[\boldsymbol{\phi}_{n+1}\right]\right]-\boldsymbol{\zeta}_{n+1}\right)\right] \cdot\left[\left[\boldsymbol{\eta}_{o}\right]\right] \mathrm{d} A \\
& +\int_{\Gamma_{i}}\left(\left[\left[\boldsymbol{\phi}_{n+1}\right]\right]-\boldsymbol{\zeta}_{n+1}\right) \cdot\left\{\left(\nabla_{X} \boldsymbol{\eta}_{o}: \mathbf{A}_{n+1}\right) \cdot \mathbf{N}\right\} \mathrm{d} A
\end{aligned}
$$

where the first elasticity tensor of material moduli $\mathbf{A}_{n+1}^{(\alpha)}$ is given in the Appendix. The appropriate functional spaces are contained in (26) and (27).

$$
\mathcal{S}^{(\alpha)}=\left\{\boldsymbol{\phi}^{(\alpha)} | \boldsymbol{\phi}^{(\alpha)} \in\left[H^{1}\left(\Omega^{(\alpha)}\right)\right]^{n_{\mathrm{sd}}}, \operatorname{det}\left(\mathbf{F}^{(\alpha)}\left(\boldsymbol{\phi}^{(\alpha)}\right)\right)>0,\left.\boldsymbol{\phi}^{(\alpha)}\right|_{\Gamma^{(\alpha)} \setminus \Gamma_{i}}=\mathbf{X}^{(\alpha)}\right\}
$$

$$
\mathcal{V}^{(\alpha)}=\left\{\boldsymbol{\eta}_{o}^{(\alpha)} | \boldsymbol{\eta}_{o}^{(\alpha)} \in\left[H_{0}^{1}\left(\Omega^{(\alpha)}\right)\right]^{n_{\mathrm{sd}}},\left.\boldsymbol{\eta}_{o}^{(\alpha)}\right|_{\Gamma^{(\alpha)} \setminus \Gamma_{i}}=\mathbf{0}\right\}
$$

## 4. Constitutive model and time integration for elastoplasticity and damage

We summarize the important steps of the return mapping scheme and Hencky material model that are used for a prototypical elastoplasticity algorithm. These constitutive assumptions help simplify the stress update by allowing infinitesimal strain predictor/corrector algorithms to be extended into the finite strain range [37,38]. The resulting stress update will provide the input for the computation of the numerical fluxes appearing in the Discontinuous Galerkin (DG) interface terms. As an additional contribution herein, the interface constitutive models and corresponding return mapping for triangular TSL are extended to extrinsic trapezoidal TSL. The new TSL has a material parameter for changing the shape of the TSL to include ductile interface effects. The reader is referred to the Appendix for the linearization of the weak form.

### 4.1. Hencky material model and elastic deformation gradient return mapping scheme

A quick summary of the elastoplastic constitutive models is presented. The reader is encouraged to see [37] for details. Let $\mathbf{V}^{\mathrm{e}}$ be the elastic left stretch tensor and $\mathbf{R}^{\mathrm{e}}$ be the elastic rotation tensor according to $\mathbf{F}^{\mathrm{e}}=\mathbf{V}^{\mathrm{e}} \mathbf{R}^{\mathrm{e}}, \mathbf{B}^{\mathrm{e}}=\mathbf{F}^{\mathrm{e}} \mathbf{F}^{\mathrm{eT}}$, and the Eulerian logarithmic elastic strain $\boldsymbol{\varepsilon}^{\mathrm{e}}=\ln \mathbf{V}^{\mathrm{e}}=\frac{1}{2} \ln \mathbf{B}^{\mathrm{e}}$. Consider a finite strain-based extension of linear elastic law that is presented using Hencky hyperelastic model with a strain energy function $\psi^{\mathrm{e}}:=\frac{1}{2} \boldsymbol{\varepsilon}^{\mathrm{e}}: \mathbf{C}: \boldsymbol{\varepsilon}^{\mathrm{e}}$. The moduli tensor $\mathbf{C}$ has the form of the infinitesimal isotropic elastic tensor, and the Kirchoff stress $\tau=\partial_{\boldsymbol{\varepsilon}^{\mathrm{e}}} \psi^{\mathrm{e}}=\mathbf{C}: \boldsymbol{\varepsilon}^{\mathrm{e}}$ has a linear relationship with logarithmic strain. Similarly, the yield function $\tilde{f}^{\mathrm{p}}(\boldsymbol{\tau}, \mathbf{Q}^{\mathrm{p}})=f^{\mathrm{p}}(\boldsymbol{\Sigma}, \mathbf{Q}^{\mathrm{p}})$ follows in a manner that is consistent with the transformation between the stress measures.

Next, the elastic deformation gradient update (28) - (29) is obtained by using the multiplicative split (1) and plastic deformation gradient backward exponential integration expression:

$$
\mathbf{F}_{n+1}^{\mathrm{e}}:=\mathbf{F}_{\Delta} \mathbf{F}_{n}^{\mathrm{e}} \mathbf{R}_{n+1}^{\mathrm{eT}} \exp \left[-\Delta \gamma^{\mathrm{p}} \partial_{\tau} \tilde{f}_{n+1}^{\mathrm{p}}\right] \mathbf{R}_{n+1}^{\mathrm{e}}
$$

$$
\mathbf{F}_{\Delta}:=\mathbf{F}_{n+1}\left(\mathbf{F}_{n}\right)^{-1}=\mathbf{I}+\partial_{\mathbf{X}_{n}}[\Delta \mathbf{u}]
$$

where the incremental displacement $\Delta \mathbf{u}=\boldsymbol{\varphi}(\mathbf{X}, t_{n+1})-\boldsymbol{\varphi}(\mathbf{X}, t_{n})$.

The trial state of the elastic deformation gradient and plastic hardening variable in (30) and (31) results from enforcing (28) with $\Delta \gamma^{\mathrm{p}}=0$.

$$
\mathbf{F}_{n+1}^{\mathrm{e} \text { trial }}:=\mathbf{F}_{\Delta} \mathbf{F}_{n}^{\mathrm{e}}
$$

$$
\boldsymbol{\alpha}_{n+1}^{\mathrm{p} \text { trial }}=\boldsymbol{\alpha}_{n}^{\mathrm{p}}
$$

The elastic state is accepted as the actual state if the ensuing trial stress and plastic flow are admissible, or the return mapping Eqs. (32)-(34) are solved.

$$
\mathbf{F}_{n+1}^{\mathrm{e}}:=\mathbf{F}_{n+1}^{\mathrm{e} \text { trial }} \mathbf{R}_{n+1}^{\mathrm{eT}} \exp \left[-\Delta \gamma^{\mathrm{p}} \partial_{\tau} \tilde{f}_{n+1}^{\mathrm{p}}\right] \mathbf{R}_{n+1}^{\mathrm{e}}
$$

$$
\boldsymbol{\alpha}_{n+1}^{\mathrm{p}}=\boldsymbol{\alpha}_{n+1}^{\mathrm{p} \text { trial }}+\Delta \gamma^{\mathrm{p}} \partial_{\mathbf{Q}^{\mathrm{p}}} \tilde{f}_{n+1}^{\mathrm{p}}
$$

$$
f_{n+1}^{\mathrm{p}} \leq 0, \quad \Delta \gamma^{\mathrm{p}} \geq 0, \quad f_{n+1}^{\mathrm{p}} \Delta \gamma^{\mathrm{p}}=0
$$

Plastic isotropy is assumed, which implies the Kirchoff stress $\tau_{n+1}$ and $\partial_{\tau} \tilde{f}_{n+1}^{\mathrm{p}}$ are coaxial. Under elastoplastic isotropy (zero plastic spin), $\mathbf{V}^{\mathrm{e}}$ and $\partial_{\tau} \tilde{f}_{n+1}^{\mathrm{p}}$ commute allowing for the simplification of (32) to arrive at (35):

$$
\mathbf{V}_{n+1}^{\mathrm{e}}:=\mathbf{V}_{n+1}^{\mathrm{e} \text { trial }} \exp \left[-\Delta \gamma^{\mathrm{p}} \partial_{\tau} \tilde{f}_{n+1}^{\mathrm{p}}\right]
$$

We arrive at a much simpler Eq. (36) by taking the tensor logarithm of both sides. Notice that (36) is expressed in terms of Eulerian logarithmic strain tensors.

$$
\boldsymbol{\varepsilon}_{n+1}^{\mathrm{e}}=\boldsymbol{\varepsilon}_{n}^{\mathrm{e} \text { trial }}-\Delta \gamma^{\mathrm{p}} \partial_{\tau} \tilde{f}_{n+1}^{\mathrm{p}}\left(\boldsymbol{\tau}_{n+1}, \mathbf{Q}_{n+1}^{\mathrm{p}}\right)
$$

Therefore, return mapping equation of the finite strain incremental problem (43) is similar to backward return mapping algorithms of the infinitesimal theory. We adopt a von Mises yield function with linear isotropic hardening as the prototypical plasticity model herein, with material parameters identified in Section 5. The detailed return mapping algorithm is described in Table 1.

### 4.2. Interface constitutive models and corresponding return mapping

We depart from the discussion of the plasticity in the bulk and turn to the damage constitutive behavior of the interface. We extend the earlier developments of triangular TSL in [25] to extrinsic trapezoidal TSL that is more suitable for ductile fracture. The extrinsic trapezoidal TSL does not have compliance issues associated with the common trapezoidal TSL.

A return mapping algorithm for the extrinsic trapezoidal TSL in Fig. 2 is developed for modeling interfacial damage. Similar to [10,11,39], it is assumed that certain fracture processes belong either to forward region or wake region of the TSL. Let $G_c$ be the total cohesive fracture energy required for creating a new crack surface. The cohesive energy associated to the forward region is

<table><thead><tr><th colspan="2">Table 1 Integration algorithm for von Mises plasticity in Hencky elasticity material.</th></tr></thead><tbody><tr><td colspan="2">Step 1: Given the incremental displacement $\Delta \mathbf{u}$</td></tr><tr><td colspan="2">Step 2: Update the deformation gradient</td></tr><tr><td colspan="2">$\mathbf{F}_{\Delta}:=\mathbf{I}+\nabla_{n}[\Delta \mathbf{u}], \quad \mathbf{F}_{n+1}:=\mathbf{F}_{\Delta} \mathbf{F}_{n}$ (37)</td></tr><tr><td colspan="2">Step 3: Compute the elastic trial state</td></tr><tr><td colspan="2">$\mathbf{B}_{n}^{\mathrm{e}}:=\exp [2 \boldsymbol{\varepsilon}_{n}^{\mathrm{e}}]$ (38)</td></tr><tr><td colspan="2">$\mathbf{B}_{n+1}^{\mathrm{e} \text { trial }}:=\mathbf{F}_{\Delta} \mathbf{B}_{n}^{\mathrm{e}}(\mathbf{F}_{\Delta})^{T}$ (39)</td></tr><tr><td colspan="2">$\boldsymbol{\varepsilon}_{n}^{\mathrm{e} \text { trial }}:=\ln [\mathbf{V}_{n+1}^{\mathrm{e} \text { trial }}]=\frac{1}{2} \ln [\mathbf{B}_{n+1}^{\mathrm{e} \text { trial }}]$ (40)</td></tr><tr><td colspan="2">$\boldsymbol{\alpha}_{n+1}^{\mathrm{p} \text { trial }}:=\boldsymbol{\alpha}_{n}^{\mathrm{p}}$ (41)</td></tr><tr><td colspan="2">$\boldsymbol{\tau}_{n+1}^{\text {trial }}:=\partial_{\boldsymbol{\varepsilon}^{\mathrm{e}}} \psi^{\mathrm{e}}(\boldsymbol{\varepsilon}^{\mathrm{e}}{ }_{n+1}{ }^{\text {trial }}), \quad \mathbf{Q}_{n+1}^{\mathrm{p} \text { trial }}:=\partial_{\boldsymbol{\alpha}^{\mathrm{p}}} \psi^{\mathrm{p}}(\boldsymbol{\alpha}_{n}^{\mathrm{p}}{ }^{\text {trial }})$ (42)</td></tr><tr><td colspan="2">IF $\tilde{f}^{\mathrm{p}}(\boldsymbol{\tau}_{n+1}^{\text {trial }}, \mathbf{Q}_{n+1}^{\mathrm{p} \text { trial }}) ≤ 0$ THEN</td></tr><tr><td colspan="2">$\operatorname{set}(\cdot)_{n+1}:=(\cdot)_{n+1}^{\text {trial }}$, and EXIT</td></tr><tr><td colspan="2">ELSE</td></tr><tr><td colspan="2">Plastic evolution step: Proceed to Step 4</td></tr><tr><td colspan="2">ENDIF</td></tr><tr><td colspan="2">Step 4: Return mapping with $\boldsymbol{\tau}_{n+1}:=\partial_{\boldsymbol{\varepsilon}^{e}} \psi^{\mathrm{e}}(\boldsymbol{\varepsilon}_{n+1}^{\mathrm{e}}), \quad \mathbf{Q}_{n+1}^{\mathrm{p}}:=\partial_{\boldsymbol{\alpha}^{\mathrm{p}}} \psi^{\mathrm{p}}(\boldsymbol{\alpha}_{n+1}^{\mathrm{p}})$</td></tr><tr><td colspan="2">solve for $\boldsymbol{\varepsilon}_{n+1}^{\mathrm{e}}, \boldsymbol{\alpha}_{n+1}^{\mathrm{p}}$ and $\Delta \gamma^{\mathrm{p}}$</td></tr><tr><td colspan="2">$\left\{\begin{array}{l}\boldsymbol{\varepsilon}_{n+1}^{\mathrm{e}}-\boldsymbol{\varepsilon}_{n}^{\mathrm{e} \text { trial }}+\Delta \gamma^{\mathrm{p}} \partial_{\boldsymbol{\tau}} \tilde{f}^{\mathrm{p}}(\boldsymbol{\tau}_{n+1}, \mathbf{Q}_{n+1}^{\mathrm{p}}) \\ \boldsymbol{\alpha}_{n+1}^{\mathrm{p}}-\boldsymbol{\alpha}_{n}^{\mathrm{p}}-\Delta \gamma^{\mathrm{p}} \partial_{\mathbf{Q}^{\mathrm{p}}} \tilde{f}^{\mathrm{p}}(\boldsymbol{\tau}_{n+1}, \mathbf{Q}_{n+1}^{\mathrm{p}}) \\ \tilde{f}^{\mathrm{p}}(\boldsymbol{\tau}_{n+1}, \mathbf{Q}_{n+1}^{\mathrm{p}})\end{array}\right\}=\left\{\begin{array}{l}0 \\ 0 \\ 0\end{array}\right\}$ (43)</td></tr><tr><td colspan="2">Step 5: Update the first Piola-Kirchhoff stress</td></tr><tr><td colspan="2">$\mathbf{P}_{n+1}:=\boldsymbol{\tau}_{n+1} \mathbf{F}_{n+1}^{-T}$ (44)</td></tr></tbody></table>

![](./images/812553785921503232_2.jpg)

Fig. 2. Extrinsic trapezoidal traction separation law.

known as the extrinsic cohesive fracture energy $\Gamma^{ext}$ while intrinsic fracture cohesive energy $\Gamma^{int}$ is associated to the wake region, such that $\Gamma^{int} \cup \Gamma^{ext}=G_{c}$. We remark that the intrinsic and extrinsic cohesive fracture energies herein have separate meanings from those directly associated to the intrinsic or extrinsic cohesive zone methods.

The reader is first referred to [25] for details of the return mapping algorithm developed for triangular TSL in Fig. 3. An isotropic yield function is assumed, such that the single hardening variable is given by $Q^{d}$. Herein, an extension of the triangular TSL model is done by adding a plateau condition to the hardening law for when the norm of the residual gap $\zeta=\|\zeta\|$ is less than the transition gap constraint $\zeta_{b}$, while the interface gap evolution remains as an associative flow rule according to normality [25]:

$$
\dot{Q}^{d}= \begin{cases}0, & \left\|\boldsymbol{\zeta}_{n}\right\| \leq \zeta_{\mathrm{b}} \text { (forward dam.) } \\ H_{c} \dot{\gamma}^{\mathrm{d}}, & \zeta_{\mathrm{b}}<\left\|\boldsymbol{\zeta}_{n}\right\|<\zeta_{\mathrm{c}} \text { (wake dam.) } \\ 0, & \zeta_{\mathrm{c}} \leq\left\|\boldsymbol{\zeta}_{n}\right\| \text { (opening) }\end{cases}
$$

$$
\dot{\boldsymbol{\zeta}}=\dot{\gamma}^{\mathrm{d}}\left(\partial f^{\mathrm{d}} / \partial \mathbf{T}\right)
$$

where $H_{c}=P_{c} /(\zeta_{c}-\zeta_{b})$ is the softening slope, $P_{c}$ is the critical debonding traction magnitude in the reference configuration, and $\zeta_{c}$ is the maximum residual opening. The transition gap constraint $\zeta_{b}$ serves as a material parameter for changing the shape of the

![](./images/812553785921503232_3.jpg)

Fig. 3. Triangular separation law.

TSL to represent ductile damage. By substitutituting (22) - (23) into the consistency condition (24) and accounting for normality [25], the incremental consistency parameter $\Delta \gamma^{d}$ can be obtained as follows:

$$
\begin{aligned}
0 & =f_{n+1}^{\mathrm{d}}=\left\|\mathbf{T}_{n+1}\right\|-\left(P_{c}-Q_{n+1}^{\mathrm{d}}\right) \\
& =\left\|\mathbf{T}_{n+1}^{\text {trial }}\right\|-\left\|\boldsymbol{\tau}_{s}\right\| \Delta \gamma^{\mathrm{d}}-\left(P_{c}-Q_{n}^{\mathrm{d}}\right)+\Delta Q_{n+1}^{\mathrm{d}}
\end{aligned}
$$

where the hardening increment $\Delta Q_{n+1}^{\mathrm{d}}$ comes from evaluating the damage conditional (45) with $\Delta \gamma^{d}$.

Crucially, the trial interface flux $\mathbf{T}_{n+1}^{\text {trial }}=$ $\left\{\mathbf{P}_{n+1} \mathbf{N}\right\}+\left\|\boldsymbol{\tau}_{s}\right\|\left(\left\|\boldsymbol{\phi}_{n+1}\right\|-\zeta_{n}\right)$ involves the interface gap $\zeta_{n}$ from the last converged step and the current value of the deformation map $\boldsymbol{\phi}_{n+1}^{(\alpha)}$ and stress tensor $\mathbf{P}_{n+1}^{(\alpha)}$ on each side of $\Gamma_{I}$, with the latter evaluated using Table 1. Lastly, defining $f_{n+1}^{\text {trial }}=\left\|\mathbf{T}_{n+1}^{\text {trial }}\right\|-\left(P_{c}-Q_{n}^{\mathrm{d}}\right)$, we combine (45) and (47) to find $\Delta \gamma^{\mathrm{d}}$ for all stages as well as the updated interface gap:

$$
\Delta \gamma^{\mathrm{d}}= \begin{cases}f_{n+1}^{\text {trial }} /\left\|\boldsymbol{\tau}_{s}\right\|, & \left\|\boldsymbol{\zeta}_{n}\right\| \leq \zeta_{\mathrm{b}} \\ f_{n+1}^{\text {trial }} /\left(\left\|\boldsymbol{\tau}_{s}\right\|-H_{c}\right), & \zeta_{\mathrm{b}}<\left\|\boldsymbol{\zeta}_{n}\right\|<\zeta_{\mathrm{c}} \\ \left\|\mathbf{T}_{n+1}^{\text {trial }}\right\| /\left(\left\|\boldsymbol{\tau}_{s}\right\|-H_{c}\right), & \zeta_{\mathrm{c}} \leq\left\|\boldsymbol{\zeta}_{n}\right\|\end{cases}
$$

$$
\boldsymbol{\zeta}_{n+1}=\boldsymbol{\zeta}_{n}+\Delta \gamma^{\mathrm{d}} \mathbf{T}_{n+1}^{\text {trial }} /\left\|\mathbf{T}_{n+1}^{\text {trial }}\right\|
$$

Remark: While an isotropic damage model has been considered (accounting for contact under compression as in [25]), more general TSL could be envisioned for this formulation. The extrinsic trapezoidal TSL was chosen since the shape can be varied to model either ductile interface behavior or brittle interface behavior through one parameter. Additionally, generalized isotropic plasticity models with segmented hardening curves could be utilized. Note that, similar to trapezoidal CZM, the plasticity hardening curve must not plateau or soften prior to reaching the critical stress in order to ensure global stability and uniqueness of the numerical solution.

## 5. Numerical results

In this section, we investigate the performance of this method using a patch test of a 3-dimensional rectangular block and a compact tension specimen test. The bubble functions used for evaluating the stability tensor of three dimensional meshes are presented in [40], and all calculations are performed using full numerical quadrature with 8-node trilinear bulk elements. The plastic hardening behavior is characterized using the finite strain von Mises flow theory. The computed global responses of the materials using

![](./images/812553785921503232_4.jpg)

Fig. 4. Problem domain and boundary condition.

![](./images/812553785921503232_5.jpg)

Fig. 5. Finite element mesh.

the triangular TSL and the extrinsic trapezoidal TSL are compared for suitability to model macroscale ductile damage.

### 5.1. Patch test of a rectangular block

A displacement of 1.5 mm is applied at 70 equal load steps onto a $4\ \text{mm} \times 2\ \text{mm} \times 1\ \text{mm}$ block shown in Fig. 4. The block is discretized into 8 linear hexahedral elements as in Fig. 5; symmetry conditions are applied on the surfaces $x = 0$ and $y = 0$, and all surfaces are constrained from deforming along the $z$ direction. We assume cracks initiate and grow at the middle plane only. For this reason, interface elements are only inserted at the middle plane [41]. We remark that interface elements could be inserted on all solid elements faces for problems where crack initiation and growth are not known a-priori [42]. The Hencky hyperelastic material model with material properties specified as $E = 100\ \text{MPa}$ and $\upsilon = 0.25$, yield stress is $\sigma_y = 5\ \text{MPa}$ and the plastic modulus $K = 20\ \text{MPa}$ is used.

A TSL shape parameter study is performed using two test cases, each comparing the total reaction force versus applied displacement $(f - \delta)$ relation of an extrinsic trapezoidal TSL to two triangular TSLs. The first triangular TSL is produced by setting $\zeta_b = 0$ while retaining the cohesive fracture energy, and the second triangular TSL retains only the intrinsic cohesive energy (energy in wake region only) of the trapezoidal TSL. The interface material properties for all test cases considered are presented in Table 2. We remark that, due to the variational consistency of the formulation as shown for elastic and plastic models [17,22], the computed interface gap prior to damage (yet before and after bulk plasticity develops) vanishes to machine precision.

Fig. 6 shows the force-displacement plot obtained from all TSL models in the first test case. Essentially, the bulk and interface responses of the body are in series with each other. The block first stretches elastically and then plastically while the interface is bonded. Then, the interface begins to debond and the block unloads elastically. The plastic hardening is noticeably small because of the small difference between the yield stress and critical stress chosen for this example. The $f - \delta$ relation is the same from all the TSL types considered when the stress is lower than the critical value.

The ductile fracture behavior (sustained force during increased deformation) is more noticeable in the trapezoidal TSL while the triangular models exhibit more brittle behavior. The difference in the shape of the TSL and the fracture energies are responsible for the difference in material responses; the total area under the curve of the triangle-A and trapezoidal case appear similar, in agreement with the shared $G_c$ parameter.

Fig. 7 shows the global material response obtained from all TSL models in the second test case. The effect of the choice of the TSL shape parameters on the global force-displacement results is more noticeable than in the first case. In the second test case, the solid elastoplastic material properties of the first case are retained while changes are made to the interface properties. The critical stress is higher than the value in the previous example. This allows the material to plastically deform more than the first test case before damage. The reduction in the reaction force of the triangular-A TSL is more gradual than the other models. Meanwhile, the trapezoidal and triangular-B TSL exhibit rapid force reduction due to the conversion of elastic energy in the blocks into dissipated fracture energy at the interface.

For interface models with the same fracture energy, the trapezoidal TSL represents a more realistic experimental ductile fracture result because it permits more work of separation to be captured by the forward region of the TSL. However, there does not appear to be a restriction on the form of the TSL that the DG method can accommodate.

<table>
<caption>Table 2<br>Interface constitutive material properties.</caption>
<thead>
<tr>
<th>First case</th>
<th>$P_c$(MPa)</th>
<th>$\zeta_b$(mm)</th>
<th>$\zeta_c$(mm)</th>
<th>$G_c$(KJ/m²)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Trapez.</td>
<td>5.5</td>
<td>0.1</td>
<td>1.1</td>
<td>3.3</td>
</tr>
<tr>
<td>Triang.-A</td>
<td>5.5</td>
<td>0.0</td>
<td>2.2</td>
<td>3.3</td>
</tr>
<tr>
<td>Triang.-B</td>
<td>5.5</td>
<td>0.0</td>
<td>1</td>
<td>2.75</td>
</tr>
<tr>
<td>Second case</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Trapez.</td>
<td>7.0</td>
<td>0.3</td>
<td>0.8</td>
<td>4.4</td>
</tr>
<tr>
<td>Triang.-A</td>
<td>7.0</td>
<td>0.0</td>
<td>1.1</td>
<td>4.4</td>
</tr>
<tr>
<td>Triang.-B</td>
<td>7.0</td>
<td>0.0</td>
<td>0.5</td>
<td>1.75</td>
</tr>
</tbody>
</table>

![](./images/812553785921503232_6.jpg)

Fig. 6. Global material response, first test case.

![](./images/812553785921503232_7.jpg)

Fig. 7. Global material response, second test case.

![](./images/812553785921503232_8.jpg)

Fig. 9. CT specimen, force vs. displacement response.

![](./images/812553785921503232_9.jpg)

Fig. 8. CT specimen, coarse FE mesh.

### 5.2. Force-displacement predictions for cracked CT specimen

The accuracy of the DG method is examined in comparison with a fracture analysis using the Park-Paulino-Roesler (PPR) cohesive zone model (CZM) [43] as implemented in the WARP3D code [44]. For the analysis domain, a coarse finite element mesh of a CT specimen having one layer of solid elements over its thickness and constrained at the surface with $z=0$ (analogous to plane stress) is used from a benchmark in the WARP3D code, as shown in Fig. 8. The CT specimen dimensions are $W=50.8$ mm, $B=0.5715$ mm and $a/W=0.24$, and it contains 1744 solid elements with 76 interface elements inserted along the direction of crack growth; note that both CZM and DG can be implemented via interface elements [45]. The material properties are specified as $E=71.66$ GPa, $v=0.3$, yield strength $\sigma_y=345$ GPa, and plastic modulus $K=170$ MPa.

The Discontinuous Galerkin interface conditions are $P_c=600$ GPa, $\zeta_b=0.001$ mm, and $\zeta_c=0.0042$ mm. A PPR model with interface conditions having equivalent cohesive fracture energy $G_c=39.63$ KJ/m² is used for comparison. The cohesive zone model is described using $P_c=600$ GPa, initial slope $\lambda=0.2$ and separation curve shape $\alpha=20$. Note also that the isotropic plasticity model in WARP3D is expressed through a hypoelastic formulation based on the Green-Naghdi objective stress rate; the CT specimen strains remain small so that this difference is expected to minimally impact the results, which was confirmed from infinite toughness simulations.

A monotonic vertical displacement is applied to the center node of the upper-left stiff-elastic pin in the CT specimen, and the computed reaction versus the displacement (measured center to center of the pins) is reported in Fig. 9. The $f-\delta$ results from both methods are close even for a coarse mesh. The lower force produced from the CZ method in the initial elastic region ($f<0.6$kN) is attributed to artificial compliance of the CZM method. The later difference in the results from the two methods after plasticity and damage accrue is attributed to both the artificial compliance and the different shapes of the PPR and trapezoidal TSL, most likely to the latter as in [13-15].

### 6. Conclusions

This method extends our previous work for modeling quasi-static and dynamic damage to enable elastoplastic deformation before damage. This paper derives the Discontinuous Galerkin method from the free energy and dissipation functional and relies on the assumption that the free energy can be decomposed to the elastic and plastic processes in the material domain and localized damage processes at the interface. The distinctive features of the formulation are the treatment of the nonlinear constitutive updates of the internal variables in both the bulk domains and interface, and the treatment of numerical flux at the interface for large strain plasticity. We extend the return mapping algorithm of a triangular TSL to an extrinsic trapezoidal TSL that is free from artificial compliance issues and suitable for modeling ductile damage processes. The new TSL allows either brittle or ductile interface behavior in an elastoplastic deforming body by varying a single material parameter. This will provide the capability of the method to model macroscale ductile interface fracture or brittle intergranular separation in plastically deforming microstructure. The results from the patch test show that the method can accommodate other TSL forms. The comparison of the results from the method to those from the cohesive zone method produced from modeling CT specimen crack example shows that the method produces physical and meaningful results on coarse meshes.

### Declaration of Competing Interest

The authors confirm that there is no conflict of interests associated with this work and this manuscript has not been submitted to, nor is under review at, another journal or other publishing venue.

### Acknowledgement

This material is based upon work supported by the National Science Foundation, USA under Grant No. CMMI-1751591.

### Appendix
#### Stability tensor

The stability tensor $\boldsymbol{\tau}_{s}^{(\alpha)}$ is defined locally along segments $\gamma_{s}$ of the interface $\Gamma_{I}$ according to the following expressions (with notation given in [36,40]):

$$
\boldsymbol{\tau}_{s}^{(\alpha)}=\left[\operatorname{meas}\left(\gamma_{s}\right)\right]^{-1}\left(\int_{\gamma_{s}} b_{s}^{(\alpha)} \mathrm{d} A\right)^{2} \widetilde{\boldsymbol{\tau}}_{s}^{(\alpha)}
\tag{50}
$$

$$
\widetilde{\boldsymbol{\tau}}_{s}^{(\alpha)}=\left[\int_{\omega_{s}^{(\alpha)}} \nabla_{X} \mathbf{b}_{s}^{(\alpha)}: \mathbf{A}_{n+1}^{(\alpha)}: \nabla_{X} \mathbf{b}_{s}^{(\alpha)} \mathrm{d} V\right]^{-1}
\tag{51}
$$

where the bubble $\mathbf{b}_{s}^{(\alpha)}=\sum_{J=1}^{n_{s d}} b_{s}^{(\alpha)} \mathbf{E}_{J}$ is supported on a sector $\omega_{s}^{(\alpha)}$ and $\mathbf{E}_{J}$ are the reference frame Cartesian basis vectors. The bubble functions $b_{s}^{(\alpha)}$ are higher order polynomials that vanish on the boundaries of the sector $\omega_{s}^{(\alpha)}$ that are not in contact with segment $\gamma_{s}$, $\nabla_{X}(\bullet)$ denotes the gradient with respect to the reference coordinate, and $\mathbf{A}_{n+1}^{(\alpha)}=d^{2} \psi^{e} / d \mathbf{F}_{n+1}^{(\alpha)} d \mathbf{F}_{n+1}^{(\alpha)}$ is the first elasticity tensor of material moduli, computed as the total algorithmic derivative of the associated strain energy density function. An expression for $\mathbf{A}$ in component form is provided in [37] along with the model-specific stress derivative $d \boldsymbol{\tau}_{n+1} / d \mathbf{F}_{n+1}$:

$$
A_{i I j J}=\frac{d \tau_{i k}}{d F_{j J}} F_{I k}^{-1}-\tau_{i k} F_{I j}^{-1} F_{J k}^{-1}
\tag{52}
$$

Perhaps the most attractive feature of this stabilized definition of $\mathbf{T}$ as described in our previous works [36,40] is that the stability parameter $\boldsymbol{\tau}_{s}^{(\alpha)}$ is systematically derived and accounts for the variation of material properties and element geometry adjacent to the interface. The derivation that led to the analytical solution of $\boldsymbol{\tau}_{s}^{(\alpha)}$ in (50) relies on variational multiscale ideas where the displacement field is decomposed into coarse and fine scales. The analytical solution of the fine scales is substituted into the coarse-scale problem to provide a stabilizing effect to the formulation. Herein, we follow additional steps as in [22] for accommodating history dependent plastic material response by treating the fine scales as small perturbations about the current coarse-scale deformation. Further details on computing $\boldsymbol{\tau}_{s}^{(\alpha)}$ are presented in [22,36]. Note that the novel contribution herein is to extend the small strain plastic formulation of [22] to large strains in combination with evolving interface debonding $\boldsymbol{\zeta}$.

Remark: Notice that the stability tensor depends on the first elasticity tensor which introduces the effect of evolving geometric and material nonlinearity properties of the adjacent elements into evolution of $\boldsymbol{\tau}_{s}^{(\alpha)}$. The softening of the tangent tensor during prolonged plasticity can affect the stability of the method, particularly when the interface begins to debond and the bulk responds incrementally elastically. Herein, the initial elastic tensor is employed in order to guarantee positive definiteness of the stability tensor $\boldsymbol{\tau}_{s}^{(\alpha)}$ for all timesteps [22].

### Weak form linearization

For completeness, the linearization of the weak form (25) can then be expressed as follows; the reader is encouraged to consult [25] for details:

$$
\begin{aligned}
& K\left(\boldsymbol{\eta}_{o}^{(\alpha)}, \Delta \mathbf{u}^{(\alpha)} ; \boldsymbol{\phi}^{(\alpha)}\right) \\
& =\sum_{\alpha=1}^{2} \int_{\Omega^{(\alpha)}} \nabla_{X} \boldsymbol{\eta}_{o}^{(\alpha)}: \mathbf{A}^{(\alpha)}: \nabla_{X}\left(\Delta \mathbf{u}^{(\alpha)}\right) \mathrm{d} V \\
& \quad+\int_{\Gamma_{I}} \llbracket \boldsymbol{\eta}_{o} \rrbracket \cdot\left\|\boldsymbol{\tau}_{s}\right\|\|\Delta \mathbf{u}\| \mathrm{d} A \\
& \quad+\int_{\Gamma_{I}} \llbracket \boldsymbol{\eta}_{o} \rrbracket \cdot\left\{\left[\mathbf{A}: \nabla_{X}(\Delta \mathbf{u})\right] \cdot \mathbf{N}\right\} \mathrm{d} A \\
& \quad+\int_{\Gamma_{I}}\left\{\left(\nabla_{X} \boldsymbol{\eta}_{o}: \mathbf{A}\right) \cdot \mathbf{N}\right\} \cdot \llbracket \Delta \mathbf{u} \rrbracket \mathrm{d} A \\
& \quad+\int_{\Gamma_{I}}\left\{\left[\nabla_{X} \boldsymbol{\eta}_{o}: \boldsymbol{\Xi}: \nabla_{X}(\Delta \mathbf{u})\right] \cdot \mathbf{N}\right\} \cdot(\llbracket \boldsymbol{\phi} \rrbracket-\boldsymbol{\zeta}) \mathrm{d} A \\
& \quad-\int_{\Gamma_{I}} \tilde{\mathbf{T}}\left(\boldsymbol{\eta}_{o}\right) \cdot\left[\frac{\partial}{\partial \mathbf{T}}\left(\Delta \gamma^{\mathrm{d}} \partial_{\mathbf{T}} f^{\mathrm{d}}\right) \cdot \tilde{\mathbf{T}}(\Delta \mathbf{u})\right] d A
\end{aligned}
\tag{53}
$$

where the subscript $n+1$ has been suppressed, and $\boldsymbol{\Xi}=d \mathbf{A}_{n+1}^{(\alpha)} / d \mathbf{F}_{n+1}^{(\alpha)}$ is a sixth order tensor of material moduli, as well as $\tilde{\mathbf{T}}$ is an incremental interface flux and $\frac{\partial}{\partial \mathbf{T}}\left(\Delta \gamma^{\mathrm{d}} \partial_{\mathbf{T}} f_{n+1}^{\mathrm{d}}\right)$ is the linearized damage tensor expression according to:

$$
\tilde{\mathbf{T}}(\bullet)=\left[\left\{\left(\nabla_{X}(\bullet): \mathbf{A}\right) \cdot \mathbf{N}\right\}+\llbracket \cdot \rrbracket \cdot\left\|\boldsymbol{\tau}_{s}\right\|\right]
\tag{54}
$$

$$
\frac{\partial}{\partial \mathbf{T}}\left(\Delta \gamma^{\mathrm{d}} \partial_{\mathbf{T}} f_{n+1}^{\mathrm{d}}\right)=\frac{\partial \Delta \gamma^{\mathrm{d}}}{\partial \mathbf{T}} \otimes \partial_{\mathbf{T}} f_{n+1}^{\mathrm{d}}+\gamma^{\mathrm{d}} \partial_{\mathbf{T T}} f_{n+1}^{\mathrm{d}}
\tag{55}
$$

In most cases the term involving $\boldsymbol{\Xi}$ can be neglected with only a minor reduction in the convergence rate of the Newton iterations residual norm.

### References

[1] J. Besson, Continuum models of ductile fracture: a review, Int. J. Damage Mech. 19 (1) (2010) 3-52.
[2] A. Pineau, A.A. Benzerga, T. Pardoen, Failure of metals I: brittle and ductile fracture, Acta Mater. 107 (2016) 424-483.
[3] J.R. Rice, A path independent integral and the approximate analysis of strain concentration by notches and cracks, J. Appl. Mech. 35 (2) (1968) 379-386.
[4] J. Rice, G.F. Rosengren, Plane strain deformation near a crack tip in a power-law hardening material, J. Mech. Phys. Solids 16 (1) (1968) 1-12.
[5] T.L. Anderson, Fracture Mechanics: Fundamentals and Applications, 3rd edition, CRC Press, Boca Raton, 2005, 640 pages.
[6] L. Kachanov, Time of the rupture process under creep conditions, Izy Akad, Nank SSR Otd Tech Nauk 8 (1958) 26-31.
[7] P. Germain, Q.S. Nguyen, P. Suquet, Continuum thermodynamics, J. Appl. Mech. 50 (4b) (1983) 1010-1020.
[8] V. Tvergaard, A. Needleman, Analysis of the cup-cone fracture in a round tensile bar, Acta Metall. 32 (1) (1984) 157-169.
[9] J. Besson, C. Guillemer-Neel, An extension of the green and gurson models to kinematic hardening, Mech. Mater. 35 (1-2) (2003) 1-18.
[10] R.O. Ritchie, Mechanisms of fatigue-crack propagation in ductile and brittle solids, Int. J. Fract. 100 (1) (1999) 55-83.
[11] H. Li, N. Chandra, Analysis of crack growth and crack-tip plasticity in ductile materials using cohesive zone models, Int. J. Plast. 19 (6) (2003) 849-882.
[12] N. Murphy, A. Ivankovic, The prediction of dynamic fracture evolution in PMMA using a cohesive zone model, Eng. Fract. Mech. 72 (6) (2005) 861-875.
[13] S. Salih, K. Davey, Z. Zou, Rate-dependent elastic and elasto-plastic cohesive zone models for dynamic crack propagation, Int. J. Solids Struct. 90 (2016) 95-115.
[14] H.D. Espinosa, P.D. Zavattieri, A grain level model for the study of failure initiation and evolution in polycrystalline brittle materials. Part I: theory and numerical implementation, Mech. Mater. 35 (3) (2003) 333-364.
[15] M.G.A. Tijssens, B.L.J. Sluys, E. van der Giessen, Numerical simulation of quasi-brittle fracture using damaging cohesive surfaces, Eur. J. Mech. A. Solids 19 (5) (2000) 761-779.
[16] A. Seagraves, R. Radovitzky, in: Advances in Cohesive Zone Modeling of Dynamic fracture, in Dynamic failure of Materials and Structures, Springer, 2009, pp. 349-405.

[17] S.C. Aduloju, T.J. Truster, A variational multiscale discontinuous Galerkin for- mulation for both implicit and explicit dynamic modeling of interfacial frac- ture, Comput. Meth. Appl. Mech. Eng. 343 (2019) 602-630.

[18] S. Wulfinghoff, et al., A low-order locking-free hybrid discontinuous Galerkin element formulation for large deformations, Comput. Meth. Appl. Mech. Eng.323(2017)353-372.

[19] T.J. Truster, P. Chen, A. Masud, Finite strain primal interface formulation withconsistently evolving stabilization, Int. J. Numer. Methods Eng. 102 (3-4)(2015) 278-315.

[20] A. Alipour, et al., The concept of control points in hybrid discontinuous Galerkin methods-application to geometrically nonlinear crystal plasticity, Int. J. Numer. Methods Eng. 114(5)(2018) 557-579.

[21] R. Liu, et al., A fast convergent rate preserving discontinuous Galerkin frame- work for rate-independent plasticity problems, Comput. Appl. Mech. Eng.199(49)(2010) 3213-3226.

[22] T.J. Truster, A. stabilized, symmetric Nitsche method for spatially localized plasticity, Comput. Mech. 57 (1) (2016) 75-103.

[23] S.C. Aduloju, T.J. Truster, A primal formulation for imposing periodic boundary conditions on conforming and nonconforming meshes, Comput. Meth. Appl. Mech.Eng.359(2020)112663.

[24] T.J. Truster, A. Masud, A discontinuous/continuous Galerkin method for model-ing of interphase damage in fibrous composite systems, Comput. Mech. 52 (3)(2013)499-514.

[25] P. Chen, T.J. Truster, A. Masud, Interfacial stabilization at finite strains for weak and strong discontinuities in multi-constituent materials, Comput. Meth. Appl. Mech.Eng.328(2018)717-751.

[26] R. Liu, M.F. Wheeler, I. Yotov, On the spatial formulation of discontinuous Galerkin methods for finite elastoplasticity, Comput. Appl. Mech. Eng.253(2013)219-236.

[27] M. Brünig, S. Ricci, Nonlocal continuum theory of anisotropically damaged metals, Int. J. Plast. 21 (7)(2005) 1346-1382.

[28] E. de Souza Neto, D. Peric, A computational framework for a class of fully cou- pled models for elastoplastic damage at finite strains with reference to the lin- earization aspects, Comput. Meth. Appl. Mech. Eng. 130 (1-2) (1996) 179-193.

[29] B.D. Coleman, M.E. Gurtin, Thermodynamics with internal state variables, J. Chem.Phys.47(2)(1967)597-613.

[30] B.D. Coleman, W. Noll, in: The Thermodynamics of Elastic Materials With Heat Conduction and viscosity, in The Foundations of Mechanics and Thermody- namics, Springer, 1974, pp. 145-156.

[31] J.C. Simo, T.J. Hughes, Computational Inelasticity, 7, Springer Science & Business Media, 2006.

[32] M. Ortiz, L. Stainier, The variational formulation of viscoplastic constitutive up- dates, Comput. Meth. Appl. Mech. Eng. 171 (3) (1999) 419-444.

[33] J. Mosler, O. Bruhns, Towards variational constitutive updates for non-associa- tive plasticity models at finite strain: models based on a volumetric-deviatoric split, Int. J. Solids Struct. 46 (7-8) (2009) 1676-1684.

[34] M. Tanaka, D. Balzani, J. Schroder, Implementation of incremental variational formulations based on the numerical calculation of derivatives using hyper dual numbers, Comput. Meth. Appl. Mech. Eng. 301 (2016) 216-241.

[35] T.J. Hughes, et al., The variational multiscale method-a paradigm for compu- tational mechanics, Comput. Meth. Appl. Mech. Eng. 166 (1-2) (1998) 3-24.

[36] T.J. Truster, A. Masud, Primal interface formulation for coupling multiple PDEs: a consistent derivation via the variational multiscale method, Comput. Meth. Appl. Mech.Eng.268(2014)194-224.

[37] E.A. de Souza Neto, D. Peric, D.R. Owen, Computational Methods for Plasticity: Theory and Applications, John Wiley & Sons, 2011.

[38] T. Elguedj, T.J. Hughes, Isogeometric analysis of nearly incompressible large strain plasticity, Comput. Meth. Appl. Mech. Eng. 268 (2014) 388-416.

[39] R. Ritchie, Mechanisms of fatigue crack propagation in metals, ceramics and composites: role of crack tip shielding, Mater. Sci. Eng. 103 (1) (1988) 15-28.

[40] T.J. Truster, P. Chen, A. Masud, On the algorithmic and implementational as- pects of a discontinuous Galerkin method at finite strains, Comput. Math. Appl.70(6)(2015)1266-1289.

[41] S.C. Aduloju, T.J. Truster, On topology-based cohesive interface element inser- tion along periodic boundary surfaces, Eng. Fract. Mech. 205 (2019) 10-13.

[42] E. Repetto, R. Radovitzky, M. Ortiz, Finite element simulation of dynamic frac-ture and fragmentation of glass rods, Comput. Meth. Appl. Mech. Eng. 183(1-2)(2000)3-14.

[43] K. Park, G.H. Paulino, J.R. Roesler, A unified potential-based cohesive model of mixed-mode fracture, J. Mech. Phys. Solids 57 (6)(2009) 891-908.

[44] Healy, B., et al., WARP3D-Release 17.0. 2011.

[45] T.J. Truster, DEIP, discontinuous element insertion program - mesh generation for interfacial finite element modeling, SoftwareX 7 (2018) 162-170.