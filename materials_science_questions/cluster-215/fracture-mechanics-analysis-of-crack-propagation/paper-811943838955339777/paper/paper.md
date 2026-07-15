# CRACK CLOSURE: A CONCEPT OF FATIGUE CRACK GROWTH UNDER EXAMINATION

F. O. RIEMELMOSER and R. PIPPAN

Erich-Schmid-Institut of solid state physics of the Austrian Academy of Science, A-8700 Leoben, Austria

Abstract—In recent literature it is asserted that the concept of crack closure in fatigue fracture mechanics is not capable of explaining fatigue crack growth behaviour. The reasons given are that both asperity induced crack closure and plasticity induced crack closure should be either negligible or non-existent. We have re-considered these hypotheses since their correctness would completely change the established picture of fatigue crack growth. In order to get mathematically tractable systems the present studies are confined to long cracks loaded in mode I. The results suggest that in case of asperity induced crack closure the proposed hypothesis is only true in special cases and the demonstration of the non-existence of plasticity induced crack closure is proved to be wrong.

Keywords—Mode I fatigue cracks; Asperity-induced crack closure; Plasticity-induced crack closure.

## INTRODUCTION

Since the discovery by Elber [1] of premature crack face contact in the unloading sequence, many investigations, both experimental and analytical, were carried out to clarify the phenomenon of crack closure. Most researches concluded that crack closure does influence the crack growth rate significantly. They state that a fatigue crack advances in that portion of the applied stress intensity factor $K_{global}$ in which the crack is fully open. However, recently counter statements have been given [2–8]. In these publications the following hypotheses are made:

(1) The compliance technique for measuring asperity-induced crack closure predicts too large closure stress intensity factors.
(2) Plasticity that originates from crack tip deformation cannot contribute to it's closure.

Since the correctness of these hypotheses would lead to a picture of fatigue crack growth which is in contrast to established theory they should be examined carefully. In this paper the concept of both asperity induced and plasticity induced crack closure is reconsidered. Asperity induced crack closure is dealt with separately while the concept of plasticity induced crack closure is re-examind later in the text.

## ASPERITY-INDUCED CRACK CLOSURE

Due to the chemisorption of oxygen on the freshly created fatigue fracture surface an oxide layer forms which effects premature crack face contact. These oxide scales usually become only a few atom radii thick, thus their influence on the crack closure level is considered to be negligible. However, in the unloading sequence of a fatigue cycle the crack surfaces come into contact, caused by residual plastic strains in the wake of the crack, and the oxide scale might be broken at weak positions, e.g. at edges of slip steps, on grain boundaries etc. During the subsequent loading the crack opens, fresh oxygen is offered again and the damaged regions are healed. As a result thicker parts (asperities) in the oxide are built-up (Fig. 1). They are responsible for asperity-induced crack closure.

![](./images/811943838955339777_1.jpg)

Fig. 1. Schematic to illustrate that asperities will effect premature crack face contact upon unloading.

Usually the magnitude of asperity-induced crack closure is measured by attaching a strain gauge on the specimen and during unloading the compliance of the sample is monitored. Crack closure is said to occur when a "significant" change in the specimen compliance is detected. It is generally believed that once a crack closes plastic flow is suppressed and the damage process stops. However, this statement is only right for fully closed cracks, i.e. the crack is closed within some distance from the crack tip, but not for partially closed cracks. In the latter case the crack faces contact at certain positions behind the crack tip. At partially closed cracks the stresses at the crack tip even may relax after crack face contact has occured. The simpliest way to demonstrate this is the elastic treatment of the asperity problem. In this case it can be shown [2-8] that the stress intensity at the crack tip decreases by a reduction of the far field stress intensity factor from $K_{cl}$ (stress intensity factor at first contact) to zero.

Asperity induced crack closure occurs most likely at certain positions behind the crack tip (see Fig. 1). The authors of hypothesis 1 argue that in this case the local crack tip stress intensity factor $k_{local}$ is in order of $20\%$ of $K_{cl}$ and-say the authors-asperity induced crack closure need not be considered when evaluating the fatigue crack growth rate.

In order to prove the correctness of hypothesis 1 we investigated the elastic interaction between asperities and a crack by means of a numerical procedure. The procedure is now explained and some results are reported.

# ELASTIC INTERACTION OF A SEMI-INFINITE CRACK WITH ASPERITIES

