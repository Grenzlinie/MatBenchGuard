PHILOSOPHICAL MAGAZINE A, 2002, VOL. 82, No. 2, 269-283

![](./images/811981912695373826_1.jpg)

# A theory of tracer diffusion in non-stoichiometric intermetallic compounds

I. V. BELOVA and G. E. MURCH†

Diffusion in Solids Group, Department of Mechanical Engineering,
The University of Newcastle, Callaghan, New South Wales 2308, Australia

[Received 16 November 2000 and accepted in revised form 11 May 2001]

## ABSTRACT

In this paper, the six-jump-cycle mechanism, which was conceived as a minimum-energy-penalty sequence of jumps for certain stoichiometric alloys showing antistructural disorder, is extended to non-stoichiometric compositions for alloys taking the B2 structure. We make use of the five-frequency model for impurity diffusion as a convenient framework for expressing our formalism; the antistructural atoms are analogous to the 'impurity' and the six-jump cycle acts as the diffusion mechanism unit. We derive expressions for the tracer diffusivity for both atomic components by utilizing the Ising alloy model. Monte Carlo simulation is used to test the expressions obtained; there is very good agreement.

## §1. INTRODUCTION

It was recognized very early in the history of diffusion in highly ordered inter-metallic compounds that a vacancy moving on a sequence of jumps in random directions, as in a pure metal, would soon leave a trail of disorder in its wake. Instead, a vacancy is confined to an ever smaller set of low-energy-penalty trajec-tories as the level of order increases. In the limit of perfect order in a stoichiometric alloy taking, say, the B2 structure, the vacancy moves on a six-jump cycle (6JC) in which, starting from a fully ordered configuration, the first three jumps progressively disorder the lattice while the remaining three vacancy jumps progressively reorder the lattice to a fully ordered configuration once more (Elcock and McCombie 1958).

Numerical computer simulations of diffusion in the Ising alloy model (Athènes et al. 1998, Belova and Murch 2000a) and a simpler four-frequency model (Belova et al. 1995) have shown that the 6JC mechanism certainly operates at very low tempera-tures at stoichiometry. Disorder, introduced either by temperature increase or by non-stoichiometry, soon weakens the dominance of the 6JC mechanism, as might be expected. However, the influence of the 6JC mechanism is much greater than this might imply. The activation energy associated with the tracer correlation process in the stoichiometric alloy is well described by a mean-field model based on the 6JC mechanism over a wide temperature range (Belova and Murch 2000b). Similarly, the correlation factor as measured in an isotope effect experiment tends to the 6JC value at surprisingly low levels of order (Belova and Murch 2000c). These observations show that, although the 6JC mechanism itself has a fairly limited domain of opera-

† Email: cggem@alinga.newcastle.edu.au

Philosophical Magazine A ISSN 0141-8610 print/ISSN 1460-6992 online © 2002 Taylor & Francis Ltd
http://www.tandf.co.uk/journals
DOI: 10.1080/01418610110067770

tion, fragments of the mechanism play a very important role generally in diffusion in intermetallics. The 6JC mechanism also acts as an important perfect order reference point for the development of analytical formalisms describing diffusion kinetics.

The pure 6JC mechanism enables tracer diffusion to occur in stoichiometric highly ordered structures. By itself it does not, however, allow for the participation of existing antistructural atoms and therefore does not provide for the development of order, that is ordering kinetics and compositional changes. Similarly, with the pure 6JC mechanism, tracer diffusion at non-stoichiometric compositions does not allow for the participation of the antistructural atoms produced by non-stoichiome- try. In effect, tracer diffusion would not then depend on composition, contrary to what is commonly seen experimentally. Another difficulty is the means for switching between the two types of cycle, that is a 6JC with the vacancy starting and finishing on the $\alpha$ sublattice ($\alpha$-6JC) and a 6JC with the vacancy starting and finishing on the $\beta$ sublattice ($\beta$-6JC). The $\alpha$ sublattice is the 'home' lattice of the A atoms and the $\beta$ sublattice is the 'home' lattice of the B atoms. Long overdue is an extension of the basic 6JC concept that allows a description of the above phenomena. The present paper is a first attempt in this direction$\dagger$. We derive expressions for the tracer correlation factors and tracer diffusivities based on a straightforward extension of the basic 6JC idea to non-stoichiometric compositions. We verify the derived expres- sions by computer simulation of the Ising alloy model. We make use of an analogue of the well-known five-frequency model for impurity diffusion via vacancy jumps (Lidiard 1955, Le Claire and Lidiard 1956). There have been several applications of the five-frequency model and analogous models in intermetallic compounds. The present authors developed a formalism to describe impurity diffusion via inter- sublattice jumps in the B2 structure (Belova and Murch 1997, 1999). Other applica- tions in intermetallics have been confined to describing intrasublattice jumps (in much the same way as oxides and alkali halides) in particular, for the antistructural minority element in nickel-based intermetallics taking the $L1_2$ structure (Koiwa et al. 1997, Numakura et al. 1998). These latter calculations have been generalized to impurity diffusion in the same structure by Belova and Murch (1998a). The asymp- totic (zero temperature) analysis undertaken in the present paper is quite different from those above in that the 6JC is taken as the basic diffusion mechanism unit itself.

## §2. THEORY

