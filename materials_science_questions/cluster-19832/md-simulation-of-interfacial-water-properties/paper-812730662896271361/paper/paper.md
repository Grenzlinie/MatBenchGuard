![](./images/812730662896271361_1.jpg)

Hydrophobic effects: A computer simulation study of the temperature influence in dilute O 2 aqueous solutions

Ettore Fois, Aldo Gamba, and Claudio Redaelli

Citation: *The Journal of Chemical Physics* **110**, 1025 (1999); doi: 10.1063/1.478147
View online: http://dx.doi.org/10.1063/1.478147
View Table of Contents: http://scitation.aip.org/content/aip/journal/jcp/110/2?ver=pdfcov
Published by the AIP Publishing

Articles you may be interested in
Interactions of S-peptide analogue in aqueous urea and trimethylamine-N-oxide solutions: A molecular dynamics simulation study
J. Chem. Phys. **139**, 034504 (2013); 10.1063/1.4813502

Terahertz absorption of dilute aqueous solutions
J. Chem. Phys. **137**, 235103 (2012); 10.1063/1.4772000

Molecular dynamics simulations of Hg 2+ in aqueous solution including N-body effects
J. Chem. Phys. **118**, 5065 (2003); 10.1063/1.1553761

A study of aqueous solutions of lanthanide ions by molecular dynamics simulation with ab initio effective pair potentials
J. Chem. Phys. **115**, 4750 (2001); 10.1063/1.1391479

Effects of molecular association on mutual diffusion: A study of hydrogen bonding in dilute solutions
J. Chem. Phys. **110**, 3003 (1999); 10.1063/1.477895

![](./images/812730662896271361_2.jpg)

# Hydrophobic effects: A computer simulation study of the temperature influence in dilute $\boldsymbol{O_2}$ aqueous solutions

Ettore Fois, Aldo Gamba, and Claudio Redaelli
Istituto di Scienze Matematiche Fisiche e Chimiche, Universita' degli Studi dell'Insubria, Sede di Como,
Via Lucini 3, I-22100 Como, Italia

(Received 22 July 1998; accepted 6 October 1998)

We present a computer simulation study of the temperature dependence of the structural and dynamical properties of dilute $\mathrm{O}_{2}$ aqueous solutions. A clathrate-like solvation shell, in line with other apolar gas solutions, emerged from the present simulations. The average number of water molecules in the first hydration shell decreases with temperature, and, in the investigated temperature range (291-348 K), a net transfer of one water molecule from the hydration shell to the bulk has been detected. We have found oscillations of both water density and electrostatic charges in the neighborhood of the apolar solute, which is surrounded by shells of water at different density, and with water molecules oriented in such a way as to form shells with alternating net electrostatic charges. In the $\mathrm{O}_{2}$, first hydration shell water-water interactions are stronger and water diffusional and rotational dynamics slower than in the bulk. A hydrogen bond's mean lifetime is affected by the apolar solute as well, being shorter in the first hydration shell. Differences between shell and bulk water properties are smoothed by increasing temperature. Suggestions for the molecular mechanism relevant to the more general problems of the hydrophobic effects are deduced from the simulations. A possible microscopic explanation for the lowering of solubility of oxygen in water with temperature is given. © 1999 American Institute of Physics. [S0021-9606(99)50502-3]

## INTRODUCTION

The solvation processes of noble gases, hydrocarbons, and other apolar molecules are typical for liquid water and are referred to as hydrophobic effects. $^{1}$ They are usually separated in two contributions: hydrophobic hydration and hydrophobic interactions. $^{2-4}$ Hydrophobic hydration is associated with an increasing in structure of the liquids around an apolar molecule; such solvent ordering is due to clathrate behavior. $^{1,5}$ Hydrophobic interactions are long-ranged solvent mediated interactions among solute molecules, and can cause clustering of apolar substances in water. $^{6}$ A microscopic description of the molecular mechanisms involved in such phenomena is of crucial interest in different fields, including biology (e.g., protein folding, micellization), chemistry (e.g., phase separation), and geology (e.g., vast undersea deposits of gas hydrate). Molecular dynamics $^{7}$ is a powerful simulation technique that allows one to study the aggregate states of matter at an atomic level, enhancing the microscopic resolution of standard laboratory experiments. Here we present extensive computer simulations of dilute solutions of an apolar gas around room temperature: the solution of oxygen in water, which is one of the most important processes in the biosphere. We used the molecular dynamics method with the pair potential approximation to study the structure and the molecular motions in such solutions at different densities and temperatures. We studied the diffusional and rotational motion of the water molecules nearby and far away from the solute oxygen. In particular, the average structure of the hydration shell of the $\mathrm{O}_{2}$ molecule has been investigated in detail. The temperature dependence of the structural and dynamical behavior of solvent molecules has been investigated as well. We focalized the study of this dependence near ambient conditions, in the range 291-348 K.

The low solubility of an apolar solute in water is essentially due to the low solution free energy caused by an entropic-enthalpic compensation. $^{8}$ In fact, upon dissolution of small apolar molecules, an enhancement of the water structure around the solute occurs. This is enough to explain the negative hydration entropy. Moreover, the negative hydration enthalpy is due to stronger hydrogen bond interactions between neighboring water molecules. The overall process of hydration is formally separable in two distinct stages: first, the formation of the cavity (host) for the solute, with a local breaking of the dipole-dipole interactions between the water molecules, hydrogen bond (Hb), followed by replacing of the Hb's by the weaker host-guest interactions, dipole-induced dipole interaction. Oxygen, an apolar gas at room temperature, has a low solubility in water that decreases with the increase of the temperature, $^{8}$ and belongs to the class of hydrophobic solutes. In water, the $\Delta G$ of solution of apolar gases is slightly dominated by negative entropic contributions, $^{8}$ $T\Delta S<0$. This implies that such solutes are structure making molecules, in the sense that the typical liquid phase disorder should decrease because of the presence of the dilute gas. As water is a network liquid, $^{9}$ characterized by a net of hydrogen bonds, the inclusion in the fluid of a nonhydrogen bond making molecule, like an apolar gas or a hydrocarbon, should collapse, at least locally, the hydrogen bond's network so naively to give a positive entropic contribution. This contrasts with the experimental finding. In this view, microscopic detailed studies are needed to explain the hydrophobic effects in solution. As stated above, the nega-

