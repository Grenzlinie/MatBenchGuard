# Combined $ab$ initio and classical potential simulation study on silicon carbide precipitation in silicon
F. Zirkelbach, $^{1, *}$ B. Stritzker, $^{1}$ K. Nordlund, $^{2}$ J. K. N. Lindner, $^{3}$ W. G. Schmidt, $^{3}$ and E. Rauls $^{3}$

$^{1}$Experimentalphysik IV, Universität Augsburg, 86135 Augsburg, Germany
$^{2}$Department of Physics, University of Helsinki, 00014 Helsinki, Finland
$^{3}$Department of Physics, Universität Paderborn, 33095 Paderborn, Germany

(Received 24 March 2011; revised manuscript received 1 July 2011; published 29 August 2011)

Atomistic simulations on the silicon carbide precipitation in bulk silicon employing both, classical potential and first-principles methods are presented. The calculations aim at a comprehensive, microscopic understanding of the precipitation mechanism in the context of controversial discussions in the literature. For the quantum-mechanical treatment, basic processes assumed in the precipitation process are calculated in feasible systems of small size. The migration mechanism of a carbon $\langle 100\rangle$ interstitial and silicon $\langle 110\rangle$ self-interstitial in otherwise defect-free silicon are investigated using density functional theory calculations. The influence of a nearby vacancy, another carbon interstitial and a substitutional defect as well as a silicon self-interstitial has been investigated systematically. Interactions of various combinations of defects have been characterized including a couple of selected migration pathways within these configurations. Most of the investigated pairs of defects tend to agglomerate allowing for a reduction in strain. The formation of structures involving strong carbon-carbon bonds turns out to be very unlikely. In contrast, substitutional carbon occurs in all probability. A long range capture radius has been observed for pairs of interstitial carbon as well as interstitial carbon and vacancies. A rather small capture radius is predicted for substitutional carbon and silicon self-interstitials. Initial assumptions regarding the precipitation mechanism of silicon carbide in bulk silicon are established and conformability to experimental findings is discussed. Furthermore, results of the accurate first-principles calculations on defects and carbon diffusion in silicon are compared to results of classical potential simulations revealing significant limitations of the latter method. An approach to work around this problem is proposed. Finally, results of the classical potential molecular dynamics simulations of large systems are examined, which reinforce previous assumptions and give further insight into basic processes involved in the silicon carbide transition.

DOI: 10.1103/PhysRevB.84.064126
PACS number(s): 61.72.J−, 66.30.Lw

## I. INTRODUCTION

The wide band gap semiconductor silicon carbide (SiC) is well known for its outstanding physical and chemical properties. The high breakdown field, saturated electron drift velocity and thermal conductivity in conjunction with the unique thermal and mechanical stability as well as radiation hardness makes SiC a suitable material for high-temperature, high-frequency, and high-power devices operational in harsh and radiation-hard environments. $^{1-5}$ Different modifications of SiC exist, which solely differ in the one-dimensional stacking sequence of identical, close-packed SiC bilayers. $^{6}$ Different polytypes exhibit different properties, in which the cubic phase of SiC (3C–SiC) shows increased values for the thermal conductivity and breakdown field compared to other polytypes, $^{3}$ which is, thus, most effective for high-performance electronic devices. Much progress has been made in 3C–SiC thin film growth by chemical vapor deposition (CVD) and molecular beam epitaxy (MBE) on hexagonal SiC (Refs. 7–9) and Si (Refs. 9–12) substrates. However, the frequent occurrence of defects such as twins, dislocations and double-position boundaries remains a challenging problem. Apart from these methods, high-dose carbon implantation into crystalline silicon (c-Si) with subsequent or in situ annealing was found to result in SiC microcrystallites in Si (Ref. 13) Utilized and enhanced, ion beam synthesis (IBS) has become a promising method to form thin SiC layers of high quality and exclusively of the 3C polytype embedded in and epitaxially aligned to the Si host featuring a sharp interface. $^{14-16}$

However, the process of the formation of SiC precipitates in Si during C implantation is not yet fully understood. High resolution transmission electron microscopy (HREM) studies $^{17-21}$ suggest the formation of C-Si dimers (dumbbells) on regular Si lattice sites, which agglomerate into large clusters indicated by dark contrasts and otherwise undisturbed Si lattice fringes in HREM, as can be seen in Fig. 1(a). A topotactic transformation into a 3C–SiC precipitate occurs once a critical radius of 2 nm to 4 nm is reached, which is manifested by the disappearance of the dark contrasts in favor of Moiré patterns [Fig. 1(b)] due to the lattice mismatch of 20% of the 3C–SiC precipitate and c–Si. The insignificantly lower Si density of SiC $(\approx[4]\%)$ compared to c–Si results in the emission of only a few excess Si atoms. In contrast, investigations of strained $Si_{1-y}C_{y}/Si$ heterostructures formed by IBS and solid-phase epitaxial regrowth $^{22}$ as well as MBE, $^{23}$ which incidentally involve the formation of SiC nanocrystallites, suggest an initial coherent precipitation by agglomeration of substitutional instead of interstitial C. Coherency is lost once the increasing strain energy of the stretched SiC structure surpasses the interfacial energy of the incoherent 3C–SiC precipitate and the Si substrate. These two different mechanisms of precipitation might be attributed to the respective method of fabrication. While in CVD and MBE surface effects need to be taken into account, SiC formation during IBS takes place in the bulk of the Si crystal. However, in another IBS study Nejim et al. $^{24}$ propose a topotactic transformation that is likewise based on the formation of substitutional C. The formation of substitutional C, however,

![](./images/811624034138587137_1.jpg)

FIG. 1. High resolution transmission electron microscopy (HREM) micrographs¹⁷ of agglomerates of C–Si dimers showing dark contrasts and otherwise undisturbed Si lattice fringes (a) and equally sized Moiré patterns indicating 3C–SiC precipitates (b).

is accompanied by Si self-interstitial atoms that previously occupied the lattice sites and a concurrent reduction of volume due to the lower lattice constant of SiC compared to Si. Both processes are believed to compensate one another. Solving this controversy and understanding the effective underlying processes will enable significant technological progress in 3C–SiC thin film formation driving the superior polytype for potential applications in high-performance electronic device production. It will likewise offer perspectives for processes that rely upon prevention of precipitation events, e.g., the fabrica- tion of strained pseudomorphic $Si_{1-y}C_y$ heterostructures.²⁵,²⁶

Atomistic simulations offer a powerful tool to study materials on a microscopic level providing detailed insight not accessible by experiment. A lot of theoretical work has been done on intrinsic point defects in Si (Refs. 27–40), threshold displacement energies in Si (Refs. 41 and 42) important in ion implantation, C defects and defect reactions in Si (Ref. 43–52) the SiC/Si interface 12,53–55 and defects in SiC (Refs. 56–60). However, none of the mentioned studies comprehenisively investigates all the relevant defect structures and reactions concentrated on the specific problem of 3C– SiC formation in C implanted Si. In fact, in a combined analytical potential molecular dynamics and ab initio study⁵⁰ the interaction of substitutional C with Si self-interstitials and C interstitials is evaluated. However, investigations are, first of all, restricted to interaction chains along the ⟨110⟩ and ⟨1̄10⟩ direction, secondly lacking combinations of C interstitials and, finally, not considering migration barriers providing further information on the probability of defect agglomeration.

In particular, molecular dynamics (MD) constitutes a suitable technique to investigate their dynamical and structural properties. Modelling the processes mentioned above requires the simulation of a large number of atoms $(\approx 10^5-10^6)$, which inevitably dictates the atomic interaction to be described by computationally efficient classical potentials. These are, however, less accurate compared to quantum-mechanical methods and their applicability for the description of the physical problem has to be verified beforehand. The most common empirical potentials for covalent systems are the Stillinger-Weber,⁶¹ Brenner,⁶² Tersoff⁶³ and environment- dependent interatomic potential.⁶⁴⁻⁶⁶ These potentials are assumed to be reliable for large-scale simulations⁶⁷⁻⁶⁹ on specific problems under investigation providing insight into phenomena that are otherwise not accessible by experimental or first-principles methods. Until recently,⁷⁰ a parametrization to describe the C–Si multicomponent system within the mentioned interaction models did only exist for the Tersoff⁷¹ and related potentials, e.g., the one by Gao and Weber⁷² as well as the one by Erhart and Albe.⁷³ All these potentials are short-range potentials employing a cut-off function, which drops the atomic interaction to zero in between the first and second nearest-neighbor distance. It was shown that the Tersoff potential properly describes binding energies of combinations of C defects in Si (Ref. 50). However, investigations of brittleness in covalent materials⁷⁴ identified the short-range character of these potentials to be responsible for overestimated forces necessary to snap the bond of two neighbored atoms. In a previous study,⁷⁵ we determined the influence on the migration barrier for C diffusion in Si. Using the Erhart/Albe (EA) potential,⁷³ an overestimated barrier height compared to ab initio calculations and experiment is obtained. A proper description of C diffusion, however, is crucial for the problem under study.

In this work, a combined ab initio and empirical potential simulation study on the initially mentioned SiC precipitation mechanism has been performed. By first-principles atomistic simulations this work aims to shed light on basic processes involved in the precipitation mechanism of SiC in Si. During implantation, defects such as vacancies (V), substitutional C $(C_s)$, interstitial C $(C_i)$, and Si self-interstitials $(Si_i)$ are created, which play a decisive role in the precipitation process. A systematic investigation of density functional theory (DFT) calculations of the structure, energetics and mobility of C defects in Si as well as the influence of other point defects in the surrounding is presented. Furthermore, highly accurate quantum-mechanical results have been used to identify short- comings of the classical potentials, which are then taken into account in these type of simulations.

## II. METHODOLOGY

The first-principles DFT calculations have been performed with the plane-wave based Vienna ab initio Simulation package (VASP).⁷⁶ The Kohn-Sham equations were solved using the generalized-gradient exchange-correlation func- tional approximation proposed by Perdew and Wang.⁷⁷,⁷⁸ The electron-ion interaction is described by norm-conserving ultra-soft pseudopotentials⁷⁹ as implemented in VASP (Ref. 80) Throughout this work, an energy cut-off of 300 eV was used to expand the wave functions into the plane-wave basis. To reduce the computational effort sampling of the Brillouin zone was restricted to the $\Gamma$-point, which has been shown to yield reliable results.⁴⁴ The defect structures and the migration paths were modelled in cubic supercells with a side length of 1.6 nm containing 216 Si atoms. Formation energies and structures are reasonably converged with respect to the system size. The ions and cell shape were allowed to change in order to realize a constant pressure simulation. The observed changes in volume were less than 0.2 % of the volume indicating a rather low dependence of the results

on the ensemble choice. Ionic relaxation was realized by the conjugate gradient algorithm. Spin polarization has been fully accounted for.

For the classical potential calculations, defect structures were modeled in a supercell of nine Si lattice constants in each direction consisting of 5832 Si atoms. Reproducing the SiC precipitation was attempted by the successive insertion of 6000 C atoms (the number necessary to form a 3C–SiC precipitate with a radius of $\approx 3.1$ nm) into the Si host, which has a size of 31 Si unit cells in each direction consisting of 238328 Si atoms. At constant temperature 10 atoms were inserted at a time. Three different regions within the total simulation volume were considered for a statistically distributed insertion of the C atoms: $V_1$ corresponding to the total simulation volume, $V_2$ corresponding to the size of the precipitate, and $V_3$, which holds the necessary amount of Si atoms of the precipitate. After C insertion, the simulation has been continued for 100 ps and is cooled down to $20^\circ$ C afterward. A Tersoff-like bond order potential by Erhart and Albe (EA)$^{73}$ has been utilized, which accounts for nearest neighbor interactions realized by a cut-off function dropping the interaction to zero in between the first and second nearest neighbor distance. The potential was used as is, i.e., without any repulsive potential extension at short interatomic distances. Constant pressure simulations are realized by the Berendsen barostat$^{81}$ using a time constant of 100 fs and a bulk modulus of 100 GPa for Si. The temperature was kept constant by the Berendsen thermostat$^{81}$ with a time constant of 100 fs. Integration of the equations of motion was realized by the velocity Verlet algorithm$^{82}$ and a fixed time step of 1 fs. For structural relaxation of defect structures, the same algorithm was used with the temperature set to 0 K.

