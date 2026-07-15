RSC Advances

This article can be cited before page numbers have been issued, to do this please use: C. H. Lee, J. Hong, A. Stroppa, M. Whangbo and J. Shim, *RSC Adv.*, 2015, DOI: 10.1039/C5RA12536G.

![](./images/814595731896664065_1.jpg)

This is an **Accepted Manuscript**, which has been through the Royal Society of Chemistry peer review process and has been accepted for publication.

Accepted Manuscripts are published online shortly after acceptance, before technical editing, formatting and proof reading. Using this free service, authors can make their results available to the community, in citable form, before we publish the edited article. This Accepted Manuscript will be replaced by the edited, formatted and paginated article as soon as this is available.

You can find more information about Accepted Manuscripts in the [Information for Authors].

Please note that technical editing may introduce minor changes to the text and/or graphics, which may alter content. The journal's standard [Terms & Conditions] and the [Ethical guidelines] still apply. In no event shall the Royal Society of Chemistry be held responsible for any errors or omissions in this Accepted Manuscript or any consequences arising from the use of any information it contains.

![](./images/814595731896664065_2.jpg)

www.rsc.org/advances

Organic-inorganic hybrid perovskites $AB\text{I}_3$ ($\text{A} = \text{CH}_3\text{NH}_3$, $\text{NH}_2\text{CHNH}_2$; $\text{B} = \text{Sn}$, $\text{Pb}$) as potential thermoelectric materials: A density functional evaluation

Changhoon Lee$^{1,2}$, Jisook Hong$^{1}$, Alessandro Stroppa$^{3}$, Myung-Hwan Whangbo$^{2,*}$, and Ji Hoon Shim$^{1,4,*}$

$^{1}$ Department of Chemistry, Pohang University of Science and Technology, Pohang 790-784, Korea

$^{2}$ Department of Chemistry, North Carolina State University, Raleigh, North Carolina 27695-8204, USA

$^{3}$ Consiglio Nazionale delle Ricerche - CNR-SPIN, I-67100 L'Aquila, Italy

$^{4}$ Division of Advanced Nuclear Engineering, Pohang University of Science and Technology, Pohang 790-784, Korea

Keywords: Organic-inorganic hybrid perovskites, Thermoelectric properties, Density functional calculations

### Abstract

To assess the feasibility of the organic-inorganic perovskite iodides $AB\text{I}_3$ ($A = \text{CH}_3\text{NH}_3$, $\text{NH}_2\text{CHNH}_2$; $B = \text{Sn}$, $\text{Pb}$; $X = \text{I}$) for thermoelectric applications, we estimated their figures of merit (ZTs) as well as that of $\text{Bi}_2\text{Te}_3$, which is optimized for temperatures around 300 K, as a function of chemical potential on the basis of density functional theory calculations. Our analysis employed the tetragonal structures (P4mm) of $(\text{CH}_3\text{NH}_3)\text{PbI}_3$ and $(\text{CH}_3\text{NH}_3)\text{SnI}_3$, the trigonal (P3m1) structure of $(\text{NH}_2\text{CHNH}_2)\text{PbI}_3$, and the orthorhombic (Amm2) structure of $(\text{NH}_2\text{CHNH}_2)\text{SnI}_3$ to examine their thermoelectric properties around room temperature. Our work reveals that the ZTs of electron-doped $AB\text{I}_3$ perovskites can be as large as that of hole-doped $\text{Bi}_2\text{Te}_3$ whereas those of hole-doped $AB\text{I}_3$ are rather smaller so that, in thermoelectric performance, electron-doped perovskites $AB\text{I}_3$ can be as good as hole-doped $\text{Bi}_2\text{Te}_3$.

### 1. Introduction

In organic-inorganic hybrid perovskite iodides $AB\text{I}_3$ ($A = \text{CH}_3\text{NH}_3$, $\text{NH}_2\text{CHNH}_2$; $B = \text{Sn}$, $\text{Pb}$), $\text{BI}_6$ octahedra containing divalent cations $\text{B}^{2+}$ form a three-dimensional (3D) perovskite lattice $\text{BI}_3$. The monovalent cations $\text{A}^{+}$ such as methyl ammonium (MA), $\text{CH}_3\text{NH}_3^{+}$, or formamidinium (FA), $\text{NH}_2\text{CHNH}_2^{+}$, occupy the center of each $\text{B}_8$ cube made up of eight corner-sharing $\text{BI}_6$ octahedra. These perovskites have been examined as light harvesting materials, $^{1,2}$ solar-cell absorbers, $^{3-6}$ and the tunability of the ferroelectric properties. $^{7}$ They were also considered as new n-type thermoelectric materials $^{8-10}$ and as solar thermoelectric generators, an alternative to thermoelectric devices. $^{11-13}$ The efficiency of thermoelectric energy conversion is measured by the figure of merit, $\text{ZT} = (\text{S}^2\sigma/\kappa)\text{T}$, where $\text{S}$, $\sigma$, $\kappa$, and $\text{T}$ refer to the Seebeck coefficient, electrical conductivity, thermal conductivity, and temperature, respectively. $^{14}$ Efficient thermoelectric materials need to possess a relatively large value of the power factor, $\text{S}^2\sigma$, and a low thermal conductivity $\kappa = \kappa_{\text{e}} + \kappa_{\text{L}}$, where $\kappa_{\text{e}}$ is

