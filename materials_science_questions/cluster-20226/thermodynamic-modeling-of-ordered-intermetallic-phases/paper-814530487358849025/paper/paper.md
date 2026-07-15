Full length article

# Thermodynamic properties of phase-field models for grain boundary segregation
![](./images/814530487358849025_1.jpg)

Seong Gyoon Kim $^{a, *}$, Jae Sang Lee $^{b}$, Byeong-Joo Lee $^{c}$

$^{a}$ Department of Materials Science and Engineering, Kunsan National University, Kunsan, 573-701, Republic of Korea
$^{b}$ Graduate Institute of Ferrous Technology (GIFT), Pohang University of Science and Technology (POSTECH), Pohang, 790-784, Republic of Korea
$^{c}$ Department of Materials Science and Engineering, Pohang University of Science and Technology (POSTECH), Pohang, 790-784, Republic of Korea

---

### ARTICLE INFO
**Article history:**
Received 22 February 2016
Received in revised form
5 April 2016
Accepted 10 April 2016
Available online 19 April 2016

**Keywords:**
Grain boundary segregation
Phase field model
Grain boundary energy

---

### ABSTRACT
Impurity atoms segregated in grain boundary (GB) regions can dramatically change the physical and chemical properties of the GBs. Such changes often appear to be attributed to the GB energy reduction and/or solute drag effect. Phase-field models have been utilized to clarify both the thermodynamic and kinetic effects of the GB segregation. In this study, we developed phase-field models for GB segregation that are diffuse interface versions of the classical two-phase model of GB segregation. The thermodynamic state at any point in the system is represented as a mixture of a GB phase and a matrix phase. There are two choices for the thermodynamic relation between the GB phase and the matrix phase that constitute the point: the equal composition condition in model I and the equal diffusion potential condition in model II. Most of the previous PFMs for GB segregation appear to be specific cases of model I. We examined the thermodynamic properties of models I and II, and compared them with each other and the classical two-phase model. Although all the models resulted in the same GB composition, the GB energy and its dependency on the composition at the equilibrium state are quite different from each other. In model I, there is a lower bound to the GB energy, which originates from the equal composition condition. The GB energy from model II shows no such lower bound, and it is represented as the vertical distance between the parallel tangent lines on the free energy diagram, as in the classical two-phase model. Nevertheless, the compositional dependence in the model II is quite different from that in the classical two-phase model. This originates from the different choices for the composition-independent parameter in the models: a constant gradient energy coefficient in model II and a constant GB width in the classical two-phase model. Model I is not suitable for simulations of alloys that show a reduction of the GB energy due to GB segregation below a certain limit (in dilute alloys, about half of the GB energy of pure solvents). Model II is a correct choice for such alloys.

© 2016 Published by Elsevier Ltd on behalf of Acta Materialia Inc.

---

## 1. Introduction
Solute atoms often segregate at the grain boundary (GB) region. Even impurities that are hardly detectable in the grain interior region (matrix) can be segregated at the GB region to very high concentrations. This GB segregation can fundamentally alter not only the microscopic GB dynamic [1], but also the macroscopic properties of the materials [2]. A typical example is the extraordinary thermal stability observed in many nanocrystalline materials. In nanocrystalline materials that show high resistance against grain growth, distinct GB segregation has often been observed [3–13]. The solute drag effect on GB motion and/or GB energy reduction due to the GB segregation has been claimed to be one of the causes of the retarded grain growth [9–19]. However, the key mechanism underlying the phenomenon seems to be far from a complete understanding [20–22].

The GB energy reduction, which is a thermodynamic aspect of GB segregation, has been studied using two different methods: the sharp interface and two-phase approaches. In the former approach [1,15–19], which is based on the Gibbs formalism of interface thermodynamics, the GB is regarded as a sharp interface with no finite thickness. In the latter approach [1,23–26], which we call the 'classical two-phase model' hereafter, the GB is regarded as a phase with a finite and constant thickness, and bulk thermodynamics is

* Corresponding author.
E-mail address: sgkim@kunsan.ac.kr (S.G. Kim).

http://dx.doi.org/10.1016/j.actamat.2016.04.028
1359-6454/© 2016 Published by Elsevier Ltd on behalf of Acta Materialia Inc.

applied to find the equilibrium state in the two-phase system of the matrix and GB phases. The study of the solute drag effect, which is a kinetic aspect of GB segregation, also has a long history, starting from Lücke and Detert [27] and Cahn [28]. The diffusional interaction between the moving GBs and the solute atoms to catch up with them gives rise to the drag force on moving GBs. If the solute segregation potential in the GB region and the free energy of the matrix phase are given, the drag force can be found by solving the diffusion equation [1,27–30].

Until late in the 20th century, the thermodynamic and kinetic aspects of GB segregation have been studied quite independently from each other. To correctly understand the thermal behaviors of the materials accompanying GB segregation, however, both aspects of GB segregation must be formulated in a unified way. One such unified approach is the phase-field model (PFM). PFMs [31–36], which were originally developed to simulate the diffusional phase transformation, are composed of two equations: the phase-field and diffusion equations. These two equations govern not only the thermodynamic properties of the system, but also the interaction between the moving interface and the diffusional field. Thus, PFMs for GB migration and grain growth have been developed to include both the thermodynamic and kinetic aspects of the segregation [37–45]. All the PFMs developed for GB segregation have a common ground that the free energy of the system is designed to be decreased for spontaneous segregation. In the details of the models, however, two different approaches have been adopted. In one approach [38–45], which has been employed in most PFMs for GB segregation, the system is assumed to be a single phase in the chemical aspect, but all the grains in the system are regarded as different phases from each other in the crystallographic orientation aspect. In the other approach, which was first developed by Cha et al. [37], the system is assumed to be composed of two phases (matrix phase and GB phase) with different compositions from each other. The GB phase fraction is unity at the center of the GB region, and it changes monotonously from one to zero in the matrix region.

The thermodynamic and kinetic properties of GBs have been examined for both approaches under the assumptions of ideal [40–42], dilute [37] or regular solutions [44]. However, there has not been any detailed examination of the differences in basic properties between the different approaches. In this study, we first develop a generalized two-phase PFM, which is the diffuse interface version of the classical two-phase model of GB segregation. We show that the previous models are specific cases of the two-phase PFM. We then compare the thermodynamic properties of the phase-field models and the classical two-phase model, and clarify where the differences between models come from. The kinetic properties of the models, such as the solute drag force, are also very important. However, even the equilibrium properties show nontrivial behaviors, depending on the models. In this study, therefore, we focus on the equilibrium properties of the models.

This work is organized as follows. In section 2, we briefly review the key concept of the classical two-phase thermodynamic model for GB segregation because it is closely related to the PFMs in this study. In section 3, we formulate a generalized PFM for GB segregation, and models I and II are derived by putting an additional condition on the thermodynamic state for an arbitrary infinitesimal point in the GB region. The GB energy and GB width are obtained for the arbitrary free energy densities of the matrix and GB phases, and the fundamental differences in GB energy among the phase-field models and the classical two-phase model are clarified. In section 4, we explicitly show the differences in the thermodynamic behaviors for specific forms of the free energy density. In the last section 5, we present the parameter fitting for the mesoscale simulation of grain growth with segregation and discuss the segregation induced recrystallization.

If necessary to keep consistency in presentation, we will rederive some of the relevant equations in several parts, but usually in simpler ways than in previous studies [37,41,42,44].

## 2. Classical two-phase model of GB segregation

As shown later, all of the PFMs for GB segregation can be regarded as two-phase models. Therefore, the classical two-phase model [1,23–26] for GB segregation should have close relationships with the PFMs for GB segregation. To clarify this point, we first briefly review the key concept of the classical two-phase model, following Hillert's approach [24]. In the classical model, the GB layer is regarded as a homogeneous volumetric phase with a constant width $2\xi$, belonging to a separate phase from the matrix phase. It is assumed that the GB width is not a thermodynamic variable in a given alloy, but rather a fixed a priori value independent of the solute concentration in the alloy, and the GB energy corresponds to the free energy difference between the GB and matrix phases per unit GB area. If the free energies per unit volume of the GB and matrix phases for the pure A element are given as $f_A^g$ and $f_A^m$, respectively, the GB energy $\sigma_A$ is given by the free energy change when the matrix phase in a volume with a unit area and a width $2\xi$ is transformed into the GB phase with the same volume:

$$
\sigma_A = 2\xi(f_A^g - f_A^m)\equiv2\xi\omega_A, \tag{1}
$$

where we defined

$$
\omega_A = f_A^g - f_A^m, \tag{2}
$$

because this parameter appears frequently throughout this study.

For an alloy at an equilibrium state, the composition of the GB phase and the GB energy change as a function of the matrix composition can be determined as follows. Let us consider a closed system of substitutional A-B alloy that is composed of two grains (matrix phase) and a GB phase with a width $2\xi$ between them. When this system is in an equilibrium state, the total free energy of the system is minimized. Equivalently, in the equilibrium state, all the driving forces for the chemical diffusion and the boundary migration between the matrix and GB phase should vanish. In the present system, the driving force for the phase boundary migration is irrelevant because the width $2\xi$ was assumed to be a fixed value. Thus, the equilibrium state is determined by the vanishing driving force for diffusion only. The driving force of the substitutional diffusion is the gradient of the diffusion potential $\tilde{\mu}$. Here, $\tilde{\mu}\equiv\mu_B - \mu_A$ is the difference between the chemical potential $\mu_B$ of the solute and $\mu_A$ of the solvent. This diffusion potential in phase $p$ is equivalent to the slope $df^p/du$ of the tangent line on the diagram of the free energy $(f^p)$ curve as a function of the solute concentration $u$. Thus, the equilibrium condition for the present system is a constant diffusion potential over the whole space of the system, which results in the same diffusion potential in the matrix phase and GB phase. This can be graphically represented by a parallel tangent construction on the free energy-concentration diagram, as shown in Fig. 1. In this figure, $f^m$ and $f^g$ are the free energy densities of the matrix and GB phases, respectively. $u_m$ and $u_g$ are the solute compositions of the matrix and GB phases, respectively. The superscript $e$ on the concentrations denotes the equilibrium concentration. The slope of the two parallel tangent lines (dotted lines) is the equilibrium diffusion potential

