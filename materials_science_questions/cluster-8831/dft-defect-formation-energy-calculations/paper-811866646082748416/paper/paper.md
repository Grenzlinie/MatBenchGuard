# Formation of Point Defects in Dilute FCC Alloys

A.Ghoraiⁱᵃ

Department of Physics, Chandernagore College,
Chandernagore-712136, Hooghly,
West Bengal,
India

ᵃamitavaghorai@rediffmail.com

**Keywords:** FCC Metals, Interstitial, Point Defect, Pseudopotential, Vacancy

## Abstract

Using pseudopotential approach, vacancy formation energy $\left(E_{FH}^{1v}\right)$, different non-split interstitial formation energies $\left(E_{FH}^{1t}\right)$ and binding energy for the vacancy-impurity pair $\left(\Delta E_{F}^{v}\right)$ and that for interstitial impurity over host $\left(\Delta E_{F}^{t}\right)$ have been calculated in some cubic fcc metal systems, viz. copper, silver, gold and lead using Ashcroft's potential and Taylor's exchange and correlation function with standard $r_{c}$ (AT) and $r_{c}$ fitted to $\left(E_{FH}^{1v}\right)$ (ATF) and also Heine-Abarenkov's model potential and same exchange and correlations (HAT). It is difficult to have a universal $r_{c}$ value for all types of atomic property calculations. The results show that ATF and HAT combinations are better in comparison to AT. Also, the substitutional impurity adjacent to a vacancy is found to be more loosely bound than the interstitial impurity in fcc metals.

## 1 Introduction

It is well known that properties of solids are more interesting if they depart from perfect lattice structure. Historically, primary interest was in the determination of energies of simplest kind of imperfections like point defects. Different kinds of diffusion mechanisms were predicted from the experimental data of diffusion, quenching, positron annihilation, etc. Vacancy being the simplest kind of point defect has been studied extensively¹,². Whereas due to its complicated nature of motion and formation through different solid substances, studies on interstitials are still in progress³,⁴, these studies have gained its momentum from some observations such as migration of impurities through interstices⁵ and presence of interstitial mechanism in fast diffuser systems⁶,⁷. There are several theoretical models for point defect calculations⁸⁻¹². The lattice static model¹¹ and the atomistic continual model¹² are applied for the calculations of relaxations around a defect and defect energy calculations in fcc metals¹³. But both the models have limitations due to the semi classical approach. Recently the molecular dynamics code has been used to calculate the defect formation and migration energies in several systems¹⁴. Mookerjee et.al.¹⁵ used ab initio potential for calculations of defect parameters.

Another approach, which has been used in this paper, is the linear response formalism of Harrison¹⁶. It is versatile in the sense that it is easy to formulate and calculate all the defect parameters easily. DuCharme and Weaver¹⁷ first used this method to calculate the vacancy formation and migration energy in fcc metals and later this method was extended to evaluate the effect of substitutional impurity during vacancy formation¹⁸. The migration of vacancy in the relaxed neighbour configuration has also been formulated by Takai et. al.¹⁹ and it is further extended to the case of impurity diffusion of tin in lead²⁰. This method is also used to calculate the energetics of non-split interstitial in otherwise pure lattice²¹. Recently this method has been used to explain self and impurity diffusion in dilute alloys by vacancy mechanism²².

In Harrison's approach the perturbation in the conduction electron distribution caused by the creation of a defect is sufficiently weak to be treated in simple linear response formalism. Any defect in the lattice changes the structure dependent lattice energy and so an algebraic difference between the energy after defect creation and that before will yield the defect formation energy when considered for the whole lattice. This structure dependent total energy depends on ion-ion, ion- electron and electron-electron interactions and is also dependent on the modified lattice wave numbers. The modifications in the lattice wave numbers from its perfect lattice value is necessary to maintain the lattice volume and the number of lattice ions constant.

Although this work is not new still it is important due to present day researches on defect structures in $\alpha$-Fe$^{23,24,25}$ using different types of density functional theory. In this paper expressions of monovacancy formation energy, interstitial formation energy and their changes in presence of a single impurity atom are derived from my earlier work.$^{22}$ Usefulness and limitations of model potentials will be analyzed with the help of some other model calculations.

## 2 Formulations

