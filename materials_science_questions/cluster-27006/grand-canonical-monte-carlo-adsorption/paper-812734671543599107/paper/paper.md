![](./images/812734671543599107_1.jpg)

This article was downloaded by: [Florida International University]
On: 26 July 2013, At: 11:00
Publisher: Taylor & Francis
Informa Ltd Registered in England and Wales Registered Number: 1072954 Registered office: Mortimer House,
37-41 Mortimer Street, London W1T 3JH, UK

Molecular Physics: An International Journal at the
Interface Between Chemistry and Physics
Publication details, including instructions for authors and subscription information:
http://www.tandfonline.com/loi/tmph20

Simulation of hydrogen adsorption in carbon nanotubes

ROGER F. CRACKNELL $^{a}$

$^{a}$ Shell Global Solutions UK, Cheshire Innovation Park, PO Box 1, Chester, CH1 3SH, UK
Published online: 01 Dec 2009.

To cite this article: ROGER F. CRACKNELL (2002) Simulation of hydrogen adsorption in carbon nanotubes, Molecular Physics: An International Journal at the Interface Between Chemistry and Physics, 100:13, 2079-2086, DOI:
10.1080/00268970210130236

To link to this article: http://dx.doi.org/10.1080/00268970210130236

PLEASE SCROLL DOWN FOR ARTICLE

Taylor & Francis makes every effort to ensure the accuracy of all the information (the "Content") contained in the publications on our platform. However, Taylor & Francis, our agents, and our licensors make no representations or warranties whatsoever as to the accuracy, completeness, or suitability for any purpose of the Content. Any opinions and views expressed in this publication are the opinions and views of the authors, and are not the views of or endorsed by Taylor & Francis. The accuracy of the Content should not be relied upon and should be independently verified with primary sources of information. Taylor and Francis shall not be liable for any losses, actions, claims, proceedings, demands, costs, expenses, damages, and other liabilities whatsoever or howsoever caused arising directly or indirectly in connection with, in relation to or arising out of the use of the Content.

This article may be used for research, teaching, and private study purposes. Any substantial or systematic reproduction, redistribution, reselling, loan, sub-licensing, systematic supply, or distribution in any form to anyone is expressly forbidden. Terms & Conditions of access and use can be found at http://www.tandfonline.com/page/terms-and-conditions

MOLECULAR PHYSICS, 2002, VOL. 100, No. 13, 2079-2086
![](./images/812734671543599107_2.jpg)

# Simulation of hydrogen adsorption in carbon nanotubes

## ROGER F. CRACKNELL*
Shell Global Solutions UK, Cheshire Innovation Park, PO Box 1,
Chester CH1 3SH, UK

(Received 21 September 2001; revised version accepted 31 January 2002)

Computer simulations are reported of hydrogen adsorption in multi-walled carbon nanotubes (MWNTs) and single-walled carbon nanotubes (SWNTs). The gas-solid interaction was modelled both as pure dispersion forces and also with a hypothetical model for chemisorption introduced in a previous paper (CRACKNELL, R., F., 2001, *Phys. Chem. chem. Phys.*, 3, 2091). A two-centre model for hydrogen was employed and the grand canonical Monte Carlo methodology was used throughout. Uptake of hydrogen in the internal space of a carbon nanotube is predicted to be lower than in the optimal graphitic nanofibre with slitlike pores (provided the gas-solid potential is consistent). Part of the difference arises from the assumption of pore surface area used in converting the raw simulation data to gravimetric adsorption; however, the majority of the differences can be attributed to the curvature of the pore. This reduces the uptake of hydrogen (on a gravimetric basis) in spite of deepening the potential minimum inside the pore associated with dispersion forces. It is concluded that for the uptake of hydrogen in SWNTs of 5-10% reported by Heben (DILLON, A. C., JONES, K. M., BEKKEDAHL, T. A., KIANG, C. H., BETHUNE, D. S., AND HEBEN, M. J., 1997, *Nature*, 386, 377), gas-solid forces other than dispersion forces are required and most of the adsorption must occur in the interstices between SWNTs.

