# Radiation-induced crystalline-to-amorphous transition in intermetallic compounds of the Cu-Ti alloy system*

N. Q. Lam and P. R. Okamoto
Materials Science Division, Argonne National Laboratory, Argonne, IL 60439 (USA)

M. J. Sabochick
Computer Applications Division, Gulf States Utilities Co., Beaumont, TX 77704 (USA)

R. Devanathan
Materials Science Division, Argonne National Laboratory, Argonne, IL 60439 (USA)

(Received March 10, 1992; in final form May 14, 1992)

## Abstract
Recent progress in molecular-dynamics studies of radiation-induced crystalline-to-amorphous transition in the ordered intermetallic compounds of the Cu-Ti system is discussed. The effect of irradiation was simulated by the generation of Frenkel pairs, which resulted in both the formation of stable point defects and chemical disorder upon defect recombination. The thermodynamic, structural and mechanical responses of the compounds during irradiation were determined by monitoring changes in the system potential energy, volume expansion, pair-correlation function, diffraction patterns, and elastic constants. It was found that the intermetallics $Cu_4Ti_3$, CuTi and $CuTi_2$ could be rendered amorphous by the creation of Frenkel pairs, but $Cu_4Ti$ could not, consistent with experimental observations during electron irradiation. However, the simulations showed that $Cu_4Ti$ did become amorphous when clusters of Frenkel pairs were introduced, indicating that this compound may be susceptible to amorphization by heavy-ion bombardment. A generalization of the Lindemann criterion was used to develop a thermodynamic description of solid-state amorphization as a disorder-induced melting process.

---

## 1. Introduction
The crystalline-to-amorphous (c-a) transition induced by displacement-producing irradiation takes place in many intermetallic compounds. Although several fundamental aspects of the transformation, including the nature of the driving force, the order of transition and the transformation mechanism, are not well understood, experiments on various ordered intermetallics have revealed a number of characteristic features [1, 2]. Firstly, for a given type of irradiation, there exists a critical temperature above which amorphization cannot be induced. The critical dose for amorphization is temperature independent at very low temperatures, but rises sharply near the critical temperature. This temperature is significantly higher for heavy-ion bombardment than for electron irradiation [3]. Secondly, during irradiation, the long-range order parameter, $S$, drops rapidly from 1 (i.e. the value for the perfect lattice), and the volume of the compound expands with increasing dose. At the onset of amorphization, $S$ decreases to approximately 0.2 [4-6], and the volume expansion saturates at values between 2% [5] and 6% [7]. Thirdly, in compounds that become amorphous during irradiation, e.g. $Zr_3Al$, FeTi and $Nb_3Ir$, the velocity of acoustic phonons decreases by about 70% when amorphization occurs [2]. Since the sound velocity is proportional to the square root of the average shear modulus, the latter is found to drop by a factor of about 2 [5, 7].

Due to its simplicity, electron irradiation-induced amorphization has been investigated most systematically during recent years ([1, 2] and references therein). Experimentally, it was found that most of the amorphizable alloys are high-temperature intermetallic compounds, which are composed of early transition or refractory elements with unpaired d-electrons (e.g. Ti, Zr, V, Mo) and late transition or noble metals having nearly filled d-shells (e.g. Fe, Co, Ni, Cu). The latter elements tend to have significantly smaller atomic sizes (> 15%) than those of the early transition metal group. It is generally accepted that the increase in the free energy of the compounds, caused by the decrease in

---

*Paper presented at the Symposium on Solid State Amorphizing Transformations, TMS Fall Meeting, Cincinnati, OH, October 21-24, 1991.

long-range order and/or by the production of Frenkel defects, provides the necessary driving force for amor- phization. However, it is difficult to determine exper- imentally which mechanism, chemical disordering or point-defect production, plays the dominant role in inducing amorphization. This difficulty arises because the incident electrons generally produce both lattice defects and chemical disorder. Their relative contri- bution to the lattice expansion and property changes, which occur prior to the c-a transition, cannot be interpreted unambiguously.

