# MONTE CARLO STUDIES OF $\text{SU}(N)/\text{Z}_N$ LATTICE GAUGE THEORIES IN FOUR DIMENSIONS

Michael CREUTZ
Brookhaven National Laboratory, Upton, New York, 11973 USA

K.J.M. MORIARTY
Department of Mathematics, Royal Holloway College, Englefield Green, Surrey, TW20, OEX, UK

Received 18 March 1982

Using Monte Carlo techniques on a four-dimensional space-time lattice, we study $\text{SU}(N)/\text{Z}_N$ gauge theories for $N=3$, 4, 5 and 6. We find first-order phase transitions at critical inverse temperatures of $\beta_{\text{c}}=6.40$, 12.0, 19.5 and 32.0 for $\text{SU}(3)/\text{Z}_3$, $\text{SU}(4)/\text{Z}_4$, $\text{SU}(5)/\text{Z}_5$ and $\text{SU}(6)/\text{Z}_6$, respectively.

It was long felt that non-abelian lattice gauge theories in four space-time dimensions would exhibit no phase transitions separating the high- and low-temperature domains. However, first-order phase transitions have been found in SU(4) [1,2], SU(5) [1,3], SU(6) [4] and $\text{O}(3)=\text{SU}(2)/\text{Z}_2$ [5]. We wish to continue this search for phase transitions to $\text{SU}(N)$ in the adjoint representation with $N=3$, 4, 5 and 6. As the center of the group is removed with adjoint representations, we refer to these models as $\text{SU}(N)/\text{Z}_N$ theories. The center of a gauge group is often invoked as crucial to the confinement mechanism [5,6]. Thus, it is interesting to study the effect of its removal. We shall see that these gauge groups also exhibit first-order phase transitions. This suggests that phase transitions for non-abelian gauge groups, using Wilson's form of the action, are the rule rather than the exception. In fact, phase transitions are only absent for the gauge groups SU(2) [7] and SU(3) [8].

We study Wilson's formulation [9] of gauge theory. We form a hypercubical euclidean lattice in four space-time dimensions and join nearest neighbor sites $i$ and $j$ by the link $\langle i,j\rangle$. With each link we associate a matrix $U_{ij}$ which is an element of the gauge group $\text{SU}(N)$. The partition function is given by

$$
Z(\beta)=\int\left(\prod_{\langle i,j\rangle} \mathrm{d}U_{ij}\right)\exp(-\beta S[U]).
$$

The normalized invariant Haar measure for the group is the measure in the above integral. In Wilson's formulation, the action $S$ is a function of ordered products of

link matrices $U_\square$ around the plaquettes $\square$ in the lattice giving

$$
S[U]=\sum_{\square} S_{\square}=\sum_{\square}\left(1-\frac{1}{N} \operatorname{Re} \operatorname{Tr} U_{\square}\right).
$$

Here the inverse temperature $\beta$ is related to the bare coupling constant $g_{0}$ by $\beta=2 N / g_{0}^{2}$.

We wish to modify this action by replacing the trace in this equation with the trace in the adjoint representation. Thus we take

$$
S_{\square}=1-\frac{1}{\left(N^{2}-1\right)} \operatorname{Tr}_{\mathrm{A}} U_{\square},
$$

where $\operatorname{Tr}_{\mathrm{A}}$ denotes the trace of the corresponding adjoint matrix. The normalization is chosen so that the expectation value of $S_{\square}$

$$
\langle E\rangle=\left\langle 1-\frac{1}{\left(N^{2}-1\right)} \operatorname{Tr}_{\mathrm{A}} U_{\square}\right\rangle
$$

runs between one and zero as $\beta$ increases from 0 to infinity. With the modified action, the connection between bare coupling and $\beta$ becomes

$$
\beta=\frac{N^{2}-1}{N g_{0}^{2}}.
$$

We establish [9] the relationship between the characters of the adjoint and the fundamental representations of $\mathrm{SU}(N)$ as follows. The character $\chi_{i}(g)=\operatorname{Tr} D^{i}(g)$ of a representation $i$ satisfies the following composition laws: If $i$ is reducible and $i=j \oplus k$ then

$$
\chi_{i}(g)=\chi_{j}(g)+\chi_{k}(g).
$$

If $i$ is a Kronecker product $i=j \otimes k$ then

$$
\chi_{i}(g)=\chi_{j}(g) \cdot \chi_{k}(g),
$$

which is merely the multiplication of complex numbers. The relation

$$
\operatorname{Tr} D^{\mathrm{A}}(g)=\left|\operatorname{Tr} D^{\mathrm{F}}(g)\right|^{2}-1, \tag{1}
$$

then follows from this because

$$
\mathrm{F} \otimes \overline{\mathrm{F}}=\mathrm{A} \oplus 1,
$$

