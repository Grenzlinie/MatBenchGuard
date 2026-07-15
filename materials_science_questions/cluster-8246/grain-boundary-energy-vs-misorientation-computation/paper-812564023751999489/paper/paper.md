# Molecular dynamics study of grain boundaries and triple junctions in ice

Cite as: J. Chem. Phys. 153, 124502 (2020); https://doi.org/10.1063/5.0021635
Submitted: 13 July 2020 . Accepted: 02 September 2020 . Published Online: 23 September 2020

Takuma Yagasaki, Masakazu Matsumoto, and Hideki Tanaka

![](./images/812564023751999489_1.jpg) ![](./images/812564023751999489_2.jpg) ![](./images/812564023751999489_3.jpg)

## ARTICLES YOU MAY BE INTERESTED IN

### Fragility and correlated dynamics in supercooled liquids
The Journal of Chemical Physics 153, 124501 (2020); https://doi.org/10.1063/5.0015091

### Liquid-liquid transition and polyamorphism
The Journal of Chemical Physics 153, 130901 (2020); https://doi.org/10.1063/5.0021045

### Connection between liquid and non-crystalline solid phases in water
The Journal of Chemical Physics 153, 104503 (2020); https://doi.org/10.1063/5.0018923

![](./images/812564023751999489_4.jpg)

J. Chem. Phys. 153, 124502 (2020); https://doi.org/10.1063/5.0021635
153, 124502

© 2020 Author(s).

# Molecular dynamics study of grain boundaries and triple junctions in ice

Cite as: J. Chem. Phys. 153, 124502 (2020); doi: 10.1063/5.0021635
Submitted: 13 July 2020 • Accepted: 2 September 2020 •
Published Online: 23 September 2020

![](./images/812564023751999489_5.jpg)
![](./images/812564023751999489_6.jpg)
![](./images/812564023751999489_7.jpg)

Takuma Yagasaki,a) Masakazu Matsumoto, and Hideki Tanaka

## AFFILIATIONS

Research Institute for Interdisciplinary Science and Department of Chemistry, Faculty of Science, Okayama University, Okayama 700-8530, Japan

a)Author to whom correspondence should be addressed: t.yagasaki@gmail.com

## ABSTRACT

We perform classical molecular dynamics simulations of polycrystalline ice at 250 K using the TIP4P/Ice model. The structures of polycrystalline ice are prepared by growing ice particles in supercooled water. An order parameter developed recently is used to characterize local structures in terms of the liquid-liquid phase transition scenario. It is shown that the grain boundaries and triple junctions in ice are structurally similar to low-density liquid water in which most water molecules form four hydrogen bonds and the O-O-O angles deviate from the tetrahedral angle of 109.47°. The thickness of the grain boundaries is ~1 nm. The diffusion coefficient of water molecules along the grain boundaries calculated in this study, $5.0 \times 10^{-13}\ \text{m}^2\ \text{s}^{-1}$, is in good agreement with experimental data. The diffusion along the triple junctions is 3.4 times faster than that along the grain boundaries. We model the grain size dependence of diffusivity of water molecules in polycrystalline ice using the simulation results and find that the impact of the grain boundaries and the triple junctions on the diffusivity is negligible for typical polycrystalline ice samples having grain sizes of the order of millimeters. We also demonstrate that the properties of the grain boundaries are quite different from those of the ice/vapor interface at the same temperature: the quasi-liquid layer at the ice/vapor interface is similar to high-density liquid water and the diffusion coefficient along the ice/vapor interface is two orders of magnitude larger than that along the grain boundaries.

Published under license by AIP Publishing. https://doi.org/10.1063/5.0021635

## INTRODUCTION

Naturally occurring ice is usually polycrystalline. The volume fraction of the grain boundary region in an ice sample is very small, and that of the triple junction region at which three grains meet is even smaller. However, these defects play a critical role in various physical processes of ice. $^{1-3}$ For example, the electric conductivity in polycrystalline crystals is higher than that in single crystals, and it has been attributed to the ionic species accumulated in the grain boundary and triple junction regions. There are substantial differences in mechanical properties between single and polycrystalline ice samples. The plastic deformation of a single crystal is mainly due to slip on the basal plane, whereas this type of deformation is blocked by other grains in polycrystalline ice. Instead, sliding of grains over one another on the plane of the boundary and migration of grain boundaries involving transfer of water molecules from a grain to the other occur in the deformation process of polycrystalline ice.

It is possible to explore the history of climate change on the basis of the concentration profiles of chemical species such as water isotope, carbon dioxide, and sulfate in polar ice cores. $^{4-7}$ The concentration profiles must be corrected considering the diffusion of the particles in the ice sample. The diffusion coefficients at the grain boundaries and the triple junctions are important parameters for this correction. $^{8,9}$ The diffusion coefficient of water molecules at the grain boundaries is also associated with the mobility of the boundaries. $^{10}$

The diffusion coefficient of water molecules in polycrystalline ice, $D_{\text{pc}}$, can be expressed as

$$
D_{\text{pc}} = (1 - f_{\text{gb}} - f_{\text{tj}})D_{\text{sc}} + f_{\text{gb}}D_{\text{gb}} + f_{\text{tj}}D_{\text{tj}}, \tag{1}
$$

where $D_{\text{sc}}$, $D_{\text{gb}}$, and $D_{\text{tj}}$ are the diffusion coefficients in single crystalline ice, along the grain boundaries, and along the triple junctions, respectively. $^{11}$ Only $D_{\text{pc}}$ and $D_{\text{sc}}$ can be directly measured in experiments. Knowledge of the volume fraction of the grain boundary

molecule when the distance between the closest intermolecular O-H pair is shorter than $0.245\ \text{nm}.^{34,44}$

