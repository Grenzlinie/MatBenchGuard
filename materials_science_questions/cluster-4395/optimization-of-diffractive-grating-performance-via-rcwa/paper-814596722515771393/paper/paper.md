# Nanoscale

PAPER

View Article Online
View Journal

![](./images/814596722515771393_1.jpg)

Cite this: DOI: 10.1039/c5nr02988k

Received 7th May 2015,
Accepted 24th August 2015
DOI: 10.1039/c5nr02988k
www.rsc.org/nanoscale

# Using nanoimprint lithography to improve the light extraction efficiency and color rendering of dichromatic white light-emitting diodes†

Yang-Chun Lee, $^{a}$ Hsuen-Li Chen, $^{*a}$ Chih-Yu Lu, $^{a}$ Hung-Sen Wu, $^{a,b}$ Yung-Fang Chou $^{c}$ and Szu-Huang Chen $^{d}$

Despite the efficiency of gallium nitride (GaN)-based blue light-emitting diodes (LEDs), the light extraction arising from the packaging of the phosphor remains an important issue when enhancing the performance of dichromatic white LEDs. In this study, we employed a simple, inexpensive nanoimprinting process to increase both the light extraction efficiency and color rendering of dichromatic white LEDs. We employed the rigorous coupled wave approach (RCWA) to optimize the light extraction efficiency of yellow and blue light. We found that the presence of the light extracting structures could also improve the color rendering of the dichromatic white LEDs, due to the different light extraction efficiencies of the textured structures at different wavelengths. After fabricating inverted pyramid structures on the surface of the encapsulation layer, the intensity of the blue light at 455 nm increased by 20%. When we further considered the color rendering and correlated color temperature (CCT), the enhancement of blue light was 15% and that of yellow light was 4%. Meanwhile, the light extraction of the intensity dip near 490 nm was enhanced significantly (by 25%), resulting in an increased dip-intensity of light at 490 nm relative to the intensities of the blue and yellow light. Accordingly, the color rendering index (CRI) of this dichromatic white LED increased from 69 to 73. Because it improved both the light extraction efficiency and color rendering of dichromatic white LEDs, this simple method should be very helpful for enhancing their applications in solid state illumination.

## Introduction

Light-emitting diodes (LEDs) continue to receive much attention because of their high radiance, long lifetimes, and low energy consumption. Generally, in the field of solid state illumination, conventional LEDs radiate white light through the phosphor-converted (pc) method. $^{1}$ The simplest pc-white LED is a dichromatic white LED comprising a gallium nitride (GaN)-based blue LED and a cerium-doped yttrium aluminum garnet (YAG:Ce) yellow phosphor. Some portion of the blue light from the GaN-based blue LED is down-converted by the YAG:Ce yellow phosphor to generate yellow light; therefore, white light is produced by mixing the blue and yellow light. Although dichromatic white LEDs are the cheapest among the available white LEDs and they perform with acceptable efficiency, the latter requires further improvement if they are to find wider acceptance for general lighting applications.

According to the working principle of pc-white LEDs, the efficiency of a dichromatic white LED is determined by the external quantum efficiency (EQE) of the pumping LED (GaN-based blue LED) and the phosphor-conversion efficiency. $^{2}$ The EQE of a GaN-based blue LED is the product of the internal quantum efficiency and the light extraction efficiency. The phosphor-conversion efficiency is determined by several factors, including the internal quantum efficiency of the phosphor, the down-conversion efficiency, and the light extraction efficiencies of both the short- and long-wavelength light for the packaging of the phosphor. $^{2}$ Among these factors, improving the light extraction efficiencies of the GaN-based blue LED and of the packaging of the phosphor is an important issue when attempting to increase the total efficiency of the dichromatic white LED. At present, most studies are focused on improving the light extraction efficiencies of GaN-based blue LEDs-a process that is limited by the effects of Fresnel

$^{a}$ Department of Materials Science and Engineering, National Taiwan University, Taipei, 10617, Taiwan. E-mail: hsuenlichen@ntu.edu.tw
$^{b}$ Center for Measurement Standards, Industrial Technology Research Institute, Chutung, Hsinchu 31040, Taiwan
$^{c}$ Material and Electro-Optics Research Division, National Chung-Shan Institute of Science and Technology, Longtan, 325, Taiwan
$^{d}$ National Nano Device Laboratories, National Applied Research Laboratories, Hsinchu, Taiwan
† Electronic supplementary information (ESI) available. See DOI: 10.1039/ c5nr02988k

This journal is © The Royal Society of Chemistry 2015
Nanoscale
![](./images/814596722515771393_2.jpg)

reflection and total internal reflection at the GaN-air interface. Therefore, decreasing Fresnel reflection and expanding the critical angle at the GaN-air interface will be necessary. Several approaches have been developed to expand the critical angle at the GaN-air interface; for example, surface roughening through wet chemical etching, $^{3,4}$ dry etching, $^{5-7}$ or the fabrication of heterogeneous random structures comprising zinc oxide (ZnO) $^{8-11}$ or indium tin oxide (ITO) $^{12,13}$ on the surface of the LED to prevent total internal reflection. The application of periodic photonic crystal (PhC) structures is also a common method for expanding the critical angle at the GaN-air interface. $^{14-20}$ Moreover, sub-wavelength antireflective nanostructures have also been employed to minimize Fresnel reflection. $^{21,22}$ In previous studies, we introduced inverted pyramid structures to the surface of GaN-based blue LEDs possessing both optical gradient and diffraction properties to optimize the light extraction efficiency. $^{23}$

