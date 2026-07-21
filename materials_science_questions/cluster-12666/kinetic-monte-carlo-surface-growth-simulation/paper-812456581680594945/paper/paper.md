# Modeling of Random Formation of Microporous Material Following Thermodynamic Limitations

Freddy Romm

Chemical Engineering Department, Technion-IIT, Haifa 32000 Israel

E-mail: cercafr@techunix.technion.ac.il

Received May 11, 1998; accepted November 30, 1998

The problem of pore formation in limited (small) volume has been considered. General equations describing the system in the continuous (many particles) and discrete (few particles) cases have been obtained. It has been shown that pore formation is not limited by nucleus genesis because of entropic reasons. Kinetic limitation leads to the auto-acceleration-like form of the dependence of the number of empty cells and the internal area functions. The percolation problem has been solved for 2- and 3-dimensional cases with comparison of systems obtained by traditional Monte Carlo and thermodynamic factors. The 3-dimensional situation leads to reduction of the percolation threshold. However, the difference in the values of percolation thresholds estimated by the ordinary Monte Carlo simulation and with thermodynamic limitation is not significant (less than the eventual error). The change of tortuosity was estimated. At the percolation threshold, the tortuosity decreases rapidly, then very slowly with an increase in microporosity, and only at very high microporosity (close to 1) the decrease in tortuosity is again sharp. The influence of the thermodynamic limitation on the regularity of the micropore cluster has been analyzed based on the consideration of behavior of free energy and surface area of the cluster. It has been found that both of these structural parameters significantly decrease if the thermodynamic limitation is imposed.
© 1999 Academic Press

**Key Words**: formation of microporous material; random formation of microporous structure; Monte Carlo simulations; thermodynamic modeling of micropore formation; percolation; tortuosity.

The problem of modeling processes of formation of microporous material attracts considerable attention of theoretical researchers in the physical chemistry of solids. There are two principal approaches in this area: Monte Carlo simulation (1–3) and thermodynamic description (4–6).

The Monte Carlo simulation considers the process of microporous cluster formation in solid as a random process in which every cell of the solid structure may become empty with high probability which does not depend on the pre-history of the process. The main drawback of such an approach is the ignorance of the thermodynamic determination of the process; therefore, this approximation is applicable mostly to structures with low microporosity where micropores “do not feel” one other.

In contrast, thermodynamic description considers only the thermodynamic aspect of the process, while the real microporous structure does not always allow application of statistical thermodynamics to microporous cluster formation.

Since many of microporous materials, especially catalysts, are prepared by high-temperature treatment of organic or gelled materials, the problem of the adequate description of such process attracts particular interest. The previous model of microporous material preparation by pyrolysis was based on the thermodynamic consideration of micropores as subsystems in the gas–solid system. The main equations of this model used the negentropy change in micropore formation processes (5, 6). This model has two principal disadvantages: (1) the discreteness of the system was neglected, and the error of this approximation was not estimated; (2) the obtained equations are not appropriate for the characterization of random-fractal properties of micropore system.

Now, we are interested in evaluation of discrete properties of the considered system and the error of the continuance approximation.

The focus of this paper is the combination of Monte Carlo simulation with the thermodynamic approach, which allows obtainment of upper correctness in the description of the process of formation of microporous structure, especially in species of solid. We take into account that distributions determined by thermodynamics (4–6) cannot realize exactly, but they limit the random process of formation of the micropore cluster and change its structure and related characteristics.

We consider a microporous system as a net containing $N_0$ cells, $N_p$ of which are empty spots corresponding to pores or dislocations. Each cell has $n$-neighbors, $m$ of which are empty ($m$ changes from 0 to $n$) and ($n-m$) are occupied. The surface

energy is approximately proportional to the internal surface area $A_{\mathrm{p}}$,

$$G \approx \sigma A_{\mathrm{p}} \tag{1}$$

