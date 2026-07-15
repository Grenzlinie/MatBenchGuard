# A Simulation Study of Oxygen Vacancy-Induced Variability in $\text{HfO}_2$/Metal Gated SOI FinFET

Amit Ranjan Trivedi, Student Member, IEEE, Takashi Ando, Senior Member, IEEE,
Amith Singhee, Senior Member, IEEE, Pranita Kerber, Emrah Acar, Senior Member, IEEE,
David J. Frank, Fellow, IEEE, and Saibal Mukhopadhyay, Senior Member, IEEE

Abstract—Deposition of a metal gate on high-$\kappa$ dielectric $\text{HfO}_2$ is known to generate oxygen vacancy (OVs) defects. Positively charged OVs in the dielectric affect the gate electrostatics and modulate the effective gate workfunction (WF). Count and spatial allocation of OVs varies from device-to-device and induces significant local variability in WF and $V_{th}$. This paper presents the statistical models to simulate OV concentration and placement depending on the gate formation conditions. OV-induced variability is studied for SOI FinFET, and compared against the other sources of variability across the technologies. The implications of gate first and gate last processes to the OV concentration/distribution are studied. Simulations show that with channel length and gate dielectric thickness scaling, the OV-induced variability becomes a significant concern.

Index Terms—FinFET, local variability, oxygen vacancy, variability in high-$\kappa$/metal gate-stacks.

![](./images/813148565273575425_1.jpg)

Fig. 1. OV generation by oxygen atom dislocation from $\text{HfO}_2$ molecule.

## I. INTRODUCTION
$T$HE effective gate workfunction (WF) in $\text{HfO}_2$/metal gated transistors is observed to shift from its theoretical value [1]–[6]. The anomalous WF shift is attributed to charged defects, oxygen vacancy (OVs) defects. An OV is a thermo-dynamic point defect caused by the diffusion of oxygen from $\text{HfO}_2$, which leaves behind a doubly charged vacancy defect, $V_O^{++}$ (Fig. 1). The presence of positively charged $V_O^{++}$ alters the gate electrostatics. By annealing the gate-stack with $\text{O}_2/\text{N}_2$, and thus passivating the OVs, an effective $V_{FB}$ modulation can be measured [1]–[6]. Furthermore, in nanoscaled transistors, as the count and spatial allocation of OVs varies from device-to-device, OVs also induce a significant local variability in WF, and hence, in threshold voltage ($V_{\text{th}}$).

Several studies have investigated OVs through experiments and simulations. Takeuchi *et al.* [2] have measured the energy level of OVs ($E_{\text{OV}}$) through absorption spectra of $\text{HfO}_2$. Cartier *et al.* [7] presented charge pump-based experiments to measure $E_{\text{OV}}$. Later, Cartier *et al.* [7] also estimated OV concentration by monitoring oxygen isotope$^{18}\text{O}$ uptake [5]. Xiong *et al.* [8] presented density functional theory (DFT)-based models to predict the OV trap energy level. Broqvist *et al.* [9] computed $E_{\text{OV}}$ for amorphous $\text{HfO}_2$ (a-$\text{HfO}_2$) using *ab initio* molecular dynamics and hybrid density functionals. Using DFT computations, the distribution of $E_{\text{OV}}$ in a-$\text{HfO}_2$ was computed, and compared against the monoclinic and cubic $\text{HfO}_2$ [10]. Recently, for Ge channel devices, the generation of OVs in high-$\kappa$/Ge stack was studied using first principle calculations [11].

Among the modeling works investigating the implications of OVs, Shiraishi *et al.* [12] modeled the effective WF shift across $\text{HfO}_2$ thickness and gate Fermi level. Guha and Narayanan [13] modeled the OV-induced $V_{\text{th}}$ shift against the oxygen partial pressure ($p_{\text{O2}}$) during gate formation. Robertson *et al.* [14] presented models to predict the OV concentration versus the gate WF. The role of OV point defects in WF modulation in ultrascaled CMOS devices was studied [15]. While the WF shift due to OV concentration has been studied both experimentally and theoretically, the OV-induced WF ($V_{\text{th}}$) variability has received a limited attention. Since the device-to-device variability of electrical parameters such as $V_{\text{th}}$ increases as the dimensions of transistors scale down, becoming a key limiting factor in circuit design, it is critical to understand the OV-induced $V_{\text{th}}$ variability.

This paper studies this OV-induced $V_{\text{th}}$ variability in SOI FinFETs. In Section II, we present the Law of mass

Manuscript received October 2, 2013; revised December 18, 2013 and January 22, 2014; accepted March 10, 2014. Date of publication April 3, 2014; date of current version April 18, 2014. This work was supported by the National Science Foundation. The review of this paper was arranged by Editor H. S. Momose.

