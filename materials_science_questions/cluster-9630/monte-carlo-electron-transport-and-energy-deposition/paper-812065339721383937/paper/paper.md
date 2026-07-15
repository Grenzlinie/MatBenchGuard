![](./images/812065339721383937_1.jpg)

Available online at www.sciencedirect.com

![](./images/812065339721383937_2.jpg)

Surface Science 600 (2006) 4464-4474

![](./images/812065339721383937_3.jpg)

# Angle-resolved elastic-peak electron spectroscopy: Solid-state effects

## A. Jablonski $^{a, *}$, J. Zemek $^{b}$
$^{a}$ Institute of Physical Chemistry, Polish Academy of Sciences, ul. Kasprzaka 44/52, 01-224 Warszawa, Poland
$^{b}$ Institute of Physics, Academy of Sciences of the Czech Republic, Cukrovarnicka 10, 162 53 Prague 6, Czech Republic

Received 10 April 2006; accepted for publication 3 July 2006
Available online 31 July 2006

### Abstract
It has been frequently reported that characteristics of electrons elastically backscattered from solid surfaces (e.g., the angular distri- bution) are well described by Monte Carlo simulations of electron trajectories in solids. The theoretical model implemented in these simulations requires knowledge of accurate differential elastic-scattering cross sections (DCSs). In computational practice, the DCSs for isolated neutral atoms constituting the solid are used to simplify the calculations. In reality, the interaction potential between an elec- tron and an atom inside a solid is different from the interaction between an electron and an isolated atom. In the present work, we study changes of the DCSs due to agglomeration of atoms. The interaction between an atom and an electron in the solid is approximated by the muffin-tin potential. It has been found that the DCSs are considerably influenced by the agglomeration of atoms for small scattering angles. The difference for silicon reaches 500% for silicon at 200 eV. On the other hand, electron elastic-backscattering probabilities cal- culated using DCSs from two potentials were only slightly affected. Calculations and measurements of elastically backscattered intensity were compared for 10 elemental solids, a number of emission angles from $35^{\circ}$ to $74^{\circ}$ , and three energies (200 eV, 500 eV, and 1000 eV). The experimental angular distributions compare very well with the calculated distributions; the mean percentage deviation between them was about 10% at 200 eV, and decreased to about 5% at 1000 eV. Agreement between theory and experiment was not improved when DCSs determined from muffin-tin potentials were used in the calculations. This result justifies the use of DCSs for isolated atoms in theoretical description of elastic-electron backscattering from surfaces.
© 2006 Elsevier B.V. All rights reserved.

Keywords: Computer simulations; Electron-solid interactions; Electron-solid scattering and transmission-elastic; Monte Carlo simulations; Electron spectroscopy; Amorphous surfaces

---

### 1. Introduction
Analytical techniques founded on measurements of the elastic-electron backscattering intensity are known by the acronym EPES (elastic-peak electron spectroscopy) [1-3]. A frequent application of such technique is the determina- tion of the electron inelastic mean free path in the surface region of solids [1]. This method is recognized as the only experimental source providing IMFPs which agree with the ASTM definition [4] of this parameter. The relevant experiment consists in measurements of the elastic-peak intensity in a particular experimental configuration, and the IMFP value is obtained after fitting the calculated intensity to the measured intensity. It is of crucial impor- tance to use in calculations a reliable theoretical model that describes well the phenomenon of elastic backscattering from solids in different experimental configurations.

A useful test of validity of the theoretical model, describ- ing the elastically backscattered intensity, is a comparison of the experimental angular distribution of elastically back- scattered electrons with the calculated distribution. Such a comparison has been made already in 1970 by Schilling and Webb [5] in studies of electron elastic backscattering from liquid mercury. These authors developed a relatively simple analytical theory taking into account multiple elastic colli- sions in the solid. It has been shown in later works that the

* Corresponding author.
E-mail address: jablo@ichf.edu.pl (A. Jablonski).

0039-6028/$ - see front matter © 2006 Elsevier B.V. All rights reserved.
doi:10.1016/j.susc.2006.07.011

angular distribution of elastically backscattered electron is well described by Monte Carlo simulations of electron tra- jectories in the solid [6–8]. There are also analytical theories describing elastic-electron backscattering; however the rel- evant formalism becomes very complicated [8–11]. In com- putational practice, the Monte Carlo simulations presently seem to be the most accurate and convenient in determina- tion of different characteristics of backscattered electrons, in particular, in calculations of the angular distribution. The drawback of this approach is the relatively large com- putational effort that is needed to reach a reasonable accu- racy. A prospective approach is the recently proposed trajectory-reversal algorithm which exhibits relatively fast convergence [12].

