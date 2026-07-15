# Two-dimensional ferromagnetic semiconductors of rare-earth Janus 2H-GdIBr monolayer with large valley polarization

Cunquan Li¹ and Yukai An¹,∗

¹Key Laboratory of Display Materials and Photoelectric Devices,
Ministry of Education, Tianjin Key Laboratory for Photoelectric Materials and Devices,
National Demonstration Center for Experimental Function Materials Education,
School of Material Science and Engineering, Tianjin University of Technology, Tianjin, 300384, China

Two-dimensional ferromagnetic semiconductors with excellent electronic, optical, and magnetic properties have become potential candidates for multiple functional nanodevices. Based on a rare-earth Gd atom with $4f$ electrons, through first-principles calculations, we demonstrate that the Janus 2H-GdIBr monolayer exhibits an intrinsic ferromagnetic (FM) semiconductor character with an indirect band gap of 0.75 eV, high Curie temperature $T_c$ of 260 K, significant magnetic moment of $8\ \mu_B/$f.u. (f.u.=formula unit), in-plane magnetic anisotropy (IMA) and large spontaneous valley polarization of 118 meV. The MAE, inter-atomic distance or angle, and $T_c$ can be efficiently modulated by in-plane strains and charge carrier doping. Under the strain range from $-5\%$ to $5\%$ and charge carrier doping from $-0.3$e to $0.3$e/f.u., the system still remains FM ordering and the corresponding $T_c$ can be modulated by strains from 233 K to 281 K and by charge carrier doping from 140 K to 245 K. Interestingly, under various strains, the matrix elements differences $(d_{z^2},d_{yz})$, $(d_{x^2-y^2},d_{xy})$ and $(p_x,p_y)$ of Gd atoms dominate the MAE behaviors, which originates from the competition between the contributions of Gd-$d$, Gd-$p$ orbitals, and $p$ orbitals of halogen atoms based on the second-order perturbation theory. Inequivalent Dirac valleys are not energetic degenerate due to the time-reversal symmetry breaking in the Janus 2H-GdIBr monolayer. A considerable valley gap between the Berry curvature at the K and K$'$ points provides an opportunity to selectively control the valley freedom and to manipulate the anomalous Hall effect. External tensile (compressive) strain further increases (decreases) the valley gap up to a maximum (minimum) value of 158 (37) meV, indicating that the valley polarization in the Janus 2H-GdIBr monolayer is robust to the external strains. This study provides a novel paradigm and platform to design the spintronic devices for next-generation quantum information technology.

## I. INTRODUCTION

As described by the Mermin-Wagner theorem [1], the long-range magnetic order of two-dimensional (2D) systems at finite temperature is forbidden by strong fluctuations. Recent studies suggest that magnetic anisotropy opens a gap in the spin-wave spectrum and suppresses the effect of thermal fluctuations. Consequently, when a 2D system exhibits intrinsic anisotropy caused by spin-orbit coupling (SOC), its long-range magnetic order can be well preserved, which has been observed in the $CrI_3$ monolayer and $Cr_2Ge_2Te_6$ bilayer with a Curie temperature ($T_c$) of 45 K[2] and 28 K [3], respectively. However, the low $T_c$ is not suitable for the advances of 2D magnetic devices in spintronics. Although, $T_c$ can be moderately increased by carrier doping [4], strain [5], and electric field [6], these extrinsic methods are not ideal for the practical application of devices. Therefore, the exploration of intrinsic 2D ferromagnetic semiconductors with high $T_c$ are urgent for the application of 2D spintronics at nanoscale [7].

Recently, various 2D materials with hexagonal lattice structures, especially for group-VI transition-metal dichalcogenides (TMDs), have opened the possibility of practical implementation of valleytronics. In monolayer TMDs, the conduction-band minima (CBM) and valence-band maxima (VBM) are located at two degenerates but inequivalent valleys at the K and K$'$ point of hexagonal Brillouin zone due to spatial inversion symmetry breaking [8]. Motivated by this observation, a great deal of interest focuses on exploiting the valley index of so-called K-valley materials, which is rather significant for information processing and storage in electronic devices [9]. If the intrinsic ferromagnetic ordering can introduce spontaneous valley polarization, the namely ferro-valley materials are proposed. Until now, only a few ferro-valley materials have been predicted, including $TiVI_6$ [10], $LaBr_2$ [11] and $VAgP_2Se_6$ monolayers [12], and so on. However, these materials are still not applicable due to the slight intrinsic valley splitting gap and low $T_c$. Most 2D valley materials do not exhibit spontaneous valley polarization due to their temporal inversion symmetry. In general, breaking the inversion symmetry also lifts the spin degeneracy of energy band due to the presence of SOC effect. The introduction of valley polarization is necessary to distinguish and manipulate the carriers in the specified valleys. In other respects, charge carriers can also be distinguished by their spin moments. Thus, many peculiar properties will also be born, such as the quantum valley anomaly Hall effect [13] .However, the results mentioned above more focus on the $d$-electron systems, while the studies on the $f$-electron systems are relatively less. Inspired by the significant magnetic mo-

∗ ykan@tjut.edu.cn

ments and high magneto-crystal anisotropy typically as- sociated with rare-earth elements [14], introducing rare earth elements is expected to largely increase the $T_{c}$ and magnetization. Very recently, the 2D systems contain- ing Gd with high $T_{c}$ have been reported, such as $GdI_{2}$ (300-340 K) [15], GdScSi (352 K) [16] and $Gd_{2}B_{2}$ (500 K) monolayers [17]. Wang er al. [18] and Feng et al.[19] reported that 2D ferromagnetic $GdI_{2}$ monolayer ex hibits a good dynamic and thermal stability with high $T_{c}$ of about 241 K. Zhang et al. further proved that the $GdCl_{2}$ monolayer exhibits the large perpendicular mag netic anisotropy and high $T_{c}(224 K)$ [20].However, there are scarce reports about the Gd based-Janus monolayers with the breaking of mirror symmetry. In this work, the stability, electronic, magnetic, and valley properties of rare-earth-based Janus 2H-GdIBr monolayer are in- vestigated systematically. Notably, the Janus 2H-GdIBr monolayer can be easily exfoliated from parent layered bulk crystal and exhibit good thermodynamically and ki- netically stability as well as the high $T_{c}$ of 260 K, large magnetic moment of $8 \mu_{B} /$ f.u., spontaneous valley po larization of 118 meV and in-plane magnetic anisotropy $(-420 \mu eV /$ f.u). The Berry curvature of K and K'-valleys shows opposite signs, and the non-zero Berry phase leads to a non-zero anomalous Hall conductivity. These find- ings strongly suggest the potential application of Janus2H-GdIBr monolayer in valley electronic devices.

