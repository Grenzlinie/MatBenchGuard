![](./images/812710468874403841_1.jpg)

Liquid-vapor interface of water-methanol mixture. I. Computer simulation

Mitsuhiro Matsumoto, Yuji Takaoka, and Yosuke Kataoka

Citation: J. Chem. Phys. 98, 1464 (1993); doi: 10.1063/1.464310
View online: http://dx.doi.org/10.1063/1.464310
View Table of Contents: http://jcp.aip.org/resource/1/JCPSA6/v98/i2
Published by the American Institute of Physics.

---

Additional information on J. Chem. Phys.
Journal Homepage: http://jcp.aip.org/
Journal Information: http://jcp.aip.org/about/about_the_journal
Top downloads: http://jcp.aip.org/features/most_downloaded
Information for Authors: http://jcp.aip.org/authors

ADVERTISEMENT

![](./images/812710468874403841_2.jpg)

# Liquid-vapor interface of water-methanol mixture. I. Computer simulation

Mitsuhiro Matsumoto
Department of Applied Physics, School of Engineering, Nagoya University, Nagoya 464-01, Japan

Yuji Takaoka and Yosuke Kataoka
Department of Chemistry, Faculty of Science, Kyoto University, Kyoto 606-01, Japan

(Received 1 July 1992; accepted 5 October 1992)

Results of molecular dynamics computer simulation are presented for liquid-vapor interface of water-methanol mixture of various compositions at room temperature. The composition dependence of calculated surface tension is typical of aqueous solutions of organic compounds. The outermost surface layer is saturated with methanol even at low bulk concentrations of methanol. The density profile of each component seems oscillatory at some compositions.

## INTRODUCTION

Inhomogeneous fluids are of great importance in wide range of science, and thermodynamics of such systems has been well developed. $^{1,2}$ Also, microscopic structures of liquid-vapor interface have been studied both theoretically and experimentally, and much information has been accumulated with help of recent computer simulation techniques. $^{3,4}$ Among others, aqueous systems are of particular interest because of their importance in chemistry and biology. There is well-known uniqueness in surface properties of associating fluids like water, $^{5}$ and microscopic structures due to hydrogen bonding seem responsible for it. However, most of the systems studied so far are pure water $^{6-12}$ and pure methanol. $^{13}$ Interfacial systems of solutions and mixtures have been difficult targets until quite recently due to insufficient computational resources; it requires a larger system than a pure fluid case to obtain good statistics. There are several reports on aqueous solutions of small ions $^{14,15}$ and organic compound (phenol), $^{16}$ the results of which show reasonable picture of interfacial properties and structures, including (positive or negative) surface adsorptions.

In this paper, we report results of molecular dynamics (MD) computer simulation concerning the surface properties of water-methanol mixture at various compositions. Methanol, which is completely miscible with water, can be regarded as one of the simplest type of surfactants. We found from computer simulations of pure methanol surface that methanol molecules show strong orientational ordering near the surface due to the hydrophobic methyl group. $^{13}$ It is also experimentally known that the composition dependence of surface tension of water-methanol mixture is typical of aqueous solutions of organic compounds which show strong positive surface adsorption of solutes. We expect, therefore, that the study of this simple mixture system in detail will elucidate the relation between thermodynamic properties and microscopic structure for the surface of water-surfactant mixture. Although insufficient statistics still prevents us from obtaining a definite conclusion, surface-excess thermodynamic quantities are found to have an extraordinary behavior at low bulk concentrations of methanol, at which the outermost surface layer is already saturated with methanol. We also show that the density profiles are very different from those of simple fluid mixtures.

## SIMULATION METHOD

We use a microcanonical ensemble (NVT-constant) MD method. The computer program is similar to what we used to simulate a liquid-vapor interface of pure methanol; $^{13}$ the periodic boundary conditions for all three dimensions, the Ewald summation technique for the Coulombic interactions, and the leap-frog algorithm with quaternion for numerical integration of the equations of motion. The time step size is $0.5$ fs $(=0.5×10^{-15}$ s). The short-ranged potential cutoff is $14$ $\mathring{A}$.

The intermolecular potentials are Jorgensen's TIP4P for water $^{17}$ and TIPS for methanol. $^{18}$ They are four-site (for water) or three-site (for methanol) rigid models; the site-site interactions are Coulombic and Lennard-Jones (12-6) types.

We have done the MD calculations for nine different compositions of mixture as shown in Table I. The total number of molecules is 1000 for all systems. The computation time was typically several CPU hours on a vector processor (FACOM VP-400E of Kyoto University Data Processing Center or HITAC S820/80 of Computer Center of the Institute for Molecular Science) for each composition.

