# TOPOLOGICAL CHARACTERIZATION OF REARRANGEMENTS IN AMORPHOUS SOLIDS

## A PREPRINT

Paul Desmarchelier
Department of Material Sciences and Engineering, Johns Hopkins University, Baltimore, Maryland 21218, USA
paul.desma@gmail.com

Spencer Fajardo
Department of Material Sciences and Engineering, Johns Hopkins University, Baltimore, Maryland 21218, USA

Michael L. Falk
Department of Material Sciences and Engineering, Johns Hopkins University, Baltimore, Maryland 21218, USA
Department of Mechanical Engineering, Johns Hopkins University, Baltimore, MD 21218, USA
Department of Physics and Astronomy, Johns Hopkins University, Baltimore, MD 21218, USA
Hopkins Extreme Materials Institute, Johns Hopkins University, Baltimore, MD 21218, USA

January 17, 2024

## ABSTRACT

In amorphous materials, plasticity is localized and occurs as shear transformations. It was recently shown by Wu et al. that these shear transformations can be predicted by applying topological defect concepts developed for liquid crystals to an analysis of vibrational eigenmodes [Wu et al.; Nat. Com.,2023]. This study relates the -1 topological defects to the displacement fields expected of an Eshelby inclusion, which are characterized by an orientation and the magnitude of the eigenstrain. A corresponding orientation and magnitude can be defined for each defect using the local displacement field around each defect. These parameters characterize the plastic stress relaxation associated with the local structural rearrangement and can be extracted using the fit to either the global displacement field or the local field. Both methods provide a reasonable estimation of the MD-measured stress drop, confirming the localized nature of the displacements that control both long-range deformation and stress relaxation.

It has been long appreciated that structural defects play an essential role in the mechanical behavior of crystalline materials. For instance, their yield stress is determined by the behavior of dislocations [1]. These defects are described as breaks in the invariance of the crystal lattice [2].

In amorphous materials, there is no lattice structure, and it is challenging to define discrete defects linked to deformation. The lack of clearly defined defects inhibits the development of a deformation theory for amorphous materials that is specifically linked to aspects of the atomic structure [3,4]. Consequently, predicting structural features that give rise to a larger-scale deformation remains an area of active investigation [5].

The sites, where the structural relaxation takes place, are characterized by large non-affine displacements [6] and high potential energy release [7]. These shear transformations (STs) are irreversible atomic displacements that contribute to the transition of the system from one inherent structure to another [8]. STs can be quantified in terms of number [9,10] and activation energy [11,12]. As such they have been integrated as a fundamental micromechanism into numerous constitutive equations [13-17].

Previous studies have characterized the spatial rearrangement taking place in the STs in 2D [18-20] and 3D [21] simulated glasses, and experimentally in colloidal [22] and metallic [23,24] glasses. They are typically analyzed in terms of the non-affine displacements occurring during a structural relaxation, a review of which has been written by

Nicolas and Röttler [25]. In particular, these STs can be described as quadrupolar zones [26]. Moreover, an orientation can be assigned to the quadrupolar zones [25]. More recently, the concept of topological defect (TD) from the liquid crystal literature has been applied to the displacement field to charcterize STs [27]. Another ongoing and important effort is being made to improve the predictions of the positions of sites susceptible to local rearrangements: the shear transformation zones. Many indicators have been developed, an overview can be found in the review paper of Richard et al. [5]. One of the approaches is to consider the eigenmodes of the system, with features of the lowest frequency eigenmodes predicting the next instability [28,29]. Very recently, Wu et al. also identified TDs within low frequencies eigenmodes to predict the STs [30].

These small-scale STs have long-range repercussions. In particular, the quadrupolar zones gjve rise to long-range elastic deformations, and these can be described using the Eshelby inclusion model [31]. This has been extensively incorporated into mesoscale models of glass plasticity [18,32,33]. Notably, Albaret et al. showed that the stress drop due to relaxation can be accurately estimated using the position and characteristics of the Eshelby inclusions fitted locally [34]. A similar analysis has been performed to study the orientation [25].

In this paper, we show that the plastic relaxation can be characterized using the core of the STs and their immediate surroundings. First, the STs are located by characterizing the topological defects within the displacement field, and measuring the orientation and a magnitude of each defect. We then show that this information can be used to reproduce the entire displacement field using the Eshelby inclusion model. Finally, we relate the orientation and magnitude of the STs to the stress drops using values estimated from either the global displacement field or from the local displacement around the STs only.

