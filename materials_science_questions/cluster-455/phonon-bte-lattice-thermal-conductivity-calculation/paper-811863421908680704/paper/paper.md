# Thermal Transport in Off-Stoichiometric Uranium Dioxide by Atomic Level Simulation

Taku Watanabe, $^{\ddagger,\sharp}$ Srinivasan G. Srivilliputhur, $^{\S,\Uparrow}$ Patrick K. Schelling, $^{\|}$ James S. Tulenko, $^{\dagger \dagger}$ Susan B. Sinnott, $^{\ddagger}$ and Simon R. Phillpot $^{\ddagger,\sharp}$

$^{\ddagger}$Department of Materials Science and Engineering, University of Florida, Gainesville, Florida 32611
$^{\S}$Los Alamos National Laboratory, Materials Science and Technology Division, Los Alamos, New Mexico 87545
$^{\Uparrow}$Department of Materials Science and Engineering, University of North Texas, Denton Texas 76203
$^{\|}$AMPAC and Department of Physics, University of Central Florida, Orlando, Florida 32816
$^{\dagger \dagger}$Department of Nuclear and Radiological Engineering, University of Florida, Gainesville, Florida 32611

The thermal conductivity of hypo- and hyperstoichiometric $\text{UO}_2$ is calculated as a function of defect concentration and temperature using the direct method in molecular dynamics simulations. Anion defects, the dominant defects in $\text{UO}_2$, are shown to significantly influence the thermal conductivity. Lattice dynamics calculations show how this reduction arises from changes in the nature of the lattice vibrations, as characterized by the polarization vectors and participation ratios. In addition, $^{235}\text{U}$ isotopic defects are shown to have a negligible influence on the thermal conductivity.

## I. Introduction

Uranium dioxide is the standard nuclear reactor fuel material. The fission reactions in the fuel generate heat, which is transported from the fuel through the cladding into the coolant. This heat passes through heat exchangers and is ultimately used to generate electricity. Thus the thermal transport properties of the fuel are a key performance metric. At most temperatures $\text{UO}_2$ is an electronic insulator; its thermal transport can thus be described by the dynamics of lattice vibrations (phonons). The point defects in $\text{UO}_2$ should have a significant influence on the thermal transport properties. In this article, the thermal transport properties of off-stoichiometric $\text{UO}_2$ are characterized by simulation, and the results analyzed in terms of the theory of thermal transport in crystalline and amorphous disordered solids. The effects of isotopic defects are also briefly analyzed.

## II. Background

We analyze the thermal transport properties in terms of the conductivity of crystalline and amorphous materials. Thermal transport in a defect-free crystalline solid can be thought of in terms of a gas of phonons interacting through random collisions, with an average spatial separation given by the mean free path, $\lambda$. If the mean sound velocity and specific heat of a solid are $v$ and $c_v$, then the thermal conductivity is given by kinetic theory as: $^{1,2}$

$$
\kappa = \frac{1}{3} c_v v \lambda \tag{1}
$$

For crystals, $c_v$ increases as $T^3$ at low temperatures according to Debye theory, and levels off to the Dulong-Petit value of $3k_\text{B}$ per atom ($k_\text{B}$ is the Boltzmann constant) above the Debye temperature. $^{1,2}$ The velocity of sound is essentially temperature independent. The mean-free path in a coarse-grained crystalline solid is usually determined by anharmonic phonon-phonon interactions, which increase as the temperature increases. In most cases, the mean-free path depends on temperature as $\lambda \sim T^{-\alpha}$ where $\alpha$ is typically between 1 and 2. $^{1}$

The thermal-transport properties of amorphous solids are quite different from those of crystalline solids. In the case of amorphous Si, the behavior of $\kappa$ can be divided into three regions. $^{3}$ Below 10 K, the $\kappa$ is approximately proportional $T^2$ and the two level system scattering model can provide a reasonable fit. Then there is a small shoulder between 10 and 30 K. Above 30 K, $\kappa$ rises smoothly to its saturation. Many disordered crystals show similar behavior. $^{4,5}$ Allen *et al.*$^{6}$ analyzed thermal transport in amorphous solids in terms of the vibrational modes, which are classified as propagons, diffusions, or locons according to their diffusivities, wave vectors, and polarizations. Propagons are propagating, phonon-like excitations with well-defined wave vectors and polarizations; diffusions are extended modes that move in a diffusive rather than a ballistic manner; locons are spatially local states.

One of the earliest experimental studies on the effect of stoichiometry on thermal transport of $\text{UO}_{2+x}$ was undertaken by Hobson *et al.*$^{7}$ In general, the thermal conductivities of all the samples showed monotonic decreases with increasing temperature, but there was an abrupt change in the slope around 700 K for $x=0.060$. This change was later ascribed to the formation of the $\text{U}_4\text{O}_9$ phases in the sample. $^{8}$ Lewis and collaborators undertook both experimental and numerical studies on the oxidation behavior of $\text{UO}_2$ in a fuel rod, and on the effect of oxidation on the thermal conductivity of the fuel. Their experimental data was used to validate their phenomenological model for the oxidation kinetics of the fuel rod. Based on the model, they showed that $\kappa$ depends significantly on the value of $x$ within the range of $0 \leq x \leq 0.2$ for temperatures below 2000 K.

