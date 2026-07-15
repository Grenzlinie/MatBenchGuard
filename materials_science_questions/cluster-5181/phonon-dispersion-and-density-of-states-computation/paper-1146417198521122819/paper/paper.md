# Role of long-range dipolar interactions in the simulation of the properties of polar crystals using effective atomic potentials

Miao Yu, $^{1,2}$ Fernando Gómez-Ortiz, $^{1}$ Louis Bastogne, $^{1}$ Jin-Zhu Zhao, $^{3,4}$ and Philippe Ghosez $^{1, *}$

$^{1}$ Theoretical Materials Physics, Q-MAT, Université de Liège, B-4000 Sart-Tilman, Belgium
$^{2}$ Institute of Atomic and Molecular Physics, Sichuan University, Chengdu 610065, China
$^{3}$ Guangdong Provincial Key Laboratory of Quantum Engineering and Quantum Materials,
School of Physics, South China Normal University, Guangzhou 510006, P. R. China
$^{4}$ Guangdong-Hong Kong Joint Laboratory of Quantum Matter,
South China Normal University, Guangzhou 510006, P. R. China
(Dated: September 12, 2025)

Driven by novel approaches and computational techniques, second-principles atomic potentials are nowadays at the forefront of computational materials science, enabling large-scale simulations of material properties with near-first-principles accuracy. However, their application to polar materials can be challenging, particularly when longitudinal-optical phonon modes are active on the material, as accurately modeling such systems requires incorporating the long-range part of the dipole-dipole interactions. In this study, we challenge the influence of these interactions on the properties of polar materials taking $BaTiO_3$ as paradigmatic example. By comparing models with and without the long-range part of the electrostatic contributions in a systematic way, we demonstrate that even if these interactions are neglected, the models can still provide an overall good description of the material, though they may lead to punctual significant artifacts. Our results propose a pathway to identify when an atomistic potential may be inadequate and needs to be corrected through the inclusion of the long-range part of dipolar interactions.

## I. INTRODUCTION

For decades, empirical and semi-empirical models have been fundamental in the atomistic modeling of materials, providing an alternative framework even prior to first-principles methods. Early approaches relied on interatomic potentials such as Lennard-Jones [1], Stillinger-Weber [2], and Tersoff [3] potentials, which successfully described properties of simple materials. Rapidly, they improved and became more sophisticated [4] and today a wide range of strategies, depending on the specific material system, can be found in the literature [5, 6] providing highly accurate predictions of material properties. With advances in computing power and electronic-structure theory [7-10], the community increasingly turned to first-principles simulations for greater predictive accuracy. However, aided by modern parameter fitting algorithms, high-quality reference data, and new perspectives, the atomistic modeling of materials is now enjoying a resurgence, allowing simulations of longer length and time scales as well as including operating conditions, such as the application of external electric fields or mechanical constraints [11]. Atomistic models directly fitted on first-principles data (and sometimes referred to as "second-principles") now offer a versatile framework that allows researchers to create custom models for a wide range of materials ranging from metals and semiconductors to insulators [12-15]. Modern approaches include pioneering lattice effective Hamiltonians [16, 17], related effective atomic potentials [18-21], phase-fields methodologies [22], shell- and bond-valence-models [23, 24], reactive force fields [25] and their application to ferroelectrics [26-28] or recent machine-learning interatomic potentials, including emerging universal potentials [29].

Recently, with the advent of machine learning, atomic potentials have indeed experienced a revolution, and are rapidly becoming a standard complementary tool in computational materials science [12-15, 30, 31] to extend the predictive power of first-principles simulations in a multiscale context. Approaches such as Gaussian process regression [32], kernel methods [31] and neural networks [30, 33] have democratized the generation of accurate interatomic models for many different materials. These models are typically trained on extensive datasets generated from first-principles calculations without the inclusion of any extra terms and relying on the configuration itself rather than distortions with respect to a high-symmetry reference structure. As a result, long-range interactions are often neglected. Although these models are typically assumed to depend on the local atomic environment at first sight, the actual range of the interactions is dependent and inherently determined by the size of the training set used to develop the model. Therefore, the correct description of the nonanalytic behavior of the interatomic force constants in the long-wavelength limit presents a challenge as it originates from the power-law behavior of the Coulombic interaction and cannot be easily captured by spatially truncated training sets. Moreover, the absence of a reference structure inherently complicates the analytical inclusion of electrostatic interactions, which are often neglected in AI models beyond the spatial range covered by their training set. Novel approaches are trying to circumvent this issue including charge equilibration schemes [34], the on-the-fly prediction of maximally localized Wannier function

* Corresponding author: Philippe.ghosez@uliege.be

centers [35, 36] or a recently proposed modification of the model without the need for additional first-principles calculations or retraining discussed in Ref. [37]. How- ever, these tools have not yet become common practice, and most of the machine-learned interatomic potentials rely on the nearsightedness of interatomic interactions neglecting such long range part of the interactions be- yond the range defined by the training set which in most cases turns out to be computed on a $2 \times 2 \times 2$ supercell.

