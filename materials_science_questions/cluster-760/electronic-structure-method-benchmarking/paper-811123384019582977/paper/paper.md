Journal of Electron Spectroscopy and Related Phenomena, 27(1973) 475-481
© Elsevier Scientific Publishing Company, Amsterdam - Printed in The Netherlands

# A SEMI-EMPIRICAL METHOD FOR THE CALCULATION OF SPIN-ORBIT SPLITTING IN DEGENERATE ELECTRONIC STATES OF LINEAR POLY-ATOMIC MOLECULES

F. A. GRIMM

Department of Chemistry, University of Tennessee, Knoxville, Tenn. 37916 (U.S.A.)

(First received 3 May 1973; in final form 3 August 1973)

## ABSTRACT

A semiempirical method for the calculation of spin-orbit coupling constants in linear polyatomic molecules is discussed. The method uses the readily available output from a CNDO/2 calculation and a set of effective atomic coupling constants obtained from observed spectroscopic data on atoms. Two procedures for obtaining the spin-orbit splitting are discussed: one based on a closed shell CNDO/2 calculation and one based on an open shell calculation.

The average error for the molecules studied was $6.8\%$ and $7.7\%$ for the two procedures used in the calculations, the easier closed shell procedure giving the lower percentage error. It should be noted that the largest errors occurred in the case of diatomic molecules where the error would be expected to be the greatest. Thus, the average error involved in the values of the spin-orbit splitting for polyatomic molecules is much less than $3.7\%$ for the closed shell procedure. The method used appears to be extendable to non-linear molecules in which the only atoms off the principle symmetry axis of the molecules are hydrogen. The method should be useful in the interpretation of photoelectron spectra.

## INTRODUCTION

In the analysis of photoelectron spectra use has been made of both the vibrational fine structure observed on some bands in the spectrum and, when ob- served, the spin-orbit splitting of degenerate electronic states. Values for the vi- brational frequencies in the ions formed have not, in most cases, been available. The estimate of the vibrational frequencies in the ions formed in photoelectron spectros- copy has been very qualitative and in many cases an exact assignment to a particular mode has not been possible. The use of spin-orbit splitting for the analysis of spectra has not been subject to the same difficulties as in the use of vibrational frequencies.

Values for the splittings have in many cases been available from molecular spectros- copy (e.g. diatomic ions $Cl_{2}^{+} I_{2}^{+}$, etc.). In the case of spin-orbit splitting it also seems we are in a better position to obtain good estimates of the splitting for diatomic molecules based upon the results of molecular spectroscopy. Certainly the ability to obtain the spin-orbit splitting to within about $5 \%$ for molecules other than diatomics would be of considerable aid in making assignments in photoelectron spectroscopy.

This paper deals with the calculation of the spin-orbit coupling constant for linear polyatomic molecules which it appears will have the advantage of being capable of extension to certain non-linear molecules. The methods of calculations presented are an outgrowth of papers by Ishiguro and Kobori $^{1}$ , Leach $^{2}$ , Walker and Richards $^{3}$ . With the exception of the paper by Leach $^{2}$ , the other papers deal only with diatomic molecules. The methods presented in this paper follow the neglect of all integrals except the one-center integrals which parallels the work of Ishiguro and Kobori $^{1}$ . The extension of their method from diatomic to polyatomic molecules and the use of a semi-empirical wave function is an important departure from prior methods since it makes calculations on spin-orbit splitting more readily available to the experi- mentalist.

THE CALCULATION OF THE SPIN-ORBIT SPLITTING

The basis for the present method is contained in the article by Ishiguro and Kobori for diatomic molecules $^{1}$ . Thus, the reader will be referred to this article for their detailed discussion of the diatomic case and we will be concerned here only with the extension to polyatomic molecules and the mechanics of the method as used in these (our) calculations. The important assumption that is made is to ignore all integrals except the one-center integrals $^{1-3}$ . The justification for this has been discussed by Walker and Richards $^{3}$ for diatomic molecules and they found that in certain cases the neglect of the two-center integrals would result in poor agreement between the calculated and observed values. They also noted that for linear polyatomic molecules the neglect of the two-center terms should be justified. Thus, the worst results should be obtained in the case of diatomics.

Two slightly different procedures were used in the calculations and they will be referred to as Procedures I and II. Both procedures are based on CNDO/2 cal- culations $^{4}$ .

Procedure I

