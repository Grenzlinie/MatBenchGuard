This article was downloaded by: [DTU Library]
On: 29 April 2014, At: 06:49
Publisher: Taylor & Francis
Informa Ltd Registered in England and Wales Registered Number: 1072954
Registered office: Mortimer House, 37-41 Mortimer Street, London W1T 3JH, UK

![](./images/811981060844814338_1.jpg)

# Philosophical Magazine A
Publication details, including instructions for authors and
subscription information:
http://www.tandfonline.com/loi/tpha20

## Atomistic simulation of cross-slip processes in model fcc structures
S. Rao $^{a}$ , T. A. Parthasarathy $^{a}$ \& C. Woodward $^{b}$

$^{a}$ Materials Directorate, Wright Laboratory, Wright-Patterson Air Force Base, Ohio, 45433, USA
$^{b}$ UES Inc, 4401 Dayton-Xenia Rd, Dayton, Ohio, 45432, USA
Published online: 12 Aug 2009.

To cite this article: S. Rao, T. A. Parthasarathy & C. Woodward (1999) Atomistic simulation of cross-slip processes in model fcc structures, Philosophical Magazine A, 79:5, 1167-1192, DOI:
10.1080/01418619908210354

To link to this article: http://dx.doi.org/10.1080/01418619908210354

PLEASE SCROLL DOWN FOR ARTICLE

Taylor & Francis makes every effort to ensure the accuracy of all the information (the "Content") contained in the publications on our platform. However, Taylor & Francis, our agents, and our licensors make no representations or warranties whatsoever as to the accuracy, completeness, or suitability for any purpose of the Content. Any opinions and views expressed in this publication are the opinions and views of the authors, and are not the views of or endorsed by Taylor & Francis. The accuracy of the Content should not be relied upon and should be independently verified with primary sources of information. Taylor and Francis shall not be liable for any losses, actions, claims, proceedings, demands, costs, expenses, damages, and other liabilities whatsoever or howsoever caused arising directly or indirectly in connection with, in relation to or arising out of the use of the Content.

This article may be used for research, teaching, and private study purposes. Any substantial or systematic reproduction, redistribution, reselling, loan, sub-licensing, systematic supply, or distribution in any form to anyone is expressly forbidden.
Terms & Conditions of access and use can be found at http://www.tandfonline.com/page/terms-and-conditions

PHILOSOPHICAL MAGAZINE A, 1999, VOL. 79, No. 5, 1167-1192

# Atomistic simulation of cross-slip processes in model fcc structures

S. RAO, T. A. PARTHASARATHY

Materials Directorate, Wright Laboratory, Wright-Patterson Air Force Base,
Ohio 45433, USA

and C. WOODWARD

UES Inc, 4401 Dayton-Xenia Rd, Dayton, Ohio 45432, USA

[Received 21 April 1998 and accepted in revised form 23 July 1998]

## ABSTRACT
Three-dimensional cross-slipped core structures of $(a / 2)[110]$ screw dislocations in model fcc structures are simulated using lattice statics within the embedded-atom method (EAM) formalism. Two parametric EAM potentials fitted to the elastic and structural properties of fcc $Ni$ were used for the simulations. The two- and three-dimensional Green's function techniques newly developed by Rao et al. are used to relax the boundary forces in the simulations. Core structures and energetics of the constrictions occurring in the cross-slip process are studied. The core structure of the constrictions are diffuse, as opposed to a point constriction as envisaged by Stroh. The two constrictions formed by cross-slip onto a cross $\{111\}$ plane have significantly different energy profiles, at variance with classical continuum theory of Stroh. This suggests that self-stress forces and atomistics dominate the energetics of the cross-slip process; the far-field elastic-energy contribution to cross-slip appears to be minimal. However, the Shockley partial separation distances near the constrictions as well as the variation in cross-slip energy with stacking-fault energy are in reasonable agreement with continuum predictions. Cross-slip energies estimated for $Cu$ and $Ni$ from these calculations show reasonable agreement with experimental data. The cross-slip energy shows a significantly weaker dependence on the Escaig stress compared with elasticity calculations. The activation volume for the cross-slip process is estimated to be of the order of $20 b^{3}$ at an applied Escaig stress of $10^{-3} \mu$ in $Cu$ , an order of magnitude lower than experimental estimates and continuum predictions.

## §1. INTRODUCTION
Cross-slip plays an important role in the plastic deformation of metallic materials. It is considered to be the mechanism through which screw-dislocation segments annihilate each other and form low-energy structures in deformation processes such as work hardening, fatigue and creep (Jackson 1985). Cross-slip of screw dislocations between different glide planes is thought to result in the formation of glide-plane obstacles in hcp metals and $L_{2}-, B 2$ - and $L_{0}$ -based intermetallic alloys, giving rise to the high-temperature yield-stress peak (Paidar et al. 1984, Couret and Caillard1988, Dimiduk 1991, Greenberg et al. 1991, Louchet and Viguier 1995). Cross-slip can also act to weaken materials by allowing the bypass of obstacles in dispersion- hardened structures such that the Orowan limit is not achieved (Humphreys and Hirsch 1970).

0141-8610/99 $12.00  1999 Taylor & Francis Ltd.

Several different mechanisms have been proposed for cross-slip in fcc materials (Schoeck and Seeger 1955, Fleischer 1959, Escaig 1968). Some of these mechanisms have been described recently by Duesbery *et al.* (1991). Different mechanisms of cross-slip have been suggested in the literature for screw dislocations dissociated into Shockley partials in both fcc as well as hcp materials.

The Shoeck–Seeger (1955) mechanism assumes that the original dislocation, dissociated into Shockley partials in the glide plane, has to recombine over a significant portion of its length and then bow out to a critical configuration in the cross-slip planes (figure 1 (a) and (b)). The critical stresses in this mechanism are the glide

![](./images/811981060844814338_2.jpg)

Figure 1. Schematic diagrams of cross-slip process according to different proposed mechanisms: (a), (b) the Seeger–Schoeck mechanism; (c) the Friedel mechanism; and (d) the Stroh-type constriction.

stress in the cross-slip plane and the resolved glide stress in the glide plane, if the recombination occurs at an obstacle. In this mechanism, the activation enthalpy for the cross-slip event has four different contributions: the energy of the two constric- tions, the energy of recombination of partial dislocations over a significant length, the energy of the bowed-out loop in the cross-slip plane, and the negative of the work done by the resolved glide stresses in the cross-slip as well as glide planes. Friedel (1957) suggested that the energy of the bowed out-loop significantly decreases if the dislocation is allowed to redissociate in the cross-slip plane as was also recognized by Schoeck and Seeger (see figure 1 of Schoeck and Seeger (1955)). As soon as redis- sociation enters into the picture (figure 1(c)), the cross-slip process can be purely thermally activated without any applied stresses, since the interaction between the constrictions is weak at large separation distances. Another mechanism of cross-slip has been proposed by Fleischer (1959), which is significantly different from either the Seeger-Schoeck or the Freidel-Escaig mechanistic description of cross-slip. We shall not consider Fleischer's mechanism in this paper since it is beyond the scope of this work.

According to the Friedel-Escaig mechanism of cross-slip, as soon as a Stroh-type constriction (figure 1(d)) forms on the glide plane owing to thermal activation, the dislocation at the constriction point can immediately redissociate in the cross-slip plane and expand (Stroh 1954). Activation enthalpies and volumes calculated using the Friedel-Escaig mechanism seem to be in fair agreement with experimental data in fcc materials (Bonneville and Escaig 1979). Recent continuum calculations based on the self-stress method also indicate that the Friedel-Escaig mechanism is in fair agreement with experimental data on cross slip in fcc Cu (Duesbery *et al.* 1991).

Early theoretical treatments of cross-slip of $(a/2)[110]$ screw dislocations in fcc-based structures were mostly performed using continuum elasticity theory within the line tension approximation (Stroh 1954, Schoeck and Seeger 1955, Friedel 1957, Escaig 1968, Bonneville and Escaig 1979). The treatment of the constriction was done within the Stroh (1954) approximation of a point constriction. The classical treatment of the point constriction by Stroh was recently reevaluated by Saada (1991). Saada generalized Stroh's treatment by removing the point constriction from the analysis and introducing a finite distance of $b$, $2b$ or $3b$ as the recombina- tion distance for the Shockley partials. The constriction energy is significantly reduced by this modification when the initial separation distance between Shockley partials is small. Recently, the cross-slip of $(a/2)[110]$ screw dislocations dissociated into $(a/6)\langle 112\rangle$-type Shockley partials has been treated within the more accurate self-stress approximation of continuum elasticity theory (Puschl 1990, Duesbery *et al.* 1991, Puschl and Schoeck 1993). Duesbery *et al.* (1991) performed a complete three-dimensional (3D) isotropic elasticity treatment of the structure and energetics of the cross-slipped configuration as a function of the separation length $\lambda$ between the two constriction points in the cross-slipped configuration (see figure 2). The effect of an applied Escaig stress on the cross-slip plane (glide stress on the edge components of the Shockley partials in the cross-slip plane) for the structure and energetics of the cross-slipped configurations were also considered. Similar calcula- tions were performed by Puschl and Schoeck (1993) using anisotropic elasticity theory combined with a two-dimensional (2D) Peierls model (Seeger and Schoeck 1953) for the core of the $(a/2)\langle 110\rangle$ and $(a/6)\langle 112\rangle$ type Shockley partials in fcc structures. However, the continuum treatment of the cross-slip process is performed as a sequence of two 2D calculations rather than a direct 3D calculation.

