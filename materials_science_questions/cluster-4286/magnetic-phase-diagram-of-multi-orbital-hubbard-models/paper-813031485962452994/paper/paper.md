# Reentrant Fulde-Ferrell-Larkin-Ovchinnikov superfluidity in the honeycomb lattice

Agnieszka Cichy$^{1,2,*}$ and Andrzej Ptok$^{3,\dagger}$

$^{1}$Solid State Theory Division, Faculty of Physics, Adam Mickiewicz University, Umultowska 85, 61-614 Poznań, Poland
$^{2}$Institut für Physik, Johannes Gutenberg-Universität Mainz, Staudingerweg 9, 55099 Mainz, Germany
$^{3}$Institute of Nuclear Physics, Polish Academy of Sciences, Ulica E. Radzikowskiego 152, 31342 Kraków, Poland

![](./images/813031485962452994_1.jpg)
(Received 20 October 2017; published 29 May 2018)

We study superconducting properties of population-imbalanced ultracold Fermi mixtures in the honeycomb lattice that can be effectively described by the spin-imbalanced attractive Hubbard model in the presence of a Zeeman magnetic field. We use the mean-field theory approach to obtain ground-state phase diagrams including the unconventional Fulde-Ferrell-Larkin-Ovchinnikov (FFLO) phase, which is characterized by atypical behavior of the Cooper-pair total momentum. We show that the momentum changes its value as well as direction with a change of the system parameters. We discuss the influence of Van Hove singularities on the possibility of the reentrant FFLO phase occurrence, without a BCS precursor.

DOI: 10.1103/PhysRevA.97.053619

## I. INTRODUCTION

The discovery of graphene [1] triggered enormous theoretical and experimental activity [2,3]. Henceforth, it has attracted much attention due to theoretical interest in fundamental physics, as well as its potential practical applications [4–8]. The attempt to understand graphene physics is not without difficulties, related, e.g., to electron-phonon interactions and the presence of a charge inhomogeneity [9]. However, recent advances in experiments offer the possibility to simulate similar condensed matter phenomena by loading ultracold bosonic or fermionic atoms into optical lattices [10–18]. The engineering of the honeycomb lattice in ultracold gas setups as well as the creation of artificial graphenelike band structures offer the possibility of exploration of regimes which are still inaccessible in solid state materials. Recently, condensed matter systems based on fermions with linear dispersion (e.g., the honeycomb lattice) have generated a surge of intensive studies [19–26]. These models have substantial differences from models with an extended Fermi surface, such as those on the square lattice. However, it is not yet understood which unconventional phases can be stable in such systems, especially in those where effective attraction is dominant.

In this work, we analyze the stability of one of the most interesting phases occurring in this type of system, the Fulde-Ferrell-Larkin-Ovchinnikov (FFLO) state (formation of Cooper pairs across the spin-split Fermi surface with nonzero total momentum) [27,28]. We consider the attractive Hubbard model in the presence of a Zeeman magnetic field. It is worth mentioning that at half filling, in the absence of a Zeeman magnetic field, a quantum phase transition from the BCS state to the normal phase takes place. It results in the occurrence of a critical attraction below which the BCS state is unstable. Our main finding is not only establishing that the FFLO phase is stable for a wide range of parameters, but also that reentrant FFLO superconductivity can occur. Moreover, at half filling and in the spin imbalanced system (equivalent to a nonzero Zeeman magnetic field), the presence of Van Hove singularities (VHSs) in the density of states (DOS) results in a stable FFLO phase for arbitrarily weak attractive interactions. This discovery is essential from the viewpoint of realizing the FFLO state in ultracold gas experiments [29] in artificial hexagonal lattices. The field of such experiments has matured over the past decade [12–16,30–34]. In particular, investigations of quantum Fermi gases with spin or mass imbalance have become very popular [35–42]. The possibility to control population imbalance by preparing mixtures with arbitrary population ratios motivates attempts to understand the influence of a Zeeman magnetic field on superfluidity.

The FFLO phase can be stable at low temperature and relatively large magnetic field (above the critical magnetic field of the Clogston-Chandrasekhar or Pauli limit [43,44]). There are experimental and theoretical premises that the FFLO state can be found in quasi-two-dimensional organic [45–48], heavy-fermion [49–54] or iron-based [54–60] superconductors. In these types of materials, a first-order phase transition from the superconducting to the normal state has been reported [46–49,51–53,55–57]. However, the observation of this type of superconductivity is very difficult because of the strong destructive influence of the orbital (paramagnetic) effect in solid state systems [53,61].

Bringing together the two important threads of research, one related to graphene and the honeycomb lattice and the second to population imbalance in ultracold atomic gases, can lead to different and interesting physics. In particular, it gives the possibility to investigate some exotic superconducting phases which could potentially be found experimentally. So far, such phases have eluded experimental realization and one of the reasons for it is the nonzero critical value of attraction for the existence of the standard superconducting phase in the honeycomb lattice at half filling and without magnetic field [10,62]. We show that reentrant FFLO superconductivity can

*agnieszkakuja2311@gmail.com
†aptok@mmj.pl


![](./images/813031485962452994_2.jpg)

FIG. 1. (a) Honeycomb lattice discussed in this paper. The unit cell defined by vectors $\boldsymbol{a}_1$ and $\boldsymbol{a}_2$ containing two atoms (blue and green points) belonging to sublattices $A$ and $B$. The three nearest-neighbor vectors are given by $\boldsymbol{\delta}_1=(\sqrt{3}/2,-1/2)$, $\boldsymbol{\delta}_2=(0,1)$, and $\boldsymbol{\delta}_3=(-\sqrt{3}/2,-1/2)$. The elementary primitive unit cell (yellow rhombus) is given by lattice vectors $\boldsymbol{a}_1=\boldsymbol{\delta}_2-\boldsymbol{\delta}_3=a(1/2,\sqrt{3}/2)$ and $\boldsymbol{a}_2=\boldsymbol{\delta}_2-\boldsymbol{\delta}_1=a(-1/2,\sqrt{3}/2)$, where $a=\sqrt{3}$. (b) Dispersion relation for $\mu/t=0$ and $h/t=0$. Reciprocal lattice vectors are given by $\boldsymbol{b}_1=2\pi/a(1,1/\sqrt{3})$ and $\boldsymbol{b}_2=2\pi/a(-1,1/\sqrt{3})$, while the first Brillouin zone is shown by a black dotted hexagon. High symmetry points are given by $M=\boldsymbol{b}_1/2=2\pi/a(1/2,1/2\sqrt{3})$ and $K=-K'=(\boldsymbol{b}_1-\boldsymbol{b}_2)/3=2\pi/a(2/3,0)$.

be realized even below this critical value (even for arbitrarily small attractions) for some range of magnetic fields. This greatly facilities the experimental realization and detection of the FFLO phase in ultracold fermionic gases in the lattice and makes searches for such a phase realistic. As such, it is the main finding of our work.

The paper is organized as follows. Section II gives a discussion of the spin-polarized Hubbard model as well as the method. Section III presents numerical results concerning, among others, the phase diagram, the density of states analysis, and the dependence of the Cooper-pair properties. We summarize in Sec. IV.

## II. MODEL AND TECHNIQUE

The system can be described by the Hamiltonian in real space as $H=H_K+H_I$, where
$$
H_K=\sum_{i,j,s,s'\sigma}\left[-t_{ij}^{ss'}-(\mu+\sigma h)\delta_{ij}\delta_{ss'}\right]c_{is\sigma}^{\dagger}c_{js'\sigma}\tag{1}
$$
and
$$
H_I=U\sum_{is}n_{is\uparrow}n_{is\downarrow}.\tag{2}
$$

