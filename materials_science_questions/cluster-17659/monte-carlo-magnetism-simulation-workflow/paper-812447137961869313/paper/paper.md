# Monte Carlo studies of random anisotropy magnets

D.R. Denholm $^{a,b}$, B.D. Rainford $^{a}$ and T.J. Sluckin $^{b}$
$^{a}$ Department of Physics and $^{b}$ Faculty of Mathematical Studies, University of Southampton, Southampton SO9 5NH, UK

We have carried out systematic studies of the $d=2$, $n=2$, HPZ model of random magnetic anisotropy, using standard Monte Carlo methods. The non-random, $D=0$, case is the usual two-dimensional $XY$ model and exhibits no magnetism or hysteresis at any temperature. We find that at finite $D/J$ (where $J$ is the magnetic exchange) there are significant hysteretic and other irreversible effects. We find, over the Monte Carlo time scales that we run our simulations, four well-delineated regions as a function of temperature: a locked spin glass phase at low $T$, an intermediate regime in which the spins are correlated to the original directions, a region of algebraic order of the Kosterlitz-Thouless type in which the anisotropy is irrelevant, and a high temperature disordered phase.

The magnetic properties of amorphous rare earth alloys are still incompletely understood [1]. The complexity in the magnetic properties of these materials arises from the spatial disorder present in the random alloy, which causes a randomness in the magnetocrystalline anisotropy, so that the local easy axis of magnetisation varies randomly from site to site. This local anisotropy is due to the action of the crystalline electric field on the large orbital angular momentum of the partly filled 4f shell. The effect of the randomness on the anisotropy energy is profound. A simple model Hamiltonian describing this case, first introduced by Harris, Plischke and Zuckermann [2] (HPZ), is:

$$
\mathscr{H}=-J \sum_{i j} S_{i} \cdot S_{j}-D \sum_{i}\left(S_{i} \cdot n_{i}\right)^{2}-\sum_{i}\left(S_{i} \cdot H\right),
$$

where $J$ is the (ferromagnetic) exchange integral, $D$ is the anisotropy constant, $H$ is the applied magnetic field, the sum is taken over sites $i$, or nearest neighbour sites $i$ and $j$, on a regular lattice, and $n_{i}$ is a random unit vector at site $i$. This model has been the subject of much theoretical [3] and computational [4-8] study.

Qualitative arguments of the Imry-Ma [9] type predict that in $d$-dimensional systems ($d<4$), the HPZ model does not sustain long-range order, though there will be short range order with a correlation length $\xi \sim (J/D)^{2/(4-d)}$. Attempts to check this and related results directly by computer simulation have run into a number of problems related to system size and the difficulty of reaching true thermodynamic equilibrium. Chakrabarti [8] calculated a spin-glass [10] order parameter and asserted that the HPZ model has a low temperature spin glass phase. Fisch [11] finds that the $D=\infty$, $d=3$ HPZ model exhibits long range algebraic order; $g(r) \sim r^{-0.6}$, in agreement with some experimental studies [12].

Although previous studies [5,7,8,11] suggest that the standard Metropolis algorithm, in which spins are sites are flipped individually, does not suffice to reach true thermodynamic equilibrium, we have adopted this procedure. If there are true non-ergodic features to the phase diagram, they will appear (albeit at lower temperatures) regardless of the smartness of the spin-flip algorithm.

As a first step, we are studying the simplest form of the HPZ model, in which there are two spin and two spatial dimensions. The $D=0$, non-random version of this model is the two-dimensional $XY$ model, whose properties have been exhaustively studied over the years [13]. We have studies system sizes $8 \times 8$, $16 \times 16$, $32 \times 32$, $64 \times 64$ and $128 \times 128$, with production runs from very short up to $10^{6}$ Monte Carlo cycles (1 cycle = one Monte Carlo time step per spin). Most of our normal production runs are on $64 \times 64$ systems. We have sought to vary systematically the various parameters of the problem, such as disorder $D$, magnetic field $H$, temperature $T$ (all measured in units of the exchange integral $J$), and the experimental run time $\tau$ (measured in Monte Carlo cycles).

A common criterion for the existence of magnetism in a given material is the presence of hysteresis loops in the $M$ vs $H$ characteristic. The hysteresis loops of amorphous rare earth alloys show bumpy and irreproducible features. In fig. 1, we show a typical hysteresis curve observed in one of our computer experiments. (Irreproducible) steps in the $M$ vs $H$ characteristic, which bear considerable resemblance to features observed experimentally, can be seen. Similar curves were seen by Dieny and Barbara [6] in their zero temperature simulations of precisely the same model. We can identify two crucial magnetic fields in this run; (a) the coercive field $H_{\text{co}}$, required to (just) reverse the magnetisation direction and (b) the critical reversible field $H_{\text{rev}}$, required that the same magnetisation be measured no matter what the history of the sample.

