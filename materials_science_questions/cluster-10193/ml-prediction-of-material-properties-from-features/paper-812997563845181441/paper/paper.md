# Noble-Metal High-Entropy-Alloy Nanoparticles: Atomic-Level Insight into the Electronic Structure

Dongshuang Wu,*\ Kohei Kusada,*\ Yusuke Nanba, Michihisa Koyama,*\ Tomokazu Yamamoto,
Takaaki Toriyama, Syo Matsumura, Okkyun Seo, Ibrahima Gueye, Jaemyung Kim,
Loku Singgapulige Rosantha Kumara, Osami Sakata, Shogo Kawaguchi, Yoshiki Kubota,
and Hiroshi Kitagawa*

Cite This: J. Am. Chem. Soc. 2022, 144, 3365−3369

Read Online

---

ACCESS |
Metrics & More |
Article Recommendations |
Supporting Information

---

**ABSTRACT:** The compositional space of high-entropy-alloy nanoparticles (HEA NPs) significantly expands the diversity of the materials library. Every atom in HEA NPs has a different elemental coordination environment, which requires knowledge of the local electronic structure at an atomic level. However, such structure has not been disclosed experimentally or theoretically. We synthesized HEA NPs composed of all eight noble-metal-group elements (NM-HEA) for the first time. Their electronic structure was revealed by hard X-ray photoelectron spectroscopy and density function theory calculations with NP models. The NM-HEA NPs have a lower degeneracy in energy level compared with the monometallic NPs, which is a common feature of HEA NPs. The local density of states (LDOS) of every surface atom was first revealed. Some atoms of the same constituent element in HEA NPs have different LDOS profiles, whereas atoms of other elements have similar LDOS profiles. In other words, one atom in HEA loses its elemental identity and it may be possible to create an ideal LDOS by adjusting the neighboring atoms. The tendency of the electronic structure change was shown by supervised learning. The NM-HEA NPs showed 10.8-times higher intrinsic activity for hydrogen evolution reaction than commercial Pt/C, which is one of the best catalysts.

Multimetallic alloys, including principal element- and high-entropy alloys (HEAs), generally consisting of at least five elements in roughly equal proportions, have significantly enriched the materials library because of their rich compositional and configurational spaces for more than 15 years.¹⁻³ Unlike the bulk, the fine nanoparticles (NPs) appeared only three years ago because of the difficulties in synthesis.⁴⁻⁶ To date, only a small part of the vast HEA NPs has been fabricated and utilized in applications in electrocatalysis⁷⁻¹⁴ and thermal catalysis.⁵,¹⁵⁻¹⁷ Quite recently, we reported on HEA NPs composed of all six platinum-group metals (PGM-HEA) to be highly active for complicated ethanol electrochemical oxidation with a 12-electron process, although four of the monometallic PGMs have disregardable activity.¹⁸ Likewise, the high activity of IrPdPtRhRu HEA NPs toward the hydrogen evolution reaction (HER) is largely a deviation from the famous d-band model.¹⁹,²⁰ These findings suggest a nonlinear relationship between composition and properties; that is, the properties of HEAs are not simply related to the properties of monometals. Because of the various configurations of neighboring atoms, every atom in HEA NPs has a different character, which is the intrinsic difference between HEA NPs and conventional alloys. This calls for revealing the electronic structures—in particular, the local structures—at the atomic level, which is one of the biggest challenges in the HEA field, both experimentally and theoretically.

The noble-metal group contains eight elements, i.e., Ru, Rh, Pd, Ag, Os, Ir, Pt, and Au, which are located next to each other in the periodic table. All noble metals are necessary for some important industrial processes, and they are the most studied nanocatalysts. If all eight noble metals can be arbitrarily mixed, a noble-metal HEA (NM-HEA) may have completely new or enhanced properties. Here, we synthesized NM-HEA NPs for the first time. Their electronic structure was uncovered by both experimental hard X-ray photoelectron spectroscopy (HAXPES) and density function theory (DFT) calculations with nano models. We confirmed that a common feature of HEA NPs is low degeneracy in the energy level. In particular, the atomic-level insight on the local density of states (LDOS) of every surface atom in HEA NPs is first presented. Some atoms of the same element have different LDOS profiles, and other atoms of different elements have similar LDOS profiles; i.e., the atoms in HEA NPs lose their elemental identity. A tendency of the electronic structure change was given by supervised learning. Although NM-HEA NPs contain three HER inert metals, Os, Ag, and Au, the intrinsic HER activity of the NM-HEA NPs was higher by a factor of 4.3 and 10.8 than those of highly active IrPdPtRhRu HEA NPs and the benchmarked Pt/C, respectively.