The glass samples studied here are 2D binary Lennard-Jones glass squares with a side length of 98.8 (Lennard-Jones reduced units) and containing 10,000 atoms, created using the same potential parameters and the slow quench approach described by Barbot et al. [35]. Fourteen independent samples using different initial spatial distributions are created. These glasses are then deformed in simple shear using an Athermal Quasi Static (AQS) algorithm. That is, the system is deformed step-wise with a strain step ($\delta\gamma$) of $1 \times 10^{-5}$ and then relaxed to mechanical equilibrium using a conjugate gradient method before performing the next strain step. This is repeated until a strain ($\gamma$) of 0.5 is reached. Lees-Edwards periodic boundary conditions are maintained throughout, and all simulations are performed using LAMMPS [36].

![](./images/954629291222499333_1.jpg)

Figure 1: Representation of the non-affine displacements during a plastic event: a) displacements mapped on atomic positions b) coarse-grained displacements c) normed coarsed-grained displacement vectors (black arrows) used to determine the topological defect positions (blue crosses for -1 defects and red circles for +1 defects )

During the deformations, the stress and strain of the whole box are recorded at each deformation step, and the atomic positions are recorded before and after each plastic event. A plastic event, or stress relaxation event, is defined in this study as a shear step that results in the global stresses in the shear direction $\sigma_{xy}$ decreasing. The impact of this choice is discussed in the supplementary materials. The non-affine displacements are computed using the atom positions before the event $r_{i-1}$ and after the event $r_i$:

$$
u_i = r_i - r_{i-1} - u_i^{aff} \tag{1}
$$

with $u_i^{aff}$ the imposed affine displacement ($u_x = \delta\gamma r_y, u_y = 0$). To represent the non-affine displacement field corresponding to the structural relaxation, the displacements computed via equation 1 are mapped onto the position of

the atoms just before the stress drop with the added affine deformation, this is depicted in figure 1a. Additionally, after each stress drop, the stress state after the reversion of a single strain step is computed. The occurrence of a plastic event during this step is very unlikely. This state will be useful for the computation of the shear modulus of the inherent state and is referred to as reverted state in the following.

The first step of the analysis is to identify the positions of the STs that give rise to the stress drop. This is done by identifying topological defects in the displacement field, in a very similar way to the approach developed by Wu et al. [30]. First, atomic displacements are projected onto a 100 by 100 orthogonal regular grid (see figure 1b) with the coarse graining function described by Albaret et al. [34] using a length of 1.17 Lennard-Jones distance units ($\sigma_{LJ}$). The topological defects are defined by the smallest closed loop for which the topological charge $q$ takes a non-zero value, as defined by the equation [37]

$$
\oint d\theta = 2\pi q. \tag{2}
$$

Here, $\theta$ is the orientation of the displacement (as represented by the orientation of the normed vector in figure 1c). As a simplification, the topological defects are computed for each point of the grid by considering a 4 by 4 square loop around the point considered. An example of the resulting charges is given in figure 1c. The final position of the defect is the center of mass of the contiguous patches sharing the same topological charge. The quadrupoles and vortices arising upon deformation of a 2D glass [38] will appear as -1 and +1 defects, respectively. Importantly, those are the only topological charge values that we observe, meaning that the displacement field can be described as a superposition of quadrupoles and vortices. In figure 1c, a -1 topological charge is detected in the central quadrupolar zone visible in panels a) and b), as well as other charges. These other charges appear in regions where the displacements are smaller. As this analysis stems from nematics, it considers directors and not vectors; as such, the quadrupoles are four-fold symmetric.

More information about the -1 defects can be extracted from the displacement field in their immediate proximity. We are able to calculate the orientation, $\phi_{esh-loc}$ estimated using the phase shift of the inner product of the displacement of each atom and their position relative to the center of the ST, i.e.

$$
\phi_{esh-loc} = \arg \left( \sum_{i=0}^{N_{shell}} \mathbf{u}_i \cdot (\mathbf{r}_i - \mathbf{x}_{esh}) \exp(-j2\Omega) \right) . \tag{3}
$$

Here, $\Omega$ is the angular position of atom $i$ relative to the Eshelby inclusion position ($\mathbf{x}_{esh}$), and $j$ is the imaginary number. The sum of equation 3 runs on all the atoms within 4 interatomic distances of the center of the -1 defect considered ($N_{shell}$). The phase shift is deduced from the argument of the second term of the complex Fourier series. This approach is similar to the method *MD/azi* introduced by Nicolas and Röttler [25]. The displacement amplitude near the defects can be used to describe the importance of the defect, both relative to other defects and relative to the global stress relaxation. This can be described using the average atomic non-affine displacement in the contiguous patch sharing the same topological charge (-1) $\langle |\mathbf{u}_{na}| \rangle_{defect}$.