The formation energy $E - N_{\text{Si}} \mu_{\text{Si}} - N_{\text{C}} \mu_{\text{C}}$ of a defect configuration is defined by choosing SiC as a particle reservoir for the C impurity, i.e., the chemical potentials are determined by the cohesive energies of a perfect Si and SiC supercell after ionic relaxation. This corresponds to the definition utilized in another study on C defects in Si$^{44}$ that we compare our results to. Migration and recombination pathways have been investigated utilizing the constraint conjugate gradient relaxation technique.$^{83}$ Although not guaranteed to find the true minimum energy path, the method turns out to identify reasonable pathways for the investigated structures. Time constants of 1 fs, which corresponds to direct velocity scaling, and 100 fs, which results in weaker coupling to the heat bath allowing the diffusing atoms to take different pathways, were used for the Berendsen thermostat for structural relaxation within the migration calculations utilizing classical potentials. The binding energy of a defect pair is given by the difference of the formation energy of the complex and the sum of the two separated defect configurations. Accordingly, energetically favorable configurations result in binding energies below zero whereas unfavorable configurations show positive values for the binding energy. The interaction strength, i.e., the absolute value of the binding energy, approaches zero for increasingly non-interacting isolated defects.

## III. COMPARISON OF CLASSICAL POTENTIAL AND FIRST-PRINCIPLES METHODS

In a first step, quantum-mechanical calculations of defects in Si and respective diffusion processes are compared to classical potential simulations as well as to results from literature. Shortcomings of the analytical potential approach are revealed and its applicability is discussed.

### A. Carbon and silicon defect configurations

Table I summarizes the formation energies of relevant defect structures for the EA and DFT calculations. The respective structures are shown in Fig. 2.

Although discrepancies exist, classical potential, and first-principles methods depict the correct order of the formation energies with regard to C defects in Si. Substitutional C ($\text{C}_\text{s}$) constitutes the energetically most favorable defect configuration. Since the C atom occupies an already vacant Si lattice site, $\text{C}_\text{s}$ is not an interstitial defect. The quantum-mechanical result agrees well with the result of another *ab initio* study.$^{44}$ Clearly, the empirical potential underestimates the $\text{C}_\text{s}$ formation energy. The C interstitial defect with the lowest energy of formation has been found to be the C–Si $\langle 100 \rangle$ interstitial dumbbell ($\text{C}_\text{i}$ $\langle 100 \rangle$ DB), which thus, constitutes the ground state of an additional C impurity in otherwise perfect c–Si. This finding is in agreement with several theoretical$^{44–47}$ and experimental$^{84,85}$ investigations. However, to our best knowledge, no energy of formation based on first-principles calculations has yet been explicitly stated in literature for the ground-state configuration. Astonishingly, EA and DFT predict almost equal formation

TABLE I. Formation energies of C and Si point defects in cSi determined by classical potential and *ab initio* methods. The formation energies are given in electron volts. T denotes the tetrahedral and BC the bond-centered configuration. Subscript i and s indicates the interstitial and substitutional configuration. Dumbbell configurations are abbreviated by DB. Formation energies for unstable configurations obtained by classical potential MD are marked by an asterisk and determined by using the low kinetic energy configuration shortly before the relaxation into the more favorable configuration starts.

<table>
  <thead>
    <tr>
      <th></th>
      <th>$\text{Si}_\text{i}$ $\langle 110 \rangle$ DB</th>
      <th>$\text{Si}_\text{i}$ H</th>
      <th>$\text{Si}_\text{i}$ T</th>
      <th>$\text{Si}_\text{i}$ $\langle 100 \rangle$ DB</th>
      <th>V</th>
      <th>$\text{C}_\text{s}$</th>
      <th>$\text{C}_\text{i}$ $\langle 100 \rangle$ DB</th>
      <th>$\text{C}_\text{i}$ $\langle 110 \rangle$ DB</th>
      <th>$\text{C}_\text{i}$ BC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Present study</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>VASP</td>
      <td>3.39</td>
      <td>3.42</td>
      <td>3.77</td>
      <td>4.41</td>
      <td>3.63</td>
      <td>1.95</td>
      <td>3.72</td>
      <td>4.16</td>
      <td>4.66</td>
    </tr>
    <tr>
      <td>Erhart/Albe</td>
      <td>4.39</td>
      <td>4.48*</td>
      <td>3.40</td>
      <td>5.42</td>
      <td>3.13</td>
      <td>0.75</td>
      <td>3.88</td>
      <td>5.18</td>
      <td>5.59*</td>
    </tr>
    <tr>
      <td>Other *ab initio* studies</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Ref. 36</td>
      <td>3.40</td>
      <td>3.45</td>
      <td>–</td>
      <td>–</td>
      <td>3.53</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Ref. 33</td>
      <td>3.31</td>
      <td>3.31</td>
      <td>3.43</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Refs. 44 and 45</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>1.89$^{44}$</td>
      <td>x</td>
      <td>–</td>
      <td>x+2.1$^{45}$</td>
    </tr>
  </tbody>
</table>

![](./images/811624034138587137_2.jpg)

FIG. 2. (Color online) Configurations of Si and C point defects in Si. Si and C atoms are illustrated by yellow and gray spheres respectively. Bonds of the defect atoms are drawn in red color. Dumbbell configurations are abbreviated by DB.

energies. There are, however, geometric differences with regard to the DB position within the tetrahedron spanned by the four neighbored Si atoms, as already reported in a previous study. $^{75}$ Since the energetic description is considered more important than the structural description, minor discrepancies of the latter are assumed non-problematic. The second most favorable configuration is the $C_{i}\langle 110\rangle$ DB followed by the $C_{i}$ bond-centered (BC) configuration. For both configurations EA overestimates the energy of formation by approximately 1 eV compared to DFT. Thus, nearly the same difference in energy has been observed for these configurations in both methods. However, we have found the BC configuration to constitute a saddle point within the EA description relaxing into the $\langle 110\rangle$ configuration. Because of the high formation energy of the BC defect resulting in a low probability of occurrence of this defect, the wrong description is not posing a serious limitation of the EA potential. A more detailed discussion of C defects in Si modeled by EA and DFT including further defect configurations can be found in our recently published article. $^{75}$

Regarding intrinsic defects in Si, classical potential and ab initio methods predict energies of formation that are within the same order of magnitude. However, discrepancies exist. Quantum-mechanical results reveal the $Si_{i}\langle 110\rangle$ DB to com pose the energetically most favorable configuration closely fol- lowed by the hexagonal and tetrahedral configuration, which is the consensus view for $Si_{i}$ and compares well to results from literature. $^{33,36}$ The EA potential does not reproduce the correct ground state. Instead, the tetrahedral defect configuration is favored. This limitation is assumed to arise due to the cut-off. In the tetrahedral configuration the second neighbors are only slightly more distant than the first neighbors, which creates the particular problem. Indeed, an increase of the cut-off results in increased values of the formation energies, $^{73}$ which is most significant for the tetrahedral configuration. The same issue has already been discussed by Tersoff $^{43}$ with regard to the description of the tetrahedral $C$ defect using his potential. The hexagonal configuration is not stable within the classical potential calculations opposed to results of the authors of the potential. $^{73}$ In the first two pico seconds, while kinetic energy is decoupled from the system, the $Si_{i}$ seems to condense at the hexagonal site. The formation energy of 4.48 eV is determined by this low kinetic energy configuration shortly before the relaxation process starts. The $Si_{i}$ atom then begins to slowly move toward an energetically more favorable position very close to the tetrahedral but slightly displaced along the three coordinate axes. The formation energy of 3.96 eV for this type of interstitial is equal to the result for the hexagonal in the original work. $^{73}$ Obviously, the authors did not carefully check the relaxed results assuming a hexagonal configuration. As has been shown, variations of this defect exist, in whichthe displacement is only along two $\langle 100\rangle$ axis $(E_{f}=3.8 eV)$  or along a single $\langle 100\rangle$ axis $(E_{f}=3.6 eV)$ successively approximating the tethrahedral configuration and formation energy. $^{86}$ The existence of these local minima located near the tetrahedral configuration seems to be an artifact of the analytical potential without physical authenticity revealing fundamental problems of analytical potential models for describing defect structures. However, further investigations revealed the energy barrier of the transition from the artificial into the tetrahedral configuration to be smaller than 0.2 eV. Hence, these artifacts have a negligible influence in finite temperature simulations. Although not completely rendering impossible further, more challenging empirical potential stud- ies on large systems, these artifacts have to be taken into account in the following investigations of defect combinations.

Instead of giving an explicit value of the energy of formation, Capaz et al., $^{45}$ investigating migration pathways of the $C_{i}\langle 100\rangle$ DB, find this defect to be 2.1 eV lower in energy than the BC configuration. The BC configuration isclaimed to constitute the saddle point within the $C_{i}[\begin{array}{lll}0 & 0 & \overline{1}\end{array}]$  DB migration path residing in the $(\begin{array}{lll}1 & 1 & 0\end{array})$ plane and, thus, interpreted as the barrier of migration for the respective path. However, the present study indicates a local minimum state for the BC defect if spin polarized calculations are performed resulting in a net magnetization of two electrons localized in a torus around the C atom. Another DFT calculation without fully accounting for the electron spin results in the smearing of a single electron over two non-degenerate Kohn-Sham states and an increase of the total energy by 0.3 eV for the BC configuration. A more detailed description can be found in a previous study. $^{75}$ Next to the $C_{i}$ BC configuration, the vacancy and $Si_{i}\langle 100\rangle$ DB have to be treated by taking into account the spin of the electrons. For the vacancy, the net spin up electron density is localized in caps at the four surroundingSi atoms directed toward the vacant site. In the $Si_{i}\langle 100\rangle$  DB configuration, the net spin up density is localized in two caps at each of the two DB atoms perpendicularly aligned to the bonds to the other two Si atoms respectively. No other configuration, within the ones that are mentioned, is affected.

![](./images/811624034138587137_3.jpg)

FIG. 3. (Color online) Migration barrier and structures of the [0 0 $\overline{1}$] DB (left) to the [0 $\overline{1}$ 0] DB (right) transition involving the [110] DB (center) configuration. Migration simulations were performed utilizing time constants of 1 fs (solid line) and 100 fs (dashed line) for the Berendsen thermostat.

### B. Mobility of carbon defects

To accurately model the SiC precipitation, which involves the agglomeration of C, a proper description of the migration process of the C impurity is required. As shown in a previous study, $^{75}$ quantum-mechanical results properly describe the $C_{i}$ $\langle 100 \rangle$ DB diffusion resulting in a migration barrier height of 0.90 eV excellently matching experimental values of 0.70–0.87 eV$^{85,87,88}$ and, for this reason, reinforcing the respective migration path as already proposed by Capaz *et al.*$^{45}$ During transition, a $C_{i}$ [0 0 $\overline{1}$] DB migrates toward a $C_{i}$ [0 $\overline{1}$ 0] DB located at the neighbored lattice site in [1 1 $\overline{1}$] direction. However, it turned out that the description fails if the EA potential is used, which overestimates the migration barrier (2.2 eV) by a factor of 2.4. In addition a different diffusion path is found to exhibit the lowest migration barrier. A $C_{i}$ [0 0 $\overline{1}$] DB turns into the [0 0 1] configuration at the neighbored lattice site. The transition involves the $C_{i}$ BC configuration, however, which was found to be unstable relaxing into the $C_{i}$ $\langle 110 \rangle$ DB configuration. If the migration is considered to occur within a single step, the kinetic energy of 2.2 eV is sufficient to turn the $\langle 100 \rangle$ DB into the BC and back into a $\langle 100 \rangle$ DB configuration. If, however, a two step process is assumed, the BC configuration will most probably relax into the $C_{i}$ $\langle 110 \rangle$ DB configuration resulting in different relative energies of the intermediate state and the saddle point. For the latter case, a migration path, which involves a $C_{i}$ $\langle 110 \rangle$ DB configuration, is proposed and displayed in Fig. 3. The activation energy of approximately 2.24 eV is needed to turn the $C_{i}$ [0 0 $\overline{1}$] DB into the $C_{i}$ [1 1 0] DB located at the neighbored lattice site in [1 1 $\overline{1}$] direction. Another barrier of 0.90 eV exists for the rotation into the $C_{i}$ [0 $\overline{1}$ 0] DB configuration for the path obtained with a time constant of 100 fs for the Berendsen thermostat. Roughly the same amount would be necessary to excite the $C_{i}$ [1 1 0] DB to the BC configuration (0.40 eV) and a successive migration into the [0 0 1] DB configuration (0.50 eV) as displayed in our previous study.$^{75}$ The former diffusion process, however, would more nicely agree with the ab initio path, because the migration is accompanied by a rotation of the DB orientation. By considering a two-step process and assuming equal preexponential factors for both diffusion steps, the probability of the total diffusion event is given by $\exp[(2.24\,\text{eV} + 0.90\,\text{eV})/k_{\text{B}}T]$, which corresponds to a single diffusion barrier that is 3.5 times higher than the barrier obtained by ab initio calculations.