the electron thermal conductivity arising from charge carriers, and $\kappa_{\mathrm{L}}$ is the lattice thermal conductivity. In general, $\kappa_{\mathrm{e}}$ increases with increasing $\sigma$, so that $\kappa_{\mathrm{L}}$ is expected to be more important in controlling the ZT. Electronic structure calculations for $\mathrm{ABI}_{3}$ perovskites show that, as expected, they all have a band gap. $^{8,15-17}$ However, as-grown samples of (MA)SnI $_{3}$ were reported to exhibit metallic properties due to a trace amount of spontaneous hole-doping in the crystallization process. $^{15}$ A systematic investigation revealed that samples of $\mathrm{ABI}_{3}$ perovskites behave as p- or n-type semiconductors depending on the preparation method, and n-type samples have a low carrier concentration. $^{9}$ The lattice thermal conductivity of (MA)PbI $_{3}$ was found to be very low. $^{18}$

Very recently, He and Galli $^{10,b}$ evaluated the thermoelectric properties of (MA)BI $_{3}$ (B = Pb, Sn) using the Kane single band model $^{19}$ on the basis of DFT calculations. Their results show that the maximum ZT values of these compounds can be obtained from electron doping rather than from hole doping. In their evaluation of the thermal transport coefficients, they calculated the electrical mobility $\mu$ by considering only the acoustic phonon scattering (electron-phonon interaction). There are several factors governing the electrical mobility. According to Matthiessen's rule, the actual mobility $\mu_{e}$ is written as

$$
\frac{1}{\mu_{e}}=\frac{1}{\mu_{\text {acoustic phonon }}}+\frac{1}{\mu_{\text {optical phonon }}}+\frac{1}{\mu_{\text {impurity }}}+\cdots. \quad(1)
$$

To know the actual mobility $\mu_{e}$, we need to consider various contributions such as acoustic phonons, optical phonons, impurities and surface scattering. In typical semiconducting materials, it is known that ionized impurities and acoustic phonons are important scattering sources. Especially in heavily doped semiconductor, there would be more ionized impurities so their scattering would be more important. In addition, when there are more than $10^{17}$ electrons per $\mathrm{cm}^{3}$, electron-electron scattering starts to become significant. He and Galli

considered only the acoustic phonon scattering in the doping range $1{\times}10^{16}-5{\times}10^{19}\ \text{cm}^{-3}$ so their estimate of the mobility might be much larger than the actual mobility of the material, leading an overestimated relaxation time $\tau$ (see Eq. 2).

$$
\mu_e = e\tau/m^* \tag{2}
$$

where e, and m* are the electric charge and effective mass, respectively.

In the present work we assess the feasibility of the perovskite iodides the ${\text{ABI}}_3$ for thermoelectric applications by evaluating the power factor (PF), $\text{S}^2\sigma$, and the figure of merit, $\text{ZT} = (\text{S}^2\sigma/\kappa)\text{T}$, as a function of the chemical potential (equivalently, as a function of charge carrier density) on the basis of density functional theory (DFT) calculations. For this purpose, it is necessary to calculate the thermoelectric properties of these perovskites using their crystal structures around room temperature, and compare them with those of the well-known thermoelectric material $\text{Bi}_2\text{Te}_3$ that is optimized for temperatures around $300\ \text{K}.^{20,21}$ The structures of the perovskites ${\text{ABI}}_3$ depend on temperature, because the organic cations $\text{A}^+$ rattle around within their $\text{B}_8$ cages interacting with the $\text{BI}_3$ framework.$^{15,22-24}$ Thus, we examine the tetragonal structures (P4mm) of $(\text{MA})\text{PbI}_3$ and $(\text{MA})\text{SnI}_3$, the trigonal (P3m1) structure of $(\text{FA})\text{PbI}_3$, and the orthorhombic (Amm2) structure of $(\text{FA})\text{SnI}_3$ (Table 1).$^{8}$ Experimentally, the precise atomic positions of these perovskite iodides are poorly determined (particularly, those of the organic cations) so that we first optimize the atomic positions of these crystal structures by DFT calculations and then use the optimized structures to calculate their thermoelectric properties. Our work suggests that, in their thermoelectric efficiency, the iodide perovskites ${\text{ABI}}_3$ can be nearly as good as that of $\text{Bi}_2\text{Te}_3$ if enough electrons can be doped. Under hole doping, they are not expected to be as efficient as $\text{Bi}_2\text{Te}_3$.

## 2. Theoretical aspects and computational details

