# Polynomial approximation to universal M-shell ionisation cross-sections induced by $H^{+}$ and $He^{2+}$ ions

A. Taborda, $^{a,b*}$ P. C. Chaves, $^{a,b}$ M. L. Carvalho and M. A. Reis$^{a,b}$

The calculation of ionisation cross-sections induced by $H^{+}$ and $He^{2+}$ ions in efficient ways for inclusion in simulation programmes to determine the X-ray intensities is still extremely useful, in spite of the significant computer power available nowadays. Particle-induced X-ray emission studies have been mostly carried out using K-shell and L-shell X-ray emission. However, the new microcalorimeter detection systems available will make M-shell and higher shell X-ray emission data increasingly important. Quantification and simulation of X-ray intensities require one to be able to compute the ionisation cross-sections, which can be carried out using the ECPSSR theory. Nevertheless, this is not an efficient process, and therefore, in previous work, K and L-shells universal ionisation cross-section curves were found as well as polynomial approximations to the universal curves. In this work, polynomial approximations to the M-shell universal ionisation cross-sections are presented, and calculated ionisation and X-ray production cross-sections based on the polynomial approximations are compared with results from literature. These polynomial approximations were included in the X-ray intensities simulation programme DT2simul, based on LibCPIXE, and the results obtained are compared with experimental data for several elements and compound samples. Copyright © 2013 John Wiley & Sons, Ltd.

## Introduction

Until recently, in particle-induced X-ray emission, the K-shell and L-shell X-ray emission lines were usually the first choice to carry out the study of the X-ray emission spectrum. With the new technological developments regarding X-ray detection systems, in particular the X-ray microcalorimeter spectrometers, the M-shell (and even N-shell) X-ray spectra are becoming increasingly important.

The elemental quantification work and the simulation of X-ray intensities demand the knowledge of the X-ray production cross-sections and the ability to compute them. The calculation of X-ray production cross-sections can be carried out using the ECPSSR theory, developed by Brandt and Lapicki$^{[1]}$ and recently reviewed by the authors.$^{[2]}$ However, computing the X-ray production cross-sections can be a time-consuming process because of the integration of form factor functions, and in spite of the computer power already available, more efficient methods are needed to allow for the simulation of X-ray intensities induced by charged particles in various analytical problems. A method commonly used for this purpose$^{[3,4]}$ is the interpolation of the M-shell ionisation cross-sections calculated by Chen and Crasemann,$^{[5]}$ but the values are limited to an energy range of 0.06 to 2.0 MeV, something not welcome in simulation programmes, such as DT2simul.

DT2simul, a computer code developed by the authors based on LibCPIXE,$^{[6,7]}$ an open source library for particle-induced X-ray emission simulation, allows for the simulation of X-ray intensities for fully multilayered samples. LibCPIXE has been used in bayesian analysis software codes such as the DataFurnace,$^{[8,9]}$ aiming at the handling of multilayered samples ion beam analysis data, which means that time efficient calculation methods are crucial. LibCPIXE, and therefore DT2simul, do not include interpolation methods to calculate the K-shell and L-shell ionisation cross-sections. Instead, these are computed using polynomial approximations to a universal ionisation cross-section function.$^{[2]}$

The time efficient K and L X-ray intensities simulation makes DT2simul a useful tool to both fundamental studies and to applications work. The growing importance of M-shell X-ray based quantification now requires the ability to also simulate M X-ray intensities.

In this work, following the approach used for the K-shell and L-shell ionisation cross-sections, a time effective method to calculate the M-shell ionisation cross-sections is presented and tentatively validated by comparison with experimental data.

## Universal ionisation cross-sections

The X-ray production cross-section corresponding to an L–S coupling scheme electron transition $t$, in Siegbahn notation (e.g.: $\alpha_{1}$, $\beta_{1}$, $\gamma_{2},...$), or from sub-shell $t$, in IUPAC notation (e.g.: $M_{5}$, $M_{4}$, $N_{2},...$), to sub-shell $o=1,2,3,...$ of the $n=K,L,M,...$ shell, $X_{n,o,t}$, can be written as

---

* Correspondence to: IST/ITN, Instituto Superior Técnico, Universidade Técnica de Lisboa, Campus Tecnológico e Nuclear, EN10, 2686-953 Sacavém, Portugal.
Email: ataborda@itn.pt

a IST/ITN, Instituto Superior Técnico, Universidade Técnica de Lisboa, Campus Tecnológico e Nuclear, EN10, 2686-953 Sacavém, Portugal

