# Robust reduction of graphene fluoride using an electrostatically biased scanning probe

Woo-Kyung Lee¹, Stanislav Tsoi¹, Keith E. Whitener¹, Rory Stine², Jeremy T. Robinson³, Jonathon S. Tobin⁴, Asanka Weerasinghe⁴, Paul E. Sheehan¹ (☒), and Sergei F. Lyuksyutov⁴ (☒)

¹ Division of Chemistry, US Naval Research Laboratory, Washington DC 20375, USA
² NOVA Research, Alexandria, Virginia 22308, USA
³ Division of Electronic Science and Technology, US Naval Research Laboratory, Washington DC 20375, USA
⁴ The University of Akron, Department of Physics, Akron OH 44325, USA

Received: 7 June 2013
Revised: 23 July 2013
Accepted: 26 July 2013

© Tsinghua University Press
and Springer-Verlag Berlin
Heidelberg 2013

## KEYWORDS
graphene fluoride,
graphene,
electrostatic lithography,
Kelvin force probe
microscopy,
atomic force microscopy-
based electrostatic
nanolithography
(AFMEN)

---

## ABSTRACT
We report a novel and easily accessible method to chemically reduce graphene fluoride (GF) sheets with nanoscopic precision using high electrostatic fields generated between an atomic force microscope (AFM) tip and the GF substrate. Reduction of fluorine by the electric field produces graphene nanoribbons (GNR) with a width of 105–1,800 nm with sheet resistivity drastically decreased from $>1\ \text{T}\Omega\text{·sq.}^{-1}$ (GF) down to $46\ \text{k}\Omega\text{·sq.}^{-1}$ (GNR). Fluorine reduction also changes the topography, friction, and work function of the GF. Kelvin probe force microscopy measurements indicate that the work function of GF is 180–280 meV greater than that of graphene. The reduction process was optimized by varying the AFM probe velocity between $1.2\ \mu\text{m·s}^{-1}$ and $12\ \mu\text{m·s}^{-1}$ and the bias voltage applied to the sample between –8 and –12 V. The electrostatic field required to remove fluorine from carbon is $\sim1.6\ \text{V·nm}^{-1}$. Reduction of the fluorine may be due to the softening of the C–F bond in this intense field or to the accumulation and hydrolysis of adventitious water into a meniscus.

---

## 1 Introduction
Chemical modification can extend the already superlative properties of graphene. Of particular interest has been tuning the electronic properties of graphene, which in its pristine form is a semimetal with excellent conductivity. While many different chemical functionalizations of graphene have been reported, the two most efficient at making graphene electrically insulating are oxidation [1, 2] and fluorination [3, 4]. Graphene oxide (GO) is an inexpensive and readily available material with the potential to excel in many

Address correspondence to Paul E. Sheehan, paul.sheehan@nrl.navy.mil; Sergei F. Lyuksyutov, sfl@uakron.edu

![](./images/813205263422062594_1.jpg)

different applications; however, it has two significant limitations if one wishes to control its chemistry. The first one is that GO has many different oxygen-rich functionalities that complicate its chemistry. The second is that, once oxidized, edge ether moieties form in the basal plane that cannot be removed without destroying the carbon lattice [5]. This implies that oxidized graphene will be quite difficult to selectively restore to pristine graphene if that is the goal, as it is in this paper. In contrast, graphene fluoride (GF) has a relatively uniform chemistry and is readily formed in large sheets by exposing graphene to $XeF_{2}$ [3,4]. GF was first synthesized independently at the Naval Research Laboratory (by Robinson et al. [3]) and Manchester University (by Nair et al. [4]) in 2010. Graphene grown on copper foil was fluorinated using a commercial $XeF_{2}$ etcher at $30^{\circ}C$ for less than 15 min [3], and exfoliated graphene was treated with $XeF_{2}$ at $70^{\circ}C$ for much longer (>100 hours) exposure times [4]. Fluorinating just one side of graphene produces one of the thinnest known insulating materials with a DFT-calculated band gap of 2.93 eV for $C_{4}F$ [3]. Another interesting approach is based on selective area fluorination of graphene with laser irradiation of a fluoropolymer so that it produces active fluorine radical reacting with graphene in irradiated areas [6]. In practical GF films, the majority of the fluorine bonds are covalent C-F bonds [7] with a small fraction of $CF_{2}$ and $CF_{3}$ bonds existing at grain boundaries, point defects, and other edges. Recent testing of GF with Raman, FTIR, and photoluminescence spectroscopy techniques suggests that the band gap can be (3.8-3.9 eV), and it may luminesce in the visible and UV ranges [8]. GF is thus a promising material for future graphene electronics and optoelectronics.

