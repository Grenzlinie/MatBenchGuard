![](./images/811115051237769219_1.jpg)

Materials Science and Engineering A204 (1995) 90-95

![](./images/811115051237769219_2.jpg)

# Growth of elongated nanostructures

## D.G. Vlachos

Department of Chemical Engineering, University of Massachusetts, Amherst, MA 01003, USA

---

### Abstract

Growth of elongated nanostructures from the gas phase on a masked substrate is modeled using the continuous time Monte Carlo method with the solid-on-solid approximation. We have found that the masked substrate imposes anisotropy on the growth of elongated nanostructures. Thus growth occurs either by nucleation of a single cluster in the short direction and wave propagation in the long direction or by formation of multiple nuclei followed by propagation of waves along the long direction. The growth rate of nanostructures depends significantly on their size. Narrow nanostructures grow about two orders of magnitude slower and there is a size-dependent critical supersaturation for growth to occur. This behavior is explained in terms of the thermal stability of nanostructures.

**Keywords**: Growth; Elongated nanostructures; Thermal stability

---

## 1. Introduction

Nanophase materials are encountered in many applications, including supported catalysts, ceramics and semiconductors. There has been a continuous need for structures of smaller dimensions and it may not be long before structures of atomic dimensions are synthesized in a reproducible and systematic way. The use of zeolite cages, for example, has opened new horizons for synthesis of materials of small size in confined geometries. Structures of small dimensions have recently been synthesized including quantum dots and wires.

The problem of crystal growth and crystal morphology has been studied since the pioneer work of Burton et al. [1]. An understanding of crystal growth at the molecular level has been pursued mostly for simple cubic crystals using Monte Carlo simulations for adsorption and desorption of growth units (homoepitaxial systems) [2,3]. These studies were subsequently extended to incorporate surface diffusion and dislocations [4].

Structures of atomic demensions exhibit finite size effects and magic numbers may be found [5]. These magic number structures have distinctly different properties from structures close in size. Such properties may include thermodynamic properties [5], selectively and reactivity [6], etc. The properties of small structures may be different from these of bulk materials. It is expected that sufficiently large three-dimensional particles and epitaxial thin films will behave like bulk materials. Despite static simulations on clusters [7], the critical size where the transition of bulk-like properties occurs is still an open question.

Understanding nucleation and growth of nanophase materials is central for miniaturization of structures with desired properties. Formation on a substrate of elongated nanostructures which are almost one-dimensional is of importance to catalysis, quantum wires and interconnecting lines for electronic devices [8,9]. Deposition on patterned and masked substrates is also of considerable interest for selective deposition.

Here we examine the morphology and growth rates of elongated nanostructrues growing from an adjacent fluid by employing the continuous time Monte Carlo method. Emphasis is placed on the role of finite size in growth rates, surface morphology, nucleation and dynamics.

## 2. Model and Monte Carlo simulations

Growth of elongated nanostructures on a masked substrate is modeled. A schematic illustration of the model is shown in the inset of Fig. 1 (see Section 3). The sticking coefficient on the masked substrate is taken to be zero. Thus incorporation into the nanos-

---

0921-5093/95/$09.50 © 1995 — Elsevier Science S.A. All rights reserved
SSDI 0921-5093(95)09943-3

tructure occurs directly from the adjacent fluid phase. Adsorption and desorption are modeled and the resistance to transport in the adjacent fluid phase is considered to be small. For simplicity a simple cubic lattice is employed with first-nearest-neighbour interactions of strength $\varepsilon$. For the simulations reported here, $\varepsilon=0.23$ eV and the temperature is taken to be $T=1000 \mathrm{~K}(\varepsilon / k T=2.669$, where $k$ is the Boltzmann constant). The lattice size representing a growing nanostructure is $80 \times w$, where $w$ is the width of the nanostructure and is a parameter of the model. The effect of length has been examined in the simulations. We have found that this size of 80 atoms gives results for the growth rate and surface morphology which are, within the accuracy of the simulations, independent of the length.

According to the kinetic theory, the adsorption probability per unit time per site is
$$
p_{\mathrm{a}}=\frac{s_{0} P}{\eta_{0}(2 \pi m k T)^{1 / 2}}
$$
where $P$ is the gas phase pressure, $s_{0}$ is the sticking coefficient, which is assumed to be independent of the local environment of a surface site, $\eta_{0}$ is the density of sites and $m$ is the mass of an atom.