Despite the high light extraction efficiency of blue light from GaN, several groups have noted that the light extraction efficiency for the packaging of the phosphor also influences the efficiency of dichromatic white LEDs. $^{24,25}$ Because the refractive index of the encapsulating materials ($n = ca$. 1.5) is higher than that of air, Fresnel reflection and total internal reflection also occur at the encapsulating material-air interface. To increase the light extraction efficiency from the packaging of the phosphor of dichromatic white LEDs, the most commonly applied strategy is packaging with a dome lens. $^{26-28}$ In a dome lens package, hemispherical encapsulation is used such that the light from the pc-LED is incident normally at the encapsulating material-air interface. Based on the geometry of the package, the total internal reflection effect can be minimized. Although the dome lens configuration is helpful to increase the light extraction efficiency, due to its special geometry, the large volume of the lens limits the applications of dichromatic white LEDs in terms of miniaturization of such devices. Moreover, the need to study the efficiency of planar encapsulation has arisen because of the current trend of using multichip LED packages. $^{29}$ Therefore, establishing textured structures on planar encapsulation surfaces, other than dome lens configurations, might be an alternative method for increasing the light extraction efficiency for the packaging of the phosphor. Although several micro- and nano-structures have been applied widely on GaN-based blue LEDs, only a few groups have discussed the light extraction behavior of these structures on the surfaces of encapsulation layers. $^{30-32}$ Chen et al. used imprinting techniques to fabricate randomly textured structures on the surface of the encapsulation layer; $^{31}$ although the luminous efficiency increased by 5.4% compared with that of the flat encapsulation layer, the efficiency of the pc-white LED was not enhanced truly because of the large decrease in the intensity of blue light. Kim et al. prepared an LED lens featuring biologically inspired cuticular nanostructures on the curved surface to increase the transmittance of the lens-air interface; the enhancement in light extraction efficiency was only approximately 3% because they were interested primarily in decreasing the Fresnel reflection at the lens-air interface. $^{32}$

In addition to improvements in efficiency, another important issue when attempting to increase the performance of dichromatic white LEDs is increasing their color rendering index (CRI). $^{33}$ CRI is a measure of the ability to show (or render) the true colors of objects (e.g., fruits, plants, toys, skin, etc.) that are being illuminated by the light source. The test procedure for determining the CRI involves comparison of the appearance of eight color samples under illumination of the tested light source and a reference light source. The reference light is typically that from a Planckian black-body source having the same correlated color temperature (CCT), because natural daylight is closely similar to a Planckian black-body source. The average differences are measured and then subtracted from 100 to give the CRI of the tested light source. $^{34}$ Several approaches have been reported for the preparation of white LEDs with high CRIs, including developing LEDs with dual-blue active layers, $^{35}$ designing multi-chip package white LEDs, $^{36,37}$ co-doping some light-emitting ions into the YAG:Ce phosphors, $^{38,39}$ and the use of multichromatic pc-white LEDs. $^{40,41}$ Although such approaches have realized white LEDs with good color rendering, these methods mainly focus on the complement of the insufficient color in the spectra emitted by multi-chips or various phosphors. In addition, Lai et al. prepared a CCT- and CRI-tuning white LED incorporating three-dimensional non-closely-packed colloidal photonic crystals; although they obtained a warm white LED with an enhanced CRI, the device exhibited decreased efficiency. $^{42}$ To the best of our knowledge, no previous reports have appeared discussing improvements in color rendering through enhancement of light extraction from textured structures on the surface of the encapsulation layer— an approach that would presumably be helpful for further increasing the CRIs of white LEDs under various applications.

In this study, we established a simple, inexpensive, nanoimprinting method for fabricating textured structures on the surface of the encapsulation layer to increase the light extraction efficiency. We employed the three-dimensional (3D) rigorous coupled wave approach (RCWA) to optimize the light extraction efficiency for the packaging of the phosphor of dichromatic white LEDs. Next, we used nanoimprint lithography to fabricate the optimized light extracting structures on the surface of the encapsulation layer. The light output powers of the blue and yellow light could both be improved as a result of decreases in both Fresnel reflection and total internal reflection. Moreover, because of the different light extraction efficiencies of the structures under different wavelengths, these light extracting structures could also be used to improve the color rendering of dichromatic white LEDs. The method established herein should be very helpful for applications in indoor solid state illumination.

## Experimental
### Simulation setup
Fig. 1a and b display the schematic representations of the phosphor-on-cup white LED structure, which consisted of a

![](./images/814596722515771393_3.jpg)

Fig. 1 (a, b) Schematic representations of the phosphor-on-cup white LED (a) with and (b) without periodic textured structures on the surface of the encapsulation layer. (c-f) Detailed diagrams of the four kinds of simulated periodic structures: (c) nanorods, (d) inverted rods, (e) pyramids, and (f) inverted pyramids. Insets: three-dimensional representations of each periodic structure.

GaN-based blue LED chip and a yellow phosphor layer with or without a textured structure on the surface of the encapsulation layer. In this study, polydimethylsiloxane (PDMS) was used as the encapsulation material due to its good thermal stability and resistance from water and oxygen. $^{43,44}$ Because the refractive index of PDMS ($n = ca. 1.45$) is much higher than that of air, Fresnel reflection and total internal reflection occur at the PDMS-air interface, restricting the light extraction of both blue and yellow light from the white LED. To optimize the light extraction efficiency of the packaging of the phosphor in dichromatic white LEDs, the RCWA method was applied to simulate the far-field transmission intensities (transmittances) of the surfaces of encapsulation layers presenting various periodic structures.