In our investigation of asperity-induced and plasticity-induced crack closure we assumed that the distance between the asperity and the crack tip and the plastic zone size, respectively, is small compared to overall specimen dimensions and to the distance from the crack tip to the points of the application of force. In this case it is sufficient to consider an unbounded body which is cut along the negative $x_1$-axis. The applied loading is described by a far field stress intensity factor $K_{global}$, where the remote stresses in this simplified situation are defined as follows:

$$
\sigma_{\mathrm{ij}}=\frac{K_{\text {global }}}{\sqrt{2 \pi r}} f_{\mathrm{ij}}(\theta) \tag{1}
$$

Here $f_{\mathrm{ij}(\theta)}$ is a dimensionless function.

![](./images/811943838955339777_2.jpg)

Fig. 2. Schematic representation of the crack face deformation due to an asperity.

For convenience and for later use a local stress intensity factor $k_{local}$ is defined by Eq. (2).

$$
k_{\text {local }}=\lim _{x_{1} \rightarrow 0^{+}}\left(\sigma_{22} \sqrt{2 \pi x_{1}}\right)
\tag{2}
$$

The coordinate system is given in Fig. 2. We make use of capital letters to designate global stress intensity factors, whereas small letters represent local ones.

Now consider Fig. 2. Suppose there is an asperity at a position $X$ with height $\delta$, its width is denoted $\Delta X$. In order to develop systematic and conclusive results, we confined our attention to a rigid, i.e. non-deformable, asperity. In reality the asperities are elastically strained. However, our simplification does significantly reduce the computational burden whereas the general features of the results are not influenced thereby.

Let's assume that the remote stresses are zero. Then the crack opening is solely caused by the asperity. In the linear elastic problem under consideration the displacement is prescribed in the interval I: $[X \leqslant x \leqslant X-\Delta X]$ and the stresses are prescribed (traction free condition) in the remaining part of the negative $x_{1}$-axis. This boundary value problem with mixed boundary conditions is solved by integrating a Greens function over the interval I (the Green's function must be constructed in such a way that the traction free condition is fulfilled automatically). This leads to a singular integral equation of Muskhelishvili type (Eq. (3)).

$$
\int_{-|X|}^{-|X-\Delta X|} P\left(x^{\prime}\right) g\left(x, x^{\prime}\right) \mathrm{d} x^{\prime}=\delta(x)
\tag{3}
$$

The as yet unknown contact stress between asperity and crack faces is denoted $P(x)$. Here $\delta(x)$ is the prescribed function of the upper crack face in the interval I. In our calculations we set

$$
\delta(x)=\frac{4 K_{\mathrm{cl}}}{E}\left(1-v^{2}\right) \sqrt{\frac{|x|}{2 \pi}}.
$$

The kernel (Green's function) $g(x, x')$ of the integral equation is well known [9] as

$$
g\left(x, x^{\prime}\right)=\frac{-2(1-v)}{\pi \mu} \operatorname{Im}\left[\arctan \sqrt{\frac{\left|x^{\prime}\right|}{x}}\right]
\tag{4}
$$

where Im denotes the imaginary part of a complex function, $E=$ Young's modulus, $\mu=$ shear modulus and $v=$ Poisson's ratio. Once the stress distribution $P(x)$ is obtained by solving Eq. (3),

![](./images/811943838955339777_3.jpg)

Fig. 3. The effect of an asperity on contact stresses. (A) A rigid asperity in an elastic crack. (B) The real stress distribution (dotted line) can be approximated by a step function (full lines).

$k_{local}$ can be calculated by Eq. (5)

$$
k_{\text {local }}=\sqrt{\frac{2}{\pi}} \int_{-|\mathrm{X}|}^{-|\mathrm{X}-\Delta \mathrm{X}|} \frac{P(x)}{\sqrt{x}} \mathrm{~d} x
\tag{5}
$$

In general an analytical solution of Eq. (3) cannot be found but a numerical one can be obtained as follows. The real stress distribution is approximated by a step function (Fig. 3).

As is suggested in Fig. 3 the several steps (elements) might have different widths. In fact, at stress concentrations, e.g. at the outer parts of I, a good accuracy requires a finer mesh than in the midpart, where a much coarser mesh can be chosen. With the use of the step function approximation, Eq. (3) is transformed to a system of linear algebraic equations.

$$
\sum_{\mathrm{i}} \tilde{P}_{\mathrm{i}}\left(x_{\mathrm{j}}\right) \tilde{g}_{\mathrm{i}}\left(x_{\mathrm{j}}\right)=\tilde{\delta}\left(x_{\mathrm{j}}\right)
\tag{6}
$$

