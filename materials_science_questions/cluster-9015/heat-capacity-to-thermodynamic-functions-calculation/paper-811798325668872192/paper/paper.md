# International Equations for the Saturation Properties of Ordinary Water Substance. Revised According to the International Temperature Scale of 1990.

Addendum to J. Phys. Chem. Ref. Data 16, 893 (1987)

W. Wagner* and A. Pruss

Institut für Thermo- und Fluiddynamik, Ruhr-Universität Bochum, D 44780 Bochum, Germany

Received October 2, 1992; revised manuscript received January 29, 1993

In 1987, consistent with the latest experimental data and the internationally recommended values for the critical parameters, we published compact and accurate correlation equations for the following properties on the saturation line of ordinary (light) water substance: vapor pressure, density, enthalpy, and entropy of both the saturated liquid and the saturated vapor [A. Saul and W. Wagner, J. Phys. Chem. Ref. Data 16, 893 (1987)]. As an addendum to this 1987 paper the present paper brings all temperature values and adjusted coefficients in all correlation equations given in the 1987 paper into agreement with the International Temperature Scale of 1990 (ITS-90). The new equations form the basis of the "Revised Supplementary Release on Saturation Properties of Ordinary Water Substance" issued by the International Association for the Properties of Water and Steam (IAPWS). This revised release which contains all equations and coefficients adjusted with regard to the ITS-90 is the main part of this paper.

Key words: enthalpy; entropy; IAPWS; saturated liquid density, saturated vapor density; saturation line; vapor pressure; water.

## 1. Introduction

The International Association for the Properties of Water and Steam (IAPWS) provides internationally accepted formulations for the properties of light and heavy steam, water and selected aqueous solutions for scientific and industrial applications. Besides publications on other properties there are special correlation equations for the gas-liquid saturation properties of ordinary water substance published in $1987^{1}$ which were based on the International Practical Temperature Scale of 1968 (IPTS-68).$^{2}$ As a result of a decision by the Executive Committee of IAPWS at their meeting in Tokyo 1991, other correlation equations, as well as the equations for the saturation properties of ordinary water substance should be revised to bring them into agreement with the International Temperature Scale of 1990 (ITS-90).$^{3}$

Therefore, it is the purpose of this addendum to Ref. 1 to summarize very briefly how these equations have been adjusted to ITS-90 and to present all temperature values and parameters in the equations corresponding to ITS-90. However, this paper does not repeat the information on the data evaluation nor the way in which the mathematical structure of the equations was obtained. All this background information can be found in the original papers of Saul and Wagner. $^{1,4}$

## 2. Conversion of the Equations

To bring any temperature value based on the IPTS-68 scale into agreement with the ITS-90 scale, equation (1.3) from Ref. 5 was used; cf. also the comment by Rusby $^{6}$ on this matter.

All equations for the properties on the saturation line vapor-liquid of $\mathrm{H}_{2} \mathrm{O}$ considered in this paper have been adjusted to ITS-90 by refitting the equations from Ref. 1 to the same input data whose temperature values had been converted to ITS-90 temperatures. Compared to the IPTS-68 temperature values given in the original paper, $^{1}$ one more decimal place has been used here for the converted ITS-90 temperature values. This ensures that any recalculation to the original IPTS-68 temperature values produces the same figures as given in the original source after rounding to the same number of decimal places. This increase by one decimal in the converted ITS-90 temperatures does not imply that these values have been redetermined or are more accurate than previously stated on IPTS-68. This procedure was agreed at the 1992 IAPWS meeting in St. Petersburg.

As a result of this conversion and refitting process we have obtained the ITS-90 coefficients for the vapor-pressure equation and the equations for the density, enthalpy, and entropy for both the saturated liquid and vapor. Full

*To whom correspondence should be addressed.

©1993 by the U.S. Secretary of Commerce on behalf of the United States. This copyright is assigned to the American Institute of Physics and the American Chemical Society.

Reprints available from ACS; see Reprints List at back of issue.

0047-2689/93/030783-05/$10.00
783
J. Phys. Chem. Ref. Data, Vol. 22, No. 3, 1993

784
W. WAGNER AND A. PRUSS

information on all these equations, namely the equations themselves, the coefficients and reference constants, the range of validity, the estimates of uncertainty and a table to assist the user in computer-program verification is given in the "Revised Supplementary Release on Satura- tion Properties of Ordinary Water Substance" which forms the Appendix of this paper.

