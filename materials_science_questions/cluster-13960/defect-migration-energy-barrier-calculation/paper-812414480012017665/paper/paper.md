# TRAPPING AND SOLUTION OF FISSION Xe IN UO₂.
## Part 1. Single gas atoms and solution from underpressurized bubbles

R.A. JACKSON and C.R.A. CATLOW

Department of Chemistry, University College London, 20 Gordon Street, London WC1H OAJ, UK

Received 7 July 1984; accepted 6 September 1984

We present results of a new theoretical survey of the energetics of fission Xe in $\mathrm{UO}_{2}$, in which improved gas-lattice potentials are employed, and calculations performed for a range of temperatures. We concentrate on single gas atom trapping and migration and their solution from underpressurized bubbles.

## 1. Introduction

There is an increasing need in studies of the behaviour of fission gas in reactor fuels for reliable information on the structural and energetic properties of fission gas. In a previous study [1] we attempted to calculate the energetics of formation of single gas atom traps in $\mathrm{UO}_{2}$, and concluded that cation/anion vacancy aggregates were of greatest importance. In this paper we re-examine our predictions for single gas atoms in the light of improvements in the modelling of gas-lattice interactions; in addition energetic properties are calculated for a range of temperatures. Furthermore, solution energies for fission Xe in $\mathrm{UO}_{2}$ are calculated for different composition regions assuming that solution occurs from underpressurized bubbles, which we define as bubbles in which the gas density is such that interactions between gas atoms can be ignored. In Part 2 of this study (see p. 167 of this issue), we shall consider the converse condition of solution from highly overpressurized bubbles.

## 2. Computational methods

Calculations of the energies required to trap Xe atoms at various vacancies and vacancy aggregates in $\mathrm{UO}_{2}$ are performed using the HADES program [2-5]. This uses well established methods for simulating defects in ionic crystals. The essential feature of these methods is the division of the lattice into two regions, the inner region surrounding the defect where explicit lattice simulation is used with specific lattice-ion and defect pair potentials, and the remainder of the crystal which is treated as a dielectric continuum. Detailed discussions of the techniques employed are available [4,5], and the method has been applied to a diverse range of ionic crystals, including $\mathrm{UO}_{2}[6,7]$. Further references are given in ref. [1].

The calculations require the specification of potentials both for the interactions of the lattice ions and for the interactions of the lattice ions and defect species - in this case gas-lattice interactions. These interactions are discussed separately below.

### 2.1. The lattice potential

A fully ionic model for $\mathrm{UO}_{2}$ is used [6] in which the ions are assumed to have integral charges, ionic polarization being treated by the shell model [8]. Short-range interactions of ions are also considered for first and second nearest neighbours; for first nearest neighbours (cation-anion interactions) a repulsive Born-Mayer potential is used, while for second nearest neighbours we use a Buckingham potential (i.e. an attractive $r^{-6}$ term is included). These potentials are parameterized by fitting to bulk crystal properties, with the exception of the anion-anion interaction, which is calculated by ab-initio Hartree-Fock methods. Two potentials describing this interaction are used; the first is that employed in ref. [1], and is in the Buckingham form; the second [9] is in the spline form. It was found necessary to make use of this second potential to achieve convergence in some of the calculations. The justification for

0022-3115/85/$03.30 © Elsevier Science Publishers B.V.
(North-Holland Physics Publishing Division)

Table 1
Lattice potential for $\mathrm{UO}_{2}$

(a) $\mathrm{U}^{4+}-\mathrm{O}^{2-}$ potential (Born-Mayer form)
<table>
<thead>
  <tr>
    <th>$A(\mathrm{eV})$</th>
    <th>$\rho(\mathring{\mathrm{A}})$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>1217.8</td>
    <td>0.3871</td>
  </tr>
</tbody>
</table>

(b) $\mathrm{O}^{2-}-\mathrm{O}^{2-}$ potential (Buckingham form)
<table>
<thead>
  <tr>
    <th>$A(\mathrm{eV})$</th>
    <th>$\rho(\mathring{\mathrm{A}})$</th>
    <th>$C(\mathrm{eV}\ \mathring{\mathrm{A}}^{6})$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>22764.3</td>
    <td>0.1490</td>
    <td>112.2</td>
  </tr>