We consider the two possible 6JCs, namely $\alpha$-6JC and $\beta$-6JC for a vacancy starting on an $\alpha$ site or a $\beta$ site respectively. The $\alpha$-6JC is shown purely schematically for a two-dimensional (2D) lattice in figure 1. At the stoichiometric composition AB the $\alpha$-6JCs provide for tracer displacement of A and B atoms; after the 6JC the vacancy will have exchanged with the A atom and the two B atoms will have exchanged places (see figure 1). Analogously, the $\beta$-6JC provides for tracer displace- ment of A and B atoms; after the 6JC the vacancy will have exchanged with the B atom and the two A atoms will have exchanged places.

We wish to extend the 6JC concept to non-stoichiometric compositions. We need only to consider the case when $c_A = 0.5 - \delta$, that is there is an excess of B atoms. The behaviour of excess-A compositions is found by interchanging A and B. We assume

$\dagger$ A preliminary account of an attack on this problem was presented by Belova and Murch (2000d).

![](./images/811981912695373826_2.jpg)

Figure 1. Schematic 6JC (for simplicity shown for the 2D lattice) for a vacancy starting on an $\alpha$ site.

that $\delta$ is sufficiently small that diffusion can only occur by (general) 6JCs at the low-temperature limit. At this limit the $\beta$-6JC has a minor role compared with the $\alpha$-6JC. The reason for this is that, for B-rich compositions in alloys exhibiting antistructural disorder, the vacancy concentration is much lower on the $\beta$ sublattice than on the $\alpha$ sublattice (Kikuchi and Sato 1969, 1972, Bakker 1979, Belova and Murch 1996). Accordingly, the tracer displacement of A atoms on the $\alpha$ sublattice only and B atoms on the $\beta$ and the $\alpha$ sublattice are mainly due to the $\alpha$-6JC.

Let us describe the Ising alloy model that will be used to illustrate the formalism. $E_{\text{AA}}$, $E_{\text{BB}}$ and $E_{\text{AB}}$ are the pair interaction energies between AA, BB and AB pairs respectively. For convenience, we write $\Delta_{\text{A}} = E_{\text{AA}} - E_{\text{AB}}$ and $\Delta_{\text{B}} = E_{\text{BB}} - E_{\text{AB}}$ and the alloy ordering energy $E$ is given by $E = E_{\text{AA}} + E_{\text{BB}} - 2E_{\text{AB}}$. The vacancy availabilities are defined as the probability of a vacancy occurring next to an A (or B) atom. The notation is, for example, $p_{\text{Av}}^{\alpha\beta}$; this is the probability that a vacancy v on the $\beta$ sublattice occurs next to an A atom on the $\alpha$ sublattice. The other vacancy availabilities are defined by analogy. If we assume that, firstly, perfect order is perturbed by the occasional antistructural B atom, secondly, such atoms are randomly distributed, thirdly, they are at a much higher concentration than the fraction of vacant sites, then we easily find that in the Bragg-Williams approximation

$$
p_{\text{Av}}^{\alpha\beta} = c_{\text{v}}^{\beta} \exp\left[\beta\left(-2\delta\Delta_{\text{B}}\right)\right], \tag{1}
$$

$$
p_{\text{Av}}^{\beta\alpha} = c_{\text{v}}^{\alpha} \exp\left[\beta\left(\Delta_{\text{A}} - 2\delta E\right)\right], \tag{2}
$$

$$
p_{\text{Bv}}^{\alpha\beta} = c_{\text{v}}^{\beta} \exp\left[\beta\left(\Delta_{\text{B}} - 16\delta\Delta_{\text{B}}\right)\right], \tag{3}
$$

$$
p_{\text{Bv}}^{\beta\alpha} = c_{\text{v}}^{\alpha}, \tag{4}
$$

where $c_{\text{v}}^{\alpha}$ and $c_{\text{v}}^{\beta}$ are the average site fractions of the vacancies on the $\alpha$ and $\beta$ sublattices respectively and $\beta = 1/kT$. These quantities are related by

$$
c_{\text{v}}^{\alpha} = 2\delta c_{\text{v}}^{\beta} \exp\left[\beta\left(8\Delta_{\text{B}} - 16\delta\Delta_{\text{B}}\right)\right]. \tag{5}
$$

Equation (5) was obtained by making use of the equilibrium conditions together with equations (1)-(4). It is worth noting that a similar relation for the stoichiometric composition exists:

$$c_{\mathrm{v}}^{\alpha(0.5)}=c_{\mathrm{v}}^{\beta(0.5)} \exp \left\{\beta\left[4\left(\Delta_{\mathrm{B}}-\Delta_{\mathrm{A}}\right)\right]\right\}.$$

The vacancy availabilities are related by
$$p_{\mathrm{Av}}^{\alpha \beta}=\frac{\exp \left[\beta\left(-8 \Delta_{\mathrm{B}}+14 \delta \Delta_{\mathrm{B}}\right)\right]}{2 \delta} p_{\mathrm{Bv}}^{\beta \alpha}.\qquad(6)$$

