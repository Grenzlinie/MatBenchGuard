# Preparation of Fe-N-C catalysts with $FeN_x$ ($x=1,3$, 4) active sites and comparison of their activities for the oxygen reduction reaction and performances in proton exchange membrane fuel cells†

Yongcheng Li, $^{a}$ Xiaofang Liu, $^{a}$ Lirong Zheng, $^{b}$ Jiaxiang Shang, $^{*a}$ Xin Wan, $^{a}$ Riming Hu, $^{a}$ Xu Guo, $^{a}$ Song Hong $^{c}$ and Jianglan Shui $^{*a}$

The active sites of Fe-N-C catalysts are nitrogen coordinated iron atoms, $FeN_x$ ($x=1-5$), that have five possible coordination numbers. $FeN_4$ active sites are commonly reported, but active sites with other coordination numbers are rarely prepared and compared with $FeN_4$ for the oxygen reduction reaction (ORR) in proton exchange membrane fuel cells (PEMFCs). Herein, Fe-N-C catalysts with different coordination numbers but similar active site densities are synthesized. Combined with theoretical calculations, the effects of $FeN_x$ coordination number $x$ on the ORR activity and PEMFC performance are systematically investigated. It is found that the annealing temperature is the key to tailoring the coordination number of $FeN_x$. The ORR activity and PEMFC performance follow the order $FeN_4 > FeN_3 > FeN_1$. $FeN_4$ delivers almost $1.7\times$ and $2.9\times$ peak power densities, and $2\times$ and $14\times$ current densities (at 0.7 V) compared with $FeN_3$ and $FeN_1$, respectively. Theoretical calculations demonstrate an "inverted volcano" relationship for the formation energy and a "volcano" relationship for the ORR activity as a function of coordination number $x=1-5$. $FeN_4$ was proved to have the lowest formation energy, the highest ORR activity and the best PEMFC performance among the five types of $FeN_x$ ($x=1-5$). This research provides a deep insight into the differences among $FeN_x$ active sites of Fe-N-C catalysts.

## 1. Introduction

M-N-C ($M = Fe, Co, Ni, etc.$) materials are attractive non-precious metal catalysts (NPMCs) for electrochemical reactions. $^{1-7}$ Their active sites are nitrogen-coordinated transition metal atoms ($MN_x$ species) hosted by porous carbon. $^{8-11}$ The coordination number $x$ of $MN_x$ affects its catalytic function by tuning the charge distribution of the active site. $^{12-16}$ For example, the $CoN_2$ site was reported to have carbon dioxide reduction reaction ($CO_2RR$) activity superior to that of $CoN_4$ and $CoN_3$. $^{12}$ $CoN_4$ was calculated to be more active than $CoN_x$ ($x=1-3$) for the oxygen evolution reaction (OER), oxygen reduction reaction (ORR) and hydrogen evolution reaction (HER). $^{17,18}$

The Fe-N-C catalyst is currently the most active NPMC for the ORR in acidic media and thus a promising alternative to the costly catalyst Pt/C for application in proton exchange membrane fuel cells (PEMFCs). Highly active Fe-N-C could deliver significantly high PEMFC performances, *e.g.* volumetric current densities of $320-450$ A cm$^{-3}$ at $0.8\ V_{IR-free}^{19-21}$ and an areal current density of $0.047$ A cm$^{-2}$ at $0.88\ V_{IR-free}^{22}$ In most Fe-N-C catalyst studies, the dominant active sites are four nitrogen coordinated iron atoms, *i.e.* $FeN_4$, which are usually produced by high temperature pyrolysis. $^{23-28}$ The $FeN_x$ active sites of Fe-N-C could theoretically have five coordination numbers $x=1-5$. Although people are familiar with $FeN_4$ active sites, the relative ORR activities and PEMFC performances of other types of $FeN_x$ active sites remain unclear and are still under debate. For example, $FeN_5$ with five coordination sites, which was prepared by grafting iron phthalocyanine on graphene or an iron porphyrin on carbon nanotubes, was reported to exhibit excellent ORR activity in acid. $^{29,30}$ However, pyrolyzed $FeN_5$ only exhibited ordinary ORR activity. $^{31}$ Although $FeN_4$ is the generally accepted favorable active site prepared through high-temperature pyrolysis, Kabir *et al.* reported that double carbon vacancy based $FeN_3$ ($DV-FeN_3/C$) has a favorable formation energy and can form during high-temperature synthesis. $^{32}$ The diversity of $FeN_x$ active sites and various ORR

---

$^{a}$School of Materials Science and Engineering, Beihang University, No. 37 Xueyuan Road, Beijing 100083, China. E-mail: shangjx@buaa.edu.cn; shuijianglan@buaa.edu.cn  
$^{b}$Beijing Synchrotron Radiation Facility, Institute of High Energy Physics, Chinese Academy of Sciences, No. 19 Yuquan Road, Beijing 100049, China  
$^{c}$State Key Laboratory of Chemical Resources Engineering Beijing Key Laboratory of Electrochemical Process and Technology for Materials, China  
† Electronic supplementary information (ESI) available: Details of experimental methods, electrochemical measurements and DFT calculations, and supplemental figures and tables. See DOI: 10.1039/c9ta08532g

activities arouse curiosity about the effect of $FeN_x$ coordination number $x$ on Fe-N-C PEMFC performance, which has not been investigated yet.