Received: December 27, 2021
Published: February 15, 2022

![](./images/812997563845181441_1.jpg)

---

© 2022 American Chemical Society
3365
https://doi.org/10.1021/jacs.1c13616
J. Am. Chem. Soc. 2022, 144, 3365−3369

The NM-HEA NPs were synthesized by adding a mixture of metal precursors (in a nearly equal atomic ratio) into preheated triethylene glycol containing polyvinylpyrrolidone as a protecting agent at 230 °C. The resultant powder was quasi-spherical NPs with a size distribution of 4.1 ± 1.2 nm (Transmission electron microscopy (TEM) image in Figure S1a). The synchrotron X-ray diffraction (XRD) pattern and the Rietveld refinement analysis show a face-centered cubic (fcc) structure with a lattice constant of 3.910(8) Å (Figure 1a). The high-resolution scanning TEM images in Figure S1b–

![](./images/812997563845181441_2.jpg)

Figure 1. (a) Synchrotron XRD of NM-HEA NPs and Rietveld refinement result. The radiation wavelength is 0.63003(7) Å. The black circles and red, blue, and gray lines are experimental data, fitting data, background line, and residual data, respectively. (b) EDX maps using the L-line characteristic X-ray from each element. The scale bar is 10 nm.

c show that most NM-HEA NPs have a polycrystalline fcc feature which is consistent with the XRD result. The energy-dispersive X-ray (EDX) maps of Figure S1b show a random distribution of each constituent over the whole NPs (Figure 1b). The atomic ratio measured by X-ray fluorescence spectroscopy was similar to the values obtained by X-ray photoemission spectroscopy (XPS) (Table S1). The doublets of 3d orbitals of Ru, Rh, Pd, and Ag and 4f orbitals of Os, Ir, Pt, and Au were detected by XPS in the range of 275–380 and 45–95 eV, respectively (core-level XPS spectra in Figure S2). Each element is in metallic state referred to the tabulated binding energy values (Table S2). These results indicate a homogeneous mixture of the constituents from the core to the surface at the atomic level, i.e., the formation of NM-HEA NPs.

The valence band (VB) spectrum of NM-HEA NPs was measured by HAXPES with a photon energy of 5.95 keV.²¹ The VB spectrum of NM-HEA NPs is featureless (Figure 2a), in contrast to monometals showing clear peaks. A similar “featureless” VB spectrum was reported in IrPdPtRhRu HEA NPs.¹⁹ Although the nanosized effect is known to influence the VB spectra, for monometallic NPs with sizes above 2 nm, the VB spectra showed a similar feature compared to the bulk.²² Therefore, the “featureless” VB spectrum of HEA NPs may be a common feature of HEA caused by the orbital hybrid. The d-

![](./images/812997563845181441_3.jpg)

Figure 2. (a) VB spectra obtained by HAXPES and (b) DOS profiles calculated by DFT for the NPs of NM-HEA, Pt, and Au.

band center ($\varepsilon_{\text{d}}$, the center of gravity of the $d$-band; see eq S7 in the Supporting Information) of the NM-HEA NPs was −4.36 eV from the VB spectrum, which is more negative than that of Pt NPs (−4.05 eV) and approaches the value of HER-inert metals such as Cu foil (−4.28 eV) and Au NPs (−5.19 eV) ($\varepsilon_{\text{d}}$ values of monometallic and HEA NPs from VB spectra in Table S3).

The VB spectrum is a summation of the electronic structures of all the atoms in a solid, which gives a few hints about the LDOS of each atom. Revealing the LDOS of realistic NPs experimentally is extremely difficult. Although several works discuss the activities with the binding energy distribution pattern using slab models of HEAs,²³,²⁴ there is no report on the deep investigation of the LDOS of HEA NPs. To this end, we revealed the (local) electronic structure of NM-HEA NPs by DFT with an NP model composed of 201 atoms for the first time. Truncated octahedral fcc models were used for NM-HEA NPs and monometallic NPs (atomic models in Figures S3, S4).²⁵

