View Article Online
View Journal

# RSC Advances

This article can be cited before page numbers have been issued, to do this please use: A. H. Reshak and
S. Auluck, *RSC Adv.*, 2016, DOI: 10.1039/C5RA24601F.

![](./images/814559975937409024_1.jpg)

This is an **Accepted Manuscript**, which has been through the
Royal Society of Chemistry peer review process and has been
accepted for publication.

Accepted Manuscripts are published online shortly after
acceptance, before technical editing, formatting and proof reading.
Using this free service, authors can make their results available
to the community, in citable form, before we publish the edited
article. This Accepted Manuscript will be replaced by the edited,
formatted and paginated article as soon as this is available.

You can find more information about Accepted Manuscripts in the
Information for Authors.

Please note that technical editing may introduce minor changes
to the text and/or graphics, which may alter content. The journal's
standard Terms & Conditions and the Ethical guidelines still
apply. In no event shall the Royal Society of Chemistry be held
responsible for any errors or omissions in this Accepted Manuscript
or any consequences arising from the use of any information it
contains.

![](./images/814559975937409024_2.jpg)

www.rsc.org/advances

# Influence of Oxygen Vacancy on the Electronic Structure of the Asymmetric Mixed Borate-Carbonate $\mathbf{Pb_7O(OH)_3(CO_3)_3(BO_3)}$

A. H. Reshak$^{1,2,*}$, Sushil Auluck$^{3,4}$

$^{1}$New Technologies - Research Centre, University of West Bohemia, Univerzitni 8, 306 14 Pilsen, Czech republic

$^{2}$Center of Excellence Geopolymer and Green Technology, School of Material Engineering, University Malaysia Perlis, 01007 Kangar, Perlis, Malaysia

$^{3}$Council of Scientific and Industrial Research - National Physical Laboratory Dr. K S Krishnan Marg, New Delhi 110012, India

$^{4}$Department of Physics, Indian Institute of Technology Delhi,Hauz Khas,New Delhi 110016, India

## Abstract
The influence of an oxygen vacancy on the electronic properties of a mixed borate-carbonate compound $\mathrm{Pb_7O(OH)_3(CO_3)_3(BO_3)}$ is studied. We report calculations of the electronic band structure, the angular momentum resolved projected density of states and the valence electronic charge density distribution. The full-potential method within the generalized gradient approximation $(PBE-GGA)$ and a recently modified Becke-Johnson potential $(mBJ)$ shows an indirect band gap of 3.34 eV $(PBE-GGA)$ and 3.56 eV $(mBJ)$ for $\mathrm{Pb_7O(OH)_3(CO_3)_3(BO_3)}$, while it is a direct gap of 1.10 eV $(PBE-GGA)$ and 1.61 eV $(mBJ)$ for the compound $\mathrm{Pb_7(OH)_3(CO_3)_3(BO_3)}$ which has one O vacancy. Thus, the O vacancy causes a significant reduction in the band gap and also changes it from indirect to direct. The band gap reduction in $\mathrm{Pb_7(OH)_3(CO_3)_3(BO_3)}$ is attributed to the appearance of a new energy bands inside the energy gap of $\mathrm{Pb_7O(OH)_3(CO_3)_3(BO_3)}$. The angular momentum resolved projected density of states for $\mathrm{Pb_7O(OH)_3(CO_3)_3(BO_3)}$ and $\mathrm{Pb_7(OH)_3(CO_3)_3(BO_3)}$ show that there exists a strong hybridization between B and O of $\mathrm{BO_3}$ group and between C and O of $\mathrm{CO_3}$ group. The valence electronic charge density for both compounds is presented. It reveals the origin of chemical bonding characters and the influence of O vacancy. After a careful comparison, it is found that the crystal structure of $\mathrm{Pb_7O(OH)_3(CO_3)_3(BO_3)}$ without O vacancy can be considered as a parent phase of defect $\mathrm{Pb_7(OH)_3(CO_3)_3(BO_3)}$.

**Keywords:** O-vacancy; $\mathrm{Pb_7O(OH)_3(CO_3)_3(BO_3)}$; $\mathrm{Pb_7(OH)_3(CO_3)_3(BO_3)}$; DFT

$^{*}$Corresponding author; E-mail address:maalidph@yahoo.co.uk

### 1. Introduction

Recently several carbonate non-centro-symmetric single crystals [1-4] have been synthesized because of their unusual structure and promising applications in optical and photonic devices, optical parametric oscillation (OPO), second harmonic generation (SHG) and laser frequency conversion [5-18]. Recently Maierhaba et al. [19] synthesized mixed borate-carbonate nonlinear optical materials which exhibit large SHG response. They reported the first borate-carbonate ultra-violet (UV) nonlinear optical material with a chemical formula $\text{Pb}_7\text{O(OH)}_3\text{(CO}_3\text{)}_3\text{(BO}_3\text{)}$. They attributed the large SHG to the strong interactions between the stereo-effect of Pb cations and co-parallel $\text{BO}_3$ and $\text{CO}_3$ triangles groups [1-4,19,20]. Maierhaba et al have reported x-ray diffraction data and have measured the energy band gap. It has been found that $\text{Pb}_7\text{O(OH)}_3\text{(CO}_3\text{)}_3\text{(BO}_3\text{)}$ crystallizes in a non-centro-symmetric structure with hexagonal space group $P6_3mc$. The unit cell contains two formulas, the lattice parameters are reported to be a=b=10.519(16) Å and c=8.900(13) Å [19]. In addition, they have calculated the band structure and the density of states using CASTEP code within the generalized gradient approximation $(PBE-GGA)$ [21]. The CASTEP code is a non-full potential method which ignores the potential in the interstitial region. Moreover $PBE-GGA$ underestimates the band gap. We would like to emphasize that in full-potential methods the potential and charge density are expanded into lattice harmonics inside each atomic sphere and as a Fourier series in the interstitial region. Hence, the effect of the full potential on the electronic properties can be ascertained. In addition, we have explored the effect of introducing one oxygen vacancy on the electronic properties. Thus the new compound is $\text{Pb}_7\text{(OH)}_3\text{(CO}_3\text{)}_3\text{(BO}_3\text{)}$. We call the original compound as I and the compound with oxygen vacancy as II. The mixed borate-carbonate $\text{Pb}_7\text{O(OH)}_3\text{(CO}_3\text{)}_3\text{(BO}_3\text{)}$ is newly synthesized compound and hence no details information regarding the electronic band structure and the total and the angular momentum resolved projected density of states. This motivated us to perform comprehensive theoretical calculations to ascertain the influence of an oxygen vacancy on the electronic properties. We thought it would be interesting to perform full potential calculation within the recently modified Becke-Johnson potential $(mBJ)$ [22], to calculate the electronic band structure, density of states, the valence electronic charge density distribution and the chemical bonding characters of I and II

