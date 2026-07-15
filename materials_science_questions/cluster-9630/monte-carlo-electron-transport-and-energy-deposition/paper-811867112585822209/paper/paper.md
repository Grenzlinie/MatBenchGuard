# Calculations of specific cellular doses for low-energy electrons

C.S. Liu $^{a}$, C.-J. Tung $^{a,b,*}$, Y.H. Hu $^{a}$, C.M. Chou $^{a,c}$, T.C. Chao $^{b}$, C.C. Lee $^{b}$

$^{a}$ Department of Biomedical Engineering and Environmental Sciences, National Tsing Hua University, Hsinchu 300, Taiwan
$^{b}$ Department of Medical Imaging and Radiological Sciences, Chang Gung University, Kwei-Shan 333, Taiwan
$^{c}$ Health Physics Division, Institute of Nuclear Energy Research, Loontan 325, Taiwan

---

## ARTICLE INFO

**Article history:**
Received 2 January 2009
Received in revised form 28 February 2009
Available online 12 March 2009

**PACS:**
87.53.Bn
87.53.Ay
87.53.-j

**Keywords:**
Cellular dose, Lineal energy
Microdosimetry
Electron transport

---

## ABSTRACT

The objectives of this work were to calculate the cellular doses and the lineal energies of low-energy electrons in liquid water for different source-target geometry in a cell. Calculated specific cellular doses and their variations were analyzed for the dependences on electron energy, source-target geometry, elastic interaction, and type of energy depositions, i.e. starter, stopper, insider and crosser. Two approaches, i.e. the probabilistic method and the mixed method, were applied. In the probabilistic method, the Monte Carlo Penelope code was used. In the mixed method, the range-energy relation and the sampling of electron paths were applied. It was found that for $\mathrm{N \leftarrow Cy}$ elastic interactions led to a change of the specific cellular dose by about 30% for electron energies below 10 keV. Here $\mathrm{N \leftarrow Cy}$ denotes electrons emitted from the source region, Cy (cytoplasm), to deposit energy in the target region, N (cell nucleus). The variation of specific cellular dose was found greater (more than 10%) for $\mathrm{N \leftarrow Cy}$ than $\mathrm{N \leftarrow N}$, $\mathrm{C \leftarrow C}$ and $\mathrm{C \leftarrow CS}$, where C and CS denote the cell and cell surface, respectively. The lineal energy distribution varied substantially with electron energy, source-target geometry, and target size. The maximum values of the relative dose-mean lineal energy for 1, 5 and 10 keV electrons, relative to 36 keV reference electrons used to define the relative biological effectiveness, occurred at target radii of several tens, hundreds and thousands nanometers, respectively.

© 2009 Elsevier B.V. All rights reserved.

---

## 1. Introduction

In internal radiation dosimetry, the radiation dose from internal radionuclide is usually expressed in terms of the mean absorbed dose to an organ or tissue. The mean absorbed dose to a target organ per nuclear transformation of the radionuclide in a source organ was determined both by the International Commission on Radiological Protection (ICRP) [1] and the Medical Internal Radiation Dose (MIRD) Committee of the Nuclear Medicine Society [2]. Internal radionuclide, however, may not be uniformly distributed in the cell of the organ or tissue. In this case, the mean absorbed dose to a subcellular target per nuclear transformation of the radionuclide in a subcellular source, i.e. the specific cellular dose, is of interest particularly for short-ranged particles. For instance, the specific cellular dose or the cellular S-value has been calculated by MIRD [3] for electrons and alpha particles assuming source regions: whole cell (C), cytoplasm (Cy), cell surface (CS), and cell nucleus (N) and target regions: C and N. Since a deterministic method was used, variations of the calculated results were not predicted. These variations are due to the statistical fluctuation of the energy deposition, referred to as the energy loss straggling [4], for a given pathlength of particles traversing in the target region. Also, elastic interactions have an effect on such variations due to the increase in particle pathlengths [5]. These variations could be significant for electrons particularly of low energies. Furthermore, the specific cellular dose represents the mean absorbed dose from a large number of deposition events. The understanding of the radiobiological effectiveness requires information on the energy deposition from a single-event, i.e. the lineal energy, which characterizes the radiation quality [6,7].

Specific cellular doses may be computed using different approaches, ranging from simple deterministic methods [3,8] to complex probabilistic or Monte Carlo (MC) simulations [9]. A combination of deterministic and probabilistic approaches may also be employed. All these approaches make use of the differential cross sections for elastic and inelastic interactions. In the case of a deterministic method, transport equation [10] is usually solved by applying the continuous slowing-down approximation (CSDA) [11] for inelastic interactions and the multiple scattering assumptions (MSA) [12] for elastic interactions. The results, with accuracy depending on the fulfillment of the CSDA and MSA, contain no information on the straggling. For the probabilistic method, however, an event-by-event trace of electrons [13] for elastic and inelastic interactions is made for a large number of tracks. Average quantities and their variations can then be determined. The MIRD

---

* Corresponding author. Address: Department of Medical Imaging and Radiological Sciences, Chang Gung University, Kwei-Shan 333, Taiwan. Tel.: +886 3 2118800x3614; fax: +886 3 2118620.
E-mail address: cjtung@mx.nthu.edu.tw (C.-J. Tung.)

0168-583X/$ - see front matter © 2009 Elsevier B.V. All rights reserved.
doi:10.1016/j.nimb.2009.03.041

calculations [3], belonging to the deterministic method, made use of the stopping power (obtained from the CSDA) and the geometric reduction factor (based on the MSA). The Penelope code [14], belonging to the probabilistic method, applied the MC technique to electrons down to several hundred eV energies.

