![](./images/812730097223073794_1.jpg)

Subscriber access provided by UNIV OF DURHAM

# Functional Inorganic Materials and Devices

## High Performance $\boldsymbol{\mu}$-Thermoelectric Device
based on Bi2Te3/Sb2Te3 p-n Junctions

Eliana Vieira, Ana L. Pires, José P. B. Silva, Vítor H. Magalhães, José Eduardo da Siva Ferreira Grilo, Francisco P. Brito, Manuel Silva, André M Pereira, and Luis M. Goncalves

ACS Appl. Mater. Interfaces, Just Accepted Manuscript • DOI: 10.1021/acsami.9b13254 • Publication Date (Web): 27 Sep 2019

Downloaded from pubs.acs.org on September 28, 2019

## Just Accepted

"Just Accepted" manuscripts have been peer-reviewed and accepted for publication. They are posted online prior to technical editing, formatting for publication and author proofing. The American Chemical Society provides "Just Accepted" as a service to the research community to expedite the dissemination of scientific material as soon as possible after acceptance. "Just Accepted" manuscripts appear in full in PDF format accompanied by an HTML abstract. "Just Accepted" manuscripts have been fully peer reviewed, but should not be considered the official version of record. They are citable by the Digital Object Identifier (DOI®). "Just Accepted" is an optional service offered to authors. Therefore, the "Just Accepted" Web site may not include all articles that will be published in the journal. After a manuscript is technically edited and formatted, it will be removed from the "Just Accepted" Web site and published as an ASAP article. Note that technical editing may introduce minor changes to the manuscript text and/or graphics which could affect content, and all legal disclaimers and ethical guidelines that apply to the journal pertain. ACS cannot be held responsible for errors or consequences arising from the use of information contained in these "Just Accepted" manuscripts.

is published by the American Chemical Society. 1155 Sixteenth Street N.W., Washington, DC 20036
Published by American Chemical Society. Copyright © American Chemical Society.
However, no copyright claim is made to original U.S. Government works, or works produced by employees of any Commonwealth realm Crown government in the course of their duties.

# High Performance $\boldsymbol{\mu}$-Thermoelectric Device based on $\boldsymbol{Bi_2Te_3/Sb_2Te_3}$ $\boldsymbol{p}$-$n$ Junctions

E M. F. Vieira $^{1*}$, A. L. Pires $^{2}$, J. P. B. Silva $^{3}$, V. H. Magalhães$^{1}$, J. Grilo$^{1}$, F. P. Brito$^{4}$, M. F. Silva$^{1}$, A. M. Pereira $^{2}$ and L. M. Goncalves$^{1}$

$^{1}$ Universidade do Minho, CMEMS—UMINHO, Campus Azurem, 4804-533 Guimaraes, Portugal

$^{2}$ IFIMUP and IN-Institute of Nanoscience and Nanotechnology, Departamento de Fisica e Astronomia, Faculdade de Ciências da Universidade do Porto, Universidade do Porto, Rua do Campo Alegre 687, 4169-007 Porto, Portugal

$^{3}$ Centro de Fisica das Universidades do Minho e do Porto (CF-UM-UP), Campus de Gualtar, 4710-057 Braga, Portugal

$^{4}$ MEtRICs, University of Minho, Mechanical Engineering Dept., Campus de Azurem,4800 Guimaraes, Portugal

* Corresponding author, Tel./Fax: + 351 – 253 – 510190/189; E-mail addresses: evieira@dei.uminho.pt (E. M. F. Vieira)

## Abstract
A flexible and ultralight planar thermoelectric generator based on 15 thermocouples composed by $n$-type bismuth telluride ($Bi_2Te_3$) and $p$-type antimony telluride ($Sb_2Te_3$) legs (each with 400 nm thick) connected in series, on 25 - $\mu$m thick Kapton® substrate, was fabricated with impressive power factor values of 2.7 mW K⁻² m⁻¹ and 0.8 mW K⁻² m⁻¹ (at 298 K) for $Bi_2Te_3$ and $Sb_2Te_3$ films, respectively. The p-n junction thermoelectric device can generate a maximum open-circuit voltage and output power of 210 mV and 0.7 $\mu$W (3.3 mW cm⁻²), respectively, for a temperature difference of 35 K, which is higher than the one observed for a conventional thermoelectric device with metallic contacts for p-n junctions. The results were combined with numerical simulations showing a good match between the experimental and the numerical results. The current density versus voltage (J-V) characteristics of the fabricated p-n junctions revealed a diode behavior with a turn-on voltage of $\approx$ 0.3 V and an impressive rectifying ratio ($I_{+1V}/I_{-1V}$) of $\approx 2 \times 10^4$.

## Keywords
$\mu$-thermoelectric generator; p-n junctions; telluride alloys; flexible device, COMSOL software

### 1. Introduction

Energy losses in the industrial processes are very significant; the inefficiency caused by these losses mostly, in the form of heat, contributes to global warming representing up to 60% of the total energy consumption. A thermoelectric generator (TEG) can convert the thermal energy contained in small thermal gradients directly into electrical energy. The TEG offers many advantages such as the absence of moving parts, maintenance free, noise-free operation, low failure rate, no chemical reactions, scalability and modularity and it can adopt rigid or flexible forms $^1$, taking into account the source power design. The main drawback of the TEG is their low efficiency compared with other types of power generation $^2$. Despite this, there are often the only viable way for powering Micro Electro Mechanical Devices (MEMS) located in remote locations by using small temperature gradients. However, over the past years, new, more performant materials have been developed and TEGs have been developed for photovoltaic, automotive, military, aerospace applications $^3$, and sensors for fluid flow measurement, and bio-chemical applications $^{4-8}$.

Moreover, flexible TEGs have many advantages over rigid TEGs; lightweight, very thin profile, easy portability, easily attached to the curved surface, and having the ability to cover a large surface area $^{9,10}$. A classic TEG architecture consists of a series of intercalated $p$- and $n$-type semiconductors where the deposition of metal makes the electrical connection between the $p$ and $n$ legs $^{11}$. It has been reported that the resistance between the semiconductor and the metal contact ($\text{R}_{\text{contact}}$) is mentioned as one of the main causes for a high device internal resistance $^{12,13}$. For TE applications, $\text{R}_{\text{cont}}$ must be small, typically between $10^{-10}$ to $10^{-5}\ \Omega\ \text{cm}^2$ $^{14,15}$. Particularly, R. McCarty $^{15}$ reported that the optimal design of a typical TEG is mainly dependent on the minimization of the $\text{R}_{\text{cont}}$, based on theoretical models. Changes in the output power of the TEG of less than 2% are observed for $\text{R}_{\text{cont}}$ between 0 and $1\ \text{x}\ 10^{-5}\ \Omega\ \text{cm}^2$. Furthermore, the hot side metal degradation can be observed for high-temperature device applications (such as in the industrial processes). Recently, R. Chavez *et al.* $^{16}$ have investigated the output power of TE devices without metal electrodes for p-n connection. The authors showed that

their bulk device with a $p$-$n$ junction without metal contact could reach twice the efficiency of the conventional TEG (with traditional ohmic contacts). This result is strong enough to motivate the implementation of $p$-$n$ junctions in $\mu$-TEGs.

