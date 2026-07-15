
# Electric polarization and discrete shift from boundary and corner charge in crystalline Chern insulators

Yuxuan Zhang \( ^{1} \)  and Maissam Barkeshli \( ^{1} \) 

 \( ^{1} \) Department of Physics and Joint Quantum Institute University of Maryland, College Park, Maryland 20742, USA

Recently, it has been shown how topological phases of matter with crystalline symmetry and  \( U(1) \)  charge conservation can be partially characterized by a set of many-body invariants, the discrete shift  \( \delta_{o} \)  and electric polarization  \( \vec{\mathcal{P}}_{o} \) , where o labels a high symmetry point. Crucially, these can be defined even with non-zero Chern number and/or magnetic field. One manifestation of these invariants is through quantized fractional contributions to the charge in the vicinity of a lattice disclination or dislocation. In this paper, we show that these invariants can also be extracted from the length and corner dependence of the total charge (mod 1) on the boundary of the system. We provide a general formula in terms of  \( \delta_{o} \)  and  \( \vec{\mathcal{P}}_{o} \)  for the total charge of any subregion of the system which can include full boundaries or bulk lattice defects, unifying boundary, corner, disclination, and dislocation charge responses into a single general theory. These results hold for Chern insulators, despite their gapless chiral edge modes, and for which an unambiguous definition of an intrinsically two-dimensional electric polarization has been unclear until recently. We also discuss how our theory can fully characterize the topological response of quadrupole insulators.

## CONTENTS

I. Introduction 1
A. Organization of paper 2
II. Main Result 2
III. Geometrical Measures 3
A. Definitions of  \( \vec{L}_{o} \)  and  \( \vec{b}_{o} \)  3
B. Definitions of  \( \Gamma \) ,  \( \Omega_{disc} \)  and  \( \Omega_{cor} \)  4
C. Equivalence classes of  \( \vec{L}_{o} \)  5
D. Definitions of  \( n_{W,o} \)  and  \( \delta\Phi_{W,o}  \)  5
IV. Charge calculation 6
A. Edge charge and quantized electric polarization 6
B. Corner charge 7
V. Equivalence between boundaries and bulk defects 8
VI. Topological crystalline gauge theory description 9
VII. Application to quadrupole and higher-order topological insulators 11
VIII. Discussion 12
Acknowledgments 13
A. C = 0 calculation of the unit cell measure  \( \vec{n}_{o} \) ,  \( m_{o} \)  13
References 14

## I. INTRODUCTION

Over the past few decades, substantial progress has been made in the understanding of  \( (2+1) \) D topological phases of matter with crystalline symmetry (for a partial list of references, see for example  \( [1-46] \) ). In particular, recently a number of topological invariants protected by crystalline symmetry have been understood which are well-defined in the many-body interacting setting beyond single-particle band theory, and which correspond to quantized physical responses  \( [33, 34, 39, 40, 44] \) . In this paper, we focus on two such invariants, which we refer to as the discrete shift  \( \delta_{o} \)  and the electric (charge) polarization  \( \vec{\mathcal{P}}_{o} \) , where o denotes a high symmetry point in the unit cell. Ref.  \( [39, 44] \)  showed how to extract these many-body invariants from microscopic models and precisely match predictions from topological quantum field theory and G-crossed braided tensor category theory  \( [8, 33, 34] \) . Crucially, these results apply also in the case of non-zero Chern number and/or magnetic field.

The discrete shift  \( \delta_{o} \)  is a  \( Z_{M} \)  invariant protected by M-fold rotations about o, and it specifies a quantized fractional contribution to the electric charge in the vicinity of a lattice disclination centered at o. \( ^{[39, 44]} \)  It also specifies a dual response, the angular momentum of magnetic flux, and can be extracted from (partial) rotation operations. \( ^{[40]} \) 

The electric polarization  \( \vec{\mathcal{P}}_{o} \)  can be viewed as a topological invariant associated with translational symmetry. It is quantized in the presence of M-fold rotational symmetry, and can only take non-trivial quantized values when  \( M = 2, 3, 4 \)  [33]. In the absence of rotational symmetry ( \( M = 1 \) ),  \( \vec{\mathcal{P}}_{o} \)  can be viewed as an unquantized topological response [47]. We emphasize that  \( \vec{\mathcal{P}}_{o} \)  is an intrinsically two-dimensional polarization, not an effective 1d polarization of the 2d system viewed as a 1d system, as it often considered in discussions of Chern insulators.

The electric polarization is of particular interest, because the question of whether electric polarization can be defined in Chern insulators has been somewhat unclear until recently. Ref. [48] provided a single-particle Berry phase definition of electric polarization in Chern
 

insulators, but this requires an arbitrary choice of momentum in the Brillouin zone, whose physical meaning is unclear. Ref. [47, 49] later suggested that electric polarization may not be well-defined in Chern insulators \( ^{1} \) . Recently [44] showed unambiguously that one can define an electric polarization in Chern insulators consistently through a variety of different physical response properties of the system. For this paper, the most relevant of these is that it specifies a fractional quantized contribution to the charge in the vicinity of a lattice defect with non-zero Burgers vector, such as a lattice dislocation or an impure lattice disclination.

In the case of Chern number C = 0, it is known that the discrete shift and electric polarization have implications for the boundary and corner charge of the system. In particular, the fractional charge associated with a lattice disclination also implies fractional charge at corners of the system  \( [32, 50–53] \) . Similarly, electric polarization is well-known to specify the boundary charge density.

The purpose of this paper is to study the fate of these corner and boundary charges in the case of non-zero Chern number,  \( C \neq 0 \) , where the system has topologically protected gapless edge states. Specifically, to what extent can  \( \delta_{o} \)  and  \( \bar{P}_{o} \)  be extracted from the boundary and corner charge of Chern insulators with crystalline symmetry?

The main result of this paper is Eq. 2-3, which gives the total charge (mod 1) on the boundary of a Chern insulator with crystalline symmetry in terms of quantized topological invariants, and which is invariant to any local perturbations on the boundary. We derive Eq. 3 from topological quantum field theory considerations and match it to numerical calculations on microscopic models.  \( \delta_{o} \)  contributes to the corner-angle dependence of the total charge mod 1 while  \( \bar{P}_{o} \)  contributes to the length-dependence along the boundary. The choice of high symmetry point o manifests as a specific ambiguity in decomposing various contributions to the boundary charge. These results unify the boundary, corner, disclination, and dislocation charge responses into a single general theory.

Our results suggest that  \( \bar{P}_{o} \)  may be experimentally measurable in crystalline Chern insulators from high-resolution scanning local charge measurements along the boundary of two-dimensional quantum materials. Our results also suggest a variety of other geometries that could be used to infer the corner-angle dependence of the boundary charge and extract  \( \delta_{o} \) .

One application of our general theory is in giving a complete characterization of quadrupole insulators and related higher-order topological insulators (HOTIs). In particular, the quantized corner charge is extensively studied in the HOTI literature  \( [24, 50, 53–57] \) , and has been explained using multipolar moment. Recently, it has been shown that multipolar moment is inadequate

![](./images/1050657912365514763_1.jpg)

FIG. 1. The  \( C_{4} \)  symmetric unit cell with maximal Wyckoff positions  \( [o] \in \{\alpha, \beta, \gamma_{1}, \gamma_{2}\} \) . The choice of unit cell in the square lattice is in general arbitrary, and we use the convention that  \( \beta \)  represents vertices and  \( \alpha \)  represents plaquette centers.

to account for the corner charges [58]. We show that the corner charge response can be fully accounted for by the discrete shift  \( \delta_{o} \) .

## A. Organization of paper

The remainder of this paper is organized as follows. Sec. II defines the charge response to boundaries and bulk defects, which is the main result of our paper. Sec. III defines the relevant geometrical measures and the notion of extra flux  \( \delta\Phi_{W,o} \)  of the boundary and bulk defects. Sec. IV presents the numerical calculations for the square lattice Hofstadter model that verify our main result. Sec. IV A outlines the procedure for calculating  \( \bar{P}_{o} \)  through edge charge on one boundary of a cylinder. Sec. IV B presents details on calculating  \( \delta_{o} \)  through corner contributions to the charge. Sec. V establishes an equivalence between corners and disclinations; edges and dislocations. Sec. VI reviews the derivation of the charge response using the framework of topological quantum field theory. Sec. VII applies our charge response to a HOTI model and calculates its  \( \delta_{o} \)  and  \( \bar{P}_{o} \) .

## II. MAIN RESULT

We consider a Chern insulator with  \( U(1) \)  charge conservation symmetry,  \( Z^{2} \)  (magnetic) translation symmetry with flux  \( \phi \)  per unit cell, and a  \( Z_{4} \)  rotational symmetry. The full symmetry group we consider is then  \( G = U(1) \times_{\phi} [\mathbb{Z}^{2} \rtimes \mathbb{Z}_{4}] \) . The Chern insulator has a Chern number C and a charge per unit cell (filling)  \( \nu \) .

Refs. [39, 44] showed the existence of quantized topological invariants  \( \delta_{o} \)  and  \( \bar{P}_{o}^{2} \) , which depend on a maximal Wyckoff position (MWP)  \( [o] = \alpha, \beta, \gamma_{1}, \gamma_{2} \)  (see Fig. 1). For a fixed C,  \( \delta_{o} \)  can take four possible values modulo 4, such that  \( \delta_{o} \mod 1 = \frac{C}{2} \mod 1 \) . The quantized electric polarization  \( \bar{P}_{o} \)  defines a  \( Z_{2} \)  invariant. For
 
![](./images/1050657912365514763_2.jpg)

![](./images/1050657912365514763_3.jpg)

![](./images/1050657912365514763_4.jpg)

![](./images/1050657912365514763_5.jpg)

FIG. 2. (a) Region W covering a boundary with three corners. The red loop  \( \gamma_{\beta} \)  is aligned with  \( \partial W \)  and determines the corresponding  \( \Gamma = \pi/2 \)  and  \( \vec{L}_{\beta} = (-6,0) \) , the total corner angle is  \( \Omega_{cor} = \Gamma - 2\pi = -3\pi/2 \) . The weightings for  \( Q_{W} \)  are labeled on each site. This lattice is created by removing the central site of a  \( \Omega_{disc} = \frac{\pi}{2} \)  disclination. (b) Region W covering a boundary with four corners. The red loop  \( \gamma_{\alpha} \)  determines the corresponding  \( \Gamma = 4\pi \)  and  \( \vec{L}_{o} = (0,-1) \) , the total corner angle is  \( \Omega_{cor} = \Gamma - 2\pi = 2\pi \) . (c) Region W covering one side of a cylinder with non-trivial shear. Here,  \( \Gamma = 2\pi \)  and  \( \vec{L}_{\beta} = (16,-1) \)  (d) Region W covering the outside of a ribbon. Here,  \( \Gamma = 5\pi/2 \) ,  \( \vec{L}_{\alpha} = (0,19) \) , and the corner angle is  \( \Omega_{cor} = \pi/2 \) .

