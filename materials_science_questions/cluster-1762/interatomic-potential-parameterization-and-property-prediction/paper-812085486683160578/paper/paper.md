This article was downloaded by: [University of Arizona]
On: 29 July 2013, At: 03:14
Publisher: Taylor & Francis
Informa Ltd Registered in England and Wales Registered Number: 1072954 Registered office:
Mortimer House, 37-41 Mortimer Street, London W1T 3JH, UK

![](./images/812085486683160578_1.jpg)

Molecular Physics: An International Journal
at the Interface Between Chemistry and
Physics

Publication details, including instructions for authors and subscription
information:
http://www.tandfonline.com/loi/tmph20

A Monte Carlo calculation of
thermodynamic properties for the liquid
NaCl+KCl mixture

Bjørn Larsen $^{a}$ , Tormod Førland $^{a}$ & Konrad Singer $^{b}$

$^{a}$ Division of Physical Chemistry, The University of Trondheim, The
Norwegian Institue of Technology, N-7034, Trondheim-NTH, Norway
$^{b}$ Department of Chemistry, Royal Holloway College, Englefield Green,
Surrey, England
Published online: 23 Aug 2006.

To cite this article: Bjrn Larsen, Tormod Frland & Konrad Singer (1973) A Monte Carlo calculation of
thermodynamic properties for the liquid NaCl+KCl mixture, Molecular Physics: An International Journal at
the Interface Between Chemistry and Physics, 26:6, 1521-1532, DOI: 10.1080/00268977300102671

To link to this article: http://dx.doi.org/10.1080/00268977300102671

PLEASE SCROLL DOWN FOR ARTICLE

Taylor & Francis makes every effort to ensure the accuracy of all the information (the
"Content") contained in the publications on our platform. However, Taylor & Francis, our
agents, and our licensors make no representations or warranties whatsoever as to the
accuracy, completeness, or suitability for any purpose of the Content. Any opinions and views
expressed in this publication are the opinions and views of the authors, and are not the views
of or endorsed by Taylor & Francis. The accuracy of the Content should not be relied upon
and should be independently verified with primary sources of information. Taylor and Francis
shall not be liable for any losses, actions, claims, proceedings, demands, costs, expenses,
damages, and other liabilities whatsoever or howsoever caused arising directly or indirectly in
connection with, in relation to or arising out of the use of the Content.

This article may be used for research, teaching, and private study purposes. Any substantial
or systematic reproduction, redistribution, reselling, loan, sub-licensing, systematic supply, or
distribution in any form to anyone is expressly forbidden. Terms & Conditions of access and
use can be found at http://www.tandfonline.com/page/terms-and-conditions

MOLECULAR PHYSICS, 1973, VOL. 26, No. 6, 1521-1532

# A Monte Carlo calculation of thermodynamic properties for the liquid NaCl+KCl mixture

by BJØRN LARSEN* and TORMOD FØRLAND

The University of Trondheim, The Norwegian Institue of Technology,
Division of Physical Chemistry, N-7034 Trondheim-NTH, Norway

and KONRAD SINGER

Department of Chemistry, Royal Holloway College, Englefield Green,
Surrey, England

(Received 15 March 1973)

The mixing process $\mathrm{NaCl}+\mathrm{KCl} \to(\mathrm{Na}, \mathrm{K}) \mathrm{Cl}$ in the liquid state at $T=1083$ K and zero pressure is simulated by means of Monte Carlo calculations. A cubic box with periodic boundary conditions containing 216 ions interacting according to a pair potential of the Huggins-Mayer form served as a model of the system. Thermodynamic properties are calculated for the mixture and the pure salt models and compared with experiments. Radial and angular distribution functions are obtained. A perturbation theory of the heats of mixing of molten salts and the 'random mixture approximation' are commented on in the light of the Monte Carlo results.

## 1. INTRODUCTION

The Monte Carlo (MC) method for calculating ensemble averages of model systems was introduced by Metropolis *et al.* [1] in 1953. The method has been applied extensively to the study of systems of particles interacting through short range forces (hard spheres, 12-6 and exp-6 potentials) [2, 3] and, more recently, also to models of liquid ionic salts. Krogh-Moe *et al.* [4] used a neutral MC cell with 64 ions interacting with a pair potential, $\phi_{ij}$, of the Pauling form [5] :

$$
\phi_{ij}(r)=z_{i} z_{j} e^{2} r^{-1}+c_{ij} r^{-n}, \tag{1}
$$

where $z_{i}$ and $z_{j}$ are the formal charges of the ions $i$ and $j$, $e$ the electron charge, $r$ the distance between the two particles, $c$ a repulsion energy coefficient and $n$ an integer exponent in the range between 5 and 12. They chose the energy parameters to simulate the effective pair potential for $\mathrm{LiCl}$ ; the density and temperature were fixed to fit experimental data for the liquid state. Woodcock and Singer [6] (subsequently referred to as WS) simulated $\mathrm{KCl}$ (liquid and solid) with 108 anions and 108 cations in the MC cell, and with an effective potential of the Huggins-Mayer form [7] :

$$
\phi_{ij}(r)=z_{i} z_{j} e^{2} r^{-1}+b_{ij} \exp (-r / \rho)+c_{ij} r^{-6}+d_{ij} r^{-8}. \tag{2}
$$

* On leave at Laboratoire de Physique Théorique et Hautes Energies (Laboratoire associée au Centre National de la Recherche Scientifique), Université de Paris-Sud, 91405 Orsay (France).