</tbody>
</table>

(c) $\mathrm{O}^{2-}-\mathrm{O}^{2-}$ potential (spline form)
<table>
<thead>
  <tr>
    <th>$A(\mathrm{eV})$</th>
    <th>$\rho(\mathring{\mathrm{A}})$</th>
    <th>$C(\mathrm{eV}\ \mathring{\mathrm{A}}^{6})$</th>
    <th>$r_{\mathrm{b}}(\mathring{\mathrm{A}})$</th>
    <th>$r_{\mathrm{m}}(\mathring{\mathrm{A}})$</th>
    <th>$r_{\mathrm{c}}(\mathring{\mathrm{A}})$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>20378.0</td>
    <td>0.12537</td>
    <td>114.0</td>
    <td>1.159</td>
    <td>1.65</td>
    <td>2.7299</td>
  </tr>
</tbody>
</table>

(d) Shell charges and spring constants
<table>
<thead>
  <tr>
    <th></th>
    <th>$Y/|e|$</th>
    <th>$K(\mathrm{eV}/\mathring{\mathrm{A}}^{2})$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$\mathrm{U}^{4+}$</td>
    <td>6.54</td>
    <td>103.38</td>
  </tr>
  <tr>
    <td>$\mathrm{O}^{2-}$</td>
    <td>$-4.40$</td>
    <td>292.98</td>
  </tr>
</tbody>
</table>

the use of these two potentials interchangeably is that where both produce satisfactory convergence there is a negligible difference in the final energies.

The potential parameters are given in table 1. For details concerning spline knots $r_{\mathrm{b}}, r_{\mathrm{m}}$ and $r_{\mathrm{c}}$, see ref. [9].

Table 2
Gas-lattice potential

(a) $\mathrm{Xe}-\mathrm{U}^{4+}$ potential (Born-Mayer form)
<table>
<thead>
  <tr>
    <th>$A(\mathrm{eV})$</th>
    <th>$\rho(\mathring{\mathrm{A}})$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>2787.7</td>
    <td>0.41426</td>
  </tr>
</tbody>
</table>

(b) $\mathrm{Xe}-\mathrm{O}^{2-}$ potential (cubic spline form)
<table>
<thead>
  <tr>
    <th>Knot position($\mathring{\mathrm{A}}$)</th>
    <th>Value of function($\mathrm{eV}$)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>2.000</td>
    <td>5.82629447</td>
  </tr>
  <tr>
    <td>2.3125</td>
    <td>2.82244869</td>
  </tr>
  <tr>
    <td>2.6250</td>
    <td>1.42011230</td>
  </tr>
  <tr>
    <td>2.9375</td>
    <td>0.67901399</td>
  </tr>
  <tr>
    <td>3.2500</td>
    <td>0.32051990</td>
  </tr>
  <tr>
    <td>3.5625</td>
    <td>0.14276991</td>
  </tr>
  <tr>
    <td>3.8750</td>
    <td>0.05475358</td>
  </tr>
  <tr>
    <td>4.1875</td>
    <td>0.01886148</td>
  </tr>
  <tr>
    <td>4.5000</td>
    <td>0.00785324</td>
  </tr>
</tbody>
</table>

(c) Shell charges and spring constants
<table>
<thead>
  <tr>
    <th></th>
    <th>$Y/|e|$</th>
    <th>$K(\mathrm{eV}/\mathring{\mathrm{A}}^{2})$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Xe</td>
    <td>$-11.3$</td>
    <td>460.8</td>
  </tr>
</tbody>
</table>

### 2.2. The gas-lattice potential

As in the previous study [1], gas-lattice potentials are calculated using the electron-gas method. However, in the present work, the electron densities of the interacting species are obtained using relativistic Hartree-Fock wavefunctions, whereas previously non-relativistic wavefunctions were used. Relativistic effects are expected to be important where heavy ions are involved. Details of the computer programs used to calculate these potentials are given elsewhere [10]. An additional feature of these calculations is that the $\mathrm{O}^{2-}$ ion is stabilized in a spherical, Madelung potential well, appropriate for an $\mathrm{O}^{2-}$ ion in $\mathrm{UO}_{2}$.