Consider a single defect in an otherwise pure lattice with a total of $N$ ions. If the point defect is a vacancy then the Brillouin zone volume has to be scaled up by a factor of $\frac{N+1}{N}$ in order to keep the lattice volume constant, i.e. the lattice wave numbers are modified to $(1+\frac{1}{3N})q_0$. Again for non- split type of interstitial the number of lattice sites will be reduced to $N-1$, thereby modifying the lattice wave numbers to $(1-\frac{1}{3N})q_0$. If now the above lattice contains one vacancy and one impurity ion at an adjacent lattice site then the vacancy formation energy changes. Also when the impurity is at an interstice, it changes the interstitial formation energy. Finally the expressions for monovacancy formation energy ($E_{FH}^{1v}$), non-split interstitial formation energy ($E_{FH}^{1t}$), and their changes in presence of impurity ion can be obtained from my earlier work$^{22}$ as

$$
E_{FH}^{1v} = \sum_{q_0}' \frac{q_0}{3} \frac{\partial U(q_0)}{\partial q_0} + \frac{\Omega_H}{2\pi^2} \int_0^\infty U(q)q^2 dq \tag{1}
$$

$$
E_{FH}^{1t} = \sum_{q_0}' \left[2(\cos \vec{q}_0 \cdot \vec{r}_i -1)U(q_0)-\frac{q_0}{3} \frac{\partial U(q_0)}{\partial q_0}\right] + \frac{\Omega_H}{2\pi^2} \int_0^\infty U(q)q^2 dq \tag{2}
$$

$$
\Delta E_F^v = -\frac{\Omega_H}{\pi^2} \int_0^\infty \frac{\sin q |\vec{r}_v - \vec{r}_I|}{q |\vec{r}_v - \vec{r}_I|} \Delta U(q)q^2 dq \tag{3}
$$

And

$$
\Delta E_F^t = \sum_{q_0}' 2(\cos \vec{q}_0 \cdot \vec{r}_i -1)\Delta U(\vec{q}_0) + \frac{\Omega_H}{\pi^2} \int_0^\infty \Delta U(q)q^2 dq \tag{4}
$$

Where

$$
U(q) = Lt_{\eta \to \infty} \frac{2\pi e^2 Z_H^2}{\Omega_H q^2} e^{-\frac{q^2}{4\eta}} + [\omega_H(q)]^2 \varepsilon_H(q)\chi_H(q) \tag{5}
$$

$$
\Delta U(q)=L t_{\eta \rightarrow \infty} \frac{2 \pi e^{2}\left(Z_{I}-Z_{H}\right)}{\Omega_{H} q^{2}} e^{-\frac{q^{2}}{4 \eta}}+\left[\omega_{I}(q)-\omega_{H}(q)\right] \omega_{H}(q) \varepsilon_{H}(q) \chi_{H}(q)
\tag{6}
$$

Here the subscripts $H$ and $I$ are for host and impurity respectively, $Z$ the valency, $\Omega_{H}$ the atomic volume, $e$ the electronic charge, $\eta$ the convergence factor, $q_{0}$ and $q$ the lattice and quasi-continuous wave numbers respectively, $\vec{r}_{v}$ the vacancy position, $\vec{r}_{I}$ the adjacent impurity position, $\vec{r}_{i}$ the interstitial position, $\omega_{H}(q)$ the pseudopotential for the host, $\varepsilon_{H}(q)$ the dielectric function $^{26}$ and $\chi_{H}(q)$ the perturbation characteristics. $^{26}$

**Table 1**
Parameters useful for defect energy calculations and pseudopotential for pure metals.

| Metal | $Z$ | $\mathrm{a}_{\mathrm{AU}}$ | $\Omega_{\mathrm{AU}}$ | $k_{F H \mathrm{AU}}$ | $\varepsilon_{F H \text { Ryd. }}$ | $r_{c \mathrm{AU}}^{*}$ | $r_{c \mathrm{AU}}^{* *}$ | $r_{m \mathrm{AU}}^{* * *}$ | $A_{\text {Ryd. }}^{* * *}$ |
| :---- | :-: | :------------------------- | :--------------------- | :------------------- | :------------------------------- | :--------------------- | :---------------------- | :----------------------- | :----------------------- |
| Cu    | 1   | 6.8219                     | 79.370                 | 0.7199               | 0.5182                           | 0.81                   | 1.2488                  | 2.407                    | 0.8308                   |
| Ag    | 1   | 7.7101                     | 114.582                | 0.6369               | 0.4057                           | 1.04                   | 1.4482                  | 2.716                    | 0.7364                   |
| Au    | 1   | 7.6912                     | 113.742                | 0.6385               | 0.4077                           | 0.81                   | 1.4067                  | 2.715                    | 0.7366                   |
| Pb    | 4   | 9.3542                     | 204.622                | 0.8334               | 0.6945                           | 1.12                   | 0.9550                  | 2.0109                   | 3.1827                   |

