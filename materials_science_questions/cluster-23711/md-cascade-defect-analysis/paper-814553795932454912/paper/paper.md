OPEN
# Ab initio molecular dynamics simulation of the effects of stacking faults on the radiation response of 3C-SiC

M. Jiang¹, S. M. Peng², H. B. Zhang², C. H. Xu², H. Y. Xiao¹, F. A. Zhao¹, Z. J. Liu³ & X. T. Zu¹⁴

Received: 29 October 2015
Accepted: 11 January 2016
Published: 16 February 2016

In this study, an *ab initio* molecular dynamics method is employed to investigate how the existence of stacking faults (SFs) influences the response of SiC to low energy irradiation. It reveals that the C and Si atoms around the SFs are generally more difficult to be displaced than those in unfaulted SiC, and the corresponding threshold displacement energies for them are generally larger, indicative of enhanced radiation tolerance caused by the introduction of SFs, which agrees well with the recent experiment. As compared with the unfaulted state, more localized point defects are generated in faulted SiC. Also, the efficiency of damage production for Si recoils is generally higher than that of C recoils. The calculated potential energy increases for defect generation in SiC with intrinsic and extrinsic SFs are found to be higher than those in unfaulted SiC, due to the stronger screen-Coulomb interaction between the PKA and its neighbors. The presented results provide a fundamental insight into the underlying mechanism of displacement events in faulted SiC and will help to advance the understanding of the radiation response of SiC with and without SFs.

Cubic silicon carbide (3C-SiC) exhibits lots of superior electronic and physical properties such as high electron mobility, saturated electron drift velocity, high corrosion resistance, favorable chemical inertness and small neutron absorption cross-section¹⁻⁵. It is thus desirable for power switching device applications and is often utilized under harsh environment such as high temperature and high pressure. Due to the superior physical properties of 3C-SiC, it has been considered as a vital component in nuclear applications. For example, 3C-SiC has been considered as an inert-matrix material for water-cooled reactors to burn minor actinides or Pu⁴, a structural material for fusion power reactors⁶, a cladding material for nuclear fuel, and a structural material for the reactor core in high temperature gas-cooled reactors⁷. It is therefore of critical importance to understand the phase stability of 3C-SiC under irradiation and explore the way to enhance its radiation tolerance.

In the past decades, a great number of experimental and theoretical studies have been carried out to investigate the radiation damage effects of SiC⁸⁻¹². Inui *et al.* have found that crystalline-to-amorphous transition in single crystalline silicon carbide (sc-SiC) can be induced by electron irradiation at temperatures around 300 K¹³,¹⁴. Several ion irradiation studies on nano-crystalline silicon carbide (nc-SiC) have also been reported and it has been suggested that reducing the grain size may improve the mechanical properties of sc-SiC¹⁵,¹⁶. Recently, Zhang *et al.* compared the radiation tolerance of sc-SiC and nc-SiC by employing 550 keV Si⁺ ion irradiation, who found that the sc-SiC readily undergoes irradiation-induced structural amorphization, whereas the nc-SiC with a high-density of stacking faults (SFs) exhibits more than an order of magnitude increase in radiation resistance¹⁷. Jamison *et al.* studied the crystalline-to-amorphous transition in nc-SiC using 1.25 MeV electron irradiation, and found that the nc-SiC has an increased dose to amorphization, as compared with the sc-SiC. They proposed that the addition of a high density of grain boundaries, grain texture, and the presence of SFs may all contribute to the enhanced radiation tolerance¹⁸. Theoretically, the density functional theory (DFT) method has been employed

¹School of Physical Electronics, University of Electronic Science and Technology of China, Chengdu 610054, China.
²Institute of Nuclear Physics and Chemistry, Chinese Academy of Engineering Physics, Mianyang 621900, China.
³Department of Physics, Lanzhou City University, Lanzhou 730070, China. ⁴Institute of Fundamental and Frontier Sciences, University of Electronic Science and Technology of China, Chengdu 610054, China. Correspondence and requests for materials should be addressed to H.Y.X. (email: hyxiao@uestc.edu.cn) or Z.J.L. (email: liuzj2000@126.com)

<table>
  <thead>
    <tr>
      <th></th>
      <th>Lattice constant (Å)</th>
      <th>Cohesive energy (eV/atom)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Our calc.</td>
      <td>4.37</td>
      <td>6.40</td>
    </tr>
    <tr>
      <td>Other calc.</td>
      <td>4.36¹, 4.45ᵇ</td>
      <td>6.66ᵃ</td>
    </tr>
    <tr>
      <td>Exp.</td>
      <td>4.36ᵃ</td>
      <td>6.34ᵃ</td>
    </tr>
  </tbody>
</table>

Table 1. Calculated lattice constant and cohesive energy for bulk SiC. ᵃref. 27. ᵇref. 26.

to study the fundamental properties of SiC containing intrinsic stacking faults (ISFs) and (or) extrinsic stacking faults (ESFs). Umeno et al. have investigated the SF formation energy and the stress-strain relationship induced by the SF formation¹⁹. Oda et al. have studied the formation energy and electronic structure of SiC with ISFs²⁰. Jamison et al. have investigated how the SFs influence the dose to amorphization in SiC and found that the energy barriers for Si interstitial migration and the rate-limiting defect recovery reaction are reduced by the existence of SFs¹⁸. In spite of these extensive studies, the dynamic processes for defect generation in SF-contained SiC at an atomic level have not been revealed yet. Besides, the origin of the enhanced radiation tolerance caused by the SF formation needs to be further explored.

In recent years, the ab initio molecular dynamics (AIMD) method, in which the interatomic potential is obtained by electronic structure calculations rather than empirical fitting, has been demonstrated to be a powerful tool in simulating the displacement events in ceramic materials²¹⁻²⁵. It has been revealed that physical parameters like threshold displacement energy can be determined with ab initio accuracy, and new mechanism for defect generation and new defective states that are different from classical molecular dynamics (MD) can be predicted. In particular, the role of charge transfer during the dynamic process of recoil events can be elucidated. In this study, the AIMD method is employed to study the low-energy recoil events of 3 C-SiC with SFs. Our main aims are (1) to investigate the defect generation mechanism and defect distribution in SiC with SFs; (2) to compare the response of unfaulted and faulted SiC to low energy radiation; and (3) to explore the origin of the difference in the radiation susceptibility between SF-contained SiC and the unfaulted state.