### 1. Introduction
The ability to store hydrogen onboard vehicles is a key technological issue for the development of fuel cell vehicles powered directly by hydrogen. The US Department of Energy has set target system gravimetric and volumetric energy densities at $6.5\,\text{wt}\%$ and $62\,\text{kg}\,\text{H}_2$ per $\text{m}^3$, respectively [1]. There are a number of potential ways in which this could be achieved, including compressed hydrogen at pressures of up to 700 bar (10 000 psi), liquid hydrogen, and metal hydride storage.

A further possible way is to adsorb hydrogen in advanced carbonaceous materials. There are effectively 3 classes of such materials.
- Graphitic nanofibres (GNFs). Graphitic platelets are oriented perpendicular, parallel or inclined to a fibre axis. The inclined (or herringbone) geometry has been reported as giving the highest uptake. The pore space can be viewed as slitlike.
- Single-wall carbon nanotubes (SWNTs). These are rolled up graphene sheets where each end is initially capped with a fullerene dome, which needs to be removed before the SWNT can be used as an adsorbent.
- Multi-walled carbon nanotubes (MWNTs). These are similar to SWNTs, but the inner tube is surrounded by concentric rings of other rolled up graphene sheets.

There was considerable interest when Rodriguez, Baker and coworkers [2, 3] reported uptake of hydrogen in graphitic nanofibres (GNFs) of up to $65\%$ by weight at ambient temperatures. However, other workers, despite considerable efforts, have not reproduced this level of uptake. *Chen et al.* [4] reported that Li or K doped MWNTs could reproducibly adsorb and desorb up to $20\,\text{wt}\%$ of hydrogen at ambient pressure and modest temperatures. However, more recent evidence seems to disprove this claim and suggests that it was $\text{H}_2\text{O}$ rather than hydrogen that was the cycling mass [5, 6].

Another claim is that of Heben and coworkers [7, 8] who inferred an uptake of $5$-$10\%$ in a SWNT at ambient temperatures, although this has yet to be converted into a practical system, since the material itself contained only $0.1$-$0.2\,\text{wt}\%$ of SWNTs. Interestingly also, they claim to have measured a heat of adsorption of $19.6\,\text{kJ}\,\text{mol}^{-1}$. This is considerably in excess of what would normally be expected for dispersion forces in carbonaceous materials. *Liu et al.* [9] have measured uptakes of $4.2\,\text{wt}\%$ on SWNTs with a mean diameter of up to $1.85\,\text{nm}$. A useful recent review of the subject of

*e-mail: roger.f.cracknell@opc.shell.com

*Molecular Physics* ISSN 0026-8976 print/ISSN 1362-3028 online © 2002 Taylor & Francis Ltd
http://www.tandf.co.uk/journals
DOI: 10.1080/00268970210130236

hydrogen adsorption on carbonaceous adsorbents has been published recently by Dillon and Heben [10].

In parallel with the effort to synthesize novel materials, there has been a considerable effort in attempting to model the adsorption of hydrogen in carbonaceous materials [11-18]. The modelling work of Wang and Johnson [11, 12] used Path Integral Monte Carlo simulations, rather than classical Monte Carlo aproaches, in order to properly model the non-classical rotations of hydrogen. Nevertheless, at ambient temperatures the results obtained by Wang and Johnson were consistent with comparable simulations adopting a classical simulation technique. A consensus seems to have emerged that if the interactions between hydrogen and graphitic surfaces are modelled on the basis of dispersion forces only, then an upper bound on the gravimetric storage density of hydrogen in GNFs is around 1.5%. This figure is lower still, if converted to an adsorption excess, and is considerably less than the uptake suggested by Baker, Rodriguez and co-workers [2, 3]. Adsorption within the pore of an MWNT or SWNT gives rise to an uptake of much less than a per cent [15, 18] at ambient temperatures when the interaction is modelled using dispersion forces, although adsorption in the interstices between SWNTs may increase this figure.

In our previous work [17] we used grand canonical Monte Carlo molecular simulation to model hydrogen adsorption in GNFs where the pore were treated as slits bounded by layers of stacked planar graphitic sheets. Hydrogen was modelled as two Lennard-Jones sites and the interaction between a site and a graphitic surface was modelled on the basis of dispersion forces, using the standard 10-4-3 potential [19]. In agreement with other modelling studies, this gave a maximum adsorption at 120 bar of about 1.5 wt%.