To aid in the interpretation of experiments, a number of molecular-dynamics studies have been carried out recently [8-15]. In computer simulations, one can easily induce chemical disorder, Frenkel pairs, or vary the system volume without introducing point defects, and thus the specific effects of individual mechanisms can be studied. Unfortunately, except the work of Massobrio et al. [12], earlier computer simulations focused on monoatomic solids, due to the lack of appropriate interatomic potentials for alloys [8-11]. More recently, we performed a series of molecular-dynamics simula- tions of radiation-induced amorphization in several intermetallics [13-17], using interatomic potentials de- veloped with the embedded-atom method [18, 19]. The present paper summarizes the simulation results that were obtained for four intermetallic compounds of the Cu-Ti alloy system, $Cu_{4} Ti, Cu_{4} Ti_{3}, CuTi$, and $CuTi_{2}$. It is noted that, among alloy systems investigated ex- perimentally, the Cu-Ti system has been studied most systematically [1, 2], and that, with the exception of $Cu_{4} Ti$, these compounds can be amorphized by electron irradiation.

## 2. Model and computational procedure

![](./images/812402998033514497_1.jpg)

Fig. 1. Crystal structures of $Cu_{4} Ti, Cu_{4} Ti_{3}, CuTi$ and $CuTi_{2}$.

The crystallographic structures of the compounds simulated in the present work are shown in Fig. 1. The model lattice that represents the ordered $Cu_{4} Ti$ com pound has a $D1_{a}$ orthorhombic structure. The $Cu_{4} Ti_{3}$ compound has a complicated Frank-Kasper-type struc- ture, consisting of seven stacked body-centered tetrag- onal sublattices. The other two compounds, CuTi and $CuTi_{2}$, have the $B 11$ and $C 15_{b}$ structures, with stacking of two and three body-centered tetragonal sublattices, respectively. The interactions between atoms in these model systems were governed by appropriate potentials, which were developed with the approach of Oh and Johnson [19], based on the embedded-atom method [18]. Details of the fitting procedure and functional form of the potentials are given elsewhere [14]. In deriving the potential for the compounds, the structure, the atomic volume and the heat of formation of CuTi and $CuTi_{2}$ were fitted. No systematic fitting was per formed for $Cu_{4} Ti$ and $Cu_{4} Ti_{3}$; however, the potential obtained was also used for simulations of these com- pounds because it stabilizes their structures and correctly predicts their lattice constants. The calculated values of the lattice constant $a$, equilibrium atomic volume $\Omega$, and heat of formation $\Delta H_{f}$ of $Cu_{4} Ti_{3}, CuTi$ and $CuTi_{2}$ have been tabulated in ref. 14; the corresponding values for $Cu_{4} Ti$ are $a=0.5885 ~nm, \Omega=0.01230 ~nm^{3} /$ atom and $\Delta H_{f}=0.0940 eV /$ atom.

In the simulation, the effect of chemical disordering was studied by exchanging a random pair of $Cu$ and Ti atoms, and the production of a Frenkel pair was simulated by removing a randomly selected atom (cre- ating a vacancy) and then reinserting it at a random position in the lattice (forming an interstitial). Initially, a perfect lattice was first equilibrated at $160 ~K$ for5000 time steps $(\Delta t)$, and the physical properties of the system in the ground state were calculated. For equilibration and property calculations, we used mo- lecular dynamics (using a modified version of the code DYNAMO [20]). Then, every $10 \Delta t$, a random pair of antisite defects or a Frenkel pair was created. To relax the system after each introduction of a defect, we employed molecular statics with the Fletcher-Powell minimization procedure [21]. The system configuration was saved periodically during the defect production process, and subsequently equilibrated for additional $6000 \Delta t$ in separate runs. The equilibrated systems were analyzed by comparing their potential energies, volumes, pair-correlation functions, structure factors, atom pro- jections and elastic constants with those of the perfect lattice. The elastic constants were determined with the fluctuation formulae of Ray et al. [22]. They werecalculated every $10 \Delta t$ and time averaged over 20000 At. Several calculations of the elastic constants for CuTi

and $Cu_4Ti_3$ after chemical disordering and Frenkel-pair production were also performed using the zero-temperature method developed recently by Lutsko [23].

## 3. Results and discussion

### 3.1. Driving force for amorphization