for $\mathrm{SU}(N)$. Here $\mathrm{F}$ represents the fundamental representation, $\overline{\mathrm{F}}$ represents its complex conjugate, 1 represents the trivial 1-dimensional representation and $\mathrm{A}$

represents the adjoint representation. The adjoint trace for any SU($N$) is found using the identity of eq. (1).

We equilibrated our lattice by the method of Metropolis et al. [11], described for lattice gauge theory in ref. [1]. Periodic boundary conditions were used throughout our calculation.

The leading-order high-temperature expansion is given by

$$
\langle E \rangle = 1 - \frac{\beta}{\left(N^2 - 1\right)^2} + \mathrm{O}\left(\beta^2\right), \tag{2}
$$

while the leading-order low-temperature expansion is the same as in the Wilson model

$$
\langle E \rangle = \frac{N^2 - 1}{4\beta} + \mathrm{O}\left(\beta^{-2}\right). \tag{3}
$$

Figs. 1a-d show the average action per plaquette for SU(3)/$Z_3$, SU(4)/$Z_4$, SU(5)/$Z_5$ and SU(6)/$Z_6$, respectively, on a $4^4$ lattice as a function of the inverse

![](./images/812436337360633857_1.jpg)

Fig. 1. The average action per plaquette $\langle E \rangle$ for (a) SU(3)/$Z_3$, (b) SU(4)/$Z_4$, (c) SU(5)/$Z_5$ and (d) SU(6)/$Z_6$ on a $4^4$ lattice as a function of the inverse temperature $\beta$. The full circles represent the unique value to which ordered and disordered starts converge, the crosses and open circles represent the average over the last 20 of 100 iterations through the lattice for ordered and disordered starts, respectively. The curves represent the leading-order high- and low-temperature expansions of eqs. (2) and (3), respectively.

![](./images/812436337360633857_2.jpg)

Fig. 1 (continued)

temperature $\beta$. All the data points result from 100 Monte Carlo iterations through the lattice with the last 20 iterations averaged over. As we pass through the lattice, each iteration consists of 20 Monte Carlo upgrades per link. In the high-temperature region, the disordered and ordered starting lattice runs converged to one another in less than 100 iterations. In the low-temperature region, the disordered and ordered starting lattice runs did not converge to one another, probably because the Monte Carlo algorithm has not been adequately optimized. Hysteresis loops clearly develop in each diagram. However, it is quite impossible to accurately estimate the critical inverse temperatures from these diagrams.

From fig. 1 we can see that the high-temperature expansion of eq. (1) nicely approaches the Monte Carlo data at small $\beta$. We can also see that the ordered starting lattice data converges on the leading-order low-temperature expansion relatively well. With more optimization of our Monte Carlo algorithm, the dis- ordered starting lattice data should also agree with the low-temperature expansion.

We show in figs. 2a-d the average action per plaquette as a function of the Monte Carlo iterations for the $\mathrm{SU}(3) / Z_{3}, \mathrm{SU}(4) / Z_{4}, \mathrm{SU}(5) / Z_{5}$ and $\mathrm{SU}(6) / Z_{6}$ gauge groups, respectively, on $4^{4}$ lattices for both disordered and ordered starts. Figs. 2a-c

![](./images/812436337360633857_3.jpg)

Fig. 2. The evolution of the disordered and ordered configurations for the average action per plaquette for (a) $SU(3)/Z_3$, (b) $SU(4)/Z_4$, $SU(5)/Z_5$ and (d) $SU(6)/Z_6$ for a $4^4$ lattice near the appropriate critical inverse temperature.

![](./images/812436337360633857_4.jpg)

Fig. 3. The evolution of the disordered and ordered configurations for the average action per plaquette for $\mathrm{SU}(3)/Z_3$ for a $4^4$ lattice at various values of the inverse temperature for $\beta=$(a) 5.60, (b) 5.90, (c) 6.65 and (d) 6.80.

correspond to 500 iterations while fig. 2d corresponds to 300 iterations through the lattice in the hysteresis loop for the appropriate gauge group. The temperatures were chosen near the transition as estimated below. In the vicinity of the critical inverse temperature the relaxation time for the lattice is very long.

Fig. 3 shows the average action per plaquette as a function of the Monte Carlo iterations for the SU(3)/$Z_3$ gauge theory on a $4^4$ lattice for both disordered and ordered starts for various values of the inverse temperature on either side of the critical inverse temperature. For $\beta=5.60$ (fig. 3a), the disordered and ordered starts

![](./images/812436337360633857_5.jpg)

Fig. 4. The evolution of the mixed phase configurations for the average action per plaquette for (a) SU(3)/$Z_3$, (b) SU(4)/$Z_4$, (c) SU(5)/$Z_5$ and (d) SU(6)/$Z_6$ for a $4^4$ lattice at various values of the inverse temperature.

![](./images/812436337360633857_6.jpg)