compounds. The modified Becke-Johnson potential allows the calculation with accuracy similar to the very expensive GW calculations [22,1000]. Hedin developed the GW method by linking 5 many-body equations together into a self-consistent scheme. The vertex correction arises from the two-particle Green's function (G) associated with the Coulomb energy (W). It provides many-body corrections to the exchange and correlation energy. It is a local approximation to an atomic "exact-exchange" potential and a screening term [22,23].

### 2. Calculation methodology

The calculations are performed based on the x-ray crystallographic data reported by Maierhaba's group [19] for the compound I. Then we have used the experimental crystallographic data of compound I and removed two oxygen atoms to investigate the influence of oxygen vacancy (as the unit cell has Z=2) on the resulting properties. Therefore, a theoretical model originating from the designed oxygen vacancies has been proposed in order to seek the influence of O-vacancy on the band structure and the associated properties. The geometrical relaxation of I was achieved within the generalized gradient approximation $(PBE-GGA)$ [21] using the full potential linear augmented plane wave $(FPLAPW+lo)$ method as embodied in the WIEN2k code [24]. The resulting relaxed geometry of I is used to calculate the electronic structure and hence the associated properties using the recently modified Becke-Johnson potential $(mBJ)$ [22]. For II we removed the two O atoms. After the self consistent cycle the forces in I and II were similar. The crystal structures of I and II along with the unit cell are presented in Fig. 1 where the oxygen vacancies are clearly shown. The optimized atomic positions of I are listed in Table 1 in comparison with the experimental data of I [19].

The muffin-tin radii $(R_{MT})$ of the atoms are chosen in such a way that the spheres did not overlap. The value of $R_{MT}$ is taken to be 2.32 a.u. for Pb, 1.19 a.u. for O, 1.23 a.u. for B, 1.18 a.u. for C and 0.64 a.u. for H for both I and II. To achieve the total energy convergence, the basis functions in the interstitial region $(IR)$ were expanded up to $R_{MT}{\times}K_{max}=7.0$ and inside the atomic spheres for the wave function. The maximum value of $l$ was taken as $l_{max}=10$, while the charge density is Fourier expanded up to $G_{max}=12$

$(a.u)^{-1}$. Self-consistency is obtained using 192 for I and 72 for II $\vec{k}$ points in the irreducible Brillouin zone ($IBZ$). The self-consistent calculations are converged since the total energy of the system is stable within 0.00001 Ry. The electronic properties are calculated using a larger number of $k$ points in the $IBZ$. It is well known that first-principles calculations are a powerful and useful tool to predict the crystal structure and its properties related to the electron configuration of a material before its synthesis [25-28].

## 3. Results and discussion
### 3.1. Electronic band structures and density of states

The calculated electronic band structure along the high symmetry points of the first BZ and the angular momentum resolved projected density of states (PDOS) of oxygen atoms of I and II compounds are shown in Fig. 2(a) and 2(b).The valence band maximum (VBM) of I and II is located at the center ($\Gamma$) of the BZ while the conduction band minimum (CBM) of I is situated between $\Gamma$ and A points of BZ, resulting in an indirect energy band gap of 3.34 eV ($PBE-GGA$) and 3.56 eV (mBJ). The CBM of II is located at $\Gamma$ of the BZ, resulting in a direct band gap of 1.10 eV ($PBE-GGA$) and 1.61 eV ($mBJ$). The band gap reduction in II is attributed to the appearance of a new energy bands within the energy gap region of I. Thus, the O-vacancy causes to reduce and tune the band gap and it changes the energy gap from indirect to direct. It has been found that mBJ succeeds by large amount in bringing the calculated energy gap of I close to the experimental one (3.65 eV) [19] as is expected from this approach [29-31]. Therefore, in the following, we show only the results obtained by mBJ. The angular momentum resolved projected density of states of I and II are presented in Fig. 3. The crystal structure of I and II consist of three Pb atoms and one atom of B, C and H. There are five O atoms in I and four O atoms in II. We illustrate the contribution of each atom in Fig. 3 (a, c, e, g, i) for I and Fig. 3(b, d, f, h, j) for II. It is clear that the three Pb atoms and five O atoms in I and four O atoms in II exhibit different contributions while Pb3 in I Pb1 in II and O5 in I and O2 in II exhibit the highest contributions. Total density of states is for unit cell (Z=2) that is 2 formula units. Partial density of states is for one atom. To explore the contribution of the orbitals we have decided to show the orbitals of one atom of each

type, the one which shows highest contribution, for instance Pb3-6s/6p/5d/4f (Pb1-6s/6p/5d/4f), O5-2s/2p (O2-2s/2p), B-2s/2p, C-2s/2p and H-1s as shown in Fig.3(g)-(j). The PDOS shows the influence of the oxygen vacancies on the bands dispersion. It is clear that in the VB of I, there is high density state region situated between -2.5 eV and Fermi level ($E_F$) which belongs to a O atom (Fig. 2a), and this feature vanishes from the electronic band structure of II (Fig. 2b) due to the oxygen vacancy. From the PDOS (Fig. 3(a)-(f)), it has been noticed that for I the VBM is mainly formed by O3, O4, O5 and Pb2, Pb3 atoms while for II it is clear that the O bands are vanished confirming that the two oxygen vacancies keeping the VBM with Pb1 and Pb3 only. It is clear that the O vacancies push Pb1 states which are situated below VBM towards Pb3 to form the VBM while it pushes Pb2 and the rest of Pb1, Pb3 states towards lower energies by around 2.0 eV. It is interesting to mention that there is a energy bands appeared directly above $E_F$ in the forbidden gap, which composed of O2-2p states. This could be called intermediate band (IB). The appearance of new bands may cause the appearance of new excitations. Recently, Ding et al. [32] reported that the position of such local energy level is changed due to the variation of oxygen vacancy concentration. There exists a strong hybridization between Pb1,Pb2 and Pb3 atoms, also between O1,O2,O3,O4 and O5 atoms. Furthermore, C atom hybridized with Pb2, B with Pb3, O4 with Pb3, O5 with Pb2 and Pb3. The degree of the hybridization favors to enhance the strength of the covalent bonding. Fig. S1a and S1b (supplementary material) shows the total density of states (TDOS) along with the electronic band structure and the first BZ are shown for I and II. It is clear that the oxygen vacancy significantly influences the TDOS.

