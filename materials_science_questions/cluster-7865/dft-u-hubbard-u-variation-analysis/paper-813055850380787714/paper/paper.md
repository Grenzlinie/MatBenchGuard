![](./images/813055850380787714_1.jpg)

Computational Materials Science 146 (2018) 84-89

Contents lists available at ScienceDirect

# Computational Materials Science

journal homepage: www.elsevier.com/locate/commatsci

![](./images/813055850380787714_2.jpg)

# Description of light-element magnetic systems via density functional theory plus $U$ with an example system of fluorinated boron nitride: An efficient alternative to hybrid functional approach

![](./images/813055850380787714_3.jpg)

Wanxue Li $^{\mathrm{a}}$, Xiaojun Xin $^{\mathrm{a}}$, Hongyan Wang $^{\mathrm{b}}$, Chunsheng Guo $^{\mathrm{a}, *}$, Hong Jiang $^{\mathrm{c}, *}$, Yong Zhao $^{\mathrm{a}}$

$^{\mathrm{a}}$ Key Laboratory of Advanced Technology of Materials (Ministry of Education), Superconductivity and New Energy R&D Center, Mail Stop 165#, Southwest Jiaotong University, Chengdu, Sichuan 610031, China
$^{\mathrm{b}}$ School of Physical Science and Technology, Southwest Jiaotong University, Chengdu, Sichuan 610031, China
$^{\mathrm{c}}$ Beijing National Laboratory for Molecular Sciences, State Key Laboratory of Rare Earth Materials Chemistry and Application, College of Chemistry and Molecular Engineering, Peking University, 100871 Beijing, China

---

## ARTICLE INFO

**Article history:**
Received 5 November 2017
Received in revised form 2 January 2018
Accepted 2 January 2018

**Keywords:**
DFT+U
Hybrid functionals
Light-element magnets

## ABSTRACT

It is well known that for light-element magnetic materials density functional theory (DFT) in the local density approximation or generalized gradient approximation (LDA or GGA) underestimates the electron localization effects and tends to give misleading results. Hybrid functionals such as Heyd-Scuseria- Ernzerhof (HSE) perform much better while being computationally expensive, especially for extended systems. In order to go beyond semi-local DFT without needing to calculate the expensive Fock exchange, here we explore the performance of the more efficient GGA plus the Hubbard $U$ correction (GGA+U) approach to light-element magnetic materials by considering fluorinated boron nitride (F-BN) sheets and nanotubes as model systems. By applying the Hubbard $U$ correction to the N-2p orbitals with the value of $U$ determined by fitting the HSE results in a particular F-BN sheet, it is found that the GGA+U approach shows a great improvement to GGA in describing the magnetic properties of F-BN systems with an accuracy close to that of the HSE hybrid functional approach. It indicates the possibility of using the ad hoc correction approach as an efficient alternative to study light-element magnetic materials, especially for large systems where calculations based on hybrid functionals become cost-demanding.

© 2018 Elsevier B.V. All rights reserved.

---

## 1. Introduction

Light-element magnets which only involve $sp$ electrons have great potential to overcome the limitation of the technologies relying on materials based on $d$ and $f$ elements. Researches on this topic have made great progress in past few years, such as experimental observations and theoretical predictions [1-6] of carbon based systems [7-9], H adsorbed on graphene [10-12], F on graphene [13-15], F on BN sheets [16,17], F on BN nanotubes [18,19], C substitution in ZnO [20,21], to name a few only. To further understand the magnetic properties of these systems and also for the capacity to predict new materials, a proper theoretical method is required for correctly describing the relative energy, charge and spin distribution of the low-lying electronic states. The commonly used semi-local density functional theory (DFT) [22,23] such as local density approximation (LDA) or generalized gradient approximation (GGA) [24], although greatly successful in the study of non-magnetic (close-shell) molecules and solids, may fail in these systems which involve un-paired and localized 2p electrons. Semi-local DFT suffers from the severe delocalization error [25], and often leads to misleading prediction regarding magnetic materials [26]. Instead, recent studies suggest that the hybrid functional approach which mixes a fraction of the exact (Fock) exchange with LDA or GGA exchange can greatly improve the description of electronic and magnetic properties of many magnetic systems, including those based on light-elements [26]. However, the necessity of computing Fork exchange makes the hybrid functionals computationally much more expensive than LDA/GGA, especially for complex material systems.