$$
\tilde{\mu}^e\equiv\frac{df^m(u_m^e)}{du} = \frac{df^g(u_g^e)}{du}. \tag{3}
$$

![](./images/814530487358849025_2.jpg)

Fig. 1. Free energy-concentration diagram. $f^m$ and $f^g$ are the free energy densities of the matrix and GB phases, respectively. $u_m$ and $u_g$ are the solute compositions of the matrix and GB phases, respectively. The superscript $e$ on the concentrations denotes the equilibrium concentration. The slope of the two parallel tangent lines (dotted lines) is the equilibrium diffusion potential $\mu^e$. The equilibrium compositions correspond to the contact points of the two parallel tangent lines with the free energy curves. The GB energy $\sigma$ scaled by the GB width $2\xi$ is represented by the vertical distance $\overline{QR}$ between the parallel tangent lines.

As shown in this figure, the equilibrium compositions correspond to the contact points of the two parallel tangent lines with the free energy curves.

The GB energy in the present two-phase approach is given by the Gibbs free energy change when the matrix phase with the composition $u_m^e$ in the volume of a unit area and a width $2\xi$ is changed into the GB phase with composition $u_g^e$, under the conditions of constant pressure, constant temperature and fixed numbers of $A$ and $B$ atoms. During this state change, assuming the same molar volumes of $A$ and $B$, the matrix gains the solvent volume of $(u_g^e - u_m^e)2\xi$ from the GB region and loses the same volume of solute into the GB region. The free energy changes take place in both the matrix region and the GB region. Assuming that the volume of the matrix region is sufficiently larger than that of the GB region, the free energy change in the matrix is $-2\xi(u_g^e - u_m^e)\mu^e$. The free energy change in the GB region is $2\xi(f^g(u_g^e)-f^m(u_m^e))$. Thus, the GB energy $\sigma$, which is the total free energy change in the system, is given by
$$
\sigma=2\xi\omega^e, \tag{4}
$$
where we defined
$$
\omega^e=f^g\left(u_g^e\right)-f^m\left(u_m^e\right)-\left(u_g^e-u_m^e\right)\frac{df^m\left(u_m^e\right)}{du} \tag{5}
$$

Because $2\xi$ in the classical two-phase model is assumed to be independent of composition, we can eliminate $2\xi$ in Eqs. (1) and (4), and it then follows that
$$
\sigma=\sigma_A\frac{\omega^e}{\omega_A} \tag{6}
$$

$\omega^e$ can be graphically represented on the free energy diagram of Fig. 1. The term $f^g(u_g^e)-f^m(u_m^e)$ in Eq. (5) corresponds to the distance $\overline{QS}$, and the remaining term to the distance $\overline{RS}$. Thus, $\sigma/2\xi$ is represented by the vertical distance $\overline{QR}$ between the parallel tangent lines. If the matrix composition $u_m^e$ is increased, the GB energy decreases because the two parallel tangent lines approach each other. At the moment when the two tangent lines are merged into one common tangent line, it vanishes. In this state, the free energy changes in the matrix region and the GB region during the GB formation process cancel each other out.

## 3. Phase-field model for GB segregation
### 3.1. Basic formulation

We develop the phase-field models based on the two-phase approach of GB, which can be regarded as a diffuse interface version of the classical two-phase GB model explained in the previous section. For convenience, we consider a specific system that consists of two grains and a GB region between them. For the matrix (grain interior region) of one grain, a phase field $\phi=0$ is assigned, and $\phi=1$ for the matrix of the other grain. Across the GB region between the two grains, the phase field changes monotonically from $\phi=0$ to $\phi=1$. We assume that the position with $\phi=1/2$ (center of the GB region) has its own specific thermodynamic properties, which we denote as a GB phase. Thus, the thermodynamic state at an arbitrary position in the system is represented as a hypothetical mixture of the matrix phase and GB phase. Thus, the effective solute concentration $u(\boldsymbol{x})$ at an arbitrary point $\boldsymbol{x}$ is given by
$$
u(\boldsymbol{x})=g(\phi)u_g(\boldsymbol{x})+(1-g(\phi))u_m(\boldsymbol{x}), \tag{7}
$$
where $u_g$ and $u_m$ are the solute concentrations of the GB phase and matrix phase that constitute the point, respectively. $g(\phi)$ is an interpolation function corresponding to the GB phase fraction, which satisfies $g(0)=0$ and $g(1)=1$ and $g(1/2)=1$. For examples, one can take $g(\phi)=4\phi(1-\phi)$ with double obstacles at $\phi=0$ and $\phi=1$ or $g(\phi)=16\phi^2(1-\phi)^2$. The function $g(\phi)$ plays another role of the double-well potential to maintain the stable GB region in the phase-field model, as will be manifested in the phase-field equation. In this study, we adopt the function $g(\phi)=4\phi(1-\phi)$ with the double obstacles because this function leads us to a clear-cut definition of the GB region [34,41,46]. However, one can adopt $g(\phi)=16\phi^2(1-\phi)^2$. In this case, only the numerical factors in the GB energy and the GB width appear to be different. The local free energy density $f$ at an arbitrary point in the system is given by a mixture rule,
$$
f=g(\phi)f^g(u_g)+(1-g(\phi))f^m(u_m), \tag{8}
$$
where $f^g(u_g)$ and $f^m(u_m)$ are the free energy densities of the GB and matrix phases, respectively. The total free energy of the present system with volume $V$ is given by
$$
F=\int_V\left[f+\frac{\varepsilon^2}{2}|\nabla\phi|^2\right]dV, \tag{9}
$$
where $\varepsilon$ is the gradient energy coefficient, which is assumed as a constant. Inserting Eq. (8) into Eq. (9), the functional $F$ can be written as
$$
F=\int_V\left[f^m(u_m)+g(\phi)\left(f^g(u_g)-f^m(u_m)\right)+\frac{\varepsilon^2}{2}|\nabla\phi|^2\right]dV, \tag{10}
$$
where $f^g - f^m$ corresponds to the height of the double-well potential. This concentration dependency of the potential height leads to the GB segregation. The time evolutions of the phase field and concentration field are governed by the non-conserved and conserved Landau-Ginzburg equations, respectively,
$$
\frac{\partial\phi}{\partial t}=-M_\phi\frac{\delta F}{\delta\phi} \tag{11}
$$
and

$$
\frac{\partial u}{\partial t}=-\nabla \cdot M_{d} \nabla \frac{\delta F}{\delta u},
\tag{12}
$$

where $M_{\phi}$ and $M_{d}$ are the phase-field mobility and the diffusion mobility, respectively. The above equations determine the time evolutions of the phase field $\phi$ and the effective concentration $u$, whereas another two concentrations $u_{g}$ and $u_{m}$ were involved in functional $F$ on the right hand sides of the above equations. For Eqs. (11) and (12) to operate, $u_{g}$ and $u_{m}$ should be related to $\phi$ and $u$, mediated by two additional relations. One of the two relations we need is the mixture rule (7). For the other relation, we assume a specific relationship between $u_{g}$ and $u_{m}$. A very similar situation has appeared in the phase-field model for phase transformation in alloys [33,47-49]. As in that situation, two choices for the relationship between $u_{g}$ and $u_{m}$ can be employed: the equal composition condition or the equal diffusion potential condition. In the following section, we derive the governing equations for GB segregation for each of the two choices. We will denote the models for two choices as model I and model II.

### 1) Model I: equal composition approach

In this approach, the solute concentrations of the matrix and GB phases at a given point $\boldsymbol{x}$ are assumed to be the same. From Eq. (7), it then follows that
$$
u_{g}(\boldsymbol{x})=u_{m}(\boldsymbol{x})=u(\boldsymbol{x})
\tag{13}
$$
and
$$
f(\phi, u)=(1-g(\phi)) f^{m}(u)+g(\phi) f^{g}(u)
\tag{14}
$$

The free energy functional is given by
$$
F=\int_{V}\left[f(\phi, u)+\frac{\varepsilon^{2}}{2}|\nabla \phi|^{2}\right] d V
\tag{15}
$$

The functional derivatives with respect to $\phi$ and $u$ yield the phase-field equation
$$
\frac{1}{M_{\phi}} \frac{\partial \phi}{\partial t}=\varepsilon^{2} \nabla^{2} \phi-\left(f^{g}(u)-f^{m}(u)\right) \frac{d g(\phi)}{d \phi}
\tag{16}
$$
and the diffusion equation
$$
\frac{\partial u}{\partial t}=\nabla \cdot M_{d} \nabla \frac{\partial f}{\partial u}=\nabla \cdot M_{d} \nabla\left[\frac{d f^{m}}{d u}+g(\phi)\left(\frac{d f^{g}(u)}{d u}-\frac{d f^{m}(u)}{d u}\right)\right],
\tag{17}
$$
where $M_{\phi}$ and $M_{d}$ are the phase-field mobility and the diffusion mobility, respectively.

### 2) Model II: equal diffusion potential approach

In this approach, we impose the equal diffusion potential condition between $u_{g}(\boldsymbol{x})$ and $u_{m}(\boldsymbol{x})$:
$$
\frac{d f^{g}\left(u_{g}\right)}{d u_{g}}=\frac{d f^{m}\left(u_{m}\right)}{d u_{m}} \equiv \tilde{\mu}
\tag{18}
$$