The unit cell is a rectangular prism (Fig. 1), in the center of which we make a thick layer (slab) of the liquid mixture (randomly arranged molecules) at the beginning of each simulation. Since methanol molecules are bulkier than water, we make the surface area composition dependent so that the thickness of the slab is about $40$ $\mathring{A}$, independent of the composition; the detail is shown in Table I. The distance between periodic slabs (due to the boundary conditions) is about $80$ $\mathring{A}$, which makes the artificial interference negligible.

We have estimated the temperature from the total kinetic energy of the system, and adjusted it to be 300 K during the equilibrating process (typically 20 000 steps, or 10 ps). The obtained temperature during the main process (100 000-175 000 steps, depending on the composition) is

<table>
<caption>TABLE I. Simulation conditions and some results. $L_x$ is the cell size shown in Fig. 1, $T$ is the temperature estimated from the total kinetic energy, $P$ is the pressure, and $x_M$ is the mole fraction of methanol in the bulk liquid phase.</caption>
<thead>
<tr>
<th colspan="2">Number of molecules</th>
<th rowspan="2">$L_x$ (Å)</th>
<th rowspan="2">Number of steps</th>
<th rowspan="2">$T$ (K)</th>
<th rowspan="2">$P$ (MPa)</th>
<th rowspan="2">$x_M$</th>
</tr>
<tr>
<th>Methanol</th>
<th>Water</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td>1000</td>
<td>32.0</td>
<td>100 000</td>
<td>301.0±1.4</td>
<td>−0.92±0.21</td>
<td>0</td>
</tr>
<tr>
<td>50</td>
<td>950</td>
<td>32.5</td>
<td>175 000</td>
<td>300.8±1.0</td>
<td>−0.83±0.36</td>
<td>0.045</td>
</tr>
<tr>
<td>100</td>
<td>900</td>
<td>33.0</td>
<td>175 000</td>
<td>301.3±0.6</td>
<td>−0.84±0.22</td>
<td>0.089</td>
</tr>
<tr>
<td>200</td>
<td>800</td>
<td>34.0</td>
<td>100 000</td>
<td>319.5±6.2</td>
<td>−0.20±0.61</td>
<td>0.195</td>
</tr>
<tr>
<td>250</td>
<td>750</td>
<td>34.5</td>
<td>100 000</td>
<td>299.8±0.8</td>
<td>−0.71±0.35</td>
<td>0.275</td>
</tr>
<tr>
<td>300</td>
<td>700</td>
<td>35.0</td>
<td>100 000</td>
<td>303.5±1.6</td>
<td>−0.59±0.38</td>
<td>0.320</td>
</tr>
<tr>
<td>500</td>
<td>500</td>
<td>37.0</td>
<td>100 000</td>
<td>301.7±1.9</td>
<td>−0.37±0.36</td>
<td>0.468</td>
</tr>
<tr>
<td>750</td>
<td>250</td>
<td>39.5</td>
<td>120 000</td>
<td>300.3±1.8</td>
<td>0.24±0.66</td>
<td>0.747</td>
</tr>
<tr>
<td>1000</td>
<td>0</td>
<td>42.0</td>
<td>120 000</td>
<td>299.8±3.0</td>
<td>0.41±0.71</td>
<td>1</td>
</tr>
</tbody>
</table>

approximately 300 K. However, for the case of methanol water=200/800, fluctuations of temperature were very large for some unknown reason and the temperature control failed; we show the data of this case separately in most of the following analyses since surface properties are usually quite sensitive to the temperature. The data fluctuations shown in Table I are the standard deviations calculated by dividing the total run into several blocks. The obtained pressure of bulk liquid phase, which is calculated as an average of zz diagonal element of the pressure tensor, is also shown in Table I. The last column of the table shows the mole fraction of methanol in the bulk liquid phase, estimated from plateau values of the density profiles as discussed in the next section. The fraction is slightly different from the initial composition due to surface adsorptions.

## RESULTS AND DISCUSSION
### Bulk liquid phase

We obtained the local number densities and local energy densities, from which the density profiles and energy profiles are calculated as discussed in some detail later. As the thermodynamic properties of bulk liquid mixtures, we can easily estimate mass densities and energy densities of bulk phases by averaging the plateau values of each profile.

![](./images/812710468874403841_3.jpg)

FIG. 1. Unit cell used in the simulation. $L_z$ is always 120 Å, but $L_x(=L_y)$ depends on the composition as described in Table I.

In Fig. 2, the mass densities of each species and their total are plotted against $x_M$, the mole fraction of methanol in bulk liquid, and compared with experimental values at room temperature.¹⁹ Except that the calculated densities of TIPS methanol are a little smaller than the experimental values, the simulational results of total density are very similar to the experimental ones; they are both slightly deviated to lower values from the linear combination of pure liquid densities.