Measurements of the elastic-backscattering probabilities for determination of the IMFP can be performed in differ- ent experimental configurations. As follows from a compi- lation of such configurations [1], the primary beam was incident along the surface normal in practically all pub- lished reports. The emission angles varied in a wide range depending on the configuration of the spectrometer: from $20^{\circ}$ to $70^{\circ}$ in the case of small acceptance angle analyzers, or between $5^{\circ}$ and $55^{\circ}$ in the case of integrated signal by the retarding field analyzers. If a theoretical model is reliable, the resulting IMFP should not depend on the experimental geometry. This issue has been approached by Jablonski and Jiricek [13] who determined the IMFPs for Si, Cu, Ag and Au from elastic-backscattering probabilities mea- sured for emission angles ranging form $5^{\circ}$ to $45^{\circ}$. Notice able variation of the IMFPs were observed for emission angles smaller than $25^{\circ}$. These effects were ascribed to the deficiency of the theoretical model. In a recent work [14], two Monte Carlo strategies were compared: conventional simulation and the trajectory-reversal simulation. It was found that these algorithms lead to insignificant differ- ences. It is also well known that the differential elastic-scat- tering cross sections (DCS) originating from different sources may considerably affect the resulting IMFPs [3]. This issue is also approached in detail in the present work.

In all theoretical models describing the effect of elastic backscattering, the DCSs used in calculations were calcu- lated for isolated neutral atoms. Obviously, the potential describing the interaction between an electron and an iso- lated atom and the potential between an electron and atom inside a solid must be different. Preliminary calculations of the DCSs for the muffin-tin potential, simulating a solid, indicate that they are different from the DCSs calculated for neutral atoms [15,16]. Furthermore, the use of the DCSs from the muffin-tin potential and DCSs from the po- tential for the isolated atoms leads to differences in the resulting attenuation length values [17], although this dif- ference is not very pronounced. An obvious question arises if the theoretical models for elastic-electron backscattering from solids based on the DCSs calculated for the muffin-tin potentials are more accurate than the models using the DCSs calculated for neutral atoms. To answer this ques- tion, we compare here the elastic-backscattering probabili- ties calculated using different DCSs with the elastically backscattered intensities measured in different experimen- tal geometries.

## 2. Experimental

### 2.1. Spectrometer

The elastic-peak spectra were recorded with an angle-re- solved photoelectron spectrometer ADES 400 (VG Scien- tific, UK) equipped with an electron gun (Varian, model 981-2455), Mg K$\alpha$ (1253.6 eV) and Al K$\alpha$ (1486.6 eV) X- ray sources, and a rotatable hemispherical electron energy analyzer. In the reported measurements, the analyzer was operated in the FAT mode at a pass energy 100 eV for XPS or 20 eV for EPES. The electron-beam current was $0.1–1.0\ \mu$A, and the electron-beam diameter at the sample surface was $\sim$3 mm. The electron elastic-backscattering intensities were recorded at primary-electron kinetic ener- gies of 200 eV, 500 eV, and 1000 eV. During measurements, the electron-beam incidence angle was normal to the sam- ple surface, while the emission angles were varied by rota- tion of the analyzer between an emission angle of $35^{\circ}$ with respect to the surface normal and an emission angle of $74^{\circ}$. Elastically backscattered electrons were collected by the analyzer within a small conical acceptance angle. The half-cone angle of the analyzer was $4.1^{\circ}$. The experimental geometry was carefully checked by a laser beam technique.

### 2.2. Samples

Elastic-backscattering intensities from Si, Fe, Co, Ni, Cu, Pd, Ag, Sm, Ir, and Au samples were measured in all experimental geometries considered. Before the EPES mea- surements, all sample surfaces were sputter-cleaned until no traces of contamination were seen in the XPS spectra. The typical width at half maximum of the elastic peak in the applied energy range was $\leqslant$0.5 eV. The inelastic-elec- tron background was subtracted using Shirley’s procedure. The silicon sample was a Si(111) wafer cut from a Si single crystal and polished. The surface roughness was evaluated to be below 1 nm. The samples of Fe, Co, Ni, Cu, Ag, Ir and Au were metal overlayers deposited on the Si(111) substrate. This procedure ensured high smoothness of the sample. The thickness of the deposited layer was in the vicinity of 400 nm, and was controlled during deposition by a crystal quartz monitor. This thickness made possible further sample processing, i.e. amorphisation by sputtering prior to EPES measurements.

The polycrystalline palladium and samarium samples were polished metal foils: palladium (99.9%, Goodfellow, UK) with a thickness of 0.5 mm, and samarium (99.9%, Safina, Czech Republic). There were some experimental problems with removing oxygen from the samarium sam- ple. After prolonged sputtering, the oxygen signal became very small, although still visible. We estimate the final oxy- gen concentration as several atomic percent.

