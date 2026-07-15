# Design of sub-wavelength dielectric antireflective grading for multijunction concentrator photovolatics

Wei Wang$^{a,b,1}$, Alex Freundlich$^{a,b}$,

$^{a}$ Photovoltaic and Nanostructure Laboratory Center for Advanced materials, University of Houston, Houston, TX United State, 77204;
$^{b}$ Department of Physics, University of Houston, Houston, TX United State, 77204

## ABSTRACT

In III-V concentrator applications, sunlight is focused with wide angular distribution that limits the effectiveness of conventional thin-film AR coatings. Furthermore the transmission properties are generally degraded non-uniformly over the electromagnetic spectrum, which in the case of multi-junction solar cells leads to additional sub-cell current matching related losses. Here, and in an attempt to identify a better alternative to the conventional planar layer ARCs for III-V multi-junction concentrator cells in case of with/without protective cover glass in conjunction with wide optical aperture angles, a systematic analysis of design parameters and angular dependent antireflective properties of dielectric gratings has been undertaken, through the implementation of sub-wavelength 2D pyramidal gratings of ZnS and TiO₂. The study indicated limited improvement for devices operated with SiO₂ like cover glass. In the absence of SiO₂ like cover glass, the evaluation indicated that reflection-loss related current losses can be reduced by 2-3 fold compared to their double-layer ARC counterparts. i.e. for a 3J metamorphic device this lead to a current improvement of 0.7 $mA/cm^2$ per concentration for a 60 degree aperture angles

**Keywords:** angular tolerance, antireflective, concentrated photovoltaic, dielectric, effective medium approach, III-V solar cell, subwavelength, texture

## 1. INTRODUCTION

In recent years, high concentration III-V multi-junction solar cell devices have reached efficiencies in excess of 40% [i.e. 1,2] and have been identified as a route to achieve high system level performances. In high X III-V concentrator applications sunlight is focused onto the surface of cell with a wide angular distribution that limits the effectiveness of conventional thin-film AR coatings. Furthermore the transmission properties are generally degraded non-uniformly over the electromagnetic spectrum which in the case of multi-junction solar cells leads to that conventional anti-reflection coatings (ARCs) perform well for normally incident light, i.e. for a double layer ARC decreasing reflection from 30% on a 0.7eV semiconductor to 5%; increasing the light angle of incidence to 60 degrees in this case results in an almost two fold increase of reflection losses. Furthermore for multi-junctions devices these losses result in uneven current degradations in sub-cells potentially leading to additional current matching related losses. Ideally the optimal performance of a multi-junction device requires identical current output for each sub cell. As the efficiency of solar cell is more dependent on the number of photons with energy above band gap, this work has focused on the fraction of integrated reflected photons instead of on the reflectivity. To overcome the limitation of planar ARC, several alternate approaches have been attempted in the literature, including use of dielectric or metallic nanoparticles (plasmonic scattering) [3], micro texturing [4], and sub-wavelength dielectric gratings. Among these approaches, the application of sub wavelength dielectric gratings has shown promising results [5]. This paper focuses on identifying optimal grating design of antireflection and angular tolerance property, for sub-wavelength dielectric grating on commonly concentrated photovoltaic systems, such as a typical 3 or 4 junction solar cells.

## 2. METHODOLOGY

In this work, textured anti-reflective grating is considered as a pile of continuous indices thin film, which varies from the index of air (or that of cover glass) to the index of grating medium [6]. Each layer of thin films behaves as a 2 by 2

---
$^{1}$ wwang14@uh.edu; phone: (1)713-743-3621

Physics, Simulation, and Photonic Engineering of Photovoltaic Devices III, edited by Alexandre Freundlich, Jean-François Guillemoles, Proc. of SPIE Vol. 8981, 89810Y · © 2014 SPIE
CCC code: 0277-786X/14/$18 · doi: 10.1117/12.2040431

Proc. of SPIE Vol. 8981 89810Y-1

