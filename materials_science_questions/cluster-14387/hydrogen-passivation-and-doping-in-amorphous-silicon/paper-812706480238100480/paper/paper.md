# Molecular-dynamics simulations of defect formation in hydrogenated amorphous silicon

I. Kwon, R. Biswas, and C. M. Soukoulis

Microelectronics Research Center, Department of Physics and Astronomy, Iowa State University, Ames, Iowa 50011
and Ames Laboratory, Iowa State University, Ames, Iowa 50011

(Received 10 July 1991; revised manuscript received 15 October 1991)

We have performed molecular-dynamics simulations to understand the Staebler-Wronski effect and defect formation in $a$-Si:H. The calculations are based on $a$-Si:H networks containing (1) only monohydride species and (2) both monohydride and dihydride species. A two- and three-body potential for Si-H interactions has been developed and used in conjunction with previous interatomic-potential models for Si-Si interactions. A localized excitation is used to model the nonradiative energy transfer of a photoexcited electron-hole pair to the lattice. Defect formation and annealing are discussed, together with their dependences on the positions of localized excitations, hydrogenation of Si, and the amount of excitation energy. The $a$-Si:H model with monohydride species only is stable to bond-breaking excitations. The $a$-Si:H model with both monohydride and dihydride species is less stable and does exhibit higher-energy dangling-bond states that can, however, be easily annealed away.

## I. INTRODUCTION

The understanding of the Staebler-Wronski (SW) effect, $^{1}$ the light-induced degradation of hydrogenated amorphous silicon ($a$-Si:H), is essential for both basic science and solar-energy-conversion applications. In the Staebler-Wronski effect, exposure of $a$-Si:H to light causes an increase in the density of metastable defect states in the gap region that can be removed by thermal annealing at $150^{\circ}\mathrm{C}$-$200^{\circ}\mathrm{C}.^{2}$ The metastable defects are paramagnetic and are commonly believed to be Si dangling bonds. Prolonged illumination, particularly at high intensities of light, lead to a saturation of the metastable defect density with saturated densities of the order of $10^{17}$ $\mathrm{cm}^{-3}$ for device-quality films. $^{3}$ Around room temperature the saturated metastable defect density is independent of light intensity and is found to correlate with the hydrogen content and optical band gap. $^{4}$

Despite extensive studies, the microscopic mechanisms for the SW effect remain unclear. Several different mechanisms have been proposed for the SW effect. The mechanisms, intrinsic to $a$-Si:H, include the breaking of weak Si-Si bonds by nonradiative recombination of photoexcited carriers and the creation of metastable dangling bonds, $^{2-7}$ the capture of carriers at existing charged dangling-bond sites, resulting in paramagnetic neutral dangling-bond defects, $^{5-8}$ and the generation of pairs of dangling- and floating-bond defects. $^{9}$ Another class of intrinsic mechanisms that has received much attention recently involves hydrogen-induced defects and includes the formation of metastable diatomic H complexes in $a$-Si:H, $^{10,11}$ the role of H interstitials, $^{12}$ and a metastable bridge-bonded H-interstitial defect in $a$-Si:H. $^{13}$ The mechanisms, extrinsic to $a$-Si:H, include a recent model for the metastable states of dopant atoms in $a$-Si:H and suggestions that impurity atoms may be responsible for light-induced degradation. $^{14}$

Among these various models, the bond-breaking model has received a great deal of attention. In this model the energy released by recombination of photoexcited electron-hole pairs leads to breaking of weak Si-Si bonds. Stutzmann, Jackson, and Tsai$^{2}$ proposed that the weak Si-Si bond would be a back bond of a monohydride (SiH) site and that hydrogen is then involved in the microscopic mechanism as a stabilizing element. Rupture of this weak Si-Si bond is followed by reorientation of the H-Si bond into the broken-bond location, leading to two dangling bonds that are pointed away from each other and are therefore paramagnetic. Although some experimental measurements could not be explained by the bond-breaking model, it is the most generally accepted model for the SW effect.

In this paper we examine the bond-breaking model with a realistic atomic model of $a$-Si:H to clarify the microscopic mechanisms for the SW effect and investigate mechanisms of defect formation in $a$-Si:H. We also compare the relative stability of $a$-Si:H models with and without dihydride species. To perform the molecular-dynamics calculations, we have developed a classical interatomic potential for Si-H interactions. A localized hot spot has been used to model the nonradiative energy transfer of photoexcited carriers to the system. Defect formation and annealing are discussed with their dependences on localized excitation location, hydrogenation of Si, and amount of energy transfer.