The two most straightforward properties to calculate in simulations are the potential energy and volume of the system. These properties are shown in Fig. 2 as functions of "dose" for the $Cu_4Ti$ compound. Here, the dose is defined as either the number of Cu-Ti pairs exchanged per atom (epa) or the number of Frenkel pairs created per atom (dpa). For the case of atom pair exchanges, as shown by curves AB, both the energy and volume increase rapidly with increasing number of exchanges, but then saturate as complete chemical disordering is approached ($S \to 0$). The energy and volume attain maximum values, which are, respectively, 0.02 eV per atom and 1% larger than those of the perfect lattice. Similar variations in these quantities are also observed during the introduction of point defects (curves AC). Although the saturation levels obtained by Frenkel-pair introduction are roughly a factor of 2 higher than in the case of atom exchanges, they are still far below the corresponding values for the quenched liquid (shown by the dashed lines). Calculated pair-correlation functions, shown by curves B and C in Fig. 3, indicate that, after a dose of 1.04 epa (complete chemical disorder) or 1.04 dpa, the compound remains crystalline. To further test the structural response of the crystalline compound to the additional accumulation of point defects, we continued to introduce Frenkel pairs to a total dose of 5 dpa, using two different approaches. From 1.04 dpa to 3.13 dpa (i.e. from C to D in Fig. 2), two Frenkel pairs were created simultaneously in each defect-production event (every $10\ \Delta t$). Even though this approach was found to be efficient in inducing amorphization in the $CuTi_2$ compound [14] (see also Fig. 7), it failed to cause further increase in the potential energy and volume and, hence, to amorphize $Cu_4Ti$ (curve D in Fig. 3). From 3.13 dpa to 5.0 dpa (i.e. from D to $E'$ or E in Fig. 2), the rate of Frenkel-pair production was increased by an order of magnitude, i.e. either a Frenkel pair was generated in every time step $\Delta t$ (from D to $E'$) or a group of 10 Frenkel pairs was created every $10\ \Delta t$ (from D to E). The former process caused only a slight increase in the energy and volume of the compound, insufficient to induce amorphization. On the contrary, the latter process was effective in destabilizing the system, boosting its energy and volume to the levels of the quenched $Cu_4Ti$ liquid, and amorphizing the compound (compare the pair-correlation functions shown by curves E and F in Fig. 3). Figure 2 also shows the corresponding changes in the shear moduli $C_{44}$, $C'=0.5(C_{11}-C_{12})$ and their average value $C_{\text{avg}}=0.5(C_{44}+C')$. Although these moduli are noticeably softened by the introduction of lattice imperfections, $C_{44}$ is always higher than $C'$ as long as the compound retains its crystallinity. Only when complete amorphization occurs do $C_{44}$ and $C'$ become equal to each other.

![](./images/812402998033514497_2.jpg)

Fig. 2. Changes in the potential energy, volume expansion and shear moduli as a function of the number of atom exchanges or Frenkel pairs per atom in $Cu_4Ti$. The values calculated for the quenched $Cu_4Ti$ liquid are indicated by the horizontal dashed lines. Note that $C_{44}$ and $C'$ approach each other when amorphization occurs.

That $Cu_4Ti$ cannot be rendered amorphous by the introduction of Frenkel pairs is in agreement with the experimental observation that this compound remained crystalline during electron irradiation [24]. However, the finding that the c-a transformation can be triggered by Frenkel pairs, simultaneously produced in groups indicates that it may be possible to amorphize $Cu_4Ti$ by ion bombardment.

The structural response of $Cu_4Ti_3$ and CuTi during irradiation is different from that of $Cu_4Ti$. For example, the changes in the physical properties of these two compounds as a result of chemical disordering and

![](./images/812402998033514497_3.jpg)

Fig. 3. Pair-correlation functions $g(r)$ of the $Cu_4Ti$ compound at 160 K. Curve A is for the perfect lattice. The other curves are for configurations after the following treatments: curve B after complete chemical disordering, 1.04 epa; curve C after introduction of Frenkel pairs to a dose of 1.04 dpa; curve D after additional introduction of double Frenkel pairs to a dose of 3.13 dpa; curve E after additional introduction of groups of ten Frenkel pairs every $10\ \Delta t$ to a dose of 4.17 dpa; and curve F quenched CuTi liquid from 4000 K.

