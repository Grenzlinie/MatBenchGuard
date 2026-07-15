Accepted Manuscript

A first-principles investigation of interstitial defects in dilute tungsten alloys

Leili Gharaee, Paul Erhart

![](./images/814598975821709312_1.jpg)

PII: S0022-3115(15)30193-8

DOI: 10.1016/j.jnucmat.2015.09.003

Reference: NUMA 49312

To appear in: *Journal of Nuclear Materials*

Received Date: 26 February 2015

Revised Date: 31 August 2015

Accepted Date: 1 September 2015

Please cite this article as: L. Gharaee, P. Erhart, A first-principles investigation of interstitial defects in dilute tungsten alloys, Journal of Nuclear Materials (2015), doi: 10.1016/j.jnucmat.2015.09.003.

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

![](./images/814598975821709312_2.jpg)

# A first-principles investigation of interstitial defects in dilute tungsten alloys

Leili Gharaee, Paul Erhart*

Department of Applied Physics, Chalmers University of Technology, S-412 67 Gothenburg, Sweden

## Abstract
The thermodynamic properties of intrinsic and extrinsic (Ti, V, Zr, Nb, Hf, Ta, Re) defects in tungsten have been investigated using density functional theory calculations. The formation energies of substitutional defects are discussed with respect to their thermodynamic solubility limits. Several different interstitial configurations have been identified as local minima on the potential energy surface. In addition to dumbbell configurations with orientations along $\langle 111 \rangle$ and $\langle 110 \rangle$, a lower symmetry configuration is described, which is referred to as a bridge interstitial. This interstitial type is found to be the lowest energy configuration for mixed-interstitials containing Ti, V, and Re, and can be up to 0.2 eV lower in energy than the other configurations. According to the calculations Ti, V and Re also trap self-interstitial atoms, which can be produced in substantial numbers during ion irradiation, affecting the mobility of the latter.

© 2015 Published by Elsevier Ltd.

**Keywords:** tungsten alloys, defects, interstitials, ion irradiation, trapping, radiation–induced segregation

## 1. Introduction

Tungsten alloys are considered for structural applications in fusion reactors, especially for armor materials at the divertor and first wall [1–4]. This interest is motivated by promising physical properties such as high melting point, low coefficient of thermal expansion, high thermal conductivity, and high sputtering resistance. Alloy formation occurs naturally during fusion reactor operation due to nuclear transmutation caused by high energy neutron exposure [5]. In this fashion pure tungsten will gradually evolve into an W–Re–Os–Ta alloy [6]. Alloying has also been suggested to lower the temperature range in which the fracture mode of pure tungsten changes from ductile to brittle [7, 8]. The latter intersects with the operation temperature window of current and future fusion reactors [2, 9], which causes concern with regard to mechanical integrity. Since alloying affects many properties of importance including mechanical performance, thermal conductivity, as well as swelling under irradiation, it is important to develop our understanding of tungsten alloys under the relevant conditions [10].

With regard to applications in fusion reactors one must in particular consider the performance of the material under ion irradiation, which causes the localized production of lattice defects such as vacancies and interstitials [11, 12]. Whereas vacancies are relatively immobile, interstitials in pure tungsten can migrate extremely fast [13] allowing for efficient defect recombination, which is a crucial factor with respect to radiation tolerance [14]. In alloys solute atoms and interstitials can potentially bind to each other, reducing the mobility of the latter and possibly accelerating damage buildup compared to the pure material.

An assessment of different alloys for applications in fusion environments should thus invoke information regarding the interaction of intrinsic point defects, solute atoms, and dislocations. As such information is difficult to obtain experimentally, computational modelling plays an important role in investigating the fundamental limits of materials performance. Since the problem at hand involves many length and time lengths, a multiscale modelling approach must be employed. In this context, first-principles calculations can provide critical microscopic parameters that cannot be accessed otherwise. While pure tungsten has been studied extensively, see e.g., Ref. [15], our understanding of alloy behavior is still in its infancy. Recent first-principles calculations considered the energetics of intrinsic defects and solute atoms for a range of transition elements and identified chemical trends across the periodic table [16]. The

*Corresponding author: erhart@chalmers.se

migration behavior has been investigated using a similar ap- proach for the two dominant products of nuclear transmutation (Re, Os) [6]. There is also information available regarding the interaction of substitutional Re with dislocations and its effect on lattice expansion [17].

The objective of the present paper is to deepen our under- standing of the interaction of alloy elements with intrinsic de- fects (formation and binding energies) and to provide param- eters that characterize the elastic long-range interactions be- tween different defects (formation volume tensors) in particular with respect to dislocations [17]. The focus is on refractory el- ements that are close to W in the periodic table and possess a similar electronic structure. The paper provides a careful analy- sis of the computational parameters that affect the convergence of the respective data. For Ti, V, and Re, a low symmetry inter- stitial configuration is observed, referred to as a bridge intersti- tial, which is between 0.05 and 0.2 eV lower in energy than the commonly investigated dumbbell configurations [16]. For these three elements, we also find a strong binding to self-interstitial atoms (SIAs), on a scale which prohibits detrapping on realistic time scales. The analysis of the formation volume tensors re- veals a very strong elastic anisotropy for the interstitial defects, which can be expected to enhance long-range defect-defect in- teraction and alignment.

## 2. Methodology

### 2.1. Computational details

Calculations were performed within density functional the- ory (DFT) using the projector augmented wave (PAW) method [18, 19] as implemented in the Vienna ab-initio simulation pack- age [20-23]. Exchange-correlation effects were treated within the generalized gradient approximation as parametrized by Perdew, Burke and Ernzerhof [24] and the occupation of electronic states was performed using the first order Methfessel-Paxton scheme with a smearing width of 0.2 eV. Defect configurations based on supercells with up to 250 atoms were considered corresponding to $5 \times 5 \times 5$ repetitions of the conventional (2-atom) unit cell. For structural optimizations the atomic coordinates as well as the cell metric were relaxed until the atomic forces were con- verged to within $20 meV/\AA$ and the residual stresses were less than 0.2 GPa. A plane wave energy cutoff energy of 300 eV was employed; increasing the cutoff energy up to 500 eV led to changes in formation and binding energies by less than 0.02 eV. We furthermore carefully considered the effects of Brillouin zone sampling, supercell size, and semicore states on the for- mation and binding energies as detailed in Sect. 3.1 below.

### 2.2. Thermodynamic relations

Defect formation energies were calculated using a well es- tablished thermodynamic formalism [25] (also see Ref. [26])

$$
E^{f}=E^{\text{defect}}-E^{\text{ideal}}-\sum_{i} \Delta n_{i} \mu_{i}, \tag{1}
$$

where $E^{defect}$ is the energy of the defective system and $E^{ideal}$ is the total energy of the perfect reference cell. The variation of the formation energy with the chemical environment is given by the last term in Eq. (1), which involves the chemical poten- tials of the constituents. The difference between the number of atoms of type $i$ in the reference cell and the defective cell is de- noted by $\Delta n_{i}$, where positive and negative values correspond to the addition and removal of an atom relative to the ideal cell, respectively. Here, we take the chemical potential $\mu_{i}$ of each constituent to be identical to its cohesive energy per atom [26].

The binding energy between solute atoms and point defects is a key factor for understanding the thermodynamic properties of alloys [27, 28]. It is given by the difference between forma- tion energies of the mixed-interstitial, $E^{f}([X-W]_{W})$, and the sum of formation energy of the self-interstitial, $E^{f}([W-W]_{W})$, and substitutional configurations, $E^{f}(X)_{W}$,

