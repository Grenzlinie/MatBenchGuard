A physically constrained classical description of the homogeneous nucleation of ice in water

Thomas Koop and Benjamin J. Murray

Citation: *J. Chem. Phys.* **145**, 211915 (2016); doi: 10.1063/1.4962355
View online: http://dx.doi.org/10.1063/1.4962355
View Table of Contents: http://aip.scitation.org/toc/jcp/145/21
Published by the American Institute of Physics

---

Articles you may be interested in

On the time required to freeze water
*J. Chem. Phys.* **145**, 211922 (2016); 10.1063/1.4965427

Pre-ordering of interfacial water in the pathway of heterogeneous ice nucleation does not lead to a two-step crystallization mechanism
*J. Chem. Phys.* **145**, 211910 (2016); 10.1063/1.4961652

Crystal nucleation as the ordering of multiple order parameters
*J. Chem. Phys.* **145**, 211801 (2016); 10.1063/1.4962166

Overview: Homogeneous nucleation from the vapor phase—The experimental science
*J. Chem. Phys.* **145**, 211702 (2016); 10.1063/1.4962283


# A physically constrained classical description of the homogeneous nucleation of ice in water

Thomas Koop${}^{1,a)}$ and Benjamin J. Murray${}^{2,a)}$

${}^{1}$Faculty of Chemistry, Bielefeld University, Bielefeld, Germany
${}^{2}$Institute for Climate and Atmospheric Science, School of Earth and Environment, University of Leeds,
Leeds, United Kingdom

(Received 10 June 2016; accepted 25 August 2016; published online 26 September 2016)

Liquid water can persist in a supercooled state to below 238 K in the Earth's atmosphere, a temperature range where homogeneous nucleation becomes increasingly probable. However, the rate of homogeneous ice nucleation in supercooled water is poorly constrained, in part, because supercooled water eludes experimental scrutiny in the region of the homogeneous nucleation regime where it can exist only fleetingly. Here we present a new parameterization of the rate of homogeneous ice nucleation based on classical nucleation theory. In our approach, we constrain the key terms in classical theory, i.e., the diffusion activation energy and the ice-liquid interfacial energy, with physi-cally consistent parameterizations of the pertinent quantities. The diffusion activation energy is related to the translational self-diffusion coefficient of water for which we assess a range of descriptions and conclude that the most physically consistent fit is provided by a power law. The other key term is the interfacial energy between the ice embryo and supercooled water whose temperature dependence we constrain using the Turnbull correlation, which relates the interfacial energy to the difference in enthalpy between the solid and liquid phases. The only adjustable parameter in our model is the abso-lute value of the interfacial energy at one reference temperature. That value is determined by fitting this classical model to a selection of laboratory homogeneous ice nucleation data sets between 233.6 K and 238.5 K. On extrapolation to temperatures below 233 K, into a range not accessible to standard techniques, we predict that the homogeneous nucleation rate peaks between about 227 and 231 K at a maximum nucleation rate many orders of magnitude lower than previous parameterizations suggest. This extrapolation to temperatures below 233 K is consistent with the most recent measurement of the ice nucleation rate in micrometer-sized droplets at temperatures of 227-232 K on very short time scales using an X-ray laser technique. In summary, we present a new physically constrained param-eterization for homogeneous ice nucleation which is consistent with the latest literature nucleation data and our physical understanding of the properties of supercooled water. © 2016 Author(s). All article content, except where otherwise noted, is licensed under a Creative Commons Attribution (CC BY) license (http://creativecommons.org/licenses/by/4.0/). [http://dx.doi.org/10.1063/1.4962355]

## I. INTRODUCTION

The properties of supercooled water in the regime of homogeneous nucleation remain poorly defined and this limits our capacity to accurately describe the rate of homogeneous nucleation of ice.${}^{1}$ Knowledge of ice nucleation kinetics is perhaps most important for the accurate description of ice particle formation in clouds arising in Earth's atmosphere. Clouds are sometimes observed to supercool to temperatures approaching and even below 238 K,${}^{2-6}$ a temperature range where homogeneous ice nucleation becomes increasingly probable. For example, a $\sim 10$ $\mu$m droplet nucleates with a half-life of hours at 238 K, and only seconds at $\sim 235$ K. Therefore, this latter temperature of 235 K is often termed the "homogeneous ice nucleation limit." However, this limit is only a practical definition and not a strict physical limit, as recent measurements of micrometer-sized droplets below 232 K clearly demonstrate.${}^{7}$ Therefore, we denote the temperature range of about 233-238 K, where most standard techniques assess homogeneous ice nucleation, as the "homogeneous nucleation regime."

In the past, it was common to represent homogeneous ice nucleation in atmospheric cloud models with a threshold function at which all droplets froze at either 233 K or 235 K ($-40\ {^\circ}\text{C}$ or $-38\ {^\circ}\text{C}$, respectively), but in a recent study, it was shown that it is very important to represent the temperature dependence of homogeneous nucleation correctly and that homogeneous nucleation starts to strongly influence a cloud at temperatures as high as about 240 K,${}^{8}$ a result that is supported by a recent theoretical analysis using a freezing-relaxation concept.${}^{9}$ At present, there is a considerable divergence of parameterizations for homogeneous nucleation which produce significant differences in cloud models,${}^{1,8}$ hence there is a clear need for an improved description of this critical and atmospherically highly relevant process.

Supercooled water is a notoriously complex liquid and has been the subject of intense discussion and debate for

${}^{a)}$Authors to whom correspondence should be addressed. Electronic addresses: thomas.koop@uni-bielefeld.de and b.j.murray@leeds.ac.uk

![](./images/811141805910261761_1.jpg)

many decades. $^{10-12}$ One of the anomalous characteristics of water is that thermodynamic variables such as heat capacity and compressibility vary strongly with decreasing temperature through the region relevant for homogeneous nucleation. This observation led Speedy and Angell$^{13}$ to propose, in 1976, that a singularity may exist in supercooled water at around 228 K, originating from a stability limit below which liquid water cannot exist. More recent studies, however, support pronounced but continuous changes in water's thermodynamic properties at ambient pressure. $^{12,14}$ It is proposed that the observed changes coincide with a fragile-to-strong transition of the liquid, which may occur in a region somewhere below the homogeneous nucleation regime and above the glass transition temperature of 136 K. $^{15,16}$ Whether or not this behavior originates from the proposed but controversially discussed occurrence of a second (liquid-liquid) critical point of water at low temperature and elevated pressure (~220-225 K, ~500 bars),$^{17-20}$ however, does not greatly influence a physical description of homogeneous ice nucleation at atmospheric pressure.

Recent experimental work shows that the structure of water also changes dramatically through the region of homogeneous nucleation which may be the underlying cause for the observed rapidly changing thermodynamic variables. Sellberg $et$ $al.^{21}$ used a fast free-electron X-ray laser technique to study the structure of water at the 100 fs time scale in micrometer-sized droplets down to about 227 K and found that the molecular nearest-neighbor coordination of water molecules increases sharply. These observations confirmed similar computational findings that there is a sharp increase in the fraction of four-coordinate water molecules in the homogeneous nucleation regime. $^{22}$ Moore and Molinero$^{22}$ suggest that this dramatic change in water structure controls the homogeneous nucleation of ice. It is also known that various dynamical properties, such as viscosity,$^{23,24}$ self-diffusion,$^{25}$ and dielectric relaxation times,$^{16,26}$ vary strongly through the region of homogeneous nucleation. It is striking that water's thermodynamic, structural, and dynamic properties all vary extremely strongly in the temperature and pressure regime of direct relevance for supercooled clouds in Earth's atmosphere. Hence, the complexity of supercooled water is key to defining and describing the rate at which ice nucleates in supercooled water, and thus, an accurate parameterization of atmospheric ice formation in liquid water clouds.

In this paper, we have developed a new parameterization for homogeneous ice nucleation which is based on classical nucleation theory (CNT), but where many of the variables within this theory are constrained using an up-to-date understanding of the behavior of physical properties of supercooled water. The new CNT formulation is then fitted to a selection of the available literature data of homogeneous ice nucleation to produce a new parameterization, which has some key differences from those previously published, particularly at low temperatures. The rate of nucleation in CNT is very sensitive to the value of various physical parameters and their temperature dependence, namely, the saturation ratio of the nucleating phase, the diffusion activation energy, and the interfacial energy between the nucleating phase and its mother phase (here, ice and supercooled water, respectively), most of which are not known accurately within the homogeneous nucleation regime. This makes it very difficult to predict ice nucleation rates from first principles. On the other hand, CNT allows for a very flexible but not necessarily unique fitting of the above terms to measured nucleation data. Thus, obtaining these terms from CNT fits to nucleation data is often ambiguous. Here, we follow a different approach by constraining the different terms and/or their temperature dependence in the supercooled range as much as possible with available physical data and current understanding of the behavior of supercooled water's properties, with only one single free parameter: the value of the interfacial energy at one fixed temperature.

## II. DEVELOPMENT OF THE PARAMETERIZATION

### A. Classical nucleation theory

Classical nucleation theory has been widely used to describe nucleation of ice in supercooled water and the rate of nucleation can be expressed as$^{1,27,28}$

$$
J(T)=\frac{k T}{h} n_{l} \exp ^{-\frac{\Delta G_{\mathrm{diff}}(T)}{k T}} \exp ^{-\frac{\Delta G_{\mathrm{crit}}(T)}{k T}},\qquad(1)
$$

