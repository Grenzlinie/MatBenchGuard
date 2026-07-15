# Thermal boundary conductance across epitaxial metal/sapphire interfaces

Yee Rui Koh, $^{1,{*}}$ Jingjing Shi, $^{2,{*}}$ Baiwei Wang, $^{3}$ Renjiu Hu, $^{4}$ Habib Ahmad, $^{5}$ Sit Kerdsongpanya, $^{3}$ Erik Milosevic, $^{3}$ W. Alan Doolittle, $^{5}$ Daniel Gall, $^{3}$ Zhiting Tian, $^{1}$ Samuel Graham, $^{2,6,\dagger}$ and Patrick E. Hopkins $^{1,7,8,\ddagger}$

$^{1}$Department of Mechanical and Aerospace Engineering, University of Virginia, Charlottesville, Virginia 22904, USA
$^{2}$George W. Woodruff School of Mechanical Engineering, Georgia Institute of Technology, Atlanta, Georgia 30332, USA
$^{3}$Department of Materials Science and Engineering, Rensselaer Polytechnic Institute, Troy, New York 12180, USA
$^{4}$Sibley School of Mechanical and Aerospace Engineering, Cornell University, Ithaca, New York 14853, USA
$^{5}$School of Electrical and Computer Engineering, Georgia Institute of Technology, Atlanta, Georgia 30332, USA
$^{6}$School of Materials Science and Engineering, Georgia Institute of Technology, Atlanta, Georgia 30332, USA
$^{7}$Department of Materials Science and Engineering, University of Virginia, Charlottesville, Virginia 22904, USA
$^{8}$Department of Physics, University of Virginia, Charlottesville, Virginia 22904, USA

![](./images/812539671354540033_1.jpg)
(Received 19 July 2020; revised 30 September 2020; accepted 1 October 2020; published 23 November 2020)

As electronic devices shrink down to their ultimate limit, the fundamental understanding of interfacial thermal transport becomes essential in thermal management. However, a comprehensive understanding of phonon transport mechanisms that drive interfacial thermal transport is still under development. The thermal transport across interfaces can be strongly affected by factors such as crystalline structure, surface roughness, chemical diffusion, etc. These complications lead to a significant quantitative uncertainty between experimentally measured thermal boundary conductance (TBC) across real material interfaces and theoretically calculated TBCs that are often predicted on structurally and/or chemically ideal interfaces. In this paper, we report on the thermal conductance across interfaces between various epitaxially grown metal films (Co, Ru, and Al) and c-plane sapphire substrates via time-domain thermoreflectance over the temperature range of $\sim$80 to $\sim$500 K. The room-temperature interface conductances of Al/sapphire, Co/sapphire, and Ru/sapphire are all $\sim 350\ \text{MW}\ \text{m}^{-1}\ \text{K}^{-1}$ despite the phonon spectra differences among the metals. We compare our results to predictions of TBC using atomistic Green's function calculations and the modal nonequilibrium Landauer method with transmission from the diffuse mismatch model. We found a consistent quantitative agreement between the experimentally measured TBCs and the predictions using the modal nonequilibrium Landauer model for the $\text{Al}/\text{Al}_{2}\text{O}_{3}$, $\text{Co}/\text{Al}_{2}\text{O}_{3}$, and $\text{Ru}/\text{Al}_{2}\text{O}_{3}$ interfaces. This result suggests that interfacial elastic phonon thermal transport dominates TBC for the various epitaxial metal/sapphire combinations of interest in this work, while other mechanisms are negligible.

DOI: 10.1103/PhysRevB.102.205304

The miniaturization of devices that is driving the decrease of material length scales to nanometers, and the corresponding increases in solid/solid interface densities, have enabled remarkable functionalities and increases in performance metrics of various technologies. However, this increased interface density can also lead to detrimental temperature rises and overheating, since these solid/solid interfaces give rise to thermal resistances from interfaces that can impede heat flow [1,2]. Thus, engineering and designing the thermal boundary conductance (TBC) across interfaces (the inverse of which is the thermal boundary resistance) is paramount to the enhanced functionalities of a wide range of materials and devices [3–5], and thus rooted in our ability to understand the fundamental phonon interactions that underpin this interfacial thermal transport.

Several relatively recent experimental techniques have afforded the ability to measure TBC across solid/solid interfaces at noncryogenic, device-relevant temperatures, particularly optical pump-probe techniques such as time-domain thermoreflectance (TDTR) [6–8] and frequency-domain thermoreflectance (FDTR) [9,10]. These techniques can effectively probe the thermal conductivity [11–15] and the TBC [16–20] in material systems that are as thin as a few nanometers. When these measurements are coupled with theory-based predictive models and simulations—such as the acoustic mismatch model (AMM) [21], the diffuse mismatch model (DMM) [22], or atomistic Green's function (AGF) [23] simulations—we can begin to advance our fundamental understanding of how phonons are exchanging energy at heterogeneous material interfaces and thus contributing to the measured TBC. However, it is not uncommon for these predictive results to fail to agree with the experimentally measured TBCs due to various fundamental assumptions that underpin each respective modeling technique [24,25]. This greatly obfuscates the ability to extract a fundamental phonon understanding from TBC measurements and suggests the need for new formalisms for TBC prediction, such as the interfacial conductance modal analysis (ICMA) [24] and the modal nonequilibrium Landauer method [26], which can be paired

---

$^{*}$These authors contributed equally to this work.
$^{\dagger}$sgraham@gatech.edu
$^{\ddagger}$phopkins@virginia.edu

![](./images/812539671354540033_2.jpg)

FIG. 1. Experimentally measured TBC vs. ratio of the elastic moduli of the two constituent materials based on Refs. [3,33]. The open symbols are based on the literature values, and the filled symbols are measured values in this paper.