We show in Fig. 3 the molar volume (not partial molar volume) of the liquid mixtures and its excess. Reasonably, the excess has a minimum. Also, the molar energy of the liquid mixtures and its excess are shown in Fig. 4. Although we cannot estimate the mixing enthalpy $h^E$ directly from these data, it is very likely that $h^E$ has also a minimum at $x_M$ (mole fraction of methanol)=0.3–0.5, which agrees with experiments.²⁰

### Profiles

Computer simulation gives us useful information which is experimentally inaccessible. In particular, density

![](./images/812710468874403841_4.jpg)

FIG. 2. Mass density of bulk liquid phase compared with experimental values (dashed line, Ref. 19). Crosses: total density, open circles: water, filled circles: methanol. The solid lines are guides to eyes.

![](./images/812710468874403841_5.jpg)

FIG. 3. Molar volume of liquid phase (open circles) and its mixing excess (filled circles) plotted against the mole fraction of methanol.

![](./images/812710468874403841_6.jpg)

FIG. 4. Molar energy of liquid phase (open circles) and its mixing excess (filled circles) plotted against the mole fraction of methanol.

![](./images/812710468874403841_7.jpg)

FIG. 5. Density profile for various compositions. The mole fraction of methanol in the bulk liquid, $x_M$, is shown on each figure.

profiles of mixtures are very important for the purpose of investigating the surface adsorption closely. Figure 5 is the mass density profiles for various compositions of the mixture, from (a) pure water to (f) pure methanol. The profiles of pure fluids are quite similar to what we reported previously. $^{11,13}$ It is apparent from Figs. 5(b)-5(e), where the mass densities of each species as well as the total mass density are shown, that methanol is strongly adsorbed to the surface as we expected.

For the mixture cases, the data fluctuations are large and the profile of each species is not symmetric around the middle of the liquid slab, especially for the cases of lower concentration of methanol. The profile of the total density is almost symmetric, and evidently, the system is at least in quasi-equilibrium. The asymmetry mainly comes from the bias of the initial configuration. Methanol molecules are adsorbed so strongly to the surface that it will take prohibitively long time to obtain symmetric profiles. In this paper, we treat the right and left surfaces as two independent samples of the mixture surfaces.

An interesting point is that the profile of water as well as that of methanol seems oscillatory near the surface at low concentrations of methanol. As far as we know, mixtures of simple fluids do not show such oscillation. $^{21,22}$ The reason for this oscillatory profile of each species is not fully understood yet, but it can be a precursory behavior of phase separation into two immiscible liquid phases. We can speculate that, since methanol-water interaction (mainly due to hydrogen bonding) is energetically more stable than methanol-methanol one, water molecules are dominant in the second outermost layer and are favorably interacting with methanol molecules which are adsorbed on the surface.

Aqueous solutions of alcohols are known to show some peculiar thermodynamic behaviors, which are often ex-

![](./images/812710468874403841_8.jpg)

FIG. 6. Examples of the potential energy profile; the mole fraction of methanol $x_M$ is shown on each figure. $E_W$ and $E_M$ are the molar potential energy of water and methanol, respectively, and $u$ is the potential energy density (energy per unit volume).

plained in terms of clathrate hydrate formation of alcohols. $^{23}$ In this report, we do not analyze the detailed local structure from that point of view, but it would be interesting to see how the inhomogeneity (liquid-vapor interface) affects the clathrate structure.

Examples of energy profiles are shown in Fig. 6. Here we calculate two different types of energy profiles; $E_W(z)$ and $E_M(z)$ are the molar energy of water and methanol, respectively, which are the mean potential energy of each molecule, and $u(z)$ is the energy density (potential energy per unit volume), which is similar to what we showed in the previous reports for pure water $^{11}$ and methanol. $^{13}$ Notice that $E_M(z)$ has a shoulder near the surface; this is seen much clearer for the case of $x_M{\leqslant}0.5$. Since the amplitude of the shoulder is about $-25$ kJ/mol (twice the typical hydrogen-bonding energy per bond), it should correspond to the outermost adsorbed methanol molecules which are stabilized by two hydrogen bonds.

From these profiles, we can estimate the surface thickness. Several definitions of thickness are known, but here for simplicity, we adopt the definition of 10-90 thickness, which is the distance encompassing 10% to 90% of the mass density change between the bulk liquid and vapor values. The results are shown in Fig. 7 for both thicknesses $t_d$ [from the mass density profiles $\rho(z)$] and $t_u$ [from the energy density profiles $u(z)$]. We reported previously $^{11,13}$ that $t_u$ is very close to $t_d$ for pure water and pure methanol, which probably reflects energy stabilization due to hydrogen bonds, while $t_u{\gg}t_d$ for the case of simple fluids near the triple point. Similar results are obtained for the mixtures.

![](./images/812710468874403841_9.jpg)