## 3. Theory

### 3.1. Elastic-scattering cross sections

The electron elastic-backscattering probability has been found to be dominated by a single large-angle elastic collision, although the contribution of multiple collisions is still significant and should not be ignored. It is then of crucial importance, in the Monte Carlo calculations, to use realistic elastic-scattering cross sections that describe the interaction between an electron and atoms constituting the solid. The usual practice is to use cross sections calculated for neutral isolated atoms. In the present work, we used cross sections calculated from the program package ELSEPA [18]. This software allows us to calculate cross sections for different potentials describing the interaction between an electron and an atom. The following assumptions were made in these calculations:

1.  The electron density of an atom was obtained from self-consistent Dirac–Hartree–Fock calculations.
2.  The nucleus is assumed to have a finite size, and the positive charge density is described by the Fermi distribution [19].
3.  The Furness and McCarthy [20] local exchange potential was assumed.

Similar to recent work [16], aggregation of atoms is assumed to be well described by the muffin-tin potential. The corresponding calculations of the DCSs were performed using the ELSEPA software. In these calculations, the needed parameter is the muffin-tin radius, $R_{\text{mt}}$. It has been assumed that this radius is equal to the interatomic distance divided by two. The interatomic distances for the considered elements were taken from the compilation of Pearson [21]. For details, the reader is referred to the original work [18].

![](./images/812065339721383937_4.jpg)

Fig. 1. Differential elastic-scattering cross sections, $\mathrm{d}\sigma/\mathrm{d}\Omega$, calculated for silicon. Solid line: the DHF potential for neutral atoms; dashed line: the corresponding muffin-tin potential. (a) Energy of 200 eV; (b) 500 eV; (c) 1000 eV.

![](./images/812065339721383937_5.jpg)

Fig. 2. The percentage deviation, defined by Eq. (1), between differential elastic-scattering cross sections shown in Fig. 1. (a) Energy of 200 eV; (b) 500 eV; (c) 1000 eV.

### 3.2. Monte Carlo simulations of electron trajectories

Different Monte Carlo strategies can be used in simulations of elastically backscattered electrons from amorphous and polycrystalline solids. Two approaches were compared in a recent work [14]. Generally, the Monte Carlo algorithms are founded on the assumption that the electron trajectory follows the Poisson stochastic process. In typical strategies used in calculations of the IMFP from the elastic-peak intensity [1], the trajectory is simulated from the point of entering the solid to the point of leaving the solid (forward simulation). However, it has been indicated recently that an algorithm based on the trajectory-reversal principle (simulation started from the point of leaving the solid) has a number of advantages [12]. It is much faster than forward scattering, and needs much less computing time, particularly for analyzers with a small acceptance angle. Both simulation strategies were found to be practically equivalent [12,14]. In the present work, only the conventional algorithm of forward simulation was used.

![](./images/812065339721383937_6.jpg)

Fig. 3. Elastic-backscattering probability, $\eta$, calculated for silicon as a function of the emission angle, $\alpha$. Solid line: the DHF potential for neutral atoms; dashed line: the corresponding muffin-tin potential. (a) Energy of 200 eV; (b) 500 eV; (c) 1000 eV.

### 4. Results

The DCSs calculated for muffin-tin potential were found to distinctly differ from the DCSs corresponding to the isolated neutral atoms [15,16]. Particularly large deviations are observed for small scattering angles. This is illustrated in Fig. 1 showing DCSs calculated for silicon at energies of 200 eV, 500 eV, and 1000 eV. At 200 eV, above $30^{\circ}$, the differences in the DCSs due to agglomeration are rather small although noticeable. At higher energies, these differences are within the thickness of the line. Significant deviations are observed at scattering angles below $30^{\circ}$. To quantify these deviations, we have plotted in Fig. 2 the following percentage differences:

$$
\Delta \mathrm{DCS}=100 \frac{(\mathrm{d} \sigma / \mathrm{d} \Omega)_{\mathrm{na}}-(\mathrm{d} \sigma / \mathrm{d} \Omega)_{\mathrm{mt}}}{(\mathrm{d} \sigma / \mathrm{d} \Omega)_{\mathrm{mt}}} \tag{1}
$$

where the subscript na denotes the DCS for isolated neutral atoms, and the subscript mt denotes the DCSs calculated from the muffin-tin potential. We see that the difference

![](./images/812065339721383937_7.jpg)

Fig. 4. Percentage difference between elastic-backscattering probabilities, defined by Eq. (2), calculated for silicon as a function of the emission angle, $\alpha$. (a) Energy of 200 eV; (b) 500 eV; (c) 1000 eV.