For magnetic materials based on transition metal ions, an alternative to go beyond LDA and GGA without introducing the heavy computational cost of hybrid functionals is the so-called LDA+$U$ (or DFT+$U$, to be more general) approach, which was originally proposed by Anisimov and coworkers to overcome the failure of LDA to properly describe electronic band structure of transition metal oxides like NiO [27]. The on-site Hubbard $U$ correction can

---

* Corresponding authors.
E-mail addresses: cguo@swjtu.edu.cn (C. Guo), h.jiang@pku.edu.cn (H. Jiang).

https://doi.org/10.1016/j.commatsci.2018.01.003
0927-0256/© 2018 Elsevier B.V. All rights reserved.

effectively remedy the excessive delocalization of $d$ and $f$ electrons in standard LDA or GGA, and it leads to significantly improved description of magnetic properties in many transition metal compounds [27,28]. The DFT+$U$ method was also used to study the carbon systems with spin polarized $p$ electrons, while the parameter $U$ varies between 2 and 4.5 eV for fitting different references and the magnetic properties are found to be very sensitive to the parameter $U$ used [29,30].

This ad hoc correction usually requires a reference to determine the value of $U$. In view of the high accuracy of hybrid functional approach, it is highly interesting to study the ability of DFT+$U$ for reproducing the HSE outcomes. In this work, we first get the $U$ parameter of the spin centers of N ions by fitting the energy difference between the ferromagnetic and antiferromagnetic phases obtained from HSE of a fluorinated boron nitride (F-BN) sheet (see details in the Section 2 session). With this $U$ as large as 7 eV added on N ions, the HSE results of various F-BN systems are well reproduced by the DFT+$U$ approach, not only for ferromagnetic stability, but also for electronic properties, i.e. electronic band structures, localization of spin density, etc. Our investigations indicate that the DFT+$U$ approach can be used as an accurate and efficient alternative to the hybrid functional approach for light-element magnetic materials, especially for large systems where calculations based on hybrid functionals become cost-demanding .

## 2. Computational details

Our first principles calculations are based on Kohn-Sham density functional theory (DFT) with the projector-augmented wave (PAW) [31-33] approach and the plane-wave basis as implemented in Vienna Ab Initio Simulation Package (VASP) [31,34-37]. Structures of F-BN sheets with various F coverage (Fig. 1), F-BN nanotubes with various F distances (Fig. 7) are relaxed with GGA-PBE functional in the ferromagnetic state until the force on each atom is less than 0.01 eV/Å. In the F-BN sheets and nanotubes, the F atoms are adsorbed on B ions of BN system which was reported to be energetically favorable [38]. With the optimized structures, the magnetic properties, including, in particular, the energy difference between the ferromagnetic and antiferromagnetic states, are calculated by HSE06 [39-41], GGA+$U$ [24] and semi-local GGA-PBE. During the calculations, the cutoff energy is always 400 eV in plane wave based expansion. A $16 \times 16 \times 1$ k-point mesh generated by the Monkhorst-Pack scheme is applied for the $(1 \times 1)$ sheet, and for other larger sheet structures the k-point grid is reduced consistently to ensure comparable numerical accuracy for that of the $(1 \times 1)$ sheet. To accelerate the convergence of the self-consistent field (SCF) iterations, we used the Gaussian smearing with a small width of 0.05 eV.

Fig. 1 shows the F-BN sheets with different F coverage considered in our calculations: in the $(2 \times 1)$ sheet all boron atoms of the BN sheet are bonded to F while in the $(6 \times 3)$ only 1/9 bonded to F. It has been reported that the planar F-BN sheets are nonmagnetic in LDA calculations [42], while they are ferromagnetic in GGA and HSE calculations [26,43] which agree with the experimental of stripping BN monolayer through absorbing F atoms, reported by Du et al. in 2014 [16]. Nevertheless, the GGA outcomes are quite different with the results from HSE calculations which are proposed to provide much better description for magnetic systems [26].

![](./images/813055850380787714_4.jpg)

Fig. 1. Structures of (a) $(2 \times 1)$, (b) $(4 \times 2)$, (c) $(6 \times 3)$, (d) $(2\sqrt{3} \times \sqrt{3})$ and (e) $(4\sqrt{3} \times 2\sqrt{3})$ sheet supercells with fluorine coverage of 50%, 12.5%, 5.6%, 16.7% and 4.2%, respectively. The boron, nitrogen and fluorine atoms are remarked by pink, blue and light green, respectively. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