matrix according to transfer matrix method[7], which indicates the behavior of electric-magnetic field propagating from incoming media (air) to final media (solar cell devices). The goal of this work is to figure out how to obtain minimum surface reflection caused current loss for specific solar cell devices, by choosing proper AR material and carefully designed geology structure parameters. In order to achieve this goal, an approximate prediction is undertaken by assuming that solar cell devices are all under single junction mechanism (without current matching issue), and AR materials have single refractive index value over the whole wavelength. Possible AR materials candidates and rough geometric grating's parameters are estimated under this assumption. By taking into account of materials' intrinsic desperation property, more accurate geometric parameters can be optimized for specific multi-junction devices.

A physical approximation assumes each layer has an effective refractive index $n_{eff}$, whose value is between that of air $n_1$ and bulk AR dielectric material $n_2$, and where $n_{eff}$ magnitude is defined as a function of the grating shape and AR occupation ratio $f$. There are three common ways to approximate effective refractive index for each layer. Equation (1) shows the three common ways.

$$
n_{eff}=(n_1^q*f_1+n_2^q*f_2)^{1/q} \tag{1}
$$

where $f_1$ and $f_2$ are the occupation ratio of two materials with refractive index $n_1$ and $n_2$ respectively, and $q$ takes a value of 1, 1/2 or 2/3, when using the approximation it would be a linear average of refractive index ($q$=1), linear average of permittivity [8] ($q$=1/2) and average of refractive index to the order of 2/3 ($q$=2/3) [9] respectively. The linear average of permittivity ($q$=1/2) was chosen in this work.

Table 1 Schematic of AR grating on solar cell devices (gray color in images), their optimized geometric parameters, and their minimum photon loss over 380 nm to 2000 nm under AM 1.5G, comparing with conventional double-layer ARC.

<table>
  <tr>
    <td>Schematic of grating structures and notations</td>
    <td>Refractive index ($n$)
profile from air to
substrate (L to R)</td>
    <td>AR grating
and materials</td>
    <td>Optimized geometric
parameters and its
current loss</td>
  </tr>
  <tr>
    <td>![](./images/813156952744919044_1.jpg)</td>
    <td>![](./images/813156952744919044_2.jpg)</td>
    <td>MgF₂-ZnS
double layer</td>
    <td>$\mathrm{t_1} = 124\ nm$,
$\mathrm{t_2} = 70\ nm$
$2.64\ mA/cm^2$</td>
  </tr>
  <tr>
    <td>![](./images/813156952744919044_3.jpg)</td>
    <td>![](./images/813156952744919044_4.jpg)</td>
    <td>1D ZnS binary
grating</td>
    <td>$\mathrm{d_1} = 110\ nm$,
$\mathrm{d_2} = 68\ nm$,
$\mathrm{f} = 0.4$.
$2.52\ mA/cm^2$</td>
  </tr>
  <tr>
    <td>![](./images/813156952744919044_5.jpg)</td>
    <td>![](./images/813156952744919044_6.jpg)</td>
    <td>1D ZnS
triangle
grating</td>
    <td>$\mathrm{h} = 1820\ nm$,
$\mathrm{t} = 0\ nm$,
$\mathrm{f} = 1$
$1.70.\ mA/cm^2$</td>
  </tr>
  <tr>
    <td>![](./images/813156952744919044_7.jpg)</td>
    <td>![](./images/813156952744919044_8.jpg)</td>
    <td>2D TiO₂
hemisphere
grating</td>
    <td>$\mathrm{R} = 170\ nm$,
$\mathrm{t} = 65\ nm$,
$\mathrm{f} = 0.7$
$2.14\ mA/cm^2$</td>
  </tr>
  <tr>
    <td>![](./images/813156952744919044_9.jpg)</td>
    <td>![](./images/813156952744919044_10.jpg)</td>
    <td>2D ZnS
pyramid
grating</td>
    <td>$\mathrm{h} = 385\ nm$,
$\mathrm{t} = 64\ nm$,
$\mathrm{f} = 0.8$
$1.12\ mA/cm^2$</td>
  </tr>
</table>

![](./images/813156952744919044_11.jpg)

Fig. 1 Schematic and notation of off normal incident light
(a) schematic of light flux reducing as incident angle increases; (b) schematic of angular notation in concentrator light disk