## Results and Discussion
### Ground-state properties for bulk SiC and stacking fault formation energy.
To test the pseudopotentials of Si and C, the lattice constant and cohesive energy for bulk SiC are first calculated and compared with experimental and other theoretical values in Table 1. It is shown that our results are in excellent agreement with experiments and are comparable with other theoretical values²⁶²⁷. The defect formation energy, which is defined by $E_{f}=E_{def}-E_{undef}+\sum_{i}\Delta n_{i}\mu_{i}$¹⁸, is calculated for ISFs and ESFs. Here, $E_{def}$ is the energy of the faulted supercell, $E_{undef}$ is the energy of the unfaulted supercell, $\Delta n_{i}$ is the change in the number of species $i$ ($i =$ Si or C) and $\mu_{i}$ is the chemical potential of species $i$. The chemical potentials of silicon ($\mu_{Si}$) and carbon ($\mu_{c}$) obey the following criteria: $\mu_{si}\leq\mu_{si}$(bulk), $\mu_{c}\leq\mu_{c}$(bulk) and $\mu_{si}+\mu_{c}=\mu_{sic}$(bulk), where $\mu_{si}$(bulk) and $\mu_{c}$(bulk) are the chemical potentials of bulk Si and diamond, respectively, and $\mu_{sic}$(bulk) is the total energy of bulk SiC²⁸. The SF formation energies are calculated under both carbon-rich ($\mu_{c}=\mu_{c}$(bulk) and $\mu_{si}=\mu_{si}$(bulk) $-\mu_{c}$(bulk)) condition and silicon-rich ($\mu_{si}=\mu_{si}$(bulk) and $\mu_{c}=\mu_{sic}$(bulk) $-\mu_{si}$(bulk)) condition. For the three types of ISFs, the calculated formation energies under both conditions are found to be nearly identical to each other, i.e., $\sim -7.8$ mJ/m², which agrees well with the value of $-3.4$ mJ/m² reported by Käckell et al.²⁹. Umeno et al. have determined the formation energy to be 9.82 mJ/m² for a single-layer ISF by DFT method¹⁹, which differs greatly from our calculations. Such discrepancy mainly results from the differences in the size of the supercell. In our calculations the supercell for SiC with ISFs consists of 256 atoms, while the supercell employed by Umeno et al. consists of only 10 atoms¹⁹. Similarly, the three types of ESFs exhibit very similar stability. The SF formation energy is calculated to be $\sim 1.7$ mJ/m², which differs a lot from the value of $-28$ mJ/m² reported by Käckell et al.²⁹ This may be due to the differences in the employed exchange-correlation potentials. Käckell et al. carried out the calculations within the framework of local-density approximation, while our calculations are performed by the generalized gradient approximation. Comparing with the experimental value of 2.5 mJ/m² ³⁰, we find that our calculated value of $\sim 1.7$ mJ/m² is in good agreement with experiments.

### Threshold displacement energies for C and Si recoils in unfaulted and faulted SiC.
The critical physical parameter for estimating damage production rates under electron, neutron, and ion irradiation and predicting the defect profile is the threshold displacement energy ($E_{d}$), which can be defined as the minimum transferred kinetic energy for the primary knock-on atom (PKA) to be permanently displaced from its lattice site and form stable defects¹². In the past several years, the $E_{d}$ values in a number of semiconductors and ceramic materials have been investigated employing the AIMD method²³⁻²⁵. In order to explore how the existence of SFs affects the radiation response of SiC, we first calculate the $E_{d}$s for C and Si recoils in unfaulted SiC along the [001] and [00$\overline{1}$] directions, which are perpendicular to the SiC(111) plane and correspond to the [111] and [$\overline{1}\overline{1}\overline{1}$] directions in bulk SiC, respectively. A comparison of our results with other theoretical values is provided in Table 2. The $E_{d}$s for C[001] and C[00$\overline{1}$] are determined to be 19 and 47.5 eV, respectively. For Si recoils, the $E_{d}$ values are calculated to be 95 eV for the [001] direction and 63 eV for the [00$\overline{1}$] direction. It is shown that our results are in good agreement with the results reported by Gao et al.¹². Comparing our results with the classical MD simulation carried out by Devanathan and Weber³¹, we find that the $E_{d}$s obtained by the AIMD method are generally much smaller, except for the case of Si[00$\overline{1}$]. This may be due to the fact that charge transfer that occurs during the recoil events is taken into account by the AIMD method while not considered in the classical MD simulations³².

<table>
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th>Ed (eV)</th>
      <th>Defect type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>C[001]</td>
      <td>Our Calc.</td>
      <td>19</td>
      <td>C<sub>vac</sub> + C<sub>int</sub></td>
    </tr>
    <tr>
      <td></td>
      <td>Other MD</td>
      <td>20.5ª, 30.0ᵇ</td>
      <td>C<sub>vac</sub> + C<sub>int</sub></td>
    </tr>
    <tr>
      <td>C[00ī]</td>
      <td>Our Calc.</td>
      <td>47.5</td>
      <td>C<sub>vac</sub> + C<sub>int</sub></td>
    </tr>
    <tr>
      <td></td>
      <td>Other MD</td>
      <td>47.5ª, 71.0ᵇ</td>
      <td>C<sub>vac</sub> + C<sub>int</sub></td>
    </tr>
    <tr>
      <td>Si[001]</td>
      <td>Our Calc.</td>
      <td>95</td>
      <td>2Si<sub>C</sub> + 2C<sub>Si</sub> + C<sub>vac</sub> + C<sub>int</sub></td>
    </tr>
    <tr>
      <td></td>
      <td>Other MD</td>
      <td>105ª, 108.0ᵇ</td>
      <td>Si<sub>vac</sub> + Si<sub>int</sub></td>
    </tr>
    <tr>
      <td>Si[00ī]</td>
      <td>Our Calc.</td>
      <td>63</td>
      <td>Si<sub>vac</sub> + Si<sub>int</sub></td>
    </tr>
    <tr>
      <td></td>
      <td>Other MD</td>
      <td>62ª, 38.0ᵇ</td>
      <td>Si<sub>vac</sub> + Si<sub>int</sub></td>
    </tr>
  </tbody>
</table>

Table 2. Calculated threshold displacement energies (E<sub>d</sub>s) and the associated defect types for C and Si recoil events along the direction normal to the SiC(111) surface. C<sub>vac</sub>: C vacancy; C<sub>int</sub>: C interstitial; Si<sub>vac</sub>: Si vacancy; Si<sub>int</sub>: Si interstitial; C<sub>Si</sub>: C occupying the lattice Si site; Si<sub>C</sub>: Si occupying the lattice C site. ªref. 12. ᵇref. 31.