In this work, we aim to clarify the concrete impact of neglecting the long-range part of the dipole-dipole in- teractions in computational models and to identify the scenarios where incorporating corrections for an accurate description becomes crucial. By focusing on the proto- typical ferroelectric material $BaTiO_{3}$ in which dipolar interactions are expected to be key [38, 39], we system- atically explore the influence of the dipole-dipole interac- tions on the phonon dispersion curves and atomic distor- tion patterns. On the one hand, we demonstrate that the inclusion of the long-range part of dipolar interactions is not always essential for an overall accurate description of the system, including the ferroelectric instability and its characteristic chain-like character, which supports the good performance of AI-based models even in polar ma- terials [40]. On the other hand, we also point out specific cases where neglecting the long-range part of the dipole- dipole interaction can lead to significant artifacts in the phonon spectrum, resulting in inaccurate descriptions of the energy landscape associated with certain atomic dis- placements and the emergence of spurious phases.

## II. METHODOLOGY

To assess the impact of the long-range character of dipolar interactions on the lattice dynamics of $BaTiO_{3}$, we rely here on a second-principles effective atomic po- tential (EAP) method, as implemented in the MULTIB- INIT software. The method relies on a Taylor expansion of the Born-Oppenheimer potential energy surface (PES) in terms of structural degrees of freedom around the cubic perovskite structure taken as reference. Although lower symmetry phases like the $P4mm$, $Amm2$, or $R3m$ could also be considered as proper references for constructing the model, the choice of the cubic parent phase follows previous similar studies in perovskites based on Taylor expansion [11, 16, 18] and is the most sensible choice to access the whole phase diagram. The Taylor expansion around the reference geometry is made in terms of indi- vidual atomic displacements and homogeneous strain de- grees of freedom and includes phonon, strain and strain- phonon energy terms at both harmonic and anharmonic levels. The coefficients of harmonic terms corresponds to second-energy derivatives which are straightforwardly determined from density-functional perturbation theory, so that the model keeps first-principles accuracy at the harmonic level. Then, most relevant anharmonic terms, which capture key deviations from harmonic behavior, are selected and their coefficients fitted in order to repro- duce the energies, forces, and stresses as obtained from DFT calculations for a representative set of atomic con- figurations. The reference model used here is a slight revision of the one reported in Ref. [41], only including refitted anharmonic terms. Parameters and a validity assessment passport are provided in Appendix.

In MULTIBINIT, the dipole-dipole contribution to the interatomic force constant (IFC), $C_{\kappa \alpha, \kappa' \beta}^{DD}$, related to atomic displacement of atom $\kappa$ in direction $\alpha$ and atom $\kappa'$ in direction $\beta$, separated by a vector $d$ are by default evaluated analytically from the knowledge of Born effec- tive charges $Z^{*}$ and optical dielectric tensor $\epsilon_{\infty}$ using an expression that generalize the following classical formula,

$$
C_{\kappa \alpha, \kappa' \beta}^{DD}=\frac{Z_{\kappa}^{*} Z_{\kappa'}^{*}}{\epsilon_{\infty}}\left(\frac{\delta_{\alpha \beta}}{d^{3}}-3 \frac{d_{\alpha} d_{\beta}}{d^{5}}\right), \tag{1}
$$

to anisotropic cases following the scheme described in Ref. [42].

![](./images/1146417198521122819_1.jpg)

FIG. 1. (a) Schematic representation of the dipole-dipole (DD, red) and short-range (SR, blue) contributions to the total interatomic force constants (IFC). (b) When activating the explicit treatment of DD interactions, the latter are com- puted analytically and infinite range while the SR IFC are obtained by subtracting the DD part from the total IFC and their range limited to that of a supercell defined by the $q$- point grid used for the calculations. (c) When deactivating the explicit treatment of DD interactions, the SR IFC cor- respond to the total IFC but truncated at the range of the supercell defined by the $q$-point grid.

In practice, and as illustrated in Fig. 1, this analyti- cal dipole-dipole (DD) contribution – which extents from nearest neighbors to infinite range – is subtracted from the total IFC to yield the remaining so-called short-range (SR) IFC. The process is associated to a Fourier trans- form of the dynamical matrices on a $n \times m \times p$ grid of $q$-points, which practically limits the SR IFC to a range defined by a corresponding $n \times m \times p$ supercell. Inside the range of this supercell, the total IFC are therefore the sum of SR and DD contributions, while outside it re- stricts to the DD contribution. Alternatively, the explicit

treatment of DD interactions can also be set to zero, in which case the SR IFC correspond to the total IFC but with a range artificially cut to the size of the supercell.

Fig. 2 illustrates the correspondence between the size of the supercell used in real space and that of the related $q$-point grid in reciprocal space. The atomic distortion patterns allowed in a given $n \times n \times n$ supercell are linear combinations of the eigendisplacements vectors of the phonon modes associated to the corresponding $n \times n \times n$ grid of $q$-points. Looking at the frequencies of the phonons associated to that mesh (and comparing model to DFT data) so quantifies the energetics, at harmonic level, of the displacement patterns compatible with that supercell. Looking at intermediate points belonging to finer meshes, allow to estimate the energetics of patterns in bigger supercells.

Second-principles models are typically trained on first-principles data using a given supercell. Looking at how the phonons on the related grid are reproduced by the model allow to assess the precision of the model at harmonic level. In the case of MULTIBINIT, the model is exact by construction at that level. Then the model is used for simulations in larger supercells. Looking at the quality of the dispersion curves at intermediate points related to finest grids allow to anticipate the precision of the model in such bigger supercells.

