# The Magnetic and Configurational Properties of Tail-Like Polymer Chain with Ferromagnetic Ising Interaction

Zhihu WANG,¹ Yingcai CHEN,²·³ Chao WANG,²·³ and Mengbo LUO²,†

¹College of Information Engineering, Hangzhou Radio & TV University, Hangzhou 310012, China
²Department of Physics, Zhejiang University, Hangzhou 310027, China
³Department of Physics, Taizhou University, Taizhou 317000, China

(Received November 2, 2006; Accepted February 27, 2007; Published April 17, 2007)

## ABSTRACT:
The magnetic and configurational properties of tail-like polymer chain with nearest-neighbor ferromagnetic Ising interaction were studied by Monte Carlo method. The results show that the tail-like polymer chain has spontaneous magnetization at temperatures below the critical temperature $T_{c}$. Correspondingly, the collapse phase transition from a random coil structure to a tight sphere is also taken place at $T_{c}$. We found the surface does not play visible effect on the magnetization and energy at any temperature. However it affects the size of chains, such as the mean-square end-to-end distance $\langle R^{2}\rangle$ and mean-square radius of gyration $\langle S^{2}\rangle$. We also found that the number of monomers that are in contact with the surface increases with the decrease of temperature. [doi:10.1295/polymj.PJ2006147]

## KEY WORDS
Polymer / Tail-Like / Ising / Monte Carlo Simulation /

The magnetic properties of organic polymers had intrigued scientists since they were first reported in $1987.^{1}$ Many organic magnetic polymers had been synthesized. The magnetic polymers have covered from those containing metal ions, such as $[Fe(C_{5}Me_{5})_{2}][TCNE]$ (TCNE is tetracyanoethylene),² $V(TCNE)_{x}y(CH_{2}Cl_{2})$ with $x\sim2$ and $y\sim1/2,^{3}$ $Fe(thiazole)_{2}-Cl_{2},^{4}$ to purely organic-based materials, such as poly-BIPO (BIPO is 1,4-bis-(2,2,6,6-tetramethyl-4-oxy-4-piperidyl-oxyl)-butadiin),¹ p-NPNN (NPNN is 4-nitrophenyl nitronyl nitroxide),⁵ and recently carbon-based magnetic polymer.⁶ The ferromagnetic phase transition temperature of organic magnetic polymer varied widely from very low temperature $(\sim0.67\mathrm{~K})$ for p-NPNN⁵ to room temperature $(>350\mathrm{~K})$ for $V(TCNE)_{x}y(CH_{2}Cl_{2}).^{3}$ At the same time, much effort had been paid on the search for the origin of magnetism.⁵⁻¹⁰ It was discovered that the magnetism arises from the interaction among unpaired electron spins. For the material p-NPNN, for example, the theoretical calculation based on the one-dimensional (1D) Heisenberg ferromagnet model with nearest neighbor (NN) coupling was in well agreement with experiment.⁵ The flexibility, transparency, thin-film-forming ability, and low density will ensure the ferromagnetic polymers playing some important roles in technology.¹¹

Earlier theoretical study on the phase transition of linear magnetic polymer adopted an Ising model on a fixed self-avoiding walk (SAW) chain.¹²⁻¹⁴ The NN interactions between spins were considered, but the change of spatial configuration of SAW chain was neglected. A finite temperature phase transition was possible in the model.¹² Recently, a three-dimensional (3D) Ising chain model, where fluctuations of chain spatial configuration and spin configuration were taken into account, was proposed to study the phase transition of magnetic polymers.¹⁵⁻¹⁷ The model chain was a SAW chain with NN Ising interaction among monomers. It was found that the Ising chain model has spontaneous magnetization at low temperature and undergoes a collapse transition near the critical temperature.¹⁵,¹⁶