The Widom line is the extension of the liquid-liquid coexistence line at which thermodynamic response functions such as the specific heat are maximized. $^{45}$ The structure of liquid water changes from HDL-like to LDL-like at the Widom line as the temperature decreases. $^{46,47}$ We perform MD simulations of liquid water containing 1600 molecules at 1 bar and calculate the temperature dependence of the specific heat, which is plotted in Fig. 1(a). The two-dimensional (2D) distribution functions of the twist parameter are also calculated from the trajectories, and they are shown in Figs. 1(b)-1(d). As shown in Fig. 1(a), the Widom line is located at $\sim 240\ \text{K}$ at 1 bar for the TIP4P/Ice model. Therefore, liquid water is HDL-like at 300 K and 250 K. The 2D distribution function of HDL is characterized by the peak at $\chi=0$ [Figs. 1(b) and 1(c)]. $^{34}$ This peak disappears completely in the distribution function of the LDL-like liquid at 200 K [Fig. 1(d)]. Figure 1(e) shows the 2D distribution functions of ice $\text{I}_\text{h}$. The system size and the pressure of the MD simulation of ice are the same as those for liquid water. The peak at $\text{Re}\ \chi=-1$ arises from the hydrogen bonds of the six-membered rings of chair conformation and the peak at $\text{Re}\ \chi=1$ is due to the hydrogen bonds that are parallel to the $c$-axis.

It is possible to classify hydrogen bonds into those in ice and in liquid water by solely using the real part of $\chi$. Figure 2(a) shows the probability distribution function of $(\text{Re}\ \chi)^2$. There is a peak at $(\text{Re}\ \chi)^2=0.8$ in the distribution functions of ice, whereas the peak is found at $(\text{Re}\ \chi)^2=0.0$ for liquid water. A reasonable threshold for the classification is $(\text{Re}\ \chi)^2=0.5$ at which the probability for ice at 250 K is the same as that for liquid water at the same temperature.

All O-O-O angles are the tetrahedral angle of $109.47^\circ$ in ice. We quantify the deviation from the tetrahedral angle for each molecule using the following order parameter:
$$
\Delta\theta_i^2=\frac{1}{N C_2}\sum_{j=1}^{N-1}\sum_{k=j+1}^{N}(\theta_{jik}-109.47)^2,\tag{3}
$$
where $N$ is the number of hydrogen bonds for molecule $i$ and $\theta_{jik}$ is the $\text{O}_j-\text{O}_i-\text{O}_k$ angle. The distribution function of $\Delta\theta_i^2$ is shown in Fig. 2(b). This order parameter can also be used for the classification of local structures with a threshold value of $\Delta\theta_i^2=150$.

![](./images/812564023751999489_8.jpg)

FIG. 2. Probability distribution function of (a) $(\text{Re}\ \chi)^2$ and (b) $\Delta\theta_i^2$ for ice $\text{I}_\text{h}$ (black solid) and liquid water at 300 K (red dotted), 250 K (green dashed), and 200 K (blue dashed-dotted) calculated from the single-phase simulations of $N_w=1600$.

## RESULTS AND DISCUSSION

Polycrystalline ice structures are prepared by growing ice particles in liquid water using MD simulations. The dimensions of the simulation box are $16\times14\times20\ \text{nm}^3$. Half of the box, $0\ \text{nm}< z<10\ \text{nm}$, is filled with liquid and water while the other half remains empty. This configuration allows us to examine the ice/vapor interface in addition to the grain boundaries. The liquid configuration is equilibrated at 250 K for 5 ns, and the configurations at $t=1\ \text{ns}$, $2\ \text{ns}$, $3\ \text{ns}$, $4\ \text{ns}$, and $5\ \text{ns}$ are recorded. Then, two or four spherical particles of ice $\text{I}_\text{h}$ with a radius of 2.8 nm are inserted in the liquid region of the recorded configurations removing overlapped molecules. The ice $\text{I}_\text{h}$ structures are generated using the Genice tool. $^{48}$ The total number of water molecules in a system is roughly 70 000 (the number of removed water molecules is different for each configuration). Two ice particles are placed at $(x,y,z)=(0\ \text{nm},0\ \text{nm},5\ \text{nm})$ and $(8\ \text{nm},0\ \text{nm},5\ \text{nm})$ in 2-grain simulations [Figs. 3(a) and 3(b)], and four ice particles are placed at $z=5\ \text{nm}$ so that they form a 2D triangular lattice on the $xy$ plane in 4-grain simulations [Figs. 3(c) and 3(d)]. The orientation of each ice particle is randomly chosen. A constant-volume MD simulation is performed to grow the ice particles in the water slab at 250 K, which is lower than the melting temperature of the employed force field model by 20 K. Figure 4 shows the time evolution of the potential energy. The potential energy decreases with time until the whole system is frozen. The structural and dynamic properties shown below are calculated from the last 800 ns of the trajectories where the potential energy no longer changes with time. The potential energy of this region is higher for the 4-grain simulations $(-60.1\ \text{kJ}\ \text{mol}^{-1})$ than for the 2-grain simulations $(-60.5\ \text{kJ}\ \text{mol}^{-1})$ because of the smaller grain size and the existence of triple junctions in the 4-grain simulations.

Panels (e) and (f) in Fig. 3 show the final structure of one out of the five 2-grain simulations. There are layers of red hydrogen bonds at $z=0\ \text{nm}$ and $10\ \text{nm}$ in panel (e), indicating that the local structures of the ice/vapor interfaces are disordered like liquid. Layers of red hydrogen bonds also exist at $x=4\ \text{nm}$ and $12\ \text{nm}$. These are grain boundaries formed by the two ice particles. An ice particle is in contact with itself at $y=\sim7\ \text{nm}$ without a distinct boundary. Figures 3(g) and 3(h) show the final structure of a 4-grain simulation. Eight triple junctions form as a result of the growth of the four ice particles. Several snapshots along the trajectory are shown in Fig. S1 of the supplementary material.

