# Local environment and electron correlation effects on the magnetic properties of clusters

E. Muñoz-Sandoval¹, J. Dorantes-Dávila¹,², and G.M. Pastor²

¹ Instituto de Física, Universidad Autónoma de San Luis Potosí, Alvaro Obregón 64, 78000 San Luis Potosí, Mexico
² Laboratoire de Physique Quantiqueᵃ, Université Paul Sabatier, 118 route de Narbonne, 31062 Toulouse, France

Received: 8 January 1998 / Revised: 22 June 1998 / Accepted: 6 August 1998

**Abstract.** The electronic and magnetic properties of clusters are investigated in the framework of the Hubbard model by treating electron correlations effects in a saddle-point slave-boson approximation. The size dependent single-particle spectrum is calculated using a third moment real-space expansion of the local density of states. Results for the magnetic moments, magnetic order, average number of double occupations and hopping renormalizations are given as a function of the local coordination number z, for different representative values of the Coulomb interaction strength $U/t$ and band filling n. Several transitions between paramagnetic, ferromagnetic and antiferromagnetic behaviors are obtained as a function of z. The environment dependence of the magnetic behavior and of the degree of electron delocalization is analyzed. Advantages and limitations of the present approach are discussed.

PACS. 36.40.Cg Electronic and magnetic properties of clusters – 71.24.+q Electronic structure of clusters and nanoparticles – 75.10.Lp Band and itinerant models

## 1 Introduction

Clusters, nanoparticles and the macroscopic structures made out of them, constitute one the most active research fields in solid-state physics and materials science. One of the main characteristics of these systems is the presence of surfaces or interfaces which restrict the propagation of particles and elementary excitations thus reducing the accessible dimensions. Different physical situations are found between the atom on the one side (dimension zero) and the periodic solid on the other (dimension three). As representative examples let us mention free clusters, small particles, chains and quasi one-dimensional systems, overlayer structures on surfaces, thin films and granular materials. The differences in morphology and composition among these systems yield a diversity of specific behaviors which are not only important from a fundamental point of view but which may also lead to novel technological applications [1]. Consequently, investigations of the relation between local atomic environment and electronic properties are of considerable interest.

One of the most challenging problems in this context is magnetism, specially when it derives from itinerant electrons like the d-electrons in transition metals (TM’s). Indeed, a large number of experimental and theoretical works have shown that the magnetic behavior of itinerant electrons depends very strongly on the system size and on the local environment of the atoms. Consider, for instance, the enhancement of the local magnetic moments at Fe atoms as their local coordination number is reduced (e.g., in thin films, near surfaces and in small clusters [2–5]) or the onset of magnetism in small clusters of 4d TM’s which are non-magnetic in the solid (e.g., Rh_N [6]). In these cases, the magnetic behavior also depends sensitively on structure. Self-consistent tight-binding calculations on Fe clusters yield ferromagnetic order if the structure is bcc-like while for fcc-like clusters antiferromagnetic-like order is obtained [4]. Exact diagonalization studies of the Hubbard model have also revealed a similar strong structural dependence of the magnetic properties of both ground-state and low-lying excited-states [7]. From a microscopic point of view, these remarkable properties are the result of a delicate balance between the effect of hybridizations, which favor equal filling of spin states, and the effect of Coulomb interactions, which according to Hund’s rules favor the formation of local magnetic moments. Electron delocalization tends to reduce the ground-state kinetic energy $E_K$, but at the same time it also involves local charge fluctuations which increase the Coulomb-interaction energy $E_C$. The interplay between $E_K$ and $E_C$ introduces correlations in the electronic motion, which play a central role in determining the magnetic properties. Electron correlation effects are expected to become more important as the cluster size is reduced, since $E_K$ decreases with decreasing coordination number z and since the reduction of z should also hinder the backflow of density excitations responsible for dynamic screening of charge fluctuations.

ᵃ Unité mixte de recherche 5626 du CNRS

It is therefore important to understand how the electronic and magnetic properties depend on the system size and on the local atomic environment. One of the purposes of this paper is to study this problem from a local point of view in the framework of the Hubbard model.

An exact solution of the Hubbard Hamiltonian is not available except for some particular mostly periodic cases [8] and for finite systems containing a rather small number of sites [7]. Even if the exact solution for arbi- trary structures would be achievable, the enormous variety of behaviors that would result as a function of structure, size and system dimensions would be overwhelming (see for instance Ref. [7]). Therefore, it should be very difficult to extract simple qualitative trends as a function of a few relevant variables characterizing the size-dependent local atomic environment. A simplified treatment of electronic correlations and local environment seems both unavoid- able and physically interesting on its own. In this paper we present an approach which emphasizes the role of the immediate local environment of the atoms. The point of view is somehow complementary to that adopted in previ- ous studies on small clusters where cluster structure and electron correlations were treated exactly [7]. Rather than a detailed determination of the magnetic behavior of spe- cific structures, in the present work we aim to determine the effects of the changes in the local coordination number $z$ without incorporating structure specific contributions explicitly. In this way, a more simple and general physical picture is achieved by treating the size dependence of the single-particle spectrum and electron correlations from a local point of view. In addition, such local approaches are also interesting since they stress similarities between finite clusters and extended low-dimensional systems which are related to the reduction of $z$.

The reminder of the paper is organized as follows. Sec- tion 2 presents the theoretical approach, which is based on the application of slave-boson methods to the Hub- bard Hamiltonian and a real-space expansion of the local density of states. Results for the electronic and magnetic properties of clusters as a function of the local coordina- tion number $z$ are presented and discussed in Section 3 (e.g., magnetic-phase diagram, local magnetic moments, magnetic order, average number of double occupations). Finally, we conclude in Section 4 by pointing out limita- tions of the present approach as well as some perspectives of future extensions.

