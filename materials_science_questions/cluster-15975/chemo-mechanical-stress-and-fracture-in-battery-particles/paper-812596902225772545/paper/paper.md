# A hybrid phase field model for fracture induced by lithium diffusion in electrode particles of Li-ion batteries

Masoud Ahmadi

Faculty of Mechanical Engineering, University of Guilan, P.O. Box 3756, Rasht, Iran

---

## ARTICLE INFO

**Keywords:**
Phase field model
Hybrid formulations
Lithium-ion batteries
Crack propagation
Finite element method
Electrode particles.

## ABSTRACT

Lithium-ion batteries (LIBs) of high energy density and light-weight design, find wide applications in electronic devices and systems. Degradation mechanisms that caused by lithiation is a main challenging problem for LIBs with high capacity electrodes like silicon (Si), which eventually can reduce the lifetime of batteries. In this paper, a hybrid phase field model (PFM) is proposed to study the fracture behavior of LIB electrodes. The model considers the coupling effects between lithium (Li) -ion diffusion process, stress evolution and crack propagation. Also, the dependency of Elastic properties on the concentration magnitude of Li-ion is considered. A numerical implementation based on a MATLAB finite element (FE) code is elaborated. Then, the proposed hybrid PF approach is applied to a Nanowire (NW) Si electrode particle. Numerical results show that the hybrid model shows less tendency to crack growth than the isotropic model.

---

## 1. Introduction

Due to high energy storage density, LIBs are widely used in different technologies such as portable electronic devices and electric vehicles [1]. The working principle of LIB cells lies essentially in the electro-chemical potential driven redox reaction in the electrode active materials [2]. In LIBs, Li-ions transfer from the anode and diffuse through the electrolyte towards the cathode during charge and when the battery is discharged, the respective electrodes change roles. Abundant efforts have been made to develop next-generation battery systems with novel electrode materials, however, most candidates with promising electro-chemical potential have chemo-mechanical stability problems [3]. Due to Graphite low volume changes (about 10%) under intercalation, Graphite is a common anode among the commercial batteries [4]. Silicon is a promising candidate material with a theoretical capacity of 4200 mA h/g, which is exceedingly higher than the theoretical capacity of Graphite with 372 mA h/g. Nevertheless, Si shows a volume changes of about 300%, which causes high stress in electrodes that eventually lead to fracture, fragmentation, or pulverization [5,6,2]. Cracking of electrodes under diffusion is one of the main reasons for the short life span of LIBs with high capacity electrodes [7].

For a better understanding of the fracture behavior of LIBs during lithiation, numbers of modeling and computational simulations have been expanded, which can offer insights into the structural reliability of electrodes in LIBs. Ryu et al. [8] used a fracture mechanics approach to study fracture behavior of Si NWs during lithiation/delithiation process. They considered large deformation associated with lithiation and effects of pressure gradients on the diffusion of Li in their study. Grantab and Shenoy [9] proposed a method that accounts for the effects of pressure-gradients within the material on the flux for studying li-thiation-induced crack propagation in Si NWs. Their model consists of FE simulations in which the pressure-gradients are computed numerically to capture the effect of the crack-tip on the localized diffusion. Chen et al. [10] established an analytical model to study the stress evolution and crack propagations in spherical particle electrodes during phase transformation. Hu et al. [11] developed an analytical model to study the diffusion induced stress evolution and discussed the crack growth by using stress intensity factor coupled with surface effects. They showed that smaller Si Spherical particles exhibit higher structural integrity. Wang et al. used Peridynamic theory to study the li-thiation induced stress and fracture in Si square thin film electrodes [12,13], and Si spherical and cylindrical nanoparticles [14]. Gwak et al. [15] investigated the stress evolution and dynamic cracking behavior of Si NWs using a chemo-mechanical model based on the large deformation theory and the bilinear cohesive zone model.

In sharp-interface modeling of phase-separating behavior, a discontinuity is imposed at the interface, and a subsequent strain mismatch will give rise to stress concentration at the interface region [16]. Phase field modeling as one of the most prominent approaches for the simulation of microstructure evolution is introduced as an alternative to sharp-interface modeling. PFM is based on the thermodynamic description of non-equilibrium states in materials including interfaces and

---

E-mail address: masoudahmadi@msc.guilan.ac.ir.

https://doi.org/10.1016/j.commatsci.2020.109879
Received 2 April 2020; Received in revised form 11 June 2020; Accepted 12 June 2020
0927-0256/ © 2020 Elsevier B.V. All rights reserved.

![](./images/812596902225772545_1.jpg)
![](./images/812596902225772545_2.jpg)
![](./images/812596902225772545_3.jpg)

### Nomenclature

| Symbol | Definition |
|--------|------------|
| $\bar{\sigma}_1$ | Largest principal value of the effective stresses |
| $\bar{f}$ | Integral term of $F$ |
| $\beta$ | A constant scalar |
| $\boldsymbol{D}$ | Damping matrix |
| $\boldsymbol{K}$ | Tangential stiffness matrix |
| $\boldsymbol{R}$ | Nodal residual vector |
| $\boldsymbol{u}$ | Displacement field |
| $\boldsymbol{\sigma}$ | Cauchy stress tensor/vector |
| $\boldsymbol{\varepsilon}$ | Infinitesimal Strain tensor/vector |
| $\boldsymbol{\varepsilon}_c$ | Chemical strain tensor |
| $\boldsymbol{\varepsilon}_e$ | Elastic strain tensor |
| $\boldsymbol{B}_\phi^I$ | Cartesian derivative matrix |
| $\boldsymbol{B}_c^I$ | Cartesian derivative matrix |
| $\boldsymbol{B}_u^I$ | Usual strain matrix |
| $\boldsymbol{D}_1$ | 2D elasticity matrix |
| $\boldsymbol{D}_2$ | A constant vector |
| $\boldsymbol{D}_3$ | A constant vector |
| $\boldsymbol{Q}$ | Field variables vector |
| $\cdot$ | Dot product |
| $\chi$ | Relaxation constant of the fracture order |
| $\dot{\square}$ | Second material time derivative |
| $\Delta$ | Increment |
| $\delta$ | Variation operator |
| $\square$ | First material time derivative |
| $\eta$ | Threshold stiffness parameter for a fully broken region |
| $\eta_\phi$ | Test function for $\phi$ |
| $\eta_c$ | Test function for $c$ |
| $\eta_{\boldsymbol{u}}$ | Test function for $\boldsymbol{u}$ |
| $D_4$ | A constant scalar |
| $\langle\square\rangle$ | Macaulay brackets |
| $\ln$ | Natural logarithm |
| $\mathbb{D}$ | Fourth-order stiffness tensor |
| $\mu_0$ | Standard chemical potential |
| $\nabla$ | Nabla operator |
| $\nu$ | Poisson's ratio |
| $\Omega$ | Partial molar volume |
| $\partial$ | Partial differential operator |
| $\phi$ | Fracture order field |
| $\sigma_p$ | Hydrostatic stress |
| $\square^T$ | Transpose of a matrix |
| $\boldsymbol{J}$ | Ion flux vector |
| $\mathrm{d}$ | Total differential operator |
| $\xi_u$ | Elastic energy density function |
| $\xi_u^+$ | Tension part of the elastic energy density function |
| $\xi_u^-$ | Compression part of the elastic energy density function |
| $c$ | Li concentration field |
| $a$ | Initial crack length |
| $c_0$ | Initial Li concentration |
| $c_{\text{max}}$ | Maximum Li concentration |
| $\gamma$ | A constant scalar |
| $E$ | Young's modulus |
| $F$ | Total free energy |
| $f_\phi$ | Local free energy density of $\phi$ |
| $f_u$ | Local free energy density of $\boldsymbol{u}$ |
| $f_c$ | Local free energy density of $c$ |
| $g'(\phi)$ | Derivative of energetic degradation function with respect to $\phi$ |
| $g(\phi)$ | Energetic degradation function |
| $G_{\text{cr}}$ | Critical energy release rate |
| $h$ | Thickness of NW electrode |
| $I$ | Node index |
| $i$ | Newton iteration index |
| $k_\phi$ | Gradient energy coefficient of $\phi$ |
| $k_B$ | Boltzmann constant |
| $l_0$ | Regularization constant |
| $M$ | Molecular mobility |
| $m$ | Number of nodes of each element |
| $n$ | Time step index |
| $N^I$ | Nodal values of shape functions |
| $N_A$ | Avogadro's constant |
| $R$ | Radius of NW electrode |
| $T$ | Absolute temperature |
| $t$ | Time |
| $\mathbf{I}$ | Second-order unit tensor |
| $V$ | Volume |
| $k_c$ | Gradient energy coefficient of $c$ |