![](./images/812564023751999489_9.jpg)

FIG. 3. Hydrogen bond networks of a 2-grain simulation and a 4-grain simulation. The left [(a)-(d)] and right [(e)-(h)] panels show the initial and final structures of the simulations. The slices of the simulation boxes in the xz plane at y = 0 nm are shown in panels (a), (c), (e), and (g), and those in the xy plane at z = 5 nm are shown in panels (b), (d), (f), and (h). The thickness of the slice is 1 nm. A bond is red when its (Re $\chi$)$^2$ value is lower than 0.5. Otherwise, the bond is colored black.

We do not observe migration of the grain boundaries within the simulation time. This is consistent with the experimental fact that the timescale of grain boundary migration is much longer than that of MD simulations. $^{10,49}$ Grain boundary migration in ice was observed in MD simulations of Chan et al. $^{50}$ This is because they employed a coarse-grained water model, and the potential energy surface of such a water model is much smoother due to the absence of hydrogen atoms. $^{51}$

It has been shown that ice particles grown in MD simulations are not ice I$_h$, but stacking disordered ice I. $^{52-55}$ The twist parameter can be used to detect stacking faults because the value of Re $\chi$ is negative for all the hydrogen bonds in ice I$_c$, whereas the Re $\chi$ value for the hydrogen bonds parallel to the c-axis in ice I$_h$ is positive. $^{34}$ Figures 5(a) and 5(b) are the same as Figs. 3(f) and 3(h), but ice-like bonds with Re $\chi$ < 0 are removed. There are layers of ice I$_c$ in the blank regions in Fig. 5. It is expected that there is no substantial difference between the I$_h$/I$_h$, I$_c$/I$_h$, and I$_c$/I$_c$ boundaries because of the similarity between the I$_h$ and I$_c$ structures. Indeed, there seems no effect of the cubic ice layers on the thickness of the grain boundaries. We do not distinguish I$_h$ and I$_c$ in the following analyses.

![](./images/812564023751999489_10.jpg)

FIG. 4. Time evolution of the potential energies of all five replicas for the (a) 2-grain and (b) 4-grain simulations.

We calculate the number density profile of the liquid-like (red) and ice-like (black) hydrogen bonds along the x direction in the 2-grain systems. The yellow boxes in Fig. 6(a) are the regions for which the density profiles are calculated. The number density profiles of ten grain boundaries (5 replicas × 2 boundaries) are shown by thin curves in Fig. 6(b), and the average over all the grain boundaries is shown by the thick curve. The center of each grain boundary, $x_0$, is

![](./images/812564023751999489_11.jpg)

FIG. 5. Liquid-like hydrogen bonds (red) and ice-like hydrogen bonds parallel to the c-axis of ice I$_h$ (black) in the (a) 2-grain and (b) 4-grain systems. The ice-like hydrogen bonds of the six-membered rings of chair conformation are not shown; there are layers of ice I$_c$ in the blank regions.

![](./images/812564023751999489_12.jpg)

FIG. 8. 2D distribution functions of the twist parameter for the (a) grain boundary, (b) triple junction, and (c) ice/vapor interface regions.

Fig. 1(d), except for the peaks at $\chi \sim 1$ and $-1$ arising from the ice-like molecules in the boxes. The structure of the triple junction region (cyan boxes) is also LDL-like as shown in Fig. 8(b). Figure 8(c) is the 2D distribution function of the ice/vapor interfaces (green boxes). We find a peak at $\chi \sim 0$, which is a characteristic feature of HDL (a similar distribution function is obtained for the basal, primary prismatic, and secondary prismatic planes as shown in Fig. S3). The 2D distribution functions are consistent with the observation that the local density of the grain boundary region is lower than that of the ice/vapor interface.

There are two types of deviation from the crystalline structure of ice I, deviation of the O-O-O angle from $109.47^{\circ}$ and deviation of the coordination number from 4. The left panels of Fig. 9 present a snapshot of a 4-grain simulation where each water molecule is classified using $\Delta\theta_{i}^{2}$ that reflects only the deviation from $109.47^{\circ}$. Both the water molecules at the grain boundaries and the ice/vapor interfaces are classified as orientationally disordered molecules. The particles in the right panels are colored on the basis of the number of hydrogen bonds, $N_{HB}$. Most of the water molecules in the grain boundary and triple junction regions are four-coordinated, whereas the number of hydrogen bonds is less than four for the water molecules in the outermost layer of the ice/vapor interfaces.

![](./images/812564023751999489_13.jpg)

FIG. 9. Classification of water molecules based on [(a) and (b)] the orientational order parameter, $\Delta\theta_{i}^{2}$, and [(c) and (d)] the number of hydrogen bonds, $N_{HB}$. Red spheres and black dots in the left panels are orientationally disordered ($\Delta\theta_{i}^{2}>150$) and ordered ($\Delta\theta_{i}^{2}\leqq150$) water molecules, respectively. Red spheres, black dots, and green spheres in the right panels are water molecules with $N_{HB}\leqq3$, $N_{HB}=4$, and $N_{HB}\geqq5$.