b Centro de Física Atómica da Universidade de Lisboa, Av. Prof. Gama Pinto 2, 1649-003 Lisboa, Portugal

---

X-Ray Spectrom. **2013**, 42, 177–182

Copyright © 2013 John Wiley & Sons, Ltd.

$$
\sigma_{n, o, t}^{X}=k_{n, o, t} \omega_{n, o} V_{n, o} \tag{1}
$$

where $k_{n, o, t}$ are the sub-shell relative emission rates, $\omega_{n, o}$ the sub-shell fluorescence yields and $V_{n, o}$ are the final vacancy distributions, defined by Bambynek et al. in $1972 .^{[10]}$ For the M-shell, the final vacancy distributions are given by

$$
\begin{aligned}
V_{M, 1}= & \sigma_{M, 1}, \\
V_{M, 2}= & \sigma_{M, 2}+f_{M, 1,2} \sigma_{M, 1} \\
V_{M, 3}= & \sigma_{M, 3}+f_{M, 2,3} \sigma_{M, 2}+\left(f_{M, 1,2} f_{M, 2,3}+f_{M, 1,3}\right) \sigma_{M, 1} \\
V_{M, 4}= & \sigma_{M, 4}+f_{M, 3,4} \sigma_{M, 3}+\left(f_{M, 2,3} f_{M, 3,4}+f_{M, 2,4}\right) \sigma_{M, 2}+ \\
& +\left(f_{M, 1,2} f_{M, 2,3} f_{M, 3,4}+f_{M, 1,2} f_{M, 2,4}+f_{M, 1,3} f_{M, 3,4}+f_{M, 1,4}\right) \sigma_{M, 1} \\
V_{M, 5}= & \sigma_{M, 5}+f_{M, 4,5} \sigma_{M, 4}+\left(f_{M, 3,4} f_{M, 4,5}+f_{M, 3,5}\right) \sigma_{M, 3}+ \\
& +\left(f_{M, 2,3} f_{M, 3,4} f_{M, 4,5}+f_{M, 2,3} f_{M, 3,5}+f_{M, 2,4} f_{M, 4,5}+f_{M, 2,5}\right) \sigma_{M, 2}+ \\
& +\left(f_{M, 1,2} f_{M, 2,3} f_{M, 3,4} f_{M, 4,5}+f_{M, 1,2} f_{M, 2,3} f_{M, 3,5}+f_{M, 1,2} f_{M, 2,4} f_{M, 4,5}\right) \sigma_{M, 1}+ \\
& +\left(f_{M, 1,3} f_{M, 3,4} f_{M, 4,5}+f_{M, 1,3} f_{M, 3,5}+f_{M, 1,4} f_{M, 4,5}+f_{M, 1,5}\right) \sigma_{M, 1}
\end{aligned} \tag{2}
$$

$f_{M, o_{1}, o_{2}}$ being the Coster-Kronig coefficients and $\sigma_{M, o}$ the ionisation cross-section for each of the $o=1,2,3,4,5$ sub-shells of the M-shell.

Following previous work for the K and L-shells $^{[2]}$ and plotting its natural logarithm against a relativistic reduced velocity, rescaled by a power of the screening parameter, $\theta_{n, o}$, one can establish a universal ionisation cross-sections function, defined as

$$
\sigma_{n, o}^{U}\left(\xi_{n, o}^{R}, \zeta_{n, o}, \theta_{n, o}\right)=\frac{\sigma_{n, o}^{\mathrm{ECPSSR}}\left(\xi_{n, o}^{R}, \zeta_{n, o}, \theta_{n, o}\right)}{8 \pi a_{0}^{2} Z_{\text {proj }}^{2} C_{n, o}\left(x_{q}\right)} \eta_{n, o} Z_{n, o}^{2} \theta_{n, o}^{1+c_{n, o}^{U}} \tag{3}
$$

where $a_{0}$ is the Bohr radius, $Z_{\text {proj }}$ is the projectile atomic number and $Z_{n, o}=Z_{\text {target }}-S h_{n, o}$ is the target effective atomic number in the Slater's shielding approximation, $^{[10]} \theta_{n, o}$ the reduced binding energy (or screening parameter) and $\eta_{n, o}$ is the reduced incident ion energy, as defined in detail by Taborda et al. $^{[2]}$ For the $M_{1}, M_{2}$ and $M_{3}$ sub-shells $S h_{M, o}=11.25$, and for the $M_{4}$ and $M_{5}$ sub-shells, $S h_{M, o}=21.15$.

