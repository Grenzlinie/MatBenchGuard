
# Profiling novel high-conductivity 2D semiconductors

Thibault Sohier, \( ^{1,2} \)  Marco Gibertini, \( ^{3,4,2} \)  and Nicola Marzari \( ^{2} \) 

 \( ^{1} \) nanomat/QMAT/CESAM and European Theoretical Spectroscopy Facility, University of Liege (Uliege), Belgium  
 \( ^{2} \) Theory and Simulation of Materials (THEOS), and National Centre for Computational Design and Discovery of Novel Materials (MARVEL), École Polytechnique Fédérale de Lausanne, CH-1015 Lausanne, Switzerland  
 \( ^{3} \) Dipartimento di Fisica Informatica e Matematica, Università di Modena e Reggio Emilia, Via Campi 213/a, I-41125 Modena, Italy  
 \( ^{4} \) Department of Quantum Matter Physics, University of Geneva, CH-1211 Geneva, Switzerland  
(Dated: August 3, 2020)

When complex mechanisms are involved, pinpointing high-performance materials within large databases is a major challenge in materials discovery. We focus here on phonon-limited conductivities, and study 2D semiconductors doped by field effects. Using state-of-the-art density-functional perturbation theory and Boltzmann transport equation, we discuss 11 monolayers with outstanding transport properties. These materials are selected from a computational database of exfoliable materials providing monolayers that are dynamically stable and that do not have more than 6 atoms per unit cell. We first analyze electron-phonon scattering in two well-known systems: electron-doped InSe and hole-doped phosphorene. Both are single-valley systems with weak electron-phonon interactions, but they represent two distinct pathways to fast transport: a steep and deep isotropic valley for the former and strongly anisotropic electron-phonon physics for the latter. We identify similar features in the database and compute the conductivities of the relevant monolayers. This process yields several high-conductivity materials, some of them only very recently emerging in the literature (GaSe,  \( Bi_{2}SeTe_{2} \) ,  \( Bi_{2}S_{e3} \) ,  \( Sb_{2}SeTe_{2} \) ), others never discussed in this context (AlLiTe \( _{2} \) , BiClTe, ClGaTe, AuI). Comparing these 11 monolayers in detail, we discuss how the strength and angular dependency of the electron-phonon scattering drives key differences in the transport performance of materials despite similar valley structure. We also discuss the high conductivity of hole-doped  \( WSe_{2} \) , and how this case study shows the limitations of a selection process that would be based on band properties alone.

## I. INTRODUCTION

Two-dimensional (2D) semiconductors with excellent intrinsic transport properties would be beneficial to many applications \( ^{1-3} \) . Some well-known 2D materials like transition-metal dichalcogenides (TMDs), phosphorene or silicene have been extensively studied both experimentally  \( \left(\mathrm{MoS}_{2}^{4,5}, \mathrm{Si}^{6,78}\right) \)  and theoretically  \( \left(\mathrm{MoS}_{2}^{9-13}, \mathrm{P}_{4}^{13-16}\right) \) . Other candidates \( ^{17} \)  have been proposed using approximate deformation potential models and the Takagi \( ^{18} \)  formula, but it has been shown that such approaches suffer from limited reliability \( ^{19} \) . The full potential of 2D materials for future device applications could be much broader than the dozen materials currently under extensive experimental investigation, since many more monolayers have been predicted to be either exfoliable from experimentally known layered materials \( ^{20-23} \)  or synthesizable \( ^{24,25} \) . Such computational collections of prospective 2D materials would likely contain some promising candidates for electronic transport in various contexts.

Finding the ideal material for a given device would require the cross-examination and co-optimization of many different properties \( ^{26} \) . Here, rather than focusing on one particular application, we are interested in the physical features leading to good transport performance. We describe the tools and knowledge needed to explore large databases with an informed, purposeful approach, and eventually identify the candidates with the highest conductivity.

We focus here on room-temperature phonon-limited electronic transport and search across 2D semiconductors. First-principles methods \( ^{27} \)  have proven quite useful and successful in predicting physics and properties in this regime \( ^{28} \)  and for 2D materials \( ^{29,30} \) , provided one is aware of its limits \( ^{19} \) . Although dedicated codes exist \( ^{31,32} \) , performing state-of-the-art first-principles transport simulations on large sets of materials remains nevertheless a challenge, and few works tackle more than one material at a time. Yet, an overall panorama on the property landscape would be very valuable to materials design. For example, in a previous work involving 5 materials \( ^{13} \) , we have shown the importance of intervalley scattering, while the authors of Ref. 33 have studied 4 hexagonal elemental materials to show the benefits of a sharp and deep single valley.

In this work, we explore our portfolio of exfoliable 2D materials \( ^{23} \)  taken from the Materials Cloud \( ^{34,35} \) , limiting ourselves to at most 6 atoms per unit cell. We select the most promising systems from a band structure analysis, and then study their transport properties using an accurate and automated framework that we recently developed \( ^{13} \) , finding several excellent 2D semiconductors. Compared to other methods \( ^{28,36} \) , the approach of Ref. 13 has two main advantages in the context of this work: i) it includes several tools to analyze band structure properties like valley structure or Fermi velocity and ii) the calculation of conductivity is automated within the AiiDA framework \( ^{37,38} \) , which is key to study many materials in
 

a high-throughput fashion. These tools are available \( ^{39} \)  to the community on the Archive section of the Materials Cloud \( ^{35} \) , in support of the FAIR principles of open science and open data.

High carrier densities are routinely obtained in monolayer 2D semiconductors by field-effect doping, especially using ionic-liquid gating \( ^{40-42} \) . Here, we consider a fixed carrier density of  \( n/p = 10^{13} \)  cm \( ^{-2} \)  (electrons or holes). Electron-phonon interactions are computed in an electrostatic framework including such doping \( ^{43} \) , as well as screening from the induced free electrons or holes. This is in contrast to other first-principles studies, usually simulating electron-phonon interactions (EPI) in neutral materials, which would be valid only in the limit of vanishing carrier density. The capability to study explicitly the high-doping regime is a valuable complement to this, and very relevant for monolayers operating in the degenerate limit, when the chemical potential is close to or inside the conduction or valence band (doping regimes are further discussed in App. A). In addition, its predictive accuracy provides meaningful comparisons to experiments. Indeed, the high-doping regime is often used experimentally to characterize the intrinsic properties of novel materials, because it allows to screen charged impurities.