In this sense, herein, we propose a flexible thin-film TEG architecture in which the p- and $n$-type TE materials are bonded together on $25\ \mu\text{m}$ thick – Kapton® substrate, as represented in Figure 1. The electrical contacts are made exclusively on the terminals of the device at the cold side of the device. For comparison, the performance of a conventional TEG with metal contacts was evaluated. Furthermore, the two devices were investigated by numerical simulations using the COMSOL Multiphysics® software. The structural, morphological, and thermoelectrical properties of $n$-type $\text{Bi}_2\text{Te}_3$ and $p$-type $\text{Sb}_2\text{Te}_3$ films were evaluated and correlated with the output performance of the TEG. The developed flexible $p$-$n$ device exhibits promising open-circuit voltage and output power. The $p$-$n$ junctions characteristics are highlighted in the present work, and the electrical transport mechanism is also discussed.

![](./images/812730097223073794_2.jpg)

Figure 1. Schematic illustration of the $p$-$n$ junction architecture used for the planar-TEG fabrication in Kapton® substrate.

## 2. Experimental

### 2.1. Flexible co-evaporated $Bi_2Te_3$ and $Sb_2Te_3$ films

Bismuth (Bi) or antimony (Sb) (99.999% purity) and telluride (Te) (99.999% purity) pellets were evaporated from independent tantalum boats, to achieve $n$-type $Bi_2Te_3$ and $p$-type $Sb_2Te_3$ alloy thin-films, respectively. The $25\ \mu\text{m}$ - thick Kapton® substrates (cleaned with isopropanol and dried by $\text{N}_2$ flow before deposition) were placed on a resistive heater located in the vacuum chamber, and used as substrates for the films and device fabrication. The Kapton® polyimide film was selected as substrate for being flexible, robust, and having low thermal conductivity. Among their advantage for integration with most type of flexible electronic device, Kapton® offers high upper working temperature (> 573 K), low thermal conductivity ($0.12\ \text{W}\ \text{m}^{-1}\ \text{K}^{-1}$) and a thermal expansion coefficient value of $12\times10^6\ \text{K}^{-1}$ which closely matches the thermal expansion coefficient of the films $^{17}$, thus reducing residual stress and improving thin-films adhesion. Two crystal oscillators with thickness monitors were used to monitor the deposition rate of Bi/Sb and Te. The growth rates of Bi/Sb and Te were 2 and $6\ \mathring{\text{A}}/\text{s}$, respectively. Each deposition rate was maintained at a fixed value by adjusting the electrical current supplied to the evaporation boat. The film growth was carried out under a vacuum level of $10^{-6}\ \text{mbar}$ at a substrate temperature of 543 K (for the $n$-type film) and 473 K (for the $p$-type film), respectively. These films did not require any post-deposition thermal treatment. $Bi_2Te_3$ and $Sb_2Te_3$ films have ~ 400 nm of thickness measured using a profilometer (Veeco Dektak 150).

### 2.2. Flexible $\mu$-TEG

Using a laser-cut patterned stainless steel mask, 400 nm – thick $Bi_2Te_3$ legs of 8 mm length and 1 mm width were deposited by co-evaporation technique, at a substrate temperature of 543 K, on $25\ \mu\text{m}$ - thick Kapton® polyimide substrate. Then, after removing the first shadow mask, the second mask was applied for the co-evaporation of 400 nm-thick $Sb_2Te_3$ legs with the same dimensions, but at a substrate temperature of 473 K. The masks were designed to have an optimized overlapping of the $p$-

$n$ legs. Finally, 500 nm-thick aluminum (Al) contacts were deposited at room temperature (298 K) by evaporation via shadow mask on the terminals of TEG legs (with 3 mm (length) x 4 mm (width)). The fabricated device consists of 15 pairs of $n$-type and $p$-type legs. All the TEG fabrication steps are shown in the Results and Discussion section. For comparison, a similar TEG with metal contacts for p-n junctions was also fabricated.

### 2.3. TE films and TEG Characterization

A 12.5 $\mu$m radius stylus profilometer (Veeco Dektak 150) was used for the film thickness measurements. In-plane electrical conductivity ($\sigma$) was measured at different temperatures (298 K to 323 K) using the van der Pauw Method. The presented values are the average of the three measurements taken in different points of the films. The carrier mobility and carrier concentration of the TE films were measured using a homemade setup based on van der Pauw configurations. The Hall effect measurements were performed at room-temperature (298 K) and under a magnetic field of 80 mT applied perpendicular to the film plane. Current was introduced between the two probes and the Hall voltage is generated between the other two probes. The Seebeck coefficient ($S$) was measured at 298 K, using a custom-built setup based on the "two-probe" method$^{18}$. This method consists in connecting one side of the film to a heated metal block at a fixed temperature (the block is heated by the application of successive voltage values, between 1 to 3V) using an DC programmable source (Yokogawa model 7651) and the other side to a heat sink at room temperature, to generate a small $\Delta$T along the film. The temperature difference was measured using platinum wire resistors, Pt-100 (100 $\Omega$ at 0 °C precision resistor) employed in the two metal blocks. The resulting thermovoltage ($\Delta$V) was measured by an Agilent 34410A 61/2 Digit Multimeter. A linear plot of $\Delta V$ vs. $\Delta T$ is expected, according to **Equation 1**, which is representative of a good thermal contact between the film and the blocks. Measurements were repeated 4-5 times for each film, and the results are reproducible.

$$
S = \Delta V/\Delta T \tag{1}
$$

The power factor ($PF$), which determines the performance of the TE film, correlates de Seebeck coefficient and the electrical conductivity of the films by the equation 2,

$$
PF = S^2. \sigma \tag{2}
$$

For TEG performance tests, a custom- built testing equipment was developed to create different $\Delta Ts$ in the device. The TEG was placed between six thermoelectric modules, TEC1 – 12706 model, three on the hot side and other three on the cold side of the device. Two aluminum heatsinks were connected to each group of modules to dissipate the generated heat and keep the temperature near room temperature. A thermal grease was applied to ensure good thermal contact between the thermoelectric modules and heatsinks. $\Delta T_{TEG}$ is created through the device by adjusting the output power of the DC power supply (Keysight model E36313A). One pair of $K$-type thermocouples were attached to the hot side and the cold side of the TEG, respectively, to measure the corresponding temperatures ($T_{hot}$ and $T_{cold}$) and therefore, obtain $\Delta T_{TEG}$ ($\Delta T_{TEG} = T_{hot} - T_{cold}$).

To characterize the behavior of the TEG, the open-circuit voltage ($V_0$) was measured at the output of the device as a function of the temperature gradient, $\Delta T_{TEG}$. $V_0$ is given by,

$$
V_0 = N\ S_{total}.\ \Delta T_{TEG} \tag{3}
$$

where $N$ is the number of thermocouples and $S_{total}$ is the sum of the Seebeck coefficients of the $p$ and $n$ materials ($S_{total} = S_p - S_n$, were $S_p > 0$ and $S_n < 0$).

After adjusting the temperature gradient, the output voltage ($V_{out}$) and the respective current ($I_{out}$) were measured. Measurement pairs of the voltage and current ($V_{out}; I_{out}$) were acquired while a series

