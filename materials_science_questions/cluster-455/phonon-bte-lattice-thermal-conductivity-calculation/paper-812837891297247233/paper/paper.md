# Odd-even phonon transport effects in strained carbon atomic chains bridging graphene nanoribbon electrodes

Hu Sung Kim, Tae Hyung Kim, Yong-Hoon Kim*

School of Electrical Engineering and Graduate School of EEWS, Korea Advanced Institute of Science and Technology (KAIST), 291 Daehak-ro, Yuseong-gu, Daejeon, 305-701, South Korea

---

## A R T I C L E I N F O

**Article history:**
Received 9 July 2018
Received in revised form
4 October 2018
Accepted 10 October 2018
Available online 12 October 2018

## A B S T R A C T

Based on first-principles approaches, we study the ballistic phonon transport characteristics of finite monatomic carbon chains stretched between graphene nanoribbons, an $sp^1$-$sp^2$ hybrid carbon nanostructure that has recently seen significant experimental advances in its synthesis. We find that the lattice thermal conductance anomalously increases with tensile strain for the even-numbered carbon chains that adopt the alternating bond-length polyyne configuration. On the other hand, in the odd-numbered carbon chain cases, which assume the equal bond-length cumulene configuration, phonon conductance decreases with increasing strain. We show that the strong odd-even phonon transport effects originate from the characteristic longitudinal acoustic phonon modes of carbon wires and their unique strain-induced redshifts with respect to graphene nanoribbon phonon modes. The novel phonon transport properties and their atomistic mechanisms revealed in this work will provide valuable guidelines in designing hybrid carbon nanostructures for next-generation device applications such as nano-biosensors.

© 2018 Elsevier Ltd. All rights reserved.

---

## 1. Introduction

Representing the ideal one-dimensional (1D) $sp^1$-hybridized carbon systems, monatomic carbon chains (CCs) were predicted to exhibit intriguing physical and chemical properties but their experimental investigations have been relatively slow compared to other $sp^2$-and $sp^3$-carbon allotropes [1–4]. While the infinite CC or carbyne is not yet observed and its existence still remains controversial, much progress has been recently made in the experimental realization of finite CC systems. An interesting aspect of this development is that, rather than the direct synthesis of isolated molecular CCs [5,6], they were successfully prepared in the $sp^1$-$sp^2$ hybrid carbon structures. A notable case is the CC confined within carbon nanotubes [7,8], and the other is the CC stretched between graphene [9–17].

In particular, the graphene–CC–graphene system assumes an ideal electrode-channel-electrode junction configuration [9–18], providing unique opportunities to study the quantum transport properties of all-carbon nanodevices. The infinite CCs can adopt cumulene ( … $C{=}C{=}C{=}C$ …) or polyyne ( … $C{\equiv}C$-$C{\equiv}C$ …) configuration (Fig. 1a) and exhibit metallic or semiconducting properties, respectively [3,4]. In a notable example, very recently, strain-induced metal-to-insulator (i.e. cumulene-to-polyyne) transition was observed [14], confirming a recent theoretical prediction [19]. Another promising example theoretically suggested is spintronic applications such as spin filter and spin valve, which will be operated based on the spin-polarized nature of graphene zigzag edge states and can be modulated by the number of carbon atoms within CCs (cumulene or polyyne) [20–22].

In this work, applying an atomistic Green's function method (AGF) based on density functional theory (DFT) calculations, we investigate the strain-dependent ballistic phonon transport properties of CCs bridging graphene nanoribbon (GNR) electrodes (Fig. 1b). Although several theoretical reports on the charge and spin transport properties of GNR–CC–GNR junctions have previously appeared [20–24], study on their phonon transport properties is non-existent [25]. More generally, while ballistic electron and spin transports in nanoscale junctions have been extensively studied in the past decade or so, still much less is known about their ballistic phononic heat transport [26,27]. We here adopt the microscopic AGF theory to describe the thermal resistance across the dimensionally mismatched $sp^1$-$sp^2$ interfaces [28–30]. Moreover, in spite of the high computational cost, we will utilize first-

* Corresponding author.
E-mail address: y.h.kim@kaist.ac.kr (Y.-H. Kim).

https://doi.org/10.1016/j.carbon.2018.10.036
0008-6223/© 2018 Elsevier Ltd. All rights reserved.

![](./images/812837891297247233_1.jpg)

Fig. 1. Atomic structures of DFT-optimized (a) polyyne (upper) and cumulene (lower), and (b) 4zGNR and 7aGNR. Schematics of GNR-CC-GNR junction contacts are shown together. Here, the red rectangles represent the primitive unit cells. (c) The bond lengths of the finite CC parts within the GNR-CC-GNR junction models are mapped to the bond lengths of infinite polyyne (solid lines) and cumulene (dotted line) at varying strain. Circles (squares) represent 4zGNR (7aGNR) cases. (d) The BLA values of even-numbered CC junctions mapped onto the infinite polyyne BLA values at varying strain. For the junction models, the bond length and BLA values are measured for the innermost carbon atoms. (A colour version of this figure can be viewed online.)

