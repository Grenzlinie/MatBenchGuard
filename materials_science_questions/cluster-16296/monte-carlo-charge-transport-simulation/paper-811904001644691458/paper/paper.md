# ELECTRICAL BREAKDOWN AND HIGH-ENERGY ELECTRON EMISSION UNDER DIELECTRIC CHARGING

V. S. Kortov and S. V. Zvonarev
UDC 539.216:621.315.592

A Monte-Carlo calculation model for electron transport in crystalline dielectrics charged by irradiation is improved with allowance for impact ionization and cascading processes. The electron transport in $SiO_2$ is simulated for high-strength electric fields. It is found that a breakdown in a dielectric can occur in the electric field strength range 11.5-12.5 MV/cm.

## INTRODUCTION

Irradiation of dielectrics is known to cause their charging. In so doing, an electric field formed in the dielectric pulls electrons to the surface which, as a rule, is positively charged. The electron transport in a high-strength field can cause an electrical breakdown and failure of dielectrics.

The physical processes and mechanisms of electrical breakdown in dielectrics are well studied. First models taking into account electron interaction with optical phonons alone were developed in the middle of XX century [1, 2]. Later, these models were modified with allowance for electron scattering by acoustic phonons, intervalley scattering, and impact ionization [3, 4]. At high field strengths, electrons involved in the impact ionization process begin to cascade generating an electron avalanche causing in turn an electrical breakdown in dielectric materials.

The action of high-energy radiant fluxes causing intense dielectric charging is of frequent occurrence in modern equipment. Therefore, studying the properties of dielectrics in electric fields with the strengths close to the breakdown ones is of great scientific and practical importance. This work is aimed at simulation of electron transport processes in charged dielectrics exposed to high-strength electric fields and determination of breakdown electric field strengths by an example of crystalline $SiO_2$.

## THE MONTE-CARLO SIMULATION OF ELECTRON TRANSPORT

In the model of electron transport in crystalline dielectrics charged by irradiation [5], an allowance was made of the electron interaction with optical and acoustic phonons alone. To study charge transport processes in high-strength electric fields, impact ionization and cascading processes should be taken into account. Let us consider these processes in detail.

### Electron scattering by longitudinal optical phonons

The electrons delocalized from the traps due to tunneling or ionization move to the dielectric surface, interacting with phonons. At electron energies from fractions up to several electron-volts, the electron transport is affected only by scattering by longitudinal optical phonons. The scattering rate of an electron with the energy E by optical phonons is calculated using the Fröhlich theory [6] as follows:

Ural State Technical University, Ekaterinburg, Russia, e-mail: v.kortov@mail.ustu.ru. Translated from Izvestiya Vysshikh Uchebnykh Zavedenii, Fizika, No. 3, pp. 52-58, March, 2008. Original article submitted June 25, 2007.

1064-8887/08/5103-0277 ©2008 Springer Science+Business Media, Inc.

$$
f_{\mathrm{LO}}^{ \pm}=\frac{e^{2}}{4 \pi \varepsilon_{0} \hbar^{2}}\left(n_{\mathrm{LO}}+\frac{1}{2} \pm \frac{1}{2}\right) \sqrt{\frac{m^{*}}{2 E}}\left(\frac{1}{\varepsilon_{\infty}}-\frac{1}{\varepsilon}\right) \hbar \omega_{\mathrm{LO}} \cdot \ln \frac{1+\sqrt{1 \mp \hbar \omega_{\mathrm{LO}} / E}}{ \pm 1 \mp \sqrt{1 \mp \hbar \omega_{\mathrm{LO}} / E}}. \tag{1}
$$

Here the (+) sign corresponds to generation, and the (-) sign corresponds to phonon annihilation; the parameters $e$ and $m^{*}$ are the electron charge and effective mass, respectively, $\hbar \omega_{\mathrm{LO}}$ is the optical-phonon oscillation energy, $\varepsilon_{0}$, $\varepsilon$, and $\varepsilon_{\infty}$ are the absolute, static, and high-frequency permittivities, respectively, and $n_{\mathrm{LO}}$ is the Bose-Einstein distribution.

## Acoustic phonon scattering

At the electron energies from units up to ten electron-volts, electron scattering by acoustic phonons begins to prevail. The rate of electron scattering by acoustic phonons is determined depending on the electron energy $E_{\mathrm{BZ}}$ at the Brillouin zone edge [3] as

$$
f_{\mathrm{ac}}^{ \pm} \approx \frac{3\left(m^{*}\right)^{3 / 2} C_{1}^{2} k_{\mathrm{B}} T}{\sqrt{2} \pi \rho C_{\mathrm{s}}^{2} \hbar^{4}} \sqrt{E} \text { for } E<E_{\mathrm{BZ}} / 2, \tag{2}
$$