There has been one previous simulation study of the thermophysical properties of off-stoichiometric $\text{UO}_2$. Yamasaki *et al.*$^{9}$ described the interatomic interactions using a nonformal charge, rigid-ion type interatomic potential. The parameters of the potential were fitted to the composition-dependent thermal expansion, based on the experimental values of Gr$\o$nvold, $^{10}$ and to other physical properties. The Green-Kubo (GK) method was then used to calculate the thermal conductivity by an equilibrium MD simulation. The calculated thermal expansion and thermal conductivity values were in good agreement with experimental values, showing a decrease of conductivity with increasing concentration of defects. $^{11,8}$ The work presented here

---

D. J. Green—contributing editor

Manuscript No. 25289. Received November 2, 2008; approved December 23, 2008.
$^{\ddagger}$Author to whom correspondence should be addressed. e-mail: sphil@mse.ufl.edu
$^{\sharp}$Current Address: School of Chemical and Biomolecular Engineering, Georgia Institute of Technology, Atlanta GA 30332


goes beyond that of Yamasaki *et al.* in a number of ways: first, we include hypostoichiometric compositions and also go to considerably higher hyperstoichiometries. Second, we analyze the thermal-transport results in the context of the theory of heat transport in crystalline and amorphous materials; third, we assess the effects of isotopic defects. At the technical level, we use both a different description of the interatomic interactions and a different simulation approach to the thermal conductivity calculations themselves.

## III. MD Simulation Approach

In the following, we describe the approach taken to perform the thermal conductivity simulations of off-stoichiometric using MD simulations. While the composition is usually written as $\text{UO}_{2\pm x}$, since both hypo- and hyperstoichiometric compositions are considered, here the system is denoted $\text{UO}_{2+x}$, where $x$ can take both negative and positive values. The range of off-stoichiometry investigated was $x=-0.02$ to $+0.25$. This range was chosen based on the known phase behavior of the U–O system between 800 and $1600\ \text{K}.^{12}$ This extends to higher values of $x$ than previously studied in any experiment or simulation. The composition $x=0.25$ corresponding to the $\text{U}_4\text{O}_9$ composition, which marks the upper limit of stability of the fluorite-structured $\text{UO}_{2+x}$ phase.

To include oxygen vacancies and interstitials, the potential must be able to describe uranium in its 3+, 4+, and 5+ charge states; the potential parameters for the Buckingham potential used in this study are given in Table I. These parameters are taken from the work of Busker *et al.*$^{13,14}$ There are a number of uranium dioxide potentials for a variety of applications; a critical assessment of these potentials has been carried out by Govers *et al.*$^{15}$ The Busker$^{14}$ potential was designed to provide a set of self-consistent parameters for several oxides and to allow investigation of off-stoichiometric systems. Note that there is no short range interaction between the cations.

Hyperstoichiometric compositions ($x>0$) are prepared from the initially defect free $\text{UO}_2$ structure by adding excess oxygen atoms corresponding to the desired composition at random octahedral (4b) interstitial sites. To maintain overall charge neutrality, randomly selected $\text{U}^{4+}$ ions are replaced with $\text{U}^{5+}$ ions. The resulting structure is heated to 3000 K for 10 ps allowing oxygen diffusion to take place, thereby bringing the structure into equilibrium. The system is slowly cooled to 0 K and quenched by a steepest descents algorithm to yield a minimum energy configuration. In a similar manner, for hypostoichiometric ($x<0$) structures, oxygen ions are removed and randomly selected $\text{U}^{4+}$ ions replaced with $\text{U}^{3+}$ ions to preserve charge neutrality.

The resulting structures were characterized through the pair distribution function (PDF). Figures 1(a) and (b) show the U–O PDFs for $\text{UO}_{2.125}$ and $\text{UO}_{1.98}$, respectively. The peaks corresponding to $\text{U}^{5+}$–$\text{O}^{2-}$ are shifted to shorter distances by $0.24\ \text{\AA}$ relative to those of $\text{U}^{4+}$–$\text{O}^{2-}$, as is expected from the larger electrostatic attraction and smaller ionic radius of $\text{U}^{5+}$ compared with that of $\text{U}^{4+}$. From the PDF analysis of $\text{UO}_{2.125}$, it is found that each $\text{U}^{5+}$ is surrounded by an average of 9.05 oxygen ions within a of $3.6\ \text{\AA}$, which is the half way between the distance to the nearest interstitial site and second nearest oxygen ion site in the fluorite structure. Within the same radius, $\text{U}^{4+}$ has 8.85 oxygen ion neighbors. Thus, as is expected on electrostatic grounds, there is a slight tendency for the O ions to cluster around the $\text{U}^{5+}$ ions. Even at the low concentration of $x=0.020$, the same trend is observed: 8.32 oxygen ion neighbors for $\text{U}^{5+}$ and 8.12 for $\text{U}^{4+}$. In $\text{UO}_{1.98}$, due to their lower charge and large radius, the $\text{U}^{3+}$–$\text{O}^{2-}$ peaks are shifted to longer distances relative to the $\text{U}^{4+}$–$\text{O}^{2-}$. However here, there is no significant oxygen segregation: each $\text{U}^{3+}$ is surrounded by $7.91\ \text{O}^{2-}$, while each $\text{U}^{4+}$ has $7.92\ \text{O}^{2-}$ neighbors.