In the present work, two approaches, i.e. the probabilistic method and the mixed method, were employed to compute the specific cellular dose and the lineal energy for electrons in liquid water by considering different source-target geometry. Results were analyzed for the dependences on electron energy, source-target configuration, elastic interaction, and type of energy depositions, i.e. starter, stopper, insider and crosser. In the mixed method, a deterministic range-energy relation and a probabilistic random sampling of electron tracks were applied. The range-energy relation was derived from the dielectric response theory [13] by fitting the extended Drude dielectric function to experimental optical data and by considering the correlation and exchange effects. The sampling of electron tracks was performed to determine electron pathlengths inside or through the target region. In the probabilistic method, the Penelope code [14] was adopted. This code employs a mixed algorithm to simulate electron interactions, i.e. through a direct event-by-event simulation for hard collisions and the CSDA/MSA for soft collisions. Secondary electrons and elastic interactions are included in the Penelope code. This code, however, cannot be applied accurately to electrons of energies less than a few hundred eV because of its generic inelastic cross sections employed. In the present work, specific cellular doses calculated for electrons of different energies and source-target geometry using probabilistic and mixed methods were compared with one another and analyzed. In addition, the lineal energy distribution and its associated mean (frequency-mean and dose-mean) values were also calculated and analyzed for the dependence on target dimension from nano- to micro-meters. The dose-mean lineal energy, a microdosimetric analogue of the dose-mean linear energy transfer (LET), gives an indication of radiation quality in the assessments of biological effectiveness.

Most applications of specific cellular doses and lineal energies involved weakly penetrating particles emitted from the non-uniform source distribution in a cell. For example, absorbed dose to the cell nucleus due to the protein-bound tritium was previously calculated for newborn mice whose mother was ingested $^3$H-thymidine during the pregnancy [15,16]. A compound biological effectiveness (CBE) was estimated from the lineal energy distribution of $\alpha$-particles and $^7$Li-ions, produced in the boron neutron capture therapy (BNCT), in the subcellular target [17].

## 2. Methods

In internal dosimetry, radiation dose and radiation quality are mostly expressed in terms of the absorbed dose and the LET. The absorbed dose is generally specified in radiation protection as the specific effective energy (SEE) [1] and in nuclear medicine as the organ S-value [2]. The LET is a measure of the single-event energy deposition excluding the energy loss to bremsstrahlung or delta-ray [18,19]. In cellular dosimetry, radiation dose and radiation quality may be expressed in terms of the cellular S-value, or the specific cellular dose, and the lineal energy. The lineal energy is defined as the single-event energy deposition in a subcellular target region divided by the mean chord length of that region [6]. In calculations of the specific cellular dose, MIRD adopted a deterministic method by applying the stopping power and the geometric reduction factor. Due to difficulties in the deterministic method, elastic interactions and secondary electrons were neglected and stochastic variations were not evaluated. Further, the lineal energy distribution was not calculated. In the current work, a probabilistic method and a mixed method were applied to calculate the specific cellular dose and the lineal energy distribution for low-energy electrons.

In the probabilistic method, Penelope code was used. This code employs the direct event-by-event simulation and the CSDA/MSA to handle hard and soft collisions, respectively. The advantages of using the probabilistic method are that stochastic processes are employed in the determination of electron tracks and interactions. Therefore, secondary electrons and elastic interactions can be easily included. Also, the stochastic variations of the calculated quantities can be readily estimated. It was mentioned that below about 500 eV the cross sections and physics of Penelope code were quite uncertain [9]. These cross sections adopted a generalized oscillator strength (GOS) model for each atomic shell in which single-resonance energy was assumed for the soft interactions [20] and a free target electron was assumed for the hard interactions [21]. In Penelope, the required resonance energy was taken as an adjustable parameter for valence electrons and equal to 1.65 times the binding energy for inner-shells, where the binding energy was obtained from the hydrogenic model. Since sum rules were applied in the GOS model, these cross sections correctly predicted the average behavior of high energy electrons. For low-energy electrons, the atomic shellwise GOS model works less accurate than the condensed medium model such as the dielectric function model which deals with collective excitations and interband transitions.

In the mixed method, the deterministic range-energy relation and the MC sampling of electron tracks were employed. The range-energy relation calculated in the current work is valid for electrons of energy down to $\sim$10 eV in liquid water. Its validity for low-energy electrons is because experimental dielectric function data were used, sum rules were applied, and exchange and correlation effects were included. A detailed discussion on theoretical calculations of the inelastic mean free path and the range-energy relation has been given elsewhere [13]. Other calculations using dielectric functions are also available [19,22,23]. The dielectric model calculations provide more accurate data than the single-pole results of the Penelope code. To compare inelastic cross sections between dielectric model calculations and single-pole results, a brief summary of the dielectric model is described below. The differential inverse mean free path (DIMFP) for an electron of energy $E$ to lose the energy $\omega$, i.e. $\mu(E,\omega)$, may be calculated from the dielectric function $\varepsilon(k,\omega)$ under the Born approximation, where $k$ and $\omega$ are the momentum and energy transfers. The dielectric function may be constructed by considering the valence band as composed of several groups of valence electrons with different oscillator strengths, binding energies, and damping coefficients. This dielectric function is fitted to the optical data of liquid water in the optical limit, i.e. $k \to 0$, to determine fitting parameters. The fitted dielectric function is then extended to the $k \neq 0$ region by applying an asymptotic dispersion relation in the Bethe ridge. The exchange effect is included with reference to the Møller DIMFP [21,24]. With DIMFP, electron CSDA range may be calculated [25].

The specific cellular dose to a target region, $R_{\text{T}}$, from radionuclide in the source region, $R_{\text{S}}$, in a cell may be calculated from