Although there is no theoretical basis to suggest a much stronger interaction between molecular hydrogen and a planar graphitic surface, we also performed simulations using two hypothetical potentials (figure 1) with 'chemisorption' minima as well as dispersion minima in order to see how this would affect the uptake. The 'chemisorption 1' potential derives from DFT calculations of the interaction between atomic hydrogen and graphite [20]. Since we are in fact considering the interaction between an atom on a hydrogen molecule and the surface, the model sets an exaggerated upper bound on the interaction strength. The 'chemisorption 2' potential is scaled down by a factor of 4 so as to give a dispersion minimum that coincides with that for the 10-4-3 potential. It could be construed as a more plausible, albeit hypothetical, model for chemisorption. The uptake using chemisorption 1 was not found to be reversible (in the sense that the majority of the hydrogen remains adsorbed at pressures below 1 atm), whereas chemisorption 2 gave rise to a reversible storage of around 6.5 wt% in model GNFs.

![](./images/812734671543599107_3.jpg)

Figure 1. Comparison of 10-4-3 potential for interaction of a single hydrogen site with a graphitic surface and two hypothetical models for chemisorption (z = distance from wall).

The objective of this work has been to extend the aproach developed in [17] to carbon nanotubes, both MWNTs and SWNTs, and in particular to test the plausibility of the claims of Heben and co-workers [7, 8].

## 2. Model for carbon nanotubes

A carbon nanotube is based on a 2-dimensional graphene sheet. The unit cell for the nanotube is such that it forms a periodic boundary at its edge. The usual notation for describing the structure of the nanotube unit cell is the so-called Hamada vector $(n, m)$ whereby $n$ and $m$ are integer multipliers of the 2-dimensional hexagonal lattice [21]. Various structures for nanotubes are possible, the more common being zigzag nanotubes when either $m$ or $n$ is zero and armchair nanotubes where $n = m$. Different types of nanotube can have quite different electronic properties. About one third of small diameter nanotubes are metallic whereas the remainder are semiconducting; this is due to the interactions of the wavefunctions around the circumference of the nanotube.

The method used for modelling dispersion forces in this work is based on integrating the Lennard-Jones interaction between the adsorbent and adsorbate over the surface of the pore walls and ignoring the detailed surface structure. A more complete account is given in the appendix. The Lennard-Jones parameters used in this work are the same as in [17], and are summarised in table 1. As in [17] hydrogen is modelled as a dumbbell molecule with two Lennard-Jones sites.

The cross parameters for the Lennard-Jones interaction between a hydrogen site and the graphitic surface

Table 1. Summary of Lennard-Jones and other related structural parameters.

| | | |
| --- | --- | --- |
| H---H distance | | 0.074 nm |
| Hydrogen hard sphere diameter | $\sigma_{\text{HH}}$ | 0.259 nm |
| Hydrogen well depth | $\varepsilon_{\text{HH}}$ | 12.5 K |
| Carbon hard sphere diameter | $\sigma_{\text{CC}}$ | 0.340 nm |
| Carbon well depth | $\varepsilon_{\text{CC}}$ | 28.0 K |
| Number of carbons per unit volume in graphitic materials | $\rho$ | $114\,\text{nm}^{-3}$ |
| Separation of sheets in graphite/<br>MWNTs | $\Delta$ | 0.335 nm |

were calculated using the standard Lorentz-Berthelot rules, viz.

$$
\sigma_{\mathrm{HC}}=\frac{1}{2}\left[\sigma_{\mathrm{CC}}+\sigma_{\mathrm{HH}}\right], \quad \varepsilon_{\mathrm{HC}}=\left(\varepsilon_{\mathrm{CC}} \varepsilon_{\mathrm{HH}}\right)^{1 / 2}.
$$

As a way of modelling hypothetical chemisorption within nanotubes, the chemisorption minimum from the chemisorption 2 model was used as shown in figure 1 for a planar surface. This was combined with the dispersion minimum calculated from the Lennard- Jones interactions between a hydrogen site and the wall. For each possible nanotube wall-hydrogen distance $z$, this combined potential was calculated by comparing the energy of the chemisorption 2 potential in a planar system as shown in figure 1, and the potential calculated from the integration of the Lennard-Jones potential over the surface of the pore wall (see appendix). The minimum of the two values was then taken. We note that several authors [22, 23] have alluded to the poss- ibility of a type of chemisorption in nanotubes. The curvature of the graphene sheet is postulated to increase the localization of electron density. This changes the hybridization of the carbon from purely $\mathrm{sp}^{2}$ to some- thing approaching $\mathrm{sp}^{3}$.