$$A_{\mathrm{p}} = \sum_{m=0}^{n} m N_{\mathrm{f}m} \tag{2}$$

$$N_{\mathrm{f}\Sigma} = N_{0} - N_{\mathrm{p}} = \sum_{m=0}^{n} N_{\mathrm{f}m}, \tag{3}$$

where $N_{\mathrm{f}m} \equiv N_{\mathrm{f}}(m)$ is the number of nonempty cells having $m$-empty neighbors. The situation $m = n$ corresponds to the cell having the minimal mechanical bond to its neighbors.

The maximum entropy corresponds to the Gibbs distribution of micropores in energy (5, 6), analogous to Poisson distribution of nonempty cells having empty neighbors,

$$\xi(m) = p_{\mathrm{p}}^{m}(1 - p_{\mathrm{p}}^{n-m})(1 - p_{\mathrm{p}})/(1 - p_{\mathrm{p}}^{\mathrm{n}+1}), \tag{4}$$

where $p_{\mathrm{p}} = N_{\mathrm{p}}/N_{0}$. If the real distribution in the interface field is $\xi^{*}(m) = N_{\mathrm{f}m}/(N_{0} - N_{\mathrm{p}})$, the related free energy of surface is

$$\Delta G_{\Lambda} = R_{\mathrm{g}}T \sum_{m=0}^{n} \left[\xi^{*}(m)\ln \xi^{*}(m) - \xi(m)\ln \xi(m)\right], \tag{5}$$

where $T$ is the temperature, and $R_{\mathrm{g}} = 8.314\ \mathrm{J/(mol \times K)}$ is the gas constant. The total free energy of the system is

$$
\begin{aligned}
\Delta G_{\Sigma} = \sigma \sum_{m=0}^{n} m(N_{0} - N_{\mathrm{p}})\xi^{*}(m) &+ R_{\mathrm{g}}T(N_{0} - N_{\mathrm{p}}) \sum_{m=0}^{n} \\
&\times \left[\xi^{*}(m)\ln \xi^{*}(m) - \xi(m)\ln \xi(m)\right]. \tag{6}
\end{aligned}
$$

If $\sigma = 0$, obviously, $\Delta G_{\Sigma} = \min = 0$ at $\xi^{*} = \xi$.

The most appropriate in the thermodynamic point of view state of the quasi-equilibrium system is described by the minimum of free energy and variations of specified parameters that is written in the continuous case as follows (6):

$$\delta \Delta G_{\Sigma} = 0,\quad \delta A_{\mathrm{p}} = 0,\quad \sum_{m=0}^{n} \delta \xi_{m}^{*} = 0, \tag{7}$$

hence,

$$\sum_{m=0}^{n} \left[\sigma m \delta \xi^{*}(m) - R_{\mathrm{g}}T(\ln \xi^{*}(m)\delta \xi^{*}(m) + \delta \xi^{*}(m))\right] = 0 \tag{8}$$

$$\sum_{m=0}^{n} \delta \xi^{*}(m) = 0,\quad \sum_{m=0}^{n} m \delta \xi^{*}(m) = 0. \tag{9}$$

From Eqs. [8] and [9] we obtain

$$\xi^{*}(m) = \alpha_{2}\mathrm{EXP}\left[ - \frac{(\sigma - \alpha_{1})}{R_{\mathrm{g}}T} m \right], \tag{10}$$

where

$$\alpha_{1} = R_{\mathrm{g}}T \ln\left[p_{\mathrm{p}}/(1 - p_{\mathrm{p}})\right],$$

$$\alpha_{2} = \frac{1 - \mathrm{EXP}\left( \frac{\alpha_{1} - \sigma}{R_{\mathrm{g}}T} \right)}{1 - \mathrm{EXP}\left( (n + 1)\frac{\alpha_{1} - \sigma}{R_{\mathrm{g}}T} \right)}.$$

