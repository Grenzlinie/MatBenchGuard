This article was downloaded by: [Northeastern University]
On: 09 January 2015, At: 03:14
Publisher: Taylor & Francis
Informa Ltd Registered in England and Wales Registered Number: 1072954 Registered office: Mortimer House, 37-41 Mortimer Street, London W1T 3JH, UK

![](./images/811714479795470337_1.jpg)

# Research in Nondestructive Evaluation
Publication details, including instructions for authors and subscription information:
http://www.tandfonline.com/loi/urnd20

## Approach to Lamb Wave Lateral Crack Quantification in Elastic Plate Based on Reflection and Transmission Coefficients Surfaces

Shen Wang $^{a}$ , Songling Huang $^{a}$ , Wei Zhao $^{a}$ \& Xue Wang $^{b}$

$^{a}$ State Key Laboratory of Control and Simulation of Power System and Generation Equipments, Tsinghua University, Beijing, China
$^{b}$ State Key Laboratory of Precision Measurement Technology and Instruments, Tsinghua University, Beijing, China
Published online: 13 Oct 2010.

---

To cite this article: Shen Wang, Songling Huang, Wei Zhao & Xue Wang (2010) Approach to Lamb Wave Lateral Crack Quantification in Elastic Plate Based on Reflection and Transmission Coefficients Surfaces, Research in Nondestructive Evaluation, 21:4, 213-223, DOI: 10.1080/09349847.2010.516060

To link to this article: http://dx.doi.org/10.1080/09349847.2010.516060

---

PLEASE SCROLL DOWN FOR ARTICLE

Taylor & Francis makes every effort to ensure the accuracy of all the information (the "Content") contained in the publications on our platform. However, Taylor & Francis, our agents, and our licensors make no representations or warranties whatsoever as to the accuracy, completeness, or suitability for any purpose of the Content. Any opinions and views expressed in this publication are the opinions and views of the authors, and are not the views of or endorsed by Taylor & Francis. The accuracy of the Content should not be relied upon and should be independently verified with primary sources of information. Taylor and Francis shall not be liable for any losses, actions, claims, proceedings, demands, costs, expenses, damages, and other liabilities whatsoever or howsoever caused arising directly or indirectly in connection with, in relation to or arising out of the use of the Content.

This article may be used for research, teaching, and private study purposes. Any substantial or systematic reproduction, redistribution, reselling, loan, sub-licensing, systematic supply, or distribution in any form to anyone is expressly forbidden. Terms & Conditions of access and use can be found at http://www.tandfonline.com/page/terms-and-conditions

Research in Nondestructive Evaluation, 21: 213–223, 2010
Copyright © American Society for Nondestructive Testing
ISSN: 0934-9847 print/1432-2110 online
DOI: 10.1080/09349847.2010.516060

![](./images/811714479795470337_2.jpg)

# APPROACH TO LAMB WAVE LATERAL CRACK QUANTIFICATION IN ELASTIC PLATE BASED ON REFLECTION AND TRANSMISSION COEFFICIENTS SURFACES

Shen Wang, $^{1}$ Songling Huang, $^{1}$ Wei Zhao, $^{1}$ and Xue Wang $^{2}$

$^{1}$ State Key Laboratory of Control and Simulation of Power System and Generation Equipments, Tsinghua University, Beijing, China
$^{2}$ State Key Laboratory of Precision Measurement Technology and Instruments, Tsinghua University, Beijing, China

Ultrasonic guided wave is promising in structure integrity management, but there is still much to learn about it because of its complex mechanism. Defect sizing or quantification is very important for structure inspection using ultrasonic guided waves, and this inverse problem is also very difficult to solve. The work presented in this article aims to resolve the lateral crack quantification problem in the inspection of thin elastic plate using Lamb wave. First, two-dimensional (2D) boundary element method (BEM) simulation was used to study the interaction of one chosen pure mode Lamb wave with lateral crack defect, and this could be defined as the forward problem. Then reflection and transmission coeffi- cients surfaces were built from the results of the numerical simulation. Finally, an approach for lateral crack quantification based on these reflection and transmission coefficients sur- faces was proposed. The quantification examples show that the presented approach gives acceptable accuracy. Some limitations of this approach are also discussed.