There are two main losses for CPV due to off normal incident photon flux. First, as shown in Fig. 1(a), light flux reducing as incident angle increases, due to shrink of effective area, which is similar as only the portion of the light source intensity perpendicular to the panel can be used. Consequently, (1-cosθ) proportion of the photons will get lost by vector product. Second, the reflectivity degrades non-uniformly over solar cells' working electromagnetic spectrum, and generally increases with augmented off normal incident. The majority of the incoming light focused from concentrators would confront the non-normal light degradation. In conclusion, at a specific incident angle θ, the photon depletion from direct light flux equals to (1-cosθ) multiplied by the photon intensity from light source; the photon depletion from non-ideal AR design equals to cosθ multiplied by the integrated reflected photon loss over certain spectrum of interest R(θ) multiplied by the photon intensity from light source. The final photon depletion, in consideration of the light coming from consecutive angle as shown in Fig. 1(b), is therefore a sum of the average photon loss of two close by incident angles (i.e. $\theta_{m}$ and $\theta_{m+1}$) multiplied by the area proportion (i.e. $(tan^{2}\theta_{m+1}-tan^{2}\theta_{m})/tan^{2}\alpha$) of a ring between incident angle $\theta_{m+1}$ and $\theta_{m}$ among the full light disk of concentrator with aperture α.The amount of energy/photon depletion in accordance with these two origins is briefly described in the equation (2) and (3) respectively.

$$
\sum_{m=1}^{N} I_{0}[R(\theta_{m})(1 - cos\theta_{m}) + R(\theta_{m+1})(1 - cos\theta_{m+1})]/2 * (\tan^{2}\theta_{m+1}-\tan^{2}\theta_{m})/\tan^{2}\alpha \tag{2}
$$

$$
\sum_{m=1}^{N} I_{0}[(1 - cos\theta_{m}) + (1 - cos\theta_{m+1})]/2 * (\tan^{2}\theta_{m+1}-\tan^{2}\theta_{m})/\tan^{2}\alpha \tag{3}
$$

Where $I_{0}$ is the number of photons from incoming light within the complete electromagnetic spectrum of interest based on certain spectrum (i.e. AM 1.5G) per unit area. $R$ is the integrated photon loss at specific incident angle (i.e. $\theta_{m}$), over the complete electromagnetic spectrum of interest based on certain spectrum (i.e. AM 1.5G). $\alpha$ is the aperture which is also the half open angle of concentrator. N is the number of section that the concentrator is divided into. $m$ is a variable changing from 1 to $N$.

## 3. RESULTS AND DISCUSSION

In order to apply transfer matrix to simulation, the physical dimensions need to in the sub-wavelength scale (grating pitch/period, height $< \lambda/4n$) so scattering and multiple reflections can be ignored. In addition the AR material should be a dielectric. Among available texturing patterns/gratings, 1D rectangle grating, 1D triangle grating, 2D hemisphere grating, and 2D pyramid grating, optimized 2D pyramid grating provide the good angular tolerant and anti-reflection properties, over $300\ nm$ to$1850\ nm$ broad band wavelength, as shown in Table 1 and Fig. 3.

Table 1 shows 4 grating morphologies schematic comparing with conventional double-layer ARC, from both 3D and 2D cross section images. 15-20 $nm$ Al-rich AlGaInP or Al-rich AlGaAs is generally used as multijunction devices' low SRV window layer for passivation, due to large band gap and close indices for AlGaInP and AlGaAs top cells, So $Al_{0.8}Ga_{0.2}As$ can be considered as the top semiconductor layer beneath of AR structure (as gray color shows in Table 1) of anti-

reflection textures (as green color shows in Table 1). Table 1 meanwhile shows the optimized geometric parameters for minimum photon loss over the region from 380 $nm$ to 2000 $nm$ under AM 1.5G. The method of choosing grating materials and optimizing textured structures is explained in reference [10].It indicates that 1D rectangle grating behaves similar to conventional double-layer ARC. 1D triangle grating requires larger grating depth (as $h=1820\ nm$ in Table 1), which may increase the risk of degrade and none uniform during fabrication. Consequently, 2D pyramid grating and 2D hemisphere are good candidates for textured AR grating for multi-junction solar cell devices.