<table>
 <thead>
  <tr>
   <th>
    $\langle T\rangle$
   </th>
   <th>
    $\rho^{14}$
   </th>
   <th>
    $t$
   </th>
   <th>
    $U_{W - W}$
   </th>
   <th>
    $U_{O_{2} - W}$
   </th>
   <th>
   </th>
   <th>
   </th>
  </tr>
  <tr>
   <th>
    (K)
   </th>
   <th>
    (g$\cdot$cm$^{-3}$)
   </th>
   <th>
    (ps)
   </th>
   <th>
    (Kcal$\cdot$mol$^{-1}$)
   </th>
   <th>
    (Kcal$\cdot$mol$^{-1}$)
   </th>
   <th>
    $N(r)\text{O}_{W}$
   </th>
   <th>
    $N(r)\text{H}_{W}$
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td colspan="7">
    Solution
   </td>
  </tr>
  <tr>
   <td>
    291
   </td>
   <td>
    0.9991
   </td>
   <td>
    232.2
   </td>
   <td>
    $-$11.274
   </td>
   <td>
    $-$0.013 12
   </td>
   <td>
    17.9
   </td>
   <td>
    36.1
   </td>
  </tr>
  <tr>
   <td>
    296
   </td>
   <td>
    0.9970
   </td>
   <td>
    222.5
   </td>
   <td>
    $-$11.134
   </td>
   <td>
    $-$0.013 23
   </td>
   <td>
    17.8
   </td>
   <td>
    35.9
   </td>
  </tr>
  <tr>
   <td>
    311
   </td>
   <td>
    0.9940
   </td>
   <td>
    232.2
   </td>
   <td>
    $-$10.909
   </td>
   <td>
    $-$0.012 61
   </td>
   <td>
    17.4
   </td>
   <td>
    35.2
   </td>
  </tr>
  <tr>
   <td>
    321
   </td>
   <td>
    0.9880
   </td>
   <td>
    241.9
   </td>
   <td>
    $-$10.761
   </td>
   <td>
    $-$0.012 49
   </td>
   <td>
    17.2
   </td>
   <td>
    34.8
   </td>
  </tr>
  <tr>
   <td>
    348
   </td>
   <td>
    0.9748
   </td>
   <td>
    232.2
   </td>
   <td>
    $-$10.393
   </td>
   <td>
    $-$0.011 98
   </td>
   <td>
    17.0
   </td>
   <td>
    34.3
   </td>
  </tr>
  <tr>
   <td colspan="7">
    Pure liquid
   </td>
  </tr>
  <tr>
   <td>
    299
   </td>
   <td>
    0.9970
   </td>
   <td>
    48.3
   </td>
   <td>
    $-$11.097
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    323
   </td>
   <td>
    0.9880
   </td>
   <td>
    48.3
   </td>
   <td>
    $-$10.747
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
 </tbody>
</table>

tive entropic contribution implies a global structural reorganization of the water molecules both near the apolar solute (first coordination shell) and in the bulk of the solution. According to the hypothesis by Frank and Evans,10 the accepted model for explaining this structural reorganization involves the presence of molecular cluster around the apolar solute.

## CALCULATIONS

We present a set of classical molecular dynamics simulations in the microcanonical ensemble (NVE), where $N$ is the number of particles, $V$ is volume, and $E$ is energy. A cubic cell with periodic boundary conditions, the pairwise potentials, and rigid molecules approximations were adopted. Water–water interactions were approximated by the SPCE/E (simple point charge/extended)11 pair potential, while oxygen–water interactions12 are approximated by a Lennard-Jones (LJ) (10-6) for the $\text{O}_{2} - \text{O}_{W}$ potential ($\text{O}_{W}$ is water’s oxygen), and a Morse function for the $\text{O}_{2} - \text{H}_{W}$ potential ($\text{H}_{W}$ is water’s hydrogen). The long-range electrostatic interactions were treated using the Ewald sum method with a reciprocal space cutoff of 6.25 Ry. Newton’s equations of motion for a rigid body were solved by the Rattle procedure13 to conserve the intramolecular constraints, with a time step of 0.484 fs. The solution’s models consisted of an $\text{O}_{2}$ molecule immersed in the liquid formed by 215 water molecules. The pure liquid water was simulated by 216 water molecules. Different simulations were performed at different temperatures, namely at different densities obtained by experimental values14 at atmospheric pressure (see Table I). For each simulation, a starting random configuration was generated and equilibrated for $\sim$50 ps at the desired temperature, then the simulations were continued for $\sim$220 ps in the case of the solutions, and for $\sim$50 ps for the pure liquid. Also, some energetic results are reported in Table I.

## STRUCTURAL PROPERTIES