The evolution equations of the phase field $\phi$ and concentration field $u$ can be obtained from Eqs. (11) and (12), respectively. In this procedure, we need some relationships between the differentiations of $u_{g}$ and $u_{m}$ with respect to $u$ and $\phi$, as follows. Differentiating Eq. (7) with respect to $\phi$ and $u$, we get
$$
g(\phi) \frac{\partial u_{g}}{\partial \phi}+(1-g(\phi)) \frac{\partial u_{m}}{\partial \phi}=\frac{d g(\phi)}{d \phi}\left(u_{m}-u_{g}\right)
\tag{19}
$$
and
$$
g(\phi) \frac{\partial u_{g}}{\partial u}+(1-g(\phi)) \frac{\partial u_{m}}{\partial u}=1,
\tag{20}
$$
respectively. It then follows that the functional derivative of Eq. (10) with respect to $\phi$ is
$$
\frac{\delta F}{\delta \phi}=-\varepsilon^{2} \nabla^{2} \phi+\frac{\partial f}{\partial \phi},
\tag{21}
$$
where the last term on the right side is given by
$$
\begin{aligned}
\frac{\partial f}{\partial \phi}= & g(\phi) \frac{d f^{g}\left(u_{g}\right)}{d u_{g}} \frac{\partial u_{g}}{\partial \phi}+(1-g(\phi)) \frac{d f^{m}\left(u_{m}\right)}{d u_{m}} \frac{\partial u_{m}}{\partial \phi}+\frac{d g(\phi)}{d \phi}\left(f^{g}\left(u_{g}\right)\right. \\
& \left.-f^{m}\left(u_{m}\right)\right) \\
= & \left(g(\phi) \frac{\partial u_{g}}{\partial \phi}+(1-g(\phi)) \frac{\partial u_{m}}{\partial \phi}\right) \tilde{\mu}+\frac{d g(\phi)}{d \phi}\left(f^{g}\left(u_{g}\right)-f^{m}\left(u_{m}\right)\right) \\
= & \left(f^{g}\left(u_{g}\right)-f^{m}\left(u_{m}\right)-\left(u_{g}-u_{m}\right) \tilde{\mu}\right) \frac{d g(\phi)}{d \phi},
\end{aligned}
\tag{22}
$$
where we used the equal diffusion potential condition (18) in the second line and Eq. (19) in the third line. The functional derivative of functional (10) with respect to $u$ is
$$
\begin{aligned}
\frac{\delta F}{\delta u} & =\frac{\partial f}{\partial u}=g(\phi) \frac{d f^{g}\left(u_{g}\right)}{d u_{g}} \frac{\partial u_{g}}{\partial u}+(1-g(\phi)) \frac{d f^{m}\left(u_{m}\right)}{d u_{m}} \frac{\partial u_{m}}{\partial u} \\
& =\left(g(\phi) \frac{\partial u_{g}}{\partial u}+(1-g(\phi)) \frac{\partial u_{m}}{\partial u}\right) \tilde{\mu}=\tilde{\mu},
\end{aligned}
\tag{23}
$$
where we used condition (18) and Eq. (20). From the Landau-Ginzburg equations (11) and (12), we then have the phase-field equation
$$
\frac{1}{M_{\phi}} \frac{\partial \phi}{\partial t}=\varepsilon^{2} \nabla^{2} \phi-\left(f^{g}\left(u_{g}\right)-f^{m}\left(u_{m}\right)-\left(u_{g}-u_{m}\right) \tilde{\mu}\right) \frac{d g(\phi)}{d \phi}
\tag{24}
$$
and diffusion equation
$$
\frac{\partial u}{\partial t}=\nabla \cdot M_{d} \nabla \tilde{\mu}
\tag{25}
$$

The diffusion equation (25) can be written in terms of $u_{g}$ and $u_{m}$, instead of the diffusion potential $\tilde{\mu}$, following the procedure in Ref. [50]:
$$
\frac{\partial u}{\partial t}=\nabla \cdot g(\phi) D_{g} \nabla u_{g}+\nabla \cdot(1-g(\phi)) D_{m} \nabla u_{m},
\tag{26}
$$
where $D_{g}$ and $D_{m}$ are the diffusivities in the GB and matrix phases:
$$
D_{g}=M_{g} \frac{d^{2} f^{g}\left(u_{g}\right)}{d u_{g}^{2}} \quad \text { and } \quad D_{m}=M_{m} \frac{d^{2} f^{m}\left(u_{m}\right)}{d u_{m}^{2}}
\tag{27}
$$

### 3.2. Thermodynamic properties of models

We examine the changes in the thermodynamic properties of the GB by segregation, particularly, focusing on the GB energy. Let

us consider the one-dimensional (1D) system in the previous section, with two grains and a straight GB between them. The width of the GB region is denoted by $2\xi$. The phase field is given by $\phi=0$ for the bulk grain in $x < -\xi$ and $\phi=1$ for the other bulk grain in $x > \xi$. In the GB region within $-\xi < x < \xi$, the phase field changes monotonically from zero to one. We consider three cases of 1) a pure substance without GB segregation, 2) model I with the equal composition condition and 3) model II with the equal diffusional potential condition. After deriving the GB energy for the three cases with arbitrary free energy density forms for the matrix and GB phases, we will consider specific forms of the free energy in the following section.

### 1) Pure substance without GB segregation
In this case without a solute species, there is no difference between model I and model II. The equilibrium property of the GB is governed only by following phase-field equation:
$$
\varepsilon^{2} \frac{d^{2} \phi}{d x^{2}}=\left(f_{A}^{g}-f_{A}^{m}\right) \frac{d g(\phi)}{d \phi}\quad(28)
$$

By integrating after multiplying both sides of Eq. (28) by $d\phi/dx$, we get
$$
\frac{d \phi}{d x}=\frac{\sqrt{2}}{\varepsilon} \sqrt{\omega_{A} g(\phi)}\quad(29)
$$
where the height of the double-well potential is defined by $\omega_A = f_A^g - f_A^m$. We assume $f_A^g > f_A^m$, which ensures the existence of the stable phase field in pure A. The GB energy is obtained by calculating the excess free energy due to the existence of the GB region from functional (10) [41], which yields the GB energy
$$
\sigma_{A}=\varepsilon^{2} \int_{-\infty}^{\infty}\left(\frac{d \phi}{d x}\right)^{2} d x=\varepsilon^{2} \int_{0}^{1} \frac{d \phi}{d x} d \phi=\frac{\pi \varepsilon}{4} \sqrt{2 \omega_{A}},\quad(30)
$$
where we used $g(\phi)=4\phi(1-\phi)$. The GB width is given by
$$
2 \xi_{A}=\int_{0}^{1} \frac{d x}{d \phi} d \phi=\frac{\pi \varepsilon}{2 \sqrt{2 \omega_{A}}}\quad(31)
$$

The terms on the right hand sides of Eqs. (30) and (31) are different from those in Refs. [41,51]. This stems from the difference in the definitions of the double-well potential: $g(\phi)=\phi(1-\phi)$ in Refs. [41,51] and $g(\phi)=4\phi(1-\phi)$ in this study. Parameters $\omega_A$ and $\varepsilon$ can be represented in terms of the GB energy and GB width. Eliminating $\varepsilon$ in Eqs. (30) and (31) yields
$$
\omega_{A}=f_{A}^{g}-f_{A}^{m}=\frac{\sigma_{A}}{2 \xi_{A}},\quad(32)
$$

Eliminating $\omega_A$ in Eqs. (30) and (31) yields
$$
\varepsilon=\frac{4}{\pi} \sqrt{\xi_{A} \sigma_{A}}\quad(33)
$$

From Eq. (32), the GB energy can be written in the form $\sigma_A=2\xi_A(f_A^g - f_A^m)$. This is identical to the GB energy (1) in the classical two-phase model for a pure substance.

### 2) Properties of model I
In the 1D equilibrium state, we write the phase-field
$$
\varepsilon^{2} \frac{d^{2} \phi}{d x^{2}}=\frac{\partial f(\phi, u)}{\partial \phi}\quad(34)
$$
and diffusion equations
$$
\frac{\partial f(\phi, u)}{\partial u}=\mathrm{const}=\frac{d f^{m}\left(u_{m}^{e}\right)}{d u}=\frac{d f^{g}\left(u_{g}^{e}\right)}{d u},\quad(35)
$$
where $u_m^e$ and $u_g^e$ are the equilibrium compositions of the matrix phase at $\phi=0$ or $\phi=1$ and the GB phase at $\phi=0.5$ (center of GB region where $g(\phi)=1$), respectively. Note that the constant in the diffusion equation should be independent of the position and $\phi$. Therefore, this constant should be the same not only as the diffusion potential $df^m(u_m^e)/du$ in the matrix but also the diffusion potential $df^m(u_g^e)/du$ at the center of the GB region. As in the classical two-phase model [23-26], therefore, the equilibrium compositions $u_g^e$ and $u_m^e$ are determined by the parallel tangent construction on the free energy diagram in Fig. 2. The equilibrium concentration profile $u(\phi)$ in the half GB region of $0\leq\phi\leq0.5$ and $-\xi\leq x\leq0$ interpolates from $u_m^e$ at $\phi=0$ to $u_g^e$ at $\phi=0.5$. This profile as a function of the phase field can be determined from Eq. (35), if $f^g(u)$ and $f^m(u)$ are given. The concentration profile on the other side of the GB region with $0.5\leq\phi\leq1$ is symmetric with respect to that in $0.5\leq\phi\leq1$.

The GB energy and width are determined by the phase-field equation (34), as follows. After multiplying both sides of Eq. (34) by $d\phi/dx$, we integrate
$$
\frac{\varepsilon^{2}}{2}\left(\frac{d \phi}{d x}\right)^{2}=\int_{0}^{\phi} \frac{\partial f(\phi, u)}{\partial \phi} d \phi\quad(36)
$$

Taking into account that
$$
d f=\frac{\partial f}{\partial \phi} d \phi+\frac{\partial f}{\partial u} d u=\frac{\partial f}{\partial \phi} d \phi+\frac{d f^{m}\left(u_{m}^{e}\right)}{d u} d u,\quad(37)
$$

Eq. (36) can be modified as
$$
\begin{aligned}
\frac{\varepsilon^{2}}{2}\left(\frac{d \phi}{d x}\right)^{2} &=\int_{0}^{\phi}\left(d f-\frac{\partial f^{m}\left(u_{m}^{e}\right)}{\partial u} d u\right) \\
&=f(\phi, u)-f^{m}\left(u_{m}^{e}\right)-\left(u-u_{m}^{e}\right) \frac{d f^{m}\left(u_{m}^{e}\right)}{d u}
\end{aligned}\quad(38)
$$

