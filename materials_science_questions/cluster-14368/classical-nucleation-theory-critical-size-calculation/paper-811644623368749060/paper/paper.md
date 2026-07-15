Minimizing the Gibbs–Thomson effect in the low-temperature plasma synthesis of thin Si nanowires

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2011 Nanotechnology 22 315707

(http://iopscience.iop.org/0957-4484/22/31/315707)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 155.69.4.4
This content was downloaded on 20/05/2015 at 10:41

Please note that terms and conditions apply.

# Minimizing the Gibbs-Thomson effect in the low-temperature plasma synthesis of thin Si nanowires

H Mehdipour¹,², K Ostrikov²,³, A E Rider² and S A Furman²

¹ Department of Physics, Faculty of Science, Sahand University of Technology, 51335-1996 Tabriz, Iran
² Plasma Nanoscience Center Australia (PNCA), CSIRO Materials Science and Engineering, PO Box 218, Lindfield, New South Wales 2070, Australia
³ Plasma Nanoscience, School of Physics, The University of Sydney, Sydney, New South Wales 2006, Australia

E-mail: Amanda.Rider@csiro.au

Received 18 February 2011, in final form 21 June 2011
Published 7 July 2011
Online at stacks.iop.org/Nano/22/315707

## Abstract
An advanced combination of numerical models, including plasma sheath, ion- and radical-induced species creation and plasma heating effects on the surface and within a Au catalyst nanoparticle, is used to describe the catalyzed growth of Si nanowires in the sheath of a low-temperature and low-pressure plasma. These models have been used to explain the higher nanowire growth rates, low-energy barriers, much thinner Si nanowire nucleation and the less effective Gibbs-Thomson effect in reactive plasma processes, compared with those of neutral gas thermal processes. The effects of variation in the plasma sheath parameters and substrate potential on Si nanowire nucleation and growth have also been investigated. It is shown that increasing the plasma-related effects leads to decreases in the nucleation energy barrier and the critical nanoparticle radius, with the Gibbs-Thomson effect diminished, even at low temperatures. The results obtained are consistent with available experimental results and open a path toward the energy- and matter-efficient nucleation and growth of a broad range of one-dimensional quantum structures.

(Some figures in this article are in colour only in the electronic version)

## 1. Introduction
Highly uniform arrays of nanowires (NWs) and other high-aspect-ratio nanostructures hold outstanding promise as components in numerous applications including electron microemitter arrays, nanoelectronic circuitry, biosensors, drug and gene delivery systems, and other nanodevices [1–14]. For implementation in such devices, a high degree of control over the NW characteristics from the very initial stage of growth is required. Silicon NWs are commonly synthesized using a variety of catalyzed chemical vapor deposition (CVD) [15–18], molecular beam epitaxy (MBE) [19–21], metalorganic vapor phase epitaxy (MOVPE) [22, 23], high-temperature annealing, and thermal evaporation [24–26] techniques. In catalyzed CVD synthesis of NWs, after the formation of a pattern of metal catalyst nanoparticles (NPs) on a substrate and the addition of the precursor gas (silane gas in this study) into the growth environment, NW growth usually proceeds via the vapor–liquid–solid (VLS) growth mode. The VLS growth mode may be described by four main stages [27]:

(i) the thermal and/or ion-assisted generation of building units (BUs) on the catalyst surface,
(ii) the saturation of the catalyst particles with adatoms which then absorb into the catalyst (followed by the formation of a Au–Si alloy),
(iii) a fast microscopic stage of nucleation of each Si monolayer (ML) from the liquid phase with constant liquid–catalyst radius $r_{\text{d}}$,
(iv) a slow macroscopic stage of NW growth from the vapor phase.

The properties of 1D nanostructures including nanowires and nanotubes [28–32] are heavily dependent on the characteristics (i.e., size and composition) of the catalyst nanoparticle from which they are nucleated. The Gibbs–Thomson (GT) effect describes the phenomenon whereby it becomes harder to nucleate nanowires the thinner they get (or rather, the smaller the catalyst nanoparticle, the larger the energy barrier for NW nucleation). This may be explained as follows: as the catalyst nanoparticles become smaller, their curvature increases and precursor atoms (Si atoms in this case) diffuse out of the catalyst NP due to high pressure inside the NP [33]—thus the energy barrier for NW nucleation increases as NWs get thinner [34], i.e. it becomes increasingly difficult to nucleate thin nanowires from small catalyst NPs. The commonly calculated critical radius of a liquid NP, below which NW nucleation ceases, is a function of the surface energy at the vapor–liquid interface, the droplet temperature and the supersaturation of liquid alloy in the droplet, $S$ [35–37]. It is thus clear that there is a lower size limit to NW growth which may only be overcome in thermal CVD processes through the use of higher process pressures (thus increased supersaturation of the catalyst particle) and higher temperatures [34]. Such an approach involving higher process pressures and temperatures is disadvantageous as it tends to result in NW defects [16] and is not an energy-efficient method [34]. The best approach is, therefore, to find a way to minimize the GT effect to achieve nucleation of thin NWs, rather than trying to forcefully overcome the lower size limit through energy-inefficient techniques.

One way to avoid the lower nucleation size limit and minimize the GT effect in order to grow thin NWs is to use plasma enhanced CVD (PECVD) for NW growth as opposed to conventional thermal CVD. It has been shown that it is possible to grow highly crystalline Si NWs, using a broad range of catalyst materials [38], via plasma-based methods [39]. This possibility is due in part to the ion and radical-assisted creation of building units on the topmost surface of a catalyst particle and the heating effects unique to the plasma environments [34, 40–45, 47]. Plasma-grown NWs typically do not bend (a common problem in epitaxy at low temperatures [23]). Moreover, they exhibit a fairly uniform diameter along the growth direction, at lower pressures [26], higher deposition rates and with substrate temperatures [48] remarkably lower than those in most neutral gas-based processes [20, 49] where the dissociation of the precursor gas is a rate-limiting step for NW growth. In contrast to neutral gases, it has been demonstrated experimentally that plasmas play a key role in the effective dissociation of precursor gases, both in the ionized gas phase and on the surface.

Although there exist many experimental reports on the nucleation and growth of NWs in low-temperature, non-equilibrium plasmas [26, 48, 50], to the best of our knowledge the interrelation between plasma bulk parameters, sheath thickness (or ion energy), plasma heating effects and the supersaturation of the BUs in the catalyst (and thus Si NW nucleation) has not been considered. Similarly, whilst the adverse effects induced by the GT effect during thin-NW nucleation and growth have been studied in neutral gas-based processes [27, 51], studies of the GT effect in plasma synthesis are limited [27]. Hence, in order to obtain a better insight into the PECVD of thin NWs and related nanostructures, where the GT effect can be minimized, an advanced combination of the plasma sheath, heating, radical- and ion-induced BU creation, and NW nucleation models should be applied to clearly describe what happens during the plasma-assisted catalyzed growth of NWs.

In this work, the plasma-sheath-related effects on catalyst heating and NW growth are investigated and the CVD and PECVD syntheses of thin NWs are directly compared. In particular, we investigate how the process parameters affect the catalyst temperature, supersaturation of BUs in the NP catalyst, formation of a Si monolayer and consequently the growth of thin NWs for which the GT effect (and thus the desorption flux from the NPs) becomes less significant in a plasma. It is demonstrated that variations in the plasma process parameters such as the electron density, electron temperature and substrate potential facilitate NW nucleation and growth mainly in low-temperature ranges where the thermal processes are less effective. Moreover, this makes it possible to dramatically reduce the importance of the GT effect and nucleate very thin nanowires with a narrow size distribution. Given that the characteristics of the NW nucleation are mainly determined by adatom diffusion through the NP surface and bulk, understanding the effect of the plasma sheath on the surface temperature and consequently on the adatom diffusion fluxes will provide a way to precisely control not only the Si NW nucleation characteristics at low process temperatures, but also the catalyzed growth of other one-dimensional (1D) nanostructures. This may ultimately make it possible to fabricate thin one-dimensional nanostructures with no external heating of the substrate.

The paper is organized as follows. In section 2, the main assumptions of the sheath, heating, BU creation as well as Si NW nucleation (and early-stage growth) models and main equations involved are presented. The results of numerical solutions for the energy barrier, critical radius and the growth rate and their dependence on the sheath parameters are presented in section 3 and discussed at greater length in section 4. Finally, the main findings are summarized in section 5 where an outlook for future work is also provided.

## 2. Numerical model and basic equations

### 2.1. General assumptions

Figure 1(a) is a schematic of the sheath configuration between an ${\rm Ar} + {\rm H}_2 + {\rm SiH}_4$ reactive plasma (the gas mixture commonly used in plasma-assisted experiments of Si NWs [48]) and a deposition surface. The plasma species fluxes and an array of NWs with Au NP droplets on their tips are also depicted. The sheath electric field $\mathbf{E}$ (due to the space charge separation) is directed along the $z$ axis and drives all ions toward the substrate. A schematic of the deposition of plasma species and subsequent BU bulk and surface diffusions (denoted by BD and SD, respectively) which commonly occur

![](./images/811644623368749060_1.jpg)

Figure 1. Schematic of (a) the geometry of the plasma sheath and (b) a Si NW with a catalyst particle at the tip of the structure, and surface and bulk diffusion processes. (c) High-resolution transmission electron microscope image of a Si NW grown via PECVD by Hofmann et al [50], reproduced with permission. Copyright 2003, American Institute of Physics.

in the VLS mechanism and a high-resolution transmission electron micrograph of a Si NW grown via PECVD are shown in figures 1(b) and (c), respectively. The main particles that interact with the surfaces of the Au droplet are silyl neutrals (SiH₃), silyl ions (SiH₃⁺), atoms and ions of the etching gas (here, atomic hydrogen H and the H⁺ ion) and argon atoms and ions (Ar and Ar⁺) all at the same temperature (Tᵢ).

### 2.2. The sheath model
Here, we have used a commonly accepted fluid approach [34, 40–42, 44–46] to investigate the effects of variation in plasma parameters on the dynamics of the plasma particles (especially the SiH₃⁺ ions) and on the characteristics of the plasma sheath formed near the substrate. The sheath equations,

$$
\frac{\mathrm{d}}{\mathrm{d} z}\left(n_{j} v_{j z}\right)=v_{I j} n_{\mathrm{e}}, \tag{1}
$$

$$
v_{j z} \frac{\mathrm{d} v_{j z}}{\mathrm{~d} z}=q_{j} \frac{\mathrm{d} \phi}{\mathrm{d} z}-\frac{T_{j}}{n_{j}} \frac{\mathrm{d} n_{j}}{\mathrm{~d} z}-m_{j} v_{j n} v_{j z}, \tag{2}
$$

$$
\frac{\mathrm{d}^{2} \phi}{\mathrm{d} z^{2}}=-4 \pi \sum_{j} q_{j} r_{j} n_{j}, \tag{3}
$$

are the continuity, momentum, and Poisson equations, respectively, where $j = \mathrm{e}, \mathrm{Ar}^{+}, \mathrm{SiH}_{3}^{+}, \mathrm{H}^{+}$. In equations (1)–(3), $m_j$ is the mass, $n_j$ is the number density, $v_{jz}$ is the z-component of the fluid velocity of particle species $j$, and $\phi$, $v_{Ij}$, $v_{jn}$, $T_j$ and $q_j$ are the sheath electric potential, the ionization frequency, the collision frequency with the neutrals, the species temperature and the charge, respectively [44]. In equation (2), the first term and the third term on the right-hand side express the acceleration of ion species $j$ by an electric field and the resistance due to collisions with the neutrals, respectively. The second term on the right-hand side of equation (2) describes the ion deceleration which is proportional to the ion temperature and influenced by the number density gradient. The quasi-neutrality condition at the sheath–plasma boundary (the sheath edge, $z = 0$) is $n_{\mathrm{e}0}-\sum_{j} r_{j} n_{j0}=0$, where $r_j$ is the $j$th-ion to electron number density ratio (or the jth gas to total gas pressure ratio). Here, we have used $\sum_{j} r_{j}=1$, where $0 < r_j < 1$ [45].

The sheath model [45] accounts for ion generation via electron impact ionization (as a function of the electron temperature, $T_\mathrm{e}$, and electron number density, $n_{\mathrm{e}0}$ [52]), which becomes more effective as the electron density and temperature are increased. For ion species $\alpha$ (where $\alpha = \mathrm{Ar}^{+}, \mathrm{SiH}_{3}^{+}$, and $\mathrm{H}^{+}$), the energy and flux at the substrate (Au NP surface) are $E_{\alpha}=\frac{1}{2}m_{\alpha}v_{\alpha}^{2}|_{z=\lambda_{\mathrm{s}}}$ and $J_{\alpha}=n_{\alpha}v_{\alpha}|_{z=\lambda_{\mathrm{s}}}$, respectively, where $\lambda_{\mathrm{s}}$ is the sheath width. The neutral argon, silyl, and hydrogen fluxes to the substrate are given by $j_{\alpha}=\bar{n}_{\alpha}v_{\mathrm{th}\alpha}/4$, where $v_{\mathrm{th}\alpha}=\sqrt{8T_{\alpha}/\pi m_{\alpha}}$ is the thermal velocity of species $\alpha$, and $\alpha = (\mathrm{Ar}, \mathrm{SiH}, \mathrm{H})$ stands for Ar, SiH₃, and H species, respectively [45].

### 2.3. The Si production and diffusion model
In the Si production and diffusion model, we have assumed that the Au NP catalyst (Au droplet) is a hemisphere with surface

area $A_{\mathrm{d}}=2 \pi r_{\mathrm{d}}^{2}$ (where $r_{\mathrm{d}}$ is the NP radius), contact angle $\beta=90^{\circ}$ and is initially at a temperature, $T_{\mathrm{d}}$, the same as that of the Si substrate. As shown in figure 1(b), the NP surface is affected by fluxes of all neutral and ion species (here, $\mathrm{Ar}, \mathrm{SiH}_{3}$, and $\mathrm{H}$, and $\mathrm{Ar}^{+}, \mathrm{SiH}_{3}^{+}$and $\mathrm{H}^{+}$) during PECVD growth of NWs. These species, upon reaching the substrate, undergo surface processes (which may contribute to either the Si production or loss on the catalyst surface) which can be categorized based on their importance in specific surface temperature ranges [42, 44, 45].

In the low-temperature range (i.e. below $600^{\circ} \mathrm{C}$ ), where the thermal dissociation of the precursor molecules is less effective, the most important processes are $\mathrm{SiH}_{3}^{+}$ion decomposition (ID), ion-induced dissociation (IID) of $\mathrm{SiH}_{3}$, and the loss of adsorbed particles through interaction with atomic hydrogen from the plasma sheath [45]. The first two processes, which are unique to PECVD, strongly depend on the flux $\left(J_{\mathrm{SiH}}\right)$ and energies of the $\mathrm{SiH}_{3}^{+}$ions at the substrate $\left(E_{\mathrm{SiH}}\right)$.

From the above assumptions, the main mass balance equations [45] on the catalyst surface are
$$
J_{\mathrm{Si}}^{+}+\operatorname{div}\left(D_{\mathrm{s}} \operatorname{grad} \tilde{n}_{\mathrm{Si}}\right)-J_{\mathrm{Si}}^{-}=0,
\tag{4}
$$
for the $\mathrm{Si}$ atoms and two similar equations for the $\mathrm{SiH}_{3}$ and $\mathrm{H}$ species. Here, the generation of $\mathrm{Si}$ atoms on the Au NP surface due to thermal and ion-induced dissociation of $\mathrm{SiH}_{3}$ radicals and the decomposition of $\mathrm{SiH}_{3}^{+}$ions is described by the first term in equation (4):
$$
J_{\mathrm{Si}}^{+}=\tilde{n}_{\mathrm{SiH}} v \exp \left(-E_{\mathrm{td}} / k_{\mathrm{B}} T_{\mathrm{d}}\right)+\theta_{\mathrm{SiH}} J_{\mathrm{SiH}} y_{\mathrm{d}}+J_{\mathrm{SiH}},
$$
where $k_{\mathrm{B}}$ is Boltzmann's constant, $v=10^{13} \mathrm{~Hz}$ is the thermal vibrational frequency, $E_{\mathrm{td}}$ is the energy barrier for thermal dissociation of $\mathrm{SiH}_{3}$ on the catalyst surface, $\tilde{n}_{\alpha}=\theta_{\alpha} v_{0}$ is the surface concentration of species $\alpha$ (where subscript $\alpha=\mathrm{SiH}$, $\mathrm{H}$, and $\mathrm{Si}$ stands for $\mathrm{SiH}_{3}, \mathrm{H}$, and $\mathrm{Si}$ species, $\theta_{\alpha}$ is the surface coverage by species $\alpha$ and $v_{0} \approx 1.4 \times 10^{15} \mathrm{~cm}^{-2}$ is the number of adsorption sites per unit area) and $y_{\mathrm{d}} \approx E_{\mathrm{SiH}} / E_{\mathrm{dis}}$, where $E_{\text {dis }} \approx 4.2 \mathrm{eV}$ is the dissociation energy for a $\mathrm{SiH}_{3}$ molecule in a vacuum. The second term in equation (4) accounts for the Si loss due to surface diffusion [45], where
$$
D_{\mathrm{s}}=D_{\mathrm{s} 0} \exp \left(-E_{\mathrm{sd}} / k_{\mathrm{B}} T_{\mathrm{d}}\right)
$$
is the surface diffusion coefficient (with an energy barrier $E_{\mathrm{sd}}$ adjusted by accounting for the polarizability of the adsorbed species [54]), with $D_{\mathrm{s} 0}$ a constant. The third term in equation (4) describes the $\mathrm{Si}$ atom loss due to evaporation, interaction of $\mathrm{Si}$ with atomic hydrogen from the sheath, and Si diffusion into the bulk of the NP as follows:
$$
J_{\mathrm{Si}}^{-}=\tilde{n}_{\mathrm{Si}} v \exp \left(-E_{\mathrm{ev}} / k_{\mathrm{B}} T_{\mathrm{d}}\right)+\tilde{n}_{\mathrm{Si}} \sigma_{\mathrm{ads}} j_{\mathrm{H}}+\pi \tilde{n}_{\mathrm{Si}} D_{\mathrm{b}} / A_{\mathrm{d}},
$$
where $E_{\mathrm{ev}}$ is the energy barrier for the evaporation of $\mathrm{Si}$ atoms, $D_{\mathrm{b}}$ is the bulk diffusion coefficient and $\sigma_{\text {ads }}\left(\approx 10^{-16} \mathrm{~cm}^{-2}\right)$ is the cross section for the reaction of atomic hydrogen with adsorbed particles [45].

From the mass balance equations [45], one can obtain the following equation for the surface concentration of $\mathrm{Si}$ atoms:
$$
D_{\mathrm{s}} \frac{1}{r_{\mathrm{d}}^{2} \sin \theta} \frac{\mathrm{d}}{\mathrm{d} \theta}\left(\sin \theta \frac{\mathrm{d} \tilde{n}_{\mathrm{Si}}}{\mathrm{d} \theta}\right)-\tilde{n}_{\mathrm{Si}} / t_{\mathrm{Si}}+F_{\mathrm{Si}}=0,
\tag{5}
$$
where $t_{\mathrm{Si}}^{-1}=(P+Q) / v_{0}$ is the inverse of the characteristic residence time of $\mathrm{Si}$ atoms on the NP surface and $F_{\mathrm{Si}}=P(M+$ $L)+J_{\mathrm{Si}}$ is the effective silicon flux to the NP surface. Here, $P=v_{0} v \exp \left(-E_{\mathrm{td}} / k_{\mathrm{B}} T_{\mathrm{d}}\right)+J_{\mathrm{Si}} y_{\mathrm{d}}, L=-j_{\mathrm{SiH}} J_{\mathrm{SiH}} /\left[B A-\hat{A} j_{\mathrm{SiH}}\right]$,
$$
\begin{aligned}
Q= & v_{0} v \exp \left(-E_{\mathrm{ev}} / k_{\mathrm{B}} T_{\mathrm{d}}\right)+v_{0} \sigma_{\mathrm{ads}} j_{\mathrm{H}} \\
& +v v_{0} \exp \left(-E_{\mathrm{bd}} / k_{\mathrm{B}} T_{\mathrm{d}}\right),
\end{aligned}
$$
$$
M=\left[B j_{\mathrm{SiH}}-j_{\mathrm{SiH}}\left(j_{\mathrm{H}}+J_{\mathrm{SiH}}\right)\right] /\left[B A-\hat{A} j_{\mathrm{SiH}}\right],
$$
$$
\begin{aligned}
A= & j_{\mathrm{SiH}}+J_{\mathrm{SiH}} y_{\mathrm{d}}+v_{0} \sigma_{\mathrm{ads}} j_{\mathrm{H}}+v_{0} v \exp \left(-E_{\mathrm{dSiH}} / k_{\mathrm{B}} T_{\mathrm{d}}\right) \\
& +v_{0} v \exp \left(-E_{\mathrm{td}} / k_{\mathrm{B}} T_{\mathrm{d}}\right),
\end{aligned}
$$
$$
\hat{A}=j_{\mathrm{H}}-v_{0} v \exp \left(-E_{\mathrm{td}} / k_{\mathrm{B}} T_{\mathrm{d}}\right)-J_{\mathrm{SiH}} y_{\mathrm{d}},
$$
$$
B=j_{\mathrm{H}}+v_{0} \sigma_{\mathrm{ads}}\left(j_{\mathrm{H}}+J_{\mathrm{H}}\right)+v_{0} v \exp \left(-E_{\mathrm{dH}} / k_{\mathrm{B}} T_{\mathrm{d}}\right),
$$
where $E_{\mathrm{bd}}$ is the energy barrier for Si diffusion into the catalyst nanoparticle bulk and $E_{\mathrm{d} \alpha}$ is the energy barrier for desorption of species $\alpha$.

To find the surface concentrations, especially that of $\mathrm{Si}$ atoms, $\tilde{n}_{\mathrm{Si}}$, from equation (5) appropriate boundary conditions are needed. First, it is assumed that the concentration of $\mathrm{Si}$ adatoms at the border of the catalyst surface $\left(\theta=90^{\circ}\right)$ is equal to zero, $\tilde{n}_{\mathrm{Si}}\left(90^{\circ}\right)=0$. Second, it is assumed that the surface diffusion flux vanishes at the top-most point of the droplet surface, namely $\left(\partial \tilde{n} /\left.\partial \theta\right|_{\theta=0^{\circ}}=0\right)$. By solving equation (5) with the boundary conditions mentioned, the Si concentration at each NP temperature may be obtained. Having found the silicon concentration, the surface coverages of $\mathrm{SiH}_{3}$ and $\mathrm{H}$ species and the total surface coverage $\left(\theta_{\mathrm{t}}=\sum_{j} \theta_{j}\right)$ can also be obtained. The Si fluxes through the bulk of the Au NP and its surface are
$$
J_{\mathrm{v}}=\int_{0}^{\pi / 2}\left(\pi \tilde{n}_{\mathrm{Si}} D_{\mathrm{b}} / A_{\mathrm{d}}\right) 2 \pi r_{\mathrm{d}}^{2} \sin \theta \mathrm{d} \theta
$$
and
$$
J_{\mathrm{s}}=-\left.2 \pi D_{\mathrm{s}}\left(\mathrm{d} \tilde{n}_{\mathrm{Si}} / \mathrm{d} \theta\right)\right|_{\theta=90^{\circ}},
$$
respectively, where $D_{\mathrm{b}}=\left(v A_{\mathrm{d}} / 2 \pi\right) \exp \left(-E_{\mathrm{bd}} / k_{\mathrm{B}} T_{\mathrm{d}}\right)$ is the bulk diffusion coefficient (for BU diffusion through the catalyst nanoparticle) determined with the energy barrier $E_{\mathrm{bd}}$ defined as above. The Si fluxes, $J_{\mathrm{s}}$ and $J_{\mathrm{v}}$, are of great importance in the calculation of the supersaturation of $\mathrm{Si}$ atoms in the catalyst NP.

### 2.4. The heat transfer model

To determine the temperature at any point on the Si substrate and also to establish how the NP droplet temperature $T_{\mathrm{d}}$ depends on the substrate holder temperature $T_{\mathrm{h}}$, the following steady state equation is used [45]:
$$
\frac{\mathrm{d}}{\mathrm{d} z}\left(\lambda_{\mathrm{Si}} \frac{\mathrm{d} T}{\mathrm{~d} z}\right)=0,
\tag{6}
$$
together with the boundary conditions (1) $T(z=0)=$ $T_{\mathrm{h}}$ and (2) the continuity of heat flux at the substrate- monolayer/droplet interface, i.e., $-\left.\lambda_{\mathrm{Si}} \mathrm{d} T / \mathrm{d} z\right|_{z=d}=Q_{\mathrm{M}}$ [45]. Here, $\lambda_{\mathrm{Si}}=\lambda_{0} \exp \left(-T / T_{0}\right)$ is the heat conductance of the silicon substrate [53] with $\lambda_{0}=2.07 \times 10^{7} \mathrm{erg} \mathrm{cm}^{-1} \mathrm{~K}^{-1}$,

$T_0 = 550$ K and $Q_{\text{M}}$ is the heat flux density to the droplet surface [45]. Therefore, $T_{\text{d}}$ and $T_{\text{h}}$ are connected by the following equation [45]:

$$
\exp (-T_{\text{d}} / T_{0})-\exp (-T_{\text{h}} / T_{0})=d Q_{\text{M}} / \lambda_{0}, \tag{7}
$$

where $Q_{\text{M}}=Q^{+}(T_{\text{d}})-Q^{-}(T_{\text{d}})$. Here, $Q^{+}$ and $Q^{-}$ describe the heating and cooling channels, respectively. For the heating channel [45] we have

$$
\begin{aligned}
Q^{+}(T_{\text{d}}) & =\sum_{\alpha} j_{\alpha}(1-\theta_{\mathrm{t}}) E_{\mathrm{d}\alpha}+H_{\mathrm{t}}^{i}+\bar{n}_{\mathrm{H}} \sigma_{\mathrm{ads}} j_{\mathrm{H}} P_{\mathrm{HAu}} \\
& \times\left(\delta E_{\mathrm{H}}-E_{\mathrm{dH}}\right)+\bar{n}_{\mathrm{H}} \sigma_{\mathrm{ads}} j_{\mathrm{H}}(\delta E_{\mathrm{H}}^{+}-E_{\mathrm{dH}}) \\
& +[\bar{n}_{\mathrm{Si}} \nu \exp (-E_{\mathrm{bd}} / k_{\mathrm{B}} T_{\mathrm{d}})-J_{\mathrm{v}} / A_{\mathrm{d}}] \delta E,
\end{aligned} \tag{8}
$$

where $\alpha=\text{SiH}$ and H. The first, second, third, fourth, and fifth terms in equation (8) describe the heat released on the droplet surface in the following processes: chemisorption of $\text{SiH}_3$ molecules and hydrogen atoms, ion bombardments (with the total heat $H_{\mathrm{t}}^{i}=\sum_{\alpha} E_{\alpha} J_{\alpha}$, where $\alpha=\text{SiH}_{3}^{+}, \text{H}^{+}$, and $\text{Ar}^{+}$), hydrogen atom recombination on an Au droplet surface with probability $P_{\text{HAu}} \approx 1$, the hydrogen ion neutralization, where $\delta E_{\mathrm{H}}$ is the energy released in the hydrogen atom recombination,

$$
\text{H (sheath) + H (surface)} \rightarrow \text{H}_2 \text{ (sheather)}+\delta E_{\text{H}} \text{ (=4.5 eV)},
$$

and $\delta E_{\mathrm{H}}^{+}$ is the energy released during hydrogen ion neutralization,

$$
\text{H}^{+} \text{ (sheath) + H (surface)} \rightarrow \text{H}_2 \text{ (sheath)}+\delta E_{\text{H}}^{+} \text{ (=13.2 eV)},
$$

on the surface, respectively, and finally the diffusion of Si from the droplet surface via its bulk [45]. In equation (8), $\delta E$ is the energy release at the dissolution of Si in the Au droplet, and $\bar{n}_{\alpha}$ is the averaged concentration of species $\alpha$ over the droplet surface.

The expression for $Q^{-}$, the cooling channel, is as follows:

$$
\begin{aligned}
Q^{-}(T_{\text{d}}) & =\bar{n}_{\text{SiH}} \nu \exp (-E_{\text{td}} / k_{\text{B}} T_{\text{d}}) E_{\text{td}}+\sum_{\alpha} \bar{n}_{\alpha} \nu \\
& \times \exp (-E_{\text{d}\alpha} / k_{\text{B}} T_{\text{d}}) E_{\text{d}\alpha}+\bar{n}_{\text{Si}} \nu \exp (-E_{\text{ev}} / k_{\text{B}} T_{\text{d}}) E_{\text{ev}} \\
& +\bar{n}_{\text{SiH}} \sigma_{\text{ads}} j_{\text{H}}(E_{\text{dSiH}}-\delta E_{\text{SiH}})+\bar{n}_{\text{Si}} \sigma_{\text{ads}} j_{\text{H}}(E_{\text{ev}}-\delta E_{\text{Si}}) \\
& +E_{\text{td}} \bar{n}_{\text{SiH}} J_{\text{SiH}} / v_{0}+1.5 k_{\mathrm{B}} \beta_{\mathrm{T}}(T_{\text{d}}-T_{\mathrm{i}}) j_{\mathrm{t}},
\end{aligned} \tag{9}
$$

where $\alpha=\text{SiH}$ and H and $\delta E_{\text{SiH}}$ and $\delta E_{\text{Si}}$ are the energies released on the catalyst surface resulting from the interactions of the adsorbed species (here $\text{SiH}_3$ and Si) with incoming hydrogen atoms from the plasma sheath [45]. In equation (9), the first, second, third, fourth and fifth terms account for the energy loss from (the cooling of) the Au droplet surface due to thermal dissociation of $\text{SiH}_3$, desorption of $\text{SiH}_3$ and H species, evaporation of Si atoms, interactions of $\text{SiH}_3$ molecules and Si atoms with hydrogen atoms from the sheath, respectively. The sixth and seventh terms in equation (9) account for the heat dissipation during ion-induced dissociation and collisions of all neutral gas species with the droplet surface, respectively, where $j_{\mathrm{t}}=\sum_{\alpha} j_{\alpha}$ is the total neutral flux from the sheath and $\beta_{\mathrm{T}} \approx 0.26$ is the thermal accommodation coefficient [45]. Finally, using the bisection method one can easily find the droplet temperature as a function of the substrate holder temperature from equation (7).

### 2.5. The nanowire nucleation model

For the nucleation model we assume that the Si atoms (BUs) that are produced as a result of the elementary surface processes are dissolved and consequently there is only an AuSi eutectic (Au-Si alloy) [55]. The dissolved Si atoms then either reevaporate (i.e. via desorption) or attach to the crystal lattice at the liquid-solid interface. This model accounts for:

(i) the absorption of Si atoms into the Au droplet due to diffusion of Si atoms through the droplet bulk;
(ii) diffusion to the droplet from the droplet surface at its border;
(iii) desorption from the droplet;
(iv) formation of two-dimensional (2D) islands at the liquid-solid interface.

In this work, it is also assumed that the number of catalyst atoms (here Au atoms) in the alloy remains constant and the Au and Si atoms occupy the same volume in the liquid phase, $V_{\text{l}}$.

The two-dimensional nucleation of a Si island (and eventually a complete Si monolayer) from a supersaturated Au-Si droplet proceeds through the attachment of Si atoms to the island. Thus, the driving force for island formation is the supersaturation of the liquid alloy in the NP, expressed as $S=C/C_{\text{eq}}-1$. Here, $C$ is the volume concentration of Si atoms in the Au-Si alloy and $C_{\text{eq}}=\vartheta_{\text{eq}}/V_{\text{l}}$ is the equilibrium concentration, where $\vartheta_{\text{eq}}$ is the equilibrium concentration of the Au-Si alloy. In the Si island formation, two-dimensional crystallized nuclei arise, grow, and then coalesce to form a continuous layer (monolayer, ML) with height $h$ [27]. In our study, we consider only the fast microscopic stage of the nucleation of a monolayer at the interface between a Si NW and a droplet with contact angle $\beta=90^{\circ}$, when the droplet radius does not change (the ML nucleation approximation) [27, 34]. For other nucleation cases [27] not considered in this work, one should take into account the contribution of the vapor-solid interface which strongly modifies the effective surface energy of the Si island [27, 56].

Generally, the supersaturation in the droplet, which changes due to the four above mentioned processes (absorption, surface diffusion via the border of the droplet surface, desorption, and the nucleation of 2D islands at the liquid-solid interface), is governed by the following kinetic equation [51]:

$$
\frac{A_{\mathrm{d}}}{V_{\mathrm{l}}} \frac{\mathrm{d} r_{\mathrm{d}}}{\mathrm{d} t}=J_{\mathrm{v}}+J_{\mathrm{s}}-J_{\mathrm{d}}-\frac{A_{\mathrm{d}}^{2}}{4} \frac{h R_{n}}{V_{\mathrm{s}}}. \tag{10}
$$

In equation (10), the first and second expressions on the right-hand side describe the diffusion of Si atoms into the droplet through the bulk and the surface, respectively, while the third and fourth expressions describe the Si loss in the droplet due to Si desorption from the droplet (with flux $J_{\mathrm{d}}=A_{\mathrm{d}} a \vartheta_{\text{eq}}(S+1)/(\tau_{\text{l}} V_{\text{l}})$ during desorption time period $\tau_{\text{l}} \approx 1$ s, where $a$ is the interatomic distance in liquid Au (=0.245 nm)) and incorporation of Si atoms into the island structure (with rate $R_{n}$ for the mononuclear mode [51, 57] as a function of the supersaturation $S$). Here, $h=0.33$ nm [51] is the height

of a monolayer, $V_{\mathrm{s}}=\sigma h$ is the volume per atom in the island (crystal phase), where $\sigma=5.5 \times 10^{-15} \mathrm{~cm}^{2}$ [51] is the area per atom on the island surface. As long as we study the nucleation in the ML nucleation approximation with $\beta=90^{\circ}$ we have $\mathrm{d} r_{\mathrm{d}} / \mathrm{d} r=0$, therefore the difference in chemical potentials of the $\mathrm{Si}$ atoms in the liquid and the solid phases $\Delta \mu_{\mathrm{ls}}$ is obtained taking the GT effect into consideration so that

$$
\Delta \mu_{\mathrm{ls}}^{\mathrm{GT}}=\Delta \mu_{\mathrm{ls}}^{0}-2 \Delta V_{\mathrm{sl}} \epsilon_{\mathrm{lv}} / r_{\mathrm{d}},
$$

where $\Delta \mu_{\mathrm{ls}}^{0}=k_{\mathrm{B}} T_{\mathrm{d}} \ln (S+1)$ and $\epsilon_{\mathrm{lv}}=0.85 \mathrm{~J} \mathrm{~m}^{-2}$ (as the liquid-vapor surface energy) together with the NP radius, $r_{\mathrm{d}}$, and $\Delta V_{\mathrm{sl}}\left(=V_{\mathrm{s}}-V_{\mathrm{l}}\right)$ determine the modification in $\Delta \mu_{\mathrm{ls}}$ due to the GT effect. For the free enthalpy of Si island formation at the fast nucleation stage we have [27]

$$
\Delta H_{n}=-\left(c_{\mathrm{v}} r^{2} h / V_{\mathrm{s}}\right) \Delta \mu_{\mathrm{ls}}^{\mathrm{GT}}+\epsilon_{\mathrm{ls}} c_{\mathrm{s}} h r, \quad(11)
$$

where $c_{\mathrm{v}}$ and $c_{\mathrm{s}}$ are the dimensionless geometric factors for volume and surface area, respectively. In equation (11), $r$ is the island radius and $\epsilon_{\mathrm{ls}}=0.3 \mathrm{~J} \mathrm{~m}^{-2}$ [58] is the interfacial surface energy per unit area at the liquid-solid interface. By maximizing the above equation in $r$ (the island radius), one obtains

$$
\Delta H_{\mathrm{N}}^{*}=c_{\mathrm{s}}^{2} \epsilon_{\mathrm{ls}}^{2} V_{\mathrm{s}} / 4 c_{\mathrm{v}} \Delta \mu_{\mathrm{ls}}^{\mathrm{GT}} \quad(12)
$$

for the energy barrier for Si island formation. Equation (12) indicates that the energy barrier for Si island nucleation is inversely proportional to the chemical potential difference, $\Delta \mu_{\mathrm{ls}}^{\mathrm{GT}}$. Therefore, unrelated to the temperature condition, if the supersaturation (thus $\Delta \mu_{\mathrm{ls}}^{\mathrm{GT}}$ ) in the liquid increases, the nucleation energy barrier will decrease.

From equation (12), the critical diameter $d_{\mathrm{c}}$, below which the growth ceases due to the Gibbs-Thomson effect, may be given by [35]

$$
d_{\mathrm{c}}=4 \Delta V_{\mathrm{sl}} \epsilon_{\mathrm{lv}} / \Delta \mu_{\mathrm{ls}},
$$

where $J_{\mathrm{s}}, J_{\mathrm{v}}$ and $J_{\mathrm{d}}$ are described in sections 2.3 and 2.4. Finally, the total NW growth rate at the initial stage, $R_{\mathrm{t}}$, which accounts for diffusion- and desorption-induced contributions, is given by $R_{\mathrm{t}}=V_{\mathrm{l}}\left(J_{\mathrm{s}}+J_{\mathrm{v}}-J_{\mathrm{d}}\right) / A_{\mathrm{d}}$.

### 2.6. Calculation procedure and input parameters

The solutions of these equations will be used to determine the dependence of the energy barrier, early-stage growth rate and critical diameter on the plasma parameters. We consider thin Si NW nucleation and growth in a high-density plasma with $\mathrm{SiH}_{4}$ as a source gas mixed with $\mathrm{Ar}$ and $\mathrm{H}_{2}$ (commonly used in Si nanostructure synthesis experiments [48]). The most important input parameters used are summarized in table 1.

By numerically solving the sheath equations (1)-(3), the values of the ion energies and fluxes at the substrate (where $\phi=\phi_{\mathrm{s}}$, here $\phi_{\mathrm{s}}$ is the surface potential determined by the plasma biasing conditions) are found, then are used as parameters in the mass and heat balance equations. In this model, the ion energies and fluxes are highly dependent on the characteristics of the plasma sheath (i.e., the sheath thickness), which in turn is influenced by the plasma bulk parameters (e.g., ion density, electron temperature, etc) and the nanostructured substrate characteristics. The substrate holder temperature, NP radius and the plasma process parameters were varied in our numerical calculations to observe how the sheath and nanostructured substrate characteristics affect the Si NW nucleation characteristics, such as the nucleation energy barrier, NW growth rate and the critical diameter for nucleation.

<table>
<caption>Table 1. Parameters used in the computation.</caption>
<thead>
<tr>
<th>Parameters</th>
<th>Notation</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Electron temperature</td>
<td>$T_{\mathrm{e}}$</td>
<td>1–3 eV</td>
</tr>
<tr>
<td>Ion temperature</td>
<td>$T_{\mathrm{i}}$</td>
<td>0.05–0.15 eV</td>
</tr>
<tr>
<td>Substrate holder temperature</td>
<td>$T_{\mathrm{h}}$</td>
<td>$400$–$800\,^\circ$C</td>
</tr>
<tr>
<td>Electron density at the sheath edge</td>
<td>$n_{\mathrm{e}0}$</td>
<td>$10^{10}$–$5 \times 10^{12}\,\mathrm{cm}^{-3}$</td>
</tr>
<tr>
<td>Neutral gas pressure</td>
<td>$p_{0}$</td>
<td>20–100 mTorr</td>
</tr>
<tr>
<td>Catalyst nanoparticle radius</td>
<td>$r_{\mathrm{d}}$</td>
<td>2–20 nm</td>
</tr>
<tr>
<td>Substrate potential</td>
<td>$\phi_{\mathrm{s}}$</td>
<td>$-100$ to $-300$ V</td>
</tr>
<tr>
<td>Percentage of silane gas</td>
<td>$r_{\mathrm{SiH}}$</td>
<td>1–40%</td>
</tr>
<tr>
<td>Percentage of hydrogen gas</td>
<td>$r_{\mathrm{H}}$</td>
<td>1–30%</td>
</tr>
<tr>
<td>Percentage of carrier gas (Ar)</td>
<td>$r_{\mathrm{Ar}}$</td>
<td>50–89%</td>
</tr>
</tbody>
</table>

## 3. Results—nanowire nucleation characteristics

In this section, the numerical solutions of the model equations from section 2 are presented. The dependences of the NW nucleation characteristics (the nucleation energy barrier $(\Delta H_{\mathrm{N}}^{*})$, early-stage growth rate $(R_{\mathrm{t}})$, and critical diameter $(d_{\mathrm{c}}))$ on the nanoparticle and surface conditions (i.e., $T_{\mathrm{h}}$, $r_{\mathrm{d}}$ and $\phi_{\mathrm{s}}$ in section 3.1), plasma parameters (i.e., $n_{\mathrm{e}}$ and $T_{\mathrm{e}}$ in section 3.2) and gas composition (i.e. $r_{\mathrm{SiH}}$ and $r_{\mathrm{H}}$ in section 3.3) in a direct current PECVD system are studied. We also explore how PECVD gives rise to much higher catalyst temperatures $T_{\mathrm{d}}$ when the substrate holder temperature $(T_{\mathrm{h}})$ remains fixed.

### 3.1. Nanoparticle and surface conditions

Figure 2 clearly shows the effects of variation in $T_{\mathrm{h}}$ on the NP temperature, the nucleation energy barrier, growth rate and critical diameter. It is clearly seen from figure 2(a) that for the PECVD case, $T_{\mathrm{d}}$ is always higher than $T_{\mathrm{h}}$, whilst we always have $T_{\mathrm{d}}=T_{\mathrm{h}}$ for the CVD case. The energy barrier for Si NW nucleation (figure 2(b)) and critical diameter (figure 2(d)), which decrease with increasing $T_{\mathrm{h}}$, become smaller in the PECVD case (compared with those of CVD), and also take slightly larger values when the GT effect is taken into consideration. One can observe that the NW early-stage growth rate (figure 2(c)), which increases as $T_{\mathrm{h}}$ rises, becomes much higher in PECVD compared with the $R_{\mathrm{t}}$ of CVD and takes smaller values (especially at lower temperatures) when the GT effect is significant. The amount of damage (increase in $\Delta H_{\mathrm{N}}^{*}$) induced by the GT effect in CVD $(\zeta_{\mathrm{GT}}^{\mathrm{C}})$ and PECVD $(\zeta_{\mathrm{GT}}^{\mathrm{P}})$ systems have been visually quantified in figure 2(b). It is clearly seen that at a given temperature $(T_{\mathrm{h}}=568\,^\circ$C), the damage for the PECVD case is much smaller than that of the CVD case (i.e. $\zeta_{\mathrm{GT}}^{\mathrm{P}} \ll \zeta_{\mathrm{GT}}^{\mathrm{C}}$). Moreover, the damage becomes smaller (for both cases) when $T_{\mathrm{h}}$ is increased.

The energy barrier for nucleation $(\Delta H_{\mathrm{N}}^{*})$ and the earlystage growth rate $(R_{\mathrm{t}})$ for both the PECVD and CVD cases

![](./images/811644623368749060_2.jpg)

Figure 2. The NP temperature (a), energy barrier for Si NW nucleation (b), nanowire growth rate (c), and critical diameter (d) as functions of the substrate holder temperature for CVD (solid and dashed curves) and PECVD (dotted and dash-dotted curves) for $T_{\rm e}=1.5$ eV, $T_{\rm i}=0.05$ eV, $n_{\rm e0}=5\times10^{12}\ {\rm cm}^{-3}$, $p_0=50$ mTorr, $r_{\rm d}=5$ nm, $\phi_{\rm s}=-100$ V, $r_{\rm Ar}=70\%$, $r_{\rm SiH}=20\%$, and $r_{\rm H}=10\%$. The dashed and dash-dotted curves in (b)-(d) correspond to the cases in which the GT effect is taken into account. The amount of damage caused by the GT effect (i.e., increase in $\Delta H_{\rm N}^*$) are indicated in (b) by $\zeta_{\rm GT}^{\rm C}$ and $\zeta_{\rm GT}^{\rm P}$ for the CVD and PECVD cases, respectively.

have been plotted as functions of NP radius $r_{\rm d}$ in figures 3(a) and (b), respectively. One can see from figure 3(a) that the energy barrier for the CVD systems is always higher than that of the PECVD systems and experiences a dramatic increase as the NP radius decreases. Despite a large change in $\Delta H_{\rm N}^*$ for the small NP radius range, $\Delta H_{\rm N}^*$ for the CVD systems does not change significantly as the NP radius is increased further (e.g. for $r_{\rm d}>10$ nm, see the solid and dashed curves in figure 3(a)). An opposing trend is observed for the PECVD case which shows the overall impact of ion-induced processes in the enhanced saturation of the NP by BUs, even for small NPs. Two different trends are exhibited by the NW growth rate for CVD and PECVD cases (see the dashed and long-dashed curves in figure 3(b)). For the neutral gas-based process, $R_{\rm t}$ increases with increasing $r_{\rm d}$ (from small to the moderate NP radius) and then increases only slightly with further increase in $r_{\rm d}$ (i.e. when $r_{\rm d}>10$ nm). For PECVD, on the other hand, the early-stage growth rate decreases with increasing NP radius. The damage induced by the GT effect (for CVD, compare the much lower $R_{\rm t}$ displayed by the dashed line with the $R_{\rm t}$ plotted by the solid line in the small to moderate $r_{\rm d}$ range in figure 3(b)) clearly indicates why thin NWs are not likely to nucleate in CVD systems (or why the thin-NW nucleation yield is so low).

As the NW nucleation and early-stage growth rates are mainly determined by the diffusive Si fluxes to the NP (through the surface and bulk), which in turn depend strongly on the ion-induced dissociation of $\rm SiH_3$ radicals on the NP surface, the surface potential (with which one can tune the ion energies at the substrate) $\phi_{\rm s}$ plays an important role in determining the characteristics of NW nucleation and growth. In figure 4, $T_{\rm d}$, $\Delta H_{\rm N}^*$, $R_{\rm t}$ and $d_{\rm c}$ have been plotted as functions of $\phi_{\rm s}$ for $T_{\rm h}=400,500$, and $600\,^\circ{\rm C}$. The same trends for $\Delta H_{\rm N}^*$, $R_{\rm t}$ and $d_{\rm c}$ observed when electron temperature and density were increased are also noted when the magnitude of the substrate potential ($|\phi_{\rm s}|$) is increased, i.e., $\Delta H_{\rm N}^*$ and $d_{\rm c}$ decrease with increasing $|\phi_{\rm s}|$, whilst $R_{\rm t}$ significantly increases with $|\phi_{\rm s}|$ at low temperatures.

### 3.2. Plasma parameters

Let us turn our attention to the effects of variation in the electron density at the sheath edge, $n_{\rm e0}$. Figure 5 displays the NP temperature and nucleation characteristics as functions of $n_{\rm e0}$ for three different substrate holder temperatures ($T_{\rm h}=400,500$ and $600\,^\circ{\rm C}$). It is seen from the $T_{\rm d}$ and $R_{\rm t}$ curves (figures 5(a) and (c)) that as $n_{\rm e0}$ is increased, the NP temperature becomes much higher than $T_{\rm h}$ (which is kept constant at the substrate-substrate holder interface) and the early-stage growth rate also increases as a result of more effective heating and ion-assisted Si creation. Also, the energy barrier, critical diameter and also the damage (induced by the GT effect) decrease with increasing electron density (see figures 5(b) and (d)).

In the plasma-assisted NW growth, an increase in the electron temperature is accompanied by an increase in the NW early-stage growth rate (see figure 6(c)) due to more effective ion-assisted Si creation on the droplet surface. The

![](./images/811644623368749060_3.jpg)

Figure 3. The energy barrier for Si NW nucleation (a) and the nanowire growth rate (b) as functions of the NP radius for CVD (solid and dashed curves) and PECVD (dotted and long-dashed curves) for $T_{\rm e}=0.05$ eV, $T_{\rm i}=0.05$ eV, $n_{\rm e0}=5\times10^{12}\ {\rm cm}^{-3}$, $p_0=50$ mTorr, $\phi_{\rm s}=-100$ V, $r_{\rm Ar}=70\%$, $r_{\rm SiH}=20\%$, and $r_{\rm H}=10\%$. The dashed and long-dashed curves in (a) and (b) correspond to the cases in which the GT effect is taken into account. The amount of damage caused by the GT effect (i.e., increase in $\Delta H_{\rm N}^{*}$) are indicated in (a) by $\zeta_{\rm GT}^{\rm C}$ and $\zeta_{\rm GT}^{\rm P}$ for the CVD and PECVD cases, respectively.

nucleation energy barrier and critical diameter decrease in response to the electron temperature increase. Also, the amount of damage induced by the GT effect becomes smaller as $T_{\rm e}$ rises, i.e., $\zeta_{\rm GT}^{\rm L}\ll\zeta_{\rm GT}^{\rm H}$, where $\zeta_{\rm GT}^{\rm L}$ and $\zeta_{\rm GT}^{\rm H}$ represent the amount of damage at low and high values of the plasma-specific parameters, respectively. It is worth noting that the nucleation characteristics mainly notably change at lower substrate holder temperatures (here, $T_{\rm h}=400$ and $500\,^{\circ}{\rm C}$) with increasing $n_{\rm e0}$, $T_{\rm e}$ and $|\phi_{\rm s}|$.

### 3.3. Gas composition

To investigate the dependences of the nucleation characteristics on the percentage of the precursor gas ($\rm SiH_4$) in the $\rm Ar+H_2+SiH_4$ gas mixture, $r_{\rm SiH}$, figure 7 plots the nucleation energy barrier, the growth rate and the critical diameter as functions of $r_{\rm SiH}$ for three different substrate holder temperatures (400, 500, and $600\,^{\circ}{\rm C}$). The increase in $r_{\rm SiH}$ gives rise to an increase in the growth rate and decrease in both the nucleation energy barrier and critical diameter, as can be seen in figures 7(a)-(c).

Finally, we study the effects of variation in the percentage of the etching gas ($\rm H_2$) in the $\rm Ar+H_2+SiH_4$ gas mixture, $r_{\rm H}$, on the NW nucleation characteristics. Figure 8 shows the dependences of the NP temperature, the nucleation energy barrier, the early-stage growth rate and the critical diameter on $r_{\rm H}$ for varied $T_{\rm h}$. One can see from figure 8(a) that the NP temperature becomes higher with increased etching gas supply. Furthermore, the nonlinear behavior of the nucleation characteristics with increased etching (hydrogen) gas pressure ratio shown in figures 8 (b)-(d) points toward a strong dependence of the NW nucleation (and growth) on the hydrogen production in reactive plasmas. It is seen in figures 8(b) and (d) that the nucleation energy barrier and critical diameter (and also the damage due to the GT effect) increase with the hydrogen pressure ratio from a small to a moderate value, $r_{\rm H}^{\rm max}\approx4\%$, and then decrease as $r_{\rm H}$ is increased further.

Also, an opposing nonlinear trend is observed for the NW growth rate in figure 8(c) when $r_{\rm H}$ is increased from small to large values. It is worth noting that $r_{\rm H}^{\rm max}$, which is the hydrogen pressure ratio at which $\Delta H_{\rm N}^{*}$ and $d_{\rm c}$ take their maximum values, increases with increasing substrate holder temperature. This indicates a strong interplay between the etching of BUs and heating-induced BU creation on the top-most NP surface.

The calculated trends presented in sections 3.1-3.3 will be discussed and interpreted in section 4.

## 4. Discussion

Let us now discuss the interrelation between the sheath characteristics, BU generation, BU loss through diffusion processes and NW nucleation (and thus growth) in greater detail. The ion energies strongly depend on the sheath thickness. The sheath thickness may be tuned by changing, for example, the electron temperature $T_{\rm e}$ and substrate potential $\phi_{\rm s}$. As $T_{\rm e}$ and $|\phi_{\rm s}|$ are increased and $n_{\rm e0}$ is decreased, the plasma sheath becomes wider. If the sheath is wider, the ions gain more energy. This leads to more effective ion-induced reactions (due to strong energetic ion flux deposition) on the NP surface, more energy is released and thus more BUs are created and diffuse into the droplet (as a result of the associated increase in NP temperature). Due to the enhanced diffusion of BUs, the BU catalyst material alloy (here, a Si-Au alloy) within the catalyst NP becomes sufficiently supersaturated and the NWs nucleate over much shorter times. The efficient energy transfer to the NP surface eventually minimizes the GT effect, which enables the nucleation of thin NWs [34] even at low substrate holder temperatures. Also, after a Si monolayer is nucleated (the onset of NW growth), more effective BU diffusion (due to more effective plasma-assisted heating and BU creation) leads to much higher NW growth rates, thus we can expect to obtain long NWs over much shorter times.

In our computations, the ion energies ($E_{\alpha}$, $\alpha={\rm Ar}^{+}$, ${\rm SiH}_3^{+}$, and ${\rm H}^{+}$) and fluxes were obtained by numerically solving the sheath-model equations. They change remarkably with variations in the bulk plasma parameters and the substrate potential. The ion energies and fluxes were then used as parameters to calculate the number of Si atoms produced

![](./images/811644623368749060_4.jpg)

Figure 4. The effects of variation in the substrate potential on the NP temperature (a), the energy barrier for Si NW nucleation (b), the Si NW growth rate (c), and the critical diameter (d) for $T_{\rm h}=400$ (solid and dashed curves), 500 (long-dashed curves), and $600\,^\circ{\rm C}$ (dotted and dash-dotted curves). The other parameters are as follows: $T_{\rm c}=1.5$ eV, $T_{\rm i}=0.05$ eV, $p_0=50$ mTorr, $r_{\rm d}=5$ nm, $n_{e0}=5\times10^{12}\,{\rm cm}^{-3}$, $r_{\rm Ar}=70\%$, $r_{\rm SiH}=20\%$, and $r_{\rm H}=10\%$. The dashed and dash-dotted curves in (b)-(d) correspond to the cases in which the GT effect is taken into account. The amount of damage caused by the GT effect (i.e., increase in $\Delta H_{\rm N}^*$, decrease in $R_{\rm t}$) are indicated on the graphs by $\zeta_{\rm GT}^{\rm L}$ and $\zeta_{\rm GT}^{\rm H}$, indicative of low and high values of the plasma-specific parameters.

![](./images/811644623368749060_5.jpg)

Figure 5. The effects of variation in the electron density at the sheath edge on the NP temperature (a), the energy barrier for Si NW nucleation (b), the NW growth rate (c), and the critical diameter (d) for $T_{\rm h}=400$ (solid and dashed curves), 500 (long-dashed curves), and $600\,^\circ{\rm C}$ (dotted and dash-dotted curves). The other parameters are as follows: $T_{\rm c}=1.5$ eV, $T_{\rm i}=0.05$ eV, $r_{\rm d}=5$ nm, $\phi_{\rm s}=-100$ V, $r_{\rm Ar}=70\%$, $r_{\rm SiH}=20\%$, and $r_{\rm H}=10\%$. The dashed and dash-dotted curves in (b)-(d) correspond to the cases in which the GT effect is taken into account. The amount of damage caused by the GT effect (i.e., increase in $\Delta H_{\rm N}^*$, decrease in $R_{\rm t}$) are indicated on the graphs by $\zeta_{\rm GT}^{\rm L}$ and $\zeta_{\rm GT}^{\rm H}$, indicative of low and high values of the plasma-specific parameters.

![](./images/811644623368749060_6.jpg)

Figure 6. The NP temperature (a), the energy barrier for Si NW nucleation (b), the Si NW growth rate (c), and the critical diameter (d) as functions of electron temperature for $T_{\rm h}=400$ (solid and dashed curves), 500 (long-dashed curves), and $600\,^\circ{\rm C}$ (dotted and dash-dotted curves). The other parameters are as follows: $T_{\rm i}=0.05$ eV, $p_0=50$ mTorr, $r_{\rm d}=5$ nm, $n_{\rm e0}=5\times10^{12}$ cm$^{-3}$, $\phi_{\rm s}=-100$ V, $r_{\rm Ar}=70\%$, $r_{\rm SiH}=20\%$, and $r_{\rm H}=10\%$. The dashed and dash-dotted curves in (b)-(d) correspond to the cases in which the GT effect is taken into account. The amount of damage caused by the GT effect (i.e., increase in $\Delta H_{\rm N}^*$, decrease in $R_{\rm t}$) are indicated on the graphs by $\zeta_{\rm GT}^{\rm L}$ and $\zeta_{\rm GT}^{\rm H}$, indicative of low and high values of the plasma-specific parameters.

and the subsequent Si diffusion fluxes into the NP. The calculated Si fluxes into and from the NP, together with the Si incorporation rate into the Si nucleus, were used in the nucleation model, which accounted for the size-dependent GT effect, in order to compute the nucleation characteristics such as the nucleation energy barrier, the critical diameter, and the NW growth rate.

To interpret the growth characteristics behaviors, described in section 3, we need to first note that in PECVD of NWs, the etching gas ($\rm H_2$), influxes of $\rm SiH_3$ neutrals and $\rm SiH_3^+$ ions all affect the NP surface. These species, upon reaching the NP surface will undergo BU-generating or -losing surface processes which can be categorized based on their efficiency at the specific NP temperatures. In the higher-temperature range ($T_{\rm h}>600\,^\circ{\rm C}$) thermal processes, such as thermal dissociation of $\rm SiH_3$ radicals, surface diffusion, etc, are the most important BU generation and loss processes in PECVD (or CVD), whilst in the lower-temperature range ($T_{\rm h}<600\,^\circ{\rm C}$), BU creation on the catalyst-NP surface proceeds via ion-induced dissociation of $\rm SiH_3$ (which is proportional to $J_{\rm SiH}E_{\rm SiH}$), $\rm SiH_3^+$ ion decomposition (which is proportional to $J_{\rm SiH}$), and the loss of all adsorbed species through interaction with atomic hydrogen from the plasma sheath.

As noted in figure 2, the temperature strongly affects the nucleation and NW growth. Due to recombination of hydrogen atoms, hydrogen ion neutralization and ion-NP surface collisions unique to hydrogen-producing plasma-assisted synthesis, the NP temperature $T_{\rm d}$ is always higher than the substrate holder temperature $T_{\rm h}$ ($T_{\rm d}>T_{\rm h}$). This is why for low-temperature plasma-assisted NW synthesis, due to the efficient minimizing of the GT effect ($\zeta_{\rm GT}^{\rm C}\ll\zeta_{\rm GT}^{\rm C}$), it is possible to nucleate thin NWs, something which is only possible at high temperatures for CVD experiments, i.e. $T_{\rm C}>T_{\rm P}$ (see figure 2(d)). At high temperatures ($T_{\rm h}>600\,^\circ{\rm C}$), due to more effective thermal dissociation of $\rm SiH_3$ radicals, Si atom generation and then diffusion into the NPs is enhanced so that the energy barrier for nucleation decreases. This means that the nucleation of much thinner NWs is likely to occur; additionally, the NW early-stage growth rate becomes higher (after nucleation of the first Si monolayer). Also, it is worth noting that the growth rate increase with increasing temperature is consistent with the available experimental results [18, 19].

As shown in figure 3, the NW nucleation and then growth strongly depend on the NP radius and behave differently for CVD (see solid and dashed curves in figure 3) and PECVD (see dotted and long-dashed curves in figure 3) systems. The relatively poor size selectivity (due to the same energy barriers for nucleation from different sized NPs) for the thermal CVD case above $r_{\rm d}>6$ nm is attributed to GT equalization, which also results in the same NW growth rates in the $r_{\rm d}$ range of our interest (see dashed curve in figure 3(b)), which is in good agreement with the NW diameter independent growth rates reported in low-pressure CVD of NWs [59, 60].

On the other hand, in a PECVD process, every NP size (NW radius) has its own energy barrier, which results in

![](./images/811644623368749060_7.jpg)

Figure 7. The effects of variation in the percentage of silane gas on the energy barrier for Si NW nucleation (a), the NW growth rate (b), and the critical diameter (c). The parameters are as follows: $T_{\rm e}=1.5$ eV, $T_{\rm i}=0.05$ eV, $p_0=50$ mTorr, $r_p=5$ nm, $n_{\rm e0}=5\times10^{12}$ cm$^{-3}$, and $r_{\rm H}=10\%$.

excellent size selectivity of the NWs via PECVD, even under low-temperature and -pressure conditions. In CVD systems, as figure 3 shows, it is expected that for much smaller NW radii (due to the strong GT effect) the Si NWs are unlikely to develop and/or will grow more slowly ($R_{\rm t}$ rapidly decreases with decreasing radius). This, in turn, confirms the available experimental results [61–63].

All the numerical and experimental results show the key role played by the GT effect as the NW get thinner. This effect is almost completely suppressed in PECVD of thin NWs (i.e., the detrimental effect becomes smaller ($\zeta_{\rm GT}^{\rm P}\ll\zeta_{\rm GT}^{\rm C}$) even at low temperatures), due to plasma-assisted heating and BU generation, so that a substantially lower energy barrier (compared with the CVD case) needs to be overcome for NW nucleation. This plasma-induced behavior is in striking contrast with that of the CVD case (see the dashed and dash-dotted curves in figure 3).

As the precursor gas pressure ratio increases, more $\text{SiH}_3$ radicals are delivered to and reside on the NP surface, then due to the more effective thermal dissociation of precursor species ($\text{SiH}_4$), more Si atoms are created. These atoms then diffuse (through the catalyst bulk and surface) into the NP and eventually reach the most suitable nucleation site. Due to the stronger Si atom fluxes, the nucleation energy barrier and the critical diameter for nucleation significantly decrease, whilst the early-stage growth rate becomes higher (see figure 7). Furthermore, the dependence of the critical diameter on the precursor gas pressure ratio (shown in figure 7(c)) is consistent with the available experimental results [16, 36, 50, 61].

When the electron (or ion) density at the sheath edge $n_{\rm e0}$ increases, the sheath thickness decreases so that the fluxes of the ions (especially $\text{SiH}_3^+$) impinging on the catalyst surface become stronger. This in turn leads to more effective heating and ion-induced decomposition processes on the NP surface. As shown in figure 5, the variation of the electron density (or equivalently the ion density) affects the nucleation characteristics mainly at low temperatures ($T_{\rm h}=400$ and $500^\circ\text{C}$) when the plasma-related processes (ion-induced dissociation, ion decomposition, and the interactions of particles on the NP surface with incoming ions and hydrogen fluxes from the sheath) mainly govern the loss and generation of BUs on the surface. Due to more effective IID (i.e., ion-induced dissociation of $\text{SiH}_3$) and ID processes (i.e., $\text{SiH}_3^+$ ion decomposition) resulting from the $n_{\rm e0}$ increase, the BU creation and then diffusion are enhanced. The difference between the catalyst temperature and the substrate holder temperature becomes more pronounced via effective ion bombardment (see the curves in figure 5), hence the GT effect is diminished even at smaller NP radius, i. e., $\zeta_{\rm GT}^{\rm L}\ll\zeta_{\rm GT}^{\rm H}$.

In sections 3.1 and 3.2 we also considered the effects of variations in the electron temperature $T_{\rm e}$ and substrate potential $\phi_{\rm s}$ on NW growth characteristics. The influence of the electron temperature and of the surface potential at low temperatures, when the thermal dissociation of $\text{SiH}_3$ radicals is less effective, may be explained as follows. With increasing $T_{\rm e}$ and $|\phi_{\rm s}|$, the ion fluxes and the kinetic energies become larger, respectively, so that the IID and ID processes are enhanced. This enhancement leads to the creation of more BUs which then diffuse into the catalyst. With more effective supersaturation of the BUs in the catalyst NP, the nucleation barrier, even for small NP radii, significantly decreases and the critical diameter for NW nucleation is set to smaller values. Furthermore, with increasing $T_{\rm e}$ and $|\phi_{\rm s}|$ more BUs reach the NP–Si NW interface and incorporate into the monolayer. Consequently, the NW early-stage growth rate increases (see the $R_{\rm t}$-curves in figures 6(c) and 4(c)). One can see that with increasing plasma heating effects, when $T_{\rm d}$ increases at a fixed $T_{\rm h}$, the damage due to the GT effect, $\zeta_{\rm GT}$, becomes increasingly lower so that it is diminished at higher plasma- (surface-) specific parameters.

Hydrogen atom recombination and ion neutralization are two of the main energy release processes, which lead

![](./images/811644623368749060_8.jpg)

Figure 8. The NP temperature (a), the energy barrier for Si NW nucleation (b), the Si NW growth rate (c), and the critical diameter (d) as functions of the percentage of the etching (hydrogen) gas for $T_{\rm h} = 420$, 450, and $480\,^\circ{\rm C}$ when $r_{\rm SiH}$ is held constant at $20\%$. The other parameters are as follows: $T_{\rm e} = 1.5$ eV, $T_{\rm i} = 0.05$ eV, $p_0 = 50$ mTorr, $r_{\rm d} = 5$ nm, $n_{\rm e0} = 5 \times 10^{12}\,{\rm cm}^{-3}$, and $\phi_{\rm s} = -100$ V. The amount of damage caused by the GT effect (i.e., increase in $\Delta H_{\rm N}^\star$ and decrease in $R_{\rm t}$) are indicated on the graphs by $\zeta_{\rm GT}^{\rm L}$, $\zeta_{\rm GT}^{\rm M}$ and $\zeta_{\rm GT}^{\rm H}$, indicative of low, moderate and high values of the plasma-specific parameters.

to increases in the catalyst temperature. Thus additional etching gas supply will increase the temperature at the catalyst surface due to more effective hydrogen atom/ion-induced reactions [43]. On the other hand, as a result of larger incoming fluxes of atomic hydrogen from the plasma, a huge number of BUs will be removed from the surface. The effect of the temperature increase is more effective dissociation of $\rm SiH_3$ radicals, whilst much higher BU loss is also expected due to hydrogen atom recombination on the catalyst surface. A competition between the above mentioned two effects plays a major role in determining the nucleation characteristics of NWs.

The nonlinear behavior in $\Delta H_{\rm N}^\star$, $R_{\rm t}$, $d_{\rm c}$, and $\zeta_{\rm GT}$ with increasing $r_{\rm H}$, shown in figure 8, can be attributed to more effective interaction of Si atoms with hydrogen atoms at low and moderate ($r_{\rm H}^{\rm max}$) values of $r_{\rm H}$ so that the Si atom desorption (from the catalyst surface) is likely to be enhanced. Consequently, more energy is needed to nucleate the first monolayer. With further increase of $r_{\rm H}$, the catalyst particle is strongly heated through hydrogen atom recombination and hydrogen ion neutralization; this effect is likely to prevail over the Si atom loss mentioned above. As a result, $\Delta\mu_{\rm Is}$ increases, which in turn lowers the energy barrier and the critical diameter for nucleation while the early-stage growth rate increases. Also, the decrease of the energy barrier with increased etching gas pressure ratio (for $r_{\rm H}^{\rm max} < r_{\rm H}$) is consistent with the trend observed experimentally in Si NW growth (assisted by a high-melting-point catalyst) after the etching gas ($\rm H_2$) is added to the $\rm Ar + SiH_4$ gas mixture [64].

## 5. Conclusion

An advanced combination of the plasma sheath, heating, BU creation and NW nucleation models for NW growth has been employed to investigate the effects of variation in the plasma process parameters on the energy barrier for NW nucleation, NP critical diameter and nanowire growth rate at early growth stages. By numerically solving the sheath and mass balance equations as well as computing the supersaturation of BUs in the NP (to determine the ion energy, energy released on the surface, and number of Si atoms produced on the NP surface and then calculating the Si atom diffusion fluxes into the NP), we have linked the NW nucleation characteristics to the bulk plasma parameters. Moreover, the thin-NW model has accounted for the Gibbs–Thomson effect which increases the NP inner pressure and eventually forces BUs to diffuse out of the catalyst. The main findings are summarized as follows.

- The NW nucleation characteristics strongly depend on the catalyst temperature, which is a function of the substrate holder temperature. When the catalyst temperature is increased, more BUs are produced (due to the effective plasma-assisted dissociation of precursor molecules) on the catalyst surface, thus the enhanced supersaturation of the BUs in the catalyst bulk results in less energy required for the first Si monolayer nucleation and a much smaller critical diameter. Furthermore, due to stronger BU fluxes into the catalyst NP and then into the incorporation site the early-stage growth rate becomes higher.

- The relatively poor size selectivity in NWs (for the large NP radius range) via a CVD process is attributed to the size-independent nucleation energy barrier. This is in strict contrast with the significant difference between nucleation energy barriers for different NW radii in the PECVD case. Moreover, in the PECVD process, with the enhanced plasma heating and induced BU creation, thin-NW nucleation is likely to occur, even at low temperatures when the GT effect denies the possibility of the growth of very thin NWs in neutral gas-based systems.
- Due to the plasma heating effect, the NP temperature is always higher than the temperature at the substrate holder for the PECVD case. This temperature difference becomes pronounced when the hydrogen production in the plasma is increased. Moreover, with increasing ion fluxes and energies (due to higher magnitudes of the electron temperature, electron number density and surface potential) the ion-induced BU creation becomes more effective, which in turn leads to a much higher supersaturation of BUs in the NP. As a result, the GT effect is diminished even at low temperatures, when thin-NW nucleation is not possible through neutral gas-based methods. Therefore, by changing the plasma parameters one can efficiently control the NW nucleation characteristics, especially at low temperatures.

Our numerical results have shown that increasing the plasma-related effects, such as the hydrogen/ion-induced heating and ion-induced Si atom creation, strongly minimizes the GT effect even at low surface temperatures, when thermal dissociation of precursor molecules is less effective. This suggests an exciting opportunity to synthesize thin nanowire arrays with the required thickness, density, and size dispersion under truly energy- and matter-efficient conditions possible through low-temperature plasmas. Hence these results are relevant to energy conversion devices such as photovoltaic solar cells [65]. Future work will focus on extending these findings for the catalyzed growth of other nanostructures and material systems.

## Acknowledgments
This work was partially supported by the CSIRO OCE Science Leadership Program, CSIRO Sensors and Sensor Network Transformational Capability Program, the Australian Research Council, and Sahand University of Technology. AER thanks the OCE Postdoctoral Fellowship scheme for financial support. Fruitful discussions with Professor I Denysenko are greatly appreciated.

## References
[1] Cui Y and Lieber C M 2001 *Science* **291** 851
[2] Ostrikov K 2005 *Rev. Mod. Phys.* **77** 489
[3] Park W, Zheng G, Jiang X, Tian B and Lieber C M 2002 *Nano Lett.* **8** 3004
[4] Zhu Y W, Yu T, Cheong F C, Xu X J, Lim C T, Tan V B C, Thong J T L and Sow C H 2005 *Nanotechnology* **16** 88
[5] Qin Y, Wang X D and Wang Z L 2008 *Nature* **451** 809
[6] Cvelbar U, Chen Z Q, Sunkara M K and Mozetic M 2008 *Small* **4** 1610
[7] Chen P-C, Ishikawa F N, Chang H-K, Ryu K and Zhou C 2009 *Nanotechnology* **20** 125503
[8] Martinez R V, Martinez J and Garcia R 2010 *Nanotechnology* **21** 245301
[9] Tang J *et al* 2010 *Nanotechnology* **21** 505704
[10] Wu L, Song F, Fang X, Guo Z-X and Liang S 2010 *Nanotechnology* **21** 475502
[11] Na J, Huh J, Park S C, Kim D, Kim D W, Lee J W, Hwang I-S, Lee J-H, Ha J S and Kim G T 2010 *Nanotechnology* **21** 485201
[12] Meyyappan M and Sunkara M K 2010 *Inorganic Nanowires: Applications, Properties, and Characterization* (New York: CRC Press)
[13] Garnett E and Yang P 2010 *Nano Lett.* **10** 1082
[14] Cao L, White J S, Park J-S, Schuller J A, Clemens B M and Brongersma M L 2009 *Nat. Mater.* **8** 643
[15] Ozaki N, Ohno Y and Takeda S 1998 *Appl. Phys. Lett.* **73** 3700
[16] Westwater J, Gosain D P, Tomiya S, Usui S and Ruda H 1997 *J. Vac. Sci. Technol. B* **15** 554
[17] Wu Y, Cui Y, Huynh L, Barrelet C J, Bell D C and Lieber C M 2004 *Nano Lett.* **4** 433
[18] Kikkawa J, Ohno Y and Takeda S 2005 *Appl. Phys. Lett.* **86** 123109
[19] Persson A I, Froberg L E, Jeppesen S, Bjork M T and Samuelson L 2007 *J. Appl. Phys.* **101** 034313
[20] Schubert L, Werner P, Zakharov N D, Gerth G, Kolb M, Long L, Gosele U and Tan T Y 2004 *Appl. Phys. Lett.* **84** 4968
[21] Bauer B, Rudolph A, Soda M, Morral A F, Zweck J, Schuh D and Reiger E 2010 *Nanotechnology* **21** 435601
[22] Dick K, Deppert K, Martensson T, Mandl B, Samuelson L and Seifert W 2005 *Nano Lett.* **5** 761
[23] Johansson J, Patrik C, Svensson T, Martensson T, Samuelson L and Seifert W 2005 *J. Phys. Chem. B* **109** 13567
[24] Yu D P *et al* 1998 *Appl. Phys. Lett.* **72** 3458
[25] Hu J, Bando Y, Zhan J, Liu Z, Golberg D and Ringer S P 2005 *Adv. Mater.* **17** 975
[26] Colli A, Hofmann S, Fasoli A, Ferrari A C, Ducati C, Dunin-Borkowski R E and Robertson J 2006 *Appl. Phys. A* **85** 247–253
[27] Dubrovskii V G, Sibirev N V, Harmand J C and Glas F 2008 *Phys. Rev. B* **78** 235301
[28] Chiang W H and Sankaran R M 2009 *Diamond Relat. Mater.* **18** 946
[29] Chiang W H and Sankaran R M 2009 *Nat. Mater.* **8** 882
[30] Gamalski A D, Tersoff J, Sharma R, Ducati C and Hofmann S 2010 *Nano Lett.* **10** 2972
[31] Keidar M 2007 *J. Phys. D: Appl. Phys.* **40** 2388
[32] Tsakadze Z L, Ostrikov K, Sow C H, Mhaisalkar S G and Boey Y C 2010 *J. Nanosci. Nanotechnol.* **10** 6575
[33] Ostrikov K and Mehdipour H 2011 *J. Mater. Chem.* **21** 8183
[34] Ostrikov K and Mehdipour H 2011 *Appl. Phys. Lett.* **98** 033104
[35] Dhalluin F, Desré P J, den Hertog M I, Rouviére J-L, Ferret P, Gentile P and Baronb T 2007 *J. Appl. Phys.* **102** 094906
[36] Froberg L E, Seifert W and Johansson J 2007 *Phys. Rev. B* **76** 153401
[37] Tan T Y, Li N and Gosele U 2003 *Appl. Phys. Lett.* **83** 1199
[38] Hou W-C, Chen L-Y and Hong F-C-N 2008 *Diamond Relat. Mater.* **17** 1780
[39] Ostrikov K, Cvelbar U and Murphy A B 2011 *J. Phys. D: Appl. Phys.* **44** 174001
[40] Denysenko I, Ostrikov K, Yu M Y and Azarenkov N A 2007 *J. Appl. Phys.* **102** 074308
[41] Denysenko I, Ostrikov K, Cvelbar U, Mozetic M and Azarenkov N A 2008 *J. Appl. Phys.* **104** 073301
[42] Denysenko I and Ostrikov K 2009 *J. Phys. D: Appl. Phys.* **42** 015208
[43] Wolter M, Levchenko I, Kersten H and Ostrikov K 2010 *Appl. Phys. Lett.* **96** 133105

[44] Mehdipour H, Ostrikov K and Rider A E 2010 *Nanotechnology* **21** 455605

[45] Mehdipour H, Ostrikov K, Rider A E and Han Z J 2011 *Plasma Proc. Polym.* **8** 386

[46] Ostrikov K, Yoon H J, Rider A E and Vladimirov S V 2007 *Plasma Proc. Polym.* **4** 27

[47] Zhou W, Zhong X X, Wu X, Yuan L, Shu Q, Li W and Xia Y 2007 *J. Phys. D: Appl. Phys.* **40** 219

[48] Iacopi F, Vereecken P M, Schaekers M, Caymax M, Moelans N, Blanpain B, Richard O, Detavernier C and Griffiths H 2007 *Nanotechnology* **18** 505307

[49] Bootsma G A and Gassen H J 1971 *J. Cryst. Growth* **10** 223–34

[50] Hofmann S, Ducati C, Neill R J, Piscanec S, Ferrari A C, Geng J, Dunin-Borkowski R E and Robertson J 2003 *J. Appl. Phys.* **94** 6005

[51] Dubrovskii V G, Sibirev N V, Cirlin G E, Harmand J C and Ustinov V M 2006 *Phys. Rev. E* **73** 021603

[52] Liberman M A and Lichtenberg A J 1994 *Principles of Plasma Discharges and Material Processing* (New York: Wiley)

[53] Glassbrenner C J and Slack G A 1964 *Phys. Rev.* **134** A1058

[54] Ostrikov K, Levchenko I and Xu S 2008 *Pure Appl. Chem.* **80** 1909

[55] Kim B J, Tersoff J, Wen C-Y, Reuter M C, Stach E A and Ross F M 2009 *Phys. Rev. Lett.* **103** 155701

[56] Glas F, Harmand J C and Patriarche G 2007 *Phys. Rev. Lett.* **99** 146101

[57] Kashchiev D 2000 *Nucleation: Basic Theory with Applications* (Oxford: Butterworth Heinemann)

[58] Kim B J, Tersoff J, Kodambaka S, Reuter M C, Stach E A and Ross F M 2008 *Science* **322** 1070

[59] Kodambaka S, Tersoff J, Reuter M C and Ross F M 2006 *Phys. Rev. Lett.* **96** 096105

[60] Ross F M 2010 *Rep. Prog. Phys.* **73** 114501

[61] Dhalluin F, Baron T, Ferret P, Salem B, Gentile P and Harmand J-C 2010 *Appl. Phys. Lett.* **96** 133109

[62] Dayeh S A and Picraux S T 2010 *Nano Lett.* **10** 4032

[63] Schmid H, Bjork M T, Knoch J, Karg S, Riel H and Riess W 2009 *Nano Lett.* **9** 173

[64] Iacopi F, Richard O, Eichhammer Y, Bender H, Vereecken P M, de Gendt S and Heyns M 2008 *Solid State Lett.* **11** K98

[65] Akimov Yu A, Koh W S and Ostrikov K 2009 *Opt. Express* **17** 10195