By simultaneously adjusting the real-space cutoff used to compute the interatomic force constants and toggling the analytical dipole-dipole term in MULTIBINIT, one can systematically modulate the effective interaction range. This dual control offered by MULTIBINIT provides a unique way to progressively refine models by incorporating interactions at larger ranges, enabling a controlled analysis of their impact through simulations on different supercell sizes. Moreover, since non-dipolar short-range interactions are expected to decay exponentially fast according to the nearsightedness principle, this approach allows us to assess the specific impact of the dipole-dipole interaction range, as will be discussed in the Results section.

The different models discussed on this article are constructed using different $q$-point meshes for the calculation of the dynamical matrices. The first model (blue points in Fig. 3) is derived using an $8 \times 8 \times 8$ $q$-point mesh, while the second (green points) and third (red points) models with a $2 \times 2 \times 2$ mesh. Notably, with the described approach, the dipole-dipole interactions are inherently included up to the specified interaction ranges (8, and 2 unit cells respectively). Some of the models, denoted as "+Dip" will include the analytical dipole-dipole correction at infinite range, while others do not, limiting consequently the dipole-dipole interactions to the specific range determined by their respective $q$-mesh as schematized in Fig. 1, allowing us to systematically assess its influence. Interestingly, since the anharmonic interactions in the model are limited to a range of $\sqrt{3}/2$ times the lattice constant on the reference structure, and no differences at the harmonic level are expected for cutoffs below two unit cells, all models effectively share the same anharmonic description—rendering them equivalent in this respect.

![](./images/1146417198521122819_2.jpg)

FIG. 2. Illustration of the relationship between $1 \times 1 \times 1$ (blue), $2 \times 2 \times 2$ (red) and $4 \times 4 \times 4$ (green) real-space supercells (projected on the $x$-$y$ plane) and reciprocal-space $q$-point grids (along $k_x$). The real-space atomic distortion patterns allowed in a given supercell are restricted to the $q$-points of the associated reciprocal-space grid. due to the periodic boundary conditions, simulations within a given supercell only provide access to interatomic force constants up to the range defined by the supercell. On the other hand, atomic displacements compatible with a given supercell are restricted to linear combination of the eigenvectors of the phonon modes associated to the associated $q$-point grid.

Remarkably, the model derived with a $2 \times 2 \times 2$ $q$-point mesh, which excludes the analytical dipole-dipole correction, is of special interest, as it mimics the typical interaction range used in the training sets of AI models, which in turn defines the maximum range of interactions these models incorporate. At the other extreme, the model with $8 \times 8 \times 8$ $q$-point mesh, including the analytical dipole-dipole correction can be considered as the exact model to be taken as reference.

Structural relaxations were performed using the Broyden-Fletcher-Goldfarb-Shanno (BFGS) method [43] and finite temperature simulations followed a Hybrid molecular dynamics Monte-Carlo approach (HMC) [44, 45], consisting of Markov chain Monte Carlo sampling.

## III. RESULTS

Let us first explore the influence of neglecting the long-range part of the dipole dipole interactions in the phonon dispersion curves of BaTiO$_3$. Figure 3 presents the phonon dispersion curves produced by three distinct models capturing each a given range of interactions (arranged by rows) at different levels of resolution in the phonon band structure (arranged by columns). The latter intent to assess the quality of the model by quantifying in reciprocal space the energetics of distortion patterns compatible with supercells of increasing sizes, not necessarily limited to the intrinsic range of interactions included in the model.

In the first column, a $2 \times 2 \times 2$ supercell is considered,

![](./images/1146417198521122819_3.jpg)

FIG. 3. Phonon dispersion curves of ${\text{BaTiO}}_{3}$ obtained from three distinct models each capturing a specific range of interactions (8, 2 and 2 from top to bottom rows) with varying levels of resolution in the phonon band structure (2, 4 and 8 from left to right columns). The first two models (blue, green) include analytically the dipole-dipole interactions that extend to infinite range M8+Dip and M2+Dip, while the third (red) omits them M2. The solid blue line present in all panels represents the reference model ($8×8×8$ $q$-point mesh with analytic treatment of the dipolar interactions).

which only give access to distortions patterns associated to phonon modes at the high-symmetry points (dots at $\Gamma$, $X$, ...) as schematized in Fig. 2. The second column ($4×4×4$ supercell) extend this to additional intermediate points along the dispersion paths. Finally, the third column ($8×8×8$ supercell) further increases the number of points offering a more detailed sampling of the phonon spectrum and overlays a faint colored line (blue, green and red) representing the frequencies as predicted by the model in the infinite supercell limit.

By rows, each model is constructed, as explained in Sec. II, using different $q$-point meshes for the calculation of the dynamical matrices and related to a specific range of interatomic-force constant in real space. The first-row model (blue points) is derived using an $8×8×8$ $q$-point mesh, while the second-row model (green points) and the third-row model (red points) with a $2×2×2$ mesh. It is important to emphasize that, within the described framework, the short-range part of the dipole-dipole interactions is inherently included up to the specified interaction range of each model. The long-range part of the dipole-dipole interactions is treated differently among the models. In the first two models, it is incorporated analytically as discussed in Sec. II. In contrast, the third model omits this contribution. We will refer to them as M8+Dip, M2+Dip, and M2, respectively.