between cross sections is dramatic for small scattering angles; the maximum difference varies from about 400% at 1000 eV to 500% at 200 eV. For scattering angles exceeding 30°, the percentage deviation is much smaller. Generally, the deviation is well below 10% with the exception of the DCS for the scattering angle of 40° at 200 eV where the deviation reaches 40%. Similar behaviour of the DCSs has been reported for other elements [16].

DCSs calculated for potentials of isolated atoms and for muffin-tin potentials were used in Monte Carlo calculations of the elastic-backscattering probability, $\eta$, over a wide range of emission angles, from 2° to 80° with respect to the surface normal. As in the majority of reported measurements of IMFPs [1], normal incidence of the primary beam has been assumed. In the present calculations, we used IMFPs calculated from experimental optical data [22], with the exception of samarium for which IMFPs were calculated from the predictive formula TPP-2M [23]. Facilities of the NIST IMFP database were used to determine IMFPs for a particular element and energy [24]. To reach reasonable precision of the elastic-backscattering probabilities, it was necessary to generate $2 \times 10^7$ electron trajectories. The same half-cone acceptance angle of the analyzer as in the experimental setup has been assumed, i.e. 4.1°.

For all elements and energies considered here, despite dramatic differences in the magnitudes of the DCSs, the calculated elastic-backscattering probabilities turned out to be very similar. This is illustrated in Fig. 3 showing results obtained for silicon. We see that the differences due to two potentials seem to be comparable or smaller than the statistical uncertainty of the Monte Carlo simulations at 500 eV and 1000 eV. At 200 eV, the difference is more systematic: the elastic-backscattering probability corresponding to the muffin-tin potential is noticeably larger that the corresponding probability obtained from the potential for isolated atoms in the region of small emission angles while this trend reverses above about 45°. To visual-

![](./images/812065339721383937_8.jpg)

Fig. 5. Comparison of the elastic-peak intensity measured for silicon with the calculated elastic-backscattering probability. Circles: elastic-peak intensity; solid line: elastic-backscattering probability calculated using the DCS for neutral atoms; dashed line: elastic-backscattering probability calculated using the DCS for the muffin-tin potential. (a) Energy of 200 eV; (b) 500 eV; (c) 1000 eV.

![](./images/812065339721383937_9.jpg)

Fig. 6. The same as Fig. 5 except for iron.

ize these deviations, the following percentage deviations have been calculated for the considered range of emission angles

$$
\Delta \eta=100 \frac{\eta_{\mathrm{na}}-\eta_{\mathrm{mt}}}{\eta_{\mathrm{mt}}}
\tag{2}
$$

The percentage differences for silicon are shown in Fig. 4. At 200 eV, the percentage deviation increases from about $-7\%$ at an emission angle of $2^\circ$ to $18\%$ at $80^\circ$. The mean percentage deviation defined by

$$
\langle\Delta \eta\rangle=\frac{1}{n} \sum_{i=1}^{n}\left|\Delta \eta_{i}\right|
\tag{3}
$$

is $7.1\%$, as indicated in Fig. 4. Note, however, that the percentage deviation is close to zero for emission angles close to $42^\circ$. This geometry corresponds to the cylindrical mirror analyzer which was frequently used in published measurements of IMFPs [1]. The percentage deviations observed at 500 eV and 1000 eV are scattered irregularly. The mean percentage deviation for these two energies is below $3\%$ which is comparable to the uncertainty of the Monte Carlo calculations.

One should mention that the above conclusions are not limited to silicon. A rather weak variation of $\eta$ due to agglomeration of atoms has been reported for other elements [16]. Despite this observation, we decided to compare calculated elastic-backscattering probabilities with the corresponding measured elastic-peak intensities, $I_{\mathrm{E}}$, to find out which theoretical model is closer to the experimental data. Since the measured intensities are proportional to the elastic-backscattering probabilities, we performed a fit of the calculated emission-angle dependence for each element and energy by minimization of the following expressions:

$$
Q_{\mathrm{na}}=\sum_{k=1}^{m}\left(C_{\mathrm{na}} \eta_{\mathrm{na}}^{(k)}-I_{\mathrm{E}}^{(k)}\right)^{2}
\tag{4a}
$$

$$
Q_{\mathrm{mt}}=\sum_{k=1}^{m}\left(C_{\mathrm{mt}} \eta_{\mathrm{mt}}^{(k)}-I_{\mathrm{E}}^{(k)}\right)^{2}
\tag{4b}
$$

![](./images/812065339721383937_10.jpg)

Fig. 7. The same as Fig. 5 except for cobalt.

