# A novel homogenization method for phase field approaches based on partial rank-one relaxation

J. Mosler $^{a,b,*}$, O. Shchyglo $^{c}$, H. Montazer Hojjat $^{a}$

$^{a}$ TU Dortmund, Institute of Mechanics, Leonhard-Euler-Str. 5, D-44227 Dortmund, Germany
$^{b}$ Helmholtz-Zentrum Geesthacht, Institute of Materials Research, Materials Mechanics, D-21502 Geesthacht, Germany
$^{c}$ Interdisciplinary Centre for Advanced Materials Simulation (ICAMS), Ruhr-Universität Bochum, Universitätsstr. 90a, D-44789 Bochum, Germany

---

## ARTICLE INFO

**Article history:**
Received 5 December 2013
Received in revised form
24 March 2014
Accepted 6 April 2014
Available online 13 April 2014

**Keywords:**
Thermodynamics
Variational principles
Energy minimization
Finite strain
Homogenization

---

## ABSTRACT

This paper deals with the analysis of homogenization assumptions within phase field theories in a finite strain setting. Such homogenization assumptions define the average bulk's energy within the diffusive interface region where more than one phase co-exist. From a physical point of view, a correct computation of these energies is essential, since they define the driving force of material interfaces between different phases. The three homogenization assumptions considered in this paper are: (a) Voigt/Taylor model, (b) Reuss/Sachs model, and (c) Khachaturyan model. It is shown that these assumptions indeed share some similarities and sometimes lead to the same results. However, they are not equivalent. Only two of them allow the computation of the individual energies of the co-existing phases even within the aforementioned diffusive interface region: the Voigt/ Taylor and the Reuss/Sachs model. Such a localization of the averaged energy is important in order to determine and to subsequently interpret the driving force at the interface. Since the Voigt/Taylor and the Reuss/Sachs model are known to be relatively restrictive in terms of kinematics (Voigt/Taylor) and linear momentum (Reuss/Sachs), a novel homo- genization approach is advocated. Within a variational setting based on (incremental) energy minimization, the results predicted by the novel approach are bounded by those corresponding to the Voigt/Taylor and the Reuss/Sachs model. The new approach fulfills equilibrium at material interfaces (continuity of the stress vector) and it is kinematically compatible. In sharp contrast to existing approaches, it naturally defines the mismatch energy at incoherent material interfaces. From a mathematical point of view, it can be interpreted as a partial rank-one convexification.

© 2014 Elsevier Ltd. All rights reserved.

---

### 1. Introduction

Phase field models have become an indispensable tool in materials science and physics in order to analyze the evolution of complex microstructures, cf. Khachaturyan (1983) and the more recent review, Steinbach (2013). Such microstructures are the source of many interesting and important phenomena defining the properties of materials. Typical examples are TRIP steels (TRansformation Induced Plasticity) and TWIP steels (TWinning Induced Plasticity). These materials are known

---

* Corresponding author at: TU Dortmund, Institute of Mechanics, Leonhard-Euler-Str. 5, D-44227 Dortmund, Germany. Tel.: +49 4152872543.
E-mail address: joern.mosler@tu-dortmund.de (J. Mosler).

http://dx.doi.org/10.1016/j.jmps.2014.04.002
0022-5096/© 2014 Elsevier Ltd. All rights reserved.

![](./images/813146708820099072_1.jpg)
![](./images/813146708820099072_2.jpg)
![](./images/813146708820099072_3.jpg)

to have a high strength (TRIP) and a high ductility (TWIP) due to transformations of the microstructure. Within a viewpoint of materials science or metal physics, phase field models go back, at least, to the pioneering work of Cahn and Hilliard (1958) and that of Allen and Cahn (1979). Focusing on the latter, the essential idea is to assign an order parameter to each phase which is similar to the mathematical indicator function. In line with the standard definition of the indicator function, the sum of all order parameters has to be equal to one at any point (partition of unity). However, and in contrast to the classical indicator function being either zero or one, the order parameters can also attain values in-between. Such points are associated with interfaces that separate different phases from each other. Physically speaking, a material point can therefore be related to more than one phase, i.e., phase field theory can be understood as a certain mixture theory.

Although phase field models have their roots in materials science, they can also be interpreted from a purely mathematical point of view, whereby phase field models represent sufficiently smooth approximations of the underlying sharp interface problems, i.e., the sharp transition from one phase to another phase is regularized by a smooth function showing a high gradient. In the limiting case, this smooth function converges to the indicator function, cf. Modica and Mortola (1977). An important advantage of phase field models compared to sharp interface representations is that tracking of material interfaces is not required. This tracking is a common numerical problem for most free boundary value problems.

Clearly, the idea to approximate a sharp interface in a smeared fashion can also be found in other types of models. A probably well known example is gradient-enhanced damage theory. By assigning two different order parameters to the virgin material and to the fully damaged state (the crack), such models fall into the range of phase field approaches. More details on the connection between phase field models and gradient-extended continua are discussed in Bourdin et al. (2000), and Miehe et al. (2010).

Although phase field models have nowadays indeed reached a certain maturity, some fundamental problems remain to be solved. A currently active research subject is the interaction of plasticity and material interfaces. To be more precise, it is not clear how a dislocation is affected by a phase boundary. For instance, a dislocation could simply be pushed away by a phase boundary such that the transformed domain would initially be dislocation free. The other limiting case would be that a dislocation can easily pass through phase boundaries and thus, the transformed phase inherits the dislocations of the original phase. Problems of this type are considered in Bartel et al. (2011), Mosler and Homayonifar (2012), Spatschek and Eidel (2013). Unfortunately, only little experimental information on this account seems to be available, cf. Kim et al. (2009). For this reason, the predictive capabilities of the models cannot currently be checked.

While the aforementioned problem, i.e., the interaction between plasticity and phase boundaries, is already relatively complex, a significantly simpler, yet unanswered and probably more fundamental problem is considered in this paper. It is related to the averaging of the bulk's energy within domains where more than one phase exists. That is, this paper deals with the underlying homogenization assumptions in phase field theory. According to the authors' knowledge, the only published paper dealing with this subject is Ammar et al. (2009). Within the cited work, the authors analyzed three different homogenization assumptions within a geometrically linearized setting: (a) Voigt/Taylor model, (b) Reuss/Sachs model and (c) Khachaturyan model, cf. Khachaturyan (1983). They show that the Khachaturyan model, although frequently applied in the phase field community, is strictly speaking not a homogenization method, since the bulk's average energy is not the average of the energies of the involved phases. Furthermore, the energies of the involved phases are not well-defined in the diffusive interface region where the phases co-exist. However, this localization property is indeed important, since the difference in energy between phases represents a driving force that moves the interface. With respect to the classical Voigt/ Taylor and Reuss/Sachs model, the authors of the paper (Ammar et al., 2009) demonstrated that the Reuss/Sachs model underestimates the influence of mechanics on diffusion. By way of contrast, the Voigt/Taylor model was found to provide a more realistic prediction on the coupled response, similarly to the non-classical homogenization approach by Khachaturyan (1983).

As implicitly mentioned in the previous paragraph, phase field models can be subdivided into two different classes with respect to the underlying homogenization assumptions. Within the first of those classes, an effective bulk's energy is a priori postulated, cf. Khachaturyan (1983). This effective energy depends on the concentration and/or on the order parameters. By way of contrast, an individual constitutive model is separately defined for each phase within the second class and, subsequently, the average bulk's energy is computed by homogenization theory. Models falling within this range can be found in Ammar et al. (2009) and references cited therein. Clearly, these two classes are not disjunctive. However, they are not equivalent either. To be more precise, every model belonging to the second class (models based on homogenization theory) also falls into the first class (since an average energy can be derived). However, the opposite is not true, i.e., the localization condition is not always fulfilled. Another disadvantage of models within the first class is that the definition of an effective energy is not always obvious – particularly if the involved phases show completely different material behavior. The focus of the present paper therefore relies on the second group of phase field models.

The classical homogenization assumptions considered so far in phase field theory are the Voigt/Taylor model and the Reuss/Sachs model, cf. Ammar et al. (2009). However, as shown in several classical textbooks on homogenization theory (see, e.g. Nemat-Nasser and Hori, 1993; Fish, 2009) both of them are known to represent limiting cases, i.e., by adopting a variational setting based on (incremental) energy minimization the Voigt/Taylor model leads to an upper bound whereas the Reuss/Sachs model leads to a lower bound. In this paper, a more realistic homogenization assumption is elaborated. It is closely related to the framework of rank-one convexification, cf. Ortiz and Repetto (1999), Miehe and Lambrecht (2003), Carstensen et al. (2002), Aubry et al. (2003), and Mosler and Homayonifar (2012). This framework has already been successfully applied to the analysis of evolving microstructures at the macroscale. The averaged energy predicted by this

framework is bounded by the Voigt/Taylor model and the Reuss/Sachs model. Furthermore, this approach fulfills equilibrium at material interfaces (continuity of the stress vector) and it is kinematically compatible. In the present paper, this framework is adapted to phase field theory. It will be shown that the resulting framework leads to better predictions and in sharp contrast to existing approaches, it naturally defines the mismatch energy at incoherent material interfaces (at incoherent interfaces, the Cauchy-Hadamard condition is not fulfilled for the Bain deformation gradients).

The paper is organized as follows: Section 2 is concerned with the fundamentals of phase field theory. The focus lies on an Allen-Cahn-type approach combined with a three-dimensional finite strain mechanical model based on a variationally consistent formulation (incremental energy minimization). For the resulting family of prototype models, different homogenization assumptions are presented in Section 3: (a) Voigt/Taylor model, (b) Reuss/Sachs model, (c) Khachaturyan model, and (d) a novel model based on partial rank-one convexification. A comparison between these models for a simple one-dimensional setting is given in Section 4, while a more realistic three-dimensional problem is numerically analyzed in Section 5.

