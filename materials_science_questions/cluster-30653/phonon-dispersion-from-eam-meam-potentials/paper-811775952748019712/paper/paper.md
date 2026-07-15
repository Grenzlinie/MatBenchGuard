# THERMOPHYSICAL PROPERTIES OF MATERIALS

# Molecular-Dynamic Simulation of the Thermophysical Properties of Liquid Uranium
D. K. Belashchenko $^{a}$ , D. E. Smirnova $^{a}$ , and O. I. Ostrovski $^{b}$

$^{a}$ National Research University of Technology-Moscow Institute of Steel and Alloys, Moscow, 117936 Russia
e-mail: dkbel@mail.ru
$^{b}$ University of New South Wales, Sydney, Australia
Received December 15, 2008

**Abstract**—The procedure for the calculation of the embedded atom model (EAM) potential, which involves the use of data on the structure of liquid metal in the vicinity of the melting temperature and of the results of impact tests, is applied to uranium. The use of the method of molecular dynamics and of the EAM potential produces good agreement with experiment as regards the structure, density, and potential energy of liquid metal at temperatures up to 5000 K, as well as along the shock adiabat up to pressures of ~360 GPa. The thermodynamic properties of solid (bcc) and liquid uranium are determined at pressures up to 470 GPa and temperatures up to 12 000 K. The predicted value of bulk modulus of liquid at 1406 K is close to the actual value. The self-diffusion coefficient under isobaric heating increases with temperature by the power law with exponent of ~2.103. The Stokes–Einstein relation is used to determine the dynamic viscosity at temperatures up to 6000 K. The obtained potential is not quite adequate for describing crystalline uranium under normal conditions. The melting temperature of uranium with EAM potential is equal to $1455 \pm 2$ K and somewhat higher than real. The melting temperature monotonically increases with pressure and reaches the value of 7342 K at 444 GPa. For obtaining agreement with experimental data for energy of uranium along the $p=0$ isobar, it is assumed that an additional contribution to energy emerges at elevated temperatures, which is due to excitation of atomic electrons and leads to a high heat capacity: it may be as high as almost 100 kJ/mol at 5000 K. This contribution further causes a high heat capacity of highly compressed states of uranium.

DOI: 10.1134/S0018151X10030107

## INTRODUCTION
It is the objective of the present study to fit an interparticle potential that would enable one to obtain agreement with literature data for the thermodynamic properties of uranium in a wide range of pressures and temperatures and to calculate these properties by the method of molecular dynamics at pressures up to 470 GPa and temperatures up to 12 000 K. For this purpose, the embedded atom model (EAM) potential is introduced; in this model, collective interaction is included. The potential energy of metal is written as a function of coordinates of ions [1, 2],

$$
U_{\text {pot }}=\sum_{i} \Phi\left(\rho_{i}\right)+\sum_{i<j} \varphi\left(r_{i j}\right). \tag{1}
$$

Here, $\Phi(\rho_{i})$ is the "embedding potential" of the $i$th ion, which depends on the effective electron density $\rho$ (dimensionless) at the point of location of the center of ion, and the second sum over pairs of ions contains an ordinary pair potential. The presence of electron subsystem is implicitly taken into account in terms of effective potentials $\Phi(\rho)$ and $\varphi(r)$, so that the characteristics of metal such as ion charge and electron spectrum do not appear in the formal scheme of the method. The "effective electron density" at the point of location of atom is developed by the surrounding atoms and is determined by the formula $\rho_{i}=\sum_{j} \psi(r_{i j})$, where $\psi(r_{i j})$ is the contribution to electron density by the number $j$ neighbor. Three fitting functions $\Phi(\rho)$, $\varphi(r)$, and $\psi(r)$ are used in the calculations; these functions are taken to be independent of temperature and density. In this study, the procedure for the calculation of EAM potential is employed, which was suggested in [3–5].

Models of uranium with interparticle potential (1) are constructed using the method of molecular dynamics. In so doing, the energy and pressure of the system are calculated relatively readily. More complex procedures are to be employed for the calculation of entropy and Helmholtz energy, in which either a series of models are constructed with the potential gradually decreasing to zero (i.e., with the transition of the model to the state of ideal gas for which the entropy is known), or a gradual transition is organized to this state from a crystal lattice for which the density of vibrational states and, accordingly, the entropy, may be calculated. We performed no calculation of entropy.

## CALCULATION PROCEDURE
In simulating a metal using the method of molecular dynamics (MD), the total force acting on atom $i$ is

<table><thead><tr><td colspan="2"><b>No.</b></td><td><b>$1^{*}$</b></td><td><b>$2^{*}$</b></td><td><b>3</b></td><td><b>4</b></td><td><b>5</b></td><td><b>6</b></td><td><b>7</b></td><td><b>8</b></td><td><b>9</b></td><td><b>10</b></td><td><b>11</b></td><td><b>12</b></td><td><b>13</b></td></tr><tr><td colspan="2"><b>T, K</b></td><td><b>298</b></td><td><b>298</b></td><td><b>1406</b></td><td><b>1500</b></td><td><b>2000</b></td><td><b>2500</b></td><td><b>3000</b></td><td><b>3500</b></td><td><b>4000</b></td><td><b>4500</b></td><td><b>5000</b></td><td><b>6000</b></td><td><b>7000</b></td></tr></thead><tbody><tr><td rowspan="2"><b>$d,g/cm^{3}$</b></td><td><b>[11]</b></td><td><b>19.05</b></td><td><b>19.14</b></td><td><b>17.226</b></td><td><b>17.06</b></td><td><b>16.18</b></td><td><b>15.33</b></td><td><b>14.53</b></td><td><b>13.76</b></td><td><b>13.03</b></td><td><b>12.3</b></td><td><b>11.7</b></td><td><b>10.4</b></td><td><b>9.2</b></td></tr><tr><td><b>[10]</b></td><td><b>—</b></td><td><b>—</b></td><td><b>—</b></td><td><b>17.11</b></td><td><b>16.04</b></td><td><b>—</b></td><td><b>—</b></td><td><b>—</b></td><td><b>—</b></td><td><b>—</b></td><td><b>—</b></td><td><b>—</b></td><td><b>—</b></td></tr><tr><td rowspan="2"><b>P, GPa</b></td><td><b>EAM</b></td><td><b>−0.295</b></td><td><b>0.002</b></td><td><b>0.001</b></td><td><b>−0.010</b></td><td><b>−0.014</b></td><td><b>0.055</b></td><td><b>0.018</b></td><td><b>−0.014</b></td><td><b>0.026</b></td><td><b>−0.294</b></td><td><b>0.135</b></td><td><b>0.477</b></td><td><b>0.394</b></td></tr><tr><td><b>experiment</b></td><td><b>~0</b></td><td><b>~0</b></td><td><b>~0</b></td><td><b>~0</b></td><td><b>~0</b></td><td><b>~0</b></td><td><b>~0</b></td><td><b>~0</b></td><td><b>~0</b></td><td><b>~0</b></td><td><b>~0</b></td><td><b>0.003?</b></td><td><b>0.008?</b></td></tr><tr><td colspan="2"><b>$\langle ρ\rangle $</b></td><td><b>1.127</b></td><td><b>1.136</b></td><td><b>1.000</b></td><td><b>0.987</b></td><td><b>0.926</b></td><td><b>0.870</b></td><td><b>0.814</b></td><td><b>0.766</b></td><td><b>0.720</b></td><td><b>0.677</b></td><td><b>0.648</b></td><td><b>0.579</b></td><td><b>0.557</b></td></tr><tr><td rowspan="4"><b>U, kJ/mol</b></td><td><b>$-U_{EAM}$</b></td><td><b>526.46</b></td><td><b>526.58</b></td><td><b>486.07</b></td><td><b>482.87</b></td><td><b>466.43</b></td><td><b>450.54</b></td><td><b>435.51</b></td><td><b>420.25</b></td><td><b>405.29</b></td><td><b>391.43</b></td><td><b>376.83</b></td><td><b>347.31</b></td><td><b>319.42</b></td></tr><tr><td><b>$U_{el}$</b></td><td><b>0.0</b></td><td><b>0.0</b></td><td><b>16.60</b></td><td><b>18.12</b></td><td><b>26.52</b></td><td><b>35.65</b></td><td><b>45.67</b></td><td><b>56.71</b></td><td><b>68.94</b></td><td><b>82.51</b></td><td><b>97.56</b></td><td><b>$132.7^{**}$</b></td><td><b>$175.7^{**}$</b></td></tr><tr><td><b>$U_{EAM}+U_{el}$</b></td><td><b>−526.46</b></td><td><b>−526.58</b></td><td><b>−469.10</b></td><td><b>−464.52</b></td><td><b>−440.16</b></td><td><b>−415.22</b></td><td><b>−390.02</b></td><td><b>−363.48</b></td><td><b>−336.11</b></td><td><b>−308.72</b></td><td><b>−279.48</b></td><td><b>−214.6</b></td><td><b>−143.7</b></td></tr><tr><td><b>$U_{exp}$</b></td><td><b>−526.8</b></td><td><b>−526.8</b></td><td><b>−469.5</b></td><td><b>−464.8</b></td><td><b>−439.9</b></td><td><b>−414.9</b></td><td><b>−389.8</b></td><td><b>−363.5</b></td><td><b>−336.4</b></td><td><b>−308.9</b></td><td><b>−279.3</b></td><td><b>?</b></td><td><b>?</b></td></tr><tr><td rowspan="2"><b>$K_{T},GPa$</b></td><td><b>EAM</b></td><td><b>—</b></td><td><b>64.2</b></td><td><b>$34.4\pm 1.7$</b></td><td><b>$31.7\pm 0.5$</b></td><td><b>$22.8\pm 2.3$</b></td><td><b>$18.7\pm 1.4$</b></td><td><b>$17.3\pm 2.2$</b></td><td><b>$14.8\pm 2.6$</b></td><td><b>$10.1\pm 5.5$</b></td><td><b>$4.9\pm 1.8$</b></td><td><b>$4.4\pm 3.8$</b></td><td><b>—</b></td><td><b>—</b></td></tr><tr><td><b>experi- ment</b></td><td><b>100</b></td><td><b>—</b></td><td><b>34.4</b></td><td><b>—</b></td><td><b>—</b></td><td><b>—</b></td><td><b>—</b></td><td><b>—</b></td><td><b>—</b></td><td><b>—</b></td><td><b>—</b></td><td><b>—</b></td><td><b>—</b></td></tr><tr><td colspan="2"><b>$D×10^{5},$ $cm^{2}/s$</b></td><td><b>—</b></td><td><b>—</b></td><td><b>1.99</b></td><td><b>2.25</b></td><td><b>5.06</b></td><td><b>7.95</b></td><td><b>11.1</b></td><td><b>15.7</b></td><td><b>19.3</b></td><td><b>24.7</b></td><td><b>28.8</b></td><td><b>43.7</b></td><td><b>73.2</b></td></tr><tr><td rowspan="2"><b>Viscosity, cP</b></td><td><b>by Eq. (14)</b></td><td><b>—</b></td><td><b>—</b></td><td><b>6.59</b></td><td><b>6.16</b></td><td><b>3.65</b></td><td><b>2.91</b></td><td><b>2.50</b></td><td><b>2.06</b></td><td><b>1.92</b></td><td><b>1.87</b></td><td><b>1.60</b></td><td><b>1.27</b></td><td><b>—</b></td></tr><tr><td><b>experiment</b></td><td><b>—</b></td><td><b>—</b></td><td><b>—</b></td><td><b>6.59 [18] 8.75 [18]</b></td><td><b>—</b></td><td><b>3.90 [28]</b></td><td><b>—</b></td><td><b>2.06 [28]</b></td><td><b>—</b></td><td><b>1.50 [28]</b></td><td><b>—</b></td><td><b>—</b></td><td><b>—</b></td></tr></tbody></table>