The effective jump frequencies $\nu^{\alpha}$ for the $\alpha-6 JC$ and $\nu^{\beta}$ for the $\beta-6 JC$ have been expressed using a mean first passage time concept (Arita et al. 1989). Although this is not strictly rigorous, nonetheless it seems to be a very good approximation (Drautz et al. 1999). Then the probabilities for the $\alpha-6 JC$ and $\beta-6 JC$ can be readily expressed in terms of the well-known 'bond-breaking' formalism of Kikuchi and Sato (1969,1972) and the above expressions for the vacancy availabilities. We then find for the effective jump frequencies that
$$\nu^{\alpha-6 J C}=48 \nu \exp \left\{\beta\left[\Delta-6 E+2 \delta\left(6 E+7 \Delta_{\mathrm{B}}\right)\right]\right\},\qquad(7)$$

$$\nu^{\beta-6 J C}=48 \nu \exp \left\{\beta\left[-6 E+2 \delta\left(6 E+7 \Delta_{\mathrm{B}}\right)\right]\right\},\qquad(8)$$
where $\Delta=U_{B}-U_{A}$ and $U_{A}$ and $U_{B}$ are the (hypothetical) migration energies in the absence of interactions and $\nu$ is the attempt frequency (assumed to be the same for both atom species).

The diffusion coefficient of either A or B is a sum of the diffusion coefficients from both types of 6JC, that is
$$D_{\mathrm{A}^{*}}^{6 J C}=D_{\mathrm{A}^{*}}^{\alpha-6 J C}+D_{\mathrm{A}^{*}}^{\beta-6 J C},\qquad(9)$$

$$D_{\mathrm{B}^{*}}^{6 J C}=D_{\mathrm{B}^{*}}^{\alpha-6 J C}+D_{\mathrm{B}^{*}}^{\beta-6 J C},\qquad(10)$$
where the cross-correlation, meaning the correlation in directions for an atom chan- ging between the $\alpha$ and $\beta$ cycles, is assumed to be negligible. This is permissible when the temperature approaches zero, see also Belova and Murch (2000a). Since the overall contribution from the $\beta-6 JC$ is much smaller than from the $\alpha-6 JC$ because the vacancy concentration is lower on the $\beta$ sublattice than on the $\alpha$ sublattice for B rich compositions, we can simply use the general expressions in the Ising alloy context for the contributions from the $\beta$ -6JCs (Arita et al. 1989) to obtain
$$D_{\mathrm{A}^{*}}^{\beta-6 J C}=2 f_{\mathrm{A}}^{\beta-6 J C} a^{2} \frac{5 c_{\mathrm{A}}^{\alpha} \nu^{\beta-6 J C} c_{\mathrm{v}}^{\beta}}{24},\qquad(11)$$

$$D_{\mathrm{B}^{*}}^{\beta-6 J C}=f_{\mathrm{B}}^{\beta-6 J C} a^{2} \frac{5 c_{\mathrm{A}}^{\alpha} \nu^{\beta-6 J C} c_{\mathrm{v}}^{\beta}}{24},\qquad(12)$$
where a is the jump distance, $c_{A}^{\alpha}$ is the site fraction of A atoms on the $\alpha$ sublattice, $f_{A}^{\beta-6 J C}=0.8$ and $f_{B}^{\beta-6 J C}=0.8$ (for the Ising model in the B2 structure) and with our expressions above for $\nu^{\beta-6 J C}$ and $p_{Av}^{\alpha \beta}$ . It is seen that for diffusion via the $\beta-6 JC$ the diffusion coefficient for A atoms is simply twice that for the B atoms.

Now let us deal with the $\alpha-6 JC$ . The contribution of the $\alpha-6 JC$ to tracer diffusion centres on the problem of calculating the tracer correlation factors with the direct and indirect participation of antistructural B atoms. Let us deal first with the B correlation factor. In the zero temperature limit there are $2 \delta$ antistructural B atoms on the $\alpha$ sublattice. Let us assume that these are randomly distributed. Therefore, there are $(18 ×2 \delta)$ connected $\alpha$ sites around every such antistructural B atom where the situation differs from the case of an isolated $\alpha-6 JC$ . The problem can

now be reformulated by making use of an analogue of the five-frequency model (Lidiard 1955, Le Claire and Lidiard 1956). Instead of the vacancy being the basic diffusion mechanism unit, here the $\alpha$-6JC is taken as the basic diffusion mechanism unit. We shall adopt the standard five-frequency notation. First, the frequency of the basic isolated $\alpha$-6JC is $w_0 = \nu^{\alpha\text{-6JC}}/48$. Next, the 6JCs which take the vacancy away from a particular antistructural B atom (equivalent to the dissociative or $w_3$ jump) can be reversed (equivalent to the associative or $w_4$ jump) via exactly the same set of local configurations. This means that in the Ising alloy model there is no effective binding between the $\alpha$-6JC vacancy and the antistructural B atom. Next, the $\alpha$-6JC which involves the antistructural B atom itself is the '$w_2$ jump' of the five-frequency model. This special cycle consists of a vacancy and three B atoms (in figure 1 replace the A atom by an antistructural B atom). By its nature it is obvious that the frequency for this $\alpha$-6JC is very much higher than the others. It is also clear that the '$w_2$ jump' is not actually a 'complete' 6JC because after the first two jumps ($V^\alpha \rightarrow B^\beta \rightarrow B^\alpha$ in this case) the resulting configuration has the same energy as the initial configuration and the net displacement of B atoms is non-zero. This is important for the detailed analysis of the tracer diffusivity of B atoms. Accordingly, for convenience we consider the '$w_2$ jump' of B atoms as two such consecutive elementary jumps with the $1/2a$ length in the $x$ direction. We need not concern ourselves with expressing this '$w_2$ jump' in terms of the interactions; it will not feature explicitly in our final expressions for the diffusivities because of its very large value compared with the other frequencies. This is completely analogous to the situation for the five-frequency model for impurity diffusion; when the frequency $w_2$ is very large, its effect on the impurity diffusion is negligible.

