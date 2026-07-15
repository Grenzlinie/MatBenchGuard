# Atomistic Theory of Bulk Metallic Glass Formation

T. Egami

Department of Materials Science and Engineering and Laboratory for Research
on the Structure of Matter, University of Pennsylvania, Philadelphia, PA 19104, USA
and Lujan Center for Neutron Scattering, LANSCE, Los Alamos National Laboratory,
Los Alamos, NM 87545, USA

## ABSTRACT

Bulk metallic glass can be formed only when the critical cooling rate for glass formation
is reduced to $10^{0-2}$ K/sec. However, a cooling rate achievable with molecular dynamics simula-
tion is higher by many orders of magnitude, so the gap has to be abridged by analytical theories.
We propose a theory of bulk metallic glass formation based upon our early theories of glass for-
mation composition. The critical concepts include the idea of local glass transition, distributed
local glass transition temperatures and coincident local fluctuation for atomic transport. Strong
repulsion between small atoms was recognized for the first time as the necessary condition for
bulk glass formation.

## INTRODUCTION

Recent development of bulk metallic glasses [1-3] has brought the field of metallic
glasses back in the limelight as in the 70's and 80's. While metallic glasses studied in the earlier
times are binary or ternary glasses, bulk metallic glasses contain many more elements. This
complexity makes it even more difficult to find the scientific basis for bulk metallic glass forma-
tion, while there are a number of empirical principles. In general it is not easy to formulate a
theory of glasses because of their statistical, many-body nature of the problem. It is hard even to
define the structure of a glass precisely and determine it by experiment.

We had earlier some success in explaining the composition limits of metallic glass forma-
tion [4]. For a binary glass, the minimum composition of a solute B in the matrix of A, $c_{B}^{min}$,
was found to be,

$$
c_{B}^{\min }=0.1 \frac{\langle V\rangle}{\Delta V} \tag{1}
$$

where $\Delta V=|V_{A}-V_{B}|$, $<V>$ is the compositionally averaged atomic volume. Some of the reasons
for the success of this approach are the following:

1. It is not based upon the comparison of the free energies.
2. We did not try to describe the structure nor state of the glass.
3. The glass (liquid) was regarded as the default state, when crystallization fails to occur.
Thus we focused on the condition that a simple crystal alloy structure becomes unstable.
4. The condition was formulated purely on the geometrical basis, without any reference to
electronic states nor atomic bonding.

This theory was later extended to account for the melting of a crystal, glass transition, and solid-state amorphization [5], and more recently to explain bulk metallic glass formation [6] and atomic transport in metallic glasses [7]. In the following we summarize the basic premises, recent progress and future prospects.

# LOCAL TOPOLOGICAL INSTABILITY

The central idea of this theory is that for a given local condition there is a critical stress threshold beyond which the local structure changes its topology. Here topology is defined in terms of connectivity of atoms being the nearest neighbors. The critical volume strain is determined through the dependence of the number of nearest neighbors, or the local coordination number, $N_C$, on the atomic radius. If the atom A is embedded in the liquid or glass matrix of element B, the local coordination number of A, $N_C^A$, is small when the radius ratio, $x = r_A/r_B$, is small, and it grows with $x$. For a system with short-range interatomic potentials it is given by,

$$
N_{C}^{A}(x)=4 \pi\left[1-\frac{\sqrt{3}}{2}\right]\bigg/\left[1-\frac{\sqrt{x(x+2)}}{x+1}\right] \tag{2}
$$

![](./images/811672608259964928_1.jpg)

Fig. 1 Local free energy as a function of the atomic size, $x = r_A/r_B$.