Fig. 1c-f present the four kinds of closely-packed periodic structures on PDMS encapsulation layers that were simulated: nanorods, inverted rods, pyramids, and inverted pyramids; the three-dimensional structures are also displayed. The duty ratio of the nanorods and inverted rods was set at 0.5; thus, the rod diameter was half of the period. On the other hand, the pyramids and inverted pyramids were set to be hexagonally closely-packed. The simulated structures featured a flat part and a textured part. The flat part was a PDMS slab of infinite thickness, because reflection from the bottom surface was not considered in our model. The structural parameters included the period and height (or depth), which varied from 200 to 900 nm and from 200 to 1500 nm, respectively. The transmitted intensity was computed in air ($n = 1.0$); therefore, the transmittance of each angle was collected and the total efficiency of the structures was calculated. In the RCWA simulation, the light emitted from the GaN-based LED chip and yellow phosphor was assumed to be a point light source emitting at different angles; the emitting light was randomly polarized. In the simulation model, however, the transmittance could be calculated only for linear polarized light (e.g., s- or p-polarized light); therefore, the transmittance of the randomly polarized light was computed by directly averaging the transmittances of s- and p-polarized light.

After computing the transmittance of the randomly polarized light at different angles of incidence, the light extraction efficiency of a structure was estimated by squaring the average transmittance from 0 to $89^{\circ}$ using the equation:

$$
\text{light extraction efficiency} = \left[ \frac{\sum_{0^{\circ}}^{89^{\circ}} T(\theta)}{90} \right]^2 \tag{1}
$$

where $T(\theta)$ is the transmittance of the incident light at an incident angle $\theta$. In eqn (1), the average transmittance from 0 to $89^{\circ}$ was assumed to be the "2D light extraction efficiency", because it considers only one axis in the polar coordinate $(\theta, \varphi)$. Because the optical behavior of an LED occurs in whole space, the light extraction efficiency was reasonably calculated by squaring the average transmittance to represent the true total extraction efficiency. $^{23}$

The total efficiencies of various structures on the surfaces of the PDMS encapsulation layers were compared and analyzed. The light extraction efficiency of flat PDMS was also calculated as a reference; therefore, the enhancement of each structure could be computed using the equation:

$$
\text{Enhancement} = \frac{\eta_{\text{stru}} - \eta_{\text{ref}}}{\eta_{\text{ref}}} \times 100\% \tag{2}
$$

where $\eta_{\text{stru}}$ is the light extraction efficiency of a structure on the surface of a PDMS encapsulation layer and $\eta_{\text{ref}}$ is the light extraction efficiency of the reference structure (flat PDMS). In addition to calculating the transmitted intensities of these structures at different incident angles, the RCWA simulation could also separately calculate the zero-order transmission (where the angle of the transmission light equalled the angle of the incident light; so-called "direct transmission") and the non-zero-order transmission (so-called "diffracted transmission"). Therefore, we could analyze the extraction behavior of directly transmitted light and diffracted light from the textured structures to optimize the light extraction efficiencies of the structures on the surfaces of the PDMS encapsulation layers.

### Experimental process

Nanoimprint lithography was used to fabricate periodic structures on the surfaces of PDMS encapsulation layers to enhance the light extraction efficiency of the packaging of the phosphor. To prepare the phosphor-on-cup white LED, a two-step

![](./images/814596722515771393_4.jpg)

Fig. 2 Schematic representations of the processes used for fabrication of dichromatic white LEDs with textured phosphor layers.

curing procedure was used to fabricate the textured phosphor layer (Fig. 2). First, we mixed the PDMS pre-polymer (base) and its cross-linker (curing agent) at a 10:1 weight ratio, under magnetic stirring. Then, YAG:Ce yellow phosphor (HEFA Rare Earth Canada) was added slowly to the PDMS pre-polymer and cross-linker mixture to prevent the agglomeration of phosphors.

Here, the phosphor concentration was 53 weight percent for the preparation of a dichromatic white LED with a CCT of approximately 5500 K. After further stirring for 30 min, the mixture of phosphor and PDMS was spin-coated on a polycarbonate (PC) substrate and then thermally cured at 150 °C for 20 min on a hot plate. Next, a layer of uncured PDMS was spin-coated on the surface of the cured phosphor-packaged PDMS layer. A silicon mold, possessing periodic structures fabricated using standard photolithography, was attached directly to the uncured PDMS layer at room temperature, and a small pressure of 0.005 MPa was applied during the imprinting process to avoid the formation of air bubbles. The periodic structures of the silicon molds were the inverse structures of the structures designed in the RCWA simulations. After thermally curing at 150 °C for 20 min, the textured phosphor layer was released from the silicon mold. Finally, the textured phosphor layer was attached to a commercial GaN-based blue LED to form a phosphor-on-cup dichromatic white LED. To characterize the textured phosphor layer, the emitted spectra of the white LED were collected by using a spectrometer system equipped with an integrating sphere. The morphology of the silicon mold was observed using thermal field emission scanning electron microscope (FESEM, JEOL JSM 6500-F). Atomic force microscope (AFM, Veeco Dimension D-5000) was also used to view the structures on the surfaces of the textured phosphor layers.

# Results and discussion

Based on the working principle of a pc-white LED, the phosphor-conversion efficiency can be calculated using the equation²

$$
\mathrm{Phosphor\text{-}conversion\ efficiency} = t \cdot \eta_{\mathrm{LEE,pump}} + (1 - t)\eta_{\mathrm{QE,ph}} \frac{\bar{E}_{\mathrm{ph}}}{\bar{E}_{\mathrm{pump}}} \eta_{\mathrm{LEE,ph}} \tag{3}
$$

