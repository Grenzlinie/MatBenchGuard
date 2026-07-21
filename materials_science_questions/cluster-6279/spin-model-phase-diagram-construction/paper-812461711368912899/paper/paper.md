Chiral segregation, an unusual racemic phase, and a residual entropy for a lattice system of model chiral molecules

This content has been downloaded from IOPscience. Please scroll down to see the full text.

J. Stat. Mech. (2010) P12027

(http://iopscience.iop.org/1742-5468/2010/12/P12027)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 128.192.114.19
This content was downloaded on 30/08/2015 at 11:28

Please note that terms and conditions apply.

![](./images/812461711368912899_1.jpg)

# Chiral segregation, an unusual racemic phase, and a residual entropy for a lattice system of model chiral molecules

I Medved'$^{1,2,4}$, A Trník$^{1,2}$ and D A Huckaby$^{3}$

$^{1}$ Department of Physics, Constantine The Philosopher University, 94974 Nitra, Slovakia
$^{2}$ Department of Materials Engineering and Chemistry, Czech Technical University, 16629 Prague, Czech Republic
$^{3}$ Department of Chemistry, Texas Christian University, Fort Worth, TX 76129, USA

E-mail: imedved@ukf.sk, atrnik@ukf.sk and d.huckaby@tcu.edu

Received 12 October 2010
Accepted 22 November 2010
Published 15 December 2010

Online at stacks.iop.org/JSTAT/2010/P12027
doi:10.1088/1742-5468/2010/12/P12027

**Abstract.** We study low temperature phases of a 2D model molecular system that contains an equimolar mixture of a chiral molecule and its mirror image. The molecules lie on a thin film in the close-packed regime, occupying the sites of a honeycomb lattice, and neither enantiomer is externally favored. We show that, in one range of interactions, chiral segregation into two ordered homochiral phases containing a single enantiomer occurs. An ordered racemic phase occurs in which one sublattice is occupied by one enantiomer and the other sublattice is occupied by the other enantiomer. When second-closest group interactions are relaxed, the ground states of the homochiral and the associated racemic phase have the same energy; in fact, the total number of ground state configurations becomes infinite and yields a residual entropy. This residual entropy is calculated exactly. In a third range of interactions, an unusual ordered racemic phase occurs in which the two enantiomers are assembled in alternating infinite rows, thus forming a pattern independent of the sublattice structure. In order to prove these results, we apply the Pirogov–Sinai theory, a powerful generalization of the Peierls-type approach of statistical mechanics.

**Keywords:** rigorous results in statistical mechanics, classical phase transitions (theory), liquid films (theory)

$^{4}$ Author to whom any correspondence should be addressed.

©2010 IOP Publishing Ltd and SISSA
1742-5468/10/P12027+14$30.00

A lattice system of model chiral molecules

Contents

1. Introduction 2
2. A system of model chiral molecules 4
3. Reformulation of the model 5
4. Ground states 7
4.1. Triangle potential $\Phi_T$ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
4.2. Minimization of $\Phi_T$ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
4.3. Construction of ground states . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
4.4. Residual entropy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
5. Low temperature phases 11
Acknowledgments 13
References 14

## 1. Introduction

Chiral molecules play an important role in biology and organic chemistry. It is a great challenge to predict whether, at sufficiently low temperatures, an equimolar mixture of a chiral molecule and its molecular mirror image, usually denoted as $d$ and $l$ enantiomers, will form a racemic phase (containing equal numbers of $d$ and $l$ molecules) or will undergo chiral segregation and form two homochiral phases (each containing a single enantiomer, $d$ or $l$). The Peierls argument [1,2] was used to give the first proof that chiral segregation into ordered homochiral phases occurs at low temperatures in a two-dimensional lattice gas model of enantiomers [3,4]. The Pirogov-Sinai theory [5,6] and its extension [7] were used to prove the existence of ordered homochiral [8] and racemic [9] crystalline phases in a three-dimensional lattice gas model of enantiomers.

Andelman and de Gennes [10]-[12] studied a model for chiral segregation of enantiomers on the surface of water (see figure 1). They used a single parameter, $\Delta$, defined as the difference between the partition functions of two molecules with identical chirality and two with opposite chirality, to conclude the tendency for the formation of heterochiral or homochiral phases when $\Delta < 0$ or $\Delta > 0$, respectively. Although their approach was not rigorous and they limited their analysis to several particular kinds of intermolecular interactions, their conclusions were later proven correct and extended to a wide range of interactions [13]. However, instead of a single parameter $\Delta$, three parameters turned out to be necessary. Computer simulations have also been used to study chiral segregation [14] in a model similar to that of Andelman and de Gennes. The latter model and its extension was also studied rigorously, proving the presence of homochiral as well as heterochiral ordered phases [15]. Again, the same three parameters had to be used to predict the phases correctly. A mesoscopic type of approach to chiral segregation based on an effective pair potential theory has also appeared [16,17].

doi:10.1088/1742-5468/2010/12/P12027 2

A lattice system of model chiral molecules

![](./images/812461711368912899_2.jpg)

Figure 1. Two enantiomers on the surface of water. An enantiomer will be said to be an l molecule (d molecule) if the groups A, B, and C are ordered clockwise (counterclockwise) when viewed from above.

The experimental separation of a racemic solution into pure d and l crystals was first recorded in 1848 by Pasteur [18], but it was not until the mid-1990s that the separation of a racemic solution into homochiral phases was observed in a Langmuir film on the surface of water [19]-[21] and in adsorbed phases on the surface of mica [22] and graphite [23]. Chiral segregation has been the focus of many recent experimental investigations, and we refer readers to reviews [16,24] on this subject.

In this paper we study low temperature phases for a model system of enantiomers, like those illustrated in figure 1, in which equal numbers of the two enantiomers occupy the sites of a honeycomb lattice. We prove that, depending on the interaction values, chiral segregation can occur, and that, besides an expected racemic phase in which each enantiomer occupies a different one of the two sublattices, an unusual racemic phase not copying the underlying sublattice structure arises. In addition, we also consider one case of the model in which the second-neighboring group interactions are relaxed, and we are able to calculate exactly the resulting residual entropy.

Each molecular tripod can be placed at a given lattice site, x, only in two orientations that are symmetric with the honeycomb lattice structure: either each of the three groups A, B, and C in a tripod lies along a segment connecting x with its neighboring site or each of the three groups lies in the middle between two such segments. We already studied the two cases in which all tripods are either in the former position or in the latter position [13,15]. Here we wish to consider the remaining case when half of the tripods have one orientation and the other half have the other orientation, with all neighboring tripods always being in opposite orientations (see figure 2).

Due to the close-packed regime, the numbers of closest interacting groups in any configuration in a finite portion, $\Lambda$, of the lattice must satisfy three equalities (corresponding to the three groups A, B, and C), with a possible error of the $\Lambda$-boundary size. Therefore, when constructing ground states, these equalities must be taken into account. In [15] we achieved this by identifying the ground states with the configurations that have a minimal specific energy. This approach allowed us to eliminate the boundary errors once the van Hove limit was taken. On the other hand, in [13] no boundary errors happened to arise whenever $\Lambda$ was a union of elementary hexagons. Hence, it sufficed to work with elementary hexagons to avoid any boundary effects. Contrary to what was done in these two previous studies, here we circumvent this problem by imposing periodic boundary conditions. This approach substantially simplifies the model by eliminating three of the six closest pair interactions so that only three parameters, coinciding with the above-mentioned ones, need to be considered (see section 3). Nevertheless, in order to

doi:10.1088/1742-5468/2010/12/P12027

A lattice system of model chiral molecules

![](./images/812461711368912899_3.jpg)

**Figure 2.** The arrangement of tripods on the honeycomb lattice. Groups $X,Y,Z$ and $X',Y',Z'$ of two neighboring molecular tripods are indicated.

exclude infinite degeneracy of ground states, we include two second-closest interactions, one of which may be eliminated (again, due to the close-packed regime), leaving us with another, fourth parameter to be considered. Such an advantageous reformulation of the model provides a straightforward explanation of which parameters are necessary and sufficient for correctly predicting the thermodynamic behavior of the model, including the existence of low temperature phases.

We wish to apply the Pirogov–Sinai theory [5, 6] to conclude the presence of low temperature phases. Its application is possible only when the number of ground states is finite and the Peierls condition is satisfied. (The condition states that, roughly speaking, in any configuration, $\omega$, an energy excess over a ground state configuration is proportional to the size of the boundaries separating various ground state regions in $\omega$.) In order to verify the Peierls condition, we use the method of an $m$-potential [25] as follows. We consider triangles (segments composed of four lattice sites, one site being from a sublattice of the honeycomb lattice and the other three sites being its closest neighbors), $T$, and rewrite the model in terms of an interaction potential, $\Phi_T$, on triangles. Then we show that there is a configuration, $\sigma$, that minimizes $\Phi_T$ in any triangle $T$. In that case $\Phi_T$ is called an $m$-potential, and the $\sigma$ so obtained are the ground states of the model (see section 4). The reason that we work with triangles is that they are the smallest lattice segments yielding the desired ground states. As soon as we have an $m$-potential, the Peierls condition is satisfied [25], and we will be able to conclude the presence of low temperature phases (see section 5).

### 2. A system of model chiral molecules

We consider a two-dimensional system of model chiral molecules in which neither enantiomer is externally favored—each of the two enantiomers is equal in number and thus

doi:10.1088/1742-5468/2010/12/P12027

A lattice system of model chiral molecules

has the same chemical potential. The model chiral molecules are the tetrahedral chiral molecules considered by Andelman and de Gennes (see figure 1). The two enantiomers are denoted as $d$ and $l$ molecules. They are placed on a regular honeycomb lattice, $\mathbb{H}$, so that each site of the lattice is occupied by a single molecular tripod center (the close-packed regime). For simplicity, the orientation of all tripods is fixed, as is shown in figure 2.

A configuration, $\omega_x$, of a tripod with a center at the site $x$ of $\mathbb{H}$ is a permutation of the triple $(A,B,C)$ of the groups $A$, $B$, and $C$; here the order corresponds to that of $(X,Y,Z)$ in figure 2. The interaction between molecules is limited to nearest neighbors: two neighboring molecules interact via pairs of their closest groups (shown as $X'Z$ and $Y'Z$ in figure 2) as well as their second-closest groups (shown as $XX'$ and $YY'$ in figure 2). Namely, we consider the Hamiltonian

$$
H_{\Lambda}(\omega_{\Lambda}) = \sum_{XY} \varepsilon_{XY} \, N_{\Lambda}^{XY}(\omega_{\Lambda}) + \varepsilon_{+}N_{\Lambda}^{+}(\omega_{\Lambda}) + \varepsilon_{-}N_{\Lambda}^{-}(\omega_{\Lambda}) \tag{1}
$$

for a configuration $\omega_{\Lambda} = (\omega_x)_{x \in \Lambda}$ on a finite portion $\Lambda$ of $\mathbb{H}$. The sum in (1) is over the six possible pairs $XY = AB, AC, BC, AA, BB, CC$ of closest interacting groups, $N_{\Lambda}^{XY}(\omega_{\Lambda})$ is the number of closest group pairs $XY$ in $\omega_{\Lambda}$, while $N_{\Lambda}^{+}(\omega_{\Lambda})$ and $N_{\Lambda}^{-}(\omega_{\Lambda})$ are the number of second-closest pairs of identical groups (i.e., $AA, BB, CC$) and distinct groups (i.e., $AB, AC, BC$) in $\omega_{\Lambda}$, respectively. In addition, $\varepsilon_{XY}$ and $\varepsilon_{\pm}$ are the strengths of interaction between the closest groups $X$ and $Y$ and between identical/distinct second-closest groups, respectively. Since the chemical potentials of the enantiomers are identical in an equimolar system, $\mu_d = \mu_l \equiv \mu$, the term $\mu_l N_l(\omega_{\Lambda}) + \mu_d N_d(\omega_{\Lambda}) = \mu|\Lambda|$ usually appearing in the Hamiltonian is here configuration independent due to the close-packed regime considered, and is thus omitted.

Remark.

(a) If the interactions between the second-closest group pairs are not included in the model, the ground state configurations are infinitely degenerate and possess a residual entropy. We would then be unable, with the help of the methods used here, to obtain the structure of its low temperature phases.

(b) Fixing the closest group pairs in two neighboring molecules, there are then only two possible sets of the second-closest group pairs. Counting how many of the second-closest pairs are identical and distinct distinguishes between the two sets. That is why we consider only the two second-closest interaction strengths $\varepsilon_{\pm}$.

### 3. Reformulation of the model

Let us rewrite the model in terms more appropriate for the study of low temperature phases. First, since the presence of a phase is independent of boundary conditions [26], we choose to work with periodic boundary conditions. Thus, we will consider the Hamiltonian (1) on a finite torus, $\mathcal{T}_n$, $n = 1,2,\dots$, whose cell is specified by the two vectors $2n\boldsymbol{i}$ and $2n\boldsymbol{j}$ as shown in figure 3, where $\boldsymbol{i}$ and $\boldsymbol{j}$ are the unit vectors in the horizontal and vertical direction, respectively.

Second, we use the observation that, due to the close-packed regime, the numbers $N_{\mathcal{T}_n}^{XY}(\omega_{\mathcal{T}_n})$ and $N_{\mathcal{T}_n}^{\pm}(\omega_{\mathcal{T}_n})$ are not independent, but are restrained. Indeed, in any $\omega_{\mathcal{T}_n}$ the

doi:10.1088/1742-5468/2010/12/P12027

A lattice system of model chiral molecules

![](./images/812461711368912899_4.jpg)

Figure 3. The cell of the torus $\mathcal{T}_2$ (the full line) specified by the two vectors $4\boldsymbol{i}$ and $4\boldsymbol{j}$. The sites in $\mathcal{T}_2$ are represented by black disks. The 16 triangles lying inside $\mathcal{T}_2$ are outlined.

group $A$, say, from a given molecule always interacts with two closest groups $X=A,B,C$ from a neighboring molecule. Consequently, the total number, $2N_{\mathcal{T}_n}^{AA}(\omega_{\mathcal{T}_n})+N_{\mathcal{T}_n}^{AB}(\omega_{\mathcal{T}_n})+N_{\mathcal{T}_n}^{AC}(\omega_{\mathcal{T}_n})$, of the groups in $\mathcal{T}_n$ with which groups $A$ interact is equal to $2|\mathcal{T}_n|$; analogous conclusions are true for groups $B$ and $C$. As a result, the three equations

$$
2N_{\mathcal{T}_n}^{AA}(\omega_{\mathcal{T}_n}) + N_{\mathcal{T}_n}^{AB}(\omega_{\mathcal{T}_n}) + N_{\mathcal{T}_n}^{AC}(\omega_{\mathcal{T}_n}) = 2|\mathcal{T}_n|, \tag{2a}
$$

$$
2N_{\mathcal{T}_n}^{BB}(\omega_{\mathcal{T}_n}) + N_{\mathcal{T}_n}^{AB}(\omega_{\mathcal{T}_n}) + N_{\mathcal{T}_n}^{BC}(\omega_{\mathcal{T}_n}) = 2|\mathcal{T}_n|, \tag{2b}
$$

$$
2N_{\mathcal{T}_n}^{CC}(\omega_{\mathcal{T}_n}) + N_{\mathcal{T}_n}^{AC}(\omega_{\mathcal{T}_n}) + N_{\mathcal{T}_n}^{BC}(\omega_{\mathcal{T}_n}) = 2|\mathcal{T}_n| \tag{2c}
$$

must be true for any $n$ and $\omega_{\mathcal{T}_n}$. Moreover, we have

$$
N_{\mathcal{T}_n}^{+}(\omega_{\mathcal{T}_n}) + N_{\mathcal{T}_n}^{-}(\omega_{\mathcal{T}_n}) = 3|\mathcal{T}_n| \tag{2d}
$$

because there are two second-closest group pairs in a pair of neighboring molecules and the number of pairs of neighboring molecules in $\mathcal{T}_n$ is $3|\mathcal{T}_n|/2$.

Using (2a)-(2d), we may eliminate $N_{\mathcal{T}_n}^{\kappa}$ with $\kappa=AA,BB,CC,+$ and rewrite the model Hamiltonian (1) in the torus $\mathcal{T}_n$ as $H_{\mathcal{T}_n}(\omega_{\mathcal{T}_n})=H_{\mathcal{T}_n}^{*}(\omega_{\mathcal{T}_n})+c_0|\mathcal{T}_n|$, where

$$
H_{\mathcal{T}_n}^{*}(\omega_{\mathcal{T}_n}) = \Delta_{AB}N_{\mathcal{T}_n}^{AB}(\omega_{\mathcal{T}_n}) + \Delta_{AC}N_{\mathcal{T}_n}^{AC}(\omega_{\mathcal{T}_n}) + \Delta_{BC}N_{\mathcal{T}_n}^{BC}(\omega_{\mathcal{T}_n}) + \delta N_{\mathcal{T}_n}^{-}(\omega_{\mathcal{T}_n}) \tag{3}
$$

with

$$
\Delta_{XY} = \varepsilon_{XY} - \frac{\varepsilon_{XX} + \varepsilon_{YY}}{2}, \quad \delta = \varepsilon_{-} - \varepsilon_{+}, \tag{4}
$$

doi:10.1088/1742-5468/2010/12/P12027

A lattice system of model chiral molecules

![](./images/812461711368912899_5.jpg)

Figure 4. A triangle $T$ used for the minimization of $\Phi_{T}$.

and the constant $c_0 = \varepsilon_{AA} + \varepsilon_{BB} + \varepsilon_{CC} + 3\varepsilon_+$. Since the Hamiltonians $H_{\mathcal{T}_n}$ and $H_{\mathcal{T}_n}^*$ are equal up to a configuration-independent constant, their phases (phase diagrams) are identical. Therefore, in the following we will work only with $H_{\mathcal{T}_n}^*$ because instead of the eight interaction parameters in the original model (1), the equivalent model (3) contains just four parameters, which will significantly simplify our subsequent analysis. In addition, we will assume that $\Delta_{AB}$, $\Delta_{AC}$, and $\Delta_{BC}$ are mutually distinct, for such extreme possibilities do not correspond to physically interesting situations.

## 4. Ground states

In order to study low temperature phases of our model (3), we shall employ the method of an $m$-potential [25]. To this end, we consider triangles, $T$, i.e., segments of $\mathbb{H}$ consisting of four sites $x$, $y_1$, $y_2$, and $y_3$ such that $x$ is from a triangular sublattice $\mathbb{T}_1$ of $\mathbb{H}$ and the $y_i$ are the three nearest neighbors of $x$ (here $\mathbb{T}_1$ is either of the two sublattices of $\mathbb{H}$, but the same for all triangles). One such triangle is illustrated in figure 4. Triangles turn out to be the smallest finite segments of $\mathbb{H}$ that are sufficiently large to generate the desired ground state configurations.

### 4.1. Triangle potential $\Phi_T$

Since each (closest or second-closest) interaction pair $XY$ is contained in a single triangle, we have
$$
H_{\mathcal{T}_n}^*(\omega_{\mathcal{T}_n}) = \sum_{T\subset\mathcal{T}_n} \Phi_T(\omega_T), \tag{5}
$$
where
$$
\Phi_T(\omega_T) = \Delta_{AB}N_T^{AB}(\omega_T) + \Delta_{AC}N_T^{AC}(\omega_T) + \Delta_{BC}N_T^{BC}(\omega_T) + \delta N_T^-(\omega_T). \tag{6}
$$

As soon as we show that, depending on $\Delta_{XY}$ and $\delta$, there is a configuration $\sigma$ that minimizes $\Phi_T$ in any triangle $T$ (i.e., $\Phi_T(\sigma_T) = \min_\omega \Phi_T(\omega_T)$ for all $T$), then $\Phi_T$ is called an $m$-potential [25]. To obtain $\sigma$, we first determine all configurations, $\sigma_T$, in $T$ that have a minimal value of $\Phi_T$. Then, using only these $\sigma_T$, we construct all possible

doi:10.1088/1742-5468/2010/12/P12027

A lattice system of model chiral molecules

configurations, $\sigma$, on $\mathbb{H}$. The $\sigma$ so obtained are all the ground state configurations, and $\Phi_T$ is an $m$-potential.

Remark. If no $\sigma$ can be constructed in some range of interactions, we have no $m$-potential and we will not be able to draw any conclusions as to the presence of a low temperature phase. As we will see later in this section, this will actually happen in three ranges of interactions. Then a finite segment of $\mathbb{H}$ larger than a triangle may perhaps be employed to obtain an $m$-potential.

### 4.2. Minimization of $\Phi_T$

In order to obtain configurations, $\sigma_T$, on a triangle $T$ that have (depending on $\Delta_{XY}$ and $\delta$) a lowest value of the potential $\Phi_T$, i.e.,

$$
\Phi_T(\sigma_T) = \min_{\omega_T} \Phi_T(\omega_T), \tag{7}
$$

we consider a triangle $T = \{x, y_1, y_2, y_3\}$ and configurations $\omega_T = \{\omega_x, \omega_{y_1}, \omega_{y_2}, \omega_{y_3}\}$ and study the values of $\Phi_T(\omega_T)$ for all possible $\omega_T$. Without loss of generality, we take $\omega_x = (ABC)$ as shown in figure 4, because a configuration in $T$ with any other $\omega_x$ can be obtained by a suitable rotation and/or reflection. Since $\Phi_T(\omega_T) = \sum_{i=1,2,3} \Psi_i(\omega_{P_i})$, where the sum is over the three pairs $P_i = (x, y_i)$ and $\Psi_i(\omega_{P_i}) = \Delta_{AB}N_{P_i}^{AB}(\omega_{P_i})+\Delta_{AC}N_{P_i}^{AC}(\omega_{P_i})+ \Delta_{BC}N_{P_i}^{BC}(\omega_{P_i}) + \delta N_{P_i}^{-}(\omega_{P_i})$, we may consider each pair $P_i$ separately as follows.

For each $i = 1$-$3$, $\Psi_i(\omega_{P_i})$ attains six possible values, one for each configuration of $y_i$. These possible values of $\Psi_i(\omega_{P_i})$ are given in table 1. Also given in table 1 are the (easily determined) conditions under which each of the six values of $\Psi_i(\omega_{P_i})$ is lowest; the ordering $\Delta_{BC} < \Delta_{AC} < \Delta_{AB}$ is assumed without loss of generality. Note that the ordering precludes some of the values of $\Psi_i(\omega_{P_i})$ from ever being lowest.

We may now readily obtain lowest values of $\Phi_T$ and the configurations $\sigma_T$ for which $\Phi_T$ attains these values. The six cases that result in a minimal $\Phi_T$ are summarized in table 2, and the triangle configurations $\sigma_T$ are shown in figures 5(a), 6(a), 7(a), and 8. For example, from table 1 it follows that if $\delta > 0$ and $\Delta_{AC} < \delta < \Delta_{AB}$, then $\Psi_i(\omega_{P_i})$, $i = 1$-$3$, are lowest for $\omega_{y_1} = (BAC)$, $\omega_{y_2} = (BAC)$, and $\omega_{y_3} = (ABC)$ so the lowest value of $\Phi_T$ is $(\Delta_{AC} + \delta) + (\Delta_{BC} + \delta) + (\Delta_{AC} + \Delta_{BC}) = 2(\Delta_{AC} + \Delta_{BC} + \delta)$ and it is attained for $\sigma_T = \{(ABC), (BAC), (BAC), (ABC)\}$ (see figure 6(a)). In fact, there is not only one $\sigma_T$ for each of the six possible lowest values of $\Phi_T$, because at the central site, $x$, of the triangle one may take any of the six tripod configurations and not only $\omega_x = (ABC)$. Therefore, there are actually six $\sigma_T$ for each lowest value of $\Phi_T$. Nevertheless, as pointed out above, the six $\sigma_T$ are mutually related by a suitable rotation and/or reflection.

### 4.3. Construction of ground states

Given a lowest value of $\Phi_T$ and the six corresponding triangle configurations $\sigma_T$, let us now construct, using only these six $\sigma_T$ (and their reflections and/or rotations), a configuration, $\sigma$, on the whole lattice $\mathbb{H}$. However, this can be achieved only in three cases, namely, for

(I) $\delta > 0$ and $\Delta_{AB} < \delta$,

doi:10.1088/1742-5468/2010/12/P12027

![](./images/812461711368912899_6.jpg)

Figure 5. The case $\delta > 0$ and $\Delta_{AB} < \delta$ (case I). (a) A triangle configuration $\sigma_T$ for which $\Phi_T$ is minimal. (b) The ground state configuration $\sigma_I$ generated from $\sigma_T$. A shaded (unshaded) triangle denotes that a molecule is a $d$ ($l$) molecule.

(II) $\delta > 0$ and $\Delta_{AC} < \delta < \Delta_{AB}$,
(III) $\delta < 0$ and $\Delta_{AB} < 0$

(see figures 5–7); it is assumed that $\Delta_{BC} < \Delta_{AC} < \Delta_{AB}$. As a result, the $\sigma$ so constructed are all the ground state configurations, and $\Phi_T$ is an $m$-potential (in a given range of interactions).

As a matter of fact, in each of the three ranges I–III there are six (periodic) configurations $\sigma$. Since they are symmetry related by rotations and/or reflections, there is actually only one sixfold-degenerate ground state to be denoted as $\sigma_I$, $\sigma_{II}$, and $\sigma_{III}$, respectively. We observe that $\sigma_I$ is homochiral (containing either $d$ molecules or $l$ molecules), whereas $\sigma_{II}$ and $\sigma_{III}$ are racemic (containing an equal number of $d$ and $l$ molecules). Moreover, while in $\sigma_{III}$,$d$ and $l$ molecules are on different sublattices, in $\sigma_{II}$ alternating infinite parallel rows of $d$ and $l$ molecules are formed, yielding a pattern independent of the sublattice structure that is not *a priori* expected.

The three cases in which a $\sigma_T$ has a minimal $\Phi_T$ but from which no $\sigma$ can be constructed are illustrated in figure 8.

### 4.4. Residual entropy
The ground state configurations $\sigma_I$ and $\sigma_{III}$ are ground state configurations for the special case $\Delta_{AB} < 0$ and $\delta = 0$; in fact, for this case there are an infinite number of ground state configurations and a residual entropy. The ground state configurations for the special case $\Delta_{AB} < 0$ and $\delta = 0$ are all the configurations in which the three bonds from each of the $N$ sites of a large honeycomb lattice contain one $A$, one $B$, and one $C$ group from the molecules on one sublattice, while the molecules at the sites of the other sublattice are in

A lattice system of model chiral molecules

![](./images/812461711368912899_7.jpg)

**Figure 6.** The case $\delta > 0$ and $\Delta_{AC} < \delta < \Delta_{AB}$ (case II). (a) A triangle configuration $\sigma_T$ for which $\Phi_T$ is minimal. (b) The ground state configuration $\sigma_{II}$ generated from $\sigma_T$ and a reflection of $\sigma_T$. A shaded (unshaded) triangle denotes that a molecule is a $d$ ($l$) molecule.

the single orientation in which each $X$ group is opposite the $X$ group that is on the bond of the honeycomb lattice.

If we let $A$, $B$, and $C$ represent three different colors, then the number of ground state configurations, $W^N$, equals the number of ways to color the bonds of a large honeycomb lattice of $N$ sites with three colors so that no two bonds from a single site are of the same color. Using transfer matrices, Baxter obtained the exact result [27]

$$
W^2 = \prod_{p=1}^{\infty} \frac{(3p-1)^2}{(3p-2)3p}, \tag{8}
$$

yielding $W = 1.208\,72\ldots$. Using the relationship [28]

$$
\prod_{n=1}^{\infty} \frac{n(n+a+b)}{(n+a)(n+b)} = \frac{\Gamma(1+a)\Gamma(1+b)}{\Gamma(1+a+b)} \tag{9}
$$

with $a = b = -1/3$, together with Euler's reflection formula,

$$
\Gamma(z)\Gamma(1-z) = \frac{\pi}{\sin(\pi z)} \tag{10}
$$

with $z = 1/3$, where $\Gamma$ is the gamma function, we obtain the exact closed-form expression

$$
W = \frac{\sqrt{3}}{2\pi}[\Gamma(\frac{1}{3})]^{3/2} = 1.208\,7177\ldots \tag{11}
$$

Thus, for the range $\Delta_{AB} < 0$ and $\delta = 0$, the model system has a residual entropy $S = Nk\ln W$.

doi:10.1088/1742-5468/2010/12/P12027

![](./images/812461711368912899_8.jpg)

Figure 7. The case $\delta < 0$ and $\Delta_{AB} < 0$ (case III). (a) A triangle configuration $\sigma_T$ for which $\Phi_T$ is minimal. (b) The ground state configuration $\sigma_{\text{III}}$ generated from $\sigma_T$ and its rotations. A shaded (unshaded) triangle denotes that a molecule is a $d$ ($l$) molecule.

![](./images/812461711368912899_9.jpg)

Figure 8. Triangle configurations $\sigma_T$ for the range (a) $\delta > 0$ and $\delta < \Delta_{AC}$, case IV; (b) $\delta < 0$ and $\Delta_{AC} < 0 < \Delta_{AB}$, case V; and (c) $\delta < 0$ and $0 < \Delta_{AC}$, case VI. In each case there are no configurations on the whole lattice $\mathbb{H}$ that could be generated from these $\sigma_T$.

### 5. Low temperature phases

In this section we shall prove that a unique low temperature phase is associated with each of the three ground state configurations $\sigma_{\text{I}}$, $\sigma_{\text{II}}$, and $\sigma_{\text{III}}$, and that the phase has a molecular structure very similar to its ground state.

In order to obtain the low temperature phases, we apply the Pirogov-Sinai theory [5,6] that allows one to state that any periodic ground state configuration of a system gives rise to a unique low temperature phase, provided

A lattice system of model chiral molecules

**Table 1.** The values of $\Psi_i(\omega_{P_i})$, where $\omega_{P_i} = \{\omega_x, \omega_{y_i}\}$ with $\omega_x=(ABC)$, for the three pairs $P_i=(x,y_i)$, $i=1$–3. Lowest values of $\Psi_i(\omega_{P_i})$ are obtained under the assumption $\Delta_{BC}<\Delta_{AC}<\Delta_{AB}$.

<table>
  <thead>
    <tr>
      <th>$(X_1Y_1Z_1)$</th>
      <th>$\Psi_1(\omega_{P_1})$</th>
      <th>$\Psi_1(\omega_{P_1})$ is lowest if</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$(ABC)$</td>
      <td>$\Delta_{AB}+\Delta_{AC}$</td>
      <td>$\delta>0$, $\Delta_{AB}<\delta$</td>
    </tr>
    <tr>
      <td>$(ACB)$</td>
      <td>$\Delta_{AB}+\Delta_{AC}+2\delta$</td>
      <td>$\delta<0$, $\Delta_{AB}<0$</td>
    </tr>
    <tr>
      <td>$(BAC)$</td>
      <td>$\Delta_{AC}+\delta$</td>
      <td>$\delta>0$, $\Delta_{AB}>\delta$</td>
    </tr>
    <tr>
      <td>$(BCA)$</td>
      <td>$\Delta_{AC}+2\delta$</td>
      <td>$\delta<0$, $\Delta_{AB}>0$</td>
    </tr>
    <tr>
      <td>$(CAB)$</td>
      <td>$\Delta_{AB}+2\delta$</td>
      <td>Never</td>
    </tr>
    <tr>
      <td>$(CBA)$</td>
      <td>$\Delta_{AB}+\delta$</td>
      <td>Never</td>
    </tr>
    <tr>
      <td>$(X_2Y_2Z_2)$</td>
      <td>$\Psi_2(\omega_{P_2})$</td>
      <td>$\Psi_2(\omega_{P_2})$ is lowest if</td>
    </tr>
    <tr>
      <td>$(ABC)$</td>
      <td>$\Delta_{AB}+\Delta_{BC}$</td>
      <td>$\delta>0$, $\Delta_{AB}<\delta$</td>
    </tr>
    <tr>
      <td>$(ACB)$</td>
      <td>$\Delta_{AB}+\delta$</td>
      <td>Never</td>
    </tr>
    <tr>
      <td>$(BAC)$</td>
      <td>$\Delta_{BC}+\delta$</td>
      <td>$\delta>0$, $\Delta_{AB}>\delta$</td>
    </tr>
    <tr>
      <td>$(BCA)$</td>
      <td>$\Delta_{AB}+2\delta$</td>
      <td>Never</td>
    </tr>
    <tr>
      <td>$(CAB)$</td>
      <td>$\Delta_{BC}+2\delta$</td>
      <td>$\delta<0$, $\Delta_{AB}>0$</td>
    </tr>
    <tr>
      <td>$(CBA)$</td>
      <td>$\Delta_{AB}+\Delta_{BC}+2\delta$</td>
      <td>$\delta<0$, $\Delta_{AB}<0$</td>
    </tr>
    <tr>
      <td>$(X_3Y_3Z_3)$</td>
      <td>$\Psi_3(\omega_{P_3})$</td>
      <td>$\Psi_3(\omega_{P_3})$ is lowest if</td>
    </tr>
    <tr>
      <td>$(ABC)$</td>
      <td>$\Delta_{AC}+\Delta_{BC}$</td>
      <td>$\delta>0$, $\Delta_{AC}<\delta$</td>
    </tr>
    <tr>
      <td>$(ACB)$</td>
      <td>$\Delta_{AC}+\delta$</td>
      <td>Never</td>
    </tr>
    <tr>
      <td>$(BAC)$</td>
      <td>$\Delta_{AC}+\Delta_{BC}+2\delta$</td>
      <td>$\delta<0$, $\Delta_{AC}<0$</td>
    </tr>
    <tr>
      <td>$(BCA)$</td>
      <td>$\Delta_{BC}+2\delta$</td>
      <td>$\delta<0$, $\Delta_{AC}>0$</td>
    </tr>
    <tr>
      <td>$(CAB)$</td>
      <td>$\Delta_{AC}+2\delta$</td>
      <td>Never</td>
    </tr>
    <tr>
      <td>$(CBA)$</td>
      <td>$\Delta_{BC}+\delta$</td>
      <td>$\delta>0$, $\Delta_{AC}>\delta$</td>
    </tr>
  </tbody>
</table>

**Table 2.** Lowest values of $\Phi_T$ and the configurations $\sigma_T=\{(ABC),\sigma_{y_1},\sigma_{y_2},\sigma_{y_3}\}$ for which these values are attained. It is assumed that $\Delta_{BC}<\Delta_{AC}<\Delta_{AB}$.

<table>
  <thead>
    <tr>
      <th>Case</th>
      <th>$\delta>0$</th>
      <th>$\sigma_{y_1}$</th>
      <th>$\sigma_{y_2}$</th>
      <th>$\sigma_{y_3}$</th>
      <th>$\min_{\omega_T}\Phi_T(\omega_T)$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>I</td>
      <td>$\Delta_{AB}<\delta$</td>
      <td>$(ABC)$</td>
      <td>$(ABC)$</td>
      <td>$(ABC)$</td>
      <td>$2(\Delta_{AB}+\Delta_{AC}+\Delta_{BC})$</td>
    </tr>
    <tr>
      <td>II</td>
      <td>$\Delta_{AC}<\delta<\Delta_{AB}$</td>
      <td>$(BAC)$</td>
      <td>$(BAC)$</td>
      <td>$(ABC)$</td>
      <td>$2(\Delta_{AC}+\Delta_{BC}+\delta)$</td>
    </tr>
    <tr>
      <td>IV</td>
      <td>$\delta<\Delta_{AC}$</td>
      <td>$(BAC)$</td>
      <td>$(BAC)$</td>
      <td>$(CBA)$</td>
      <td>$\Delta_{AC}+2\Delta_{BC}+3\delta$</td>
    </tr>
    <tr>
      <td></td>
      <td>$\delta<0$</td>
      <td>$\sigma_{y_1}$</td>
      <td>$\sigma_{y_2}$</td>
      <td>$\sigma_{y_3}$</td>
      <td>$\min_{\omega_T}\Phi_T(\omega_T)$</td>
    </tr>
    <tr>
      <td>III</td>
      <td>$\Delta_{AB}<0$</td>
      <td>$(ACB)$</td>
      <td>$(CBA)$</td>
      <td>$(BAC)$</td>
      <td>$2(\Delta_{AB}+\Delta_{AC}+\Delta_{BC}+3\delta)$</td>
    </tr>
    <tr>
      <td>V</td>
      <td>$\Delta_{AC}<0<\Delta_{AB}$</td>
      <td>$(BCA)$</td>
      <td>$(CAB)$</td>
      <td>$(BAC)$</td>
      <td>$2(\Delta_{AC}+\Delta_{BC}+3\delta)$</td>
    </tr>
    <tr>
      <td>VI</td>
      <td>$0<\Delta_{AC}$</td>
      <td>$(BCA)$</td>
      <td>$(CAB)$</td>
      <td>$(BCA)$</td>
      <td>$\Delta_{AC}+2\Delta_{BC}+6\delta$</td>
    </tr>
  </tbody>
</table>

(i) the number of ground states is finite and

(ii) the Peierls condition (see section 1) is satisfied.

Moreover, a typical configuration in the phase looks as a 'sea' of the ground state configuration containing isolated 'islands' of non-ground state configurations, with a non-zero volume density of the islands that is of the order of $\exp(-\mathrm{const}\,\beta)$, where $\beta=1/kT$ is the inverse temperature. Thus, the molecular structure of a typical configuration in the low temperature phase reproduces the molecular structure of the corresponding ground state.

doi:10.1088/1742-5468/2010/12/P12027

A lattice system of model chiral molecules

**Table 3.** The ground states and low temperature of the model.

<table>
  <thead>
    <tr>
      <th>Case</th>
      <th>$\delta$</th>
      <th>$\Delta_{XY}$</th>
      <th>Ground states (degeneracy)</th>
      <th>Low temperature phases</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>I</td>
      <td>Positive</td>
      <td>All three less than $\delta$</td>
      <td>See figure 5 ($6\times$)</td>
      <td>Homochiral</td>
    </tr>
    <tr>
      <td>II</td>
      <td></td>
      <td>Largest greater than $\delta$, the other two less than $\delta$</td>
      <td>See figure 6 ($6\times$)</td>
      <td>Unusual racemic</td>
    </tr>
    <tr>
      <td>IV</td>
      <td></td>
      <td>Two largest greater than $\delta$</td>
      <td>None obtained</td>
      <td>No conclusion</td>
    </tr>
    <tr>
      <td>III</td>
      <td>Negative</td>
      <td>All three negative</td>
      <td>See figure 7 ($6\times$)</td>
      <td>Racemic</td>
    </tr>
    <tr>
      <td>V</td>
      <td></td>
      <td>Largest positive, the other two negative</td>
      <td>None obtained</td>
      <td>No conclusion</td>
    </tr>
    <tr>
      <td>VI</td>
      <td></td>
      <td>Two largest positive</td>
      <td>None obtained</td>
      <td>No conclusion</td>
    </tr>
  </tbody>
</table>

Consequently, if a periodic ground state is racemic (with equal numbers of $d$ and $l$ molecules), the associated low temperature phase is also racemic. On the other hand, if a periodic ground state is homochiral (having $d$ or $l$ molecules alone), then the associated phase is also homochiral.

We know from section 4 that there is only one sixfold-degenerate ground state $\sigma_{\text{I}}$, $\sigma_{\text{II}}$, and $\sigma_{\text{III}}$ when $\Delta_{XY}$ and $\delta$ have values within the ranges (I) $\delta>0$ and $\Delta_{AB}<\delta$, (II) $\delta>0$ and $\Delta_{AC}<\delta<\Delta_{AB}$, and (III) $\delta<0$ and $\Delta_{AB}<0$, respectively (here we assume that $\Delta_{BC}<\Delta_{AC}<\Delta_{AB}$). Hence, the requirement (i) is satisfied. In order to verify (ii), we employ the fact that if a finite-ranged model Hamiltonian can be rewritten in terms of an $m$-potential, and the number of ground states is finite, then the Peierls condition is satisfied [25]. Since we know from section 4 that $\Phi_{T}$ is an $m$-potential in ranges I, II, and III, we conclude that (ii) is true within these three ranges of interactions.

As both (i) and (ii) are true, the Pirogov-Sinai theory implies that our model (1) or (3) has the following low temperature phases:

(i) a homochiral phase associated with the ground state $\sigma_{\text{I}}$ in range I,

(ii) a racemic phase with an unusual, striped/pair structure associated with the ground state $\sigma_{\text{II}}$ in range II,

(iii) a racemic phase with a 'usual' sublattice structure associated with the ground state $\sigma_{\text{III}}$ in range III.

The existence of the homochiral phase in range I proves that chiral segregation occurs in the system. Beyond these three ranges we obtained none of the ground states $\sigma$, and thus we are unable to draw any conclusions as to the presence of low temperature phases. These results are summarized in table 3.

### Acknowledgments

This research was supported by the Robert A Welch Foundation under Grant No. P-0446, by the VEGA under Grant No. 1/0302/09, by the FCVV Initiative under Grant No. I-06-399-01, and by the Ministry of Education, Youth and Sports of the Czech Republic, under the project No. MSM: 6840770031. IM and AT would like to thank DAH and express their appreciation for the hospitality extended to them during their stays at TCU.

doi:10.1088/1742-5468/2010/12/P12027

A lattice system of model chiral molecules

## References
[1] Peierls R F, 1936 *Proc. Cambridge Phil. Soc.* **32** 477
[2] Heilmann O J, 1974 *Commun. Math. Phys.* **36** 91
[3] Huckaby D A, Ausloos M and Clippe P, 1985 *J. Chem. Phys.* **82** 5140
[4] Huckaby D A, Shinmi M, Ausloos M and Clippe P, 1986 *J. Chem. Phys.* **84** 5090
[5] Borgs C and Imbrie J Z, 1989 *Commun. Math. Phys.* **123** 305
[6] Zahradník M, 1984 *Commun. Math. Phys.* **93** 559
[7] Bricmont J and Slawny J, 1989 *J. Stat. Phys.* **54** 89
[8] Huckaby D A, Pitiş R and Shinmi M, 1994 *J. Stat. Phys.* **75** 981
[9] Belkasri A K and Huckaby D A, 1997 *J. Phys. A: Math. Gen.* **30** 6205
[10] Andelman D and de Gennes P-G, 1988 *C. R. Acad. Sci. Paris* **307** 233
[11] Andelman D, 1989 *J. Am. Chem. Soc.* **111** 6536
[12] Andelman D, 1990 *Physica A* **168** 172
[13] Medved' I, Trník A, Belkasri A K and Huckaby D A, 2007 *J. Chem. Phys.* **126** 154512
[14] Mao L, Harris H and Stine K J, 2002 *J. Chem. Inf. Comput. Sci.* **42** 1179
[15] Medved' I, Trník A and Huckaby D A, 2009 *Phys. Rev. E* **80** 011601
[16] Nandi N and Vollhardt D, 2003 *Chem. Rev.* **103** 4033
[17] Nandi N and Vollhardt D, 2003 *J. Phys. Chem. B* **107** 3464
[18] Pasteur L, 1848 *C. R. Acad. Sci. Paris* **26** 535
[19] Brezesinski G, Rietz R, Kjaer K, Bouwman W G and Möhwald H, 1994 *Nuovo Cimento D* **16** 1487
[20] Nassoy P, Goldman M, Bouloussa O and Rondelez F, 1995 *Phys. Rev. Lett.* **75** 457
[21] Vollhardt D, Emrich G, Gutberlet T and Fuhrhop J-H, 1996 *Langmuir* **12** 5659
[22] Eckhardt C J, Peachey N M, Swanson D R, Takacs J M, Khan M A, Gong X, Kim J-H, Wang J and Uphaus R A, 1993 *Nature* **362** 614
[23] Stevens F, Dyer D J and Walba D M, 1996 *Angew. Chem. Int. Edn Engl.* **35** 900
[24] Pérez-Garcia L and Amabilino D B, 2007 *Chem. Soc. Rev.* **36** 941
[25] Holsztynski W and Slawny J, 1978 *Commun. Math. Phys.* **61** 177
[26] Gallavotti G, 1999 *Statistical Mechanics: A Short Treatise* (New York: Springer)
[27] Baxter R J, 1970 *J. Math. Phys.* **11** 784
[28] Jolley L B W, 1961 *Summation of Series* (New York: Dover) p 196

doi:10.1088/1742-5468/2010/12/P12027
14