where $T$ is absolute temperature, $k$ is the Boltzmann constant, $h$ is the Plank constant, and $n_{l}$ is the volume number density of water molecules in liquid water (derived from the density of water, $\rho_{l}$, multiplied by $N_{\mathrm{A}} / M\left(\mathrm{H}_{2} \mathrm{O}\right)$, i.e., the Avogadro constant divided by the molar mass of water, see Tables I and II). $\Delta G_{\mathrm{diff}}(T)$ is the diffusion activation free energy, which approximates the activation energy associated with the unfavorable bond orientation as a molecule adds to a cluster,$^{28}$ and $\Delta G_{\mathrm{crit}}(T)$ is the free energy barrier associated with the formation of a critical ice cluster. According to CNT, $\Delta G_{\mathrm{crit}}(T)$ is given by$^{1,28}$

$$
\Delta G_{\mathrm{crit}}(T)=\frac{16 \pi v_{i}^{2}(T) \sigma_{i, l}^{3}(T)}{3[k T \ln S(T)]^{2}},\qquad(2)
$$

<table>
<caption>TABLE I. Parameterizations for density and vapor pressure of ice and of liquid water. These parameterizations are valid for temperature $T$ given in K.</caption>
<thead>
<tr>
<th>Quantity</th>
<th>Parameterization</th>
<th>Reference</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\rho_{l}$ in g cm$^{-3}$</td>
<td>0.965$^{\mathrm{a}}$</td>
<td></td>
</tr>
<tr>
<td>$\rho_{i}$ in g cm$^{-3}$</td>
<td>$-1.3103×10^{-9}T^{3}+3.8109×10^{-7}T^{2}$</td>
<td>89</td>
</tr>
<tr>
<td></td>
<td>$-9.2592×10^{-5}T+0.94040$</td>
<td></td>
</tr>
<tr>
<td>$\ln(P_{l}$ in Pa)</td>
<td>$54.842763-6763.22/T-4.210\ln(T)$</td>
<td>29</td>
</tr>
<tr>
<td></td>
<td>$+0.000367T+\tanh[0.0415(T$</td>
<td></td>
</tr>
<tr>
<td></td>
<td>$-218.8)](53.878-1331.22/T$</td>
<td></td>
</tr>
<tr>
<td></td>
<td>$-9.44523\ln(T)+0.014025T)$</td>
<td></td>
</tr>
<tr>
<td>$\ln(P_{h}$ in Pa)</td>
<td>$9.550426-5723.265/T+3.53068\ln(T)$</td>
<td>29</td>
</tr>
<tr>
<td></td>
<td>$-0.00728332T$</td>
<td></td>
</tr>
</tbody>
</table>

$^{\mathrm{a}}$Note that the value of $\rho_{l}$ is required for calculating $n_{l}$. Since $\rho_{l}$ varies only by less than a few percent in the supercooled temperature range, we set it to a fixed value which approximately corresponds to that of available data extrapolated to the homogeneous nucleation regime. As $n_{l}$ enters only linearly in the prefactor of $J_{hom}$ in Eq. (1), the resulting error in $J_{hom}$ is negligible.

<table><caption>TABLE II. Physical constants and parameters used.</caption>
<tbody>
<tr>
<td>Parameter</td>
<td>Value</td>
<td>Description</td>
</tr>
<tr>
<td>$T_m$</td>
<td>273.15 K</td>
<td>Melting temperature of hexagonal ice
at standard pressure</td>
</tr>
<tr>
<td>$k$</td>
<td>$1.380\ 648×10^{-23}$ J K$^{-1}$</td>
<td>Boltzmann constant</td>
</tr>
<tr>
<td>$h$</td>
<td>$6.626\ 070×10^{-34}$ J s</td>
<td>Planck constant</td>
</tr>
<tr>
<td>$N_A$</td>
<td>$6.022\ 14×10^{23}$ mol$^{-1}$</td>
<td>Avogadro constant</td>
</tr>
<tr>
<td>$M(\text{H}_2\text{O})$</td>
<td>$18.014\ 8$ g mol$^{-1}$</td>
<td>Molar mass of water</td>
</tr>
<tr>
<td>$\Delta H_{sd,h}$</td>
<td>$0.155$ kJ mol$^{-1}$</td>
<td>Enthalpy difference between stacking
disordered and hexagonal ice,
see Eq. (A2)</td>
</tr>
<tr>
<td>$T_r$</td>
<td>236.0 K</td>
<td>Reference temperature for fitting
interfacial energy</td>
</tr>
</tbody>
</table>

where $v_i$ is the volume of a water molecule in ice, which is derived from dividing the term $M(\text{H}_2\text{O})/N_A$ by the density of crystalline ice $\rho_i$ (given in Table I), $\sigma_{i,1}$ is the interfacial energy between liquid water and ice, and $S$ is the saturation ratio with respect to the nucleating phase, i.e., ice.

### B. Saturation ratio

The value of $S$ is related to the difference of the chemical potentials of water and ice and can be represented by the ratio of the vapor pressures of supercooled water $(P_l)$ and of ice, $^{29}$ see Table I. In this study, we assume that the metastable stacking-disordered phase of ice initially nucleates, which is consistent with computational simulations of ice nucleation $^{30–35}$ as well as diffraction studies of frozen droplets. $^{33,34}$ As a metastable phase, stacking-disordered ice (ice $\text{I}_{sd}$) has an equilibrium vapor pressure $(P_{sd})$ larger than that of hexagonal ice $(P_h)$. It has been shown that this metastable phase has an enthalpy which is about $155 \pm 30$ J mol$^{-1}$ larger than that of ice $\text{I}_h$, $^{36}$ a value consistent with the range defined by calorimetry data. Assuming that the entropy difference is negligible, $^{29}$ we can say that this enthalpy difference is equal to the change in free energy associated with the hexagonal ice (ice $\text{I}_h$) to stacking-disordered ice (ice $\text{I}_{sd}$) transition ($\Delta G_{\text{h}\rightarrow\text{sd}}$). This difference in free energy is directly related to the ratio of the vapor pressures of the two phases, i.e., $\Delta G_{\text{h}\rightarrow\text{sd}} = RT\ln(P_{sd}/P_h)$, resulting in the following formulation for $S$:

$$
S = \frac{P_l}{P_{sd}} = \frac{P_l}{P_h \exp(\Delta G_{\text{h}\rightarrow\text{sd}}/RT)}. \tag{3}
$$

### C. Diffusion activation energy

The diffusion-activation energy, $\Delta G_{\text{diff}}$, can be related to the translational self-diffusion coefficient of water $D(T)$ as follows:$^{27,28}$

$$
\Delta G_{\text{diff}}(T) = \frac{\partial \ln D(T)}{\partial T} kT^2. \tag{4}
$$

Measurements show that the rate of self-diffusion of water molecules in liquid water decreases rapidly with decreasing temperature. $^{25,37–41}$ This means that water molecules add to ice clusters less readily at lower temperatures, which increases $\Delta G_{\text{diff}}$ in Eq. (1), and has the effect of slowing the rate of nucleation. The strong dependence of $D$ with temperature implies that it is a key parameter to treat accurately in a parameterization of the nucleation rate. The selection of the available literature data for $D(T)$ is shown in Figure 1 together with fits both from the literature and the present study. Dynamic properties of water are commonly represented by a power-law (PL) or a Vogel–Fulcher–Tammann (VFT) style fit. $^{38,42}$ The PL relationship ($D = D^*T^{0.5}(T/T_s - 1)^\gamma$, where $T_s$, $\gamma$, and $D^*$ are fitted parameters) defines a curve where $D$ decreases asymptotically to negative infinity as $T$ decreases towards a singularity temperature $T_s$, see discussion above. The VFT relationship ($D = D_o\text{exp}(-B/T - T_o)$, where $D_o$, $B$, and $T_o$ are fitted parameters) is commonly applied to the temperature dependence of transport properties of fragile liquids. $^{43,44}$

![](./images/811141805910261761_2.jpg)

FIG. 1. Translational self-diffusion coefficient of $\text{H}_2\text{O}$ in liquid water. The data (black circles) are taken from the literature. $^{25,38–41}$ The fits from Smith and Kay, $^{42}$ Prielmeier <i>et al.</i>, $^{39}$ Dehaoui <i>et al.</i>, $^{23}$ and Laksmono <i>et al.</i>$^7$ are shown in addition to the PL and VFT fits derived in this study (red and green line, respectively). (a) Diffusion coefficients over a broad temperature range are shown, whereas (b) is focused on the supercooled regime and additionally shows confidence limits to our PL fit.

The PL fit from Smith and Kay $^{42}$ underestimates the latest $D$ values below about 255 K and their VFT fit underpredicts

$D$ between 260 and 300 K; the discrepancy is because they fitted their parameterization to an older data set from Gillen et al., $^{37}$ whereas we use more recent data of Price et al. $^{25}$ together with those of Prielmeier et al. $^{38,39}$ and others $^{40,41}$ in this regime. In order to better represent the latest literature data, we have re-fitted a PL and VFT equation to the $D(T)$ data below 318.15 K and the results are shown in Figure 1. Both fits represent the bulk of the data well, but the PL equation fits the strong downturn in $D$ below about 240 K much better. We also note that our PL fit is consistent with the parameterization of $D(T)$ recently presented by Dehaoui et al., $^{23}$ see Figure 1(b). The difference in the various fits implies that extrapolation to temperatures where most homogeneous nucleation experiments have been performed leads to significant deviations in both the absolute value of $D$, and more importantly for $\Delta G_{\text{diff}}$, its temperature dependence.