![](./images/811981060844814338_3.jpg)

Figure 2. A schematic picture of the cross-slipped configurations considered in the 3D con- tinuum study of the structure and energetics of cross-slip in a fcc material (Duesbery et al. 1991).

In most of these continuum calculations an arbitrary core radius ($b$ or $2b$) has to be assumed as the distance of separation at which the two Shockley partials are considered to have recombined into a perfect $(a/2)\langle 110\rangle$ screw dislocation. Puschl and Schoeck (1993) obtain a value of $0.15b$ for the core radius based on comparison with a 2D Peierls model for the core of the individual Shockley partials as well as the combined $(a/2)\langle 110\rangle$ screw dislocation. The energy of the cross-slipped configura- tion is significantly affected by the choice of the core radius, especially when the original separation distance between Shockley partials in the unconstricted config- uration is relatively small (i.e. materials with a large stacking-fault energy) (Saada 1991, Duesbery et al. 1991). Larger values for the core radius result in a lower value for the cross-slip energy. As a result of the various approximations in the continuum calculations, the published cross-slip energies for an identical initial separation dis- tance between Shockley partials in the unconstricted configuration can vary by a factor of almost four (Puschl and Schoeck 1993). The recent self-stress treatments of the energetics of the cross-slip process give significantly higher formation energy values compared with the earlier more approximate line tension treatments (Puschl and Schoeck 1993, Duesbery et al. 1991).

Considering the influence of cross-slip processes on material properties, and the significant difficulties that one encounters in a continuum treatment of the problem, more accurate treatments of this fundamental problem are needed. This is especially true with the recent attempts to simulate dislocation dynamics. Recent 2D and 3D simulations of dislocation dynamics on the mesoscopic scale (Kubin et al. 1992, Mills and Chrzan 1992, Devincre et al. 1997) are completely dependent upon reliable input data or 'rules' for cross-slip conditions. Calculations of the cross-slip process at the atomistic level should be very useful and may give new insights into the problem. Proper treatment of the Friedel-Escaig process of cross-slip in fcc structures requires atomistic simulations of 3D configurations of dislocations, in contrast with standard 2D simulations of infinite straight dislocations. Very few 3D atomistic simulations of dislocation configurations have been published to date (Duesbery 1983, Parthasarathy et al. 1993, Bulatov et al. 1995, Parthasarathy and Dimiduk 1996, Rasmussen et al. 1997a,b, Rao et al. 1998, Simmons et al. 1998). Standard techni- ques require a large simulation cell which would involve a large number of atoms (about 100000). This has made such simulations problematic. However, with the advent of faster computers, new methods such as more reliable interatomic

potentials based on the embedded-atom method (EAM) for fcc materials (Daw and Baskes 1984, Finnis and Sinclair 1994), and the 3D lattice Green's function (GF) method to establish the cell boundary conditions (Rao *et al.* 1998), these simulations become feasible. To date, 3D atomistic simulations of dislocation activation pro- cesses using empirical interatomic potentials have been performed for single kinks and kink pairs in the bcc structures K and Fe (Duesbery 1983), as well as the diamond-cubic structure Si (Bulatov *et al.* 1995). 3D atomistic simulation studies, using empirical EAM potentials, have also been performed of the structure and mobility of single kinks in B2 NiAl and $Ll_{0}$ TiAl (Parthasarathy *et al.* 1993, Simmons *et al.* 1998), dislocation glide barriers or Paidar-Pope-Vitek (PPV) locks in $Ll_{2} Ni_{3} Al$ (Parthasarathy and Dimiduk 1996) as well as the structure and ener getics of the cross-slip of screw dislocations in fcc Cu (Rasmussen *et al.* 1997a,b).

Parthasarathy and Dimiduk (1996) estimated the activation energy for nuclea- tion of cross-slip PPV locks of heights $b / 2$ and $b$ in fcc-based $Ll_{2} Ni_{3} Al$ using 3D atomistic simulations, employing fixed boundary conditions along the radius direc- tion and periodic boundary conditions along the dislocation line direction. The constrictions occurring in the cross-slip process were simulated in pairs at various separation distances. Rasmussen *et al.* (1997a,b) determined the activation energy and activation length for cross-slip via the Friedel-Escaig mechanism in fcc Cu employing fixed boundary conditions along the dislocation line direction and free surface boundary conditions along the other two perpendicular directions. They show that the two constrictions occurring in the cross-slip process are not equivalent with each other, and that one of the constrictions has a negative formation energy.

In this study, a 3D atomistic simulation technique combining molecular statics and GF methods is used to determine self-consistently the appropriate 3D boundary conditions for a general dislocation configuration. This method has been used pre- viously to simulate kinks in bcc Fe (Rao *et al.* 1998). The incompatibility stresses that arise at the boundary of the simulation cell during the atomistic relaxation procedure are relaxed using the GF technique. This allows an atomistic study of cross-slip without any boundary interactions. The boundary conditions of the simu- lations are such that the Friedel-Escaig mechanistic description of the cross-slip process is obtained after atomistic relaxation. The constrictions occurring in the cross-slip process are simulated individually as well as in pairs. This allows a deter- mination of the formation energies of the constrictions, as well as their interaction energies. The empirical EAM potential developed for fcc Ni by Voter and Chen (1987) is used in most of the calculations. In addition, another EAM potential for fcc Ni, with a higher stacking-fault energy, is used to study the cross-slip energy as a function of the initial width of separation between Shockley partials in the uncon- stricted configuration. The atomistic simulations are performed in both the unstressed as well as the stressed states. For the calculations with an applied stress, a general state of stress is applied such that there is no resolved Escaig stress on the cross-slip plane but an Escaig stress extending the Shockley partials on the glide plane exists. The results of the atomistic simulations are compared with continuum calculations of cross-slip in fcc-based structures as well as experimental data.

## §2. POTENTIALS

In most of the atomistic simulations to be described below, we use the empirical potential developed for fcc Ni by Voter and Chen (1987), which we label the Ni(1)

potential. Within the EAM format, the energy of an ensemble of atoms is written as a sum of a pair interaction and a local volume-dependent embedding term as†

$$
E = \sum_{i} E_{i} = \sum_{i,j,\neq j} V_{ij}(R_{ij}) + \sum_{i} F_{i}(\rho_{i}), \tag{1}
$$

where $V_{ij}$ and $F_{i}$ are the pair interaction and embedding terms respectively. The argument $\rho_{i}$ of the embedding term is taken to be a sum of pairwise terms as

$$
\rho_{i} = \sum_{j} \phi_{j}(R_{ij}). \tag{2}
$$

The form of the pair interaction term is taken to be a Morse potential (Voter and Chen 1987), the function $\phi$ is taken to be an exponentially decreasing function with distance, and the embedding function is obtained from an exact fit to the equation of state (obtained by Rose *et al.* (1984)). A given EAM potential is defined by varying the various Morse potential parameters, as well as the parameter which describes the rate of decay of the function $\phi$ with distance to fit the properties of fcc Ni (Voter and Chen 1987).

For a parametric study of the constriction energy as a function of the separation between Shockley partials in the unconstricted configuration, another EAM potential Ni(2) was developed for fcc Ni within the Voter–Chen format. The various parameters which describe the Voter–Chen EAM Ni(1) potential for fcc Ni as well as the Ni(2) potential for fcc Ni are given in table 1. A comparison of the properties of Ni given by the two Ni potentials shown in table 2 indicates that the EAM potentials give almost identical properties, excepting for the stacking-fault energy which changes from $58\ \mathrm{mJ}\,\mathrm{m}^{-2}$ for the Ni(1) potential to $119\ \mathrm{mJ}\,\mathrm{m}^{-2}$ for the Ni(2) potential.

Elasticity calculations, as well as current atomistic simulations, predict a disso- ciation of the $(a/2)[110]$ screw dislocation into two Shockley partials as