with TBC measurements of well-controlled and characterized interfaces. Thus, paramount to comparing measured TBC data to any of these aforementioned modeling or simulation approaches are judiciously fabricated interfaces prepared in such a way as to most accurately reflect the simulated domain. Since phonon transport across interfaces relies on a wide spectrum of phonon wavelengths [27,28], the materials that are experimentally studied should be fabricated with as much control as possible of the atomic arrangements near the interface and continuum mechanical properties of the materials so as to match the simulated domains.

Epitaxially grown systems are often necessary to achieve this aforementioned level of control of materials at interfaces [16,18,25,29-32]. For example, Cheng et al. [18] found near-perfect agreement between TDTR measurements of TBC on epitaxially grown Al films on sapphire $(Al_{2}O_{3})$ substrates when compared to two different predictive formalisms: AGF simulations and a modal nonequilibrium Landauer method with transmission from DMM. This agreement between these elastic, phonon-based simulations and the measured TBC across the $Al/Al_{2}O_{3}$ interfaces implied that other possible electron or phonon processes are not contributing to TBC (for example, electron-phonon coupling at or near the interface or inelastic phonon-phonon coupling across the interface).

The goal of this work is to evaluate the accuracies of these two different modeling approaches (AGF and the modal nonequilibrium Landauer method) on predicting the TBC at metal/nonmetal interfaces. In addition to further studies of the epitaxially grown Al/sapphire interfaces discussed in Ref. [18], we also study epitaxial interfaces of Co/sapphire and Ru/sapphire. We measured the TiN/MgO sample as a calibration sample to compare to measured TBC in [16]. This comparison is essential to verify the samples' qualities, our measurement precision, and the rigorous uncertainty in our TDTR measurements.

A survey of the TBCs as a function of the ratio of the elastic moduli of the two constituent materials comprising their respective interfaces is shown in Fig. 1. The experimentally measured TBCs in this work demonstrate that the relative mismatch of the phonon spectra of materials at interfaces (e.g., Debye temperatures) is not a good indicator of the TBCs. We included the thermomechanical and acoustic parameters of the materials in Table I. The AGF and simulations based on the modal nonequilibrium Landauer method support these findings and quantify the importance of considering the spectral structure in a material's phonon density of states (DOS) on the TBC across interfaces. This study further serves to validate and compare these simulation approaches along with demonstrating the importance of the details of the calculated phonon density of states in predictions of solid/solid TBC.

We employed the TDTR to measure TBC across the epitaxially grown metal/sapphire interfaces. The details of the thermal measurements and sample preparation are described in the Supplemental Material [65] and other references [6-8,43-54]. Figure 2 shows the measured TBC of the epitaxially grown Al/sapphire, Co/sapphire, Ru/sapphire, and TiN/MgO samples as a function of temperature. For comparison, we include previously measured TBC measurements on various other metal/nonmetal interfaces with high TBCs, including TiN/MgO and TiN/sapphire from Costescu et al. [16] and $CoSi_{2}/Si$ from Ye et al. [29]. Costescu et al.'s [16] results on TiN/MgO [in (001) and (111) orientation] and TiN/sapphire (0001) are the earliest reports of TDTR measurements of TBC across epitaxial metal/nonmetal interfaces, and they remain one of the highest experimentally measured TBCs across metal/nonmetal interfaces to date at ambient conditions (note, another work has reported higher TBCs across the interface of the conducting oxide $SrRuO_{3}$ and $SrTiO_{3}$ at room temperature [32]). Our measured TiN/MgO interface conductance is in agreement with that reported by Costescu et al. [16]. Further, our measured Al/sapphire (0001) TBC measurements show similar agreement with prior reports, including our previous measurements across similar Al/sapphire (0001) interfaces, which we compare in detail in our prior work [18]. The agreement between our measurement and the previous literature results of the TBC at the TiN/MgO and Al/sapphire interfaces indicates the accuracy of our measurements with our TDTR

TABLE I. List of material properties of Co, Al, Ru, and sapphire.

<table>
<thead>
  <tr>
    <th></th>
    <th>Sapphire</th>
    <th>Co</th>
    <th>Al</th>
    <th>Ru</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Density (g cm⁻³)</td>
    <td>3.97</td>
    <td>8.90 [34]</td>
    <td>2.70 [34]</td>
    <td>12.45 [34]</td>
  </tr>
  <tr>
    <td>Young’s modulus (GPa)</td>
    <td>400 [35]</td>
    <td>211 [36]</td>
    <td>70 [37]</td>
    <td>292.3 [38]</td>
  </tr>
  <tr>
    <td>LA velocity (m s⁻¹)</td>
    <td>10 400–11 100 [39]</td>
    <td>6889</td>
    <td>6420 [34]</td>
    <td>6530 [40]</td>
  </tr>
  <tr>
    <td>TA velocity (m s⁻¹)</td>
    <td>5700–6700 [39]</td>
    <td>2880</td>
    <td>3040 [34]</td>
    <td>3740 [40]</td>
  </tr>
  <tr>
    <td>Debye temperature (K)</td>
    <td>1010 [41]</td>
    <td>460 [42]</td>
    <td>433 [42]</td>
    <td>555 [42]</td>
  </tr>
</tbody>
</table>

![](./images/812539671354540033_3.jpg)

FIG. 2. Measured thermal boundary conductance across Co/sapphire (♦), Al/sapphire (■), Ru/sapphire (◀), and TiN/MgO (●) interfaces as a function of temperature, shown as the filled symbols. For comparison, TBC across epitaxial interface of TiN/MgO(001) (○), TiN/MgO(111) (◎), and TiN/Al₂O₃ (0001) (□) [16], Al/Al₂O₃ (0001) (□) [18], and CoSi₂/Si (∇) [29] are also plotted. Measurements from this current work are filled symbols, while literature TBC values are open symbols.