The development of the Si-H interatomic potential is described in Sec. II, whereas the atomic structure of the $a$-Si:H networks studied is described in Sec. III. The results of the molecular-dynamics simulations for the SW effect are discussed in Sec. IV, followed by the summary in Sec. V.

## II. INTERATOMIC POTENTIALS

Although there has been extensive development of classical interatomic potential models for Si-Si interactions, $^{15-17}$ the modeling of interatomic potentials for Si-H interactions is in an early stage of development. A

---

©1992 The American Physical Society

difficult problem in Si-H potential models is to ensure the monovalency of H. Recently, Mousseau and Lewis¹⁸ have developed a Stillinger-Weber-type interatomic po- tential¹⁵ for Si-H interactions to construct a computer- generated a-Si:H model. Although the structural and dynamical properties of a-Si:H networks developed with this potential agree well with experimental measure- ments, they used different potentials for bonded H-Si pairs and nonbonded H-Si pairs, which generally makes molecular-dynamics simulations difficult, particularly at finite temperature, where atomic environments can change. We have instead developed a set of two- and three-body interatomic potentials that can describe the energy of any arbitrary configuration of Si and H atoms without the need to classify bonded and nonbonded H-Si pairs.

It is crucial to have one Si-H potential for all geometries to study defect-formation processes in a-Si:H with molecular-dynamics simulations. In the bond- breaking process, or the H-switching mechanism of Stutzmann, Jackson, and Tsai,² the Si-H bond ruptures with H passing to a nonbonded transition state and then returns to a different bonding configuration. To describe such processes, it is essential to have a single Si-H poten- tial describing the various H-bonding environments. En- ergy calculations or molecular-dynamics simulations would not be possible if different potentials existed for different geometries. Although we study a-Si:H in this paper, we believe that the interatomic potential developed here could be useful for other Si-H systems as well.

Following previous classical models of Si-Si interac- tions,¹⁶ we partition the Si-H interaction into a sum of two- and three-body interactions. The two-body potential for Si-H interactions is
$$
V_{\mathrm{Si}-\mathrm{H}}^{2}(r)=\left[A_{1} \exp \left(-\lambda_{1} r\right)+A_{2} \exp \left(-\lambda_{2} r\right)\right] f_{c}(r), \quad(1)
$$
where $f_{c}(r)$ is the cutoff function,
$$
f_{c}(r)= \begin{cases}1 & \text { for } r \leq 1.70 \mathring{A} \\
0.5+0.5 \cos [(\pi / 0.2)(r-1.7)] & \text { for } 1.70 \mathring{A} \leq r \leq 1.90 \mathring{A} \\
0 & \text { for } r \geq 1.90 \mathring{A}.\end{cases}
\tag{2}
$$

The parameters¹⁹ were obtained by fitting to an ab initio calculation of the energy of H on a Si cluster.²⁰ This two-body potential has a minimum energy of $-3.05$ eV at $r=1.5$ Å, which is a good representation of the Si-H bond energy and bond length in a a-Si:H. In addition, the potential leads to the H-Si stretching-mode frequency of $2023 \mathrm{~cm}^{-1}$, in good agreement with experimental values in a-Si:H. The cutoff function $f_{c}(r)$ was designed to ensure the short-range nature of the interaction using a simple smooth functional form.

A three-body potential is essential for modeling the co- valent Si-H interaction and for stabilizing the tetrahedral environment of Si. We have developed a three-body po- tential for Si-H interactions, similar to the Si-Si intera- tomic potential,¹⁶ which is
$$
\begin{aligned}
V^{3}\left(r_{12}, r_{13}, \theta\right)= & B_{\mathrm{H}} \phi_{1,2}\left(r_{12}\right) \phi_{2}\left(r_{13}\right) \\
& ×\left(\cos \theta+\frac{1}{3}\right)^{2} g_{c_{1,2}}\left(r_{12}\right) g_{c_{2}}\left(r_{13}\right), \quad(3)
\end{aligned}
$$
where the subscripts 1 and 2 refer to Si-Si and Si-H in- teractions, respectively.²¹ As in previous work,¹⁶ we use a Keating form for the angular dependence of the poten- tial. Here $\phi_{1}(r)=\exp (-\alpha r^{2})$ and $\phi_{2}(r)=\exp (-\alpha_{H} r^{2})$ are radial functions and $g_{c_{1,2}}(r)=\{1+\exp [(r-r_{c_{1,2}}) /$  $\mu_{1,2}]]\}^{-1}$ is a cutoff function. We adopt the same form of the cutoff function $g_{c}(r)$ as used in previous work, except for new parameters $(r_{c_{2}}$ and $\mu_{2})$ for the Si-H interaction to ensure the shorter-range nature of the interaction. The parameters of the potential $B_{\mathrm{H}}$ and $\alpha_{\mathrm{H}}$ were obtained by fitting to the H-Si wagging mode of $630 \mathrm{~cm}^{-1}$ and the scissors bending mode of $897 \mathrm{~cm}^{-1}$ in $a$-Si:H. This three-body potential describes Si-Si-H, H-Si-H, or even Si-H-Si interactions, and its strength ensures that the lowest-energy configuration of a H atom is when the H atom is bonded to a single Si atom.

