![](./images/812402110615257089_1.jpg)

Available online at www.sciencedirect.com

![](./images/812402110615257089_2.jpg)

Chemical Physics Letters 373 (2003) 606-614

![](./images/812402110615257089_3.jpg)

www.elsevier.com/locate/cplett

# Coupled-cluster calculations of optical rotation

Kenneth Ruud $^{a,*}$, Philip J. Stephens $^{b}$, Frank J. Devlin $^{b}$, Peter R. Taylor $^{c}$,
James R. Cheeseman $^{d}$, Michael J. Frisch $^{d}$

$^{a}$ Department of Chemistry, University of Tromsø, N-9037 Tromso, Norway
$^{b}$ Department of Chemistry, University of Southern California, Los Angeles, CA 90089-0482, USA
$^{c}$ Department of Chemistry, University of Warwick, Coventry CV4 7AL, UK
$^{d}$ Gaussian Inc., 140 Washington Avenue, North Haven, CT 06473, USA

Received 19 March 2003

## Abstract
CC2 and CCSD coupled-cluster calculations of the sodium D line specific rotations of 13 chiral organic molecules are compared to HF and DFT/B3LYP calculations and to experiment. For 12 of the molecules, whose $[\alpha]_D$ values are in the range 0–200, CCSD and B3LYP $[\alpha]_D$ values are in very similar agreement with experiment: average deviations are 19.8 and 19.4, respectively. CC2 and HF values are less accurate: average deviations are 24.7 and 32.2, respectively. For one molecule, norbornenone, the CCSD $[\alpha]_D$ value (741) is very different from the B3LYP value (1216) and in much worse agreement with experiment (1146).

© 2003 Elsevier Science B.V. All rights reserved.

## 1. Introduction
Enantiomers of chiral molecules exhibit optical rotations of equal magnitude and opposite sign. In principle, the calculation of the optical rotation of a chiral molecule permits its absolute configura- tion to be determined. This has recently motivated a number of studies in which ab initio methods have been used to calculate optical rotations [1–18]. In a few cases, such calculations have been used to assign absolute configurations (see for example [12]).

The earliest ab initio calculations of optical rotation used the Hartree–Fock (HF) methodol- ogy [1–6]. More recently, density functional theory (DFT) [7–12,15–18], multiconfiguration self-con- sistent field (MCSCF) theory [13] and coupled- cluster (CC) theory [15] have been used. In the case of the HF and DFT methodologies, a thorough study of the basis set dependence of the sodium D line specific rotations $[\alpha]_D$ for two molecules (methyl oxirane and trans-2,3-dimethylthiirane) [7] and an extensive comparison of predicted and experimental $[\alpha]_D$ values for nearly 30 organic molecules and for a selection of basis sets [9] have been reported. These studies showed, inter alia, that (1) calculated rotations are strongly depen- dent on the choice of basis set, basis sets including diffuse functions giving results much closer to the

* Corresponding author. Fax: +47-7764-4737.
E-mail address: ruud@chem.uit.no (K. Ruud).

0009-2614/03/$ - see front matter © 2003 Elsevier Science B.V. All rights reserved.
doi:10.1016/S0009-2614(03)00667-5

basis set limit; and (2) DFT rotations are in sub- stantially better agreement with experiment than HF rotations, demonstrating the importance of including electron correlation. Up till now, sys- tematic studies of rotations predicted using other correlated methods, such as MCSCF and CC, have not been reported. Here, we report the first such study using CC theory. Specifically, we report CC2 and CCSD calculations of the $[\alpha]_{D}$ values of13 organic molecules, a subset of those studied previously using the HF and DFT methodologies[9]. These calculations have been made possible by recent developments in the implementation of CC linear response theory [19,20].

### 2. Methods

The specific rotation of a chiral molecule at thefrequency $v$ is given by [21-23]

$$
[\alpha]_{v}=\frac{28800 \pi^{2} N_{\mathrm{A}} v^{2}}{c^{2} M} \gamma_{\mathrm{s}, \mathrm{v}}[\beta(v)]_{0}, \quad(1)
$$

where $N_{\mathrm{A}}$ is Avogadro's number and $M$ is the molecular weight; $\beta(v)$ is given by

$$
\beta(v)=\frac{1}{3} \operatorname{Tr}\left[\beta_{\alpha \beta}(v)\right], \quad(2)
$$

where $\beta_{\alpha \beta}(v)$ is the mixed electric dipole-magnetic dipole polarizability tensor, given within linear response theory by

$$
\beta_{\alpha \beta}=\omega^{-1} \operatorname{Im}\left\langle\left\langle\mu_{\alpha}^{\mathrm{e}} ; m_{\beta}^{\mathrm{e}}\right\rangle\right\rangle_{\omega}, \quad(3)
$$

where $\omega(=2 \pi v)$ is the frequency in atomic units, and $\mu_{\alpha}^{\mathrm{e}}$ and $m_{\beta}^{\mathrm{e}}$ are components of the electronic electric and magnetic dipole operators respec- tively. $[\beta(v)]_{0}$ is the value of $\beta(v)$ at the gas phase equilibrium geometry. $\gamma_{s, v}$ is the contribution of solvent and vibrational effects. In this work, sol- vent and vibrational effects are not included, i.e., $\gamma_{s, v}=1$.

