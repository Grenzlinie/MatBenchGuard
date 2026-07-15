![](./images/811147802724794369_1.jpg)

Radiation Physics and Chemistry

Radiation Physics and Chemistry 63 (2002) 581-586
www.elsevier.com/locate/radphyschem

# Electron beam process validation for sterilization of complex geometries

Douglas E. Weiss$^{\text{a}}$, Denise A. Cleghorn$^{\text{b}}$, Sam V. Nablo$^{\text{b},*}$

$^{\text{a}}$3M Corporate Research, St. Paul, MN 55144, USA
$^{\text{b}}$Electron Processing Systems, Inc., Executive Park Drive, N. Billerica, MA 01862, USA

## Abstract
The application of low-energy electrons for the disinfection of containers of complex geometries has been limited due to their inability to efficiently penetrate the rigid walls. Most three-dimensional applications have been evaluated using higher energy processors with bulk or through-the-wall treatment. This work has been directed to the validation of electron disinfection of interior surfaces by injecting electrons through the open-mouth of the container. Both direct thin-film dosimetric mapping of the interior and exterior dose distributions for in-line treatment have been conducted and compared with the results of Monte Carlo modeling utilizing $10^{6}$ or more source electron histories. Sterilizer characterization and model assumptions are described and the advantages of the modeling technique for process parameter optimization discussed. © 2002 Elsevier Science Ltd. All rights reserved.

Keywords: Electron sterilization; Dosimetry mapping; Monte Carlo modeling; Dosimetry model correlation

---

## 1. Introduction
The use of compact, self-shielded electron processors for the disinfection and sterilization of containers, particularly those made of thermolabile materials, has been considered for some time (Kotov and Sokovnin, 2000; Nablo et al., 1993; Inai et al., 1999; Nablo, 1987). A major consideration is the high interior dose ratios experienced for "opening restricted" electron injection in order to treat the product contact surfaces. If these ratios become excessive while achieving the requisite minimum dose for the application, then several factors can affect the process: the polymer may be degraded or damaged in the heavily dosed region, at which point extractable limits may be exceeded; the polymer may be softened and deformed; or the container may be affected cosmetically. Hence, it is important to determine acceptable dose ratios so that practicable dose rates can be used for these high-speed applications where container treatment rates of up to 10/s may be encountered. This work has been directed to the validation of such a dynamic sterilization process. This requires the documentation of evidence assuring the process will treat a product to a predetermined level.

Thin radiochromic film (Far West Technology)$^{1}$ was employed for the surface dose mapping. 5 mm wide strips of the film are attached to the inner surfaces of the container, usually by cutting open the container for dosimeter mounting and removal, and taping the container together for irradiation. Static irradiations were used for much of this work although the test system based upon the 250 kV Electrocurtain$^{\text{®}}$ (Energy Sciences, Inc.)$^{2}$ shown in Fig. 1 was used for dynamic trials in which limiting dose rates for various materials can be evaluated at line speeds to 0.67 m/s. The electron window width is 55 mm while its length on this unit is 340 mm.

For the modeling studies, definition of the injected electron current density distribution is important, and

---
*Corresponding author. Tel.: +1-978-667-6366; fax: +1-978-671-0122.
E-mail address: eps@tiac.net (S.V. Nablo).
$^{1}$Far West Technology Inc., 330 D South Kellogg, Goleta, CA 93117.
$^{2}$Electrocurtain is a registered trademark of Energy Sciences Inc., 42 Industrial Way, Wilmington, MA 01877.

0969-806X/02/$-see front matter © 2002 Elsevier Science Ltd. All rights reserved.
PII: S0969-806X(01)00597-7

![](./images/811147802724794369_2.jpg)

Fig. 1. EPS Bottle Sterilizer Test Facility.

this was accomplished again with film dosimetry in order to provide accurate code input. This paper will present data for a 300 ml (10 oz.) bottle, 15 cm high, and a 2.0 l (68 oz.) bottle 27 cm high with internal mouth diameters of 30 and 35 mm, respectively.

The eb source current density distribution mapping is covered in the next section followed by the assumptions used in the Monte Carlo modeling in Section 3. The interior dose mapping for the two containers is then reviewed and compared with the predictions of the model. Process validation work (American National Standard, 1994; Moruzzi et al., 2000) is typically supported by lethality studies in inoculated containers and such a trial is presented in Section 6. The final section illustrates the application of modeling to process optimization.