The major difference between I and II is that Procedure I uses the results of an open shell calculation on the degenerate electronic state. Let us write in the usual way the i-th molecular orbital
$$\psi_{\mathrm{i}}=\sum_{\mu} c_{\mathrm{i} \mu}^{\alpha} \phi_{\mu}$$
where the sum is over all atomic orbitals in the basis set. The $c_{i \mu}^{\alpha}$'s would then be the

eigenvector corresponding to the i-th molecular orbital (containing the "unpaired" electron) in the $\alpha$ matrix of an open shell CNDO/2 calculation. Let $P_{\mu v}$ be the charge density matrix defined by

$$
P_{\mu v}=\sum_{\mathrm{i}}^{\mathrm{occ} \alpha} c_{\mathrm{i} \mu}^{\alpha} c_{\mathrm{i} v}^{\alpha}+\sum_{\mathrm{i}}^{\mathrm{occ} \beta} c_{\mathrm{i} \mu}^{\beta} c_{\mathrm{i} v}^{\beta}
$$

where the sums are over the occupied orbitals in the $\alpha$ and $\beta$ matrices respectively. Then the total charge on atom A is given by

$$
P_{\mathrm{AA}}=\sum_{\mu}^{\mathrm{A}} P_{\mu \mu}
$$

where the sum is over all atomic orbitals on atom A. The net charge on atom A $(Q_{\mathrm{A}})$ is obtained from

$$
Q_{\mathrm{A}}=Z_{\mathrm{A}}-P_{\mathrm{AA}}
$$

where $Z_{\mathrm{A}}$ would be the charge on the atom minus the number of core electrons since in the CNDO/2 calculation used only the valence electrons were considered.

Let $\xi_{\mathrm{A}}$ be the effective atomic coupling constant for the neutral atom A and $\xi_{\mathrm{A}}^{+}$be the effective atomic coupling for the cation. The effective atomic coupling constants are calculated from the experimentally observed atomic splittings. The values for $\xi_{\mathrm{A}}$ and $\xi_{\mathrm{A}}^{+}$, can be found in the paper by Ishiguro and Kubori $^{5}$. Their table of values does not include $\mathrm{Be}^{+}\left(1 \mathrm{~s}^{2} 2 \mathrm{~s}\right), \mathrm{I}\left(\mathrm{p}^{5}\right)$ or $\mathrm{I}^{+}\left(\mathrm{p}^{4}\right)$ and these have been calculated and appear in Table 1 (see footnote) along with the values for the other elements used in the calculations presented.

We now assume that we can define an effective molecular orbital coupling constant for the i-th orbital $\left(\zeta_{\mathrm{i}}\right)$ by the equation

$$
\zeta_{\mathrm{i}}=\sum_{\mathrm{A}} \sum_{\mu}^{\mathrm{A}}\left(c_{\mathrm{i} \mu}^{\mathrm{A}}\right)^{2}\left[\left|Q_{\mathrm{A}}\right| \xi_{\mathrm{A}}^{+}+\left(1-\left|Q_{\mathrm{A}}\right|\right) \xi_{\mathrm{A}}\right]. \tag{1}
$$

This equation would give the results obtained by Ishiguro and Kobori for homo- nuclear diatomic molecules when they used the expression $\left[\xi_{\mathrm{n}, 1}(\mathrm{X})+\xi_{\mathrm{n}, 1}\left(\mathrm{X}^{+}\right)\right] / 2$. Equation (1) has, also, been obtained by Leach $^{2}$ and the reader will be referred to his paper for a more detailed discussion of its "derivation". The relation between the effective molecular coupling constant and the spectroscopic coupling constant $(A)$ calculated from the observed spin-orbit splitting $(\Delta v)$ are easily obtained $^{1,2,6}$. For $^{2} \pi$ states $A=\Delta v= \pm \zeta$ where the plus sign is for regular $(^{2} \pi_{3 / 2}$ below $^{2} \pi_{1 / 2})$ and the minus sign for inverted $(^{2} \pi_{1 / 2}$ below $^{2} \pi_{3 / 2})$ states.

Thus, for $^{2} \pi$ states of linear polyatomic molecules we obtain the value for the spin-orbit splitting in wave numbers directly from eqn. (1), since the effective atomic coupling constants are given in Table 1 in wave numbers.

### Procedure II
This procedure assumes that the removal of an electron from the i-th molecular