For a semiconductor, the band gap $E_{\text{g}}$ is given by $E_{\text{g}} = E_{\text{CBM}} - E_{\text{VBM}}$, where $E_{\text{CBM}}$ and $E_{\text{VBM}}$ refer to the energies of the conduction band minimum (CBM) and valence band maximum (VBM), respectively. The chemical potential $\mu$ for holes ($\mu < 0$) is defined as $\mu = \text{E} - E_{\text{VBM}}$ where $\text{E} < E_{\text{VBM}}$, and that for electrons ($\mu > 0$) by $\mu = \text{E} - E_{\text{CBM}}$ where $\text{E} > E_{\text{CBM}}$. The charge carriers available for a hole-doped or an electron-doped semiconductor at a given chemical potential $\mu$ can be approximated by integrating the electronic density of states (DOS) $\text{N}(\mu)$.

Our DFT electronic structure calculations employed the frozen-core projector augmented wave (PAW) method$^{25}$ encoded in the Vienna *ab initio* simulation package (VASP)$^{26}$ using the generalized-gradient approximation (GGA)$^{27}$ of Perdew, Burke and Ernzerhof for the exchange-correlation functional with the plane-wave-cut-off energy of 550 eV, the Monkhorst-Pack k-points mesh of $10 \times 10 \times 10$, and the threshold of self-consistent-field energy convergence of $10^{-6}$ eV. In general, it is not easy to measure exact positions of small atoms such as hydrogen atoms by XRD measurements. For this reason, the hydrogen atom positions of organic molecules are not specified in most cases. Thus, we add H atoms to the FA and MA molecules and then optimize the atom positions of $\text{ABI}_{3}$ while keeping constant the cell parameters $\text{ABI}_{3}$ on the basis of density functional calculations. The atomic positions of $(\text{MA})\text{PbI}_{3}$, $(\text{MA})\text{SnI}_{3}$, $(\text{FA})\text{PbI}_{3}$, and $(\text{FA})\text{SnI}_{3}$ were fully optimized until all the residual forces are smaller than $0.005$ eV/Å with their cell parameters fixed (**Table 1**). The atom positions obtained from these optimizations are summarized in **Table S1-S4** of the supporting information (SI). Heavy elements such as Pb, Sn and I possess a strong spin orbit coupling (SOC) effect. We examine the SOC effect on our calculations by comparing the band gaps of the perovskite iodides obtained from GGA and GGA+SOC calculations. As listed in **Table 2**, the band gaps determined from the GGA calculations agree better with the experimental band gaps than do those from the GGA+SOC calculations, as has already been reported for $(\text{MA})\text{PbI}_{3}$.$^{16}$ In estimating thermoelectric properties, it is important to describe a band gap

correctly so that our discussion of the perovskite iodides will be based on GGA calculations.

The thermoelectric properties of all considered $ABI_3$ systems were calculated by using the BoltzTrap code, $^{28}$ which solves the semi-classical Boltzmann equation using the rigid band approach $^{29}$ under the constant relaxation time approximation. The electronic structures of $ABI_3$ needed for these calculations were obtained by performing GGA calculations with the Monkhorst-Pack k-points mesh of $15{\times}15{\times}15$. We calculate the Seebeck coefficients (S), the electrical conductivity ($\sigma$), the electric thermal conductivity ($\kappa_e$), the power factor $S^2\sigma$ under the assumption that the total electron momentum relaxation time $\tau$ is independent of energy. The latter approximation, though simple, has provided explanations for the thermoelectric properties of numerous systems. $^{30-34}$

### 3. Electronic structures

The band dispersion relations calculated for $(MA)PbI_3$, $(MA)SnI_3$, $(FA)PbI_3$, and $(FA)SnI_3$ are summarized in Fig. 2. $(FA)PbI_3$ and $(FA)SnI_3$ have a direct band gap at (0.5, 0, 0), while $(MA)PbI_3$ and $(MA)SnI_3$ have a direct band gap at $R=(0.5, 0.5, 0.5)$. In cubic $ABI_3$ perovskites, a direct band gap occurs at $R=(0.5, 0.5, 0.5).^{17}$ The low-temperature distorted phases of $ABI_3$ do not differ much from their high temperature cubic phases so that the electronic structures of the low-temperature distorted $ABI_3$ are quite similar to those of their high-temperature cubic structures. Thus, the direct band gap opens at R for $(MA)BI_3$ (B = Pb, Sn). The occurrence of a direct band gap at (0.5, 0, 0) for the low-temperature $(FA)BI_3$ arises from the increase in the unit cell size caused by the structural distortion and the concomitant folding of the Billouin zone. The calculated band gaps of $(MA)PbI_3$ and $(FA)PbI_3$ are greater than those of their Sn analogues. The calculated band gaps obtained from our GGA (GGA+SOC) calculations are 1.69 (1.12), 1.62 (0.91), 0.86 (0.78), and 0.74 (0.75) eV for $(MA)PbI_3$, $(FA)PbI_3$, $(MA)SnI_3$, and $(FA)SnI_3$, respectively. The experimentally observed