We count the number of the liquid-like molecules, $N_{liq}^{mol}$, and that of the ice-like molecules, $N_{ice}^{mol}$, in the three types of boxes defined in Fig. 7 using the orientational order parameter with the threshold of $\Delta\theta_{i}^{2}=150$. The fraction of liquid-like molecules is given by $f_{liq}^{mol}=N_{liq}^{mol}/(N_{liq}^{mol}+N_{ice}^{mol})$. The fraction of water molecules with $N_{HB}\neq4$ is expressed by $f_{N_{HB}\neq4}$. Table I shows that the ratio of $f_{N_{HB}\neq4}$ to $f_{liq}^{mol}$ is only $\sim0.05$ in the grain boundary and triple junction regions, whereas the ratio is 0.282 for the ice/vapor interfaces. Table I also shows the fraction of liquid-like hydrogen bonds, $f_{liq}^{bond}$, calculated using the twist parameter with the threshold value of $(\text{Re }\chi)^{2}=0.5$. $f_{liq}^{bond}$ is close to $f_{liq}^{mol}$ for all three types of boxes.

There are many methods that can distinguish ice-like and liquid-like water molecules. $^{56-65}$ We select two of them to compare $(\text{Re }\chi)^{2}$. One is the CHILL+ algorithm and the other is the polyhedral template matching (PTM) algorithm. $^{61,62}$ These two have been implemented in the Ovito visualization software. $^{66}$ CHILL+ was developed to classify water molecules into the following six types: molecules in hexagonal ice, cubic ice, interfacial ice, clathrate hydrate, interfacial clathrate hydrate, and others. $^{61}$ $f_{liq}^{\text{CHILL(a)}}$ in Table I is the fraction of liquid-like molecules when the water molecules belonging to hexagonal ice, cubic ice, and interfacial ice are assumed to be ice-like. We can also assume that the interfacial ice molecules are liquid-like. The fraction calculated under this assumption is $f_{liq}^{\text{CHILL(b)}}$. We find that $f_{liq}^{bond}$ is close to $(f_{liq}^{\text{CHILL(a)}}+f_{liq}^{\text{CHILL(b)}})/2$. This means that the classification of CHILL+ is similar to that of $(\text{Re }\chi)^{2}$ if half the interfacial ice molecules are classified as liquid-like. The PTM algorithm implemented in Ovito can identify eight types of local crystalline order: face-centered cubic, hexagonal close-packed, body-centered cubic, icosahedral coordination, simple cubic, graphene, cubic diamond, and hexagonal diamond. $^{62,66}$ In this study, only the cubic diamond and hexagonal diamond structures need to be considered. The PTM algorithm requires a cutoff value of the root mean square deviation (RMSD) of the template matching for classification. This value is set to be 0.15 (Fig. S4). The fraction calculated using the PTM algorithm, $f_{liq}^{\text{PTM}}$, is very close to $f_{liq}^{\text{CHILL(b)}}$, indicating that the interfacial ice molecules in the CHILL+ algorithm are classified into liquid-like molecules in the PTM algorithm.

We calculate the MSD of water molecules in the yellow boxes defined in Fig. 7 to determine the diffusion coefficient of water in the grain boundary region. There are liquid-like and ice-like water molecules in the boxes with fractions of $f_{liq}$ and $f_{ice}=1-f_{liq}$. The MSD is given by

$$
r^{2}(\tau)=f_{\text{liq}}r_{\text{liq}}^{2}(\tau)+\left(1-f_{\text{liq}}\right)r_{\text{ice}}^{2}(\tau),\tag{6}
$$

where $r_{\text{liq}}^{2}(\tau)$ and $r_{\text{ice}}^{2}(\tau)$ are the MSDs of the liquid-like and ice-like water molecules, respectively. We obtain

$$
r_{\text{liq}}^{2}(\tau)=\frac{r^{2}(\tau)}{f_{\text{liq}}}\tag{7}
$$

<table><caption>TABLE I. Fraction of the liquid-like bonds calculated using the twist parameter ($f_{\text{liq}}^{\text{bond}}$), the fractions of liquid-like molecules calculated using the orientational order parameter ($f_{\text{liq}}^{\text{mol}}$), CHILL+ algorithm ($f_{\text{liq}}^{\text{CHILL}}$), and PTM algorithm ($f_{\text{liq}}^{\text{PTM}}$) in the boxes defined in Fig. 7. The interfacial ice molecules are counted as ice-like molecules in $f_{\text{liq}}^{\text{CHILL(a)}}$, whereas they are assumed to be liquid-like in $f_{\text{liq}}^{\text{CHILL(b)}}$. $f_{N_{\text{HB}} \neq 4}$ is the fraction of water molecules with $N_{\text{HB}} \neq 4$.</caption>
<tbody>
<tr>
<td>
</td>
<td>
$f_{\text{liq}}^{\text{mol}}$
</td>
<td>
$f_{N_{\text{HB}} \neq 4}$
</td>
<td>
$f_{N_{\text{HB}} \neq 4}/f_{\text{liq}}^{\text{mol}}$
</td>
<td>
$f_{\text{liq}}^{\text{bond}}$
</td>
<td>
$f_{\text{liq}}^{\text{CHILL(a)}}$
</td>
<td>
$f_{\text{liq}}^{\text{CHILL(b)}}$
</td>
<td>
$f_{\text{liq}}^{\text{PTM}}$
</td>
</tr>
<tr>
<td>
Grain boundary (yellow boxes)
</td>
<td>
0.305
</td>
<td>
0.013
</td>
<td>
0.044
</td>
<td>
0.332
</td>
<td>
0.218
</td>
<td>
0.410
</td>
<td>
0.406
</td>
</tr>
<tr>
<td>
Triple junction (cyan boxes)
</td>
<td>
0.527
</td>
<td>
0.032
</td>
<td>
0.061
</td>
<td>
0.638
</td>
<td>
0.572
</td>
<td>
0.838
</td>
<td>
0.865
</td>
</tr>
<tr>
<td>
Ice/vapor interface (green boxes)
</td>
<td>
0.393
</td>
<td>
0.111
</td>
<td>
0.282
</td>
<td>
0.406
</td>
<td>
0.349
</td>
<td>
0.480
</td>
<td>
0.469
</td>
</tr>
</tbody>
</table>