The potential parameters are given in table 2. The $\mathrm{Xe}-\mathrm{U}^{4+}$ potential was fitted to a Born-Mayer form, but when this procedure was tried for the $\mathrm{Xe}-\mathrm{O}^{2-}$ potential, it was found to give a very poor fit, so the potential was fitted to a cubic spline form which gave an improved fit.

### 2.3. Inclusion of temperature effects

The effect of temperature is included in our calculations by using the lattice constant appropriate to each temperature. The following values were used [11]:

<table>
<thead>
  <tr>
    <th>Temperature (K)</th>
    <th>298</th>
    <th>1773</th>
    <th>2273</th>
    <th>2773</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Lattice constant ($\mathring{\mathrm{A}}$)</td>
    <td>2.734</td>
    <td>2.779</td>
    <td>2.794</td>
    <td>2.809</td>
  </tr>
</tbody>
</table>

Previous studies of e.g. defect energies in $\mathrm{AgCl}$ [12] have shown that such quasiharmonic treatments of defect energies yield reliable results.

## 3. Trapping sites considered

$\mathrm{UO}_{2}$ crystallizes in the fluorite structure, which is a primitive cubic array of anions with half the cube centres occupied by cations. The treatment of gas trapping in ref. [1] referred all energies to that of the interstitial sites, and it was assumed that the body-centre interstitial sites (the vacant cube centres) would be occupied. We should emphasize that in this study energies are referred to an isolated gas atom in free space.

The trapping sites considered are as in ref. [1]: cation and anion vacancies, and vacancy aggregates which could be important because of the large size of the gas atoms. The vacancy aggregates considered are listed below.

(1) The divacancy consisting of one cation and one anion vacancy.

![](./images/812414480012017665_1.jpg)

Figs. 1 (top left), 2 (top right) and 3 (bottom).

(2) The neutral trivacancy, comprising one cation and two anion vacancies. There are a number of alternative structures possible for this trivacancy. These alternative configurations were considered; that shown in fig. 1 has the lowest energy when a Xe atom is present in the trap, a linear configuration having an energy 0.86 eV higher at 298 K; higher energies for this configuration are obtained for the higher temperatures.

(3) The charged trivacancy, comprising one anion and two cation vacancies. This is shown in fig. 2.

(4) The tetravacancy, comprising two cation and two anion vacancies. This is shown in fig. 3.

## 4. Results of calculations

This section is divided into three parts. In the first part, we present the results of calculations on both the creation of the various trap sites, and the trapping of Xe atoms at these sites. In the second part we use these results to calculate solution energies of Xe atoms in