In molecular dynamics simulations using totally $ab$ initio potentials of hydrogen adsorbed in a (9,9) nano- tube (with diameter 1.2 nm), Cheng et al. [23] found that the H---H bond distance could be considerably lengthened and the hydrogen atoms act as acceptors of electron density from the re-hybridized carbon. By comparison with the work of Cheng et al., the potential models used in this paper are relatively simple (the walls are treated as rigid and without surface structure; the hydrogen is rigid). Nevertheless the simplicity has the advantage of numerical tractability in terms being able to simulate and compare adsorption isotherms for vari- ous potential models. In this work, we have considered explicitly only the adsorption inside the pore, and not the adsorption in the interstitial space between nano- tubes.

![](./images/812734671543599107_4.jpg)

Figure 2. Comparison of potential functions for a pore of width 1.2 nm.

A comparison of potential functions for a pore of width 1.2 nm is shown in figure 2 (width refers to the distance between carbon centres in the context of this paper). As discussed in the appendix, the curvature of the surface makes the dispersion minima stronger for carbon nanotubes than for slitlike pores. The isoteric heat of adsorption at zero loading was calculated for each potential model by Monte Carlo integration (over 50 million random positions and orientations) and the results are presented in table 2. We note that the value of $26\,\text{kJ}\,\text{mol}^{-1}$ for the SWNT with the chemisorption 2 potential is comparable both with the range of heats of adsorption predicted by Cheng et al. at 300 K [23] $(31\,\text{kJ}\,\text{mol}^{-1})$ and measured by Heben et al. $(19.6\,\text{kJ}\,\text{mol}^{-1})$ for pores of this width [7].

Table 2. Comparison of calculated isosteric heat of adsorption at 298 K (at zero loading) for various pore models for a pore width of 1.2 nm.

| Pore model | Potential | $q_{\text{ST}}/\text{kJ}\,\text{mol}^{-1}$ |
| --- | --- | --- |
| Multi-walled slit pore (nanofibre or activated carbon) | Dispersion (10-4-3) | 3.1 |
| SWNT | Dispersion (see appendix) | 7.1 |
| MWNT | Dispersion (see appendix) | 7.9 |
| SWNT | Dispersion + chemisorption 2 | 26.0 |

## 3. Monte Carlo molecular simulations

### 3.1. Methodology

In the grand canonical Monte Carlo method, the chemical potential (or gas fugacity), volume and temperature of the system are fixed, and the simulation calculates the number of particles in the system and the configurational energy corresponding to a particular choice of $\mu$, $V$ and $T$. The method is discussed in detail in a number of books [24, 25]. The interaction between hydrogen sites was cut off at 2 nm and no long range correction was applied. Hydrogen was modelled as a dumbbell with two Lennard-Jones sites. The parameters are given in table 1. The gas-solid potential was discussed in the preceding section. Typically, the simulations were run for 5 million configurations and used up to 500 particles. The rate of acceptance for particle creations and deletions was in the range 5-15%. Since the objective of this work was to evaluate systems for ambient temperature hydrogen storage, the simulation temperature was 298 K in every case.

### 3.2. Comparison of simulation data with experimental data

The raw simulation results yield the number of hydrogen molecules per unit length of nanotube. To be compared directly with adsorption experiments, this can be converted to an adsorption excess by determining the density of hydrogen molecules that would be present in the pore space without the effects of adsorption [26]. The maximum theoretical surface area of a graphitic material is $2680 \mathrm{m}^{2} \mathrm{g}^{-1}$. This assumes adsorption on both sides of a graphite sheet. However, the maximum theoretical surface area of the inside of a nanotube is only half this value, viz. $1340 \mathrm{m}^{2} \mathrm{g}^{-1}$. The simulation data for adsorption inside a nanotube was converted to a gravimetric value by this assumption. The simulation results therefore represent an upper bound on the gravimetric hydrogen adsorption possible inside the nanotube; however, they do not account for interstitial adsorption in nanotubes.

![](./images/812734671543599107_5.jpg)