For reference, the solid blue line, representing the phonon frequencies predicted by the M8+Dip model constructed with an $8×8×8$ $q$-point mesh and including long-range part of the dipole-dipole interactions, is superimposed on all panels. Importantly, the long-range part of the dipole-dipole interactions is only included in the plot of the phonon dispersion lines if the model accounts for this information.

We first compare the results of the $2×2×2$ model with the analytic electrostatic interactions (M2+Dip) with those of the reference model M8+Dip (8x8x8 $q$-mesh and full dipole-dipole contributions). As shown in Fig. 3, we notice only minor differences in the phonon dispersion curves, which show good agreement with what is reported in the literature [46]. This suggests that beyond a range of two unit cells, the interactions are mostly dominated by electrostatics while the short-range part nearly vanishes [47]. This observation is in line

with the results of Ref. [46] where the inclusion of the point $\Lambda=(0.25,0.25,0.25)$ on top of the $2{\times}2{\times}2$ $q$-point mesh was anticipated to provide good convergence of the phonon dispersion curves.

We then investigate the difference between the phonon dispersion curves obtained using the model constructed with a $2{\times}2{\times}2$ $q$-point mesh without the long-range component of dipole-dipole interactions (M2) and those obtained with the models that include this component M8+Dip and M2+Dip. When this long-range part of the dipolar contribution is omitted, Fig. 3 clearly shows that while the overall description of the phonon dispersion bands remains accurate, certain specific bands, particularly near the $\Gamma$ point, are inadequately described. This is evidenced by the extra unstable LO branch and the artificial degeneracy between the LO and TO modes of the topmost band at $\Gamma$. These discrepancies underscore the critical role of the long-range part of electrostatic interactions in accurately capturing the giant LO-TO splitting characteristic of BaTiO$_3$ [48, 49]. Including the long-range part of the dipole-dipole interactions corrects these inaccuracies, yielding a significantly improved representation of the phonon bands in this region. Nevertheless, the model is in good agreement with the reference dispersion curves for the remaining bands and for the LO branches away from $\Gamma$, as indicated by the overlap of the red curves with the blue one in Fig. 3(f,i).

Interestingly, the ferroelectric instability, intrinsic to TO modes, is very well captured even without incorporating the long-range part of electrostatic interactions in the model. This demonstrates that the short-range part of the Coulomb interactions alone (limited to two unit cells in this case) are sufficient to accurately describe this instability, indicating that in BaTiO$_3$, the long-range part of the Coulomb interaction does not play a significant role in its ferroelectric character. This may sound surprising at first sight since the ferroelectric instability has historically been explained from the Cochran picture [38] as the competition between the short-range and the dipole-dipole interactions. This picture was validated by first principles calculations in Ref. [39]. However, it is important to note that, as we have already mentioned before, the dipole-dipole interactions include both short-range and long-range parts and the competition between the so-called short-range and dipole-dipole interactions is already present in the interatomic force constants down to first neighbors as studied in Ref. [50]. Our results simply highlight this fact and demonstrate that, in BaTiO$_3$, the dominant contributions of the dipole-dipole interactions responsible for the ferroelectric instability are already well captured within a $2{\times}2{\times}2$ supercell.

This establishes for instance, that if a BaTiO$_3$ model is built using AI methods with a $2{\times}2{\times}2$ supercell for the training set, and so limiting implicitly the interaction range to 2 unit cells (equivalently to our $2{\times}2{\times}2$ model without dipole-dipole), the overall description of the material will remain largely accurate (the ferroelectric instability and its chain-like character [46] are preserved), except for the specific LO phonon branches affected by the missing long-range part of dipolar interactions, particularly near $\Gamma$. This discrepancy is unlikely to significantly impact the material's dynamics and phase transitions, as the phonon density of states remains well reproduced and the number of poorly described phonon bands is marginal. This is indeed confirmed in Fig. 4 where it appears that the phase transition sequence and hysteresis loops reproduced by M2 and M8+Dip models are very closely similar which explains why AI-based models limited to short-range interactions have been shown to successfully predict phase diagrams and ferroelectric transitions in complex materials [40, 51-54]. However, as it will be emphasized later, the improper treatment of the long-range part of dipolar interactions may introduce artificial discrepancies in the energy landscape, potentially affecting specific analyses. It must also be noted that,

![](./images/1146417198521122819_4.jpg)

FIG. 4. (a) Phase diagram of BaTiO$_3$, and (b) hysteresis loop of the $R3m$ phase at 50 K, reproduced using the M2 and M8+Dip models, as indicated in the legend. The supercell size used for the calculations was $12{\times}12{\times}12$.

although the present discussion might have some general character, the specific $2{\times}2{\times}2$ range is a priori material

![](./images/1146417198521122819_5.jpg)

FIG. 5. Phonon dispersion curves of $BaTiO_3$ along the $\Gamma - X$ branch for the same three models as described in Fig. 3. Blue lines corresponds to the phonon dispersion curves computed with the reference model.

dependent and cannot be taken for granted in a general case.

It is important at this stage to clarify the dis- tinction between the plotted phonon dispersion curves and the information within the model. Programs like PHONOPY [55] can include the contribution of dipole- dipole interactions on top of the information provided by the M2 model, thereby mimicking the phonon disper- sion curves of M2+Dip model plotted in Fig.3(f). This is indeed a common practice in the literature [40, 53, 56]. However, this correction is artificially made at the level of the post-processing while it is not present in the indepen- dent use of the model creating the illusion that the model phonons correspond to those plotted on Fig.3(f), while in reality, the model remains at the level of Fig. 3(i).