The analysis of the radial distribution functions, $g(r)$’s, can provide detailed information of the structure of liquids, and their knowledge is of main importance for a better understanding of the hydrophobic phenomena (e.g., see for recent applications, Ref. 15). Our main interest is to investigate the effect of the temperature on the reorganization of the water molecules around the solute, in order to study the thermal behavior of the ‘‘clathration shell.’’ The oxygen–hydrogen, $g_{\text{O}_{2} - \text{H}_{W}}$, and the oxygen–oxygen, $g_{\text{O}_{2} - \text{O}_{W}}$, $g(r)$’s of the solutions in the temperature range of 291 and 348 K are shown in Fig. 1. At each temperature the first peak of the two $g(r)$’s is found nearly at the same distance from the solute, $\sim$3.5 Å. This can be possible only if the water molecules of the first shell lie, on average, nearly on a sphere, centered on the apolar solute. Such a finding indicates that water molecules that cannot be involved in Hb with the hydrophobic solute prefer to be linked, via Hb, to other molecules within the hydration shell. On the other hand, the second peak of $g_{\text{O}_{2} - \text{O}_{W}}$ is located at a shorter distance than that of $g_{\text{O}_{2} - \text{H}_{W}}$, and the tail of the first peak of $g_{\text{O}_{2} - \text{H}_{W}}$ is at a longer distance than the tail of the first peak of $g_{\text{O}_{2} - \text{O}_{W}}$. This suggests that some water molecules are able to turn their hydrogens toward the bulk, allowing formation of Hb bridges between the first two hydration shells. This enclathration structure, also observed in previous simulations of apolar molecules in water,16–21 is the accepted description at a microscopic level of the hydrophobic hydration. These quantities have been widely investigated in the past years, and also the results of recent x-ray and neutron scattering experiments22,23 agree with the model derived from computer simulations. Both experiments and computer simulations are consistent with Pratt and Chandler theory,24 the single one available to obtain these quantities. We have found that the first hydration shell of the $\text{O}_{2}$ molecule includes about 18 water molecules at room temperature. This number is compatible with an icosahedral structure, like that found for crystalline hydrates of small sized apolar substances.25 In order for the clathrate-like structure to exist, the distributions along the hydrophobic surface are expected to be formed by pentagons, with significant depletions of hexagons and larger polygons.5,26 However, this is a static viewpoint; indeed the solvation cage changes on the picosecond scale, and several short living structures alternate rapidly.

A snapshot of the hydration shell (from the 296 K simulation), where a planar pentagon is evidenced, is shown in Fig. 2. Such short living polyhedra are common structures in many simulations (e.g., see Ref. 5). In the gas phase, the more stable structure of a $(\text{H}_{2}\text{O})_{5}$ cluster is a planar pentagon, with oxygen atoms at the vertices, and where each water molecule acts both as a donor and acceptor of Hb’s. Infrared (IR) spectroscopy of benzene–water clusters and ab initio calculations of isolated $(\text{H}_{2}\text{O})_{5}$ support this model.27 On the other hand, in our simulations in the liquid phase, we found that the most frequent pentamer is a structure like that in Fig. 2, namely a nearly planar $(\text{H}_{2}\text{O})_{5}$, with a double donor molecule (molecule No. 1 in Fig. 2) and a double acceptor one (molecule No. 4). It should be noticed that such $(\text{H}_{2}\text{O})_{5}$ clusters are linked, via Hb, to other $\text{H}_{2}\text{O}$ molecules in the shell. Pentagonal water structures have been found in more complex systems like proteins and other biochemistry relevant macromolecules. Direct evidence came from a solid-state

![](./images/812730662896271361_3.jpg)

FIG. 1. Radial distribution functions $g(r)$'s, $O_2$ with water's oxygens ($O_2$-$O_W$), and $O_2$ with hydrogens ($O_2$-$H_W$); solid lines: 291 K; dotted lines: 296 K; dashed lines: 311 K; long-dashed lines: 321 K; dot-dashed lines: 348 K.

x-ray study of the protein crambin, $^{28}$ where the hydrophobic region of the macromolecule has been found to be surrounded by chains of pentagonal $(H_2O)_5$ clusters (some of which are planar), whose oxygen atoms are separated by ~3.4–3.5 Å from the carbon atoms of the hydrophobic residue; however, as hydrogen atoms are practically undetected by x-ray analysis, it was not possible to establish the nature of $H_2O$ in the pentamer (single/double-donor/acceptor). In our liquid phase simulations, both solvent and temperature-induced effects could account for the departure from the single donor's structure found in the gas phase. The first hydration shell is a dynamical structure, and its cluster subunits are in continuous rearrangement; for example, pentamers like the one shown in Fig. 2 have a mean life of about 0.1 ps before a water molecule breaks both hydrogen bonds with its first neighbors. By increasing the temperature, a decrease of the number of water molecules in the first coordination shell is observed; at 348 K the coordination number reduces to 17 molecules. The comparison between $g_{O_2-H_W}$ and $g_{O_2-O_W}$ shows that the first peak of the $g_{O_2-H_W}$ moves to slightly longer distances than the one of $g_{O_2-O_W}$ as the temperature increases, meaning that the number of water molecules that point their hydrogens toward the bulk is increasing, as found previously for the neon-water system. $^{20}$ This effect, together with the loss of a water molecule, provokes the modification of the first hydration shell structure, as the temperature increases, and suggests that kinetic energy contribution is starting to balance the potential energy gain obtained by intrashell hydrogen bonds. A discontinuity in the solute-solvent $g(r)$'s near 311 K is observed. Such discontinuity seems to be a peculiarity of the first hydration shell only, in fact water-water $g(r)$'s (see Fig. 3) show a progressive smoothing of the peaks only.

![](./images/812730662896271361_4.jpg)

FIG. 2. A typical first hydration shell structure for oxygen, where a planar pentagonal system $(H_2O)_5$ is evidenced by continuous lines. Dotted lines represent hydrogen bonds.

The variation of the coordination number with temperature implies a transfer of a water molecule from the shell to the bulk. Such a transfer causes a change in the relative density of the solvation shell with respect to the bulk. We calculated the water density as a function of the distance

![](./images/812730662896271361_5.jpg)

FIG. 3. Radial distribution functions $g(r)$'s, water's oxygen ($\mathrm{O_w-O_w}$), and water's oxygens with hydrogens ($\mathrm{O_w-H_w}$); solid lines: 291 K; dotted lines: 296 K; dashed lines: 311 K; long-dashed lines: 321 K; dot-dashed lines: 348 K.