## 2 Theoretical approach

In order to determine the electronic and mag- netic properties of clusters, we consider the Hubbard Hamiltonian [9]

$$
H=-t \sum_{\langle i, j\rangle, \sigma} \hat{c}_{i \sigma}^{\dagger} \hat{c}_{j \sigma}+U \sum_{i} \hat{n}_{i \uparrow} \hat{n}_{i \downarrow}, \quad(1)
$$

where $\hat{c}_{i \sigma}^{\dagger}$, $(\hat{c}_{i \sigma})$ refers to the electron creation (annihila- tion) operator at site $i$ and spin $\sigma$, and $\hat{n}_{i \sigma}=\hat{c}_{i \sigma}^{\dagger} \hat{c}_{i \sigma}$ is the corresponding number operator. The hopping integral between nearest neighbor (NN) sites $i$ and $j$ is denoted by $t$ and the on-site Coulomb repulsion by $U$. The present single-band version of this model is certainly too over- simplified for describing accurately real systems in gen- eral. Successful applications to specific systems have been made in the case of low-energy properties of simple-metal clusters [10-12]. However, in spite of its simplicity, equa- tion (1) can be considered as a minimum model for corre- lated itinerant electrons, since it includes the fundamen- tal interplay between electron delocalization, described by the first term, and the Coulomb repulsion energy associ- ated to local charge fluctuations, described by the second term. It is our purpose, to use the Hubbard model in or- der to investigate the magnetic behavior and the degree of electron delocalization in clusters as a function of the size-dependent local environment.

The electronic correlations are taken into account us- ing the slave-bosons method proposed by Kotliar and Ruckenstein [13], which has been applied to a variety of periodic systems [14-23] and also to the van der Waals to metal transition in Hg clusters [24]. In this scheme, the representation of the many-body electronic states is changed by introducing a set of four additional boson op- erators at each site $i$, which keep trace of the state of occu- pation of the site. The boson operators $\hat{e}_{i}^{\dagger}$ ($\hat{e}_{i}$), $\hat{p}_{i \sigma}^{\dagger}$ ($\hat{p}_{i \sigma}$), and $\hat{d}_{i}^{\dagger}$ ($\hat{d}_{i}$) correspond to the creation (annihilation) of an empty, singly occupied with spin $\sigma$ or doubly occupied state. In this enlarged Hilbert space only the states which have consistent boson and fermion occupation numbers have a physical sense. Therefore, the conditions

$$
\hat{e}_{i}^{\dagger} \hat{e}_{i}+\sum_{\sigma} \hat{p}_{i \sigma}^{\dagger} \hat{p}_{i \sigma}+\hat{d}_{i}^{\dagger} \hat{d}_{i}=1, \quad(2)
$$

and

$$
\hat{p}_{i \sigma}^{\dagger} \hat{p}_{i \sigma}+\hat{d}_{i}^{\dagger} \hat{d}_{i}=\hat{n}_{i \sigma} \quad(3)
$$

have to be imposed. The form of any physical operator in the new representation (with fermions and bosons) is readily obtained once the transformation law for the ele- mentary fermion operators is defined: $\hat{c}_{i \sigma} \to \hat{c}_{i \sigma} \hat{z}_{i \sigma}$, where $\hat{z}_{i \sigma}$ is an operator acting only on the boson variables. An appropriate choice for $\hat{z}_{i \sigma}$ is [13,25]

$$
\begin{aligned}
\hat{z}_{i \sigma}= & \left(1-\hat{d}_{i}^{\dagger} \hat{d}_{i}-\hat{p}_{i \sigma}^{\dagger} \hat{p}_{i \sigma}\right)^{-1 / 2}\left(\hat{e}_{i}^{\dagger} \hat{p}_{i \sigma}+\hat{p}_{i \bar{\sigma}}^{\dagger} \hat{d}_{i}\right) \\
& \times\left(1-\hat{e}_{i}^{\dagger} \hat{e}_{i}-\hat{p}_{i \bar{\sigma}}^{\dagger} \hat{p}_{i \bar{\sigma}}\right)^{-1 / 2}.
\end{aligned}
$$

In the saddle point approximation, the electronic proper- ties are derived from an effective Hamiltonian

$$
\hat{H}^{\prime}=\sum_{i \sigma} \varepsilon_{i}^{\prime} \hat{n}_{i \sigma}+\sum_{i \neq j} t_{i j \sigma}^{\prime} \hat{c}_{i \sigma}^{\dagger} \hat{c}_{j \sigma}, \quad(5)
$$

which describes the electrons as if they were independent (quasi) particles having shifted energy levels $\varepsilon_{i \sigma}^{\prime}$ and renor- malized hopping integrals $t_{i j \sigma}^{\prime}=q_{i j}^{\sigma} t_{i j}$, as a consequence of Coulomb interactions and correlations. The hopping

renormalization factor $q_{i j}^{\sigma}=\left\langle\hat{z}_{i \sigma}^{\dagger} \hat{z}_{j \sigma}\right\rangle$ is given by

$$
q_{i j}^{\sigma}=\frac{\left(e_{i} p_{i \sigma}+p_{i \sigma} d_{i}\right)\left(e_{j} p_{j \sigma}+p_{j \sigma} d_{j}\right)}{\left[n_{i \sigma}\left(1-n_{i \sigma}\right) n_{j \sigma}\left(1-n_{j \sigma}\right)\right]^{\frac{1}{2}}}
\tag{6}
$$

where $e_{i}, p_{i \sigma}$ and $d_{i}$ refer to ground-state averages. Thus, the hopping integrals are replaced by $t_{i j \sigma}^{\prime}=q_{i j}^{\sigma} t_{i j}$ which takes into account the tendency to electron localization due to correlations. However, notice that in a real system, the hoppings between two sites depend on the actual many-body configuration of these sites (e.g., whether they are empty, singly occupied, etc.). These more subtle correlation effects are lost by the average over all configurations due to the saddle-point approximation.