![](./images/812402998033514497_4.jpg)

Fig. 4. Changes in the potential energy, volume expansion and shear moduli as a function of the number of atom exchanges or Frenkel pairs per atom in $Cu_4Ti_3$ at 160 K. The values calculated for the quenched $Cu_4Ti_3$ liquid are shown by the horizontal dashed lines. All the shear moduli, $C_{44}$, $C'$ and $C_{avg}$, become equal to each other when the system is completely isotropic.

Frenkel-pair production are shown in Figs. 4 and 5 respectively. Initially, most of the Frenkel pairs created recombine, resulting in the formation of antisite defects. Consequently, the difference in the effects of the two types of defect production in the early stage is small. If chemical disordering is produced via atom-pair ex- changes, the system energy and volume expansion reach maximum values at a certain degree of disorder (cor- responding to $S=0.16$ [16]). These values are, however, significantly smaller than those of the quenched liquids, shown by the dashed lines. Only when point defects are introduced can their accumulation further boost the potential energy and system volume to the quenched- liquid levels. Furthermore, as shown in the lower por- tions of Figs. 4 and 5, the lattice softens considerably during the generation of Frenkel pairs, as indicated by the variations in the shear moduli $C_{44}$ and $C'$, and their average values, $C_{avg}$. The shear modulus $C_{44}$ decreases rapidly with increasing dose and eventually becomes equal to $C'$ (which first decreases and then increases) when amorphization is completed.

An example of the microstructural evolution of the compounds is given in Fig. 6, showing the changes in

![](./images/812402998033514497_5.jpg)

Fig. 5. Changes in the potential energy, volume expansion and shear moduli as a function of the number of atom exchanges or Frenkel pairs per atom in CuTi at 160 K. The values calculated for the quenched CuTi liquid are shown by the horizontal dashed lines. The shear moduli are equal to each other when the system becomes completely isotropic.

the calculated pair-correlation functions, atom projections onto the (100) plane and diffraction patterns for CuTi. As can be seen, when all the Cu and Ti atoms have been exchanged, the system becomes chemically disordered, but not amorphized. However, when Frenkel pairs are created, the system becomes partially amorphized at a dose of about 0.5 dpa, and completely amorphous at about 1.0 dpa. Here, the critical dose for complete amorphization is defined as the point when the system becomes isotropic, i.e. when $C_{44}=C'$. Using this definition, the critical dose for amorphization of $Cu_{4}Ti_{3}$ is 0.6 dpa.

Somewhat similar behavior was observed in $CuTi_{2}$, as shown in Fig. 7. It was found, however, that, if only one Frenkel pair was created in each defect-production event, almost all the interstitials and vacancies recombined, resulting in the creation of antisite defects. As a result, there was no large difference in the effects of atom exchange and Frenkel-pair generation, and even after a dose of 2 dpa the energy storage and volume expansion were insufficient to drive the system toward an amorphous state [14]. One way to increase further the energy and volume of the compound is to reduce the recombination effect, e.g. by allowing defect clustering or by randomly producing interstitials and vacancies individually in time-separated events [14]. For example, simultaneous creation of two Frenkel pairs in each event rapidly increases the system energy and volume to the values obtained for the quenched $CuTi_{2}$ liquid (Fig. 7), and amorphization can be induced after a dose of about 0.45 dpa (curve E in Fig. 7). The rates of energy and volume increase were found to be independent of the spatial separation between the vacancies in each defect-production step.

The calculated critical doses for amorphization of $Cu_{4}Ti_{3}$, CuTi and $CuTi_{2}$ are in general agreement with experimental observations [3-6, 25]. There are no measurements of the volume expansions at the onset of amorphization in the intermetallics of the Cu-Ti system. However, the simulation results appear consistent with those calculated for $NiZr_{2}$ [12] and NiZr [26], as well as with those obtained experimentally for other compounds, including $Zr_{3}Al$ [5], NiAl [7], $Nb_{3}Ge$ [27, 28] and $Mo_{3}Si$ [29].

### 3.2. Relationship between shear modulus and volume expansion