Here $b_{ij}$ and $\rho$ denote repulsion energy parameters and $c_{ij}$ and $d_{ij}$ dispersion energy parameters. Whereas Krogh-Moe *et al.* employed the ' minimum image con- vention ' where the energy summation is performed over all particle pairs, $i,j;\ j=1,2,...,N,j\neq i$ within a neutral cell with particle $i$ in the centre, WS used the Ewald method [8]. The Evjen method [9], which corresponds to the ' minimum image ' method, has been shown to give configurational energies satisfying the Poisson equation only for lattices of high symmetry (see e.g. Dahl [10]). Unless the ensemble averaging eliminates the effect of the departures from high symmetry, this method may therefore introduce significant errors when applied to molten salt systems. In some preliminary calculations, Woodcock [11] found that the use of the Evjen method in the MC process leads to mean energies lying substantially below the lattice energy of the stable crystal. The Ewald method is, on the other hand, applicable to any type of lattice. Objections may be raised against both methods on physical grounds because they imply a periodic structure of the macroscopic system. Using the Ewald method, however, the calculated energies and radial distribution functions agree quite well with the experimental data and it appears that the effect of the periodic structure is not serious if the MC cell is sufficiently large ( $\geqslant 3a$, $a=$ lattice constant) [12].

The aim of the present work was to ascertain whether MC calculations can be used as a tool in the study of molten salt mixtures. Since WS calculations of thermodynamic properties for the KCl model showed good agreement with experimental results, the Huggins-Mayer pair potential and the Ewald method for calculating the Coulomb energy were used. Because the mixture (Na, K)Cl has been thoroughly investigated experimentally, we designed the model system to simulate pure NaCl, pure KCl and the 50-50 per cent mixture (Na, K)Cl in the liquid states and at $T=1083$ K. For each system two molar volumes were fixed so that thermodynamic properties corresponding to zero pressure could be ob- tained by linear interpolation. While the effective energy parameters for the model used (equation (2)) are determined for the pure salts [13, 14], they are not known for the mixture and had therefore to be estimated from the pure salt data. This procedure is described in $\S 2$.

In $\S 3$ is given a description of how the calculations were carried out. Because of limitations in the computer time allocated for this project, we were restricted to do calculations for very few (N, V, T) points and to use the ' effective free volume method ' [15] for the entropy calculations.

The results from the MC calculations are given in $\S 4$. In this section we also give a brief discussion of the validity of the ' random mixture approximation ' [16] and a perturbation theory [17] for molten salt mixtures.

## 2. THE MODEL

The dispersion parameters in (2) are given by Mayer as

$$
c_{ij} \approx \frac{3}{2} \alpha_{i} \alpha_{j} \epsilon_{i} \epsilon_{j} /\left(\epsilon_{i}+\epsilon_{j}\right), \tag{3}
$$

where $\alpha$ is the polarizability of an ion and $\epsilon$ is either ionization energy (for cations) or electron affinity (for anions), and

$$
d_{ij} \approx \frac{3}{2} c_{ij}\left(\pi_{i}+\pi_{j}\right), \tag{4}
$$

where the $\pi$'s are functions of the number of valence electrons.

Monte Carlo calculations

The parameters $c_{\mathrm{Na}^{+} \mathrm{K}^{+}}$and $d_{\mathrm{Na}^{+} \mathrm{K}^{+}}$were obtained from Mayer's single ion data with the use of (3) and (4). The parameters $c_{++}$and $d_{++}$(except those just mentioned) and $c_{+-}$and $d_{+-}$for the mixture were taken as those for the corres- ponding pure salts. For the mixture the single ion data for $\mathrm{Cl}^{-}$were taken as the arithmetic mean of the corresponding pure salt data, i.e.
$$\alpha_{\mathrm{Cl}^{-}}(\operatorname{mix}):=\frac{1}{2}\left[\alpha_{\mathrm{Cl}^{-}}(\mathrm{NaCl})+\alpha_{\mathrm{Cl}^{-}}(\mathrm{KCl})\right], \quad(5)$$
and $c_{--}$and $d_{--}$were calculated by using (3) and (4).

The repulsion parameters are given by Tosi and Fumi [13,14], who fitted the pair potential (2) to experimental compressibility data at $25^{\circ} \mathrm{C}$, assuming $\mathrm{NaCl}$ structure of the crystal lattice. The $b_{i j}$'s are defined as
$$b_{i j}=c_{i j}{ }^{\prime} b \exp \left(\sigma_{i j} / \rho\right), \quad(6)$$
where $b$ is a constant for all alkali halides $(b=0.338 ×10^{-12} \mathrm{erg} \dagger$ in this set of data) and $\sigma_{i j}$ is the sum of the radii of the ions $i$ and $j$. The constants $c_{i j}{ }^{\prime}$ are given by Pauling [18] as $c_{++}{ }^{\prime}=1 \cdot 25, c_{+-}{ }^{\prime}=1 \cdot 00, c_{--}{ }^{\prime}=0 \cdot 75$ for the salts considered in this paper. During a test run on $\mathrm{Cl}(\mathrm{l})$ at $1083 \mathrm{~K}$ it appeared that these values gave at zero pressure an internal energy being only $0 \cdot 2$ per cent lower, but a volume 10 per cent larger than the experimental values. At the expense of the agreement between experimental and MC internal energy, the constants $c_{i j}{ }^{\prime}$ were therefore adjusted so that a MC calculated volume $4 \cdot 4$ per cent larger than the experimental was obtained. The corresponding values of the $c_{i j}{ }^{\prime \prime}$'s were $c_{++}{ }^{\prime}=1 \cdot 11, c_{+-}{ }^{\prime}=0.96$ and $c_{--}{ }^{\prime}=0.75$; this was considered as an approximately optimal set under the conditions described above. Because of lack of computer time this procedure was not repeated for the $\mathrm{NaCl}$ and $(\mathrm{Na}, \mathrm{K}) \mathrm{Cl}$ systems, and