<table>
<caption>Table 3 Defect energies</caption>
<thead>
<tr>
<th>Site</th>
<th colspan="4">Energies (eV)</th>
</tr>
<tr>
<th></th>
<th>T = 298 K</th>
<th>1773 K</th>
<th>2273 K</th>
<th>2773 K</th>
</tr>
</thead>
<tbody>
<tr>
<td>Anion vacancy</td>
<td>34.46</td>
<td>30.98</td>
<td>29.78</td>
<td>28.55</td>
</tr>
<tr>
<td>Cation vacancy</td>
<td>87.89</td>
<td>85.70</td>
<td>84.96</td>
<td>84.23</td>
</tr>
<tr>
<td>Divacancy</td>
<td>100.85</td>
<td>99.01</td>
<td>98.34</td>
<td>97.65</td>
</tr>
<tr>
<td>Neutral trivacancy</td>
<td>114.72</td>
<td>113.12</td>
<td>112.51</td>
<td>111.86</td>
</tr>
<tr>
<td>Charged trivacancy</td>
<td>179.84</td>
<td>176.89</td>
<td>175.82</td>
<td>175.10</td>
</tr>
<tr>
<td>Tetravacancy</td>
<td>191.08</td>
<td>189.09</td>
<td>188.23</td>
<td>186.13</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 4 Unoccupied trap energies</caption>
<thead>
<tr>
<th>Site</th>
<th colspan="4">Energies (eV)</th>
</tr>
<tr>
<th></th>
<th>T = 298 K</th>
<th>1773 K</th>
<th>2273 K</th>
<th>2773 K</th>
</tr>
</thead>
<tbody>
<tr>
<td>Anion vacancy</td>
<td>16.65</td>
<td>16.37</td>
<td>16.34</td>
<td>16.30</td>
</tr>
<tr>
<td>Cation vacancy</td>
<td>80.42</td>
<td>78.56</td>
<td>78.20</td>
<td>77.82</td>
</tr>
<tr>
<td>Divacancy</td>
<td>94.08</td>
<td>93.35</td>
<td>93.07</td>
<td>92.75</td>
</tr>
<tr>
<td>Neutral trivacancy</td>
<td>110.23</td>
<td>108.76</td>
<td>108.59</td>
<td>108.16</td>
</tr>
<tr>
<td>Charged trivacancy</td>
<td>174.42</td>
<td>172.37</td>
<td>171.74</td>
<td>171.23</td>
</tr>
<tr>
<td>Tetravacancy</td>
<td>186.82</td>
<td>185.24</td>
<td>184.73</td>
<td>184.17</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 5 Trap formation energies</caption>
<tbody>
<tr>
<td colspan="5">(a) Anion-deficient UO₂</td>
</tr>
<tr>
<td>Site</td>
<th colspan="4">Energies (eV)</th>
</tr>
<tr>
<td></td>
<th>T = 298 K</th>
<th>1773 K</th>
<th>2273 K</th>
<th>2773 K</th>
</tr>
<tr>
<td>Anion vacancy</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
</tr>
<tr>
<td>Cation vacancy</td>
<td>10.63</td>
<td>8.33</td>
<td>7.97</td>
<td>7.59</td>
</tr>
<tr>
<td>Divacancy</td>
<td>13.62</td>
<td>9.91</td>
<td>9.44</td>
<td>8.96</td>
</tr>
<tr>
<td>Neutral trivacancy</td>
<td>7.14</td>
<td>5.79</td>
<td>5.68</td>
<td>5.33</td>
</tr>
<tr>
<td>Charged trivacancy</td>
<td>18.19</td>
<td>15.54</td>
<td>14.94</td>
<td>14.47</td>
</tr>
<tr>
<td>Tetravacancy</td>
<td>13.94</td>
<td>12.04</td>
<td>11.59</td>
<td>11.11</td>
</tr>
<tr>
<td colspan="5">(b) Stoichiometric UO₂</td>
</tr>
<tr>
<td>Site</td>
<th colspan="4">Energies (eV)</th>
</tr>
<tr>
<td></td>
<th>T = 298 K</th>
<th>1773 K</th>
<th>2273 K</th>
<th>2773 K</th>
</tr>
<tr>
<td>Anion vacancy</td>
<td>2.66</td>
<td>2.34</td>
<td>2.27</td>
<td>2.20</td>
</tr>
<tr>
<td>Cation vacancy</td>
<td>5.31</td>
<td>3.65</td>
<td>3.43</td>
<td>3.19</td>
</tr>
<tr>
<td>Divacancy</td>
<td>10.96</td>
<td>7.57</td>
<td>7.17</td>
<td>6.76</td>
</tr>
<tr>
<td>Neutral trivacancy</td>
<td>7.14</td>
<td>5.79</td>
<td>5.68</td>
<td>5.33</td>
</tr>
<tr>
<td>Charged trivacancy</td>
<td>10.21</td>
<td>8.52</td>
<td>8.13</td>
<td>7.87</td>
</tr>
<tr>
<td>Tetravacancy</td>
<td>8.62</td>
<td>7.36</td>
<td>7.05</td>
<td>6.71</td>
</tr>
<tr>
<td colspan="5">(c) Anion-excess UO₂</td>
</tr>
<tr>
<td>Site</td>
<th colspan="4">Energies (eV)</th>
</tr>
<tr>
<td></td>
<th>T = 298 K</th>
<th>1773 K</th>
<th>2273 K</th>
<th>2773 K</th>
</tr>
<tr>
<td>Anion vacancy</td>
<td>5.32</td>
<td>4.68</td>
<td>4.54</td>
<td>4.40</td>
</tr>
<tr>
<td>Cation vacancy</td>
<td>−0.01</td>
<td>−1.03</td>
<td>−1.11</td>
<td>−1.21</td>
</tr>
<tr>
<td>Divacancy</td>
<td>8.3</td>
<td>5.23</td>
<td>4.9</td>
<td>4.56</td>
</tr>
<tr>
<td>Neutral trivacancy</td>
<td>7.14</td>
<td>5.79</td>
<td>5.68</td>
<td>5.33</td>
</tr>
<tr>
<td>Charged trivacancy</td>
<td>2.23</td>
<td>1.5</td>
<td>1.32</td>
<td>1.27</td>
</tr>
<tr>
<td>Tetravacancy</td>
<td>3.3</td>
<td>2.68</td>
<td>2.51</td>
<td>2.31</td>
</tr>
</tbody>
</table>

