# Seismic Wave Propagation in Composite Elastic Media

T. J. T. Spanos

Received: 29 January 2008 / Accepted: 1 July 2009 / Published online: 18 July 2009
© Springer Science+Business Media B.V. 2009

**Abstract** It has been known since the time of Biot–Gassman theory (Biot, J Acoust Soc Am 28:168–178, 1956, Gassmann, Naturf Ges Zurich 96:1–24, 1951) that additional seismic waves are predicted by a multicomponent theory. It is shown in this article that if the second or third phase is also an elastic medium then multiple p and s waves are predicted. Futhermore, since viscous dissipation no longer appears as an attenuation mechanism and the media are perfectly elastic, these waves propagate without attenuation. As well, these additional elastic waves contain information about the coupling of the elastic solids at the pore scale. Attempts to model such a medium as a single elastic solid causes this additional information to be misinterpreted. In the limit as the shear modulus of one of the solids tends to zero, it is shown that the equations of motion become identical to the equations of motion for a fluid filled porous medium when the viscosity of the fluid becomes zero. In this limit, an additional dilatational wave is predicted, which moves the fluid though the porous matrix much similar to a heart pumping blood through a body. This allows for a connection with studies which have been done on fluid-filled porous media (Spanos, 2002).

**Keywords** Seismic wave propagation · Composite elastic media ·
Porous medium · Ideal fluid

## List of Symbols

### Greek Symbols

$\alpha_A$
Thermal expansion coefficient for solid A
$\alpha_A^2$
Defined by Eq. A3 (square of the velocity of a P wave)
$\beta_A^2$
Defined by Eq. A4 (square of the velocity of an S wave)

---

T. J. T. Spanos (⊗)
Department of Physics, University of Alberta, Edmonton, AB, Canada
e-mail: tim@phys.ualberta.ca

T. J. T. Spanos
Wavefront Technology Solutions, Edmonton, AB, Canada

![](./images/811843326113218562_1.jpg)

| $\gamma$ | Surface coefficient of heat transfer between solid phases |
|----------|-----------------------------------------------------------|
| $\delta_A$ | Coefficients defined by the porosity Eq. 38 |
| $\delta_\eta$ | Coefficient of the hyperbolic term in the porosity Eq. 46 |
| $\delta_{ik}$ | Kronecker delta |
| $\zeta_A$ | Constant defined in Eq. 32 |
| $\eta_A$ | Volume fraction of space occupied by solid A |
| $\eta_A^o$ | Volume fraction of space occupied by solid A under static conditions |
| $\kappa_A$ | Heat conductivity of solid A |
| $\kappa_M^A$ | Defined by Eq. 34 |
| $\mu_A$ | Shear modulus of solid A |
| $\mu_M, \mu_M^A$ | Defined by Eq. 33 |
| $\rho_A$ | Mass density of solid A |
| $\rho_{AB}$ | Reduced mass of solid A due to interactions with solid B |
| $\sigma_{ik}^A$ | Stress tensor for solid A |
| $\phi$ | Velocity potential for dilatational motions |

### Latin Symbols

| $A_B$ | Surface area bounding solid B |
|-------|--------------------------------|
| $B^A$ | Body force acting on solid A |
| $B_o$ | Defined by Eq. 39 |
| $c_v^A$ | Heat capacity of solid A |
| $D_{ik}$ | Defined by Eq. A11 |
| $\Delta D$ | Defined by Eq. A5 |
| $I_i^A$ | Defined by Eq. 25 |
| $I_{ik}^A$ | Defined by Eq. 27 |
| $J^A$ | Defined by Eq. 30 |
| $K_A$ | Bulk Modulus of solid A |
| $K_M$ | Bulk modulus of the composite material |
| $P_{ik}$ | Defined by Eq. A10 |
| $\Delta P$ | Defined by Eq. A6 |
| $S_{ik}$ | Defined by Eq. A12 |
| $\Delta S$ | Defined by Eq. A7 |
| $T_A$ | Temperature of solid A |
| $\bar{T}_A$ | Average temperature of solid A |
| $T_o$ | Unperturbed ambient temperature |
| $\vec{u}$ | Velocities of the interfaces at the macroscale (pore scale) |
| $u_{ik}$ | Strain tensor |
| $\bar{u}_{ik}$ | Average of the strain tensor |
| $\vec{u}_A$ | Average displacement of solid A |
| $\vec{u}_s$ | Average displacement of solid |
| $\vec{u}_f$ | Average displacement of fluid |
| $V$ | Averaging volume |

## 1 Introduction

In fields such as global seismology (Dahlen and Tromp 1998) and exploration geophysics (Yilmaz 2000), elasticity theory is generally used as the physical model to which experimental

![](./images/811843326113218562_2.jpg)

observations are fit. Attenuation is artificially introduced by making the wave number complex. On the other hand, seismic wave propagation in fluid-filled elastic porous matrix addresses the interrelationship between the megascopic parameters and the basic physical quantities which describe the macroscopically segregated phases at the pore scale. As a result, attenuation is naturally introduced through the fluid viscosity. At the pore scale, macroscopic descriptions of the component phases result from molecular scale mixing. Thus, standard thermodynamics and thermo-mechanics of molecular scale mixtures describe the behaviour of the component phases. These phases are then mixed again at the pore scale, and such effects as differences in the bulk modulii and other parameters cause their volume fractions to change during compressional motions. The change in volume fractions during compression then requires an additional constraint on porosity to make the two energy potentials compatible. As a result, the megascopic dynamics and thermodynamics must include these additional degrees of freedom (de la Cruz et al. 1993). Furthermore, fluid motions are irreversible in dynamic processes, and non-equilibrium thermodynamics must be used. For perfect elastic media, however, equilibrium thermodynamics may be used since all the motions may be described by equilibrium thermodynamics. This allows for a detailed description of the interactions of the elastic phases and the associated megascopic processes. The actual construction may be done using arguments equivalent to those proposed by Biot for a single elastic matrix, separately, to the two individual matrixes. The two energy potentials now obtained require an additional constraint on the change in volume fraction during compressional motions to make them compatible. This description includes multiple seismic waves at the megascale, which depend on the structure of the medium at the macroscale (pore scale). In this article, this construction is done using volume averaging. For a porous medium filled with an ideal fluid, it is observed that irreversible fluid motions may occur introducing an additional physical process, a porosity wave, as is observed in an elastic medium filled with a viscous fluid (Spanos 2002). Examples of this type of wave in more complex systems include the pulse of fluid associated with a heart beat and porosity waves which carry fluids through porous media such as oil reservoirs. These waves have been observed in the lab (Davidson et al. 1999 Wang et al. 1998) and in the field (Dusseault et al. 2002), and have been applied to commercial processes associated with enhanced oil recovery (Dusseault et al. 2000), and environmental remediation (Gray et al. 2001). In the limit as the inertial terms in the fluid and solid equations of motion tend to zero, the associated equations predict a porosity–pressure diffusion process which describes pressure diffusion (Spanos 2002) which may easily be measured in the lab and is observed following the loading of dams (Geilikman et al. 1993). This article presents the simplest example of this wave as described, for an ideal fluid in an elastic matrix. It is assumed that no non-ideal fluids are present, the materials are mixed at the pore scale and the materials fully saturate the medium. The Einstein summation convention is used with respect to the indices i, j, k representing the coordinates x, y and z.