$$
E_{X}^{b}=E^{f}\left([X-\mathrm{W}]_{\mathrm{W}}\right)-E^{f}\left([\mathrm{W}-\mathrm{W}]_{\mathrm{W}}\right)-E^{f}\left(X_{\mathrm{W}}\right). \tag{2}
$$

In this notation, the binding energy corresponds to the quasi- chemical reaction

$$
\underbrace{(\mathrm{W}-\mathrm{W})_{\mathrm{W}}}_{\text{self-interstitial}}+\underbrace{X_{\mathrm{W}}}_{\text{extrinsic substitutional defect}} \stackrel{E_{X}^{b}}{\longrightarrow} \underbrace{(X-\mathrm{W})_{\mathrm{W}}}_{\text{mixed interstitial}}.
$$

Negative binding energies thus imply an attractive interaction between SIA and extrinsic substitutional defect.

The elastic distortion caused by a defect can be quantified by its formation volume tensor [29-31]. It determines the long- range elastic interaction between defects including but not lim- ited to point and line defects. Given the cell metrics of the ideal supercell $L_{0}$ and the fully relaxed supercell containing the de- fect $L$, the formation volume tensor can be obtained from therelation [29, 31]

$$
v^{f}=\operatorname{det}\left(\boldsymbol{L}_{\mathbf{0}}\right) \ln \left(\boldsymbol{L}_{\mathbf{0}}{ }^{-1} \boldsymbol{L}\right) \approx \operatorname{det}\left(\boldsymbol{L}_{\mathbf{0}}\right)\left(\boldsymbol{L}-\boldsymbol{L}_{\mathbf{0}}{ }^{-1}\right) \boldsymbol{L}_{\mathbf{0}}^{-1}. \tag{3}
$$

The formation volume equals one third of the trace of the for- mation volume tensor. By diagonalizing the formation volume tensor one obtains the orientation and the strength of the strain field. The former is specified by the eigenvectors whereas the latter is related to the magnitude of the eigenvalues. In particu- lar, we consider below the anisotropy defined here as the ratio of the largest to the smallest eigenvalue.

## 3. Results and discussion

### 3.1. Convergence considerations

#### 3.1.1. Brillouin zone sampling

The calculation of defect formation energies in metallic sys- tems via density functional theory calculations and the super- cell approach is subject to several sources of errors most impor- tantly the sampling of the Brillouin zone via a discrete $k$-point mesh, the interaction between periodic images of the same de- fect, and the treatment of semicore states. The first aspect re- sults from the fact that defects in metals act as perturbations, which can cause long-range oscillations in the electronic struc- ture (Friedel oscillations). To capture these oscillations it is not uncommon that one requires a denser $k$-point mesh than for the

![](./images/814598975821709312_3.jpg)

Figure 1. Convergence of the formation energies of (a) vacancy, (b) Ti bridge interstitial, (c) and substitutional Ti with $k$-point density for different system sizes. (d) Finite size scaling of formation energies for Ti interstitial defects. The defect configurations are schematically shown in Fig. 3. The calculations shown here did not include semicore states.

corresponding defect free system. This is illustrated in Fig. 1(a) for the W vacancy. It is apparent from these data that even for a 250-atom cell ($5 \times 5 \times 5$ conventional unit cells) one requires at least a $5 \times 5 \times 5$ Monkhorst-Pack mesh in order to converge the formation energy to better than 0.1 eV; this is equivalent to a $25 \times 25 \times 25$ mesh with respect to the primitive unit cell. For comparison, a $15 \times 15 \times 15$ Monkhorst-Pack is sufficient to converge the total energy of a primitive cell to better than 1 meV/atom. In the case of interstitials, which are also strong perturbation centers, the formation energies exhibit a slightly smaller yet still pronounced variation than for the vacancy as illustrated in Fig. 1(b). Finally, for substitutional defects the effect is rather weak as shown for substitutional Ti in Fig. 1(c). An extensive data set of calculated formation energies provided in the appendix demonstrates that the aforedescribed effects are present for all alloying elements considered in the present study. All formation energies discussed in Sect. 3.2 were calculated using a $6 \times 6 \times 6$ Monkhorst-Pack grid in order to minimize Brillouin zone sampling errors.

### 3.1.2. Size dependence

The most widely methodology to describe defects in the dilute limit is the supercell approach, in which a defect is represented by a periodic array of identical configurations. The approach has significant computational advantages and avoids surface effects. Even with relatively large supercells there is, however, a contribution to the formation energy that results from the interaction of a periodic array of elastic dipoles. $^{1}$ In an elastically isotropic medium the elastic interaction scales with the inverse volume, i.e.

$$
E_{f}(N) \approx E_{f}(N \rightarrow \infty)+a / V=E_{f}(N \rightarrow \infty)+b / N, \quad(4)
$$

where $a$ and $b$ are constants of proportionality. This relation enables one to correct for this error by finite size scaling [33, 34].

This is illustrated for Ti interstitial configurations in Fig. 1(d), which clearly exhibits an inverse linear behavior; the interstitial configurations are shown in Fig. 3. Note that smaller cells than the ones included here (e.g., a $2 \times 2 \times 2$ 16-atom cell) deviate from the inverse linear behavior because of to non-linear contributions associated with interacting defect cores. The formation energies discussed in Sect. 3.2 were obtained using the same finite-size scaling approach as used in Fig. 1(d) based on the data compiled in the appendix. The error associated with fitting the data to Eq. (4) is 0.03 eV or less for all defect configurations.

### 3.1.3. Semicore states

It is has been argued that the inclusion of semicore states, specifically W-$5p$ states, in the pseudopotential or PAW data set is important to correctly describe the formation energies of SIAs in tungsten [16, 35]. This is reasonable as interstitial configurations involve very short interatomic distances and are therefore more sensitive to the core radius of the pseudopotential/PAW data set. To quantify these effects for the present defects, we carried out a systematic analysis of the effect of including semicore states. As the computational effort increases significantly due to approximately twice as many electrons in the calculation, the bulk of this study was restricted to 128-atom cells and a $3 \times 3 \times 3$ Monkhorst-Pack $k$-point mesh, see table in the appendix. For a selected number of configurations including both interstitial and substitutional defects, we also studied 250-atom cells as well as $6 \times 6 \times 6$ $k$-point grids. These data showed that the effect of semicore states is only weakly dependent by Brillouin zone sampling and system size.

From the data in Table .2, one can deduce that semicore states have a negligible influence on the formation energies of substitutional defects with the exception of V and possibly Zr. The situation is quite different in the case of the interstitial defects, for which the effect ranges from almost zero (Zr, Nb) to 0.5 eV and above (Ti, V, Ta). The energy shift varies between the different configurations and in some cases changes the energetic order (Ti, V). It is typically larger for $\langle 110\rangle$ interstitials, which have the shortest interatomic separation, than for $\langle 111\rangle$ and bridge interstitial configurations.

$^{1}$In the case of semiconductors additional effects such as image charge interactions and potential alignment corrections need to be taken into account. [32]

![](./images/814598975821709312_4.jpg)

Figure 2. Variation of the formation energies of substitutional defects across the periodic table according to the present calculations as well as prior calculations by Kong et al. [16].

Given the computational expense associated not only with the treatment of semicore states but system size and Brillouin zone sampling, we below present formation energies that are obtained as follows. We consider calculations that are based a $6 \times 6 \times 6$ Monkhorst-Pack mesh and do not include semicore states. These data are subjected to the finite-size scaling procedure described in Sect. 3.1.2, after which we add the shift in the formation energies due to semicore states that was obtained using 128-atom cells and a $3 \times 3 \times 3$ Monkhorst-Pack mesh. All respective formation energies are shown explicitly in Table .2. Based on the analysis in the present section, we conservatively estimate the error in the calculated formation energies to be about 0.1 eV for absolute numbers and 0.05 eV for energy differences.