<table>
<caption>TABLE 1
VALUES OF THE EFFECTIVE ATOMIC COUPLING CONSTANT ($\xi$) FOR THE NEUTRAL ATOM AND THE SINGULARLY CHARGED CATION

Values are in $\text{cm}^{-1}$.</caption>
<thead>
  <tr>
    <th>$A$</th>
    <th>$\xi_{\text{A}}$</th>
    <th>$\xi_{\text{A}^{+}}$</th>
    <th>$A$</th>
    <th>$\xi_{\text{A}}$</th>
    <th>$\xi_{\text{A}^{+}}$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Be</td>
    <td>2.02</td>
    <td>3.0ª</td>
    <td>Al</td>
    <td>74.7</td>
    <td>124.9</td>
  </tr>
  <tr>
    <td>B</td>
    <td>10.7</td>
    <td>15.2</td>
    <td>Si</td>
    <td>148.9</td>
    <td>191.3</td>
  </tr>
  <tr>
    <td>C</td>
    <td>29</td>
    <td>42.7</td>
    <td>P</td>
    <td>275.2</td>
    <td>313.5</td>
  </tr>
  <tr>
    <td>N</td>
    <td>73.3</td>
    <td>87.5</td>
    <td>S</td>
    <td>382.4</td>
    <td>482.8</td>
  </tr>
  <tr>
    <td>O</td>
    <td>151</td>
    <td>168.9</td>
    <td>Cl</td>
    <td>587.3</td>
    <td>664.0</td>
  </tr>
  <tr>
    <td>F</td>
    <td>269.3</td>
    <td>327.1</td>
    <td>Br</td>
    <td>2456.7</td>
    <td>2560</td>
  </tr>
  <tr>
    <td>Mg</td>
    <td>40.5</td>
    <td>61.0</td>
    <td>I</td>
    <td>5068.8</td>
    <td>5152.7ᵇ</td>
  </tr>
</tbody>
</table>

ª Obtained from the results for boron and carbon that $\xi_{\text{A}^{+}} \simeq \frac{3}{2}\xi_{\text{A}}$.
ᵇ From the tables on Atomic Energy Levels, Vol. III, C. E. Moore, NBS Circular 467 (1949) using the method of Ishiguro and Kobori¹.