<table>
<caption>Table I. Potential Parameters for the Short-Range Interactions in $\text{UO}_{2\pm x}$. Uranium Ions Interact with Each Other Only Through the Electrostatic Interactions$^{13,14}$</caption>
<thead>
<tr>
<th></th>
<th>$\text{O}^{2-}$–$\text{O}^{2-}$</th>
<th>$\text{U}^{4+}$–$\text{O}^{2-}$</th>
<th>$\text{U}^{5+}$–$\text{O}^{2-}$</th>
<th>$\text{U}^{3+}$–$\text{O}^{2-}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$A_{ij}$ (eV)</td>
<td>9547.96</td>
<td>1761.775</td>
<td>2386.42</td>
<td>1165.65</td>
</tr>
<tr>
<td>$\rho_{ij}$ (Å)</td>
<td>0.2192</td>
<td>0.35643</td>
<td>0.3411</td>
<td>0.3786</td>
</tr>
<tr>
<td>$C_{ij}$ ($\text{eV}\cdot\text{\AA}^6$)</td>
<td>32</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
</tbody>
</table>

![](./images/811863421908680704_1.jpg)

Fig. 1. Pair distribution function between U–O in (a) $\text{UO}_{2.125}$ and (b) $\text{UO}_{1.98}$. The structures were annealed at 3000 K and cooled down to 0 K before the analysis.

We use the direct method to determine thermal conductivity.$^{16,17}$ In this approach a heat current is set up and the resulting temperature gradient $\text{d}T/\text{d}x$, is determined. The thermal conductivity is then calculated from Fourier's law, $J=-\kappa\text{d}T/\text{d}x$, where $J$ is the heat current and $\kappa$ the thermal conductivity tensor.

Since the thermal resistance of a defect-free system comes from phonon–phonon scattering, it is sensitive to the degree of anharmonicity of the potential energy surface. This anharmonicity is also the origin of the thermal expansion of the material, which would be zero for a completely harmonic material. As we have discussed elsewhere, good agreement between the calculated and experimental values for the thermal conductivity is obtained when the calculated values are renormalized according to the differences in the anharmonicty.$^{18}$ For the Busker $\text{UO}_2$ potential, this factor turns out to be 3.0. We apply this renormalization to the calculated values here also.

Another important factor to consider is that thermal conductivity determined by simulation depends on the size of the sample. As described in detail elsewhere,$^{17,18}$ the thermal conductivity in MD simulations can be written as a function of simulation cell length as:

$$
\frac{1}{\kappa}=\frac{2a^3}{k_BN_Cv_S}\left(\frac{1}{\lambda_\infty}+\frac{4}{L_z}\right) \tag{2}
$$

where $a$ is the lattice parameter, $k_B$ is the Boltzmann constant, $N_C$ is the number of atoms in the unit cell, $v_s$ is the mean velocity of sound, $\lambda_\infty$ is the phonon mean free path, and $L_z$ is the length of the simulation cell. Thus, the infinite size bulk thermal conductivity can be obtained from MD simulations by the extrapolation of the conductivity values to the $1/L_z=0$ limit.

## IV. Thermal Properties of $\text{UO}_{2+x}$

### (1) Chemical and Thermal Expansions

Before investigating the thermal expansion, it is necessary to analyze the change in lattice parameter due to the off-stoichiometry alone. Figure 2 shows that the lattice parameter of $\text{UO}_{2+x}$ at 0 K decreases with increasing concentration of oxygen interstitials. For $x<0$, the reduced strength of the Coulombic interactions arising from the replacement of $\text{U}^{4+}$ ions by $\text{U}^{3+}$ ions, the larger size of the $\text{U}^{3+}$ ions, and the presence of vacancies tend to lead to lattice expansion. As a result the lattice parameter depends strongly on composition: a 0.25% expansion of the lattice for $x=-0.02$ (Fig. 2). For $x=+0.02$ the change in the lattice parameter is much smaller. Indeed, even at the highest

![](./images/811863421908680704_2.jpg)

Fig. 2. Normalized lattice parameter of $\mathrm{UO}_{2+x}$ ($x=-0.02$–0.25) at 0 K after the high temperature annealing. $a(0)$ is the lattice parameter of $\mathrm{UO}_{2.000}$.

defect concentration ($x=0.250$), the lattice parameter is only $\sim 0.5\%$ smaller than the lattice parameter of stoichiometric $\mathrm{UO}_{2}$. This smaller contraction is the result of a partial cancel- lation of the effects that were additive for the hypostoichiomet- ric compositions: the increased electrostatic attractions arising from the $\mathrm{U}^{5+}$ ions and from the extra $\mathrm{O}^{2-}$ in the octahedral sites tend to lead to a contraction of the lattice, as does the smaller ionic radius of the $\mathrm{U}^{5+}$ relative to the $\mathrm{U}^{4+}$. These are partially counteracted by the lattice strain introduced by the oxygen in- terstitials tends to increase the lattice parameter. The electro- static interactions dominate, resulting in an overall small lattice contraction.

In 1955 Grønvold$^{10}$ performed X-ray studies to determine the lattice expansion of $\mathrm{UO}_{2+x}$. His data showed no indication of any lattice expansion over the range of $x=0.0$–0.2. Surprisingly, despite the complexities of the phase diagram of $\mathrm{UO}_{2+x}$, $^{12}$ there have been no subsequent systematic studies. There is no exper- imental data on the chemical expansion of $\mathrm{UO}_{2-x}$.