The ideal Fe-N-C catalysts are the key to the investigation of the effect of coordination number $x$. The ideal materials should meet three preconditions. First, the $FeN_x$ active site density on each catalyst should be the same or very similar, with only different Fe-N coordination numbers. Second, the catalysts should have identical morphology and porosity, because these parameters affect the mass transport and active site utilization. Third, the material should preferably be single-atom catalysts (SACs) to exclude the interference of metal nanoparticles. It is reported that controlling the temperature is an effective way to tailor M-N coordination numbers for M-N-C catalysts. For example, Wang et al. $^{12}$ adjusted the Co-N coordination number of Co-N-C catalysts to 2, 3 and 4 by regulating the heat treatment temperature to 800, 900 and 1000 °C, respectively. Liu et al. $^{15}$ synthesized $FeN_x$ ($x = 4$-$6$) on a nano-MgO sacrificial template by varying the synthesis temperature from 600 to 800 °C. Although several M-N-C catalysts with varying coordination numbers have been synthesized, an ideal group of Fe-N-C catalysts is still lacking.

Herein, Fe-N-C SACs (named FeNC-300, FeNC-500, and FeNC-1000) with identical morphology and very similar content of atomic $FeN_x$ active sites but different Fe-N coordination numbers were prepared by heating pre-carbonized ZIF-8 nanoparticles (NPs) with adsorbed $Fe^{3+}$ ions at different temperatures of 300, 500 and 1000 °C. The synthesized FeNC-300, -500, and -1000 were speculated to have active sites of $FeN_1$, $FeN_3$ and $FeN_4$, respectively, which showed an order of PEMFC performance of $FeN_4 > FeN_3 > FeN_1$, consistent with the order of ORR activity. The theoretical calculations reveal an "inverted volcano" relationship for the formation energy and a "volcano" relationship for the ORR activity of Fe-N-C catalysts as a function of $FeN_x$ coordination number $x$. The order of ORR activity is determined to be $FeN_4 > FeN_3 > FeN_2 > FeN_1 > FeN_5$. Among all $FeN_x$ active sites, $FeN_4$ (FeNC-1000) was experimentally and theoretically proven to have the lowest formation energy, and the highest ORR activity and PEMFC performance.

## 2. Results and discussion

### 2.1. Catalyst preparation and structural characterization
ZIF-8 is a commonly used precursor for preparing Fe-N-C catalysts because of its high specific surface area, abundant nitrogen and micropores that benefit hosting numerous atomic $FeN_x$ species. $^{33,34}$ In this work, ZIF-8 was selected as the precursor to prepare three Fe-N-C catalysts, which have exclusive atomic $FeN_x$ active sites with different Fe-N coordination numbers. An illustration of the preparation is shown in Scheme 1. The experimental details are provided in the ESI. $\dagger$ Briefly, ZIF-8 NPs were synthesized by a liquid phase method, and pyrolyzed to nitrogen-doped carbon (N/C*) NPs (see Fig. S1$\dagger$ for the scanning electron microscopy (SEM) image and X-ray diffraction (XRD) pattern of ZIF-8). $FeCl_3$ solution was added into the N/C* suspension to prepare N/C* (Fe@N/C*) NPs with anchored $Fe^{3+}$, which were then heat-treated at different temperatures of 300, 500 and 1000 °C in an argon atmosphere (labeled as FeNC-300, FeNC-500 and FeNC-1000, respectively). Since the pyrolysis temperatures of $800$-$1050$ °C$^{8,24,26,35-40}$ are commonly used for preparing $FeN_4$ species, we chose 1000 °C to prepare $FeN_4$ dominant Fe-N-C SACs. For most other synthesis methods, polymer or MOF materials are usually directly used as carbon sources. Thus, $FeN_4$ active sites are formed during the high temperature carbonization process. $^{41-44}$ In our work, however, Fe ions were adsorbed on the pre-carbonized ZIF-8. In this case, high-temperature annealing is not necessary for the coordination of Fe ions with the doped N, which provides an opportunity to adjust the coordination number $x$ of $FeN_x$ by controlling the pyrolysis temperature. The obtained N/C and FeNC-300/500/1000 maintain the dodecahedron shape of ZIF-8 with a size of approximately 100 nm (Fig. 1a and S2a-d$\dagger$). The Brunauer-Emmett-Teller (BET) results show that FeNC-300, -500, and -1000 have a microporous structure with similar specific surface areas of 948, 1054 and 1188 $m^2$ $g^{-1}$, respectively (Fig. S3 and Table S1$\dagger$).

![](./images/812715971625091074_1.jpg)

Scheme 1 Schematic illustration of the synthesis of FeNC-300/500/1000 with different Fe-N coordination numbers.