The -1 defects, being essentially quadrupoles, can be interpreted as the center of an Eshelby inclusion, and as such, the resulting displacement field may be computed using the following equations, derived by Dasgupta et al. in 2D [32],

$$
\begin{aligned}
u_x &= \frac{\varepsilon^*}{4(1-\nu)} \frac{a^2}{r^2} \Bigg\{ \left[ 2(1-2\nu) + \frac{a^2}{r^2} \right] [x \cos 2\phi + y \sin 2\phi] + \left[ 1 - \frac{a^2}{r^2} \right] \left[ \frac{(x^2 - y^2) \cos 2\phi + 2xy \sin 2\phi}{r^2} \right] 2x \Bigg\}, \\
u_y &= \frac{\varepsilon^*}{4(1-\nu)} \frac{a^2}{r^2} \Bigg\{ \left[ 2(1-2\nu) + \frac{a^2}{r^2} \right] [x \sin 2\phi - y \cos 2\phi] + \left[ 1 - \frac{a^2}{r^2} \right] \left[ \frac{(x^2 - y^2) \cos 2\phi + 2xy \sin 2\phi}{r^2} \right] 2y \Bigg\}.
\end{aligned} \tag{4}
$$

Here $a$ is the radius of the inclusion; $\phi$ is the orientation of the quadrupolar zone; $r$ is the distance to the center of the core; $x$ and $y$ describe the position of the center of the inclusion; $\varepsilon^*$ is the eigenstrain magnitude, and $\nu$ the Poisson ratio. The Poisson ratio is set at 0.46, based on an AQS tensile deformation simulation of the same glass, and is considered to be homogeneous and constant through the simulation. It is also important to note that here we assume a traceless eigenstrain as Dasgupta et al. [32], that is, that locally the Eshelby inclusion undergoes a transformation at constant volume. Equation 4 provides a solution for the displacements outside the core ($r > a$) in an infinite homogeneous medium and can be used to fit the displacement field obtained via MD. To this end, the global field is reproduced by summing the displacement of each -1 defect obtained by applying equation 4. The parameter $a$ is set to $2\ \sigma_{LJ}$, and $\varepsilon^*$ and $\phi$ are fitted using a conjugated direction method. As a result, for each event, the displacement field is fitted using two parameters ($\varepsilon^*$ and $\phi$) per defect. Importantly, only the atoms at a distance greater than $a$=$2\ \sigma_{LJ}$ away from defects are considered. Details about the fitting process and visualizations of the fitted displacements can be found in the supplementary materials.

![](./images/954629291222499333_2.jpg)

Figure 2: a) Distribution of the angle $\phi$ obtained from the fitting of the whole displacement field to equation 4 vis-à-vis $\phi_{esh-loc}$ the angle of the local displacement field from equation 3. The diagonal blue line represents one-to-one correspondence. b) The eigenstrain of the Eshelby equation $\varepsilon^{*}$ vis-à-vis the average displacement around the defect. The blue line represents the linear fit.

The parameters $\phi$ and $\varepsilon^{*}$, describe the displacements associated with the local ST while $\phi_{esh-loc}$ and $\langle|\mathbf{u}_{na}|\rangle_{defect}$ characterize the displacement field surrounding the ST. Their correlation is displayed in figure 2. The link between $\phi_{esh-fit}$ and $\phi_{esh-loc}$ appears clearly in figure 2a with a diagonal distribution showing a one-to-one correspondence. It spans over $[0,\pi/2]$ because of the four-fold symmetry of the quadrupolar zones. The Pearson correlation between the two parameters is 0.26. It also appears that the distribution is not uniform over the whole set of angles, but rather appears centered around $\pi/4$. This $\pi/4$ value corresponds approximately to the orientation of the rearrangement shown in figure 1 and aligns with simple shear in the $x$ direction [25,38].

The Eshelby inclusion eigenstrain magnitude $\varepsilon^{*}$ can be characterized by the displacement within the core, and approximated using $\langle|\mathbf{u}_{na}|\rangle_{defect}$. As shown in figure 2b, these terms can be linked through a linear fit with a $R^{2}$ of 0.72. In this figure, one can also notice that there is an important concentration of $\varepsilon^{*}$ values around $1\times10^{-1}$ and a long tail up to $1\times10^{-4}$. It can be noted that less than $1\%$ of the defects have an associated $\varepsilon^{*}$ below $1\times10^{-10}$ and are not displayed in figure 2b.

![](./images/954629291222499333_3.jpg)

