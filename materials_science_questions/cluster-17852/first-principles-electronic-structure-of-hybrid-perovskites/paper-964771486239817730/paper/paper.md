
# Band gaps of hybrid metal halide perovskites: efficient estimation

Sergei M. Butorin \( ^{*} \) 

Condensed Matter Physics of Energy Materials, X-ray Photon Science, Department of Physics and Astronomy, Uppsala University, P.O. Box 516, SE-751 20 Uppsala, Sweden

E-mail: sergei.butorin@physics.uu.se

## Abstract

The employment of the parameter-free Armentio-Kümmel generalized gradient approximation (AK13-GGA) exchange functional was examined as means of the band gap prediction for hybrid metal halide perovskites (HaPs) or systems with strong spin-orbit coupling in the full-relativistic density-functional-theory (DFT) calculations. The new combination of AK13 with the nonseparable gradient approximation Minnesota correlation functional (GAM) was established as an approach allowing for the efficient band gap estimation with accuracy similar to the GW approximation method but at the computational costs of conventional DFT. This was further supported by results of the AK13/GAM calculations performed for various HaPs. The described approach creates an opportunity for the effective assessment of the electronic structure of large, complex, doped or defective HaPs and modelling of new materials.

Hybrid metal halide perovskites (HaPs) with Pb, Bi, Sn and Sb for metal are considered to be advanced materials for solar cell applications \( ^{1} \) . Related physics and chemistry depend on the size of the band gap and processes involving the states close to the valence band maximum (VBM) and conduction band minimum (CBM). However, conventional density functional theory (DFT) with usually good predictive ability fails to estimate correctly the size of the band gap in HaPs (Ref. \( ^{2} \) ) when spin-orbit coupling (SOC) is taken into account in calculations. Since SOC is significant in HaPs, it cannot be neglected. Furthermore, the role of SOC in the related processes needs to be studied. The use of hybrid functionals (e.g. Ref. \( ^{2} \) ) and the GW approximation approach (e.g. Ref. \( ^{3} \) ) help to reproduce the right band gap sizes in HaPs but require extensive computational resources making calculations difficult for compounds with large number of atoms in the unit cell and other complex systems and interfaces. There is a need for less expensive methods with similar accuracy (for example, based on applications of suitable local density approximation (LDA) or generalized gradient approximation (GGA) functionals).

For HaPs, it was suggested to use the DFT-1/2 approach \( ^{7} \)  or to take advantage of the mBJ (Ref. \( ^{8} \) ) and GLLB-SC (Ref. \( ^{9} \) ) potentials for the calculation of the electronic structure and estimation of the band gaps. The calculated band gap sizes using these methods were reported to be in fair agreement with results of the GW calculations or/and experimentally determined values for a number of HaPs. Nevertheless, while minimizing the computational cost, these methods can bear some uncertainties.

In the DFT-1/2 approach \( ^{10} \) , the parameter (cutoff radius  \( r_{cut} \) ) value needs to be set for each chemical element in the compound under study and that can cause alternative decisions on the choice of the orbital symmetry (s or p or d) for removing half an electron (or a quarter of an electron) from for the same element (see e.g. \( ^{7,11} \) ). Although, the unified optimized set
 

Table 1: Shifted k-point mesh and optimized crystal structure data (adopted from references indicated in the table) used in the calculations of the electronic structure of HaPs. Orth stands for orthorombic, tetr stands for tetragonal, mon stands for monoclinic and all the other structures are pseudocubic.

<table><tr><td>Compound</td><td>Shifted k-point mesh</td><td>Optimized crystal structure</td></tr><tr><td>MAPbCl3</td><td>10x10x10</td><td>Ref. 4</td></tr><tr><td>FAPbCl3</td><td>10x10x10</td><td>Ref. 3</td></tr><tr><td>CsPbCl3-orth</td><td>8x8x10</td><td>Ref. 5</td></tr><tr><td>MAPbBr3</td><td>10x10x10</td><td>Ref. 4</td></tr><tr><td>FAPbBr3</td><td>10x10x10</td><td>Ref. 3</td></tr><tr><td>CsPbBr3-orth</td><td>8x8x6</td><td>Ref. 5</td></tr><tr><td>MAPbI3-tetr</td><td>6x6x6</td><td>Ref. 4</td></tr><tr><td>FAPbI3</td><td>10x10x10</td><td>Ref. 4</td></tr><tr><td>CsPbI3-orth</td><td>8x8x6</td><td>Ref. 5</td></tr><tr><td>HdAPbI4-mon</td><td>4x6x6</td><td>Ref. 6</td></tr><tr><td>Cs2AgBiCl6</td><td>10x10x10</td><td>Ref. 4</td></tr><tr><td>Cs2AgBiBr6</td><td>10x10x10</td><td>Ref. 4</td></tr><tr><td>Cs2AgBiI6</td><td>10x10x10</td><td>Ref. 4</td></tr><tr><td>MASnCl3</td><td>10x10x10</td><td>Ref. 3</td></tr><tr><td>MASnBr3</td><td>10x10x10</td><td>Ref. 3</td></tr><tr><td>MASnI3</td><td>10x10x10</td><td>Ref. 3</td></tr><tr><td>CsSnI3-orth</td><td>8x6x8</td><td>Ref. 4</td></tr></table>