## 3. Results and discussion

### 3.1. Determination of the Hubbard $U$

Here we take the energy difference $\Delta E = E^{\text{AFM}} - E^{\text{FM}}$, which is related to the strength of magnetic coupling, in F-BN sheets calculated by the HSE06 functional as the reference to obtain the empirical effective parameter $U_{\text{eff}} = U$-$J$. Considering that in the F-BN systems N ions are spin centers on which over 95% spin densities are localized, we only added the Hubbard $U$ correction to N-$2p$ orbitals in our calculations. Actually we have tested and found that adding the $U$ correction to F and B ions has little effect on the performance of the GGA+$U$ approach. Fig. 2 shows $\Delta E$ as a function of $U_{\text{eff}}$ in the magnetic $(2\sqrt{3} \times \sqrt{3})$ F-BN sheet which is the smallest F-BN sheet not fully covered by F adatoms. Apparently $\Delta E$ increases linearly with increasing $U_{\text{eff}}$. To obtain the identical $\Delta E$ from HSE calculations, the value of $U_{\text{eff}}$ for the N spin centers has to be as large as 7.3 eV. The values of $U_{\text{eff}}$ determined in a similar way for other structures shown in Fig. 1 are slightly different, but they are all around 7 eV. In the following, for simplification we apply $U_{\text{eff}} = 7$ eV for N spin centers in all spin polarized F-BN systems to explore the performance of GGA+$U$ calculations.

The value of $U$, as large as 7 eV, is much larger than the $U$ applied for the carbon [29,30] and the transition metal systems [27,28]. Although for the electronic and magnetic properties the GGA+$U$ outcomes are very similar to the HSE results, as demonstrated in the following, this semi-empirical approach with a large $U$ is not suitable for the structure relaxation. Actually we have tested the $U = 7$ eV to optimize the geometry and obtained lattice constant differs a lot from the experimental results. Consequently, the structures are optimized by GGA-PBE while with GGA+$U$ to calculate the magnetic and electronic properties in our calculations.

![](./images/813055850380787714_5.jpg)

Fig. 2. The energy difference between the ferromagnetic and antiferromagnetic states of the $(2\sqrt{3} \times \sqrt{3})$ F-BN sheet by GGA+$U$ as function of $U_{\text{eff}}$ compared to that calculated by the HSE hybrid functional.

With GGA-PBE functional the lattice constant of planar BN sheet is 2.49 Å, which agrees with previous work [44] and the experimental [45] results.

### 3.2. Performance of GGA+U for magnetic properties

The GGA calculations show that $\Delta E$ of $(2 \times 1)$, $(2\sqrt{3} \times \sqrt{3})$, $(4 \times 2)$, $(6 \times 3)$, and $(4\sqrt{3} \times 2\sqrt{3})$ structures are 63.7, 70.1, 45.0, 0.6, 25.2 meV, while in the HSE calculations they are 11.5, 526.8, 129.6, 93, and 147 meV, respectively. GGA+$U$ calculations produce the results of 11.5, 522.7, 50.8, 95, and 147 meV, respectively, which agree very well with the HSE results, as shown in the Fig. 3, although for the $(4 \times 2)$ case, the difference between GGA +$U$ and HSE is a bit larger. Apparently, results by HSE, GGA+$U$ calculations show the F-BN sheets are ferromagnetic, which is consistent with the experimental results [16]. This corrects the non-magnetic results from the LSDA calculations [42]. Although the GGA also yields the ferromagnetic coupling for the F-BN sheets, previous studies suggested HSE improves the description of electronic and magnetic properties than the GGA approach, i.e. for the Mn doped in Ge [46] and NiO systems [47]. This means the GGA+$U$ can describe the F-BN systems much better than the GGA functional.