Multiple lithographic approaches have been introduced to create graphene-based devices using fluorination, such as creating chemically-isolated graphene nanoribbons via thermal dip-pen nanolithography [9] or directly reducing GF to reduced graphene fluoride (rGF) via electron beam irradiation [10]. Similarly, there have been studies using a high electric field between graphene and a conductive scanning probe either to oxidize [11-13] or hydrogenate graphene and thereby define electronic devices [14]. Here, we explore an alternative approach that uses high electrostatic fields to reduce GF to rGF from the 2D graphene mesh by "breaking" the C-F bonds. This bond breaking may stem from local chemistry induced by the electrolysis of adventitious water or from the polarization of the C-F bond under the electrostatic field.

## 2 Results and discussion

### 2.1 Patterning of GF devices

To pattern the GF, we followed the protocol for atomic force microscopy-based electrostatic nanolithography, or AFMEN, where a conducting AFM tip is held a fixed distance above the surface while an intense electric field is applied across the gap [15]. AFMEN has been used to generate nanostructured polymeric films by inducing the mass transport of polarized polymer molecules along the electric field lines emanating from an electrically charged AFM tip and the grounded conductive substrate. The electric field inside an insulator such as polystyrene can exceed $1-10V\cdot nm^{-1}$. Without external heating or AFM-tip contact, the process can precisely generate 1-50 nm high polymer nanostructures at AFM tip velocities from 0.1 to $8\ \mu m\cdot s^{-1}[15,16]$.

All experiments were performed by modifying pre-existing micrometer-scale graphene field effect transistor (FET) devices (Figs. 1(a) and 1(b)). This enables the electronic properties of the graphene to be measured at the beginning of the experiment and then monitored at each stage of fabrication. To prepare these base devices, the silicon oxide substrate (100 nm of $SiO_{2}$ on n-Si (resistivity: $1-10\ \Omega\cdot cm$)) was first reacted with hexamethyldisilazane (HMDS) prior to depositing graphene onto the surface of $SiO_{2}$. The HMDS reacts with silanol groups to form a hydrophobic monolayer that reduces the intercalation of water and other polar adsorbates into the substrate/graphene interface where they can dope the graphene device and produce hysteresis in $I-V$ sweeps [17]. The next stage was fluorination of the whole device with a Xactix® $XeF_{2}$ etching system with the duration of gas exposure ranging from 12 to 15 min at a temperature of $\sim30^{\circ}C$. The $XeF_{2}$ fluorination affects the graphene bridges (i.e., the film between the two gold electrodes) but not the gold electrodes themselves [18]. The resistance of each device was then measured using a Keithley 4200-SCS

![](./images/813205263422062594_2.jpg)
![](./images/813205263422062594_3.jpg)
www.editorialmanager.com/nare/default.asp

![](./images/813205263422062594_4.jpg)

Figure 1 (a) Optical image of the base devices used for AFMEN fabrication of a GNR FET. (b) Zoomed in image of the device with a graphene sheet width of 12 μm and a channel length of 4 μm. (c) Cartoon of the biased AFM probe using AFMEN to write a nanoribbon that is chemically isolated in the insulating graphene fluoride. Three stage process of graphene de-fluorination. (d) Height and (e) friction images of the formed GNR. The cross-section in (d) is a horizontal average of the channel area to the left of the plot.

and only open circuit devices ($R_{\text{sheet}} > 1\ \text{T}\Omega\cdot\text{sq.}^{-1}$) were selected for subsequent nanolithography.

The GF bridge was then selectively defluorinated to rGF using AFMEN [15, 16] as shown in Fig. 1(c). Specifically, the grounded AFM tip was moved above the GF film that rested on top of the negatively biased silicon/silicon oxide substrate. Experiments could be carried out in nitrogen ambient; however, reproducibility was enhanced at ambient levels of humidity. To write the line, the conductive AFM tip was rastered over the area to be reduced in lift mode (~5 Å separation from GF) at tip velocities between 1 and $10\ \mu\text{m}\cdot\text{s}^{-1}$ (Fig. 2(a)) and with applied negative biases between –8 and –12 V (Fig. 2(b)). The scan size was maintained at 6 μm; however, the length of the bridge, and thus the effective length of the patterned nanoribbons, was ~4 μm. The dynamic friction (lateral bending of a cantilever) between the moving probe and the substrate is greater for GF than grapheme [19, 20], so the most immediate means of imaging the graphene nanoribbons formed in the GF was to image simultaneously in height and friction modes (Figs. 1(d) and 1(e)). Note that in each operation only a single nanoribbon was produced between two gold electrodes. After fabrication, the sheet resistivity