The actual $T=0$ values of $e_{i}, p_{i \sigma}$ and $d_{i}$ are determined by minimizing the electronic energy

$$
E=\sum_{i \sigma} \int_{-\infty}^{\varepsilon_{F}}\left(\varepsilon-\varepsilon_{i \sigma}^{\prime}\right) \rho_{i \sigma}(\varepsilon) d \varepsilon+U \sum_{i} d_{i}^{2}
\tag{7}
$$

under the constraints (2) and (3). The first term in equation (7) represents the kinetic energy renormalized by correlations, i.e., resulting from hopping integrals $t_{i j \sigma}^{\prime}=q_{i j}^{\sigma} t_{i j} . \rho_{i \sigma}(\varepsilon)=-(1 / \pi) \operatorname{Im}\left\{G_{i \sigma, i \sigma}(\varepsilon)\right\}$ refers to the local density of states (LDOS) $[G(\varepsilon)=(\varepsilon-H')^{-1}]$ and $\varepsilon_{F}$ to the Fermi energy. The second term represents the Coulomb energy associated to local charge fluctuations, where $d_{i}^{2}$ is the average double occupation at site $i$. Equation (7) reflects the competition between the increase of local charge fluctuations when electrons delocalize and the localization of the electrons when charge fluctuations are suppressed.

The environment dependence of the electronic properties enters into the calculation through the LDOS $\rho_{i \sigma}(\varepsilon)$. Since the energy and magnetic moments result from integrals of $\rho_{i \sigma}(\varepsilon)$, one expects that in first approximation these properties should not depend sensitively on the details of the LDOS [26]. Still, situations are known where this is not the case and where a precise determination of the DOS is crucial, as it will be discussed at the end of Section 3. A systematic expansion of $\rho_{i \sigma}(\varepsilon)$ which allows to include the contributions to the LDOS from a local point of view is provided by the Haydock-Heine-Kelly recursion scheme [27]. In order to identify the leading contributions of the local environment on the electronic correlations and magnetic behavior we restrict the expansion up to the third moment. Higher-moment terms would start to depend on the details of the cluster structure beyond the first NN shell. In the case of bipartite structures, with sublattices denoted by $A$ and $B$, the third moment approximation to $\rho_{i \sigma}(\varepsilon)$ is given by

$$
\rho_{i \sigma}(\varepsilon)=\left(\frac{b_{i \sigma}}{\pi}\right) \frac{\sqrt{1-\left(\frac{\varepsilon-\sigma \Delta_{i} / 2}{2 b_{i \sigma}}\right)^{2}}}{\sigma \Delta_{i}\left(\varepsilon+\sigma \Delta_{i} / 2\right)+b_{i \sigma}^{2}},
\tag{8}
$$

where $b_{i \sigma}^{2}=\sum_{j}\left(q_{i j}^{\sigma} t_{i j}\right)^{2}=z\left(q^{\sigma} t\right)^{2}, \Delta_{i}=\varepsilon_{A \uparrow}-\varepsilon_{B \downarrow}=\Delta$ for $i \in A$ and $\Delta_{i}=\varepsilon_{B \uparrow}-\varepsilon_{A \downarrow}=-\Delta$ for $i \in B$. Equation (8) corresponds to a density of states centered at $\sigma \Delta_{i} / 2$ and having an effective band width $4 b_{i \sigma}$. For simplicity we assume that the number of atoms in each sublattice is the same $\left(N_{A}=N_{B}=N / 2\right)$ which implies that $z_{A}=z_{B}=z\left(N_{A} z_{A}=N_{B} z_{B}\right)$. This excludes the possibility of ferrimagnetic-like solutions resulting from different local band widths $\left(z_{A} \neq z_{B}\right)$ and non-compensated sublattice magnetizations [28]. The restriction to bipartite structures leaves triangular loops and the resulting magnetic frustration effects out of the scope of this work. The presence of triangular loops, as those often found in compact clusters structures, would yield an asymmetry in the single particle density of states even in paramagnetic or ferromagnetic cases (i.e., for $\Delta=0$ ). Their contribution, which is proportional to $t^{3}$ in the third moment expansion could be easily taken into account by including the number of triangular loops per site as an additional parameter characterizing the local environment.

The electronic energy $E$ is minimized by considering paramagnetic, ferromagnetic and anti-ferromagnetic solutions taking the number of electrons $n_{i}=p_{i \uparrow}^{2}+p_{i \downarrow}^{2}+2 d_{i}^{2}$, the local magnetic moment $\mu_{i}=p_{i \uparrow}^{2}-p_{i \downarrow}^{2}$ and the average double occupation $d_{i}^{2}$ as independent variables. More complex magnetic structures such as ferrimagnetic solutions or non-collinear spin arrangements have not been considered. First, for each set of values of $n_{i}, \mu_{i}$ and $d_{i}^{2}$, the self-consistent equations

$$
n_{i}=\left\langle\hat{n}_{i \uparrow}\right\rangle+\left\langle\hat{n}_{i \downarrow}\right\rangle,
\tag{9}
$$

$$
\mu_{i}=\left\langle\hat{n}_{i \uparrow}\right\rangle-\left\langle\hat{n}_{i \downarrow}\right\rangle
\tag{10}
$$

and

$$
\left\langle\hat{n}_{i \sigma}\right\rangle=\int_{-\infty}^{\varepsilon_{F}} \rho_{i \sigma}(\varepsilon) d \varepsilon
\tag{11}
$$

are solved in order to satisfy the constrains (2) and (3). The electronic energy is then computed from equation (7) and minimized with respect to $n_{i}, \mu_{i}$ and $d_{i}^{2}$. Phase boundaries are obtained by comparing the electronic energies.

## 3 Results and discussion

In this section we present and discuss results for several electronic and magnetic properties of clusters as a function of the local coordination number $z$. For periodic systems it is straightforward to relate the system dimension with $z$, once the lattice structure is given. For instance, $z=2$ corresponds to the one-dimensional chain, $z=4$ to the two-dimensional square lattice and $z=6$ to the three-dimensional simple cubic lattice. For finite clusters, the relation between $z$ and the number of atoms $N$ is in general more complicated, since $z$ changes as we move from the interior to the surface of the cluster and also for different surface atoms. In fact, one would have to consider at least two values of $z$ : one for bulk-like atoms $z_{b}$ and one for surface atoms $z_{s}$. Within this simplified picture the average coordination number $\bar{z}$ is given by

$$
\bar{z}=\left(z_{b} N_{b}+z_{s} N_{s}\right) / N \simeq z_{b}-4 N^{-1 / 3}\left(z_{b}-z_{s}\right).
\tag{12}
$$

![](./images/812461720751570945_1.jpg)

Fig. 1. Cluster-size dependence of the average coordination number $\bar{z}$ in simple cubic ($sc$) cubes, body centered cubic ($bcc$) rhombododecahedra and face centered cubic ($fcc$) cubooctahedra. The dots correspond to clusters having perfect compact surfaces of only one type, namely, the most compact one: (100)-like for $sc$, (110)-like for $bcc$ and (111)-like for $fcc$. The full curves show the large $N$ limit $\bar{z}=z_b - 4N^{-1/3}(z_b - z_s)$, where $N$ refers to the number of atoms and $z_b$ ($z_s$) to the bulk (surface) coordination number (see the appendix).

In more realistic situations the local coordinations of face, corner and edge atoms have to be distinguished. The average coordination number is then given by

$$
\bar{z}=(z_bN_b + z_fN_f + z_cN_c + z_eN_e)/N, \tag{13}
$$

where $b$, $f$, $c$, and $e$ refer to bulk, face, corner and edge atoms respectively ($N=N_b + N_f + N_c + N_e$). One may consider for example clusters with simple cubic ($sc$), body centered cubic ($bcc$) or face centered cubic ($fcc$) structures having only the most compact surfaces, i.e., (100)-like for $sc$, (110)-like for $bcc$ and (111)-like for $fcc$. The expressions for $z_i$ and $N_i$ for these cases are given in the appendix. The results for $\bar{z}$ shown in Figure 1 as a function of $N^{-1/3}$ illustrate how the local atomic environment changes as a function of the number of atoms, for representative cubic structures. One may also refer to this figure in order to infer qualitatively the size dependence of the electronic and magnetic properties, which in the following shall be presented as a function of the local coordination number $z$. Different values of $z$ correspond to different atoms within the cluster (bulk, face, corner, etc.) or to different cluster structures (examples are given in the appendix).

In Figure 2 results are given for the magnetic phase diagram of the Hubbard model as obtained using the theoretical approach described in the previous section. The ground-state magnetic order – for example, ferromagnetic (FM), antiferromagnetic (AF) or paramagnetic (PM) – is given as a function of $U/t$, $z$ and the number of electrons per site $n$. Since the Hubbard model has electron-hole symmetry for bipartite structures, we only show the results for $n\geq1$. Notice that $W=4t\sqrt{z}$ represents the band width of the unrenormalized single-particle LDOS. It is worth noting that, in spite of some quantitative differences, there are several common features between the present local approach and similar studies of the periodic square and Bethe lattices [13–17]. Different behaviors may be distinguished. For small values of $U/W$ ($0\leq U/W\leq0.5$) PM order dominates for all values of $n$. For $U/W>0.5$ and close to half-band filling ($1\leq n\leq1.05$) we find AF order. Starting from the strongly correlated limit and decreasing $U/W$ we observe that the AF region extends to larger values of $n$ (from $n=1.0$ for $U/W=\infty$ to up $n=1.25$ for $U/W=1.31$). A change of behavior is found for $U/W<1$, where AF order is displaced by the PM order. For $n>1.25$, the PM solution is always the most stable one irrespectively of the values of $U/W$ and $z$. Finally, for sufficiently large $U/W$ ($U/W>7$) we find FM order. The FM region is located between the AF and PM domains. Starting from a point where all 3 phases have the same energy ($n=1.12$, $U/W=7.15$) the range of electron densities where the ferromagnetism dominates increases monotonically with increasing $U$. In agreement with Nagaoka's theorem [30], the boundary between FM and AF regions includes the point $n=1$ and $U/W=\infty$. Notice that, in contrast to Hartree-Fock results, the FM solution is less stable than the PM one for $n>1.38$, even if the Coulomb interaction strength $U/W$ is arbitrary large. This illustrates the ability of saddle-point slave-boson approach to suppress local charge fluctuations, an important feature in order to determine the ground-state energy of low-spin states.

![](./images/812461720751570945_2.jpg)

Fig. 2. Magnetic-phase diagram of the Hubbard model on bipartite structures ($N_A=N_B=N/2$) as obtained by using the slave-boson mean-field approximation and the 3rd moment expansion of the local density of states. The ground-state magnetic order (ferromagnetic (FM), antiferromagnetic (AF) or paramagnetic (PM)) corresponding to a Coulomb repulsion $U$, a band width $W=4t\sqrt{z}$ and a number of electrons per site $n$ is indicated. For $n>1.38$ the solution is always PM.

From the phase diagram shown in Figure 2, we may infer the magnetic transitions which occur as a function

of $z$ for different values of $U/t$ and $n$. Taking into account that in clusters $1 \leq z \leq 12$ and that the single-particle band width is given by $W=4t\sqrt{z}$, one finds the following magnetic transitions as $z$ increases:

i) from FM to AF order for $28.6 \leq U/t \leq +\infty$ and $1 < n \leq 1.12$,

ii) from FM to PM order for $28.6 \leq U/t \leq +\infty$ and $1.12 \leq n \leq 1.38$,