Thus, we get
$$
\frac{d \phi}{d x}=\frac{\sqrt{2}}{\varepsilon} \sqrt{\Omega_{1}(\phi)},\quad(39)
$$
where we define
$$
\begin{aligned}
\Omega_{1}(\phi)= & \left(g(\phi) f^{g}(u)+(1-g(\phi)) f^{m}(u)\right)-f^{m}\left(u_{m}^{e}\right) \\
& -\left(u-u_{m}^{e}\right) \frac{d f^{m}\left(u_{m}^{e}\right)}{d u}
\end{aligned}\quad(40)
$$

Note that $\Omega_1$ is a function of only $\phi$ because the equilibrium concentration profile $u$ is a function of $\phi$. Comparing Eq. (39) for the alloy with Eq. (29) for pure solvent, $\Omega_1$ may be regarded as an effective double-well potential for alloys. The GB energy is obtained by summing the excess energy of the GB region and the energy change of the matrix phase according to the GB segregation [41,42], which results in

$$
\sigma=\varepsilon^{2} \int_{0}^{1} \frac{d \phi}{d x} d \phi=\sqrt{2} \varepsilon \int_{0}^{1} \sqrt{\Omega_{1}(\phi)} d \phi
\tag{41}
$$

The GB width is

$$
2 \xi=\int_{0}^{1} \frac{d x}{d \phi} d \phi=\frac{\varepsilon}{\sqrt{2}} \int_{0}^{1} \frac{d \phi}{\sqrt{\Omega_{1}(\phi)}}
\tag{42}
$$

It should be noted that the phase-field profile (39) GB energy (41) and GB width (42) can exist only when $\Omega_{1}(\phi) \geq 0$ in the whole range of $0 \leq \phi \leq 1$. As will be shown later, this imposes restrictions on the GB segregation level and the resultant GB energy reduction for a given alloy.

The effective potential $\Omega_{1}(\phi)$ can be graphically represented on the free energy diagram in Fig. 2. $u=u_{m}^{e}$ and $u=u_{g}^{e}$ are the equilibrium compositions at $\phi=0$ (or $\phi=1$) and $\phi=1 / 2$, respectively. The composition profile $u(\phi)$ in $0 \leq \phi \leq 1 / 2$ (and then $0 \leq g(\phi) \leq 1$) interpolates between $u=u_{m}^{e}$ and $u=u_{g}^{e}$. Similarly, the free energy density $f(u, \phi)=g(\phi) f^{g}(u)+(1-g(\phi)) f^{m}(u)$ interpolates between $f^{m}\left(u_{m}^{e}\right)$ and $f^{g}\left(u_{g}^{e}\right)$ with the changing GB phase fraction of $g(\phi)$, which is shown as a red curve in Fig. 2. Let us consider a position with a composition $u(\phi)$ in the GB region. $f(u, \phi)$ at this position corresponds to the distance $\overline{Q T^{\prime}}$ in Fig. 2, which is the first term on the right side of the effective potential (40). The second term and third term in (40) correspond to the distances $-\overline{R T}$ and $\overline{R S}$, respectively. Summing three terms, $\Omega_{1}(\phi)$ appears as the distance $\overline{Q S^{\prime}}$, which is the distance between $f(u, \phi)$ and the tangent line to $f^{m}(u)$. Thus, $\Omega_{1}(\phi)$ is a monotonically increasing function from zero at $\phi=0$ to a maximum at $\phi=1 / 2$, as indicated by the shaded region in Fig. 2. When $\phi$ is in the range of $1 / 2 \leq \phi \leq 1, \Omega_{1}(\phi)$ becomes its mirror image in $0 \leq \phi \leq 1 / 2$.

![](./images/814530487358849025_3.jpg)

Fig. 2. Schematic representation of the effective potential $\Omega_{1}(\phi) . f^{m}(u)$ and $f^{g}(u)$ are the free energy densities of the matrix and GB phases, respectively. $u_{m}^{e}$ and $u_{g}^{e}$ are the equilibrium compositions of the matrix phase at $\phi=0$ (or $\phi=1$) and the GB phase at $\phi=0.5$, respectively. $u(\phi)$ is the solute concentration at the position with a phase field value $\phi$. The height of the effective potential $\Omega_{1}(\phi)$ is given by the length $\overline{Q S^{\prime}}$. Thus, $\Omega_{1}(\phi)$ is a monotonically increasing function from zero at $\phi=0$ to a maximum at $\phi=1 /$ 2, as indicated by the shaded region.

If the matrix composition $u_{m}^{e}$ is increased over the critical value where $f^{m}(u)=f^{g}(u)$, the basic form of $\Omega_{1}(\phi)$ is changed. This situation is shown in Fig. 3(a). The composition where the two free energy curves intersect is designated by $u^{*}$, and the GB composition on the common tangent line by $u_{g}^{c t}$. As $\phi$ increases from zero, $u$ increases from $u_{m}^{e}$, and then $\Omega_{1}(\phi)$ also does so from zero. When $u$ becomes larger than $u^{*}$, however, $\Omega_{1}(\phi)$ begins to decrease. Thus, one can see that in the case of $u^{*}<u_{g}^{e}<u_{c t}$, the potential $\Omega_{1}(\phi)$ shows a maximum at $\phi<1 / 2$ and a local minimum at $\phi=1 / 2$. A more interesting case is when the compositions $u_{m}^{e}$ and $u_{g}^{e}$ are increased to values such that $u_{m}^{e}=u_{m}^{c t}$ and $u_{g}^{e}=u_{g}^{c t}$, where the two parallel tangent lines are merged into a common tangent line. In this case, as shown in Fig. 3(b)u, the height of $\Omega_{1}(\phi)$ vanishes at $\phi=1 /$ 2.

For the three cases of $u_{g}^{e}<u^{*}, u^{*}<u_{g}^{e}<u_{g}^{c t}$ and $u_{g}^{e}=u_{g}^{c t}$, the resultant forms of $\Omega_{1}(\phi)$ are schematically represented in Fig. 4 over the range of $0 \leq \phi \leq 1$. In this figure, the GB phase fractions, compositions and positions corresponding to $\phi=0, \phi=1 / 2$ and $\phi=1$ are denoted under the horizontal axis. The effective potential $\Omega_{1}(\phi)$ has a single peak at $\phi=1 / 2$ when $u_{g}^{e}<u^{*}$ and double peaks when $u_{g}^{e}>u^{*}$. If $u_{g}^{e}>u_{g}^{c t}$, the potential would then be negative at $\phi=1 / 2$. Two interesting aspects should be noted for the potential $\Omega_{1}(\phi)$ shown in Fig. 4. First, when $u_{g}^{e}=u_{g}^{c t}$, the GB energy given by Eq. (41) maintains a positive value because the area between $\Omega_{1}(\phi)$ and the $\phi$-axis remains finite. This situation is in sharp contrast with the classical two-phase model for GB segregation, where the GB energy should vanish, as explained in section 2. The reason why the GB energy of model I remains finite in this situation is simple: the region with the intermediate composition between $u_{m}^{e}$ and $u_{g}^{e}$ contributes to the GB energy, whereas there exists no such intermediate region in the classical two-phase model. Second, the phase-field profile (39), GB energy (41) and GB width (42) can be defined only when $\Omega_{1}(\phi)$ remains positive in the whole range of the phase field $(0<\phi<1)$. When $u_{g}^{e}>u_{g}^{c t}$, therefore, there exists no stable equilibrium solution in model I. The fact that $\Omega_{1}(\phi)$ in model I should remain positive imposes a bound on the GB energy change by GB segregation. This bound is not an intrinsic characteristic in the PFMs for GB segregation, but it stems from the equal composition condition (13) in model I and can be removed by adopting another condition instead of the equal composition condition, as will be shown in the following model II.

### 3) Properties of model II

We examine the properties of model II with the equal diffusion potential condition for the same 1D system as in model I. The equilibrium solution of the diffusion equation (25) coupled with condition (18) is

$$
\tilde{\mu}^{e}=\frac{d f^{m}\left(u_{m}^{e}\right)}{d u_{m}}=\frac{d f^{g}\left(u_{g}^{e}\right)}{d u_{g}}=\mathrm{const},
\tag{43}
$$

which is identical to Eq. (3) and leads to $u_{g}^{e}=$ const and $u_{m}^{e}=$ const. Thus, the equilibrium compositions are determined by the parallel tangent construction on the free energy diagram, as in the previous model I and the classical two-phase model. Following the mixture rule (7), the equilibrium profile $u(\phi)$ of the effective composition as a function of the phase field is given by

$$
u(\phi)=g(\phi) u_{g}^{e}+(1-g(\phi)) u_{m}^{e}
\tag{44}
$$

Approaching from the matrix phase to the GB phase at the center of the GB region, the equilibrium composition in the present model II continuously changes from $u_{m}^{e}$ at $\phi=0$ to $u_{g}^{e} \phi=1 / 2$, as in the previous model I. However, there is a notable difference between the composition profiles of models I and II. In model I with the equal composition condition of $u=u_{m}=u_{g}$, all three compositions simultaneously change from $u_{m}^{e}$ at $\phi=0$ to $u_{g}^{e} \phi=1 / 2$. In model II, on the other hand, $u_{m}^{e}$ and $u_{g}^{e}$ remain constant over the whole space of the system, although the mixture composition $u(\phi)$ changes in the GB region according to Eq. (44). This seemingly trivial difference will lead to large differences in the thermodynamic properties

![](./images/814530487358849025_4.jpg)

Fig. 3. Schematic representation of the effective potential $\Omega_{1}(\phi)$. (a) $u^{*}<u_{g}^{e}<u_{g}^{c t}$ and (b) $u_{g}^{e}=u_{g}^{c t}$, where $u^{*}$ is the composition where the two free energy curves intersect and $u_{g}^{c t}$ is the GB phase composition on the common tangent line. The height of $\Omega_{1}(\phi)$ corresponds to the distance between the red curve and the lower dotted tangent line. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

![](./images/814530487358849025_5.jpg)

Fig. 4. Schematic representation of the effective potential $\Omega_{1}(\phi)$ for the three cases of $u_{g}^{e}<u^{*}, u^{*}<u_{g}^{e}<u_{g}^{c t}$ and $u_{g}^{e}=u_{g}^{c t}$. GB phase fractions, compositions and positions corresponding to $\phi=0, \phi=1 / 2$ and $\phi=1$ are denoted under the horizontal axis.