### 3.2. Formation energies
#### 3.2.1. Substitutional defects
The formation energies for substitutional solute atoms are compiled in Table 1 and are shown in Fig. 2. One observes that both the elements from group 4 (V, Nb, Ta) and group 5 (Ti, Zr, Hf) exhibit a non-monotonic variation as one passes the $3d$ to the $5d$ series. These observations are in accord with earlier calculations [16] although in the latter case the formation energy of Zr is slightly negative whereas it is slightly positive in the present case. As discussed in Sect. 3.1, various sources of errors have been very carefully considered in the present case and the full data set shown in Table .2 also shows the present data to be very consistent.

The formation energy of a substitutional defect is related to the slope of the mixing energy curve in the dilute limit. Negative formation energies therefore imply a tendency to form solid solutions over a wide temperature range with W and additionally indicate a tendency to form ordered phases at lower temperatures [39-41].

For the group 5 elements one obtains consistently negative formation energies, which is consistent with the mixing energy curves calculated earlier for the W-V [41], W-Nb [39], and W-Ta [39,41] systems.

![](./images/814598975821709312_5.jpg)

Figure 3. Representative configurations of (a) bridge, (b) $\langle 110\rangle$ dumbbell, and (c) $\langle 111\rangle$ dumbbell interstitial defects. The $\langle 111\rangle$ crowdion configuration closely resembles the $\langle 111\rangle$ dumbbell configuration with a slightly larger spacing of the defect atoms along $\langle 111\rangle$ axis. The figure shows a slice parallel to a $\{110\}$ plane of the structure. Small (blue) spheres indicate tungsten atoms whereas large (gray) spheres indicate alloying elements in the case of extrinsic and tungsten atoms in the case of intrinsic defects. Thicker (yellow) cylinders indicate bond lengths shorter than $2.3 \AA$ whereas thinner (gray) cylinders indicate bond lengths shorter than $2.5 \AA$.

While in the case of the group 5 alloys all boundary phases possess a BCC lattice structure, the situation is more complicated in the case of the group 4 and group 7 (Re) elements, for which the low temperature boundary phases with the exception of W adopt a hexagonal-close packed (HCP) structure. In addition, in the case of the group 4 elements one furthermore observes a high-temperature BCC phase that is vibrationally stabilized, whereas it is mechanically unstable at low temperatures.

Experimentally, it is difficult to accurately assess the phase diagrams of W-based alloys down to low temperatures due to the slow kinetics of refractory systems even at relatively high temperatures. As a result, most of the information available to date is based on thermodynamic assessments, which are frequently based on assumptions concerning the nature of the interatomic interactions [42].

In the case of Ti the calculated phase diagram [42] suggests a very extended solubility region at high-temperatures but a vanishing solubility as the temperature approaches zero. Barring any experimental information for temperatures below approximately 1000 K [43], this assessment was based on the assumption that the mixing energy is positive over the entire concentration range [42]. The present finding suggests that this assumption needs to be revised and a better data basis is required to accurately determine the solvus line for Ti in W. It should be noted that while this region of the phase diagram is difficult to access by thermodynamic equilibrium studies, it can nonetheless be relevant for the behavior of the material under irradiation conditions as it determines the thermodynamic driving forces.

The solubility limits of Zr [42], Hf [42] as well as Re [44] in W are not determined by the equilibrium between W and another elemental phase but rather several ordered structure including the $\chi$ and $\sigma$ phases [45]. This implies that the respective compound formation enthalpy should be used to determine the chemical boundary conditions that enter Eq. (1) in the form of the chemical potentials $\mu_{i}$. This level of analysis is beyond the scope of the present work.

#### 3.2.2. Interstitial defects
A systematic exploration of interstitial configurations associated with solute atoms in BCC tungsten, revealed three dis-

<table><caption>Table 1. Formation energies and volumes of intrinsic and extrinsic point defects in tungsten.</caption>
<thead>
<tr>
<th rowspan="2">Element</th>
<th rowspan="2">Sub</th>
<th colspan="3">Formation energies</th>
<th colspan="6">Formation volumes</th>
</tr>
<tr>
<th>〈111〉–int</th>
<th>〈110〉–int</th>
<th>bridge–int</th>
<th>$v_{Sub}^{f}$</th>
<th>$v_{\langle 111\rangle }^{f}$</th>
<th>$A_{\langle 111\rangle }$</th>
<th>$v_{\langle 110\rangle }^{f}$</th>
<th>$A_{\langle 110\rangle }$</th>
<th>$v_{bridge}^{f}$</th>
<th>$A_{bridge}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>W</td>
<td></td>
<td>10.16</td>
<td>10.59</td>
<td>10.17</td>
<td>-</td>
<td>1.63</td>
<td>9.05</td>
<td>1.66</td>
<td>6.16</td>
<td>1.64</td>
<td>12.10</td>
</tr>
<tr>
<td>DFT [36]</td>
<td></td>
<td>9.55</td>
<td>9.84</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>DFT [37]</td>
<td></td>
<td>9.82</td>
<td>10.10</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Expt. [38]</td>
<td></td>
<td>$9.06\pm 0.63$</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Ti</td>
<td></td>
<td>−0.81</td>
<td>8.83</td>
<td>8.99</td>
<td>8.73</td>
<td>0.01</td>
<td>1.38</td>
<td>8.99</td>
<td>1.30</td>
<td>8.34</td>
<td>1.33</td>
<td>9.45</td>
</tr>
<tr>
<td>V</td>
<td></td>
<td>−0.60</td>
<td>8.00</td>
<td>8.10</td>
<td>7.77</td>
<td>−0.18</td>
<td>1.21</td>
<td>16.37</td>
<td>1.19</td>
<td>14.93</td>
<td>1.20</td>
<td>24.37</td>
</tr>
<tr>
<td>Zr</td>
<td></td>
<td>0.07</td>
<td>11.21</td>
<td>11.74</td>
<td>11.21</td>
<td>0.28</td>
<td>1.85</td>
<td>5.18</td>
<td>1.83</td>
<td>3.35</td>
<td>1.85</td>
<td>5.62</td>
</tr>
<tr>
<td>Nb</td>
<td></td>
<td>−0.32</td>
<td>10.22</td>
<td>10.74</td>
<td>10.19</td>
<td>0.12</td>
<td>1.73</td>
<td>7.42</td>
<td>1.74</td>
<td>4.44</td>
<td>1.73</td>
<td>7.49</td>
</tr>
<tr>
<td>Hf</td>
<td></td>
<td>−0.20</td>
<td>9.99</td>
<td>11.53</td>
<td>10.14</td>
<td>0.25</td>
<td>1.86</td>
<td>8.25</td>
<td>1.64</td>
<td>4.96</td>
<td>1.85</td>
<td>7.04</td>
</tr>
<tr>
<td>Ta</td>
<td></td>
<td>−0.47</td>
<td>10.34</td>
<td>11.01</td>
<td>10.33</td>
<td>0.06</td>
<td>1.70</td>
<td>7.58</td>
<td>1.67</td>
<td>5.48</td>
<td>1.69</td>
<td>8.03</td>
</tr>
<tr>
<td>Re</td>
<td></td>
<td>0.17</td>
<td>9.53</td>
<td>9.55</td>
<td>9.49</td>
<td>−0.02</td>
<td>1.56</td>
<td>15.25</td>
<td>1.63</td>
<td>8.72</td>
<td>1.60</td>
<td>18.68</td>
</tr>
</tbody>
</table>

![](./images/814598975821709312_6.jpg)

Figure 4. Formation energy of bridge, 〈111〉 and 〈110〉 interstitials (left axis). Energy difference between 〈111〉 and 〈110〉 dumbbell interstitials with respect to bridge interstitial (right axis).