Figure 3: 2D histogram of the stress drop of each event $\Delta\sigma_{0}$: a) as a function of the stress drop computed from equation 5 using the parameters obtained with the Eshelby fit $\Delta\sigma_{esh-fit}$, b) compared to using the defect description parameters $\Delta\sigma_{esh-loc}$. The blue lines representing where the two are exactly equal.

As described by Albaret et al. [34] the stress drop $(\Delta \sigma_{xy})$ associated with an event can be recomputed by summing the individual contribution of each inclusion,

$$
\Delta \sigma_{xy} = \sum^{n_{in}} \frac{a^2 \pi}{V} G_i \varepsilon^* \sin(2\phi),
\tag{5}
$$

with V the volume of the simulation cell and $G_i$ the shear modulus during event $i$. This has been obtained by identifying the parameters of equation 4 in the equation derived by Albaret et al. [34]. From this point on, unless otherwise stated, $\Delta \sigma$ or $\sigma$ will refer to the xy component, the only one being treated in this study. The shear modulus is estimated using the same method as Albaret et al.: it is the difference between the $\sigma_{xy}$ after the event and on the reverted state divided by $\delta \gamma$. This gives an estimation of the shear modulus of the inherent structure in the absence of plasticity. Other approximations not relying on the reversion of events can be used but do not perform as well for the prediction of $\Delta \sigma$ (see supplementary materials). As for equation 4, a homogeneous medium is assumed. As shown in figure 3a, the MD-derived stress drop $\Delta \sigma_0$ and the value derived from the displacement field fit through equation 5, $\Delta \sigma_{esh-fit}$ have almost a one-to-one correspondence. This is particularly true for stress drops above $1 \times 10^{-3}$, which account for most of the stress relaxation [39]. The Pearson correlation coefficient between fitted and MD stress drops is 0.97. More importantly, using the parameters derived from the field displacement in the vicinity of the defects alone yields a similarly good correlation, with the Pearson correlation coefficient shifting to 0.92 as shown in figure 3b. It is also worth mentioning that the distribution of stress drops is not uniform over a range but that there is an important concentration around $1 \times 10^{-2}$ and a long tail at lower values, much like for the distribution of the eigenstrain magnitudes.

The stress-strain curves can be reproduced by adding the elastic part to the result equation 5,

$$
\sigma_{esh}^n = \sum_{i}^{n} \Delta \sigma_{esh-i} + \delta \gamma_i G_i,
\tag{6}
$$

and are displayed in figure 4. Despite the close correspondence observed in figure 3a the stress is overestimated, meaning that the stress relaxation computed with equation 5 is underestimated. This underestimation averages at -3 % in relative error, the full distribution can be found in the supplementary material.

![](./images/954629291222499333_4.jpg)

Figure 4: Stress-strain curves from the simulation (dotted red line), and estimated from equation 5 with the parameters fitted from equation 4,a) example with good correspondence and b) poor correspondence.

We have shown that it is possible to infer the stress drops linked to plastic events with fair accuracy, considering either the entire displacement field or only the amplitude and orientation of the field around the -1 topological defects.

This analysis is in essence close to the $D_{min}^2$ analysis introduced by Falk and Langer [40] which is still widely used [5], both quantify heterogeneities in the non-affine displacement field. But the analysis presented here contains more information and can be used to identify quadrupolar zones (-1 defects) and vortices (+1 defects) [30]. As described by Sopu et al. [38], those two structures can be used to describe plastic phenomena in glasses, notably shear banding. Moreover, it is less complex than the method of Fusco et al., which relies on the spatial decay of the plastic energy [7].

Albaret, et al. previously reproduced the stress-strain curves from the displacement field for a 3D amorphous silicon, with a very good accuracy [34]. This accuracy can partially be attributed to the consideration of a variable inclusion size. We and others have relied on a constant $a$ [32], a ST size that varies from event to event can also be estimated based on the spatial decay of plastic potential energy [34], or the number of atoms having a high $D_{min}^2$ [25]. In those studies, $a$ ranged from 2 to 10 interatomic distances for a-Si and 2 to 20 for the LJ glasses. However, the estimation of the ST size

is bound to the estimation of the position of the ST, and this position does not always precisely match the topological defect position. It might be possible to circumvent this issue by isolating every STs by pinning the atoms of other STs in an auxiliary simulation, as proposed by Nicolas and Röttler [25]. However, this will most probably impact $\varepsilon^*$ due to the altered boundary conditions in the immediate surroundings of the inclusion. Moreover, using relative fitting error as defined by Albaret et al, we find a similar distribution. [34] . It is rather spread and provides an estimate with high error for some events, but achieved a lower error for the high-stress drop events (see supplementary materials).