## 2 Two Elastic Solids

### 2.1 Pore Scale Equations

Inside the elastic solids, the pore scale equations of motion are given by

$$
\frac{\partial^{2}}{\partial t^{2}}\left[\rho_{A} u_{i}^{A}\right]=\frac{\partial}{\partial x_{k}} \sigma_{i k}^{A}+B_{i}^{A} \tag{1}
$$

where

![](./images/811843326113218562_3.jpg)

$$
\sigma_{i k}^{A}=-K_{A} \alpha_{A}\left(T_{A}-T_{o}\right) \delta_{i k}+K_{A} u_{j j}^{A} \delta_{i k}+2 \mu_{A}\left(u_{i k}^{A}-\frac{2}{3} \delta_{i k} \partial_{j} u_{j}^{A}\right)
\tag{2}
$$

are the elastic stress tensors for the solid. Here, A = 1, 2 distinguishes between the solid components and capital Latin letters are not summed over. $T_{o}$ is the ambient temperature and $T_{A}(\vec{x}, t)$ is the actual temperature in solid A. The temperature difference $T_{A}-T_{o}$ is treated as a first-order quantity; $\rho_{A}, \vec{u}^{A}, K_{A}, \mu_{A}$ and $\alpha_{A}$ are the mass density, displacement, bulk modulus, shear modulus and thermal expansion coefficient, respectively, for material A.

$$
u_{i k}^{A}=\frac{1}{2}\left(u_{i, k}^{A}+u_{k, i}^{A}\right)+\text { second order in } \vec{u}^{A}
\tag{3}
$$

$\vec{B}^{A}$ represents the body forces acting on the solid A by external forces such as gravity and will be assumed to be zero in the following discussion.

The linearized equation of heat transfer in each solid medium is Landau and Lifshitz (1975)

$$
\rho_{A} c_{v}^{A} \frac{\partial T_{A}}{\partial t}+\alpha_{A} K_{A} T_{A} \frac{\partial}{\partial t} \nabla \cdot \vec{u}^{A}-\kappa_{A} \nabla^{2} T_{A}=0
\tag{4}
$$

where $c_{v}^{A}$ is the heat capacity of solid A at constant volume and $\kappa_{A}$ is the thermal conductivity of solid A.

The equations of continuity are given by

$$
\frac{\partial \rho_{A}}{\partial t}+\nabla \cdot\left(\rho_{A} \vec{v}^{A}\right)=0
\tag{5}
$$

The mechanical boundary conditions between the two elastic solids are

$$
\vec{u}^{1}=\vec{u}^{2}
\tag{6}
$$

$$
\sigma_{i k}^{1} n_{k}=\sigma_{i k}^{2} n_{k}
\tag{7}
$$

And the boundary condition on temperature is

$$
\kappa_{1} \nabla T_{1}=\kappa_{2} \nabla T_{2}
\tag{8}
$$

### 2.2 The averging procedure used

The use of volume averaging procedure which converts the pore scale equations into megas-cale equations is described by a number of authors (Whitaker 1967; Slattery 1967; Anderson and Jackson 1967; Newman 1997). Here, one lets V be regions in the medium defined to be of identical shapes volumes and orientations and centred at points $\vec{x}$ of the medium. For example, if V were chosen to be spheres, it is simplest to assign each V to its centre $\vec{x}$.

Now, let $f_{B}(\vec{x})$ be a physical quantity associated with solid A, for example, its mass density. $f_{B}(\vec{x})$ is defined to be zero everywhere outside solid A. The volume average of $f_{B}$ over the volume V is defined as

$$
\left\langle f_{B}\right\rangle=\frac{1}{V} \int_{V} f_{B}(\vec{x}) d V
\tag{9}
$$

The quantity $\left\langle f_{B}\right\rangle$ regarded as a function of the centroids of V and is a smooth function provided V is large with respect to the scale at which the solids are mixed.

A related quantity $\bar{f}_{B}$ is defined as

$$
\bar{f}_{B}=\frac{1}{V_{B}} \int_{V} f_{B}(\vec{x}) d V
\tag{10}
$$

![](./images/811843326113218562_4.jpg)

Where $V_B$ is the volume of solid A in V. The fractional volume of solid B (porosity of solid A) is

$$
\eta_B = V_B / V \tag{11}
$$

Equation 10 may be rewritten as

$$
\bar{f}_B = \frac{1}{\eta_B} \langle f_B \rangle \tag{12}
$$

The averaging procedure is based on two averaging theorems which link the average of derivatives to the derivatives of averages:

$$
\int_V \partial_i f_B dV = \partial_i \int_V f_B dV + \int_{A_B} f_B n_i dA, \quad \text{i=x,y,z} \tag{13}
$$

$$
\int_V \partial_t f_B dV = \partial_t \int_V f_B dV - \int_{A_B} f_B \vec{u} \cdot \vec{n} dA \tag{14}
$$

Here, $A_B$ refers to all interfaces in V involving solid B. The convention is chosen such that $\vec{n}$ is directed outward from solid B. $\vec{u}$ are the velocities of the interfaces.

## 3 Construction of the Megascopic Equations