In conjunction with this Si-H model, we have used the Biswas-Hamann two- and three-body interatomic poten- tials for Si-Si interactions,¹⁶ which have had much suc- cess in describing several properties of pure $a$-Si and Si thin-film growth.²²

We have also used a repulsive H-H interatomic poten- tial $V_{\mathrm{H}-\mathrm{H}}^{2}$, similar to that employed by Mousseau and Lewis,¹⁸ which prevents H atoms from approaching un- physically close to each other, where²³
$$
\begin{aligned}
V_{\mathrm{H}-\mathrm{H}}^{2}(r)= & {\left[\varepsilon /\left(1-6 / \alpha_{\mathrm{HH}}\right)\right] } \\
& ×\left[\left(6 / \alpha_{\mathrm{HH}}\right) e^{\alpha_{\mathrm{HH}}(1-r / \sigma)}-(\sigma / r)^{6}\right]. \quad(4)
\end{aligned}
$$

Therefore, $\mathrm{H}_{2}$ molecular formation is inhibited in this scheme, but that is less important for the purposes of this paper. Clearly, an extension of this model would be to in- corporate a H-H molecular potential.

In our model all Si-H interactions are described through Eqs. (1)-(3). In contrast to this model, we note that Guttman and Fong²⁴ used a Keating potential for bonded Si-H pairs and a repulsive potential of the form $(r_{\mathrm{Si}-\mathrm{H}})^{-6}$ between H and Si atoms that were not bonded to each other in constructing $a$-Si:H models. Although a Keating potential can also give a good description of the vibrational properties of $a$-Si:H,²⁵ it is not sufficient for molecular-dynamics simulations.

### III. MODELS OF HYDROGENATED AMORPHOUS SILICON

Although the importance of $a$-Si:H to photovoltaics and other applications is well recognized through exten-

sive experimental studies, theoretical models of $a$-Si:H are few in contrast to pure $a$-Si models. $^{22,26-28}$ One reason is the difficulty in modeling the interatomic Si-H interactions. There is a class of $a$-Si:H structures generated by the saturation of dangling bonds in pure $a$-Si (Ref. 25) or built by hand $^{29}$ and then relaxed by Keating-type potentials for both H and Si atoms. A drawback of these models is that structural and vibrational properties of the $a$-Si:H networks can be studied only by static calculations. Recently, however, Chiarotti $et$ $al.^{30}$ have performed $ab$ $initio$ molecular-dynamics simulations to investigate static and dynamic properties of H in crystalline Si and $a$-Si based on the Car-Parrinello approach. Such $ab$ $initio$ molecular-dynamics calculations are more accurate but far less efficient for simulations with either long times or large systems than classical molecular dynamics. Mousseau and Lewis $^{18}$ have developed $a$-Si:H networks using a Stillinger-Weber-type interatomic potential for bonded H, but a different form of potential for nonbonded H.

In our approach we started with $a$-Si:H networks proposed by Guttman and Fong. $^{24}$ In their scheme a pair of H atoms were introduced to a four-coordinated pure $a$-Si network. Their approach consisted of first making a new bond between two Si atoms that were close but unbonded, breaking some other bond to each, and attaching H atoms to the two remaining dangling bonds. Hence two Si-H bonds in monohydride species were introduced with the two H atoms more spatially separated than if they were attached to a bonded pair of Si atoms. The procedure to make dihydride groups was to break two bonds on a Si atom, attach two H atoms there, and then make a new bond between the two remaining Si atoms that had dangling bonds. They used Keating-type potentials to relax the $a$-Si:H structures.

We have relaxed a monohydride $a$-Si:H network which contains 60 atoms with 54 Si atoms and 6 H atoms, i.e., containing 10 at. % H, with our Si-H interatomic potential together with the Biswas-Hamann Si-Si interatomic potential. Periodic-boundary conditions were used in a cubic cell to avoid spurious surface effects. The density of the system was allowed to vary to find the minimum-energy configuration. The most relaxed configuration (model 1) has a mass density about 8% smaller than crystalline Si density. An appealing feature of the model is the absence of dangling- or floating-bond defects. Bond cutoffs of 3.0 and 1.7 $\mathring{A}$ were used to define Si-Si and Si-H bonds, respectively. All H atoms remain in monohydride form, and the average Si-H bond length is 1.55 $\mathring{A}$, which is slightly larger than the experimental value 1.48 $\mathring{A}$. The Si-Si bonds have a distribution of bond lengths with a rms value of 0.10 $\mathring{A}$, whereas the Si-H bonds have an extremely narrow distribution of bond lengths with a rms value of 0.01 $\mathring{A}$.