In Fig. 8, the average shear modulus $C_{avg}$ and $C'$ of $Cu_{4}Ti_{3}$ and CuTi are plotted as a function of volume expansion caused by heating, chemical disordering and Frenkel-pair creation. Two important features are noted. Firstly, the average shear modulus of the crystal that contains defects decreases significantly faster with volume expansion than that associated with heating. Secondly, when Frenkel pairs are generated, a reduction of about 55% in the average shear modulus is found at the onset of amorphization.

The first of these results was somewhat surprising, since earlier computer simulations of the melting process in Cu [30] showed that the volume dependence of the shear moduli $C_{44}$ and $C'$ during homogeneous expansion at constant temperature was virtually identical to that associated with thermal expansion at constant pressure, which implies that the volume dependence of the elastic

![](./images/812402998033514497_6.jpg)

Fig. 6. Pair-correlation functions $g(r)$, atom projections onto the (100) plane and diffraction patterns of the CuTi compound in various configurations: (A) the perfect lattice; (B) after complete chemical disordering, 1.04 epa, (C) after introduction of Frenkel pairs to a dose of 0.43 dpa; (D) after a dose of 0.52 dpa; (E) after a dose of 0.69 dpa; and (F) quenched CuTi liquid from 4000 K.

constant does not depend on how the expansion is produced. However, it is now recognized that this behavior is simply a consequence of the homogeneous nature of the expansions employed in the earlier sim- ulations. Thermal expansion involves no change in chemical long-range order and is thus homogeneous in nature. By contrast, the volume expansion associated with chemical disordering and/or Frenkel defects results

![](./images/812402998033514497_7.jpg)

Fig. 7. Left: changes in the potential energy and volume expansion as a function of the number of atom exchanges or Frenkel pairs per atom in $CuTi_2$ at 160 K. The values calculated for the quenched $CuTi_2$ liquid are shown by the horizontal dashed lines. Right: pair-correlation functions of the compound in various configurations: (A) the perfect lattice; (B) after complete chemical disordering, 1.36 epa; (C) after introduction of Frenkel pairs to a dose of 0.45 dpa; (D) after a dose of 1.59 dpa; (E) after introduction of double Frenkel pairs (2FP, with creation of either a divacancy or two isolated vacancies) to a dose of 0.45 dpa; and (F) quenched $CuTi_2$ liquid from 4000 K. Double Frenkel pairs were produced by moving either two nearest-neighbor atoms, 2FP (vac. cluster), or two random atoms, 2FP (random), to interstitial positions.

![](./images/812402998033514497_8.jpg)

Fig. 8. Volume dependence of the average shear moduli $C_{avg}$ and $C'$ in $CuTi$ and $Cu_4Ti_3$, calculated for three different processes: heating, atom exchanges and Frenkel-pair production.

from static atomic displacements. Consequently, the critical volume expansion at which the shear modulus vanishes during heating is substantially larger than that found for radiation-induced amorphization. However, the second result, *i.e.* the nearly factor-of-two decrease in the shear constant when the c-a transition occurs, is not surprising. It is, in fact, in good agreement with the elastic softening observed experimentally in the three compounds $FeTi$, $Nb_3Ir$ and $Zr_3Al$ during $Kr^+$ ion irradiation [2]. Furthermore, large differences in the shear moduli of the crystalline and amorphous materials have also been measured [31-36] and esti- mated from theoretical considerations [37-39].

### 3.3. Generalized Lindemann criterion for amorphization
The faster decrease of the average shear modulus $C_{avg}$ of the structurally disordered crystal with increasing volume expansion, relative to that of the perfect crystal during heating, can be interpreted in terms of a gen- eralization of the Lindemann melting criterion [17,40].

The new interpretation of c-a transformations focuses on static atomic displacements as a measure of chemical and topological disorder in solids.

According to the original Lindemann melting criterion [41], an ideal crystal melts when the root-mean-square amplitude of thermal vibrations, $\langle\mu_{\mathrm{vib}}^{2}\rangle^{1/2}$, exceeds a critical value, $\langle\mu_{\mathrm{cri}}^{2}\rangle^{1/2}$, which is some critical fraction of the nearest-neighbor distance. For monatomic Debye solids, $\langle\mu_{\mathrm{vib}}^{2}\rangle^{1/2}$ scales linearly with temperature and with the inverse square of the Debye temperature; the Lindemann criterion is expressed as