The megascopic continuum equations constructed here describe the deformations of a porous elastic matrix whose pores are completely filled with another elastic material. Furthermore, these deformations are assumed to occur at a scale of orders of magnitude larger than the scale at which elastic materials are mixed. The medium is also assumed to be megascopically homogeneous and isotropic. Thermomechanical coupling refers to the first-order heating of the phases from compression and the expansion/contraction of the phases due to heating and cooling.

The fractional volume change in the interior of each elastic solid during deformation, $\nabla \cdot \vec{u}^A$ may be written as

$$
\nabla \cdot \vec{u}^A = -\frac{(\rho_A - \rho_A^o)}{\rho_A^o} \tag{15}
$$

Taking the volume average of each side one obtains

$$
\eta_A^o \frac{(\overline{\rho}_A - \rho_A^o)}{\rho_A^o} = -\nabla \cdot \frac{1}{V} \int \vec{u}^A dV - \frac{1}{V} \int_{A_{AB}} \vec{u}^A \cdot d\vec{s} \tag{16}
$$

where B=1, 2 and B≠A

Here, $\vec{u}^A \cdot d\vec{s}$ is the volume swept out by the displacement $\vec{u}^A$ of the boundary surface element.

$$
\frac{1}{V} \int_{A_{AB}} \vec{u}^A \cdot d\vec{s} = -(\eta_A^o - \eta_A) \tag{17}
$$

Thus,

$$
\eta_A^o \frac{(\overline{\rho}_A - \rho_A^o)}{\rho_A^o} = -\eta_A^o \nabla \cdot \overline{\vec{u}}^A + (\eta_A^o - \eta_A) \tag{18}
$$

![](./images/811843326113218562_5.jpg)

Taking the volume average of the following pore scale equations defining bulk modulus for each solid (in the absence of Thermomechanical coupling)

$$
\frac{\left(\rho_{A}-\rho_{A}^{o}\right)}{\rho_{A}^{o}}=\frac{\left(p_{A}-p_{o}\right)}{K_{A}} \tag{19}
$$

one obtains

$$
\frac{\left(\bar{\rho}_{A}-\rho_{A}^{o}\right)}{\rho_{A}^{o}}=\frac{\left(\bar{p}_{A}-p_{o}\right)}{K_{A}} \tag{20}
$$

Combining the megascopic continuity equation for solid A with this equation one obtains

$$
\frac{1}{K_{A}}\left(\bar{p}_{A}-p_{o}\right)=-\nabla \cdot \overline{\bar{u}}^{A}+\frac{\left(\eta_{A}^{o}-\eta_{A}\right)}{\eta_{A}^{o}} \tag{21}
$$

If thermomechanical coupling is included, then Eq. 20 becomes

$$
\frac{\left(\rho_{A}-\rho_{A}^{o}\right)}{\rho_{A}^{o}}=\frac{\left(p_{A}-p_{o}\right)}{K_{A}}+\alpha_{A}\left(T_{A}-T_{o}\right) \tag{22}
$$

Taking the average of this equation yields

$$
\frac{1}{K_{A}}\left(\bar{p}_{A}-p_{o}\right)=-\nabla \cdot \overline{\bar{u}}^{A}+\frac{\left(\eta_{A}^{o}-\eta_{A}\right)}{\eta_{A}^{o}}+\alpha_{A}\left(T_{A}-T_{o}\right) \tag{23}
$$

The volume averages of the equations of motion yield:

$$
\begin{aligned}
\eta_{A}^{o} \rho_{A} \frac{\partial^{2} \overline{\bar{u}}_{i}^{A}}{\partial t^{2}} &=\eta_{A}^{o} K_{A} \partial_{i}\left(\nabla \cdot \overline{\bar{u}}^{A}\right)+K_{A} \nabla \eta_{A} \\
&+\eta_{A}^{o} \mu_{A}\left[\nabla^{2} \overline{\bar{u}}_{i}^{A}+1 / 3 \partial_{i}\left(\nabla \cdot \overline{\bar{u}}^{A}\right)\right] \\
&-\eta_{A}^{o} K_{A} \alpha_{A} \partial_{i} \bar{T}_{A}-I_{i}^{(A)}+\mu_{A} \partial_{k} I_{i k}^{(A)}
\end{aligned} \tag{24}
$$

The integrals (denoted by I’s) over the solid–solid interface in the above equations represent the coupling between the constituents and representative expressions in terms of megascopic observables, which may be uniquely obtained through physical arguments. These expressions introduce the majority of the megascopic parameters in the theory, except for porosity. These area integrals are not all independent but are related due to the pore scale boundary conditions. The area integrals given by

$$
I_{i}^{(A)}=-\frac{1}{V} \int_{A_{A B}}\left[\sigma_{i k}^{A}+p_{o} \delta_{i k}\right] n_{k} d A \tag{25}
$$

are related, due to continuity of stress at the pore scale interface (Newton’s third law), by

$$
I_{i}^{(1)}=-I_{i}^{(2)} \tag{26}
$$

The area integrals given by

$$
I_{i k}^{(A)}=\frac{1}{V} \int_{A_{A B}}\left(u_{k}^{A} n_{i}+u_{i}^{A} n_{k}-\frac{2}{3} u_{j}^{A} n_{j} \delta_{i k}\right) d A \tag{27}
$$

are related by

$$
I_{i k}^{(1)}=-I_{i k}^{(2)} \tag{28}
$$

![](./images/811843326113218562_6.jpg)

Taking the volume average of the heat equations one obtains

$$
\begin{aligned}
\eta_{A}^{o} \rho_{A} c_{v}^{A} \frac{\partial \bar{T}_{A}}{\partial t} & +T_{o} K_{A} \alpha_{A}\left[\frac{\partial \eta_{A}}{\partial t}+\eta_{A}^{o} \frac{\partial}{\partial t} \nabla \cdot \vec{u}^{A}\right] \\
& -\eta_{A}^{o} \kappa_{A} \nabla^{2} \bar{T}_{A}-\kappa_{A} \nabla \cdot \vec{J}^{(A)}-J^{(A)}=0
\end{aligned}
\tag{29}
$$

where

$$
\vec{J}^{(A)}=\frac{1}{V} \int_{A_{A B}}\left(T_{A}-T_{o}\right) d \vec{A}
\tag{30}
$$

and

$$
\vec{J}^{(1)}=-\vec{J}^{(2)}
\tag{31}
$$