Many thermodynamic and dynamic properties of water are well approximated by a power law in the region of homogeneous nucleation. For example, Dehaoui et al. $^{23}$ recently demonstrated that their measurements of viscosity down to temperatures of 239 K were best represented by a PL. Similarly to our fits to diffusion data in Figure 1, Dehaoui et al. $^{23}$ found that a power law fit to their viscosity data was superior to those following simple Arrhenius, parabolic, or VFT behavior as the temperature approaches the homogeneous nucleation regime. As discussed in the Introduction, the rapid change in transport properties is echoed by rapidly changing thermodynamic variables in the same regime. In fact, other thermodynamic properties can also be well approximated by a PL in the region of homogeneous nucleation. $^{13,22,45}$ At lower temperatures, in so-called no-man's land where crystallization is inevitable, it is suggested that water may undergo a fragile-to-strong transition where the temperature dependence of dynamic properties switches from a strong non-Arrhenius relationship to one close to an Arrhenius relationship. Mattsson et al. $^{26}$ illustrate such a fragile-to-strong transition also in a range of other H-bonding systems analogous to water, which are not prone to crystallization. Above a threshold temperature, they suggest that their dielectric structural relaxation times are well-represented by a power law and below the threshold the temperature dependence clearly changes to a behavior closer to Arrhenius. Furthermore, by extrapolating their results to the case of water, they suggest that the dynamic crossover point is around 220 K, which is consistent with the proposed fragile-to-strong transition suggested elsewhere $^{15}$ and also inferred from studies of water in confinement such as in porous materials. $^{16}$

Generally, a power law implies the existence of a critical temperature (here $T_{\text{s}}$) at which the parameterized property (here $D$) diverges. The proposed liquid-liquid critical point (LLCP) of water $^{17,18}$ may be the physical cause of such a divergence. However, most models predict the existence of a LLCP at higher pressure, and thus, suggest a thermodynamic continuity of water at ambient pressure to very low temperature. Yet, a so-called Widom line emanates from the LLCP towards ambient pressure, $^{46,47}$ which connects the points of maxima with respect to temperature of a thermodynamic or dynamic property of water. Hence, in such a scenario, ambient properties of water may not diverge at $T_{\text{s}}$ but may approach a finite maximum near $T_{\text{s}}$. Therefore, the PL equation for $D$ does not imply a strict power-law dependence all the way down to $T_{\text{s}}$ but rather an apparent power-law behavior. As such it is well suited to describe $D$ over a wider temperature range, but it becomes invalid in close proximity to the apparent divergence temperature $T_{\text{s}}$, which is $\sim$213 K in our case. We note that $T_{\text{s}}$ may indicate the approximate location of the strong-to-fragile transition discussed above.

Overall, the available data and fundamental understanding of water may suggest that there is a transition from a fragile to a strong liquid somewhere below the homogeneous nucleation regime, but through the homogeneous nucleation regime, an apparent power lower law is probably the most physically consistent means of approximating the temperature dependence of water's self-diffusion coefficient. In the following, we use both VFT and PL fits, but as will be seen, the PL fits tend to produce nucleation rates which are more consistent with the available data.

### D. Interfacial energy

There exist several measurements of the equilibrium ice-liquid interfacial energy $\sigma_{\text{i,l}}$ at the melting temperature of hexagonal ice, at 273.15 K (see, e.g., Ref. 1). However, in the supercooled range, $\sigma_{\text{i,l}}$ cannot be measured directly in laboratory experiments, and hence, it is often estimated theoretically or obtained indirectly by fitting CNT to nucleation data. In order to derive the temperature dependence of the interfacial energy between the ice embryo and supercooled water, we make use of the Turnbull correlation. $^{48}$ The Turnbull correlation relates the interfacial energy of a solid in its melt in the homogeneous nucleation regime to the change in enthalpy of the phase change $\Delta H_{\text{m}}$ at the equilibrium melting temperature, $^{48}$ $\sigma_{\text{s,l}}(T_{\text{hom}}) \propto \Delta H_{m}(T_{m})$, and has sometimes been applied for deriving $\sigma_{\text{i,l}}$ in ice nucleation studies, e.g., Refs. 28, 49, and 50, see detailed discussion in Ickes et al. $^{1}$ This relationship was originally derived for describing homogeneous nucleation of various metals from their melts, but it was shown to also work for alkali halides. $^{51}$ More recently, in a computational study of water and ice confined in nanopores, the Turnbull correlation was found to be consistent also in the supercooled range of water, revealing the same temperature dependence of $\sigma_{i,l}(T)$ and $\Delta H_{m}(T)$, i.e., $\sigma_{i,l}(T)/\Delta H_{m}(T) \approx \text{const}.^{52}$ The more alike the liquid and solid phases are, the smaller the enthalpy of the phase change and the smaller the interfacial energy. Hence, in this study, we approximate the temperature dependence of $\sigma_{i,l}(T)$ by scaling its value to the temperature dependence of the enthalpy of melting of ice, $\Delta H_{m}(T)$, an approach already employed by McDonald for describing homogeneous ice nucleation, albeit with outdated data. $^{53}$ Here, we determine $\Delta H_{m}(T)$ from fits to calorimetry data of the isobaric heat capacity $C_{p}(T)$ of ice and supercooled water. $^{29}$ While the heat capacity of hexagonal ice $I_{\text{h}}$ has been measured over a wide temperature range, there are no data for the heat capacity of supercooled bulk or emulsified water below about 236 K. We have used the parameterization of the heat capacity from Murphy and Koop $^{29}$ together with their estimated upper and

lower limits. The resulting values of the enthalpy of melting $\Delta H_{m,h}(T)$ for hexagonal ice are shown as the solid blue line in Figure 2(a) together with the lower and upper bounds (dotted blue lines; note that an upper limit in $C_p$ leads to a lower limit in $\Delta H_{m,h}$ and vice versa). The observed behavior is consistent with earlier analyses of $\Delta H_{m,h}(T)$ in the supercooled range, $^{13,54}$ as well as with more recent theoretical models of water. $^{14,55}$ Moreover, we can approximate the enthalpy of melting for stacking-disordered ice $\Delta H_{m,sd}(T)$ by subtracting $0.155\ \text{kJ mol}^{-1}$, see above in Section II B, resulting in the red lines in Figure 2(a). The interfacial energy between stacking-disordered ice and supercooled water $\sigma_{sd,l}(T)$ is then related to $\Delta H_{m,sd}(T)$ through the following expression based on Turnbull's correlation: $^{52}$

$$
\sigma_{sd,l}(T)=\Delta H_{m,sd}(T)\times\frac{\sigma_{sd,l}(T_{r})}{\Delta H_{m,sd}(T_{r})}, \tag{5}
$$

where the subscript "r" indicates a reference temperature which we define as $T_r=236$ K, i.e., in the heart of the homogeneous nucleation regime. The absolute value of $\sigma_{sd,l}(T_r)$ is treated as the only adjustable parameter in our CNT analysis, while the temperature dependence of $\sigma_{sd,l}(T)$ is constrained to that of $\Delta H_{m,sd}(T)$.

![](./images/811141805910261761_3.jpg)

FIG. 2. Melting enthalpies and derived interfacial energies used in the present CNT parameterization. (a) The enthalpy of melting ($\Delta H_m$) of ice $\text{I}_h$ and ice $\text{I}_{sd}$ (solid lines). The value for ice $\text{I}_h$ was determined from the heat capacity of ice and supercooled water $^{29}$ and that for ice $\text{I}_{sd}$ was derived assuming a constant enthalpy difference between ice $\text{I}_h$ and ice $\text{I}_{sd}$ of $0.155\ \text{kJ mol}^{-1}.^{36}$ The uncertainty in $\Delta H_m$ (dotted lines) was determined from the uncertainty in the heat capacity of liquid water. $^{29}$ The nominal $\Delta H_m$ and upper and lower limits are parameterized by polynomials in Eq. (A1) with details given in Table III. The solid circles represent the values at the melting temperature of ice $\text{I}_h$ at 273.15 K and that of ice $\text{I}_{sd}$ calculated here as 265.94 K, respectively. (b) The solid-liquid interfacial energy derived for stacking-disordered ice, $\sigma_{sd,l}(T)$. The temperature dependence of $\sigma_{sd,l}$ is derived using the relationship in Eq. (5), whereas the $\sigma_{sd,l}(T_r)$ at the reference temperature ($T_r=236$ K) is fitted to the experimental data, see text for details. Also shown are various literature parameterizations $^{7,71,72,86}$ of $\sigma_{sd,l}(T)$, originally referred to as that of cubic ice in these papers (see text for details), using a different temperature dependence of $\sigma_{sd,l}(T)=\sigma_{sd,l}(T_0)\times(T/T_0)^n$ with $T_0=235.8$ K and $n$ as given in the annotation.

### III. FITTING THE CNT-BASED MODEL TO EXPERIMENTAL DATA