of load resistances ($R_{load}$) were connected in the output terminals of the device. All voltages and currents were measured using an Agilent multimeter model 34410A with $6^{1/2}$ digits. The maximum voltage error is 3 μV, 6 μV and 40 μV for voltages smaller than 100 mV, 1 V and 10 V, respectively; while the maximum current error is 40 μA, 60 μA and 0.6 mA, for currents smaller than 100 mA, 1 A and 3 A, under voltages smaller than 0.3 V, 0.8 V and 2 V, respectively. These errors were calculated from the operation manual of the Agilent manufacturer $^{19}$. Considering the $V_{out}$ and $I_{out}$ obtained for several values for the $R_{load}$, it was possible to evaluate the output power, $P_{out}$, of the device, as given by $^{20}$,

$$
P_{out}=I_{out}\cdot V_{out}=V_{0}^{2}\cdot\frac{R_{load}}{\left(R_{load}+R_{int}\right)^{2}} \tag{4}
$$

where the $R_{int}$ is the TEG electrical resistance. The maximum output power $P_{máx}$ value is achieved under matched load condition ($R_{load}=R_{int}$), in which the load electrical resistance is equal to the internal resistance of the TEG:

$$
P_{máx}=V_{0}^{2}/4R_{int} \tag{5}
$$

The current–voltage (I - V) characteristics of the TEG were measured using a programmable electrometer (Keithley model 617).

## 3. Results and Discussion

### 3.1. Structure, morphology and TE properties of $Bi_2Te_3$ and $Sb_2Te_3$ films

In present work, the Seebeck voltage response of TE thin- films fabricated at 543 K for the $Bi_2Te_3$ and 473 K for the $Sb_2Te_3$ films, respectively, is shown in **Figure 2**, at room-temperature (298 K). An $S$ value of $-220 \pm 2.17\ \mu\text{V K}^{-1}$ for $Bi_2Te_3$ alloy was measured. This value is similar to the one reported for bulk $Bi_2Te_3$ $^{21}$, and is one of the highest $S$ values found in literature, namely when compared with reference works such as those by D. Kong *et al.* $^{22}$ ($-177\ \mu\text{V K}^{-1}$), P. Nuthongkum *et al.* $^{23}$ (- 35 to -119 $\mu\text{V K}^{-1}$), K. Singkaselit *et al.* $^{24}$ (-34 and -71 $\mu\text{V K}^{-1}$), and Z Cao *et al.*$^{25}$ (-135 and -138 $\mu\text{V K}^{-1}$). On the other side, the $Sb_2Te_3$ alloy exhibit a positive $S$ value ($p$-type) of $+167 \pm 2.38\ \mu\text{V K}^{-1}$, which is higher than the value reported by S. Shen *et al.* $^{26}$ for polyimide substrates ($+135\ \mu\text{V K}^{-1}$). Using the four-probe technique, we measured the electrical conductivity ($\sigma$) of both TE films. $\sigma$ values of $5.60 \times 10^4 \pm 5.90\ (\Omega\text{ m})^{-1}$ and $2.72 \times 10^4 \pm 3.70\ (\Omega\text{ m})^{-1}$, were obtained for $n$-type and $p$-type films, resulting in an outstanding power factors of $2.71 \times 10^{-3} \pm 0.05\ \text{W m}^{-1}\text{ K}^{-2}$ and $0.76 \times 10^{-3} \pm 0.02\ \text{W m}^{-1}\text{ K}^{-2}$ for $Bi_2Te_3$ and $Sb_2Te_3$ films, respectively. The high electrical conductivity observed in the n-type film is due to its relatively high carrier concentration ($7.4 \times 10^{19}\ \text{cm}^{-3}$) and mediate mobility ($47\ \text{cm}^2\text{ V}^{-1}\text{ s}^{-1}$). In turn, the carrier mobility of the p-type film is $118\ \text{cm}^2\text{ V}^{-1}\text{ s}^{-1}$ with a concentration of $1.4 \times 10^{19}\ \text{cm}^{-3}$, respectively. The carrier concentration required for optimal TE performance usually locates between $10^{19}$–$10^{21}\ \text{cm}^{-3}$$^{27}$.

![](./images/812730097223073794_3.jpg)

Figure 2. Seebeck voltage measured as a function of the temperature gradient for $Bi_2Te_3$ and $Sb_2Te_3$ films.

Resistivity values of both materials, in the temperature range between 298 K and 323 K are also shown in **Figure 3**. The $Sb_2Te_3$ and $Bi_2Te_3$ films show a semiconductor behavior until 323 K, due to the decrease in resistivity value with the increase of temperature.

![](./images/812730097223073794_4.jpg)

Figure 3. Resistivity values of the $Sb_2Te_3$ and $Bi_2Te_3$ films measured as a function of the applied temperature.

Previously to TEG characterization, we first investigated the chemical ratio and microstructural properties of the n- and $p$-type TE films. The crystal structure and morphology of both films are similar to the films reported by our previous work $^{28}$. In overall, scanning electron microscopy and energy – dispersive electron X-ray spectroscopy (SEM/EDS) revealed that both films have a grain morphology, with large flakes (100 to 200 nm of size), and have a near – stoichiometric atomic percentages of the Te element (~60 %). Furthermore, X-ray diffraction (XRD) peaks are indexed to the XRD patterns of $Bi_2Te_3$ and $Sb_2Te_3$ hexagonal structures, JCPDS files 15-0863 and 15-0874, respectively. Average grain sizes of 33 nm are found for n- and p-type films. The specific SEM/EDS and XRD figures, as well as the detailed structural and morphological characterization of the n-type and p-type films can be found in our previous work $^{28}$.

Our high $PF$ values (at room temperature) could be associated with the structure of the films. Several works reported an increase in the $\sigma$ with the increase of the crystal size $^{26}$. For instance, A. Bollero *et al.* $^{29}$ observed a decrease by a factor of 10 in electrical resistivity value with the small increase of the mean grain size of 55 nm. In the same way, S. Morikawa *et al.*$^{30}$, reported an increase in the electrical conductivity value by a factor of 32 when the crystallite' size increase from 5.8 nm to 19.6 nm. As grain increases in size, the total boundary area decreases, and therefore, the carrier's mobility and $\sigma$ also increase, because $\sigma$ depends linearly on the carrier's mobility $^{23}$. Furthermore, with the increase of $\sigma$, the $PF$ also increase. In conclusion, our $PF$ values are comparable to or even greater than those obtained in the literature for films with $>1\ \mu$m of thickness $^{23–25,31,32}$.

### 3.2. Performance of $\mu$-TEG

A TEG is a solid-state device that converts temperature differences directly into electrical energy, through the Seebeck effect. P- and $n$-type TE materials are typically arranged in series electrically, and thermally in parallel.

As shown in **Figure 4** (left side), by using patterned metal masks, we deposited firstly the $Bi_2Te_3$ thin-film legs on 25 $\mu$m - thick Kapton® substrate, and then the $Sb_2Te_3$ thin - film legs. Finally, 500 nm-thick Al contacts were deposited by thermal evaporation at the ends of the TEG for the electrical tests. A thin, light, and flexible $p$-$n$ TEG was developed, as visible in **Figure 4** (right side). The optical image shows the well-defined $n$ and $p$ legs separated by a gap of around 0.5 mm.