## 2. Source characterization

The selection of electron energy to ensure adequate air path penetration into these unfilled containers is critical. For example, for the 27 cm depth of the 2 l container, a 240 kV operating voltage was selected which provides a 50% dose point at 30 cm (360 g/m² of air at NTP). Using 50 g/m² FWT-60-00 dosimeters taped to 9 μm aluminum foil strips, current density profiles over the 55 mm window foil width at two longitudinal locations were recorded at its surface, and over 70 mm width at the plane 10 mm from the 12.5 μm thick titanium window. These profiles are shown in Fig. 2 and demonstrate a full-width at half-maximum of 25 and 35 mm, respectively, near optimum for the containers studied here which typically pass 18 mm from the foil surface. The electron scatter leading to these distributions occurs primarily in the window foil so that they are relatively insensitive to source details.

![](./images/811147802724794369_3.jpg)

Fig. 2. Monte Carlo code replication of the electron current density distributions at the 0 mm (foil) and the 12 mm planes.

## 3. Establishing the model for analysis

Mathematical methods for calculation of absorbed dose rate can be used to estimate the absorbed dose delivered to a small volume within the product. The Monte Carlo method used here involves numerically simulating the paths of individual electrons and then estimating dose delivered to a volume in the product by integrating and averaging the histories of many particles. This calculation continues until some acceptable statistical uncertainty in dose is reached. There are a number of examples of Monte Carlo codes described in the literature (Weiss, 2001) but the one selected for use

in this work is ITS (Integrated Tiger Series). This method may be used for very general multidimensional geometries. The physics of electron–electron interaction is sufficiently well understood that models of good accuracy are possible. For our purposes here, we wish to develop an interior dose distribution against which the experimental dosimetric data can be compared. As a result, major simplifications in the container geometry are required to reduce the effort required to build the model description and the computer run times. In the bottle cases, the container is divided into zones for which the average dose at the interior wall surface for each zone can be calculated. Wall geometry simplification was accomplished by smoothing out stiffening ridges or convolutions in walls, particularly for the blow molded polymer bottles using standard cylinder and truncated cone descriptions.

Fig. 3(a) shows the cylinder: cone: cylinder approximation to the actual blow molded bottle shown in Fig. 3(b). The actual dimensions were a $\varphi = 35\mathrm{mm} \times 25\mathrm{mm}$ long neck, a conical section extending to a diameter of $110\mathrm{mm}$ and a uniform, cylindrical flat bottomed geometry to a plane $270\mathrm{mm}$ below the mouth-opening. This reduced the calculation time required to achieve a result with good precision.

For the interior wall dose calculations, a $10\mathrm{\mu m}$ thick annulus of dosimeters was assumed to line the bottle. This was divided into $27 \times 1\mathrm{cm}$ zones vertically and $2\mathrm{cm}$ wide horizontally by constructing a set of intersecting rectangles used to define the individual zones. The rectangles overlapped both sides of the bottle to take advantage of symmetry, permitting each zone to consist of two $1\mathrm{cm} \times 2\mathrm{cm}$ area ($0^{\circ}$ and $180^{\circ}$). The wall dose calculations show the dose levels starting in the top 36 subzones at $100\mathrm{kGy}$, and then working in $1\mathrm{cm}$ steps down through the remaining $26 \times 36=936$ subzones. These calculated values of the dose delivered to the inner $10\mathrm{\mu m}$ depth of the 2 l bottle wall are shown for every second subzone in column 2 of Table 1. A similar model was established for the $300\mathrm{ml}$ bottle, which was $60\mathrm{mm}$ in diameter with a $30\mathrm{mm}$ diameter by $15\mathrm{mm}$ deep cylindrical mouth. These data are shown in column 5 of Table 1. Shifting the stack of rectangles from $0$–$180^{\circ}$ to $90$–$270^{\circ}$ allowed the calculation of the “lateral (with respect to the eb window) set” of dosimeters. The result did not deviate significantly from the “longitudinal set” indicating good uniformity in dose distribution around the interior circumference of the bottle.

