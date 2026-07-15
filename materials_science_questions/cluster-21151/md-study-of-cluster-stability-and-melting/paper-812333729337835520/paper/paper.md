Surface Review and Letters, Vol. 3, No. 1 (1996) 457-461
© World Scientific Publishing Company

# LONG-RANGE CORRELATIONS IN SMALL ATOMIC CLUSTERS

SAROJ K. NAYAK and R. RAMASWAMY

School of Physical Sciences, Jawaharlal Nehru University, New Delhi 110 067, India

We study the power spectrum of fluctuations in the potential energy of atoms in small rare-gas clusters. At temperatures when the cluster is in a liquid-like state the spectra have a "1/f" dependence over a wide range of frequency $f$. This behavior is distinctly different from both the solid phase of clusters or bulk liquid, and is indicative of long-range temporal correlations. The origins of this phenomenon is explored by studying the individual potential-energy distributions in pure and mixed rare-gas clusters, $Xe_{55}$ and $ArXe_{54}$, via molecular dynamics simulations. Substitution of atomic impurities acts as an effective probe of the dynamics, and we observe that long-lived memory effects have their origins in hierarchical relaxation processes arising in the motion of the atoms from the surface to the core and vice-versa.

The study of finite clusters of atoms or molecules has helped in understanding how atomic or molecular properties are gradually modified with size as one approaches bulk matter. Because of the small size, these systems can be studied in considerable individual detail, and several techniques of nonlinear dynamics or molecular dynamics (MD), which have principally developed for systems with a small number of degrees of freedom, can find application.

Molecular dynamics simulation studies of rare-gas atomic clusters have given evidence for a transition from a solid-like phase to a liquid-like phase as the internal energy is increased. $^{1,2}$ Since the classical dynamics of small clusters can be studied in detail, effort has been made to correlate the nature of the dynamics with features of the underlying potential-energy surface. $^{7}$ Thus, in the solid phase the atoms constituting the cluster are mainly seen to execute harmonic vibrations about the equilibrium position in the deepest well, the global minimum of the potential-energy surface. As the energy is increased, the system gradually begins to make (activated) transitions to nearby (metastable) local minima, and eventually, as the system becomes less rigid, begins to explore more and more of these shallower minima, eventually going over into the liquid state. An interesting phenomenon that is exhibited by clusters is a dynamical coexistence $^{3,4,13}$ of these phases over a range of energy, quite unlike the solid-liquid trasition in bulk matter.

The change in phase can be characterized by studying the Lindeman index, $\delta$, the root-mean-square bond length fluctuation, which is defined by

$$
\delta=\frac{2}{N(N-1)} \sum_{i<j} \frac{\sqrt{\left\langle r_{i j}^{2}\right\rangle-\left\langle r_{i j}\right\rangle^{2}}}{r_{i j}}, \tag{1}
$$

where $N$ is the number of atoms in the cluster, and $r_{i j}$ is the separation between pairs of atoms. At the melting temperature, $\delta$ increases abruptly. Other indicators, such as the largest Lyapunov exponent, have also been observed to behave similarly. $^{6}$

Concurrent with the structural change embodied in the variation of $\delta$, there are dynamical changes as well when the cluster "melts". In particular, we observed $^{12}$ that long-range dynamical correlations are set up in the liquid state, which is reflected in the power spectrum of individual potential-energy fluctuations showing $1/f$ behavior. This is in contrast to the solid phase, where the spectra do not have the $1/f$ character. These $1/f$ spectra are often seen as a signature of complex dynamics. In recent years, an effort has been made to understand the ubiquitous occurence of such temporal (or spatial) power-law correlations through general mechanisms, and one interesting framework that has been proposed is the self-organized criticality. $^{14}$ These ideas have found application in a variety of systems, most notably those wherein the timescale of relaxation is widely

separated from the timescale of excitation. $^{15}$ Al though the present systems do not intrinsically pos- sess very widely separated timescales, the organi- zation of a cluster offers a hierarchy of relaxation pathways and barriers, and this effectively makes the dynamics complex.

