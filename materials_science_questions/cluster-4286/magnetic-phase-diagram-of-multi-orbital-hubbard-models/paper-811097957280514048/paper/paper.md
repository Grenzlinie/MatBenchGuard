# Hartree-Fock study of the magnetism in the single-band Hubbard model

M. Inui* and P. B. Littlewood
AT&T Bell Laboratories, Murray Hill, New Jersey 07974
(Received 27 August 1990; revised manuscript received 11 March 1991)

We study the magnetic phases of the single-band Hubbard model within the self-consistent Hartree- Fock formalism applied to a large supercell. We find that incommensurate spin-density waves gradually deform into domain walls with increasing correlation energy $U$, in agreement with previous studies. For $U/t>8$ the domain walls evaporate into separated magnetic polarons. For $U/t<20$, the spin expectation values are collinear. However, we find clear evidence for the importance of the transverse spin components in the large-correlation limit, although the exact ground state cannot be determined. The connection between the resulting band structures and photoabsorption and optical data is discussed.

## I. INTRODUCTION

The single-band Hubbard model has been under intense study since the discovery of high-temperature (high-$T_c$) superconductivity. Though this simple model is likely to contain the correct qualitative properties of low-energy excitations associated with magnetism, until recently few attempts have been made $^{1}$ to elucidate what possible phases to expect as doping and the correlation energy $U$ are varied. Because of the difficulty of calculations in the strong-correlation limit, discussions of this problem have often been based on plausibility rather than concrete results.

It is known that a linearly polarized incommensurate spin-density wave develops at the phase boundary between magnetic and metallic phases. $^{2}$ In addition, recent studies $^{3}$ have shown that a linearly polarized Hartree Fock decomposition results in holes staying along boundaries between antiferromagnetic (AF) domains. In the two-band Hubbard model, a domain wall has been found to be stable with one set of parameters. $^{4}$ However, for large correlation (large $U/t$) and small doping, (i.e., far away from the boundary to paramagnetism) it is not clear if these are the only relevant phases. In particular, the importance of transverse spin components and the possibility of a spiral phase $^{5}$ remains open.

In this paper, we attempt a systematic study of the Hubbard model near half-filling within the Hartree-Fock (HF) approximation. We use a large supercell and do not impose any restriction on the local moment's amplitude and direction; this allows any magnetically ordered phases to develop so long as they respect the given boundary conditions. Our calculations are performed in a supercell with up to 121 sites; for smaller cells, $k$-point sampling was used to give comparable numerical accuracy.