In the present work we investigated the behavior of a 3D Ising chain with one end grafted to a flat surface with dynamic Monte Carlo (MC) method. The end grafted chain was often called as tail-like chain.¹⁸⁻²⁰ They are useful for many applications, such as polymer compatibilizers, copolymer microphases, colloid stabilization, polymeric surfactants.¹⁸,²¹⁻²³ The property of adsorbed chain plays a key role in many technological and biological applications and has therefore attracted extensive studies experimentally and theoretically. In the model the NN Ising interactions between spins and dynamic of spatial configuration were considered. The effect of flat surface on properties of Ising chain was studied by comparing the properties of tail-like chain with that of free chain. Here the free chain referred to an Ising chain in the free space without surface restriction.

## MODEL AND SIMULATION METHOD

The chain model we considered is a SAW chain with NN Ising interaction. The chain is comprised of $n$ monomers on the simple cubic (SC) lattice. The

---
†To whom correspondence should be addressed (E-mail: luomengbo@zju.edu.cn).

Tail-Like Polymer with Ferromagnetic Ising Interaction

Hamiltonian of the system is
$$
H=-\sum_{i j} \frac{J}{2} \delta\left(r_{i j}-1\right) \sigma_{i} \sigma_{j}, \tag{1}
$$
where $J$ is the exchange energy and $\sigma_{i}= \pm 1$ the spin on the $i$th monomer. The delta function $\delta(r_{i j}-1)=1$ if the spatial distance $r_{i j}$ between two monomers $i$ and $j$ equals to 1 and $\delta(r_{i j}-1)=0$ if $r_{i j} \neq 1$. On the SC lattice, there are six NN sites $(r_{i j}=1)$ with vector set $\{(1,0,0)\}$ and its symmetries. In this work, we considered a polymer chain with ferromagnetic Ising interaction, i.e., $J>0$. Besides the Ising interaction, self-avoiding interaction between monomers was also taken into account by the requirement that no two monomers can share a common site.

A coarse-grained polymer chain model was used in this work. The polymer chain is comprised of $n$ identical monomers consecutively linked with fluctuating bond length that can be $1, \sqrt{2}$ or $\sqrt{3}$ on the SC lattice. $^{16,24,25}$ Each monomer occupies one site of the lattice. The bond between successive monomers along a chain can be taken from a set of 26 allowed bond vectors obtained from the set $\{(1,0,0),(1,1,0),(1,1,1)\}$ by symmetry operations of the SC lattice. In this model, the monomers do not correspond to specific atoms in a polymer but rather to small groups of atoms, and the bonds do not represent specific covalent bonds between two atoms but instead the linkages between monomers. Since there are six NN sites belong to the subset $\{(1,0,0)\}$, therefore the number of NN monomers of a monomer in this model can vary from 0 to 6.

As to the tail-like polymer chain, the flat surface was placed at $z=0$ and was assumed infinitely large and impenetrable to polymer monomers. The first monomer was put at site $(0,0,1)$ and was immobile forever, while all other monomers were forbidden to contact with the flat surface. The movement of the polymer chain was then restricted to the upper semi-infinite space.

The dynamic MC procedure contained two aspects: one was the change of spatial configuration and another was the update of spins. The change of spatial configuration started by choosing a monomer at random and attempted to move it one lattice spacing in one of the six randomly selected directions: $\pm x, \pm y, \pm z$. This trial move would be accepted if the following four conditions were satisfied: $^{16}$ (1) self-avoidance was obeyed, (2) the new bond vector still belonged to the allowed bond set, (3) two bonds did not intersect, and (4) the Boltzmann factor $\exp (-\Delta E / k_{\mathrm{B}} T)$ was greater than a random number uniformly distributed in the interval $(0,1)$, where $\Delta E$ was the change in energy due to the trial move. The fourth criterion, i.e., the Metropolis criterion, ensures that the system obeys Boltzmann statistics at a specific temperature. $^{26}$ In the simulation, we set the exchange energy $J=1$ and absorbed the Boltzmann constant $k_{\mathrm{B}}$. Therefore, the temperature is in the unit $J / k_{\mathrm{B}}$. To update the spins, we picked up a monomer randomly at first and then flipped the spin on it according to the Metropolis criterion described above for monomer movement. The time unit used in the work was MC step (MCS). One MCS includes $n$ monomer trial movement and $n$ trial spin flip.