![](./images/812730097223073794_5.jpg)

**Figure 4.** (Left) Schematic describing of the fabrication process of the $p$-$n$ TEG, and (right) photographs of the developed flexible thin-film TEG, showing the thermocouple legs. Optical image of thermocouples shows the dimensions of the legs and their separation.

The TEG composed of 15 $p$-$n$ pairs made by $Bi_2Te_3$-$Sb_2Te_3$ materials with 53 mm in length was characterized using a custom-built setup which can accurately control the temperature gradients by 6 commercial thermoelectric modules. As shown in **Figure 5**, our $p$-$n$ flexible device with 15 pairs generated a maximum output voltage of 210 mV at a temperature difference of 35 K. A similar maximum output voltage $(\approx211$ mV) is obtained by the conventional $p$-$metal$-$n$ TEG device. In both devices, the open circuit voltage is linear with the temperature gradient. An Optris PI 450 infrared (IR) camera placed at 4 cm from the setup was used to acquire thermal images of the TEGs. The inset of **Figure 5** shows the $p$-$n$ TEG tests. The $p$-$n$ TEG and $p$-$metal$-$n$ TEG sensitivities taken from each slope of the graph of **Figure 5** was found to be 5.97 mV K⁻¹ and 5.80 mV K⁻¹, respectively, which are

close to the values calculated from the Seebeck coefficients of the $Bi_2Te_3$ and $Sb_2Te_3$ films (5.81 mV K⁻¹), for the same number N of legs. The achieved $S_{par}$ value for each thermocouple for the $p$-$n$ TEG was 398 μV K⁻¹ which when comparing with the literature is much larger than the $S_{par}=108$ μV K⁻¹ for the flexible TE generator with 100 pairs of co-sputtered $Bi_2Te_3$-$Sb_2Te_3$ legs (with 500 nm-thick) developed by L. Francioso et al. $^{33}$ and the 13 pairs of 800 nm - TE legs performed by D. Kong et al.²² ($S_{par}=155$ μV K⁻¹).

![](./images/812730097223073794_6.jpg)

Figure 5. Open circuit voltage ($V_0$) of the 15 TE pairs, with and without metal contacts, as a function of the temperature gradient. Inset shows the photograph of the $p$-$n$ TEG in the measurement system.

To evaluate the power generation performance of our flexible device, we measured the $V_{out}/I_{out}$ (output voltage/output current) characteristic of the $p$-$n$ TEGs. Figure 6 (a) shows the output voltage $V_{out}$ (mV) and output power $P_{out}$ (nW) versus the output current $I_{out}$ (μA) for temperature gradients of 11 K, 17 K, 22 K and 35 K. By fitting the experimental data of $\Delta T=35$ K to equation 5 the maximum power output ($P_{max}$), and the current ($I_{out}$) and voltage ($V_{out}$) that maximizes the output

power of the TEG are 693 nW, 6.5 μA and 106 mV, respectively. However, the *p-metal-n* TEG reveals a slightly lower maximum power output (662 nW), as shown in **Figure 6 (b)**. Furthermore, a maximum output power per unit area of 3.3 mW cm⁻² can be achieved by our *p-n* device, for a $\Delta T = 35$ K. **Figure 6 (c, d)** shows the average surface temperature gradient from the cooled to the heated ends of each device at the area marked by the white square, during the TE performance test, at temperature gradient of 35 K. The surface temperatures were also measured with wire thermocouples for temperature calibration. An error below 1% was observed between the acquired temperatures from thermocouples and the thermal camera.

The internal resistance ($R_{int}$) of the *p-n* flexible device obtained from the fitting procedure was around $1.6 \times 10\ ^4 \Omega$. This value is close to the total resistance of the 15 pairs of BiTe - SbTe, calculated from the electrical properties of each material ($\sim 1.6 \times 10^4 \Omega$), which translates to a contact resistance ($\text{R}_{\text{cont}}$) of each *p-n* junction of our device in the order of $10^{-9} \Omega \text{ m}^2$. As for TE applications, $\text{R}_{\text{cont}}$ must be typically between $10^{-10}$ to $10^{-5} \Omega \text{ cm}^2$ $^{14,15}$ and therefore, our device with a direct *p-n* junction is acceptable for thermoelectric applications.

![](./images/812730097223073794_7.jpg)

**Figure 6.** (a,b) Current–voltage– power curves of the TEGs, with and without metal contacts for *p-n* junctions, and at various values of the temperature gradient. The lines are the corresponding fits of the data; (c,d) Typical thermal images of the TEGs captured using an infrared (IR) camera during the measurements at temperature gradient of 35 K.

In addition, to further verify the behavior of the developed *p-n* TEG, numerical simulations were performed using the COMSOL 5.2 multiphysics software and using the main parameters shown in **Table 1**. The heat conduction model was used for the numerical simulations. The simulated current-voltage-power curves of the *p-n* TEG as a function of the applied temperature gradient is shown in **Figure 7 (a)**. It is clearly visible that the power output values obtained for the fabricated device (**Figure 6**) are in close agreement with the simulated values (**Figure 7 (a)**). Furthermore, the performance of the conventional TEG structure with metal contacts for *p-n* junction was also predicted (**Figure 7 (b)**). For a better comparison of the device output performance, the output power values of each device for the different temperature gradients are shown in **Table 2**. Furthermore, the deviation obtained for the output power generated by the *p-n* TEG and the simulated one is also given in **Table 2**. It is possible

to confirm a good agreement between our $p$-$n$ TEG experimental and the theoretical works (error below 5%). Moreover, the output results evidences that the $p$-$n$ TEG slightly outperforming the conventional $p$-$metal$-$n$ TEG. Therefore, the use of p-n TEG can overcome the problem of the degradation of metal contacts on the hot side when it is applied on very hot surfaces. In this sense, we successfully fabricated a thermoelectric device without metal contacts for the p-n junction.

The schematic configurations of both simulated devices when a temperature gradient of 35 K is applied are shown in the insets of **Figure 7 (a)** and **(b)**.

Table 1. Numerical simulations parameters of the studied thermoelectric devices.

<table>
  <tr>
    <th>METHOD</th>
    <td>Finite Element Method (FEM)</td>
  </tr>
  <tr>
    <th>EQUATIONS SOLVED</th>
    <td>