![](./images/814553795932454912_1.jpg)

Figure 1. Illustration of schematic view of SiC containing intrinsic SFs with (a) (ABC)(AC)(ABC); (b) (ABC)(AB)(ABC); (c) (ABC)(BC)(ABC) stacking sequences.

The calculated E<sub>d</sub>s for C and Si PKAs in SiC with ISFs and ESFs (see Figs 1 and 2) are summarized in Table 3. As for C recoils around the ISFs, it is found that along both the [001] and [00ī] directions the E<sub>d</sub> values for C₃ PKAs are generally larger than those for C₁ and C₂ PKAs. In the case of C recoils around the ESFs, the E<sub>d</sub> values for C₁ PKAs are the highest for both [001] and [00ī] directions. Obviously, the three types of C PKAs that have different interlayer spacing from the SFs exhibit different tolerance to irradiation. Similar phenomenon is also observed for Si recoils, for which the E<sub>d</sub>s in several cases are larger than 150 eV, i.e., the PKA is not permanently displaced at energy up to 150 eV. It is found that the three types of Si recoils around the SFs are affected remarkably and exhibit different E<sub>d</sub> values. Comparing the E<sub>d</sub>s for C and Si PKAs, we find that generally considerably higher energies are needed for displacing the Si PKAs than those for displacing the C PKAs, similar to the cases in bulk SiC¹². These results show that the radiation susceptibility of the C and Si atoms around the SFs is affected significantly by the existence of SFs.

In this study, the weighted average E<sub>d</sub> values are calculated to be 52.1 eV for C[001], 59.5 eV for C[00ī], >99.6 eV for Si[001] and >122.1 eV for Si[00ī] in SiC containing ISFs. As for the PKAs in SiC with ESFs, the average E<sub>d</sub> values are calculated to be 37.8, 71.6, >128.4 and >88.1 eV for C[001], C[00ī], Si[001] and Si[00ī], respectively. Comparing these results with the values of 19, 47.5, 95 and 63 eV for C[001], C[00ī], Si[001]and Si[00ī] in unfaulted SiC, respectively, we find that the E<sub>d</sub> values in faulted SiC are generally larger. The maximum energy transferred to an atom can be expressed as $T = 2E_e(E_e + 2m_ec^2)/Mc^2$ under electron irradiation, where

![](./images/814553795932454912_2.jpg)

Figure 2. Illustration of schematic view of SiC containing extrinsic SFs with (a) (ABC)(BABC)(ABC); (b) (ABC)(ACBC)(ABC); (c) (ABC)(ABAC)(ABC) stacking sequences.

<table>
  <thead>
    <tr>
      <th rowspan="2"></th>
      <th rowspan="2">Stacking sequence</th>
      <th rowspan="2">Direction</th>
      <th colspan="6">E<sub>d</sub>(eV)</th>
    </tr>
    <tr>
      <th>C<sub>1</sub></th>
      <th>C<sub>2</sub></th>
      <th>C<sub>3</sub></th>
      <th>Si<sub>1</sub></th>
      <th>Si<sub>2</sub></th>
      <th>Si<sub>3</sub></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="6">ISFs</td>
      <td rowspan="2">(ABC)(AC)(ABC)</td>
      <td>[001]</td>
      <td>64</td>
      <td>40</td>
      <td><b>68.5</b></td>
      <td>69</td>
      <td><b>131</b></td>
      <td>80.5</td>
    </tr>
    <tr>
      <td>[00<span class="overline">1</span>]</td>
      <td>57</td>
      <td>58</td>
      <td><b>63</b></td>
      <td>&gt;150</td>
      <td>65</td>
      <td>&gt;150</td>
    </tr>
    <tr>
      <td rowspan="2">(ABC)(AB)(ABC)</td>
      <td>[001]</td>
      <td>64</td>
      <td>19.5</td>
      <td><b>67</b></td>
      <td>68.5</td>
      <td>128</td>
      <td>&gt;150</td>
    </tr>
    <tr>
      <td>[00<span class="overline">1</span>]</td>
      <td>54</td>
      <td>58</td>
      <td><b>66.5</b></td>
      <td>&gt;150</td>
      <td>66</td>
      <td>&gt;150</td>
    </tr>
    <tr>
      <td rowspan="2">(ABC)(BC)(ABC)</td>
      <td>[001]</td>
      <td><b>64</b></td>
      <td>19.5</td>
      <td>62</td>
      <td>68.5</td>
      <td><b>130</b></td>
      <td>70.5</td>
    </tr>
    <tr>
      <td>[00<span class="overline">1</span>]</td>
      <td>56</td>
      <td>57.5</td>
      <td><b>65</b></td>
      <td>&gt;150</td>
      <td>68</td>
      <td>&gt;150</td>
    </tr>
    <tr>
      <td rowspan="6">ESFs</td>
      <td rowspan="2">(ABC)(BABC)(ABC)</td>
      <td>[001]</td>
      <td><b>67</b></td>
      <td>19.5</td>
      <td>19.5</td>
      <td>&gt;150</td>
      <td>&gt;150</td>
      <td>87.5</td>
    </tr>
    <tr>
      <td>[00<span class="overline">1</span>]</td>
      <td><b>112.5</b></td>
      <td>46.5</td>
      <td>50.5</td>
      <td>&gt;150</td>
      <td>49</td>
      <td>65</td>
    </tr>
    <tr>
      <td rowspan="2">(ABC)(ABAC)(ABC)</td>
      <td>[001]</td>
      <td><b>66.5</b></td>
      <td>19</td>
      <td>19.5</td>
      <td>&gt;150</td>
      <td>&gt;150</td>
      <td>88.5</td>
    </tr>
    <tr>
      <td>[00<span class="overline">1</span>]</td>
      <td><b>120.5</b></td>
      <td>50</td>
      <td>48.5</td>
      <td>&gt;150</td>
      <td>49</td>
      <td>64</td>
    </tr>
    <tr>
      <td rowspan="2">(ABC)(ACBC)(ABC)</td>
      <td>[001]</td>
      <td><b>67</b></td>
      <td>19.5</td>
      <td>42.5</td>
      <td>&gt;150</td>
      <td>141</td>
      <td>88.5</td>
    </tr>
    <tr>
      <td>[00<span class="overline">1</span>]</td>
      <td><b>115.5</b></td>
      <td>49</td>
      <td>51</td>
      <td>&gt;150</td>
      <td>49</td>
      <td>67</td>
    </tr>
  </tbody>
</table>