### 4. Interior dose mapping
Strips of film dosimetry, $5\mathrm{mm}$ wide $\times 10\mathrm{\mu m}$ in thickness, were attached to the interior walls of the 2 l bottle at $0$–$180^{\circ}$ and $90$–$270^{\circ}$ with respect to the longitudinal axis of the beam. The bottle was sectioned at $45$–$225^{\circ}$, and re-closed and sealed with electron opaque tape after positioning the filmstrips at the $0^{\circ}$ and

![](./images/811147802724794369_4.jpg)

![](./images/811147802724794369_5.jpg)

Fig. 3. (a) Model of the 2-l container and (b) The 2-liter blow molded container.

<table>
<caption>Table 1
Interior wall Monte Carlo calculations and film dosimetry measurements for through-the-mouth electron sterilization at 240 keV</caption>
<thead>
<tr>
<th colspan="3">2 l bottle</th>
<th colspan="3">0.3 l bottle</th>
</tr>
<tr>
<th>Zone no.</th>
<th>Dose calculation</th>
<th>Dose measured</th>
<th>Zone no.</th>
<th>Dose calculation</th>
<th>Dose measured</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>991</td>
<td>a</td>
<td>1</td>
<td>137</td>
<td>125</td>
</tr>
<tr>
<td>3</td>
<td>231</td>
<td>230</td>
<td>2</td>
<td>113</td>
<td>110</td>
</tr>
<tr>
<td>5</td>
<td>105</td>
<td>100</td>
<td>3</td>
<td>65</td>
<td>42</td>
</tr>
<tr>
<td>7</td>
<td>62</td>
<td>55</td>
<td>4</td>
<td>41</td>
<td>30</td>
</tr>
<tr>
<td>9</td>
<td>37</td>
<td>36</td>
<td>5</td>
<td>28</td>
<td>21.5</td>
</tr>
<tr>
<td>11</td>
<td>47</td>
<td>18</td>
<td>6</td>
<td>21</td>
<td>17</td>
</tr>
<tr>
<td>13</td>
<td>42</td>
<td>26</td>
<td>7</td>
<td>15</td>
<td>15</td>
</tr>
<tr>
<td>15</td>
<td>30</td>
<td>25</td>
<td>8</td>
<td>15</td>
<td>14</td>
</tr>
<tr>
<td>17</td>
<td>22</td>
<td>16</td>
<td>9</td>
<td>13</td>
<td>12.7</td>
</tr>
<tr>
<td>19</td>
<td>16</td>
<td>15</td>
<td>10</td>
<td>11.3</td>
<td>12</td>
</tr>
<tr>
<td>21</td>
<td>13</td>
<td>10</td>
<td>11</td>
<td>9.6</td>
<td>9.5</td>
</tr>
<tr>
<td>23</td>
<td>12</td>
<td>10</td>
<td>12</td>
<td>8.5</td>
<td>8.5</td>
</tr>
<tr>
<td>25</td>
<td>9</td>
<td>7</td>
<td>13</td>
<td>6.9</td>
<td>8</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>14</td>
<td>6.1</td>
<td>7.3</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>15</td>
<td>5.4</td>
<td>7.3</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="6">aExceeded film range.</td>
</tr>
</tfoot>
</table>

![](./images/811147802724794369_6.jpg)

Fig. 4. Experimental dosimetric and Monte Carlo predictions at 240 kV, for the 2 l container.

90° planes along the sidewalls. Dosimeters were located at 72° intervals in the bottle bottom positioned in the bottom of each of these 5 stiffening depressions in the bottle bottom. A 240 kV dose distribution at the 0° location is shown in Fig. 4, illustrating a 12:1 dose ratio from the curved section at the 5 cm plane to the bottom sections at 27 cm. Detailed mapping of the upper neck region was conducted at reduced electron fluences in order to prevent radiochromic film saturation so that a complete picture of the dose distribution up to the top (0 cm) location and down the accessible exterior surface was collected. The measured data are shown in column 3 of Table 1 for the 2 l bottle.

![](./images/811147802724794369_7.jpg)

Fig. 5. Experimental dosimetric and Monte Carlo predictions at 240 kV for the 10 oz. glass bottle.