A. R. Trivedi and S. Mukhopadhyay are with the Department of Electrical and Computer Engineering, Georgia Institute of Technology, GA 30332 USA (e-mail: amitrt@ece.gatech.edu; saibal@ece.gatech.edu).

T. Ando, A. Singhee, P. Kerber, E. Acar, and D. J. Frank are with the IBM T. J. Watson Research Center, Yorktown-Heights, NY 10598 USA (e-mail: andot@us.ibm.com; asinghe@us.ibm.com; k_pranita@us.ibm.com; emrah@us.ibm.com; djf@us.ibm.com).

Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.

Digital Object Identifier 10.1109/TED.2014.2313086

0018-9383 © 2014 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.

![](./images/813148565273575425_2.jpg)

Fig. 2. (a) Surplus electrons fall from the trap energy level into the lower energy metal electrode, and OV dipole forms (b) OV induced dipole created by the mirror charge.

action-based model equations to evaluate the OV concentration/distribution across the gate-stack formation process parameters. Spatial allocation of OVs is studied, and correlation to the standard distribution models is explored. In Section III, using the above OV distribution in TCAD simulations, OV-induced $V_{\text{th}}$ shift and variability is evaluated across technologies for SOI FinFETs. OV-induced variability is compared against the other known sources, random dopant fluctuation (RDF), metal gate granularity (MGG), and fin/gate edge roughness (FER/GER) from [16]. At the end, key conclusions are presented in Section IV.

## II. STATISTICAL MODEL FOR OXYGEN VACANCY CONCENTRATION AND PLACEMENT

An OV is a thermodynamic point defect formed by the diffusion of an oxygen atom from $\text{HfO}_2$, which also generates surplus electrons in its place. Considering delocalization of the surplus electrons, Shiraishi *et al.* [17] explained the higher OV concentration in $\text{HfO}_2$ than in $\text{SiO}_2$. The delocalized electrons fall from the trap energy level ($E_{\text{OV}}$) to the lower energy metal electrode [Fig. 2(a)], and this reduces the effective formation energy of OVs in $\text{HfO}_2$ and contributes to the higher OV concentration [14]. Statistical models to evaluate the concentration and placement of OVs depending on the gate-stack process are presented here.

The generation of OV can be expressed as
$$
O_{O}^{x} \leftrightarrow V_{O}^{++}+2 e+\frac{1}{2} O_{2}-\Delta G_{1}^{0}. \tag{1}
$$

Here, $O_{O}^{x}$ is an oxygen atom in the dielectric $\text{HfO}_2$, e is the delocalized surplus electron created by OV formation, $O_2$ is the oxygen gas molecule, and $\Delta G_{1}^{0}$ is the standard free energy of exchange in OV formation. At equilibrium, according to the law of mass action, the effective OV concentration is established as [18]
$$
\frac{\left[V_{O}^{++}\right]}{\left[O_{O}^{x}\right]}[e]^{2} p_{O 2}^{1 / 2}=\exp \left(-\frac{\Delta G_{1}^{0}}{k T_{\mathrm{G}, \mathrm{form}}}\right). \tag{2a}
$$

Here, the quantities in the brackets [] represent the corresponding concentration. $T_{\mathrm{G}, \text{ form}}$ is the gate-stack formation temperature. OV-liberated electrons are collected by the adjacent metal electrode. Hence, using Fermi-Dirac statistics [18], the electron concentration can be expressed as
$$
[e]=\frac{1}{1+\exp \left(\frac{E_{o v(r)}-E_{F, m}}{k T_{\mathrm{G}, \mathrm{form}}}\right)} \approx \exp \left(-\frac{E_{o v(r)}-E_{F, m}}{k T_{\mathrm{G}, \mathrm{form}}}\right).(2 \mathrm{b})
$$

Here, $E_{\mathrm{F}, \mathrm{m}}$ is the metal Fermi energy level. Using (2a) and (2b), the probability of OV generation will be given as
$$
\begin{aligned}
P_{O V}(r) &=\frac{\left[V_{O}^{++}\right]}{\left[O_{O}^{x}\right]} \\
&=\frac{1}{p_{O 2}^{1 / 2}} \exp \left(-\frac{\Delta G_{1}^{0}}{k T_{G, f o r m}}+2 × \frac{E_{O V}(r)-E_{F, m}}{k T_{G, f o r m}}\right). \quad(3)
\end{aligned}
$$

However, due to its positive charge, an OV affects the potential field and defect energy level, $E_{\text{OV}}$, in its proximity, as shown in Fig. 2(a). With the local variation in $E_{\text{OV}}$ relative to the metal Fermi level, $E_{\mathrm{F}, \mathrm{m}}$, the generation of another OV in proximity is also affected as is evident from (3). The potential field due to the positively charged OV can be analyzed by the method of mirror charges [19], where an opposite and equidistant charge from the metal interface is considered, as shown in Fig. 2(b). Considering the dipole formed by the OV and its mirror charge, the potential field of an OV dipole can be approximated as
$$
\Delta V(r) \approx \frac{q}{4 \pi \varepsilon} \frac{2 d × \sin \theta}{r^{2}}. \tag{4}
$$