* Crystalline bcc uranium.
**Extrapolated.

<table><thead><tr><td><b>T, K</b></td><td><b>1406</b></td><td><b>1500</b></td><td><b>2000</b></td><td><b>2500</b></td><td><b>3000</b></td><td><b>3500</b></td><td><b>4000</b></td><td><b>4500</b></td><td><b>5000</b></td><td><b>6000</b></td></tr></thead><tbody><tr><td><b>$-U_{pot}$</b></td><td><b>486.56</b></td><td><b>483.31</b></td><td><b>465.30</b></td><td><b>446.62</b></td><td><b>427.20</b></td><td><b>407.01</b></td><td><b>386.04</b></td><td><b>364.28</b></td><td><b>341.72</b></td><td><b>294.20</b></td></tr><tr><td><b>-U</b></td><td><b>469.0</b></td><td><b>464.6</b></td><td><b>440.4</b></td><td><b>415.4</b></td><td><b>389.8</b></td><td><b>363.4</b></td><td><b>336.2</b></td><td><b>308.2</b></td><td><b>279.4</b></td><td><b>219.4</b></td></tr></tbody></table>

obtained by differentiating the total energy with respect to coordinates of this atom. This total force may be presented in the form of the sum of effective pair forces. In the case of a single-component system, we have the following for effective pair force of the $i-j$ pair:

$$
F_{i j}=-\left[\left.\left(\frac{\partial \Phi_{i}}{\partial \rho}\right)\right|_{\rho_{i}}+\left.\left(\frac{\partial \Phi_{j}}{\partial \rho}\right)\right|_{\rho_{j}}\right] \frac{\partial \psi}{\partial r}\left|_{r_{i j}}-\frac{\partial \varphi(r)}{\partial r}\right|_{r_{i j}} \quad(2)
$$

The first sum is the result of the effect of embedding potential, and the second sum is the contribution made by pair potential $\varphi(r)$ selected in the Morse form (see below). Similarly [3-5], in this study we write the functions $\Phi(\rho)$ and $\psi(r)$ for liquid uranium in the following form:

$$
\psi(r)=p_{1} \exp \left(-p_{2} r\right), \quad(3)
$$

$$
\Phi(\rho)=a_{1}+c_{1}\left(\rho-\rho_{0}\right)^{2} \text { at } \rho_{1}<\rho<\rho_{8}, \quad(4)
$$

$$
\begin{gathered}
\Phi(\rho)=a_{i}+b_{i}\left(\rho-\rho_{i-1}\right) \\
+c_{i}\left(\rho-\rho_{i-1}\right)^{2} \text { at } \rho_{i}<\rho<\rho_{i-1}(i=2-7),
\end{gathered}
$$

$$
\begin{gathered}
\Phi(\rho)=\left[a_{8}+b_{8}\left(\rho-\rho_{7}\right)+c_{8}\left(\rho-\rho_{7}\right)^{2}\right]\left[2 \frac{\rho}{\rho_{7}}-\left(\frac{\rho}{\rho_{7}}\right)^{2}\right] \\
\text { at } \rho<\rho_{7},
\end{gathered}
$$

$$
\begin{gathered}
\Phi(\rho)=a_{9}+b_{9}\left(\rho-\rho_{8}\right)+c_{9}\left(\rho-\rho_{8}\right)^{m} \\
\text { at } \rho_{8} \leq \rho \leq \rho_{9},
\end{gathered}
$$

$$
\Phi(\rho)=a_{10}+b_{10}\left(\rho-\rho_{9}\right)+c_{10}\left(\rho-\rho_{9}\right)^{n} \text { at } \rho \geq \rho_{9}, \quad(8)
$$

in so doing, $\rho_{0}=1$; at $\rho=\rho_{i}$, the function $\Phi(\rho)$ and its first derivative are continuous. As a result, the EAM potential is defined by the parameters $p_{1}, p_{2}, a_{1}, c_{1}-$ $c_{10}, \rho_{1}-\rho_{9}, m$, and $n$, which make it in principle possible to fit to experimental data the properties such as density, potential energy (atomization energy), bulk modulus $K_{T}$, and coefficient of thermal expansion. Expressions (4)-(6) are used in simulating the states of lower density, and expressions (7) and (8)-in simulating the states of higher density.

In further calculations, the parameter $p_{2}$ in Eq. (3) was a fitting one. The parameter $p_{1}$ was determined so as to obtain the value of $\langle\rho\rangle=\rho_{0}=1$ for the model of liquid at melting temperature. In the stage of selection of potentials, the sum of derivatives $s=\partial \Phi_{i}(\rho) / \partial \rho+$ $\partial \Phi_{j}(\rho) / \partial \rho$ in Eq. (2) may be approximately replaced by the average value of this sum over all particles $2 \partial \Phi(\rho) / \partial \rho$ at $\rho=\langle\rho\rangle$. Then, Eq. (2) for the total effective force may be written as

$$
F(r)=-\frac{d \varphi_{\text {total }}}{d r}=-2 \frac{d \Phi(\rho)}{d \rho} \frac{d \psi}{d r}-\frac{d \varphi}{d r} .
$$

Here, $\varphi_{\text {total }}$ is the total effective potential which defines the structure of liquid, and the derivative $d \Phi(\rho) / d \rho$ is taken at $\rho=\langle\rho\rangle$. In accordance with formula (4), $\partial \Phi(\rho) / \partial \rho=0$ at $\rho=\rho_{0}=1$, and we obtain from Eq. (9) that the forces of interparticle interaction in the vicinity of the melting temperature are in fact defined only by pair contribution. In the calculations of the properties of uranium using the MD method, the average effective electron density $\langle\rho\rangle$ varied in rather wide limits from 0.25 to 2.8 (see below), and the interparticle forces were calculated by formula (2).

## LIQUID URANIUM
### Experimental Data for Uranium
The estimates of the critical temperature of uranium exhibit significant scatter (from 6000 to 14 000 K [6-9]). For example, according to Martynyuk [6], the critical parameters of uranium are as follows: $T_{c}=$ $9900 \mathrm{~K}, p_{c}=137.6 \mathrm{MPa}$, and the critical density is $2.743 \mathrm{~g} / \mathrm{cm}^{3}$. The density of liquid uranium was investigated in a number of studies at temperatures up to $5400 \mathrm{~K}$, and the results are summarized in [7, 10-12]. Shpil'rain et al. [10] measured the density of liquid uranium in a precision static experiment in the range $T=1460-2100 \mathrm{~K}$ with probable error of $0.75 \%$. Fokin [11] thoroughly analyzed the available literature data on the density of liquid uranium. The data of $[10,11]$ are given in Table 1. Apparently, the structure of liquid uranium was not investigated by diffraction methods.

The literature data on heat capacity and enthalpy of liquid uranium are characterized by significant scatter. According to Gathers [7], the variation of enthalpy under heating from $298 \mathrm{~K}$ to temperature $T$ (at $2000 \leq$ $T \leq 5400 \mathrm{~K})$ is $\Delta H_{\text {heat }}=-0.2337+2.8813 \times 10^{-4} T$, $\mathrm{MJ} / \mathrm{kg}$. This means that the heat capacity of liquid uranium is independent of temperature and equal to $68.6 \mathrm{~J} /(\mathrm{mol} \mathrm{K})$. On the other hand, according to [12], the heat capacity of liquid uranium (at $T \leq 6000 \mathrm{~K}$ ) is described by the equation $C_{p}=42.144+3.232 x+$ $2.07 / x^{2}$, where $x=T / 1000$. These values are much lower than the data of Gathers [7]. For example, at $2000 \mathrm{~K}$, the heat capacity according to [12] is equal to $49.13 \mathrm{~J} /(\mathrm{mol} \mathrm{K})$. The data of [12] will be employed below.

It is important that the heat capacity of liquid ura- nium is abnormally high compared to ordinary value ($\cong 3R$, Dulong and Petit law), same as the heat capac- ity of uranium vapor at elevated temperatures signifi- cantly exceeds the heat capacity of monatomic ideal gas $C_{p}=(5/2)R=23.693$ J/(mol K) (for example, $C_{p}=$ 36.43 J/(mol K) at 2000 K and 55.41 J/(mol K) at 4000 K [12]). This is explained by the appreciable importance of electron contribution to heat capacity; this contribution further increases with temperature. At 298 K, the heat capacity of uranium vapor is close to $(5/2)R$, because electron excitations are still low here. The presence of this contribution must be taken into account in performing molecular-dynamic calcu- lations.

