Article

# Thermal Expansion and Other Thermodynamic Properties of $\alpha_2$-Ti₃Al and $\gamma$-TiAl Intermetallic Phases from First Principles Methods

David Holec \*, Neda Abdoshahi, Svea Mayer and Helmut Clemens

Department of Materials Science, Montanuniversität Leoben, Franz-Josef-Straße 18, A-8700 Leoben, Austria;
neda.abdoshahi@unileoben.ac.at (N.A.); svea.mayer@unileoben.ac.at (S.M.);
helmut.clemens@unileoben.ac.at (H.C.)

* Correspondence: david.holec@unileoben.ac.at; Tel.: +43-3841-402-4211

Received: 28 March 2019; Accepted: 15 April 2019; Published: 19 April 2019

![](./images/812783287536713729_1.jpg)

**Abstract:** Anisotropic thermal expansion coefficients of tetragonal $\gamma$-TiAl and hexagonal $\alpha_2$-Ti₃Al phases were calculated using first principles methods. Two approaches with different computational costs and degrees of freedom were proposed. The predicted values were compared with available experimental data showing that for $\gamma$-TiAl, the more computational demanding method with decoupled impact of volume and temperature effects on the cell shape leads to significantly better results than that with only ground-state optimised unit cell geometry. In the case of the $\alpha_2$-Ti₃Al phase, both approaches yielded comparable results. Additionally, heat capacity and bulk modulus were evaluated as functions of temperature for both phases, and were fitted to provide an analytical formula which can be further used.

**Keywords:** thermal expansion; titanium aluminides; thermodynamic properties; ab initio calculations; quasi-harmonic approximation

## 1. Introduction

First principles calculations are now a widely used and well-established method for complementing experimental materials science research [1]. Despite the fact that many recent activities have been directed towards big-data and machine learning [2–4], there are still many topics which require individualised treatments. An example of such a problem is the discrepancy between the experimentally and theoretically reported stability and chemistry of the Nb₃Al phase also published in this special issue [5]. Starting from the pioneering works of Grabowski and co-workers [6–11], the first-principles thermodynamics by including the vibrational contribution to the free energy within the harmonic approximation have became fairly routine. Among other available tools, phonopy [12] has become widely used thanks to its robustness, openness and flexibility. The there implemented quasi-harmonic approximation (QHA) for calculating thermal properties, such as thermal expansion, bulk modulus or heat capacity, however, does not include effects of temperature-induced changes in the unit cell geometry in terms of $c/a$ or $b/a$ ratios or lattice angles, as may be the case of systems with lower than cubic symmetry.

In this paper we will focus on $\gamma$-titanium aluminides, which are a class of intermetallic materials with a broad range of potential high temperature applications [13–17]. They exhibit good specific yield strength and elastic moduli at elevated temperatures, while simultaneously having low density, good oxidation resistance and resistance against Ti-fire [18–22]. Depending on the exact chemical composition, several phases are present in TiAl alloys [23]. The majority phase is the tetragonal $\gamma$-TiAl phase (tetragonal L1₀, space group P4/mmm) after which this material class is named. In addition,

Materials 2019, 12, 1292; doi:10.3390/ma12081292
www.mdpi.com/journal/materials

the $\alpha_2$-Ti$_3$Al phase (hexagonal D0$_{19}$, space group P6$_3$/mmc) is also present in alloys of industrial relevance. When the solidification proceeds via the $\beta$-phase field, the ordered $\beta_o$-TiAl phase (B2, Pm$\overline{3}$m) may also be detected at room temperature (RT) [24–26]. A careful selection of the alloy processing route, by which the phase volume fractions and grain morphology are adjusted, results in optimising the TiAl mechanical properties within certain limits [14,27,28]. The $\beta_o$ phase, however, does not appear in the pure binary Ti–Al system [29], and therefore will not be discussed here anymore.

Many material parameters are needed as inputs for the precise consideration of structural materials. Thermodynamic data such as heat capacities and Gibbs free energies are essential inputs for Calphad-based modelling, as demonstrated, e.g., by a recent reassessment of the Ti–Al–Mo ternary system [30]. Nevertheless, for structural materials for high temperature applications, as is the case of TiAl-based alloys, other properties are equally important for predicting a precise microstructural state including internal stresses. Among these is coefficient of thermal expansion (TEC), $\alpha$, which is not part of a standard thermodynamic assessment. This is demonstrated, for example, in Refs. Nabarro [31], Schuh et al. [32], where the influence of the anisotropic thermal expansion in $\gamma$-TiAl on the creep behaviour under cyclic thermal loading is discussed. Further on, the authors suggested that the effect of thermal cycling is expected to be significantly higher in the $\alpha_2$-phase and that ratcheting creep is to be expected in polycrystalline specimens. However, due to the lack of thermal expansion data, this postulation could not be substantiated.

Several techniques have been used to estimate TEC experimentally. Zupan and Hemker [33] used micro tensile testing to study $\gamma$ single crystals. He et al. [34] presented a comprehensive investigation of $\gamma$-Ti$_{44}$Al$_{56}$ (Ti-56Al, in atomic percent) using a capacitance dilatometer to determine TEC along the $a$ ($\gamma$-[100]) and $c$ ($\gamma$-[001]) directions in the temperature range between 0 and 750 K. Bittorf et al. [35] determined the TEC of $\gamma$ single-phase polycrystalline specimen of Ti$_{45}$Al$_{54}$ (Ti-54Al in atomic percent) by means of neutron diffraction, which are very close to those of He et al. [34]. Both these studies suggest that $\alpha_a > \alpha_c$.

