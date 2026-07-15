# Chemical state and diffusion behavior of hydrogen isotopes in liquid lithium-lead

Daisuke Masuyama $^{a,*}$, Takuji Oda $^{a}$, Satoshi Fukada $^{b}$, Satoru Tanaka $^{a}$

$^{a}$The University of Tokyo, Bunkyo-ku, Hongo, 7-3-1, 113-8656 Tokyo, Japan
$^{b}$Kyushu University, Higashi-ku, Hakozaki, 6-10-1 Fukuoka, Japan

---

## ARTICLE INFO

Article history:
Received 3 March 2009
In final form 23 October 2009
Available online 30 October 2009

## ABSTRACT

Hydrogen existing in liquid lithium-lead was modeled using first-principles molecular dynamics. The chemical state of hydrogen was analyzed based on the trajectory and charge of hydrogen, and the H-Li radial distribution function, as obtained from calculations. Results show that, in liquid lithium-lead, the charge state of hydrogen correlates with Li-H interatomic distance: it becomes close to $H^-$ because of a binding interaction of Li-H when the distance is short, whereas it becomes close to $H^0$ as a hydrogen atom dissolved in liquid lead when the distance is long. Additionally, it was observed that hydrogen dif-fuses in liquid lithium-lead with jumping from one site to another where the binding interaction of Li-H can be formed, which would be one of the main diffusion mechanisms.

© 2009 Elsevier B.V. All rights reserved.

---

### 1. Introduction

In fusion reactors, because the tritium used as a fuel does not exist naturally, it must be produced artificially. Lithium-containing materials will therefore be loaded into a fusion reactor blanket, and tritium will be produced using lithium-neutron nuclear reactions. Liquid lithium-lead eutectic (e.g. Li17Pb83) is regarded as a prom-ising candidate of tritium-breeding materials. For recovering tri-tium rapidly from liquid lithium-lead and establishing an efficient fuel cycle, understanding the nature of hydrogen isotopes such as the diffusion constant, solubility, and chemical state is important.

Among them, the diffusion constant has been determined through several experiments [1-3], which revealed that the diffu-sion constant of hydrogen isotopes in liquid lithium-lead (Li17Pb83) is greater than that in liquid lithium [4,5]. Furthermore, the solubility of hydrogen isotopes has been studied [6], revealing that solubility increases as the lithium composition increases in li-quid lithium-lead.

Nevertheless, the mechanisms of diffusion and solution of hydrogen isotopes have not been elucidated adequately. Many uncertainties remain in applying knowledge obtained from small-scale and short-term experiments to the design of fusion reactors. For understanding those mechanisms, it is necessary to consider precisely the chemical state of hydrogen isotopes such as charge state, binding state, and so on. One reason why the mech-anisms have not been clarified by previous experimental studies is that it is difficult for experiments to acquire information about the chemical state directly in molten materials.

Consequently, in this study, hydrogen existing in liquid lithium-lead was modeled using first-principles molecular dynam-ics (MD) with the intention of elucidating the chemical state of hydrogen in molten materials from an atomic scale. Moreover, the diffusion behavior of hydrogen was discussed based on the obtained information.

As presented in this Letter, all in Section 2, the calculation con-dition of first-principles MD used for this study and evaluation method of the chemical state are described. Then, the charge state of hydrogen and the H-Li radial distribution function, which were obtained from MD at 900 K, are explained in Section 3. The chem-ical state of hydrogen in liquid lithium-lead was estimated through comparison with results obtained for liquid lithium or li-quid lead. Furthermore, the diffusion behavior of hydrogen in li-quid lithium-lead was discussed. Finally, the Letter closes with Section 4, which presents concluding remarks.

### 2. Method and computational details