In the classical MD method, the internal energy $U$ consists of kinetic energy $(3/2)RT$ and potential energy $U_{\text{pot}}$ ($U=U_{\text{pot}}+(3/2)RT$). The form of poten- tial energy in the EAM is given in Eq. (1), whence one can see that the EAM potential is defined by interpar- ticle interaction. Therefore, for uranium, the expres- sion for internal energy of mole of metal in the EAM must be transformed to
$$
\begin{aligned}
U & =U_{\mathrm{EAM}}+U_{\mathrm{el}}=(3 / 2) R T+U_{\mathrm{pot}} \\
& =(3 / 2) R T+\sum_{i} \Phi\left(\rho_{i}\right)+\sum_{i<j} \varphi\left(r_{i j}\right)+U_{\mathrm{el}},
\end{aligned} \quad(10)
$$
where $U_{\text{el}}$ is the electron contribution. We assume that this contribution is independent of the coordinates of particles and does not affect the interparticle interac- tion and the pressure of the system. This contribution may include both the thermal energy of conduction electrons and the excitation energy of atomic elec- trons. The contribution associated with the excitation of conduction electrons was taken into account previ- ously, for example, in calculations of shock compres- sion of lithium, sodium, and potassium by the pseudo- potential method [13]. The contribution associated with the excitation of atomic electrons is taken into account in MD calculations for the first time in the present study.

The average value of $U$ (formula (10)) in molecu- lar-dynamic run is ordinary thermodynamic internal energy. The system pressure in the method of molecu- lar dynamics is calculated by the statistical-mechani- cal "virial theorem",
$$p V=N k T-(1 / 3) \sum_{i<j} \mathbf{r}_{i j} \mathbf{F}_{i j},$$
where $\mathbf{r}_{i j}=\mathbf{r}_{i}-\mathbf{r}_{j}$ is the vector connecting ions $i$ and $j$, and $\mathbf{F}_{i j}$ is the total force with which the $i$ th ion acts on the $j$ th ion (2).

We selected the actual potential energy of uranium gas at 298.15 K (hereinafter referred to as "standard gas") as the reference point. The standard enthalpy of monatomic uranium gas at 298.15 K is equal to $533 \pm$ 8 kJ/mol [14, 15]. In view of the fact that the sublima- tion heat is $\Delta H_{\text{evap}}=\Delta U_{\text{evap}}+RT$ ($R$ is the gas con- stant), we find the value of $\Delta U_{\text{evap}}$ of uranium at 298 K: $\Delta U_{\text{evap}}=-U_{\text{pot}}=530.52$ kJ/mol and $U=U_{\text{pot}}+(3/2)R \times$ 298/1000 = -526.8 kJ/mol. Then we can use the data of [12] and compute the enthalpy $\Delta H_{\text{heat}}$ under heating of uranium from 298 K to $T$, calculate $\Delta U_{\text{heat}}(T)=$ $\Delta H_{\text{heat}}(T)$ (because the pressure is close to zero), and find the internal energy of liquid with respect to stan- dard gas $U=-526.800+\Delta H_{\text{heat}}$ in kJ/mol. For the melting temperature of liquid uranium according to the data of [12], we have $U_{\text{pot}}=-486.560$ kJ/mol and $U=-469.000$ kJ/mol. The reference book [12] gives, at 1406 K, the heat of evaporation of uranium of 504.219 kJ/mol. For the variation of potential energy upon evaporation, we have $U_{\text{pot}}=492.53$ kJ/mol. This value is a little higher than that in the case of transition to standard gas (486.56), because the energy of real uranium gas at $T>298$ K is higher than that of stan- dard gas because of higher heat capacity.

We use the data of [12] and find $\Delta H_{\text{heat}}$ under heat- ing from 1406 K to $T$, and then $\Delta U_{\text{heat}}$, $U_{\text{pot}}$, and $U$. The results are given in Table 2.

The bulk modulus of solid uranium at 298 K is $K_{T} \cong$ 100 GPa [15]. According to the estimate of Tekuchev [16], the adiabatic compressibility of liquid at 1406 K is $\beta_{s}=2.24 \times 10^{-11} \mathrm{~Pa}^{-1}$ and the adiabatic modulus is $K_{s}=44.6$ GPa. Accordingly, the isothermal compress- ibility $\beta_{T}=2.91 \times 10^{-11} \mathrm{~Pa}^{-1}$ and $K_{T}=34.4$ GPa. Boivineau et al. [17] used experimental data on sound velocity for calculating the values of isothermal coeffi- cient of compressibility $\beta_{T}$ for liquid uranium at tem- peratures of 1810-3300 K and pressure of ~1 kbar. In this range of parameters, the value of $\beta_{T}$ varies from0.0024 to $0.00351 / kbar$ , and that of modulus $K_{T}$  from 41.7 to 28.3 GPa.

Wittenberg [18] estimated the properties of liquid uranium at melting temperature using the hard-sphere model. The values of hard sphere diameter $\sigma=2.75 \AA$ and of packing factor $\eta=0.4763$ were obtained. The estimation by the formula for hard-sphere model
$$\frac{N}{V} \beta_{T} k T=\frac{(1-\eta)^{4}}{1+4 \eta+4 \eta^{2}-4 \eta^{3}+\eta^{4}}$$
gives the values of compressibility $\beta_{T}=2.59 \times 10^{-11} \mathrm{~Pa}^{-1}$ and of modulus $K_{T}=38.6$ GPa, which is just a little lower than the estimate of Tekuchev [16]. In view of the probable error of the data of [17] of $20-30 \%$ , the value of modulus of 34.4 GPa may be taken as basic.

### Fitting the Parameters of Pair Contribution to Uranium Potential

The starting point was the construction of a model of liquid uranium at 1406 K by the MD method (Verlet algorithm) [19, 20] with the Morse pair potential,
$$\varphi_{\mathrm{M}}(r)=\varepsilon\left[e^{-2 \alpha(r / d-1)}-2 e^{-\alpha(r / d-1)}\right].\qquad(11)$$


![](./images/811775952748019712_1.jpg)

Fig. 1. Morse pair potential for liquid uranium (11).

![](./images/811775952748019712_2.jpg)

Fig. 2. Embedding potential for liquid uranium (3)-(8).

Here, $\varepsilon$ is the depth of minimum of potential, $d$ is the coordinate of the minimum, and $\alpha$ is the parameter defining the curvature of potential at the minimum. Because this potential includes three parameters, the fitting of parameters may produce correct values of density, of modulus $K_{T}$, and of topological parameter for dense non-crystalline structures $\rho_{t}=r_{1}(N/V)^{1/3} \cong 1.08$ [21] (where $r_{1}$ is the coordinate of the first peak of pair correlation function) in the vicinity of the melting temperature. For loose structures, $\rho_{t}$ is less than unity (for example, for vitreous silica, $\rho_{t}=0.930$). The computer model contained 1968 atoms in the basic cube with edge length of $35.610$ Å. The density of the model was equal to the actual density at $1406$ K ($17.226$ g/cm$^{3}$ [11]). The cut-off radius of interatomic interaction was taken to be equal to $12.20$ Å. The time step was $0.01\ t_{0}$, where $t_{0}=1.571\times10^{-13}$ s is the internal time unit. Given the parameters $\varepsilon=0.209$ eV, $d=3.3318$ Å, and $\alpha=4.100$, the MD method was used for constructing a model with low pressure ($0.025$ GPa) and good value of topological parameter $\rho_{1}=1.073$. In view of expression (9) and condition $\partial\Phi(\rho)/\partial\rho=0$ at $\rho=\rho_{0}=1$, the effective pair potential (11) given in Fig. 1 was directly employed as the EAM pair potential.

### Fitting the Parameters of Embedding Potential at Pressure $p\sim0$

This fitting was performed for the properties of liquid uranium at $1406$ K. The coefficient $p_{2}$ was estimated by the approximate equality $r_{1}p_{2}\cong\text{const}$ for liquid metals [3-5] with subsequent correction; the result is $p_{2}=1.3850$. The coefficient $p_{1}$ was determined from the following condition: at $1406$ K, the average value of effective electron density on atoms is $\langle\rho\rangle=1.0000$; this gave $p_{1}=5.5619$. The coefficient $a_{1}$ was fitted by the atomization energy of uranium at normal pressure. Because $a_{1}$ is associated with the choice of reference point for the $U_{\text{el}}$ contribution, it is assumed that, at $298$ K, $U_{\text{el}}=0$. Then, at $298$ K and $a_{1}=-3.5659$, we have $U=-526.58$ kJ/mol, which is very close to the actual value (see Table 1). The coefficient $c_{1}$ was determined by the modulus $K_{T}$ at $1406$ K. The actual value of modulus $K_{T}=34.4$ GPa is obtained at $c_{1}=0.2753$.

The values of $\rho_{i}$ and coefficients $c_{i}$ were fitted in view of the temperature dependence of density of liquid uranium [7, 11]. The parameters of embedding potential at high densities ($\rho_{8}$, $\rho_{9}$, $c_{9}$, $c_{10}$, $m$, $n$) were determined by the data obtained under shock compression of uranium [22-25] (see below).

The coefficients $a_{i}$ and $b_{i}$ were calculated from the condition of continuity of functions $\Phi(\rho)$ and $d\Phi/d\rho$ at $\rho=\rho_{i}$. As a result, the following parameters of EAM potential were found: $p_{1}=5.5619$, $p_{2}=1.3850$, $\rho_{1}=0.900$, $\rho_{2}=0.800$, $\rho_{3}=0.700$, $\rho_{4}=0.600$, $\rho_{5}=0.500$, $\rho_{6}=0.400$, $\rho_{7}=0.100$, $\rho_{8}=1.20$, $\rho_{9}=2.00$, $a_{1}=-3.5659$, $c_{1}=0.2753$, $c_{2}=-0.100$, $c_{3}=-0.200$, $c_{4}=3.65$, $c_{5}=-1.850$, $c_{6}=0.500$, $c_{7}=10.60$, $c_{8}=0.050$, $c_{9}=1.62$, $c_{10}=2.24$, $m=1.80$, and $n=1.71$. Figure 3 gives the embedding potential $\Phi(\rho)$ as a function of $\rho$.

The form of $U_{\text{el}}$ function may be found as follows. At $298$ K, it may be taken to be zero, because the heat capacity of uranium under these conditions is close to $3R$. Under conditions of heating of actual uranium from $298$ to $1406$ K (above the melting point), the variation of energy is equal to $64.139-6.364=57.775$ kJ/mol [12]. For uranium models at these temperatures, we have the energy difference of $40.80$ kJ/mol (see Table 1). The difference of $57.775-40.80=16.98$ kJ/mol will be attributed to the $U_{\text{el}}$ contribution at $1406$ K. Agreement with experimental data for energy of uranium along the $p\cong0$ isobar at temperatures from $1406$ to $5000$ K is attained by selecting the $U_{\text{el}}$ function in the form