In this study we find excellent phonon-limited transport properties for electron-doped  \( Bi_{2}SeTe_{2} \) ,  \( Bi_{2}S_{e3} \) ,  \( B i C l T e \) ,  \( Sb_{2}SeTe_{2} \) , InSe, GaSe,  \( AlLiTe_{2} \)  and hole-doped phosphorene ( \( P_{4} \) ), AuI,  \( ClGaTe \) , and  \( WSe_{2} \) , all showing mobilities in the range from few hundreds to few thousands  \( cm^{2}/Vs \) . Three of these 2D materials are very well-known and studied ( \( P_{4}^{13-16} \) ,  \( WSe_{2}^{13} \) ,  \( InSe^{44} \) ). The  \( Sb_{2}X_{3} \)  and  \( Bi_{2}X_{3}\ (X=Se, Te, S) \)  compounds are better known for the topological properties of their 3D parents \( ^{45,46} \) . Monolayers have been recently studied in the context of phonon-limited transport \( ^{17,47,48} \) , but only within the approximate Tagaki formalism \( ^{18} \) . The transport performance of monolayer  \( Sb_{2}SeTe_{2} \)  has been confirmed experimentally \( ^{49} \) . GaSe (along with InSe) was studied \( ^{50} \)  ab initio with a representation of electron-phonon scattering that goes beyond deformation potential theory while this work was carried out.  \( AlLiTe_{2} \) ,  \( B i C l T e \) ,  \( C l G a T e \) , and AuI are, to our knowledge, still new in the context of 2D charge transport. Beyond the relatively large number of materials identified and the novelty of some of them, this work most importantly provides visual and intuitive understanding of electron-phonon scattering as well as a systematic and data-supported analysis of the features leading to good transport performance. We confirm and extend previous remarks on the importance of band properties such as number of valleys, effective masses or anisotropy; and show that these can be used for larger scale databases studies to shortlist prospective conductors. On the other hand, we also show how differences in the strength and angular dependency of electron-phonon scattering still induce significant variations in the conductivity of materials with similar band properties.

## II. COMPUTATIONAL AND THEORETICAL FRAMEWORK

## A. Computational details

First-principles calculations of structures, bands, phonons and electron-phonon interactions are performed with the Quantum ESPRESSO \( ^{51,52} \)  (QE) software, by combining density-functional theory (DFT) and density-functional perturbation theory (DFPT) within the generalized gradient approximation as formulated by Perdew, Burke, and Ernzerhof \( ^{53} \)  (PBE). 2D periodic-boundary conditions are applied and the electrostatics of a symmetric double-gate field-effect setup are simulated using the approach described in Ref. 43. Open-boundary conditions are important to properly describe polar-optical phonons \( ^{54} \)  and screening \( ^{55} \) . The field-effect setup is used to induce an electron or hole density with a default value of  \( n/p = 10^{13} \)  cm \( ^{-2} \) . The simulation of this relatively high-doping regime is further discussed in App. A. Calculations are managed using the AiiDA materials informatics infrastructure \( ^{37,38} \) . The AiiDA database containing the provenance for the transport calculations and the tools necessary to reproduce this work are provided in the Archive section of the Materials Cloud \( ^{35,39} \) . The standard numerical setup for all ground state and phonon calculations has  \( 32 \times 32 \)  Monkhorst-Pack k-point grids to sample the full Brillouin zone, 0.02 Ry cold smearing \( ^{56} \)  with SSSP pseudopotentials \( ^{57} \)  (efficiency version 0.7) and energy cutoffs recommended therein. PAW pseudopotentials were substituted because they are incompatible with the use of symmetry in the electron-phonon routines of QE. Other minor variations from the standard setup can be found in the AiiDA database provided. The use of cold smearing allows k-point convergence while keeping a lower effective temperature in the calculations, making the free-carrier screening closer to what it would be in real conditions. Spin-orbit interactions are included only for hole-doped  \( WSe_{2} \) , where they play a significant role. For other materials, while spin-orbit interactions may have an effect on the band structure in general (e.g., on the band gap for  \( BiSeTe_{2} \)  \( ^{17} \) ), they will not have large consequences on the conductivity or mobility as long as there is no significant energy splitting of valleys with opposite spins (small variations may come from changes in the effective masses). The analysis starts from a database of band structures computed (non-self-consistently) in the neutral material on very fine electronic momenta grids (about 90 by 90) to analyse the valley structure. These bands are then recomputed with field-effect doping for the selected materials. Phonon momenta are chosen to include only relevant transitions, and the Boltzmann transport equation (BTE) is solved as described in Ref. 13. We improved the stability for the solution of the BTE by using the velocity of each initial state as a fictitious electric field direction [Eq. (11) of Ref. 13].
 

## B. Boltzmann transport equation

The solution of the BTE is briefly outlined here for convenience; more details can be found in Ref. 13. The (longitudinal) conductivity is computed as follows:

 \[ \sigma=\frac{1}{\rho}=2e^{2}\int\frac{d\mathbf{k}}{(2\pi)^{2}}\left(\boldsymbol{v}(\mathbf{k})\cdot\boldsymbol{u}_{E}\right)^{2}\tau(\mathbf{k})\left[-\frac{\partial f^{0}(\varepsilon_{\mathbf{k}})}{\partial\varepsilon}\right] \quad (1) \] 