iii) from AF to PM order for $2.13 \leq U/t \leq 8.24$ and $1 \leq n \leq 1.12$,

iv) from PM to AF order for $5.23 \leq U/t \leq 99.1$ and $1.12 \leq n \leq 1.25$,

v) a re-entrance of the type PM–AF–PM for $2.38 \leq U/t \leq 99.1$ and $1.12 \leq n \leq 1.25$ and

vi) a double transition of the type FM-PM-AF for $28.6 \leq U/t \leq 218.72$ and $1.12 \leq n \leq 1.25$.

In the following we discuss electronic and magnetic properties as a function of $z$, which are representative of most of the previous cases and which reveal the physical behavior within the different FM, AF and PM regimes.

One should keep in mind that in finite systems there are no true long-range phase transitions. Nevertheless and in spite of the fact that the wave function of each many-body eigenstate depends continuously on Hamiltonian parameters, level crossings may occur which often lead to discontinuous changes of the magnetic behavior as a function of $U/t$. The results of Ishii and Sugano for a rhombohedral 4-atom cluster [31] are a particularly illustrative example in the context of cluster magnetism and the Hubbard model. In this case one observes a discontinuity in the ground-state wave function, in the average of double occupations and in the spin correlations as a function of $U/t$, which has been interpreted as a transition from PM to AF like behavior at $U/t=2.8$ (half band filling). The NN spin correlation functions allow to discern between AF-like and non-correlated PM-like ground states even if the total spin $S$ is in both cases minimal ($S=0$). The saddle-point approximation mimics the onset of AF NN correlations by the formation of local magnetic moments with AF order. It is in this sense that broken-symmetry spin-density-wave states are to be interpreted in finite systems.