Figure 3 shows the temperature dependence of the lattice pa- rameter of $\mathrm{UO}_{2+x}$ obtained from the MD simulations. The differences at $T=0$ K arise from the chemical expansion dis- cussed above. The lattice parameter is an almost linear function of temperature for all the concentrations of defects studied. The thermal expansion coefficient, $\alpha$, determined from the slope of the curves, decreases from $6.8 \times 10^{-6}$ to $5.4 \times 10^{-6}\ \mathrm{K}^{-1}$ as the defect concentration increases, as shown in Fig. 4. Yamasaki's data show a thermal expansion of $11.4 \times 10^{-6}\ \mathrm{K}^{-1}$ for the narrow

![](./images/811863421908680704_3.jpg)

Fig. 3. Thermal expansion of $\mathrm{UO}_{2+x}$ from MD simulations and experiment. The dotted line is the data from Yamasaki *et al.*'s simulations, $^{9}$ and the solid lines are the experimental data by Grønvold. $^{10,20}$ Our data are shown by the filled symbols. All data indicates that increasing the defect concentration reduces the lattice parameter.

![](./images/811863421908680704_4.jpg)

Fig. 4. Thermal expansion coefficient of $\mathrm{UO}_{2+x}$ as a function of $x$.

range of defect concentrations studied $(0.00 \leq x \leq 0.09)$ which agrees better with experimental data by Fink. $^{19}$ This is not sur- prising because the Yamasaki potential was specifically fitted to the thermal expansion, whereas the potential used here was not. Again, there have been no systematic experimental studies of the effect of defect concentration on $\alpha$ since the work of Grønvold, which showed no significant effect of composition on thermal expansion.

### (2) Thermal Conductivity of $\mathrm{UO}_{2+x}$
$\mathrm{UO}_{2+x}$ structures of $21.9\ \mathring{\mathrm{A}} \times 21.9\ \mathring{\mathrm{A}}$ ($4 \times 4$ unit cells) cross sec- tions were prepared using the technique described in Section III. Because the effect of the simulation cell length is important and must be investigated to obtain the infinite size bulk thermal conductivity, simulation cell lengths of 48, 64, 80, sand 96 unit cells (262.5, 350.0, 437.4, and $524.9\ \mathring{\mathrm{A}}$ at 0 K) were used.

The simulations were performed at 800 and 1600 K, which correspond to the surface and centerline temperatures of a fuel pellet in a typical PWR. It is known that at high temperatures, the electronic contribution to the thermal conductivity from po- laron hopping, becomes important. Ronchi *et al.*$^{21}$ estimated the polaron contribution to the thermal conductivity of $\mathrm{UO}_{2}$ based on their experimental data as approximately $7\%$ of the materials overall thermal conductivity at 1800 K. Using their model, the polaron contribution at 1600 K can be estimated to be $\sim 3\%$ and to decrease rapidly as the temperature drops. Thus for the temperatures of interest, the polaronic effects can be safely neglected.

A small section of the simulated system is heated at constant rate, and another section is cooled at the same rate to conserve the total energy of the system. The thermal conductivity ob- tained with this method depends on the distance between the hot and cold regions. The size dependence based on Eq. (2) is an- alyzed in Fig. 5 for the case of 800 K. When plotted on $1/\kappa$ versus $1/L$ axes, the data points fit a straight line quite well for

![](./images/811863421908680704_5.jpg)

Fig. 5. Thermal resistivity of $\mathrm{UO}_{2+x}$ with various concentrations of oxygen interstitials as a function of simulation cell length $L_{z}$ at 800 K.

most defect concentrations. The intercept in the infinite size limit corresponds to our best estimate of the thermal conductivity of the materials. Because the quality of fit was not quite as good for the 1600 K case, the resulting statistical error in the infinite-size limit values are somewhat larger.

Our best estimates of the concentration dependence of the thermal conductivity at 800 K and 1600 K, based on these ex- trapolations are shown in Fig. 6. Both temperatures show monotonic decreases of the conductivity with increasing con- centration of oxygen interstitials. Interestingly, the two curves converge to essentially the same value of the conductivity of $\sim 1.7$ W/mK above $x=0.125$. As discussed below, this is ex pected for an amorphous system, in which the thermal conduc- tivity becomes both concentration and temperature independent for high defect concentrations.

The 800 K simulation data matches the experimental values at $x=0$, but yields a somewhat sharper decrease in thermal conductivity with increasing off-stoichiometry. The 1600K sim- ulation data match the corresponding experimental data well.

We have analyzed the effect of the nature of the off-stoic- hiometry (hypo- versus hyperstoichiometric) for low defect con- centrations. Figure 7 shows the thermal conductivity for $UO_{1.98}-UO_{2.02}$ at 800 and 1600 K. For this low concentration regime, the thermal conductivity depends approximately linearly on the defect concentration as we would expect for scattering from isolated point defect. $^{22}$ Moreover, the effects of vacancies and interstitials seem to be rather similar: the absolute valuesof the slopes differ by $<20 \%$ (122 W/m $\cdot$ K for $x>0$ versus 141W/m $\cdot$ K for $x<0$ at 800 K and 53 W/m $\cdot$ K for $x>0$ versus 64W/m $\cdot$ K for $x<0$ at 1600 K).