To conduct a deeper analysis, we now focus on the $\Gamma-$ X branch of the phonon dispersion curve, which allows us to explore larger supercells. The results, presented in Fig. 5, demonstrate that certain features, such as an extra unstable phonon branch predicted by the M2 model, are artifacts arising from the absence of the long-range part of the dipole-dipole interactions. When these interactions are included, the branch stabilizes. Similarly, the high- frequency LO mode is significantly corrected, eliminating its near degeneracy with the TO mode near the $\Gamma$ point, as predicted by the model when the long-range part of dipolar interactions are not included. In contrast, the remaining bands are reasonably well described.

Some key conclusions can be drawn at this stage. First, neglecting the long-range part of the dipole-dipole inter- actions leads to significant inaccuracies in the description of the LO modes, making it essential to include them whenever these bands are involved in the materials dis- tortions. Second, accounting for these interactions not only improves the accuracy of the phonon frequencies but also speeds up convergence, allowing a good description of the phonon dispersion curves with a relatively crude q-point grid value and providing a clear computational advantage as the short-range interactions are already rea- sonably well described with a supercell of size 2. Finally, a relatively small interaction cutoff might be sufficient to achieve a reasonable global description of the phonon dispersion curves for most materials (besides the descrip- tion of the LO modes), even capturing the ferroelectric instability. This explains the good performance of AI methods in accurately describing the phase diagram of BaTiO3 and other compounds even when trained on rel- atively small supercells [40]. However, it is important to keep in mind that this range is material dependent.

To point out the main and concrete deficiencies aris- ing from the exclusion of the long-range component of the dipole-dipole interactions, we can condense the LO phonon at $q=1 / 20$ u.c. $^{-1}$ from the spurious unstable branch predicted by the M2 model (Fig. 5a) As shown in Fig. 6, the condensation of such LO modes induce head- to-head and tail-to-tail domains that remain metastable due to the wrong description of the phonon branch. Clearly, this polarization state is unphysical as the di- vergence of the polarization generates bound charges on the material that enormously increase the electrostatic energy of the system. Similarly, when condensing to- gether two of these LO phonon modes directed along x and y, we can stabilize a lattice of center-convergent and center-divergent vortices demonstrating that more com- plex polar phases can also suffer from this spurious be- havior. As shown in Fig. 6, the energy lowering associ-ated to such fake metastable phase is not negligible $(\approx 10$  meV/f.u.) and comparable to that of the Pmma phase(≈ 10 meV/f.u.).

Properly including the long-range part of the dipole- dipole interactions, as discussed earlier, stabilizes the problematic phonon LO branch and corrects the issue, leading to the suppression of the related fake low-energy states. As shown in Fig. 6(c), the energy landscape as a function of the phonon mode amplitude changes dra- matically with the inclusion of the long-range part of the dipole-dipole interactions. The original double-well po- tential is replaced by a steeply rising energy surface, pre- venting the formation of bound charges and restoring a proper description of the material.

In the present examples, the apparent minima ob- served in Fig. 6(a) and (c) when limiting the range of interactions, are in fact saddle points of the Born- Oppenheimer energy surface once full structural relax- ation without symmetry constraints is allowed. This is confirmed by finite-temperature simulations using the

![](./images/1146417198521122819_6.jpg)

FIG. 6. Polarization map resulting from the condensation of (a) one and (c) two LO phonon modes (directed along $y$ and $x$)
from the $\Gamma-X$ branch at $q=1 / 20$ u.c. $^{-1}$ predicted by the model calculated using a 2x2x2 $q$-point mesh and excluding the
long range part of the dipole dipole interactions. (b,d) Energy landscapes as a function of the amplitude of the corresponding
LO modes predicted by the models calculated using a 2x2x2, 4x4x4, 8x8x8 $q$-point mesh without the long range part and a
2x2x2 with the long range part of the dipole-dipole interactions as specified in the legend.

M2 models, where the associated atomic configurations
are unstable and do not persist. This result is consis-
tent with the absence of report of such metastable phases
in previous AI models restricted to short-range interac-
tions. But we cannot exclude the presence of eventual
spurious local minima in other cases and, at least, our
Fig. 6 demonstrates that models limited to short-range
interactions will significantly over-stabilize head-to-head
or tail-to-tail polar configurations, which will unavoid-
ably affect phase competition.

In short, it is important to know that as soon as the
longitudinal optical phonon modes are involved in the
atomic displacements of the material under study, the
proper treatment of the long-range part of the dipole-
dipole interactions remains crucial to properly quantify
the energetics. This might become relevant when study-
ing topological textures, dynamics of large supercells or
thin films and superlattices where depolarizing fields play
an important role.

## IV. CONCLUSIONS

In summary, our results demonstrate that the over-
all phonon dispersion curves as well as structural phase
transitions with temperature and hysteresis loops are well
captured even when the interactions are limited to a rela-
tively small range which explains the success of AI-based
models in describing material properties, where the range
of interactions is inherently limited by the supercell size
used to generate the training set. Particularly surprising
is the fact that the ferroelectric instability is very well
described even in the case of $BaTiO_3$, where long-range
electrostatic interactions were thought to be crucial for
its ferroelectric character. Our results show, however,
that while these dipolar interactions are crucial, it is the
short-range part of them that appears to play a key role
in driving this effect.