In order to make clear what is meant by the conversion of the input data to bring them into accordance with the ITS-90, the following details are given:
(1) All directly measured input data (all $p_{s}, T$ and all $\rho^{\prime}, T$ data except Osborne et al.'s$^{\text{b}}$ $\rho^{\prime}$ values) were brought into agreement with ITS-90 by temperature conver- sion only and keeping the $p_{s}$ and $\rho^{\prime}$ values unchanged.
(2) Osborne et al. did not measure $\rho^{\prime}, T$ and $\rho^{\prime \prime}, T$ data but $\beta, T$ and $\gamma, T$ data which we had already had in form of $\beta, T_{68}$ and $\gamma, T_{68}$ data in Ref. 1. The $\rho_{68}^{\prime}, T_{68}$ and $\rho_{68}^{\prime \prime}, T_{68}$ data used in Ref. 1 were determined from the $\beta, T_{68}$ and $\gamma, T_{68}$ data by using relation $\rho_{68}^{\prime}=T_{68} \cdot(\mathrm{d} p_{s} / \mathrm{d} T)_{68} / \beta$ and $\rho_{68}^{\prime \prime}=T_{68} \cdot(\mathrm{d} p_{s} / \mathrm{d} T)_{68} / \gamma$, for details see Ref. 1. Here, in order to get the $\rho_{90}^{\prime}, T_{90}$ and $\rho_{90}^{\prime \prime}, T_{90}$ data we con verted the $\beta, T_{68}$ and $\gamma, T_{68}$ data to $\beta, T_{90}$ and $\gamma, T_{90}$ data by applying the above-mentioned procedure used to convert $T_{68}$ to $T_{90}$ temperatures. Then, the needed $\rho_{90}^{\prime}, T_{90}$ and $\rho_{90}^{\prime \prime}, T_{90}$ input data were obtained from $\rho_{90}^{\prime}=$ $T_{90} \cdot(\mathrm{d} p_{s} / \mathrm{d} T)_{90} / \beta$ and from $\rho_{90}^{\prime \prime}=T_{90} \cdot(\mathrm{d} p_{s} / \mathrm{d} T)_{90} / \gamma$, re spectively. This means, that Osborne et al.'s $\rho_{90}^{\prime}, T_{90}$ and $\rho_{90}^{\prime \prime}, T_{90}$ input data do not only have different tem perature values ($T_{90}$ instead of $T_{68}$) but they also have slightly different density values ($\rho_{90}^{\prime}$ and $\rho_{90}^{\prime \prime}$ instead of $\rho_{68}^{\prime}$ and $\rho_{68}^{\prime \prime}$, respectively).
(3) The key values for establishing the equations for the enthalpies $h^{\prime}$ and $h^{\prime \prime}$ and for the entropies $s^{\prime}$ and $s^{\prime \prime}$ of the saturated liquid and vapor are Osborne et al.'s $\alpha$ experiments where the change of $\alpha$ corresponding to $\alpha_{1}^{2}=\alpha(T_{2})-\alpha(T_{1})$ was measured between the two temperatures $T_{1}$ and $T_{2}$. These two IPTS-68 tempera ture values belonging to each $\alpha_{1}^{2}$ input value were con verted to ITS-90 temperatures as indicated above. This means that the ITS-90 input values $\alpha_{1}^{2}$ for Eq. (3.12a) in Ref. 1 belong to slightly changed tempera- ture differences $(T_{2}-T_{1})_{90}$ ; the $\alpha_{1}^{2}$ values themselves were not changed.

The critical parameters needed for the evaluation of the ITS-90 saturation equations are given in Sec. 2 of the Appendix. The numerical values for the critical pressure $p_{c}$ and the critical density $\rho_{c}$ are identical to those given in Ref. $7^{\mathrm{c}}$ and accordingly also in Ref. 1. The IPTS-68 value for the critical temperature ($T_{c, 68}=647.14 \mathrm{~K}^{7}$) was converted to ITS-90 by using the procedure described at the beginning of Sec. 2. The value of the critical temper- ature on ITS-90 is 647.096 K. Agreement on this value was reached at the 1992 IAPWS meeting in St. Peters- burg. The "Revised Release on the IAPS Statement, 1983, of the Values of the Temperature, Pressure, and Density of Ordinary and Heavy Water Substances at their Respective Critical Points" is available from the IAPWS Secretariat and will be published as an Addendum to Ref. 7.

3. Acknowledgments

The authors would like to thank the members of the IAPWS Working Group "Thermophysical Properties of Water and Steam" for fruitful discussions and helpful hints. We are especially grateful to J. R. Cooper and Dr. H. Sato, who checked the draft of the revised supplemen- tary release, and to Dr. J. M. H. Levelt Sengers and Prof. K. Watanahe who contributed useful ideas and sugges- tions for the final version of this work.

4. References

$^{1}$A. Saul and W. Wagner, J. Phys. Chem. Ref. Data 16, 893 (1987).
$^{2}$International Practical Temperature Scale of 1968, Metrologia 5, 35 (1969).
$^{3}$H. Preston-Thomas, Metrologia 27, 3 (1990).
$^{4}$W. Wagner and A. Saul, in Proceedings of the 10th International Confer- ence on the Properties of Steam, edited by V. V. Sychev and A. A. Alex- androv (Mir, Moscow, 1986), p. 199.
$^{5}$Supplementary Information for the ITS-90. International Bureau of Weights and Measures: Pavillon de Breteuil, F-92312 Sevres, France, 1990.
$^{6}$R. L. Rusty, J. Chem. Thermodynamics 23, 1153 (1991).
$^{7}$J. M. H. Levelt Sengers, J. Straub, K. Watanabe, and P. G. Hill, J. Phys. Chem. Ref. Data 14, 193 (1985).

$^{\text{a}}$For Nomenclature see Appendix or Ref. 1.
$^{\text{b}}$The corresponding references can be taken from Ref. 1.

$^{\text{c}}$Reference 7 contains the verbatim copy of the IAPS Statement, 1983, of the Values of the Temperature, Pressure, and Density of Pure Or- dinary and Heavy Water Substances at their Respective Critical Points.

J. Phys. Chem. Ref. Data, Vol. 22, No. 3, 1993

# INTERNATIONAL EQUATIONS FOR THE SATURATION PROPERTIES OF WATER

## Appendix

### The International Association for
the Properties of Water and Steam

St. Petersburg, Russia
September 1992

### Revised Supplementary Release on Saturation
Properties of Ordinary Water Substance

Unrestricted publication allowed in all countries.
Issued by the International Association for the Properties of Water and Steam

President, Dr. Dr. h. c. J. M. H. Levelt Sengers
Thermophysics Division
National Institute of Standards and Technology
Gaithersburg, Maryland 20899
U.S.A.

Executive Secretary, Dr. B. Dooley
EPRI
3412 Hillview Ave, Palo Alto,
California 94303
U.S.A.

This release has been authorized by the International Association for the Properties of Water and Steam (IAPWS) at its meeting in St. Petersburg, Russia, 6-12 September 1992, for issue by its Secretariat. The members of IAPWS are Canada, Czechoslovakia, Denmark, the Federal Republic of Germany, France, Japan, Russia, the United Kingdom, and the United States of America.

IAPS previously issued a *Release on the IAPS Formula- tion 1984 for the Thermodynamic Properties of Ordinary Water Substance for Scientific and General Use* and a *Release on the IAPS Skeleton Tables 1985 for the Thermodynamic Properties of Ordinary Water Substance*. Both releases yield values for the saturation properties of ordinary water substance which are not identical but which agree within the mutual tolerances quoted in the two releases. IAPS also issued a *Supplementary Release on Saturation Properties of Ordinary Water Substance* containing a set of simple equations which yield for ordinary water substance the vapor pressure as well as the density, specific enthalpy and specific entropy of the saturated vapor and liquid. The values calculated from these equations for the vapor pressure, the density and specific enthalpy of the vapor and liquid at saturation are identical to the values tabulated for these properties in the IAPS Skeleton Tables 1985.

This *Supplementary Release on Saturation Properties of Ordinary Water Substance* issued in 1986 was based on the IPTS-68 temperature scale. The temperatures of the triple point, the critical point, and the temperature dependence of all correlation equations presented are known to an accuracy that require parameters to be adjusted for the use of the current Temperature Scale of 1990 (ITS-90). In this revised release the temperature values of the critical point and the parameters in the correlation equations have been changed to comply with the Temperature Scale of 1990 (ITS-90).

The equations in this revised Supplementary Release have been adjusted to ITS-90 by refitting all equations from the Supplementary Release issued in 1986 to the same input data whose temperature values had been converted to ITS-90 temperatures. Compared to the IPTS-68 temperature values given in the original release, one more decimal place is given here to the converted ITS-90 temperature values. This ensures that any recalculation to the original IPTS-68 temperature values produces the same figures as given in the original source after rounding to the same number of decimal places. This increase by one decimal in the converted ITS-90 temperatures does not imply that these values have been redetermined or are more accurate than previously stated on IPTS-68.

Further details about the equations presented in the release can be found in "International Equations for the Saturation Properties of Ordinary Water Substance Revised according to the International Temperature Scale of 1990" by W. Wagner and A. Pruss, to be published in the Journal of Physical and Chemical Reference Data.

Further information about this release and other releases issued by IAPWS can be obtained from the Executive Secretary of IAPWS.

---

## Equations for the Thermodynamic
Properties of Ordinary Water
Substance at Saturation

### 1. Nomenclature

Thermodynamic quantities:
$h$ = Specific enthalpy
$p$ = Vapor pressure
$s$ = Specific entropy
$T$ = Temperature
$u$ = Specific internal energy
$\rho$ = Density (mass divided by volume)
$\alpha$ = Auxiliary quantity for specific enthalpy
$\phi$ = Auxiliary quantity for specific entropy
$\theta$ = $T/T_c$
$\tau$ = $1-\theta$

Subscripts:
c Denotes value at the critical point
t Denotes value at the (ice I, liquid, vapor) triple point

Superscripts:
' Denotes value of the saturated liquid
'' Denotes value of the saturated vapor

Note: $T$ denotes absolute temperature on the International Temperature Scale of 1990.

---

J. Phys. Chem. Ref. Data, Vol. 22, No. 3, 1993

### 2. Reference Constants

$$
\begin{align*}
T_{\mathrm{c}} &= 647.096\ \mathrm{K} & \alpha_{0} &= 1000\ \mathrm{J/kg} \\
p_{\mathrm{c}} &= 22.064\ \mathrm{MPa} & \phi_{0} &= \alpha_{0}/T_{\mathrm{c}} \\
\rho_{\mathrm{c}} &= 322\ \mathrm{kg/m^3}
\end{align*}
$$

Note: The numerical values for the critical parameters $p_{\mathrm{c}}$ and $\rho_{\mathrm{c}}$ are identical to those given in *IAPS Statement, 1983, of the Values of the Temperature, Pressure and Density of the Pure Ordinary and Heavy Water Substances at their Respective Critical Points*. The value for $T_{\mathrm{c}}$ corresponds to the IAPS value converted to the current Temperature Scale of 1990 (ITS-90).

### 3. Vapor Pressure

$$
\ln\left(\frac{p}{p_{\mathrm{c}}}\right)=\frac{T_{\mathrm{c}}}{T}\left[a_{1}\tau+a_{2}\tau^{1.5}+a_{3}\tau^{3}+a_{4}\tau^{3.5}+a_{5}\tau^{4}+a_{6}\tau^{7.5}\right] \tag{1}
$$

with
$$
\begin{align*}
a_{1} &= -7.85951783 & a_{4} &= 22.6807411 \\
a_{2} &= 1.84408259 & a_{5} &= -15.9618719 \\
a_{3} &= -11.7866497 & a_{6} &= 1.80122502
\end{align*}
$$

### 4. Densities

#### 4.1. Density of the saturated liquid

$$
\frac{\rho'}{\rho_{\mathrm{c}}}=1+b_{1}\tau^{1/3}+b_{2}\tau^{2/3}+b_{3}\tau^{5/3}+b_{4}\tau^{16/3}+b_{5}\tau^{43/3}+b_{6}\tau^{110/3} \tag{2}
$$

with
$$
\begin{align*}
b_{1} &= 1.99274064 & b_{4} &= -1.75493479 \\
b_{2} &= 1.09965342 & b_{5} &= -45.5170352 \\
b_{3} &= -0.510839303 & b_{6} &= -6.74694450 \times 10^{5}
\end{align*}
$$

#### 4.2 Density of the saturated vapor

$$
\ln\left(\frac{\rho''}{\rho_{\mathrm{c}}}\right)=c_{1}\tau^{2/6}+c_{2}\tau^{4/6}+c_{3}\tau^{8/6}+c_{4}\tau^{18/6}+c_{5}\tau^{37/6}+c_{6}\tau^{71/6} \tag{3}
$$

with
$$
\begin{align*}
c_{1} &= -2.03150240 & c_{4} &= -17.2991605 \\
c_{2} &= -2.68302940 & c_{5} &= -44.7586581 \\
c_{3} &= -5.38626492 & c_{6} &= -63.9201063
\end{align*}
$$

### 5. Specific Enthalpy and Specific Entropy

#### 5.1. Auxiliary equations

$$
\frac{\alpha}{\alpha_{0}}=d_{\alpha}+d_{1}\theta^{-19}+d_{2}\theta+d_{3}\theta^{4.5}+d_{4}\theta^{5}+d_{5}\theta^{54.5} \tag{4}
$$

$$
\frac{\phi}{\phi_{0}}=d_{\phi}+\frac{19}{20}d_{1}\theta^{-20}+d_{2}\ln\theta+\frac{9}{7}d_{3}\theta^{3.5}+\frac{5}{4}d_{4}\theta^{4}+\frac{109}{107}d_{5}\theta^{53.5} \tag{5}
$$

with
$$
\begin{align*}
d_{1} &= -5.65134998 \times 10^{-8} & d_{\alpha} &= -1135.905627715 \\
d_{2} &= 2690.66631 & d_{\phi} &= 2319.5246 \\
d_{3} &= 127.287297 \\
d_{4} &= -135.003439 \\
d_{5} &= 0.981825814
\end{align*}
$$

#### 5.2. Specific enthalpy of the saturated liquid

$$
h'=\alpha+\frac{T}{\rho'}\frac{\mathrm{d}p}{\mathrm{d}T} \tag{6}
$$

Equation (6) yields the specific enthalpy of the saturated liquid when used in conjunction with Eqs. (1), (2), and (4).

Note: The specific internal energy and the specific entropy of the liquid at the triple point $u'_{\mathrm{t}}$ and $s'_{\mathrm{t}}$ have been set equal to zero (5th ICPS 1956). As a consequence, from the relation $h'_{\mathrm{t}}=p_{\mathrm{s}}(T_{\mathrm{t}})/\rho'(T_{\mathrm{t}})$ one gets for the specific enthalpy of the liquid at the triple point the value
$$
h'_{\mathrm{t}}=0.611786\ \mathrm{J/kg}.
$$

In order to reproduce this numerical value for $h'_{\mathrm{t}}$ from Eq. (6), 13 significant figures are required for the constant $d_{\alpha}$ as quoted above. A decrease of the number of decimal places in $d_{\alpha}$ affects the enthalpy of the saturated liquid only near the triple point, but does not significantly affect the values of $p$, $\rho'$, $\rho''$, $h''$, $s'$ and $s''$. For example, a reduction of $d_{\alpha}$ to 10 significant figures changes $h'/(J/kg)$ in the 4th decimal place at a temperature of 273.16 K.

#### 5.3. Specific enthalpy of the saturated vapor

$$
h''=\alpha+\frac{T}{\rho''}\frac{\mathrm{d}p}{\mathrm{d}T} \tag{7}
$$

Equation (7) yields the specific enthalpy of the saturated vapor when used in conjunction with Eqs. (1), (3), and (4).

#### 5.4. Specific entropy of the saturated liquid

$$
s'=\phi+\frac{1}{\rho'}\frac{\mathrm{d}p}{\mathrm{d}T} \tag{8}
$$