As noted previously, $^{[2]}$ by means of this universal ionisation cross-section, the ECPSSR standard weighting of the particles Coulomb field by the targets Coulomb field is replaced by an extra weight of the screening parameter, $\theta_{n, o} . C_{n, o}(x_{q})$ in Eqn (3) being the Coulomb deflection correction for the incident particle, with binding and energy loss corrections. This term is one of the most important in ECPSSR theory as it is due to it that the plane-wave Born approximation (PWBA) cross-section values, calculated by a Perturbed Stationary States method, are made to come close to experimental values. $^{[11]}$ The Coulomb deflection correction, such as introduced by Brandt and Lapicki, $^{[11]}$ is essentially a semi empirical correction, which, as pointed out by Brandt and Lapicki, may in fact not be valid for higher beam energies. It is important to note here that this term is not present in the universal ionisation cross-section curve, as a direct consequence of the definition [Eqn (3)]. This means that any approximations made to the universal ionisation cross-sections will also not depend on experimental values, making the present calculations robust. $^{[2]}$

The $\sigma_{n, o}^{\text {ECPSSR }}$ term represents the ionisation cross-sections calculated using the ECPSSR theory, $^{[11,12]}$ which can be expressed as

$$
\sigma_{n, o}^{\mathrm{ECPSSR}}\left(\xi_{n, o}^{R}, \zeta_{n, o}, \theta_{n, o}\right)=C_{n, o}\left(x_{q}\right) \sigma_{n, o}^{\mathrm{PWBA}}\left(\frac{\xi_{n, o}^{R}}{\zeta_{n, o}}, \zeta_{n, o} \theta_{n, o}\right) \tag{4}
$$

where $\sigma_{n, o}^{\text {PWBA }}$ is the ionisation cross-section in the PWBA. In this work, the PWBA cross-sections were evaluated as that by Taborda et al., $^{[2]}$ directly from the form factors using the form factor polynomial functions from Choi $^{[13]}$ and using exact integration limits; therefore, the function to correct for the finite values of the maximum momentum transfer, introduced by Brandt and Lapicki, $^{[1]}$ is omitted, as recommended by Cohen and Harrigan. $^{[14]}$ The numerical integration was carried out using Lobatto's rule with ten points $^{[15]}$ for each subinterval. The total integration intervals were subdivided into smaller intervals of size $h$ defined by

$$
\ln h=\frac{\ln b / a}{N} \tag{5}
$$

where $N$ is the number of small intervals, and $a$ and $b$ the lower and upper integration limits. For incident particle energy values lower than 2.6 MeV, $N$ was set as 100, and for energy values above or equal to $2.6 \mathrm{MeV}, N$ was set as 400 to ensure that the variation in the final value of the calculated cross-sections was less than $1 \%$.

## Polynomial approximation to the universal ionisation cross-sections

The universal M-shell ionisation cross-sections $\sigma_{M, o}^{U}$ were calculated using Eqn (3), with $c_{M, o}^{U}=0$, and previous expressions, implemented in an adapted version of the computer code used by Reis to produce the 1996 tables of semi-empirical ionisation cross-sections. $^{[16]}$

The calculations were performed for elements with atomic number from $Z_{\text {target }}=62$ to $Z_{\text {target }}=92$ and for 70 beam energy values in the range of $100 \mathrm{keV}$ to $10.0 \mathrm{MeV}$, for incident $\mathrm{H}^{+}$ $\left(Z_{\text {proj }}=1\right)$ and $\mathrm{He}^{2+}\left(Z_{\text {proj }}=2\right)$ ions.

The universal ionisation cross-section curves were then obtained by fitting seventh-order polynomial functions, $P_{M, o}(x_{M, o})$, as

$$
P_{M, o}\left(x_{M, o}\right)=-\ln \left(\sigma_{M, o}^{U} \theta_{M, o}^{c_{M, o}^{U}}\right) \quad \Leftrightarrow \quad \sigma_{M, o}^{U}=\frac{e^{-P_{M, o}\left(x_{M, o}\right)}}{\theta_{M, o}^{c_{M, o}^{U}}} \tag{6}
$$

where

$$
x_{M, o}=\left(\frac{1}{\xi_{M, o}^{R} \theta_{M, o}^{b_{M, o}^{U}}}\right)^{\frac{1}{2}} \tag{7}
$$

and fine tuning both $b_{M, o}^{U}$ and $c_{M, o}^{U}$ until a minimum widespread was reached. Final $b_{M, o}^{U}$ and $c_{M, o}^{U}$ values obtained are presented in Table 1.

