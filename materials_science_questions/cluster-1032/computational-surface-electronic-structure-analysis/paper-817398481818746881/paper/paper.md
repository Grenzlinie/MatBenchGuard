PHYSICAL REVIEW B 103, 085413 (2021)

# Floquet second order topological superconductor based on unconventional pairing

Arnob Kumar Ghosh $^{1,2,*}$, Tanay Nag $^{3,4,\dagger}$ and Arijit Saha $^{1,2,\ddagger}$

$^{1}$Institute of Physics, Sachivalaya Marg, Bhubaneswar-751005, India
$^{2}$Homi Bhabha National Institute, Training School Complex, Anushakti Nagar, Mumbai 400094, India
$^{3}$SISSA, via Bonomea 265, 34136 Trieste, Italy
$^{4}$Institut für Theorie der Statistischen Physik, RWTH Aachen University, 52056 Aachen, Germany

![](./images/817398481818746881_1.jpg)
(Received 7 December 2020; revised 22 January 2021; accepted 26 January 2021; published 8 February 2021)

We theoretically investigate the Floquet generation of second-order topological superconducting (SOTSC) phase in the high-temperature platform both in two dimension (2D) and three dimension (3D). Starting from a $d$-wave superconducting pairing gap, we periodically kick the mass term to engineer the dynamical SOTSC phase within a specific range of the strength of the drive. Under such dynamical breaking of time-reversal symmetry (TRS), we show the emergence of the *weak* SOTSC phase, harboring eight corner modes, i.e., two zero-energy Majorana per corner, with vanishing Floquet quadrupole moment. On the other hand, our study interestingly indicates that upon the introduction of an explicit TRS breaking Zeeman field, the *weak* SOTSC phase can be transformed into *strong* SOTSC phase, hosting one zero-energy Majorana mode per corner, with quantized quadrupole moment. We also compute the Floquet Wannier spectra that further establishes the *weak* and *strong* nature of these phases. We numerically verify our protocol computing the exact Floquet operator in open boundary condition and then analytically validate our findings with the low energy effective theory (in the high-frequency limit). The above protocol is applicable for 3D as well as where we find one dimensional (1D) hinge mode in the SOTSC phase. We then show that these corner modes are robust against moderate disorder and the topological invariants continue to exhibit quantized nature until disorder becomes substantially strong. The existence of zero-energy Majorana modes in these higher-order phases is guaranteed by the antiunitary spectral symmetry.

DOI: 10.1103/PhysRevB.103.085413

## I. INTRODUCTION

The advent of topological superconductors (TSCs), harboring Majorana zero modes (MZMs) at their boundary, have generated immense interest in the quantum condensed matter community from both theoretical and experimental perspectives in the last few years [1–5]. Due to the non-Abelian statistics of the MZMs, they are proposed to be suitable candidates for the topological quantum computation [6,7]. There have been multitudinous proposals based on heterostructure setup of materials with strong spin-orbit coupling such as topological insulator, semiconductor thin films, and nanowires with the proximity induced superconductivity and Zeeman field that provide an efficient platform to realize the MZMs [8–12].

In recent times, the concept of conventional bulk-boundary correspondence of topological phases in various topological systems such as topological insulators (TIs), Dirac semimetals (DSMs), Weyl semimetals (WSMs), TSCs, etc. have been generalized to higher-order topological (HOT) phases [13–43]. To be precise, an $n$th order $d$-dimensional TI/TSC exhibits gapless modes on their $(d-n)$-dimensional boundary ($n \leqslant d$). In particular, a 3D second (third) order TIs/TSCs are characterized by the presence of one (zero)-dimensional hinge (corner) modes, whereas 2D second order topological insulators (SOTIs)/SOTSCs exhibit zero-dimensional (0D) corner modes only. There have been a few experimental proposals to realize 2D SOTIs hosting corner modes, based on acoustic materials [44], photonic crystals [45,46], and electrical circuit [47] setups.

Given the growing interest of the research community in this field, the nonequilibrium Floquet engineering emerges as a fertile hunch to generate the dynamical analog of the HOT phases. It has been shown that a trivial phase can be made topologically nontrivial with suitable periodic driving [48–54]. The time translational symmetry of the problem causes the Floquet topological phase to host dissipationless dynamical topological boundary modes. The resulting bulk-boundary correspondence here becomes intriguing in the presence of the extra-temporal dimension. This nonequilibrium version of generating topological phase have been applied to HOTIs/HOTSCs resulting in Floquet HOTIs (FHOTIs) [55–72]. However, the search for Floquet HOTSCs (FHOTSCs) is still at its initial stage [59,61,70,73,74] even from a theoretical point of view.

In a very recent work, we show that the Floquet SOTSC phase can be engineered by kicking the time-reversal symmetry (TRS) breaking perturbation while the underlying static, $s$-wave proximitized parent system is in a trivial phase [70]. In

*arnob@iopb.res.in
†tnag@physik.rwth-aachen.de
‡arijit@iopb.res.in

2469-9950/2021/103(8)/085413(14)
085413-1
©2021 American Physical Society

this paper, we aim to generate Floquet SOTSC phase, hosting MZMs at the corner (hinges) for a 2D (3D) system, by suitably tuning some other parameter of the underlying first order TI such as the onsite mass term. Given the recent experimental advancements in Floquet systems based on solid state systems [75], metamaterials [52,53,76–78], we believe that our question regarding the Floquet generation of MZMs in HOTSC phase is timely and pertinent. More importantly, the kicking of the onsite term has been able to demonstrate a variety of interesting theoretical observation such as Floquet topological insulator and superconductor [51,58,79,80] dynamical localization [81,82], survival probability of initial state [83,84], and thus motivates us to consider the onsite mass kicking dynamical protocol in order to obtain the desired outcome. However, the dynamical manipulation of mass term is yet to be experimentally realized. Moreover, the 2D TIs have been experimentally realized at high-temperature 100 K [85,86], paving the way to explore the high-temperature platform of MZMs.

To investigate the above mentioned possibility, we begin with a 2D TI in close proximity to a $d$-wave superconductor with unconventional pairing. Here, we consider the external drive to be periodically kicking the onsite mass term of the first order TI. This results in a *weak* Floquet SOTSC (FSOTSC) phase where two MZMs are localized at each corner of the 2D sample. Here the TRS is dynamically broken in the effective Floquet Hamiltonian. Remarkably, this degeneracy of two Majorana corner modes (MCMs) per corner can be lifted by incorporating an explicit TRS broken Zeeman field leading to a *strong* FSOTSC phase with one MZM per corner. We numerically study the exact Floquet operator to obtain the above mentioned results that are further verified by the low energy effective theory in the high-frequency approximation. We characterize the topological nature of these phases by the appropriate topological invariants as Floquet quadrupole moment (FQM) and Floquet Wannier spectra (FWS). We then extend our proposal to 3D where also we find the *weak* (*strong*) FSOTSC phase in the absence (presence) of a homogeneous Zeeman field. Here, the corresponding HOT phase hosts 1D Majorana hinge modes (MHMs). Furthermore, we investigate the effect of disorder on these Majorana corner modes (MCMs), and we find that these modes are robust against moderate disorder strength. The existence of the MZMs are protected by antiunitary spectral symmetry in all of the above cases.

The remainder of the paper is organized as follows. In Sec. II, we introduce our model and the driving protocol. We illustrate the emergence of Floquet MCMs in the local density of states (LDOS) behavior. We resort to low energy edge theory to understand the emergence of the corner mode solutions. First, we solve these edge Hamiltonians to derive the corner mode solution. We characterize the MCMs using FQM and FWS. In Sec. III, we provide a protocol to generate 3D FSOTSC. We show the appearance of MHMs in rod geometry. We use low energy surface theory to confirm the existence of these hinge modes. Then we provide the analytical solutions for the hinge modes by solving the surface Hamiltonian. In Sec. IV, we study the effect of disorder on MZMs and show that they are robust against a finite amount of disorder. Finally in Sec. V, we summarize and conclude our results.

![](./images/817398481818746881_2.jpg)

FIG. 1. Schematic of our setup is demonstrated in the presence of a periodic kick (yellow, light gray) in the mass term as an external drive. Here, a 2D TI (violet, dark gray) is placed in close proximity to a bulk high-temperature $d$-wave superconductor (cyan, light gray). MCMs are shown by circular dots (gray) at the four corners of the 2D sample and the four edges of the TI are denoted by I, II, III, IV.

## II. MAJORANA CORNER MODES IN 2D

In this section, we discuss in detail the model Hamiltonian of our setup along with the driving protocol, the emergence of Floquet MCMs by numerically computing the exact Floquet evolution operator, low energy effective edge theory in the high-frequency regime and analytical understanding of the MCMs solutions therein.

### A. Model Hamiltonian and driving protocol

#### 1. Model

We consider the model of a 2D TI proximitized with $d$-wave superconductivity on a square lattice [23]. This is schematically shown in Fig. 1. The experimental realization of high-temperature 2D TI allows us to consider proximity induced high-temperature superconductor [85,86]. It acquires the following form while written in Bogoliubov-de Gennes (BdG) basis $H_{\text{BdG}} = \frac{1}{2}\sum_{\mathbf{k}} \Psi_{\mathbf{k}}^{\dagger}\mathcal{H}_{0}(\mathbf{k})\Psi_{\mathbf{k}}$, with $\Psi_{\mathbf{k}} = \left(c_{\mathbf{k},a\uparrow},c_{-\mathbf{k},a\uparrow}^{\dagger},c_{\mathbf{k},a\downarrow},c_{-\mathbf{k},a\downarrow}^{\dagger},c_{\mathbf{k},b\uparrow},c_{-\mathbf{k},b\uparrow}^{\dagger},c_{\mathbf{k},b\downarrow},c_{-\mathbf{k},b\downarrow}^{\dagger}\right)^{T}$ and $\mathcal{H}_{0}(\mathbf{k})$, is given by
$$
\begin{aligned}
\mathcal{H}_{0}(\mathbf{k}) & =\epsilon(\mathbf{k})\Gamma_{1}+\lambda_{x}\sin k_{x}\Gamma_{2}+\lambda_{y}\sin k_{y}\Gamma_{3}+\Delta(\mathbf{k})\Gamma_{4} \\
& +B_{x}\Gamma_{5}\equiv\mathbf{N}(\mathbf{k})\cdot\mathbf{\Gamma}.\qquad\qquad(1)
\end{aligned}
$$

Here, $t_{x,y}$ and $\lambda_{x,y}$ represent the nearest-neighbor hopping and spin-orbit coupling, respectively, $\epsilon(\mathbf{k})=(m_{0}-t_{x}\cos k_{x}-t_{y}\cos k_{y})$, $\Delta(\mathbf{k})=\Delta_{0}(\cos k_{x}-\cos k_{y})$ is the $d$-wave superconducting pairing term, and $m_{0}$ is the crystal-field splitting energy. In Eq. (1), $\Gamma_{1}=\sigma_{z}\tau_{z}$, $\Gamma_{2}=\sigma_{x}s_{z}$, $\Gamma_{3}=\sigma_{y}\tau_{z}$, $\Gamma_{4}=s_{y}\tau_{y}$, and $\Gamma_{5}=s_{x}\tau_{z}$. The three Pauli matrices $\boldsymbol{\sigma}$, $\mathbf{s}$, and $\boldsymbol{\tau}$ act on orbital $(a,b)$, spin $(\uparrow,\downarrow)$, and particle-hole degrees of freedom, respectively. When $B_{x}=0$, the system respects TRS, i.e., $\mathcal{T}^{-1}\mathcal{H}_{0}(\mathbf{k})\mathcal{T}=\mathcal{H}_{0}(-\mathbf{k})$ with $\mathcal{T}=is_{y}\mathcal{K}$, $\mathcal{K}$ being the complex-conjugation operator. The Hamiltonian continues to preserve the particle-hole symmetry (PHS) $\mathcal{C}^{-1}\mathcal{H}_{0}(\mathbf{k})\mathcal{C}=-\mathcal{H}_{0}(-\mathbf{k})$ with $\mathcal{C}=\tau_{x}\mathcal{K}$ for $B_{x}\neq0$. Below we discuss the properties of our model at length.

First, we discuss the topological nature associated with the Hamiltonian [Eq. (1)] for $\Delta(\mathbf{k})=0$ and $B_{x}=0$. This model supports topological phase, hosting gapless helical edge modes, when $|m_{0}|<t_{x}+t_{y}$. For $|m_{0}|>t_{x}+t_{y}$, the model becomes trivially gapped. Upon the introduction of $d$-wave pairing only, i.e., $\Delta(\mathbf{k})\neq0$ and $B_{x}=0$, the 1D massless Dirac fermions representing the edge modes of TI phase,