![](./images/811624034138587137_4.jpg)

FIG. 4. (Color online) Position of the initial $C_{i}$ [0 0 $\overline{1}$] DB (I) [Fig. 4(a)] and of the lattice site chosen for the initial $\text{Si}_{i}$ $\langle 110 \rangle$ DB ($\text{Si}_{i}$) [Fig. 4(b)]. Lattice sites for the second defect used for investigating defect pairs are numbered from 1 to 5.

Accordingly, the effective barrier of migration of $C_{i}$ is overestimated by a factor of 2.4 to 3.5 compared to the highly accurate quantum-mechanical methods. This constitutes a serious limitation that has to be taken into account for modeling the C–Si system using the otherwise quite promising EA potential.

### IV. QUANTUM-MECHANICAL INVESTIGATIONS OF DEFECT COMBINATIONS AND RELATED DIFFUSION PROCESSES

The implantation of highly energetic C atoms results in a multiplicity of possible defect configurations. Next to individual $\text{Si}_{i}$, $C_{i}$, V, and $C_{s}$ defects, combinations of these defects and their interaction are considered important for the problem under study. In the following, pairs of the ground state and, thus, most probable defect configurations that are believed to be fundamental in the Si to SiC conversion and related diffusion processes are investigated. These systems are small enough to allow for a first-principles treatment.

#### A. Pairs of $C_{i}$

Figure 4(a) schematically displays the initial $C_{i}$ [0 0 $\overline{1}$] DB structure and various positions for the second defect (1–5) that have been used for investigating defect pairs. Table II summarizes resulting binding energies for the combination with a second C–Si $\langle 100 \rangle$ DB obtained for different orientations at positions 1 to 5. Most of the obtained configurations result in binding energies well below zero indicating a preferable agglomeration of this type of defects. For increasing distances of the defect pair, the binding energy approaches to zero (R in Table II) as it is expected for noninteracting isolated defects. Energetically favorable and unfavorable configurations can be explained by stress compensation and increase respectively

TABLE II. Binding energies in eV of $C_i$ $\langle 100 \rangle$-type defect pairs. Equivalent configurations exhibit equal energies. Column 1 lists the orientation of the second defect, which is combined with the initial $C_i$ [0 0 $\overline{1}$] DB. The position index of the second defect is given in the first row according to Fig. 4. R corresponds to the position located at $\frac{a_{Si}}{2}[323]$ relative to the initial defect position, which is the maximum realizable defect separation distance ($\approx$1.3 nm) due to periodic boundary conditions.

<table>
  <thead>
    <tr>
      <th>
      </th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>R</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>[0 0 $\overline{1}$]</td>
      <td>$-0.08$</td>
      <td>$-1.15$</td>
      <td>$-0.08$</td>
      <td>$0.04$</td>
      <td>$-1.66$</td>
      <td>$-0.19$</td>
    </tr>
    <tr>
      <td>[0 0 1]</td>
      <td>$0.34$</td>
      <td>$0.004$</td>
      <td>$-2.05$</td>
      <td>$0.26$</td>
      <td>$-1.53$</td>
      <td>$-0.19$</td>
    </tr>
    <tr>
      <td>[0 $\overline{1}$ 0]</td>
      <td>$-2.39$</td>
      <td>$-0.17$</td>
      <td>$-0.10$</td>
      <td>$-0.27$</td>
      <td>$-1.88$</td>
      <td>$-0.05$</td>
    </tr>
    <tr>
      <td>[0 1 0]</td>
      <td>$-2.25$</td>
      <td>$-1.90$</td>
      <td>$-2.25$</td>
      <td>$-0.12$</td>
      <td>$-1.38$</td>
      <td>$-0.06$</td>
    </tr>
    <tr>
      <td>[$\overline{1}$ 0 0]</td>
      <td>$-2.39$</td>
      <td>$-0.36$</td>
      <td>$-2.25$</td>
      <td>$-0.12$</td>
      <td>$-1.88$</td>
      <td>$-0.05$</td>
    </tr>
    <tr>
      <td>[1 0 0]</td>
      <td>$-2.25$</td>
      <td>$-2.16$</td>
      <td>$-0.10$</td>
      <td>$-0.27$</td>
      <td>$-1.38$</td>
      <td>$-0.06$</td>
    </tr>
  </tbody>
</table>

based on the resulting net strain of the respective configuration of the defect combination. Antiparallel orientations of the second defect, i.e., [0 0 1] for positions located below the [0 0 1] plane with respect to the initial one (positions 1, 2, and 4) form the energetically most unfavorable configurations. In contrast, the parallel and particularly the twisted orientations constitute energetically-favorable configurations, in which a vast reduction of strain is enabled by combination of these defects.

Mattoni $et\ al.^{50}$ predict the ground-state configuration for a [1 0 0] or equivalently a [0 1 0] defect created at position 1. Both defects basically maintain the as-isolated DB structure resulting in a binding energy of $-2.1$ eV. In this work, we observed a further relaxation of this defect structure. The C atom of the second and the Si atom of the initial DB move toward each other forming a bond, which results in a somewhat lower binding energy of $-2.25$ eV. The structure is displayed in the bottom right of Fig. 6. Apart from that, we found a more favorable configuration for the combination with a [0 $\overline{1}$ 0] and [$\overline{1}$ 0 0] DB respectively, which is assumed to constitute the actual ground-state configuration of two $C_i$ DBs in Si. The atomic arrangement is shown in the bottom right of Fig. 5. The two $C_i$ atoms form a strong C–C bond, which is responsible for the large gain in energy resulting in a binding energy of $-2.39$ eV.

Investigating migration barriers allows to predict the probability of formation of defect complexes by thermally activated diffusion processes. Based on the lowest energy migration path of a single $C_i$ DB, the configuration, in which the second $C_i$ DB is oriented along [0 1 0] at position 2, is assumed to constitute an ideal starting point for a transition into the ground state. In addition, the starting configuration exhibits a low binding energy ($-1.90$ eV) and is thus, very likely to occur. However, a barrier height of more than 4 eV was detected resulting in a low probability for the transition. The high activation energy is attributed to the stability of such a low energy configuration, in which the C atom of the second DB is located close to the initial DB. Low barriers have only been identified for transitions starting from energetically less favorable configurations, e.g., the configuration of a [$\overline{1}$ 0 0] DB located at position 2 ($-0.36$ eV). Starting from this configuration, an activation energy of only 1.2 eV is necessary for the transition into the ground-state configuration. The corresponding migration energies and atomic configurations are displayed in Fig. 5. Because thermally activated C clustering is thus only possible by traversing energetically unfavored configurations, extensive C clustering is not expected. Furthermore, the migration barrier of 1.2 eV is still higher than the activation energy of 0.9 eV observed for a single $C_i$ $\langle 100 \rangle$ DB in c-Si. The migration barrier of a $C_i$ DB in a complex system is assumed to approximate the barrier of a DB in a separated system with increasing defect separation. Accordingly, lower migration barriers are expected for pathways resulting in larger separations of the $C_i$ DBs. However, if the increase of separation is accompanied by an increase in binding energy, this difference is needed in addition to the activation energy for the respective migration process. Configurations, which exhibit both, a low binding energy as well as afferent transitions with low activation energies are thus, most probable $C_i$ complex structures. However, if elevated temperatures enable migrations with huge activation energies, comparably small differences in configurational energy can be neglected resulting in an almost equal occupation of such configurations. In both cases, the configuration yielding a binding energy of $-2.25$ eV is promising. First of all, it constitutes the second most energetically favorable structure. Secondly, a migration path with a barrier as low as 0.47 eV exists starting from a configuration of largely separated defects exhibiting a low binding energy ($-1.88$ eV). The migration barrier and corresponding structures are shown in Fig. 6. Finally, this type of defect pair is represented four times (two times more often than the ground-state configuration) within the systematically investigated configuration space. The latter is considered very important at high temperatures, accompanied by an increase in the entropic contribution to structure formation. As a result, C defect agglomeration indeed is expected, but only a low probability is assumed for C–C clustering by thermally activated processes with regard to the considered process time in IBS.

![](./images/811624034138587137_5.jpg)

FIG. 5. (Color online) Migration barrier and structures of the transition of a $C_i$ [$\overline{1}$ 0 0] DB at position 2 (left) into a $C_i$ [0 $\overline{1}$ 0] DB at position 1 (right). An activation energy of 1.2 eV is observed.

![](./images/811624034138587137_6.jpg)

FIG. 6. (Color online) Migration barrier and structures of the transition of a $C_i$ [0 $\bar{1}$ 0] DB at position 5 (left) into a $C_i$ [1 0 0] DB at position 1 (right). An activation energy of 0.47 eV is observed.

The binding energies of the energetically most favorable configurations with the second DB located along the [1 1 0] direction and resulting C-C distances of the relaxed structures are summarized in Table III. The binding energy of these configurations with respect to the C-C distance is plotted in Fig. 7. The interaction is found to be proportional to the reciprocal cube of the C-C distance for extended separations of the $C_i$ and saturates for the smallest possible separation, i.e., the ground-state configuration. Not considering the previously mentioned elevated barriers for migration, an attractive interaction between the $C_i$ defects indeed is detected with a capture radius that clearly exceeds 1 nm. The interpolated graph suggests the disappearance of attractive interaction forces, which are proportional to the slope of the graph, between the two lowest separation distances of the defects. This finding, in turn, supports the previously established assumption of C agglomeration and absence of C clustering.

### B. $C_i$ next to $C_s$

The first row of Table IV lists the binding energies of $C_s$ next to the $C_i$ [0 0 $\bar{1}$] DB. For $C_s$ located at position 1 and 3 the configurations a and A correspond to the naive relaxation of the structure by substituting the Si atom by a C atom in the initial $C_i$ [0 0 $\bar{1}$] DB structure at positions 1 and 3 respectively. However, small displacements of the involved atoms near the defect result in different stable structures labeled b and B respectively. Figures 8 and 9 show structures A, B and a, b together with the barrier of migration for the A to B and a to b transition respectively.

TABLE III. Binding energies $E_b$ and C-C distance of energetically most favorable $C_i$ $\langle 100 \rangle$-type defect pairs separated along the [1 1 0] bond chain.

<table>
  <thead>
    <tr>
      <th></th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$E_b$ eV</td>
      <td>$-2.39$</td>
      <td>$-1.88$</td>
      <td>$-0.59$</td>
      <td>$-0.31$</td>
      <td>$-0.24$</td>
      <td>$-0.21$</td>
    </tr>
    <tr>
      <td>C-C distance [nm]</td>
      <td>0.14</td>
      <td>0.46</td>
      <td>0.65</td>
      <td>0.86</td>
      <td>1.05</td>
      <td>1.08</td>
    </tr>
  </tbody>
</table>

![](./images/811624034138587137_7.jpg)

FIG. 7. (Color online) Minimum binding energy of dumbbell combinations separated along [1 1 0] with respect to the C-C distance. The blue line is a guide for the eye and the green curve corresponds to the most suitable fit function consisting of all but the first data point.