This study relies on the formulation of the Eshelby displacement field, which assumes a homogeneous infinite medium. Thus, the solution for individual inclusion does not consider self-interaction through the periodic boundary condition, and a size effect might arise. If there is indeed a size effect observable for smaller sizes, the error seems to stabilize within 3% from a size of $100\ \sigma_{L,J}$ on (see supplementary materials). Moreover, the relative stress drop error distribution is not dependent on the number of events [39]. This hints that the underestimation is not caused by neglecting interaction between defects, and much less by self-interaction through the boundary conditions. Albaret et al. considered the interaction thanks to the superposition of displacement fields due to inclusion in periodic images [34], but in our case it does not improve the results and increases the computational cost.

We conclude that there is an essential relationship between the rearrangements that control plasticity and -1 topological defects in the displacement field. They can be used to identify the center of the shear transformations from which quadrupolar relaxation arise. An orientation and magnitude of the eigenstrain can be assigned to these centers either by fitting the displacement field using the Eshelby inclusions model or using the non-affine displacement in the vicinity of the defect. Using the characteristics of the inclusions obtained from the fits or from the local displacement field, it is possible to obtain a reasonable approximation of the stress relaxation. This reaffirms, with earlier studies [4,8,32,41], that rearrangements in amorphous materials are composed of discrete, local STs that can be enumerated and characterized as such. This is likely true not only in the 3D covalent glasses previously studied by Albaret, but across a wide range of glasses, including metallic glasses and 2D systems. The topological defect concept provides an unambigous methodology for locating and characterizing such STs.

## Acknowledgment

This work supported by the US National Science Foundation (NSF) under Grant No. DMR-2323718/2323719/2323720 and was carried out at the Advanced Research Computing at Hopkins (ARCH) core facility (rockfish.jhu.edu), which is supported by the NSF under grant number OAC 1920103. The authors would like to thank T. Albaret, W. Kob and T. Curk for fruitful discussion.

## References

[1] V. Vitek, “Structure of dislocation cores in metallic materials and its impact on their plastic behaviour,” *Progress in Materials Science*, vol. 36, pp. 1–27, 1992.

[2] V. Vitek, “Atomic level computer modelling of crystal defects with emphasis on dislocations: Past, present and future,” *Progress in Materials Science*, vol. 56, no. 6, pp. 577–585, 2011. Festschrift Vaclav Vitek.

[3] M. L. Falk and J. Langer, “Deformation and failure of amorphous, solidlike materials,” *Annual Review of Condensed Matter Physics*, vol. 2, no. 1, pp. 353–373, 2011.

[4] A. Tanguy, “Elasto-plastic behavior of amorphous materials: a brief review,” *Comptes Rendus. Physique*, vol. 22, pp. 117–133, Dec. 2021.

[5] D. Richard, “Predicting plasticity in disordered solids from structural indicators,” *Physical Review Materials*, p. 19, 2020.

[6] M. L. Falk and J. S. Langer, “Dynamics of viscoplastic deformation in amorphous solids,” vol. 57, no. 6, p. 14, 1998.

[7] C. Fusco, T. Albaret, and A. Tanguy, “Role of local order in the small-scale plasticity of model amorphous materials,” *Phys. Rev. E*, vol. 82, p. 066116, Dec 2010.

[8] E. Stanifer and M. L. Manning, “Avalanche dynamics in sheared athermal particle packings occurs via localized bursts predicted by unstable linear response,” *Soft Matter*, vol. 18, no. 12, pp. 2394–2406, 2022.

[9] F. Delogu, “Identification and characterization of potential shear transformation zones in metallic glasses,” *Phys. Rev. Lett.*, vol. 100, p. 255901, Jun 2008.

[10] J. Yu, A. Datye, Z. Chen, C. Zhou, O. E. Dagdeviren, J. Schroers, and U. D. Schwarz, "Atomic-scale homogeneous plastic flow beyond near-theoretical yield stress in a metallic glass," *Communications Materials*, vol. 2, no. 1, p. 22, 2021.

[11] B. Xu, M. Falk, J. Li, and L. Kong, "Strain-dependent activation energy of shear transformation in metallic glasses," *Physical Review B*, vol. 95, p. 144201, Apr. 2017.

[12] F. Boioli, T. Albaret, and D. Rodney, "Shear transformation distribution and activation in glasses at the atomic scale," *Phys. Rev. E*, vol. 95, p. 033005, Mar 2017.

[13] E. Bouchbinder, J. S. Langer, and I. Procaccia, "Athermal shear-transformation-zone theory of amorphous plastic deformation. i. basic principles," *Phys. Rev. E*, vol. 75, p. 036107, Mar 2007.