* taken from ref. $^{26}$ ** fitted to vacancy formation energy. *** taken from ref. $^{22}$

## 3 Discussions

Here integration over quasi-continuous wave numbers is done by quadrature technique and the discrete sum is done over lattice wave numbers. In the formulations relaxation effect around a defect is not considered, so also in the calculations as in the earlier case $^{22}$. Out of six kinds of interstitials, only calculations for non-split type, viz. octahedral, tetrahedral, and crowdion, are discussed here in cases of noble metals (copper, silver and gold) and lead as both host and impurity. Calculations are done using Ashcroft's empty core model potential $^{26}$ $(r_{c})$ with Taylor's $^{27}$ exchange and correlation (henceforth called AT) and Heine and Abarenkov's model potential $^{26}$ $(r_{m}, A)$ with same exchange and correlation (called HAT) and their expressions are

$$
\omega^{\text {Ashcroft }}(q)=-\frac{4 \pi Z_{H} e^{2}}{\Omega_{H} q^{2}} \cos q r_{c}
\tag{7}
$$

$$
\omega^{\text {Heine-Abarenkov }}(q)=\frac{4 \pi A}{\Omega_{H} q^{3}}\left[q r_{m} \cos q r_{m}-\sin q r_{m}\right]-\frac{4 \pi Z_{H} e^{2}}{\Omega_{H} q^{2}} \cos q r_{m}
\tag{8}
$$

And

$$
f^{\text {Taylor }}(q)=\frac{q^{2}}{4 k_{F H}^{2}}\left(1+\frac{0.1534}{\pi k_{F H}}\right)
\tag{9}
$$

Table 1 gives the input parameters used in the present calculations. Two values of $(r_{c})$ for AT combination are given in table 1, the first one $^{26}$ taken from the value fitted to the resistivity of liquid metals (called standard AT) and the second one from the best fit to the experimental value of $E_{F H}^{1 v}$ (called ATF). Table 2 gives the calculated values of $E_{F H}^{1 v}$ and $E_{F H}^{1 t}$ together with their available experimental values $^{28}$ and it is found that $E_{F H}^{1 v}$ is about one-third of $E_{F H}^{1 t}$. Thus more the value of

the defect formation energy less is the stability of that defect. The standard AT model does not yield the correct value of $E_{FH}^{1v}$. The inherent simplicity of Ashcroft's model makes it difficult to have a universal $r_c$ parameter for all types of atomic property calculations where electronic configurations, viz. sp hybridization, d-electron interaction etc. change differently. So experimental value of $E_{FH}^{1v}$ is fitted and calculated values of defect formation energies are presented in table 2. The values of $E_{FH}^{1v}$ calculated from HAT combination agrees fairly well with the experimental values. The value of $E_{FH}^{1t}$ for octahedral, tetrahedral and crowdion are slightly lower than the values calculated by others $^{3}$ in case of ATF and HAT combinations. They used Ashcroft-Hubbard combination with $r_c$ values 1.28, 1.47, and 1.43 atomic unit (AU) for Cu, Ag, and Au, respectively. But Hubbard's exchange and correlation function misrepresents the near neighbour region of inter-atomic potentials and cannot always be trusted $^{29}$. Thus Ashcroft-Taylor combination is perhaps a better choice. Another reason may be due to relaxation effect $^{3}$. It has been pointed out by Doan $^{14}$ that the stable interstitial configuration in noble metals is [100] split. There is a systematic increase in the value of $E_{FH}^{1t}$ from octahedral to crowdion for each metal, which most probably indicates the greater instability of crowdion type. In case of lead $E_{FH}^{1t}$ is negative in general for AT and ATF combinations. For HAT combination it is large for tetrahedral and crowdion and negative for octahedral type. This perhaps indicates the less probability of occurrence of these defects in lead, where vacancy plays the dominant role $^{20}$ and the limitations of Ashcroft's potential.