$$
\begin{aligned}
U_{\text{el}}[\text{kJ/mol}] &= 2.021783\times10^{-10}T^{3} \\
&+ 2.447619\times10^{-7}T^{2} \\
&+ 1.408133\times10^{-2}T - 4.239155.
\end{aligned} \tag{12}
$$

![](./images/811775952748019712_3.jpg)

Fig. 3. Pair correlation functions for liquid uranium:
(1) 1406 K, (2) 2000 K, (3) 3000 K. The densities are given
in the third column of Table 1. The curves are shifted on
the ordinate axis.

This contribution gives an addition to heat capacity
of uranium, which is equal to
$$
\begin{gathered}
C_{\mathrm{el}}[\mathrm{J} /(\mathrm{mol} \mathrm{K})] \\
=6.065 \times 10^{-7} T^{2}+4.895 \times 10^{-4} T+14.081.
\end{gathered} \tag{13}
$$

### Simulation of Crystalline Uranium with EAM Potential

For checking the validity of EAM potential for the
description of solid uranium, the MD method was
used to construct models with bcc lattice (hypotheti-
cal) at a temperature of 298 K (states 1 and 2 in Table 1).
Each model contained 1024 particles in the basic
cube. At 298 K and close-to-zero pressure, the density of
the model is equal to $19.148 \mathrm{~g} / \mathrm{cm}^{3}$ and exceeds the nor-
mal density of uranium (19.05) by $0.5 \%$. In so doing, the
internal energy of the model is $-526.58 \mathrm{~kJ} / \mathrm{mol}$, which is
almost equal to the actual value of $-526.8 \mathrm{~kJ} / \mathrm{mol}$. The
predicted value of modulus $K_{T}$ at zero pressure is
appreciably lower than the actual value. Therefore, the
EAM potential fitted for liquid is not quite adequate
for the bcc phase under close-to-normal conditions.

### Simulation of Liquid Uranium by the MD Method along the $p \cong 0$ Isobar

EAM potential (3)-(6) was used to construct, by
the MD method, a series of liquid uranium models at
temperatures of 1406 to 6000 K with real values of
density [7, 10-12]. The models contained 1968 atoms
in the basic cube. The cut-off radius of all contribu-
tions to the potential was equal to $12.20 \AA$. The prop-
erties were averaged in runs 1000 to 15 000 time steps
long. In states 3-10, the system pressure was very low
on the atomic scale. At 5000-7000 K, the EAM
potential a little overstates the pressure. This overstate-
ment at 5000 K is possibly associated with the inaccu-
racy of experimental determination of density. If the
density at 5000 K is 11.5 instead of $11.7 \mathrm{~g} / \mathrm{cm}^{3}$ (the dif-
ference of less than $2 \%$ ), the pressure of the model will
already be negative $(-0.054 \mathrm{GPa})$.

Table 1 gives the internal energy $U$, the modulus $K_{T}$,
and the self-diffusion coefficient $D$. One can see in the
table that agreement with experiment as regards
potential energy at $T \leq 5000 \mathrm{~K}$ is very good. The mod-
ulus $K_{T}=-V(\partial P / \partial V)_{T}$ was determined by the varia-
tion of pressure with a minor variation of the edge
length of the basic cube. At 1406 K, the predicted
value of $K_{T}$ agrees well with the experimentally
obtained value. With the temperature increasing to
$5000 \mathrm{~K}, K_{T}$ decreases by a factor of approximately
eight.

### Liquid Uranium Structure

Figure 3 gives the PCFs of liquid uranium models
at 1406, 2000, and 3000 K. They have the form common
for simple metals. Table 3 gives the structural characteris-
tics of liquid uranium, namely, the coordinate of the first
peak of PCF $r_{1}$, the height of this peak $g\left(r_{1}\right)$, the coordi-

Table 3. The structural characteristics of uranium models, obtained by the MD method with EAM potential (3)-(6). States with close-to-zero pressure

<table>
  <thead>
    <tr>
      <th rowspan="2">No.</th>
      <th rowspan="2">T, K</th>
      <th rowspan="2">d, g/cm³</th>
      <th colspan="2">First peak of PCF</th>
      <th rowspan="2">Coordination number</th>
      <th rowspan="2">ρᵣ</th>
    </tr>
    <tr>
      <th>r₁, Å</th>
      <th>g(r₁)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>1406</td>
      <td>17.226</td>
      <td>2.99</td>
      <td>2.67</td>
      <td>13.2 ± 1.1</td>
      <td>1.073</td>
    </tr>
    <tr>
      <td>2</td>
      <td>1500</td>
      <td>17.06</td>
      <td>3.00</td>
      <td>2.59</td>
      <td>13.4 ± 1.1</td>
      <td>1.087</td>
    </tr>
    <tr>
      <td>3</td>
      <td>2000</td>
      <td>16.18</td>
      <td>3.00</td>
      <td>2.22</td>
      <td>12.8 ± 1.2</td>
      <td>1.019</td>
    </tr>
    <tr>
      <td>4</td>
      <td>2500</td>
      <td>15.33</td>
      <td>3.01</td>
      <td>2.08</td>
      <td>13.0 ± 1.4</td>
      <td>1.003</td>
    </tr>
    <tr>
      <td>5</td>
      <td>3000</td>
      <td>14.53</td>
      <td>3.02</td>
      <td>1.92</td>
      <td>12.9 ± 1.4</td>
      <td>0.998</td>
    </tr>
    <tr>
      <td>6</td>
      <td>3500</td>
      <td>13.76</td>
      <td>3.03</td>
      <td>1.81</td>
      <td>12.3 ± 1.5</td>
      <td>0.980</td>
    </tr>
    <tr>
      <td>7</td>
      <td>4000</td>
      <td>13.03</td>
      <td>3.04</td>
      <td>1.70</td>
      <td>13.1 ± 1.7</td>
      <td>0.939</td>
    </tr>
    <tr>
      <td>8</td>
      <td>4500</td>
      <td>12.3</td>
      <td>3.02</td>
      <td>1.68</td>
      <td>12.4 ± 1.8</td>
      <td>0.933</td>
    </tr>
  </tbody>
</table>

HIGH TEMPERATURE Vol. 48 No. 3 2010

nation number, and the topological parameter $\rho_{r}$. The parameters of uranium structure are in general smoothly dependent on temperature. Above 1500 K, the liquid structure is loose and contains voids (pores).

### Diffusion Properties and Viscosity
The calculated self-diffusion coefficients of ura- nium were found by the slope of the curve of time dependence of the mean square of displacement of particles. The temperature dependence of self-diffu- sion coefficient along the $p \cong 0$ isobar (see Table 1) is well described by the power-law formula $D\left[\mathrm{cm}^{2} / \mathrm{s}\right]=$ $5.17 \times 10^{-12} T^{2.1029}$. Expressions of this type are well valid for numerous liquid metals [26].

The viscosity $\eta$ of liquid uranium may be estimated by the Stokes-Einstein relation,
$$
D=\frac{k T}{6 \pi \eta r_{a}}, \quad(14)
$$
where $r_{a}$ is the "ion radius". Good results are usually produced by the substitution of the radius of singly charged ion as $r_{a}[21,26]$. The radii of $U^{+3}(1.04 \mathring{A})$ and $U^{+4}(0.89 \mathring{A})$ ions are given for uranium in reference books. If we take the viscosity of 0.0653 P at the melt- ing temperature [18], Eq. (14) yields $r_{a}=0.792 \mathring{A}$. Table 1 gives values of viscosity calculated by Eq. (14) assuming that $r_{a}=0.792 \mathring{A}$. Under heating to 6000 K, the viscosity decreases by a factor of five.

The viscosity of liquid uranium was further mea- sured in [27-29] at temperatures up to 1520 K [28] and 1805 K [29]. The results of these studies differ by a factor of up to 1.5. The data obtained at OIVT RAN (Joint Inst. for High Temperatures, Russ. Acad. Sci.)[27] are described by the equation $\eta=$ $0.577 \exp (3823 / T)$ mPa s (with an error of up to 20-30% at temperatures above 2000 K). They are given in Table 1 with extrapolation to 4000 K. The difference between the results of MD calculations and experi- mental data does not exceed 20%.

### Estimation of Normal Melting Temperature of Uranium Models with EAM Potential
We used the "method of reheating" of defective lattice [30] for estimating the melting temperature. A model of crystalline bcc uranium with defective lattice was obtained by superposition of EAM potential onto a model of crystallized potassium 1968 particles in size. Then the resultant model was alternately heated to differ- ent temperatures under close-to-zero pressure, and iso- thermal MD runs 50 000 to 100 000 steps long were per- formed. The process of melting was monitored, with the structure factors of the model being calculated after every 5000 steps in different directions by the formula
$$
S(\mathbf{K})=\frac{1}{N}\left|\sum_{j} \exp \left(i \mathbf{K} \mathbf{R}_{j}\right)\right|^{2}.
$$

![](./images/811775952748019712_4.jpg)

Fig. 4. Pressure as a function of volume along the shock adiabat: (1) experimental data of [22, 23], (2) MD simula- tion with EAM potential (our study); $V_{0}=12.49 \mathrm{~cm}^{3} / \mathrm{mol}$.

Here, $\mathbf{R}_{i}$ denotes the radius vectors of particles of the model, $\mathbf{K}$ is the scattering vector, and $N$ is the number of particles of the model. For an ideal crystal, the max- imal value of $S(\mathbf{K})$ is $N$. The scanning of reciprocal space involved the use of 27000 values of vector $\mathbf{K}$ with a step of $0.118-0.140 \AA^{-1}$ for each projection. As a result, the melting temperature of uranium model with EAM potential may be estimated at $1455 \pm 2 \mathrm{~K}$. This value is 3.5% higher than the melting temperature of real uranium (1406 K).

### Simulation of Uranium at High Densities
In their dynamic experiments, Zhernokletov [25] and Funtikov [31] measured shock adiabats and expansion isentropes of solid uranium and shock adi- abats of porous uranium, respectively. Given in [22-24] are values of uranium pressure in states along shock adiabats up to values of ~480 GPa according to the data of Russian and foreign researchers. The experimental data of [22, 23] are given in Fig. 4 and exhibit significant scatter. Calculations involving the use of the Grüneisen model [22-24] give temperatures on the adiabat of 11 000-12 000 K. However, in reality, a significant part of the impact energy goes to increase the $U_{el}$ contribution, and the actual values of tempera- ture on the adiabat turn out to be much lower than those calculated using the Grüneisen model (seebelow). In our calculations, we assumed that the $U_{el}$  contribution does not affect the system pressure.