$$-\nabla\left(\left(\sigma S^{2} T+k\right) \nabla T\right)-\nabla(\sigma S T \nabla V)=\sigma\left((\nabla V)^{2}+S \nabla T \nabla V\right)$$
$$\nabla(\sigma \nabla V)+\nabla(\sigma S \nabla T)=0$$
where $T$, $V$, $S$, $k$ and $\sigma$ are the absolute temperature, the electrical potential, the Seebeck coefficient, the thermal conductivity and the electrical conductivity, respectively.
    </td>
  </tr>
  <tr>
    <th>STUDY</th>
    <td>Steady State</td>
  </tr>
  <tr>
    <th>COMPUTATIONAL MESH</th>
    <td>3D mesh with triangular, hexahedral, quadrilateral and prism elements (free triangular and swept from COMSOL)</td>
  </tr>
  <tr>
    <th>REFINEMENT OF THE COMPUTATIONAL MESH</th>
    <td>Extremely fine (with 0.69 mm as maximum element size and 10.7 µm as minimum element size)</td>
  </tr>
  <tr>
    <th>CONVERGENCE CRITERIA</th>
    <td>Stationary iterative solver MUMPS with a relative tolerance of $1 × 10^{-7}$</td>
  </tr>
  <tr>
    <th>MATERIAL PROPERTIES</th>
    <td>Aluminum used for the metal contacts and pads have a thermal conductivity and electrical conductivity of 238 W/(m·K) and 3.77×$10^{-7}$ S/m, respectively. Bismuth Telluride and Antimony Telluride have a thermal conductivity of 2 W/(m·K) ³⁴ and 1.65 W/(m·K) ³⁵, respectively. All other material properties are provided by experimentally measured data in this paper.</td>
  </tr>
  <tr>
    <th>BOUNDARY CONDITIONS</th>
    <td>All outer surfaces are thermally and electrically isolated. One of the silver pad was grounded ($V = 0$ V). One of the sides of the device was at a constant temperature of 30 °C and the other side was at a temperature within the range [11, 17, 22, 35] °C, to create the temperature differences, which was constant in each simulation but varied in order to study different applied temperatures. Contact resistance was applied at the contact area between the $p$-$n$ junctions for the simulated TEG without metal contacts and between the p-metal and metal-n junctions for the simulated TEG with metal contacts. According to the experimentally measured data, the estimated contact resistance between each $p$-$n$ junction was 9.4 ×$10^{8}$ Ω·m². Dividing this value with the area of contact between the p and n legs of the device (1 mm²), a resistance of 0.0094 Ω per junction was obtained. By multiplying this resistance with the $p$-$n$ junction contact area of the simulated geometry (4 ×$10^{-4}$ mm²), equivalent contact resistance of 3.75 ×$10^{-11}$ Ω·m² was obtained. For the junction between the aluminum and p/n material, a previous work ³⁶ estimated the contact resistance between both materials, fabricated by the co-evaporation method, to be 1 ×$10^{-5}$ Ω·m². Furthermore, the contact area between the aluminum and the p and n legs in the referred work was 1 mm², which yields a resistance of 10 Ω per junction. The product of this resistance with the junctions contact area of the simulated geometry (4×$10^{-4}$ mm²) resulted in a contact resistance of 4×$10^{-9}$ Ω·m².</td>
  </tr>
  <tr>
    <th>OUTPUT RESULTS</th>
    <td>Open circuit voltage between the first and last leg of the device. The power output is calculated from eq.(4). The internal resistance of the TEG without metal contacts (16368 Ω) is provided by experimentally measured data in this paper. The internal resistance of the TEG with metal contacts (16965 Ω) was obtained using the total resistance of the pairs of BiTe - SbTe, calculated from the electrical properties of each material with the addition of the contact resistance at each p-metal and metal-n junction, obtained from a previous work ³⁶. The maximum power output was calculated from eq.(5).</td>
  </tr>
</table>

![](./images/812730097223073794_8.jpg)

Figure 7. (a) Simulated current–voltage–power curves of the (a) $p$-$n$ TEG and (b) $p$-metal-$n$ TEG devices at different temperature gradient values. The lines are the corresponding fits of the data. Insets: Schematic configuration of the simulated devices at a specific temperature gradient of 35 K.

**Table 2.** The maximum power output value of $p$-n TEG $_{\text{experimental}}$, $p$-n TEG $_{\text{simulated}}$, $p$-$metal$-$n$ TEG$_{\text{experimental}}$ and $p$-$metal$-$n$ TEG$_{\text{simulated}}$ for the differently applied temperature differences.

<table>
<thead>
<tr>
<th>ΔT
(K)</th>
<th>P<sub>output</sub>
$p$-n TEG
experimental
(nW)</th>
<th>P<sub>output</sub>
$p$-n TEG
simulated
(nW)</th>
<th>Error
(%)</th>
<th>P<sub>output</sub>
$p$-$metal$-$n$ TEG
experimental (nW)</th>
<th>P<sub>output</sub>
$p$-$metal$-$n$ TEG
simulated
(nW)</th>
</tr>
</thead>
<tbody>
<tr>
<td>11</td>
<td>77.56</td>
<td>77.45</td>
<td>0.14</td>
<td>73.66</td>
<td>64.54</td>
</tr>
<tr>
<td>17</td>
<td>187.70</td>
<td>189.10</td>
<td>0.74</td>
<td>169.77</td>
<td>174.21</td>
</tr>
<tr>
<td>22</td>
<td>358.65</td>
<td>349.78</td>
<td>2.54</td>
<td>280.22</td>
<td>337.20</td>
</tr>
<tr>
<td>35</td>
<td>693.12</td>
<td>668.38</td>
<td>3.70</td>
<td>662.38</td>
<td>666.81</td>
</tr>
</tbody>
</table>

To confirm the quality of the $p$-$n$ junctions, the current density-voltage ($J$–$V$) characteristics of 29 $p$-$n$ junctions of the TEG, under dark conditions and at room temperature, are depicted in **Figure 8** (a). We investigated only the 29 $p$-$n$ junctions (instead of 30) to have an odd number of junctions, and so that the diode effect is not cancelled $^{37}$. The $J$-$V$ curves exhibit an asymmetric nature, confirming the formation of $p$-$n$ junctions at the interfaces, with an impressive rectifying ratio ($J_{+1\text{V}}/J_{-1\text{V}}$) of $\approx2\text{x}10^4$. Moreover, a turn-on voltage ($V_{\text{on}}$) of $\approx0.3$ V is obtained. The forward $J$-$V$ characteristic of a heterojunction can be described by the following **Equation 6** $^{38}$:

$$
J \alpha \exp\left(\frac{qV}{nkT}\right) \tag{6}
$$

where $q$ is the electron charge, $n$ is the ideality factor, $k$ is the Boltzmann constant, and $T$ is the temperature. In $p$-$n$ junctions, the ideality factor can be independently determined from the slope of the exponential regime of dark $J$-$V$ characteristics on a semi-logarithmic plot. **Figure 8** (b) shows the replot of the $J$-$V$ curve in the semi-logarithmic mode for the heterojunctions and the ideality factor was

found to be ≈1.1. Since the ideality factor is close to the unity, the electrical transport of the junctions is dominated by diffusion current, where recombination processes are minor $^{38,39}$. Furthermore, the diode characteristics of the present device are improved when compared with the ones presented by R. Chavez *et al.* $^{16,40}$ and T. D. Desissa *et al.* $^{41}$ in their bulk devices with a $p$-$n$ junction without metal contact. Particularly, R. Chavez *et al.* $^{16}$ reported an inhomogeneous $p$-$n$ junction due to the mixing of the nanoparticle powders prior and during the densification step for the device fabrication. Furthermore, the activation energy (E<sub>activation</sub>) lies outside of the range $\mathrm{E_g/2 \leq E_{activation} \leq E_g}$ indicating that the charge transport across the junction is dominated by recombination limited transport process (due to the high density of intraband states inherent to the fabric process), which is in contrast with the diffusion current mechanism revealed by our I-V curves. In this context it is expectable that our P-N TEG device shows better output power performance than the device reported by them.

