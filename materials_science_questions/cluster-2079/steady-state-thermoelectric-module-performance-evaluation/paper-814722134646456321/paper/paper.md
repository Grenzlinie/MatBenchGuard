# Light-concentration characteristic of water lens and its application to thermoelectric generation

Keita O. Ito¹, Hongtao Sui¹, Hidetoshi Hakozaki², Hiroshi Kinoshita²,
and Ryosuke O. Suzuki¹, ³

¹Division of Materials Science and Engineering, Faculty of Engineering, Hokkaido University
²Department of Mechanical Engineering, Fukushima National College of Technology
³CREST (Core Research of Evolutional Science & Technology) researcher,
Japan Science and Technology Agency (JST)

**Keywords:** thermoelectric generation; water lens; light condensing; temperature distribution

**Abstract.** A water lens was used to concentrate sunlight on the surface of a thermoelectric (TE) module in order to heat it. The shape of this water lens could be flexibly adjusted to compensate for solar altitude changes. The light condensed by the water lens produced a large energy distribution on the top of the module. In this study, we simulated the power generation properties when the top of the module was heated by light with a certain condensing distribution. The simulation results revealed that the energy distribution had little effect on the TE generation if the solar light was effectively condensed on a plate with a condensing width of a few millimeters.

## Introduction
Solar energy is a clean source of energy. Thus, power generation using solar cells has been widely studied. Photovoltaic solar cells can effectively convert solar energy into electrical energy. However, the power generation of a solar cell is less effective in the infrared region, which contains approximately 50% of the solar energy. Therefore, infrared rays have been separated and used as a heat source for thermoelectric (TE) power generation [1–3]. In order to generate electricity using a heat source with a low energy density, such as solar heat [4,5], it is considerably effective to condense the heat. The use of a mirror or lens is a standard method for condensing solar heat. However, a solar tracking system is needed to obtain a high condensing ratio with these methods. We investigated the possibility of using the refraction of water as a new method for condensing heat. This system could be easily constructed anywhere in the world because its components, water and a plastic sheet, are inexpensive and easily obtained. The condensing position of the *water lens* [6,7] can be adjusted to compensate for solar altitude variations without moving the position of the lens. Instead of mechanical movement, the tensile stress of the transparent sheet and the amount of water are controlled. Some previous experiments and simulations using water lenses examined methods for adjusting the lens shape and condensing position in response to the solar position [6,7]. Although previous papers revealed that a high condensing ratio could be obtained by optimally moving the focusing position of the condensing plate, this study examined the condensing distribution on the surface of a module assuming that both the lens shape and condensing position were optimally controlled. To simplify the analysis, the applicability of a half-cylindrical water lens was considered. The purpose of this work was to show the condensing distribution of the solar light passing through the water lens and demonstrate its applicability to solar light–thermoelectric conversion.

All rights reserved. No part of contents of this paper may be reproduced or transmitted in any form or by any means without the written permission of Trans Tech Publications, www.ttp.net. (ID: 128.210.126.199, Purdue University Libraries, West Lafayette, USA-28/05/15,17:31:36)

## Analysis Procedure

Condensing Property of the Water Lens. In comparison to a normal lens, a water lens has wider energy distribution or dispersion. As an example, we simulated this distribution on the surface of a TE module when light was irradiated on the surface of a 0.2-m-wide water lens. We assumed that the light was condensed on the surface of a 2.5-mm-wide module. This condition was analyzed using the method reported in a previous paper [7]. A condensing ratio of approximately 68 could be achieved when both the lens shape and condensing position were optimally controlled. Fig. 1 shows the light path under these optimal conditions, where the tensile angle applied to both ends of the plastic sheet, $\beta$, was $34.5^\circ$ to the horizontal, and the distance between the water surface and the top of the TE module, $d$, was 0.36 m. The condensing profile on the top surface of the module under these conditions showed sharp condensation peaks close to both edges, as shown in Fig. 2. This same profile was observed at any height. This was because the refraction angles at the outer area of the lens became larger than those at the inner area.