where $t$ is the portion of the unabsorbed blue light; $\eta_{\mathrm{LEE,pump}}$ is the light extraction efficiency of the pumping blue light from the packaging of the phosphor; $\eta_{\mathrm{QE,ph}}$ is the internal quantum efficiency of the phosphor; $\bar{E}_{\mathrm{ph}}$ and $\bar{E}_{\mathrm{pump}}$ are the photon energies of the down-converted yellow light and pumping blue light, respectively; and $\eta_{\mathrm{LEE,ph}}$ is the light extraction efficiency of the yellow light from the packaging layer of the phosphor. According to eqn (3), because the yellow light was generated by down-converting the blue light through the yellow phosphor, the down-conversion efficiency would always be fixed at approximately 82% (the ratio of the wavelengths of blue and yellow light). Moreover, the internal quantum efficiency of the phosphor is only in the range from approximately 12 to 75%.⁴⁵⁻⁴⁸ Therefore, the light extraction efficiency of yellow light for the packaging of the phosphor is much more important than that of blue light to alleviate this down-converting loss. To increase the phosphor-conversion efficiency of dichromatic white LEDs, the light extraction efficiency of the yellow light for the packaging of the phosphor should first be considered.

Fig. 3a displays the measured emitted spectrum of the dichromatic white LED without any textured structure on the surface. As mentioned above, the spectrum of dichromatic white LED featured a sharp peak of blue light located at a wavelength of 455 nm and a broad spectral bandwidth of yellow light with its peak located near 550 nm. To optimize the light extraction efficiency of yellow light for packaging of the phosphor, we first simulated the transmission intensity at a

![](./images/814596722515771393_5.jpg)

Fig. 3 (a) Measured emitted spectrum of the dichromatic white LED. (b) Simulated transmittances on a flat LED at wavelengths of 455 and 550 nm for various angles of incidence.

wavelength 550 nm of a flat PDMS slab in the absence of peri- odic structures. We also computed the transmission intensity of the same simulated model at a wavelength of 455 nm. Fig. 3b displays the simulated transmittances of randomly polarized light at wavelengths of 455 and 550 nm under different angles of incidence. For incident angles less than the critical angle of the PDMS-air interface (ca. $41.7^{\circ}$ for a wave length of 455 nm; ca. $42.2^{\circ}$ for a wavelength of 550 nm ), the reflectance was approximately 4% as a result of Fresnel reflec- tion. When the incident angle of the light was greater than the critical angle, the transmittance decreased dramatically to zero as a result of total internal reflection. Therefore, to increase the light extraction efficiency of the yellow light for the packa- ging of the phosphor, we required a textured structure that could decrease both the Fresnel reflection and the total internal reflection.

To optimize the light extraction ability for yellow light of different kinds of textured structures at the PDMS-air inter- face, we simulated the transmission intensities and calculated the light extraction efficiencies of structures having different periods and depths on the surface of PDMS. Fig. 4 presents contour diagrams of the light extraction efficiency enhance- ments of nanorods, inverted rods, pyramids, and inverted pyr- amids having periods ranging from 200 to 900 nm and depths ranging from 200 to 1500 nm. First, we observe that the light extraction efficiency enhancement depended strongly on the structural parameters. The structures providing higher enhancements in these contour diagrams had periods mostly located in the region from 400 to 500 nm, especially for the pyramid and inverted pyramid structures. Moreover, the enhancement in the light extraction efficiency of the inverted pyramid structures was the highest among the four kinds of the periodic structures that we tested. Table 1 lists the highest extraction efficiency enhancement of yellow light for each of the four kinds of structures. Table 1 also lists the extraction efficiency enhancements of these structures under blue light, because the structures on the surface of the encapsulation layer also influenced the optical behavior of blue light from the pumping LED. The simulations suggested that the opti- mized extraction efficiency of yellow light could be achieved by positioning inverted pyramids having a period of 500 nm and a depth of 900 nm at the PDMS-air interface, providing an enhancement of 24.5% for yellow light and 13.7% for blue light.

![](./images/814596722515771393_6.jpg)

Fig. 4 Contour diagrams of the simulated light extraction efficiency enhancements at a wavelength of 550 nm of (a) nanorods, (b) inverted rods, (c) pyramids, and (d) inverted pyramids, for periods ranging from 200 to 900 nm and depths ranging from 200 to 1500 nm.

<table><caption>Table 1 Structural parameters of some textured structures designed for yellow light; the enhancement in the light extraction efficiency of blue light is also listed</caption>
<thead>
  <tr>
    <th>Structure</th>
    <th>Blue light (455 nm)</th>
    <th>Yellow light (550 nm)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Nanorod<br>Period 400 nm<br>Depth 900 nm</td>
    <td>4.34%</td>
    <td>12.1%</td>
  </tr>
  <tr>
    <td>Inverted rod<br>Period 400 nm<br>Depth 1100 nm</td>
    <td>13.07%</td>
    <td>16.89%</td>
  </tr>
  <tr>
    <td>Pyramid<br>Period 400 nm<br>Depth 1100 nm</td>
    <td>16.45%</td>
    <td>20.75%</td>
  </tr>
  <tr>
    <td>Inverted pyramid<br>Period 500 nm<br>Depth 900 nm</td>
    <td>13.74%</td>
    <td>24.52%</td>
  </tr>
</tbody>
</table>