Ten configurations of NM-HEA NP were randomly selected, as the total DOS converged with 10 configurations shown in Figure S5. The DOS profile of monometallic NP is intrinsically coarse because of the quantum size effect of NP.²⁶ The NM-HEA NP possesses a smoother and more “featureless” DOS profile than monometals (Figure 2b). This reflects that the atoms in NM-HEA have various LDOS profiles because of the numerous atomic configurations and that NM-HEA has a lower degeneracy in energy level, whereas most atoms in monometals have similar LDOS profiles because of the uniform atomic configuration. Both the DOS profiles and the tendency of the calculated $\varepsilon_{\text{d}}$ values from the models are also consistent with the HAXPES results (comparing $\varepsilon_{\text{d}}$ values from VB spectra and DFT in Table S3, Os and Ir NPs are excluded),

![](./images/812997563845181441_4.jpg)

Figure 3. (a) The $\varepsilon_{\mathrm{d}}$ value of surface atoms in monometallic and NM-HEA NPs. The pink dotted lines are the average surface $\varepsilon_{\mathrm{d}}$ value of each element, respectively. (b) DFT Model 2 of NM-HEA NP. (c) The $\varepsilon_{\mathrm{d}}$ value of surface atoms in NM-HEA NP. (d) The $\varepsilon_{\mathrm{d}}$ of the surface Pt atoms in the NM-HEA NP. The other atoms are shown in white as a visual guide. (e) The $\varepsilon_{\mathrm{d}}$ value in Pt NP.

which reflects the accuracy of DFT models. The "featureless" VB structure is an intrinsic feature of HEAs.

Because catalytic reactions occur on the surface of NPs, we first focused on the $\varepsilon_{\mathrm{d}}$ values of surface atoms. The $\varepsilon_{\mathrm{d}}$ values of all surface atoms were calculated (Figure 3a). The average $\varepsilon_{\mathrm{d}}$ value of the surface atoms of each element (pink dotted lines) in NM-HEA NPs is different from the value in their corresponding monometallic NPs (Figure 3a, $\varepsilon_{\mathrm{d}}$ values of 10 NM-HEA models in Figure S6, $\varepsilon_{\mathrm{d}}$ values from VB spectra and DFT calculations in Table S3 and S4). The atoms of each element in NM-HEA NPs showed a wider range of $\varepsilon_{\mathrm{d}}$ value distribution range than the monometallic NPs. For example, the $\varepsilon_{\mathrm{d}}$ value distribution of surface atoms in a Pt NP was in the range of -2.37 to -2.57 eV depending on the location of the Pt atoms (edge, terrace, vertices, etc.). While the $\varepsilon_{\mathrm{d}}$ value range of Pt atoms in NM-HEA NPs was -2.07 to -3.46 eV, which covers the range of monometallic Ru, Rh, Os, Ir, Pt, and Au NPs. The $\varepsilon_{\mathrm{d}}$ values for Au and Ag atoms in monometallic NPs were much more negative than for the other elements, which is the intrinsic reason that Au and Ag are basically inert for catalysis. By contrast, in NM-HEA, some Ag and Au atoms have less negative $\varepsilon_{\mathrm{d}}$ values than the corresponding monometallic NP, with similar $\varepsilon_{\mathrm{d}}$ positions to some Ru, Os, Ir, and Pt atoms. Figure 3c shows the $\varepsilon_{\mathrm{d}}$ values of the surface atoms in the NM-HEA (Figure 3b), which covers the range from -3.4 to -2.0 eV. In monometallic Pt NP, the surface atoms located on the same facets have similar $\varepsilon_{\mathrm{d}}$ values (Figure 3e). By contrast, the $\varepsilon_{\mathrm{d}}$ value of every surface Pt atom in NM-HEA NP was different (Figure 3d).