$$
D(R_{\text{T}} \leftarrow R_{\text{S}}) = \frac{\bar{\varepsilon}(R_{\text{T}} \leftarrow R_{\text{S}})}{m_{\text{T}}}, \tag{1}
$$

where $\bar{\varepsilon}(R_{\text{T}} \leftarrow R_{\text{S}})$ is the mean energy deposition in the target region per electron emission from the source region, contributed by all deposition events including those of zero energy deposition, and $m_{\text{T}}$ is the mass of target region. In the deterministic method, $\bar{\varepsilon}(R_{\text{T}} \leftarrow R_{\text{S}})$ may be calculated either from the stopping power and geometry reduction factor or the range-energy relation and sampling of electron tracks. For the probabilistic method, $\bar{\varepsilon}(R_{\text{T}} \leftarrow R_{\text{S}})$ may be determined from simulations of a large number of electrons ($10^7$ in the present work) transporting in liquid water. Contribu-

tions to the specific cellular dose may be due to insiders, starters, stoppers, and crossers, corresponding to electron paths within the target, starting inside and ending outside the target, starting outside and ending insider the target, and crossing the target, respectively.

The lineal energy, $y$, for a source-target geometry is defined by
$$
y\left(R_{\mathrm{T}} \leftarrow R_{\mathrm{S}}\right)=\frac{\varepsilon_{1}\left(R_{\mathrm{T}} \leftarrow R_{\mathrm{S}}\right)}{\bar{\ell}}, \tag{2}
$$
where $\varepsilon_{1}(R_{\mathrm{T}} \leftarrow R_{\mathrm{S}})$ is the single-event energy deposition in the target region from an electron emitted from the source region, considering only the non-zero energy deposition, and $\bar{\ell}$ is the mean chord length of the target volume. There are two mean values of the lineal energy frequency distribution, $f[y(R_{\mathrm{T}} \leftarrow R_{\mathrm{S}})]$, that are of interest. The frequency-mean lineal energy and the dose-mean lineal energy are calculated using
$$
\bar{y}_{\mathrm{F}}\left(R_{\mathrm{T}} \leftarrow R_{\mathrm{S}}\right)=\int_{0}^{\infty} y\left(R_{\mathrm{T}} \leftarrow R_{\mathrm{S}}\right) f\left[y\left(R_{\mathrm{T}} \leftarrow R_{\mathrm{S}}\right)\right] d y\left(R_{\mathrm{T}} \leftarrow R_{\mathrm{S}}\right) \tag{3}
$$
and
$$
\begin{aligned}
\bar{y}_{\mathrm{D}}\left(R_{\mathrm{T}} \leftarrow R_{\mathrm{S}}\right)=& \frac{1}{\bar{y}_{\mathrm{F}}\left(R_{\mathrm{T}} \leftarrow R_{\mathrm{S}}\right)} \int_{0}^{\infty} y^{2}\left(R_{\mathrm{T}} \leftarrow R_{\mathrm{S}}\right) f\left[y\left(R_{\mathrm{T}} \leftarrow R_{\mathrm{S}}\right)\right] \\
& \times d y\left(R_{\mathrm{T}} \leftarrow R_{\mathrm{S}}\right). \tag{4}
\end{aligned}
$$

Here $\bar{y}_{\mathrm{D}}$, an important parameter describing radiation quality for assessing the biological effectiveness, is a microdosimetric analogue of the dose-mean LET. For instance, the International Commission on Radiation Units and Measurements has recommended a mean quality factor, $\bar{Q}$, based on a linear relationship with $\bar{y}_{\mathrm{D}}$ [26]. Further, the relative biological effectiveness (RBE) of electrons with different energies was estimated using the ratio of $\bar{y}_{\mathrm{D}}$ for these electrons to $\bar{y}_{\mathrm{D}}$ for 36 keV electrons [27]. In the present work, the lineal energy distribution and the frequency- and dose-mean lineal energies were calculated for a spherical cell of various source-target geometry. Similar calculations were made for a sub-cellular target of nanometer dimension applicable to the DNA. In this case, DNA was assumed randomly located in the cell nucleus where electron source was uniformly distributed in it. Under this assumption, the distance between source and target could be any value up to the diameter of cell nucleus. It was therefore interesting to study the dependence of lineal energy on the separation between source and target and on the dimension of the target.

### 3. Results and discussion

Dielectric functions of the extended Drude model were fitted to optical data of liquid water [28] to determine the fitting parameters in the dielectric functions. Fitted results were then verified by checking the sum rules [29]. Values of fitting parameters were previously published [13]. Using these dielectric functions, the DIMFP of electrons in liquid water was calculated. Fig. 1 shows a plot of the DIMFP from present calculations (solid curve) for 1 keV electrons in liquid water as a function of energy loss. Corresponding results calculated using the Møller formula (dash curve) and the Penelope code (dot curve) are also plotted. It indicates that the DIMFP using dielectric functions exhibits a broad peak around 24 eV, the DIMFP using Møller formula increases continuously with decreasing energy loss, and the DIMFP using Penelope code shows two sharp peaks (around 16 and 150 eV) contributed from excitations of the valence band and ionizations of the inner-shells. Since the Møller formula is valid only for large energy losses and the sharp peaks differ from measured optical data (in position, width, and height), the DIMFP of either Møller formula or Penelope code works unsatisfactorily for low-energy electrons.

![](./images/811867112585822209_1.jpg)

Fig. 1. The calculated DIMFP for 1 keV electrons in liquid water as a function of energy loss. Solid, dash and dot curves are the results calculated using the dielectric function, Møller formula, and Penelope code, respectively.