Finally, we have evaluated the effect of the presence of ura- nium isotopic defects on the thermal conductivity. $UO_{2}$ in a typical LWR is isotopically enriched to increase the fissile $^{235}U$, with the concentration depending on the specifications of the reactor, but typically in the range of $3-4$ wt $\%.^{23}$ In the MD simulations, $^{235}U$ was introduced into $^{238}UO_{2.00}$ as a simple mass defect at a concentration of 5 at.%. The thermal conduc-tivity obtained from the simulation at 300 K was $10.8 \pm 2.6$ W/m $\cdot$ K, which is within the error bar of the value of $11.0 \pm 2.8$  $W/m \cdot K$ the isotopically pure $UO_{2.00}$ . Thus, there is no signifi cant isotopic effect on the thermal conductivity for relevant concentrations.

The results obtained by Yamasaki et al. using the GK method $^{9}$ and our results obtained using the direct method agree well with each other and, where available, with experimental results. At $x=0$ at 1600 K, all three data sets show a thermalconductivity of $\sim 3$ W/mK, with agreement within $\sim 0.2$  W/mK. Yamasaki's data and our simulation data are consis- tent with the Lucuta's data at 800 K and 900 K respectively within 0.1 W/mK. Thus taken as a whole, the experimental re- sults and the results of the two simulations can be taken as a fairly complete and reliable dataset for the thermal transport properties of off-stoichiometric $UO_{2}$.

![](./images/811863421908680704_6.jpg)

Fig. 6. Thermal conductivity of $UO_{2+x}$ as a function of degree of off stoichiometry at 800 and 1600 K derived from simulation compared withexperimental values by Lucuta et al. $^{20}$

![](./images/811863421908680704_7.jpg)

Fig. 7. Bulk thermal conductivity of $UO_{2 \pm x}$ as a function of degree of off-stoichiometry at 800 and 1600 K.

In the following section, we analyze these thermal-transport results in the context of the theories of the conductivity of crys- talline and amorphous materials.

## V. Analysis of the Thermal Conductivity

The vibrational excitations of a solid, responsible for the ther-mal transport, can be analyzed using lattice dynamics (LD). $^{1,24}$  LD solves the equation of motion in the form of an eigenvalueproblem:

$$
\omega_{\lambda}^{2}(\vec{k}) e_{\lambda, \alpha i}(\vec{k})=D_{\alpha \beta}(\vec{k}) e_{\lambda, \beta i}(\vec{k}) \tag{3}
$$

where $\omega_{\lambda}^{2}(\vec{k})$ and $e_{\lambda, \alpha i}(\vec{k})$ are the eigenvalues and eigenvectors of mode $\lambda$, with wave vector $k$ in the $\alpha$ Cartesian direction at the atom $i$. $D_{\alpha \beta}(\vec{k})$, the so-called dynamical matrix, is a second rank tensor. The solution of Eq. (3) is given in the form of planewaves:

$$
u_{\lambda, \alpha}(j l, \vec{k})=e_{\lambda, \alpha} \exp \left[-i\left(\vec{k} \cdot \vec{r}_{j l}-\omega_{\lambda} t\right)\right] \tag{4}
$$

Here $u_{\lambda, \alpha}(j l, \vec{k})$ is the displacement vector of atom $(j, l)$ at time $t$, and $\vec{r}_{j l}$ is the equilibrium position of atom $(j, l)$. The calcula tions of the eigenvalues (i.e., vibrational frequencies) and eigen- vectors were carried out on $6 \times 6 \times 6$ unit cells of $UO_{2 \pm x}$ for $k=0$ modes. Because the system is disordered when point de fects are present, and the periodicity of the simulation cell is somewhat artificial, it is appropriate to focus only on the modes with $k=0$. For the $6 \times 6 \times 6$ unit cell, the $k=0$ calculation does not correspond to only the zone-center modes of the prim- itive unit cell; thus it actually samples the Brillouin zone quite extensively.

As the first step in characterizing the structures, the vibratio- nal densities of states (DOS), $g(\omega)$ , of $UO_{1.98}-UO_{2.25}$ are shown in Figs. 8(a)-(d). In the defect-free structure, Fig. 8(b) shows that the vibrational frequencies yield sharp peaks over the entirefrequency range. Moreover, the Debye-like behavior, $g(\omega) \sim \omega^{2}$  extends up to $\sim 4$ THz. The absence of modes below $\sim 1$ THz is due to the finite size of the simulation cell used for the DOS calculations. As the defect concentration is increased, both in the hyper- and hypostoichiometric directions, the DOS smears outand the minor peaks disappear. However, as shown in Figs. 8(a) and (c), there is no significant change in the DOS over the com- position range, $-0.020 \leq x \leq 0.020$ . This suggests that the con centrations of defects are low enough that the dynamics of the vibrational modes in $UO_{2}$ are largely unaffected. By contrast,

![](./images/811863421908680704_8.jpg)

Fig. 8. Density of states of $UO_{2\pm x}$ (a) $x=-0.020$, (b) $x=0.000$, (c) $x=0.020$, and (d) $x=0.125$. System size is $6\times6\times6$ unit cells. The frequency bin size is 0.2 THz.

Fig. 8(d) shows that the DOS for $x=0.125$ is different from that at lower defect concentrations in that density of states is nearly linear at low frequencies and the large featureless region of DOS is largely featureless region of from 7 to 22 THz.