<table>
<caption>Table 1. $b_{M, o}^{U}$ and $c_{M, o}^{U}$ constants for the $o=1,2,3,4,5$ sub-shell of the M-shell used in the polynomial approximation</caption>
<thead>
<tr>
<th>$n,o$</th>
<th>M,1</th>
<th>M,2</th>
<th>M,3</th>
<th>M,4</th>
<th>M,5</th>
</tr>
</thead>
<tbody>
<tr>
<td>$b_{M,o}^{U}$</td>
<td>0.2</td>
<td>0.2</td>
<td>0.32</td>
<td>0.4</td>
<td>0.4</td>
</tr>
<tr>
<td>$c_{M,o}^{U}$</td>
<td>2.0</td>
<td>2.0</td>
<td>4.0</td>
<td>8.0</td>
<td>9.0</td>
</tr>
</tbody>
</table>

Universal M-shell ionisation cross-sections

![](./images/813228748726861825_1.jpg)

Figure 1. Rescaled M-shell universal ionisation cross-sections displayed versus the rescaled reduced ion velocity for elements with atomic number from $Z_{\text{target}} = 62$ to $Z_{\text{target}} = 92$, for $\text{H}^{+}$ and $\text{He}^{2+}$ ions, and for 70 beam energy values in the range of 100 keV to 10.0 MeV. Relative residuals of the polynomial fittings to these universal curves are presented in the insets.

The universal curves are presented in Fig. 1. The residues of the fittings of the seventh-order polynomials are presented in the insets. Unlike the K-shell and L-shell universal curves cases, in the case of the M-shell, the universal curves for $\text{H}^{+}$ and $\text{He}^{2+}$ ions are the same within each M sub-shell, allowing for a single polynomial function approximation. The polynomial coefficients for the $\text{M}_{1}$ and $\text{M}_{2}$ sub-shells are presented in Table 2, and those for the $\text{M}_{3}$, $\text{M}_{4}$ and $\text{M}_{5}$ sub-shells are presented in Table 3.

The approximated ECPSSR ionisation cross-sections can thus now be easily calculated as

$$
\sigma_{n, o}^{\text{ECPSSR}}=8 \pi a_{0}^{2} Z_{\text{proj}}^{2} C_{n, o}\left(x_{q}\right) \frac{1}{\eta_{n, o} \theta_{n, o} Z_{n, o}^{2}} \sigma_{n, o}^{U} \tag{8}
$$

using the polynomial approximations to $\sigma_{n, o}^{U}$.

# Comparison with experimental M X-ray production cross-sections

The comparison between the calculated cross-sections and experimental M X-ray production cross-sections was made to test the polynomial approximations obtained. The M-shell X-ray production cross-sections were calculated using Eqn (1), where the fluorescence yields, $\omega_{M, o}$, and the Coster-Kronig yields, $f_{M, o_{1}, o_{2}}$, were taken from Chauhan and Puri$^{[17]}$ and the M lines relative emission rates, $k_{M, o, t}$, were taken from the compilation by Zschornack.$^{[18]}$ The M-shell X-ray production cross-section calculations were performed using the polynomial approximations and also using the form factors from Choi,$^{[13]}$ and both values were compared with experimental M-shell X-ray production cross-sections from literature.

Experimental M-shell X-ray production cross-sections data found in literature are mostly presented as the total M-shell X-ray production cross-sections.$^{[19-28]}$ Only a few references present experimental results for the $\text{M}_{\alpha}$, $\text{M}_{\beta}$ and $\text{M}_{\gamma}$ X-ray productions cross-sections determined for H and/or He ions impact,$^{[29-31]}$ which are the ones of interest for this comparison.

The $\text{M}_{\alpha}$, $\text{M}_{\beta}$ and $\text{M}_{\gamma}$ X-ray production cross-sections were calculated for $\text{H}^{+}$ and $\text{He}^{2+}$ ions with energies between 0.1 and 6.0 MeV impacting on Th ($Z_{\text{target}} = 90$) and U ($Z_{\text{target}} = 92$) targets. In Figs 2 and 3, the comparison between calculated and experimental $\text{M}_{\alpha}$, $\text{M}_{\beta}$ and $\text{M}_{\gamma}$ X-ray production cross-sections for $\text{H}^{+}$ and $\text{He}^{2+}$ ions impacting on Th and U are presented. The experimental M-shell X-ray production cross-sections for