UO₂ from underpressurized bubbles, for the different composition regions, and under different conditions. In the third part migration mechanisms for single gas atoms are considered.

### 4.1. Calculations on creation of trap sites and the trapping of Xe atoms at these sites

Defect energies are given in table 3. These are the energies required to introduce the gas atom from infinity, and to create the trapping site by displacement of the lattice ions to infinity. In table 4, unoccupied trap energies are given. These correspond to the energies required to create the trapping site by displacement of the lattice ions to infinity. Trap formation energies are given in table 5. These energies are related to the concentration of a given trapping site in the lattice through the equation

$$C_{\mathrm{t}}=S_{\mathrm{t}} \exp \left(-E_{\mathrm{t}} / k T\right). \tag{1}$$

In this equation $C_{\mathrm{T}}$ is the trap concentration, $S_{\mathrm{T}}$ the entropy of trap formation, and $E_{\mathrm{T}}$ is the trap formation energy. Expressions for the calculation of the trap formation energies are given in Appendix 1.

### 4.2. Solution energies for Xe atoms in $\boldsymbol{UO}_{2}$ (from underpressurized bubbles)

We now make use of the results given in section 4.1 to calculate solution energies for Xe atoms at the various trap sites in $\mathrm{UO}_{2}$. Two different cases are distinguished, the first being where trap sites are pre-existent due to radiation damage, and the second and probably more important case being where the defect population of the crystal is in full thermodynamic equilibrium.

#### 4.2.1. Case where trap sites are pre-existent.

In this case the solution energy is defined as the energy required to introduce an isolated gas atom to a pre-existent trap site. In terms of the energies tabulated in the first part of this section, it is defined as follows.
Solution energy = defect energy - unoccupied trap energy

Solution energies for the case of pre-existent trap sites are given in table 6.

<table>
<caption>Table 6<br>Solution energies where trap sites are pre-existent</caption>
<thead>
<tr>
<th>Site</th>
<th colspan="4">Energies (eV)</th>
</tr>
<tr>
<th></th>
<th>$T=298$ K</th>
<th>1773 K</th>
<th>2273 K</th>
<th>2773 K</th>
</tr>
</thead>
<tbody>
<tr>
<td>Anion vacancy</td>
<td>17.81</td>
<td>14.61</td>
<td>13.44</td>
<td>12.25</td>
</tr>
<tr>
<td>Cation vacancy</td>
<td>7.47</td>
<td>7.14</td>
<td>6.76</td>
<td>6.41</td>
</tr>
<tr>
<td>Divacancy</td>
<td>6.77</td>
<td>5.66</td>
<td>5.27</td>
<td>4.9</td>
</tr>
<tr>
<td>Neutral trivacancy</td>
<td>4.49</td>
<td>4.36</td>
<td>3.92</td>
<td>3.7</td>
</tr>
<tr>
<td>Charged trivacancy</td>
<td>5.42</td>
<td>4.52</td>
<td>4.08</td>
<td>3.87</td>
</tr>
<tr>
<td>Tetravacancy</td>
<td>4.26</td>
<td>3.85</td>
<td>3.50</td>
<td>1.96</td>
</tr>
</tbody>
</table>

### 4.2.2. Case where defect population is in full thermodynamic equilibrium.

In this case the solution energy is defined as in section 4.2.1., except that the trap formation energy (table 5) has to be added. Solution energies are thus dependent on the $\mathrm{UO}_{2}$ stoichiometry.

Solution energies for the case of full thermodynamic equilibrium are given in table 7.