tinct low energy configurations corresponding to different local minima on the potential energy surface; these configurations are shown in Fig. 3. In addition to the well known 〈111〉 and 〈110〉 dumbbell configurations [3, 13, 36] a third “bridge interstitial” configuration [see Fig. 3(a)] was identified. This configuration can be understood as a lower symmetry derivative of the 〈111〉 dumbbell configuration, in which the solute atom has moved away from the 〈111〉 direction along one of the three $\langle 2\overline{1}1\rangle$ directions. This results in a bond angle with the nearest neighbors of approximately $150^{\circ}$ (compared to $180^{\circ}$ in the case of the straight dumbbell interstitial).

A configuration similar to the bridge interstitial has been reported for SIAs [6, 35] and for the Re mixed-interstitial [6], which in the latter reference was referred to as a $\langle 11h\rangle$ interstitial. In both of those cases the energy difference relative to the respective 〈111〉 interstitial configurations appeared to be rather small (less than 0.05 eV). In particular in the case of the SIA the energy difference between crowdion and bridge $\langle 11h\rangle$ configurations is quite sensitive to supercell size and shape with the crowdion configuration being the most stable in the limit of large defect separations [35]. We have carried out a vibrational analysis of bridge and crowdion configurations that demonstrates the slow size convergence of the crowdion configuration (due its strongly delocalized nature [3]) and supports the earlier analysis and conclusion [35]. In absolute numbers our results are very close to previous calculations [36, 37].

The formation energies of extrinsic interstitial configurations are compiled in Table 1 and shown in Fig. 4. The bridge interstitial is found to be the most stable configuration for Ti, V, and Re interstitials. In the case of Zr and Hf the 〈111〉 dumbbell shows the lowest formation energy, while for Nb and Ta the bridge and 〈111〉 dumbbell configurations are energetically practically degenerate (yet configurationally distinct). Our finding of a bridge interstitial for Re agrees the results presented in [6]. Note that bridge interstitial-type configurations were not considered in Ref. [16]. Furthermore, the binding of solute atoms was investigated relative to the 〈111〉-crowdion interstitial rather than with regard to the respective lowest energy configuration. For radiation induced segregation and precipitation processes, however, the latter quantitiy, which yields the thermodynamic binding energy, is the most relevant quantity.

In contrast to the present calculations for W-V, Muzyk et al. [41] found the 〈110〉 dumbbell interstitial to be the most stable configuration. The latter study, however, relied on calculations involving only 128-atom supercells and a $3\times 3\times 3$ $k$-point mesh. The analysis of computational errors provided in Sect. 3.1 suggests that these values are not fully converged.

For reference, Table 1 also contains data for SIAs, which have been extensively described before [6, 35]. The geometries and energetics obtained here agree with these earlier calculations.

### 3.3. Binding energies
Interactions of impurities and alloying elements with point defects are of great importance for materials under irradiation as they can significantly affect the mobility of defects [4]. This can result in segregation, precipitation and/or the formation of secondary phases at grain boundaries. To assess the tendency of different elements to trap SIAs we have therefore calculated

![](./images/814598975821709312_7.jpg)

Figure 5. Binding energies in units of electronvolts between self-interstitial atoms and substitutional solute atoms relative to the respective most stable mixed-interstitial configuration according to Eq. (2).

![](./images/814598975821709312_8.jpg)

Figure 6. Distance dependence of the binding energy between a self-interstitial atom (SIA) and a Ti atom. Open and closed circles represent configurations, in which the SIA is oriented along ⟨110⟩ and ⟨111⟩, respectively. Calculations were carried out using 128-atom cells at constant volume.

binding energies between impurities and interstitials. As shown in Fig. 5 negative values are obtained for Ti, V and Re interstitial configurations, while for the remaining elements the binding energies are positive.

A previous study [4] has also reported an attractive interaction between Re and SIAs of $E^b=-0.8$ eV, the orientation of the mixed-interstitial was, however, not specified. The binding energies obtained in the present study are $E_{bridge}^b=-0.62$ eV, $E_{\langle 111\rangle int}^b=-0.52$ eV and $E_{\langle 110\rangle int}^b=-0.36$ eV.

The negative binding energies for Ti, V and Re, which are also the three elements that favor bridge interstitial configurations, imply an attractive interactions with SIAs, whence these elements are expected to trap interstitials. The binding is very strong ($\sim0.6-1.8$ eV) in all three cases, indicating that thermal detrapping is unlikely. Trapping is a precursor to segregation and associated with radiation-induced segregation and precipitation. Previous experimental studies have confirmed radiation-induced Re precipitation in tungsten [46,47], yet no equivalent experimental data has yet been reported for Ti and V.

SIAs travel with very high mobility along the cowdion direction with a migration barrier on the order of a few meV ($\leq0.046$ eV) [48]. The high diffusivity of SIAs is closely related to the effective delocalization of the defect center and the fact that their migration involves only small atomic displacements [3]. The strong tendency of impurities to bind with SIAs causes the interstitial to localize and reduces its mobility dramatically. In this context it is important to quantify the range of the SIA-solute interaction as it provides a measure for the effective capture radius associated with a substitutional solute atom. Figure 6 shows the formation energy of solute-interstitial configurations as a function of the distance between interstitial center and solute atom for the case of Ti. The data indicate a short interaction range as binding is practically absent outside a radius of approximately $2.5\mathring{A}$, which corresponds to the first nearest neighbor shell of the BCC lattice.

### 3.4. Formation volumes and formation volume tensors
A defect can affect other point as well as line defects (dislocations) either via a direct "chemical" interaction or via long-range elastic interactions. The strain field can modify the saddle points during point defect migration [49]. Similarly, it can affect the barriers for dislocation kink nucleation and growth and thereby affect the plastic behavior of the materials [17]. Formation volumes quantify the induced strain in terms of linear elasticity theory; the formation volume tensors provide additional information concerning the orientation and anisotropy of the strain field.

From constant pressure calculations we obtain the change in cell shape due to defect formation $L-L_0$, from which one readily obtains the formation volume tensor $\nu^f$ using Eq. (3). All solute atoms are associated with a symmetric lattice relaxation whence the formation volume tensor is simply $\nu^f=\nu^f I$, where $\nu^f=(1/3)\text{Tr}\nu^f$ is the formation volume. The values are compiled in Table 1 and Fig. 7, which shows that the formation volumes closely correlate with the atomic radii.

In the case of interstitial defects the formation volume tensor reflects the orientation of the dumbbell as illustrated in Fig. 9.

![](./images/814598975821709312_9.jpg)

Figure 7. Formation volumes of intrinsic and extrinsic defects in tungsten (left axis). For comparison the atomic radii are shown on the right axis.

![](./images/814598975821709312_10.jpg)

Figure 8. Anisotropy of <111> dumbbell, <110> dumbbell and bridge interstitials with respect to atomic radius.

![](./images/814598975821709312_11.jpg)

Figure 9. Ellipsoids representing (formation) volume tensors corresponding to a (left) tungsten atom in the perfect lattice, (center) a Ti <111> dumbbell interstitial, and (right) a Ti <110> dumbbell interstitial.

The formation volumes are reported in Table 1 and Fig. 7. The strongly elongated shape of the ellipsoids in Fig. 9 indicates a large degree of anisotropy. The latter can be conveniently mea- sured by the ratio A of the largest and smallest eigenvalues of the formation volume tensor, see Table 1. Large values of A are obtained with typical values in the range from 6-10. For Re and V the anisotropy is even larger with A values up to 24, see Fig. 8. It is remarkable that the three elements that favor the bridge interstitial configuration and trap SIAs, are also the three elements with the largest anisotropy ratio.