Further, we revealed for the first time a tendency of the electronic structure with a different elemental environment by supervised learning. For each element, the $\varepsilon_{\mathrm{d}}$ values of the surface atoms obtained by DFT were expressed as a multiple regression equation, where the elemental-based CN is a descriptor. The model accuracy is demonstrated by the mean absolute error (MAE < 0.15 eV) and the predictive square correlation coefficient, $R_{\mathrm{LOO}}{}^{2} > 0.5$ (LOO: leave-one-out method, Figure S7 and Table S5), for Ru, Rh, Pd, Os, Ir, and Pt. We note that Au and Ag have a low $R_{\mathrm{LOO}}{}^{2}$ because of their $d^{10}$ electronic configuration. $^{27}$ The average regression coefficients shown in Figure S8 suggest that the $\varepsilon_{\mathrm{d}}$ value shift is more negative when neighbored with Ru or Ir and less negative or even slightly positive if neighbored with Au and Ag in the NM-HEA NPs.

A DOS profile can provide a more accurate interpretation than the $\varepsilon_{\mathrm{d}}$ values on the properties of alloys. $^{28}$ In monometallic NPs, the LDOS profile of an atom changes with the coordination number (CN), which is associated with the atom position (the CN and LDOS profiles of Pt NP in Figure S9). The situation becomes quite different in HEA NPs. Although these Ru atoms have the same CN of 6 (only considering the nearest neighboring atoms), their $\varepsilon_{\mathrm{d}}$ and band profiles are completely different depending on the configuration of the neighboring elements (Figure 4a). We also found that some different elements, Ru, Rh, Os, and Ir, have similar LDOS profiles (Figure 4b). These results suggest that an element in an HEA NP could lose its identity and the properties of HEA NPs cannot be determined directly based on the monometals.

To demonstrate the influence of unique electronic structure of HEA NPs, we tested HER activity by rotation disk electrode in $0.15\ \mathrm{M}\ \mathrm{H}_{2}\mathrm{SO}_{4}$ (see experimental details in the Supporting Information). It is assumed that NM-HEA NPs have a much weaker interaction with H and a lower HER activity compared with Pt NPs based on the linear relationship in the d-band model. $^{29}$ Considering the poor HER activities of Os, Ag, and

![](./images/812997563845181441_5.jpg)

Figure 4. LDOS profiles of (a) four Ru atoms with CN = 6 and (b) Ru, Rh, Os, and Ir atoms on the surface of NM-HEA NPs. The right panel shows the first-shell neighboring atoms of the target atoms.

Au, the NM-HEA NPs are also supposed to have a lower HER activity than IrPdPtRhRu HEA NPs. Nevertheless, the NM-HEA NPs showed a higher turnover frequency, by a factor of 4.3 and 10.8, than IrPdPtRhRu HEA NPs and benchmarked Pt/C catalyst, respectively (Figures S10 and S11, geometric HER activity, copper underpotential deposition data, and TOF), which is one of the best HER activities among the reported catalysts. Such high activity also verified the calculation results mentioned above. Some of the unreactive Os, Au, and Ag atoms in HEA can possess suitable LDOS profiles for HER. On the other hand, adding these three elements to active IrPdPtRhRu HEA NPs changes the LDOS of the other elements and might enhance the HER kinetics.

In summary, HEA NPs using all eight noble metals were synthesized for the first time, and their electronic structure was revealed both experimentally and theoretically. The LDOS of surface atoms of HEA NPs was also first discussed. The HEA NPs intrinsically have a broad VB spectrum because of the diversity of LDOS. The unreactive elements could function directly as active sites or indirectly as useful neighboring atoms of the active center for certain reactions if they exist in the HEA matrix. The DFT and supervised learning results show that one atom can lose its elemental identity in an HEA matrix and suitable LDOS could be obtained by adjusting the elemental environment. The wide $\varepsilon_{\text{d}}$ value distribution of the atoms in NM-HEA NPs also suggested the possibility of highly efficient catalysts for complicated reactions requiring diverse adsorption energy levels.

## ASSOCIATED CONTENT

### Supporting Information
The Supporting Information is available free of charge at https://pubs.acs.org/doi/10.1021/jacs.1c13616.

Experimental details and theoretical calculations, TEM, XPS spectra, models of calculation, electrochemistry data, and Tables (PDF)

## AUTHOR INFORMATION

### Corresponding Authors
Dongshuang Wu – Division of Chemistry, Graduate School of Science, Kyoto University, Kyoto 606-8502, Japan;
orcid.org/0000-0001-8512-8473;
Email: dongshuangwu@kuchem.kyoto-u.ac.jp