A comparison of electron elastic (dash curve) and inelastic (solid curve) inverse mean free paths in liquid water is made in Fig. 2, where calculations were made using the phase-shift analysis [30] for elastic interactions and the dielectric function method for inelastic interactions. It is seen that at low energies electron elastic interactions are more probable than inelastic interactions. Although each elastic interaction leads to a negligible energy loss, the angular deflection of this interaction increases the pathlength and thus contributes to the specific cellular dose. A comparison of electron CSDA range in liquid water is shown in Fig. 3 among results calculated using the dielectric function (solid curve), data given in ICRU (open circles and chain curve) [14,31], and values recommended by MIRD (dash curve) [3].

![](./images/811867112585822209_2.jpg)

Fig. 2. A comparison of electron elastic (dash curve) and inelastic (solid curve) inverse mean free paths in liquid water as a function of electron energy. Results are calculated using the phase-shift analysis for elastic interactions and the dielectric function for inelastic interactions.

Specific cellular doses of electrons were calculated for different source-target geometry and various sizes of cell and cell nucleus. Table 1 lists the specific cellular doses for a typical cell of $R_{\mathrm{C}}$(cell radius) $=5$ $\mu$m and $R_{\mathrm{N}}$(nuclear radius) $=2$ $\mu$m. Column A shows the results obtained using the radiation equilibrium (RE) [32], i.e. the entire electron energy is deposited in the target region, valid for small electron energy and large target size in cases of $\mathrm{N} \leftarrow \mathrm{N}$ and $\mathrm{C} \leftarrow \mathrm{C}$. Column B gives the results published by MIRD [3] for the deterministic method using stopping power and geometric reduction factor. Column C is the results of present calculations for the mixed method using range-energy relation and electron track sampling. Column D provides the results of current calculations for the probabilistic method using Penelope code,

![](./images/811867112585822209_3.jpg)

Fig. 3. Electron CSDA range in liquid water, calculated using the dielectric function (solid curve), as a function of electron energy. Corresponding data given in ICRU (open circles and chain curve) and recommended by MIRD (dash curve) are included for comparisons.

however, without elastic interactions. Column E lists the results of current calculations for the probabilistic method using Penelope code with elastic interactions. In columns D and E, variations of the specific cellular doses are expressed in terms of the standard deviation (in parentheses). Note that the lowest electron energies available in MIRD and Penelope are 1 and 0.5 keV, respectively. These energies are, however, extended to 0.1 keV in the mixed method. A comparison of the results between columns B and C indicates trivial differences, which validate the mixed method. The deviation between results in columns C and D is due to the different cross sections, secondary electrons, and the CSDA. This deviation, expressed in percentage difference, is given under the column: (D − C)/D. The deviation between results in columns D and E is due to elastic interactions. Again, this deviation, in terms of the percentage difference, is given under the column: (E − D)/
D. To analyze these deviations, Table 2 gives data on the fractional contribution from each type of energy depositions, i.e. insider, star-ter, stopper and crosser, to the specific cellular dose using the Penelope code. Here insider refers to the energy deposition of a charged particle emitted and ended inside the target region. Star-ter, stopper and crosser refer to that, respectively, from inside to outside, outside to inside, and outside to outside the target region. In this table, the backscatter contribution, i.e. for electrons travel-ing from inside to outside and then back to inside the target region, is also listed. It is seen that for N ← N the fractional contribution from insiders decreases from 99% at 1 keV to 64% at 10 keV. This reveals that at 1 keV nearly all electron energy is deposited in N as insiders; but at 10 keV a sizable electron energy is deposited