<table>
<caption>Table 2. Coefficients for the polynomial approximations to universal ionisation cross-sections for the $\text{M}_{1}$ sub-shell, $P_{M, 1}(x_{M, 1})$, and for the $\text{M}_{2}$ sub-shell, $P_{M, 2}(x_{M, 2})$, for $\text{H}^{+}$ and $\text{He}^{2+}$ ion beams</caption>
<thead>
<tr>
<th rowspan="2">Coeff.</th>
<th>$P_{M1}$</th>
<th>$P_{M1}$</th>
<th>$P_{M2}$</th>
</tr>
<tr>
<th>$x_{M1} < 1.55$</th>
<th>$x_{M1} \geq 1.55$</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>$a_{0}$</td>
<td>273.2811152565</td>
<td>18960.7026915645</td>
<td>−19.3032617394</td>
</tr>
<tr>
<td>$a_{1}$</td>
<td>−2082.9030957469</td>
<td>−61901.8187537211</td>
<td>162.4889234855</td>
</tr>
<tr>
<td>$a_{2}$</td>
<td>6832.6238222042</td>
<td>85755.8327740529</td>
<td>−414.1290897664</td>
</tr>
<tr>
<td>$a_{3}$</td>
<td>−12125.3297104949</td>
<td>−65339.2989595359</td>
<td>561.7207849555</td>
</tr>
<tr>
<td>$a_{4}$</td>
<td>12547.0102221068</td>
<td>29591.5200404446</td>
<td>−417.3451966095</td>
</tr>
<tr>
<td>$a_{5}$</td>
<td>−7545.6495150664</td>
<td>−7970.7461695478</td>
<td>172.3296154360</td>
</tr>
<tr>
<td>$a_{6}$</td>
<td>2440.5793893631</td>
<td>1182.9960575510</td>
<td>−37.1283921263</td>
</tr>
<tr>
<td>$a_{7}$</td>
<td>−327.8696048707</td>
<td>−74.6673617955</td>
<td>3.2557924758</td>
</tr>
</tbody>
</table>


<table><caption>Table 3. Coefficients for the polynomial approximations to universal ionisation cross-sections for the M₃ sub-shell, $P_{M,3}(X_{M,3})$, for the M₄ sub-shell, $P_{M,4}(X_{M,4})$ and for the M₅ sub-shell, $P_{M,5}(X_{M,5})$, for H⁺ and He²⁺ ion beams</caption>
<thead>
<tr>
<th>Coeff.</th>
<th>$P_{M3}$</th>
<th>$P_{M4}$</th>
<th>$P_{M5}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$a_{0}$</td>
<td>−14.5226110476</td>
<td>22.8520799108</td>
<td>21.0251379002</td>
</tr>
<tr>
<td>$a_{1}$</td>
<td>135.8535328558</td>
<td>−77.9308005626</td>
<td>−63.2951932146</td>
</tr>
<tr>
<td>$a_{2}$</td>
<td>−331.6701884640</td>
<td>182.6729987502</td>
<td>148.1231462956</td>
</tr>
<tr>
<td>$a_{3}$</td>
<td>432.6175954277</td>
<td>−201.8905874954</td>
<td>−158.2779532376</td>
</tr>
<tr>
<td>$a_{4}$</td>
<td>−308.2058772968</td>
<td>125.5548133832</td>
<td>93.8561574567</td>
</tr>
<tr>
<td>$a_{5}$</td>
<td>121.8414099151</td>
<td>−43.9527679606</td>
<td>−30.7094667261</td>
</tr>
<tr>
<td>$a_{6}$</td>
<td>−25.1229785618</td>
<td>8.0710516244</td>
<td>5.1205995416</td>
</tr>
<tr>
<td>$a_{7}$</td>
<td>2.1093747715</td>
<td>−0.6038197960</td>
<td>−0.3325172832</td>
</tr>
</tbody>
</table>

Th and U, represented as black squares, were taken from Phinney et al. $^{[30]}$ The X-ray production cross-sections calculated using the form factors functions are represented as white squares, and the polynomial approximation to the universal ionisation cross-sections are represented as grey circles.

It can be seen that for Th and U, the calculated X-ray production cross-sections are in good agreement with experimental values in the case of $M_{\alpha}$ and $M_{\beta}$. The same does not hold true in the case of the $M_{\gamma}$ X-ray production cross-sections. A possible explanation for the differences observed is that the experimental $M_{\gamma}$ values presented by Phinney $^{[30]}$ correspond to the sum of the X-ray production cross-sections for the transitions $M_{3}-N_{4}$ (M$_{\gamma 2}$) and $M_{3}-N_{5}$ (M$_{\gamma 1}$) plus those for the transitions $M_{4}-O_{3}$ and $M_{5}-P_{3}$. On the other hand, the calculated $M_{\gamma}$ values do not include the $M_{4}-O_{3}$ and $M_{5}-P_{3}$ contributions, which should be, nevertheless, small contributions according to the atomic parameters present in literature. Furthermore, it is known that the theory behind the calculation of the M X-ray ionisation cross-sections falls short to reproduce the experimental data as pointed out by some authors $^{[26,32]}$ indicating that the theory needs to be improved, but the fact that the experimental cross-sections data can be misleading, as seen previously, should also be kept in mind.