Equation [10] is analogous to that obtained in (5) for steady-state preparation of microporous material of limited (small) size. However, the equations above are valid only if the variation is enough short but wrong in the case of microscopic system in which the number of empty cells (belonging to micropore cluster) changes discretely and the discreteness is not negligible. Distribution [10] is thermodynamically optimal but not available at $N_{\mathrm{p}} \ll N_{0}$ because of the discreteness of the change of $N_{\mathrm{p}}$ and, respectively, $\xi$. The real free energy $G'$ differs from that in Eq. [5], and this difference is the driving force for the further evolution of the system. Each act of release of empty space may take place at every occupied cell, but the related change of the free energy is different and determined by the formation of a new surface and the combinatorial entropy change. The probability that the micropore formation realizes at a cell having $m_{0}$ empty neighbors is proportional to the weight parameter of this event (thermodynamic weight),

$$P(m_{0}) \sim N_{\mathrm{f}}(m_{0})\mathrm{EXP}\left( - \frac{\Delta G_{\Sigma,\nu}^{0}}{R_{\mathrm{g}}T} \right), \tag{11}$$

where $\Delta G_{\Sigma,\nu}^{0}$ is the related virtual change of the free energy, and $R_{\mathrm{g}}$ is the gas constant. Equation [11] means that the probability that an occupied cell with $m_{0}$ neighbors is released is proportional to $P(m_{0})$.