FIG. 7. Surface thicknesses vs mole fraction of methanol, calculated from density profiles (open circles) and from energy profiles (filled circles).

## Thermodynamics

Surface tension $\gamma$ is easily calculated as the spatial integral of difference between tangential and normal components of the pressure tensor by use of virial expression. $^{24}$ In Fig. 8, we compare the obtained $\gamma$ with experimental results. $^{25,26}$ The obtained values are 20%-50% smaller than the experimental ones, but the dependence on the composition is similar; a small amount of methanol drastically decreases $\gamma$. This tendency is typical of organoaqueous systems, in which the organic compound is strongly adsorbed to the surface.

![](./images/812710468874403841_10.jpg)

FIG. 8. Surface tension vs mole fraction of methanol. Simulation data (circles) are compared with experimental data (dashed curve, Refs. 24 and 25). Typical range of fluctuations of the simulation data is shown as an error bar. The solid lines and dash-dot lines are the tangent predicted by the Gibbs' isotherm relations, Eq. (6), as described in the text.

Next we consider surface excess thermodynamic quantities per unit area. The word "excess" here means the difference of any thermodynamic quantity between the observed value and the sum of bulk phase values. In general, $\phi^{s}$, the surface excess of $\Phi$ (=mass, energy, entropy, etc.), is defined through the following relation:²

$$
\Phi=\phi^{l} V^{l}+\phi^{g} V^{g}+\phi^{s} A, \tag{1}
$$

where $\phi^{i}$ ($i=l$ for liquid phase, $g$ for gas phase) is the density of $\Phi$ of each bulk phase at equilibrium, $V^{i}$ is the volume of each phase, and $A$ is the area of the interface.

In principle, one can choose the position of the interface arbitrarily, which is equivalent to the arbitrariness of choosing $V^{l}$ (=$V-V^{g}$, where $V$ is the total volume). However, the surface tension is equal to the surface excess (Helmholtz) free energy only when we choose the position of the interface as the so-called Gibbs dividing surface. In the case of pure fluids, this choice is quite natural because surface excess number of molecules (surface adsorption), $\Gamma$, is zero for this choice. Also, at least in simulational studies, it is easy to determine the position of Gibbs surface from the density profile data. For mixture systems, however, the determination is very difficult. Instead of the simple condition $\Gamma=0$, the consistent definition of Gibbs surface for mixtures is written as²

$$
\sum_{\alpha} \mu_{\alpha} \Gamma_{\alpha}=0, \tag{2}
$$

where $\mu_{\alpha}$ is the chemical potential of $\alpha$ species and $\Gamma_{\alpha}$ is its surface adsorption. In other words, we should use the "chemical-potential-averaged" density profile to determine the position of the Gibbs surface. Only when we adopt the definition Eq. (2), the surface tension $\gamma$, which itself is experimentally measurable, can be equated to the surface excess free energy. However, since estimating the chemical potential (or free energy) from simulational data requires much more computation time than estimation of other thermodynamic quantities, we do not use the condition Eq. (2) in this study. In Ref. 22, the gas density was used to estimate the chemical potential; in our case, however, the temperature is low and we cannot determine the gas density accurately enough.

There is another, and more frequently adopted, definition for the surface position; we arbitrarily regard one species as a "solvent" and others "solutes," and apply the Gibbs surface condition only to the solvent, i.e., $\Gamma_{\text{solvent}}=0$. This definition would be practical when one considers the system in a narrow range of composition and one of the species is dominant, but it would be inappropriate for our systems since we are interested in mixtures of whole range of composition, from pure water to pure methanol. Therefore, we adopt an approximate condition instead of Eq. (2),

$$
\sum_{\alpha} m_{\alpha} \Gamma_{\alpha}=0, \tag{3}
$$

where $m_{\alpha}$ is molecular mass of $\alpha$ species. This condition means that the total "surface excess mass" is zero. Although there would be many other choices (e.g., using experimental values for chemical potential), we believe that the qualitative features described below would not be changed much.

![](./images/812710468874403841_11.jpg)

FIG. 9. Surface excess energy (open circles) and surface excess entropy (filled circles) vs mole fraction of methanol.

Once we define the position of the surface, we can calculate the surface-excess (internal) energy, $u^{s}$, based on Eq. (1). Surface excess entropy, $s^{s}$, is obtained through a fundamental thermodynamic relation²

$$
\gamma=u^{s}-T s^{s}, \tag{4}
$$