Table 3. Calculated threshold displacement energies (E<sub>d</sub>s) for C and Si in SiC with intrinsic stacking faults (ISFs) and extrinsic stacking faults (ESFs). The maximum E<sub>d</sub> values for C and Si PKAs in each SiC with SFs are indicated in bold.

$E_e$ is the incident energy, $m_e$ is the electronic mass, $M$ is the atomic mass and $c$ is the velocity of light³³. Assuming 300 keV electrons incident on SiC, the maximum energy transferred to Si and C atom are 59.5 and 71 eV, respectively. Our finding that the E<sub>d</sub> values of C and Si recoils are increased by the existence of SFs, therefore, suggests that SiC with SFs is less susceptible to low energy irradiation. This is consistent with the experiments carried out by Zhang et al.¹⁷ and Jamison et al.¹⁸. Employing 550 keV Si⁺ ion irradiation, Zhang et al. investigated the radiation tolerance of SiC with and without SFs, and found that the SiC with a high-density of SFs exhibits more than an order of magnitude increase in radiation resistance¹⁷. Jamison et al. studied the crystalline-to-amorphous transition in SiC using 1.25 MeV electron irradiation, and also found that SiC with ISFs or ESFs behaves more robustly under irradiation environment¹⁸.

Defect distribution in unfaulted and faulted SiC. The defects created by C and Si PKAs in recoil events are summarized in Tables 4 and 5, respectively. In the case of C PKAs, the defects created in unfaulted SiC mainly consist of the carbon vacancy (C<sub>vac</sub>) and carbon interstitial (C<sub>int</sub>), as shown in Table 2, which agrees well with the results reported by Gao et al.¹². Comparing the damage end states created by different carbon recoils in SiC with

<table>
<thead>
<tr>
<th rowspan="2"></th>
<th rowspan="2">Stacking sequence</th>
<th rowspan="2">Direction</th>
<th colspan="3">Defect type</th>
</tr>
<tr>
<th>C₁</th>
<th>C₂</th>
<th>C₃</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="8">ISFs</td>
<td>(ABC) (AC) (ABC)</td>
<td>[001]</td>
<td>C<sub>Si</sub> + Si<sub>C</sub> + C<sub>int</sub> + C<sub>vac</sub></td>
<td>C<sub>vac</sub> + C<sub>int</sub></td>
<td>C<sub>Si</sub> + Si<sub>C</sub> + C<sub>int</sub> + C<sub>vac</sub></td>
</tr>
<tr>
<td></td>
<td>[001̅]</td>
<td>C<sub>Si</sub> + Si<sub>C</sub> + C<sub>int</sub> + C<sub>vac</sub></td>
<td>C<sub>vac</sub> + C<sub>int</sub></td>
<td>C<sub>vac</sub> + C<sub>Si</sub> + Si<sub>int</sub></td>
</tr>
<tr>
<td>(ABC) (AB) (ABC)</td>
<td>[001]</td>
<td>C<sub>Si</sub> + Si<sub>C</sub> + C<sub>int</sub> + C<sub>vac</sub></td>
<td>C<sub>vac</sub> + C<sub>int</sub></td>
<td>2Si<sub>C</sub> + 2 C<sub>Si</sub> + C<sub>int</sub> + C<sub>vac</sub></td>
</tr>
<tr>
<td></td>
<td>[001̅]</td>
<td>C<sub>vac</sub> + C<sub>Si</sub> + Si<sub>int</sub></td>
<td>C<sub>vac</sub> + C<sub>int</sub></td>
<td>C<sub>vac</sub> + C<sub>Si</sub> + Si<sub>int</sub></td>
</tr>
<tr>
<td>(ABC) (BC) (ABC)</td>
<td>[001]</td>
<td>C<sub>Si</sub> + Si<sub>C</sub> + C<sub>int</sub> + C<sub>vac</sub></td>
<td>C<sub>vac</sub> + C<sub>int</sub></td>
<td>C<sub>Si</sub> + Si<sub>C</sub> + C<sub>int</sub> + C<sub>vac</sub></td>
</tr>
<tr>
<td></td>
<td>[001̅]</td>
<td>C<sub>vac</sub> + C<sub>Si</sub> + Si<sub>int</sub></td>
<td>C<sub>vac</sub> + C<sub>int</sub></td>
<td>C<sub>vac</sub> + C<sub>Si</sub> + Si<sub>int</sub></td>
</tr>
<tr>
<td rowspan="6">ESFs</td>
<td>(ABC) (BABC) (ABC)</td>
<td>[001]</td>
<td>C<sub>Si</sub> + Si<sub>C</sub> + C<sub>int</sub> + C<sub>vac</sub></td>
<td>C<sub>vac</sub> + C<sub>int</sub></td>
<td>C<sub>vac</sub> + C<sub>int</sub></td>
</tr>
<tr>
<td></td>
<td>[001̅]</td>
<td>C<sub>Si</sub> + Si<sub>C</sub> + C<sub>int</sub> + C<sub>vac</sub></td>
<td>C<sub>int</sub> + C<sub>vac</sub></td>
<td>C<sub>vac</sub> + C<sub>int</sub></td>
</tr>
<tr>
<td>(ABC) (ABAC) (ABC)</td>
<td>[001]</td>
<td>C<sub>Si</sub> + Si<sub>C</sub> + C<sub>int</sub> + C<sub>vac</sub></td>
<td>C<sub>Si</sub> + Si<sub>C</sub></td>
<td>C<sub>vac</sub> + C<sub>int</sub></td>
</tr>
<tr>
<td></td>
<td>[001̅]</td>
<td>C<sub>Si</sub> + Si<sub>C</sub> + C<sub>int</sub> + C<sub>vac</sub></td>
<td>C<sub>vac</sub> + C<sub>int</sub></td>
<td>C<sub>vac</sub> + C<sub>int</sub></td>
</tr>
<tr>
<td>(ABC) (ACBC) (ABC)</td>
<td>[001]</td>
<td>C<sub>Si</sub> + Si<sub>C</sub> + C<sub>int</sub> + C<sub>vac</sub></td>
<td>C<sub>vac</sub> + C<sub>int</sub></td>
<td>C<sub>vac</sub> + C<sub>int</sub></td>
</tr>
<tr>
<td></td>
<td>[001̅]</td>
<td>C<sub>Si</sub> + Si<sub>C</sub> + C<sub>int</sub> + C<sub>vac</sub></td>
<td>C<sub>vac</sub> + C<sub>int</sub></td>
<td>C<sub>vac</sub> + C<sub>int</sub></td>
</tr>
</tbody>
</table>