For the 300 ml glass bottle, strips of film dosimeters were positioned along the interior surface and taped with the use of forceps so that dose determinations could be made continuously down the 15 cm deep side walls and across a bottom diameter. As with the larger container, a 240 kV source setting was used although a much lower (<200 kV) energy would suffice for this container. We did not change the energy because half-angles of scatter in the foil vary with energy, and we did not wish to re-characterize the source whose scattering properties are critical to this application. The measured data are given for the 16 zones in column 6 of Table 1 and the data shown in Fig. 5, illustrating a 10:1 dose ratio from the 2.5 cm plane to the bottom at 15 cm at 240 keV.

### 5. A reconciliation of the experimental data with the prediction of the analytical model

For the 2 l container, one would expect the greatest divergence of model: experiment in the convoluted upper region from 0 to 110 mm, the latter plane marking the beginning of the 160 mm deep cylindrical region. As shown in Fig. 3(b), stiffening convex contours in the polyester at the 45 and 85 mm planes are separated by a 75 mm diameter concave contour at the 65 mm plane,

which serves to "shadow" the regions below. This shielded depression in the measured dose is seen to extend down to the 130mm plane from the data of Fig. 4, from which point the agreement of experiment with the model is excellent. The elevation of dose at the 65mm plane of minimum diameter is shown by the experimental data. The model however, with its conical upper section truncated at the 100mm plane, shows a rapid decrease in dose in its lower section and then an elevation in wall dose at this transition to the cylindrical section. The most important part of the model's predictions is, of course, the location of the minimum dose and its relationship to the measured dose at the mouth plane. Although not shown here, the measured dose profile across the bottom diameter is very flat $( \pm 5 \%)$ and depth: dose determinations made at that plane, when corrected for air path, show excellent agreement with an assumption of illumination by elastically scattered primary electrons, not, as expected, by multiply scattered secondaries.

The agreement of the experimental and modeled distributions for the 300ml bottle was excellent as shown in Fig. 5. Once again the truncated conical assumption for the upper region from 15mm to the top of the cylindrical region at the 60mm plane resulted in an overestimate of modeled dose from the measured distribution over this convex region. Excellent agree- ment is then shown along the cylindrical wall from the 70mm plane to the bottom 150mm plane. As with the 21 case, the bottom diametric profile is flat and not shown here.

## 6. Process verification
An evaluation of the ability to determine sterilization treatment levels, now offered by this understanding of the bottle's internal dose distribution, was conducted in the 21 container. An inoculum cocktail of yeasts and molds (*Saccharomyces* sp., *Penicillium* sp., and *Mucor* sp.) was evaluated under good geometry electron beam treatment and was shown to have a combined $D_{10}$ value of 0.5 kGy.

A screening test was then performed with 14 inoculated 21 containers in which the inoculum was distributed uniformly in the bottle interior and dried, at levels of $9 \times 10^{6}$ cfu (colony forming units) and $1.3 \times 10^{5}$ cfu. Four treatment levels providing bottom corner minimum doses of 2.0-5.8 kGy were then applied and the results shown in Table 2.

These data illustrate the ability to predict the dose required to give a predetermined log count reduction (LCR) given good knowledge of the minimum dose regions in the container interior. Typical aseptic proces- sing would require LCR levels of 6.0 or a microbial population reduction of $10^{-6}$.

<table>
<caption>Table 2<br>Inoculum lethality verification</caption>
<thead>
<tr>
<th>Min dose (kGy)</th>
<th>Inoc. level (cfu)</th>
<th>Log count reduction (experimental)</th>
<th>Log count reduction (calculated)</th>
<th>Survivors</th>
</tr>
</thead>
<tbody>
<tr>
<td>5.8</td>
<td>$9 \times 10^{6}$</td>
<td>&gt; 7.0</td>
<td>11.7</td>
<td>0</td>
</tr>
<tr>
<td>5.8</td>
<td>$1.3 \times 10^{5}$</td>
<td>&gt; 5.1</td>
<td></td>
<td>0</td>
</tr>
<tr>
<td>4.5</td>
<td>$9 \times 10^{6}$</td>
<td>6.9</td>
<td>9.0</td>
<td>2</td>
</tr>
<tr>
<td>4.5</td>
<td>$1.3 \times 10^{5}$</td>
<td>&gt; 5.1</td>
<td></td>
<td>0</td>
</tr>
<tr>
<td>2.9</td>
<td>$9 \times 10^{6}$</td>
<td>5.3</td>
<td>5.8</td>
<td>85</td>
</tr>
<tr>
<td>2.9</td>
<td>$1.3 \times 10^{5}$</td>
<td>&gt; 5.1</td>
<td></td>
<td>0</td>
</tr>
<tr>
<td>2.0</td>
<td>$9 \times 10^{6}$</td>
<td>4.9</td>
<td>4.0</td>
<td>130</td>
</tr>
<tr>
<td>2.0</td>
<td>$1.3 \times 10^{5}$</td>
<td>&gt; 5.1</td>
<td></td>
<td>0</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 3<br>Model dose ratio calculations</caption>
<thead>
<tr>
<th>Bottle volume (ml)</th>
<th>Neck:bottom (300 kV)</th>
<th>Neck:bottom (240 kV)</th>
<th>Neck:bottom (200 kV)</th>
</tr>
</thead>
<tbody>
<tr>
<td>300</td>
<td>13:1</td>
<td>22:1</td>
<td>42:1</td>
</tr>
<tr>
<td>2000</td>
<td>55:1</td>
<td>124:1</td>
<td>$\infty$</td>
</tr>
</tbody>
</table>