This DOS is rather similar to those previously seen in amorphous $Si^{2}$ and in zirconia heavily doped with yttria. $^{25}$ In both cases it was useful to follow the approach of Allen et al. $^{6}$ by classifying the vibrational modes into three distinct types: (i) propagons, which are similar to phonons in that they have well-defined polarizations and wave-vectors, (ii) diffusons, which do not have well-defined wave-vectors but do involve the vibration of a large number of atoms, and (iii) locons, which are spatially localized over a relatively small fraction of the total atoms in the system. $^{6}$ While propagons are efficient transporters of heat, diffusons are much less efficient; locons hardly transport heat at all.

The degree of localization of each mode is quantified by the participation ratio, $p_{\lambda}$:

$$
p_{\lambda}^{-1}=N \sum_{i}\left(\sum_{\alpha} e_{\lambda, i \alpha}^{*} e_{\lambda, i \alpha}\right)^{2} \tag{5}
$$

In an ideal crystalline structure, $p_{\lambda}$ is of order of unity for all modes. In practice, for a large unit cell the eigenvectors at $k=0$ correspond to standing rather than traveling waves. $^{26}$ For standing waves, there are peaks and troughs and as a result many modes have $p \sim 1 / 2$ even though the mode is completely delocalized and periodic. In a defected or amorphous structure, localized modes (i.e., locons) may occur, characterized by small values of $p_{\lambda}$, a few times $1/N$, corresponding to the participation of only a few ions in the vibrational mode.

Figure 9 shows the participation ratios for each of the modes in the $6\times6\times6$ simulation cells of $UO_{2\pm x}$. The participation ratios for the defect-free $UO_{2}$ in Fig. 9(b) show significant scatter around 0.5, which is a characteristic of crystalline solids with the modes taken to be standing waves. Once the defects are introduced, $p_{\lambda}$ displays a much narrower range of distribution, Figs. 9(a) and (c) for $x=-0.02$ and $x=+0.02$. For the highest defect concentration, $x=+0.125$, the participation ratio is between 0.4 and 0.5 for frequencies between 7 and 22 THz. This is the same frequency range for which we saw the DOS to be largely featureless. While all three off-stoichiometric compositions show high-frequency phonons with low participation ratios, characteristic of locons, this is especially true for $x=0.125$.

We can further differentiate the different types of modes by examining the polarization of a typical vibrational mode. Figure 10 compares of the polarization vectors at 1.5 THz in $UO_{2+x}$ for $-0.020\leq x\leq0.125$. This frequency is near the low end of the frequency range which is expected to be dominated by the propagon modes. The horizontal and vertical axes are both $\langle 001\rangle$ directions. Since the polarization vector is normalized, data points are plotted on the circle of unit radius. We might expect to see a unique polarization in the defect-free crystal, which would be manifested as a few isolated points in the polarization plot. However, for many frequencies we actually find that for the defect-free crystal ($x=0$) there is some scatter in the polarization plots for the defect-free crystal ($x=0$). This arises from the substantial degeneracy for almost all the modes in the perfect crystal. Because any normalized linear combination of degenerate modes is also a normal mode, the polarization vector of most modes in the perfect crystal is not uniquely defined. The sole exception to this occurs at the $\Gamma$-point for the nondegenerate longitudinal optical branches which, as expected, show only a few points in the polarization plot. For the typical propagon mode shown in Fig. 10, for $x=0$ the concentration of points at the two poles of the figure are characteristic of a polarized mode. For low concentrations of defects ($-0.020\leq x\leq0.020$), the polarization plot shows more scatter, yet still retains an obvious polarization characterized by the remaining concentration of

![](./images/811863421908680704_9.jpg)

Fig. 9. Participation ratios of $UO_{2\pm x}$ (a) $x=-0.020$, (b) $x=0.000$, (c) $x=0.020$, and (d) $x=0.125$. System size is $6\times6\times6$ unit cells. The frequency bin size is 0.2 THz.

![](./images/811863421908680704_10.jpg)

Fig. 10. Polarization plot of vibrational modes in $UO_{2+x}$ near 1.5 THz.

points at the poles. By contrast, at $x=0.125$ the plot is rather uniform and the mode shows no obvious polarization. This behavior is more characteristic of a diffuson, indicating that for $x \geq 0.125$, transport occurs for modes near 1.5 THz via a diffusive mechanism with a characteristic length comparable to the lattice parameter. Interestingly, for $x=0.125$, the average separation between oxygen interstitials is $2^{1 / 3} a_{0}$.

For modes with frequency above 5 THz, the polarization plots of $\mathrm{UO}_{2+x}$ are homogeneous and show no obvious polarization except for $x=0$. This is characteristic of diffuson or locon behavior.

Taken together, these data provide a consistent view of the thermal-transport behavior. Three observations point to the concentration regime $|x| \leq 0.020$ being dominated by phonon like modes (propagons), with the thermal conductivity being still largely determined by phonon-phonon scattering. First, the approximately linear dependence of the thermal conductivity on concentration for $|x| \leq 0.020$ is consistent with the Klemens-Callaway theory of phonon-defect scattering in crystalline materials. $^{3,27} \mathrm{~S}$, the ratios of the thermal conductivity values at 800 and $1600 \mathrm{~K}$ for $|x| \leq 0.020$ are approximately 2.2, which is consistent with the $\sim 1 / T$ dependence of $k$ for a crystalline material. Third, the analysis of the vibrational modes shows the presence of propagons modes at lower frequencies. These modes carry most of the heat. There are higher frequency diffuson modes, which carry heat only inefficiently and a few locon modes at the highest frequencies, which do not carry heat at all.