However, despite these successes, some problems can
arise as a consequence of neglecting the long-range part
of the Coulomb interactions. In particular, some arti-
facts such as fake minima and improper treatment of LO
modes, which lead to inaccuracies in the phonon spec-
trum at particular bands and in the energetics of related
distortion patterns. These issues suggest that further re-
finement of the AI models is necessary whenever atomic
distortions associated to LO modes are active on the ma-
terial under study.

On the light of these results, a useful strategy for de-
termining when long-range electrostatic corrections are
needed to properly predict the energetics of some distor-
tion patterns is to project the atomic displacements onto
the phonon modes and check how much the LO modes
contribute. This approach helps to identify a posteri-
ori when the model's accuracy might be compromised,

allowing for necessary refinements to improve its predic-
tive power. We anticipate that these modifications will be
particularly useful in studying thin films, superlattices or
topological textures, where the intricate interplay of in-
teractions requires a more precise treatment. It is worth
noting that an analytical treatment of dipole-dipole in-
teractions is easy to incorporate whenever a reference
structure is used to build the model and is inherently in-
cluded for instance in effective Hamiltonian approaches
or effective atomic potential approaches. Strategies to
incorporate the long-range part of the dipole-dipole in-
teractions in machine learning potentials include charge
equilibration schemes [34], the on-the-fly computation of
maximally localized Wannier function centers [35, 36], or
a recently proposed modification of the model without
the need for additional first-principles calculations or re-
training discussed in Ref. [37].

## DATA AVAILABILITY

All data are available in the main text. The second-
principles model is open-source and available at Ref [57]
along with a validation assessment.

## ACKNOWLEDGMENTS

This work has been supported by the European
Union's Horizon 2020 research and innovation program
under Grant Agreement No. 964931 (TSAR) and
by F.R.S.-FNRS Belgium under PDR grants T.0107.20
(PROMOSPAN) and T.0128.25 (TOPOTEX). M.Y. ac-
knowledges financial support of the China Scholarship
Council program (Grant No.202306240141). F.G.O. ac-
knowledges financial support from MSCA-PF 101148906
funded by the European Union and the Fonds de
la Recherche Scientifique (FNRS) through the grant
FNRS-CR 1.B.227.25F. J. Z. acknowledges financial
support from National Natural Science Foundation
of China (NSFC, Grants 12274145), Guangdong Ba-
sic and Applied Basic Research Foundation, China
(Grant 2023A1515010672), and Guangdong Provincial
University Science and Technology Program (Grant
2023KTSCX029). The authors also acknowledge access
to the Consortium des Équipements de Calcul Intensif
(CÉCI), funded by the F.R.S.-FNRS under Grant No.
2.5020.11 and to the Tier-1 Lucia supercomputer of the
Walloon Region, infrastructure funded by the Walloon
Region under the grant agreement No. 1910247.

[1] J. E. Jones and S. Chapman, On the determination of
molecular fields. —II. from the equation of state of a
gas, *Proceedings of the Royal Society of London. Series
A, Containing Papers of a Mathematical and Physical
Character* **106**, 463 (1924).

[2] F. H. Stillinger and T. A. Weber, Computer simulation
of local order in condensed phases of silicon, *Phys. Rev.
B* **31**, 5262 (1985).

[3] J. Tersoff, New empirical approach for the structure and
energy of covalent systems, *Phys. Rev. B* **37**, 6991 (1988).

[4] A. Pedone, G. Malavasi, M. C. Menziani, A. N. Cor-
mack, and U. Segre, A new self-consistent empirical in-
teratomic potential model for oxides, silicates, and silica-
based glasses, *The Journal of Physical Chemistry B* **110**,
11780 (2006).

[5] T. Liang, Y. K. Shin, Y.-T. Cheng, D. E. Yilmaz, K. G.
Vishnu, O. Verners, C. Zou, S. R. Phillpot, S. B. Sinnott,
and A. C. van Duin, Reactive potentials for advanced
atomistic simulations, *Annual Review of Materials Re-
search* **43**, 109 (2013).

[6] J. A. Harrison, J. D. Schall, S. Maskey, P. T. Mikul-
ski, M. T. Knippenberg, and B. H. Morrow, Review of
force fields and intermolecular potentials used in atom-
istic computational materials research, *Applied Physics
Reviews* **5**, 031104 (2018).

[7] W. Kohn and L. J. Sham, Self-consistent equations in-
cluding exchange and correlation effects, *Phys. Rev.* **140**,
A1133 (1965).

[8] P. Hohenberg and W. Kohn, Inhomogeneous electron gas,
*Phys. Rev.* **136**, B864 (1964).

[9] J. P. Perdew, K. Burke, and M. Ernzerhof, Generalized
gradient approximation made simple, *Phys. Rev. Lett.*
**77**, 3865 (1996).

[10] M. C. Payne, M. P. Teter, D. C. Allan, T. A. Arias, and
J. D. Joannopoulos, Iterative minimization techniques
for ab initio total-energy calculations: molecular dynam-
ics and conjugate gradients, *Rev. Mod. Phys.* **64**, 1045
(1992).

[11] P. Ghosez and J. Junquera, Modeling of ferroelectric ox-
ide perovskites: From first to second principles, *Annual
Review of Condensed Matter Physics* **13**, 325 (2022).