The available experimental data for the rates of homogeneous nucleation $J_{\text{hom}}$ were recently reviewed in the literature. $^{1,56}$ In this study, we have selected a subset $^{56-68}$ of the available data sets for the purposes of constraining the new parameterization. The criteria for selection were (i) minimal and well defined uncertainties, (ii) good reproducibility within the data set, and (iii) an internal droplet pressure of about 1 bar. These criteria ruled out much of the literature data from the last millennium where uncertainties, such as temperature offsets, were not clear. The data from Wood et al. $^{69}$ are not included because of the large spread in nucleation rates over three orders of magnitude at one temperature. Data from nanometer-sized droplets are not included because the internal Laplace pressure of several hundred bar places these droplets in a regime where thermodynamic and dynamic properties are very different. $^{55}$ Also, we do not include in the fitting procedure the very recent data of Laksmono et al. $^{7}$ in micrometer-sized droplets as cold as 227 K since the temperature uncertainties of these data are more than a degree. Note that it has been pointed out that temperature accuracy is likely the single-most important cause for uncertainty in measured ice nucleation rates. $^{56}$ Even with only the data sets which fit these criteria selected, shown in Figure 3, the possible values of $J_{\text{hom}}$ are spread over two orders of magnitude (or 2 K), but this is significantly less spread than represented by the full literature review conducted by Ickes et al., $^{1}$ where the spread in $J_{\text{hom}}$ at 236 K is more than five orders of magnitude.

In order to fit the CNT-based parameterization for each of the four parameterizations of $D(T)$, we have used a least-square fitting routine where the only adjustable parameter is $\sigma_{sd,l}(T_r)$, as discussed above. Each $J_{\text{hom}}$ data set was weighted equally by representing it with three data points, at the maximum, minimum, and average temperature, determined from a straight line fit to $\ln(J_{\text{hom}})$ versus $T$. In addition, we grouped measurements from separate papers, but made with the same instrument and methodology, into single data sets (i.e., we grouped data from Duft and Leisner $^{58}$ with Rzesanke et al., $^{59}$ Stöckel et al. $^{61}$ with Kabath et al., $^{62}$ as well as Hoyle et al. $^{64}$ with Lüönd et al. $^{65}$). The resulting CNT

![](./images/811141805910261761_4.jpg)

FIG. 3. Fitted ice nucleation rate $J_{\text{hom}}$ parameterizations compared to the selected literature data. The fits to the literature data are shown using the four different parameterizations of $D(T)$ shown in Figure 1(a). Only the selected literature data above $233\ \text{K}^{56-68}$ were used in the fitting procedure (grey symbols), but the data from Laksmono $et\ al.^{7}$ are also shown for comparison (open circles). In order to give each data set equal weight, each data set was represented by three points (not shown for clarity), see text for details. The upper and lower limits (dotted and dashed red lines) to the $J_{\text{hom}}(T)$ curve (solid red line) corresponding to our power law fit $D(T)$ are also shown. The dotted lines indicate the uncertainty due to the 95.4% confidence interval of our fit to $D(T)$ and the dashed lines correspond to the uncertainty related to uncertainty in $\sigma_{s,d,l}(T)$ derived from the upper and lower limits in the heat capacity of supercooled water.

fits are shown in Figure 3, with different lines originating from employing different parameterizations of $D(T)$. It is clear that using the PL parameterization of $D(T)$ by Smith and $Kay^{42}$ produces a very poor fit to the data (blue line in Figure 3). This is perhaps not unexpected since $D(T)$ is a poor fit to the low temperature diffusion data in Figure 1, but the degree to which the fitted nucleation rates deviate from the experimental values is quite striking. This illustrates how critical the choice of $D(T)$ parameterization is for nucleation rates. The CNT $J_{\text{hom}}$ curves for the two VFT parameterizations (yellow and green lines) and our PL fit are all reasonable fits to the experimental data. However, the PL based fit provides a better overall fit to the data in the homogeneous nucleation regime (~233-238 K), as it results in the smallest sum of squared residuals when compared to the other three fits. While we did not include the low-temperature nucleation data of Laksmono $et\ al.^{7}$ in any of our CNT fitting procedures (see above), it does help to constrain which diffusion parameterization results in the best fit of the nucleation rate. The two VFT fits clearly overpredict $J_{\text{hom}}$ at temperatures below 232 K by as much as seven orders of magnitude at 227 K. In contrast, our PL fit to $D(T)$ produces values of $J_{\text{hom}}$ which are within our and their estimated uncertainty limits. This may imply that the PL fit to the diffusion data produces a more realistic temperature dependence of the diffusion activation energy in the temperature range between about 227 and 238 K than does the VFT fit. This is consistent with the discussion above on the fact that apparent PL fits tend to reproduce various thermodynamic and dynamic properties of water in the homogeneous nucleation regime. We note that if the apparent PL function levels off at some temperature above $T_s$, then $J_{\text{hom}}$ may decrease less strongly at low temperature than shown in Fig. 3.

We further note that our new parameterization is not consistent with the $J_{\text{hom}}$ values, of $\sim10^{23}$-$10^{25}\ \text{cm}^{-3}\ \text{s}^{-1}$ between 193 and 215 K, determined from the freezing of nanometer-sized droplets. $^{70,71}$ Due to the Laplace pressure, the internal pressure in nanometer-droplets is several orders greater than in a micrometer-droplet (where the Laplace pressure is very small). Thermodynamic as well as dynamic properties such as the self-diffusion coefficient are known to be pressure dependent, $^{38,55}$ hence the rate of nucleation in these droplets is most likely also very different to droplets at $\sim1$ bar. Moreover, it is not clear whether ice nucleation in nanometer-sized droplets may be driven by a surface-dependent nucleation process rather than the volume-dependent process in micrometer and super-micrometer droplets investigated here. $^{7,58}$ Nevertheless, several authors have attempted to link the low temperature nanometer-droplet data with higher temperature micrometer-droplet data, $^{1,70-74}$ but as Laksmono $et\ al.^{7}$ already pointed out this should probably not be done for the reasons given above. In a previous study, $^{75}$ the internal droplet pressure has been considered by including a pressure-dependent interface energy term, leading to a reduction in $J_{\text{hom}}$ by about 2-3 orders of magnitude at 200-210 K and implying $J_{\text{hom}}$ values at ambient pressure that are even larger than those measured in nanometer droplets. In addition, Laksmono $et\ al.^{7}$ argue that there is a “hard limit” for the maximum in $J_{\text{hom}}$ anywhere in the supercooled temperature region of $J_{\text{hom}}^{\text{max}} \leq 10^{16}\ \text{cm}^{-3}\ \text{s}^{-1}$, which is set by the fact that previous experiments had shown that micrometer droplets vitrify at cooling rates of $10^{7}\ \text{K}\ \text{s}^{-1}.^{76,77}$ Our new parameterization suggests a maximum nucleation rate of about $J_{\text{hom}}^{\text{max}} \approx 2 \times 10^{12} \pm 10^{2}\ \text{cm}^{-3}\ \text{s}^{-1}$ at about 229 K, which is consistent with this notion. Similarly, previous experiments had shown that micrometer droplets nucleate ice at cooling rates of about $10^{4}\ \text{K}\ \text{s}^{-1}$, implying a minimal value of approximately $J_{\text{hom}}^{\text{min}} \approx 10^{13}\ \text{cm}^{-3}\ \text{s}^{-1}$ somewhere in the supercooled temperature range, which is consistent with our maximum nucleation rate of about $J_{\text{hom}}^{\text{max}} \approx 2 \times 10^{12} \pm 10^{2}\ \text{cm}^{-3}\ \text{s}^{-1}$ at about 229 K. We further note that if the apparent power-law behavior of $D$ levels off at temperatures around 225 K to 230 K, the maximum in the nucleation rate may be shifted to lower temperatures and slightly higher $J_{\text{hom}}$ values.

We also estimate the uncertainties in our derived values of $J_{\text{hom}}$ based on uncertainties in diffusion and interfacial energy. The dashed red lines in Figure 3, resulting from the uncertainties in the temperature dependence of $\sigma_{s,d,l}(T)$ which in turn arise from uncertainties in $\Delta H_{m,sd}(T)$ (see Figure 2), vary by about one order of magnitude from our best estimate $J_{\text{hom}}$ (solid red line). The dotted red lines show the uncertainties in $J_{\text{hom}}$ arising from the $D(T)$ parameterization. These originate from the $2\sigma$ limits (95.4%) of our power law parameterization to the experimental $D(T)$ data. It is clear that the uncertainties in $\sigma_{s,d,l}(T)$ as well as in $D(T)$ limit

our ability to accurately predict $J_{\text{hom}}$ at low temperature, clearly underpinning the need for more and accurate data of $\sigma_{sd,l}$ and $D$ and in the supercooled temperature range.