$$
f_{\mathrm{ac}}^{ \pm}=\frac{8 \pi^{3} \hbar^{2} N^{2} \sigma}{m^{*} M \omega_{\mathrm{BZ}}}\left(\frac{E}{E_{\mathrm{BZ}}}\right)^{3 / 2}\left(n_{\mathrm{BZ}}+\frac{1}{2} \pm \frac{1}{2}\right) \text { for } E \geq E_{\mathrm{BZ}} / 2. \tag{2a}
$$

In formulas (2) and (2a), the parameter $C_{1}=S_{q} / q$ is the deformation potential constant, $T$ is the temperature, $\rho$ is the dielectric density, $C_{\mathrm{s}}$ is the speed of sound in the dielectric determined with allowance for three branches (two longitudinal and one transverse branches) of the acoustic phonon spectrum, $\sigma$ is the cross section, $M$ is the mass of the heaviest atom in a unit cell, $n_{\mathrm{BZ}}$ is the Bose-Einstein distribution at $\omega_{\mathrm{BZ}}=C_{S} q_{\mathrm{BZ}}$, and $N$ is the lattice atom concentration calculated using a relation from [3] as follows:

$$
\left|S_{q}\right|^{2}=\frac{\pi \hbar^{4} N^{2} q^{2}}{m^{*^{2}}} \sigma, \tag{3}
$$

where $S_{q}$ is the interaction constant and $q$ is the phonon wave vector.

## Calculation of electron energy and trajectories

The trajectories were calculated using the Monte-Carlo technique by simulating 10000 histories. The electron-phonon interaction mode was determined by random number generation in the range from 0 to 1. Depending on the determined random number, interaction with the phonon formation, phonon annihilation, or without interaction with a phonon was chosen. In our simulation, we assumed that each of the three interaction modes is equally probable. To calculate the parameters of the angle electron distribution after each electron-phonon interaction, use was made of the Monte-Carlo method.

The electron energy changes after each electron-phonon interaction due to scattering by phonons and acceleration in the electric field as follows:

$$
E_{j}=E_{j-1}+l_{j} F \cos \theta_{j} \pm \hbar \omega, \tag{4}
$$

![](./images/811904001644691458_1.jpg)

Fig. 1. Variation of electron scattering rates in SiO₂ for different interaction processes: with optical phonons (LO⁺ and LO⁻ correspond to phonon formation and annihilation, respectively), with acoustic phonons (ac⁺ and ac⁻ correspond to phonon formation and annihilation, respectively), and under impact ionization (ii).

where $F$ is the electric field strength, $l_j$ is the mean free path, and $\theta_j$ is the scattering angle. In so doing, phonon annihilation and generation result in an increase and a decrease in the electron energy, respectively. In the absence of electron-phonon interaction, the electron energy depends only on the electric field strength.

### Impact ionization

Electrons moving to the surface acquire energy due to electron-phonon interaction and acceleration in the electric field. As a result, the electron energy can reach the ionization energy $E_{\text{th}}$ determined from the following relation adopted in [7]:

$$
E_{\text{th}} = \frac{2 + m_{VB}^{*} / m_{CB}^{*}}{1 + m_{VB}^{*} / m_{CB}^{*}} E_{g}. \tag{5}
$$

The effective masses of valence band holes $m_{VB}^{*}$ and conductivity band electrons $m_{CB}^{*}$ depend on the electron rest mass $m_0$, as $m_{VB}^{*}=10m_0$ and $m_{CB}^{*}=m_0$, respectively. $E_g$ is the band gap energy.

The electrons, whose energy becomes equal to ionization energy, are involved in impact ionization. In this case, the electron scattering rate can be written as [7]

$$
f_{\text{ii}} = C_{\text{ii}} \left[ \frac{(E / E_{\text{th}} - 1)}{1 + D_{\text{ii}} E^{2} / E_{\text{th}}} \ln\left( \frac{E}{E_{\text{th}}} \right) \right]^{\alpha} \text{ at } E > E_{\text{th}}, \tag{6}
$$

where $C_{\text{ii}}$ is the impact ionization coefficient, $D_{\text{ii}}$ is the impact screening parameter, and $\alpha$ is a constant.