The position of the dipole relative to the observation point r is shown in Fig. 2(b), along with the notations, $d$, $r$, and $\theta$. Thus, accounting for the potential field of existing OV-induced dipoles ($\Delta \mathrm{V}_{\mathrm{i}}(\mathrm{r})$), the probability of OV generation is expressed as
$$
\begin{aligned}
P_{\mathrm{OV}}(r)=\frac{\left[V_{O}^{++}\right]}{\left[O_{O}^{x}\right]}=& \frac{1}{p_{O 2}^{1 / 2}} × \\
& \exp \left(-\frac{\Delta G_{1}^{0}}{k T_{\mathrm{G}, \mathrm{form}}}+2 × \frac{E_{\mathrm{OV}}(r)-\sum_{i} \Delta V_{i}(r)-E_{F, m}}{k T_{\mathrm{G}, \mathrm{form}}}\right).
\end{aligned}
\tag{5}
$$

### A. Simulation Methodology for OV placement

The OV probability expression developed in (5) is used to mimic the random placement of OVs in a $\text{HfO}_2$ layer.

![](./images/813148565273575425_3.jpg)

Fig. 3. OV concentration and variability while varying. (a) Oxygen partial pressure (pO2). (b) Gate-stack formation temperature. (c) Gate WF (T = 1300 K corresponds to the GF process and T = 750 K to the GL process).

<table>
  <thead>
    <tr>
      <th colspan="2">TABLE I<br>OXYGEN VACANCY GENERATION MODEL PARAMETERS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>a-HfO2 parameter</td>
      <td>Value</td>
    </tr>
    <tr>
      <td>Standard free energy of<br>OV formation $\Delta G_1^0$</td>
      <td>3eV [18]</td>
    </tr>
    <tr>
      <td>Electron affinity</td>
      <td>2.45eV [9]</td>
    </tr>
    <tr>
      <td>$\Delta(E_C-E_{OV})$</td>
      <td>1.2eV [5]</td>
    </tr>
    <tr>
      <td>TiN parameter</td>
      <td>Value</td>
    </tr>
    <tr>
      <td>Vac. Work function</td>
      <td>4.7eV [6]</td>
    </tr>
  </tbody>
</table>

Films with the dimensions of the HfO₂ layer, as in a transistor, are meshed with the node density $\sim$55/nm³. This is equivalent to the oxygen atom density in the HfO₂ layer [20]. Each mesh node is considered for possible placement of an OV. To emulate the amorphous nature of HfO₂ film, the order in which the mesh nodes are considered is randomized. Using the gate-stack process parameters ($T_{\text{G, form}}$, pO₂, and gate WF), the expression in (5) is evaluated, and an OV is placed based on the probability $P_{\text{OV}}$(r). Various parameter values for (5) are listed in Table I. Based on [18], for ultrathin films of HfO₂, the value $\Delta G_1^0 = 3$ eV is used in our work. As discussed in [18], this value of $\Delta G_1^0$ explains the experimental observations for the HfO₂/metal gate-stacks in [13]. The energy level $E_{\text{OV}}$ is 1.2 eV from the HfO₂ conduction band, and it corresponds to the donor level of the doubly charged vacancy, $\text{V}_\text{O}^{++}$. Based on *ab initio* calculations for a-HfO₂, the trap charge transition level from the neutral OV to $\text{V}_\text{O}^{++}$ was computed as $\sim$1.1 eV below the HfO₂ conduction band [9]. Likewise, based on absorption spectra, the trap energy level of the HfO₂ films deposited on silicon was found to be $\sim$1.2 eV from the HfO₂ conduction band [2]. In agreement with the above work, here we have taken the donor energy level ($E_{\text{OV}}$) as 1.2 eV below the HfO₂ conduction band, since, as discussed subsequently, it also corroborates the OV concentration from our model to the experimentally observed concentration in [5].

### B. Simulation Results

OV concentration ($N_{\text{OV}}$) and spatial distribution results based on the above simulation methodology are shown in Fig. 3. Mean $N_{\text{OV}}$ and variability in $N_{\text{OV}}$ are demonstrated as a function of oxygen partial pressure (pO₂), gate-stack formation temperature ($T_{\text{G, form}}$), and WF. Statistics are extracted over 100 random samples. $N_{\text{OV}}$ increases with reducing pO₂, increasing $T_{\text{G, form}}$, and increasing WF. At higher $N_{\text{OV}}$, the variability in OV count also increases. In Fig. 3(c), the gate last (GL) process ($T_{\text{G, form}} = 750$ K) generates a fewer OVs than the gate first (GF) process ($T_{\text{G, form}} = 1300$ K) for the same WF gate. For the GF processed TiN/HfO₂ gate-stack, the OV concentration was estimated to be $\sim$$2 \times 10^{13} - 3.9 \times 10^{14}$/cm² experimentally [5]. Considering vacuum WF of TiN as 4.7 eV [6], this relates well to our simulation results in Fig. 3(c).