The Si-Si partial pair-correlation function $g_{\text{Si-Si}}(r)$ for model 1 (Fig. 1) is comparable to the experimental measurement $^{31}$ except for the slight mismatch of the peak positions. The difference comes from the larger Si-Si equilibrium bond length (2.50 $\mathring{A}$) caused by strengthening the three-body Si-Si potential, which was necessary for the satisfactory description of $a$-Si. $^{22}$ Figure 2 shows the Si-H partial pair-correlation function $g_{\text{Si-H}}(r)$ together with the experimental result. $^{31}$ The agreement is remarkable, except that the first peak is much sharper than the experimental result. The experimental curve involves subtraction of structure-factor measurements of $a$-Si:H from a different $a$-Si sample, a procedure that also introduces uncertainties. The peak around $r=3.2$ $\mathring{A}$ corresponds to the distances between H atoms and the nearest Si neighbors of the monohydride Si atoms.

![](./images/812706480238100480_1.jpg)

FIG. 1. Si-Si partial pair-correlation function $g_{\text{Si-Si}}(r)$ for models 1 and 2 compared with the experimental result from Ref. 31.

![](./images/812706480238100480_2.jpg)

FIG. 2. Si-H partial pair-correlation function $g_{\text{Si-H}}(r)$ for models 1 and 2 compared with experimental result from Ref. 31.

The rms bond-angle deviation of model 1 is $10.4^\circ$, which is smaller than $11^\circ$-$14^\circ$ of typical computer-generated pure $a$-Si networks. $^{22,26-28}$ Also, there is no tail below $80^\circ$ or above $150^\circ$, in contrast to pure $a$-Si networks. The introduction of H into the $a$-Si networks substantially reduces the local strain of the system, as is known in experimental studies.

We have developed another network model of $a$-Si:H, which has dihydride species, to study further the role of H atoms and to compare stability properties of monohydride and dihydride species. This system consists of 54 Si atoms and 14 H atoms with 3 dihydrides and 8 monohydrides, i.e., 20.6 at. % H in the network. We first started with the network developed by Guttman and Fong, $^{24}$ which had 54 Si atoms and 3 dihydrides (6 H atoms). When we relaxed this network with our potential, there were 8 dangling-bond defects. Thus 8 H atoms were added to saturate dangling bonds and the system was relaxed further with variations of the density.

It is highly desirable to have coordination defect-free configurations for molecular-dynamics simulations of the light-induced defect-formation process. This is necessary so that light-induced (i.e., in the structure, excitation-induced) defects can be clearly distinguished from the initial defects. Also, device-quality $a$-Si:H films with defect densities of the order of $10^{15}\ \mathrm{cm}^{-3}$ may be best modeled by defect-free finite-size networks.

The most relaxed configuration (model 2) with a density about 10% smaller than the crystalline Si density has no coordination defects with a bond cutoff of $3.10\ \mathring{\mathrm{A}}$ for Si-Si bonds and $1.7\ \mathring{\mathrm{A}}$ for Si-H bonds. The rms bond-length deviation is $0.13\ \mathring{\mathrm{A}}$ for Si-Si bonds and $0.03\ \mathring{\mathrm{A}}$ for Si-H bonds. The partial pair-correlation functions of model 2 are very similar to those of model 1 (Figs. 1 and 2). However, the rms bond-angle deviation of model 2 is $9.51^\circ$, which is smaller than the $10.4^\circ$ of model 1. The increase of H content from 10 at. % of model 1 to 20.6 at. % of model 2 causes the decrease of the bond-angle distortions.

One important difference between models 1 and 2, which is not quite apparent in Fig. 1, is a substantial increase in the number of weak Si-Si bonds in model 2. This may reflect the lower network stability or the less desirable features of dihydride species. Alternatively, this may be due to the way in which the $a$-Si:H network was initially generated.