of the  \( r_{cut} \)  values is claimed to be transferrable from one HaP to another, in reality, these values require some re-adjustment for each compound if the criterium of obtaining the maximum band gap size is to be fulfilled. In case of the scheme using the mBJ potential \( ^{12} \) , the re-adjustment of its parameters were also required in order to reproduce the correct sizes of the band gaps in HaPs (see e.g. \( ^{8,13} \) ). The calculations using the GLLB-SC potential \( ^{14,15} \)  which were performed for HaPs (Ref. \( ^{9} \) ) did not include SOC. The unified SOC correction to the GLLB-SC-calculated band gaps was made based on results from another DFT code \( ^{9} \) .

Another scheme which can be suggested to keep the computational cost similar to standard LDA and GGA and the accuracy comparable to the GW method in case of HaPs is to use the parameter-free AK13-GGA exchange functional by Armiento and Kümmel \( ^{16} \) . Our paper suggests the optimal combination of this exchange functional with a type of the correlation functional when applied to HaPs, presents the results of calculations of the band gap sizes for various HaPs and discusses some limitations of the AK13 functional in terms of the calculated electronic structure.

To apply DFT, the Quantum Espresso v.6.8 code \( ^{17} \)  was taken advantage of. The calculations were performed in the full-relativistic mode. First, combinations of the GGA exchange functional by Armiento and Kümmel (AK13) \( ^{16} \)  (as it is defined in the LibXC v.5.1.6 library \( ^{18} \) ) with various correlation functionals were used to calculate the electronic structure of MAPbBr \( _{3} \)  (MA stands for methylammonium) and determine the size of the band gap. Then, a combination of AK13 with nonseparable-gradient-approximation Minnesota correlation functional by Yu et al. \( ^{19} \)  (GAM) was applied in electronic-structure calculations for various Pb- and Bi-based HaPs. Furthermore, for Sn-based HaPs, a combination of AK13 with LDA correlation of the Perdew and Wang type \( ^{20} \)  (PW) was also examined due to weaker SOC in those HaPs. The full-relativistic norm-conserving PBE (Perdew, Burke, and Ernzerhof \( ^{21} \) ) pseudopotentials for lead, bismuth, tin, cesium, chlorine, bromine, iodine and silver were generated by the code
 

Table 2: Band gap size in MAPbBr \( _{3} \)  calculated at various levels of theory and compared with experimental value (in units of eV).

<table><tr><td>Compound</td><td>AK13/NOC</td><td>AK13/WI</td><td>AK13/AM05</td><td>AK13/PW</td><td>AK13/GAM</td><td>Experiment</td></tr><tr><td>MAPbBr3</td><td>1.89</td><td>1.93</td><td>1.98</td><td>1.99</td><td>2.39</td><td>2.30</td></tr></table>

