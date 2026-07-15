ISSN 0016-7029, Geochemistry International, 2008, Vol. 46, No. 2, pp. 182-186. © Pleiades Publishing, Ltd., 2008.
Original Russian Text © V.A. Bychinskii, Zh.V. Kostyanetskaya, K.V. Chudnenko, A.A. Tupitsin, Yu.I. Sidorov, 2008, published in Geokhimiya, 2008, No. 2, pp. 210-214.

# SHORT COMMUNICATIONS

## Techniques for the Calculation of Consistent Low-Temperature Thermodynamic Data for Compounds

V. A. Bychinskiiⁱ, Zh. V. Kostyanetskayaⁱ, K. V. Chudnenkoⁱ, A. A. Tupitsinⁱ, and Yu. I. Sidorovᵇ†

ⁱ Vinogradov Institute of Geochemistry, Siberian Branch, Russian Academy of Sciences,
ul. Favorskogo 1a, Irkutsk, 664033 Russia
ᵇ Vernadsky Institute of Geochemistry and Analytical Chemistry, Russian Academy of Sciences,
ul. Kosygina 19, Moscow, 119991 Russia

Received February 5, 2007

DOI: 10.1134/S0016702908020080

The development of the theoretical and experimental basis for chemical thermodynamics in the second half of the 20th century made it possible to formulate and resolve a number of fundamental problems of geochemistry and petrology. In spite of the complicated and multiphase character of natural processes and their spatiotemporal scale that preclude their direct experimental modeling, extensive information is currently accumulated on the thermodynamic constants of natural and synthetic compounds.

The adequacy of reproduction of cryogenic processes in space and at the Earth's surface is determined in terms of chemical thermodynamics and depends not on the capabilities of computer simulations or specifics of the behavior of various compounds under these conditions but on the availability of pertinent thermodynamic information. In this context, a task of paramount importance is the development of a modern methodological basis for the calculation of consistent thermodynamic properties for describing the behavior of compounds at 0–300 K.

The input data for modeling numerical simulations are the thermodynamic constants and functional dependences of the partial chemical properties of chemical components that can potentially exist in a system of specified chemical composition. Knowing the temperature dependence of the isobaric heat capacity $C_p^\circ(T)$ of a compound, one can calculate its enthalpy $H^\circ(T) = \int C_p^\circ(T)dT$ and entropy $S^\circ(T) = \int C_p^\circ(T)/TdT$ functions, which, in turn, make it possible to determine the temperature function of the Gibbs energy $G^\circ(T)$, whose numerical values are needed to calculate the equilibrium compositions of heterogeneous multicomponent systems by minimization techniques. The key problem of this approach is the experimental and methodological difficulty of measuring the heat capacity of compounds at low temperatures [1].

One of the main tasks of our research was the experimental appraisal of the possibility of extrapolating heat capacity values known at temperatures above 298.15 K to low temperatures using the thermodynamic database with the aim of conducting physicochemical simulations of the transformations of compounds at absolutely low temperatures.

An approach to evaluating thermodynamic potentials at low absolute temperatures was proposed by Sidorov et al. [1, 2], who not only experimentally examined such systems but also developed a method for the approximation of the thermodynamic properties of various compounds to low temperatures. The results of the specialized research [2] convincingly demonstrate that the analytical form for the $C_p^\circ(T)$ dependence proposed in [3] and based on the so-called Lorentz distribution (referred to as the $L$ approximation),

$$
C_{p}^{\circ}(T)=a\left(1-\frac{1}{1+b T^{2}}\right)+c T, \tag{1}
$$

possesses required approximation characteristics.

At the same time, the experimental databank of the low-temperature dependences of heat capacities is very scarce and contains mostly data on simple compounds, such as oxides and native elements. In view of this, we attempted to work out techniques for the extrapolation of heat capacity values obtained at temperatures of >273 K to low temperatures of ≲273K. At the minimum amount of available data and with regard for the difficulty of direct experimental reproducing physicochemical processes in space, we were left with the only possibility of theoretical studying of the evolution of the protoplanetary nebula and the gas shells and surfaces of terrestrial planets.

First of all, we revised all approximating equations (1). Using an extensive selection of experimental $C_p^\circ(T)$ values at $T < 300$ K, which were published in *The Journal of Physical Chemistry* in 1990–1998 (Table 1), we calculated the coefficients of the $L$ approximation,

† Deceased August 11, 2007

**Table 1.** Compounds whose thermodynamic properties were used in our numerical simulations