<table>
<caption>Table 2
Evaluated defect formation energies in Rydbergs for some fcc metals.</caption>
<thead>
<tr>
<th>Energy</th>
<th>Type</th>
<th>Combination</th>
<th>Cu</th>
<th>Ag</th>
<th>Au</th>
<th>Pb</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="4">$E_{FH}^{1v}$</td>
<td rowspan="4">Mono vacancy</td>
<td>Expt*</td>
<td>0.0831</td>
<td>0.0750</td>
<td>0.0662</td>
<td>0.0426</td>
</tr>
<tr>
<td>AT</td>
<td>-0.0059</td>
<td>-0.0017</td>
<td>-0.0249</td>
<td>-0.0147</td>
</tr>
<tr>
<td>ATF</td>
<td>0.0830</td>
<td>0.0750</td>
<td>0.0662</td>
<td>0.0402</td>
</tr>
<tr>
<td>HAT</td>
<td>0.1097</td>
<td>0.0910</td>
<td>0.0919</td>
<td>0.0338</td>
</tr>
<tr>
<td rowspan="12">$E_{FH}^{1t}$</td>
<td rowspan="4">Octahedral</td>
<td>AT</td>
<td>-0.0824</td>
<td>-0.0145</td>
<td>-0.1300</td>
<td>-1.1267</td>
</tr>
<tr>
<td>ATF</td>
<td>0.1780</td>
<td>0.1866</td>
<td>0.1708</td>
<td>-2.0612</td>
</tr>
<tr>
<td>HAT</td>
<td>0.1738</td>
<td>0.1580</td>
<td>0.1592</td>
<td>-0.0444</td>
</tr>
<tr>
<td>AS!</td>
<td>0.25</td>
<td>0.224</td>
<td>0.214</td>
<td></td>
</tr>
<tr>
<td rowspan="4">Tetrahedral</td>
<td>AT</td>
<td>-0.0085</td>
<td>0.0578</td>
<td>-0.0731</td>
<td>-0.6057</td>
</tr>
<tr>
<td>ATF</td>
<td>0.2716</td>
<td>0.2703</td>
<td>0.2550</td>
<td>-1.8084</td>
</tr>
<tr>
<td>HAT</td>
<td>0.2580</td>
<td>0.2326</td>
<td>0.2339</td>
<td>0.8759</td>
</tr>
<tr>
<td>AS!</td>
<td>0.343</td>
<td>0.306</td>
<td>0.298</td>
<td></td>
</tr>
<tr>
<td rowspan="4">Crowdion</td>
<td>AT</td>
<td>0.0552</td>
<td>0.1170</td>
<td>-0.0181</td>
<td>0.2007</td>
</tr>
<tr>
<td>ATF</td>
<td>0.3338</td>
<td>0.3245</td>
<td>0.3109</td>
<td>-1.2213</td>
</tr>
<tr>
<td>HAT</td>
<td>0.3201</td>
<td>0.2881</td>
<td>0.2895</td>
<td>1.6859</td>
</tr>
<tr>
<td>AS!</td>
<td>0.401</td>
<td>0.357</td>
<td>0.35</td>
<td></td>
</tr>
</tbody>
</table>

{*} experimental values taken from $^{22,28}$. ! AS taken from ref. $^{3}$.

The computed values of change in the vacancy formation energy in presence of impurity ion or vacancy impurity binding energy ($\Delta E_{F}^{v}$) and the change in the impurity interstitial formation energy over host interstitial ($\Delta E_{F}^{i}$) are shown in table 3 for AT, ATF and HAT combinations. Since AT combination does not produce correct order of magnitude, the energy values in AT columns are shown for comparison only. It is found that the values of $\Delta E_{F}^{v}$ are small positive and negative and also these values are in general less than $\Delta E_{F}^{i}$, which may be due to the fact that substitutional impurity is more loosely bound to the lattice than the interstitial impurity. Thus substitutional impurity formation adjacent to a vacancy is easier and vacancy plays the dominant role for diffusion in these alloys. The value of $\Delta E_{F}^{i}$ gradually decreases in magnitude from octahedral to crowdion for homovalent systems and for lead based systems. Also every binary system and its reverse (say Cu-Ag and Ag-Cu) show complementary character. In case of heterovalent systems this

complementary nature is satisfied in case of $\Delta E_{F}^{v}$ with HAT combination only. The value of $\Delta E_{F}^{t}$
in lead based systems is large enough, indicating less probable occurrence. At present there is very
little experimental data on point defect parameters. So it is difficult to say the last word about the
calculated defect parameters.

Table 3
Evaluated values of change in defect formation energies in presence of impurities in Cu, Ag, Au
and Pb based binary systems in Rydbergs.

