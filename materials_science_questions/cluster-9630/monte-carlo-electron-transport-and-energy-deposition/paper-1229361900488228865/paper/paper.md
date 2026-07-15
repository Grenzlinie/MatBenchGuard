# Photoneutron Yield for an Electron Beam on Tantalum and Erbium Deuteride

Andrew K. Gillespie $^{a*}$, Cuikun Lin $^{a}$, and R. V. Duncan $^{a}$

## AFFILIATIONS

$^{a}$Department of Physics and Astronomy, Texas Tech University, Lubbock Texas 79409, USA

*Author to whom correspondence should be addressed: a.gillespie@ttu.edu

## ABSTRACT

An electron beam may be used to generate bremsstrahlung photons that go on to create photoneutrons within metals. This serves as a low-energy neutron source for irradiation experiments [1-3]. In this article, we present simulation results for optimizing photoneutron yield for a 10-MeV electron beam on tantalum foil and erbium deuteride (ErD₃). The thickness of the metal layers was varied. A tantalum foil thickness of 1.5 mm resulted in the most photons reaching the second metal layer. When a second metal layer of ErD₃ was included, the photoneutron yield increased with the thickness of the secondary layer. When the electron beam was directly incident upon a layer of ErD₃, the photoneutron yield did not differ significantly from the yield when a layer of tantalum was included. The directional photoneutron yield reached a maximum level when the thickness of the ErD₃ layer was around 12 cm. About 1 neutron was generated per $10^4$ source electrons. When using a 2-mA beam current, it is possible to generate up to $10^{12}$ neutrons per second, making this combination a relatively-inexpensive neutron generator.

## I. INTRODUCTION

In 1932, James Chadwick announced the discovery of the neutron. Since then, this groundbreaking finding has led to numerous applications across various fields, including the utilization of neutrons in fusion reactors, the geochronological dating of rocks, the development of non-intrusive inspection techniques based on neutron technology, the use of radioisotopes for radiotherapy, medical imaging advancements, and even pain relief techniques. [4]

However, a major obstacle in the further advancement of these applications is often the lack of suitable neutron sources. There are many ways to produce neutrons, including: (1) Alpha neutron sources (2) Gamma neutron sources (3) Spontaneous fission neutron sources such as Cf-252. (4) Fission reactors (5) Accelerators. This also includes D-D (deuterium-deuterium) neutron generators and D-T (deuterium-tritium) neutron generators. Table 1 provides a summary of the different types of neutron sources along with their respective yields.

**Table 1:** Neutron sources and respective yields

<table>
  <thead>
    <tr>
      <th></th>
      <th>Source</th>
      <th>Target</th>
      <th>Most Common Yield [5]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Alpha Neutron Sources</td>
      <td>Am-241; Pu-238, Pu-239, Po-210; Ra-226</td>
      <td>Be, Li, F, B</td>
      <td>AmBe 2.0-2.4x10⁶ neutrons/sec. per Ci <br> PuBe, 1.5-2.0 x10⁶ n/s per Ci</td>
    </tr>
    <tr>
      <td>Gamma Neutron Source</td>
      <td>Gamma emitting core</td>
      <td>Be-9; D; mix of Sb-124 and Be-9</td>
      <td>0.2-0.3 x10⁶ n/s per Ci</td>
    </tr>
    <tr>
      <td>Spontaneous Fission Sources</td>
      <td>Cf-252</td>
      <td></td>
      <td>4.4 x10⁹ n/s per Ci</td>
    </tr>
    <tr>
      <td>Fission Reactors</td>
      <td>²³⁵U + n → ²³⁶U <br> → ¹⁴¹Ba + ⁹²Kr + 3n</td>
      <td></td>
      <td>10¹² to 10¹⁵ n/cm² s – <br> 10¹² n/s per megawatt (MW)</td>
    </tr>
    <tr>
      <td>Accelerators</td>
      <td>betatron, synchrotron and linear accelerators</td>
      <td>Be-9; D, Ta, W, Pb</td>
      <td>10¹² n/s</td>
    </tr>
    <tr>
      <td></td>
      <td>D</td>
      <td>Ti/D, Ti/T</td>
      <td>10⁶-10⁹ n/s, 10⁹-10¹⁰ n/s</td>
    </tr>
  </tbody>
</table>