Two conditions served as the criteria of adequacy of the potential, namely, 1) the predicted pressure of the model is close to that found on the shock adiabat, and 2) good validity of the relation for shock wave,
$$
U_{2}-U_{1}=(1 / 2)\left(p_{1}+p_{2}\right)\left(V_{1}-V_{2}\right), \quad(15)
$$
where $V_{1}, p_{1}$, and $U_{1}$ denote the molar volume, pres sure, and energy of matter before the shock wave front,

<table>
<caption>Table 4. The properties of uranium predicted using the MD method with EAM potential (3)–(8); $N = 2000$</caption>
<thead>
<tr>
<th rowspan="2">No.</th>
<th colspan="2">Temperature, K</th>
<th rowspan="2">$Z = V/V_0$</th>
<th rowspan="2">XL, A</th>
<th colspan="2">Pressure, GPa</th>
<th colspan="5">Uranium energy, kJ/mol</th>
<th rowspan="2">$S_{\text{max}}(K)$</th>
</tr>
<tr>
<th>according to [24]</th>
<th>model</th>
<th>model</th>
<th>[22, 23]</th>
<th>$U_2 - U_1$ (15)</th>
<th>$U_2$ on adiabat</th>
<th>$U_{\text{el}}$</th>
<th>$U_2 - U_{\text{el}}$</th>
<th>model</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>—</td>
<td>298</td>
<td>1.0048</td>
<td>34.561</td>
<td>0.014</td>
<td>0</td>
<td>0</td>
<td>−526.6</td>
<td>0</td>
<td>−526.6</td>
<td>−526.58</td>
<td>1735</td>
</tr>
<tr>
<td>2</td>
<td>—</td>
<td>420</td>
<td>0.900</td>
<td>33.421</td>
<td>16.8</td>
<td>17.1</td>
<td>10.67</td>
<td>−515.9</td>
<td>1.73</td>
<td>−517.6</td>
<td>−517.3</td>
<td>1681</td>
</tr>
<tr>
<td>3</td>
<td>1094</td>
<td>810</td>
<td>0.800</td>
<td>32.135</td>
<td>51.2</td>
<td>51.3</td>
<td>64.07</td>
<td>−462.4</td>
<td>7.43</td>
<td>−469.8</td>
<td>−469.9</td>
<td>1649</td>
</tr>
<tr>
<td>4</td>
<td>1406</td>
<td>1075</td>
<td>0.768</td>
<td>31.701</td>
<td>67.6</td>
<td>67.0</td>
<td>97.07</td>
<td>−429.4</td>
<td>11.43</td>
<td>−440.8</td>
<td>−440.9</td>
<td>1661</td>
</tr>
<tr>
<td>5</td>
<td>1875</td>
<td>1170</td>
<td>0.750</td>
<td>31.451</td>
<td>78.2</td>
<td>78.0</td>
<td>116.62</td>
<td>−409.8</td>
<td>12.89</td>
<td>−422.7</td>
<td>−423.0</td>
<td>1576</td>
</tr>
<tr>
<td>6</td>
<td>3370</td>
<td>1910</td>
<td>0.718</td>
<td>30.998</td>
<td>102.2</td>
<td>103.8</td>
<td>180.33</td>
<td>−346.1</td>
<td>24.96</td>
<td>−371.1</td>
<td>−371.4</td>
<td>1398</td>
</tr>
<tr>
<td>7</td>
<td>3750</td>
<td>2540</td>
<td>0.700</td>
<td>30.736</td>
<td>120.7</td>
<td>123.2</td>
<td>230.82</td>
<td>−295.6</td>
<td>36.42</td>
<td>−332.0</td>
<td>−332.2</td>
<td>1394</td>
</tr>
<tr>
<td>8</td>
<td>4531</td>
<td>2830</td>
<td>0.693</td>
<td>30.630</td>
<td>130.0</td>
<td>132.4</td>
<td>253.84</td>
<td>−272.6</td>
<td>42.15</td>
<td>−314.8</td>
<td>−314.7</td>
<td>1342</td>
</tr>
<tr>
<td>9</td>
<td>6094</td>
<td>4010</td>
<td>0.668</td>
<td>30.260</td>
<td>170.3</td>
<td>170.4</td>
<td>353.30</td>
<td>−173.3</td>
<td>69.20</td>
<td>−242.5</td>
<td>−243.0</td>
<td>1163</td>
</tr>
<tr>
<td>10</td>
<td>7813</td>
<td>4825</td>
<td>0.653</td>
<td>30.032</td>
<td>198.2</td>
<td>197.8</td>
<td>428.63</td>
<td>−97.8</td>
<td>92.11</td>
<td>−189.9</td>
<td>−189.6</td>
<td>1038</td>
</tr>
<tr>
<td>11</td>
<td>9688</td>
<td>5515</td>
<td>0.6423</td>
<td>29.875</td>
<td>224.7</td>
<td>217.0</td>
<td>486.99</td>
<td>−5.88</td>
<td>114.4</td>
<td>−120.3</td>
<td>−120.8</td>
<td>24.0</td>
</tr>
<tr>
<td>12</td>
<td>11406</td>
<td>5810</td>
<td>0.628</td>
<td>29.644</td>
<td>252.2</td>
<td>248.9</td>
<td>578.23</td>
<td>51.8</td>
<td>125.5</td>
<td>−73.7</td>
<td>−74.1</td>
<td>24.6</td>
</tr>
<tr>
<td>13</td>
<td>—</td>
<td>9045</td>
<td>0.5834</td>
<td>28.934</td>
<td>360.2</td>
<td>371.6</td>
<td>980.9</td>
<td>454.3</td>
<td>292.8*</td>
<td>161.5</td>
<td>161.2</td>
<td>19.7</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="13">* Extrapolated by formula (12). XL is the rib length of basic cube, and $S_{\text{max}}(K)$ is the maximal value of structure factor.</td>
</tr>
</tfoot>
</table>

respectively, and the quantities with subscript 2 denote the same properties behind the front. In constructing the models using the MD method, it was taken into account that the model energy must be equal to the difference $U_2 - U_{\text{el}}$. Formula (12) was used for calculating $U_{\text{el}}$. In this method of calculation, the temperature is the quantity to be determined. Because the experimental data for pressure exhibit significant scatter (see Fig. 4), smoothed values are used in fitting the embedding potential. We constructed a series of models of different densities with 2000 atoms per basic cube and fitted the parameters of embedding potential so as to attain the best agreement with the results of impact tests for pressure and energy. As a result, the values of coefficients of embedding potential given above were obtained, namely, $\rho_8 = 1.20$, $\rho_9 = 2.00$, $m = 1.80$, $n = 1.71$, $c_9 = 1.62$, and $c_{10} = 2.24$.

<table>
<caption>Table 5. The “cold pressure” of bcc uranium at $T = 0$ K</caption>
<thead>
<tr>
<th rowspan="2">No.</th>
<th rowspan="2">$Z = V/V_0$</th>
<th rowspan="2">$U$, kJ/mol, at $T = 0$</th>
<th colspan="2">$p$, GPa</th>
</tr>
<tr>
<th>EAM, $T = 0$ K</th>
<th>according to [24]</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>0.980</td>
<td>−534.06</td>
<td>≅0</td>
<td>0</td>
</tr>
<tr>
<td>2</td>
<td>0.900</td>
<td>−527.75</td>
<td>15.18</td>
<td>19.0</td>
</tr>
<tr>
<td>3</td>
<td>0.800</td>
<td>−490.08</td>
<td>48.22</td>
<td>46.9</td>
</tr>
<tr>
<td>4</td>
<td>0.700</td>
<td>−395.87</td>
<td>109.0</td>
<td>107.8</td>
</tr>
<tr>
<td>5</td>
<td>0.653</td>
<td>−314.31</td>
<td>176.7</td>
<td>153.0</td>
</tr>
<tr>
<td>6</td>
<td>0.637</td>
<td>−276.31</td>
<td>203.9</td>
<td>168.8</td>
</tr>
<tr>
<td>7</td>
<td>0.628</td>
<td>−252.45</td>
<td>220.1</td>
<td>184.3</td>
</tr>
</tbody>
</table>

Note that, because the interparticle EAM potential is a characteristic of matter (phase), it must equally well describe both solid and porous uranium. Therefore, we did not calculate the shock adiabats of porous uranium in this study. The calculations of expansion isentropes are not discussed in this paper for the same reason.

The calculation results are given in Table 4 and in Fig. 4. One can see that the EAM potential provides for attaining adequate agreement with experimental data for uranium pressure along the shock adiabat and for very good agreement with respect to energy in view of the $U_{\text{el}}$ contribution calculated above. One can see from the maximal values of structure factors that all models 1–8 exhibit a crystalline structure under these conditions, and models 11–13 melt.

In their monograph [24], Zharkov and Kalinin give temperatures along the Hugoniot adiabat and the volume dependence of “cold pressure”, calculated using the approximate Grüneisen model. The inclusion of $U_{\text{el}}$ contribution leads to reduction of predicted temperatures along the Hugoniot adiabat almost by half (see Table 4). One can further check the adequacy of the Grüneisen model by comparing the values of “cold pressure” from [24] and the values of pressure determined with our EAM potential at absolute zero temperature. Table 5 gives values of pressure of models at $T = 0$ K (method of continuous static relaxation [21]). The cold pressure calculated with EAM potential is close to that calculated by the Grüneisen model at $Z = V/V_0 \geq 0.7$ [24]; however, it significantly exceeds the data of the Grüneisen model at lower values of $Z$. This is explained by the fact that the pressures on the adiabat employed in our calculations and in the Grüneisen