TE Module Modeling and Evaluation Procedure. The light condensed by the water lens had a long rectangular shape, and a TE module was set at this long focus, as shown in Fig. 1. Table 1 lists the temperature dependencies of the material properties and the sizes of the TE elements, electrode, and insulator in reference to a commercial one. The power generation simulations were conducted numerically based on the finite-volume method adding TE phenomena on the commercial software

![](./images/814722134646456321_1.jpg)

Fig. 1 Model of water lens and TE module.

![](./images/814722134646456321_2.jpg)

Fig. 2 Condensing profile on top surface of module.

<table><caption>Table 1 Temperature dependencies of material properties and size (where $T$ is temperature in K)</caption>
<tbody><tr><td></td><td>$p$-type element</td><td>$n$-type element</td><td>electrode</td><td>Insulator</td></tr>
<tr><td>Thermal conductivity,
$\lambda$ [W/(m·K)]</td><td>$0.0000361558T^{2}$
-0.0263513427$T$+6.22162</td><td>$0.0000334545T^{2}$
-0.0233503037$T$+5.606333</td><td>398</td><td>30</td></tr>
<tr><td>Seebeck coefficient,
$S$ [V/K]</td><td>$(-0.0036380957T^{2}$
+2.74380952$T$-296.214286)×$10^{-6}$</td><td>$(0.001530737T^{2}$
-1.08058874$T$-28.338095)×$10^{-6}$</td><td>$2×10^{-6}$</td><td>0</td></tr>
<tr><td>Electrical
conductivity,
$\sigma$ [Sm]</td><td>$(0.0156017327T^{2}$
-15.708052$T$+4466.38095)×$10^{2}$</td><td>$(0.010571437T^{2}$
-10.16048$T$-+3113.71429)×$10^{-6}$</td><td>$6×10^{7}$</td><td>1</td></tr>
<tr><td>Size [$\text{mm}^3$]</td><td>$1.5×1.5×1.6$</td><td>$1.5×1.5×1.6$</td><td>$1.5×1.5×0.3$,
$4×1.5×0.3$</td><td>$30×2.5×0.8$</td></tr>
</tbody></table>

ANSYS FLUENT. The software was modified to simultaneously solve for the TE phenomena, heat balance, and charge conservation under a steady state. The details of this calculation process were reported in our previous papers [8,9]. A value of $1\ \text{kW/m}^2$ (the standard quantity of solar radiation for the evaluation of a solar panel) was assumed for the energy of the light irradiated on the water lens. The heat input to the top of the module was set at $C$ [kW/m²], where $C$ was a condensing ratio. The temperature at the bottom of the module was fixed at 288.15 K. The heat losses from the module surface due to heat transfer and heat radiation were ignored for simplicity.

## Results of Evaluation for TE Generation

Simulations under two conditions were conducted to reveal the influence of the condensing profile on TE generation. In the first condition, the heat input had a certain energy distribution due to the condensation produced by the water lens. In the second, the total heat input was ideal, and the module surface was heated uniformly.

The current–voltage (C–V) curves and current–power (C–P) curves were obtained from these simulations and were approximately same, as shown in Fig. 3. The maximum condensing ratio was approximately three times larger than the average value, as shown in Fig. 2. Therefore, the condensing distribution was sufficiently large to heat the surface inhomogeneously.

Fig. 4 shows the steady-state temperature distribution at the upper part of a cross-section of the TE module, where no TE elements exist below the electrodes. It should be noted that the energy distribution in this analysis was the most largely influenced in the studied models. It is clear that the inhomogeneous heat flux was immediately diffused in an insulator thickness of only a few millimeters. The influence of the heat detour in the receiving plate (insulator) was larger than that of the condensing distribution.