Thermal expansion of polycrystalline multiphase specimens was investigated by Stone and Kurfess [36] and Zhang et al. [37] employing dilatometric techniques. In these cases, however, the results describe the overall thermal expansion behaviour of the investigated alloys, and do not allow for distinguishing TEC of individual phases. Novoselova et al. [38] utilised high-energy X-ray diffraction (HEXRD) to determine various material parameters including TEC, for the $\alpha_2$ and $\gamma$-phase in a polycrystalline specimen of Ti–46Al–1.9Cr–3Nb (at. %), in the temperature range from 0–1500 °C. Unfortunately, this study provides only a low number of data points between 0 and 1000 °C. Recently, Li et al. [39] published a study on Ti-45Al-7.5Nb-0.5C (at. %), in which they report on thermal strains in individual ($\gamma$ and $\alpha_2$) phases using synchrotron diffraction. They also suggest that $\alpha_a$ is slightly larger than $\alpha_c$, although they do not focus on the low-temperature regime below 1000 K and report only a single value independent of temperature (linear thermal expansion with respect to room temperature lattice constants). In contrast to Refs. [34,35,39], Novoselova et al. [38] obtained $\alpha_a \approx$ 2.5-times smaller than $\alpha_c$. It is therefore reasonable to expect that TEC is strongly composition-dependent.

Other phases present in the Ti–Al system, in particular the $\alpha_2$-Ti$_3$Al phase, have received very little attention and data on their thermal expansion coefficients are scarce. While Novoselova et al. [38] reported $\alpha_a > \alpha_c$ for Ti-46Al-1.9Cr-3Nb (at. %), Li et al. [39] measured TEC for Ti-45Al-7.5Nb-0.5C (at. %) in both directions essentially the same and more than twice higher than in the formed case. Despite both these studies are not for pure phases, we can conclude that in this case TEC is also likely to be strongly composition-dependent.

As a counterpart to the experimentally estimated values of TEC, first principles quantum mechanical calculations were used by Fu et al. [40] to predict the thermal expansion behaviour of the $\gamma$-TiAl phase at pressures ranging from 0 (ambient pressure) to 100 GPa. However, in comparison with the experimental TEC obtained by He et al. [34], the calculated values are significantly higher. Moreover, the authors did not account for the tetragonality of the $\gamma$-TiAl, i.e., the possible anisotropy of TEC.

Therefore, in the current work, we employ first principles calculations within the quasi-harmonic approximation to reveal TEC of the $\alpha_2$-Ti$_3$Al and $\gamma$-TiAl phases with a special focus on determining the anisotropy of this property.

## 2. Methods

We used the state-of-the-art program VASP (Vienna Ab-initio Simulation Package) [41] employing Density Functional Theory [42,43] to carry out the first principles calculations. The atomic basis functions were represented by projector augmented wave pseudopotentials with the $3s^23p^64s^23d^2$ and $3s^22p^1$ valence electron configuration for Ti and Al atoms, respectively. The exchange-correlation effects were treated using gradient corrected exchange-correlation functional parametrised by Perdew-Burke-Ernzerhof (GGA-PBE) [44,45] and the plane wave cut-off energy of 500 eV were applied to predict ground state properties of both the $\gamma$-TiAl and $\alpha_2$-Ti$_3$Al phases. The reciprocal unit cell was sampled with $14 \times 14 \times 14$ ($\gamma$, 4 atoms) and $12 \times 12 \times 13$ ($\alpha_2$, 8 atoms) **k**-point mesh using the Monkhorst-Pack scheme. These parameters guarantee total energy accuracy better than 1 meV/at.

The structural optimisation includes evaluation of total energies at various volumes. Full relaxation including unit cell shape and internal atomic coordinates optimisation was performed for every volume, yielding lattice parameters $a_0^\xi(V)$ and $c_0^\xi(V)$ ($\xi = \gamma$ or $\alpha_2$) as functions of volume at 0 K.

Thermal properties were evaluated within the quasi-harmonic approximation (QHA) using the phonopy code [12,46]. The phonon frequencies were calculated for 6 evenly spaced volumes in the range $15.4$–$17.4 \mathring{A}^3$/at. ($\gamma$-phase) and 6 volumes in the range $15.8$–$17.9 \mathring{A}^3$/at. ($\alpha_2$-phase) employing $3 \times 3 \times 3$ (54 atoms) and $2 \times 2 \times 2$ (64 atoms) supercells, respectively.

Assuming that the $c/a$ ratio is only a function of volume and not temperature, the resulting temperature dependence of volume $V^\xi(T)$ as obtained from the QHA (phonopy-qha package), allows to determine also the temperature dependencies of individual lattice constants $x^\xi(T)$, $x=a,c$ and $\xi=\gamma,\alpha_2$, as:

$$
x^{\xi}(T)=x_{0}^{\xi}(V(T)). \tag{1}
$$

This treatment is in the following termed as 'ground state optimised cell shape' (gs-cs).

To probe the validity of the assumption that the $c/a$ is only a function of volume independent of temperature, we have adopted additional scheme. For every volume, we selected 5 $c/a$ ratios around the GGA-PBE equilibrium values $((c/a)_\gamma^{\text{GGA-PBE}}=1.018, (c/a)_{\alpha_2}^{\text{GGA-PBE}}=0.809)$. For each of these static configurations, thermodynamic properties within the harmonic approximation (phonopy package) were calculated, hence yielding vibrational Helmholtz free energies $F_{\text{vib}}(T,V,c/a)$. The total Helmholtz free energy, $F$, was constructed by adding the 0 K total energies:

$$
F(T,V,c/a)=E_{\text{tot}}(V,c/a)+F_{\text{vib}}(T,V,c/a). \tag{2}
$$

The equilibrium geometry at a fixed temperature $T$ was then calculated by a two step fitting. First, we estimated

$$
F(T,V)=\min_{c/a}F(T,V,c/a) \tag{3}
$$