where e is the Coulomb charge, and  \( \kappa,\varepsilon_{\mathbf{k}},v(\mathbf{k}) \)  represent electronic momenta (and band index implicitly), energies, and velocities, respectively. The unit vector  \( u_{E} \)  points in the electric field's direction and  \( f^{0} \)  is the Fermi-Dirac distribution. Here  \( \tau \)  is an energy- and momentum-dependent variable that has the dimensions of time and solves the linearized BTE:

 \[ \begin{align*}(1-f^{0}(\mathbf{k}))v(\mathbf{k})\cdot\boldsymbol{u}_{E}=&\sum_{\mathbf{k}^{\prime}}P_{\mathbf{k}\mathbf{k}^{\prime}}(1-f^{0}(\mathbf{k}^{\prime}))\times\\&\{\boldsymbol{v}(\mathbf{k})\cdot\boldsymbol{u}_{E}\tau(\mathbf{k})-v(\mathbf{k}^{\prime})\cdot\boldsymbol{u}_{E}\tau(\mathbf{k}^{\prime})]\}\end{align*} \quad (2) \] 

 \( P_{kk'} \)  being the probability for an electron in state k to be scattered into state  \( k' \) . In the following we consider only phonon-induced scattering, so that:

 \[ \begin{align*}P_{\mathbf{k}\mathbf{k}^{\prime}+\mathbf{q}}=\sum_{\nu}\frac{2\pi}{\hbar}\frac{1}{N}|g_{\mathbf{k}\mathbf{k}+\mathbf{q},\nu}|^{2}\{n_{\mathbf{q},\nu}\delta(\varepsilon_{\mathbf{k}+\mathbf{q}}-\varepsilon_{\mathbf{k}}-\hbar\omega_{\mathbf{q},\nu})\\+&(n_{\mathbf{q},\nu}+1)\delta(\varepsilon_{\mathbf{k}+\mathbf{q}}-\varepsilon_{\mathbf{k}}+\hbar\omega_{\mathbf{q},\nu})\}.\end{align*} \quad (3) \] 

where  \( q, \nu, \hbar\omega_{q,\nu}, n_{q,\nu} \)  are phonon momenta, mode index, energy and occupations, and  \( g_{kk+q,\nu} \)  are the electron-phonon coupling matrix elements.

## III. HIGH-CONDUCTIVITY 2D SEMICONDUCTORS

We study in careful detail eleven monolayers obtained from our database of 256 easily exfoliable materials with at most 6 atoms per unit cell \( ^{23} \) , as available on the Materials Cloud \( ^{34,35} \)  and in the supplementary material of Ref. 23. The corresponding conductivity and mobility, as a function of the PBE gap, are shown in Fig. 1. At this doping level a conductivity of a few  \( e^{2}/h \)  is already considered good \( ^{4,8} \)  for a semiconductor, while the best graphene devices yield values around  \( 500\ e^{2}/h^{58,59} \) . The materials presented in this work are in the intermediary orders of magnitude, with conductivities of  \( 10\sim100\ e^{2}/h \) , and mobilities in the same range as bulk silicon ( \( 400\ cm^{2}/Vs \)  for holes,  \( 1400\ cm^{2}/Vs \)  for electrons).

In the following, we detail the exploration process that led to those materials. First, two well-known high-conductivity 2D semiconductors are analyzed to identify representative band features. We then search for those features within the Materials Cloud database \( ^{23,34} \)  and

![](./images/867772924138881971_1.jpg)

FIG. 1. Computed conductivities and mobilities at room temperature plotted against PBE gap for all the materials considered in this work. BTE is solved for a fixed carrier density of  \( n/p = 10^{13} \, cm^{-2} \)  (electrons or holes).

compute the transport properties of the most promising candidates. Electron-phonon scattering is analyzed in each monolayer. The suffix “-e” or “-h” is attached to the materials’ formula to indicate if either electron doping or hole doping is considered.

## A. Prototypical high-conductivity materials: InSe and P_{4}

We start by analyzing key features of two well-known semiconductors with excellent transport performance, InSe on the electron side (InSe-e) and phosphorene on the hole side (P_{4}-h). In the following we will use repeatedly two different plots to visualize, understand and compare the details of the transport properties of 2D materials, reported first in Fig. 2 for InSe and P_{4}. On the left, a “velocity plot” shows the band structure in a format that is relevant for transport. For each electronic state k (each black dot) on the fine k-point grid used for solving the BTE and within a certain energy range from the band edge (set as the origin of the y-axis), the energy  \( \varepsilon_{k} \)  is plotted against the norm of the velocity  \( |v| = |\frac{1}{\hbar}\nabla_{k}\varepsilon_{k}| \) , given in atomic Rydberg units (ARU) \( ^{60} \) . The spread indicates the anisotropy of the valley. The red scale of the background is proportional to the derivative of the Fermi-Dirac occupation at 300 K, thus highlighting the states participating in transport with a non-vanishing contribution to Eq. (1). The Fermi level is computed at room temperature (i.e. such that  \( \int_{\mathbf{k}} f^{0}(\varepsilon_{\mathbf{k}}, T) d\mathbf{k}/(2\pi^{2}) = 10^{13} \, \text{cm}^{-2} \)  for electrons, and similarly for holes). On the right side, a “scattering plot” shows where and how easily a certain initial state can be scattered. The initial state at  \( k_{in} \) , indicated by a black square, is chosen to be at the Fermi level (and in the transport direction, when rel-
 

evant). The grey shading shows the morphology of the valley(s) considered for transport. The red color scale represents an effective coupling constant  \( g_{eff} \)  which accounts for all phonon modes, their occupation at 300 K, and energy conservation, since this quantity can be meaningfully compared between materials. In practice,  \( g_{eff} \)  is defined as the square root of the sum of the interpolated  \( |g_{\mathbf{k}_{in},\mathbf{k}_{in}+\mathbf{q},\nu}|^{2}n_{\mathbf{q},\nu} \)  (or  \( n_{q,\nu} + 1 \) ) over all  \( \nu \)  and q that fulfill energy conservation during phonon absorption (or emission) when the final state at  \( k_{in} + q \)  falls into a certain zone (the valley being tessellated into triangles). The value given at the top of each scattering plot is the lifetime of the initial state computed within the momentum relaxation time approximation:

 \[ \frac{1}{\tau(\mathbf{k})}=\sum_{\mathbf{k}^{\prime}}P_{\mathbf{k}\mathbf{k}^{\prime}}\frac{1-f^{0}(\mathbf{k}^{\prime})}{1-f^{0}(\mathrm{k})}\times\left\{1-\frac{\mathbf{v}(\mathbf{k}^{\prime})\cdot\mathbf{v}(\mathbf{k})}{\mathbf{v}(\mathbf{k})^{2}}\right\} \quad (4) \] 

Everything is computed at 300 K, with the corresponding chemical potential in  \( f^{0} \) .

We now discuss qualitatively the features allowing electron-doped InSe and hole-doped phosphorene to maximize the conductivity in Eq. (1): this is a sum over electronic states weighted by the derivative of the Fermi-Dirac occupation. The weight effectively selects states around the chemical potential within an energy range that scales with temperature, as represented in the left panels of Fig. 2. The rest of the integrand can be separated in two contributions: i) one from scattering (electron-phonon here) through the scattering lifetime  \( \tau \) ; ii) and one from the velocity of the carriers v projected along the transport direction  \( u_{E} \) .

The scattering contribution i) is inversely proportional to the strength of the EPI and the amount of states available for scattering (as apparent in Eq. (4)), i.e. the density of states (DOS) within a certain energy window around the initial states, depending on the energy of the phonons involved. We note, however, that the DOS contribution is essentially compensated when doing the integral over electronic states to get the conductivity, Eq. (1). To maximize  \( \tau \) , the quantity to focus on is thus the strength of the EPI, which should of course be minimized. Weak EPIs is a feature shared by InSe and phosphorene.

There are different ways to maximize the velocity contribution ii); in general, one needs to maximize the velocity in the direction of transport. In the case of InSe, the velocity is isotropic and very large, with a small effective mass. Accordingly, the DOS is low and the Fermi level reaches high energies above the valley edge, towards higher velocities, eventually saturating at a maximal value in case of non-parabolic materials. The benefits of a such a steep and deep single valley is that current carrying states around the chemical potential have high velocities, as also pointed out in Ref. 33. In the contrasting case of phosphorene, the valley is highly anisotropic. Provided one chooses the low effective mass direction for transport, the projection of the velocity in the transport direction is maximized. However, the DOS here is relatively larger, and the Fermi level stays closer to the band edge, where velocities are lower. The good performance of phosphorene thus relies on a somewhat more fragile balance.

An essential feature to maximize both i) and ii) is to work with single valley materials. Single valley band structures lead to a lower DOS, higher Fermi level and higher velocities. Even more compelling, one avoids intervalley scattering, which is usually stronger than intravalley scattering and hinders transport \( ^{13} \) .

In a related work \( ^{26} \) , several promising materials for ultra-short transistor devices have been identified. In that situation, one optimizes the performance of the material in the ballistic limit and the role of electron-phonon scattering is secondary, since the channels are usually below the scattering length. Thus, maximizing both the velocity in the transport direction and the DOS is extremely beneficial, and anisotropic and multivalley materials are interesting. When electron-phonon scattering is turned on, multivalley band structures are not ideal, while anisotropy can remain relevant.

## B. More like InSe: Steep and deep single-valleys