![](./images/813148565273575425_4.jpg)

Fig. 4. (a) OV distribution along the depth in HfO₂ layer, and correlation to truncated Exponential distribution E($\lambda$). (b) $\lambda$ for varying mean OV concentration and gate-stack processing temperatures.

The distribution of OVs within the HfO₂ is shown in Fig. 4(a). Due to the angular dependence of the OV dipole potential field, the distribution is self-limiting toward the HfO₂/metal interface. The dipole potential field (4) diminishes for $\theta \to 0$, i.e., for locations close to the HfO₂/metal interface. Hence, $P_{\text{OV}}$(r) is not affected at these locations by the presence of other OVs in proximity, resulting in higher OV segregation toward the HfO₂/metal interface. The OV distribution correlates to the truncated exponential distribution (E($\lambda$)) over the HfO₂ thickness, $T_{\text{HK}}$, where

$$
E(\lambda)=\frac{1}{\lambda}\left(\frac{\exp (-x / \lambda)}{1-\exp \left(-T_{\text{HK}} / \lambda\right)}\right). \tag{6}
$$

Here, $x$ is the depth into the HfO₂ ($x =0$ is the metal interface) and $\lambda$ is the skewness parameter of the exponential distribution. By fitting the mean OV distribution to E($\lambda$) for various samples, the skewness parameter $\lambda$ versus mean $N_{\text{OV}}$ is found [Fig. 4(b)]. At higher $N_{\text{OV}}$, $\lambda$ decreases, which

![](./images/813148565273575425_5.jpg)
![](./images/813148565273575425_6.jpg)
![](./images/813148565273575425_7.jpg)

Fig. 5. (a) FinFET schematic. (b) Charged cubes (0.5 nm) representing a random placement and count of positively charged OV in the HfO₂ layer to induce local variability. (c) OV-induced local variability in surface potential at the channel/oxide interface.

<table><tbody><tr><td colspan="4">TABLE II<br>FinFET Specifications</td></tr><tr><td>Spec.</td><td>22nm</td><td>16nm</td><td>11nm</td></tr><tr><td>L<sub>gate</sub> (nm)</td><td>20</td><td>14</td><td>10</td></tr><tr><td>T<sub>ox</sub> (nm)</td><td>0.48</td><td>0.40</td><td>0.34</td></tr><tr><td>T<sub>HK</sub> (nm)</td><td>2</td><td>1.7</td><td>1.4</td></tr><tr><td>H<sub>FIN</sub> (nm)</td><td>25</td><td>17.5</td><td>12.5</td></tr><tr><td>W<sub>FIN</sub> (nm)</td><td>10</td><td>7</td><td>5</td></tr><tr><td>N<sub>SD</sub> (cm⁻³)</td><td>3×10²⁰</td><td>3×10²⁰</td><td>3×10²⁰</td></tr><tr><td>V<sub>DD</sub> (V)</td><td>1</td><td>0.9</td><td>0.8</td></tr><tr><td>SS (mV/dec)</td><td>77.5</td><td>74</td><td>72</td></tr><tr><td>V<sub>th,sat</sub> (mV)</td><td>0.31</td><td>0.31</td><td>0.31</td></tr><tr><td>DIBL (mV/V)</td><td>46.3</td><td>50.6</td><td>53</td></tr><tr><td>I<sub>ds,sat</sub> (mV/μA)</td><td>1.41</td><td>1.70</td><td>1.97</td></tr></tbody></table>

indicates that the majority of OV concentration is segregated toward the metal/HfO₂ interface. Comparing $\lambda$ at the same N<sub>OV</sub> for the two gate processes (GF and GL), it is seen that GL has smaller $\lambda$. At lower $T_{\text{G, form}}$, the greater sensitivity of $\Delta\text{V(r)}$ to OV probability (5), causes an even greater self-limiting, hence, a smaller $\lambda$, or a higher segregation probability toward the metal/HfO₂ interface for the GL process.

Hence, OV concentration increases with the increasing gate processing temperature, increasing WF, and decreasing po₂. At the higher OV concentration, most of the OVs segregate toward the HfO₂/metal interface. Low gate processing temperature also limits the OV concentration away from the channel. Using the above simulation framework, the OV-induced variability in high-$\kappa$/metal gate-stacked FinFETs is studied in Section III.

### III. OXYGEN VACANCY-INDUCED VARIABILITY IN TRI-GATED SOI FINFET