<table>
<caption>Table 1<br>Specific cellular doses of electrons calculated using different methods for cells of radii $R_C$ = 5 μm and $R_N$ = 2 μm.</caption>
<thead>
<tr>
<th>E (keV)</th>
<th colspan="5">$D(N\leftarrow N)$ (Gy emission⁻¹)ᵃ</th>
<th rowspan="2">(D − C)/D (%)</th>
<th rowspan="2">(E − D)/D (%)</th>
</tr>
<tr>
<th></th>
<th>(A) REᵇ</th>
<th>(B) MIRDᶜ</th>
<th>(C) Mixedᵈ</th>
<th>(D) Penelopeᵉ</th>
<th>(E) Penelopeᶠ</th>
</tr>
</thead>
<tbody>
<tr>
<td>0.1</td>
<td>4.77E-04</td>
<td>–</td>
<td>4.77E-04</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>–</td>
</tr>
<tr>
<td>0.5</td>
<td>2.39E-03</td>
<td>–</td>
<td>2.37E-03</td>
<td>2.38E-03(3.73E-07)</td>
<td>2.38E-03(3.39E-07)</td>
<td>0.4</td>
<td>0.0</td>
</tr>
<tr>
<td>1</td>
<td>4.77E-03</td>
<td>4.71E-03</td>
<td>4.71E-03</td>
<td>4.73E-03(1.29E-06)</td>
<td>4.74E-03(1.20E-06)</td>
<td>0.4</td>
<td>0.2</td>
</tr>
<tr>
<td>5</td>
<td>2.39E-02</td>
<td>1.93E-02</td>
<td>1.93E-02</td>
<td>1.96E-02(2.29E-05)</td>
<td>2.05E-02(2.10E-05)</td>
<td>1.5</td>
<td>4.4</td>
</tr>
<tr>
<td>10</td>
<td>4.77E-02</td>
<td>2.04E-02</td>
<td>2.04E-02</td>
<td>2.14E-02(5.26E-05)</td>
<td>2.60E-02(5.74E-05)</td>
<td>4.7</td>
<td>17.7</td>
</tr>
<tr>
<td colspan="8">$D(N\leftarrow Cy)$ (Gy emission⁻¹)ᵃ</td>
</tr>
<tr>
<td>0.1</td>
<td>–</td>
<td>–</td>
<td>2.50E-08</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>–</td>
</tr>
<tr>
<td>0.5</td>
<td>–</td>
<td>–</td>
<td>9.10E-07</td>
<td>6.23E-07(1.00E-7)</td>
<td>4.79E-07(9.08E-08)</td>
<td>–46.1</td>
<td>–30.1</td>
</tr>
<tr>
<td>1</td>
<td>–</td>
<td>4.77E-06</td>
<td>4.80E-06</td>
<td>3.80E-06(3.54E-07)</td>
<td>2.86E-06(3.01E-07)</td>
<td>–26.3</td>
<td>–32.9</td>
</tr>
<tr>
<td>5</td>
<td>–</td>
<td>3.15E-04</td>
<td>3.12E-04</td>
<td>2.91E-04(6.69E-6)</td>
<td>2.34E-04(6.21E-06)</td>
<td>–7.2</td>
<td>–24.4</td>
</tr>
<tr>
<td>10</td>
<td>–</td>
<td>1.89E-03</td>
<td>1.87E-03</td>
<td>1.81E-03(2.25E-05)</td>
<td>1.50E-03(2.06E-05)</td>
<td>–3.3</td>
<td>–24.4</td>
</tr>
<tr>
<td colspan="8">$D(C\leftarrow C)$ (Gy emission⁻¹)ᵃ</td>
</tr>
<tr>
<td>0.1</td>
<td>3.06E-05</td>
<td>–</td>
<td>3.06E-05</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>–</td>
</tr>
<tr>
<td>0.5</td>
<td>1.53E-04</td>
<td>–</td>
<td>1.52E-04</td>
<td>1.53E-04(1.53E-08)</td>
<td>1.53E-04(1.38E-08)</td>
<td>0.7</td>
<td>0.0</td>
</tr>
<tr>
<td>1</td>
<td>3.06E-04</td>
<td>3.04E-04</td>
<td>3.04E-04</td>
<td>3.05E-04(5.20E-08)</td>
<td>3.05E-04(4.90E-08)</td>
<td>0.3</td>
<td>0.0</td>
</tr>
<tr>
<td>5</td>
<td>1.53E-03</td>
<td>1.41E-03</td>
<td>1.41E-03</td>
<td>1.42E-03(1.01E-06)</td>
<td>1.44E-03(9.18E-7)</td>
<td>0.7</td>
<td>1.4</td>
</tr>
<tr>
<td>10</td>
<td>3.06E-03</td>
<td>2.30E-03</td>
<td>2.29E-03</td>
<td>2.32E-03(3.37E-06)</td>
<td>2.47E-03(3.03E-06)</td>
<td>1.3</td>
<td>6.1</td>
</tr>
<tr>
<td colspan="8">$D(C\leftarrow CS)$ (Gy emission⁻¹)ᵃ</td>
</tr>
<tr>
<td>0.1</td>
<td>–</td>
<td>–</td>
<td>1.53E-05</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>–</td>
</tr>
<tr>
<td>0.5</td>
<td>–</td>
<td>–</td>
<td>7.63E-05</td>
<td>7.63E-05(2.17E-07)</td>
<td>7.65E-05(2.08E-07)</td>
<td>0.0</td>
<td>0.3</td>
</tr>
<tr>
<td>1</td>
<td>–</td>
<td>1.52E-04</td>
<td>1.52E-04</td>
<td>1.52E-04(4.28E-07)</td>
<td>1.53E-04(3.98E-07)</td>
<td>0.0</td>
<td>0.7</td>
</tr>
<tr>
<td>5</td>
<td>–</td>
<td>7.25E-04</td>
<td>7.24E-04</td>
<td>7.28E-04(2.17E-06)</td>
<td>7.36E-04(2.05E-6)</td>
<td>0.6</td>
<td>1.1</td>
</tr>
<tr>
<td>10</td>
<td>–</td>
<td>1.27E-03</td>
<td>1.27E-03</td>
<td>1.28E-03(4.28E-06)</td>
<td>1.33E-03(3.98E-06)</td>
<td>0.8</td>
<td>3.8</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="8">ᵃ Numbers in parentheses are the standard deviation of the specific cellular dose.</td>
</tr>
<tr>
<td colspan="8">ᵇ Results calculated using the radiation equilibrium.</td>
</tr>
<tr>
<td colspan="8">ᶜ Data published by MIRD [3].</td>
</tr>
<tr>
<td colspan="8">ᵈ Results calculated using the mixed method.</td>
</tr>
<tr>
<td colspan="8">ᵉ Results calculated using the Penelope code without elastic interactions.</td>
</tr>
<tr>
<td colspan="8">ᶠ Results calculated using the Penelope code with elastic interactions.</td>
</tr>
</tfoot>
</table>