$$
\langle\mu_{\mathrm{vib}}^{2}\rangle\longrightarrow\langle\mu_{\mathrm{cri}}^{2}\rangle\quad T\longrightarrow T_{\mathrm{m}}=\frac{Mk\theta^{2}}{9\hbar^{2}}\langle\mu_{\mathrm{cri}}^{2}\rangle\tag{1}
$$

where $M$ is the atomic mass, $k$ is the Boltzmann constant and $\theta$ is the Debye temperature of the *perfect* crystal. The predicted direct proportionality between the melting temperature and the square of the Debye temperature has been confirmed by existing experimental data on pure metals and ordered compounds [43].

For irradiated or chemically disordered alloys, where lattice imperfections such as Frenkel pairs and antisite defects can introduce a static component, $\langle\mu_{\mathrm{sta}}^{2}\rangle$, to the mean-square atomic displacement, the original Lindemann criterion should be applied to the total mean-square atomic displacement $\langle\mu_{T}^{2}\rangle$, [40]

$$
\langle\mu_{T}^{2}\rangle=\langle\mu_{\mathrm{vib}}^{2}\rangle+\langle\mu_{\mathrm{sta}}^{2}\rangle\tag{2}
$$

As a result, the defective crystal becomes unstable at a temperature $T_{\mathrm{ins}}^{\mathrm{d}}\ll T_{\mathrm{m}}$:

$$
T_{\mathrm{ins}}^{\mathrm{d}}=\frac{Mk\theta_{\mathrm{def}}^{2}}{9\hbar^{2}}\langle\mu_{\mathrm{cri}}^{2}\rangle\tag{3}
$$

with $\theta_{\mathrm{def}}$, the Debye temperature of the *defective* crystal, being related to $\theta$ by

$$
\theta_{\mathrm{def}}^{2}=\theta^{2}\left[1-\frac{\langle\mu_{\mathrm{sta}}^{2}\rangle}{\langle\mu_{\mathrm{cri}}^{2}\rangle}\right]\tag{4}
$$

Equations (3) and (4) represent a generalization of the Lindemann criterion for c-a transformations. In contrast to the original version, the Debye temperature of the defective solid and, consequently, its melting point at constant pressure are no longer constant; they now decrease linearly with increasing damage as measured by the mean-square static atomic displacement. Since the average shear modulus scales directly with the square of the Debye temperature for many metals and compounds [43], and since the increase in $\Delta V/V$ per unit mean-square displacement is smaller with static displacements than with vibrational displacements [44], eqn. (4) clearly shows that $C_{\mathrm{avg}}$ of the irradiated compound ($\langle\mu_{T}^{2}\rangle\approx\langle\mu_{\mathrm{sta}}^{2}\rangle$) decreases much faster with $\Delta V/V$ than that of an unirradiated compound subject to heating ($\langle\mu_{T}^{2}\rangle=\langle\mu_{\mathrm{vib}}^{2}\rangle$).

Finally, Okamoto and Meshii [2] have shown that the enthalpy of the disordered crystal becomes equal to that of its glassy state when their Debye temperatures become equal. As a result, during irradiation, the c-a transition is triggered when the average shear modulus of the *defective compound*, $C_{\mathrm{avg}}^{\mathrm{d}}$, becomes equal to that of the *amorphous state*, $C_{\mathrm{avg}}^{\mathrm{a}}$, i.e. when

$$
C_{\mathrm{avg}}^{\mathrm{d}}/C_{\mathrm{avg}}^{\mathrm{c}}=C_{\mathrm{avg}}^{\mathrm{a}}/C_{\mathrm{avg}}^{\mathrm{c}}=\theta_{\mathrm{a}}^{2}/\theta^{2}\tag{5}
$$