band gaps are 1.55, 1.48, 1.35, and 1.41 for (MA)PbI₃,³⁵ (FA)PbI₃,³⁶ (MA)SnI₃,⁸ and (FA)SnI₃,³⁷ respectively.

The total DOS and projected DOS plots calculated for (MA)PbI₃, (MA)SnI₃, (FA)PbI₃, and (FA)SnI₃ are presented in Fig. 3. The VBM is composed of the Pb 6s and I 5p states for (MA)PbI₃ and (FA)PbI₃, and the Sn 5s and I 5p states for (MA)SnI₃ and (FA)SnI₃. The CBM is made up of the Pb 6p states for (MA)PbI₃ and (FA)PbI₃, and the Sn 5p states for (MA)SnI₃ and (FA)SnI₃. At the VBM, the Pb 6s - I 5p antibonding is weaker than the Sn 5s - I 5p antibonding, most likely because the Pb-O bonds are longer than the Sn-O bonds and because Pb 6s orbital is more diffuse than the Sn 5s orbital. The organic cations $A^+$ of the perovskites $ABI_3$ have their filled states well below the VBM, their empty states well above the CBM, and their contribution to the Fermi level is very weak. Thus, the transport properties of $ABI_3$ are governed by the electrons or holes generated in the $BI_3$ framework. The important role of the $A^+$ cations is that, by rattling within the $B_8$ cages, the $A^+$ cations would disturb the acoustic phonon dispersions of the $BI_3$ framework and hence lower the lattice thermal conductivity $\kappa_L$, as found for the rattling cations of Skutterudites in their cages.³⁸

## 4. Thermoelectric properties

We now compare the calculated thermoelectric properties of $ABI_3$ compounds with those of a p-type semiconductor $Bi_2Te_3$. The Seebeck coefficients S of $ABI_3$ calculated as a function of the chemical potential $\mu$ are shown in Fig. 4a, which exhibits two peaks at $\mu \approx$ +0.1 and -0.1 eV. At 400 K the maximum Seebeck coefficients are ~1600 μV/K for (MA)PbI₃ and (FA)PbI₃, and ~800 μV/K for (MA)SnI₃ and (FA)SnI₃. The Seebeck coefficients are considerably larger for the Pb systems because they have narrower band dispersions around the Fermi level and a larger band gap than do the Sn systems. The Seebeck coefficients of the $ABI_3$ perovskites are quite large compared with that of $Bi_2Te_3$ because the perovskites have a

much larger band gap than does $Bi_2Te_3$ ($E_g = 0.21$ eV for $Bi_2Te_3$). In general, the electron momentum relaxation time $\tau$ of conventional semiconductors is of the order of $10^{-14}$ s. $^{20,21,39,40}$ For example, $\tau \approx 2{\times}10^{-14}$ and $3{\times}10^{-14}$ s have been reported to reproduce the experimental resistivities of $Bi_2Te_3$ and PbTe, respectively. $^{20,21,40}$ Thus, in calculating the electron conductivity $\sigma$ and hence the power factor $S^2\sigma$ for all the $ABl_3$ perovskites and $Bi_2Te_3$, we employed $\tau = 2{\times}10^{-14}$ s for direct comparison of their transport properties. Indeed, the calculated electronic conductivities at low carrier concentrations show a good agreement with the experimentally observed values for $(MA)SnI_3$ $^{18}$ and $(MA)PbI_3$. $^{10a}$ The dependence of the power factor $S^2\sigma$ on the chemical potential $\mu$ is presented in **Fig. 4b**, which exhibits maximum peaks around $\mu \approx 0.8$ eV with values slightly larger for the $ASnI_3$ than for the $APbI_3$ perovskites. The maximum $S^2\sigma$ values of $ABl_3$ are $\sim$0.007 $WK^{-2}m^{-1}$ at 400 K, which can be achieved by electron doping. On the other hand, the maximum $S^2\sigma$ value attainable by hole doping is an order of magnitude smaller than that attainable by electron doping as well as that of $Bi_2Te_3$. In terms of $S^2\sigma$ alone, the perovskites $ABl_3$ would be expected to be a poor thermoelectric material compared to $Bi_2Te_3$ (**Fig. 4b**). However, what matters for thermoelectric properties is the figure of merit $ZT = (S^2\sigma/\kappa)T$, which can be enhanced by reducing the value of the thermal conductivity $\kappa = \kappa_L + \kappa_e$.