Finally, the $w_1$-type or rotational jump in the five-frequency model is represented by a set of 6JCs which can occur around the antistructural B atom but without directly involving the B atom except via its energy of interaction (see also Athènes *et al.* (1997)). The rotational $w_1$ jump actually takes four possible values depending on the proximity of the antistructural B atom with respect to the 6JC:

$$
\begin{aligned}
w_{1}^{1} & =\nu \exp \left\{\beta\left[\Delta-6 E+\Delta_{\mathrm{B}}+2 \delta\left(6 E+6 \Delta_{\mathrm{B}}\right)\right]\right\}, \\
w_{1}^{2} & =\nu \exp \left\{\beta\left[\Delta-5 E+2 \delta\left(5 E+7 \Delta_{\mathrm{B}}\right)\right]\right\}, \\
w_{1}^{3} & =\nu \exp \left\{\beta\left[\Delta-5 E+\Delta_{B}+2 \delta\left(5 E+6 \Delta_{\mathrm{B}}\right)\right]\right\}, \\
w_{1}^{4} & =w_{0}.
\end{aligned} \tag{13}
$$

We note that, in the zero temperature limit, $w_1^3$ is the highest and $w_1^1$ and $w_1^2$ always appear as a sum $w_1^1 + w_1^2$ in the analysis.

Before proceeding further, we can roughly summarize the present situation in the usual five-frequency parlance as

$$
w_{2} \gg w_{1}^{3}>\frac{\left(w_{1}^{2}+w_{1}^{1}\right)}{2}>w_{1}^{4}=w_{0}=w_{3}=w_{4}. \tag{14}
$$

Physically, the situation is that there is no binding of the $\alpha$-6JC vacancy to the antistructural B atom. The vacancy moves relatively slowly through the lattice, largely by isolated $\alpha$-6JCs ($w_0$). When the vacancy is close to an antistructural B atom, the vacancy is engaged in either the faster rotational $\alpha$-6JCs ($w_1$) around the antistructural atom or the even faster $\alpha$-6JCs ($w_2$) involving the antistructural atom itself.

The diffusion process via the $\alpha$-6JC can be formally split into two parts. The first (region 1) refers to the domain where an atom moves in the region around a B antistructural atom (i.e. the five-frequency model region, see the sites numbered 1 in figure 2). The second (region 2) refers to the domain where the atom can move in the rest of the structure. We assume that cross-correlation between atom displacements resulting from these two parts is negligible.

Consider now the tracer correlation effects for the B atoms. In this analysis we consider diffusion in the $x$ direction. When a B atom is involved in movements in the five-frequency model region, there are 11 different types of jump in the sense that they are described by Howard (1966). (We have to emphasize that the geometry of the present model is different from the fcc structure (see figure 2).) There are four '$w_2$ jump' types for a B atom to jump into a vacant antistructural $\alpha$ site and four '$w_2$ jump' types for the B atom to jump from the antistructural $\alpha$ site into the neighbouring $\beta$ site. There are also another three different '$w_1$ jumps' of a B atom between $\beta$-sites (with an $x$ component equal to $a$). We introduce $t_{\text{B}}^{ij}$ as the net probability that, after a first jump of type $i$, the second jump is of type $j$ with the same direction along the $x$ axis.

If the first B atom jump is one of the first four types, then we can determine $t_{\text{B}}^{ij}$, $i=1,2,3,4$, by directly using the procedure described by Le Claire and Lidiard (1956). This gives

$$
\begin{align}
t_{\text{B}}^{15} &= -1 + \frac{2w_1^3 + 2(w_1^2 + w_1^1)}{w_2 + 3w_1^3 + 4.5(w_1^2 + w_1^1)}, \\
t_{\text{B}}^{16} &= -\frac{w_1^3 + 2(w_1^2 + w_1^1)}{w_2 + 3w_1^3 + 4.5(w_1^2 + w_1^1)},
\end{align} \tag{15}
$$

![](./images/811981912695373826_3.jpg)

Figure 2. The region immediately around an antistructural B atom. Only $\alpha$ sites are shown and are numbered 1 if they can be involved in $w_2$- or $w_1$-type jumps.

$$
t_{\mathrm{B}}^{26}=-1+\frac{w_{1}^{3}+2.5\left(w_{1}^{2}+w_{1}^{1}\right)}{w_{2}+3 w_{1}^{3}+4.5\left(w_{1}^{2}+w_{1}^{1}\right)},
$$

$$
t_{\mathrm{B}}^{25}=-\frac{w_{1}^{3}+2\left(w_{1}^{2}+w_{1}^{1}\right)}{2 w_{2}+6 w_{1}^{3}+9\left(w_{1}^{2}+w_{1}^{1}\right)}.
$$
(16)