where $T$ is the temperature of the system. Note that Eq. (4) is approximate in the sense of equating $\gamma$ to the surface excess free energy of our system. The results of $u^{s}$ and $s^{s}$ are plotted in Fig. 9. Figure 10 shows their mixing excess, i.e., the deviation from the linear combination of pure fluid values. $\Delta u^{s}$ and $\Delta s^{s}$ have a similar behavior and compensate each other to give small values of $\Delta \gamma$. At the compositions of $x_{M} \leqslant 0.3$, $\Delta u^{s}$ and $\Delta s^{s}$ are both negative; this also suggests that the surface is energetically stabilized at the expense of the entropy decrease.

For monolayers of surfactants on water, the concept of surface pressure is often used to analyze the system.² The

![](./images/812710468874403841_12.jpg)

FIG. 10. Mixing excess of surface tension (crosses), surface excess energy (open circles), and surface excess entropy (filled circles) vs mole fraction of methanol.

J. Chem. Phys., Vol. 98, No. 2, 15 January 1993

![](./images/812710468874403841_13.jpg)

FIG. 11. (a) Surface pressure $\pi$ plotted against molar concentration of methanol $C_{M}$ in bulk liquid. (b) Surface compressibility factor $Z$ plotted against $\pi$.

surface pressure, $\pi$, is defined as the decrease of surface tension from the value of pure water. If one can assume the monolayer as two-dimensional ideal gas, $\pi$ should be proportional to the concentration of the solute. Also, the surface compressibility factor $Z$, defined as
$$
Z \equiv \frac{\pi A}{R T}=\frac{\pi}{\Gamma_{M}^{W} R T},
$$
is a useful quality to check the ideality of the layer. Here $R$ is the gas constant and $\Gamma_{M}^{W}$ is the surface adsorption of solute (methanol) when the Gibbs surface is determined for the solvent (water) density profile; the detail about the surface adsorption is described later. Figure 11 shows the results of $\pi$ and $Z$ for our systems. The feature is reasonable when compared with experimental results of higher alcohols, $^{27}$ though it would be unrealistic to imagine a "methanol monolayer" on water surface.

## Orientational order
On a surface of molecular liquids, molecules can have orientational ordering. The ordering of pure water was found to be weak, $^{10,11}$ but pure methanol shows significant ordering due to the hydrophobic methyl group. $^{13}$

One of the quantitative measure of the orientational ordering is the surface potential $\Delta \chi^{d}$ caused by the ordering of electric dipoles. In our case of water-methanol mixture system, $\Delta \chi^{d}$ can be expressed as
$$
\Delta \chi^{d}=\int_{\text {vapor }}^{\text {liquid }} E^{d}(z) d z, \quad(5)
$$
where
$$
\begin{aligned}
E^{d}(z)= & \epsilon_{0}^{-1}\left[n_{W}(z) d_{W}\left\langle\cos \Theta_{W}\right\rangle_{z}\right. \\
& \left.+n_{M}(z) d_{M}\left\langle\cos \Theta_{M}\right\rangle_{z}\right]
\end{aligned}
$$
is the local electric field induced by ordering of molecular electric dipoles of both species. Here $\epsilon_{0}$ is the dielectric constant of vacuum, $n_{i}(z)(i=W, M)$ is the number density of water and methanol, respectively, $d_{i}$ is the molecular electric dipole moment (the usual symbol for the electric dipole $\mu$ is used for the chemical potential in this paper), $\Theta_{i}$ is the angle between the dipole and the surface normal, and $\langle\cdots\rangle_{z}$ represents the local ensemble average at the position $z$. Although experimentally measured surface potential might be affected by the quadrupole density of bulk phases, $^{10}$ we omit the contribution here to see clearly the effect of the molecular orientational ordering at the surface; the correction is easy when necessary. $\left\langle\cos \Theta_{i}\right\rangle_{z}$ is calculated from the simulation data of molecular orientational distributions. We define two orientational angles $\theta$ and $\phi$ using the principal axes of the moment of inertia tensor in the same way as before $^{11,13}$ for each molecule.

In Fig. 12, we show the mean angles $\langle\Delta \theta\rangle$ and $\langle\Delta \phi\rangle$ of each species, and the electrostatic potential profile $\phi^{d}(z)$, defined as $d \phi^{d}(z) / d z=E^{d}(z)$, for (a) pure water, (b) 1:1 mixture, and (c) pure methanol. The mean angles are shown as the deviation from the mean of randomly oriented molecules
$$
\langle\Delta \theta\rangle \equiv\langle\theta\rangle-\langle\theta\rangle_{\text {random }}=\langle\theta\rangle-90^{\circ},
$$
and
$$
\langle\Delta \phi\rangle \equiv\langle\phi\rangle-\langle\phi\rangle_{\text {random }}= \begin{cases}\langle\phi\rangle-45^{\circ} & \text { water, } \\ \langle\phi\rangle-90^{\circ} & \text { methanol. }\end{cases}
$$