<table>
<caption>Table 2<br>Fractional contribution to the specific cellular dose from different types of energy deposition events for various source-target geometry with $R_C$ = 5 μm and $R_N$ = 2 μm.</caption>
<thead>
<tr>
<th>Type</th>
<th>Event</th>
<th colspan="3">Fractional contribution</th>
</tr>
<tr>
<th></th>
<th></th>
<th>1 keV</th>
<th>5 keV</th>
<th>10 keV</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="3">$N\leftarrow N$</td>
<td>Insiders</td>
<td>0.9945</td>
<td>0.9017</td>
<td>0.6431</td>
</tr>
<tr>
<td>Starters</td>
<td>0.0035</td>
<td>0.0646</td>
<td>0.2602</td>
</tr>
<tr>
<td>Backscatter</td>
<td>0.0020</td>
<td>0.0337</td>
<td>0.0967</td>
</tr>
<tr>
<td rowspan="3">$N\leftarrow Cy$</td>
<td>Stopper</td>
<td>0.8812</td>
<td>0.8612</td>
<td>0.7980</td>
</tr>
<tr>
<td>Crosser</td>
<td>0.0777</td>
<td>0.0860</td>
<td>0.1343</td>
</tr>
<tr>
<td>Backscatter</td>
<td>0.0411</td>
<td>0.0528</td>
<td>0.0677</td>
</tr>
<tr>
<td rowspan="3">$C\leftarrow C$</td>
<td>Insider</td>
<td>0.9979</td>
<td>0.9653</td>
<td>0.8772</td>
</tr>
<tr>
<td>Starter</td>
<td>0.0014</td>
<td>0.0218</td>
<td>0.0824</td>
</tr>
<tr>
<td>Backscatter</td>
<td>0.0007</td>
<td>0.0129</td>
<td>0.0404</td>
</tr>
<tr>
<td rowspan="3">$C\leftarrow CS$</td>
<td>Stopper</td>
<td>0.8159</td>
<td>0.7927</td>
<td>0.7607</td>
</tr>
<tr>
<td>Crosser</td>
<td>0.0951</td>
<td>0.0980</td>
<td>0.1214</td>
</tr>
<tr>
<td>Backscatter</td>
<td>0.0890</td>
<td>0.1093</td>
<td>0.1179</td>
</tr>
</tbody>
</table>

![](./images/811867112585822209_4.jpg)

Fig. 4. The variation of the specific cellular dose, in terms of the relative standard deviation, as a function of electron energy for $C \leftarrow C$, $C \leftarrow CS$, $N \leftarrow Cy$ and $N \leftarrow N$ with $R_C = 5$ $\mu$m and $R_N = 2$ $\mu$m.

in N as starters and backscatters. Since insiders correspond to the total energy deposition, no variation on the energy deposition is re- sulted. Therefore, it is conceivable that the more fractional contri- bution from starters and backscatters, the larger is the variation of the specific cellular dose. This variation comes from the energy loss straggling and the unbalance of scatter-in and scatter-out second- ary electrons in starters and backscatters. Fig. 4 plots the relative variation of the specific cellular dose, i.e. the ratio of standard devi- ation to the specific cellular dose given in column D of Table 1, according to the four types of energy depositions. It is seen that for $N \leftarrow N$ the relative variation increases with electron energy, confirming the increased values in column $(D-C)/D$ of Table 1 with electron energy. In the case of $N \leftarrow Cy$, the energy deposition types become stoppers, crossers and backscatters (see Table 2). All these types generate variation in electron energy deposition in the target region. Therefore, the relative variation of the specific cellu- lar dose (see Fig. 4) is larger for $N \leftarrow Cy$ than for $N \leftarrow N$. This vari- ation may be greater than 10% for low-energy electrons in the case of $N \leftarrow Cy$. In Table 1, the last column indicates the effect of elastic interactions on the specific cellular dose. It shows that for $N \leftarrow Cy$ elastic interactions lead to a change of the specific cellular dose by about 30% for electron energies below 10 keV. To summarize, the Penelope code calculates the specific cellular dose and its variation by direct simulations including secondary electrons and elastic interactions. Due to the limitation of cross sections in the Penelope code, it is less accurate to use the code to compute the specific cel- lular dose for low-energy electrons.

Fig. 5 plots the frequency distribution of lineal energy calcu- lated using the Penelope code for $N \leftarrow N$, $R_C = 5$ $\mu$m, $R_N = 2$ $\mu$m, and several electron energies, $E$. Note that only distributions with non-zero lineal energy $(y \neq 0)$ are shown in this figure. For $E=5$ and 10 keV, there exists delta function peaks at the lineal energy $y = E/\bar{\ell}$, corresponding to insiders. Below this lineal energy, the $y$ distribution increases with decreasing $y$, corresponding to starters with decreasing electron pathlengths in N. For $E=50$ keV, the delta function peak disappears because in this case electron range is greater than the target size. Therefore, the $y$ distribution is entirely contributed from starters. To understand the two peaks in the $y$ distribution for $E=50$ keV, it is shown in Fig. 6 the frequency dis- tribution of electron total pathlength in N. For 5 and 10 keV, this distribution is composed of two parts, i.e. the peak at larger path- lengths and the linear descending portion at smaller pathlengths. The peak and the descending portion correspond to insiders, with peak width related to the pathlength straggling, and starters, respectively. For 50 keV, this distribution, a broad half peak, corre- sponds to starters with a tail (see the insert in the figure) extending to large pathlengths. The tail indicates that the total zigzag step- wise pathlength can be greater than the diameter of N, i.e. 4 $\mu$m. Although the frequency distribution of this tail is small, it results in a small peak (note that $f(y)$ is in logarithm scale) at

![](./images/811867112585822209_5.jpg)

Fig. 5. The frequency distribution of the lineal energy for different electron energies and $N \leftarrow N$ with $R_C = 5$ $\mu$m and $R_N = 2$ $\mu$m. Only non-zero lineal energies are shown. Contributions from different types of deposition events, i.e. insiders and starters, are labeled by the curves.

![](./images/811867112585822209_6.jpg)

Fig. 6. The frequency distribution of electron total pathlength in N for $N \leftarrow N$ with $R_C = 5$ $\mu$m and $R_N = 2$ $\mu$m. The insert is a zoom-in distribution showing pathlengths greater than 4 $\mu$m for 50 keV electrons.

![](./images/811867112585822209_7.jpg)

Fig. 7. The frequency distribution of the lineal energy for different electron energies and $N \leftarrow Cy$ with $R_C = 5$ $\mu$m and $R_N = 2$ $\mu$m. Only non-zero lineal energies are shown. Contributions from different types of deposition events, i.e. stoppers and crossers, are labeled by the curves.