system. The uncertainty reported in these measurements is based on assumptions in the thermal model used for determin- ing TBC, repeatability among multiple measurements, and the mean-square deviation of our thermal model fits to TDTR data based on a 95% confidence interval contour plot analysis, as detailed in the supplemental material [65].

When comparing the measured TBC across our Al/sapphire, Co/sapphire, and Ru/sapphire interfaces as shown in Fig. 3(a), we find that despite differences in Debye temperatures/phonon cutoff frequencies and zone-center (Γ point) acoustic phonon group velocities (Table I), we do not observe any discernable difference in measured TBC at temperatures below 300 K. We do observe differences in TBC among these samples at higher temperatures, >300 K; however, the trends in the measured TBC among these metal/sapphire interfaces do not follow the qualitative trends expected from considerations based on the differences in the aforementioned phonon acoustic and spectral properties of Al, Ru, and Co. The relation of Debye temperature $\theta_{\text{D}}$ for these three metals is $\theta_{\text{D,Al}} < \theta_{\text{D,Co}} < \theta_{\text{D,Ru}}$. Traditionally assumed scaling rules of thumb would thus imply that $\text{TBC}_{\text{Al}} < \text{TBC}_{\text{Co}} < \text{TBC}_{\text{Ru}}$ considering the much higher Debye temperature (1010 K) [41] of sapphire, yet our high-temperature measurements show that Co/sapphire TBC is the highest, while the difference between Al/sapphire TBC and Ru/sapphire TBC are within uncertainty. These experimental results suggest the importance of considering additional phonon modal properties beyond those predicted from only acoustic phonon dispersion relations near the $\Gamma$ point of the first Brillouin zone, such as Young's modulus, speed of sounds, and Debye temperatures. We note that this is consistent with our prior theoretical and computational works highlighting the importance of phonon dispersion on TBC and the inability of the spectral mismatch in the phonon densities of states alone to accurately capture trends in TBC [55,56]. While prior attempts have been made to understand the impact of specific details in the phonon DOS on experimentally measured metal/nonmetal TBCs [27,57-59], without a direct comparison of measured values across epitaxially grown interfaces to rigorous simulations that properly account for contribution in the first Brillouin zone with full-band phonon dispersion of all polarizations, a sufficient level of understanding and conclusion is not possible. In the remainder of this work, we address this by directly comparing our experimental results of the TBCs across the epitaxially formed Al/sapphire, Co/sapphire, and Ru/sapphire interfaces with AGF and the modal nonequilibrium Landauer method simulations using full-band phonon properties of all the branches generated from density functional theory (DFT) under different approximations to the exchange-correlation (XC) energy functional. We used the local density approximation for the Landauer method and the generalized gradient approximation for AGF, respectively.

A comparison between modal nonequilibrium Landauer method-predicted TBC and the TDTR experimental measured TBC values is shown in Fig. 3(a). The modal nonequilibrium Landauer method is reported in Ref. [26], which had shown promising results in predicting accurate TBCs of Al/Si, ZnO/GaN, and Al/sapphire [18,26]. Based on the foundation of these references, we use the Landauer method to calculate the exact thermal transport detail of the sample interfaces. The modal nonequilibrium Landauer method is an improved original Landauer method, with a temperature correction to account for the local nonequilibrium effect of the phonon transport across the interfaces. The details of the modal nonequilibrium Landauer method are discussed in Ref. [26] and the Supplemental Material [65]. Unlike the conventional Landauer method, the modal nonequilibrium Landauer method considers the local nonequilibrium at the interface. Here we apply the diffuse mismatch model to calculate the spectral phonon transmission coefficient at the interface [16,60] This formalism only accounts for the elastic contri- bution of the phonon TBC, which is the dominant phonon transport mechanism at the highly lattice-matched interfaces of Al/sapphire (4% mismatch) [18], Co/sapphire (9.6% mismatch) [46], and Ru/sapphire (1.8% mismatch) [43]. Precise calculations of the dispersion relation are essential to predict the probability of transmission to either side of the interfaces. These results would lead to a detailed knowledge of the phonon dispersion relation over the entire Brillouin zone and a trustable predicted TBC [22]. DFT with the Vienna Ab-initio Simulation Package (VASP) framework [61,62] is employed to calculate the phonon properties of metals and

![](./images/812539671354540033_4.jpg)

FIG. 3. (a) A comparison between TDTR measured TBC (filled symbols) with predicted TBC via modal nonequilibrium Landauer (solid line) across Co/sapphire, Al/sapphire, and Ru/sapphire interfaces. (b) The calculated DOS of the metals and sapphire via DFT with a VASP framework for the modal nonequilibrium Landauer method. (c) Comparison of the calculated thermal conductivity vs. measured thermal conductivity [16,29]. The dashed line represents an identical match between calculated and experimental TBC values.

c-plane sapphire, as shown in Fig. 3(b). The different DOS trends of Co, Al, Ru, and c-plane sapphire illustrate the allowed channels in the TBC. The phonon frequencies of the sapphire are distributed over a wide range, 0–25 THz, and the cutoff frequency is around three times that of the metals' cutoff frequencies studied in our work. The cutoff phonon frequencies of the Co, Al, and Ru are $\sim$9.5, $\sim$10.5, and $\sim$8.5 THz, respectively. Since the modal nonequilibrium Landauer method only accounts for interfacial elastic phonon transport, the phonons of the sapphire above the metals' cutoff frequencies do not contribute to the TBC in our calculation.