of the ONCVPSP v.4.0.1 package \( ^{22} \)  using input files from the SG15 database \( ^{23} \)  (see Supplementary information (SI)). An additional feature of this ONCVPSP version is its ability to check for positive ghost states. For hydrogen, carbon and nitrogen, the full-relativistic norm-conserving PBE pseudopotentials in the UPF format from the SG15 database were used. The valence configurations for the pseudopotentials were defined as 1s \( ^{1} \)  for H, 2s \( ^{2} \) 2p \( ^{2} \) for C, 2s \( ^{2} \) 2p \( ^{3} \)  for N, 3s \( ^{2} \) 3p \( ^{5} \)  for Cl, 4s \( ^{2} \) 4p \( ^{5} \)  for Br, 4s \( ^{2} \) 4p \( ^{6} \) 4d \( ^{9} \) 5s \( ^{2} \)  for Ag, 4d \( ^{10} \) 5s \( ^{2} \) 5p \( ^{2} \) for Sn, 4d \( ^{10} \) 5s \( ^{2} \) 5p \( ^{5} \)  for I, 5s \( ^{2} \) 5p \( ^{6} \) 6s \( ^{1} \)  for Cs, 5d \( ^{10} \) 6s \( ^{2} \) 6p \( ^{2} \) for Pb, and 5d \( ^{10} \) 6s \( ^{2} \) 6p \( ^{3} \)  for Bi. The plane-wave cut-off energy was set to 60 Ry. The convergence threshold for density was 1.0x10 \( ^{-12} \)  Ry. The Van der Waals correction was applied using Grimme's D2 method \( ^{24} \) . The Brillouin zone was sampled using the Monkhorst-Pack scheme \( ^{25} \)  and sizes of the k-point mesh for each compound are indicated in Table 1 (where FA stands for formamidinium). The calculations were performed for the optimized crystal structures (using the conventional unit cell) adopted from Refs. \( ^{3-5} \)  (see Table 1) where the structures were optimized using the PBEsol functional \( ^{26} \) . The structures optimized with this functional were used because it has been shown \( ^{27} \)  that AK13 is not accurate for the geometry optimization. In the case of HdAPbI \( _{4} \)  (HdA stands for NH \( _{3} \) (CH \( _{2} \) ) \( _{6} \) NH \( _{3} \) ), the experimental crystal structure from Ref. \( ^{6} \)  was used.

Initially, the AK13 functional was used without correlation in the DFT calculations \( ^{16,37-39} \) . Later, in some publications it was claimed that a combination of the AK13 with LDA (PW) correlation functional produces better results (see e.g. Refs. \( ^{40,41} \) ). Therefore, in present work, an attempt was made to find the right combination of AK13 with some correlation functional which would provide a correct result in terms of the band gap size in HaPs. Using MAPbBr \( _{3} \)  as

![](./images/964771486239817730_1.jpg)

![](./images/964771486239817730_2.jpg)

Figure 1: Bandstructure of pseudocubic MAPbBr_{3} calculated at the level of a) AK13/NOC and b) AK13/GAM theory. Zero eV is at the valence band maximum.

a test compound, a number of combinations of AK13 with various correlation functionals from LibXC were applied to calculate the electronic structure and the band gap size in this compound. As a reference point, the result of applying AK13 with no correlation (NOC) was used. In this case, the calculated band gap of MAPbBr \( _{3} \)  was 1.89 eV which is smaller than the experimentally-established value of 2.30 eV. Table 2 contains the results of only those combinations when the calculated band gap size is larger than that in the AK13/NOC case. Although,
 

Table 3: Calculated and measured band gaps of Pb- and Bi-based HaPs (in units of eV).

<table><tr><td>Compound</td><td>AK13/GAM</td><td>GW</td><td>Experiment</td></tr><tr><td>MAPbCl_{3}</td><td>2.90</td><td>3.07 (Ref. \( ^{3} \) )</td><td>2.94 (Ref. \( ^{28} \) )</td></tr><tr><td>FAPbCl_{3}</td><td>2.88</td><td>3.07 (Ref. \( ^{3} \) )</td><td>3.01 (Ref. \( ^{29} \) )</td></tr><tr><td>CsPbCl_{3}-orth</td><td>2.98</td><td>3.38 (Ref. \( ^{30} \) )</td><td>3.06 (Ref. \( ^{31} \) )</td></tr><tr><td>MAPbBr_{3}</td><td>2.39</td><td>2.34 (Ref. \( ^{3} \) )</td><td>2.22 (Ref. \( ^{28} \) )</td></tr><tr><td>FAPbBr_{3}</td><td>2.40</td><td>2.26 (Ref. \( ^{3} \) )</td><td>2.23 (Ref. \( ^{32} \) )</td></tr><tr><td>CsPbBr_{3}-orth</td><td>2.62</td><td>2.66 (Ref. \( ^{30} \) )</td><td>2.34 (Ref. \( ^{33} \) )</td></tr><tr><td>MAPbI_{3}-tetr</td><td>1.42</td><td>1.67 (Ref. \( ^{3} \) )</td><td>1.51 (Ref. \( ^{28} \) )</td></tr><tr><td>FAPbI_{3}</td><td>1.16</td><td>1.48 (Ref. \( ^{3} \) )</td><td>1.48(Ref. \( ^{32} \) )</td></tr><tr><td>CsPbI_{3}-orth</td><td>1.54</td><td>1.81 (Ref. \( ^{30} \) )</td><td>1.72 (Ref. \( ^{33} \) )</td></tr><tr><td>HdAPbI_{4}-mon</td><td>2.30</td><td></td><td>2.44 (Ref. \( ^{6} \) )</td></tr><tr><td>Cs_{2}AgBiCl_{6}</td><td>2.45</td><td>2.42 (Ref. \( ^{34} \) )</td><td>2.77 (Ref. \( ^{35} \) )</td></tr><tr><td>Cs_{2}AgBiBr_{6}</td><td>2.18</td><td>1.83 (Ref. \( ^{34} \) )</td><td>2.19 (Ref. \( ^{35} \) )</td></tr><tr><td>Cs_{2}AgBiI_{6}</td><td>1.33</td><td></td><td>1.75 (Ref. \( ^{36} \) )</td></tr></table>