![](./images/812065339721383937_11.jpg)

Fig. 8. The same as Fig. 5 except for nickel.

where the fitted constants $C_{\text{na}}$ and $C_{\text{mt}}$ are parameters for a given element and energy, and $m$ denotes the number of emission angles for which the measurements were made. The values of $C_{\text{na}}$ and $C_{\text{mt}}$ are not reported and compared here since experimental settings varied from run to run. Comparisons of measured intensities with elastically backscattered probabilities after the fits are shown in Figs. 5-14. In this way, we compare the shapes of the emission-angle dependences of measured and calculated backscattered signal intensities. Two conclusions can be derived from these results. Firstly, the experimental intensities compare very well with the calculated curves for all elements and energies. In particular, the position of maxima observed experimentally for high-atomic-number elements is practically reproduced by calculations (e.g., Figs. 12-14). Secondly, after the fitting procedure, the dependences calculated for the two considered DCSs are practically identical. Consequently, it is difficult to state which cross sections should be recommended for calculations of the elastically backscattered intensity.

![](./images/812065339721383937_12.jpg)

Fig. 9. The same as Fig. 5 except for copper.

## 5. Discussion and conclusions

The effect of a weak dependence of the elastically backscattered intensity on the DCSs for isolated atoms and for atoms in a solid has recently been submitted to extensive theoretical analysis [16]. It was found that the large difference between the DCSs, observed in the region of small scattering angles, has only a weak influence on the shape of the electron trajectory. The trajectory shape is determined mainly by the large-angle scattering events which have the same probability for the two considered interaction potentials. In effect, the probability of an electron for leaving the solid is practically identical for both DCSs.

A similar conclusion resulted from a study of the variation of the angular distribution of elastically backscattered electrons from the use of the Thomas-Fermi-Dirac (TFD) potential and from the Dirac-Hartree-Fock-Slater (DHFS) potential in calculations of DCSs [25]. The DCSs calculated from both potentials exhibited a significant difference at small scattering angles. For beryllium at 1000 eV, the difference in the DCSs was a factor of three

![](./images/812065339721383937_13.jpg)

Fig. 10. The same as Fig. 5 except for palladium.

for small scattering angles, below $2^\circ$. At the same energy, the total elastic-scattering cross section varied by 15–61%, depending on element. In contrast, the elastic-back-scattering probability varied much less. For an emission angle of $45^\circ$ at 1000 eV, the variation reached 9.4%, which is slightly more pronounced than the variation due to agglomeration observed in the present work. This result may be associated with the fact that the difference between DCSs resulting from the TFD and DHF potentials, although significant at small scattering angles, is also pro- nounced in some narrow angular regions at medium and large scattering angles (e.g., reaching 70% for Au at 1000 eV and a scattering angle of $100^\circ$ [26]). An extensive analysis of DCSs from the TFD and DHF potentials, and especially a comparison with DCSs determined exper- imentally for noble gases, indicate that DCSs derived from the DHF potential seems to be more accurate [26].

An attempt has been made here to analyze the devia- tions between the measured elastic-peak intensities, $I_{\rm E}$, and the fitted theoretical elastic-backscattering probabili- ties, $C\eta$. We assumed the same criteria for the quality of each fit as in the earlier analysis of measured IMFPs [1]. One of the measures of scatter is the mean percentage deviation

$$
R_{\rm na}=100\frac{1}{m}\sum_{k=1}^{m}\left| \frac{C_{\rm na}\eta_{\rm na}^{(k)}-I_{\rm E}^{(k)}}{C_{\rm na}\eta_{\rm na}^{(k)}} \right| \tag{5a}
$$

$$
R_{\rm mt}=100\frac{1}{m}\sum_{k=1}^{m}\left| \frac{C_{\rm mt}\eta_{\rm mt}^{(k)}-I_{\rm E}^{(k)}}{C_{\rm mt}\eta_{\rm mt}^{(k)}} \right| \tag{5b}
$$

These deviations are listed in Table 1. We see that the largest deviation reaches 18% although, in the majority of cases, the mean deviation is well below 10%. The total mean percentage deviations, $\langle R_{\rm na}\rangle$ and $\langle R_{\rm mt}\rangle$, systematically decrease with energy increase from 8.82% and 10.12% at 200 eV to 4.69% and 4.75%, respectively, at 1000 eV. An unexpected result is that the elastic-backscattering proba- bilities calculated using DCSs for isolated atoms seem to be slightly better fitted to the experimental data than the probabilities calculated using DCSs for the muffin-tin potentials. The last line in Table 1 shows the number of ele- ments for which the fit is better (smaller value of the mean

![](./images/812065339721383937_14.jpg)

Fig. 11. The same as Fig. 5 except for silver.

![](./images/812065339721383937_15.jpg)

Fig. 12. The same as Fig. 5 except for samarium.

percentage deviation). We see that the better performance for the model of isolated atoms is particularly pronounced at the lowest energy, i.e. 200 eV; at the two higher energies, there is no significant difference in results for the two potentials.