Configuration A consists of a $C_i$ [0 0 -1] DB with three fold coordinated Si and C DB atoms slightly disturbed by the $C_s$ at position 3 facing the Si DB atom as a neighbor. By a single bond switch, i.e., the breaking of a Si-Si in favor of a Si-C bond, configuration B is obtained, which shows a two fold coordinated Si atom located between two substitutional C atoms residing on regular Si lattice sites. This configuration has been identified and described by spectroscopic experimental techniques$^{89}$ as well as theoretical studies.$^{47,48}$ Configuration B is found to constitute the energetically slightly more favorable configuration. However, the gain in energy due to the significantly lower energy of a Si-C compared to a Si-Si bond turns out to be smaller than expected because of a large compensation by introduced strain as a result of the Si interstitial structure. Present results show a difference in energy of states A and B, which exactly matches the experimental value of $0.02$ eV$^{89}$ reinforcing qualitatively correct results of previous theoretical studies on these structures. The migration barrier was identified to be 0.44 eV, almost three times higher than the experimental value of 0.16 eV Ref. 89 estimated for the neutral charge state transition in p- and n-type Si. Keeping in mind the formidable agreement of the energy difference with experiment, the overestimated activation energy is quite unexpected. Obviously, either the CRT algorithm fails to seize the actual saddle point structure or the influence of dopants

TABLE IV. Binding energies of combinations of the $C_i$ [0 0 $\bar{1}$] defect with a substitutional C or vacancy located at positions 1 to 5 according to Fig. 4(a). R corresponds to the position located at $\frac{a_{Si}}{2}$ [3 2 3] relative to the initial defect position, which is the maximum realizable distance due to periodic boundary conditions.

<table>
  <thead>
    <tr>
      <th></th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>R</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$C_s$</td>
      <td>$0.26^a/-1.28^b$</td>
      <td>$-0.51$</td>
      <td>$-0.93^A/-0.95^B$</td>
      <td>$-0.15$</td>
      <td>$0.49$</td>
      <td>$-0.05$</td>
    </tr>
    <tr>
      <td>V</td>
      <td>$-5.39$ ($\rightarrow C_S$)</td>
      <td>$-0.59$</td>
      <td>$-3.14$</td>
      <td>$-0.54$</td>
      <td>$-0.50$</td>
      <td>$-0.31$</td>
    </tr>
  </tbody>
</table>

![](./images/811624034138587137_8.jpg)

FIG. 8. (Color online) Migration barrier and structures of the transition of the initial $C_i$ [0 0 $\bar{1}$] DB and $C_s$ at position 3 (left) into a configuration of a two-fold coordinated $Si_i$ located between two $C_s$ atoms occupying the lattice sites of the initial DB and position 3 (right). An activation energy of 0.44 eV is observed.

has exceptional effect in the experimentally covered diffusion process being responsible for the low migration barrier.

Configuration a is similar to configuration A, except that the $C_s$ atom at position 1 is facing the C DB atom as a neighbor resulting in the formation of a strong C–C bond and a much more noticeable perturbation of the DB structure. Neverthe- less, the C and Si DB atoms remain threefold coordinated. Although the C–C bond exhibiting a distance of 0.15 nm close to the distance expected in diamond or graphite should lead to a huge gain in energy, a repulsive interaction with a binding energy of 0.26 eV is observed due to compressive strain of the Si DB atom and its top neighbors (0.230 nm/0.236 nm) along with additional tensile strain of the $C_s$ and its three neighboring Si atoms (0.198–0.209 nm/0.189 nm). Again a single bond switch, i.e., the breaking of the bond of the Si atom bound to the fourfold coordinated $C_s$ atom and the formation of a double bond between the two C atoms, results in configuration b. The two C atoms form a [1 0 0] DB sharing the initial $C_s$ lattice site while the initial Si DB atom occupies its previously regular lattice site. The transition is accompanied by a large gain in energy as can be seen in Fig. 9 making it the ground-state configuration of a $C_s$ and $C_i$ DB in Si yet 0.33 eV lower in energy than configuration B. This finding is in good agreement with a combined $ab$ $initio$ and experimental study of Liu $et$ $al$.,$^{90}$ who first proposed this structure as the ground state identifying an energy difference compared to configuration B of 0.2 eV. A net magnetization of two spin up electrons, which are equally localized as in the $Si_i$ $\langle$1 0 0$\rangle$ DB structure is observed. In fact, these two configurations are very similar and are qualitatively different from the $C_i$ $\langle$1 0 0$\rangle$ DB that does not show magnetization but a nearly collinear bond of the C DB atom to its two neighbored Si atoms while the Si DB atom approximates $120^\circ$ angles in between its bonds. Configurations a, A and B are not affected by spin polarization and show zero magnetization. Mattoni $et$ $al$.,$^{50}$ in contrast, find configuration b less favorable than configuration A by 0.2 eV. Next to differences in the XC functional and plane-wave energy cut-off, this discrepancy might be attributed to the neglect of spin polarization in their calculations, which, as has been shown for the $C_i$ BC configuration, results in an increase of configurational energy. Indeed, investigating the migration path from configurations a to b and, in doing so, reusing the wave functions of the previous migration step, the final structure, i.e., configuration b, was obtained with zero magnetization and an increase in configurational energy by 0.2 eV. Obviously, a different energy minimum of the electronic system is obtained indicating hysteresis behavior. However, because the total energy is lower for the magnetic result it is believed to constitute the real, i.e., global, minimum with respect to electronic minimization. A low activation energy of 0.1 eV is observed for the a$\rightarrow$b transition. Thus, configuration a is very unlikely to occur in favor of configuration b.

![](./images/811624034138587137_9.jpg)

FIG. 9. (Color online) Migration barrier and structures of the transition of the initial $C_i$ [0 0 $\bar{1}$] DB and $C_s$ at position 1 (left) into a C–C [1 0 0] DB occupying the lattice site at position 1 (right). An activation energy of 0.1 eV is observed.

A repulsive interaction is observed for $C_s$ at lattice sites along [1 1 0], i.e., positions 1 (configuration a) and 5. This is due to tensile strain originating from both, the $C_i$ DB and the $C_s$ atom residing within the [1 1 0] bond chain. This finding agrees well with results by Mattoni $et$ $al$.$^{50}$ In contrast, all other investigated configurations show attractive interactions. The most favorable configuration is found for $C_s$ at position 3, which corresponds to the lattice site of one of the upper neighbored Si atoms of the DB structure that is compressively strained along [1 $\bar{1}$ 0] and [0 0 1] by the C–Si DB. The substitution with C allows for most effective compensation of strain. This structure is followed by $C_s$ located at position 2, the lattice site of one of the neighbor atoms below the two Si atoms that are bound to the $C_i$ DB atom. As mentioned earlier, these two lower Si atoms indeed experience tensile strain along the [1 1 0] bond chain. However, additional compressive strain along [0 0 1] exists. The latter is partially compensated by the $C_s$ atom. Yet less of compensation is realized if $C_s$ is located at position 4 due to a larger separation although both bottom Si atoms of the DB structure are indirectly affected, i.e., each of

them is connected by another Si atom to the C atom enabling the reduction of strain along [0 0 1].

Obviously, agglomeration of $C_i$ and $C_s$ is energetically favorable except for separations along one of the $\langle 110 \rangle$ directions. The energetically most favorable configuration (configuration b) forms a strong but compressively strained C–C bond with a separation distance of 0.142nm sharing a Si lattice site. Again, conclusions concerning the probability of formation are drawn by investigating migration paths. Because $C_s$ is unlikely to exhibit a low activation energy for migration the focus is on $C_i$. Pathways starting from the two next most favored configurations were investigated, which show activation energies above 2.2 eV and 3.5 eV respectively. Although lower than the barriers for obtaining the ground state of two $C_i$ defects, the activation energies are yet considered too high. For the same reasons as in the last subsection, structures other than the ground-state configuration are thus assumed to arise more likely due to much lower activation energies necessary for their formation and still comparatively low binding energies.

### C. $C_i$ next to V
Binding energies of a $C_i$ DB and a nearby vacancy are listed in the second row of Table IV. All investigated structures are preferred compared to isolated, largely separated defects. In contrast to $C_s$, this is also valid for positions along [1 1 0] resulting in an entirely attractive interaction between defects of these types. Even for the largest possible distance (R) achieved in the calculations of the periodic supercell, a binding energy as low as $-0.31$ eV is observed. The ground-state configuration is obtained for a V at position 1. The C atom of the DB moves toward the vacant site forming a stable $C_s$ configuration resulting in the release of a huge amount of energy. The second most favorable configuration is accomplished for a V located at position 3 due to the reduction of compressive strain of the Si DB atom and its two upper Si neighbors present in the $C_i$ DB configuration. This configuration is followed by the structure, in which a vacant site is created at position 2. Similar to the observations for $C_s$ in the last subsection, a reduction of strain along [0 0 1] is enabled by this configuration. Relaxed structures of the latter two defect combinations are shown in the bottom left of Figs. 10 and 11 respectively together with their energetics during transition into the ground state. Activation energies as low as 0.1 eV and 0.6 eV are observed. In the first case, the Si and C atom of the DB move toward the vacant and initial DB lattice site respectively. In total, three Si–Si and one more Si–C bond is formed during transition. In the second case, the lowest barrier is found for the migration of Si number 1, which is substituted by the $C_i$ atom, toward the vacant site. A net amount of five Si–Si and one Si–C bond are additionally formed during transition. The direct migration of the $C_i$ atom onto the vacant lattice site results in a somewhat higher barrier of 1.0 eV. In both cases, the formation of additional bonds is responsible for the vast gain in energy rendering almost impossible the reverse processes.

In summary, pairs of $C_i$ DBs and Vs, like no other before, show highly attractive interactions for all investigated combinations independent of orientation and separation direction of the defects. Furthermore, small activation energies, even for transitions into the ground state, exist. Based on these results, a high probability for the formation of $C_s$ must be concluded.

![](./images/811624034138587137_10.jpg)

FIG. 10. (Color online) Migration barrier and structures of the transition of the initial $C_i$ [0 0 $\bar{1}$] DB and a V created at position 3 (left) into a $C_s$ configuration (right). An activation energy of 0.1 eV is observed.

### D. $C_s$ next to $Si_i$
As shown in Sec. III A, $C_s$ exhibits the lowest energy of formation. Considering a perfect Si crystal and conservation of particles, however, the occupation of a Si lattice site by a slowed down implanted C atom is necessarily accompanied by the formation of a Si self-interstitial. The $Si_i$ $\langle 110 \rangle$ DB, which was found to exhibit the lowest energy of formation within the investigated self-interstitial configurations, is assumed to provide the energetically most favorable configuration in combination with $C_s$.

![](./images/811624034138587137_11.jpg)

FIG. 11. (Color online) Migration barrier and structures of the transition of the initial $C_i$ [0 0 $\bar{1}$] DB and a V created at position 2 (left) into a $C_s$ configuration (right). An activation energy of 0.6 eV is observed.


TABLE V. Equivalent configurations labeled I-X of $\langle 110 \rangle$-type Si$_i$ DBs created at position I and C$_s$ created at positions 1 to 5 according to Fig. 4(b). The respective orientation of the Si$_i$ DB is given in the first row.

|     | $\left[ 1\ 1\ 0 \right]$ | $\left[ \bar{1}\ 1\ 0 \right]$ | $\left[ 0\ 1\ 1 \right]$ | $\left[ 0\ \bar{1}\ 1 \right]$ | $\left[ 1\ 0\ 1 \right]$ | $\left[ \bar{1}\ 0\ 1 \right]$ |
|-----|---------------------------|---------------------------------|---------------------------|---------------------------------|---------------------------|---------------------------------|
| 1   | I                         | III                             | III                       | I                               | III                       | I                               |
| 2   | II                        | VI                              | VI                        | II                              | VIII                      | V                               |
| 3   | III                       | I                               | III                       | I                               | I                         | III                             |
| 4   | IV                        | VII                             | IX                        | X                               | X                         | IX                              |
| 5   | V                         | VIII                            | VI                        | II                              | VI                        | II                              |