is formulated as a state variable in space and time, the evolution of which controls the pathway towards equilibrium [17]. Phase field fracture models were developed by regularizing the sharp crack topology by a diffuse damage band through the introduction of phase field parameter that discriminate the intact and broken material [18-24]. Phase field fracture models have been employed in order to investigate the fracture behavior of the electrodes in LIBs during lithiation/delithiation process. Zuo and Zhao [7] developed a PFM coupling Li diffusion and stress evolution with crack propagation to investigate the behavior of Si thin film electrodes. Miehe et al. [25] studied chemo-mechanical induced fracture in LIBs by PF fracture modeling. Zuo et al. [26] proposed a PFM coupling Li diffusion, finite deformation, stress evolutions with crack propagation to study spherical Si electrodes in LIBs. Guan et al. [27] studied the stress evolution and crack propagation in the solid electrolyte interface (SEI) layer formed on the $\text{LiMn}_2\text{O}_4$ electrode during the Li-ion diffusion by using a PFM. The Cahn-Hilliard PFM was used by Wang er al. [28] to study the SEI thickness of LIB in the initial charge-discharge cycle.

In the isotropic PF fracture models, cracking may arise in regions under compression, thus leading to unphysical crack growth patterns. All the PF fracture models that have been discussed yet are isotropic models. In order to prevent cracking under compressive load states, a tension/compression split of the strain energy is proposed in the so-called anisotropic models [29,30]. In some PF simulations of lithiation induced stress and fracture in electrode particles in the literature such as [31-37], the split of the strain energy into tensile and compressive parts is considered. By using PFM of fracture coupled with anisotropic Cahn-Hilliard-type diffusion, Zhao et al. [31] investigated the electrochemical reaction in LIBs. A chemo-mechanical coupled computational framework was formulated by Zhang et al. [32] to model diffusion induced large plastic deformation and PF fracture of Si electrodes. Klinsmann et al. developed a coupled model of Li diffusion, mechanical stress and crack growth, that uses a PF method for the fracture to investigate crack growth in $\text{LiMn}_2\text{O}_4$ spherical and cylindrical particles during Li extraction [33] and insertion[34] in the first half cycle and in the 2nd half cycle [35]. Xu et al. [36] investigated the fracture behavior of cylinder electrode particles by using a finite strain PF fracture model, in which phase segregation and electrochemical reaction on both particle surfaces and fracture surfaces have been taken into account. Nguyen et al. [37] developed a new formulation based on the PF method for modeling stress corrosion cracking induced by anodic dissolution. They coupled classical phase transition model for material dissolution with the mechanical problem and applied their model to an aluminum alloy in a saline medium.

From the computational viewpoint, anisotropic models are significantly more expensive than the isotropic ones, since the tension/compression split of the strain energy leads to nonlinear balance of momentum equations [38]. To overcome this issue, the so-called hybrid PFM has been proposed in recent years [39,40,38,41]. The hybrid formulation formally comprises features from both the isotropic and anisotropic models [38]. In this paper, the author proposes a FE-based hybrid PF model to study the fracture behavior of electrode particle in LIBs during lithiation. The proposed model with coupling effects among Li diffusion, stress evolution and crack propagation, enables a significant reduction of computational cost in comparison with the available anisotropic models.

## 2. Phase field model

In this section, a PF model with hybrid formulation based on the total free energy of the system is developed, which is characterized by elastic deformation, Li concentration and crack propagation.

### 2.1. Free energy functional

The total free energy of the system is formulated as a functional of the parameters, $\boldsymbol{u}$, $c$ and $\phi$ [26]

$$
F=\int\left(f_{u}+f_{c}+f_{\phi}+\frac{1}{2} k_{c}(\nabla c)^{2}+\frac{1}{2} k_{\phi}(\nabla \phi)^{2}\right) \mathrm{d} V,
\tag{1}
$$

where $f_{u}, f_{c}$ and $f_{\phi}$ are the local free energy densities of the displacement field $\boldsymbol{u}$, Li concentration field $c$ and fracture order field $\phi$, and $\nabla c$ and $\nabla \phi$ are the gradients of concentration and fracture respectively. Also, $k_{c}$ and $k_{\phi}$ represent the gradient energy coefficients.

Considering the coupling between the elastic field and the fracture field, $f_{u}$ is described as follows

$$
f_{u}=\frac{1}{2} g(\phi) \boldsymbol{\sigma}: \boldsymbol{\varepsilon}=g(\phi) \xi_{u},
\tag{2}
$$

where $\xi_{u}=\frac{1}{2} \boldsymbol{\sigma}: \boldsymbol{\varepsilon}$ indicates the elastic energy density function, $\boldsymbol{\sigma}$ denotes the Cauchy stress tensor and $\boldsymbol{\varepsilon}$ is the infinitesimal strain tensor which is given by

$$
\boldsymbol{\varepsilon}=\frac{1}{2}\left(\nabla \boldsymbol{u}+(\nabla \boldsymbol{u})^{T}\right).
\tag{3}
$$

The energetic degradation function $g(\phi)$ couples the elastic field and fracture order parameter by considering the stiffness loss between an intact $(\phi=1)$ and a fully broken region $(\phi=0)$. The $g(\phi)$ has to be monotonically decreasing and also satisfies $g(0)=0, g(1)=1$, and $\partial g(0) / \partial \phi=0$. Herein, the fourth quartic polynomial function $g(\phi)=4 \phi^{3}-3 \phi^{4}+\eta$ is chosen from the several available degradation functions in the literature [38,42]. The parameter $\eta$ is a residual stiffness for a fully broken region and its value may not be too small because of stability issues [43]. The influence of the concentration field on the elastic field is modeled in analogy to thermal effects [44,45]. Therefore, the total infinitesimal strain in the material is decomposed into chemical and elastic parts as

$$
\boldsymbol{\varepsilon}=\boldsymbol{\varepsilon}_{e}+\boldsymbol{\varepsilon}_{c},
\tag{4}
$$

where $\boldsymbol{\varepsilon}_{e}$ is the elastic strain and $\boldsymbol{\varepsilon}_{c}$ is the chemical strain which is assumed as a hydrostatic dilatation as $\boldsymbol{\varepsilon}_{c}=(\Omega c) / 3 \mathbf{I}$, where $\Omega$ is the partial molar volume and $\mathbf{I}$ is the second-order unit tensor. The constitutive equation for the mechanical stresses is given by

$$
\boldsymbol{\sigma}=\mathbb{D}: \boldsymbol{\varepsilon}_{e}=\mathbb{D}:\left(\boldsymbol{\varepsilon}-c \frac{\Omega}{3} \mathbf{I}\right).
\tag{5}
$$

Therein, $\mathbb{D}$ is the fourth-order stiffness tensor.

In general, $f_{c}$ is modeled by a regular solution model [46] or an ideal solution model [47]. Here, for $f_{c}$ it holds [47]

$$
\frac{\partial f_{c}}{\partial c}=\mu_{0}+N_{A} k_{B} T c_{\text {max }} \operatorname{lnc},
\tag{6}
$$

where the constant parameter $\mu_{0}$, is the standard chemical potential, $N_{A}$ is Avogadro's constant, $k_{B}$ is the Boltzmann constant, $c_{\text {max }}$ is the maximum Li concentration, and $T$ is the absolute temperature.

From the $[30,48], f_{\phi}$ is modeled as follows

$$
f_{\phi}=\frac{G_{\text {cr }}}{2 l_{0}}(1-\phi)^{2},
\tag{7}
$$