become gapped by the induced unconventional superconducting pairing. However, the specific nature of pairing symmetry causes the Dirac mass to change signs at the corners. This in turn generates MCMs, a signature of SOTSC phase for TRS invariant TSC system, as domain-wall excitations when $|m_0| < t_x + t_y$. Here, one can observe Majorana Kramers pairs (MKPs) (i.e., two Majoranas per corner are time-reversal partners of each other) pinned at zero energy which are protected by the TRS. When $|m_0| > t_x + t_y$, the underlying TI becomes nontopological and $d$-wave pairing cannot lead to MKPs anymore as the system becomes gapped. Now, in the presence of TRS breaking Zeeman field $B_x \neq 0$, the degeneracy of MKPs can be lifted by destroying one mode in the pair at the corner. Therefore, the Hamiltonian supports MZMs with one Majorana per corner for $\Delta(\mathbf{k}) \neq 0$ and $B_x \neq 0$ while $|m_0| < t_x + t_y$. The magnetic field allows us to tune the bulk gap which is introduced by the superconducting order parameter $\Delta(\mathbf{k})$. Given this background, it would be interesting to study the emergence of MCMs starting from the underlying nontopological phase $|m_0| > t_x + t_y$ by periodically kicking the mass with a finite amplitude and frequency.

### 2. Driving protocol and Floquet operator

Here we introduce our driving protocol in the form of periodic kick in the mass term as discussed before

$$
m(t)=m_{1} \sum_{r=1}^{\infty} \delta(t-r T),\qquad(2)
$$

with $r$ being an integer. This driving protocol allows one to write the exact Floquet operator in the following way using the time ordered (TO) notation as

$$
\begin{aligned}
U(T) & =\mathbf{T O} \exp \left[-i \int_{0}^{T} d t\left(\mathcal{H}_{0}(\mathbf{k})+m(t) \Gamma_{1}\right)\right] \\
& =\exp \left(-i \mathcal{H}_{0}(\mathbf{k}) T\right) \exp \left(-i m_{1} \Gamma_{1}\right).
\end{aligned}\qquad(3)
$$

Here, $T$ and $m_1$ are the period and amplitude of the drive, respectively. The above decomposition essentially means that the system is freely evolved between two subsequent kicks. The Floquet operator $U(T)$ can be written in a more compact form as follows

$$
U(T)=C_{T}\left(p-i q \Gamma_{1}\right)-i S_{T} \sum_{j=1}^{5}\left(n_{j} \Gamma_{j}+m_{j} \Gamma_{j 1}\right),\quad(4)
$$

where $C_T = \cos(|\mathbf{N}(\mathbf{k})|T)$, $S_T = \sin(|\mathbf{N}(\mathbf{k})|T)$, $p = \cos m_1$, $q = \sin m_1$, $n_j = \frac{N_j(\mathbf{k})\cos m_1}{|\mathbf{N}(\mathbf{k})|}$, $m_j = \frac{N_j(\mathbf{k})\sin m_1}{|\mathbf{N}(\mathbf{k})|}$, and $\Gamma_{j1} = \frac{1}{2i}[\Gamma_j, \Gamma_1]$ with $j=2,3,4,5$. One can thus obtain the general form of the effective Hamiltonian as

$$
H_{\mathrm{Flq}}=\frac{\xi_{\mathbf{k}}}{\sin \xi_{\mathbf{k}} T}\left[\sin (|\mathbf{N}(\mathbf{k})| T) \cos m_{1} \sum_{j=1}^{5} r_{j} \Gamma_{j}+\cos (|\mathbf{N}(\mathbf{k})| T) \sin m_{1} \Gamma_{1}+\sin (|\mathbf{N}(\mathbf{k})| T) \sin m_{1} \sum_{j=2}^{5} r_{j} \Gamma_{j 1}\right],\qquad(5)
$$

with $\xi_{\mathbf{k}}=\frac{1}{T} \cos ^{-1}\left[\cos (|\mathbf{N}(\mathbf{k})| T) \cos m_{1}\right]$, $r_j = \frac{N_j(\mathbf{k})}{|\mathbf{N}(\mathbf{k})|}$. In the high-frequency limit, i.e., $T \to 0$ and small amplitude of drive, i.e., $m_1 \to 0$, one can neglect the higher order terms in $T$ and $m_1$. Thus, the effective Hamiltonian in that limit reads as

$$
H_{\mathrm{Flq}} \approx \mathcal{H}_{0}(\mathbf{k})+\frac{m_{1}}{T} \Gamma_{1}+m_{1} \sum_{j=2}^{5} r_{j} \Gamma_{j 1}.\qquad(6)
$$

In Eq. (6), terms associated with $\Gamma_{j1}$ are originated due to the driving and not present in the static Hamiltonian [Eq. (1)]. It is noteworthy that these extra $r_j\Gamma_{j1}$ terms break TRS $\mathcal{T}$ in the system. Consequently, the above Hamiltonian breaks TRS $\mathcal{T}$ even when $B_x=0$. This reflects the fact that the TRS can be broken dynamically by mass kicking while the static perturbation respects the TRS. Therefore, it would be important to study the effect of these terms in the dynamics with and without the magnetic field. The former situation can be referred to as the explicit breaking of TRS while the latter is related to the dynamical breaking of TRS. At the outset, we would like to comment from Eq. (6) that the mass term gets renormalized by the driving $m_0 \to m_0 + m_1/T$. Therefore, the topological phase boundary thus got renormalized. Hence, MCMs can be found when $|m_0 + m_1/T| < t_x + t_y$ with $\Delta(\mathbf{k}) \neq 0$ and $B_x \neq 0$. Similar to the static case, here also for the Floquet case the magnetic field allows us to tune the bulk gap which is introduced by the superconducting order parameter $\Delta(\mathbf{k})$. This would lead to analytical handling which we describe below in terms of the low energy effective model. In the presence of $\Delta$, interestingly, we find $H_{\text{Flq}}$ continues to preserve the antiunitary PHS generated by $\mathcal{C}$. This antiunitary symmetry is essential to localize the MCMs at zero energy associated with the effective Hamiltonian [Eq. (6)]. Here, we would like to emphasize that we make use of the high-frequency Hamiltonian [Eq. (6)] only to corroborate the existence of the *dressed* corner modes which we obtain from the exact diagonalization of the Floquet operator $U(T)$ [Eq. (3)] (see Fig. 1).

### B. Floquet corner mode

Having established the possible route to an analytical understanding of the emergence of MZMs, we here numerically show their existence in the 2D FSOTSC phase that is characterized by the presence of Floquet MCMs. To be precise, we find the signature of dynamical MCMs that appear in the Floquet LDOS as shown in Fig. 2. We know $U(T)|\phi_m\rangle = \exp(-i\mu_m T)|\phi_m\rangle$, where $|\phi_m\rangle$ is the Floquet quasienergy states corresponding to the Floquet quasienergy $\mu_m$. To calculate the LDOS, we numerically diagonalize the Floquet operator $U(T)$ [in Eq. (3)] in the open boundary condition (OBC). Here, we consider the Floquet eigenmodes $|\phi_m\rangle$'s associated with $\mu_m \approx 0$ (within numerical accuracy) to compute

![](./images/817398481818746881_3.jpg)

FIG. 2. (a) The behavior of LDOS, associated with the MCMs at $\mu_m=0$, is demonstrated for $B_x=0$ considering finite geometry. The inset exhibits the Floquet quasienenergy spectrum $\mu_m$ as a function of $m$ where eight MZMs are observed. Here, $L_x=L_y=25, t_x=t_y=\lambda_x=\lambda_y=1.0, m_0=2.5$, $\Delta=0.6, m_1=-0.4, T=0.419$. (b) LDOS in finite geometry and eigenvalue spectrum (inset) are depicted for $B_x=0.3$. Here four MZMs appear at quasienergy $\mu_m=0$. The number of MCMs at $\mu_m=0$ can be reduced to half upon the introduction of the Zeeman field.

the LDOS of these zero-energy states. These MCMs can be easily distinguished from the gapped bulk modes. Note that the 2D SOTSC phase hosting MCMs has been very recently studied in static [23,31,32,36] and Floquet driven [61,70] cases with different driving protocols.

We consider two cases: In the first case, we set the amplitude of the in-plane magnetic field, $B_x=0$, and the corresponding LDOS is shown in Fig. 2(a). One can identify from the inset of Fig. 2(a) that there exist eight MCMs, i.e., two MZMs per corner. While for $B_x\neq0$, we obtain four MCMs, i.e., one MZM per corner as depicted in the inset of Fig. 2(b). One can thus infer from Fig. 2(a) that two MZMs sharing the same corner annihilate each other to give rise to an electronic corner mode which may lead to a *weak* FSOTSC phase. Interestingly, in Fig. 2(b) the applied in-plane magnetic field yields only one MZM per corner carrying a signature of *strong* FSOTSC phase [70]. Moreover, the localization properties of these MCMs are significantly modified with the introduction of the Zeeman field. From the weight structure of MCMs as observed in LDOS, it is evident that the localization length remains the same in the $x$ and $y$ direction for $B_x=0$. Finite $B_x$ breaks this symmetry of localization length and the weight becomes less along the $y$ direction as compared to the $x$ direction. The introduction of $B_y$ instead of $B_x$ does not change these properties. We discuss more regarding this in the latter part of the paper.

### C. Low energy edge theory

Here, we turn ourselves to the low energy edge theory to corroborate the findings of the MCMs. We begin by expanding the effective Hamiltonian in the high-frequency limit [Eq. (6)] around the $\Gamma=(0,0)$ point as