| System       | $1 / \rho\left[\AA^{-1}\right] \ddagger$ |
|--------------|-----------------------------------------|
| $\mathrm{NaCl}$ | $3 \cdot 15$                             |
| $\mathrm{KCl}$  | $2 \cdot 97$                             |
| $(\mathrm{Na}, \mathrm{K}) \mathrm{Cl}$ | $3 \cdot 06$                             |

<table>
  <thead>
    <tr>
      <th>System</th>
      <th>$i$</th>
      <th>$j$</th>
      <th>$b_{ij}[10^{-9}\ \text{erg}]$</th>
      <th>$c_{ij}[10^{-12}\ \text{erg}\cdot\mathring{\text{A}}^6]$</th>
      <th>$d_{ij}[10^{-12}\ \text{erg}\cdot\mathring{\text{A}}^8]$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>NaCl</td>
      <td>Na⁺</td>
      <td>Na⁺</td>
      <td>0·596</td>
      <td>1·68</td>
      <td>0·8</td>
    </tr>
    <tr>
      <td>NaCl</td>
      <td>Na⁺</td>
      <td>Cl⁻</td>
      <td>1·906</td>
      <td>11·2</td>
      <td>13·9</td>
    </tr>
    <tr>
      <td>NaCl</td>
      <td>Cl⁻</td>
      <td>Cl⁻</td>
      <td>5·504</td>
      <td>116·0</td>
      <td>233·0</td>
    </tr>
    <tr>
      <td>KCl</td>
      <td>K⁺</td>
      <td>K⁺</td>
      <td>2·230</td>
      <td>24·3</td>
      <td>24·0</td>
    </tr>
    <tr>
      <td>KCl</td>
      <td>K⁺</td>
      <td>Cl⁻</td>
      <td>2·772</td>
      <td>48·0</td>
      <td>73·0</td>
    </tr>
    <tr>
      <td>KCl</td>
      <td>Cl⁻</td>
      <td>Cl⁻</td>
      <td>3·110</td>
      <td>125·0</td>
      <td>250·0</td>
    </tr>
    <tr>
      <td>(Na, K)Cl</td>
      <td>Na⁺</td>
      <td>Na⁺</td>
      <td>0·483</td>
      <td>1·68</td>
      <td>0·8</td>
    </tr>
    <tr>
      <td>(Na, K)Cl</td>
      <td>Na⁺</td>
      <td>K⁺</td>
      <td>1·184</td>
      <td>6·27</td>
      <td>4·6</td>
    </tr>
    <tr>
      <td>(Na, K)Cl</td>
      <td>Na⁺</td>
      <td>Cl⁻</td>
      <td>1·581</td>
      <td>11·2</td>
      <td>13·9</td>
    </tr>
    <tr>
      <td>(Na, K)Cl</td>
      <td>K⁺</td>
      <td>K⁺</td>
      <td>2·903</td>
      <td>24·3</td>
      <td>24·0</td>
    </tr>
    <tr>
      <td>(Na, K)Cl</td>
      <td>K⁺</td>
      <td>Cl⁻</td>
      <td>3·646</td>
      <td>48·0</td>
      <td>73·0</td>
    </tr>
    <tr>
      <td>(Na, K)Cl</td>
      <td>Cl⁻</td>
      <td>Cl⁻</td>
      <td>4·137</td>
      <td>123·0</td>
      <td>246·0</td>
    </tr>
  </tbody>
</table>

$\ddagger \mathring{\text{A}}=10^{-10}\ \text{m}.$

Table 1. Repulsion and dispersion parameters.

$\dagger \text{erg}=10^{-7}\ \text{J}.$

the adjusted $c_{ij}$'s from KCl were used for all systems. The parameter $\rho$, which is a constant for a given salt, was for the mixture taken as

$$
\rho(\mathrm{mix})=\frac{1}{2}[\rho(\mathrm{NaCl})+\rho(\mathrm{KCl})]. \tag{7}
$$

The $\sigma_{\mathrm{Na}^{+} \mathrm{K}^{+}}$for the mixture was obtained as the sum of the ionic radii $r_{\mathrm{Na}^{+}}$and $r_{\mathrm{K}^{+}}$.

The repulsion and dispersion parameters used are given in table 1.

### 3. THE CALCULATIONS

A FORTRAN V computer programme was used, and the calculations were started from an ideal NaCl structure. 100 000 configurations were used for melting the crystal, then six V, T points were calculated consecutively. For each V, T point 225 000 configurations were generated. The last 200 000 of these were used for obtaining averages. For the mixture the calculations were started after $1.2 \times 10^{6}$ configurations from the ideal lattice, and 75000 configurations were allowed for equilibration. The neutral MC cell contained 216 ions.

For a more detailed description of the model system, see refs. [11] and [6].

### 4. RESULTS AND DISCUSSION

Thermodynamic properties were calculated from the appropriate ensemble averages. The molar volume $V$, internal energy $E$, entropy $S$ and the Gibbs free energy $G$ at zero pressure are given in table 2. The standard deviations in the MC data are calculated from the scatter of the sub-averages for 5000 MC configurations. The internal energies agree reasonably well with experimental values calculated from cohesive energies at $25^{\circ} \mathrm{C}$ [14], heat capacity data [19], and changes in enthalpy on melting [20] and on mixing [21]. The molar volumes, however, are well outside the margins of error from the experimental values [20, 22]. The volume for KCl is 2 per cent less than that of WS, the difference may be due to the adjustment of the Pauling constants $c_{ij}{ }^{\prime}$. The calculated entropies agree for all systems within 2 per cent with the experimental values obtained from entropy data at $25^{\circ} \mathrm{C}$ [19], the heat capacity data [19] and changes in entropy on mixing [23].