due to continuity of temperatures of the two components on the interface. The two area integrals

$$
J^{(A)}=\frac{1}{V} \int_{A_{A B}} \kappa_{A} \nabla T_{A} \cdot d \vec{A}
\tag{32}
$$

are related by

$$
J^{(1)}=-J^{(2)}
\tag{33}
$$

due to continuity of heat flux.

The integral $I_{i k}^{(A)}$ is the force (per unit volume) exerted on one elastic solid by the other elastic solid across the interface due to compressional or shear motion. From the point of view of the megascopic continuum equations, it is a body force. An additional term, proportional to the relative acceleration may also be presented (Landau and Lifshitz 1975; Johnson 1980; Berryman 1980; de la Cruz and Spanos 1989) $\rho_{12} \frac{\partial^{2}}{\partial t^{2}}\left(\vec{u}^{1}-\vec{u}^{2}\right)$. Now, note that the equations in their current form do not satisfy the principle of equivalence. In the presence of gravity there will be an induced buoyancy force acting on one solid by the other, say $-\rho_{b} g_{i}$. How- ever, a uniformly accelerating frame can simulate gravity. Since relative acceleration is an invariant, another linear combination of accelerations is needed. When gravity is included, this additional term is of the form $\rho_{b}\left(\frac{\partial^{2} u_{i}^{m}}{\partial t^{2}}-g_{i}\right)$ where $\frac{\partial^{2} u_{i}^{m}}{\partial t^{2}}$ is the acceleration of the megascopic medium.

$$
\frac{\partial^{2} u_{i}^{m}}{\partial t^{2}}=\frac{\eta_{1}^{o} \rho_{o}^{1}}{\rho_{o}^{m}} \frac{\partial^{2} \bar{u}_{i}^{1}}{\partial t^{2}}+\frac{\eta_{1}^{o} \rho_{o}^{2}}{\rho_{o}^{m}} \frac{\partial^{2} \bar{u}_{i}^{2}}{\partial t^{2}}
\tag{34}
$$

and $\rho_{o}^{m}=\eta_{1}^{o} \rho_{o}^{1}+\eta_{1}^{o} \rho_{o}^{2}$ is the mass density of the megascopic medium. When gravity is switched off, this term has the form $\rho_{b} \frac{\partial^{2} u_{i}^{m}}{\partial t^{2}}$.

The area integral $I_{i k}^{(A)}$ may be expressed in megascopic form in the above case as follows:
According to Eq. $24, \mu_{A} I_{i k}^{(A)}$ is the piece needed to fully determine the megascopic solid stress tensor (which will be denoted by $\bar{\sigma}_{i j}^{A}$ ). It can be shown quite generally (de la Cruz et al. 1993; Spanos 2002) that the dependence of $\bar{\sigma}_{i j}^{A}$ on deformation $\bar{u}_{i j}^{A}$ and that $\eta_{A}-\eta_{A}^{o}$ occurs only through the combination

$$
\bar{u}_{i j}^{A^{\prime}}=\bar{u}_{i j}^{A}+\frac{1}{3} \delta_{i j}\left(\eta_{A}-\eta_{A}^{o}\right) / \eta_{A}^{o}
\tag{35}
$$

![](./images/811843326113218562_7.jpg)

where

$$
\bar{u}_{i j}^{A}=\frac{1}{2}\left(\partial_{i} \bar{u}_{j}^{A}+\partial_{j} \bar{u}_{i}^{A}\right)
\tag{36}
$$

Here, the symmetric tensor $I_{i k}^{(A)}$ has the general form:

$$
I_{i k}^{(A)}=\varsigma_{A} \eta_{A}^{o}\left[\partial_{k} \bar{u}_{i}^{A}+\partial_{i} \bar{u}_{k}^{A}-\frac{2}{3} \delta_{i k} \partial_{j} \bar{u}_{j}^{A}\right]+\varsigma_{A}^{\prime} \delta_{i k} \bar{u}_{j j}^{A}+\varsigma_{A}^{\prime \prime} \delta_{i k}\left(\eta_{A}-\eta_{A}^{o}\right)
\tag{37}
$$

where $\varsigma_{A}, \varsigma_{A}^{\prime}$ and $\varsigma_{A}^{\prime \prime}$ are constants. However, since $I_{i k}^{(A)}$ is trace free $\varsigma_{A}^{\prime}, \varsigma_{A}^{\prime \prime}=0$, and thus

$$
I_{i k}^{(A)}=\varsigma_{A} \eta_{A}^{o}\left[\partial_{k} \bar{u}_{i}^{A}+\partial_{i} \bar{u}_{k}^{A}-\frac{2}{3} \delta_{i k} \partial_{j} \bar{u}_{j}^{A}\right]
\tag{38}
$$

The dimensionless constant $\varsigma_{A}$ may be conveniently eliminated in favour of a megascopic shear modulus $\mu_{M}$ (Hickey et al. 1995) through the definition

$$
\mu_{M}=\eta_{1}^{o} \mu_{1}\left(1+\varsigma_{1}\right)+\eta_{2}^{o} \mu_{2}\left(1+\varsigma_{2}\right)
\tag{39}
$$

Thus, the physical meaning of the $\varsigma_{A}$ is observed to be a measure of the difference between $\mu_{M}$ and the simple averaged value of $\eta_{1}^{o} \mu_{1}+\eta_{2}^{o} \mu_{2}$.

Thus, $\eta_{A}^{o} \mu_{A}$ may be replaced by $\mu_{M}^{A}=\eta_{A}^{o} \mu_{A}\left(1+\varsigma_{A}\right)$ in Eq. 24 representing the contribution of solid A to the megascopic shear modulus.

At the same time, each elastic solid acquires a new term involving space derivatives of the other solids velocity. This new term

$$
-\eta_{B}^{o} \mu_{A}\left(\frac{\mu_{M}^{A}}{\eta_{B}^{o} \mu_{B}}-1\right) \frac{\partial}{\partial x_{k}}\left[\partial_{i} \bar{u}_{k}^{B}+\partial_{k} \bar{u}_{i}^{B}-\frac{2}{3} \delta_{i k} \partial_{j} \bar{u}_{j}^{B}\right]
$$

arises from Eq. 38 and fails to vanish unless $\varsigma_{B}=0$.