To understand the light extraction behavior of the different textured structures, we performed a detailed diffraction inten- sity analysis of the various structures. The zero-order transmit- tance and non-zero-order (diffraction order) transmittance could be calculated separately by the RCWA method, allowing us to analyze the light extraction behavior of each of these structures. The total transmittance was the sum of the zero- order and non-zero-order transmittances. Fig. 5 displays the simulated transmissions of the nanorods and inverted pyra- mids having a depth of 900 nm, but different periods, at each angle of incidence. The depth of the structures was fixed because the light extraction efficiency of the structure on the PDMS surface was only slightly dependent on the structural depth, as observed in Fig. 4; the structural period had a much more significant influence. Fig. 5a, b, d and e display the extraction transmissions of the zero-order and diffraction order of light for nanorod and inverted pyramid structures having a depth of 900 nm and various periods, at various angles of incidence. In Fig. 5a and d, we observe that the zero- order transmittance decreased dramatically to zero at angles of incidence of greater than $42.2^{\circ}$ (the critical angle of the PDMS-air interface), representing the effect of total internal reflection. Upon increasing the period, the zero-order trans- mittances decreased, whether the structure featured nanorods or inverted pyramids. In Fig. 5b and e, however, we observe the opposite phenomenon for the diffraction order transmission from the zero-order transmission upon increasing the period.

![](./images/814596722515771393_7.jpg)

Fig. 5 Simulated (a) zero-order, (b) non-zero-order, and (c) total trans- mittances of nanorod structures and (d) zero-order, (e) non-zero-order, and (f) total transmittances of inverted pyramid structures having a depth of 900 nm and various periods, plotted with respect to the inci- dent angle, at a wavelength of 550 nm. Insets: schematic represen- tations of the textured structures.

First, we could not observe the diffraction order transmission when the period was 200 or 300 nm at any angle of incidence, due to the sub-wavelength periodicity in these cases. When the period increased to 400 nm, the diffracted transmittance began to increase from zero at an incident angle of $35^{\circ}$. The diffracted transmittance existed even when the angle of inci- dence was larger than the critical angle $(42.2^{\circ})$. Therefore, diffraction of light was the key factor for expanding the critical angle of the PDMS-air interface and, thereby, decrease the total internal reflection. When we increased the period of the textured structure further, diffraction occurred at normal inci- dence when the period of the textured structure was larger than the wavelength of light. The diffraction behavior observed above can be modeled using the diffraction eqn (4)

$$
n_{2} \sin \theta_{m}=n_{1} \sin \theta_{\mathrm{i}}+m \frac{\lambda}{P} \tag{4}
$$

where $n_{1}$ and $n_{2}$ are the refractive indices of medium 1 and 2, respectively; $\theta_{\mathrm{i}}$ is the angle of incidence; $\theta_{m}$ is the diffraction angle of the $m$-th order $(m=0, \pm 1...)$ diffracted light; $\lambda$ is the wavelength of light; and $P$ is the period of the textured struc ture. In summary, upon increasing the period of the textured structure, the zero-order transmittances of the nanorods and inverted pyramids decreased, whereas the diffracted transmit- tances increased. We attribute the decrease in zero-order trans- mittance to the incident light being diffracted as higher orders of diffracted light. Because the diffracted light at incident angles greater than the critical angle would be helpful to expand the critical angle of the PDMS-air interface, there exists a trade-off between the zero-order transmission and the diffracted transmission to optimize the structural period of these periodic textured structures. As a result, we calculated the total transmittances for nanorods and inverted pyramids having various periods at different angles of incidence (Fig. 5c and f, respectively). We found that the areas under the curves were largest for the periodic textured structures having a period in the range from approximately 400 to 500 nm. From the simulation data, we concluded that optimized enhance- ment of the light extraction efficiency would be achieved when applying an inverted pyramid structure having a period of approximately 400-500 nm on the surface of the PDMS encap- sulation layer. Moreover, we employed the same optimization process for the light extraction behavior toward blue light of the different kinds of periodic structures at the PDMS-air interface; a detailed discussion can be found in the ESI.†

According to our simulations, the inverted pyramid struc- ture having a period of 500 nm and a depth of 900 nm was the optimal structure for the extraction of yellow light from the packaging of the phosphor to improve the efficiency of the dichromatic white LEDs. As mentioned above, however, the CRI should be increased to enhance the performance of the dichromatic white LED if it is to be applied for solid state illu- mination. Because evaluation of CRIs is conducted by compar- ing the appearance of eight standard color samples under illumination from a tested light source and a reference Planck- ian black-body source having the same CCT as the test source, the simplest strategy for achieving a high-CRI light source is to produce a light source having a spectrum close to that of a Planckian black-body source. Fig. 6a presents the emitted light spectra of a dichromatic white LED having a standard CCT of 5500 K and of a Planckian black-body source (5500 K). Based on the working principle of a dichromatic white LED, the spec- trum of the LED featured two peaks of light, at wavelengths of455 and 550 nm. The intensity dip in the spectrum at a wave- length of 490 nm restricted the CRI of the dichromatic white LED (CRI = ca. 69). Therefore, to increase the CRI of the dichromatic white LED, we had to increase the relative inten- sity of the light located near the intensity dip of 490 nm. Fig. 6b displays the calculated enhancement spectrum of the light extraction efficiency of the inverted pyramid structures having a period of 500 nm and a depth of 900 nm in the visible regime. We observe that the enhancement in light extraction efficiency depended strongly on the wavelength of incident light. The enhancement in light extraction was the highest for yellow light having a wavelength of 550 nm, due to the optimized optical gradient and diffraction behavior, as determined through RCWA simulation. When the wavelength of the incident light was far from the designed wavelength, the light extraction efficiency would decrease significantly. As a

