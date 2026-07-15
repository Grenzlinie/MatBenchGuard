phys. stat. sol. (b) 96, 469 (1979)
Subject classification: 13.1; 21.7; 22.1.1; 22.1.2

Faculty of Electronic Engineering, Niš (a) and Laboratory for Theoretical Physics,
Boris Kidrić Institute of Nuclear Sciences, Belgrade (b)

# Model Pseudopotential for Elementary Semiconductors

By
D. R. MAŠOVIĆ¹) (a) and S. ZEKOVIĆ (b)

A simple model pseudopotential, particularly suitable for energy band calculations in elementary semiconductors, is presented. It includes the Veljkovié-Slavie's general model pseudopotential and phenomenological correction. This correction represents a sum of spherical Bessel functions of higher order with the coefficients obtained by fitting the form factor of the pseudopotential to the experimental values of the transition energies around the energy gap. The band structures of Si, Ge, and $\alpha$-Sn are calculated and agree well with the experimental data. This pseudopotential is tested by calculating the resistivity of liquid Si, Ge, and Sn.

On propose dans ce travail un simple modele de pseudopotential permettant le calcul des bandes d'énergie des semiconducteurs élémentaires. Il contient le modele général du pseudopotentiel de Veljkovié et de Slavié une correction phénoménologique sous forme d'une somme des fonctions spheriques de Bessel et avec les coefficients obtenus par l'accommodement des facteurs de forme de ce pseudopotentiel aux valeurs expérimentales de l'énergie de transitions autour de la bande interdite. Les bandes d'énergie de Si, de Ge et de $\alpha$-Sn sont calquées et elles s'accordent tres bien avec les données expérimentales. Ce pseudopotentiel est testé par le calcul de la résistance de Si, de Ge et de Sn dans la phase liquide.

## 1. Introduction
The general model pseudopotential²) [1] has been proposed for simple metals as a func- tion of atomic number and successfully applied to investigations of metals [2 to 4], alloys, and intermetallic compounds [5], and even in biological systems [6].

The results for the energy bands of Si, Ge, and $\alpha$-Sn obtained by the VS pseudopoten tial are useless, especially for energy levels of $\Gamma_{2}'$ type which strongly affect many elec tronic characteristics of these materials. A phenomenological correction of the VS pseudopotential based on calculation of the energy band of Al is given in [7]. Following the same idea, the pseudopotential mVS capable of describing the known band struc- ture of elementary semiconductors is suggested in this work.

The band structure of the elementary semiconductors can be obtained by solving the secular equation
$$\operatorname{det}\left|\left\{(\boldsymbol{k}-\boldsymbol{g})^{2}-\varepsilon(\boldsymbol{k})\right\} \delta_{\boldsymbol{g} \boldsymbol{g}^{\prime}}+S\left(\boldsymbol{g}-\boldsymbol{g}^{\prime}\right)\left\langle\boldsymbol{k}+\boldsymbol{g}|w| \boldsymbol{k}+\boldsymbol{g}^{\prime}\right\rangle\right|=0, \quad(1)$$
where $\varepsilon(k)$ is in Ryd. In (1), $g$ and $g'$ are vectors of the reciprocal lattice, while $S(g-g')$ is the geometrical structure factor of the lattice and $\langlek+g|w| k+g'\rangle$ is the pseudopotential form factor.

## 2. Pseudopotential and Method of Fitting
For the form factor of the mVS pseudopotential we take
$$\langle\boldsymbol{k}+\boldsymbol{q}|w| \boldsymbol{k}\rangle=\beta_{1} \beta_{2} \mathrm{j}_{0}\left(\frac{2 \pi \beta_{2} q}{2 k_{\mathrm{F}}}\right)+\sum_{i=1}^{3} C_{i} \mathrm{j}_{i}\left(\frac{2 \pi \beta_{2} q}{2 k_{\mathrm{F}}}\right).\quad(2)$$

¹) Permanent address: Božidara Adžije 26a/IV, st. 15, 18000 Niš, Yugoslavia.
²) We are going to label Veljkovié and Slavié's general model pseudopotential with VS. and its modified version with mVS.