principles atomics forces obtained through DFT because it was shown in a previous study that classical force fields significantly overestimate phonon transmissions across GNR-atomic carbon contacts [25].

In examining the ballistic phonon transport properties of various GNR-CC-GNR junction models, we particularly focus on the effects of tensile strain as well as the number of carbon atoms within CCs. Strain was predicted to be an important variable that affects the structural and electronic properties of infinite [31-33] as well as finite CCs [14,18,19,24,32,34]. Regarding the number of C atoms within finite CCs, while strong odd-even effects were pre- dicted for the structural and electron transport properties of GNR-CC-GNR [20,23,24,34] as well as metal-CC-metal junctions [35], it remains to be seen whether an oscillatory behavior also appears in phonon transport and if does what its nature is. We will show that a strong strain-dependent odd-even phonon transport effect indeed arises because phonon conductances in the even- numbered (odd-numbered) CC junctions increase (decrease) with tensile strain. The effect is found in both armchair and zigzag GNRs, indicating the robust nature of the effect. The microscopic mech- anisms will be rationalized by the polyynic atomic structure of even-numbered CCs and the strong redshifting behavior of their longitudinal optical (LO) modes with respect to GNR phonon bands.

## 2. Computational method
### 2.1. Density-functional theory phonon calculations

Following our earlier works on stretched molecular junctions [36,37], we carried out strain-dependent geometry optimizations within the local density approximation (LDA) of DFT implemented in the SIESTA package [38]. Dynamical matrices were obtained with the DFT forces and the small displacement method as implemented in the Phonopy code [39]. Norm-conserving pseudopotentials and double-zeta-plus-polarization quality atomic orbital basis sets were adopted. The convergence criterion for atomic forces was set to $10^{-3}$ eV/Å.

### 2.2. Quantum phonon transport calculations

For the computation of ballistic phonon transport properties, we used an in-house code that implements the atomistic matrix Green's function (MGF) formalism [25,28-30,40,41] and was developed based on our electronic MGF code [36,42,43]. We are concerned with the linear response limit, or when the difference of the electrode 1/2 temperature $T_{1/2}$ is very small, $T_{1}-T_{2} \ll T \equiv (T_{1}+T_{2})/2$. Then, after computing the phonon transmission function,

$$
T_{\mathrm{ph}}(\omega)=\operatorname{Tr}\left[\boldsymbol{\Gamma}_{1}(\omega) \mathbf{G}(\omega) \boldsymbol{\Gamma}_{2}(\omega) \mathbf{G}^{+}(\omega)\right], \tag{1}
$$

where $\mathbf{G}$ is the retarded Green's function matrix of the channel region and $\boldsymbol{\Gamma}_{1/2}$ is the broadening matrix resulting from the coupling of the channel with the electrode 1/2, we calculated the lattice thermal conductance according to

$$
K_{\mathrm{ph}}(T)=\int_{0}^{\infty} \frac{d \omega}{2 \pi} \hbar \omega T(\omega) \frac{\partial n}{\partial T}, \tag{2}
$$

where $n=\left[\exp (\hbar \omega / k_{B} T)-1\right]^{-1}$ is the Bose-Einstein distribution function.

## 3. Results and discussion

### 3.1. Phononic heat transport in infinite CCs

We first discuss the strain-dependent variations in the lattice thermal transport properties of infinite CCs (carbyne) and GNRs, which become the basis of analyzing the phonon transport in GNR-CC-GNR junctions. In terms of the atomic structures of infinite carbynes, we obtained within LDA 1.269 Å (1.301 Å) as the $C\equiv C$ (C-C) bond length in the polyyne form and 1.285 Å as the $C\equiv$ C bond length in the cumulene counterpart (Fig. 1a). Due to Peierls distortion that drives the bond-length alternation and associated opening of a bandgap [31-33], the polyyne structure should be energetically more stable than the cumulene counterpart and within our calculations the energy difference between the two was of 1.12 meV per carbon atom. As the GNR electrodes, we adopted the hydrogen-passivated four zigzag-chain zigzag GNR (4zGNR) and seven dimer-line armchair GNR (7aGNR) with the optimized widths of 9.31 Å and 9.27 Å, respectively (unit cell lattice constants of 2.46 Å and 4.26 Å, respectively) (Fig. 1b) [44,45]. Note that these dimensions are comparable to those of atomically precise narrow GNRs that have recently became available through the bottom-up synthesis techniques [46].

Upon applying tensile strains, we find for the polyene case that the long C-C bond length increases faster than the short C-C bond length, or the preference for the polyyne configuration is enhanced with strain (Fig. 1c) [32,33]. Quantifying the degree of polyynicity using the bond-length alternation (BLA) value, defined as the difference between short $C\equiv C$ and long C-C bond lengths, we find that BLA increases from 0.032 Å to 0.130 Å and to 0.207 Å as the tensile strain increases from 0% to 8% and to 12% (Fig. 1d). The Peierls instability manifested in BLA is underestimated within LDA, which incorrectly overestimates the tendency of electron delocalization due to its self-interaction error, and the deficiency could be corrected by employing more elaborate hybrid DFT functionals. However, such calculations are prohibitive for the large GNR-C-C-GNR junction models, and more importantly one can expect that the qualitative conclusions based on LDA or generalized gradient approximation will not be modified by employing hybrid functionals [19,32]. Considering the increasing Peierls distortion and strain effects within hybrid functionals, we expect that the strain-dependent odd-even effects for the GNR-CC-GNR junctions reported below will become more prominent in experimental situations.