The desorption probability per unit time of an atom with $n$ first-nearest neighbors is
$$
p_{\mathrm{d}}(n)=v_{0} \exp \left(-\frac{n \varepsilon}{k T}\right)
$$
where $v_{0}$ is the pre-exponential factor. For an ideal gas in contact with a solid the difference in chemical potential between the two phases is
$$
\Delta \mu=k T \ln \left(\frac{P}{P_{\mathrm{c}}^{\varkappa}}\right)
$$
where $P_{\mathrm{c}}^{\varkappa}$ is the equilibrium crystal vapor pressure of an infinite surface. The relative supersaturation with respect to an infinite surface is here defined as
$$
\sigma_{\varkappa}=\frac{P}{P_{\mathrm{c}}^{\varkappa}}-1
$$

From Eqs. (1), (3) and (4), $p_{\mathrm{a}}$ becomes
$$
p_{\mathrm{a}}=p_{\mathrm{a}, \mathrm{e}} \exp \left(\frac{\Delta \mu}{k T}\right)=p_{\mathrm{a}, \mathrm{e}}\left(1+\sigma_{\varkappa}\right)
$$
where $p_{\mathrm{a}, \mathrm{e}}$ is the adsorption transition probability of a gas in equilibrium with the solid phase. Equilibrium occurs when the adsorption rate equals the average desorption rate. The two rates are equal at "kink" sites with exactly half the neighbors present [10], i.e. $p_{\mathrm{d}}(3)=p_{\mathrm{a}, \mathrm{e}}$.

![](./images/811115051237769219_3.jpg)

Fig. 1. Number of layers deposited vs. time for various nanostructure widths with $\sigma_{\alpha}=0.6$. The inset is a schematic illustration of an elongated nanostructure growing on an inert substrate. For narrow stripes, nucleation barriers exist and the growth oscillates between low and high values.

The continuous time Monte Carlo method [11] is employed which is an extension of the $n$-fold method proposed by Bortz et al. [12]. Every trial is successful and the time is updated by a continuous amount determined from the average lifetime of the surface configuration. A priori probabilities of various events are calculated before rather than after choosing an event. The efficiency of simulations increases by putting the atoms in classes of the same transition probability. For example, in the case of an adsorption event all sites are equivalent and belong to the same class. For desorption the activation energy depends on the local environment of an atom. The probability per unit time of choosing a particular desorption class is then $N_{\mathrm{d}}(n) p_{\mathrm{d}}(n)$, where $N_{\mathrm{d}}(n)$ is the number of atoms with $n$ first-nearest neighbors. The total probability per unit time is then
$$
p^{\mathrm{tot}}=p_{\mathrm{a}, \mathrm{e}} \sum_{\text {surface }}\left[\exp \left(\frac{\Delta \mu}{k T}\right)+\exp \left(\frac{(3-n) \varepsilon}{k T}\right)\right]
$$

After selecting a class, a site from this class is randomly chosen and the event is executed. The time is then incremented by [11]
$$
\Delta t=-\frac{\ln (\xi)}{p^{\mathrm{tot}}}
$$
where $\xi$ is a random number $(0<\xi<1)$.

The size of the nanostructure in one direction is sufficiently long so that periodic boundary conditions are used. The width in the other direction is short and free boundary conditions are employed. Since the sticking coefficient on the mask is taken to be zero, creeping of material from the nanostructure to the mask is not considered here. Runs with $10^{6}$ up to $2 \times 10^{8}$ successful Monte Carlo trials have been performed. Longer runs were done for slow-growing stripes and shorter runs for fast-growing stripes.

## 3. Results and discussion

Fig. 1 shows the number of layers deposited vs. time for various nanostructure widths at a relative supersaturation $\sigma_{\infty}=0.6$. The time is made dimensionless by dividing $t$ by the characteristic time for adsorption of an atom, $\tau_{\mathrm{a}}=1 / p_{\mathrm{a}, \mathrm{e}}$. The width $w$ is made dimensionless by the lattice constant $a_{0}$, and its numerical value indicates the number of rows of atoms in the stripe.

The first noticeable feature is that the average slope of the curves decreases as the width of a nanostructure decreases. Thus the growth rate of wide stripes is much higher than that of narrow nanostructures. For the case of $w / a_{0}=160$ the height of the nanostructures changes smoothly with time. In contrast, step-like curves are obtained for $w / a_{0}=15$ and 8. This behavior is reminiscent of nucleation barriers.

At relatively low supersaturations, growth on flat surfaces proceeds slowly by two-dimensional nucleation. There is some time elapsed before a critical size nucleus is formed on a surface. This is indicated by a horizontal line with small fluctuations in Fig. 1. Two-dimensional growth of a critical nucleus then occurs rapidly to complete one monolayer. This is indicated by an almost vertical line connecting horizontal lines in Fig. 1. During the time needed for cluster formation the growth rate is very low (a small slope in the height-time curve). In contrast, during two-dimensional growth of a supercritical cluster the growth rate is high (a large slope in the height-time curve). Thus the growth rate oscillates between low and high values for sufficiently narrow nanostructures but is almost constant (a constant slope in the height-time curve) for wide nanostructures.

