SHORT COMMUNICATIONS

# Investigation of the Influence of Lattice Anharmonicity on the Heat Capacities of Diamond, Silicon, and Germanium

S. Sh. Rekhviashvili and Kh. L. Kunizhev

Institute of Applied Mathematics and Automation, Nalchik, Kabardino-Balkaria, 360000 Russia
e-mail: rsergo@mail.ru
Received July 10, 2016

**Abstract**—The isochoric heat capacities of diamond, silicon, and germanium have been calculated ab initio using the quantum-statistical method. The phonon energy has been calculated with the Morse potential. The anharmonicity of lattice atomic vibrations is shown to occur at temperatures below the Debye temperature. Experimental data on the temperature dependences of the heat capacities of diamond, silicon, and germanium can be interpreted more correctly by taking into account the lattice anharmonicity.

DOI: 10.1134/S0018151X17020146

## INTRODUCTION

Nonmetals of the carbon subgroup (diamond, silicon, and germanium) are widely applied in electronics and modern nanotechnologies. For example, a quantum computer can be fabricated based on a diamond crystal, and diamond substrates are assumed to be very promising for micro- and nanoelectronics. Currently, silicon is an irreplaceable material for semiconductor devices, integrated circuits, and photocells for solar power engineering. Germanium is used in microwave devices, fiber and IR optics, and chemical catalysts. Correspondingly, it is critical to reveal and investigate new physicochemical properties of these materials.

The influence of anharmonicity of atomic vibrations on the thermophysical properties of diamond, silicon, and germanium crystals was experimentally and theoretically investigated in [1–14]. Anharmonicity was observed in experiments on Raman scattering [1–4], neutron spectroscopy [5, 6], and X-ray diffraction [7]. Various theoretical questions related to anharmonicity in diamond, silicon, and germanium crystals were considered in [8–14]: the Grüneisen parameters were calculated, the temperature dependence of the Debye temperature was taken into account, and the thermal-expansion coefficients, isobaric heat capacity, etc., were calculated in the high-temperature limit. It is well known that the anharmonicity of atomic vibrations in a solid violates the theorem of uniform energy distribution over the degrees of freedom of independent oscillators and, accordingly, the Dulong–Petit law. In this context, it is generally agreed that lattice anharmonicity can be observed only at high temperatures ($T > \theta_{\text{D}}$, where $\theta_{\text{D}}$ is the Debye temperature). However, analysis of the literature shows that, within a unified approach, the isochoric heat capacities of diamond, silicon, and germanium have not been calculated in detail taking into account the lattice anharmonicity in a wide temperature range. In this study, we performed these calculations and showed that the anharmonicity of atomic vibrations caused here by the exponential dependence of the potential energy on the displacement (Morse potential) occurs even at relatively low temperatures ($T < \theta_{\text{D}}/2$), which affects the temperature dependence of the isochoric heat capacity.

## CALCULATION OF THE ISOCHORIC heat capacity AND DISCUSSION OF THE RESULTS

The pair Morse potential is chosen to describe interatomic bonds for two reasons. First, this potential is successfully used for describing covalent bonds in calculations according to the molecular dynamics method [15, 16]. Second, the Schrödinger equation for an anharmonic oscillator with the Morse potential allows for the analytical solution [17]. The energy eigenvalues of this oscillator are determined by the formula

$$
\begin{gathered}
E_{n}(\omega) = \hbar\omega\left(n + \frac{1}{2}\right) - \frac{\hbar^{2}\omega^{2}}{4D}\left(n + \frac{1}{2}\right)^{2} \\
(n = 0,1,2,...),
\end{gathered} \tag{1}
$$

where $\hbar$ is Planck's constant, $\omega$ is the oscillator frequency, and $D$ is the potential-well depth for the Morse potential. Note that expression (1) at $D \to \infty$ transforms into the formula for a harmonic oscillator. In contrast to the harmonic approximation, the number of energy levels in the potential well is finite in this case. If formula (1) is used to calculate the phonon energy in a crystal, the maximum value of the quantum number $n$ should correspond to the Debye temperature:

$$
N = \max(n) = \left\lfloor \frac{4D}{k\theta_{\text{D}}} - \frac{1}{2} \right\rfloor, \tag{2}
$$

![](./images/817063494267437056_1.jpg)

Fig. 1. Temperature dependences of the isochoric heat capacity of (a) diamond, (b) silicon, and (c) germanium.

where square brackets indicate an integer part of the number (floor) and $k$ is the Boltzmann constant. Taking into account (1) and (2), one can calculate the partition function