$$
\frac{a}{2}[110] = \frac{a}{6}[121] + \frac{a}{6}[21\bar{1}]. \tag{3}
$$

The elasticity calculations of the separation distance between Shockley partials scaled by the Burgers vector $d/b$ were obtained using the relation

$$
\frac{d}{b} = \frac{b}{8\pi\gamma_{\mathrm{sf}}} \left( \frac{K_{\mathrm{s}} - K_{\mathrm{e}}}{3} \right), \tag{4}
$$

Table 1. Parameters used to generate EAM potentials Ni(1) and Ni(2) for fcc Ni within the Voter–Chen (1987) format.

<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Value for Ni(1)</th>
      <th>Value for Ni(2)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$D_{\mathrm{m}}$ (eV)</td>
      <td>1.533 5</td>
      <td>1.758 8</td>
    </tr>
    <tr>
      <td>$R_{\mathrm{m}}$ (nm)</td>
      <td>0.220 53</td>
      <td>0.215 51</td>
    </tr>
    <tr>
      <td>$\alpha_{\mathrm{m}}$ ($\mathrm{nm}^{-1}$)</td>
      <td>17.728</td>
      <td>15.453</td>
    </tr>
    <tr>
      <td>$\beta$ ($\mathrm{nm}^{-1}$)</td>
      <td>36.408</td>
      <td>34.950</td>
    </tr>
    <tr>
      <td>$R_{\mathrm{cut}}$ (nm)</td>
      <td>0.478 95</td>
      <td>0.48318</td>
    </tr>
  </tbody>
</table>

† Note that a factor of $\frac{1}{2}$, which is usually written before the pair potential term explicitly, to take into account of double counting is folded into the expression for $V$ in equation (1).

**Table 2.** Various structural and elastic properties given by the EAM potentials Ni(1) and Ni(2) for fcc Ni. $a_0$ and $E_\text{c}$ are the lattice parameter and cohesive energy per atom respectively; $C_{11}$, $C_{12}$ and $C_{44}$ are the cubic elastic constants; $E_\text{v}$ is the vacancy formation energy and $E_\text{sf}$ is the stacking-fault energy. $E_\text{bcc}$ and $E_\text{hcp}$ are the cohesive energies per atom of bcc and hcp unit cells of Ni.

<table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Value for Ni(1)</th>
      <th>Value for Ni(2)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$a_0$ (nm)</td>
      <td>0.352</td>
      <td>0.352</td>
    </tr>
    <tr>
      <td>$E_\text{c}$ (eV)</td>
      <td>4.45</td>
      <td>4.45</td>
    </tr>
    <tr>
      <td>$C_{11}(10^{12}\ \text{dyn}\,\text{cm}^{-2})$</td>
      <td>2.44</td>
      <td>2.44</td>
    </tr>
    <tr>
      <td>$C_{12}(10^{12}\ \text{dyn}\,\text{cm}^{-2})$</td>
      <td>1.49</td>
      <td>1.49</td>
    </tr>
    <tr>
      <td>$C_{44}(10^{12}\ \text{dyn}\,\text{cm}^{-2})$</td>
      <td>1.25</td>
      <td>1.19</td>
    </tr>
    <tr>
      <td>$E_\text{v}$ (eV)</td>
      <td>1.60</td>
      <td>1.83</td>
    </tr>
    <tr>
      <td>$E_\text{sf}(\text{mJ}\,\text{m}^{-2})$</td>
      <td>58</td>
      <td>119</td>
    </tr>
    <tr>
      <td>$E_\text{bcc}-E_\text{c}(\text{eV}\,\text{atom}^{-1})$</td>
      <td></td>
      <td>0.091</td>
    </tr>
    <tr>
      <td>$E_\text{hcp}-E_\text{c}(\text{eV}\,\text{atom}^{-1})$</td>
      <td></td>
      <td>0.010</td>
    </tr>
  </tbody>
</table>

**Table 3.** The Shockley-partial spacing $d/b$ for the two Ni potentials Ni(1) and Ni(2). Both atomistic and elasticity results are given.

<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="2">$d/b$</th>
    </tr>
    <tr>
      <th></th>
      <th>Atomistic</th>
      <th>Elastic</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Ni(1)</td>
      <td>7.8</td>
      <td>6.1</td>
    </tr>
    <tr>
      <td>Ni(2)</td>
      <td>5.2</td>
      <td>3.0</td>
    </tr>
  </tbody>
</table>

where $K_\text{s}$ and $K_\text{e}$ are functions of the elastic constants (Hirth and Lothe 1982) and $\gamma_\text{sf}$ is the stacking-fault energy. The equilibrium distances of this spreading are given in table 3 for both the Ni potentials. The scaled separation distance between Shockley partials in the unconstricted configuration is $d/b=6.0$-$7.5$ and $d/b=3.0$-$5.0$ for Ni(1) and Ni(2) respectively. Note the deviation of the continuum computation, particularly for the Ni(2) potential, which has a high $\gamma_\text{sf}$. The two potentials were used to study the cross-slip energy as a function of $d/b$ and to compare the atomistic results with continuum calculations.

## §3. GREEN'S FUNCTION BOUNDARY CONDITIONS

The simulations presented in this paper include systems with and without periodic symmetry along the dislocation axis. The flexible boundary conditions used to describe these 2D and 3D systems are based on the lattice GF method (Rao *et al.* 1998). In 2D simulation cells, the incompatibility forces that build up at the boundary between the atomistic and GF regions are relieved by displacing all the atoms within the simulation cell according to the GF solution

$$
u_{i}^{m}=\sum_{j,n}G_{ij}^{mn}(R_{mn})f_{j}^{n}, \tag{5}
$$

where the indices m, n denote atoms, the indices i, j denote the Cartesian components, and $\mathbf{R}_{mn}=\mathbf{R}_{n}-\mathbf{R}_{m}$. When $R_{mn}>R_0$, the elastic GF of the perfect lattice, appropriate for line forces, is used as an approximation to $G_{kj}^{mn}$ (Stroh 1962, Bacon *et al.* 1979). Since the elastic GF diverges at short distances ($R_{mn}<R_0$) the lattice GF

of the perfect lattice is used as an approximation to $\mathbf{G}$. The lattice GF of the perfect lattice is calculated using a simple numerical procedure described by Rao et al. (1998). It was found that a value of $0.45\,\text{nm}$ for $R_0$ was sufficient (i.e. the elastic and lattice GFs match) for the fcc Ni potentials used in this manuscript. Since the GFs used for relaxation of forces are that of a perfect lattice and the simulation cell contains an $(a/2)[110]$ screw dislocation, the atomistic relaxation procedure and the GF technique must be iterated to relax completely all the forces in the boundary region. For a cylindrical cell size $7.5\,\text{nm}$ radius used in the simulations here, three iterations were sufficient.

The GF solution for the displacement field in three-dimensions is also given by equation (5), but with the forces considered to be point forces acting on atoms in the 3D cell. For distances $R_{mn} > R_0$, the elastic GF for a unit point force in the perfect lattice is used to approximate the 3D GF (Leibfried and Breuer 1978) as

$$
G_{ij}^{mn}(R_{mn}) = \frac{1}{R_{mn}} g_{ij}(\Omega_r), \tag{6a}
$$

$$
g_{ij}(\Omega_r) = \frac{1}{8\pi^2} \int_\Omega (nn)_{ij}^{-1} \mathrm{d}\Omega_n, \tag{6b}
$$

where $\mathbf{n}$ is an orthogonal unit vector perpendicular to $R_{mn}$, $(nn)_{jk}=n_i C_{ijk l}n_l$ and $\Omega$ is the solid angle. $C_{ijk l}$ are the single-crystal elastic constants of the material. The radial dependence of the elastic GF in three-dimensions is known analytically and con- verges with distance as $1/R_{mn}$. However, the angular dependence which is embodied in the function $g_{ij}(\Omega_r)$ has to be evaluated numerically. For our purposes, the func- tion $g_{ij}(\Omega_r)$ was evaluated numerically by evaluating the integral in equation $(6b)$, for different unit vectors $\mathbf{R}_{mn}/|\mathbf{R}_{mn}|$ within the solid angle $\Omega_r$. The solid angle $\Omega_r$ was written in terms of the spherical coordinates of the unit vector $\mathbf{R}_{mn}/|\mathbf{R}_{mn}|$ in the crystal coordinate system, $(\theta,\phi)$. An equally spaced grid of 161 by 161 values of the function $g_{ij}(\Omega_r)$ was evaluated in the $(\theta,\phi)$ coordinate system. For a given $\mathbf{R}_{mn}$, the spherical coordinates of the unit vector in the crystal coordinate system were first evaluated and the value of the function $g_{ij}(\Omega_r)$ extracted from the tables using simple rectangular interpolation. As for line forces, for distances $R_{mn} < R_0$, the lattice GF of the perfect lattice is used as an approximation to $G_{ij}^{mn}$. In three dimensions, a value of $0.5\,\text{nm}$ for $R_0$ was used.