The calculations reported in this Letter have been made possible by the recent extension of the DALTON program [24] to calculate linear response functions for various CC wave functions [19,20]. Since the truncated CC wave function is non-var- iational, gauge origin independence cannot be achieved, even in the limit of a complete basis set[25]. Our results will therefore depend on our choice of a gauge origin. Note that, for frequency- dependent properties such as the optical rotation, the origin dependence remains even if London orbitals [26] (gauge-invariant/including atomic orbitals, GIAOs) are used; in contrast to the HF, MCSCF and DFT methodologies, the inclusion of London orbitals does not eliminate the problem of origin dependence in CC calculations.

We use the cc-pVXZ and aug-cc-pVXZ $(X=D, T, Q)$ correlation-consistent basis sets de veloped by Dunning and Woon [27,28]. DFT/ B3LYP/6-31G* optimized geometries have been used throughout (as in [9]). HF and DFT/B3LYP calculations of optical rotations not already re- ported in [9] were carried out using the GAUSSIAN program [29].

### 3. Results

We have examined the basis set and origin de- pendence of CC2 and CCSD $[\alpha]_{D}$ values for the small, chiral molecule $CNOFH_{2}$ (derived from2-F-oxirane by substitution of the ring $CH_{2}$ with NH). The B3LYP/6-31G* geometry is given in Table $1.[\alpha]_{D}$ values calculated using the cc-pVDZ, cc-pVTZ, aug-cc-pVDZ and aug-cc-pVTZ basis sets with the origin at the center of mass are given in Table 2, together with HF and B3LYP values calculated using the same basis sets (and also using aug-cc-pVQZ), with and without London orbitals. For both CC2 and CCSD we find large changes in[a], when the basis set is changed from cc-pVDZ to cc-pVTZ, but small changes from aug-cc-pVDZ to aug-cc-pVTZ. Thus, as reported previously for

Table 1
DFT/B3LYP/6-31G* optimized geometry (in Bohr) of $CNOFH_{2}$

<table>
<thead>
<tr>
<th>Atom</th>
<th>X</th>
<th>Y</th>
<th>Z</th>
</tr>
</thead>
<tbody>
<tr>
<td>C</td>
<td>0.235331</td>
<td>−0.024799</td>
<td>2.604937</td>
</tr>
<tr>
<td>N</td>
<td>1.135707</td>
<td>2.265012</td>
<td>3.680713</td>
</tr>
<tr>
<td>O</td>
<td>2.673760</td>
<td>−0.161604</td>
<td>3.442526</td>
</tr>
<tr>
<td>F</td>
<td>−0.131918</td>
<td>−0.013366</td>
<td>0.087106</td>
</tr>
<tr>
<td>H(N)</td>
<td>0.626412</td>
<td>2.288347</td>
<td>5.557639</td>
</tr>
<tr>
<td>H(C)</td>
<td>−1.181567</td>
<td>−1.202414</td>
<td>3.530770</td>
</tr>
</tbody>
</table>

Origin is at the center of mass.

<table>
<caption>Table 2
Basis set dependence of $[\alpha]_D$ for $CNOFH_2$</caption>
<thead>
<tr>
<th>Basis set</th>
<th>HF
(No London)ª</th>
<th>HF
(London)</th>
<th>B3LYP
(No London)ª</th>
<th>B3LYP
(London)</th>
<th>CC2
(No London)ª</th>
<th>CCSD
(No London)ª</th>
</tr>
</thead>
<tbody>
<tr>
<td>cc-pVDZ</td>
<td>122</td>
<td>112</td>
<td>54</td>
<td>57</td>
<td>45</td>
<td>60</td>
</tr>
<tr>
<td>aug-cc-pVDZ</td>
<td>143</td>
<td>142</td>
<td>79</td>
<td>79</td>
<td>74</td>
<td>87</td>
</tr>
<tr>
<td>cc-pVTZ</td>
<td>124</td>
<td>120</td>
<td>66</td>
<td>62</td>
<td>69</td>
<td>82</td>
</tr>
<tr>
<td>aug-cc-pVTZ</td>
<td>135</td>
<td>134</td>
<td>76</td>
<td>75</td>
<td>77</td>
<td>91</td>
</tr>
<tr>
<td>aug-cc-pVQZ</td>
<td>133</td>
<td>133</td>
<td>75</td>
<td>75</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

$[\alpha]_D$ values are in degrees $[\text{dm }(\text{gm/cm}^3)]^{-1}$.
ªOrigin is at the center of mass.

the HF and B3LYP methods [7], convergence to the complete basis set limit is accelerated when diffuse functions are included in the basis set. At both the HF and B3LYP levels ‘London’ and ‘no-London’ $[\alpha]_D$ values are very similar when the augmented basis sets are used; differences are much larger for the non-augmented basis sets.

The origin dependence of the CC2 and CCSD $[\alpha]_D$ values for $CNOFH_2$ calculated using the no-London aug-cc-pVDZ and aug-cc-pVTZ basis sets is illustrated in Table 3, together with the corresponding HF and B3LYP results. At the aug-cc-pVDZ basis set level the origin dependence is greater for CCSD (76–106) than for CC2 (73–86). The CC2 origin dependence is comparable to that for B3LYP (75–84). The HF $[\alpha]_D$ values exhibit the smallest origin dependence (140–146). At the aug-cc-pVTZ basis set level, the origin dependence of HF and B3LYP $[\alpha]_D$ values is greatly reduced, to an extent that the $[\alpha]_D$ values are essentially origin independent. In contrast, the origin dependences of the CC2 and CCSD $[\alpha]_D$ values are greater than at the aug-cc-pVDZ basis set level. These results illustrate the fact, discussed earlier, that truncated CC $[\alpha]_D$ values are not gauge invariant, even in the limit of a complete basis set. Quantitatively, the origin dependence can be substantial, even across a small molecule such as $CNOFH_2$.