The fitted value of interfacial energy ($\sigma_{sd,l}$) at 236 K, based on the power law fit to $D(T)$, is $18.5 \pm 0.3$ mJ m$^{-2}$ (where the uncertainty is derived from uncertainty in $D(T)$). As mentioned above, there are no direct experimental measurements of interfacial energy at supercooled temperatures with which to compare this value. However, this value falls within the range of values previously derived from nucleation experiments, most of which are between $\sim$12 and 25 mJ m$^{-2}$ (see the compilation of results in Figure 2 of Ickes *et al.*$^1$). The interfacial energy of hexagonal ice in equilibrium with water at the melting temperature of 273.15 K has been determined both experimentally and computationally. Extrapolating our $\sigma_{sd,l}(T)$ to 265.94 K (the predicted melting temperature of stacking-disordered ice) and 273.15 K on the basis of the Turnbull correlation in Eq. (5) yields values of $24.7 \pm 0.5$ mJ m$^{-2}$ and $25.9 \pm 0.5$ mJ m$^{-2}$, respectively. It is not obvious that we should compare these values for stacking-disordered ice to literature values of interfacial energy of hexagonal ice, but computational studies suggest there is only a small difference in interfacial energy between the different forms of ice I,$^{78,79}$ and that the basal face of hexagonal ice at equilibrium may be stacking disordered.$^{80}$ Hence, we cautiously compare our values of $\sigma_{sd,l}$ at the melting temperature with values determined for hexagonal ice also at the melting temperature. From experiments, there is a substantial spread of the reported interfacial energy at 273.15 K,$^1$ but it has been suggested that the value of Hardy$^{81}$ of $29.1 \pm 0.8$ mJ m$^{-2}$ may be the most reliable.$^{1,82}$ Studies with the TIP4P family of models yield values averaged across several faces ranging between $26.5 \pm 0.4$ to $29.8 \pm 0.8$ mJ m$^{-2}$,$^{80,82,83}$ whereas the mW model of water yields somewhat higher values of $35.5 \pm 2.5$ mJ m$^{-2}$.$^{84}$ Estimates of the interfacial energy based on the critical cluster size of hexagonal ice in TIP4P/2005 and TIP4P/ice water models yield an interfacial free energy of $29 \pm 3$ mJ m$^{-2}$.$^{85}$ Hence, our estimate of the interfacial energy at melting is at the low end of, but consistent with, the various predictions.

Repeating the fitting procedure, but where we assume the critical cluster has the thermodynamic properties of hexagonal ice rather than stacking-disordered ice yield a $\sigma_{h,l}$ at 236 K and 273.15 K of 21.9 mJ m$^{-2}$ and 30.7 mJ m$^{-2}$, respectively. This value is in better agreement with the experimentally derived value from Hardy$^{81}$ ($29.1 \pm 0.8$ mJ m$^{-2}$) but larger than the values derived from the TIP4P family of models. More importantly, we also note that the fitted slope of $J_{\text{hom}}$ versus $T$ is shallower than many of the experimental data sets when we assume hexagonal ice nucleates. This calculation suggests that a metastable stacking-disordered phase nucleates, but also that the parameterization of the nucleation rate and derived interfacial energy is sensitive to the choice of $\Delta H_{sd,h}$. We have chosen a value of 155 J mol$^{-1}$ based on vapour pressure measurements,$^{36}$ whereas stacking disorder is known to be highly variable and the ice made in those experiments may not have the same thermodynamic properties as the ice in a critical cluster.$^{34}$ In addition, it has been suggested that the energy cost of stacking disorder is minor and that defects in ice are responsible for much of the observed metastability.$^{79}$

The temperature dependence of the interfacial energy used in our CNT parameterization, shown in Figures 2(b), is substantially steeper than the majority of literature parameterizations summarized by Ickes *et al.*$^1$ In order to illustrate this point, we plot in Figure 2(b) a selection$^{7,71,72,86}$ of those literature parameterizations that refer to cubic ice. In the meantime it has become clear, that what used to be termed cubic ice, is now believed to have been stacking-disordered ice,$^{33,34,87}$ thus, they may be directly compared to our derivation of $\sigma_{sd,l}(T)$. The use of the Turnbull correlation, which produces a much stronger temperature dependence of $\sigma_{i,l}$, is consistent with Limmer and Chandler$^{52}$ who demonstrated the consistency of the Turnbull correlation in the mW water model.$^{52}$ In addition, Sanz *et al.*$^{85}$ reported a temperature dependence of $\sigma_{i,l}$ of $\sim$0.18 mJ m$^{-2}$ K$^{-1}$ for supercoolings between 14.5 and 34.5 K using TIP4P/2005 and TIP4P/ice water models. Over a similar supercooling range, the curve in Figure 2(b) has a slope of approximately 0.21 mJ m$^{-2}$ K$^{-1}$. Hence, computational studies with various models of water produce temperature dependencies of the interfacial energy, which are in far better agreement with our parameterisation than the parameterisations used previously in the literature to analyse experimental nucleation data.

## IV. SUMMARY AND CONCLUSIONS

We present a new parameterization for homogeneous nucleation of ice from supercooled water which is based on CNT where we have constrained key variables with available data for supercooled water. By constraining the ice-liquid interfacial energy and the self-diffusion coefficient of water in a physically realistic manner, we were able to reproduce the experimentally observed temperature trend of the rate of homogeneous ice nucleation at atmospheric pressure. While this parameterization is constrained to a selection of laboratory nucleation data between about 233 and 238 K, our parameterization also reproduces within uncertainties the more recent X-ray laser-derived data down to 227 K even though they were not included in the analysis.

The new parameterization is strikingly different at temperatures below $\sim$237 K when compared to commonly used literature parameterizations (see Figure 4). For example, Pruppacher$^{88}$ and Zobrist *et al.*$^{27}$ produce nucleation rates many orders of magnitude larger than the values observed by Laksmono *et al.*$^7$ and predicted by our parameterization below 237 K. In particular, Pruppacher$^{88}$ predicts that the increase in $J_{\text{hom}}$ with decreasing temperature accelerates below 231 K, whereas our parameterization predicts that the nucleation rate should start to decrease with decreasing temperature at around 229 K. The much smaller values of $J_{\text{hom}}$ predicted by our parameterization are a result of the strong decrease in translational self-diffusion predicted by the power law fit. We justify the use of a power law on the basis that many thermodynamic and transport properties of supercooled

![](./images/811141805910261761_5.jpg)

FIG. 4. The new CNT-based homogeneous ice nucleation rate parameterization $J_{\rm hom}(T)$ compared to other parameterizations $^{1,7,27,88}$ in the literature. While we provide all the individual terms and their parameters of our CNT-based parameterization for $J_{\rm hom}$ in Tables I–VI of the Appendix, it is sometimes necessary to use a more computationally cheaper, i.e., simpler, parameterization. Therefore, we have fitted our best estimate for $J_{\rm hom}$ by means of a 6th-order-polynomial for this purpose, see Table VII.

water are well defined by an apparent power law in the temperature range above homogeneous freezing and it is expected that diffusion will follow a similar law. Our fits to diffusion coefficients in Figure 1 clearly show that only the apparent power law can fit the downturn in diffusion at low temperatures, a similar conclusion to that of Dehaoui et al. $^{23}$ for both diffusion coefficients and viscosity. Nevertheless, a large source of uncertainty in the predicted values of $J_{\rm hom}$ arise from uncertainties in the extrapolated diffusion coefficients, and thus, measurements of diffusion in strongly supercooled water are highly desirable to further constrain the diffusion coefficient. On the other hand, the consistency we find between nucleation data at temperatures below 237 K and the use of the power law fit to $D(T)$ data suggests that diffusion does indeed follow an apparent power law through this temperature range.

The parameterization of $J_{\rm hom}$ given by Laksmono et al., $^{7}$ which was fitted to their own data at 227–232 K as well as data in the homogeneous nucleation regime at 233–238 K, is very similar to our new parameterization, but it is restricted to temperatures below about 238 K. $^{90}$ Hence, it is not applicable to the potentially very important atmospheric temperature range above 238 K, see below. Moreover, while the parameterization of Laksmono et al. $^{7}$ describes the data between 227 and 238 K very well, we believe our parameterization is based more soundly on the temperature dependence of the underlying physical properties of supercooled water. Laksmono et al. $^{7}$ used a simple literature parameterization for the interfacial energy that was originally derived by Huang and Bartell and meant to reproduce their nanometer-droplet nucleation data at very low temperature. That analysis resulted in a linear decrease in $\sigma_{sd,l}$ with decreasing temperature, whereas we relate the temperature dependence of $\sigma_{sd,l}$ to the difference in enthalpy between stacking-disordered ice and water, see Figure 2(b). Furthermore, Laksmono et al. $^{7}$ used a parameterization for $D(T)$ (see Figure 1(b)), which shows a much stronger decrease with decreasing temperature, although we note that they used a CNT model with a different formulation of the prefactor for their analysis, which may be the cause for the strong decrease in their $D(T)$.

Using a simple cloud model, Herbert et al. $^{8}$ tested the sensitivity of cloud glaciation to various parameterizations of homogeneous nucleation. They concluded that temperature dependence of the nucleation rate is very important. Unlike a simple offset in temperature, a change in temperature dependence does not have a simple linear effect upon cloud evolution. With a more shallow temperature dependence, the onset of ice nucleation is more gradual allowing more time for secondary processes, such as growth of crystals and depletion of supercooled water, to take place. Inspection of Figure 4 reveals that at temperatures above 235 K, where homogenous nucleation is most likely in the atmosphere, the temperature dependence of the parameterization of Zobrist et al. $^{27}$ is significantly steeper than that of the new parameterization. In fact, the slope of our new parameterization is very close to that of Pruppacher, $^{88}$ although Pruppacher's parameterization is shifted to warmer temperatures, and the "mixed-effect" CNT parameterization of Ickes et al., $^{1}$ which is shifted to slightly lower temperatures, with a shallower slope in the high-temperature range.

