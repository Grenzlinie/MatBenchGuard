# X-RAY DOSE SCALING IN REFLEX TRIODES*

S.B. Swanekamp⁽ᵃ⁾, B.V. Weber, R.J. Commisso, and D.P
Murphy

Naval Research Laboratory
Washington, DC 20375, USA

V. J. Harper-Slaboszewicz
Sandia National Laboratories, Albuquerque, NM 87185, USA

J. Goyer and J. Riordan
L-3 Pulsed Sciences, San Leandro, CA 94577, USA

Calculations to determine the dose scaling from a low-impedance (~1 Ω) reflex triode with voltage and current have been performed. These calculations use the particle-in-cell code LSP¹ to follow the charged particle dynamics in a reflex triode. As electrons interact with the thin anode foil, the LSP code writes out the positions, energies, and direction cosines of the bremsstrahlung photons that are created. These photons are then read into the Monte-Carlo electron-photon transport code, ITS, to predict the radiation field emerging from the foil. In previous work, it was shown that an optimum foil thickness exists which maximizes the dose.² When the foil is thicker than the optimum, the 10-100 keV photons are increasingly self absorbed in the converter. For foils thinner than the optimum, the electrons leak out radially and return to ground without making useful radiation. The calculations presented here show that, for foil thicknesses equal to or greater than the optimum and voltages less than 2 MV, the dose per electron from the more complex LSP calculations which accurately predict the electron angles of incidence on the foil can be predicted by simple ITS calculations where normally-incident electrons reflex back and forth through the foil until they are stopped. Therefore, the dose-rate from experiments can be predicted from relatively simple ITS calculations provided the electron and ion current fractions and the voltage can be reliably measured. The LSP simulations show that the electron current increases slowly with voltage and asymptotes at about 1 MA while the ion current increases rapidly as $V^{3/2}$. Therefore, as the voltage increases the electron current becomes an increasingly smaller fraction of the total current and the ion current dominates. At 1 MV, the LSP simulations show that the ion current fraction is approximately 40% and increases to more than 60% at 2 MV. Furthermore, the absolute x-ray spectrum can be deduced from the ITS calculations to provide information about the spectral content of the x-rays.

¹LSP is a licensed software product of ATK
(http://www.mrcwdc.com/LSP/index.html)
²S. B. Swanekamp, B. V. Weber, S. J. Stephanakis, D.
Mosher, and R. J. Commisso, Phys. Plasmas 15, 083105
(2008).
⁽ᵃ⁾L3 Communications, Chantilly, VA

* Work supported by DTRA

978-1-4244-2636-2/09/$25.00 ©2009 IEEE