<table>
<caption>Table 3
Origin dependence of $[\alpha]_D$ of $CNOFH_2$ using the no-London aug-cc-pVDZ and aug-cc-pVTZ basis sets</caption>
<thead>
<tr>
<th>Origin</th>
<th>HF</th>
<th>B3LYP</th>
<th>CC2</th>
<th>CCSD</th>
</tr>
</thead>
<tbody>
<tr>
<td>COM</td>
<td>143/135ª</td>
<td>79/76ª</td>
<td>74/77ª</td>
<td>87/91ª</td>
</tr>
<tr>
<td>F</td>
<td>146/135</td>
<td>81/76</td>
<td>86/86</td>
<td>106/110</td>
</tr>
<tr>
<td>H(N)</td>
<td>141/134</td>
<td>84/77</td>
<td>74/69</td>
<td>76/60</td>
</tr>
<tr>
<td>H(C)</td>
<td>140/135</td>
<td>75/76</td>
<td>73/77</td>
<td>84/83</td>
</tr>
</tbody>
</table>

$[\alpha]_D$ values are in degrees $[\text{dm }(\text{gm/cm}^3)]^{-1}$.
ªFirst and second numbers are for the aug-cc-pVDZ and aug-cc-pVTZ basis sets, respectively.

We now turn our attention to the set of 13 molecules listed in Table 4. These molecules are a subset of a larger set previously studied using the HF and DFT methods [9]. CC calculations have been carried out using the no-London aug-cc-pVDZ basis set; at the present time, aug-cc-pVTZ calculations are not practicable. It is also impractical to carry

<table>
<caption>Table 4
Molecules investigated in this Letter</caption>
<tbody>
<tr>
<td>1</td>
<td>2S-2-methyloxirane</td>
</tr>
<tr>
<td>2</td>
<td>(2R,3R)-trans-2,3-dimethyloxirane</td>
</tr>
<tr>
<td>3</td>
<td>2R-2-methylthiirane</td>
</tr>
<tr>
<td>4</td>
<td>(2R,3R)-trans-2,3-dimethylthiirane</td>
</tr>
<tr>
<td>5</td>
<td>(1S,2S)-trans-1,2-dimethylcyclopropane</td>
</tr>
<tr>
<td>6</td>
<td>(2R,3R)-1-methylene-trans-2,3-dimethylcyclopropane</td>
</tr>
<tr>
<td>7</td>
<td>(2R,3R)-trans-dimethylaziridine</td>
</tr>
<tr>
<td>8</td>
<td>(2R,3R)-N-chloro-trans-2,3-dimethylaziridine</td>
</tr>
<tr>
<td>9</td>
<td>(1S,2R)-cis-N-chloro-2-methylaziridine</td>
</tr>
<tr>
<td>10</td>
<td>(1S,2R)-trans-N-chloro-2-methylaziridine</td>
</tr>
<tr>
<td>11</td>
<td>(3S)-3-methylcyclobutene</td>
</tr>
<tr>
<td>13</td>
<td>S-1,3-dimethylallene</td>
</tr>
<tr>
<td>14</td>
<td>(1S,4S)-norbornenone</td>
</tr>
</tbody>
</table>

The numbering is that of [9]. See also Fig. 1 in [9].

out calculations for each molecule with a variety of origins. Accordingly, we have adopted a single, uniform choice of origin, namely the center of mass. We fully recognize that $[\alpha]_D$ values would be different with a different choice of origin.

$[\alpha]_D$ values calculated at the CC2 and CCSD levels for molecules **1–11, 13** and **14** are given in Table 5, together with HF and B3LYP values (both calculated using London orbitals and therefore origin independent) and experimental $[\alpha]_D$ values. HF, B3LYP, CC2/COM and CCSD/COM $[\alpha]_D$ values are also compared to experimental $[\alpha]_D$ values in Fig. 1. (For ease of presentation, we will in the rest of this Letter refer to the set of molecules **1–11** and **13** as molecules **1–13**, implicitly excluding molecule **12** of [9], which is presently too large for CC calculations.)

For molecules **1–13**, B3LYP and CCSD/COM $[\alpha]_D$ values are in comparable agreement with experiment. Average absolute deviations from experimental $[\alpha]_D$ values are: B3LYP, 19.4; and CCSD/COM, 19.8. Agreement of the CC2/COM $[\alpha]_D$ values is somewhat lower; the average absolute deviation is 24.7. Agreement is worst for the HF $[\alpha]_D$ values, for which the average absolute deviation is 32.2. Thus, prima facie, one can conclude that the accuracies of calculated $[\alpha]_D$ values are: $\text{HF} < \text{CC2/COM} < \text{CCSD/COM} \approx \text{B3LYP}$.

While very similar in their overall accuracy in predicting experimental $[\alpha]_D$ values, B3LYP and CCSD/COM $[\alpha]_D$ values can differ substantially for individual molecules. The largest differences are found for molecules **11** and **13**: 42.8 and 56.2 respectively. When B3LYP and CCSD/COM $[\alpha]_D$ values differ substantially, in some cases B3LYP $[\alpha]_D$ values are closer to experiment, while in other cases CCSD/COM values are in better agreement. Thus, for example, in the case of **11**, the B3LYP $[\alpha]_D$ differs from experiment by 3.9, while the CCSD/COM $[\alpha]_D$ differs by 46.7. In the case of **13**, the differences are: B3LYP, 54.4; CCSD/COM, 1.8.