Table 4. Defect configurations for C recoil events in SiC with intrinsic stacking faults (ISFs) and extrinsic stacking faults (ESFs). The denotations for the defect type are the same as those in Table 2.

<table>
<thead>
<tr>
<th rowspan="2"></th>
<th rowspan="2">Stacking sequence</th>
<th rowspan="2">Direction</th>
<th colspan="3">Defect type</th>
</tr>
<tr>
<th>Si₁</th>
<th>Si₂</th>
<th>Si₃</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="6">ISFs</td>
<td>(ABC) (AC) (ABC)</td>
<td>[001]</td>
<td>3Si<sub>C</sub> + 2 C<sub>Si</sub> + Si<sub>vac</sub> + C<sub>int</sub></td>
<td>Si<sub>C</sub> + C<sub>Si</sub> + C<sub>vac</sub> + C<sub>int</sub></td>
<td>2Si<sub>C</sub> + 2 C<sub>Si</sub> + C<sub>vac</sub> + C<sub>int</sub></td>
</tr>
<tr>
<td></td>
<td>[001̅]</td>
<td>–</td>
<td>Si<sub>C</sub> + Si<sub>vac</sub> + C<sub>int</sub></td>
<td>–</td>
</tr>
<tr>
<td>(ABC) (AB) (ABC)</td>
<td>[001]</td>
<td>3Si<sub>C</sub> + 2 C<sub>Si</sub> + Si<sub>vac</sub> + C<sub>int</sub></td>
<td>Si<sub>C</sub> + C<sub>Si</sub></td>
<td>–</td>
</tr>
<tr>
<td></td>
<td>[001̅]</td>
<td>–</td>
<td>Si<sub>C</sub> + Si<sub>vac</sub> + C<sub>int</sub></td>
<td>–</td>
</tr>
<tr>
<td>(ABC) (BC) (ABC)</td>
<td>[001]</td>
<td>3Si<sub>C</sub> + 2 C<sub>Si</sub> + Si<sub>vac</sub> + C<sub>int</sub></td>
<td>C<sub>Si</sub> + Si<sub>C</sub></td>
<td>2Si<sub>C</sub> + 2 C<sub>Si</sub> + C<sub>int</sub> + C<sub>vac</sub></td>
</tr>
<tr>
<td></td>
<td>[001̅]</td>
<td>–</td>
<td>Si<sub>int</sub> + Si<sub>vac</sub></td>
<td>–</td>
</tr>
<tr>
<td rowspan="6">ESFs</td>
<td>(ABC) (BABC) (ABC)</td>
<td>[001]</td>
<td>–</td>
<td>–</td>
<td>2Si<sub>C</sub> + 2 C<sub>Si</sub> + C<sub>int</sub> + C<sub>vac</sub></td>
</tr>
<tr>
<td></td>
<td>[001̅]</td>
<td>–</td>
<td>Si<sub>int</sub> + Si<sub>vac</sub></td>
<td>C<sub>Si</sub> + Si<sub>C</sub></td>
</tr>
<tr>
<td>(ABC) (ABAC) (ABC)</td>
<td>[001]</td>
<td>–</td>
<td>–</td>
<td>2Si<sub>C</sub> + C<sub>Si</sub> + Si<sub>vac</sub> + C<sub>int</sub></td>
</tr>
<tr>
<td></td>
<td>[001̅]</td>
<td>–</td>
<td>Si<sub>int</sub> + Si<sub>vac</sub></td>
<td>Si<sub>int</sub> + Si<sub>vac</sub></td>
</tr>
<tr>
<td>(ABC) (ACBC) (ABC)</td>
<td>[001]</td>
<td>–</td>
<td>C<sub>Si</sub> + Si<sub>C</sub></td>
<td>2Si<sub>C</sub> + 2 C<sub>Si</sub> + C<sub>int</sub> + C<sub>vac</sub></td>
</tr>
<tr>
<td></td>
<td>[001̅]</td>
<td>–</td>
<td>Si<sub>int</sub> + Si<sub>vac</sub></td>
<td>Si<sub>C</sub> + C<sub>int</sub> + Si<sub>vac</sub></td>
</tr>
</tbody>
</table>

Table 5. Defect configurations for Si PKA recoil events in SiC with intrinsic stacking faults (ISFs) and extrinsic stacking faults (ESFs). The denotations for the defect type are the same as those in Table 2.

ISFs, we find that C₂ PKAs show similar defect distribution to unfaulted SiC. However, the Frenkel pair separation (d<sub>FP</sub>) between the carbon vacancy and carbon interstitial is somewhat different. As compared with the d<sub>FP</sub> of 4.02 Å for C[001] in unfaulted SiC, the separations are 3.83, 4.38, 4.42 Å for C₂[001] with (ABC)(AC)(ABC), (ABC)(AB)(ABC) and (ABC)(BC)(ABC) stacking sequences, respectively. For C[001̅] in unfaulted SiC, the Frenkel pair distance is 1.67 Å, which is much smaller than the values of 2.45, 2.51 and 2.50 Å for C₂[001̅] in SiC with (ABC)(AC)(ABC), (ABC)(AB)(ABC) and (ABC)(BC)(ABC) stacking sequences, respectively. These results suggest that in spite of similar damage end states, the pathway for defect generation should be different. For C₁ and C₃ PKAs, the defect generations are more complex. Besides the C FPs, the neighboring Si atoms of the C PKAs are involved in the recoil events, resulting in the additional formation of Si occupying the lattice C site (Si<sub>C</sub>), C occupying the lattice Si site (C<sub>Si</sub>), and (or) Si interstitials (Si<sub>int</sub>). As for C PKAs in SiC with ESFs, the damage end states generated by C₂ and C₃ PKAs are generally similar to those for C PKAs in unfaulted SiC, except for C₂[001] with (ABC)(ABAC)(ABC) arrangement. In this case, the neighboring Si atom is ejected along the [001] direction and then rebounds along the opposite direction to occupy the original site of C PKA. In the meantime, the vacant Si site is occupied by the C PKA, leading to the formation of Si<sub>C</sub> and C<sub>Si</sub> antisite defects. The mechanism for defect generation in C₁ recoil events is different from that in C₂ and C₃ recoils events. The C₁ PKA collides directly with its nearest-neighboring Si atom along the [001] (or [001̅]) direction and occupies the Si lattice site to form C<sub>Si</sub> defect. The struck Si atom receives sufficient energy and moves along the [001] (or [001̅]) direction to replace its neighboring C atom. The replaced C atom then moves away from its lattice site to form stable carbon interstitial. As a result, the final defect structure consists of a C FP, a Si<sub>C</sub> antisite defect and a C<sub>Si</sub> antisite defect. Our calculations show that the total defect number generated by C PKAs in faulted SiC is generally not less than that in unfaulted SiC.