Table V classifies equivalent configurations of $\langle 110 \rangle$-type Si$_i$ DBs created at position I and C$_s$ created at positions 1 to 5 according to Fig. 4(b). Corresponding formation as well as binding energies and the separation distances of the C$_s$ atom and the Si$_i$ DB lattice site are listed in Table VI. In total, ten different configurations exist within the investigated range. Configuration 1 constitutes the energetically most favorable structure exhibiting a formation energy of 4.37 eV. Obviously, the configuration of a Si$_i$ $\left[ 1\ 1\ 0 \right]$ DB and a neighbored C$_s$ atom along the bond chain, which has the same direction as the alignment of the DB, enables the largest possible reduction of strain. The relaxed structure is displayed in the bottom right of Fig. 12. Compressive strain originating from the Si$_i$ is compensated by tensile strain inherent to the C$_s$ configuration. The Si$_i$ DB atoms are displaced toward the lattice site occupied by the C$_s$ atom in such a way that the Si$_i$ DB atom closest to the C atom does no longer form bonds to its top Si neighbors, but to the next neighbored Si atom along $\left[ 1\ 1\ 0 \right]$.

However, the configuration is energetically less favorable than the $\langle 100 \rangle$ C$_i$ DB, which thus remains the ground state of a C atom introduced into otherwise perfect c-Si. The transition involving the latter two configurations is shown in Fig. 12. An activation energy as low as 0.12 eV is necessary for the migration into the ground-state configuration. Accordingly, the C$_i$ $\langle 100 \rangle$ DB configuration is assumed to occur more likely. However, only 0.77 eV are needed for the reverse process, i.e., the formation of C$_s$ and a Si$_i$ DB out of the ground state. Due to the low activation energy, this process must be considered to be activated without much effort either thermally or by introduced energy of the implantation process.

Figure 13 shows the binding energies of pairs of C$_s$ and a Si$_i$ $\langle 110 \rangle$ DB with respect to the separation distance. As can be seen, the interaction strength, i.e., the absolute value of the binding energy, quickly drops to zero with increasing separation distance. Almost zero interaction may be assumed already at distances about $0.5-0.6$ nm, indicating a low interaction capture radius of the defect pair. In IBS, highly energetic collisions are assumed to easily produce configurations of defects exhibiting separation distances exceeding the capture radius. For this reason, C$_s$ without a Si$_i$ DB located within the immediate proximity, which is thus unable to form the thermodynamically stable C$_i$ $\langle 100 \rangle$ DB, constitutes a most likely configuration to be found in IBS.

Similar to what was previously mentioned, configurations of C$_s$ and a Si$_i$ DB might be particularly important at higher temperatures due to the low activation energy necessary for its formation. At higher temperatures the contribution of entropy to structural formation increases, which might result in a spatial separation even for defects located within the capture radius. Indeed, an $ab$ $initio$ molecular dynamics run at $900\,^{\circ}\text{C}$ starting from configuration 1, which, based on the above findings, is assumed to recombine into the ground-state configuration, results in a separation of the C$_s$ and Si$_i$ DB by more than 4 neighbor distances realized in a repeated migration mechanism of annihilating and arising Si$_i$ DBs. The atomic configurations for two different points in time are shown in Fig. 14. Si atoms 1 and 2, which form the initial DB, occupy Si lattice sites in the final configuration whereas Si atom 3 is transferred from a regular lattice site into the interstitial lattice.

![](./images/811624034138587137_12.jpg)

FIG. 12. (Color online) Migration barrier and structures of the transition of a $\left[ 1\ 1\ 0 \right]$ Si$_i$ DB next to C$_s$ (right) into the C$_i$ $\left[ 0\ 0\ \bar{1} \right]$ DB configuration (left). An activation energy of 0.12 eV and 0.77 eV for the reverse process is observed.

### E. Mobility of silicon defects

Separated configurations of C$_s$ and Si$_i$ become even more likely if Si diffusion exhibits a low barrier of migration.

TABLE VI. Formation energies $E_{\text{f}}$, binding energies $E_{\text{b}}$, and C$_s$-Si$_i$ separation distances of configurations combining C$_s$ and Si$_i$ as defined in Table V.

|     | I     | II    | II    | IV    | V     | VI    | VII   | VIII  | IX    | X     |
|-----|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| $E_{\text{f}}$ [eV] | 4.37  | 5.26  | 5.57  | 5.37  | 5.12  | 5.10  | 5.32  | 5.28  | 5.39  | 5.32  |
| $E_{\text{b}}$ [eV] | $-0.97$ | $-0.08$ | 0.22  | $-0.02$ | $-0.23$ | $-0.25$ | $-0.02$ | $-0.06$ | 0.05  | $-0.03$ |
| $r$ [nm] | 0.292 | 0.394 | 0.241 | 0.453 | 0.407 | 0.408 | 0.452 | 0.392 | 0.456 | 0.453 |

![](./images/811624034138587137_13.jpg)

FIG. 13. (Color online) Binding energies of combinations of a $C_s$ and a $Si_i$ DB with respect to the separation distance.

Concerning the mobility of the ground-state $Si_i$, an activation energy of 0.67 eV for the transition of the $Si_i$ [0 1 $\bar{1}$] to [1 1 0] DB located at the neighbored Si lattice site in [1 1 $\bar{1}$] direction is obtained by first-principles calculations. Further quantum-mechanical investigations revealed a barrier of 0.94 eV for the $Si_i$ [1 1 0] DB to $Si_i$ H, 0.53 eV for the $Si_i$ [1 1 0] DB to $Si_i$ T and 0.35 eV for the $Si_i$ H to $Si_i$ T transition. These are of the same order of magnitude than values derived from other $ab$ $initio$ studies. $^{31,38}$ The low barriers indeed enable configurations of further separated $C_s$ and $Si_i$ atoms by the highly mobile $Si_i$ atom departing from the $C_s$ defect as observed in the previously discussed MD simulation.

## F. Summary
Obtained results for separated point defects in Si are in good agreement to previous theoretical work on this subject, both for intrinsic defects $^{33,36}$ as well as for C point defects. $^{44,45}$ The ground-state configurations of these defects, i.e., the $Si_i$ $\langle 110\rangle$ and $C_i$ $\langle 100\rangle$ DB, have been reproduced and compare well to previous findings of theoretical investigations on $Si_i$ (Refs. 33 and 36) as well as theoretical $^{44-47,52}$ and experimental $^{84}$ (Ref. 85) studies on $C_i$. A quantitatively improved activation energy of 0.9 eV for a qualitatively equal migration path based on studies by Capaz $et$ $al.^{45}$ to experimental values $^{85,87,88}$ ranging from 0.70-0.87 eV reinforce their derived mechanism of diffusion for $C_i$ in Si.

The investigation of defect pairs indicated a general trend of defect agglomeration mainly driven by the potential of strain reduction. Obtained results for the most part compare well with results gained in previous studies $^{47,48,50,90}$ and show an astonishingly good agreement with experiment (Ref. 85). For configurations involving two C impurities, the ground-state configurations have been found to consist of C-C bonds, which are responsible for the vast gain in energy. However, based on investigations of possible migration pathways, these structures are less likely to arise than structures, in which both C atoms are interconnected by another Si atom, which is due to high activation energies of the respective pathways or alternative pathways featuring less high activation energies, however, that involve intermediate unfavorable configurations. Thus, agglomeration of $C_i$ is expected whereas the formation of C-C bonds is assumed to fail to appear by thermally activated diffusion processes.

In contrast, $C_i$ and Vs were found to efficiently react with each other exhibiting activation energies as low as 0.1 eV and 0.6 eV resulting in stable $C_s$ configurations. In addition, we observed a highly attractive interaction exhibiting a large capture radius, effective independent of the orientation and the direction of separation of the defects. Accordingly, the formation of $C_s$ is very likely to occur. Comparatively high energies necessary for the reverse process reveal this configuration to be extremely stable.

Investigating configurations of $C_s$ and $Si_i$, formation energies higher than that of the $C_i$ $\langle 100\rangle$ DB were obtained keeping previously derived assumptions concerning the ground state of $C_i$ in otherwise perfect Si. However, a small capture radius was identified for the respective interaction that might prevent the recombination of defects exceeding a separation of 0.6 nm into the ground-state configuration. In addition, a rather small activation energy of 0.77 eV allows for the formation of a $C_s$-$Si_i$ pair originating from the $C_i$ $\langle 100\rangle$ DB structure by thermally activated processes. Thus, elevated temperatures might lead to configurations of $C_s$ and a remaining Si atom in the near interstitial lattice, which is supported by the result of the molecular dynamics run.

## V. EXCURSUS: COMPETITION OF $C_i$ AND $C_s$-$SI_i$
As has been shown in Sec. IV D, the energetically most favorable configuration of $C_s$ and $Si_i$ is obtained for $C_s$ located at the neighbored lattice site along the $\langle 110\rangle$ bond chain of a $Si_i$ $\langle 110\rangle$ DB. However, the energy of formation is slightly higher than that of the $C_i$ $\langle 100\rangle$ DB, which constitutes the ground state for a C impurity introduced into otherwise perfect c-Si.

For a possible clarification of the controversial views on the participation of $C_s$ in the precipitation mechanism by classical potential simulations, test calculations need to ensure the proper description of the relative formation energies of combined structures of $C_s$ and $Si_i$ compared to $C_i$. This is particularly important because the energy of formation of $C_s$ is drastically underestimated by the EA potential. A possible occurrence of $C_s$ could then be attributed to a lower energy of formation of the $C_s$-$Si_i$ combination due to the low formation energy of $C_s$, which is obviously wrong.

![](./images/811624034138587137_14.jpg)

FIG. 14. (Color online) Atomic configurations of an $ab$ $initio$ molecular dynamics run at $900\,^{\circ}\text{C}$ starting from a configuration of $C_s$ located next to a $Si_i$ [1 1 0] DB (atoms 1 and 2). Equal atoms are marked by equal numbers.

TABLE VII. Formation energies of defect configurations of a single C impurity in otherwise perfect c-Si determined by classical potential and ab initio methods. The formation energies are given in electron volts. T denotes the tetrahedral and the subscripts i and s indicate the interstitial and substitutional configuration. Superscripts a, b, and c denote configurations of $C_{s}$ located at the first, second, and third nearest-neighbored lattice site with respect to the $Si_{i}$ atom.

|              | $C_{i}\langle 100\rangle$ | $C_{s}$ & $Si_{i}\langle 110\rangle$ | $C_{s}$ & $Si_{i}$ T |
|--------------|---------------------------|--------------------------------------|----------------------|
| VASP         | 3.72                      | 4.37                                 | $4.17^{a}/4.99^{b}/4.96^{c}$ |
| Erhart/Albe  | 3.88                      | 4.93                                 | $5.25^{a}/5.08^{b}/4.43^{c}$ |

Because quantum-mechanical calculations reveal the $Si_{i}$ $\langle 110\rangle$ DB as the ground-state configuration of $Si_{i}$ in Si, it is assumed to provide the energetically most favorable configuration in combination with $C_{s}$. Empirical potentials, however, predict $Si_{i}$ T to be the energetically most favorable configuration. Thus, investigations of the relative energies of formation of defect pairs need to include combinations of $C_{s}$ with $Si_{i}$ T. Results of VASP and EA calculations are summarized in Table VII. Obviously, the EA potential properly describes the relative energies of formation. Combined structures of $C_{s}$ and $Si_{i}$ T are energetically less favorable than the ground-state $C_{i}\langle 100\rangle$ DB configuration. With increasing separation distance, the energies of formation decrease. However, even for noninteracting defects, the energy of formation, which is then given by the sum of the formation energies of the separated defects (4.15 eV) is still higher than that of the $C_{i}\langle 100\rangle$ DB. Unexpectedly, the structure of a $Si_{i}$ $\langle 110\rangle$ DB and a neighbored $C_{s}$, which is the most favored configuration of a $C_{s}$ and $Si_{i}$ DB according to the quantum-mechanical calculations, likewise constitutes an energetically favorable configuration within the EA description, which is even preferred over the two least separated configurations of $C_{s}$ and $Si_{i}$ T. This is attributed to an effective reduction in strain enabled by the respective combination. Quantum-mechanical results reveal a more favorable energy of fomation for the $C_{s}$ and $Si_{i}$ T (a) configuration. However, this configuration is unstable involving a structural transition into the $C_{i}\langle 110\rangle$ interstitial, thus, not maintaining the tetrahedral Si nor the substitutional C defect.