As shown in Fig. 2, InSe has a sharp and deep single electron valley, with carrier velocities close to 6 ARU at the Fermi level when  \( n = 10^{13} \)  cm \( ^{-2} \)  (roughly 6 times larger than the Fermi velocity in graphene,  \( \sim 1 \)  ARU). Steep isotropic valleys are obviously characterized by low DOS, which means that the Fermi level quickly shifts away from the band edge with increasing carrier density. This allows to reach higher carrier velocities, but it often means that the Fermi level reaches other valleys in the band structure. In that case, the aforementioned benefits of the single valley structure are lost. If the Fermi level is close to the edges of the next valleys, intervalley scattering is activated and the new states populated are not helping to conduct due to their low velocity. Note that, in a similar spirit, the suppression of intervalley scattering via valley-engineering (e.g. through strain) has been proposed \( ^{61} \)  to enhance the transport properties of multivalley materials such as arsenene. Thus, a steep valley is not sufficient to have good transport performance: it must also be deep. More precisely, higher-energy valleys need to be far enough for the material to operate effectively as a single valley material for a doping of  \( 10^{13} \)  cm \( ^{-2} \) .

We look for such valleys among the exfoliable materials in our study set. We use band structures computed on very fine grids in the neutral materials and select materials with positive phonons, a limited gap  \( E_{g} < 2.5 \)  eV, a single valley (within 100 meV of the Fermi level), and a maximum Fermi velocity  \( |v_{max}| > 6 \)  ARU. This allows us to identify BiClTe-e, AlLiTe \( _{2} \) -e, GaSe-e, Bi \( _{2} \) SeTe \( _{2} \) -e, Bi \( _{2} \) STe \( _{2} \) -e, Bi \( _{2} \) Se \( _{3} \) -e, and Sb \( _{2} \) SeTe \( _{2} \) -e as promising candidates. Electron-phonon scattering
 
![](./images/867772924138881971_2.jpg)

FIG. 2. Transport properties of InSe and phosphorene  \( \left(\mathrm{P}_{4}\right) \) , two well-known good conductors. On the left, the “velocity plot” shows, for each electronic state k in the valley, the energy  \( \varepsilon_{k} \)  from the band edge plotted against the norm of the velocity  \( |v|=|\frac{1}{h}\nabla_{k}\varepsilon_{k}| \) , in atomic Rydberg units (ARU). The color scale of the background is proportional to the derivative of the Fermi-Dirac distribution, which appears in Eq. (1). On the right, the “scattering plot” shows where an initial state (black square) can be scattered within the valley (grey shade). The color scale represents the effective coupling constant  \( g_{eff} \) , which accounts for all phonon modes, their occupation at 300 K, and energy conservation. At the top,  \( \tau \)  is the scattering time of the initial state computed within the momentum relaxation time approximation, Eq. (4).

is studied for these monolayers (except  \( Bi_{2}Se_{2}-e \) , a bit redundant with respect to the other two members of the  \( Bi_{2}X_{3} \)  family). The results are shown in Fig. 3 for  \( Bi_{2}SeTe_{2}-e \)  and  \( AlLiTe_{2}-e, \)  and in the appendix for the rest. The general similarity of the plots indicates at a glance why these materials have similar transport properties. The carrier velocities at the Fermi level, the strength of EPI, and the scattering times are of similar orders of magnitude. A closer look reveals the reasons underlying their precise ranking.  \( BiSeTe_{2}-e \) ,  \( BiSe_{3}-e \) , and  \( Sb_{2}SeTe_{2}-e \)  are very similar in terms of chemistry, band structure, and phonons.  \( BiSeTe_{2}-e \)  (see Fig. 3) displays the highest conductivity ( \( \sigma = 42 e^{2}/h \) ), combining some of the weakest EPI with the largest velocities. It is followed by  \( Sb_{2}SeTe_{2}-e \)  ( \( \sigma = 30 e^{2}/h \) ) with similar EPI but slightly smaller velocities.  \( Bi_{2}Se_{3}-e \)  ( \( \sigma = 14 e^{2}/h \) ) also has a very sharp valley, but the EPI is 2 to 3 times stronger. As could be expected, electron-phonon scattering in GaSe-e ( \( \sigma = 25 e^{2}/h \) ) is similar to InSe-e ( \( \sigma = 20 e^{2}/h \) ), with scattering times differing by only  \( \sim 10\% \) . GaSe-e owes its higher conductivity mostly to a sharper valley and higher velocities. Finally,  \( AlLiTe_{2}-e \)  ( \( \sigma = 18 e^{2}/h \) , see Fig. 3) and  \( BiClTe-e \)  ( \( \sigma = 16 e^{2}/h \) ) have slightly larger velocities but stronger EPIs than InSe-e, making them slightly less conductive. Note that all these systems with sharp valleys are electron-doped, which may be rationalized by considering that conduction bands are more often made of delocalized non-bonding states which tend to be more dispersive. Despite the valleys being very similar (isotropic with  \( |v_{max}| \approx 6 \sim 7 \)  ARU), the conductivity varies from 14 to  \( 42 e^{2}/h \) . This points to the importance of accounting for the details of EPIs to rank materials accurately.

We also note that the selection process does not guarantee to find all the best conductors, as demonstrated by the example of  \( WSe_{2}-h \) : TMDs were not selected because they are not single-valley (also their Fermi velocities would be too small). However, thanks to strong spin-orbit interactions, the hole side of TMDs can be considered to be in the steep and deep single valley category. Indeed, as is well known, the hole valleys associated to opposite spin textures split very strongly in energy, of the
 
![](./images/867772924138881971_3.jpg)

![](./images/867772924138881971_4.jpg)

FIG. 3. Transport properties of  \( Bi_{2}SeTe_{2} \)  ( \( \sigma = 42 e^{2}/h \) ) and  \( AlLiTe_{2} \)  ( \( \sigma = 18 e^{2}/h \) ), showing the velocity (left) and scattering (plots) as described in Fig. 2. Both monolayers belong to a category of materials with steep and deep single valleys in the conduction band. Similar plots are given in App. B for other monolayers in this category: BiClTe-e, GaSe-e,  \( Bi_{2}SeTe_{2} \) -e,  \( Bi_{3}Se_{3} \) -e, and  \( Sb_{2}SeTe_{2} \) -e.

![](./images/867772924138881971_5.jpg)

FIG. 4. Transport properties of WSe \( _{2} \) -h ( \( \sigma = 81 e^{2}/h \) ), showing the velocity (left) and scattering (plots) as described in Fig. 2. Thanks to spin-orbit interactions, weak spin-flip scattering, and the effective absence of any valley at  \( \Gamma \) , spins travel in parallel channels not connected to each other.