where, $G_{\text {cr }}$ is the critical energy release rate and $l_{0}$ controls the width of the transition area between the unbroken and the broken region. Also, the $k_{\phi}$ parameter in Eq. (1), is assumed to be $k_{\phi}=G_{\text {cr }} l_{0}$. With regard to a better understanding of $l_{0}$, consider an axial bar of infinite length in which a 1-D crack at $x=0$ is defined by

$$
\phi(x)=1-\exp \left(-\frac{|x|}{l_{0}}\right),
\tag{8}
$$

which satisfies $\phi=0$ at $x=0$ and $\phi=1$ at the limit $x \rightarrow \infty$. Fig. 1 illustrates how the width of the transition area is controlled by $l_{0}$ for a fully developed crack in a 1-D bar. The limit $l_{0} \rightarrow 0$ represents a discontinuous function which is 1 at $x=0$ and 0 elsewhere. For more details about the regularisation of the sharp crack topology, see [30,49,50]

In the present multi-field modeling, the following coupling effects are considered:

- Li diffusion affects elastic field by the chemical strain $\varepsilon_{c}$.
- Fracture affects elastic field by the energetic degradation function $g(\phi)$.

It should be noted that no direct coupling between Li concentration and fracture is considered in this model. Nevertheless, the coupling effects among Li diffusion, elastic field and crack propagation are captured via bridging interactions, i.e. Li concentration can cause elastic deformation which can lead to crack propagation.

### 2.2. Strong form of equations

For each variation of (1) the Cahn-Hilliard equation and the Ginzburg-Landau equation can be derived through a variational method [51]. Due to the characteristic time of the elastic field being far less than the concentration field and fracture field, the evolution equation of displacement is assumed to be quasi-static. The governing equations of the system are derived by solving the Ginzburg-Landau equations for the evolution of locally non-conserved parameters $\boldsymbol{u}$ and $\phi$, and the Cahn-Hilliard equation for the evolution of locally conserved parameter $c$, [7]

$$
\frac{\partial \boldsymbol{u}}{\partial t}=-\frac{\delta F}{\delta \boldsymbol{u}}=\nabla \frac{\partial \bar{f}}{\partial(\nabla \boldsymbol{u})}-\frac{\partial \bar{f}}{\partial \boldsymbol{u}}=0,
\tag{9}
$$

$$
\frac{\partial \phi}{\partial t}=-\chi \frac{\delta F}{\delta \phi}=\chi\left(\nabla \frac{\partial \bar{f}}{\partial(\nabla \phi)}-\frac{\partial \bar{f}}{\partial \phi}\right),
\tag{10}
$$

$$
\frac{\partial c}{\partial t}=\nabla M \nabla\left(\frac{\delta F}{\delta c}\right),
\tag{11}
$$

where $\bar{f}$ is the integral term of the total free energy of the system in (1), and $M$ and $\chi$ are molecular mobility and relaxation constant of the fracture order filed respectively.

Eq. (9) is the balance of linear momentum which can be written explicitly as

$$
\nabla \cdot(g(\phi) \boldsymbol{\sigma})=0.
\tag{12}
$$

According to (1) and (6), (11) finally yields the mass conservation equation which can be written explicitly as follows

$$
\frac{\partial c}{\partial t}+\nabla \cdot \mathbf{J}=0,
\tag{13}
$$

where $\mathbf{J}$ is the ion flux vector given by

$$
\mathbf{J}=-M k_{B} T\left[\nabla c-\left(\frac{\Omega}{N_{A} K_{B} T}\right) c \nabla\left(g(\phi) \sigma_{p}\right)\right],
\tag{14}
$$

with hydrostatic stress $\sigma_{p}$, in turn defined by

$$
\sigma_{p}=\frac{1}{3} \boldsymbol{\sigma}: \mathbf{I}.
\tag{15}
$$

So, the evolution of the Li concentration can be written in a more convenient form by inserting (14) into (13) as [7]

$$
\begin{aligned}
\frac{\partial c}{\partial t} & -M k_{B} T \nabla^{2} c+\frac{M c k_{c}}{N_{A} c_{\max }} \nabla^{4} c+\frac{M k_{c}}{N_{A} c_{\max }} \nabla \nabla^{2} c \cdot \nabla c+\frac{M c \Omega}{N_{A}} \nabla^{2} \\
& \left(g(\phi) \sigma_{p}\right)+\frac{M \Omega}{N_{A}} \nabla c \cdot \nabla\left(g(\phi) \sigma_{p}\right)=0.
\end{aligned}
\tag{16}
$$

Following [52,7], for convenience in the numerical simulations, the fourth order terms in (16) are neglected in numerical study in Section 3.

By inserting Eq. (1) and (7) to Eq. (10), the crack propagation equation becomes

$$
\frac{1}{\chi} \frac{\partial \phi}{\partial t}+G_{\mathrm{cr}} l_{0} \nabla^{2} \phi+\frac{G_{\mathrm{cr}}}{l_{0}}(1-\phi)-g^{\prime}(\phi) \xi_{u}=0.
\tag{17}
$$

The $g^{\prime}(\phi)$ is the derivative of energetic degradation function with respect to $\phi$.

Eqs. (12), (16) and (17) are the strong form of governing equations of the electrode for isotropic PF model.

### 2.3. Hybrid formulations

The isotropic models allow for cracking in regions under compression and interpenetration of the crack faces, hence it yields physically unrealistic crack evolution patterns. To address this issue, the anisotropic models suggest a tension/compression split of elastic energy density function, i.e.,

$$
f_{u}=g(\phi) \xi_{u}^{+}+\xi_{u}^{-},
\tag{18}
$$

such that (17) turns into

$$
\frac{1}{\chi} \frac{\partial \phi}{\partial t}+G_{\mathrm{cr}} l_{0} \nabla^{2} \phi+\frac{G_{\mathrm{cr}}}{l_{0}}(1-\phi)-g^{\prime}(\phi) \xi_{u}^{+}=0,
\tag{19}
$$

where the energetic degradation function $g(\phi)$ is only applied to the tension part of the elastic energy density function.

Although the anisotropic formulation prevent crack growth in compressive regions, it leads to nonlinear balance of momentum equations, hence makes the numerical treatment more expensive [38]. The general idea of hybrid (isotropic-anisotropic) formulation is to retain a linear momentum balance equation and also prevent crack growth in regions under compressive load states. To this end, the not separated form of $f_{u}$ in (2) is kept from isotropic model, while (17) is replaced by (19) from anisotropic model which contains tension part of the elastic energy density. Therefore, Eqs. (12), (16) and (19) are the complete set of governing equations for hybrid PF model. The only seeming disadvantage of the hybrid formulation is that it is variationally inconsistent [38], however, it does not violate the second law of thermodynamics [53].

The tension part of the elastic energy density function, $\xi_{u}^{+}$is given by [53]

$$
\xi_{u}^{+}=\frac{1}{2 E}\left\langle\bar{\sigma}_{1}\right\rangle^{2},
\tag{20}
$$

where $E$ is Young's modulus, $\bar{\sigma}_{1}$ denotes the largest principal value of the effective stresses which is described in A, and Macaulay brackets $\langle\square\rangle$ are defined as $\langle x\rangle=\max \{x, 0\}$.

### 2.4. Weak form of equations

Utilizing the tests functions $\eta_{c}$ for $c, \eta_{\phi}$ for $\phi, \eta_{u}$ for $\boldsymbol{u}$, and integrate over the domain, results in the weak forms of (12), (16) and (19) as

$$
\int_{V} \nabla \eta_{u}:(g(\phi) \boldsymbol{\sigma}) \mathrm{d} V=0,
\tag{21}
$$

$$
\begin{aligned}
& \int_{V} \dot{c} \eta_{c} \mathrm{~d} V+\int_{V}\left(M k_{B} T\right) \nabla c \cdot \nabla \eta_{c} \mathrm{~d} V-\int_{V}\left(\frac{M c \Omega}{N_{A}}\right) \nabla\left(g(\phi) \sigma_{p}\right) \cdot \nabla \eta_{c} \mathrm{~d} V \\
& =0,
\end{aligned}
\tag{22}
$$