<table><caption>Table 3
The frequency-mean lineal energy and the most probable lineal energy for different electron energies and source-target geometry with $R_{C}=5\ \mu$m and $R_{N}=2\ \mu$m.</caption>
<tbody>
<tr>
<td>$E$ (keV)</td>
<td colspan="6">$\bar{y}_{F},y_{mp}$ (keV $\mu$m$^{-1}$)</td>
</tr>
<tr>
<td>
</td>
<td>$N\leftarrow N$</td>
<td>$N\leftarrow Cy$</td>
<td>$C\leftarrow C$</td>
<td>$C\leftarrow CS$</td>
<td>$N\leftarrow CS$</td>
</tr>
<tr>
<td>0.5</td>
<td>0.188, 0.188</td>
<td>0.120, 0.188</td>
<td>0.073, 0.075</td>
<td>0.058, 0.075</td>
<td>0.000, 0.000</td>
</tr>
<tr>
<td>1</td>
<td>0.370, 0.375</td>
<td>0.234, 0.375</td>
<td>0.148, 0.150</td>
<td>0.114, 0.150</td>
<td>0.000, 0.000</td>
</tr>
<tr>
<td>5</td>
<td>1.615, 1.875</td>
<td>1.139, 1.875</td>
<td>0.707, 0.750</td>
<td>0.552, 0.750</td>
<td>0.000, 0.000</td>
</tr>
<tr>
<td>10</td>
<td>2.059, 3.750</td>
<td>2.062, 3.750</td>
<td>1.215, 1.500</td>
<td>1.041, 1.500</td>
<td>0.000, 0.000</td>
</tr>
<tr>
<td>50</td>
<td>0.372, 0.0581</td>
<td>0.612, 0.493</td>
<td>0.379, 0.023</td>
<td>0.502, 0.023</td>
<td>0.648, 0.523</td>
</tr>
<tr>
<td>100</td>
<td>0.225, 0.0581</td>
<td>0.363, 0.264</td>
<td>0.225, 0.023</td>
<td>0.296, 0.023</td>
<td>0.381, 0.257</td>
</tr>
</tbody>
</table>

$y\sim1.5$ keV/$\mu$m in Fig. 5. The other peak at smaller $y$ in Fig. 5 is con- tributed from starters of smaller pathlengths. A similar plot of the results for $N\leftarrow Cy$ is shown in Fig. 7. Here the distributions for 5, 10, and 50 keV are mainly contributed from, stoppers, stoppers plus crossers, and crossers, respectively. Similar interpretations of these distributions can be made accordingly. Although the fre- quency- and dose-mean lineal energies, $\bar{y}_{F}$ and $\bar{y}_{D}$, are frequently adopted to characterize the lineal energy distribution, the most probable value of this distribution, $y_{mp}$, is also of significance. This is especially true when the distribution is skew or composed of delta peaks such as those shown in Figs. 5 and 7. Table 3 is the re- sults of calculated $\bar{y}_{F}$ and $y_{mp}$ for different source-target geometry with $R_{C}=5\ \mu$m and $R_{N}=2\ \mu$m. It is visible that in all cases electrons of 10 keV have the maximum values in their mean and most prob- able lineal energies than other electron energies. This is because 10 keV electrons have a range close to the target mean chord length (see Fig. 2).

Since most radiobiological effects are initiated by the energy deposition in nanometer sized subcellular structures like DNA, the frequency- and dose-mean lineal energies in a sensitive vol- ume of nanometer dimension were also calculated. These mean lineal energies are plotted in Fig. 8 (Panel A) for different electron energies as a function of target radius from nano- to micro-meter scales. Here electrons are assumed to be emitted from the center of a spherical target of different radii. It is seen that there are local maximum values of mean lineal energies for 1, 5 and 10 keV elec- trons at target radii of several tens, hundreds and thousands nano- meters, respectively. Therefore, electrons of energy in the order of 10 keV have the maximum radiation quality for a cellular target of micrometer dimension. Whereas, electrons of energy in the order of 1 keV have the optimal radiation quality for a subcellular target of nanometer dimension. Panel B of Fig. 8 plots the ratio of $\bar{y}_{D}$ for a given electron energy to $\bar{y}_{D}$ for 36 keV in a spherical target with dif- ferent radii. This ratio serves as an indicator of the low-dose RBE for electrons of different energies [27]. It reveals that the maxi- mum value of this ratio occurs at a target size from nano- to mi- cro-meter for electron energies from 1 to 10 keV.

![](./images/811867112585822209_8.jpg)

Fig. 8. (Panel A) The frequency- and dose-mean lineal energies, $\bar{y}_{F}$ and $\bar{y}_{D}$, in a target volume ranging from nanometer to micrometer dimensions for different electron energies. (Panel B) The ratio of $\bar{y}_{D}$ for a given electron energy to $\bar{y}_{D}$ for 36 keV as a function of target radius for different electron energies.

## 4. Conclusions
The specific cellular dose represents the mean absorbed dose to a subcellular target due to radiations emitted from a subcellular source per radiation emission. This cellular dose and its variation are of special interest for short-ranged particles and non-uniform source distributions. Low-energy electrons irradiate a subcellular target, e.g. the cell nucleus, and deposit their energy in the target from contributions of crossers, stoppers, starters and insiders. Both the energy deposition and the pathlength of electrons in the target straggle due to statistical variation and, therefore, result in the var- iation of the specific cellular dose. In the current work, the specific cellular dose and its variation were estimated using MC simula- tions including the contributions from elastic interactions and sec- ondary electrons. It was found that for $N\leftarrow Cy$ the relative variation might be quite large.