## IV. MOLECULAR-DYNAMICS SIMULATIONS OF DEFECT FORMATION
Metastable midgap defects are produced by either illumination or excess carrier injection in $a$-Si:H. Hence it is commonly believed that the nonradiative recombination of photoexcited carriers is responsible for the creation of metastable defects in $a$-Si:H under illumination. The transfer of the recombination energy of an excited electron-hole pair to the system is a difficult problem involving the electron-phonon interaction. A simple and computationally feasible way to model the energy transfer is to assume that the nonradiative recombination event creates a local region of a few excited atoms in the network. We expect this nonradiative decay channel to be much weaker than the dominant radiative decay channel. In fact, Weeks, Tully, and Kimmerling$^{32}$ have argued that the nonradiative carrier-recombination energy can be largely converted into the vibrational energy that is localized in the vicinity of a defect.

In the molecular-dynamics simulations, we create a localized excitation by providing excess kinetic energy to two bonded atoms and allowing the system to evolve dynamically and equilibrate. Velocities of atoms in the localized excitation can be in random directions, along the bond, or perpendicular to the bond. We examine whether the local excitation can lead to structural changes or defects. A convenient way to study resulting structural changes is by performing a steepest-descent relaxation on the equilibrated configuration. The steepest-descent relaxation gives the intrinsic configuration and separates the thermal disorder from the underlying structural disorder. The variables we have studied in the dynamical simulations are the spatial locations of localized excitations, the amount of excitation energies, and the relative effectiveness of bond stretching, bond bending, and random distortions. Some of these variables have already been studied in our earlier work on amorphous silicon without hydrogen. $^{33}$

We first note that model 1, containing monohydrides, is very stable to thermal annealing up to 700 K, and no lower-energy configuration could be produced by quenching or cooling from elevated temperatures. Hence this $a$-Si:H model with no coordination defects is a good starting configuration for the investigation of the Staebler-Wronski effect.

To examine the bond-breaking mechanism suggested by Stutzmann, Jackson, and Tsai, $^{2}$ we first tested Si-Si bonds on monohydride sites in the network of model 1. We have applied localized excitation on Si-Si bonds 40-41, 42-48, 42-43, and 42-7. 40 and 42 are monohydride sites, and the bond lengths of these bonds are longer than other Si-Si bonds on monohydride sites. Excitations of 1.7 eV (i.e., an excess kinetic energy of 0.85 eV to each atom) on various Si-Si bonds did not produce any structural change after dynamical evolution of 50 000 time steps (9.25 ps) in all cases. Figure 3(a) is the kinetic energy per atom in the vicinity of the localized excitation of the 40-41 pair as a function of time and shows how the system equilibrates. After the local excitation, the excess kinetic energies of atoms 40 and 41 dissipate into the rest of the system. The information on structural changes induced by the localized excitation is obtained by plotting the bond length of the excited Si-Si pair and the distances of the H atom from each of these atoms [Fig. 3(b)]. Bond lengths of these three atom pairs fluctuated only by a small amount, resulting in no defect creation. Simulations were done at room temperature and led to similar results, with the structure essentially returning to its initial configuration after equilibration of the excess energy.

One hypothesis we investigated was that the bond-breaking process may be a low-probability event, so that it may not be observed with a finite number of simulations. To increase the probability of such a bond-breaking process, we increased the excitation energy to as

large as 7.0 eV, far in excess of the possible recombina- tion energy or optical gap. In spite of the higher-energy 3.0-7.0-eV excitations, we did not observe any process where dangling bonds or other coordination defects were produced, except for the 19-29 case (at 3.0 eV), and the model returned to its initial configuration. We note that the breaking of bond 19-29 was seen by thermal activa- tion by equilibration above 700 K. Therefore, the break- ing of bond 19-29 with a localized excitation of 3.0 eV is not related to the light-induced degradation process in $a$-Si:H.

To study the effect of the finite size of the system, we constructed a system of 480 atoms by combining together 8 of the 60-atom cells. Excitations on this enlarged sys- tem gave similar results for the stability to local excita- tions. We conclude that the $a$-Si:H network (model 1) with 10 at. % H and no coordination defects, similar to device-quality $a$-Si:H materials, is very stable to local ex- citations.

![](./images/812706480238100480_3.jpg)

FIG. 3. (a) Kinetic energy per atom as a function of time when a localized excitation with excitation energy of 1.7 eV was given to atoms 40 and 41 in model 1. The directions of the ve- locities were random. The first shell is localized-excitation atoms 40 and 41, the second shell is the six nearest-neighbor atoms of 40 and 41, and the third shell the second-nearest- neighbor atoms. (b) Distances between excited atoms 40 and 41 [$r$(Si-Si)], between localized-excitation atom 40 and its bonded neighboring H atom [$r$(Si-H)], and the distance between the oth- er localized-excitation atom 41 and H atom, which is bonded to 40 [$r$(Si-H), nonbonded], as a function of time. One time step corresponds to 0.185 fs.