![](./images/812461720751570945_3.jpg)

Fig. 3. Electronic and magnetic ground-state properties of the Hubbard model on bipartite structures ($N_A=N_B=N/2$) as obtained by using the slave-boson mean-field approximation and the 3rd moment expansion of the local density of states. Results are given for half-band filling ($n=1$) as a function of the local coordination number $z$: (a) $U/t$-$z$ magnetic-phase diagram, (b) average local magnetic moment $\mu$, (c) average double occupation $d^2$ and (d) hopping renormalization factor $q^\sigma$ ($q^\uparrow=q^\downarrow$ for PM and AF order). In (b), (c) and (d) different values of the Coulomb repulsion $U/t$ are considered: $U/t=5$ (dashed curves), $U/t=7$ (full curves) and $U/t=10$ (dashed-dotted curves).

In the Figures 3 and 4 results are given for (a) the $U/t$-$z$ magnetic phase diagram, (b) the local magnetic moments $\mu$, (c) the average number of double occupations $d^2$ and (d) the hopping renormalization factor $q^\sigma=t'/t$. In the half-filled-band case we may observe that the critical coordination number $z_c$ at which the AF-PM transition occurs depends very strongly on $U/t$. $z$ varies from $z_c=1$, for $U/t=2.13$, to $z_c=12$, for $U/t=7.4$. This implies that the onset of antiferromagnetism, which occurs as $z$ decreases, depends strongly on the considered element and on the inter-atomic distance $R$ (e.g., $t \sim R^{-5}$ in TM’s). For larger values of $U/t$, AF order always dominates as also found in exact diagonalization studies on small clusters [31]. Notice in Figure 3b the onset and increase of the magnetic moments as the cluster size decreases. The enhancement of $\mu$ is qualitatively in agreement with realistic $spd$-band Hartree-Fock calculations on Cr clusters and surfaces [4,32]. Figures 3c and 3d illustrate the interplay between electron delocalization and Coulomb-energy fluctuations. As $z$ decreases the gain in kinetic energy associated to band formation decreases. The electrons tend to be more localized and therefore the average number of double occupations $d^2$ decreases (see Fig. 3c). A remarkable change of behavior is found at the PM to AF transition ($z_c=5.5$ for $U/t=5$ and $z_c=10.7$ for $U/t=7$). Starting from $z=12$ in the PM state and decreasing $z$, we first observe that the kinetic energy is strongly renormalized in order to suppress charge fluctuations ($q=t'/t$ decreases strongly). However, in spite of this important reduction of $q$, the double occupations are not very efficiently reduced since $d^2$ decreases rather slowly (compare

![](./images/812461720751570945_4.jpg)

Fig. 4. Electronic and magnetic ground-state properties of the Hubbard model on bipartite structures ($N_A = N_B = N/2$). Results are given as in Figure 3 for a band-filling $n = 1.2$ and for $U/t = 7$ (full curves), $U/t = 35$ (dashed curves) and $U/t = 90$ (dashed-dotted curves). Notice that in the FM case $q^\uparrow < q^\downarrow$ (e.g., for $U/t = 90$ and $z < 3.8$).

Figs. 3c and 3d for $z > z_c$). Consequently, when $q$ reaches a critical value ($q \simeq 0.90$) it is more efficient to develop local magnetic moments and to reduce $d^2$ by separating the up and down electron-densities in space (i.e., AF order). A rapid increase of $\mu$ follows together with a rapid decrease of $d^2$ (Figs. 3b and 3c). Now, the kinetic energy does not need to be further renormalized since the reduction of $d^2$ is taken over by the formation of local moments in a similar way as in the Hartree-Fock approximation. In fact $q$ increases together with $\mu$ as $z$ decreases. The AF behavior contrasts with the PM one. Following the PM solution for $z < z_c$, one observes that $q$ continues to decrease and even-tually vanishes at given value of $z$ ($q_{PM} = 0$ for $z \leq 0.54$ and $U/t = 5$; $q_{PM} = 0$ for $z \leq 1.06$ and $U/t = 7$). At this point also $d^2$ and the electronic energy vanish. While the localization is never complete in the AF case ($d^2 > 0$), the reduction of $d^2$ can be very important when the system dimensions are very small (e.g., $d^2 =0.01$–$0.04$ for $z \simeq 1$–$2$ and $U/t =5$–$10$). This is qualitatively in agreement with exact diagonalization results [7]. Finally, notice that in the purely AF regime, for example for $U/t = 10$, $\mu$, $d^2$ and $q$ depend weakly on $z$.