The first term in (2) corresponds to the VS pseudopotential. Its parameters $\beta_{1}$ and $\beta_{2}$ are obtained by using the Animalu-Heine results [8], based on the Heine-Abarenkov model potential [9]. They are connected by the following relation:

$$
\beta_{1} \beta_{2}=-\frac{2}{3} \varepsilon_{\mathrm{F} 0}. \tag{3}
$$

Here $\varepsilon_{\mathrm{F} 0}$ is the free-electron Fermi level. The values of these parameters are shown in Table 1 of [1], $\mathrm{j}_{0}, \mathrm{j}_{1}, \mathrm{j}_{2}$, and $\mathrm{j}_{3}$ are spherical Bessel functions of zero, first, second, and third order, respectively.

The unknown coefficients $C_{1}, C_{2}$, and $C_{3}$ in (2) are determined by fitting the solution of (1) to the experimental values of transition energies near the band gap of the given semiconductors, according to Cohen and Bergstresser [10].

The procedure of the fitting method consists of the following steps:

1.  As input data we take: a) three form factors of some well-known phenomenolo- gical pseudopotential that give a good energy band, and b) limits of reliability of the solution of (1) with reference to the experimental data.
2.  For solving (1) we apply Brust's modification of Löwdin's perturbation tech- nique [11] with the parameters $N$ and $\Gamma$ chosen so that the convergence of the solution of (1) is within the limits of reliability.
3.  The initial values of coefficients $C_{1}, C_{2}$, and $C_{3}$ in (2) are calculated from the con dition that the mVS pseudopotential goes through the input phenomenological form factors.
4.  From three form factors we determine the optimum one in this sense that its changes provide us a possibility to follow the changes of the band structure in the best way.
5.  Now, we change the value of the optimum form factor at the last decimal, $^{3)}$ and then we calculate the coefficients of the mVS pseudopotential. If this step causes changes in the band structure above the chosen limits of reliability we are reducing the form factor's last decimal alteration until we get the band structure changes within the limits of reliability. If such an alteration of the last decimal does not exist, from the optimum form factor and its varieties we take such one for which the calculated transition energies around the band gap are closest to the experimental data. Then the procedure 5 is repeated for the next decimal. Once, when we find the necessary step, we search for such a value of the form factor which provides the best agreement with experimental transition energies around the energy gap, and definitely determine the coefficients $C_{1}, C_{2}$, and $C_{3}$ of the pseudopotential (2).

![](./images/811978364054142976_1.jpg)

Fig. 1. mVS pseudopotential form factor $w(q)$. (a) Si, (b) Ge, and (c) $\alpha$-Sn

$^{3)}$ For instance, the greatest step at the last decimal is 0.09 Ryd for the optimal form factor $w=x . x x$ Ryd.

**Table 1**
The optimum values and accuracy of the form factors $w(220)$ for Si, Ge, and $\alpha$-Sn, and the coefficients (all the data are given in Ryd)

|              | Si      | Ge      | $\alpha$-Sn |
|--------------|---------|---------|-------------|
| $w(220)$     | 0.0390  | 0.0000  | $-0.0120$   |
| accuracy     | 0.0005  | 0.0005  | 0.0005      |
| $C_1$        | 0.1475  | 0.2035  | 0.2600      |
| $C_2$        | $-0.3490$| $-0.6803$| $-0.6285$   |
| $C_3$        | 0.1092  | 0.3914  | 0.3803      |

### 3. Results and Conclusion

In [12] it is mentioned that the limit of accuracy of the experimental transition energies obtained from the optical and photoemission spectra is $\pm 0.05$ eV. By choosing Löwdin's parameters $N=50$ and $\Gamma=89$ we provide the convergence for the solution of (1) about 0.01 eV, which is within the experimental accuracy. As input data in point 1a, the form factors of Cohen and Bergstresser [10] are taken. For the optimum form factor, $w(220)$ is chosen, while the other form factors $w(111)$ and $w(311)$ have the values given in [10]. According to the procedure 5, we calculate the coefficients $C_1$,