Herbert et al. $^{8}$ also noted that clouds begin to become sensitive to homogeneous nucleation at a rate $J_{\rm hom}$ of $1\ \rm cm^{-3}\ s^{-1}$, which corresponds to a temperature of about 240 K for our parameterization. In contrast, the experimental data we have chosen for this analysis are limited to $J_{\rm hom}$ values larger than $\sim10^{4}\ \rm cm^{-3}\ s^{-1}$ at temperatures mostly below 238 K. Clearly, there is a need to test our new parameterization for homogeneous nucleation at warmer temperatures for smaller values of $J_{\rm hom}$. However, since the temperature dependence of $D(T)$ and that of $\sigma_{sd,l}(T)$ (through its correlation with $\Delta H_{\rm m}$) is relatively well constrained at temperatures above $\sim$237 K, we are more confident in the behavior of our $J_{\rm hom}$ parameterization at higher temperature.

## ACKNOWLEDGMENTS

We thank Jamshed Anwar, Carsten Budke, David Chandler, Hans Peter Dette, Ross Herbert, Luisa Ickes, Hartawan Laksmono, Johan Mattsson, Valeria Molinero, Daniel Murphy, Anders Nilsson, and William Price for helpful comments and discussion or provision of experimental data. This research was supported by the European Research Council (Grant Nos. 240449 ICE and 648661 MarineIce), the Natural Environment Research Council (Grant Nos. NE/I013466/1 and NE/K004417/1), the Engineering and Physical Sciences Research Council (Grant No. EP/M003027/1), and the DFG research unit FOR-1525 (INUIT) under Grant Nos. KO 2944/2-1 and KO 2944/2-2, as well as support from the Institute for Climate and Atmospheric Science during the visit of T.K. to the University of Leeds.

## APPENDIX: DETAILED PARAMETERIZATION

The temperature-dependent enthalpy of melting of hexagonal ice with respect to water $\Delta H_{m,h}(T)$ is parameterized as follows:

$$
\Delta H_{m,h}(T) = \sum_{i} k_{i} \cdot (T-T_{m})^{i}, \tag{A1}
$$

where $T$ is the temperature in K, and $\Delta H_{m,h}$ is given in kJ mol⁻¹. The fitting parameters $k_i$ and $i$ are given in Table III. Their number $i$ was chosen such that the maximum deviation between the fit and the exact parameterization is about 0.01 kJ mol⁻¹ in the temperature range of validity of 225–273.15 K.

The temperature-dependent enthalpy of melting of stacking-disordered ice with respect to water $\Delta H_{m,sd}(T)$ then follows:

$$
\Delta H_{m,sd}(T) = \Delta H_{m,h}(T) - \Delta H_{sd,h}, \tag{A2}
$$

where $\Delta H_{sd,h}$ is a constant, see Table II.

The temperature-dependent interfacial energy between stacking-disordered ice and water $\sigma_{sd,l}(T)$ is parameterized according to the Turnbull correlation using the fitted values of $\Delta H_{m,sd}$ and $\sigma_{sd,l}$ at a reference temperature $T_r=236.0$ K by

$$
\sigma_{sd,l}(T) = \frac{\Delta H_{m,sd}(T)}{\Delta H_{m,sd}(T_r)} \sigma_{sd,l}(T_r). \tag{A3}
$$

The corresponding values are given in Table IV.

The parameters for the temperature-dependent diffusion activation energy $\Delta G_{\text{diff}}(T)$ were obtained by fitting experimental data of the translational self-diffusion coefficient of water $D(T)$ in the stable and supercooled liquid. $D(T)$ was parameterized by a power-law³⁸

$$
D(T) = D^{*} \cdot T^{0.5} \cdot \left( \frac{T}{T_s} - 1 \right)^{\gamma}. \tag{A4}
$$

The parameters from fitting the experimental $D(T)$ data in units of cm² s⁻¹ are given in Table V.

The following derivative with respect to temperature can be used to obtain $\Delta G_{\text{diff}}(T)$ from $D(T)$:

$$
\Delta G_{\text{diff}}(T) = \frac{\partial \ln D(T)}{\partial T} kT^{2}. \tag{A5}
$$

Applying this derivative to the power law in Eq. (A4) above then yields the following term for the diffusion activation energy, with parameters given in Table V:

$$
\Delta G_{\text{diff,PL}}(T) = \frac{kT}{2} + \frac{\gamma kT^{2}}{T-T_s}. \tag{A6}
$$

This parameterization was used for our best estimate of $J_{\text{hom}}(T)$.

Alternatively, $D(T)$ can be parameterized by the Vogel–Fulcher–Tammann (VFT) law

$$
D(T) = D_0 \cdot \exp \left( \frac{-B}{T-T_0} \right). \tag{A7}
$$

The parameters from fitting the experimental $D(T)$ data in units of cm² s⁻¹ are given in Table VI.

Applying the derivative of Eq. (A5) to the VFT Eq. (A7) above then yields the following term for the diffusion

---

<table>
<caption>Table III. Parameters for calculating $\Delta H_{m,h}(T)$ according to Eq. (A1).</caption>
<thead>
<tr>
<th></th>
<th>Best estimate</th>
<th>Lower limit</th>
<th>Upper limit</th>
</tr>
<tr>
<th>$i$</th>
<th>$k_i$</th>
<th>$k_i$</th>
<th>$k_i$</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td>6.008</td>
<td>6.008</td>
<td>6.008</td>
</tr>
<tr>
<td>1</td>
<td>0.036 16</td>
<td>0.039 035</td>
<td>0.039 178</td>
</tr>
<tr>
<td>2</td>
<td>$-3.947\;9\times10^{-4}$</td>
<td>$1.585\;8\times10^{-4}$</td>
<td>$4.297\;1\times10^{-4}$</td>
</tr>
<tr>
<td>3</td>
<td>$-1.624\;8\times10^{-5}$</td>
<td>$2.422\;1\times10^{-5}$</td>
<td>$6.666\times10^{-5}$</td>
</tr>
<tr>
<td>4</td>
<td>$-3.256\;3\times10^{-7}$</td>
<td>$8.226\;6\times10^{-7}$</td>
<td>$3.668\;2\times10^{-6}$</td>
</tr>
<tr>
<td>5</td>
<td>0</td>
<td>$1.218\;7\times10^{-8}$</td>
<td>$9.310\;5\times10^{-8}$</td>
</tr>
<tr>
<td>6</td>
<td>0</td>
<td>0</td>
<td>$8.392\times10^{-10}$</td>
</tr>
</tbody>
</table>

---

<table>
<caption>Table IV. Parameters for calculating $\sigma_{sd,l}(T)$ according to Eq. (A3).</caption>
<thead>
<tr>
<th></th>
<th>$\Delta H_{m,sd}(T_r)$ in kJ mol⁻¹</th>
<th>$\sigma_{sd,l}(T_r)$ in mJ m⁻²</th>
</tr>
</thead>
<tbody>
<tr>
<td>Best estimate</td>
<td>4.1776</td>
<td>18.505</td>
</tr>
<tr>
<td>Lower limit</td>
<td>4.0844</td>
<td>18.469</td>
</tr>
<tr>
<td>Upper limit</td>
<td>4.1776</td>
<td>18.513</td>
</tr>
</tbody>
</table>

---

<table>
<caption>Table V. Parameters for calculating $D(T)$ according to the PL fit in Eq. (A4). $D(T)$ results in cm² s⁻¹ for $T$ in K.</caption>
<thead>
<tr>
<th>Parameter</th>
<th>Value best fit</th>
<th>Value $2\sigma$ lower limit</th>
<th>Value $2\sigma$ upper limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>$D^{*}$</td>
<td>$8.3175\times10^{-6}$ cm² s⁻¹ K⁻⁰.⁵</td>
<td>$8.1617\times10^{-6}$ cm² s⁻¹ K⁻⁰.⁵</td>
<td>$8.392\times10^{-6}$ cm² s⁻¹ K⁻⁰.⁵</td>
</tr>
<tr>
<td>$T_s$</td>
<td>215.45 K</td>
<td>218.47 K</td>
<td>212.07 K</td>
</tr>
<tr>
<td>$\gamma$</td>
<td>1.9188</td>
<td>1.8178</td>
<td>2.0311</td>
</tr>
</tbody>
</table>

---

<table>
<caption>Table VI. Parameters for calculating $D(T)$ according to VFT fit in Eq. (A7). $D(T)$ results in cm² s⁻¹ for $T$ in K.</caption>
<thead>
<tr>
<th>Parameter</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>$D_0$</td>
<td>$9.6307\times10^{-4}$ cm² s⁻¹</td>
</tr>
<tr>
<td>$T_0$</td>
<td>148.0 K</td>
</tr>
<tr>
<td>$B$</td>
<td>560.96 K</td>
</tr>
</tbody>
</table>

---