[12] J. Behler and M. Parrinello, Generalized neural-network
representation of high-dimensional potential-energy sur-
faces, *Phys. Rev. Lett.* **98**, 146401 (2007).

[13] S. Chmiela, A. Tkatchenko, H. E. Sauceda, I. Poltavsky,
K. T. Schütt, and K.-R. Müller, Machine learning of ac-
curate energy-conserving molecular force fields, *Science
Advances* **3**, e1603015 (2017).

[14] R. Jinnouchi, J. Lahnsteiner, F. Karsai, G. Kresse, and
M. Bokdam, Phase transitions of hybrid perovskites sim-
ulated by machine-learning force fields trained on the fly
with bayesian inference, *Phys. Rev. Lett.* **122**, 225701
(2019).

[15] S. Gorsse, W.-C. Lin, H. Murakami, G.-M. Rignanese,
and A.-C. Yeh, Advancing refractory high entropy alloy
development with ai-predictive models for high tempera-
ture oxidation resistance, *Scripta Materialia* **255**, 116394
(2025).

[16] W. Zhong, D. Vanderbilt, and K. M. Rabe, Phase tran-
sitions in ${\text{BaTiO}}_{3}$ from first principles, *Phys. Rev. Lett.*

73, 1861 (1994).

[17] K. M. Rabe and U. V. Waghmare, Localized basis for effective lattice hamiltonians: Lattice Wannier functions, Phys. Rev. B 52, 13236 (1995).

[18] J. C. Wojdeł, P. Hermet, M. P. Ljungberg, P. Ghosez, and J. Íñiguez, First-principles model potentials for lattice- dynamical studies: general methodology and example of application to ferroic perovskite oxides, Journal of Physics: Condensed Matter 25, 305401 (2013).

[19] C. Escorihuela-Sayalero, J. C. Wojdeł, and J. Íñiguez, Ef- ficient systematic scheme to construct second-principles lattice dynamical models, Phys. Rev. B 95, 094115 (2017).

[20] P. García-Fernández, J. C. Wojdeł, J. Íñiguez, and J. Junquera, Second-principles method for materials sim- ulations including electron and lattice degrees of freedom, Phys. Rev. B 93, 195137 (2016).

[21] X. Gonze, B. Amadon, G. Antonius, F. Arnardi, L. Baguet, J.-M. Beuken, J. Bieder, F. Bottin, J. Bouchet, E. Bousquet, et al., The abinit project: Im- pact, environment and recent developments, Computer Physics Communications 248, 107042 (2020).

[22] L.-Q. Chen, Phase-field models for microstructure evo- lution, Annual Review of Materials Research 32, 113 (2002).

[23] M. Sepliansky, S. R. Phillpot, D. Wolf, M. G. Stachiotti, and R. L. Migoni, Atomic-level simulation of ferroelec- tricity in perovskite solid solutions, Applied Physics Let- ters 76, 3986 (2000).

[24] Y.-H. Shin, V. R. Cooper, I. Grinberg, and A. M. Rappe, Development of a bond-valence molecular-dynamics model for complex oxides, Phys. Rev. B 71, 054104 (2005).

[25] A. C. T. van Duin, S. Dasgupta, F. Lorant, and W. A. Goddard, ReaxFF: a reactive force field for hydrocar- bons, The Journal of Physical Chemistry A 105, 9396 (2001).

[26] D. Akbarian, D. E. Yilmaz, Y. Cao, P. Ganesh, I. Dabo, J. Munro, R. Van Ginhoven, and A. C. T. van Duin, Understanding the influence of defects and surface chem- istry on ferroelectric switching: a reaxFF investigation of BaTiO₃, Phys. Chem. Chem. Phys. 21, 18240 (2019).

[27] K. P. Kelley, A. N. Morozovska, E. A. Eliseev, V. Sharma, D. E. Yilmaz, A. C. T. van Duin, P. Ganesh, A. Borise- vich, S. Jesse, P. Maksymovych, N. Balke, S. V. Kalinin, and R. K. Vasudevan, Oxygen vacancy injection as a pathway to enhancing electromechanical response in fer- roelectrics, Advanced Materials 34, 2106426 (2022).

[28] A. Dhakane, T. Xie, D. E. Yilmaz, A. C. van Duin, B. G. Sumpter, and P. Ganesh, A graph dynamical neural net- work approach for decoding dynamical states in ferro- electrics., Carbon Trends 11, 100264 (2023).

[29] J. Wu, J. Yang, Y.-J. Liu, D. Zhang, Y. Yang, Y. Zhang, L. Zhang, and S. Liu, Universal interatomic potential for perovskite oxides, Phys. Rev. B 108, L180104 (2023).

[30] L. Zhang, J. Han, H. Wang, R. Car, and W. E, Deep potential molecular dynamics: A scalable model with the accuracy of quantum mechanics, Phys. Rev. Lett. 120, 143001 (2018).

[31] V. Botu and R. Ramprasad, Learning scheme to predict atomic forces and accelerate materials simulations, Phys. Rev. B 92, 094306 (2015).

[32] S. Klawohn, J. P. Darby, J. R. Kermode, G. Csányi, M. A. Caro, and A. P. Bartók, Gaussian approximation potentials: Theory, software implementation and appli- cation examples, The Journal of Chemical Physics 159, 174108 (2023).