<table>
  <thead>
    <tr>
      <th>System</th>
      <th>$V[\mathrm{cm}^{3}\mathrm{mol}^{-1}]$</th>
      <th>$E[\mathrm{kcal}\mathrm{mol}^{-1}]$</th>
      <th>$S$<br>$[\mathrm{cal}\mathrm{mol}^{-1}\mathrm{K}^{-1}]$</th>
      <th>$G[\mathrm{kcal}\mathrm{mol}^{-1}]$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">NaCl (l)</td>
      <td>MC $38\cdot 2\ \pm 0\cdot 2$</td>
      <td>$-166\cdot 3\pm 0\cdot 1$</td>
      <td>$40\cdot 1$</td>
      <td>$-209\cdot 7$</td>
    </tr>
    <tr>
      <td>Exp $37\cdot 67\pm 0\cdot 05$</td>
      <td>$-165\cdot 2\pm 1\cdot 0$</td>
      <td>$40\cdot 9$</td>
      <td>$-209\cdot 5$</td>
    </tr>
    <tr>
      <td rowspan="2">KCl (l)</td>
      <td>MC $51\cdot 8\ \pm 0\cdot 2$</td>
      <td>$-149\cdot 9\pm 0\cdot 1$</td>
      <td>$43\cdot 2$</td>
      <td>$-196\cdot 7$</td>
    </tr>
    <tr>
      <td>Exp $49\cdot 56\pm 0\cdot 05$</td>
      <td>$-148\cdot 7\pm 1\cdot 0$</td>
      <td>$43\cdot 1$</td>
      <td>$-195\cdot 4$</td>
    </tr>
    <tr>
      <td rowspan="2">($\mathrm{Na},\mathrm{K}$)Cl (l)</td>
      <td>MC $46\cdot 2\ \pm 0\cdot 4$</td>
      <td>$-157\cdot 3\pm 0\cdot 1$</td>
      <td>$43\cdot 1$</td>
      <td>$-204\cdot 0$</td>
    </tr>
    <tr>
      <td>Exp $43\cdot 86\pm 0\cdot 05$</td>
      <td>$-157\cdot 1\pm 1\cdot 0$</td>
      <td>$43\cdot 3$</td>
      <td>$-204\cdot 0$</td>
    </tr>
  </tbody>
</table>

Table 2. Thermodynamic properties at zero pressure. Comparison with experimental data. Composition of the system $(\mathrm{Na},\mathrm{K})\mathrm{Cl}$: $x_{\mathrm{NaCl}}=x_{\mathrm{KCl}}=0\cdot 5$. $T=1083\ \mathrm{K}$.

<table>
<thead>
<tr>
<th>$\Delta V [\text{cm}^3 \text{mol}^{-1}]$</th>
<th>$\Delta E [\text{kcal mol}^{-1}]$</th>
<th>$\Delta S$<br>$[\text{cal mol}^{-1} \text{K}^{-1}]$</th>
<th>$\Delta G [\text{kcal mol}^{-1}]$</th>
</tr>
</thead>
<tbody>
<tr>
<td>MC $1.2 \pm 0.4$</td>
<td>$0.8 \pm 0.1$</td>
<td>$1.4$</td>
<td>$-0.8$</td>
</tr>
<tr>
<td>Exp $0.24 \pm 0.08$</td>
<td>$-0.13 \pm 0.01$</td>
<td>$1.32$</td>
<td>$-1.56$</td>
</tr>
</tbody>
</table>

Table 3. Thermodynamic properties on mixing of NaCl (l) and KCl (l) at zero pressure and $T=1083$ K. Comparison with experimental data. Composition of the system (Na, K)Cl : $x_{\text{NaCl}}=x_{\text{Cl}}=0.5$.

Changes in thermodynamic properties on mixing are calculated from the data given in table 2 and compared with experimental data in table 3. Generally speaking, the MC data for the mixing process calculated this way are obtained as small differences between large quantities, and are accordingly subject to large relative errors. In addition, the parameters of the repulsion potential are probably not the best ones for all three systems and this may explain the rather large difference between the MC and experimental $\Delta V$. A smaller value of $\Delta V$ would certainly also give a smaller $\Delta E$, but unfortunately the available MC data are insufficient to estimate the value of $\Delta E$ which would correspond to the experimental $\Delta V$. As the main contribution to the entropy change is the Temkin ideal entropy [24], which is independent of the MC calculations, the good agreement between MC and experimental $\Delta S$ was not unexpected. It gives some support, however, to the ' effective free volume ' method for the calculation of entropies [25].

For comparison the change in Gibbs' free energy on mixing, $\Delta G$, was obtained at zero pressure by integrating $(\partial F / \partial \lambda_{j})$, the derivatives of Helmholtz's free energy with respect to potential energy parameters [26]. Because data for only the initial and final states of the mixing process had been calculated, a linear variation of the integrands $\partial F / \partial \lambda_{j}$ along the integration path was assumed

$$
\Delta F^{\mathrm{E}}=\frac{1}{2} \sum_{j}\left[\left(\frac{\partial F}{\partial \lambda_{j}}\right)_{\mathrm{f}}+\left(\frac{\partial F}{\partial \lambda_{j}}\right)_{\mathrm{i}}\right]\left[\left(\lambda_{j}\right)_{\mathrm{f}}-\left(\lambda_{j}\right)_{\mathrm{i}}\right] \tag{8}
$$

where $\lambda_{j}$ is an energy parameter for the system, f and i denote the final and the initial state, respectively, and the sum goes over the entire set of energy parameters. The resulting value of $\Delta G$ is $-1.3$ kcal/mole$\dagger$, and even if this is not as accurate as it could be (if intermediate parameter points were included along the integration path), it is close to the experimental value $-1.56$ kcal/mol.

It is also of interest to note that even for a melt just above the melting point the Temkin ideal entropy of mixing contributes to the full extent, i.e. the $\text{Na}^{+}$and $\text{K}^{+}$ions share their combined free volumes.