<table>
<thead>
<tr>
<th rowspan="2">System</th>
<th colspan="3">$\Delta E_{F}^{v}$</th>
<th colspan="9">$\Delta E_{F}^{t}$</th>
</tr>
<tr>
<th colspan="3">Mono vacancy</th>
<th colspan="3">Octahedral</th>
<th colspan="3">Tetrahedral</th>
<th colspan="3">Crowdion</th>
</tr>
<tr>
<th></th>
<th>AT</th>
<th>ATF</th>
<th>HAT</th>
<th>AT</th>
<th>ATF</th>
<th>HAT</th>
<th>AT</th>
<th>ATF</th>
<th>HAT</th>
<th>AT</th>
<th>ATF</th>
<th>HAT</th>
</tr>
</thead>
<tbody>
<tr>
<td>CuAg</td>
<td>0.0</td>
<td>-0.002</td>
<td>-0.004</td>
<td>0.111</td>
<td>0.108</td>
<td>0.059</td>
<td>0.121</td>
<td>0.106</td>
<td>0.058</td>
<td>0.123</td>
<td>0.102</td>
<td>0.058</td>
</tr>
<tr>
<td>CuAu</td>
<td>0.0</td>
<td>-0.002</td>
<td>-0.004</td>
<td>0.0</td>
<td>0.085</td>
<td>0.059</td>
<td>0.0</td>
<td>0.084</td>
<td>0.058</td>
<td>0.0</td>
<td>0.081</td>
<td>0.058</td>
</tr>
<tr>
<td>CuPb</td>
<td>0.0</td>
<td>-0.0</td>
<td>-0.029</td>
<td>-0.153</td>
<td>-0.023</td>
<td>0.650</td>
<td>0.121</td>
<td>0.257</td>
<td>0.903</td>
<td>0.326</td>
<td>0.463</td>
<td>1.087</td>
</tr>
<tr>
<td>AgCu</td>
<td>-0.0</td>
<td>0.001</td>
<td>0.002</td>
<td>-0.099</td>
<td>-0.08</td>
<td>-0.044</td>
<td>-0.105</td>
<td>-0.079</td>
<td>-0.043</td>
<td>-0.107</td>
<td>-0.075</td>
<td>-0.042</td>
</tr>
<tr>
<td>AgAu</td>
<td>-0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>-0.099</td>
<td>-0.017</td>
<td>-0.0</td>
<td>-0.105</td>
<td>-0.016</td>
<td>-0.0</td>
<td>-0.107</td>
<td>-0.015</td>
<td>-0.0</td>
</tr>
<tr>
<td>AgPb</td>
<td>0.003</td>
<td>0.007</td>
<td>-0.01</td>
<td>-0.228</td>
<td>-0.073</td>
<td>0.419</td>
<td>-0.001</td>
<td>0.182</td>
<td>0.649</td>
<td>0.178</td>
<td>0.375</td>
<td>0.815</td>
</tr>
<tr>
<td>AuCu</td>
<td>0.0</td>
<td>0.001</td>
<td>0.002</td>
<td>0.0</td>
<td>-0.066</td>
<td>-0.044</td>
<td>0.0</td>
<td>-0.066</td>
<td>-0.043</td>
<td>0.0</td>
<td>-0.063</td>
<td>-0.042</td>
</tr>
<tr>
<td>AuAg</td>
<td>0.001</td>
<td>-0.0</td>
<td>-0.0</td>
<td>0.097</td>
<td>0.017</td>
<td>0.0</td>
<td>0.106</td>
<td>0.017</td>
<td>0.0</td>
<td>0.109</td>
<td>0.016</td>
<td>0.0</td>
</tr>
<tr>
<td>AuPb</td>
<td>0.004</td>
<td>0.006</td>
<td>-0.011</td>
<td>-0.419</td>
<td>-0.124</td>
<td>0.425</td>
<td>-0.198</td>
<td>0.126</td>
<td>0.656</td>
<td>-0.017</td>
<td>0.316</td>
<td>0.823</td>
</tr>
<tr>
<td>PbCu</td>
<td>0.004</td>
<td>0.001</td>
<td>0.003</td>
<td>1.394</td>
<td>3.418</td>
<td>0.812</td>
<td>0.936</td>
<td>3.284</td>
<td>0.119</td>
<td>0.287</td>
<td>2.899</td>
<td>-0.492</td>
</tr>
<tr>
<td>PbAg</td>
<td>0.004</td>
<td>0.001</td>
<td>0.002</td>
<td>1.725</td>
<td>3.646</td>
<td>1.004</td>
<td>1.315</td>
<td>3.560</td>
<td>0.340</td>
<td>0.698</td>
<td>3.214</td>
<td>-0.275</td>
</tr>
<tr>
<td>PbAu</td>
<td>0.004</td>
<td>0.001</td>
<td>0.002</td>
<td>1.394</td>
<td>3.597</td>
<td>1.004</td>
<td>.936</td>
<td>3.500</td>
<td>0.339</td>
<td>0.287</td>
<td>3.146</td>
<td>-0.276</td>
</tr>
</tbody>
</table>

