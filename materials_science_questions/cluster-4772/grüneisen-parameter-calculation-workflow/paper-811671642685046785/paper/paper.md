# EQUATION OF STATE OF WARM CONDENSED MATTER

T. W. BARBEE III, D. A. YOUNG, F. J. ROGERS
Physics Dept., Lawrence Livermore National Laboratory, Livermore, CA 94550

## ABSTRACT

Recent advances in computational condensed matter theory have yielded accurate calculations of properties of materials. These calculations have, for the most part, focused on the low temperature (T=0) limit. An accurate determination of the equation of state (EOS) at finite temperature also requires knowledge of the behavior of the electron and ion thermal pressure as a function of T. Current approaches often interpolate between calculated T=0 results and approximations valid in the high T limit. Plasma physics-based approaches are accurate in the high temperature limit, but lose accuracy below $T{\sim}T_{Fermi}$. We seek to "connect up" these two regimes by using *ab initio* finite temperature methods (including linear-response[1] based phonon calculations) to derive an equation of state of condensed matter for $T{\leq}T_{Fermi}$.

We will present theoretical results for the principal Hugoniot of shocked materials, including carbon and aluminum, up to pressures P>100 GPa and temperatures $T>10^{4}K$, and compare our results with available experimental data.

## INTRODUCTION

An equation of state (EOS) is required for any continuum mechanics simulation, and for processes involving high energy densities, the EOS needs to cover a large range of the density and temperature. There is a longstanding need for more accurate EOS generation models and tabular representations[2]. In this paper we discuss two new models which will be useful in generating accurate EOS tables for hydrodynamic codes.

New data on compressed states of matter are available from the diamond anvil cell and from strong shockwave sources. These data are now numerous enough to stimulate improvements in theory and detailed comparisons between experiments and theory.

## THEORY

The EOS of a material can be derived from the free energy $F(T,V)=U-TS$. We separate $F$ into three components:

$$
F(T,V)=F_{0}(V)+F_{\text{ion}}(T,V)+F_{\text{el}}(T,V)
$$

where $F_{0}$ is the free energy of the material at zero temperature (the "cold curve"), $F_{\text{ion}}$ is the thermal contribution due to the ions, and $F_{\text{el}}$ is the thermal contribution due to the electrons. We calculate $F_{0}$ using a total-energy method based on the local density approximation (LDA) within density functional theory[3]. The calculation is carried out using a plane wave basis for the electron wavefunctions and pseudopotentials to remove the core electrons. The calculated electronic density of states is then used to determine the electron thermal energy $F_{\text{el}}$.

Linear response theory[1] is a method for computing lattice phonon frequencies within the electron band structure formalism. For a periodic atomic displacement corresponding

105
Mat. Res. Soc. Symp. Proc. Vol. 499 © 1998 Materials Research Society

![](./images/811671642685046785_1.jpg)

Figure 1: Experimental room temperature isotherm for diamond (points) compared with ab initio phonon theory (curve).

to a given phonon wave vector, a self-consistent electron band-structure calculation using the perturbed Hamiltonian yields the harmonic energy and the corresponding lattice mode frequencies $\omega_{\mathbf{q}\nu}$. The ion thermal energy $F_{\text{ion}}$ may then be obtained either directly from the phonon frequencies $\omega_{\mathbf{q}\nu}$, or a small number of phonon frequencies may be combined into an density-dependent effective Einstein frequency $\omega_E$. The Grüneisen parameter is then defined by $\gamma(V) = -\partial\ln\omega_E/\partial\ln V$ and the ion thermal pressure $P_{\text{ion}}$ may be calculated within the Grüneisen model from $P_{\text{ion}}=3RT\gamma(V)/V$.

The principal Hugoniot can then be derived from knowledge of the initial state $(P_0, V_0, E_0)$ using the Rankine-Hugoniot relation[4]

$$
E - E_0 = \frac{1}{2}(P + P_0)(V - V_0)
$$

RESULTS

We have carried out this calculation for carbon in the diamond structure, averaging over a small set of phonons to yield a density-dependent Einstein frequency. The sum of the vibrational free energy and static lattice energy provides a complete equation of state,

diamond hugoniot

![](./images/811671642685046785_2.jpg)

Figure 2: Experimental shock Hugoniot for diamond (points) compared with theory (curve).

since the electronic contribution is negligible for a wide-gap insulator such as diamond.

Comparison of theory and experiment is shown in Fig. 1 for the diamond room temperature isotherm[5] and in Fig. 2 for the principal shock Hugoniot[6]. The model predicts a normal density about 1% too large, and this gives a slight offset to the predictions. Remarkably, the model is in good agreement with shock data up to 6 Mbar, where diamond is predicted to melt. Hotter shock states can be obtained from porous diamond with starting densities below the normal density of $3.51\ \text{g/cm}^3$ and the agreement here is also good. Evidently diamond is very nearly a harmonic solid with negligible contributions from anharmonic and electronic terms.

One of the remarkable results from the ab initio phonon theory is the first-principles prediction of the Grüneisen gamma function. This function is frequently used as an empirical parameter, since it is only poorly known from experiments. The ab initio phonon theory has now made it possible to compute the Grüneisen function with much more confidence. The Grüneisen function for diamond is shown in Fig. 3.

Ab initio phonon theory can be applied with confidence to low-Z sp-bonded materials where the plane wave technique works well. The use of pseudopotentials allows application of the theory to some higher-Z and d-bonded materials. The theory should be helpful in