| Compound      | Reference | Compound    | Reference | Compound      | Reference |
|---------------|-----------|-------------|-----------|---------------|-----------|
| $\text{Cd}_3\text{Fe}_5\text{O}_{12}$ | [4]       | $\text{Pr}$ | [14]      | $\text{Nb}_3\text{I}_8$ | [26]      |
| $\text{CsBrO}_4$ | [5]       | $\text{NaLaWO}_{42}$ | [15] | $\text{La}_3\text{Si}_2$ | [27]      |
| $\text{YCl}_3$ | [6]       | $\text{TiCl}_2$ | [16]      | $\text{La}_5\text{Si}_3$ | [27]      |
| $\text{ErCl}_3$ | [7]       | $\text{Tm}$ | [17]      | $\text{La}_5\text{Si}_4$ | [27]      |
| $\text{TmCl}_3$ | [8]       | $\text{KBF}_4$ | [18]      | $\text{LaSi}_2$ | [28]      |
| $\text{HoCl}_3$ | [9]       | $\text{Cu}_3\text{AsS}_3$ | [19] | $\text{LaSi}$ | [28]      |
| $\text{FeAs}$ | [10]      | $\text{Dy}_3\text{Fe}_5\text{O}_{12}$ | [20] | $\text{GeI}_4$ | [29]      |
| $\text{Mn}_2\text{B}$ | [11]      | $\text{Y}_2\text{O}_3$ | [21]      | $\text{GeI}_2$ | [30]      |
| $\text{MnB}_4$ | [11]      | $\text{CsBF}_4$ | [22]      | $\text{Lu}_3\text{Fe}_5\text{O}_{12}$ | [31] |
| $\text{MnB}$ | [11]      | $B\text{-Eu}_2\text{O}_3$ | [23] | $\text{CoB}$ | [32]      |
| $\text{RbIO}_4$ | [12]      | $C\text{-Eu}_2\text{O}_3$ | [23] | $\text{FeB}$ | [32]      |
| $\text{Mo}_6\text{Se}_8$ | [13]      | $\text{SeO}_3$ | [24]      | $\text{NiB}$ | [32]      |
| $\text{Mo}_6\text{Te}_8$ | [13]      | $\text{GaCl}_3$ | [25]      |               |           |

which enabled us to compare the calculated and experimentally determined heat capacity values (Fig. 1).

Indeed, in contrast to polynomial representations of $C_p^\circ(T)$, its $L$ form is characterized by $\lim_{T \to 0} C_p^\circ(T) = 0$, which makes it possible to accurately enough approximate experimental data (Fig. 1). This property, as well as the character of the approximating curve, led us to anticipate that an $L$ approximation can produce a satisfactory extrapolation of experimental heat capacity values obtained for compounds at temperatures above 298.15 K to absolutely low values.

We examined temperature ranges sufficient to calculate the coefficients of an $L$ approximation equation for the extrapolation of $C_p^\circ(T)$ values to low temperatures.

The extrapolating characteristics of Eq. (1) were tested using data from [33]. We selected compounds for which experimental $C_p^\circ(T)$ values are tabulated for temperatures including $T = 100$ and 200 K. We did not, however, introduce these values into the regression matrix for the calculation of coefficients of the $L$ approximation but instead utilized them as benchmarks that enabled us to monitor the accuracy of our calculations. For each of the selected temperature ranges of 298.15–700, 298.15–1000, 298.15–1500, and 298.15–2000 K, we determined the coefficients of Eq. (1) and calculated $C_p^\circ(T)$ values for the temperature range of 0–300 K. The plots in Figs. 2a and 2b show the corresponding lines and make it possible to compare our calculated values with those published in [33] at $T = 100$, 200, and 298.15 K.

**Table 2.** $L$ approximation coefficients for $C_p^0(T)$

| Approximation interval, K | Coefficients of Eq. (1) | | | $\Delta$ | $R$ |
|---------------------------|-------------------------|---|---|-----------|-----|
|                           | $a$ | $b \times 10^5$ | $c \times 10^2$ | | |
| | | $\text{LiBO}_2(\text{sol})$ | | | |
| 298–2000 | 55.191 | 4.663 | 5.452 | 1.1699 | 0.99996 |
| 298–1500 | 56.095 | 4.369 | 5.371 | 0.92854 | 0.99995 |
| 298–1117 | 57.364 | 4.057 | 5.240 | 0.6843 | 0.99994 |
| 298–1000 | 58.259 | 3.888 | 5.135 | 0.57288 | 0.99993 |
| 298–700 | 62.082 | 3.384 | 4.636 | 0.27738 | 0.99995 |
| | | $\text{BaS}(\text{sol})$ | | | |
| 298–3000 | 50.328 | 15.971 | 0.755 | 0.43765 | 0.99993 |
| 298–2000 | 50.362 | 15.813 | 0.753 | 0.43245 | 0.99979 |
| 298–1500 | 50.236 | 16.309 | 0.765 | 0.41666 | 0.9996 |
| 298–1000 | 49.612 | 18.820 | 0.838 | 0.33651 | 0.99926 |
| 298–700 | 47.994 | 28.381 | 1.070 | 0.18121 | 0.99942 |