using AK13 with GGA correlation functionals by Wilson and Ivanov (WI) \( ^{42} \) , Armiento and Mattsson (AM05) \( ^{43} \) , as well as with LDA (PW) correlation functional leads to increased band gaps, the calculated sizes are still smaller than the experimental value. A significant improvement in terms of agreement between calculated and measured values was obtained when AK13 was combined with GAM (see Table 2 and Fig. 1). The results stand out and calculated 2.39 eV is quite close to the experimental observation.

Consequently, the AK13/GAM combination was further used in the DFT calculations to predict the band gap sizes in the Pb- and Bi-based HaPs. Table 3 shows a comparison of the band gaps calculated at the AK13/GAM level of theory with experimental values for a number of HaPs. The published results obtained using the GW method are also included with corresponding references. For some compounds, the reported experimental data comprise a range of values for the band gap depending on whether the measurements were performed for policrystalline material in the form of powder or films or single crystals. In attempt to avoid a significant expansion of the reference list, a single, representative or average value of the measured band gap with the corresponding reference were chosen for the table.

Overall, the AK13/GAM-calculated band gaps of Pb- and Bi-based HaPs in Table 3 are in similar agreement with experimental data as the GW band gaps. For example, for APbX_{3} with X = Cl or I, the AK13/GAM band gaps are slightly underestimated while for X = Br they are slightly overestimated but the calculated values are relatively close to the measured ones. Similar predictive ability in terms of band gap estimations, as in case of the GW method, makes the AK13/GAM approach attractive for calculations for large, complex, doped or defective HaPs systems.

The AK13/GAM approach seems to work well for compounds with strong SOC but it may lead to a significant overestimation of the band gap size for compounds with relatively weak SOC. For latter compounds, combinations of AK13 with other correlation functionals may produce satisfactory results. For Sn-based HaPs, Table 4 additionally contains the band gaps calculated with the AK13/PW combination. One can see that the differences between results obtained at the AK13/GAM and AK13/PW levels of theory become less pronounced when compared to the case of Pb-based HaPs.

Another important finding when using the AK13/GAM approach for HaPs is that the energy positions of the shallow core levels are more accurately calculated as compared to the results of the PBE calculations commonly used to describe x-ray photoemission (XPS) spectra of HaPs (e.g. Refs. \( ^{[47-51]} \) ) which probe the
 

Table 4: Calculated and measured band gaps of Sn-based HaPs (in units of eV). Note that the band gap in MASnCl \( _{3} \)  was measured for the monoclinic phase.

<table><tr><td>Compound</td><td>AK13/GAM</td><td>AK13/PW</td><td>GW</td><td>Experiment</td></tr><tr><td>MASnCl3</td><td>3.57</td><td>3.47</td><td>4.02 (Ref. \( ^{3} \) )</td><td>3.61 (Ref. \( ^{44} \) )</td></tr><tr><td>MASnBr3</td><td>2.44</td><td>2.07</td><td>1.87 (Ref. \( ^{3} \) )</td><td>2.15 (Ref. \( ^{45} \) )</td></tr><tr><td>MASnI3</td><td>1.20</td><td>1.08</td><td>1.03 (Ref. \( ^{3} \) )</td><td>1.21 (Ref. \( ^{46} \) )</td></tr><tr><td>CsSnI3-orth</td><td>1.28</td><td>1.16</td><td>1.34 (Ref. \( ^{30} \) )</td><td>1.30 (Ref. \( ^{46} \) )</td></tr></table>