$$
Z(\omega, T)=\sum_{n=0}^{N} \exp \left(-\frac{E_{n}(\omega)}{k T}\right). \tag{3}
$$

The mean free energy is calculated using the integral

$$
\langle F(T)\rangle=-\frac{9 R T}{\omega_{\mathrm{D}}^{3}} \int_{0}^{\omega_{\mathrm{D}}} \omega^{2} \ln Z(\omega, T) d \omega, \tag{4}
$$

where $R$ is the universal gas constant and $\omega_{\mathrm{D}}=k \theta_{\mathrm{D}} / \hbar$ is the Debye frequency. The isochoric heat capacity is determined as

$$
C_{V}(T)=-T \frac{\partial^{2}\langle F(T)\rangle}{\partial T^{2}}. \tag{5}
$$

For $D \rightarrow \infty$ and $N \rightarrow \infty$, expressions (1)-(5) yield the standard Debye model of heat capacity of solids (harmonic approximation).

A computational algorithm and a program for simu- lating thermophysical properties of crystals were developed based on (1)-(5). Functions (1) and (3) were tabulated with respect to variables $\omega$ and $T$ to cal culate the frequency integral in (4) and the second derivative in (5) and to plot the temperature depen- dences of the heat capacity. The number $N$ was calcu lated from (2) taking into account the data in the lite- rature on the Debye temperature [18] and potential- well depth for the pair interatomic potential [19]. It must be noted that the above parameters were deter- mined in [18, 19] by sufficiently reliable theoretical methods using data on the elastic properties and sub- limation heats of materials rather than obtained directly from the temperature dependences of the thermodynamic characteristics or phase diagrams. The authors believed that the use of specifically these data makes it possible to correctly compare the calcu- lation results within the proposed theoretical model and the experimental data on the heat capacity. In other words, the use of numerical values of $\theta_{\mathrm{D}}$ and $D$ from [18, 19] allows one to deal without purely empi- rical values of the parameters in this theoretical model. Numerical values of all the parameters of the model are listed in the table.

Figure 1 shows the theoretical and experimental temperature dependences of the isochoric heat capa- cities for nonmetals of carbon subgroup. Solid curves indicate the results of calculations based on (1)-(5), dashed curves show the results of calculations within the Debye model, and dots are the data obtained tak- ing into account the experimental values of the iso- baric heat capacity, thermal coefficient of volume expansion, and isothermal compressibility reported in [20]. The calculations show that, for all three materi- als, the lattice anharmonicity caused by the asymme- try of forces exerted on atoms upon their thermal vibrations occurs even at $T<\theta_{\mathrm{D}} / 2$. It can be seen in the table that the number of possible vibrational modes $N$ decreases with an increase in the Debye tem-

<table>
<caption>Numerical values of the parameters of the model</caption>
<thead>
<tr>
<th>Crystal</th>
<th>$\theta_{\mathrm{D}}$, K</th>
<th>$\omega_{\mathrm{D}}$, $10^{14}\ \mathrm{s}^{-1}$</th>
<th>$D$, eV</th>
<th>$N$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Diamond</td>
<td>2239.6</td>
<td>2.932</td>
<td>3.68</td>
<td>75</td>
</tr>
<tr>
<td>Si</td>
<td>648.9</td>
<td>0.850</td>
<td>2.32</td>
<td>165</td>
</tr>
<tr>
<td>Ge</td>
<td>373.4</td>
<td>0.489</td>
<td>1.94</td>
<td>240</td>
</tr>
</tbody>
</table>

perature and atomic binding energy in the crystal. This fact corresponds to the increasing influence of the lat- tice anharmonicity on the temperature dependence of the isochoric heat capacity. According to the pre- sented model, number $N$ or temperature ratio $\xi=T_{s}/\theta_{D}$ ($T_{s}$ is the sublimation temperature) can be considered as parameters that characterize lattice anharmonicity. In this case, parameter $\xi$ was chosen for estimation because the numerical values of $D$ found in [19] from the sublimation heats of the mate- rials were used in the calculations. Sublimation tem- perature is assumed to be directly related to the energy of interatomic bonds by expression $T_{s}\sim D/k$. Taking into account the reference values of $T_{s}$ for carbon, sil- icon, and germanium [20], parameters $\xi$ for these materials are, respectively, 2, 5.5, and 8.4. Thus, con- cerning the thermodynamic properties, germanium is closest to an ideal harmonic crystal. The lattice anhar- monicity in silicon is more pronounced than in germa- nium and, consequently, the Dulong–Petit law is vio- lated more here (see Figs. 1b, 1c). The isochoric heat capacity of diamond exceeds 21 J/(mol K) even at a tem- perature of 1000 K, which is much lower than the Debye temperature. This fact is indicative of a rather strong anharmonicity of carbon atomic vibrations in the dia- mond crystal, which is in qualitative agreement with the results of [11, 12]. The likely reason is that, under low pressures, diamond is a metastable form of carbon [21].

