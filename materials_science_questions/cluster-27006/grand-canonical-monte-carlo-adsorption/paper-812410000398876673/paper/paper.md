# Computer Simulation Studies of Adsorption of
## Simple Gases on Alkali Metal Surfaces

M. J. Bojan,† M. W. Cole,† J. K. Johnson,**
W. A. Steele,† and Q. Wang**

†Departments of Chemistry and Physics, Penn State, University Park, PA 16802
**Department of Chemical and Petroleum Engineering, University of Pittsburgh,
Pittsburgh, PA 15260

Wetting properties of simple gases on alkali metal surfaces are of fundamental im-
portance because they manifest the least attractive gas-surface interactions in nature
and because their critical behavior is described by the two-dimensional Ising model.
We report simulation results for the adsorption of neon and hydrogen on alkali metal
surfaces. These use the grand canonical (classical) Monte Carlo and (quantum) path
integral Monte Carlo methods, respectively. We find a set of wetting transitions at
temperatures which are very sensitive to the adsorption potentials. Comparison is
made with recent experiments and with predictions of a model of Cheng, et al. in
which the transition temperature is estimated from a simple cost-benefit analysis
involving the surface tension and the adsorption potential.

## 1. INTRODUCTION

The problem of wetting is understood qualitatively in terms of the relative
strength of adhesive forces and cohesive forces. In the case of inert gases. it was
once expected that (complete) wetting should be the generic behavior because the
self-interaction well depth $\epsilon$ is small in comparison with the well depth D of the
adsorption potential on most surfaces. It therefore came as a surprise that the most
reactive surfaces, i.e. alkali metals, were predicted some years ago to not be wetttd
by these gases at low temperature T.¹⁻⁵ The basis for this prediction is that the
values of D on these surfaces are actually smaller than $\epsilon$ (as a consequence of the
repulsive electron-atom pseudopotential and the fact that the metal's electrons spill
out far from the surface). Cheng et al. used a simple model to predict the wetting
temperature $T_w$ in such circumstances:¹ using the Young criterion, their result was

$$(CD^{2})^{1/3}=3.33\sigma/n \tag{1}$$

Here C is the coefficient of the asymptotic van der Waals gas-surface interaction
and $\sigma$ and n are the surface tension and number density of the bulk liquid phase at
$T_w$. Eq. 1 implies that ultraweak adsorption systems have transition temperatures

close to the adsorbate's critical temperature $T_c$, since then the right side of Eq. 1 is small. Eq. 1 is in semiquantitative accord with predictions made with a superfluid density functional model (T=0), a classical density functional model, and a Monte Carlo calculation. $^{1,3,6,7}$ The model has had mixed success in relation to actual experiments for the He, Ne, and $H_2$ cases where wetting transitions have been observed. $^{8-11}$ The latter comparison, however, is complicated by the uncertainty in the assumed potential. As discussed elsewhere, $^{12}$ D has a typical uncertainty of perhaps $20 \%$, leading to a roughly comparable uncertainty in $T_w$. In order to assess Eq. 1 definitively, it is important to perform reliable statistical mechanics calculations of the adsorption behavior on the alkalis, which is what we report here. We treat two cases of particular interest, hydrogen and neon. $H_2$ was predicted $^2$ by Eq. 1 to exhibit a wetting transition on Rb near 19 K and on Cs near 20 K, i.e. about $60 \%$ of the critical temperature. The experiments find results $^{10}$ which are close to these predicted values. Ne was predicted by the same model to undergo wetting transitions on Rb and Cs within $5\%$ of the critical temperature. The reason for the higher relative temperature is that the Ne relative well depth $D/\epsilon$ is of order 0.3, while the $H_2$ relative well depth is of order unity for both Rb and Cs. The recent experiments find Ne to wet Rb at T about $98\%$ of $T_c$ and to exhibit drying behavior on Cs very close to $T_c.^{11}$ Thus Eq. 1 seems to be qualitatively useful in this ultraweak attraction situation. Simulations can provide a more precise assessment tool, being limited only by the statistics associated with simulation "time" and size effects associated with the dimensions of the simulation volume.

## 2. NEON

The adsorption of Ne has been studied with classical grand canonical Monte Carlo (GCMC) simulations. $^{13,14}$ The Ne-Ne interaction was taken to be of Lennard-Jones (LJ) form, with interaction parameters $\epsilon=33.9$ K and $\sigma=2.78$ Å. The Ne atom's interaction with the Rb surface was taken to be a sum of interactions with planes of substrate atoms, with the net interaction taken to represent the theoretical form:$^3$

$$V(z)=\left(4 C^{3}\right) /\left(27 D^{2} z^{9}\right)-C / z^{3} \tag{2}$$

