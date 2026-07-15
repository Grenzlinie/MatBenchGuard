# Computer study of the specific heat for metallic liquids and glasses

J. Lu $^{1}$ and D.W. Qi

Guelph-Waterloo Program for Graduate Work in Physics, Waterloo Campus, University of Waterloo,
Waterloo, Ontario, Canada N2L 3G1

Received 18 February 1991; revised manuscript received 18 April 1991; accepted for publication 13 May 1991
Communicated by A.A. Maradudin

It is demonstrated that the specific heat behaves as a monotonically increasing function of temperature with falling temperature for those supercooled metallic liquids, which can be laboratory glasses. This is in contrast to cases where supercooled metallic liquids do not become laboratory glasses. In addition, a comment is made on the specific heat of a supercooled Lennard-Jones liquid.

The rate of crystal growth becomes so large for supercooled metallic liquids in the temperature range between a $T$ significantly below the melting temperature, $T_{\mathrm{m}}$, and the glass-transition temperature, $T_{\mathrm{g}}$, that these liquids are inaccessible to measurement. This is true even for such a supercooled metallic liquid as $\mathrm{Ni}_{0.4} \mathrm{Pd}_{0.4} \mathrm{P}_{0.2}$ alloy, which possesses an exceptionally high resistance to crystallization as compared with other metallic glass-forming systems [1,2]. As a result, the behaviour of the specific heat at constant pressure, $C_{p}(T)$, in the range $T_{\mathrm{g}}<T \ll T_{\mathrm{m}}$ was only estimated in refs. [1-3] by extrapolating the measured $C_{p}$ of the high-$T$ supercooled-liquid branch to the low-$T$ supercooled-liquid branch near $T_{\mathrm{g}}$. This extrapolation increases continuously with falling temperature and implies that the specific heat at constant volume, $C_{\Omega}$ (which is a dominant part of $C_{p}$ [4]), increases monotonically in going down from $T_{\mathrm{m}}$ to $T_{\mathrm{g}}$ for metallic liquids.

This implication deserves quantitative investigation, because the specific heat is an important property in the study of both the supercooled-liquid states and the liquid-glass transition. Therefore, we have carried out a computer calculation of the specific heats for the supercooled-liquid and glass states of the binary system $(\mathrm{Ca}_{0.7} \mathrm{Mg}_{0.3})$ consisting of 700 Ca atoms and 300 Mg atoms in a cube subject to the standard periodic boundary conditions. First, using the same atomic potentials (which include not only the two-body type interactions but also the volume dependent energies) and the same atomic volumes as in ref. [5] and following the procedure as described in ref. [6], the well-known molecular dynamic (MD) procedure is applied to prepare a liquid state configuration at a $T$ significantly above $T_{\mathrm{m}}$ and to determine the corresponding $C_{\Omega}$. Next, the temperature-quench computer simulation procedure is employed to prepare the possible metastable states of the system with the atomic volume being the same as in ref. [5] and to determine $C_{\Omega}$ at each temperature step in the transition from the liquid state to the glass state. The results thus obtained for the pair distribution functions (PDFs, which characterize the states of the system) are similar to those obtained from a Monte Carlo calculation [5]. As for the determination of $C_{\Omega}$, we remark that only the simulation results of the second 6000 time steps and those of the third 6000 time steps are taken into account, the results of these two groups being very similar. This is done because the energy fluctuations in the first 6000 time steps are too large to be accepted for the type of system considered. The values of $C_{\Omega}(T)$ thus determined are displayed in fig. 1 along with the corresponding error bars. Because the character of

1 On leave from Institute of Metal Research, Academia Sinica, Shenyang, China.

![](./images/812446301303078913_1.jpg)

Fig. 1. MD results of $C_{\Omega}k_{B}^{-1}$ for the rapidly quenched $\mathrm{Ca}_{0.7}\mathrm{Mg}_{0.3}$ metal, determined as described in the text.

![](./images/812446301303078913_2.jpg)

Fig. 2. The temperature dependence of $\Omega$ [5] and that of $\alpha_{p}$ (determined as described in the text) for the rapidly quenched $\mathrm{Ca}_{0.7}\mathrm{Mg}_{0.3}$ metal.

the temperature dependence is nearly the same for both $C_{\Omega}(T)$ (which gives the primary temperature dependence of $C_{p}$ [4]) and $\alpha_{p}(T)$ (the thermal expansion coefficient at constant pressure) [7], the temperature dependence of $C_{\Omega}(T)$ (fig. 1) can be understood readily by considering the corresponding temperature dependence of $\alpha_{p}$ (fig. 2), obtained from $\alpha_{p}=(\partial\Omega/\partial T)_{p}/\Omega$ using the above-noted atomic volumes, $\Omega(T)$. These $\Omega$'s were determined in ref. [5] from $\partial F/\partial\Omega=0$ using a Helmholtz free energy $F$ including also the above-noted volume dependent energies, which are dominant in the determination of $\Omega$. Hence, the $\alpha_{p}$'s, displayed in fig. 2, include volume dependent effects and are reliable. Now, the results in fig. 1 for $T>780$ K (which is about $T_{\mathrm{g}}$ for the present case [5]) show that the specific heat behaves as a monotonically increasing function of temperature in decreasing from $T_{\mathrm{m}}$ to $T_{\mathrm{g}}$ for the binary alloy $\mathrm{Ca}_{0.7}\mathrm{Mg}_{0.3}$, which can be formed into a metallic glass in the laboratory through the liquid-quenching process. This is consistent with the above-noted extrapolation.