Figure 3(a) shows the experimental and theoretical results for the metal/sapphire TBC as a function of the temperature. In general, for each metal/sapphire interface, the Landauer method captures the high-temperature (200–500 K) TBCs, but slightly overpredicts part of the low-temperature (80–200 K) TBCs. The discrepancy between modeling and experiments might come from the imperfection in real materials and at real interfaces, since the Landauer method is based on the perfect bulk material assumption. At low temperatures, thermal phonons are more impacted by the impurities, dislocations, and strain fields inside the material considering their relatively low intrinsic scattering rate from anharmonicity relative to elevated temperatures. As a result, the measured TBC at low temperature would be lower than that predicted from modeling with perfect bulk assumption. We also note a different temperature trend in the measured TBC at the Co/sapphire interface at high temperature as compared to the Landauer-based method, which we speculate could be indicative of inelastic scattering processes.

Comparing the three metal/sapphire interfaces with nonequilibrium Landauer modeling, the calculated Co/sapphire TBC shows the highest value, while the Ru/sapphire shows the lowest value, despite the fact that Ru has the highest Debye temperature (555 K) [42] compared to Al (433 K) [42] and Co (460 K) [42]. Our experimental measurements confirm that Co/sapphire has the highest TBC among these samples, but the measured Al/sapphire and Ru/sapphire TBCs have similar values. The experimental measurements clearly suggest that considering only acoustic phonon properties near the $\Gamma$ point is not sufficient to understand the TBC across interfaces. The contributions from all phonon modes must be considered, and as a result, the phonon information from the entire first Brillouin zone is needed to accurately capture the temperature-dependent trend in TBC.

Figure 3(c) illustrates the exceptional agreement between the TDTR-measured TBCs and the model nonequilibrium Landauer predicted TBCs at room temperature, in comparison to other modeled TBCs (AGF and DMM) versus the experimentally measured TBCs in Refs. [16,29]. The similarities of the measured and theoretical TBCs, in both magnitude

![](./images/812539671354540033_5.jpg)

FIG. 4. (a) A comparison of AGF simulations and the modal nonequilibrium Landauer method for Al/sapphire and Ru/sapphire TBCs. (b) The calculated DOS of the Al, Ru, and sapphire via DFT with a QUANTUM ESPRESSO framework.

and temperature trends, suggest similar heat transport mechanisms driving TBC. These results imply that TBCs of the Co/sapphire, Al/sapphire, and Ru/sapphire are dominated by the elastic phonon thermal transport.

We now turn our attention to evaluating the predictive power of AGF by comparing AGF simulations of TBC across these interfaces to our measured values. The AGF method is rooted in the Landauer formalism and accounts for the transmission of the wave-based nature phonons in the TBC. Unlike the Landauer formalism with transmission from mismatch models, and our implemented modal nonequilibrium Landauer method with DMM employed in this work, an AGF analysis can account for the atomic structure and interatomic potential at interfaces. Although AGF has demonstrated capabilities in predicting TBC of epitaxial interfaces with submonolayer roughness [25,29,63,64], it often requires large simulation domains and is computationally expensive relative to the modal nonequilibrium Landauer method. Given their similar assumptions of elastic-phonon scattering contributing to TBC, a comparison of TBC predictive capability between these two methods will allow for assessment of the role of interfacial structure and potentials on TBC across these covalently bonded, epitaxial interfaces.

Thus, we present a comparison of AGF calculations and modal nonequilibrium Landauer method calculations on the Al/sapphire TBC and Ru/sapphire TBCs in Fig. 4(a). We had restricted our attention by comparing two kinds of extreme cases for the rigorous comparison: (i) A similar pseudopotential of Al is used to calculate via DFT with the QUANTUM ESPRESSO framework, which produces an almost similar DOS of the Al in Fig. 3(b). (ii) An arbitrary pseudopotential of Ru is created and used in DFT with the QUANTUM ESPRESSO framework, to only capture phonons with lower frequency (<7 THz) in Ru. These calculated DOSs are presented in Fig. 4(b). Both predicted Al/sapphire and Ru/sapphire TBCs via AGF and the modal nonequilibrium Landauer method are almost identical ($\pm 10\%$ errors) assuming the same DOS. These results prove that the differences applied in both calculations—e.g., phonon transmission coefficient, $k$-mesh, and supercell size—play an insignificant role and only contribute to a slight discrepancy. The comparison between
Figs. 3(a) and 4(a) also reveals an important insight. We found that predicted Al/sapphire TBCs are almost equivalent in Figs. 3(a) and 4(a), but the predicted Ru/sapphire TBC in Fig. 4(a) is $\sim 50\%$ less than Fig. 3(a). Based on the observations above, we affirm that both methods can produce similar predicted TBCs under the same calculated DOS. However, the accuracy of predicted TBC compared to experimental TBC is strongly affected, if not solely, by the factually predicted DOS.

In summary, the thermal boundary conductance of a series of well-characterized epitaxially grown interfaces of Co, Al, and Ru films on sapphire (0001) was measured using TDTR. Despite differences in the phonon spectra, the room-temperature interface conductances of Co/sapphire, Al/sapphire, and Ru/sapphire are $350 \pm 60\ \text{MW}\ \text{m}^{-2}\ \text{K}^{-1}$, which is among the highest ever measured thermal boundary conductance for a metal/sapphire interfaces. The measured TBC as a function of the temperature is comparable with the predicted TBC via the modal nonequilibrium Landauer method. In general, a qualitative and quantitative agreement has been achieved between the measured TBC and the predicted values of the modal nonequilibrium Landauer method. These similarities imply that the Landauer method, which only accounts for the interfacial elastic-phonon transport in the calculation, can accurately predict TBC across metal/sapphire interfaces with different phonon spectra, e.g., Co/sapphire, Al/sapphire, and Ru/sapphire. We also presented a comparison of the AGF and Landauer methods, concluding that both methods are nearly identical when using the same input parameters and spectral phonon. This observation suggests that the less expensive modal nonequilibrium Landauer method is an ideal alternative for the theoretical TBC predic- tions [65].