We next examined the stability of the model containing dihydride species to local excitations. In the $a$-Si:H net- work (model 2) with 20.6 at. % H and dihydride species, there were two cases of structural changes induced by lo- calized excitations. In the first case where atoms 49 and 50, which have higher site energies than other atoms, were excited in the bond direction with 1.7 eV excitation, the bond was broken. Both atoms were more than $4.2\ \mathring{\text{A}}$ apart after dynamical evolution of 70 000 time steps (12.95 ps) [Fig. 4(a)]. This time is sufficient for equilibra- tion of the system, as verified by the energy relaxation plot that is similar to Fig. 3(a).

Here the site energy of an atom is defined in such a way that a two-body potential is divided equally into each atom which is bonded to each other and a three-body po- tential is given to the vertex atom. Both 49 and 50 have very large bond-angle distortions, resulting in high site energies.

![](./images/812706480238100480_4.jpg)

FIG. 4. (a) Distance between atoms 49 and 50 in model 2 as a function of time. A localized excitation energy of 1.7 eV was given along the bond direction. (b) Distance between atoms 49 and 50 as a function of time when the system was thermally an- nealed at about 560 K after the localized excitation.

There are additional structural changes in the vicinity of the 49-50 pair induced by the localized excitation. Two neighboring bonds (13-52 and 32-54) are broken, and a new bond between 50 and 52 is formed. Therefore, there are four dangling bonds in the final configuration [Fig. 5(a)]. The energy of the final configuration after a steepest-descent relaxation is 0.64 eV ($\Delta E$) higher than the energy of the initial configuration [Fig. 5(b)].

We have calculated electronic densities of states of both the initial and final configurations using an empirical tight-binding method. For the Si-H interaction, we have used the tight-binding parameters obtained by Min et al. $^{34}$ by fitting to vibrational frequencies of SiH$_4$. These parameters describe quantitatively well the electronic and vibrational properties of the hydrogenated Si(111) surface. The Chadi parameters$^{35}$ were used for Si-Si interactions. Figure 6 shows that the initial configuration with no dangling bonds has a well-defined gap of about 1.3 eV, whereas the higher-energy configuration has gap states induced by dangling bonds.

We investigated the stability of the higher-energy configuration by thermally annealing the final configuration. Annealing in the temperature range from 270 to 560 K relaxed the structure back to its original configuration after 40 000 time steps, as illustrated by Fig. 4(b), where the bond between 49 and 50 reforms and then fluctuates about its initial distance 2.61 Å. This annealing kinetics indicates a small energy barrier $E_b$ of about 0.11 eV separating this higher-energy configuration from the initial configuration. The higher-energy configuration is then only weakly stable, and the annealing energy barrier is smaller than that expected for light-induced defects (0.9-1.3 eV).$^2$

![](./images/812706480238100480_5.jpg)

FIG. 5. (a) Atomic configuration in the vicinity of the 49-50 pair after a localized excitation of 1.7 eV on the pair. Bonds 49-50, 32-54, and 13-52 are broken (dashed line), and a new bond between 50 and 52 is formed (dot-dashed line), resulting in four dangling bonds (DB) in the network. (b) Schematic energy-level diagram for the two configurations before the localized excitation ($i$) and after ($f$).

![](./images/812706480238100480_6.jpg)

FIG. 6. Electronic density of the states for the initial configuration of model 2 (without defects) and for the configuration after excitation of atoms 49 and 50 (with defects) using the empirical tight-binding method.

The second example of defect formation by localized excitations is the 32-54 pair. The bond length of the 32-54 pair (2.875 Å) is longer than the average bond length (2.541 Å), and both atoms have higher site energies. At room temperature bond 32-54 was broken by an excitation of 1.7 eV, although no change was observed when the excitation was applied to the zero-temperature configuration. The energy of the final configuration after a steepest-descent relaxation is 0.15 eV higher than the energy of the initial configuration, and the higher-energy configuration has two dangling bonds (on 32 and 54). This high-energy configuration could be easily annealed back to the initial configuration at room temperature in 20 000 time steps, implying only a very small barrier of about 0.04 eV separating it from the initial state. This higher-energy configuration may in fact be a transient state rather than a metastable state. As seen in model 1, Si-H and Si-Si bonds in either monohydride or dihydride sites are stable to localized excitations.

The overall result is that model 1 with monohydride species only is stable to bond-breaking excitations with energies as high as 7.0 eV. Model 2 with both dihydride and monohydride species is less stable than model 1 and does have metastable higher-energy dangling-bond states induced by localized excitations. However, the energy barriers for the annealing of these dangling-bond states are small (0.04-0.11 eV), generally much smaller than that measured for light-induced defects (0.9-1.3 eV).$^2$ Hence these higher-energy configurations may be transient rather than metastable under the experimental conditions.