by fitting the $F(T=\text{const.}, V=\text{const.},c/a)$ data with a second order polynomial. Subsequently, the $F(T,V)$ data were fitted with the Birch-Murnaghan equation of state [47] to obtain the equilibrium volume $V_0(T)$ (in addition to free energy, $F(T)$, bulk modulus, $B(T)$, and pressure derivative of bulk modulus, $B'(T)$). Finally, the $(c/a)(T=\text{const.},V)$ data minimising $F(T=\text{const.},V,c/a)$ in Equation (3), were linearly interpolated as a function of $V$, and the equilibrium value at temperature $T$ was estimated from this linear fit at $V=V_0(T)$. This procedure allows to decouple influence of temperature and pressure (volume) on the cell geometry, and is in the following thus termed 'temperature optimised cell shape' (to-cs) approach.

The thermal expansion coefficients were calculated from the estimated lattice parameters as

$$
\alpha_{x}^{\xi}(T)=\frac{1}{x_{\xi}(T)} \frac{d x_{\xi}}{d T} \approx \frac{1}{x_{\xi}(T)} \frac{x_{\xi}(T+\Delta T)-x_{\xi}(T-\Delta T)}{2 \Delta T}. \tag{4}
$$

Finally, the heat capacity at constant (ambient) pressure, $C_p$, was estimated from the Helmholtz free energy, $F^{\xi}(T)$, as

$$
C_{p}(T)=-T \frac{\partial^{2} F(T)}{\partial T^{2}} \approx-T \frac{F(T+\Delta T)+F(T-\Delta T)-2 F(T)}{(\Delta T)^{2}}. \tag{5}
$$

The latter expressions in Equations (4) and (5) represent numerical derivatives as both, lattice constants and Helmholtz free energy were calculated on a discrete set of temperatures from 0 to 1000 K with a step of 10 K.

### 3. Results

#### 3.1. Thermal Expansion

We start our analysis by comparing the predicted temperature dependence of specific volumes of the $\alpha_2$-Ti₃Al and $\gamma$-TiAl phases using both approaches as described in the Section 2. Figure 1a shows the temperature dependence of specific volume (i.e., volume per atom) for both considered phases as predicted using volume geometries optimised only at 0 K (gs-cs) and at every temperature (to-cs). While these two approaches provide almost identical results for the $\alpha_2$-Ti₃Al phase (blue curves), significant differences are obtained for the $\gamma$-TiAl. Namely, the gs-cs method yields larger and faster expanding volumes than the to-cs treatment. The former is also significantly non-linear, suggesting that the resulting coefficient of volume thermal expansion is strongly increasing at higher temperatures and does not reach the usual near-to-linear behaviour for temperatures above room temperature (RT, $\sim$298 K).

![](./images/812783287536713729_2.jpg)

Figure 1. (a) Specific volume and (b) $c/a$ ratio as functions of temperature for the $\alpha_2$-Ti₃Al (blue) and $\gamma$-TiAl (orange) phases predicted using quasi-harmonic approximation with cell shape optimised at 0 K (dashed, label 'gs-cs' (ground state optimised cell shape)) and at every temperature (solid line, label 'to-cs' (temperature optimised cell shape)).

Importantly, both approaches allow for explicitly estimating $a$ and $c$ lattice constants describing the hexagonal $\alpha_2$-Ti₃Al and tetragonal $\gamma$-TiAl structures. Similarly to the specific volume, the $c/a$ ratio for the $\alpha_2$ structure also does not differ much for both the gs-cs and to-cs approaches. While the absolute values do not differ very much, the qualitative temperature-dependence changes from $c/a$ decreasing with temperature as predicted by the gs-cs method to $c/a$ increasing with raising temperature for the to-cs approach (see Figure 1b). Qualitatively similar behaviour is also predicted

for the $\gamma$-TiAl phase, although in the opposite sense: the gs-cs and to-cs methods predict slightly increasing and strongly decreasing $c/a$ values, respectively, with increasing temperature.

The specific volume and $c/a$ ratio allow to calculate also the corresponding lattice parameters $a$ and $c$, and then to further use these to obtain lattice thermal expansion coefficients, $\alpha_a$ (Figure 2a) and $\alpha_c$ (Figure 2b), according to Equation (4). Regarding the hexagonal $\alpha_2$-Ti₃Al phase, $\alpha_a$ is slightly larger than $\alpha_c$ for all temperatures. Perhaps the most important difference is that while $\alpha_a$ still increases with temperature even above RT and to higher values than $10 \times 10^{-6}\ \text{K}^{-1}$ above $\sim$600 K, while $\alpha_c$ seems to quickly saturate around $10 \times 10^{-6}\ \text{K}^{-1}$ above RT. Importantly, there are no significant differences between the predicted values by gs-cs and to-cs methods. The obtained differences are of the same order as the scatter of the numerical noise imposed by the to-cs method, represented by the individual data points in Figure 2.

![](./images/812783287536713729_3.jpg)

Figure 2. Lattice thermal expansion along (a) $a$-direction, $\alpha_a$, and (b) $c$-direction, $\alpha_c$, as functions of temperature for the $\alpha_2$-Ti₃Al (blue) and $\gamma$-TiAl (orange) phases predicted using quasi-harmonic approximation with cell shape optimised at 0 K (dashed, label 'gs-cs') and at every temperature (solid line, label 'to-cs'). The data points shown by dots are the actual numerically calculated values using Equation (4). The smooth curves are 'guides for the eyes' from interpolation using Bezier curves.

A very different situation is obtained in the $\gamma$-TiAl case. The gs-cs case predicts significant temperature dependence of both $\alpha_a$ and $\alpha_c$, moreover, both having very similar values. This large increase of TEC with temperature is a consequence of strongly expanding volume of the $\gamma$-TiAl (cf. Figure 1a) resulting from the gs-cs method. On the other hand, the to-cs approach predicts large TEC values of $\sim$$15 \times 10^{-6}\ \text{K}^{-1}$ above RT in the $a$-direction, while 3-fold smaller values of around $5 \times 10^{-6}\ \text{K}^{-1}$ (and basically temperature-independent above RT) are predicted for $\alpha_c$. This behaviour leads to a strong temperature dependence of $c/a$ (cf. Figure 1b).

In summary, while the computationally more demanding to-cs method does not yield too different temperature dependence of structural properties in comparison to the simpler gs-cs approach for the $\alpha_2$-Ti₃Al, non-negligible differences are obtained in the case of the $\gamma$-TiAl.

### 3.2. Other Thermodynamic Properties

The calculation of the thermal expansion is based on evaluation of the vibrational entropy term of the Helmholtz free energy, which is the most important contribution, and has been demonstrated several times to be the only important contribution when dealing with non-magnetic materials at temperatures far below melting point [9,11]. The thus obtained thermodynamic potentials, however, offer thermal dependence of other quantities, too.

The heat capacity, $C_p$, at constant (ambient) pressure was evaluated according to Equation (5). The calculated values for the two phases are almost identical, in particular from the to-cs treatment (Figure 3a). This result could be intuitively understood by the fact that the molar heat capacities of Al and Ti are very similar [6]. Such prediction is important, e.g., for the discussion of microstructure evolution upon phase transformations during cooling.

![](./images/812783287536713729_4.jpg)

Figure 3. (a) Heat capacity at constant (ambient) pressure and (b) bulk modulus of the $\alpha_2$ (blue lines) and $\gamma$ (orange lines) phase as functions of temperature evaluated within the gs-cs (dashed lines) and to-cs (solid lines) approach.

The temperature dependence of bulk modulus (i.e., the inverse of compressibility) (Figure 3b) can be estimated from fitting section of the Helmholtz free energy surface at fixed temperature with, e.g., the Birch–Murnaghan equation of state [47]. It turns out that the bulk modulus of the $\gamma$-phase is smaller than that of the $\alpha_2$-phase in the whole temperature range up to 1000 K. The bulk modulus softens with the increasing temperature by $\sim$12% between 0 K and 770 K ($\sim$500 °C) and by approximately $\sim$8.5% between RT and 500 °C for both, $\gamma$ and $\alpha_2$-phases. Significantly different is only the gs-cs temperature dependence for the $\gamma$-phase, which yields drop of over 30% between 0 and 770 K, further underlying that this approach is not reasonable for the $\gamma$-TiAl, in accordance with other properties discussed so far.

In order to provide the reader with an easy access to our calculated quantities, the trends were fitted with analytical expressions and the resulting fitted parameters as well as the fits themselves are summarised in Appendix A.

### 3.3. Discussion

As mentioned in the introduction, experimental data for comparison are scarce. In fact, data corresponding to exactly ideal conditions of single phases with exact stoichiometric compositions are non-existant at all. Nevertheless, experimental data on single crystal [34], as well as on polycrystalline $\gamma$-TiAl [35], suggest that $\alpha_a > \alpha_c$, in agreement with our calculations. On the one hand, the differences between $a$ ([1 0 0]) and $c$ ([0 0 1]) directions are not so large in experiments as they are predicted here (cf. Figure 2), on the other hand the experimental data are for Al-rich compositions with 54 and 56 at.% Al. That the composition can play a significant role is demonstrated by the hugely different TEC reported for Ti-46Al-3Nb-1.9Cr (at. %) [38] and Ti-45Al-7.5Nb-0.5C (at. %) [39]. In the light of these hugely scattering experimental data, our predictions are qualitatively correct in implying $\alpha_a > \alpha_c$.

The structurally optimised $c/a$ ratio of $\sim$1.020 is in excellent agreement with the experimentally reported values 1.016 [48] for Al-rich $\gamma$-TiAl to 1.02 [17]. The latter two values are higher than the $\sim$1.012 measured for Ti-45Al-7.5Nb-0.5C (at. %) [39]. Importantly, Li et al. [39] obtained a slightly

decreasing $c/a$ ratio with increasing temperature up to 1000 K (followed by a strong decrease for temperatures further increasing up to 1400 K), a result qualitatively well in agreement with our to-cs predictions. Further on, Li et al. [39] reported that the $c/a$ of $\alpha_2$-Ti$_3$Al stays rather constant, i.e., $\sim$0.806, in the temperature range from 450 to 1000 K. Despite the fact that the gs-cs and to-cs approaches yield decreasing and increasing $c/a$ with temperature, respectively, the temperature dependence is not very strong (as, e.g., in the case of the $\gamma$-TiAl phase) and hence both methods are, in fact, valid for the $\alpha_2$-phase. It should also be mentioned that experimental results on polycrystalline specimens may be biased by building up coherency strains between phases with different expansion behaviour [49]. Especially in the case of TiAl alloys, which contain a large volume fraction of lamellar $\alpha_2/\gamma$ colonies, this effect may potentially have a significant impact on the obtained experimental data.

Finally, our calculated values of TEC agree with experimental results, but are significantly lower than other DFT-based predictions by Fu et al. [40]. We ascribe this discrepancy to the different methodology used: in the present study, we have explicitly evaluated the vibrational contribution to the Helmholtz free energy by calculating phonon properties, whereas Fu et al. [40] used a semi-classical Debye model. We therefore conclude that explicit evaluation of the phonon frequencies and their contribution to the phonon free energy is essential.

## 4. Conclusions
Thermal properties, with a special focus on structural analysis of temperature dependent lattice parameters and coefficients of thermal expansion of tetragonal $\gamma$-TiAl and hexagonal $\alpha_2$-Ti$_3$Al phases of binary Ti-Al system, were calculated using first principles methods. We put our attention on testing whether the $c/a$ ratio is purely a function of volume independent of temperature, or whether temperature and volumetric effects have to be separated. Our calculations show that in the case of the $\gamma$-TiAl phase significant differences are obtained, while both approaches yield comparable results for the hexagonal $\alpha_2$-Ti$_3$Al phase. The predictions were further compared with available experimental data. While this was not straightforward due to lack of single-crystalline data with close-to-perfect stoichiometries, we propose that the to-cs method with decoupled impact of temperature and volume on the cell geometry ($c/a$ ratio) gives better agreement for the $\gamma$-TiAl phase. The present paper therefore contributes to advancing first principles thermodynamics beyond systems with cubic symmetry.

**Author Contributions:** The author contributions are as follows: concept, D.H. and H.C.; methodology, D.H.; calculations, N.A., D.H.; resources, D.H.; writing—original draft preparation, D.H.; writing—review and editing, D.H., H.C., N.A., S.M.; visualization, D.H.; supervision, D.H.; project administration, D.H.; funding acquisition, D.H., S.M.

**Funding:** This research was funded by the Austrian Science Fund (FWF) Project Number P29731.

**Acknowledgments:** The computational results presented have been achieved in part using the Vienna Scientific Cluster (VSC).

**Conflicts of Interest:** The authors declare no conflict of interest. The funders had no role in the design of the study; in the collection, analyses, or interpretation of data; in the writing of the manuscript, or in the decision to publish the results.

### Abbreviations
The following abbreviations are used in this manuscript:

| Abbreviation | Meaning |
|---|---|
| DFT | Density Functional Theory |
| GGA | Generalised Gradient Approximation |
| gs-cs | ground state optimised cell shape |
| HA | harmonic approximation |
| QHA | quasi-harmonic approximation |
| RT | room temperature |
| TEC | coefficient of thermal expansion |
| to-cs | temperature optimised cell shape |

## Appendix A. Analytical Fits

The thermodynamic quantities discussed above calculated using the to-cs approach were fitted with a function of the form

$$
X(T)=a_{0}^{X}+\sum_{i=1}^{4} a_{i}^{X} T^{i}+\sum_{i=1}^{4} b_{i}^{X} \frac{1}{T^{i}}+c^{X} \ln(T). \tag{A1}
$$

This function fits accurately all obtained data within the temperature window from 0 to 1000 K.
The fitted coefficients for $X=F$ (Helmholtz free energy), $C_p$ (molar heat capacity), $B$ (bulk modulus) and $\alpha_a$ and $\alpha_c$ (TEC in the $a$ and $c$ directions) are summarised in Tables A1 and A2, and the fits are presented in Figure A1. The calculated dependencies provide a consistent set of material constants.

**Table A1.** Fitted coefficients according to Equation (A1) for the calculated thermodynamic properties of the $\gamma$-TiAl phase. $F$ is Helmholtz free energy [eV/at.], $C_p$ is molar heat capacity at constant pressure [J/K/mol] (mol of atoms), $B$ is bulk modulus [GPa] and $\alpha_a$ and $\alpha_c$ are coefficient of thermal expansion (TEC) in the [1 0 0] and in the [0 0 1] directions [K⁻¹].

<table>
<thead>
<tr>
<th></th>
<th>F</th>
<th>C<sub>p</sub></th>
<th>B</th>
<th>$\alpha_a$</th>
<th>$\alpha_c$</th>
</tr>
<tr>
<th></th>
<th>[eV/at.]</th>
<th>[J/K/mol]</th>
<th>[GPa]</th>
<th>[K⁻¹]</th>
<th>[K⁻¹]</th>
</tr>
</thead>
<tbody>
<tr>
<td>$a_0$</td>
<td>$-6.4187\times 10^{+00}$</td>
<td>$-3.4558\times 10^{+01}$</td>
<td>$1.1499\times 10^{+02}$</td>
<td>$-3.6457\times 10^{-05}$</td>
<td>$-3.8562\times 10^{-04}$</td>
</tr>
<tr>
<td>$a_1$</td>
<td>$-1.8683\times 10^{-04}$</td>
<td>$-4.2978\times 10^{-02}$</td>
<td>$-1.8487\times 10^{-02}$</td>
<td>$-7.0845\times 10^{-08}$</td>
<td>$-3.9878\times 10^{-07}$</td>
</tr>
<tr>
<td>$a_2$</td>
<td>$-3.7211\times 10^{-07}$</td>
<td>$5.0198\times 10^{-05}$</td>
<td>$1.5144\times 10^{-06}$</td>
<td>$8.5104\times 10^{-11}$</td>
<td>$4.5801\times 10^{-10}$</td>
</tr>
<tr>
<td>$a_3$</td>
<td>$1.5691\times 10^{-10}$</td>
<td>$-3.5403\times 10^{-08}$</td>
<td>$-6.3023\times 10^{-10}$</td>
<td>$-5.4782\times 10^{-14}$</td>
<td>$-3.2999\times 10^{-13}$</td>
</tr>
<tr>
<td>$a_4$</td>
<td>$-3.7138\times 10^{-14}$</td>
<td>$1.0447\times 10^{-11}$</td>
<td>$-2.0214\times 10^{-12}$</td>
<td>$1.4449\times 10^{-17}$</td>
<td>$1.0165\times 10^{-16}$</td>
</tr>
<tr>
<td>$b_1$</td>
<td>$3.4305\times 10^{+00}$</td>
<td>$2.9671\times 10^{+02}$</td>
<td>$-2.1317\times 10^{+02}$</td>
<td>$-7.2401\times 10^{-04}$</td>
<td>$6.0522\times 10^{-03}$</td>
</tr>
<tr>
<td>$b_2$</td>
<td>$-6.0577\times 10^{+01}$</td>
<td>$-2.0669\times 10^{+01}$</td>
<td>$5.5554\times 10^{+03}$</td>
<td>$3.6802\times 10^{-02}$</td>
<td>$-9.7074\times 10^{-02}$</td>
</tr>
<tr>
<td>$b_3$</td>
<td>$6.3758\times 10^{+02}$</td>
<td>$-3.9874\times 10^{+04}$</td>
<td>$-6.9252\times 10^{+04}$</td>
<td>$-5.5989\times 10^{-01}$</td>
<td>$9.1203\times 10^{-01}$</td>
</tr>
<tr>
<td>$b_4$</td>
<td>$-2.6280\times 10^{+03}$</td>
<td>$2.7003\times 10^{+05}$</td>
<td>$3.1027\times 10^{+05}$</td>
<td>$2.7435\times 10^{+00}$</td>
<td>$-3.4160\times 10^{+00}$</td>
</tr>
<tr>
<td>$c$</td>
<td>$4.4277\times 10^{-02}$</td>
<td>$7.9870\times 10^{+00}$</td>
<td>$-4.5702\times 10^{-01}$</td>
<td>$1.1764\times 10^{-05}$</td>
<td>$8.0199\times 10^{-05}$</td>
</tr>
</tbody>
</table>

**Table A2.** Fitted coefficients according to Equation (A1) for the calculated thermodynamic properties of the $\alpha_2$-Ti₃Al phase. $F$ is Helmholtz free energy [eV/at.], $C_p$ is molar heat capacity at constant pressure [J/K/mol] (mol of atoms), $B$ is bulk modulus [GPa] and $\alpha_a$ and $\alpha_c$ are TEC in the (0 0 0 1) plane and in the [0 0 0 1] direction [K⁻¹].

<table>
<thead>
<tr>
<th></th>
<th>F</th>
<th>C<sub>p</sub></th>
<th>B</th>
<th>$\alpha_a$</th>
<th>$\alpha_c$</th>
</tr>
<tr>
<th></th>
<th>[eV/at.]</th>
<th>[J/K/mol]</th>
<th>[GPa]</th>
<th>[K⁻¹]</th>
<th>[K⁻¹]</th>
</tr>
</thead>
<tbody>
<tr>
<td>$a_0$</td>
<td>$-7.3540\times 10^{+00}$</td>
<td>$-2.0371\times 10^{+01}$</td>
<td>$1.1716\times 10^{+02}$</td>
<td>$-1.6008\times 10^{-04}$</td>
<td>$5.4128\times 10^{-05}$</td>
</tr>
<tr>
<td>$a_1$</td>
<td>$-2.1062\times 10^{-04}$</td>
<td>$-3.1196\times 10^{-02}$</td>
<td>$-1.4167\times 10^{-02}$</td>
<td>$-1.8981\times 10^{-07}$</td>
<td>$2.5208\times 10^{-08}$</td>
</tr>
<tr>
<td>$a_2$</td>
<td>$-3.6153\times 10^{-07}$</td>
<td>$3.8017\times 10^{-05}$</td>
<td>$-4.9187\times 10^{-06}$</td>
<td>$2.3150\times 10^{-10}$</td>
<td>$-3.7248\times 10^{-11}$</td>
</tr>
<tr>
<td>$a_3$</td>
<td>$1.5105\times 10^{-10}$</td>
<td>$-2.7416\times 10^{-08}$</td>
<td>$-6.5580\times 10^{-10}$</td>
<td>$-1.6951\times 10^{-13}$</td>
<td>$3.9920\times 10^{-14}$</td>
</tr>
<tr>
<td>$a_4$</td>
<td>$-3.5505\times 10^{-14}$</td>
<td>$8.2107\times 10^{-12}$</td>
<td>$6.6516\times 10^{-14}$</td>
<td>$5.2923\times 10^{-17}$</td>
<td>$-1.6988\times 10^{-17}$</td>
</tr>
<tr>
<td>$b_1$</td>
<td>$3.4451\times 10^{+00}$</td>
<td>$1.9711\times 10^{+01}$</td>
<td>$-1.6377\times 10^{+02}$</td>
<td>$1.8767\times 10^{-03}$</td>
<td>$-2.2451\times 10^{-03}$</td>
</tr>
<tr>
<td>$b_2$</td>
<td>$-5.9472\times 10^{+01}$</td>
<td>$5.5440\times 10^{+03}$</td>
<td>$3.9202\times 10^{+03}$</td>
<td>$-1.9966\times 10^{-02}$</td>
<td>$6.8760\times 10^{-02}$</td>
</tr>
<tr>
<td>$b_3$</td>
<td>$6.1738\times 10^{+02}$</td>
<td>$-1.0178\times 10^{+05}$</td>
<td>$-4.6560\times 10^{+04}$</td>
<td>$1.1511\times 10^{-01}$</td>
<td>$-9.5646\times 10^{-01}$</td>
</tr>
<tr>
<td>$b_4$</td>
<td>$-2.5244\times 10^{+03}$</td>
<td>$5.3097\times 10^{+05}$</td>
<td>$2.0274\times 10^{+05}$</td>
<td>$-2.3378\times 10^{-01}$</td>
<td>$4.5685\times 10^{+00}$</td>
</tr>
<tr>
<td>$c$</td>
<td>$4.6143\times 10^{-02}$</td>
<td>$5.1928\times 10^{+00}$</td>
<td>$-5.4515\times 10^{-01}$</td>
<td>$3.5711\times 10^{-05}$</td>
<td>$-7.7496\times 10^{-06}$</td>
</tr>
</tbody>
</table>

![](./images/812783287536713729_5.jpg)

Figure A1. Fits of temperature optimised cell shape (to-cs) calculated thermodynamic properties using Equation (A1) and coefficients from Table A1 (γ-TiAl, left column) and Table A2 (α₂-Ti₃Al, right column). The actual calculated data are shown by the small coloured points while the fits are thin continuous black lines.

## References

1.  Holec, D.; Zhou, L.; Riedl, H.; Koller, C.M.; Mayrhofer, P.H.; Friák, M.; Šob, M.; Körmann, F.; Neugebauer, J.; Music, D.; et al. Atomistic modeling-based design of novel materials. Adv. Eng. Mater. 2017, 19, 1600688. [CrossRef]

2.  Curtarolo, S.; Hart, G.L.W.; Nardelli, M.B.; Mingo, N.; Sanvito, S.; Levy, O. The high-throughput highway to computational materials design. Nat. Mater. 2013, 12, 191–201. [CrossRef] [PubMed]

3.  Butler, K.T.; Davies, D.W.; Cartwright, H.; Isayev, O.; Walsh, A. Machine learning for molecular and materials science. Nature 2018, 559, 547–555. [CrossRef] [PubMed]

4.  Draxl, C.; Scheffler, M. NOMAD: The FAIR concept for big data-driven materials science. MRS Bull. 2018, 43, 676–682. [CrossRef]

5.  Koutná, N.; Erdely, P.; Zöhrer, S.; Franz, R.; Du, Y.; Liu, S.; Mayrhofer, P.H.; Holec, D. Experimental chemistry and structural stability of AlNb enabled by antisite defects formation. *Materials* **2019**, *12*, 1104. [CrossRef] [PubMed]

6.  Grabowski, B.; Hickel, T.; Neugebauer, J. Ab initio study of the thermodynamic properties of nonmagnetic elementary fcc metals: Exchange-correlation-related error bars and chemical trends. *Phys. Rev. B Condens. Matter* **2007**, *76*, 024309. [CrossRef]

7.  Körmann, F.; Dick, A.; Grabowski, B.; Hallstedt, B.; Hickel, T.; Neugebauer, J. Free energy of bcc iron: Integrated ab initio derivation of vibrational, electronic, and magnetic contributions. *Phys. Rev. B Condens. Matter* **2008**, *78*, 033102. [CrossRef]

8.  Grabowski, B.; Ismer, L.; Hickel, T.; Neugebauer, J. Ab initio up to the melting point: Anharmonicity and vacancies in aluminum. *Phys. Rev. B Condens. Matter Mater. Phys.* **2009**, *79*, 134106. [CrossRef]

9.  Hickel, T.; Grabowski, B.; Körmann, F.; Neugebauer, J. Advancing density functional theory to finite temperatures: Methods and applications in steel design. *J. Phys. Condens. Matter* **2012**, *24*, 053202. [CrossRef]

10. Palumbo, M.; Fries, S.G.; Corso, A.D.; Kürmann, F.; Hickel, T.; Neugebauer, J. Reliability evaluation of thermophysical properties from first-principles calculations. *J. Phys. Condens. Matter* **2014**, *26*, 335401. [CrossRef]

11. Glensk, A.; Grabowski, B.; Hickel, T.; Neugebauer, J. Understanding anharmonicity in fcc materials: From its origin to ab initio strategies beyond the quasiharmonic approximation. *Phys. Rev. Lett.* **2015**, *114*, 195901. [CrossRef] [PubMed]

12. Togo, A.; Tanaka, I. First principles phonon calculations in materials science. *Scr. Mater.* **2015**, *108*, 1–5. [CrossRef]

13. Cui, W.F.; Liu, C.M.; Bauer, V.; Christ, H.J. Thermomechanical fatigue behaviours of a third generation $\gamma$-TiAl based alloy—Advanced intermetallic alloys and bulk metallic glasses 6th international workshop on advanced intermetallic and metallic materials. *Intermetallics* **2007**, *15*, 675–678. [CrossRef]

14. Clemens, H.; Mayer, S. Design, processing, microstructure, properties, and applications of advanced intermetallic TiAl alloys. *Adv. Eng. Mater.* **2013**, *15*, 191–215. [CrossRef]

15. Lasalmonie, A. Intermetallics: Why is it so difficult to introduce them in gas turbine engines? *Intermetallics* **2006**, *14*, 1123–1129. [CrossRef]

16. Appel, F.; Paul, J.; Oehring, M. *Gamma Titanium Aluminide Alloys: Science and Technology*; Wiley: Hoboken, NJ, USA, 2011.

17. Clemens, H.; Mayer, S. Intermetallic titanium aluminides in aerospace applications—Processing, microstructure and properties. *Mater. High Temp.* **2016**, *33*, 560–570. [CrossRef]

18. Kim, Y.W.; Clemens, H.; Rosenberger, A.H. *Gamma Titanium Aluminides 2003*; Minerals, Metals, & Materials Society: Pittsburgh, PA, USA, 2003.

19. Yamaguchi, M.; Inui, H.; Ito, K. High-temperature structural intermetallics. *Acta Mater.* **2000**, *48*, 307–322. [CrossRef]

20. Appel, F.; Wagner, R. Microstructure and deformation of two-phase $\gamma$-titanium aluminides. *Mater. Sci. Eng. R Rep.* **1998**, *22*, 187–268. [CrossRef]

21. Kestler, H.; Clemens, H. Production, processing and application of gamma (TiAl)-based alloys. In *Titanium and Titanium Alloys: Fundamentals and Applications*; Leyens, C., Peters, M., Eds.; WILEY-VCH Verlag GmbH & Co. KGaA: Weinheim, Germany, 2003; pp. 351–392.

22. Wu, X. Review of alloy and process development of TiAl alloys. *Intermetallics* **2006**, *14*, 1114–1122. [CrossRef]

23. Kainuma, R.; Fujita, Y.; Mitsui, H.; Ohnuma, I.; Ishida, K. Phase equilibria among $\alpha$ (hcp), $\beta$ (bcc) and $\gamma$ (L1₀) phases in Ti–Al base ternary alloys. *Intermetallics* **2000**, *8*, 855–867. [CrossRef]

24. Tetsui, T.; Shindo, K.; Kobayashi, S.; Takeyama, M. A newly developed hot worked TiAl alloy for blades and structural components. *Scr. Mater.* **2002**, *47*, 399–403. [CrossRef]

25. Shi, J.D.; Pu, Z.; Zhong, Z.; Zou, D. Improving the ductility of $\gamma$(TiAl) based alloy by introducing disordered $\beta$ phase. *Scr. Metall. Mater.* **1992**, *27*, 1331–1336. [CrossRef]

26. Mayer, S.; Erdely, P.; Fischer, F.D.; Holec, D.; Kastenhuber, M.; Klein, T.; Clemens, H. Intermetallic $\beta$-solidifying $\gamma$-TiAl based alloys—From fundamental research to application. *Adv. Eng. Mater.* **2017**, *19*, 1600735. [CrossRef]

27. Clemens, H.; Wallgram, W.; Kremmer, S.; Güther, V.; Otto, A.; Bartels, A. Design of novel $\beta$-solidifying TiAl alloys with adjustable $\beta$/B2-phase fraction and excellent hot-workability. *Adv. Eng. Mater.* **2008**, *10*, 707–713. [CrossRef]

28. Loretto, M.H.; Godfrey, A.B.; Hu, D.; Blenkinsop, P.A.; Jones, I.P.; Cheng, T.T. The influence of composition and processing on the structure and properties of TiAl-based alloys. *Intermetallics* **1998**, *6*, 663–666. [CrossRef]

29. Holec, D.; Legut, D.; Isaeva, L.; Souvatzis, P.; Clemens, H.; Mayer, S. Interplay between effect of Mo and chemical disorder on the stability of $\beta/\beta_{o}$-TiAl phase. *Intermetallics* **2015**, *61*, 85–90. [CrossRef]

30. Witusiewicz, V.T.; Bondar, A.A.; Hecht, U.; Stryzhyboroda, O.M.; Tsyganenko, N.I.; Voblikov, V.M.; Petyukh, V.M.; Velikanova, T.Y. Thermodynamic re-modelling of the ternary Al-Mo-Ti system based on novel experimental data. *J. Alloys Compd.* **2018**, *749*, 1071–1091. [CrossRef]

31. Nabarro, F. Two-phase materials for high-temperature service. *Intermetallics* **2000**, *8*, 979–985. [CrossRef]

32. Schuh, C.; Dunand, D.C.; Wanner, A.; Clemens, H. Thermal-cycling creep of $\gamma$-TiAl-based alloys. *Intermetallics* **2000**, *8*, 339–343. [CrossRef]

33. Zupan, M.; Hemker, K.J. High temperature microsample tensile testing of $\gamma$-TiAl. *Mater. Sci. Eng. A* **2001**, *319–321*, 810–814. [CrossRef]

34. He, Y.; Schwarz, R.B.; Darling, T.; Hundley, M.; Whang, S.H.; Wang, Z.M. Elastic constants and thermal expansion of single crystal $\gamma$-TiAl from 300 to 750 K—4th conference on high-temperature intermetallics. *Mater. Sci. Eng. A* **1997**, *239–240*, 157–163. [CrossRef]

35. Bittorf, C.; Matthies, S.; Priesmeyer, H.G.; Wagner, R. Diffractive determination of thermo-elastic single crystal constants using polycrystalline samples. I. Thermal expansion of $\gamma$-TiAl from 300 to 900 K. *Intermetallics* **1999**, *7*, 251–258. [CrossRef]

36. Stone, W.; Kurfess, T. *Titanium Aluminide-Thermal Diffusivity, Heat Capacitance, and Coefficient of Thermal Expansion as a Function of Temperature*; Technical Paper; Society of Manufacturing Engineers: Dearborn, MI, USA, 2002; number MR02-143, pp. 1–5.

37. Zhang, W.J.; Reddy, B.V.; Deevi, S.C. Physical properties of TiAl-base alloys. *Scr. Mater.* **2001**, *45*, 645–651. [CrossRef]

38. Novoselova, T.; Malinov, S.; Sha, W.; Zhecheva, A. High-temperature synchrotron X-ray diffraction study of phases in a gamma TiAl alloy. *Mater. Sci. Eng. A* **2004**, *371*, 103–112. [CrossRef]

39. Li, X.; Dippenaar, R.; Shiro, A.; Shobu, T.; Higo, Y.; Reid, M.; Suzuki, H.; Akita, K.; Funakoshi, K.I.; Liss, K.D. Lattice parameter evolution during heating of Ti-45Al-7.5Nb-0.25/0.5C alloys under atmospheric and high pressures. *Intermetallics* **2018**, *102*, 120–131. [CrossRef]

40. Fu, H.; Zhao, Z.; Liu, W.; Peng, F.; Gao, T.; Cheng, X. Ab initio calculations of elastic constants and thermodynamic properties of $\gamma$TiAl under high pressures. *Intermetallics* **2010**, *18*, 761–766. [CrossRef]

41. Kresse, G.; Furthmüller, J. Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set. *Phys. Rev. B Condens. Matter Mater. Phys.* **1996**, *54*, 11169–11186. [CrossRef]

42. Kohn, W.; Sham, L.J. Self-consistent equations including exchange and correlation effects. *Phys. Rev.* **1965**, *140*, A1133–A1138. [CrossRef]

43. Hohenberg, P.; Kohn, W. Inhomogeneous electron gas. *Phys. Rev.* **1964**, *136*, B864–B871. [CrossRef]

44. Perdew, J.P.; Burke, K.; Ernzerhof, M. Generalized gradient approximation made simple. *Phys. Rev. Lett.* **1996**, *77*, 3865–3868. [CrossRef] [PubMed]

45. Kresse, G.; Joubert, D. From ultrasoft pseudopotentials to the projector augmented-wave method. *Phys. Rev. B Condens. Matter Mater. Phys.* **1999**, *59*, 1758–1775. [CrossRef]

46. Togo, A.; Chaput, L.; Tanaka, I.; Hug, G. First-principles phonon calculations of thermal expansion in Ti₃SiC₂, Ti₃AlC₂, and Ti₃GeC₂. *Phys. Rev. B Condens. Matter* **2010**, *81*, 174301. [CrossRef]

47. Birch, F. Finite elastic strain of cubic crystals. *Phys. Rev.* **1947**, *71*, 809–824. [CrossRef]

48. Nakano, T.; Negishi, A.; Hayashi, K.; Umakoshi, Y. Ordering process of Al₅Ti₃, h-Al₂Ti and r-Al₂Ti with f.c.c.-based long-period superstructures in rapidly solidified Al-rich TiAl alloys. *Acta Mater.* **1999**, *47*, 1091–1104. [CrossRef]

49. Daniel, R.; Holec, D.; Bartosik, M.; Keckes, J.; Mitterer, C. Size effect of thermal expansion and thermal/intrinsic stresses in nanostructured thin films: Experiment and model. *Acta Mater.* **2011**, *59*, 6631–6645. [CrossRef]

![](./images/812783287536713729_6.jpg)

© 2019 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (http://creativecommons.org/licenses/by/4.0/).