$$
\begin{aligned}
& \int_{V} \frac{1}{\chi} \dot{\phi} \eta_{\phi} \mathrm{d} V+\int_{V} G_{\mathrm{cr}} l_{0} \nabla \phi \cdot \nabla \eta_{\phi} \mathrm{d} V-\int_{V} \frac{G_{\mathrm{cr}}}{l_{0}}(1-\phi) \eta_{\phi} \mathrm{d} V+\int_{V} g \\
& \quad{ }^{\prime}(\phi) \xi_{u}^{+} \eta_{\phi} \mathrm{d} V=0,
\end{aligned}
\tag{23}
$$

where $\dot{c}$ and $\dot{\phi}$ are the material time derivative of the Li concentration field and fracture order parameter respectively. It should be noted that, the external nodal forces applied on the electrode boundaries are considered in the global residual vector by means of the FE code.

## 3. Finite element implementation

In the implementation of numerical method, matrix-vector notation is more convenient than tensor notation. Hence, we switch to the matrix-vector notation for the rest of this paper. In matrix-vector notation, a second-order symmetric tensor is expressed using a vector, while a fourth-order symmetric tensor is expressed using a matrix.

Since the numerical example considered in the present work can be accurately and effectively be treated by a two-dimensional plane strain model. So, the $\boldsymbol{\sigma}, \varepsilon$ and $\boldsymbol{u}$ from (5) and (3) are defined in vector form as

$$
\boldsymbol{\sigma}=\left[\sigma_{x x}, \sigma_{y y}, \sigma_{x y}\right]^{T}, \quad \boldsymbol{\varepsilon}=\left[\varepsilon_{x x}, \varepsilon_{y y}, 2 \varepsilon_{x y}\right]^{T}, \quad \boldsymbol{u}=\left[u_{x}, u_{y}\right]^{T}.
\tag{24}
$$

### 3.1. Spatial discretisation

By taking nodal variables as $\boldsymbol{u}, c$ and $\phi$, and utilizing the element shape functions, (21), (22) and (23) are discretized by isoparametric elements

$$
\boldsymbol{u}=\sum_{I}^{m} N^{I} \boldsymbol{u}^{I}, \quad \boldsymbol{\varepsilon}=\sum_{I}^{m} \boldsymbol{B}_{u}^{I} \boldsymbol{u}^{I},
\tag{25}
$$

$$
c=\sum_{I}^{m} N^{I} c^{I}, \quad \nabla c=\sum_{I}^{m} \boldsymbol{B}_{c}^{I} c^{I},
\tag{26}
$$

$$
\phi=\sum_{I}^{m} N^{I} \phi^{I}, \quad \nabla \phi=\sum_{I}^{m} \boldsymbol{B}_{\phi}^{I} \phi^{I},
\tag{27}
$$

where $m$ is the number of nodes of each element and $N^{I}$ is the nodal values of shape functions. The $\boldsymbol{B}_{u}^{I}$ is the usual strain matrix, and $\boldsymbol{B}_{c}^{I}$ and $\boldsymbol{B}_{\phi}^{I}$ are the Cartesian derivative matrices, which are expressed as

$$
\boldsymbol{B}_{u}^{I}=\left[\begin{array}{cc}
\frac{\partial N^{I}}{\partial x} & 0 \\
0 & \frac{\partial N^{I}}{\partial y} \\
\frac{\partial N^{I}}{\partial y} & \frac{\partial N^{I}}{\partial x}
\end{array}\right], \quad \boldsymbol{B}_{c}^{I}=\boldsymbol{B}_{\phi}^{I}=\left[\begin{array}{c}
\frac{\partial N^{I}}{\partial x} \\
\frac{\partial N^{I}}{\partial y}
\end{array}\right].
\tag{28}
$$

Without losing the generality of formulation, test functions can be expressed as the variations of different fields, namely

$$
\eta_{u}=\sum_{I}^{m} N^{I} \delta \boldsymbol{u}^{I}, \quad \nabla \eta_{u}=\sum_{I}^{m} \boldsymbol{B}_{u}^{I} \delta \boldsymbol{u}^{I},
\tag{29}
$$

$$
\eta_{c}=\sum_{I}^{m} N^{I} \delta c^{I}, \quad \nabla \eta_{c}=\sum_{I}^{m} \boldsymbol{B}_{c}^{I} \delta c^{I},
\tag{30}
$$

![](./images/812596902225772545_4.jpg)

Fig. 1. Diffusive crack modeling of a 1-D crack for different values of $l_0$.

$$
\begin{aligned}
K_{c c}^{I J}= & \frac{\partial P_{c}^{I}}{\partial c^{J}}=\int_{V}\left(M k_{B} \mathrm{~T}\right)\left(\boldsymbol{B}_{c}^{I}\right)^{T} \boldsymbol{B}_{c}^{J} \mathrm{~d} V \\
& -\int_{V}\left(\frac{M \Omega}{N_{A}}\right)\left(\boldsymbol{B}_{c}^{I}\right)^{T} \nabla\left(g(\phi) \sigma_{p}\right) N^{J} \mathrm{~d} V \\
- & \int_{V}\left(\frac{M \Omega}{N_{A}}\right)\left(\boldsymbol{B}_{c}^{I}\right)^{T}\left[g(\phi)\left(\frac{1}{3} \mathrm{D}_{4} \boldsymbol{B}_{c}^{J}\right)\right. \\
& \left.+\left(12 \phi^{2}(1-\phi) \nabla \phi\right)\left(\frac{1}{3} \mathrm{D}_{4} N^{J}\right)\right] c \mathrm{~d} V,
\end{aligned}
\label{eq50e}
$$

$$
\begin{aligned}
K_{c \phi}^{I J} & =\frac{\partial P_{c}^{I}}{\partial \phi^{J}} \\
& =\int_{V}\left(\frac{M \Omega}{N_{A}}\right)\left(\boldsymbol{B}_{c}^{I}\right)^{T}\left[g^{\prime}(\phi) \nabla \sigma_{p}+\sigma_{p}\left(12 \phi^{2}(1-\phi) \boldsymbol{B}_{\phi}^{J}+6 \phi(4+6 \phi)\right.\right. \\
& \left.\left.\nabla \phi N^{J}\right)\right] c \mathrm{~d} V,
\end{aligned}
\label{eq50f}
$$

$$
\boldsymbol{K}_{\phi \boldsymbol{u}}^{I J}=\frac{\partial P_{\phi}^{I}}{\partial \boldsymbol{u}^{J}}=\int_{V} N^{I}\left(\frac{\partial\left(g^{\prime}(\phi) \xi_{u}^{+}\right)}{\partial \boldsymbol{u}}\right) \mathrm{d} V,
\label{eq50g}
$$

$$
K_{\phi c}^{I J}=\frac{\partial P_{\phi}^{I}}{\partial c^{J}}=\int_{V} N^{I}\left(\frac{\partial\left(g^{\prime}(\phi) \xi_{u}^{+}\right)}{\partial c}\right) \mathrm{d} V,
\label{eq50h}
$$

$$
K_{\phi \phi}^{I J}=\frac{\partial P_{\phi}^{I}}{\partial \phi^{J}}=\int_{V} G_{\mathrm{cr}} l_{0}\left(\boldsymbol{B}_{\phi}^{I}\right)^{T} \boldsymbol{B}_{\phi}^{J} \mathrm{~d} V+\int_{V} N^{I}\left(\frac{G_{\mathrm{cr}}}{l_{0}}+g^{\prime \prime}(\phi) \xi_{u}^{+}\right) N^{J} \mathrm{~d} V.
\label{eq50i}
$$

For calculating $\partial(g'(\phi)\xi_u^+)/\partial \boldsymbol{u}$ and $\partial(g'(\phi)\xi_u^+)/\partial c$ in 50 g and 50 h, the readers are referred to B. The nodal contributions to the $\boldsymbol{D}^{IJ}$ matrix result from