In Fig. 2, we summarize the characteristics of strain-dependent phonon properties of infinite CCs as well as 4zGNR. Analyzing the spatial decay of dynamical matrix elements (Fig. 2a upper panels), the force interaction range in CCs is found to be much longer than that in 4zGNRs. Particularly, we observe that the interaction is extremely long-ranged for the cumulene chain, obtaining over the $10^{-2}$ eVÅ$^{-2}$amu$^{-1}$ level values for the off-diagonal dynamical matrix elements even at the 150 Å distance compared with the drop to the $10^{-4}$ eVÅ$^{-2}$amu$^{-1}$ level at about 70 Å (15 Å) for the polyyne (4zGNR) counterpart. These characteristics show up in the phonon band structures of the cumulene chain as a Kohn anomaly (over bending of the longitudinal acoustic (LA) phonon dispersion and the phonon softening) at the $\Gamma$ point of the polyyne Brillouin zone (or the zone boundary at the cumulene Brillouin zone, Fig. 2b).

On the other hand, in the polyyne case, Peierls distortion opens a gap between the LA and LO branches at the zone boundary X point. (Fig. 2a) [3,47,48]. The frequency ranges of infinite polyyne and cumulene phonon modes are extended up to about 2250 cm$^{-1}$ (Fig. 2a middle panels, dotted lines) and 2240 cm$^{-1}$ (Fig. 2b middle panels, dotted lines), respectively, within our calculations, and these high-frequency phonon modes are the sources of experimentally observed Raman signals in the 1800-2300 cm$^{-1}$ spectral region [49,50]. Note that no other carbon nanostructure have Raman peaks in this region, so they become the characteristic feature of $sp^1$-hybridized carbons [3].

In terms of thermal transmissions and conductance, we find that the Kohn anomaly-related features result in $T_{\rm ph}(\omega)$ of cumulene larger than that of polyyne over some frequency ranges (particularly up to ~1200 cm$^{-1}$; Fig. 2a and b middle right panels, dotted lines) and thus the $K_{\rm ph}(T)$ values of cumulene enhanced over those of polyyne (Fig. 2a and b lower panels, dotted lines). Here, note that the LO mode of unstrained polyyne at $\Gamma$ is found at a rather low frequency region (~1250 cm$^{-1}$) due to the employment of LDA that overestimates the $\pi$-electron conjugation [47,48]. Upon upshifting this mode by, e.g. employing a hybrid DFT functional [19,32], as discussed above, the difference between polyyne and cumulene $K_{\rm ph}(T)$ values will be increased. Furthermore, we emphasize that such LDA-derived deficiency will not qualitatively affect our main conclusions concerning the high-frequency (~2250 cm$^{-1}$ in the unstrained case) CC LO modes within the GNR-CC-GNR junction setting.

Next, applying tensile strains on the polyyne chain, we find that the short triple bond length relatively remains constant while the long single bond length linearly increases (Fig. 1c). The large strain-induced decrease in force constants of alternating single bonds results in significant redshifts of LA and LO modes and corresponding reduction of high-frequency range $T_{\rm ph}(\omega)$ (Fig. 2a middle panels, dot-dahsed and solid lines), resulting in the decrease of $K_{\rm ph}(T)$ by ~38% with 12% strain at 300 K (Fig. 2a lower panels, dot-dahsed and solid lines). For the cumulene case, we again observe a large-scale redshift of $T_{\rm ph}(\omega)$ corresponding to the LA mode in the high-frequency region, and it in turn results in a ~27% reduction of $K_{\rm ph}(T)$ with 12% strain at 300 K (Fig. 2b, dot-dahsed and solid lines). We note that two recent studies based on force-fields molecular dynamics simulations provided contradicting predictions on the behavior of thermal conductance in infinite CCs under tensile strain, and it appears that the strain-induced thermal conductance increase can result from the restrictions introduced in the force fields (overestimation of axial stiffness or underestimation of the role of flexural modes) [51,52]. Our first-principles atomistic MGF-based results support the decreasing phononic thermal conductance in infinite CCs with increasing tensile strain, which is more in line with the general trend obtained for infinite carbon nanotubes and GNRs [41,53,54].

For the cases of 4zGNR (Fig. 2c) and 7aGNR (Data in Brief Fig. D1), the frequency ranges of their phonons reaching up to ~1680 cm$^{-1}$ and ~1690 cm$^{-1}$, respectively, are lower than those of CCs extending up to ~2250 cm$^{-1}$. Moreover, due to the structural rigidity of the hexagonal arrangement of $sp^2$ carbon atoms, the degree of strain-induced phonon band flattening or redshift of high-frequency $T_{\rm ph}(\omega)$ is smaller for GNRs, amounting to the $K_{\rm ph}(T)$ reductions of ~14% and ~11% in the 4zGNR and 7aGNR, respectively.