Calculated $[\alpha]_D$ values can be written $[\alpha]_D = \sum_\alpha [\alpha]_D^{\alpha\alpha}\ (\alpha=x,y,z)$. $[\alpha]_D^{xx}$, $[\alpha]_D^{yy}$ and $[\alpha]_D^{zz}$ values are given in Table 6. For each molecule, $[\alpha]_D^{\alpha\alpha}$ values are both positive and negative, and considerable cancellation occurs in calculating $[\alpha]_D$. In Fig. 2 we compare the HF, B3LYP and CC2/COM values for all components, $[\alpha]_D^{\alpha\alpha}$, of $[\alpha]_D$ to the CCSD/COM values. Least-squares linear fits for molecules **1–13** give lines of slope: HF 1.072; B3LYP 1.147 and CC2/COM 1.045. Scatter is quite small for the B3LYP and CC2/COM fits. Thus, B3LYP

Table 5
Calculated and experimental $[\alpha]_D$ values

<table>
  <thead>
    <tr>
      <th>Molecule</th>
      <th>HFª</th>
      <th>B3LYPª</th>
      <th>CC2ᵇ</th>
      <th>CCSDᵇ</th>
      <th>Experimentᶜ</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>−13.8</td>
      <td>−17.5</td>
      <td>−38.4</td>
      <td>−29.2</td>
      <td>−18.7</td>
    </tr>
    <tr>
      <td>2</td>
      <td>53.4</td>
      <td>78.6</td>
      <td>101.8</td>
      <td>78.3</td>
      <td>58.8</td>
    </tr>
    <tr>
      <td>3</td>
      <td>78.4</td>
      <td>53.1</td>
      <td>66.6</td>
      <td>69.0</td>
      <td>51.2</td>
    </tr>
    <tr>
      <td>4</td>
      <td>162.9</td>
      <td>167.1</td>
      <td>170.1</td>
      <td>156.0</td>
      <td>129.0</td>
    </tr>
    <tr>
      <td>5</td>
      <td>48.6</td>
      <td>59.0</td>
      <td>43.2</td>
      <td>41.2</td>
      <td>42.0</td>
    </tr>
    <tr>
      <td>6</td>
      <td>−21.6</td>
      <td>3.4</td>
      <td>−14.5</td>
      <td>−2.6</td>
      <td>57.6</td>
    </tr>
    <tr>
      <td>7</td>
      <td>65.9</td>
      <td>103.1</td>
      <td>123.0</td>
      <td>93.5</td>
      <td>103.8</td>
    </tr>
    <tr>
      <td>8</td>
      <td>−60.4</td>
      <td>−28.4</td>
      <td>−27.2</td>
      <td>−29.9</td>
      <td>−16.8</td>
    </tr>
    <tr>
      <td>9</td>
      <td>42.8</td>
      <td>78.6</td>
      <td>60.0</td>
      <td>61.3</td>
      <td>78.2</td>
    </tr>
    <tr>
      <td>10</td>
      <td>−133.3</td>
      <td>−133.2</td>
      <td>−114.8</td>
      <td>−117.1</td>
      <td>−103.4</td>
    </tr>
    <tr>
      <td>11</td>
      <td>−129.2</td>
      <td>−171.7</td>
      <td>−154.3</td>
      <td>−128.9</td>
      <td>−175.6</td>
    </tr>
    <tr>
      <td>13</td>
      <td>117.4</td>
      <td>135.4</td>
      <td>104.1</td>
      <td>79.2</td>
      <td>81.0</td>
    </tr>
    <tr>
      <td>14</td>
      <td>−606.7</td>
      <td>−1215.8</td>
      <td>−1000.0</td>
      <td>−740.6</td>
      <td>−1146.0</td>
    </tr>
  </tbody>
</table>

$[\alpha]_D$ values are in degrees $[\text{dm}\ (\text{gm/cm}^3)]^{-1}$. All calculations used the aug-cc-pVDZ basis set except for the CC2 and CCSD calculations on **14** where the basis set was aug-cc-pVDZ/cc-pVDZ. All calculations used B3LYP/6-31G* geometries. The HF and B3LYP calculations used London orbitals (GIAOs); CC2 and CCSD calculations did not. The origins for the CC2 and CCSD calculations were the centers of mass.

ªFrom [9].
ᵇThis work.
ᶜFrom [9] and corrected to 100% ee.

![](./images/812402110615257089_4.jpg)

Fig. 1. Comparison of HF, CC2/COM, CCSD/COM and B3LYP $[\alpha]_D$ values for 1-11, 13 and 14 to experiment. The lines have slope +1. The inset expands the plot for 1-11 and 13.

and CC2/COM $[\alpha]_D^{zz}$ values are systematically greater than CCSD/COM values by, on average, $\approx$15% and $\approx$5%, respectively. Scatter is much larger for the HF fit.