Entropy contributions from the ionic species are given in table 4. Comparing the mixture and the pure salts one finds that the single contributions from each species are about the same. An exception is the anion contribution where properties for the mixture are approximately the arithmetic mean of the corresponding pure salt properties.

$\dagger$ kcal $=4.184$ kJ.

<table>
  <thead>
    <tr>
      <th>System</th>
      <th>p[atm]†</th>
      <th>Species</th>
      <th>S
        <br>
        [cal mol⁻¹ K⁻¹]
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>NaCl (l)</td>
      <td>--270</td>
      <td>Na⁺</td>
      <td>19·54</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cl⁻</td>
      <td>20·55</td>
    </tr>
    <tr>
      <td></td>
      <td>940</td>
      <td>Na⁺</td>
      <td>19·45</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cl⁻</td>
      <td>20·55</td>
    </tr>
    <tr>
      <td>KCl (l)</td>
      <td>--370</td>
      <td>K⁺</td>
      <td>22·03</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cl⁻</td>
      <td>21·43</td>
    </tr>
    <tr>
      <td></td>
      <td>810</td>
      <td>K⁺</td>
      <td>21·38</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cl⁻</td>
      <td>21·24</td>
    </tr>
    <tr>
      <td>(Na, K)Cl (l)</td>
      <td>--150</td>
      <td>Na⁺</td>
      <td>10·47</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>K⁺</td>
      <td>11·56</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cl⁻</td>
      <td>21·07</td>
    </tr>
    <tr>
      <td></td>
      <td>730</td>
      <td>Na⁺</td>
      <td>10·38</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>K⁺</td>
      <td>11·44</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cl⁻</td>
      <td>20·98</td>
    </tr>
  </tbody>
</table>

† atm=101 325 Pa.

Table 4. Entropy contributions from the ionic species at $T$=1083 K. Composition of the system (Na, K)Cl : $x_{\text{NaCl}}=x_{\text{KCl}}$=0·5.

<table>
  <thead>
    <tr>
      <th>System</th>
      <th>p[atm]</th>
      <th>$V$[cm³
        <br>
        mol⁻¹]
      </th>
      <th>$\langle \Phi \rangle$</th>
      <th>$\langle \Phi_{\text{c}} \rangle$</th>
      <th>$\langle \Phi_{\text{r}} \rangle$</th>
      <th>$\langle \Phi_{\text{dd}} \rangle$</th>
      <th>$\langle \Phi_{\text{dq}} \rangle$</th>
      <th>$W$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>NaCl (l)</td>
      <td>--270</td>
      <td>38·55</td>
      <td>--172·65</td>
      <td>--192·87</td>
      <td>24·61</td>
      <td>--3·71</td>
      <td>--0·52</td>
      <td>--0·16</td>
    </tr>
    <tr>
      <td></td>
      <td>940</td>
      <td>37·11</td>
      <td>--173·20</td>
      <td>--193·81</td>
      <td>25·19</td>
      <td>--3·86</td>
      <td>--0·56</td>
      <td>--0·16</td>
    </tr>
    <tr>
      <td>KCl (l)</td>
      <td>--370</td>
      <td>52·65</td>
      <td>--156·11</td>
      <td>--172·41</td>
      <td>22·54</td>
      <td>--5·32</td>
      <td>--0·78</td>
      <td>--0·14</td>
    </tr>
    <tr>
      <td></td>
      <td>810</td>
      <td>50·00</td>
      <td>--156·71</td>
      <td>--173·49</td>
      <td>23·33</td>
      <td>--5·58</td>
      <td>--0·81</td>
      <td>--0·16</td>
    </tr>
    <tr>
      <td>(Na, K)Cl (l)</td>
      <td>--150</td>
      <td>46·51</td>
      <td>--163·63</td>
      <td>--181·92</td>
      <td>23·49</td>
      <td>--4·42</td>
      <td>--0·64</td>
      <td>--0·14</td>
    </tr>
    <tr>
      <td></td>
      <td>730</td>
      <td>44·48</td>
      <td>--164·28</td>
      <td>--182·87</td>
      <td>24·01</td>
      <td>--4·60</td>
      <td>--0·66</td>
      <td>--0·16</td>
    </tr>
  </tbody>
</table>

Table 5. Contributions to the internal potential energy $\Phi$ from Coulomb energy $\Phi_{\text{c}}$, repulsion energy $\Phi_{\text{r}}$, dipole-dipole dispersion energy $\Phi_{\text{dd}}$, dipole-quadrupole energy $\Phi_{\text{dq}}$ and long-range correction to dispersion energies $W$. $T$=1083 K. Composition of the mixture : $x_{\text{NaCl}}=x_{\text{KCl}}$=0·5. All energies are given in kcal/mol.

In table 5 the Coulomb, repulsion, dipole-dipole and dipole-quadrupole contributions to the internal energies are given. Contributing less than 5 per cent for all systems, the dispersion forces are of little importance as far as the internal energy is concerned. The sum of ++ and -- pair interactions account for about 50, 25 and 35 per cent of the dispersion energy in NaCl, KCl and (Na, K)Cl, respectively, at the given conditions (table 6).

In some calculations of mixing energies of molten salts, Blander [27] made the assumption that cation-anion dispersion interactions do not contribute to the energy of mixing. In a perturbation theory of the heats of mixing of fused salts, David and Rice [17, 28] conclude that both nearest (+ -- pairs) and next-nearest neighbour ( ++ and -- pairs) interactions are likely to be of importance,