![](./images/814596722515771393_8.jpg)

![](./images/814596722515771393_9.jpg)

Fig. 6 (a) Emitted light spectra from the dichromatic white LED and a Planckian black-body source having a standard CCT of 5500 K. (b) Cal- culated enhancement spectrum of the light extraction efficiency of the inverted pyramid structure having a period of 500 nm and a depth of 900 nm.

result, the enhancement in light extraction at 490 nm (ca. 20%) was larger than that at 455 nm (ca. 14%). On the other hand, although the enhancement in light extraction at a wave- length of 490 nm was slightly lower than that at 550 nm, the enhancement in extracted blue light means that less yellow light would be generated by the phosphor. Therefore, we sus- pected that the intensity of light at 490 nm relative to those of the blue and yellow light might be increased by adding the tex- tured structure, thereby helping to increase the CRI of the dichromatic white LED.

To verify the light extraction efficiency enhancement for the packaging of the phosphor, we used nanoimprint lithography to fabricate the inverted pyramid structure on the surface of the PDMS encapsulation layer. Fig. 7a and b display SEM images (top and cross-sectional views, respectively) of the tex- tured silicon mold. The periodic structure on the silicon mold was a pyramid structure having a period of 500 nm and a depth of 900 nm, because the imprinted structure on the PDMS surface was by necessity the inverse structure of the silicon mold. After depositing the package of the first phos- phor layer, the second layer featuring the designed textured structure was fabricated by applying the nanoimprint process (Fig. 2). Fig. 7c displays an AFM image of the surface of the tex- tured PDMS encapsulation layer. From the top view image and the cross-sectional analysis, the measured structural depth on the PDMS surface was only approximately 600 nm because of the difficulty of preparing such a high-aspect-ratio structure.

![](./images/814596722515771393_10.jpg)

Fig. 7 (a) Top-view and (b) cross-sectional view SEM images of the tex- tured silicon mold fabricated using photolithography. (c) AFM images of the surface of the textured PDMS encapsulation layer.

The large enhancement region in the contour diagrams of the light extraction efficiency (red region in Fig. 4d) means that the fabricated structure remained located within the large enhancement region of the inverted pyramid structure. There- fore, we anticipated that the light extraction efficiency of both yellow and blue light would be enhanced effectively.

After fabricating the textured structure on the LED, we used a spectrometer system equipped with an integrating sphere to collect the emitted spectra from the dichromatic white LED (incorporating the textured phosphor layer on a GaN-based blue LED) to examine the enhancement in the phosphor- conversion efficiency. Fig. 8 displays the emitted spectra from the dichromatic white LED before and after adding the inverted pyramid structure on the surface of the PDMS encapsulation layer. When the textured structure was present, the intensity of the blue light at 455 nm was enhanced by approximately 20%

![](./images/814596722515771393_11.jpg)

Fig. 8 Emitted spectra from the dichromatic white LED in the absence and presence of the inverted pyramid structure on the surface of the PDMS encapsulation layer.

due to the enhancement of light extraction efficiency (see Fig. S2 in the ESI†). This enhancement was larger than our predicted value from the simulations, presumably because of the formation of a rough surface on the PDMS encapsulation layer during the process of imprinting, potentially helping to increase the light extraction efficiency. The intensity of the yellow light at 550 nm, however, increased by only 2%, a value that was much lower than the simulated extraction enhancement. We attribute this low enhancement to the working principle of the dichromatic white LED. When the textured structures were present on the surface of the PDMS encapsulation layer, the enhancement in the light extraction efficiency of blue light meant that more blue light could transmit directly through the PDMS-air interface. Meanwhile, less blue light could be absorbed by the phosphors, resulting in less yellow light being generated through down-conversion from the blue light. Therefore, the intensity of the yellow light from the white LED featuring the textured phosphor layer could not be enhanced as predicted. Next, we focused on the CRI of the white LED incorporating the designed inverted pyramid structure. In Fig. 8, the CCT of the dichromatic white LED featuring a flat phosphor layer was approximately 5500 K. When the periodic inverted pyramid structure was present on the surface of the PDMS layer, the CCT changed because the light extraction enhancement was strongly wavelength-dependent. The enhancement in light intensity for blue light (455 nm) was larger than that for yellow light (550 nm); as a result, the CCT of the white LED featuring the textured phosphor layer increased to approximately 5700 K, due to the color of this light source becoming bluish. Nevertheless, to determine the CRI of a white light source, we required a reference light source having the same CCT as the tested light source. The CCT of the dichromatic white LED featuring the textured phosphor layer should have been fixed at 5500 K if we were to compare their color rendering abilities. Therefore, we increased the weight percentage of the phosphor (to 54.5 weight percent) in the PDMS mixture to fabricate a textured phosphor layer incorporating a higher phosphor concentration; accordingly, more blue light from the bottom GaN-based blue LED would be absorbed by the phosphor. As a result, the enhancement in the intensity of blue light decreased slightly, from 20 to 15%, while that of yellow light increased from 2 to 4%. In addition, the intensity dip in the spectrum at 490 nm was significantly enhanced (by 25%) after positioning the periodic inverted pyramid structure on the surface of the phosphor layer (Fig. 8). The CCT of the dichromatic white LED featuring the textured phosphor layer had now decreased to 5500 K. Therefore, we could calculate the CRI by measuring the average difference between a Planckian black-body source having a CCT of 5500 K (as displayed in Fig. 6a) and this textured white LED. As mentioned above, the increase in relative intensity of light at 490 nm due to the blue and yellow light would assist in increasing the CRI of the dichromatic white LED. Accordingly, the performance of the dichromatic white LED did improve, with the CRI increasing from 69 to 73. Thus, the performance of this dichromatic white LED was enhanced effectively by fabricating periodic structures on the surface of the encapsulation layer, the result of increases in both the light extraction efficiency and the CRI.