![](./images/811671642685046785_3.jpg)

Figure 3: Ab initio phonon theory prediction of the density dependence of Grüneisen gamma for diamond.

generating accurate Grüneisen functions for simple metallic, molecular, covalent, and ionic materials, and these can then be used to construct approximate Grüneisen functions for more complex solid materials.

**ACTEX**

ACTEX (Activity Expansion) is a dense plasma model based on the Abe cluster expansion of the partition function for a Coulomb gas of nuclei and electrons, combined with quantum corrections and a renormalization which includes a representation of atomic species in various states of ionization[7]. The ACTEX EOS predictions are exact for weakly coupled plasmas at very high temperature, and become less accurate as the condensed matter regime is approached. ACTEX includes the electron shell ionization region which occurs as a density maximum on the Hugoniot. Recently published ultrahigh pressure Hugoniot data from nuclear explosion and pulsed laser sources overlap the region of validity of ACTEX and a detailed comparison between the two is now possible.

The comparison has been made for D, Be, CH, $\mathrm{H_2O}$, Al, and $\mathrm{SiO_2}$[8]. The best overall comparison is with Al, for which nuclear explosion-driven shock experiments have been performed up to 4000 Mbar, where K and L shell ionization is occurring[9]. The comparison is shown in Fig. 4. The ACTEX curve shows two large density maxima which correspond to the ionization of the K and L electron shells. The data have large errors and so the test of the theory is not rigorous, but the theory shows the expected form and appears to be semiquantitative in the 10 - 100 Mbar region.

New shock data on liquid deuterium using high energy pulsed lasers have revealed a sharp density maximum in the Hugoniot[10]. This feature provides a very strong constraint

![](./images/811671642685046785_4.jpg)

Figure 4: Comparison of experimental (points) and ACTEX (curve) ultrahigh pressure shock Hugoniot of aluminum.

on any theory of dense, dissociating hydrogen. ACTEX is compared with the data in Fig.
5. The agreement is very good in that ACTEX closely approximates the density and pressure of the experiment near the Hugoniot maximum. Since the ACTEX model does not include the diatomic molecular fluid, it cannot make predictions for the lower part of the Hugoniot curve. Fig. 5 also shows other model predictions for the shock Hugoniot of deuterium. It is clear that there are major discrepancies between theoretical models, largely due to our limited understanding of dissociation in dense fluids.

Overall, ACTEX is in good agreement with experimental data. It appears that the AC- TEX shock pressures fall systematically slightly below the experimental pressures, which may indicate that the ACTEX treatment of the repulsive interactions between ionic cores, taken only to the second virial coefficient level, is not adequate.

## DISCUSSION

The ab initio phonon theory is accurate for the solid state and can be extended with corrections into the liquid state, but is valid only when the electronic excitations are neg- ligible, i.e., $T \ll T_{F}$. ACTEX is a plasma theory valid for conditions where condensed matter interactions are small, i.e., $T \gg T_{F}$. At present we lack a single theory which covers the entire temperature range from cold solid to hot plasma. A possible candidate for such a theory is the hot band structure model, in which the thermally excited states of the condensed phase are included in the self-consistent LDA calculation. This model should pass smoothly from the $T=0$ limit to the $T=\infty$ (one-component plasma) limit. Work on this model is underway at Livermore.

The two theories described here increase the precision of theoretical EOS modeling. The application of this work to hydrodynamic code calculations can best be done by

![](./images/811671642685046785_5.jpg)

Figure 5: Comparison of experimental (points), ACTEX (smooth curve), and other theoretical (dashed curves) shock Hugoniots for deuterium.

incorporating the results into simpler global EOS generators such as QEOS[2] by using adjustable parameters to fit the theoretical data as if it were experimental. Then smooth and consistent global EOS tables can be generated which incorporate the most accurate physics.

ACKNOWLEDGMENTS

This work was performed under the auspices of the U.S. DOE by LLNL under contract No. W-7405-ENG-48.

REFERENCES

1. P. Giannozzi, S. de Gironcoli, P. Pavone, and S. Baroni, Phys. Rev. B 43, 7231 (1991).

2. D. A. Young and E. M. Corey, J. Appl. Phys. 78, 3748 (1995).

3. J. Ihm, A. Zunger, and M. L. Cohen, J. Phys. C 12, 4409 (1979).

4. R. G. McQueen, S. P. Marsh, J. W. Taylor, J. N. Fritz, and W. J. Carter, in High-Velocity Impact Phenomena, edited by R. Kinslow (Academic, New York, 1970) Chap. 7.

5. I. V. Aleksandrov, A. F. Goncharov, A. N. Zisman, and S. M. Stishov, Zh. Eksp. Teor. Fiz. 93, 680 (1987) [Sov. Phys. JETP 66, 384 (1987)].

6. M. N. Pavlovskii, Fiz. Tverd. Tela 13, 893 (1971) [Sov. Phys. Solid State 13, 741(1971)].

7. F. J. Rogers, Phys. Rev. A 24, 1531(1981).

8. F. J. Rogers and D. A. Young, Phys. Rev. E **56**, 5876 (1997).

9. A. S. Vladimirov, V. N. Voloshin, V. N. Nogin, A. V. Petrovtsev, and V. A. Simonenko, Pis'ma Zh. Eksp. Teor. Fiz. **39**, 69 (1984) [JETP Lett. **39**, 82 (1984)].

10. L. B. Da Silva et al., Phys. Rev. Lett. **78**, 483 (1997).