We appreciate support from the Office of Naval Research under a MURI program, Grant N00014-18-1-2429 and from the National Science Foundation under Grant No. 1712752. R.H. and Z.T acknowledge the support from the Department of the Navy, Office of Naval Research under ONR award number N00014-18-1-2724. AGF work used Oak Ridge Leadership Computing Facility (OLCF), which is a DOE Office of Science User Facility supported under Contract DE-AC05-00OR22725.

[1] P. L. Kapitza, Heat transfer and superfluidity of helium II, Phys. Rev. 60, 354 (1941).

[2] E. T. Swartz and R. O. Pohl, Thermal boundary resistance, Rev. Mod. Phys. 61, 605 (1989).

[3] A. Giri and P. E. Hopkins, A review of experimental and computational advances in thermal boundary conductance and nanoscale thermal transport across solid interfaces, Adv. Funct. Mater. 30, 1903857 (2020).

[4] C. Monachon, L. Weber, and C. Dames, Thermal boundary conductance: a materials science perspective, Annu. Rev. Mater. Res. 46, 433 (2016).

[5] P. E. Hopkins, Thermal transport across solid interfaces with nanoscale imperfections: effects of roughness, disorder, dislo- cations, and bonding on thermal boundary conductance, ISRN Mech. Eng. 2013, 682586 (2013).

[6] P. Jiang, X. Qian, and R. Yang, Tutorial: Time-domain ther- moreflectance (TDTR) for thermal property characterization of bulk and thin film materials, J. Appl. Phys. 124, 161103 (2018).

[7] D. G. Cahill, Analysis of heat flow in layered structures for time-domain thermoreflectance, Rev. Sci. Instrum. 75, 5119 (2004).

[8] A. J. Schmidt, X. Chen, and G. Chen, Pulse accumulation, radial heat conduction, and anisotropic thermal conductivity in pump-probe transient thermoreflectance, Rev. Sci. Instrum. 79, 114902 (2008).

[9] D. Rodin and S. K. Yee, Simultaneous measurement of in-plane and through-plane thermal conductivity using beam-offset frequency domain thermoreflectance, Rev. Sci. Instrum. 88, 014902 (2017).

[10] A. J. Schmidt, R. Cheaito, and M. Chiesa, A frequency-domain thermoreflectance method for the characterization of thermal properties, Rev. Sci. Instrum. 80, 094901 (2009).

[11] P. Jiang, X. Qian, X. Gu, and R. Yang, Probing anisotropic thermal conductivity of transition metal dichalcogenides $MX_2$ ($M=$ Mo, W and $X=$ S, Se) using time-domain thermore- flectance, Adv. Mater. 29, 1701068 (2017).

[12] A. Sood, J. Cho, K. D. Hobart, T. Feygelson, B. Pate, M. Asheghi, and K. E. Goodson, Anisotropic and nonhomogeneous thermal conduction in $1\ \mu$m thick CVD diamond, in Fourteenth Intersociety Conference on Thermal and Thermomechanical Phenomena in Electronic Systems (ITherm), Orlando, FL (IEEE, 2014), pp. 1192–1198.

[13] Y. Xu, D. Kraemer, B. Song, Z. Jiang, J. Zhou, J. Loomis, J. Wang, M. Li, H. Ghasemi, X. Huang, X. Li, and G. Chen, Nanostructured polymer films with metal-like thermal conduc- tivity, Nat. Commun. 10, 1771 (2019).

[14] Y. Koh and D. Cahill, Frequency dependence of the thermal conductivity of semiconductor alloys, Phys. Rev. B 76, 075207 (2007).

[15] Y. R. Koh, M. Shirazi-Hd, B. Vermeersch, A. M. S. Mohammed, J. Shao, G. Pernot, J. H. Bahk, M. J. Manfra, and A. Shakouri, Quasi-ballistic thermal transport in Al0.1Ga0.9N thin film semiconductors, Appl. Phys. Lett. 109, 243107 (2016).

[16] R. M. Costescu, M. A. Wall, and D. G. Cahill, Thermal conductance of epitaxial interfaces, Phys. Rev. B 67, 054302 (2003).

[17] G. T. Hohensee, R. B. Wilson, and D. G. Cahill, Thermal conductance of metal-diamond interfaces at high pressure, Nat. Commun. 6, 6578 (2015).

[18] Z. Cheng, Y. R. Koh, H. Ahmad, R. Hu, J. Shi, M. E. Liao, Y. Wang, T. Bai, R. Li, E. Lee, E. A. Clinton, C. M. Matthews, Z. Engel, Yates, T. Luo, M. S. Goorsky, W. Doolittle, Z. Tian, P. E. Hopkins et al., Thermal conductance across harmonic-matched epitaxial Al-sapphire heterointerfaces, Commun. Phys. 3, 115 (2019).

[19] P. E. Hopkins, R. N. Salaway, R. J. Stevens, and P. M. Norris, Temperature-dependent thermal boundary conductance at Al/Al 2O 3 and Pt/Al 2O 3 interfaces, Int. J. Thermophys. 28, 947 (2007).

[20] P. E. Hopkins, T. Beechem, J. C. Duda, K. Hattar, J. F. Ihlefeld, M. A. Rodriguez, and E. S. Piekos, Influence of anisotropy on thermal boundary conductance at solid interfaces, Phys. Rev. B 84, 125408 (2011).

[21] R. Prasher, Acoustic mismatch model for thermal contact resis- tance of van der Waals contacts, Appl. Phys. Lett. 94, 041905 (2009).

[22] P. Reddy, K. Castelino, and A. Majumdar, Diffuse mismatch model of thermal boundary conductance using exact phonon dispersion, Appl. Phys. Lett. 87, 211908 (2005).

[23] W. Zhang, T. S. Fisher, and N. Mingo, The atomistic Green’s function method: An efficient simulation approach for nanoscale phonon transport, Numer. Heat Transf. Part B 51, 333 (2007).

