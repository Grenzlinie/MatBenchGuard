# MODELS FOR CARBON GRADIENT GENERATION IN THE WELD HEAT-AFFECTED ZONE OF C-MN STEELS

R.L. Eadie and B.M. Patchett

Dept. of Mining, Metallurgical & Petroleum Engineering
University of Alberta, Edmonton, Alberta T6G 2G6, Canada

(Received September 24, 1990)

## Introduction

Some differences in the welding behaviour of C-Mn steels have been observed by Patchett [1] when comparing hot-rolled and normalized steels (A516 Gr70 and Lloyds LT-60) at a carbon level of about 0.2%. For a given heat input, normalized structures were less prone to hydrogen-assisted cracking (HAC) than hot-rolled structures and hardness levels in the heat-affected zone (HAZ) near the fusion line were higher in the hot-rolled material. There is some evidence that structural and pressure vessel failures, in which HAC played a prominent role, have been associated with welding hot-rolled steels at low heat inputs [2]. Metallography of A516 Gr70 material in a non-welded condition showed, as expected, a coarser structure in the hot rolled material. Normalizing the same material produced finer pearlite colony sizes and smaller lamellar spacing within the colonies, also as expected. The harder microstructures produced in the hot-rolled material suggested that carbide dissolution and migration in the coarser microstructure was retarded, causing a partial retention of its carbon gradient (between pearlite colonies) in the HAZ during the welding thermal cycle. On cooling from the peak welding temperatures, there were thus regions of austenite in the HAZ which had higher than nominal C levels and associated higher hardenability. It is the harder martensite/bainite associated with these regions which would make the steel more susceptible to HAC. In this paper we shall consider the microstructural characteristics of the base metal and present diffusion models to illustrate how thermal processing history may affect the carbon gradients in the HAZ and hence influence the tendency toward HAC.

## Transformation to Austenite

In welds, there are severe thermal gradients in a very small zone near the fusion line, both as the temperature increases and as it later decreases. The peak temperature varies from $T_m$ down to the $A_1$ within a few mm. The total time spent above the $A_1$ varies from less than 1 second up to about 10 seconds in most arc welding procedures. Thus the "heat-treating" conditions are far removed from normal practices and significant deviations from expected microstructures may occur.

Mehl [3] suggested that pearlite transforms with difficulty to austenite at the eutectoid temperature with the transformation occurring more rapidly the higher the temperature. The nucleation of austenite only begins after 6 s. at $750^\circ$C and after 2 s. at $800^\circ$C. At $850^\circ$C, the production of homogeneous austenite requires about 3 minutes to complete. Hypoeutectoid steels resist transformation to austenite below $910^\circ$C in proeutectoid ferrite regions until the carbon level has been enhanced by diffusion from the neighbouring pearlite regions. This can only occur after the transformation of the pearlitic regions has occurred. For the purposes of this report it will be considered that the transformation of these proeutectoid regions begins when the temperature rises above $910^\circ$C and continues until the temperature falls below the solvus for the carbon level in the region when the austenite becomes unstable. For the purposes of the diffusion model then we will include time spent above $910^\circ$C on heating and time spent down to $850^\circ$C on cooling.

## Model Geometries

Typical microstructures for the base metals are shown in Fig. 1.


![](./images/812402555161149440_1.jpg)

FIG.1 Microstructures of (a) Normalized and (b) Hot-Rolled A516 Gr70 Plate.

The normalized structure is more variable than the hot-rolled structure, possibly because the normalizing procedure has not removed all traces of the banding present in the hot-rolled structure. The ferritic regions are globular and more or less surrounded by layers of pearlite. The carbon content of the pearlite will be taken as a uniform 0.77%. We shall show that the homogenization time for this pearlitic region (once it has transformed) is negligible compared to the time for diffusion of carbon into the region of prior ferrite. The normalized structure will be modeled as spheres of ferrite surrounded by uniform shells of pearlite as depicted in Figure 2a. The radius of the sphere is the dimension of the largest region of ferrite seen in Figure 1a, about $10\ \mu\text{m}$. This represents the majority of the regions, but is not strictly the worst case. The appropriate pearlite shell size for a carbon level of 0.2% is $10.8\ \mu\text{m}$.

![](./images/812402555161149440_2.jpg)