of models I and II.

The phase-field equation (24) in the 1D equilibrium state reads
$$
\varepsilon^{2} \frac{d^{2} \phi}{d x^{2}}-\omega^{e} \frac{d g(\phi)}{d \phi}=0,
\tag{45}
$$
where $\omega^{e}$ is just the parameter defined by Eq. (5) in the classical two-phase model. Note that $\omega^{e}$ is a constant in the whole space of the system because $u_{m}^{e}$ and $u_{g}^{e}$ are constant. By integrating Eq. (45) after multiplying by $d \phi / d x$, we obtain the phase-field gradient
$$
\frac{d \phi}{d x}=\frac{\sqrt{2}}{\varepsilon} \sqrt{\Omega_{\mathrm{II}}(\phi)},
\tag{46}
$$
where we define
$$
\Omega_{\mathrm{II}}(\phi)=\omega^{e} g(\phi)
\tag{47}
$$

The effective potential $\Omega_{\mathrm{II}}(\phi)$ in model II has the same functional form as the double-well potential $g(\phi)$, but with a compositiondependent height $\omega^{e}$. The GB energy can be obtained by taking into account the free energy changes in the matrix region and GB region during the GB formation process, as in Refs. [41], which yields
$$
\sigma=\varepsilon^{2} \int_{0}^{1} \frac{d \phi}{d x} d \phi=\frac{\pi \varepsilon}{4} \sqrt{2 \omega^{e}},
\tag{48}
$$
where we used $g(\phi)=4 \phi(1-\phi)$. The GB width follows as
$$
2 \xi=\int_{0}^{1} \frac{d x}{d \phi} d \phi=\frac{\pi \varepsilon}{2 \sqrt{2 \omega^{e}}}
\tag{49}
$$

The phase-field profile is obtained by integrating Eq. (46):
$$
\phi(x)=\frac{1}{2}\left(1+\sin \frac{2 \sqrt{2 \omega^{e}}}{\varepsilon} x\right) \text { in }|x| \leq \frac{\pi \varepsilon}{4 \sqrt{2 \omega^{e}}},
\tag{50}
$$

It is notable that the GB energy, GB width and phase-field profile are all analytically obtained, whereas in Model I, all of them are obtained by numerical integrations. The GB energy can be modified into different informative forms: We eliminate $\varepsilon$ by dividing Eqs. (48) and (49), which yields
$$
\sigma=2 \xi \omega^{e}
\tag{51}
$$

Remarkably, this is the same form as the GB energy (4) in the classical two-phase model: in both models, the GB energy is determined as the vertical distance between two parallel tangent lines, multiplied by the GB width. However, one should keep in mind which parameter in the models is being preserved as a constant independent of the composition. In the classical two-phase model, $2 \xi$ is assumed to be a constant independent of the composition. In the present model, on the other hand, the gradient energy coefficient $\varepsilon$ is the constant and the GB width $2 \xi$, given by Eq. (49), is dependent on the composition. To see more clearly the result caused by the difference in choosing the constant, we make another equation of the GB energy without the GB width by getting $\varepsilon$ from Eq. (30) for the pure solvent and inserting it into Eq. (48):
$$
\sigma=\sigma_{A} \sqrt{\frac{\omega^{e}}{\omega_{A}}}
\tag{52}
$$

Thus, the dependence of the GB energy on the composition in

model II is contained in the form $\sqrt{\omega^{e}}$. This is in sharp contrast with Eq. (6): the GB energy in the classical two-phase model is proportional to $\omega^{e}$. We assumed that $\varepsilon$ is a constant in deriving Eq. (52) from Eqs. (30) and (48), whereas we assumed that $2 \xi$ is a constant in deriving Eq. (6). This brings about a quite different dependence of the GB energy on the composition.

## 4. Thermodynamic approximation

In this section, we adopt specific free energy forms for the matrix and GB phases. This explicitly reveals not only the basic characteristics of the models, but also the relationship between the PFMs proposed in the literature for GB segregation and the present models.

For the GBs in pure $A$ and pure $B$ to be stable, the free energy density of the GB phase should be larger than that of the matrix phase: $f_{A}^{g}>f_{A}^{m}$ and $f_{B}^{g}>f_{B}^{m}$, where subscripts $A$ or $B$ under $f$ denote the free energy density of pure solvent $A$ or pure solute $B$. In many practical alloys, the solubility in the matrix appears to be very limited, whereas the GB segregation varies over a wide range depending on the matrix composition. To include such a situation in the model, we add a regular solution term to the free energy of the matrix phase, $L^{m} u_{m}\left(1-u_{m}\right) \simeq L^{m} u_{m}$, where $L^{m}$ is a regulation solution parameter:
$$
\begin{aligned}
f^{m}\left(u_{m}\right)= & u_{m} f_{B}^{m}+\left(1-u_{m}\right) f_{A}^{m}+L^{m} u_{m}+\frac{1}{\beta}\left(u_{m} \ln u_{m}\right. \\
& \left.+\left(1-u_{m}\right) \ln \left(1-u_{m}\right)\right).
\end{aligned}
$$

This form of $f^{m}\left(u_{m}\right)$ is valid for a dilute solution because we ignored the quadratic term $L^{m} u_{m}^{2}$. The GB phase is simply assumed to be an ideal solution:
$$
f^{g}\left(u_{g}\right)=u_{g} f_{B}^{g}+\left(1-u_{g}\right) f_{A}^{g}+\frac{1}{\beta}\left(u_{g} \ln u_{g}+\left(1-u_{g}\right) \ln \left(1-u_{g}\right)\right).
$$

### 4.1. Properties of model I

With $u_{g}=u_{m} \equiv u$, we have
$$
f^{g}(u)-f^{m}(u)=\omega_{A}(1-\alpha u),
$$
where $\omega_{A}=f_{A}^{g}-f_{A}^{m}$ and a dimensionless parameter $\alpha$ is defined by
$$
\alpha=\frac{\left(f_{A}^{g}-f_{B}^{g}-f_{A}^{m}+f_{B}^{m}+L^{m}\right)}{f_{A}^{g}-f_{A}^{m}}.
$$

If we neglect the parameter $L^{m}, \alpha$ is fixed by the GB energies and widths in pure $A$ and pure $B$ because of Eq. (32). With the addition of $L^{m}$, however, $\alpha$ can be regarded as a free parameter. This enables us to arbitrarily control the GB segregation level and GB energy change. In terms of $\alpha$, the phase-field equation (16) is written as
$$
\frac{1}{M_{\phi}} \frac{\partial \phi}{\partial t}=\varepsilon^{2} \nabla^{2} \phi-\omega_{A}(1-\alpha u) \frac{d g(\phi)}{d \phi}
$$
and the diffusion equation (17) as
$$
\frac{\partial u}{\partial t}=\nabla \cdot M_{d} \nabla\left[\frac{d f^{m}(u)}{d u}-\alpha \omega_{A} g(\phi)\right],
$$
where $d f^{m}(u) / d u=\omega_{A}+L^{m}+(1 / \beta) \ln \left(u_{m} /\left(1-u_{m}\right)\right)$. These equations (57) and (58) are identical with those in the PFM first proposed by Grönhagen and Ågren [40], adopted for the grain growth simulation with GB segregation by Kim and Park [41] and for investigating the kinetic aspect of GB segregation by Li et al. [42]. If we do not ignore the quadratic term $\left(-L^{m} u^{2}\right)$ in the regular solution, we should make replacements of $(1-\alpha u) \rightarrow\left(1-\alpha u+\alpha^{\prime} u^{2}\right)$ in the phase-field equation and $\alpha \omega_{A} \rightarrow\left(\alpha-2 \alpha^{\prime} u\right) \omega_{A}$ in the diffusion equation, where $\alpha^{\prime}$ is another constant parameter. The resultant equations appear to be identical to those in Ref. [44]. When we take some specific forms for the free energy densities of the matrix and GB phases, therefore, the governing equations in the PFMs developed and used in previous studies are reproduced from model I. On such a basis, most PFMs for GB segregation, even if they look like a single-phase approach, can be regarded as specific forms of the phase-field model constructed on the two-phase approach and the equal composition condition.

With the free energy densities of Eqs. (53) and (54), Eq. (35) gives the equilibrium composition profile as a function of the phase field:
$$
\frac{u(\phi)}{1-u(\phi)}=\frac{u_{m}^{e}}{1-u_{m}^{e}} \exp \left(\alpha \beta \omega_{A} g(\phi)\right).
$$

The GB composition $u_{g}^{e}$, which is the equilibrium composition at the center of the GB region, is obtained by setting $\phi=0.5$ and then $g(\phi)=1$:
$$
\frac{u_{g}^{e}}{1-u_{g}^{e}}=\frac{u_{m}^{e}}{1-u_{m}^{e}} \exp \left(\alpha \beta \omega_{A}\right).
$$

This is same as equation [1,23-26] for the GB composition in the classical two-phase model. The regular solution parameter $L^{m}$ is included in the parameter $\alpha$ defined by Eq. (56). Thus, a large positive $L^{m}$ significantly increases the GB segregation level. The GB equilibrium composition given by Eq. (60) should equally operate not only in model II but also in the classical two-phase model because it should be determined by the same parallel tangent construction.

We turn to the GB energy and width, which are determined from the effective potential $\Omega_{1}$ given by Eq. (40). Directly inserting the free energy densities (53) and (54) into Eq. (40) yields
$$
\begin{aligned}
\Omega_{1}(\phi) & =\omega_{A}(1-\alpha u) g(\phi)+\frac{u}{\beta} \ln \frac{u\left(1-u_{m}^{e}\right)}{(1-u) u_{m}^{e}}+\frac{1}{\beta} \ln \frac{1-u}{1-u_{m}^{e}} \\
& =\omega_{A} g(\phi)+\frac{1}{\beta} \ln \frac{1-u(\phi)}{1-u_{m}^{e}},
\end{aligned}
$$
where we use Eq. (59) to get the second equality. Eqs. (30) and (41) yield the GB energy
$$
\sigma=\frac{4}{\pi} \sigma_{A} \int_{0}^{1} \sqrt{g(\phi)+\frac{1}{\beta \omega_{A}} \ln \frac{1-u(\phi)}{1-u_{m}^{e}}} d \phi.
$$