[14] M. L. Manning, J. S. Langer, and J. M. Carlson, "Strain localization in a shear transformation zone model for amorphous solids," *Physical Review E*, vol. 76, p. 056106, Nov. 2007.

[15] C. H. Rycroft, Y. Sui, and E. Bouchbinder, "An Eulerian projection method for quasi-static elastoplasticity," *Journal of Computational Physics*, vol. 300, pp. 136-166, Nov. 2015.

[16] A. R. Hinkle, C. H. Rycroft, M. D. Shields, and M. L. Falk, "Coarse graining atomistic simulations of plastically deforming amorphous solids," *Physical Review E*, p. 15, 2017.

[17] K. Kontolati, D. Alix-Williams, N. M. Boffi, M. L. Falk, C. H. Rycroft, and M. D. Shields, "Manifold learning for coarse-graining atomistic simulations: Application to amorphous solids," *Acta Materialia*, vol. 215, p. 117008, Aug. 2021.

[18] A. Tanguy, F. Leonforte, and J. L. Barrat, "Plastic response of a 2D Lennard-Jones amorphous solid: Detailed analysis of the local rearrangements at very slow strain rate," *The European Physical Journal E*, vol. 20, pp. 355-364, July 2006.

[19] P. Cao, H. S. Park, and X. Lin, "Strain-rate and temperature-driven transition in the shear transformation zone for two-dimensional amorphous solids," *Physical Review E*, vol. 88, p. 042404, Oct. 2013.

[20] W. Jin, A. Datye, U. D. Schwarz, M. D. Shattuck, and C. S. O'Hern, "Using delaunay triangularization to characterize non-affine displacement fields during athermal, quasistatic deformation of amorphous solids," *Soft Matter*, vol. 17, no. 38, pp. 8612-8623, 2021.

[21] M. Zink, K. Samwer, W. L. Johnson, and S. G. Mayr, "Plastic deformation of metallic glasses: Size of shear transformation zones from molecular dynamics simulations," *Phys. Rev. B*, vol. 73, p. 172203, May 2006.

[22] P. Schall, D. A. Weitz, and F. Spaepen, "Structural Rearrangements That Govern Flow in Colloidal Glasses," *Science*, vol. 318, pp. 1895-1899, Dec. 2007.

[23] Y. Ma, J. Ye, G. Peng, D. Wen, and T. Zhang, "Nanoindentation study of size effect on shear transformation zone size in a ni-nb metallic glass," *Materials Science and Engineering: A*, vol. 627, pp. 153-160, 2015.

[24] S. Kang, D. Wang, A. Caron, C. Minnert, K. Durst, C. Kübel, and X. Mu, "Direct observation of quadrupolar strain fields forming a shear band in metallic glasses," *Advanced Materials*, vol. 35, no. 25, p. 2212086, 2023.

[25] A. Nicolas and J. Rottler, "Orientation of plastic rearrangements in two-dimensional model glasses under shear," *Phys. Rev. E*, vol. 97, p. 063002, Jun 2018.

[26] D. Şopu, A. Stukowski, M. Stoica, and S. Scudino, "Atomic-Level Processes of Shear Band Nucleation in Metallic Glasses," *Physical Review Letters*, vol. 119, p. 195503, Nov. 2017.

[27] M. Baggioli, I. Kriuchevskyi, T. W. Sirk, and A. Zaccone, "Plasticity in Amorphous Solids Is Mediated by Topological Defects in the Displacement Field," *Physical Review Letters*, vol. 127, p. 015501, July 2021.

[28] V. Mazzacurati, G. Ruocco, and M. Sampoli, "Low-frequency atomic motion in a model glass," *Europhysics Letters*, vol. 34, p. 681, jun 1996.

[29] A. Tanguy, B. Mantisi, and M. Tsamados, "Vibrational modes as a predictor for plasticity in a model glass," *Europhysics Letters*, vol. 90, p. 16004, apr 2010.

[30] Z. W. Wu, Y. Chen, W.-H. Wang, W. Kob, and L. Xu, "Topology of vibrational modes predicts plastic events in glasses," *Nature Communications*, vol. 14, may 2023.

[31] J. D. Eshelby and R. E. Peierls, "The determination of the elastic field of an ellipsoidal inclusion, and related problems," *Proceedings of the Royal Society of London. Series A. Mathematical and Physical Sciences*, vol. 241, no. 1226, pp. 376-396, 1957.

[32] R. Dasgupta, H. G. E. Hentschel, and I. Procaccia, "Yield strain in shear banding amorphous solids," *Physical Review E*, vol. 87, p. 022810, Feb. 2013.