The generalizations arrived at above for molecules 1-13 do not extend to molecule 14. First, and most dramatic, B3LYP and CCSD/COM $[\alpha]_D$ values (1216 and 741, respectively) differ hugely. The B3LYP result is in much better agreement with experiment: deviations are 70 and 405 for B3LYP and CCSD/COM, respectively. Second, CC2/COM and CCSD/COM $[\alpha]_D$ values (1000 and 741) are very different, and the CC2/COM value is in better agreement with experiment, giving a deviation of 146. These results can largely be attributed to the 'anomalous' behavior of the $[\alpha]_D^{xx}$ contribution to $[\alpha]_D$. At the B3LYP, CC2/COM and CCSD/COM levels, $[\alpha]_D^{xx}$ is 2455, 2043 and 1681, respectively. This contribution is very large and is the dominant contribution to $[\alpha]_D$. As a result, the variation in $[\alpha]_D$ is predominantly due to the variation in $[\alpha]_D^{xx}$, which from B3LYP to CCSD/COM varies by 774. As shown in Fig. 2, $[\alpha]_D^{xx}$ for molecule 14 lies far from the line fitting the $[\alpha]_D^{zz}$ values for molecules 1-13, whether it is the B3LYP or CC2/COM values which are compared to the CCSD/COM values. That is, the percentage variations from the CCSD/COM $[\alpha]_D^{xx}$ of the B3LYP and CC2/COM values, 46% and 22% respectively, are much greater than the $\approx$15% and $\approx$5% variations found for the $[\alpha]_D^{zz}$ values of molecules 1-13.

Table 6
Calculated and $[\alpha]_D^{xx}$, $[\alpha]_D^{yy}$ and $[\alpha]_D^{zz}$ values

<table>
<thead>
<tr>
<th>Molecules</th>
<th colspan="4">$[\alpha]_D^{xx}$</th>
<th colspan="4">$[\alpha]_D^{yy}$</th>
<th colspan="4">$[\alpha]_D^{zz}$</th>
</tr>
<tr>
<th></th>
<th>HF</th>
<th>B3LYP</th>
<th>CC2</th>
<th>CCSD</th>
<th>HF</th>
<th>B3LYP</th>
<th>CC2</th>
<th>CCSD</th>
<th>HF</th>
<th>B3LYP</th>
<th>CC2</th>
<th>CCSD</th>
</tr>
</thead>
<tbody>
<tr>
<th>1</th>
<td>−159.2</td>
<td>−175.4</td>
<td>−136.0</td>
<td>−147.9</td>
<td>−151.5</td>
<td>−173.1</td>
<td>−159.3</td>
<td>−154.3</td>
<td>296.9</td>
<td>331.0</td>
<td>256.9</td>
<td>273.0</td>
</tr>
<tr>
<th>2</th>
<td>32.2</td>
<td>61.6</td>
<td>50.0</td>
<td>54.4</td>
<td>142.3</td>
<td>135.3</td>
<td>98.8</td>
<td>116.1</td>
<td>−121.1</td>
<td>−118.2</td>
<td>−47.0</td>
<td>−92.2</td>
</tr>
<tr>
<th>3</th>
<td>−37.9</td>
<td>−186.9</td>
<td>−192.3</td>
<td>−150.5</td>
<td>−6.6</td>
<td>6.4</td>
<td>−5.6</td>
<td>−34.1</td>
<td>122.9</td>
<td>233.6</td>
<td>246.4</td>
<td>253.5</td>
</tr>
<tr>
<th>4</th>
<td>336.8</td>
<td>437.6</td>
<td>383.9</td>
<td>376.1</td>
<td>230.6</td>
<td>203.8</td>
<td>194.9</td>
<td>183.9</td>
<td>−404.7</td>
<td>−474.4</td>
<td>−408.7</td>
<td>−404.0</td>
</tr>
<tr>
<th>5</th>
<td>355.3</td>
<td>411.8</td>
<td>405.8</td>
<td>359.6</td>
<td>−293.0</td>
<td>−368.2</td>
<td>−337.0</td>
<td>−307.7</td>
<td>−13.7</td>
<td>15.3</td>
<td>−25.6</td>
<td>−10.4</td>
</tr>
<tr>
<th>6</th>
<td>341.9</td>
<td>612.3</td>
<td>533.6</td>
<td>525.1</td>
<td>−371.3</td>
<td>−499.2</td>
<td>−472.0</td>
<td>−412.8</td>
<td>7.8</td>
<td>−109.7</td>
<td>−76.1</td>
<td>−114.9</td>
</tr>
<tr>
<th>7</th>
<td>334.1</td>
<td>304.4</td>
<td>259.7</td>
<td>249.0</td>
<td>−184.7</td>
<td>−200.9</td>
<td>−161.5</td>
<td>−168.4</td>
<td>−83.4</td>
<td>−0.5</td>
<td>24.8</td>
<td>12.9</td>
</tr>
<tr>
<th>8</th>
<td>−907.3</td>
<td>−854.1</td>
<td>−803.0</td>
<td>−770.3</td>
<td>540.5</td>
<td>496.7</td>
<td>487.4</td>
<td>462.1</td>
<td>306.4</td>
<td>329.0</td>
<td>288.4</td>
<td>278.4</td>
</tr>
<tr>
<th>9</th>
<td>405.2</td>
<td>419.3</td>
<td>416.5</td>
<td>380.9</td>
<td>−917.8</td>
<td>−917.0</td>
<td>−873.6</td>
<td>−826.2</td>
<td>555.4</td>
<td>576.2</td>
<td>517.2</td>
<td>506.5</td>
</tr>
<tr>
<th>10</th>
<td>−804.7</td>
<td>−825.3</td>
<td>−774.3</td>
<td>−728.2</td>
<td>682.7</td>
<td>690.7</td>
<td>658.6</td>
<td>624.7</td>
<td>−11.2</td>
<td>1.5</td>
<td>0.9</td>
<td>−13.6</td>
</tr>
<tr>
<th>11</th>
<td>−546.3</td>
<td>−526.4</td>
<td>−432.4</td>
<td>−428.4</td>
<td>−319.0</td>
<td>−275.2</td>
<td>−224.9</td>
<td>−200.4</td>
<td>736.1</td>
<td>630.0</td>
<td>502.9</td>
<td>499.9</td>
</tr>
<tr>
<th>13</th>
<td>1081.3</td>
<td>1075.0</td>
<td>958.1</td>
<td>906.1</td>
<td>−572.0</td>
<td>−842.4</td>
<td>−771.7</td>
<td>−749.5</td>
<td>−392.0</td>
<td>−97.4</td>
<td>−82.2</td>
<td>−77.4</td>
</tr>
<tr>
<th>14</th>
<td>−1651.7</td>
<td>−2454.6</td>
<td>−2042.8</td>
<td>−1681.1</td>
<td>518.9</td>
<td>794.9</td>
<td>770.9</td>
<td>678.6</td>
<td>526.4</td>
<td>444.6</td>
<td>272.0</td>
<td>261.9</td>
</tr>
</tbody>
</table>