Here $c_{is\sigma}$ ($c_{is\sigma}^{\dagger}$) describes the annihilation (creation) of an electron with spin $\sigma\in\{\uparrow,\downarrow\}$ in the $i$th site of sublattice $s\in\{A,B\}$ [Fig. 1(a)]. The first term describes a noninteracting state. We assume equal hopping between the nearest-neighbor (NN) sites (i.e., $t_{ij}^{ss'}=t=1$ as energy unit and 0 otherwise). In addition, $\mu$ is the chemical potential, whereas $h$ is the external magnetic field. The second term describes the on-site Coulomb interaction $U/t<0$ being the source of $s$-wave-type superconductivity.

### A. Noninteracting state

In the absence of interaction ($U=0$), the kinetic term (1) can be transformed to the reciprocal space as
$$
\begin{aligned}
H_K=&\sum_{\boldsymbol{k},s,\sigma}(-\mu-\sigma h)c_{\boldsymbol{k}s\sigma}^{\dagger}c_{\boldsymbol{k}s\sigma}\\
&+\sum_{\boldsymbol{k},\sigma}-t\left[g(\boldsymbol{k})c_{\boldsymbol{k}A\sigma}^{\dagger}c_{\boldsymbol{k}B\sigma}+\text{H.c.}\right],\tag{3}
\end{aligned}
$$
where $g(\boldsymbol{k})=\sum_{i=1}^{3}\exp(i\boldsymbol{k}\cdot\boldsymbol{\delta}_i)$. Here $\boldsymbol{\delta}_i$ defines the location of the NN sites [Fig. 1(a)]. Hence, one obtains
$$
g(\boldsymbol{k})=\sqrt{3+2\cos(\sqrt{3}k_x)+4\cos\left(\frac{\sqrt{3}}{2}k_x\right)\cos\left(\frac{3}{2}k_y\right)}.\tag{4}
$$

Using the Nambu notation, $H_K$ can be rewritten as
$$
H_K=\sum_{\boldsymbol{k}\sigma}\Phi_{\boldsymbol{k}\sigma}^{\dagger}\mathbb{H}(\boldsymbol{k},\sigma)\Phi_{\boldsymbol{k}\sigma},\tag{5}
$$
where $\Phi_{\boldsymbol{k}\sigma}^{\dagger}=(c_{\boldsymbol{k}A\sigma}^{\dagger},c_{\boldsymbol{k}B\sigma}^{\dagger})$ is the Nambu spinor and
$$
\mathbb{H}(\boldsymbol{k},\sigma)=\begin{pmatrix}
-(\mu+\sigma h)&-tg(\boldsymbol{k})\\
-tg(\boldsymbol{k})&-(\mu+\sigma h)
\end{pmatrix}.\tag{6}
$$

The eigenvalues $\mathcal{E}_{\alpha\boldsymbol{k}\sigma}$ of the Hamiltonian $H_K$ can be found by diagonalization of the matrix (6). As a result, one obtains $\mathcal{E}_{\pm,\boldsymbol{k}\sigma}=\pm t|g(\boldsymbol{k})|-(\mu+\sigma h)$ [Fig. 1(b)].

### B. Superconducting state

The source of the $s$-wave superconductivity in the Hubbard model is the on-site attraction ($U/t<0$) between particles with opposite spins on the same site. The interaction term $H_I$ can be decoupled in the mean-field approximation by
$$
n_{is\uparrow}n_{is\downarrow}=\Delta_{i,s}^{*}c_{is\downarrow}c_{is\uparrow}+\Delta_{i,s}c_{is\uparrow}^{\dagger}c_{is\downarrow}^{\dagger}-|\Delta_{i,s}|^2,\tag{7}
$$
where $\Delta_{i,s}=\langle c_{is\downarrow}c_{is\uparrow}\rangle$ is the superconducting order parameter (SOP) in the sublattice $s$. Then
$$
H_I^{\text{MF}}=U\sum_{is}\left(\Delta_{i,s}c_{is\uparrow}^{\dagger}c_{is\downarrow}^{\dagger}+\text{H.c.}\right),\tag{8}
$$
where the last term from Eq. (7) has been omitted, because it does not affect the self-consistent equations. However, it is important to emphasize that this term has to be taken into account in a grand canonical potential calculation to determine the stability of different phases, since this constant term decreases the energy of the system [63].

Because there are two shifted sublattices ($A$ and $B$) in the system, the SOP term for the FFLO phase can be rewritten as
$$
\begin{aligned}
\Delta_{j,s}=&\Delta_0\{\delta_{s,A}\exp(i\boldsymbol{Q}\cdot\boldsymbol{R}_j)\\
&+\delta_{s,B}\exp[i\boldsymbol{Q}\cdot(\boldsymbol{R}_j+\boldsymbol{w})]\},\tag{9}
\end{aligned}
$$
where $\Delta_0$ is the SOP amplitude in the entire system and $\boldsymbol{Q}$ is the total momentum of the Cooper pair. Here $\boldsymbol{R}_i$ denotes the location of the $i$th site in real space, while $\boldsymbol{w}$ describes the shift between both atoms in the unit cell and equals $\boldsymbol{\delta}_2$ [cf. Fig. 1(a)]. In the superconducting phase ($\Delta_0>0$), one can

distinguish the BCS state with $|\boldsymbol{Q}|=0$ and the FFLO phase for $|\boldsymbol{Q}|>0$. Hence, in momentum space
$$
\begin{aligned}
H_{I}^{\mathrm{MF}}= & U \sum_{\boldsymbol{k}} \Delta_{0}\left[c_{\boldsymbol{k} A \uparrow}^{\dagger} c_{-\boldsymbol{k}+\boldsymbol{Q} A \downarrow}^{\dagger}\right. \\
& \left.+\exp (i \boldsymbol{Q} \cdot \boldsymbol{w}) c_{\boldsymbol{k} B \uparrow}^{\dagger} c_{-\boldsymbol{k}+\boldsymbol{Q} B \downarrow}^{\dagger}\right]+\text { H.c. } \quad(10)
\end{aligned}
$$

As a consequence, the mean-field Hamiltonian $H^{\mathrm{MF}}=H_{K}+$ $H_{I}^{\mathrm{MF}}$ can be rewritten in a block matrix form
$$
H^{\mathrm{MF}}=\sum_{\boldsymbol{k}} \Psi_{\boldsymbol{k}}^{\dagger} \mathbb{H}_{\mathrm{MF}}(\boldsymbol{k}) \Psi_{\boldsymbol{k}}, \quad(11)
$$
where $\Psi_{\boldsymbol{k}}^{\dagger} \equiv\left(\Phi_{\boldsymbol{k} \uparrow}^{\dagger}, \Phi_{-\boldsymbol{k}+\boldsymbol{Q} \downarrow}^{T}\right)$, while the partial block matrix $\mathbb{H}_{\boldsymbol{k}}^{\mathrm{MF}}$ is given as
$$
\mathbb{H}_{\boldsymbol{k}}^{\mathrm{MF}}=\left(\begin{array}{cc}
\mathbb{H}(\boldsymbol{k}, \uparrow) & \mathbb{U}(\boldsymbol{Q}) \\
\mathbb{U}^{*}(\boldsymbol{Q}) & -\mathbb{H}^{*}(-\boldsymbol{k}+\boldsymbol{Q}, \downarrow)
\end{array}\right). \quad(12)
$$

The diagonal elements of $\mathbb{H}_{\boldsymbol{k}}^{\mathrm{MF}}$, i.e., ones involving the matrix $\mathbb{H}(\boldsymbol{k}, \sigma)$, describe the single-particle spectrum and are given by Eq. (6), while the off-diagonal elements describe superconductivity and $\mathbb{U}(\boldsymbol{Q})$ is defined as $\mathbb{U}(\boldsymbol{Q})=U \Delta_{0} \delta_{s s^{\prime}}(\delta_{s, A}+$ $e^{i \boldsymbol{Q} \cdot \boldsymbol{w}} \delta_{s, B})$, where the index of matrix elements describes sublattices.

## NUMERICAL RESULTS AND DISCUSSION

In this section we show and discuss the numerical results. First, we describe the details of numerical predictions (Sec. III A). Then we present the phase diagrams for the half-filling and non-half-filling (i.e., doped) cases (Sec. III B) and we discuss them in the context of the density-of-states analysis (Sec. III C). Finally, we provide the numerical calculations and discuss the main properties of the FFLO phase in the hexagonal lattice (Sec. III D).

### Numerical details

To find the ground state, we calculate the grand canonical potential, defined by $\Omega \equiv-k_{B} T \ln \{\operatorname{Tr}[\exp (-H^{\mathrm{MF}} / k_{B} T)]\}$, which at $T=0$ is equivalent to the mean-field energy. The calculations were performed in momentum space, on an $N=$ $121 \times 121 \boldsymbol{k}$ grid inside the first Brillouin zone (FBZ). Since we study the stability of the FFLO phase, $\Omega$ is a function of the SOP amplitude $\Delta_{0}$ and the total momentum $\boldsymbol{Q}$ of Cooper pairs [64]. In this case, the procedure of minimization of $\Omega$ with respect to the SOP amplitude $\Delta_{0}$ and all possible momenta $\boldsymbol{Q}$ realized in the system is essential. To find the global minimum of $\Omega(\Delta_{0}, \boldsymbol{Q})$, the numerical calculations were accelerated using graphics processing unit (GPU), according to the procedure described in Ref. [63].

It is important to emphasize that the mean-field approximation (MFA) overestimates, in general, the critical temperatures and the range of stability of the phases with a long-range order. However, the MFA gives at least a qualitative description of the system in the ground state $(T=0)$, even in the strong-coupling limit [65].

The ansatz which we have proposed to describe the SOP in real space, i.e., Eq. (9), does not limit the solutions with respect to the Cooper-pair momentum $\boldsymbol{Q}$. It is a very important extension in comparison to the previous theoretical works in which the assumed ansatz strongly limits the possibility of the occurrence of a stable phase. For instance, it is worth mentioning the Kekulé order [66], for which the SOP in real space is $2 \pi / 3$ phase modulated [67,68]. Moreover, using the ansatz proposed in our paper, one can provide the analysis of phases other than FFLO, e.g., the spatially homogeneous spin-polarized superfluidity (called the breached pair state or Sarma phase [69]). However, our numerical calculations show that this type of phase is unstable for the whole region of parameters, which is in agreement with other theoretical works [70-72]. Moreover, using this ansatz, e.g., pairing in the presence of the Fermi surface deformation [73-76] (called Pomeranchuk instability [77]) or multiparticle instability [78] can be analyzed. However, these types of unconventional phases go beyond the scope of this work.

Additionally, the existence of a discontinuous phase transition between the BCS and the FFLO phase or the normal state, which is characteristic of the systems in the Pauli limit, leads to the occurrence of the phase separation regions. In contrast to the case of a fixed chemical potential, if the number of particles is fixed, one obtains two critical Zeeman fields in the phase diagrams which determine the phase separation (PS) region between different types of phases [38,39,64,79-81], e.g., the BCS and the FFLO phase or the normal state.

### Phase diagram

In the normal state, based on the dispersion relation $\mathcal{E}_{\alpha k \sigma}$, one can distinguish the conduction $(\alpha=+)$ and valence $(\alpha=-)$ bands in the band structure of the system. At half filling (for $\mu / t=0$, for which the average number of particles per lattice site $n=\frac{1}{N} \sum_{i s \sigma}\langle c_{i s \sigma}^{\dagger} c_{i s \sigma}\rangle=\frac{1}{N} \sum_{k s \sigma}\langle c_{k s \sigma}^{\dagger} c_{k s \sigma}\rangle$ is equal to 1) and at $h / t=0$, the conduction (valence) band is fully empty (occupied) and the system exhibits a semimetal behavior (Fig. 2). These two bands touch each other at the corner points of the FBZ in the Dirac cones, which is manifested by the vanishing DOS at the Fermi level.

At half filling $(\mu / t=0$ and $n=1)$ and in the absence of the magnetic field, the honeycomb lattice exhibits a continuous quantum phase transition between the semimetal phase and the BCS state [10,82,83] (Fig. 3). The superconducting state

![](./images/813031485962452994_3.jpg)

FIG. 2. Energy band structure of the honeycomb lattice. The FBZ is shown by the black hexagon. Simultaneously, the hexagon shows the Fermi level in the case of half filling $(\mu / t=0)$ and absence of the magnetic field $(h / t=0)$. The Dirac cones are located in the corner $K$ and $K'$ points of the FBZ.

![](./images/813031485962452994_4.jpg)

FIG. 3. Amplitude of the superconducting order parameter in the absence of the Zeeman magnetic field as a function of the chemical potential $\mu$ and pairing interaction $U$.

can emerge in the system for a pairing interaction stronger than some critical interaction $U_c$. We estimate $|U_c|/t \simeq 2.245$ [Fig. 4(a)], which is in good agreement with previous mean-field studies [10]. However, for any $\mu \neq 0$, the SOP exhibits an exponential-like decrease to zero with decreasing $|U|$ [Fig. 4(a)]. This behavior is clearly visible around VHSs ($\mu/t = \pm 1$ at Fig. 3).

The increase of the attraction above $U_c$ leads to the stabilization of the BCS state [Fig. 4(a)]. With an increasing Zeeman magnetic field (increasing population imbalance), the FFLO phase becomes stable at some $|U|$-dependent critical value $h_c$, through a first-order phase transition. The discontinuous phase transition is manifested by a jump of the order parameter with increasing $|U|$ and at fixed $h$, which is illustrated in Fig. 4(b) and indicated by stars. As we mentioned above, this behavior of the order parameter is reflected in the occurrence of the phase separation region in the phase diagrams for fixed $n$. Indeed, such behavior is observed in the system under consideration as well, which will be discussed in detail in the next paragraph.

The essential finding of our work is that the FFLO phase can also be stable below $U_c$ for some range of magnetic fields. As we already emphasized, this feature makes the experimental realization of this phase much simpler because any superconducting state which appears in the range $0 > U > U_c$ can only be the FFLO phase. Preparing the experimental setup in such a way that the average number of particles per lattice site is equal to one while introducing a mismatch between the atoms with up and down spins and tuning the interaction to be between $U = 0$ and $U_c$ facilitates observing and identifying the FFLO phase (see also some remarks in the last paragraph of this section).

![](./images/813031485962452994_5.jpg)

FIG. 4. Amplitude of the superconducting order parameter $\Delta_0$ as a function of the chemical potential $\mu$ and attractive interaction $U$. The results (a) in the absence ($h = 0.0t$) and (b) in the presence ($h = 1.0t$) of the magnetic field $h$. Stars in (b) show the phase transition from FFLO to BCS with increasing $|U|$.

![](./images/813031485962452994_6.jpg)

FIG. 5. Ground-state phase diagram; the magnetic field $h$ vs the attractive interaction $U$ at (a) $\mu/t = 0$ and (b) $\mu/t = \pm 1$. The colormap shows the SOP amplitude $\Delta_0$ (blue and red for BCS and FFLO phases, respectively), whereas white indicates the normal (NO) phase. At $\mu/t = 0$ ($n = 1$), the reentrant FFLO superconductivity is stable around $h/t = 1$, below $U_c$.

If the chemical potential and hence the density is changed, the character of the phase diagram changes (cf. Figs. 3 and 5 for $h/t = 0$). As mentioned above, in the absence of a Zeeman magnetic field and at half filling, the system exhibits a quantum phase transition. As a consequence of this fact, superconductivity becomes unstable above some critical value of attraction

![](./images/813031485962452994_7.jpg)

FIG. 6. Ground-state phase diagram: magnetic field $h$ vs chemical potential $\mu$ for different values of the interaction $U$: (a) $U=-2.0t$, (b) $U=-2.5t$, (c) $U=-3.0t$, and (d) $U=-3.5t$. The colormap shows the SOP amplitude $\Delta_0$ (blue and red for BCS and FFLO phases, respectively, and white for the NO phase). Green dashed lines indicate parameters for which the VHSs are located at the Fermi level.

$|U_c|$ [shown in Figs. 3, 4(a), and 5(a)]. However, at any small deviation from half filling (i.e. for any nonzero doping), the superconductivity is stable for the whole range of attractive interactions and one can observe an exponential decay of the order parameter with decreasing $|U|$ [e.g., Fig. 3 or 5(b) shows the case of $\mu/t=\pm1$]. Away from half filling and for small values of the attraction $(|U|/t\lesssim4)$, the FFLO phase occurs for larger values of $h$ than in the half-filled system. It is important to emphasize that the phase transition from the BCS to the normal state as well as from the BCS to the FFLO phase is always discontinuous. However, the phase transition from the FFLO phase to the normal state is of second order for the whole range of parameters. Hence, the FFLO phase, in comparison to the BCS state, evinces a reentrant behavior (i.e., appearing and then disappearing when varying $h$ at fixed $U$ and $t$), because the FFLO phase can occur at $h>0$ for some $|U|<|U_c|$, even without the BCS as a precursor at half filling.

In both cases, i.e., at half filling and away from it, the boundaries of the FFLO and BCS phases (critical magnetic fields) show typical behavior at larger values of $U$ [64], i.e., the FFLO state becomes unstable with an increasing attractive interaction because of the vanishing of at least one Fermi surface [40,84]. In this case, the system is in a phase of tightly bound local pairs (hard-core bosons) [65,80,81].

The influence of the presence of VHS in the DOS on the stabilization of the FFLO phase is illustrated in Fig. 6 with $h$-$\mu$ phase diagrams, at four fixed values of $U$. Green dashed lines indicate parameters for which the VHSs are located at the Fermi level. Around these lines, for larger values of magnetic fields, the FFLO state becomes stable. Moreover, the evolution of the reentrant transition with $U$, at $\mu=0$, is clearly visible. It should also be emphasized that results similar to those presented in this paper, for Lieb and kagome lattices, can be reproduced using more advanced methods like, e.g., the dynamical mean-field theory [85].

![](./images/813031485962452994_8.jpg)

FIG. 7. Ground-state phase diagram: magnetic field $h$ vs average number of particles $n$ for (a) $U=-2.0t$, (b) $U=-2.5t$, (c) $U=-3.0t$, and (d) $U=-3.5t$. The colormap shows the SOP amplitude $\Delta_0$ (blue and red for BCS and FFLO phases, respectively, white for the NO phase). The yellow area denotes the phase separation region. Green dashed lines indicate parameters for which the VHSs are located at the Fermi level.

As mentioned above, discontinuous phase transition can lead to the occurrence of a phase separation in the case of a fixed number of particles $n$. It can be found by mapping of phase diagrams at a fixed chemical potential $\mu$ (Fig. 6) onto the phase diagrams with fixed $n$ (Fig. 7). The region of parameters for which the phase separation is observed is shown in Fig. 7 (the yellow area). The existence of the FFLO phase leads to the suppression of the phase separation region. Hence, it is more likely to observe the PS region rather between spatially homogeneous phases such as the BCS and the normal states.

One needs to remember that FFLO phases are known to be much more sensitive to thermal fluctuations than the BCS state and typically have very low critical temperatures. Hence, the experimental detection of these phases could still be rather problematic. Moreover, for a two-dimensional system, at a zero Zeeman magnetic field, the superconducting-normal transition in the attractive Hubbard model is of the Kosterlitz-Thouless (KT) type, mediated by unbinding of vortices, i.e., below the KT temperature, the system has a quasi-long-range (algebraic) order, which is characterized by a power-law decay of the order parameter correlation function and a nonzero superfluid stiffness. As has been shown in Ref. [80], the KT phase (quasisuperconducting Sarma phase for a homogeneous system) is restricted to the weak-coupling region and low values of polarizations (magnetic fields).

### C. Density-of-states analysis

DOS of the honeycomb lattice shows $1/\sqrt{E}$ singularities due to the one-dimensional nature of the electronic spectrum [2,86-88]. Moreover, near the "neutral" point $(E=0)$, the DOS can be approximated by $\rho(\omega)\propto|\omega|$. As we show below, the presence of the VHS in the DOS, located at $\omega/t=\pm1$, at half filling $(\mu/t=0)$ and $h/t=0$ [e.g., Fig. 8(a)], is important from the point of view of unconventional superconductivity. As

![](./images/813031485962452994_9.jpg)

FIG. 8. The DOS of the honeycomb lattice ($U=0$) for different values of the chemical potential $\mu$ and external magnetic field $h$. Red and blue lines denote the DOS for particles with spin $\uparrow$ and $\downarrow$, respectively, whereas the Fermi level is shown as gray line. The scheme for the different parameters is as follows: (a) $\mu/t=0$ and $h/t=0$, (b) $\mu/t=0$ and $h/t=1$, (c) $\mu/t=1$ and $h/t=0$, and (d) $\mu/t=1$ and $h/t=2$.

a consequence of the existence of two equivalent sublattices, there are two VHSs in the DOS. Changing the location of the Fermi level by changing the value of the chemical potential $\mu$ (filling $n$) or external magnetic field $h$ in the system, one can change the relative position between VHSs for particles with spin up ($\uparrow$) and down ($\downarrow$) (red and blue lines in Fig. 8, respectively).

It is important to emphasize that the DOS has influence on the critical temperature. In the BCS theory $T_c \propto \exp[-1/|U|\rho(E_F)]$, where $\rho(E_F)$ is the total DOS at the Fermi level $E_F$ for both spin components. We describe the behavior of the DOS schematically with the example shown in Fig. 8, in relation to some characteristic parameters taken from the phase diagram in Fig. 5. Without a magnetic field ($h=0$), at half filling ($\mu=0$), $E_F$ is located at the neutral points $K$ and $K'$, with $E=0$ [Fig. 8(a)]. Consequently, there exists a critical value of the interaction $U_c$ below which the BCS phase is unstable and the normal state is favored (the semimetal-superconductor transition) [see Fig. 5(a)]. A similar phenomenon is also observed, e.g., in the metal-insulator transition [89]. In the presence of a Zeeman magnetic field, the DOSs are unequal for the particles with opposite spins. For instance, at $h/t=1$, DOSs are shifted in the way illustrated in Fig. 8(b). Both VHSs are located at $E_F$, with energies $\omega/t=\pm 1$, where the $+$ and $-$ correspond to particles with spins $\uparrow$ and $\downarrow$, respectively. Consequently, the DOS has a maximum at $E_F$. The large spin imbalance implicates the stabilization of the FFLO phase. Similar behavior can be observed in the case of an over- or underdoped system (e.g., $\mu/t=\pm 1$) without magnetic field [Fig. 8(c)]. In this case, both VHSs (for both spin components) with energies $\omega/t=\pm 1$ are located at $E_F$, whereas spin imbalance does not exist. Consequently, the BCS phase is stable. Hence, the superfluid phase can be realized for any pairing interaction strength because of the finite value of $\rho(E_F)$. If the magnetic field is increased, the DOS is shifted again. For $h/t=2$, only the VHS for particles with spin up is located at $E_F$ [Fig. 8(d)]. In this case, i.e., for large magnetic fields, the attractive interaction can lead to the stabilization of the FFLO phase. However, it is important to emphasize that there is a critical value of $U$ below which the FFLO state becomes unstable, in contrast to the half-filled case.

![](./images/813031485962452994_10.jpg)

FIG. 9. Fermi surface of the honeycomb lattice for different values of the Fermi level shown by isoenergetic red lines. The first Brillouin zone is shown by a blue hexagon. Vectors show an example of the Cooper-pair formation, while solid red line shows the Fermi level for fillings equal to 3/8 and 5/8.

As mentioned above, the mutual position of the DOSs for particles with opposite spins is crucial for the stabilization of the BCS state as well as the FFLO phase. For instance, to stabilize the FFLO state, the system should be doped to the so-called $M$ point of the FBZ. This situation corresponds to a 3/8 or 5/8 filling in a given spin-type band [90,91]. At these fillings, the VHS originates from three nonequivalent saddle points. Moreover, the Fermi surface exhibits a high degree of nesting (Fig. 9), forming a perfect hexagon at this filling [88]). These two features lead to the stabilization of the FFLO phase, as a consequence of the perfect nesting of the Fermi surfaces corresponding to the opposite spins [92,93]. It can be described using notation from Fig. 9. In the case of the mentioned filling (i.e., 3/8 and 5/8 filling), the Fermi surfaces for the particles with spin up and down are degenerate (shown by the solid red line). Hereby, the Cooper pairs with total momentum $\boldsymbol{Q}$ can be formed by the particles with momenta $\boldsymbol{k}_1$ and $\boldsymbol{k}_2$. Because of the fact that the Fermi surface is given by the hexagon, the Cooper pairs with momentum $\boldsymbol{Q}$ (along the $\Gamma$-$M$ line) can be realized for many different $\boldsymbol{k}_1$ and $\boldsymbol{k}_2$. Then the FFLO state can be energetically more favorable for a larger range of the pairing interaction $U$. The situation described above is clearly visible, e.g., in Fig. 5(a), at $h/t=1$.

### D. Cooper-pair-momentum $\boldsymbol{Q}$ dependence

The dependence of the Cooper-pair properties is also related to the nesting of Fermi surfaces. This is clearly visible in the evolution of the total momentum $\boldsymbol{Q}$ of pairs with increasing magnetic field (Fig. 10). Usually (for instance, in the square [57,63] or triangular [94-96] lattice case), only the length of $\boldsymbol{Q}$ changes, without changing the direction. It is the consequence

![](./images/813031485962452994_11.jpg)

FIG. 10. Spatial decomposition of the SOP in real space for different total momenta of Cooper pairs $\boldsymbol{Q}$ [marked by points $b$-$g$ in (a)]. The color (red and blue) and the size of the circles correspond to the sign (+ and $-$) and the value of the order parameter. White lines are nodal lines in real space.

of the mutual shift of the Fermi surfaces for the particles with spin up and down. Moreover, the direction of $\boldsymbol{Q}$ can be found, within a good approximation, from the Cooper-pair susceptibility calculation [54,58,63]. However, it is worth

![](./images/813031485962452994_12.jpg)

FIG. 11. (a) Mean-field ground-state phase diagram. The magnetic field $h$ vs pairing interaction $U$ at half filling $(\mu/t=0)$. In the case when the FFLO phase is neglected in calculations, the dashed red line indicates the critical magnetic field above which the BCS state is unstable. Above this line, the normal state (NO) exists. The occurrence of the FFLO state in the phase diagram slightly shifts the boundary of the BCS phase, which is indicated by the solid blue line. The labels $A$, $B$, and $C$ show three different directions of the total momentum $\boldsymbol{Q}$ for which the FFLO phase is realized. (b) Schematic picture of vectors $\boldsymbol{Q}$ in the FBZ, for three different variants of the FFLO phase: $A$, $B$, and $C$.

![](./images/813031485962452994_13.jpg)

FIG. 12. Components of the Cooper-pair momentum vector $\boldsymbol{Q}=(Q_x,Q_y)$ as a function of the interaction strength $U$ and the external magnetic field $h$.

emphasizing that only the global minimum of the energy with respect to $\boldsymbol{Q}$ and $\Delta_0$ has to be found to give proper information on the BCS or FFLO phase.

In the case of the honeycomb lattice, with two atoms per unit cell, $\boldsymbol{Q}$ is not subject to the typical evolution described above. Instead, the evolution of $\boldsymbol{Q}$ with increasing magnetic field can be divided into three phases (shown in Fig. 11): phase $A$, the evolution along the reciprocal lattice vectors; phase $B$, the evolution along the boundary of the FBZ, perpendicular to reciprocal lattice vectors; and phase $C$, the evolution along the boundary of the FBZ perpendicular to $\boldsymbol{w}$, which describes the mutual shift of two sublattices. This evolution is a consequence of the nesting between the Fermi surfaces for particles with spin up and down, which are shifted by the Zeeman magnetic field. As a consequence, the magnitude as well as the direction of $\boldsymbol{Q}$ change in a nonmonotonic way with an increasing magnetic field $h$ (Fig. 12). One can indicate the boundaries in the phase diagram between the FFLO phase with different directions of $\boldsymbol{Q}$. The properties described above are shown in Fig. 10 and in the Supplemental Material [97], which schematically

present the spatial decomposition of the SOP for different $\boldsymbol{Q}$ [in the Supplemental Material the small black crosses denote the position of lattice sites in real space, while the size and color of the closed circles correspond to the value and sign of the SOP (blue and red denote minus and plus signs, respectively)].

## IV. SUMMARY
The honeycomb lattice exhibits a characteristic band structure in which two bands touch each other at the Dirac cones vertices. Consequently, at half filling, there exists some critical interaction $U_c$ above which the BCS phase becomes stable. This value indicates the occurrence of a quantum phase transition from the semimetallic to the superconducting phase, in the absence of a Zeeman magnetic filed. In this paper, we demonstrated that the behavior of the system changes significantly when population imbalance is introduced. Such a system can be realized in ultracold gas experiments, by loading atoms in two different hyperfine states onto a honeycomb-shaped lattice. In such a case, the FFLO state with nonzero total momentum of Cooper pairs can be realized. The characteristic features of the honeycomb lattice DOS can lead to the FFLO phase stabilization for any pairing interaction strength. Moreover, at half filling, $n = 1$, the FFLO phase shows a reentrant behavior. For any pairing interaction (also lower than $U_c$), this phase can be realized without the BCS phase as a precursor, which is not observed in the case of other lattices, e.g., square or triangular. We explain this behavior as a consequence of the singular DOS and the strong nesting of Fermi surfaces. These results can be helpful for experimental realization of the FFLO phase on an artificial hexagonal optical lattice, because any superconducting state which appears in the range of $0 > U > U_c$ can only be the FFLO phase. Additionally, we show that the evolution of the total momentum of Cooper pairs is atypical. As a consequence of the nesting between the Fermi surfaces for particles with different spins, the momenta change values and directions.

## ACKNOWLEDGMENTS
We thank Krzysztof Cichy, Peter G. J. van Dongen, and Matteo Rizzi for careful reading of the manuscript, valuable comments, and discussions. We also thank Ravindra W. Chhajlany, Roman Micnas, and Andrii Sotnikov for many fruitful discussions. This work was supported by the National Science Centre (Poland) under Grants No. UMO-2017/24/C/ST3/00357 (A.C.) and No. UMO-2016/20/S/ST3/00274 (A.P.).

[1] K. S. Novoselov, A. K. Geim, S. V. Morozov, D. Jiang, Y. Zhang, S. V. Dubonos, I. V. Grigorieva, and A. A. Firsov, Electric field effect in atomically thin carbon films, *Science* **306**, 666 (2004).
[2] A. H. Castro Neto, F. Guinea, N. M. R. Peres, K. S. Novoselov, and A. K. Geim, The electronic properties of graphene, *Rev. Mod. Phys.* **81**, 109 (2009).
[3] V. N. Kotov, B. Uchoa, V. M. Pereira, F. Guinea, and A. H. Castro Neto, Electron-electron interactions in graphene: Current status and perspectives, *Rev. Mod. Phys.* **84**, 1067 (2012).
[4] D.-W. Park, A. A. Schendel, S. Mikael, S. K. Brodnick, T. J. Richner, J. P. Ness, M. R. Hayat, F. Atry, S. T. Frye, R. Pashaie, S. Thongpang, Z. Ma, and J. C. Williams, Graphene-based carbon-layered electrode array technology for neural imaging and optogenetic applications, *Nat. Commun.* **5**, 5258 (2014).
[5] Q. Zhou, J. Zheng, S. Onishi, M. F. Crommie, and A. K. Zettl, Graphene electrostatic microphone and ultrasonic radio, *Proc. Natl. Acad. Sci. USA* **112**, 8942 (2015).
[6] H. Lee, T. K. Choi, Y. B. Lee, H. R. Cho, R. Ghaffari, L. Wang, H. J. Choi, T. D. Chung, N. Lu, T. Hyeon, S. H. Choi, and D.-H. Kim, A graphene-based electrochemical device with thermoresponsive microneedles for diabetes monitoring and therapy, *Nat. Nanotechnol.* **11**, 566 (2016).
[7] G. Liu, B. Debnath, T. R. Pope, T. T. Salguero, R. K. Lake, and A. A. Balandin, A charge-density-wave oscillator based on an integrated tantalum disulfide-boron nitride-graphene device operating at room temperature, *Nat. Nanotechnol.* **11**, 845 (2016).
[8] C. Cervetti, A. Rettori, Maria G. Pini, A. Cornia, A. Repolles, F. Luis, M. Dressel, S. Rauschenbach, K. Kern, M. Burghard, and L. Bogani, The classical and quantum dynamics of molecular spins on graphene, *Nat. Mater.* **15**, 164 (2016).
[9] L. K. Loon, Ultracold fermions in a honeycomb optical lattice, Ph.D. thesis, National University of Singapore, 2010.
[10] E. Zhao and A. Paramekanti, BCS-BEC Crossover on the Two-Dimensional Honeycomb Lattice, *Phys. Rev. Lett.* **97**, 230404 (2006).
[11] S.-L. Zhu, B. Wang, and L.-M. Duan, Simulation and Detection of Dirac Fermions with Cold Atoms in an Optical Lattice, *Phys. Rev. Lett.* **98**, 260402 (2007).
[12] P. Soltan-Panahi, J. Struck, P. Hauke, A. Bick, W. Plenkers, G. Meineke, C. Becker, P. Windpassinger, M. Lewenstein, and K. Sengstock, Multi-component quantum gases in spin-dependent hexagonal lattices, *Nat. Phys.* **7**, 434 (2011).
[13] L. Tarruell, D. Greif, T. Uehlinger, G. Jotzu, and T. Esslinger, Creating, moving and merging Dirac points with a Fermi gas in a tunable honeycomb lattice, *Nature* (London) **483**, 302 (2012).
[14] K. K. Gomes, W. Mar, W. Ko, F. Guinea, and H. C. Manoharan, Designer Dirac fermions and topological phases in molecular graphene, *Nature* (London) **483**, 306 (2012).
[15] T. Uehlinger, G. Jotzu, M. Messer, D. Greif, W. Hofstetter, U. Bissbort, and T. Esslinger, Artificial Graphene with Tunable Interactions, *Phys. Rev. Lett.* **111**, 185307 (2013).
[16] M. Polini, F. Guinea, M. Lewenstein, H. C. Manoharan, and V. Pellegrini, Artificial honeycomb lattices for electrons, atoms and photons, *Nat. Nanotechnol.* **8**, 625 (2013).
[17] M. Messer, R. Desbuquois, T. Uehlinger, G. Jotzu, S. Huber, D. Greif, and T. Esslinger, Exploring Competing Density Order in the Ionic Hubbard Model with Ultracold Fermions, *Phys. Rev. Lett.* **115**, 115303 (2015).
[18] I. Vasić, A. Petrescu, K. Le Hur, and W. Hofstetter, Chiral bosonic phases on the Haldane honeycomb lattice, *Phys. Rev. B* **91**, 094502 (2015).

[19] A. M. Black-Schaffer and S. Doniach, Resonating valence bonds and mean-field $d$-wave superconductivity in graphite, *Phys. Rev. B* **75**, 134512 (2007).

[20] K. L. Lee, K. Bouadim, G. G. Batrouni, F. Hébert, R. T. Scalettar, C. Miniatura, and B. Grémaud, Attractive Hubbard model on a honeycomb lattice: Quantum Monte Carlo study, *Phys. Rev. B* **80**, 245118 (2009).

[21] L. Chen, C.-C. Liu, B. Feng, X. He, P. Cheng, Z. Ding, S. Meng, Y. Yao, and G. Wu, Evidence for Dirac Fermions in a Honey- comb Lattice Based on Silicon, *Phys. Rev. Lett.* **109**, 056804 (2012).

[22] W. Li, M. Guo, G. Zhang, and Y.-W. Zhang, Gapless ${\rm MoS_2}$ allotrope possessing both massless Dirac and heavy fermions, *Phys. Rev. B* **89**, 205402 (2014).

[23] A. M. Black-Schaffer, W. Wu, and K. LeHur, Chiral $d$-wave superconductivity on the honeycomb lattice close to the Mott state, *Phys. Rev. B* **90**, 054521 (2014).

[24] W. Beugeling, E. Kalesaki, C. Delerue, Y.-M. Niquet, D. Vanmaekelbergh, and C. M. Smith, Topological states in multi- orbital HgTe honeycomb lattices, *Nat. Commun.* **6**, 6316 (2015).

[25] S. Sadeddine, H. Enriquez, A. Bendounan, P. Kumar Das, I. Vobornik, A. Kara, A. J. Mayne, F. Sirotti, G. Dujardin, and H. Oughaddou, Compelling experimental evidence of a Dirac cone in the electronic structure of a 2D Silicon layer, *Sci. Rep.* **7**, 44400 (2017).

[26] T. Grass, R. W. Chhajlany, L. Tarruell, V. Pellegrini, and M. Lewenstein, Proximity effects in cold atom artificial graphene, *2D Mater.* **4**, 015039 (2017).

[27] P. Fulde and R. A. Ferrell, Superconductivity in a strong spin- exchange field, *Phys. Rev.* **135**, A550 (1964).

[28] A. I. Larkin and Y. N. Ovchinnikov, Nonuniform state of superconductors, *Zh. Eksp. Teor. Fiz.* **47**, 1136 (1964) [Sov. Phys. JETP **20**, 762 (1965)].

[29] Y.-a. Liao, A. S. C. Rittner, T. Paprotta, W. Li, G. B. Partridge, R. G. Hulet, S. K. Baur, and E. J. Mueller, Spin-imbalance in a one-dimensional Fermi gas, *Nature (London)* **467**, 567 (2010).

[30] I. Bloch, J. Dalibard, and W. Zwerger, Many-body physics with ultracold gases, *Rev. Mod. Phys.* **80**, 885 (2008).

[31] A. Singha, M. Gibertini, B. Karmakar, S. Yuan, M. Polini, G. Vignale, M. I. Katsnelson, A. Pinczuk, L. N. Pfeiffer, K. W. West, and V. Pellegrini, Two-dimensional Mott-Hubbard electrons in an artificial honeycomb lattice, *Science* **332**, 1176 (2011).

[32] H. Mayaffre, S. Krämer, M. Horvatic, C. Berthier, K. Miyagawa, K. Kanoda, and V. F. Mitrovic, Evidence of Andreev bound states as a hallmark of the FFLO phase in $\kappa$-(BEDT-TTF)$_2$Cu(NCS)$_2$, *Nat. Phys.* **10**, 928 (2014).

[33] M. C. Revelle, J. A. Fry, B. A. Olsen, and R. G. Hulet, 1D to 3D Crossover of a Spin-Imbalanced Fermi Gas, *Phys. Rev. Lett.* **117**, 235301 (2016).

[34] J. J. Kinnunen, J. Baarsma, J.-P. Martikainen, and P. Törma, The Fulde-Ferrell-Larkin-Ovchinnikov state for ultracold fermions in lattice and harmonic potentials: A review, *Rep. Prog. Phys.* **81**, 046401 (2018).

[35] M. W. Zwierlein, A. Schirotzek, C. H. Schunck, and W. Ket- terle, Fermionic superfluidity with imbalanced spin populations, *Science* **311**, 492 (2006).

[36] G. B. Partridge, W. Li, R. I. Kamar, Y.-a. Liao, and R. G. Hulet, Pairing and phase separation in a polarized Fermi gas, *Science* **311**, 503 (2006).

[37] M. W. Zwierlein and W. Ketterle, Comment on pairing and phase separation in a polarized Fermi gas, *Science* **314**, 54 (2006).

[38] D. E. Sheehy and L. Radzihovsky, BEC-BCS Crossover in "Magnetized" Feshbach-Resonantly Paired Superfluids, *Phys. Rev. Lett.* **96**, 060401 (2006).

[39] D. E. Sheehy and L. Radzihovsky, BEC-BCS crossover, phase transitions and phase separation in polarized resonantly-paired superfluids, *Ann. Phys. (NY)* **322**, 1790 (2007).

[40] G. J. Conduit, P. H. Conlon, and B. D. Simons, Superfluidity at the BEC-BCS crossover in two-dimensional Fermi gases with population and mass imbalance, *Phys. Rev. A* **77**, 053617 (2008).

[41] G. J. Conduit, A. G. Green, and B. D. Simons, Inhomogeneous Phase Formation on the Border of Itinerant Ferromagnetism, *Phys. Rev. Lett.* **103**, 207201 (2009).

[42] L. Radzihovsky and D. E. Sheehy, Imbalanced Feshbach- resonant Fermi gases, *Rep. Prog. Phys.* **73**, 076501 (2010).

[43] B. S. Chandrasekhar, A note on the maximum critical field of high-field superconductors, *Appl. Phys. Lett.* **1**, 7 (1962).

[44] A. M. Clogston, Upper Limit for the Critical Field in Hard Superconductors, *Phys. Rev. Lett.* **9**, 266 (1962).

[45] F. Piazza, W. Zwerger, and P. Strack, FFLO strange metal and quantum criticality in two dimensions: Theory and application to organic superconductors, *Phys. Rev. B* **93**, 085112 (2016).

[46] R. Lortz, A. Demuer, P. H. M. Böttger, B. Bergk, G. Zwicknagl, Y. Nakazawa, and J. Wosnitza, Calorimet- ric Evidence for a Fulde-Ferrell-Larkin-Ovchinnikov Super- conducting State in the Layered Organic Superconductor $\kappa$-(BEDT-TTF)$_2$Cu(NCS)$_2$, *Phys. Rev. Lett.* **99**, 187002 (2007).

[47] B. Bergk, A. Demuer, I. Sheikin, Y. Wang, J. Wosnitza, Y. Nakazawa, and R. Lortz, Magnetic torque evidence for the Fulde-Ferrell-Larkin-Ovchinnikov state in the layered organic superconductor $\kappa$-(BEDT-TTF)$_2$Cu(NCS)$_2$, *Phys. Rev. B* **83**, 064506 (2011).

[48] R. Beyer and J. Wosnitza, Emerging evidence for FFLO states in layered organic superconductors (review article), *Low Temp. Phys.* **39**, 225 (2013).

[49] A. Bianchi, R. Movshovich, N. Oeschler, P. Gegenwart, F. Steglich, J. D. Thompson, P. G. Pagliuso, and J. L. Sarrao, First-Order Superconducting Phase Transition in CeCoIn$_5$, *Phys. Rev. Lett.* **89**, 137002 (2002).

[50] H. A. Radovan, N. A. Fortune, T. P. Murphy, S. T. Hannahs, E. C. Palm, S. W. Tozer, and D. Hall, Magnetic enhancement of superconductivity from electron spin domains, *Nature (London)* **425**, 51 (2003).

[51] A. Bianchi, R. Movshovich, C. Capan, P. G. Pagliuso, and J. L. Sarrao, Possible Fulde-Ferrell-Larkin-Ovchinnikov Supercon- ducting State in CeCoIn$_5$, *Phys. Rev. Lett.* **91**, 187004 (2003).

[52] T. Watanabe, Y. Kasahara, K. Izawa, T. Sakakibara, Y. Matsuda, C. J. van der Beek, T. Hanaguri, H. Shishido, R. Settai, and Y. Onuki, High-field state of the flux-line lattice in the uncon- ventional superconductor CeCoIn$_5$, *Phys. Rev. B* **70**, 020506 (2004).

[53] Y. Matsuda and H. Shimahara, Fulde-Ferrell-Larkin- Ovchinnikov state in heavy fermion superconductors, *J. Phys. Soc. Jpn.* **76**, 051005 (2007).

[54] A. Ptok, K. J. Kapcia, P. Piekarz, and A. M Oleś, The $ab$ initio study of unconventional superconductivity in CeCoIn$_5$ and FeSe, *New J. Phys.* **19**, 063039 (2017).

[55] K. Cho, H. Kim, M. A. Tanatar, Y. J. Song, Y. S. Kwon, W. A. Coniglio, C. C. Agosta, A. Gurevich, and R. Prozorov,

AGNIESZKA CICHY AND ANDRZEJ PTOK
PHYSICAL REVIEW A 97, 053619 (2018)

Anisotropic upper critical field and possible Fulde-Ferrel- Larkin-Ovchinnikov state in the stoichiometric pnictide superconductor LiFeAs, Phys. Rev. B 83, 060502 (2011).

[56] D. A. Zocco, K. Grube, F. Eilers, T. Wolf, and H. v. Löhneysen, Pauli-Limited Multiband Superconductivity in $KFe_2As_2$, Phys. Rev. Lett. 111, 057007 (2013).

[57] A. Ptok, Multiple phase transitions in Pauli-limited iron- based superconductors, J. Phys.: Condens. Matter 27, 482001 (2015).

[58] A. Ptok and D. Crivelli, The Fulde-Ferrell-Larkin-Ovchinnikov state in pnictides, J. Low Temp. Phys. 172, 226 (2013).

[59] C. W. Cho, J. H. Yang, N. F. Q. Yuan, J. Shen, T. Wolf, and R. Lortz, Thermodynamic Evidence for the Fulde-Ferrell-Larkin- Ovchinnikov State in the $KFe_2As_2$ Superconductor, Phys. Rev. Lett. 119, 217002 (2017).

[60] S. Kasahara, T. Watashige, T. Hanaguri, Y. Kohsaka, T. Yamashita, Y. Shimoyama, Y. Mizukami, R. Endo, H. Ikeda, K. Aoyama, T. Terashima, S. Uji, T. Wolf, H. von Löhneysen, T. Shibauchi, and Y. Matsuda, Field-induced superconducting phase of FeSe in the BCS-BEC cross-over, Proc. Natl. Acad. Sci. USA 111, 16309 (2014).

[61] L. W. Gruenberg and L. Gunther, Fulde-Ferrell Effect in Type-II Superconductors, Phys. Rev. Lett. 16, 996 (1966).

[62] S.-Q. Su, K.-M. Tam, and H.-Q. Lin, Evolution of supercon- ductor pairing interactions from weak to strong coupling on a honeycomb lattice, Phys. Rev. B 80, 104517 (2009).

[63] M. Januszewski, A. Ptok, D. Crivelli, and B. Gardas, GPU-based acceleration of free energy calculations in solid state physics, Comput. Phys. Commun. 192, 220 (2015).

[64] A. Ptok, A. Cichy, K. Rodríguez, and K. J. Kapcia, Critical behavior in one dimension: Unconventional pairing, phase sep- aration, BEC-BCS crossover, and magnetic Lifshitz transition, Phys. Rev. A 95, 033613 (2017).

[65] R. Micnas, J. Ranninger, and S. Robaszkiewicz, Superconduc- tivity in narrow-band systems with local nonretarded attractive interactions, Rev. Mod. Phys. 62, 113 (1990).

[66] D. J. Klein, G. E. Hite, W. A. Seitz, and T. G. Schmalz, Dimer coverings and Kekulé structures on honeycomb lattice strips, Theor. Chim. Acta 69, 409 (1986).

[67] B. Roy and I. F. Herbut, Unconventional superconductivity on honeycomb lattice: Theory of Kekule order parameter, Phys. Rev. B 82, 035429 (2010).

[68] Z.-X. Li, Y.-F. Jiang, S.-K. Jian, and H. Yao, Fermion-induced quantum critical points, Nat. Commun. 8, 314 (2017).

[69] G. Sarma, On the influence of a uniform exchange field acting on the spins of the conduction electrons in a superconductor, J. Phys. Chem. Solids 24, 1029 (1963).

[70] H. Hu and X. J. Liu, Mean-field phase diagrams of imbalanced Fermi gases near a Feshbach resonance, Phys. Rev. A 73, 051603 (2006).

[71] X.-J. Liu, H. Hu, and P. D. Drummond, Fulde-Ferrell-Larkin- Ovchinnikov states in one-dimensional spin-polarized ultracold atomic Fermi gases, Phys. Rev. A 76, 043605 (2007).

[72] J. P. A. Devreese, S. N. Klimin, and J. Tempere, Resonant enhancement of the Fulde-Ferell-Larkin-Ovchinnikov state in three dimensions by a one-dimensional optical potential, Phys. Rev. A 83, 013606 (2011).

[73] V. Oganesyan, S. A. Kivelson, and E. Fradkin, Quantum theory of a nematic Fermi fluid, Phys. Rev. B 64, 195109 (2001).

[74] D. G. Barci and L. E. Oxman, Strongly correlated fermions with nonlinear energy dispersion and spontaneous gener- ation of anisotropic phases, Phys. Rev. B 67, 205108 (2003).

[75] D. G. Barci and P. S. A. Bonfim, Superconductivity near Pomeranchuk instabilities in the spin channel, Mod. Phys. Lett. B 27, 1350102 (2013).

[76] P. Schlottmann, Instabilities of a Fermi gas with nested Fermi surfaces, Ann. Phys. (Berlin) 530, 1700263 (2017).

[77] I. I. Pomeranchuk, On the stability of a Fermi liquid, Zh. Eksp. Teor. Fiz. 35, 524 (1959) [Sov. Phys. JETP 8, 361 (1959)].

[78] T. M. Whitehead and G. J. Conduit, Multiparticle instability in a spin-imbalanced Fermi gas, Phys. Rev. B 97, 014502 (2018).

[79] P. F. Bedaque, H. Caldas, and G. Rupak, Phase Separation in Asymmetrical Fermion Superfluids, Phys. Rev. Lett. 91, 247002 (2003).

[80] A. Kujawa-Cichy and R. Micnas, Stability of superfluid phases in the 2D spin-polarized attractive Hubbard model, Europhys. Lett. 95, 37003 (2011).

[81] A. Cichy and R. Micnas, The spin-imbalanced attractive Hub- bard model in $d=3$: Phase diagrams and BCS-BEC crossover at low filling, Ann. Phys. (NY) 347, 207 (2014).

[82] K. Seki and Y. Ohta, Quantum phase transitions in the honeycomb-lattice Hubbard model, arXiv:1209.2101.

[83] H.-F. Lin, H.-D. Liu, H.-S. Tao, and W.-M. Liu, Phase transitions of the ionic Hubbard model on the honeycomb lattice, Sci. Rep. 5, 9810 (2015).

[84] F. Heidrich-Meisner, A. E. Feiguin, U. Schollwöck, and W. Zwerger, BCS-BEC crossover and the disappearance of Fulde- Ferrell-Larkin-Ovchinnikov correlations in a spin-imbalanced one-dimensional Fermi gas, Phys. Rev. A 81, 023629 (2010).

[85] K.-E. Huhtinen, M. Tylutki, P. Kumar, T. I. Vanhala, S. Peotta, and P. Törmä, Spin-imbalanced pairing and fermi surface defor- mation in flat bands, arXiv:1802.00274.

[86] R. Saito, M. Fujita, G. Dresselhaus, and M. S Dresselhaus, Electronic structure of chiral graphene tubules, Appl. Phys. Lett. 60, 2204 (1992).

[87] R. Saito, M. Fujita, G. Dresselhaus, and M. S. Dresselhaus, Electronic structure of graphene tubules based on $C_{60}$, Phys. Rev. B 46, 1804 (1992).

[88] J. González, Kohn-Luttinger superconductivity in graphene, Phys. Rev. B 78, 205431 (2008).

[89] I. F. Herbut, V. Juričić, and B. Roy, Theory of interacting electrons on the honeycomb lattice, Phys. Rev. B 79, 085116 (2009).

[90] R. Nandkishore, L. S. Levitov, and A. V. Chubukov, Chiral su- perconductivity from repulsive interactions in doped graphene, Nat. Phys. 8, 158 (2012).

[91] R. Nandkishore, R. Thomale, and A. V. Chubukov, Supercon- ductivity from weak repulsion in hexagonal lattice systems, Phys. Rev. B 89, 144501 (2014).

[92] H. Shimahara, Fulde-Ferrell state in quasi-two-dimensional superconductors, Phys. Rev. B 50, 12760 (1994).

[93] A. Ptok, The influence of the dimensionality of the sys- tem on the realization of unconventional Fulde-Ferrell-Larkin- Ovchinnikov pairing in ultra-cold Fermi gases, J. Phys.: Condens. Matter 29, 475901 (2017).

053619-10

[94] J. Guo, H.-M. Jiang, and J.-X. Li, Exploring the relationship between the magnetic frustration and the emergence of FFLO state on a triangular lattice, *Physica C* **471**, 533 (2011).

[95] X.-S. Ye, L.-H. Pan, and H.-M. Jiang, Quantum phase transition of the Fulde-Ferrell-Larkin-Ovchinnikov states in two-dimensional anisotropic triangular system, *Physica C* **470**, 669 (2010).

[96] A. Ptok, M. M. Maśka, and M. Mierzejewski, The Fulde-Ferrell-Larkin-Ovchinnikov phase in the presence of pair hopping interaction, *J. Phys.: Condens. Matter* **21**, 295601 (2009).

[97] See Supplemental Material at http://link.aps.org/supplemental/10.1103/PhysRevA.97.053619 for illustration of the spatial modulation of the superconducting order parameter (SOP) in real space for different $\boldsymbol{Q}$. Black crosses denote the position of the lattice sites in real space, while the size and color of closed circles correspond to the value and sign of the SOP (blue and red denote minus and plus, respectively).