[33] A. Singraber, J. Behler, and C. Dellago, Library-based lammps implementation of high-dimensional neural net- work potentials, Journal of Chemical Theory and Com- putation 15, 1827 (2019).

[34] Y. Shaidu, F. Pellegrini, E. Küçükbenli, R. Lot, and S. de Gironcoli, Incorporating long-range electrostatics in neural network potentials via variational charge equi- libration from shortsighted ingredients, npj Computa- tional Materials 10, 47 (2024).

[35] L. Zhang, H. Wang, M. C. Muniz, A. Z. Panagiotopou- los, R. Car, and W. E, A deep potential model with long-range electrostatic interactions, J. Chem. Phys. 156, 124107 (2022).

[36] A. Gao and R. C. Remsing, Self-consistent determination of long-range electrostatics in neural network potentials, Nature Communications 13, 1572 (2022).

[37] L. Monacelli and N. Marzari, Electrostatic interactions in atomistic and machine-learned potentials for polar mate- rials (2024), arXiv:2412.01642 [cond-mat.mtrl-sci].

[38] W. Cochran, Crystal stability and the theory of ferro- electricity, Advances in Physics 9, 387 (1960).

[39] P. Ghosez, X. Gonze, and J.-P. Michenaud, Coulomb in- teraction and ferroelectric instability of BaTiO₃, Euro- physics Letters 33, 713 (1996).

[40] L. Gigli, M. Veit, M. Kotiuga, G. Pizzi, N. Marzari, and M. Ceriotti, Thermodynamics and dielectric response of BaTiO₃ by data-driven modeling, npj Computational Materials 8, 209 (2022).

[41] F. Gómez-Ortiz, L. Bastogne, S. Anand, M. Yu, X. He, and P. Ghosez, Switchable skyrmion–antiskyrmion tubes in rhombohedral BaTiO₃ and related materials, Phys. Rev. B 111, L180104 (2025).

[42] X. Gonze and C. Lee, Dynamical matrices, born effective charges, dielectric permittivity tensors, and interatomic force constants from density-functional perturbation the- ory, Phys. Rev. B 55, 10355 (1997).

[43] R. Fletcher, Practical methods of optimization (John Wi- ley & Sons, 2000).

[44] S. Duane, A. D. Kennedy, B. J. Pendleton, and D. Roweth, Hybrid monte carlo, Physics letters B 195, 216 (1987).

[45] M. Betancourt, A conceptual introduction to Hamil- tonian Monte Carlo, arXiv preprint arXiv:1701.02434 10.48550/arXiv.1701.02434 (2017).

[46] X. G. Ph. Ghosez and J. P. Michenaud, Ab initio phonon dispersion curves and interatomic force constants of bar- ium titanate, Ferroelectrics 206, 205 (1998).

[47] X.-L. Chen, J.-Z. Zhao, and P. Ghosez, Lattice dynamical properties and interatomic force constants of transition metal oxide perovskite superlattices, Phys. Rev. B 110, 245302 (2024).

[48] W. Zhong, R. D. King-Smith, and D. Vanderbilt, Giant LO-TO splittings in perovskite ferroelectrics, Phys. Rev. Lett. 72, 3618 (1994).

[49] X. G. Ph. Ghosez and J.-P. Michenaud, Lattice dynam- ics and ferroelectric instability of barium titanate, Ferro- electrics 194, 39 (1997).

[50] P. Ghosez, E. Cockayne, U. V. Waghmare, and K. M. Rabe, Lattice dynamics of BaTiO₃, PbTiO₃, and

PbZrO₃: A comparative first-principles study, Phys. Rev. B 60, 836 (1999).

[51] L. Gigli, A. Goscinski, M. Ceriotti, and G. A. Tribello, Modeling the ferroelectric phase transition in barium ti- tanate with dft accuracy and converged sampling, Phys. Rev. B 110, 024101 (2024).

[52] C. Zhang and X. Chen, FerroAI: a deep learning model for predicting phase diagrams of ferroelectric materials, npj Computational Materials 11, 282 (2025).

[53] H.-C. Thong, X. Wang, J. Han, L. Zhang, B. Li, K. Wang, and B. Xu, Machine learning interatomic po- tential for molecular dynamics simulation of the ferroelec- tric KNbo₃ perovskite, Phys. Rev. B 107, 014101 (2023).

[54] N. Feng, H.-C. Thong, K. Wang, K. Bi, and B. Xu, Atomic-scale polarization switching driven by terahertz light in ferroelectric knbo₃, Phys. Rev. B 111, 024305 (2025).

[55] A. Togo, L. Chaput, T. Tadano, and I. Tanaka, Imple- mentation strategies in phonopy and phono3py, Journal of Physics: Condensed Matter 35, 353001 (2023).

[56] H. Zhang, H.-C. Thong, L. Bastogne, C. Gui, X. He, and P. Ghosez, Finite-temperature properties of the antifer- roelectric perovskite pbzro₃ from a deep-learning inter- atomic potential, Phys. Rev. B 110, 054109 (2024).

[57] M. Yu, S. Anand, J. Zhang, A. Sasani, L. Bastogne, F. Gómez-Ortiz, H. Xu, and G. Philippe, Second- Principles Model of BaTiO3 used on "Role of long-range dipolar interactions in the simulation of the properties of polar crystals using effective atomic potentials" (2025).