Kohei Kusada – Division of Chemistry, Graduate School of Science, Kyoto University, Kyoto 606-8502, Japan; The HAKUBI Center for Advanced Research, Kyoto University, Kyoto 606-8502, Japan; JST-PRESTO, Saitama 332-0012, Japan; orcid.org/0000-0002-9679-6749;
Email: kusada@kuchem.kyoto-u.ac.jp

Michihisa Koyama – Research Initiative for Supra-Materials, Shinshu University, Nagano 380-8553, Japan; Open Innovation Institute, Kyoto University, Kyoto 606-8501, Japan; Email: koyama_michihisa@shinshu-u.ac.jp

Hiroshi Kitagawa – Division of Chemistry, Graduate School of Science, Kyoto University, Kyoto 606-8502, Japan;
orcid.org/0000-0001-6955-3015; Email: kitagawa@kuchem.kyoto-u.ac.jp

### Authors
Yusuke Nanba – Research Initiative for Supra-Materials, Shinshu University, Nagano 380-8553, Japan; orcid.org/0000-0002-1692-4465

Tomokazu Yamamoto – The Ultramicroscopy Research Center, Kyushu Uiversity, Fukuoka 819-0395, Japan

Takaaki Toriyama – The Ultramicroscopy Research Center, Kyushu Uiversity, Fukuoka 819-0395, Japan

Syo Matsumura – The Ultramicroscopy Research Center, Kyushu Uiversity, Fukuoka 819-0395, Japan; Department of Applied Quantum Physics and Nuclear Engineering, Kyushu University, Fukuoka 819-0395, Japan

Okkyun Seo – Center for Synchrotron Radiation Research, Japan Synchrotron Radiation Research Institute (JASRI), Sayo-gun, Hyogo 679-5198, Japan; Research Network and Facility Services Division, National Institute for Materials Science (NIMS), Sayo-gun, Hyogo 679-5148, Japan;
orcid.org/0000-0002-8732-0255

Ibrahima Gueye – Research Network and Facility Services Division, National Institute for Materials Science (NIMS), Sayo-gun, Hyogo 679-5148, Japan; orcid.org/0000-0001-5296-3894

Jaemyung Kim – Research Network and Facility Services Division, National Institute for Materials Science (NIMS), Sayo-gun, Hyogo 679-5148, Japan; orcid.org/0000-0002-3298-2972

Loku Singgapulige Rosantha Kumara – Center for Synchrotron Radiation Research, Japan Synchrotron Radiation Research Institute (JASRI), Sayo-gun, Hyogo 679-5198, Japan; Research Network and Facility Services Division, National Institute for Materials Science (NIMS), Sayo-gun, Hyogo 679-5148, Japan

Osami Sakata – Center for Synchrotron Radiation Research, Japan Synchrotron Radiation Research Institute (JASRI), Sayo-gun, Hyogo 679-5198, Japan; Research Network and Facility Services Division, National Institute for Materials Science (NIMS), Sayo-gun, Hyogo 679-5148, Japan

Shogo Kawaguchi – Center for Synchrotron Radiation Research, Japan Synchrotron Radiation Research Institute (JASRI), Sayo-gun, Hyogo 679-5198, Japan

Yoshiki Kubota – Department of Physical Science, Osaka Prefecture University, Sakai, Osaka 599-8531, Japan

Complete contact information is available at:
https://pubs.acs.org/10.1021/jacs.1c13616

Notes
The authors declare no competing financial interest.

### ACKNOWLEDGMENTS
We acknowledge the support from a Grant-in-Aid for Specially Promoted Research, No. 20H05623. Synchrotron XRD measurements were carried out on beamline BL02B2 at SPring-8 under Proposal Nos. 2020A1162 and 2020A0528. HAXPES measurements were carried out on beamline BL15XU at SPring-8 under proposal Nos. 2020A4952 and 2020A4905. STEM analyses were performed as a part of a program conducted by the Advanced Characterization Nano- technology Platform sponsored by the Ministry of Education, Culture, Sports, Science and Technology (MEXT) of the Japanese government.