Commercially-available neutron generators can cost between $100,000 - $300,000 depending on the model and desired neutron output. [6] Among the various options, nuclear fission reactors undoubtedly provide the highest neutron flux. However, these reactors are often not readily available or easily constructed. The costs associated with building new nuclear units are substantial, with estimates ranging from $5,500/kW to $8,100/kW or between $6 billion and $9 billion for each 1,100 MW plant, considering factors such as escalation and financing costs [7]. While Cf252 is an option for neutron production, it is generally not suitable for long-term usage due to its short half-life and high price, exceeding $2 million per Curie. Overall, a neutron source with a high thermal neutron flux that is economically viable and suitable for installation in industries or clinics is not widely available. Among the remaining options, the use of electron accelerators with low beam energies to produce neutrons through the $(\gamma, n)$ reaction has garnered significant attention due to the availability and comparably lower cost of such accelerators as listed in **Table 2**.

**Table 2:** Commercially available electron generators

<table>
  <thead>
    <tr>
      <th>Manufacture</th>
      <th>Electron Beam<br>Accelerator Model <sup>[8]</sup></th>
      <th>Type</th>
      <th>Energy (MeV)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="5">IBA Industrial<br>Solutions</td>
      <td>TT-50</td>
      <td>RF-SCR</td>
      <td>10</td>
    </tr>
    <tr>
      <td>TT-100</td>
      <td>RF-SCR</td>
      <td>10</td>
    </tr>
    <tr>
      <td>TT-200</td>
      <td>RF-SCR</td>
      <td>10</td>
    </tr>
    <tr>
      <td>TT-300</td>
      <td>RF-SCR</td>
      <td>10</td>
    </tr>
    <tr>
      <td>TT-1000</td>
      <td>RF-SCR</td>
      <td>7.5</td>
    </tr>
    <tr>
      <td>NIIEFA</td>
      <td>UEL-10-D</td>
      <td>RF-Linac</td>
      <td>10</td>
    </tr>
    <tr>
      <td>NIIEFA</td>
      <td>Elektron 23</td>
      <td>DC</td>
      <td>1</td>
    </tr>
    <tr>
      <td>BINP</td>
      <td>ILU-10</td>
      <td>RF-SCR</td>
      <td>5</td>
    </tr>
    <tr>
      <td>BINP</td>
      <td>ILU-14</td>
      <td>RF-Linac</td>
      <td>10</td>
    </tr>
    <tr>
      <td>BINP</td>
      <td>ELV-12</td>
      <td>DC</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Varian</td>
      <td>Linatron</td>
      <td>RF-Linac</td>
      <td>9</td>
    </tr>
    <tr>
      <td>Mevex</td>
      <td>Linac</td>
      <td>RF-Linac</td>
      <td>3</td>
    </tr>
    <tr>
      <td>Wasik Assoc.</td>
      <td>ICT</td>
      <td>DC</td>
      <td>3</td>
    </tr>
    <tr>
      <td>Getinge Group</td>
      <td>Linac</td>
      <td>RF-Linac</td>
      <td>10</td>
    </tr>
    <tr>
      <td>Vivirad S.A.</td>
      <td>ICT</td>
      <td>DC</td>
      <td>5</td>
    </tr>
  </tbody>
</table>

One of the notable highlights on the list is the compact TT50 Rhodotron™. The design objective for this unit is to achieve a beam energy of 10 MeV and a power output of 20 kW using 80 cm cavity diameter unit [9]. With its impressive energy efficiency of 20%, this unit will serve as an excellent tool for small- to medium-sized service providers as well as research and development institutions. FARSHID et al. estimated a neutron flux of $10^{12}$ n/cm²/s, with average energies of 0.9 MeV, 0.4 MeV, and 0.9 MeV for Pb, Ta, and W targets, respectively, using the RHODOTRON TT200 (IBA) accelerator, as detailed in [10]. Chakhlov et al. also reported using 10 MeV electrons to produce bremsstrahlung beams that irradiated LiD, Be, depleted U, and Pb targets to generate photoneutrons [11,12]. **Figure 1** illustrates a typical design of the photoneutron generator. In this setup, when an accelerated electron beam interacts with a Bremsstrahlung target such as Ta, W, or Pb, Bremsstrahlung radiation is emitted. The total energy and yield of photons generated from the target at various thicknesses are significant parameters to take into account in this process [13].

![](./images/1229361900488228865_1.jpg)