Our simulations indicate that for a certain pressure (supersaturation) and temperature, nucleation times may be very short on large surfaces but very long on small size structures, which creates the difference in growth rates among structures of various widths. In contrast, when the supersaturation is high, the probability of formation of a critical nucleus is high. Under these conditions, kink sites are available at the periphery of growing clusters and growth proceeds rapidly, resulting in smooth height-time curves.

Fig. 2 shows the growth rate vs. the width of nanostructures for $\sigma_{\infty}=0.6$. The points are obtained from Monte Carlo simulations and the full curve connects the points. The growth rate is an average of at least 10 independent runs generated from various sequences of random numbers. Larger uncertainties occur for narrow nanostructures, because the number of layers deposited during a simulation is not large and times for nucleation of a new layer are long. Longer and more runs are then required for narrow stripes to obtain good statistics.

It is found that narrow nanostructures exhibit a considerably low growth rate as compared with wide nanostructures. The growth rate increases very sharply with nanostructure width and at sufficiently large widths it increases slightly with $w$ approaching an asymptote. The broken line shows the growth rate of the (100) plane obtained from an $80 \times 80$ lattice using periodic boundary conditions in both directions. This value is a theoretical upper bound for the growth rate of elongated nanostructures. The asymptote is approached slowly, because even for wide stripes there are always edge effects. Atoms at edges have fewer bonds as compared with an infinite surface where atoms at edges have nearest neighbors through the use of periodic boundary conditions. As an example of a material with a lattice constant of $3 \AA$ and $w / a_{0}=150$, the width of the nanostructure is $450 \AA$. Fig. 2 indicates that the growth rate of stripes of this size is overestimated by more than $10 \%$ when periodic boundary conditions are employed in both directions as compared with free boundary conditions in the short dimension.

![](./images/811115051237769219_4.jpg)

Fig. 2. Time average growth rate vs. width of nanostructures for $\sigma_{\infty}=0.6$. The broken line shows the growth rate of the (100) surface. The growth rate decreases very rapidly with decreasing stripe width. Periodic boundary conditions overestimate the growth rate of relatively small structures.

The growth rate of narrow nanostructures can be lower than that of large films by as much as two orders of magnitude. In fact, for a certain supersaturation there may be a critical width below which growth of nanostructures is impossible. Instead, etching of more narrow nanostructures occurs. For the conditions shown in Fig. 2, $w / a_{0}=6$ is the minimum size for which growth occurs. This is at first surprising, because for a positive supersaturation one would expect growth of stripes of all sizes but not etching.

The supersaturation is the driving force for growth; conversely, undersaturation is the driving force for etching. At equilibrium of an infinite crystal with the gas phase the supersaturation is zero ($\sigma_{\infty}=0$) and no

growth occurs. For gas phase pressure above the equi- librium pressure, $P > P_{e}^{\varkappa}(\sigma_{\varkappa}>0)$, growth occurs and the growth rate increases with $\sigma_{\varkappa}$. Based on a disloca- tion model of crystal growth, the growth rate exhibits a linear and a quadratic dependence on the driving force for high and low supersaturations respectively [1]. On the other hand, for gas phase pressure below the equi- librium pressure, $P < P_{e}^{\varkappa}(\sigma_{\varkappa}<0)$, etching of crystals occurs.

When the critical nucleus size is sufficiently large, its probability of formation is very low. Nucleation then controls the growth rate, which is low. The probabilities of formation and disappearance of a critical nucleus are equal. From a thermodynamic point of view, clusters of different shape may have a different free enegy. Thus the critical nucleus size may depend also on its shape. In particular, the contribution of line tension to the free energy plays a central role in affecting critical nucleus size. The anisotropy of the substrate imposes an an- isotropy in the critical nucleus, which must be elon- gated. Such an elongated nucleus has an increased line free energy as compared with a square nucleus and is thermodynamically less stable. Consequently, nucle- ation of such elongated nanoclusters is more difficult, requires longer times and results in lower growth rates as the width decreases. Sufficiently narrow nanostruc- tures are unstable and disappear. We have found that the critical value of supersaturation below which growth is impossible decreases as $w$ decreases.