![](./images/813205263422062594_5.jpg)

Figure 2 Friction force AFM image showing the experimental thresholds of the AFMEN technique on graphene fluoride when using varying (a) tip velocities and (b) voltages. The $y$-averaged friction values are below each plot. The portions of the line where a graphene wrinkle occurred were not included in the average.

of graphene nanoribbons with widths from 105 to 1,800 nm was measured at zero gate bias (Fig. 3). The sheet resistivity decreases dramatically with nanoribbon width from $149\ \mathrm{G\Omega{\cdot}sq.^{-1}}$ for a 105 nm wide GNR down to $46\ \mathrm{k\Omega{\cdot}sq.^{-1}}$ for a 1,080 nm wide GNR. The reason for this dramatic shift is not clear; however, the reduction process could depend heavily on the nature of the probe–GF gap such that any contamination by residual resist would greatly reduce its efficiency and increase the patchiness of the reduction. The fabricated GNRs were highly p-doped, presumably due to residual fluorine or surrounding GF (see Fig. S4 in the Electronic Supplementary Material (ESM))[9]. More importantly, the resistivity of the rGF structures is $46\ \mathrm{k\Omega{\cdot}sq.^{-1}}$ which is only ~30 times that of the pristine graphene and is less than half the resistivity achieved through high electron doses via electron beam irradiation [10]. This indicates that high quality reduction can be achieved. Finally, it should be noted that, unlike other efforts at modifying pristine graphene, reduction may be started arbitrarily on the GF substrate and does not require commencing either at an electrode or graphene edge.

### 2.2 Kelvin probe force microscopy (KPFM) measurements
Fluorine reduction was confirmed initially by topographical changes in height (5–8 Å, Fig. 1(d)), images in friction mode, and also by the substantial decrease in resistance. This abrupt decrease of resistance is similar to the percolation behavior of carbon nanotube thin film channels after the width was reduced by patterning [21]. To verify independently the successful reduction of the fluorinated graphene by AFMEN, the surface potentials of nanoribbon devices were recorded with KPFM. Figure 4 shows the topography (a), surface potential (b), and friction (c) of a wide graphene nanoribbon device captured with two different instruments. Histograms of the data are also shown along with their attributions. Similar results for two more nanoribbon devices are provided in the ESM (Fig. S1 in the ESM). Relative to the untreated GF, the AFMEN-treated area exhibits lower friction and a higher surface potential. The surface potential of the rGF (Fig. 4(b)) is close to that of pristine graphene (Fig. S2 in the ESM) demonstrating the high degree of the reduction in the former. Note that typically in KPFM, the electrostatic surface potential measured with respect to the conductive cantilever tends to drift

![](./images/813205263422062594_6.jpg)

Figure 3 Resistivity ($\Omega{\cdot}\text{sq.}^{-1}$) of the rGF versus the width of the nanoribbon.

![](./images/813205263422062594_7.jpg)

Figure 4 (a) Topography of a wide graphene nanoribbon chemically isolated in fluorinated graphene. The GNR was produced by selective reduction of fluorinated graphene via electrostatic pressure. (b) A Kelvin probe image of the same nanoribbon along with a labeled histogram of the surface potentials with the potential of the Au electrodes set to 0. (c) Friction image of the same device along with a labeled histogram of the friction forces experienced by the tip.

between measurements and often shows poor repro- ducibility, possibly due to inadvertent contamination of the tip. Consequently, a more reliable value is the potential difference between areas of the same surface recorded in a single measurement. Here the surface potentials are referenced to that of the contacting gold electrodes, whose potential is set to zero.