Comparing our reported results with the current state-of-art of micro-devices based on telluride alloys, our $p$-$n$ device offers competitive results. **Table 3** compares the thermoelectric properties of our micro-device with the results found in the literature for planar devices based on telluride alloys and using different fabrication techniques. In terms of output performance, our $p$-$n$ TEG device shows higher output power values than the ones revealed by the TE devices with larger number of TE units and for similar TE materials thickness $^{12,33}$, higher TE material thickness $^{42,43}$ and higher temperature gradients than 35 K $^{33,43}$.

The present work highlights the elimination of the annealing steps (to achieve high TE material properties), the rapid and low-cost fabrication of TE device without complex and expensive lithographic method, which is a goal for the development of TE appealing to the market. Moreover, this TEG design can be useful for high–temperature applications, in which the temperature at the hot side could promote the degradation of the metal contacts., and therefore decrease significantly the TEG performance.

![](./images/812730097223073794_9.jpg)

Figure 8. (a) Current density - voltage curve of 29 $n$-Bi₂Te₃ / $p$-Sb₂Te₃ heterojunctions of the fabricated TEG and (b) Replot of the J-V curve of the heterojunction in the forward voltage range using semi-logarithmic mode.

**Table 3.** Comparison of the performance data of p-Sb₂Te₃/n-Bi₂Te₃ device fabricated in present work with those μ-devices published in the literature.

<table>
  <thead>
    <tr>
      <th>Reference,<br>Year</th>
      <th>TE units</th>
      <th>Device<br>dimensions</th>
      <th>ΔT (K)</th>
      <th>Output voltage<br>(mV)</th>
      <th>Output Power</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">This work,<br>2019</td>
      <td>p-type</td>
      <td>53 mm × 0.8</td>
      <td>35</td>
      <td>210 mV</td>
      <td>0.7 μW (3.3 mWcm⁻²)</td>
    </tr>
    <tr>
      <td>Sb₂Te₃;</td>
      <td>mm × 400 nm;</td>
      <td>22</td>
      <td>153 mV</td>
      <td></td>
    </tr>
    <tr>
      <td>n-type</td>
      <td>15 pairs</td>
      <td></td>
      <td></td>
      <td>0.4 μW (2.0 mW cm⁻²)</td>
    </tr>
    <tr>
      <td>Bi₂Te₃</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4">S. Kim <i>et al.</i> ⁴⁴,<br>2014</td>
      <td>p-type</td>
      <td>15 mm × 20</td>
      <td>35</td>
      <td>62 mV</td>
      <td>1.8 mWcm⁻²</td>
    </tr>
    <tr>
      <td>Sb₂Te₃;</td>
      <td>mm × 500 μm;</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>n-type</td>
      <td>8 pairs</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Bi₂Te₃</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4">D. Madan <i>et al.</i> ⁴⁵,<br>2012</td>
      <td>n-type:</td>
      <td>5 mm × 700</td>
      <td>20</td>
      <td>109 mV</td>
      <td>25 μW</td>
    </tr>
    <tr>
      <td>Bi2Te3-</td>
      <td>μm × 120 μm</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>epoxy</td>
      <td>TE legs</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>62 pairs</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="6">L. Jun <i>et al.</i>⁴⁶,<br>2019</td>
      <td>p-type</td>
      <td>50 mm × 0.7</td>
      <td>35</td>
      <td>18 mV</td>
      <td>----</td>
    </tr>
    <tr>
      <td>Bi₀.₄₈Sb₁.₅₂T</td>
      <td>mm × 0.001</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>e₃;</td>
      <td>mm p-TE leg;</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>n-type</td>
      <td>50 mm × 0.7</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Bi₂Se₀.₃Te₂.₇</td>
      <td>mm × 0.0004</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>mm n-TE leg;<br>11 pairs</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4">F. Yang <i>et al.</i>¹²,<br>2017</td>
      <td>p-type</td>
      <td>0.3 mm × 6</td>
      <td>30</td>
      <td>190 mV</td>
      <td>~150 nW</td>
    </tr>
    <tr>
      <td>Sb₂Te₃;</td>
      <td>mm × 400 nm</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>n-type</td>
      <td>TE legs;</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Bi₂Te₃</td>
      <td>20 pairs</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Reference, Year</th>
      <th>TE units</th>
      <th>Device dimensions</th>
      <th>ΔT (K)</th>
      <th>Output voltage (mV)</th>
      <th>Output Power</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>L. Francioso et al.³³, 2011</td>
      <td>p-type Sb₂Te₃; n-type Bi₂Te₃</td>
      <td>70 mm × 30 mm × 500 nm 100 pairs</td>
      <td>40</td>
      <td>430 mV</td>
      <td>32 nW</td>
    </tr>
    <tr>
      <td>Z. Lu et al.⁴², 2016</td>
      <td>p-type Sb₂Te₃; n-type Bi₂Te₃</td>
      <td>40 mm × 80 mm × 300 μm 12 pairs</td>
      <td>35</td>
      <td>10 mV</td>
      <td>15 nW</td>
    </tr>
    <tr>
      <td>J.P. Rojas et al.⁴³, 2017</td>
      <td>p-type Sb₂Te₃; n-type Bi₂Te₃</td>
      <td>40 mm × 10 mm × 2 μm 20 pairs</td>
      <td>75 K</td>
      <td>190.7 mV</td>
      <td>24 nW</td>
    </tr>
  </tbody>
</table>

## 4. Conclusions

In present work, a complete investigation of a $p$-$n$ flexible $\mu$-TEG device concept, from the active materials (morphology, structure, electrical, and thermoelectric analysis) up to the TEG device was performed. A prototype of a flexible thermoelectric generator with 15 pairs of $Bi_2Te_3/Sb_2Te_3$ legs and without metal contacts at $p$-$n$ junctions was designed and fabricated using a low-cost and straightforward shadow-mask procedure. Our results are in good agreement with the theoretical predictions for the TEG device without metal contacts. The flexible TEG achieved an output voltage of 210 mV and a maximum output power (power density) of $0.7\ \mu\text{W}$ ($3.3\ \text{mW}\ \text{cm}^{-2}$) for a temperature difference of 35 K. Moreover, the device exhibits diode characteristics with a remarkable rectifying ratio and with a turn-on voltage of $\approx0.3$ V. Our TEG design could be of great interest for real

applications which involve hot surfaces (e.g., industrial processes), due to the elimination of metal contacts for the $p$-$n$ junction at the hot-side of the device. Furthermore, considering the output performance, its application in physiological wireless sensors is envisaged since the power requirements are of the same order of magnitude (nW to mW).

## Acknowledgements

The present work is supported by Portuguese Foundation for Science and Technology (FCT) in the framework of the (1) reference project UID/EEA/04436/2019, by FEDER funds through the COMPETE 2020 – Programa Operacional Competitividade e Internacionalização (POCI); (2) Strategic Funding Contract UID/FIS/04650/2019; (3) project PTDC/CTM – NAN/5414/2014 (POCI-01-0145-FEDER-016723); (4) co-financed by Programa Operacional Regional do Norte (NORTE2020), through Fundo Europeu de Desenvolvimento Regional (FEDER), Project NORTE-01-0145-FEDER-000032 – NextSea and (5) project PTDC/EEI-TEL/5250/2014, by FEDER funds through POCI-01-145-FEDER-16695.

## Conflict of Interest