M-shell X-ray production cross-section was also calculated for elements W ($Z_{target}=74$), Au ($Z_{target}=79$) and Pb ($Z_{target}=82$) and compared with experimental data from Rodriguez-Fernandez et al. $^{[31]}$ for the impact of H⁺ ions. Rodriguez-Fernandez experimental data are presented as the sum of $M_{\alpha 1,2}$ and $M_{\beta}$, meaning that for the comparison with the experimental values, the calculated $M_{\alpha 1,2}$ and $M_{\beta}$ were also summed, and are represented using the notation $M_{\alpha,\beta}$. This comparison is presented in Fig. 4 for the $M_{\alpha,\beta}$ and $M_{\gamma}$ X-ray production cross-sections, where the experimental data are represented by the black squares, the form factor calculated values by the white squares and the polynomial approximation-based calculated values by the grey squares.

As in the case of the elements Th and U, the calculated $M_{\alpha,\beta}$ X-ray production cross-sections in the energy range considered are in good agreement with the experimental data for W, Au and Pb, but the $M_{\gamma}$ experimental data are, again, not well reproduced by the calculated values, especially in the case of W.

In the three figures (Figs 2, 3 and 4), it is clear as well that the two theoretical curves, the one based on the form factor calculations (white squares) and the on the polynomial approximations (grey circles), reproduce differently the experimental data, not being clear if one is better than the other. This different behaviour between the two theoretical curves is not entirely surprising, because although the seventh-degree polynomial functions are fitted to calculations based on the form factor

![](./images/813228748726861825_2.jpg)

Figure 2. Comparison between experimental Th and U $M_{\alpha}$, $M_{\beta}$ and $M_{\gamma}$ X-ray production cross-sections (black squares) for the impact of H ions from Phinney et al. $^{[30]}$ and calculated X-ray production cross-sections using the form factors (white squares) and the polynomial approximation to the universal ionisation cross-sections (grey circles).

![](./images/813228748726861825_3.jpg)

Figure 3. Comparison between experimental Th and U $M_{\alpha}$, $M_{\beta}$ and $M_{\gamma}$ X-ray production cross-sections for the impact of He ions (black squares) from Phinney et al.$^{[30]}$ and calculated X-ray production cross-sections using the form factors (white squares) and the polynomial approximation to the universal ionisation cross-sections (grey circles).

functions, this fit is performed to the universal ionisation cross-sections, in which, as mentioned before, the weighting of the particles Coulomb field by the targets Coulomb field is replaced by an extra weight of the screening parameter, $\theta_{n,o}$.

![](./images/813228748726861825_4.jpg)

Figure 4. Comparison between experimental W, Au, Pb $M_{\alpha,\beta}$ and $M_{\gamma}$ X-ray production cross-sections (black squares) for the impact of H ions from Rodriguez-Fernandez et al.$^{[31]}$ and calculated X-ray production cross-sections using the form factors (white squares) and the polynomial approximation to the universal ionisation cross-sections (grey squares).

In any case, the polynomial approximations to the universal ionisation cross-sections obtained are shown to be accurate enough to be used in efficient calculation of M-shell ionisation cross-sections and M X-ray production cross-sections, and their use in X-ray intensities simulation programmes that need to calculate X-ray production cross-sections in an efficient way is clearly justified.

## Simulation of M X-ray intensities

As mentioned, the polynomial approximations to the universal ionisation cross-sections provide an efficient and expedited way to calculate the X-ray production cross-sections in X-ray intensities simulation programmes such as the DT2simul. DT2simul allows for the simulation of K-shell, L-shell and M-shell X-ray intensities induced by H and He ions and is based on LibCPIXE v2.08.$^{[6,7]}$ The K-shell and L-shell polynomial approximations to the universal ionisation cross-sections were implemented in DT2simul in previous work$^{[2]}$ allowing to successfully calculate X-ray production cross-sections and simulate K-shell and L-shell X-ray intensities induced by H and He ions. The seventh-order polynomial functions determined for the M-shell were now implemented, and DT2simul can now simulate M-shell X-ray intensities and what is expected to be observed in real samples particle-induced X-ray emission analysis.