Experimentally, it is observed that $a$-Si:H with more dihydride species is more unstable to light-induced degradation.$^{36}$ Our results with model 2 may qualitatively support this trend, but further work is clearly necessary to

clarify a correlation, if any, between dihydride concentra- tion and light-induced defect densities.

## V. SUMMARY
We have performed molecular-dynamics simulations to understand microscopic mechanisms of the Staebler- Wronski effect in $a$-Si:H. Si-H two- and three-body in- teratomic potentials have been developed by fitting to $ab$ initio calculations of the energy of H on a Si cluster and H bending frequencies in $a$-Si:H. The Biswas-Hamann interatomic potential has been used for Si-Si interactions.

Using these potentials, we have examined two $a$-Si:H models: (1) a 60-atom model with 10 at. % H and only monohydride species and (2) a 68-atom model with 20.6 at. % H and both monohydride and dihydride species. The structural properties of these $a$-Si:H networks are well described and compare well with experimental mea- surements. The presence of H atoms reduces strain and disorder relative to networks without H.

A localized excitation has been used to model the non- radiative energy transfer of photoexcited carriers to the system, and structural changes induced by this excitation are studied in detail. The important result is that the single-phase $a$-Si:H monohydride model, with no coordi- nation defects or H-induced defects, is stable to bond- breaking excitations. The monohydride $a$-Si:H model has a H content similar to device-quality materials. This re- sult does not support the suggestion of Stutzmann, Jack- son, and Tsai$^2$ involving rupturing of a weak Si-Si back bond at a monohydride site. Alternatively, the proposed motion of H into the Si-Si bond site$^2$ may be a very-low- probability event.

The $a$-Si:H model with both dihydride and monohy- dride species is somewhat less stable than the model with only monohydride species. The dihydride-containing $a$- Si:H model does have higher-energy dangling-bond states induced by localized excitations, but these can easily an- neal back to the initial configuration (with annealing bar- riers of 0.04-0.11 eV). These dangling-bond states, which are produced by local excitations, are then not similar to metastable light-induced defect states.

All structural models are less than accurate descrip- tions of real $a$-Si:H films. The present structural models of $a$-Si:H cannot account for (i) defect formation that in- volves long-range H motion (over length scales of $10\ \mathring{A}$ or longer) or (ii) defect formation near microvoids in $a$-Si:H. Larger $a$-Si:H models with microvoids are clearly an as- pect for further work.

The present structural models that are free of coordi- nation defects do account for H concentrations, local structural disorder, and bond energies of experimental $a$- Si:H films. We hence expect that the present defect- formation results should be applicable to other $a$-Si:H models that are free of coordination defects.

## ACKNOWLEDGMENTS
We thank B. Min, Y. H. Lee, C. Z. Wang, C. T. Chan, and K. M. Ho for permitting us to use their results prior to publication. We acknowledge support from the Elec- tric Power Research Institute under the amorphous thin- film solar-cell program. We also acknowledge a NSF grant of Supercomputer time at the National Center for Supercomputer Applications, Champaign, IL. Work at the Ames Laboratory, operated by Iowa State University for the U.S. Department of Energy (USDOE) under Con- tract No. W-7405-ENG-82, was supported by the Direc- tor for Energy Research, Division of Materials Sciences, USDOE.