GGA+$U$ calculations not only produce better results for $\Delta E$ which is related to the magnetic coupling, but also generate magnetic moments per F adsorbate and the distribution of local moments with the accuracy comparable with HSE. Large structures of $(6 \times 3)$, and $(4\sqrt{3} \times 2\sqrt{3})$ with F-F distance larger than 7 Å are no longer fully spin polarized in GGA calculations, with the total moment less than $1\ \mu_B$ per F atom adsorption, while in HSE and GGA+$U$ calculations the total moment of these systems are always $1\ \mu_B$ per F atom adsorption. In GGA calculations magnetic moments are 10% localized on F atoms and 82% on N atoms, while in HSE and GGA+$U$ calculations, magnetic moments are over 95% localized on N atoms and less than 2% on F (other moment localized on B). The localization of the spin electrons can be roughly viewed by the spin density plot in Fig. 4. In the GGA result, we can see some spin density localized on the F atoms while it is almost invisible in the HSE and GGA+$U$ calculations. With the same isosurface less spin density is found on N atoms in GGA result than those in HSE and GGA+$U$ results.

### 3.3. Performance of GGA+U for electronic properties

Fig. 5 shows more details of the electronic structures of the F-BN sheets with the $(2 \times 2)$ F-BN sheet as an example. Generally speaking, the spin density of states (DOS) near the Fermi level is

![](./images/813055850380787714_6.jpg)

Fig. 3. The energy difference $\Delta E$, and the total magnetic moment obtained by GGA, HSE and GGA+$U$ approaches for $(2 \times 1)$, $(2\sqrt{3} \times \sqrt{3})$, $(4 \times 2)$, $(6 \times 3)$, and $(4\sqrt{3} \times 2\sqrt{3})$ F-BN structures, respectively.

![](./images/813055850380787714_7.jpg)

Fig. 4. spin density of $(2\sqrt{3} \times \sqrt{3})$ F-BN sheet with isosurface = 0.02 e/Å³.

![](./images/813055850380787714_8.jpg)

Fig. 5. DOS and band structures of the $(2 \times 2)$ F-BN sheet by (a) and (b) GGA, (c) and (d) HSE, (e) and (f) GGA+$U$ approaches.

![](./images/813055850380787714_9.jpg)

Fig. 6. (a) With $U_{\text{eff}}$ = 3, 5, 7, and 9 eV, the shift of VBM in majority according to that of GGA, and (b) the plot of projected DOS of N $p_{z}$ with $U_{\text{eff}}$ = 7 eV.

dominantly contributed by the N atoms and little by F and B [26]. The features of electronic bands near the conduction band minimum (CBM) and valance band maximum (VBM) are similar in all of the GGA, HSE, and GGA+$U$ calculations. For example, in the minority there are two partially filled energy bands contributed by N atoms at the Fermi level ($E_{\text{F}}$), see the DOS in red. In the GGA approach the $E_{\text{F}}$ is very close to the VBM in the majority, with a band gap of 5.0 eV. In the HSE and GGA+$U$ approaches the $E_{\text{F}}$ is around 1 eV above the VBM, with band gaps of 5.8 and 5.2 eV, respectively. The HSE band gap is consistent with the experimental result around 5 eV.

In order to further study the effect of Coulomb on-site repulsion at the N spin centers, we look into the shift of VBM in the spin majority states, which is contributed by $p_{z}$ of N (see Fig. 6b), for a series of $U_{\text{eff}}$ values in the $(2\times2)$ F-BN sheet. As shown in Fig. 6a, increasing $U_{\text{eff}}$ induces a rigid left-shift of VBM energy in the spin majority states. Due to the fact that the energy bands of the spin minority (metallic) change little with increasing $U_{\text{eff}}$, the shift of the VBM in the majority near the Fermi level is consistent with the spin splitting of the energy bands at the VBM which is mostly contributed by the $p_{z}$ of N atoms (see Fig. 6b). It can be estimated that the spin splitting increases 0.25, 0.5, 0.75, and 1.2 eV with the increasing $U_{\text{eff}}$, 3, 5, 7 and 9 eV, respectively. When $U_{\text{eff}}$ = 7 eV GGA+$U$ produces the close $\Delta E$ with the HSE, the spin splitting from GGA+$U$ is only 0.2 eV smaller than the HSE outcomes. On the other hand, it is found that the spin polarization in these systems has nothing to do with N $2s$ state but mostly contributed by N $2p_{z}$ state. Considering the $sp^{2}$ hybridization of the clean BN systems, which are similar with the typical $sp^{2}$ structure of graphene [44,48], it seems that after the F adsorbed, one $\pi$ electron transfer to the F atom and the left electron in the $\pi$ orbital becomes localized and spin polarized. This could be the rationality that only applying $U_{\text{eff}}$ on N-$2p$ state can well reproduce the HSE results.