Finally, for the vacancy one obtains a formation volume that is very close to zero, which is an indication for the covalent bonding character that is characteristic for W.

## 4. Conclusions

Substitutional and interstitial defects in W associated with several alloying elements of interest were investigated by first- principles calculations based on density functional theory. A systematic investigation of computational parameters was car- ried out in order to establish the accuracy limits of the present calculations. The errors due to finite size, Brillouin zone sam- pling, and the treatment of semicore effects were shown to be of similar magnitude and a procedure was described to account for each contribution.

Negative formation energies were obtained for substitutional Ti, V, Nb, Hf as well as Ta and positive values for Zr and Re. The negative values suggest a negative mixing energy for the BCC solutions, which should result in an extended miscibil- ity range and possibly the formation of ordered phases at low temperatures, see Refs. [40, 41]. This is partially at odds with phase diagrams based on thermodynamic calculations. As the latter are based on limited experimental data due to the refrac- tory nature of the W-alloys, this suggests that further investi- gations should be carried out to establish the low temperature phase diagrams as they determine the thermodynamic driving forces that underpin the dynamic behavior of the material.

While interstitials are practically absent under equilibrium conditions due to their large formation energies, they are im- portant under reactor relevant conditions when SIAs are pro- duced by ion irradiation. In addition to high symmetry dumb- bell configurations, here another interstitial configuration has been systematically investigated that was referred to as a bridge interstitial. For mixed-interstitials involving Ti, V, and Re the bridge interstitial configuration is found to be the most stable configuration.

The same three elements (Ti, V and Re) exhibit negative binding energies with respect to SIAs and are thus predicted to trap these defects. This causes a reduction of the interstitial mo- bility, which is likely to accelerate damage build up. It is also of interest in connection with radiation-induced segregation and precipitation, which has already been observed for Re.

Finally, the elastic strain field of both substitutional and in- terstitial defects was quantified in the form of formation volume tensors. Remarkably, again Ti, V, and Re interstitials are the defects that exhibit the strongest anisotropy as quantified by the

ratio between the largest and smallest eigenvalues of the forma- tion volume tensor. These parameters are suitable e.g., for the construction of kinetic Monte Carlo models of defect migration and dislocation mobility.

## Acknowledgments

This work was supported by the the Swedish Research Coun- cil in the form of a Young Researcher grant, the European Re- search Council via a Marie Curie Career Integration Grant, and the *Area of Advance – Materials Science* at Chalmers. Com- puter time allocations by the Swedish National Infrastructure for Computing at NSC (Linköping) and C3SE (Gothenburg) are gratefully acknowledged.

Table. 2. Convergence of formation energies (in units of electronvolts) of intrinsic and extrinsic point defects in tungsten with respect to cell size, $k$-point sampling, and the treatment of semicore states. Numbers in upright format correspond to calculations, in which the semicore states (in particular the W-$5p$ states) were not included. By contrast, italicized numbers show the results from calculations that did not include semicore states with numbers in brackets indicating the difference between the two types of calculations. Additional calculations with semicore states were carried out for selected 250-atom supercell configurations. These calculations confirmed that the shift in the formation energies due to the neglect of semicore states is only weakly dependent on system size. The last but one column reports the formation energies in the dilute limit from finite size scaling using data obtained in calculations without semicore states (w/o sc) using $6 \times 6 \times 6$ $k$-point grids. The final column shows these data including a semicore correction (w/ sc) as described in Sect. 3.1.3.