The potential at the center of the slab is chosen to be zero. The qualitative tendencies for mixtures are similar to those of pure systems except for the two points: (i) orientational orders in the mixture is enhanced for both water and methanol when compared with those in pure fluids; and (ii) the ordering of water molecules on vapor side of the interface $^{11}$ (one hydrogen atom is projected to vapor) disappears for mixtures.

In Fig. 13, the surface potential $\Delta \chi^{d}$ is plotted as a function of methanol mole fraction. The obtained surface potentials for pure water and pure methanol agree with our previous results, $^{11,13}$ which suggests that the orientational ordering of TIP4P water is almost the same as that of Carravetta-Clementi water. $^{27}$ The values for the two surfaces of the slab, shown as open circles in Fig. 13, are very different at lower concentrations of methanol, probably due to insufficient statistics.

It is amazing that a small amount of methanol adsorbed to the surface can change even the sign of $\Delta \chi^{d}$. Also it is interesting that the ordering of methanol molecules is enhanced at lower concentrations of methanol, which supports again the picture that methanol behaves like a surfactant. Experimental estimation of $\Delta \chi$ for water-methanol mixture $^{28}$ suggests a monotonic change with increase of methanol concentration, but the large statistical fluctuations of our results prevent us from further discussion. It would be also interesting to investigate more closely the relationship between $\Delta \chi$ and the surface adsorption, as pointed out from experiments of aliphatic alcohol solutions. $^{29}$

![](./images/812710468874403841_14.jpg)

FIG. 12. Locally averaged orientation angles of each species $\langle\Delta\theta\rangle$ and $\langle\Delta\phi\rangle$, and electrostatic potential profiles $\varphi^{d}$ as a function of position $z$ for (a) pure water, (b) 1:1 mixture of water and methanol, and (c) pure methanol. Angles are expressed as deviations from the values of random orientation. The electrostatic potential at the center of the slab is chosen to be zero.

## Adsorption

Another interesting quantity is the surface adsorption or surface excess number of molecules, $\Gamma_{i}$ ($i=W$ for water and $M$ for methanol), which is calculated from the definition Eq. (1):

$$
N_{i}=n_{i}^{l} V^{l}+n_{i}^{g} V^{g}+\Gamma_{i} A,
$$

where $N_{i}$ is the total number of molecules of species $i$, and $n_{i}^{l}$ and $n_{i}^{g}$ are the bulk number density of liquid and gas phases, respectively. We choose the surface position as the surface of zero total excess mass, as described above. There are various definitions of surface adsorption, which are related to differences in the choice of the surface position. $^{2}$ Here we also calculate $\Gamma_{i}^{j}$ ($i\neq j$ are either $W$ or $M$), which is the adsorption of species $i$ when species $j$ is considered as the solvent. For example, both $\Gamma_{M}$ and $\Gamma_{M}^{W}$ can be used as a measure of methanol adsorption; they should have the same value in the limit of $x_{M}\to0$ (infinite dilution of methanol), but in general, the two are different. Note that $\Gamma_{M}^{W}$ at $x_{M}=1$ (pure methanol) and $\Gamma_{M}^{W}$ at $x_{M}=0$ (pure water) are not defined, but the limit values can be obtained experimentally. $^{2}$

![](./images/812710468874403841_15.jpg)

FIG. 13. Surface potential $\Delta\chi^{d}$ plotted against mole fraction of methanol. Open circles are the calculated values for each side of the slab. The dotted lines connecting the average of the two are only for the guide to eyes.

Figure 14 is the results of surface adsorptions; $\Gamma_{i}$ and $\Gamma_{i}^{j}$ are shown as open circles and crosses, respectively. They seem contrary to our naive expectations that methanol is always positively adsorbed; as seen in Fig. 14(b), methanol shows negative adsorption at $x_{M}=0.25$-$0.3$. Since the statistics at these concentrations are not good, we cannot conclude whether the negativity is physically meaningful or not, but the reason for this peculiar behavior is

![](./images/812710468874403841_16.jpg)

FIG. 14. Surface adsorption of (a) water and (b) methanol. The definition of adsorption is different for each of three lines, as discussed in the text.

apparent from the density profile, Fig. 5(c). At this concentration, although methanol adsorption is actually positive around the vapor side of the surface, water density is enhanced near the liquid side of the surface, which contributes much to the positive value of water adsorption ($\Gamma_W$ and $\Gamma_W^M$).

Seeking for another measure of surface adsorption, we also calculate the excess of molecules in the layer of 10–90 thickness, $\Gamma_i^{10-90}$ (filled circles in Fig. 14), which roughly corresponds to experimental results evaluated with the microtome method. When the number of water and methanol molecules in the 10–90 layer are $N_W^{10-90}$ and $N_M^{10-90}$, respectively, the excess of methanol $\Gamma_M^{10-90}$, for example, can be defined as the difference between $N_M^{10-90}$ and the expected value calculated with the bulk liquid compositions:

$$
\begin{aligned}
\Gamma_{M}^{10-90} A & \equiv N_{M}^{10-90}-N_{W}^{10-90} \times n_{M}^{l} / n_{W}^{l} \\
& =N_{M}^{10-90}-N_{W}^{10-90} \times \frac{x_{M}}{1-x_{M}},
\end{aligned}
$$

where $A$ is the surface area, and $n_W^l$ and $n_M^l$ are the liquid phase number density of water and methanol, respectively. Similarly, $\Gamma_W^{10-90}$ is defined as

$$
\Gamma_{W}^{10-90} A \equiv N_{W}^{10-90}-N_{M}^{10-90} \times \frac{1-x_{M}}{x_{M}}.
$$

The results give a reasonable picture of positive methanol adsorptions for the whole range of composition, as we expected.

Surface adsorption $\Gamma$ is related to the surface tension $\gamma$ through the Gibbs equation.² The general form of the equation,

$$
\Gamma_{i}=-\left(\frac{\partial \gamma}{\partial \mu_{i}}\right)_{\left\{T, \mu_{j \neq i}\right\}},
$$

becomes more useful for a dilute solution of species $i$

$$
\Gamma_{i}=-\frac{c_{i}}{R T} \frac{\partial \gamma}{\partial c_{i}}, \quad (6)
$$

where $c_i$ is the molar concentration of species $i$. The tangent of $\gamma$ calculated with Eq. (6) is shown in Fig. 8. By definition, we ought to use $\Gamma_W^M (x_M \to 0)$ and $\Gamma_M^W (x_M \to 1)$ for $\Gamma_i$, but the results shown in Fig. 8 as the thick solid lines do not agree with the tendency of $\gamma$. When we use $\Gamma_i^{10-90}$ (dash–dot lines), however, the agreements are improved greatly.

![](./images/812710468874403841_17.jpg)

FIG. 15. Composition of the surface layer of 10–90 thickness vs mole fraction of methanol. The number of water molecules and methanol molecules in the layer are shown by open and filled circles, respectively, and the dashed line is the mole fraction of methanol of the layer.

### Surface layer composition

Finally, let us make a brief consideration about a possible cause of the "anomaly" in surface excess quantities at $x_M=0.2$–$0.5$. The deviation of surface tension from the linear mixing rule, typical of aqueous solutions of organic compounds, is often explained qualitatively that additional organic compound is strongly adsorbed to the surface and decreases the surface tension. In fact, we have shown in Fig. 14 that methanol is positively adsorbed in general, but the data are not so clear, partly due to the difficulty in determining the surface position.

In order to examine in some detail the idea that the surface is "covered" with methanol, we plot in Fig. 15 the number of molecules of each species in the layer of 10–90 thickness, and the mole fraction of methanol in the surface region, $\alpha$, as functions of $x_M$. The fraction $\alpha$ is a convex function of $x_M$, which supports again the positive adsorption of methanol, but the picture of adsorption is still vague. We also note from the figure that the number of methanol in the surface layer is almost independent of $x_M$ when $x_M \geqslant 0.5$.

Hence, we investigate the composition of surface layer more closely by cutting the layer of 10–90 thickness into nine thin slices (10–20, 20–30, ..., and 80–90 layers, where $r_1$–$r_2$ layer is the surface region which mass density is $r_1\%$

![](./images/812710468874403841_18.jpg)

FIG. 16. Number of molecules in thin-sliced surface layers plotted against the mole fraction of methanol.

to $r_{2} \%$ of the density change between the bulk liquid and vapor values) and examining the composition of each layer (Fig. 16). It is apparent from Fig. 16(b) that the vapor side of the surface layer is almost saturated with methanol even at low bulk concentrations ($x_{M} \geqslant 0.2$), while methanol density in the liquid side of the layer increases only grad- ually with the increase of $x_{M}$. This picture agrees with our previous observation about the oscillatory density profiles.

In summary, the results of MD simulation show typi- cal features of water-alcohol mixture surfaces. The meth- anol adsorbed to the surface significantly affects the surface thermodynamics as well as the microscopic interfacial structure. In particular, the vapor side of the surface is fully covered with methanol even at low concentrations of methanol; in such case, the density of water is enhanced from the bulk density just inside the adsorbed methanol layer. Orientational ordering near the surface is also en- hanced for both methanol and water. We will examine these findings in some detail in the following paper using a simple lattice-gas model. $^{30}$