converge to a unique value after approximately 230 iterations. Fig. 3 shows how difficult it is to calculate the critical inverse temperature solely from observing the evolution of disordered and ordered starts at fixed values of the inverse temperature $\beta$. Similar convergence properties are found for $\mathrm{SU}(4)/Z_{4}$, $\mathrm{SU}(5)/Z_{5}$, and $\mathrm{SU}(6)/Z_{6}$. Note, however, the strong evidence for superheating and supercooling in figs. 3b and 3c, respectively.

To determine the critical temperatures more precisely we studied mixed initial conditions as described in ref. [12]. All links were first randomized, and then those with time coordinates less than half the total lattice length were refrozen to the identity. Thus either above or below the transition temperature we always have a

seed for the growth of the stable phase. In figs. 4a-d we show the evolution of the mixed phase starting lattice runs for various values of the inverse temperature $\beta$ in the region of the hysteresis loops for $\mathrm{SU}(3)/Z_{3}$, $\mathrm{SU}(4)/Z_{4}$, $\mathrm{SU}(5)/Z_{5}$ and $\mathrm{SU}(6)/Z_{6}$, respectively. On either side of the critical inverse temperature, there is a rapid initial relaxation of the system to a definite value of the average action per plaquette, while at the critical inverse temperature there are two phases which can coexist and there is only a meandering drift in the average action per plaquette. Using these diagrams, we estimate the critical inverse temperatures to be $\beta_{\mathrm{c}}=6.40 \pm 0.10$, $12.00 \pm 0.35$, $19.5 \pm 1.1$ and $32.0 \pm 1.0$ for $\mathrm{SU}(3)/Z_{3}$, $\mathrm{SU}(4)/Z_{4}$, $\mathrm{SU}(5)/Z_{5}$ and $\mathrm{SU}(6)/Z_{6}$, respectively. Čvitanovic et al. [13] used mean field theory to predict that the critical inverse temperatures for $\mathrm{SU}(3)/Z_{3}$, $\mathrm{SU}(4)/Z_{4}$, $\mathrm{SU}(5)/Z_{5}$ and $\mathrm{SU}(6)/Z_{6}$ would be $\beta_{\mathrm{c}}=6.78$, $12.40$, $20.3$ and $29.6$, respectively. These results are in reasonable agreement with our values.

From the present calculations we see that $\mathrm{SU}(N)/Z_{N}$, $N=3,4,5$ and 6, all have first-order phase transitions. Previously, it was shown [5] that $\mathrm{SU}(2)/Z_{2}$ also has a first-order phase transition. Thus, it appears that the adjoint representations of $\mathrm{SU}(N)$ and $\mathrm{U}(N)$ exhibit first-order phase transitions for all $N$ larger than unity.

We wish to thank the Science and Engineering Research Council of Great Britain for the award of grants (Grant numbers NG-0983.9 and NG-1068.2) which provided time on the CRAY-1 computer at the Daresbury Laboratory in Warrington on which part of this calculation was performed. We also wish to thank Professor Dr. G. Mack for much useful correspondence and Dr. B. Lautrup for supplying us with a correct version of ref. [13].

## References

[1] M. Creutz, Phys. Rev. Lett. 46 (1981) 1441
[2] K.J.M. Moriarty, Phys. Lett. 106B (1981) 130
[3] H. Bohr and K.J.M. Moriarty, Phys. Lett. 104B (1981) 217
[4] M. Creutz and K.J.M. Moriarty, Phys. Rev. D25 (1982) 1724
[5] I. G. Halliday and A. Schwimmer, Phys. Lett. 101B (1981) 327;
J. Greensite and B. Lautrup, Phys. Rev. Lett. 47 (1981) 9;
I. G. Halliday and A. Schwimmer, Phys. Lett. 102B (1981) 337;
G. Bhanot and M. Creutz, Phys. Rev. D24 (1981) 3212
[6] R. Brower, D. Kessler and M. LeVine, preprint (1981);
E. Tomboulis, Phys. Rev. D23 (1981) 2371;
G. Mack and E. Pietarinen, preprint (1981)
[7] M. Creutz, Phys. Rev. D21 (1980) 2308
[8] M. Creutz, Phys. Rev. Lett. 45 (1980) 313;
K.J.M. Moriarty, Nucl. Phys. B [FS], to be published
[9] K.G. Wilson, Phys. Rev. D10 (1974) 2445
[10] G. Mack, private communication
[11] N. Metropolis, A. W. Rosenbluth, M. N. Rosenbluth, A. H. Teller and E. Teller, J. Chem. Phys. 21 (1953) 1087
[12] M. Creutz, L. Jacobs, and C. Rebbi, Phys. Rev. Lett. 42 (1979) 1390
[13] P. Čitanovic, J. Greensite and B. Lautrup, Phys. Lett. 105B (1981) 197