In the present work, these effects are studied in Lennard-Jones clusters. One mechanism whereby temporal correlations are built up comes from the in- trinsic spatial anisotropy of clusters. There are, for example, differences in the environment of surface atoms and those in the interior, and this gives rise to memory effects. Thus, over a fairly long timescale, an atom "remembers" where it has been. Removal of the anisotropy, as for example in bulk liquid, makes correlations die out more rapidly, and this results in a flat, white-noise-like spectrum.

We studied 55-atom clusters, both pure $LJ_{55}$ (pa rameters are scaled so that the system corres- ponds to $Xe_{55}$ ), and a mixed cluster wherein one of the atoms is taken to be lighter than the others(nominally corresponding to $ArXe_{54}$ ). In the later system, the substitutional impurity acts as an effec- tive probe of the mechanism whereby long-range cor- relations arise.

MD simulations are carried out using standard techniques. $^{16}$ The interatomic potential between neu tral rare-gas atoms is taken to be the usual Lennard- Jones potential of the form

$$
V\left(r_{i j}\right)=4 \epsilon\left[\left(\sigma / r_{i j}\right)^{12}-\left(\sigma / r_{i j}\right)^{6}\right], \quad (2)
$$

where $r_{i j}$ is the distance between the atoms $i$ and $j, \epsilon$ is the unit of energy. The potential minimum occurs at a distance $2^{1 / 6} \sigma$ , where $\sigma$ is the unit of distance. The parameters $\epsilon$ and $\sigma$ depend on whether the in teracting atoms are Xe-Xe or $Ar-Xe^{8,9}$ and distance and time are scaled by $\sigma$ and $(m \sigma^{2} / 48 \epsilon)^{1 / 2}$ respec tively, where $\epsilon$ and $\sigma$ are parameters appropriate forthe Ar-Ar: $:^{17,18} m=6.63382 ×10^{-26} kg, \sigma=0.3405$  $nm$ , and $\epsilon=120 ~K$ . Sufficient accuracy is maintained by choosing the time step for integraton to be 0.01 in reduced units, which is 3.125 fs. The total linear and angular momenta are both set to zero, $^{13}$ and the clusters are equilibrated for $3 ×10^{5} MD$ steps. The average temperature, $T$ , of the system is given by

$$
T=\frac{2 E}{(3 N-6) K_{B}}, \quad (3)
$$

where $N$ is the number of atoms, $K_{B}=1.381 \times$  $10^{-23} erg / K$ is the Boltzmann constant, and $E$ is the kinetic energy, suitably averaged over the entire trajectory.

The total potential energy of an individual atom,(Xe or Ar) labeled $k$ is defined as

$$
V_{k}(t)=\Sigma_{j \neq k} V\left(\left[r_{k j}(t)\right]\right), \quad (4)
$$

and the power spectrum can be calculated for a trajectory of length $\tau$ by the usual fast Fourier transform method

$$
S(f)=\lim _{\tau \to \infty}\left|\frac{1}{\tau} \int_{0}^{\tau} V_{k}(t) \exp (-i f t) d t\right|^{2}, \quad (5)
$$

where $f$ is the frequency. In the present work, the spectra have been averaged over different realizations at the same temperature.

The power spectrum of individual atomic poten- tial-energy fluctuations in $Xe_{55}$ clusters is shown in Fig. 1, where it can be seen to have a distinct $1 / f$ de pendence over a wide frequency range, indicative of strong correlations between individual motions in the liquid state. At temperatures such that the cluster is "liquid", the $1 / f$ behavior usually obtains above a threshold frequency $f_{c}$ , below which the spectrum is flat. (However, in the solid phase or in coexis- tence phase no such power law is seen in the powerspectrum.)

![](./images/812333729337835520_1.jpg)

Fig. 1. Power Spectrum of individual atomic potential- energy fluctuations in the liquid state of $Xe_{55}$ at $T=69.6 ~K$ .