Keywords: Lamb wave, lateral crack quantification, reflection and transmission coefficients surfaces, ultrasonic guided wave

## INTRODUCTION

The integrity maintenance of in-service structure is indispensable to ensure safe operation. Nondestructive Testing and Evaluation (NDT&E) is the process of investigating the structure about possible defects without damaging it, thus very suitable for structure integrity management. Various methods exist in NDT&E field, based on different physical mechanisms ranging from electricity to mechanics.

Ultrasonic testing relies on ultrasonic waves that propagate in the material under investigation, and is widely used because of its relatively fast, clean, and cost-effective nature. A limitation of traditional ultrasonic

Address correspondence to Shen Wang, State Key Laboratory of Control and Simulation of Power System and Generation Equipments, Tsinghua University, Beijing 100084, China. E-mail: wangshen@ mail.tsinghua.edu.cn

inspection using bulk waves is the low inspection speed because of the generally applied point-by-point scheme of testing. Ultrasonic guided wave is the special ultrasonic wave that propagates in bounded media called waveguide, along its extension direction [1–3]. Typical guided waves include Lamb wave and shear horizontal (SH) guided wave in a thin plate, Rayleigh wave at a half space surface, longitudinal and torsional waves along the pipe's axis [4,5], pipe circumferential Lamb [6], SH guided wave [7], etc. One unique characteristic of guided waves is the dispersion relation between the velocity of wave propagation and the testing frequency, with only Rayleigh wave as an exception. Structure inspection using ultrasonic guided waves is promising because of its high speed and the ability of long-distance material investigation, while there is still much to learn about it because of its relatively complex mechanism.

Defect sizing or quantification is always an important, necessary but difficult process in NDT&E field. There is no exception for NDE based on ultrasonic guided waves. Rose studied Lamb wave's transmission coefficient $(|T|)$'s variation with frequency-thickness product $(|T|$-$fd$ curve) based on BEM formulation, and observed the approximate linear relationship between the $fd$ corresponding to $|T|$-$fd$ curve's minimum and the defect depth [8]. One difficulty still exists in this approach, as in a practical guided wave-based inspection system the testing frequency is often selected in advance and fixed, and thus it is inconvenient to obtain the $|T|$-$fd$ curve or $|R|$-$fd$ curve ($|R|$ is the reflection coefficient. These two curves describe transmission and reflection coefficients' variations with frequency-thickness product, respectively) in most cases.

This article presents an alternative approach to solve, at least partially, the inverse problem of lateral crack quantification in an elastic plate using Lamb waves, also based on the results from numerical simulation. Although cracks in the real world may have irregular shapes and complex geometries, notches with regular shapes and tight openings are used in this study as an idealization. The word 'crack' really means 'notch' in the following context, while 'crack' is still reserved to indicate that the ultimate goal of this study is to detect cracking defect quantitatively in a real inspection. 'Lateral' here means the extension direction of the crack is ideally perpendicular to the propagating direction of Lamb wave. Another added assumption is that the length of the crack is infinite, so a two-dimensional (2D) plane-strain model is enough for this study.

Although the strictly lateral cracking with an infinite length in an elastic plate is in fact a special and idealized model of the general 3-dimensional arbitrary defects found in practical structures, it is still useful to study guided wave scattering and size quantification of this kind of cracking. One good example is stress corrosion cracking (SCC) detection in natural gas pipelines using circumferential Lamb wave. SCC often extends in the axial direction of the pipeline, thus forming a lateral cracking pattern with the circumferential Lamb wave.

# NUMERICAL SIMULATIONS, THE FORWARD PROBLEM

## BEM Modeling

The BEM modeling presented here was inspired by the work of Cho [9,10] and Zhao [11,12]. This hybrid method combines the analytical equations of Lamb wave with numerical elastodynamic BEM formulation. The model of the simulation is depicted in Fig. 1. A closed region for BEM formulation consisting of the top and bottom traction free boundaries, two virtual boundaries and defect surface is formed. A pure mode of Lamb wave is input from the left virtual boundary. After scattering at the defect, reflected and transmitted modes reach the left and right boundaries, respectively.