### 3.1. Simulation of dislocation core structures

For simulations of infinite $(a/2)[110]$ screw dislocations, a cylindrical crystal was constructed that was $7.5\,\text{nm}$ in radius and one periodic unit along the symmetry axis in the dislocation line direction. The dislocation line direction was [110], and the length of the periodic unit in the simulations was $a/2^{1/2}$. The $x$ and $y$ axes in the simulation cell were parallel to $[1\overline{1}2]$ and $[1\overline{1}\overline{1}]$ respectively. The $(a/2)[110]$ screw dislocation was introduced into the simulation cell by displacing all atoms according to anisotropic elasticity theory calculated using Stroh's (1958) sextic formalism. Since the anisotropic elasticity solution diverges at the origin, the origin for the displacement field was chosen to be in between atomic positions. A flexible-boundary technique based on the GF method was used in the simulations to obtain a true local minimum energy structure with little residual boundary forces (Rao et al. 1998). Two different core structures g and c for $(a/2)[110]$ screw dislocations were obtained by

varying the elastic centre of the displacement field in the initial anisotropic elasticity approximation (see figure 4 later).

With the GF technique, the simulation cell was divided into three regions:
(i) atomistic region (5.1 nm in radius);
(ii) GF region (5.1-6.3 nm radius shell);
(iii) continuum region (6.3-7.5 nm radius shell).

The width of the GF and continuum regions (1.2 nm) were kept larger than twice the cut-off radius, $2R_{\text{cut}}$, of the Ni potentials. Complete atomistic relaxation using one of the empirical EAM Ni potentials was performed in the atomistic region. The GF and molecular statics methods were iterated until the sum of squares of the magnitudes of all forces on the atoms reached a value that was considered small enough, typically $10^{-8}\ \text{eV}^2\text{nm}^{-2}$ for 2000 atoms. The sum

$$
\mathbf{f} \cdot \mathbf{f} = \sum_{n} (f_{x}^{2} + f_{y}^{2} + f_{z}^{2})_{n} \tag{7}
$$

was used to characterize the strength of forces in the boundary region. The summa- tion in equation (7) extends over all the atoms in the GF and atomistic regions of the simulation cell. For all the cores in two dimensions obtained for fcc Ni, the strength of $\mathbf{f} \cdot \mathbf{f}$ in the atomistic plus GF regions drops from a value of $1.2 \times 10^{-4}$ to $10^{-8}\ \text{eV}^2\text{nm}^{-2}$ after three iterations through the GF atomistic relaxation schemes. The details of the 2D GF method have been described in the literature (Sinclair *et al.* 1978, Rao *et al.* 1998).

### 3.2. Cross-slip simulations

In the Friedel-Escaig mechanism of cross-slip, as soon as a Stroh-type constric- tion (figure 1(d)) is formed on the glide plane (Friedel 1957), the dislocation is assumed to redissociate immediately on the cross-slip plane and expand (figure 1(c)). The cross-slipped configuration of the dislocation involves two constrictions: a constriction of the dislocation which continuously changes the dislocation from the octahedral glide plane to the cross-slip plane, and a constriction which continuously changes the dislocation from the cross-slip to the glide plane. At large or infinite separation distances between the two constrictions, the cross-slip energy can be viewed as a sum of the two constriction energies, since the interaction between the two constrictions is zero.

It should be appreciated that the structures and energetics of the two individual constrictions are expected to be different from each other. At the positive constric- tion, that is the constriction that takes the dislocation from the cross-slip to the glide plane (labelled A in figure 1(c) and referred to as 'edge' constriction by Rasmussen *et al.* (1997a,b)), the local character of both the Shockley partials becomes more edge like in the cross-slip as well as the glide planes. On the other hand, at the negative constriction, where the constriction takes the dislocation from the glide to the cross- slip plane (labelled B in figure 1(c) and referred to as a 'screw' constriction by Rasmussen *et al.* (1997a,b)), the local character of both the Shockley partials becomes more screw like in the cross-slip and the glide planes. This feature is dis- tinctly different from the Stroh-type constrictions where the local character of the Shockley partials changes towards edge like on one side of the constriction and screw like on the other side.

Therefore, the atomistic simulation of cross-slip is divided naturally into two separate simulations: simulation of a positive constriction and simulation of a nega- tive constriction.

The initial conditions to the simulation of a positive constriction were obtained in the following fashion. The left and right halves of the simulation cell were made up of 22 periodic units of the c and g cores respectively. A simple procedure, as described by Rao et al. (1998) was used to make the atomic coordinates of the two cores g and c compatible, to avoid overlapping atoms or vacancies during the build up of the 3D cell. The central cell of unit length $b$ was defined as the average of the positions of identical atoms in the c and g cores. The total length of the simula- tion cell was $45b$, where $b$ is the lattice periodicity along the [110] direction in a fcc structure. Because of the accuracy of GFs, the radius of the simulation cell could be decreased to 4.4 nm, from the 7.5 nm used in the 2D simulations. Atoms within a radius of 4.4 nm in the converged 2D simulation c core and corresponding atoms in the g core were used to build up the 3D cell.

With the above overall procedure, even though the core structures are compa- tible through most of the dislocation line (since the core structures on both sides are compatible), an appreciable misfit force develops at the central three planes or layers, where there is an abrupt change in the core structure of the dislocation. The forces in the continuum region of these three layers were relaxed using the 3D GF technique (Rao et al. 1998).

The 3D simulation cell is divided into three regions similar to the 2D cell: an inner atomistic region, an outermost continuum region and an intermediate GF region. The thicknesses of both the GF and the continuum regions are greater than $2R_{\rm cut}$ along both the radius and the length axis. The atomistic region is 2 nm in radius and $25b$ in length. One of the Ni potentials was used to relax the forces in this region. Atoms in the GF region lie between radii of 2 and 3.2 nm and lengths of $25b$ and $35b$ and the forces that develop in this region are relaxed using the GF technique. Atoms in the continuum region lie between radii of 3.2 and 4.4 nm and lengths of $35b$ and $45b$. Since the GFs of the perfect lattice are used to relax forces in the boundary region, the GF and atomistic relaxation techniques were iterated more than once for a significant relaxation of forces in the boundary region. Since the dislocation threads through the GF and continuum regions along the length axis, the amount of force that can be relieved in the boundary region depends on the length of the simulation cell. Such a procedure was applied to determine the core structure and formation energy of the positive constriction in fcc Ni using the two Ni potentials described previously.

Similar procedures were applied to determine the core structure and formation energy of the second constriction in the cross-slip process, the negative constriction. To simulate the negative constriction, the initial boundary conditions were inter- changed relative to the positive constriction, with the core spread on the cross-slip plane c core extending from $b$ to $22b$, and the core spread on the glide plane g core extending from $-b$ to $-22b$.

Interaction energies between the two constrictions at four separation distances, $3b$, $5b$, $11b$ and $21b$, were evaluated using the Ni(2) potential. Fully relaxed atomic positions corresponding to the positive and negative constrictions were used in the calculations. For a separation distance of $nb$ between the two constrictions, the atoms belonging to layers greater the $[(n-1)/2]$th layer from the positive constriction results, and the atoms belonging to layers less than the $-[(n-1)/2]$th

layer from the negative constriction results, were removed from the calculations. The remaining atoms from the positive constriction results were displaced by a distance of $-[(n-1)/2]b$ along the dislocation line, whereas atoms from the negative con- striction results were displaced by a distance of $[(n+1)/2]b$ along the dislocation line. These atoms, with their modified positions, were then assembled together for the interaction calculations. The atomistic region was 2 nm in radius and $25+(n-1)b$ in length. Atoms within two layers, the original central layers within the positive and negative constriction results, were held fixed during the relaxation procedure. This ensures that the cross-slipped configuration does not collapse owing to the attractive force between the two constrictions. The residual forces that develop at the boundary of the simulation cell are once again relaxed using Green's function boundary conditions (GFBCs). This procedure is schematically illustrated in figure 3.