**Table 2**
The transition energies for Si, Ge, and $\alpha$-Sn (in eV) compared with the experimental data

|              | Si        |           | Ge        |           | $\alpha$-Sn |           |
|--------------|-----------|-----------|-----------|-----------|-------------|-----------|
|              | mVS       | exp.      | mVS       | exp.      | mVS         | exp.      |
| $\Gamma_2'-\Gamma_{25}'$ | 4.15 | 4.15 [14] | 0.97 | 0.99 [17] | $-0.20$ | $-0.16$ [21] |
| $\Gamma_{15}-\Gamma_{25}'$ | 3.35 | 3.41 [15] | 3.18 | 3.23 [17] | 2.60 | 2.9 [10] |
| $\text{L}_1-\Gamma_{25}'$ | 2.07 | — | 1.00 | 0.84 [18] | 0.68 | 0.32 [21] |
| $\text{X}_1(\Delta_1)-\Gamma_{25}'$ | — | — | 1.49 | 1.26 [19] | 1.60 | — |
| $\text{L}_1-\text{L}_3'$ | 3.31 | 3.40 [16] | 2.19 | 2.34 [17] | 1.39 | 1.4 [10] |
| $\text{L}_3-\text{L}_3'$ | 5.41 | 5.1 [14] | 5.39 | 5.80 [20] | 4.33 | 4.4 [22] |
| $\text{X}_1-\text{X}_4$ | 4.12 | 4.3 [16] | 3.98 | 4.50 [17] | 3.29 | 3.5 [10] |

**Table 3**
The resistivities of liquid Si, Ge, and Sn. ($\varrho_{\text{e}}$ is the experimental resistivity at the indicated temperature. $\varrho_{\text{HAA}}$, $\varrho_{\text{SR}}$, and $\varrho_{\text{AS}}$ are resistivities calculated by Animaly-Heine, Srivastava, and Ashcroft's pseudopotential, respectively [4]. $\varrho_{\text{VS}}$ and $\varrho_{\text{mVS}}$ are, respectively, resistivities calculated by VS and mVS pseudopotentials. All resistivities are given in $\mu\Omega$ cm.)

|     | $T$ ($^\circ$C) | $\varrho_{\text{e}}$ | $\varrho_{\text{HAA}}$ | $\varrho_{\text{SR}}$ | $\varrho_{\text{AS}}$ | $\varrho_{\text{VS}}^*$ | | $\varrho_{\text{mVS}}$ |
|-----|-----------------|----------------------|------------------------|-----------------------|-----------------------|-------------------------|-|-------------------------|
|     |                 |                      |                        |                       |                       | (a)                     | (b) |                         |
| Si  | 1410            | 71                   | 28.8                   | —                     | —                     | 52.6                    | 134.0 | 43.6 |
| Ge  | 937             | 73                   | 40.8                   | —                     | —                     | 55.5                    | 60.5 | 84.3 |
| Sn  | 410             | 48                   | 34.8                   | 62.3                  | 32.4                  | 57.9                    | 83.7 | 54.7 |

*) The resistivities in columns (a) and (b) are calculated according to the formulas (2) and (3) in [4], respectively.

![](./images/811978364054142976_2.jpg)

Fig. 2

$C_{2}$, and $C_{3}$ (Table 1). The form factors of the mVS pseudopotential for Si, Ge, and $\alpha$-Sn are shown in Fig. 1.

The transition energies for Si, Ge, and $\alpha$-Sn are presented in Table 2, compared with the experimental data. The corresponding energy bands are shown in Fig. 2 a, b, and c.

The present calculation does not include spin-orbit effects. For $\alpha$-Sn we have considered the centre of gravity of spin-orbit split levels for comparison with transition energies (given in Table 2) according to the procedure of Cohen-Bergstresser [10] and Anda-Majlis [13].

The results for transition energies obtained by the mVS pseudopotential are more precise and in a better agreement with experimental data than for the well-known Cohen and Bergstresser results, especially for the very important transitions around the band gap: $\Gamma_{2}'-\Gamma_{25}', \mathrm{~L}_{1}-\mathrm{L}_{3}^{\prime}$, and $\mathrm{X}_{1}-\mathrm{X}_{4}$.