The authors declare no conflict of interest.

---

## REFERENCES

(1) Zhang, D.; Wang, Y.; Yang, Y. Design, Performance, and Application of Thermoelectric Nanogenerators. *Small* **2019**, 1805241.

(2) Raj, A.; Steingart, D. Review—Power Sources for the Internet of Things. *J. Electrochem. Soc.* **2018**, *165* (8), B3130–B3136.

(3) Stachowiak, H.; Lassue, S.; Dubernard, A.; Gaviot, E. A thermoelectric sensor for fluid flow measurement. principles, calibration and solution for self temperature compensation. *Flow Meas. Instrum.* **1998**, *9* (3), 135–141.

(4) Willars-Rodríguez, F. J.; Chávez-Urbiola, E. A.; Vorobiev, P.; Vorobiev, Y. V. Investigation of solar hybrid system with concentrating Fresnel lens, photovoltaic and thermoelectric generators. *Int. J. Energy Res.* **2017**, *41* (3), 377–388.

(5) Demir, M. E.; Dincer, I. Performance assessment of a thermoelectric generator applied to exhaust waste heat recovery. *Appl. Therm. Eng.* **2017**, *120*, 694–707.

(6) Meng, F.; Chen, L.; Feng, Y.; Xiong, B. Thermoelectric generator for industrial gas phase waste heat recovery. *Energy* **2017**, *135*, 83–90.

(7) Quan, R.; Liu, G.; Wang, C.; Zhou, W.; Huang, L.; Deng, Y. Performance Investigation of an Exhaust Thermoelectric Generator for Military SUV Application. *Coatings* **2018**, *8* (1), 45.

(8) Kopparthy, V. L.; Tangutooru, S. M.; Nestorova, G. G.; Guilbeau, E. J. Thermoelectric

microfluidic sensor for bio-chemical applications. *Sensors Actuators B Chem.* **2012**, *166–167*, 608–615.

(9) Siddique, A. R. M.; Mahmud, S.; Heyst, B. Van. A review of the state of the science on wearable thermoelectric power generators (TEGs) and their existing challenges. *Renew. Sustain. Energy Rev.* **2017**, *73*, 730–744.

(10) Carmo, J. P.; Goncalves, L. M.; Correia, J. H. Thermoelectric Microconverter for Energy Harvesting Systems. *IEEE Trans. Ind. Electron.* **2010**, *57* (3), 861–867.

(11) Nguyen Huu, T.; Nguyen Van, T.; Takahito, O. Flexible thermoelectric power generator with Y-type structure using electrochemical deposition process. *Appl. Energy* **2018**, *210*, 467–476.

(12) Yang, F.; Zheng, S.; Wang, H.; Chu, W.; Dong, Y. A thin film thermoelectric device fabricated by a self-aligned shadow mask method. *J. Micromechanics Microengineering* **2017**, *27* (5), 055005.

(13) Jung, Y. S.; Jeong, D. H.; Kang, S. B.; Kim, F.; Jeong, M. H.; Lee, K.-S.; Son, J. S.; Baik, J. M.; Kim, J.-S.; Choi, K. J. Wearable solar thermoelectric generator driven by unprecedentedly high temperature difference. *Nano Energy* **2017**, *40*, 663–672.

(14) Bjørk, R. The Universal Influence of Contact Resistance on the Efficiency of a Thermoelectric Generator. *J. Electron. Mater.* **2015**, *44* (8), 2869–2876.

(15) McCarty, R. Thermoelectric Power Generator Design for Maximum Power: It’s All About ZT. *J. Electron. Mater.* **2013**, *42* (7), 1504–1508.

(16) Chavez, R.; Angst, S.; Hall, J.; Maculewicz, F.; Stoetzel, J.; Wiggers, H.; Thanh Hung, L.; Van Nong, N.; Pryds, N.; Span, G.; ىز. Efficient p-n junction-based thermoelectric generator that can operate at extreme temperature conditions. *J. Phys. D. Appl. Phys.* **2018**, *51* (1), 014005.

(17) Touloukian, Y. S.; Kirby, R. K.; Taylor, R. E. and Desai, P. D. *Thermal Expansion: Metallic Elements and Alloys (Thermophysical Properties of Matter)*, 1st. Ed.; Springer Science + Business Media, LLC: New York, 1975.

(18) Valalaki, K.; Benech, P.; Galiouna Nassiopoulou, A. High Seebeck Coefficient of Porous Silicon: Study of the Porosity Dependence. *Nanoscale Res. Lett.* **2016**, *11* (1), 201.

(19) Agilent Technologies, 34410A digital multimeter 6½ digit high performance.
<http://www.agilent.com/>.

(20) M. H. Cobble, "Calculations of Generator Performance", *Handbook of Thermoelectrics*, CRC Press, (1995).

(21) Park, M. S.; Song, J.-H.; Medvedeva, J. E.; Kim, M.; Kim, I. G.; Freeman, A. J. Electronic structure and volume effect on thermoelectric transport in p -type Bi and Sb tellurides. *Phys. Rev. B* **2010**, *81* (15), 155211.

(22) Kong, D.; Zhu, W.; Guo, Z.; Deng, Y. High-performance flexible Bi2Te3 films based wearable thermoelectric generator for energy harvesting. *Energy* **2019**, *175*, 292–299.

(23) Nuthongkum, P.; Sakdanuphab, R.; Horprathum, M.; Sakulkalavek, A. [Bi]:[Te] Control, Structural and Thermoelectric Properties of Flexible Bi x Te y Thin Films Prepared by RF Magnetron Sputtering at Different Sputtering Pressures. *J. Electron. Mater.* **2017**, *46* (11), 6444–6450.

(24) Singkaselit, K.; Sakulkalavek, A.; Sakdanuphab, R. Effects of annealing temperature on the structural, mechanical and electrical properties of flexible bismuth telluride thin films prepared by high-pressure RF magnetron sputtering. *Adv. Nat. Sci. Nanosci. Nanotechnol.* **2017**, *8* (3), 035002.

(25) Cao, Z.; Tudor, M. J.; Torah, R. N.; Beeby, S. P. Screen Printable Flexible BiTe–SbTe-Based

Composite Thermoelectric Materials on Textiles for Wearable Applications. *IEEE Trans. Electron Devices* **2016**, *63* (10), 4024–4030.

(26) Shen, S.; Zhu, W.; Deng, Y.; Zhao, H.; Peng, Y.; Wang, C. Enhancing thermoelectric properties of Sb 2 Te 3 flexible thin film through microstructure control and crystal preferential orientation engineering. *Appl. Surf. Sci.* **2017**, *414*, 197–204.

(27) Li, J.; Chen, Z.; Zhang, X.; Yu, H.; Wu, Z.; Xie, H.; Chen, Y.; Pei, Y. Simultaneous Optimization of Carrier Concentration and Alloy Scattering for Ultrahigh Performance GeTe Thermoelectrics. *Adv. Sci.* **2017**, *4* (12), 1700341.

(28) Vieira, E. M. F.; Figueira, J.; Pires, A. L.; Grilo, J.; Silva, M. F.; Pereira, A. M.; Goncalves, L. M. Enhanced thermoelectric properties of Sb2Te3 and Bi2Te3 films for flexible thermal sensors. *J. Alloys Compd.* **2019**, *774*, 1102–1116.