Formation of dislocations. Let us consider an occupied cell which transforms to an empty cell. It has $m_0$ empty neighbors and $m^-=(n-m_0)$ occupied. We assume that the probability that each neighbor has $m'$ empty neighbors ($m'\leq n-1$) is proportional to $N_{\mathrm{f}}(m')$ and does not depend on the previous history of the micropore formation. In such case, the act of dislocation formation leads to reduction of $N_{\mathrm{f}}(m_0)$ by one $(N_{\mathrm{f}}(m_0)\to N_{\mathrm{f}}(m_0)-1)$, and $N_{f}(m_0+1)$ rises by one $(N_{f}(m_0+1)\to N_{f}(m_0+1)+1)$, while for all $N_{\mathrm{f}}(m)$ the change is

$$
\begin{aligned}
& \Delta N_{m}^{0}(m) \\
& = \begin{cases}m^{-}\left(\left(N_{\mathrm{f}(m-1)}+\delta_{2}\right)-\left(N_{\mathrm{f} m}+\delta_{1}\right)\right) /\left(N_{\mathrm{f} \Sigma}-1\right) & \text { if } m \geq 1 \\
-m^{-}\left(N_{\mathrm{f} m}+\delta_{1}\right) /\left(N_{\mathrm{f} \Sigma}-1\right) & \text { if } m=0\end{cases}
\end{aligned}
\tag{12}
$$

$$
\delta_{1}=\left\{\begin{array}{ll}
0, & \text { if } m \neq m_{0} ; \\
-1, & \text { if } m=m_{0}
\end{array} ; \delta_{2}=\left\{\begin{array}{ll}
0, & \text { if } m \neq 1+m_{0} \\
-1, & \text { if } m=1+m_{0}
\end{array}\right.\right.
\tag{13}
$$

$$
\sum_{m=0}^{n} \Delta N_{\mathrm{f}}^{0}(m)=-1
\tag{14}
$$

If we neglect the discontinuation of $N_{\mathrm{f}}$, Eq. [9] stays always valid, while parameters $\alpha_{1}$ and $\alpha_{2}$ monotonically change with increase of $p_{\mathrm{p}}$.

Nucleus formation. Since many of interface processes are limited by nucleus genesis, before we deal with the kinetics of pyrolysis in limited size we need be sure that the considered system is not the case. Indeed, if we apply Eq. [6] to a real system containing about $10^{20}$ particles, we easily see that even a single entropic factor is enough to assure one empty cell (dislocation) formation. That is in agreement with known facts from the dislocation theory (7). Hence, pore formation has no limitation in nucleus genesis.

Kinetic limitation. To analyze the kinetic aspect of the problem, we may apply Eqs. [1]-[14] to theory of active complex. The reaction may realize for each cell, and the total rate of reaction is the sum over all kinds of cells, whereas the local change of the number of cells having $m$ neighbors is proportional to their number,

$$
W_{m}=Q_{0} N_{\mathrm{f} m} \operatorname{EXP}\left(-\frac{\Delta H_{m}^{0}}{R_{\mathrm{g}} T}\right),
\tag{15}
$$

where $\Delta H_{m}^{0}$ is the enthalpy of the active complex formation, and $Q_{0}$ is the normalization coefficient. However, the total change of the number of cells of each kind depends also on the transformation of cells of different kind: around the released cell, the cells characterized by the number of neighbors ($m-$
1) transform to these with $m$ neighbors, and the related change of $N_{\mathrm{f} m}$ is found from Eqs. [12]-[14]. Let us assume that the active complex formation enthalpy linearly depends on the internal surface area and is proportional to the surface tension.

![](./images/812456581680594945_1.jpg)

FIG. 1. Kinetics of growth of internal surface in nonequilibrium solid.

Calculations. The calculations are carried out for the temperature $T=300 \mathrm{~K}$ and the surface tension $\sigma=70 \mathrm{~J} / \mathrm{m}^{2}$. The computing program for the estimation of the reaction rate of micropore cluster formation comprises the following parts:

1. The main program: (a) for each moment of time, the related value of the number of empty cells is estimated from Eqs. [12]-[15]; if its rising is not less 1 (which means that the number of empty cells increases by 1 or more), all eventual options of the possible change of $\xi^{*}(m)$ are tested with evaluation of the change of the free energy and the related active complex formation energy; (b) for all of the above-mentioned options the probabilities of their realization (their weights) are found from Eq. [11]; (c) the random number is requested; (d) the whole interval from 0 to 1 is divided into parts, each part corresponding to several numbers; the option from item (b) with its weight is compared to the random number, if this is in the corresponding interval, the option is accepted; (e) for the chosen option, all related changes of thermodynamic functions, comprising the internal surface area, are calculated.
2. The subroutine of calculation of the value of free energy/activation energy from Eqs. [1]-[6].
3. The subroutine for generation of random numbers.
4. The subroutine of calculation of the value of the change of all values of $N_{\mathrm{f}}(m)$ from Eq. [12] and the internal surface area.

The results of calculations for the system containing 10,000 cells are presented in Figs. 1 and 2.

As we see from the graphs, the behavior of both functions is

![](./images/812456581680594945_2.jpg)

FIG. 2. Kinetics of rising of porosity in nonequilibrium solid.

very similar. The auto-acceleration-like form can be explained if we take into account that the growth of porosity leads to a decrease in mechanical stability of the solid phase.

Percolation. Now, let us apply the combined thermodynamically limited Monte Carlo approach to simulation of percolation. We do it in two stages: (1) estimation of percolation threshold for various numbers of cells (in comparison with the analogous parameter obtained by ordinary Monte Carlo approach), and (2) study of the tortuosity when the microporosity rises.

We assume that the head and bottom edges are permeable, and others (side edges) are not.

Estimation of percolation threshold. The estimation of the minimum number of empty cells which allows percolation in the studied system (percolation threshold) is carried out based on the same program. The system is considered as the combination of $(n+1)$-groups of cells, according to their kinds, the cells inside the same group being equivalent. The thermodynamic factor stimulating the empty cell formation (weight) is found from Eq. [11]-[15].

1. In the first step, the program selects randomly the kind of cells where the release is expected, taking into account the thermodynamic weight [11]. The probability of selection of the $m$th group is proportional to the thermodynamic weight obtained from Eq. [11] and normalized so that the sum of all probabilities (for all kinds of cells) is 1. Each kind of cells corresponds to a numerical interval between 0 and 1. Then, the random number (between 0 and 1) is found, and one selects the kind of cells corresponding to the value of the random number.

2. In the second step, inside the selected group of equivalent cells containing $m$ neighbors the cell for transformation into micropore is selected randomly by the ordinary Monte Carlo. For all cells around the chosen one, the number of empty neighbors increases by 1. For edge and corner cells, the number of treated neighbors decreases, respectively. The program builds the following matrix dimensions: (a) the matrix corresponding to the cells themselves; if the cell is occupied, it corresponds to 0; if that is empty, it corresponds to 1; (b) the matrix corresponding to the number of empty cells around each of occupied cells.

3. We choose a "vertical" direction corresponding to the expected percolation. All empty cells are divided into two groups: those connected to "head" empty cells and those isolated from them. The first kind of cells is considered as the micropore cluster through which the percolation may realize.

The search of cells which join the micropore cluster is carried out on this step of calculation. The new empty cell is checked whether or not it belongs to the cluster (has direct contact with one of its empty cells); if not, the computing returns to step 1; if yes, the program checks all neighbors of the newcomer empty cell, their neighbors, etc., until no new cells belonging to the cluster are found. After that is done, the program checks whether or not any of the new cells in the cluster are at the bottom of the structure. If not, the program returns to step 1; if yes, the calculation stops, and all requested information (number of percolation threshold, the form of the cluster, etc.) is provided.

We carried out calculations for 2- and 3-dimensional systems and found that the 3-dimensional one provides almost always down level of the percolation threshold. We explain this fact if we take into account that the 3-dimensional system allows 1 additional degree of freedom.

The results of calculations carried out for various initial numbers of cells in cube are compared to the traditional Monte Carlo procedure in which each cell can be transformed into micropore without relation to thermodynamic considerations (see Figs. 3-5).

Let us note that the selection with thermodynamic factor leads to reduction of the percolation thresholds for most of systems. However, the divergence between the random and thermodynamically limited situations is on the level of eventual error and does not allow ultimate conclusions.

Tortuosity modeling. The specific definition of tortuosity presented below has been undertaken by the author because traditional definitions could cause several difficulties in the attempt to combine the Monte Carlo approach with the thermodynamic one.

The computing program described above has been employed for the evaluation of the change of tortuosity of the microporous system formed under thermodynamic limitations.

We assume that the diffusion with minimal resistance is due to the occurrence of empty cells not only connected to the pore cluster but also connected between them on the shorter way ("vertical" connection; we mean that the percolation realizes

![](./images/812456581680594945_3.jpg)

FIG. 3. Micropores at percolation threshold: thermodynamically limited square $100\times100$.

from head to bottom). Let us call these cells 1st kind cells. If percolation is due to cells connected in the plane perpendicular to the direction of percolation (horizontal connection), the way increases (2nd kind cells). The same happens twice if the percolation way comprises motion back (toward the head), which corresponds to 3rd kind cells.

Now, let us evaluate the general formula of tortuosity based on the definition that tortuosity is the inverse diffusional con- ductivity, using the analogy with electricity.

1. Let us consider a cube $(n_{m}\times n_{m}\times n_{m}=N_{0})$ containing empty cells only. Of course, its conductivity is maximal, and minimal tortuosity is $\tau=1$ by definition.

![](./images/812456581680594945_4.jpg)

FIG. 4. Percolation way at threshold: thermodynamically limited square $100\times100$.

![](./images/812456581680594945_5.jpg)

FIG. 5. Threshold of random (+) and thermodynamically determined (○) clusters.

2. Let us consider the same cube but containing $n_{m}$ empty cells of 1st kind on the vertical line. Its conductivity is $(n_{m}^{2})$ times less but per the empty cell no change; let us assume also in this situation $\tau=1$ by definition.

3. Let us consider the line of empty cells comprising $n_{1}=$ $n_{m}$ cells of 1st kind and $n_{2}$ of 2nd kind. Following the analogy with electrical conductivity (the resistance is proportional to the length of the conductor), the diffusional resistance (analo- gous to tortuosity) is found from
$$
R_{\mathrm{d}}=\tau=1+n_{2}/n_{1}=1+n_{2}/n_{m}. \tag{16}
$$

4. Let us consider the line of empty cells comprising $n_{1}$ cells of 1st kind, $n_{2}$ of 2nd kind, and $n_{3}$ of 3rd kind (forwarding motion back); $n_{1}=n_{m}+n_{3}$. Following the analogy with electrical conductivity, the diffusional resistance (analogous to tortuosity) is found from
$$
\begin{aligned}
R_{\mathrm{d}}=\tau=1+n_{2}/n_{1} & +n_{3}/n_{1} \\
& =1+n_{2}/(n_{m}+n_{3})+n_{3}/(n_{m}+n_{3}). \tag{17}
\end{aligned}
$$

5. Let us consider a cluster of empty cells containing $n_{1}$ cells of 1st kind, $n_{2}$ of 2nd kind, and $n_{3}$ of 3rd kind. Additional 1st kind cells increase the conductivity (as in electricity the parallel conductors provide the sum of conductivities) and reduce the tortuosity. The tortuosity is found from
$$
\tau=1+n_{2}/(n_{1}+n_{3})+n_{3}/(n_{1}+n_{3}). \tag{18}
$$

6. Let us consider a number $n_{\mathrm{c}}$ of isolated clusters of empty cells comprising $n_{1k}$ cells of 1st kind, $n_{2k}$ of 2nd kind, and $n_{3k}$ of 3rd kind ( $k$ changes from 1 to $n_{\mathrm{c}}$). Additional 1st kind cells increase the conductivity (as in electricity the parallel conduc-

![](./images/812456581680594945_6.jpg)

FIG. 6. Inverse tortuosity vs microporosity, cube $10 \times 10 \times 10$.

tors provide the sum of conductivities). The diffusional resis- tance (analogous to tortuosity) is found from

$$
1 / \tau=\frac{1}{n_{\mathrm{c}}} \sum_{k=1}^{n_{\mathrm{c}}} \frac{n_{1 k}}{n_{1 k}+n_{2 k}+n_{3 k}}=\frac{1}{n_{\mathrm{c}}} \sum_{k=1}^{n_{\mathrm{c}}} \frac{1}{1+n_{2 k} / n_{1 k}+n_{3 k} / n_{1 k}}.
\tag{19}
$$

If we assume the fractal structure of the microporous system, the distribution of empty cells of all kinds is approximately the same, and from [19] we obtain

$$
1 / \tau \approx 1 /\left(1+n_{2} / n_{1}+n_{3} / n_{1}\right).
\tag{20}
$$

![](./images/812456581680594945_7.jpg)

FIG. 7. Inverse tortuosity vs microporosity, cube $18 \times 18 \times 18$.

![](./images/812456581680594945_8.jpg)

FIG. 8. Surface of random (+) and thermodynamically limited $(\bigcirc)$ clus ters.

Taking into account that not all clusters are permeable, the resulting tortuosity is evaluated from

$$
1 / \tau=\frac{N_{\mathrm{p}^{+}}-N_{\mathrm{p}^{-}}}{N_{\mathrm{p}}},
\tag{21}
$$

where $N_{\mathrm{p}^{+}}$is the number of cells of 1st kind (connected vertically from head to bottom), $N_{\mathrm{p}}$ is the total number of empty cells belonging to permeable clusters, and $N_{\mathrm{p}^{-}}$is the number of empty cells causing the motion back (from bottom to head) belonging to the same clusters.

The program employed at this stage was very similar to that used for the estimation of the percolation threshold, with the only difference being that the calculation was not stopped at the percolation threshold but continued until the specified value of microporosity.

The results are given in Figs. 6 and 7.

As we may see from Figs. 6 and 7, as soon as the percolation process starts, the inverse tortuosity (1/tortuosity) sharply in- creases, and then its rising becomes slow while increases with microporosity.

Structural aspect of thermodynamic limitation. The next study concerns the regularity of the obtained structure. For its characterization, we need to choose any formal parameters. For this aim, let us consider the principal difference of random and regular structures.

If the thermodynamic limitation does not appear, one obtains an ordinary random cluster. Its randomness can be character- ized by the entropy and related free energy estimated from Eq. [6] for $\sigma=0$. With the increase in the number of cells, the free energy is $\lim _{N_{0} \rightarrow \infty}\left(\Delta G_{\Sigma}(\sigma=0) / N_{0}\right)=0$. However, if the surface tension is not zero, its value per cell goes to a constant

![](./images/812456581680594945_9.jpg)

FIG. 9. Free energy (Gibbs) of random (+) and thermodynamically determined (○) clusters.

value at a large number of cells. This value is larger than that obtained at thermodynamic limitation (because this one im- poses the minimum of free energy). Hence, the first parameter characterizing the randomness of the obtained cluster is free energy. The free energy in both cases is obtained from Eq. [6].

The other related characteristic is the internal surface area. For the random cluster, the surface area has no importance, whereas in the case of thermodynamic limitation it does.

The calculations were carried out for the microporosity 20% at various numbers of cells.

The graphs of free energy and surface area are presented in Figs. 8 and 9. We may conclude that both parameters exhibit obvious sensitivity to thermodynamic limitation. The thermo- dynamic limitation of Monte Carlo release of cells leads to considerable reduction of the free surface and the free energy of the system.

Conclusions. The problem of pore formation in limited (small) volume has been considered. General equations de- scribing the system in the continuous (many particles) and discrete (few number of particles) cases have been obtained. It has been shown that pore formation is not limited by nucleus genesis, because of entropic reasons. Kinetic limitation leads to the auto-acceleration-like form of the dependence of the num- ber of empty cells and the internal area functions.

The percolation problem has been solved for 2- and 3-di- mensional cases with comparison of systems obtained by tra- ditional Monte Carlo and thermodynamic factors. The 3-di- mensional situation leads to reduction of the percolation threshold. However, the difference in the values of percolation thresholds estimated by the ordinary Monte Carlo simulation and with thermodynamic limitation is not significant (less than the eventual error).

The change of tortuosity was estimated. At the percolation threshold, the tortuosity decreases rapidly, then very slowly with an increase in microporosity, and only at very high microporosity (close 1) the decrease in tortuosity is again sharp.

The influence of the thermodynamic limitation on the regu- larity of the micropore cluster has been analyzed based on the consideration of the behavior of free energy and surface area of the cluster. It has been found that both these structural param- eters significantly decrease if the thermodynamic limitation is imposed.

## ACKNOWLEDGMENT

I thank very much Professor Moshe Sheintuch (Department of Chemical Engineering, Technion-IIT, Haifa) for his help in the definition of this problem and further fruitful discussion.

## REFERENCES

1. Gutfraind, R., and Sheintuch, M., *Chem. Engng. Sci.* **47**, 4425 (1992).
2. Avnir, D., Farin, D., and Pfeifer, P., *J. Colloid Interface Sci.* **103**, 112 (1985).
3. Sahimi, M., "Flow and Transport in Porous Media and Fractured Rock." VCH, Weinheim/New York.
4. Rudzinski, W., and Everett, D. H., "Adsorption of Gases on Heterogeneous Surfaces." Academic Press, London, 1992.
5. Romm, F., *J. Colloid Interface Sci.* **179**, 1 (1996).
6. Romm, F., *J. Colloid Interface Sci.* **179**, 12 (1996).