The electron scattering rates for phonon scattering and impact ionization (Fig. 1) are calculated using Eqs. (1)–(3) and (5)–(6) for crystalline SiO₂. It is seen from Fig. 1 that in the low-energy range, the electron scattering by longitudinal optical phonons prevails. In so doing, in the energy range 0–0.07 eV, the rate of electron scattering accompanied by phonon formation LO⁺ is zero, which testifies to the fact that there is no phonon generation. In the energy range 0.07–2.75 eV, the rate of electron scattering accompanied by phonon formation LO⁺ exceeds that

![](./images/811904001644691458_2.jpg)

Fig. 2. The mean free path $l$ versus electron energy in SiO₂ for the processes of scattering by optical phonons (LO), acoustic phonons (ac), and impact ionization (ii).

accompanied by phonon annihilation LO⁻. As a result, in this energy range, electrons lose their energy with higher probability, that is, thermalization of electrons takes place. At energies higher than 2.75 eV, scattering by acoustic phonons becomes more significant. The impact ionization process starts at the electron energies higher than 10 eV.

### Cascading

The drifting electrons involved in impact ionization can form new electrons due to cascading processes. In so doing, the probability of secondary electron formation depends on the electron drift length $z$ and on the electric field strength $F$ [8], and we have

$$
\omega_{A}(z, F)=\exp [\alpha(f) z]=\exp \left[\alpha_{0} \exp \left(-\frac{H}{F}\right) z\right],
\tag{7}
$$

where $\alpha_{0}$ and $H$ are the material dependent constants. For SiO₂, $\alpha_{0}=6.5 \cdot 10^{11} \mathrm{~1/cm}$ and $H=1.8 \cdot 10^{8} \mathrm{~V/cm}$ [8].

The electron drift length can be determined as a projection onto the normal to surface, taking into account the mean free path $l$ after each electron-phonon or electron-electron interaction and a scattering angle. In so doing, the distance covered by an electron between the interactions can be calculated using the following formula:

$$
l=\sqrt{\frac{2 E}{m^{*}}} \Delta t,
\tag{8}
$$

where $\Delta t$ is the time interval between the interactions.

The initial energy of a generated electron is determined by the energy losses of a primary electron under impact ionization. Minimal electron energy losses necessary for generation of the second electron under impact ionization depend on the SiO₂ energy gap width $E_{\text{min}}=E_{g}=9$ eV. The generated secondary electrons gaining sufficiently high initial energy can generate the so-called tertiary electrons under further acceleration in the electric field. As a result, avalanche electron generation takes place. The electron cascading process is time limited and lasts about $10^{-14}$ s [9].

Both the energy and direction of motion of electrons moving to the surface change after each electron-phonon or electron-electron interaction. The distance covered by an electron in a crystal can be calculated as a projection of the mean free path onto the surface normal. Our calculations of the electron mean free path for crystalline SiO₂ are presented in Fig. 2 for different scattering mechanisms. In the electron energy range 0.01–0.1 eV, the mean free path $l$ linearly increases in the case of scattering by optical phonons LO followed by an abrupt decrease of $l$ which can be

attributed to a sharp increase in the scattering rate accompanied by phonon formation at electron energies higher than 0.07 eV (see Fig. 1). The mean free path of electrons with energies higher than 0.1 eV increases almost linearly. This is due to the fact that the time between the electron-phonon interactions increases due to a decrease in the scattering rate causing the electrons to cover longer distances. This situation is in direct opposition to the case of acoustic phonons where the mean free path is constant in the low-energy range, and then it gradually decreases. This occurs in the energy range where the scattering rate begins to gradually increase. The dependence of the distance covered by electrons between the interactions on the electron energy is parabolic in the case of impact ionization. In so doing, the mean free path is drastically decreased and then (at nearly 100 eV) it gradually increases.

## Electron emission into vacuum
An electron can emit reaching the surface, if the electron energy is higher than the electron affinity $\chi$ with allowance for the scattering angle $\theta$

$$
E>\frac{\chi}{\cos ^{2} \theta}. \tag{9}
$$

In so doing, the emission energy can be determined using the following formula:

$$
E=E_{i}-\chi, \tag{10}
$$

where $E_{i}$ is the electron energy after the last interaction.

## RESULTS OF SIMULATION AND DISCUSSION
The electric field strength and energy distribution of emitted electrons under electron transport in a charged dielectric were calculated for the dielectric charged by electron bombardment with energies of 1–10 keV. In this case, a plus – minus injected charge structure is formed in the surface layers of the dielectrics [10]. The dielectric surface is charged positively, while a negative charge occurs in the near-surface layer at the depth up to 100 nm due to capture of electrons by traps. Simultaneously, a strong electric field with the strength up to several MV/cm is generated in the dielectric [10]. As noted above, the electrons captured by traps are delocalized due to tunneling in the electric field or thermal ionization and move in the electric charge field towards the surface.