The other $t_{\mathrm{B}}^{i j}, i=1,2,3,4$, are all zero.

Consider now the ' $w_{2}$ jump' of a B atom from the antistructural $\alpha$-site position to a neighbouring $\beta$ site, that is the second jump in the sequence and can be of four types. All such jumps will have a non-zero $x$ component. It is straightforward to calculate the corresponding $t_{\mathrm{B}}^{i j}, i=5,6,7,8$, by making a direct inspection of the probabilities for a vacancy to reverse the first jump. The major contribution will come from the ' $w_{2}$ jump' of the particular B atom to an $\alpha$ site and of the other B atom from the $\alpha$ site (where it was an antistructural atom) to a $\beta$ site. After detailed consideration of this we have that

$$
t_{\mathrm{B}}^{51}=-\frac{w_{2}}{7 w_{2}+8 w_{1}^{3}+8\left(w_{1}^{2}+w_{1}^{1}\right)},
$$

$$
t_{\mathrm{B}}^{62}=-\frac{w_{2}}{3 w_{2}+2 w_{1}^{3}+6\left(w_{1}^{2}+w_{1}^{1}\right)},
$$
(17)

$$
t_{\mathrm{B}}^{73}=-\frac{w_{2}}{w_{2}+8 w_{1}^{3}+8\left(w_{1}^{2}+w_{1}^{1}\right)},
$$

$$
t_{\mathrm{B}}^{84}=-\frac{w_{2}}{w_{2}+2 w_{1}^{3}+6\left(w_{1}^{2}+w_{1}^{1}\right)},
$$
(18)

$$
t_{\mathrm{B}}^{79}=t_{\mathrm{B}}^{711}=-\frac{w_{1}}{w_{2}+8 w_{1}^{3}+8\left(w_{1}^{2}+w_{1}^{1}\right)},
$$

$$
t_{\mathrm{B}}^{810}=-\frac{2 w_{1}}{w_{2}+2 w_{1}^{3}+6\left(w_{1}^{2}+w_{1}^{1}\right)}.
$$
(19)

The other $t_{\mathrm{B}}^{i j}, i=5,6,7,8$, are all zero.

The other $t_{\mathrm{B}}^{i j}, i=9,10,11$, can be found in a similar way. The final relations are

$$
t_{\mathrm{B}}^{93}=t_{\mathrm{B}}^{103}=-\frac{w_{2}}{w_{2}+8 w_{1}^{3}+8\left(w_{1}^{2}+w_{1}^{1}\right)},
$$

$$
t_{\mathrm{B}}^{99}=t_{\mathrm{B}}^{911}=t_{\mathrm{B}}^{109}=t_{\mathrm{B}}^{1011}=-\frac{w_{1}}{3 w_{2}+2 w_{1}^{3}+6\left(w_{1}^{2}+w_{1}^{1}\right)},
$$
(20)

$$
t_{\mathrm{B}}^{114}=-\frac{w_{2}}{w_{2}+2 w_{1}^{3}+6\left(w_{1}^{2}+w_{1}^{1}\right)},
$$

$$
t_{\mathrm{B}}^{1110}=-\frac{2 w_{1}}{w_{2}+2 w_{1}^{3}+6\left(w_{1}^{2}+w_{1}^{1}\right)}
$$
(21)

The other $t_{\mathrm{B}}^{i j}, i=9,10,11$, are all zero.

We can now use the general expression for the correlation factor (Howard 1966)

$$
f_{x}=1+2 \mathbf{b} \cdot \mathbf{T} \cdot(\mathbf{I}-\mathbf{T})^{-1} \cdot \mathbf{d},
$$
(22)
where $\mathbf{b}=\left\{b_{i}\right\}$ is the vector of the fractions $b_{i}=n_{x}^{i} r_{x}^{i} / \sum_{j}\left[n_{x}^{j}\left(r_{x}^{j}\right)^{2}\right]$, where $n_{x}^{i}$ is the number of jumps of type $i$ with non-zero $x$ component and $r_{x}^{i}$ is the $x$ component of the $i$ th jump vector, and is given by

$$
\begin{aligned}
\mathbf{b}=\left\{\frac{4 w_{2}}{g}, \frac{8 w_{2}}{g}, \frac{8 w_{2}}{g}, \frac{4 w_{2}}{g}, \frac{4 w_{2}}{g}, \frac{8 w_{2}}{g}, \frac{8 w_{2}}{g}, \frac{4 w_{2}}{g},\right. & \frac{8 w_{1}^{3}+4\left(w_{1}^{1}+w_{1}^{2}\right)}{g}, \\
& \left.\frac{8 w_{1}^{3}+4\left(w_{1}^{1}+w_{1}^{2}\right)}{g}, \frac{8 w_{1}^{3}+4\left(w_{1}^{1}+w_{1}^{3}\right)}{g}\right\},
\end{aligned}
$$
with $g=24 w_{2}+24 w_{1}^{3}+12 w_{1}^{1}+12 w_{1}^{2} ; \mathbf{d}=\left\{d_{i}\right\}, d_{i}=r_{x}^{i}$, and is given by
$$
\mathbf{d}=\left\{\frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, \frac{1}{2}, 1,1,1,\right\}.
$$

