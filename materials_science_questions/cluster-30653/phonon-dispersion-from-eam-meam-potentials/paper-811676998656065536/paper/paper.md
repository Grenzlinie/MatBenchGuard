# H MOTION IN Pd AND Nb: A MOLECULAR-DYNAMICS STUDY

Yinggang Li* and Göran Wahnström**
*Institute of Theoretical Physics, Chalmers University of Technology and University of Göteborg, S-412 96 Göteborg, Sweden
**Department of Applied Physics, Chalmers University of Technology and University of Göteborg, S-412 96 Göteborg, Sweden

## ABSTRACT

Based on realistic many-body potentials molecular-dynamics simulations are carried out for $PdH_{0.03}$ and $NbH_{0.02}$. The H motion is investigated at two different temperatures, $T=300$ and 600K, paying attention to the vibrational and diffusive motion. We find that the motion of H in Nb, a bcc metal, is more complicated than in Pd, a fcc metal, and the differences are discussed. When detailed comparison is made with quasielastic neutron scattering data for H in Pd at 600K, we argue that in order to characterize the diffusion correctly, one has to include nonadiabatic effects.

## INTRODUCTION

Metal-hydrogen systems are of applied as well as of basic physical interest and have attracted great attention from both the experimental and the theoretical communities [1]. Over the last 20 years extensive neutron scattering studies have been performed which give detailed information on the H motion on an atomistic scale.

Numerical molecular-dynamics (MD) simulations provide complementary information and recently this method has been used for theoretical studies of metal-hydrogen systems. In that case a sufficiently accurate model for the interatomic interactions is required as input.

New potential models have been developed during the last decade for metals and their alloys. The embedded-atom method (EAM)[2] and the similar scheme by Finnis and Sinclair [3] are two such approaches, which are suited for fcc and bcc transition metals, respectively. The EAM has been used by Pratt and Eckert [4] and more recently by us [5,6] to study H motion in Pd. The Finnis-Sinclair model has been applied by Gillan and his coworkers[7,8] in the study of quantum vibrational states and quantum diffusion of H in Nb.

This paper presents our MD results for the motion of hydrogen in Pd and some prelim- inary results for H in Nb. $PdH_{x}$ and $NbH_{x}$ are typical representatives of fcc and bcc metal hydrogen systems, respectively, and they are extensively studied experimentally. First we present the models to be used. This is followed by a presentation of the results. We show the stationary positions for H and give the numerical values for the diffusion constant. We then determine the H motion at room temperature, where the vibrational properties are investigated, and at higher temperatures, where the detailed features of H diffusion are studied. The results are compared with quasielastic-neutron-scattering experiment and the effect of electron-hole pair excitations is discussed.

## THE SYSTEM AND THE MANY-ATOM INTERACTION MODELS

For $PdH_{x}$ we use 256 Pd atoms and 8 H atoms, except in the study of the vibrational motion where only 1 H atom is included. Periodic boundary conditions are always em-

Mat. Res. Soc. Symp. Proc. Vol. 291. ©1993 Materials Research Society

![](./images/811676998656065536_1.jpg)
in Pd (fcc)

![](./images/811676998656065536_2.jpg)
in Nb (bcc)

Figure 1: H locations obtained from the MD simulations. The trajectories for H atoms have been folded into an unit cell of the corresponding lattice. Dots: the H positions; Circles: the equilibrium positions for the host-metal atoms.

ployed. The temperatures is 298K when studying the vibrational motion, and 623K when the diffusive motion is considered. The lattice spacing is $3.89Å$ and $3.94Å$, respectively, at the two different temperatures, which takes the thermal expansion into account in a proper way. The parameterization proposed by Foiles, Baskes and Daw [9] is used for the EAM potential and for further details of our model potential, we refer to Ref.[6].

The $NbH_x$ system consists of 432 Nb atoms and 8 H atoms. Two different temperatures are considered, 300K and 580K, and the lattice spacing is equal to $3.30Å$ in both cases. The EAM is not suited for bcc transition metals, because of the partially-filled $d$-states and the nonclose-packed structure [10], for which the nonspherical distribution of electron density is more pronounced than in the fcc metals. The Finnis-Sinclair empirical approach [3] is essentially the same as the EAM but developed for bcc metals. Based on this approach, Gillan and his coworkers have proposed a model for H in Nb and we apply their model without doing any modifications. For details we refer to the original papers [7, 8].