At the limit of vanishing solute content, $u_{m}^{e} \rightarrow 0$, the effective potential $\Omega_{1}(\phi)$ is reduced to the double-well potential $\omega_{A} g(\phi)$ of pure solvent $A$. The GB segregation level and GB energy are dependent on parameter $\alpha$ and the matrix composition $u_{m}^{e}$. For a given $\alpha, \sigma$ decreases with the increasing matrix composition $u_{m}^{e}$ because the integral $\int_{0}^{1} \sqrt{\Omega_{1}(\phi)} d \phi$ decreases as in Fig. 4. However, there exists an upper bound in $u_{m}^{e}$ and $u_{g}^{e}$ over which $\Omega_{1}(1 / 2)<0$, so the equilibrium phase-field profile does not exist. As shown in Fig. 3(b),

they correspond to the common tangent compositions ($u_m^{ct}$ and $u_g^{ct}$) of the matrix and GB phases on the free energy diagram. For the free energy densities (53) and (54), they are given by

$$
u_{m}^{ct}=\frac{e^{\beta \omega_{A}}-1}{e^{\alpha \beta \omega_{A}}-1} \quad \text { and } \quad u_{g}^{ct}=\frac{e^{\alpha \beta \omega_{A}}\left(e^{\beta \omega_{A}}-1\right)}{e^{\beta \omega_{A}}\left(e^{\alpha \beta \omega_{A}}-1\right)}.
\tag{63}
$$

By inserting the composition profile (59) into Eq. (62) and numerically integrating it, we can obtain the GB energy as a func- tion of the matrix composition $u_m^e$ for the given parameters. We take typical parameters for iron: $v_m = 1.06 × 10^{-5} m^3/mol$, $T = 1273$ K, $\sigma_A = 1$ J/m² and $2\xi_A = 1$ nm. We get $\beta = v_m/RT = 1.0 × 10^{-9}$ J/m³, $\omega_A = \sigma_A/2\xi_A = 1.0 × 10^9$ J/m³, and then $\beta\omega_A = 1.0$. For three selected parameters of $\alpha = 2, 3$ and 4, the changes of GB composition and the GB energy obtained by nu- merical integration are shown in Fig. 5. In Fig. 5(a), $u_g^e$ increases with $u_m^e$ and more rapidly for a larger $\alpha$ value. The upper bounds on $u_m^e$ and $u_g^e$ over which the equilibrium phase-field profile and GB energy cannot be defined are determined from Eq. (63) for each $\alpha$ value, as indicated by filled circles in Fig. 5(a). At the limit of $\alpha \to \infty$, the upper bound on $u_g^e$ converges to a constant value of $(e-1)/e=0.632$. In Fig. 5(b), the GB energies decrease with increasing $u_m^e$ more rapidly for a larger $\alpha$ value but reaches the lower bounds indicated by the filled circles, where $u_m^e = u_m^{ct}$. Over this composi- tion, the integration to obtain the GB energy is not possible because $\Omega_1(\phi)$ becomes negative around $\phi=1/2$. For a fixed matrix composition, the GB energy is dependent on the $\alpha$ value. Let us take an example with $u_m^e=0.09$. From Fig. 5(b), we read $\sigma=0.41$ J/m² for $\alpha=3, \sigma>0.41$ J/m² for $\alpha<3$ and no solution of $\sigma$ for $\alpha>3$. In the system with $u_m^e=0.09$, therefore, the GB energy cannot be decreased under $0.41$ J/m², no matter how $\alpha$ changes. Such a re- striction on the GB energy reduction by segregation in the present model I originates from the equal composition condition, as explained in the previous section. It disappears in the next section on model II, where we adopt the equal diffusion potential condition.

### 4.2. Properties of model II

A point $\boldsymbol{x}$ in the system is composed of a matrix phase with a composition $u_m(\boldsymbol{x})$ and a GB phase with a composition $u_g(\boldsymbol{x})$. In model II, the two compositions at the point are correlated by the equal diffusion potential condition (18). For the free energy den- sities of Eqs. (53) and (54), this condition reads

$$
\frac{u_{g}(\boldsymbol{x})}{1-u_{g}(\boldsymbol{x})}=\frac{u_{m}(\boldsymbol{x})}{1-u_{m}(\boldsymbol{x})} \exp \left(\alpha \beta \omega_{A}\right).
\tag{64}
$$

Additionally, one can see that

$$
f^{g}\left(u_{g}\right)-f^{m}\left(u_{m}\right)-\left(u_{g}-u_{m}\right) \frac{d f^{m}\left(u_{m}\right)}{d u_{m}}=\left(\omega_{A}+\frac{1}{\beta} \ln \frac{1-u_{g}}{1-u_{m}}\right).
\tag{65}
$$

This leads to the phase-field equation

$$
\frac{1}{M_{\phi}} \frac{\partial \phi}{\partial t}=\varepsilon^{2} \nabla^{2} \phi-\left(\omega_{A}+\frac{1}{\beta} \ln \frac{1-u_{g}}{1-u_{m}}\right) \frac{d g(\phi)}{d \phi}
\tag{66}
$$

and the diffusion equation

$$
\frac{\partial u}{\partial t}=\nabla \cdot \frac{M_{d}}{\beta u_{m}\left(1-u_{m}\right)} \nabla u_{m}.
\tag{67}
$$

Model II for the present free energy densities is composed of the effective composition (7), equal diffusion potential condition (64), phase-field equation (66) and diffusion equation (67). Another form (26) of the diffusion equation may be adopted instead of Eq. (67). In the equilibrium state without solute flux in the system, the $u_m$ should be constant over the whole space of the system, and Eq. (64) yields

$$
\frac{u_{g}^{e}}{1-u_{g}^{e}}=\frac{u_{m}^{e}}{1-u_{m}^{e}} \exp \left(\alpha \beta \omega_{A}\right),
\tag{68}
$$

which is same as Eq. (60) in model I. The equilibrium concentration profile in the interfacial region is

$$
u(\phi)=g(\phi) u_{g}^{e}+(1-g(\phi)) u_{m}^{e}.
\tag{69}
$$

It should be noted that although the relationship between the compositions of $u_m^e$ and $u_g^e$ are the same in both model I and II, composition profiles (59) in model I and (69) in model II across the GB region are quite different from each other.

The free energy densities of Eqs. (53) and (54) yield the parameter $\omega^e$, defined by Eq. (5) as

$$
\omega^{e}=\omega_{A}+\frac{1}{\beta} \ln \frac{1-u_{g}^{e}}{1-u_{m}^{e}}.
\tag{70}
$$

From Eq. (52), we then get the GB energy

![](./images/814530487358849025_6.jpg)

Fig. 5. (a) GB composition changes and (b) GB energy changes with matrix composition for the parameters $\alpha=2,3$ and 4. The upper bounds on $u_m^e$ and $u_g^e$ over which the equilibrium phase-field profile and GB energy cannot be defined are indicated by filled circles.

$$
\sigma=\sigma_{A} \sqrt{1+\frac{1}{\beta \omega_{A}} \ln \frac{1-u_{g}^{e}}{1-u_{m}^{e}}}=\sigma_{A} \sqrt{1+\frac{2 \xi_{A}}{\beta \sigma_{A}} \ln \frac{1-u_{g}^{e}}{1-u_{m}^{e}}},
\tag{71}
$$

where we used Eq. (32) for the parameter $\omega_{A}$. On the other hand, the GB energy [23-26] for the classical two-phase model is given by Eq. (6), which is written as

$$
\sigma=\sigma_{A}\left(1+\frac{2 \xi_{A}}{\beta \sigma_{A}} \ln \frac{1-u_{g}^{e}}{1-u_{m}^{e}}\right).
\tag{72}
$$

As discussed in the previous section, the difference between Eqs. (71) and (72) originates from which variable is taken as a constant in the models: the GB width in the classical two-phase model and the gradient energy coefficient in model II. Fig. 6 shows the GB energy changes with the matrix composition, which were obtained by inserting Eq. (68) into Eq. (71). Other parameters were the same as those in Fig. 5. The black, blue and red solid curves are the GB energies from model II for $\alpha=2,3$ and 4, respectively. For comparison, the GB energies from model I and the classical two-phase model (Eq. (72)) are also presented as the dashed lines and dotted lines, respectively. The GB energy from model II shows a faster decrease with the increasing matrix composition compared with that from model II. As noted in the previous section, it can decrease to zero, without the bound that is unavoidable in model I. The difference between the GB energies from model II and the classical two-phase model is considerable, as expected from the difference between the $\sqrt{\omega^{e}}$ and $\omega^{e}$ dependencies.

## 5. Discussion

In the previous sections, we examined the thermodynamic properties of models I and II and compared them with each other and the classical two-phase model. All the models resulted in the same GB composition, which is given by the parallel tangent construction. However, the GB energies appeared to be quite different from each other. The differences between models I and II originated from the equal composition condition in the former and the equal diffusion potential condition in the latter. The differences between model II and the classical two-phase model originated from the assumptions of the constant gradient energy coefficient in the former and the constant GB width in the latter. It is far from conclusive which conditions and which assumptions are more realistic in views of the real physics and chemistry of the GBs. An example is the GB energy change with the matrix composition. Kirchheim [5] reported that the GB energy could be vanishingly small in some nanocrystalline materials due to the GB segregation. This seems to exclude the existence of a lower bound to the GB energy, which is a characteristic of model I. His argument is based on the existence of an equilibrium-like grain size in nanocrystalline materials. However, it is not still conclusive whether its existence is of thermodynamic origin or not [20-22]. The best way to examine the applicability of the models to real materials is to compare the predicted compositional dependency of the GB energy with that from experimental measurements. At the present stage, however, there are too limited experimental data to make any meaningful comparison between the models.

![](./images/814530487358849025_7.jpg)

Fig. 6. GB energy changes with the matrix composition. The black, blue and red solid curves are the GB energies for $\alpha=2,3$ and 4, respectively. Solid lines, dashed lines and dotted lines represent the GB energy changes from model II, model I and classical two-phase model, respectively. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