For units and calculational details, see Table 5.

![](./images/812402110615257089_5.jpg)

Fig. 2. Comparison of HF, CC2/COM and B3LYP $[\alpha]_D^{zz}$ values for 1-11, 13 and 14 to CCSD/COM values. Open circles are for 1-11 and 13; filled circles are for 14. The lines are least-squares fits, excluding molecule 14.

### 4. Discussion

For the 12 molecules **1–13** both B3LYP and CCSD/COM calculations at the aug-cc-pVDZ basis set level yield $[\alpha]_D$ values differing on average from experimental values by <20. The residual differences can be attributed to: (1) remaining errors in the B3LYP and CCSD/COM methodologies; (2) vibrational effects; (3) solvent effects and (4) experimental errors. That errors remain in the B3LYP and/or CCSD/COM calculations of $[\beta]_0$ is shown by the fact that B3LYP and CCSD/COM $[\alpha]_D$ values can differ substantially; on average, their difference is 17.2. Vibrational effects and solvent effects undoubtedly exist [11,14]. Their magnitudes are not easily predicted – and can be expected to vary substantially with the molecule – but it is very likely that, on average, they are commensurate with the deviations between calculated and experimental values. Experimental errors – for example arising from errors in enantiomeric excesses – cannot be assumed to be negligible. It is clear that for molecules **1–13**, a more precise definition of the absolute and relative accuracies of B3LYP and CCSD/COM $[\beta]_0$ values requires a more precise evaluation of vibrational effects, solvent effects and experimental errors. At the present time, it would be premature to conclude that there is a significant difference in accuracy in the B3LYP and CCSD/COM $[\beta]_0$ values.

For **1–13**, HF $[\alpha]_D$ values differ on average from experimental values by >30. The significantly lower accuracy of HF $[\alpha]_D$ values compared to B3LYP $[\alpha]_D$ values was previously demonstrated by comparisons to experimental $[\alpha]_D$ values for 28 molecules, including the molecules of this study [9]. Here, we have further demonstrated the importance of the inclusion of correlation in the calculation of $[\alpha]_D$ via the improved accuracy of CCSD/COM $[\alpha]_D$ values. At the same time, it should be noted that, *for molecules 1–13*, the contributions of electron correlation are modest in magnitude. HF $[\alpha]_D$ values differ on average from B3LYP and CCSD/COM $[\alpha]_D$ values by 21.6 and 17.9.

In addition to CCSD/COM calculations of $[\alpha]_D$, CC2/COM calculations have been carried out in order to gauge the degree of convergence of the CCSD/COM calculations to the full CC limit. On average, CC2/COM $[\alpha]_D$ values deviate from experimental values by 24.7. Their accuracy is intermediate between HF and CCSD/COM $[\alpha]_D$ values, as to be expected, and closer to CCSD/COM. Thus, one may anticipate relatively small changes on passing to higher level CC approximations, such as CC3 [30] and CCSDT.

Molecule **14**, norbornenone, is in a different category from molecules **1–13**. As is already clear from the prior comparison of HF and B3LYP $[\alpha]_D$ values [9], 607 and 1216, respectively, the electron correlation contribution is very large for this molecule. The B3LYP $[\alpha]_D$ is in very good agreement with the experimental value of 1146. Surprisingly, the CCSD/COM $[\alpha]_D$ value 741 is actually closer to the HF value than to the B3LYP value. In contrast to the average behavior of molecules **1–13**, for molecule **14** $[\alpha]_D$ values swing dramatically in progressing from HF to CC2/COM to CCSD/COM. The CC2/COM value of $[\alpha]_D$, 1000, is much closer to both B3LYP and experimental values than is the CCSD/COM value. It appears that for molecule **14**, CCSD/COM is far from the CC limit. Clearly, this deserves further investigation, and depends on the assumption that, for **14**, vibrational effects, solvent effects and experimental errors are all small. Solvent effects should be minimal since the solvent is the low dielectric, innocuous solvent hexane [31]. Vibrational effects are difficult to estimate. However, it is unlikely that they could be as large as the difference between the CCSD/COM and experimental $[\alpha]_D$ values of (405).