### 3.4. Flexibility of GGA+$U$

With $U_{\text{eff}}$ = 7 eV, GGA+$U$ calculations do not only give good descriptions for planar F-BN sheets with various F concentrations, but also yield results which agree well with the HSE for F-BN nanotubes with large curvatures. For example, with an F atom adsorbed on the B atom of a primitive tube cell (thus forming an F chain along the BN nanotube), the $\Delta E$ of the (8, 0) F-BN nanotube obtained with GGA is 77.0 meV, while with HSE and GGA+$U$ the $\Delta E$ is 10.2 and 11.2 meV, respectively. In the GGA calculations, the (8, 0) F-BN nanotube is only around 50% spin polarized [16],

![](./images/813055850380787714_10.jpg)

Fig. 7. Axial view of circumferentially adsorbed two F atoms in the primitive cell of the (8, 0) BN nanotube. The two F atoms are adsorbed on two nearest (a), second nearest (b), third nearest (c) and opposite (d) B atoms. $\Delta E = E^{\text{AFM}} - E^{\text{FM}}$ (e) and magnetic moment per F adsorbate (f) of these F-BN structures with various F-F distances calculated by HSE, GGA+$U$ and GGA schemes.

according to the definition [49] $P=[N_{\downarrow}(E_{F})-N_{\uparrow}(E_{F})]/[N_{\downarrow}(E_{F})+N_{\uparrow}(E_{F})]$ where $N_{\downarrow}(E_{F})$ and $N_{\uparrow}(E_{F})$ are the DOS corresponding to the two spin orientations at the Fermi level $(E_{F})$. However, it is fully spin polarized in HSE and GGA+U calculations. In addition, the (8, 0) F-BN nanotube calculated by GGA is metallic in both majority and minority, while in HSE and GGA+U calculations it is half-metallic with a semiconducting gap of 4.8 and 3.5 eV in spin majority states, respectively. The local moments by the GGA+U are mostly contributed by N1 atom $(0.38\ \mu_{B})$ and N2 and N3 atoms $(0.14\ \mu_{B}$ each), agree well with the results of HSE which are 0.4 $\mu_{B}$ at N1 atom and $0.15\ \mu_{B}$ at N2 and N3 atoms, respectively [26], indicating large local moments compared to the results from LSDA $(0.27\ \mu_{B}, 0.063\ \mu_{B}$ and $0.063\ \mu_{B}$ for N1, N2 and N3) [41] and GGA calculations $(0.23\ \mu_{B}, 0.11\ \mu_{B}$ and $0.11\ \mu_{B}$ for N1, N2 and N3).

Adding one more F atoms adsorbed on the B atom in the primitive cell of a BN nanotube increase the F concentration. In this system, the F-F atom distance can be modified and subsequently the distortions of the nanotubes. As shown in Fig. 7, the (8, 0) F-BN nanotube is distorted dramatically by changing the F-F distances. The F-F distance increases from 3.86 Å of two F atoms on the two nearest boron atoms in Fig. 7a to 10.47 Å of two F atoms at the opposite sides in Fig. 7d. It is consistent in HSE, GGA+U and GGA calculations that the magnetic coupling decreases with increase F-F distances. Nevertheless, GGA+U yields $\Delta E$ very close to those from HSE, but around 50-100 meV larger than GGA results, as shown in Fig. 7e. Most strikingly, the structure with two F atoms at the opposite sides in Fig. 7d is antiferromagnetic in GGA calculation, while it is ferromagnetic from HSE and GGA+U calculations. Similar to the BN sheets cases, the local moment per F adsorbate by GGA+U and HSE calculations is robustly $1\ \mu_{B}$ while by GGA it varies with F-F distances, as shown in Fig. 7f.

## 4. Conclusion