In analogy with the generalization of the shear modulus, the megascopic heat conductivities can be introduced as phenomenological parameters and are related to component heat conductivities $\kappa_{A}$ according to

$$
\kappa_{M}^{A}=\eta_{A}^{o} \kappa_{A}\left(1+b_{A}\right)
\tag{40}
$$

where the dimensionless constants $b_{A}$ reflect the pore scale behaviour through the assumed relation

$$
\vec{J}^{(A)}=\frac{1}{V} \int_{A_{A B}}\left(T_{A}-T_{o}\right) d \vec{A}=\eta_{A}^{o} c_{A} \nabla \bar{T}_{A}-\eta_{B}^{o} c_{B} \nabla \bar{T}_{B}
\tag{41}
$$

Thus, one obtains additional megascopic terms in the averaged heat Eqs. 29

The two integrals $J^{(A)}$ are equal and opposite, and represent the heat transfer from one component to the other across the macroscopic interfaces. Hence, solid A acts as an additional heat source for solid B and vice versa. These heat exchange terms between components should vanish if and only if the megascopic component temperatures are equal $(\bar{T}_{A}=\bar{T}_{B})$. These terms may be represented by a first-order scalar proportional to $(\bar{T}_{A}-\bar{T}_{B},)$, and therefore, yield

$$
J^{(A)}=\frac{1}{V} \int_{A_{A B}} \kappa_{A} \nabla T_{A} \cdot d \vec{A}=\gamma\left(\bar{T}_{A}-\bar{T}_{B}\right)
\tag{42}
$$

![](./images/811843326113218562_8.jpg)

where $\gamma$ is the surface coefficient of heat transfer between the solid phases, a positive empirical parameter. This parameter may be estimated by

$$
\gamma=O|\kappa A /(V L)| \tag{43}
$$

where $\kappa$ is the effective conductivity between the solids, $A$ is the interfacial surface area between the solids within the averaging volume $V$, and $L$ is the characteristic pore scale length.

Counting the number of variables and equations, one observes that an additional equation is needed for completeness when dilatational motions are considered. At this point, note that Newton's second law has not been completely specified. When the medium is compressed, the two solids may be compressed or deformed, each having its own bulk modulus and shear modulus thus changing the porosity. Thus, the relationship between $\nabla \vec{u}_{A}, \nabla \vec{u}_{B}$ and $\eta_{A}-\eta_{A}^{o}$ must be specified to completely describe a compression. Thus, one obtains the relationship (assuming that locally the phases remain in thermal equilibrium)

$$
\eta_{A}-\eta_{A}^{o}=\delta_{A} \nabla \cdot \vec{u}_{A}-\delta_{B} \nabla \cdot \vec{u}_{B} \tag{44}
$$

where $\delta_{A}$ and $\delta_{B}$ are dimensionless parameters. A basic physical understanding of this relationship for a fluid and a solid has been presented in the context of dilatational experiments (Hickey et al. 1995). In the above case, it is possible to obtain this equation through the following arguments. The volume fraction of phase A may be changed by altering the mega-scopic compressive stresses on the component phases or by altering the other forces such as body forces. Thus,

$$
\eta_{A}-\eta_{A}^{o}=a \bar{\sigma}_{j j}^{A}+b \bar{\sigma}_{j j}^{B}+B_{o} \tag{45}
$$

where $B_{o}$ represents the contribution from forces other than the stresses. For phenomena such as seismic wave propagation, these forces may be set to zero. According to Eq. 18 for $\bar{\sigma}_{j k}^{A}$, one obtains

$$
\bar{\sigma}_{j j}^{A}=3 K_{A}\left[\bar{u}_{j j}^{A}+\frac{\eta_{A}-\eta_{A}^{o}}{\eta_{A}^{o}}\right] \tag{46}
$$

Thus one obtains

$$
\left[1+\frac{3 a K_{A}}{\eta_{A}^{o}}-\frac{3 b K_{B}}{\eta_{B}^{o}}\right]\left(\eta_{A}-\eta_{A}^{o}\right)=3 a K_{A} \bar{u}_{j j}^{A}-3 b K_{B} \bar{u}_{j j}^{B} \tag{47}
$$

This yields the porosity Eq. 44 which is independent of the equations of motion for the solids. Note that if the two phases are not purely elastic then Eq. 44 must be replaced by its time derivative, plus an additional term must be included which makes the above equation hyperbolic (c.f. Eq. 52).

Summary of the equations for a homogeneous medium (neglecting thermomechanical coupling)

Equations of Motion (for the elastic phases)

$$
\begin{aligned}
\rho_{A} \frac{\partial^{2}}{\partial t^{2}} \vec{u}_{A}= & K_{A} \nabla\left(\nabla \cdot \vec{u}_{A}\right)-\frac{K_{A}}{\eta_{A}^{o}} \nabla \eta_{A} \\
& +\frac{\eta_{B}^{o}}{\eta_{A}^{o}} \mu_{A}\left(\frac{\mu_{M}^{B}}{\eta_{B}^{o} \mu_{B}}-1\right)\left[\nabla^{2} \frac{\partial \vec{u}_{B}}{\partial t}+1 / 3 \nabla\left(\nabla \cdot \frac{\partial \vec{u}_{B}}{\partial t}\right)\right] \\
& +(-1)^{A} \frac{\rho_{12}}{\eta_{A}^{o}} \frac{\partial^{2}}{\partial t^{2}}\left(\vec{u}_{A}-\vec{u}_{B}\right)+\frac{\mu_{M}^{A}}{\eta_{A}^{o}}\left[\nabla^{2} \vec{u}_{A}+1 / 3 \nabla\left(\nabla \cdot \vec{u}_{A}\right)\right]
\end{aligned} \tag{48}
$$

![](./images/811843326113218562_9.jpg)

### Equation of Motion (for porosity)
$$
\eta_{A}-\eta_{A}^{o}=\delta_{A} \nabla \cdot \vec{u}_{A}-\delta_{B} \nabla \cdot \vec{u}_{B}
\tag{49}
$$

### Equations of continuity
$$
\frac{\rho_{A}-\rho_{A}^{o}}{\rho_{A}^{o}}+\frac{\eta_{A}-\eta_{A}^{o}}{\eta_{A}^{o}}+\nabla \cdot \vec{u}_{A}=0
\tag{50}
$$