[33] D. F. Castellanos, S. Roux, and S. Patinet, "History dependent plasticity of glass: A mapping between atomistic and elasto-plastic models," *Acta Materialia*, vol. 241, p. 118405, Dec. 2022.

[34] T. Albaret, A. Tanguy, F. Boioli, and D. Rodney, "Mapping between atomistic simulations and Eshelby inclusions in the shear deformation of an amorphous silicon model," *Physical Review E*, vol. 93, p. 053002, May 2016.

[35] A. Barbot, M. Lerbinger, A. Hernandez-Garcia, R. García-García, M. L. Falk, D. Vandembroucq, and S. Patinet, "Local yield stress statistics in model amorphous solids," *Physical Review E*, vol. 97, p. 033001, Mar. 2018.

[36] A. P. Thompson, H. M. Aktulga, R. Berger, D. S. Bolintineanu, W. M. Brown, P. S. Crozier, P. J. in 't Veld, A. Kohlmeyer, S. G. Moore, T. D. Nguyen, R. Shan, M. J. Stevens, J. Tranchida, C. Trott, and S. J. Plimpton, "LAMMPS - a flexible simulation tool for particle-based materials modeling at the atomic, meso, and continuum scales," *Comp. Phys. Comm.*, vol. 271, p. 108171, 2022.

[37] J. V. Selinger, *Introduction to the theory of soft matter: from ideal gases to liquid crystals*. Springer, 2016.

[38] D. Şopu, "STZ-Vortex model: The key to understand STZ percolation and shear banding in metallic glasses," *Journal of Alloys and Compounds*, vol. 960, p. 170585, Oct. 2023.

[39] P. Desmarchelier, S. Fajado, and M. L. Falk, "Supplementary materials, see online version," 2023. .

[40] M. L. Falk and J. S. Langer, "Dynamics of viscoplastic deformation in amorphous solids M.," *Physical Review E*, vol. 57, no. 6, p. 14, 1998. Number: 6.

[41] V. Hieronymus-Schmidt, H. Rösner, G. Wilde, and A. Zaccone, "Shear banding in metallic glasses described by alignments of Eshelby quadrupoles," *Physical Review B*, vol. 95, p. 134111, Apr. 2017.

# Supplementary Materials: Topological characterization of rearrangements in amorphous solids

Paul Desmarchelier, Spencer Fajardo, Michael L. Falk

January 17, 2024

## 1 Contribution to Relaxation and Event Definition

The normed cumulative contribution to the total stress relaxation of events as a function of $\Delta\sigma_0$ is represented in figure S1. It shows the impact of the choice of event detection. In the present study, the relaxation events are defined as steps $i$ where $\sigma_i - \sigma_{i-1} < 0$. However, this neglects steps where the plastic stress relaxations are lower than the elastic stress increases ($\delta\gamma G \approx 2 \times 10^{-4}$). Those steps can be considered by using the following relation to define events: $\sigma_i - \sigma_{i-1} - \delta\gamma G(\gamma_i) < 0$. In figure S1 the two are represented, and it appears that the error made by neglecting $\delta\gamma G(\gamma_i)$ (the difference between the curves) amounts to less than 5% of the stress relaxation. From the distribution, it also appears that most of the stress relaxation occurs for drops larger than $1 \times 10^{-3}$. So that, with an accurate prediction of relaxation above this value, most of the behavior should be reproducible. This may contribute to the under estimation of the stress relaxation seen in figure 4.

![](./images/954629291222499333_5.jpg)

Figure S1: Normed cumulative contribution to the total stress drop as a function of stress relaxation, with (orange line) or without considering the elastic part of the stress drop (blue line).

## 2 Fitting error

The function that is minimized by the fitting procedure is defined as:

$$
R^{2}=\sum^{N_{out}}\left|\mathbf{u}_{NA}-\sum^{N_{incl}}\begin{pmatrix}u_x\\u_y\end{pmatrix}(\mathbf{r}-\mathbf{r}_{incl})\right|^{2} \tag{S1}
$$


with$\sum^{N_{out}}$ the sum over the atoms that are out of the inner core (at a distance of more than $a$ away) of all inclusions, $\mathbf{u}_{NA}$ the non-affine displacements, and $\sum^{N_{incl}}$ the sum over the displacement due to each inclusion. As suggested by Albaret et al. [1], the final value of $R^2$ is compared to $R_0^2 = \sum^{N_{out}} |\mathbf{u}_{NA}|^2$ to compute a relative error, the result is represented in figure S2. The error seems to depend on $\Delta \sigma$, as can be seen by the shift in the peak of the error when weighted by the stress drop; the resulting error distribution is centered around a lower value. The displacements due to high-stress drop events are thus easier to reproduce using equation 4, centered on the main TDs. This behavior was already shown by Albaret et al. for events with large plastic energy [1].