## II. COMPUTATIONAL METHODS

All calculations are performed based on spin-polarized density generalized function theory (DFT) using the Perdew-Burke-Ernzerhof (PBE) function in the gen- eralized gradient approximation (GGA) [21, 22], im- plemented in the Vienna ab-initio simulation Package(VASP) [23-25]. A vacuum space of $18 \AA$ is set to avoid the interaction between monolayers, and an energy cut- off of 500 eV is set for the plane-wave basis set. The Brillouin zone is sampled using a converged $\Gamma$ -centered8×8×1 k-mesh for structural relaxation and 18×18×1 for the electronic calculations. The standard pseudopo- tential is used and the valence electron configuration is considered as $5 s^{2} 5 p^{6} 4 f^{7} 5 d^{1} 6 s^{2}$ for Gd [26], $4 s^{2} 4 p^{5}$ for Br, and $5 s^{2} 5 p^{5}$ for I. The crystal structure of Janus2H-GdIBr monolayer is fully relaxed, and the conver- gence criteria of energy and forces are $10^{-7} eV$ and 0.005eV/Å, respectively. The rotationally invariant LSDA+U method is used to handle the strongly correlated correc- tions to the Gd 4f electrons, and the on-site Coulomb interaction parameter (U) and exchange interaction pa- rameter (J) are set at 9.20 and 1.20 eV, respectively[27, 28]. Phonon dispersion spectrum of Janus 2H-GdIBr monolayer is obtained by the PHONOPY code [29, 30]based on the density of functional perturbation theory[31] using a 4×4×1 supercell. The VASPKIT code is used to process the VASP data [32]. Ab initio molecular dynamic (AIMD) simulations are adopted the NVT en- semble based on the Nosé-Hothermostat [33] controlledthe temperature of systems at 300 K with a total of 10 ps at 2 fs per step. The Monte Carlo simulation open- source project MCSOLVER [34] is used to estimate the T. based on the Wolff algorithm of the classical Heisen- berg model. 80,000 scans are set to fully thermalize the system to equilibrium within the specified temper- ature interval starting from the ferromagnetic order. All statistics are obtained from the 720,000 scans that im- mediately followed. The Berry curvature and anomalous Hall conductivity of Janus 2H-GdIBr monolayer are cal- culated using maximally localized Wannier functions im- plemented in the WANNIER90 [35] and WannierTools package [36]. VASPBERRY [37] is used to study its op- tical properties.

## III. RESULTS AND DISCUSSION

The top and side views of crystal structures for the Janus 2H-GdIBr monolayer are shown in Figure 1a. The Janus 2H-GdIBr monolayer consists of three atomic lay- ers, where the Gd atomic layer is sandwiched between two halogen atomic layers. Meanwhile, the central Gd atom is a trigonal shape coordinated to six halogen atoms. The calculated relaxation equilibrium lattice constants, Gd-I and Gd-Br bond lengths for the Janus 2H-GdIBr mono- layer are $a=b=4.019 \AA, 3.121 \AA$ , and $2.955 \AA$ , respec tively. The cleavage energy is calculated from a slab model to confirm the possibility of exfoliation of Janus2H-GdIBr monolayer from its layered bulk crystal. As shown in Figure 1b, the energy difference increases with the increase of separation distance $(\Delta d=d-d_{0})$ . Even tually, it converges to $0.24 J / m^{2}$ at the $\Delta d=9 \AA$ point, which is taken as the exfoliation energy and confirmed by the calculated cleavage strength (the first derivative of cleavage energy). The exfoliation energy is less than the experimental value of graphite $(0.36 J / m^{2})$ [38], suggest ing the feasibility of exfoliating Janus 2H-GdIBr mono- layer experimentally. The calculated magnetic moment of Gd atom is $7.4 \mu_{B} / Gd$ due to the contribution of half-filled 4f and 5d shells. Possible magnetic configu- rations including ferromagnetic (FM) and antiferromag- netic (AFM) states are considered, as shown in Figure 1c, which are the same as those reported previously [20, 39]. To investigate the magnetic ground state and configu- rations of Janus 2H-GdIBr monolayer, the energies of FM and AFM states of 2×2×1 supercell are compared. The energy of FM state is lower than that of AFM state by 152 meV/Gd [Figure S1], indicating the existence of strong FM coupling. As shown in Figure S2a, with the system always remaining FM state, the variation in the total energy of FM and AFM states can be considered a quadratic function of strains. Charge carrier doping can also effectively modulate the total energy of FM and AFM states [Figure S2b], but the system remains in the FM state. The calculated average electrostatic poten- tial $(\Delta \rho)$ along the z-axis is asymmetric with a potential

![](./images/867768896369721392_1.jpg)

FIG. 1. (a) Top and side views of Janus 2H-GdIBr monolayer with the nearest Gd-Gd distance $d_1$, Gd-I(Br) distance $d_2$ ($d_3$), and Gd-I(Br)-Gd bond angle $\theta_1(\theta_2)$. (b) The dependence of cleavage energy and cleavage strength on the separation distance ($\Delta d=d-d_0$) for the Janus 2H-GdIBr monolayer, where $d_0$ indicates the equilibrium vdW gap in the bulk crystal. The insert shows the calculated exfoliation process. (c) The FM and AFM orders for the Janus 2H-GdIBr monolayer. Red and green arrows denote spin-up and spin-down orientations, respectively. (d) Planar average electrostatic potential energy of Janus 2H-GdIBr monolayer. (e) The fluctuation of total energy and snapshots of geometric structures for the Janus 2H-GdIBr monolayer at 10 ps from AIMD simulations. (f) The phonon dispersion of Janus 2H-GdIBr monolayer.

drop of 6.9 eV, as shown in Figure 1d. In the sandwich structure, the potential difference between the two sides implies a change in the work function. Obviously, on the I side, the potential energy is smaller and work function is larger than those on the Br side, which is related to the larger electronegativity of I atom. Moreover, the electrostatic potential difference $\Delta \Phi$ of 0.13 eV can be considered as the redistribution of charges in the Janus 2H-GdIBr monolayer. Figure 1e shows the fluctuation of total energy and snapshots of geometric structures for the Janus 2H-GdIBr monolayer at 10 ps from AIMD simulations and the insets are snapshots of the geometry at 0 ps and 10 ps, respectively. Clearly, the simulated total free energy fluctuates within a small range and no significant deformation is observed at the final, suggesting good thermal stability. In addition, the phonon dispersion of Janus 2H-GdIBr monolayer is shown in Figure 1f. The frequencies of all phonon modes within the Brillouin zone are positive, indicating that the Janus 2H-GdIBr monolayer is dynamically stable.