In addition to the specific cellular dose, the single-event size or lineal energy is also of interest for the description of radiation qual- ity. The specific cellular dose relates to the mean energy deposition from all emitted electrons including those of zero energy deposi- tion. The lineal energy, however, describes the energy deposition from a single-event excluding the zero energy deposition. It was found that the lineal energy distribution varied substantially with electron energy, source-target geometry, and target size. In the current work, the lineal energy distribution and the frequency- and dose-mean lineal energies in a subcellular target were calcu- lated and analyzed.

The specific cellular dose and the lineal energy may be applied to the OBT internal dosimetry of low-energy electrons. They may also be applied to the BNCT cellular dosimetry of alpha particles and lithium ions. These applications require data on the subcellular distributions of radiation sources, which are difficult to obtain. More applications of specific cellular dose and lineal energy need to be explored.

## Acknowledgements
This research was supported by the National Science Council of the Republic of China and the Chang Gung Medical Research Program.

## References
[1] ICRP, Limits for Intakes of Radionuclides by Workers, ICRP Publication 30, Elsevier, Oxford, 1982.

[2] R. Loevinger, T.F. Budinger, E.E. Watson, MIRD Primer for Absorbed Dose Calculations, Revised Edition, The Society of Nuclear Medicine, Reston, VA, 1991.

[3] S.M. Goddu, R.W. Howell, L.G. Bouchet, W.E. Bolch, D.V. Rao, MIRD Cellular S Values, The Society of Nuclear Medicine, Reston, VA, 1997.

[4] C.J. Tung, L.Y. Yu, Radiat. Effects 100 (1986) 129.

[5] C.J. Tung, C.P. Wang, IEEE Trans. Nucl. Sci. 30 (1983) 4409.

[6] H.H. Rossi, M. Zaider, Microdosimetry and its Applications, Springer, Berlin, 1996.

[7] ICRU, Fundamental Quantities and Units for Ionizing Radiation, ICRU Report 60, International Commission on Radiation Units and Measurements, 7910 Woodmont Avenue, Bethesda, MD 20814, 1998.

[8] C.J. Tung, C.S. Liu, J.P. Wang, S.L. Chang, Appl. Radiat. Isotop. 61 (2004) 739.

[9] R.D. Stewart, W.E. Wilson, J.C. McDonald, D.J. Strom, Med. Biol. 47 (2002) 79.

[10] C.J. Tung, R.H. Ritchie, Phys. Rev. B 16 (1977) 4302.

[11] K. Kowari, Phys. Rev. A 41 (1990) 2500.

[12] Y.F. Chen, C.M. Kwei, C.J. Tung, J. Phys. D 25 (1992) 262.

[13] C.J. Tung, T.C. Chao, H.W. Hsieh, W.T. Chan, Nucl. Instr. and Meth. B 262 (2007) 231.

[14] F. Salvat, J.M. Fernández-Varea, E. Acosta, J. Sempau, Penelope: a code system for Monte Carlo simulation of electron and photon transport, in: Workshop Proceedings Issy-les-Moulineaux, OECD, Paris, 2001.

[15] M. Saito, M.R. Ishida, C. Streffer, M. Molls, Health Phys. 48 (1985) 465.

[16] M. Saito, M.R. Ishida, C.C. Travis, Health Phys. 56 (1989) 869.

[17] C.S. Liu, C.J. Tung, in: Y. Nakagawa, T. Kobayashi, H. Fukuda (Eds.), Proceedings of the 12th International Congress on Neutron Capture Therapy, International Society for Neutron Capture Therapy, 2006, p. 183.

[18] ICRU, Linear Energy Transfer, ICRU Report 16, International Commission on Radiation Units and Measurements, 7910 Woodmont Avenue, Bethesda, MD 20814, 1970.

[19] D.E. Watt, Quantities for Dosimetry of Ionizing Radiations in Liquid Water, Taylor & Francis, London, 1996.

[20] D. Liljequist, J. Phys. D 16 (1983) 1567.

[21] C. Møller, Ann. Physik. 14 (1932) 531.

[22] D. Emfietzoglou, F.A. Cucinotta, H. Nikjoo, Radiat. Res. 164 (2005) 202.

[23] C.J. Powell, A. Jablonski, NIST Standard Reference Database 71, NIST Electron Inelastic-Mean-Free-Path Database: Version 1.1, <http://www.nist.gov/srd/nist71.htm>.

[24] W.R. Ferrell, R.H. Ritchie, T.L. Ferrell, Am. J. Phys. 52 (1984) 915.

[25] C.J. Tung, C.M. Kwei, J. Phys. 17 (1979) 1.

[26] ICRU, The Quality Factor in Radiation Protection, ICRU Report 40, International Commission on Radiation Units and Measurements, 7910 Woodmont Avenue, Bethesda, MD 20814, 1986.

[27] D. Frankenberg, K. Kelnhofer, K. Bar, M. Frankenberg-Schwager, Radiat. Res. 157 (2002) 99.

[28] E.D. Palik (Ed.), Handbook of Optical Constants of Solids II, Academic Press, New York, 1991.

[29] D. Stroud, Phys. Rev. B 19 (1979) 1783.

[30] Y.F. Chen, P. Su, C.M. Kwei, C.J. Tung, Phys. Rev. B 50 (1994) 17547.

[31] ICRU, Stopping Powers for Electrons and Positions, ICRU Report 37, International Commission on Radiation Units and Measurements, 7910 Woodmont Avenue, Bethesda, MD 20814, 1989.

[32] G.A. Carlsson, in: K.R. Kase, B.E. Bjarngard, F.H. Attix (Eds.), The Dosimetry of Ionizing Radiation, vol. I, Academic Press, New York, 1985, p. 1.