because $r_{\text{liq}}^2(\tau)$ is much larger than $r_{\text{ice}}^2(\tau)$. We use $f_{\text{liq}}^{\text{bond}}$ in Table I as $f_{\text{liq}}$ in Eq. (7). $r^2(\tau)$ is calculated from the displacement of water molecules located in any yellow box at $\tau = 0$ (i.e., escape of the molecules from the box during $\tau$ is allowed). Figure 10(a) shows that $r_{\text{liq}}^2(\tau)$ parallel to the grain boundaries can be well fit to a linear function for $t > 40$ ns. The diffusion coefficient obtained from the slope is $D_{\text{gb}} = 5.0 \times 10^{-13}$ m$^2$ s$^{-1}$. Moreira <i>et al.</i> calculated the MSD of the $\Sigma 35$ grain boundary of ice up to 100 ns at 266 K using the TIP4P/Ice model and reported that the MSD can be approximated to a power-law function, $r^2(\tau) \sim t^\alpha$, with $\alpha \sim 0.75$ for a range of 10 ns $< t < 100$ ns.$^{18}$ We find that our result can also be approximated to a power-law function with $\alpha \sim 0.78$ for the same range (black curve). Moreira <i>et al.</i> attributed the sub-diffusive behavior ($\alpha < 1$) to glassy dynamics of water molecules moving in a jump-like fashion between traps with a power-law waiting-time distribution. The long time region of the MSD is linear ($\alpha = 1$) because it reflects the averaged behavior of water molecules that experience many jumps at different local structures.$^{67}$ Figure 10(a) shows that the MSD perpendicular to the grain boundaries is non-linear even for the long time region. This is because of the confinement of mobile water molecules in a narrow space for this direction.$^{68,69}$

![](./images/812564023751999489_14.jpg)

FIG. 10. (a) MSD of water molecules in the grain boundary region. The parallel component (the average of the $y$- and $z$-components) and the perpendicular component ($x$-component) are shown by the yellow and blue symbols, respectively. The parallel component is fitted by a linear function (red dotted line) and a power-law function (black solid curve). The inset shows the MSDs on a log–log scale. (b) MSDs along the grain boundaries (yellow), triple junctions (cyan), and ice/vapor interfaces (green). The average over the $x$-, $y$-, and $z$-components of the MSD of liquid water at the same temperature is shown by the black symbols. Each MSD is fitted by a linear function to determine the diffusion coefficient (dotted line).

We compare the diffusion coefficient parallel to the grain boundaries determined from the slope of the MSD, $D_{\text{gb}} = 5.0 \times 10^{-13}$ m$^2$ s$^{-1}$, with the value estimated in the experimental study of Lu <i>et al.</i>$^{12}$ The temperature of the present study, 250 K, is out of range of the experimental study of $T \geq 261$ K. However, it is possible to extrapolate the data using the reported activation energy of 69 kJ mol$^{-1}$. The extrapolated value is $1.7 \times 10^{-13}$ m$^2$ s$^{-1}$ at 250 K. Our simulation result is satisfactorily close to this value.

The MSDs along the grain boundaries, triple junctions, and ice/vapor interfaces are shown in Fig. 10(b) together with the MSD of liquid water at the same temperature. We obtain $D_{\text{tj}} = 1.7 \times 10^{-12}$ m$^2$ s$^{-1}$, which is 3.4 times larger than $D_{\text{gb}}$. The diffusion coefficient of water along the ice/vapor interfaces is 3.4 $\times 10^{-11}$ m$^2$ s$^{-1}$. This value is two orders of magnitude larger than $D_{\text{gb}}$ and comparable to the diffusion coefficient of bulk liquid water, $9.6 \times 10^{-11}$ m$^2$ s$^{-1}$.

Now, we can evaluate the impact of the grain boundaries and the triple junctions on the diffusion coefficient of water molecules in polycrystalline ice given by Eq. (1). The difference between $D_{\text{tj}}$ and $D_{\text{gb}}$ is not so large, and $f_{\text{tj}}$ is much smaller than $f_{\text{gb}}$ unless the diameter of each grain is close to the thickness of the grain boundaries, $\delta_{\text{gb}}$. Therefore, the contribution from the triple junctions is omitted. We assume simply that the sizes of all grains are the same and a grain is a truncated octahedron, which is a space-filling polyhedron. Equation (1) is recast into

$$
D_{\text{pc}} = \left(1 - f_{\text{gb}}(b)\right)D_{\text{sc}} + f_{\text{gb}}(b)D_{\text{gb}} \tag{8}
$$

with

$$
f_{\text{gb}}(b) = \frac{(3 + 6\sqrt{3})}{8\sqrt{2}} \frac{\delta_{\text{gb}}}{b}, \tag{9}
$$

where $b$ is the edge length of the truncated octahedron. The ratio of $D_{\text{pc}}$ to $D_{\text{sc}}$ is plotted against $b$ in Fig. 11. The diffusion coefficient of

![](./images/812564023751999489_15.jpg)

FIG. 11. Diffusion coefficient of water molecules in polycrystalline ice, $D_{\text{pc}}$, calculated from Eqs. (8) and (9). We assume that a grain is a truncated octahedron with an edge length of $b$. The thickness and diffusion coefficient of the grain boundaries are $\delta_{\text{gb}} = 1$ nm and $D_{\text{gb}} = 5.0 \times 10^{-13}$ m$^2$ s$^{-1}$, respectively. The diffusion coefficient in single-crystal ice, $D_{\text{sc}} = 6.2 \times 10^{-16}$ m$^2$ s$^{-1}$, is taken from an experimental study.$^{70}$