### 3.2. Phononic heat transport in GNR-CC-GNR junctions

We now move on to consider the phonon transport properties of CCs stretched between two GNR electrodes, which is the main focus of this work. Different from the infinite carbyne limit, the ideal case where Peierls distortion could be rigorously defined, the structural and electronic properties of finite CCs such as BLA, electronic band gap, and vibrational properties are strongly affected by the length and termination of CCs [3,19,32,34,55]. Inserting several odd- and even-numbered CCs between 4zGNR or 7aGNR electrodes, we first prepared a series of GNR-CC-GNR junction models (Fig. 1b). Each junction model was once more optimized with DFT and then its dynamical matrices were calculated to extract coherent phonon

![](./images/812837891297247233_2.jpg)

Fig. 2. Density plots of the dynamical matrices (upper panels), strain-dependent phonon band structures (middle left panels), phonon transmissions (middle right panels), and thermal conductance (lower panels) of (a) polyyne, (b) cumulene, and (c) 4zGNR. For the density plots, left and right panels are from 0% to 8% strain conditions, respectively. Each axis represents the number of unit cells (UCs). The magnitude of matrix elements are given in the units of eVÅ⁻²amu⁻¹. For the polyyne and cumulene cases, black dashed, green dash-dot, and red solid lines represent the 0, 8, and 12% strain conditions, respectively. For the zGNR case, black dashed and green solid lines represent the 0 and 8% strain conditions, respectively. (A colour version of this figure can be viewed online.)

transport properties. For the strained junction models, the electrode-region GNRs were stretched by $\Delta L=0.8$ Å and once again the DFT-phonon MGF calculations were repeated. More computa- tional details can be found in the Computational method section and Data in Brief Fig. D2.

The results summarized in Fig. 3 strikingly show that we obtain the opposite strain-induced $K_{\text{ph}}(T)$ variation trends for the even- numbered and odd-numbered CCs (Fig. 3a). There already exists a weak oscillatory behaivor of $K_{\text{ph}}$ in the unstrained condition, and with tensile strain this oscillation is amplified and more interest- ingly shows an opposite-direction oscillation trend (Fig. 3b). The strong odd-even effect becomes a robust feature at $T>\sim100$ K and is observed for varying number of carbon atoms $(N_{C})$ as well as for both 4zGNR and 7aGNR electrode cases, indicating its robustness and universality in the GNR-CC-GNR junction configuration. The overall reduction of $K_{\text{ph}}$ in junction models compared with that in infinite carbynes can be understood in view of the introduction of two GNR-CC $sp^{2}$-$sp^{1}$ contacts, which will result in the (dimensional) mismatch between GNR and CC phonon modes [25,40]. In addition, considering the reduction of $K_{\text{ph}}$ with increasing tensile strain in carbynes and GNRs (Fig. 2), the strain-induced $K_{\text{ph}}$ reduction in odd-numbered CC is reasonable. On the other hand, the strain- induced enhancement of $K_{\text{ph}}$ in even-numbered CC cases cannot be understood using the infinite carbyne data, implying it originates from the unique interactions between finite-CC and GNR phonons. Before discussing the details further, we mention that the anomalous strain-induced conductance increase in even- numbered CCs was not observed when the GNR electrodes were replaced by graphene (see Data in Brief Fig. D3). This indicates that the presence of GNR edges plays an important role in generating the observed behavior, and suggests the GNR width dependence as an interesting future study.

To explain the microscopic mechanisms of the strain-induced increase (decrease) in $K_{\text{ph}}(T)$ for even-numbered (odd-numbered) CC junctions, we analyzed the atomic structures, phonon trans- missions, and projected density of states (PDOS) at the unstrained and strained conditions shown in Fig. 4. Note that as shown in Fig. 5 we obtain essentially identical results for the 7aGNR case. To begin with, observing the optimized atomic structures of GNR-CC-GNR junctions in detail (see Data in Brief Figs. D4 and D5), we find that the even-numbered (odd-numbered) CCs stretched between GNRs adopt the alternated polyyne-like (equalized cumulene-like) structures. In addition, compared with the infinite carbyne limits, we observe that the finite CCs in junction models are in effectively strained conditions (Fig. 1c and d). This is a natural consequence of the termination of a finite CC by $sp^{2}$ GNRs, which as in finite mo- lecular CC cases, results in overall enhanced BLAs [55]. Observing the optimized GNR-CC-GNR junction geometries more closely

![](./images/812837891297247233_3.jpg)

Fig. 3. Strain-dependent (a) lattice thermal conductances of the representative GNR-CC-GNR junction models. Black dotted and blue solid lines represent the unstrained (dashed lines) and strained (solid lines) conditions, respectively. Effective strain values for the innermost carbon atoms in reference to infinite polyyne and cumulene structures are given for the even-numbered and odd-numbered CC cases, respectively. (b) Compilations of strain-dependent lattice thermal conductance with different number of carbon atoms for the 4zGNR (left) and 7aGNR (right) cases. Black dotted and solid lines represent the unstrained and strained conditions, respectively. (A colour version of this figure can be viewed online.)