This equation gives a continuous value of $N_C^A$ as a function of $x$. But the coordination number is an integer, so only at special values of $x = x_0(N_C^A)$, does eq. (2) agree with the actual coordination number. When the integral value of $N_C^A$ is different from (2), there will be local strains, and the local elastic energy associated with them. Thus the local free energy must be a nearly periodic function, with minima at $x = x_0(N_C^A)$ (Fig. 1). If $x$ is continuously increased, the free energy will increase, but when the maximum is reached the value of $N_C^A$ will quickly change to the one at the next minimum. Thus the amount of change in $x$ that is needed to bring about the change in $N_C^A$ is given by,

$$
\Delta x_{C}=\frac{1}{2}\bigg/\frac{\partial N_{C}^{A}(x)}{\partial x}=\frac{1}{4 \pi} \frac{\left(x+1-\sqrt{x(x+2)}\right)^{2} \sqrt{x(x+2)}}{2-\sqrt{3}}. \tag{3}
$$

From this we obtain the critical uniform volume expansion for local topological instability, $\varepsilon_{V}^{crit}$,

$$
\varepsilon_{V}^{c r i t}=\frac{3 \Delta x_{C}}{2 x}. \tag{4}
$$

Fig. 2 shows the value of $\varepsilon_{V}^{crit}$ as a function of $x$. Clearly as $x$ decreases $\Delta x_C$ becomes sharply increased. Since a small atom has a fewer neighbors, the critical volume expansion for instability also is large. For $x = 1$,

$$
\varepsilon_{V}^{crit} = \frac{6\sqrt{3}-9}{8\pi} = 0.0554 \tag{5}
$$

This value compares well with the result of computer simulation [8]. The condition of local topological instability (5) led to the expression for the glass transition temperature,

$$
\begin{aligned}
T_{g} &= \frac{2\Omega K}{k_{B}} \left(\varepsilon_{V}^{crit}\right)^{2} \\
&= 6.14\times10^{-3} \frac{\Omega K}{k_{B}}
\end{aligned} \tag{6}
$$

where $\Omega$ is the atomic volume, $K$ is the bulk modulus and $k_{B}$ Boltzmann's constant. For instance for $\text{Fe}_{80}\text{B}_{20}$ this gives $\text{T}_\text{g} = 652$ K, which compares well with the experimental value of 660 K.

![](./images/811672608259964928_2.jpg)

Fig. 2 The critical value of uniform expansion strain as a function of the atomic size ratio, $x$.

# CONDITIONS FOR BULK METALLIC GLASS FORMATION

The key to obtaining a bulk metallic glass is a low crystallization rate in the supercooled liquid, thus low diffusivity in the melt. We suggest that if glass transition occurs *locally* over a wide range of temperature the viscosity of the melt will gradually increase far above the global glass transition temperature, and glass formation becomes much easier [6]. The condition (4) applies locally to each atom. Thus a small atom surrounded by large atoms has a high value of critical strain as shown in Fig. 2, and thus its environment becomes frozen at a temperature higher than the overall glass transition temperature. We therefore propose that distributed local freezing temperature increases the viscosity of the melt, and makes glass formation easier.

It became immediately obvious that the possibility of a small atom having other small atoms as neighbors reduces the local $T_{g}$, and viscosity. Thus it is important that small atoms repel each other in the alloy in order for glasses to form easily. This condition is indeed satisfied in metallic glasses; for instance in transition metal (TM)-metalloid (M) glasses charge transfer from M to TM makes M-M potential repulsive. When the repulsion among the small atoms was assumed the local glass transition temperature of the minor constituent smaller atom depends strongly on the atomic size ratio, $x$, as shown in Fig. 3 [6].

These considerations led to four principles for obtaining bulk metallic glasses:
1. Increase the atomic size ratio of the constituent elements.
2. Increase the number of elements involved.
3. Increase the interaction between the small and large atoms.
4. Introduce repulsive interaction between small atoms.