The non-zero potential of graphene relative to the gold electrodes results from the electron transfer between the graphene and electrodes necessary to align their Fermi levels [22]. The relative surface potential of the graphene $\Delta \varphi_{\text{C-Au}} = 87.1\ \text{meV} \pm 6.6\ \text{meV}$ (see Fig. S1 in the ESM) is comparable to the $\sim$+150 meV potential difference in a previous KPFM experiment [23] without backgating. The relative surface potential of the rGF is slightly lower at $\Delta \varphi_{\text{rGF-Au}} = 77.5\ \text{meV} \pm$ 20.2 meV, a value within the experimental error if one makes the fairly safe assumption that the gold electrodes in the two devices investigated have identical work functions. This suggests that the rGF possesses a work function and electronic structure close to those of pristine graphene. Noting the very different potential difference between the GF and gold electrodes (Fig. 4(b)), our measurements indicate that AFMEN can almost completely reduce the GF. Finally, our measurements indicate that the work function of the fluorinated graphene is some $230\ \text{meV} \pm 57.3\ \text{meV}$ greater than that of graphene (or rGF) and alignment of Fermi levels in the fluorinated and rGF requires electron transfer from the latter to the former. Such electron transfer is consistent with the lateral hole doping of graphene nanoribbons chemically isolated in GF recently reported by us [9].

### 2.3 Effects of tip bias and velocity
The impact of changing the velocity and bias voltage of the AFM probe on reduction quality is presented in Fig. 2. In the first experiment the probe velocity was increased from $1.2\ \mu\text{m·s}^{-1}$ to $12\ \mu\text{m·s}^{-1}$ while the scan area $(6\ \mu\text{m} \times 0.1\ \mu\text{m})$ and bias voltage $(-12\ \text{V})$ remained constant. An AFM tip travelled the entire area four times to draw each nanoribbon. This experiment was essential to determine the optimal tip velocity (between $1.2\ \mu\text{m·s}^{-1}$ and $4\ \mu\text{m·s}^{-1}$) which was later used in further experiments. The purpose of the second experiment was to determine the threshold voltage for fluorine reduction. The AFM tip velocity was held at $1.6\ \mu\text{m·s}^{-1}$ while the scan area was again $6\ \mu\text{m} \times 0.1\ \mu\text{m}$, and exposure time was optimized at 240 s to pattern nanoribbons in GF. The substrate bias was then adjusted from -9 to -12 V. The results show that the minimum voltage required to remove fluorine is -10 V.

### 2.4 Finite element calculations
While it is clear that fluorine is reduced from the GF, these experiments provide only indirect evidence for the mechanism of reduction. Understanding the mechanism is further complicated in that the intense electric fields used can activate multiple processes that lead to reduction. The two most likely processes of fluorine reduction are the polarization of the C–F bond and the generation of reactive species during the hydrolysis of adventitious water. To estimate the electrostatic field present at the GF surface, we used finite element analysis (COMSOL 4.3a) and obtained the electric field distribution between a groundedgold coated AFM tip, modeled as a cone with a $20^\circ$ internal angle terminated by a hemisphere of radius 30 nm, raised by 0.2–1 nm above the 1 nm thick GF.The GF sheet sits on a 100 nm thick thermal $\text{SiO}_2$ film that terminates the highly doped n-Si $(\rho: 5\Omega\text{·cm})$ substrate, the bottom of which is biased at 10 V. The two main unknowns are the dielectric properties of the fluorinated graphene and the composition of the gap between the probe and GF. We assumed the dielectric constant of GF was the same as that of polytetrafluoroethylene $(\varepsilon = 2.1)$ due to their structural similarity. The composition of the gap is more difficult to estimate in that while fluorine may be reduced under nitrogen, more reproducible reduction occurred in the ambient, suggesting that adventitious water may enhance fluorine reduction. The amount of water present would be limited since water wets GF even less than the already hydrophobic graphene; however, high electric fields can draw water into the meniscus [24, 25]. The balance of these forces, and thus whether adventitious water forms a meniscus, is unknown. To set an upper bound on the electric field we chose nitrogen $(\varepsilon\sim1)$ as the gap material with the understanding that the presence of water $(\varepsilon\sim80.1)$ would reduce the field. Figure 5 displays the results

![](./images/813205263422062594_8.jpg)

Figure 5 Electric field at the GF surface as a function of the lateral distance from the probe apex coordinate for (a) a probe held at 0.2, 0.6, and 1.0 nm with a 10 V bias and (b) a probe held at 0.6 nm with -8, -10, and -12 V. The inset in (a) shows the calculated potential.