Liquid lithium-lead eutectic (Li6Pb30H), liquid lithium (Li54H), and liquid lead (Pb36H) were selected as calculation targets. The composition of Li6Pb30 is almost equivalent to that of Li17Pb83, which is regarded as a promising candidate for tritium-breeding materials because of its low melting point. A three-dimensional periodic boundary condition was adopted for each system. Hydro-gen, which is the lightest and therefore the most mobile among the three sorts of hydrogen isotopes (hydrogen, deuterium, tritium), was used to facilitate analyses of the diffusion behavior. In fact, the interest for fusion technology is not in the chemical states and diffusion behavior of hydrogen but in those of tritium. How-ever, the chemical states and diffusion mechanism of hydrogen, which are addressed in the present Letter, should be very similar

---

* Corresponding author. Fax: +81 3 5841 6970.
E-mail address: masuyama@flanker.q.t.u-tokyo.ac.jp (D. Masuyama).

0009-2614/$ - see front matter © 2009 Elsevier B.V. All rights reserved.
doi:10.1016/j.cplett.2009.10.079

to those of tritium because there is no significant difference in electronic structure between hydrogen and tritium.

Movement of hydrogen in those molten materials at 900 K was simulated using first-principles MD [7] with CASTEP code [8] based on density-functional theory (DFT) and the plane-wave pseudopotential approach. The GGA-PBE functional [9] and ultrasoft pseudopotentials were used: the number of electrons treated explicitly is 4 for a lead atom, 3 for a lithium atom, and 1 for a hydrogen atom. We tested $k$-point sampling and energy cutoff convergence for each system (Li6Pb30H, Li54H, and Pb36H). As a result of the convergence tests, Monkhorst-Pack grid [10] for $k$-point sampling was set to $2 \times 2 \times 2$ in all the systems, and the energy cutoff was set to 450 eV in Li6Pb30H and Li54H, and 270 eV in Pb36H, which converged energy differences to around 0.01 eV per system and forces to within $0.05 \, \text{eV} \, \text{\AA}^{-1}$ for each atom.

Regarding the simulation time, it is difficult to perform long-term simulation using first-principles MD. Therefore, if atomic positions of solid crystals are adopted as the initial configuration of liquid-state simulation, the vestige of the initial configuration remains strongly for a long time. In this study, each atom's position was initialized randomly under the following two conditions:

(i) Each interatomic distance is greater than $2.6 \, \text{\AA}$.
(ii) Each Li-Li distance is greater than $4.8 \, \text{\AA}$.

Condition (i) avoids a short interatomic distance. Condition (ii) makes lithium atoms exist separately.

First, for systems containing no hydrogen atom, the atomic positions were relaxed using MD under the NPT ensemble [11] at 0 Pa and 900 K for 500 fs with the time step of 2 fs. In addition, the equilibrium lattice constants were determined approximately in this run: $11.00 \, \text{\AA}$ for Li54, $10.93 \, \text{\AA}$ for Li6Pb30, and $10.68 \, \text{\AA}$ for Pb36. The lattice constants estimated from densities reported in previous works are $10.9 \, \text{\AA}$ for Li54 ($0.476 \, \text{g/cm}^3$ for liquid lithium [12]) and $10.5 \, \text{\AA}$ for Li6Pb30 ($8.94 \, \text{g/cm}^3$ for liquid Li17Pb83 [13]). Although the calculation value for Li6Pb30 is overestimated by 3.94%, we judged that it was within a permissible range. A hydrogen atom was then introduced to these systems. For Li6Pb30, we performed four simulations with different initial locations of a hydrogen atom, in order to improve the statistics. In each simulation, a hydrogen atom was put near a lithium atom. One of the initial configurations of Li6Pb30H is presented in Fig. 1. In these systems, the hydrogen behavior was simulated under the NVT ensemble at 900 K. The lattice constants were fixed at $11.00 \, \text{\AA}$ for Li54H, $10.93 \, \text{\AA}$ for Li6Pb30H, and $10.68 \, \text{\AA}$ for Pb36H, which were determined approximately in the previous NPT run. The time step was set to 1 fs. By a test calculation for 50 fs, we confirmed that configurations obtained with 1 fs time step was almost the same with those with 0.5 fs time step. The total time step was set to 1000 fs for liquid lithium-lead, and 750 fs for liquid lithium and liquid lead.