Figure 1: A simplified model of a photoneutron generator involving an electron beam incident on tantalum, tungsten, or lead. Photons are created and participate in (γ, n) reactions. [14]

Tsechanski [15] and Berger [16] have demonstrated that when the target thickness exceeds the optimal value, the efficiency decreases due to a greater absorption of braking radiation within the target material. It is important to note that neutrons can also be generated using electrons with an energy of 10 MeV. According to Mahmod et al., by using a 10 MeV electron source and directing it towards a 2 cm-thick Pb material, the estimated photoneutron yield is $1.7x10^{-5}$ photoneutrons per electron. [17]. This implies that for a 10 kW accelerator with a 10 MeV and 1 mA electron source, the neutron production would be approximately $10^{11}$ n/s. This production rate is comparable to D-D neutron generators and D-T neutron generators but comes at considerably higher cost. This is mainly due to the high threshold energies (>6 MeV) required by these high atomic number (Z) materials, resulting in limited photon utilization and lower cross sections. Table 3 provides an overview of materials along with their corresponding high threshold reactions for neutron generation.

Table 3: Materials and high threashold reactions for neutron generation [10,18]

<table>
  <thead>
    <tr>
      <th>Nuclei</th>
      <th>Threshold (MeV)</th>
      <th>Isotope Abundance (%)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>²⁰⁶Pb</td>
      <td>8.09</td>
      <td>24.1</td>
    </tr>
    <tr>
      <td>²⁰⁷Pb</td>
      <td>6.74</td>
      <td>22.1</td>
    </tr>
    <tr>
      <td>²⁰⁸Pb</td>
      <td>7.37</td>
      <td>52.4</td>
    </tr>
    <tr>
      <td>¹⁸¹Ta</td>
      <td>7.58</td>
      <td>99.9</td>
    </tr>
    <tr>
      <td>¹⁸⁰W</td>
      <td>8.41</td>
      <td>0.12</td>
    </tr>
    <tr>
      <td>¹⁸²W</td>
      <td>8.07</td>
      <td>26.3</td>
    </tr>
    <tr>
      <td>¹⁸³W</td>
      <td>6.19</td>
      <td>14.3</td>
    </tr>
    <tr>
      <td>¹⁸⁴W</td>
      <td>7.41</td>
      <td>30.7</td>
    </tr>
    <tr>
      <td>¹⁸⁶W</td>
      <td>7.19</td>
      <td>28.6</td>
    </tr>
  </tbody>
</table>

Another viable option for photoneutron production is to utilize low threshold materials. Table 4 provides an overview of materials along with their corresponding low threshold reactions for neutron generation. D (deuterium) and Be-9 (beryllium-9) are particularly noteworthy due to their low binding energies of 2.23 MeV and 1.66 MeV, respectively. In a recent study conducted by a team at NASA-Glenn SFC, a novel d+D fusion process in metals was investigated at low deuteron projectile energy but under high-flux gamma radiation. Steinetz *et al.* [3] performed experimental investigations utilizing an electron beam. The electron beam had an energy range of 0.45 to 3.0 MeV and a current of 10 to 30 mA, which was directed towards a tantalum target. By generating bremsstrahlung X-rays up to 2.9 MeV, the beam irradiated both ErD₃ and TiD₂ samples, resulting in the production of photo-neutrons. By leveraging these low threshold materials, more efficient and cost-effective photoneutron generation can be achieved.

**Table 4: Materials and low threshold reactions**

<table>
  <thead>
    <tr>
      <th>Nuclide</th>
      <th>Threshold (MeV)</th>
      <th>Reaction</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$^2$D</td>
      <td>2.23</td>
      <td>$^2$H(γ,n)$^1$H</td>
    </tr>
    <tr>
      <td>$^6$Li</td>
      <td>3.70</td>
      <td>$^6$Li(γ,n+p)$^4$He</td>
    </tr>
    <tr>
      <td>$^6$Li</td>
      <td>5.67</td>
      <td>$^6$Li(γ,n)$^5$Li</td>
    </tr>
    <tr>
      <td>$^7$Li</td>
      <td>7.25</td>
      <td>$^7$Li(γ,n)$^6$Li</td>
    </tr>
    <tr>
      <td>$^9$Be</td>
      <td>1.67</td>
      <td>$^9$Be(γ,n)$^8$Be</td>
    </tr>
    <tr>
      <td>$^{13}$C</td>
      <td>4.90</td>
      <td>$^{13}$C(γ,n)$^{12}$C</td>
    </tr>
  </tbody>