(Figs. S4 and S5), we find that the BLA values are nonuniform across CC and the BLAs in the CC boundaries are larger than those in the middle CC region [19,32]. Moreover, due to the differences in their structural rigidity, we find that the effective strain induced onto the GNR regions is relatively negligible compare to that of CCs.

Scrutinizing the strain-dependent $T_{\rm ph}(\omega)$ spectra of eight-carbon (8C) wire bridging 4zGNR electrodes, while there appear strain-induced enhancement and reduction of $T_{\rm ph}$ throughout all $\omega$ ranges (see Data in Brief Fig. D6 for more detailed analysis of changes in $T_{\rm ph}$ that lead to the enhanced $K_{\rm ph}$), we identify the enhancement of $T_{\rm ph}$ values at $\omega \approx 1300 - 1500\ \rm cm^{-1}$ as the most consistent and notable change (Fig. 4a, blue down arrows). On the other hand, such $T_{\rm ph}$ enhancement at $\omega \approx 1500\ \rm cm^{-1}$ is absent for the seven-carbon (7C) chain case (Fig. 4b), explaining the strong strain-induced odd-even effects in $K_{\rm ph}(T)$ of GNR-CC-GNR junctions. The origins of different strain-induced $T_{\rm ph}(\omega)$ changes in the ~1500 cm⁻¹ frequency region can be understood by analyzing the phonon PDOS projected onto CCs. As emphasized earlier, the high-frequency LO phonon modes of polyyne chains are discriminated from those of other carbon-based nanostructures [3], and particularly they are strongly redshifted with increasing tensile strain (Fig. 2). Although the 8C chain within the unstrained junction is in an effectively strained state with reference to the infinite polyyne case (5.8% in terms of the bond lengths of central carbon atoms), the 8C chain LO mode is still located above the 4zGNR phonon states (Fig. 4a, upper panels). However, upon applying additional strain to the 4zGNR-8C-4zGNR junction, the 8C chain LO mode is further redshifted, making the spectral ranges of the 8C chain and 4zGNR phonons overlap with each other and accordingly increasing $T_{\rm ph}(\omega)$ at $\omega \approx 1500\ \rm cm^{-1}$ significantly (Fig. 4a, lower panels).

The spatially well-delocalized nature is a necessary condition for a transmission eigenmode to support efficient quantum transport, and the visualization of eigenstates of the molecular projected Hamiltonian has well established such a criterion in the electron quantum transport case [56,57]. In a similar spirit, we visualized the vibrational modes (phonon local PDOS) corresponding to the enhanced transmission peak at $\omega \approx 1490\ \rm cm^{-1}$ in the unstrained and strained 8C junction cases, and they indeed clearly show the absence and activation of CC phonon modes in the former and latter cases, respectively (Fig. 4a, right panels). For the 7C chain case, on the other hand, such strain-induced transition behavior is less noticeable (Fig. 4b, right panels). The 7C chain mode at $\omega \approx 1490\ \rm cm^{-1}$ is already activated within the unstrained 4zGNR-

![](./images/812837891297247233_4.jpg)

Fig. 4. Phonon transmissions (left upper panels), vibrational PDOS (left lower panels), and local phonon modes (right panels) at $\omega \approx 1490\ \text{cm}^{-1}$ in the (a) 4zGNR-8C-4zGNR and (b) 4zGNR-7C-4zGNR junction models for the unstrained (upper panels) and strained (lower panels) conditions. Effective strain values for the innermost CC atoms in reference to infinite polyyne and cumulene structures are given for the 8C and 7C cases, respectively. In the phonon PDOS red and grey lines represent the CC and GNR PDOS, respectively. In the transmission and PDOS data, blue down arrows indicate the frequency where local phonon mode is visualized ($\omega \approx 1490\ \text{cm}^{-1}$). In the local phonon mode plots, black arrows represent the in-plane vibrational directions of each atom. (A colour version of this figure can be viewed online.)

![](./images/812837891297247233_5.jpg)

Fig. 5. Phonon transmissions, vibrational PDOS, and real-space visualizations of $\omega \approx 1490\ \text{cm}^{-1}$ phonon modes in the (a) 7aGNR-6C-7aGNR and (b) 7aGNR-5C-7aGNR junction models for the unstrained (upper panels) and strained (lower panels) conditions. Effective strain values for the innermost CC atoms in reference to infinite polyyne and cumulene structures are given for the 6C and 5C cases, respectively. Red and grey filled lines in the PDOS plots represent the PDOS of CC and GNR parts, respectively. Blue down arrows indicate the frequency near $\omega \approx 1490\ \text{cm}^{-1}$. In the local phonon mode plots, black arrows represent the in-plane vibrational directions of each atom. (A colour version of this figure can be viewed online.)

8C-4zGNR junction configuration, and correspondingly the trans- mission and CC PDOS peaks are present in Fig. 4b upper left panels. Such difference between even- and odd-number CC cases can be simplistically understood in terms of the slightly more strained condition for the odd-numbered CCs with reference to the infinite cumulene limit (6.5% in terms of the bond lengths of central carbon atoms). However, more detailed analysis indicates that odd- numbered CC cases correspond to a complex situation where the mapping to cumulene is not strictly valid (e.g. the C-C bonds adjacent to GNRs are single-bonded rather than double-bonded; see Data in Brief Figs. D4 and D5), and we believe it deserves more close examinations in combination with the electronic structures of different $sp^{1}$-$sp^{2}$ contacts in the future [17,34].