This pseudopotential has been tested by calculating the resistivities of Si, Ge, and Sn in the liquid phase according to Ziman's theory [23]. The results obtained by the use of the theoretical struture factor, computed from the Percus-Yevick equation for a model liquid consisting of hard spheres, are given in Table 3.

![](./images/811978364054142976_3.jpg)

Fig. 2. Band structure of a) Si, b) Ge, c) $\alpha$-Sn

The good agreement of the resistivities $\varrho_{\mathrm{e}}$ and $\varrho_{\mathrm{mvs}}$ in case of Si, Ge, and Sn indicates that the pseudopotential (2) could be applied to investigations of other electronic properties of these semiconductors.

### Acknowledgements
The authors are thankful to Dr. F. Vukajlović and Dr. V. Veljković for their interest shown in this work and for useful advices.

### References
[1] V. VELJKOVIĆ and I. SLAVIĆ, Phys. Rev. Letters 29, 105 (1972).
[2] V. VELJKOVIĆ, Phys. Letters A 45, 41 (1973).
[3] V. VELJKOVIĆ and D. I. LALOVIĆ, Phys. Rev. B 11, 4242 (1975).

474
D. R. MAŠOVIĆ and S. ZEKOVIĆ: Model Pseudopotential for Semiconductors

[4] F. R. VUKAJLOVIĆ, S. ZEKOVIĆ, and V. VELJKOVIĆ, Physica (Utrecht) 92B, 66 (1977).

[5] M. BLAŽON, B. STANOJEVIĆ, and V. VELJKOVIĆ, Scripta metall. 1, 1153 (1975).

[6] V. VELJKOVIĆ and D. I. LALOVIĆ, Cancer Biochem. Biophys. 1, 295 (1976).

[7] D. R. MAŠOVIĆ and S. ZEKOVIĆ, phys. stat. sol. (b) 89, K57 (1978).

[8] A. D. E. ANIMALU and V. HEINE, Phil. Mag. 12, 1249 (1965).

[9] V. HEINE and I. ABARENKOV, Phil. Mag. 9, 451 (1964).

[10] M. L. COHEN and T. K. BERGSTRESSER, Phys. Rev. 141, 789 (1966).

[11] D. BR UST, Phys. Rev. 134, A1337 (1964).

[12] K. C. PANDEY and J. C. PHILLIPS, Phys. Rev. B 9, 1552 (1974).

[13] E. V. ANDA and N. MAJLIS, Nuovo Cimento B15, 225 (1973).

[14] W. E. SPICER and R. C. EDEN, Proc. Internat. Conf. Semicond. Phys., Moscow 1968, Izd. Nauka, Leningrad 1968.

[15] M. WELKOWSKY and R. BRAUNSTEIN, Phys. Rev. B 5, 497 (1972).

[16] R. R. L. ZUCCA, J. P. WALTER, Y. R. SHEN, and M. L. COHEN, Solid State Commun. 8, 627 (1970).

[17] D. E. ASPNES, Phys. Rev. Letters 31, 230 (1973).

[18] J. E. FISCHER, Proc. X. Internat. Conf. Phys. Semicond., MIT Press, Cambridge (Mass.) 1971 (p.427).

[19] F. HERMAN, R. L. KORTUM, D. C. KUGLIN, and R. A. SHORT, Quantum Theory of Atoms, Molecules, and Solid State, Academic Press, New York 1966.

[20] R. R. L. ZUCCA and Y. R. SHEN, Phys. Rev. B 1, 2669 (1970).

[21] S. GROVES and W. PAUL, Proc. Internat. Conf. Phys. Semicond., Paris 1964 (p. 41).

[22] M. CARDONA, P. MCELROY, and K. L. SHAKLEE, Solid State Commun. 4, 319 (1966).

[23] J. M. ZIMAN, Phil. Mag. 6, 1013 (1961).

( Received July 16, 1979)