</table>

To further comprehend and optimize the neutron yield, comprehensive simulations were conducted in our paper. The objective was to optimize the photoneutron yield using a 10-MeV electron beam incident on tantalum foil and erbium deuteride. The simulations involved varying the thickness of the metal layers and ErD₃ layers in order to explore the impact on the neutron generation process.

## II. METHODS AND SIMULATION GEOMETRY

Three simulation sets were performed using Monte Carlo n-Particle (MCNP™ 6.2) transport calculations [19]. All simulations used the same 10-MeV electron beam as a planar source. All simulations used one hundred million histories in their calculations. Two vacuum spaces were included before and after the metal layers to determine particle counts. The first set of simulations involved a disk layer of tantalum metal with a radius of 2.0 cm. The second set involved a cylinder of erbium deuteride with a radius of 10.0 cm. The third set involved both a layer of tantalum and a layer of erbium. These simulation geometries are shown in **Figure 2**.

![](./images/1229361900488228865_2.jpg)

Figure 2: Left: Simulation set #1 involving only a layer of tantalum. Right: Simulation set #3 involving a 1.5 mm-thick layer of tantalum and a layer of erbium deuteride. Simulation set #2 uses this same geometry template as in simulation set #3 with the tantalum layer removed.

For simulations involving the 10-cm radius cylinder of ErD₃, an additional tally region was added surrounding the cylindrical wrap. This tally zone, along with the tally region behind the metal layers, allowed for the detection of any particles escaping the layers in specific directions of interest. Though ErD₃ has a crystal density near 7.6 g/mL, the synthesis process often involves embrittlement of the metal. When in powder form, ErD₃ has a tap density near 3.8 g/mL. Therefore, this 50% packing fraction was used for the ErD₃ layer within these simulations.

Within MCNP, the F4 tally calculates the track length estimate of cell flux in units of [1/cm²]. This is calculated by multiplying the importance weight by the track length and is normalized by the cell volume. When multiplied by the source strength in particles per second, this results in the average flux across the tally zone in units of [particles/s/cm²]. The F4 tally can be useful in estimating the neutron yield reaching a volume of interest. The F4 tally may also be split into energy bins to obtain an energy spectrum of particles entering the zone. MCNP is also able to output particle tracks entering each defined volume cell.

## III. RESULTS AND DISCUSSIONS

To investigate the number of electrons transmitted through the tantalum layer, particles entering the first and second tally regions were compared. The percent of electrons reaching the tally region behind the tantalum is shown in Figure 3.

![](./images/1229361900488228865_3.jpg)

**Figure 3:** The percentage of electrons reaching the tally region behind the tantalum layer as the thickness of the layer is varied.

For layers $<1\ \mu\text{m}$, almost all of the 10-MeV electrons are transmitted through the tantalum to the second tally region. For thicker layers $>0.5$ cm, electrons interact significantly and almost zero electrons are transmitted. When the tantalum layer is still thin, but only about 50% of electrons are transmitted, the deccelerating electrons create bremsstrahlung radiation that is able to escape the tantalum layer. There should be an optimal tantalum thickness that permits the maximum amount of bremsstrahlung photons to escape and continue on to generate photoneutrons. **Figure 4** displays the number of photons created as a function of tantalum thickness.

![](./images/1229361900488228865_4.jpg)

Figure 4: The number of photons created as the thickness of the tantalum layer is varied. The total number of photons created increases with tantalum thickness.

The number of photons created increases with thickness of the tantalum layer. However, only the photons that escape the layer will go on to generate photoneutrons in a secondary metal layer. It is more enlightening to investigate the photon tallies in a region immediately behind the tantalum layer. Figure 5 displays the F4 photon tally within the vacuum region immediately behind the tantalum

![](./images/1229361900488228865_5.jpg)

Figure 5: The average track length estimate for photons reaching the tally region behind the tantalum layer as the thickness of the layer is varied. When the source strength, in units of [particles/s], is multiplied by this tally, one obtains the average flux in units of [particles/s/cm²].