occupied density of states (DOS). Fig. 2 compares the total DOS of  \( CsPbBr_{3} \)  calculated using the AK13/GAM and PBE functionals with hard x-ray photoemission (HAXPES) spectrum of  \( CsPbBr_{3} \)  recorded at the incident photon energy of 4000 eV. The total DOS was broadened by Gaussian with full width at half maximum (FWHM) of 25 meV.  \( CsPbBr_{3} \)  was chosen as an example because its XPS/HAXPES spectrum contains, besides  \( Pb\ 5d_{5/2} \)  and  \( 5d_{3/2} \)  lines, the  \( Cs\ 5p_{3/2} \)  and  \( 3p_{1/2} \)  doublet close to the valence band.

![](./images/964771486239817730_3.jpg)

Figure 2: Comparison of total density of states of  \( CsPbBr_{3} \)  calculated using AK13/GAM (black curve) and PBE (green curve) functionals with the HAXPES spectrum (red curve) published in Ref. \( ^{[50]} \) . The calculated DOS curves are aligned with the HAXPES spectrum using the intensity maximum of the valence band.

An inspection of Fig. 2 reveals that in addition to the more correct description of the size of the band gap by the AK13/GAM calculations as compared to the PBE case, the energy positions of the core levels appear to be a better match for experimental ones than in the PBE case. The AK13/GAM-calculated energies of the Cs  \( 5p_{3/2,1/2} \)  levels are in good agreement with experiment while the offset of the AK13/GAM-calculated Pb  \( 5d_{5/2,3/2} \)  levels with respect to measured ones is much less than in the PBE calculations. It is interesting that the comparison of the AK13/GAM-calculated total DOS with the HAXPES spectrum suggests the Fermi level (chemical potential for electrons) position to be close to CBM, thus indicating rather the n-type semiconductor character for  \( CsPbBr_{3} \) .

Fig. 2 also shows that the width of the valence band calculated by the AK13/GAM method appears to be smaller as compared to the PBE calculations. As it was previously pointed out in Refs. \( ^{[37,39]} \) , AK13 somewhat underestimates the band dispersion, which in turn can lead to an overestimation of the effective hole and electron masses. Another discussed limitation \( ^{[52]} \)  of AK13 is a difficulty in calculations for atomically thin films often referred to as two-dimensional (2D) systems, because AK13 leads to numerical problems due to the presence of vacuum. However, there was now problem to perform the AK13/GAM calculations and obtain the band gap estimation for the layered 2D material, such as  \( HdAPbI_{4} \) .

The overall results reported here show a very useful utility of the AK13 functional for the prediction of the band gaps in HaPs. The AK13/GAM combination allows one to keep the computational cost at the level of standard DFT while providing the accuracy similar to that of the GW method. In particular, the employment of the described approach can be taken advantage of in calculations of the electronic structure of large, defective, doped or more sophisticated, newly modelled HaPs systems.

Furthermore, a comparison with experimental
 

data, which probe the occupied states, shows that the use of the AK13 functional leads to a better description of the shallow core levels in the calculated DOS of HaPs as compared to rather common PBE approach. It is an important finding since the electrons from the shallow core levels are participating in the chemical bonding.

Notes The author declare no competing financial interest.

Acknowledgement The author acknowledges the support from the Swedish Research Council (research grant 2018-05525). The computations and data handling were enabled by resources provided by the Swedish National Infrastructure for Computing (SNIC) at National Supercomputer Centre at Linköping University partially funded by the Swedish Research Council through grant agreement no. 2018-05973.

## Supporting Information Available

Input files to generate the full relativistic norm-conserving pseudopotentials using ONCVPSP v.4.0.1.

## References

(1) Kojima, A.; Teshima, K.; Shirai, Y.; Miyasaka, T. Organometal Halide Perovskites as Visible-Light Sensitizers for Photovoltaic Cells. J. Am. Chem. Soc. 2009, 131, 6050–6051.

(2) Du, M.-H. Density Functional Calculations of Native Defects in  \( CH_{3}NH_{3}PbI_{3} \) : Effects of Spin-Orbit Coupling and Self-Interaction Error. J. Phys. Chem. Lett. 2015, 6, 1461–1466.

(3) Bokdam, M.; Sander, T.; Stroppa, A.; Picozzi, S.; Sarma, D. D.; Franchini, C.; Kresse, G. Role of Polar Phonons in the Photo Excited State of Metal Halide Perovskites. Sci Rep 2016, 6, 28618.

(4) Materials Design Group (Department of Materials, Imperial College London) led by Prof. Aaron Walsh. Database of crystal structures of halide perovskites. https://github.com/WMD-group/hybrid-perovskites.