orbital in no way effects the electron distribution of the remaining electrons and the reduction in the electron density can be obtained from the square of the coefficients ($c_{i\mu}^{2}$). Thus, the total electron charge on atom A ($Q_{\text{A}}'$) after removal of an electron from the i-th molecular orbital is obtained from the equation

$$
Q_{\text{A}}' = Q_{\text{A}} - \sum_{\mu}^{\text{A}} (c_{i\mu}^{\text{A}})^2
$$

where $Q_{\text{A}}$ is the charge on atom A before the removal of the electron from the i-th molecular orbital. The calculation then proceeds as in eqn. (1) replacing $Q_{\text{A}}$ by $Q_{\text{A}}'$.
Note: $P_{\mu\nu}$ can now be obtained from the simpler expression

$$
P_{\mu\nu} = 2 \sum_{\text{i}}^{\text{occ}} c_{i\mu}c_{i\nu}.
$$

Using the results of closed shell calculations this procedure has the advantage of giving results on all the excited states of a positively charged ion in the photoelectron spectrum from a single CNDO/2 calculation.

# RESULTS AND DISCUSSION

The results of the calculations on a collection of diatomics and linear poly-atomic molecules are presented in Table 2. When available the experimental bond lengths were used in the CNDO/2 calculations to obtain the wave functions and electron densities. For those negative ions where no experimental lengths were avail-able the bond lengths for the neutral species were used. In the case of the interhalides $\text{BrCl}^{+}$, $\text{IBr}^{+}$ and $\text{ICl}^{+}$ the spin-orbit splitting was calculated using the wave functions and electron densities of ClF and the appropriate effective atomic coupling constants. The results are very good suggesting that one might use calculations on first and

second row elements to obtain an entire series of molecules [e.g. from calculations on FCN and ClCN one could also obtain BrCN and ICN using the wave function and electron densities from ClCN].

Since the experimental bond lengths are not the same as the bond lengths that would give the minimum energy in the CNDO calculations it was felt that an in- dication of the effect of bond length should be included. For example, in the case of CO₂ the difference in the calculation between the experimental bond length and the calculated equilibrium bond length is less than 0.1 cm⁻¹ in both the open shell case and the closed shell case. It was found that in general small changes in the bond lengths had little effect on the calculated coupling constants, since the electron den- sities changed very little with bond lengths. Thus, in a case where the electron density was very sensitive to the bond length one would expect to observe differences in the calculated spin-orbit coupling constant.

One of the more interesting observations is that the closed shell calculations

<table>
<caption>TABLE 2 CALCULATED AND OBSERVED SPIN-ORBIT SPLITTINGS (cm⁻¹)</caption>
<thead>
<tr>
<th>Molecule</th>
<th>State</th>
<th>Procedure I</th>
<th>Procedure II</th>
<th>Experimentalª</th>
</tr>
</thead>
<tbody>
<tr>
<th colspan="5">Diatomics</th>
</tr>
<tr>
<td>BeH</td>
<td>A²π</td>
<td>—</td>
<td>2.13</td>
<td>2.14</td>
</tr>
<tr>
<td>BH⁺</td>
<td>A²π</td>
<td>—</td>
<td>14.0</td>
<td>14.0</td>
</tr>
<tr>
<td>BO</td>
<td>A²π</td>
<td>—</td>
<td>119.6</td>
<td>122.4</td>
</tr>
<tr>
<td>CH</td>
<td>X²π</td>
<td>28.8</td>
<td>31.4</td>
<td>28.</td>
</tr>
<tr>
<td>CN</td>
<td></td>
<td>—</td>
<td>53.9</td>
<td>52.2</td>
</tr>
<tr>
<td>CO⁺</td>
<td>A²π</td>
<td>—</td>
<td>124.5</td>
<td>117.5</td>
</tr>
<tr>
<td>CF</td>
<td>X²π</td>
<td>66.4</td>
<td>56.5</td>
<td>77.1</td>
</tr>
<tr>
<td>NO</td>
<td>X²π</td>
<td>102.5</td>
<td>100.0</td>
<td>122.1</td>
</tr>
<tr>
<td>OH</td>
<td>X²π</td>
<td>126.2</td>
<td>154.1</td>
<td>140</td>
</tr>
<tr>
<td>HF⁺</td>
<td>X²π</td>
<td>295.5</td>
<td>313.7</td>
<td>240±20</td>
</tr>
<tr>
<td>F₂⁺</td>
<td>X²π</td>
<td>298.2</td>
<td>298.2</td>
<td>337±40</td>
</tr>
<tr>
<td>Cl₂⁺</td>
<td>X²π</td>
<td>625.7</td>
<td>625.7</td>
<td>645±40</td>
</tr>
<tr>
<td>Br₂⁺</td>
<td>X²π</td>
<td>2508</td>
<td>2508</td>
<td>2904</td>
</tr>
<tr>
<td>I₂⁺</td>
<td>X²π</td>
<td>5111</td>
<td>5111</td>
<td>5162</td>
</tr>
<tr>
<td>ClF⁺</td>
<td>X²π</td>
<td>600.0</td>
<td>619.0</td>
<td>637±30</td>
</tr>
<tr>
<td>BrCl⁺</td>
<td>X²π</td>
<td>—</td>
<td>2364</td>
<td>—</td>
</tr>
<tr>
<td>ICl⁺</td>
<td>X²π</td>
<td>—</td>
<td>4700</td>
<td>4678±40</td>
</tr>
<tr>
<td>IBr⁺</td>
<td>X²π</td>
<td>—</td>
<td>4859.4</td>
<td>4678±40</td>
</tr>
<tr>
<th colspan="5">Polyatomics</th>
</tr>
<tr>
<td>CNC</td>
<td>X²πg</td>
<td>27.6</td>
<td>26.7</td>
<td>26.4</td>
</tr>
<tr>
<td>NCO</td>
<td>X²π</td>
<td>83.2</td>
<td>84.1</td>
<td>95.6</td>
</tr>
<tr>
<td>CO₂⁺</td>
<td>X²π</td>
<td>154.2</td>
<td>155.2</td>
<td>159.5</td>
</tr>
<tr>
<td>CS₂⁺</td>
<td>X²π</td>
<td>—</td>
<td>431.9</td>
<td>440.</td>
</tr>
<tr>
<td>C₄H₂⁺</td>
<td>X²πg</td>
<td>30.9</td>
<td>32.1</td>
<td>33.3</td>
</tr>
<tr>
<td>C₄H₂⁺</td>
<td>²πu</td>
<td>—</td>
<td>31.5</td>
<td>30.6</td>
</tr>
</tbody>
</table>

ª These values were taken from refs. 1, 8, 11, and 12.

[Procedure II] give better results than those obtained by the wave function obtained from the open shell calculations [Procedure I]. The average percent error for all the molecules in Table 1 containing only first and second row elements is $7.7\%$ for the open shell and $6.8\%$ for the closed shell calculations. As expected the results are better for the polyatomic molecules. The error excluding the diatomic molecules is $5.9\%$ for the open shell and $3.7\%$ for the closed shell. For Procedure II this gives an error of less than $5\%$ for all polyatomic molecules except for NCO where it is noted that the negative ion is used in the calculations. One might in general observe that for cases requiring the use of negative ions in the closed shell calculation (e.g. OH, CF) the error is large and is larger than in the open shell calculation implying the possibility that the assumption of no change in the electron density for all electrons when one is removed is very poor when applied to negatively charged species.

Since the atomic coupling constants are treated as parameters in the method it is possible that a more empirical set of constants could be found that would im- prove upon the results. Since this would require "fitting" certain selected molecules for all elements it was decided that the present straight forward means of extending these results to elements not included in Table 2 should be kept. Therefore, no attempt was made to improve on these results by adjustment of the effective atomic coupling constants.

Because the coupling constant for hydrogen is taken to be zero, and obvious extension of the method to non-linear molecules in which only hydrogen is off axis presents itself. The possibility of using the methods presented to molecules like $\mathrm{H}_{3} \mathrm{CCl}, \mathrm{H}_{2} \mathrm{CCH}_{2}, \mathrm{H}_{2} \mathrm{CCO}$, etc. is presently being investigated. Results on the series $\mathrm{CH}_{3} \mathrm{~F}, \mathrm{CH}_{3} \mathrm{Cl}, \mathrm{CH}_{3} \mathrm{Br}, \mathrm{CH}_{3} \mathrm{I}$ indicate errors of less than $11\%$. The largest error being for the bromide $(10.5\%)$. One difficulty in using the percent error to show the ability of the method to reproduce the experimental results can be seen from the results on $\mathrm{CH}_{3} \mathrm{Br}$. The calculated value from the closed shell Procedure II is $4637.3\ \mathrm{cm}^{-1}$. In the literature one finds the following values reported for the spin-orbit splitting $4700^{7}, 5060^{8}, 4596^{9}$, and $5050^{10}\ \mathrm{cm}^{-1}$. Since the calculated values for molecules containing bromide have tended to be too low we have chosen to use the value by Ragle et al. $^{10}$ which gives an error of $10.5\%$. Thus, the calculated values are certainly within the limits of the experimental results.

REFERENCES

1 E. Ishiguro and M. Kobori, *J. Phys. Soc. Jap.*, 22 (1967) 263.
2 S. Leach, *Acta Phys. Pol.*, XXXIV (1968) 705.
3 T. Walker and W. Richards, *J. Chem. Phys.*, 52 (1970) 1311. See also *Phys. Rev.*, 177 (1969) 100.
4 J. Pople and D. Beveridge, *Approximate Molecular Orbital Theory*, McGraw-Hill, New York, 1970.
5 Reference 1, page 266, Table I [Note: Ishiguro and Kobori use the symbol $\xi_{\mathrm{n}, 1}$ so that $\xi_{\mathrm{A}}=\xi_{\mathrm{n}, 1}(\mathrm{~A})$ and $\xi_{\mathrm{A}^{+}}=\xi_{\mathrm{n}, 1}\left(\mathrm{~A}^{+}\right)$e.g. $\xi_{\mathrm{C}}=29\ \mathrm{~cm}^{-1}, \xi_{\mathrm{C}^{+}}=42.7\ \mathrm{~cm}^{-1}$.]
6 R. Mulliken, *Rev. Mol. Phys.*, 4 (1932) 1.
7 V. Cermak, *Collect. Czech. Chem. Commun.*, 33 (1968) 2739.

8 G. Herzberg, *Electron Spectra of Polyatomic Molecules*, Van Nostrand, New York, 1966, Table 69.

9 A. Nicholson, *J. Chem. Phys.*, 43 (1965) 1171.

10 J. Ragle, I. Stenhouse, D. Frost and C. McDowell, *J. Chem. Phys.*, 53 (1970) 178.

11 G. Herzberg, *Spectra of Diatomic Molecules*, Van Nostrand, New York, 1950.

12 S. Evans and A. F. Orchard, *Inorg. Chim. Acta*, 5 (1971) 81.