$$
D_{c c}^{I J}=\frac{\partial C_{c}^{I}}{\partial c^{J}}=\int_{V} N^{I} N^{J} \mathrm{~d} V,
\label{eq51a}
$$

$$
D_{\phi \phi}^{I J}=\frac{\partial C_{\phi}^{I}}{\partial \phi^{J}}=\int_{V} \frac{1}{\chi} N^{I} N^{J} \mathrm{~d} V.
\label{eq51b}
$$

After forming element stiffness, damping and residuals, they are assembled into the global stiffness matrix, damping matrix and the right-hand side vector. The resulting set of nonlinear equation have been implemented in Matlab. The implementation of the isotropic model is presented in C.

### 3.4. Irreversibility constraints

Crack propagation is an irreversible process. However, the system of equations does not guarantee the irreversible evolution of non-conserved PF fracture field, where crack healing is possible. To prevent crack from healing, irreversibility constraints are considered. Miehe et al. [30,48] proposed a local history field of the maximum tension part of the elastic energy density function, which automatically deals with the irreversibility conditions. Nevertheless, this irreversibility condition cannot be used in the present PFM since the boundedness cannot be guaranteed for non-quadratic energetic degradation functions. Herein, a damage like formulation is utilized, where $\Delta \phi=-\langle-\Delta \phi\rangle$ ensures the irreversibility constraint.

## 4. Numerical example

To study the crack propagation under diffusion, the hybrid and also isotropic PF simulation of a Si NW electrode is explored. Two-dimensional circular plate is considered for modeling the cross section of NW electrode as shown in Fig. 2. The radius of the circle plate is equal to $R=60 \mathrm{~nm}$ and its thickness is $h=3 \mu \mathrm{m}$ [57,58]. Also, there is an initial crack with a length of $a$, which is located in the center of the specimen plate. The plane strain assumption is conducted and the edges of the models are free from any displacement constraints. As shown a constant Li concentration, $c_{\max }=88.67 \mathrm{Kmol} / \mathrm{m}^{3}$ [8] is applied on boundaries of the electrode. Also, the initial value of concentration in the inner part of electrode is $c_{0}=c(t=0)=1.0 \mathrm{Kmol} / \mathrm{m}^{3}$ [52]. As the time progresses, Li-ions start to diffuse from outer boundaries into the inner region of the electrode particle.

The material properties of Si electrode [52,59-61] are listed in Table 1. Unless otherwise stated, the fracture properties are set to be $G_{\mathrm{cr}}=7 \mathrm{~N} / \mathrm{m}$ and $l_{0}=10 \mathrm{~nm}$, and the length of pre-existing crack is considered to be $a=60 \mathrm{~nm}$.

### 4.1. Concentration-dependent elastic properties

Elastic properties of Li-Si alloys strongly depend on the Li concentration [31,62]. Herein, based on a linear rule of mixtures, $E=E_{\mathrm{Li}-\mathrm{Si}}+\left(1-c / c_{\max }\right)\left(E_{\mathrm{Si}}-E_{\mathrm{Li}-\mathrm{Si}}\right)$, the dependency of Young's modulus on concentration of lithiated Si is considered. Also, with a similar relationship, $\nu=\nu_{\mathrm{Li}-\mathrm{Si}}+\left(1-c / c_{\max }\right)\left(\nu_{\mathrm{Si}}-\nu_{\mathrm{Li}-\mathrm{Si}}\right)$, the dependency of Poisson's ratio on Li concentration is considered.

### 4.2. Mesh and time step convergence

Choosing a suitable mesh size is critical to obtain sound results at low cost and appropriate time span. For meshing the model, 4-node isoparametric quadrilateral elements with the refined mesh around the vicinity of the crack are employed. Elaborate mesh convergence analyses are conducted to ensure the full convergence of nonlinear FE solution. The meshed shape of the NW cross section plate is shown in Fig. 3. Besides, time step convergence analyses show that for

![](./images/812596902225772545_5.jpg)

Fig. 2. Geometry of and loading conditions on the NW cross section plate.

<table><caption>Table 1 Material properties of Si electrode [52,59–61].</caption>
<thead>
<tr>
<th>Parameter</th>
<th>Symbol</th>
<th>Value</th>
<th>Unit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Young's modulus of Si</td>
<td>$E_{Si}$</td>
<td>80</td>
<td>GPa</td>
</tr>
<tr>
<td>Poisson's ratio of Si</td>
<td>$v_{Si}$</td>
<td>0.22</td>
<td>-</td>
</tr>
<tr>
<td>Young's modulus of Li–Si</td>
<td>$E_{Li-Si}$</td>
<td>41</td>
<td>GPa</td>
</tr>
<tr>
<td>Poisson's ratio of Li–Si</td>
<td>$v_{Li-Si}$</td>
<td>0.24</td>
<td>-</td>
</tr>
<tr>
<td>Partial molar volume</td>
<td>$\Omega$</td>
<td>$8.5×10^{-6}$</td>
<td>m³/mol</td>
</tr>
<tr>
<td>Molecular mobility</td>
<td>$M$</td>
<td>500</td>
<td>m²/Js</td>
</tr>
<tr>
<td>Boltzmann constant</td>
<td>$k_{B}$</td>
<td>$1.38×10^{-23}$</td>
<td>J/K</td>
</tr>
<tr>
<td>Absolute temperature</td>
<td>$T$</td>
<td>298.15</td>
<td>K</td>
</tr>
<tr>
<td>Avogadro's constant</td>
<td>$N_{A}$</td>
<td>$6.02×10^{23}$</td>
<td>1/mol</td>
</tr>
<tr>
<td>Relaxation constant</td>
<td>$\chi$</td>
<td>$1.25×10^{-10}$</td>
<td>m³/Js</td>
</tr>
<tr>
<td>Critical energy release rate</td>
<td>$G_{cr}$</td>
<td>$2.4-14.9$</td>
<td>N/m</td>
</tr>
<tr>
<td>Length parameter for crack</td>
<td>$l_{0}$</td>
<td>$5-30$</td>
<td>nm</td>
</tr>
</tbody>
</table>

$\Delta t \geqslant 0.006$ s the solution process shows divergence and for $\Delta t \leqslant 0.003$ s the results are virtually converged in time. The $\Delta t = 0.0025$ s temporal discretization is selected for the next simulations in the paper.

### 4.3. Effect of initial crack length

The evolutions of $c$ and $g(\phi)\sigma_{p}$ distributions in the electrode during the charging process for the isotropic and hybrid model are depicted in Fig. 4. It can be seen that at the beginning of process, $c$ increases radially from the boundaries into the center of the plate and the interface gradually moves to the center of the NW. As a consequence, volumetric expansion of the electrode is observed which induces stress in the electrode. Despite the NW electrode without a pre-existing crack [63], here the volumetric expansion is not isotropic and the electrode expands more in the direction perpendicular to the crack length. At early stages of lithiation, when higher concentrations are confined to the outer region of the model, the corresponding volume expansion in this region is hindered by the interior domain which causes compressive hydrostatic stress in the outer region and tensile hydrostatic stress in the inner region of the NW. It is also observed that hydrostatic stress concentrates at the vicinity of the initial crack tips, then it reduces by time which makes the crack more stable. The above outcomes are in agreement with the previous studies in [11,26,10,14,15]. In addition, by the arrival of concentration front to the vicinity of the crack tips, the concentration distribution in electrode becomes nonuniform and a very high accumulation of $c$ is observed at the tips. This is mainly because that Li-ions transfer from lower hydrostatic stress regions towards higher hydrostatic stress regions based on (13), which was reported in [7,27,13]. Contrary to the $c$ distribution, the distribution of hydrostatic stress becomes uniformed by time evolution. For comprehensive descriptions on the dynamics of lithiation in Si NW one can refer to [63].