Time changes of the charge state of hydrogen and the interaction between atoms were extracted from the obtained trajectory of hydrogen. The calculation results up to 250 fs were not used to reduce the influence of the initial configuration. The charge states of hydrogen in Li6Pb30H, Li54H and Pb36H were estimated using Mulliken population analysis [14]. In addition, LiH crystal was also analyzed for comparison. Because the plane-wave basis set is not a localized basis set, the CASTEP code projects the optimized plane-wave states onto a Linear Combination of Atomic Orbitals (LCAO) basis that is set to execute the population analysis. For the population analysis, Monkhorst-Pack grid [10] for $k$-point sampling was set to $2 \times 2 \times 2$ in all the systems, and the energy cutoff was set to 330 eV in Li6Pb30H, Li54H and LiH crystal, and 290 eV in Pb36H, which converged Mulliken population to within 0.01 e for each atom.

![](./images/811825716394983424_1.jpg)

Fig. 1. Initial configuration of liquid lithium-lead containing hydrogen (Li6Pb30H).

## 3. Results and discussion

### 3.1. Trajectory of hydrogen

In first-principles MD simulations of Li6Pb30H, hydrogen generally took the following three states:

(a) Neighboring to a lithium atom.
(b) Neighboring to two lithium atoms.
(c) Remaining distant from lithium atoms, and surrounded by lead atoms.

![](./images/811825716394983424_2.jpg)

Fig. 2. The configurations of three discriminative states of hydrogen in Li6Pb30H: (a) neighboring to a lithium atom, (b) neighboring to two lithium atoms, and (c) remaining distant from lithium atoms, and surrounded by lead atoms.

Typical examples of these states are presented in Fig. 2, and the time changes of Li–H distances in one of four simulations are depicted in Fig. 3. The time span of the state (a), (b) and (c) are respectively about 270 fs (250–350 fs, 480–650 fs), 350 fs (650–1000 fs) and 130 fs (350–480 fs) in Fig. 3. The sum of each time span over four simulations was 2380 fs for (a), 490 fs for (b) and 130 fs for (c). It is considered that the time spans of the state (a) and (b) are longer than that of the state (c) because hydrogen is stabilized as a result of binding interaction of Li–H when remaining near a lithium atom. Although it is better to compare average potential energies of these three states for confirmation, adequate statistics could not be achieved in the present simulation.

It should be noted that three lithium atoms did not neighbor to a hydrogen atom at the same time, although a lithium atom ($\text{Li}_\text{D}$) once approached to a hydrogen atom neighboring to two lithium atoms ($\text{Li}_\text{B}$, $\text{Li}_\text{C}$), as seen around 850–950 fs in Fig. 3. Furthermore, a configuration in which three lithium atoms neighbor to a hydrogen atom did not appear throughout the four simulations of liquid lithium–lead. It could be suggested that such a configuration is energetically unfavorable, although a more long-term simulation is needed to conclude it. If this is the case, one possible reason is that repulsive interactions arise among lithium atoms neighboring to hydrogen. Mulliken population of lithium atoms neighboring to hydrogen was 2.92 (the average of 100 data), and that of lithium atoms remaining distant from hydrogen was 3.00 (the average of 525 data). Whether the number of lithium atoms neighboring to the same hydrogen atom is one or two, the average population was 2.92. It is indicated that lithium atoms neighboring to hydrogen are positively charged, which would cause repulsive interactions among them and thus would restrain the number of lithium atoms neighboring to the same hydrogen atom.

### 3.2. Hydrogen charge

Time changes of the Mulliken population of hydrogen in liquid lithium–lead, liquid lithium and liquid lead are presented in Fig. 4. Population analysis was performed once per 10 fs over 750 fs (250–1000 fs) for liquid lithium–lead, and over 250 fs (250–500 fs) for liquid lithium and liquid lead. The solid red line expresses the population in LiH crystal (1.41 e). In LiH crystal, hydrogen is generally thought to exist as $\text{H}^-$. Such a charge state was evaluated as 1.41 e using this Mulliken population analysis. The value of the Mulliken population depends on LCAO basis sets, and physical signification of the absolute value is not definite. Consequently, 1.41 e of the population was thought to correspond to the charge of $\text{H}^-$ state in the present condition. According to this criterion, the charge state of hydrogen in each molten material was investigated.