<table>
  <thead>
    <tr>
      <th>Element</th>
      <th>Defect</th>
      <th colspan="3">54-atom cells ($3 \times 3 \times 3$)</th>
      <th colspan="3">128-atom cells ($4 \times 4 \times 4$)</th>
      <th colspan="4">250-atom cells ($5 \times 5 \times 5$)</th>
      <th rowspan="2">Extrapolated</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th>$n_k$ 3</th>
      <th>$n_k$ 4</th>
      <th>$n_k$ 5</th>
      <th>$n_k$ 6</th>
      <th>$n_k$ 3</th>
      <th>$n_k$ 4</th>
      <th>$n_k$ 6</th>
      <th>$n_k$ 3</th>
      <th>$n_k$ 4</th>
      <th>$n_k$ 6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3">self</th>
      <td>⟨110⟩-int</td>
      <td>9.21</td>
      <td>9.40</td>
      <td>9.66</td>
      <td>9.83</td>
      <td>10.15</td>
      <td>10.20</td>
      <td>10.07</td>
      <td>10.24</td>
      <td>-</td>
      <td>10.16</td>
      <td>10.25</td>
      <td>10.59</td>
    </tr>
    <tr>
      <td>⟨111⟩-int</td>
      <td>8.92</td>
      <td>-</td>
      <td>-</td>
      <td>9.61</td>
      <td>9.82</td>
      <td>9.88</td>
      <td>9.71</td>
      <td>9.96</td>
      <td>9.73</td>
      <td>9.87</td>
      <td>9.89</td>
      <td>10.16</td>
    </tr>
    <tr>
      <td>bridge-int</td>
      <td>8.88</td>
      <td>-</td>
      <td>-</td>
      <td>9.53</td>
      <td>9.78</td>
      <td>9.84</td>
      <td>9.69</td>
      <td>9.88</td>
      <td>-</td>
      <td>9.79</td>
      <td>9.85</td>
      <td>10.17</td>
    </tr>
    <tr>
      <th rowspan="3">Ti</th>
      <td>sub</td>
      <td>−0.83</td>
      <td>−0.82</td>
      <td>−0.72</td>
      <td>−0.77</td>
      <td>−0.74</td>
      <td>−0.67</td>
      <td>−0.78</td>
      <td>−0.75</td>
      <td>−0.81</td>
      <td>−0.79</td>
      <td>−0.79</td>
      <td>-0.81</td>
    </tr>
    <tr>
      <td>⟨110⟩-int</td>
      <td>7.66</td>
      <td>-</td>
      <td>-</td>
      <td>8.12</td>
      <td>8.30</td>
      <td>8.33</td>
      <td>8.24</td>
      <td>8.36</td>
      <td>-</td>
      <td>8.31</td>
      <td>8.35</td>
      <td>8.99</td>
    </tr>
    <tr>
      <td>⟨111⟩-int</td>
      <td>7.64</td>
      <td>-</td>
      <td>-</td>
      <td>8.26</td>
      <td>8.43</td>
      <td>8.50</td>
      <td>8.36</td>
      <td>8.56</td>
      <td>-</td>
      <td>8.46</td>
      <td>8.49</td>
      <td>8.83</td>
    </tr>
    <tr>
      <th></th>
      <td>bridge-int</td>
      <td>7.51</td>
      <td>-</td>
      <td>-</td>
      <td>8.07</td>
      <td>8.27</td>
      <td>8.31</td>
      <td>8.18</td>
      <td>8.32</td>
      <td>-</td>
      <td>8.24</td>
      <td>8.28</td>
      <td>8.73</td>
    </tr>
    <tr>
      <th rowspan="3">V</th>
      <td>sub</td>
      <td>−0.44</td>
      <td>−0.45</td>
      <td>−0.41</td>
      <td>−0.44</td>
      <td>−0.42</td>
      <td>−0.38</td>
      <td>−0.44</td>
      <td>−0.41</td>
      <td>−0.46</td>
      <td>−0.43</td>
      <td>−0.43</td>
      <td>-0.60</td>
    </tr>
    <tr>
      <td>⟨110⟩-int</td>
      <td>6.94</td>
      <td>-</td>
      <td>-</td>
      <td>7.40</td>
      <td>7.55</td>
      <td>7.60</td>
      <td>7.52</td>
      <td>7.63</td>
      <td>-</td>
      <td>7.82</td>
      <td>7.61</td>
      <td>8.10</td>
    </tr>
    <tr>
      <td>⟨111⟩-int</td>
      <td>6.87</td>
      <td>-</td>
      <td>-</td>
      <td>7.49</td>
      <td>7.65</td>
      <td>7.71</td>
      <td>7.59</td>
      <td>7.78</td>
      <td>-</td>
      <td>7.67</td>
      <td>7.70</td>
      <td>8.00</td>
    </tr>
    <tr>
      <th></th>
      <td>bridge-int</td>
      <td>6.70</td>
      <td>-</td>
      <td>-</td>
      <td>7.24</td>
      <td>7.41</td>
      <td>7.46</td>
      <td>7.34</td>
      <td>7.46</td>
      <td>-</td>
      <td>7.38</td>
      <td>7.42</td>
      <td>7.77</td>
    </tr>
    <tr>
      <th rowspan="3">Zr*</th>
      <td>sub</td>
      <td>0.08</td>
      <td>0.09</td>
      <td>0.19</td>
      <td>0.14</td>
      <td>0.17</td>
      <td>0.23</td>
      <td>0.13</td>
      <td>0.18</td>
      <td>0.09</td>
      <td>0.13</td>
      <td>0.13</td>
      <td>0.07</td>
    </tr>
    <tr>
      <td>⟨110⟩-int</td>
      <td>10.71</td>
      <td>-</td>
      <td>-</td>
      <td>11.33</td>
      <td>11.66</td>
      <td>11.68</td>
      <td>11.54</td>
      <td>11.75</td>
      <td>-</td>
      <td>11.69</td>
      <td>11.76</td>
      <td>11.74</td>
    </tr>
    <tr>
      <td>⟨111⟩-int</td>
      <td>10.14</td>
      <td>-</td>
      <td>-</td>
      <td>10.86</td>
      <td>11.10</td>
      <td>11.18</td>
      <td>10.98</td>
      <td>11.27</td>
      <td>-</td>
      <td>11.13</td>
      <td>11.16</td>
      <td>11.21</td>
    </tr>
    <tr>
      <th rowspan="3">Nb</th>
      <td>sub</td>
      <td>−0.30</td>
      <td>−0.30</td>
      <td>−0.27</td>
      <td>−0.30</td>
      <td>−0.29</td>
      <td>−0.24</td>
      <td>−0.30</td>
      <td>−0.27</td>
      <td>−0.31</td>
      <td>−0.29</td>
      <td>−0.29</td>
      <td>-0.32</td>
    </tr>
    <tr>
      <td>⟨110⟩-int</td>
      <td>9.71</td>
      <td>-</td>
      <td>-</td>
      <td>10.33</td>
      <td>10.67</td>
      <td>10.70</td>
      <td>10.57</td>
      <td>10.76</td>
      <td>-</td>
      <td>10.68</td>
      <td>10.77</td>
      <td>10.74</td>
    </tr>
    <tr>
      <td>⟨111⟩-int</td>
      <td>9.22</td>
      <td>-</td>
      <td>-</td>
      <td>9.91</td>
      <td>10.13</td>
      <td>10.21</td>
      <td>10.02</td>
      <td>10.28</td>
      <td>-</td>
      <td>10.15</td>
      <td>10.18</td>
      <td>10.22</td>
    </tr>
    <tr>
      <th></th>
      <td>bridge-int</td>
      <td>9.25</td>
      <td>-</td>
      <td>-</td>
      <td>9.95</td>
      <td>10.13</td>
      <td>10.21</td>
      <td>10.02</td>
      <td>10.28</td>
      <td>-</td>
      <td>10.15</td>
      <td>10.16</td>
      <td>10.19</td>
    </tr>
    <tr>
      <th rowspan="3">Hf</th>
      <td>sub</td>
      <td>−0.27</td>
      <td>−0.25</td>
      <td>−0.15</td>
      <td>−0.19</td>
      <td>−0.16</td>
      <td>−0.10</td>
      <td>−0.20</td>
      <td>−0.17</td>
      <td>−0.23</td>
      <td>−0.20</td>
      <td>−0.20</td>
      <td>-0.20</td>
    </tr>
    <tr>
      <td>⟨110⟩-int</td>
      <td>9.98</td>
      <td>-</td>
      <td>-</td>
      <td>10.52</td>
      <td>10.78</td>
      <td>10.79</td>
      <td>10.69</td>
      <td>10.84</td>
      <td>-</td>
      <td>10.78</td>
      <td>10.84</td>
      <td>11.53</td>
    </tr>
    <tr>
      <td>⟨111⟩-int</td>
      <td>9.68</td>
      <td>-</td>
      <td>-</td>
      <td>10.39</td>
      <td>11.47</td>
      <td>9.80</td>
      <td>9.59</td>
      <td>9.80</td>
      <td>-</td>
      <td>10.10</td>
      <td>9.71</td>
      <td>9.99</td>
    </tr>
    <tr>
      <th></th>
      <td>bridge-int</td>
      <td>8.91</td>
      <td>-</td>
      <td>-</td>
      <td>9.56</td>
      <td>9.72</td>
      <td>9.85</td>
      <td>9.65</td>
      <td>9.88</td>
      <td>-</td>
      <td>9.77</td>
      <td>9.79</td>
      <td>10.14</td>
    </tr>
    <tr>
      <th rowspan="3">Ta</th>
      <td>sub</td>
      <td>−0.48</td>
      <td>−0.48</td>
      <td>−0.45</td>
      <td>−0.47</td>
      <td>−0.45</td>
      <td>−0.41</td>
      <td>−0.47</td>
      <td>−0.45</td>
      <td>−0.47</td>
      <td>−0.46</td>
      <td>−0.46</td>
      <td>-0.47</td>
    </tr>
    <tr>
      <td>⟨110⟩-int</td>
      <td>9.53</td>
      <td>-</td>
      <td>-</td>
      <td>10.12</td>
      <td>10.42</td>
      <td>10.45</td>
      <td>10.34</td>
      <td>10.51</td>
      <td>-</td>
      <td>10.45</td>
      <td>10.53</td>
      <td>11.01</td>
    </tr>
    <tr>
      <td>⟨111⟩-int</td>
      <td>9.06</td>
      <td>-</td>
      <td>-</td>
      <td>9.74</td>
      <td>10.90</td>
      <td>10.04</td>
      <td>9.86</td>
      <td>10.11</td>
      <td>-</td>
      <td>10.01</td>
      <td>10.04</td>
      <td>10.34</td>
    </tr>
    <tr>
      <th></th>
      <td>bridge-int</td>
      <td>9.08</td>
      <td>-</td>
      <td>-</td>
      <td>9.76</td>
      <td>9.97</td>
      <td>10.05</td>
      <td>9.86</td>
      <td>10.12</td>
      <td>-</td>
      <td>10.02</td>
      <td>10.04</td>
      <td>10.33</td>
    </tr>
    <tr>
      <th rowspan="3">Re</th>
      <td>sub</td>
      <td>0.12</td>
      <td>0.15</td>
      <td>0.18</td>
      <td>0.18</td>
      <td>0.17</td>
      <td>0.12</td>
      <td>0.18</td>
      <td>0.18</td>
      <td>0.18</td>
      <td>0.17</td>
      <td>0.17</td>
      <td>0.17</td>
    </tr>
    <tr>
      <td>⟨110⟩-int</td>
      <td>8.29</td>
      <td>-</td>
      <td>-</td>
      <td>8.91</td>
      <td>9.23</td>
      <td>9.28</td>
      <td>9.14</td>
      <td>9.29</td>
      <td>-</td>
      <td>9.21</td>
      <td>9.30</td>
      <td>9.55</td>
    </tr>
    <tr>
      <td>⟨111⟩-int</td>
      <td>8.25</td>
      <td>-</td>
      <td>-</td>
      <td>8.93</td>
      <td>9.48</td>
      <td>9.25</td>
      <td>9.09</td>
      <td>9.33</td>
      <td>-</td>
      <td>9.25</td>
      <td>9.30</td>
      <td>9.53</td>
    </tr>
    <tr>
      <th></th>
      <td>bridge-int</td>
      <td>8.24</td>
      <td>-</td>
      <td>-</td>
      <td>8.86</td>
      <td>9.21</td>
      <td>9.18</td>
      <td>9.06</td>
      <td>9.23</td>
      <td>-</td>
      <td>9.15</td>
      <td>9.22</td>
      <td>9.49</td>
    </tr>
    <tr>
      <th></th>
      <td>w/o sc</td>
      <td colspan="4"></td>
      <td colspan="3"></td>
      <td colspan="3"></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th></th>
      <td>w/ sc</td>
      <td colspan="4"></td>
      <td colspan="3"></td>
      <td colspan="3"></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th></th>
      <td>diff</td>
      <td colspan="4"></td>
      <td>(0.34)</td>
      <td>(0.27)</td>
      <td>(0.32)</td>
      <td>(-0.02)</td>
      <td>(0.64)</td>
      <td>(0.34)</td>
      <td>(0.45)</td>
      <td></td>
    </tr>
    <tr>
      <th></th>
      <td></td>
      <td colspan="4"></td>
      <td>-0.59</td>
      <td>(-0.17)</td>
      <td>(0.49)</td>
      <td>(0.30)</td>
      <td>(0.35)</td>
      <td>(-0.06)</td>
      <td>(-0.02)</td>
      <td></td>
    </tr>
    <tr>
      <th></th>
      <td></td>
      <td colspan="4"></td>
      <td>-0.42</td>
      <td>(0.05)</td>
      <td>(-0.03)</td>
      <td>(-0.03)</td>
      <td>(0.04)</td>
      <td>(0.03)</td>
      <td>(0.00)</td>
      <td></td>
    </tr>
    <tr>
      <th></th>
      <td></td>
      <td colspan="4"></td>
      <td>-0.32</td>
      <td>(0.69)</td>
      <td>(0.29)</td>
      <td>(0.35)</td>
      <td>(-0.01)</td>
      <td>(0.48)</td>
      <td>(0.30)</td>
      <td></td>
    </tr>
    <tr>
      <th></th>
      <td></td>
      <td colspan="4"></td>
      <td>-0.29</td>
      <td>(0.29)</td>
      <td>(0.00)</td>
      <td>(0.25)</td>
      <td>(0.23)</td>
      <td>(0.27)</td>
      <td></td>
    </tr>
  </tbody>