Fig. 4 does not disclose a remarkable distinction between isotropic model and hybrid model for the evolutions of $c$ and $g(\phi)\sigma_{p}$. However, as it was shown, the outer regions of the electrode undergo compressive hydrostatic stress. Therefore, it is expected that when the initial crack grows and the crack tips reach to the regions under compression, hybrid model shows less tendency to crack growth than the isotropic one. Fig. 5 shows the crack propagation during the charging process for isotropic and hybrid models. It is observed that at early stages of the process, both cracks start to propagate with a similar trend. But as predicted, at the final stages, crack growth in the hybrid model is impeded, unlike the isotropic model. Also, the grown crack in the isotropic model is evidently thicker, which indicates that the hybrid model has less crack growth tendency toward outer regions which are under compression. As mentioned before, the presence of a crack at the center of the electrode plate leads to anisotropic expansion. The length of the electrode in $x$ direction at $t = 6$ s is 142.8 nm for the isotropic model and 143.8 nm for the hybrid model, and in $y$ direction is 161.1 nm for the isotropic model and 158.8 nm for the hybrid model. So, the measured values indicate that anisotropic expansion and hence crack growth are more evident in the isotropic model than the hybrid one.

Fig. 6 compares the crack length and crack thickness of NWs with different initial crack lengths for isotropic and hybrid models over the time. Before the start of crack propagation, the crack is compacted due to anisotropic volumetric expansion which causes a small drop of the crack length. This phenomenon is more pronounced for NW electrodes with larger initial crack. In both models, cracks start to propagate with almost a constant slope until reaching certain values. Then the crack growth stops while crack length continues to increase slightly due to the volumetric expansion. The crack growth starts sooner and also ends sooner for the NWs with larger initial cracks. At the $t = 6$ s, the crack lengths are increased 62.77%, 22.79% and 159.30% for isotropic models, and 57.05%, 17.18% and 128.38% for hybrid models, respectively for initial crack lengths of 30 nm, 60 nm and 90 nm. Obviously, the hybrid models show smaller final crack length since they prevent crack growth in compressive regions. The crack lengths for isotropic models at $t = 6$ s are 13.54%, 3.64% and 4.78% bigger than hybrid models for initial lengths of 30 nm, 60 nm, and 90 nm, respectively. Furthermore, Fig. 6(b) shows that cracks get thicker in the isotropic models which also was observed in Fig. 5. It is also revealed that crack thickness increases faster in the models with longer initial cracks.

### 4.4. Effect of fracture properties

The crack length during the lithiation process for two different values of $G_{cr}$ are plotted over the time in Fig. 7(a). Crack propagation in

![](./images/812596902225772545_6.jpg)

Fig. 3. Meshed shape of the NW cross section plate.

![](./images/812596902225772545_7.jpg)

![](./images/812596902225772545_8.jpg)

models with lesser critical energy release rate starts a little sooner and ends later with significantly bigger crack lengths. Furthermore, the effect of $G_{cr}$ on the crack length at $t=5$ s for isotropic and hybrid models is shown in Fig. 7(b). The increase of the critical energy release rate reduces the crack length for both isotropic and hybrid models with a linear pattern, while, as expected, hybrid models show an average of 4.1% less crack length.

Fig. 8(a) illustrates the evolution of crack length versus time for different values of $l_0$. Similar to the critical energy release rate, crack propagation for the models with lesser regularization constant starts sooner and ends later with bigger crack lengths. Also, the increase of $l_0$ reduces the crack length for both isotropic and hybrid models with an exponential pattern, as shown in Fig. 8(b). The isotropic models show 3.74%, 3.69%, 7.19% and 6.53% larger crack length than the hybrid

![](./images/812596902225772545_9.jpg)

Fig. 6. (a) Crack length and (b) crack thickness versus time for isotropic and hybrid models.

models for $l_0=5$ nm, $l_0=10$ nm, $l_0=20$ nm and $l_0=30$ nm, respectively.

## 5. Conclusions

In this contribution, a hybrid phase field model was proposed to investigate the fracture process of electrodes in Li-ion batteries. The framework links Li-ion diffusion, stress evolution and crack propagation. The model takes account of the dependency of Elastic properties on the Li concentration. The variational approach along with the finite element method was conducted to obtain the discretized governing equations of the system on space domain. The model was implemented in MATLAB, and all simulations were performed in the same software. Unlike the traditional isotopic models, the proposed hybrid formulation aims to prevent crack growth in the region under compression. Both isotopic and hybrid models were applied to a silicon nanowire electrode particle, and the effects of different initial crack lengths and fracture properties were investigated. The numerical results shown that the hybrid model shows less tendency to crack growth than the isotropic model. Moreover, the increase of the critical energy release rate and regularization constant reduces the crack length with linear and exponential patterns, respectively. The proposed hybrid model has the potential to assist the understanding of the fracture behavior of Li-ion battery electrodes and provides insightful guidelines for the design of next-generation electrodes in the future. It should be noted that the present work is only a preliminary study, and to demonstrate the capability and potential applicability of the proposed hybrid approach there are still different detailed aspects that must be explored. For example, electrodes with geometrical constraints which undergo huge compressive stresses [32,64], delithiation process of an electrode, in which compressive stress is generated in the inner part of the electrode [36,33,35,65], and electrode with multiple pre-existing cracks [7,13,36,14,25,33]. Besides, different electrode particles with different shapes and sizes must be investigated.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

![](./images/812596902225772545_10.jpg)

Fig. 7. (a) Crack length versus time for different values of $G_{cr}$ and (b) Crack length at $t=5$ s versus $G_c r$.

![](./images/812596902225772545_11.jpg)
![](./images/812596902225772545_12.jpg)

Fig. 8. (a) Crack length versus time for different values of $l_0$ and (b) Crack length at $t = 5$ s versus $l_0$.

## Appendix A. The largest principal value of the effective stresses

The largest principal value of the effective stresses can be obtained by
$$\bar{\sigma}_{1}=\max \left\{\boldsymbol{T}_{1}^{T} \boldsymbol{\sigma}, \boldsymbol{T}_{2}^{T} \boldsymbol{\sigma}\right\},\tag{A.1}$$
where $\boldsymbol{T}_{1}$ and $\boldsymbol{T}_{2}$ are the rotational transformation vectors which are defined as
$$\boldsymbol{T}_{1}=\left[\begin{array}{c}
\cos ^{2} \theta \\
\sin ^{2} \theta \\
2 \sin \theta \cos \theta
\end{array}\right], \quad \boldsymbol{T}_{2}=\left[\begin{array}{c}
\sin ^{2} \theta \\
\cos ^{2} \theta \\
-2 \sin \theta \cos \theta
\end{array}\right],\tag{A.2}$$
and the rotation angle $\theta$ is obtained as follows
$$\tan (2 \theta)=\frac{2 \sigma_{x y}}{\sigma_{x x}-\sigma_{y y}}.\tag{A.3}$$

## Appendix B. Tension part of the elastic energy density function derivatives

Adopting the chain rule of differentiation, the tension part of the elastic energy density function derivatives with respect to $\boldsymbol{u}$ and $c$ respectively are derived as
$$\frac{\partial\left(g^{\prime}(\phi) \xi_{u}^{+}\right)}{\partial \boldsymbol{u}}=\frac{\partial\left(g^{\prime}(\phi) \xi_{u}^{+}\right)}{\partial \boldsymbol{\sigma}} \frac{\partial \boldsymbol{\sigma}}{\partial \boldsymbol{u}}=g^{\prime}(\phi) \frac{\partial\left(\xi_{u}^{+}\right)}{\partial \boldsymbol{\sigma}} \boldsymbol{D}_{1} \boldsymbol{B}_{u}^{J},\tag{B.1}$$

$$\frac{\partial\left(g^{\prime}(\phi) \xi_{u}^{+}\right)}{\partial c}=\frac{\partial\left(g^{\prime}(\phi) \xi_{u}^{+}\right)}{\partial \boldsymbol{\sigma}} \frac{\partial \boldsymbol{\sigma}}{\partial c}=g^{\prime}(\phi) \frac{\partial\left(\xi_{u}^{+}\right)}{\partial \boldsymbol{\sigma}} \boldsymbol{D}_{2} N^{J}.\tag{B.2}$$

From A,
$$\xi_{u}^{+}=\frac{1}{2 E}\left\langle\max \left\{\boldsymbol{T}_{1}^{T} \boldsymbol{\sigma}, \boldsymbol{T}_{2}^{T} \boldsymbol{\sigma}\right\}\right\rangle^{2}.\tag{B.3}$$

