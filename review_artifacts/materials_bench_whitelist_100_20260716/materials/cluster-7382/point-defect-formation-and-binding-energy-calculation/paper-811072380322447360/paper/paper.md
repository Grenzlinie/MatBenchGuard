PII S1359-6462(97)00087-0

# AB-INITIO CALCULATION OF EFFECTIVE FORMATION VOLUMES FOR ATOMIC DEFECTS IN B2-FeAl

J. Mayer and M. Fähnle

Institut für Physik, Max-Planck-Institut für Metallforschung
Heisenbergstr. 1, D-70569 Stuttgart, Germany

(Received December 30, 1996)
(Accepted January 30, 1997)

## Introduction

Intermetallic compounds are promising candidates for high-temperature applications [1]. A detailed knowledge of the properties of defects thereby is required to understand the mechanical behaviour concerning high-temperature creep (atomic defects) and plasticity (dislocations, including their interactions with atomic defects). Powerful tools for the identification of atomic defects are measurements at finite pressure. For instance, the results for the pressure dependence of the positron lifetime for non-stoichiometric B2-FeAl [2] point to the existence of composite defects with formation volumes larger than the mean atomic volume $\bar{\Omega}_{0}$. However, it is not clear whether the composite defects also contribute significantly to the diffusion. Information concerning the diffusion mechanism itself is obtained from the pressure dependence of the diffusion coefficient. For instance, such measurements on $D_{3}-Fe_{3} Si$ [3] revealed an activation volume for the diffusion (which is the sum of the formation and the migration volume) which is again larger than the mean atomic volume. This large activation volume was attributed to vacancy-mediated Fe diffusion, in which divacancies or even larger vacancy clusters are involved. It should be taken into account that this does not necessarily mean that all vacancies of the composite defect are directly involved in the diffusion process. It might well be that such vacancy clusters form because of thermodynamic reasons but that only one vacancy of the composite defect is directly used as diffusion vehicle.

It was outlined in recent papers [4,5] that the interpretation of finite-pressure data is further aggravated by the fact that in compounds it is not possible to create just one type of defect (vacancy or antistructure atom on one sublattice) but that various defects must appear simultaneously in order to maintain the composition and homogeneity of the sample. This was demonstrated explicitly for a system near stoichiometry where deviations from the ideal structure due to small deviations from stoichiometry ("structural defects") or to finite temperature effects ("thermal defects") may be described within the framework of a generalized grandcanonical formalism by a few simple grandcanonical excitations, for instance, removal of atoms from the system or generation of antistructure atoms. To be more specific, if we consider only single vacancies and antistructure atoms but no composite defects, the concentration of Fe monovacancies, $c_{V}^{\mathrm{Fe}}$, in B2-Fe $_{x} \mathrm{Al}_{1-x}$ near $x=0.5$ is given by [4,5]

$$
c_{V}^{\mathrm{Fe}}=\frac{1}{2} e^{s_{V}^{\mathrm{Fe}} / k_{B}} \frac{e^{-\left(\varepsilon_{V}^{\mathrm{Fe}}+\mu_{\mathrm{Fe}}+p \Delta V_{V}^{\mathrm{Fe}}\right) / k_{B} T}}{1+e^{s_{V}^{\mathrm{Fe}} / k_{B}} e^{-\left(\varepsilon_{V}^{\mathrm{Fe}}+\mu_{\mathrm{Fe}}+p \Delta V_{V}^{\mathrm{Fe}}\right) / k_{B} T}+e^{s_{\mathrm{Al}}^{\mathrm{Fe}} / k_{B}} e^{-\left(\varepsilon_{\mathrm{Al}}^{\mathrm{Fe}}-\mu_{\mathrm{Al}}+\mu_{\mathrm{Fe}}+p \Delta V_{\mathrm{Al}}^{\mathrm{Fe}}\right) / k_{B} T}} \quad \text {. (1) }
$$

Here $\varepsilon_{V}^{\mathrm{Fe}}, s_{V}^{\mathrm{Fe}}$, and $\Delta V_{V}^{\mathrm{Fe}}$ ("local relaxation volume") describe the change of energy, vibrational entropy and volume of the system when removing an Fe atom; $\varepsilon_{\mathrm{Al}}^{\mathrm{Fe}}, s_{\mathrm{Al}}^{\mathrm{Fe}}$, and $\Delta V_{\mathrm{Al}}^{\mathrm{Fe}}$ are the corresponding changes upon creation of an Al antistructure atom on the Fe sublattice, and $\mu_{\mathrm{Fe}}, \mu_{\mathrm{Al}}$ are the chemical potentials which depend on temperature $T$, pressure $p$ and on the above introduced defect parameters $\varepsilon_{i}, s_{i}$ and $\Delta V_{i}$ for all possible vacancies and antistructure atoms. As a result, if we define the effective vacancy formation energy, $\tilde{E}_{V}^{\mathrm{Fe}}$, and the effective vacancy formation volume, $\tilde{\Omega}_{V}^{\mathrm{Fe}}$, in the same way as in monoatomic crystals, i.e. via