from $\mathrm{O_2}$, $\rho(r)=N(r)/V(r)$, where $N(r)$ is the number of $\mathrm{H_2O}$ units in a sphere of radius $r$ from $\mathrm{O_2}$, and $V(r)$ is the volume of the sphere. In Fig. 4, $\rho(r)$'s are shown, where a different behavior as a function of the temperature is evident:
$\rho(r)$ in the first solvation shell is higher than in the bulk for $T$<296 K, while it is lower than in the bulk for $T$>311 K. The two regions, shell and bulk, are separated by a low-density region. Therefore the presence of the apolar gas

![](./images/812730662896271361_6.jpg)

FIG. 4. Density, $\rho$ (in molecules $A^{-3}$), variation in function of distance, $r$ (Å), from solute. The region between 3 and 9 Å is enlarged in the inset. Solid line: 291 K; dotted line: 296 K; dashed line: 311 K; long-dashed line: 321 K; dot-dashed line: 348 K.

![](./images/812730662896271361_7.jpg)

FIG. 5. Charge's distribution function Z(r) around water molecules, solid line: 291 K; dotted line: 296 K; dashed line: 311 K; long-dashed line: 321 K; dot-dashed line: 348 K.

causes oscillations in the water density, generating, at least, one high density shell, a low density one, and then a flat density region that tends to the bulk value of the solution (N/V). Beyond oscillations in density, $H_2O$ being a polar molecule, a different arrangement around the apolar solute with respect to another $H_2O$ molecule may cause local differences in the electrostatic field, which can affect the properties of the solutions. As electrostatic forces are long ranged, these effects may propagate far away from the apolar solute. By inspection of the $O_W-O_W$ and $O_W-H_W$ g(r)'s, shown in Fig. 3, it seems that there is a well-defined distribution of charge around water molecules. $^{29}$ Such charge's distribution must fulfill the electroneutrality condition for which the total charge around a particle $\nu$ must be cancelled by the particle's opposite charge $z_{\nu}$ (charge's sum rule), $^{30}$

$$
-z_{\nu}=\rho \int_{0}^{\infty} 4 \pi r^{2} \sum_{\mu} \chi_{\mu} z_{\mu} g_{\nu \mu}(r) d r,
\tag{1}
$$

where $\rho$ is the density, $\chi_{\mu}$ the concentration, and $z_{\mu}$ the charge of the particle $\mu$, while $g_{\nu \mu}$ is the radial distribution function between $\nu$ and $\mu$. The charges $z_{\mu}$ are the same used in the SPC/E model for water, while they are zero for the $O_2$ molecule. The charge's distribution around a water molecule is shown in Fig. 5, where, for each temperature, the function Z(r) is reported,

$$
Z(r')=\rho \int_{0}^{r'} 4 \pi r^{2} \sum_{\mu=\mathrm{H}_{W}}^{\mathrm{O}_{W}} \chi_{\mu} z_{\mu}\left(g_{\mu \mathrm{O}_{W}}(r)\right)+\left(g_{\mu \mathrm{H}_{W}}(r)\right) d r.
\tag{2}
$$

The same functions,

$$
Z\left(r^{\prime}\right)=\rho \int_{0}^{r^{\prime}} 4 \pi r^{2} \sum_{\mu=\mathrm{H}_{W}}^{\mathrm{O}_{W}} \chi_{\mu} z_{\mu} g_{\mu \mathrm{O}_{2}}(r) d r,
\tag{3}
$$

calculated for the solute molecule $O_2$, are collected in Fig. 6. A solvent's static polarization is observed around the apolar solute: alternating shells of positively and negatively charged layers surround $O_2$; the amplitudes of such oscillations decrease with temperature. A point has to be noticed here, namely, the "static charge" distribution around $O_2$ is qualitatively different from that found around the water molecules.

## DYNAMICAL PROPERTIES

The structural properties of the water molecules in the first hydration shell, different from those in the bulk, may suggest that also their dynamical behavior can be affected by the presence of an apolar solute. Previous simulations $^{31,32}$ and experimental works $^{33,34}$ suggest that both the translational (diffusive) and the reorientational motions of the water molecules are slowed down in the close neighborhood of an apolar molecule, compared to the motion in the bulk (retardation effect). $^{34}$ The clathrate is to be considered as a dynamical structure, with continuous exchanges of water molecules with the bulk. However, it is possible to define an average residence time, namely, the average time a molecule stays in the first hydration shell before it diffuses in the bulk of the solution. In our simulations the residence time result was $\sim 5$ ps. We used this elapsed time to study the dynamical properties of the hydration shell molecules. Correlation functions for such molecules, for example, were calculated in the

![](./images/812730662896271361_8.jpg)

FIG. 6. Charge's distribution function $Z(r)$ around the $\text{O}_2$ solute molecule solid line: 291 K; dotted line: 296 K; dashed line: 311 K; long-dashed line: 321 K: dot-dashed line: 348 K.

following way: a configuration at a reference $t=0$ time was chosen, and the molecules within the first minimum of the $g_{\text{O}_2-\text{O}_w}$ were assigned to the shell. So, with the shell molecules defined, we calculated the various functions for 5 ps, then averages were taken starting from different $t=0$ configurations. The water diffusion coefficients, $D_{\text{O}_w}$ in the bulk and $D_{\text{O}_{Sb}}$ in the shell, calculated from the root-mean-square displacement (rms), by the Einstein relation

$$
D_{\text{rms}}=\frac{1}{6} \lim _{t \rightarrow \infty} \frac{d}{d t}\left\langle\left|R_{i}(t)-R_{i}(0)\right|^{2}\right\rangle \tag{4}
$$

(the limit is intended of 5 ps for the first hydration shell, and the maximum elapsed time for the bulk and for pure liquid) and from the Fourier transform of the velocity autocorrelation function $F(\omega)$ at zero frequency,

$$
D_{\mathrm{VACF}}=\frac{F(\omega=0) K_{B} T}{m}, \tag{5}
$$

where $K_{B}$ is the Boltzmann constant, $T$ the temperature, and $m$ the mass. The diffusion coefficients, calculated in the two ways, are reported in Table II, together with the available experimental values. $^{14}$ The diffusion coefficients are in the sequence