<table>
<caption>Table VII. Parameters for calculating $J_{\text{hom}}(T)$ according to Eq. (A9). $J_{\text{hom}}$ results in cm⁻³ s⁻¹ for $T$ in K.</caption>
<thead>
<tr>
<th>$i$</th>
<th>$c_i$</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td>$-3020.684$</td>
</tr>
<tr>
<td>1</td>
<td>$-425.921$</td>
</tr>
<tr>
<td>2</td>
<td>$-25.977\;9$</td>
</tr>
<tr>
<td>3</td>
<td>$-0.868\;451$</td>
</tr>
<tr>
<td>4</td>
<td>$-1.662\;03\times10^{-2}$</td>
</tr>
<tr>
<td>5</td>
<td>$-1.717\;36\times10^{-4}$</td>
</tr>
<tr>
<td>6</td>
<td>$-7.469\;53\times10^{-7}$</td>
</tr>
</tbody>
</table>

<table>
<caption>TABLE VIII. Values recommended for checking computed parameterizations. Note that the last digits may vary depending upon the computational environment.</caption>
<thead>
<tr>
<th>Equation</th>
<th>230 K</th>
<th>240 K</th>
<th>250 K</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="4">Best fit from CNT analysis</td>
</tr>
<tr>
<td>$\Delta H_{m,h}(T)$ in kJ mol⁻¹ (A1)</td>
<td>3.8891</td>
<td>4.5741</td>
<td>5.0673</td>
</tr>
<tr>
<td>$\sigma_{sd,l}(T)$ in mJ m⁻² (A3)</td>
<td>16.5407</td>
<td>19.5748</td>
<td>21.7598</td>
</tr>
<tr>
<td>$D(T)$ in cm² s⁻¹ (A4)</td>
<td>$7.1603 × 10^{-07}$</td>
<td>$1.9957 × 10^{-06}$</td>
<td>$3.9238 × 10^{-06}$</td>
</tr>
<tr>
<td>$\Delta G_{\text{diff,PL}}(T)$ in J (A6)</td>
<td>$9.7905 × 10^{-20}$</td>
<td>$6.3813 × 10^{-20}$</td>
<td>$4.9649 × 10^{-20}$</td>
</tr>
<tr>
<td>$J_{hom}(T)$ in cm⁻³ s⁻¹ (1)</td>
<td>$1.33 × 10^{12}$</td>
<td>3.85</td>
<td>$1.05 × 10^{-55}$</td>
</tr>
<tr>
<td>$J_{hom}(T)$ polynomial fit in cm⁻³ s⁻¹ (A9)</td>
<td>$1.33 × 10^{12}$</td>
<td>3.83</td>
<td>$1.27 × 10^{-55}$</td>
</tr>
<tr>
<td colspan="4">Other parameters</td>
</tr>
<tr>
<td>$\Delta H_{m,h}(T)$ low in kJ mol⁻¹ (A1)</td>
<td>3.7018</td>
<td>4.5115</td>
<td>5.0441</td>
</tr>
<tr>
<td>$\Delta H_{m,h}(T)$ up in kJ mol⁻¹ (A1)</td>
<td>3.9680</td>
<td>4.5693</td>
<td>5.0680</td>
</tr>
</tbody>
</table>

activation energy, with parameters given in Table VI:

$$
\Delta G_{\text{diff,VFT}}(T) = \frac{kT^{2}B}{(T - T_{0})^{2}}. \tag{A8}
$$

The best fit for the temperature-dependent homogeneous ice nucleation rate coefficient $J_{hom}(T)$ was fitted to a polynomial for simpler computation

$$
x = \sum_{i} c_{i} \cdot (T - T_{m})^{i}, \tag{A9a}
$$

with

$$
J_{hom}(T) = 10^{x}, \tag{A9b}
$$

where $T$ is the temperature in K, and $J_{hom}(T)$ is given in $\text{cm}^{-3}\text{ s}^{-1}$. The fitting parameters $c_{i}$ and $i$ for Eq. (A9) are given in Table VII. Deviations between the best fit from CNT and the polynomial given in Eq. (A9) are smaller than $1.3\%$ over the atmospherically important temperature range of 230-245 K, smaller than $5\%$ at 225-230 K, and smaller than $22\%$ at 245-250 K. Equation (A9) should not be used outside this temperature range. Finally, in Table VIII we present values that we recommend for checking computer codes of all parameterizations presented in this manuscript.

¹L. Ickes, A. Welti, C. Hoose, and U. Lohmann, <i>Phys. Chem. Chem. Phys.</i> 17, 5514 (2015).

²G. de Boer, H. Morrison, M. D. Shupe, and R. Hildner, <i>Geophys. Res. Lett.</i> 38, L01803, doi:10.1029/2010gl046016 (2011).

³Y.-S. Choi, R. S. Lindzen, C.-H. Ho, and J. Kim, <i>Proc. Natl. Acad. Sci. U. S. A.</i> 107, 11211 (2010).

⁴C. D. Westbrook and A. J. Illingworth, <i>Geophys. Res. Lett.</i> 38, L14808, doi:10.1029/2011GL048021 (2011).

⁵D. Rosenfeld and W. L. Woodley, <i>Nature</i> 405, 440 (2000).

⁶D. Rosenfeld, X. Yu, G. Liu, X. Xu, Y. Zhu, Z. Yue, J. Dai, Z. Dong, Y. Dong, and Y. Peng, <i>Geophys. Res. Lett.</i> 38, L21804, doi:10.1029/2011GL049423 (2011).

⁷H. Laksmono, A. McQueen, J. A. Sellberg, N. D. Loh, C. Huang, D. Schlesinger, R. G. Sierra, C. Y. Hampton, D. Nordlund, M. Beye, A. V. Martin, A. Barty, M. M. Seibert, M. Messerschmidt, G. J. Williams, S. Boutet, K. Amann-Winkel, T. Loerting, L. G. M. Pettersson, M. J. Bogan, and A. Nilsson, <i>J. Phys. Chem. Lett.</i> 6, 2826 (2015).

⁸R. J. Herbert, B. J. Murray, S. J. Dobbie, and T. Koop, <i>Geophys. Res. Lett.</i> 42, 1599, doi:10.1002/2014GL062729 (2015).

⁹B. Kärcher and A. Seifert, <i>Q. J. R. Meteorol. Soc.</i> 142, 1320 (2016).

¹⁰C. A. Angell, <i>Annu. Rev. Phys. Chem.</i> 34, 593 (1983).

¹¹O. Mishima and H. E. Stanley, <i>Nature</i> 396, 329 (1998).

¹²P. G. Debenedetti, <i>J. Phys.: Condens. Matter</i> 15, R1669 (2003).

¹³R. J. Speedy and C. A. Angell, <i>J. Chem. Phys.</i> 65, 851 (1976).

¹⁴V. Holten and M. A. Anisimov, <i>Sci. Rep.</i> 2, 713 (2012).

¹⁵K. Ito, C. T. Moynihan, and C. A. Angell, <i>Nature</i> 398, 492 (1999).

¹⁶S. Cerveny, F. Mallamace, J. Swenson, M. Vogel, and L. Xu, <i>Chem. Rev.</i> 116, 7608 (2016).

¹⁷P. H. Poole, F. Sciortino, U. Essmann, and H. E. Stanley, <i>Nature</i> 360, 324 (1992).

¹⁸O. Mishima, <i>J. Chem. Phys.</i> 133, 144503 (2010).

¹⁹D. T. Limmer and D. Chandler, <i>J. Chem. Phys.</i> 135, 134503 (2011).

²⁰J. C. Palmer, F. Martelli, Y. Liu, R. Car, A. Z. Panagiotopoulos, and P. G. Debenedetti, <i>Nature</i> 510, 385 (2014).

²¹J. A. Sellberg, C. Huang, T. A. McQueen, N. D. Loh, H. Laksmono, D. Schlesinger, R. G. Sierra, D. Nordlund, C. Y. Hampton, D. Starodub, D. P. DePonte, M. Beye, C. Chen, A. V. Martin, A. Barty, K. T. Wikfeldt, T. M. Weiss, C. Caronna, J. Feldkamp, L. B. Skinner, M. M. Seibert, M. Messerschmidt, G. J. Williams, S. Boutet, L. G. M. Pettersson, M. J. Bogan, and A. Nilsson, <i>Nature</i> 510, 381 (2014).

²²E. B. Moore and V. Molinero, <i>Nature</i> 479, 506 (2011).

²³A. Dehaoui, B. Issenmann, and F. Caupin, <i>Proc. Natl. Acad. Sci. U. S. A.</i> 112, 12020 (2015).

²⁴S.-H. Chen, F. Mallamace, C.-Y. Mou, M. Broccio, C. Corsaro, A. Faraone, and L. Liu, <i>Proc. Natl. Acad. Sci. U. S. A.</i> 103, 12974 (2006).

²⁵W. S. Price, H. Ide, and Y. Arata, <i>J. Phys. Chem. A</i> 103, 448 (1999).

²⁶J. Mattsson, R. Bergman, P. Jacobsson, and L. Börjesson, <i>Phys. Rev. B</i> 79, 174205 (2009).

²⁷B. Zobrist, T. Koop, B. P. Luo, C. Marcolli, and T. Peter, <i>J. Phys. Chem. C</i> 111, 2149 (2007).

²⁸H. R. Pruppacher and J. D. Klett, <i>Microphysics of Clouds and Precipitation</i>, 2nd ed. (Kluwer Academic Publishers, 1997).

²⁹D. M. Murphy and T. Koop, <i>Q. J. R. Meteorol. Soc.</i> 131, 1539 (2005).

³⁰E. B. Moore and V. Molinero, <i>Phys. Chem. Chem. Phys.</i> 13, 20008 (2011).