(29) Bollero, A.; Andrés, M.; García, C.; Abajo, J. de; Gutiérrez, M. T. Morphological, electrical and optical properties of sputtered Mo thin films on flexible substrates. *Phys. status solidi* **2009**, *206* (3), 540–546.

(30) Morikawa, S.; Inamoto, T.; Takashiri, M. Thermoelectric properties of nanocrystalline Sb 2 Te 3 thin films: experimental evaluation and first-principles calculation, addressing effect of crystal grain size. *Nanotechnology* **2018**, *29* (7), 075701.

(31) Joo, S.-J.; Kim, B. S.; Min, B.-K.; Oh, M. W.; Lee, J.-E.; Ryu, B. K.; Lee, H. W.; Park, S. D. Deposition of n-Type Bi2Te3 Thin Films on Polyimide by Using RF Magnetron Co-Sputtering Method. *J. Nanosci. Nanotechnol.* **2015**, *15* (10), 8299–8304.

(32) Kim, J.-H.; Choi, J.-Y.; Bae, J.-M.; Kim, M.-Y.; Oh, T.-S. Thermoelectric Characteristics of n-Type Bi2Te3 and p-Type Sb2Te3 Thin Films Prepared by Co-Evaporation and Annealing for Thermopile Sensor Applications. *Mater. Trans.* **2013**, *54* (4), 618–625.

(33) Francioso, L.; De Pascali, C.; Farella, I.; Martucci, C.; Creti, P.; Siciliano, P.; Perrone, A.
Flexible thermoelectric generator for wearable biometric sensors. في 2010 IEEE Sensors;
IEEE, 2010; 747-750.

(34) Jeon, H.-W.; Ha, H.-P.; Hyun, D.-B.; Shim, J.-D. Electrical and thermoelectrical properties of
undoped Bi2Te3-Sb2Te3 and Bi2Te3-Sb2Te3-Sb2Se3 single crystals. J. Phys. Chem. Solids
1991, 52 (4), 579-585.

(35) Yáñez-Limón, J. M.; González-Hernández, J.; Alvarado-Gil, J. J.; Delgadillo, I.; Vargas, H.
Thermal and electrical properties of the Ge:Sb:Te system by photoacoustic and Hall
measurements. Phys. Rev. B 1995, 52 (23), 16321-16324.

(36) L.M.V.Gonçalves. Microssistema termoeléctrico baseado em teluretos de bismuto e
antimónio, 2008.

(37) Q., B.; Lorenz, M.; Zimmermann, G.; Czekalla, C.; Brandt, M.; Von, H.; Grundm, M. P-Type
Phosphorus Doped ZnO Wires for Optoelectronic Applications. في Nanowires; InTech, 2010.

(38) Hao, L.; Liu, Y.; Gao, W.; Han, Z.; Xue, Q.; Zeng, H.; Wu, Z.; Zhu, J.; Zhang, W. Electrical
and photovoltaic characteristics of MoS 2/Si p-n junctions. J. Appl. Phys. 2015, 117 (11),
114502.

(39) Wetzelaer, G. A. H.; Kuik, M.; Lenes, M.; Blom, P. W. M. Origin of the dark-current ideality
factor in polymer:fullerene bulk heterojunction solar cells. Appl. Phys. Lett. 2011, 99 (15),
153506.

(40) Chavez, R.; Angst, S.; Hall, J.; Stoetzel, J.; Kessler, V.; Bitzer, L.; Maculewicz, F.; Benson,
N.; Wiggers, H.; Wolf, D.; واخ. High Temperature Thermoelectric Device Concept Using
Large Area PN Junctions. J. Electron. Mater. 2014, 43 (6), 2376-2383.

(41) Desissa, T. D.; Schrade, M.; Norby, T. Electrical Properties of a p-n Heterojunction of Li-

Doped NiO and Al-Doped ZnO for Thermoelectrics. *J. Electron. Mater.* **2018**, *47* (9), 5296–5301.

(42) Lu, Z.; Zhang, H.; Mao, C.; Li, C. M. Silk fabric-based wearable thermoelectric generator for energy harvesting from the human body. *Appl. Energy* **2016**, *164*, 57–63.

(43) Rojas, J. P.; Conchouso, D.; Arevalo, A.; Singh, D.; Foulds, I. G.; Hussain, M. M. Paper-based origami flexible and foldable thermoelectric nanogenerator. *Nano Energy* **2017**, *31*, 296–301.

(44) Kim, S. J.; We, J. H.; Cho, B. J. A wearable thermoelectric generator fabricated on a glass fabric. *Energy Environ. Sci.* **2014**, *7* (6), 1959.

(45) Madan, D.; Wang, Z.; Chen, A.; Juang, R.; Keist, J.; Wright, P. K.; Evans, J. W. Enhanced Performance of Dispenser Printed MA n-type Bi 2 Te 3 Composite Thermoelectric Generators. *ACS Appl. Mater. Interfaces* **2012**, *4* (11), 6117–6124.

(46) Luo, J.; Cao, Z.; Yuan, M.; Chou, X. Preparation and testing of flexible thermoelectric power generator. *Results Phys.* **2019**, *12*, 1304–1310.

![](./images/812730097223073794_10.jpg)

Figure 1. Schematic illustration of the p-n junction architecture used for the planar-TEG fabrication in Kapton® substrate.

![](./images/812730097223073794_11.jpg)

Figure 2. Seebeck voltage measured as a function of the temperature gradient for Bi2Te3 and Sb2Te3 films.

![](./images/812730097223073794_12.jpg)

Figure 3. Resistivity values of the Sb2Te3 and Bi2Te3 films measured as a function of the applied temperature.

![](./images/812730097223073794_13.jpg)

Figure 4. (Left) Schematic describing of the fabrication process of the p-n TEG, and (right) photographs of the developed flexible thin-film TEG, showing the thermocouple legs. Optical image of thermocouples shows the dimensions of the legs and their separation.

![](./images/812730097223073794_14.jpg)

Figure 5. Open circuit voltage (V_0) of the 15 TE pairs, with and without metal contacts, as a function of the temperature gradient. Inset shows the photograph of the p-n TEG in the measurement system.

![](./images/812730097223073794_15.jpg)

Figure 6. (a,b) Current-voltage- power curves of the TEGs, with and without metal contacts for p-n junctions, and at various values of the temperature gradient. The lines are the corresponding fits of the data; (c,d) Typical thermal images of the TEGs captured using an infrared (IR) camera during the measurements at temperature gradient of 35 K.

![](./images/812730097223073794_16.jpg)

Figure 7. (a) Simulated current-voltage-power curves of the (a) p-n TEG and (b) p-metal-n TEG devices at different temperature gradient values. The lines are the corresponding fits of the data. Insets: Schematic configuration of the simulated devices at a specific temperature gradient of 35 K.

183x263mm (96 x 96 DPI)

![](./images/812730097223073794_17.jpg)

Figure 8. (a) Current density - voltage curve of 29 n-Bi2Te3 / p-Sb2Te3 heterojunctions of the fabricated TEG and (b) Replot of the J-V curve of the heterojunction in the forward voltage range using semi-logarithmic mode.

![](./images/812730097223073794_18.jpg)

Graphical abstract