In the scope of this work, the simulation of M-shell X-ray intensities for two thick samples composed of different uranium alloys, namely, $Pd_3U$ and $UO_2$, was carried out considering the impact of H$^+$ ions with energies between 0.5 and 4.0 MeV, the use of a Si(Li) semiconductor X-ray detector, an incidence angle of 22.5° and a detection angle of 47.5°.

In Fig. 5, the simulated uranium X-ray intensities ratio $M_{\beta}/M_{\alpha1,2}$ as a function of energy is presented for the two alloys. It is seen that the U $M_{\beta}/M_{\alpha1,2}$ ratio of the two alloys exhibit a different trend for low energies. The trend of the U $M_{\beta}/M_{\alpha1,2}$ ratio is promptly explained by the sample self absorption, because the U $M_{\alpha1,2}$ X-ray energy is 3.165 keV and the U $M_{\beta}$ X-ray energy is 3.337 keV,$^{[18]}$ leading to a greater absorption of

![](./images/813228748726861825_5.jpg)

Figure 5. Simulated uranium $M_{\beta}$ and $M_{\alpha 1,2}$ X-ray intensities ratio for two uranium alloys, $Pd_{3} U$ and $UO_{2}$. The simulated $M_{\beta} / M_{\alpha 1,2}$ ratio is displayed as a function of the $H^{+}$ ion beam energy.

the $M_{\alpha 1,2}$ X-rays in the sample comparing to the absorption of the $M_{\beta}$ X-rays, as the incident particle energy increases. On the other hand, the presence of the element Pd in the $Pd_{3} U$ alloy is the cause for the difference in trend between the two U alloys due to the Pd $L_{2}$ and Pd $L_{3}$ absorption edge energies. The Pd $L_{3}$ absorption edge energy is 3.173 keV, and the Pd $L_{2}$ absorption edge energy is 3.331 keV, $^{[18]}$ both situated between the U $M_{\alpha 1,2}$ (3.165 keV) and U $M_{\beta}$ (3.337 keV) X-ray energies. This means that the emitted U $M_{\beta}$ X-rays will be preferably and strongly absorbed by Pd translating in the decrease of the U $M_{\beta}$ X-ray intensities observed in Fig. 5. It is known that matrix effects have to be considered in the analysis of X-ray spectra, because not taking them into consideration can have dramatic consequences in the final results, $^{[33]}$ and here, DT2simul plays an important role by previewing what one is to expect in the analysis of X-ray spectra, allowing for more accurate spectra fits and elemental quantification.

## Conclusions

In this work, nearly universal M-shell ionisation cross-sections curves for incident $H^{+}$ and $He^{2+}$ ions were obtained, and, as was observed in previous work for the K and L-shells, $^{[2]}$ the universal behaviour of the ionisation cross-section has a strong dependence on the screening parameter, $\theta_{n, o}$. For the M-shell, the universal ionisation cross-sections curves are the same for incident $H^{+}$ and $He^{2+}$ ions, which was not the case for the K and L-shells, and a single seventh-order polynomial function could be fitted to each universal M sub-shell ionisation cross-sections curves to describe both cases, $H^{+}$ and $He^{2+}$ ions.

Comparing to the experimental K-shell and L-shell cross- sections data, experimental M-shell X-ray production cross- sections data are limited, and, when available, it is presented mostly as the total M-shell X-ray production cross-section and the need for more experimental data is clear. Nevertheless, the comparison to available experimental M X-ray production cross- sections data shows that the polynomial approximations to the rescaled universal ionisation cross-sections are reliable and can be used to calculate ionisation and X-ray production cross- sections, as well as to simulate X-ray intensities induced by
$H^{+}$ and $He^{2+}$ ions in X-ray intensities simulation programmes such as the DT2simul, which need efficient ways to perform the calculations.

## Acknowledgements

This work was partially supported by the Portuguese Foundation for Science and Technology, FCT, fellowships SFRH/BD/43379/2008 and SFRH/BPD/76733/2011.

## References