The quality of each fit can also be described by the root-mean-square deviations

$$
\mathrm{RMS}_{\mathrm{na}}=\sqrt{\frac{1}{m} \sum_{k=1}^{m}\left(C_{\mathrm{na}} \eta_{\mathrm{na}}^{(k)}-I_{\mathrm{E}}^{(k)}\right)^{2}} \tag{6a}
$$

$$
\mathrm{RMS}_{\mathrm{mt}}=\sqrt{\frac{1}{m} \sum_{k=1}^{m}\left(C_{\mathrm{mt}} \eta_{\mathrm{mt}}^{(k)}-I_{\mathrm{E}}^{(k)}\right)^{2}} \tag{6b}
$$

The RMS values are listed in Table 2. These values are expressed in arbitrary units associated with the spectrometer settings. They were kept constant in a particular experimental run (a particular element and energy); however, the setting and the spectrometer response could be different in different runs. For this reason, the total mean was not calculated. We can similarly indicate the number of cases for which RMS is smaller. The results are practically the same as for the mean percentage deviation.

A useful result of the present analysis is the fact that the use of potentials for isolated atoms in calculations of DCSs is justified in Monte Carlo simulations of electron transport in solids, in calculations of the elastic-backscattering probability. This observation is valid for electron energies of 200 eV or higher. In effect, the Monte Carlo calculations are considerably simplified since DCSs for isolated atoms are readily available [18,27]. Determination of the muffin-tin potentials may be a major problem. For the elemental solid, we can assume that the muffin-tin radius, $R_{\mathrm{mt}}$, is equal to half of the interatomic distance. For compounds with complex crystallographic structure, however, the determination of the muffin-tin radius is not straightforward.

One should also stress that the model of a solid considered here, described by muffin-tin potentials, is still an approximation. In our calculation of the DCSs, we neglected the contribution of electron absorption due to scattering into inelastic channels [18]. In general, the

![](./images/812065339721383937_16.jpg)

Fig. 13. The same as Fig. 5 except for iridium.

![](./images/812065339721383937_17.jpg)

Fig. 14. The same as Fig. 5 except for gold.

**Table 1**
Mean percentage deviations calculated from Eqs. (5a) and (5b)

<table>
<thead>
<tr>
<th>Element</th>
<th colspan="2">$E=200$ eV</th>
<th colspan="2">$E=500$ eV</th>
<th colspan="2">$E=1000$ eV</th>
</tr>
<tr>
<th></th>
<th>Isolated atom</th>
<th>Muffin-tin</th>
<th>Isolated atom</th>
<th>Muffin-tin</th>
<th>Isolated atom</th>
<th>Muffin-tin</th>
</tr>
</thead>
<tbody>
<tr>
<td>Si</td>
<td>5.38</td>
<td>2.61</td>
<td>4.62</td>
<td>4.38</td>
<td>6.44</td>
<td>6.93</td>
</tr>
<tr>
<td>Fe</td>
<td>13.08</td>
<td>18.17</td>
<td>7.96</td>
<td>6.06</td>
<td>8.22</td>
<td>8.05</td>
</tr>
<tr>
<td>Co</td>
<td>14.45</td>
<td>17.12</td>
<td>3.80</td>
<td>6.69</td>
<td>1.30</td>
<td>1.19</td>
</tr>
<tr>
<td>Ni</td>
<td>15.35</td>
<td>17.80</td>
<td>3.57</td>
<td>7.34</td>
<td>2.19</td>
<td>1.36</td>
</tr>
<tr>
<td>Cu</td>
<td>15.01</td>
<td>17.39</td>
<td>16.85</td>
<td>15.04</td>
<td>5.70</td>
<td>5.32</td>
</tr>
<tr>
<td>Pd</td>
<td>5.94</td>
<td>6.52</td>
<td>4.47</td>
<td>4.38</td>
<td>2.56</td>
<td>2.97</td>
</tr>
<tr>
<td>Ag</td>
<td>5.08</td>
<td>4.40</td>
<td>4.54</td>
<td>3.75</td>
<td>7.62</td>
<td>9.41</td>
</tr>
<tr>
<td>Sm</td>
<td>4.00</td>
<td>5.80</td>
<td>3.13</td>
<td>5.06</td>
<td>5.83</td>
<td>4.39</td>
</tr>
<tr>
<td>Ir</td>
<td>5.90</td>
<td>8.13</td>
<td>3.74</td>
<td>3.23</td>
<td>3.64</td>
<td>4.43</td>
</tr>
<tr>
<td>Au</td>
<td>3.96</td>
<td>3.31</td>
<td>10.08</td>
<td>10.14</td>
<td>3.39</td>
<td>3.43</td>
</tr>
<tr>
<td>Total mean</td>
<td>8.82</td>
<td>10.12</td>
<td>6.28</td>
<td>6.61</td>
<td>4.69</td>
<td>4.75</td>
</tr>
<tr>
<td>$N$</td>
<td>7</td>
<td>3</td>
<td>4</td>
<td>6</td>
<td>5</td>
<td>5</td>
</tr>
</tbody>
</table>