Then it obtains as
$$\frac{\partial\left(\xi_{u}^{+}\right)}{\partial \boldsymbol{\sigma}}=\frac{1}{E}\left\langle\max \left\{\boldsymbol{T}_{1}^{T} \boldsymbol{\sigma}, \boldsymbol{T}_{2}^{T} \boldsymbol{\sigma}\right\}\right\rangle\left\langle\frac{\max \left\{\boldsymbol{T}_{1}^{T} \boldsymbol{\sigma}, \boldsymbol{T}_{2}^{T} \boldsymbol{\sigma}\right\}}{\boldsymbol{\sigma}}\right\rangle.\tag{B.4}$$

## Appendix C. Isotropic model implementation

If one continues 17 with $\xi_{u}$, instead of $\xi_{u}^{+}$ in hybrid formulation, one can obtain the isotropic model. Therefore, the FE implantation for isotropic model is the same, except that $R_{\phi}^{I}$ in 47 is changed into
$$R_{\phi}^{I}=\int_{V} G_{\mathrm{cr}} l_{0}\left(\boldsymbol{B}_{\phi}^{I}\right)^{T} \nabla \phi \mathrm{d} V-\int_{V} N^{I}\left(\frac{G_{\mathrm{cr}}}{l_{0}}(1-\phi)-g^{\prime}(\phi) \xi_{u}\right) \mathrm{d} V,\tag{c.1}$$
and, $\boldsymbol{K}_{\phi \boldsymbol{u}}^{I I}, K_{\phi c}^{I I}$ and $K_{\phi \phi}^{I I}$ in 50 are changed into

$$
\boldsymbol{K}_{\phi u}^{I I}=\frac{\partial P_{\phi}^{I}}{\partial \boldsymbol{u}^{J}}=\int_{V} N^{I} g^{\prime}(\phi)\left(\frac{1}{2} \boldsymbol{\varepsilon}^{T} \boldsymbol{D}_{1}+\frac{1}{2} \boldsymbol{\sigma}^{T}\right) \boldsymbol{B}_{u}^{J} \mathrm{~d} V,
\tag{c.2a}
$$

$$
K_{\phi c}^{I I}=\frac{\partial P_{\phi}^{I}}{\partial c^{J}}=\int_{V} N^{I} g^{\prime}(\phi)\left(\frac{1}{2} \boldsymbol{\varepsilon}^{T} \boldsymbol{D}_{2}\right) N^{J} \mathrm{~d} V,
\tag{c.2b}
$$

$$
K_{\phi \phi}^{I I}=\frac{\partial P_{\phi}^{I}}{\partial \phi^{J}}=\int_{V} G_{\mathrm{cr}} l_{0}\left(\boldsymbol{B}_{\phi}^{I}\right)^{T} \boldsymbol{B}_{\phi}^{J} \mathrm{~d} V+\int_{V} N^{I}\left(\frac{G_{\mathrm{cr}}}{l_{0}}+g^{\prime \prime}(\phi) \xi_{u}\right) N^{J} \mathrm{~d} V.
\tag{c.2c}
$$

## Appendix D. Supplementary data

Supplementary data associated with this article can be found, in the online version, athttps://doi.org/10.1016/j.commatsci.2020.109879.

## References

[1] K.A. Smith, Electrochemical control of lithium-ion batteries, IEEE Control Syst. Mag. 30 (2010) 18-25.

[2] Y. Zhao, P. Stein, Y. Bai, M. Al-Siraj, Y. Yang, B.-X. Xu, A review on modeling of electro-chemo-mechanics in lithium-ion batteries, J. Power Sources 413 (2019) 259-283.

[3] A. Mukhopadhyay, B.W. Sheldon, Deformation and stress in electrode materials for li-ion batteries, Prog. Mater. Sci. 63 (2014) 58-116.

[4] S. Kumar, M. Nehra, D. Kedia, N. Dilbaghi, K. Tankeshwar, K.-H. Kim, Carbon na- notubes: a potential material for energy conversion and storage, Prog. Energy Combust. Sci. 64 (2018) 219-253.

[5] M. Obrovac, L. Christensen, Structural changes in silicon anodes during lithium insertion/extraction, Electrochem. Solid-State Lett. 7 (2004) A93-A96.

[6] M. Ebner, F. Marone, M. Stampanoni, V. Wood, Visualization and quantification of electrochemical and mechanical degradation in li ion batteries, Science 342 (2013) 716-720.

[7] P. Zuo, Y.-P. Zhao, A phase field model coupling lithium diffusion and stress evo- lution with crack propagation and application in lithium ion batteries, Phys. Chem. Chem. Phys. 17 (2015) 287-297.

[8] I. Ryu, J.W. Choi, Y. Cui, W.D. Nix, Size-dependent fracture of si nanowire battery anodes, J. Mech. Phys. Solids 59 (2011) 1717-1730.

[9] R. Grantab, V.B. Shenoy, Pressure-gradient dependent diffusion and crack propa- gation in lithiated silicon nanowires, J. Electrochem. Soc. 159 (2012) A584-A591.

[10] B. Chen, J. Zhou, R. Cai, Analytical model for crack propagation in spherical nano electrodes of lithium-ion batteries, Electrochim. Acta 210 (2016) 7-14.

[11] X. Hu, Y. Zhao, R. Cai, J. Zhou, Surface effected fracture behavior of nano-spherical electrodes during lithiation reaction, Mater. Sci. Eng. A 707 (2017) 92-100.

[12] H. Wang, E. Oterkus, S. Oterkus, Predicting fracture evolution during lithiation process using peridynamics, Eng. Fract. Mech. 192 (2018) 176-191.

[13] H. Wang, E. Oterkus, S. Oterkus, Peridynamic modelling of fracture in marine li- thium-ion batteries, Ocean Eng. 151 (2018) 257-267.

[14] H. Wang, E. Oterkus, S. Oterkus, Three-dimensional peridynamic model for pre- dicting fracture evolution during the lithiation process, Energies 11 (2018) 1461.

[15] Y. Gwak, Y. Jin, M. Cho, Cohesive zone model for crack propagation in crystalline silicon nanowires, J. Mech. Sci. Technol. 32 (2018) 3755-3763.

[16] Y. Hu, X. Zhao, Z. Suo, Averting cracks caused by insertion reaction in lithium-ion batteries, J. Mater. Res. 25 (2010) 1007-1010.

[17] I. Steinbach, Phase-field models in materials science, Model. Simul. Mater. Sci. Eng. 17 (2009) 073001.

[18] B. Bourdin, G.A. Francfort, J.-J. Marigo, Numerical experiments in revisited brittle fracture, J. Mech. Phys. Solids 48 (2000) 797-826.

[19] B. Bourdin, G.A. Francfort, J.-J. Marigo, The variational approach to fracture, J. Elast. 91 (2008) 5-148.

[20] I. Aranson, V. Kalatsky, V. Vinokur, Continuum field description of crack propa- gation, Phys. Rev. Lett. 85 (2000) 118.

[21] A. Karma, D.A. Kessler, H. Levine, Phase-field model of mode iii dynamic fracture, Phys. Rev. Lett. 87 (2001) 045501.

[22] V. Hakim, A. Karma, Laws of crack motion and phase-field models of fracture, J. Mech. Phys. Solids 57 (2009) 342-368.

[23] R. Spatschek, E. Brener, A. Karma, Phase field modeling of crack propagation, Philos. Mag. 91 (2011) 75-95.

[24] X. Lu, C. Li, Y. Tie, Y. Hou, C. Zhang, Crack propagation simulation in brittle elastic materials by a phase field method, Theor. Appl. Mech. Lett. 9 (2019) 339-352.

[25] C. Miehe, H. Dal, L.-M. Schänzel, A. Raina, A phase-field model for chemo-me- chanical induced fracture in lithium-ion battery electrode particles, Int. J. Numer. Methods Eng. 106 (2016) 683-711.