A tantalum foil thickness of 1.5 mm resulted in the most photons reaching the second metal layer. Steinetz et al. used a tantalum foil with a thickness of 1.2 mm, which yields a high photon tally very close to the peak in this series of simulations. The energy spectrum of these photons is also moderated with increasing tantalum thickness. As more electrons interact with the layer, more photons are created. However, with increased layer thickness, fewer of those photons are able to escape and reach the tally zone. Figure 6 displays the energy spectrum of the photons reaching the tally zone.

![](./images/1229361900488228865_6.jpg)

**Figure 6:** The bremsstrahlung photon energy spectrum with varied tantalum thickness.

For a tantalum foil with a thickness near 1.5 mm, prominent peaks around 60 keV, between 230 – 310 keV, and around 520 keV are observed. These photon spectra are comparable to those calculated by Huang *et al.* which shows a similar peak around 0.5 MeV.[20] Maximizing the number of photons reaching the secondary metal layer will result in the most photoneutrons being generated. The tantalum foil thickness was set to 1.5 mm and a secondary layer of ErD₃ was added to the system. **Figure 7** displays the number of neutrons generated in these layers as a function of the ErD₃ layer thickness.

![](./images/1229361900488228865_7.jpg)

**Figure 7:** *Left:* The photoneutrons generated as a function of increasing ErD₃ thickness. *Right:* The total number of photoneutrons created when the electron beam is incident on tantalum and erbium deuteride versus when the beam is incident only upon the erbium deuteride.

When a second metal layer of ErD₃ was included, the photoneutron yield increased with the thickness of the secondary layer. When the electron beam was directly incident upon a layer of ErD₃, the photoneutron yield was not significantly different from the yield when a layer of

tantalum was included. Therefore, it is not beneficial to include the tantalum layer, and instead, run the electron beam directly into the ErD₃ layer to generate the most neutrons.

Many applications of neutron generators are interested in maximizing the neutron flux in a specific direction. In this case, it is important to focus only on the number of neutrons reaching the tally zone behind the ErD₃ layer, shown in Figure 8.

![](./images/1229361900488228865_8.jpg)

**Figure 8:** The photoneutrons entering the tally zone behind the ErD₃ as a function of increasing ErD₃ thickness. Results are shown for cases when the electron beam is incident on tantalum and erbium deuteride versus when the beam is incident only upon the erbium deuteride.

A smaller fraction of photoneutrons exit the layer along the same axis as the source. This reaches a peak when the thickness of the ErD₃ layer is around 12 cm. A thicker layer results in a higher amount of neutrons being generated overall, but the amount that exit through the back of the ErD₃ layer decreases with increasing layer thickness. As shown in Figure 9, The average energy of the photoneutrons escaping the layers did not change significantly with layer thickness.

![](./images/1229361900488228865_9.jpg)

**Figure 9:** The energy spectrum of photoneutrons entering the tally zone behind the ErD₃ layer of 12-cm thickness.

The weighted average energy of these directional photoneutrons is near 14 keV. Across all simulations, nearly all neutrons were generated from photodissociation and only between 0.02 – 0.03% were created from (n, xn) reactions within the metals.

All simulations used one hundred million histories in their calculations. Overall, about 1 neutron is generated per $10^4$ source electrons in the beam. Only about 1 directional neutron is generated per $10^6$ source electrons in the beam. A Rhodotron TT50 operates with a 2 mA beam current and 20 kW producing 10-MeV electrons. Since one amp is $6.28x10^{18}$ electrons per second, this 2-mA source should generate about $1.2x10^{16}$ electrons per second. Therefore, this setup would generate about $1.2x10^{12}$ neutrons per second overall and $1.2x10^{10}$ directional neutrons per second.

This demonstrates the feasibility of using an electron beam and bremsstrahlung photons, to generate photoneutrons. Depending on the model specifications, electron generators may be run with low power consumption. When using a 2-mA beam current, it is possible to generate up to around $10^{12}$ neutrons per second, making this combination a relatively-inexpensive neutron generator.

## IV. CONCLUSIONS

The bremsstrahlung photon and photoneutron yield was simulated for a 10-MeV electron beam incident on tantalum foil and erbium deuteride. A tantalum foil thickness of 1.5 mm resulted in the most photons reaching the second metal layer. The directional photoneutron yield reached a maximum level when a 12 cm-thick layer of erbium deuteride was included behind the tantalum layer. When using a 2-mA beam current, it is possible to generate up to $10^{12}$ neutrons per second, making this combination a relatively-inexpensive neutron generator that could be employed in numerous applications, including fusion research.