The constant gradient energy coefficient $\varepsilon$ is an assumption common to models I and II, and thereby, the compositional dependency of the GB width follows. However, this may not be an intrinsic characteristic of the phase-field model of GB segregation. If one allows $\varepsilon$ to depend on the composition, the resultant PFM will show a different compositional dependency for the GB width, or possibly even a constant GB width. Such a model with a constant or nearly constant GB width may be useful, in particular, for enhancing the computational efficiency in a grain growth simulation where the GB width should be maintained sufficiently smaller than the grain size.

The PFM on the real scale must be one of the useful tools for modeling the real GB with segregation. However, it is more powerful in simulating the microstructure evolution on the mesoscale. For the mesoscale simulation for grain growth with GB segregation to operate in a quantitatively correct way, both the GB energy and the solute drag force should be maintained at the prescribed or predicted values, independent of the GB width. In mesoscale simulations, one should adopt a grid size $(\Delta x)$ and GB width much larger than the real GB width. For example, employing the scales of $\Delta x \sim 0.2 \mu \mathrm{m}$ and $2 \xi \sim 1 \mu \mathrm{m}$ is not uncommon in phase-field simulations of grain growth. This enormously exaggerated GB width brings about highly anomalous values of i) total solute content in the GB region, ii) GB composition (concentration in the center of GB region), iii) GB energy and iv) solute drag force on a GB moving under a driving force. An effective remedy [41,45] for such a situation has been proposed and successfully applied to the mesoscale simulation of grain growth by a PFM under an ideal solution approximation which belongs to model I. This is based on the observation that all of the segregation profile $u(\phi)$, the GB energy and the solute drag force in the low GB velocity regime are governed by the same parameter $\beta \omega_{A}$, which is equivalent to $\sigma_{A} \beta / 2 \xi_{A}$ because of Eq. (32). That is, if we regard $\beta(=v_{m} / R T)$ as a control parameter and maintain $\beta / 2 \xi_{A}$ unchanged from the real physical value, the same segregation profile $u(\phi)$, GB energy and solute drag force as those on the real scale will play their roles in the microstructural evolution during the mesoscale simulation, even with the enormously exaggerated GB width. This remedy can be applied to not only model I but also model II. This is because the same parameter $\beta \omega_{A}$ governs the GB energies of Eq. (62) in model I and Eq. (71) in model II, and it also governs the solute drag force in the low velocity regime in both models. (The latter fact can be shown by examining the steady motion of a planar GB under a constant driving force, as in Refs. [37,41]. In particular, the solute drag effect was clearly observed in a simulation for a dilute solution version [37] of model II and its dynamics also appeared to be in a close agreement with a prediction from the classic model by Cahn [28].). Also note that the segregation profiles of Eq. (59) in model I and Eqs. (68) and (69) in model II are governed by the parameter $\beta \omega_{A}$. As far as the thermodynamic and kinetic properties of the GBs in the mesoscale simulation are controlled to maintain those on the

real scale, however, the exaggerated total solute content in the GB region is unavoidable.

Throughout this study, we used the function $g(\phi)=4 \phi(1-\phi)$ as the dual meaning of both the GB phase fraction and the double-well potential. In order to apply the present models for simulating grain growth in polycrystalline system, however, we should modify the definition of GB phase fraction to take into account the multiple junctions. This can be easily done by following the multi-phase field model (MPFM) [34,46,51] for grain growth. In this MPFM, the double-well potential $g$ in a polycrystalline system is represented as

$$
g=4 \sum_{p>q}^{n} \sum_{q}^{n} \phi_{p} \phi_{q},
\tag{73}
$$

where $\phi_{p}$ is the phase-field value of the $p$ grain and $n$ is the total number of the grains coexisting at a point in the system. With the definition (73), we can get the effective concentration $u=g u_{g}+(1-g) u_{m}$ at a given point and the free energy density as $f=g f^{g}\left(u_{g}\right)+(1-g) f^{m}\left(u_{m}\right)$ which are basically the same form as Eqs. (7) and (8), respectively. For a system with two grains denoted by $\phi_{1}=1$ and $\phi_{2}=1$, respectively, Eq. (73) is reduced to the previous case of $g=4 \phi_{1} \phi_{2}=4 \phi_{1}\left(1-\phi_{1}\right)$. (Note that the total sum of the phase fields coexisting at a point is unity in the MPFM.). It should be noted that there is a delicate problem related with the multiple junctions. For example, let us consider a triple junction region where the phase fields of $\phi_{1}, \phi_{2}$ and $\phi_{3}$ coexist. At the center of the region, we see the phase-field values of $\phi_{1}=\phi_{2}=\phi_{3}=1 / 3$ and then obtain $g=4\left(\phi_{1} \phi_{2}+\phi_{1} \phi_{3}+\phi_{2} \phi_{3}\right)=4 / 3$. Thus, the definition (73) implies that a multiple junction would have a higher energy and stronger segregation level than those of GB between two grains. This situation is not unreasonable in view of the existence of the additional energy at multiple junctions. Another form of $g$ can be employed, however, if this additional energy at multiple junctions should be avoided. At multiple junctions where $n$ different grains coexist, the maximum value of the function $4 \sum_{p>q}^{n} \sum_{q}^{n} \phi_{p} \phi_{q}$ is given by $2(n-1) / n$ at $\phi_{1}=\phi_{2}=\ldots=1 / n$. So, if we define the GB phase fraction and double-well potential as

$$
g=\frac{2 n}{(n-1)} \sum_{p>q}^{n} \sum_{q}^{n} \phi_{p} \phi_{q},
\tag{74}
$$

$g=1$ can be maintained at the center of multiple junctions. The choice between Eqs. (73) and (74) will depend on the real characteristics of multiple junctions, which is beyond the scope of MPFM.

One interesting question is what occurs if the matrix composition is deliberately increased over $u_{m}^{c t}$ (common tangent composition of the matrix phase) in a system with a fixed grain size. In the case of the classical two-phase model, the GB energy becomes negative because the two parallel tangent lines in Fig. 1 change their relative positions. In a system with a negative GB energy, according to the definition of the GB energy, the free energy loss due to the solute transfer into the newly formed GB region in the matrix phase exceeds the free energy gain due to the new GB region formation itself. As the result, new GBs would be spontaneously formed to increase the GB area at the expense of the matrix phase. Meanwhile, the matrix composition reaches $u_{m}^{c t}$ as the result of excess solute absorption into the new GB regions. For the cases of models I and II, we examined the GB behavior by 1D numerical simulation on a system with a straight GB. Just after the matrix composition was increased over $u_{m}^{c t}$, in both models I and II, the width of the GB region was anomalously increased. The next evolution appeared quite different in the two models. The thickened GB region in model II was continuously changed into two separate GB regions and a new grain between them, like a phase separation phenomenon. This occurrence of recrystallization implies that the original GB energy was negative, as expected in model II. During the recrystallization process, the composition of the matrix phase was reduced to just below the common tangent composition, and the phase-field profiles in two GB regions become stable. On the other hand, the GB region in model I was thickened without new GB formation until the composition of the matrix phase was reduced to just below the common tangent composition. In the final stationary state, the phase-field profile remained much broader than the equilibrium profile given by Eq. (39). No recrystallization in model I is an expected result because the GB energy in model I cannot be negative, as explained in the section 3.2. Such a 'segregation-induced recrystallization' expected during alloying in model II and the classical two-phase model is possibly related to the diffusion-induced recrystallization phenomenon [52-55], where new grains are formed on the surface or GBs during the alloying or dealloying of materials. Examining the diffusion-induced recrystallization in view of the segregation-induced recrystallization will be of interest for future study.

## 6. Conclusions

In this study, we developed phase-field models for GB segregation that are diffuse interface versions of the classical two-phase model of GB segregation. The thermodynamic state of a point in the system is represented as a mixture of a GB phase and a matrix phase. There are two choices for the thermodynamic relation between the GB phase and the matrix phase that constitute the point: the equal composition condition in model I and the equal diffusion potential condition in model II. Most previous PFMs for GB segregation appear to be specific cases of model I. We examined the thermodynamic properties of models I and II and compared them with each other and the classical two-phase model. All the models resulted in the same GB composition, determined by the parallel tangent construction on the free energy diagram. However, the GB energy and its dependency on the composition in the equilibrium state appeared to be quite different for the two models. In model I, there is a lower bound to the GB energy that originates from the equal composition condition. The GB energy from model II with the equal diffusion potential condition shows no such lower bound and can be vanishingly small. This GB energy on the free energy diagram is represented as the vertical distance between the parallel tangent lines, multiplied by the GB width. This is exactly the same form as that from the classical two-phase model. Nevertheless, the compositional dependence of model II is quite different from that in the classical two-phase model. This originates from the different choice of the composition-independent parameter in the models: a constant gradient energy coefficient in model II and a constant GB width in the classical two-phase model. Model I is not suitable for simulations of alloys that show a reduction of the GB energy due to GB segregation below a certain limit (in dilute alloys, about half of the GB energy of pure solvents). Model II is a correct choice for such alloys. In mesoscale simulations of grain growth, an enormously exaggerated GB width is often adopted. For such a simulation with GB segregation to operate in a quantitatively correct way, both the GB energy and the solute drag force should be maintained at the prescribed or predicted values, independent of the GB width $2 \xi$. This can be done by regarding $\beta\left(=v_{m} / R T\right)$ as a control parameter and keeping $2 \xi / \beta$ constant, independent of GB width. Finally, we discussed the segregation-induced recrystallization phenomenon that appears in the simulation using model II.

### Acknowledgement

This research was supported by Basic Science Research Program through the National Research Foundation of Korea (NRF) funded by the Ministry of Education (13A13907350).

### References