![](./images/811825716394983424_3.jpg)

Fig. 4. Time changes of Mulliken populations of hydrogen in molten materials at 900 K together with the population in solid LiH crystal. The black dashed line and green dotted line show the average values of the Mulliken populations of 250–500 fs in liquid lithium and liquid lead, respectively.

The Mulliken population of hydrogen in liquid lithium is close to the population in LiH crystal, which indicates that the charge state of hydrogen is close to $\text{H}^-$ in liquid lithium. The population in liquid lead is about 1.2 e, which is far from that in LiH crystal. Because no characteristic binding interaction is expected between a lead atom and a hydrogen atom, the charge state of hydrogen is regarded as $\text{H}^0$. Therefore, the value of 1.2 e is expected to correspond to $\text{H}^0$ state. In liquid lithium–lead, the population was around an intermediate value between in liquid lithium and in liquid lead.

For further discussion related to the charge state of hydrogen in liquid lithium–lead, the Mulliken population of hydrogen and the nearest Li–H interatomic distance were compared for 250–1000 fs in Fig. 5. For 250–350 fs and for 480–1000 fs, the population is large and the nearest Li–H interatomic distance is short. However, for 350–480 fs, the population is small and the distance is long. Consequently, it was considered that the charge state of hydrogen in liquid lithium–lead correlates with the nearest Li–H interatomic distance; it becomes close to $\text{H}^-$ because of a binding interaction of Li–H when the distance is short, although it becomes

![](./images/811825716394983424_4.jpg)

Fig. 3. Time changes of Li–H distances in liquid lithium–lead at 900 K. Two lithium atoms that remained distant from the hydrogen atom were excluded.

![](./images/811825716394983424_5.jpg)

Fig. 5. Time changes of Mulliken population of hydrogen and the nearest Li–H interatomic distance in liquid lithium–lead.

close to $\text{H}^0$ as hydrogen solving in liquid lead when the distance is long. In order to confirm this correlation, Mulliken populations of hydrogen are plotted as a function of the nearest Li-H interatomic distance in Fig. 6. The populations were obtained from the population analysis over 750 fs (250-1000 fs). It was confirmed that the shorter the nearest Li-H interatomic distance is, the larger the Mulliken population is, and vice versa. Furthermore, hydrogen generally has a larger population in the state (b) than in the state (a). It is noteworthy, however, that the population is around 1.3 e, even when the binding interaction of Li-H is formed. This value is smaller than that in LiH crystal or liquid lithium (around 1.4 e), which indicates that the binding interaction of Li-H in liquid lithium-lead is weaker than the conventional Li-H bond. The weakening is attributed to the influence from circumjacent free electrons.

### 3.3. H-Li radial distribution function

The H-Li radial distribution functions in liquid lithium-lead and liquid lithium obtained by first-principles MD are portrayed in Fig. 7. The sampling was performed once per 1 fs over 3000 fs (250-1000 fs in four simulations) for liquid lithium-lead and 500 fs (250-750 fs) for liquid lithium. The horizontal axis expresses the distance from hydrogen, and the vertical axis expresses the probability density of lithium atoms. In both liquid lithium-lead and liquid lithium, the probability density peaks at around $1.75$ Å, which corresponds to the Li-H interatomic distance when the binding interaction of Li-H is formed in the case of liquid lithium-lead. This value ($1.75$ Å) is close to the Li-H bond distance in LiH crystal ($1.99$ Å) [15] or a gaseous LiH molecule ($1.59$ Å) [16]. Consequently, hydrogen is thought to bind to a lithium atom with the binding interaction of Li-H. This discussion is supported also from results related to the charge state of hydrogen in Section 3.2.

### 3.4. Li-H vibration