### 4.2.3. Migration mechanisms.

In the previous study [1], a migration mechanism for Xe atoms was proposed which involved a Xe atom adjacent to a neutral trivacancy changing places with a neighbouring lattice cation via interstitial sites. An activation energy of 5.0 eV was calculated for this mechanism, which compared with an experimentally obtained value of 3.9 eV [13]. We have repeated these calculations using our new potentials and obtain a value

<table>
<caption>Table 7<br>Solution energies for full thermodynamic equilibrium</caption>
<thead>
<tr>
<th colspan="5">(a) Anion-deficient $\mathrm{UO}_{2}$</th>
</tr>
<tr>
<th>Site</th>
<th colspan="4">Energies (eV)</th>
</tr>
<tr>
<th></th>
<th>$T=298$ K</th>
<th>1773 K</th>
<th>2273 K</th>
<th>2773 K</th>
</tr>
</thead>
<tbody>
<tr>
<td>Anion vacancy</td>
<td>17.81</td>
<td>14.61</td>
<td>13.44</td>
<td>12.25</td>
</tr>
<tr>
<td>Cation vacancy</td>
<td>18.10</td>
<td>15.47</td>
<td>14.73</td>
<td>14.0</td>
</tr>
<tr>
<td>Neutral trivacancy</td>
<td>11.63</td>
<td>10.15</td>
<td>9.6</td>
<td>9.03</td>
</tr>
<tr>
<td>Charged trivacancy</td>
<td>23.61</td>
<td>20.06</td>
<td>18.86</td>
<td>18.34</td>
</tr>
<tr>
<td>Tetravacancy</td>
<td>18.20</td>
<td>15.89</td>
<td>15.09</td>
<td>13.07</td>
</tr>
</tbody>
<thead>
<tr>
<th colspan="5">(b) Stoichiometric $\mathrm{UO}_{2}$</th>
</tr>
<tr>
<th>Site</th>
<th colspan="4">Energies (eV)</th>
</tr>
<tr>
<th></th>
<th>$T=298$ K</th>
<th>1773 K</th>
<th>2273 K</th>
<th>2773 K</th>
</tr>
</thead>
<tbody>
<tr>
<td>Anion vacancy</td>
<td>20.47</td>
<td>16.95</td>
<td>15.71</td>
<td>14.45</td>
</tr>
<tr>
<td>Cation vacancy</td>
<td>12.78</td>
<td>10.79</td>
<td>10.19</td>
<td>9.60</td>
</tr>
<tr>
<td>Neutral trivacancy</td>
<td>11.63</td>
<td>10.15</td>
<td>9.60</td>
<td>9.03</td>
</tr>
<tr>
<td>Charged trivacancy</td>
<td>15.63</td>
<td>13.04</td>
<td>12.21</td>
<td>11.74</td>
</tr>
<tr>
<td>Tetravacancy</td>
<td>12.88</td>
<td>11.21</td>
<td>10.55</td>
<td>8.67</td>
</tr>
</tbody>
<thead>
<tr>
<th colspan="5">(c) Anion-excess $\mathrm{UO}_{2}$</th>
</tr>
<tr>
<th>Site</th>
<th colspan="4">Energies (eV)</th>
</tr>
<tr>
<th></th>
<th>$T=298$ K</th>
<th>1773 K</th>
<th>2273 K</th>
<th>2773 K</th>
</tr>
</thead>
<tbody>
<tr>
<td>Anion vacancy</td>
<td>23.13</td>
<td>19.29</td>
<td>17.98</td>
<td>16.65</td>
</tr>
<tr>
<td>Cation vacancy</td>
<td>7.46</td>
<td>6.11</td>
<td>5.65</td>
<td>5.20</td>
</tr>
<tr>
<td>Neutral trivacancy</td>
<td>11.63</td>
<td>10.15</td>
<td>9.60</td>
<td>9.03</td>
</tr>
<tr>
<td>Charged trivacancy</td>
<td>7.65</td>
<td>6.02</td>
<td>5.40</td>
<td>5.14</td>
</tr>
<tr>
<td>Tetravacancy</td>
<td>7.56</td>
<td>6.53</td>
<td>6.01</td>
<td>4.27</td>
</tr>
</tbody>
</table>