[1] G. Gottstein, L.S. Shvindlerman, Grain Boundary Migration in Metals: Thermodynamics, Kinetics, Applications, second ed., CRC Press, Bota Raton, 2009.
[2] P. Lejcek, S. Hofmann, Thermodynamics and structural aspects of grain boundary segregation, Crit. Rev. Solid State Mater. Sci. 20 (1995) 1-85.
[3] K.A. Darling, R.N. Chan, P.Z. Wong, J.E. Semones, R.O. Scattergood, C.C. Koch, Grain-size stabilization in nanocrystalline FeZr alloys, Scr. Mater. 59 (2008) 530-533.
[4] B. Farber, E. Cadel, A. Menand, G. Schmitzi, R. Kirchheim, Phosphorus segregation in nanocrystalline Ni-3.6 at.% P alloy investigated with the tomographic atom probe, Acta Mater. 48 (2000), 789-976.
[5] R. Kirchheim, Grain coarsening inhibited by solute segregation, Acta Mater. 50 (2002) 413-419.
[6] P. Choi, M. da Silva, U. Klement, T. Al-Kassab, R. Kirchheim, Thermal stability of electrodeposited nanocrystalline Co-1.1 at.% P 53, Acta Mater. (2005) 4473-4481.
[7] E. Botcharova, J. Freudenberger, L. Schultz, Mechanical and electrical properties of mechanically alloyed nanocrystalline Cu-Nb alloys, Acta Mater. 54 (2006) 3333-3341.
[8] C.C. Koch, R.O. Scattergood, K.A. Darling, J.E. Semones, Stabilization of nanocrystalline grain sizes by solute additions, J. Mater. Sci. 43 (2008) 7264-7272.
[9] M. Thuvander, M. Abraham, A. Cerezo, G.D.W. Smith, Thermal stability of electrodeposited nanocrystalline nickel and iron-nickel alloys, Mater. Sci. Tech. 17 (2001) 961-970.
[10] B.K. VanLeeuwen, K.A. Darling, C.C. Koch, R.O. Scattergood, B.G. Butler, Thermal stability of nanocrystalline Pd₈₁Zr₁₉, Acta Mater. 58 (2010) 4292-4297.
[11] A.J. Detor, M.K. Miller, C.A. Schuh, Measuring grain-boundary segregation in nanocrystalline alloys: direct validation of statistical techniques using atom probe tomography, Phil. Mag. Lett. 87 (2007) 581-587.
[12] P.C. Millett, R.P. Selvam, A. Saxena, Stabilizing nanocrystalline materials with dopants, Acta Mater. 55 (2007) 2329-2336.
[13] F. Tang, D.S. Gianola, M.P. Moody, K.J. Hemker, J.M. Cairney, Observations of grain boundary impurities in nanocrystalline Al and their influence on microstructural stability and mechanical behaviour, Acta Mater. 60 (2012) 1038-1047.
[14] Y. Li, D. Raabe, M. Herbig, P.-P. Choi, S. Goto, A. Kostka, H. Yarita, C. Borchers, R. Kirchheim, Segregation stabilizes nanocrystalline bulk steel with near theoretical strength, Phys. Rev. Lett. 113 (2014) 106104.
[15] F. Liu, R. Kirchheim, Grain boundary saturation and grain growth, Scr. Mater. 51 (2004) 521-525.
[16] A.J. Detor, C.A. Schuh, Grain boundary segregation, chemical ordering and stability of nanocrystalline alloys: atomistic computer simulations in the Ni-W system, Acta Mater. 55 (2007) 4221-4232.
[17] K.A. Darling, B.K. VanLeeuwen, J.E. Semones, C.C. Koch, R.O. Scattergood, L.J. Kecskes, S.N. Mathaudhu, Stabilized nanocrystalline iron-based alloys: guiding efforts in alloy selection, Mater. Sci. Eng. A 528 (2011) 4365-4371.
[18] H.A. Murdoch, C.A. Schuh, Stability of binary nanocrystalline alloys against grain growth and phase separation, Acta Mater. 61 (2013) 2121-2132.
[19] M. Saber, C.C. Koch, R.O. Scattergood, Thermodynamic grain size stabilization models: an overview, Mater. Res. Lett. 3 (2015) 66-75.
[20] L.S. Shvindlerman, G. Gottstein, Reply to comments on "unexplored topics and potentials of grain boundary engineering", [Scripta Materialia, 54 (2006) 1041-1045], Scr. Mater. 55 (2006) 965-966.
[21] R. Kirchheim, Comment on "Unexplored topics and potentials of grain boundary engineering" by LS Shvindlerman and G. Gottstein, Acta Mater. 55 (2006) 963-964.
[22] G. Gottstein, L.S. Shvindlerman, Unexplored topics and potentials of grain boundary engineering, Scr. Mater. 54 (2006) 1041-1045.
[23] J.A.V. Butler, The thermodynamics of the surfaces of solutions, Proc. Roy. Soc. Lond. A 135 (1932) 348-375.
[24] M. Hillert, in: H.I. Aaronson (Ed.), Lectures on the Theory of Phase Transformations, 1975, pp. 1-33 (Am. Inst. Min. Pet. Metall. Eng. New York.
[25] T. Tanaka, K. Oack, S. Hara, Calculation of surface tension of liquid Bi-Sn alloy using thermochemical application library ChemApp, Calphad 24 (2000) 465-474.

[26] Y.B. Kang, Relationship between surface tension and Gibbs energy, and application of constrained Gibbs energy minimization, Calphad 50 (2015) 23-31.
[27] K. Lücke, K. Detert, Acta Metall. 5 (1957) 628.
[28] J.W. Cahn, The impurity-drag effect in grain boundary motion, Acta Metall. 10 (1962) 789-798.
[29] M. Hillert, Solute drag, solute trapping and diffusional dissipation of Gibbs energy, Acta Mater. 47 (1999) 4481-4505.
[30] M.I. Mendelev, D.J. Srolovitz, A regular solution model for impurity drag on a migrating grain boundary, Acta Mater. 49 (2001) 589-597.
[31] J.A. Warren, W.J. Boettinger, Prediction of dendritic growth and microsegregation patterns in a binary alloy using the phase-field method, Acta Metall. Mater. 43 (1995) 689-703.
[32] I. Steinbach, F. Pezzolla, B. Nestler, M. Seeßelberg, R. Prieler, G.J. Schmitz, A phase field concept for multiphase systems, Phys. D. 94 (1996) 135-147.
[33] S.G. Kim, W.T. Kim, T. Suzuki, Phase-field model for binary alloys, Phys. Rev. E 60 (1999) 7186-7197.
[34] I. Steinbach, F. Pezzolla, A generalized field method for multiphase transformations using interface fields, Phys. D. 134 (1999) 385-393.
[35] A. Karma, W.J. Rappel, Quantitative phase-field modeling of dendritic growth in two and three dimensions, Phys. Rev. E 57 (1998) 4323-4349.
[36] A. Karma, Phase-field formulation for quantitative modeling of alloy solidification, Phys. Rev. Lett. 87 (2001) 115701.
[37] P.R. Cha, S.G. Kim, D.H. Yeon, J.K. Yoon, A phase field model for the solute drag on moving grain boundaries, Acta Mater. 50 (2002) 3817-3829.
[38] D. Fan, S.P. Chen, L.Q. Chen, Computer simulation of grain growth kinetics with solute drag, J. Mater. Res. 14 (1999) 1113-1123.
[39] M. Bouville, S. Hu, L.Q. Chen, D. Chi, D.J. Srolovitz, Phase-field model for grain boundary grooving in multi-component thin films, Model. Sim. Mater. Sci. Eng. 14 (2006) 433-443.
[40] K. Grönhagen, J. Ågren, Grain-boundary segregation and dynamic solute drag theory-A phase-field approach, Acta Mater. 55 (2007) 955-960.
[41] S.G. Kim, Y.B. Park, Grain boundary segregation, solute drag and abnormal grain growth, Acta Mater. 56 (2008) 3739-3753.
[42] J. Li, J. Wang, G. Yang, Phase field modeling of grain boundary migration with solute drag, Acta Mater. 57 (2009) 2108-2120.
[43] Y. Mishin, W.J. Boettinger, J.A. Warren, G.B. McFadden, Thermodynamics of grain boundary premelting in alloys. I. Phase-field modeling, Acta Mater. 57 (2009) 3771-3785.
[44] F. Abdeljawad, S.M. Foiles, Stabilization of nanocrystalline alloys via grain boundary segregation: a diffuse interface model, Acta Mater. 101 (2015) 159-171.
[45] K.-M. Kim, H.-K. Kim, J.Y. Park, J.S. Lee, S.G. Kim, N.J. Kim, B.-J. Lee, {100} texture evolution in bcc Fe sheets-computational design and experiments, Acta Mater. 106 (2016) 106-116.
[46] I. Steinbach, Phase-field models in materials science, Model. Sim. Mater. Sci. Eng. 17 (2009) 073001.
[47] S.G. Kim, W.T. Kim, T. Suzuki, Interfacial compositions of solid and liquid in a phase-field model with finite interface thickness for isothermal solidification in binary alloys, Phys. Rev. E 58 (1998) 3316-3323.
[48] S.G. Kim, W.T. Kim, T. Suzuki, M. Ode, Phase-field modeling of eutectic solidification, J. Cryst. Growth 261 (2004) 135-158.
[49] J. Eiken, B. Böttger, I. Steinbach, Multiphase-field approach for multicomponent alloys with extrapolation scheme for numerical application, Phys. Rev. E 73 (2006) 066122.
[50] S.G. Kim, A phase-field model with antitrapping current for multicomponent alloys with arbitrary thermodynamic properties, Acta Mater. 55 (2007) 4391-4399.
[51] S.G. Kim, D.I. Kim, W.T. Kim, Y.B. Park, Computer simulations of two-dimensional and three-dimensional ideal grain growth, Phys. Rev. E 74 (2006) 061605.
[52] T.A. Parthasarathy, P.G. Shewmon, Diffusion induced recrystallization of NiO, Acta Metall. 32 (1984) 29-33.
[53] Y. Kawanami, M. Nakano, M. Mori, Growth rate of fine grains formed by diffusion induced recrystallization in Ni layer of Cu/Ni/Cu diffusion couples, Mater. Trans. 1 (1998) 218-224.
[54] N. Goukon, T. Ikeda, M. Kajihara, Growth behavior of fine grains formed by diffusion induced recrystallization in the Cu (Zn) system, Acta Mater. 48 (2000) 2959-2968.
[55] M. Kasprzak, D. Baither, G. Schmitz, Diffusion-induced recrystallization in nickel/palladium multilayers, Acta Mater. 59 (2011) 1734-1741.