In summary, we studied the performance of efficient GGA+U approach for magnetic properties of systems only involving $sp$ elements by comparing with hybrid HSE and GGA calculations. By fitting the energy difference $\Delta E$ between the ferromagnetic and antiferromagnetic states from HSE calculation which is related to the strength of magnetic coupling, we obtained the $U_{\text{eff}}$ parameter as large as 7 eV for the N spin centers of F-BN sheets. By applying $U_{\text{eff}}$ on N spin centers the DFT+U is able to well reproduce the HSE results flexibly for various F-BN systems, with different distortions or F concentrations, leading to great improvement from GGA in describing the $\Delta E$, total magnetic moments, spin splitting, and localization of the magnetic moments. It indicates that the GGA +U approach with proper U can be an accurate and efficient alternative to the more expensive hybrid functional approach for adequately describing the magnetic properties of large light-element magnetic systems.

## Acknowledgement

This work is partly supported National Natural Science Foundation of China (No. 51302231, 51271155, 51377138, and 21373017), Ministry of Science and Technology (2013CB933400), by the Fundamental Research Funds for the Central Universities (SWJTU2682013RC02, SWJTU11ZT31, SWJTU2682016ZDPY10),

## References

[1] J.S. Arellano, L.M. Molina, A. Rubio, J.A. Alonso, Density functional study of adsorption of molecular hydrogen on graphene layers, J. Chem. Phys. 112 (2000) 8114-8119.

[2] D.W. Boukhvalov, M.I. Katsnelson, Chemical functionalization of graphene, J. Phys-Condens. Mat. 21 (2009) 344205.

[3] D.W. Boukhvalov, M.I. Katsnelson, A.I. Lichtenstein, Hydrogen on graphene: electronic structure, total energy, structural distortions and magnetism from first-principles calculations, Phys. Rev. B 77 (2008) 035427.

[4] H. Pan, J.B. Yi, L. Shen, R.Q. Wu, J.H. Yang, J.Y. Lin, Y.P. Feng, J. Ding, L.H. Van, J.H. Yin, Room-temperature ferromagnetism in carbon-doped ZnO, Phys. Rev. Lett. 99 (2007) 127201.

[5] Q.X. Pei, Y.W. Zhang, V.B. Shenoy, A molecular dynamics study of the mechanical properties of hydrogen functionalized graphene, Carbon 48 (2010) 898-904.

[6] J.O. Sofo, A.S. Chaudhari, G.D. Barber, Graphane: a two-dimensional hydrocarbon, Phys. Rev. B 75 (2007) 153401.

[7] K.S. Novoselov, A.K. Geim, S.V. Morozov, D. Jiang, Y. Zhang, S.V. Dubonos, I.V. Grigorieva, A.A. Firsov, Electric field effect in atomically thin carbon films, Science 306 (2004) 666-669.

[8] D. Li, M.B. Muller, S. Gilje, R.B. Kaner, G.G. Wallace, Processable aqueous dispersions of graphene nanosheets, Nat. Nanotechnol. 3 (2008) 101-105.

[9] H.W. Kroto, C60 Buckminsterfullerene, Mater. Res. Soc. Symp. p 206 (1991) 611-617.

[10] D.C. Elias, R.R. Nair, T.M.G. Mohiuddin, S.V. Morozov, P. Blake, M.P. Halsall, A.C. Ferrari, D.W. Boukhvalov, M.I. Katsnelson, A.K. Geim, K.S. Novoselov, Control of graphene's properties by reversible hydrogenation: evidence for graphane, Science 323 (2009) 610-613.

[11] S. Ryu, M.Y. Han, J. Maultzsch, T.F. Heinz, P. Kim, M.L. Steigerwald, L.E. Brus, Reversible basal plane hydrogenation of graphene, Nano Lett. 8 (2008) 4597-4602.

[12] H. Gonzalez-Herrero, J.M. Gomez-Rodriguez, P. Mallet, M. Moaied, J.J. Palacios, C. Salgado, M.M. Ugeda, J.Y. Veuillen, F. Yndurain, I. Brihuega, Atomic-scale control of graphene magnetism by using hydrogen atoms, Science 352 (2016) 437-441.

[13] Y.C. Cheng, T.P. Kaloni, G.S. Huang, U. Schwingenschlogl, Origin of the high p-doping in F intercalated graphene on SiC, Appl. Phys. Lett. 99 (2011) 12307-12311.

[14] R.R. Nair, M. Sepioni, I.L. Tsai, O. Lehtinen, J. Keinonen, A.V. Krasheninnikov, T. Thomson, A.K. Geim, I.V. Grigorieva, Spin-half paramagnetism in graphene induced by point defects, Nat. Phys. 8 (2012) 199-202.