$\mathbf{T}$ is the matrix and is given by $\mathbf{T}=\left\{t_{\mathrm{B}}^{i j}\right\}, i, j=1,2, \ldots, 11$ with the non-zero components all being listed above.

Using the symbolic algebra software (Mathematica) we calculate the B-atom correlation factor from equation (22). The result in the low temperature limit is
$$
f_{\mathrm{B}}^{\alpha-6 \mathrm{JC}, 1}=\frac{7 w_{1}^{3}+12.5\left(w_{1}^{1}+w_{1}^{2}\right)}{3 w_{1}^{3}+3 w_{2}+1.5\left(w_{1}^{1}+w_{1}^{2}\right)}.\qquad(23)
$$

The $\alpha$-6JC events which are in region 2 contribute to the total number of B-atom jumps (with non-zero $x$ component) $[48-48(2 \delta)-144(2 \delta)-$ $168(2 \delta)] / 48 w_{0} c_{\mathrm{v}}^{\alpha}\left(20 a^{2} / 2\right)$ which gives $10(1-15 \delta) a^{2} w_{0} c_{\mathrm{v}}^{\alpha}$. We approximate the correlation factor for this region by 0.8 (this corresponds to the case when region 2 contains all sites and the correlation factor $f_{\mathrm{B}}^{\alpha-6 \mathrm{JC}}(=f_{\mathrm{A}}^{\beta-6 \mathrm{JC}})$). Now we can combine this with equations (10), (12) and (23) with the corresponding number of jumps to obtain the total tracer diffusivity of the B atoms as
$$
\begin{aligned}
D_{\mathrm{B}^{*}}= & \left(4\left[14 w_{1}^{3}+25\left(w_{1}^{1}+w_{1}^{2}\right)\right] \delta+16(1-15 \delta) w_{0}\right. \\
& \left.+\frac{4(1-15 \delta) w_{0} \exp \left[\beta\left(-8 \Delta_{\mathrm{B}}+16 \delta \Delta_{\mathrm{B}}\right)\right]}{\delta}\right) \\
& \times \frac{a^{2} c_{\mathrm{v}}^{\alpha} \exp \left(7 E_{\mathrm{AB}} \beta\right)}{1+2 \delta}
\end{aligned}\qquad(24)
$$
and therefore the tracer correlation factor of the B atoms is
$$
\begin{aligned}
f_{\mathrm{B}}= & 2\left[14 w_{1}^{3}+25\left(w_{1}^{1}+w_{1}^{2}\right)\right] \delta+8(1-15 \delta) w_{0} \\
& +\frac{2(1-15 \delta) w_{0} \exp \left[\beta\left(-8 \Delta_{\mathrm{B}}+16 \delta \Delta_{\mathrm{B}}\right)\right]}{\delta}.
\end{aligned}\qquad(25)
$$

We can summarize the physical situation as follows. A given B atom diffuses partly by pure $\alpha$-6JCs $\left(w_{0}\right)$ in region 2 but this is a small contribution to the total B diffusivity. The major contribution comes from region 1 where enhanced diffusion takes place by both direct antistructural B-atom-assisted 6JCs $\left(w_{2}\right)$ and indirect antistructural B-atom-assisted 6JCs $\left(w_{1}\right)$. As mentioned above, the (very large) $w_{2}$ frequency does not enter into the expression for the diffusivity of the B atoms (equation (24)).

Calculation of the A-atom diffusion coefficient and tracer correlation factor can be performed in a similar way as for the B atoms. First, for the ' $w_{1}$ jumps' (with non-zero $x$ component) we see that there are six different types of jump. Keeping the highest contribution in a similar way as was done for the B-atom calculations above, we find that the non-zero components of the $\mathbf{T}$ matrix for the A atoms are

$$
t_{\mathrm{A}}^{13}=t_{\mathrm{A}}^{31}=t_{\mathrm{A}}^{32}=t_{\mathrm{A}}^{41}=-\frac{w_{1}^{3}}{16 w_{1}^{3}+16\left(w_{1}^{1}+w_{1}^{2}\right)},
$$

$$
\begin{aligned}
& t_{\mathrm{A}}^{24}=-\frac{w_{1}^{3}+2\left(w_{1}^{1}+w_{1}^{2}\right)}{4 w_{1}^{3}+12\left(w_{1}^{1}+w_{1}^{2}\right)}, \\
& t_{\mathrm{A}}^{42}=-\frac{w_{1}^{3}+2\left(w_{1}^{1}+w_{1}^{2}\right)}{16 w_{1}^{3}+16\left(w_{1}^{1}+w_{1}^{2}\right)},
\end{aligned}
\tag{26}
$$

$$
t_{\mathrm{A}}^{56}=-\frac{w_{1}^{3}}{2 w_{1}^{3}+6\left(w_{1}^{1}+w_{1}^{2}\right)},
$$

$$
t_{\mathrm{A}}^{65}=-\frac{w_{1}^{3}}{4 w_{1}^{3}+12\left(w_{1}^{1}+w_{1}^{2}\right)}.
\tag{27}
$$

The vectors $\mathbf{d}$ and $\mathbf{b}$ are
$$
\mathbf{d}=\{1,1,1,1,1,1\},
$$