To validate the difference between the properties of the binding interaction of Li-H in liquid lithium-lead and an ordinary Li-H interaction, as observed in a gaseous LiH molecule, frequencies of the Li-H vibration were estimated. With respect to the Li-H frequency in liquid lithium-lead, we focused on variation of the Li-H distance when hydrogen stays near a lithium atom. In each of the four simulations of liquid lithium-lead, the frequency was evaluated to be $1.8 \times 10^{13}\ \text{s}^{-1}$ ($600\ \text{cm}^{-1}$), $2.0 \times 10^{13}\ \text{s}^{-1}$ ($670\ \text{cm}^{-1}$), $2.2 \times 10^{13}\ \text{s}^{-1}$ ($730\ \text{cm}^{-1}$) and $2.6 \times 10^{13}\ \text{s}^{-1}$ ($870\ \text{cm}^{-1}$), respectively. Because the frequency of the state (a) seemed to be comparable with that of the state (b), they were not separately evaluated.

![](./images/811825716394983424_6.jpg)

Fig. 6. Correlation between Mulliken population of hydrogen and the nearest Li-H interatomic distance in liquid lithium-lead.

![](./images/811825716394983424_7.jpg)

Fig. 7. H-Li radial distribution functions in liquid lithium and liquid lithium-lead at 900 K.

The frequency in a gaseous LiH molecule is $4.08 \times 10^{13}\ \text{s}^{-1}$ ($1360\ \text{cm}^{-1}$) [17], which is greater than that in liquid lithium-lead (around $2 \times 10^{13}\ \text{s}^{-1}$). These results suggest that the binding interaction of Li-H in liquid lithium-lead is weaker than ordinal Li-H interaction. In Section 3.2, it was verified that the minus charge of hydrogen is smaller than that in LiH crystal or liquid lithium, even when the binding interaction of Li-H is formed in liquid lithium. The Li-H bond is characterized by strong ionicity. Therefore, the weakening because of the reduction of the minus charge is reasonable.

### 3.5. Diffusion behavior of hydrogen

It was verified from MD at 900 K that the binding interaction of Li-H is formed between lithium and hydrogen. In addition, hydrogen generally can take the following three states: (a) neighboring to a lithium atom with binding to it, (b) neighboring to two lithium atoms with binding to them, and (c) remaining distant from lithium atoms, and surrounded by lead atoms. It was also indicated that hydrogen is stabilized near a lithium atom more than in the cloud of lead atoms. Based on these results, we propose the following diffusion processes of hydrogen in liquid lithium-lead.

First, hydrogen is trapped by a lithium atom because of the binding interaction of Li-H; it drifts near the lithium atom. Subsequently, hydrogen breaks the interaction at a certain moment, and moves into the cloud of lead atoms. Here, the attempt frequency for breaking the interaction is regarded as the frequency of the Li-H vibration in liquid lithium-lead ($1.8$-$2.6 \times 10^{13}\ \text{s}^{-1}$), as estimated in Section 3.4. As verified in Section 3.1, the duration of the state (c) is short. Therefore, it is considered that hydrogen can migrate rapidly in the cloud of lead atoms. Then, hydrogen gets to another or the same lithium atom, and the binding interaction of Li-H is formed again. Repeating these processes, hydrogen diffuses in liquid lithium-lead.

In Fig. 8, time changes of the nearest Li-H distance and the displacements of a hydrogen atom and lithium atoms are shown. The results of Figs. 3 and 8 were derived from the same MD simulation. When the Li-H interaction was broken (around 350 fs) or rebuilt (around 450 fs), not the lithium but the hydrogen moved largely. In addition, hydrogen did not largely move when the Li-H interaction was maintained. These observations support the proposed diffusion model.

Based on the present diffusion model, the rate-determining process of hydrogen diffusion in liquid lithium-lead should be the breaking process of the binding interaction of Li-H. In this case, the experimental values of the apparent activation energy of

![](./images/811825716394983424_8.jpg)

Fig. 8. Time changes of the nearest Li-H distance and the displacements of a hydrogen atom and lithium atoms. The notation of lithium atoms (Liₐ, Liᵦ, and Liᶜ) is identical with that in Fig. 3.