$\text{shell} < \text{bulk} < \text{pure liquid}$,

in agreement with the hypothesis of the retardation effect promoted by the apolar solute. Hb breaking has the main responsibility for diffusion (exchange) of water from shell to bulk and vice versa. We have focused our attention on the breaking of structures like the pentagonal one shown in Fig. 2. We have found that it is a molecule pointing both its hydrogens out of the first shell (e.g., the double acceptor molecule number 4 in Fig. 2) that generally starts the diffusive process toward the bulk. As, however, water molecules

<table>
<caption>TABLE II. Average dynamical properties obtained from simulations of $\text{O}_2$ in water and of pure water at different temperatures. $\langle T\rangle$: temperature; $D_{\text{O}_w}$ and $D_{\text{Sh}}$: diffusive coefficients for bulk and shell calculated from root-mean square: $D_{\text{rms}}$; calculated from velocity autocorrelation functions: $D_{\text{VACF}}$; experimental: $D_{\text{EXP}}$. (Ref. 14), Hb: average number of hydrogen bonds; $\tau$: single-molecule relaxation time (SMOR).</caption>
<thead>
<tr>
<th>$\langle T\rangle$ (K)</th>
<th></th>
<th>$D_{\text{rms}}$ ($10^{-9}$ m² s⁻¹)</th>
<th>$D_{\text{VACF}}$ ($10^{-9}$ m² s⁻¹)</th>
<th>$D_{\text{EXP}}^{\text{a}}$ ($10^{-9}$ m² s⁻¹)</th>
<th>$\tau$ H-bond</th>
<th>$\tau$ (ps)</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="7">Solution</td>
</tr>
<tr>
<td>291</td>
<td>$\text{O}_w$</td>
<td>2.09</td>
<td>2.18</td>
<td>2.1</td>
<td>3.625</td>
<td>5.50</td>
</tr>
<tr>
<td></td>
<td>$\text{O}_{\text{Sh}}$</td>
<td>2.08</td>
<td>1.83</td>
<td></td>
<td>3.615</td>
<td>6.08</td>
</tr>
<tr>
<td>296</td>
<td>$\text{O}_w$</td>
<td>2.25</td>
<td>2.29</td>
<td>2.3</td>
<td>3.604</td>
<td>4.55</td>
</tr>
<tr>
<td></td>
<td>$\text{O}_{\text{Sh}}$</td>
<td>2.21</td>
<td>1.75</td>
<td></td>
<td>3.575</td>
<td>5.41</td>
</tr>
<tr>
<td>311</td>
<td>$\text{O}_w$</td>
<td>3.00</td>
<td>3.33</td>
<td>3.4</td>
<td>3.548</td>
<td>3.63</td>
</tr>
<tr>
<td></td>
<td>$\text{O}_{\text{Sh}}$</td>
<td>3.17</td>
<td>3.03</td>
<td></td>
<td>3.518</td>
<td>3.61</td>
</tr>
<tr>
<td>321</td>
<td>$\text{O}_w$</td>
<td>3.43</td>
<td>3.86</td>
<td>4.2</td>
<td>3.490</td>
<td>3.27</td>
</tr>
<tr>
<td></td>
<td>$\text{O}_{\text{Sh}}$</td>
<td>3.84</td>
<td>3.58</td>
<td></td>
<td>3.463</td>
<td>3.40</td>
</tr>
<tr>
<td>348</td>
<td>$\text{O}_w$</td>
<td>5.24</td>
<td>5.61</td>
<td>6.8</td>
<td>3.463</td>
<td>2.12</td>
</tr>
<tr>
<td></td>
<td>$\text{O}_{\text{Sh}}$</td>
<td>5.59</td>
<td>5.50</td>
<td></td>
<td>3.367</td>
<td>2.47</td>
</tr>
<tr>
<td colspan="7">Pure liquid</td>
</tr>
<tr>
<td>299</td>
<td></td>
<td>2.31</td>
<td>2.63</td>
<td>2.5</td>
<td>3.596</td>
<td>4.45</td>
</tr>
<tr>
<td>323</td>
<td></td>
<td>4.34</td>
<td>4.96</td>
<td>4.4</td>
<td>3.493</td>
<td>3.00</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="7">${}^{\text{a}}$Reference 14.</td>
</tr>
</tfoot>
</table>

are hydrogen bonded to each other, it is the Hb breaking at the origin of the diffusive process. There are two main routes for the breaking of an Hb:

(i) two molecules increase their $O-H\cdots O$ separation until they are no longer linked, then one of them (or both), can diffuse and rotate;