Figure 3. Comparison of simulated adsorption isotherms for hydrogen in carbonaceous pores of width 1.2 nm at 298 K. The gas-solid potential is modelled using dispersion forces. The SWNT and MWNT adsorption refers only to the internal pore space and ignores any interstitial adsorption.

![](./images/812734671543599107_6.jpg)

Figure 4. Comparison of simulated adsorption isotherms for hydrogen in carbonaceous pores of width 1.2 nm at 298 K. The gas-solid potential is modelled using the chemisorption 2 potential. The SWNT and MWNT adsorption refers only to the internal pore space and ignores any interstitial adsorption.

## 4. Results

Figure 3 shows a comparison of the total (i.e. not excess) amount of hydrogen adsorbed inside MWNTs and SWNTs of diameter 1.2 nm where the gas-solid potential is modelled using dispersion forces only. This is equivalent to a (9,9) nanotube. The uptake barely exceeds 0.4 wt%. This is compared with the simulated results of hydrogen in a slit pore of width 1.2 nm (a model graphitic nanofibre) taken from [17], where the total (i.e., not excess) amount adsorbed reached 1.5 wt%. It should be noted that the conversion to gravimetric adsorption was on the basis of $2680 \mathrm{m}^{2} \mathrm{g}^{-1}$ for the slit pore and $1340 \mathrm{m}^{2} \mathrm{g}^{-1}$ for the inside of the nanotube (which strictly speaking is correct only for a single-walled nanotube). The results agree quite well with the simulation data of Rzepa and Lamp [15], who presented their simulation results on a gravimetric basis by assuming a specific surface area of $2600 \mathrm{m}^{2} \mathrm{g}^{-1}$ for all carbonaceous systems.

Figure 4 shows simulation results for hydrogen adsorbed inside an SWNT of diameter 1.2 nm using the chemisorption 2 potential. The uptake is expressed as the total amount of hydrogen. This is compared with results for a slit pore of width 1.2 nm taken from [17]

also using the chemisorption 2 potential. Whereas about 9-10% could be stored in an optimal graphitic nanofibre using this hypothetical potential function, a much smaller amount can be stored inside an optimal SWNT using this potential function. Figures 3 and 4 show that the ratio between the amounts adsorbed in the nanotube and the slit pore of comparable width are similar, regardless of the potential function. This occurs in spite of the fact that, as shown in figure 2, the disper- sion minimum is deeper in a nanotube than a slitlike pore of comparable width. This is due in part to the assumption of specific surface area used in converting the raw simulation data to gravimetric adsorption: $2680 m^{2} g^{-1}$ for the slit pore and $1340 m^{2} g^{-1}$ for the inside of the nanotube. However, there is an additional factor at play. The circumference of the first adsorbed layer in the pore is much less than the circumference of the ring of carbon centres defining the pore (by a factor of two in the case of SWNTs and MWNTs modelled purely by dispersion forces). In other words, the curva- ture of the tube means that the effective surface area of the inside of the pore is reduced. For a slitlike pore, this effect would not apply, and for the exterior surfaces of a carbon nanotube the convex curvature would cause the opposite effect.

Figure 5 shows additional results for adsorption on the inside of SWNTs of differing width using the chemi- sorption 2 potential. The results are plotted as total amount adsorbed and excess amount adsorbed on a gravimetric basis, asssuming an internal pore surface area of $1340 m^{2} g^{-1}$. Also plotted are the results for total amount adsorbed per unit internal volume of the nanotube (the volume here is the area bounded by the curved plane of carbon centres on the pore walls). For a given pressure, the adsorption increases slightly with pore diameter on both a gravimetric and volumetric basis. This is in contrast with results for a slot pore in [17] whereby once the pore was sufficiently large to have two adsorbed layers, the adsorption on a (excess) gravi- metric basis was almost constant with varying pore dia- meter, and the adsorption on a volumetric basis decreased with increasing pore diameter. The reasons for this are as discussed above: the concave curvature of the pore wall reduces the effective surface area of the pole per gram of carbon. As the pore gets wider, the ratio of the circumference of the first adsorbed layer to the circumference of the pore (defined by the ring of carbon centres) tends towards unity.

![](./images/812734671543599107_7.jpg)

Figure 5. Simulated adsorption isotherms for hydrogen in SWNTs of differing diameters at 298 K. The gas-solid potential is modelled using the chemisorption 2 potential. The SWNT and MWNT adsorption refers only to the internal pore space and ignores any interstitial adsorption.