Therefore the chain changed its configuration with time. However, to obtain two independent chain configurations one need to wait at least one correlation time $\tau$ because of the correlation between two successive configurations. In the present simulation we recorded an independent chain configuration with time interval $\Delta t=n^{2}.^{16,25}$ And we recorded 500 independent configurations at every temperature. Afterwards we decreased the temperature with a step $\Delta T$. The step $\Delta T$ was chosen as 0.05 near the critical temperature, while a slightly big value of $\Delta T$ was chosen away from $T_{\mathrm{c}}$. The simulation results were also averaged over 500 initial chain configurations. It was found the relaxation of spin is much faster than spatial configuration, $^{25}$ so our updating time interval was always enough for the spin configuration.

## RESULTS AND DISCUSSION

The order parameter for the phase transition was magnetization defined as the average spin per monomer,
$$
M=\frac{1}{n} \sum_{i=1}^{n} \sigma_{i}. \tag{2}
$$

Since the statistical averaged magnetization $\langle M\rangle$ roughly equals zero at zero field because of the symmetry of spin direction, we therefore used mean absolute magnetization $\langle|M|\rangle$ and mean square magnetization $\langle M^{2}\rangle$ instead. Figure 1 presents the magnetizations $\langle|M|\rangle$ and $\langle M^{2}\rangle$ for the linear tail-like and free

![](./images/811986017434206209_1.jpg)

Figure 1. The temperature dependence of the mean absolute magnetization $\langle|M|\rangle$ and mean square magnetization $\langle M^{2}\rangle$ of the tail-like and free polymer chains.

Polym. J., Vol. 39, No. 6, 2007

![](./images/811986017434206209_2.jpg)

**Figure 2.** Plot of mean energy per monomer $\langle E \rangle$ (a) and specific heat $C_v$ (b) vs. temperature $T$ for both tail-like and free chains.

polymer chains at different temperatures. It is clear that the surface plays minimal effect on the magneti- zation of Ising chain since no visible difference is found between these two chain models. Values $\langle|M|\rangle$ and $\langle M^2 \rangle$ are very small ($\langle M^2 \rangle$ is approximately 0) at high temperatures and tend to 1 at low tempera- tures. The temperature at which there is a steepest var- iation is defined as the critical temperature $T_c.^{17}$ With this definition, $T_c$ is about 1.30 for $n=300$ for both types of chain. Within a narrow range of temperature near $T_c$ both $\langle|M|\rangle$ and $\langle M^2 \rangle$ change very rapidly, in dicating a phase transition as that was described in Ref 16 for free 3D Ising chain model. We conclude that the surface does not affect the magnetic phase transition in the 3D Ising chain model.

The energy of system $H$ (eq 1) was calculated, too. Figure 2 presents the dependence of mean energy per monomer, $\langle E \rangle = \langle H \rangle /n$, on the temperature. We find that $\langle E \rangle$ is also not influenced by the restriction of the surface for the Ising chain, similar to that of mag- netizations $\langle|M|\rangle$ and $\langle M^2 \rangle$. The phase transition tem- perature $T_c=1.31$ can be also defined from the specific heat $C_v=\frac{\langle E^2 \rangle-\langle E \rangle^2}{k_B T^2}$. The specific heat of the system is also presented in Figure 2, where a maxi- mum at $T_c=1.31$ is found. Moreover, no obvious dif- ference is observed for the energy and specific heat between the tail-like chain and the free one. So we conclude that the surface does not affect the energy of Ising chain.

The physical parameters that denote the configura- tional size of the polymer chain can be mainly charac- terized by mean-square end-to-end distance $\langle R^2 \rangle$ and mean-square radius of gyration $\langle S^2 \rangle$. The values of $\langle R^2 \rangle$ and $\langle S^2 \rangle$ of the tail-like and the free Ising chains were calculated at different temperatures. Figure 3 presents the dependence of $\langle R^2 \rangle$ and $\langle S^2 \rangle$ on the tem perature for both chains. Both $\langle R^2 \rangle$ and $\langle S^2 \rangle$ decreases with decreasing temperature and they drop sharply around the phase transition temperature $T_c=1.31$. Such a sharp decrease in size was found to be a col- lapse transition of Ising chain and was attributed to the cooperation between magnetic and spatial config-uration. $^{16}$