### REFERENCES
(1) Yeh, J.; Chen, S.; Gan, J.; Chin, T.; Shun, T.; Tsau, C.; Chang, S. Formation of simple crystal structures in Cu-Co-Ni-Cr-Al-Fe-Ti-V alloys with multiprincipal metallic elements. Metall. Mater. Trans. A 2004, 35, 2533−2536.

(2) Miracle, D.; Senkov, O. A critical review of high entropy alloys and related concepts. Acta Mater. 2017, 122, 448−511.

(3) George, E.; Raabe, D.; Ritchie, R. High-entropy alloys. Nat. Rev. Mater. 2019, 4, 515−534.

(4) Chen, P.; Liu, X.; Hedrick, J.; Xie, Z.; Wang, S.; Lin, Q.; Hersam, M.; Dravid, V.; Mirkin, C. Polyelemental nanoparticle libraries. Science 2016, 352, 1565−1569.

(5) Yao, G.; Huang, Z.; Xie, P.; Lacey, S.; Jacob, R.; Xie, H.; Chen, F.; Nie, A.; Pu, T.; Rehwoldt, M.; Yu, D.; Zachariah, M.; Wang, C.; Shahbazian-Yassar, R.; Li, J.; Hu, L. Carbothermal shock synthesis of high-entropy-alloy nanoparticles. Science 2018, 359, 1489−1494.

(6) Feng, J.; Chen, D.; Pikhitsa, P.; Jung, Y.; Yang, J.; Choi, M. Unconventional alloys confined in nanoparticles: building blocks for new matter. Matter 2020, 3, 1646−1663.

(7) Glasscott, M.; Pendergast, A.; Goines, S.; et al. Electrosynthesis of high-entropy metallic glass nanoparticles for designer, multifunc- tional electrocatalysis. Nat. Commun. 2019, 10, 2650.

(8) Löffler, T.; Savan, A.; Meyer, H.; Meischein, M.; Strotkotter, V.; Ludwig, A.; Schuhmann, W. Design of Complex Solid-Solution Electrocatalysts by Correlating Configuration, Adsorption Energy Distribution Patterns, and Activity Curves. Angew. Chem., Int. Ed. 2020, 59, 5844−5850.

(9) Feng, G.; Ning, F.; Song, J.; Shang, H.; Zhang, K.; Ding, Z.; Gao, P.; Chu, W.; Xia, D. Sub-2 nm ultrasmall high-entropy alloy nanoparticles for extremely superior electrocatalytic hydrogen evolution. J. Am. Chem. Soc. 2021, 143, 17117.

(10) Nellaiappan, S.; Katiyar, N.; Kumar, R.; Parui, A.; Malviya, K.; Pradeep, K.; Singh, A.; Sharma, S.; Tiwary, C.; Biswas, K. High- entropy alloys as catalysts for the CO₂ and CO reduction reactions: experimental realization. ACS Catal. 2020, 10, 3658−3663.

(11) Zhan, C.; Xu, Y.; Bu, L.; Zhu, H.; Feng, Y.; Yang, T.; Zhang, Y.; Huang, B.; Shao, Q.; Huang, X. Subnanometer high-entropy alloy nanowires enable remarkable hydrogen oxidation catalysis. Nat. Commun. 2021, 12, 6261.

(12) Zhang, D.; Zhao, H.; Wu, X.; Deng, Y.; Wang, Z.; Han, Y.; Li, H.; Shi, Y.; Chen, X.; Li, S.; Lai, J.; Huang, B.; Wang, L. Multi-site electrocatalysts boost pH-universal nitrogen reduction by high- entropy alloys. Adv. Funct. Mater. 2021, 31, 2006939.

(13) Li, H.; Han, Y.; Zhao, H.; Qi, W.; Zhang, D.; Yu, Y.; Cai, W.; Li, S.; Lai, J.; Huang, B.; Wang, L. Fast site-to-site electron transfer of high-entropy alloy nanocatalysts driving redox electrocatalysis. Nat. Commun. 2020, 11, 5437.

(14) Gao, S.; Hao, S.; Huang, Z.; Yuan, Y.; Han, S.; Lei, L.; Zhang, X.; Shahbazian-Yassar, R.; Lu, J. Synthesis of high-entropy alloy nanoparticles on supports by the fast moving bed pyrolysis. Nat. Commun. 2016, 11, DOI: 10.1038/s41467-020-15934-1.