[15] J.T. Robinson, J.S. Burgess, C.E. Junkermeier, S.C. Badescu, T.L. Reinecke, F.K. Perkins, M.K. Zalalutdniov, J.W. Baldwin, J.C. Culbertson, P.E. Sheehan, E.S. Snow, Properties of fluorinated graphene films, Nano Lett. 10 (2010) 3001-3005.

[16] M. Du, X.L. Li, A.Z. Wang, Y.Z. Wu, X.P. Hao, M.W. Zhao, One-step exfoliation and fluorination of boron nitride nanosheets and a study of their magnetic properties, Angew. Chem. Int. Ed. 53 (2014) 3645-3649.

[17] Y.F. Xue, Q. Liu, G.J. He, K.B. Xu, L. Jiang, X.H. Hu, J.Q. Hu, Excellent electrical conductivity of the exfoliated and fluorinated hexagonal boron nitride nanosheets, Nanoscale Res. Lett. 8 (2013) 12868-12886.

[18] L. Lai, W. Song, J. Lu, Z.X. Gao, S. Nagase, M. Ni, W.N. Mei, J.J. Liu, D.P. Yu, H.Q. Ye, Structural and electronic properties of fluorinated boron nitride nanotubes, J. Phys. Chem. B 110 (2006) 14092-14097.

[19] Z. Zhou, Z.J. Zhao, Z.F. Chen, C.V. Schleyer, Atomic and electronic structures of fluorinated BN nanotubes: computational study, J. Phys. Chem. B 110 (2006) 25678-25685.

[20] J.P. Liu, C.X. Guo, C.M. Li, Y. Li, Q. Lib, X.T. Huang, L. Liao, T. Yu, Carbondecorated ZnO nanowire array: a novel platform for direct electrochemistry of enzymes and biosensing applications, Electrochem. Commun. 11 (2009) 202-205.

[21] S.Q. Zhou, Q.Y. Xu, K. Potzger, G. Talut, R. Grotzschel, J. Fassbender, M. Vinnichenko, J. Grenzer, M. Helm, H. Hochmuth, M. Lorenz, M. Grundmann, H. Schmidt, Room temperature ferromagnetism in carbon-implanted ZnO, Appl. Phys. Lett. 93 (2008) 15-50.

[22] A. Karton, A. Tarnopolsky, J.F. Lamere, G.C. Schatz, J.M.L. Martin, Highly accurate first-principles benchmark data sets for the parametrization and validation of density functional and other approximate methods. Derivation of a robust, generally applicable, double-hybrid functional for thermochemistry and thermochemical kinetics, J. Phys. Chem. A 112 (2008) 12868-12886.

[23] S. Kummel, L. Kronik, Orbital-dependent density functionals: theory and applications, Rev. Mod. Phys. 80 (2008) 3-60.

[24] J.P. Perdew, K. Burke, M. Ernzerhof, Generalized gradient approximation made simple (vol 77, pg 3865, 1996), Phys. Rev. Lett. 78 (1997) 1396.

[25] A.J. Cohen, P. Mori-Sanchez, W.T. Yang, Insights into current limitations of density functional theory, Science 321 (2008) 792-794.

[26] C.S. Guo, Y. Zhou, X.Q. Shi, L.Y. Gan, H. Jiang, Y. Zhao, Robust half-metallic ferromagnetism and curvature dependent magnetic coupling in fluorinated boron nitride nanotubes, Phys. Chem. Chem. Phys. 18 (2016) 12307-12311.

[27] P. Rivero, C. Loschen, I.D.R. Moreira, F. Illas, Performance of plane-wave-based LDA plus U and GGA plus U approaches to describe magnetic coupling in molecular systems, J. Comput. Chem. 30 (2009) 2316-2326.

[28] V.I. Anisimov, J. Zaanen, O.K. Andersen, Band theory and Mott Insulators - Hubbard U instead of Stoner-I, Phys. Rev. B 44 (1991) 943-954.

[29] M.J. Han, G. Kim, J.I. Lee, J. Yu, Competition between structural distortion and magnetic moment formation in fullerene C-20, J. Chem. Phys. 130 (2009) 898-904.