hydrogen diffusion [1-3] (0.120-0.280 eV) can be regarded as the energy for breaking the interaction. These values are smaller than the apparent activation energy of hydrogen diffusion in liquid lith- ium (1.08 eV [4], 1.68 eV [5]) or the bond dissociation energy of LiH molecule (2.42 eV [16]). As discussed above, this tendency reflects the fact that the binding interaction of Li-H in liquid lithium-lead is weaker than that in LiH molecule because of circumjacent free electrons.

Although the proposed model would correspond to one of the main diffusion mechanisms of hydrogen in liquid lithium-lead, there could be other mechanisms that did not appear in the pres- ent simulations. For example, in the present MD simulations, diffu- sion of hydrogen binding to two lithium atoms was not clearly observed. We suggest that diffusion of such hydrogen is induced by moving away of one of the two lithium atoms from the hydro- gen atom (namely, transition from the state (b) to (a)) or by mov- ing away of the hydrogen atom from the two lithium atoms (transition from the state (b) to (c)); however, it cannot be con- cluded in the present Letter. Moreover, interaction between multi- ple hydrogen atoms, interaction between multiple lithium atoms, and interaction of hydrogen with more than two lithium atoms were not handled. To address these topics, a more long-term sim- ulation with a greater number of atoms is needed, which is a sub- ject for future study.

## 4. Conclusions
The chemical state of hydrogen in liquid lithium-lead was esti- mated using first-principles molecular dynamics. Results show that the charge state of hydrogen becomes close to $H^{-}$ and a bind ing interaction of Li-H is formed when hydrogen exists near one or two lithium atoms. Results further showed that the charge state becomes $H^{0}$ and hydrogen solves in liquid lead when the Li-H interatomic distance is long. In addition, the diffusion behavior of hydrogen in liquid lithium-lead was discussed based on these re- sults. Hydrogen in liquid lithium-lead is stabilized near a lithium atom by this binding interaction of Li-H. After breaking the inter- action at a certain moment, hydrogen moves into the cloud of lead atoms and migrates for a short time; subsequently, it binds to an- other or the same lithium atom. It was proposed as one of the main diffusion mechanisms that hydrogen diffuses in liquid lithium- lead with repetition of such processes.

## References
[1] F. Reiter, Fusion Eng. Des. 14 (1991) 207.
[2] Y. Maeda, Y. Edao, S. Yamaguchi, S. Fukada, et al., Fusion Sci. Technol. 54 (2008)131.
[3] T. Terai, S. Nagai, T. Yoneoka, Y. Takahashi, J. Nucl. Mater. 187 (1992) 247.
[4] R.M. Alire, J. Chem. Phys. 65 (1976) 1134.
[5] S. Fukada, M. Kinoshita, K. Kuroki, T. Muroga, J. Nucl. Mater. 346 (2005) 293.
[6] S. Fukada, Y. Edao, Y. Maeda, T. Norimatsu, Fusion Eng. Des. 83 (2008) 747.
[7] R. Car, M. Parrinello, Phys. Rev. Lett. 55 (1985) 2471.
[8] V. Milman, B. Winkler, J.A. White, et al., Int. J. Quantum Chem. 77 (2000) 895.
[9] J.P. Perdew, K. Burke, M. Ernzerhof, Phys. Rev. Lett. 77 (1996) 3865.
[10] J.D. Pack, H.J. Monkhorst, Phys. Rev. B 16 (1977) 1748.
[11] H.C. Andersen, J. Chem. Phys. 72 (1980) 2384.
[12] R.W. Ohse (Ed.), Handbook of Thermodynamic and Transport Properties of Alkali Metals, Intern. Union of Pure and Applied Chemistry Chemical Data Series No. 30, Blackwell Scientific Publ., Oxford, 1985, p. 987.
[13] B. Schulz, Fusion Eng. Des. 14 (1991) 199.
[14] R.S. Mulliken, J. Chem. Phys. 23 (1955) 1833.
[15] S. Nagakura, Iwanami Physical and Chemical Science Dictionary, Fifth edn.,1998.
[16] D.H. Lide, Handbook of Chemistry and Physics, 84th edn., 2003.
[17] M. Elstner et al., Phys. Rev. B 58 (1998) 7260.