Thus, the underestimated energy of formation of $C_{s}$ within the EA calculation does not pose a serious limitation in the present context. Because C is introduced into a perfect Si crystal and the number of particles is conserved in simulation, the creation of $C_{s}$ is accompanied by the creation of $Si_{i}$, which is energetically less favorable than the ground state, i.e., the $C_{i}\langle 100\rangle$ DB configuration, for both, the EA and ab initio treatment. In either case, no configuration more favorable than the $C_{i}\langle 100\rangle$ DB has been found. Thus, a proper description with respect to the relative energies of formation is assumed for the EA potential.

## VI. CLASSICAL POTENTIAL CALCULATIONS ON THE SIC PRECIPITATION IN SI

The MD technique is used to gain insight into the behavior of C existing in different concentrations in c-Si on the microscopic level at finite temperatures. In a first step, simulations are performed, which try to mimic the conditions during IBS. Results reveal limitations of the employed potential and MD in general. With reference to the results of the last section, a workaround is discussed. The approach is follwed and, finally, results gained by the MD simulations are interpreted drawing special attention to the established controversy concerning precipitation of SiC in Si.

### A. Molecular dynamics simulations

Figure 15 shows the radial distribution functions of simulations, in which C was inserted at $450\ ^{\circ}\text{C}$, an operative and efficient temperature in IBS, $^{14}$ for all three insertion volumes.

There is no significant difference between C insertion into $V_{2}$ and $V_{3}$. Thus, in the following, the focus is on low $(V_{1})$ and high $(V_{2},V_{3})$ C concentration simulations only.

In the low C concentration simulation the number of C$-$C bonds is small, as can be seen in the upper part of

![](./images/811624034138587137_15.jpg)

FIG. 15. (Color online) Radial distribution function for C$-$C and Si$-$Si [Fig. 15(a)] as well as Si$-$C [Fig. 15(b)] pairs for C inserted at $450\ ^{\circ}\text{C}$. In the latter case the resulting C$-$Si distances for a $C_{i}\langle 100\rangle$ DB are given additionally and the Si$-$C cut-off distance is marked by an arrow. Insets in Fig. 15(a) show magnified regions of the respective distribution functions.

Fig. 15(a). On average, there are only 0.2 C atoms per Si unit cell. By comparing the Si-C peaks of the low concentration simulation with the resulting Si-C distances of a $C_i$ $\langle 100 \rangle$ DB in Fig. 15(b), it becomes evident that the structure is clearly dominated by this kind of defect. One exceptional peak at 0.26 nm [marked with an arrow in Fig. 15(b)] exists, which is due to the Si-C cut-off, at which the interaction is pushed to zero. Investigating the C-C peak at 0.31 nm, which is also available for low C concentrations as can be seen in the upper inset of Fig. 15(a), reveals a structure of two concatenated, differently oriented $C_i$ $\langle 100 \rangle$ DBs to be responsible for this distance. In addition, in the inset of the bottom part of Fig. 15(a) the Si-Si radial distribution shows non-zero values at distances around 0.3 nm, which again is due to the DB structure stretching two neighbored Si atoms. This is accompanied by a reduction of the number of bonds at regular Si distances of c-Si. A more detailed description of the resulting C-Si distances in the $C_i$ $\langle 100 \rangle$ DB configuration and the influence of the defect on the structure is available in a previous study. $^{86}$

For high C concentrations, the defect concentration is likewise increased and a considerable amount of damage is introduced in the insertion volume. A subsequent superpo- sition of defects generates new displacement arrangements for the C-C as well as Si-C pair distances, which become hard to categorize and trace and obviously lead to a broader distribution. Shortrange order indeed is observed, i.e., the large amount of strong neighbored C-C bonds at 0.15 nm as expected in graphite or diamond and Si-C bonds at 0.19 nm as expected in SiC, but hardly visible is the long-range order. This indicates the formation of an amorphous SiC-like phase. In fact, resulting Si-C and C-C radial distribution functions compare quite well with these obtained by cascade amorphized and melt-quenched amorphous SiC using a modified Tersoff potential. $^{72}$

In both cases, i.e., low and high C concentrations, the formation of 3C-SiC fails to appear. With respect to the precipitation model, the formation of $C_i$ $\langle 100 \rangle$ DBs indeed occurs for low C concentrations. However, sufficient defect agglomeration is not observed. For high C concentrations, a rearrangement of the amorphous SiC structure, which is not expected at prevailing temperatures, and a transition into 3C-SiC is not observed either. On closer inspection two reasons for describing this obstacle become evident.

First of all, there is the time scale problem inherent to MD in general. To minimize the integration error, the discretized time step must be chosen smaller than the reciprocal of the fastest vibrational mode resulting in a time step of 1 fs for the investigated materials system. Limitations in computer power result in a slow propagation in phase space. Several local minima exist, which are separated by large energy barriers. Due to the low probability of escaping such a local minimum, a single transition event corresponds to a multiple of vibrational periods. Long-term evolution, such as a phase transformation and defect diffusion, in turn, are made up of a multiple of these infrequent transition events. Thus, time scales to observe long-term evolution are not accessible by traditional MD. New accelerated methods have been developed to bypass the time scale problem retaining proper thermodynamic sampling. $^{91-95}$

However, the applied potential comes up with an additional limitation, as previously mentioned in the introduction. The cut-off function of the short-range potential limits the interac- tion to nearest neighbors. Since the total binding energy is thus accommodated within this short distance, which according to the universal energy relation would usually correspond to a much larger distance, unphysical high forces between two neighbored atoms arise. Although cohesive and formational energies are often well described, these effects increase for non-equilibrium structures and dynamics. This behavior, as observed and discussed for the Tersoff potential, $^{74,96}$ is supported by the overestimated activation energies necessary for C diffusion as investigated in Sec. III B. Indeed, it is not only the strong, hard to break C-C bond inhibiting C diffusion and further rearrangements in the case of the high C concentration simulations. This is also true for the low concentration simulations dominated by the occurrence of $C_i$ $\langle 100 \rangle$ DBs spread over the whole simulation volume, which are unable to agglomerate due to the high migration barrier.

### B. Increased temperature simulations

Due to the problem of slow phase space propagation, which is enhanced by the employed potential, pushing the time scale to the limits of computational resources or applying one of the above mentioned accelerated dynamics methods exclusively, might not be sufficient. Instead, higher temperatures are utilized to compensate overestimated diffusion barriers. These are overestimated by a factor of 2.4 to 3.5. Scaling the absolute temperatures accordingly results in maximum temperatures of $1460$-$2260\,^\circ\text{C}$. Because melting already occurs shortly below the melting point of the potential $(2450\ \text{K})^{73}$ due to the presence of defects, a maximum temperature of $2050\,^\circ\text{C}$ is used.

Figure 16 shows the resulting radial distribution functions for various temperatures. In Fig. 16(a), the first noticeable and promising change observed for the Si-C bonds is the successive decline of the artificial peak at the cut-off distance with increasing temperature. Obviously, sufficient kinetic energy is provided to affected atoms that are enabled to escape the cut-off region. In addition, a more important structural change was observed, which is illustrated in the two shaded areas in Fig. 16(a). Obviously, the structure obtained at $450\,^\circ\text{C}$, which was found to be dominated by $C_i$, transforms into a $C_s$ dominated structure with increasing temperature. Comparing the radial distribution at $2050\,^\circ\text{C}$ to the resulting bonds of $C_s$ in c-Si excludes all possibility of doubt.

The phase transformation is accompanied by an arising Si-Si peak at 0.325 nm in Fig. 16(b), which corresponds to the distance of next neighbored Si atoms along the $\langle 110 \rangle$ bond chain with $C_s$ in between. Because the expected distance of these Si pairs in 3C-SiC is 0.308 nm, the existing SiC structures embedded in the c-Si host are stretched.

According to the C-C radial distribution displayed in Fig. 16(c), agglomeration of C fails to appear even for elevated temperatures, as can be seen on the total amount of C pairs within the investigated separation range, which does not change significantly. However, a small decrease in the amount of neighbored C pairs can be observed with increasing temperature. This high temperature behavior is promising

![](./images/811624034138587137_16.jpg)

FIG. 16. (Color online) Radial distribution function for Si-C [Fig. 16(a)], Si-Si [Fig. 16(b)] and C-C [Fig. 16(c)] pairs for the C insertion into $V_{1}$ at elevated temperatures. For the Si-C distribution resulting Si-C distances of a $C_{s}$ configuration are plotted. In the C-C distribution dashed arrows mark C-C distances occurring from $C_{i}$ $\langle 100\rangle$ DB combinations, solid arrows mark C-C distances of pure $C_{s}$ combinations and the dashed line marks C-C distances of a $C_{i}$ and $C_{s}$ combination.

because the breaking of these diamond- and graphite-like bonds is mandatory for the formation of 3C-SiC. Obviously, acceleration of the dynamics occurred by supplying additional kinetic energy. A slight shift toward higher distances can be observed for the maximum located shortly above 0.3 nm. Arrows with dashed lines mark C-C distances resulting from $C_{i}$ $\langle 100\rangle$ DB combinations whereas arrows with solid lines mark distances arising from combinations of $C_{s}$. The continuous dashed line corresponds to the distance of $C_{s}$ and a neighbored $C_{i}$ DB. Obviously, the shift of the peak is caused by the advancing transformation of the $C_{i}$ DB into the $C_{s}$ defect. Quite high g(r) values are obtained for distances in between the continuous dashed line and the first arrow with a solid line. For the most part, these structures can be identified as configurations of $C_{s}$ with either another C atom that basically occupies a Si lattice site but is displaced by a Si interstitial residing in the very next surrounding or a C atom that nearly occupies a Si lattice site forming a defect other than the $\langle 100\rangle$-type with the Si atom. Again, this is a quite promising result because the C atoms are taking the appropriate coordination as expected in 3C-SiC.

Figure 17 displays the radial distribution for high C concentrations. The amorphous SiC-like phase remains. No significant change in structure is observed. However, the decrease of the cut-off artifact and slightly sharper peaks observed with increasing temperature, in turn, indicate a slight acceleration of the dynamics realized by the supply of kinetic energy. However, it is not sufficient to enable the amorphous to crystalline transition. In contrast, even though bonds of neighbored C atoms could be partially dissolved in the system exhibiting low C concentrations, the amount of neighbored C pairs even increased in the latter case. Moreover, the C-C peak at 0.252 nm in Fig. 17(b), which gets slightly more distinct, equals the second nearest-neighbor distance in diamond and indeed is made up by a structure of two C atoms interconnected by a third C atom. Obviously, processes that appear to be non-conducive are likewise accelerated in a system, in which high amounts of C are incorporated within a short period of time, which is accompanied by a concurrent introduction of accumulating, for the reason of time nondegradable damage. Thus, for these systems even larger time scales, which are not accessible within traditional MD, must be assumed for an amorphous to crystalline transition or structural evolution in general. Nevertheless, some results likewise indicate the acceleration of other processes that, again, involve $C_{s}$. The increasingly pronounced Si-C peak at 0.35 nm in Fig. 17(a) corresponds to the distance of a C and a Si atom interconnected by another Si atom. Additionally, the C-C peak at 0.31 nm in Fig. 17(b) corresponds to the distance of two C atoms bound to a central Si atom. For both structures the C atom appears to reside on a substitutional rather than an interstitial lattice site. However, huge amounts of damage hamper identification. The alignment of the investigated structures to the c-Si host is lost in many cases, which suggests the necessity of much more time for structural evolution to maintain the topotactic orientation of the precipitate.

![](./images/811624034138587137_17.jpg)

FIG. 17. (Color online) Radial distribution function for Si−C [Fig. 17(a)] and C−C [Fig. 17(b)] pairs for the C insertion into $V_2$ at elevated temperatures. Arrows mark the respective cut-off distances.

### C. Summary of classical potential calculations

Investigations are targeted at the initially stated controversy of SiC precipitation, i.e., whether precipitation occurs abruptly after enough $C_i$ agglomerated or after a successive agglomeration of $C_s$ on usual Si lattice sites (and $Si_i$) followed by a contraction into incoherent SiC. Results of the previous $ab$ $initio$ study on defects and defect combinations in C implanted Si suggest $C_s$ to play a decisive role in the precipitation of SiC in Si. To support previous assumptions, MD simulations, which are capable of modeling the necessary amount of atoms, i.e., the precipitate and the surrounding c−Si structure, have been employed in the current study.