# RESULTS

Hydrogen in fcc Pd and bcc Nb is experimentally found to occupy the octahedral (O) and tetrahedral (T) interstitial sites, respectively [11]. The present model systems correctly predict these equilibrium locations. This can be seen in Fig. 1 where the H locations obtained from the MD simulation are shown. We have then folded the result into an unit cell of the host metal.

The temperature dependence of self-diffusion constant $D_s$ observed for H in Pd is also well reproduced by our model potential. Within the temperature range studied (600 - 1000K), an Arrhenius form is found: $D_s = D_0exp(-U/K_BT)$, with $D_0 = 4.8×10^{-3}cm^{-2}s^{-1}$ and $U = 0.245eV$. This should be compared with the observed $T$-dependence: $D_0 = 2.9 × 10^{-3}cm^{-2}s^{-1}, U = 0.230eV$ [12].

For H in Nb and above room temperature, the experimental data for the self-diffusion constant can be represented by $D_0 = 5.0 × 10^{-4}cm^{-2}s^{-1}, U = 0.106eV$ [12]. The model by Gillan for H in Nb also gives reasonable values: $U = 0.101eV$, but slightly larger pre-exponential factor, $D_0 \sim 7.5 × 10^{-4}cm^{-2}s^{-1}$.

![](./images/811676998656065536_3.jpg)

Figure 2: The intermediate scattering function, $F_s(\mathbf{q}, t)$, vs time for different q-values and directions calculated at room temperature for PdH$_{0.004}$ and NbH$_{0.02}$. Note that for PdH$_x$ the curves for [100] and [110] directions coincide.

### The Intermediate Scattering Function at Room Temperature

Consider now the intermediate scattering function