To exclude the possible agglomeration of adsorbed Fe ions, we first performed XRD detection and the results only show diffraction peaks of carbon without crystal Fe in FeNC-300/500/1000 (Fig. S4$\dagger$). Generally, high heating temperatures tend to cause severe agglomeration of adsorbed Fe ions. We characterized the highest temperature treated sample FeNC-1000 using transmission electron microscopy (TEM), high-resolution TEM (HRTEM), sub-angstrom-resolution high-angle annular dark field scanning TEM (HAADF-STEM) and elemental mapping. TEM and HRTEM images preliminarily exclude the presence of Fe NPs in the sample (Fig. S2e$\dagger$ and 1b). The elemental mapping shows uniformly distributed Fe and N elements on carbon NPs (Fig. 1c and S5$\dagger$). HAADF-STEM further directly reveals the atomically dispersed Fe atoms in FeNC-1000 as highlighted by circles (Fig. 1d). Since the residual Zn could not be completely excluded from the carbonized ZIF-8 (Table S2$\dagger$), and the sizes of atomic Fe and Zn are similar, the observed bright dots in Fig. 1d possibly contain Zn atoms. However, the presence of Zn did not influence the ORR activity of the catalysts as discussed later. The X-ray photoelectron spectroscopy (XPS)

![](./images/812715971625091074_2.jpg)

Fig. 1 (a) SEM, (b) HRTEM, (c) STEM and the corresponding elemental mapping images, and (d) HAADF-STEM image of FeNC-1000. (e) Fourier-transformed EXAFS spectra of FeNC-300/500/1000 with references.

characterization results of Fe and N elements are shown in Fig. S6 and S7, and Table S3.† With the increase of heating temperature, the content of the N coordinated with Fe (Fe–N) increases while the content of pyridinic N decreases, suggesting that some pyridinic nitrogen was converted to metal-coordinated N. The Fe contents determined by XPS are similar, *i.e.* 3.77, 3.83 and 3.91 wt% for FeNC-300/500/1000, respectively. In comparison, the Fe contents determined by the inductively coupled plasma (ICP) technique are approximately 0.20–0.25 wt% (Table S2†). We also measured the Fe content by the thermogravimetric (TG) technique and the results show that FeNC-300, -500, and -1000 contain 0.8, 1.2 and 0.9 wt% Fe after deducting the contribution of residual Zn [Fig. S8†]. The large difference in Fe content measured by XPS and ICP demonstrates that the Fe atoms are preferentially distributed on the surface of FeNC-300/500/1000. This surface enrichment of Fe atoms maximizes the utilization of FeNₓ active sites and benefits the catalyst performance.

To explore the coordination structure of Fe atoms in FeNC-300/500/1000, we characterized the samples using X-ray absorption spectroscopy (XAS). The Fourier transformed extended X-ray absorption fine structure (FT-EXAFS) spectra in Fig. 1e show that FeNC-300, -500, and -1000 have a main peak around 1.48 Å, which could be assigned to Fe–N (or Fe–O/Fe–C, which cannot be distinguished from Fe–N) coordination by comparing with the references of iron phthalocyanine (FePc) and ferric oxide (Fe₂O₃). The absence of the Fe–Fe peak (Fe-foil) rules out the existence of Fe NPs or clusters in the three samples. In addition, the positions of absorption edges of the X-ray absorption near-edge structure (XANES) spectra at the Fe K edge for FeNC-300/500/1000 are far away from that of the Fe-foil spectrum (Fig. S9†). These results indicate that the Fe element is possibly in the atomically dispersed FeNₓ species on FeNC-300/500/1000. According to the EXAFS fitting results in *R* space (see Fig. 2 and Table S4†), the optimized Fe–N coordination numbers are 1.0, 2.8 and 4.0 in the first shell for samples FeNC-300/500/1000, respectively. This fitting result is supported by the above XPS results. Besides, the intensity of the Fe–N peak increases slightly from FeNC-300 to FeNC-500 and to FeNC-1000, which may imply an increase in the N coordination number around the Fe center as reported by Wang *et al.*⁴⁵ The secondary peaks around 2.5 Å may belong to the Fe–C bonds in the high shells around the Fe center. The active site models of FeNC-300/500/1000 are given in the inset of Fig. 2. The N coordination numbers are speculated to be 1, 3 and 4 for FeNC-300/500/1000, respectively. Overall, FeNC-300, -500, and -1000 have similar morphology and Fe content but different Fe–N coordination numbers, and thus can be used as ideal models to study the effects of Fe–N coordination number on ORR activity and PEMFC performance.

![](./images/812715971625091074_3.jpg)

Fig. 2 Fitting results of the FT-EXAFS data and active site models of (a) FeNC-300, (b) FeNC-500 and (c) FeNC-1000. Red, golden and black balls represent Fe, N, and C atoms, respectively.

### 2.2. ORR measurements in a half-cell
For electrochemical evaluation, we measured the linear sweep voltammetry (LSV) curves of FeNC-300/500/1000 in oxygen saturated 0.5 M H₂SO₄ solution and 0.1 M KOH solution using a rotating ring-disk electrode (RRDE). In acidic electrolyte (Fig. 3a), the onset potential $E_{\text{onset}}$ (defined as the potential with a current density of $-0.1$ mA cm⁻²) of FeNC-300/500/1000 increases sequentially from 0.769 to 0.811 and to 0.894 V, respectively. The half-wave potential $(E_{1/2})$ increases from 0.581 to 0.662 and to 0.804 V, respectively. The carbonized ZIF-8 with and without adsorbed iron ions (Fe@NC or N/C) exhibit almost identical activities, which are much lower than those of FeNC-300/500. This indicates that there is no Fe–N bond between the N/C substrate and the adsorbed iron ions before the heat

![](./images/812715971625091074_4.jpg)