Equation (8) yields the specific entropy of the saturated liquid when used in conjunction with Eqs. (1), (2), and (5).

#### 5.5. Specific entropy of the saturated vapor

$$
s''=\phi+\frac{1}{\rho''}\frac{\mathrm{d}p}{\mathrm{d}T} \tag{9}
$$

Equation (9) yields the specific entropy of the saturated vapor when used in conjunction with Eqs. (1), (3), and (5).

---

J. Phys. Chem. Ref. Data, Vol. 22, No. 3, 1993

# INTERNATIONAL EQUATIONS FOR THE SATURATION PROPERTIES OF WATER

## 6. Range of Validity of the Equations

IAPWS endorses the validity of the equations presented in this revised supplementary release for vapor-liquid equilibrium from the triple point to the critical point. This corresponds to

$$273.16\ \text{K} \leqslant T \leqslant 647.096\ \text{K} \tag{10}$$

## 7. Estimates of Uncertainty

Values calculated from the equations for $p$, $1/\rho'$, $1/\rho''$, $h'$, and $h''$ have estimated uncertainties which are identical to the values in Table 3 of the *Release on the IAPS Skeleton Tables 1985 for the Thermodynamic Properties of Ordinary Water Substance*. The values calculated from the equations for $p$, $1/\rho'$, $1/\rho''$, $h'$, and $h''$ together with their estimated uncertainties are identical to values in Table 3 of the forthcoming *Revised Release on the IAPWS Skeleton Tables 1985 for the Thermodynamic Properties of Ordinary Water Substance*.