$$
\begin{aligned}
H_{\text{Flq},\Gamma} & \approx\left(m'-\frac{t_x}{2}k_x^2-\frac{t_y}{2}k_y^2\right)\Gamma_1+\lambda_x k_x\Gamma_2+\lambda_y k_y\Gamma_3 \\
& -\frac{\Delta}{2}\left(k_x^2-k_y^2\right)\Gamma_4+B_x\Gamma_5+\frac{m_1}{T}\Gamma_1+m_1\lambda_x k_x\Gamma_{21} \\
& +m_1\lambda_y k_y\Gamma_{31}-\frac{m_1\Delta}{2}\left(k_x^2-k_y^2\right)\Gamma_{41},
\end{aligned}
$$

where $m'=(m_0-t_x-t_y)$, $\Gamma_{21}=-\sigma_y s_z\tau_z$, $\Gamma_{31}=\sigma_x$, and $\Gamma_{41}=\sigma_z s_y\tau_x$. For a demonstrative example, we present the analytical solution for edge-I. We consider here the open (periodic) boundary condition along the $x$ ($y$) direction. We rewrite $H_{\text{Flq},\Gamma}=H_0(-i\partial_x)+H_p(-i\partial_x,k_y)$ by replacing $k_x\rightarrow -i\partial_x$ and neglecting $k_y^2$ term. We thus obtain

$$
\begin{aligned}
H_0 & =\left(m-\frac{t_x}{2}\partial_x^2\right)\Gamma_1-i\lambda_x\partial_x\Gamma_2, \\
H_p & =\lambda_y k_y\Gamma_3+\frac{\Delta}{2}\partial_x^2\Gamma_4+B_x\Gamma_5-im_1\lambda_x\partial_x\Gamma_{21} \\
& +m_1\lambda_y k_y\Gamma_{31}+\frac{m_1\Delta}{2}\partial_x^2\Gamma_{41}.
\end{aligned}
$$

Here, we consider the pairing amplitude $\Delta$ and the amplitude of the in-plane magnetic field $B_x$ to be small and treat them as small perturbation [23,32,70]. The mass term $m=(m'+\frac{m_1}{T})$ is considered to be less than zero. Assuming $\Psi$ to be the zero-energy eigenstate of $H_0$ and following the boundary condition $\Psi(x=0)=\Psi(x=\infty)=0$, we obtain

$$
\Psi_\alpha=|\mathcal{N}_x|^2 e^{-\mathcal{K}_1 x}\sin\mathcal{K}_2 x\ e^{ik_y y}\Phi_\alpha,
$$

where $\mathcal{K}_1=\frac{\lambda_x}{t_x}$, $\mathcal{K}_2=\sqrt{|\frac{m}{t_x}|-\mathcal{K}_1^2}$, $|\mathcal{N}_x|^2=\frac{4\mathcal{K}_1(\mathcal{K}_1^2+\mathcal{K}_2^2)}{\mathcal{K}_2^2}$, and $\Phi_\alpha$ is an eight-component spinor satisfying $\sigma_y s_z\tau_z\Phi_\alpha=-\Phi_\alpha$. Our chosen basis reads

$$
\begin{aligned}
& \Phi_1=|\sigma_y=+1\rangle\otimes|s_z=+1\rangle\otimes|\tau_z=-1\rangle, \\
& \Phi_2=|\sigma_y=-1\rangle\otimes|s_z=+1\rangle\otimes|\tau_z=+1\rangle, \\
& \Phi_3=|\sigma_y=-1\rangle\otimes|s_z=-1\rangle\otimes|\tau_z=-1\rangle, \\
& \Phi_4=|\sigma_y=+1\rangle\otimes|s_z=-1\rangle\otimes|\tau_z=+1\rangle.
\end{aligned}
$$

The matrix element of $H_p$ in this basis can be written as

$$
H_{\text{I},\alpha\beta}^{\text{Edge}}=\int_0^\infty dx\ \Psi_\alpha^\dagger(x)H_p(-i\partial_x,k_y)\Psi_\beta(x).
$$

Thus, we obtain the effective Hamiltonian for the edge-I as

$$
H_{\text{I}}^{\text{Edge}}=-\lambda_y k_y s_z+M_{\text{I}}s_y\tau_y,
$$

where $M_{\text{I}}=|\frac{m\Delta}{t_x}|$. Similarly, for edge-II, III, and IV, one can obtain the effective Hamiltonian as

$$
\begin{aligned}
& H_{\text{II}}^{\text{Edge}}=\lambda_x k_x s_z-M_{\text{II}}s_y\tau_y-B_x s_x\tau_z, \\
& H_{\text{III}}^{\text{Edge}}=-\lambda_y k_y s_z+M_{\text{III}}s_y\tau_y, \\
& H_{\text{IV}}^{\text{Edge}}=\lambda_x k_x s_z-M_{\text{IV}}s_y\tau_y-B_x s_x\tau_z.
\end{aligned}
$$

where $M_{\text{II}}=|\frac{m\Delta}{t_y}|$, $M_{\text{III}}=M_{\text{I}}$, and $M_{\text{IV}}=M_{\text{II}}$. Therefore, the low energy effective Hamiltonian written in the edge coordinate $j$ is given by the compact form as

$$
H_j^{\text{Edge}}=-i\lambda(j)s_z\partial_j+M(j)s_y\tau_y-B(j)s_x\tau_z,
$$

with $\lambda(j)=\{-\lambda_y,\lambda_x,-\lambda_y,\lambda_x\}$, $M(j)=\{M_{\text{I}},-M_{\text{II}}, M_{\text{III}},-M_{\text{IV}}\}$, and $B(j)=\{0,B_x,0,B_x\}$. Note that one can consider $B_y$ instead of $B_x$; however, the above results do not change qualitatively. Now to proceed further we study two cases.

### I. Case I: $B_x = 0$

First, we turn off the in-plane magnetic field $B_x$. The edge Hamiltonian $H_j^{\text{Edge}}$ can be decomposed into two independent blocks as
$$
H_j^{\text{Edge}} = H_{\tau_y=+1} \oplus H_{\tau_y=-1}, \tag{15}
$$
where
$$
\begin{align}
H_{\tau_y=+1} &= -i\lambda(j)s_z\partial_j + M(j)s_y, \\
H_{\tau_y=-1} &= -i\lambda(j)s_z\partial_j - M(j)s_y. \tag{16}
\end{align}
$$

We obtain domain walls for both these blocks $\tau_y = \pm 1$ as the mass term $M(j)$ changes its sign between two adjacent edges; from edge-I, III to edge-II, IV. In terms of the system parameters the Dirac mass changes from $|\frac{m_\Delta}{t_x}|$ to $-|\frac{m_\Delta}{t_y}|$. Consequently, one finds two MZMs per corner [see Fig. 2(a)]; each block is giving rise to one MZM per corner. Therefore, one finds the origin of MCMs at each corner as obtained from the above low-energy edge theory. The dynamical breaking of TRS is only thus able to generate a *weak* FSOTSC phase (see text for discussion).

### 2. Case II: $B_x \neq 0$

Incorporating the Zeeman field $B_x \neq 0$, in $\tau_x = s_z$ subspace, the last term in Eq. (14) can be written as $B(j)s_x\tau_z \to \mp B(j)s_y$ for the $\tau_y = \pm 1$ block. The edge Hamiltonian $H_j^{\text{Edge}} = H_{\tau_y=+1} \oplus H_{\tau_y=-1}$ thus takes the following form upon decomposing into two independent blocks as
$$
\begin{align}
H_{\tau_y=+1} &= -i\lambda(j)s_z\partial_j + D(j)s_y, \\
H_{\tau_y=-1} &= -i\lambda(j)s_z\partial_j - D'(j)s_y, \tag{17}
\end{align}
$$
with $D(j) = \{D_{\text{I}}, D_{\text{II}}, D_{\text{III}}, D_{\text{IV}}\} = M(j) + B(j)$ and $D'(j) = \{D_{\text{I}}', D_{\text{II}}', D_{\text{III}}', D_{\text{IV}}'\} = M(j) - B(j)$. Hence, one can eventually obtain two decoupled diagonal blocks with Dirac masses in different edges as $D_{\text{I}} = |\frac{m_\Delta}{t_x}|$, $D_{\text{II}} = -|\frac{m_\Delta}{t_y}| + B_x$, $D_{\text{III}} = |\frac{m_\Delta}{t_x}|$, and $D_{\text{IV}} = -|\frac{m_\Delta}{t_y}| + B_x$; $D_{\text{I}}' = D_{I}$, $D_{\text{II}}' = -|\frac{m_\Delta}{t_y}| - B_x$, $D_{\text{III}}' = D_{\text{III}}$, and $D_{\text{IV}}' = -|\frac{m_\Delta}{t_y}| - B_x$. Therefore, we observe that $B_x$ can change the gap along edge-II and IV leaving edge-I and III unaltered for both of these blocks. It is now quite evident from Eq. (17) that $B_x = |\frac{m_\Delta}{t_y}|$ ($B_x = -|\frac{m_\Delta}{t_y}|$) refers to a special situation where edge-II and IV become gapless for the $\tau_y = +1$ ($\tau_y = -1$) block. This is in sharp contrast to the edge Hamiltonian without magnetic field as described in Eq. (16) where all four edges are massive. In the present case with magnetic field $B_x = |\frac{m_\Delta}{t_y}|$ ($B_x = -|\frac{m_\Delta}{t_y}|$), the remaining two edges become massive for the $\tau_y = +1$ ($\tau_y = -1$) block. We consider only positive values of $B_x$, and due to that reason we investigate two instances where $B_x > |\frac{m_\Delta}{t_y}|$ and $B_x < |\frac{m_\Delta}{t_y}|$.

When we consider $B_x > |\frac{m_\Delta}{t_y}|$, $D'(j)$ changes its sign from edge-I (III) to edge-II (IV) while $D(j)$ remains positive in all four edges. Therefore, $\tau_y = +1$ block becomes inactive and remains always massive while $\tau_y = -1$, being the only active block, can lead to Jackie-Rebbi localized MCMs at zero quasienergy. One can thus observe one MZM per corner as depicted in Fig. 2(b). On the other hand, for $B_x < |\frac{m_\Delta}{t_y}|$, both the blocks turn out to be active, i.e., mass changes its sign between two adjacent edges. Hence the MZMs are supported by both of these blocks. This would result in two MZMs per corner similar to the LDOS as shown in Fig. 2(a). Therefore, the explicit breaking of TRS by applying the magnetic field appears to be more efficient to obtain the FSOTSC phase as both *weak* (two MZM per corner) and *strong* (one MZM per corner) phases can be explored simultaneously. By contrast, the dynamical breaking of TRS without applying the magnetic field only allows us to explore the *weak* FSOTSC phase. We explain these phases more elaborately while discussing the topological invariants.

---

### D. Corner mode solution

#### 1. Case I: $B_x = 0$

To obtain the analytical solution of the MCMs, residing at the intersection between edge-I and II, we solve the corresponding edge Hamiltonians for the zero-energy solution. At edge-I, we assume a solution of the form
$$
\Psi_C \sim e^{-\xi y}(a_1, a_2, a_3, a_4)^{\tilde{T}}. \tag{18}
$$

Here, $\tilde{T}$ denotes the transpose. The eigenvalue equation for $\Psi_C$ acquires the following form
$$
\begin{pmatrix}
-i\lambda_y\xi & 0 & 0 & -M_{\text{I}} \\
0 & -i\lambda_y\xi & M_{\text{I}} & 0 \\
0 & M_{\text{I}} & i\lambda_y\xi & 0 \\
-M_{\text{I}} & 0 & 0 & i\lambda_y\xi
\end{pmatrix}
\begin{pmatrix}
a_1 \\
a_2 \\
a_3 \\
a_4
\end{pmatrix} = 0. \tag{19}
$$

The secular equation for $\Psi_C$ then reads
$$
\det
\begin{pmatrix}
-i\lambda_y\xi & 0 & 0 & -M_{\text{I}} \\
0 & -i\lambda_y\xi & M_{\text{I}} & 0 \\
0 & M_{\text{I}} & i\lambda_y\xi & 0 \\
-M_{\text{I}} & 0 & 0 & i\lambda_y\xi
\end{pmatrix} = 0. \tag{20}
$$

Solving Eq. (20), we find four solutions for $\xi$ as
$$
\xi = \left\{ -\frac{M_{\text{I}}}{\lambda_y}, -\frac{M_{\text{I}}}{\lambda_y}, \frac{M_{\text{I}}}{\lambda_y}, \frac{M_{\text{I}}}{\lambda_y} \right\}. \tag{21}
$$

Given the fact that $\Psi_C$ must vanish at $y \to \infty$, therefore, we obtain two linearly independent solutions for edge-I, $\Phi_C^{\text{I,1}} = (1, 1, i, -i)^{\tilde{T}}$ and $\Phi_C^{\text{I,2}} = (1, -1, -i, -i)^{\tilde{T}}$. Thus, $\Psi_C$ can be expanded as
$$
\Psi_C \sim \alpha_{\text{I}} e^{-\frac{M_{\text{I}}}{\lambda_y}y}\Phi_C^{\text{I,1}} + \beta_{\text{I}} e^{-\frac{M_{\text{I}}}{\lambda_y}y}\Phi_C^{\text{I,2}}. \tag{22}
$$

Here, $\alpha_{\text{I}}$ and $\beta_{\text{I}}$ are the normalization factors for edge-I. Similarly, for edge-II with $\alpha_{\text{II}}$ and $\beta_{\text{II}}$ being the normalization factors, we obtain
$$
\Psi_C \sim \alpha_{\text{II}} e^{-\frac{M_{\text{II}}}{\lambda_x}x}\Phi_C^{\text{II,1}} + \beta_{\text{II}} e^{-\frac{M_{\text{II}}}{\lambda_x}x}\Phi_C^{\text{II,2}}, \tag{23}
$$
where $\Phi_C^{\text{II,1}} = (1, 1, i, -i)^{\tilde{T}}$ and $\Phi_C^{\text{II,2}} = (1, -1, -i, -i)^{\tilde{T}}$. Considering the wave function $\Psi_C$ to be continuous at the interface, i.e., at $x = y = 0$, we obtain $\alpha_{\text{I}} = \alpha_{\text{II}} = \alpha$ and $\beta_{\text{I}} = \beta_{\text{II}} = \beta$. Hence, the wave function for the MCMs becomes
$$
\begin{align}
\Psi_C &\sim \alpha\ e^{-\frac{M_{\text{I}}}{\lambda_y}y}\Phi_C^{\text{I,1}} + \beta\ e^{-\frac{M_{\text{I}}}{\lambda_y}y}\Phi_C^{\text{I,2}} \quad : \text{edge-I}, \\
\Psi_C &\sim \alpha\ e^{-\frac{M_{\text{II}}}{\lambda_x}x}\Phi_C^{\text{I,1}} + \beta\ e^{-\frac{M_{\text{II}}}{\lambda_x}x}\Phi_C^{\text{I,2}} \quad : \text{edge-II}. \tag{24}
\end{align}
$$

The localization length in the $x$ ($y$) direction becomes $\lambda_x/M_{\text{II}}$ ($\lambda_y/M_{\text{I}}$). This clearly suggests that localization lengths of MCMs are dependent on the strength of hopping, spin-orbit

coupling, mass, and proximity induced superconducting gap function. In the present case, choice of $t_x = t_y$ and $\lambda_x = \lambda_y$ leads to the fact that localization length becomes uniform in the $x$ and $y$ direction as observed in the Floquet LDOS [see Fig. 2(a)]. More importantly, one can observe that there exist two MZMs at each corner corroborating our numerical findings as shown in the inset of Fig. 2(a). The presence of two MCMs suggests that they would annihilate each other leaving an electronic state at the corner. The dynamical breaking of TRS thus leads to a *weak* FSOTSC phase as each corner is occupied by two MCMs.

### 2. Case II: $B_x \neq 0$

Here we investigate the solutions for the MCMs in the presence of $B_x$. To begin with, we assume $B_x > M_{\text{II}}$. We proceed as before and obtain the following solutions for edge-I and II as
$$
\Psi_C \sim \alpha_{\text{I}} e^{-\frac{M_{\text{I}}}{\lambda_y} y} \Phi_C^{\text{I,1}} + \beta_{\text{I}} e^{-\frac{M_{\text{I}}}{\lambda_y} y} \Phi_C^{\text{I,2}} \quad : \text{edge-I},
$$

$$
\Psi_C \sim \alpha_{\text{II}} e^{-\frac{B_x-M_{\text{II}}}{\lambda_x} x} \Phi_C^{\text{II,1}} + \beta_{\text{II}} e^{-\frac{B_x+M_{\text{II}}}{\lambda_x} x} \Phi_C^{\text{II,2}} : \text{edge-II}, \ (25)
$$
where $\Phi_C^{\text{I,1}} = (1,1,i,-i)^{\tilde{T}}$, $\Phi_C^{\text{I,2}} = (1,-1,-i,-i)^{\tilde{T}}$, $\Phi_C^{\text{II,1}} = (1,-1,i,i)^{\tilde{T}}$, and $\Phi_C^{\text{II,2}} = (1,1,i,-i)^{\tilde{T}}$. Upon matching $\Psi_C$ at the boundary, we obtain $\alpha_{\text{I}} = \beta_{\text{II}} = \alpha$ and $\beta_{\text{I}} = \alpha_{\text{II}} = 0$. The final solution becomes
$$
\Psi_C \sim \alpha e^{-\frac{M_{\text{I}}}{\lambda_y} y} \Phi_C^{\text{I,1}} \quad : \text{edge-I},
$$

$$
\Psi_C \sim \alpha e^{-\frac{B_x+M_{\text{II}}}{\lambda_x} x} \Phi_C^{\text{I,1}} \quad : \text{edge-II}. \ (26)
$$

In this case, the localization lengths are given by $\lambda_x/(B_x + M_{\text{II}})$ ($\lambda_y/M_{\text{I}}$) along the $x$ ($y$) direction. Thus the MCMs decay differently along the two directions into the bulk. This is also evident from the Floquet LDOS where localization of MZMs at the corners are stronger in the $y$ direction as compared to the $x$ direction [see Fig. 2(b)]. Moreover, there exists one MCM per corner, as shown in the inset of Fig. 2(b). The presence of one MCM suggests that it corresponds to a *strong* FSOTSC phase when $B_x \neq 0$. This phase cannot be realized in the presence of only a periodic kick drive, i.e., when TRS is broken dynamically.

Furthermore, when $B_x < M_{\text{II}}$, we continue to obtain two MZMs per corner like the previous case with $B_x = 0$, except for the modification in localization length that is modulated by $B_x$. The final solution for this case reads
$$
\Psi_C \sim \alpha e^{-\frac{M_{\text{I}}}{\lambda_y} y} \Phi_C^{\text{I,1}} + \beta e^{-\frac{M_{\text{I}}}{\lambda_y} y} \Phi_C^{\text{I,2}} \quad : \text{edge-I},
$$

$$
\Psi_C \sim \alpha e^{-\frac{B_x+M_{\text{II}}}{\lambda_x} x} \Phi_C^{\text{I,1}} + \beta e^{-\frac{M_{\text{II}}-B_x}{\lambda_x} x} \Phi_C^{\text{I,2}} \quad : \text{edge-II}. \ (27)
$$

Therefore, the incorporation of Zeeman field allows one to explore both the *weak* and *strong* phases depending on the values of $B_x$.

### E. Topological characterization of MCMs

Having understood the wave functions associated with the MCMs, we would now like to characterize these FSOTSC phases with appropriate topological invariants. We compute two invariants, namely FWS and FQM, to identify the underlying topological nature of these MCMs. For the calculation

![](./images/817398481818746881_4.jpg)

FIG. 3. (a) Floquet Wannier spectrum (FWS) is demonstrated for $B_x = 0$ and the inset manifests the same for $B_x = 0.3$. The values of all other parameters remain the same as in Fig. 2. Connecting with Fig. 2, we can comment that eight (four) MCMs correspond to four (two) FWS quantized at 0.5. We refer the phase with eight and four MCMs as *weak* and *strong* FSOTSC phases, respectively. (b) Floquet quadrupole moment (FQM), which is only quantized at 0.5 for the *strong* FSOTSC phase, is demonstrated in the $m_1$-$\omega$ plane where $m_1$ and $\omega$ are the amplitude of the drive and the driving frequency, respectively.

of FWS, we construct the Wilson loop operator [14] as
$$
\mathcal{W}_x = F_{x,k_x+(N_x-1)\Delta k_x} \cdots F_{x,k_x+\Delta k_x} F_{x,k_x}, \ (28)
$$
with $[F_{x,k_x}]_{mn} = \langle \phi_{n,k_x+\Delta k_x} | \phi_{m,k_x} \rangle$, where $\Delta k_x = 2\pi/N_x$ [$N_x$ being the number of discrete points considered inside the Brillouin zone (BZ) along $k_x$] and $|\phi_{m,k_x}\rangle$ is the $m$th occupied Floquet quasistate in the semi-infinite geometry (considering periodic boundary condition (PBC) and open boundary condition (OBC) along the $x$ and $y$ direction, respectively). One can obtain $|\phi_{m,k_x}\rangle$ by diagonalizing the effective Floquet Hamiltonian in the high-frequency limit [Eq. (6)]. Thus we obtain the Wannier Hamiltonian as
$$
\mathcal{H}_{\mathcal{W}_x}^{\text{Flq}} = -i \ln \mathcal{W}_x, \ (29)
$$
whose eigenvalues $2\pi \nu_x^{\text{Flq}}$ correspond to the FWS. Similarly, one can find $\nu_y^{\text{Flq}}$ by considering PBC (OBC) along the $y$ ($x$) direction.

The quantized nature of Wannier spectra at 0.5 characterizes the SOTSC phase in our case. In the FSOTSC phase, one expects to obtain a quantized value pinned at 0.5 similar to the static counterpart. In the first case for $B_x = 0$, we obtain four eigenvalues at 0.5 as shown in Fig. 3(a), whereas for $B_x \neq 0$, one obtains such two eigenvalues only by diagonalizing $\mathcal{H}_{\mathcal{W}_x}^{\text{Flq}}$ [see the inset of Fig. 3(a)]. One can thus identify the FSOTSC phase, hosting two MCMs per corner in the absence of the Zeeman field ($B_x = 0$), as the *weak* phase where there exist two pairs of FWS quantized at 0.5. On the other hand, in the presence of the Zeeman field ($B_x \neq 0$), the FSOTSC phase becomes a *strong* one where a single MZM is localized per corner, leading to a single pair of FWS quantized at 0.5. Therefore, one can directly correlate the wave function of MZMs at the corner with the topological signature of the invariant FWS. In this way, we can distinguish between the *strong* and *weak* FSOTSC phases that are, respectively, associated with two and four FWS eigenvalues stabilized at 0.5.

In order to calculate the FQM, being another invariant for the quantification of the topological phases,

we numerically diagonalize the exact Floquet operator [Eq. (3)]. We then construct the Floquet many-body ground state $\Psi_{0,\text{F}}$ by columnwise marshalling the quasis- tates according to their quasienergy $-\omega/2 \leqslant \mu_m \leqslant 0$: $\Psi_{0,\text{F}} = \sum_{m \in \mu_m \leqslant 0} |\phi_m \rangle \langle \phi_m|$ [56,62]. Now $Q_{xy}^{\text{Flq}}(r)$ can be defined, con- sidering the geometrical number operator $\hat{q}_{xy} = \hat{n}(r)xy/L^2$ with $\hat{n}(r)$ being the number operator at $r = (x,y)$, as follows

$$
Q_{xy}^{\text{Flq}} = \operatorname{Re}\left[-\frac{i}{2\pi}\operatorname{Tr}\left(\ln\left(\Psi_{0,\text{F}}^{\dagger}\exp\left[2\pi i \sum_{r} \hat{q}_{xy}(r)\right]\Psi_{0,\text{F}}\right)\right)\right].
\tag{30}
$$

For $B_x \neq 0$, we obtain $Q_{xy}^{\text{Flq}} \equiv \text{mod}(Q_{xy}^{\text{Flq}},1)=0.5$. On the other hand, when $B_x=0$, $Q_{xy}^{\text{Flq}}$ turns out to be zero, depicting weak topological nature of the phase. Therefore, similar to the FWS, we here also find finite (vanishing) FQM for strong (weak) FSOTSC phases. We then explore the dynamic FSOTSC phase for a range of the driving frequency $\omega$ and the driving amplitude $m_1$ where $Q_{xy}^{\text{Flq}}=0.5$. This is shown in Fig. 3(b). This clearly suggests that the emergent strong phase is indeed an outcome of nonequilibrium dynamics as the underlying static model remains in a nontopological phase.

## III. MAJORANA HINGE MODES IN 3d

In this section we generalize our earlier findings of FSOTSC phase in the case of 3D.

### A. Model Hamiltonian and driving protocol
#### 1. Model

In 3D, we begin by writing down the Hamiltonian in the Bogoliubov-de Gennes (BdG) form as $H_{\text{BdG}} = \sum_{\mathbf{k}} \Psi_{\mathbf{k}}^{\dagger} \mathcal{H}_0^{3\text{D}}(\mathbf{k}) \Psi_{\mathbf{k}}$, with $\Psi_{\mathbf{k}} = (c_{\mathbf{k},a\uparrow}, -c_{-\mathbf{k},a\downarrow}^{\dagger}, c_{\mathbf{k},a\downarrow}, c_{-\mathbf{k},a\uparrow}^{\dagger}, c_{\mathbf{k},b\uparrow}, -c_{-\mathbf{k},b\downarrow}^{\dagger}, c_{\mathbf{k},b\downarrow}, c_{-\mathbf{k},b\uparrow}^{\dagger})^{\tilde{T}}$, and $\mathcal{H}_0^{3\text{D}}(\mathbf{k})$ is given by

$$
\begin{aligned}
\mathcal{H}_0^{3\text{D}} &= \boldsymbol{\epsilon}(\mathbf{k}) \Gamma_1 + \lambda_x \sin k_x \Gamma_2 + \lambda_y \sin k_y \Gamma_3 + \lambda_z \sin k_z \Gamma_4 \\
&\quad + \Delta(\mathbf{k}) \Gamma_5 + B_x \Gamma_6 + B_y \Gamma_7 + B_z \Gamma_8 \equiv \mathbf{N}(\mathbf{k}) \cdot \boldsymbol{\Gamma},
\tag{31}
\end{aligned}
$$

where $\boldsymbol{\epsilon}(\mathbf{k}) = (m_0 - t_x \cos k_x - t_y \cos k_y - t_z \cos k_z)$, $\Delta(\mathbf{k}) = \Delta(\cos k_x - \cos k_y)$ and $\Gamma_1 = \sigma_z \tau_z$, $\Gamma_2 = \sigma_x s_x \tau_z$, $\Gamma_3 = \sigma_x s_y \tau_z$, $\Gamma_4 = \sigma_x s_z \tau_z$, $\Gamma_5 = \tau_x$, $\Gamma_6 = s_x$, $\Gamma_7 = s_y$, and $\Gamma_8 = s_z$. Similar to the Hamiltonian [Eq. (1)] in the 2D case, $\mathcal{H}_0^{3\text{D}}$ respects both TRS $\mathcal{T} = i s_y \mathcal{K}$ and PHS $\mathcal{C} = s_y \tau_y \mathcal{K}$ in the absence of Zeeman field, i.e., $B_x = B_y = B_z = 0$. In the absence of the superconducting term $\Delta(\mathbf{k})=0$, the model supports zero- energy surface states for $|m_0| < t_x + t_y + t_z$. While for $|m_0| > t_x + t_y + t_z$, the models becomes nontopological (trivial band insulator). This model thus supports the first order topological phase in the absence of $\Delta(\mathbf{k})$. Interestingly, the model becomes a PHS protected SOTSC, hosting MKPs at the hinges along the $z$ direction, in the presence of $\Delta(\mathbf{k})$ when $|m_0| < t_x + t_y + t_z$. In the case of the 2D system [Eq. (1)], the SOTSC phase supports MCMs; here for the 3D system [Eq. (31)], it hosts Majorana hinge modes (MHMs). Upon breaking TRS by introducing magnetic field $B_x \neq 0$, the degeneracy of MKPs gets lifted and there exists only one MZM per hinge. We note that $B_y$ does the same job as done by $B_x$. In contrast, $B_z$ is not able to lift the degeneracy of MKPs. In general, the MHMs are observed along the $c$ direction when the SC order has the form $\Delta(\mathbf{k}) = \cos k_a - \cos k_b$ with $a,b,c=x,y,z$. The MKPs along the hinges in the $c$ direction remain unaffected by the magnetic field $B_c$. On the other hand, for $|m_0| > t_x + t_y + t_z$, the system continues to remain in the nontopological phases even with $\Delta(\mathbf{k}) \neq 0$ and $B_x \neq 0$. Therefore, it would be interesting to study the generation of the FSOTSC phase in the presence of $\Delta$ by kicking the mass term while the underlying static system remains in a nontopological phase. Our aim is to generate the Floquet MHMs (FMHMs) and their topological characterization in 3D geometry.

### 2. Driving protocol and Floquet operator

We consider the same driving protocol in the form of periodic kick as followed in the 2D case where

$$
m(t) = m_1 \sum_{r=1}^{\infty} \delta(t - rT).
\tag{32}
$$

Here, $T$ is the period of the drive and $m_1$ is the amplitude of the drive. With the periodic kick [see Eq. (32)], the Floquet operator reads

$$
\begin{aligned}
U(T) &= \mathbf{TO} \exp\left[-i \int_0^T dt \left(\mathcal{H}_0^{3\text{D}}(\mathbf{k}) + m(t)\Gamma_1\right)\right] \\
&= \exp(-i \mathcal{H}_0^{3\text{D}}(\mathbf{k})T) \exp(-i m_1 \Gamma_1).
\tag{33}
\end{aligned}
$$

We can cast the Floquet operator $U(T)$ in a more compact form as

$$
U(T) = C_T (p - i q \Gamma_1) - i S_T \sum_{j=1}^8 \left(n_j \Gamma_j + m_j \Gamma_{j1}\right), \quad (34)
$$

where $C_T = \cos(|\mathbf{N}(\mathbf{k})|T)$, $S_T = \sin(|\mathbf{N}(\mathbf{k})|T)$, $p = \cos m_1$, $q = \sin m_1$, $n_j = \frac{N_j(\mathbf{k})\cos m_1}{|\mathbf{N}(\mathbf{k})|}$, $m_j = \frac{N_j(\mathbf{k})\sin m_1}{|\mathbf{N}(\mathbf{k})|}$, and $\Gamma_{j1} = \frac{1}{2i}[\Gamma_j,\Gamma_1]$ with $j=2,3,4,5,6,7,8$. One can find the general form of the effective Hamiltonian as

$$
H_{\text{Flq}} = \frac{\xi_{\mathbf{k}}}{\sin \xi_{\mathbf{k}} T} \left[ \sin(|\mathbf{N}(\mathbf{k})|T) \cos m_1 \sum_{j=1}^8 r_j \Gamma_j + \cos(|\mathbf{N}(\mathbf{k})|T) \sin m_1 \Gamma_1 + \sin(|\mathbf{N}(\mathbf{k})|T) \sin m_1 \sum_{j=2}^8 r_j \Gamma_{j1} \right],
\tag{35}
$$

with $\xi_{\mathbf{k}} = \frac{1}{T} \cos^{-1} \left[ \cos(|\mathbf{N}(\mathbf{k})|T) \cos m_1 \right]$, $r_j = \frac{N_j(\mathbf{k})}{|\mathbf{N}(\mathbf{k})|}$. In the high-frequency limit, i.e., $T \to 0$ and $m_1 \to 0$, neglecting the higher order terms in $T$ and $m_1$, we find the effective Hamiltonian as

$$
H_{\text{Flq}} \approx \mathcal{H}_0(\mathbf{k}) + \frac{m_1}{T} \Gamma_1 + m_1 \sum_{j=2}^8 r_j \Gamma_{j1}.
\tag{36}
$$


![](./images/817398481818746881_5.jpg)

FIG. 4. (a) The LDOS associated with the MZMs clearly exhibits the emergence of the 1D Floquet MHMs in finite geometry. The LDOS structure remains qualitatively invariant in the presence of an in-plane Zeeman field. We choose the other parameter values as $t_x = t_y = t_z = 2.0$, $\lambda_x = \lambda_y = \lambda_z = 1.0$, $m_0 = 5.5$, $m_1 = -0.3$, and $T = 0.393$. (b) The Floquet quasienergy spectra is shown for the 3D FSOTSC in real space without the Zeeman field. There exist eight MHMs (due to the finite size effect, these modes do not appear exactly at zero energy) referring to the fact that this is a weak phase where each hinge is occupied by two MZMs. The finite-size effect is investigated in the inset I1 showing the gap as an exponentially falling function of the system size in one real space direction as $\Delta_G \sim \beta \exp(-\alpha L)$ with $\alpha = 0.127283$ and $\beta = 0.769069$. With Zeeman field $B_x = 0.4$, we depict (inset I2) the emergence of four MHMs, i.e., one MZM per hinge. The Zeeman field can thus transform a weak FSOTSC to a strong FSOTSC phase.

In Eq. (36), terms associated with $\Gamma_{j1}$ are the new terms generated by the drive. Note that these new terms break TRS $\mathcal{T}$ present in the static Hamiltonian, although $H_{\text{Flq}}$ continues to preserve the antiunitary PHS $\mathcal{C}$. Similar to the 2D case as described by Eq. (6), here also the extra terms $r_j\Gamma_{j1}$ break the TRS of the model even when $B_x = B_y = B_z = 0$. The Hamiltonian [Eq. (36)] shares similar characteristics as shown by the 2D Hamiltonian [Eq. (6)]. Here also the mass term is renormalized to $m_0 \to (m_0 + m_1/T)$ and the topological phase boundary becomes accordingly modified. The dynamical (explicit) breaking of TRS would lead to an interesting study as far as the weak (strong) FSOTSC phases are concerned. As noted in the static case, the in-plane Zeeman field $B_x$ or $B_y$ can lead to an interesting effect for the Floquet case also.

## B. Floquet Majorana hinge mode

Here, we numerically diagonalize the Floquet operator [Eq. (33)] in real space geometry to manifest the signature of the 1D propagating MHMs along the $z$ direction in the LDOS spectrum. Like before, we consider two cases. When the Zeeman field $\mathbf{B} = 0$, we obtain eight eigenvalues close to zero energy like the 2D case as shown in Fig. 4(b). However, when we incorporate $B_x \neq 0$ or $B_y \neq 0$, we obtain four modes near zero energy [see Fig. 4(b)I2]. Interestingly, the transverse magnetic field $B_z$ does not give rise to these kinds of phenomena. However, the finite-size effect is very prominent here that we depict in the inset I1 of Fig. 4(b). The finite-size gap $\Delta_G$ vanishes exponentially with $L$: $\Delta_G \sim \beta \exp(-\alpha L)$. This ensures the fact that MHMs are indeed zero-energy FSOTSC states in 3D. We show the LDOS explicitly in Fig. 4(a) where one can observe that a finite spectral weight is uniformly distributed over the four hinges of the 3D cubic system.

## C. Low energy surface theory

We here investigate the low-energy theory for the 3D case to search for the existence of the hinge states, originated due to the periodically kicked mass term, in the underlying static Hamiltonian [Eq. (31)]. For simplicity we choose $t_x = t_y = t_z = t$ and $\lambda_x = \lambda_y = \lambda_z = \lambda$. We expand the high-frequency effective Hamiltonian [Eq. (36)] around the $\Gamma = (0,0,0)$ point and obtain

$$
\begin{aligned}
H_{\text{Flq},\Gamma}^{3\text{D}} =& \left(m' + \frac{t}{2}\partial_x^2 + \frac{t}{2}\partial_y^2 + \frac{t}{2}\partial_z^2\right)\Gamma_1 + \lambda k_x\Gamma_2 \\
&+ \lambda k_y\Gamma_3 + \lambda k_z\Gamma_4 - \frac{\Delta}{2}(k_x^2 - k_y^2)\Gamma_5 + \frac{m_1}{T}\Gamma_1 \\
&+ m_1\lambda k_x\Gamma_{21} + m_1\lambda k_y\Gamma_{31} + m_1\lambda k_z\Gamma_{41} \\
&- \frac{m_1\Delta}{2}(k_x^2 - k_y^2)\Gamma_{51} + B_x\Gamma_6 + B_y\Gamma_7 + B_z\Gamma_8,
\end{aligned}
\tag{37}
$$

where $m' = (m_0 - 3t)$ and $\Gamma_{21} = -\sigma_y s_x$, $\Gamma_{31} = -\sigma_y s_y$, $\Gamma_{41} = -\sigma_y s_z$, and $\Gamma_{51} = -\sigma_z \tau_y$. We choose a surface perpendicular to the $xy$ plane, with a deviation from the $yz$ plane by an angle $\theta$. In order to cast the above equations in a convenient form we translate to a rotated frame defined by $k_1 = -\sin\theta\ k_x + \cos\theta\ k_y$, $k_2 = k_z$, and $k_3 = \cos\theta\ k_x + \sin\theta\ k_y$. This rotation transforms $x,y,z \to y,z,x$ for $\theta = 0$ while for $\theta = \pi/2$, $x,y,z \to -x,z,y$. We now consider OBC in the $x_3$ direction and replace $k_3 \to -i\partial_3$. One can hence divide Eq. (37) into two parts as

$$
\begin{aligned}
H_0 =& \left(m - \frac{t}{2}\partial_3^2\right)\sigma_z \tau_z - i\lambda \partial_3\ \sigma_x(s_x \cos\theta + s_y \sin\theta)\tau_z, \\
H_p =& \lambda k_1\sigma_x(-s_x \sin\theta + s_y \cos\theta)\tau_z + \lambda k_2\sigma_x s_z \tau_z \\
&- \frac{\Delta(\theta)}{2}\partial_3^2\ \tau_x + i m_1 \lambda \partial_3 \sigma_y(s_x \cos\theta + s_y \sin\theta) \\
&- m_1 \lambda k_1 \sigma_y(-s_x \sin\theta + s_y \cos\theta) - m_1 \lambda k_2 \sigma_y s_z \\
&+ \frac{m_1 \Delta(\theta)}{2}\partial_3^2\ \sigma_z \tau_y + B_x s_x + B_y s_y + B_z s_z,
\end{aligned}
\tag{38}
$$

where $m = (m' + \frac{m_1}{T})$ and $\Delta(\theta) = \Delta(\sin^2\theta - \cos^2\theta)$. We consider the following transformation for spins

$$
\begin{pmatrix}
s_x \\
s_y \\
s_z
\end{pmatrix}
=
\begin{pmatrix}
-\sin\theta & \cos\theta & 0 \\
\cos\theta & \sin\theta & 0 \\
0 & 0 & 1
\end{pmatrix}
\begin{pmatrix}
s_1 \\
s_3 \\
s_2
\end{pmatrix}
\tag{39}
$$

such that Eq. (38) acquires a compact form as we notice for the 2D case. Here, $s_1$, $s_2$, and $s_3$ are Pauli matrices. Therefore, Eq. (38) can be rewritten as

$$
\begin{aligned}
H_0 =& \left(m - \frac{t}{2}\partial_3^2\right)\sigma_z \tau_z - i\lambda \partial_3\ \sigma_x s_3 \tau_z, \\
H_p =& \lambda k_1 \sigma_x s_1 \tau_z + \lambda k_2 \sigma_x s_2 \tau_z - \frac{\Delta(\theta)}{2}\partial_3^2\ \tau_x + i m_1 \lambda \partial_3 \sigma_y s_3 \\
&- m_1 \lambda k_1 \sigma_y s_1 - m_1 \lambda k_2 \sigma_y s_2 + \frac{m_1 \Delta(\theta)}{2}\partial_3^2\ \sigma_z \tau_y \\
&+ B_x(-s_1 \sin\theta + s_3 \cos\theta) + B_y(s_1 \cos\theta + s_3 \sin\theta) \\
&+ B_z s_2.
\end{aligned}
\tag{40}
$$

We assume $\Psi$ to be the zero-energy solution of $H_0$ with the boundary condition $\Psi(x_3 = 0) = \Psi(x_3 = \infty) = 0$. We finally

obtain the following wave function in the rotated frame as
$$
\Psi_{\alpha}=A e^{-\mathcal{K}_{1} x_{3}} \sin \left(\mathcal{K}_{2} x_{3}\right) e^{i k_{1} x_{1}+i k_{2} x_{2}} \Phi_{\alpha}, \quad(41)
$$
where $\mathcal{K}_{1}=\frac{\lambda}{t}, \mathcal{K}_{2}=\sqrt{\left|\frac{2 m}{t}\right|-\mathcal{K}_{1}^{2}}$, and $A=\frac{4 \mathcal{K}_{1}\left(\mathcal{K}_{1}^{2}+\mathcal{K}_{2}^{2}\right)}{\mathcal{K}_{2}^{2}}$ and $\Phi_{\alpha}$ is the eight-component spinor satisfying $\sigma_{y} s_{3} \Phi_{\alpha}=-\Phi_{\alpha}$.
$$
\begin{aligned}
& \Phi_{1}=\left|\sigma_{y}=+1\right\rangle \otimes\left|s_{3}=-1\right\rangle \otimes\left|\tau_{z}=+1\right\rangle, \\
& \Phi_{2}=\left|\sigma_{y}=-1\right\rangle \otimes\left|s_{3}=+1\right\rangle \otimes\left|\tau_{z}=+1\right\rangle, \\
& \Phi_{3}=\left|\sigma_{y}=+1\right\rangle \otimes\left|s_{3}=-1\right\rangle \otimes\left|\tau_{z}=-1\right\rangle, \\
& \Phi_{4}=\left|\sigma_{y}=-1\right\rangle \otimes\left|s_{3}=+1\right\rangle \otimes\left|\tau_{z}=-1\right\rangle. \quad(42)
\end{aligned}
$$

The matrix element of $H_{p}$ in the rotated frame within the above basis reads
$$
H_{\alpha \beta}^{\text {Surf }}=\int_{0}^{\infty} d x_{3} \Psi_{\alpha}^{\dagger}\left(x_{3}\right) H_{p} \Psi_{\beta}\left(x_{3}\right). \quad(43)
$$

Therefore, we obtain the Hamiltonian for the surface in the rotated frame to be
$$
H^{\text {Surf }}=\lambda k_{1} s_{3} \tau_{y}-\lambda k_{2} s_{3} \tau_{x}+M(\theta) s_{1}-B(\theta) \tau_{z}. \quad(44)
$$

Here, $M(\theta)=\Delta(\theta)\left|\frac{m}{t}\right|$ and $B(\theta)=\left(B_{x} \cos \theta+B_{y} \sin \theta\right)$. The transverse magnetic field $B_{z}$ does not appear in the surface Hamiltonian referring to the fact that the in-plane magnetic field plays an important role in determining the nature of the FSOTSC phase. Interestingly, $\Delta(\theta)=-\Delta(\theta+\pi / 2)$ resulting in $M(\theta)$ to change its sign between two adjacent surfaces under $C_{4}$ rotation around the $z$ axis. Consequently, one can get hinge mode in the junction between the $x z$ and $y z$ plane. This sign change of the mass term is shown in Fig. 4(a). We can explicitly write down the surface Hamiltonian for the $y z$ ($x z$) surface by putting $\theta=0\left(\frac{\pi}{2}\right)$ as
$$
\begin{aligned}
& H^{y z}=\lambda k_{y} s_{3} \tau_{y}-\lambda k_{z} s_{3} \tau_{x}-\Delta\left|\frac{m}{t}\right| s_{1}-B_{x} \tau_{z}, \\
& H^{x z}=-\lambda k_{x} s_{3} \tau_{y}-\lambda k_{z} s_{3} \tau_{x}+\Delta\left|\frac{m}{t}\right| s_{1}-B_{y} \tau_{z}. \quad(45)
\end{aligned}
$$

Let us now discuss the above surface Hamiltonian at length. As compared to the edge Hamiltonian for edge $a$ with $k_{a}$ only, the surface Hamiltonian for the $a b$ surface consists of $k_{a}$ and $k_{b}$. In the absence of magnetic field, $\Delta\left|\frac{m}{t}\right| s_{1}$ acts as a mass in the Nambu space spanned by $s_{3} \tau_{x, y}$. This mass changes its sign between two adjacent surfaces, namely $y z$ and $x z$. Both the blocks participate actively here as the mass term uniformly appears in both of them. Thus two MZMs per hinge are observed. On the other hand, in the presence of any of the in-plane Zeeman field, mass terms become different in the two blocks. This leads to a situation where one block can be made active keeping the other block inactive. As a result, one MZM per hinge can be observed. This behavior again resembles that of the 2D case. Therefore, the dynamical and explicit breaking of TRS imprints their signatures unanimously for 3D as well.

### D. Hinge mode solution

Having obtained the low energy surface Hamiltonian, the hinge Hamiltonian can be estimated by considering the PBC (OBC) along (perpendicular to) the hinge direction. We thus divide $H^{\text {Surf }}$ into two parts as
$$
\begin{aligned}
& H_{0}^{S}=-i \lambda \partial_{1} s_{3} \tau_{y}+M(\theta) s_{1}-B(\theta) \tau_{z}, \\
& H_{p}^{S}=-\lambda k_{2} s_{3} \tau_{x}. \quad(46)
\end{aligned}
$$

Here the superconducting order parameter and Zeeman field are treated in the unperturbed Hamiltonian $H_{0}^{S}$. We solve $H_{0}^{S}$ exactly and expand $H_{p}^{S}$ in the basis of $H_{0}^{S}$. For $\mathbf{B}=0$, we obtain the Hamiltonian for the hinge mode (after replacing $k_{2} \rightarrow k_{z}$ ) as
$$
H^{\text {Hinge }}=-\lambda k_{z} \tau_{y}. \quad(47)
$$

This manifests a propagating mode along the $z$ direction. Therefore, it is clear that dynamical breaking of TRS leads to two solutions of MHMs with $\tau_{y}= \pm 1$. Contrastingly for $B_{x} \neq 0$ or $B_{y} \neq 0$, we obtain the solution as
$$
H^{\text {Hinge }}=-\lambda k_{z} \mathbb{I}, \quad(48)
$$
which only hosts a single MHM as the hinge Hamiltonian is described by $\mathbb{I}$. Similar to the 2D case, here also the explicit breaking of TRS can lead to a situation different from the dynamical breaking of TRS by the periodic kick drive. Hence, one expects that without (with) magnetic field there exist two MHMs (one MHM) per hinge along the $z$ direction as shown in the inset I2 of Fig. 4(b).

### E. Floquet Wannier spectrum

To calculate FWS using Eq. (28), we write down the Hamiltonian [Eq. (31)] in slab geometry, i.e., we consider OBC in one direction while the other two directions continue to satisfy PBC. For an $x$-directed slab (OBC along the $x$ direction; PBC along the $y$ and $z$ direction), we can calculate $\nu_{z}^{(x), \text { Flq }}$ $\left(\nu_{y}^{(x), \text { Flq }}\right)$ as a function of $k_{y}\left(k_{z}\right)$. Since we obtain propagating 1D hinge mode in the $z$ direction only, the spectrum of $\nu_{y}^{(x), \text { Flq }}$ and $\nu_{x}^{(y), \text { Flq }}$ as a function of $k_{z}$ exhibits gapless nature, while all other FWS remain gapped. We illustrate the representative plots for FWS in Figs. 5(a) and 5(b). Focussing only at the $k_{z}=0$ point, we show FWS as a function of the state index at $k_{z}=0$ in Figs. 5(c) and 5(d). In the absence of the in-plane Zeeman field, i.e., for *weak* FSOTSC phase, we obtain four eigenvalues at 0.5 corresponding to the two MHMs per hinge [see Fig. 5(c)]. In contrast, when we turn on the in-plane Zeeman field $B_{x}$, i.e., for *strong* FSOTSC, we obtain two eigenvalues at 0.5 [see Fig. 5(d)] corroborating one MHM per hinge. We also calculate the FQM to further distinguish between the *weak* and *strong* FSOTSC. To proceed, we write the Floquet operator $U(T)$ [Eq. (33)] in rod geometry (considering PBC along the $z$ direction, OBC along the $x$ and $y$ direction). We then implement Eq. (30) to calculate the FQM $\left(Q_{x y}^{\text {Flq }}\right)$ as a function of $k_{z}$. We find that $Q_{x y}^{\text {Flq }}=0.5$ (0) at $k_{z}=0$ for the *strong* (*weak*) phase [87].

## IV. ROBUSTNESS OF HIGHER ORDER MAJORANA MODES AGAINST DISORDER

Having investigated the topological classification of the FSOTSC phases, we now focus on the robustness of these phases in the presence of finite disorder. We first concentrate on the 2D case. Instead of choosing $m_{1}$ to be constant, we consider $m_{1}$ to be randomly distributed in between $\left[-\frac{W}{2}, \frac{W}{2}\right]$ in an uncorrelated manner. Here, $W$ is the strength of the disorder. Note that, the disorder being random, we have taken the average over 500 disorder configurations in our numerical

![](./images/817398481818746881_6.jpg)

FIG. 5. (a) We depict the FWS $\nu_{z}^{(x),\text{Flq}}$ as a function of $k_{y}$ in the slab geometry with OBC along the $x$ direction and PBC along the $y,z$ directions. (b) We work in the same geometry as mentioned in panel (a) but show $\nu_{y}^{(x),\text{Flq}}$ as a function of $k_{z}$. Since the hinge mode propagates along the $z$ direction, we obtain gapless FWS for $\nu_{y}^{(x),\text{Flq}}$. (c) We show the FWS $\nu_{y}^{(x),\text{Flq}}$ as a function of state number at $k_{z}=0$ for $B_{x}=0$. In the inset one can clearly observe four eigenvalues at 0.5 refer to the weak FSOTSC phase. (d) We repeat (c) but with the in-plane Zeeman field $B_{x}\neq0$. We obtain two eigenvalues at 0.5 as shown in the inset refer to strong FSOTSC phase. The values of all the parameters remain the same as in Fig. 4.

calculation. We analyze our results for two values of disorder strengths, $W=0.1$ and 0.4, while hopping and spin-orbit coupling strength is fixed to unity. We first study the effect of disorder on the weak phase hosting eight MCMs. For weak disorder strength, $W=0.1$, one does not observe any perceptible difference from the clean case [see Fig. 6(a)]. To be precise, the spectral weight of MCMs is uniformly distributed among all four corners of the square lattice, i.e., the localization length remains almost unaltered in the presence of weak disorder, while for $W=0.4$, we notice that the spectral weight of some corner modes in LDOS becomes higher compared to others as shown in Fig. 6(b). This nonuniform distribution of spectral weight among the corners thus suggests that the strong disorder can substantially modify the localization properties of these MCMs. However, it is noteworthy that even strong disorder cannot lift the Majorana modes from the zero energy as depicted in the inset of Figs. 6(a) and 6(b). This results in the fact that FWS continues to exhibit similar behavior as compared to the clean case [see Figs. 7(a) and 7(b)]. Therefore, weak FSOTSC phase can preserve its signature in the presence of moderate disorder.

We also investigate the effect of moderate disorder in the strong FSOTSC phase hosting four MZMs at the corners in the presence of explicit TRS breaking Zeeman field. Since the disorder does not break any further symmetry (except translational), we find that the effect of the disorder remains the same as the earlier case with $B_{x}=0$. The uniform (nonuniform) distribution of spectral weight of MZMs is observed for $W=0.1$ (0.4) as depicted in Figs. 6(c) and 6(d). These MCMs are localized at zero energy always [see the inset of Figs. 6(c) and 6(d)]. As a result, their topological protection remains unaltered as noticed in the clean case. We find quantized FWS for weak as well as moderate disorder strength [see the inset of

![](./images/817398481818746881_7.jpg)

FIG. 6. (a) LDOS, associated with zero quasienergy states $\mu_{m}=0$, in finite geometry is demonstrated for $B_{x}=0$ and the inset shows the Floquet quasienergy spectrum for the same for the disorder strength $W=0.1$. (b) We repeat (a) with the disorder strength $W=0.4$. (c),(d) We repeat (a) and (b) with $B_{x}=0.3$, respectively. One can clearly observe that the localization properties become modified as the disorder strength increases substantially, otherwise for small disorder, they remain the same as the clean case. The value of all other parameters remains the same as in Fig. 2.

![](./images/817398481818746881_8.jpg)

FIG. 7. (a) FWS is depicted for the case $B_{x}=0$ when the disorder strength is chosen to be $W=0.1$, while the same for the case $B_{x}=0.3$ is shown in the inset. (b) FWS is demonstrated with the disorder strength $W=0.4$ for $B_{x}=0$ and $B_{x}\neq0$ (inset). One can obtain an indication that upon increasing the disorder strength substantially, the FWS might deviate from the quantized value 0.5. However, for our chosen disorder strength $(W<t_{x},t_{y},\lambda_{x},\lambda_{y})$ the invariant behaves in a robust manner referring to that these FSOTSC phases are stable against moderate disorder. The value of all the other parameters remains the same as chosen in Fig. 2.


Figs. 7(a) and 7(b)]. It is important to mention that the FQM is also quantized at a value 0.5, for such strength of the disorder with $B_x \neq 0$. This investigation with moderate disorder thus clearly suggests that both *weak* and *strong* FSOTSC phases are robust against moderate disorder. Having investigated the effect of disorder and protection of topological properties in 2D, we believe the same line of argument would also hold for 3D.

## V. SUMMARY AND CONCLUSIONS

To summarize, in this paper, we provide a dynamical prescription to generate the FSOTSC phase starting from a 2D/3D TI in close proximity to an unconventional $d$-wave superconductor. We periodically kick the mass term to generate MZMs at the corners and hinges in 2D square and 3D cubic lattice geometry, respectively. Our aim here is to investigate the effect of TRS breaking magnetic field on these Floquet SOTSC phases as the initial (effective) Hamiltonian, describing the static (driven) system which preserves (breaks) the dynamical TRS. In 2D, we first consider our model in the presence of periodically kicked mass term when Zeeman field $B_x = 0$. Here, we find the FSOTSC phase harboring eight MZMs, i.e., two MZMs per corner. In order to characterize this FSOTSC phase, we compute two topological invariants, namely FWS and FQM. We find that this phase corresponds to four FWS quantized at 0.5 while FQM vanishes; we identify this FSOTSC phase as the *weak* one. Upon introduction of an explicit TRS breaking Zeeman field $B_x \neq 0$, we find four MZMs, i.e., one MZM per corner. We here obtain two quantized FWS at 0.5 and quantized FQM referring to the *strong* nature of the phase. We analytically support our numerical findings, as obtained by diagonalizing the Floquet operator in OBC, with the help of effective low-energy edge theory and MCMs solutions. The low-energy theory can successfully predict the nature of the SOTSC phase whether it is *strong* or *weak* in terms of the spinor states of MZMs. We further introduce moderate disorder in the driving amplitude to study the stability of the FSOTSC phase against disorder. We find that the FSOTSC is stable against the moderate strength of disorder. However, the localization property of the MZMs depends on the disorder strength. We also generalize our theory based on the 3D model and identify the *weak* (*strong*) FSOTSC phase via FWS hosting MHMs. In this case, we derive the low energy surface theory and analytical solutions of the MHMs therein. The effect of the disorder remains similar to in the 2D case.

As far as experimental feasibility of our setup is concerned, $d$-wave superconductivity in TI can be induced via the proximity effect (e.g., $\text{Bi}_2\text{Sr}_2\text{CaCu}_2\text{O}_{8+\delta}$ [88] with an induced gap amplitude $\Delta \sim 15$ meV [88]. It has been theoretically [89] and experimentally [90] demonstrated that the topological properties of $(\text{Bi,Sb})_2\text{Te}_3$ thin films can be tuned by the quantum confinement, i.e., varying the number of quintuple layers. It is indeed possible to tune the mass term in the underlying static model which might pave the way to realize the dynamical manipulation of the mass term in the proximized topological superconductor. In recent times, experimental advancements on the pump-probe techniques [53,75,76] have enabled one to observe Floquet topological insulators [75] and anomalous Hall effect in graphene [91]. Therefore, we believe that the signature of MCMs and MHMs may be possible to achieve via pump-probe-based time-resolved transport [e.g., local scanning tunneling microscope (STM)] measurements [92–94] for an in-plane magnetic field $B_x \sim 7$–8 T, amplitude of the drive $m_1 \sim 100$ meV, and period $T \sim 2$ fs.

At last, we would like to comment on robustness of these Floquet MZMs in HOTSC phases under periodic driving as far as heating and dissipation are concerned. Based on the recent theoretical and experimental investigations on quantum many-body systems [95,96], the heating is suppressed in the prethermal window where our findings can be tested with dissipationless MZMs associated with the periodic steady state. We work in the high frequency regime away from the resonance points. This further enables us to minimize the heating effect [97]. We therefore believe that our theoretical findings do not suffer from heating issue and dissipation.

## ACKNOWLEDGMENTS

We acknowledge SAMKHYA: High-Performance Computing Facility provided by the Institute of Physics, Bhubaneswar, for our numerical computation. A.K.G. thanks Atanu Jana for useful technical discussions.

[1] A. Yu Kitaev, Unpaired majorana fermions in quantum wires, *Phys. Usp.* **44**, 131 (2001).

[2] X.-L. Qi and S.-C. Zhang, Topological insulators and superconductors, *Rev. Mod. Phys.* **83**, 1057 (2011).

[3] M. Z. Hasan and C. L. Kane, Colloquium: topological insulators, *Rev. Mod. Phys.* **82**, 3045 (2010).

[4] A. Das, Y. Ronen, Y. Most, Y. Oreg, M. Heiblum, and H. Shtrikman, Zero-bias peaks and splitting in an al–inas nanowire topological superconductor as a signature of majorana fermions, *Nat. Phys.* **8**, 887 (2012).

[5] M. T. Deng, S. Vaitiekenas, E. B. Hansen, J. Danon, M. Leijnse, K. Flensberg, J. Nygård, P. Krogstrup, and C. M. Marcus, Majorana bound state in a coupled quantum-dot hybrid-nanowire system, *Science* **354**, 1557 (2016).

[6] D. A. Ivanov, Non-Abelian Statistics of Half-Quantum Vortices in $p$-Wave Superconductors, *Phys. Rev. Lett.* **86**, 268 (2001).

[7] C. Nayak, S. H. Simon, A. Stern, M. Freedman, and S. Das Sarma, Non-abelian anyons and topological quantum computation, *Rev. Mod. Phys.* **80**, 1083 (2008).

[8] L. Fu and C. L. Kane, Superconducting Proximity Effect and Majorana Fermions at the Surface of a Topological Insulator, *Phys. Rev. Lett.* **100**, 096407 (2008).

[9] J. D. Sau, R. M. Lutchyn, S. Tewari, and S. Das Sarma, Generic New Platform for Topological Quantum Computation using Semiconductor Heterostructures, *Phys. Rev. Lett.* **104**, 040502 (2010).

[10] R. M. Lutchyn, J. D. Sau, and S. Das Sarma, Majorana Fermions and a Topological Phase Transition in

085413-11

Semiconductor-Superconductor Heterostructures, Phys. Rev. Lett. 105, 077001 (2010).

[11] X.-L. Qi, T. L. Hughes, and S.-C. Zhang, Chiral topological superconductor from the quantum hall state, Phys. Rev. B 82, 184516 (2010).

[12] Y. Oreg, G. Refael, and F. von Oppen, Helical Liquids and Majorana Bound States in Quantum Wires, Phys. Rev. Lett. 105, 177002 (2010).

[13] W. A. Benalcazar, B. A. Bernevig, and T. L. Hughes, Quantized electric multipole insulators, Science 357, 61 (2017).

[14] W. A. Benalcazar, B. A. Bernevig, and T. L. Hughes, Electric multipole moments, topological multipole moment pumping, and chiral hinge states in crystalline insulators, Phys. Rev. B 96, 245115 (2017).

[15] Z. Song, Z. Fang, and C. Fang, $(d-2)$-Dimensional Edge States of Rotation Symmetry Protected Topological States, Phys. Rev. Lett. 119, 246402 (2017).

[16] J. Langbehn, Y. Peng, L. Trifunovic, F. von Oppen, and P. W. Brouwer, Reflection-Symmetric Second-Order Topological Insulators and Superconductors, Phys. Rev. Lett. 119, 246401 (2017).

[17] F. Schindler, A. M. Cook, M. G. Vergniory, Z. Wang, S. S. P. Parkin, B. A. Bernevig, and T. Neupert, Higher-order topological insulators, Sci. Adv. 4, eaat0346 (2018).

[18] E. Khalaf, Higher-order topological insulators and superconductors protected by inversion symmetry, Phys. Rev. B 97, 205136 (2018).

[19] M. Geier, L. Trifunovic, M. Hoskam, and P. W. Brouwer, Second-order topological insulators and superconductors with an order-two crystalline symmetry, Phys. Rev. B 97, 205135 (2018).

[20] S. Franca, J. van den Brink, and I. C. Fulga, An anomalous higher-order topological insulator, Phys. Rev. B 98, 201114(R) (2018).

[21] X. Zhu, Tunable majorana corner states in a two-dimensional second-order topological superconductor induced by magnetic fields, Phys. Rev. B 97, 205134 (2018).

[22] T. Liu, J. J. He, and F. Nori, Majorana corner states in a two-dimensional magnetic topological insulator on a high-temperature superconductor, Phys. Rev. B 98, 245413 (2018).

[23] Z. Yan, F. Song, and Z. Wang, Majorana Corner Modes in a High-Temperature Platform, Phys. Rev. Lett. 121, 096803 (2018).

[24] Z. Wang, B. J. Wieder, J. Li, B. Yan, and B. A. Bernevig, Higher-Order Topology, Monopole Nodal Lines, and the Origin of Large Fermi Arcs in Transition Metal Dichalcogenides $xte_2$ ($x=$ Mo, W), Phys. Rev. Lett. 123, 186401 (2019).

[25] Y. Wang, M. Lin, and T. L. Hughes, Weak-pairing higher order topological superconductors, Phys. Rev. B 98, 165144 (2018).

[26] M. Ezawa, Higher-Order Topological Insulators and Semimetals on the Breathing Kagome and Pyrochlore Lattices, Phys. Rev. Lett. 120, 026801 (2018).

[27] D. Călugăru, V. Juričić, and B. Roy, Higher-order topological phases: A general principle of construction, Phys. Rev. B 99, 041301(R) (2019).

[28] L. Trifunovic and P. W. Brouwer, Higher-Order Bulk-Boundary Correspondence for Topological Crystalline Phases, Phys. Rev. X 9, 011012 (2019).

[29] C. Zeng, T. D. Stanescu, C. Zhang, V. W. Scarola, and S. Tewari, Majorana Corner Modes with Solitons in an Attractive Hubbard-Hofstadter Model of Cold Atom Optical Lattices, Phys. Rev. Lett. 123, 060402 (2019).

[30] Rui-Xing Zhang, W. S. Cole, and S. Das Sarma, Helical Hinge Majorana Modes in Iron-Based Superconductors, Phys. Rev. Lett. 122, 187001 (2019).

[31] Y. Volpez, D. Loss, and J. Klinovaja, Second-Order Topological Superconductivity in $\pi$-Junction Rashba Layers, Phys. Rev. Lett. 122, 126402 (2019).

[32] Z. Yan, Majorana corner and hinge modes in second-order topological insulator/superconductor heterostructures, Phys. Rev. B 100, 205406 (2019).

[33] S. A. A. Ghorashi, X. Hu, T. L. Hughes, and E. Rossi, Second-order dirac superconductors and magnetic field induced majorana hinge modes, Phys. Rev. B 100, 020509 (2019).

[34] S. A. A. Ghorashi, T. L. Hughes, and E. Rossi, Vortex and Surface Phase Transitions in Superconducting Higher-Order Topological Insulators, Phys. Rev. Lett. 125, 037001 (2020).

[35] S. J. De, U. Khanna, and S. Rao, Magnetic flux periodicity in second order topological superconductors, Phys. Rev. B 101, 125429 (2020).

[36] Y.-J. Wu, J. Hou, Y.-M. Li, X.-W. Luo, X. Shi, and C. Zhang, In-Plane Zeeman-Field-Induced Majorana Corner and Hinge Modes in an $s$-Wave Superconductor Heterostructure, Phys. Rev. Lett. 124, 227001 (2020).

[37] K. Laubscher, D. Chughtai, D. Loss, and J. Klinovaja, Kramers pairs of majorana corner states in a topological insulator bilayer, Phys. Rev. B 102, 195401 (2020).

[38] B. Roy, Higher-order topological superconductors in $\mathcal{P}$-, $\mathcal{T}$-odd quadrupolar dirac materials, Phys. Rev. B 101, 220506(R) (2020).

[39] S.-B. Zhang and B. Trauzettel, Detection of second-order topological superconductors by josephson junctions, Phys. Rev. Research 2, 012018(R) (2020).

[40] S.-B. Zhang, W. B. Rui, A. Calzona, S.-J. Choi, A. P. Schnyder, and B. Trauzettel, Topological and holonomic quantum computation based on second-order topological superconductors, Phys. Rev. Research 2, 043025 (2020).

[41] S.-B. Zhang, A. Calzona, and B. Trauzettel, All-electrically tunable networks of majorana bound states, Phys. Rev. B 102, 100503 (2020).

[42] M. Kheirkhah, Z. Yan, and F. Marsiglio, Vortex line topology in iron-based superconductors with and without second-order topology, arXiv:2007.10326.

[43] K. Plekhanov, N. Müller, Y. Volpez, D. M. Kennes, H. Schoeller, D. Loss, and J. Klinovaja, Quadrupole spin polarization as signature of second-order topological superconductors, Phys. Rev. B 103, L041401 (2021).

[44] H. Xue, Y. Yang, F. Gao, Y. Chong, and B. Zhang, Acoustic higher-order topological insulator on a kagome lattice, Nat. Mater. 18, 108 (2019).

[45] X.-D. Chen, W.-M. Deng, F.-L. Shi, F.-L. Zhao, M. Chen, and J.-W. Dong, Direct Observation of Corner States in Second-Order Topological Photonic Crystal Slabs, Phys. Rev. Lett. 122, 233902 (2019).

[46] B.-Y. Xie, G.-X. Su, H.-F. Wang, H. Su, X.-P. Shen, P. Zhan, M.-H. Lu, Z.-L. Wang, and Y.-F. Chen, Visualization of Higher-Order Topological Insulating Phases in Two-Dimensional Dielectric Photonic Crystals, Phys. Rev. Lett. 122, 233903 (2019).

085413-12

[47] S. Imhof, C. Berger, F. Bayer, J. Brehm, L. W. Molenkamp, T. Kiessling, F. Schindler, C. H. Lee, M. Greiter, T. Neupert, and R. Thomale, Topoelectrical-circuit realization of topological corner modes, *Nat. Phys.* **14**, 925 (2018).

[48] N. H. Lindner, G. Refael, and V. Galitski, Floquet topological insulator in semiconductor quantum wells, *Nat. Phys.* **7**, 490 (2011).

[49] B. Dóra, J. Cayssol, F. Simon, and R. Moessner, Optically Engineering the Topological Properties of a Spin Hall Insulator, *Phys. Rev. Lett.* **108**, 056602 (2012).

[50] M. S. Rudner, N. H. Lindner, E. Berg, and M. Levin, Anomalous Edge States and the Bulk-Edge Correspondence for Periodically Driven Two-Dimensional Systems, *Phys. Rev. X* **3**, 031005 (2013).

[51] M. Thakurathi, A. A. Patel, D. Sen, and A. Dutta, Floquet generation of majorana end modes and topological invariants, *Phys. Rev. B* **88**, 155133 (2013).

[52] M. C. Rechtsman, J. M. Zeuner, Y. Plotnik, Y. Lumer, D. Podolsky, F. Dreisow, S. Nolte, M. Segev, and A. Szameit, Photonic floquet topological insulators, *Nature (London)* **496**, 196 (2013).

[53] L. J. Maczewsky, J. M. Zeuner, S. Nolte, and A. Szameit, Observation of photonic anomalous floquet topological insulators, *Nat. Commun.* **8**, 13756 (2017).

[54] A. Eckardt, Colloquium: Atomic quantum gases in periodically driven optical lattices, *Rev. Mod. Phys.* **89**, 011004 (2017).

[55] R. W. Bomantara, L. Zhou, J. Pan, and J. Gong, Coupled-wire construction of static and floquet second-order topological insulators, *Phys. Rev. B* **99**, 045441 (2019).

[56] T. Nag, V. Juričić, and B. Roy, Out of equilibrium higher-order topological insulator: Floquet engineering and quench dynamics, *Phys. Rev. Research* **1**, 032045(R) (2019).

[57] Y. Peng and G. Refael, Floquet Second-Order Topological Insulators from Nonsymmorphic Space-Time Symmetries, *Phys. Rev. Lett.* **123**, 016806 (2019).

[58] R. Seshadri, A. Dutta, and D. Sen, Generating a second-order topological insulator with multiple corner states by periodic driving, *Phys. Rev. B* **100**, 115403 (2019).

[59] S. Chaudhary, A. Haim, Y. Peng, and G. Refael, Phonon-induced floquet second-order topological phases protected by space-time symmetries, *Phys. Rev. Research* **2**, 043431 (2020).

[60] M. Rodriguez-Vega, A. Kumar, and B. Seradjeh, Higher-order floquet topological phases with corner and bulk bound states, *Phys. Rev. B* **100**, 085138 (2019).

[61] K. Plekhanov, M. Thakurathi, D. Loss, and J. Klinovaja, Floquet second-order topological superconductor driven via ferromagnetic resonance, *Phys. Rev. Research* **1**, 032013(R) (2019).

[62] A. K. Ghosh, G. C. Paul, and A. Saha, Higher order topological insulator via periodic driving, *Phys. Rev. B* **101**, 235403 (2020).

[63] B. Huang and W. V. Liu, Floquet Higher-Order Topological Insulators with Anomalous Dynamical Polarization, *Phys. Rev. Lett.* **124**, 216601 (2020).

[64] H. Hu, B. Huang, E. Zhao, and W. V. Liu, Dynamical Singularities of Floquet Higher-Order Topological Insulators, *Phys. Rev. Lett.* **124**, 057001 (2020).

[65] R. W. Bomantara and J. Gong, Measurement-only quantum computation with floquet majorana corner modes, *Phys. Rev. B* **101**, 085401 (2020).

[66] Y. Peng, Floquet higher-order topological insulators and superconductors with space-time symmetries, *Phys. Rev. Research* **2**, 013124 (2020).

[67] T. Nag, V. Juričić, and B. Roy, Hierarchy of higher-order floquet topological phases in three dimensions, arXiv:2009.10719.

[68] A. Tiwari, A. Jahin, and Y. Wang, Chiral dirac superconductors: Second-order and boundary-obstructed topology, *Phys. Rev. Research* **2**, 043300 (2020).

[69] R. X. Zhang and Z. C. Yang, Tunable fragile topology in floquet systems, arXiv:2005.08970.

[70] A. K. Ghosh, T. Nag, and A. Saha, Floquet generation of second order topological superconductor, *Phys. Rev. B* **103**, 045424 (2021).

[71] R. V. Bhat and S. Bera, Out of equilibrium chiral higher order topological insulator on a $\pi$-flux square lattice, arXiv:2011.01742.

[72] W. Zhu, Y. D. Chong, and J. Gong, Floquet higher order topological insulator in a periodically driven bipartite lattice, *Phys. Rev. B* **103**, L041402 (2021).

[73] R.-X. Zhang, W. S. Cole, X. Wu, and S. Das Sarma, Higher-Order Topology and Nodal Topological Superconductivity in fe(se,te) Heterostructures, *Phys. Rev. Lett.* **123**, 167001 (2019).

[74] R. W. Bomantara, Time-induced second-order topological superconductors, *Phys. Rev. Research* **2**, 033495 (2020).

[75] Y. H. Wang, H. Steinberg, P. Jarillo-Herrero, and N. Gedik, Observation of floquet-bloch states on the surface of a topological insulator, *Science* **342**, 453 (2013).

[76] Y.-G. Peng, C.-Z. Qin, D.-G. Zhao, Y.-X. Shen, X.-Y. Xu, M. Bao, H. Jia, and X.-F. Zhu, Experimental demonstration of anomalous floquet topological insulator for sound, *Nat. Commun.* **7**, 13368 (2016).

[77] M. Lejman, G. Vaudel, I. C. Infante, P. Gemeiner, V. E. Gusev, B. Dkhil, and P. Ruello, Giant ultrafast photo-induced shear strain in ferroelectric bifeo3, *Nat. Commun.* **5**, 4301 (2014).

[78] R. Fleury, A. B. Khanikaev, and A. Alu, Floquet topological insulators for sound, *Nat. Commun.* **7**, 11744 (2016).

[79] T. Čadež, R. Mondaini, and P. D. Sacramento, Edge and bulk localization of floquet topological superconductors, *Phys. Rev. B* **99**, 014301 (2019).

[80] T. Nag and B. Roy, Anomalous and normal dislocation modes in floquet topological insulators, arXiv:2010.11952.

[81] T. Nag, S. Roy, A. Dutta, and D. Sen, Dynamical localization in a chain of hard core bosons under periodic driving, *Phys. Rev. B* **89**, 165425 (2014).

[82] A. Agarwala, U. Bhattacharya, A. Dutta, and D. Sen, Effects of periodic kicking on dispersion and wave packet dynamics in graphene, *Phys. Rev. B* **93**, 174301 (2016).

[83] A. A. Patel, S. Sharma, and A. Dutta, Quench dynamics of edge states in 2-d topological insulator ribbons, *Eur. Phys. J. B* **86**, 367 (2013).

[84] A. Rajak and A. Dutta, Survival probability of an edge majorana in a one-dimensional $p$-wave superconducting chain under sudden quenching of parameters, *Phys. Rev. E* **89**, 042125 (2014).

[85] S. Wu, V. Fatemi, Q. D. Gibson, K. Watanabe, T. Taniguchi, R. J. Cava, and P. Jarillo-Herrero, Observation of the quantum spin hall effect up to 100 kelvin in a monolayer crystal, *Science* **359**, 76 (2018).

[86] X. Qian, J. Liu, L. Fu, and J. Li, Quantum spin hall effect in two-dimensional transition metal dichalcogenides, *Science* **346**, 1344 (2014).

085413-13

[87] B. Fu, Zi-Ang Hu, C.-A. Li, J. Li, and S.-Q. Shen, Chi- ral majorana hinge modes in superconducting dirac materials, arXiv:2010.15633.

[88] E. Wang, H. Ding, A. V. Fedorov, W. Yao, Z. Li, Y.-F. Lv, K. Zhao, L.-G. Zhang, Z. Xu, J. Schneeloch, R. Zhong, S.-H. Ji, L. Wang, K. He, X. Ma, G. Gu, H. Yao, Q.-K. Xue, X. Chen, and S. Zhou, Fully gapped topological surface states in bi2se3 films induced by a d-wave high-temperature superconductor, Nat. Phys. 9, 621 (2013).

[89] C.-X. Liu, H. Zhang, B. Yan, X.-L. Qi, T. Frauenheim, X. Dai, Z. Fang, and S.-C. Zhang, Oscillatory crossover from two- dimensional to three-dimensional topological insulators, Phys. Rev. B 81, 041307(R) (2010).

[90] Y. Zhang, K. He, C.-Z. Chang, C.-L. Song, L.-L. Wang, X. Chen, J.-F. Jia, Z. Fang, X. Dai, W.-Y. Shan et al., Crossover of the three-dimensional topological insulator bi 2 se 3 to the two-dimensional limit, Nat. Phys. 6, 584 (2010).

[91] J. W. McIver, B. Schulte, F.-U. Stein, T. Matsuyama, G. Jotzu, G. Meier, and A. Cavalleri, Light-induced anomalous hall effect in graphene, Nat. Phys. 16, 38 (2020).

[92] S. Nadj-Perge, I. K. Drozdov, J. Li, H. Chen, S. Jeon, J. Seo, A. H. MacDonald, B. Andrei Bernevig, and A. Yazdani, Obser- vation of majorana fermions in ferromagnetic atomic chains on a superconductor, Science 346, 602 (2014).

[93] S. A. Sato, J. W. McIver, M. Nuske, P. Tang, G. Jotzu, B. Schulte, H. Hübener, U. De Giovannini, L. Mathey, M. A. Sentef, A. Cavalleri, and A. Rubio, Microscopic theory for the light-induced anomalous hall effect in graphene, Phys. Rev. B 99, 214302 (2019).

[94] R. Tuovinen, E. Perfetto, R. van Leeuwen, G. Stefanucci, and M. A. Sentef, Distinguishing majorana zero modes from im- purity states through time-resolved transport, New J. Phys. 21, 103038 (2019).

[95] D. A. Abanin, W. De Roeck, and F. Huveneers, Exponentially Slow Heating in Periodically Driven Many-Body Systems, Phys. Rev. Lett. 115, 256803 (2015).

[96] M. Messer, K. Sandholzer, F. Görg, J. Minguzzi, R. Desbuquois, and T. Esslinger, Floquet Dynamics in Driven Fermi-Hubbard Systems, Phys. Rev. Lett. 121, 233603 (2018).

[97] M. Bukov, L. D'Alessio, and A. Polkovnikov, Universal high-frequency behavior of periodically driven systems: from dynamical stabilization to floquet engineering, Adv. Phys. 64, 139 (2015).