The surface of stripes examined here is flat without dislocations and steps from misorientation for which the model of Burton et al. holds. Steps appear only at the periphery of growing clusters. For narrow nanos- tructures, clusters first grow along the short dimension and then along the long dimension to produce a critical nucleus size as shown in Fig. 3. That is, clusters perco- late fast in the short dimension but grow slowly along the long dimension until a critical size nucleus is formed. Under these circumstances, clusters possess steps for atom incorporation only along the short di- mension. Thus the anisotropic growth results in propa- gation of waves along the long dimension. When the stripe is short, we found that only one nucleus forms and two one-dimensional waves propagate in opposite directions to produce one monolayer. When the stripe is long, such as 80 atoms, multiple nuclei form in a layer and waves propagate and annihilate as they col- lide.

![](./images/811115051237769219_5.jpg)

Fig. 3. Snapshots of the top four layers during growth of a $40 \times 8$ stripe. The top snapshot shows a nucleus which has formed in the short dimension and subsequently grown in the long dimension. The bottom snapshot shows the surface morphology after a layer has just been completed. Defects at the edges of the nanostructure are ob- served.

![](./images/811115051237769219_6.jpg)

Fig. 4. Square root of time average growth rate vs. supersaturation for various stripe widths. The growth rate depends in a quadratic way on the supersaturation. There may be a critical supersaturation for every stripe width below which etching occurs.

Fig. 4 shows the square root of the growth rate of a nanostructure vs. the supersaturation for various widths of nanostructures. The points correspond to Monte Carlo simulations and the curves are interpola- tions of the points. An almost straight line is obtained, indicating that the growth rate has an almost quadratic dependence on the driving force defined with respect to an infinite surface. The distance between curves corre- sponding to different widths is slightly reduced with increasing supersaturation. This indicates that there is only one dominant mechanism for all supersaturations which creates the difference in growth rates between various widths. It is expected that in the limit of fast growth the dependence of growth rate on size will be weak. For example, the growth rate of $w / a_{0}=15$ is higher than that of $w / a_{0}=8$ by about $160 \%, 1.5 \%$ and $1.0 \%$ for $\sigma_{\varkappa}=0.6,20$ and 50 respectively.

Atoms at edges of nanostructures are energetically unfavorable and thus the vapor pressure of narrow nanostructures is enhanced compared with an infinite surface. This reduces the growth rate, because desorp- tion rates near the edges are locally high. Desorption of

atoms at the edges creates energetically unfavorable atoms next to the edges. This situation propagates subsequently toward the axis of symmetry of a nanostructure. When a nanostructure is very narrow, desorption occurs quickly compared with the time required for nucleation of an elongated critical nucleus. Thus clusters of small length are rapidly destroyed owing to edge effects and the probability of formation of a critical nucleus is low.

To examine the interplay of thermal stability and nucleation in the observed growth rates, the critical supersaturation needed for growth has been calculated vs. the nanostructure width. The critical supersaturation determines the pressure at which the nanostructure is in equilibrium with the gas phase. Growth and etching are very slow near equilibrium, i.e. as the supersaturation approaches the critical value. In addition, during growth of narrow nanostructures near the critical supersaturation, large fluctuations are observed. Typically a few layers are deposited followed by etching and subsequent growth. To determine the critical supersaturation, the growth and etching rates have been determined sufficiently close to the critical value. An interpolation has then been used to find the critical supersaturation for which the growth rate is zero. The error in calculating the critical supersaturation is bounded by the difference between the data obtained on either side of zero rate. The inset in Fig. 5 shows an example of this calculation. The points are obtained from Monte Carlo simulations and the full curves are interpolations of the points. The rate $r_{\mathrm{g}}$ of growth (positive sign) and etching (negative sign) and the square root of $r_{\mathrm{g}}$ are plotted vs. the supersaturation for $w / a_{0}=8$. The intersection of the two curves with the horizontal axis at $r_{\mathrm{g}}=0$ provides the critical supersaturation $\sigma_{\mathrm{c}}=P_{\mathrm{c}} / P_{\mathrm{c}}^{\infty}-1$ separating the growth from the etching conditions for a certain nanostructure.

![](./images/811115051237769219_7.jpg)

Fig. 5. Critical supersaturation vs. inverse of stripe width. The vapor pressure of a nanostructure is inversely proportional to the width of the nanostructure. The inset shows the growth rate and the square of the growth rate vs. supersaturation for $w / a_{0}=8$ for an estimation of the equilibrium vapor pressure.

![](./images/811115051237769219_8.jpg)

Fig. 6. Square root of time average growth rate vs. acutal supersaturation for various stripe widths. The dominant mechanism for the low growth rates of narrow nanostructures is due to the reduced thermal stability manifested by their low vapor pressure.