$$
\tilde{E}_{V}^{\mathrm{Fe}}=-k_{B} \partial \ln c_{V}^{\mathrm{Fe}} / \partial\left(\frac{1}{T}\right)
\tag{2}
$$

and

$$
\tilde{\Omega}_{V}^{\mathrm{Fe}}=-k_{B} T \partial \ln c_{V}^{\mathrm{Fe}} / \partial p,
\tag{3}
$$

these quantities do not depend only on the defect parameters $\varepsilon_{V}^{\mathrm{Fe}}, s_{V}^{\mathrm{Fe}}$, and $\Delta V_{V}^{\mathrm{Fe}}$ of the Fe vacancy but on the corresponding defect parameters of all considered defects. Then the effective formation volume $\tilde{\Omega}_{V}^{\mathrm{Fe}}$ does no longer have the simple geometrical meaning of the change in system volume when removing an Fe-atom from the bulk and inserting it at a typical surface site, as it was the case in a monoatomic crystal, i.e.

$$
\tilde{\Omega}_{V}^{\mathrm{Fe}} \neq \Omega_{V}^{\mathrm{Fe}}=\Delta V_{V}^{\mathrm{Fe}}+\bar{\Omega}_{0}.
\tag{4}
$$

For example, if stoichiometric FeAl was a pure triple-defect system, i.e. if only Fe vacancies and Fe antistructure atoms on the Al sublattice appeared, we would find [4]

$$
\tilde{\Omega}_{V}^{\mathrm{Fe}}=\tilde{\Omega}_{\mathrm{Fe}}^{\mathrm{Al}}=\frac{2}{3} \Delta V_{V}^{\mathrm{Fe}}+\frac{1}{3} \Delta V_{\mathrm{Fe}}^{\mathrm{Al}}+\frac{2}{3} \bar{\Omega}_{0},
\tag{5}
$$

whereas for a pure antistructure-type system, i.e., if only Fe and Al antistructure atoms were created, we obtain

$$
\tilde{\Omega}_{\mathrm{Fe}}^{\mathrm{Al}}=\tilde{\Omega}_{\mathrm{Al}}^{\mathrm{Fe}}=\frac{1}{2}\left(\Delta V_{\mathrm{Fe}}^{\mathrm{Al}}+\Delta V_{\mathrm{Al}}^{\mathrm{Fe}}\right).
\tag{6}
$$

In special cases it might even appear that the effective formation volume for a monovacancy exceeds the mean atomic volume [4].

### Calculational Procedure

It has been shown [6,7] that FeAl is neither a pure triple-defect system nor a pure antistructure-type system, and then the effective formation volumes have to be evaluated numerically from eq. (3). To do this, we determined the defect parameters $\varepsilon_{i}$ and $\Delta V_{i}$ (the formation entropies $s_{i}$ were neglected) for the various defects $i$ within the framework of the ab-initio pseudopotential theory (for details, see Ref. 6). Thereby a supercell approach is used, i.e. supercells containing 32 sites and one atomic defect, respectively, were repeated periodically. The defect parameters are defined as $\varepsilon_{i}=E_{i}-E$, where $E_{i}$ and $E$ are the total energies of the supercell with defect and of the perfect supercell, both in mechanical equilibrium, i.e. $\partial E_{i} / \partial V=\partial E / \partial V=\partial \varepsilon_{i} / \partial V=0$. Hence there are no implicit contributions to $\tilde{\Omega}_{i}$ arising from terms $\frac{\partial c_{i}}{\partial \varepsilon_{i}} \frac{\partial s_{i}}{\partial V} \frac{\partial V}{\partial p}$. For a calculation of the local relaxation volume $\Delta V_{V}^{\mathrm{Fe}}$, for instance, an Fe-atom is removed from the system at zero external pressure, the atoms surrounding the Fe vacancy are allowed to relax while fixing the supercell volume and then the supercell volume is relaxed while scaling linearly the interatomic distances, yielding $\Delta V_{V}^{\mathrm{Fe}}$. The equilibrium volume is obtained from the minimum of an universal binding curve which is fitted to the data for the total energy of the supercell for various volumes. Because the energy depends only weakly on the volume, the small numerical scatter in the data induces an uncertainty for the

<table>
<caption>TABLE 1
Local Relaxation Volumes $\Delta V$, Effective Formation Volumes $\bar{\Omega}$, and Fictitious Formation Volumes $\Omega$
According to Eq. (4) for Various Atomic Defects in Stoichiometric FeAl and in $Fe_{0.52}Al_{0.48}$ (numbers in brackets)
at $T=1300$ K, All in Units of the Mean Atomic Volume $\bar{\Omega}_{0}$.</caption>
<tbody>
<tr>
<td></td>
<td>Fe vacancy</td>
<td>Al vacancy</td>
<td>Fe antistructure atom</td>
<td>Al antistructure atom</td>
</tr>
<tr>
<td>$\Delta V$</td>
<td>$-0.2\pm0.2$</td>
<td>$-0.7\pm0.2$</td>
<td>$-0.4\pm0.2$</td>
<td>$0.4\pm0.2$</td>
</tr>
<tr>
<td>$\bar{\Omega}$</td>
<td>$0.5\pm0.15$</td>
<td>$0.6\pm0.15$</td>
<td>$-0.2\pm0.15$</td>
<td>$0.2\pm0.15$</td>
</tr>
<tr>
<td></td>
<td>$(0.55\pm0.15)$</td>
<td>$(0.5\pm0.15)$</td>
<td>$(0.0\pm0.15)$</td>
<td>$(0.05\pm0.15)$</td>
</tr>
<tr>
<td>$\Omega$</td>
<td>$0.8\pm0.2$</td>
<td>$0.3\pm0.2$</td>
<td>-</td>
<td>-</td>
</tr>
</tbody>
</table>