## 2. Phase field theory in a nutshell

### 2.1. Sufficiently smooth approximation of sharp interfaces

In the following, a body $\Omega$ (undeformed configuration) consisting of two phases is considered. Such phases occupy the domains $\Omega_{1}$ and $\Omega_{2}$ such that $\Omega_{1} \cup \Omega_{2}=\Omega$ and $\Omega_{1} \cap \Omega_{2}=\emptyset$. By introducing the indicator functions of these sets according to
$$
i_{1}(\boldsymbol{X})=\left\{\begin{array}{ll}
1 & \text { if } \boldsymbol{X} \in \overline{\Omega}_{1} \\
0 & \text { if } \boldsymbol{X} \in \Omega_{2}
\end{array}\right\}, \quad i_{2}(\boldsymbol{X})=\left\{\begin{array}{ll}
0 & \text { if } \boldsymbol{X} \in \overline{\Omega}_{1} \\
1 & \text { if } \boldsymbol{X} \in \Omega_{2}
\end{array}\right\}
\tag{1}
$$
a phase is assigned to every point $\boldsymbol{X} \in \Omega$. Clearly, the indicator functions define a partition of unity, i.e., $i_{1}+i_{2}=1 \forall \boldsymbol{X} \in \Omega$. Consequently, only one of the indicator functions is independent. In what follows and without loss of generality, $i_{2}$ is chosen as independent and $i_{1}=1-i_{2}$. Since the partition and the respective interface between the different phases are usually not known in advance but governed by the underlying physics, problems of this type are also referred to as free boundary value problems.

According to the work of Modica and Mortola (1977), the aforementioned sharp interface problem (both indicator functions are discontinuous) can be approximated in the sense of gamma convergence (see Braides, 2002) by means of the by now classical Modica-Mortola energy (see Remark 1). In the one-dimensional setting, this energy reads
$$
f^{\varepsilon}[p]:=\int_{-\infty}^{\infty}\left\{\frac{3}{2} \varepsilon\left|\partial_{X} p\right|^{2}+6 \frac{1}{\varepsilon} p^{2}(1-p)^{2}\right\} \mathrm{d} X.
\tag{2}
$$
and a straightforward computation shows that the minimizer of this functional is (for the suitable boundary conditions $\lim _{X \rightarrow-\infty} p^{\varepsilon}=0$ and $\lim _{X \rightarrow \infty} p^{\varepsilon}=1$)
$$
p^{\varepsilon}(X)=1 / 2(\tanh [X / \varepsilon]+1)=\arg \min f^{\varepsilon}[p].
\tag{3}
$$