Fig. 5 shows the critical supersaturation (equilibrium pressure) vs. the inverse of the width of the nanostructure. The points are obtained from an analysis similar to that shown in the inset and the line is a least-squares fit to the points. A linear dependence is found with a good correlation coefficient. This indicates that the vapor pressure is inversely proportional to the width of the nanostructure for the conditions examined.

For finite size nanostructures the vapor pressure is higher than that of an infinite surface. As a result the actual driving force for growth of nanostructures is lower than that of an infinite (100) surface. The growth rate is then replotted vs. the actual driving force made dimensionless with the equilibrium pressure of a reference size (in this case of an infinite (100) surface) for various widths in Fig. 6. The points correspond to Monte Carlo simulations and the curve is an interpolation of the points obtained for $w / a_{0}=15$. When the growth rate is plotted vs. the actual supersaturation, most of the finite size effects disappear. Within the accuracy of the simulations, points collapse on a single curve, especially at high supersaturations. This indicates that to a large extent the strong dependence of growth rate on size is due to the variation in vapor pressure with finite width. However, some small deviations are still observed at small supersaturations among different widths. Since simulations are more inaccurate at low supersaturations because of slow nucleation, our conclusions cannot be more definite. However, our simulations indicate that the strong dependence of growth rate

on finite size is primarily due to the finite size depen- dence of the vapor pressure.

Here we examined adsorption and desorption with- out migration. Surface diffusion results in establishment of local equilibrium at a solid-fluid interface. Adatoms migrate on a surface to reach energetically favorable positions such as steps and kinks where they get incor- porated. The activation energy for desorption and sur- face diffusion from such positions is considerably high and as a result the probability of adatoms escaping the nanostructure is low. It is thus expected that surface diffusion will reduce the desorption rate and increase the growth rate as also happens with large cyrstals [4].

## 4. Conclusions

We have examined the growth of elongated nanos- tructures from a fluid phase using the continuous time Monte Carlo algorithm and the solid-on-solid approxi- mation. We have found that the growth rate is consid- erably low for narrow nanostructures and tends to an asymptote for a few hundred angstroms under the conditions studied. Low growth rates are attributed to the reduced thermal stability of narrow nanostructures manifested by low vapor pressures. Nucleation is ob- served for sufficiently narrow structures under condi- tions where fast growth occurs for large surfaces. This results in alternation of the growth rate between high and low values (oscillations). The time average growth rate changes almost in a quadratic way with the relative supersaturation. The anisotropy of the initial surface imposes an anisotropy in the growth of elongated struc- tures. Clusters first nucleate along the short dimension and then propagate along the long dimension. For long nanostructures, multiple nuclei are formed and merge, whereas for short nanostructures only one nucleus is formed and propagates to create one monolayer. Our simulations here indicate that growth of small nanos- tructures including stripes and three-dimensional clus- ters can be profoundly slower than growth of thin films and large particles respectively.

## Acknowledgements

This work was supported in part by the Engineering Computing Services of the University of Massachusetts.

## References

[1] W.K. Burton, N. Cabrera and F.C. Frank, Philos. Trans. R. Soc. Lond. A, 243 (1951) 299.

[2] J.P. van der Eerden and P. Bennema, Prog. Cryst. Growth Charact., 1 (1978) 219.

[3] G.H. Gilmer and K.A. Jackson, in E. Kaldis and H.J. Scheel (eds.), Crystal Growth and Materials, North-Holland, Amster- dam, 1977, p. 79.

[4] G.H. Gilmer and P. Bennema, J. Appl. Phys., 43(4) (1972) 1347.

[5] D.G. Vlachos, L.D. Schmidt and R. Aris, J. Chem. Phys., 96 (1992) 6880.

[6] E.K. Parks, B.H. Weiller, P.S. Bechthold, W.F. Hoffman, G.C. Nieman, L.G. Pobo and S.J. Riley, J. Chem. Phys., 88 (1988) 1622.

[7] B. Raoult, J. Farges, M.F. De Feraudy and G. Torchet, Philos. Mag. B, 60 (1989) 881.

[8] I. Zuburtikudis and H. Saltsburg, Science, 258 (1992) 1337.

[9] J. Tersoff and R.M. Tromp, Phys. Rev. Lett., 70 (1993) 2782.

[10] G.H. Gilmer, Science, 208 (1980) 355.

[11] D.G. Vlachos, L.D. Schmidt and R. Aris, Phys. Rev. B, 47 (1993) 4896.

[12] A.B. Bortz, M.H. Kalos and J.L. Lebowitz, J. Comput. Phys., 17 (1975) 10.