## 4. Conclusions

In summary, we carried out $ab$ initio phonon transport calcula- tions on finite monatomic CCs stretched between GNR electrodes. Representing the ultimate all-carbon junction model, these hybrid carbon nanostructures based on $sp$-$sp^{2}$ interfaces are appealing in many aspects but the research efforts have been so far limited to their structural and electronic (and spin) transport properties. Systematically considering a series of CC channels and both zGNR and aGNR electrodes, we found that the phonon conductance of the $sp$-$sp^{2}$ hybrid structures exhibits strong odd-even oscillations. Specifically, while odd-numbered CCs adopted the cumulenic structure and showed the phonon conductance decrease with increasing tensile strain, even-numbered CCs assumed the polyynic configuration and anomalously showed the strain-induced conductance increase. The strong odd-even ballistic phonon transport effects were rationalized in terms of the strain- dependent behavior of polyyne LO phonon modes, which are characteristic to $sp$-hybridized CCs and exhibit stronger redshifts than the high-frequency phonon modes of $sp^{2}$ carbons in GNRs. The strong strain-induced odd-even phonon transport effects could open up new opportunities in advanced nano-device applications, e.g., bio-sensors detecting strain change induced by the adsorption of DNA on CCs [58,59].

## Acknowledgement

This work was supported by the Nano-Material Technology Development Program (Nos. 2016M3A7B4024133 and 2016M3A7B4909944), Basic Research Program (No. 2017R1A2B3009872), Global Frontier Program (No. 2013M3A6B1078881), and Basic Research Lab Program (No. 2016M3A7B4909944) of the National Research Foundation funded by the Ministry of Science and ICT of Korea. Computational re- sources were provided by the KISTI Supercomputing Center (KSC-2016-C3-0076).

## References