<table>
 <thead>
  <tr>
   <th>
    Temperature (K)
   </th>
   <th>
    Activation energy (eV)
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
    298
   </td>
   <td>
    2.20
   </td>
  </tr>
  <tr>
   <td>
    1773
   </td>
   <td>
    2.13
   </td>
  </tr>
  <tr>
   <td>
    2273
   </td>
   <td>
    2.08
   </td>
  </tr>
  <tr>
   <td>
    2773
   </td>
   <td>
    2.03
   </td>
  </tr>
 </tbody>
</table>

of 10.5 eV for a lattice parameter appropriate to 2000°C. The difference in these results is due to there having been an unacceptably large Xe polarization energy in the earlier work. This mechanism is therefore rejected because of its poor agreement with experiment.

We propose a new mechanism for this process in which a neutral trivacancy diffuses to a trapped Xe atom, which then hops from one trivacancy to the other. The activation energy is taken as the energy required to form the trivacancy in the site adjacent to the trapped gas atom plus the energy to move the gas atom to the position midway between the cation vacancies. The values are reported in table 8. The low values of ~ 2 eV are largely due to the strong binding energy of the additional trivacancy to the trapped gas atom.

## 5. Discussion

The results in table 7 clearly show that single gas atoms are generally trapped at cation/anion vacancy aggregates, rather than at single vacancy sites. For an ion-deficient and stoichiometric UO₂ the neutral trivacancy is clearly the preferred site. For the anion-excess materials, the calculations suggest several possible trap sites, with the charged trivacancy and the tetra-vacancy as well as the simple cation vacancy being possible on energetic grounds. These qualitative conclusions are similar to those of our previous study [1] and the prediction of neutral trivacancy traps for UO₂ and UO₂₋ₓ accords with experimental information [13].

The calculated solution energies are high (~ 10 eV) for stoichiometric and anion-deficient UO₂, although they drop significantly on passing to anion-excess UO₂. The defect energies reported in table 3 are higher than those calculated in our previous study [1], due to the modifications principally in the gas–lattice potentials. The calculations refer to dissolved gas in the UO₂ lattice in equilibrium with isolated gas atoms in the gas phase. As such they may be taken as yielding energies for gas solution from large underpressurized bubbles into single gas atoms at trap sites in the lattice. The large values we have calculated would preclude significant thermal resolution under these conditions. In part 2 of this study we shall report contrasting results for solution energies from small overpressurized bubbles.

Regarding our study of migration mechanisms, the low values calculated for the activation energies establish the plausibility of the trivacancy mechanism that we have proposed, and we consider that it is unlikely that any non-defect-assisted mechanisms can effect Xe diffusion in UO₂.

As to the agreement of these results with experimental data, the detailed review of Matzke [13] concludes that there is no strong evidence for major differences in the Xe diffusion coefficient in UO₂₋ₓ and UO₂. This is predicted by our results which suggest trapping of Xe at trivacancies in both composition regions, with a trivacancy (and hence stoichiometry-independent) assisted migration mechanism. In UO₂₊ₓ different trap sites are predicted, which would be expected to lead to different Xe migration rates, as is indeed observed experimentally. Our calculated activation energy is rather low when compared with experiment. This may be due to the fact that the Xe diffusion is controlled by the rate of trivacancy migration to the trapped gas atom, rather than the equilibrium concentration of the complex formed by trapping an additional trivacancy by the trapped gas atom.

## 6. Conclusions

The results we have presented confirm the qualitative conclusions following from our previous study [1] as regards gas atom trapping. A new migration mechanism is proposed which appears to give a better general agreement between the prediction of our calculations and experiment. As regards the important question of thermal re-solution, our calculations rule this out for the case of gas in equilibrium with underpressurized bubbles. The following paper will examine the question of the behaviour of overpressurized bubbles.

## Appendix 1. Expressions for trap formation energies

In giving the expressions, the following symbols will be used throughout:
$E_t$ Trap formation energy
$E_s$ Schottky trio formation energy
$E_f$ Frenkel pair formation energy
$B_{dv}$ Binding energy of divacancy
$B_{nt}$ Binding energy of neutral trivacancy