[1] W. Brandt, G. Lapicki. *Physical Review A* **1981**, 23, 1717.
[2] A. Taborda, P. C. Chaves, M. A. Reis. *X-ray Spectrometry* **2011**, 40, 127.
[3] J. L. Campbell, N. I. Boyd, N. Grassi, P. Bonnick, J. A. Maxwell. *Nucl. Instrum. Meth. B* **2010**, 268, 3356.
[4] G. Szabó, I. Borbély-Kiss. *Nucl. Instrum. Meth. B* **1993**, 75, 123.
[5] M. H. Chen, B. Crasemann. *At. Data Nucl. Data Tables* **1989**, 41, 257.
[6] C. Pascual-Izarra, N. Barradas, M. A. Reis. *Nucl. Instrum. Meth. B* **2006**, 249, 820.
[7] C. Pascual-Izarra, M. A. Reis, A. Taborda. Version v2.08, February 2012, http://cpixe.sourceforge.net/.
[8] N. P. Barradas, C. Jeynes. *Nucl. Instrum. Meth. B* **2008**, 266, 1875.
[9] C. Pascual-Izarra, N. P. Barradas, M. A. Reis, C. Jeynes, M. Menu, B. Lavedrine, J. Jacques Ezrati, S. Rohrs. *Nucl. Instrum. Meth. B* **2007**, 261(1-2), 426.
[10] W. Bambynek, B. Crasemann, R. W. Fink, H.-U. Freund, H. Mark, C. D. Swift, R. E. Prince, P. V. Rao. *Reviews of Modern Physics* **1972**, 44, 716.
[11] W. Brandt, G. Lapicki. *Physical Review A* **1974**, 10, 474.
[12] W. Brandt, G. Lapicki. *Physical Review A* **1979**, 20, 465.
[13] B.-H. Choi. *Physical Review A* **1973**, 7, 2056.
[14] D. D. Cohen, M. Harrigan. *At. Data Nucl. Data Tables* **1985**, 33, 255.
[15] M. Abramovitz, I. Stegun, Handbook of Mathematical Functions, 1st edn, Dover, New York, 1965.
[16] M. A. Reis, A. P. Jesus. *At. Data and Nucl. Data Tables* **1996**, 63, 1-55.
[17] Y. Chauhan, S. Puri. *At. Data Nucl. Data Tables* **2008**, 94, 38.
[18] G. Zschornack. Handbook of X-ray Data. Springer, Berlin, 2007.
[19] J. S. Braich, P. Verma, D. P. Goyal, A. Mandal, B. B. Dhal, H. C. Padhi, H. R. Verma. *Nucl. Instrum. Meth. B* **1996**, 119, 317.
[20] S. J. Cipolla. *Nucl. Instrum. Meth. B* **1995**, 99(1-4), 22.
[21] M. Goudarzi, F. Shokouhi, M. Lamehi-Rachti, P. Oliaiy. *Nucl. Instrum. Meth. B* **2006**, 247, 217.
[22] M. Jaskola, T. Czyzewski, L. Glowacka, D. Banas, J. Braziewicz, M. Pajek, W. Kretschmer, G. Lapicki, D. Trautmann. *Nucl. Instrum. Meth. B* **2000**, 161-163, 191.
[23] R. Mehta, J. L. Duggan, J. L. Price, F. D. McDaniel, G. Lapicki. *Physical Review A* **1982**, 26, 1883.
[24] R. Mehta, J. L. Duggan, J. L. Price, P. M. Kocur, F. D. McDaniel, G. Lapicki. *Physical Review A* **1983**, 28(6), 3217.
[25] M. Pajek, A. P. Kobzev, R. Sandrik, A. V. Skrypnik, R. A. Ilkhamov, S. H. Khusmurodov, G. Lapicki. *Physical Review A* **1990**, 42, 261.
[26] M. Pajek, M. Jaskola, T. Czyzewski, L. Glowacka, D. Banas, J. Braziewicz, W. Kretschmer, G. Lapicki, D. Trautmann. *Nucl. Instrum. Meth. B* **1999**, 150, 33.
[27] K. Sera, K. Ishii, A. Yamadera, A. Kuwako, M. Kamiya, M. Sebata, S. Morita, T. C. Chu. *Physical Review A* **1980**, 22, 2536.
[28] R. Gowda, D. Powers. *Physical Review A* **1985**, 31, 134.
[29] F. Shokouhi, S. Fazinik, I. Bogdanovic, M. Jaksic, V. Valkovic, H. Afarideh. *Nucl. Instrum. Meth. B* **1996**, 109-110, 15.
[30] L. C. Phinney, J. L. Duggan, G. Lapicki, F. U. Naab, K. Hossain, F. D. McDaniel. *J. Phys. B: At. Mol. Opt. Phys.* **2009**, 42, 085202.
[31] L. Rodriguez-Fernandez, J. Miranda, J. L. Ruvalcaba-Sil, E. Segundo, A. Oliver. *Nucl. Instrum. Meth. B* **2002**, 189, 27.
[32] J. L. Campbell. *International Radiation Physics Society* **2010**, 24, 17.
[33] M. A. Reis, L. C. Alves, A. P. Jesus. *Nucl. Instrum. Meth. B* **1996**, 109-110, 134.