The electron thermal conductivities $\kappa_e$ calculated for $ABl_3$ and $Bi_2Te_3$ as a function of $\mu$ at 400 K are presented in **Fig. 4c**. The lattice thermal conductivities $\kappa_L$ measured for single crystal and polycrystalline samples of $(MA)PbI_3$ are 0.5 and 0.3 $WK^{-1}m^{-1}$, respectively. $^{19}$ For $Bi_2Te_3$, the reported the lattice thermal conductivities is $\kappa_L = 1.2$ $WK^{-1}m^{-1}$. $^{20,21}$ Indeed, the simulated ZT value for $Bi_2Te_3$ well describes the experimentally measured one with $\kappa_L = 1.2$ $WK^{-1}m^-1$ and $\tau = 2{\times}10^{-14}$ s. Although the measured lattice thermal conductivity of $(MA)PbI_3$ is 0.5 $WK^{-1}m^{-1}$, we adopt $\kappa_L = 1.2$ $WK^{-1}m^{-1}$ for $ABl_3$ and $Bi_2Te_3$ for direct comparison of

their thermoelectric properties in estimating the ZT values for $ABl_3$ and $Bi_2Te_3$ at 400 K. The ZTs at 400 K calculated for $ABl_3$ and $Bi_2Te_3$ as a function of $\mu$ are presented in **Fig. 4d**. It is noted that the optimum ZTs of $ABl_3$ in the $\mu > 0$ (electron-doped) region are comparable to that of $Bi_2Te_3$ in the $\mu < 0$ (hole-doped) region. In conventional semiconducting materials, the optimum ZT is generally found for the carrier concentration around $10^{19}-10^{20}\ cm^{-3}.^{41}$ Indeed, around the chemical potential $\mu \approx 0.4$ and 0.8 eV, leading to the optimum ZTs of $ASnl_3$ and $APbl_3$, the DOS value $N(\mu)$ corresponds to the carrier concentration around $10^{19}-10^{20}\ cm^{-3}$.

In **Fig. 4d**, the values of the optimal carrier concentration for each compound are indicated in the unit of $10^{19}\ cm^{-3}$. It should be noted that, in the $\mu < 0$ (hole-doped) region, the optimum ZTs of $ABl_3$ are considerably smaller than that of $Bi_2Te_3$. Thus, only when they are electron doped, the perovskites would be as good a thermoelectric material as $Bi_2Te_3$. As already pointed out in introduction section, He and Galli $^{10b}$ evaluated the thermoelectric properties of $(MA)Bl_3$ (B = Pb, Sn) on the basis of DFT calculations using the Kane single band model. $^{19}$ Their study also shows that the maximum ZT values of these compounds can be obtained from electron doping rather than from hole doping. However, their ZT values are optimized with the carrier concentration of $\sim 10^{18}cm^{-3}$, due to the use of an overestimated value for the mobility. It should lead to an extreme overestimation of the relaxation time $\tau$ as a result. We calculated the ZT values of $(MA)Pbl_3$ system by adopting various relaxation times $\tau$ to see how the relaxation time affects the ZT values as shown in Fig. S2, which shows the ZT values to be strongly influenced by the relaxation time $\tau$. Our work suggests that the carrier concentration of $10^{19}\sim 10^{20}\ cm^{-3}$ is needed for the optimum ZT values (see Fig. S3).

## 5. Concluding remarks

The thermoelectric properties of the perovskite iodides $ABl_3$ were compared with that of

$Bi_2Te_3$ on the basis of DFT calculations. The ZTs of the electron-doped $ABl_3$ can be as large as that of hole-doped $Bi_2Te_3$ while those of hole-doped $ABl_3$ are rather smaller. Thus, electron-doped perovskites $ABl_3$ are expected to exhibit as good a thermoelectric performance as does hole-doped $Bi_2Te_3$. Experimentally, it is known that the carrier density is rather low in electron-doped $ABl_3$ perovskites. It would be an interesting challenge to see if $ABl_3$ perovskites can be doped with a large number of electrons.

Supporting information

Tables S1 – S4 and Figures S1 – S3 are available free of charge via the Internet at http://

Acknowledgements

This research was supported by Global Frontier Program through the Global Frontier Hybrid Interface Materials (GFHIM) of the National Research Foundation of Korea (NRFK) funded by the Ministry of Science, ICT & Future Planning (2013M3A6B1078870) and by the resource of Supercomputing Center/Korea Institute of Science and Technology Information with supercomputing resources including technical support (KSC-2014-C1-024 and KSC-2014-C1-52). This research was supported by the computing resources of the NERSC center and the HPC center of NCSU.

References

1 J. Burschka, N. Pellet, S. –J. Moon, R. Humphry-Baker, P. Gao, M. K. Nazeeruddin and M. Grätzel, *Nature*, 2013, **499**, 316-319.

2 H. J. Snaith, *J. Phys. Chem. Lett.*, 2013, **4**, 3623-3630.

3 M. A. Green, A. Ho-Baillie and H. J. Snaith, *Nat. Photonics*, 2014, **8**, 506–514.

4 M. M. Lee, J. Teuscher, T. Miyasaka, T. N. Murakami and H. J. Snaith, *Science*, 2012, **338**, 643-647.