Note: $\Delta$ is the mean square deviation; $R$ is the correlation coefficient.

Our numerical simulations testify that $C_p^\circ(T)$ values optimal for heat capacity extrapolations to low temperatures are those obtained for the temperature ranges from 298.15 K to the phase transition point or, in the absence of a phase transition, from 298.15 to 700 K, which provides required thermodynamic accuracy (Table 2). Thus, our research demonstrates that the problem of heat capacity extrapolation to low temperatures can be successfully solved using the Lorentz

![](./images/811679976163115009_1.jpg)

**Fig. 1.** $L$ approximation of experimentally determined heat capacity values.

![](./images/811679976163115009_2.jpg)

equation. Although the differences between the $C_p^\circ(T)$ low-temperature values obtained using various temperature ranges are insignificant, it is necessary to select temperature ranges that yield the lowest errors, because they are further used for integration.

Heat capacity values obtained for minerals usually make it possible to calculate the standard entropies of these minerals and the enthalpy change functions by means of the numerical integration of the functions $S^\circ(T)=\int C_p^\circ(T)/T\ dT$ and $H^\circ(T)=\int C_p^\circ(T)dT$. The utilization of a temperature dependence of isobaric heat capacity in the Lorentz form enables the researcher to obtain accurate evaluations for such integral functions as the entropy and enthalpy change and to analytically integrate according to (2)-(4)

$$
\begin{aligned}
H^{\circ}(T) & =\int C_{p}^{\circ}(T) d T \\
& =a T-\frac{a}{\sqrt{b}} \arctan (\sqrt{b} T)+\frac{1}{2} c T^{2} ;
\end{aligned}
\tag{2}
$$

$$
S^{\circ}(T)=\int \frac{C_{p}^{\circ}(T)}{T} d T=\frac{a}{2} \ln \left(1+b T^{2}\right)+c T ; \tag{3}
$$

$$
\begin{aligned}
G^{\circ}(T) & =\int S^{\circ}(T) d T=a T-\frac{a}{\sqrt{b}} \arctan (\sqrt{b} T) \\
& -\frac{a}{2} T \ln \left(1+b T^{2}\right)-\frac{1}{2} c T^{2}+\text { const. }
\end{aligned}
\tag{4}
$$

Inasmuch as the $C_p^\circ(T)$ values are extrapolated "downward" from $T=298.15$ K, integrating should be conducted from the standard temperature to zero. For example, in calculating entropy, we use the difference of the integrals

$$
\begin{aligned}
S^{\circ}(T) & =\int_{0}^{T_{r}} \frac{C_{p}^{\circ}(T)}{T} d T-\int_{T}^{T_{r}} \frac{C_{p}^{\circ}(T)}{T} d T \\
& =S_{r e f}^{\circ}-\left(S^{\circ}\left(T_{r}\right)-S^{\circ}(T)\right).
\end{aligned}
\tag{5}
$$

In this approach, finding the optimum approximation of a pointwise defined continuous function $C_p^\circ(T)$ ensures a good consistency between the experimental and calculated values (Fig. 3). This makes it possible to more accurately calculate the values of integral thermo-

![](./images/811679976163115009_3.jpg)

dynamic potentials within temperature ranges from
100 K to the standard temperature.

## CONCLUSIONS
The results of our research have proved the possibil-
ity of calculating the coefficients of the $L$ approximat-
ing equation from heat capacity values within a temper-
ature range of 298.15–700 K, which makes it possible
to extrapolate heat capacity values to low temperatures.
Integrating the obtained heat capacity values over a
temperature interval of 0–298.15 K, it is possible to cal-
culate the entropy, enthalpy, and consequently, the
Gibbs energy satisfying the condition $\lim_{T \to 0} C_p^\circ(T) = 0$.

The method proposed in this publication provides a
basis for developing a thermodynamic database for the
calculation of the equilibrium composition of heteroge-
neous multicomponent and multiaggregate systems at
superlow temperatures.