In this work, dielectric materials of transparent properties in working spectrum were chosen as AR textured materials, sacrificing the consecutive from AR materials to substrates. The textured AR could eliminate the discontinuous from ambient to AR materials themselves at most. Not as general imagination that fully grating occupation contributes to the best result because of consecutive refractive index from air to AR materials; in fact 0.6~0.8 occupation ratio might demonstrate better AR property relating to geometric shape. The discontinuity between AR material and solar cell is not avoidable, therefore the not fully occupation can help the refractive indices close to ideal index profile. High indices materials, compared with low index materials, were proved to better reduce the discontinuity between solar cells substrate and AR materials [6].

![](./images/813156952744919044_12.jpg)

Fig. 2 Angular dependence of current loss $(mA/cm^{2})$ in GaInP/GaAs/InGaAs device's each subcell with BK7 cover glass condition (a) glass match optimized duo layer in glass(b) glass match optimized $TiO_{2}$ pyramid texturing in glass

Fig. 2 presents the angular dependence of current loss in 3J MM device each sub cell with BK7 cover glass condition. It shows from simulation that glass match duo layer materials should be the combination of $96\ nm\ Ta_{2}O_{5}$ on top of $58\ nm$ $TiO_{2}$, choosing among the candidates of $MgF_{2}$, $SiO_{2}$, $Al_{2}O_{3}$, $Si_{3}N_{4}$, $ZnO$, $Ta_{2}O_{5}$, $ZnS$, $ZnSe$, and $TiO_{2}$. Likewise, optimized pyramid grating is made of $TiO_{2}$ with $260\ nm$ height, $50\ nm$ planar-film underneath and 0.7 occupation, as the h, t and f shown in Fig. 2 (b) respectively. The photon loss due to vector product from light flux cannot be optimized; for the sake for intuitively comparing the reflection caused current loss, Fig.2 is assuming the spectrum that can be used by solar cell devices from any angles are AM1.5G, as the standard testing condition. 2D pyramid grading shows lower current loss for the device, especially for high off normal incident angle, almost half of the value for double layer ARC. But there is limited improvement at normal or near normal incident light, which is due to limited access of high index materials for pyramid grading. InGaAs is the main current loss cell due to reflection in both AR design, and its current loss increases as the off normal incident angle increases. GaAs and GaInP sub cells, however, do not exactly follow this regular rule. In glass matched device, the current loss from GaInP with optimized double layer decreases as the incident angle increases to $40^{\circ}$, and then it increases as the incident angle increases to $60^{\circ}$. Similarly, in glass matched device, the current loss from GaAs with optimized pyramid grading decreases as the incident angle increases from $30^{\circ}$ to $50^{\circ}$, and then it increases as the incident angle increases to $60^{\circ}$.

There is usually a current limiting sub cell in solar cell devices; therefore, the ARC can be designed in such a way that reduces the current mismatch most for the current limiting sub cell to bring the device current to the highest value. The results would be shown elsewhere (W. Wang, A. Freundlich, unpublished).

By integral over the entire incident angles multiplied by intensity ratio respectively, where it is assumed that the light above lens distributes uniformly, the current loss for specific design of concentrators per concentration can be calculated, as shown in Fig. 3. Fig. 3 demonstrates the total current loss in considerate of both flux loss and reflection loss, as the theory explained in equation (2) and (3).

![](./images/813156952744919044_13.jpg)

Fig.3. Current loss $(mA/cm^{2})$ comparison between duo layer and 2D pyramid grating on 3J MM devices with and without protective cover glass

It can be seen from Fig. 3 that graded dielectric with single material performs better AR and angular tolerant property compared with conventional planar thin film ARC for various concentrator application. 3J GaInP/GaAs/InGaAs air matched device for example, the current loss from surface reflection is around $0.3mA/cm^{2}$ higher than that from conventional 2-layer ARC, and as the acceptance angle increases, this improvement increases. 3J GaInP/GaAs/InGaAs glass matched device shows that 2D pyramid presents similar reflection loss comparing with 2-layer ARC, however, limited improvement due to not ideal AR material's refractive index. Yet the improvement is maintained within $0.5mA/cm^{2}$, not as outstanding as the current improvement shown in Fig. 2, which is because as the aperture angle increases, more current gets consumed by flux loss, so less photons are actually going through AR structure and saved.