![](./images/811986017434206209_3.jpg)

**Figure 3.** Mean-square end-to-end distance $\langle R^2 \rangle$ (a) and mean-square radius of gyration $\langle S^2 \rangle$ (b) vs. temperature $T$ for tail-like and free Ising chain.

![](./images/811986017434206209_4.jpg)

**Figure 4.** Plot of expansion factors $\alpha_R$ and $\alpha_S$ vs. temperature for Ising chain of length $n=300$.

We find $\langle R^2 \rangle$ and $\langle S^2 \rangle$ of tail-like chain are bigger than that of free chain. Since only the excluded vol- ume effect between surface and polymer chain was considered in the work, the increase in $\langle R^2 \rangle$ and $\langle S^2 \rangle$ reflects that the surface effectively produces a repul- sive effect on the tail-like chain. $^{27-29}$ The repulsive ef fect of flat surface was also characterized by two ex- pansion factors $\alpha_R=\langle R^2 \rangle_{TL}/\langle R^2 \rangle_F$ and $\alpha_S=\langle S^2 \rangle_{TL}/$ $\langle S^2 \rangle_F$, where subscripts 'TL' and 'F' represent tail-like chain and free chain, respectively. $^{19,27}$ The depend ence of expansion factors $\alpha_R$ and $\alpha_S$ on the tempera ture for chain length $n=300$ is presented in Figure 4. At high temperatures $T>T_c$, both $\alpha_R$ and $\alpha_S$ are big-

Tail-Like Polymer with Ferromagnetic Ising Interaction

![](./images/811986017434206209_5.jpg)

Figure 5. (Color online) Typical configurations of the Ising tail-like chain at temperatures $T = 1.5$, $1.35$, $1.3$ and $0.7$. Chain length $n = 300$. Red and blue spheres represent polymer segments with spin up and spin down, respectively. Grey net represents the flat surface.

ger than 1 but smaller than the asymptotic values $\alpha_{\rm R} = 1.32$ and $\alpha_{\rm S} = 1.07$ of SAW chain without Ising interaction. $^{19,27}$ This is because we used a finite long chain where the Ising interaction cannot be totally neglected at finite temperatures. While a SAW chain without Ising interaction corresponds to the Ising chain model at infinite high temperature. Near $T_{\rm c}$ the fluctuations of values $\alpha_{\rm R}$ and $\alpha_{\rm S}$ are quite large due to large thermal fluctuation near critical point. The variation of $\alpha_{\rm S}$ with temperature is very small: it decreases from about $1.04$ at $T = 1.8$ to $1.0$ at $T = 0.7$, indicating the effect of surface on $\langle S^2 \rangle$ decreases with the decrease of temperature. However, there is a large bulge in $\alpha_{\rm R}$ below $T_{\rm c}$: $\alpha_{\rm R}$ shows a sharp increase and then decreases with the decrease of temperature. That means the surface produces much stronger repulsive effect on another end monomer at temperature slightly below $T_{\rm c}$. In other words, the relative distance of two end monomers becomes larger at temperature slightly below $T_{\rm c}$.

Figure 5 presents several typical configurations of tail-like Ising chain at different temperatures. At temperatures higher than $T_{\rm c}$, the chain is an extended coil as shown in Figure 5a. Although the summation of spins $\sum_{i=1}^n \sigma_i$ is roughly equal to zero above $T_{\rm c}$, small spin clusters are clearly found. With decreasing temperature, the size of spin cluster increases and the configurational size of chain decreases. At temperatures far below $T_{\rm c}$, a sphere like chain configuration forms and almost all spins point to the same direction, as shown in Figure 5d. With the increase in the cluster size, the number of nearest neighbor, $N_{\rm nn}$, increases. Figure 6 presents the average number of nearest neighbor $\langle N_{\rm nn} \rangle$ at different temperatures for the tail-like Ising chain. At high temperature, $\langle N_{\rm nn} \rangle$ is about 1 which indicates a very loose configuration. Around the critical temperature, $\langle N_{\rm nn} \rangle$ goes up sharply from about 1 to about 3.5 at $T < 1.3$, indicating a sharp transition from a loose structure to a tight structure. And it increases smoothly with the decrease of temperature. At $T = 0.7$, $\langle N_{\rm nn} \rangle$ is about 4.7. Actually, we find a compact structure with roughly all spins point to the same direction (Figure 5d).