Fig. 3 Half-cell tests of catalysts. (a) LSV curves, (b) $H_2O_2$ yields and electron transfer numbers and (c) durability of the indicated catalysts in $O_2$ saturated $0.5\ M\ H_2SO_4$ determined by RRDE tests. (d) LSV curves of the indicated catalysts in $O_2$ saturated $0.1\ M$ KOH solution.

treatment. Furthermore, we also tested FeNC-1500 synthesized at a temperature of $1500\ ^{\circ}C$, and the result shows negligible activity compared to FeNC-1000 (Fig. S10$\dagger$). We speculate that the nitrogen was evaporated by such intensive annealing. $^{46,47}$ Although the heat treatment temperatures of 300 and $500\ ^{\circ}C$ are fairly low compared with the commonly used ones (800-1050) in the literature, the formation of $Fe-N_x$ bonds in FeNC-300/500 is responsible for the much higher ORR activities than that of Fe@NC. FeNC-1000 shows the highest selectivity for the $4\ e^-$ ORR compared to FeNC-300/500 in acidic electrolyte (Fig. 3b). We further tested the electrochemical stabilities of the three catalysts in acid at a constant voltage of $0.5\ V$ (vs. RHE). After 10k seconds, FeNC-1000 maintains 98.7% current, higher than the 91.1% for FeNC-500 and the 83.1% for FeNC-300 (Fig. 3c). After the stability test, the $E_{1/2}$ reduces by 10.5 mV for FeNC-1000, less than 25.5 mV for FeNC-500 and 38.6 mV for FeNC-300 (Fig. S11a$\dagger$). Clearly, the ORR stability follows the same order as the activity, i.e. FeNC-1000 > FeNC-500 > FeNC-300 in the acidic electrolyte. Similarly, the ORR activities of FeNC-300/500/1000 in 0.1 M KOH solution follow the same order as that in acid as shown in Fig. 3d. $E_{onset}$ and $E_{1/2}$ of FeNC-1000 are as high as 0.987 and 0.903 V respectively, even better than the 0.985 and 0.875 V for a commercial Pt/C (20%) catalyst. No matter whether an acidic or alkaline electrolyte is used, the ORR activities of FeNC-1000 are very close to those reported in the literature for $FeN_4$ dominated Fe-N-C catalysts (Table S5$\dagger$). Therefore, given the same catalyst morphology and similar Fe content, the distinctively different ORR performances among FeNC-300, -500, and -1000 should be associated with the different coordination numbers $x$ of the $FeN_x$ active sites.

In addition, the differences among FeNC-300, -500, and -1000 were also reflected by the poisoning experiments. FeNC-300, -500, and -1000 show 3.4%, 7.9% and 16.8% current losses upon adding KSCN into the electrolyte as shown in Fig. S11b.$\dagger$ To exclude the influence of annealing temperature on the activity of the nitrogen doped carbon support (NC), we heated the NC at 300, 500 and $1000\ ^{\circ}C$. NC-300, -500, and -1000 show almost identical and weak ORR activities (Fig. S12a$\dagger$), which means that the interference of the catalyst support in the ORR activities can be neglected. Moreover, Fe-C-300, -500, and -1000 that are prepared by annealing $Fe^{3+}$ adsorbed carbon black at 300, 500 and $1000\ ^{\circ}C$, respectively, in an Ar atmosphere for 2 hours, are completely inactive to the ORR as shown in Fig. S12b.$\dagger$ These results indicate that the formation of Fe-N bonds in FeNC-300/500/1000 is the source of ORR activity. Finally, we examined the effect of the heating duration on the resultant Fe-N coordination number by extending the pyrolysis time from 2 to 5 h. The corresponding ORR activities and the XANES spectra of the catalysts do not show significant changes (Fig. S13$\dagger$). Therefore, the temperature rather than the heating duration is effective for tailoring the coordination number of $FeN_x$.

### 2.3. Theoretical calculations of active sites

In previous studies, only the $FeN_4$ site has been extensively studied; other $FeN_x$ active sites and their relationship with the ORR activity have rarely been investigated. To gain a deep insight into the ORR activity of $FeN_x$, we performed DFT calculations to make a systematic comparison among the nitrogen coordinated iron species. Eight $FeN_x$ ($x=1$-$6$) models were selected to study the thermodynamic stabilities of the active sites first as shown in Fig. S14.$\dagger$ Among all $FeN_x$ ($x=1$-$6$), $FeN_4$ shows the lowest formation energy of $-5.10$ eV, much lower than the $-1.24$ eV of $FeN_1$ and the $-0.95$ eV of $FeN_6$. $FeN_2$ has three possible configurations, among which $FeN_{2-02}$ is selected to represent $FeN_2$ in the following discussion due to its lower formation energy compared with that of $FeN_{2-01}$ and $FeN_{2-03}$ (Table S6$\dagger$). Fig. 4a plots the formation energy of $FeN_x$ ($x=1$-$6$) as a function of the Fe-N coordination number $x$, which presents an "inverted

![](./images/812715971625091074_5.jpg)

Fig. 4 (a) Formation energies of $FeN_x$ ($x=1$-$6$) and ORR overpotentials of $FeN_x$ ($x=1$-$5$) determined by DFT calculations. (b) The partial density of states of Fe 3d and O 2p for $OH^*$ adsorbed $FeN_x$ ($x=1$-$5$). ORR free energy curves of $FeN_x$ ($x=1$-$5$) at (c) 0 V and (d) 1.23 V in an acidic environment.