## Conclusions
Although dichromatic white LEDs are inexpensive and display quite high efficiency when compared with the available variety of white LEDs, their efficiencies and performance will have to improve if they are to be adopted more widely in general lighting applications. In contrast to enhancing the efficiency of GaN-based blue LEDs, improving the light extraction of the phosphor package layer, by fabricating textured structures on the surface of encapsulation layer, has seldom been investigated. The efficiency of dichromatic white LEDs is limited by the effects of total internal reflection and Fresnel reflection at the encapsulation layer-air interface. In this study, we calculated the light extraction behavior of four kinds of periodic structures—nanorods, inverted rods, pyramids, and inverted pyramids—on the surface of the encapsulation layer. We applied the RCWA method to determine the optimized structural parameters that provided the highest light extraction efficiency for yellow light at a wavelength of 550 nm to prevent the loss of down-converting efficiency. We found that a closely-packed inverted pyramid structure provided the superior light extraction by decreasing not only Fresnel reflection at incident angles less than the critical angle (by an optical gradient effect) but also total internal reflection at incident angles greater than the critical angle (by modifying the diffraction behavior). In an experimental study, we used nanoimprint lithography to fabricate an inverted pyramid structure on the surface of the PDMS layer. The intensities of blue light at 455 nm and yellow light at 550 nm increased by 20 and 2%, respectively. To examine the effect of the inverted pyramid structure on the CRI, we optimized the CCT of the white LED by increasing the concentration of phosphor to generate more yellow light, due to enhancement of the light extraction of blue light after fabricating the textured structure. By maintaining the same CCT, the enhancement of blue light was 15% and that of yellow light was 4%. Meanwhile the light extraction of the intensity dip near 490 nm was enhanced significantly (by 25%), resulting in increased relative intensity of light at 490 nm due to the blue and yellow light. The CRI of this dichromatic white LED increased from 69 to 73. Therefore, this method improved not only the light extraction efficiency but also the CRI, providing an effective and simple means of enhancing the applicability of dichromatic white LEDs in solid state illumination.

## Acknowledgements
We thank the Ministry of Science and Technology, Taiwan, for supporting this study under contracts MOST-103-2221-E-002-041-MY3 and MOST-103-2221-E-002-092-MY3.

# Notes and references

1  S. Pimputkar, J. S. Speck, S. P. DenBaars and S. Nakamura, *Nat. Photonics*, 2009, **3**, 180.

2  M. R. Krames, O. B. Shchekin, R. Mueller-Mach, G. O. Mueller, L. Zhou, G. Harbers and M. G. Craford, *J. Dispersion Sci. Technol.*, 2007, **3**, 160.

3  C. C. Yang, C. F. Lin, H. C. Liu, C. M. Lin, R. H. Jiang, K. T. Chen and J. F. Chien, *J. Electrochem. Soc.*, 2009, **156**, H316.

4  S. J. Bae, J. Choi, D. H. Kim, I. C. Ju, C. S. Shin, C. G. Ko and J. S. Yu, *Phys. Status Solidi A*, 2012, **209**, 1168.

5  R. Dylewicz, A. Z. Khokhar, R. Wasielewski, P. Mazur and F. Rahman, *Nanotechnology*, 2011, **22**, 055301.

6  R. Dylewicz, A. Z. Khokhar, R. Wasielewski, P. Mazur and F. Rahman, *Appl. Phys. B*, 2012, **107**, 393.

7  H. X. Yin, C. R. Zhu, Y. Shen, H. F. Yang, Z. Liu, C. Z. Gu, B. L. Liu and X. G. Xu, *Appl. Phys. Lett.*, 2014, **104**, 061113.

8  K. S. Kim, S. M. Kim, H. Jeong, M. S. Jeong and G. Y. Jung, *Adv. Funct. Mater.*, 2010, **20**, 1076.

9  H. K. Lee, D. H. Joo, Y. H. Ko, Y. Yeh, Y. P. Kim and J. S. Yu, *Jpn. J. Appl. Phys.*, 2012, **51**, 122102.

10 C. T. Lee and T. J. Wu, *J. Lumin.*, 2013, **137**, 143.

11 H. Jeong, D. J. Park, H. S. Lee, Y. H. Ko, J. S. Yu, S. B. Choi, D. S. Lee, E. K. Suh and M. S. Jeong, *Nanoscale*, 2014, **6**, 4371.

12 J. H. Kang, H. G. Kim, J. H. Ryu, H. K. Kim, H. Y. Kim, J. Joo, M. S. Lee and Y. J. Park, *Electrochem. Solid-State Lett.*, 2010, **13**, D1.

13 S. Oh, P. C. Su, Y. J. Yoon, S. Cho, J. H. Oh, T. Y. Seong and K. K. Kim, *Opt. Express*, 2013, **21**, A970.

14 J. J. Wierer Jr., A. David and M. M. Megens, *Nat. Photonics*, 2009, **3**, 163.

15 E. J. Hong, K. J. Byeon, H. Park, J. Hwang, H. Lee, K. Choi and H. S. Kim, *Solid-State Electron.*, 2009, **53**, 1099.