[1] R.B. Heimann, S.E. Evsukov, Y. Koga, Carbon allotropes: a suggested classi- fication scheme based on valence orbital hybridization, Carbon 35 (10-11)(1997) 1654-1658.
[2] A. Hirsch, The era of carbon allotropes, Nat. Mater. 9 (11) (2010) 868-871.
[3] C.S. Casari, M. Tommasini, R.R. Tykwinski, A. Milani, Carbon-atom wires: 1-D systems with tunable properties, Nanoscale 8 (2016) 4414-4435.
[4] F. Banhart, Chains of carbon atoms: a vision or a new nanomaterial? Beilstein J. Nanotechnol. 6 (2015) 559-569.
[5] W.A. Chalifoux, R.R. Tykwinski, Synthesis of polyynes to model the sp-carbon allotrope carbyne, Nat. Chem. 2 (11) (2010) 967-971.
[6] J.A. Januszewski, R.R. Tykwinski, Synthesis and properties of long [n]cumu- lenes (n ≥ 5), Chem. Soc. Rev. 43 (9) (2014) 3184-3203.
[7] X. Zhao, Y. Ando, Y. Liu, M. Jinno, T. Suzuki, Carbon nanowire made of a long linear carbon chain inserted inside a multiwalled carbon nanotube, Phys. Rev. Lett. 90 (18) (2004) 187401.
[8] L. Shi, P. Rohringer, K. Suenaga, Y. Niimi, J. Kotakoski, J.C. Meyer, H. Peterlik, M. Wanko, S. Cahangirov, A. Rubio, Z.J. Lapin, L. Novotny, P. Ayala, T. Pichler, Confined linear carbon chains as a route to bulk carbyne, Nat. Mater. 15 (6)(2016)634-639.
[9] B. Standley, W. Bao, H. Zhang, J. Bruck, C.N. Lau, M. Bockrath, Graphene-based atomic-scale switches, Nano Lett. 8 (2008) 3345-3349.
[10] C. Jin, H. Lan, L. Peng, K. Suenaga, S. lijima, Deriving carbon atomic chains from graphene, Phys. Rev. Lett. 102 (2009) 205501.
[11] A. Chuviilin, J.C. Meyer, G. Algara-Siller, U. Kaiser, Deriving from graphene constrictions to single carbon chains, New J. Phys. 11 (2009), 083019.
[12] H. Zhang, W. Bao, Z. Zhao, J.W. Huang, B. Standley, G. Liu, F. Wang, P. Kratz, L. Jing, M. Bockrath, C.N. Lau, Visualizing electrical breakdown and ON/OFF states in electrically switchable suspended graphene break junctions, Nano Lett. 12 (2012) 1772-1775.
[13] G. Casillas, A. Mayoral, M. Liu, A. Ponce, V.I. Artyukhov, B.I. Yakobson, M. Jose- Yacaman, New insights into the properties and interactions of carbon chains as revealed by HRTEM and DFT analysis, Carbon 66 (2014) 436-441.
[14] A. La Torre, A. Botello-Mendez, W. Baaziz, J.C. Charlier, F. Banhart, Strain- induced metal-semiconductor transition observed in atomic carbon chains, Nat. Commun. 6 (2015) 6636.
[15] S.G. Sarwat, P. Gehring, G. Rodriguez Hernandez, J.H. Warner, G.A.D. Briggs, J.A. Mol, H. Bhaskaran, Scaling limits of graphene nanoelectrodes, Nano Lett.17 (2017) 3688-3693.
[16] Y.C. Lin, S. Morishita, M. Koshino, C.H. Yeh, P.Y. Teng, P.W. Chiu, H. Sawada, K. Suenaga, Unexpected huge dimerization ratio in one-dimensional carbon atomic chains, Nano Lett. 17 (2017) 494-500.
[17] F. Ben Romdhane, J.-J. Adjizian, J.-C. Charlier, F. Banhart, Electrical transport through atomic carbon chains: the role of contacts, Carbon 122 (2017) 92-97.
[18] O. Cretu, A.R. Botello-Mendez, I. Janowska, C. Pham-Huu, J.C. Charlier, F. Banhart, Electrical transport measured in atomic carbon chains, Nano Lett.13 (2013) 3487-3493.
[19] V.I. Artyukhov, M. Liu, B.I. Yakobson, Mechanically induced metal-insulator transition in carbyne, Nano Lett. 14 (2014) 4224-4229.
[20] Z. Zanolli, G. Onida, J.C. Charlier, Quantum spin transport in carbon chains, ACS Nano 4 (2010) 5174-5180.
[21] J.A. Fürst, M. Brandbyge, A.P. Jauho, Atomic carbon chains as spin- transmitters: an ab initio transport study, EPL-Europhys Lett 91 (2010), 37002.
[22] M.G. Zeng, L. Shen, Y.Q. Cai, Z.D. Sha, Y.P. Feng, Perfect spin-filter and spin- valve in carbon atomic chains, Appl. Phys. Lett. 96 (2010), 042104.
[23] L. Shen, M. Zeng, S.W. Yang, C. Zhang, X. Wang, Y. Feng, Electron transport properties of atomic carbon nanowires between graphene electrodes, J. Am. Chem. Soc. 132 (2010) 11481-11486.
[24] B. Akdim, R. Pachter, Switching behavior of carbon chains bridging graphene nanoribbons: effects of uniaxial strain, ACS Nano 5 (2011) 1769-1774.
[25] B.K. Nikolic, K.K. Saha, T. Markussen, K.S. Thygesen, First-principles quantum transport modeling of thermoelectricity in single-molecule nanojunctions with graphene nanoribbon electrodes, J. Comput. Electron. 11 (2012) 78-92.
[26] Y. Dubi, M. Di Ventra, Colloquium: heat flow and thermoelectricity in atomic and molecular junctions, Rev. Mod. Phys. 83 (2011) 131-155.
[27] N. Li, J. Ren, L. Wang, G. Zhang, P. Hänggi, B. Li, Colloquium: phononics: Manipulating heat flow with electronic analogs and beyond, Rev. Mod. Phys.84 (2012) 1045-1066.
[28] N. Mingo, L. Yang, Phonon transport in nanowires coated with an amorphous material: an atomistic Green's function approach, Phys. Rev. B 68 (2003),245406.
[29] T. Yamamoto, K. Watanabe, Nonequilibrium Green's function approach to phonon transport in defective carbon nanotubes, Phys. Rev. Lett. 96 (2006),255503.
[30] J.-S. Wang, J. Wang, N. Zeng, Nonequilibrium Green's function approach to mesoscopic thermal transport, Phys. Rev. B 74 (2006), 033408.
[31] S. Tongay, R.T. Senger, S. Dag, S. Ciraci, Ab-initio electron transport calcula- tions of carbon based string structures, Phys. Rev. Lett. 93 (2004), 136404.
[32] S. Cahangirov, M. Topsakal, S. Ciraci, Long-range interactions in carbon atomic chains, Phys. Rev. B 82 (2010), 195444.
[33] M. Liu, V.I. Artyukhov, H. Lee, F. Xu, B.I. Yakobson, Carbyne from first princi- ples: chain of C atoms, a nanorod or a nanorope, ACS Nano 7 (2013)10075-10082.
[34] L. Ravagnan, N. Manini, E. Cinquanta, G. Onida, D. Sangalli, C. Motta, M. Devetta, A. Bordoni, P. Piseri, P. Milani, Effect of axial torsion on sp carbon atomic wires, Phys. Rev. Lett. 102 (2009) 245502.
[35] N.D. Lang, P. Avouris, Oscillatory conductance of carbon-atom wires, Phys. Rev. Lett. 81 (16)(1998) 3515-3518.
[36] Y.-H. Kim, Toward numerically accurate first-principles calculations of nano- device charge transport characteristics: the case of alkane single-molecule junctions, J. Kor. Phys. Soc. 52 (2008) 1181-1186.
[37] Y.-H. Kim, H.S. Kim, J. Lee, M. Tsutsui, T. Kawai, Stretching-induced conduc- tance variations as fingerprints of contact configurations in single-molecule junctions, J. Am. Chem. Soc. 139 (2017) 8286-8294.
[38] J.M. Soler, E. Artacho, J.D. Gale, A. Garcia, J. Junquera, P. Ordejon, D. Sanchez- Portal, The SIESTA method for ab initio order-N materials simulation, J. Phys. Condens. Matter 14 (2002) 2745-2779.
[39] A. Togo, L. Chaput, I. Tanaka, G. Hug, First-principles phonon calculations of thermal expansion inTi3SiC2,Ti3AIC2, andTi3GeC2, Phys. Rev. B 81 (2010),174301.
[40] Z. Huang, T.S. Fisher, J.Y. Murthy, Simulation of thermal conductance across