of the numerical calculations for electric field for a probe held at distances of 0.2, 0.6, and 1.0 nm above the GF (Fig. 2(a)) as well as a tip held at 0.6 nm with biases from 8 to 12 V (Fig. 2(b)), bracketing the con- ditions from Fig. 2. We note that an analytical approach using the method of images gave comparable results (Figs. S2 and S3 in the ESM) [26]. The peak field of ~2 V·nm⁻¹ is comparable both to the field needed to rupture a chemical bond and the field needed to dissociate water (2.5 V·nm⁻¹ by theory [27], 3.2 V·nm⁻¹ by experiment [28]). We will briefly discuss each mechanism as outlined in Fig. 6.

### 2.5 Reduction mechanism.

Previous studies [10-12] have shown that the dissocia- tion of water can drive chemistry with graphene, with either hydrogenation or oxidation possible depending on bias. In our experiments we applied a negative bias to the substrate (i.e., positive tip bias) to defluorinate the material. Since defluorination appears to require at least a low level of relative humidity, we initially assumed that hydrolysis of the water played a role in defluorination.

$$2\ \text{H}_2\text{O} \leftrightarrow \text{OH}^- + \text{H}_3\text{O}^+$$

Given the electrical bias in the experiment, we expect hydronium to be driven to the substrate and the hydroxyl anion to be driven towards the tip; however, the tip-substrate separation is comparable to a single hydration sphere, so both ions would be available for chemistry at the interfaces of GF and tip. To determine whether either $\text{OH}^-$ or $\text{H}_3\text{O}^+$ could remove fluorine, we used XPS to monitor the stability of large

![](./images/813205263422062594_9.jpg)

Figure 6 Two possible mechanisms for the AFMEN reduction of fluorine. (a) Fluorine could be reduced by electric field driven desorption. The electric field due to the negatively biased sample is represented by light blue arrows. (b) Water molecules are dissociated in the meniscus around the AFM tip due to electrolysis. This forms hydronium ($\text{H}_3\text{O}^+$) and hydroxyl ($\text{OH}^-$) ions that can react with the fluorine.

sheets of fluorinated graphene submerged in buffers of different pH for 3 hours by XPS (Fig. 7). From the results it is clear that extended submersion in water alone can reduce much of the fluorine from the surface. At room temperature, there is a secondary effect where higher pH values, and thus higher $OH^-$ concentrations, reduces more fluorine. These results suggest that the drawing of water into a meniscus may be the more significant contribution of the electric field to reduction.

The second potential mechanism for fluorine reduction is field-induced dissociation and desorption of fluorine from the C–F bond (Fig. 6(a)) [29]. In this mechanism, the intense electric field will soften the highly polar C–F bond. The passage of electrons will also stimulate this bond ultimately leading to the desorption of fluorine from the surface. Although the current apparatus for this experiment provides us with the precise gap height and bias on the probe, it does not allow us to measure the current through the system. Determining the relative contributions of these two mechanisms and also influence of water condensation in the vicinity of nanoscale asperities are the goals of ongoing research.

![](./images/813205263422062594_10.jpg)

Figure 7 Loss of fluorine from GF after submersion in a buffered solution at $25\ ^\circ\text{C}$ and $100\ ^\circ\text{C}$ at the stated pH. Loss is greater at higher temperatures and, at room temperature, at higher pH. Note that submersion in pH 10 buffer at $100\ ^\circ\text{C}$ etched the substrate and removed the GF.

## 3 Conclusions
We have demonstrated that the AFMEN process can robustly reduce fluorine from GF to form chemically isolated graphene nanoribbons with dramatically decreased sheet resistivity. The approach requires only commercially available conductive probes which, because the tip does not contact the surface, should wear minimally during fabrication. The technique may be started arbitrarily on the GF substrate and does not require commencing either at an electrode or graphene edge. Given this and the relatively fast lithography speeds ($\mu\text{m·s}^{-1}$), the technique should be sufficient for the routine manufacturing of conducting graphene nanostructures. The next logical steps in this research would be to determine the stability of GF-based devices and the nature of electronic transport through them using variable temperature conductivity measurements.

## Acknowledgments
SFL and JST acknowledge support from the Summer Faculty Program with the Office of Naval Research. They are very thankful to the Chemistry Division of the Naval Research Laboratory for hospitality. PES, ST, JTR, and WKL gratefully acknowledge support from the NRL Nanoscience Institute. KEW is grateful for the NRL/NRC Postdoctoral Fellowship.