The origin of chemical bonding can be elucidated from the angular momentum decomposition of the atoms projected electronic density of states (Fig. 3(a-f)). Integrating the latter from -6.0 eV up to Fermi level ($E_F$) we obtain the total number of electrons/eV ($e/eV$) for the orbitals in each atom of I (II), Pb1 atom 3.8 (1.8) $e/eV$, Pb2 atom 7.8 (3.9) $e/eV$, Pb3 9.2 (2.3)$e/eV$, O1 atom 6.0 $e/eV$, O2 atom 9.0 (8.0) $e/eV$, O3 atom 12.0 (13.5) $e/eV$, O4 atom 14.5 (11.0) $e/eV$, O5 atom 16.0 (12.5) $e/eV$, C atom 6.0 (2.4) $e/eV$, B atom 1.8 (1.2) $e/eV$ and H atom 0.6 (0.3) $e/eV$. The contributions of these atoms to the valence bands show that there is a clear influence on the electronic structure due to O vacancy. Also it is indicated that some electrons from Pb, C, B, H and


O atoms are transferred into valence bands and contribute in covalence interactions between the atoms. The covalent bond arises due to the degree of the hybridization and the electronegativity differences between the atoms. It is clear that there is an interaction of charges between the atoms due to the existence of the hybridization, showing that there is a strong/weak covalent bonding between these atoms. Thus the angular momentum decomposition of the atoms projected electronic density of states help us to analyze the nature of the bonds according to the classical chemical concept. This concept is very useful to classify compounds into different categories with respect to different chemical and physical properties.

### 3.2. Valence electronic charge density

To investigate the nature of the bonds and the interactions between the atoms we have taken a careful look at valence electronic charge density distribution of I and II in three crystallographic planes namely (1 0 0), ( 1 0 1) and (1 1 0) as shown in Fig. 4(a)-(f). It has been observed that the (1 0 0) plane of I and II show only Pb, B and O atoms (Fig. 4(a),(b)). The Pb atoms are surrounded by a spherical charge indicating the ionic nature of these atoms. The existence of B atom between the three O atoms which forms the $BO_3$ group perturbs the contour of the three O atoms. According to Pauling scale the electro-negativity of Pb, B, O, C and H are 2.33, 2.04, 3.44, 2.55 and 2.20. Therefore, due to the electro-negativity difference between O and B atoms one can see the charge transfer towards O atoms as indicated by the blue color around O atoms (according to the thermoscale the blue color exhibits the maximum charge accumulation). It has been noticed that the B atom forms strong covalent bonds with the nearest three O atoms ($BO_3$ group). It is clear that the (1 0 0) plane for II does not show the O-vacancy.

Fig. 4(c) and 4 (d) illustrates (1 0 1) crystallographic plane of I and II which shows all the atoms. It is clear that C atom form a strong covalent bond with the three O atoms ($CO_3$) group. Therefore, there exists a strong covalent bond between C atom and the three O atoms ($CO_3$ group). The Pb atoms tend to form a very weak covalent bond with O atoms. The (1 0 1) crystallographic plane confirms that B atom perturbs the contour of the three O atoms. It is clear that the (1 0 1) plane for II does not show the O-vacancy. Therefore,

we have calculated the valence electronic charge density distribution of I and II in the (1
1 0) plane as shown in Fig. 4(e) and 4(f).

We have labeled the O-vacancy by arrows 1 and 2 (see Fig. 4(e),(f)). It is clear that Pb
(Fig. 4(e)) form strong covalent bond with O at the location labeled by 1 (see Fig. 4(e)).
This covalent bond is missing in Fig. 4(f) due to the O vacancy. Thus, O vacancy leads to
connect Pb by six O atoms in II instead of seven O atoms in I. The calculated valence
electronic charge density distribution supports our finding from the PDOS which states
that there exists a strong hybridization between B and O atoms also between C and O
atoms. The strong/weak hybridization may lead to form strong/weak covalent bonding. It
is interesting to compare our calculated bond lengths and angles with the measured one
[19]. This is given in Table 2 and 3 which reveal that there is a good agreement between
the theory and experiment.

After a careful comparison, it is found that the crystal structure of I without O vacancy
(Fig. 1a,b) can be considered as a parent phase of defect II structure (Fig.1c,d).

### 4. Conclusions
The electronic band structure, the angular momentum resolved projected density of
states and the valence electronic charge density distribution of the mixed borate-
carbonate I and II are reported. The full-potential method within the generalized gradient
approximation ($PBE-GGA$) and the recently modified Becke-Johnson potential ($mBJ$)
reveals the I structure possesses an indirect band gap of 3.34 eV ($PBE-GGA$) and 3.56
eV ($mBJ$), while it is direct gap of 1.10 eV ($PBE-GGA$) and 1.61 eV ($mBJ$) for the O
vacancy II structure. Thus, the O-vacancy causes to reduce and tune the band gap from
indirect to direct band gap. The band gap reduction in II is attributed to the appearance of
a new energy bands in the band gap of I. The angular momentum resolved projected
density of states for I and II show that there exists a strong hybridization between B and
O of $BO_3$ group and also between C and O of $CO_3$ group. The calculated valence
electronic charge density reveals the origin of chemical bonding character. It shows the
influence of O vacancy on the resulting properties of II. After a careful comparison, it is
found that the crystal structure of I can be considered as a parent phase of defect II.

### Associated content

Fig. S1: The total density of states (TDOS) along with the electronic band structure and the first BZ are shown for I and II. It is clear that the oxygen vacancy significantly influences the TDOS.