dimensionally mismatched graphene interfaces, J. Appl. Phys. 108 (11) (2010) 114310.

[41] P.S. Yeo, K.P. Loh, C.K. Gan, Strain dependence of the heat transport properties of graphene nanoribbons, Nanotechnology 23 (49) (2012), 495702.

[42] Y.-H. Kim, S.S. Jang, Y.H. Jang, W.A. Goddard III, First-principles study of the switching mechanism of [2]catenane molecular electronic devices, Phys. Rev. Lett. 94 (2005), 156801.

[43] Y.-H. Kim, J. Tahir-Kheli, P.A. Schultz, W.A. Goddard III, First-principles approach to the charge-transport characteristics of monolayer molecular-electronics devices: application to hexanedithiolate devices, Phys. Rev. B 73 (2006), 235419.

[44] S.S. Kim, H.S. Kim, H.S. Kim, Y.-H. Kim, Conductance recovery and spin polarization in boron and nitrogen co-doped graphene nanoribbons, Carbon 81 (2015) 339–346.

[45] H.S. Kim, S.S. Kim, H.S. Kim, Y.-H. Kim, Anomalous transport properties in boron and phosphorus co-doped armchair graphene nanoribbons, Nanotechnology 27 (47) (2016) 47LT01.

[46] J. Cai, P. Ruffieux, R. Jaafar, M. Bieri, T. Braun, S. Blankenburg, M. Muoth, A.P. Seitsonen, M. Saleh, X. Feng, K. Mullen, R. Fasel, Atomically precise bottom-up fabrication of graphene nanoribbons, Nature 466 (7305) (2010) 470–473.

[47] A. Milani, M. Tommasini, M. Del Zoppo, C. Castiglioni, G. Zerbi, Carbon nanowires: phonon and $\pi$-electron confinement, Phys. Rev. B 74 (15) (2006), 153418.

[48] A. Milani, M. Tommasini, G. Zerbi, Carbynes phonons: a tight binding force field, J. Chem. Phys. 128 (6) (2008), 064501.

[49] L. Ravagnan, F. Siviero, C. Lenardi, P. Piseri, E. Barborini, P. Milani, C.S. Casari, A. Li Bassi, C.E. Bottani, Cluster-beam deposition and in situ characterization of carbyne-rich carbon films, Phys. Rev. Lett. 89 (2002) 285506.

[50] L. Ravagnan, P. Piseri, M. Bruzzi, S. Miglio, G. Bongiorno, A. Baserga, C.S. Casari, A. Li Bassi, C. Lenardi, Y. Yamaguchi, T. Wakabayashi, C.E. Bottani, P. Milani, Influence of cumulenic chains on the vibrational and electronic properties of sp-sp2 amorphous carbon, Phys. Rev. Lett. 98 (2007), 216103.

[51] M. Wang, S. Lin, Ballistic thermal transport in carbyne and cumulene with micron-scale spectral acoustic phonon mean free path, Sci. Rep. 5 (2015) 18122.

[52] Y.C. Deng, S.W. Cranford, Thermal conductivity of 1D carbyne chains, Comput. Mater. Sci. 129 (2017) 226–230.

[53] X. Li, K. Maute, M.L. Dunn, R. Yang, Strain effects on the thermal conductivity of nanostructures, Phys. Rev. B 81 (24) (2010) 245318.

[54] N. Wei, L. Xu, H.Q. Wang, J.C. Zheng, Strain engineering of thermal conductivity in graphene sheets and nanoribbons: a demonstration of magic flexibility, Nanotechnology 22 (10) (2011), 105705.

[55] A. Milani, M. Tommasini, V. Barbieri, A. Lucotti, V. Russo, F. Cataldo, C.S. Casari, Semiconductor-to-Metal transition in carbon-atom wires driven by sp2 conjugated end groups, J. Phys. Chem. C 121 (19) (2017) 10562–10570.

[56] J. Heurich, J.C. Cuevas, W. Wenzel, G. Schon, Electrical transport through single-molecule junctions: from molecular orbitals to conduction channels, Phys. Rev. Lett. 88 (25) (2002), 256803.

[57] G.I. Lee, J.K. Kang, Y.-H. Kim, Metal-independent coherent electron tunneling through polymerized fullerene chains, J. Phys. Chem. C 112 (2008) 7029–7035.

[58] H.S. Kim, Y.H. Kim, Recent progress in atomistic simulation of electrical current DNA sequencing, Biosens. Bioelectron. 69 (2015) 186–198.

[59] S.J. Heerema, C. Dekker, Graphene nanodevices for DNA sequencing, Nat. Nanotechnol. 11 (2016) 127–136.