<table>
<thead>
<tr>
<th></th>
<th colspan="3">$\langle\Phi_{\mathrm{r}}\rangle$</th>
<th colspan="3">$\langle\Phi_{\mathrm{d}}\rangle$</th>
<th>$\langle\Phi_{\mathrm{c}}\rangle$</th>
</tr>
<tr>
<th></th>
<td>$++$</td>
<td>$+-$</td>
<td>$--$</td>
<td>$++$</td>
<td>$+-$</td>
<td>$--$</td>
<td></td>
</tr>
</thead>
<tbody>
<tr>
<td>NaCl (l)</td>
<td>0·17</td>
<td>23·20</td>
<td>1·36</td>
<td>$-0.03$</td>
<td>$-2\cdot11$</td>
<td>$-2\cdot12$</td>
<td>$-193.08$</td>
</tr>
<tr>
<td>KCl (l)</td>
<td>0·39</td>
<td>21·85</td>
<td>0·55</td>
<td>$-0.24$</td>
<td>$-4\cdot70$</td>
<td>$-1\cdot26$</td>
<td>$-172.75$</td>
</tr>
<tr>
<td>(Na, K)Cl (l)</td>
<td>0·25</td>
<td>22·44</td>
<td>0·89</td>
<td>$-0.11$</td>
<td>$-3\cdot33$</td>
<td>$-1\cdot65$</td>
<td>$-182.08$</td>
</tr>
<tr>
<td>$\Delta\langle\Phi\rangle_{\text{mix}}$</td>
<td>$-0.03$</td>
<td>$-0.09$</td>
<td>$-0.07$</td>
<td>0·03</td>
<td>0·08</td>
<td>0·04</td>
<td>0·84</td>
</tr>
</tbody>
</table>

Table 6. Energy contributions from the ionic species at zero pressure and $T=1083$ K.
Composition of the mixture : $x_{\mathrm{NaCl}}=x_{\mathrm{KCl}}=0.5$. All energies are given in kcal/mol.

and that anion-cation pairs give the major contribution to the energy of mixing. The MC data indicate that the dispersion energy is of importance, and that nearest and next-nearest neighbour interactions contribute about equally to the energy of mixing in the system studied in this work (table 6). It also seems that the total energy of mixing depends on the balance between the Coulomb contribution, which in general is believed to be negative [29] and very sensitive to the volume of mixing, and the short-range contribution, which for the (Na, K)Cl system is relatively small.

The radial distribution function is defined in the usual way :

$$
g(r)=\frac{1}{n_{0}} \cdot \frac{d n(r)}{4 \pi r^{2} d r}, \tag{9}
$$

where $n_{0}$ is the overall particle density of the system, $d n(r) / 4 \pi r^{2} d r$ is the particle density in a spherical shell with radius $r$ and of thickness $d r$ around a fixed point. The rdf's obtained from averaging histograms from every 5000th configuration are shown in figures 1-3. For a more detailed description of the short-range structure, an angular distribution function was defined as

$$
a(r, \theta)=\frac{1}{n_{0}} \cdot \frac{d n(r, \theta)}{2 \pi r^{2} \sin \theta d r d \theta}. \tag{10}
$$

Thus $a(r, \theta) \cdot 2 \pi r^{2} \sin \theta d r d \theta$ is the probability of finding a third ion $j^{\prime}$ in the volume element $2 \pi r^{2} \sin \theta d r d \theta$ around the pair $i j$, and $\theta$ denotes the angle $j i j^{\prime}$ and $r$ the distance $i j^{\prime}$. Similar to the rdf's, the adf's can be separated into contributions from the different combinations of ionic species. Some examples are shown in figures 4-6. In these examples three to five typical liquid state configurations from the MC runs were investigated for each system. Two ions, the central ion $i$ of species $k$, and a second ion $j$ of species $l$ being a distance in the interval $(r_{k l}, r_{k l}+\Delta r_{k l})$ from $i$, formed a pair. The number of third ions $j^{\prime}$ of species $l^{\prime}$ in a radial interval $(r_{k l^{\prime}}, r_{k l^{\prime}}+\Delta r_{k l^{\prime}})$ from $i$ and in an angular interval $(\theta, \theta+\Delta \theta)$ around the axis $i j$ was recorded so that the total $\theta$ range was covered. The radial intervals to be examined were taken from the rdf's ; $r_{k l}(r_{k l^{\prime}})$ was taken as the distance of closest approach and $r_{k l}+\Delta r_{k l}(r_{k l^{\prime}}+\Delta r_{k l^{\prime}})$ the distance of the first minimum in the $k l(k l^{\prime})$ type rdf. Only triplets of nearest and next nearest neighbours were examined. The angular interval $\theta$ was chosen as $5^{\circ}$.

The curves show an effect of ordering of the cation-cation distributions in the mixture, which may explain the experimental negative excess entropy of

![](./images/812085486683160578_2.jpg)

Figure 1. Radial distribution functions for NaCl (l) at $T$=1083 K and zero pressure.

![](./images/812085486683160578_3.jpg)

Figure 2. Radial distribution functions for KCl (l) at $T$=1083 K and zero pressure.

![](./images/812085486683160578_4.jpg)

Figure 3. Radial distribution functions for (Na, K)Cl (l) at $T=1083$ K and zero pressure. Composition of the mixture : $x_{\mathrm{NaCl}}=x_{\mathrm{KCl}}=0 \cdot 5$.

mixing [23]. The rdf's for the mixture are nearly identical to those for the corresponding pure salts.