### Pressure Equations
$$
\frac{1}{K_{A}} p_{A}=-\nabla \cdot \vec{u}_{A}-\frac{\eta_{A}-\eta_{A}^{o}}{\eta_{A}^{o}}
\tag{51}
$$

Aside from the (unperturbed) porosity five other megascopic empirical parameters $(\rho_{12}, \mu_{M}^{A}$, and $\delta_{A})$ appear in these equations. On the other hand, the parameters $K_{A}, \rho_{A}^{o}$ etc. are the pore scale physical parameters specifying the constituents. If thermomechanical coupling is not ignored then Eqs. 48 and 51 are replaced by (24) and (23) and the heat Eq.29 must be included. Now, note that if the shear modulus of one of the solids is set to zero in Eq.48, then one obtains the equations of motion for an ideal fluid in an elastic porous medium. This identical result may be obtained by setting the shear and bulk viscosity of the fluid equation for a fluid filled porous medium to zero. These equations are given by Eqs. 2.81 and 2.82 in Spanos (2002). When these two limits are taken, it is observed that the equations of motion become identical once the time derivative of Eq.49 is considered and the hyperbolic term is included to account for fluid flow as explained above. Here, for a dynamic process involving flow, the concept of an elastic displacement must be replaced by a fluid velocity as given in Eq.52.

$$
\delta_{\eta} \frac{\partial^{2} \eta_{A}}{\partial t^{2}}+\frac{\partial \eta_{A}}{\partial t}=\delta_{A} \nabla \cdot \frac{\partial \vec{u}_{A}}{\partial t}-\delta_{B} \nabla \cdot \frac{\partial \vec{u}_{B}}{\partial t}
\tag{52}
$$

## 3.1 Wave Propagation
A Helmholtz decomposition yields two p waves and two s waves as shown in the appendix (Spanos 2002) representing the in phase and out of phase motions of the component elastic solids. Here, $\alpha_{1}$ and $\alpha_{2}$ are the speeds of the first and second $p$ waves, respectively, and $\beta_{1}$ and $\beta_{2}$ are the speeds of the first and second $s$ waves, respectively. Contrary to the case of a fluid-filled porous medium where the out of phase motions are highly attenuated, for the case of two elastic solids, the second $p$ wave propagates without attenuation. Of course, in a real medium, friction would introduce some attenuation; however, that would also require the present assumption of equilibrium thermodynamics to be relaxed. As a numerical example, consider a mixture of two elastic solids $(\rho_{1}=2650 \mathrm{kg} / \mathrm{m}^{3}, \mu_{M}^{(1)}=2.0 x 10^{10} \mathrm{Pa}, \mu_{s}^{(1)}=$ $2.3 x 10^{10} \mathrm{Pa}, K_{1}=3.3 x 10^{10} \mathrm{Pa}, \rho_{2}=3400 \mathrm{kg} / \mathrm{m}^{3} \quad \mu_{M}^{(2)}=3.1 x 10^{10} \mathrm{Pa}, \mu_{s}^{(2)}=3.8 x 10^{10} \mathrm{Pa}$, $K_{2}=5.2 x 10^{10} \mathrm{Pa}, K_{M}=3.25 x 10^{10}, \rho_{12}=-.86 \mathrm{kg} / \mathrm{m}^{3}$). For such a mixture the bulk modulus of the megascopic material depends on the microscopic structure. A straightforward calculation (c.f. Hickey et al. 1995) allows one to calculate the parameters in Eq.49 from the megascopic bulk modulus.

$$
\delta_{A}=\frac{K_{A}\left[\left(\eta_{A} K_{A}+\eta_{B} K_{B}\right)-K_{M}\right]}{\left(K_{A}-K_{B}\right)^{2}}
\tag{53}
$$

Note this equation tells us that the bulk modulus of the composite material $K_{M}$ must always be less than the weighted average $(\eta_{A} K_{A}+\eta_{B} K_{B})$ which of course is due to the effect of

![](./images/811843326113218562_10.jpg)

the shear modulii. The only way the two can be equal is if the shear modulii are both infinite or the properties of the two solids become identical. A representative calculation of the wave speeds using mathematica yields (a first $p$ wave propagating at 5.94 km/s, a second $p$ wave propagating at 4.36 km/s, a first s wave at 4.92 km/s and a second s wave at 3.28 km/s). Once attenuation is allowed, the analysis requires additional concepts from non-equilibrium thermodynamics to be used, which places very strong constraints on the motions of the component materials; however, this information is outside the scope of this article.

As a second example, consider a porous medium composed of liquid helium in a glass matrix. In this case Eq. 53 must be used as the porosity equation in place of Eq. 49. Previously, Eq. 49 was a special case of Eq. 53 only valid for two perfectly elastic media. Here, the time derivatives occur in the porosity equation because of the irreversible fluid motions (i.e. the fluid motions have no memory). The solid and fluid equations of motion become

$$
\begin{aligned}
\rho_{s} \frac{\partial^{2}}{\partial t^{2}} \vec{u}_{s}=K_{s} & \nabla\left(\nabla \cdot \vec{u}_{s}\right)-\frac{K_{s}}{\eta_{s}^{o}} \nabla \eta_{s}-\frac{\rho_{12}}{\eta_{s}^{o}} \frac{\partial^{2}}{\partial t^{2}}\left(\vec{u}_{f}-\vec{u}_{s}\right) \\
& +\frac{\mu_{M}}{\eta_{s}^{o}}\left[\nabla^{2} \vec{u}_{s}+1 / 3 \nabla\left(\nabla \cdot \vec{u}_{s}\right)\right]
\end{aligned}
$$

$$
\rho_{f} \frac{\partial^{2}}{\partial t^{2}} \vec{u}_{f}=K_{f} \nabla\left(\nabla \cdot \vec{u}_{f}\right)-\frac{K_{f}}{\eta_{f}^{o}} \nabla \eta_{f}+\frac{\rho_{12}}{\eta_{f}^{o}} \frac{\partial^{2}}{\partial t^{2}}\left(\vec{u}_{f}-\vec{u}_{s}\right)
$$