Variability in $V_{\text{th}}$ due to the variability in count and placement of OVs in the gate-stack is studied for the tri-gated SOI FinFET. A schematic drawing of a FinFET is shown in Fig. 5(a). The gate-stack consists of interfacial oxide, HfO₂, and TiN metal electrode. The channel is considered to be undoped. FinFETs of 22, 16, and 11-nm channel length technology are studied. Various geometry and electrical specifications are listed in Table II. Similar FinFET structures were studied in [16] for the RDF, MGG, and FER/GER variability. To facilitate comparison between the OV-induced variability and the other sources of variability, similar FinFET structures are being studied here.

#### A. Simulation Methodology for Oxygen Vacancy-Induced Variability

Following the methodology in Section II, the spatial distribution and concentration of OVs in the HfO₂ layer is obtained. The OV distribution/concentration is obtained for the process parameters: WF = 4.7 eV (TiN vacuum value), po₂ = $5 \times 10^{-8}$ atm, and $T_{\text{G, form}} = 1300$ K (GF process) and 750 K (GL process). Each OV is represented by a charge cube (dimension: 0.5 nm), and charge density equivalent to two electron charges. Using Sentaurus Structure Editor [21], these charged cubes are placed in the HfO₂ layer with the corresponding spatial distribution, as shown in Fig. 5(b). Simulations of electrical characteristics were performed using Sentaurus device [21]. Unified mobility models from [22] were used. Scattering models for the mobility degradation at the channel/gate interface due to high-$\kappa$ dielectric were used [23]. Quantum confinement models were used in the channel. A sample distribution of OV-induced surface potential variability at the oxide/channel interface is shown in Fig. 5(c). A significant local variability in the potential, ~0.4–0.65 V, is observed. Sharper transitions correspond to the vacancies located closer to the channel. Due to their greater electric field at the oxide/channel interface, a greater gradient in the potential field occurs.

#### B. Oxygen Vacancy-Induced Variability in FinFET

An ensemble of I<sub>DS</sub>–V<sub>GS</sub> characteristics ($V_{\text{DS}} = V_{\text{DD}} = 1$ V) for the 22-nm technology n-FinFET with OVs is shown in Fig. 6(a). Hereafter, the presented statistical characteristics are extracted over 100 random samples. By reducing the effective WF of the metal electrode, OVs shift the $V_{\text{th}}$ by ~0.17 V. The distribution of OV-induced $V_{\text{th}}$ variability is shown in Fig. 6(b), where OV induces ~20 mV $3\sigma$-variability in $V_{\text{th}}$. In Fig. 6(c), the correlation of $V_{\text{th}}$ quantiles against the standard Normal is shown for the various technologies.

![](./images/813148565273575425_8.jpg)

![](./images/813148565273575425_9.jpg)

The $V_{\text{th}}$ distribution closely resembles the standard Normal. Moreover, the $V_{\text{th}}$ variability increases for the smaller channel length technology.

In Fig. 7, the $V_{\text{th}}$ shift, $\Delta V_{\text{th}}$, and variability, $\sigma(V_{\text{th}})$, due to OVs are shown for the varying mean OV concentration across the technologies. The OV concentration was generated for a TiN gate ($\text{WF}=4.7$ eV), GF processing temperature ($T_{\text{G,form}}=1300$ K), and for varying $\text{p}_\text{O2}$. Here, $\Delta V_{\text{th}}$ and $\sigma(V_{\text{th}})$ increase with the higher OV concentration. At the same OV concentration, the smaller channel length technology exhibits a smaller $\Delta V_{\text{th}}$ but larger $\sigma(V_{\text{th}})$. For the 11-nm technology, we also show the results for the GL processing temperature ($T_{\text{G, form}}=750$ K). As shown in Fig. 4(b), at the lower gate processing temperature, the OV concentration has a greater segregation probability toward the metal/HfO$_2$ interface and away from the channel. Comparing $\sigma(\text{V}_\text{th})$ at the same $N_{\text{OV}}$, the GL process exhibits a lesser variability than the GF process, due to this OV segregation away from the channel.

The effect of OV placement is studied in Fig. 8. Here, we limit the OV allocation to a plane. For the same OV concentration, the plane is traversed from the oxide interface toward the metal interface in HfO$_2$. $\Delta V_{\text{th}}$ and $\sigma(V_{\text{th}})$ are demonstrated against the separation of OV plane from the oxide interface. As the plane traverses closer to the channel, $\Delta V_{\text{th}}$ and $\sigma(V_{\text{th}})$ significantly increase. OVs closer to the channel impart a greater electric field to the channel to induce a greater $\Delta V_{\text{th}}$ and greater local variability in the surface potential [hence, larger $\sigma(V_{\text{th}})$]. This also explains the observation in Fig. 7(b), where due to the accumulation of OVs away from the channel, the GL process results into lesser variability than the GF process.