[24] M. G. Muraleedharan, K. Gordiz, S. Ju, J. Shiomi, V. Yang, and A. Henry, Thermal interface conductance between aluminum and aluminum oxide: A rigorous test of atomistic level theories, arXiv:1807.06631v1.

[25] J. T. Gaskins, G. Kotsonis, A. Giri, S. Ju, A. Rohskopf, Y. Wang, T. Bai, E. Sachet, C. T. Shelton, Z. Liu, Z. Cheng, B. M. Foley, S. Graham, T. Luo, A. Henry, M. S. Goorsky, J. Shiomi, J. P. Maria, and P. E. Hopkins, Thermal boundary conductance across heteroepitaxial ZnO/GaN interfaces: assessment of the phonon gas model, Nano Lett. 18, 7469 (2018).

[26] J. Shi, X. Yang, T. S. Fisher, and X. Ruan, Dramatic increase in the thermal boundary conductance and radiation limit from a nonequilibrium Landauer approach, arXiv:1812.07910v2 (2018).

[27] R. Cheaito, J. T. Gaskins, M. E. Caplan, B. F. Donovan, B. M. Foley, A. Giri, J. C. Duda, C. J. Szwejkowski, C. Constantin, H. J. Brown-Shaklee, J. F. Ihlefeld, and P. E Hopkins, Thermal boundary conductance accumulation and interfacial phonon transmission: Measurements and theory, Phys. Rev. B 91, 035432 (2015).

[28] C. Hua, X. Chen, N. K. Ravichandran, and A. J. Minnich, Experimental metrology to obtain thermal phonon transmission coefficients at solid interfaces, Phys. Rev. B 95, 205423 (2017).

[29] N. Ye, J. P. Feser, S. Sadasivam, T. S. Fisher, T. Wang, C. Ni, and A. Janotti, Thermal transport across metal silicide-silicon interfaces: an experimental comparison between epitaxial and nonepitaxial interfaces, Phys. Rev. B 95, 085430 (2017).

[30] A. Hanisch, B. Krenzer, T. Pelka, S. Möllenbeck, and M. Horn– Von Hoegen, Thermal response of epitaxial thin Bi films on Si(001) upon femtosecond laser excitation studied by ultrafast electron diffraction, Phys. Rev. B 77, 125410 (2008).

[31] B. Krenzer, A. Hanisch-Blicharski, P. Schneider, T. Payer, S. Möllenbeck, O. Osmani, M. Kammler, R. Meyer, and M. Horn–Von Hoegen, Phonon confinement effects in ultrathin epi- taxial bismuth films on silicon studied by time-resolved electron diffraction, Phys. Rev. B 80, 024307 (2009).

[32] R. B. Wilson, B. A. Apgar, W. P. Hsieh, L. W. Martin, and D. G. Cahill, Thermal conductance of strongly bonded metal-oxide interfaces, Phys. Rev. B 91, 115414 (2015).

[33] A. Giri, S. W. King, W. A. Lanford, A. B. Mei, D. Merrill, L. Li, R. Oviedo, J. Richards, D. H. Olson, J. L. Braun, J. T. Gaskins, F. Deangelis, A. Henry, and P. E. Hopkins, Interfacial defect vibrations enhance thermal transport in amorphous multilayers with ultrahigh thermal boundary conductance, Adv. Mater. 30, 1804097 (2018).

[34] D. R. Lide and G. Baysinger, CRC handbook of chemistry and physics: A ready-reference book of chemical and physical data, Choice Rev. Online 41, 41-4368-41 (2004).

[35] J. Franc, N. Morgado, R. Flaminio, R. Nawrodt, I. Martin, L. Cunningham, A. Cumming, S. Rowan, and J. Hough, Mirror thermal noise in laser interferometer gravitational wave detectors operating at room and cryogenic temperature, arXiv:0912.0107v1 (2009).

[36] A. E. Kaloyeros, Y. Pan, J. Goff, and B. Arkles, Editors' Choice—Review—Cobalt thin films: Trends in processing tech- nologies and emerging applications, ECS J. Solid State Sci. Technol. 8, P119 (2019).

[37] B. Hälg, On a micro-electro-mechanical nonvolatile memory cell, IEEE Trans. Electron Dev. 37, 2230 (1990).

[38] H. Lee, R. A. Coutu, S. Mall, and K. D. Leedy, Characterization of metal and metal alloy films as contact materials in MEMS switches, J. Micromech. Microeng. 16, 557 (2006).

[39] I. Chisti, V. Kitaeva, N. Sobolev, and V. Bakhar, Investigation of the molecular scattering of light in a sapphire crystal, Sov. J. Exp. Theor. Phys. 36, 783 (1973).

[40] F. Cardarelli and F. Cardarelli, Materials Handbook: A Concise Desktop Reference (Springer, London, 2008).

[41] E. R. Smith, Electrostatic energy in ionic crystals, Proc. R. Soc. London, Ser. A 375, 475 (2009).

[42] C. Y. Ho, R. W. Powell, and P. E. Liley, Thermal conductivity of the elements: A comprehensive review, J. Phys. Chem. Ref. Data 3, 1 (1974).

[43] E. Milosevic, S. Kerdsongpanya, A. Zangiabadi, K. Barmak, K. R. Coffey, and D. Gall, Resistivity size effect in epitaxial Ru(0001) layers, J. Appl. Phys. 124, 165105 (2018).

[44] E. Milosevic, S. Kerdsongpanya, M. E. McGahay, A. Zangiabadi, K. Barmak, and D. Gall, Resistivity scaling and electron surface scattering in epitaxial Co(0001) layers, J. Appl. Phys. 125, 245105 (2019).

[45] B. Wang and D. Gall, Fully strained epitaxial $Ti_{1-x}Mg_xN$(001) layers, Thin Solid Films 688, 137165 (2019).