$$
F_{s}(\mathbf{q}, t)=\frac{1}{N_{\mathrm{H}}}<\sum_{j=1}^{N_{\mathrm{H}}} \exp \left(-i \mathbf{q} \cdot\left(\mathbf{R}_{\mathrm{H}}^{j}(t)-\mathbf{R}_{\mathrm{H}}^{j}(0)\right)>\right. \tag{1}
$$

where $N_{\mathrm{H}}$ is the number of H atoms and $\mathbf{R}_{\mathrm{H}}^{j}(t)$ denotes the position for hydrogen atom $j$ at time $t$. The time-Fourier transform of $F_s$ is equal to the self part of the dynamical structure factor and is measured directly in neutron scattering experiments. It contains information on both the vibrational and the diffusive motion of hydrogen atoms.

It is straightforward to evaluate the time dependence of $F_s(\mathbf{q}, t)$ for different wave-vectors $\mathbf{q}$ from the output of the MD simulation. Fig 2 shows our results obtained for PdH$_{0.004}$ and NbH$_{0.02}$, respectively.

We notice that at room temperature for PdH$_{0.004}$, the long-range diffusion is negligible at the picosecond time-scale. The hydrogen atom is located around an O-site and vibrates. On the contrary, the H motion in Nb is more complicated and it is not possible to clearly separate the vibrational and translational motion even at room temperature.

The vibrational frequencies for H can also be deduced from Fig 2. We obtain about 75 and 110 meV for H in Pd and Nb, respectively, in accordance with the experimental values, 69.5 and 110 meV [11, 13].

### The Intermediate Scattering Function at Higher Temperatures

At high temperatures hydrogen is very mobile both in Pd and in Nb. The diffusion constant at $T=600 \mathrm{~K}$ is $0.34 \times 10^{-4}$ and $0.64 \times 10^{-4} \mathrm{~cm}^{-2} \mathrm{~s}^{-1}$, respectively [12], which is characteristic of diffusion rates in ordinary liquids (e.g., the diffusion constant for liquid sodium is $0.4-0.8 \times 10^{-4} \mathrm{~cm}^{-2} \mathrm{~s}^{-1}$ in the temperature range $380-460 \mathrm{~K}$ [14]).

First we consider H in Pd. In the long-time limit $F_{s}(\mathbf{q}, t)$ decays exponentially, $F_{s}(\mathbf{q}, t) \rightarrow$ $e^{-\Gamma(\mathbf{q}) t}$, with a q-dependent decay-rate. This gives rise to a quasielastic peak in the corresponding spectrum, with the width at half-maximum $\omega_{1 / 2}(\mathbf{q})=\Gamma(\mathbf{q})$. For small $q$-values,

![](./images/811676998656065536_4.jpg)

Figure 3: The intermediate scattering function $F_s(q,t)$ in logscale, vs time for different q-values and directions calculated for PdH₀.₀₃ at 623K. The curves are labelled by the components of the reduced wavevector k defined by $\mathbf{q}=(2\pi/a)\mathbf{k}$.

the width is directly related to the diffusion constant, $\Gamma(\mathbf{q}) \to D_s q^2$, and for larger $q$-values it depends on the details of the diffusive motion. Therefore, information on the diffusion mechanism can be obtained from the study of the q-dependence of the quasielastic width.

Reliable quasielastic-neutron-scattering data are available for the width [15, 16, 17]. For PdHₓ, a simple random-walk model due to Chudley and Elliott [18] is found sufficient to describe the experimental data (see Fig.4) and from this it is concluded that H atoms in Pd diffuse predominantly via uncorrelated jumps between nearest-neighbor O-sites.

Numerically, we have determined the width in the following way. In Fig.3 we show $-\ln F_s$ as function of time for different q-values and directions. Using the fact that $F_s(\mathbf{q},t) \to e^{-\Gamma(\mathbf{q})t}$, the width $\Gamma(\mathbf{q})$ is simply obtained from the slope. We notice that after about 0.5 ps $F_s$ decays exponentially.

Fig. 4 shows our results for the q-dependence of the dimensionless width defined as $\Delta(\mathbf{q}) \equiv \omega_{1/2}(\mathbf{q}) \cdot a^2/D_s$, where $a$ is the lattice spacing. First we use the EAM potential and curve (a) is obtained. The departure from the experimental data [16] (curve (b)) is far beyond the error bars. Similar discrepancy was also noticed in an earlier MD study using a pair-potential model [19] and nonadiabaticity, i.e., e-h pair excitations, was emphasized as a possible reason for the discrepancy.

Due to the mismatch in their masses, the phonon coupling between the H atom and the metal atoms is weak. Electron-hole pair excitations can then become an important mechanism for energy dissipation. We have included these nonadiabatic corrections to the EAM in a approximate way [6]. The incorporation of this effect results in the curve (c) in Fig. 4 for the width. Excellent agreement with experimental data is achieved. More detailed analysis [6] shows that including nonadiabatic corrections reduces the probability for a H atom to move over several O-sites without getting trapped in between. As a result, the motion becomes more similar to that assumed in the Chudley-Elliott model which describes well the neutron-scattering data. From this we argue that in order to characterize the diffusion correctly, one has to include nonadiabatic effects.

For H in Nb the behavior is more complicated [20]. All residence sites (T-sites) are not equivalent which implies that $F_s(\mathbf{q},t)$ does not decay with a single rate [21]. The quasielastic peak is no longer a single Lorentzian but a superposition of several Lorentzian peaks. Our preliminary results for the intermediate scattering function for H in Nb show this behavior [20]. We also obtain a slower decay compared with the Chudley-Elliot model for intermediate $q$-values, in accordance with the experimental observation [22].

Besides the decay due to long-range diffusion, a much faster decay on a time scale of less than 200 fs is seen from our MD results for $F_s(\mathbf{q},t)$. This decay is not due to vibrations and may be connected to the localized-diffusion motion suggested in recent neutron scattering experiments for NbH₀.₀₂ [23]. More detailed analysis is however needed before more definite

![](./images/811676998656065536_5.jpg)

Figure 4: Half width of the quasielastic peak, $\Delta(\mathbf{q})=\omega_{1 / 2}(\mathbf{q}) \cdot a^{2} / D_{s}$, vs $q$ for two different directions. Curve (a): EAM calculation; (b): experiment [16]; (c): EAM plus nonadiabatic corrections; and (d): the Chudley-Elliott model-calculation. The error bars represent a 95% confidence interval.

conclusion can be made. Investigation in this direction is in progress [20].

# CONCLUSIONS

Molecular-dynamics (MD) simulation has turned out to be a powerful tool for the study of dynamical properties of point defects in metals. A necessary input is a model for the interatomic interaction. We have performed MD studies for H motion in Pd and in Nb using the embedded-atom method [2] for $PdH_{0.03}$ and the similar scheme proposed by Finnis and Sinclair [3] for $NbH_{0.02}$. Both models correctly predict the equilibrium locations for H and give reasonable values for the diffusion constant. We find that the H motion is very different in the two systems. The behavior in the bcc metal is much more complicated and hence less understood than in the fcc metal. At room temperature, it is not possible to clearly separate the vibrational and diffusive motion for H in Nb. At high temperatures, our results show that the intermediate scattering function for H in Nb does not decay at a single rate and shows an additional fast decay on a time scale of 200 fs. This decay can be a manifestation of the localized-diffusion motion suggested by recent experiments [23].

In all simulations here, classical mechanics is assumed. Quantum effects influence, however, the H motion and are more pronounced for H in Nb. In a forthcoming publication [20], we will discuss this issue in connection to our simulation results.

In conclusion, many open questions remain in the study of H motion in metals, in particular for H motion in bcc metals.

Acknowledgment: Discussions with Prof. A. Sjölander and allocation of computer time by the National Supercomputer Center in Sweden are gratefully acknowledged.

# REFERENCES

1.  *Hydrogen in Metals I*, *Topics in Applied Physics*, **28**, edited by G. Alefeld and J. Völkl (Springer-Verlag, Berlin, 1978).

2.  M. S. Daw and M. I. Baskes, Phys. Rev. Lett. **50**, 1285 (1983); Phys. Rev. B **29**, 6443 (1984).

3.  M. W. Finnis and J. E. Sinclair, Philos. Mag. A **50**, 45 (1984).

4.  L. R. Pratt and J. Eckert, Phys. Rev. B **39**, 13170 (1989).

5.  Y. Li and G. Wahnström, Phys. Rev. Lett. **68**, 3444 (1992).

6.  Y. Li and G. Wahnström, Phys. Rev. B **46**, (1992) (in press).

7.  M. J. Gillan, Phys. Rev. Lett. **58**, 563 (1987); Phil. Mag. A **38**, 257 (1988); J. Less-Common Metals **172-174**, 529 (1991).

8.  F. Christodoulos and M. J. Gillan, Phil. Mag. B **63**, 641 (1991); J. Phys.: Condens. Matter **3**, 9429 (1991).

9.  S. M. Foiles, M. I. Baskes and M. S. Daw, Phys. Rev. B **33**, 7983 (1986).

10. For improvements in extending the EAM to bcc metals, see A. E. Carlsson, Phys. Rev. B **44**, 6590 (1991); W. Xu, J. B. Adams and S. M. Foiles, (preprint).

11. T. Springer, in Ref. [1], page 75.

12. J. Völkl and G. Alefeld, in Ref. [1], page 321.

13. J. J. Rush, J. M. Rowe, and D. Richter, Z. Phys. B, **55**, 283 (1984).

14. P. A. Egelstaff, *An Introduction to the Liquid State*, (Academic Press, London, 1967).

15. K. Sköld and G. Nelin, J. Phys. Chem. Solids **28**, 2369 (1967).

16. J. M. Rowe *et al.*, Phys. Rev. Lett. **29**, 1250 (1972).

17. C. J. Carlile and D. K. Ross, Solid State Commun. **15**, 1923 (1974).

18. C. T. Chudley and R. J. Elliott, Proc. Phys. Soc. London **77**, 353 (1961).

19. M. J. Gillan, J. Phys. C: Solid State Phys. **19**, 6169 (1986).

20. Y. Li and G. Wahnström, (to be published).

21. K. Sköld, in Ref. [1], page 267.

22. V. Lottner *et al.*, J. Phys. Chem. Solids **40**, 557 (1979).

23. H. Dosch *et al.*, Phys. Rev. B **46**, 55 (1992).