volcano" relationship. In general, a higher heat treatment temperature will cause the material to form a more stable structure with a lower formation energy. Therefore, the highest heating temperature of 1000 °C in our experiment should be favorable for the formation of the most stable coordination structure, i.e. FeN₄, while the medium temperature of 500 °C and the relatively low temperature of 300 °C tend to produce FeNₓ with other coordination numbers of FeN₃ and FeN₁. The results are in agreement with the above structural characterization. Based on the calculation results, it is also possible to fabricate catalysts with dominant FeN₅ or FeN₂ active sites. However, it is hard to determine the exact synthesis conditions for these two sites at present.

The calculation of the ORR activity on different FeNₓ (x = 1-5) structures is based on the method developed by Nørskov and his co-workers,⁴⁸ which has been widely used to predict the activity of many catalysts.¹⁷,²⁴,²⁷,⁴⁹ The optimized adsorption configurations of ORR intermediates O*, OH* and OOH* on FeNₓ (x = 1-5) are shown in Fig. S15.† O atoms on FeN₁-FeN₃ preferentially occupy the Fe-C bridge site, while on FeN₄ and FeN₅, O atoms prefer to occupy the top sites of Fe atoms. OH* and OOH* tend to be adsorbed on the top site of Fe atoms in all of the five FeNₓ (x = 1-5) forming an Fe-O bond. The corresponding adsorption free energies of the adsorbates are given in Table S7.† Given that the adsorption of OH* affects the ORR electrocatalysis, the partial density of states (pDOS) of the Fe 3d and O 2p orbitals is examined based on the OH adsorbed FeNₓ (x = 1-5). The hybridization between Fe 3d and O 2p is shown in Fig. 4b. FeN₁, FeN₂ and FeN₃ have a high hybrid strength, indicating the formation of a strong Fe-O chemical bond, while the weak hybridization of O 2p with the Fe 3d of FeN₅ indicates a weak Fe-O chemical bond. The moderate hybridization strength of O 2p and Fe 3d of FeN₄ leads to a medium-strength Fe-O bond with $\Delta G_{\text{OH}*}$ of 0.77 eV, which is close to the value of 0.8 eV on the Pt (111) surface.⁴⁹ The appropriate adsorption of OH on FeN₄ benefits the ORR by avoiding the deactivation of active sites due to the insufficient or permanent adsorption of OH oxidation on the metal center.¹⁶,⁴⁹ The easy desorption of H₂O (the final product of the ORR) from the active sites is a necessary condition for the catalytic activity. We also calculated the adsorption energies of water molecules on FeNₓ (x = 1-5) as shown in Table S8.† The H₂O molecules have lower adsorption energies on all FeNₓ (x = 1-5) sites, indicating that H₂O molecules can be easily desorbed from FeNₓ sites.

To further clarify the ORR process on FeNₓ (x = 1-5), we calculated the four basic steps of the ORR shown in the Experimental section. The corresponding free energy changes for each intermediate reaction step relative to the initial state at 0 and 1.23 V are summarized in Fig. 4c and d respectively and Table S9.† It is found that the ORR free energy of each reaction step goes downhill for all FeNₓ (x = 1-5), indicating that the four ORR steps are all exothermic reactions at the five active sites. The rate limiting step for the ORR on FeN₂ and FeN₃ is the desorption of OH* to form H₂O (OH* + H⁺ + e⁻ → H₂O(l) + *).¹⁷,⁴⁹ The similarity of the adsorption free energies of OH* on FeN₂ (0.44 eV) and FeN₃ (0.48 eV) leads to similar ORR overpotentials of 0.79 and 0.75 V. The rate limiting step of the ORR on FeN₁ and FeNₓ is the formation of OH* (O* + H⁺ + e⁻ → OH*) and the corresponding $\Delta G$ is -0.19 and -0.72 eV, respectively. The large $\Delta G$ on FeN₁ hinders the formation of OH*. The weak adsorption free energy of OOH* on FeN₅ produces the largest $\Delta G$ of -0.06 eV, which restricts the formation of OOH* (O₂(g) + * + (H⁺ + e⁻) → OOH*), thus hindering the ORR. Clearly, FeN₄ has the smallest ORR free energy for the limiting step. Overpotential is an indicator of the catalyst activity.⁴⁸,⁵⁰ The ORR overpotential decreases with the increase of the nitrogen coordination number from 1 to 4, and then it begins to increase when the coordination number further increases to 5. Overall, the ORR activity of FeNₓ (x = 1-5) presents a "volcano" relationship as a function of the coordination number x (Fig. 4a). Thus, the order of ORR activity is theoretically determined to be FeN₄ > FeN₃ > FeN₂ > FeN₁ > FeN₅. The order of ORR activity calculated using DFT is consistent with the RDE test results of FeNC-300, -500, and -1000 catalysts.