(5) Jocić, M.; Vukmirović, N. Ab-initio calculations of temperature dependent electronic structures of inorganic halide perovskites. Phys. Chem. Chem. Phys. 2023, 25, 29017–29031.

(6) Safdari, M.; Svensson, P. H.; Hoang, M. T.; Oh, I.; Kloo, L.; Gardner, J. M. Layered 2D alkyldiammonium lead iodide perovskites: synthesis, characterization, and use in solar cells. J. Mater. Chem. A 2016, 4, 15638–15646.

(7) Tao, S. X.; Cao, X.; Bobbert, P. A. Accurate and efficient band gap predictions of metal halide perovskites using the DFT-1/2 method: GW accuracy with DFT expense. Sci Rep 2017, 7, 14386.

(8) Jishi, R. A.; Ta, O. B.; Sharif, A. A. Modeling of Lead Halide Perovskites for Photovoltaic Applications. J. Phys. Chem. C 2014, 118, 28344–28349.

(9) Castelli, I. E.; García-Lastra, J. M.; Thygesen, K. S.; Jacobsen, K. W. Bandgap calculations and trends of organometal halide perovskites. APL Materials 2014, 2, 081514.

(10) Ferreira, L. G.; Marques, M.; Teles, L. K. Approximation to density functional theory for the calculation of band gaps of semiconductors. Phys. Rev. B 2008, 78, 125116.

(11) Traoré, B.; Even, J.; Pedesseau, L.; Képénekián, M.; Katan, C. Band gap, effective masses, and energy level alignment of 2D and 3D halide perovskites and heterostructures using DFT-1/2. Phys. Rev. Materials 2022, 6, 014604.

(12) Tran, F.; Blaha, P. Accurate Band Gaps of Semiconductors and Insulators with
 

a Semilocal Exchange-Correlation Poten-
tial. Phys. Rev. Lett. 2009, 102, 226401.

(13) Traoré, B.; Bouder, G.; Lafargue-Dit-Hauret, W.; Rocquefelte, X.; Katan, C.; Tran, F.; Kepenekian, M. Efficient and accurate calculation of band gaps of halide perovskites with the Tran-Blaha modified Becke-Johnson potential. Phys. Rev. B 2019, 99, 035139.

(14) Gritsenko, O.; Van Leeuwen, R.; Van Lenthe, E.; Baerends, E. J. Self-consistent approximation to the Kohn-Sham exchange potential. Phys. Rev. A 1995, 51, 1944–1954.

(15) Kuisma, M.; Ojanen, J.; Enkovaara, J.; Rantala, T. T. Kohn-Sham potential with discontinuity for band gap materials. Phys. Rev. B 2010, 82, 115106.

(16) Armiento, R.; Kummel, S. Orbital Localization, Charge Transfer, and Band Gaps in Semilocal Density-Functional Theory. Phys. Rev. Lett. 2013, 111, 036402.

(17) Giannozzi, P. et al. Advanced capabilities for materials modelling with Quantum ESPRESSO. J. Phys.: Condens. Matter 2017, 29, 465901.

(18) Lehtola, S.; Steigemann, C.; Oliveira, M. J.; Marques, M. A. Recent developments in libxc — A comprehensive library of functionals for density functional theory. SoftwareX 2018, 7, 1–5.

(19) Yu, H. S.; Zhang, W.; Verma, P.; He, X.; Truhlar, D. G. Nonseparable exchange-correlation functional for molecules, including homogeneous catalysis involving transition metals. Phys. Chem. Chem. Phys. 2015, 17, 12146–12160.

(20) Perdew, J. P.; Wang, Y. Accurate and simple analytic representation of the electron-gas correlation energy. Phys. Rev. B 1992, 45, 13244–13249.

(21) Perdew, J. P.; Burke, K.; Ernzerhof, M. Generalized Gradient Approximation Made Simple. Phys. Rev. Lett. 1996, 77, 3865–3868.

(22) Hamann, D. R. Optimized norm-conserving Vanderbilt pseudopotentials. Phys. Rev. B 2013, 88, 085117.

(23) Scherpelz, P.; Govoni, M.; Hamada, I.; Galli, G. Implementation and Validation of Fully Relativistic GW Calculations: Spin–Orbit Coupling in Molecules, Nanocrystals, and Solids. J. Chem. Theory Comput. 2016, 12, 3523–3544.

(24) Grimme, S. Semiempirical GGA-type density functional constructed with a long-range dispersion correction. J Comput Chem 2006, 27, 1787–1799.