[26] P. Zuo, Y.-P. Zhao, Phase field modeling of lithium diffusion, finite deformation, stress evolution and crack propagation in lithium ion battery, Extreme Mech. Lett. 9 (2016) 467-479.

[27] P. Guan, L. Liu, Y. Gao, Phase-field modeling of solid electrolyte interphase (sei) cracking in lithium batteries, ECS Trans. 85 (2018) 1041-1051.

[28] X. Wang, W. Shen, X. Huang, J. Zang, Y. Zhao, Estimating the thickness of diffusive solid electrolyte interface, Sci. China Phys. Mech. Astron. 60 (2017) 064612.

[29] H. Amor, J.-J. Marigo, C. Maurini, Regularized formulation of the variational brittle fracture with unilateral contact: numerical experiments, J. Mech. Phys. Solids 57 (2009) 1209-1229.

[30] C. Miehe, F. Welschinger, M. Hofacker, Thermodynamically consistent phase-field models of fracture: variational principles and multi-field fe implementations, Int. J. Numer. Methods Eng. 83 (2010) 1273-1311.

[31] Y. Zhao, B.-X. Xu, P. Stein, D. Gross, Phase-field study of electrochemical reactions at exterior and interior interfaces in li-ion battery electrode particles, Comput. Methods Appl. Mech. Eng. 312 (2016) 428-446.

[32] X. Zhang, A. Krischok, C. Linder, A variational framework to model diffusion in- duced large plastic deformation and phase field fracture during initial two-phase lithiation of silicon electrodes, Comput. Methods Appl. Mech. Eng. 312 (2016) 51-77.

[33] M. Klinsmann, D. Rosato, M. Kamlah, R.M. McMeeking, Modeling crack growth during li extraction in storage particles using a fracture phase field approach, J. Electrochem. Soc. 163 (2016) A102-A118.

[34] M. Klinsmann, D. Rosato, M. Kamlah, R.M. McMeeking, Modeling crack growth during li insertion in storage particles using a fracture phase field approach, J. Mech. Phys. Solids 92 (2016) 313-344.

[35] M. Klinsmann, D. Rosato, M. Kamlah, R.M. McMeeking, Modeling crack growth during li extraction and insertion within the second half cycle, J. Power Sources 331 (2016) 32-42.

[36] B.-X. Xu, Y. Zhao, P. Stein, Phase field modeling of electrochemically induced fracture in li-ion battery with large deformation and phase segregation, GAMM- Mitteilungen 39 (2016) 92-109.

[37] T.T. Nguyen, J. Bolivar, Y. Shi, J. Réthoré, A. King, M. Fregonese, J. Adrien, J.- Y. Buffiere, M.-C. Baietto, A phase field method for modeling anodic dissolution induced stress corrosion crack propagation, Corros. Sci. 132 (2018) 146-160.

[38] M. Ambati, T. Gerasimov, L. De Lorenzis, A review on phase-field models of brittle fracture and a new fast hybrid formulation, Comput. Mech. 55 (2015) 383-405.

[39] J.-Y. Wu, A unified phase-field theory for the mechanics of damage and quasi-brittle fracture, J. Mech. Phys. Solids 103 (2017) 72-99.

[40] J.-Y. Wu, A geometrically regularized gradient-damage model with energetic equivalence, Comput. Methods Appl. Mech. Eng. 328 (2018) 612-637.

[41] J.-Y. Wu, V.P. Nguyen, A length scale insensitive phase-field damage model for brittle fracture, J. Mech. Phys. Solids 119 (2018) 20-42.

[42] C. Kuhn, A. Schlüter, R. Müller, On degradation functions in phase field fracture models, Comput. Mater. Sci. 108 (2015) 374-384.

[43] C. Kuhn, R. Müller, A continuum phase field model for fracture, Eng. Fract. Mech. 77 (2010) 3625-3634.

[44] S. Prussin, Generation and distribution of dislocations by solute diffusion, J. Appl. Phys. 32 (1961) 1876-1881.

[45] J.C.-M. Li, Physical chemistry of some microstructural phenomena, Metall. Trans. A 9 (1978) 1353-1380.

[46] G.K. Singh, G. Ceder, M.Z. Bazant, Intercalation dynamics in rechargeable battery materials: General theory and phase-transformation waves in lifepo4, Electrochim. Acta 53 (2008) 7599-7613.

[47] F. Yang, Interaction between diffusion and chemical stresses, Mater. Sci. Eng. A 409 (2005) 153-159.

[48] C. Miehe, M. Hofacker, F. Welschinger, A phase field model for rate-independent crack propagation: robust algorithmic implementation based on operator splits, Comput. Methods Appl. Mech. Eng. 199 (2010) 2765-2778.

[49] X. Zhang, C. Vignes, S.W. Sloan, D. Sheng, Numerical evaluation of the phase-field model for brittle fracture with emphasis on the length scale, Comput. Mech. 59 (2017) 737-752.

[50] A. Egger, U. Pillai, K. Agathos, E. Kakouris, E. Chatzi, I.A. Aschroft, S.P. Triantafyllou, Discrete and phase field methods for linear elastic fracture me- chanics: a comparative study and state-of-the-art review, Appl. Sci. 9 (2019) 2436.

[51] L.-Q. Chen, Phase-field models for microstructure evolution, Annu. Rev. Mater. Res. 32 (2002) 113-140.

[52] Y. Xie, M. Qiu, X. Gao, D. Guan, C. Yuan, Phase field modeling of silicon nanowire based lithium ion battery composite electrode, Electrochim. Acta 186 (2015) 542-551.

[53] J.-Y. Wu, Robust numerical implementation of non-standard phase-field damage models for failure in solids, Comput. Methods Appl. Mech. Eng. 340 (2018) 767-797.

[54] N.M. Newmark, et al., A method of computation for structural dynamics, Am. Soc. Civil Eng. (1959).

[55] P. Wriggers, Nonlinear Finite Element Methods, Springer Science & Business Media,

2008.

[56] O.C. Zienkiewicz, R.L. Taylor, R.L. Taylor, R. Taylor, The Finite Element Method: Solid Mechanics vol. 2, Butterworth-heinemann, 2000.

[57] T. Toriyama, Y. Tanimoto, S. Sugiyama, Single crystal silicon nano-wire piezo- resistors for mechanical sensors, J. Microelectromech. Syst. 11 (2002) 605–611.

[58] Y. Li, P. Gao, Q. Chen, J. Yang, J. Li, D. He, Nanostructured semiconductor solar absorbers with near 100% absorption and related light management picture, J. Phys. D Appl. Phys. 49 (2016) 215104.

[59] M. Pharr, Z. Suo, J.J. Vlassak, Measurements of the fracture energy of lithiated silicon electrodes of li-ion batteries, Nano Lett. 13 (2013) 5570–5577.

[60] L.A. Berla, S.W. Lee, Y. Cui, W.D. Nix, Mechanical behavior of electrochemically lithiated silicon, J. Power Sources 273 (2015) 41–51.

[61] V.B. Shenoy, P. Johari, Y. Qi, Elastic softening of amorphous and crystalline li–si phases with increasing li concentration: a first-principles study, J. Power Sources 195 (2010) 6825–6830.

[62] J. Ratchford, B. Schuster, B. Crawford, C. Lundgren, J. Allen, J. Wolfenstine, Young's modulus of polycrystalline li22si5, J. Power Sources 196 (2011) 7747–7749.

[63] B. Eidel, M. Ahmadi, Insights into the interplay of diffusion and stress in the in- tercalation dynamics of a li-ion battery electrode by phase-field finite element modeling (2020).

[64] S.W. Lee, H.-W. Lee, I. Ryu, W.D. Nix, H. Gao, Y. Cui, Kinetics and fracture re- sistance of lithiated silicon nanostructure pairs controlled by their mechanical in- teraction, Nat. Commun. 6 (2015) 7533.

[65] X.H. Liu, S. Huang, S.T. Picraux, J. Li, T. Zhu, J.Y. Huang, Reversible nanopore formation in ge nanowires during lithiation-delithiation cycling: an in situ trans- mission electron microscopy study, Nano Lett. 11 (2011) 3991–3997.