## REFERENCES
1. Yu. I. Sidorov, Doctoral Dissertation in Geology and
Mineralogy (Moscow, 1999).
2. A. I. Shapkin and Yu. I. Sidorov, “New Form of $C_p$(T)
Representation,” Geokhimiya, No. 12, 1230–1235
(1996) [Geochem. Int. 34, 1108–1112 (1996)].
3. V. N. Kuznetsov and V. K. Kozlov, “Temperature Depen-
dence for Heat Capacity of Minerals, “in *Proceedings of
2nd All-Russian Symposium on Thermodynamics in
Geology, Miass, Russia, 1988*,” (Miass, 1988), pp. 32–33
[in Russian].
4. V. S. Varazashvili, M. S. Tsarakhov, K. S. Gavrichev,
et al., “Low-Temperature Heat Capacity of Gadolinium
Ferrogarnet,” Zh. Fiz. Khim. 64 (1), 248–250 (1990).
5. V. E. Gorbunov, K. S. Gavrichev, G. A. Totrova, et al.,
“Thermodynamic Properties of Cesium Perborate within
a Range of 10–320 K,” Zh. Fiz. Khim. 64 (1), 274–277
(1990).
6. P. I. Tolmach, V. E. Gorbunov, K. S. Gavrichev, and
V. F. Goryushkin, “Low-Temperature Heat Capacity of
YCl₃,” Zh. Fiz. Khim. 64 (4), 1088–1090 (1990).
7. P. I. Tolmach, V. M. Gorbunov, K. S. Gavrichev, et al.,
“Low-Temperature Heat Capacity of ErCl₃,” Zh. Fiz.
Khim. 64 (4), 1090–1093 (1990).
8. P. I. Tolmach, V. E. Gorbunov, K. S. Gavrichev, and V. F. Go-
ryushkin, “Low-Temperature Heat Capacity of TmCl₃,”
Zh. Fiz. Khim. 64 (4), 1093–1095 (1990).
9. P. I. Tolmach, V. E. Gorbunov, K. S. Gavrichev, et al.,
“Low-Temperature Heat Capacity of HoCl₃,” Zh. Fiz.
Khim. 64 (4), 1096–1098 (1990).
10. A. S. Pashinkin, V. A. Muratova, N. V. Moiseev, and
Yu. V. Bazhenov, “Thermodynamic Functions of Iron
Monoarsenide,” Zh. Fiz. Khim. 64 (5), 1408–1409
(1990).
11. N. N. Sirota, V. A. Vinokurov, and V. V. Novikov, “Heat
Capacity, Characteristic Temperature, and Thermody-
namic Properties of Borides Mn₂B, MnB, MnB₄ within
a Range of 4–300 K,” Zh. Fiz. Khim. 64 (6), 1516–1520
(1990).
12. K. S. Gavrichev, V. E. Gorbunov, G. A. Totrova, et al.,
“Heat Capacity of Rubidium within a Range of 10–330 K,”
Zh. Fiz. Khim. 64 (6), 1690–1693 (1990).
13. E. B. Amitin, Yu. F. Minenkov, O. A. Nabutovskaya, et
al., “Thermodynamic Properties of Mo₆Se₈ and Mo₆Te₈
within a Range of 7–300 K,” Zh. Fiz. Khim. 64 (7),
1755–1760 (1990).
14. G. A. Berezovskii, G. S. Burzhanov, N. B. Kol’chugina,
et al., “Heat Capacity within a Range from 5.6 to 314 K,”
Zh. Fiz. Khim. 64 (10), 2636–2640 (1990).
15. G. I. Frolova, L. P. Kozeeva, and I. E. Paukov, “Low-
Temperature Heat Capacity, Entropy, and Enthalpy Dif-
ference of NaLa(WO₄)₂,” Zh. Fiz. Khim. 64 (10), 2790–
2791 (1990).
16. E. M. Snigireva, G. A. Berezovskii, and V. I. Tsi-
rel’nikov, “Heat Capacity and Thermodynamic Function
of Crystalline Low Titanium Chlorides within a Range
of 5–315 K,” Zh. Fiz. Khim. 64 (12), 3370–3373 (1990).
17. G. L. Berezovskii, G. S. Burkhanov, S. Sh. Il’yasov, et al.,
“Heat Capacity of Thulium within a Range from 8 to
325 K,” Zh. Fiz. Khim. 65 (6), 1698–1703 (1991).
18. V. E. Gorbunov, K. S. Gavrichev, L. N. Golushina, et al.,
“Low-Temperature Heat Capacity of Potassium Tetra-
ferroborate,” Zh. Fiz. Khim. 67 (3), 609–611 (1993).
19. S. M. Tolkachev, V. B. Zlokazov, L. Ya. Kobelev, and N. V. Mel’-
nikova, “Heat Capacity of Cu₃AsS₃ with a Range of
3–300 K,” Zh. Fiz. Khim. 67 (8), 1577–1579 (1993).
20. T. B. Mirianashvili, V. S. Varazashvili, K. M. Gavrichev,
et al., “Low-Temperature Heat Capacity of Dysprosium
Ferrogarnet,” Zh. Fiz. Khim. 67 (8), 1721–1722 (1993).
21. K. S. Gavrichev, V. E. Gorbunov, L. N. Golushina, et al.,
“Heat Capacity and Thermodynamic Properties of Y₂O₃
within a Range of 14–300 K,” Zh. Fiz. Khim. 67 (8),
1731–1733 (1993).
22. K. S. Gavrichev, V. E. Gorbunov, L. N. Golushina, et al.,
“Heat Capcity of CsBF₄ with a Temperature Range of
12–320 K,” Zh. Fiz. Khim. 68 (5), 784–786 (1994).
23. N. S. Lyutsareva, G. A. Berezovskii, and I. E. Paukov,
“Heat Capacity of Two Modifications of Eu₂O₃ with a
Range of 8–300 K,” Zh. Fiz. Khim. 68 (7), 1179–1182
(1994).
24. S. N. Kondrat’ev and B. V. Strizhov, “Heat Capacity and
Thermodynamic Functions of Selenium Trioxide within
a Range of 12–307 K,” Zh. Fiz. Khim. 68 (7), 1190–1192
(1994).
25. E. B. Amitin, Yu. F. Minenkov, I. E. Paukov, and
Yu. G. Stenin, “Heat Capacity and Thermodynamic
Functions of GaCl₃ with a Range of 5.8–302 K,” Zh. Fiz.
Khim. 68 (7), 1330–1331 (1994).
26. E. B. Amitin, Yu. F. Minenkov, I. E. Paukov, et al., “Heat
Capacity and Thermodynamic Functions of Nb₃I₈ with a
Range of 8.5–300.6 K,” Zh. Fiz. Khim. 68 (7), 1332–1333
(1994).
27. A. S. Bolgar, N. P. Gorbachuk, A. V. Blinder, and
N. V. Moiseev, “Low-Temperature Thermodynamic
Characteristics of Lanthanum Silicide,” Zh. Fiz. Khim.
70, 492–495 (1996) [Russ. J. Phys. Chem. 70, 454–457
(1996)]
28. A. S. Bolgar, N. P. Gorbachuk, A. V. Blinder, and
N. V. Moiseev, “Thermodynamic Characteristics of Lan-
thanum Mono- and Disilicides at Low Temperatures,”