Last line indicates the number of elements, $N$, for which the mean percentage deviation is smaller for the potential indicated at the top of the column.

**Table 2**
Root-mean-square deviations calculated from Eqs. (6a) and (6b)

<table>
<thead>
<tr>
<th>Element</th>
<th colspan="2">$E=200$ eV</th>
<th colspan="2">$E=500$ eV</th>
<th colspan="2">$E=1000$ eV</th>
</tr>
<tr>
<th></th>
<th>Isolated atom</th>
<th>Muffin-tin</th>
<th>Isolated atom</th>
<th>Muffin-tin</th>
<th>Isolated atom</th>
<th>Muffin-tin</th>
</tr>
</thead>
<tbody>
<tr>
<td>Si</td>
<td>8230.0</td>
<td>3336.5</td>
<td>9790.8</td>
<td>9637.5</td>
<td>26313.6</td>
<td>26654.0</td>
</tr>
<tr>
<td>Fe</td>
<td>13112.8</td>
<td>18832.8</td>
<td>14650.8</td>
<td>10719.5</td>
<td>5455.5</td>
<td>5394.8</td>
</tr>
<tr>
<td>Co</td>
<td>69090.5</td>
<td>83578.6</td>
<td>2863.8</td>
<td>4470.8</td>
<td>491.5</td>
<td>427.4</td>
</tr>
<tr>
<td>Ni</td>
<td>77173.2</td>
<td>92633.8</td>
<td>2308.2</td>
<td>4272.0</td>
<td>798.8</td>
<td>482.9</td>
</tr>
<tr>
<td>Cu</td>
<td>26683.5</td>
<td>31499.0</td>
<td>37771.0</td>
<td>31509.4</td>
<td>7813.3</td>
<td>7596.5</td>
</tr>
<tr>
<td>Pd</td>
<td>37311.9</td>
<td>39751.6</td>
<td>5144.1</td>
<td>4922.9</td>
<td>1681.3</td>
<td>1807.4</td>
</tr>
<tr>
<td>Ag</td>
<td>18469.9</td>
<td>17797.4</td>
<td>25036.4</td>
<td>18757.0</td>
<td>6771.0</td>
<td>8223.6</td>
</tr>
<tr>
<td>Sm</td>
<td>686.6</td>
<td>786.4</td>
<td>744.7</td>
<td>1073.0</td>
<td>193.7</td>
<td>157.2</td>
</tr>
<tr>
<td>Ir</td>
<td>2623.4</td>
<td>3657.7</td>
<td>4512.6</td>
<td>4101.8</td>
<td>1717.4</td>
<td>2227.3</td>
</tr>
<tr>
<td>Au</td>
<td>3617.6</td>
<td>2666.8</td>
<td>43321.2</td>
<td>44632.2</td>
<td>6127.2</td>
<td>5807.5</td>
</tr>
<tr>
<td>$N$</td>
<td>7</td>
<td>3</td>
<td>4</td>
<td>6</td>
<td>4</td>
<td>6</td>
</tr>
</tbody>
</table>

Last line indicates the number of elements, $N$, for which the RMS deviation is smaller for the potential indicated at the top of the column.

absorption effects can be different for an isolated atom and for a solid. Accounting for this effect distinctly modifies the DCSs for an isolated atom [28]. We may expect that the DCSs for atoms in the solid are also affected by electron absorption effects. At present, work is continued on this issue. Furthermore, in the present analysis, we neglected electron energy losses due to surface excitations. The influence of these excitations on the elastically backscattered intensity depends on the emission angle. Thus, the shape of the calculated emission-angle dependences of the elastic-backscattering probability may be modified when surface energy losses are accounted for. This modification is relatively weak for normal incidence of the primary beam [29]. Unfortunately, there is no universal theoretical tool providing the relevant correction. Werner et al. [30] proposed a simple procedure for determining the surface excitation correction; however its accuracy seems to be difficult to estimate. Finally, one should also remember that the measured elastic-backscattering probabilities are burdened with experimental errors, which contribute to the observed differences between theory and experiment in Figs. 5-14. Nevertheless, the agreement between computed and measured angular distributions of elastic-backscattered intensities is very reasonable. This agreement justifies the use of the elastic-backscattering probabilities for analytical applications, e.g., measurements of IMFPs [1].