5 A. Kojima, K. Teshima, Y. Shirai and T. Miyasaka, *J. Am. Chem. Soc.*, 2009, **131**, 6050-6051.

6 L. Etgar, P. Gao, Z. Xue, Q. Peng, A. K. Chandiran, B. Liu, M. K. Nazeeruddin and M. Gratzel, *J. Am. Chem. Soc.*, 2012, **134**, 17396-17399.

7 Stroppa, A.; Di Sante, D.; Barone, P.; Bokdam, M.; Kresse, G.; Franchini, C.; Whangbo, M.-H. Picozzi, S. *Nature Comm.*, 2014, **5**, 3335-3339.

8 C. C. Stoumpos, C. D. Malliakas and M. G. Kanatzidis, *Inorg. Chem.*, 2013, **52**, 9019-9038.

9 F. Hao, C. C. Stoumpos, D. H. Cao, R. P. H. Chang and M. G. Kanatzidis, *Nat. Photonics.*, 2014, **8**, 489-494.

10 (a) X. Mettan, R. Pisoni, P. Matus, A. Pisoni, J. Jaćimović, B. Náfrádi, M. Spina, D. Pavuna, L. Forró and E. Horváth, *Phys. Chem. C*, 2015, **119**, 11506–11510. (b) Y. He and G. Galli, *Chem. Mater.*, 2014, **26**, 5394-5400.

11 D. Kraemer, B. Poudel, H. –P. Feng, J. C. Caylor, B. Yu, X. Yan, Y. Ma, X. Wang, D. Wang, A. Muto, K. McEnaney, M. Chiesa, Z. Ren and G. Chen, *Nat. Mater.*, 2011, **10**, 532-538.

12 L. L. Baranowski, G. J. Snyder and E. S. Toberer, *Energy Environ. Sci.*, 2012, **5**, 9055-9067.

13 W. –H. Chen, C. –C. Wang, C. –I. Hung, C. –C. Yang and R. –C. Juang, *Energy*, 2014, **64**, 287-300.

14 G. S. Nolas, J. Sharp and H. J. Goldsmid, *Thermoelectrics-Basic principles and New Materials Developments*, Springer, Berlin, 2001.

15 (a) Y. Takahashi, R. Obara, Z. -Z. Lin, Y. Takahashi, T. Naito, T. Inabe, S. Ishibashi and K. Terakura, *Dalton Trans.*, 2011, **40**, 5563-5568; (b) Y. Takahashi, H. Hasegawa, Y. Takahashi and T. Inabe, *J. Solid State Chem.*, 2013, **205**, 39-43.

16 E. Menéndez-Proupin, P. Palacios, P. Wahnón and J. C. Conesa, *Phys. Rev. B*, 2014, **90**, 045207.

17 L. Li, J. Yang, H. Liu, H. J. Xiang and X. G. Gong, *Phys. Lett. A*, 2014, **378**, 290-293.

18 A. Pisoni, J. Jaćimović, O. S. Barišić, M. Spina1, R. Gaáll, L. Forról and E. Horváth, *J. Phys. Chem. Lett.*, 2014, **5**, 2488-2492.

19 Y. I. Ravich, B. A. Efimova and I. A. Smirnov, *Semiconducting Lead Chalcogenides*, Plenum Press, New York, 1970, p. 85-216.

20 (a) H. -W. Jeon, H. -P. Ha, D. -B. Hyun and J. -D. Shim, *J. Phys. Chem. Solids*, 1991, **52**, 579-587; (b) T. J. Scheidemantel, C. Ambrosch-Draxl, T. Thonhauser, J. V. Badding and J. O. Sofo, *Phys. Rev. B*, 2003, **68**, 125210.

21 B. -L. Huang and M. Kaviany, *Phys. Rev. B*, 2008, **77**, 125209.

22 D. B. Mitzi and K. Liang, *J. Solid State Chem.*, 1997, **134**, 376-381.

23 A. Poglitsch and D. Weber, *J. Chem. Phys.*, 1987, **87**, 6373-6378.

24 T. Baikie, Y. N. Fang, J. M. Kadro, M. Schreyer, F. X. Wei, S. G. Mhaisalkar, M. Graetzel and T. J. White, *J. Mater. Chem. A*, 2013, **1**, 5628-5641.

25 (a) P. E. Blöchl, *Phys. Rev. B*, 1994, **50**, 17953-17979; (b) G. Kresse and D. Joubert, *Phys. Rev. B*, 1999, **59**, 1758-1775.

26 G. Kresse and J. Furthmüller, *Phys. Rev. B*, 1996, **54**, 11169-11186.

27 J. P. Perdew, K. Burke and M. Ernzerhof, *Phys. Rev. Lett.*, 1996, **77**, 3865-3868.

28 G. K. H. Madsen and D. J. Singh, *Comp. Phys. Commun.*, 2006, **175**, 67-71.

29 T. Boker, R. Severin, A. Muller, C. Janowitz, R. Manzke, D. Vob, P. Kruger, A. Mazur and J. Pollmann, *Phys. Rev. B*, 2001, **64**, 235305.