## 5. Discussion

By assuming a model for the adsorption potential based on dispersion forces, the maximum amount of hydrogen that can be adsorbed inside the pore of a MWNT or SWNT is around $0.4 wt \%$ in pores of diameter 1.2 nm. By assuming a model based on ahypothetical chemisorption effect, an uptake of $3.2 wt \%$  is measured in pores of diameter 1.2 nm. Although the potential is hypothetical, the heat of adsorption is of the same order as the calorimetric measurements of Heben

and co-workers [7, 8] and other recent theoretical studies [23]. This is somewhat less than the 5–10% uptake claimed by Heben in pores of similar diameter. It appears to be the case that if the Heben data are reliable, a significant amount of the adsorption must occur in the interstitial spaces between the nanotubes.

As discussed in the preceding section, for the exterior surface of a carbon nanotube, the convex curvature is likely to mean that the effective surface area of the first adsorbed layer is greater than the area defined by the ring of carbon centres on the pore wall. If it may be assumed that there is a degree of chemisorption of hydrogen molecules due to a partial rehybridization of carbon atoms in the lattice, then the adsorption field on the convex and concave surfaces of a nanotube will be dominated by the chemisorption minimum, and the adsorption energies will be similar. Therefore on this basis, a slit pore system modelled with the chemisorption 2 potential could be considered to be equivalent to modelling a complete SWNT system using the chemisorption 2 potential, where the effects due to the curvature on the internal and external surfaces of the micropore serve to cancel each other out. (One could never make this contention for dispersion forces where the curvature within narrow micropores causes a significant deepening of the potential minimum (see figure 2).)

The chemisorption 2 potential used to model a slit pore (with results reported in [17]) gave uptakes of up to 9% at 100 bar and 298 K with 2.5% remaining adsorbed at ambient pressure. It is noted that in planar graphitic sheets there is no basis for assuming intermolecular forces other than dispersion forces. However, as discussed previously, there are reasons why it is not completely unreasonable to suppose that some kind of chemisorption could occur in SWNTs. On this basis, therefore, the 5–10% uptake reported by Heben and coworkers is not impossible.

## 6. Conclusion
Adsorption of hydrogen in multi-walled carbon nanotubes (MWNTs) and single-walled carbon nanotubes (SWNTs) has been simulated by treating the gas–solid interaction purely as dispersion forces, and also by using a hypothetical model for chemisorption used in a previous paper. Uptake of hydrogen in the internal space of a carbon nanotube is predicted to be considerably less than in a slitlike pore of a model optimal graphitic nanofibre (provided the gas–solid potential is consistent). This is consistent with the findings of Wang and Johnson [11] and Rzepa *et al.* [15]. Part of the difference arises from the assumption of pore specific surface area used in converting the raw simulation data to gravimetric adsorption: $2680\mathrm{m}^2\mathrm{g}^{-1}$ for the slit pore and $1340\mathrm{m}^2\mathrm{g}^{-1}$ for the inside of the nanotube. However, the concave curvature means that the surface area of the first adsorbed layer is less than the area defined by the ring of carbon centres. Although the model for chemisorption remains somewhat speculative, the heats of adsorption calculated from it are consistent with the measured values reported by Heben and coworkers [7] for SWNTs of the same size as modelled here. Also, there is some theoretical support in the literature for a partial re-hybridization of graphitic $\mathrm{sp}^2$ carbons when the sheets are curved.

If Heben’s reported uptake of 5–10% hydrogen in SWNTs is accurate, then

- Much of the adsorption must occur in the interstices between SWNTs.
- There must be intermolecular forces other than dispersion forces at play between the hydrogen molecules and the curved graphene sheets.

The results presented here suggest that the 5–10% hydrogen uptake reported by Heben is not impossible. However, there are two major caveats.

- A difficulty with Heben’s results is that SWNTs comprised only a small fraction of the sample. Doubts remain therefore over whether the adsorption in the non-SWNT portion of the sample has been properly accounted for in calculating the uptake due to the nanotubes. The small fraction of SWNTs in the sample also means that a practical system for hydrogen storage based on SWNTs is some way off.
- It remains possible that the high heat of adsorption reported by Heben was due to the continuing presence of metal template atoms, rather than being due to strong forces between the nanotube wall and the adsorbate.