### Acknowledgements

One of the authors (A.J.) would like to acknowledge partial support by the Foundation for Polish Science. The other author (J.Z.) acknowledges the support by the Institutional Research Plan No. AV0Z10100521 and by the Czech Science Foundation Project No. 202/06/0459.

### References

[1] C.J. Powell, A. Jablonski, J. Phys. Chem. Ref. Data 28 (1999) 19.
[2] G. Gergely, Prog. Surf. Sci. 71 (2002) 31.
[3] A. Jablonski, Prog. Surf. Sci. 74 (2003) 357.
[4] Annual Book of ASTM Standards 2004, vol. 03.06, Standard Terminology Relating to Surface Analysis, Standard E 673-03, ASTM International, West Conshohocken, Pennsylvania, 2004, p. 811.
[5] J.S. Schilling, M.B. Webb, Phys. Rev. B 2 (1970) 1665.

[6] A. Jablonski, J. Gryko, J. Kraaer, S. Tougaard, Phys. Rev. B 39 (1989) 61.

[7] A. Jablonski, Phys. Rev. B 43 (1991) 7546.

[8] A. Jablonski, H.S. Hansen, C. Jansson, S. Tougaard, Phys. Rev. B 45 (1992) 3694.

[9] W.S.M. Werner, I.S. Tilinin, M. Hayek, Phys. Rev. B 50 (1994) 4819.

[10] L.G. Glazov, S. Tougaard, Phys. Rev. B 68 (2003) 155409.

[11] L.G. Glazov, S. Tougaard, Phys. Rev. B 72 (2005) 085406.

[12] W.S.M. Werner, Phys. Rev. B 71 (2005) 115415.

[13] A. Jablonski, P. Jiricek, Surf. Sci. 412/413 (1998) 42.

[14] J. Zemek, P. Jiricek, W.S.M. Werner, B. Lesiak, A. Jablonski, Surf. Interf. Anal. 38 (2006) 615.

[15] Z. Czyzewski, D.O. MacCallum, A. Romig, D.C. Joy, J. Appl. Phys. 68 (1990) 3066.

[16] A. Jablonski, F. Salvat, Nucl. Instrum. Methods B, in press.

[17] P.J. Cumpson, M.P. Seah, Surf. Interf. Anal. 25 (1997) 430.

[18] F. Salvat, A. Jablonski, C.J. Powell, Comput. Phys. Commun. 165 (2005) 157.

[19] B. Hahn, D.G. Ravenhall, R. Hofstadter, Phys. Rev. 101 (1956) 1131.

[20] J.B. Furness, I.E. McCarthy, J. Phys. B: At. Mol. Phys. 6 (1973) 2280.

[21] W.B. Pearson, A Handbook of Lattice Spacing and Structures of Metals and Alloys, Pergamon Press, Oxford, 1967 (Chapter 2).

[22] S. Tanuma, C.J. Powell, D.R. Penn, Surf. Interf. Anal. 17 (1991) 911.

[23] S. Tanuma, C.J. Powell, D.R. Penn, Surf. Interf. Anal. 21 (1994) 165.

[24] C.J. Powell, A. Jablonski, NIST Electron Inelastic-Mean-Free-Path Database, Version 1.0, Standard Reference Data Program Database 71, US Department of Commerce, National Institute of Standards and Technology, Gaithersburg, MD, 1999.

[25] A. Jablonski, C.J. Powell, Surf. Sci. 463 (2000) 29.

[26] A. Jablonski, F. Salvat, C.J. Powell, J. Phys. Chem. Ref. Data 33 (2004) 409.

[27] A. Jablonski, F. Salvat, C.J. Powell, NIST Electron Elastic-Scattering Cross-Section Database, Version 3.1, Standard Reference Data Program Database 64, US Department of Commerce, National Institute of Standards and Technology, Gaithersburg, MD, 2003. Available from: <http://www.nist.gov/srd/nist64.htm>.

[28] A. Jablonski, F. Salvat, C.J. Powell, Surf. Interf. Anal. 37 (2005) 1115.

[29] A. Jablonski, K. Olejnik, J. Zemek, J. Electron Spectrosc. Relat. Phenom. 152 (2006) 100.

[30] W.S.M. Werner, W. Smekal, C. Tomastik, H. Stori, Surf. Sci. 486 (2001) L461.