The behavior at higher off-stoichiometries is completely different and is best understood in terms of the thermal transport properties of amorphous and highly disordered materials. First, the temperature independence of the thermal conductivity for high-defect concentrations is similar to that in amorphous materials in which the mean-free path of the diffusons is on the atomic scale and essentially temperature independent. Second, the results of the mode analysis were consistent with the results of Allen-Feldman for $\alpha$-Si2, and to those on YSZ. $^{25}$ In particular, moreover, localization was observed only for $x=0.125$ at around 27-28 THz. Nevertheless, the fraction of locon modes is still a small portion of the entire vibrational modes. However the participation ratio analyses showed the vibrational modes at frequencies lower than this were delocalized, with the polarization maps indicated that they had no clear wave vector or polarization.

This study has looked exclusively at intrinsic point defects. However, extrinsic defects such, fission products are present in $\mathrm{UO}_{2}$ the form of solid solutions, dispersions, and fission gases. Fission products that form solid solutions lower the thermal conductivity of $\mathrm{UO}_{2}$ by becoming mass defects or by straining the host crystal, thereby acting as scattering centers. $^{28,20}$ The second phase formed by fission may increase or decrease the thermal conductivity. $^{20,29}$ Fission products are often metallic precipitates and their behavior depends on the effect of burn up. $^{30}$ Near the center line region, the relatively high temperature allows formation of $0.05-1 \mu \mathrm{m}$ metallic particles, and their high electrical conductivity improves the heat transfer in $\mathrm{UO}_{2} \cdot{ }^{29,8}$ In a high burn up structure, the precipitates are often quite tiny (order of nanometers) and to the attendant phonon scattering lowers the thermal conductivity of the fuel. The effects of porosity depend on the size of the pore. For example, microbubbles act as obstacles to the phonons while larger pores commonly found at GBs impede heat transfer. Lucuta et al. $^{20}$ review the effect of fission products on thermal transport.

## VI. Concluding Remarks

Our results and analyses provide a coherent picture of the effect of off-stoichiometry on the thermal properties of $\mathrm{UO}_{2}$ in terms of a transition in increasing off-stoichiometry from crystalline to amorphous-like behavior. In particular, the effects of hypo- and hyperstoichiometry on thermal conductivity are very similar at the low concentrations. In addition, the temperature dependence is linear as in the classic phonon theory of heat transfer. However, at high concentrations, the thermal conductivity shows becomes essentially independent of temperature and concentration. In this regime, the diffuson modes dominate the heat transfer.

As discussed above, these results and physical mechanisms are very reminiscent of those operating in yttria-stabilized zirconia. They are thus strongly suggestive that this transition from ballistic phonon-like thermal transport to a less-efficient diffusive energy transport mechanism may be endemic in ceramics, regardless of the origin of the chemical or structural disorder, be it doping, off-stoichiometry or radiation damage.

## Acknowledgment

This work is supported by DOE-NERI Award DE-FC07-051D14649 at the University of Florida and by the AFCI/GNEP program at The Los Alamos National Laboratory (LANL). TW thanks Blas Uberuaga and Christopher Stanek for useful discussions during his stay at LANL.

## References

${ }^{1}$ N. W. Ashcroft and D. N. Mermin, Solid State Physics. Saunders College Publishing, New York, 1976.

${ }^{2}$ C. Kittel, Introduction to Solid State Physics, 7th edition, John Wiley \& Sons, Inc., New York, 1996.

${ }^{3}$ J. L. Feldman, M. D. Kluge, P. B. Allen, and F. Wooten, "Thermal-Conductivity and Localization in Glasses - Numerical Study of a Model of Amorphous Silicon," Phys. Rev. B, 48 [17] 12589-602 (1993).

${ }^{4}$ D. G. Cahill, S. K. Watson, and R. O. Pohl, "Lower Limit to the ThermalConductivity of Disordered Crystals," Phys. Rev. B, 46 [10] 6131-40 (1992).

${ }^{5}$ R. O. Pohl, X. Liu, and E. Thompson, "Low-Temperature Thermal Conductivity and Acoustic Attenuation in Amorphous Solids," Rev. Modern Phys., 74 [4] 991-1013 (2002).

${ }^{6}$ P. B. Allen, J. L. Feldman, J. Fabian, and F. Wooten, "Diffusons, Locons and Propagons: Character of Atomic Vibrations in Amorphous Si," Philos. Mag. B-Phys. Condens. Matter Stat. Mech. Electron. Opt. Magnetic Prop., 79 [11-12] 1715-31 (1999).

${ }^{7}$ I. C. Hobson, R. Taylor, and JB Ainscoug, "Effect of Porosity and Stoichiometry on Thermal-Conductivity of Uranium-Dioxide," J. Phys. D-Appl. Phys., 7 [7] 1003-15 (1974).

${ }^{8}$ P. G. Lucuta, H. Matzke, and R. A. Verrall, "Thermal-Conductivity of Hyperstoichiometric Simfuel," J. Nucl. Mater., 223 [1] 51-60 (1995).

${ }^{9}$ S. Yamasaki, T. Arima, K. Idemitsu, and Y. Inagaki, "Evaluation of Thermal Conductivity of Hyperstoichiometric $\mathrm{UO}_{2+x}$ by Molecular Dynamics Simulation," Int. J. Thermophys., 28 [2] 661-73 (2007).