In order to check whether this behaviour in the specific heat is generally true, the same computer calculation is carried out for pure Na metal ($T_{\mathrm{g}}\approx0.37T_{\mathrm{m}}$ from computer simulations [8]) by using the same atomic potentials as in ref. [9]. The calculated results for the PDFs are displayed in fig. 3 and those for $C_{\Omega}(T)$ in fig. 4. The PDFs indicate that the transition from the liquid-like phase to the glass-like phase occurs at $T\approx0.373T_{\mathrm{m}}$ (=140 K), i.e., $T_{\mathrm{g}}\approx140$ K, in the computer calculation for Na. Now, the behaviour of the $C_{\Omega}(T)$ for Na (fig. 4) is as follows: At first, $C_{\Omega}$ increases in decreasing from $T_{\mathrm{m}}$ to a lower $T$, next, $C_{\Omega}$ decreases rapidly and then very slowly with further decrease in $T$, finally, $C_{\Omega}$ increases again as $T$ approaches $T_{\mathrm{g}}$. This temperature dependence can also be understood by considering the temperature dependence of the corresponding $\alpha_{p}$ (fig. 5), obtained from the presently determined $\Omega(T)$ (see ref. [4] for this determination). Now, because the slope of the $\Omega$-$T$ curve changes rather

![](./images/812446301303078913_3.jpg)

Fig. 3. Temperature-quench results for the PDFs of pure Na metal (for which $T_{\mathrm{m}}=312.64$ K). The second peak of the PDF at $0.373T_{\mathrm{m}}$ tends to split into two subpeaks.

![](./images/812446301303078913_4.jpg)
Fig. 4. MD results of $C_{\Omega} k_{B}^{-1}$ for the rapidly quenched Na metal.

![](./images/812446301303078913_5.jpg)
Fig. 5. The temperature dependences of $\Omega$ and $\alpha_{p}$ for the rapidly quenched Na metal (determined as described in the text).

abruptly around $T \approx 250$ K, which is considerably greater than $T_{g}, \alpha_{p}(T)$, and thereby $C_{\Omega}(T)$, varies anomalously in the vicinity of this $T$ and is different from the $Ca_{0.7} Mg_{0.3}$ case (figs. 1 and 2). This suggests that the supercooled-liquid region from $T_{m}$ to $T_{g}$ for the pure Na metal consists of two distinct structural regimes. A further result and discussion along this line will be published elsewhere.

In summary, it turns out that the implication of the above-mentioned extrapolation applies only to those supercooled metallic liquids for which $T_{g}$ is sufficiently high so that the corresponding supercooled-liquid region is essentially of a simple structural type. Also, it appears that the specific heat first increases with decrease in $T$ and then decreases dras tically with further decrease in $T$ in the transition from the supercooled-liquid state to the glass state.

In addition, it is found that the temperature depen- dence of $\Omega(T)$ obtained herein for pure Na metal is similar to that determined in ref. [10] for supercooled Ar liquid, which also cannot be a laboratory glass ( $T_{g} \approx 0.5 T_{m}$ for Ar from computer simulations [10]). Accordingly, the anomalous change in the specific heat at a $T$ significantly above $0.5 T_{m}$ in the MD calculation for the Ar liquid [11] should not be related to the liquid-glass transition, as has been customarily done in the literature (see ref. [11] for example) but to a transition between two different structural regimes in its supercooled-liquid region.

The authors would like to thank Professor S. Wang for his guidance. This work has been supported by the NSERC of Canada.

## References
[1] H.W. Kui and D. Turnbull, J. Non-Cryst. Solids 94 (1987) 62.
[2] P.V. Evans, A. Garcia-Escorial, P.E. Donovan and A.L. Greer, in: Phase transitions in condensed systems, eds. G.S. Cargill III, F. Spaepen and K.N. Tu, Mater. Res. Sol. Prog. 57 (1986) 239.
[3] H.S. Chen and D. Turnbull, J. Appl. Phys. 38 (1967) 3646; J. Chem. Phys. 48 (1968) 2560.
[4] H. Nakano, D.W. Qi and S. Wang, J. Chem. Phys. 90 (1989) 1871.
[5] D.H. Li, R.A. Moore and S. Wang, J. Chem. Phys. 88 (1988) 2700.
[6] J.L. Lebowitz, J.K. Percus and L. Verlet, Phys. Rev. 153 (1967) 250.
[7] H.S. Chen and K.A. Jackson, in: Metallic glasses (American Society for Metals, Metals Park, OH, 1976) p. 74.
[8] S.K. Lai and M.S. Lin, J. Non-Cryst. Solids 117/118 (1990) 907.
[9] D.H. Li, X.R. Li and S. Wang, J. Phys. F 16 (1986) 309.
[10] S. Nosé and F. Yonezawa, Solid State Commun. 56 (1985) 1005.
[11] M. Kimura and F. Yonezawa, in: Topological disorder in condensed matter, eds. F. Yonezawa and T. Ninomiya (Springer, Berlin, 1983) p. 80.