Figure 2a shows the band structure of Janus 2H-GdIBr monolayer with spin polarization (without considering SOC). The spin splitting leads to an indirect band gap of 0.75 eV, with the VBM at the K(K$'$) point and the CBM at the M point. Around the Fermi level ($E_\text{F}$), the fully spin-polarized valence band and the opposite spin channel conduction band make the Janus 2H-GdIBr monolayer bipolar magnetic semiconductor (BMS). The spin-resolved density of states shown in Figure S3 demonstrates that the $d$ orbitals of Gd atoms contribute to the VBM and CBM for the Janus 2H-GdIBr monolayer. The spin splitting around $E_\text{F}$ does not appear for the I and Br atoms, implying that the magnetic moments of Janus 2H-GdIBr monolayer are mainly from the Gd atoms. As shown in Figure 2b, the SOC effect breaks the degeneracy between the K and K$'$ valleys in the valence band, namely the energy of K valley is higher than that of K$'$ valley. This results in a large spontaneous valley polarization of 118 meV, which is equivalent to a huge external magnetic field of about 590-1180 T. The valley states at the K and K$'$ points are mainly contributed by the occupied $d_{x^2-y^2}$ and $d_{xy}$ orbitals of Gd atom and the $\Gamma$ point is mainly distributed around the $d_{z^2}$ orbital of Gd atom, as shown in Figure S4. The spontaneous valley polarization can be attributed to the strong SOC effect combined with the magnetic exchange interaction of Gd-$d$ electrons due to the breaking of time-reversal symmetry. To further investigate the valley properties, the 3D energy band map in the first Brillouin zone is shown in Figure S5a. By projecting the two energy bands of VBM and CBM onto the horizontal plane, as shown in Figure S5b-c, the energy of VBM at the K and K$'$ points is not a global but a local minimum, while the energy of CBM at the K and K$'$ points is a global maximum. The valley polarization of Janus 2H-GdIBr monolayer is much larger than those of other reported ferro-valley materials, e.g., $\text{GdF}_2$ (47.6 meV) [40], $\text{VAgP}_2\text{Se}_6$ (15 meV) [12], and $\text{LaBr}_2$ (33 meV) [41]. To be a valley material for practical applications,

![](./images/867768896369721392_2.jpg)

FIG. 2. The band structure of Janus 2H-GdIBr monolayer (a) without SOC; (b) with SOC, and (c) with SOC+MLWFs, respectively. Red (blue) arrows represent the spin up (down). (d) The local density of states of edge states for the Janus 2H-GdIBr monolayer projected on (001) surface. The $E_{\text{F}}$ is set to zero.

the valley polarization must be large enough. Generally, an estimated valley polarization of 100 meV is required to overcome the thermal noise [42]. In addition, the absence of other bands within the transmission energy window of $-2$ to 0 eV provides more possibilities for tuning the valley polarization of Janus 2H-GdIBr monolayer, such as applying magnetic fields and changing the magnetic axis orientation.

To ensure the accuracy of Wannier basis functions, the tightly bound band structure with the spin operator projection $(\hat{S}_{z})$, obtained from the Wannier interpolation [43] is calculated using MLWFs [Figure 2c], which is basically in full agreement with the DFT results [Figure 2b]. The average spin values of the valence and conduction band edge states are found to be 1 and $-1$, respectively. Thus, their spins remain almost parallel in the upward and downward directions, which usually generates an effective magnetic field that contributes to the energy transfer. Simultaneously, simulated ARPES spectrum [Figure 2d] are calculated using the Wannier function and the iterative Green's function method [44, 45], strongly suggesting that the surface is also a semiconductor state.

Magnetic anisotropy is a critical factor for realizing the long-range FM ordering and the corresponding magnetic anisotropy energy (MAE) can be calculated by considering the transition of magnetic moment from the in-plane [100] to the out-of-plane [001] axis. The Janus 2H-GdIBr monolayer exhibits the in-plane magnetic anisotropy (IMA) with a value of 0.42 meV, which is between the $2\text{H-GdI}_{2}$ (0.688 meV) and $2\text{H-GdBr}_{2}$ (0.109 meV) monolayers [20]. Figure 3a shows the MAE of Janus 2H-GdIBr monolayer under various strains. The in-plane strain can be defined as $\varepsilon$=$({a - a_{0}})/a_{0}$×100%, where $a$ and $a_{0}$ represented the in-plane lattice constants of strained and unstrained Janus 2H-GdIBr monolayer, respectively. It is obvious that the MAE of Janus 2H-GdIBr monolayer shows a monotonous increase as the strain increases from $-8\%$ to $8\%$. The atomic layer-resolved MAEs for the Janus 2H-GdIBr monolayer under various strains are shown in Figure 3b. One can see that the MAE of Janus 2H-GdIBr monolayer is mainly determined by the Gd and I atoms. The Br and I atoms show the IMA character, while the Gd atom exhibits a transition from the PMA to IMA characters at the strain increases from $-8\%$ to $8\%$. The orbital-resolved MAE can be defined by using the second-order perturbation theory:

$$
\text{MAE} = \xi^{2} \sum_{o,u} \frac{\left|\left\langle \psi_{o} \left| \hat{L}_{x} \right| \psi_{u} \right\rangle\right|^{2} - \left|\left\langle \psi_{o} \left| \hat{L}_{z} \right| \psi_{u} \right\rangle\right|^{2}}{E_{u} - E_{o}} \quad (1)
$$

where $E_{o}$ ($E_{u}$) represent the energies of occupied (non-occupied) states and the $\xi$, $o$, and $u$ are the SOC constants. The Gd-d, Gd-p and I(Br)-p orbital resolved MAEs of Janus 2H-GdIBr monolayer at the strains of $-6\%$, $0\%$, and $6\%$ are shown in Figure 3c and Figure S6. For the unstrained (0%) Janus 2H-GdIBr monolayer, more significant positive MAE (IMA) can be attributed to the matrix elements differences $(p_{x},p_{y})$ of I atom as well as the matrix elements differences $(d_{z^{2}},d_{yz})$ and $(p_{x},p_{y})$ of Gd atom. When the strain changes from $-6\%$ to $6\%$, the positive MAE increases, which is mainly caused by the increase of matrix element difference $(d_{z^{2}},d_{yz})$ of Gd atom and the decrease of matrix element difference $(p_{x},p_{y})$ and $(d_{x^{2}-y^{2}},d_{xy})$ of Gd atom. It is noted that the matrix elements difference $(d_{z^{2}},d_{yz})$ and $(d_{x^{2}-y^{2}},d_{xy})$ of Gd atom shows the opposite signs at the strain of $-6\%$. However, at the strain of $6\%$, the matrix element difference $(d_{x^{2}-y^{2}},d_{xy})$ of Gd atom remarkably decreases, which is weak to the matrix element difference $(d_{z^{2}},d_{yz})$ of Gd atom. Meanwhile, the matrix elements differences $(p_{x},p_{y})$ of I and Br atoms keep stable and the matrix elements differences $(p_{x},p_{y})$ of Gd atom monotonously decrease, which results in the appearance of IMA character. Thus, the matrix elements differences $(d_{z^{2}},d_{yz})$, $(d_{x^{2}-y^{2}},d_{xy})$ and $(p_{x},p_{y})$ of Gd atoms dominate the MAE behaviors under various strains for the Janus 2H-GdIBr monolayer. The dependence of MAE (MAE=E$^{[001]}$−E$^{\theta}$) on the polar angle ($\theta$) is also investigated. Figure 4a shows the angular dependence of MAE along the X (100), Y (010), and Z (001) axes. It is clear

![](./images/867768896369721392_3.jpg)

FIG. 3. (a) Total and (b) atomic-layer-resolved MAEs for the Janus 2H-GdIBr monolayer under various strains. (c) Gd-d, Gd-p and I-p orbital resolved MAEs for the Janus 2H-GdIBr monolayer under biaxial strains of $-6\%$, $0\%$ and $6\%$.

that the MAE strongly depends on the direction of magnetization in the $xz$ and $yz$ planes. In contrast, the MAE in the $xy$ plane is isotropic. Thus, a strong dependence of MAE on the angle of magnetization in the out-of-plane is observed, which is similar to the case of $VS_2$ [47] and $FeCl_2$ [48] monolayers. The strong magnetic anisotropy of Janus 2H-GdIBr monolayer can be confirmed by the distribution of MAE on the whole space, as shown in Figure 4b. The MAE is zero in the xy-plane and reaches a maximum value of $415\ \mu eV\ Gd^{-1}$ in the $xz$ ($yz$) plane, which is comparable to the $GdI_2$ monolayer ( $553\ \mu eV$ $Gd^{-1}$) [20].

High $T_c$ is crucial for the practical application of spintronic devices. To determine the long-range magnetic exchange interactions of Janus 2H-GdIBr monolayer, the metropolis Monte Carlo algorithm based on the Heisenberg model is used, and the spin Hamiltonian can be described as [49]:
$$
H=-J \sum_{i, j} S_{i} S_{j}-D \sum_{i}\left(S_{i}^{z}\right)^{2} \tag{2}
$$
where $S_i$ and $S_j$ are the spin operator, $J$ represents the isotropic part of exchange interaction, and $D$ represents the single-ion magnetic anisotropy on iron. All parameters in Eqn. (1) are determined by the energy mapping in relativistic density generalized function theory calculations for the 2×2×1 supercells, including cells with the FM and AFM configurations. The energies of FM and AFM states and the magnetic ion anisotropy parameter $D$ with considering the SOC effect can be calculated as follows:
$$
\mathrm{E}_{\mathrm{FM}}=\mathrm{E}_{0}-6 J|S|^{2}-D|S|^{2} \tag{3}
$$

$$
\mathrm{E}_{\mathrm{AFM}}=\mathrm{E}_{0}+2 J|S|^{2}-D|S|^{2} \tag{4}
$$
where $\mathrm{E}_{\mathrm{FM}}$ and $\mathrm{E}_{\mathrm{AFM}}$ are the total energies of FM and AFM configurations. $\mathrm{E}_{0}$ is the total energy in the system without magnetic exchange coupling. $|S|$ is the total spin of Gd. The nearest neighbor exchange parameter $J$ is defined as:
$$
J=\frac{\mathrm{E}_{\mathrm{AFM}}-\mathrm{E}_{\mathrm{FM}}}{8|S|^{2}} \tag{5}
$$

The calculated $J$ value for the Janus 2H-GdIBr monolayer is 1.188 meV, suggesting that the magnetic interactions between the nearest neighboring Gd atoms are in FM state. Figure 4c shows the temperature dependences of average magnetic moment and speciated heat for the Janus 2H-GdIBr monolayer. During the simulation from 0 K to 400 K, $T_c$ can be estimated to be about 260 K. Also, using the same method, the calculated $T_c$ of $\mathrm{CrI}_{3}$ monolayer is about 47 K, which is similar to the experimental result of 45 K [50], proving the reliability of the results. Combined with the calculated high $T_c$, the Janus 2H-GdIBr monolayer can be expected as an ideal ferrovalley material for applications in valley electronics. A real-space renormalization group analysis is used to avoid errors originating from finite size by roughly dividing the original 32×32 lattices into a 16×16 lattice, with every four adjacent spins forming quasiparticles, each with a representative spin. The Heisenberg Hamiltonian of the renormalized model is assumed to be the same as before, and the internal energy of this system is recalculated. More details are shown in Figure S7.

The highly localized $4f$ electrons on Gd atoms is negligible in the magnetic exchange coupling. However, more

![](./images/867768896369721392_4.jpg)

FIG. 4. Dependence of MAE on the polar angle ($\theta$) for the Janus 2H-GdIBr monolayer with the direction of magnetization lying on (a) $xy$, $xz$ and $yz$ planes as well as (b) the whole space. (c) Evolution of average magnetic moment and specific heat for the Janus 2H-GdIBr monolayer.

extended $5d$ electrons on Gd atoms occupy the spin-up channel near the $E_{\text{F}}$, making the Janus 2H-GdIBr monolayer a magnetic semiconductor. According to the Kramer mechanism, the partially occupied states can result in the direct exchange interaction between the nearest Gd-Gd atoms, and the bond angle of Gd-I(Br)-Gd is close to $90^{\circ}$, satisfying the Goodenough-Kanamori-Anderson (GKA) rules [51-53]. To investigate the origin of FM coupling in the Janus 2H-GdIBr monolayer, interatomic interactions need to be considered. Generally, the direct (super) exchange depends on the Gd-Gd (Gd-I(Br)-Gd) bond, which leads to the FM (AFM) states. Generally, the Gd-Gd (I/Br) distance and the Gd-I(Br)-Gd bond angle mainly contribute to this magnetic exchange mechanism. Thus, the synergistic effects of direct and super exchange interactions determine the magnetic ground state of Janus 2H-GdIBr monolayer. The high concentration of hole carrier doping usually induces a transition from the AFM to FM states, proving the effectiveness of modulating the magnetic behavior by charge carrier doping. As shown in Figure 5a-b, the nearest Gd-Gd distance $d_{1}$ always remains constant, and the Gd-I distance $d_{2}$, and Gd-Br distance $d_{3}$ show a monotonic and slight increasing (decreasing) trend under electron (hole) doping. Meanwhile, the Gd-I-Gd bond angle $\theta_{1}$/Gd-Br-Gd bond angle $\theta_{2}$ increases (decreases) with increasing hole (electron) concentration, which significantly strengthens (weakens) the super-exchange interaction. During the experiment, various strains caused by the lattice mismatch of substrate is common. Figure 5c-d shows the dependence of the Gd-Gd(I/Br) distance $d$ and the Gd-I(Br)-Gd bond angle $\theta$ on strains. As the strain increases from $-8\%$ to $8\%$, the nearest Gd-Gd distance $d_{1}$ (from $3.70$ Å to $4.34$ Å) and Gd-I-Gd bond angle $\theta_{1}$ (from $74.2^{\circ}$ to $85.5^{\circ}$)/Gd-Br-Gd bond angle $\theta_{2}$ (from $79.4^{\circ}$ to $91.0^{\circ}$) exhibit the monotonical increasing behaviors. According to the GKA rule, the increased (decreased) $d_{1}$ weakens (strengthens) the direct exchange interaction. Meanwhile, the increased (decreased) angle $\theta_{1}/\theta_{2}$ enhances (weakens) the super-exchange interaction. Clearly, the direct exchange and super-exchange interactions compete with each other. Combing with the dependence of exchange parameter $J$ on strain [Figure S8a], the increased or decreased $d_{1}$ makes the direct exchange interaction more critical in determining the FM state. Generally, the tensile (compressive) strain weakens (enhances) the FM coupling and plays a vital role in the direct and super exchange mechanisms. Meanwhile, in the range of hole doping, the exchange parameter $J$ changes slightly, and the $T_{c}$ near room-temperature is well preserved for the Janus 2H-GdIBr monolayer. In contrast, the exchange parameter $J$ and corresponding $T_{c}$ change significantly with increasing electron doping [Figure S8b-d]. The tensile (compressive) strain tends to monotonically decrease (increase) the exchange parameter $J$ and corresponding $T_{c}$. Interestingly, the maximum $T_{c}$ reaches to 281 K at the tensile strain of $8\%$, close to the room temperature [Figure S8a, c-d].

![](./images/867768896369721392_5.jpg)

FIG. 5. Charge carrier doping dependence of the inter-atomic (a) distance and (b) angle for the Janus 2H-GdIBr monolayer. Biaxial strain dependence of the inter-atomic (c) distance and (d) angle for the Janus 2H-GdIBr monolayer.

Berry curvature is closely related to the Hall effect of

![](./images/867768896369721392_6.jpg)

FIG. 6. Calculated Berry curvature of Janus 2H-GdIBr mono- layer (a) along high symmetry lines and (b) over the 2D Bril- louin zone. (c) Calculated anomalous Hall conductivity of the Janus 2H-GdIBr monolayer, the two dashed lines denote the two valley extrema. (d) Variation of valley polarization for the Janus 2H-GdIBr monolayer as a function of strain from $-8\%$ to $8\%$.

the system. When the space inversion symmetry is bro- ken in the hexagonal systems, the charge carriers at the K and K' valleys can generate the non-zero Berry phases along the z-direction in accompany with a non-zero Berry curvature. When the time-reversal symmetry is also bro- ken, the characteristic of valley contrast appears. To investigate this property, the Berry curvature of Janus2H-GdIBr monolayer is calculated according to the Kuboformula [54]:

$$
\Omega(k)=-\sum_{n} \sum_{n \neq m} f(n) \frac{2 \operatorname{Im}\left\langle\varphi_{n k}\left|v_{x}\right| \varphi_{m k}\right\rangle\left\langle\varphi_{m k}\left|v_{y}\right| \varphi_{n k}\right\rangle}{\left(\mathrm{E}_{n}-\mathrm{E}_{m}\right)^{2}}
\tag{6}
$$

where $v_{x}$ and $v_{y}$ are velocity operators of the Dirac elec trons along $x$ and $y$ directions, respectively. $f(n)$ is the Fermi-Dirac distribution function for the $n^{th}$ band, and $|\varphi_{n k}\rangle$ is the calculated Bloch wave function with the energy eigenvalue $E_{n}(E_{m})$ . The maximally localized Wannier function is used to calculate the Berry curva- ture. Figure 6a-b shows the Berry curvature of Janus 2H- GdIBr monolayer along the high symmetry line and over the 2D Brillouin zone. It is clear that the K and K' valleys have opposite signs of Berry curvature and slightly dif- ferent absolute values, revealing that the valley contrast phenomenon plays an important role in characterizing the Bloch electron chirality in k-space [55]. Away from the K and K' valleys, Berry curvature decays rapidly and disappears at the M point. As described in Eqn. (6) [56], the Berry curvature drives a peculiar transverse velocityin the presence of an in-plane electric field $E$:

$$
v=-\frac{e}{\hbar} E × \Omega(k)
\tag{7}
$$

This is an intrinsic contribution of the anomalous Hall effect. The integral of Berry curvature in the Brillouin zone gives the contribution to the anomalous Hall con-ductivity (AHC), which can be defined as [57]:

$$
\sigma_{x y}=-\frac{e^{2}}{\hbar} \int_{B Z} \frac{d^{2} k}{(2 \pi)^{2}} \Omega(k)
\tag{8}
$$

Due to the opposite sign and unequal absolute value of Berry curvature, the charge carriers in the K and K' val- leys have opposite transverse velocities. Thus, anomalous Hall conductivity with a net value of non-zero is gener- ated. As shown in Figure 6c, when the $E_{F}$ is located be tween the valence band edges of the K and K' valleys, a fully valley-polarized Hall conductivity is generated with a calculated maximum AHC of 9.5 S/cm. In addition, the $E_{F}$ can be effectively tuned above (below) the val ley splitting gap by a low concentration of carrier doping[Figure S9]. On the other hand, if a finite valley polariza- tion can be generated, for example, by irradiating with circularly polarized light [see details in Figure S10], the Hall currents will also appear. As shown in Figure 6d, the valley polarization increases monotonically with the increase (decrease) of tensile (compressive) strains. And a giant valley polarization of about 158 meV is obtained at tensile strain of $8 \%$ . But the valley polarization re mains significant (about 37 meV) under a considerable compressive strain of $-8 \%$ , implying that the valley po larization is robust against the in-plane strain. Therefore, the Janus 2H-GdIBr monolayer can be considered as an ideal ferro-valley material providing a potential platform for valley electronic applications.

## IV. CONCLUSIONS
In summary, by first principles calculations, we pre- dict that the Janus 2H-GdIBr monolayer exhibits a low exfoliation energy of $0.24 ~J / m^{2}$ and possesses tunable semiconductor character with the sizeable magnetic mo- ment, high $T_{c}$ of $260 ~K$ , in-plane magnetic anisotropy, and excellent thermal and dynamic stability. The MAE and valley polarization features are robust against the in-plane biaxial strains. The total MAE can increase monotonously from nearly 0.1 to 0.81 meV/f.u. under strain from $-8 \%$ to $8 \%$ . Meanwhile, the easy axis of Gd atom show a transition from the [001] to [100] direc- tion. Based on the second-order perturbation theory, it is found that the competition between the contributions of Gd- $d$ , Gd- $p$ orbitals, and $p$ orbitals of halogen atoms in duce the IMA character. When the tensile strain of $8 \%$ is applied, the valley polarization of Janus 2H-GdIBr mono- layer can reach a maximum value of 158 meV. Further-more, the corresponding $T_{c}$ is tuned by strains from 233

$K\ (8\%)$ to $281\ K\ (-8\%)$ and charge carrier doping from $140\ K\ (0.3\mathrm{e/f.u.})$ to $245\ K\ (-0.3\mathrm{e/f.u.})$. In addition, the origin of FM coupling in the Janus 2H-GdIBr monolayer can be attributed to the direct-exchange (Gd-Gd) and super-exchange (Gd-I(Br)-Gd) interactions. Due to the space-inversion and time-reversal symmetry breaking, an appropriate external electric field can achieve the anoma- lous valley Hall effect in the Janus 2H-GdIBr monolayer.

Overall, it can be expected that Janus-2H-GdIBr mono- layer is a new candidate for the next generation of spin- tronic and valleytronic devices.

## ACKNOWLEDGMENTS

This work was supported by Natural Science Founda- tion of Tianjin City (Grant No. 20JCYBJC16540).

[1] N. D. Mermin and H. Wagner, Absence of ferromag- netism or antiferromagnetism in one-or two-dimensional isotropic Heisenberg models, *Phys. Rev. Lett.* **17**, 1133 (1966).

[2] B. Huang, G. Clark, E. Navarro-Moratalla, D. R. Klein, R. Cheng, K. L. Seyler, D. Zhong, E. Schmidgall, M. A. McGuire, D. H. Cobden, W. Yao, D. Xiao, P. Jarillo- Herrero, and X. Xu, Layer-dependent ferromagnetism in a van der Waals crystal down to the monolayer limit, *Nature* **546**, 270 (2017).

[3] C. Gong, L. Li, Z. Li, H. Ji, A. Stern, Y. Xia, T. Cao, W. Bao, C. Wang, Y. Wang, Z. Q. Qiu, R. J. Cava, S. G. Louie, J. Xia, and X. Zhang, Discovery of intrinsic fer- romagnetism in two-dimensional van der Waals crystals, *Nature* **546**, 265 (2017).

[4] B. Wang, Q. Wu, Y. Zhang, Y. Guo, X. Zhang, Q. Zhou, S. Dong, and J. Wang, High Curie-temperature in- trinsic ferromagnetism and hole doping-induced half- metallicity in two-dimensional scandium chlorine mono- layers, *Nanoscale Horiz.* **3**, 551 (2018).

[5] L. Webster and J.-A. Yan, Strain-tunable magnetic anisotropy in monolayer $\mathrm{CrCl_3}$, $\mathrm{CrBr_3}$, and $\mathrm{CrI_3}$, *Phys. Rev. B* **98**, 144411 (2018).

[6] Z. Wang, T. Zhang, M. Ding, B. Dong, Y. Li, M. Chen, X. Li, J. Huang, H. Wang, and X. Zhao, Electric-field control of magnetism in a few-layered van der Waals ferromagnetic semiconductor, *Nat. Nanotechnol.* **13**, 554 (2018).

[7] L. Cai, V. Tung, and A. Wee, Room-temperature ferro- magnetism in two-dimensional transition metal chalco- genides: Strategies and origin, *J. Alloys Compd.* **913**, 165289 (2022).

[8] T. Zhang, X. Xu, B. Huang, Y. Dai, and Y. Ma, 2D spontaneous valley polarization from inversion symmetric single-layer lattices, *npj Comput. Mater.* **8**, 64 (2022).

[9] T. Zhang, S. Zhao, A. Wang, Z. Xiong, Y. Liu, M. Xi, S. Li, H. Lei, Z. V. Han, and F. Wang, Electrically and Magnetically Tunable Valley Polarization in Monolayer $\mathrm{MoSe_2}$ Proximitized by a 2D Ferromagnetic Semiconduc- tor, *Adv. Funct. Mater.* 2204779 (2022).

[10] W. Du, Y. Ma, R. Peng, H. Wang, B. Huang, and Y. Dai, Prediction of single-layer $\mathrm{TiVI_6}$ as a promising two-dimensional valleytronic semiconductor with spon- taneous valley polarization, *J. Mater. Chem. C* **8**, 13220 (2020).

[11] J. Zhou, Y. P. Feng, and L. Shen, Atomic-orbital-free intrinsic ferromagnetism in electrenes, *Phys. Rev. B* **102**, 180407 (2020),.

[12] Z. Song, X. Sun, J. Zheng, F. Pan, Y. Hou, M.-H. Yung, J. Yang, and J. Lu, Spontaneous valley splitting and valley pseudospin field effect transistors of monolayer $\mathrm{VAgP_2Se_6}$, *Nanoscale* **10**, 13986 (2018).

[13] P. Zhao, Y. Dai, H. Wang, B. Huang, and Y. Ma, Intrinsic valley polarization and anomalous valley hall effect in single-layer $2\mathrm{H}$-$\mathrm{FeCl_2}$, *ChemPhysMater* **1**, 56 (2022).

[14] H. Hedjar, S. Meskine, A. Boukortt, H. Bennacer, and M. R. Benzidane, First-principles studies of electronic structure, magnetic and optical properties of rare-earth (RE= Sm, Eu, Gd, and Er) doped ZnS, *Comput. Con- dens. Matter* **30**, e00632 (2022).

[15] A. Kasten, P. H. Müller, and M. Schienle, Magnetic or- dering in $\mathrm{GdI_2}$, *Solid State Commun.* **51**, 919 (1984).

[16] S. Gupta and K. G. Suresh, Review on magnetic and related properties of RTX compounds, *J. Alloys Compd.* **618**, 562 (2015).

[17] T. Gorkan, E. Vatansever, Ü. Akıncı, G. Gökoglu, E. Ak- türk, and S. Ciraci, Above Room Temperature Ferro- magnetism in $\mathrm{Gd_2B_2}$ Monolayer with High Magnetic Anisotropy, *J. Phys. Chem. C* **124**, 12816 (2020),.

[18] B. Wang, X. Zhang, Y. Zhang, S. Yuan, Y. Guo, S. Dong, and J. Wang, Prediction of a two-dimensional high-$T_C$ f-electron ferromagnetic semiconductor, *Mater. Horiz.* **7**, 1623 (2020).

[19] H.-X. Cheng, J. Zhou, W. Ji, Y.-N. Zhang, and Y.-P. Feng, Two-dimensional intrinsic ferrovalley $\mathrm{GdI_2}$ with large valley polarization, *Phys. Rev. B* **103**, 125121 (2021),.

[20] W. Liu, J. Tong, L. Deng, B. Yang, G. Xie, G. Qin, F. Tian, and X. Zhang, Two-dimensional ferromagnetic semiconductors of rare-earth monolayer $\mathrm{GdX_2}$ (X= Cl, Br, I) with large perpendicular magnetic anisotropy and high Curie temperature, *Mater. Today Phys.* **21**, 100514 (2021).

[21] J. P. Perdew, K. Burke, and M. Ernzerhof, Generalized Gradient Approximation Made Simple, *Phys. Rev. Lett.* **77**, 3865 (1996),.

[22] P. Söderlind, O. Eriksson, B. Johansson, and J. M. Wills, Electronic properties of f-electron metals using the gen- eralized gradient approximation, *Phys. Rev. B* **50**, 7291 (1994),.

[23] G. Kresse and J. Furthmüller, Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set, *Comput. Mater. Sci.* **6**, 15 (1996).

[24] G. Kresse and J. Furthmüller, Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set, *Phys. Rev. B* **54**, 11169 (1996),.

[25] G. Kresse and J. Hafner, Ab initio molecular dynamics for liquid metals, *Phys. Rev. B* **47**, 558 (1993),.

[26] H. You, Y. Zhang, J. Chen, N. Ding, M. An, L. Miao, and S. Dong, Peierls transition driven ferroelasticity in

the two-dimensional $d-f$ hybrid magnets, Phys. Rev. B 103, L161408 (2021),.

[27] P. Larson, W. R. L. Lambrecht, A. Chantis, and M. van Schilfgaarde, Electronic structure of rare-earth nitrides using the LSDA $+U$ approach: Importance of allowing $4f$ orbitals to break the cubic crystal symmetry, Phys. Rev. B 75, 045114 (2007),.

[28] H. Jannezhad and M. Jafari, Structural, electronic, and optical properties of C-type $Gd_2O_3$: a density func- tional theory investigation, J. Comput. Electron. 16, 272 (2017).

[29] S. Baroni, S. de Gironcoli, A. Dal Corso, and P. Gi- annozzi, Phonons and related crystal properties from density-functional perturbation theory, Rev. Mod. Phys. 73, 515 (2001),.

[30] A. Togo and I. Tanaka, First principles phonon calcula- tions in materials science, Scripta Mater. 108, 1 (2015).

[31] X. Gonze and C. Lee, Dynamical matrices, Born effective charges, dielectric permittivity tensors, and interatomic force constants from density-functional perturbation the- ory, Phys. Rev. B 55, 10355 (1997),.

[32] V. Wang, N. Xu, J.-C. Liu, G. Tang, and W.-T. Geng, VASPKIT: A user-friendly interface facilitating high- throughput computing and analysis using VASP code, Comput. Phys. Commun. 267, 108033 (2021).

[33] G. J. Martyna, M. L. Klein, and M. Tuckerman, Nosé- Hoover chains: The canonical ensemble via continuous dynamics, J. Chem. Phys. 97, 2635 (1992).

[34] L. Liu, X. Ren, J. Xie, B. Cheng, W. Liu, T. An, H. Qin, and J. Hu, Magnetic switches via electric field in BN nanoribbons, Appl. Surf. Sci. 480, 300 (2019).

[35] A. A. Mostofi, J. R. Yates, Y.-S. Lee, I. Souza, D. Van- derbilt, and N. Marzari, wannier90: A tool for obtaining maximally-localised Wannier functions, Comput. Phys. Commun. 178, 685 (2008).

[36] Q. Wu, S. Zhang, H.-F. Song, M. Troyer, and A. A. Soluyanov, WannierTools: An open-source software package for novel topological materials, Comput. Phys. Commun. 224, 405 (2018).

[37] S.-W. Kim, H.-J. Kim, S. Cheon, and T.-H. Kim, Circular dichroism of emergent chiral stacking orders in quasi-one- dimensional charge density waves, Phys. Rev. Lett. 128, 046401 (2022).

[38] R. Zacharia, H. Ulbricht, and T. Hertel, Interlayer co- hesive energy of graphite from thermal desorption of polyaromatic hydrocarbons, Phys. Rev. B 69, 155406 (2004),.

[39] Q. Chen, R. Wang, Z. Huang, S. Yuan, H. Wang, L. Ma, and J. Wang, Two dimensional $CrGa_2Se_4$: a spin- gapless ferromagnetic semiconductor with inclined uniax- ial anisotropy, Nanoscale 13, 6024 (2021).

[40] S.-D. Guo, J.-X. Zhu, W.-Q. Mu, and B.-G. Liu, Possi- ble way to achieve anomalous valley Hall effect by piezo- electric effect in a $GdCl_2$ monolayer, Phys. Rev. B 104, 224428 (2021).

[41] P. Zhao, Y. Ma, C. Lei, H. Wang, B. Huang, and Y. Dai, Single-layer $LaBr_2$: Two-dimensional valleytronic semi- conductor with spontaneous spin and valley polariza- tions, Appl. Phys. Lett. 115, 261605 (2019).

[42] T. Norden, C. Zhao, P. Zhang, R. Sabirianov, A. Petrou, and H. Zeng, Giant valley splitting in monolayer $WS_2$ by magnetic proximity effect, Nat. Commun. 10, 4163 (2019).

[43] Y. Yao, L. Kleinman, A. H. MacDonald, J. Sinova, T. Jungwirth, D.-s. Wang, E. Wang, and Q. Niu, First Principles Calculation of Anomalous Hall Conductivity in Ferromagnetic bcc Fe, Phys. Rev. Lett. 92, 037204 (2004),.

[44] M. P. L. Sancho, J. M. L. Sancho, J. M. L. Sancho, and J. Rubio, Highly convergent schemes for the calculation of bulk and surface Green functions, J. Phys. F: Metal Phys. 15, 851 (1985).

[45] I. Souza, N. Marzari, and D. Vanderbilt, Maximally lo- calized Wannier functions for entangled energy bands, Phys. Rev. B 65, 035109 (2001),.

[46] D.-s. Wang, R. Wu, and A. J. Freeman, First-principles theory of surface magnetocrystalline anisotropy and the diatomic-pair model, Phys. Rev. B 47, 14932 (1993),.

[47] H. L. Zhuang and R. G. Hennig, Stability and magnetism of strongly correlated single-layer $VS_2$, Phys. Rev. B 93, 054429 (2016).

[48] M. Ashton, D. Gluhovic, S. B. Sinnott, J. Guo, D. A. Stewart, and R. G. Hennig, Two-dimensional intrinsic half-metals with large spin gaps, Nano Lett. 17, 5251 (2017).

[49] K. Sheng, Z.-Y. Wang, H.-K. Yuan, and H. Chen, Two-dimensional hexagonal manganese carbide mono- layer with intrinsic ferromagnetism and half-metallicity, New J. Phys. 22, 103049 (2020).

[50] D. R. Klein, D. MacNeill, J. L. Lado, D. Soriano, E. Navarro-Moratalla, K. Watanabe, T. Taniguchi, S. Manni, P. Canfield, and J. Fernández-Rossier, Prob- ing magnetism in 2D van der Waals crystalline insulators via electron tunneling, Science 360, 1218 (2018).

[51] J. B. Goodenough, Theory of the Role of Covalence in the Perovskite-Type Manganites [La, $M$(II)]MnO₃, Phys. Rev. 100, 564 (1955),.

[52] J. Kanamori, Crystal distortion in magnetic compounds, J. Appl. Phys. 31, S14 (1960).

[53] P. W. Anderson, New approach to the theory of superex- change interactions, Phys. Rev. 115, 2 (1959).

[54] D. J. Thouless, M. Kohmoto, M. P. Nightingale, and M. den Nijs, Quantized Hall Conductance in a Two- Dimensional Periodic Potential, Phys. Rev. Lett. 49, 405 (1982),.

[55] D. Xiao, G.-B. Liu, W. Feng, X. Xu, and W. Yao, Cou- pled Spin and Valley Physics in Monolayers of $MoS_2$ and Other Group-VI Dichalcogenides, Phys. Rev. Lett. 108, 196802 (2012),.

[56] D. Xiao, M.-C. Chang, and Q. Niu, Berry phase effects on electronic properties, Rev. Mod. Phys. 82, 1959 (2010),.

[57] T. Cai, S. A. Yang, X. Li, F. Zhang, J. Shi, W. Yao, and Q. Niu, Magnetic control of the valley degree of freedom of massive Dirac fermions with application to transition metal dichalcogenides, Phys. Rev. B 88, 115140 (2013),.

— Supporting Information —

Two-dimensional ferromagnetic semiconductors of rare-earth Janus 2H-GdIBr
monolayer with large valley polarization

Cunquan Li¹, Yukai An¹,*

¹ Key Laboratory of Display Materials and Photoelectric Devices,
Ministry of Education, Tianjin Key Laboratory for Photoelectric Materials and Devices,
National Demonstration Center for Experimental Function Materials Education,
School of Material Science and Engineering, Tianjin University of Technology, Tianjin, 300384, China

![](./images/867768896369721392_7.jpg)

FIG. S1. Spin density of 2×2×1 Janus 2H-GdIBr monolayer for different magnetic configurations. Yellow (blue) color refers
to the spin up (down) charge density. The isosurface is 0.0094 e/Born³.

![](./images/867768896369721392_8.jpg)

FIG. S2. (a) Strain and (b) charge carrier dependence of the energy in FM and AFM states for the 2×2×1 Janus 2H-GdIBr monolayer.

![](./images/867768896369721392_9.jpg)

FIG. S3. The spin-resolved PDOSs of Janus 2H-GdIBr monolayer.

![](./images/867768896369721392_10.jpg)

FIG. S4. Projected band structure of Gd-$d$ orbitals for the Janus 2H-GdIBr monolayer with SOC. The Fermi level is set to zero.

![](./images/867768896369721392_11.jpg)

FIG. S5. (a) 3D band structure as well as the 2D projected band structure of (b) CBM and (c) VBM at the $k_x$$k_y$-plane for the Janus 2H-GdIBr monolayer with considering SOC. The different colors in color bar show different iso-values. The blue and red color correspond to the smallest and largest energy values, respectively.

![](./images/867768896369721392_12.jpg)

FIG. S6. Br-p orbital resolved MAEs for the Janus 2H-GdIBr monolayer at the strains of $-6\%$, $0\%$ and $6\%$.

![](./images/867768896369721392_13.jpg)

FIG. S7. Nearly linear evolution of the internal energy per unit cell in the original 16×16 superlattice of spins (red) and the renormalized 32×32 superlattice of quasi-particles (blue). Lines are only to guide the eye.

![](./images/867768896369721392_14.jpg)

FIG. S8. Dependences of exchange parameter $J$ on (a) biaxial strain and (b) charge carrier doping for the Janus 2H-GdIBr monolayer. Dependences of (c) magnetic moment and (d) heat capacity on the temperature for the Janus 2H-GdIBr monolayer at the strains of $\pm8\%$ and with carrier concentration of $\pm0.3$e per.u.

![](./images/867768896369721392_15.jpg)

FIG. S9. The band structures Janus 2H-GdIBr monolayer with (a) 0.05 holes and (b) 0.05 electrons doping. The Fermi level is set to zero.

![](./images/867768896369721392_16.jpg)

FIG. S10. The circular polarization $\eta(\mathbf{k})$ of the optical transition between the VBM and CBM in the first Brillouin zone.