During the dynamical evolution of the liquid cluster, the atoms move from one instantaneous structure¹⁰ – one metastable minimum in the potential-energy surface – to another. In the process, the movement of atoms among the different shells in the cluster, (see Fig. 2), involve a crossing of several potential-energy barriers. In order to see this picture more clearly, we tag a particle and calculate its distance $R_i$ from the center-of-mass of the cluster with time and compare $R_i$ with the individual potential-energy fluctuation $V_i$. When the atom stays on the surface, the distance from the center-of-mass of the cluster is large and its individual energy is also high compared to when it stays in the core. There is a high degree of correspondence between variations in $R_i(t)$ and $V_i(t)$ since major energy changes occur principally when a given atom travels from the surface of cluster to the core. The correspondence is however not exact, since there are cooperative effects, but variation of $R_i$ vs $V_i$ shows a strong correlation. In the liquid state, the distribution of individual atomic potential energies is a superposition of several Gaussians, depending on the size of the cluster. The individual potential-energy distribution, $P(V)$ can be represented by sum of Gaussians of the form

$$
P(V)=\sum_{i=1}^{n} A_{i} \exp \left[-\left(V-V_{i}^{0}\right)^{2} / 2 \sigma_{i}^{2}\right], \tag{6}
$$

![](./images/812333729337835520_2.jpg)

Fig. 2. Distribution of distance of a tagged atom in Xe₅₅.

Long-Range Correlations in Small Atomic Clusters 459

where $A_i$ is the amplitude, $V_i^0$ is the mean, and $\sigma_i$ is the width of the $i$th Gaussian. This essentially leads to the existence of multiple time scales in the dynamics, which is eventually reflected in its power spectrum having a power-law decay.²⁰

![](./images/812333729337835520_3.jpg)

Fig. 3. Distribution of the distance of (a) Ar in ArXe₅₄ and (b) a tagged Xe atom in ArXe₅₄ in the liquid state at temperature $T=68$ K.

Substitution of an impurity atom in the pure clus- ter gives another probe of the dynamics. By replac- ing an atom in the pure cluster gives another probeof the dynamics. By replacing an atom of the $Xe_{55}$  cluster by a lighter atom Ar, the effect of the mul- tiple relaxation pathways can be suppressed drasti- cally. At low temperature in the solid state, or even at slightly higher temperatures, when the cluster has just melted, the lighter atom remains mainly in the core. In the solid state the most favorable position of Ar is in the core of the $Xe_{54} Ar$ cluster, in order to reduce the Xe-Xe interaction. The Ar atom stays in the core until it gets the activation energy to over- come the barrier, and thus, only with increasing tem- perature can the different atoms diffuse into the core from the surface or vice-versa. At low temperature in the liquid state a typical Xe atom in $Xe_{54} Ar$ shows a more diffusional motion while the Ar atom does not. The distribution of $R_{i}(t)$ for these atoms are shown in Fig. 3, the Ar atom confines its motion to the core while a typical Xe atom travels from one shell to another. Consequently the power spectrum of a typical Xe atom is of $1 / f$ type while that of Ar is flat or white-noise like. The power spectra are shown in Figs. 4(a) and 4(b). However, at higher temperatures in the liquid state the same Ar atom is able to move throughout the cluster; when this happens, there are changes in the power spectra and we observe that1/f behavior is obtained only when atoms are capa- ble of large-scale motion which involves traversal of different portions of the potential-energy landscape. In the situation when such dynamics is suppressed, the corresponding spectrum of potential-energy fluc- tuations is flat and more white-noise like, similar tothat observed in Lennard-Jones liquids. $^{11}$

![](./images/812333729337835520_4.jpg)

Fig. 4. Power Spectrum of the potential-energy fluctu-ations of Ar in the liquid state of (a) $ArXe_{54}$ at $T=$ 68 K, which is flatter and more white-noise like, com- pared to the spectrum of (b) Xe in $Xe_{54} Ar$ at the same temperature.

Although the fluctuation spectrum of the atomic potential energy is not directly observable, we believe that this phenomena is amenable to experimental verification. Temporal correlations of the type dis- cussed above can be explored and analyzed through the detailed study of absorption spectra $^{22}$ of impu rity molecules embedded in atomic clusters.