$$
\mathbf{b}=\left\{\frac{w_{1}^{3}}{q}, \frac{w_{1}^{3}+2\left(w_{1}^{1}+w_{1}^{2}\right)}{q}, \frac{w_{1}^{3}}{q}, \frac{w_{1}^{3}+2\left(w_{1}^{1}+w_{1}^{2}\right)}{q}, \frac{w_{1}^{1}+w_{1}^{2}}{q}, \frac{w_{1}^{1}+w_{1}^{2}}{q}\right\},
$$

where $q=4 w_{1}^{3}+6\left(w_{1}^{1}+w_{1}^{2}\right)$. Making use of the general expression equation (22) again we find that $0.893 \geqslant f_{\mathrm{A}}^{\alpha, 1} \geqslant 0.753$. We shall use the value 0.753 which corresponds to the case when $w_{1}^{3} \gg w_{1}^{1}+w_{1}^{2}$.

The final expression for the A atom tracer diffusion coefficient (equations (9) and (11) together with the sum of the diffusivities in regions 1 and 2) is

$$
\begin{aligned}
D_{\mathrm{A}^{*}}= & \left(24.1 \delta\left[w_{1}^{3}+1.5\left(w_{1}^{1}+w_{1}^{2}\right)\right] \delta+8(1-15 \delta) w_{0}\right. \\
& \left.+\frac{8(1-15 \delta) w_{0} \exp \left[\beta\left(-8 \Delta_{\mathrm{B}}+16 \delta \Delta_{\mathrm{B}}\right)\right]}{\delta}\right) \\
& \times \frac{a^{2} c_{\mathrm{v}}^{\alpha} \exp \left(7 E_{\mathrm{AB}} \beta\right)}{1-2 \delta}
\end{aligned}
\tag{28}
$$

and therefore the tracer correlation factor is

$$
\begin{aligned}
f_{\mathrm{A}}= & \frac{24.1 \delta^{2}}{1-2 \delta}\left[w_{1}^{3}+1.5\left(w_{1}^{1}+w_{1}^{2}\right)\right] \exp \left[\beta\left(8 \Delta_{\mathrm{B}}-14 \delta \Delta_{\mathrm{B}}\right)\right] \\
& +\frac{8(1-15 \delta) w_{0}}{1-2 \delta}\left\{\delta \exp \left[\beta\left(8 \Delta_{\mathrm{B}}-14 \delta \Delta_{\mathrm{B}}\right)\right]+\exp \left(\beta 2 \delta \Delta_{\mathrm{B}}\right)\right\}.
\end{aligned}
\tag{29}
$$

Physically, the A atoms also diffuse by pure $\alpha-6 \mathrm{JCs}\left(w_{0}\right)$ in region 2 but this also is a small contribution to their diffusivity. The major contribution comes from region 1 where enhanced diffusion takes place by indirect antistructural B-atom-assisted $6 \mathrm{JCs}\left(w_{1}\right)$.

Using exactly the same procedure as described by Belova and Murch (2000b) we also performed Monte Carlo computer simulations to calculate the tracer correlation factors at three deviations from stoichiometry, $\delta=0, \delta=0.02$ and $\delta=0.04$, and to very low temperatures.

### §3. RESULTS AND DISCUSSION

In figure 3, we present analytical and Monte Carlo results for the tracer correlation factors $f_{\mathrm{A}}$ and $f_{\mathrm{B}}$ for the concentration $c_{\mathrm{A}}=0.48$, that is $\delta=0.02$ for three values of the asymmetry parameter $U\left(=\left(E_{\mathrm{AA}}-E_{\mathrm{BB}}\right) / E\right): 0,0.125$ and $-0.125$. It can be seen that the convergence of the simulated tracer correlation factors at low temperatures to the derived asymptotic limits is very good. In the same figure we have included the behaviour for $f_{\mathrm{A}}$ and $f_{\mathrm{B}}$ for the case where a deviation from

![](./images/811981912695373826_4.jpg)

Figure 3. The dependences of the tracer correlation factors $f_{\mathrm{A}}$ and $f_{\mathrm{B}}$ on $E / k T$ at $\delta=0.02$ for (a) $U=0.0$, (b) $U=0.125$ and (c) $U=-0.125:(\bigcirc),(\square)$, Monte Carlo simulation results; (——), equation (29) $(f_{\mathrm{A}})$ and equation (25) $(f_{\mathrm{B}})$; (- - -), analytical results for the stoichiometric composition by way of application of the expressions from Arita et al. (1989) to the Ising model.

![](./images/811981912695373826_5.jpg)

Figure 3. (Continued)

stoichiometry is ignored and diffusion is carried entirely by the basic 6JCs (just as at the stoichiometric composition). This gives very poor agreement with the simulation results, thereby indicating the necessity of including antistructural-atom-assisted 6JCs.

In figure 4, we present analogous results for $c_{\mathrm{A}}=0.46$, that is $\delta=0.04$. The agreement remains very good although slightly less so than for $\delta=0.02$. This is

![](./images/811981912695373826_6.jpg)

Figure 4. The dependences of the tracer correlation factors $f_{\mathrm{A}}$ and $f_{\mathrm{B}}$ on $E / k T$ at $\delta=0.04$ for (a) $U=0.0$, (b) $U=0.125$, (c) $U=-0.125$: $(\bigcirc),(\square)$, Monte Carlo simulation results; (-----), equation (29) $(f_{\mathrm{A}})$ and equation (25) $(f_{\mathrm{B}})$.