### Acknowledgments
The result was developed within the CENTEM project, reg. no. CZ.1.05/2.1.00/03.0088, cofunded by the ERDF as part of the Ministry of Education, Youth and Sports OP RDI programme and, in the follow-up sustainability stage, supported through CENTEM PLUS (LO1402) by financial means from the Ministry of Education, Youth and Sports under the "National Sustainability Programme I. Computational resources were provided by MetaCentrum (LM2010005) and CERIT-SC (CZ.1.05/3.2.00/08.0144) infrastructures. SA would like to thank CSIR-National Physical Laboratory and Physics Department Indian Institute of Technology Delhi for support.

### References
[1] Zou, G. H.; Ye, N.; Huang, L.; Lin, X. S. Alkaline-Alkaline Earth Fluoride Carbonate Crystals ABCO3F (A = K, Rb, Cs; B = Ca, Sr, Ba) as Nonlinear Optical Materials. J. Am. Chem. Soc. 2011, 133,20001–20007.

[2] Zou, G. H.; Huang, L.; Ye, N.; Lin, C. S.; Cheng, W. D.; Huang, H. Designing a Deep-Ultraviolet Nonlinear Optical Material with a Large Second Harmonic Generation Response. J. Am. Chem. Soc. 2013, 135, 18560–18566.

[3] Tran, T. T.; Halasyamani, P. S.; Rondinelli, J. M. Role of Acentric Displacements on the Crystal Structure and Second-Harmonic Generating Properties of RbPbCO3F and CsPbCO3F. Inorg. Chem. 2014, 53, 6241–6251.

[4] Tran, T. T.; Halasyamani, P. S. New Fluoride Carbonates: Centrosymmetric KPb2(CO3)2F and Noncentrosymmetric K2.70Pb5.15(CO3)5F3. Inorg. Chem. 2013, 52, 2466–2473.

[5] Wei, Q. C.; Gunter, H.; Petri, K.; Margit, R.; Markus, H.; Hubert, H.; Gert, L. Effects of Gigapascal Level Pressure on Protein Structure and Function. J. Phys. Chem. B 2012, 116, 1100–1110.

[6] Halasyamani, P. S.; Poeppelmeier, K. R. Chem. Mater. 1998, 10, 2753–2769; Halasyamani, P. S. Asymmetric Cation Coordination in Oxide Materials: Influence of Lone-Pair Cations on the Intra-octahedral Distortion in d0 Transition Metals. Chem. Mater. 2004, 16, 3586–3592.

[7] Chung, I.; Jang, J. I.; Malliakas, C. D.; Ketterson, J. B.; Kanatzidis, M. G. Strongly Nonlinear Optical Glass Fibers from Noncentrosymmetric Phase-Change Chalcogenide Materials. J. Am. Chem. Soc. 2010, 132, 384-389.

[8] (a) Yao, W. J.; He, R.; Wang, X. Y.; Lin, Z. S.; Chen, C. T. Analysis of Deep-UV Nonlinear Optical Borates: Approaching the End. Adv. Opt. Mater. 2014, 2, 411-417.

[9] Huang, H. W.; Yao, J. Y.; Lin, Z. S.; Wang, X. Y.; He, R.; Yao, W. J.; Zhai, N. X.; Chen, C. T. Molecular Engineering Design to Resolve the Layering Habit and Polymorphism Problems in Deep UV NLO Crystals: New Structures in MM'Be2B2O6F (M=Na, M'=Ca; M= K, M'=Ca, Sr). Chem. Mater. 2011, 23, 5457-5463.

[10] Li, L. Y.; Li, G. B.; Wang, Y. X.; Liao, F. H.; Lin, J. H. Bismuth Borates: One- Dimensional Borate Chains and Nonlinear Optical Properties. Chem. Mater. 2005, 17, 4174-4180.

[11] Cao, G.-J.; Lin, J.; Wang, J.-Y.; Zheng, S.-T.; Fang, W.-H.; Yang, G.-Y. Two additive-induced isomeric aluminoborates templated by methylamine. Dalton Trans. 2010, 39, 8631-8636.

[12] Donakowski, M. D.; Gautier, R.; Yeon, J.; Moore, D. T.; Nino, J. C.; Halasyamani, P. S.; Poeppelmeier, K. R. The Role of Polar, Lamdba ($\Lambda$)-Shaped Building Units in Noncentrosymmetric Inorganic Structures. J. Am. Chem. Soc. 2012, 134, 7679-7689.

[13] Sun, C. F.; Hu, C. L.; Xu, X.; Yang, B. P.; Mao, J. G. Explorations of New Second- Order Nonlinear Optical Materials in the Potassium Vanadyl Iodate System. J. Am. Chem. Soc. 2011, 133, 5561-5572.

[14] Hu, H. S.; Wei, F.; Wang, X. F.; Andrews, L.; Li, J. Actinide-Silicon Multiradical Bonding: Infrared Spectra and Electronic Structures of the Si($\mu$-X)AnF3 (An = Th, U; X = H, F) Molecules. J. Am. Chem. Soc. 2014, 136, 1427-1437.

[15] Wu, H. P.; Yu, H. W.; Yang, Z. H.; Hou, X. L.; Su, X.; Pan, S. L.; Poeppelmeier, K. R.; Rondinelli, J. M. Designing a Deep-Ultraviolet Nonlinear Optical Material with a Large Second Harmonic Generation Response. J. Am. Chem. Soc. 2013, 135, 4215-4218.

[16] Choyke, S. J.; Blau, S. M.; Larner, A. A.; Narducci, S. A.; Yeon, J.; Halasyamani, P. S.; Norquist, A. Noncentrosymmetry in New Templated Gallium Fluorophosphates. J. Inorg. Chem. 2009, 48, 11277- 11282.

[17] Tan, H. Q.; Du, S. C.; Bi, Y. F.; Liao, W. P. Two Elongated Octahedral Coordination Cages Constructed by M4-TC4A Secondary Building Units (M = CoII and FeII) and 2,2'-Bipyridine-4,4'-dicarboxylic Acids. Inorg. Chem. 2014, 53, 7083-7085.

[18] Zeng, M.-H.; Yin, Z.; Tan, Y.-X.; Zhang, W.-X.; He, Y.-P.; Kurmoo, M. Nanoporous Cobalt(II) MOF Exhibiting Four Magnetic Ground States and Changes in Gas Sorption upon Post-Synthetic Modification. J. Am. Chem. Soc. 2014, 136, 4680-4688.