![](./images/813148565273575425_10.jpg)

![](./images/813148565273575425_11.jpg)

Fig. 10. OV-induced variability compared with the other sources of variability: RDF, MGG, FER, and GER.

The dependence of OV-induced variability on FinFET

![](./images/813148565273575425_12.jpg)

Fig. 11. (a) MGG demonstration. (b) MGG-induced $V_{th}$ distribution for the 11-nm FinFET device. (c) Variability at varying grain sizes and orientation probabilities.

geometry is studied in Fig. 9. In Fig. 9(a), as the HfO₂ thickness, $T_{HK}$, is scaled down, OVs are placed closer to the channel, and the OV-induced variability increases. Thus, the OV-induced variability is expected to be a limitation to high-$\kappa$ dielectric thickness scaling in future technology nodes. By varying $L_{CH}$, $H_{FIN}$, and $W_{FIN}$ for the 11-nm device, we study the variability against the varying gate area. Various sample geometries correspond to a $\pm$30% deviation from the nominal LCH and HFIN, and a $\pm$20% from the nominal WFIN. A close correlation between the Pelgrom's model and the simulation results is shown in Fig. 9(b).

The total variability of FinFET, consisting of RDF, MGG, FER, GER, and OV-induced variability, is shown in Fig. 10. The other variability results (i.e., for RDF, MGG, FER, and GER) were presented for similar FinFET structures in [16]. Here, the total variability increases for smaller channel length technologies, along with all the other variability components. By comparison with the other sources of variability, it is observed that the OV-induced variability becomes a significant component.

### C. Oxygen Vacancy Versus MGG-Induced Variability

Among the discussed variability sources, OVs and MGG are also relevant to the other high-$\kappa$/metal gate structures (and not just FinFETs). MGG as a variability concern was addressed [24], [25]. Summarizing a few relevant process developments, we argue that OVs becomes a greater concern for WF variability in high-$\kappa$/metal gate structures than MGG.

Metal grains exist in the deposited metal electrode with random grain orientations and grain sizes. WF of metal grain varies with its orientation. Hence, as the grain size and orientation varies from device-to-device, it contributes to the local variability in WF and $V_{th}$. The MGG-induced variability is studied for varying grain sizes and orientation probability. Using Sentaurus Structure Editor, the metal gate is granularized and grains are randomly assigned an orientation, as shown in Fig. 11(a). For TiN, the majority of grains were observed to be aligned to <111> or <100> [25], and we restrict our analysis to these two grain orientations only. Using Sentaurus Device, we extract statistics from simulations of 100 random samples. The distribution of $V_{th}$ is shown in Fig. 11(b) for various <100> orientation probability. Since the MGG-induced distribution is not always Normal, the effective $\sigma_{eq}$ is estimated as one sixth of the 99.7% confidence interval of $V_{th}$. In Fig. 11(c), the MGG-induced variability is shown for the varying grain sizes and orientation probabilities. The variability reduces for smaller grain size. Also, as the predominance of either grain orientation occurs, the variability decreases. Process techniques to reduce the grain size [26] and align grain orientation [27] were demonstrated. Also, note that the grain size reduces with the scaling film thickness [28], and it will reduce with the scaling of gate film thickness in the future technology nodes. Using these techniques, the MGG-induced variability can be significantly contained. Meanwhile, the OV generation is intrinsic to the Hf-based high-$\kappa$ dielectrics, and difficult to avoid. Hence, we believe that the OV becomes a more significant concern for WF variability than the MGG.

### IV. CONCLUSION

OV becomes an important source of variability in the scaled high-$\kappa$/metal gate-stacked transistors. Statistical models to mimic the OV concentration/distribution based on the gate processing conditions are presented. For the low temperature GL process, the OV concentration is reduced, and the OV distribution has a greater segregation toward the metal/HfO₂ interface, and away from the channel. TCAD simulation methodology to extract OV-induced variability is presented, and results are shown for the tri-gated SOI FinFET. Comparing with the other sources of variability, OVs become an important component. With self-limiting of OVs away from the channel, the GL process reduces the OV-induced variability. Intrinsic OV generation to the Hf-based dielectric/metal interface makes it difficult to avoid, and the OV-induced variability modeling grows in significance.

### REFERENCES

[1] J. K. Schaeffer, L. R. C. Fonseca, S. B. Samavedam, Y. Liang, P. J. Tobin, and B. E. White, "Contributions to the effective work function of platinum on hafnium dioxide," *Appl. Phys. Lett.*, vol. 85, no. 10, pp. 1826-1828, 2004.

[2] H. Takeuchi, H. Daewon, and T.-J. King, "Observation of bulk HfO₂ defects by spectroscopic ellipsometry," *J. Vac. Sci., Technol. A, Vac., Surf., Films*, vol. 22, no. 4, pp. 1337-1341, 2004.