In Figure 4 results are given for $n = 1.2$. For $U/t = 7$ we observe a transition from PM to AF order as $z$ decreases, which is qualitatively similar to the one previously discussed for $n = 1$ (Fig. 3). Notice, however, the reduction of $z_c$ and of the magnetic moment $\mu$ as we go from $n = 1$ to $n = 1.2$, e.g., $z_c(n = 1,U/t = 7) = 10.7$ and $\mu(n = 1,z = 1) = 0.96$ while $z_c(n = 1.2,U/t = 7) = 5.3$ and $\mu(n = 1.2,z = 1) = 0.56$. This reflects the decreasing stability of the AF solution as we move away from half-band filling. Nevertheless, as in the $n = 1$ case, the magnetic moments $\mu$ are enhanced as the cluster size decreases. In contrast the hopping renormalization factor $q$ now decreases slowly with decreasing $z$ (compare Figs. 4b and 4c with Figs. 3b and 3c). As the coordination number is reduced, the average double occupations $d^2$ are suppressed more rapidly in AF state than in the PM state. This agrees with the results for $n = 1$ although the difference between the slops $\partial d^2/\partial z$ in the AF and PM solutions is much less important in the present case. In other words, the suppression of double occupations becomes less efficient in the AF state as $n$ moves away from half-band filling.

For larger values of $U/t$ a qualitatively different behavior is found as a function of $z$. For example, for $U/t = 35$ we obtain AF order in the bulk ($z = 12$) with unsaturated magnetic moments $\mu = 0.5$ and a considerably renormalized kinetic energy ($q \simeq 0.56$). Remarkably, $\mu$ now decreases with decreasing $z$. This is a consequence of the increasing stability of the PM state and the resulting PM-AF transition which occurs at $z \simeq 8.4$. At these values of $U/t$ the double occupations are reduced almost to the minimum possible value $d_{min}^2 = n - 1$ already for $z = 12$ ($n \geq 1$). Therefore, reducing the cluster size has little influence on $d^2$, which decreases only very weakly as $z$ decreases (see Fig. 4c). At even larger values of $U/t$ we observe PM to FM transitions. The critical coordination number $z_c$, below which FM sets in, increases with increasing $U/t$. The same holds for the magnetic moments $\mu$ in qualitatively agreement with Hartree-Fock $d$-band model calculations [4]. In Figure 4 results are shown for $U/t = 90$. Notice the rapid increase of $\mu$ for $z < z_c$, which approaches its saturation value $\mu_{sat} = 2 - n$ for $z \to 1$. In contrast, $d^2$ is unaffected by the transition since already for $z > z_c$ (in the PM regime) $d^2$ is very close to the minimum value $d_{min}^2 = n - 1$. The hopping renormalization factors $q^\sigma$ also show a remarkable dependence as a function of $z$. In the PM solution $q^\sigma$ is nearly independent of $z$ and it is of course the same for both spins. As the magnetic moment develops ($z < z_c$) the majority and minority spins renormalization factors $q^\uparrow$ and $q^\downarrow$, split. $q^\downarrow$ increases with $\mu$ and eventually tends to 1 when $\mu \to 2 - n$. The minority electrons give the dominant contribution to the kinetic energy $E_K$. In contrast, $q^\uparrow$ decreases as $\mu$ increases and the majority-electron contribution to $E_K$ becomes less and less important as the up band tends to be completely filled ($n_\uparrow \to 1$ as $z \to 1$ for $n > 1$).

It is also interesting to compare our local-approach with previous calculations on periodic infinite systems in which rectangular, elliptical or Bethe-lattice single- particle densities of states were used [13–17]. As already pointed out, the topology of our phase diagram for a fixed $z$ (e.g., $z=4$) is similar to that reported in references [13–17] in the most relevant large $U/t$ regime. However, some quantitative differences in the position of the phase boundaries are present. In particular the behavior for $U \to 0$ and $n=1$ deserves a more detailed analysis. While our calculations yield a transition from PM to AF order at a finite value of $U/t$, in references [13–17] AF sets in already for arbitrary small $U/t>0$. In order to under- stand this discrepancy, notice that in the present local approach one cannot distinguish between a true bipartite structure and a structure which is bipartite only locally around site $i$. As a consequence no gap opens at $\varepsilon_{F}=0$ in the third moment $\rho_{i \sigma}(\varepsilon)$ for arbitrary small $\Delta>0$. In contrast, references [13–17] considered infinite bipartite structures (square and Bethe lattices) for which perfect nesting ensures the existence of a finite gap at $\varepsilon_{F}=0$ for any $\Delta$ ($E_k=\sqrt{\varepsilon_k^2+\Delta^2}$) thus stabilizing the AF so- lution at arbitrary small $U/t$ [33]. To further investigate this problem we have also performed calculations on fi- nite rings with $L$ sites using the saddle-point slave-boson approximation and calculating the DOS exactly (no 3rd moment approximation). For half-band filling one obtains AF order for all $U>0$ if $L=4m$ with $m$ integer, since the highest occupied molecular orbital (HOMO) and the low- est unoccupied molecular orbital (LUMO) are degenerate ($\varepsilon_{HOMO}=\varepsilon_{LUMO}=0$). In contrast, AF sets in only at a finite $U$ if $L=2(2m+1)$ since $\varepsilon_{LUMO}-\varepsilon_{HOMO}>0$ ($U_c/t=2.3$, 1.9 and 1.3 for $L=18$, 30 and 110 respec- tively [34]). These results show that in finite bipartite clus- ters both behaviors are possible.