To evaluate the effect of applied stresses on cross-slip energy, Escaig stresses were applied on the atomistically relaxed cross-slip pair configurations separated by the four different distances $\lambda$. An Escaig stress was applied on the glide plane, with the corresponding applied Escaig stress on the cross-slip plane being zero. This was achieved by applying a generalized strain tensor which included all three normal components as well as the Escaig strain component. The applied strain tensor, in the glide plane coordinate system, for a given Escaig stress, is given in table 4 together with the corresponding stress tensors in the glide and cross-slip plane coordinate systems. As before, the constriction pair configurations were atomistically relaxed, with the central layers of the two constrictions fixed. The residual forces that develop at the boundary of the simulation cell are relaxed using GFBCs.

![](./images/811981060844814338_4.jpg)

Figure 3. Schematic illustration of the atomistic simulation cell used for constriction interaction calculations.

Table 4. Applied 3D strain and stess tensors in the glide plane coordinate system $1 \overline{1} 2,1 \overline{1} \overline{1}$ and 110 . The applied stress tensor resolved on to the cross-slip plane coordinate system $1 \overline{1} \overline{2}, 1 \overline{1} 1$ and 110 is also given.

<table>
<thead>
<tr>
<th colspan="4">3D strain tensor</th>
</tr>
</thead>
<tbody>
<tr>
<td>$1 \overline{1} 2$</td>
<td>$-0.0007408$</td>
<td>$0.0016000$</td>
<td>$0.0000$</td>
</tr>
<tr>
<td>$1 \overline{1} \overline{1}$</td>
<td>$0.0000$</td>
<td>$0.0004076$</td>
<td>$0.0000$</td>
</tr>
<tr>
<td>110</td>
<td>$0.0000$</td>
<td>$0.0000$</td>
<td>$0.0003331$</td>
</tr>
<tr>
<td colspan="4">3D stress tensor (units of $\mu$)</td>
</tr>
<tr>
<td>$1 \overline{1} 2$</td>
<td>$-0.00124$</td>
<td>$0.0010$</td>
<td>$0.0000$</td>
</tr>
<tr>
<td>$1 \overline{1} \overline{1}$</td>
<td>$0.0010$</td>
<td>$0.00124$</td>
<td>$0.000$</td>
</tr>
<tr>
<td>110</td>
<td>$0.0000$</td>
<td>$0.0000$</td>
<td>$0.0000$</td>
</tr>
<tr>
<td colspan="4">Applied stress tensor (units of $\mu$)</td>
</tr>
<tr>
<td>$1 \overline{1} 2$</td>
<td>$-0.00153$</td>
<td>$-0.000002$</td>
<td>$0.0000$</td>
</tr>
<tr>
<td>$1 \overline{1} \overline{1}$</td>
<td>$-0.000002$</td>
<td>$0.00153$</td>
<td>$0.0000$</td>
</tr>
<tr>
<td>110</td>
<td>$0.0000$</td>
<td>$0.0000$</td>
<td>$0.0000$</td>
</tr>
</tbody>
</table>

## §4. RESULTS AND DISCUSSION

### 4.1. Dislocation core structures

The core of an $(a / 2)[110]$ screw dislocation was made to relax on two different octahedral planes by using two different initial elastic centres in the anisotropic solution to the displacement field of the dislocation. If the elastic centre of the initial approximation to the dislocation displacement field was taken as $(0.01 \mathrm{~nm}, 0.01 \mathrm{~nm})$, the core of the dislocation spreads on the cross-slip octahedral plane $(1 \overline{1} 1)$. Similarly, if an elastic centre of $(-0.05 \mathrm{~nm}, 0.05 \mathrm{~nm})$ is chosen for the initial approximation, the core of the screw dislocation relaxes on the glide octahedral plane, $(1 \overline{1} \overline{1})$.

Figure 4 shows a differential displacement field plot (Vitek 1974) of the two symmetry-related core structures obtained for the $(a / 2)[110]$ screw dislocation, $\mathrm{c}$ and $\mathrm{g}$ using the $\mathrm{Ni}(1)$ potential. In the differential displacement plot, the difference between the displacements of each atom from each neighbouring atom, projected along the Burgers vector direction is indicated by the magnitude of the arrow drawn between the two atoms. In figure 4, the projected differential displacements have been adjusted such that, if they are greater than integer multiples of half the screw component of the Burgers vector of the Shockley partials $((a / 4)[110])$, the differential displacement is taken to be a fraction (minimum) of the screw component of the Burgers vector of the Shockley partial obtained by adding or subtracting integer multiples of $(a / 2)[110]$, the 'wrap-around' vector. In this way, the magnitude of the differential displacements become a maximum in the stacking-fault region. The core of the $(a / 2)[110]$ screw dislocation spreads onto the glide plane or the cross-slip plane according to the classical dissociation scheme involving two Shockley partials with the stacking fault in between as

$$
\frac{a}{2}[110]=\frac{a}{6}[121]+\mathrm{SF}(1 \overline{1} 1)+\frac{a}{6}[21 \overline{1}), \tag{8a}
$$

$$
\frac{a}{2}[110]=\frac{a}{6}[12 \overline{1}]+\mathrm{SF}(1 \overline{1} \overline{1})+\frac{a}{6}[211). \tag{8b}
$$

![](./images/811981060844814338_5.jpg)

Figure 4. Differential-displacement plots of the relaxed core structures of $(a/2)[110]$ screw dislocations in fcc Ni. The Ni(1) potential referred to in the text is used in the atomistic relaxations. The two types of core are shown in the figure: one spread on the cross-slip octahedral plane $(1\overline{1}1)$ and the other spread on the octahedral glide plane $(11\overline{1})$. These are referred to as cores c and g in the text. The screw component of the differential displacements are shown and, as a qualitative guide to the eye, the region of significant differential displacements is highlighted.

Figure 5 shows the core structures obtained for the $(a/2)[110]$ screw dislocation with the two different fcc Ni potentials used in this study. In all cases, an initial elastic centre of $(-0.05\,\text{nm}, 0.05\,\text{nm})$ was used for the anisotropic elastic displacement field. For both the Ni potentials, the core of the $(a/2)[110]$ screw dislocation spreads according to equation $(8b)$. However, as expected, the core becomes con- stricted or the width of separation of the Shockley partials decreases with increasing stacking-fault energy. Table 3 compares the atomistic results with continuum calcu-

![](./images/811981060844814338_6.jpg)

Figure 5. Comparison of differential-displacement plots of the core of $(a/2)[110]$ screw dislocations, relaxed on the octahedral glide plane $(1\overline{1}\overline{1})$, referred to as core g in the text, obtained using two different Ni potentials, Ni(1) and Ni(2). The screw component of the differential displacements are shown.

lations (equation (4)) of the separation distances between Shockley partials obtained with the two different fcc Ni potentials. For both the Ni potentials, the atomistic results show an increased spreading of the Shockley partials relative to the conti- nuum calculations, approximately by two periodic units. Similar results were obtained for an initial elastic centre of (0.01 nm, 0.01 nm), but with the core spread according to equation (8 a) on the cross-slip octahedral plane.

### 4.2. Cross-slip simulations

#### 4.2.1. Core structure of $(a/2)[110]$ screw dislocations during the cross-slip process
Figures 6 (a) and (b) show differential displacement-field plots of the screw com- ponents of the atomistically relaxed core configuration of $(a/2)[110]$ screw disloca tions at the positive and negative constrictions respectively involved in the cross-slip process. The differential displacement-field plots are plotted for different perpendi- cular slices along the dislocation line. Thin cylindrical slices perpendicular to the dislocation axis are taken of the original unperturbed lattice with the thickness of the slice equal to the lattice periodicity along the dislocation axis, $(a/2)[110]$. The rela- tive displacements of all the atoms within the slice at both the positive and the

negative constrictions are used to obtain the differential displacement-field plot for that particular slice in figures 6 (a) and (b). At the central plane of both the constric- tions, the differential displacements are more or less equally spread over both the octahedral planes and the core structures are diffuse, as opposed to the classical point constriction (Stroh 1954). However, within a few slices away from the central plane (about two), the core displacements at the $(a / 2)[110]$ screw dislocation are predominantly contained within one of the two octahedral planes: the $(1 \overline{1} \overline{1})$ glide plane on the positive side and the $(1 \overline{1} 1)$ cross-slip plane on the negative side for the positive constriction, and vice versa for the negative constriction. However, in this region the core of the dislocation is constricted, by a factor of at least 2.5, relative to the extension of the core for a straight dislocation (figures 5-7).

