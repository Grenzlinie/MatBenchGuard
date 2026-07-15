# Computer modeling of $Ba_2RE^{3+}NbO_6$ ($RE^{3+}$ = rare-earth and Y) compounds

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2009 J. Phys.: Condens. Matter 21 075901

(http://iopscience.iop.org/0953-8984/21/7/075901)

View [the table of contents for this issue](), or go to the [journal homepage]() for more

Download details:

IP Address: 130.132.123.28
This content was downloaded on 04/02/2015 at 20:07

Please note that [terms and conditions apply].

# Computer modeling of $Ba_2RE^{3+}NbO_6$ ($RE^{3+}=$ rare-earth and Y) compounds

C W A Paschoal¹ and E M Diniz²

¹ Departamento de Física, CCET, Universidade Federal do Maranhão, 65085-580, São Luís, MA, Brazil
² Departamento de Física, ICEx, Universidade Federal de Minas Gerais, PO Box 702, 30161-970, Belo Horizonte, MG, Brazil

E-mail: paschoal@ufma.br

Received 29 September 2008, in final form 10 December 2008
Published 19 January 2009
Online at stacks.iop.org/JPhysCM/21/075901

## Abstract
In this work we have performed atomistic simulations in $Ba_2RE^{3+}NbO_6$ ($RE^{3+}=$ La, Ce, Nd, Pr, Pm, Sm, Eu, Gd, Tb, Dy, Y, Ho, Er, Tm, Yb and Lu) compounds in order to predict their physical properties and behavior under lanthanide substitutions. The potential model adopted describes very well the structural and dielectric properties of these materials. The dependence of the tolerance factor on their physical properties was investigated and the results indicate that the lattice energy, sound velocities and bulk modulus do not show morphotropic phase boundaries between the three phases in which these compounds crystallize. These observables have a linear dependence on the tolerance factor. Only the elastic constant shows morphotropic phase boundaries.

(Some figures in this article are in colour only in the electronic version)

---

## 1. Introduction

The perovskite structure is doubtless the most versatile ceramic host that has been investigated in material science. Since the crystal chemistry investigations of Goldschmidt [1], several substitutions have been performed in $ABX_3$ basic stoichiometry with the aim of obtaining new compounds with new physical properties. Thus, compounds with perovskite or related structure were obtained as metallic conductors, superconductors, ferroelectrics, relaxors, high dielectric constant materials, piezoelectrics and electrooptics amongst others, as was very well reviewed by Bhalla *et al* [2]. Also, there is an increasing interest in ionic conductors with perovskite structure being used as separator materials in solid oxide fuel cells [3]. Commonly, the complex perovskite structure is that obtained by multiple ion substitution at the A, B or X sites. These substitutions can imply order or disorder, depending on the statistical distribution of ions among the sites. There are two large complex perovskite families when the substitution occurs at the B site: $A(B'_{1/3}B''_{2/3})X_3$ or $A(B'_{1/2}B''_{1/2})X_3$. Both families have great applicability in integrated industrial devices. In particular, the $Ba(RE_{1/2}Nb_{1/2})O_3$ family, where RE is a lanthanide ion or yttrium, has been investigated in the last two decades due to its interesting properties that make possible its application in the microwave frequency range [4–9]. Several investigations involving substitutions have been performed in order to understand its crystal chemistry, but conclusive general remarks are still not possible [10–13].

From the structural viewpoint, there are some controversies about the structure in which this family crystallizes. The first structural investigation of this family was performed by Brixner [14] who found a simple cubic perovskite structure with the exception of $RE=$ La which presented a distorted tetragonal perovskite structure. After this, Filip’ev and Fesenko observed that for $RE=$ La the structure was orthorhombic [15]. Later the unit cell for $RE=$ La was referred to as monoclinic while for $RE=$ Gd the unit cell was referred to as tetragonal by Von Wittmann [16]. Evdokimov and Menshenina also determined that for $RE=$ La–Sm the unit cell is monoclinic, tetragonal for $RE=$ Eu–Tb and double NaCl ordered perovskite type for $RE=$ Dy–Lu and Y [17]. After this, Henmi *et al* determined by Rietveld analyses of the x-ray diffraction that the structure for all compounds in the series is monoclinic belonging to the space group $P2_1/n$ that corresponds to the tilted system $(a^-a^-c^+)$ [18]. More recently,

The Raman spectra for this compound series was assigned as tetragonal for RE = Y, Gd and Tb and orthorhombic for Re = Sm, Gd and La [10]. Finally, using x-ray powder diffraction, Fu [12] showed that this family crystallizes in a distorted monoclinic structure for RE = La-Sm, tetragonal for RE = Eu-Dy and ordered cubic for RE = Ho and Y, belonging to $I2/m$, $I4/m$ and $Fm\overline{3}m$ space groups, respectively. The fact is that despite the crystalline structure for some compounds in this family being different from the NaCl ordered double cubic perovskite, the distortions are very low, complicating the structure determination. Moreover, all structural phase transitions between these phases are subtle without abrupt changes as shown by Fu [12] in the calculated octahedra tilt.

On this basis, we have employed atomistic simulation to model the $Ba_2RE^{3+}NbO_6$ family at room temperature in a NaCl ordered doubled cubic perovskite structure and derived structures where RE is a lanthanide ion or yttrium, in order to calculate their physical properties and investigate the behavior of these properties at the morphotropic phase boundaries. This procedure has been employed with success to model oxides with perovskite structure as reviewed in [19].

## 2. Computational methodology

In this work we have performed standard lattice-energy minimization to model the $Ba_2RE^{3+}NbO_6$ compounds using the General Utility Lattice Program (GULP) code [20, 21]. This methodology is based on the assumption of pairwise potentials for all interionic interactions. Thus, the minimum-energy structure is calculated at the fixed space groups in order to fit the experimentally determined unit cell parameters and other physical observables. The relaxation of the unit cell dimensions and atomic coordinates at constant pressure was obtained using a Newton-Raphson procedure together with the BFGS method of updating the Hessian matrix [22]. After relaxation of the structure, several bulk properties, such as elastic and dielectric constants, bulk modulus and lattice energy could be calculated.

The potential adopted for ionic compounds commonly has the form

$$
\varphi=\sum_{i>j}\left[\frac{e^{2}}{4 \pi \epsilon_{0}} \frac{Z_{i} Z_{j}}{r_{i j}}+A_{i j} \exp \left(-\frac{r_{i j}}{\rho_{i j}}\right)-\frac{C_{i j}}{r_{i j}^{6}}\right], \quad(1)
$$

where the first term describes the long-range electrostatic interaction between the ions of charge $Z_i e$ and $Z_j e$ separated by a distance $r_{ij}$; the second term gives the Pauli short-range repulsion and the last term is the induced-dipole attraction. In order to sum the Coulomb term, the Ewald summation [23] was employed. Finally, the superposition of the second and the third terms is called the short-range Buckingham potential, whose parameters $A_{ij}$, $\rho_{ij}$ and $C_{ij}$ are fitted to reproduce experimental data.

The $RE^{3+}$ ion was treated by a rigid ion model [24] due to its low polarizability. In contrast, the remaining ions were modeled by the shell model proposed by Dick and Overhauser [25], in order to consider the polarization of the other ions. In this model, it is assumed that the $i$th ion is formed by a massless shell with charge $Y_i$ and a core with mass $m_i$ and charge $X_i = Z_i - Y_i$, where $Z_i$ is the ion valence. To obtain a finite polarizability of the ions, the core is connected to the shell by a harmonic spring whose force constant is $k_i$.

<table>
<caption>Table 1. Short-range potential parameters for barium, niobium and oxygen ions assumed for $Ba_2RE^{3+}NbO_6$ compounds [26, 27].</caption>
<tbody>
<tr>
<td colspan="3">Shell-shell interactions</td>
</tr>
<tr>
<td></td>
<td>$A$ (eV)</td>
<td>$\rho$ (Å)</td>
<td>$C$ (eV Å$^6$)</td>
</tr>
<tr>
<td>$Ba^{2+}$–$O^{2-}$</td>
<td>4818.4160</td>
<td>0.306 700</td>
<td>0.00</td>
</tr>
<tr>
<td>$Nb^{5+}$–$O^{2-}$</td>
<td>1796.3000</td>
<td>0.345 980</td>
<td>0.00</td>
</tr>
<tr>
<td>$O^{2-}$–$O^{2-}$</td>
<td>25.4100</td>
<td>0.693 700</td>
<td>32.32</td>
</tr>
<tr>
<td colspan="3">Core-shell interactions</td>
</tr>
<tr>
<td></td>
<td>$k$ (eV Å$^{-2}$)</td>
<td>$Y$ (|e|)</td>
</tr>
<tr>
<td>$Ba^{2+}$</td>
<td>34.05</td>
<td>1.831 00</td>
</tr>
<tr>
<td>$Nb^{5+}$</td>
<td>1358.58</td>
<td>−4.497 00</td>
</tr>
<tr>
<td>$O^{2-}$</td>
<td>20.53</td>
<td>−2.513 00</td>
</tr>
</tbody>
</table>

In our simulations, for the $Ba^{2+}$–$O^{2-}$, $Nb^{5+}$–$O^{2-}$ and $O^{2-}$–$O^{2-}$ interactions, we have employed interionic potential parameters found in the literature [26, 27]. To describe the $RE^{3+}$–$O^{2-}$ interaction, we consider potential parameters that could describe better the dielectric constant of these compounds.

## 3. Results and discussions

### 3.1. Potential derivation

Initially, in order to obtain the interionic potentials of $Ba_2RE^{3+}NbO_6$ compounds, we firstly have assumed the $Ba^{2+}$–$O^{2-}$, $Nb^{5+}$–$O^{2-}$ and $O^{2-}$–$O^{2-}$ Buckingham and $Ba^{2+}$, $Nb^{5+}$ and $O^{2-}$ core–shell potentials listed in the literature [26, 27], which are given in table 1.

The interaction between $RE^{3+}$ and oxygen ions was initially modeled through the potential data presented by Lewis and Catlow [28]. However, these good potential data do not fit well the structural and dielectric data of the investigated materials. Thus, taking the RE = La interaction and optimizing its potential, in order to reproduce the structure and dielectric constant of the $Ba_2LaNbO_6$ compound, we have obtained the remaining $RE^{3+}$–$O^{2-}$ interactions, using the recursive relationship given by (2) [29, 30].

$$
A_{i}=A_{j} \exp \left(\frac{R_{\mathrm{i}}-R_{j}}{\rho}\right) \quad(2)
$$

where $R_i$ is the ionic radius of the lanthanide ion. Finally, the found potentials were refined in order to adjust simultaneously the best possible experimental structural data and dielectric constants. The final potential data obtained for these interactions are given in table 2 together with the tolerance factor $t$ calculated with basis in the $RE^{3+}$ ionic radius [31]. The tolerance factor is a geometrical parameter defined by Goldschmidt [1] for the $ABO_3$ perovskite compounds as follows

$$
t=\frac{R_{\mathrm{A}}+R_{\mathrm{O}}}{\sqrt{2}\left(R_{\mathrm{B}}+R_{\mathrm{O}}\right)}. \quad(3)
$$

**Table 2.** Potential parameters for the RE³⁺–O²⁻ short-range interactions used in this work.

| Ion | $t$ | $A$ (eV) | $\rho$ (Å) |
|-----|-----|----------|------------|
| La  | 0.952 | 806.83 | 0.371 755 |
| Ce  | 0.957 | 865.62 | 0.363 607 |
| Pr  | 0.961 | 941.48 | 0.355 825 |
| Nd  | 0.900 | 970.25 | 0.352 981 |
| Pm  | 0.965 | 1023.72 | 0.347 135 |
| Sm  | 0.968 | 1081.88 | 0.343 001 |
| Eu  | 0.970 | 1156.72 | 0.337 617 |
| Gd  | 0.972 | 1204.60 | 0.334 137 |
| Tb  | 0.976 | 1320.19 | 0.326 753 |
| Dy  | 0.978 | 1374.80 | 0.323 547 |
| Ho  | 0.981 | 1483.38 | 0.318 034 |
| Y   | 0.981 | 1463.80 | 0.318 857 |
| Er  | 0.983 | 1568.57 | 0.314 192 |
| Tm  | 0.985 | 1658.11 | 0.310 074 |
| Yb  | 0.988 | 1782.54 | 0.304 980 |
| Lu  | 0.990 | 1841.37 | 0.302 250 |

In the case of double ordered perovskites, this can be rewritten as

$$
t = \frac{R_{\mathrm{A}} + R_{\mathrm{O}}}{\sqrt{2} \left( \left( \frac{R_{\mathrm{B}'}+R_{\mathrm{B}''}}{2} \right) + R_{\mathrm{O}} \right)}. \tag{4}
$$

This parameter indicates how far from ideal packing the ionic sizes can move and the structure still remain as a perovskite [2]. Recently, useful correlations have been found between it and device-oriented physical properties of the materials, see for example [8, 9, 32]. Thus, it is interesting to investigate the dependence of this parameter on the physical properties and potential parameters. The behavior permits us to tailor the mixed materials to obtain the desired properties.

It is interesting to note that the structural check was also performed for the pseudocubic parameters calculated by [4]. Moreover, the structural adjust was good even for the compounds with monoclinic and tetragonal structures cited in [12], as we show in table 3. In this table we show the percentage error between experimental and calculated structural parameters. The low errors confirm the good reliability of the potential.

In figure 1 we show the ionic radius dependence on the short-range potential intensity $A$ and range $\rho$.

As pointed out by Senyshyn *et al* [33], the increase in $\rho$ and the decrease in $A$ demonstrate the so-called ‘lanthanide stiffness’ effect, where the atomic radius of the rare-earth elements decreases with increase of the atomic number. It is interesting to point out that $\rho$ increases linearly with the RE³⁺ ionic radius and the $A$ parameter has a sigmoidal decay behavior, as the adjusts indicate. This nonlinear behavior is imposed by the Pauli repulsion that inhibits the electronic shell superposition when the lanthanide ionic radius increases such that the sum of oxygen ($R_{\mathrm{O}}$) and lanthanide ($R_{\mathrm{RE}}$) ionic radii is of the order of the ionic distance in the $\mathrm{REO}_{6}$ octahedra. Thus, as the sigmoidal (Boltzmann) curve has a lower level constant it adjusts well for this behavior. In order to clarify this, figure 2 shows the $A$ dependence on the sum ($R_{\mathrm{O}} + R_{\mathrm{RE}}$). As we can note, the constant lower limit is imposed at distances in the proximity of the higher experimental ($R_{\mathrm{O}} + R_{\mathrm{RE}}$) distance obtained, which is $2.461$ Å, measured for the $\mathrm{Ba}_{2}\mathrm{LaNbO}_{6}$ [12].

![](./images/811873980003647489_1.jpg)

**Figure 1.** The dependence of short-range potential parameters on the rare-earth ionic radius for the RE³⁺–O²⁻ interaction.

<table><tbody><tr><td colspan="7">**Table 3.** Percentual error between calculated and experimental [4, 12] structural data for the investigated $\mathrm{Ba}_{2}\mathrm{RE}^{3+}\mathrm{NbO}_{6}$ compounds.</td></tr><tr><td></td><td></td><td colspan="2">Pseudocubic axis [4]</td><td colspan="3">Monoclinic [12]</td></tr><tr><td>Ion</td><td>$t$</td><td>$\Delta a$</td><td></td><td>$\Delta a$</td><td>$\Delta b$</td><td>$\Delta c$</td><td>$\Delta\theta$</td></tr><tr><td>La</td><td>0.952</td><td>0.04</td><td></td><td>0.14</td><td>0.22</td><td>1.08</td><td>0.03</td></tr><tr><td>Ce</td><td>0.957</td><td>—</td><td></td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>Pr</td><td>0.961</td><td>0.05</td><td></td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>Nd</td><td>0.900</td><td>0.05</td><td></td><td>0.70</td><td>0.03</td><td>0.13</td><td>0.03</td></tr><tr><td>Pm</td><td>0.965</td><td>—</td><td></td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>Sm</td><td>0.968</td><td>0.05</td><td></td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td colspan="8">Tetragonal [12]</td></tr><tr><td></td><td></td><td></td><td></td><td>$\Delta a$</td><td></td><td>$\Delta c$</td><td></td></tr><tr><td>Eu</td><td>0.970</td><td>0.05</td><td></td><td>—</td><td></td><td>—</td><td></td></tr><tr><td>Gd</td><td>0.972</td><td>0.05</td><td></td><td>0.23</td><td></td><td>0.20</td><td></td></tr><tr><td>Tb</td><td>0.976</td><td>0.02</td><td></td><td>0.26</td><td></td><td>0.04</td><td></td></tr><tr><td>Dy</td><td>0.978</td><td>0.06</td><td></td><td>—</td><td></td><td>—</td><td></td></tr><tr><td colspan="8">Cubic [12]</td></tr><tr><td></td><td></td><td></td><td></td><td>$\Delta a$</td><td></td><td></td><td></td></tr><tr><td>Ho</td><td>0.981</td><td>0.06</td><td></td><td>—</td><td></td><td></td><td></td></tr><tr><td>Y</td><td>0.981</td><td>0.06</td><td></td><td>0.40</td><td></td><td></td><td></td></tr><tr><td>Er</td><td>0.983</td><td>—</td><td></td><td>—</td><td></td><td></td><td></td></tr><tr><td>Tm</td><td>0.985</td><td>—</td><td></td><td>—</td><td></td><td></td><td></td></tr><tr><td>Yb</td><td>0.988</td><td>0.07</td><td></td><td>—</td><td></td><td></td><td></td></tr><tr><td>Lu</td><td>0.990</td><td>—</td><td></td><td>—</td><td></td><td></td><td></td></tr></tbody></table>

Good reliability of the assumed potential is given by the comparison between the measured [4] and calculated dielectric constants. This comparison is given in table 4. Once we have good potentials, we can calculate several physical properties of the compounds. In the next section we present the calculated physical properties and emphasize their behavior at the morphotropic phase boundaries (MPB).

### 3.2. Property calculations

The independent coefficients of the elastic constant tensors for the cubic, monoclinic and tetragonal symmetries in which the

![](./images/811873980003647489_2.jpg)

Figure 2. Short-range potential parameter dependence on the
$(R_O + R_{RE})$ sum.

![](./images/811873980003647489_3.jpg)

Figure 3. Independent tensor components of the elastic constant
tensor for the (a) cubic, (b) tetragonal and (c) monoclinic symmetries
in which $Ba_2RE^{3+}NbO_6$ compounds crystallize. The Nye
notation [34] has been used, where the symbol $\bullet$ indicates a non-zero
component, $\cdot$ indicates a zero component, two $\bullet$ connected by a line
indicates two components numerically equal and $\bullet$ connected by a
line to a $\bigcirc$ indicates two components whose moduli are equal but
opposite in sign.

Table 4. Comparison between the measured [4] and calculated
dielectric constants for the investigated $Ba_2RE^{3+}NbO_6$ compounds.

<table>
  <thead>
    <tr>
      <th>$RE^{3+}$</th>
      <th>$t$</th>
      <th>Calculated</th>
      <th>Measured</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>La</td>
      <td>0.952</td>
      <td>45.00</td>
      <td>45</td>
    </tr>
    <tr>
      <td>Ce</td>
      <td>0.957</td>
      <td>48.77</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Pr</td>
      <td>0.961</td>
      <td>44.50</td>
      <td>44.5</td>
    </tr>
    <tr>
      <td>Nd</td>
      <td>0.962</td>
      <td>44.00</td>
      <td>44</td>
    </tr>
    <tr>
      <td>Pm</td>
      <td>0.965</td>
      <td>49.28</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Sm</td>
      <td>0.968</td>
      <td>43.01</td>
      <td>43</td>
    </tr>
    <tr>
      <td>Eu</td>
      <td>0.970</td>
      <td>40.00</td>
      <td>40</td>
    </tr>
    <tr>
      <td>Gd</td>
      <td>0.972</td>
      <td>40.00</td>
      <td>40</td>
    </tr>
    <tr>
      <td>Tb</td>
      <td>0.976</td>
      <td>39.00</td>
      <td>39</td>
    </tr>
    <tr>
      <td>Dy</td>
      <td>0.978</td>
      <td>38.90</td>
      <td>38.9</td>
    </tr>
    <tr>
      <td>Ho</td>
      <td>0.981</td>
      <td>38.00</td>
      <td>38</td>
    </tr>
    <tr>
      <td>Y</td>
      <td>0.981</td>
      <td>36.99</td>
      <td>37</td>
    </tr>
    <tr>
      <td>Er</td>
      <td>0.983</td>
      <td>35.36</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Tm</td>
      <td>0.985</td>
      <td>35.85</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Yb</td>
      <td>0.988</td>
      <td>36.00</td>
      <td>36</td>
    </tr>
    <tr>
      <td>Lu</td>
      <td>0.990</td>
      <td>39.27</td>
      <td>—</td>
    </tr>
  </tbody>
</table>

$Ba_2RE^{3+}NbO_6$ compounds crystallize are shown in figure 3.
In this figure we used the Nye notation [34].

In figure 4 we show these elastic constant coefficients for
all the investigated $Ba_2RE^{3+}NbO_6$ compounds. As we can
see, they increase subtly with the tolerance factor. This linear
behavior is similar to that observed for the elastic constants
under low-pressure induced lattice changes and implies a linear
behavior of all observables that depends on the elastic constant
in the limit of lower lattice distortions. It is interesting to
note that both MPBs between cubic and tetragonal phases and
tetragonal and monoclinic phases are clear.

![](./images/811873980003647489_4.jpg)

Figure 4. Calculated independent coefficients of the elastic constant
tensor for the investigated $Ba_2RE^{3+}NbO_6$ compounds.

![](./images/811873980003647489_5.jpg)

Figure 5. Calculated wave velocities for the investigated
$Ba_2RE^{3+}NbO_6$ compounds.

These contours are not clear in other properties, such as
the S and P wave velocities, given in figure 5. These velocities
are practically constant for all compounds. Only for $RE = Y$
are the velocities subtly higher. This effect is due to the low
mass of the Y ion in relation to the lanthanide ions.

The bulk modulus shown in figure 6 increases practically
linearly with the tolerance factor but does not show the MPBs.
The behavior of the bulk modulus is given by

$$
B = -525.89 + 711.91t \tag{5}
$$

As the tolerance factor is a purely geometrical parameter,
we can tune in the bulk modulus by substituting similar

![](./images/811873980003647489_6.jpg)

Figure 6. Calculated bulk modulus for the investigated
Ba₂RE³⁺NbO₆ compounds. The line indicates a linear adjust.

![](./images/811873980003647489_7.jpg)

Figure 7. Calculated lattice energies for the investigated
Ba₂RE³⁺NbO₆ compounds. The line indicates a linear adjust.

ions. This is interesting information for applications as substrates.

The lattice energy also does not show the MPB. This fact reflects the low distortion drives out by the octahedra tilt in relation to the cubic phase. As well as the bulk modulus behavior, the energy dependence on the tolerance factor is also linear. But, in this case, there is a linear decrease in relation to the increase of the tolerance factor, as shown in figure 7.

The relation between tolerance factor and lattice energy is

$$
E_{\mathrm{L}}=-165.25-131.41 t. \tag{6}
$$

## 4. Concluding remarks

In this work we have used a static simulation method to investigate the dependence of the physical properties of the Ba₂RE³⁺NbO₆ (RE³⁺ = La, Ce, Nd, Pr, Pm, Sm, Eu, Gd, Tb, Dy, Y, Ho, Er, Tm, Yb and Lu) compounds on the tolerance factor. The model adopted describes very well the structural and dielectric properties of the compounds. The parameter that describes the short-range intensity of the interaction between the lanthanide and oxygen ions has a sigmoidal decrease imposed on the approximation of these ions. The parameter that describes the range in this interaction increases linearly. Both behaviors demonstrate the lanthanide stiffness effect. The calculated lattice energy, bulk modulus and sound velocities do not show the morphotropic phase boundaries between cubic, tetragonal and monoclinic phases in which these compounds crystallize. Moreover, the elastic constant coefficients show clearly the MPB.

## Acknowledgments

This work was partially supported by the Brazilian funding agencies CNPq and FAPEMA. We thank Dr J D Gale for permission to use the GULP code.

## References

[1] Goldschmidt V M 1927 *Geochemisce Verterlungsgesetze der Elemente* (Oslo: Norske Videnskap)
[2] Bhalla A S, Guo R Y and Roy R 2000 *Mater. Res. Innov.* **4** 3
[3] Kreuer K D 2003 *Annu. Rev. Mater. Res.* **33** 333
[4] Khalam L A, Sreemoolanathan H, Ratheesh R, Mohanan P and Sebastian M T 2004 *Mater. Sci. Eng.* **B** 107 264
[5] Kim H S, Kim J H, Choo W K and Setter N 2001 *J. Eur. Ceram. Soc.* **21** 1665
[6] Petzelt J, Zurmuhlen R, Bell A, Kamba S, Kozlov G V, Volkov A A and Setter N 1992 *Ferroelectrics* **133** 205
[7] Zurmuhlen R, Colla E, Dube D C, Petzelt J, Reaney I, Bell A and Setter N 1994 *J. Appl. Phys.* **76** 5864
[8] Zurmuhlen R, Petzelt J, Kamba S, Voitsekhovskii V V, Colla E and Setter N 1995 *J. Appl. Phys.* **77** 5341
[9] Zurmuhlen R, Petzelt J, Kamba S, Kozlov G, Volkov A, Gorshunov B, Dube D, Tagantsev A and Setter N 1995 *J. Appl. Phys.* **77** 5351
[10] Dias A, Khalam L A, Sebastian M T, William C, Paschoal C W A and Moreira R L 2006 *Chem. Mater.* **18** 214
[11] Moreira R L, Khalam L A, Sebastian M T and Dias A 2007 *J. Eur. Ceram. Soc.* **27** 2803
[12] Fu W T and Ijdo D J W 2006 *J. Solid State Chem.* **179** 1022
[13] Gregora I, Petzelt J, Pokorny J, Vorlicek V and Zikmund Z 1995 *Solid State Commun.* **94** 899
[14] Brixner L 1960 *J. Inorg. Nucl. Chem.* **15** 352
[15] Filip'ev V S and Fesenko G E 1961 *Kristallografiya* **6** 770
[16] Wittmann U, Rauser G and Kemmlersack S 1981 *Z. Anorg. Allg. Chem.* **482** 143
[17] Evdokimov A A and Menshenina N F 1982 *Zh. Neorg. Khim.* **27** 2137
[18] Henmi K, Hinatsu Y and Masaki N M 1999 *J. Solid State Chem.* **148** 353
[19] Islam M S 2000 *J. Mater. Chem.* **10** 1027
[20] Gale J D 1997 *J. Chem. Soc. Faraday Trans.* **93** 629
[21] Gale J D and Rohl A L 2003 *Mol. Simul.* **29** 291
[22] Press W H, Teukolsky S A, Vetterling W T and Flannery B P 1992 *Numerical Recipes in Fortran 77* (Cambridge: Cambridge University Press)
[23] Tosi M P 1964 *Solid State Phys.—Adv. Res. Appl.* **16** 1
[24] Valerio M E G, Jackson R A and de Lima J F 2000 *J. Phys.: Condens. Matter* **12** 7727
[25] Dick B G and Overhauser A W 1958 *Phys. Rev.* **112** 90
[26] Pirovano C, Islam M S, Vannier R N, Nowogrocki G and Mairesse G 2001 *Solid State Ion.* **140** 115

[27] Bush T S, Gale J D, Catlow C R A and Battle P D 1994
J. Mater. Chem. **4** 831

[28] Lewis G V and Catlow C R A 1985 *J. Phys. C: Solid State
Phys.* **18** 1149

[29] Banerjee A, Adams N, Simons J and Shepard R 1985 *J. Phys.
Chem.* **89** 52

[30] Woodley S M, Battle P D, Gale J D and Catlow C R A 2003
*Chem. Mater.* **15** 1669

[31] Shannon R D 1976 *Acta Crystallogr. A* **32** 751

[32] Colla I M R E L and Setter N 1994 *Japan. J. Appl. Phys.*
**33** 3984

[33] Senyshyn A, Ehrenberg H, Vasylechko L, Gale J D and
Bismayer U 2005 *J. Phys.: Condens. Matter* **17** 6217

[34] Nye J F 1985 *Physical Properties of Crystals: Their
Representation by Tensors and Matrices* (Oxford: Oxford
University Press)