single-crystal ice, $D_{\text{sc}} = 6.2 \times 10^{-16}$ m$^2$ s$^{-1}$, is taken from an experimental study.$^{70}$ The grain sizes in typical ice samples including polar ice cores are of the order of millimeters.$^{1,71,72}$ The contribution from the grain boundaries is negligible in such a sample. The impact of the grain boundaries becomes significant when $b$ is less than 1 $\mu$m. It is possible to prepare such an extremely fine-grained ice sample experimentally, but the average grain size in the sample increases rapidly as time evolves unless the temperature is low enough to inhibit the reorientation of water molecules.$^{72-74}$

## CONCLUSIONS

We have investigated the grain boundaries and triple junctions in ice using MD simulations. The structures of polycrystalline ice are generated by growing ice particles in a slab of supercooled water in contact with the vapor phase. This configuration allows examining the ice/vapor interfaces in addition to the grain boundaries. The 2D distribution functions of the twist order parameter calculated from the O-O-O-O dihedral angles show that the structure of the grain boundaries is LDL-like, whereas that of the ice/vapor interfaces is HDL-like. This is consistent with the observation that the density of the grain boundary region is lower than that of the quasi-liquid layer at the ice/vapor interfaces. The thickness of the grain boundary region is $\sim$1 nm. The diffusion coefficient of water molecules along the grain boundaries determined from the slope of the MSD is $D_{\text{gb}} = 5.0 \times 10^{-13}$ m$^2$ s$^{-1}$. This result is in good agreement with the experimental study of Lu *et al.*$^{12}$ The diffusion coefficient along the triple junctions is $D_{\text{tj}} = 1.7 \times 10^{-12}$ m$^2$ s$^{-1}$. The impact of the grain boundaries and the triple junctions on the whole diffusivity in polycrystalline ice is evaluated using the simulation results. Our model suggests that the diffusion through the grain boundaries is dominant only for extremely fine-grained samples. The contribution from the triple junctions is much smaller than that from the grain boundaries because of the quite small volume fraction of the triple junction region and the small difference between $D_{\text{tj}}$ and $D_{\text{gb}}$.

In this study, the MD simulations are performed only at a single temperature of 250 K. It has been suggested that diffusion through the triple junctions becomes significant at temperatures near the melting point of ice because of pre-melting.$^{3,8,75}$ The local structure there may be HDL-like. The thickness of the ice/vapor interface decreases with decreasing temperature.$^{65,76,77}$ The thickness of the grain boundaries may depend on the temperature as well. (The thickness of the grain boundaries is almost double the thickness of the ice/vapor interfaces at 250 K as shown in Fig. 6. This relationship might hold at other temperatures.) There might also be some characteristic temperatures at which the structure and dynamics of the grain boundaries and triple junctions change drastically likewise those found for the ice/vapor interface.$^{77-79}$ Further MD simulations are required to investigate the temperature dependence of the structural and dynamic properties of the grain boundaries and triple junctions in ice.

## SUPPLEMENTARY MATERIAL

See the supplementary material for the crystal growth process of the 4-grain system, the orientation of each grain, the 2D distribution functions of the twist parameter for the basal, primary prismatic, and secondary prismatic planes, and the cutoff RMSD value for the PTM algorithm.

## ACKNOWLEDGMENTS

The present work was supported by MEXT as "Priority Issue on Post-Kcomputer" (Development of new fundamental technologies for high-efficiency energy creation, conversion/storage and use) using computational resources of the K computer provided by the RIKEN Advanced Institute for Computational Science through the HPCI System Research (Project No. hp180204). The MD simulations were also performed on the computers at the Research Center for Computational Science, Okazaki, Japan.

## DATA AVAILABILITY

The data that support the findings of this study are available from the corresponding author upon reasonable request.

## REFERENCES

$^{1}$V. F. Petrenko and R. W. Whitworth, *Physics of Ice* (Oxford University Press, Oxford, 1999).

$^{2}$T. Bartels-Rausch, H.-W. Jacobi, T. F. Kahan, J. L. Thomas, E. S. Thomson, J. P. D. Abbatt, M. Ammann, J. R. Blackford, H. Bluhm, C. Boxe, F. Domine, M. M. Frey, I. Gladich, M. I. Guzmán, D. Heger, T. Huthwelker, P. Klán, W. F. Kuhs, M. H. Kuo, S. Maus, S. G. Moussa, V. F. McNeill, J. T. Newberg, J. B. C. Pettersson, M. Roeselová, and J. R. Sodeau, *Atmos. Chem. Phys.* 14, 1587 (2014).

$^{3}$J. G. Dash, A. W. Rempel, and J. S. Wettlaufer, *Rev. Mod. Phys.* 78, 695 (2006).

$^{4}$J. Jouzel, R. B. Alley, K. M. Cuffey, W. Dansgaard, P. Grootes, G. Hoffmann, S. J. Johnsen, R. D. Koster, D. Peel, C. A. Shuman, M. Stievenard, M. Stuiver, and J. White, *J. Geophys. Res.: Oceans* 102, 26471, https://doi.org/10.1029/97jc01283 (1997).

$^{5}$C. Buizert, M. Sigl, M. Severi, B. R. Markle, J. J. Wettstein, J. R. McConnell, J. B. Pedro, H. Sodemann, K. Goto-Azuma, K. Kawamura, S. Fujita, H. Motoyama, M. Hirabayashi, R. Uemura, B. Stenni, F. Parrenin, F. He, T. J. Fudge, and E. J. Steig, *Nature* 563, 681 (2018).