$B_{\text{ct}}$ Binding energy of charged trivacancy
$B_{\text{tv}}$ Binding energy of tetravacancy

(1) Anion vacancy
$\text{UO}_{2-x}\quad E_{\text{t}}=0$
$\text{UO}_{2}:\quad E_{\text{t}}=\frac{1}{2}E_{\text{f}}$
$\text{UO}_{2+x}:\ E_{\text{t}}=E_{\text{f}}$

(2) Cation vacancy
$\text{UO}_{2-x}:\ E_{\text{t}}=E_{\text{s}}$
$\text{UO}_{2}:\quad E_{\text{t}}=E_{\text{s}}-E_{\text{f}}$
$\text{UO}_{2+x}:\ E_{\text{t}}=E_{\text{s}}-2E_{\text{f}}$

(3) Divacancy
$\text{UO}_{2-x}:\ E_{\text{t}}=E_{\text{s}}-B_{\text{dv}}$
$\text{UO}_{2}:\quad E_{\text{t}}=E_{\text{s}}-\frac{1}{2}E_{\text{f}}-B_{\text{dv}}$
$\text{UO}_{2+x}:\ E_{\text{t}}=E_{\text{s}}-E_{\text{f}}+B_{\text{dv}}$

(4) Neutral trivacancy
$$E_{\text{t}}=E_{\text{s}}-B_{\text{nt}}\ (\text{stoichiometry-independent})$$

(5) Charged trivacancy
$\text{UO}_{2-x}:\ E_{\text{t}}=2E_{\text{s}}-B_{\text{ct}}$
$\text{UO}_{2}:\quad E_{\text{t}}=2E_{\text{s}}-\frac{3}{2}E_{\text{f}}-B_{\text{ct}}$
$\text{UO}_{2+x}:\ E_{\text{t}}=2E_{\text{s}}-3E_{\text{f}}-B_{\text{ct}}$

(b) Tetravacancy
$\text{UO}_{2-x}:\ E_{\text{t}}=2E_{\text{s}}-B_{\text{tv}}$
$\text{UO}_{2}:\quad E_{\text{t}}=2E_{\text{s}}-E_{\text{f}}-B_{\text{tv}}$
$\text{UO}_{2+x}:\ E_{\text{t}}=2E_{\text{s}}-2D_{\text{f}}-B_{\text{tv}}$

### Acknowledgements

We acknowledge useful discussions with Dr. I.R. Brearley, Mr. P.T. Elton and Dr. D.A. MacInnes of SRD, Culcheth, and with Dr. J.H. Harding, Dr. A.B. Lidiard, Dr. J.R. Matthews, Dr. A.M. Stoneham and Dr. M.H. Wood of AERE, Harwell, The UKAEA is thanked for financial support.

### References

[1] C.R.A. Catlow, Proc. Soc. A364 (1978) 473.
[2] C.R.A. Catlow, J. de Phys. C6-53 (1980).
[3] C.R.A. Catlow and W.C. Mackrodt, in: Computer Simulation of Solids (Lecture Notes in Physics No. 166) (Springer-Verlag, Berlin, 1982).
[4] C.R.A. Catlow, R. James, W.C. Mackrodt and R.F. Stewart, Phys. Rev. B25 (1982) 1006.
[5] M.J. Norgett, UKAEA Report AERE-R7650.
[6] C.R.A. Catlow, Proc. Soc. A353 (1977) 533.
[7] C.R.A. Catlow and A.B. Lidiard Proc. Symposium on Thermodynamics of Reactor Materials (IAEA, Vienna, 1974) Vol. II, p. 27.
[8] B.G. Dick and A.W. Overhauser, Phys. Rev. 112 (1958) 90.
[9] R.A. Jackson, A.D. Murray, J.H. Harding and C.R.A. Catlow, Phil. Mag., to be published.
[10] J.H. Harding and A.H. Harker, UKAEA Report AERE-R10425.
[11] P.J. Baloock, W.E. Spindler and T.W. Baker, UKAEA Report AERE-R5007.
[12] C.R.A. Catlow, J. Corish and P.W.M. Jacobs, J. Phys. C12 (1979) 3433.
[13] Hj. Matzke, Rad. Effects 53 (1980) 219.