For simulation of the electron transport process in crystalline $SiO_{2}$, we used the following parameters: $\hbar \omega_{LO}=$ 0.063 eV, $\varepsilon=3.84$, $\varepsilon_{\infty}=2.25$ [7], $C_{1}=3.5$ eV, $\sigma=3.5 \cdot 10^{-15} \mathrm{cm}^{2}$ [3], $\rho=2.65 \mathrm{~g} / \mathrm{cm}^{3}$, $C_{\mathrm{s}}=4030 \mathrm{~m} / \mathrm{s}$ [11], $C_{\mathrm{ii}}=$ $1.26 \cdot 10^{15} 1 / \mathrm{s}$, $D_{\mathrm{ii}}=0.01$, $\alpha=0.45$ [7], $M=46.6 \cdot 10^{-27} \mathrm{~kg}$, $T=300 \mathrm{~K}$, and $\chi=0.3$ eV.

Figure 3 shows the calculated dependence of the number of emitted electrons on the electric field strength for two electron localization depths 20 and 100 nm. At these depths, the highest charge density is formed at the bombarding electron energies 1 and 10 keV, respectively [10]. It is seen that an increase in the electric field strength in the range 0–3 MV/cm results in a significant increase in the number $n$ of electrons emitted from the crystal ($N$ is the number of delocalized electrons). An increase in the electron energy due to acceleration in the electric field acceleration cannot be compensated by the energy losses under electron-phonon interactions. As a result, a larger part of electrons is emitted into vacuum. In the field strength range 3–10 MV/cm, the electron emission is stabilized and is almost 100 %. In this range, the average electron energy amounts to several tens of electron-volts, however, no cascading is caused by impact ionization. Therefore, a wide plateau appears in the dependence curve (Fig. 3). At the electric field strength 10 MV/cm, the electrons are involved in a cascading process, resulting in a gradual increase in the number of emitted electrons. At the electric field strengths 11.5–12.5 10 MV/cm, an avalanche increase of the number of emitted electrons occurs causing a breakdown. This dependence also shows the effect of the electron localization depth on the beginning of

<table>
<caption>TABLE I. Electric Field Strengths for Breakdown in SiO₂</caption>
<thead>
<tr>
<th>$F$ of breakdown,
MV/cm</th>
<th>Calculation or experiment</th>
<th>Material</th>
<th>Reference</th>
</tr>
</thead>
<tbody>
<tr>
<td>2–4</td>
<td>Calculation with allowance for optical phonon scattering</td>
<td>quartz</td>
<td>[2,12]</td>
</tr>
<tr>
<td>7.4</td>
<td>Calculation with allowance for optical phonon scattering</td>
<td>quartz</td>
<td>[1]</td>
</tr>
<tr>
<td>8–10</td>
<td>Experiment</td>
<td>amorphous SiO₂
films</td>
<td>[13]</td>
</tr>
<tr>
<td>7–10</td>
<td>Calculation with allowance for optical phonon scattering</td>
<td>quartz</td>
<td>[14]</td>
</tr>
<tr>
<td>15–18</td>
<td>Experiment</td>
<td>thin SiO₂ films</td>
<td>[15]</td>
</tr>
<tr>
<td>12–16</td>
<td>Experiment</td>
<td>thin SiO₂ films</td>
<td>[16]</td>
</tr>
<tr>
<td>10–15</td>
<td>Calculation with allowance for optical and acoustic phonon
scattering and impact ionization</td>
<td>thin SiO₂ films</td>
<td>[17]</td>
</tr>
<tr>
<td>11.5–12.5</td>
<td>Calculation with allowance for optical and acoustic phonon
scattering, impact ionization, and cascading</td>
<td>crystalline SiO₂</td>
<td>present work</td>
</tr>
</tbody>
</table>

![](./images/811904001644691458_3.jpg)

Fig. 3. The number of emitted electrons vs. electric field strength
in crystalline SiO₂ for different electron localization depths $x$.

cascading. For larger localization depths, the process of avalanche electron generation begins at lower electric field strengths, since the probability of electron generation is proportional to the electron drift length.

The electric field strengths for breakdown in SiO₂ are listed in Table 1. Our results are in good agreement with the literature data.