For surfaces other than Rb, the assumption was made that the functional form of the potential is identical to that on Rb, but the well depth was varied from the value on Rb (14 K) by varying the strength of the gas-surface interaction. Since the shape of the potential in the case of other alkali metals is quite similar to that on Rb, this is a good approximation (including Li, D=50 K). No lateral variation of V was included because it is believed to be small for the case of alkali metals (since there is negligible adsorption at $z<5$ Å). In the cases D>50 K, the results pertain to no specific surface, but are of qualitative interest for future study of other weak-binding surfaces, e.g. alkaline earths. $^{12}$

In these simulations, the z=0 plane bounds the nominal substrate while the plane $z=L=75$ Å is a hard wall. The Ne atoms' positions are (x/y) periodically replicated versions of those within a cell of dimensions $27.8 × 27.8 × L$ Å. The results are critically sensitive to the value of D; the results reported here are only indicative of those to be found with a more extensive variation of D and T. Figures

![](./images/812410000398876673_1.jpg)

Fig. 1. Ne coverage vs. pressure at T=34.3 K as a function of assumed well depth. Ne wets the D=75 K surface but adsorbs negligbly on Li (D=50 K) below saturated vapor pressure, indicated by the vertical line.

1 and 2 exhibit one kind of phenomenon. One observes in Fig. 1 that at T=34.3 K a moderately attractive surface, D= 75 K, corresponds to a wetting situation (since the available space is almost filled with liquid just svp). In contrast, the case of D=50 K (Li) involves less than a single monolayer of Ne (below svp). This comparison is remarkable because the difference in well depths is less than T; the reason for the sensitivity to D is that we are near a wetting transition. This occurs near 39 K for the case D=50 K; we see in Fig. 2 isotherms at 40.7 K. Note the smooth film growth as a function of pressure for D=50, whereas there is negligible adsorption for the case of Rb (D=14 K). While the experiments of Hess et al show that Rb is wet at 43.4 K, this is too close to the critical temperature (44.4 K) for our simulations to accurately represent critical fluctuations. We have found strong nonwetting on both Rb and, of course, Cs (D=11 K) throughout the regime T < 42 K. The extension of our study to a broader range of interactions and temperatures is in progress, as is a more definitive characterization of the wetting transitions.

### 3. HYDROGEN

The path integral formalism¹⁵ was used to incorporate the quantum nature of the H₂ molecules. In previous papers we have derived extensions of the path integral hybrid Monte Carlo (PIHMC) method to the Gibbs and grand canonical ensembles.¹³,¹⁶,¹⁷ The method is used here for computing the adsorption of H₂ on Rb at T= 18, 22, and 30 K. We have used the Silvera-Goldman potential¹⁸ to describe the H₂-H₂ interactions. This potential has been shown to reproduce the

![](./images/812410000398876673_2.jpg)

Fig. 2. Same as Fig. 1, except at 40.7 K. Ne wets both D= 50 and 75 K surfaces, but adsorbs negligibly below saturated pressure for D= 14 K (Rb).

thermodynamic properties of fluid hydrogen over a wide temperature and pressure range. $^{13,16}$ The $Rb-H_{2}$ potential was taken from the work of Cheng et al. $^{2}$

We have used the multiple-time step PIHMC algorithm $^{19}$ to accomplish the molecular displacements. All molecules in the simulation cell are moved in a single PIHMC displacement. A single hybrid MC displacement move typically consists of five to ten long molecular dynamics time steps. The value of the long time step was adjusted during equilibration to give an acceptance rate of roughly $50 \%$. Each long time step consists of ten short time steps in our simulations. Details of the multiple-time step PIHMC simulations are presented elsewhere. $^{13,16,17}$ In the molecule creation step, a path is inserted in the box with a random position and orientation. The conformation of the inserted molecule is randomly picked from the conformations of the ideal gas ring polymer system. Conformations of the ideal gas system were generated as in previous bulk GCMC and Gibbs ensemble simulations. The probabilities of making a displacement, a molecule creation, or a deletion were set to 0.1, 0.45, and 0.45, respectively.

The path integral GCMC simulations were carried out in a simulation box with fixed volume, chemical potential, and temperature. Periodic boundary conditions in x and y directions were used. The bead-bead intermolecular cutoff was maintained at $5 \sigma$, where $\sigma=3.003 \AA$ is the effective size of the molecule, taken from the Silvera Goldman potential. The lateral dimensions of the box were set to be larger than $10 \sigma$. No fluid-fluid long range corrections were applied to the configurational properties. One wall of the box (in the x-y plane) was chosen as the Rb surface, and the other wall was chosen to be repulsive so as to keep the molecules in the simulation box, while avoiding the possibility of capillary condensation. The two

![](./images/812410000398876673_3.jpg)

Fig. 3. Adsorption isotherms of at 18, 22, and 30 K for $H_2$ on Rb. The chemical potential is reduced as discussed in the text. The 18 and 22 K isotherms show incomplete wetting behavior, while the 30 K isotherm shows complete wetting.

walls were separated by a distance of at least $6\ \sigma$ in order to minimize the effect of the repulsive wall on the isotherms.