[30] J.C. Ren, Z.G. Wang, R.Q. Zhang, Z.J. Ding, M.A. Van Hove, Enhancement of spin polarization induced by Coulomb on-site repulsion between localized p(z) electrons in graphene embedded with line defects, Phys. Chem. Chem. Phys. 17 (2015) 30744-30750.

[31] S.N. Datta, C. Trindle, F. Illas, Theoretical and Computational Aspects of Magnetic Organic Molecules, Imperial College Press, London, 2013.

[32] P.E. Blochl, Projector augmented-wave method, Phys. Rev. B 50 (1994) 17953-17979.

[33] G. Kresse, D. Joubert, From ultrasoft pseudopotentials to the projector augmented-wave method, Phys. Rev. B 59 (1999) 1758-1775.

[34] G. Kresse, J. Hafner, Ab-initio molecular-dynamics simulation of the liquid-metal amorphous-semiconductor transition in germanium, Phys. Rev. B 49 (1994) 14251-14269.

[35] G. Kresse, Ab-initio molecular-dynamics for liquid-metals, J. Non-Cryst. Solids 193 (1995) 222-229.

[36] G. Kresse, J. Furthmuller, Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set, Computat. Mater. Sci. 6 (1996) 15-50.

[37] G. Kresse, J. Furthmuller, Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set, Phys. Rev. B 54 (1996) 11169-11186.

[38] F. Li, Z.G. Zhu, X.D. Yao, G.Q. Lu, M.W. Zhao, Y.Y. Xia, Y. Chen, Fluorination-induced magnetism in boron nitride nanotubes from ab initio calculations, Appl. Phys. Lett. 92 (2008) 102515.

[39] J. Heyd, G.E. Scuseria, M. Ernzerhof, Hybrid functionals based on a screened Coulomb potential, J. Chem. Phys. 118 (2003) 8207-8215.

[40] J. Heyd, G.E. Scuseria, M. Ernzerhof, Hybrid functionals based on a screened Coulomb potential (vol 118, pg 8207, 2003), J. Chem. Phys. 124 (2006) 101-105.

[41] A.V. Krukau, O.A. Vydrov, A.F. Izmaylov, G.E. Scuseria, Influence of the exchange screening parameter on the performance of screened hybrid functionals, J. Chem. Phys. 125 (2006) 202-205.

[42] Z.H. Zhang, W.L. Guo, Tunable ferromagnetic spin ordering in boron nitride nanotubes with topological fluorine adsorption, J. Amer. Chem. Soc. 131 (2009) 6874-6879.

[43] S. Radhakrishnan, D. Das, A. Samanta, C.A. de los Reyes, L.Z. Deng, L.B. Alemany, T.K. Weldeghiorghis, V.N. Khabashesku, V. Kochat, Z.H. Jin, P.M. Sudeep, A.A. Marti, C.W. Chu, A. Roy, C.S. Tiwary, A.K. Singh, P.M. Ajayan, Fluorinated h-BN as a magnetic semiconductor, Sci. Adv. 3 (2017) e1700842.

[44] R.F. Liu, C. Cheng, Ab initio studies of possible magnetism in a BN sheet by nonmagnetic impurities and vacancies, Phys. Rev. B. 76 (2007) 014405.

[45] N. Ooi, A. Rairkar, L. Lindsley, J.B. Adams, Electronic structure and bonding in hexagonal boron nitride, J. Phys.-Condens. Mat. 18 (2006) 97-115.

[46] A. Stroppa, G. Kresse, A. Continenza, Revisiting Mn-doped Ge using the Heyd-Scuseria-Ernzerhof hybrid functional, Phys. Rev. B 83 (2011) 085201.

[47] P. Rivero, I.D.R. Moreira, G.E. Scuseria, F. Illas, Description of magnetic interactions in strongly correlated solids via range-separated hybrid functionals, Phys. Rev. B 79 (2009) 245129.

[48] A. Pakdel, Y. Bando, D. Shtansky, D. Golberg, Nonwetting and optical properties of BN nanosheet films, Surf. Innov. 1 (2013) 32-39.

[49] R.J. Soulen, J.M. Byers, M.S. Osofsky, B. Nadgorny, T. Ambrose, S.F. Cheng, P.R. Broussard, C.T. Tanaka, J. Nowak, J.S. Moodera, A. Barry, J.M.D. Coey, Measuring the spin polarization of a metal with a superconducting point contact, Science 282 (1998) 85-88.