(15) Song, B.; Yang, Y.; Yang, T.; He, K.; Hu, X.; Yuan, Y.; Dravid, V.; Zachariah, M.; Saidi, W.; Liu, Y.; Shahbazian-Yassar, R. Revealing high-temperature reduction dynamics of high-entropy alloy nano- particles vis in situ transmission electron microscopy. Nano Lett. 2021, 21, 1742−1748.

(16) Xie, P.; Yao, Y.; Huang, Z.; Liu, Z.; Zhang, J.; Li, T.; Wang, G.; Shahbazian-Yassar, R.; Hu, L.; Wang, C. Highly efficient decom- position of ammonia using high-entropy alloy catalysts. Nat. Commun. 2019, 10, 4011.

(17) Mori, K.; Hashimoto, N.; Kamiuchi, N.; Yoshida, H.; Kobayashi, H.; Yamashita, H. Hydrogen spillover-driven synthesis of high-entropy alloy nanoparticles as a robust catalyst for CO2 hydrogenation. Nat. Commun. 2021, 12, 3884.

(18) Wu, D.; Kusada, K.; Yamamoto, T.; Toriyama, T.; Matsumura, S.; Kawaguchi, S.; Kubota, Y.; Kitagawa, H. Platinum-group-metal high-entropy-alloy nanoparticles. J. Am. Chem. Soc. 2020, 142, 13833−13838.

(19) Wu, D.; Kusada, K.; Yamamoto, T.; Toriyama, T.; Matsumura, S.; Gueye, I.; Seo, O.; Kim, J.; Hiroi, S.; Sakata, O.; Kawaguchi, S.; Kubota, Y.; Kitagawa, H. On the electronic structure and hydrogen evolution reaction activity of platinum group metal-based high- entropy-alloy nanoparticle. Chem. Sci. 2020, 11, 12731−12736.

(20) Hammer, B.; Nørskov, J. K. Theoretical surface science and catalysis - calculations and concepts. Adv. Catal. 2000, 45, 71−129.

(21) Chen, Y.; Sakata, O.; Nanba, Y.; Kumara, L.; Yang, A.; Song, C.; Koyama, M.; Li, G.; Kobayashi, H.; Kitagawa, H. Electronic origin hydrogen storage in MOF-covered palladium nanocubes investigated by synchrotron X-rays. Commun. Chem. 2018, 1, 61.

(22) Song, C.; Yang, A.; Sakata, O.; Kumara, L.; Hiroi, S.; Cui, Y.; Kusada, K.; Kobayashi, H.; Kitagawa, H. Size effects on rhodium nanoparticles related to hydrogen-storage capability. Phys. Chem. Chem. Phys. 2018, 20, 15183−15191.

(23) Batchelor, T.; Pedersen, J.; Winther, S.; Castelli, I.; Jacobsen, K.; Rossmeisl, J. High-entropy alloys as a discovery platform for electrocatalysis. Joule 2019, 3, 834−845.

(24) Lu, Z.; Chen, Z.; Singh, C. Neutral network-assisted development of high-entropy alloy catalysts: decoupling ligand and coordination effects. Matter 2020, 3, 1318−1333.

(25) Nanba, Y.; Koyama, M. NO adsorption on 4d and 5d transition-metal (Rh, Pd, Ag, Ir, and Pt) nanoparticles: density functional theory study and supervised learning. J. Phys. Chem. C 2019, 123, 28114−28122.

(26) Kubo, R. Electronic Properties of Metallic Fine Particles. J. Phys. Soc. Jpn. 1962, 17, 975−986.

(27) Ou, L.; Chen, S. DFT calculation analysis of oxygen reduction reaction activity and stability of bimetallic catalysts with Pt-segregated surface. Sci. China: Chem. 2015, 58, 586−592.

(28) Vojvodic, A.; Nørskov, J.; Abild-Pedersen, F. Electronic structure effects in transition metal surface chemistry. Top. Catal. 2014, 57, 25−32.

(29) Zeradjanin, A.; Grote, J.; Polymeros, G.; Mayrhofer, K. A critical review on hydrogen evolution electrolysis: reexploring the volcano-relationship. Electrolysis 2016, 28, 2256−2269.