[46] E. Milosevic, S. Kerdsongpanya, and D. Gall, The resistivity size effect in epitaxial Ru(0001) and Co(0001) layers, IEEE Nanotechnol. Symp. ANTS 2018, 1 (2019).

[47] B. Wang and D. Gall, A new semiconductor: Ti0.5Mg0.5N(001), in Proceeding of the 2018 IEEE Nanotechnology Symposium (ANTS), Albany, NY, USA (IEEE, 2018), pp. 1-5.

[48] D. Gall, I. Petrov, P. Desjardins, and J. E. Greene, Microstruc- tural evolution and Poisson ratio of epitaxial ScN grown on TiN(001)/MgO(001) by ultrahigh vacuum reactive magnetron sputter deposition, J. Appl. Phys. 86, 5524 (1999).

[49] D. Gall, I. Petrov, and J. E. Greene, Epitaxial $Sc_{1-x}Ti_xN$(001): Optical and electronic transport properties, J. Appl. Phys. 89, 401 (2001).

[50] J. S. Chawla, X. Y. Zhang, and D. Gall, Effective electron mean free path in TiN(001), J. Appl. Phys. 113, 063704 (2013).

[51] J. S. Chawla, X. Y. Zhang, and D. Gall, Epitaxial TiN(001) wetting layer for growth of thin single-crystal Cu(001), J. Appl. Phys. 110, 043714 (2011).

[52] M. A. Wall, D. G. Cahill, I. Petrov, D. Gall, and J. E. Greene, Nucleation kinetics during homoepitaxial growth of TiN(001) by reactive magnetron sputtering, Phys. Rev. B 70, 035413 (2004).

[53] C. S. Shin, D. Gall, N. Hellgren, J. Patscheider, I. Petrov, and J. E. Greene, Vacancy hardening in single-crystal TiNx(001) layers, J. Appl. Phys. 93, 6025 (2003).

[54] C. S. Shin, S. Rudenja, D. Gall, N. Hellgren, T. Y. Lee, I. Petrov, and J. E. Greene, Growth, surface morphology, and electrical resistivity of fully strained substoichiometric epitaxial TiNx (0.67 $\leqslant$ x < 1.0) layers on MgO(001), J. Appl. Phys. 95, 356 (2004).

[55] J. C. Duda, C. J. Kimmer, W. A. Soffa, X. W. Zhou, R. E. Jones, and P. E. Hopkins, Influence of crystallographic orientation and anisotropy on Kapitza conductance via classical molecular dynamics simulations, J. Appl. Phys. 112, 093515 (2012).

[56] J. C. Duda, T. E. Beechem, J. L. Smoyer, P. M. Norris, and P. E. Hopkins, Role of dispersion on phononic thermal boundary conductance, J. Appl. Phys. 108, 073515 (2010).

[57] R. J. Stevens, A. N. Smith, and P. M. Norris, Measurement of thermal boundary conductance of a series of metal-dielectric interfaces by the transient thermoreflectance technique, J. Heat Transf. 127, 315 (2005).

[58] P. M. Norris and P. E. Hopkins, Examining interfacial diffuse phonon scattering through transient thermoreflectance measure- ments of thermal boundary conductance, J. Heat Transf. 131, 043207 (2009).

[59] P. E. Hopkins and P. M. Norris, Contribution of ballistic electron transport to energy transfer during electron-phonon nonequilib- rium in thin metal films, J. Heat Transf. 131, 043208 (2009).

[60] S. Shin, M. Kaviany, T. Desai, and R. Bonner, Roles of atomic restructuring in interfacial phonon transport, Phys. Rev. B 82, 081302 (2010).

[61] G. Kresse and J. Furthmüller, Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set, Comput. Mater. Sci. 6, 15 (1996).

[62] G. Kresse and J. Hafner, Ab initio molecular dynamics for open-shell transition metals, Phys. Rev. B 48, 13115 (1993).

[63] X. Li and R. Yang, Effect of lattice mismatch on phonon trans- mission and interface thermal conductance across dissimilar material interfaces, Phys. Rev. B 86, 054305 (2012).

[64] K. Gordiz and A. Henry, A formalism for calculating the modal contributions to thermal interface conductance, New J. Phys. 17, 103002 (2015).

[65] See Supplemental Material at http://link.aps.org/supplemental/10.1103/PhysRevB.102.205304 for a description on molecular- beam epitaxy (MBE), magnetron sputtering, the modal nonequilibrium Landauer approach, the atomistic Green's func- tion (AGF), and time-domain thermoreflectance (TDTR) (see also references therein [18,26,66-95]).

[66] B. Wang, S. Kerdsongpanya, M. E. McGahay, E. Milosevic, P. Patsalas, and D. Gall, Growth and properties of epitaxial $Ti_{1-x}Mg_x$ N(001) layers, J. Vac. Sci. Technol. A 36, 061501 (2018).


[67] A. S. Ingason, F. Magnus, S. Olafsson, and J. T. Gudmundsson, Morphology of TiN thin films grown on MgO(001) by reactive dc magnetron sputtering, J. Vac. Sci. Technol. A 28, 912 (2010).

[68] K. Zhang, K. Balasubramanian, B. D. Ozsdolay, C. P. Mulligan, S. V. Khare, W. T. Zheng, and D. Gall, Growth and mechanical properties of epitaxial NbN(001) films on MgO(001), Surf. Coatings Technol. 288, 105 (2016).

[69] B. D. Ozsdolay, C. P. Mulligan, M. Guerette, L. Huang, and D. Gall, Epitaxial growth and properties of cubic WN on MgO(001), MgO(111), and Al2O3(0001), Thin Solid Films 590, 276 (2015).