While the conditions 1-3 are generally recognized, the condition 4 is a novel one. These conditions can easily be extended for ternary and more complex alloy systems. For ternary glasses with small and large solutes, such as Al-TM-RE (RE: rare earths), the potential between small atom (TM) and large atom (RE) has to be repulsive. Even though TM and RE form strong intermetallic compounds and their heat of association is negative, the presence of aluminum makes all the difference. Both TM and RE form strong chemical bonds with Al with charge transfer, and develop an electron excess. This must be the reason why the TM-RE interaction is repulsive.

# ATOMIC TRANSPORT IN METALLIC GLASSES

The leading concept in the study of diffusion in metallic glasses has been the idea of "free volume" by Cohen and Turnbull [9-11]. In this theory diffusion occurs when a free volume large enough to accept an atom opens up by statistical fluctuation. The volume of the free volume element is estimated to be about 80% of the atomic volume. This theory is essentially an extension of the vacancy diffusion mechanism in crystalline metals. However, recent studies by isotope diffusion [12] and molecular dynamics simulation [13] suggest that the real diffusion process in metallic glasses is more collaborative, many atoms moving by a small amount each, and is very different from the single atom hopping process in crystalline solids.

Based upon the principle of local topological instability a theory of atomic transport was developed

![](./images/811672608259964928_3.jpg)

Fig. 3 Local glass transition temperature of metalloid, $T_{g}^{M}$, compared to that of the transition metal, in TM₈₀M₂₀ glass, as a function of the atomic size ratio $x = r_M/r_{TM}$ [6].

![](./images/811672608259964928_4.jpg)

Fig. 4 Bond-exchange process for diffusion, from left to right. As the atoms 1 and 2 form a bond, the bond 3-4 is cut.

[7]. In this theory the fundamental process for atomic transport is the nearest neighbor bond-exchange as shown in Fig. 4. In Fig. 4, as the new bond 1-2 is formed the bond 3-4 is cut. As a result the system undergoes a shear transformation. The existence of such bond-exchange process was experimentally confirmed by x-ray diffraction study of anelastically deformed metallic glass ribbons [14]. After anelastic creep deformation the atomic pair-density function (PDF) became anisotropic, suggesting a higher density of atomic bonds in the direction perpendicular to the applied stress. This point may appear the other way around, but as seen in Fig. 4, anelastic deformation produces more bonds in the direction perpendicular to the direction of deformation. The atomic movements by this process are only a small fraction of the atomic distance at a time. Our theory catches this collective aspect very well; the magnitude of the critical volume fluctuation for a change in the local topology is given by equation (4), thus amounts only to $6-8$ % of the atomic volume. Without forming a large free volume equivalent to a vacancy, diffusion can occur in glasses. Actually the concept of a single atomic jump over the interatomic distance is closely tied to the lattice periodicity, and in the absence of periodicity the distance of atomic motion does not have to be equal to the interatomic distance. For supercooled liquid the activation energy for diffusion is given by,

$$
E_{a}(S L)=\Omega K(1+7 f(T))\left(\left(\varepsilon_{V}^{c r i t}\right)^{2}+\frac{6}{5}\left(\varepsilon_{S}^{c r i t}\right)^{2}\right)=0.039(1+7 f(T)) \Omega K
\tag{7}
$$

where $f(T)$ is the fraction of atoms that are frozen, or below the local glass transition temperature. At the glass transition, $f(T_{g})=1$, but at higher temperatures $f(T)$ goes down. However, if many elements remain frozen above $T_{g}$, the value of $f(T)$ will decrease only slowly with temperature, increasing the viscosity of the melt. Thus increasing the fraction of elements with high values of local $T_{g}$ is the key for forming bulk metallic glasses. This conclusion confirms the idea of distributed local glass transition temperature discussed earlier.

# DESIGNING NEW COMPOSITIONS

The ultimate goal of such a research is to predict new alloy compositions that would lead to novel bulk metallic glasses. The ideas discussed above can be translated to reality by examining each element in terms of contribution to glass formation. As an example here we discuss Fe based alloys and Al based alloys. As a prototype system we consider a ternary alloy with small and large solutes. These predictions are presently being tested.