$^{6}$K. Goto-Azuma, M. Hirabayashi, H. Motoyama, T. Miyake, T. Kuramoto, R. Uemura, M. Igarashi, Y. lizuka, T. Sakurai, S. Horikawa, K. Suzuki, T. Suzuki, K. Fujita, Y. Kondo, S. Hattori, and Y. Fujii, *Nat. Commun.* 10, 3247 (2019).

$^{7}$J. Eichler, C. Weikusat, A. Wegner, B. Twarloh, M. Behrens, H. Fischer, M. Hörhold, D. Jansen, S. Kipfstuhl, U. Ruth, F. Wilhelms, and I. Weikusat, Front. Earth Sci. 7, 20 (2019).

$^{8}$A. W. Rempel, E. D. Waddington, J. S. Wettlaufer, and M. G. Worster, Nature 411, 568 (2001).

$^{9}$T. R. Jones, K. M. Cuffey, J. W. C. White, E. J. Steig, C. Buizert, B. R. Markle, J. M. McConnell, and M. Sigl, J. Geophys. Res.: Earth Surf. 122, 290, https://doi.org/10.1002/2016jf003938 (2017).

$^{10}$O. B. Nasello, C. L. Di Prinzio, and P. G. Guzmán, Acta Mater. 53, 4863 (2005).

$^{11}$L. G. Harrison, Trans. Faraday Soc. 57, 1191 (1961).

$^{12}$H. Lu, S. A. McCartney, and V. Sadtchenko, J. Chem. Phys. 130, 054501 (2009).

$^{13}$Y. R. Kolobov, G. P. Grabovetskaya, I. V. Ratochka, and K. V. Ivanov, Nanos- truct. Mater. 12, 1127 (1999).

$^{14}$A. Portavoce, L. Chow, and J. Bernardini, Appl. Phys. Lett. 96, 214102 (2010).

$^{15}$M. R. Chellali, Z. Balogh, H. Bouchikhaoui, R. Schlesiger, P. Stender, L. Zheng, and G. Schmitz, Nano Lett. 12, 3448 (2012).

$^{16}$M. Wegner, J. Leuthold, M. Peterlechner, X. Song, S. V. Divinski, and G. Wilde, J. Appl. Phys. 116, 093514 (2014).

$^{17}$C. L. Di Prinzio and R. G. Pereyra, Modell. Simul. Mater. Sci. Eng. 24, 045015 (2016).

$^{18}$P. A. F. P. Moreira, R. G. de Aguiar Veiga, I. de Almeida Ribeiro, R. Freitas, J. Helfferich, and M. de Koning, Phys. Chem. Chem. Phys. 20, 13944 (2018).

$^{19}$P. R. Cantwell, M. Tang, S. J. Dillon, J. Luo, G. S. Rohrer, and M. P. Harmer, Acta Mater. 62, 1 (2014).

$^{20}$O. Mishima, L. D. Calvert, and E. Whalley, Nature 314, 76 (1985).

$^{21}$P. G. Debenedetti, J. Phys.: Condens. Matter 15, R1669 (2003).

$^{22}$P. H. Poole, F. Sciortino, U. Essmann, and H. E. Stanley, Nature 360, 324 (1992).

$^{23}$O. Mishima and H. E. Stanley, Nature 396, 329 (1998).

$^{24}$S. Harrington, R. Zhang, P. H. Poole, F. Sciortino, and H. E. Stanley, Phys. Rev. Lett. 78, 2409 (1997).

$^{25}$M. Yamada, S. Mossa, H. E. Stanley, and F. Sciortino, Phys. Rev. Lett. 88, 195701 (2002).

$^{26}$Y. Liu, J. C. Palmer, A. Z. Panagiotopoulos, and P. G. Debenedetti, J. Chem. Phys. 137, 214505 (2012).

$^{27}$P. H. Poole, R. K. Bowles, I. Saika-Voivod, and F. Sciortino, J. Chem. Phys. 138, 034505 (2013).

$^{28}$T. Yagasaki, M. Matsumoto, and H. Tanaka, Phys. Rev. E 89, 020301 (2014).

$^{29}$T. Yagasaki, M. Matsumoto, and H. Tanaka, Phys. Rev. E 91, 016302 (2015).

$^{30}$T. Yagasaki, M. Matsumoto, and H. Tanaka, J. Chem. Phys. 150, 214506 (2019).

$^{31}$J. C. Palmer, F. Martelli, Y. Liu, R. Car, A. Z. Panagiotopoulos, and P. G. Debenedetti, Nature 510, 385 (2014).

$^{32}$J. C. Palmer, A. Haji-Akbari, R. S. Singh, F. Martelli, R. Car, A. Z. Panagiotopou- los, and P. G. Debenedetti, J. Chem. Phys. 148, 137101 (2018).

$^{33}$T. Frolov, D. L. Olmsted, M. Asta, and Y. Mishin, Nat. Commun. 4, 1899 (2013).

$^{34}$M. Matsumoto, T. Yagasaki, and H. Tanaka, J. Chem. Phys. 150, 214504 (2019).

$^{35}$B. Hess, C. Kutzner, D. van der Spoel, and E. Lindahl, J. Chem. Theory Comput. 4, 435 (2008).

$^{36}$D. Van der Spoel, E. Lindahl, B. Hess, G. Groenhof, A. E. Mark, and H. J. C. Berendsen, J. Comput. Chem. 26, 1701 (2005).

$^{37}$T. Darden, D. York, and L. Pedersen, J. Chem. Phys. 98, 10089 (1993).

$^{38}$U. Essmann, L. Perera, M. L. Berkowitz, T. Darden, H. Lee, and L. G. Pedersen, J. Chem. Phys. 103, 8577 (1995).

$^{39}$S. Nosé, Mol. Phys. 52, 255 (1984).