In a previous comparative study,⁷⁵ we have shown that the utilized empirical potential fails to describe some selected processes. Thus, limitations of the employed potential have been further investigated and taken into account in the present study. We focused on two major shortcomings: the overestimated activation energy and the improper description of intrinsic and C point defects in Si. Overestimated forces between nearest neighbor atoms that are expected for short range potentials⁷⁴ have been confirmed to influence the $C_i$ diffusion. The migration barrier was estimated to be larger by a factor of 2.4 to 3.5 compared to highly accurate quantum-mechanical calculations.⁷⁵ Concerning point defects, the drastically underestimated formation energy of $C_s$ and deficiency in the description of the $Si_i$ ground state necessitated further investigations on structures that are considered important for the problem under study. It turned out that the EA potential still favors a $C_i$ ⟨1 0 0⟩ DB over a $C_s$−$Si_i$ configuration, which thus does not constitute any limitation for the simulations aiming to resolve the present controversy of the proposed SiC precipitation models.

MD simulations at temperatures used in IBS resulted in structures that were dominated by the $C_i$ ⟨1 0 0⟩ DB and its combinations if C is inserted into the total volume. Incorporation into volumes $V_2$ and $V_3$ led to an amorphous SiC−like structure within the respective volume. To compensate overestimated diffusion barriers, we performed simulations at accordingly increased temperatures. No significant change was observed for high C concentrations. The amorphous phase is maintained. Due to the incorporation of a huge amount of C into a small volume within a short period of time, damage is produced, which obviously decelerates structural evolution. For the low C concentrations, time scales are still too low to observe C agglomeration sufficient for SiC precipitation, which is attributed to the slow phase space propagation inherent to MD in general. However, we observed a phase transition of the $C_i$-dominated into a clearly $C_s$-dominated structure. The amount of substitutionally occupied C atoms increases with increasing temperature. Entropic contributions are assumed to be responsible for these structures at elevated temperatures that deviate from the ground state at 0 K. Indeed, in the $ab$ $initio$ MD simulation performed at $900^\circ$C, we observed the departing of a $Si_i$ ⟨11 0⟩ DB located next to a $C_s$ atom instead of a recombination into the ground-state configuration, i.e., a $C_i$ ⟨1 0 0⟩ DB.

### VII. CONCLUSIONS

Results of the present atomistic simulation study based on first-principles as well as classical potential methods allow to draw conclusions on mechanisms involved in the process of SiC conversion in Si. Agglomeration of $C_i$ is energetically favored and enabled by a low activation energy for migration. Although ion implantation is a process far from thermodynamic equilibrium, which might result in phases not described by the Si/C phase diagram, i.e., a C phase in Si, high activation energies are believed to be responsible for a low probability of the formation of C−C clusters.

In the context of the initially stated controversy present in the precipitation model, quantum-mechanical results suggest an increased participation of $C_s$ already in the initial stage due to its high probability of incidence. In the MD calculations, increased temperatures simulate the conditions prevalent in IBS that deviate the system from thermodynamic equilibrium enabling $C_i$ to turn into $C_s$. The associated emission of $Si_i$ serves two needs: as a vehicle for other $C_s$ atoms and as a supply of Si atoms needed elsewhere to form the SiC structure. As for the vehicle, $Si_i$ is believed to react with $C_s$ turning it

into highly mobile $C_i$ again, allowing for the rearrangement of the C atom. The rearrangement is crucial to end up in a configuration of C atoms only occupying substitutionally lattice sites of one of the two fcc lattices that build up the diamond lattice. However, the conversion of some region of Si into SiC by substitutional C is accompanied by a reduction of the volume because SiC exhibits a 20% smaller lattice constant than Si. The reduction in volume is compensated by excess $S_i$ serving as building blocks for the surrounding Si host or a further formation of SiC.

It is worth to mention that there is no contradiction to results of the HREM studies. $^{17-21}$ Regions showing dark contrasts in an otherwise undisturbed Si lattice are attributed to C atoms in the interstitial lattice. However, there is no particular reason for the C species to reside in the interstitial lattice. Contrasts are also assumed for $S_i$. After precipitation occurs, regions of dark contrasts disappear in favor of Moiré patterns indicating 3C–SiC in c–Si due to the mismatch in the lattice constant. Until then, however, these regions are either composed of stretched coherent SiC and interstitials or of already contracted incoherent SiC surrounded by Si and interstitials, where the latter is too small to be detected in HREM. In both cases $S_i$ might be attributed a third role, which is the partial compensation of tensile strain that is present either in the stretched SiC or at the interface of the contracted SiC and the Si host.

In addition, the experimentally observed alignment of the $(h\ k\ l)$ planes of the precipitate and the substrate is satisfied by the mechanism of successive positioning of $C_s$. In contrast, there is no obvious reason for the topotactic orientation of an agglomerate consisting exclusively of C–Si dimers, which would necessarily involve a much more profound change in structure for the transition into SiC.

Moreover, results of the MD simulations at different temperatures and C concentrations can be correlated to experimental findings. Experimental studies revealed increased implantation temperatures to be more efficient than postannealing methods for the formation of topotactically aligned precipitates. $^{97,98}$ In particular, restructuring of strong C–C bonds is affected, $^{99}$ which preferentially arise if additional kinetic energy provided by an increase of the implantation temperature is missing to accelerate or even enable atomic rearrangements. We assume this to be related to the problem of slow structural evolution encountered in the high C concentration simulations due to the insertion of high amounts of C into a small volume within a short period of time resulting in essentially no time for the system to rearrange. More substantially, understoichiometric implantations at room temperature into preamorphized Si followed by a solid phase epitaxial regrowth step at $700\,^{\circ}\text{C}$ result in $\text{Si}_{1-x}\text{C}_x$ layers in the diamond cubic phase with C residing on substitutional Si lattice sites. $^{100}$ The strained structure is found to be stable up to $810\,^{\circ}\text{C}$. Coherent clustering followed by precipitation is suggested if these structures are annealed at higher temperatures. Similar, implantations of an understoichiometric dose at room temperature followed by thermal annealing results in small spherical sized $C_i$ agglomerates at temperatures below $700\,^{\circ}\text{C}$ and SiC precipitates of the same size at temperatures above $700\,^{\circ}\text{C}$ (Ref. 18). However, because the implantation temperature is considered more efficient than the postannealing temperature, SiC precipitates are expected and indeed observed for as-implanted samples in implantations performed at $450\,^{\circ}\text{C}$. (Refs. 14 and 15) Thus, implanted C is likewise expected to occupy substitutionally usual Si lattice sites right from the start for implantations into c–Si at elevated temperatures.

Thus, we propose an increased participation of $C_s$ already in the initial stages of the implantation process at temperatures above $450\,^{\circ}\text{C}$, the temperature most applicable for the formation of SiC layers of high crystalline quality and topotactical alignment. $^{14}$ Thermally activated, $C_i$ is enabled to turn into $C_s$ accompanied by $S_i$. The associated emission of $S_i$ is needed for several reasons. For the agglomeration and rearrangement of C, $S_i$ is needed to turn $C_s$ into highly mobile $C_i$ again. Because the conversion of a coherent SiC structure, i.e., $C_s$ occupying the Si lattice sites of one of the two fcc lattices that build up the c–Si diamond lattice, into incoherent SiC is accompanied by a reduction in volume, large amounts of strain are assumed to reside in the coherent as well as at the surface of the incoherent structure. $S_i$ serves either as a supply of Si atoms needed in the surrounding of the contracted precipitates or as an interstitial defect minimizing the emerging strain energy of a coherent precipitate. The latter has been directly identified in the present simulation study, i.e., structures of two $C_s$ atoms and $S_i$ located in the vicinity.

### VIII. SUMMARY

In summary, C and Si point defects in Si, combinations of these defects and diffusion processes within such configurations have been investigated. We have shown that C interstitials in Si tend to agglomerate, which is mainly driven by a reduction of strain. Investigations of migration pathways, however, allow to conclude that C clustering is hindered due to high activation energies of the respective diffusion processes. A highly attractive interaction and a large capture radius has been identified for the $C_i$ $\langle 100 \rangle$ DB and the vacancy indicating a high probability for the formation of $C_s$. In contrast, a rapidly decreasing interaction with respect to the separation distance has been identified for $C_s$ and a $S_i$ $\langle 110 \rangle$ DB resulting in a low probability of defects exhibiting respective separations to transform into the $C_i$ $\langle 100 \rangle$ DB, which constitutes the ground-state configuration for a C atom introduced into otherwise perfect Si. An increased participation of $C_s$ during implantation at elevated temperatures is concluded.

Results of the classical potential MD simulations reinforce conclusions drawn from first-principles calculations. Increased temperatures were utilized to compensate overestimated diffusion barriers and simulate conditions of the IBS process, which is far from equilibrium. A transition of a $C_i$-dominated structure at low temperatures into a $C_s$-dominated structure at high temperatures was observed. The associated $S_i$ existing in structures of the high temperature simulations is directly identified to compensate tensile strain available in stretched structures of $C_s$, which are considered initial, coherently aligned SiC precipitates.

We conclude that precipitation occurs by successive agglomeration of $C_s$ as already proposed by Nejim *et al.*$^{24}$ However, agglomeration and rearrangement is enabled by

mobile $C_i$, which has to be present at the same time and is formed by recombination of $C_s$ and $Si_i$. In contrast to assumptions of an abrupt precipitation of an agglomerate of $C_i$, $^{17-21}$ however, structural evolution is believed to occur by a successive occupation of usual Si lattice sites with substitutional C. This mechanism satisfies the experimentally observed alignment of the $(h\ k\ l)$ planes of the precipitate and the substrate, whereas there is no obvious reason for the topotactic orientation of an agglomerate consisting ex- clusively of C–Si dimers, which would necessarily involve a much more profound change in structure for the transition into SiC.

## ACKNOWLEDGMENTS

We gratefully acknowledge financial support by the Bay- erische Forschungsstiftung (DPA-61/05) and the Deutsche Forschungsgemeinschaft (DFG SCHM 1361/11).

*frank.zirkelbach@physik.unl-augsburg.de*

$^{1}$J. H. Edgar, J. Mater. Res. **7**, 235 (1992).
$^{2}$H. Morkoç, S. Strite, G. B. Gao, M. E. Lin, B. Sverdlov, and M. Burns, J. Appl. Phys. **76**, 1363 (1994).
$^{3}$W. Wesch, Nucl. Instrum. Methods Phys. Res., Sec. B **116**, 305 (1996).
$^{4}$M. A. Capano and R. J. Trew, MRS Bull. **22**, 19 (1997).
$^{5}$Y. S. Park, *SiC Materials and Devices* (Academic Press, San Diego, 1998).
$^{6}$G. R. Fisher and P. Barnes, Philos. Mag. B **61**, 217 (1990).
$^{7}$J. A. Powell, D. J. Larkin, L. G. Matus, W. J. Choyke, J. L. Bradshaw, L. Henderson, M. Yoganathan, J. Yang, and P. Pirouz, Appl. Phys. Lett. **56**, 1353 (1990).
$^{8}$A. Fissel, U. Kaiser, E. Ducke, B. Schröter, and W. Richter, J. Cryst. Growth **154**, 72 (1995).
$^{9}$A. Fissel, B. Schröter, and W. Richter, Appl. Phys. Lett. **66**, 3182 (1995).
$^{10}$S. Nishino, J. A. Powell, and H. A. Will, Appl. Phys. Lett. **42**, 460 (1983).
$^{11}$S. Nishino, H. Suhara, H. Ono, and H. Matsunami, J. Appl. Phys. **61**, 4889 (1987).
$^{12}$M. Kitabatake, M. Deguchi, and T. Hirao, J. Appl. Phys. **74**, 4438 (1993).
$^{13}$J. A. Borders, S. T. Picraux, and W. Beezhold, Appl. Phys. Lett. **18**, 509 (1971).
$^{14}$J. K. N. Lindner and B. Stritzker, Nucl. Instrum. Methods Phys. Res. Sec. B **147**, 249 (1999).
$^{15}$J. K. N. Lindner, Nucl. Instrum. Methods Phys. Res. Sec. B **178**, 44 (2001).
$^{16}$J. K. N. Lindner, Appl. Phys. A **77**, 27 (2003).
$^{17}$J. K. N. Lindner and B. Stritzker, Nucl. Instrum. Methods Phys. Res. B **148**, 528 (1999).
$^{18}$P. Werner, R. Kögler, W. Skorupa, and D. Eichler, in *Proceedings of the 11th International Conference on Ion Implantation Technology* (IEEE, Austin, TX, USA, 1996), pp. 675–678.
$^{19}$P. Werner, S. Eichler, G. Mariani, R. Kögler, and W. Skorupa, Appl. Phys. Lett. **70**, 252 (1997).
$^{20}$F. Eichhorn, N. Schell, W. Matz, and R. Kögler, J. Appl. Phys. **86**, 4184 (1999).
$^{21}$R. Kögler, F. Eichhorn, J. R. Kaschny, A. Mücklich, H. Reuther, W. Skorupa, C. Serre, and A. Perez-Rodriguez, Appl. Phys. A **76**, 827 (2003).
$^{22}$J. W. Strane, H. J. Stein, S. R. Lee, S. T. Picraux, J. K. Watanabe, and J. W. Mayer, J. Appl. Phys. **76**, 3656 (1994).
$^{23}$C. Guedj, M. W. Dashiell, L. Kulik, J. Kolodzey, and A. Hairie, J. Appl. Phys. **84**, 4631 (1998).