with $C_{\mathrm{avg}}^{\mathrm{c}}$ being the average shear modulus of the *crystalline, unirradiated compound*. Since the Debye temperatures of amorphous compounds, $\theta_{\mathrm{a}}$, are typically between 0.6 and $0.8\ \theta$ (see *e.g.* ref. 2 and references therein), it is expected, from eqn. (5), that $C_{\mathrm{avg}}^{\mathrm{d}}/C_{\mathrm{avg}}^{\mathrm{c}}\approx0.5$ when amorphization occurs.

## 4. Conclusions
(1) Radiation-induced amorphization of $\mathrm{Cu}_{4}\mathrm{Ti}$, $\mathrm{Cu}_{4}\mathrm{Ti}_{3}$, $\mathrm{CuTi}$ and $\mathrm{CuTi}_{2}$ was simulated using molecular dynamics in conjunction with embedded-atom potentials. Changes in the system energy, volume, pair-correlation function, atom projection, diffraction pattern and elastic constants were analyzed.

(2) It was found that, among these intermetallics, $\mathrm{Cu}_{4}\mathrm{Ti}_{3}$, $\mathrm{CuTi}$, and $\mathrm{CuTi}_{2}$ could be rendered amorphous by the creation of Frenkel pairs, but $\mathrm{Cu}_{4}\mathrm{Ti}$ could not, consistent with the behaviors observed experimentally during electron irradiation. The $\mathrm{Cu}_{4}\mathrm{Ti}$ compound, however, became amorphous when clusters of several Frenkel pairs were introduced, indicating that this compound may be amorphized by heavy-ion bombardment.

(3) The calculated damage doses required to render the compounds completely amorphous, and volume expansions after the c-a transition, are in general agreement with experimental observations.

(4) The average shear modulus of the defective crystal decreases much faster with volume expansion than that associated with heating. At the onset of amorphization, this elastic modulus drops by a factor of about 2, which is in good accord with experiment.

(5) Solid-state amorphization can be described as a disorder-induced melting process using a generalization of the Lindemann criterion.

## Acknowledgments
This work was supported by the US Department of Energy, Basic Energy Sciences-Materials Sciences, under contract W-31-109-Eng-38. It benefited from an allocation of computer time on the Cray system at the National Energy Research Supercomputer Center (Lawrence Livermore National Laboratory). One of us

(M.J.S.) was a Faculty Research Participant at Argonne National Laboratory under the auspices of the Division of Educational Programs, whose support is gratefully acknowledged.

## References

1 D. E. Luzzi and M. Meshii, *Res. Mechanica*, 21 (1987) 207.
2 P. R. Okamoto and M. Meshii, in H. Wiedersich and M. Meshii (eds.), *Science of Advanced Materials*, American Society for Metals, Metals Park, OH, 1990, pp. 33-98.
3 J. Koike, P. R. Okamoto, R. E. Rehn and M. Meshii, *J. Mater. Res.*, 4 (1989) 1143.
4 D. E. Luzzi, H. Mori, H. Fujita and M. Meshii, *Acta Metall.*, 34 (1986) 629.
5 P. R. Okamoto, L. E. Rehn, J. Pearson, R. Bhadra and M. Grimsditch, *J. Less-Common Met.*, 140 (1988) 231.
6 J. Koike, *Ph.D. Thesis*, Northwestern University, 1989.
7 J. Koike, P. R. Okamoto, R. E. Rehn and M. Meshii, *Mater. Res. Soc. Symp. Proc.*, 157 (1990) 777.
8 K. Maeda and S. Takeuchi, *Philos. Mag. B*, 52 (1985) 955.
9 H. Hsieh and S. Yip, *Phys. Rev. Lett.*, 59 (1987) 2760; *Phys. Rev. B*, 39 (1989) 7476.
10 Y. Limoge, A. Rahman, H. Hsieh and S. Yip, *J. Non-Cryst. Solids*, 99 (1988) 75.
11 S. Yip and H. Hsieh, in H. Wiedersich and M. Meshii (eds.), *Science of Advanced Materials*, American Society for Metals, Metals Park, OH, 1990, pp. 121-154.
12 C. Massobrio, V. Pontikis and G. Martin, *Phys. Rev. Lett.*, 62 (1989) 1142; *Phys. Rev. B*, 41 (1990) 10486.
13 M. J. Sabochick and N. Q. Lam, *Scripta Metall. Mater.*, 24 (1990) 565; *Mater. Res. Soc. Symp. Proc.*, 157 (1990) 265.
14 M. J. Sabochick and N. Q. Lam, *Phys. Rev. B*, 43 (1991) 5243.
15 M. J. Sabochick and N. Q. Lam, *Mater. Res. Soc. Symp. Proc.*, 201 (1991) 387.
16 R. Devanathan, N. Q. Lam, M. J. Sabochick, P. Okamoto and M. Meshii, *Mater. Res. Soc. Symp. Proc.*, 209 (1991) 231.
17 N. Q. Lam, M. J. Sabochick and P. R. Okamoto, *Proc. IEA Workshop on The Use of Molecular Dynamics in Modeling Radiation Effects and Other Nonequilibrium Phenomena*, 6-8 May 1991, La Jolla, CA, *Radiation Effects and Defects in Solids*, 1992, in press.