where the tilde denotes step function approximation. Here and in Eq. (8) the summation is taken over all elements. Thus

$$
\begin{aligned}
\tilde{g}_{\mathrm{i}}\left(x_{\mathrm{j}}\right)= & \int_{\mathrm{e}_{1 \mathrm{i}}}^{\mathrm{e}_{2 \mathrm{i}}} g\left(x_{\mathrm{j}}, x^{\prime}\right) \mathrm{d} x^{\prime}=\frac{-2(1-v)}{\pi \mu} \\
& \times \operatorname{Im}\left\{e_{2}\left[\sqrt{\frac{x_{\mathrm{j}}}{e_{2}}}-\left(1+\frac{x_{\mathrm{j}}}{e_{2}} \arctan \sqrt{\frac{e_{2}}{x_{\mathrm{j}}}}\right]-e_{1}\left[\sqrt{\frac{x_{\mathrm{j}}}{e_{1}}}-\left(1+\frac{x_{\mathrm{j}}}{e_{1}} \arctan \sqrt{\frac{e_{1}}{x_{\mathrm{j}}}}\right]\right\}\right.
\tag{7}
\end{aligned}
$$

Here $e_{1 \mathrm{i}}$ denotes the coordinate of the left side of the $i$-th element and $e_{2 \mathrm{i}}$ the right side, respectively. Eq. (5) is now read:

$$
\tilde{k}_{\text {local }}=2 \sqrt{\frac{2}{\pi}} \sum_{\mathrm{i}} \tilde{P}_{\mathrm{i}}\left(\sqrt{\left|e_{1 \mathrm{i}}\right|}-\left(\sqrt{\left|e_{2 \mathrm{i}}\right|}\right)\right.
\tag{8}
$$

Equation (6) can be solved by an ordinary algebraic equation solver, e.g. the Gauss algorithm. By application of the sketched procedure a wide class of mixed problems in fracture mechanics can be treated. Results of our investigations concerning the interaction between a single asperity and a multiple asperity arrangement, respectively, and a semi-infinite crack, are now reported.

![](./images/811943838955339777_4.jpg)

Fig. 4. Crack contour at closure level and at zero load. The asperity lies in the validy region of hypothesis 1.

### Single asperity
As mentioned earlier the upper edge (horizon) of the asperity is supposed to be parabolic. Due to this assumption a smooth contact between the asperity and the crack is achieved.

The dotted line in Fig. 4 shows the crack contour at the moment of the first contact between asperity and crack ($K_{\text{global}} = K_{\text{cl}}$), the full line is the contour when the remote load is zero. Note that in this figure and in the following ones the units in the $x_2$ direction are about 1/100 of the units in the $x_1$ direction. The reduction of the stress intensity factor at the crack tip by decreasing $K_{\text{global}}$ from $K_{\text{cl}}$ to zero is readily apparent. This is the point of hypothesis 1. Hence, an experi- mentator using the compliance technique does not measure the actual $k_{\text{local}}$ at zero load but rather the larger $K$ at first contact, $K_{\text{cl}}$. The ratio $k_{\text{local}}/K_{\text{cl}}$ is strongly effected by the width $\Delta X$ of the asperity and by its position $X$. More precisely, in our numerical simulation it turned out that $k_{\text{local}}/K_{\text{cl}}$ can be correlated to $\Delta X$ (note that per definition the height of the asperity is determined by the position $X$). Thus, the effect of all possible single asperity arrangements can be plotted in a single curve, a mastercurve-this is shown in Fig. 5.

On the right side of Fig. 5, at $X/\Delta X = 1$, the asperity is a wedge which begins at the crack tip and ends at position $X$. Consequently, the stress intensity at zero load is equal to the stress

![](./images/811943838955339777_5.jpg)

Fig. 5. Mastercurve of the influence of a single asperity on the crack tip stress intensity factor $k_{\text{local}}$.
(A) The asperity lies in the validy range of hypothesis 1. (B) Asperities close to the crack tip have a significant larger influence on $k_{\text{local}}$.

intensity at first contact (full closed crack). Suppose now the asperity is shifted away from the crack tip towards $x_1 \to -\infty$. In this case its influence on the crack tip stress intensity decreases. The same dependence was identified by the analysis of the authors of hypothesis 1 and recently by Chen *et al.* [21]. They argue that for normally encountered asperities the ratio $k_{local}/K_{cl} \approx 0.2$. In Fig. 5(a) this region is marked by a shaded area. The corresponding $X/\Delta X \approx 1000$. This ratio might be a likely one in real situations (e.g. suppose the area of contact between asperity and crack surface is about 10 nm then the corresponding $X$ should be of the order of $10\ \mu$m). Asperities lying closer to the crack tip may have a significant larger influence on the crack tip stress intensity factor. This is shown in Fig. 5(b). However, the point is that in general there is not a single asperity only but there is a multiple asperity arrangement as sketched in Fig. 1. The influence of multiple asperities on the local stress intensity is considered in the following section.

Multiple asperity

Since the influence of a given asperity on the ratio $k_{local}/K_{cl}$ strongly depends on its position two extreme cases can be distinguished: firstly asperities with equal widths (in this case each asperity has a different influence (effectiveness) on the ratio $k_{local}/K_{cl}$) secondly asperities with different widths but the same effectiveness. We have considered both arrangements. As a result it is shown that in a multiple asperity arrangement the width of a single asperity plays a minor role; the actual $k_{local}$ is mostly influenced by the separation distance between the first and the last asperity.

In Tables 1 and 2 the positions and the widths for the asperities in the two computations are listed. The heigth of each asperity was chosen so that the crack faces contact at the same $K_{global} = K_{cl}$ for each asperity. In both calculations the same closure level $K_{cl}$ was taken. The results of both calculations are summarized in Fig. 6.

Two crack contours at zero load conditions are compared in Fig. 7. In Fig. 7(a) the result of

Table 1. Geometric relations in the case of equal widths between each asperity

<table>
  <thead>
    <tr>
      <th>Asperity</th>
      <th>$\frac{X_n}{\Delta X_1}$</th>
      <th>$\frac{\Delta X_n}{\Delta X_1}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>1000</td>
      <td>1</td>
    </tr>
    <tr>
      <td>2</td>
      <td>2000</td>
      <td>1</td>
    </tr>
    <tr>
      <td>3</td>
      <td>4000</td>
      <td>1</td>
    </tr>
    <tr>
      <td>4</td>
      <td>8000</td>
      <td>1</td>
    </tr>
  </tbody>
</table>

Table 2. Geometric relations in the case of equal effectiv- ness of each asperity

<table>
  <thead>
    <tr>
      <th>Asperity</th>
      <th>$\frac{X_n}{\Delta X_1}$</th>
      <th>$\frac{\Delta X_n}{\Delta X_1}$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>1000</td>
      <td>1</td>
    </tr>
    <tr>
      <td>2</td>
      <td>2000</td>
      <td>2</td>
    </tr>
    <tr>
      <td>3</td>
      <td>4000</td>
      <td>4</td>
    </tr>
    <tr>
      <td>4</td>
      <td>8000</td>
      <td>8</td>
    </tr>
  </tbody>
</table>

![](./images/811943838955339777_6.jpg)

Fig. 6. The influence of a multiple asperity arrangement on the stress intensity of the crack tip.

![](./images/811943838955339777_7.jpg)

Fig. 7. The crack face displacement (CFD). (A) Multiple asperity arrangement. (B) Single asperity arrangement.

the computation with 4 asperities (equal effectiveness) is shown and in Fig. 7(b) the crack faces due to one asperity with the same effectiveness is depicted.

The contrast clearly illustrates that in a multiple asperity configuration not only that asperity which is closest to the crack tip but all asperities contribute to the local stress intensity $k_{local}$. It should be emphasized that in real fatigue cracks the situation of Fig. 7(a) is more likely than that of 7(b).

In the former case an experimentor using the compliance technique would measure a $K_{cl}$ which is approximately equal to $k_{local}$. In our opinion hypothesis 1 is valid in case of a single dominating asperity. Such an arrangement is unlikely but not impossible. Vecchio *et al.* [10] and later Hertzberg *et al.* [11] studied experimentally the influence of asperities on the fatigue crack growth rate. Their idea was to put a needle or similar artificial asperities between the two mating surfaces. The advantage of such a procedure is that the position and the geometry of the asperity are well defined. Their experiments clearly indicate that the crack growth rate decreased by inserting the needles. But a more elaborate analysis showed that the measured $da/dN$ was much larger than predicted by utilization of the closure concept. Our results and hypothesis 1 suggest that the discrepancy between measured and predicted crack growth rates is due to the implicitness of a fully closed crack by the classical closure concept, but in this special experiment this assumption was not fulfilled.

Nevertheless, in a great majority of non-artificial asperities at fatigue cracks hypothesis 1 is false, at least in the stringency proposed by its authors. Besides, it should be remembered that the two- dimensional and purely elastic treatment of the interaction between asperities and a fatigue crack tip only gives a rough idea of the actual events at the tip. Numerical values obtained by means of two-dimensional linear elasticity should be considered with caution when transfered to three- dimensional elasto-plastic fatigue crack growth. Firstly, in the case of a three-dimensional arrange- ment of asperities the numerical values of $k_{local}/K_{cl}$ might change to some extent but to us it appears even more important that the co-existence of the plastic wake and the asperities change the situation at the crack tip thoroughly. Plasticity induced crack closure is probably the reason why asperities are formed at all and the contribution of the two kinds of crack closure might not be summable (in contrast to $K$ fields in linear elasticity) but we expect an interdependence. It is not yet clear how large the excess becomes and how it depends on the actual situation at the crack tip. These are points which should be considered in future.

In what follows hypothesis 2 is investigated; it will be shown that plasticity induced crack closure is not physically impossible. Contrarily, conditions are given when it occurs.

# PLASTICITY-INDUCED CRACK CLOSURE

During fatigue crack growth residual plastic strains are left in the wake of the crack. In the unloading sequence the plastic wake is elastically unloaded which might cause crack closure. At present this kind of crack closure is well understood under plane stress conditions. Here the crack closes due to an out-of-plane plastic flow, which can be regarded as an additional wedge filled into the crack (e.g. Budiansky and Hutchinson [12]). Under plane strain conditions such a mechanism is impossible, since per definition out-of-plane flow is not permitted. However, it is not yet clear whether plasticity induced crack closure occurs also under plane strain conditions. The results reported in the literature are ambiguous; see McClung [13] and [2-8]. In the present study the investigations [2-8] are re-considered.

To begin with, let us suppose that plasticity (i.e. dislocation flow) is originated at the crack tip in accordance with the assumptions in [2-8]. Each emitted dislocation leaves an edge in the crack contour (see Fig. 8).

In order to estimate the crack opening we have to sum up the contributions which force the crack to be open (the edge which is produced by dislocation emission) and the elastic back-bending of the crack faces due to dislocation 1, 2, 3. It is known [12] that the elastic $y$-deformation of the crack faces caused by dislocation 1 is smaller than the height of the edge produced by dislocation 1. This is also true for dislocation 2, 3, .... The authors of hypothesis 2 argue that for that reason the crack is open always (i.e. if the remote stresses are tensile) and everywhere.

But they did not take into account that dislocations, of course, also displace the crack faces between the edge they produce and the crack tip. These contributions to the total $y$-displacement are also negative-this is shown in Fig. 9(a) for an edge dislocation whose slip plane intersects the crack plane behind the tip. The co-ordinates of the dislocation are: $r=-100 b$, $\rho=2000 b, \alpha=70.5^{\circ}$, where the various symbols are explained in Fig. 9(b). The equations describing the crack face deformation caused by an edge dislocation are given in the Appendix. The elastic constants chosen to make Fig. 9(a) are: Young's modulus $E=200,000 \mathrm{MPa}$, Poisson's ratio $v=0.3$.

We again direct attention to Fig. 8. Let's consider the displacement of the marked point $P_{\mathrm{c}}$. The single contribution which opens the crack is the edge produced by dislocation 1, but there are many contributions which force the crack to close-the elastic displacement of dislocation $1,2,3, \ldots$ It is theoretically, easy to choose a dislocation distribution which in sum leads to a negative displacement of the crack faces at $P_{\mathrm{c}}$-in this case the crack is closed.

A somewhat more quantitative argument is obtained by use of a dislocation model for describing

![](./images/811943838955339777_8.jpg)

Fig. 8. The crack is opened by the edges of the dislocations. The closure effect and the elastic back bending is not indicated; for comparison see Fig. 10.

![](./images/811943838955339777_9.jpg)

Fig. 9. Schematic crack contour after dislocation emission. (A) The crack faces overlap induced by a single edge dislocation. (B) The co-ordinates used to describe the dislocation-crack system.

cyclic crack tip plasticity. The model is explained in detail in [14]. The advantage of describing crack tip plasticity as the motion of dislocations is that the linear elasticity theory can be applied to simulate non-linear, i.e. plastic, material behavior. Especially, it can be shown that the stresses at a crack tip embedded into a plastified region, i.e. a crack tip surrounded by dislocations, can be characterized by a local stress intensity factor $k_{local}$. Of course, $k_{local}$ differs, in general, from the applied or far field stress intensity factor $K_{global}$ (the definitions have been presented previously).

In our simulations we applied the Rice-Thomson mechanism for dislocation generation at a crack tip. As a result $k_{local}$ never can rise above $+k_{e}$ and it never can get lower than $-k_{e}$, where $k_{e}$ is the critical stress intensity for dislocation emission [15-16]. In the investigations [14], it turned out that $k_{local}$ at maximum load and at minimum load is equal to $+k_{e}$ and $-k_{e}$, respectively, provided that $\Delta K_{global}>3.5k_{e}$. For a smaller $\Delta K_{global}$ value the local stress intensity $k_{local}$ at minimum load is somewhat larger than $-k_{e}$.

Consider now Fig. 10 where the crack contour at zero load is sketched. Note that at the second edge the crack is closed. In the subsequent analysis two length parameters $h, w$ appear, both are marked in Fig. 10. The term $h$ denotes the height of the edge which is produced by dislocation emission, thus $h/2=|b|\sin\alpha$ (the factor $\frac{1}{2}$ is due to the assumption of a symmetric dislocation emission). Parameter $w$ is the average length between the slip planes of two neighbouring dislo-cations remaining in the bulk. In order to get conclusive results we confine attention to $k_{local}=$ $-k_{e}$. As discussed above this limits the validity of our results to $\Delta K_{global}>3.5k_{e}$. However, $k_{e}$ in ductile metals is a very small value, it is below the Griffith value for ideally brittle materials, so that this limitation is insignificant. Apart from this the analysis is confined to "opened" cracks, i.e.

![](./images/811943838955339777_10.jpg)

Fig. 10. The crack closes due to the plastic wake.

to the moment of the first contact between the two crack faces; since the occurence of crack closure would change the stress field in the vicinity of the tip and, hence, $k_{local}$.

The crack face deformation in the immediate vicinity of the tip can be calculated fairly well with the common crack tip equations of linear elasticity. Thus, crack face contact occurs if the elastic displacement $u$ at position $x=-w$ is equal to $-h/2$, i.e. if:

$$
w \geqslant 2\pi \left( \frac{E}{k_{\mathrm{e}}} \right)^2 \left[ \frac{|b| \sin \alpha}{4(1-v^2)} \right]^2 \tag{9}
$$

Here, plane strain conditions are supposed.

Just for demonstration: Let $\beta=0.25$ nm, $\alpha=70^\circ$, $E=210$ GPa, $v=0.3$, $k_{\mathrm{e}}=0.5$ MPa$\sqrt{\mathrm{m}}$; then $w/b$ has to be equal or larger than 18. This is well below the $w/b=200$ which turned out in our simulations [17]. Thus, plasticity induced crack closure is in fact a phenomenon which inhibits fatigue crack growth. Here it should also be emphasized that the purely mechanical consideration of crack tip events neglects interatomic (Van der Waal's) forces. Due to the small crack tip opening (of the order of one Burgers vector) the Van der Waal's forces may have a considerable influence on crack deformation and crack closure behaviour as well [18]. Since the freshly separated atom layers want to recombine again the Van der Waal's forces even support the propensity of the crack to close.

## CONCLUSIONS

In recent literature the assertion is made that the concept of crack closure is not capable of describing the various influences on the fatigue crack growth rate. The reasons given are:

(1) The compliance technique for measuring asperity-induced crack closure predicts too large a closure stress intensity factor.
(2) Plasticity that originates from the crack tip cannot contribute to its closure.

We have shown that hypothesis 1 is valid in the single asperity situation only. In more likely situations (multiple asperities) an experimentor using the compliance technique would nearly measure the true crack tip stress intensity factor. Furthermore, some statements are given which suggest that the line of arguments in hypothesis 2 is erroneous. A sufficient condition for plasticity induced crack closure to occur is presented.

Acknowledgement—This work was supported by the Austrian FFF (Fonds zur Förderung der wissenschaftlichen Forschung), Projekt Nr. P 10116 TEC.

## REFERENCES

1. W. Elber (1970) Fatigue crack closure under cyclic tension. *Engng Fract. Mech.* **2**, 37-45.
2. A. K. Vasudevan, K. Sadananda and N. Louat (1992) Reconsideration of fatigue crack closure. *Scripta Metall. Materialia* **27**, 1673-1678.
3. A. K. Vasudevan, K. Sadananda and N. Louat (1993) Two critical stress intensities for threshold fatigue crack propagation. *Scripta Metall. Materialia* **28**, 65-70.
4. K. Sadananda and A. K. Vasudevan (1995) Analysis of fatigue crack closure and thresholds.In: *Fracture Mechanics, 25th Volume, ASTM STP 1220* (Edited by F. Erdogan), pp. 484-501.
5. A. K. Vasudevan, K. Sadananda and N. Louat (1993) In: *Fatigue '93* (Edited by J.-P. Bailond and J. I. Dickson), EMAS Publ., I, pp. 571.
6. K. Sadananda and A. K. Vasudevan (1993) In: *Aspects of High Temperature Deformation and Fracture in Crystalline Materials* (Edited by Y. Hosoi *et al.*), JIM Publ., Tokyo, p. 551.
7. A. K. Vasudevan, K. Sadananda and N. Louat (1994) A review of crack closure, fatigue thresholds and related phenomena. *Mater. Sci. Engng* **A188**, 1-22.

8. K. Sadananda and A. K. Vasudevan (1995) Fatigue crack growth behavior in titanium aluminides. *Mater. Sci. Engng* **A192/193**, 490-501.

9. H. Tada, P. C. Paris and G. R. Irwin (1985) The stress analysis of cracks handbook. Del Research Corporation, St. Louis, Missouri.

10. R. S. Vecchio, J. S. Crompton and R. W. Hertzberg (1986) Anomalous aspects of crack closure. *Int. J. Fract.* **31**, R29-R33.

11. R. W. Hertzberg, C. H. Newton and R. Jaccard (1988) *Crack Closure: Correlation and Confusion*, ASTM STP 982. American Society for Testing and Materials, Philadelphia, 139-148.

12. B. Budiansky and J. W. Hutchinson (1978) Analysis of closure in fatigue crack growth. *J. Appl. Mech.* **45**, 267-276.

13. R. C. McClung, B. H. Thacker and S. Roy (1991) Finite element visualization of fatigue crack closure in plane stress and plane strain. *Int. J. Fract.* **50**, 27-49.

14. F. O. Riemelmoser, R. Pippan and O. Kolednik. "Cyclic crack growth in elastic plastic solids: A description in terms of dislocation theory", *J. Comp. Mech.*, in press.

15. J. R. Rice and R. Thomson, (1974) Ductile versus brittle behaviour of crystals. *Phil. Mag.* **29**, 73-97.

16. J. R. Rice (1992) Dislocation nucleation from a crack tip: an analysis based on the Peierls concept. *J. Mech. Phys. Solids* **40**, 239-271.

17. F. O. Riemelmoser and R. Pippan (1996) Plasticity induced crack closure under plane strain conditions in terms of dislocation arrangement. *Proc. Fatigue 96*.

18. G. Ebi and P. Neumann (1990) Closure behavior of small cracks. In: *Proceeding of Fatigue 90*. Honolulu Hawaii, pp. 1033-1042.

19. N. I. Muskhelishvili (1963) *Some basic problems of the theory of elasticity*. Noordhof, Groningen, The Nederlands.

20. L. H. Lin and R. Thomson (1986) Cleavage, dislocation emission, and shielding for cracks under general loading. *Acta Metall.* **34**, 187-206.

21. D. L. Chen, B. Weiss and R. Stickler (1996) A model for crack closure. *Engng Fract. Mech.* **53**, 493-509.

## APPENDIX

Let us consider a linear elastic body which is cut along the negative $x_1$-axis. The stresses and displacements $u$ are described by Eq. (A.1) of Muskhelishvili and Kolosov [19]:

$$
\begin{align}
\sigma_{11}+\sigma_{22}&=2\left[\phi^{\prime}(z)+\overline{\phi^{\prime}(z)}\right] \\
\sigma_{22}-i\sigma_{12}&=\phi^{\prime}(z)+\overline{\omega^{\prime}(z)}+(z-\bar{z})\overline{\phi^{\prime\prime}(z)} \tag{A.1} \\
u=u_1+iu_2&=\frac{1}{2\mu}\left[\kappa\phi(z)-(z-\bar{z})\overline{\phi^{\prime}(z)}-\overline{\omega(z)}\right]
\end{align}
$$

Here $\phi, \omega$ are two complex functions and $z$ is the complex variable $z=x+iy$. A bar denotes the complex conjugate and a prime the complex derivation with respect to $z$. The parameters $\mu$ and $\kappa$ are the shear modulus and the Muskhelishvili constant, respectively.

Since the knowledge of the stress field introduced by a dislocation in the cracked body is essential for a proper understanding of crack tip plasticity and crack tip shielding, many researchers have investigated the system edge dislocation-crack. The complex potentials $\Omega(z)=\omega^{\prime}(z)$ and $\Phi(z)=\phi^{\prime}(z)$ are given, e.g. in [20]. A simple integration with respect to $z$ gives

$$
\begin{align}
\phi=\phi_0+\phi_1&=2\log\left[\frac{z_0-z}{z_0}\right]+\bar{A}\frac{z_0-\overline{z_0}}{\overline{z_0}}\frac{\sqrt{z}}{\sqrt{z}+\sqrt{\overline{z_0}}}-2A\log\left[\frac{(\sqrt{z}+\sqrt{\overline{z_0}})(\sqrt{z}+\sqrt{z_0})}{\sqrt{z_0\overline{z_0}}}\right] \\
\omega=\omega_0+\omega_1&=2\bar{A}\log\left[\frac{z_0-z}{z_0}\right]+2A\frac{z(z_0-\overline{z_0})}{z_0(z-z_0)}-A\frac{(z_0-\overline{z_0})}{z_0}\frac{\sqrt{z}}{\sqrt{z}+\sqrt{z_0}}-2\bar{A}\log\left[\frac{(\sqrt{z}+\sqrt{\overline{z_0}})(\sqrt{z}+\sqrt{z_0})}{\sqrt{z_0\overline{z_0}}}\right] \tag{A.2}
\end{align}
$$

Here $\phi_0$ (the first term on the right side of Eq. (A.2)) and $\omega_0$ (the first and the second term) correspond to the potentials of an edge dislocation at position $z_0$ in the unbounded and uncut continuum whereas $\phi_1$ and $\omega_1$ give the "reaction" of the crack. The constant $A$ in Eq. (A.2) is defined as follows:

$$
A=\frac{\mu b}{2\pi i(\kappa+1)}, \tag{A.3}
$$

where $b$ is the Burgers vector in its complex form, i.e. $b=b_1+ib_2$. Equation (A.2) is based on the assumption that the crack is either opened or the crack faces are allowed to overlap. The latter is, of course, physically impossible and a more suitable solution should be sought. Nevertheless, Eq. (A.2) can be used in the argument presented in the paper where we want to prove whether the crack closes due to dislocations in the wake of the crack. The point is that either the crack is

open and Eq. (A.2) makes physical sense or, on the other hand, the crack is closed and our assertion that plasticity induced crack closure occurs under plane strain conditions is anyway proved to be true.

Let us now estimate the crack opening displacement $\delta$ due to an edge dislocation. Equation (A.1) in conjunction with Eq. (A.2) gives:

$$
\delta=u_{2}^{+}-u_{2}^{-}=\frac{1}{2 \mu}\left\{\operatorname{Im}[\kappa \phi(z)-\overline{\omega(z)}]^{+}-\operatorname{Im}[\kappa \phi(z)-\overline{\omega(z)}]^{-}\right\} \tag{A.4}
$$

Here $^{+}$and $^{-}$correponds to the boundary value of the complex functions on the upper and lower side of the negative $x_{1^{-}}$ axis, respectively, and Im denotes the imaginary part of a complex function. With the assumption $\sqrt{|x_{1}|}<1$ can be expanded into a Taylor series. Omitting the details this provides:

$$
\delta_{\left(\sqrt{\left|x_{1}\right|}<1\right)} \approx \frac{1}{\pi i} \frac{\sqrt{\left|x_{1}\right|}}{\sqrt{\overline{z_{0}}}}\left[b+b \sqrt{\frac{\overline{z_{0}}}{z_{0}}}+\bar{b}\left(\frac{z_{0}}{\overline{z_{0}}}-1\right)\right] \tag{A.5}
$$

Accordingly, $\delta$ decreases with $1/\sqrt{r_{0}}$, where $r_{0}$ is Euklid's distance between the edge dislocation and the crack tip.