[3] H. Takeuchi, W. H. Yung, H. Daewon, and T.-J. King, "Impact of oxygen vacancies on high-k gate stack engineering," in *Proc. IEEE IEDM*, Dec. 2004, pp. 829-832.

[4] E. Cartier *et al.*, "Role of oxygen vacancies in VFB/Vt stability of pFET metals on HfO₂," in *Proc. Symp. VLSI Technol.*, 2005, pp. 230-231.

[5] E. Cartier, M. Hopstaken, and M. Copel, "Oxygen passivation of vacancy defects in metal-nitride gated HfO₂/SiO₂/Si devices," *Appl. Phys. Lett.*, vol. 95, no. 1, pp. 042901-1-042901-3, 2009.

[6] E. Cartier *et al.*, "pFET Vt control with HfO₂/TiN/poly-Si gate stack using a lateral oxygenation process," in *Proc. Symp. VLSI Technol.*, 2009, pp. 42-43.

[7] E. Cartier, B. P. Linder, V. Narayanan, and V. K. Paruchuri, "Fundamen- tal understanding and optimization of PBTI in nFETs with SiO₂/HfO₂ gate stack," in *Proc. IEDM*, 2006, pp. 1-4.

[8] K. Xiong, J. Robertson, M. C. Gibson, and S. J. Clark, "Defect energy levels in HfO₂ high-dielectric-constant gate oxide," *Appl. Phys. Lett.*, vol. 87, no. 18, pp. 183505-1-183505-3, 2005.

[9] P. Broqvist, A. Alkauskas, and A. Pasquarello, "Band alignments and defect levels in Si/HfO₂ gate stacks: Oxygen vacancy and fermi-level pinning," *Appl. Phys. Lett.*, vol. 92, no. 13, pp. 132911-1-132911-3, 2008.

[10] C. Kaneta and T. Yamasaki, "Oxygen-related defects in amorphous HfO₂ gate dielectrics," *Microelectron. Eng.*, vol. 84, no. 9, pp. 2370-2373, 2007.

[11] E. Golias, L. Tsetseris, A. Chroneos, and A. Dimoulas, "Interaction of metal impurities with native oxygen defects in GeO2," *Microelectron. Eng.*, vol. 104, pp. 37-41, Apr. 2013.

[12] K. Shiraishi *et al.*, "Physics in fermi level pinning at the poly Si/Hf- based high-k oxide interface," in *Proc. VLSI Technol. Dig. Tech. Papers*, 2004, pp. 108-109.

[13] S. Guha and V. Narayanan, "Oxygen vacancies in high dielectric constant oxide-semiconductor films," *Phys. Rev. Lett.*, vol. 98, no. 19, p. 196101, 2007.

[14] J. Robertson, O. Sharia, and A. A. Demkov, "Fermi level pinning by defects in HfO₂-metal gate stacks," *Appl. Phys. Lett.*, vol. 91, no. 13, pp. 132912-1-132912-3, 2007.

[15] R. K. Pandey, R. Sathiyanarayanan, U. Kwon, V. Narayanan, and K. V. R. M. Murali, "Role of point defects and HfO₂/TiN interface stoichiometry on effective work function modulation in ultra-scaled complementary metal-oxide-semiconductor devices," *J. Appl. Phys.*, vol. 114, no. 3, pp. 034505-1-034505-7, 2013.

[16] W. Xingsheng, A. R. Brown, C. Binjie, and A. Asenov, "Statistical variability and reliability in nanoscale FinFETs," in *Proc. IEEE IEDM*, Dec. 2011, pp. 5.4.1-5.4.4.

[17] K. Shiraishi *et al.*, "Oxygen-vacancy-induced threshold voltage shifts in Hf-related high-k gate stacks," *Thin Solid Films*, vol. 508, pp. 305-310, May 2006.

[18] S. Guha and P. Solomon, "Band bending and the thermochemistry of oxygen vacancies in ionic metal oxide thin films," *Appl. Phys. Lett.*, vol. 92, no. 1, pp. 012909-1-012909-3, 2008.

[19] C. Kittel, *Introduction to Solid State Physics*. New York, NY, USA: Wiley, 1986.

[20] D. Ceresoli and D. Vanderbilt, "Structural and dielectric properties of amorphous ZrO₂ and HfO₂," *Phys. Rev. B*, vol. 74, p. 125108, Sep. 2006.

[21] Synopsys Sentaurus [Online]. Available: http://www.synopsys.com/tools/tcad/Pages/default.aspx

[22] K. Y. Toh, P. K. Ko, and R. G. Meyer, "An engineering model for short- channel MOS devices," *IEEE J. Solid-State Circuits*, vol. 23, no. 4, pp. 950-958, Aug. 1988.