Reflection coefficient $|R|$ is defined as the amplitude ratio of a reflected mode and the input mode. Transmission coefficient $|T|$ is defined as the amplitude ratio of a transmitted mode and the input mode. Total numbers of reflected mode(s) and transmitted mode(s) are decided from the dispersion curves of Lamb wave.

## BEM Simulation Examples

A 2D frequency domain hybrid boundary element method simulation program was developed to study Lamb wave's scattering from lateral cracking defects in an elastic isotropic plate, following the similar procedure by Cho. The simulation results are curves representing reflection and transmission coefficients' variations with the variables like the opening width and depth of the crack, and the inspection frequency (or frequency-thickness product), under the selected incident Lamb wave mode.

The material parameters used in the simulation are listed in Table 1. Unless stated explicitly, a steel plate of 1 mm thickness is used.

A typical simulation result depicting the reflection and transmission coefficients' variations with increasing defect depth ($|R|$-depth and $|T|$-depth curves) for a triangular cross-section crack with 0.1 mm opening width is shown in Fig. 2, with $S_0$ mode, $fd=1000\ \text{Hz} \times \text{m}$ as the incidence. Coefficients $|R|_{S_0}$ and $|T|_{S_0}$ change monotonically in this example. Mode conversion from input $S_0$ mode to reflected $A_0$ mode ($|R|_{A_0}$) and transmitted $A_0$ mode ($|T|_{A_0}$) could also be observed.

![](./images/811714479795470337_3.jpg)

FIGURE 1. The BEM model.

<table>
<caption>TABLE 1 Material Parameters for Numerical Simulation (Steel Plate)</caption>
<thead>
  <tr>
    <th>Material parameter</th>
    <th>Value of the parameter</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Mass density $\rho$ (kg/m³)</td>
    <td>7800</td>
  </tr>
  <tr>
    <td>Transverse wave velocity $C_{\text{T}}$ (m/s)</td>
    <td>3200</td>
  </tr>
  <tr>
    <td>Longitudinal wave velocity $C_{\text{L}}$ (m/s)</td>
    <td>5940</td>
  </tr>
</tbody>
</table>

Theoretical validation of the simulation could be achieved using the energy conservation rule, expressed as

$$
E = \sum_{j} \left[ \left( |R|^{j} \right)^{2} + \left( |T|^{j} \right)^{2} \right] = 1,
$$

in which $E$ stands for normalized total energy, and $j$ is the mode index of the reflection coefficient $|R|$ and the transmission coefficient $|T|$. The range of $j$ is decided from the dispersion curves of Lamb wave. For the example in Fig. 2, $j=2$ because there are only 2 modes ($S_0$ and $A_0$) under the selected $fd$ value. The energy curve calculated from the coefficients corresponding to Fig. 2 is shown in Fig. 3, in which the normalized total energy is very near to 1 for all investigated defect depths.

To validate the simulation experimentally, an electromagnetic acoustic transducer (EMAT) inspection system was built to detect artificial lateral

![](./images/811714479795470337_4.jpg)

FIGURE 2. Reflection and transmission coefficients’ variations with increasing defect depth ($|R|$-depth and $|T|$-depth curves) for a triangular cross-section crack with 0.1 mm opening width, with $S_0$ mode Lamb wave, $fd=1000\,\text{Hz} \times \text{m}$ as the incidence.

![](./images/811714479795470337_5.jpg)

FIGURE 3. Energy-depth curve corresponding to Fig. 2.

cracks/notches in steel plates. Low power tone burst signal from an HP33120A signal generator enters an AG1024 power amplifier; the gener- ated high power signal travels through an impedance matching network, then into the EMAT transmitter coil. The meander type coil was built on a printed circuit board (PCB), and the coil's wire spacing satisfies the matching relation between the wave length, the phase velocity and the frequency of the selected operation point on Lamb wave's phase velocity dispersion curves. Static horizontal bias magnetic field is perpendicular to the coil's wires. Lamb wave is generated in the steel plate by the combined action of both Lorentz force and magnetostrictive force [13,14]. An EMAT receiver with the same structure as the transmitter detects the signal, sends it through another impedance matching network, an amplifier and a band pass filter, and finally into an oscilloscope or a DAQ card installed in the computer.