It is mentioned earlier $^{22}$ that a proper choice of pseudopotential is very important and a
careful attention must be paid in achieving accuracy in numerical computation in order to arrive at a
meaningful result. So Ashcroft-Taylor combination with $r_{c}$ fitted to $E_{FH}^{lv}$ or Heine-Abarenkov
model with approximate overall explanation of all atomic properties $^{26}$ is perhaps a better choice.

### Acknowledgements

The author is grateful to Prof. S. K. Sen (Retd.), Department of Materials Sciene, I. A. C. S.
Kolkata-700032 and Prof. J. Dey (Retd), Physics Department, Maulana Azad College, Kolkata-
700013, for their constant encouragement during the course of this work.

### References

1  Vacancies '76, ed Smallman R E & Harris J E (The Metal Society), 1976.

2  Triftshauser W, Matter H & Winter J, Appl. Phys. A, 28 (1982) 179.

3  Bandyopadhyay A K & Sen S K, phys. status solidi b, 157 (1990) 519.

4  Lam N Q, Dagens L & Doan N V, J. Phys. F, 13 (1983) 2503.

5  Sen S K, Huntington H B & Sokolowski R S, Scripta Metall. 17 (1983) 569.

6  Warburton W K & Turnbull D in Diffusion in Solids : Recent Developments, ed Nowick A S
and Burton S S (Academic Press, NewYork), 1975 p.171.

7  Fujita S, J. Phys. Chem. Solids, 49 (1988) 41.

8  Thomson M N, Defects and radiation damage in metals(Cambridge Univ.Press, Oxford), 1968.

9  Evans R & Finnis M W, J. Phys. F, 6 (1976) 483.

10 Doyama M & Koehler J S in Point defects and defect interactions in metals, ed Takamura J, Doyama M and Kiritani M(North-Holland, Amsterdam), 1982, p.643.

11 Kanzaki H, J. Phys. Chem. Solids, 2 (1957) 24.

12 Kornblit L, phys. status solidi b, 115 (1983) 485.

13 Ghorai A, phys. status solidi b, 167 (1991) 551.

14 Doan N V, Phil. Mag. A, 58 (1988) 179.

15 Abhijit Mookerjee, Nan-Xian Chen, Vijay Kumar & Mohammed Abdus Satter, J. Phys. Condens. Matter, 4 (1992) 2439.

16 Harrison W A, Pseudopotentials in the theory of metals(Benjamin, NewYork), 1966.

17 DuCharme A R & Weaver H T, Phys. Rev. B, 5 (1972) 330.

18 Yamamoto R, Takai O & Doyama M, Crystal Lattice Defects, 5 (1974) 45.

19 Takai O, Doyama M & Hisamatsu in Point defects and defect interactions in metals, ed Takamura J, Doyama M & Kiritani M(North-Holland, Amsterdam), 1982, p.117.

20 Sen S K & Ghorai A, Phil. Mag. A, 59 (1989) 707.

21 Ghorai A, Indian J. Pure & Appl. phys. 32 (1994) 508.

22 Ghorai A, Phys. Rev. B, 46 (1992) 5229.

23 Domain C & Becquart C S, Phys. Rev. B 71 (2005) 214109.

24 Gordon Stewart M J, Kenny S D & Smith Roger, Phys. Rev. B 72 (2005) 214104.

25 Olsson Par, Domain Christophe & Wallenius Janne, Phys. Rev. B 75 (2007) 014110.

26 Cohen M & Heine V, Solid State Phys. ed. Ehrenreich H, Seitz F & Turnbull D(Academic, NewYork) 24 (1970) 55.

27 Taylor R, J. Phys. F 8 (1978) 1699.

28 Schule W, Defect and Diffusion Forum 66-69 (1989) 313.

29 Duesbery M S and Taylor R, Solid State Comun. A 30 (1969) 496.

Defects and Diffusion in Ceramics X
10.4028/www.scientific.net/DDF.280-281

Formation of Point Defects in Dilute FCC Alloys
10.4028/www.scientific.net/DDF.280-281.79