Optical rotation and electronic circular dichroism (CD) are intimately interconnected. The rotational strength $R_i$ determines the CD intensity of electronic excitation $i$. The rotational strength of the lowest $\mathrm{n} \rightarrow \pi^{*}$ electronic excitation of **14** has been measured [32]. The energies and rotational strengths of this excitation calculated at the B3LYP, CC2 and CCSD levels using the aug-cc-pVDZ basis set are compared to experimental values in Table 7. (Note that the rotational strengths are calculated using the velocity representation and are therefore origin independent.) In addition, the contribution of the lowest excitation to $[\alpha]_D$, $[\alpha]_D^{\mathrm{n} \rightarrow \pi^{*}}$, is given. For this particular molecule, the contribution of the lowest excitation to $[\alpha]_D$ is large. It is not unrea-

Table 7
Electronic excitation energies and rotational strengths of the
$n \rightarrow \pi^{*}$ transition of 14 and its contribution to $[\alpha]_{D}$

|          | $\Delta E$ (eV) | $\lambda$ (nm) | $R^{\text{a}}$ | $[\alpha]_{D}$ (n $\rightarrow \pi^{*}$)$^{\text{b}}$ |
|----------|-----------------|----------------|----------------|-------------------------------------------------------|
| HF$^{\text{c}}$ | 4.86            | 255            | $-44.6$        | $-869$                                                 |
| B3LYP$^{\text{d}}$ | 4.03          | 307            | $-55.6$        | $-1756$                                                |
| CC2$^{\text{e}}$ | 4.26           | 291            | $-37.6$        | $-1026$                                                |
| CCSD$^{\text{e}}$ | 4.30          | 288            | $-23.1$        | $-615$                                                 |
| Expt.$^{\text{f}}$ | 4.02         | 308            | $-51$          | $-1627$                                                |

The HF, B3LYP and CC2 calculations used the aug-cc-pVDZ basis set; the CCSD calculation used the aug-cc-p-VDZ/cc-pVDZ basis set. All calculations used the velocity representation of the rotational strength $R$, yielding origin independent $R$ values.
$^{\text{a}}$ $R$ values are in $10^{-40}$ esu$^{2}$ cm$^{2}$.
$^{\text{b}}$ Contribution of the n $\rightarrow \pi^{*}$ excitation to $[\alpha]_{D}$, obtained from the excitation energies and rotational strengths in this table.
$^{\text{c}}$ The HF results were obtained using the RPA and GAUSSIAN [29]. London orbitals/GIAOs were not used. For earlier RPA calculations, see [33].
$^{\text{d}}$ The B3LYP results obtained using time-dependent DFT (TDDFT) and GAUSSIAN [29]. London orbitals/GIAOs were not used.
$^{\text{e}}$ The CC2 and CCSD results were obtained using linear response theory and DALTON [24].
$^{\text{f}}$ From [32]. The energy and wavelength are for the most intense vibrational component [34].

sonable, therefore, to expect the accuracies of calculated $[\alpha]_{D}$ values to track the accuracies of the rotational strengths of the lowest excitation. From Table 7, we see that B3LYP, CC2 and CCSD calculations all give excitation energies in good agreement with the experimental value (allowing for the considerable uncertainty in the latter due to the complex band shape observed). However, while the B3LYP $R$ value is in excellent agreement with the experimental value (and probably within the experimental error bars of the latter), the CC2 and CCSD $R$ values are much smaller and in much worse agreement with experiment. Thus, for 14 the relative accuracies of the B3LYP, CC2 and CCSD n $\rightarrow \pi^{*}$ $R$ values are B3LYP $>$ CC2 $>$ CCSD, identical to the ordering found for the $[\alpha]_{D}$ values. This corroborates our findings for the $[\alpha]_{D}$ values regarding the relative accuracies of the B3LYP, CC2 and CCSD methods, and suggests that the reason for the lower accuracy of the CCSD $[\alpha]_{D}$ value might become clearer if the reason for the lower $R$ value of the n $\rightarrow \pi^{*}$ transition can be identified.

The HF(RPA) results in Table 7 show that the
$\mathrm{n} \rightarrow \pi^{*}$ excitation energy is substantially higher
than the B3LYP energy, while the HF $R$ value is
somewhat smaller than the B3LYP $R$ value. Thus,
the contribution of the $\mathrm{n} \rightarrow \pi^{*}$ transition to $[\alpha]_{D}$ is
much smaller at the HF level predominantly be-
cause of the difference in excitation energy.

## 5. Conclusion
For molecules 1-13, whose $[\alpha]_{D}$ values are in the range $0-200$, CCSD/COM calculations of $[\alpha]_{D}$ are in good agreement with experiment: the average deviation is 19.8. The average deviation for HF $[\alpha]_{D}$ values is 32.2. The inclusion of electron correlation in calculating $[\alpha]_{D}$ is thus clearly of importance. CCSD/COM calculations are more accurate than CC2/COM calculations, for which the average deviation is 24.7. One may expect further improvement using CC methods more accurate than CCSD. The CCSD/COM calculations are comparable in accuracy to B3LYP calculations, for which the average deviation is 19.4.

For molecule 14, $[\alpha]_{D}$ is much larger (1146). HF and B3LYP $[\alpha]_{D}$ values are 607 and 1216, in very poor and good agreement with experiment, respectively. CCSD/COM gives $[\alpha]_{D}=741$, not much larger than the HF value and also in poor agreement with experiment. The CC2/COM $[\alpha]_{D}$ of 1000 is substantially different from, and in better agreement with experiment than, the CCSD/COM value. The contribution to $[\alpha]_{D}$ of the lowest $\mathrm{n} \rightarrow \pi^{*}$ excitation of 14, obtained by calculating its excitation frequency and rotational strength, parallels the behavior of the calculated $[\alpha]_{D}$. CCSD and B3LYP calculations give similar excitation energies but very different rotational strengths. CCSD and B3LYP rotational strengths are in poor and excellent agreement with the experimental value, respectively. Understanding the sources of the error in the CCSD rotational strength may simultaneously explain the error in the CCSD $[\alpha]_{D}$ value.