$^{24}$A. Nejim, P. L. F. Hemment, and J. Stoemenos, Appl. Phys. Lett. **66**, 2646 (1995).
$^{25}$J. W. Strane, S. R. Lee, H. J. Stein, S. T. Picraux, J. K. Watanabe, and J. W. Mayer, J. Appl. Phys. **79**, 637 (1996).
$^{26}$P. Lavéant, G. Gerth, P. Werner, and U. Gösele, Mater. Sci. Eng. B **89**, 241 (2002).
$^{27}$Y. Bar-Yam and J. D. Joannopoulos, Phys. Rev. Lett. **52**, 1129 (1984).
$^{28}$Y. Bar-Yam and J. D. Joannopoulos, Phys. Rev. B **30**, 1844 (1984).
$^{29}$R. Car, P. J. Kelly, A. Oshiyama, and S. T. Pantelides, Phys. Rev. Lett. **52**, 1814 (1984).
$^{30}$I. P. Batra, F. F. Abraham, and S. Ciraci, Phys. Rev. B **35**, 9552 (1987).
$^{31}$P. E. Blöchl, E. Smargiassi, R. Car, D. B. Laks, W. Andreoni, and S. T. Pantelides, Phys. Rev. Lett. **70**, 2435 (1993).
$^{32}$M. Tang, L. Colombo, J. Zhu, and T. Diaz de la Rubia, Phys. Rev. B **55**, 14279 (1997).
$^{33}$W.-K. Leung, R. J. Needs, G. Rajagopal, S. Itoh, and S. Ihara, Phys. Rev. Lett. **83**, 2351 (1999).
$^{34}$L. Colombo, Annu. Rev. Mater. Res. **32**, 271 (2002).
$^{35}$S. Goedecker, T. Deutsch, and L. Billard, Phys. Rev. Lett. **88**, 235501 (2002).
$^{36}$O. K. Al-Mushadani and R. J. Needs, Phys. Rev. B **68**, 235205 (2003).
$^{37}$G. Hobler and G. Kresse, Mater. Sci. Eng. B **124-125**, 368 (2005).
$^{38}$B. Sahli and W. Fichtner, Phys. Rev. B **72**, 245210 (2005).
$^{39}$M. Posselt, F. Gao, and H. Bracht, Phys. Rev. B **78**, 035208 (2008).
$^{40}$S. Ma and S. Wang, Phys. Rev. B **81**, 193203 (2010).
$^{41}$M. Mazzarolo, L. Colombo, G. Lulli, and E. Albertazzi, Phys. Rev. B **63**, 195207 (2001).
$^{42}$E. Holmström, A. Kuronen, and K. Nordlund, Phys. Rev. B **78**, 045202 (2008).
$^{43}$J. Tersoff, Phys. Rev. Lett. **64**, 1757 (1990).
$^{44}$A. Dal Pino, A. M. Rappe, and J. D. Joannopoulos, Phys. Rev. B **47**, 12554 (1993).
$^{45}$R. B. Capaz, A. Dal Pino, and J. D. Joannopoulos, Phys. Rev. B **50**, 7439 (1994).
$^{46}$M. J. Burnard and G. G. DeLeo, Phys. Rev. B **47**, 10217 (1993).
$^{47}$P. Leary, R. Jones, S. Öberg, and V. J. B. Torres, Phys. Rev. B **55**, 2188 (1997).
$^{48}$R. B. Capaz, A. Dal Pino, and J. D. Joannopoulos, Phys. Rev. B **58**, 9845 (1998).
$^{49}$J. Zhu, Comput. Mater. Sci. **12**, 309 (1998).
$^{50}$A. Mattoni, F. Bernardini, and L. Colombo, Phys. Rev. B **66**, 195214 (2002).


$^{51}$S. Y. Park, J. D'Arcy-Gall, D. Gall, J. A. N. T. Soares, Y.-W. Kim, H. Kim, P. Desjardins, J. E. Greene, and S. G. Bishop, J. Appl. Phys. **91**, 5716 (2002).

$^{52}$R. Jones, B. J. Coomer, and P. R. Briddon, J. Phys. Condens. Matter **16**, S2643 (2004).

$^{53}$V. Chirita, L. Hultman, and L. R. Wallenberg, *Thin Solid Films* **294**, 47 (1997).

$^{54}$G. Cicero, L. Pizzagalli, and A. Catellani, Phys. Rev. Lett. **89**, 156101 (2002).

$^{55}$L. Pizzagalli, G. Cicero, and A. Catellani, Phys. Rev. B **68**, 195302 (2003).

$^{56}$M. Bockstedte, A. Mattausch, and O. Pankratov, Phys. Rev. B **68**, 205201 (2003).

$^{57}$E. Rauls, T. Frauenheim, A. Gali, and P. Deák, Phys. Rev. B **68**, 155208 (2003).

$^{58}$F. Gao, W. J. Weber, M. Posselt, and V. Belko, Phys. Rev. B **69**, 245205 (2004).

$^{59}$M. Posselt, F. Gao, and W. J. Weber, Phys. Rev. B **73**, 125206 (2006).

$^{60}$F. Gao, J. Du, E. J. Bylaska, M. Posselt, and W. J. Weber, Appl. Phys. Lett. **90**, 221915 (2007).

$^{61}$F. H. Stillinger and T. A. Weber, Phys. Rev. B **31**, 5262 (1985).

$^{62}$D. W. Brenner, Phys. Rev. B **42**, 9458 (1990).

$^{63}$J. Tersoff, Phys. Rev. B **38**, 9902 (1988).

$^{64}$M. Z. Bazant and E. Kaxiras, Phys. Rev. Lett. **77**, 4370 (1996).

$^{65}$M. Z. Bazant, E. Kaxiras, and J. F. Justo, Phys. Rev. B **56**, 8542 (1997).

$^{66}$J. F. Justo, M. Z. Bazant, E. Kaxiras, V. V. Bulatov, and S. Yip, Phys. Rev. B **58**, 2539 (1998).

$^{67}$H. Balamane, T. Halicioglu, and W. A. Tiller, Phys. Rev. B **46**, 2250 (1992).

$^{68}$H. Huang, N. M. Ghoniem, J. K. Wong, and M. Baskes, Modell. Simul. Mater. Sci. Eng. **3**, 615 (1995).

$^{69}$J. Godet, L. Pizzagalli, S. Brochard, and P. Beauchamp, J. Phys. Condens. Matter **15**, 6943 (2003).

$^{70}$G. Lucas, M. Bertolus, and L. Pizzagalli, J. Phys. Condens. Matter **22**, 035802 (2010).

$^{71}$J. Tersoff, Phys. Rev. B **39**, 5566 (1989).

$^{72}$F. Gao and W. J. Weber, Nucl. Instrum. Methods Phys. Res. Sec. B **191**, 487 (2002).

$^{73}$P. Erhart and K. Albe, Phys. Rev. B **71**, 035211 (2005).

$^{74}$A. Mattoni, M. Ippolito, and L. Colombo, Phys. Rev. B **76**, 224103 (2007).

$^{75}$F. Zirkelbach, B. Stritzker, K. Nordlund, J. K. N. Lindner, W. G. Schmidt, and E. Rauls, Phys. Rev. B **82**, 094110 (2010).

$^{76}$G. Kresse and J. Furthmüller, Comput. Mater. Sci. **6**, 15 (1996).

$^{77}$J. P. Perdew and Y. Wang, Phys. Rev. B **33**, 8800 (1986).

$^{78}$J. P. Perdew, J. A. Chevary, S. H. Vosko, K. A. Jackson, M. R. Pederson, D. J. Singh, and C. Fiolhais, Phys. Rev. B **46**, 6671 (1992).

$^{79}$D. R. Hamann, M. Schlüter, and C. Chiang, Phys. Rev. Lett. **43**, 1494 (1979).

$^{80}$D. Vanderbilt, Phys. Rev. B **41**, 7892 (1990).

$^{81}$H. J. C. Berendsen, J. P. M. Postma, W. F. van Gunsteren, A. DiNola, and J. R. Haak, J. Chem. Phys. **81**, 3684 (1984).

$^{82}$L. Verlet, Phys. Rev. **159**, 98 (1967).

$^{83}$M. Kaukonen, P. K. Sitch, G. Jungnickel, R. M. Nieminen, S. Pöykkö, D. Porezag, and T. Frauenheim, Phys. Rev. B **57**, 9965 (1998).

$^{84}$G. D. Watkins and K. L. Brower, Phys. Rev. Lett. **36**, 1329 (1976).

$^{85}$L. W. Song and G. D. Watkins, Phys. Rev. B **42**, 5759 (1990).

$^{86}$F. Zirkelbach, J. K. N. Lindner, K. Nordlund, and B. Stritzker, Mater. Sci. Eng. B **159-160**, 149 (2009).

$^{87}$J. K. N. Lindner, M. Häberlen, G. Thorwarth, and B. Stritzker, Mater. Sci. Eng. C **26**, 857 (2006).

$^{88}$A. K. Tipping and R. C. Newman, Semicond. Sci. Technol. **2**, 315 (1987).

$^{89}$L. W. Song, X. D. Zhan, B. W. Benson, and G. D. Watkins, Phys. Rev. B **42**, 5765 (1990).

$^{90}$C.-L. Liu, W. Windl, L. Borucki, S. Lu, and X.-Y. Liu, Appl. Phys. Lett. **80**, 52 (2002).

$^{91}$A. F. Voter, Phys. Rev. Lett. **78**, 3908 (1997).

$^{92}$A. F. Voter, J. Chem. Phys. **106**, 4665 (1997).

$^{93}$A. F. Voter, Phys. Rev. B **57**, R13985 (1998).

$^{94}$M. R. Sørensen and A. F. Voter, J. Chem. Phys. **112**, 9599 (2000).

$^{95}$X. Wu and S. Wang, J. Chem. Phys. **110**, 9401 (1999).

$^{96}$M. Tang and S. Yip, Phys. Rev. B **52**, 15150 (1995).

$^{97}$T. Kimura, S. Kagiyama, and S. Yugo, *Thin Solid Films* **94**, 191 (1982).

$^{98}$F. Eichhorn, N. Schell, A. Mücklich, H. Metzger, W. Matz, and R. Kögler, J. Appl. Phys. **91**, 1287 (2002).

$^{99}$M. Deguchi, M. Kitabatake, T. Hirao, N. Arai, and T. Izumi, Jpn. J. Appl. Phys. **31**, 343 (1992).

$^{100}$J. W. Strane, H. J. Stein, S. R. Lee, B. L. Doyle, S. T. Picraux, and J. W. Mayer, Appl. Phys. Lett. **63**, 2786 (1993).