## Fe-based alloys
As small atoms B is ideal because of the size and the high value of $K$. Other small atoms, such as P and Si are used, but P has a low value of $K$ and Si is not small enough. Since the bonding between B and Fe is not overly strong, it is useful to replace a part of Fe with elements that interact more strongly with B, such as Ni or Nb. As large atoms $5d$ elements, such as Hf, Ta, and W, or $4f$ elements (RE) may be considered.

## Al-based alloys
The standard composition is Al-TM-RE, a small atom being TM and a large atom RE. Among the TM elements, Fe and Ni interact most with Al, through charge transfer. Al has a very high spatial free electron density and a high Fermi level. Pairing it with an element with a

high density of states and low Fermi level, such as TM causes strong hybridization with the charge transfer. The Al-Fe bond is reduced by as much as 0.2 Å [15], making Fe appearing even smaller than its nominal metallic radius. It is not easy to find an element larger than a rare earth, and this limits the possibility of increasing its stability even further. On the other hand it is pos- sible to find an element smaller than Fe and Ni, and still interact with Al. Li or Be are the candi- dates, but Li has a small value of K, and Be is toxic.

## CONCLUSIONS

It is difficult to develop a theory of glasses, since it is not easy to describe the atomic structure of a glass. We developed a theory, which addresses the problem from a different point of view of local topological instability and describes the structure statistically. The theory suc- ceeded in describing the glass transition, glass formability and atomic transport in metallic glasses. It is simple enough to be used in predicting glass formability of alloys, and presently its power is being tested in the effort to seek new bulk metallic glass systems.

## ACKNOWLEDGMENT

This work was supported by the Defense Advanced Research Projects Agency and the Office Naval Research through DARPA/ONR Grant N00014-01-1-0961 and through Boeing Co. Grant 44955-00-00. The author is grateful to S. J. Poon, G. J. Shiflet, W. L. Johnson and M. Khantha for useful discussions.

## REFERENCES

1. A. Inoue, T. Zhang and T. Masumoto, *Mater. Trans. JIM*, **31**, 425 (1990).
2. T. Zhang, A. Inoue and T. Masumoto, *Mater. Trans. JIM*, **32**, 1005 (1991).
3. A. Peker and W. L. Johnson, *Appl. Phys. Lett.*, **63**, 2342 (1993).
4. T. Egami and Y. Waseda, *J. Non-Cryst. Solids* **64**, 113 (1984).
5. T. Egami, *Mater. Sci. Eng.* **A226-228**, 261 (1997).
6. T. Egami, *Mater. Trans.* **43**, 510 (2002).
7. T. Egami, *Z. Metallkunde* **93**, 1071 (2002).
8. T. Egami and D. Srolovitz, *J. Phys. F: Metal Phys.* **12**, 2414 (1982).
9. M. H. Cohen and D. Turnbull, *J. Chem. Phys.* **31**, 1164 (1959).
10. D. Turnbull and M. H. Cohen, *J. Chem. Phys.* **34**, 120 (1961).
11. D. Turnbull and M. H. Cohen, *J. Chem. Phys.* **52**, 3038 (1970).
12. F. Faupel, W. Frank, M.-P. Macht, H. Mehrer, V Naundorf, K. Rätzke, H. Schober, S. K. Sharma and H. Teichler, *Rev. Mod. Phys.* **75**, 237 (2003).
13. H. R.Schober, C. Olingschleger and B. B. Laird, *J. Non-Cryst. Solids* **156**, 965 (1993).
14. Y. Suzuki, J. Haimovich and T. Egami, *Phys. Rev. B* **35**, 2162 (1987).
15. H.-Y. Hsieh, T. Egami, Y. He, S. J. Poon and G. J. Shiflet, *J. Non-Cryst. Solids* **135**, 248 (1991).