### 2.4. PEMFC performance comparison of FeNC-1000, -500, and -300
FeNC-1000, -500, and -300 were further assembled into 5 cm² membrane electrode assemblies (MEAs) to examine the PEMFC performance of FeN₄, FeN₃ and FeN₁ active sites. The catalyst loading was optimized to 2 mg cm⁻² (Fig. S16†). As revealed by the polarization curves in Fig. 5a, FeNC-1000 shows a current density of 300 mA cm⁻² at 0.8 V (or 380 mA cm⁻² at 0.8 $V_{\text{IR-free}}$ in Fig. S17a†), while FeNC-500 and -300 hardly have obvious currents at this high voltage. At 0.7 V, FeNC-500 and -300 deliver current densities of 420 and 59.8 mA cm⁻², respectively, much lower than the 839 mA cm⁻² of FeNC-1000. The power density curves in Fig. 5b show a peak power density ($P_{\text{max}}$) of 1.01 W

![](./images/812715971625091074_6.jpg)

Fig. 5 PEMFC performances of FeNC-1000/500/300 and reference materials N/C and Pt/C (20%) as cathode catalysts: (a) polarization curves and (b) power density curves. (c) SEM image of irregularly shaped N/C particles from the solid-phase reaction derived ZIF-8. (d) PEMFC polarization curves and power density curves of FeNC-300_irreg, FeNC-500_irreg and FeNC-1000_irreg (fuel cell operation conditions: 80 °C, 100% humidified H₂ and O₂ with flow rates of 200 and 240 mL min⁻¹, respectively. The gauge pressures of H₂ and O₂ are 22 psig).

$cm^{-2}$ (at 0.55 V) for FeNC-1000, while the $P_{max}$ of FeNC-500 and FeNC-300 are only 604 and 352 mW $cm^{-2}$, respectively. Thus, FeNC-1000 ($FeN_4$) delivered $1.7\times$ and $2.9\times$ peak power densities, and $2\times$ and $14\times$ current densities (at 0.7 V) compared with FeNC-500 ($FeN_3$) and FeNC-300 ($FeN_1$), respectively. When the power density is converted to the loading of Fe single-atoms, the mass specific $P_{max}$ is 230, 121 and 88 W $mg_{Fe}^{-2}$ for FeNC-1000, FeNC-500 and FeNC-300, respectively. The ultra-high specific power densities show the high catalytic efficiency of Fe single-atoms. The order of PEMFC performance is FeNC-1000 > FeNC-500 > FeNC-300, which is the same as the ORR activity results obtained using the half-cell.

The effect of annealing temperature and PEMFC performance order are further confirmed by another group of Fe-N-C catalysts (named as FeNC-1000_irreg), which were synthesized with a solid-phase reaction derived ZIF-8 precursor that has large particle sizes of 0.1–5 μm and irregular particle shapes as shown in Fig. 5c and d. The PEMFC current densities (at 0.7 V) are 740, 200 and 80 mA $cm^{-2}$ for FeNC-1000_irreg, FeN-500_irreg and FeN-300_irreg, respectively. Their peak power densities are 903, 505 and 381 mW $cm^{-2}$, respectively. We can see that the order of PEMFC performance of FeNC-1000/500/300_irreg is the same as that of the dodecahedral Fe-N-C NPs. Due to the large particle size and the relatively low external surface area, FeNC-1000/500/300_irreg have fewer active sites to participate in the ORR. Thus, their PEMFC performances are relatively lower than those of FeNC-1000/500/300.

## 3. Conclusions

In this paper, the effects of nitrogen coordination number $x$ of $FeN_x$ active sites on the ORR activity and PEMFC performance of Fe-N-C catalysts are investigated by a combination of experimental and theoretical approaches. By adjusting the heating temperature (300, 500, and 1000 °C), FeNC-300, FeNC-500 and FeNC-1000 catalysts are prepared with different active sites of $FeN_1$, $FeN_3$ and $FeN_4$, respectively. The order of PEMFC performance is measured to be FeN-1000 ($FeN_4$) > FeN-500 ($FeN_3$) > FeN-300 ($FeN_1$), consistent with their ORR activity order. The synthesized FeNC-1000 exhibits a high PEMFC activity of 380 mA $cm^{-2}$ at 0.8 $V_{IR-free}$ and a high peak power density of 1.01 W $cm^{-2}$. DFT calculations demonstrate an "inverted volcano" relationship and a "volcano" relationship respectively for the ORR activity and formation energy of $FeN_x$ species as a function of Fe-N coordination number $x$. The order of ORR activity is calculated to be $FeN_4 > FeN_3 > FeN_2 > FeN_1 > FeN_5$. $FeN_4$ has the most stable configuration and the highest ORR activity among all $FeN_x$ ($x=1$–5). This work deepens our understanding of the significant effect of the $FeN_x$ coordination number $x$ on the ORR activity and PEMFC performance of Fe-N-C catalysts.

## Conflicts of interest

There are no conflicts of interest to declare.

## Acknowledgements

This work was supported by the National Natural Science Foundation of China (21673014 and 21975010), the Fundamental Research Funds for the Central Universities of China, and the "111" Project (B17002) funded by the Ministry of Education of China.

## References

1 M. Shao, Q. Chang, J. P. Dodelet and R. Chenitz, *Chem. Rev.*, 2016, **116**, 3594-3657.

2 Y. Wang, J. Li and Z. Wei, *J. Mater. Chem. A*, 2018, **6**, 8194-8209.

3 Y. Zheng, Y. Jiao, Y. Zhu, Q. Cai, A. Vasileff, L. H. Li, Y. Han, Y. Chen and S. Z. Qiao, *J. Am. Chem. Soc.*, 2017, **139**, 3336-3339.