$^{40}$W. G. Hoover, Phys. Rev. A 31, 1695 (1985).

$^{41}$J. L. F. Abascal, E. Sanz, R. García Fernández, and C. Vega, J. Chem. Phys. 122, 234511 (2005).

$^{42}$R. García Fernández, J. L. F. Abascal, and C. Vega, J. Chem. Phys. 124, 144506 (2006).

$^{43}$T. Yagasaki, M. Matsumoto, and H. Tanaka, J. Phys. Chem. C 120, 3305 (2016).

$^{44}$M. Matsumoto, J. Chem. Phys. 126, 054503 (2007).

$^{45}$L. Xu, P. Kumar, S. V. Buldyrev, S.-H. Chen, P. H. Poole, F. Sciortino, and H. E. Stanley, Proc. Natl. Acad. Sci. U. S. A. 102, 16558 (2005).

$^{46}$J. L. F. Abascal and C. Vega, J. Chem. Phys. 133, 234502 (2010).

$^{47}$S. Saito, B. Bagchi, and I. Ohmine, J. Chem. Phys. 149, 124504 (2018).

$^{48}$M. Matsumoto, T. Yagasaki, and H. Tanaka, J. Comput. Chem. 39, 61 (2018).

$^{49}$T. Hondoh and A. Higashi, Philos. Mag. A 39, 137 (1979).

$^{50}$H. Chan, M. J. Cherukara, B. Narayanan, T. D. Loeffler, C. Benmore, S. K. Gray, and S. K. R. S. Sankaranarayanan, Nat. Commun. 10, 379 (2019).

$^{51}$E. B. Moore and V. Molinero, J. Chem. Phys. 130, 244505 (2009).

$^{52}$E. B. Moore and V. Molinero, Phys. Chem. Chem. Phys. 13, 20008 (2011).

$^{53}$A. Haji-Akbari and P. G. Debenedetti, Proc. Natl. Acad. Sci. U. S. A. 112, 10582 (2015).

$^{54}$T. L. Malkin, B. J. Murray, C. G. Salzmann, V. Molinero, S. J. Pickering, and T. F. Whale, Phys. Chem. Chem. Phys. 17, 60 (2015).

$^{55}$L. Lupi, A. Hudait, B. Peters, M. Grünwald, R. Gotchy Mullen, A. H. Nguyen, and V. Molinero, Nature 551, 218 (2017).

$^{56}$P. J. Steinhardt, D. R. Nelson, and M. Ronchetti, Phys. Rev. B 28, 784 (1983).

$^{57}$L. A. Báez and P. Clancy, Ann. N. Y. Acad. Sci. 715, 177 (1994).

$^{58}$J. R. Errington and P. G. Debenedetti, Nature 409, 318 (2001).

$^{59}$M. Matsumoto, A. Baba, and I. Ohmine, J. Chem. Phys. 127, 134504 (2007).

$^{60}$J. Vatamanu and P. G. Kusalik, J. Chem. Phys. 126, 124703 (2007).

$^{61}$A. H. Nguyen and V. Molinero, J. Phys. Chem. B 119, 9369 (2015).

$^{62}$P. M. Larsen, S. Schmidt, and J. Schiøtz, Modell. Simul. Mater. Sci. Eng. 24, 055007 (2016).

$^{63}$T. Yagasaki, M. Matsumoto, and H. Tanaka, J. Phys. Chem. B 122, 3396 (2018).

$^{64}$M. Fulford, M. Salvalaglio, and C. Molteni, J. Chem. Inf. Model. 59, 2141 (2019).

$^{65}$P. Llombart, R. M. Bergua, E. G. Noya, and L. G. MacDowell, Phys. Chem. Chem. Phys. 21, 19594 (2019).

$^{66}$A. Stukowski, Modell. Simul. Mater. Sci. Eng. 18, 015012 (2009).

$^{67}$R. Metzler, J.-H. Jeon, A. G. Cherstvy, and E. Barkai, Phys. Chem. Chem. Phys. 16, 24128 (2014).

$^{68}$P. Liu, E. Harder, and B. J. Berne, J. Phys. Chem. B 108, 6595 (2004).

$^{69}$M. Sega, R. Vallauri, and S. Melchionna, Phys. Rev. E 72, 041201 (2005).

$^{70}$K. Goto, T. Hondoh, and A. Higashi, Jpn. J. Appl. Phys., Part 1 25, 351 (1986).

$^{71}$T. Thorsteinsson, J. Kipfstuhl, and H. Miller, J. Geophys. Res.: Oceans 102, 26583, https://doi.org/10.1029/97jc00161 (1997).

$^{72}$D. L. Goldsby and D. L. Kohlstedt, Scr. Mater. 37, 1399 (1997).

$^{73}$H. Lu, S. A. McCartney, and V. Sadtchenko, J. Chem. Phys. 127, 184701 (2007).

$^{74}$L. Arena, O. B. Nasello, and L. Levi, J. Phys. Chem. B 101, 6109 (1997).

$^{75}$H. M. Mader, J. Glaciol. 38, 359 (1992).

$^{76}$M. M. Conde, C. Vega, and A. Patrykiejew, J. Chem. Phys. 129, 014702 (2008).

$^{77}$P. Llombart, E. G. Noya, D. N. Sibley, A. J. Archer, and L. G. MacDowell, Phys. Rev. Lett. 124, 065702 (2020).

$^{78}$P. Llombart, E. G. Noya, and L. G. MacDowell, Sci. Adv. 6, eaay9322 (2020).

$^{79}$T. Kling, F. Kling, and D. Donadio, J. Phys. Chem. C 122, 24780 (2018).

---

J. Chem. Phys. 153, 124502 (2020); doi: 10.1063/5.0021635

Published under license by AIP Publishing

153, 124502-9