30 (a) K. P. Ong, D. J. Singh and P. Wu, *Phys. Rev. B*, 2011, **83**, 115110; (b) D. Parker, M. –H. Du and D. J. Singh, *Phys. Rev. B*, 2011, **83**, 245111; (c) L. Zhang and D. J. Singh, *Phys. Rev. B*, 1993, **47**, 13164-13174. (d) D. J. Singh, *Phys. Rev. B*, 2010, **81**, 195217; (e) L. Zhang, M. -H. Du and D. J. Singh, *Phys. Rev. B*, 2010, **81**, 075117; (f) G. K. H. Madsen, K. Schwarz, P. Blaha and D. J. Singh, *Phys. Rev. B*, 2003, **68**, 125212; (g) T. J. Scheidemantel, C. Ambrosch-Draxl, T. Thonhauser, J. V. Badding and J. O. Sofo, *Phys. Rev. B*, 2003, **68**, 125210; (h) L. Bertini and C. Gatti, *J. Chem. Phys.*, 2004, **121**, 8983-8989; (i) L. Lykke, B. B. Iversen and G. K. H. Madsen, *Phys. Rev. B*, 2006, **73**, 195121; (j) Y. Wang, X. Chen, T. Cui, Y. Niu, Y. Wang, M. Wang, Y. Ma and G. Zou, *Phys. Rev. B*, 2007, **76**, 155127; (k) B. Xu, C. G. Long, Y. Wang and L. Yi, *Chem. Phys. Lett.*, 2012, **529**, 45-51; (l) H. A. Rahnamaye Aliabad, M. Ghazanfari, I. Ahmad and M. A. Saeed, *Comp. mater. Sci.*, 2012, **65**, 509-519; (m) C. Lee, J. Hong, M. –H. Whangbo and J. H. Shim, *Chem. Mater.*, 2013, **25**, 3745-3752; (n) C. Lee, J. Hong, W. R. Lee, D. Y. Kim and J. H. Shim, *J. Solid State Chem.*, 2014, **211**, 113-119.

31 T. J. Scheidemantel, C. Ambrosch-Draxl, T. Thonhauser, J. V. Badding and J. O. Sofo, *Phys. Rev. B*, 2003, **68**, 125210.

32 G. K. H. Madsen, *J. Am. Chem. Soc.*, 2006, **128**, 12140-12146.

33 L. Chaput, P. Pécheur, J. Tobola and H. Scherrer, *Phys. Rev. B*, 2005, **72**, 085126.

34 X. Gao, K. Uehara, D. D. Klug, S. Patchkovskii, J. S. Tse and T. M. Tritt, *Phys. Rev. B*, 2005, **72**, 125202.

35 (a) J. H. Noh, S. H. Im, J. H. Heo, T. N. Mandal and S. I. Seok, *Nano Lett.*, 2013, **13**, 1764–1769; (b) H. S. Jung and N. –G. Park, *Small*, 2015, **11**, 10-25.

36 G. E. Eperon, S. D. Stranks, C. Menelaou, M. B. Johnston, L. M. Herz and H. J. Snaith, *Energy Environ. Sci.*, 2014, **7**, 982-988.

37 W. Yin, J. Yang, J. Kang, Y. Yan and S. –H. Wei, DOI: 10.1039/c4ta05033a.

38 (a) W. Jeitschko and D. J. Braun, *Acta Crystallogr. Sect. B*, 1977, **33**, 3401-3406; (b) B. C. Sales, D. Mandrus and R. K. Williams, *Science*, 1996, **272**, 1325-1328; (c) B. C. Sales, D. Mandrus, B. C. Chakoumakos, V. Keppens and J. R. Thompson, *Phys. Rev. B*, 1997, **56**, 15081-15089.

39 (a) J. –S. Rhyee, K. H. Lee, S. M. Lee, E. Cho, S. I. Kim, E. Lee, Y. S. Kwon, J. H. Shim and G. Kotliar, *Nature*, 2009, **459**, 965-968; (b) H. S. Ji, H. Kim, C. Lee, J. –S. Rhyee. M. H. Kim, M. Kaviany and J. H. Shim, *Phys. Rev. B*, 2013, **87**, 125111.

40 S. Ahmad and S. D. Mahanti, *Phys. Rev. B*, 2010, **81**, 165203.

41 G. Mahan, B. Sales and J. Sharp, *Phys. Today*, 1997, **50**, 42-47.

### Figure captions

Figure 1. Schematic projection views of organic-inorganic hybrid perovskites along the c-axis:
(a) (MA)BI₃ and (b) (FA)BI₃, where M = Pb, Sn. MA = methyl ammonium
$(CH_3NH_3^+)$, and FA = formamidinium $(HC(NH_2)_2^+)$. The blue, grey and black circles
represent the N, C and H atoms, respectively, and purple octahedral units represent
the BI₆ octahedra. The C-N axis of MA and the N…N axis of FA cations are oriented
along the c-axis, but are shown schematically to show their chemical structures.