${ }^{10}$ F. Grønvold, "High-Temperature X-Ray Study of Uranium Oxides in the $\mathrm{UO}_{2}-\mathrm{U}_{3} \mathrm{O}_{8}$ Region," J. Inorg. Nucl. Chem., 1 [6] 357-70 (1955).

${ }^{11}$ M. Amaya, T. Kubo, and Y. Korei, "Thermal Conductivity Measurements on $\mathrm{UO}_{2+x}$ from 300 to 1,400 K," J. Nucl. Sci. Technol., 33 [8] 636-40 (1996).

${ }^{12}$ J. D. Higgs, W. T. Thompson, B. J. Lewis, and S. C. Vogel, "Kinetics of Precipitation of $\mathrm{U}_{4} \mathrm{O}_{9}$ from Hyperstoichiometric $\mathrm{UO}_{2+x}$," J. Nucl. Mater., 366 [3] 297-305 (2007).

${ }^{13}$ M. Abramowski, R. W. Grimes, and S. Owens, "Morphology of $\mathrm{UO}_{2}$," J. Nucl. Mater., 275 [1] 12-8 (1999).

${ }^{14}$ G. Busker, "Solution and Migration of Impurity Ions in $\mathrm{UO}_{2}, \mathrm{U}_{3} \mathrm{O}_{8}$, and $\mathrm{Y}_{2} \mathrm{O}_{3}$ "; in Department of Materials, Imperial College of Science, Technology, and Medicine, London, UK, 2002.

${ }^{15}$ K. Govers, S. Lemehov, and M. Verwerft, "Comparison of Interatomic Potentials for $\mathrm{UO}_{2}$. Part I: Static Calculations," J. Nucl. Mater., 266 [1-2] 161-77 (2007).

${ }^{16}$ P. Jund and R. Jullien, "Molecular Dynamics Calculation of the Thermal Conductivity of Vitreous Silica," Phys. Rev. B, 59 [21] 13707-11 (1999).

${ }^{17}$ P. K. Schelling, S. R. Phillpot, and P. Keblinski, "Comparison of Atomic-level Simulation Methods for Computing Thermal Conductivity," Phys. Rev. B, 65 [14] 144306 (2002).

${ }^{18}$ T. Watanabe, S. B. Sinnott, J. S. Tulenko, R. W. Grimes, P. K. Schelling, and S. R. Phillpot, "Thermal Transport Properties of Uranium Dioxide by Molecular Dynamics Simulations," J. Nucl. Mater., 375 [3] 388-96 (2008).

${ }^{19}$ J. K. Fink, "Thermophysical Properties of Uranium Dioxide," J. Nucl. Mater., 279 [1] 1-18 (2000).

${ }^{20}$ P. G. Lucuta, H. Matzke, and I. J. Hastings, "A Pragmatic Approach to Modelling Thermal Conductivity of Irradiated $\mathrm{UO}_{2}$ Fuel: Review and Recommendations," J. Nucl. Mater., 232 [2-3] 166-80 (1996).

${ }^{21}$ C. Ronchi, M. Sheindlin, M. Musella, and G. J. Hyland, "Thermal Conductivity of Uranium Dioxide up to $2900 \mathrm{~K}$ from Simultaneous Measurement of the Heat Capacity and Thermal Diffusivity," J. Appl. Phys., 85 [2] 776-89 (1999).

${ }^{22}$ J. M. Ziman, Electrons and Phonons. Oxford University Press, London, UK, 1960.

${ }^{23}$ C. K. Gupta, Materials in Nuclear Energy Applications. CRC Press, Boca Raton, FL, 1989, 2pp.

${ }^{24}$ A. Maradudin, Theory of Lattice Dynamics in the Harmonic Approximation, 2nd edition, Academic Press, New York, 1971.

$^{25}$P. K. Schelling and S. R. Phillpot, "Mechanism of Thermal Transport in Zir- conia and Yttria-Stabilized Zirconia by Molecular-Dynamics Simulation," *J. Am. Ceram. Soc.*, **84** [12] 2997–3007 (2001).

$^{26}$R. J. Bell, P. Dean, and DC. Hibbinsb, "Localization of Normal Modes in Vitreous Silica, Germania and Beryllium Fluoride," *J. Phys. Part C Solid State Phys.*, **3** [10] 2111–8 (1970).

$^{27}$P. G. Klemens, "The Scattering of Low-Frequency Lattice Waves by Static Imperfections," *Proc. Phys. Soc. Lond. Sect. A*, **68** [12] 1113–28 (1955).

$^{28}$J. Janeczek, R. C. Ewing, V. M. Oversby, and L. O. Werme, "Uraninite and UO₂ in Spent Nuclear Fuel: A Comparison," *J. Nucl. Mater.*, **238** [1] 121–30 (1996).

$^{29}$P. G. Lucuta, H. Matzke, and R. A. Verrall, "Modeling of UO₂-Based Simfuel Thermal-Conductivity – the Effect of the Burn up," *J. Nucl. Mater.*, **217** [3] 279–86 (1994).

$^{30}$C. T. Walker, D. Staicu, M. Sheindlin, D. Papaioannou, W. Goll, and F. Sontheimer, "On the Thermal Conductivity of UO₂ Nuclear Fuel at a High Burn-Up of Around 100 MWd/kgHM," *J. Nucl. Mater.*, **350** [1] 19–39 (2006).$\square$