In unfaulted SiC, the defects created by Si PKAs under low energy irradiation are one C FP, two SiC and two CSi antisite defects for Si[001], and one Si FP for Si[00$\overline{1}$]. Comparing the damage end states created by different Si recoils in SiC with ISFs, we find that Si₃[001] show similar defect distribution to unfaulted SiC, whereas Si₁[001], Si₂[001] and Si₂[00$\overline{1}$] recoil events exhibit different character. For Si₁[001], the damage end states consist of three SiC, two CSi, one Si vacancy and one C interstitial. In the case of Si₂[001], only two antisite defects (and one C FP for SiC with (ABC)(AB)(ABC) stacking sequence) are generated. Regarding Si₂[00$\overline{1}$], the created defects are one SiC, one Sivac and one Cint for SiC with (ABC)(AC)(ABC) and (ABC)(AB)(ABC) stacking sequences, and one Si FP for SiC with (ABC)(BC)(ABC) stacking sequence.

As for Si PKAs in SiC with ESFs, only one Si FP is generated by Si₂ along the [00$\overline{1}$] direction and two antisite defects are generated by Si₂ along the [001] direction in SiC with (ABC)(ACBC)(ABC) stacking sequence. For the Si₃[001], the damage end states in SiC with (ABC)(BABC)(ABC) and (ABC)(ACBC)(ABC) arrangements are similar to those in unfaulted SiC, whereas the recoil events in SiC with (ABC)(ABAC)(ABC) stacking sequence show different end states, i.e., two SiC, one CSi, one Si vacancy and one C interstitial. In the case of Si₃ PKAs along the [00$\overline{1}$] direction, the defect generation are relatively simple, as indicated by CSi + SiC for (ABC)(BABC)(ABC), Si FP for (ABC)(ABAC)(ABC), and SiC + Cint + Sivac for (ABC)(ACBC)(ABC) stacking sequences.

The total defect number created by C and Si PKAs in faulted SiC is illustrated in Fig. 3. It is found that the Si PKAs are generally more efficient in damage production than C PKAs³⁴. Weber *et al.* have calculated the efficiency of damage production for C, Si and Au PKAs over the energy range from 0.1 to 400 keV using a modified version of the stopping and range of ions in matter (SRIM) code³⁴. They suggested that the total damage efficiency for C PKAs is much lower than that for Si PKAs at low damage energies³⁴, which is consistent with our results. Comparing the defects generated by Si PKAs in faulted SiC, we find that the defect configurations are similar, i.e., antisite defect, Si FP and C FP. Besides, the defect number for different Si PKA along a certain incident direction is nearly identical to each other. Zhang *et al.* applied the MD method to study the defect production in sc-SiC, SiC with a high density of ESFs and SiC with a high density of ISFs, and found that there are no great difference among the three simulation cells in defect number and configurations¹⁷. In the meantime, the distribution of created defects in faulted SiC is shown to be very localized. These results agree well with the study of radiation tolerance of sc-SiC and SiC with SFs performed by Zhang *et al.*, in which it was found that the existence of SFs leads to more localized point defect production¹⁷. Comparing the different defect configurations for unfaulted and faulted SiC, we find that antisite defects are the most common defects in faulted SiC, whereas in unfaulted SiC the FPs are dominant. The defect generation in sc-SiC and nc-SiC with a grain size smaller than 12 nm have been investigated by Gao *et al.* using the MD method, in which the kinetic energies of 10 keV for PKA were simulated. They also found that in nc-SiC the antisite defects are more than other defects, in contrast to those produced in sc-SiC, where the dominant defects are FPs³⁵.

### Origin of the difference in the radiation response between unfaulted and faulted SiC.
Jamison *et al.* studied the energetics of point defects near the SFs and found that the critical migration and reaction energies are reduced significantly enough to enhance the amorphization resistance by increasing the probability of point defect recombination and annihilation¹⁸. To explore the origin of the difference in the radiation response behavior of unfaulted and faulted SiC, we further analyze the potential energy increase for stable defect formation in the recoil events of C₂[001] at 70 eV, C₂[00$\overline{1}$] at 70 eV, Si₂[001] at 141 eV and Si₃[00$\overline{1}$] at 152.5 eV. As illustrated in Fig. 4(a), the maximum potential energy increases for C₂[001] are 25.3, 19.2 and 17.2 eV for SiC with (ABC)(AC)(ABC) arrangement, SiC with (ABC)(ACBC)(ABC) arrangement and unfaulted SiC, respectively. In the case of C₂[00$\overline{1}$], the maximum potential energy increases are 20.8, 17.2 and 12.2 eV, corresponding to SiC with (ABC)(AC)(ABC), (ABC)(ACBC)(ABC) arrangements and unfaulted SiC, respectively. The situation in Si₂[001] at 141 eV and Si₃[00$\overline{1}$] at 152.5 eV are very similar to those in C recoil events, i.e., the maximum potential energy increases for SiC with SFs are always larger than those for unfaulted SiC. The maximum potential energy increases represent the maximum in screen-Coulomb interactions between PKAs and one or more atomic nuclei on lattice or defect sites, similar to classical two-body interaction³³. Our results show that the introduction of SFs leads to greater maximum potential energy increase than unfaulted state, i.e., stronger interaction due to more effective screening of Coulomb force between PKA and its neighbors exist in faulted SiC, which may increase the energy barrier for defect generation. Consequently, a greater kinetic energy is necessary to overcome the larger energy barrier for defect generation, corresponding to the larger threshold displacement energies for C and Si PKAs in faulted SiC than those in unfaulted SiC. Another finding is that the maximum potential energy increases for Si PKAs are generally larger than those for C PKAs, which is consistent with our results that generally considerably higher energies are needed for displacing the Si PKAs than those for displacing the C PKAs.