Note added in proof. We wish to thank Dr. Colin G. Barraclough for drawing our attention to their recent work [C. G. Barraclough, P. T. McTigue, and Y. Leung Ng, J. Electroanal. Chem. 329, 9 (1992)] of water-methanol mix- ture surfaces, which we overlooked when preparing this manuscript. Their subject is the composition dependence of the surface potential, and they gave the critical comparison between their simulation results and experimental data. Our results of the surface potential are similar to theirs. Although they mentioned nothing about the surface ad- sorption in their paper, their density profiles of the water- methanol mixtures clearly show the anomalous peak of water density, especially at 0.25 mole fraction of methanol.

We are grateful to Kyoto University Data Processing Center and the Computer Center of the Institute for Mo- lecular Science for allowing us to use their computer facil- ities. This work is supported in part by Grants in Aid for Scientific Research (Nos. 01540398, 02245209, and 03231211) from the Ministry of Education, Science and Culture, Japan, and also by the Japan Society for the Pro- motion of Science and Japan/U.S. Research Corporation.

$^{1}$ E. A. Guggenheim, Thermodynamics (North-Holland, Amsterdam, 1949).
$^{2}$ A. W. Adamson, Physical Chemistry of Surfaces, 4th ed. (Wiley, New York, 1982).
$^{3}$ J. S. Rowlinson and B. Widom, Molecular Theory of Capillarity (Clar- endon, Oxford, 1982).
$^{4}$ Many recent theoretical and computational results are found in Fluid Interfacial Phenomena, edited by C. A. Croxton (Wiley, Chichester, 1986).
$^{5}$ R. J. Good, J. Phys. Chem. 61, 810 (1957).
$^{6}$ C. U. Lee and H. L. Scott, J. Chem. Phys. 73, 4591 (1980).
$^{7}$ R. M. Townsend, J. Gryko, and S. A. Rice, J. Chem. Phys. 82, 4391 (1985).
$^{8}$ N. I. Christou, J. S. Whitehouse, D. Nicholson, and N. G. Parsonage, Mol. Phys. 55, 397 (1985).
$^{9}$ E. N. Brodskaya and A. I. Rusanov, Mol. Phys. 62, 251 (1987).
$^{10}$ M. A. Wilson, A. Pohorille, and L. R. Pratt, J. Chem. Phys. 91, 4873 (1987); 88, 3281 (1988).
$^{11}$ M. Matsumoto and Y. Kataoka, J. Chem. Phys. 88, 3233 (1988).
$^{12}$ K. A. Motakabbir and M. L. Berkowitz, Chem. Phys. Lett. 176, 61 (1991).
$^{13}$ M. Matsumoto and Y. Kataoka, J. Chem. Phys. 90, 2398 (1989); 95,7782(E)(1991).
$^{14}$ I. Benjamin, J. Chem. Phys. 95, 3698 (1991).
$^{15}$ M. A. Wilson and A. Pohorille, J. Chem. Phys. 95, 6005 (1991).
$^{16}$ A. Pohorille and I. Benjamin, J. Chem. Phys. 94, 5599 (1991).
$^{17}$ W. L. Jorgensen, J. Chandrasekhar, J. D. Madura, R. W. Impey, and M. L. Klein, J. Chem. Phys. 79, 926 (1983).
$^{18}$ W. L. Jorgensen, J. Am. Chem. Soc. 103, 335 (1981).
$^{19}$ International Critical Tables of Numerical Data, Vol. 3, edited by Na- tional Academy of Sciences (McGraw-Hill, New York, 1926).
$^{20}$ L. Benjamin and G. C. Benson, J. Phys. Chem. 67, 858 (1963).
$^{21}$ G. A. Chapela, G. Saville, S. M. Thompson, and J. S. Rowlinson, J. Chem. Soc. Faraday Trans. 2 73, 1133 (1977).
$^{22}$ D. L. Lee, M. M. Telo da Gama, and K. E. Gubbins, Mol. Phys. 53,1113(1984).
$^{23}$ K. Iwasaki and T. Fujiyama, J. Phys. Chem. 81, 1908 (1977).
$^{24}$ J. G. Kirkwood and F. P. Buff, J. Chem. Phys. 17, 338 (1949).
$^{25}$ CRC Handbook of Chemistry and Physics, 72nd ed., edited by D. R. Lide et al. (CRC, Boston, 1991).
$^{26}$ International Critical Tables of Numerical Data, Vol. 4, edited by Na- tional Academy of Sciences (McGraw-Hill, New York, 1926).
$^{27}$ V. Carravetta and E. Clementi, J. Chem. Phys. 81, 2646 (1984).
$^{28}$ B. Case and R. Parsons, Trans. Faraday Soc. 63, 1224 (1967).
$^{29}$ A. M. Posner, J. R. Anderson, and A. E. Alexander, J. Colloid Sci. 7,623(1952).
$^{30}$ M. Matsumoto, H. Mizukuchi, and Y. Kataoka, J. Chem. Phys. 98,1473 (1993), following paper.