As an example, Fig. 4 shows theoretical and experimental curves depict- ing $S_{0}$ mode reflection coefficient $|R|_{S_{0}}$,s variation with increasing defect depth (|R|-depth curve). The defects investigated are rectangular cross- section cracks with the same width of 0.5 mm, and $fd=2343.8 Hz × m$. The thickness of the plate is 7 mm. Difference exists between these two curves, but the trends of variation are the same.

The discrepancy between the simulation and experimental data stems from the complexity of guided wave mechanism. Many factors may influ- ence the practical inspection, and thus contribute to the discrepancy. To name a few, the simulation is carried out in the frequency domain, while a tone burst signal with a short time duration is used in the experiments, which has a slightly broader frequency band than what the simulation expects, so the generation of a single pure mode cannot be completely guar- anteed, and the accompanying frequency dispersion will cause loss of

![](./images/811714479795470337_6.jpg)

FIGURE 4. Theoretical and experimental curves of $S_0$ mode reflection coefficient's variation with defect depth ($|R|$-depth curve), the defects are rectangular cross-section cracks with 0.5 mm width, $fd$=2343.8 Hz × m.

amplitude of the received signal; all theoretical derivations assume that the steel plate is elastically isotropic and has free top and bottom surfaces, which is only an approximation of the real situation; the values of the material parameters listed in Table 1 are typical values, the real parameters of the steel plate under investigation may have slightly different values, which will also introduce some errors; noises from many sources could lead to accuracy loss, too, especially when using EMATs that almost always have a very low signal noise ratio (SNR) as the transmitter and receiver.

# APPROACH TO CRACK SIZE QUANTIFICATION BASED ON COEFFICIENTS SURFACES, THE INVERSE PROBLEM

The proposed crack size quantification approach is based on the numerical simulation results. The testing frequency is assumed to be constant in the size quantification process.

First, the quantification process involves the generation of so-called reflection and transmission coefficients surfaces. These surfaces depict the variations of the reflection and transmission coefficients with the two variables of crack opening width and crack depth, under the selected and fixed inspection frequency. Figures 5 and 6 show, respectively, the reflection and transmission coefficients surfaces for $S_0$ mode incidence at a rectangular cross-section crack in a steel plate with a thickness of 1 mm, and the $fd$ value is 1000 Hz × m.

The reflection and transmission coefficients of a crack with unknown width and depth are assumed to be known already, and serve as the inputs to this algorithm. These coefficients should come from experimental

![](./images/811714479795470337_7.jpg)

FIGURE 5. $S_0$ mode reflection coefficients surface for rectangular cross-section defect ($fd=1000\ \text{Hz} \times \text{m}$).

measurements of signal amplitudes as defined previously, while in order to minimize the disturbances from so many practical inspection parameters, coefficients from the numerical simulation are used instead.

In the second step of the quantification approach, $|R|$-plane corresponding to the known reflection coefficient is drawn in the reflection coefficients sur- face figure; the points on the projection of their intersecting line in the width-depth plane should satisfy the $|R|$ coefficient requirement. In the same

![](./images/811714479795470337_8.jpg)

FIGURE 6. $S_0$ mode transmission coefficients surface for rectangular cross-section defect ($fd=1000\ \text{Hz} \times \text{m}$).

![](./images/811714479795470337_9.jpg)

FIGURE 7. Projections of $|R|$ plane-$|R|$ surface intersecting line and $|T|$ plane-$|T|$ surface intersecting line for 0.26 mm width and 40% depth rectangular cross-section defect, $S_0$ mode, $fd$=1000 Hz $\times$ m.