## 7. Process optimization
There are clearly several limitations to the dose ratios practicable for such a process. The ability of the model to simulate the dose distributions delivered as a function of electron energy is an important asset in selecting the energy which provides the best compromise of shielding geometry and weight, requisite treatment duration and container cosmetic/physical response for a given LCR. Some examples of voltage dependence are illustrated in Table 3 for the two container geometries based upon the Monte Carlo models presented here.

Minimum interior doses will range from 2 to 10 kGy for container treatment depending upon the microbial challenge. Hence, neck: bottom dose ratios much above 50:1 may begin to impose excessive dose levels in the neck region in order to realize the LCR required for the application.

Because of the high dose ratios encountered in these applications one must be careful of the response range of the dosimeter film used for mapping work. We have found the modeling technique described here to be very effective in detecting errors in dosimetry due to such saturation effects.

## 8. Conclusion
Monte Carlo modeling techniques for the container geometries used in consumer products can provide

detailed information on the electron beam delivered dose distributions to the product contact surfaces. Such data is often difficult and laborious to obtain by pure dosimetry. Once verified (Nablo and Cleghorn, 2001), a model can be used to efficiently screen a wide range of bottle geometries and identify an optimum electron energy before committing to a dosimetry verification experiment. Knowledge of the minimum dose points can greatly simplify the validation process, particularly since spot inoculation trials can now be employed.

## Acknowledgements

The authors acknowledge the assistance of Dana Cunniff and Pamela Kazama of Ocean Spray Cranberries, Inc., Lakeville, MA. in performing the inoculated container studies described here.

## References

American National Standard, 1994. Sterilization of health care products-requirements for validation and routine control- radiation sterilization. ANSI/AAMI/ISO 11137, Association for the Advancement of Medical Instrumentation, Arlington, VA.

Inai, T., Akai, T., Iwano, F., Yamamato, E., Ueda, M., 1999. Sterilization treatment for tubular packaging material. Japanese Patent Hei, 11-35015.

Kotov, Y.A., Sokovnin, S.Y., 2000. Overview of the application of nanosecond electron beams for radiochemical sterilization. IEEE Trans. Plasma Sci. 28, 133-136.

Moruzzi, G., Garthright, W.E., Floros, J.D., 2000. Aseptic packaging machine pre-sterilization and package sterilization: statistical aspects of microbiological validation. Food Control 11, 57-66.

Nablo, S.V., 1987. Electron beam irradiation sterilization process. US Patent 4,652,763, March 24.

Nablo, S.V., Cleghorn, D.A., Fletcher, P.M., 1993. Dose distributions for containers electron sterilized at energies from 150-250 keV. Radiat. Phys. Chem. 42, 827-831.

Nablo, S.V., Cleghorn, D.A., 2001. Technique for interior electron sterilization of an open mouthed container. USP. 6,221,216 and foreign patents pending, Electron Processing Systems Inc., N. Billerica, MA 01862 (April 24).

Weiss, D.E., 2001. Standard guide for selection and use of mathematical methods for calculating absorbed dose in radiation processing applications. Draft Standard E10.01-Δ; ASTM, 100 Barr Harbor Dr., Conshohocken, PA 19428.