Fig. 5 shows the temperature distribution at the cross-sectional surface of the $p$-type element located near the center of the module. In this cross-section, TE materials exist just below the electrodes, and they carry the penetrated heat to the colder electrode. It is clear that the condensing distribution negligibly affected the temperature profile in this module. Therefore, the small inhomogeneous distribution of heat flux on the top surface of the module smears out as a result of the heat transfer in the module, and it does not have a significant effect. From the viewpoint of industrial application, the inhomogeneous focus of the water lens does not provide any significant response in power generation.

## Summary

Although the water lens could not condense solar light homogeneously, the thermal nonuniformity at the insulator surface was immediately diffused and did not affect the TE-generation performance. As an example, a power output of approximately 70 mW could be achieved using a 0.2-m-wide water lens when perpendicular light was condensed on a 2.5-mm-wide module connected to six pairs of TE elements in series.

![](./images/814722134646456321_3.jpg)

Fig. 3 Comparison of $I$–$V$ and $I$–$P$ curves
simulated under different conditions.

![](./images/814722134646456321_4.jpg)

Fig. 4 Temperature profile at interface between
insulator (A) and electrode (B).

![](./images/814722134646456321_5.jpg)

Fig. 5 Temperature profile at cross-section of element near center of module.

## References

[1] N. Wang, L. Han, H. He, N.H. Park, K. Koumoto, Energy Environ. Sci. 4 (2011) 3676-3679.

[2] X. Ju, Z. Wang, G. Flamant, P Li, W. Zhao, Sol. Energy 86 (2012) 1941-1954.

[3] D. Kraemer, B. Poudel, H. P. Feng, J. C. Carlor, B. Yu, X. Yan, Y. Ma, X. Wang, D. Wang, A. Muto, K. McEnaney, M. Chiesa, Z. Ren, G. Chen, Nature Materials 10 (2011) 532-538.

[4] A. Weidenkaff, M. Trottmann, P. Tomes, C. Suter, A. Steinfeld, A. Veziridis, "Solar TE Converter Applications", in "Thermoelectric Nanomaterials, ed. K. Koumoto and T. Mori (Springer, Heidelberg, 2013) 365-382.

[5] Y. Deng, W. Zhu, Y. Wang, Y. Shi, Sol. Energy 88 (2013) 182-191.

[6] K. O. Ito, H. Sui, H. Hakozaki, H. Kinoshita, and R. O. Suzuki, J. Electron. Mater. DOI:10.1007/s11664-013-2768-8, in press.

[7] R. O. Suzuki, A. Nakagawa, H. Sui, J. Electron. Mater. 42 (2013) 1688-1696.

[8] T. Fujisaka, R. O. Suzuki, Proc of 38th Annual Conference on IEEE Industrial Electronics Society (2012) 5868-5872.

[9] T. Fujisaka, H. Sui, R. O. Suzuki, J. Electron. Mater. 42 (2013) 1688-1696.

Inorganic and Environmental Materials
10.4028/www.scientific.net/KEM.617

Light-Concentration Characteristic of Water Lens and its Application to Thermoelectric Generation
10.4028/www.scientific.net/KEM.617.247

DOI References

[3] D. Kraemer, B. Poudel, H. P. Feng, J. C. Carlor, B. Yu, X. Yan, Y. Ma, X. Wang, D. Wang, A. Muto, K. McEnaney, M. Chiesa, Z. Ren, G. Chen, Nature Materials 10 (2011) 532-538.
http://dx.doi.org/10.1038/nmat3013

[5] Y. Deng, W. Zhu, Y. Wang, Y. Shi, Sol. Energy 88 (2013) 182-191.
http://dx.doi.org/10.1016/j.solener.2012.12.002

[7] R. O. Suzuki, A. Nakagawa, H. Sui, J. Electron. Mater. 42 (2013) 1688-1696.
http://dx.doi.org/10.1007/s11664-013-2483-5

[9] T. Fujisaka, H. Sui, R. O. Suzuki, J. Electron. Mater. 42 (2013) 1688-1696.
http://dx.doi.org/10.1007/s11664-012-2400-3