which may be obtained by setting the shear modulus of one of the solids equal to zero in Eq. 48 or by setting the fluid viscosity equal to zero in Eqs. 2.81 and 2.82 in Spanos (2002). As in the previous analysis, one obtains two $p$ waves; however, the fluid motions may also couple to the porosity pressure variations resulting in a porosity wave which carries fluid through the porous medium similar to the pulsing of a heart. (c.f. Chap. 8, Spanos 2002). Assume the properties of glass for the matrix and of liquid helium for the fluid $(\rho_{s}=2650 kg / m^{3}, \mu_{s}=2.0 ×10^{9} Pa$ , $K_{s}=3.3 ×10^{10} Pa, \rho_{f}=150 kg / m^{3}, \mu_{f}=0 Pa, K_{f}=5.0 ×10^{7} Pa, K_{M}=2.65 ×10^{10}$ (for seismic waves $K_{M}$ is not onkyclose to the undrained bulk modulus but also must account for local flow which occurs as a part of the seismic wave), $\rho_{12}=-.86 kg / m^{3}$ ). Here, the volume fractions of the fluid and solid, $\eta_{f}+\eta_{s}=1$ and may be eliminated from Eqs. 54 and55 using Eq.52. A representative calculation of the wave speeds using mathematica yields a first $p$ wave propagating at 3.35 km/s, a second $p$ wave propagating at 0.55 km/s, one s wave propagating at 1.26 km/s and a porosity wave (the incompressible limit of fluid motions coupled to elastic deformations of the matrix, for this process $K_{M}=2.15 ×10^{10}$ , is not only close to the drained bulk modulus but also must account for the fluid motions during deformation) propagating at 2.92 km/s.

## 4 Three Elastic Solids
Using an identical construction to the case of two elastic solids, the equations of motion are given by

Equations of motion (for the elastic phases)
$$
\begin{aligned}
\rho_{A} \frac{\partial^{2}}{\partial t^{2}} \vec{u}_{A}=K_{A} & \nabla\left(\nabla \cdot \vec{u}_{A}\right)-\frac{K_{A}}{\eta_{A}^{o}} \nabla \eta_{A} \\
& +\frac{\eta_{B}^{o}}{\eta_{A}^{o}} \mu_{A}\left(\frac{\mu_{M}^{B}}{\eta_{B}^{o} \mu_{B}}-1\right)\left[\nabla^{2} \frac{\partial \vec{u}_{B}}{\partial t}+1 / 3 \nabla\left(\nabla \cdot \frac{\partial \vec{u}_{B}}{\partial t}\right)\right]
\end{aligned}
$$

![](./images/811843326113218562_11.jpg)

$$
\begin{aligned}
& +\frac{\eta_{C}^{o}}{\eta_{A}^{o}} \mu_{A}\left(\frac{\mu_{M}^{B}}{\eta_{C}^{o} \mu_{C}}-1\right)\left[\nabla^{2} \frac{\partial \vec{u}_{C}}{\partial t}+1 / 3 \nabla\left(\nabla \cdot \frac{\partial \vec{u}_{C}}{\partial t}\right)\right] \\
& -\frac{\rho_{A B}}{\eta_{A}^{o}} \frac{\partial^{2}}{\partial t^{2}}\left(\vec{u}_{A}-\vec{u}_{B}\right)-\frac{\rho_{A C}}{\eta_{A}^{o}} \frac{\partial^{2}}{\partial t^{2}}\left(\vec{u}_{A}-\vec{u}_{C}\right) \\
& +\frac{\mu_{M}^{A}}{\eta_{A}^{o}}\left[\nabla^{2} \vec{u}_{A}+1 / 3 \nabla\left(\nabla \cdot \vec{u}_{A}\right)\right]
\end{aligned}
\tag{56}
$$

Here, A,B,C=1,2,3 where A≠B, A≠C, B≠C and $\rho_{A B}=-\rho_{B A}$
    Equation of Motion (for porosity)

$$
\eta_{A}-\eta_{A}^{o}=\delta_{A}^{(A)} \nabla \cdot \vec{u}_{A}-\delta_{B}^{(A)} \nabla \cdot \vec{u}_{B}-\delta_{C}^{(A)} \nabla \cdot \vec{u}_{C}
\tag{57}
$$

Here any two porosity equations may be taken as independent, and the third may be derived from the other two.

The equations of continuity and pressure are unchanged.

The Helmholtz decomposition now yields four P waves and four S waves. For each case, the first wave propagates with all components moving in phase and for the subsequent three, one component moves out of phase with the other two.

### 4.1 Conclusions

As an illustration, an idealized case of a composite elastic solid composed of elastic components mixed at the pore scale is considered. It is observed, that for seismic waves at a scale orders of magnitude larger than the pore scale, the use of a single elastic continuum is not a good approximation. Details of the nature of the interaction of the components at the pore scale appear in the megascopic equations for the multicomponent description which arises from volume averaging. Additional waves are observed that do not appear in a single elastic continuum model. For a real composite elastic material, the wave speeds may be calculated exactly after the physical parameters describing the material have been measured. In the limit as the shear modulus of one of the fluids tends to zero, one obtains the same description of seismic wave propagation as is obtained for a fluid-filled porous medium when the fluid viscosity tends to zero. This analysis illustrates that the study which has been done on seismic wave propagation in fluid-filled porous media may be applied to composite elastic media. Furthermore, multiple waves propagate through such media which would be misinterpreted as dispersion if an effective elastic model is used. Thus, information from the intermediate scale would be lost. Attenuation may be introduced either by introducing a small amount of viscous liquid at the pore scale or allowing frictional motions of the matrix. Both of these generalizations would require that additional subtleties associated with non-equilibrium thermodynamics be incorporated into the theory.

## Appendix

### Helmholtz Decomposition

Assuming seismic wave propagation, the equations (48), (49) and (50) may be written in the form (cf. Spanos 2002)

![](./images/811843326113218562_12.jpg)

$$
\left(\nabla^{2}+\frac{\omega^{2}}{\alpha_{A}^{2}}\right) \phi_{A}^{\prime \prime}=0
\tag{A1}
$$

$$
\left(\nabla^{2}+\frac{\omega^{2}}{\beta_{A}^{2}}\right) \psi_{A}^{\prime \prime}=0
\tag{A2}
$$

where

$$
\alpha_{1}^{2}, \alpha_{2}^{2}=\frac{1}{2 \Delta D}\left[\operatorname{Tr}\left(P^{\dagger} D\right) \pm \sqrt{\operatorname{Tr}^{2}\left(P^{\dagger} D\right)-4 \Delta P \Delta D}\right]
\tag{A3}
$$