</table>

* In the case of Zr, the bridge interstitial configuration always relaxed toward the ⟨111⟩-int configuration regardless of system size.

[1] S. J. Zinkle, N. M. Ghoniem, Operating temperature windows for fusion reactor structural materials, Fusion Engineering and Design 51-52 (2000) 55-71. doi:10.1016/S0920-3796(00)00320-3.

[2] M. Rieth, S. Dudarev, S. Gonzalez de Vicente, J. Aktaa, T. Ahlgren, S. Antusch, D. Armstrong, M. Balden, N. Baluc, M.-F. Barthe, et al., Recent progress in research on tungsten materials for nuclear fusion ap- plications in europe, Journal of Nuclear Materials 432 (1) (2013) 482-500.

[3] S. P. Fitzgerald, D. Nguyen-Manh, Peierls potential for crowdions in the bcc transition metals, Phys. Rev. Lett. 101 (2008) 115504.

[4] C. Becquart, C. Domain, An object kinetic monte carlo simulation of the dynamics of helium and point defects in tungsten, Journal of Nuclear Ma- terials 385 (2) (2009) 223-227.

[5] T. Noda, M. Fujita, M. Okada, Transmutation and induced radioactivity of W in the armor and first wall of fusion reactors, J. Nucl. Mater. 258-263, Part 1 (1998) 934-939. doi:10.1016/S0022-3115(98)00088-9.

[6] T. Suzudo, M. Yamaguchi, A. Hasegawa, Stability and mobility of rhe- nium and osmium in tungsten: first principles study, Modelling and Sim- ulation in Materials Science and Engineering 22 (7) (2014) 075006.

[7] T. Tietz, J. Wilson, Behavior and Properties of Refractory Metals, Stan- ford University Press, 1965.

[8] P. Gumbsch, J. Riedle, A. Hartmaier, H. F. Fischmeister, Controlling fac- tors for the brittle-to-ductile transition in tungsten single crystals, Science 282 (5392) (1998) 1293-1295. doi:10.2307/2897296.

[9] M. V. Aguirre, A. Martín, J. Y. Pastor, J. LLorca, M. A. Monge, R. Pareja, Mechanical properties of tungsten alloys with $y_{203}$ and titanium additions, J. Nucl. Mater. 417 (1-3) (2011) 516-519. doi:10.1016/j.jnucmat.2010.12.120.

[10] F. Hofmann, D. Nguyen-Manh, M. R. Gilbert, C. E. Beck, J. K. Elia- son, A. A. Maznev, W. Liu, D. E. J. Armstrong, K. A. Nelson, S. L. Dudarev, Lattice swelling and modulus change in a helium-implanted tungsten alloy: X-ray micro-diffraction, surface acoustic wave measure- ments, and multiscale modelling, Acta Materialia 89 (2015) 352-363. doi:10.1016/j.actamat.2015.01.055.

[11] R. S. Averback, T. Diaz de la Rubia, Displacement Damage in Irradiated Metals and Semiconductors, Solid State Physics 51 (1998) 281.

[12] Y. Zhong, K. Nordlund, M. Ghaly, R. S. Averback, Defect produc- tion in tungsten: A comparison between field-ion microscopy and molecular-dynamics simulations, Phys. Rev. B 58 (5) (1998) 2361-2364. doi:10.1103/PhysRevB.58.2361.

[13] W. H. Zhou, Y. G. Li, L. F. Huang, Z. Zeng, X. Ju, Dynamical behaviors of self-interstitial atoms in tungsten, J. Nucl. Mater. 437 (1-3) (2013) 438-444. doi:10.1016/j.jnucmat.2013.02.075.

[14] A. L. Bement, Irradiation effects on structural alloys for nuclear reactor applications, Vol. 484, ASTM International, 1971. doi:10.1520/STP484- EB.

[15] G.-H. Lu, H.-B. Zhou, C. S. Becquart, A review of modelling and simu- lation of hydrogen behaviour in tungsten at different scales, Nucl. Fusion 54 (8) (2014) 086001. doi:10.1088/0029-5515/54/8/086001.

[16] X.-S. Kong, X. Wu, Y.-W. You, C. S. Liu, Q. F. Fang, J.-L. Chen, G. N. Luo, Z. Wang, First-principles calculations of transition metal-solute in- teractions with point defects in tungsten, Acta Materialia 66 (2014) 172-183. doi:10.1016/j.actamat.2013.11.044.

[17] M. Z. Hossain, J. Marian, Stress-dependent solute energetics in w-re al- loys from first-principles calculations, Acta Materialia 80 (2014) 107-117. doi:10.1016/j.actamat.2014.07.028.

[18] P. E. Blöchl, Projector augmented-wave method, Phys. Rev. B 50 (24) (1994) 17953 -17979. doi:10.1103/PhysRevB.54.11169.