fit parameters which defines the error limits for the local relaxation volumes in Table 1. (The additional errors arising from the finite size of the supercell are much smaller). The local relaxations of the atoms around the defects are typically a few percent of the nearest-neighbour distance (Detailed information is given in Ref. 6.). With these defect formation parameters the chemical potentials and the concentrations of the various defects were determined by the generalized grandcanonical formalism according to Refs. [4,5], and the effective formation volumes were obtained from eq. (3). The errors for the local relaxation volumes thereby result in errors for the effective formation volumes which would be hard to figure out numerically. Instead, we estimate the error limits by applying the law of error propagation to eqs. (5,6) which would hold if FeAl was a pure triple-defect system or a pure antistructure-type system. For both cases we obtain very similar error limits, and therefore we use them in Table 1 also for FeAl which is in between these two limiting cases.

## Results and Discussion

The values of the local relaxation volumes $\Delta V_{i}$, the effective formation volumes $\bar{\Omega}_{i}$ and the fictitious formation volumes $\Omega_{i}=\Delta V_{i}+\bar{\Omega}_{0}$ are shown in Table 1 for the stoichiometric compound FeAl and for $Fe_{0.52}Al_{0.48}$, both at $T=1300$ K. The local relaxation volume of the Al vacancy is much larger than the one of the Fe vacancy due to the larger size of the Al atom. Accordingly, the local relaxation volume is negative (positive) for the Fe(Al) antistructure atom. If FeAl was a pure triple defect system, we would find according to eq. (5) for the stoichiometric compound $\bar{\Omega}_{V}^{Fe}=\bar{\Omega}_{Fe}^{Al}=(0.4\pm0.2)\bar{\Omega}_{0}$, if it was a pure antistructure-type system, eq. (5) would yield $\bar{\Omega}_{Fe}^{Al}=\bar{\Omega}_{Al}^{Fe}=(0.0\pm0.2)\bar{\Omega}_{0}$. Inspection of Table 1 reveals that according to the computer results the effective formation volume of the Fe vacancy in the stoichiometric compound is similar to that which would arise for a triple defect system, but the one of the Fe antistructure atom is similar to that which would arise for an antistructure-type system, indicating that FeAl is neither a pure triple-defect system nor a pure antistructure-type system [6]. It becomes also clear from Table 1 that the effective formation volumes depend sensitively on composition. Comparing the second and third lines of Table 1 reveals a big difference between the real effective formation volume of the Fe vacancy, $\bar{\Omega}_{V}^{Fe}$, and the fictitious value $\Omega_{V}^{Fe}$ which would arise if we just added the mean atomic volume $\bar{\Omega}_{0}$ to the local relaxation volume $\Delta V_{V}^{Fe}$ as in a monoatomic crystal. The effective formation volumes of the Fe and the Al monovacancy are much smaller than the mean atomic volume. Therefore, if the pressure dependence of the positron lifetime yielded an effective formation volume larger than $\bar{\Omega}_{0}$ not only apart from stoichiometry [2] (where our theory does not hold and where the situation might be rather different [5]) but also very close to stoichiometry, this would be indeed a hint to composite defects including more than one Fe vacancy (the concentration of Al vacancies is extremely small in near-stoichiometric FeAl, see Refs. 5-7). However, as discussed above, this would not necessarily mean that this composite defect contributes significantly to the diffusion or that more than one Fe vacancy of the composite defect serves directly as diffusion vehicle (for a discussion of possible diffusion mechanisms in FeAl see Ref. 5).

### References

1.  G. Sauthoff, "Intermetallics", VCH Verlag, 1995.
2.  J. Wolff, M. Franz, and Th. Hehenkamp, Microchimica Acta.
3.  A. Gude, K. Freitag, B. Sepiol, G. Vogl, and H. Mehrer, phys. stat. sol. (b) **197**, 299 (1996).
4.  J. Mayer and M. Fähnle, Acta Materialia, to be published.
5.  J. Mayer and M. Fähnle, Proceedings of the DIMAT96 conference, Nordkirchen, Germany, 1996, to be published.
6.  J. Mayer, C. Elsässer and M. Fähnle, phys. stat. sol. (b) **191**, 283 (1995).
7.  C.L. Fu, Y.Y. Ye, M.H. Yoo, and K.M. Ho, Phys. Rev. **B48**, 6712, (1993).