[19] Maierhaba Abudoureheman, Li Wang, Xianming Zhang, Hongwei Yu, Zhihua Yang, Chen Lei, Jian Han, and Shilie Pan, Pb7O(OH)3(CO3)3(BO3): First Mixed Borate and Carbonate Nonlinear Optical Material Exhibiting Large Second-Harmonic Generation Response, Inorg. Chem. 2015, 54, 4138-4142

[20] Yu, H. W.; Wu, H. P.; Pan, S. L.; Yang, Z. H.; Hou, X. L.; Su, X.; Jing, Q.; Poeppelmeier, K. R.; Rondinelli, J. M. Cs3Zn6B9O21: A Chemically Benign Member of the KBBF Family Exhibiting the Largest Second Harmonic Generation Response. J. Am. Chem. Soc. 2014, 136, 1264-1267.

[21] Perdew, J. P.; Burke, K.; Ernzerhof, M. Generalized Gradient Approximation Made Simple. *Phys. Rev. Lett.* **1996**, 77, 3865-3868.

[22] Tran, F.; Blaha P. Accurate Band Gaps of Semiconductors and Insulators with a Semilocal Exchange-Correlation Potential. *Phys. Rev. Lett.* 2009, 102, 226401;

[23] Hedin, L. New Method for Calculating the One-Particle Green's Function with Application to the Electron-Gas Problem. 1965, Phys. Rev. 139 A796; Hedin, L. and Lundqvist, S. 1969 Solid State Physics vol. 23, eds. H. Ehrenreich, F. Seitz, and D. Turnbull (Academic, New York); Hedin, L. Electron correlation: keeping close to an orbital description. Int. J. Quantum Chem. 1995, 56, 445-52

[24] Blaha, P.; Schwarz, K.; Madsen, G. K. H.; Kvasnicka, D.; Luitz, J. WIEN2k, An augmented plane wave plus local orbitals program for calculating crystal properties, Vienna University of Technology, Austria (2001)

[25] Plucinski, K. J.; Kityk, I. V.; Kasperczyk, J.; Sahraoui, B. The structure and electronic properties of silicon oxynitride gate dielectrics. Semiconductor Science and Technology 16, 467-470 (2001).

[26] Malachowski, M.; Kityk, I. R.; Sahraoui, B. Electronic structure and optical response in $Ga_xAl_{1-x}$N solid alloys. Physics Letters A 242, 337-342 (1998).

[27] Fuks-Janczarek, I.; Miedzinski, R.; Brik, M.G.; Majchrowski, A.; Jaroszewicz, L.R.; Kityk, I.V. Z-scan analysis and ab initio studies of $\beta$-BaTeMo2O9 single crystal. Solid State Sciences 27 (2014) 30-35

[28] Reshak, A. H.; Majchrowski, A.; Swirkowicz, M.; Kłos, A.; Łukasiewicz, T.; Kityk, I.V.; Iliopoulos, K.; Couris, S. Brik, M.G. Optical features of calcium neodymium oxyborate Ca4NdO(BO3)3 doped by Yb3+, Journal of Alloys and Compounds 481 (2009) 14–16

[29] Reshak, A.H. Specific features of electronic structures and optical susceptibilities of molybdenum oxide, RSC Adv., 2015, 5, 22044

[30] Reshak, A.H.; Huang, H.; Kamarudin, H.; Auluck, S. Alkali-metal/alkaline-earth-metal fluorine beryllium borate NaSr3Be3B3O9F4 with large nonlinear optical properties in the deep-ultraviolet region, J. Appl. Phys 117, 085703 (2015)

[31] Reshak, A.H. Transport properties of g-BC3 and t-BC3 phases, RSC Adv., 2015, 5, 33632

[32] Ding, B. F.; Qian, H. J.; Han, C.; Zhang, J. Y.; Lindquist, S. E.; Wei, B.; Tang, Z. L. Oxygen Vacancy Effect on Photoluminescence Properties of Self-Activated Yttrium Tungstate, J. Phys. Chem. C., 2014, **118**, 25633

Table 1: Optimized atomic positions of $Pb_7O(OH)_3(CO_3)_3(BO_3)$ in comparison with the experimental data [19].

<table>
<thead>
<tr>
<th>Atom</th>
<th>x-exp.</th>
<th>x-opt.</th>
<th>y-exp.</th>
<th>y-opt.</th>
<th>z-exp.</th>
<th>z-opt.</th>
</tr>
</thead>
<tbody>
<tr>
<td>Pb(1)</td>
<td>0.3333</td>
<td>0.3333</td>
<td>0.6667</td>
<td>0.6667</td>
<td>0.2753(2)</td>
<td>0.2751</td>
</tr>
<tr>
<td>Pb(2)</td>
<td>0.6606(2)</td>
<td>0.6600</td>
<td>0.8303(1)</td>
<td>0.8301</td>
<td>0.8995(2)</td>
<td>0.8992</td>
</tr>
<tr>
<td>Pb(3)</td>
<td>0.4567(1)</td>
<td>0.4561</td>
<td>0.5433(1)</td>
<td>0.5431</td>
<td>0.6025(2)</td>
<td>0.6023</td>
</tr>
<tr>
<td>O(1)</td>
<td>0.3333</td>
<td>0.3333</td>
<td>0.6667</td>
<td>0.6667</td>
<td>0.5220(50)</td>
<td>0.5221</td>
</tr>
<tr>
<td>O(2)</td>
<td>0.6310(20)</td>
<td>0.6312</td>
<td>0.8154(12)</td>
<td>0.8152</td>
<td>0.6520(30)</td>
<td>0.6522</td>
</tr>
<tr>
<td>O(3)</td>
<td>0.4094(12)</td>
<td>0.4092</td>
<td>0.5906(12)</td>
<td>0.5904</td>
<td>0.8520(20)</td>
<td>0.8520</td>
</tr>
<tr>
<td>O(4)</td>
<td>0.8090(30)</td>
<td>0.8091</td>
<td>0.9045(13)</td>
<td>0.9043</td>
<td>0.3440(30)</td>
<td>0.3439</td>
</tr>
<tr>
<td>O(5)</td>
<td>0.5918(17)</td>
<td>0.5916</td>
<td>0.9014(19)</td>
<td>0.9012</td>
<td>0.3176(18)</td>
<td>0.3174</td>
</tr>
<tr>
<td>B(1)</td>
<td>0.3333</td>
<td>0.3333</td>
<td>0.6667</td>
<td>0.6667</td>
<td>0.8640(90)</td>
<td>0.8641</td>
</tr>
<tr>
<td>C(1)</td>
<td>0.6610(40)</td>
<td>0.6611</td>
<td>0.8310(20)</td>
<td>0.8311</td>
<td>0.3290(60)</td>
<td>0.3292</td>
</tr>
<tr>
<td>H</td>
<td>0.8615</td>
<td>0.8619</td>
<td>0.1379</td>
<td>0.1380</td>
<td>0.0941</td>
<td>0.0944</td>
</tr>
</tbody>
</table>

