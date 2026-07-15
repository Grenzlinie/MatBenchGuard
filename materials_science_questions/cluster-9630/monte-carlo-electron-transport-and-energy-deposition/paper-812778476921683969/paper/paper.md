# ELECTRON RANGE AT LOW ENERGY ($\text{E}_\text{O} < 10$ KEV): ATOMIC NUMBER DEPENDANT ?

Pierre Hovington*, Marin Lagacé*, Dominique Drouin **, Raynald Gauvin ***

*Hydro-Québec Research Institut, 1800 Boul. Lionel-Boulet, Varennes, Québec, J3X 1S1, Canada
** Department of Electrical, Université de Sherbrooke, Sherbrooke, Québec, Canada
**Mining and Metallurgy Department, McGill University, Montréal, Québec, Canada

The electron range and x-ray production for a given beam energy and atomic number is one of the most valuable piece of information a microscopist must have before carrying out qualitative and quantitative analysis on heterogeneous samples in a scanning electron microscope (SEM). Initial experiments by Kanter & Sternglass [1] and Cosslett & Thomas [2] show that the electron range, when expressed in mass thickness units ($\rho$R), depends only lightly on the atomic number (Z) of the material. However, some experiments (Al-Ahmad & Watt [3]) found an increase in the electron range with the atomic number. At low energy ($\text{E}_\text{o} < 5$ keV), because of the very limited electron range (< 40 nm for Al at 1 keV), experimental measurements are strongly affected by the surface condition and contamination making them very hard to perform. In addition, the frequently used parametrization of Kanaya & Okayama [4] is only « valid » at high energy ($\text{E}_\text{o} > 10$ keV). In this work, the CASINO Monte Carlo program⁵, specially designed for low energy simulation, was used to compute the electron range for 10 elements at 20 different energies. The parameterization of the electron range at low energy as a function of atomic number and beam energy will be presented for x-ray production as well as for backscattered and internal electrons.

The maximum depth reached by 99.9 % of 250k simulated electrons was used for the calculation of the range (Fig. 1). Excellent agreement was found between simulated and experimental data for Al and Ag (Fig. 2-3). For electrons, the relation between range and $\text{E}_\text{o}$ can written as a simple power law :

$$\text{R} = \text{kE}_\text{o}^\text{n} \, (\text{nm}).$$

For X-ray, the relation must be modified to take into account the ionization energy threshold of a given shell ($\text{E}_\text{c}$):

$$\text{R} = \text{k}(\text{E}_\text{o}^\text{n} -\text{E}_\text{c}^\text{n})(\text{nm}).$$

where $\text{E}_\text{o}$ and $\text{E}_\text{c}$ are given in keV. k and n are $2^\text{nd}$ degree polynomials in Z (cf. table 1). The fit precision is better than 10 % for E > 1 keV. Fig. 4 shows the simulated and fitted range for the Al, Cu and Ag internal electrons. An applet will be available on the internet for online calculations (www.ireq.ca). We present in figure 4 the electron range for C, Al, Cu, Ag and Au. The error bars were calculated based on Tung's relative fluctuation of the electron range at low energy[6]. An increase in the electron range with the atomic number (when expressed in mass thickness units) was found even if this statistical fluctuation was taken into account.

In conclusion, the CASINO Monte Carlo program, specially designed for low energy simulation, allows us to model the electron range and x-ray ionization in solids at low energy. At this energy range, simulations must often be preferred to experiments. Based on those results, the electron range varies with atomic number especially at very low energy ($\text{E}_\text{o} < 2$ keV).

## References
[1] Kanter, H., and Sternglass, E.J., (1959), J. Appl. Phys., Vol. 30, p. 1428
[2] Cosslett, V.E., and Thomas, R.N., (1964), Britt. J. Appl. Phys. , Vol. 15., pp. 1283- 1300.
[3] Al-Ahmad, K.O., and Watt, D.E., (1983), J.Phys.D : Appl. Phys., 16, pp 2257-67
[4] Kanaya, K., and Okayama, S., (1972), J. Phys. D : Appl. Phys., 5, pp. 43-58.
[5] Hovington, P. *et al.*, (1997), Scanning Vol. 19, pp. 1-14

[6] Tung C.J., *et al*, (1979), Transactions on Nuclear Science, Vol. NS-**26**, no 6., p. 4874

[7] Young, J.R., (1956), J. Appl. Phys., **27**, p. 1

[8] Holliday, J.E., and Sternglass, E.J., (1959), J. Appl. Phys., **30**, p. 1428.

[9] Kanter, H., and Sternglass, E.J., (1962), J. Appl. Phys., Vol. 30, p. 1428

[10] This work was supported by Hydro-Quebec Research Institut

**TABLE 1 : $2^\text{nd}$ degree polynomials used as the n and k parameters of the range of internal electrons ($\text{E}_\text{o} < 10$ keV). $\rho$ is the density of the analyzed region in $\text{g/cm}^3$.**

<table>
  <tr>
    <td colspan="4">$\begin{bmatrix} n \\ k\rho \end{bmatrix} = a_o + a_1Z + a_2Z^2$</td>
  </tr>
  <tr>
    <td></td>
    <th>$\text{a}_\text{o}$</th>
    <th>$\text{a}_1$</th>
    <th>$\text{a}_2$</th>
  </tr>
  <tr>
    <td>N</td>
    <td>1.755</td>
    <td>$-7.4\text{x}10^{-3}$</td>
    <td>$3.0\text{x}10^{-5}$</td>
  </tr>
  <tr>
    <td>Kp</td>
    <td>43.04</td>
    <td>1.5</td>
    <td>$5.4\text{x}10^{-3}$</td>
  </tr>
</table>

![](./images/812778476921683969_1.jpg)

Fig. 1

![](./images/812778476921683969_2.jpg)

Fig. 2

![](./images/812778476921683969_3.jpg)

Fig. 3

![](./images/812778476921683969_4.jpg)

Fig. 4

FIG. 1 : Distribution of the electron range (internal, backscattered and cumulative fraction) for Al at 5 kV. As showed, the maximum reached by 99.9 % of the simulated electrons was used.

FIG. 2 : Range for Al simulated by CASINO and determined experimentally as a function of $\text{E}_\text{o}$.

FIG. 3 : Range for Ag simulated by CASINO and determined experimentally as a function of $\text{E}_\text{o}$.

FIG. 4 : Range for C, Al, Ag and Au simulated by CASINO and determined experimentally as a function of $\text{E}_\text{o}$.