![](./images/811981912695373826_7.jpg)

understandable because at $\delta = 0.04$ the condition of the very dilute limit has probably been violated. Although the deviation $\delta$ from stoichiometry (and hence the local environment) is included in the expressions for the frequencies, it is not included explicitly in the calculation of the correlation effects arising from interference of antistructural atoms. In other words, the influence of one antistructural atom on the diffusion behaviour of the others is not taken into account; each antistructural atom is assumed to be isolated, that is they are assumed to diffuse independently as at the very dilute limit. It is known too that at higher deviations from stoichiometry $(\delta \geqslant 0.065)$ the antistructural atoms are then sufficiently well connected that it is possible for atoms (B in this case) to percolate through the lattice via the antistructural bridge mechanism (Kao and Chang 1993, Belova and Murch 1998b).

In order to appreciate better the role of non-stoichiometry in figure 5, we present analytical and Monte Carlo results for $D_{\mathrm{A}^{*}}$ and $D_{\mathrm{B}^{*}}$ as a function of $c_{\mathrm{A}}$ for the low temperature $E / k T=1.6$. The tracer diffusivities have been scaled to the stoichiometric diffusivities where diffusion takes place by pure 6JCs only. Good agreement between simulation results and the asymptotic analysis is evident.

![](./images/811981912695373826_8.jpg)

Figure 5. The dependence of the tracer diffusion coefficients $D_{\mathrm{A}^{*}}$ and $D_{\mathrm{B}^{*}}$ (scaled to those at the stoichiometric composition) as a function of $c_{\mathrm{A}}$ at $E / k T=1.6$ for (a) $U=0.0$, (b) $U=0.125$, (c) $U=-0.125:(\bullet),(\nabla)$, Monte Carlo simulation results; (——), equation (28) $(D_{\mathrm{A}^{*}})$ and equation (24) $(D_{\mathrm{B}^{*}})$ with stoichiometric $D$ values by way of application of the expressions from Arita et al. (1989) to the Ising model.

![](./images/811981912695373826_9.jpg)

Figure 5. (Continued)

### §4. CONCLUSIONS
In this paper we have been able to show that the five-frequency model provides a useful framework for the purposes of formulating a theory of tracer diffusion by only 6JCs and (direct and indirect) antistructural-atom-assisted 6JCs in non-stoichio- metric B2 intermetallics. We were able to derive explicit asymptotic ($T \to 0$) expres- sions for the tracer diffusivities for both atomic components in the context of the Ising alloy model. Monte Carlo simulation results showed very good agreement with the expressions derived.

### ACKNOWLEDGEMENTS
We wish to thank Professor A. D. Le Claire (Oxford Research Unit, The Open University) and Professor A. B. Lidiard (University of Reading) for useful discussions. We also wish to thank the Australian Research Council (Large Grants Scheme) for its support of this research. One of us (I.V.B.) also wishes to thank the Australian Research Council for the award of a Queen Elizabeth II Fellowship.

### REFERENCES
ARITA, M., KOIWA, M., and ISHIOKA, S., 1989, Acta metall., 37, 1363.
ATHÈNES, M., BELLON, P., and MARTIN, G., 1997, Phil. Mag. A, 76, 965.
BAKKER, H., 1979, Phil. Mag. A, 40, 525.
BELOVA, I. V., IVORY, M. E., and MURCH, G. E., 1995, Phil. Mag. A, 72, 871.
BELOVA, I. V., and MURCH, G. E., 1996, Phil. Mag. A, 73, 117; 1997, Ber. Bunsenges phys. Chem., 101, 1325; 1998a, Mater. Res. Soc. Symp. Proc., 527, 159; 1998b, Intermetallics, 6, 115; 1999, Metall. Nov. Tekhn., 21, 41; 2000a, Phil. Mag. A, 80, 1481; 2000b, J. Phys. Chem. Solids, 61, 1755; 2000c, Phil. Mag. A, 80, 2073; 2000d, Defect Diffusion Forum, 194-199, 411.
DRAUTZ, R., MEYER, B. AND FÄHNLE, M., 1999, Acta Mater., 47, 2437.
ELCOCK, E. W., and MCCOMBIE, C. W., 1958, Phys. Rev., 109, 605.

HOWARD, R. E., 1966, *Phys. Rev.*, **144**, 650.

KAO, C. R., and CHANG, Y. A., 1993, *Intermetallics*, **1**, 237.

KIKUCHI, R., and SATO, H., 1969, *J. Chem. Phys.*, **51**, 161; 1972, *ibid*, **57**, 4962.

KOIWA, M., NUMAKURA, H., and ISHIOKA, S., 1997, *Defect Diffusion Forum*, **143-147**, 209.

LE CLAIRE, A. D., and LIDIARD, A. B., 1956, *Phil. Mag.*, **47**, 518.

LIDIARD, A. B., 1955, *Phil. Mag.*, **46**, 1218.

NUMAKURA, H, IKEDA, T., KOIWA, M., and ALMAZOUZI, A., 1998, *Phil. Mag. A*, **77**, 887.