The author wishes to thank Shell Hydrogen for permission to publish.

## Appendix
### Dispersion forces within carbon nanotubes
A mathematical description of dispersion forces within cylindrical pores has been presented previously (e.g. by Peterson *et al.* [27]), but the following analysis (particular to nanotubes) is included here for completeness.

If a pairwise potential function has the general form
$$
U=\frac{M}{r^n}, \tag{A1}
$$
then the potential function can be calculated by integration of equation (A1) over the whole pore wall. Consider the case of the interaction $u_{\text{STRIP}}$ between an

![](./images/812734671543599107_8.jpg)

Figure A1. Integration of the pairwise potential over an elemental strip of graphitic material in the pore wall.

adsorbate and an elemental strip of graphitic material of width $q$ on the wall of the nanotube (figure A1). For an infinite pore, this is given by
$$
u_{\text{STRIP}} = \int_{-\infty}^{+\infty} \frac{q \rho_{2 \text{D}} M}{y^n} \mathrm{d}x, \tag{A 2}
$$
where $\rho_{2 \text{D}}$ is the number of carbon atoms per unit area of the pore wall. After some manipulation, it can be shown that
$$
u_{\text{STRIP}} = \frac{2 q \rho_{2 \text{D}} M I_{n-2}}{l^{n-1}}, \tag{A 3}
$$
where
$$
I_{m} = \frac{\sqrt{\pi}}{2} \frac{\Gamma\left(\frac{m}{2} - \frac{1}{2}\right)}{\Gamma\left(\frac{m}{2}\right)}. \tag{A 4}
$$

This means that for the Lennard-Jones potential, the interaction is given by
$$
u_{\text{STRIP}} = -8 \varepsilon_{\text{CH}} q \rho_{2 \text{D}} \left( \frac{\sigma_{\text{CH}}^6 I_{4}}{l^5} - \frac{\sigma_{\text{CH}}^{12} I_{10}}{l^{11}} \right), \tag{A 5}
$$
where $\varepsilon_{\text{CH}}$ and $\sigma_{\text{CH}}$ are the Lennard-Jones well depth and hard sphere diameter parameters, respectively, for the interaction between a hydrogen site and graphitic carbon. The constants calculated from equation (A 4) are $I_{10} = 63\pi/516$ and $I_{4} = 3\pi/16$. In order to calculate the potential at a position within the nanotube, a numerical integration is required. However, for the special case of the centre of the pore, $q$ in equation (A 5) can be replaced with $2\pi l$ where $l$ is now the radius of the pore.

For comparison, using the same nomenclature as above, the interaction between an adsorbate site and a single graphitic surface can be shown to be
$$
u_{\text{PLANE}} = -8 \pi \varepsilon_{\text{CH}} \rho_{2 \text{D}} \left( \frac{\sigma_{\text{CH}}^6}{4 l^4} - \frac{\sigma_{\text{CH}}^{12}}{10 l^{10}} \right). \tag{A 6}
$$

These are the "10" and "4" terms of the 10-4-3 potential [19]. The "3" term in the 10-4-3 arises from summation of the attractive part of the potential function over an infinite number of stacked plates (separated by distance $\Delta$) behind the graphite later at the surface. For a comparison with the normal nomenclature for the 10-4-3 potential, $\rho_{2 \text{D}}$ is equal to $\rho \Delta$, where $\rho$ is the number of carbon atoms per unit volume of graphite when stacked into plates separated by distance $\Delta$; normally $\rho$ is taken as $114 \mathrm{nm}^{-3}$. The potential in the centre of a slitlike pore would be double, to account for the interaction with the two walls.

If the attractive term in the potential is dominant, then for single-walled slit pores of the same diameter as SWNTs, the following relationship is true for dispersion forces:
$$
\frac{u_{\text{CENTRE OF SWNT}}}{u_{\text{CENTRE OF SINGLE-WALL SLIT PORE}}} = \frac{3\pi}{4}. \tag{A 7}
$$

The same ratio must also hold for a comparison of a multi-walled nanotube (MWNT) with a slit pore having walls comprising multiple stacked graphite sheets (as would be modelled by the 10-4-3 potential), providing the number of stacked layers and the interlayer spacing are the same.

## References