![](./images/811986017434206209_6.jpg)

Figure 6. Plot of the average number of nearest neighbor $\langle N_{\rm nn} \rangle$ vs. temperature $T$ for tail-like Ising chain of length $n = 300$.

![](./images/811986017434206209_7.jpg)

Figure 7. Plot of the average number of monomers in contact with the surface $\langle N_1 \rangle$ vs. temperature $T$ for tail-like Ising chain of length $n = 300$.

To further investigate the effect of surface on the tail-like chain, we had calculated the average number of monomers in contact with the surface $\langle N_1 \rangle$ for the tail-like chain. Here, a monomer that is on the first layer above the flat surface is named as a monomer in contact with the surface. Figure 7 presents the dependence of $\langle N_1 \rangle$ on temperature for chain length $n = 300$. At temperatures above $T_{\rm c}$, $\langle N_1 \rangle$ roughly remains a constant which is about 2.6. While at temperature below $T_{\rm c}$, $\langle N_1 \rangle$ grows with the decrease of temperature, indicating that more and more monomers contact with the surface. Therefore, we could expect that the surface will play more important role at lower temperature if one consider attractive interaction between surface and polymer. That had attracted much attention on this topic. $^{30-34}$

## CONCLUSION

The magnetic and configurational properties of the tail-like polymer chain with ferromagnetic Ising interaction were studied by dynamic Monte Carlo method. Magnetic phase transition from a disordered to an ordered spin arrangement state is observed. For the

Polym. J., Vol. 39, No. 6, 2007

chain of length $n=300$, the transition temperature $T_{\rm c}$ is estimated to be about 1.31. At $T_{\rm c}=1.31$, a collapse transition of spatial configuration is also observed. We conclude that the flat surface do not play obvious role on the magnetic property, energy as well as phase transition temperature. However, it does affect the spatial configuration at temperatures above or below $T_{\rm c}$. Both $\langle R^2\rangle$ and $\langle S^2\rangle$ of the tail-like chain are bigger than that of the free chain. And the expansion factors $\alpha_{\rm R}=\langle R^2\rangle_{\rm TL}/\langle R^2\rangle_{\rm F}$ has a large bulge below $T_{\rm c}$, indicating the surface produces much stronger repulsive effect on end monomer at temperature slightly below $T_{\rm c}$. The average number of monomers in contact with the surface $\langle N_1\rangle$ grows with the decrease of temperature below $T_{\rm c}$, therefore, we could expect that the surface will play more important role at low temperatures if one consider attractive interaction between surface and polymer.

Nevertheless, the reason why the magnetic properties are not affected by the flat surface is not clear from our MC simulation results. It deserves further investigation on this topic. However, two possible reasons can be derived from MC simulations: (1) there is only a little portion of monomers contacts with the surface above $T_{\rm c}$; and (2) the flat surface contacts with the surface of tight structure of chain below $T_{\rm c}$. Both of them roughly do not affect the magnetic interactions among monomers. We expect mean-field theory may be a good tool to investigate this topic.$^{15}$

An important point we should point out is that long-range attractive interactions, such as the tail part of van der Waals interactions among polymer segments, were not taken into account in our Ising chain model. Long-range attractive interactions will certainly play roles at low temperatures. So our results are mainly suitable for magnetic polymers with high ferromagnetic phase transition temperature or with weak long-range attractive interactions.

Acknowledgment. This work was supported by the National Natural Science Foundation of China under Grant No. 20674074 and 20204014.

## REFERENCES