4 L. Zhao, Y. Zhang, L. B. Huang, X. Z. Liu, Q. H. Zhang, C. He, Z. Y. Wu, L. J. Zhang, J. Wu, W. Yang, L. Gu, J. S. Hu and L. J. Wan, *Nat. Commun.*, 2019, **10**, 1278.

5 F. Yang, P. Song, X. Liu, B. Mei, W. Xing, Z. Jiang, L. Gu and W. Xu, *Angew. Chem., Int. Ed.*, 2018, **57**, 12303-12307.

6 J. Zhao and Z. Chen, *J. Am. Chem. Soc.*, 2017, **139**, 12480-12487.

7 Y. Shao, J. P. Dodelet, G. Wu and P. Zelenay, *Adv. Mater.*, 2019, 1807615.

8 X.-D. Yang, Y. Zheng, J. Yang, W. Shi, J.-H. Zhong, C. Zhang, X. Zhang, Y.-H. Hong, X.-X. Peng, Z.-Y. Zhou and S.-G. Sun, *ACS Catal.*, 2016, **7**, 139-145.

9 L. Yang, D. Cheng, H. Xu, X. Zeng, X. Wan, J. Shui, Z. Xiang and D. Cao, *Proc. Natl. Acad. Sci.*, 2018, **115**, 6626-6631.

10 S. Ratso, N. Ranjbar Sahraie, M. T. Sougrati, M. Käärik, M. Kook, R. Saar, P. Paiste, Q. Jia, J. Leis, S. Mukerjee, F. Jaouen and K. Tammeveski, *J. Mater. Chem. A*, 2018, **6**, 14663-14674.

11 H. Fei, J. Dong, Y. Feng, C. S. Allen, C. Wan, B. Volosskiy, M. Li, Z. Zhao, Y. Wang, H. Sun, P. An, W. Chen, Z. Guo, C. Lee, D. Chen, I. Shakir, M. Liu, T. Hu, Y. Li, A. I. Kirkland, X. Duan and Y. Huang, *Nat. Catal.*, 2018, **1**, 63-72.

12 X. Wang, Z. Chen, X. Zhao, T. Yao, W. Chen, R. You, C. Zhao, G. Wu, J. Wang, W. Huang, J. Yang, X. Hong, S. Wei, Y. Wu and Y. Li, *Angew. Chem., Int. Ed.*, 2018, **57**, 1944-1948.

13 X. Li, W. Bi, M. Chen, Y. Sun, H. Ju, W. Yan, J. Zhu, X. Wu, W. Chu, C. Wu and Y. Xie, *J. Am. Chem. Soc.*, 2017, **139**, 14889-14892.

14 C. Zhao, X. Dai, T. Yao, W. Chen, X. Wang, J. Wang, J. Yang, S. Wei, Y. Wu and Y. Li, *J. Am. Chem. Soc.*, 2017, **139**, 8078-8081.

15 W. Liu, L. Zhang, X. Liu, X. Liu, X. Yang, S. Miao, W. Wang, A. Wang and T. Zhang, *J. Am. Chem. Soc.*, 2017, **139**, 10790-10798.

16 Q. Lai, L. Zheng, Y. Liang, J. He, J. Zhao and J. Chen, *ACS Catal.*, 2017, **7**, 1655-1663.

17 X. Zhang, Z. Yang, Z. Lu and W. Wang, *Carbon*, 2018, **130**, 112-119.

18 X. Zhang, Z. Yang, X. Yang, Y. Wang and Z. Lu, *Int. J. Hydrogen Energy*, 2018, **43**, 20573-20579.

19 J. Shui, C. Chen, L. Grabstanowicz, D. Zhao and D. J. Liu, *Proc. Natl. Acad. Sci.*, 2015, **112**, 10629-10634.

20 Y. J. Sa, D. J. Seo, J. Woo, J. T. Lim, J. Y. Cheon, S. Y. Yang, J. M. Lee, D. Kang, T. J. Shin, H. S. Shin, H. Y. Jeong, C. S. Kim, M. G. Kim, T. Y. Kim and S. H. Joo, *J. Am. Chem. Soc.*, 2016, **138**, 15046-15056.

21 U. Martinez, S. Komini Babu, E. F. Holby, H. T. Chung, X. Yin and P. Zelenay, *Adv. Mater.*, 2019, 1806545.

22 X. Wan, X. Liu, Y. Li, R. Yu, L. Zheng, W. Yan, H. Wang, M. Xu and J. Shui, *Nat. Catal.*, 2019, **2**, 259-268.

23 Y. Chen, S. Ji, Y. Wang, J. Dong, W. Chen, Z. Li, R. Shen, L. Zheng, Z. Zhuang, D. Wang and Y. Li, *Angew. Chem., Int. Ed.*, 2017, **56**, 6937-6941.

24 Z. Miao, X. Wang, M.-C. Tsai, Q. Jin, J. Liang, F. Ma, T. Wang, S. Zheng, B.-J. Hwang, Y. Huang, S. Guo and Q. Li, *Adv. Energy Mater.*, 2018, **8**, 1801226.

25 M. Lefèvre, E. Proietti, F. Jaouen and J.-P. Dodelet, *Science*, 2009, **324**, 71-74.