<table>
<caption>Table 6. The pressure of uranium models, GPa</caption>
<thead>
<tr>
<th rowspan="2">$T$, K</th>
<th colspan="6">$Z=V/V_0$</th>
</tr>
<tr>
<th>0.9</th>
<th>0.8</th>
<th>0.7</th>
<th>0.65</th>
<th>0.6</th>
<th>0.55</th>
</tr>
</thead>
<tbody>
<tr>
<td>300</td>
<td>16.31</td>
<td>49.35</td>
<td>110.1</td>
<td>183.0</td>
<td>277.3</td>
<td>407.2</td>
</tr>
<tr>
<td>1000</td>
<td>18.86</td>
<td>51.86</td>
<td>113.0</td>
<td>186.0</td>
<td>280.3</td>
<td>410.2</td>
</tr>
<tr>
<td>2000</td>
<td>24.78</td>
<td>55.54</td>
<td>118.0</td>
<td>190.3</td>
<td>284.5</td>
<td>414.6</td>
</tr>
<tr>
<td>3000</td>
<td>29.03</td>
<td>59.47</td>
<td>123.1</td>
<td>194.6</td>
<td>288.9</td>
<td>418.9</td>
</tr>
<tr>
<td>4000</td>
<td>32.99</td>
<td>64.49</td>
<td>128.2</td>
<td>199.1</td>
<td>293.3</td>
<td>423.3</td>
</tr>
<tr>
<td>5000</td>
<td>36.11</td>
<td>70.53</td>
<td>135.8</td>
<td>203.8</td>
<td>297.7</td>
<td>427.8</td>
</tr>
<tr>
<td>6000</td>
<td>39.09</td>
<td>73.87</td>
<td>143.8</td>
<td>214.3</td>
<td>302.8</td>
<td>432.4</td>
</tr>
<tr>
<td>7000</td>
<td>42.05</td>
<td>77.03</td>
<td>148.0</td>
<td>219.1</td>
<td>313.5</td>
<td>437.4</td>
</tr>
<tr>
<td>8000</td>
<td>44.43</td>
<td>79.67</td>
<td>152.3</td>
<td>223.5</td>
<td>318.5</td>
<td>444.6</td>
</tr>
<tr>
<td>9000</td>
<td>46.71</td>
<td>82.99</td>
<td>156.3</td>
<td>227.1</td>
<td>322.3</td>
<td>454.1</td>
</tr>
<tr>
<td>10000</td>
<td>49.44</td>
<td>85.57</td>
<td>160.0</td>
<td>231.2</td>
<td>326.4</td>
<td>458.7</td>
</tr>
<tr>
<td>11000</td>
<td>51.49</td>
<td>88.46</td>
<td>164.0</td>
<td>234.8</td>
<td>330.2</td>
<td>462.9</td>
</tr>
<tr>
<td>12000</td>
<td>53.67</td>
<td>90.89</td>
<td>167.2</td>
<td>237.8</td>
<td>334.0</td>
<td>466.7</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 7. The energy of uranium models, kJ/mol</caption>
<thead>
<tr>
<th rowspan="2">$T$, K</th>
<th colspan="6">$Z=V/V_0$</th>
</tr>
<tr>
<th>0.9</th>
<th>0.8</th>
<th>0.7</th>
<th>0.65</th>
<th>0.6</th>
<th>0.55</th>
</tr>
</thead>
<tbody>
<tr>
<td>300</td>
<td>−520.2</td>
<td>−482.4</td>
<td>−388.5</td>
<td>−300.1</td>
<td>−158.6</td>
<td>52.1</td>
</tr>
<tr>
<td>1000</td>
<td>−503.0</td>
<td>−465.4</td>
<td>−371.1</td>
<td>−282.6</td>
<td>−141.0</td>
<td>69.7</td>
</tr>
<tr>
<td>2000</td>
<td>−468.1</td>
<td>−440.5</td>
<td>−345.5</td>
<td>−257.5</td>
<td>−115.9</td>
<td>95.1</td>
</tr>
<tr>
<td>3000</td>
<td>−439.8</td>
<td>−414.2</td>
<td>−320.2</td>
<td>−232.0</td>
<td>−90.4</td>
<td>120.2</td>
</tr>
<tr>
<td>4000</td>
<td>−412.8</td>
<td>−382.5</td>
<td>−293.6</td>
<td>−206.1</td>
<td>−64.5</td>
<td>145.5</td>
</tr>
<tr>
<td>5000</td>
<td>−388.9</td>
<td>−345.2</td>
<td>−257.7</td>
<td>−178.7</td>
<td>−38.5</td>
<td>172.0</td>
</tr>
<tr>
<td>6000</td>
<td>−366.0</td>
<td>−320.8</td>
<td>−219.0</td>
<td>−127.6</td>
<td>−9.3</td>
<td>198.3</td>
</tr>
<tr>
<td>7000</td>
<td>−343.0</td>
<td>−297.3</td>
<td>−194.6</td>
<td>−99.2</td>
<td>44.8</td>
<td>226.9</td>
</tr>
<tr>
<td>8000</td>
<td>−322.7</td>
<td>−276.2</td>
<td>−169.9</td>
<td>−72.9</td>
<td>74.1</td>
<td>265.0</td>
</tr>
<tr>
<td>9000</td>
<td>−302.8</td>
<td>−251.8</td>
<td>−145.6</td>
<td>−49.8</td>
<td>98.3</td>
<td>314.3</td>
</tr>
<tr>
<td>10000</td>
<td>−280.7</td>
<td>−230.9</td>
<td>−123.4</td>
<td>−24.2</td>
<td>123.5</td>
<td>341.4</td>
</tr>
<tr>
<td>11000</td>
<td>−261.6</td>
<td>−209.0</td>
<td>−99.2</td>
<td>−0.8</td>
<td>147.3</td>
<td>367.4</td>
</tr>
<tr>
<td>12000</td>
<td>−242.0</td>
<td>−188.9</td>
<td>−78.4</td>
<td>20.0</td>
<td>171.8</td>
<td>391.1</td>
</tr>
</tbody>
</table>

model coincide, but the thermal contributions in the Grüneisen model are much higher because of higher predicted temperatures.

The obtained EAM potential was used for constructing uranium models at volume ratios $Z$ from 1 to 0.55 and temperatures up to 12 000 K. The models contained 2000 particles per basic cube. The model pressures are given in Table 6, and the energies—in table 7. The sites in Table 6, which correspond to crystalline states, are shaded.

The data of Table 7 may be used for estimating the heats of isochoric melting of uranium for different molar volumes (Table 8).

Table 9 gives the values of derivatives $(\partial p/\partial T)_V$ at constant volume. They are positive everywhere and amount to 2–4 MPa/K on the average. A slight increase in $(\partial p/\partial T)_V$ on both sides of the melting line is associated with the fact that the pressure jump in

<table>
<caption>Table 8. The heat of isochoric melting of uranium</caption>
<thead>
<tr>
<th>$Z=V/V_0$</th>
<th>0.80</th>
<th>0.70</th>
<th>0.65</th>
<th>0.60</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\Delta H_{\text{melt}}$, kJ/mol</td>
<td>12.5</td>
<td>18.6</td>
<td>~20</td>
<td>~30</td>
</tr>
</tbody>
</table>

<table>
 <thead>
  <tr>
   <th rowspan="2">
    $T$, K
   </th>
   <th colspan="6">
    $Z = {V/V_{0}}$
   </th>
  </tr>
  <tr>
   <th>
    0.9
   </th>
   <th>
    0.8
   </th>
   <th>
    0.7
   </th>
   <th>
    0.65
   </th>
   <th>
    0.6
   </th>
   <th>
    0.55
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <th>
    1000
   </th>
   <td>
    5.19
   </td>
   <td>
    3.44
   </td>
   <td>
    3.76
   </td>
   <td>
    3.08
   </td>
   <td>
    3.44
   </td>
   <td>
    4.90
   </td>
  </tr>
  <tr>
   <th>
    2000
   </th>
   <td>
    4.61
   </td>
   <td>
    4.36
   </td>
   <td>
    5.41
   </td>
   <td>
    4.58
   </td>
   <td>
    4.16
   </td>
   <td>
    3.95
   </td>
  </tr>
  <tr>
   <th>
    3000
   </th>
   <td>
    4.09
   </td>
   <td>
    4.75
   </td>
   <td>
    6.30
   </td>
   <td>
    5.53
   </td>
   <td>
    4.83
   </td>
   <td>
    3.77
   </td>
  </tr>
  <tr>
   <th>
    4000
   </th>
   <td>
    3.63
   </td>
   <td>
    4.73
   </td>
   <td>
    6.57
   </td>
   <td>
    6.02
   </td>
   <td>
    5.38
   </td>
   <td>
    4.15
   </td>
  </tr>
  <tr>
   <th>
    5000
   </th>
   <td>
    3.23
   </td>
   <td>
    4.41
   </td>
   <td>
    6.37
   </td>
   <td>
    6.12
   </td>
   <td>
    5.80
   </td>
   <td>
    4.88
   </td>
  </tr>
  <tr>
   <th>
    6000
   </th>
   <td>
    2.90
   </td>
   <td>
    3.92
   </td>
   <td>
    5.85
   </td>
   <td>
    5.92
   </td>
   <td>
    6.03
   </td>
   <td>
    5.72
   </td>
  </tr>
  <tr>
   <th>
    7000
   </th>
   <td>
    2.63
   </td>
   <td>
    3.35
   </td>
   <td>
    5.15
   </td>
   <td>
    5.48
   </td>
   <td>
    6.04
   </td>
   <td>
    6.46
   </td>
  </tr>
  <tr>
   <th>
    8000
   </th>
   <td>
    2.44
   </td>
   <td>
    2.84
   </td>
   <td>
    4.41
   </td>
   <td>
    4.88
   </td>
   <td>
    5.79
   </td>
   <td>
    6.89
   </td>
  </tr>
  <tr>
   <th>
    9000
   </th>
   <td>
    2.31
   </td>
   <td>
    2.50
   </td>
   <td>
    3.79
   </td>
   <td>
    4.21
   </td>
   <td>
    5.23
   </td>
   <td>
    6.79
   </td>
  </tr>
  <tr>
   <th>
    10 000
   </th>
   <td>
    2.26
   </td>
   <td>
    2.44
   </td>
   <td>
    3.41
   </td>
   <td>
    3.53
   </td>
   <td>
    4.34
   </td>
   <td>
    5.92
   </td>
  </tr>
  <tr>
   <th>
    11 000
   </th>
   <td>
    2.28
   </td>
   <td>
    2.77
   </td>
   <td>
    3.43
   </td>
   <td>
    2.94
   </td>
   <td>
    3.06
   </td>
   <td>
    4.08
   </td>
  </tr>
 </tbody>
</table>
Table 9. Derivatives ${({\partial p}/{\partial T})}_{V}$, MPa/K