(25) Monkhorst, H. J.; Pack, J. D. Special points for Brillouin-zone integrations. Phys. Rev. B 1976, 13, 5188–5192.

(26) Perdew, J. P.; Ruzsinszky, A.; Csonka, G. I.; Vydrov, O. A.; Scuseria, G. E.; Constantin, L. A.; Zhou, X.; Burke, K. Restoring the Density-Gradient Expansion for Exchange in Solids and Surfaces. Phys. Rev. Lett. 2008, 100, 136406.

(27) Lindmaa, A.; Armiento, R. Energetics of the AK13 semilocal Kohn-Sham exchange energy functional. Phys. Rev. B 2016, 94, 155143.

(28) Baikie, T.; Barrow, N. S.; Fang, Y.; Keenan, P. J.; Slater, P. R.; Piltz, R. O.; Gutmann, M.; Mhaisalkar, S. G.; White, T. J. A combined single crystal neutron/X-ray diffraction and solid-state nuclear magnetic resonance study of the hybrid perovskites  \( CH_{3}NH_{3}PbX_{3} \)  (X = I, Br and Cl). J. Mater. Chem. A 2015, 3, 9298–9307.

(29) Wang, J.; Peng, J.; Sun, Y.; Liu, X.; Chen, Y.; Liang, Z. FAPbCl \( _{3} \)  Perovskite as Alternative Interfacial Layer for Highly
 

Efficient and Stable Polymer Solar Cells. Adv Elect Materials 2016, 2, 1600329.

(30) Lang, L.; Zhang, Y.-Y.; Xu, P.; Chen, S.; Xiang, H. J.; Gong, X. G. Three-step approach for computing band offsets and its application to inorganic ABX \( _{3} \)  halide perovskites. Phys. Rev. B 2015, 92, 075102.

(31) Baranowski, M.; Plochocka, P.; Su, R.; Legrand, L.; Barisien, T.; Bernardot, F.; Xiong, Q.; Testelin, C.; Chamarro, M. Exciton binding energy and effective mass of  \( CsPbCl_{3} \) : a magneto-optical study. Photon. Res. 2020, 8, A50.

(32) Eperon, G. E.; Stranks, S. D.; Menelaou, C.; Johnston, M. B.; Herz, L. M.; Snaith, H. J. Formamidinium lead trihalide: a broadly tunable perovskite for efficient planar heterojunction solar cells. Energy Environ. Sci. 2014, 7, 982.

(33) Yang, Z.; Surrente, A.; Galkowski, K.; Miyata, A.; Portugall, O.; Sutton, R. J.; Haghighirad, A. A.; Snaith, H. J.; Maude, D. K.; Plochocka, P.; Nicholas, R. J. Impact of the Halide Cage on the Electronic Properties of Fully Inorganic Cesium Lead Halide Perovskites. ACS Energy Lett. 2017, 2, 1621–1627.

(34) Filip, M. R.; Hillman, S.; Haghighirad, A. A.; Snaith, H. J.; Giustino, F. Band Gaps of the Lead-Free Halide Double Perovskites  \( Cs_{2}BiAgCl_{6} \)  and  \( Cs_{2}B i Ag Br_{6} \)  from Theory and Experiment. J. Phys. Chem. Lett. 2016, 7, 2579–2585.

(35) McClure, E. T.; Ball, M. R.; Windl, W.; Woodward, P. M.  \( Cs_{2}AgBiX_{6} \)  (X = Br, Cl): New Visible Light Absorbing, Lead-Free Halide Perovskite Semiconductors. Chem. Mater. 2016, 28, 1348–1354.

(36) Creutz, S. E.; Crites, E. N.; De Siena, M. C.; Gamelin, D. R. Colloidal Nanocrystals of Lead-Free

Double-Perovskite (Elpasolite) Semiconductors: Synthesis and Anion Exchange To Access New Materials. Nano Lett. 2018, 18, 1118–1123.

(37) Vlček, V.; Steinle-Neumann, G.; Leppert, L.; Armiento, R.; Kümmel, S. Improved ground-state electronic structure and optical dielectric constants with a semilocal exchange functional. Phys. Rev. B 2015, 91, 035107.

(38) Tran, F.; Blaha, P. Importance of the Kinetic Energy Density for Band Gap Calculations in Solids with Density Functional Theory. J. Phys. Chem. A 2017, 121, 3318–3325.

(39) Tran, F.; Doumont, J.; Kalantari, L.; Huran, A. W.; Marques, M. A. L.; Blaha, P. Semilocal exchange-correlation potentials for solid-state calculations: Current status and future directions. Journal of Applied Physics 2019, 126, 110902.