Similar differential displacement-field plots were used to identify the location of the two Shockley partials along the dislocation line, at both the positive and the negative constrictions. A 'wrap-around' vector of $(a / 4)[110]$ was used to make the relative displacements a maximum at the core of the Shockley partials, and a mini- mum at the perfect lattice and stacking-fault positions. This identifies the location of the individual Shockley partials fairly accurately. Figure 7 shows the results obtained for the location of the two Shockley partials close to the positive and negative constrictions. Only the locations on one side of each of the two constrictions are plotted. The location of Shockley partials on the other side was found to be sym- metric about the centre, at both the two constrictions. It is noted that, with this technique, the location of the partials could not be obtained very close to the two constrictions where the relative displacements are diffuse and spread over more than one octahedral plane. No significant difference is found between the two types of constriction as far as the extent of and variation in the constriction process. However, they differ in their energetics as will be shown in the next section.

#### 4.2.2. Energetics of cross slip of $(a / 2)[110]$ screw dislocations: unstressed

The differential energy $\delta E$ between the constricted dislocation in the cross-slip event and the original unconstricted configuration, for each cylindrical periodic unit along the dislocation line is plotted in figure 8. The thickness of each cylindrical slice is taken to be $(a / 2)[110]$ and the position of the shell is taken to be its mean position nb along the dislocation line in the unperturbed lattice. For each shell, the differential energy $\delta E$ was obtained by summing the differences in energy between identical atoms in the constricted and unconstricted configurations within a cylindrical radius of 3.2 nm. This radius was chosen to avoid any surface effects on the differential- energy plots. The differential-energy plot is shown for both the positive and the negative constrictions. There is a marked difference between the energy plots of the two constrictions. For one of the constrictions, the differential energy $\delta E$ is always positive along the dislocation line with a maximum at the central plane. The other constriction has a differential-energy plot which is predominantly negative along the dislocation line.

The integral of the differential-energy curve over the length of the dislocation line gives the formation energy of the constrictions at zero applied stress. The total energy of the positive constriction is equal to 6.30 eV whereas the negative constric- tion has a negative formation energy of -1.45 eV. The sum of the formation energies of the two constrictions which is the total energy of the cross-slip event under no applied stress is found to be approximately 4.85 eV for Ni(1). Similar asymmetry in the energetics of the constrictions was found in an atomistic study of cross-slip in fcc

![](./images/811981060844814338_7.jpg)

Figure 6. Differential displacement plots of the core structure $(a/2)[110]$ screw dislocations during a Friedel-Escaig type of cross-slip event. The individual cells used in the generation of the differential displacement plots are described in the text. Here, (centre) denotes the differential-displacement plot for the central plane in the simulation cell and $(-1)$, $(-2)$ and $(-3)$ denote differential-displacement plots for perpendicular slices $-(a/2)[110]$, $-a[110]$ and $-(3a/2)[110]$ from the central plane. Similarly, $(+1)$ and $(+2)$ denote differential-displacement plots for perpendicular slices $(a/2)[110]$ and $a[110]$ from the central plane. These differential displacement plots are shown for both the positive constriction and the negative constriction. Atom pairs with significant differential displacements are shown and highlighted. Each of the differential-displacement plots are enclosed in a box to depict approximately the size and shape of the core structure. In all cases, the screw component of the differential displacements are shown.

![](./images/811981060844814338_8.jpg)

Cu by Rasmussen *et al.* (1997a,b), using an interatomic potential based on effective-medium theory.

The convergence of the formation energies of the constrictions was determined as a function of the radius and length of the simulation cell. Overall, it was found that the energies of the constrictions were completely contained within a cylinder of radius $2d$ and length $6d$ around the centre of the constrictions, and the far field elastic energy contribution to the formation energies appears to be minimal. This is in contrast with the observations of Rasmussen *et al.* (1997a,b) who find that the cross-slip energy is confined to a cylinder of radius $6.5d$ and length $8.3d$ around the centre of the constrictions. The faster convergence of the formation energy in the present simulations is most probably due to the use of the GF technique for relaxing the boundary forces. This suggests that the use of GF technique can reduce the number of atoms required in these types of simulation by at least an order of magnitude, relative to free surface and fixed boundary conditions.

![](./images/811981060844814338_9.jpg)

Figure 7. Location of Shockley partials at both the positive and the negative constrictions, as a function of the position along the dislocation line. Differential-displacement plots of the screw component using the $(a/4)[110]$ 'wrap-around' vector were used to derive the location of the Shockley partials. Atomistic results are also compared with Stroh's continuum calculations.

There are four contributions to the differential energy $\delta E$:

(i) change in the energy of interaction between two Shockley partials;
(ii) an increase in dislocation length at the constrictions;
(iii) a decrease in area of the stacking fault between the two Shockley partials at the constrictions;
(iv) a change in character of the Shockley partials at the constriction.

The first two factors contribute to an increase in energy of the dislocation at the constrictions. The third contribution is expected to be negative. The energy change due to a change in character of Shockley partials at the constrictions is expected to be positive at the positive constriction, and negative at the negative constriction. The first three contributions are included in a line-tension model of cross slip, within the limitations of elasticity theory (Stroh 1954, Escaig 1968, Saada 1991). However, within elasticity theory, the energetics of the two constrictions are identical only if these three contributions to the energetics are considered. If self-stress effects, which account for the change in character of Shockley partials at the two constrictions, are included in a continuum model the energetics of the two constrictions are expected to be different from each other (Duesbery et al. 1991). The atomistic simulation results suggest that the energy changes due to change in character of the Shockley partials, the fourth contribution, dominate the energetics of the two constrictions. In addition

![](./images/811981060844814338_10.jpg)

Figure 8. Differential energies, the increase or decrease in energy with respect to the original unconstricted dislocation, as a function of the position along the dislocation line, at both the positive and the negative constrictions. The individual cells used to extract the differential energies $\delta E$ are described in the text.

to this, core effects which are not included in an elastic model may also contribute to the significant asymmetry in the energetics of the two constrictions.

Figure 9 shows polar plots (Hirth and Lothe 1982) of the line energy factor $K$ as well as the line tension factor $K+\delta^{2} K / \delta \theta^{2}$ on the (111) plane for the Shockley partials involved in the cross-slip process. The cubic elastic constants $C_{11}=2.44 \times 10^{12} \mathrm{dyn} \mathrm{cm}^{-2}$, $C_{12}=1.49 \times 10^{12} \mathrm{dyn} \mathrm{cm}^{-2}$ and $C_{44}=1.25 \times$ $10^{12} \mathrm{dyn} \mathrm{cm}^{-2}$ as given by the EAM interatomic potential are used in the calculations. The initial Shockley-partial alignment in the unconstricted configuration is at $\pm 30^{\circ}$ to the screw direction as indicated in the figure. Both the polar plots show that the line energy and line tension factors are positive for any direction on the (111) plane and that there is no elastic instability on the (111) plane for the Shockley partials. This indicates that the energy to increase the length of the Shockley partials at the constrictions is positive within elasticity theory, and is not a cause for the negative formation energy found in atomistic calculations for one of the constrictions, the negative constriction.

The cross-slip energy was evaluated using two Ni potentials with different stacking-fault energies. The Ni potentials have almost identical properties for fcc Ni (see table 2), except that the stacking-fault energy is $58 \mathrm{~mJ} \mathrm{~m}^{-2}$ for $\mathrm{Ni}(1)$ and $119 \mathrm{~mJ} \mathrm{~m}^{-2}$ for $\mathrm{Ni}(2)$. As a result, the Shockley partial spacing $d / b$ for $\mathrm{Ni}(1)$ is a factor of 1.5 larger than that for $\mathrm{Ni}(2)$ (see table 3). This is expected to result in a decrease in the cross-slip energy, with $\mathrm{Ni}(2)$ giving a lower cross-slip energy than $\mathrm{Ni}(1)$ (Stroh 1954). The cross-slip energy at zero applied stress, the sum of the energy of positive and negative constrictions, is found to be $4.85 \mathrm{eV}$ with $\mathrm{Ni}(1)$ and $2.35 \mathrm{eV}$ with $\mathrm{Ni}(2)$. Clearly, the cross-slip energy is decreasing with increasing stacking-fault energy or decreasing $d / b$ ratio. The ratio of cross-slip energies obtained with the two potentials is approximately equal to two. Both the self-stress and the line tension continuum

![](./images/811981060844814338_11.jpg)

![](./images/811981060844814338_12.jpg)

Figure 9. Polar plot of (a) line energy as well as (b) the line tension factors of the Shockley partials involved in the cross-slip process.

treatments of the cross-slip process predict a decreasing cross-slip energy with decreasing $d/b$ ratio and are in agreement as to the expected scaling of cross-slip energy with $d/b$ ratio (Duesbery et al. 1991). The energy $E_{\rm c}$ of cross-slip at zero stress, according to the Stroh (1954) line tension solution, is given by

$$
E_{\rm c} \propto \frac{d}{b} \left[ \ln \left( \frac{d}{b} \right) \right]^{1/2}. \tag{9}
$$