<table>
 <thead>
  <tr>
   <th rowspan="2">
    $T$, K
   </th>
   <th rowspan="2">
    $C_{el}$ by Eq. (13)
   </th>
   <th colspan="6">
    $Z = {V/V_{0}}$
   </th>
  </tr>
  <tr>
   <th>
    0.9
   </th>
   <th>
    0.8
   </th>
   <th>
    0.7
   </th>
   <th>
    0.65
   </th>
   <th>
    0.6
   </th>
   <th>
    0.55
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <th>
    1000
   </th>
   <td>
    15.18
   </td>
   <td>
    31.6
   </td>
   <td>
    23.6
   </td>
   <td>
    21.4
   </td>
   <td>
    23.7
   </td>
   <td>
    21.5
   </td>
   <td>
    27.8
   </td>
  </tr>
  <tr>
   <th>
    2000
   </th>
   <td>
    17.49
   </td>
   <td>
    29.5
   </td>
   <td>
    28.3
   </td>
   <td>
    27.4
   </td>
   <td>
    23.6
   </td>
   <td>
    24.7
   </td>
   <td>
    23.5
   </td>
  </tr>
  <tr>
   <th>
    3000
   </th>
   <td>
    21.01
   </td>
   <td>
    27.6
   </td>
   <td>
    30.5
   </td>
   <td>
    30.8
   </td>
   <td>
    27.2
   </td>
   <td>
    27.7
   </td>
   <td>
    22.7
   </td>
  </tr>
  <tr>
   <th>
    4000
   </th>
   <td>
    22.74
   </td>
   <td>
    25.8
   </td>
   <td>
    30.6
   </td>
   <td>
    32.1
   </td>
   <td>
    31.6
   </td>
   <td>
    30.2
   </td>
   <td>
    24.4
   </td>
  </tr>
  <tr>
   <th>
    5000
   </th>
   <td>
    31.69
   </td>
   <td>
    24.2
   </td>
   <td>
    29.3
   </td>
   <td>
    31.7
   </td>
   <td>
    34.6
   </td>
   <td>
    32.2
   </td>
   <td>
    27.7
   </td>
  </tr>
  <tr>
   <th>
    6000
   </th>
   <td>
    38.20*
   </td>
   <td>
    22.7
   </td>
   <td>
    27.1
   </td>
   <td>
    30.2
   </td>
   <td>
    35.1
   </td>
   <td>
    33.4
   </td>
   <td>
    31.6
   </td>
  </tr>
  <tr>
   <th>
    7000
   </th>
   <td>
    47.23*
   </td>
   <td>
    21.5
   </td>
   <td>
    24.5
   </td>
   <td>
    28.0
   </td>
   <td>
    32.8
   </td>
   <td>
    33.6
   </td>
   <td>
    35.1
   </td>
  </tr>
  <tr>
   <th>
    8000
   </th>
   <td>
    56.81*
   </td>
   <td>
    20.6
   </td>
   <td>
    22.1
   </td>
   <td>
    25.5
   </td>
   <td>
    28.3
   </td>
   <td>
    32.7
   </td>
   <td>
    37.2
   </td>
  </tr>
  <tr>
   <th>
    9000
   </th>
   <td>
    67.61*
   </td>
   <td>
    20.1
   </td>
   <td>
    20.4
   </td>
   <td>
    23.4
   </td>
   <td>
    23.2
   </td>
   <td>
    30.4
   </td>
   <td>
    36.9
   </td>
  </tr>
  <tr>
   <th>
    10 000
   </th>
   <td>
    79.63*
   </td>
   <td>
    19.9
   </td>
   <td>
    20.1
   </td>
   <td>
    21.9
   </td>
   <td>
    19.7
   </td>
   <td>
    26.5
   </td>
   <td>
    33.2
   </td>
  </tr>
  <tr>
   <th>
    11 000
   </th>
   <td>
    92.85*
   </td>
   <td>
    20.1
   </td>
   <td>
    21.5
   </td>
   <td>
    21.6
   </td>
   <td>
    21.3
   </td>
   <td>
    20.9
   </td>
   <td>
    25.2
   </td>
  </tr>
 </tbody>
</table>
Table 10. Heat capacity $C_{V}$ of uranium models, J/(mol K) (for obtaining the total heat capacity, the amounts in columns 3–8 are to be summed with the $C_{el}$ contribution)

* Extrapolation by Eq. (13).

melting is included in the average value of derivative in an interval 1000 K long.

Table 10 gives values of heat capacity $C_{V}$ at constant volume (columns 3–8) calculated by the values of energy of the models. The values of $C_{el}$ given in the second column of the table must be added for obtaining the total heat capacity. One can see in Table 10 that, by and large, the kinetic and potential contributions to $C_{V}$ are little dependent on density and temperature, they decrease a little under heating and are close to the classical value of $3R \cong 25$ J/(mol K). A minor increase in $C_{V}$ on both sides of the melting line is associated with the fact that the heat of melting is included in the average value of heat capacity in an interval 1000 K long. However, the total values of heat capacity may be as high as 60–70 J/(mol K) at 5000 K and increase with further heating owing to the rapid growth of $C_{el}$.

Series of models at constant pressure of 1 to 100 GPa and temperatures up to 12 000 K were constructed for the calculation of isobaric heat capacity $C_{p}$ and heat of melting $\Delta H$. The heat capacity was calculated in view of equation $C_{p} = {({\partial H}/{\partial T})}_{p} = {({\partial U}/{\partial T})}_{p} - p{({\partial V}/{\partial T})}_{p} + C_{el}$. The $p{({\partial V}/{\partial T})}_{p}$ additions amounted to 2.3–6.1 J/(mol K) at $p = 10$ GPa and to 5.0–10.4 J/(mol K) at 100 GPa. Some results are given in Table 11. The total heat capacity is equal to the sum of heat capacity of the model and $C_{el}$ contribution. The values of heat capacity $C_{p}$ of uranium models (the sum of the third column with the fourth or fifth column) at high pressures are close to those of heat capacity of actual uranium at

HIGH TEMPERATURE Vol. 48 No. 3 2010

<table>
<caption>Table 11. Heat capacity $C_p$, J/(mol K), at pressures of 10 and 100 GPa</caption>
<thead>
<tr>
<th rowspan="2">T, K</th>
<th rowspan="2">$C_p$ of uranium at $p \cong 0$ [12]</th>
<th rowspan="2">$C_{\text{el}}$, J/(mol K), (13)</th>
<th colspan="2">Heat capacity of model, J/(mol K)</th>
</tr>
<tr>
<th>10 GPa</th>
<th>100 GPa</th>
</tr>
</thead>
<tbody>
<tr>
<td>300</td>
<td>27.67</td>
<td>14.28</td>
<td>25.5</td>
<td>25.6</td>
</tr>
<tr>
<td>1000</td>
<td>37.70</td>
<td>15.18</td>
<td>26.5</td>
<td>24.5</td>
</tr>
<tr>
<td>2000</td>
<td>49.12</td>
<td>17.49</td>
<td>34.5**</td>
<td>29.5</td>
</tr>
<tr>
<td>3000</td>
<td>52.07</td>
<td>21.01</td>
<td>34.3**</td>
<td>32.1</td>
</tr>
<tr>
<td>4000</td>
<td>55.20</td>
<td>22.74</td>
<td>26.6</td>
<td>34.8**</td>
</tr>
<tr>
<td>5000</td>
<td>58.39</td>
<td>31.69</td>
<td>26.5</td>
<td>32.7</td>
</tr>
<tr>
<td>6000</td>
<td>61.60</td>
<td>38.20*</td>
<td>27.0</td>
<td>25.9</td>
</tr>
<tr>
<td>7000</td>
<td>?</td>
<td>47.23*</td>
<td>26.3</td>
<td>25.3</td>
</tr>
<tr>
<td>8000</td>
<td>?</td>
<td>56.81*</td>
<td>24.6</td>
<td>24.0</td>
</tr>
<tr>
<td>9000</td>
<td>?</td>
<td>67.61*</td>
<td>23.0</td>
<td>20.7</td>
</tr>
<tr>
<td>10000</td>
<td>?</td>
<td>79.63*</td>
<td>22.5</td>
<td>24.1</td>
</tr>
<tr>
<td>11000</td>
<td>?</td>
<td>92.85*</td>
<td>24.5</td>
<td>22.9</td>
</tr>
<tr>
<td>12000</td>
<td>?</td>
<td>107.30*</td>
<td>26.7</td>
<td>22.7</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="5">* Extrapolation by Eq. (13).</td>
</tr>
<tr>
<td colspan="5">** Including the heat of melting.</td>
</tr>
</tfoot>
</table>

close-to-atmospheric pressure (the second column of table) and significantly exceed the classical value of $3R$. The heat of melting under a pressure of 10 GPa amounted to ~15.6 kJ/mol and, at 100 GPa, turned out to be within the error of calculation. The error in this case is 2–3 kJ/mol.

The "method of reheating" described above was used for determining the melting temperature $T_{\text{melt}}$ of uranium in compressed states. In this part of the study, we used a model of bcc uranium with 2000 particles in the basic cube. The obtained values of $T_{\text{melt}}$ are given in Table 12.

Figure 5 gives comparison of these temperatures with those found by the static method at pressures up to 45 GPa using laser heating [32]. These results are in good agreement with one another.

The data of Tables 9 and 10 may be used for calculating the Grüneisen coefficient $\gamma = (V/C_V)(\partial p/\partial T)_V$. Table 13 gives some results at compression ratio $Z = 0.70$ ($V = 8.743\ \text{cm}^3/\text{mol}$).

At temperatures below 8000 K, the coefficient $\gamma$ only slightly depends on temperature, as is presumed in the Grüneisen model. The value of $\gamma$ is somewhat lower than that calculated in [24], where ~1.4 was obtained at $Z = 0.7$.

## DISCUSSION OF THE RESULTS

The foregoing results demonstrate that the EAM potential adequately describes the behavior of the structural and thermodynamic properties of liquid uranium in a wide range of temperatures and densities. The suggested EAM potential enables one to calculate the properties of uranium with good accuracy.

The "reheating method" proved to be quite suitable for estimating the melting temperature of uranium model. This temperature ($1455 \pm 2$ K) is close to the actual value. The melting line was predicted up to a pressure of 444 GPa. The predicted pressure dependence of melting temperature at $p \leq 45$ GPa agrees well with experimental results.