## V. ACKNOWLEDGEMENTS

The authors would like to thank Dr John Gahl at the University of Missouri for their useful discussions. This work was supported by NIAC Phase I contract No. 80NSSC23K0592 and the Texas Research Incentive Program, and by Texas Tech University. The identification of commercial products, contractors, and suppliers within this article are for informational purposes only, and do not imply endorsement by Texas Tech University, their associates, or their collaborators.

## VI. DATA AVAILABILITY

The data that support the findings of this study are available from the corresponding author upon reasonable request.

## VII. REFERENCES

1.  V. Pines, et al., "Nuclear Fusion Reactions in Deuterated Metals", NASA TP-20205001617, and Phys. Rev. C 101, 044609 (2020)

2.  T.L. Benyo and L.P. Forsley, "MCNP Fusion Modeling of Electron-Screened Ions", 2021 MCNP® User Symposium, Los Alamos National Laboratory

3.  B. Steinetz, et al., "Novel nuclear reactions observed in bremsstrahlung-irradiated deuterated metals", NASA TP-20205001616, and Phys. Rev. C 101, 044610 (2020)

4.  T. P. Lou, "Compact D-D / D-T Neutron Generators and Their Applications," University of California, 2003.

5.  United States Nuclear Regulatory Commission, Neutron Sources, Basic Health Physics, 0751 - H122 - 25 (2010); https://www.nrc.gov/docs/ML1122/ML11229A704.pdf.

6.  International Atomic Energy Agency, Neutron Generators for Analytical Purposes, IAEA Radiation Technology Reports No. 1, IAEA, Vienna (2012)

7.  D. Schlissel and B. Biewald, Nuclear Power Plant Construction Costs. Synapse Energy Economics, Inc. (July 2008)

8.  United States Department of Energy, "Workshop on Energy and Environmental Applications of Accelerators." June 24-26, 2015.

9.  Andrzej, G. Chmielewski. Future developments in radiation processing. In Applications of Ionizing Radiation in Materials Processing, 1st ed.; Sun, Y., Ed.; Institute of Nuclear Chemistry and Technology: Warsaw, Poland, 2017; pp. 501–516.

10. Tabbakh, F., Aldaavati, M. M., Hoseyni, M. S. et al. "Induced photonuclear interaction by Rhodotron-TT200 10 MeV electron beam." Pramana - J Phys 78, 257–264 (2012). https://doi.org/10.1007/s12043-011-0232-y

11. V.L. Chakhlov et al. Nucl. Instr. and Meth. in Phys. Res. A 422 (1999) 5—9

12. V. P. Kovalev, Secondary Radiations in Electron Accelerators (Atomizdat, Moscow, 1979).

13. I. K. Alhagaish, V. K. Sakharov, Characterization of Bremsstrahlung Radiation for 10 – 30 and 60-MeV Electron Beam from Thick Tungsten. International Journal of Scientific & Technology Research, Vol9, 06 (June 2020)

14. J. Gahl and G. Dale, Method and Apparatus for Generating Thermal Neutrons Using and Electron Accelerator. U.S Patent No. US8666015B2 (2014).

15. A. Tsechanski, A.F. Bielajew, J.P. Archambault, E. Mainegra-Hing, Electron accelerator-based production of molybdenum-99: Bremsstrahlung and photoneutron generation from molybdenum vs. tungsten, Nuclear Instruments and Methods in Physics Research Section B: Beam Interactions with Materials and Atoms, Volume 366, 2016, Pages 124-139.

16. M. J. Berger and S. M. Seltzer. Bremsstrahlung and photoneutrons from thick tungsten and tantalum targets. Phys. Rev. C, 2:621–631, Aug 1970. 5, 6

17. M. B. Zarandi, F. Tabbakh, and H. A. Bioki, "Neutron generation from 10MeV electron beam to produce 99Mo," Int. J. Sci. Eng. Tech. 4, 1–4 (2015).

18. B. L. Berman, At. Data Nucl. Data Tables, 15: 319-390 (1975)

19. J. A. Kulesza, et al. MCNP® Code Version 6.3.0 Theory & User Manual. Los Alamos National Laboratory Tech. Rep. LA-UR-22-30006, Rev. 1. Los Alamos, NM, USA. September 2022.

20. W. L. Huang et al. Nucl. Instr. and Meth. in Phys. Res. B 229 (2005) 339–347