[70] R. Deng, P. Y. Zheng, and D. Gall, Optical and electron transport properties of rock-salt $Sc_{1-x}Al_xN$, J. Appl. Phys. 118, 015706 (2015).

[71] R. Deng, B. D. Ozsdolay, P. Y. Zheng, S. V. Khare, and D. Gall, Optical and transport measurement and first-principles determination of the ScN band gap, Phys. Rev. B 91, 045104 (2015).

[72] B. D. Ozsdolay, X. Shen, K. Balasubramanian, G. Scannell, L. Huang, M. Yamaguchi, and D. Gall, Elastic constants of epitaxial cubic $MoN_x(001)$ layers, Surf. Coatings Technol. 325, 572 (2017).

[73] D. Gall, C. S. Shin, R. T. Haasch, I. Petrov, and J. E. Greene, Band gap in epitaxial NaCl-structure CrN(001) layers, J. Appl. Phys. 91, 5882 (2002).

[74] C. S. Shin, D. Gall, Y. W. Kim, P. Desjardins, I. Petrov, J. E. Greene, M. Odn, and L. Hultman, Epitaxial NaCl structure $\delta-$ $TaN_x(001)$: electronic transport properties, elastic modulus, and hardness versus N/Ta ratio, J. Appl. Phys. 90, 2879 (2001).

[75] K. Zhang, K. Balasubramanian, B. D. Ozsdolay, C. P.Mulligan, S. V. Khare, W. T. Zheng, and D. Gall, Epitaxial $NbC_xN_{1-x}(001)$ layers: Growth, mechanical properties, and electrical resistivity, Surf. Coatings Technol. 277, 136 (2015).

[76] N. Mingo and L. Yang, Phonon transport in nanowires coated with an amorphous material: An atomistic Green's function approach, Phys. Rev. B 68, 245406 (2003).

[77] W. Zhang, T. S. Fisher, and N. Mingo, Simulation of interfacial phonon transport in Si-Ge heterostructures using an atomistic Green's function method, J. Heat Transf. 129, 483 (2007).

[78] W. Zhang, N. Mingo, and T. S. Fisher, Simulation of phonon transport across a non-polar nanowire junction using an atomistic Green's function method, Phys. Rev. B 76, 195429 (2007).

[79] K. Momma and F. Izumi, VESTA 3 for three-dimensional visualization of crystal, volumetric and morphology data, J. Appl. Crystallogr. 44, 1272 (2011).

[80] K. Esfarjani, G. Chen, and H. T. Stokes, Heat transport in silicon from first-principles calculations, Phys. Rev. B 84, 085204 (2011)

[81] Z. Tian, J. Garg, K. Esfarjani, T. Shiga, J. Shiomi, and G. Chen, Phonon conduction in PbSe, PbTe, and $PbTe_{1-x}Se_x$ from first principles calculations, Phys. Rev. B 85, 184303 (2012).

[82] P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, G. L. Chiarotti, M. Cococcioni, I. Dabo, A. Dal Corso, S. De Gironcoli, S. Fabris, G. Fratesi, R. Gebauer, U. Gerstmann, C. Gougoussis, A. Kokalj, M. Lazzeri et al., Quantum espresso: A modular and open-source software project for quantum simulations of materials, J. Phys.: Condens. Matter 21, 395502 (2009).

[83] A. Togo and I. Tanaka, First principles phonon calculations in materials science, Scr. Mater. 108, 1 (2015).

[84] P. E. Blöchl, Projector augmented-wave method, Phys. Rev. B 50, 17953 (1994).

[85] J. P. Perdew, K. Burke, and M. Ernzerhof, Generalized Gradient Approximation Made Simple, Phys. Rev. Lett. 77, 3865 (1996)

[86] Z. Tian, K. Esfarjani, and G. Chen, Enhancing phonon transmission across a Si/Ge interface by atomic roughness: First-principles study with the Green's function method, Phys. Rev. B 86, 235304 (2012)

[87] Thermophysical Properties of High Temperature Solid Materials (Purdue Research Foundation, 1967).

[88] S. A. Montague, C. W. Draper, and G. M. Rosenblatt, Thermal diffusivities of hafnium and cobalt from 300 to 1000 K, J. Phys. Chem. Solids 40, 987 (1979).

[89] J. J. Valencia and Peter N. Quested, Thermophysical poperties, in Metal Process Simulation, edited by D. U. Furrer and S. L. Semiatin, ASM Handbook Vol. 22B (ASM International, 2010).

[90] R. W. Powell, R. P. Tye, and M. J. Woodman, The thermal conductivity and electrical resistivity of polycrystalline metals of the platinum group and of single crystals of ruthenium, J. Less-Common Met. 12, 1 (1967).

[91] M. W. Chase, NIST-JANAF Thermochemical Tables, 4th ed. (American Institute of Physics, USA, 1998).

[92] N. N. Sirota, V. A. Vinokurov, and V. V. Novikov, Heat capacity and thermodynamic functions of iron, cobalt, and nickel borides in the range of 5-300 K, Zh. Fiz. Khim. 72, 785 (1998).

[93] G. T. Furukawa, M. L. Reilly, and J. S. Gallagher, Critical analysis of heat-capacity data and evaluation of thermodynamic properties of ruthenium, rhodium, palladium, iridium, and platinum from 0 to 300 K. A survey of the literature data on osmium, J. Phys. Chem. Ref. Data 3, 163 (1974).

[94] D. G. Cahill, S. Lee, and T. I. Selinder, Thermal conductivity of $\kappa$-Al$_2$O$_3$ and $\alpha$-Al$_2$O$_3$ wear-resistant coatings, J. Appl. Phys. 83, 5783 (1998).

[95] N. N. Kovalev, A. V. Petrov, and O. V. Sorkin, Thermal conductivity of single crystals of barium, strontium, calcium, and magnesium oxides, Sov. Phys. Solid State 13, 232 (1971).