In Fig. 1b, the hot rolled structure is clearly banded. This can be modelled as alternate layers of ferrite and pearlite. For an overall carbon level of 0.2% the ferrite band is 3 times thicker than the pearlite band. The bands are about 60 and $20\ \mu\text{m}$ respectively. To a good approximation, the carbon concentration in the pearlite is 0.77%

and in the ferrite is 0.02%. We shall show that the time for the austenite to homogenize in the prior pearlite regions is negligible compared to the carbon diffusion time across the 60 µm former ferrite band. The idealized geometry and its symmetry element are shown in Figure 2b.

### Diffusion Model for the Normalized Case

For the spherical geometry associated with the normalized microstructure, a reasonable approximation is that of diffusion into a sphere from a well stirred solution of limited volume. This is appropriate because the depth of shell to account for the 25% by volume pearlite structure is only about 8% of the radius of the sphere of ferrite. The solution for this problem is found in Berthier [4]. In its complete form the solution for the concentration gradient in the sphere is given by:

$$
C(r,t)=\frac{1}{1+K}+\sum_{i=1}^{\infty} \frac{6K}{3K(3K+3)+\alpha_{i}^{2}} \frac{\sin \alpha_{i} \xi}{\sin \alpha_{i}} \exp \left\{-\alpha_{i}^{2} \tau\right\} \tag{1}
$$

where "a" is the sphere radius, "V" is the liquid volume, $K = 3V/4\pi a^{2}$, $\xi = r/a$, $\alpha_{i}$ are the non-zero roots of $\alpha \cot \alpha - \left(1+\frac{\alpha^{2}}{3K}\right)=0$ and $\tau = \frac{Dt}{a^{2}}$. A graph of the percent completion versus $\tau$ for this solution is found in Crank [5]. For the present case, the graph indicates that diffusion into the sphere is 95% complete when $\sqrt{Dt} = 3.1$ µm. Any remaining high carbon regions would then be discontinuous and quite small.

### Diffusion Model for the Hot Rolled Case

This repeating structure can be truncated at the symmetry planes in the centres of the high carbon and low carbon regions. The problem is essentially that of a finite one dimensional slab with a region of uniform solute at one end. The solution to this problem was first reported some time ago by Stefan [6] and is based on the similar problem for the semi-infinite slab and an application of the principle of reflection at the boundaries. An account of this solution is given in Jost [7]. For an infinite slab with solute of $C_{0}$ over length "p" the concentration profile is described by:

$$
C=\frac{C_{0}}{2}\left[ \text{erf}\left(\frac{p+x}{2\sqrt{Dt}}\right)+\text{erf}\left(\frac{p-x}{2\sqrt{Dt}}\right)\right] \tag{2}
$$

This is modified by reflection at the boundary for the finite slab case. The concentration profiles for a slab of length 4p having initial solute of concentration $C_{0}$ along a length "p" is shown in Fig. 3 for a number of values of the parameter $\sqrt{Dt}$.

![](./images/812402555161149440_3.jpg)

The parameter "p" is, in this case, 0.125 of the repeat distance for the structure (r). We see immediately that the diffusion is significant at $\sqrt{Dt} = p$ (10 μm) and is essentially complete when $\sqrt{Dt}$ reaches 2.5p (25 μm). For $\sqrt{Dt} < p$, there is essentially no difference between the infinite slab and finite slab cases. For large values of $\sqrt{Dt}$ , there are numerous reflections and for the one case shown ($\sqrt{Dt} = 2.5p$) the tabulation of Kawalki [8] was used. It is significant that the characteristic distance for homogenization is nearly an order of magnitude larger in this case (25 μm) than for the normalized case (3.1 μm). It means that we are much more likely to have regions of high carbon persisting during the welding thermal cycle in the hot-rolled case, leading to attendant HAC problems. If welding is parallel to the banding, then the affected regions could be continuous.

This type of diffusion solution is also appropriate to model the diffusion of carbon within the lamellar pearlite structure. The repeat distance (r) in the normalized and hot-rolled cases were determined from photomicrographs [1] as approximately 0.17 and 0.53 μm respectively. The ratio of cementite to ferrite plate width is 8. From Table VI (p. 66) in [7] we can conclude that the homogenization of austenite from such a structure would be virtually complete when $\sqrt{Dt} = 0.3$ r. Thus, for the normalized case, homogenization of the prior pearlite regions requires a diffusion distance of 0.05 μm compared to 3.1 μm for the overall homogenization. Local homogenization of pearlite takes only 0.03% of the time required for complete homogenization. For the hot-rolled case, the characteristic diffusion distances are 0.16 and 25 μm respectively. Pearlite homogenization requires only 0.004% of the time required for complete homogenization. Therefore the important step is the the equilibration of carbon level between the eutectoid austenite colonies and the surrounding ferritic areas.