Electronic Supplementary Material: Additional information about the analytical solution for pressure and electric field distributions using the method of images of AFM tip–graphene fluoride configurations, KPFM images of unmodified graphene devices, and the experimental procedure to measure the stability of graphene fluoride in buffer solutions can be found in the online version of this article at http://dx.doi.org/10.1007/s12274-013-0355-1.

## References
[1] Dikin, D. A.; Stankovich, S.; Zimney, E. J.; Piner, R. D.; Dommett, G. H. B.; Evmenenko, G.; Nguyen, S. T.; Ruoff, R. S. Preparation and characterization of graphene oxide paper. *Nature* **2007**, 448, 457–460.
[2] Wei, Z. Q.; Wang, D. B.; Kim, S.; Kim, S.-Y.; Hu, Y.; Yakes, M. K.; Laracuente, A. R.; Dai, Z. T.; Marder, S. R.; Berger, C.; et al. Nanoscale tunable reduction of graphene oxide for graphene electronics. *Science* **2010**, 328, 1373–1376.
[3] Robinson, J. T.; Burgess, J. S.; Junkermeier, C. E.; Badescu, S. C.; Reinecke, T. L.; Perkins, F. K.; Zalalutdniov, M. K.; Baldwin, J. W.; Culbertson, J. C.; Sheehan, P. E.; Snow, E. S.

Properties of fluorinated graphene films. *Nano Lett.* 2010, 10, 3001-3005.

[4] Nair, R. R.; Ren, W.; Jalil, R.; Riaz, I.; Kravets, V. G.; Britnell, L.; Blake, P.; Schedin, F.; Mayorov, A. S.; Yuan, S. J.; et al. Fluorographene: A two-dimensional counterpart of teflon. *Small* 2010, 6, 2877-2884.

[5] Bagri, A.; Mattevi, C.; Acik, M.; Chabal, Y. J.; Chhowalla, M.; Shenoy, V. Structural evolution during the reduction of chemically derived graphene oxide. *Nat. Chem.* 2010, 2, 581-587.

[6] Lee, W.-H.; Suk, J.-W.; Chou, H.; Lee, J.; Hao, Y. F.; Wu, Y. P.; Piner, R.; Akinwande, D.; Kim, K. S.; Rouff, R. S. Selective area fluorination of graphene with fluoropolymer and laser irradiation. *Nano Lett.* 2012, 12, 2374-2378.

[7] Sofo, J. O.; Suarez, A. M.; Usaj, G.; Cornaglia, P. S.; Hernandez-Nieves, A.; Balseiro, C. A. Electrical control of the chemical bonding of fluorine on graphene. *Phys. Rev. B* 2011, 83, 081411.

[8] Jeon, K.-J.; Lee, Z.; Pollak, E.; Moreschini, L.; Bostwick, A.; Park, C.-M.; Mendelsberg, R.; Radmilovic, V.; Kostecki, R.; Richardson, T. J.; et al. Fluorographene: A wide bandgap semiconductor with ultraviolet luminescence. *ACS Nano* 2011, 5, 1042-1046.

[9] Lee, W.-K.; Robinson, J. T.; Gunlycke, D.; Stine, R. R.; Tamanaha, C. R.; King, W. P.; Sheehan, P. E. Chemically isolated graphene nanoribbons reversibly formed in fluorographene using polymer nanowire masks. *Nano Lett.* 2011, 11, 5461-5464.

[10] Withers, F.; Bointon, T. H.; Dubois, M.; Russo, S.; Craciun, M. F. Nanopatterning of fluorinated graphene by electron beam irradiation. *Nano Lett.* 2011, 11, 3912-3916.

[11] Giesbers, A. J. M.; Zeitler, U.; Neubeck, S.; Freitag, F.; Novoselov, K. S.; Maan, J. C. Nanolithography and manipulation of graphene using an atomic force microscope. *Solid State Commun.* 2008, 147, 366-369.

[12] Masubuchi, S.; Arai, M.; Machida, T. Atomic force micros- copy based tunable local anodic oxidation of graphene. *Nano Lett.* 2011, 11, 4542-4546.

[13] Weng, L.; Zhang, L.; Chen, Y. P.; Rokhinson, L. P. Atomic force microscopy local oxidation of graphene. *Appl. Phys. Lett.* 2008, 93, 112102.