CONCLUSIONS

The temperature dependences of the isochoric heat capacities of diamond, silicon, and germanium were calculated within the quantum statistical method using the Morse potential. The influence of lattice anharmonicity on thermodynamic properties of a nonmetallic solid is characterized by dimensionless parameter $\xi$. This influence is most pronounced for diamond ($\xi=2$), while silicon occupies an intermedi- ate position ($\xi=5.5$) and germanium is closest to a harmonic crystal ($\xi=8.4$).

REFERENCES

1. Hart, T.R., Aggarwal, R.L., and Lax, B., *Phys. Rev. B: Solid State*, 1970, vol. 1, p. 638.
2. Balkanski, M., Wallis, R.F., and Haro, E., *Phys. Rev. B: Condens. Matter Mater. Phys.*, 1983, vol. 28, p. 1928.
3. Menendez, J. and Cardona, M., *Phys. Rev. B: Condens. Matter Mater. Phys.*, 1984, vol. 29, p. 2051.
4. Brazhkin, V.V., Lyapin, S.G., Troyan, I.A., Voloshin, R.N., Lyapin, A.G., and Mel’nik, N.N., *JETP Lett.*, 2000, vol. 72, no. 4, p. 195.
5. Nelin, G. and Nilsson, G., *Phys. Rev. B: Solid State*, 1974, vol. 10, p. 612.
6. Kim, D.S., Smith, H.L., Niedziela, J.L., Li, C.W., Abernathy, D.L., and Fultz, B., *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2015, vol. 91, 014307.
7. Cavalleri, A., Siders, C.W., Brown, F.L.H., et al., *Phys. Rev. Lett.*, 2000, vol. 65, no. 3, p. 586.
8. Jex, H., *Phys. Status Solidi B*, 1971, vol. 45, p. 343.
9. Trivedi, P.C., Sharma, H.O., and Kothari, L.S., *J. Phys. C: Solid State Phys.*, 1977, vol. 10, no. 2, p. 3487.
10. Narasimhan, Sh. and Vanderbilt, D., *Phys. Rev. B: Condens. Matter Mater. Phys.*, 1991, vol. 43, p. 4541.
11. Lomonosov, I.V., Fortov, V.E., Frolova, A.A., Khishchenko, K.V., Charakhch’yan, A.A., and Shur- shalov, L.V., *High Temp.*, 2003, vol. 41, no. 4, p. 447.
12. Khishchenko, K.V., Fortov, V.E., and Lomonosov, I.V., *Int. J. Thermophys.*, 2005, vol. 26, no. 2, p. 479.
13. Bodryakov, V.Yu. and Povzner, A.A., *Phys. Solid State*, 2003, vol. 45, no. 7, p. 1254.
14. Rekhviashvili, S.Sh., *Tech. Phys.*, 2008, vol. 53, no. 12, p. 1586.
15. Zhang, J.Z.H., *Theory and Applications of Quantum Molecular Dynamics*, Singapore–New Jersey–London– Hong Kong: New York University, World Sci., 1999.
16. Hahn, J. and Trebin, H.-R., in *High Performance Com- puting in Science and Engineering’99*, Krause, E. and Jager, W., Eds., Berlin, Heidelberg: Springer, 2000, p. 92.
17. Morse, Ph.M., *Phys. Rev.*, 1929, vol. 34, p. 57.
18. Konti, A., *Debye Temperature of Some Cubic Elements and Alkali Halides*, Ottawa: Univ. Ottawa, 1971.
19. Magomedov, M.N., *Tech. Phys.*, 2013, vol. 58, no. 12, p. 1789.
20. *Fizicheskie velichiny: Spravochnik* (Physical Quantities: Handbook), Grigor’ev, I.S. and Meilikhov, E.Z., Eds., Moscow: Energoatomizdat, 1991.
21. Deryagin, B.V. and Fedoseev, D.V., *Rost almaza i graf- ita iz gazovoi fazy* (Growth of Diamond and Graphite from the Gaseous Phase), Moscow: Nauka, 1977.

Translated by A. Sin’kov

HIGH TEMPERATURE Vol. 55 No. 2 2017