### Discussion

With approximate diffusion solutions in hand, it only remains to look at the thermal history in the weld region and select suitable diffusion coefficients. The diffusion coefficients for carbon in the austenitic region (1000 -1200°C) for Fe - 1% Mn was determined at 0.4% C by Blanter [9] and has been reported in Smithells [10] as:

$$
\mathbf{D}=0.08\left(\frac{\mathrm{cm}^{2}}{\mathrm{~s}}\right) \exp \left\{\frac{-31,600}{1.987 T}\right\} \tag{3}
$$

The thermal history at the fusion line for a submerged arc weld with a heat input of 2 kJ/mm was determined by Smith [11] and is shown in Fig. 4.

![](./images/812402555161149440_4.jpg)

FIG.4 Fusion Line Thermal Cycle for a 2 kJ/mm Submerged Arc Weld.

The solid metal is in the temperature range of interest for about 5 s. The approximate value of $\sqrt{Dt}$ for this curve is 62 μm. This is greater than than even the characteristic distance in the hot-rolled case and indicates the carbon is

fully homogenized in the austenite by the time the temperature passes below $A_3$ after the weld. However, further out in the HAZ, the peak temperature and time above $900^\circ$C will be lower and there will be a zone that will not reach equilibrium. For example, if the steel spent 2.5 s between 1000 and $850^\circ$C, then $\sqrt{Dt}$ for that thermal cycle is about $5\ \mu$m (0.5 p). Therefore there would be a region of about $20\ \mu$m (considering both sides of the centre of symmetry) that would have carbon levels above 0.5% and hence would have significantly higher hardenability. On cooling below the eutectoid, this region would have a significantly higher tendency to transform to martensite and render the HAZ susceptible to HAC. Furthermore, if the structure is banded and the bands of pearlite were parallel to the weld axis, then the susceptible zone would be continuous. In the normalized structure, the high carbon regions would be discontinuous and much smaller. The regions not achieving equilibrium %C levels in the austenite would have to be further from the fusion line, where the diffusion time is significantly shorter and the peak temperature lower. These small, discontinuous regions would reduce the tendency of carbon segregation to contribute to problems with HAC.

In summary, these approximate diffusion models for carbon migration during austenitization show that, in ferritic steels containing pearlite, a weld HAZ will contain regions of sufficient hardenability to affect resulting microstructure and hardness significantly, regardless of nominal steel chemical composition. Hot-rolled steels will have larger and more continuous regions of higher hardenability than normalized steels of the same chemistry, and these regions may be continuous along the fusion line. Therefore HAC would be expected to be more prominent in hot-rolled steels, as has been observed [1].

## Acknowledgments

One of the authors (BMP) would like to thank the Canadian Electrical Association for financial support of the experimental work.

## References

1.  B.M. Patchett, CEA Report No. 109 G 276, "Assessment of Alternate Steels for Welded Pressure Vessels", University of Alberta, Edmonton (1987).
2.  B.M. Patchett, "The Effect of Pearlite Coarseness on HAZ Hardness in C-Mn Steels", Paper 18, International Conference Welded Structures '90, The Welding Institute, London November (1990).
3.  R.F. Mehl, Transactions ASM, 29, 813 (1941).
4.  G. Berthier, J. Chim. Phys. 49, 527 (1952).
5.  J. Crank, The Mathematics of Diffusion, $2^{nd}$ Ed., p. 95, Clarendon Press, Oxford (1975).
6.  A. Stefan, Sitzungsber. Wiener Akad. Wissensch. II, 68, 385 (1873).
7.  W. Jost, Diffusion in Solids, Liquids, Gases, Academic Press, New York (1952).
8.  W. Kawalki, Wied. Ann., 52, 166 (1894).
9.  M. Blanter, Zhur. Tech. Phys. SSSR, 21, 818 (1951).
10. C.J. Smithells, Metals Reference Book, $6^{th}$ Edition, E.A. Brandes (ed.), pp. 13-58, Butterworths, London (1983).
11. N.J. Smith, Private Communication, Metals Technology Laboratory (EMR), Ottawa (1990).