[19] G. Kresse, D. Joubert, From ultrasoft pseudopotentials to the projec- tor augmented-wave method, Phys. Rev. B 59 (3) (1999) 1758 - 1775. doi:10.1103/PhysRevB.59.1758.

[20] G. Kresse, J. Hafner, Ab initio molecular dynamics for liquid metals, Phys. Rev. B 47 (1) (1993) 558-561. doi:10.1103/PhysRevB.47.558.

[21] G. Kresse, J. Hafner, Ab initio molecular-dynamics simulation of the liquid-metal-amorphous-semiconductor transition in germanium, Phys. Rev. B 49 (20) (1994) 14251. doi:10.1103/PhysRevB.49.14251.

[22] G. Kresse, J. Furthmüller, Efficient iterative schemes for ab initio total- energy calculations using a plane-wave basis set, Phys. Rev. B 54 (1996) 11169. doi:10.1103/PhysRevB.54.11169.

[23] G. Kresse, J. Furthmüller, Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set, Comput. Mater. Sci. 6 (1) (1996) 15-50. doi:10.1016/0927-0256(96)00008-0.

[24] J. P. Perdew, K. Burke, M. Ernzerhof, Generalized Gradient Approxima- tion Made Simple, Phys. Rev. Lett. 77 (18) (1996) 3865-3868, erratum, ibid. 78, 1396(E) (1997). doi:10.1103/PhysRevLett.77.3865.

[25] S. B. Zhang, J. E. Northrup, Chemical potential dependence of defect formation energies in GaAs: Application to Ga self-diffusion, Phys. Rev. Lett. 67 (17) (1991) 2339-2342.

[26] P. Erhart, K. Albe, Thermodynamics of mono- and di-vacancies in barium titanate, J. Appl. Phys. 102 (08) (2007) 084111. doi:10.1063/1.2801011.

[27] C. Wolverton, Solute-vacancy binding in aluminum, Acta Materialia 55 (17) (2007) 5867 - 5872. doi:http://dx.doi.org/10.1016/j.actamat.2007.06.039.

[28] P. Olsson, T. P. C. Klaver, C. Domain, Ab initio study of solute transition- metal interactions with point defects in bcc fe, Phys. Rev. B 81 (5) (2010) 054102. doi:10.1103/PhysRevB.81.054102.

[29] S. A. Centoni, B. Sadigh, G. H. Gilmer, S. L. Lenosky, T. J. Lenosky, T. Diaz de la Rubia, C. B. Musgrave, First-principles calculation of intrinsic defect formation volumes in silicon, Phys. Rev. B 72 (2005) 195206.

[30] K. Garikipati, M. Falk, M. Bouville, B. Puchalac, H. Narayanan, The continuum elastic and atomistic viewpoints on the formation volume and strain energy of a point defect, J. Mech. Phys. Solids 54 (9) (2006) 1929-51.

[31] E. Jedvik, A. Lindman, M. . Benediktsson, G. Wahnstrm, Size and shape of oxygen vacancies and protons in acceptor-doped barium zirconate, Solid State Ionics 275 (2015) 2-8.

[32] S. Lany, A. Zunger, Assessment of correction methods for the band-gap problem and for finite-size effects in supercell defect calculations: Case studies for zno and gaas, Phys. Rev. B 78 (23) (2008) 235104. doi:10.1103/PhysRevB.78.235104.

[33] D. Grecu, P. H. Dederichs, The asymptotic behavior of the displacement field of point defects in 'isotropic' crystals, Phys. Lett. 36A (2) (1971) 135.

[34] P. H. Dederichs, J. Pollmann, Elastic displacement field of point defects in anisotropic cubic crystals, Z. Physik 255 (1972) 315.

[35] L. Ventelon, F. Willaime, C.-C. Fu, M. Heran, I. Ginoux, Ab ini- tio investigation of radiation defects in tungsten: Structure of self- interstitials and specificity of di-vacancies compared to other bcc tran- sition metals, Journal of Nuclear Materials 425 (1-3) (2012) 16-21. doi:10.1016/j.jnucmat.2011.08.024.

[36] D. Nguyen-Manh, A. P. Horsfield, S. L. Dudarev, Self-interstitial atom de- fects in bcc transition metals: Group-specific trends, Phys. Rev. B 73 (2) (2006) 020101. doi:10.1103/PhysRevB.73.020101.

[37] C. S. Becquart, C. Domain, Ab initio calculations about intrinsic point de- fects and he in w, Nuclear Instruments and Methods in Physics Research Section B: Beam Interactions with Materials and Atoms 255 (1) (2007) 23-26, computer Simulation of Radiation Effects in Solids Proceedings of the Eighth International Conference on Computer Simulation of Radi- ation Effects in Solids (COSIRES 2006) Computer Simulation of Radia- tion Effects in Solids. doi:http://dx.doi.org/10.1016/j.nimb.2006.11.006.

[38] H. Wollenberger, Point defects, in: Physical metallurgy. 3. ed, 1983.

[39] V. Blum, A. Zunger, Prediction of ordered structures in the bcc binary systems of mo, nb, ta, and w from first-principles search of approximately 3,000,000 possible configurations, Phys. Rev. B 72 (2) (2005) 020104(R). doi:10.1103/PhysRevB.72.020104.

[40] P. Erhart, B. Sadigh, A. Caro, Are there stable long-range ordered $Fe_{1-x}Cr_x$ compounds?, Appl. Phys. Lett. 92 (14) (2008) 141904. doi:10.1063/1.2907337.

[41] M. Muzyk, D. Nguyen-Manh, K. J. Kurzydłowski, N. L. Baluc, S. L. Dudarev, Phase stability, point defects, and elastic proper- ties of w-v and w-ta alloys, Phys. Rev. B 84 (10) (2011) 104115. doi:10.1103/PhysRevB.84.104115.

[42] S. K. Lee, D. N. Lee, Calculation of phase diagrams using partial phase diagram data, Calphad 10 (1) (1986) 61.

[43] E. Rudy, S. Windisch, Revision of titanium-tungsten system, Trans. Met- all. Soc. AIME 242 (5) (1968) 953-&.

[44] S. G. Fries, B. Sundman, Using Re-W $\sigma$-phase first-principles re- sults in the Bragg-Williams approximation to calculate finite-temperature thermodynamic properties, Physical Review B 66 (1) (2002) 012203. doi:10.1103/PhysRevB.66.012203.

[45] J.-C. Crivello, J.-M. Joubert, First principles calculations of the - and - phases in the mo-re and w-re systems, J. Phys. Condens. Matter 22 (3)

(2010) 035402. doi:10.1088/0953-8984/22/3/035402.

[46] T. Tanno, A. Hasegawa, M. Fujiwara, J.-C. He, S. Nogami, M. Satou, T. Shishido, K. Abe, Precipitation of solid transmutation elements in irra- diated tungsten alloys, Materials transactions 49 (10) (2008) 2259–2264.

[47] R. Herschitz, D. N. Seidman, Radiation-induced precipitation in fast- neutron irradiated tungsten-rhenium alloys: An atom-probe field-ion mi- croscope study, Nuclear Instruments and Methods in Physics Research Section B: Beam Interactions with Materials and Atoms 7 (1985) 137–142.

[48] T. Amino, K. Arakawa, H. Mori, Activation energy for long-range migra- tion of self-interstitial atoms in tungsten obtained by direct measurement of radiation-induced point-defect clusters, Philosophical Magazine Let- ters 91 (2) (2010) 86–96. doi:10.1080/09500839.2010.533133.

[49] C. S. Becquart, C. Domain, Molecular dynamics simulations of dam- age and plasticity: The role of ab initio calculations in the devel- opment of interatomic potentials, Philos. Mag. 89 (2009) 3215–3234. doi:10.1080/14786430903250819PII 917306934.