In the 'random mixture approximation' [16] the true pair potential $\phi(r_{ij})$ between two molecules situated at $\boldsymbol{r}_{i}$ and $\boldsymbol{r}_{j}$ is replaced by the
$$\left[\phi\left(r_{i j}\right)\right]=\sum_{k} \sum_{l} x_{k} x_{l} \phi_{k l}\left(r_{i j}\right),\qquad(11)$$
i.e. by the average potential which results if the probability of occupation of the positions $\boldsymbol{r}_{i}$ and $\boldsymbol{r}_{j}$ by particles of species $k$ and $l$ is proportional to mole fractions of $k$ and $l$. For ionic systems the randomization has to be restricted to particles of like charge. In the present case,
$$\left.\begin{array}{l}
{\left[\phi_{++}(r)\right]=x_{\mathrm{Na}^{+}} x_{\mathrm{Na}^{+}} \phi_{\mathrm{Na}^{+} \mathrm{Na}^{+}}(r)+2 x_{\mathrm{Na}^{+}} x_{\mathrm{K}^{+}} \phi_{\mathrm{Na}^{+} \mathrm{K}^{+}}(r)+x_{\mathrm{K}^{+}} x_{\mathrm{K}^{+}} \phi_{\mathrm{K}^{+} \mathrm{K}^{+}}(r),} \\
{\left[\phi_{+-}(r)\right]=x_{\mathrm{Na}^{+}} \phi_{\mathrm{Na}^{+} \mathrm{Cl}}(r)+x_{\mathrm{K}^{+}} \phi_{\mathrm{K}^{+} \mathrm{Cl}^{-}}(r),} \\
{\left[\phi_{--}(r)\right]=\phi_{--}(r)} \\
\left(x_{\mathrm{Na}^{+}}=N_{\mathrm{Na}^{+}} / N, \quad x_{\mathrm{K}^{+}}=N_{\mathrm{K}^{+}} / N, \quad N=N_{\mathrm{Na}^{+}}+N_{\mathrm{K}^{+}}\right).
\end{array}\right\}(12)$$

The true total potential energy accordingly is replaced by
$$\left.\begin{array}{l}
{\left[\Phi_{\alpha \beta}\right]=\frac{1}{2} \sum_{i} \sum_{j \neq i}\left[\phi_{\alpha \beta}(r)\right],} \\
(\alpha, \beta=+ \text { or }-).
\end{array}\right\}\qquad(13)$$

The pair correlation functions are defined by
$$g_{\alpha \beta}(\boldsymbol{r})=V^{2} Q_{\mathrm{N}}{ }^{-1} \int \ldots \int \exp \left(-\left[\Phi_{\alpha \beta}\right] / k T\right) d \boldsymbol{r}_{3} \ldots d \boldsymbol{r}_{\mathrm{N}},\qquad(14)$$

![](./images/812085486683160578_5.jpg)

Figure 4. Angular distribution functions for NaCl (l) at $T=1083$ K and zero pressure.
1 : $Na^+ Cl^- Cl^-$ distribution, $Cl^-$ as central ion. 2 : $Na^+ Na^+ Cl^-$ distribution, $Na^+$ as central ion. 3 : $Cl^- Cl^- Cl^-$ distribution. 4 : $Na^+ Na^+ Na^+$ distribution. 5 : $Cl^- Na^+ Cl^-$ distribution, $Na^+$ as central ion. 6 : $Na^+ Cl^- Na^+$ distribution, $Cl^-$ as central ion.

![](./images/812085486683160578_6.jpg)

Figure 5. Selected angular distribution functions for KCl (l) and (Na, K)Cl (l) at $T=1083$ K and zero pressure. Composition of the mixture : $x_{NaCl}=x_{KCl}=0.5$.
1 : $K^+ K^+ K^+$ distribution in KCl. 2 : $Cl^- Cl^- Cl^-$ distribution in KCl. 3 : $Na^+ Na^+ Na^+$ distribution in (Na, K)Cl. 4 : $K^+ K^+ K^+$ distribution in (Na, K)Cl.

![](./images/812085486683160578_7.jpg)

Figure 6. Selected angular distribution functions for (Na, K)Cl (l) at $T=1083$ K and zero pressure. Composition of the mixture : $x_{\mathrm{NaCl}}=x_{\mathrm{KCl}}=0 \cdot 5$. 1 : $\mathrm{Na}^{+} \mathrm{K}^{+} \mathrm{Na}^{+}$ distribution, $\mathrm{K}^{+}$as central ion. 2 : $\mathrm{K}^{+} \mathrm{Na}^{+} \mathrm{K}^{+}$distribution, $\mathrm{Na}^{+}$as central ion.

where
$$
Q_{N}=\int \ldots \int \exp \left(-\sum_{\alpha} \sum_{\beta}\left[\Phi_{\alpha \beta}\right] / k T\right) d \boldsymbol{r}_{1}, \ldots d \boldsymbol{r}_{N}, \tag{15}
$$
i.e.
$$g_{\mathrm{Na}^{+} \mathrm{Na}^{+}}=g_{\mathrm{Na}^{+} \mathrm{K}^{+}}=g_{\mathrm{K}^{+} \mathrm{K}^{+}} \quad \text { and } \quad g_{\mathrm{Na}^{+} \mathrm{Cl}^{-}}=g_{\mathrm{K}^{+} \mathrm{Cl}^{-}}.$$

Figure 3 shows clearly that the three cation-cation and the two cation-anion rdf's have peaks at different distances. One may therefore conclude that the random mixing approximation is not a realistic model even when the difference between the relevant ionic radii $(\mathrm{Na}^{+}$and $\mathrm{K}^{+})$is comparatively small.

There are essentially three different adf's, types III, IIu, and Iul, where l means ' like ' and u ' unlike ' ions. In a NaCl-type lattice one will expect maxima in the adf's for nearest and next-nearest neighbours at $\theta=60,90,120$ and $180^{\circ}$ for the III types, at $\theta=45,90$ and $135^{\circ}$ for the IIu types and at $\theta=90$ and $180^{\circ}$ for the Iul types. For pure NaCl (l) the first maximum in $a(r, \theta)$ is found at a lower $\theta$ value than the corresponding maximum for the lattice (at $\theta=47^{\circ}$ for the III types, $\theta=38^{\circ}$ for the IIu types and $\theta=82^{\circ}$ for the Iul types). (See also figure 4.) The other peaks are rather diffuse, probably because of the packing disorder. A similar trend is found by Scott and Mader [30] in the packing of balls.