16 K. J. Byeon, E. J. Hong, H. Park, K. M. Yoon, H. D. Song, J. W. Lee, S. K. Kim, H. K. Cho, H. K. Kwon and H. Lee, *Semicond. Sci. Technol.*, 2010, **25**, 035008.

17 Z. G. Yu, P. Chen, G. F. Yang, B. Liu, Z. L. Xie, X. Q. Xiu, Z. L. Wu, F. Xu, Z. Xu, X. M. Hua, P. Han, Y. Shi, R. Zhang and Y. D. Zheng, *Chin. Phys. Lett.*, 2012, **29**, 098502.

18 S. K. Parta, S. Adhikari and S. Pal, *J. Dispersion Sci. Technol.*, 2013, **9**, 339.

19 P. H. Fu, G. J. Lin, H. P. Wang, K. Y. Lai and J. H. He, *Nano Energy*, 2014, **8**, 78.

20 S. K. Patra, S. Adhikari and S. Pal, *Appl. Opt.*, 2014, **53**, 3890.

21 Y. M. Song, E. S. Choi, J. S. Yu and Y. T. Lee, *Opt. Express*, 2009, **17**, 20991.

22 Y. H. Hsiao, C. Y. Chen, L. C. Huang, G. J. Lin, D. H. Lien, J. J. Huang and J. H. He, *Nanoscale*, 2014, **6**, 2624.

23 C. W. Hsu, Y. C. Lee, H. L. Chen and Y. F. Chou, *Photonic Nanostruct.*, 2012, **10**, 523.

24 H. Luo, J. K. Kim, E. F. Schubert, J. Cho, C. Sone and Y. Park, *Appl. Phys. Lett.*, 2005, **86**, 243505.

25 N. Narendran, Y. Gu, J. P. Freyssinier-Nova and Y. Zhu, *Phys. Status Solidi*, 2005, **202**, R60.

26 I. Moreno, D. Bermudez and M. Avendano-Alejo, *Appl. Opt.*, 2010, **49**, 12.

27 Y. C. Lin, J. P. You, N. T. Tran, Y. He and F. G. Shi, *J. Elec- tron. Packag.*, 2011, **133**, 011009.

28 H. C. Hsu, C. J. Wang, H. R. Lin and P. Han, *Microelectron. Reliab.*, 2012, **52**, 894.

29 H. S. Choi, J. S. Park and C. H. Moon, *J. Opt. Soc. Korea*, 2014, **18**, 370.

30 J. J. Kim, S. Chae and K. H. Jeong, *Opt. Lett.*, 2010, **35**, 823.

31 H. C. Chen, K. J. Chen, C. H. Wang, C. C. Lin, C. Lin, C. Y. Yeh, H. H. Tsai, M. H. Shih, H. C. Kuo and T. C. Lu, *Nanoscale Res. Lett.*, 2012, **7**, 188.

32 J. K. Kim, Y. Lee, H. G. Kim, K. J. Choi, H. S. Kweon, S. Park and K. H. Jeong, *Proc. Natl. Acad. Sci. U. S. A.*, 2012, **109**, 18674.

33 E. Taylor, P. R. Edwards and R. W. Martin, *Phys. Status Solidi A*, 2012, **209**, 461.

34 CIE Technical Report, Colorimetry, 3rd edn, CIE 15:2004, Commission Internationale de l'Eclairage, Vienna, Austra- lia, 2004.

35 Q. R. Yan, Y. Zhang, S. T. Li, Q. A. Yan, P. P. Shi, Q. L. Niu, M. He, G. P. Li and J. R. Li, *Opt. Lett.*, 2012, **37**, 1556.

36 M. Zhang, Y. Chen and G. He, *Sci. World J.*, 2014, **2014**, 897960.

37 J. H. Oh, S. J. Yang, Y. G. Sung and Y. R. Do, *Opt. Express*, 2012, **20**, 20276.

38 H. Shi, C. Zhu, J. Huang, J. Chen, D. Chen, W. Wang, F. Wang, Y. Cao and X. Yuan, *Opt. Mater. Express*, 2014, **4**, 649.

39 C. Zhao, D. Zhu, M. Ma, T. Han and M. Tu, *J. Alloys Compd.*, 2012, **523**, 151.

40 G. He and J. Tang, *IEEE Photonics Tech. Lett.*, 2014, **26**, 1450.

41 Y. Yin, R. Wang and L. Zhou, *Luminescence*, 2014, **29**, 626.

42 C. F. Lai, C. C. Chang, M. J. Wang and M. K. Wu, *Opt. Express*, 2013, **21**, A687.

43 J. S. Kim, S. C. Yang and B. S. Bae, *Chem. Mater.*, 2010, **22**, 3549.

44 J. M. Han, J. W. Han, J. Y. Chun, C. H. Ok and D. S. Seo, *J. Jpn. Appl. Phys.*, 2008, **47**, 8986.

45 C. D. M. Donega, S. J. L. Ribeiro, R. R. Goncalves and G. Blasse, *J. Phys. Chem. Solids*, 1996, **57**, 1727.

46 P. Schlotter, J. Baur, Ch. Hielscher, M. Kunzer, H. Obloh, R. Schmidt and J. Schneider, *Mater. Sci. Eng., B*, 1999, **59**, 390.

47 D. Haranath, H. Chander, P. Sharma and S. Singh, *Appl. Phys. Lett.*, 2006, **89**, 173118.

48 A. Purwanto, W. N. Wang, T. Ogi, I. W. Lenggoro, E. Tanabe and K. Okuyama, *J. Alloys Compd.*, 2008, **463**, 350.