![](./images/954629291222499333_6.jpg)

Figure S2: Fitting error as defined by Albert et al. for all stress drops (orange), and for all events weighted by $\Delta \sigma$ (blue).

## 3 Displacement field examples

The displacement field obtained through the MD simulation and the one resulting from the fit of $\varepsilon^*$ and $\phi$ from equation 4 for the selected -1 defect are displayed in figure S3. The results for an event containing only one clearly visible defect (a,b), another containing two visible defects (c,d) and finally a shear banding case (e,f) are displayed. In all cases, the fit corresponds reasonably well, at least visually, in particular further away from the inclusion.In the center of the core equation 4 is not valid, and the displacements can diverge.


![](./images/954629291222499333_7.jpg)

Figure S3: Representation of the non-affine displacements from the MD simulation (a, c, e) and fitted by equation 4 (b, d, f), each row representing the same event.

## 4 Shear Modulus Estimation and error distribution

The shear modulus $G$ is estimated thanks to $G_i = (\sigma_i - \sigma_i^{rev})/\delta\gamma$, $\sigma_i^{rev}$ being the stress in the reverted state of event $i$. In the absence of plastic deformation during the reversion of a single $\delta\gamma^1$, this allows us to consider the elastic shear modulus of the inherent state. However, another method can be used: $G_i$ can be obtained from the stress-strain curves. For this, they are expunged of the stress drops to remove the influence of plastic events. These curves are then filtered with a Savitzky-Golay filter, whose result is derived with respect to strain to obtain the shear modulus. The results are displayed in figure S4.

$^1$Which is true for 99.7 % of the events, and in the case of an outlier, the $G_i$ of the previous event is used.

![](./images/954629291222499333_8.jpg)

Figure S4: Shear modulus $G$ (green and cyan) obtained from the stress-strain curve (red and blue) with the stress drop removed. The green and red curves are respectively the average modulus and "increase only" stress-strain curves, while the cyan and blue curves give the individual realization for the 14 different repetitions of the process.

Using the stress-strain curves estimated shear modulus has a relatively small impact on the precision of the estimation of the stress drop. This difference is mostly visible in the shifted distribution of relative error shown in figure S5. This distribution is limited to events with a stress drop superior to $\Delta\sigma >1 \times 10^{-3}$ to limit the impact of low stress drop events whose contribution to the global relaxation can be neglected (see figure S1). Relying on the stress strain curves shifts the relative error from -3 to -8 % and does not impact the variance of the distribution.

![](./images/954629291222499333_9.jpg)

Figure S5: Normed stress relaxation relative error distribution for events with $\Delta\sigma >1 \times 10^{-3}$, for all events weighted (blue) or not (orange) by the number of events. The full lines correspond to the distribution obtained using the reverted stress estimation of $G$ and the dashed line to the estimation using the stress strain curves.

## 5 Boundary Conditions and Size Effects

In this section, the size effects and periodic boundary conditions are discussed. As pointed out in the main article, even though periodic boundary conditions are accounted for in equation 5, equation 4 assumes an infinite medium for a single inclusion [1]. Thus, the model does not account for interactions between inclusion and self-interaction through the periodic boundary conditions. This may induce an error. This effect can be studied through the relative error distribution displayed in figure S5. There is a systematic relative error in the prediction of stress relaxation. However, the distribution remains very similar once weighted by the number of defects considered. This absence of impact of the number of events shows that the under-

estimation is not due to the interaction between defects. This also indicates that the infinite medium approximation does not impact the results at this scale; indeed, it would model self-interaction between inclusion at a distance of a box length when we know that the superposition (sum) of displacement due to multiple defects can give an accurate prediction.

Another method to check for size effects is to study the impact of the size of the simulation supercell. This is provided in figure S6 with the relative error for single events for a few box sizes. For each size, 3 to 14 independent glasses are studied. Although it is not possible to assess the asymptote for large systems, it appears that the error stabilizes around -3% from a size of 100. This hints that size effects are not the cause of the underestimation of the stresses observed in figure S5.

![](./images/954629291222499333_10.jpg)

Figure S6: Average relative error in stress relaxation for events with a single considered inclusion and $\Delta\sigma>1\times10^{-3}$ as a function of system size. The shaded area represent the standard deviation.

## References

[1] T. Albaret, A. Tanguy, F. Boioli, and D. Rodney, "Mapping between atomistic simulations and Eshelby inclusions in the shear deformation of an amorphous silicon model," *Physical Review E*, vol. 93, p. 053002, May 2016.