$^1$D. L. Staebler and C. R. Wronski, Appl. Phys. Lett. 31, 292 (1977).
$^2$M. Stutzmann, W. B. Jackson, and C. C. Tsai, Phys. Rev. B 32, 23 (1985).
$^3$H. R. Park, J. Z. Liu, and S. Wagner, Appl. Phys. Lett. 55, 2658 (1989).
$^4$H. R. Park, J. Z. Liu, P. Roca i Cabarrocas, A. Maruyama, M. Isomura, S. Wagner, J. R. Abelson, and F. Finger, Appl. Phys. Lett. 57, 1440 (1990).
$^5$R. S. Crandall, Phys. Rev. B 43, 4057 (1991), and references cit- ed therein.
$^6$R. Jones and G. M. Lister, Philos. Mag. B 61, 881 (1990).
$^7$M. Fathallah, Philos. Mag. B 61, 403 (1990).
$^8$D. Adler, J. Phys. (Paris) Colloq. 42, C4-3 (1981).
$^9$S. T. Pantelides, Phys. Rev. B 36, 3479 (1987).
$^{10}$S. B. Zhang, W. B. Jackson, and D. J. Chadi, Phys. Rev. Lett. 65, 2575 (1990).
$^{11}$W. Jackson, Phys. Rev. B 41, 10 257 (1990).
$^{12}$R. A. Street, in *Amorphous Silicon Materials and Solar Cells*, edited by B. L. Stafford, AIP Conf. Proc. No. 234 (AIP, New York, 1991), p. 21.
$^{13}$R. Biswas, I. Kwon, and C. M. Soukoulis, Phys. Rev. B 44, 3403 (1991).
$^{14}$D. Redfield and R. H. Bube, Phys. Rev. Lett. 65, 464 (1990).
$^{15}$F. Stillinger and T. Weber, Phys. Rev. B 31, 5263 (1985).
$^{16}$R. Biswas and D. R. Hamann, Phys. Rev. B 36, 6434 (1987); Phys. Rev. Lett. 55, 2001 (1985).
$^{17}$J. Tersoff, Phys. Rev. B 37, 6991 (1988).
$^{18}$N. Mosseau and L. J. Lewis, Phys. Rev. B 41, 3702 (1990); 43, 9810 (1991).
$^{19}$Parameters of the two-body potential are $A_1=0.111\,396\,7\times10^4$ eV, $A_2=-0.7\times10^3$ eV, $\lambda_1=2.7801\ \mathring{A}^{-1}$, and $\lambda_2=2.3616\ \mathring{A}^{-1}$.
$^{20}$A. Selmani, D. R. Salahub, and A. Yelson, Surf. Sci. 202, 269 (1988).
$^{21}$Parameters of the three-body potential are $B_{\text{H}}=22.6526$ eV, $\alpha_{\text{H}}=0.603\,34\ \mathring{A}^{-2}$, $r_c=1.8\ \mathring{A}$, and $\mu_2=0.2\ \mathring{A}$.
$^{22}$R. Biswas, G. S. Grest, and C. M. Soukoulis, Phys. Rev. B 36, 7437 (1987); I. Kwon, R. Biswas, G. S. Grest, and C. M. Soukoulis, ibid. 41, 3678 (1990).
$^{23}$Parameter for the H-H interaction are $\varepsilon=0.147$ eV, $\alpha_{\text{HH}}=15.20$, and $\sigma=1.9\ \mathring{A}$.
$^{24}$L. Guttmann and C. Y. Fong, Phys. Rev. B 26, 6756 (1982).
$^{25}$W. A. Kamitakahara, R. Biswas, A. M. Bouchard, F. Gompf, and J. B. Suck, in *Neutron Scattering for Materials Science*, edited by S. M. Shapiro, S. C. Moss, and J. D. Jorgensen, MRS Symposia Proceedings No. 166 (Materials Research So- ciety, Pittsburgh, 1990), p. 361.

$^{26}$F. Wooten, K. Winer, and D. Weaire, Phys. Rev. Lett. 54,
1392 (1985).

$^{27}$P. C. Kelires and J. Tersoff, Phys. Rev. Lett. 61, 562 (1988).

$^{28}$W. D. Luedtke and U. Landman, Phys. Rev. B 37, 4656
(1988); 40, 1164 (1989).

$^{29}$K. Winer and F. Wooten, Phys. Status Solidi B 124, 473
(1984).

$^{30}$Guido L. Chiarotti, F. Buda, R. C. Car, and M. Parinello, in
Impurities, Defects and Diffusion in Semiconductors: Bulk
and Layered Structures, edited by D. J. Wolford, J. Bernholc,
and E. E. Haller, MRS Symposia Proceedings No. 163 (MRS,
Pittsburgh, 1990), p. 383.

$^{31}$R. Bellisent, A. Menelle, W. S. Howells, Adrian C. Wright, T.
M. Brunier, R. N. Sinclair, and F. Jansen, Physica B
156&157, 217 (1989).

$^{32}$J. D. Weeks, J. C. Tully, and L. C. Kimmering, Phys. Rev. B
12, 3286 (1975).

$^{33}$I. Kwon, R. Biswas, and C. M. Soukoulis, Phys. Rev. B 43,
1859 (1991).

$^{34}$B. Min, Y. H. Lee, C. Z. Wang, K. M. Ho, and C. T. Chan,
Phys. Rev. B (to be published).

$^{35}$D. J. Chadi, Phys. Rev. Lett. 41, 1062 (1978); Phys. Rev. B 29,
785 (1984); Phys. Rev. Lett. 59, 1961 (1988).

$^{36}$V. L. Dalal and C. Fuleiman, in Amorphous Silicon
Technology—1989, edited by A. Madan, M. J. Thompson, P.
C. Taylor, Y. Hamakawa, and P. G. LeComber, MRS Sympo-
sium Proceedings No. 149 (Materials Research Society, Pitts-
burgh, 1989), p. 601.