## 4 Summary

The magnetic and electronic properties of clusters have been investigated in the framework of the Hubbard model. The interplay between correlations, delocalization and magnetism was taken into account within a saddle-point slave-boson approach. The environment dependence of the single-particle electronic structure was calculated by us- ing a simple third moment real-space expansion of the lo- cal density of states, which allows to relate the electronic properties to the local coordination number $z$. Within this scheme a variety of magnetic transitions have been ob- tained as a function of $z$, the Coulomb interaction strength $U/t$ and the band filling $n$. The resulting changes in prop- erties such as the magnetic moment, the average number of double occupations and the renormalization of the ki- netic energy have been analyzed in some detail, in particu- lar concerning the effects of the reduction of coordination and system size on the electronic correlations.

The present work incorporates electron correlation ef- fects and charge fluctuations beyond most previous mean- field studies on clusters. However, the approximations used for calculating the single-particle DOS have pre- cluded us from addressing some important aspects of the problem of electronic correlations and magnetism in clus- ters. For example, non-bipartite structures and the associ- ated magnetic frustration effects are of considerable inter- est and would deserve to be studied in detail. Moreover, it is well known that the magnetic properties of itinerant electrons often depend on details of the geometry of the cluster. Therefore, for a quantitative description of specific systems, a precise account of the local atomic environ- ment (e.g., by expanding the local Green's functions well beyond the 3rd moment approximation) would be neces- sary. This would of course require a complete knowledge of the system structure and would deprive the calcula- tions from the general character adopted in this paper. In any case, in view of the impossibility of performing exact calculations on large clusters or extended low-dimensional systems, the coordination number dependence of magnetic moments and magnetic order reported in this work should provide useful information on the qualitative trends to be expected.

This work was financed in part by CONACyT (Mexico) and CNRS (France).

## Appendix

Let $\nu$ denote the number of shells surrounding a central atom. The number of cluster atoms $N(\nu)$ for the $sc$-, $bcc$- and $fcc$-like structures are then given by

$$
N_{sc}=8\nu^3+12\nu^2+6\nu+1,\tag{A.1}
$$

$$
N_{bcc}=4\nu^3+6\nu^2+4\nu+1\tag{A.2}
$$

and

$$
N_{fcc}=\frac{16}{3}\nu^3+8\nu^2+\frac{14}{3}\nu+1.\tag{A.3}
$$

The expressions for the number of bulk, face, edge and corner atoms, $N_b$, $N_f$, $N_e$ and $N_c$, and for the correspond- ing local coordination numbers, $z_b$, $z_f$, $z_e$ and $z_c$ are the following: For simple cubic cubes

$$
\begin{aligned}
N_b&=8\nu^3-12\nu^2+6\nu-1,& z_b&=6,\\
N_f&=24\nu^2-24\nu+6,& z_f&=5,\\
N_e&=24\nu-12,& z_e&=4,\\
N_c&=8,& z_c&=3;
\end{aligned}\tag{A.4}
$$

for $bcc$ rhombododecahedra

$$
\begin{aligned}
N_b&=4\nu^3-6\nu^2+4\nu-1,& z_b&=8,\\
N_f&=12\nu^2-24\nu+12,& z_f&=6,\\
N_e&=24\nu-24,& z_e&=5,\\
N_c&=14,& z_c&=4;
\end{aligned}\tag{A.5}
$$
```

and for fcc cubooctahedra

$$
\begin{aligned}
N_{b} & =\frac{16}{3} \nu^{3}-8 \nu^{2}+\frac{14}{3} \nu-1, & z_{b} & =12, \\
N_{f} & =16 \nu^{2}-24 \nu+12, & z_{f} & =9, \\
N_{e} & =24 \nu-12, & z_{e} & =7, \\
N_{c} & =6, & z_{c} & =4.
\end{aligned} \tag{A.6}
$$

The results shown in Figure 1 are derived by combining equation (13) and equations (A.1-A.6).

## References

1. See, for instance, Phys. Today **48**, 24 (1995).

2. L.M. Falicov, G. Somorjai, Proc. Natl. Acad. Sci. USA **82**, 2207 (1985).

3. D.R. Salahub, R.P. Messmer, Surf. Sci. **106**, 415 (1981); K. Lee, J. Callaway, S. Dhar, Phys. Rev. B **30**, 1724 (1985); K. Lee, J. Callaway, K. Wong, R. Tang, A. Ziegler, *ibid.* **31**, 1796 (1985).

4. G.M. Pastor, J. Dorantes-Dávila, K.H. Bennemann, Phys- ica B **149**, 22 (1988); Phys. Rev. B **40**, 7642 (1989); J. Dorantes-Dávila, H. Dreyssé, G.M. Pastor, Phys. Rev. B **46**, 10432 (1992).

5. I.M.L. Billas, J.A. Becker, A. Châtelain, W.A. de Heer, Phys. Rev. Lett. **71**, 4067 (1993); I.M.L. Billas, A. Châtelain, W.A. de Heer, Science **265**, 1662 (1994); J.P. Bucher, D.C. Douglas, L.A. Bloomfield, Phys. Rev. Lett. **66**, 3052 (1991); Phys. Rev. B **45**, 6341 (1992); D.C. Douglass, A.J. Cox, J.P. Bucher, L.A. Bloomfield, Phys. Rev. B **47**, 12874 (1993); S.E. Apsel, J.W. Emert, J. Deng, L.A. Bloomfield, Phys. Rev. Lett. **76**, 1441 (1996).

6. A.J. Cox, J.G. Louderback, L.A. Bloomfield, Phys. Rev. Lett. **71**, 923 (1993); A.J. Cox, J.G. Louderback, S.E. Apsel, L.A. Bloomfield, Phys. Rev. B **49**, 12295 (1994).

7. G.M. Pastor, R. Hirsch, B. Mühlschlegel, Phys. Rev. Lett. **72**, 3879 (1994); Phys. Rev. B **53**, 10382 (1996).

8. For reviews of exact results on the Hubbard model see E.H. Lieb, *Proceedings of 1993 conference in honor of G.F. Dell'Antonio*, Advances in Dynamical Systems and Quan- tum Physics (World Scientific, 1995), pp. 173-193; *Pro- ceedings of 1993 NATO ASW, The Physics and Mathe- matical Physics of the Hubbard Model* (Plenum, in press); *Proceedings of the XIth International Congress of Mathe- matical Physics*, Paris, 1994, edited by D. Iagolnitzer (In- ternational Press, 1995), pp. 392-412.

9. J. Hubbard, Proc. Roy. Soc. Lond. A **276** 238 (1963); *ibid.* A **281**, 401 (1964); J. Kanamori, Prog. Theo. Phys. **30**, 275 (1963); M.C. Gutzwiller, Phys. Rev. Lett. **10**, 159 (1963).

10. Y. Wang, T.F. George, D.M. Lindsay, A.C. Beri, J. Chem. Phys. **86**, 3493 (1987).

11. F. Spiegelmann, P. Blaise, J.P. Malrieu, D. Maynau, Z. Phys. D **12**, 341 (1989); Phys. Rev. B **41**, 5566 (1990).

12. J. Friedel, J. Phys. France **51**, 2023 (1990).

13. G. Kotliar, A.E. Ruckenstein, Phys. Rev. Lett. **57**, 1362 (1986).

14. S.M.M. Evans, Europhys. Lett. **20**, 53 (1992).

15. P. Denteneer, M. Blaauboer, J. Phys.-Cond. **7**, 151 (1995).

16. M. Deeg, H. Fehske, H. Bütner, Z. Phys. B **91**, 31 (1993).

17. W. Zhang, M. Avignon, K.H. Bennemann, Phys. Rev. B **45**, 12478 (1992).

18. R. Frésard, K. Doll, in *The Hubbard Model: Its Physics and Mathematical Physics*, edited by D. Baeriswyl, D.K. Campbell, J.M.P. Carmelo, F. Guinea, E. Louis (Plenum Press, 1995), p. 385.

19. S.E. Barnes, J. Phys. F **6**, 1375 (1976); *ibid.* **7**, 2637 (1977).

20. P. Coleman, Phys. Rev. B **29**, 3035 (1984).

21. N. Read, D. Newns, J. Phys. C **16**, 3273 (1983); N. Read, J. Phys. C **18**, 2651 (1985).

22. L. Lilly, A. Muramatsu, W. Hanke, Phys. Rev. Lett. **65**, 1379 (1990); *ibid.* **70**, 2049 (1993); B. Mehlig, *ibid.* **70**, 2048 (1993).

23. W. Ziegler, P. Dieterich, A. Muramatsu, W. Hanke, Phys. Rev. B **53**, 1231 (1996) and references therein.

24. M.E. Garcia, G.M. Pastor, K.H. Bennemann, Phys. Rev. Lett. **67**, 1142 (1991).

25. The square root pre- and post-factors yield 1 over any physical state (see Eqs. (2, 3)). They are introduced in order to ensure the proper $U \to 0$ limit in the saddle-point approximation (see Ref. [13]).

26. G.M. Pastor, J. Dorantes-Dávila, K.H. Bennemann, Chem. Phys. Lett. **148**, 459 (1988) and references therein.

27. R. Haydock, in *Solid State Physics*, edited by H. Ehrenreich, F. Seitz, D. Turnbull (Academic, New York, 1980), Vol. 35, p. 215.

28. For half-band filling and $U/t > 0$ Lieb demonstrated that $S=(N_A - N_B)/2$ ($N_A + N_B$ even) [29]. The theorem was also checked to hold for $N = N_A + N_B$ odd on arbitrary graphs having $N \leq 7$ sites R. Hirsch, G.M. Pastor (private communication); R. Hirsch, Ph.D. thesis, Universtät zu Köln (1993).

29. E.H. Lieb, Phys. Rev. Lett. **62**, 1201 (1989).

30. Y. Nagaoka, Solid State Comunn. **3**, 409 (1965); D.J. Thouless, Proc. Phys. Soc. Lond. **86**, 893 (1965); Y. Nagaoka, Phys. Rev. **147**, 392 (1996); H. Tasaki, Phys. Rev. **40**, 9192 (1989).

31. Y. Ishii, S. Sugano, J. Phys. Soc. Jpn **53**, 3895 (1984).

32. A. Vega, J. Dorantes-Dávila, G.M. Pastor, L.C. Balbás, Z. Phys. D **19**, 263 (1991); R.H. Victora, L.M. Falicov, S. Ishida, Phys. Rev. B **30**, 3896 (1989).

33. Notice that for the honeycomb lattice, the transition from PM to AF order occurs at a finite $U/t$ since there is a gap at $\varepsilon_F = 0$ already for $\Delta = 0$ [18].

34. M.A. Ojeda-López, E. Muñoz-Sandoval (private communi- cation).