³¹J. C. Johnston and V. Molinero, <i>J. Am. Chem. Soc.</i> 134, 6650 (2012).

³²T. Li, D. Donadio, G. Russo, and G. Galli, <i>Phys. Chem. Chem. Phys.</i> 13, 19807 (2011).

³³T. L. Malkin, B. J. Murray, A. V. Brukhno, J. Anwar, and C. G. Salzmann, <i>Proc. Natl. Acad. Sci. U. S. A.</i> 109, 1041 (2012).

³⁴T. L. Malkin, B. J. Murray, C. G. Salzmann, V. Molinero, S. J. Pickering, and T. F. Whale, <i>Phys. Chem. Chem. Phys.</i> 17, 60 (2015).

³⁵A. Haji-Akbari and P. G. Debenedetti, <i>Proc. Natl. Acad. Sci. U. S. A.</i> 112, 10582 (2015).

³⁶J. E. Shilling, M. A. Tolbert, O. B. Toon, E. J. Jensen, B. J. Murray, and A. K. Bertram, <i>Geophys. Res. Lett.</i> 33, L17801, doi:10.1029/2006GL026671 (2006).

³⁷K. T. Gillen, D. C. Douglass, and M. J. R. Hoch, <i>J. Chem. Phys.</i> 57, 5117 (1972).

³⁸F. X. Prielmeier, E. W. Lang, R. J. Speedy, and H. D. Lüdemann, <i>Phys. Rev. Lett.</i> 59, 1128 (1987).

³⁹F. X. Prielmeier, E. W. Lang, R. J. Speedy, and H. D. Lüdemann, <i>Ber. Bunsengesellschaft Phys. Chem.</i> 92, 1111 (1988).

⁴⁰H. Weingärtner, <i>Z. Phys. Chem.</i> 132, 129 (1982).

⁴¹M. Holz, S. R. Heil, and A. Sacco, <i>Phys. Chem. Chem. Phys.</i> 2, 4740 (2000).

⁴²R. S. Smith and B. D. Kay, <i>Nature</i> 398, 788 (1999).

⁴³C. A. Angell, <i>Science</i> 267, 1924 (1995).

⁴⁴P. G. Debenedetti and F. H. Stillinger, <i>Nature</i> 410, 259 (2001).

⁴⁵R. J. Speedy, <i>J. Phys. Chem.</i> 91, 3354 (1987).

⁴⁶P. Gallo, D. Corradini, and M. Rovere, <i>Nat. Commun.</i> 5, 5806 (2014).

⁴⁷L. Xu, P. Kumar, S. V. Buldyrev, S.-H. Chen, P. H. Poole, F. Sciortino, and H. E. Stanley, <i>Proc. Natl. Acad. Sci. U. S. A.</i> 102, 16558 (2005).

$^{48}$D. Turnbull, J. Appl. Phys. 21, 1022 (1950).

$^{49}$C. A. Jeffery and P. H. Austin, J. Geophys. Res. 102, 25269, doi:10.1029/97JD02243 (1997).

$^{50}$A. Reinhardt and J. P. K. Doye, J. Chem. Phys. 139, 096102 (2013).

$^{51}$Y. Cheng, H. Su, T. Koop, E. Mikhailov, and U. Pöschl, Nat. Commun. 6, 5923 (2015).

$^{52}$D. T. Limmer and D. Chandler, J. Chem. Phys. 137, 044509 (2012).

$^{53}$J. E. McDonald, J. Meteorol. 10, 416 (1953).

$^{54}$G. P. Johari, G. Fleissner, A. Hallbrucker, and E. Mayer, J. Phys. Chem. 98, 4719 (1994).

$^{55}$V. Holten, D. T. Limmer, V. Molinero, and M. A. Anisimov, J. Chem. Phys. 138, 174501 (2013).

$^{56}$B. Riechers, F. Wittbracht, A. Hutten, and T. Koop, Phys. Chem. Chem. Phys. 15, 5873 (2013).

$^{57}$B. Kramer, O. Hubner, H. Vortisch, L. Woste, T. Leisner, M. Schwell, E. Ruhl, and H. Baumgartel, J. Chem. Phys. 111, 6521 (1999).

$^{58}$D. Duft and T. Leisner, Atmos. Chem. Phys. 4, 1997 (2004).

$^{59}$D. Rzesanke, J. Nadolny, D. Duft, R. Muller, A. Kiselev, and T. Leisner, Phys. Chem. Chem. Phys. 14, 9359 (2012).

$^{60}$S. Benz, K. Megahed, O. Mohler, H. Saathoff, R. Wagner, and U. Schurath, J. Photochem. Photobiol. A: Chem. 176, 208 (2005).

$^{61}$P. Stöckel, I. M. Weidinger, H. Baumgartel, and T. Leisner, J. Phys. Chem. A 109, 2540 (2005).

$^{62}$P. Kabath, P. Stöckel, A. Lindinger, and H. Baumgärtel, J. Mol. Liq. 125, 204 (2006).

$^{63}$C. A. Stan, G. F. Schneider, S. S. Shevkoplyas, M. Hashimoto, M. Ibanescu, B. J. Wiley, and G. M. Whitesides, Lab Chip 9, 2293 (2009).

$^{64}$C. R. Hoyle, V. Pinti, A. Welti, B. Zobrist, C. Marcolli, B. Luo, Á Höskuldsson, H. B. Mattsson, O. Stetzer, T. Thorsteinsson, G. Larsen, and T. Peter, Atmos. Chem. Phys. 11, 9911 (2011).

$^{65}$F. Lüönd, O. Stetzer, A. Welti, and U. Lohmann, J. Geophys. Res. 115, D14201, doi:10.1029/2009JD012959 (2010).

$^{66}$L. Ladino, O. Stetzer, F. Lüönd, A. Welti, and U. Lohmann, J. Geophys. Res. 116, D22202, doi:10.1029/2011JD015727 (2011).

$^{67}$D. A. Knopf, P. A. Alpert, B. Wang, and J. Y. Aller, Nat. Geosci. 4, 88 (2011).

$^{68}$M. E. Earle, T. Kuhn, A. F. Khalizov, and J. J. Sloan, Atmos. Chem. Phys. 10, 7945 (2010).

$^{69}$S. E. Wood, M. B. Baker, and B. D. Swanson, Rev. Sci. Instrum. 73, 3988 (2002).

$^{70}$A. Manka, H. Pathak, S. Tanimura, J. Wolk, R. Strey, and B. E. Wyslouzil, Phys. Chem. Chem. Phys. 14, 4505 (2012).

$^{71}$J. Huang and L. S. Bartell, J. Phys. Chem. 99, 3924 (1995).

$^{72}$B. J. Murray, S. L. Broadley, T. W. Wilson, S. J. Bull, R. H. Wills, H. K. Christenson, and E. J. Murray, Phys. Chem. Chem. Phys. 12, 10380 (2010).

$^{73}$D. J. Safarik and C. B. Mullins, J. Chem. Phys. 121, 6003 (2004).

$^{74}$P. Jenniskens and D. F. Blake, Astrophys. J. 473, 1104 (1996).

$^{75}$T. Nemec, Chem. Phys. Lett. 583, 64 (2013).

$^{76}$E. Mayer and P. Bruggeller, Nature 298, 715 (1982).

$^{77}$I. Kohl, L. Bachmann, A. Hallbrucker, E. Mayer, and T. Loerting, Phys. Chem. Chem. Phys. 7, 3210 (2005).

$^{78}$A. Zaragoza, M. M. Conde, J. R. Espinosa, C. Valeriani, C. Vega, and E. Sanz, J. Chem. Phys. 143, 134504 (2015).

$^{79}$A. Hudait, S. Qiu, L. Lupi, and V. Molinero, Phys. Chem. Chem. Phys. 18, 9544 (2016).

$^{80}$J. Benet, L. G. MacDowell, and E. Sanz, Phys. Chem. Chem. Phys. 16, 22159 (2014).

$^{81}$S. C. Hardy, Philos. Mag. 35, 471 (1977).

$^{82}$R. L. Davidchack, R. Handal, J. Anwar, and A. V. Brukhno, J. Chem. Theory Comput. 8, 2383 (2012).

$^{83}$J. R. Espinosa, C. Vega, and E. Sanz, J. Phys. Chem. C 120, 8068 (2016).

$^{84}$J. R. Espinosa, C. Vega, C. Valeriani, and E. Sanz, J. Chem. Phys. 144, 034501 (2016).

$^{85}$E. Sanz, C. Vega, J. R. Espinosa, R. Caballero-Bernal, J. L. F. Abascal, and C. Valeriani, J. Am. Chem. Soc. 135, 15008 (2013).

$^{86}$A. Bhabhe, H. Pathak, and B. E. Wyslouzil, J. Phys. Chem. A 117, 5472 (2013).

$^{87}$W. F. Kuhs, C. Sippel, A. Falenty, and T. C. Hansen, Proc. Natl. Acad. Sci. U. S. A. 109, 21259 (2012).

$^{88}$H. R. Pruppacher, J. Atmos. Sci. 52, 1924 (1995).

$^{89}$B. J. Murray and E. J. Jensen, J. Atmos. Sol.-Terr. Phys. 72, 51 (2010).

$^{90}$A. Nillson and H. Laksmono, personal communication (2016).