**Table 2:** Calculated bond lengths (Å) of $\text{Pb}_7\text{O(OH)}_3\text{(CO}_3\text{)}_3\text{(BO}_3\text{)}$ in comparison with the experimental data [19].

<table>
  <thead>
    <tr>
      <th>Bond</th>
      <th>Exp.</th>
      <th>This work</th>
      <th>Bond</th>
      <th>Exp.</th>
      <th>This work</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Pb(1)-O(1)</td>
      <td>2.19(4)</td>
      <td>2.20</td>
      <td>Pb(2)-O(4)ⁿ</td>
      <td>2.729(6)</td>
      <td>2.730</td>
    </tr>
    <tr>
      <td>Pb(1)-O(5)ª</td>
      <td>2.630(17)</td>
      <td>2.631</td>
      <td>Pb(2)-O(4)ⁱ</td>
      <td>2.729(6)</td>
      <td>2.730</td>
    </tr>
    <tr>
      <td>Pb(1)-O(5)ᵇ</td>
      <td>2.630(18)</td>
      <td>2.631</td>
      <td>Pb(3)-O(1)</td>
      <td>2.359(13)</td>
      <td>2.358</td>
    </tr>
    <tr>
      <td>Pb(1)-O(5)ᶜ</td>
      <td>2.630(17)</td>
      <td>2.631</td>
      <td>Pb(3)-O(3)</td>
      <td>2.38 (2)</td>
      <td>2.39</td>
    </tr>
    <tr>
      <td>Pb(1)-O(5)</td>
      <td>2.630(17)</td>
      <td>2.631</td>
      <td>Pb(3)-O(2)</td>
      <td>2.548(13)</td>
      <td>2.547</td>
    </tr>
    <tr>
      <td>Pb(1)-O(5)ᵈ</td>
      <td>2.630(18)</td>
      <td>2.631</td>
      <td>Pb(3)-O(2)ᵉ</td>
      <td>2.548(14)</td>
      <td>2.547</td>
    </tr>
    <tr>
      <td>Pb(1)-O(5)ᵉ</td>
      <td>2.630(17)</td>
      <td>2.631</td>
      <td>B(1)-O(3)</td>
      <td>1.39 (2)</td>
      <td>1.38</td>
    </tr>
    <tr>
      <td>Pb(2)-O(2)</td>
      <td>2.22(2)</td>
      <td>2.23</td>
      <td>B(1)-O(3)ᵉ</td>
      <td>1.39(2)</td>
      <td>1.38</td>
    </tr>
    <tr>
      <td>Pb(2)-O(3)</td>
      <td>2.619(5)</td>
      <td>2.620</td>
      <td>B(1)-O(3)ᵇ</td>
      <td>1.39(2)</td>
      <td>1.38</td>
    </tr>
    <tr>
      <td>Pb(2)-O(3)ᵇ</td>
      <td>2.619(6)</td>
      <td>2.620</td>
      <td>C(1)-O(4)</td>
      <td>1.35(4)</td>
      <td>1.36</td>
    </tr>
    <tr>
      <td>Pb(2)-O(4)ᶠ</td>
      <td>2.729(6)</td>
      <td>2.729</td>
      <td>C(1)-O(5)</td>
      <td>1.28(3)</td>
      <td>1.29</td>
    </tr>
    <tr>
      <td>Pb(2)-O(4)ᵍ</td>
      <td>2.729(7)</td>
      <td>2.729</td>
      <td>C(1)-O(5)ᵈ</td>
      <td>1.28(3)</td>
      <td>1.29</td>
    </tr>
  </tbody>
</table>

**Table 3:** Calculated bond angles (ᵒ) of $\text{Pb}_7\text{O(OH)}_3\text{(CO}_3\text{)}_3\text{(BO}_3\text{)}$ in comparison with the experimental data [19].