The CC methodology used in this work is not gauge-origin independent and calculated $[\alpha]_{D}$ values are origin dependent. In our calculations we have adopted a uniform choice of origin: the center of mass. Further studies of the origin

dependence of CC $[\alpha]_D$ values in these molecules are obviously of interest and will be pursued, as will the development of gauge-origin independent CC methodologies.

## Acknowledgements
KR is grateful to the Norwegian Research Council for a postdoctoral fellowship (Grant No. 12581/1410) and a grant of computer time from the Programme for Supercomputing. This work was also supported by NSF Grants CHE-9902832 and CHE-0209957 to PJS.

## References
[1] P.L. Polavarapu, Mol. Phys. 91 (1997) 551.
[2] P.L. Polavarapu, D.K. Chakraborty, J. Am. Chem. Soc. 120 (1998) 6160.
[3] P.L. Polavarapu, C. Zhao, Chem. Phys. Lett. 296 (1998) 105.
[4] R.K. Kondru, P. Wipf, D.N. Beratan, J. Am. Chem. Soc. 120 (1998) 2204.
[5] R.K. Kondru, P. Wipf, D.N. Beratan, Science 282 (1998) 2247.
[6] R.K. Kondru, P. Wipf, D.N. Beratan, J. Phys. Chem. A 103 (1999) 6603.
[7] J.R. Cheeseman, M.J. Frisch, F.J. Devlin, P.J. Stephens, J. Phys. Chem. A 104 (2000) 1039.
[8] P.J. Stephens, F.J. Devlin, J.R. Cheeseman, M.J. Frisch, B. Mennucci, J. Tomasi, Tetrahedron: Asymmetry 11 (2000) 2443.
[9] P.J. Stephens, F.J. Devlin, J.R. Cheeseman, M.J. Frisch, J. Phys. Chem. A 105 (2001) 5356.
[10] P.J. Stephens, F.J. Devlin, J.R. Cheeseman, M.J. Frisch, Chirality 14 (2001) 1.

[11] B. Mennucci, J. Tomasi, R. Cammi, J.R. Cheeseman, M.J. Frisch, F.J. Devlin, S. Gabriel, P.J. Stephens, J. Phys. Chem. A 106 (2002) 6102.
[12] P.J. Stephens, F.J. Devlin, J.R. Cheeseman, M.J. Frisch, C. Rosini, Org. Lett. 4 (2002) 4595.
[13] P.L. Polavarapu, D.K. Chakraborty, K. Ruud, Chem. Phys. Lett. 319 (2000) 595.
[14] K. Ruud, P.R. Taylor, P.-O. Åstrand, Chem. Phys. Lett. 337 (2001) 215.
[15] K. Ruud, T. Helgaker, Chem. Phys. Lett. 352 (2002) 533.
[16] S. Grimme, Chem. Phys. Lett. 339 (2001) 380.
[17] S. Grimme, F. Furche, R. Ahlrichs, Chem. Phys. Lett. 361 (2002) 321.
[18] J. Autschbach, S. Petchkovskii, T. Ziegler, S.J.A. van Gisbergen, E.J. Baerends, J. Chem. Phys. 117 (2002) 581.
[19] O. Christiansen, H. Koch, P. Jørgensen, T. Helgaker, A.S. de Merás, J. Chem. Phys. 105 (1996) 6921.
[20] O. Christiansen, A. Halkier, H. Koch, P. Jørgensen, T. Helgaker, J. Chem. Phys. 108 (1998) 2801.
[21] L. Rosenfeld, Z. Phys. 52 (1928) 161.
[22] E.U. Condon, Rev. Mod. Phys. 9 (1937) 432.
[23] H. Eyring, J. Walter, G.E. Kimball, Quantum Chemistry, Wiley, New York, 1944.
[24] T. Helgaker et al., DALTON, an ab initio electronic structure program, Release 1.2. See http://www.kjemi.uio.no/software/dalton/dalton.html, 2001.
[25] T.B. Pedersen, H. Koch, C. Hättig, J. Chem. Phys. 110 (1999) 8318.
[26] F. London, J. Phys. Radium 8 (1937) 397.
[27] T.H. Dunning Jr., J. Chem. Phys. 90 (1989) 1007.
[28] D.E. Woon, T.H. Dunning Jr., J. Chem. Phys. 100 (1994) 2975.
[29] GAUSSIAN, Development version, Gaussian Inc., Pittsburgh.
[30] H. Koch, O. Christiansen, P. Jørgensen, J. Olsen, Chem. Phys. Lett. 244 (1995) 75.
[31] D.A. Lightner, J.K. Gawronski, T.D. Bouman, J. Am. Chem. Soc. 102 (1980) 5749.
[32] D.A. Lightner, W.A. Beavers, J. Am. Chem. Soc. 93 (1971) 2677.
[33] A.E. Hansen, K.L. Bak, Enantiomer 4 (1999) 455.
[34] D.J. Sandman, K. Mislow, J. Org. Chem. 33 (1968) 2924.