[14] Byun, I. S.; Yoon, D.; Choi, J. S.; Hwang, I.; Lee, D. H.; Lee, M. J.; Kawai, T.; Son, Y.-W.; Jia, Q. X.; Cheong, H.; Park, B. H. Nanoscale lithography on monolayer graphene using hydrogenation and oxidation. *ACS Nano* 2011, 5, 6417-6424.

[15] Lyuksyutov, S. F.; Vaia, R. A.; Paramonov, P. B.; Juhl, S.; Waterhouse, L.; Ralich, R. M.; Sigalov, G.; Sancaktar, E. Electrostatic nanolithography in polymers using atomic force microscopy. *Nat. Mater.* 2003, 2, 468-472.

[16] Juhl, S.; Phillips, D.; Vaia, R. A.; Lyuksyutov, S. F.; Paramonov, P. B. Precise formation of nanoscopic dots on polystyrene film using z-lift electrostatic lithography. *Appl. Phys. Lett.* 2004, 85, 3836-3838.

[17] Lafkioti, M.; Krauss, B.; Lohmann, T.; Zschieschang, U.; Klauk, H.; von Klitzing, K.; Smet, J. H. Graphene on a hydrophobic substrate: Doping reduction and hysteresis suppression under ambient conditions. *Nano Lett.* 2010, 10, 1149-1153.

[18] Tramšek, M.; Žemva, B. Synthesis, properties and chemistry of Xenon(II) fluoride. *Acta Chim. Slov.* 2006, 53, 105-116.

[19] Kwon, S.; Ko, J. H.; Jeon, K. H.; Kim, Y. H.; Park, J. Enhanced nanoscale friction on fluorinated graphene. *Nano Lett.* 2012, 12, 6043-6048.

[20] Ko, J.-H.; Kwon, S.; Byun, I.-S.; Choi, J. S.; Park, B. H.; Kim, Y.-H.; Park J. Y. Nanotribological properties of fluorinated, hydrogeneted and oxidized graphenes. *Tribol. Lett.* 2013, 50, 137-144.

[21] Behnam, A.; Noriega, L.; Choy, Y.; Wu, Z. C.; Rinzler, A. G.; Ural, A. Resistivity scaling in single-walled carbon nanotube films patterned to submicron dimensions. *Appl. Phys. Lett.* 2006, 89, 093107.

[22] Giovannetti, G.; Khomyakov, P. A.; Brocks, G.; Karpan, V. M.; van den Brink, J.; Kelly, P. J. Doping graphene with metal contacts. *Phys. Rev. Lett.* 2008, 101, 026803.

[23] Yu, Y. J.; Zhao, Y.; Ryu, S.; Brus, L. E.; Kim, K. S.; Kim, P. Tuning the graphene work function by electric field effect. *Nano Lett.* 2009, 9, 3430-3434.

[24] Calleja, M.; Tello, M.; Garcia, R. Size determination of field- induced water menisci in noncontact atomic force microscopy. *J. Appl. Phys.* 2002, 92, 5539-5542.

[25] Garcia, R.; Calleja, M.; Rohrer, H. Patterning of silicon surfaces with noncontact atomic force microscopy: Field- induced formation of nanometer-size water bridges. *J. Appl. Phys.* 1999, 86, 1898-1903.

[26] Lyuksyutov, S. F.; Paramonov, P. B.; Sharipov, R. A.; Sigalov, G. Induced nanoscale deformations in polymers using atomic force microscopy. *Phys. Rev. B* 2004, 70, 174110.

[27] Saitta, A. M.; Saija, F.; Giaquinta, P. V. *Ab initio* molecular dynamics study of dissociation of water under an electric field. *Phys. Rev. Lett.* 2012, 108, 207801.

[28] Rothfuss, C. J.; Medvedev, V. K.; Stuve, E. M. The influence of the surface electric field on water ionization: A two step dissociative ionization and desorption mechanism for water ion cluster emission from a platinum field emitter tip. *J. Electroanal. Chem.* 2003, 554, 133-143.

[29] Avouris, Ph.; Walkup, R. E.; Rossi, A. R.; Akpati, H. C.; Nordlander, P.; Shen, T.-C.; Abeln, G. C.; Lyding, J. W. Breaking individual chemical bounds via STM-induced excitations. *Surf. Sci.* 1996, 363, 368-377.

![](./images/813205263422062594_11.jpg)