the  \( C_{4} \)  symmetric MWPs  \( \alpha,\beta \) , we have  \( \mathcal{P}_{\mathrm{o}}=(0,0) \)  or  \( (1/2,1/2) \)  mod  \( Z^{2} \) . The dependence on o was found to be [44]:

 \[ \{\mathcal{S}_{\beta},\mathcal{\bar{\mathcal{P}}}_{\beta},\kappa\}=\{\mathcal{S}_{\alpha}+4\mathcal{P}_{\alpha,\gamma}-\kappa,\mathcal{\bar{\mathcal{P}}}_{\alpha}+(\frac{\kappa}{2},\frac{\kappa}{2}),\kappa\}, \quad (1) \] 

where  \( \kappa\equiv\nu-C\phi/2\pi \) . Note that the fact that electric polarization of a system with total non-zero charge requires a choice of origin o in the unit cell is well-known. The dependence on o is usually removed when a neutralizing background, such as a background ionic contribution, is added. In this paper we are focused on properties of the electronic system, and thus do not consider a neutralizing background.

To determine the contribution of these invariants to the charge response, we consider a large subregion W of the system. W is chosen such that its boundary  \( \partial W \)  is deep in the bulk, far away from any boundaries of the lattice and any defects in the interior of the lattice. Moreover, W is defined so that  \( \partial W \)  is aligned with the boundary of the unit cell. We note that unlike the definition in Ref. [44], W can include boundaries and corners of the lattice in addition to disclinations and dislocations. Our results show how equivalences can be made between lattice defects and boundaries, which will be discussed in Sec. V.

The total charge  \( Q_{W} \)  within the region W is defined as [39]

 \[ Q_{W}\equiv\sum_{i\in W}\mathrm{wt}(i)Q_{i}. \quad (2) \] 

Here  \( i \in W \)  labels the sites in W, and  \( Q_{i} \)  is the average charge on site i. The weighting factor  \( \mathrm{wt}(i) = 1 \)  if i is in the interior W, and  \( \mathrm{wt}(i) = 0 \)  if i is outside of W. For sites i that lie at the boundary  \( \partial W \) ,  \( 2\pi\mathrm{wt}(i) \)  is the angle subtended by  \( \partial W \)  in the interior of W at i.

We find that, in the limit where  \( \partial W \)  is far from boundaries and defects,  \( Q_{W} \)  obeys the following equation:

 \[ Q_{W}=\mathcal{s}_{0}\frac{\Gamma}{2\pi}+\vec{L}_{o}\cdot\mathcal{\bar{\mathcal{P}}}_{o}+\nu n_{W,o}+\frac{C\delta\Phi_{W,o}}{2\pi}\mod1. \quad (3) \] 

Here, the quantities  \( \Gamma \) ,  \( \vec{L}_{o} \) ,  \( n_{W,o} \) , and  \( \delta\Phi_{W,o} \mod \)  on geometrical properties of the lattice with boundaries, corners, dislocations, and disclinations in the region W, and will be defined precisely in Sec. III. Briefly,  \( 2\pi - \Gamma \)  is the total angle by which a vector is rotated upon traversing  \( \partial W \) . \( ^{3} \)   \( \vec{L}_{o} \)  is the sum of translation vectors obtained upon traversing a loop  \( \gamma_{o} \)  in W that starts at o and encloses all lattice boundaries and defects in W.  \( \gamma_{o} \)  should be smoothly deformable to the boundary  \( \partial W \)  without passing through any defects or boundaries of the lattice. For simplicity we also require  \( \gamma_{o} \)  to be non-self-intersecting.  \( n_{W,o} \)  is a measure of an effective number of unit cells in W, and  \( \delta\Phi_{W,o} \)  is a measure of the change in magnetic flux in W relative to an appropriate reference background.

The main point of Eq. 3 is that given a choice of high symmetry point o, there are distinct fractionally quantized contributions to  \( Q_{W} \)  arising from the invariants  \( \delta_{o} \)  and  \( \bar{P}_{o} \) , Chern number C, and filling  \( \nu \) .

Eq. (3) is numerically verified in Sec. IV A, IV B, and VII, and is explained using field theory in Sec. VI.

## III. GEOMETRICAL MEASURES

In this section we define precisely the geometrical quantities  \( \vec{L}_{o} \) ,  \( \Gamma \) ,  \( n_{W,o} \)  and  \( \delta\Phi_{W,o} \mod \)  in Eq. 3, and their relationship to Burger's vectors and Frank angles of lattice dislocations and disclinations.

## A. Definitions of  \( \vec{L}_{o} \)  and  \( \vec{b}_{o} \) 

Consider a loop  \( \gamma_{o} \)  which is obtained by starting and ending at a high symmetry point o and following a set of unit translation vectors.
 

(a)

![](./images/1050657912365514763_6.jpg)

(b)

![](./images/1050657912365514763_7.jpg)

(c)

![](./images/1050657912365514763_8.jpg)

FIG. 3. (a) Lattice with corner angle  \( \Gamma = -\pi/2 \)  can be isometrically embedded on a cone with apex angle  \( \Omega = 3\pi/2 \)  (i.e. disclination angle for a lattice). (b)  \( \Gamma \)  and  \( \vec{L}_{o} \)  can be calculated using the red loop via Eq. 4. For  \( o = \beta \) , choosing origin to be either  \( o_{1} \)  or  \( o_{2} \)  gives either  \( \vec{L}_{o_{1}} = (0, 10) \)  or  \( \vec{L}_{o_{2}} = (1, 9) \) , which is in the same equivalence class. (c) For  \( o = \alpha \) ,  \( \vec{L}_{o} = (0, 11) \)  which lies in a different equivalence class compared to choosing  \( o = \beta \) .

Note that o refers to a point on the lattice. We can write  \( [o] \in \{\alpha, \beta, \gamma_{1}, \gamma_{2}\} \)  as the maximal Wyckoff position (MWP) of o. In this paper we will slightly abuse notation and drop the square brackets. Whether a given quantity depends on o as a specific high symmetry point in the lattice or only through its MWP should be clear from context.

The interior of  \( \gamma_{o} \)  contains all relevant defects and boundaries whose charge response we wish to compute using Eq. 3. Note that here the interior is defined to the left of the loop; that is, in the direction of the cross product of the out-of-plane direction and the translation vector. We then define

 \[ \vec{L}_{o}\equiv\sum_{j\in\gamma_{o}}\hat{L}_{j}. \quad (4) \] 

Here the sum is taken over the set of unit translations needed to traverse  \( \gamma_{o} \) , with  \( \hat{L}_{j} \in \{\pm\hat{x}, \pm\hat{y}\} \)  being the unit translation vectors, and j being points on the loop  \( \gamma_{o} \)  related by the translations. All j points correspond to the same MWP as o.

When  \( \gamma_{o} \)  encloses a single boundary,  \( \vec{L}_{o} \)  is a vectorized edge length of that boundary. In Fig. 2(c) we give an example of calculating  \( \vec{L}_{o} \)  on a cylinder with non-zero shear. In this case  \( \vec{L}_{o} \)  is independent of o, and the subscript can be omitted. When  \( \gamma_{o} \)  encloses a single dislocation or disclination,  \( \vec{L}_{o} \)  is reduced to the Burgers vector  \( \vec{b}_{o} = \vec{L}_{o} \)  (see also the discussion below in Sec. III C).

Recall that, as discussed in [44], the Burgers vector for a pure dislocation, in the absence of any disclinations, is independent of the choice of origin o. However in the presence of disclinations, the Burgers vector does depend on the MWP of o.

## B. Definitions of  \( \Gamma \) ,  \( \Omega_{disc} \)  and  \( \Omega_{cor} \) 

For the loop  \( \gamma_{o} \) ,  \( \Gamma \)  is defined as:

![](./images/1050657912365514763_9.jpg)

FIG. 4. A  \( \Omega_{disc} = -2\pi \)  disclination.

 \[ \Gamma\equiv2\pi-\sum_{j\in\gamma_{o}}K_{j}. \quad (5) \] 

Here, the  \( \sum_{j\in\gamma_{o}} \)  is as above, where we sum over points related by unit translation vectors.  \( K_{j} \)  is the curvature of the loop at the point j on  \( \gamma_{o} \) . More specifically,  \( K_{j} \)  is equal to  \( \pi - \theta \)  where  \( \theta \in \{\pi/2, \pi, 3\pi/2\} \)  is the angle subtended by the inside of the loop. Importantly, we define  \( \theta \)  as a real number (not just modulo  \( 2\pi \) ), so we have chosen a particular lift of the angles to the real numbers.

In the case where  \( \gamma_{o} \)  only encloses a disclination, then  \( \Gamma = \Omega_{disc} \) , which is the disclination angle lifted to the real numbers. This definition of  \( \Omega_{disc} \)  diverges slightly from more standard previous formulations, where  \( \Omega \)  is defined as the angle by which a local frame (vielbein) is rotated upon being parallel transported around the defect; under such a definition,  \( \Omega \)  is only defined modulo  \( 2\pi \) , which is problematic:  \( A\Omega_{disc} = -2\pi \)  disclination shown in Fig. 4 contributes a non-trivial fractional charge  \( Q_{W} = -\mathcal{E}_{o} = C/2 \mod 1 \)  [39]. This issue is fixed upon treating  \( \Omega_{disc} \)  as a lift of the disclination angle to the real numbers.

When  \( \gamma_{o} \)  only encloses a boundary, the corner angle
 

<table><tr><td>o</td><td>\( \vec{n}_{o} \)</td><td>\( m_{o} \)</td></tr><tr><td>\( \alpha \)</td><td>(0,0)</td><td>1</td></tr><tr><td>\( \beta \)</td><td>\( (1/2,1/2) \)</td><td>0</td></tr><tr><td>\( \gamma_{1} \)</td><td>(0,1/2)</td><td>0</td></tr><tr><td>\( \gamma_{2} \)</td><td>(1/2,0)</td><td>0</td></tr></table>

TABLE I.  \( \vec{n}_{o} \)  and  \( m_{o} \)  in the  \( C_{4} \)  symmetric unit cell

 \( \Omega_{cor} \)  can be determined from  \( \Gamma \)  by:

 \[ \Omega_{\mathrm{c o r}}=\Gamma-2\pi \quad (6) \] 

For instance, a lattice with corner angle  \( \Omega_{cor} = \pi/2 \)  is shown in Fig. 2(d).

Note that the boundary in Fig. 2(c) also includes two corners with opposite corner angle and the total corner angle  \( \Omega_{cor} = 0 \) .