## 4. CONCLUSION

From the properties of light propagation, it was found that the presence of consecutive refractive indices from ambient to substrates can highly reduce reflectivity, and even at large off-normal incidence angles, reflectivity stayed at a low value. In this study, dielectric materials with transparent properties in the working spectrum, such as $Ta_{2}O_{5}$ and $TiO_{2}$, were chosen as AR materials. Sacrificing the consecutive refractive indices from dielectric materials to substrates, the textured AR could, at the most, eliminate the refractive indices discontinuity from the ambient to AR materials. A non-fully occupied texture helps the index grading to be closer to ideal condition. Among all the 1D and 2D texturing analyzed, carefully designed 2D sub-wavelength pyramid $TiO_{2}$ AR grating, which presented the best properties for single junction devices, was optimized for 3J air matched and glass matched GaInP/ GaAs/ InGaAs, solar cells under $60^{0}$- $120^{0}$ wide angle concentrators. The maximum current loss among all their sub cells was shown as well. Since high index materials were preferred to reduce the discontinuity between solar cells substrate and AR materials, the study indicated limited improvement for devices operating with a $SiO_{2}$ like cover glass. In the absence of a cover the evaluation indicates that

Proc. of SPIE Vol. 8981 89810Y-5

through a careful selection of the design these dielectric grading can reduce reflection-loss related current losses by 2 fold by comparison to their planar double layer ARC counterparts. The ARC can be designed in such a way to reduce the current limiting sub cell's reflection current loss, so that it can reduce the current mismatch for the device.

## REFERENCES

[1] S. Wojtczuk, P. Chiu, X.B. Zhang , D. Derkacs, C. Harris, D. Pulver, and M. Timmon, "InGaP/GaAs/InGaAs 41% Concentrator Cells Using Bi-facial Epigrowth," Potovoltaic Specialists Conference (PVSC), 35th IEEE, pp.1259-1264 (2010).

[2] M.A. Green, K. Emery, Y. Hishikawa, W. Warta, and E.D. Dunlop, "Solar cell efficiency tables (version 40)," prog. Photovolt: Res. Appl. Vol.20, pp.606-614 (2012).

[3] Y.S. Wang, N.F. Chen, X.W. Zhang, X.L. Yang, Y.M. Bai, M. Cui, Y. Wang, X.F. Chen, and T.M. Huang, "Ag surface plasmon enhanced double-layer antireflection coatings for GaAs solar cells," Jounals of Semiconductors, 30 (7) (2009).

[4] C.H. Chang, P.C. Yu, M.H. Hsu, et. al, "Combined micro- and nano-scale surface textures for enhanced near- infrared light harvesting in silicon photovoltaics," Nanotechnology 22, 095201 (2011).

[5] S.L. Diedenhofen, G. Vecchi, R.E. Algra, A. Hartsuiker, et. al, "Broad-band and Omnidirectional Antireflection Coatings Based on Semiconductor," Adv. Mater., 21, 973-978 (2009).

[6] W. Wang, A. Freundlich, "Optimizing the Design of 2D Subwavelength ARC Gratings for Multijunction III-V Concentrator Cells," Photovoltaic Specialists Conference (PVSC), 38th IEEE, article #621-I18 (2012).

[7] M. Born, E. Worf, [Principles of Optics], Cambridge University Press, 952p. (1999).

[8] T.K. Gaylord, M.G. Moharam, E.B. Grann and D.A. Pommet, "Formulation for stable and efficient implementation of the rigorous coupled-wave analysis of binary gratings," J. Opt. Soc. Am. A 12(5) (1995).

[9] D.G. Stavenga, S. Foletti, G. Palasantzas, K. Arikawa,"Light on the moth-eye corneal nipple array of butterflies," Proc. R. Soc. B 273,661-667(2006).

[10] W.Wang, A. Mehrotra, A. Alemu, A. Freundlich, "Minimizing solar cell reflection loss through surface texturing and implementation of 1D and 2D subwavelength dielectric gratings," Proc. of SPIE, paper NO.8256 (2012).