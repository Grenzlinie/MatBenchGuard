$Ab$ initio study on the rare-earth iron-pnictides RFeAsO (R = Pr, Nd, Sm, Gd) in the low-temperature $Cmma$ phase

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2014 J. Phys.: Condens. Matter 26 045501

(http://iopscience.iop.org/0953-8984/26/4/045501)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 93.180.53.211
This content was downloaded on 12/02/2014 at 10:49

Please note that terms and conditions apply.

# Ab initio study on the rare-earth iron-pnictides RFeAsO ($\text{R} = \text{Pr}$, $\text{Nd}$, $\text{Sm}$, $\text{Gd}$) in the low-temperature $Cmma$ phase

Esra Ertürk$^1$, Tanju Gürel$^1$, A V Lukoyanov$^{2,3}$, Güven Akçay$^4$, Resul Eryiğit$^4$ and V I Anisimov$^{2,3}$

$^1$ Department of Physics, Namik Kemal University, Tekirdağ, TR-59030, Turkey
$^2$ Institute of Metal Physics, Ural Branch of Russian Academy of Sciences, 620990 Yekaterinburg, Russia
$^3$ Ural Federal University, 620002 Yekaterinburg, Russia
$^4$ Department of Physics, Abant Izzet Baysal University, Bolu, TR-14280, Turkey

E-mail: tgurel@nku.edu.tr

Received 30 September 2013, revised 28 November 2013
Accepted for publication 2 December 2013
Published 6 January 2014

## Abstract
We present density functional theory calculations on the iron-based pnictides RFeAsO ($\text{R} = \text{Pr}$, $\text{Nd}$, $\text{Sm}$, $\text{Gd}$). The calculations have been carried out using plane waves and the projector augmented wave (PAW) pseudopotential approach. Structural, magnetic and electronic properties are studied within the generalized gradient approximation (GGA) and also within $\text{GGA} + U$ in order to investigate the influence of electron correlation effects. The low-temperature $Cmma$ structure is fully optimized by the GGA considering both non-magnetic and magnetic cells. We have found that the spin-polarized structure improves the agreement with experiments on equilibrium lattice parameters, particularly the $c$ lattice parameter and the Fe–As bond-lengths. The electronic band structure, total density of states, and spin-dependent orbital-resolved density of states are also analyzed and discussed in the frameworks of GGA and $\text{GGA} + U$. For all materials, by including an on-site Coulomb correction, the rare-earth 4f states move away from the Fermi level and the Fermi level features of the systems are found to be mostly defined by the 3d electron–electron correlations in Fe.

Keywords: rare-earth iron-pnictides, electronic structure, first-principles calculations, electronic density of states, electron correlations

(Some figures may appear in colour only in the online journal)

---

## 1. Introduction

The discovery of superconductivity in the fluorine-doped LaFeAsO compound with a critical temperature $T_{\rm c} = 26$ K has generated extensive research on iron-pnictides [1]. By substituting La with other rare-earths such as $\text{R} = \text{Ce}$, $\text{Pr}$, $\text{Nd}$, $\text{Sm}$, and $\text{Gd}$, the critical temperature has been increased up to $\sim 55$ K [2–5]. These new types of superconductors have attracted much attention both experimentally and theoretically because they are the only class of materials that show high-$T_{\rm c}$ other than cuprates. There exist a great number of iron-based superconductors, which can be classified as 1111, 122, 111, 11, 21311 types according to their compositions [6, 7]. Among them, 1111 type compounds have the highest critical temperature and many studies are focused on these materials.

In iron-based oxypnictides, superconductivity emerges with electron doping to the parent compound by fluorine substitution for oxygen ($\text{RFeAsO}_{1-x}\text{F}_x$) or by oxygen deficiencies ($\text{RFeAsO}_{1-\delta}$). Superconductivity is also achieved with hole doping by substituting the related rare-earths by $\text{Sr}$ or $\text{Th}$ [8, 9]. For the parent compound LaFeAsO, a pressure-induced superconductivity is also found with a maximum $T_{\rm c} = 21$ K at $\sim 12$ GPa [10]. In all these methods, superconductivity appears after the suppression

of magnetic ordering. So, to understand the mechanism of superconductivity in iron-based superconductor materials, a detailed knowledge of the magnetic ordering is crucial.

Experimentally, for the undoped R-1111 materials, a crystallographic phase transition from the tetragonal $P4/nmm$ (space group no. 129) structure to the orthorhombic $Cmma$ (space group no. 67) structure is observed around 130–160 K [11–15]. Also, an onset of antiferromagnetic ordering for iron atoms in the temperature range 127–141 K has been found in x-ray and neutron diffraction measurements [11–13, 15, 16]. For the rare-earth atoms, antiferromagnetic ordering has also been measured at very low temperatures in the range 3.7–14 K [13, 15, 17, 18].

After the discovery of superconductivity in this family, a question has arisen about the effects of a strong correlation to the electronic structure, as is the case for cuprates. Although different results are obtained from earlier calculations [19–22], the common idea now is that the correlation strength in iron-pnictides is weak or moderate [23–27].

The electronic structure of the LaFeAsO and CeFeAsO materials has been discussed by many experimental and theoretical studies, but there are few theoretical studies for other rare-earth 1111 materials, particularly with low-temperature $Cmma$ magnetic structures. Alyahyaei and Jishi [28], in their density functional theory (DFT) calculations with the generalized gradient approximation (GGA), have considered various possible magnetic orders for Fe and R ions in the materials CeFeAsO and PrFeAsO and found that, when including the on-site Coulomb interaction (GGA $+$ $U$), the ground state magnetic moments have a stripe-like antiferromagnetic (AFM) order for Fe ions and a zigzag-like AFM order for the rare-earths. In the studies of [29, 30], several collinear and non-collinear magnetic structures of PrFeAsO and CeFeAsO were investigated theoretically, exhibiting similar densities of states (DOS) in different magnetic configurations. The electronic properties of RFeAsO compounds with high-temperature $P4/nmm$ structures were also investigated theoretically by considering rare-earth 4f states as core [31] or valence [32].

In this study, we have performed systematic first-principles calculations for the less studied $Cmma$ magnetic structures of the iron-pnictides PrFeAsO, NdFeAsO, SmFeAsO and GdFeAsO using the density functional formalism within the projector augmented wave method. In the framework of the GGA, structural optimization has been performed and the lattice parameters and bond-lengths have been found to be in good agreement with experimental results when considering the magnetic cell. By using the optimized lattice parameters, the magnetic moments, electronic band structure, and total and projected density of states are calculated by the pure GGA and by including on-site Coulomb interactions (GGA+$U$). The calculated magnetic moments for both Fe and R atoms are found to be overestimated compared to the experimental measurements as encountered in the previous similar calculations. For the compounds considered in this study, the Fe moments do not change with respect to the rare-earth atom but the R moments increase with an increase of rare-earth 4f occupation. From the electronic structure calculations, we have found that the Fermi level features are sensitive to the strength of the correlation parameter of the iron atom.

This paper is organized as follows. In section 2 we give details of the computational methodology and the parameters of the calculations. In section 3 the details of the calculated structural parameters obtained by the optimized magnetic cell and the electronic properties are discussed. We conclude the paper with a brief summary of the main findings of the present study in section 4.

## 2. Computational details

The calculations have been carried out with the generalized gradient approximation to density functional theory as implemented in the QUANTUM ESPRESSO code [33]. The Perdew–Burke–Ernzerhof (PBE) [34] functional is used for the exchange–correlation potential. Wave functions are expanded in terms of plane waves and interactions between ions and valence electrons are represented by projector augmented wave (PAW) atomic potentials. PAW potentials for the rare-earths Pr, Nd, Sm, and Gd have been generated by using the ATOMPAW code [35], where the 5s, 6s, 5p, 5d and 4f states are treated as valence.

For all compounds, a 60 Ryd energy cutoff for the plane waves has been found to be sufficiently converged for optimization and electronic properties. We have used a $6 \times 6 \times 4$ $k$-point grid to describe the Brillouin zone. Since the materials show metallic properties, a 0.02 Ryd Gaussian smearing is used. For structural geometry optimization, we have used the Broyden–Fletcher–Goldfarb–Shanno (BFGS) algorithm with threshold values of 0.001 Ryd au$^{-1}$ and $10^{-4}$ Ryd for residual forces and energy variation, respectively. For GGA $+$ $U$ calculations [36], the effective on-site Coulomb interaction parameters [37] are chosen as $U_{\rm eff}=5$ eV for rare-earths and $U_{\rm eff}=2$ eV and 3 eV for iron atoms, consistent with previous findings [24, 28–30].

## 3. Results and discussion

In this study we have considered the orthorhombic phase with the $Cmma$ space group, which is the reported magnetic structure for low temperatures in iron-pnictides. Wyckoff positions for the atoms are R: $2\text{b}(0, 0.25, z_R)$, Fe: $4\text{b}(0.25, 0, 0.5)$, As: $4\text{g}(0, 0.25, z_{\rm As})$, and O: $4\text{a}(0.25, 0, 0)$, where $z_R$ and $z_{\rm As}$ are the internal coordinate parameters of rare-earth and arsenic atoms respectively [11, 13, 38]. Rare-earths constitute a plane which is sandwiched between oxygen planes and iron planes lie between arsenic planes. In order to account for the magnetic properties, the nuclear unit cell is replaced with an orthorhombic magnetic cell having a total of 16 atoms with four of each element. In the study of Alyahyaei and Jishi [28], DFT calculations are performed in the low-temperature $Cmma$ structure of CeFeAsO and PrFeAsO in order to determine the magnetic order of the ground state. They compared non-magnetic, paramagnetic,

ferromagnetic and three different AFM orders of rare-earth atoms and found that for both CeFeAsO and PrFeAsO, a zigzag-like pattern along the $a$ axis has the lowest energy. For the Fe ions, following the experimental results [11, 13] and theoretical findings [28, 39], we have set the magnetic orders as an AFM stripe-like pattern. AFM ordering has been chosen for rare-earth atoms with a zigzag-like pattern, which is reported as the ground state in [28]. We set the arrangement of rare-earth sites $(0, 0.25, z_{\mathrm{R}})$ and $(0.5, 0.25, -z_{\mathrm{R}})$ as spin-up and $(0, 0.75, -z_{\mathrm{R}})$ and $(0.5, 0.75, z_{\mathrm{R}})$ as spin-down, where $z_{\mathrm{R}}$ is the internal parameter of the rare-earths.

Since the magnetic properties are sensitive to the lattice and internal parameters, we have performed geometric optimization for the 1111 pnictides in the orthorhombic Cmma structure by both considering a non-magnetic nuclear cell and a magnetic cell, and the results are presented in table 1. In R-1111 iron-pnictides, the lattice constants decrease with an increase in the rare-earth atomic number due to the lanthanide compression effect. Optimization calculations are done within the GGA framework. We have found significant discrepancies between the two cells after optimization. In the non-magnetic structure, the calculated equilibrium lattice constants $a$ and $b$ are found to be almost the same, which is not the case in experiments. Furthermore, for all the materials considered in this study, optimized $c$ parameters underestimate experiments, with a discrepancy up to 7.4%. But when we consider the magnetic ordering as described above, we have found that the optimized $c$ parameter agrees well with the experimental measurements, with error less than 2%. A distinction between $a$ and $b$ is also successfully obtained. In the magnetic optimization, the internal parameters of rare-earths $z_{\mathrm{R}}$ and As atoms $z_{\mathrm{As}}$ are found to be much closer to the experimental values than those found in the non-magnetic optimization. It is reported in [42] that using well optimized coordinates is essential for the modeling of the magnetic properties in pnictides. After our spin-polarized GGA optimization calculations, for the Fe–As bond length, we obtained very good agreement with the experimental results for all materials, with a small discrepancy of about $0.02\ \mathring{\mathrm{A}}$.

The magnetic moments for rare-earths and Fe atoms are calculated by considering a GGA optimized magnetic cell and presented in table 2. While the R magnetic moments do not change considerably on including the Coulomb correction, in the case of Fe atoms the magnetic moments increase by about 30% when we use $U_{\mathrm{R}} = 5$ eV and $U_{\mathrm{Fe}} = 2$ eV, and about 40% when we use $U_{\mathrm{R}} = 5$ eV, $U_{\mathrm{Fe}} = 3$ eV. The same increment of Fe magnetic moments was also reported for LaFeAsO [43, 44]. Our results are in agreement with the previous calculations both for the Fe moments and the R moments [29, 30]. However, the magnetic moments of Fe calculated with DFT overestimate the experimental measurements [45]. In iron-pnictides, the experimental moments of Fe are measured as $0.3$–$0.9\ \mu_{\mathrm{B}}$, while the calculated values are larger than $2\ \mu_{\mathrm{B}}$. In our results, it is seen that the Fe magnetic moment does not differ meaningfully with a change of rare-earth atom. Not for RFeAsO but for the other iron-pnictide compound LaFeAsO, the overestimation problem of large magnetic moments for the Fe atom has been studied in the framework of DFT combined with dynamical mean-field theory (DMFT) calculations [46, 47]. In these calculations, when considering the local spin–spin correlation function of the paramagnetic state of LaFeAsO on very short time scales, large Fe moments $(2\ \mu_{\mathrm{B}}$ or more) are observed, just as predicted by spin-polarized DFT calculations. They also suggest that if the electron mobility is high enough, fast fluctuations of the local moment reduce the time-averaged magnetic moments not only for the paramagnetic phase but also for the antiferromagnetic phase. In the recent LDA $+U$ studies of [48, 49], a reduced magnetic moment of Fe in LaFeAsO is obtained by considering a mean-field double counting correction [50]. For the 122 type iron-based compound $\mathrm{BaFe_2As_2}$, a reduction in the magnetic moments of iron is obtained by altering Hund’s rule coupling $J$ with fixed $U$ values in the LDA + DMFT [51] and LDA + Gutzwiller [52] methods. By using the value $J = 0.8$ eV, the LDA + DMFT study of [45] has also calculated an iron magnetic moment of LaFeAsO, in good agreement with experiments.

The experimentally reported moments for Pr as $0.83(9)\ \mu_{\mathrm{B}}$ [53], $0.84(4)\ \mu_{\mathrm{B}}$ [13] and for Nd as $1.55\ \mu_{\mathrm{B}}$ [38] are also very low from our results $2.00\ \mu_{\mathrm{B}}$ for Pr and $3.01\ \mu_{\mathrm{B}}$ for Nd. We have found the moments for Sm as $4.94\ \mu_{\mathrm{B}}$ and for Gd $6.93\ \mu_{\mathrm{B}}$, indicating that within the DFT scheme the rare-earth moments increase with increasing atomic number of the rare-earth element. According to the present calculations, the problem of the large magnetic moment from DFT or DFT $+U$ is not just the case for the Fe moment but also for the rare-earth moments and should be investigated in detail by other methods such as the LDA + DMFT and LDA + Gutzwiller approximations.

Electronic density of states calculations were done for the optimized magnetic cell by considering both GGA and GGA $+U$. Within the GGA $+U$ calculations, the on-site Coulomb interaction parameter for the R ions was set as $U_{\mathrm{eff}} = 5$ eV and for the Fe ions as $U_{\mathrm{eff}} = 2$ and 3 eV. Figures 1–4 show the calculated total and spin-resolved density of states for PrFeAsO, NdFeAsO, SmFeAsO, and GdFeAsO, respectively, with the spin-up occupations in the upper panel and the spin-down occupations in the lower panel. For the material PrFeAsO, our GGA/GGA $+U$ total DOS and partial DOS results are in good agreement with the previous calculations of Alyahyaei and Jishi [28] with the same magnetic configuration and using similar effective Coulomb interaction values of $U_{\mathrm{eff}} = 3$ or 5 eV for Pr and $U_{\mathrm{eff}} = 3.4$ eV for Fe. In the study of Liu *et al* [29], they reported their density of state calculations within a non-collinear magnetic structure considering the effective Coulomb interaction parameters as $U_{\mathrm{eff}} = 4$ eV for Pr and $U_{\mathrm{eff}} = 2$ eV for Fe, and our results are also very similar to this non-collinear magnetic structure.

In the GGA framework, the main contributions to the Fermi level come from the large band Fe 3d and narrow band rare-earth 4f spin-up states, but in the case of the GdFeAsO the Gd 4f spin-up states are well below (positioned at $-4$ eV) the Fermi level (figure 4). In all materials, As p state occupations are larger between $-5.5$ and $-2$ eV compared to the range of

<table><thead><tr><th colspan="2">Param.</th><th colspan="3">PrFeAsO</th><th colspan="3">NdFeAsO</th><th colspan="3">SmFeAsO</th><th colspan="3">GdFeAsO</th></tr><tr><th></th><th></th><th>NM Calc</th><th>Magn. Calc.</th><th>Expt. [13]</th><th>NM Calc</th><th>Magn. Calc.</th><th>Expt. [40]</th><th>NM Calc.</th><th>Magn. Calc.</th><th>Expt. [14]</th><th>NM Calc</th><th>Magn. Calc.</th><th>Expt. [41]</th></tr></thead><tbody><tr><td colspan="2">a</td><td>5.5852</td><td>5.6290</td><td>5.6374</td><td>5.5683</td><td>5.6643</td><td>5.6154</td><td>5.5849</td><td>5.6520</td><td>5.5511</td><td>5.5116</td><td>5.5673</td><td>5.5327</td></tr><tr><td colspan="2">b</td><td>5.5861</td><td>5.5507</td><td>5.6063</td><td>5.5686</td><td>5.5977</td><td>5.5856</td><td>5.5846</td><td>5.6446</td><td>5.5788</td><td>5.5098</td><td>5.4734</td><td>5.5120</td></tr><tr><td colspan="2">c</td><td>7.9570</td><td>8.4213</td><td>8.5966</td><td>7.9554</td><td>8.4117</td><td>8.5591</td><td>7.9974</td><td>8.4917</td><td>8.4701</td><td>7.9302</td><td>8.3048</td><td>8.3956</td></tr><tr><td colspan="2">zR</td><td>0.1529</td><td>0.1460</td><td>0.1385</td><td>0.1500</td><td>0.1432</td><td>0.1390</td><td>0.1471</td><td>0.1401</td><td>0.1374</td><td>0.1403</td><td>0.1393</td><td>0.1363</td></tr><tr><td colspan="2">zAs</td><td>0.6520</td><td>0.6570</td><td>0.6565</td><td>0.6526</td><td>0.6552</td><td>0.6587</td><td>0.6507</td><td>0.6521</td><td>0.6612</td><td>0.3443</td><td>0.6599</td><td>0.6677</td></tr><tr><td colspan="2">Fe–As</td><td>2.3155</td><td>2.3773</td><td>2.400</td><td>2.3124</td><td>2.3801</td><td>2.401</td><td>2.3131</td><td>2.3754</td><td>2.3947</td><td>2.3065</td><td>2.3601</td><td>2.379</td></tr><tr><td colspan="2">Fe–As</td><td>2.3160</td><td>2.3778</td><td></td><td>2.3126</td><td>2.3807</td><td></td><td>2.3132</td><td>2.3763</td><td></td><td>2.3069</td><td>2.3606</td><td></td></tr><tr><td colspan="2">Fe–Fe</td><td>2.7927</td><td>2.7753</td><td></td><td>2.7843</td><td>2.7988</td><td></td><td>2.7923</td><td>2.8223</td><td></td><td>2.7548</td><td>2.7366</td><td></td></tr><tr><td colspan="2">Fe–Fe</td><td>2.7930</td><td>2.8146</td><td>2.8030</td><td>2.7843</td><td>2.8323</td><td>2.7928</td><td>2.7925</td><td>2.8260</td><td>2.7755</td><td>2.7559</td><td>2.7838</td><td>2.756</td></tr><tr><td colspan="2">R–O</td><td>2.3193</td><td>2.3271</td><td>2.8190</td><td>2.3020</td><td>2.3199</td><td>2.8077</td><td>2.2984</td><td>2.3227</td><td>2.7894</td><td>2.2434</td><td>2.2690</td><td></td></tr><tr><td colspan="2">R–O</td><td>2.3195</td><td>2.3272</td><td>2.3170</td><td>2.3021</td><td>2.3292</td><td>2.310</td><td>2.2988</td><td>2.3248</td><td>2.2860</td><td>2.2436</td><td>2.2690</td><td>2.263</td></tr><tr><td colspan="2">R–As</td><td>3.1951</td><td>3.2339</td><td></td><td>3.1968</td><td>3.2796</td><td></td><td>3.2256</td><td>3.3303</td><td></td><td>3.1947</td><td>3.2048</td><td></td></tr><tr><td colspan="2">R–As</td><td>3.1954</td><td>3.2676</td><td>3.3110</td><td>3.1970</td><td>3.3084</td><td>3.286</td><td>3.2265</td><td>3.3334</td><td>3.2580</td><td>3.1956</td><td>3.2449</td><td>3.235</td></tr><tr><td colspan="2"></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>3.244</td></tr></tbody></table>

Table 1. Optimized structural parameters and bond-lengths for theCmmaphase using a non-magnetic (NM) cell and a magnetic cell within the GGA in units of Å.

![](./images/813168194121367554_1.jpg)

Figure 1. Total and spin projected density of states of PrFeAsO for the considered magnetic structure. The Fermi level is set to zero.
(a) DOS without the Coulomb interaction (GGA). (b) DOS with the Coulomb interaction (GGA $+U$, $U_{\text{eff}}=2$ or $3$ eV for Fe and $U_{\text{eff}}=5$ eV for Pr).

<table>
<caption>Table 2. Calculated magnetic moments of rare-earth (R) and Fe atoms.</caption>
<tbody>
<tr>
<th>Calc. type</th>
<td>PrFeAsO</td>
<td>NdFeAsO</td>
<td>SmFeAsO</td>
<td>GdFeAsO</td>
</tr>
<tr>
<th colspan="5">R magnetic moment in $\mu_{\text{B}}$</th>
</tr>
<tr>
<th>GGA</th>
<td>1.95</td>
<td>3.09</td>
<td>5.13</td>
<td>6.82</td>
</tr>
<tr>
<th>GGA $+U$ ($U_{\text{R}}=5$ eV, $U_{\text{Fe}}=2$ eV)</th>
<td>2.00</td>
<td>3.01</td>
<td>4.93</td>
<td>6.93</td>
</tr>
<tr>
<th>GGA $+U$ ($U_{\text{R}}=5$ eV, $U_{\text{Fe}}=3$ eV)</th>
<td>2.01</td>
<td>3.02</td>
<td>4.94</td>
<td>6.93</td>
</tr>
<tr>
<th>GGA $+U$ [29]</th>
<td>1.96</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<th>GGA $+U$ ($U_{\text{R}}=3$ eV, $U_{\text{Fe}}=0$ eV) [30]</th>
<td>1.94</td>
<td>2.85</td>
<td></td>
<td></td>
</tr>
<tr>
<th colspan="5">Fe magnetic moment in $\mu_{\text{B}}$</th>
</tr>
<tr>
<th>GGA</th>
<td>1.95</td>
<td>2.02</td>
<td>2.03</td>
<td>1.72</td>
</tr>
<tr>
<th>GGA $+U$ ($U_{\text{R}}=5$ eV, $U_{\text{Fe}}=2$ eV)</th>
<td>2.63</td>
<td>2.68</td>
<td>2.62</td>
<td>2.56</td>
</tr>
<tr>
<th>GGA $+U$ ($U_{\text{R}}=5$ eV, $U_{\text{Fe}}=3$ eV)</th>
<td>2.80</td>
<td>2.81</td>
<td>2.78</td>
<td>2.73</td>
</tr>
<tr>
<th>GGA $+U$ [29]</th>
<td>2.83</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<th>GGA $+U$ ($U_{\text{R}}=3$ eV, $U_{\text{Fe}}=0$ eV) [30]</th>
<td>2.03</td>
<td>1.89</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

$-2$ to $0$ eV. O p states are also well below the Fermi energy and occur between $\sim-5.5$ and $-2$ eV.

When we include Coulomb correction, all compounds display semi-metallic behavior, contrary to the GGA metallic characteristics. 4f states of all rare-earths move away from the Fermi level, as expected. The rare-earth 4f states separation is found to be largest in GdFeAsO. By contrast with other materials, the spin-up Sm 4f states of SmFeAsO are located in two different regions, one around $5$ eV below the Fermi level and the other around $0.4$ eV above the Fermi level, as also reported in previous calculations [54]. Using an effective value of $U_{\text{eff}}=5$ eV for the rare-earth atoms, the positions of the occupied and unoccupied 4f states are in good agreement with the x-ray photoelectron spectroscopy (XPS) and bremsstrahlung isochromat spectroscopy (BIS) results of elemental metals [55].

As for the other states, one important feature is that the As p states occupy a large region from $-5$ eV to just below the Fermi level by showing hybridization features with the Fe 3d states. The O p states are not affected by the inclusion of the Coulomb interaction and exhibit minor hybridization effects.

We have also calculated the electronic band structure of the materials in the orthorhombic magnetic cell with space group $Cmma$ along the directions $\Gamma$–X–Y–S–$\Gamma$–Z throughout the Brillouin zone and focused around the Fermi level (figure 5). In PrFeAsO, NdFeAsO, and GdFeAsO materials, the choice of $U_{\text{eff}}$ value of Fe as 2 or 3 eV displays significant differences. There is no gap when the Fe $U_{\text{eff}}$ value is set to $2$ eV, but a gap occurs with a value about $0.25$ eV in the case

![](./images/813168194121367554_2.jpg)

Figure 2. Total and spin projected density of states of NdFeAsO for the considered magnetic structure. The Fermi level is set to zero.
(a) DOS without the Coulomb interaction (GGA). (b) DOS with the Coulomb interaction (GGA $+U$, $U_{\text{eff}} = 2$ or $3$ eV for Fe and
$U_{\text{eff}} = 5$ eV for Nd).

![](./images/813168194121367554_3.jpg)

Figure 3. Total and spin projected density of states of SmFeAsO for the considered magnetic structure. The Fermi level is set to zero.
(a) DOS without the Coulomb interaction (GGA). (b) DOS with the Coulomb interaction (GGA $+U$, $U_{\text{eff}} = 2$ or $3$ eV for Fe and
$U_{\text{eff}} = 5$ eV for Sm).

of $U_{\text{eff}} = 3$ eV. All these results allow us to conclude that a correct determination of the strength of electron correlation in iron-pnictides is necessary to describe their magnetic properties and electronic structure.

## 4. Conclusion

In this study, we have investigated the structural, magnetic, and electronic properties of rare-earth iron-pnictides RFeAsO

![](./images/813168194121367554_4.jpg)

Figure 4. Total and spin projected density of states of GdFeAsO for the considered magnetic structure. The Fermi level is set to zero. (a) DOS without the Coulomb interaction (GGA). (b) DOS with the Coulomb interaction (GGA $+U$, $U_{\rm eff}=2$ or 3 eV for Fe and $U_{\rm eff}=5$ eV for Gd).

![](./images/813168194121367554_5.jpg)

Figure 5. GGA $+U$ electronic band structure of (a) PrFeAsO, (b) NdFeAsO, (c) SmFeAsO, and (d) GdFeAsO in the simple orthorhombic magnetic cell with space group Cmma. The Fermi level is set to zero. Black lines are for $U(5,3)$ eV and red lines are for $U(5,2)$. While the full lines are for spin-up states, the dashed lines are for spin-down states.

($R={\rm Pr,\ Nd,\ Sm,\ Gd}$) within the GGA and GGA $+U$ using plane waves and PAW atomic potentials. The low-temperature Cmma structure is optimized by considering non-magnetic and magnetic structures and we have found better agreement for the case of a magnetic cell for all lattice parameters. While the structural parameters are well described by spin-polarized DFT calculations, the magnetic moments are largely overestimated, as found in previous calculations. According to our calculations, the overestimation problem not only occurs for the Fe atoms, but also for the rare-earth atoms. In GGA $+U$, the Fe moments are increased by about 30-40% compared to GGA, as reported before, but

the R moments do not change significantly on including the Coulomb effects. The magnetic moments of rare-earths become larger with increasing rare-earth atomic number. The problem of overestimation of the magnetic moment of these R-1111 iron-pnictides other than in LaFeAsO needs further investigations not only for the Fe atom, but also for the rare-earth atoms.

The electronic band structure, total and projected density of states of the materials are also investigated. The metallic behavior of GGA transforms to a semi-metallic scheme within GGA + U, with the major effect being R 4f state separation from the Fermi level. The positions of the rare-earth 4f states of all materials with $U_{\text{eff}} = 5$ eV are found to be in good agreement with elemental rare-earth crystal spectroscopy experiments. Fe d states also have a shift whose magnitude is controlled by the $U_{\text{eff}}$ value of the Fe atom. For PrFeAsO, NdFeAsO, and GdFeAsO we have found that a larger value ($U_{\text{eff}} = 3$ eV) opens a small gap of about 0.25 eV, but when $U_{\text{eff}} = 2$ eV, bands cross Fermi level. Significant hybridization between Fe 3d and As p states is also observed.

## Acknowledgments
This work was supported by the Scientific and Technological Research Council of Turkey (TUBITAK Project No. TBAG-111T796) and the Russian Foundation for Basic Research (Project No. 12-02-91371-CT_a), Program of the Russian Academy of Science Presidium Quantum Microphysics of Condensed Matter 12-P-2-1017, the Dynasty Foundation, and the Ministry of Education and Science of the Russian Federation through Project 14.A18.21.0076. The supports are gratefully acknowledged.

## References
[1] Kamihara Y, Watanabe T, Hirano M and Hosono H 2008 J. Am. Chem. Soc. **130** 3296

[2] Chen G F, Li Z, Wu D, Li G, Hu W Z, Dong J, Zheng P, Luo J L and Wang N L 2008 Phys. Rev. Lett. **100** 247002

[3] Chen X H, Wu T, Wu G, Liu R H, Chen H and Fang D F 2008 Nature **453** 761

[4] Ren Z-A *et al* 2008 Europhys. Lett. **83** 17002

[5] Ren Z-A *et al* 2008 Chin. Phys. Lett. **25** 2215

[6] Johnston D C 2010 Adv. Phys. **59** 803

[7] Wen H-H and Li S 2011 Annu. Rev. Condens. Matter Phys. **2** 121

[8] Wen H-H, Mu G, Fang L, Yang H and Zhu X 2008 Europhys. Lett. **82** 17009

[9] Wang C *et al* 2008 Europhys. Lett. **83** 67006

[10] Okada H, Igawa K, Takahashi K, Kamihara Y, Hirano M, Hosono H, Matsubayashi K and Uwatoko Y 2008 J. Phys. Soc. Japan **77** 113712

[11] Zhao J *et al* 2008 Nature Mater. **7** 953

[12] de la Cruz C *et al* 2008 Nature **453** 899

[13] Zhao J *et al* 2008 Phys. Rev. B **78** 132504

[14] Margadonna S, Takabayashi Y, McDonald M T, Brunelli M, Wu G, Liu R H, Chen X H and Prassides K 2009 Phys. Rev. B **79** 014503

[15] Tian W *et al* 2010 Phys. Rev. B **82** 060514

[16] Chen Y, Lynn J W, Li J, Li G, Chen G F, Luo J L, Wang N L, Dai P, de la Cruz C and Mook H A 2008 Magnetic order of the iron spins in NdFeAsO Phys. Rev. B **78** 064515

[17] Ding L, He C, Dong J K, Wu T, Liu R H, Chen X H and Li S Y 2008 Phys. Rev. B **77** 180510

[18] Jesche A, Krellner C, de Souza M, Lang M and Geibel C 2009 New J. Phys. **11** 103050

[19] Haule K, Shim J H and Kotliar G 2008 Phys. Rev. Lett. **100** 226402

[20] Craco L, Laad M S, Leoni S and Rosner H 2008 Phys. Rev. B **78** 134511

[21] Nakamura K, Arita R and Imada M 2008 J. Phys. Soc. Japan **77** 093711

[22] Anisimov V I, Korotin D M, Streltsov S V, Kozhevnikov A V, Kuneš J, Shorikov A O and Korotin M A 2008 JETP Lett. **88** 729

[23] Yang W L *et al* 2009 Phys. Rev. B **80** 014508

[24] Anisimov V I, Korotin D M, Korotin M A, Kozhevnikov A V, Kuneš J, Shorikov A O and Skornyakov S L and Streltsov S V 2009 J. Phys.: Condens. Matter **21** 075602

[25] Anisimov V I, Kurmaev E Z, Moewes A and Izyumov I A 2009 Physica C **469** 442

[26] Skornyakov S L, Efremov A V, Skorikov N A, Korotin M A, Izyumov Y A, Anisimov V I, Kozhevnikov A V and Vollhardt D 2009 Phys. Rev. B **80** 092501

[27] Jarrige I *et al* 2012 Phys. Rev. B **86** 115104

[28] Alyahyaei H M and Jishi R A 2009 Phys. Rev. B **79** 064516

[29] Liu J, Luo B, Laskowski R and Yao K L 2011 Europhys. Lett. **93** 17003

[30] Liu J, Luo B, Sun Z, Fu H and Yao K 2011 Phys. Rev. B **84** 115123

[31] Nekrasov I A, Pchelkina Z V and Sadovskii M V 2008 JETP Lett. **87** 560

[32] Pourovskii L, Vildosola V, Biermann S and Georges A 2008 Europhys. Lett. **84** 37006

[33] Giannozzi P *et al* 2009 J. Phys.: Condens. Matter **21** 395502

[34] Perdew J P, Burke K and Ernzerhof M 1996 Phys. Rev. Lett. **77** 3865

[35] Holzwarth N A W, Tackett A R and Matthews G E 2001 Comput. Phys. Commun. **135** 329

[36] Anisimov V I, Zaanen J and Andersen O K 1991 Phys. Rev. B **44** 943

[37] Cococcioni M and de Gironcoli S 2005 Phys. Rev. B **71** 035105

[38] Qiu Y *et al* 2008 Phys. Rev. Lett. **101** 257002

[39] Yildirim T 2008 Phys. Rev. Lett. **101** 057010

[40] Marcinkova A, Suard E, Fitch A N, Margadonna S and Bos J W G 2009 Chem. Mater. **21** 2967

[41] Nitsche F, Doert T and Ruck M 2013 Solid State Sci. **19** 162

[42] Mazin I I, Johannes M D, Boeri L, Koepernik K and Singh D J 2008 Phys. Rev. B **78** 085104

[43] Ishibashi S and Terakura K 2008 J. Phys. Soc. Japan **77** 91

[44] Nakamura H, Hayashi N, Nakai N, Okumura M and Machida M 2009 Physica C **469** 908

[45] Aichhorn M, Pourovskii L and Georges A 2011 Phys. Rev. B **84** 054529

[46] Hansmann P, Arita R, Toschi A, Sakai S, Sangiovanni G and Held K 2010 Phys. Rev. Lett. **104** 197002

[47] Toschi A, Arita R, Hansmann P, Sangiovanni G and Held K 2012 Phys. Rev. B **86** 064411

[48] Cricchio F, Grånäs O and Nordström L 2010 Phys. Rev. B **81** 140403

[49] Machida M and Nakamura H 2011 Physica C **471** 659

[50] Czyżyk M T and Sawatzky G A 1994 Phys. Rev. B **49** 14211

[51] Yin Z P, Haule K and Kotliar G 2011 Nature Phys. **7** 294

[52] Yao Y X, Smalian J, Wang C Z, Ho K M and Kotliar G 2011 Phys. Rev. B **84** 245112

[53] Kimber S A J *et al* 2008 Phys. Rev. B **78** 140503

[54] Antonov V N, Harmon B N and Yaresko A N 2002 Phys. Rev. B **66** 165209

[55] Lang J K, Baer Y and Cox P A 1981 J. Phys. F: Met. Phys. **11** 121