$$
\beta_{1}^{2}, \beta_{2}^{2}=\frac{1}{2 \Delta D}\left[\operatorname{Tr}\left(S^{\dagger} D\right) \pm \sqrt{\operatorname{Tr}^{2}\left(S^{\dagger} D\right)-4 \Delta S \Delta D}\right]
\tag{A4}
$$

and

$$
\Delta D=D_{11} D_{22}-D_{12} D_{21}
\tag{A5}
$$

$$
\Delta P=P_{11} P_{22}-P_{12} P_{21}
\tag{A6}
$$

$$
\Delta S=S_{11} S_{22}-S_{12} S_{21}
\tag{A7}
$$

$$
\operatorname{Tr}\left(P^{\dagger} D\right)=D_{11} P_{22}+D_{22} P_{11}-D_{21} P_{12}-D_{12} P_{21}
\tag{A8}
$$

$$
\operatorname{Tr}\left(S^{\dagger} D\right)=D_{11} S_{22}+D_{22} S_{11}-D_{21} S_{12}-D_{12} S_{21}
\tag{A9}
$$

$$
\begin{gathered}
P_{11}=\eta_{1}^{o} K_{1}\left(1-\frac{\delta_{1}}{\eta_{1}^{o}}\right)+\frac{4}{3} \mu_{M}^{1} \quad P_{12}=K_{1} \delta_{2} \\
P_{22}=\eta_{2}^{o} K_{2}\left(1-\frac{\delta_{2}}{\eta_{2}^{o}}\right)+\frac{4}{3} \mu_{M}^{2} \quad P_{21}=K_{2} \delta_{1}
\end{gathered}
\tag{A10}
$$

$$
\begin{gathered}
D_{11}=\eta_{1}^{o} \rho_{1}^{o}-\rho_{12} \quad D_{12}=\rho_{12} \\
D_{22}=\eta_{2}^{o} \rho_{2}^{o}-\rho_{12} \quad D_{21}=\rho_{12}
\end{gathered}
\tag{A11}
$$

$$
\begin{gathered}
S_{11}=\mu_{M}^{1} \quad S_{12}=\eta_{2}^{o} \mu_{1}\left(\frac{\mu_{M}^{2}}{\eta_{2}^{o} \mu_{2}}-1\right) \\
S_{22}=\mu_{M}^{2} \quad S_{21}=\eta_{1}^{o} \mu_{2}\left(\frac{\mu_{M}^{1}}{\eta_{1}^{o} \mu_{1}}-1\right)
\end{gathered}
\tag{A12}
$$

## References

Anderson, T.B., Jackson, R.: Fluid mechanical description of fluidized beds equations of motion. Ind. Eng. Chem. Fundam. 6, 527–539 (1967)

Berryman, J.G.: Confirmation of Biot’s theory. Appl. Phys. Lett. 37(4), 382–384 (1980)

Biot, M.A.: Theory of propagation of elastic waves in a fluid saturated porous solid, 1, Low frequency range. J. Acoust. Soc. Am. 28, 168–178 (1956). doi:10.1121/1.1908239

Dahlen F.A., Tromp J. (1998) Theoretical Global Seismology. Princeton University Press, Princeton, NJ

Davidson, B., Spanos, T.J.T., Dusseault, M.B.: Laboratory experiments on pressure pulse flow enhancement in porous media. In: Proceedings of the CIM Regina Technical Meeting (Oct 1999)

de la Cruz, V., Sahay, P.N., Spanos, T.J.T.: Thermodynamics of porous media. Proc. Soc. R. Lond. A. 443, 247–255 (1993)

de la Cruz, V., Spanos, T.J.T.: Thermomechanical coupling during seismic wave propagation in a porous medium. J. Geophys. Res. 94, 637–642 (1989)

Dusseault, M.B., Davidson, B., Spanos, T.J.T.: Pressure pulsing: the ups and downs of starting a new technology. J. Can. Petrol. Technol. 39(4), 13–17 (2000)

Dusseault, M.B., Shand, D., Meling, T., Spanos, T.J.T., Davidson, B.C.: Field applications of pressure pulsing in porous media, pp.639–645. In: Proceedings of Second Biot Conference on Poromechanics, Grenoble France Balkema, Rotterdam, 2002

![](./images/811843326113218562_13.jpg)

Gassmann, F.: Uber die elastizitat poroser medien, Vierteljahresschrift d. Naturf. Ges. Zurich 96, 1–24 (1951)

Geilikman, M. A., Spanos, T. J.T., Nyland, E.: Porosity diffusion in fluid saturated media. Tectonphysics 217, 111–115 (1993)

Gray, P., Davidson, B., MacDonald, A.: Dramatic LNAPL recovery at an Ontario manufacturing facility. Environ. Sci. Eng. (January) 22–24 (2001)

Hickey, C.J., Spanos, T.J.T., de la Cruz, V.: Deformation parameters of permeable media. Geophys. J. Int. 121, 359–376 (1995)

Johnson, D.L.: Equivalence between fourth sound on helium at low temperatures and the Biot slow wave in consolidated porous media. Appl. Phys. Lett. 37(12), 1065–1067 (1980)

Landau L.D., Lifshitz E.M. (1975) Fluid Mechanics. Pergamon, Toronto

Newman, S.P.: Theoretical derivation of Darcy’s Law. Acta. Mech. 25, 153–170 (1997)

Slattery, J.C.: Flow of Viscoelastic fluids through porous media. AIChE. J. 13, 1066–1071 (1967)

Spanos, T.J.T.: The Thermophysics of Porous Media, Monographs and Surveys in Pure and Applied Mathe- matics, Chapman and Hall/CRC Press, Boca Raton (2002)

Wang, J., Dusseault, M.B., Davidson B., Spanos, T.J.T.: Fluid enhancement under liquid pressuire pulsing at low frequency. In: Proceedings UNITAR Conference on Heavy Oil and Tar Sands, p. 7, Beijing, PRC, 1998

Whitaker, S.: Diffusion and dispersion in porous media. AIChE. J. 13, 420–427 (1967)

Yilmaz, O.: Seismic data processing: Investigations in Geophysics, vol 2. Soc. Explor. Geophys. (2000)

![](./images/811843326113218562_14.jpg)