way, a projection of the intersecting line of $|T|$-plane and transmission coefficients surface could also be obtained. The intersecting point of these two projection curves is the quantification point, whose coordinates are the quantified width and depth. An example of these two projection curves is shown in Fig. 7. In this figure, the rectangular cross-section crack used to generate the simulated known coefficients $|R|$ and $|T|$ is 0.26 mm in width and 40% in depth, and the quantified width and depth are 0.261 mm and 40.00% respectively.

Several examples including the previous one are summarized in Table 2. From this table it can easily be concluded that the depth quantification has enough accuracy, while width quantification error is relatively bigger. This is understandable considering that the $|R|$-depth and $|T|$-depth curves of the same mode as the incidence ($|R|_{S_0}$ and $|T|_{S_0}$ curves in Fig. 2) almost occupy the full coefficient range between 0 and 1, but the $|R|$-width and $|T|$-width curves (not given in this article) often change gently.

<table>
<caption>TABLE 2 Examples of Rectangular Cross-Section Crack Quantification</caption>
<thead>
<tr>
<th>Width (mm)</th>
<th>Depth (%)</th>
<th>$|R|$</th>
<th>$|T|$</th>
<th>Quantified width (mm)</th>
<th>Quantified depth (%)</th>
</tr>
</thead>
<tbody>
<tr>
<td>0.26</td>
<td>40</td>
<td>0.398</td>
<td>0.785</td>
<td>0.261</td>
<td>40.00</td>
</tr>
<tr>
<td>0.45</td>
<td>23</td>
<td>0.212</td>
<td>0.932</td>
<td>0.476</td>
<td>22.77</td>
</tr>
<tr>
<td>0.15</td>
<td>55</td>
<td>0.551</td>
<td>0.615</td>
<td>0.150</td>
<td>55.00</td>
</tr>
<tr>
<td>0.56</td>
<td>22</td>
<td>0.210</td>
<td>0.937</td>
<td>0.585</td>
<td>21.85</td>
</tr>
<tr>
<td>0.67</td>
<td>46</td>
<td>0.495</td>
<td>0.723</td>
<td>0.674</td>
<td>46.03</td>
</tr>
</tbody>
</table>

![](./images/811714479795470337_10.jpg)

FIGURE 8. $S_0$ mode reflection coefficients surface for triangular cross-section defect ($fd=1000\,\text{Hz} \times \text{m}$).

A similar process is then applied to triangular cross-section crack quanti- fication. Reflection coefficients surface is depicted in Fig. 8, and transmission coefficients surface is depicted in Fig. 9.

In Fig. 10, the crack used to generate the simulated known coefficients $|R|$ and $|T|$ is 0.67 mm in width and $46\%$ in depth, and the quantified width and depth are 0.677 mm and $46.01\%$, respectively.

![](./images/811714479795470337_11.jpg)

FIGURE 9. $S_0$ mode transmission coefficients surface for triangular cross-section defect ($fd=1000\,\text{Hz} \times \text{m}$).

![](./images/811714479795470337_12.jpg)

FIGURE 10. Projections of $|R|$ plane-$|R|$ surface intersecting line and $|T|$ plane-$|T|$ surface intersecting line for 0.67 mm opening width and 46% depth triangular cross-section defect, $S_0$ mode, $fd$=$1000\,\text{Hz} \times \text{m}$.

Examples including the previous one are summarized in Table 3.

The results in Tables 2 and 3 show that the method based on the reflection and transmission coefficients surfaces has acceptable accuracy. This approach has a clear physical interpretation and is easy to implement.

The proposed quantification method requires that both $|R|$ and $|T|$ coefficients be measured in the inspection. This method also relies on the monotonicity, or existence of inverse function, of curves representing the reflection and transmission coefficients' variations with crack depth and opening width. Monotonicity in the depth increasing direction is easier to obtain, especially for $S_0$ mode, while the coefficients often change little and non-monotonically in the width increasing direction, so it is possible that more than one intersecting points could be found in projection curves figures like Figs. 7 and 10; those points have different widths and similar depths. Considering that the depth is relatively more important than width in crack