order of 100 meV, making the lower valleys irrelevant for transport. One effectively obtains two valleys at K and  \( K' \)  with opposite spin textures. WSe \( _{2} \) -h, at least within our computational framework, also has the advantage that the edge of the valence band at  \( \Gamma \)  is quite low, eliminating a potential intervalley scattering channel. Furthermore, as shown in Fig. 4, the intervalley scattering, associated with spin-flip EPIs, is weak ( \( < 10 \)  meV) compared to intravalley, spin-conserving EPIs ( \( \sim 50 \)  meV). This implies that the two valleys are effectively decou-
 

pled as far as phonon-limited transport is concerned and transport is similar to the single valley case, except opposite spins travel in separate channels located at different points in the Brillouin zone. Comparing with the isotropic single-valley materials discussed above, WSe \( _{2} \) -h has velocities half as small but EPIs at least 3 times weaker, leading to the largest conductivity  \( (\sigma = 81 e^{2}/h) \) . This high value is due to the (effective) absence of the  \( \Gamma \)  valley. Indeed, opposite spins are degenerate at  \( \Gamma \) , and if the  \( \Gamma \)  valley were accessible for scattering, intervalley scattering from both K and K' would be quite strong. In addition, as shown in Ref. 61, multi-valley occupations enhances the intravalley coupling to the homopolar optical phonon mode by making free-carrier screening inefficient. At any rate, the extraordinarily weak EPI in WSe \( _{2} \) -h is tied to subtle spin-orbit and screening effects that are difficult to predict and highlights the limitations of simple selection processes based solely on the band structure.

## C. More like phosphorene: anisotropic single valleys

In contrast with the fairly isotropic band structures of InSe, the case of phosphorene showed that anisotropy can also lead to good performance. So, we look for similar materials in our database, having stable phonons, single valleys and small band gap at the PBE level ( \( E_{g} < 2.5 \)  eV). This time we filter materials keeping materials that combine high velocity ratios ( \( \frac{v_{max}}{v_{max}} < 1.7 \) ) and a decent maximum velocity ( \( v_{max} > 2.0 \)  ARU) at the Fermi level. These search criteria allow us to identify Au-Ih, and ClGaTe-h as well as the electron-side of  \( P_{4} \) -e as promising candidates. The electron side of phosphorene is a similar, less pronounced version of the hole side, and was already studied in our previous work \( ^{13} \) . Thus, we focus here on ClGaTe-h ( \( \sigma = 13 e^{2}/h \) ) and Au-Ih ( \( \sigma = 14 e^{2}/h \) ).

The results of the electron-phonon calculations are plotted in Fig. 5. The spread of the velocity traces indicates high anisotropy, the velocity varying by a factor 2 at a given energy. The high-velocity direction preferable for transport is x for ClGaTe and  \( x + y \)  for AuI. The anisotropy allows one to benefit from many high velocity states, thanks to a flatter band in the direction perpendicular to transport. However, if the band is too flat and the DOS too high, the Fermi level stays close to the band edges and the velocities are too low. Here, velocities of the order of  \( 3 \sim 4 \)  ARU ensure good transport properties. While ClGaTe-h and AuI-h share the anisotropic character of phosphorene, their conductivity remains lower, which in part reflects the fact that the good transport properties of anisotropic materials rely on a more fragile balance of features.

A closer look at the scattering plots in Fig. 5, contrasted with phosphorene in Fig. 2 further reveals the reasons behind phosphorene's superior conductivity. In addition to generally weaker EPIs (which is partly due to the monoatomic nature of  \( P_{4} \) , eliminating all Born effective charge and piezoelectric couplings), one can observe in  \( P_{4} \)  a predominance of "side-scattering": states in the direction of transport are mostly scattered to states on the sides of the valley with velocities perpendicular to the direction of transport. As can be seen from Eq. (4), this leads to a longer scattering times, since the term involving a scalar product of the velocities vanishes. The contribution of the DOS from the integral of the conductivity usually cancels out with the integral over available scattering states. This is not the case here because we benefit from the larger weight of high velocity states in the conductivity integral while having less dense, low-velocity states in the scattering integral. Thus, "side scattering" definitely brings the performance of  \( P_{4} \) -h from great to exceptional. ClGaTe-h is similar to  \( P_{4} \)  in terms of velocities, but the EPI is stronger and, importantly, mostly backscattering. The scattering time is consequently 10 times larger. Au-Ih has lower velocities and higher EPI.

While targeting the band features of phosphorene has allowed us to find other excellent candidates, we see that the essence of its exceptional performance comes from something much harder to identify at the level of a database: the anisotropy of its electron-phonon interactions. Thus, phosphorene is at the same time both a prototype and an example of the limitations of selection processes based on band structures.

## IV. CONCLUSIONS

State-of-the-art density-functional perturbation theory and the Boltzmann transport equation are used to study the outstanding transport properties of several 2D semiconductors. Focusing on conductivity at a fixed density of  \( n/p = 10^{13} \, cm^{-2} \) , the present results offer a complementary perspective with respect to most first-principles calculations valid in the zero carrier density limit. We provide a detailed analysis of electron-phonon scattering in two well-known high-conductivity systems: electron-doped InSe and hole-doped phosphorene. While they share some features –like weak EPI and a single-valley electronic structure– they exemplify two different strategies to maximize the conductivity. InSe's high-velocity, isotropic valley can be exploited thanks to the fact that the next valleys are much higher in energy. Phosphorene, instead, owes its excellent transport performance to the anisotropy of both its band structure and electron-phonon scattering. Analyzing the band properties of around  \( \sim 150 \)  small stable semiconductors with 6 atoms or less in the unit-cell, from the Materials Cloud, we identify systems with band features similar to either InSe or phosphorene. We find large phonon-limited conductivities for electron-doped  \( Bi_{2}SeTe_{2} \) ,  \( Bi_{2}S_{3} \) , BiClTe,  \( Sb_{2}SeTe_{2} \) , AlLiTe, and GaSe, as well as hole-doped AuI, ClGaTe, and WSe \( _{2} \) . These results confirm that the band structure landscape plays an important role in determining transport and shows that seeking peculiar features
 
![](./images/867772924138881971_6.jpg)

![](./images/867772924138881971_7.jpg)

![](./images/867772924138881971_8.jpg)

![](./images/867772924138881971_9.jpg)

FIG. 5. Transport properties of ClGaTe and AuI showing the velocity (left) and scattering (right) plots as described in Fig. 2. Anisotropic valleys imply there is one optimal transport direction, corresponding to higher velocities. Initial states (marked with a black square) are chosen to be in that direction.

in the electronic structure does lead to high-performance materials. Nevertheless, we also show how the details of the strength and angular dependency of electron-phonon scattering play a critical role in ranking those materials with respect to each other.

## ACKNOWLEDGEMENTS:

The authors are grateful to Davide Campi for sharing the initial band structures. This work has been in part supported by NCCR MARVEL. Simulation time was awarded by PRACE on Marconi at Cineca, Italy (project id. 2016163963). Computational resources have been provided by the Consortium des quipements de Calcul Intensif (CCI), funded by the Fonds de la Recherche Scientifique de Belgique (F.R.S.-FNRS) under Grant No. 2.5020.11 and by the Walloon Region. T.S. acknowledges support from the University of Liege under Special Funds for Research, IPD-STEMA Programme. M.G. acknowledges support by the Italian Ministry for University and Research through the Levi-Montalcini program and by the Swiss National Science Foundation (SNSF) through the Ambizione program (grant PZ00P2_174056).

 \( ^{1} \)  S. Z. Butler et al., Progress, challenges, and opportunities in two-dimensional materials beyond graphene., ACS nano 7, 2898 (2013).

 \( ^{2} \)  D. Akinwande, N. Petrone, and J. Hone, Two-dimensional flexible nanoelectronics, Nature Communications 5, 5678 (2014).

 \( ^{3} \)  M. Chhowalla, D. Jena, and H. Zhang, Two-dimensional semiconductors for transistors, Nature Reviews Materials 1, 16052 (2016).

 \( ^{4} \)  B. Radisavljevic and A. Kis, Mobility engineering and a metal-insulator transition in monolayer  \( MoS_{2} \) , Nature Materials 12, 815 (2013).

 \( ^{5} \)  B. Radisavljevic, A. Radenovic, J. Brivio, V. Giacometti, and A. Kis, Single-layer  \( MoS_{2} \)  transistors, Nature nanotechnology 6, 147 (2011).

 \( ^{6} \)  X. Li, Z. Yu, X. Xiong, T. Li, T. Gao, R. Wang, R. Huang, and Y. Wu, High-speed black phosphorus field-effect transistors approaching ballistic limit, Science Advances 5
 

(2019).

 \( ^{7} \)  L. Li et al., Black phosphorus field-effect transistors., Nat. Nanotechnol. 9, 372 (2014).

 \( ^{8} \)  L. Tao, E. Cinquanta, D. Chiappe, C. Grazianetti, M. Fanciulli, M. Dubey, A. Molle, and D. Akinwande, Silicene field-effect transistors operating at room temperature, Nature Nanotechnology 10, 227 (2015).

 \( ^{9} \)  X. Li, J. T. Mullen, Z. Jin, K. M. Borysenko, M. Buongiorno Nardelli, and K. W. Kim, Intrinsic electrical transport properties of monolayer silicene and MoS \( _{2} \)  from first principles, Physical Review B - Condensed Matter and Materials Physics 87, 115418 (2013).

 \( ^{10} \)  W. Li, Electrical transport limited by electron-phonon coupling from Boltzmann transport equation: An ab initio study of Si, Al, and MoS \( _{2} \) , Physical Review B 92, 075405 (2015).

 \( ^{11} \)  K. Kaasbjerg, K. S. Thygesen, and K. W. Jacobsen, Phonon-limited mobility in n-type single-layer  \( MoS_{2} \)  from first principles, Physical Review B - Condensed Matter and Materials Physics 85, 115317 (2012).

 \( ^{12} \)  T. Gunst, T. Markussen, K. Stokbro, and M. Brandbyge, First-principles method for electron-phonon coupling and electron mobility: Applications to two-dimensional materials, Physical Review B 93, 035414 (2016).

 \( ^{13} \)  T. Sohier, D. Campi, N. Marzari, and M. Gibertini, Mobility of 2D materials from first principles in an accurate and automated framework, Physical Review Materials 2, 114010 (2018).

 \( ^{14} \)  A. N. Rudenko, S. Brener, and M. I. Katsnelson, Intrinsic Charge Carrier Mobility in Single-Layer Black Phosphorus, Physical Review Letters 116, 246401 (2016).

 \( ^{15} \)  Y. Trushkov and V. Perebeinos, Phonon-limited carrier mobility in monolayer black phosphorus, Physical Review B 95, 075436 (2017).

 \( ^{16} \)  G. Gaddemane, W. G. Vandenberghe, M. L. Van De Put, S. Chen, S. Tiwari, E. Chen, and M. V. Fischetti, Theoretical studies of electronic transport in monolayer and bilayer phosphorene: A critical overview, Physical Review B 98 (2018).

 \( ^{17} \)  B. Wang, X. Niu, Y. Ouyang, Q. Zhou, and J. Wang, Ultrathin Semiconducting  \( Bi_{2}Te_{2}S \)  and  \( Bi_{2}T_{e2}Se \)  with High Electron Mobilities, The Journal of Physical Chemistry Letters 9, 487 (2018).

 \( ^{18} \)  S. Takagi, A. Toriumi, M. Iwase, and H. Tango, On the universality of inversion layer mobility in Si MOSFET's: Part I-effects of substrate impurity concentration, IEEE Transactions on Electron Devices 41, 2357 (1994).

 \( ^{19} \)  G. Gaddemane, S. Gopalan, M. Van de Put, and M. V. Fischetti, Limitations of ab initio methods to predict the electronic-transport properties of two-dimensional materials: The computational example of 2H-phase transition metal dichalcogenides, arXiv:1912.03795 (2019).

 \( ^{20} \)  G. Cheon, K.-A. N. Duerloo, A. D. Sendek, C. Porter, Y. Chen, and E. J. Reed, Data Mining for New Two- and One-Dimensional Weakly Bonded Solids and Lattice-Commensurate Heterostructures, Nano Letters 17, 1915 (2017).

 \( ^{21} \)  M. Ashton, J. Paul, S. B. Sinnott, and R. G. Hennig, Topology-Scaling Identification of Layered Solids and Stable Exfoliated 2D Materials, Physical Review Letters 118, 106101 (2017).

 \( ^{22} \)  K. Choudhary, I. Kalish, R. Beams, and F. Tavazza, High-throughput Identification and Characterization of Two-dimensional Materials using Density functional theory,

Scientific Reports 7, 5179 (2017).

 \( ^{23} \)  N. Mounet et al., Two-dimensional materials from high-throughput computational exfoliation of experimentally known compounds, Nature Nanotechnology 13, 246 (2018).

 \( ^{24} \)  S. Haastrup et al., The Computational 2D Materials Database: high-throughput modeling and discovery of atomically thin crystals, 2D Materials 5, 042002 (2018).

 \( ^{25} \)  J. Zhou et al., 2DMatPedia, an open computational database of two-dimensional materials from top-down and bottom-up approaches, Scientific Data 6, 86 (2019).

 \( ^{26} \)  C. Klinkert, Á. Szabó, C. Stieger, D. Campi, N. Marzari, and M. Luisier, 2-D Materials for Ultrascaled Field-Effect Transistors: One Hundred Candidates under the Ab Initio Microscope, ACS Nano 14, 8605 (2020).

 \( ^{27} \)  F. Giustino, Electron-phonon interactions from first principles, Reviews of Modern Physics 89, 015003 (2017).

 \( ^{28} \)  S. Poncé, W. Li, S. Reichardt, and F. Giustino, First-principles calculations of charge carrier mobility and conductivity in bulk semiconductors and two-dimensional materials, Reports on Progress in Physics 83, 036501 (2020).

 \( ^{29} \)  C.-H. Park, N. Bonini, T. Sohier, G. Samsonidze, B. Kozinsky, M. Calandra, F. Mauri, and N. Marzari, Electron-Phonon Interactions and the Intrinsic Electrical Resistivity of Graphene., Nano letters 14, 1113 (2014).

 \( ^{30} \)  T. Sohier, M. Calandra, C.-H. C.-H. Park, N. Bonini, N. Marzari, and F. Mauri, Phonon-limited resistivity of graphene by first-principles calculations: Electron-phonon interactions, strain-induced gauge field, and Boltzmann equation, Physical Review B 90, 125414 (2014).

 \( ^{31} \)  S. Poncé, E. Margine, C. Verdi, and F. Giustino, EPW: Electron-phonon coupling, transport and superconducting properties using maximally localized Wannier functions, Computer Physics Communications 209, 116 (2016).

 \( ^{32} \)  J.-J. Zhou, J. Park, I.-T. Lu, I. Maliyov, X. Tong, and M. Bernardi, Perturbo: a software package for ab initio electron-phonon interactions, charge transport and ultrafast dynamics, arXiv:2002.02045 (2020).

 \( ^{33} \)  L. Cheng, C. Zhang, and Y. Liu, The Optimal Electronic Structure for High-Mobility 2D Semiconductors: Exceptionally High Hole Mobility in 2D Antimony, Journal of the American Chemical Society 141, 16296 (2019).

 \( ^{34} \)  https://www.materialscloud.org/discover/2dstructures/.

 \( ^{35} \)  L. Talirz et al., Materials Cloud, a platform for open computational science, arXiv:2003.12510 (2020).

 \( ^{36} \)  G. Brunin et al., Phonon-limited electron mobility in Si, GaAs and GaP using plane waves and Bloch states, arXiv:2002.00630 (2020).

 \( ^{37} \)  G. Pizzi, A. Cepellotti, R. Sabatini, N. Marzari, and B. Kozinsky, AviDA: automated interactive infrastructure and database for computational science, Computational Materials Science 111, 218 (2016).

 \( ^{38} \)  S. P. Huber et al., AviDA 1.0, a scalable computational infrastructure for automated reproducible workflows and data provenance, arXiv:2003.12476 (2020).

 \( ^{39} \)  https://doi.org/10.24435/materialscloud:fr-r0.

 \( ^{40} \)  Y. Zhang, J. Ye, Y. Matsuhashi, and Y. Iwasa, Ambipolar  \( MoS_{2} \)  Thin Flake Transistors, Nano Letters 12, 1136 (2012).

 \( ^{41} \)  D. Braga, I. Gutiérrez Lezama, H. Berger, and A. F. Morpurgo, Quantitative Determination of the Band Gap of  \( WS_{2} \)  with Ambipolar Ionic Liquid-Gated Transistors, Nano Letters 12, 5218 (2012).
 

 \( ^{42} \)  J. T. Ye, Y. J. Zhang, R. Akashi, M. S. Bahramy, R. Arita, and Y. Iwasa, Superconducting Dome in a Gate-Tuned Band Insulator, Science 338, 1193 (2012).

 \( ^{43} \)  T. Sohier, M. Calandra, and F. Mauri, Density functional perturbation theory for gated two-dimensional heterostructures: Theoretical developments and application to flexural phonons in graphene, Physical Review B 96, 075448 (2017).

 \( ^{44} \)  W. Li, S. Poncé, and F. Giustino, Dimensional Crossover in the Carrier Mobility of Two-Dimensional Semiconductors: The Case of InSe, Nano Letters 19, 1774 (2019).

 \( ^{45} \)  W. Zhang, R. Yu, H. J. Zhang, X. Dai, and Z. Fang, First-principles studies of the three-dimensional strong topological insulators  \( Bi_{2}Te_{3} \) ,  \( Bi_{2}S_{e3} \)  and  \( Sb_{2}Te_{3} \) , New Journal of Physics 12, 065013 (2010).

 \( ^{46} \)  S. Jafarpisheh, A. Ju, K. Janßen, T. Taniguchi, K. Watanabe, C. Stampfer, and B. Beschoten, Reducing the Impact of Bulk Doping on Transport Properties of Bi-Based 3D Topological Insulators, Physica Status Solidi (B) Basic Research, pssb.202000021 (2020).

 \( ^{47} \)  Y. Liu, Y. Xu, Y. Ji, and H. Zhang, Monolayer  \( Bi_{2}Se_{3-x}Te_{x} \) : novel two dimensional semiconductors with excellent stability and high electron mobility, Physical Chemistry Chemical Physics 22, 9685 (2020).

 \( ^{48} \)  C. Tang, L. Zhang, C. Zhang, J. Macleod, K. Ostrikov, and A. Du, Highly stable two-dimensional gold selenide with large in-plane anisotropy and ultrahigh carrier mobility, Nanoscale Horizons 5, 366 (2020).

 \( ^{49} \)  H. Qu, W. Zhou, S. Guo, Z. Li, Y. Wang, and S. Zhang, Ballistic Quantum Transport of Sub10 nm 2D  \( Sb_{2}Te_{2}Se \)  Transistors, Advanced Electronic Materials 5, 1900813 (2019).

 \( ^{50} \)  J. Chen, X. Tan, P. Lin, B. Sa, J. Zhou, Y. Zhang, C. Wen, and Z. Sun, Comprehensive understanding of intrinsic mobility in the monolayers of III-VI group 2D materials, Physical Chemistry Chemical Physics 21, 21898 (2019).

 \( ^{51} \)  P. Giannozzi et al., QUANTUM ESPRESSO: a modular and open-source software project for quantum simulations of materials., Journal of Physics: Condensed Matter 21, 395502 (2009).

 \( ^{52} \)  P. Giannozzi et al., Advanced capabilities for materials modelling with Quantum ESPRESSO, Journal of Physics Condensed Matter 29, 465901 (2017).

 \( ^{53} \)  J. P. Perdew, K. Burke, and M. Ernzerhof, Generalized Gradient Approximation Made Simple, Physical Review Letters 77, 3865 (1996).

 \( ^{54} \)  T. Sohier, M. Gibertini, M. Calandra, F. Mauri, and N. Marzari, Breakdown of Optical Phonons' Splitting in Two-Dimensional Materials, Nano Letters 17, 3758 (2017).

 \( ^{55} \)  T. Sohier, M. Calandra, and F. Mauri, Density-functional calculation of static screening in two-dimensional materials: The long-wavelength dielectric function of graphene, Physical Review B 91, 165428 (2015).

 \( ^{56} \)  N. Marzari, D. Vanderbilt, A. De Vita, and M. C. Payne, Thermal contraction and disordering of the al(110) surface, Physical Review Letters (1999).

 \( ^{57} \)  G. Prandini, A. Marrazzo, I. E. Castelli, N. Mounet, and N. Marzari, Precision and efficiency in solid-state pseudopotential calculations, npj Computational Materials 4, 72 (2018).

 \( ^{58} \)  L. Wang et al., One-dimensional electrical contact to a two-dimensional material., Science 342, 614 (2013).

 \( ^{59} \)  L. Banszerus et al., Extraordinary high room-temperature carrier mobility in graphene- \( WSe_{2} \)  heterostructures, arXiv:1909.09523 (2019).

 \( ^{60} \)  Atomic Rydberg units are the most convenient units for velocity in materials. Typical Fermi velocities in the database –including graphene– are on the order of 1 ARU, which corresponds to  \( \sim10^{6} \)  m/s.

 \( ^{61} \)  T. Sohier, E. Ponomarev, M. Gibertini, H. Berger, N. Marzari, N. Ubrig, and A. F. Morpurgo, Enhanced Electron-Phonon Interaction in Multivalley Materials, Physical Review X 9, 031019 (2019).

 \( ^{62} \)  N. Ma and D. Jena, Charge scattering and mobility in atomically thin semiconductors, Physical Review X 4, 011043 (2014).

 \( ^{63} \)  C. Verdi, F. Caruso, and F. Giustino, Origin of the crossover from polarons to Fermi liquids in transition metal oxides, Nature Communications 8, 15769 (2017).

 \( ^{64} \)  P. Bogulsawski and J. Mycielski, Is the deformation potential in semiconductors screened by free carriers?, Journal of Physics C: Solid State Physics 10, 2413 (1977).

 \( ^{65} \)  P. Boguslawski, Screening of the deformation potential by free electrons in the multivalley conduction band, Journal of Physics C: Solid State Physics 10, L417 (1977).

 \( ^{66} \)  P. Boguslawski and J. Mycielski, Free-electron screening of short-range scattering potentials in semiconductors, Journal of Physics C: Solid State Physics 13, 1019 (1980).

 \( ^{67} \)  M. Verstraete and X. Gonze, Smearing scheme for finite-temperature electronic-structure calculations, Physical Review B 65, 035111 (2001).

 \( ^{68} \)  J. Ma, D. Xu, R. Hu, and X. Luo, Examining two-dimensional Fröhlich model and enhancing the electron mobility of monolayer InSe by dielectric engineering, Journal of Applied Physics 128, 035107 (2020).
 

## Appendix A: Comments on doping-dependent transport performance

The mobility is a typical figure of merit for “transport performance”: It depends on doping (i.e. the carrier density induced by field effects), and the relevant doping range might vary with the application. Most first-principles computations of mobility are done in the zero carrier density limit  \( \mu_{0} = \lim_{n \to 0} \mu \) . Here, instead, we focus on 2D semiconductors with high conductivity  \( \sigma \)  at a fixed carrier density of  \( n/p = 10^{13} \, cm^{-2} \) . Of course, by optimizing  \( \sigma \)  we also maximize the mobility  \( \mu = \frac{\sigma}{\epsilon n/p} \)  at this particular density, denoted with  \( \mu_{13} \) . It should be highlighted that, in general,  \( \mu_{0} \neq \mu_{13} \) , and the variation of the mobility in between these two doping regimes is not obvious to predict.

The low (but finite) doping regime is very challenging to simulate realistically. The chemical potential is below the band edge and depends strongly on temperature. One would ideally run one simulation per temperature, with an electronic smearing corresponding to this temperature and an accordingly dense grid of k-points. Unfortunately, even room temperature corresponds to a very low electronic smearing compared to standard DFT and DFPT calculations, resulting in very dense grids of k-points and prohibitively expensive calculations (especially when studying many materials as in this work). This issue is usually circumvented by simulating the neutral system and computing only  \( \mu_{0} \) . Sometimes, the most obvious consequence of doping, i.e. screening form free carriers, is added as an analytical post-processing correction \( ^{62,63} \) , but which scattering sources should be screened by free carriers, and how, has been debated \( ^{64-66} \) . Moreover, field effects and screening can have non-trivial consequences, as demonstrated in TMDs \( ^{61} \)  or in graphene \( ^{43} \) . In this work we choose to fully account for doping in the calculations, but at relatively high carrier density. This allows us to perform more realistic calculations, easier to converge, with a chemical potential within the band and a well-defined Fermi surface. We use a smearing that is large compared to room temperature in order to have accurate results with affordable k-point grids, but the “cold” nature of the smearing \( ^{56} \)  allows to get closer to room temperature conditions. The effects of smearing can be significant at low doping, when the chemical potential is in the gap; at the high doping levels considered here, however, we expect the calculations to be representative of room-temperature conditions. Note that an alternative consistent approach to smear a finite temperature Fermi-Dirac distribution has been put forward \( ^{67} \) , but it is not implemented in our computational framework.

To predict the behavior of the mobility as doping decreases, one needs to account for the variation of electron-phonon interactions. If the strength of EPIs are constant, simple models using quadratic bands and elastic scattering show that the mobility is roughly constant \( ^{62} \)  up to fairly large dopings and then decreases. Considering inelastic scattering increases mobility at small doping because there are no more available states for phonon emission close to the band edge. In any case, maximizing  \( \mu_{13} \)  implies maximizing  \( \mu_{\Omega} \) . However, for the materials considered here, EPIs are likely to be at least partially doping-dependent via free-carrier screening. Indeed, those are all single-valley materials, implying that scattering is dominated by momenta smaller than the size of the Fermi surface, where free carriers screening is efficient. If all EPI were sensitive to free-carrier screening, we would see an opposite trend, with mobility increasing as a function of doping \( ^{62} \) , as free carriers screen the scattering sources.  \( \mu_{0} \)  might be then significantly lower than the  \( \mu_{13} \)  computed here. In practice, the magnitude of this trend will depend on which EPIs are sensitive to screening and how strong the bare EPIs are.

The electron-doped materials studied here (InSe, GaSe,  \( Bi_{2}SeTe_{2} \) ,  \( Sb_{2}SeTe_2 \) ) have strong Born effective charges and Fröhlich couplings, which is screening-sensitive and sharply increases at small momenta. For InSe, we compute  \( \mu_{13} \approx 490 \, cm^{2}/Vs \) , compared to  \( \mu_{0} \approx 100 \, cm^{2}/Vs \)  computed in Refs. 44 and 68 including polar effects and  \( \mu_{0} = 488 \, cm^{2}/Vs \)  when the Fröhlich coupling is suppressed \( ^{68} \)  (as due to screening). Similar trends are expected for the other electron-doped materials in this work. Whether  \( \mu_{0} \)  or  \( \mu_{13} \)  is more relevant to a certain operating doping range depends on the critical carrier density at which free-carrier screening becomes efficient. In 2D and assuming a constant density of states per area D, one can derive  \( n = k_{B}TD \ln \left[1 + e^{\frac{\mu_{F} - \varepsilon_{C}}{k_{B}T}}\right] \)  where  \( k_{B}T \)  is the thermal energy,  \( \mu_{F} \)  the chemical potential (entering the Fermi-Dirac distribution) and  \( \varepsilon_{C} \)  the bottom of the conduction band. If we estimate the onset of free-carrier screening as  \( \mu_{F} - \varepsilon_{C} > -k_{B}T \)  (when the occupations are not dominated by the tail of the Fermi-Dirac distribution), we obtain  \( n > 5 \times 10^{11} \, cm^{-2} \)  for all the electron-doped materials studied here.

The hole-doped materials studied here have weaker Born effective charges, but that is not to say that the remaining EPIs are not sensitive to screening; nevertheless, smaller variations of the mobility are to be expected.

## Appendix B: Additional electron-phonon scattering data

Fig. 6 shows the transport properties of GaSe-e,  \( Bi_{2}Se_{3} \) -e,  \( Sb_{2}SeTe_{2} \) -e, and BiClTe-e.

Fig. 7 shows the velocity plot for  \( Bi_{2}STe_{2} \) -e, for which phonon-limited transport was not computed, but is expected to be similar to  \( Bi_{2}SeTe_{2} \) -e.
 
![](./images/867772924138881971_10.jpg)

![](./images/867772924138881971_11.jpg)

![](./images/867772924138881971_12.jpg)

![](./images/867772924138881971_13.jpg)

FIG. 6. Velocity and scattering plots of GaSe-e,  \( Bi_{2}Se_{3} \) -e,  \( Sb_{2}SeTe_{2} \) -e, and BiClTe-e, in order of decreasing conductivity.
 
![](./images/867772924138881971_14.jpg)

FIG. 7. Velocity plot of neutral  \( Bi_{2}STe_{2} \) -e. Electron-phonon scattering was not computed but it is expected to be similar to  \( Bi_{2}SeTe_{2} \) -e.
 