We find that for any hole concentration and for $U/t\leq20$ ($U/t$ is the ratio of correlation energy to the hopping), the spin configuration remains linearly polarized, without any indication of a spiral phase. Near the boundary to the paramagnetic phase (small doping and $U/t$), we observe incommensurate AF spin-density waves (SDW's) $^{6}$ in the (1,0) or (0,1) direction, which transform smoothly to an array of sharp domain walls as $U/t$ is increased. The "vertical" [i.e., walls perpendicular to the (1,0) or (0,1) direction] and "diagonal" [i.e., perpendicular to (1,1) or (1,-1)] domain walls cross in energy at a value of $U/t\sim3.6$ for small doping, as first suggested by Schulz $^{7}$ from a Landau expansion of the free energy (and who found the crossover at $U/t=4.5$). For $U/t\geq8$, the domain-wall states are unstable toward localized small ferromagnetic polarons. These repel weakly and form a Wigner crystal (at least in the HF approximation) at low temperatures. With increasing temperature, the domain wall or polaron structure disappears in favor of the commensurate AF phase, also in agreement with Schulz.

As the ratio $U/t$ is further increased, it becomes difficult to obtain self-consistent solutions. However, we have observed that the transverse components of the spins become important (i.e., spins are not collinear). However, we do find that spiral order, as suggested from studies of the $t-J$ model, $^{5}$ is not stable in this regime within the HF approximation.

Within the parameter range where domain walls (either vertical or diagonal) or polarons are stable, the addition of holes results in the creation of empty states within the Hubbard gap. This may provide a qualitative insight to the photoabsorption and infrared experiments where doped samples show additional absorption peaks within the gap.

## II. HARTREE-FOCK APPROXIMATION

We use the standard Hartree-Fock decomposition method on the single-band Hubbard model on a square lattice which keeps both $z$ and $xy$ components of the spins,
$$
\begin{aligned}
H_{\mathrm{HF}}= & -t \sum_{\langle i, j\rangle, \sigma}\left(c_{i \sigma}^{\dagger} c_{j \sigma}+c_{j \sigma}^{\dagger} c_{i \sigma}\right) \\
& +U \sum_{i}\left(n_{i \uparrow}\left\langle n_{i \downarrow}\right\rangle+\left\langle n_{i \uparrow}\right\rangle n_{i \downarrow}-\left\langle S_{i}^{+}\right\rangle S_{i}^{-}-S_{i}^{+}\left\langle S_{i}^{-}\right\rangle\right) \\
& -U \sum_{i}\left(\left\langle n_{i \uparrow}\right\rangle\left\langle n_{i \downarrow}\right\rangle-\left\langle S_{i}^{+}\right\rangle\left\langle S_{i}^{-}\right\rangle\right).
\end{aligned}\qquad(1)
$$
This Hamiltonian can be easily diagonalized, and we find self-consistent solutions by iteration. We have used

periodic, antiperiodic, and free (or combinations of these) boundary conditions on lattices containing up to 121 sites.

The computation of the energy of domain-wall structures (see the discussion below) requires a careful choice of supercell, since it is essential that a wall does not terminate with an "edge." The energy of a domain wall, due to its one-dimensional nature, can be computed accurately by using a rectangular supercell elongated perpendicular to the walls and applying periodic boundary conditions; e.g., for the doping level of two holes in 66 sites, we have used a supercell $(33,0) \times(0,2)$ for studying vertical walls and $(33,33) \times(1,-1)$ for diagonal walls. Note that the boundary conditions dictate, which of the two types of domain walls is formed in such a supercell, regardless of the value of $U / t$ (so long as doping is kept low). In order to compensate for the reduced cell size, we sample a number of $k$ points in the reduced Brillouin zone in the direction that has only a few sites in order to have a sufficient number of available states. This reduces systematic errors occasioned by calculations for different system sizes.

We further emphasize that, in the absence of proper finite-size scaling studies, one must check all plausible supercell shapes in order to assess the effects of imposed boundary conditions. For instance, the study by Bishop et $a l .{ }^{8}$ on a $12 \times 12$ lattice showed that domain walls with two or six holes have higher energy than separated polarons (see below). We believe this to be an artifact of inappropriate boundary conditions. One requires, for $12 \times 12$ lattice, 12 holes in order to have a "straight" wall (where, in fact, they report a lower energy for a domain wall, in agreement with our study). At all other filling values, their domain walls are only partially populated by holes; the system would prefer to adjust the domain-wall periodicity so as to have a full occupation, and lower energy.

Because of computational limitations, we have limited the system size to less than 121 sites. With a smaller superlattice size, the smallness is compensated by sampling a number of $k$ points in the reduced Brillouin zone. Typically the number of sites in a given direction [e.g., 16 in the $x$ direction and 2 in the $y$ direction for an $(16,0) \times(0,2)$ lattice] times the number of $k$ points in the same direction is kept sufficiently large. The total number of states $N_{\text {state }}$ considered, which is the product of twice the number of sites $(2 N)$ times the number of $k$ points $\left(N_{k}\right)$, is kept greater than 200. Since the computation time for the diagonalization of the HF Hamiltonian (a complex $2 N \times 2 N$ Hermitian matrix) grows as $8 N^{3}$, keeping $N_{\text {state }}$ constant involves an $N^{2}$ increase in computing time for a larger system size. Thus, typically, a square lattice larger than $10 \times 10$ has only $N_{k}=1$ (resulting in $N_{\text {state }} \geq 200$ ) at $\mathbf{k}=(0,0)$, whereas for a typical size used for computing accurate HF energies (64 66 sites), we used $N_{k}=16$, resulting $N_{\text {state }}=2048$.

The layout of the $k$ points sampled depends on the shape of the supercell. If the cell is defined by two orthogonal vectors $\mathbf{L}_{1}$ and $\mathbf{L}_{2}$ where $\left|\mathbf{L}_{1}\right| \gg\left|\mathbf{L}_{2}\right|$ then the sampled $k$ points are given by $k_{1}=0$, $k_{2}= \pm\left(2 \pi / N_{k}\left|\mathbf{L}_{2}\right|\right)\left(m-\frac{1}{2}\right), \quad\left(m=1,2, \ldots, N_{k} / 2\right)$ with $\mathbf{k}=k_{1} \mathbf{e}_{1}+k_{2} \mathbf{e}_{2}$ and $\mathbf{e}_{i}=\mathbf{L}_{i} /\left|\mathbf{L}_{i}\right| \quad(i=1,2)$. For a square cell, on the other hand, we use a square mesh. Let $\left|\mathbf{L}_{1}\right|=\left|\mathbf{L}_{2}\right|$ and further let $N_{k}=M_{k}^{2}$ with integer $M_{k}$, then the sampled $k$ points are simply $k_{i}= \pm\left(2 \pi / M_{k}\left|\mathbf{L}_{i}\right|\right)\left(m_{i}=\frac{1}{2}\right)\left(i=1,2\right.$ and $\left.m_{i}=1,2, \ldots, M_{k} / 2\right)$. For example, the $(32,0) \times(0,2)$ cell took $N_{k}=16$ with $\mathbf{k}= \pm(\pi / 32)(2 m-1) \mathbf{e}_{y}$ $(m=1,2, \ldots, 8)$; and a square cell of $(8,0) \times(0,8)$ required
$$
\begin{aligned}
\mathbf{k}= \pm(\pi / 32)\left(2 m_{1}-1\right) \mathbf{e}_{x} \pm(\pi / 32)\left(2 m_{2}-1\right) \mathbf{e}_{y} & \\
& \left(m_{i}=1,2\right)
\end{aligned}
$$
for the same $N_{k}$. The error in computing the energy per site from insufficient $k$-point sampling, etc., is somewhat $U$ dependent (increasing with decreasing $(U / t)$ but typically $\lesssim 0.0003 t$.

In our calculation, we have avoided an infinitely sharp Fermi surface at $t=0$ because of finite-size-induced symmetry-breaking effects on degenerate states at the Fermi energy. We have, instead, used $T \leq 0.001 t$ for the "zero-temperature" calculation.

The convergence toward the self-consistent solution as the Hamiltonian $H_{\mathrm{HF}}$ is iteratively applied is generally "overdamped" in that the system shows no tendency to oscillate about the self-consistent solution. The convergence is checked by evaluating the quantity
$$
\left[\frac{1}{N} \sum_{i}\left[\mathbf{S}_{i}^{(n)}-\mathbf{S}_{i}^{(n-1)}\right)^{2}+\left(p_{i}^{(n)}-p_{i}^{(n-1)}\right)^{2}\right]^{1 / 2},
$$
where $\mathbf{S}_{i}^{(n)}$ and $p_{i}^{(n)}$ are the spin and charge expectation values at site $i$ after $n$ iterations. In order to accelerate the convergence, we have used various forms of predictor schemes which increase the convergence rate by factor of $\sim 5$ for small $U / t$. The simplest of these methods is to assume an exponential convergence for every spin and charge component,
$$
f^{(n+1)} \leftarrow \frac{\left(f^{(n-1)}\right)^{2}-f^{(n)} f^{(n-2)}}{f^{(n-1)}-f^{(n)}}
$$
where $f^{(n)}$ stands for $x, y$, or $z$ component of $\mathbf{S}_{i}^{(n)}$ or $p^{(n)}$. We have applied Eq. (3) every 4-5 iterations (after 50-100 initial relaxation steps) to be the components that seemed to be following an exponential trajectory, i.e., when the "slope" does not change sign and its magnitude is decreasing, or $\left(f^{(n)}-f^{(n-1)}\right)\left(f^{(n-1)}-f^{(n-2)}\right)>0$ and $\left|f^{(n)}-f^{(n-1)}\right|<\left|f^{(n-1)}-f^{(n-2)}\right|$.

We have generally started our system from a random configuration with small spin components. This worked well for $U / t \lesssim 7$. However, for larger values of $U / t$, the convergence becomes slow and the final self-consistent solution, if obtained, nonunique. In such circumstances, we have often started from an ordered phase (commensurate AF, domain walls, spiral phase, etc.) with small added noise and checked their stability.

Determining which of the different self-consistent solutions is the most favorable can be difficult to judge for a doped system with different supercells and boundary conditions. We study the competition between vertical domain walls, diagonal domain walls, and polarons in

two ways. One is the comparison of energy gains over uniform charge and spin state for a fixed number of sites, as suggested by Schulz. $^{7}$ Another is checking of the stability of a given domain wall as $U / t$ is varied with free boundary conditions. We find the former method to be far less ambiguous and adopt this criterion for our discussions.

## III. RESULTS
We now proceed to discuss our results. For small doping, we find a commensurate AF phase at high enough temperatures for any value of $U / t$. However, as temperature is lowered toward zero, it always becomes unstable for nonzero doping. Since there are several possible phases which have nonuniform charge and spin density we discuss these $T \to 0$ phases in this section.

When a single hole is forced on a supercell at $T=0$, a linearly polarized spin polaron is formed, where charge density as well as spin magnitude is locally depressed, in agreement with previous studies. $^{9}$ The polarons are found to be quite compact for $U / t \lesssim 20$ in that the ferromagnetic bonds are only the four adjacent to the local charge depression peak. $^{10}$

However, for a small $U / t$, when a multiple number of these polarons are placed on a large cell (typically $10 \times 10$ ), they bind to form a line, suggesting a possible formation of a domain wall or spin bags. We find that a spin-bag configuration with multiple holes in the bag deforms to a domain wall for the several values of $U / t$ we have checked. Therefore we will ignore this possibility for the rest of this paper, and compare the energies for polarons in square supercells and domain walls in rectangular cells. For a finite but small concentration of holes, the system clearly shows a tendency to form a domain-wall structure. Here, we mean by domain walls the localized holes arranged in a straight line, with the charge and spins away from the walls rapidly approaching the undoped AF values. By using various combinations of boundary conditions and doping, we find that the vertical domain wall contains one hole per unit length along the wall, whereas in a diagonal wall holes are more spread out [i.e., one hole per $(1,1) \times(-1,1)$ unit]. Also, we have established that a domain wall separates two AF phases with opposite sublattice magnetization through a gradual change of spin magnitude across the domain wall. This implies that one must be careful in choosing the size of rectangular supercell in order not to frustrate the system.

We find that for $U / t=3$, a vertical wall is clearly favored, whereas $U / t=5$ gives diagonal walls. To find the crossover, we have computed the energy (per site) gained by creating domain walls or collinear spin polarons over the state with uniform AF spins and charge. (Error is estimated at $\lesssim 0.0003 t$.) We observe that the interaction between walls or polarons is repulsive and very small for small doping $(\delta \lesssim 0.08)$ for $3 \lesssim U / t \lesssim 15$, since they are separated far from each other. Thus, the per hole energy gain is practically doping independent for the low doping levels we have studied, viz., $\delta=\frac{1}{16}, \frac{1}{32}$, and $\frac{1}{33}$ (difference smaller than one part in $10^{3}$ ). We show in Fig. 1 the energy gain per site for $\delta=\frac{1}{32}$ for the two types of domain walls and polarons. $^{10}$ The lines drawn are parametric spline fits to the numerical data. Note that the points for the vertical walls for $U / t \geq 7$ are saddle points and are unstable to buckling (making a zigzag line) because of the lower energy of diagonal walls, and that the diagonal walls are unstable beyond $U / t=10$ [where our calculation places two holes in $(32,32) \times(-1,1)$ supercell]. The vertical-to-diagonal crossover occurs at $U / t \approx 3.6$. This is in qualitative agreement with Schulz, $^{7}$ though the value is somewhat lower than his result of 4.8. A further increase in $U / t$ results in another crossover from diagonal walls to independent polarons at $U / t \approx 8.0$, effectively "evaporating" the wall structure. This is probably an indication that the (short-range) interaction between holes changes from attractive to repulsive as we increase $U / t$.

![](./images/811097957280514048_1.jpg)

FIG. 1. Energy per site (in units of $t$ ) for vertical domain walls (solid line), diagonal domain walls (dashed line), and polarons (dotted line), with hole concentrations $\delta \lesssim 1 / 32=0.0625$. Energies are measured with respect to the uniform AF state.

Note the domain walls and polarons are locked to the underlying lattice and cannot be continuously translated. Hence the existence of polarons does not imply simple metallic behavior; the low-temperature HF state is crystalline and insulating unless the whole pattern is sliding.

One way to look at domain walls is to associate them with increased harmonic content in the SDW. Although it is clear that higher harmonics can be ignored for small $U / t$ within perturbation theory, our self-consistent solution shows that this is no longer a valid approximation for $U / t \gtrsim 3$. Figure 2 shows the dependence of the SDW shape on increasing $U / t$. Note that the SDW's are approximately sinusoidal for small $U / t$ but gradually deform to sharp domain walls; the interaction between walls is reduced because of the strong localization of holes.

Within the parameter range where domain walls are stable, increased doping simply decreases the distance between them. At very low doping, the interaction between the walls can be ignored because it falls off exponentially with separation (neglecting the long-range Coulomb

![](./images/811097957280514048_2.jpg)

FIG. 2. Spin expectation values around a vertical domain wall for varying $U/t$ on $(33,0)\times(0,2)$ supercell. Spins on one antiferromagnetic sublattice have been flipped for ease of viewing. The change in spin direction across the domain wall corresponds to a reversal of the AF sublattice magnetization. We have used a rectangular supercell to suppress the vertical to diagonal crossover.

repulsion). However, since the walls do interact repulsively with each other at shorter distances, vertical walls are expected to become more stable than diagonal ones at large doping levels even for $U/t\gtrsim3.6$. (Recall that the distance between two diagonal walls is $1/\sqrt{2}$ of that vertical walls at the same doping.) This behavior is natural because when the system approaches the paramagnetic (metallic) phase with increased doping, it must form SDW's with the wave vector pointing in the $(1,0)$ or $(0,1)$ direction. Regardless of the value of $U/t$, it must form vertical domain walls at sufficiently large doping. However, the crossover from diagonal to vertical walls is difficult to investigate numerically because of the closeness to the nonmagnetic phase at high doping levels.

We have also not studied carefully the transition to the paramagnetic phase. We have stressed above that localization of holes in a midgap state in the domain walls forces the periodicity of the DW lattice to be inversely proportional to the doping. However, the wave vector at which the paramagnetic phase goes unstable is determined by nesting of a Fermi surface $^{1}$ and is different. Thus there is expected to be a "locking" transition, where the $Q$ vector of the magnetic order varies continuously before locking at a value of $2\pi/\delta$. At the same point will come a semimetal to insulator transition where conductivity by quasiparticles vanishes, and there is a gap in the single-particle spectrum. (Depending on whether the domain wall array is commensurately locked to the underlying lattice, there may still be conductivity from collective "sliding" of the structure.)

Calculations with $U/t$ beyond $\approx10$ are hampered by extremely slow convergence; we also observe a significant deviation from "collinear" spin configurations which does not converge in 1000-2000 iterations. We have tried in various ways to find out the lowest energy configurations in this range, but we have been unable to do so. A part of the problem stems from the fact that spin amplitudes become large everywhere in the system, including the sites where holes are found. Thus, when the spins are "twisted," the system has difficulty in undoing the twist; i.e., the system starts to develop a capacity for topological defects that cannot easily be removed. Thus a random initial configuration leads to neither an ordered phase nor a unique spin/charge state. In the case of small $U/t$, the spin amplitudes are small at hole sites (i.e., along the domain walls) and topological defects are easily removed as $H_{\text{HF}}$ is repeatedly applied. The large number of metastable states in spin-configuration space contributes to a slowdown of convergence accompanied by large drifts of spin components, and we cannot implement a method that can intelligently predict where the spin configuration is approaching.

One can, nevertheless, make several observations for large $U/t$ by checking whether an ordered initial configuration is stable as we iteratively apply the Hartree-Fock Hamiltonian. We find that states that seemed plausible to us as the mean-field ground state are all unstable. We have tried different types of domain walls, spiral phase, large ferromagnetic polarons (spin bags), commensurate AF, and SDW and saw significant departure from these states.

The only stable initial configuration (i.e., that can withstand a small perturbation and is not a saddle point) we found for $U/t\gtrsim11$ is that of spin polarons on a square cell, which does not lose its stability until $U/t\gtrsim20$. From this study, we can state the following: Two holes do not bind together to form a pair; one hole creates a localized ferromagnetic polaron whose physical size increases with $U/t$ beyond $\sim20$; as the size of such a polaron becomes large (a few unit cells with ferromagnetic spin alignment), the spins inside or near the polaron cease to be collinear; i.e., the spins are no longer aligned in one direction. The last of these is seen to happen at $U/t\gtrsim25$, in rough agreement with the results of Singh and Tesanović. $^{9}$ One must, however, note that such a study is at best suspicious, since a few holes in a large square lattice (say $10\times10$) does not correspond to a finite hole concentration in the real system, and the configuration is possibly only metastable (we were never able to find a polaron by iteration from a random initial configuration with $U/t\gtrsim10$). For this reason, unfortunately, we cannot conclude anything of substance from our study of one or two holes in a large cell at large $U/t$, since there may be another state that is more stable than independent polarons.

We have not studied extensively the vortex states discussed by Bishop et al. $^{8}$ We find that for $U/t\lesssim15$ the vortex state is much higher in energy than that of pola-

rons regardless of the choice of boundary conditions (free, periodic, or antiperiodic). We also believe that the comparison of Bishop *et al.* between polarons and vor- tices (where they found polarons to be more stable) can be trusted because neither are as sensitive to boundary conditions.

Another possibility we did not pursue is that of "cross- ing" domain walls. $^{11}$ At the small doping levels we are concerned with, the creation of vertices will be more cost- ly than the gain one might find in placing the walls fur- ther apart. (Recall that the interaction energy is extreme- ly small for $\delta<0.08$ .) Obviously, however, at higher dop ing, one should consider such possibilities.

Finally, as we mentioned at the beginning of this sec- tion, the nonuniform $T \to 0$ phases disappear with in creased temperature. This transition temperature (call it $T_U$) from nonuniform AF or metal is dependent on dop- ing and the ratio $U / t$ . We find in our limited study that $T_{U}$ increases with $U / t$ , up to at least $U / t=12$ for a dop ing of $\delta=\frac{1}{32}$ . This increase is hardly surprising, since the increase in the correlation energy makes the AF order parameter larger, and that contributes to the stability of the nonuniform structure. Obviously, however, further increase in $U / t$ eventually saturates $S_{i}$ , and then the de crease in the spin stiffness (varying as $J=4 t^{2} / U$ ) starts to take effect, thus reducing $T_{U}$ . Thus one expects $T_{U}$ to have a peak as $U / t$ is varied, which therefore must be lo cated at $U / t$ larger than 12.

## IV. COMPARISON WITH OTHER METHODS
Next we point out the similarities and differences be- tween our results and other approximate methods for the Hubbard model. The principal advantage of the HF ap- proach is the ability to study comparatively large-size systems. On the other hand, its disadvantage lies in the uncertainty of the stability of the HF ground states against quantum fluctuations, and the disagreement with known results may indicate the problems associated with our study.

The works that are closely relevant to ours are the variational Monte Carlo (VMC) studies of Yokoyama and Shiba, $^{12}$ and later by Giamarchi and Lhuillier, $^{13}$ and Coppersmith and Yu. $^{14}$ The first makes a comparison between the HF method and the Gutzwiller wave func- tion $^{15}$ VMC as well as quantum Monte Carlo (QMC) re sults. $^{16}$ They find that HF, at least at half-filling, gives energies close to those of other methods, although HF and VMC both overestimate the magnitude of the sublat- tice magnetization compared to QMC. Away from half- filling, on the other hand, it has been shown that a Gutzwiller variational wave function does show the domain-wall structures similar to the ones reported here and in Ref. 3. $^{13}$ This qualitative agreement is an indica tion that the inclusion of the quantum fluctuations may not necessarily destroy the inhomogeneous magnetic phases. The energy gain over the uniform AF state, how- ever, was found to be smaller for the VMC case. We also note that finite-size and exact-diagonalization studies on small systems (up to 16 sites) $^{17}$ indicate that the binding energy of two holes becomes negative (i.e., they repel) for U/t≥9. This is close to the value where we found that domain walls evaporate to form a polaron lattice.

The comparison with exact diagonalization studies is hampered by the fact that diagonalization involves only a few holes in a small lattice and that their geometry (typi- cally square) does not favor wall-type structures. In Table I, we compare results from our HF calculations with exact diagonalization results on 8- and 10-site lat- tices. $^{17}$ We have used identical geometries to those of the exact diagonalizations, but we compensate for the finite size by using periodic boundary conditions and $k$ -point sampling, as described above. Our calculations are thus for a periodic array, rather than a finite cluster. Never- theless, the trends in both sets of calculations are similar, and the energies per hole are comparable. Most impor- tantly from our point of view, the finite-size fluctuations in the exact calculation are comparable or larger to their differences from the HF results.

Some estimate of the "error" in the Hartree- Fock results can be obtained from $\sigma=\sqrt{\langle\psi_{HF}|(H-H_{HF})^{2}| \psi_{HF}\rangle}$ . For the configurations shown in the table, $\sigma$ increases from zero (at $U=0$ ) to a maximum value of $\sim 0.3 t$ per site at intermediate cou pling, and decreases with large $U$ . The HF states shown in the table are, however, not the HF ground states at that doping (which would be domain walls). In the domain-wall states, we find $\sigma \lesssim 0.12 t$ . Unfortunately, this error estimate is not a useful guide for our purposes, because we are concerned with the *difference* in energy of alternative ordered states; the value of $\sigma$ represents prin cipally the error in the description of the commensurate antiferromagnet.

In general, comparison with more sophisticated methods yields quantitative differences as expected but we find no qualitative contradictions. Clearly, on physi- cal grounds, there are questions to be answered and some qualifications have to be made (see below). Nevertheless, it must be evident that in order to make a meaningful

<table>
<caption>TABLE I. Comparison of exact diagonalization results for the Hubbard model on eight and ten-site lattices (from Ref. 17) with Hartree-Fock. $E_{g}$ is the ground-state energy of half-filling, and $E_{h}$ the energy to add one hole.</caption>
<thead>
<tr>
<th rowspan="2">$U/t$</th>
<th colspan="2">Exact diagonalization</th>
<th colspan="2">Hartree-Fock</th>
</tr>
<tr>
<th>$E_{g}/t$</th>
<th>$E_{h}/t$</th>
<th>$E_{g}/t$</th>
<th>$E_{h}/t$</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5">Eight sites</td>
</tr>
<tr>
<td>0</td>
<td>-8.00</td>
<td>0.00</td>
<td>-12.96</td>
<td>0.109</td>
</tr>
<tr>
<td>1</td>
<td>-7.19</td>
<td>-0.126</td>
<td>-10.97</td>
<td>-0.351</td>
</tr>
<tr>
<td>2</td>
<td>-6.47</td>
<td>-0.250</td>
<td>-9.11</td>
<td>-0.683</td>
</tr>
<tr>
<td>4</td>
<td>-5.32</td>
<td>-0.481</td>
<td>-6.38</td>
<td>-0.710</td>
</tr>
<tr>
<td>8</td>
<td>-3.78</td>
<td>-0.861</td>
<td>-3.72</td>
<td>-1.058</td>
</tr>
<tr>
<td>10</td>
<td>-3.27</td>
<td>-1.011</td>
<td>-3.05</td>
<td>-1.204</td>
</tr>
<tr>
<td colspan="5">Ten sites</td>
</tr>
<tr>
<td>0</td>
<td>-16.00</td>
<td>1.00</td>
<td>-16.21</td>
<td>0.078</td>
</tr>
<tr>
<td>1</td>
<td>-13.65</td>
<td>0.517</td>
<td>-13.72</td>
<td>-0.388</td>
</tr>
<tr>
<td>2</td>
<td>-11.61</td>
<td>0.066</td>
<td>-11.39</td>
<td>-0.691</td>
</tr>
<tr>
<td>4</td>
<td>-8.40</td>
<td>-0.723</td>
<td>-7.97</td>
<td>-0.726</td>
</tr>
<tr>
<td>8</td>
<td>-5.10</td>
<td>-1.464</td>
<td>-4.66</td>
<td>-1.072</td>
</tr>
<tr>
<td>10</td>
<td>-4.28</td>
<td>-1.617</td>
<td>-3.82</td>
<td>-1.214</td>
</tr>
</tbody>
</table>

comparison between the HF approach and other finite-
size studies (such as QMC and the exact diagonalization),
attention must be paid so that inhomogeneous magnetic
phases are not artificially suppressed.

## V. DISCUSSION AND PHOTOABSORPTION AND OPTICAL EXPERIMENTS

According to our calculation, with small doping and
increasing $U/t$, one should observe a metal, a transition
to a linear SDW in either the $x$ or $y$ direction which de-
forms to sharp vertical domain walls, a transition to diag-
onal domain walls, and then to weakly interacting pola-
rons. Note that the walls and polarons are locked to the
underlying lattice, and the weak interaction among them
does not imply metallic behavior. If the high-$T_c$ materi-
als develop a domain-wall phase or regular spin polaron
lattice, one should be able to observe them by neutron
scattering, provided that there is negligible disorder in
the system.

These low-doping phases, however, are susceptible to
the physics that is ignored by the HF approximation, as
well as the additional effects of long-range Coulomb
forces and the interaction of added holes with impurities
or the dopant atoms themselves. Quantum fluctuations
could lead to "wall wandering" and a destruction of
long-range order. Long-range order should also be lost at
nonzero temperature as $\delta\rightarrow0$, at least in the absence of
long-range Coulomb interactions. Since the incommens-
urate states all have a nonuniform charge distribution,
long-range Coulomb interactions will play an important
role, both by stiffening the polaron or domain-wall lat-
tice, and by changing the relative energetic stability of
commensurate and incommensurate phases. While the
HF approximation undoubtedly gives a poor description
of the low-energy physics, for intermediate energy scales
$\sim t$ it should be more reliable. A more sophisticated cal-
culation might be able to take account of "melting" of
the (domain wall or polaron) lattice, as distinct from the
Stoner-like transition to the paramagnetic metal. It is
realistic to use HF results to describe the types of fluctua-
tion one would see over an AF or metallic background,
but not detailed low-energy physics.

![](./images/811097957280514048_3.jpg)

FIG. 3. A typical band structure obtained in the diagonal
domain-wall phase. Shown is that obtained for two holes in a
$(32,32)\times(-1,1)$ lattice for $U/t=7$. The dashed line marks the
Fermi energy inside the gap.

![](./images/811097957280514048_4.jpg)

FIG. 4. Band gaps vs $U/t$. Three lines correspond to the
gaps for the vertical domain wall (solid), the diagonal domain
wall (dashed) and polarons (dotted). Note that the HF ground
states cross over from vertical domain walls to diagonal domain
walls at $U/t=3.6$, and then to polarons at $U/t=8.0$.

The question of when the polarons become truly
mobile is an interesting one. Since an isolated polaron
can be translated between neighboring lattice sites
without costing energy, it will have a small but nonzero
dispersion. Our HF solutions give a commensurate lat-
tice of polarons (or domain walls) which are therefore in-
sulating; the commensurability pinning energy is, howev-
er, very small. If the doping level is such that the spacing
between domain walls is incommensurate with the under-
lying lattice, Hartree-Fock will probably enforce a long-
period superstructure, and the appearance of tiny
subgaps in the band structure.

Even if stable domain walls or polarons exist, it is not
clear whether the weak interaction between walls or pola-
rons is sufficient to form a regular structure at a low dop-
ing level in the presence of unavoidable disorder. Cer-
tainly any type of disorder will destroy the long-range
spatial coherence; this will be extremely important at low
doping levels when the interaction between added holes is
weak. In the physical system where each added hole is
accompanied by a dopant atom, the first few added holes
are most likely bound to the dopant site, but will have a
local structure similar to that of the HF polaron. At
higher doping levels where the interactions between car-
riers become important, the effects of disorder caused by
impurities or dopants are still important. If there indeed
are domain walls in the physical system, then the walls
will be "pinned" by impurities. Then the equilibrium
structure would be determined by the competition be-
tween the deformation energy (since the walls and pola-
rons tend to be equally spaced from each other) and the
pinning energy. One can imagine that the static and dy-
namic behavior of such a system may be analogous to
those found in charge-density wave (CDW) systems or
flux lattices in superconductors. For the domain walls, a

Landau theory similar to the one developed by McMillan¹⁸ for CDW problems is a suitable starting point.

Within the parameter range where domain walls or polarons are found we obtain a band structure with empty states inside the Hubbard gap (see Fig. 3) separated from the lower band. This comes about because of the reconfiguration of spins and charge density around localized holes, making them look like "impurity bands" in semiconductors.¹⁹ Similar results were reported in the context of the two-band Hubbard model⁴ and the single-band model.¹¹ (This is a further indication that the lightly doped systems are either insulators or semiconductors and not metals.)

One could identify these states with the pre-edge peaks found in the data of x-ray-absorption studies of high-$T_c$ materials. The claim that these peaks do not exist for undoped materials²⁰ is consistent with our result, though it has been disputed recently.²¹

The splitting of the empty states from the lower Hubbard band should also be observable by infrared absorption.²² We find that the splitting between the lower Hubbard band and the states in the gap are weakly dependent on $U$ or the spin exchange energy $J=4t^2/U$ for $U\gtrsim 6$ (see Fig. 4), and it remains roughly in the range $t\sim 2t$. Experiments do indeed show the existence of states within the charge transfer gap,²² but are clearly influenced by attraction of the holes toward the dopant atom. Nevertheless, recent data of Thomas et al.²² on $\text{Nd}_2\text{CuO}_{4-y}$ ($y\sim 0.03$) shows low-energy absorptions with a strong temperature-dependence characteristic of a bound polaron.

Also our calculation suggests that the domain walls disappear for small doping in favor of commensurate AF phase (with uniform charge distribution) at high temperature indicating that the pre-edge peak, for instance, should disappear with increased temperature. The temperature scale for this transition is, however, large. Our calculation shows that the transition temperature (for all polarons to disappear) to be about $T\sim 0.32t$ for $U/t=8$ and $T\sim 0.49t$ for $U/t=12$, which are of the same order of Néel temperature and naive substitution of $t=0.5$ eV would result in a few thousand degrees. We should identify this with the characteristic Stoner temperature of a magnet, where the local moments disappear. Fluctuations beyond the HF approximation will undoubtedly destroy long-range order at a lower temperature.

The doped material studied in most experiments are not magnetic (except at very low doping levels) whereas our mean-field interpretation only makes sense when there are significant magnetic moments in the system. Hartree-Fock can only generate local moments concomitantly with long-range magnetic order. Therefore, for these ideas to be appropriate, it must be assumed that there are sufficient spin fluctuations even in the doped systems that are not seen in static measurements. This is consistent with some interpretations of NMR data,²³ as well as neutron-scattering measurements.²⁴ Our calculation suggests that the number of states contributing to the infrared peak should grow linearly with doping, whereas experimentally the dependence has been found strongly nonlinear.²⁵

## VI. CONCLUSION

In sum, we have studied the single-band Hubbard model within the framework of self-consistent Hartree-Fock theory. We find that the system, for small doping, goes through paramagnetic, vertical (or horizontal) domain wall, diagonal domain wall, and small ferromagnetic polaron phases as the ratio $U/t$ is increased from zero toward $U/t\sim 15$. We have not been able to elucidate what happens for the large-correlation-energy limit, i.e., $U/t\gtrsim 20$, because of the many states that seem metastable and a considerable slowdown of the convergence of the iteration scheme. Nevertheless, there is clear evidence for the development of transverse spin components in this regime. We have, on the other hand, established that conventional finite-size studies of the doped Hubbard model based on square supercells are at best incomplete, and that we must think carefully in order not to impose unnecessary constraints. Since the basic physics behind our study also applies to the $t-J$ model,²⁶ similar care must be taken for numerical studies of this model as well.

Within the domain-wall and polaronic phases, we find that holes added to the half-filled system create empty states inside the Hubbard gap, whose splitting from the lower Hubbard band is roughly independent of $U$. The existence of such states may be related to the observed pre-edge peaks of x-ray absorption and the midinfrared peak(s) in optical experiments.

The Hartree-Fock approximation undoubtedly overstresses the importance of long-range magnetic order. Nevertheless, a HF mean-field solution is an appropriate starting point for more sophisticated calculations which incorporate correlation effects more accurately. The richness and complexity of even the mean-field ground states suggests that there is considerably more to be understood in the single-band Hubbard model.

## ACKNOWLEDGMENTS

We thank A. R. Bishop, S. L. Cooper, S. N. Coppersmith, W. M. C. Foulkes, M. S. Hybertson, E. B. Stechel, and J. Zaanen for useful discussions and suggestions. We are also grateful to E. B. Stechel for calling our attention to the photoabsorption data, and S. N. Coppersmith for a critical reading of the manuscript.

*Present address: Los Alamos National Laboratory, Los Alamos, NM 87545.
¹D. R. Penn, Phys. Rev. 142, 350 (1966); R. J. Jelitto, Phys. Status Solidi B 147, 391 (1988).
²H. J. Schulz, Europhys. Lett. 4, 609 (1987); Phys. Rev. Lett. 64, 1445 (1990).
³D. Poiblanc and T. M. Rice, Phys. Rev. B 39, 9749 (1989); H. J. Schulz, J. Phys. (Paris) 50, 2833 (1989); M. Kato et al., J.

Phys. Soc. Jpn. 59, 1047 (1990).

$^4$J. Zaanen and O. Gunnarsson, Phys. Rev. 40, 7391 (1989).

$^5$B. I. Shraiman and E. D. Siggia, Phys. Rev. Lett. 62, 1564 (1989); B. I. Shraiman and E. D. Siggia, Phys. Rev. B 40, 9162 (1989); D. M. Frenkel et al., ibid. 41, 350 (1990).

$^6$We use the designation SDW as a form of domain wall with a single harmonic at $q=2k_F$ dominating the structure.

$^7$H. Schulz, in Ref. 3.

$^8$A. R. Bishop et al. (unpublished).

$^9$W. P. Su, Phys. Rev. B 37, 9904 (1988); A. Singh and Z. Tesanović, ibid. 41, 614 (1990); see also Ref. 8.

$^{10}$The line for the diagonal wall has been obtained by scaling $\delta=\frac{1}{33}$ data by $\frac{33}{32}$. The calculation required an odd number of sites along the $x$ direction $[(33,0)\times(0,2)$ in this case] in order not to frustrate the spins when one domain wall (consisting of two holes) lies along the $y$ direction. Scaling $\delta=\frac{1}{16}$ data [two-domain walls in a $(32,0)\times(0,2)$ supercell] by $\frac{1}{2}$ gives virtually the same result for $U/t\gtrsim3$ owing to the weakness of the interaction between walls.

$^{11}$See Kato et al. in Ref. 3.

$^{12}$H. Yokoyama and H. Shiba, J. Phys. Soc. Jpn. 56, 3582 (1982).

$^{13}$T. Giamarchi and C. Lhuillier, Phys. Rev. B 42, 10 641 (1990).

$^{14}$S. N. Coppersmith and C. C. Yu, Phys. Rev. B 39, 11 464 (1989).

$^{15}$M. C. Gutzwiller, Phys. Rev. Lett. 10, 159 (1963); Phys. Rev. 134, A1726 (1965).

$^{16}$J. E. Hirsch, Phys. Rev. Lett. 51, 1900 (1983); Phys. Rev. B 31, 4403 (1985).

$^{17}$E. Dagotto, R. Joynt, A. Moreo, S. Bacci, and E. Gagliano, Phys. Rev. B 41, 9049 (1990); see also J. Riera and A. Young, ibid. 39, 9697 (1989); E. Dagotto, A. Moreo, R. Sugar, and D. Toussaint, ibid. 41, 811 (1990).

$^{18}$W. L. McMillan, Phys. Rev. B 12, 1187 (1975); 12, 1197 (1975); 14, 1496 (1976).

$^{19}$This type of behavior has much in common with spin-bag pic- ture of Schrieffer et al. See J. R. Schrieffer, X.-G. Wen, and S.-C. Zhang, Phys. Rev. Lett. 60, 944 (1988).

$^{20}$See, for instance, P. Kupier et al., Phys. Rev. B 38, 6483 (1988); M. L. den Boer et al., ibid. 38, 6588 (1988).

$^{21}$A. Krol et al. Phys. Rev. B. 42, 4763 (1990); C. T. Chen et al. (unpublished).

$^{22}$S. L. Cooper et al., Phys. Rev. B 40, 11 358 (1989); 41, 11 605 (1990); G. A. Thomas, D. H. Rapkine, S. L. Cooper, S.-W. Cheong, and A. S. Cooper, Phys. Rev. B (to be published).

$^{23}$A. Millis, H. Monier, and D. Pines, Phys. Rev. B 41, 167 (1990).

$^{24}$B. Ellman et al., Phys. Rev. B 39, 9012 (1989); S. M. Hayden et al., Phys. Rev. Lett. 66, 821 (1991).

$^{25}$See Ref. 22. Note, however, that the number of states in the gap and the optical absorption do not necessarily scale. In fact, the large effective mass at small doping could enhance the strength and give rise to the nonlinearity.

$^{26}$See, e.g., C. L. Kane, P. A. Lee, and N. Read, Phys. Rev. B 39, 6880 (1989); V. Elser, D. A. Huse, B. I. Shraiman, and E. D. Siggia, ibid. 6715 (1990); also see Ref. 5.