18 M. S. Daw and M. I. Baskes, *Phys. Rev. B*, 29 (1984) 6443.
19 D. J. Oh and R. A. Johnson, *J. Mater. Res.*, 3 (1988) 471.
20 M. S. Daw, M. I. Baskes and S. M. Foiles, personal com- munication, 1986.
21 M. J. Sabochick and S. Yip, *J. Phys. F*, 18 (1988) 1689.
22 J. R. Ray, M. C. Moody and A. Rahman, *Phys. Rev. B*, 32 (1985) 733.
23 J. F. Lutsko, *J. Appl. Phys.*, 65 (1989) 2991.
24 H. Mori, H. Fujita, M. Tendo and M. Meshii, *Scripta Metall.*, 18 (1984) 783.
25 D. E. Luzzi, H. Mori, H. Fujita, and M. Meshii, *Mater. Res. Soc. Symp. Proc.*, 51 (1985) 479.
26 R. Devanathan, N. Q. Lam, M. J. Sabochick, P. R. Okamoto and M. Meshii, *Mater. Res. Soc. Symp. Proc.*, 235 (1992) 539.
27 J. Pfluger and O. Meyer, *Solid State Commun.*, 32 (1979) 1143.
28 A. R. Sweedler, D. E. Cox and S. Moehlecke, *J. Nucl. Mater.*, 72 (1978) 50.
29 A. V. Mirmelshteyn, A. Ye Karlin, V. Ye Arkhipov and V. I. Voronin, *Phys. Met. Metall.*, 55 (1983) 67.
30 D. Wolf, P. R. Okamoto, S. Yip, J. F. Lutsko and M. Kluge, *J. Mater. Res.*, 5 (1990) 286.
31 M. F. Ashby, A. N. Nelson and R. M. A. Centamore, *Scripta Metall.*, 4 (1970) 715.
32 B. Golding, B. G. Bagley and F. S. L. Hsu, *Phys. Rev. Lett.*, 29 (1972) 68.
33 J. Logan and M. F. Ashby, *Acta Metall.*, 22 (1974) 1047.
34 M. D. Merz, R. P. Allen and S. D. Dahlgren, *J. Appl. Phys.*, 45 (1974) 4126.
35 J. J. Gilman, *Phys. Today, (May)*, (1975) 46.
36 C. P. Chou, L. A. Davis and R. Hasegawa, *J. Appl. Phys.*, 50 (1979) 3334.
37 D. Weaire, M. F. Ashby, J. Logan and M. J. Weins, *Acta Metall.*, 19 (1971) 779.
38 G. Knuyt, L. De Schepper and L. M. Stals, *J. Phys. F. 16* (1986) 1989.
39 G. Knuyt and L. M. Stals, *Philos. Mag. B*, 64 (1991) 299.
40 A. Voronel, S. Rabinovich and A. Kisliuk, *Phys. Rev. Lett.*, 60 (1988) 2402.
41 A. Lindemann, *Z. Phys.*, 11 (1910) 609.
42 J. M. Ziman, *Principles of the Theory of Solids*, Cambridge University Press, Cambridge, 1972, pp. 60-63.
43 G. Grimvall and S. Sjodin, *Phys. Scripta*, 10 (1974) 340.
44 N. Q. Lam, R. Devanathan, P. R. Okamoto and M. Meshii, to be published.