<table>
<caption>TABLE 3 Examples of Triangular Cross-Section Crack Quantification</caption>
<thead>
<tr>
<th>Width (mm)</th>
<th>Depth (%)</th>
<th>$|R|$</th>
<th>$|T|$</th>
<th>Quantified width (mm)</th>
<th>Quantified depth (%)</th>
</tr>
</thead>
<tbody>
<tr>
<td>0.26</td>
<td>40</td>
<td>0.334</td>
<td>0.840</td>
<td>0.282</td>
<td>39.85</td>
</tr>
<tr>
<td>0.45</td>
<td>23</td>
<td>0.141</td>
<td>0.963</td>
<td>0.516</td>
<td>22.70</td>
</tr>
<tr>
<td>0.15</td>
<td>55</td>
<td>0.490</td>
<td>0.675</td>
<td>0.149</td>
<td>55.02</td>
</tr>
<tr>
<td>0.56</td>
<td>22</td>
<td>0.134</td>
<td>0.966</td>
<td>0.635</td>
<td>21.63</td>
</tr>
<tr>
<td>0.67</td>
<td>46</td>
<td>0.415</td>
<td>0.783</td>
<td>0.677</td>
<td>46.01</td>
</tr>
</tbody>
</table>

size quantification, the non-uniqueness of solutions derived from the insuf- ficiency of the input information ($|R|$ and $|T|$ coefficients only) is acceptable, in some sense. Another limitation is that different coefficients surfaces are required for different defect shapes (rectangular, triangular, etc.), so a unified defect model is necessary to improve the generalization and applicability of the quantification method. Beside the above, this method is sensitive to the disturbance of the input parameters, which means the possibility of failing to find a proper solution, so a more robust approach with better error tolerance such as one based on pattern recognition and artificial neural network is suggested as a future research direction by the authors.

## CONCLUSION

The approach presented in this article investigates lateral crack size quantification based on reflection and transmission coefficients surfaces built from numerical simulation results. The quantification examples show that acceptable accuracy could be achieved. Some limitations of this approach are also discussed. There are still many factors to take into account before applying this method to a practical inspection system, considering the complexity in ultrasonic guided wave mechanism.

## ACKNOWLEDGMENTS

This research was financially supported by National Natural Science Foundation of China (Grant No. 10974115).

## REFERENCES

1. B. A. Auld. *Acoustic Fields and Waves in Solids*. Krieger Publishing Company, Malabar, Florida. (1990).
2. J. L. Rose. *Ultrasonic Waves in Solid Media*. Cambridge University Press, New York. (2004).
3. J. L. Rose. *Journal of Pressure Vessel Technology-Transactions of the ASME* **124(3)**:273-282 (2002).
4. D. C. Gazis. *Journal of the Acoustical Society of America* **31**:568-573 (1959).
5. D. C. Gazis. *Journal of the Acoustical Society of America* **51**:573-578 (1959).
6. G. Liu, and J. Qu. *Journal of Applied Mechanics* **65**:424-430 (1998).
7. X. Zhao, and J. L. Rose. *Journal of the Acoustical Society of America* **115**:1912-1916 (2004).
8. J. L. Rose, S. Pelts, and Y. Cho. *Journal of Nondestructive Evaluation* **19**:55-66 (2000).
9. Y. Cho, D. Hongerholt, and J. L. Rose. *IEEE Transactions on Ultrasonics, Ferroelectrics and Frequency Control* **44**:44-52 (1997).
10. Y. Cho, and J. L. Rose. *International Journal of Solids and Structures* **37**:4103-4124 (2000).
11. X. L. Zhao, J. L. Rose, and S. Pelts. *Review of Progress in Quantitative Nondestructive Evaluation, Vols. 21A & B, AIP Conference Proceedings* **615**:196-202 (2002).
12. X. Zhao, and J. L. Rose. *International Journal of Solids and Structures* **40**:2645-2658 (2003).
13. R. B. Thompson. *IEEE Transactions on Sonics and Ultrasonics* **SU-20**:340-346 (1973).
14. R. B. Thompson. *IEEE Transactions on Sonics and Ultrasonics* **SU-25**:7-15 (1978).