(ii) the $O-H\cdots O$ angle increases till the pair of molecules are no longer hydrogen bonded, so that one of the pair is free to increase the $O\cdots O$ distance and diffuse. We have found that the faster librational motion is the necessary step for the Hb breaking and the successive migration of water from shell to bulk. The Hb dynamics is quantitatively investigated through the hydrogen bond population operator, $h.^{35}$ When the considered pair of water molecules is hydrogen bonded, $h$ is assigned the value of one, and zero otherwise. Two water molecules are considered hydrogen bonded when their interoxygen distance is less then 3.5 A [the range of a water molecule's first coordination shell in the $g(r)$], and simultaneously the $O-H\cdots O$ angle is less than $30^{\circ}.^{36}$ The average number of hydrogen bonds is

$$
\frac{1}{2} N(N-1)\langle h\rangle, \tag{6}
$$

where $\langle h\rangle$ denotes the time average of $h$. The decay properties of the Hb's network can be characterized by the autocorrelation function of $h$,

$$
c(t)=\frac{\langle h(t) \cdot h(0)\rangle}{\langle h\rangle}. \tag{7}
$$

This function represents the probability that a hydrogen bond is intact at time $t$, given it was intact at time zero, and the faster the decay of $c(t)$, the shorter the Hb average lifetime. $^{35}$ The average number of hydrogen bonds is temperature dependent, and is inversely proportional to the temperature; moreover, the average number of hydrogen bonds in the first shell of $O_{2}$ is lower than that in the bulk (see Table II). This finding is confirmed by analyzing the $c(t)$ functions (Fig. 7), whose decay suggests that the hydrogen bond's lifetime in the first shell is shorter than that in the bulk, at the same temperature. However, the difference reduces as temperature increases, as shown in Fig. 7, and nearly vanishes at 348 K. The correlation functions $c(t)$ for both the solution and the pure liquid are shown in Fig. 8. At the highest temperature considered, the Hb lifetimes are nearly equal in both cases. At short times, $\sim 0.1$ ps, a fast decay of $c(t)$ is observed implying that many crosses in and out of the Hb definition area are possible, and, on this time scale, it is the librational motion that governs the dynamics of the Hb equilibrium. After this fast librational relaxation, $c(t)$ exhibits a slower decay, where the diffusional $(O\cdots O$ separation) mechanism becomes relevant in the Hb breaking and forming. Further information on the dynamics in solution can be obtained by the velocity autocorrelation functions (VACF) for both the oxygen $(O_{W})$ and the hydrogen $(H_{W})$ of the water molecules,

$$
f(t)=\frac{\langle\mathbf{v}(t) \cdot \mathbf{v}(0)\rangle}{\langle\mathbf{v}(0) \cdot \mathbf{v}(0)\rangle}, \tag{8}
$$

![](./images/812730662896271361_9.jpg)

FIG. 7. $h$ operator correlation function at different temperature; solid lines: bulk water; dotted lines: first hydration shell.

with its Fourier transform, to give the power spectrum

$$
F(\omega)=K_{B} T \int_{0}^{\infty} \frac{\langle\mathbf{v}(t) \cdot \mathbf{v}(0)\rangle}{\langle\mathbf{v}(0) \cdot \mathbf{v}(0)\rangle} \cos (\omega t) d t. \tag{9}
$$

The power spectra are collected in Fig. 9. Information on the intermolecular vibrational motion can be obtained by analyzing the $O_{W}$ spectra, while the $H_{W}$ spectra give more information on the shorter time librational motion. $^{37}$ The motion of water molecules is hindered by the network of hydrogen bonds; the stronger the Hb the more hindered the motion. The intermolecular vibrations can be decomposed in bending and stretching of the $O\cdots O\cdots O$ units. The bands of VACF power spectra for both $O_{W}$ and $H_{W}$ at about $50 \mathrm{~cm}^{-1}$ are assigned to bending, while the bands at higher frequencies, $\sim 200 \mathrm{~cm}^{-1}$, are assigned to $O\cdots O\cdots O$ stretching. Experimental data (Raman and neutron scattering, and IR) $^{14}$ present bands at $60 \mathrm{~cm}^{-1}$ (bending) and at $170-200 \mathrm{~cm}^{-1}$ (stretching). $^{38}$ The fast librational motion of the $O-H\cdots O$ is associated with the $H_{W}$ VACF broad band from 200 to 1000 $\mathrm{cm}^{-1}$ (maximum at $\sim 500 \mathrm{~cm}^{-1}$ ). As is known, $^{14}$ the librational motion has three components which, in liquid phase, are weak, broad, and nearly overlapping. In particular, the maximum of this band occurs at about $500 \mathrm{~cm}^{-1}$, in accordance with experimental $^{39}$ and theoretical $^{37}$ results as well. The loss in intensities and the lowering of the frequencies of spectral bands as the temperature increases is essentially due to a progressive weakening of the Hb network. The VACF and their relative power spectra for the first hydration shell, bulk water, and pure liquid (data at room temperature are shown in Fig. 10) are quite similar; however, the shell's bands are moderately shifted to higher frequencies, and this

![](./images/812730662896271361_10.jpg)

FIG. 8. $h$ operator correlation function for the solutions at 296 (solid line) and 321 K (dashed line); and for the pure liquid at 299 (dotted line) and 323 K (long-dashed line).

![](./images/812730662896271361_11.jpg)

FIG. 9. Power spectra of the velocity autocorrelation functions for water molecules in solution at different temperature $F(\omega)$; solid lines: 291 K; dotted lines: 296 K; dashed lines: 311 K; long-dashed lines: 321 K; dot-dashed lines: 348 K.

![](./images/812730662896271361_12.jpg)

FIG. 10. Power spectra of the velocity autocorrelation functions for water molecules around room temperature $F(\omega)$; solid line: solution (296 K); dotted line: pure water (299 K); dashed line: shell's water (296 K).

shift indicates stronger interactions among water molecules near an apolar solute, in agreement with the hypothesis for which an apolar solute is a structure making molecules. An- other way to look at the dynamics in molecular liquids is the study of the orientational motion. $^{40}$ We calculated the single molecule orientation relaxation (SMOR) $^{41,42}$ defined by

$$
\phi(t)=\frac{\langle\boldsymbol{\mu}(t) \cdot \boldsymbol{\mu}(0)\rangle}{\langle\boldsymbol{\mu}(0) \cdot \boldsymbol{\mu}(0)\rangle}, \tag{10}
$$

where $\boldsymbol{\mu}$ is the dipole moment of a $H_{2}O$ molecule. The re- laxation times $\tau$, in Table II, are calculated assuming a Debye-type mechanism of the dielectric relaxation [exponen- tial decay of the correlation functions $\propto \exp(-t/\tau)$]. The re- laxation functions $\phi(t)$, for solutions at different tempera- tures, are collected in Fig. 11. The initial part of decay, on a time scale of about 0.1 ps, is in the region of the fast libra- tional motion. Higher relaxation time involves hindered dy- namics in agreement with the retardation effect promoted by the apolar solutes. Most of these findings can be related to the high density region that surrounds the solute, indeed, as water density in the shell and in the bulk get closer, dynami- cal properties in the two regions also get closer.

## DISCUSSION AND CONCLUSIONS

In the last decades the understanding of hydrophobic hy- dration on atomic length scales has been widely investigated by different theoretical approaches. $^{24,43-52}$ Moreover, the scaled-particle theory, $^{43-45}$ which provides a basis for widely used phenomenological models, provides a connection to mesoscopic and macroscopic phenomena.

The main target of our paper is to provide new micro- scopic information in order to check or improve available theories. The present results obtained by the simulations of dilute solutions of $O_{2}$ in water in the temperature range 291348 K, put in evidence some points:

(i) quasiplanar water clusters are stabilized by an apolar gas in its first hydration shell;
(ii) density and charge oscillations are generated in water in the neighborhood of an apolar gas;
(iii) stronger interactions among water molecules are pro- moted by an apolar gas;
(iv) the differences between shell and bulk water are smoothed by increasing temperature.

Can these findings help to better understand the hydrophobic phenomena?

First of all, the two-dimensional structures found both in computer simulations studies and in x-ray studies of biomol- ecules may account for the negative entropic contribution in the hydrophobic hydration.

Another peculiar property of the dilute solution of apolar gases in water is the lowering of their solubility with tem- perature. The unusual hydrophobic temperature dependence appears to be tied to the behavior of the isothermal com- pressibility for pure water at low pressures; $^{20,46,49,50}$ again, our effort is mainly addressed to a molecular level descrip- tion of such behavior. It has been suggested (see, for ex- ample, the review of P. M. Wiggins $^{53}$ ) that the affinity of apolar substances to water is proportional to water density: the higher the density the higher the affinity, and high- density water regions have been proposed to surround apolar

![](./images/812730662896271361_13.jpg)

FIG. 11. Single-molecule reorientational relaxation functions $\phi(t)$ for water molecules in solution at different temperature: solid line: 291 K; dotted line: 296 K; dashed line: 311 K; long-dashed line: 321 K; dot-dashed line: 348 K. The inset contains the $\phi(t)$'s short time behavior in the region between 0 and 0.1 ps on an enlarged scale.

residues in biomolecules. This hypothesis can be rationalized in molecular terms by thinking of the kind of interactions involved between polar water molecules and apolar groups. Such interactions are essentially London dispersion and dipole-induced dipole forces, which are short ranged and proportional to the water density, but we believe that such forces alone are not enough to explain the phenomenon, because water-water interactions also are density dependent. Indeed, it has been found that an apolar solute promotes stronger water-water interactions in the first shell region than in the bulk, $^{21}$ and this is confirmed by the more hindered water dynamics in the high-density region. The fact that water density decreases with temperature nearby the apolar solute faster than the overall $(N/V)$ density may explain the trend of $O_{2}$ solubility with temperature. The drop in water density with increasing temperature may be related to the results of two recent computer simulations:

(i) "...methane particles in water show the existence of a tendency for aggregation of these solutes which increases with temperature..." $^{6}$ At low temperature we found a minimum, see Table II, in the solute-solvent interaction energy; such energy rises rapidly with the transfer of a water molecule to the bulk, showing higher affinity of an apolar solute to high-density water. As temperature increases, the drop in density in the vicinity of the solute weakens such interactions and, together with the weakening of water-water interactions, may promote the apolar solutes clustering, eventually favoring the phase separation of the gas.

(ii) "...density of water molecules is shown to be drastically depressed at the (hydrophobic) monolayer-water interface when the monolayer separation is fully increased..." $^{54}$ The latter authors found, in a study of water confined between hydrophobic walls, a drop in water density at the interfaces with increasing inter-wall separation. Even if they do not discuss the origin of such density depression, they ascribe the generation of an attractive surface-surface force (hydrophobic interactions) to the transfer of water from the interface region to the bulk. This addresses the discussion of another important issue in hydrophobic phenomena, their long-range behavior, $^{55-57}$ namely the fact that the presence of an apolar solute is "felt'' far away from its localization. Therefore, in principle, one needs long-ranged forces. The results of our simulations show that the presence of an apolar solute alters the electrostatic charge distribution with respect to pure liquid water, and as electrostatic interactions are long ranged, this study shows a possible origin for such forces.

$^{1}$F. Franks, in *Water: A Comprehensive Treatise*, edited by F. Franks (Plenum, New York, 1973), Vol. 2.
$^{2}$F. Franks, in *Water: A Comprehensive Treatise*, edited by F. Franks (Plenum, New York, 1975), Vol. 4.
$^{3}$N. Muller, Acc. Chem. Res. **23**, 23 (1990).
$^{4}$L. R. Pratt, Annu. Rev. Phys. Chem. **36**, 433 (1985).
$^{5}$T. Head-Gordon, Proc. Natl. Acad. Sci. USA **92**, 8308 (1995).
$^{6}$R. L. Mancera, A. D. Buckingham, and N. T. Skipper, J. Chem. Soc., Faraday Trans. **93**, 2263 (1997).

$^{7}$M. P. Allen and D. J. Tildesley, *Computer Simulation of Liquids* (Oxford Science, Oxford, 1987).

$^{8}$M. H. Abraham, J. Am. Chem. Soc. **104**, 2085 (1982).

$^{9}$D. Eisenberg and W. Kauzmann, *The Structure and Properties of Water* (Clarendon, Oxford, 1969).

$^{10}$H. S. Frank and M. W. Evans, J. Chem. Phys. **13**, 507 (1945).

$^{11}$H. J. C. Berendsen, J. R. Grigera, and T. P. Straatsma, J. Phys. Chem. **91**, 6269 (1987).

$^{12}$E. Fois, A. Gamba, G. Morosi, P. Demontis, and G. B. Suffritti, J. Chim. Phys. **84**, 751 (1987).

$^{13}$H. C. Andersen, J. Comput. Chem. **52**, 24 (1982).

$^{14}$G. S. Kell, in *Water: A Comprehensive Treatise*, edited by F. Franks (Plenum, New York, 1972), Vol. 1.

$^{15}$G. Hummer and S. Garde, Phys. Rev. Lett. **80**, 4193 (1998).

$^{16}$J. C. Owiki and H. A. Scheraga, J. Am. Chem. Soc. **99**, 7403 (1977); **99**, 7413 (1977).

$^{17}$S. Swaminathan, S. W. Harrison, and D. L. Beveridge, J. Am. Chem. Soc. **100**, 5705 (1978).

$^{18}$G. Alagona and A. Tani, J. Chem. Phys. **72**, 580 (1980).

$^{19}$E. Fois, A. Gamba, G. Morosi, P. Demontis, and G. B. Suffritti, Mol. Phys. **58**, 65 (1986).

$^{20}$B. Guillot and Y. Guissani, J. Chem. Phys. **99**, 8075 (1993).

$^{21}$E. Fois, A. Gamba, and G. Morosi, Gazz. Chim. Ital. **126**, 729 (1996).

$^{22}$P. H. K. De Jong, J. E. Wilson, G. W. Neilson, and A. D. Buckingham, Mol. Phys. **91**, 99 (1997).

$^{23}$A. Filipponi, D. T. Bowron, C. Lobban, and J. L. Finney, Phys. Rev. Lett. **79**, 1293 (1997).

$^{24}$L. R. Pratt and D. Chandler, J. Chem. Phys. **67**, 3683 (1977); **73**, 3430 (1980); **73**, 3434 (1980); Methods Enzymol. **127**, 48 (1985).

$^{25}$D. W. Davidson, in *Water: A Comprehensive Treatise*, edited by F. Franks (Plenum, New York, 1973), Vol. 2.

$^{26}$T. H. Head-Gordon, J. M. Sorenson, A. Pertsemlidis, and R. M. Glaeser, Biophys. J. **73**, 2106 (1997).

$^{27}$N. R. Pribble and T. S. Zwier, Science **265**, 265 (1994).

$^{28}$M. M. Teeter, Proc. Natl. Acad. Sci. USA **81**, 6014 (1984).

$^{29}$D. Bressanini, E. Fois, A. Gamba, and G. Morosi, Chem. Phys. Lett. **200**, 333 (1992).

$^{30}$J. P. Hansen and I. R. McDonald, *Theory of Simple Liquids* (Accademic, London, 1986).

$^{31}$P. J. Rossky and M. Karplus, J. Am. Chem. Soc. **101**, 1913 (1979).

$^{32}$A. Laaksonen and P. Stilbs, Mol. Phys. **74**, 747 (1991).

$^{33}$M. Holz, R. Haselmeier, R. K. Mazitov, and H. Weingartner, J. Am. Chem. Soc. **116**, 801 (1994).

$^{34}$R. Haselmeier, M. Holz, W. Marbach, and H. Weingartner, J. Phys. Chem. **99**, 2243 (1995).

$^{35}$A. Luzar and D. Chandler, Phys. Rev. Lett. **76**, 928 (1996).

$^{36}$J. Teixeira, M. C. Bellisent-Funel, and S. H. Chen, J. Phys.: Condens. Matter **105**, 2 (1990).

$^{37}$R. W. Impey, P. A. Madden, and I. R. McDonald, Mol. Phys. **46**, 513 (1982).

$^{38}$J. B. Hasted, S. K. Husain, F. A. M. Frescura, and J. R. Birch, Chem. Phys. Lett. **118**, 622 (1985).

$^{39}$G. E. Walrafen, in *Water: A Comprehensive Treatise*, edited by F. Franks (Plenum, New York, 1972), Vol. 1.

$^{40}$P. A. Madden, in *Liquids, Freezing and Glass Transition*, edited by J. P. Hansen, D. Levesque, and J. Zinn-Justin (Elsevier Science, London, 1991).

$^{41}$M. Neumann, J. Chem. Phys. **85**, 1567 (1986).

$^{42}$I. Ohmine, J. Phys. Chem. **99**, 6767 (1995).

$^{43}$H. Reiss, Adv. Chem. Phys. **9**, 1 (1965).

$^{44}$F. H. Stillinger, J. Solution Chem. **2**, 141 (1973).

$^{45}$R. A. Pierotti, Chem. Rev. **76**, 717 (1976).

$^{46}$A. Pohorille and L. R. Pratt, J. Am. Chem. Soc. **112**, 50,566 (1990).

$^{47}$T. Lazaridis and M. E. Paulaitis, J. Phys. Chem. **96**, 3847 (1992).

$^{48}$D. Chandler, Phys. Rev. E **48**, 2898 (1993).

$^{49}$G. Hummer, S. Garde, A. E. Garcia, A. Pohorille, and L. R. Pratt, Proc. Natl. Acad. Sci. USA **93**, 8951 (1996).

$^{50}$S. Garde, G. Hummer, A. E. Garcia, M. E. Paulaitis, and L. R. Pratt, Phys. Rev. Lett. **77**, 4966 (1996).

$^{51}$A. D. J. Haymet, K. A. T. Silverstein, and K. A. Dill, Faraday Discuss. **103**, 117 (1996).

$^{52}$K. A. T. Silverstein, A. D. J. Haymet, and K. A. Dill, J. Am. Chem. Soc. **120**, 3166 (1998).

$^{53}$P. M. Wiggins, Physica A **238**, 113 (1997).

$^{54}$M. Sakurai, H. Tamagawa, A. Ariga, T. Kunitake, and Y. Inoue, Chem. Phys. Lett. **289**, 567 (1998).

$^{55}$P. Attard, J. Phys. Chem. **93**, 6441 (1989).

$^{56}$Y. H. Tsao, D. F. Evans, and H. Wennerstrom, Langmuir **9**, 779 (1993).

$^{57}$J. Forsman, B. Jonsson, C. E. Woodward, and H. Wennerstrom, J. Phys. Chem. B **101**, 4253 (1997).