### Conclusions
In summary, low-energy recoil events in unfaulted and faulted SiC have been investigated by *ab initio* molecular dynamics method based on density functional theory. The threshold displacement energies are shown to be dependent on the interlayer spacing between the PKA and the SFs. The weighted average E_d values are calculated to be 52.1 eV for C[001], 59.5 eV for C[00$\overline{1}$], >99.6 eV for Si[001] and >122.1 eV for Si[00$\overline{1}$] in SiC with ISFs. As for SiC containing ESFs, the average E_d values are 37.8, 71.6, >128.4 and >88.1 eV for C[001], C[00$\overline{1}$], Si[001] and Si[00$\overline{1}$], respectively. As compared with the E_d values in unfaulted SiC, the E_d values in faulted SiC are generally larger, i.e., the PKAs in faulted SiC are more difficult to be displaced, which may enhance the radiation tolerance of SiC, agreeing well with the recent experiments. In the meantime, the defect generation mechanism for C and Si PKAs in faulted SiC is generally more complex and the defect contribution is very localized. The most common defect configurations in faulted SiC are antisite defects, whereas the Frenkel pairs are dominant in unfaulted SiC.

![](./images/814553795932454912_3.jpg)

Figure 3. Total defect number created by (a) C PKAs in SiC with intrinsic SFs; (b) C PKAs in SiC with extrinsic SFs; (c) Si PKAs in SiC with intrinsic SFs; and (d) Si PKAs in SiC with extrinsic SFs. Here, the $SF_{int1}$, $SF_{int2}$ and $SF_{int3}$ represent intrinsic SFs with (ABC)(AC)(ABC), (ABC)(AB)(ABC) and (ABC)(BC)(ABC) atomic arrangements, respectively, and the $SF_{ext1}$, $SF_{ext2}$ and $SF_{ext3}$ represent extrinsic SFs with (ABC)(BABC)(ABC), (ABC)(ABAC)(ABC) and (ABC)(ACBC)(ABC) atomic arrangements, respectively.

![](./images/814553795932454912_4.jpg)

Figure 4. The calculated potential energy increase for (a) $C_3[001]$ at 70 eV; (b) $C_3[00\overline{1}]$ at 70 eV; (c) $Si_2[001]$ at 141 eV; and (d) $Si_3[00\overline{1}]$ at 152.5 eV.

Potential energy increase analysis shows that the existence of SFs increases the energy barrier for defect generation, i.e., the C and Si primary knock-on atoms in faulted SiC need to overcome higher energy barrier than those in unfaulted SiC to generate defects.

## Methods
All the calculations are carried out using the Spanish Initiative for Electronic Simulations with Thousands of Atoms (SIESTA) code. The norm-conserving Troullier-Martins pseudopotential³⁶ are employed to determine the interaction between ions and electrons and the exchange-correlation potential is described by the generalized gradient approximation parameterized by Perdew, Burke and Ernzerhof³⁷. The valence wave functions are expanded by a basis set of localized atomic orbitals and single-ζ basis sets are employed, with a K-point sampling of $1 \times 1 \times 1$ in the Brillouin zone and a cutoff energy of 90 Ry. In the literature, Zhang *et al.*¹⁷ and Lin *et al.*³⁸ have reported that the SFs lie in the (111) plane of SiC. Hence, both the ISFs and ESFs investigated in this study are created based on the 3C-SiC(111) plane. For SiC with ISFs and ESFs, the supercell consists of 256 and 320 atoms, respectively. Three types of ISFs, i.e., (ABC)(AC)(ABC), (ABC)(AB)(ABC) and (ABC)(BC)(ABC) and three types of ESFs, i.e., (ABC)(BABC)(ABC), (ABC)(ABAC)(ABC) and (ABC)(ACBC)(ABC), as shown in Figs 1 and 2, have been considered. To simulate the low energy recoil events, three types of Si or C on the boundary of the SFs, as denoted in Figs 1 and 2, are selected as PKA and a certain amount of kinetic energy is provided along the direction perpendicular to the SiC(111) surface, i.e.,[001] and [00$\overline{1}$]. The simulations are conducted with a NVE ensemble and a variable time step scheme is employed to avoid the instability of the system.