The resulting isotherms are shown in fig. 3. At 18 K no significant adsorption is observed on the Rb surface until the entire simulation box fills with liquid hydrogen. This takes place between $\mu^\ast=-2.68$ and $\mu^\ast=-2.65$, where $\mu^\ast=\mu/\epsilon$ is the reduced chemical potential of the hydrogen; $\epsilon=32.21$ K is the well depth of the Silvera-Goldman potential. Plots of the density profile (not shown) reveal that the adsorption is always low while there is vapor in the box. The sharp increase in the amount adsorbed corresponds to liquid filling the simulation box.

The behavior at 22 K is very similar to that at 18 K; very little adsorption takes place until the simulation box fills with liquid. The vapor-liquid transition takes place between $\mu^\ast=-2.68$ and $\mu^\ast=-2.678$. Thus, the 22 K isotherm also indicates incomplete wetting. At 30 K, in contrast, the adsorption isotherm shows a continuous growth of the liquid film on the Rb surface. The density profiles show that the liquid film coexists with a low density gas away from the surface. Hence, the 30 K isotherm shows complete wetting behavior. Simulations currently in progress show preliminary evidence that a prewetting transition takes place at 27 K. Assuming that prewetting does occur at 27 K, our simulations indicate a wetting temperature above 22 K and a prewetting critical temperature somewhere between 27 and 30 K.

These simulation results yield the onset of wetting behavior at temperatures about $20\ \%$ higher than those found experimentally by Mistura, Lee, and Chan.${}^{10}$

This implies that the assumed adsorption potential is somewhat weaker than the true potential provided by the Rb surface. Simulation using a revised potential is evidently one direction for further study.

## 4. SUMMARY

Simulation results have been presented for the cases of Ne and $\text{H}_2$ adsorption on certain alkali metal surfaces. In the case of Ne, we make the prediction of a wetting transition on Li near 40 K. For $\text{H}_2$, comparison with experimental data implies that the theoretical potential underestimates the attraction. Our results demonstrate how simulation can be a valuable tool for both predicting new wetting transitions and testing model potentials by comparing results with existing experiments. The present results are suggestive of much more which can be accomplished with these techniques.

This research has benefitted from discussion with M. H. W. Chan and D. Ross, as well as support from NSF.

## REFERENCES

1. E. Cheng, M. W. Cole, W. F. Saam and J. Treiner, *Phys. Rev.* B46, 13967 (1992); Erratum B47, 14661 (1993).
2. E. Cheng, G. Mistura, H. C. Lee, M. H. W. Chan, M. W. Cole, C. Carraro, W. F. Saam and F. Toigo, *Phys. Rev. Lett.* 70, 1854 (1993).
3. E. Cheng, M. W. Cole, W. F. Saam and J. Treiner, *Phys. Rev.* B48, 18214 (1993).
4. M. W. Cole, E. Cheng, C. Carraro, W. F. Saam, M. R. Swift and J. Treiner, *Physica* B197, 254(1994); M. W. Cole, *J. Low Temp. Phys.* 101, 25 (1995).
5. J. Treiner, *Czech. J. Phys.* 46, Suppl. S6, 2957 (1996).
6. J. E. Finn and P. A. Monson, *Phys. Rev. A* 39, 6402 (1989).
7. E. Bruno, C. Caccamo, and P. Tarazona, *Phys. Rev.* A35, 1210 (1987).
8. P. Taborek and J. E. Rutledge, *PPhysica* B197, 283 (1994).
9. R. B. Hallock, *J. Low Temp. Phys.* 101, 31, 1995.
10. G. Mistura, H. C. Lee and M. H. W. Chan, *J. Low Temp. Phys.* 96, 221 (1994); D. Ross, J. E. Rutledge, and P. Taborek, to be published.
11. G. B. Hess, M. J. Sabatini and M. H. W. Chan, *Phys. Rev. Lett.* 78, 1739 (1997).
12. A. Chizmeshiya, M. W. Cole, and E. Zaremba, in these proceedings.
13. Q. Wang and J. K. Johnson, Fluid Phase Equilibria, in press, shows the accuracy of the classical approximation at the high temperatures relevant to this paper; for example, the liquid density at saturation is reduced by $\sim 5\%$ due to quantum effects.
14. Some related results for Ne adsorption are presented in M. J. Bojan, M. W. Cole, and W. A. Steele, submitted to *Phys. Rev. E*.
15. R. P. Feynman and A. R. Hibbs, *Quantum Mechanics and Path Integrals* (New York: McGraw-Hill, 1965).
16. Q. Wang, J. K. Johnson, and J. Q. Broughton, *Mol. Phys.* 89, 1105 (1996).
17. Q. Wang, J. K. Johnson, and J. Q. Broughton, submitted to *J. Chem. Phys.*
18. I. F. Silvera and V. V. Goldman, *J. Chem. Phys.* 69, 4209 (1978).
19. M. E. Tuckerman, B. J. Berne, G. J. Martyna, and M. L. Klein, *J. Chem. Phys.* 99, 2796 (1993).