Using equation (9), the cross-slip energy ratio for a change in Shockley partial spacing from $d/b = 7.8$ to $d/b = 5.2$ is determined to be 1.67. This is in fair agreement with the atomistic results, which gives a value of 2.06. Surprisingly, the scaling

of energies is in good agreement with continuum calculations, even though self-stress and atomistic forces dominate the energetics of the constrictions. However, the scaling of cross-slip energy according to equation (9) is expected to break down at extremely small Shockley partial spacings, $d / b \approx 1-2$, as in $\mathrm{L1}_{0}$ TiAl (S. I. Rao 1998, unpublished calculations).

### 4.2.3. Comparison of results on cross-slip energies with experimental data

The experimental value for the stacking-fault energy in fcc Ni is approximately $125 \mathrm{mJ} \mathrm{m}^{-2}$ (Carter and Holmes 1977, Hirth and Lothe 1982), closer to the stackingfault energy given by potential $\mathrm{Ni}(2), 118 \mathrm{mJ} \mathrm{m}^{-2}$. As a result, the cross-slip energy given by $\mathrm{Ni}(2), 2.35 \mathrm{eV}$, should be representative of the real value for cross-slip in fcc $\mathrm{Ni}$. A value of $2.35 \mathrm{eV}$ for the cross-slip energy at zero stress in fcc $\mathrm{Ni}$ is in reasonable agreement with the experimental value for the energy of cross-slip in fcc Ni (Clement and Coloumb 1974).

Similarly, the cross-slip energy in fcc $\mathrm{Cu}$ can be estimated from these atomistic simulations since it scales according to equation (9). The $d / b$ value given by $\mathrm{Ni}(2)$ for the unconstricted $(a / 2)[110]$ screw dislocation (table 3 ) is in reasonable agreement with the $d / b$ value observed in fcc $\mathrm{Cu}$ (Stobbs and Sworn 1971). As a result, the cross-slip energy in fcc $\mathrm{Cu}$ can be obtained from the atomistic result for cross-slip energy in $\mathrm{Ni}(2)$ by simply scaling by the shear modulus of $\mathrm{Cu}$ relative to the shear modulus of $\mathrm{Ni}$ (or by the elastic interaction energy coefficient of $\mathrm{Cu}$ relative to that of $\mathrm{Ni}$ ). This gives a value of $1.07-1.28 \mathrm{eV}$ for the cross-slip energy in fcc $\mathrm{Cu}$. This is in reasonable agreement with the experimental value of $1.15 \mathrm{eV}$ deduced for the crossslip energy in $\mathrm{Cu}$ (Bonneville and Escaig 1979).

The present atomistic results give a significantly smaller cross-slip energy than the value of $2.7 \mathrm{eV}$ obtained by Rasmussen et al. (1997a,b) for fcc $\mathrm{Cu}$ using the effective-medium theory. This may be due to the different interatomic potentials used in the two simulations, as well as the use of the GF technique for relaxing the boundary forces in the present simulations. However, when fixed boundary conditions (boundary atoms fixed at atomic positions corresponding to the aniso- tropic elasticity displacement field for a constricted $(a / 2)[110]$ dislocation) were used in the present simulations with $\mathrm{Ni}(1)$, the measured cross-slip energy actually decreased from 4.85 to $3.3 \mathrm{eV}$. The fixed boundary simulations tend to increase the energy of the unconstricted configuration more than the energy of the constricted configuration.

### 4.2.4. Constriction interaction energies

The atomistic results for the energy $E(\lambda)$ of the cross-slipped configuration as a function of the separation distance $\lambda$ between the two constrictions scaled relative to the energy $E_{\mathrm{c}}$ at infinite separation distance is shown in figure 10. Superposed on the atomistic results is a least-squares fit of the form

$$
\frac{E(\lambda)}{E_{\mathrm{c}}}=1-\frac{1}{\lambda} K_{\mathrm{int}}, \quad(10 a)
$$

where $K_{\text {int }}$ characterizes the strength of the interaction between the positive and negative constrictions. Figure 10 also compares the atomistic results with continuum calculations by Pusch and Schoeck (1993). The atomistic results give a weaker interaction strength $K_{\text {int }}$ than continuum calculations do. The change in character of Shockley partials towards more edge like at the positive constriction and towards

![](./images/811981060844814338_13.jpg)

Figure 10. Atomistic and continuum results on double constriction energies as a function of separation distance $\lambda$ between constrictions. A least-squares fit to the atomistic results, according to equation (10), is also shown.

more screw like at the negative constriction is explicitly taken into account in the atomistic calculations. This results in a weaker interaction between the two constric- tions, since parallel edge and screw dislocations are expected to have very little interaction with each other (Hull and Bacon 1984). These results on the strength of the interaction between the constrictions are similar to previous atomistic results obtained by Parthasarathy and Dimiduk (1996) in the simulation of PPV locks of height $b / 2$ in $Ll_{2} Ni_{3} Al$. However, in the analytical treatment of cross-slip in fcc structures within continuum theory by Bonneville and Escaig (1979), the interaction energy between the constrictions is neglected. The present results for the interaction strength $K_{int }$ , therefore, lie between continuum calculations (Duesbery et al. 1991, Puschl and Schoeck 1993) and an assumption of zero interaction (Bonneville and Escaig, 1979). The atomistic results for the strength of the interaction between the constrictions is closer to one extreme of the range in interactions obtained in con- tinuum calculations as

$$
\begin{aligned}
\frac{E(\lambda)}{E_{\mathrm{c}}} & =\frac{1+q}{2}, \\
q & =\frac{2}{\pi} \tan ^{-1}\left(\frac{p \lambda}{d}\right), \quad p=1.8
\end{aligned} \quad(10 b)
$$

Continuum calculations (Puschl and Schoeck 1993) give a value of 0.8-1.4 for $p$ in equation (10b).

### 4.2.5. Energetics of cross-slip of (a/2)[110] screw dislocations: Escaig stress effects

The energy of the cross-slipped configurations at separation distances of $3b$, $5b$, $11b$ and $21b$ were also evaluated at applied Escaig stresses of $0.00045\mu$, $0.0009\mu$ and $0.0045\mu$ on the glide plane, with no Escaig stress on the cross-slip plane. As given in table 4, a 3D state of strain was applied on the simulation cell to achieve such a state of stress. Differences in energies between the relaxed cross-slipped configurations and the infinite dislocation confined to the glide plane with an identical applied Escaig stress was determined. The applied Escaig stresses were such that they tended to increase the equilibrium Shockley partial splitting of the $(a/2)[110]$ screw dislocation on the glide plane, resulting in a lower-energy core structure relative to the unstressed structure. Atomistic results at each applied Escaig stress were fitted to an equation of the form similar to equation (10):

$$
\frac{E(\tau, \lambda)}{E_{\mathrm{c}}}=1-\frac{1}{\lambda} K_{\mathrm{int}}(\tau), \tag{11}
$$

where $\tau$ is the applied Escaig stress. The interaction strength $K_{\mathrm{int}}(\tau)$ continuously decreases with increasing Escaig stress. Atomistic calculations, however, do not include the work done by the applied Escaig stress in expanding the Shockley partials in the glide plane. Considering the work done term as simply $E_{\mathrm{w}}=-\tau b_{\mathrm{e}} d_{0} \lambda$, where $b_{\mathrm{e}}$ is the magnitude of the edge component of the Shockley partials, $a_{0} 6^{1 / 2} / 12$, adding to equation (11) and maximizing the energy with respect to $\lambda$, the activation energy $E_{1}(\tau)$ for cross-slip as a function of the applied Escaig stress $\tau$ was determined. Such a plot is shown in figure 11. In the maximization procedure, if the effect of the Escaig stress on constriction interaction energies is neglected, that is equation (11) is replaced by equation (10), a slightly different curve is obtained for the activa-

![](./images/811981060844814338_14.jpg)

Figure 11. Cross-slip energies as a function of the applied Escaig stress, scaled to cross-slip energy at zero stress. The $E_{1}(\tau)$ and $E_{2}(\tau)$ plots are explained in the text.

tion energy for cross-slip as a function of the applied Escaig stress $E_{2}(\tau)$. This is also shown in figure 11. As expected, the two calculations deviate at large stresses. The atomistic results on the activation energy for cross-slip with the applied Escaig stress shows a much weaker dependence compared with previous continuum calculations (Bonneville and Escaig 1979, Duesbery *et al.* 1991, Puschl and Schoeck 1993). This results in an activation volume $-\delta E / \delta \tau$ for cross-slip to be approximately $20b^{3}$ at $10^{-3}\mu$ in fcc Cu, which is an order of magnitude smaller than the measurements made by Bonneville and Escaig (1979) as well as continuum calculations. However, simple analytical calculations by Saada (1991) of the activation volume for cross-slip in Cu based on Stroh's (1958) formalism also gives a low value, similar to present results. Also, the measurements on activation volume have been made on a deformed crystal which complicates the interpretation since the screw dislocations are cross-slipping in a crystal with a developed dislocation substructure, rather than a defect-free crystal.