## C. Equivalence classes of  \( \vec{L}_{o} \) 

When the total corner angle for a boundary is not zero modulo  \( 2\pi \) ,  \( \vec{L}_{o} \)  depends on the origin o. If we shift o by an integer vector  \( \vec{v} \in \vec{\Lambda} \) ,  \( o \to o + \vec{v} \)  such that  \( o + \vec{v}' \)  is still a point on  \( \gamma_{o} \) , then

 \[ \vec{L}_{o+\vec{v}}=\vec{L}_{o}+(1-U(\Gamma))\vec{v}, \quad (7) \] 

where  \( U(\Gamma) \)  represents a counterclockwise rotation by  \( \Gamma \) .

The shift  \( o \rightarrow o + \vec{v} \)  does not change the high symmetry point of o; they both lie in the same maximal Wyckoff position. We define an equivalence class on  \( \vec{L}_{o} \) :

 \[ \vec{L}_{o}\simeq\vec{L}_{o}+(1-U(\Gamma))\vec{\Lambda}, \quad (8) \] 

where  \( \vec{\Lambda} \)  is an integer vector. Then  \( \vec{L}_{o+\vec{v}} \simeq \vec{L}_{o} \) . Notably,  \( (1 - U(\Gamma))\vec{\Lambda} \cdot \vec{\mathcal{P}}_{o} = 0 \mod 1 \) , which implies that the charge response in Eq. (3) only depends on the equivalence class of  \( \vec{L}_{o} \)  rather than its exact value [33, 44].

We can see this equivalence in the example shown in Fig. 3(b). For two origins  \( o_{1} \)  and  \( o_{2} \) , both having MWP  \( \beta \)  and related by an integer vector, both  \( \vec{L}_{o_{1}} \)  and  \( \vec{L}_{\circ_{2}} \)  lie in the same  \( [(0,0)] \)  equivalence class. If  \( o_{3} = \alpha \) , as seen in Fig. 3(c), then  \( \vec{L}_{o_{3}} \)  lies in the  \( [(0,1)] \)  equivalence class instead.

We remark that a lattice with corner angle  \( \Omega_{cor} \)  can be isometrically embedded on a cone with deficit angle  \( \Omega = \Omega_{cor} + 2\pi \)  as seen in Fig. 3(a). This demonstrates that a lattice with a corner will reduce to a pure disclination in the limit where  \( \vec{L}_{o} \)  vanishes. This equivalence between corners and disclinations will be a recurring theme and discussed in Sec. V.

## D. Definitions of  \( n_{W,o} \)  and  \( \delta\Phi_{W,o} $ 

To calculate the charge associated to lattice disclinations, dislocations, boundaries, and corners, we need to

![](./images/1050657912365514763_10.jpg)

FIG. 5. A cylinder with periodic boundary condition in y-direction. The charge calculation using the blue(orange) shaded region  \( W_{1}(W_{2}) \)  will extract  \( \mathcal{P}_{\alpha,y}(\mathcal{P}_{\beta,y}) \) . In this example,  \( n_{W_{1},\beta}=4L_{y} \) ,  \( n_{W_{2},\alpha}=(3+1/2)L_{y} \)  is the number of unit cells inside  \( W_{1} \)  and  \( W_{2} \)  respectively. The red circle is the cutoff and is not regarded as the boundary of W.

account for the background charge density. Thus we need a measure of the number of unit cells in the region W. However, when we have lattice defects and boundaries, it is possible that the defect cores and lattice boundaries have irregular, fractional unit cells. This makes it more complicated to properly define the number of unit cells in W. The resolution to this is that we define a quantity  \( n_{W,o} \) :

 \[ n_{W,o}=k+\vec{L}_{o}\cdot\vec{n}_{o}+\frac{2\pi-\Gamma}{2\pi}m_{o}. \quad (9) \] 

Here, k is an integer, which is the number of full unit cells inside W.  \( \vec{n}_{o} \)  is a fractional vector and  \( m_{o} \)  is an fractional scalar, both of which depend only on the maximal Wyckoff position of o. Their values are tabulated in Table I, and are determined by fitting Eq. (3), (9) to the case where the Chern number C = 0 and the insulating state can be fully described in terms of maximally localized Wannier functions (see App. A), in which case there is an independent definition of the electric polarization. This approach is similar to the method presented in [44].

 \( n_{W,o} \)  plays the role of an effective number of unit cells in W. When there are no defects or lattice boundaries in W, then  \( n_{W,o} = k \)  is simply the integer number of unit cells in W, and is independent of o. However in the presence of defects and/or boundaries, the contribution of the background charge term  \( \nu n_{W,o} \)  in Eq. 3 necessarily depends on maximal Wyckoff position (MWP) of o. This is because the other terms in the decomposition of Eq. 3,  \( \mathcal{E}_{o}\Gamma/2\pi \) ,  \( \vec{L}_{o}\cdot\vec{\mathcal{P}}_{o} \) , also depend on the MWP of o.

Similarly, we define an effective excess flux in W as

 \[ \delta\Phi_{W,o}=\Phi_{W}-\phi n_{W,o}. \quad (10) \] 

 \( \Phi_{W} \)  is the total flux within W and  \( \phi \)  is the flux per unit cell.  \( \phi n_{W,o} \)  indicates how much flux there should be if no excess flux is inserted.

Note that if we shift  \( n_{W,o} \rightarrow n_{W,o}+1 \) , then we can see from Eq. 3 that  \( Q_{W} \rightarrow Q_{W} + \nu - C\phi/2\pi \mod 1 = Q_{W} \mod 1 \) , because  \( \kappa \equiv \nu - C\phi/2\pi \)  must be an integer for any Chern insulator. Therefore,  \( Q_{W} \mod 1 \)  is only sensitive to  \( n_{W,o} \mod 1 \) . We can think of the latter as
 
![](./images/1050657912365514763_11.jpg)

FIG. 6. (a) (b) The charge density at each site on a cylinder with periodic boundary condition in the y-direction. The region W covers the left boundary. We have added a random on-site potential on the left boundary to show that  \( \overline{Q}_{W,o} \)  is robust against perturbations. The parameters are:  \( o = \alpha \) , C = -2,  \( \phi/2\pi = \pi - \epsilon \) , where  \( \epsilon \)  is a small amount required to open the gap.  \( L_{x} \times L_{y} = 40 \times 30 \)  for (a), and  \( L_{x} \times L_{y} = 40 \times 31 \)  for (b). (c)  \( \overline{Q}_{W,o} \)  converges to fractional values as R, the width of W, is large enough.

the effective fractional value of the number of unit cells in W.

To understand more clearly how the origin dependence of  \( n_{W,o} \)  is manifested, consider the case where the lattice forms a cylinder, and W encloses one of the boundaries. We can think of the lattice boundary as either having support on the vertices or the plaquette centers. Specifically, we take the lattice boundary to have support along  \( x = o_{x} + 1/2 \) , where  \( o_{x} \)  is the x-component of o. With this lattice cutoff,  \( n_{W,o} \)  calculated in Eq. (9) is the same as the area of W. As shown in Fig. 5, the cutoff, depicted as the red cycle, is vertically crossing the sites when  \( o = \alpha \) , and the cutoff is vertically crossing the plaquette center when  \( o = \beta \) . The fractional number of unit cells per unit length can then be visualized in terms of the area between the red cycle and the closest unit cell boundary.

It is important to clarify that the choice of the boundary cutoff (red cycle in Fig. 5) should not be conflated with the smooth and rough boundaries of the lattice. The latter refers to the lattice configuration at the boundary, while the former is a theoretical tool to define the total number of unit cells  \( n_{W,o} \) , without imposing any constraint on the lattice configuration at the boundary. Our numerics confirms that the lattice configuration at the boundaries does not affect the calculation of the  \( \delta_{o} \)  and  \( \overline{P}_{o} \)  invariants, regardless of whether the boundary is smooth, rough or even more exotic, such as breaking translation symmetry in the y-direction.

## IV. CHARGE CALCULATION

In this section we numerically verify Eq. 3, focusing on the polarization and discrete shift contributions separately by first studying boundary charge on a cylinder and second by studying corner contributions to the charge.

## A. Edge charge and quantized electric polarization

In this section, we focus on the explicit calculation of the electric polarization  \( \overline{\mathcal{P}}_{o} \)  using boundary charge. We consider the Hofstadter model defined on a cylindrical geometry with periodic boundary conditions along the y-axis and open boundary conditions along the x-axis, as shown in Fig. 5.

The Hofstadter Hamiltonian is

 \[ H_{\mathrm{c y l i n d e r}}=-\sum_{\langle i j\rangle}t_{i j}c_{i}^{\dagger}c_{j}+\mathrm{h.c.}, \quad (11) \] 

where the nearest neighbour hopping  \( t_{ij} \equiv te^{iA_{ij}} \)  defines the vector potential  \( A_{ij} \)  with  \( \phi \)  flux per plaquette.

We define a large region W which fully encloses one of the boundaries of the cylinder shown in Fig. 5. In this example, the vectorized edge length is  \( \bar{L}_{\mathrm{o}} = (0, L_{y}) \) ,  \( \Gamma = 2\pi \)  and the corner angle  \( \Omega_{cor} = 0 \) .

We empirically find that  \( Q_{W} \)  obeys

 \[ Q_{W}=\frac{C}{2}+\bar{L}_{\mathrm{o}}\cdot\vec{\mathcal{P}}_{\mathrm{o}}+\nu n_{W,\mathrm{o}}+\frac{C\delta\Phi_{W,\mathrm{o}}}{2\pi}\mod1. \quad (12) \] 

This agrees with Eq. (3) after using the relation  \( \delta_{o} \mod 1 = C/2 \mod 1 \)  [39]. To show this, we set  \( \delta\Phi_{W,o} = 0 \)  in the Hamiltonian and present the explicit numerical data for the regularized charge after subtracting the background contribution:

 \[ \overline{{Q}}_{W,\mathrm{o}}\equiv Q_{W}-\nu n_{W,\mathrm{o}}. \quad (13) \] 

In Fig. 6, we show the charge profile on a cylinder where  \( \overline{Q}_{W,o} \)  converges to the predicted fraction for a large enough W. The quantization is shown to persist even in the presence of random on-site perturbations along the boundary as shown in Fig. 6. In Fig. 7, we show the full colored Hofstadter butterfly for  \( \overline{Q}_{W,o} \) , where  \( P_{o,y} \)  can be extracted. We find that the extracted  \( P_{o,y} \)  agrees with  \( P_{o} \) , calculated using other methods in [44].

A naive interpretation of a two-dimensional polarization would be that it specifies a charge per unit length along the boundary. However such a definition is complicated because one needs to disentangle the boundary
 
![](./images/1050657912365514763_12.jpg)

FIG. 7. The full Hofstadter butterfly of the regularized charge  \( \overline{Q}_{W,o} \)  for  \( o=\{\alpha,\beta\} \) ,  \( L_{y}=\{30,31\} \) . There are 40 sites in x-direction.  \( n_{W,o}=15L_{y}(15.5L_{y}) \)  if  \( o=\alpha(\beta) \) . In lobes of higher Chern number, the correlation length is of the order of the size of the system, so finite size effects result in noise in the colored Hofstadter butterfly.

(a)

![](./images/1050657912365514763_13.jpg)

(b)

![](./images/1050657912365514763_14.jpg)

(c)

![](./images/1050657912365514763_15.jpg)

(d)

![](./images/1050657912365514763_16.jpg)

FIG. 8. (a) Region W covering the outer boundary of a  \( \pi/2 \)  disclination. In this example  \( \Gamma=7\pi/2 \) ,  \( \vec{L}_{\beta}\simeq[(0,0)] \) ,  \( \vec{L}_{\alpha}\simeq[(1,0)] \) ,  \( n_{W,\beta}=36 \) ,  \( n_{\mathrm{W},\beta}=36-3/4 \) . (b) A ribbon geometry where W encloses a corner with  \( \Omega_{cor}=-\frac{\pi}{2} \)  and a full edge. This lattice is effectively a top-down projection of the lattice in Fig. 3. Although visually distorted, each unit cell is regarded as a perfect square. In this example  \( \Gamma=3\pi/2 \) .  \( \vec{L}_{\beta}\simeq[(0,0)] \) ,  \( \vec{L}_{\beta}\simeq[(1,0)] \) ,  \( n_{W,\beta}=17 \) ,  \( n_{\mathrm{W},\alpha}=17+1/4 \) . (c)-(d) charge profile of the geometry in (a) and (b). In (d) we glue the two boundary along the arrow direction to obtain the ribbon geometry. The inner corner and outer corners are labeled with stars. The parameters are  \( C=2 \) ,  \( \phi=\pi+\epsilon=0 \) ,  \( \beta \) . (e)  \( \overline{Q}_{W,o} \)  converges to fractional values for a large enough R.

and the bulk charge, and furthermore it is not robust to perturbations along the boundary that break translational symmetry. Our results demonstrate that one can generically define a boundary charge and obtain a precise definition of  \( \overline{\mathcal{S}}_{o} \)  that is robust to random perturbations along the boundary in terms of the oscillatory system size dependence of  \( Q_{W} \)  mod 1.

As found in [44], an oscillatory  \( L_{y} \) -dependent response also appears when we view the cylinder as an effective 1d system and compute the effective 1d polarization along the x direction. Indeed  \( \overline{Q}_{W,o} \) , which is the boundary contribution of the charge, effectively specifies a polarization of the 1d system through a net dipole moment along the x-direction. The results here provide an alternative way to extract  \( \overline{\mathcal{S}}_{o} \)  through a careful definition of the boundary charge  \( \overline{Q}_{W,o} \) .

## B. Corner charge

We now outline the methodology for calculating the corner charge in the square lattice Hofstadter model. A corner is inherently conjoined with 2 edges. Furthermore, the presence of gapless chiral edge states implies that we cannot directly consider the charge near a corner. Rather, we must consider a region containing a full boundary. We can then isolate the contribution from the corners by taking into account the contribution from the polarization and other bulk contributions.
 
![](./images/1050657912365514763_17.jpg)

FIG. 9. The full Hofstadter butterfly of the regularized ribbon charge  \( \overline{Q}_{W,o} \)  for  \( o = \{\alpha, \beta\} \) . The total number of sites at the inner boundary is 10, 11 for  \( o = \beta \) ,  \( \alpha \)  and the width of the ribbon is 30. In both cases  \( \vec{L}_{o} \in [(0, 0)] \) 

A familiar example of a corner geometry is shown in Fig. 8(a) which is the outer boundary of a lattice with a disclination, where \(\Gamma = \frac{7\pi}{2}\). Another example is shown in Fig. 8(b) where the region \(W\) contains only one corner with the minimal corner angle \(\Omega_{\mathrm{cor}} = -\frac{\pi}{2}\), \(\Gamma = \frac{3\pi}{2}\).

We can numerically calculate  \( Q_{W} \)  for Fig.8(a)(b). They follow:

 \[ Q_{W}=\frac{C}{2}+\frac{3}{4}\mathcal{E}_{o}+\vec{L}_{o}\cdot\vec{\mathcal{P}}_{o}+\nu n_{W,o}+\frac{C\delta\Phi_{W,o}}{2\pi}\mod1, \quad (14) \] 

 \[ Q_{W}=\frac{C}{2}-\frac{1}{4}\mathcal{E}_{o}+\vec{L}_{o}\cdot\vec{\mathcal{P}}_{o}+\nu n_{W,o}+\frac{C\delta\Phi_{W,o}}{2\pi}\mod1, \quad (15) \] 

which agrees with Eq. (3) after using the relation  \( \delta_{o} \mod 1 = C \mod 1 \) . Similar to the edge charge calculation in the preceding section, we consider systems where  \( \delta\Phi_{W,o} = 0 \) , and define  \( \overline{Q}_{W,o} \equiv Q_{W} - \nu_{W,o} \) . We show in Fig. 8(c,d,e) the charge profile of  \( \overline{Q}_{W,o} \)  which converges to the predicted fraction for a large enough W.

In Fig. 8(a), one can consider the complement of W,  \( \overline{W} \) , which has the same boundary  \( \partial\overline{W} \equiv \partial W \) .  \( \overline{W} \)  characterizes the familiar disclination charge. Since the total charge over the manifold is a integer, we can obtain the boundary charge by  \( Q_{W} = -Q_{\overline{W}} \mod 1 \) . Such procedure gives the same result as in Eq. (14).

We additionally show the full Hofstadter butterfly of  \( \overline{Q}_{W,o} \)  for the Fig. 8(b) geometry in Fig. 9, where we have considered geometries where  \( \vec{L}_{o} \simeq [(0,0)] \)  such that the  \( \vec{P}_{o} \)  contribution vanishes.

It is worth noting that since  \( \delta_{o} \mod 1 = C/2 \mod 1 \) , Eq. (15) can be reformulated as

 \[ Q_{W}=\vec{L}_{o}\cdot\vec{\mathcal{P}}_{o}+\frac{3}{4}\mathcal{E}_{o}+\nu n_{W,o}+\frac{C\delta\Phi_{W,o}}{2\pi}\mod1. \quad (16) \] 

This alternative expression offers a different interpretation:  \( Q_{W} \)  represents the charge of a impure disclination with burgers vector  \( \vec{b}_{o} = \vec{L}_{o} \)  and disclination angle  \( \Omega_{disc} = 2\pi + \Omega_{cor} = 3\pi/2 \) . In the  \( \vec{L}_{o} = 0 \)  limit the ribbon geometry reduces to a pure disclination with origin o and  \( \Omega_{disc} = 3\pi/2 \)  as demonstrated in Fig. 3(a). This suggests the existence of a generalized framework for understanding crystalline defects and boundaries, which we explore in Sec. V.

## V. EQUIVALENCE BETWEEN BOUNDARIES AND BULK DEFECTS

We now present a more in-depth understanding of the equivalence between edges and dislocations, and corners and disclinations. In Sec. IV B we showed an example where a  \( \Omega_{cor} = -\frac{\pi}{2} \)  corner with vectorized edge length  \( \vec{L}_{o} \)  is equivalent to a  \( \Omega = \frac{3\pi}{2} \)  pure disclination in the limit  \( \vec{L}_{o} = (0,0) \) . This statement can be further generalized as follows.

Consider an orientable 2-manifold M with genus g and number of boundaries  \( n_{boundary} \) . The Gauss-Bonnet theorem is given by:

 \[ \chi=\frac{1}{2\pi}\int_{\mathcal{M}}R d A+\frac{1}{2\pi}\int_{\partial\mathcal{M}}K d s \quad (17) \] 

where  \( \chi = 2 - 2g - n_{boundary} \)  is the Euler characteristic of the manifold M. R is the Gaussian curvature, and dA is an area element; K is the geodesic curvature on the boundary  \( \partialM \) , and ds is a line element. The geodesic curvature K is formally defined as the norm of the covariant derivative  \( K = ||D\hat{T}/ds|| \) , where  \( \hat{T} \)  is the unit tangent vector along the boundary.

Now consider a lattice which in the bulk contains lattice disclinations with disclination angle  \( \Omega_{disc,i} \)  and on the boundary contains corners with corner angles  \( \Omega_{cor,j} \) . Here i and j label the disclinations and corners respectively. The total disclination and corner angles are  \( \Omega_{disc} = \sum_{i} \Omega_{disc,i} \)  and  \( \Omega_{cor} = \sum_{j} \Omega_{cor,j} \) . A quantum many-body system defined on such a lattice will be described at low energies by a quantum field theory defined on a spatial manifold M, where the lattice disclinations and corners can be modeled in the continuum geometry by delta function sources of bulk and boundary curva-
 

ture. That is,

 \[ \int_{\mathcal{M}}R d A=\sum_{i}\Omega_{\mathrm{d i s c},i},\quad\int_{\partial\mathcal{M}}K d s=\sum_{j}\Omega_{\mathrm{c o r},j}. \quad (18) \] 

Eq. (17) can then be reformulated as

 \[ \frac{\sum_{i}\Omega_{\mathrm{d i s c},i}}{2\pi}+\frac{\sum_{j}\Omega_{\mathrm{c o r},j}}{2\pi}=2-2g-n_{\mathrm{b o u n d a r y}}. \quad (19) \] 

A corollary of Eq. (19) is that we can choose one of two different ways to label a boundary.

1. A boundary with  \( n_{boundary} = 1 \)  and total edge curvature  \( \Omega_{cor} \) , vectorized edge length  \( \vec{L}_{o} \) ,

2. A (impure) disclination with disclination angle  \( \Omega_{disc} = \Omega_{cor} + 2\pi \)  and Burgers vector  \( \vec{b}_{o} = \vec{L}_{o} \) , and there is no boundary at all,  \( n_{boundary} = 0 \) .

This is consistent with the intuition from Sec. II in that two sets of lattice defects/boundaries contribute equivalently to the charge mod 1 if their  \( \Gamma \)  and  \( \vec{L}_{o} \)  are the same.

By this corollary, in the charge calculation we could choose to separate the contributions from bulk lattice defects (dislocations and disclinations) and the lattice boundaries (edges and corners) instead of packaging all of the information in  \( \Gamma \)  and  \( \vec{L}_{o} \) . Eq. (3) can be equivalently written as:

 \[ \begin{align*}Q_{W}=\frac{C}{2}n_{\mathrm{boundary}}+\frac{\Omega_{\mathrm{disc}}}{2\pi}\mathcal{E}_{o}+\frac{\Omega_{\mathrm{cor}}}{2\pi}\mathcal{E}_{o}+\vec{b}_{o}\cdot\vec{\mathcal{P}}_{o}\\+\vec{L}_{o}\cdot\tilde{\mathcal{P}}_{o}+\nu n_{W,o}+C\frac{\delta\Phi_{W,o}}{2\pi}\mod1\end{align*} \quad (20) \] 

where we have used the relation  \( E_{o} \mod 1 = C/2 \mod 1 \) . Here  \( \vec{b}_{o} \)  is the total Burgers vector of the lattice disclinations and dislocations in W, while  \( \vec{L}_{o} \)  is the vectorized edge length along any lattice boundaries in W.

To intuitively understand the  \( \frac{C}{2} \)  term, consider a cylinder constructed by removing the opposite faces of a rectangular cuboid. Each face of the cuboid is conjoined with four  \( \frac{\pi}{2} \)  disclinations. The action of removing one face can be considered local as it is far from the boundary of region W. Therefore, one end of the cylinder can be considered to have total disclination angle  \( 2\pi \) , resulting in an extra  \( E_{o} \)  mod 1 contribution to  \( Q_{W} \)  in Eq. (20). Using the proven relation  \( E_{o} \mod 1 = C/2 \mod 1 \)  [39], attributing the hole of the cylinder as a  \( 2\pi \)  disclination recovers the  \( \frac{C}{2} \)  contribution to  \( Q_{W} \)  on the cylinder.

A different way of understanding the  \( \frac{C}{2} \)  contribution is that this term is necessary to regularize the charge such that a trivial defect will have  \( Q_{W}=0 \)  mod 1. Consider a trivial defect constructed by removing a site, setting  \( o=\beta \) , as shown in Fig. 10. Before inserting this defect,  \( Q_{W}=16\nu \)  mod 1 only receives contributions from the  \( \nu n_{W,o} \)  term. Since this trivial defect is a local modification of the system,  \( Q_{W} \)  should not change modulo 1 after

![](./images/1050657912365514763_18.jpg)

FIG. 10. The region W covering a trivial defect which is created by removing a site.

inserting the defect. We can model this defect as having one boundary, four corners with total corner angle  \( \Omega_{cor} = -2\pi \) , an edge length  \( \vec{L}_{\beta} = (0,0) \) , and four fewer unit cells as compared to the clean lattice while maintaining the same total flux  \( \Phi_{W} \) . The charge response, according to Eq. 3, reads

 \[ \begin{aligned}Q_{W}&=\frac{C}{2}+\vec{0}\cdot\vec{\mathcal{P}}_{\beta}-\mathcal{E}_{\beta}\frac{2\pi}{2\pi}+\nu(16-4)+\frac{4C\phi}{2\pi}\mod1\\&=\frac{C}{2}-\mathcal{E}_{\beta}+16\nu-4\kappa\mod1\\&=16\nu\mod1,\end{aligned} \quad (21) \] 

Here, we have again used the proven relation  \( E_{o} \mod 1 = \frac{C}{2} \mod 1 \) . The charge before and after inserting the trivial defect is both  \( 16\nu \mod 1 \)  as expected since a trivial defect contributes integer charge. This means that for each boundary within W, there should be a  \( \frac{C}{2} \)  charge which is crucial for regularizing  \( Q_{W} \) . It is easy to check that with  \( o = \alpha \) ,  \( Q_{W} = 16\nu \mod 1 \)  as well and the same argument applies.

The discussion above shows that another way to view lattice boundaries with corners is entirely using the framework of disclinations and Burgers vectors. To use this perspective, we shift

 \[ \begin{aligned}\{\Omega_{\mathrm{disc}},\Omega_{\mathrm{cor}},n_{\mathrm{boundary}}\}\\\rightarrow\{\Omega_{\mathrm{disc}}+\Omega_{\mathrm{cor}}+2\pi n_{\mathrm{boundary}},0,0\},\end{aligned} \quad (22) \] 

and treat  \( \vec{L}_{o} = \vec{b}_{o} \)  as a Burgers vector. This is the perspective that we will take in connecting our results to the topological effective action derived in [33, 34, 39, 44] and reviewed below.

## VI. TOPOLOGICAL CRYSTALLINE GAUGE THEORY DESCRIPTION

In this section, we discuss how the results of the preceding sections can be understood through the framework of topological quantum field theory. Much of this section is a review of results presented in [33, 34, 39, 44].
 

Refs. [33, 34] developed the topological effective action for topological phases of bosons with symmetry group  \( G = U(1) \times_{\phi} [\mathbb{Z}^{2} \rtimes \mathbb{Z}_{M}] \) . The results were then extended to invertible fermionic topological phases in [39, 44], using the general theory of invertible fermionic topological phases of [59]. We proceed by introducing the background  \( U(1) \)  gauge field A, a background  \( Z_{M} \)  gauge field  \( \omega_{o} \)  associated with  \( Z_{M} \)  point group rotations about o, and a background  \( Z^{2} \)  gauge field  \( \vec{R} \) . Together  \( (A, \omega_{o}, \vec{R}) \)  define a background gauge field for the G symmetry.  \( \omega_{o} \)  and  \( \vec{R} \)  are referred to as crystalline gauge fields. In particular,  \( \omega_{o} \)  is referred to as the rotation gauge field, while  \( \vec{R} \)  is referred to as the translation gauge field. Their holonomies encode geometrical properties of the lattice [33].  \( \int_{W} d\omega_{o} \)  encodes the disclination angle in the region W, while  \( \int_{W} d\vec{R} \)  encodes the Burgers vector in the region W. For convenience we drop the subscript on  \( \omega_{o} \)  below.

Mathematically, it is helpful to begin in a simplicial formulation. We start with a 3-dimensional space-time manifold N and triangulate it. Then,  \( A_{ij} \in R \) ,  \( \omega_{ij} \in \frac{2\pi}{4}Z \)  and  \( \vec{R}_{ij} \)  are defined on 1-simplices (ij) of the triangulation, where i, j label 0-simplices (vertices). That is, mathematically they are 1-cochains defined on the triangulation. Note that  \( A_{ij} \)  and  \( \omega_{ij} \)  are technically lifts of the  \( U(1) \)  and  \( Z_{4} \)  gauge fields to R and  \( \frac{2\pi}{4}Z \) , respectively, which is important for defining the topological action. The action is then independent of the choice of lift.

To obtain a topological action for invertible bosonic topological phases, we pick a cohomology class  \( [\nu_{3}] \in H^{3}(BG, \mathbb{R}/\mathbb{Z}) \) , where BG is the classifying space [60, 61]. The gauge field can be interpreted as a map from the space-time manifold to the classifying space. Thus, assuming that  \( A, \omega, \vec{R} \)  are flat gauge fields, we can use them to pull back the 3-cocycle  \( \nu_{3} \)  to a 3-cocycle defined on the space-time manifold. On a closed space-time manifold, this leads [33] to a topologically invariant action  \( S = \int_{N} L \) , with Lagrangian density

 \[ \begin{align*}\mathcal{L}=&\frac{C}{4\pi}A\cup dA+\frac{\mathcal{S}_{o}}{2\pi}A\cup d\omega+\frac{\mathcal{T}_{o}}{2\pi}\cdot A\cup d\vec{R}\\&+\frac{\kappa}{2\pi}A\cup A_{XY}+\cdots,\end{align*} \quad (23) \] 

where  \( \cdots \)  includes topological terms not involving A, which do not concern us in this paper. Here  \( \cup \)  denotes the cup product and d denotes the coboundary operation. Here  \( A_{XY} \)  is a 2-cochain, whose explicit formula in terms of  \( \vec{R} \) ,  \( \omega \)  is given in [33]. If we take W to be a spatial region,  \( \int_{W} A_{XY} \)  represents the number of unit cells in  \( W^{4} \) .

In order to use more familiar notation, it is convenient to recast the above action in a continuum formulation. In this formulation, \(A\), \(\omega\), and \(\vec{R}\) are real-valued differential forms, and the action is written in the continuum using differentials and wedge products:

 \[ \begin{align*}\mathcal{L}=&\frac{C}{4\pi}A\wedge dA+\frac{\mathcal{S}_{o}}{2\pi}A\wedge d\omega+\frac{\mathcal{T}_{o}}{2\pi}\cdot A\wedge d\vec{R}\\&+\frac{\kappa}{2\pi}A\wedge A_{XY}+\cdots.\end{align*} \quad (24) \] 

The continuum versions of the gauge fields are defined such that integrating over a simplex gives the corresponding quantity in the simplicial formulation.

As explained in [33], the rotation gauge field  \( \omega \)  is closely related to the  \( SO(2) \)  spin connection on the spatial manifold on which the system is defined. A lattice system with a disclination is expected to be described at long wavelengths by a quantum field theory defined on a manifold where the disclination corresponds to a conical singularity, that is, a delta function source of curvature. Thus, if we split our space-time manifold into space and time,  \( N = M \times S^{1} \) , the space M has conical singularities at the locations corresponding to the lattice disclinations. Therefore, the rotation gauge flux  \( d\omega \)  is also equal to the geometric curvature. Nevertheless, it is important to distinguish the  \( SO(2) \)  spin connection from the  \( Z_{M} \)  rotation gauge field  \( \omega \) , because the discrete character of the rotation gauge field implies different possibilities for the classification of invariants and topological terms. The topological terms presented here can then be viewed as a discrete cousin of analogous terms that appear in the geometric response of continuum quantum Hall systems [62–64].

In the case of invertible fermionic phases, such as Chern insulators, which are the focus of this paper, we first use the classification of [59]. For the case of invertible fermionic phases with  \( U(1)^{f} \)  symmetry, \( ^{5} \)  invertible phases can be classified by  \( (c_{-}, n_{2}, \nu_{3}) \) , where  \( c_{-} \in Z \)  is the chiral central charge,  \( n_{2} \)  is a Z \( _{2} \) -valued 2-cochain on BG, while  \( \nu_{3} \)  is an R/Z \( \sim \) 2-valued 3-cochain on BG. As in the bosonic case, the topological action then corresponds to the pullback of  \( \nu_{3} \)  onto the space-time manifold N, and results in the same Lagrangian density as in the bosonic case, Eq. 23,24. The only difference is the quantization of the invariants C,  \( S_{o} \) . In the bosonic case, C must be an even integer and  \( S_{o} \)  is an integer. In the fermionic case C is any integer,  \( S_{o} \)  can be half-integer, and we have the identity  \( S_{o} = C/2 \mod 1 \)  [39].

We can use the topological action to obtain the charge in a region W:

 \[ Q_{W}=\int_{W}\frac{\delta\mathcal{L}}{\delta A_{0}}=C\frac{\Phi_{W}}{2\pi}+\mathcal{S}_{o}\frac{\Omega_{\mathrm{d i s c}}}{2\pi}+\mathcal{T}_{o}\cdot\vec{b}+\kappa n_{W} \quad (25) \] 

Here \(\Phi_{W} = \int_{W} dA\), \(\Omega_{\mathrm{disc}} = \int_{W} d\omega\), \(\vec{b} = \frac{1}{2\pi} \int_{W} d\vec{R}\), and \(n_{W} = \frac{1}{2\pi} \int_{W} A_{XY}\), and \(A_{0}\) is the time-component of \(A\).
 

So far, the topological action is defined for flat gauge fields. This translates to the requirement that for any region  \( W \) ,  \( \Phi_{W}/2\pi \) ,  \( \Omega_{\mathrm{disc}}/2\pi \) ,  $ (1-U(2\pi/M))^{-1}\vec{b}, and  \( n_{W} \)  are integer-valued [33]. While the topological action was derived for flat gauge fields, we will use it to deduce the response of the system to non-flat configurations of the gauge fields, which physically means that the region W contains non-trivial lattice disclinations and dislocations. This leads to complications where  \( n_{W} \)  is no longer well-defined in the topological gauge theory and the Burgers vector  \( \vec{b} \)  necessarily depends on a choice of high symmetry point o when disclinations are present in the system.

Therefore, motivated by the topological field theory result, we consider the prediction:

 \[ \begin{align*}Q_{W}&=C\frac{\Phi_{W}}{2\pi}+\mathcal{E}_{0}\frac{\Omega_{\mathrm{disc}}}{2\pi}+\vec{\mathcal{P}}_{o}\cdot\vec{b}_{o}+\kappa n_{W,o}\mod1\\&=C\frac{\partial\Phi_{W,o}}{2\pi}+\mathcal{E}_{0}\frac{\Omega_{\mathrm{disc}}}{2\pi}+\vec{\mathcal{P}}_{o}\cdot\vec{b}_{o}+\nu n_{W,o}\mod1,\end{align*} \quad (26) \] 

where in the second line we have used that the charge per unit cell satisfies  \( \nu = \kappa + C\phi/2\pi \) ,  \( \phi \)  is the flux per unit cell, and we defined  \( \delta\Phi_{W,o} \equiv \Phi_W - \phi n_{W,o} \) . This equation incorporates the fact that the Burgers vector  \( \vec{b}_o \)  must generically depend on a choice of high symmetry point o. The modular reduction incorporates the charge quantization,  \( \Phi_W \sim \Phi_W + 2\pi \)  by a large gauge transformation, and also the fact that non-topological effects like local potentials can change the charge in a given region by an integer. Empirically we find that this equation does successfully account for the charge in the region W, provided that  \( n_{W,o} \)  is suitably defined, as discussed in Sec. III D.

The discussion above explicitly accounted for boundaries and corners in W by treating them using the formalism of disclinations and dislocations. An alternative way to proceed would be to explicitly derive a boundary effective action, and then use it to compute the charge response at the boundary. Such a method was pursued for continuum quantum Hall systems and the Wen-Zee term in  \( [65] \)  and used to understand the filling anomaly in higher order topological insulators in  \( [52] \) . We leave it to future work to explicitly derive a general boundary effective action for the topological crystalline gauge theory used in this paper.

## VII. APPLICATION TO QUADRUPOLE AND HIGHER-ORDER TOPOLOGICAL INSULATORS

In light of our theory of corner charges, it is now appropriate to revisit earlier studies that have investigated corner charges in higher order topological insulators (HOTIs) and quadrupole insulators (QIs)  \( [24, 50, 53–56] \) . In this section we demonstrate how these quantized corner charges can be completely described using our charge response theory in the case where the symmetry under consideration involves  \( U(1) \)  charge conservation,  \( Z^{2} \)  translation symmetry, and  \( Z_{M} \)  point group rotational

![](./images/1050657912365514763_19.jpg)

FIG. 11. Unit cell of the QI model, grey dots represent sites, red links represent hoppings with amplitude  \( t_{1} \)  black links connecting adjacent unit cells represent hoppings with amplitude  \( t_{2} \) . Dotted lines have negative hopping amplitude. This inserts  \( \pi \)  flux per plaquette. The colored dots are MWPs  \( \alpha \) ,  \( \beta \) ,  \( \gamma \) . The sites are not at the MWPs in this example

symmetry, as in this paper. An important conclusion is that the discrete shift  \( \delta_{o} \)  and quantized electric polarization  \( \vec{P}_{o} \)  are the invariants that completely account for the corner charge phenomena; quadrupole and higher multipole moments are not necessary to describe these phenomena. Furthermore, as we will see, our results also highlight how there is no natural notion of a trivial vs. non-trivial quadrupole insulator, since a shift of the origin on a real lattice zero and non-zero values of  \( \delta_{o} \)  and  \( \vec{P}_{o} \) .

The first QI model, as defined in [54] is a  \( C_{4} \)  symmetric tight binding model where the bands have Chern number C = 0. The choice of unit cell and the hopping parameters are shown in Fig. 11. We proceed to calculate  \( \delta_{o} \)  and  \( \vec{P}_{o} \)  in this model.

First, we analyze the band structure. When corners and edges are present in the lattice, localized corner modes and delocalized edge states emerge. These states are highlighted in Fig. 12(a). Since the topological invariant  \( \delta_{o} \)   \( \vec{P}_{o} \)  and  \( \nu \)  are intrinsically bulk invariants, they remain unaltered upon filling these edge and corner states.

To calculate  \( \vec{P}_{o} \)  we set up the system on a cylinder similar to the procedure outlined in Sec. IV A. Since C = 0 for each band, the edge charge equation (12) simplifies to

 \[ Q_{W}=L_{y}\mathcal{P}_{o,y}+\nu n_{W,o}\mod1 \quad (27) \] 

Again,  \( \nu n_{W,\alpha} \)  is always an integer, and  \( \nu n_{W,\beta} = \nu n_{W, \alpha} + L_{y}/2 \) . A direct numerical calculation of  \( P_{o,y} \)  using Eq. (27) is shown in Fig. 12. We found  \( P_{\alpha,y} = P_{\beta,y} = 0 \mod 1 \)  for every bulk gapped phase. Because of the  \( C_{4} \)  symmetry, we have  \( P_{\alpha,x} = P_{\beta,x} = 0 \mod 1 \)  as well.

As a sanity check, [44] derived that under a shift of origin  \( o \rightarrow o + \vec{v} \) ,  \( \vec{P}_{o} \)  should shift following the equation:

 \[ \vec{\mathcal{P}}_{o+\vec{v}}=\vec{\mathcal{P}}_{0}+\kappa(-v_{y},v_{x}), \quad (28) \] 

where  \( \kappa = \nu - C\phi/2\pi = \nu \)  in this case. The numerically calculated  \( \vec{P}_{o} \)  in this case indeed satisfies Eq. 28.

Next, we set up the calculation of S through corner charge in a ribbon geometry similar to Fig. 8(b). In this
 
![](./images/1050657912365514763_20.jpg)

![](./images/1050657912365514763_21.jpg)

![](./images/1050657912365514763_22.jpg)

![](./images/1050657912365514763_23.jpg)

FIG. 12. (a) Energy levels of the QI model as a function of  \( t_{1}/t_{2} \) . Grey colored states are bulk states; blue colored states are localized at the edge, and the red colored states are localized at a corner. The edge states vanish on a torus, and the corner states vanish on either a torus or a cylinder. (b) Numerically calculated  \( S_{o,y} \) , on the edge of a cylinder following Eq. (27) for  \( L_{y}=15,16 \) . We set up the radius of W such that  \( n_{W,\alpha}=6L_{y} \) , and  \( n_{W,\beta}=6.5L_{y} \) .  \( o=\alpha \) ,  \( \beta \)  extract the same  \( S_{o,y} \) . (c)(d) Numerically calculated  \( S_{o} \)  following Eq. (29). W is defined similarly to that of Fig. 8(b) on a lattice where  \( \vec{L}_{o}\simeq[(0,0)] \) . Gray color label represent possible values of  \( S_{o} \)  and  \( \vec{S}_{o} \)  but never appeared in the spectrum. Note that  \( S_{o} \)  and  \( \vec{S}_{o} \)  give quantized values only when the bulk is gapped, and regardless of whether the boundary is gapped or not.

case \(\Omega_{\mathrm{cor}} = -\frac{\pi}{2}\), \(C = 0\), \(\vec{\mathcal{P}}_{\mathrm{o}} = (0,0)\). Eq. (15) simplifies to

 \[ Q_{W}=-\frac{1}{4}\mathcal{E}_{\mathrm{o}}+\nu n_{W,\mathrm{o}}\mod1. \quad (29) \] 

The ribbon lattice of the QI is constructed by replacing each plaquette in Fig. 8(b) by the QI unit cell. A direct numerical calculation of  \( E_{o} \)  is shown in Fig. 12.

As a sanity check, the numerical value of  \( E_{\alpha} \)  and  \( E_{\beta} \)  satisfy their proven relation [44]

 \[ \mathcal{E}_{\beta}=\mathcal{E}_{\alpha}+4\mathcal{P}_{\alpha,y}-\kappa. \quad (30) \] 

We have thereby shown that the corner charge in a HOTI model can be described using our theory of the charge response.

In the HOTI literature, insulators with non-zero corner (or disclination) charges are classified as topologically non-trivial HOTIs, while those with zero corner (or disclination) charges are deemed trivial. However, this binary classification is unnatural. For instance, in the square-lattice Hofstadter model at full filling,  \( E_{\alpha} = 0 \mod 4 \)  but  \( E_{\beta} = 1 \mod 4 \)  [44]. This means that a plaquette-centered corner would contribute zero charge, while a vertex-centered corner would contribute a charge of  \( \pm1/8 \mod 1 \) . Therefore, whether a HOTI is deemed trivial or non-trivial depends on what high symmetry point o is chosen for the corner and disclination cores. Furthermore, one can show that even the simplest model, the one-band square lattice tight-binding model has  \( E_{\beta} = 1 \mod 4 \)  and  \( E_{\alpha} = 0 \mod 4 \)  at full filling. Therefore, we avoid making the binary distinction between trivial and non-trivial insulators.

In previous studies of QIs, quantized  \( \frac{1}{2} \)  corner charge is calculated in the parameter range  \( \left|\frac{t_{1}}{t_{2}}\right|<1 \) . Within the framework of TQFT, this is equivalent to asserting that  \( E_{\beta}=2\mod4 \)  within this parameter range as dictated by Eq. (29).

## VIII. DISCUSSION

In this paper, we have explored how topological invariants, specifically the discrete shift  \( E_{o} \)  and the electric polarization  \( \vec{S}_{o} \) , manifest in the boundary and corner charges of crystalline Chern insulators. Our main result, the full charge response in Eq. (3), provides a unified framework for understanding the contributions to boundary and corner charges as arising from a combination of the topological invariants  \( \{C,\nu,\mathcal{E}_{o},\vec{\mathcal{P}}_{o}\} \) .

Importantly, our theory is applicable to systems with gapless boundaries such as Chern insulators, where traditional approaches to defining polarization are often problematic. By properly defining the full boundary charge modulo 1, we circumvent these issues and provide a consistent definition of a topologically protected polarization  \( \vec{S}_{o} \)  even in the presence of the gapless edge mode.

One of our key insights from our work is that the boundary charge and the charge associated with bulk defects such as disclination and dislocations can be treated on a equal footing. Specifically, we have used the same geometrical measure  \( \Gamma \)  and  \( \vec{L}_{o} \)  which applies to both bulk defects and boundary.

As an application of our result, our charge response naturally describes the corner charges in higher-order topological insulators. We find that the discrete shift  \( E_{o} \)  fully accounts for the corner charges, contrary to the multipolar moments which is widely used in the literature.

Though in this paper we focus on the square lattice, which has  \( C_{4} \)  rotational point group symmetry, our results naturally extend to other point group symmetries  \( C_{M} \)  for M = 2, 3, 6. Note that for the M = 6 case, the polarization is quantized to a single trivial value [33].

We can also use our methods to define an electric polarization for Chern insulators in the case of no point group symmetry, M = 1. In this case, we can pick any
 
![](./images/1050657912365514763_24.jpg)

FIG. 13. Square lattice on a cylinder with MWPs  \( \{\alpha,\beta,\gamma_{1},\gamma_{2}\} \)  labeled explicitly.

point o in the unit cell, and we must not allow corners and disclinations since their response relies on rotational symmetry, so we are limited to geometries without corners. To use our formulas, we then need to define  \( n_{W,o} \)  for any point o in the unit cell. This can be done by independently computing the polarization in the case of C = 0 using the localized Wannier functions, and then fitting to the formula for  \( Q_{W} \)  to obtain  \( n_{W,o} \) . However this procedure requires a notion of distance between the origin o and the Wannier orbitals, and this information does not come directly from the Hamiltonian, but rather needs to come from additional input about the system being described.

We close by pointing out interesting future directions. First, it is important to understand the relationship between the many-body electric polarization defined here for Chern insulators and the one defined in [48], which required an arbitrary choice of origin in the Brillouin Zone and used the single-particle Berry phase theory of polarization. Furthermore, it is important to further study  \( \delta_{o} \)  and  \( \bar{\mathcal{P}}_{o} \)  in the fractional Chern insulators. These were studied using topological field theory methods in Refs. [33, 41]. Given the anyon data and the M fold point group symmetry, these  \( \delta_{o} \)  and  \( \bar{\mathcal{P}}_{o} \)  could further fractionalize. These symmetry fractionalization data are encapsulated in the spin vector s and the discrete torsion vector  \( \vec{t} \) . They also manifest as the charge response of the bulk defects and boundaries and could in principle be extracted in microscopic models using similar methods.

## ACKNOWLEDGMENTS

We thank Naren Manjunath for discussions, comments on the draft, and collaboration on related work. This work is supported by NSF DMR-2345644 and by NSF QLCI grant OMA-2120757 through the Institute for Robust Quantum Simulation (RQS).

## Appendix A: C = 0 calculation of the unit cell measure  \( \vec{n}_{o} \) ,  \( m_{o} \) 

When C = 0 the system can be adiabatically connected to an atomic insulator in which the electron wave function consists of localized Wannier orbitals placed at the maximal Wyckoff positions.  \( \bar{\mathcal{P}}_{o} \) ,  \( \delta_{o} \)  can be analytically calculated in such a state in terms of the classical charge distribution. In this section we use this fact to calculate  \( \vec{n}_{o} \)  and  \( m_{o} \)  by fitting to the charge response equation.

In the discussion below we only discuss the  \( C_{4} \)  symmetric unit cell but the whole calculation can be straightforwardly generalized to  \( C_{2}, C_{3}, C_{6} \)  symmetric unit cells. We denote the positive integers  \( N_{o} \)  as the number of filled orbitals at the MWPs  \( o \in \{\alpha, \beta, \gamma\} \) . As derived in [44],  \( \delta_{o} \)  for the  \( C_{4} \)  symmetric MWPs  \( \{\alpha, \beta\} \)  can be expressed as

 \[ \begin{aligned}\delta_{\alpha}&=N_{\alpha}\mod4,\\\delta_{\beta}&=N_{\beta}\mod4,\end{aligned} \quad (A1) \] 

and  \( \bar{\mathcal{P}}_{o} \)  is expressed as, modulo 1,

 \[ \begin{aligned}\bar{\mathcal{P}}_{\alpha}&=\frac{N_{\beta}+N_{\gamma}}{2}(1,1)\\\bar{\mathcal{P}}_{\beta}&=\frac{N_{\alpha}+N_{\gamma}}{2}(1,1)\end{aligned} \quad (A2) \] 

We first calculate  \( \vec{n}_{o}=(n_{o,x},n_{o,y}) \) . Consider a C=0 model defined on a cylinder shown in Fig. 13. The charge response is of the form

 \[ Q_{W}=\vec{L}_{o}\cdot\vec{\mathcal{P}}_{o}+\nu(k+\vec{L}_{o}\cdot\vec{n}_{o})\mod1, \quad (A3) \] 

Plugging in Eq. (A2), and  \( \nu = N_{\alpha} + N_{\beta} + 2N_{\gamma} \) ,  \( k = 3L_{y} \) , we have

 \[ \begin{align*}Q_{W}=&L_{y}[\frac{N_{\beta}+N_{\gamma}}{2}+(N_{\alpha}+N_{\beta}+2N_{\gamma})(3+n_{\alpha,y})]\mod1\\=&L_{y}[\frac{N_{\alpha}+N_{\gamma}}{2}+(N_{\alpha}+N_{\beta}+2N_{\gamma})(3+n_{\beta,y})]\mod1\end{align*} \quad (A4) \] 

On the other hand, by explicit counting of the orbitals in Fig. 13,

 \[ Q_{W}=L_{y}[3N_{\alpha}+(3+1/2)N_{\beta}+(3+3+1/2) N_{\gamma}]\mod1 \quad (A5) \] 

Plugging in Eq. (A4), we can solve for  \( n_{o,y} \) . For generic  \( L_{y} \in Z \) 

 \[ \begin{aligned}&n_{\alpha,y}=0\mod1\\&n_{\beta,y}=1/2\mod1,\\ \end{aligned} \quad (A6) \] 

and  \( n_{o,x} = n_{o,y} \)  for  \( o = \{\alpha, \beta\} \)  because of the  \( C_{4} \)  symmetry.

Note that in order to define  \( \delta\Phi_{W,o} \) , we need to know  \( \vec{n}_{o} \)  absolutely instead of modulo 1. To resolve this, we can simply pick an arbitrary lift to  \( R^{2} \) . Our choice is

 \[ \begin{aligned}\vec{n}_{\alpha}&=(0,0)\\\vec{n}_{\beta}&=(1/2,1/2).\end{aligned} \quad (A7) \]
 
![](./images/1050657912365514763_25.jpg)

![](./images/1050657912365514763_26.jpg)

FIG. 14. (a)(b) Inserting a trivial defect by removing a site at the core of a pure  \( \omega = \beta \)  disclination.  \( n_{W,\beta} = 3 \)  before and after inserting the trivial defect. (c)(d) Inserting a trivial defect by removing three sites at the core of a pure  \( \omega = \alpha \)  disclination.  \( n_{W,\beta} = 6\frac{3}{4} \)  before and after inserting the trivial defect.

This recovers the  \( \vec{n}_{o} \)  entry in Tab. I. We could pick a different lift:  \( \vec{n}_{o} \rightarrow \vec{n}_{o}+\vec{v} \)  for an integer vector  \( \vec{v} \) . Under this choice,  \( n_{W,o} \rightarrow n_{W,o}+\vec{v} \cdot \vec{L}_{o} \)  and  \( \delta\Phi_{W,o} \rightarrow \delta\Phi_{w,o} - \phi\vec{v} \cdot \vec{L}_{o} \)  so that  \( \nu n_{W,o} + \frac{C}{2\pi}\delta\Phi_{W,o} \rightarrow \nu n_{W,o} + \frac{C}{2\pi}\delta\Phi_{W,o} + \vec{v} \cdot \vec{L}_{o}\kappa \) , where the shift  \( \vec{v} \cdot \vec{L}_{o}\kappa \)  is an integer. Therefore, the invariants extracted using Eq. (3) are unchanged under this change of lift.

Next, we calculate  \( m_{o} \) . One could perform a similar calculation to that of  \( \vec{n}_{o} \)  as above, and obtain  \( m_{\alpha} = 1 \)  and  \( m_{\beta} = 0 \) . Here, we provide a more geometrically illuminating solution.

In Sec. V, we have argued that a ribbon with  \( \Omega_{cor} \)  total corner angle can be seen as a disclination with  \( 2\pi + \Omega_{cor} \)  disclination angle, and vice versa. Consider two  \( \Omega = \frac{\pi}{2} \)  pure disclinations with holes in the middle shown in Fig. 14 for  \( o = \{\alpha, \beta\} \) . They are created by removing sites from the disclination core which amounts to inserting trivial defects. During this process, the number of unit cells within the region W defined in the figure does not change. We treat Fig. 14 (b), (d) as having three corners with corner angle  \( -\pi/2 \)  each, and total corner

[1] X.-G. Wen, Physical Review B 65, 165113 (2002).

[2] X.-G. Wen, Quantum Field Theory of Many-Body Systems (Oxford Univ. Press, Oxford, 2004).

[3] M. Z. Hasan and C. L. Kane, Rev. Mod. Phys. 82, 3045 (2010).

[4] L. Fu, Physical review letters 106, 106802 (2011).

angle  \( \Omega_{cor} = -\frac{3\pi}{2} \) . Now we solve for  \( m_{o} \)  by matching the fractional part of  \( n_{W,o} \) .

 \[ \begin{aligned}\vec{L}_{\beta}\cdot\vec{n}_{\beta}+\frac{3}{4}m_{\beta}&=3\mod1\\\vec{L}_{\alpha}\cdot\vec{n}_{\alpha}+\frac{3}{4}m_{\alpha}&=6\frac{3}{4}\mod1.\end{aligned} \quad (A8) \] 

Since both disclinations are pure with trivial Burgers vector,  \( \vec{L}_{o} \)  is also in the trivial class, and therefore  \( \vec{n}_{o} \)  does not contribute to fractional part of  \( n_{W,o} \) . Therefore, we have

 \[ \begin{aligned}&m_{\beta}=0\mod4/3\\&m_{\alpha}=1\mod4/3\end{aligned} \quad (A9) \] 

Eq. (A9) determines  \( m_{o} \)  modulo 4/3. Now consider a trivial defect on a clean lattice shown in Fig. 10 where the hole consists of 4 corners with total corner angle  \( -2\pi \)  and no fractional unit cell, therefore we have

 \[ \begin{aligned}&m_{\beta}=0\mod1\\&m_{\alpha}=0\mod1,\\ \end{aligned} \quad (A10) \] 

Together with Eq. (A9), we are able to determine  \( m_{\beta} \)  modulo  \( lcm(\frac{4}{3},1)=4 \) , where lcm is the lowest common multiple:

 \[ \begin{aligned}&m_{\beta}=0\mod4\\&m_{\alpha}=1\mod4.\\ \end{aligned} \quad (A11) \] 

Again, in order to define  \( \delta\Phi_{W,o} \) , we need to know  \( m_{o} \)  absolutely, and this requires picking a lift to Z, our choice is

 \[ \begin{aligned}&m_{\beta}=0\\&m_{\alpha}=1.\\ \end{aligned} \quad (A12) \] 

This reproduces the  \( m_{o} \)  entry in Tab. I. Similar to  \( \vec{n}_{o} \) , upon picking a different lift  \( m_{o} \rightarrow m_{o} + 4r \)  for a integer r. Under this choice,  \( n_{W,o} \rightarrow n_{W,o}+r\frac{C}{2\pi} \)  and  \( \delta\Phi_{W,o} \rightarrow \delta\Phi_{w,o}-\phi r\frac{C}{2\pi} \)  so that  \( \nu n_{W,o}+\frac{C}{2\pi}\delta\Phi_{W,o} \rightarrow \nu n_{W,o}+\frac{C}{2\pi}\delta\Phi_{W,o}+r\frac{C}{2\pi}\kappa \) , where the shift  \( r\frac{C}{2\pi} \)  is an integer. Therefore, the invariants extracted using Eq. (3) are unchanged under this change of lift.

[5] M. Barkeshli and X.-L. Qi, Phys. Rev. X 2, 031013 (2012), arXiv:1112.3311.

[6] A. M. Essin and M. Hermele, Phys. Rev. B 87, 104406 (2013).

[7] A. M. Essin and M. Hermele, Phys. Rev. B 90, 121102 (2014).
 

[8] M. Barkeshli, P. Bonderson, M. Cheng, and Z. Wang, Phys. Rev. B 100, 115147 (2019), arXiv:1410.4540.

[9] W. A. Benalcazar, J. C. Y. Teo, and T. L. Hughes, Phys. Rev. B 89, 224503 (2014).

[10] Y. Ando and L. Fu, Annu. Rev. Condens. Matter Phys. 6, 361 (2015).

[11] Y. Qi and L. Fu, Phys. Rev. Lett. 115, 236801 (2015).

[12] H. Watanabe, H. C. Po, A. Vishwanath, and M. Zaletel, Proceedings of the National Academy of Sciences 112, 14551 (2015).

[13] H. Watanabe, H. C. Po, M. P. Zaletel, and A. Vishwanath, Physical review letters 117, 096404 (2016).

[14] C.-K. Chiu, J. C. Y. Teo, A. P. Schnyder, and S. Ryu, Rev. Mod. Phys. 88, 035005 (2016).

[15] M. Hermele and X. Chen, Phys. Rev. X 6, 041006 (2016).

[16] M. Barkeshli, P. Bonderson, M. Cheng, C.-M. Jian, and K. Walker, Communications in Mathematical Physics (2019), 10.1007/s00220-019-03475-8, arXiv:1612.07792.

[17] M. P. Zaletel, Y.-M. Lu, and A. Vishwanath, Phys. Rev. B 96, 195164 (2017).

[18] H. C. Po, A. Vishwanath, and H. Watanabe, Nature Communications 8 (2017), 10.1038/s41467-017-00133-2.

[19] H. Song, S.-J. Huang, L. Fu, and M. Hermele, Phys. Rev. X 7, 011020 (2017).

[20] S.-J. Huang, H. Song, Y.-P. Huang, and M. Hermele, Phys. Rev. B 96, 205106 (2017).

[21] K. Shiozaki, H. Shapourian, and S. Ryu, Physical Review B 95 (2017), 10.1103/physrevb.95.205139, arXiv:1609.05970 [cond-mat.str-el].

[22] J. Kruthoff, J. de Boer, J. van Wezel, C. L. Kane, and R.-J. Slager, Phys. Rev. X 7, 041069 (2017).

[23] B. Bradlyn, L. Elcoro, and e. a. Jennifer Cano, Nature 547, 298 (2017).

[24] F. Schindler, A. M. Cook, M. G. Vergniory, Z. Wang, S. S. P. Parkin, B. A. Bernevig, and T. Neupert, Science Advances 4, eaat0346 (2018).

[25] H. Watanabe and M. Oshikawa, Physical Review X 8 (2018), 10.1103/physrevx.8.021065.

[26] G. van Miert and C. Ortix, Phys. Rev. B 97, 201111 (2018).

[27] E. Khalaf, H. C. Po, A. Vishwanath, and H. Watanabe, Physical Review X 8, 031070 (2018).

[28] R. Thorngren and D. V. Else, Phys. Rev. X 8, 011040 (2018).

[29] F. Tang, H. C. Po, A. Vishwanath, and X. Wan, Nature 566, 486 (2019).

[30] S. Liu, A. Vishwanath, and E. Khalaf, Phys. Rev. X 9, 031003 (2019).

[31] Z. Song, C. Fang, and Y. Qi, Nature Communications 11 (2020), 10.1038/s41467-020-17685-5.

[32] T. Li, P. Zhu, W. A. Benalcazar, and T. L. Hughes, Phys. Rev. B 101, 115115 (2020).

[33] N. Manjunath and M. Barkeshli, Phys. Rev. Research 3, 013040 (2021).

[34] N. Manjunath and M. Barkeshli, “Classification of fractional quantum hall states with spatial symmetries,” (2020), arXiv:2012.11603 [cond-mat.str-el].

[35] J. Cano and B. Bradlyn, Annual Review of Condensed Matter Physics 12, 225 (2021).

[36] L. Elcoro, B. Wieder, Z. Song, Y. Xu, B. Bradlyn, and B. A. Bernevig, Nature Communications 12 (2021), https://doi.org/10.1038/s41467-021-26241-8.

[37] N. Manjunath, V. Calvera, and M. Barkeshli, Phys. Rev. B 107, 165126 (2023).

[38] J. Herzog-Arbeitman, B. A. Bernevig, and Z.

D. Song, “Interacting topological quantum chemistry in 2d: Many-body real space invariants,” (2022), arXiv:2212.00030 [cond-mat.str-el].

[39] Y. Zhang, N. Manjunath, G. Nambiar, and M. Barkeshli, Phys. Rev. Lett. 129, 275301 (2022).

[40] Y. Zhang, N. Manjunath, R. Kobayashi, and M. Barkeshli, Physical Review Letters 131, 176501 (2023).

[41] N. Manjunath, V. Calvera, and M. Barkeshli, Phys. Rev. B 109, 035168 (2024).

[42] S. Sachdev, Quantum Phases of Matter (Cambridge University Press, 2023).

[43] R. Kobayashi, Y. Zhang, Y.-Q. Wang, and M. Barkeshli, “(2+1)d topological phases with rt symmetry: many-body invariant, classification, and higher order edge modes,” (2024), arXiv:2403.18887 [cond-mat.str-el].

[44] Y. Zhang, N. Manjunath, G. Nambiar, and M. Barkeshli, “Quantized charge polarization as a many-body invariant in  \( (2+1) \) d crystalline topological states and hofstadter butterflies,” (2022), 2211.09127.

[45] N. Manjunath, V. Calvera, and M. Barkeshli, Phys. Rev. B 109, 035168 (2024).

[46] R. Kobayashi, Y. Zhang, N. Manjunath, and M. Barkeshli, “Crystalline invariants of fractional chern insulators,” (2024), arXiv:2405.17431 [cond-mat.str-el].

[47] X.-Y. Song, Y.-C. He, A. Vishwanath, and C. Wang, Phys. Rev. Research 3, 023011 (2021).

[48] S. Coh and D. Vanderbilt, Phys. Rev. Lett. 102, 107603 (2009).

[49] C. Fang, M. J. Gilbert, and B. A. Bernevig, Phys. Rev. B 86, 115112 (2012).

[50] W. A. Benalcazar, T. Li, and T. L. Hughes, Phys. Rev. B 99, 245151 (2019).

[51] N. Manjunath, A. Prem, and Y.-M. Lu, Phys. Rev. B 107, 195130 (2023).

[52] P. Rao and B. Bradlyn, Phys. Rev. B 107, 195153 (2023).

[53] J. May-Mann and T. L. Hughes, Phys. Rev. B 106, L241113 (2022).

[54] W. A. Benalcazar, B. A. Bernevig, and T. L. Hughes, Science 357, 61 (2017), https://www.science.org/doi/pdf/10.1126/science.aah6442.

[55] B. Roy and V. Juričić, Phys. Rev. Res. 3, 033107 (2021).

[56] M. R. Hirsbrunner, A. D. Gray, and T. L. Hughes, "Crystalline-electromagnetic responses of higher order topological semimetals," (2023), arXiv:2308.05796 [cond-mat.mes-hall].

[57] E. Khalaf, Physical Review B 97, 205136 (2018).

[58] A. Jahin, Y.-M. Lu, and Y. Wang, Phys. Rev. B 109, 205123 (2024).

[59] M. Barkeshli, Y.-A. Chen, P.-S. Hsin, and N. Manjunath, Phys. Rev. B 105, 235143 (2022).

[60] R. Dijkgraaf and E. Witten, Comm. Math. Phys. 129, 393 (1990).

[61] X. Chen, Z.-C. Gu, Z.-X. Liu, and X.-G. Wen, Phys. Rev. B 87, 155114 (2013).

[62] X. G. Wen and A. Zee, Phys. Rev. Lett. 69, 953 (1992).

[63] A. G. Abanov and A. Gromov, Phys. Rev. B 90, 014435 (2014).

[64] A. Gromov, G. Y. Cho, Y. You, A. G. Abanov, and E. Fradkin, Phys. Rev. Lett. 114, 016805 (2015).

[65] A. Gromov, K. Jensen, and A. G. Abanov, Phys. Rev. Lett. 116, 126802 (2016).
 