Evidently, the function $p^{\varepsilon}$ which is also referred to as *order-parameter* represents the aforementioned smooth approximation of the sharp interface problem, if the interface is at the origin, i.e.,
$$
\lim _{\varepsilon \rightarrow 0} p^{\varepsilon}(X)=i_{2}(X)=\left\{\begin{array}{ll}
1 & \forall X>0 \\
0 & \forall X \leq 0
\end{array}\right.
\tag{4}
$$

The degree of relaxation is controlled by the parameter $\varepsilon>0$. Mathematically speaking, functional (2) is a smooth approximation of the Hausdorff measure. Particularly,
$$
f^{\varepsilon}\left[p^{\varepsilon}(X)=1 / 2(\tanh [X / \varepsilon]+1)\right]=1
\tag{5}
$$
and the minimum of the functional is equivalent to the number of interfaces (points) between different phases, cf. Modica and Mortola (1977).

The previously described approximation of the one-dimensional problem can be directly generalized to the three-dimensional setting, i.e.,
$$
f^{\varepsilon}[p]:=\int_{\Omega}\left\{\frac{3}{2} \varepsilon|\nabla p|^{2}+6 \frac{1}{\varepsilon} p^{2}(1-p)^{2}\right\} \mathrm{d} V, \quad \nabla p:=\partial_{X} p.
\tag{6}
$$

In the three-dimensional case, the minimizer of the functional converges to the total area of all interfaces between the phases (mathematically speaking, the two-dimensional Hausdorff measure; the interested reader is referred to Modica and Mortola, 1977 for further details). Assuming a volume-specific interface energy $\psi_{\mathrm{i}}$, the total energy of all interfaces is thus given by
$$
I_{\Gamma}^{\varepsilon}[p]:=\int_{\Omega} \underbrace{\psi_{\mathrm{i}}\left\{\frac{3}{2} \varepsilon|\mathrm{GRAD} p|^{2}+6 \frac{1}{\varepsilon} p^{2}(1-p)^{2}\right\}}_{=: \psi_{\Gamma}^{\varepsilon}} \mathrm{d} V
\tag{7}
$$

and the postulate of minimum potential energy (for conservative systems) governing the geometry of the interfaces is given by
$$\min I_{\Gamma}^{\varepsilon}[p].\tag{8}$$

Remark 1. The original Modica-Mortola energy is
$$f^{\varepsilon}[p]:=\frac{1}{2} \int_{-\infty}^{\infty}\left\{\varepsilon\left|\partial_{X} u\right|^{2}+\frac{1}{\varepsilon} W(u)\right\} \mathrm{d} X\tag{9}$$
in which the double-well functional $W$ is usually chosen as
$$W(u)=\left(1-u^{2}\right)^{2}.\tag{10}$$

The minimizer of $f^{\varepsilon}$ is (for the suitable boundary conditions $\lim _{X \rightarrow-\infty} u^{\varepsilon}=-1$ and $\lim _{X \rightarrow \infty} u^{\varepsilon}=1$ )
$$u^{\varepsilon}(X)=\tanh (X / \varepsilon)\tag{11}$$
which leads to
$$f^{\varepsilon}\left[u^{\varepsilon}=\tanh (X / \varepsilon)\right]=4 / 3.\tag{12}$$

Starting from this, by now classic, result, Eq. (2) is obtained by rescaling
$$p^{\varepsilon}(X)=1 / 2\left(u^{\varepsilon}(X)+1\right)\tag{13}$$
and by multiplying Eq. (9) by the factor 3/4 (scaling).

### 2.2. Constitutive modeling of the bulk material

In this paper, an individual constitutive model for each phase involved is chosen and, subsequently, the effective energy of the mixture is derived by homogenization methods explained later. Thus, the chosen framework is in line with the works of Ammar et al. (2009) and Steinbach (2013). To neither overload the paper nor to distract the reader, an Allen-Cahn-type model is considered and the effect of a varying concentration is ignored and temperature effects are excluded. However, both aforementioned effects could be included in the presented framework in a relatively straightforward manner. Even with these restrictions, the discussed family of constitutive models and the resulting range of applications are still very broad. To be more explicit, a three-dimensional finite strain setting based on a variationally consistent formulation (incremental energy minimization) represents the starting point. The interested reader is referred to Ortiz and Repetto (1999), Carstensen et al. (2002), and Miehe and Lambrecht (2003), Mosler and Homayonifar (2012) for further details. This variational formulation encompasses, as special case, hyperelasticity and so-called *standard dissipative materials* in the sense of cf. Halphen and Nguyen (1975).

Following standard notation in continuum mechanics, a point $\boldsymbol{X} \in \Omega$ of the reference configuration is mapped to the deformed configuration $\boldsymbol{x} \in \varphi(\Omega)$ by means of the deformation mapping $\varphi$. Locally, this mapping can be approximated by the deformation gradient $\boldsymbol{F}:=\mathrm{GRAD} \varphi:=\nabla \varphi:=\partial_{X} \varphi$.

#### 2.2.1. Hyperelasticity

Based on the deformation gradient, standard (local) hyperelastic materials are defined by means of a Helmholtz energy of the type $\Psi_{B}=\Psi_{B}(\boldsymbol{F})$. Clearly, in order to fulfill the principle of frame indifference, the Helmholtz energy can be re-written as $\Psi_{B}=\Psi_{B}(\boldsymbol{C})$ with $\boldsymbol{C}=\boldsymbol{F}^{T} \cdot \boldsymbol{F}$ denoting the right Cauchy-Green tensor. Application of the standard Coleman and Noll procedure, Coleman and Noll, 1963, leads to the first Piola-Kirchhoff stress tensor
$$\boldsymbol{P}=\partial_{\boldsymbol{F}} \Psi_{B}=2 \boldsymbol{F}^{T} \cdot \partial_{\boldsymbol{C}} \Psi_{B}.\tag{14}$$

Assuming that the whole boundary value problem is conservative, the unknown deformation mapping follows from the postulate of minimum potential energy, i.e.,
$$\boldsymbol{\varphi}=\arg \inf I_{B}(\boldsymbol{\varphi}).\tag{15}$$

In the case of dead body loads $\left(\rho_{0} \boldsymbol{b}\right)$ and deformation-independent prescribed tractions $\overline{\boldsymbol{T}}$ at the Neumann boundary $\partial_{\mathrm{N}} \Omega$, the functional to be minimized reads
$$I_{B}(\boldsymbol{\varphi}):=\int_{\Omega} \Psi_{B}(\nabla \boldsymbol{\varphi}) \mathrm{d} V-\int_{\Omega} \rho_{0} \boldsymbol{b} \cdot \boldsymbol{\varphi} \mathrm{d} V-\int_{\partial_{\mathrm{N}} \Omega} \overline{\boldsymbol{T}} \cdot \boldsymbol{\varphi} \mathrm{d} A\tag{16}$$

Evidently, the deformation mapping has to fulfill the Dirichlet boundary conditions.

#### 2.2.2. Standard dissipative materials – incremental energy minimization

In the case of materials also showing dissipation, the Helmholtz energy does not depend solely on the deformation gradient at the considered time. One possibility to account for the path-dependence characteristic of materials with dissipation is the introduction of internal variables $\boldsymbol{\alpha}$ (strain-like), such as the plastic strains. Consequently, materials of this

type can be characterized by a Helmholtz energy

$$\Psi_{B}=\Psi_{B}(\boldsymbol{F}, \boldsymbol{\alpha})\tag{17}$$

and the stresses resulting from the Coleman and Noll procedure are given by

$$\boldsymbol{P}=\partial_{\boldsymbol{F}} \Psi_{B}.\tag{18}$$

In analogy to Eq. (18), stress-like internal variables can be defined as

$$\boldsymbol{Q}:=-\partial_{\boldsymbol{\alpha}} \Psi_{B}\tag{19}$$

and the reduced dissipation inequality yields (for isothermal processes)

$$\mathcal{D}_{B}=\boldsymbol{Q} * \dot{\boldsymbol{\alpha}} \geq 0.\tag{20}$$

Here, $*$ is a generalized scalar product.

The only equations that remain to be specified are the evolution equations of the type $\dot{\boldsymbol{\alpha}}=\boldsymbol{f}$. They have to fulfill, in particular, the second law of thermodynamics, i.e., In eq. (20). Focusing on *standard dissipative materials* in the sense of Halphen and Nguyen (1975), such equations are derived from a dissipation functional $\mathfrak{D}_{B}=\mathfrak{D}_{B}(\dot{\boldsymbol{\alpha}})$. To be more precise,

$$\boldsymbol{Q} \in \partial \mathfrak{D}_{B}\tag{21}$$

where $\partial \mathfrak{D}_{B}$ is the subdifferential of $\mathfrak{D}_{B}$. If the functional $\mathfrak{D}_{B}$ is convex, non-negative and $\mathcal{D}(\mathbf{0})=0$, the second law of thermodynamics is automatically fulfilled. In the case of rate-independent constitutive models, $\mathfrak{D}_{B}$ has to be positively homogeneous of degree one in $\dot{\boldsymbol{\alpha}}$ and the dissipation functional then equals the physical dissipation, i.e., $\mathfrak{D}_{B}=\mathcal{D}_{B}$. An illustrative example of such a constitutive model is given in Remark 2.

Eq. (21) is equivalent to the minimization problem

$$\inf _{\dot{\boldsymbol{\alpha}}}\left\{\dot{\Psi}_{B}+\mathfrak{D}_{B}\right\}.\tag{22}$$

Consequently, the consideration of a suitable time discretization of the time interval $[t_{n} ; t_{n+1}]$, such as the implicit first-order integration,

$$\mathcal{I}_{B}\left(\boldsymbol{F}_{n+1}, \boldsymbol{\alpha}_{n+1}\right):=\Psi_{B n+1}-\Psi_{B n}+\Delta t \mathfrak{D}_{B}\left(\frac{\boldsymbol{\alpha}_{n+1}-\boldsymbol{\alpha}_{n}}{\Delta t}\right)\tag{23}$$

yields the canonical update of the internal variables at time $t_{n+1}$

$$\boldsymbol{\alpha}_{n+1}=\left.\arg \inf \mathcal{I}_{B}\left(\boldsymbol{F}_{n+1}, \boldsymbol{\alpha}_{n+1}\right)\right|_{\boldsymbol{F}_{n+1}}\tag{24}$$

together with the reduced incremental potential

$$\mathcal{I}_{B}^{\mathrm{red}}\left(\boldsymbol{F}_{n+1}\right)=\left.\inf \mathcal{I}_{B}\left(\boldsymbol{F}_{n+1}, \boldsymbol{\alpha}_{n+1}\right)\right|_{\boldsymbol{F}_{n+1}}.\tag{25}$$

This reduced potential, in turn, serves as a pseudo-hyperelastic functional defining the stresses, i.e.,

$$\boldsymbol{P}_{n+1}=\partial_{\boldsymbol{F}_{n+1}} \mathcal{I}_{B}^{\mathrm{red}}\tag{26}$$

and, in analogy to standard hyperelasticity, the deformation mapping can be computed from the minimization problem (compare to Eqs. (15) and (16))

$$\boldsymbol{\varphi}_{n+1}=\arg \inf I_{B}\left(\boldsymbol{\varphi}_{n+1}\right).\tag{27}$$

where

$$I_{B}\left(\boldsymbol{\varphi}_{n+1}\right)=\int_{\Omega} \mathcal{I}_{B}^{\mathrm{red}}\left(\nabla \boldsymbol{\varphi}_{n+1}\right) \mathrm{d} V-\int_{\Omega} \rho_{0} \boldsymbol{b} \cdot \boldsymbol{\varphi}_{n+1} \mathrm{d} V-\int_{\partial_{\mathrm{N}} \Omega} \overline{\boldsymbol{T}} \cdot \boldsymbol{\varphi}_{n+1} \mathrm{d} A.\tag{28}$$

Remark 2. In the case of a von Mises plasticity model based on the multiplicative decomposition of the deformation gradient into an elastic part $\boldsymbol{F}^{\mathrm{e}}$ and a plastic part $\boldsymbol{F}^{\mathrm{p}}$, the evolution equation (flow rule) is of the type

$$\dot{\boldsymbol{F}}^{\mathrm{p}} \cdot \boldsymbol{F}^{\mathrm{p}-1}=: \boldsymbol{L}^{\mathrm{p}}, \quad \text { with } \operatorname{tr} \boldsymbol{L}^{\mathrm{p}}=0.\tag{29}$$

Introducing a threshold $Q_{0}>0$ (the yield stress), a reasonable choice for the dissipational functional for this rate-independent model is thus

$$\mathfrak{D}_{B}=Q_{0}\left\|\operatorname{DEV} \boldsymbol{L}^{\mathrm{p}}\right\| \geq 0\tag{30}$$

where $\operatorname{DEV} \boldsymbol{L}^{\mathrm{p}}$ is the deviator of $\boldsymbol{L}^{\mathrm{p}}$.

### 2.3. A variationally consistent phase field approach

Since hyperelastic models are included in the more general class of standard dissipative materials, each phase is assumed to be governed by a minimization problem of the type (27) with the energy (28). For the sake of brevity, body loads $(\rho_0 \boldsymbol{b})$ and prescribed tractions $(\overline{\boldsymbol{T}})$ will not be considered in what follows.

Combining the minimization problem (27) governing the bulk material with the minimization problem associated with the interface between the phases (see Eq. (8)) leads to the unified problem

$$
(\boldsymbol{\varphi}, p)=\arg \inf I(\boldsymbol{\varphi}, p). \tag{31}
$$

where

$$
I(\boldsymbol{\varphi}, p)=\int_{\Omega} \overline{\mathcal{I}}_{B}^{\text {red }}(\nabla \boldsymbol{\varphi}, p) \mathrm{d} V+\int_{\Omega} \Psi_{\Gamma}^{e}[p] \mathrm{d} V. \tag{32}
$$

While the second term in Eq. (32) has already been explained in detail in Section 2.1, the (incremental) energy $\overline{\mathcal{I}}_{B}^{\text {red }}$ remains to be defined. In domains where only one phase exists, the energy $\overline{\mathcal{I}}_{B}^{\text {red }}$ is identical to the energy $\mathcal{I}_{B}^{\text {red }}$ at the respective point. By way of contrast, in domains where both phases co-exist, this energy represents a suitable mixture of both energies (homogenization). The definition of a physically sound homogenization assumption for this energy is the key aspect of this paper. It will be dealt with in the next section.

In addition to a proper definition of $\overline{\mathcal{I}}_{B}^{\text {red }}$, another point has to be addressed: the dissipation associated with a propagating phase boundary. For that purpose, the variational derivative of the stored energy with respect to the order parameter $p$ (the driving force) is usually related to the rate of the order parameter, cf. Steinbach (2013). To be more precise, the simplest constitutive model

$$
\delta_{p}\left\{\overline{\mathcal{I}}_{B}^{\text {red }}+\Psi_{\Gamma}^{e}\right\}=-\dot{p} \eta \tag{33}
$$

is usually adopted where the variational derivative, which is the driving force from a physical point of view, shows the form

$$
\delta_{p}\left\{\overline{\mathcal{I}}_{B}^{\text {red }}(\boldsymbol{F}, p)+\Psi_{\Gamma}^{e}(p, \nabla p)\right\}=\partial_{p}\left\{\overline{\mathcal{I}}_{B}^{\text {red }}+\Psi_{\Gamma}^{e}\right\}-\operatorname{DIV}\left[\partial_{\nabla p} \Psi_{\Gamma}^{e}\right]. \tag{34}
$$

In Eq. (33), $\eta$ is a (constant) model parameter which can be interpreted as a viscosity or mobility of the interface. Evidently, constitutive model (33) can be re-written as

$$
\delta_{p}\left\{\overline{\mathcal{I}}_{B}^{\text {red }}+\Psi_{\Gamma}^{e}+\mathfrak{D}_{\Gamma}\right\}=0 \tag{35}
$$

with the interface-related dissipation functional (of Ginzburg-Landau-type)

$$
\mathfrak{D}_{\Gamma}=\mathfrak{D}_{\Gamma}(\dot{p})=\frac{1}{2} \eta \dot{p}^{2}. \tag{36}
$$

Since this functional is non-negative and convex and $\mathfrak{D}_{\Gamma}(0)=0$, the second law of thermodynamics is automatically fulfilled. Furthermore, due to the convexity of $\mathfrak{D}_{\Gamma}$, the stationarity condition (35) corresponds to a minimum. This minimization problem is non-local in nature, since $\Psi_{\Gamma}^{e}$ depends on $\nabla p$.

Applying once again a time integration, together with a suitable time discretization (here an implicit first-order scheme) such as

$$
\int_{t_{n}}^{t_{n+1}} \mathfrak{D}_{\Gamma} \mathrm{d} \approx \Delta t \mathfrak{D}_{\Gamma}\left(\frac{p_{n+1}-p_{n}}{\Delta t}\right), \tag{37}
$$

the minimization problem (31), (32) and the constitutive model (33) can be canonically coupled as

$$
\left(\boldsymbol{\varphi}_{n+1}, p_{n+1}\right)=\arg \inf I\left(\boldsymbol{\varphi}_{n+1}, p_{n+1}\right). \tag{38}
$$

with the modified (incremental) energy

$$
I\left(\boldsymbol{\varphi}_{n+1}, p_{n+1}\right)=\int_{\Omega} \overline{\mathcal{I}}_{B}^{\text {red }}\left(\nabla \boldsymbol{\varphi}_{n+1}, p_{n+1}\right) \mathrm{d} V+\int_{\Omega} \Psi_{\Gamma}^{e}\left[p_{n+1}\right] \mathrm{d} V+\int_{\Omega} \Delta t \mathfrak{D}_{\Gamma}\left(\frac{p_{n+1}-p_{n}}{\Delta t}\right) \mathrm{d} V. \tag{39}
$$

They key aspect of this paper is the analysis of the homogenization assumption with phase field approaches and its implications. This homogenization assumption affects only the first term of the potential (39). For this reason, only this term is considered in what follows.

### 3. Homogenization assumption in phase field approaches

In this section, the definition of the averaged energy $\overline{\mathcal{I}}_{B}^{\text {red }}$ is discussed in detail. As already mentioned, this aspect is of utmost importance from a physical point of view, since this definition enters the variational derivative (35) and thus, it governs the driving force associated with the interface's motion, e.g., by means of Eq. (33). Two different classes of models for deriving such an averaged energy can be found in the literature. Within the first of those classes, an individual constitutive model is separately defined for each phase and, subsequently, the average bulk's energy is computed by homogenization theory. Models falling within this range will be addressed in Section 3.1. By way of contrast, an effective

bulk's energy is a priori postulated in the second class of models. This effective energy depends on the order parameter. Such models will be discussed in Section 3.2.

### 3.1. Models based on homogenization theory
Assuming that the constitutive models of the two considered phases are variationally consistent (e.g. standard dissipative materials), they can be defined by means of (incremental) energies $\mathcal{I}_{E(i)}^{\text{red}}$. With the introduction of the Bain strains $\boldsymbol{F}_{(i)}^{\text{B}}$ (deformation gradients) within the phases, the energies can be written as
$$
\mathcal{I}_{E(1)}^{\text{red}}=\mathcal{I}_{B}^{\text{red}}\left(\boldsymbol{F}_{(1)} \cdot\left[\boldsymbol{F}_{(1)}^{\text{B}}\right]^{-1}\right), \quad \mathcal{I}_{E(2)}^{\text{red}}=\mathcal{I}_{B}^{\text{red}}\left(\boldsymbol{F}_{(2)} \cdot\left[\boldsymbol{F}_{(2)}^{\text{B}}\right]^{-1}\right).\tag{40}
$$

In what follows, the deformation gradients are assumed to be constant in each phase with respect to the spatial coordinates (a material point is considered). For this reason, the averaged bulk's energy is defined as
$$
\overline{\mathcal{I}}_{B}^{\text{red}}=(1-p) \mathcal{I}_{E(1)}^{\text{red}}+p \mathcal{I}_{E(2)}^{\text{red}}.\tag{41}
$$

Being further in line with standard homogenization theory, the (volumetric) averaging of the deformation gradients belonging to individual phases has to be equal to the (macroscopic) deformation gradient at the considered point, i.e.,
$$
\boldsymbol{F}=(1-p) \boldsymbol{F}_{(1)}+p \boldsymbol{F}_{(2)}.\tag{42}
$$

The only assumption which remains to be defined is the coupling of the deformation gradients within the different phases.

**Remark 3.** In contrast to the natural homogenization according to Eq. (41), a non-linear interpolation between the different energies is also sometimes used. Certainly, such a non-linear interpolation could also be employed here. However, it bears emphasis that a linear weighting of the energies does not imply that the second derivative of the mixed bulk's energy will vanish in general, since the deformation gradients $\boldsymbol{F}_{(1)}$ and $\boldsymbol{F}_{(2)}$ usually depend also on $p$.

#### 3.1.1. Reuss/Sachs model
The key assumption within the classic Reuss/Sachs model is that the stresses within both phases are identical. However, instead of enforcing this constraint directly, a variational reformulation is used here.

Since no constraint with respect to the kinematics is considered within the Reuss/Sachs model, the deformation gradients $\boldsymbol{F}_{(i)}$ are completely uncoupled. Denoting the jump of the deformation gradient across the interface as $\llbracket \boldsymbol{F} \rrbracket=\boldsymbol{F}_{(2)}-\boldsymbol{F}_{(1)}$, Eq. (42) can therefore be rewritten as
$$
\begin{aligned}
& \boldsymbol{F}_{(1)}=\boldsymbol{F}-p \llbracket \boldsymbol{F} \rrbracket \\
& \boldsymbol{F}_{(2)}=\boldsymbol{F}+(1-p) \llbracket \boldsymbol{F} \rrbracket.
\end{aligned}\tag{43}
$$

Inserting these equations into the energy (41) yields
$$
\overline{\mathcal{I}}_{B}^{\text{red}}(\boldsymbol{F}, \llbracket \boldsymbol{F} \rrbracket, p)=(1-p) \mathcal{I}_{E(1)}^{\text{red}}\left(\left[\boldsymbol{F}-p \llbracket \boldsymbol{F} \rrbracket\right] \cdot\left[\boldsymbol{F}_{(1)}^{\text{B}}\right]^{-1}\right)+p \mathcal{I}_{E(2)}^{\text{red}}\left(\left[\boldsymbol{F}+(1-p) \llbracket \boldsymbol{F} \rrbracket\right] \cdot\left[\boldsymbol{F}_{(2)}^{\text{B}}\right]^{-1}\right).\tag{44}
$$

Since energy minimization is the overriding principle within the adopted variational setting, and since energy $\overline{\mathcal{I}}_{B}^{\text{red}}$ is the only energy depending on the jump of the deformation gradient, minimization of the total energy $I$ with respect to $\llbracket \boldsymbol{F} \rrbracket$ is equivalent to minimizing Eq. (39) locally. Application of the variational derivative shows that minimizing Eq. (44) with respect to $\llbracket \boldsymbol{F} \rrbracket$ is equivalent to the classic Reuss assumption. To be more precise,
$$
\delta_{\llbracket \boldsymbol{F} \rrbracket} \overline{\mathcal{I}}_{B}^{\text{red}}(\boldsymbol{F}, \llbracket \boldsymbol{F} \rrbracket, p)=\left\{(1-p)(-p) \frac{\partial \mathcal{I}_{E(1)}^{\text{red}}}{\partial \boldsymbol{F}_{(1)}}+p(1-p) \frac{\partial \mathcal{I}_{E(2)}^{\text{red}}}{\partial \boldsymbol{F}_{(2)}}\right\}: \delta \llbracket \boldsymbol{F} \rrbracket=\left\{(1-p) p\left[-\boldsymbol{P}_{(1)}+\boldsymbol{P}_{(2)}\right]\right\}: \delta \llbracket \boldsymbol{F} \rrbracket=\mathbf{0} \Leftrightarrow \llbracket \boldsymbol{P} \rrbracket=\mathbf{0}.\quad(45)
$$

**Remark 4.** Minimization of Eq. (44) with respect to the jump of the deformation gradient shows strong analogies to the computation of the convex hull. As well known in continuum mechanics, the convex hull has good mathematical properties, however, it is physically not realistic, cf. Ciarlet (1988).

#### 3.1.2. Taylor/Voigt model
If a jump of the deformation gradient is not permitted, i.e., $\boldsymbol{F}_{(i)}=\boldsymbol{F}$, the classical Taylor model is obtained. In contrast to the Reuss model, this assumption is kinematically compatible. However, equilibrium at the interface is completely ignored. Hence, the Taylor assumption is statically incompatible. Furthermore, since the Reuss model can be interpreted as a relaxed Taylor model (relaxation with respect to $\llbracket \boldsymbol{F} \rrbracket$), the Taylor model defines an upper bound of the energy.

#### 3.1.3. Partial rank-one convexification
Since the energy is usually underestimated by the Reuss/Sachs model due to ignoring the constraints associated with kinematics, and due to the fact that the Taylor/Voigt model overestimates the energy due to not allowing for a relaxation, both homogenization approaches are not optimal. For this reason, an improved homogenization method is elaborated here.

In order to improve the Reuss/Sachs model, a kinematic compatibility can be enforced. The resulting model will be statically as well as kinematically compatible. A two-dimensional model within the small strain setting which is also statically as well as kinematically compatible was recently proposed in Durga et al. (2013). However, it bears emphasis that the model presented here is significantly more general. To be more precise, this novel model can be applied to any finite strain constitutive model which shows a variational structure – in a three-dimensional setting. Furthermore and equally important, the model is rigorously based on energy minimization.

According to the classical Hadamard jump condition, two deformation gradients result from a continuous deformation, if they fulfill the compatibility condition

$$
[\![\boldsymbol{F}]\!]:=\boldsymbol{F}_{(2)}-\boldsymbol{F}_{(1)}=\boldsymbol{a} \otimes \boldsymbol{N}
\tag{46}
$$

at the interface. Here, $\boldsymbol{N}$ is the normal vector of the interface with respect to the undeformed configuration and $\boldsymbol{a}$ denotes the jump across the interface. In phase field models, the normal vector can be computed from the order-parameter. To be more precise,

$$
\boldsymbol{N}=\frac{\mathrm{GRAD} p}{\|\mathrm{GRAD} p\|}
\tag{47}
$$

and the deformation gradients within the two different phases are

$$
\begin{aligned}
& \boldsymbol{F}_{(1)}=\boldsymbol{F}-p \boldsymbol{a} \otimes \boldsymbol{N} \\
& \boldsymbol{F}_{(2)}=\boldsymbol{F}+(1-p) \boldsymbol{a} \otimes \boldsymbol{N}.
\end{aligned}
\tag{48}
$$

The insertion of these equations into Eqs. (40) and Eq. (41) eventually yields

$$
\overline{\mathcal{I}}_{B}^{\text {red }}(\boldsymbol{F}, \boldsymbol{a}, p)=(1-p) \mathcal{I}_{B(1)}^{\text {red }}\left([\boldsymbol{F}-p \boldsymbol{a} \otimes \boldsymbol{N}] \cdot\left[\boldsymbol{F}_{(1)}^{\mathrm{B}}\right]^{-1}\right)+p \mathcal{I}_{B(2)}^{\text {red }}\left([\boldsymbol{F}+(1-p) \boldsymbol{a} \otimes \boldsymbol{N}] \cdot\left[\boldsymbol{F}_{(2)}^{\mathrm{B}}\right]^{-1}\right).
\tag{49}
$$

Again, the variable $\boldsymbol{a}$ describing the discontinuity enters the total energy only through $\overline{\mathcal{I}}_{B}^{\text {red }}$. For this reason, a minimization of the total energy with respect to $\boldsymbol{a}$ is equivalent to minimizing Eq. (49) pointwise. By computing the necessary condition for a minimum

$$
\begin{aligned}
\delta_{\boldsymbol{a}} \overline{\mathcal{I}}_{B}^{\text {red }}(\boldsymbol{F}, \boldsymbol{a}, p) & =\left\{(1-p)(-p) \frac{\partial \mathcal{I}_{B(1)}^{\text {red }}}{\partial \boldsymbol{F}_{(1)}} \cdot \boldsymbol{N}+p(1-p) \frac{\partial \mathcal{I}_{B(2)}^{\text {red }}}{\partial \boldsymbol{F}_{(2)}} \cdot \boldsymbol{N}\right\} \cdot \delta \boldsymbol{a}=\left\{(1-p) p\left[-\boldsymbol{T}_{(1)}+\boldsymbol{T}_{(2)}\right]\right\} \cdot \delta \boldsymbol{a}=\mathbf{0} \\
& \Leftrightarrow[\![\boldsymbol{T}]\!]=\mathbf{0}, \quad \boldsymbol{T}_{(i)}:=\boldsymbol{P}_{(i)} \cdot \boldsymbol{N}.
\end{aligned}
\tag{50}
$$

it can be seen that the stress state predicted by this new model is statically admissible, i.e., traction equilibrium is fulfilled.

Remark 5. Since the normal vector $\boldsymbol{N}$ depends on the gradient of the order-parameter, the variational derivative (34) changes to

$$
\delta_{p}\left\{\overline{\mathcal{I}}_{B}^{\text {red }}(\boldsymbol{F}, p)+\Psi_{\Gamma}^{e}(p, \nabla p)\right\}=\partial_{p}\left\{\overline{\mathcal{I}}_{B}^{\text {red }}+\Psi_{\Gamma}^{e}\right\}-\operatorname{DIV}\left[\partial_{\nabla p} \overline{\mathcal{I}}_{B}^{\text {red }}+\partial_{\nabla p} \Psi_{\Gamma}^{e}\right].
\tag{51}
$$

This clearly underlines the influence of the homogenization assumption on the driving force.

Remark 6. Within classical models based on rank-one laminates, the orientation of the interface (the normal vector $\boldsymbol{N}$) as well as jump direction (the vector $\boldsymbol{a}$) are computed by local energy minimization. By way of contrast, the phase field parameter $p$ defines the normal vector $\boldsymbol{N}$ and only the jump vector $\boldsymbol{a}$ is computed by local energy minimization within the proposed model. Furthermore and in contrast to classical models based on rank-one laminates, the evolution of the normal vector $\boldsymbol{N}$ leads to dissipation (through the evolution of $p$). Due to the aforementioned points, the authors have named the approach 'partial rank-one convexification'.

### 3.1.4. Summary
The Reuss/Sachs model, the Taylor/Voigt model as well as the novel model based on partial rank-one convexification can be summarized as a minimization problem of the type

$$
\left(\boldsymbol{\varphi}_{n+1},[\![\boldsymbol{F}]\!]_{n+1}, p_{n+1}\right)=\arg \inf I\left(\boldsymbol{\varphi}_{n+1},[\![\boldsymbol{F}]\!]_{n+1}, p_{n+1}\right).
\tag{52}
$$

where the energy $I\left(\boldsymbol{\varphi}_{n+1},[\![\boldsymbol{F}]\!]_{n+1}, p_{n+1}\right)$ is given by

$$
I\left(\boldsymbol{\varphi}_{n+1},[\![\boldsymbol{F}]\!]_{n+1}, p_{n+1}\right)=\int_{\Omega} \overline{\mathcal{I}}_{B}^{\text {red }}\left(\nabla \boldsymbol{\varphi}_{n+1},[\![\boldsymbol{F}]\!]_{n+1}, p_{n+1}\right) \mathrm{d} V+\int_{\Omega} \Psi_{\Gamma}^{e}\left[p_{n+1}\right] \mathrm{d} V+\int_{\Omega} \Delta t \mathfrak{D}_{\Gamma}\left(\frac{p_{n+1}-p_{n}}{\Delta t}\right) \mathrm{d} V.
\tag{53}
$$

The only, but nevertheless essential, difference between the Reuss/Sachs model, the Taylor/Voigt model and the novel model based on partial rank-one convexification is the space of admissible discontinuous deformation gradients. According to the previous subsections

$$
[\![\boldsymbol{F}]\!] \in\left\{\begin{array}{ll}
\emptyset=: \mathbb{U}_{\mathrm{TV}} & \text { Taylor/Voigt model } \\
\left\{\boldsymbol{a} \otimes \boldsymbol{N} \mid \boldsymbol{a} \in \mathbb{R}^{3}\right\}=: \mathbb{U}_{\mathrm{R} 1} & \text { partial rank }- \text { one } \\
\mathbb{R}^{3 \times 3}=: \mathbb{U}_{\mathrm{RS}} & \text { Reuss/Sachs model }
\end{array}\right.
\tag{54}
$$

implying $\mathbb{U}_{\mathrm{TV}} \subset \mathbb{U}_{\mathrm{R} 1} \subset \mathbb{U}_{\mathrm{RS}}$ and thus
$$
\inf _{[\boldsymbol{F}] \in \mathbb{U}_{\mathrm{RS}}} I \leq \inf _{[\boldsymbol{F}] \in \mathbb{U}_{\mathrm{R} 1}} I \leq \inf _{[\boldsymbol{F}] \in \mathbb{U}_{\mathrm{TV}}} I.
\tag{55}
$$

Remark 7. Within the computations presented in the next section, functional (53) has been discretized in space by finite elements, and the resulting nodal unknowns defining the approximation of the deformation mapping and the order parameter have been computed by applying an LBFGS-type optimization algorithm, cf. Liu and Nocedal (1989). The same algorithm has also been applied in order to solve the local problem
$$
\inf _{[\boldsymbol{F}]_{n+1}} I\left(\boldsymbol{\varphi}_{n+1}, [\boldsymbol{F}]_{n+1}, p_{n+1}\right)
\tag{56}
$$
at the integration points. Further details on the implementation are omitted here but will be published in a forthcoming paper.

### 3.2. Models not based on homogenization theory

For the sake of completeness and comparison, models not based on homogenization theory are also briefly discussed. In sharp contrast to the models presented before, deriving an effective averaged energy without classical homogenization assumptions is by no means trivial or straightforward in general - particularly, if the different phases involved show a different constitutive response. Some relatively restrictive assumptions are therefore usually required. Here, it is assumed that the energies of both phases have the same form. The only difference arises from different Bain strains. Furthermore, the focus lies on hyperelasticity, since the Helmholtz energies (as functions of the deformation gradient) would not remain identical for both phases, if dissipative effects are taken into account.

As a prototype model falling into the range of models not based on homogenization theory, the Khachaturyan model is discussed, cf. Khachaturyan (1983). According to Ammar et al. (2009), the elastic stiffnesses and the Bain strains are averaged within the model proposed by Khachaturyan. Since, the same Helmholtz energies have been assumed in both phases in this subsection, only the Bain strains have to be averaged. Although the classic Khachaturyan model has been developed in a geometrically linearized setting, a volume averaging of the engineering Bain strains is essentially equivalent to a volume averaging of the respective deformation gradients. Thus, the Khachaturyan model reads
$$
\overline{\Psi}_{B}(\boldsymbol{F}, p)=\Psi_{B}\left(\boldsymbol{F} \cdot\left[\overline{\boldsymbol{F}}^{\mathrm{B}}\right]^{-1}\right)
\tag{57}
$$
with the average Bain deformation gradient
$$
\overline{\boldsymbol{F}}^{\mathrm{B}}=(1-p) \boldsymbol{F}_{(1)}^{\mathrm{B}}+p \boldsymbol{F}_{(2)}^{\mathrm{B}}.
\tag{58}
$$

Remark 8. A similar extension of the Khachaturyan model to finite strains can also be found in Miehe and Hildebrand (2012). Within the cited paper, the Bain strains
$$
\boldsymbol{F}_{1}^{\mathrm{B}}=\boldsymbol{Q} \cdot \boldsymbol{U}_{(1)}, \quad \boldsymbol{F}_{2}^{\mathrm{B}}=\boldsymbol{U}_{(2)}
\tag{59}
$$
fulfilling the twinning equation
$$
\boldsymbol{Q} \cdot \boldsymbol{U}_{(1)}-\boldsymbol{U}_{(2)}=\boldsymbol{a} \otimes \boldsymbol{N}
\tag{60}
$$
are considered and the averaged energy of the mixture is postulated to be
$$
\overline{\Psi}_{B}(\boldsymbol{F}, p)=\overline{\Psi}_{B}\left(\boldsymbol{F} \cdot \overline{\boldsymbol{U}}^{-1}(p)\right)
\tag{61}
$$
where the averaged right stretch tensor is chosen as
$$
\overline{\boldsymbol{U}}(p)=(1-p) \boldsymbol{Q} \cdot \boldsymbol{U}_{(1)}+p \boldsymbol{U}_{(2)}.
\tag{62}
$$
Clearly, this is equivalent to the Khachaturyan model.

## 4. Comparison of different homogenization assumptions within phase field theory: the one-dimensional case based on a geometrically linearized setting

In this section, the implications resulting from different homogenization assumptions within phase field theory are analyzed by means of a one-dimensional academic example. It is a bar of unit length $\Omega=(-1 / 2 ;+1 / 2)$ which is decomposed into two time-invariant phases $(\dot{p}=0)$. The first phase is spanned by the interval $(-1 / 2 ; 0)$, while the second one is defined by the interval $(0 ;+1 / 2)$. For each of these phases, a Helmholtz energy of the type
$$
\Psi_{B(i)}\left(\varepsilon_{(i)}\right)=\frac{1}{2} E_{(i)}\left(\varepsilon_{(i)}-\varepsilon_{(i)}^{\mathrm{B}}\right)^{2}+\Psi_{B(i)}^{0}
\tag{63}
$$


is considered. Here, $E_{(i)}$ is the Young's modulus of phase $i$, $\varepsilon_{(i)}^{\mathrm{B}}$ is the Bain strain of phase $i$ and $\Psi_{B(i)}^{0}$ is the chemical energy of phase $i$. The bar is subjected to a constant stress field $\sigma_{0}$. In the following, the closed form solutions of this problem depending on the homogenization assumptions are summarized.

Remark 9. Concerning phase field models based on homogenization theory (see Sections 4.1-4.3), the numerical solution is expected to converge to the sharp interface problem: a constant Helmholtz energy within the different phases and the driving force (variational derivative of the total energy with respect to the order parameter) should be proportional to the configurational force acting at the interface.

### 4.1. Voigt/Taylor assumption

Considering the classical Voigt/Taylor assumption $\varepsilon_{(1)}=\varepsilon_{(2)}=\varepsilon$, the bulk's energy within the diffusive interface region reads

$$
\overline{\Psi}_{B}=(1-p) \Psi_{B(1)}(\varepsilon)+p \Psi_{B(2)}(\varepsilon).\tag{64}
$$

Since the applied boundary conditions result in a constant stress field $\sigma_{0}$, balance of linear momentum yields

$$
\sigma=\partial_{\varepsilon} \overline{\Psi}_{B}=\sigma_{0} \Rightarrow \varepsilon=\frac{\sigma_{0}+(1-p) E_{(1)} \varepsilon_{(1)}^{\mathrm{B}}+p E_{(2)} \varepsilon_{(2)}^{\mathrm{B}}}{(1-p) E_{(1)}+p E_{(2)}}.\tag{65}
$$

The insertion of this equation into the Helmholtz energies, finally leads to

$$
\begin{aligned}
& \Psi_{(1)}=\frac{1}{2} E_{(1)}\left(\frac{\sigma_{0}+p E_{(2)}\left(\varepsilon_{(2)}^{\mathrm{B}}-\varepsilon_{(1)}^{\mathrm{B}}\right)}{(1-p) E_{(1)}+p E_{(2)}}\right)^{2}+\Psi_{B(1)}^{0} \\
& \Psi_{(2)}=\frac{1}{2} E_{(2)}\left(\frac{\sigma_{0}+(1-p) E_{(1)}\left(\varepsilon_{(1)}^{\mathrm{B}}-\varepsilon_{(2)}^{\mathrm{B}}\right)}{(1-p) E_{(1)}+p E_{(2)}}\right)^{2}+\Psi_{B(2)}^{0}.
\end{aligned}\tag{66}
$$

Accordingly, the energies within the different phases are not constant in the diffusive interface region, but depend on the order parameter $p$. This contradicts the physical expectation associated with the underlying sharp interface problem, see Remark 9.

### 4.2. Reuss/Sachs assumption

Considering the classical Reuss/Sachs assumption, the bulk's energy within the diffusive interface region reads

$$
\overline{\Psi}_{B}=(1-p) \Psi_{B(1)}(\varepsilon-p [\![\varepsilon]\!])+p \Psi_{B(2)}(\varepsilon+(1-p) [\![\varepsilon]\!]).\tag{67}
$$

As shown before, the classical Reuss/Sachs assumption $\sigma_{(1)}=\sigma_{(2)}$ is equivalent to minimizing Eq. (67) with respect to the strain jump $[\![\varepsilon]\!]$ which gives rise to the introduction of the reduced Helmholtz energy

$$
\overline{\Psi}_{B, \mathrm{red}}=\inf _{[\![\varepsilon]\!]} \overline{\Psi}_{B}=\frac{1}{2} \frac{E_{(1)} E_{(2)}}{\left(p E_{(1)}+(1-p) E_{(2)}\right)}\left(\varepsilon-(1-p) \varepsilon_{(1)}^{\mathrm{B}}-p \varepsilon_{(2)}^{\mathrm{B}}\right)^{2}+(1-p) \Psi_{B(1)}^{0}+p \Psi_{B(2)}^{0}.\tag{68}
$$

With this reduced energy, the solution of the problem can be computed following the steps outlined in the previous subsection. To be more explicit, balance of linear momentum yields

$$
\partial_{\varepsilon} \overline{\Psi}_{B, \mathrm{red}}=\sigma_{0} \Rightarrow \varepsilon=\frac{\sigma_{0}}{E_{(1)} E_{(2)}}\left(p E_{(1)}+(1-p) E_{(2)}\right)+(1-p) \varepsilon_{(1)}^{\mathrm{B}}+p \varepsilon_{(2)}^{\mathrm{B}}\tag{69}
$$

and the insertion of this equation into the Helmholtz energies finally leads to

$$
\begin{aligned}
& \Psi_{(1)}=\frac{\sigma_{0}^{2}}{2 E_{(1)}}+\Psi_{B(1)}^{0} \\
& \Psi_{(2)}=\frac{\sigma_{0}^{2}}{2 E_{(2)}}+\Psi_{B(2)}^{0}.
\end{aligned}\tag{70}
$$

Accordingly, the energies within the different phases are constant in the diffusive interface region - as expected from a physical point of view, see Remark 9.

### 4.3. Partial rank-one convexification

In a one-dimensional setting, rank-one convexification is equivalent to a (standard) convexification. Since the variational formulation of the Reuss/Sachs model is, from a mathematical point of view, a (standard) convexification, the novel model based on a partial rank-one convexification is equivalent to the classical Reuss/Sachs model in the one-dimensional setting.

That can also be verified by observing that the strains

$$
\varepsilon_{(1)}=\varepsilon-p \llbracket \varepsilon \rrbracket, \quad \varepsilon_{(2)}=\varepsilon+(1-p) \llbracket \varepsilon \rrbracket
\tag{71}
$$

are indeed kinematically compatible, i.e, they result from a continuous deformation mapping.

### 4.4. Khachaturyan model

According to Khachaturyan (1983), the Khachaturyan model is based on the bulk's Helmholtz energy

$$
\overline{\Psi}_{B}=\frac{1}{2} \bar{E}(p)\left(\varepsilon-\bar{\varepsilon}^{\mathrm{B}}(p)\right)^{2}+(1-p) \Psi_{B(1)}^{0}+p \Psi_{B(2)}^{0}
\tag{72}
$$

within the diffusive interface region. It depends on the averaged Bain strain

$$
\bar{\varepsilon}^{\mathrm{B}}(p)=(1-p) \varepsilon_{(1)}^{\mathrm{B}}+p \varepsilon_{(2)}^{\mathrm{B}}
\tag{73}
$$

and the averaged Young's modulus

$$
\bar{E}(p)=(1-p) E_{(1)}+p E_{(2)}.
\tag{74}
$$

Following the previous subsections, balance of linear momentum yields

$$
\sigma=\partial_{\varepsilon} \overline{\Psi}_{B}=\sigma_{0} \Rightarrow \varepsilon=\frac{\sigma_{0}}{\bar{E}}+\bar{\varepsilon}^{\mathrm{B}}.
\tag{75}
$$

As a result, the bulk's energy corresponding to strain field (75) is given by

$$
\overline{\Psi}_{B}=\frac{1}{2} \frac{\sigma_{0}^{2}}{\bar{E}(p)}+(1-p) \Psi_{B(1)}^{0}+p \Psi_{B(2)}^{0}.
\tag{76}
$$

Once again, it is noted that only the averaged energy (76) can be computed i the Khachaturyan model, not the Helmholtz energies associated with the different phases. Furthermore, it is noted that Energy (76) depends on the order parameter.

### 4.5. Summary

A comparison between the different solutions corresponding to the different homogenization assumptions is presented here. The results are based on the material parameters summarized in Table 1.

Fig. 1 shows the spatial distribution of the bulk's energy. Accordingly, except for the Taylor/voigt model, all homogenization assumptions lead to a similar transition between the energies of the different phases. A simple possibility to estimate the physical reasonableness of the solutions is to set the chemical energies of both phases to zero, e.g., $\Psi_{B(1)}^{0}=\Psi_{B(2)}^{0}=0$ and $\sigma_{0}=0$. In this case, the averaged bulk's energy has to vanish everywhere. However, that is not the case for the Voigt/Taylor model, cf. Miehe and Hildebrand (2012).

A more detailed analysis of the physical reasonableness can be carried out by investigating the driving force acting at the interface. Within all frameworks discussed here, this driving force is defined by the variational derivative of the total energy, i.e., by $\delta_{p} I$, see Eq. (34). Since the only term of the total energy $I$ depending on the homogenization assumption is the energy $\overline{\mathcal{I}}_{B}^{\text {red }}$, the variational derivative $\delta_{p} \overline{\mathcal{I}}_{B}^{\text {red }}$ will be analyzed in what follows. By taking the predetermined assumptions (hyperelastic model of Hooke's type), the identity $\overline{\mathcal{I}}_{B}^{\text {red }}=\overline{\Psi}_{B}$ holds.

In the case of the Voigt/Taylor model, the Sachs/Reuss model or the novel model based on partial rank-one convexification, the averaged bulk's energy shows the structure

$$
\overline{\Psi}_{B}=(1-p) \Psi_{B(1)}+p \Psi_{B(2)}.
\tag{77}
$$

Consequently, the general structure of the driving force reads

$$
f:=\partial_{p} \overline{\Psi}_{B}=\left[\Psi_{B(2)}-\Psi_{B(1)}\right]-\sigma_{0}\left[\varepsilon_{2}-\varepsilon_{1}\right]=\llbracket \Psi_{B} \rrbracket-\sigma_{0} \llbracket \varepsilon \rrbracket.
\tag{78}
$$

<table>
<caption>Table 1<br>One-dimensional analysis of a bar. The bar of unit length consists of phase 1 ($X \in (-1/2;0)$) and phase 2 ($X \in (0;+1/2)$) and is subjected to a constant stress field $\sigma_{0}=1 \times 10^{7}$ ($\text{N/m}^2$). The length of the diffusive interface region is defined by $\varepsilon=0.04$. Material parameters used within the numerical analysis.</caption>
<thead>
<tr>
<th></th>
<th>Phase 1</th>
<th>Phase 2</th>
</tr>
</thead>
<tbody>
<tr>
<td>Elastic modulus, E ($\text{N/m}^2$)</td>
<td>$2.0 \times 10^{9}$</td>
<td>$2.5 \times 10^{9}$</td>
</tr>
<tr>
<td>Poisson ration, $\nu$ (-)</td>
<td>0.3</td>
<td>0.3</td>
</tr>
<tr>
<td>Bain strain, $\varepsilon_{(i)}^{\text{B}}$ (-)</td>
<td>0.011</td>
<td>0.022</td>
</tr>
<tr>
<td>Chemical energy, $\Psi_{B(i)}^{0}$ ($\text{N/m}^2$)</td>
<td>$1.0 \times 10^{5}$</td>
<td>$1.5 \times 10^{5}$</td>
</tr>
</tbody>
</table>

![](./images/813146708820099072_4.jpg)

Fig. 1. One-dimensional analysis of a bar. The bar of unit length consists of phase 1 $(X \in (-1/2; 0))$ and phase 2 $(X \in (0; +1/2))$ and is subjected to a constant stress field $\sigma_0=1 \times 10^7$. The diagram shows the normalized bulk's energy.

![](./images/813146708820099072_5.jpg)

Fig. 2. One-dimensional analysis of a bar. The bar of unit length consists of phase 1 $(X \in (-1/2; 0))$ and phase 2 $(X \in (0; +1/2))$ and is subjected to a constant stress field $\sigma_0=1 \times 10^7$. The diagram shows the normalized driving force at the interface – to be more precise, it shows the normalized variational derivative of the bulk's energy with respect to the phase field parameter.

For the Voigt/Taylor model, $\varepsilon_1 = \varepsilon_2$ holds and, hence, the driving force simplifies to $f = [\![ \Psi_B ]\!]$. Accordingly, the difference in bulk's energy is one of the dominating factors for phase transformation. In the case of the Khachaturyan's model such a physically sound interpretation is not possible, since the energies within the individual phases cannot be computed (the model does not show a localization property).

The spatial distribution of the phase field's driving force $f$ is shown in Fig. 2. As evident from these figures, the models should predict a constant driving force – also in the diffusive interface region which is proportional to the respective configurational force of the underlying sharp interface problem, cf. Remark 9. However, only the Reuss/Sachs model and the novel model based on partial rank-one convexification (which is identical to the Reuss/Sachs model in 1D) meet this expectation. The Voigt/Taylor model yields the largest deviation from the physical solution – in line with the previous observations.

## 5. Comparison of different homogenization assumptions within phase field theory: the fully three-dimensional case in a finite strain setting

Within the one-dimensional example analyzed in the previous section, only the Reuss/Sachs homogenization as well as the novel model based on partial rank-one convexification led to the physically correct solution (spatially constant driving

force). In this section, a fully three-dimensional setting will be considered. In this case, the Reuss/Sachs homogenization and the novel model are no longer equivalent.

### 5.1. Representative volume element with piece-wise constant deformation gradient

A three-dimensional representative volume element (RVE) is numerically studied in this section. The RVE consists of two time-invariant phases ($\dot{p}=0$) which are assumed to be governed by the hyperelastic Helmholtz energies

$$
\Psi_{B(i)}=\Psi_{B}\left(\boldsymbol{F}_{(i)}^{\mathrm{e}}\right)
\tag{79}
$$

where

$$
\boldsymbol{F}_{(i)}^{\mathrm{e}}=\boldsymbol{F}_{(i)} \cdot\left[\boldsymbol{F}_{(i)}^{\mathrm{B}}\right]^{-1}
\tag{80}
$$

are the elastic parts of the deformation gradients. Hence, the only difference in the constitutive response is due to the different Bain strains $\boldsymbol{F}_{(i)}^{\mathrm{B}}$. For the sake of simplicity, an isotropic neo-Hooke Helmholtz energy is adopted for $\Psi_{B}$ in what follows.

If one assumes that the deformation gradients $\boldsymbol{F}_{(i)}$ are spatially constant within the two phases, the averaged bulk's Helmholtz energy of the RVE is given by $\overline{\Psi}_{B}$ and, consequently, the macroscopically fully relaxed RVE's bulk's energy can be computed from the minimization problem

$$
\inf _{\boldsymbol{F}} \overline{\Psi}_{B}.
\tag{81}
$$

It bears emphasis that, due to the assumption $\dot{p}=0$, all other parts of the total energy are constant (time-independent) and that only the bulk's energy is unknown.

From a physical point of view, Energy (81) should depend on the Bain strains $\boldsymbol{F}_{(i)}^{\mathrm{B}}$ as well as on the topology of the interface between the different phases. Here, a planar interface characterized by its normal vector $\boldsymbol{N}$ is considered and the Bain strains are chosen as

$$
\boldsymbol{F}_{(1)}^{\mathrm{B}}=\boldsymbol{Q} \cdot \boldsymbol{U}_{(1)}^{\mathrm{B}}, \quad \boldsymbol{F}_{(2)}^{\mathrm{B}}=\boldsymbol{U}_{(2)}^{\mathrm{B}}
\tag{82}
$$

with the right stretch tensors

$$
\boldsymbol{U}_{(1)}^{\mathrm{B}}=\left[\begin{array}{ccc}
\frac{\alpha+\gamma}{2} & \frac{\alpha-\gamma}{2} & 0 \\
\frac{\alpha-\gamma}{2} & \frac{\alpha+\gamma}{2} & 0 \\
0 & 0 & \beta
\end{array}\right], \quad \boldsymbol{U}_{(2)}^{\mathrm{B}}=\left[\begin{array}{ccc}
\frac{\alpha+\gamma}{2} & \frac{\gamma-\alpha}{2} & 0 \\
\frac{\gamma-\alpha}{2} & \frac{\alpha+\gamma}{2} & 0 \\
0 & 0 & \beta
\end{array}\right]
\tag{83}
$$

and the rotation

$$
\boldsymbol{Q}=\left[\begin{array}{ccc}
\frac{2 \alpha \gamma}{\alpha^{2}+\gamma^{2}} & -\frac{\alpha^{2}-\gamma^{2}}{\alpha^{2}+\gamma^{2}} & 0 \\
\frac{\alpha^{2}-\gamma^{2}}{\alpha^{2}+\gamma^{2}} & \frac{2 \alpha \gamma}{\alpha^{2}+\gamma^{2}} & 0 \\
0 & 0 & 1
\end{array}\right].
\tag{84}
$$

In these equations, the parameters $\alpha, \beta$ and $\gamma$ define the strain induced by a phase transformation. In line with Miehe and Hildebrand (2012), these parameters are set to $\alpha=1.0619, \beta=0.9178$ and $\gamma=1.0231$. For this choice, the twinning equation

$$
\left[\left[\boldsymbol{F}^{\mathrm{B}}\right]\right]=\boldsymbol{Q} \cdot \boldsymbol{U}_{(1)}^{\mathrm{B}}-\boldsymbol{U}_{(2)}^{\mathrm{B}}=\boldsymbol{a} \otimes \boldsymbol{N}
\tag{85}
$$

shows two solutions. These are: $\boldsymbol{N}= \pm \boldsymbol{e}_{1}$ and $\boldsymbol{N}= \pm \boldsymbol{e}_{2}$ where $\boldsymbol{e}_{i}$ define the cartesian base vectors. As a result, such orientations characterize coherent interfaces (with respect to the initial undeformed state), cf. Remark 10. Accordingly, Energy (81) should vanish in this case (no chemical energies are considered here). By way of contrast, for orientations $\boldsymbol{N}$ for which the Bain strains cannot be derived from a continuous deformation mapping, i.e., the twinning equation (85) cannot be fulfilled, the respective Energy (81) should not vanish. To be more precise, this energy is expected to depend monotonically on the mismatch angle.

Energy (81) is now computed for all different homogenization assumptions. The first crucial observation is that neither the Voigt/Taylor model nor the Reuss/Sachs model depend on the normal vector $\boldsymbol{N}$. As a result, Energy (81) is not affected by the mismatch angle for these homogenization assumptions. In sharp contrast, the novel model based on partial rank-one convexification does depend on $\boldsymbol{N}$. The results obtained from the different homogenization assumptions are summarized in Fig. 3. As expected from the order relation between the different homogenization assumptions according to Eq. (55), the energies predicted by the novel model based on partial rank-one convexification are bounded by those related to the classical approach by Voigt/Taylor and to that by Sachs/Reuss. Furthermore, only the energy associated with the novel model depends on the mismatch angle. The larger the mismatch, the larger the respective mismatch energy. Coherent interfaces correspond to energy minima.

In summary only the novel model naturally defines the mismatch energy at incoherent material interfaces. An additional artificial mismatch energy is thus not required.

![](./images/813146708820099072_6.jpg)

Fig. 3. Three-dimensional analysis of a representative volume element (RVE) consisting of two time-invariant phases ($\dot{\rho}=0$) which are assumed to be governed by hyperelastic Helmholtz energies. The phases are separated by a planar interface. The Bain strains within the different phases are defined in Eq. (82). The diagram shows the averaged bulk's Energy (81) of the RVE for three different homogenization assumptions. The energy predicted by the novel model based on rank-one convexification is bounded by the constant energies corresponding to the Taylor/Voigt model and to the Reuss/Sachs model. Only the energy associated with the novel model depends monotonically on the mismatch angle.

Remark 10. An interface is called incoherent, if the Cauchy-Hadamard condition is not fulfilled for the Bain strains (the respective deformation gradients $\boldsymbol{F}_{(i)}^{\mathrm{B}}$). However, that does not imply that the total deformation is incompatible. As a matter of fact, compatibility is enforced in the novel approach based on partial rank-one convexification - for the total strains $\boldsymbol{F}$, not for the Bain strains.

### 5.2. Spherical inclusion embedded in a cube

A slightly modified version of the problem discussed in the previous subsection is investigated here. Once more it is an RVE consisting of two time-invariant phases with the same bulk's Helmholtz energies as considered before (i.e., see Eq. (79) and Eqs. (80) and (82)). However, and in contrast to the example analyzed before, the geometry is more complex. To be more precise, phase 1 is now a spherical inclusion (normalized unit diameter) embedded in a cube ($2\times2\times2$) of phase 2. In order to model this problem realistically, the assumption of a spatially constant deformation gradient within the two phases is abandoned here. Instead, the RVE is discretized by finite elements. To be more explicit, a mesh consisting of 204.273 tri-quadratic tetrahedron elements is used. Since the phases are assumed as time-invariant, the only unknown at the global level is the deformation mapping. The resulting 825.558 deformation degrees of freedom are computed by means of an LBFGS-type optimization algorithm as minimizer of the total energy. Again, an unconstrained minimization is considered, i.e., homogeneous Neumann boundary conditions (stress-free surface) are applied. The 7.353.828 DOFs (Reuss/Sachs-model) and the 2.451.276 DOFs (model based on partial rank-one convexification) characterizing the jump in the deformation gradient are computed in the same manner.

The results obtained from the Taylor/Voigt, the Reuss/Sachs and the novel model based on partial rank-one convexification are summarized in Fig. 4.

According to the twinning equation (85) and the underlying Bain transformations (82), coherent interfaces are those represented by the normal vectors $\boldsymbol{N}=\pm\boldsymbol{e}_{1}$ and $\boldsymbol{N}=\pm\boldsymbol{e}_{2}$. Consequently, the bulk's Helmholtz energy associated with such orientation should correspond to a minimum. As can be seen in Fig. 4, this is only the case for the novel model based on partial rank-one convexification. By way of contrast, the Taylor/Voigt as well as the Reuss/Sachs assumptions lead to the opposite result: Minima are associated with interfaces showing the largest mismatch angle. Interestingly, the Taylor/Voigt and the Reuss/Sachs homogenization assumption lead qualitatively to the same results.

## 6. Conclusions

The presented paper provided an analysis of the influence of homogenization assumptions in phase field theories. As a prototype, two phases driven by an Allen-Cahn-type model were considered. Within such phases, the mechanical response was assumed to be governed by means of a general variational principle. This principle is embedded in a three-dimensional finite strain setting and includes so-called *standard dissipative materials* in the sense of Halphen and Nguyen. It was shown that the underlying homogenization assumptions are indeed of utmost importance, since they define several fundamental physical properties, e.g., the driving force of material interfaces. It turned out that none of the existing homogenization assumptions captures all relevant physical characteristics. For this reason, a novel homogenization approach was advocated. From a mathematical point of view, this new model can be interpreted as a partial rank-one convexification. Within a variational setting based on (incremental) energy minimization, the energies predicted by novel approach are bounded by

![](./images/813146708820099072_7.jpg)

Fig. 4. Spatial distribution of the bulk's Helmholtz energy at a matrix-inclusion interface for different homogenization assumptions. Coherent interfaces are those represented by the normal vectors $N = \pm \boldsymbol{e}_1$ and $N = \pm \boldsymbol{e}_2$. Only the novel model based on partial rank-one convexification captures the physically correct minima.

the Voigt/Taylor and the Reuss/Sachs model. The new approach was shown to be statically and kinematically compatible. Furthermore and equally important, it naturally defines the mismatch energy at incoherent material interfaces.

## Acknowledgments

Financial support from the Mercator Research Center (MERCUR) is gratefully acknowledged.

## References

Allen, S.M., Cahn, J.W., 1979. A microscopic theory for antiphase boundary motion and its application to antiphase domain coarsening. Acta Metall. 27, 1085-1095.
Ammar, K., Appolaire, B., Cailletaud, G., Forest, S., 2009. Combining phase field approach and homogenization methods for modelling phase transformation in elastoplastic media. Eur. J. Comput. Mech. 18 (5-6), 485-523.
Aubry, S., Fago, M., Ortiz, M., 2003. A constrained sequential-lamination algorithm for the simulation of sub-grid microstructure in martensitic materials. Comput. Methods Appl. Mech. Eng. 192, 2823-2843.
Bartel, T., Menzel, A., Svendsen, B., 2011. Thermodynamic and relaxation-based modeling of the interaction between martensitic phase transformations and plasticity. J. Mech. Phys. Solids 59, 1004-1019.
Bourdin, B., Francfort, G.A., Marigo, J-J., 2000. Numerical experiments in revisited brittle fracture. J. Mech. Phys. Solids 48, 797-826.
Braides, A., 2002. Gamma-Convergence for Beginners. Oxford University Press ISBN-10: 0198507844.
Cahn, J.W., Hilliard, J.E., 1958. Free energy of a nonuniform system. I. Interfacial free energy. J. Chem. Phys. 28, 258-267.
Carstensen, C., Hackl, K., Mielke, A., 2002. Non-convex potentials and microstructures in finite-strain plasticity. Proc. R. Soc. A 458, 299-317.
Ciarlet, P., 1988. Mathematical Elasticity. Three-dimensional Elasticity, vol. 1. North-Holland Publishing Company, Amsterdam.
Coleman, B., Noll, W., 1963. The thermodynamics of elastic materials with heat conduction and viscosity. Arch. Ration. Mech. Anal. 13, 167-178.
Durga, A., Wollants, P., Moelans, N., 2013. Evaluation of interfacial excess contributions in different phase-field models for elastically inhomogeneous systems. Modelling Simul. Mater. Sci. Eng. 21, 055018.
Fish, J., 2009. Multiscale Methods: Bridging the Scales in Science and Engineering. Oxford University Press ISBN-10: 0199233853.

Halphen, B., Nguyen, Q.S., 1975. Sur les matériaux standard généralisés. J. de Mécanique 14, 39–63.

Khachaturyan, A.G., 1983. Theory of Structural Transformations in Solids. Wiley & Sons ISBN-10: 0444500847.

Kim, G.S., Yi, S., Huang, Y., Lilleodden, E., 2009. Twining and slip activity in magnesium ⟨1120⟩ single crystal. In: Mechanical Behavior at Small Scales – Experiments and Modeling, vol. 1224 of MRS Proceedings.

Liu, D.C., Nocedal, J., 1989. On the limited memory method for large scale optimization. Math. Program. B 45, 503–528.

Miehe, C., Hildebrand, F.E., 2012. A phase field model for the formation and evolution of martensitic laminate microstructure at finite strains. Philos. Mag. 92 (34), 4250–4290.

Miehe, C., Lambrecht, M., 2003. A two-scale finite element relaxation analysis of shear bands in non-convex inelastic solids: small-strain theory for standard dissipative materials. Comput. Meth. Appl. Mech. Eng. 192, 473–508.

Miehe, C., Welschinger, F., Hofacker, M., 2010. Thermodynamically consistent phase-field models of fracture: variational principles and multi-field FE implementations. Int. J. Numer. Methods Eng. 83, 1273–1311.

Modica, L., Mortola, S., 1977. Un esempio di Gamma-convergenza. Boll. Un. Mat. Ital. 14B, 285–299.

Mosler, J., Homayonifar, M., 2012. Efficient modeling of microstructure evolution in magnesium by energy minimization. Int. J. Plast. 28, 1–20.

Nemat-Nasser, S., Hori, M., 1993. Micromechanics: Overall Properties of Heterogeneous Solids. Elsevier ISBN-10: 0486462803.

Ortiz, M., Repetto, E.A., 1999. Nonconvex energy minimization and dislocation structures in ductile single crystals. J. Mech. Phys. Solids 47, 397–462.

Spatschek, R., Eidel, B., 2013. Driving forces for interface kinetics and phase field models. Int. J. Solids Struct. 50, 2424–2436.

Steinbach, I., 2013. Phase-field model for microstructure evolution at the mescoscopic scale. Annu. Rev. Mater. Res. 43, 89–107.