<table>
  <thead>
    <tr>
      <th>Angles</th>
      <th>Exp.</th>
      <th>This work</th>
      <th>Angles</th>
      <th>Exp.</th>
      <th>This work</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>O(1)-Pb(1)-O(5)ª</td>
      <td>81.8(4)</td>
      <td>81.79</td>
      <td>O(5)ᵇ-Pb(1)-O(5)ᶜ</td>
      <td>68.7(7)</td>
      <td>68.71</td>
    </tr>
    <tr>
      <td>O(1)-Pb(1)-O(5)ᵇ</td>
      <td>81.8(4)</td>
      <td>81.79</td>
      <td>O(5)-Pb(1)-O(5)ᵈ</td>
      <td>49.9(7)</td>
      <td>49.91</td>
    </tr>
    <tr>
      <td>O(1)-Pb(1)-O(5)ᶜ</td>
      <td>81.8(4)</td>
      <td>81.79</td>
      <td>O(5)ª-Pb(1)-O(5)ᵇ</td>
      <td>49.9(7)</td>
      <td>49.91</td>
    </tr>
    <tr>
      <td>O(1)-Pb(1)-O(5)</td>
      <td>81.8(4)</td>
      <td>81.79</td>
      <td>O(5)ᶜ-Pb(1)-O(5)ᵉ</td>
      <td>49.9(7)</td>
      <td>49.91</td>
    </tr>
    <tr>
      <td>O(1)-Pb(1)-O(5)ᵈ</td>
      <td>81.8(4)</td>
      <td>81.79</td>
      <td>O(2)-Pb(2)-O(3)</td>
      <td>74.5(7)</td>
      <td>74.49</td>
    </tr>
    <tr>
      <td>O(1)-Pb(1)-O(5)ᵉ</td>
      <td>81.8(4)</td>
      <td>81.79</td>
      <td>O(2)-Pb(2)-O(3)ᵇ</td>
      <td>74.5(7)</td>
      <td>74.49</td>
    </tr>
    <tr>
      <td>O(5)ᵇ-Pb(1)-O(5)</td>
      <td>117.99(19)</td>
      <td>117.98</td>
      <td>O(3)-Pb(2)-O(3)ᵇ</td>
      <td>54.6(9)</td>
      <td>54.7</td>
    </tr>
    <tr>
      <td>O(5)ª-Pb(1)-O(5)ᶜ</td>
      <td>117.99(19)</td>
      <td>117.98</td>
      <td>O(2)-Pb(2)-O(4)ᶠ</td>
      <td>85.5(8)</td>
      <td>85.6</td>
    </tr>
    <tr>
      <td>O(5)ª-Pb(1)-O(5)ᵈ</td>
      <td>117.99(17)</td>
      <td>117.98</td>
      <td>O(4)ᶠ-Pb(2)-O(4)ᵍ</td>
      <td>67.0(10)</td>
      <td>67.1</td>
    </tr>
    <tr>
      <td>O(5)ᶜ-Pb(1)-O(5)ᵈ</td>
      <td>117.99(18)</td>
      <td>117.98</td>
      <td>O(3)ᵇ-Pb(2)-O(4)ᶠ</td>
      <td>115.4(7)</td>
      <td>115.4</td>
    </tr>
    <tr>
      <td>O(5)ᵇ-Pb(1)-O(5)ᵉ</td>
      <td>117.99(17)</td>
      <td>117.98</td>
      <td>O(3)-Pb(2)-O(4)ᶠ</td>
      <td>159.3(8)</td>
      <td>159.4</td>
    </tr>
    <tr>
      <td>O(5)-Pb(1)-O(5)ᵉ</td>
      <td>117.99(18)</td>
      <td>117.98</td>
      <td>O(3)ᵇ-Pb(2)-O(4)ᵍ</td>
      <td>159.3(8)</td>
      <td>159.4</td>
    </tr>
    <tr>
      <td>O(5)ᶜ-Pb(1)-O(5)</td>
      <td>161.0(7)</td>
      <td>161.0(7)</td>
      <td>O(3)-Pb(2)-O(4)ᵍ</td>
      <td>115.4(7)</td>
      <td>115.5</td>
    </tr>
    <tr>
      <td>O(5)ᵇ-Pb(1)-O(5)ᵈ</td>
      <td>161.0(7)</td>
      <td>161.0(7)</td>
      <td>O(2)-Pb(2)-O(4)ᵍ</td>
      <td>85.5(7)</td>
      <td>85.4</td>
    </tr>
    <tr>
      <td>O(5)ª-Pb(1)-O(5)ᵉ</td>
      <td>161.0(7)</td>
      <td>161.0</td>
      <td>O(1)-Pb(3)-O(3)</td>
      <td>86.5(11)</td>
      <td>86.4</td>
    </tr>
    <tr>
      <td>O(5)ª-Pb(1)-O(5)</td>
      <td>68.7(7)</td>
      <td>68.6</td>
      <td>O(1)-Pb(3)-O(2)</td>
      <td>73.7(4)</td>
      <td>73.8</td>
    </tr>
    <tr>
      <td>O(5)ᵇ-Pb(1)-O(5)ᶜ</td>
      <td>68.7(7)</td>
      <td>68.6</td>
      <td>O(1)-Pb(3)-O(2)ᵉ</td>
      <td>73.7(4)</td>
      <td>73.8</td>
    </tr>
    <tr>
      <td>O(3)ᵇ-Pb(2)-O(4)ᵍ</td>
      <td>159.3(8)</td>
      <td>159.4</td>
      <td>O(3)-Pb(3)-O(2)</td>
      <td>73.3(6)</td>
      <td>73.2</td>
    </tr>
    <tr>
      <td>O(3)-Pb(2)-O(4)ᶠ</td>
      <td>159.3(8)</td>
      <td>159.4</td>
      <td>O(3)-Pb(3)-O(2)ᵉ</td>
      <td>73.3(6)</td>
      <td>73.2</td>
    </tr>
    <tr>
      <td>O(3)-Pb(2)-O(4)ᵍ</td>
      <td>115.4(7)</td>
      <td>115.3</td>
      <td>O(2)-Pb(3)-O(2)ᵉ</td>
      <td>134.1(9)</td>
      <td>134.2</td>
    </tr>
    <tr>
      <td>O(3)ᵇ-Pb(2)-O(4)ᶠ</td>
      <td>115.4(7)</td>
      <td>115.3</td>
      <td>O(5)ᵈ-C(1)-O(5)</td>
      <td>120.0(3)</td>
      <td>120.1</td>
    </tr>
    <tr>
      <td>O(3)ᵇ-Pb(2)-O(3)</td>
      <td>54.6(9)</td>
      <td>54.7</td>
      <td>O(5)ᵈ-C(1)-O(4)</td>
      <td>120.0(17)</td>
      <td>120.1</td>
    </tr>
    <tr>
      <td>O(3)ᵉ-B(1)-O(3)ᵇ</td>
      <td>119.4(9)</td>
      <td>119.5</td>
      <td>O(5)-C(1)-O(4)</td>
      <td>120.0(17)</td>
      <td>120.1</td>
    </tr>
    <tr>
      <td>O(3)ᵉ-B(1)-O(3)</td>
      <td>119.4(9)</td>
      <td>119.5</td>
      <td>O(3)ᵇ-B(1)-O(3)</td>
      <td>119.4(9)</td>
      <td>119.3</td>
    </tr>
  </tbody>
</table>

### Figure captions

Fig. 1: (a) The crystal structure of the mixed borate-carbonate $\text{Pb}_7\text{O(OH)}_3\text{(CO}_3\text{)}_3\text{(BO}_3\text{)}$. The rectangular represents the unit cell which contains two formulas. The red ball represent O atoms, pink ball represent B atoms, light gray represent C atoms and dark gray represent Pb atoms; (b) Polyhedra of $\text{Pb}_7\text{O(OH)}_3\text{(CO}_3\text{)}_3\text{(BO}_3\text{)}$; (c) The crystal structure of the mixed borate-carbonate $\text{Pb}_7\text{(OH)}_3\text{(CO}_3\text{)}_3\text{(BO}_3\text{)}$ with one oxygen vacancy. The rectangular represents the unit cell which contains two formulas. The arrows show the oxygen vacancy. The red ball represent O atoms, pink ball represent B atoms, light gray represent C atoms and dark gray represent Pb atoms; (d) Polyhedra of $\text{Pb}_7\text{(OH)}_3\text{(CO}_3\text{)}_3\text{(BO}_3\text{)}$. The arrows show the oxygen vacancy.