26 Y. Deng, B. Chi, X. Tian, Z. Cui, E. Liu, Q. Jia, W. Fan, G. Wang, D. Dang, M. Li, K. Zang, J. Luo, Y. Hu, S. Liao, X. Sun and S. Mukerjee, *J. Mater. Chem. A*, 2019, **7**, 5020-5030.

27 X. Fu, N. Li, B. Ren, G. Jiang, Y. Liu, F. M. Hassan, D. Su, J. Zhu, L. Yang, Z. Bai, Z. P. Cano, A. Yu and Z. Chen, *Adv. Energy Mater.*, 2019, **9**, 1803737.

28 Y. Cheng, S. He, S. Lu, J.-P. Veder, B. Johannessen, L. Thomsen, M. Saunders, T. Becker, R. De Marco, Q. Li, S.-z. Yang and S. P. Jiang, *Adv. Sci.*, 2019, 1802066.

29 J. Huang, Q. Lu, X. Ma and X. Yang, *J. Mater. Chem. A*, 2018, **6**, 18488-18497.

30 P. J. Wei, G. Q. Yu, Y. Naruta and J. G. Liu, *Angew. Chem., Int. Ed.*, 2014, **53**, 6659-6663.

31 Y. Lin, P. Liu, E. Velasco, G. Yao, Z. Tian, L. Zhang and L. Chen, *Adv. Mater.*, 2019, **31**, 1808193.

32 S. Kabir, K. Artyushkova, B. Kiefer and P. Atanassov, *Phys. Chem. Chem. Phys.*, 2015, **17**, 17785-17789.

33 D. Zhang, W. Chen, Z. Li, Y. Chen, L. Zheng, Y. Gong, Q. Li, R. Shen, Y. Han, W. C. Cheong, L. Gu and Y. Li, *Chem. Commun.*, 2018, **54**, 4274-4277.

34 V. Armel, S. Hindocha, F. Salles, S. Bennett, D. Jones and F. Jaouen, *J. Am. Chem. Soc.*, 2017, **139**, 453-464.

35 Y. Deng, B. Chi, J. Li, G. Wang, L. Zheng, X. Shi, Z. Cui, L. Du, S. Liao, K. Zang, J. Luo, Y. Hu and X. Sun, *Adv. Energy Mater.*, 2019, **9**, 1802856.

36 Q. Liu, X. Liu, L. Zheng and J. Shui, *Angew. Chem., Int. Ed.*, 2018, **57**, 1204-1208.

37 U. I. Kramm, M. Lefevre, N. Larouche, D. Schmeisser and J. P. Dodelet, *J. Am. Chem. Soc.*, 2014, **136**, 978-985.

38 R. Chenitz, U. I. Kramm, M. Lefèvre, V. Glibin, G. Zhang, S. Sun and J.-P. Dodelet, *Energy Environ. Sci.*, 2018, **11**, 365-382.

39 C.-Y. Su, H. Cheng, W. Li, Z.-Q. Liu, N. Li, Z. Hou, F.-Q. Bai, H.-X. Zhang and T.-Y. Ma, *Adv. Energy Mater.*, 2017, **7**, 1602420.

40 W. Fan, Z. Li, C. You, X. Zong, X. Tian, S. Miao, T. Shu, C. Li and S. Liao, *Nano Energy*, 2017, **37**, 187-194.

41 L. T. Weng, P. Bertrand, G. Lalande, D. Guay and J. P. Dodelet, *Appl. Surf. Sci.*, 1994, **84**, 9-21.

42 M. Ladouceur, G. Lalande, D. Guay and J. P. Dodelet, *J. Electrochem. Soc.*, 1993, **140**, 1974-1981.

43 M. C. Martins Alves, J. P. Dodelet, D. Guay, M. Ladouceur and G. Tourillon, *J. Phys. Chem.*, 1992, **96**, 10898-10905.

44 G. Lalande, G. Faubert, R. Cote, D. Guay, J. P. Dodelet, L. T. Weng and P. Bertrand, *J. Power Sources*, 1996, **61**, 227-237.

45 X. Wang, Z. Chen, X. Zhao, T. Yao, W. Chen, R. You, C. Zhao, G. Wu, J. Wang, W. Huang, J. Yang, X. Hong, S. Wei, Y. Wu and Y. Li, *Angew. Chem., Int. Ed.*, 2018, **57**, 1944-1948.

46 C. Young, R. R. Salunkhe, J. Tang, C. C. Hu, M. Shahabuddin, E. Yanmaz, M. S. Hossain, J. H. Kim and Y. Yamauchi, *Phys. Chem. Chem. Phys.*, 2016, **18**, 29308-29315.

47 S. Gadipelli and Z. X. Guo, *ChemSusChem*, 2015, **8**, 2123-2132.

48 J. K. Nørskov, J. Rossmeisl, A. Logadottir, L. Lindqvist, J. R. Kitchin, T. Bligaard and H. Jónsson, *J. Phys. Chem. B*, 2004, **108**, 17886-17892.

49 H. Xu, D. Cheng, D. Cao and X. C. Zeng, *Nat. Catal.*, 2018, **1**, 339-348.

50 Z. Liu, Z. Zhao, Y. Wang, S. Dou, D. Yan, D. Liu, Z. Xia and S. Wang, *Adv. Mater.*, 2017, **29**, 1606207.