## Acknowledgments
We thank the Department of Science and Technology for support under Grant No. SP/S2/MOS/92. SKN acknowledges financial support from the University Grants Commission and the CSIR.

## References
1. R. S. Berry, T. L. Beck, H. L. Davis, and J. Jellinek, Adv. Chem. Phys. 70, 75 (1988).
2. S. Sugano, Microcluster Physics (Springer, Berlin,1991).

Long-Range Correlations in Small Atomic Clusters 461

3. C. L. Briant and J. J. Burton, *Nature Physical Science* **100**, 243 (1973); *J. Chem. Phys.* **63**, 2045 (1975).

4. R. D. Etters and J. Kaelberer, *Phys. Rev.* **A11**, 1068 (1975); J. Kaelberer and R. D. Etters, *J. Chem. Phys.* **66**, 3233 (1977).

5. R. J. Hinde, R. S. Berry, and D. J. Wales, *J. Chem. Phys.* **96**, 1376 (1992).

6. S. K. Nayak, R. Ramaswamy, and C. Chakravarty, *Phys. Rev.* **E51**, 3376 (1995).

7. R. S. Berry, *Chem. Rev.* **93**, 2379 (1993); *J. Phys. Chem.* **98**, 6910 (1994).

8. D. Scharf, J. Jortner, and U. Landman, *J. Chem. Phys.* **88**, 4273 (1988).

9. The parameters used in the two-body Lennard-Jones potentials are taken from Ref. 8. For Ar-Xe $\sigma = 3.65$, $\epsilon = 1.48$, and for Xe-Xe $\sigma = 4.10$, $\epsilon = 1.853$.

10. F. Stillinger and T. Weber, *Phys. Rev.* **A25**, 978 (1982).

11. M. Sasai, I. Ohmine, and R. Ramaswamy, *J. Chem. Phys.* **96**, 3045 (1992).

12. S. K. Nayak and R. Ramaswamy, *Proc. Ind. Acad. Sci.* (Chemical Sciences) **106**, 521 (1994); S. K. Nayak and R. Ramaswamy, *J. Phys. Chem.* **98**, 9260 (1994); S. K. Nayak, R. Ramaswamy, and C. Chakravarty, *Phys. Rev. Lett.* **74**, 4181 (1995).

13. T. L. Beck, J. Jellinek, and R. S. Berry, *J. Chem. Phys.* **87**, 545 (1987); R. S. Berry, J. Jellinek, and G. Natanson, *Phys. Rev.* **A30**, 919 (1984); D. Wales, *Mol. Phys.* **78**, 151 (1993).

14. P. Bak, C. Tang, and K. Wiesenfeld, *Phys. Rev. Lett.* **59**, 381 (1978); *Phys. Rev.* **A38**, 364 (1988).

15. G. Grinstenin, *J. Appl. Phys.* **69**, 5441 (1991).

16. M. P. Allen and D. J. Tildesley, *Computer Simulation of Liquids* (Oxford University Press, Oxford, 1987).

17. D. W. Heerman, *Computer Simulation methods in Theoretical Physics* (Springer-Verlag, Berlin, 1990).

18. A. Rahman, *Phys. Rev.* **135**, A405 (1964).

19. D. J. Wales and R. S. Berry, *J. Chem. Phys.* **92**, 4283 (1990).

20. E. W. Montroll and M. F. Shlesinger, *J. Stat. Phys.* **32**, 209 (1993).

21. See, e.g., T. Hwa and M. Kardar, *Phys. Rev.* **A45**, 7002(1992) for a recent survey of self-organized criticality. A recent review that covers some relevant topics is M. C. Cross and P. C. Hohenberg, *Rev. Mod. Phys.* **65**, 851 (1993). This also forms the subject of several articles in the book *Correlations and Connectivity*, eds. H. E. Stanley and N. Ostrowsky (Kluwer Academic Publishers, Dordrecht, 1990).

22. I. Ohmine and H. Tanaka, *Chem. Rev.* **93**, 2545 (1993).