1. Y. V. Korshak, T. V. Medvedeva, A. A. Ovchinnikov, and V. N. Spector, *Nature*, **326**, 370 (1987).
2. J. S. Miller, P. J. Krusic, A. J. Epstein, W. M. Reiff, and J. H. Zhang, *Mol. Cryst. Liq. Cryst.*, **120**, 27 (1985).
3. J. M. Manriquez, G. T. Yee, R. S. Mclean, A. J. Epstein, and J. S. Miller, *Science*, **252**, 1415 (1991).
4. M. James, *J. Phys. Chem. Solids*, **61**, 1865 (2000).
5. M. Takahashi, P. Turek, Y. Nakazawa, M. Tamura, K. Nozawa, D. Shiomi, M. Ishikawa, and M. Kinoshita, *Phys. Rev. Lett.*, **67**, 746 (1991).
6. A. Rajca, J. Wongsriratanakul, and S. Rajca, *Science*, **294**, 1503 (2001).
7. K. Nasu, *Phys. Rev. B: Condens. Matter Mater. Phys.*, **33**, 330 (1986).
8. K. L. Yao and L. Zhao, *Eur. Phys. J. B*, **14**, 411 (2000).
9. Z. B. Huang and H. Q. Lin, *J. Chem. Phys.*, **114**, 3284 (2001).
10. H. Genin and R. Hoffmann, *Macromolecules*, **31**, 444 (1998).
11. M. Pope and C. E. Swenberg, "Electronic Processes in Organic Crystal and Polymers," 2nd ed., New York, Oxford, 1999, pp. 1026-1080.
12. B. K. Chakrabarti, A. C. Maggs, and R. B. Stinchcombe, *J. Phys. A: Math. Gen.*, **18**, L373 (1985).
13. B. K. Chakrabarti and S. Bhattacharya, *J. Phys. A: Math. Gen.*, **18**, 1037 (1985).
14. M. Aertsens and C. Vanderzande, *J. Phys. A: Math. Gen.*, **25**, 735 (1992).
15. T. Garel, H. Orland, and E. Orlandini, *Eur. Phys. J. B*, **12**, 261 (1999).
16. M. B. Luo and J. H. Huang, *J. Chem. Phys.*, **119**, 2439 (2003).
17. M. B. Luo, *J. Chem. Phys.*, **124**, 34903 (2006).
18. S. T. Milner, *Science*, **251**, 905 (1991).
19. Y. C. Chen and M. B. Luo, *J. Zhejiang Univ. Sci.*, **6B**, 1130 (2005).
20. S. Metzger, M. Müller, K. Binder, and J. Baschnagel, *Macromol. Theory Simul.*, **11**, 985 (2002).
21. S. Alexander, *J. Phys. (Paris)*, **38**, 983 (1977).
22. P. G. de Gennes, *J. Phys. (Paris)*, **37**, 1445 (1976).
23. P. G. de Gennes, *Macromolecules*, **13**, 1069 (1980).
24. J. H. Huang and M. B. Luo, *Polymer*, **45**, 2863 (2004).
25. M. B. Luo and C. J. Qian, *Polymer*, **47**, 1451 (2006).
26. D. P. Landau and K. Binder, "A Guide to Monte Carlo Simulations in Statistical Physics," Cambridge, Cambridge University Press, 2000.
27. T. Tanaka, *Macromolecules*, **10**, 51 (1977).
28. W. L. Mattice and D. H. Napper, *Macromolecules*, **14**, 1066 (1981).
29. W. Gottstein, S. Kreitmeier, M. Wittkop, D. Göritz, and F. Gotsis, *Polymer*, **38**, 1607 (1997).
30. J. M. Hammersly, G. M. Torrie, and S. G. Whittington, *J. Phys. A: Math. Gen.*, **15**, 539 (1982).
31. E. Eisenriegler, K. Kremer, and K. Binder, *J. Chem. Phys.*, **77**, 6296 (1982).
32. H. Meirovitch and S. Livne, *J. Chem. Phys.*, **88**, 4507 (1988).
33. Y. C. Gong and Y. M. Wang, *Macromolecules*, **35**, 7492 (2002).
34. R. Descas, J.-U. Sommer, and A. Blumen, *J. Chem. Phys.*, **120**, 8831 (2004).