Zh. Fiz. Khim. **70** (7), 1185–1189 (1996) [Russ. J. Phys. Chem. **70**, 1100–1104 (1996)].

29. I. E. Paukov, Yu. F. Minenkov, V. N. Naumov, and L. N. Zelenina, "Thermodynamic Functions and Phonon Spectrum of Germanium Tetraiodide," Zh. Fiz. Khim. **71** (8), 1367–1370 (1997) [Russ. J. Phys. Chem. **71**, 1222–1225 (1997)].

30. G. A. Berezovskii, L. N. Zelenina, V. A. Titov, and I. E. Paukov, "Heat Capacity and Thermodynamic Func- tions of Germanium Diiodide over the Temperature Range 6–325 K," Zh. Fiz. Khim. **71** (10), 1904–1906 (1997) [Russ. J. Phys. Chem. **71**, 1719–1721 (1997)].

31. T. B. Mirianashvili, V. S. Varazashvili, M. S. Tsarakhov, et al., "Low-Temperature Heat Capacity and Thermody- namic Functions of Lutecium Ferrogarnet," Zh. Fiz. Khim. **72** (2), 16–18 (1998) [Russ. J. Phys. Chem. **72**, 10–12 (1998)].

32. N. N. Sirota, V. A. Vinokurov, and V. V. Novikov, "Heat Capacity and Thermodynamic Functions of Iron, Cobalt, and Nickel Borides in the Range 5–300 K," Zh. Fiz. Khim. **72** (5), 785–789 (1998) [Russ. J. Phys. Chem. **72**, 684–988 (1998)].

33. M. W. Chase, Jr., C. A. Davies, J. R. Powney, Jr., et al., "JANAF Thermochemical Tables. Third Edition. Part I, Al-Co. Part II, Cr-Zr," J. Phys. Chem. Ref. Data **14** (1985).