## References
1.  Baumeier, B., Kruger, P., Pollmann, J. & Vajenine, G. V. Electronic structure of alkali-metal fluorides, oxides, and nitrides: Density-functional calculations including self-interaction corrections. *Phys. Rev. B* **78**, 12 (2008).
2.  Nakano, H., Watari, K., Kinemuchi, Y., Ishizaki, K. & Urabe, K. Microstructural characterization of high-thermal-conductivity SiC ceramics. *J. European Ceram. Soc.* **24**, 3685–3690 (2004).
3.  Raffray, A. R. *et al.* Design and material issues for high performance SiCf/SiC-based fusion power cores. *Fusion Eng. Des.* **55**, 55–95 (2001).
4.  Verrall, R. A., Vlajic, M. D. & Krstic, V. D. Silicon carbide as an inert-matrix for a thermal reactor fuel. *J. Nucl. Mater.* **274**, 54–60 (1999).
5.  Yano, T., Suzuki, M., Miyazaki, H. & Iseki, T. Effect of neutron irradiation on passive oxidation of silicon carbide. *J. Nucl. Mater.* **233**, 1275–1278 (1996).
6.  Fenici, P., Rebelo, A. J. F., Jones, R. H., Kohyama, A. & Snead, L. L. Current status of SiC/SiC composites R & D. *J. Nucl. Mater.* **258**, 215–225 (1998).
7.  Audren, A., Benyagoub, A., Thome, L. & Garrido, F. Ion implantation of iodine into silicon carbide: Influence of temperature on the produced damage and on the diffusion behaviour. *Nucl. Instrum. Meth. B* **266**, 2810–2813 (2008).
8.  Ishimaru, M., Bae, I. T. & Hirotsu, Y. Electron-beam-induced amorphization in SiC. *Phys. Rev. B* **68**, 144102 (2003).
9.  Weber, W. J. & Wang, L. M. The temperature dependence of ion-beam-induced amorphization in beta-SiC. *Nucl. Nucl. Instrum. Meth. B* **106**, 298–302 (1995).
10. Snead, L. L. & Hay, J. C. Neutron irradiation induced amorphization of silicon carbide. *J. Nucl. Mater.* **273**, 213–220 (1999).
11. Lucas, G. & Pizzagalli, L. Ab initio molecular dynamics calculations of threshold displacement energies in silicon carbide. *Phys. Rev. B* **72**, 161202 (2005).
12. Gao, F., Xiao, H. Y. & Weber, W. J. Ab initio molecular dynamics simulations of low energy recoil events in ceramics. *Nucl. Instrum. Meth. B* **269**, 1693–1697 (2011).
13. Inui, H., Mori, H., Suzuki, A. & Fujita, H. Electron-irradiation-induced crystalline-to-amorphous transition in β-SiC single crystals. *Philos. Mag. B* **65**, 1–14 (1992).
14. Inui, H., Mori, H. & Fujita, H. Electron-irradiation-induced crystalline to amorphous transition in α-Sic single crystals. *Philos. Mag. B* **61**, 107–124 (1990).
15. Kurishita, H. *et al.* Development of ultra-fine grained W-(0.25-0.8)wt%TiC and its superior resistance to neutron and 3 MeV He-ion irradiations. *J. Nucl. Mater.* **377**, 34–40 (2008).
16. Mo, Y. F. & Szlufarska, I. Simultaneous enhancement of toughness, ductility, and strength of nanocrystalline ceramics at high strain rates. *Appl. Phys. Lett.* **90**, 18 (2007).
17. Zhang, Y. W. *et al.* Nanoscale engineering of radiation tolerant silicon carbide. *Phys. Chem.Chem.I Phys.* **14**, 13429–13436 (2012).
18. Jamison, L. *et al.* Experimental and ab initio study of enhanced resistance to amorphization of nanocrystalline silicon carbide under electron irradiation. *J. Nucl. Mater.* **445**, 181–189 (2014).
19. Umeno, Y., Yagi, K. & Nagasawa, H. Ab initio density functional theory calculation of stacking fault energy and stress in 3C-SiC. *Phys. Status. Solidi. B* **249**, 1229–1234 (2012).
20. Oda, T., Zhang, Y. W. & Weber, W. J. Study of intrinsic defects in 3C-SiC using first-principles calculation with a hybrid functional. *J. Chem. Phys.* **139**, 12 (2013).
21. Lucas, G. & Pizzagalli, L. Ab initio molecular dynamics calculations of threshold displacement energies in silicon carbide. *Phys. Rev. B* **72**, 161202 (2005).
22. Lucas, G. & Pizzagalli, L. Comparison of threshold displacement energies in beta-SiC determined by classical potentials and ab initio calculations. *Nucl. Instrum. Meth. B* **229**, 359–366 (2005).
23. Xiao, H. Y., Gao, F., Zu, X. T. & Weber, W. J. Threshold displacement energy in GaN: Ab initio molecular dynamics study. *J. Appl. Phys.*,**105**, 12 (2009).
24. Xiao, H. Y., Gao, F. & Weber, W. J. Ab initio investigation of phase stability of Y2Ti2O7 and Y2Zr2O7 under high pressure. *Phys. Rev. B* **80**, 21 (2009).
25. Xiao, H. Y., Zhang, Y. & Weber, W. J. Ab initio molecular dynamics simulations of low-energy recoil events in ThO2, CeO2, and ZrO2. *Phys. Rev. B* **86**, 5 (2012).
26. Xiao, H. Y., Gao, F., Zu, X. T. & Weber, W. J. Ab initio molecular dynamics simulation of a pressure induced zinc blende to rocksalt phase transition in SiC. *J.Phys.:Conden. Matter* **21**, 24 (2009).
27. Chang, K. J. & Cohen, M. L. Ab initio pseudopotential study of structural and high-pressure properties of SiC. *Phys. Rev. B* **35**, 8196–8201 (1987).
28. Salvador, M., Perlado, J. M., Mattoni, A., Bernardini, F. & Colombo, L. Defect energetics of beta-SIC using a new tight-binding molecular dynamics model. *J. Nucl. Mater.* **329**, 1219–1222 (2004).
29. Kackell, P., Furthmuller, J. & Bechstedt, F. Stacking faults in group-IV crystals: An ab initio study. *Phys. Rev. B* **58**, 1326–1330 (1998).
30. Maeda, K., Suzuki, K., Fujita, S., Ichihara, M. & Hyodo, S. Defects in plastically deformed 6H SiC single crystals studied by transmission electron microscopy. *Philos. Mag. A* **57**, 573–592 (1988).

31. Devanathan, R. & Weber, W. J. Displacement energy surface in 3C and 6H SiC. J. Nucl. Mater. 278, 258–265 (2000).

32. Gao, F., Xiao, H. Y., Zu, X. T., Posselt, M. & Weber, W. J. Defect-Enhanced Charge Transfer by Ion-Solid Interactions in SiC using Large-Scale Ab Initio Molecular Dynamics Simulations. Phys.Rev. Lett. 103, 2 (2009).

33. Xiao, H. Y., Weber, W. J., Zhang, Y. & Zu, X. T. Ab initio molecular dynamics simulations of ion-solid interactions in zirconate pyrochlores. Acta Mater. 87, 273–282 (2015).

34. Weber, W. J., Gao, F., Devanathan, R. & Jiang, W. The efficiency of damage production in silicon carbide. Nucl. Instrum. Meth. B 218, 68–73 (2004).

35. Gao, F., Chen, D., Hu, W. & Weber, W. J. Energy dissipation and defect generation in nanocrystalline silicon carbide. Phys. Rev. B 81, 18 (2010).

36. Troullier, N. & Martins, J. L. Efficient pseudopotential for plane-wave calculatuons. Phys. Rev. B 43, 1993–2006 (1991).

37. Perdew, J. P., Burke, K. & Ernzerhof, M. Generalized gradient approximation made simple. Phys. Rev. Lett. 77, 3865–3868 (1996).

38. Lin, Y. R. et al. Atomic configuration of irradiation-induced planar defects in 3C-SiC. Appl. Phys. Lett. 104, 121909 (2014).

## Acknowledgements
H.Y. Xiao was supported by the NSAF Joint Foundation of China (Grant No. U1530129) and the scientific research starting funding of University of Electronic Science and Technology of China (Grant No. Y02002010401085). Z.J. Liu was supported by National Natural Science Foundation of China (Grant No. 11464025) and the New Century Excellent Talents in University under Grant No. NCET-11-0906. The theoretical calculations were performed using the supercomputer resources at TianHe-1 located at National Supercomputer Center in Tianjin.

## Author Contributions
Z.L. and X.Z. designed the calculations. M.J. conducted the calculations and wrote the manuscript. S.P., H.Z., C.X., H.X. and F. Z. contributed to the discussion and interpretation of the results. All authors discussed the results and reviewed the manuscript.

## Additional Information
Competing financial interests: The authors declare no competing financial interests.

How to cite this article: Jiang, M. et al. Ab initio molecular dynamics simulation of the effects of stacking faults on the radiation response of 3C-SiC. Sci. Rep. 6, 20669; doi: 10.1038/srep20669 (2016).

![](./images/814553795932454912_5.jpg)
This work is licensed under a Creative Commons Attribution 4.0 International License. The images or other third party material in this article are included in the article's Creative Commons license, unless indicated otherwise in the credit line; if the material is not included under the Creative Commons license, users will need to obtain permission from the license holder to reproduce the material. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/