We can now collect together the hysteresis data from many different simulations. The curve $H_{\text{rev}}(T)$ for a given $D$ may be thought of as analogous to the De

![](./images/812447137961869313_1.jpg)

Fig. 1. $M$ vs $H$ for $D/J=0.4$, $T/J=0.1$, showing irreproducible features.

![](./images/812447137961869313_2.jpg)

Fig. 2. $H_{\text{co}}(T)$ for five values of $D$.

Almeida-Thouless line [14] separating ergodic and non-ergodic regions in the spin-glass phase diagram. We find that it is easier computationally to plot $H_{\text{co}}(T)$; the ratio of $H_{\text{co}}$ and $H_{\text{rev}}$ is more or less constant in any given situation. A series of such plots, for various values of $D$, is shown in fig. 2. It will be seen that hysteresis ceases above $T_{\text{c}} \simeq 1.1$, which we identify with the Kosterlitz-Thouless ordering temperature.

We have also studied the behaviour of quenched systems. In fig. 3. we show the behaviour of $M(T)$ at zero magnetic field for a system quenched from a random configuration to $T=0$ and slowly heated up. It will be seen that the magnetisation reaches a maximum at $T \simeq 0.6$, suggesting a glassification transition at about this temperature. Further studies over very long relaxation times confirm this point of view. These studies start with a perfectly aligned state and run for $10^{6}$ cycles. From these long runs the following picture emerges. At very low temperatures the system is glassified and the final (stable) configuration remembers the initial configuration. At higher temperatures the initial configuration is forgotten and the system on average lies along the easy anisotropy direction closest to the initial direction. At higher temperatures still, even this memory is lost, and the system is in a Kosterlitz-Thouless state; apparently in this regime the randomness is irrelevant. Finally above the Kosterlitz-Thouless temperature the spins are completely disordered. This seems to be more or less independent of $D$ in the systems we have tested, and finite size scaling studies identify reasonably unambiguously the crossover between the last two behaviours.

![](./images/812447137961869313_3.jpg)

Fig. 3. $M(T)$ for a system quenched to $T=0$, then warmed.

We have investigated the $XY$ model in two dimensions with random anisotropy. We find, as do other authors, strong evidence of irreversible behaviour in the low temperature regime, but at this stage it is not yet clear whether this is true spin-glass-like order. Further studies will enable more detailed comparison between simulation and both experiment and theory; space has precluded us giving a more detailed description of the evidence we have gathered so far.

### References

[1] R.W. Cochrane, R. Harris and M.J. Zuckermann, Phys. Rep. 48 (1978) 1.
[2] R. Harris, M. Plischke and M.J. Zuckermann, Phys. Rev. Lett. 31 (1973) 160.
[3] A. Aharony and E. Pytte, Phys. Rev. Lett. 45 (1980) 1583. E.M. Chudnovsky, J. Magn. Magn. Mater. 79 (1989) 127. Y.Y. Goldschmidt, Nucl. Phys. B 220 (1982) 351-65. E.M. Chudnovsky, W.M. Saslow and R.A. Serota, Phys. Rev. B 33 (1986) 251.
[4] M.C. Chi and R. Alben, J. Appl. Phys. 48 (1977) 2987.
[5] C. Jayaprakash and S. Kirkpatrick, Phys. Rev. B 21 (1980) 4072.
[6] B. Dieny and B. Barbara, Phys. Rev. B 41 (1990) 11549.
[7] R. Fisch, Phys. Rev. B 39 (1989) 873.
[8] A. Chakrabarti, J. Appl. Phys. 63 (1988) 3735.
[9] Y. Imry and S.K. Ma, Phys. Rev. Lett. 35 (1975) 1399.
[10] N.D. Mackenzie and A.P. Young, Phys. Rev. Lett. 49 (1982) 301.
[11] R. Fisch, Phys. Rev. Lett. 66 (1991) 2041.
[12] S.J. Pickart, J.J. Rhyne and H.A. Alperin, Phys. Rev. Lett. 33 (1974) 424.
[13] J.M. Kosterlitz and D.J. Thouless, J. Phys. C 6 (1973) 1181.
[14] J.R.L. De Almeida and D.J. Thouless, J. Phys. A 11 (1978) 983.