### §5. SUMMARY
3D atomistic simulations using EAM potentials together with 2D and 3D GFBC techniques have been used successfully to study cross-slip of $(a/2)[110]$ screw dislocations in fcc structures. The GFBC techniques were used to make the boundaries in the atomistic simulations respond to changes in defect structure occurring in the atomistic region, such that there are no residual forces in the boundary region. The GF techniques used in the simulations are identical with those used by Rao *et al.* (1998) in their simulations of kinks on $(a/2)[111]$ screw dislocations in bcc Fe.

Differential displacement-field plots of the core structure of an $(a/2)[110]$ screw dislocation near the constrictions occurring in the cross-slip process reveal that the core structures are diffuse, as opposed to a point constriction as postulated by Stroh (1954). The differential displacement fields at the constriction region are spread on both the glide and the cross-slip octahedral planes. These results are similar to the results obtained by Parthasarathy and Dimiduk (1996) in their simulations of cross-slip PPV locks in $L1_{2}Ni_{3}Al$. However, a few interatomic distances away from the centres of the constrictions the core structures are contained within a single octahedral plane. The dislocations are significantly constricted in this region, by a factor of at least 2.5 compared with the separation between Shockley partials in the unconstricted dislocation. A study of the location of Shockley partials at these positions indicate that their locations are in reasonable agreement with continuum predictions (Stroh 1954).

However, the energetics of the two constrictions, positive and negative, are significantly different, with the positive constriction having a positive formation energy and the negative constriction having a negative formation energy, suggesting that self-stress forces and atomistics dominate the energetics of the constrictions.

Atomistic results on the scaling of cross-slip energy with $d/b$ ratio is in reasonable agreement with continuum predictions, being proportional $(d/b)[\ln (d/b)]^{1/2}$. The cross-slip energies are determined to be 2.35 and 1.20 eV in fcc Ni and Cu respectively, compared with a measured value of 1.15 eV in Cu.

Atomistic calculations show that the cross-slip energy is weakly dependent on the applied Escaig stress, with an activation volume for cross-slip of the order of $20b^{3}$ at $10^{-3}\mu$ in fcc Cu. This result on the activation volume for cross-slip is an order of magnitude smaller than previous predictions based on continuum theory.

## ACKNOWLEDGEMENTS

The authors wish to thank Dr P. Hazzledine and Dr J. P. Simmons of UES Inc. and Dr D. Dimiduk of Wright Laboratory for helpful discussions during the course of this work. Sincere thanks is also extended to C. Hernandez, SOCHE scholar at Wright Laboratory, for writing the GF program and helping with the figures and tables for this paper. This work was performed while S. I. Rao, T. A. Parthasarathy and C. Woodward worked at the US Air Force Wright Laboratory, Materials Directorate, MLLM under contract F33615-91-C-5663. This work was supported in part by a grant of HPC, time from the CEWES DOD HPC shared resource centre using Cray YMP and C90 supercomputers.

## REFERENCES

BACON, D. J., BARNETT, D. M., and SCATTERGOOD, R. O., 1979, Prog. Mater. Sci., 23, 51.

BONNEVILLE, J., and ESCAIG, B., 1979, Acta metall., 27, 1477.

BULATOV, V. V., YIP, S., and ARGON, A. S., 1995, Phil. Mag. A, 72, 1995.

CARTER, C.B., and HOLMES, S. M., 1977, Phil. Mag. A, 35, 1161.

CLEMENT, P. N., and COULOMB, P., 1974, Phil. Mag., 30, 363.

COURET, A., and CAILLARD, D., 1988, Acta metall., 36, 215.

DAW, M. S., and BASKES, M. I., 1984, Phys. Rev. B, 29, 6443.

DIMIDUK, D. M., 1991, J. Phys. Paris, III, 1, 1025.

DEVINCRE, B., VEYSSIERE, P., KUBIN, L.P., and SAADA, G., 1997, Phil. Mag. A, 75, 1263.

DUESBERY, M. S., 1983, Acta metall., 31, 1747.

DUESBERY, M. S., LOUAT, N. P., and SADANANDA, K., 1991, Acta metall. mater., 40, 149.

ESCAIG, B., 1968, *Proceedings of the Battelle Colloquium in Dislocation Dynamics*, edited by A. R. Rosenfield, G. T. Hahn, A. L. Bement, Jr, and R. I. Jaffee (New York: McGraw-Hill), p. 655.

FARKAS, D., SCHON, C. G., and GOLDENSTEIN, H., 1996, Acta mater., 44, 409.

FINNIS, M. W., and SINCLAIR, J. E., 1984, Phil. Mag. A, 50, 45.

FLEISCHER, R. L., 1959, Acta metall., 7, 134.

FRIEDEL, J., 1957, *Dislocations and Mechanical Properties of Crystals* (New York: Wiley), p. 330.

GREENBERG, B. A., ANTONOVA, O. V., INDENBAUM, V. N., KARKINA, L. I., NOTKIN, A. B., PONOMAREV, M. V., and SMIRNOV, L. V., 1991, Acta metall. mater., 39, 233.

HIRTH, J. P., and LOTHE, J., 1982, *Theory of Dislocations*, second edition (New York: Wiley).

HULL, D., and BACON, D. J., 1984, *Introduction to Dislocations*, third edition (Oxford: Pergamon).

HUMPHREYS, F. J., and HIRSCH, P. B., 1970, Proc. R. Soc. A, 318, 73.

JACKSON, P. J., 1985, Prog. Mater. Sci., 29, 139.

LEIBFRIED, G., and BREUER, N., 1978, *Point Defects in Metals 1*, Springer Tracts in Modern Physics, Vol. 81, (Berlin: Springer).

KUBIN, L. P., CANOVA, G., CONDAT, M., DEVINCRE, B., PONTIKIS, V., and BRECHET, Y., 1992, Solid St. Phenom., 23-24, 455.

LOUCHET, F., and VIGUIER, B., 1995, Phil. Mag. A, 71, 1313.

MILLS, M. J., and CHRZAN, D. C., 1992, Acta metall., 40, 3051.

PAIDAR, V., POPE, D. P., and VITEK, V., 1984, Acta metall., 30, 435.

PARTHASARATHY, T. A., and DIMIDUK, D., 1996, Acta mater., 44, 2237.

PARTHASARATHY, T. A., DIMIDUK, D., and SAADA, G., 1993, Mater. Res. Soc. Symp. Proc., 288, 311.

PUSCHL, W., 1990, Phys. Stat. sol. (b), 162, 363.

PUSCHL, W., and SCHOECK, G., 1993, Mat. Sci. Engng., 164, 286.

RAO, S. I., HERNANDEZ, C., SIMMONS, J. P., PARTHASARATHY, T. A., and WOODWARD, C., 1998, Phil. Mag. A, 77, 231.

RASMUSSEN, T., JACOBSEN, K. W., LEFFERS, T., and PEDERSEN, O. B., 1997a, Phys. Rev. B; 56, 2977; 1997b, Mater. Sci. Engng., A234-236, 544.

ROSE, J. H., SMITH, J. R., GUINEA, F., and FERRANTE, J., 1984, Phys. Rev. B, 29, 2963.

SAADA, G., 1991, Mater. Sci. Engng., 137, 177.

SCHOECK, G., and SEEGER, A., 1955, *Defects in Crystalline Solids* (London: Physical Society), p. 340.

SEEGER, A., and SCHOECK, G., 1953, *Acta metall.*, **1**, 519.

SIMMONS, J. P., RAO, S. I., and DIMIDUK, D., 1998, *Phil. Mag. Lett.*, **77**, 327.

SINCLAIR, J. E., GEHLEN, P. C., HOAGLAND, R. G., and HIRTH, J. P., 1978, *J. appl. Phys.*, **49**, 3890.

STOBBS, W. M., and SWORN, C. H., 1971, *Phil. Mag.*, **24**, 1365.

STROH, A. N., 1954, *Proc. phys. Soc. B*, **67**, 427; 1959, *Phil. Mag.*, **3**, 625; 1962, *J. math. Phys.*, **41**, 77.

VITEK, V., 1974, *Cryst. Lattice Defects*, **5**, 1.

VOTER, A. F., and CHEN, S. P., 1987, *Mater. Res. Soc. Symp. Proc.*, **82**, 175.