By comparing the pure salts and the mixture (figures 4 and 5), one finds that the III types adf's do not change on mixing (the size effects are accounted for by the choice of radial intervals). This is also the case for the other types of adf's. The effect of the substitution of $\mathrm{Na}^{+}$for $\mathrm{K}^{+}$ions in the mixture is illustrated in figure 6, which shows a clear difference between the adf's of type $++'$ and $+'++'$. This finding is interesting because the difference in size between the $\mathrm{Na}^{+}$and $\mathrm{K}^{+}$ions is small and one should expect the $++'$ and $+'++'$ adf's to be identical. Since they are not, this raises again a qualitative argument against the ' random mixture approximation ' as a theory for molten salt mixtures.

In conclusion, let us emphasize that the present work should be regarded as an exploration of the power of MC calculations in the study of molten salt mixtures rather than a full investigation of the $\mathrm{NaCl}+\mathrm{KCl} \rightarrow(\mathrm{Na}, \mathrm{K}) \mathrm{Cl}$ mixing process.

1532
B. Larsen et al.

If one wants to compare calculations with experiments, there is first of all the difficult problem of the determination of the energy parameters, in particular the parameters for the mixture. Secondly, the thermodynamic changes on mixing obtained as described above, are small differences between large quantities and they are therefore subject to large relative errors. It would certainly be better but also more time-consuming to determine the excess free energy by the para- meter integration method. The present calculations seem to indicate, however, that the detailed information about the mixing process that can be obtained from MC calculations will be useful in a further discussion of theories of mixing of molten salts.

REFERENCES

[1] Metropolis, N., Rosenbluth, A. W., Rosenbluth, M. N., Teller, A. H., and Teller, E., 1953, $\mathcal{F}$. chem. Phys., 21, 1087.

[2] Wood, W. W., 1968, *Physics of Simple Liquids*, edited by H. N. V. Temperley, J. S. Rowlinson, and G. S. Rushbrooke (North-Holland Publ. Co.).

[3] McDonald, I. R., and Singer, K., 1970, *Q. Rev. chem. Soc.*, 24, 238.

[4] Krogh-Moe, J., Østvold, T., and Førland, T., 1969, *Acta chem. Scand.*, 23, 2421.

[5] Pauling, L., 1960, *The Nature of the Chemical Bond* (Cornell University Press).

[6] Woodcock, L. V., and Singer, K., 1971, *Trans. Faraday Soc.*, 67, 12.

[7] Huggins, M. L., and Mayer, J. E., 1933, $\mathcal{F}$. chem. Phys., 1, 643.

[8] Ewald, P. P., 1921, *Annln. Phys.*, 64, 253.

[9] Evjen, H. M., 1932, *Phys. Rev.*, 39, 675.

[10] Dahl, J. P., 1965, $\mathcal{F}$. Phys. Chem. Solids, 26, 33.

[11] Woodcock, L. V., 1970, Thesis, University of London.

[12] The application of this method involves errors resulting from the truncation of two infinite series and a compromise must be made between accuracy and expenditure of computing time. The procedure adopted here (following WS) leads to an error which gives Coulomb energies being systematically 0.5 per cent too low (Dixon, M., and Sangster, M. J. L. (unpublished data), Singer, K. (unpublished data)). The error is not included in the estimated uncertainties given in table 2.

[13] Mayer, J. E., 1933, $\mathcal{F}$. chem. Phys., 1, 270.

[14] Fumi, F. G., and Tosi, M. P., 1964, $\mathcal{F}$. Phys. Chem. Solids, 25, 31. Tosi, M. P., and Fumi, F. G., 1964, $\mathcal{F}$. Phys. Chem. Solids, 25, 45.

[15] Gosling, E. M., and Singer, K., 1970, *Pure appl. Chem.*, 22, 303.

[16] Brown, W. B., 1957, *Phil. Trans. A*, 250, 175.

[17] Davis, H. T., and Rice, S. A., 1964, $\mathcal{F}$. chem. Phys., 41, 14.

[18] Pauling, L., 1928, *Zeitschrift für Kristallografie*, 67, 377.

[19] Metallurgical Thermochemistry, 1967, edited by G. V. Raynor, 4th edition (Pergamon Press).

[20] Janz, G. J., 1967, *Molten Salts Handbook* (Academic Press).

[21] Hersh, L. S., and Kleppa, O. J., 1965, $\mathcal{F}$. chem. Phys., 42, 1309.

[22] Van Artsdalen, E. R., and Yaffe, I. S., 1955, $\mathcal{F}$. Phys. Chem., 59, 218.

[23] Thulin, L. U., 1970, Thesis, The University of Trondheim, NTH.

[24] Temkin, M., 1945, *Acta Physicochim. URSS*, 20, 411.

[25] This method has been severely criticized by Valleau J. P., and Whittington, S. G. ($\mathcal{F}$.C.S. Faraday II, 69 (1973) 1004). While agreeing with the criticism of the theoretical arguments originally advanced for this method [15], we believe that the method has been shown to give reliable estimates of the entropy in dense liquids (Gosling, E. M., and Singer, K., 1973, $\mathcal{F}$.C.S. Faraday II, 69, 1009).

[26] Singer, J. V. L., and Singer, K., 1970, *Molec. Phys.*, 19, 279.

[27] Blander, M., 1962, $\mathcal{F}$. chem. Phys., 36, 1092.

[28] Davis, H. T., and Rice, S. A., 1965, $\mathcal{F}$. chem. Phys., 42, 810.

[29] Førland, T., 1957, *Norges. Tek. Vitenskapsaka. Skr. II, 4*.

[30] Scott, G. D., and Mader, D. L., 1964, *Nature, Lond.*, 201, 382.