The electron energy distribution is calculated for the localization depth $x = 50$ nm and different electric field strengths. At low electric field strengths (see Fig 4a), the electron scattering by optical and acoustic phonons become dominant, which allows compensation for the electron energy increase due to acceleration in the electric field. As the electric field strength increases up to 2.3 MV/cm, a part of electrons accelerates up to the ionization energy and begins to interact with other electrons causing the second peak in the energy distribution curve. This is due to the fact that the electrons cannot yet cascade at this strength, and their energy depends on the electric field alone. On further increase in the electric field strength, a larger part of electrons accelerates up to the ionization energy resulting in the disappearance of low-energy peak and a shift of high-energy peak to higher energies. At the field strength 10 MV/cm, the cascading process begins to form a 15–25 eV peak in the energy spectrum (Fig. 4b), whose intensity increases with increase in the electric field strength.

We calculated the dependence of the average energy of electrons emitted into vacuum from SiO₂ on the electric field strength for different electron delocalization depths (Fig. 5). The average electron energy is only slightly increased in the range of field strengths 0–3 MV/cm. In the range 3–10 MV/cm, the electron transport occurs under the conditions

![](./images/811904001644691458_4.jpg)

Fig. 4. Energy distribution of electrons emitted from SiO₂ at different electric field strengths: 1 MV/cm (a) and 10 MV/cm (b).

![](./images/811904001644691458_5.jpg)

Fig. 5. The average energy of electrons emitted into vacuum vs. electric field strength for different electron delocalization depths.

of increasing electron-electron interaction. Yet, the electrons cannot cascade at this electric field strength, therefore the average energy of emitted electrons gradually increases. At the field strengths higher than 10 MV/cm, the rate of increase in the average electron energy slows down due to the fact that the electrons begin to cascade. The generated electrons cannot accelerate up to significant values due to a short distance to the crystal edge and limited cascading time (10 fs). Therefore cascading preceding a breakdown is accompanied by an abrupt decrease in the average energies of electrons emitted from the crystal.

## CONCLUSION

A physical model for electron transport in crystalline dielectrics was refined with allowance for charge transfer both in the low- and high-energy ranges of electron energies. For the first time, the cascading processes are taken into account in the electron transport processes in strong electric fields. The electron transport in high-strength electric fields is simulated for silicon dioxide. It is found that a breakdown in this dielectric can occur in the range of electric field strengths 11.5–12.5 MV/cm, depending on the electron drift length. Good agreement between the calculated field strengths and literature data prove the adequacy of the physical model to real processes, which makes it possible to use this model for calculating electric strengths for other dielectrics. The energy spectra of the emitted electrons obtained

for different electric field strengths correspond to physical processes in the crystal. An abrupt change in the energy of emitted electrons at the pre-breakdown phase can serve as an indicator of possible failure of dielectrics.

## REFERENCES
1.  H. Fröhlich, Phys. Rev., **56**, 349 (1939).
2.  H. B. Callen, Phys. Rev., **76**, No. 9, 1394 (1949).
3.  M. V. Fischetti, D. J. DiMaria, S. D. Brorson, *et al.*, Phys. Rev. B, **31**, No. 12, 8124 (1985).
4.  W. Porod and D. K. Ferry, Phys. Rev. Lett., **54**, No. 11, 1189 (1985).
5.  S. V. Zvonarev and V. S. Kortov, Proc. Int. Sci. Pract. Conf., Snezhinsk (2006).
6.  J. Llacer and E. L. Garwin, J. Appl. Phys., **40**, No. 7, 2766 (1969).
7.  E. Schreiber and H. -J. Fitting, J. Electr. Spectr. Rel. Phenom., **124**, 25 (2002).
8.  P. Solomon and N. Klein, Solid State Commun., **17**, 1397 (1975).
9.  H. -J. Fitting, V. S. Kortov, and G. Petite, J. Lumin., **122–123**, 542 (2007).
10. H. -J. Fitting, E. Schreiber, and I. A. Glavatskikh, Microsc. Microanal., **10**, 764–770 (2004).
11. A. I. Nazarov and V. V. Sergeev, Zh. Tekh. Fiz., **67**, No. 6, 127 (1997).
12. K. K. Thornber and R. P. Feynman, Phys. Rev. B, **1**, 4099 (1970).
13. N. J. Chou and J. M. Eldridge, J. Electrochem. Soc., **117**, 1287 (1970).
14. W. T. Lynch, J. Appl. Phys., **43**, No. 8, 3274 (1972).
15. S. Simon and Cohen, J. Electrochem. Soc., **130**, 929 (1983).
16. D. J. DiMaria, T. N. Theis, J. R. Kirtley, *et al.*, J. Appl. Phys., **57**, No. 4, 1214 (1985).
17. D. Arnold, E. Cartier, and D. J. DiMaria, Phys. Rev. B, **49**, No. 15, 10278 (1994).