Figure 2. Band dispersion relations calculated for (a) (MA)PbI₃, (b) (MA)SnI₃, (c) (FA)PbI₃,
and (d) (FA)SnI₃. They were calculated along the high symmetry lines Γ-X-M-Γ-R
for (MA)PbI₃, (MA)SnI₃, and (FA)SnI₃, where $\Gamma=(0, 0, 0)$, $\text{X}=(1/2, 0, 0)$, $\text{M}=(1/2$,
$1/2, 0)$, and $\text{R}=(1/2, 1/2, 1/2)$ in the first Brillouin zone (Fig. S1 of the SI). For
(FA)PbI₃, the band structures were calculated along the high symmetry lines Γ-M-K-
Γ-H, where $\Gamma=(0, 0, 0)$, $\text{M}=(1/2, 0, 0)$, $\text{K}=(1/3, 1/3, 0)$, and $\text{H}=(1/3, 1/3, 1/2)$ in
the first Brillouin zone (Fig. S1 of the SI).

Figure 3. The calculated total DOS of ABI₃ (left) and projected DOS of BI₃ (right): (a)
(MA)PbI₃, (b) (MA)SnI₃, (c) (FA)PbI₃, and (d) (FA)SnI₃. In the total DOS, the
projected DOS for the organic cations are added with shading.

Figure 4. Calculated transport coefficients for the organic-inorganic hybrid perovskite ABI₃
as a function of the chemical potential $\mu$: (a) the Seebeck coefficients S, (b) the
power factor $\text{S}^2\sigma$, (c) the electrical thermal conductivity $\kappa_\text{e}$, and (d) the figure of merit
ZT. The filled triangles in (c) indicate the $\kappa_\text{e}$ at the chemical potentials leading to the
maximum ZTs, and the numbers at the peaks in (d) refer to the carrier concentrations
(in units of $10^{19}\ \text{cm}^{-3}$) at the chemical potentials leading to the maximum ZTs. The
zero chemical potential refers to the midpoint of the band gap.

Table 1. Structural parameters and crystallographic data of $ABI_3$ taken from ref. 9.

<table>
  <thead>
    <tr>
      <th></th>
      <th>(MA)PbI₃</th>
      <th>(MA)SnI₃</th>
      <th>(FA)PbI₃</th>
      <th>(FA)SnI₃</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Crystal system</td>
      <td>tetragonal</td>
      <td>tetragonal</td>
      <td>trigonal</td>
      <td>orthorhombic</td>
    </tr>
    <tr>
      <td>Space group</td>
      <td>P4mm</td>
      <td>P4mm</td>
      <td>P3m1</td>
      <td>Amm2</td>
    </tr>
    <tr>
      <td>Unit cell</td>
      <td>a=6.3115</td>
      <td>a=6.2302</td>
      <td>a=8.9817</td>
      <td>a=6.3286</td>
    </tr>
    <tr>
      <td>Parameters</td>
      <td>b=6.3115</td>
      <td>b=6.2302</td>
      <td>b=8.9817</td>
      <td>b=8.9554</td>
    </tr>
    <tr>
      <td>(Å)</td>
      <td>c=6.3161</td>
      <td>c=6.2316</td>
      <td>c=11.006</td>
      <td>c=8.9463</td>
    </tr>
  </tbody>
</table>

Table 2. Calculated band gaps $E_g$ (eV) of the perovskites $ABI_3$.

<table>
  <thead>
    <tr>
      <th></th>
      <th>(MA)PbI₃</th>
      <th>(FA)PbI₃</th>
      <th>(MA)SnI₃</th>
      <th>(FA)SnI₃</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>GGA</td>
      <td>1.69</td>
      <td>1.62</td>
      <td>0.86</td>
      <td>0.74</td>
    </tr>
    <tr>
      <td>GGA+SOC</td>
      <td>1.12</td>
      <td>0.91</td>
      <td>0.78</td>
      <td>0.75</td>
    </tr>
    <tr>
      <td>Expt.</td>
      <td>1.57 ³⁴</td>
      <td>1.48 ³⁵</td>
      <td>1.35 ⁷</td>
      <td>1.41³⁶</td>
    </tr>
    <tr>
      <td></td>
      <td>1.55 ³⁴</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

![](./images/814595731896664065_3.jpg)

(a) $(MA)BI_3$

![](./images/814595731896664065_4.jpg)

(b) $(FA)BI_3$

Figure 1.

![](./images/814595731896664065_5.jpg)

Figure 2

![](./images/814595731896664065_6.jpg)

Figure 3

![](./images/814595731896664065_7.jpg)

(c) (FA)PbI₃

![](./images/814595731896664065_8.jpg)

(d) (FA)SnI₃

Figure 3

![](./images/814595731896664065_9.jpg)

Figure 4