[23] C. Lombardi, S. Manzini, A. Saporito, and M. Vanzi, "A physically based mobility model for numerical simulation of nonplanar devices," *IEEE Trans. Comput. Aided Des. Integr. Circuits Syst.*, vol. 7, no. 11, pp. 1164-1171, Nov. 1988.

[24] H. Dadgour, K. Endo, V. De, and K. Banerjee, "Modeling and analysis of grain-orientation effects in emerging metal-gate devices and implications for SRAM reliability," in *Proc. IEEE IEDM*, Feb. 2008, pp. 1-4.

[25] H. F. Dadgour, K. Endo, V. K. De, and K. Banerjee, "Grain- orientation induced work function variation in nanoscale metal-gate transistors-Part I: Modeling, analysis, and experimental validation," *IEEE Trans. Electron Devices*, vol. 57, no. 10, pp. 2504-2514, Oct. 2010.

[26] K. Ohmori *et al.*, "Impact of additional factors in threshold voltage variability of metal/high-k gate stacks and its reduction by controlling crystalline structure and grain size in the metal gates," in *Proc. IEEE IEDM*, Jun. 2008, pp. 1-4.

[27] R. Banerjee, R. Chandra, and P. Ayyub, "Influence of the sputtering gas on the preferred orientation of nanocrystalline titanium nitride thin films," *Thin Solid Films*, vol. 405, pp. 64-72, Feb. 2002.

[28] J. M. López, F. J. Gordillo-Vázquez, O. Böhme, and J. M. Albella, "Low grain size TiN thin films obtained by low energy ion beam assisted deposition," *Appl. Surf. Sci.*, vol. 173, pp. 290-295, Mar. 2001.

![](./images/813148565273575425_13.jpg)

Amit Ranjan Trivedi (S'10) is currently pursuing the Ph.D. degree with the Georgia Institute of Tech- nology, Atlanta, GA, USA.

He was a Research Staff Member with IBM Semiconductors Research and Development Center, Bangalore, India, involved in compact modeling and process/device characterization. His current research interest includes ultralow-power devices and circuits, and process induced variability at advanced nanome- ter node transistors.

![](./images/813148565273575425_14.jpg)

Takashi Ando (SM'11) received the B.S. and M.E. degrees from the University of Tokyo, Tokyo, Japan, and the Ph.D. degree from Osaka University, Suita, Japan, in 1999, 2001, and 2010, respectively.

He has been a Research Staff Member with the IBM T. J. Watson Research Center, Yorktown- Heights, NY, USA, since 2008. He has authored and co-authored more than 60 publications.

![](./images/813148565273575425_15.jpg)

Amith Singhee (SM'14) is a Research Staff Mem- ber with the IBM T. J. Watson Research Center, Yorktown-Heights, NY, USA, where he is involved in smart grid applications and simulation, modeling, and optimization of analog and memory circuits.

Dr. Singhee has served as a Program Chair for the IEEE International Workshop on Design for Manufacturability and Yield and on the Program Committee of the IEEE International Conference on Computer-Aided Design.

![](./images/813148565273575425_16.jpg)

Pranita Kerber received the M.S. and Ph.D. degrees in materials science and engineering from Carnegie Mellon University, Pittsburgh, PA, USA, in 2006 and 2008, respectively.

She joined IBM Corporation, Armonk, NY, USA, as a Research Staff Member in 2008, where she conducts research in process and device simulation of advanced semiconductor devices and circuits. She is a reviewer for numerous IEEE publications.

![](./images/813148565273575425_17.jpg)

Emrah Acar (SM'06) received the Ph.D. degree in electrical and computer engineering from Carnegie Mellon University, Pittsburgh, PA, USA, in 2001.

He has been with IBM Research as a Research Staff Member since graduation. His current research interests include modeling and simulation of devices, circuits, systems, power modeling and optimization, statistical modeling, prediction and optimization, and data analytics.

![](./images/813148565273575425_18.jpg)

David J. Frank (F'03) received the B.S. degree from the California Institute of Technology, Pasadena, CA, USA, and the Ph.D. degree in physics from Harvard University, Cambridge, MA, USA, in 1977 and 1983, respectively.

He has been a Research Staff Member with the IBM T. J. Watson Research Center, Yorktown-Heights, NY, USA. His current research interests include superconductivity, III-V devices, and the limits of silicon technology scaling.

![](./images/813148565273575425_19.jpg)

Saibal Mukhopadhyay (SM'11) received the Ph.D. degree in electrical and computer engineering from Purdue University, West Lafayette, IN, USA.

He was with the IBM T. J. Watson Research Center, Yorktown-Heights, NY, USA, as a Research Staff Member. Then, he joined the Faculty of the Georgia Institute of Technology, Atlanta, GA, USA, in 2007. His research interest is in low power circuit design at advanced nanometer nodes.