[1] HYNEK, S., FULLER, W., and BENTLEY, J., 1997, *Intl J. Hydrogen Energy*, **22**, 601.
[2] CHAMBERS, A., PARK, C., BAKER, R. T. K., and RODRIGUEZ, N. M., 1998, *J. phys. Chem. B*, **102**, 4235.
[3] PARK, C., ANDERSON, P. E., CHAMBERS, A., TAN., C. D., HIDALGO, R., and RODRIGUEZ, N. M., 1999, *J. phys. Chem. B*, **103**, 10572.
[4] CHEN, P., WU, X., LIN, J., and TAN, K. L., 1999, *Science*, **285**, 91.
[5] YANG, R. T., 2000, *Carbon*, **38**, 623.
[6] PINKERTON, F. W., WICKE, B. G., OLK, C. H., TIBBETTS, G. G., MEISNER, G. P., MEYER, M. S., and HERBST, J. F., 2000, *J. phys. Chem. B*, **104**, 9460.
[7] DILLON, A. C., JONES, K. M., BEKKEDAHL, T. A., KIANG, C. H., BETHUNE, D. S., and HEBEN, M. J., 1997, *Nature*, **386**, 377.
[8] DILLON, A. C., GENNETT, T., ALLEMAN, J. L., JONES, K. M., PARILLA, P. A., and HEBEN, M. J., 2000, *Carbon nanotube materials for hydrogen storage. Proceedings of the 2000 US DOE Hydrogen Program; available at http://www.eren.doe.gov/hydrogen/docs/26938toc.html#storage*
[9] LIU, C., FAN, Y. Y., LIU, M., CONG, H. T., CHENG, H. M., and DRESSELHAUS, M., 1999, *Science*, **286**, 1127.
[10] DILLON, A. C., and HEBEN, M. J., 2001, *Appl. Phys. A*, **72**, 133.
[11] WANG, Q., and JOHNSON, J. K., 1999, *J. chem. Phys.*, **110**, 577.
[12] WANG, Q., and JOHNSON, J. K., 1999, *J. phys. Chem. B*, **103**, 277.
[13] STAN, G., and COLE, M. W., 1998, *J. low Temp. Phys.*, **110**, 539.
[14] GORDON, P. A., and SAEGER, R. B., 1999, *Ind. Eng. Chem. Res.*, **38**, 4647.
[15] RZEPA, M., LAMP, P., and DE LA CASA LILLO, M. A., 1998, *J. phys. Chem. B*, **102**, 10894.

[16] DARKRIM, F., and LEVESQUE, D., 1998, *J. chem. Phys.*,
109, 4981.

[17] CRACKNELL, R. F., 2001, *Phys. Chem. chem. Phys.*, 3,
2091.

[18] GU, C., GAO, G.-H., YU, Y.-X., and MAO, Z.-Q., 2001,
*Intl J. Hydrogen Energy*, 26, 691.

[19] STEELE, W. A., 1974, *The Interaction of Gases with Solid
Surfaces* (Oxford: Pargemon Press).

[20] JELOAICA, L., and SIDIS, V., 1999, *Chem. Phys. Lett.*, 300,
157.

[21] DRESSELHAUS, M., DRESSELHAUS, G., and ECKLUND,
P. C., 1996, *Science of Fullerenes and Carbon Nanotubes*
(New York: Academic Press).

[22] TOMBLER, T. W., ZHOU, C., ALEXSAYEV, L., KONG, J.,
DAI, H., LIU, L., JAYNATHI, C. S., TANG, M., and WU,
S.-Y., 2000, *Nature*, 405, 769.

[23] CHENG, H., PEZ, G. P., and COOPER, A. C., 2001, *J. Amer.
chem. Soc.*, 123, 5845.

[24] ALLEN, M. P., and TILDESLEY, D. J., 1987, *Computer
Simulation of Liquids* (Oxford: Clarendon Press).

[25] NICHOLSON, D., and PARSONAGE, N. G., 1982, *Computer
Simulation and the Statistical Mechanics of Adsorption*
(New York: Academic Press).

[26] KANEKO, K., CRACKNELL, R. F., and NICHOLSON, D.,
1994, *Langmuir*, 10, 4606.

[27] PETERSON, B. K., WALTON, J. P. R. B., and GUBBINS,
K. E., 1986, *J. chem. Soc. Faraday Trans*, ii, 82, 1789.