## 8. Computer-Program Verification

To assist the user in computer-program verification, Table 1 lists values for $p$, $\text{d}p/\text{d}T$, $\rho'$, $\rho''$, $\alpha$, $h'$, $h''$, $\phi$, $s'$, and $s''$ calculated at three temperatures. The results quoted in Table 1 were obtained with the aid of a computer having 14 significant figure accuracy and with the values of $d_{\alpha}$ and $d_{\phi}$ given in Sec. 5.1. of the Appendix. If the calculations are performed with a computer with less than 14 significant figures, the results will be clearly within the estimated uncertainty of the various properties except for the enthalpy of the saturated liquid close to the triple point.

Table 1. Thermodynamic property values calculated at three selected temperatures

<table>
  <thead>
    <tr>
      <th></th>
      <th>$T = 273.16\ \text{K}$</th>
      <th>$T = 373.1243\ \text{K}$</th>
      <th>$T = 647.096$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$p/\text{Pa}$</td>
      <td>611.657</td>
      <td>$0.101325 \times 10^6$</td>
      <td>$22.064 \times 10^6$</td>
    </tr>
    <tr>
      <td>$(\text{d}p/\text{d}T)/(\text{Pa K}^{-1})$</td>
      <td>44.436693</td>
      <td>$3.616 \times 10^3$</td>
      <td>$268 \times 10^3$</td>
    </tr>
    <tr>
      <td>$\rho'/({\text{kg m}^{-3}})$</td>
      <td>999.789</td>
      <td>958.365</td>
      <td>322</td>
    </tr>
    <tr>
      <td>$\rho''/({\text{kg m}^{-3}})$</td>
      <td>0.00485426</td>
      <td>0.597586</td>
      <td>322</td>
    </tr>
    <tr>
      <td>$\alpha/({\text{J kg}^{-1}})$</td>
      <td>$-11.529101$</td>
      <td>$417.65 \times 10^3$</td>
      <td>$1548 \times 10^3$</td>
    </tr>
    <tr>
      <td>$h'/({\text{J kg}^{-1}})$</td>
      <td>0.611786</td>
      <td>$419.05 \times 10^3$</td>
      <td>$2086.6 \times 10^3$</td>
    </tr>
    <tr>
      <td>$h''/({\text{J kg}^{-1}})$</td>
      <td>$2500.5 \times 10^3$</td>
      <td>$2675.7 \times 10^3$</td>
      <td>$2086.6 \times 10^3$</td>
    </tr>
    <tr>
      <td>$\phi/({\text{J kg}^{-1}\text{K}^{-1}})$</td>
      <td>$- 0.04$</td>
      <td>$1.303 \times 10^3$</td>
      <td>$3.578 \times 10^3$</td>
    </tr>
    <tr>
      <td>$s'/({\text{J kg}^{-1}\text{K}^{-1}})$</td>
      <td>0</td>
      <td>$1.307 \times 10^3$</td>
      <td>$4.410 \times 10^3$</td>
    </tr>
    <tr>
      <td>$s''/({\text{J kg}^{-1}\text{K}^{-1}})$</td>
      <td>$9.154 \times 10^3$</td>
      <td>$7.355 \times 10^3$</td>
      <td>$4.410 \times 10^3$</td>
    </tr>
  </tbody>
</table>

J. Phys. Chem. Ref. Data. Vol. 22. No. 3. 1993