(40) Cerqueira, T. F. T.; Oliveira, M. J. T.; Marques, M. A. L. Benchmarking the AK13 Exchange Functional: Ionization Potentials and Electron Affinities. J. Chem. Theory Comput. 2014, 10, 5625–5629.

(41) Borlido, P.; Schmidt, J.; Huran, A. W.; Tran, F.; Marques, M. A. L.; Botti, S. Exchange-correlation functionals for band gaps of solids: benchmark, reparametrization and machine learning. npj Comput Mater 2020, 6, 96.

(42) Wilson, L. C.; Ivanov, S. A new Wigner-like correlation-energy functional from coordinate scaling requirements. Int. J. Quant. Chem. 1998, 69, 523–532.

(43) Armiento, R.; Mattsson, A. E. Functional designed to include surface effects in self-consistent density functional theory. Phys. Rev. B 2005, 72, 085108.

(44) Wang, L.; Ou, T.; Wang, K.; Xiao, G.; Gao, C.; Zou, B. Pressure-induced structural evolution, optical and electronic
 

transitions of nontoxic organometal halide perovskite-based methylammonium tin chloride. Appl. Phys. Lett. 2017, 111, 233901.

(45) Hao, F.; Stoumpos, C. C.; Cao, D. H.; Chang, R. P. H.; Kanatzidis, M. G. Lead-free solid-state organic–inorganic halide perovskite solar cells. Nature Photonics 2014, 8, 489–494.

(46) Stoumpos, C. C.; Malliakas, C. D.; Kanatzidis, M. G. Semiconducting Tin and Lead Iodide Perovskites with Organic Cations: Phase Transitions, High Mobilities, and Near-Infrared Photoluminescent Properties. Inorg. Chem. 2013, 52, 9019–9038.

(47) Phuyal, D.; Jain, S. M.; Philippe, B.; Johansson, M. B.; Pazoki, M.; Kullgren, J.; Kvashnina, K. O.; Klintenberg, M.; Johansson, E. M. J.; Butorin, S. M.; Karis, O.; Rensmo, H. The electronic structure and band interface of cesium bismuth iodide on a titania heterostructure using hard X-ray spectroscopy. J. Mater. Chem. A 2018, 6, 9498–9505.

(48) Phuyal, D.; Safdari, M.; Pazoki, M.; Liu, P.; Philippe, B.; Kvashnina, K. O.; Karis, O.; Butorin, S. M.; Rensmo, H.; Edvinsson, T.; Kloo, L.; Gardner, J. M. Electronic Structure of Two-Dimensional Lead(II) Iodide Perovskites: An Experimental and Theoretical Study. Chem. Mater. 2018, 30, 4959–4967.

(49) Man, G. J.; Sterling, C. M.; Kamal, C.; Simonov, K. A.; Svanström, S.; Acharya, J.; Johansson, F. O. L.; Giangrisostomi, E.; Ovsyannikov, R.; Huthwelker, T.; Butorin, S. M.; Nayak, P. K.; Odelius, M.; Rensmo, H. Electronic coupling between the unoccupied states of the organic and inorganic sublattices of methylammonium lead iodide: A hybrid organic-inorganic perovskite single crystal. Phys. Rev. B 2021, 104, L041302.

(50) Man, G. J.; Kamal, C.; Kalinko, A.; Phuyal, D.; Acharya, J.; Mukherjee, S.; Nayak, P. K.; Rensmo, H.; Odelius, M.; Butorin, S. M. A-site cation influence on the conduction band of lead bromide perovskites. Nat Commun 2022, 13, 3839.

(51) Sterling, C. M.; Kamal, C.; García-Fernández, A.; Man, G. J.; Svanström, S.; Nayak, P. K.; Butorin, S. M.; Rensmo, H.; Cappel, U. B.; Odelius, M. Electronic Structure and Chemical Bonding in Methylammonium Lead Triiodide and Its Precursor Methylammonium Iodide. J. Phys. Chem. C 2022, 126, 20143–20154.

(52) Tran, F.; Doumont, J.; Kalantari, L.; Blaha, P.; Rauch, T.; Borlido, P.; Botti, S.; Marques, M. A. L.; Patra, A.; Jana, S.; Samal, P. Bandgap of two-dimensional materials: Thorough assessment of modern exchange-correlation functionals. The Journal of Chemical Physics 2021, 155, 104103.
 
![](./images/964771486239817730_4.jpg)

 