For obtaining agreement with experimental data for energy along the $p = 0$ isobar, we had to assume that a peculiar contribution to energy emerges at elevated temperatures, which is due to excitation of atomic electrons and leads to a high heat capacity of uranium. This contribution is included into the scheme of molecular-dynamic calculations; it may be as high as almost 100 kJ/mol at 5000 K.

We used the limited available data on pressure and energy along the Hugoniot shock adiabat and managed to calculate the thermodynamic properties of uranium at temperatures up to 12 000 K and pressures up to 470 GPa. At $T \leq 5000$ K, the heat capacities $C_p$ and $C_V$, the derivatives $(\partial p/\partial T)_V$, and the Grüneisen

<table>
<caption>Table 12. The melting temperature of uranium</caption>
<thead>
<tr>
<th>$Z = V/V_0$</th>
<th>0.90</th>
<th>0.80</th>
<th>0.70</th>
<th>0.65</th>
<th>0.60</th>
<th>0.55</th>
</tr>
</thead>
<tbody>
<tr>
<td>$P$, GPa</td>
<td>$26.1 \pm 0.1$</td>
<td>$63.2 \pm 1.1$</td>
<td>$134.2 \pm 1.8$</td>
<td>$209.1 \pm 1.7$</td>
<td>$306.8 \pm 0.6$</td>
<td>$443.8 \pm 1.7$</td>
</tr>
<tr>
<td>$T_{\text{melt}}$, K</td>
<td>$2492 \pm 5$</td>
<td>$3582 \pm 5$</td>
<td>$4650 \pm 10$</td>
<td>$5495 \pm 5$</td>
<td>$6430 \pm 5$</td>
<td>$7342 \pm 5$</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 13. Parameters of uranium at high temperatures (the heat capacity is given in view of the $C_{\text{el}}$ contribution)</caption>
<thead>
<tr>
<th>$T$, K</th>
<th>1000</th>
<th>2000</th>
<th>5000</th>
<th>8000</th>
<th>10000</th>
</tr>
</thead>
<tbody>
<tr>
<td>$C_V$</td>
<td>36.6</td>
<td>44.9</td>
<td>63.4</td>
<td>82.3*</td>
<td>101.5*</td>
</tr>
<tr>
<td>$(\partial p/\partial T)_V$, MPa/K</td>
<td>3.76</td>
<td>5.41</td>
<td>6.37</td>
<td>4.41</td>
<td>3.41</td>
</tr>
<tr>
<td>$\gamma$</td>
<td>0.90</td>
<td>1.05</td>
<td>0.88</td>
<td>0.47*</td>
<td>0.29*</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="6">* Extrapolated values.</td>
</tr>
</tfoot>
</table>

![](./images/811775952748019712_5.jpg)

Fig. 5. The melting temperature of uranium at high pres- sures: (1) experimental data of [32], (2) our calculation results.

coefficient vary relatively slightly. The Grüneisen model highly overestimates the temperature on the shock adiabat and underestimates the "cold pressure" at high values of compression ratio.

## CONCLUSIONS

A new method was suggested in the present study for the calculation of the EAM potential for metal under extreme conditions, which involves the use of data for pressure and energy on the Hugoniot shock adiabat. This method enables one to calculate the properties of metals in a very wide range of pressures and temperatures without resorting to approximate estimates of the Grüneisen model type. The thus obtained potential may be used for calculating numer- ous properties of metal both at fixed density and tem- perature and in dynamic processes. The suggested method enables one to find thermal and caloric equa- tions of state for metals using the extensive literature available on shock adiabats. The prediction capacity of the method is defined by the adequacy of the structure of expressions (1) and (10) and merits special study.

## ACKNOWLEDGMENTS

We are grateful to L.R. Fokin for great assistance in analysis of experimental data and valuable discussions and to N.V. Shatrova for her part in performing the calculations.

This study was supported by the Ministry of Educa- tion and Science of the Russian Federation (grant RNP.2.1.1.712) and by the Russian Foundation for Basic Research (grant nos. 06-08-01142, 07-03-91558-NNIO, and 06-03-32690).

## REFERENCES

1. Finnis, M.W. and Sinclair, J.E., Philos. Mag. A, 1984, vol. 50, p. 45.
2. Daw, M.S. and Baskes, M.I., Phys. Rev. B, 1984, vol. 29, no. 12, p. 6443.
3. Belashchenko, D.K., Teplofiz. Vys. Temp., 2009, vol. 47, no. 4, p. 522 (High Temp. (Engl. transl.), vol. 47, no. 4, p. 494).
4. Belashchenko, D.K. and Ostrovski, O.I., Teplofiz. Vys. Temp., 2009, vol. 47, no. 2, p. 231 (High Temp. (Engl. transl.), vol. 47, no. 2, p. 211).
5. Belashchenko, D.K., Zh. Fiz. Khim., 2006, vol. 80, no. 10, p. 1767 (Russ. J. Phys. Chem. (Engl. transl.), vol. 80, no. 10).
6. Martynyuk, M.M., Fazovye perekhody pri impul'snom nagreve (Phase Transitions under Pulsed Heating), Moscow: Izd. RUDN (Russ. Univ. of Friendship of Peoples), Moscow, 1999.
7. Gathers, G., Rep. Prog. Phys., 1986, vol. 49, no. 4, p. 341.
8. Fortov, V.E., Dremin, A.N., and Leont'ev, A.A., Teplofiz. Vys. Temp., 1975, vol. 13, no. 5, p. 1072.
9. Likal'ter, A.A., Usp. Fiz. Nauk, 2000, vol. 170, p. 831 (Phys. Usp. (Engl. transl.), vol. 170).
10. Shpil'rain, E.E., Fomin, V.A., and Kachalov, V.V., Teplofiz. Vys. Temp., 1988, vol. 26, no. 5, p. 892.
11. Fokin, L.R., Liquid Uranium, Density Isobar of 1406-4500 K, Sbornik dokladov mezhvedomstvennogo semi- nara TF-2007 (Collection of Papers to TF-2007 Inter- departmental Seminar), Obninsk: State Scientific Cen- ter of the Russian Federation-Leipunskii Institute of Energy Physics, 2008, p. 400; CD.
12. Gurvich, L.V., Veits, I.V., Medvedev, V.A. et al., Termo- dinamicheskie svoistva individual'nykh veshchestv: Spra- vochnik (The Thermodynamic Properties of Pure Sub- stances: A Handbook), Moscow: Nauka, 1982, vol. 4, Books 1 and 2.
13. Young, D.A. and Ross, M., Phys. Rev. B, 1984, vol. 29, no. 2, p. 682.
14. IVTANTERMO-baza dannykh termodi- namicheskikh svoistv individual'nykh Veshchestv (IVTANTERMO - a Data Base of Thermodynamic Properties of Pure Substances). OIVT RAN (http://www.chem.msu.su/ rus/handbook/ivtan).
15. Site (httr://www.webelements.com).
16. Tekuchev, V.V., Akusticheskoe issledovanie svoistv elek- tronnykh rasplavov (Acoustic Investigation of the Prop- erties of Electron Melts), Volgograd: RPK "Politekh- nik", 2005.
17. Boivineau, M., Arles, L., Vermeulen, J.M., and Theve- nin, Th., Phys. B, 1993, vol. 190, no. 1, p. 31.
18. Wittenberg, L.J, A Model for Liquid Uranium and Plu- tonium with Implications on the Adjacent Solid Phases, in Plutonium 1975 and Other Actinides. Proc. 5th Int. Conf. on Plutonium and Other Actinides, Blank, H. and Linder, R., Eds., Baden-Baden: North-Holland Publishers, 1976, p. 71.
19. Norman, G.E. and Stegailov, V.V., Mol. Simul., 2004, vol. 30, no. 6, p. 397.
20. Kuksin, A.Y., Morozov, I.V., Norman, G.E. et al., Mol. Simul., 2005, vol. 31, nos. 14-15, p. 1005.

HIGH TEMPERATURE Vol. 48 No. 3 2010

21. Belashchenko, D.K., *Komp'yuternoe modelirovanie zhidkikh i amorfnykh veshchestv: Nauchnoe izdanie* (Computer Simulation of Liquid and Amorphous Sub- stances: A Scientific Publication), Moscow: MISIS (Moscow Inst. of Steel and Alloys), 2005.

22. *LASL Shock Hugoniot Data*, Marsh, S.P., Ed., Berkeley: Univ. California Press, 1979.

23. Van Thiel, M., *Compendium of Shock Wave Data. Rep. UCRL-50108*, Livermore: Lawrence Livermore Labo- ratory, 1977.

24. Zharkov, V.N. and Kalinin, V.A., *Uravneniya sostoya- niya tverdykh tel pri vysokikh davleniyakh i temper- aturakh* (Equations of State for Solids at High Pressures and Temperatures), Moscow: Nauka, 1968.

25. Zhernokletov, M.V., *Teplofiz. Vys. Temp.*, 1998, vol. 36, no. 2, p. 231 (*High Temp.* (Engl. transl.), vol. 36, no. 2, p. 214).

26. Belashchenko, D.K., *Usp. Fiz. Nauk*, 1999, vol. 169, no. 4, p. 361 (*Phys. Usp.* (Engl. transl.), vol. 169, no. 4).

27. Fomin, V.A., Kachalov, V.V., Mozgovoi, A.G. et al., The Thermophysical Properties of Uranium in the Liq- uid Phase, in *Materialy dokladov i soobshchenii XI Ros- siiskoi konferentsii po teplofizicheskim svoistvam Ve- shchestv* (Materials of Papers and Communications to Xi Russian Conference on Thermophysical Proper- ties), St. Petersburg, 2005, vol. 2, p. 119.

28. Ofte, D., *J. Nucl. Mater.*, 1967, vol. 22, p. 28.

29. Finucane, I.S. and Olander, D.R., *High Temp. Sci.*, 1969, vol. 1, p. 466.

30. Belashchenko, D.K. and Ostrovski, O.I., *Zh. Fiz. Khim.*, 2008, vol. 82, no. 3, p. 443 (*Russ. J. Phys. Chem.* (Engl. transl.), vol. 82, no. 3).

31. Funtikov, A.I., *Teplofiz. Vys. Temp.*, 1998, vol. 36, no. 3, p. 406 (*High Temp.* (Engl. transl.), vol. 36, no. 3, p. 384).

32. Yoo, C.S., Akella, J., and Moriarty, J.A., *Phys. Rev. B*, 1993, vol. 48, no. 21, p. 15529.

HIGH TEMPERATURE Vol. 48 No. 3 2010