Fig.2: The calculated electronic band structure of the mixed borate and carbonate $\text{Pb}_7\text{O(OH)}_3\text{(CO}_3\text{)}_3\text{(BO}_3\text{)}$ and $\text{Pb}_7\text{(OH)}_3\text{(CO}_3\text{)}_3\text{(BO}_3\text{)}$ along with the angular momentum resolved projected density of states (PDOS) of oxygen atoms of (I) and (II) crystals using LDA-mBJ. Total density of states is for unit cell (Z=2) that is 2 formula units. Partial density of states is for one atom.

Fig.3: (a,c,e,g,i) Calculated partial density of states (states/eV/ unit cell) of the mixed borate and carbonate $\text{Pb}_7\text{O(OH)}_3\text{(CO}_3\text{)}_3\text{(BO}_3\text{)}$ using LDA-mBJ; (b,d,f,h,j) Calculated partial density of states (states/eV/ unit cell) of the mixed borate and carbonate $\text{Pb}_7\text{(OH)}_3\text{(CO}_3\text{)}_3\text{(BO}_3\text{)}$ using LDA-mBJ.

Fig. 4: The electron charge density distribution of the mixed borate and carbonate $\text{Pb}_7\text{O(OH)}_3\text{(CO}_3\text{)}_3\text{(BO}_3\text{)}$ and $\text{Pb}_7\text{(OH)}_3\text{(CO}_3\text{)}_3\text{(BO}_3\text{)}$ were calculated for ; (a) (1 0 0) crystallographic plane of $\text{Pb}_7\text{O(OH)}_3\text{(CO}_3\text{)}_3\text{(BO}_3\text{)}$; (b) (1 0 0) crystallographic plane of $\text{Pb}_7\text{(OH)}_3\text{(CO}_3\text{)}_3\text{(BO}_3\text{)}$, it is clear that the (1 0 0) plane for $\text{Pb}_7\text{(OH)}_3\text{(CO}_3\text{)}_3\text{(BO}_3\text{)}$ does not show the O vacancy; (c) (1 0 1) crystallographic plane of $\text{Pb}_7\text{O(OH)}_3\text{(CO}_3\text{)}_3\text{(BO}_3\text{)}$; (d) (1 0 1) crystallographic plane of $\text{Pb}_7\text{(OH)}_3\text{(CO}_3\text{)}_3\text{(BO}_3\text{)}$, it is clear that the (1 0 1) plane for $\text{Pb}_7\text{(OH)}_3\text{(CO}_3\text{)}_3\text{(BO}_3\text{)}$ does not show the O vacancy; (e) (1 1 0) crystallographic plane of $\text{Pb}_7\text{O(OH)}_3\text{(CO}_3\text{)}_3\text{(BO}_3\text{)}$; (f) (1 1 0) crystallographic plane of $\text{Pb}_7\text{(OH)}_3\text{(CO}_3\text{)}_3\text{(BO}_3\text{)}$, the arrows show the oxygen vacancy.

![](./images/814559975937409024_3.jpg)

(a) The crystal structure of the mixed borate and carbonate $\text{Pb}_7\text{O(OH)}_3\text{(CO}_3\text{)}_3\text{(BO}_3\text{)}$. The rectangular represents the unit cell which contains two formulas. The red ball represent O atoms, pink ball represent B atoms, light gray represent C atoms and dark gray represent Pb atoms.

![](./images/814559975937409024_4.jpg)

(b) Polyhedra of $\text{Pb}_7\text{O(OH)}_3\text{(CO}_3\text{)}_3\text{(BO}_3\text{)}$.

![](./images/814559975937409024_5.jpg)

(c) The crystal structure of the mixed borate-carbonate $Pb_7(OH)_3(CO_3)_3(BO_3)$ with one oxygen vacancy.
The rectangular represents the unit cell which contains two formulas. The arrows show the oxygen vacancy.
The red ball represent O atoms, pink ball represent B atoms, light gray represent C atoms and dark gray represent Pb atoms.

![](./images/814559975937409024_6.jpg)

(d) Polyhedra of $Pb_7(OH)_3(CO_3)_3(BO_3)$. The arrows show the oxygen vacancy.

Fig1:

![](./images/814559975937409024_7.jpg)

![](./images/814559975937409024_8.jpg)

![](./images/814559975937409024_9.jpg)

![](./images/814559975937409024_10.jpg)

Fig. 3

### Crystallographic plane (1 0 0)

![](./images/814559975937409024_11.jpg)

(a) $\text{Pb}_7\text{O(OH)}_3\text{(CO}_3\text{)}_3\text{(BO}_3\text{)}$

![](./images/814559975937409024_12.jpg)

(b) $\text{Pb}_7\text{(OH)}_3\text{(CO}_3\text{)}_3\text{(BO}_3\text{)}$, it is clear that
this plane does not show the O vacancy

![](./images/814559975937409024_13.jpg)

### Crystallographic plane (1 0 1)

![](./images/814559975937409024_14.jpg)
(c) $\text{Pb}_7\text{O}(\text{OH})_3(\text{CO}_3)_3(\text{BO}_3)$

![](./images/814559975937409024_15.jpg)
(d) $\text{Pb}_7(\text{OH})_3(\text{CO}_3)_3(\text{BO}_3)$, it is clear that this plane does not show the O-vacancy

![](./images/814559975937409024_16.jpg)

# Crystallographic plane (1 1 0)

![](./images/814559975937409024_17.jpg)

(e) $\text{Pb}_7\text{O(OH)}_3\text{(CO}_3\text{)}_3\text{(BO}_3\text{)}$

![](./images/814559975937409024_18.jpg)

(f) $\text{Pb}_7\text{(OH)}_3\text{(CO}_3\text{)}_3\text{(BO}_3\text{)}$, the arrows show the O vacancy

![](./images/814559975937409024_19.jpg)

Fig. 4