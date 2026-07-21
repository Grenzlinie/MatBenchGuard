# Random bearings and their stability
R. Mahmoodi Baram* and Hans J. Herrmann†

Institute for Computational Physics, University of Stuttgart Pfaffenwaldring 27, 70569 Stuttgart, Germany
(Dated: July 2, 2018)

Self-similar space-filling bearings have been proposed some time ago as models for the motion of tectonic plates and appearance of seismic gaps. These models have two features which, however, seem unrealistic, namely, high symmetry in the arrangement of the particles, and lack of a lower cutoff in the size of the particles. In this work, an algorithm for generating random bearings in both two and three dimensions is presented. Introducing a lower cutoff for the sizes of the particles, the instabilities of the bearing under an external force such as gravity are studied.

PACS numbers: 03.20.+i,02.20.+b,03.40.Gc,91.45.Dh

The term seismic gap refers to any region along an active geological plate boundary that has not experienced a large thrust or strike-up earthquake for more than 30 years [1]. Plate tectonic theory uses the concept of seismic gaps to provide very rough estimates on the location and magnitude likeliness of earthquakes. The tectonic plates usually tend to move relative to each other due to the earth's internal convection, but the large friction between the boundaries hinders a continuous sliding which would be several centimeters per year and leads to accumulation of stress over the course of time. Beyond a critical point the accumulated stress is released resulting in big shocks and large relative motions of the plates of up to $20m$. Figure 1 demonstrates San Andreas fault and nearby geological structure and how different tectonic plates move relatively.

![](./images/867745317515165912_1.jpg)

FIG. 1: San Andreas fault and nearby geological structure. Different tectonic plates move relatively.

In some faults, like that of San Andreas, tectonic plates have been moving for a long time (thousands of years) without any significant earthquake or production of heat as it is expected for the processes involving rubbing rough surfaces. The understanding of these seismic gaps is one of the big challenges in geophysics. Space-filling bearings were introduced more than a decade ago for the first time as a simplified model for explaining this phenomenon[2, 3]. In this model, it is assumed that the space between the tectonic plates is filled with more or less round particles which, as the plates move, may roll on each other resulting in the spontaneous formation of local bearings and reducing the amount of friction and dissipation of energy. The spontaneous formation of bearings has been evidenced to be possible in Molecular Dynamics simulations of shear bands [4], supporting the model. Using techniques based on conformal mapping, originally self-similar space-filling bearings in two dimensions were proposed. They are stripes completely filled with an infinite number of discs of different sizes. Following the same line, three dimensional packing of spheres has been recently constructed. Although the dynamics of bearings in three dimensions is more complicated than in two dimensions due to higher degrees of freedom, it has been shown that the necessary and sufficient condition for a packing of spheres to be a bearing is to be bi-chromatic [6]. In other words, only two colors are needed for coloring all spheres in such a way that no spheres of the same color touch each other.

There are two major criticisms which have been raised about such bearings. First, due to the nature of the construction algorithm the location of the particles are very specific which makes such bearings very unlikely to occur in nature. Second, the space is completely filled with particles of different sizes down to infinitely fine grains, whereas in the reality there exists always a minimum size of the particles. The present work is focused on constructing random bearings and studying the effect of cutoffs for the size of the particles on the stability of the system. In the following, an algorithm for constructing random bearings in both two and three dimensions is presented. In the construction procedure, the formation of odd loops is avoided by imposing the bi-chromatic condition. Next, the instability of the configurations as a consequence of setting a cutoff is discussed and calculations for the dissipation of energy in a system with rotating particles under gravity are presented. One can

![](./images/867745317515165912_2.jpg)

FIG. 2: The method for construction of a bi-chromatic pack-
ing: If all three discs are of the same color (left image) a disc
is inserted with opposite color touching all three, otherwise
its size is reduced by a factor $\alpha$ so that it only touches the
two that have the same color (right image).

see, that the energy dissipation decreases as the cutoff
is reduced. Finally a discussion of the results and the
conclusion is given.

The algorithm can be divided in two parts. First we
construct a general random packing of discs or spheres.
Second we impose the bi-chromatic condition which im-
plicitly guarantees the packing to contain no odd loops
and, therefore, be a bearing [6]. Initially, some discs
within a given range of sizes are randomly distributed
in space without touching each other. The filling proce-
dure is continued from then on by inserting always the
biggest possible disc into the system without overlapping
with any existing disc. This is the most efficient way of
filling the space starting from a given initial configura-
tion of discs. This becomes more obvious as the local
configurations are observed to be close to that of clas-
sic Apollonian which is the most efficient known way of
packing discs. For finding the biggest hole where a new
disc can be inserted, an arbitrary disc $A$ from the cur-
rent configuration is chosen and all possible neighboring
pairs are examined between which a disc can be inserted
touching all three without overlapping any other disc in
the system. In this way, the locally biggest disc is found
and set as the candidate to be inserted next into the sys-
tem. This disc will touch the initially chosen disc $A$ and
two others, namely, $B$ and $C$. To find the final candi-
date we check whether the current candidate is also the
biggest for $B$ and $C$. In other words, discs $B$ and $C$
are examined as was disc $A$. If a bigger disc is found
the candidate for being inserted next is updated. Con-
tinuing this search, the biggest disc can be finally found
and inserted. More discs are packed into the system by
repeating the same procedure over and over. One no-
tices that as the density increases, different regions of
the packing become independent. Therefore one doesn’t
need to look for the globally biggest disc each time and
the search can be stopped after a few iterations.

So far no considerations have been made for the pack-
ing to act as a bearing. As the consequence, there will
be many odd loops in the packing which will hinder any
frictionless rotation of the discs. The bearing condition,
however, can be easily implemented into the algorithm.
The system is initialized as before except that the initial
discs are also assigned randomly with two colors. A new
disc, gets a color such that it doesn’t touch any disc with
the same color. This is only possible if all three touch-
ing discs have the same color. In other cases, where only
two of the discs have the same colors, the radius of the
inserted disc is reduced by a factor $\alpha$ with respect to the
size which would make it touch to all three:

$$
r = \alpha r_0, \tag{1}
$$

where $r_0$ is the size of the biggest possible and $r$ is the size
of inserted disc as shown in figure 2. For $\alpha = 1$ a random
packing is obtained which is not a bearing. Therefore,
for any $\alpha$ less than unity one obtains a bearing.

Similarly, random packings and bearings can be ob-
tained in three dimensions with this method. The differ-
ence to two dimensions is that each new sphere is inserted
touching four spheres. To construct a bearing three sit-
uations should be considered, that is, among the four
spheres one is of one color and three of the other color,
two are of one color and two of the other or all three
have the same color. Figure 3 shows a resulting bearing
in three dimensions for $\alpha = 0.6$.

From both the computational point of view and that
of what happens in reality, a smallest particle size must
inevitably exist. The main consequence of this cutoff $\varepsilon$
are unfilled spaces which may cause instabilities in the
system under external forces. In other words, the par-
ticles may no longer be fixed in their positions, causing
changes in the configuration. As we will see, this plays
an important role in the dynamics of the bearing. Here
in particular we will study the effect of gravity on the
system. In a random bearing with a cutoff, the particles
which are not supported from below will be displaced by
gravity, resulting eventually in the formation of odd loops
in the system. In an odd loop at least one frustrated con-
tact will form as the particles are forced to rotate. These
are sources for local dissipation of energy and the system
will not act as perfect bearing anymore.

The stability of the system depends on how loose it is
before applying the gravity. Here, we make an estimate
for the total dissipated energy in the system. Assuming
that the friction acting between two rubbing surfaces fol-
lows Coulomb’s law, at a frustrated contact, the amount
of energy dissipated per unit time is,

$$
\mathcal{E}_{dis} = \mu N v_{rel}, \tag{2}
$$

where $\mu$ is the Coulomb friction coefficient, $v_{rel}$ is the
relative velocity of the surfaces of the particles at the
frustrated contact, and $N$ is the normal force acting be-
tween them. As can be easily verified, the normal force
$N$ is proportional to the weight of the dislocated particle.
The proportionality factor is a function of the angles be-
tween normal forces at the contacts of a particle and the

![](./images/867745317515165912_3.jpg)

FIG. 3: Three dimensional random bearing. No two spheres of the same color touch each other.

gravity direction. In both two and three dimensions, we assume for all frustrated contacts a typical value for this factor. It should be noted that in two dimensions the rel- ative tangential contact velocity is exactly the same for all contacts, zero for unfrustrated and non-zero for frus- trated ones, since all touching pairs of discs can rotate either in the same or in opposite direction. Therefore, we can describe the total dissipation of energy as pro- portional to the total mass of dislocated particles thatproduce frustrated loops:

$$
\mathcal{E}_{\text {total }} \sim \mathcal{M}, \quad \text { (3) }
$$

which we will consider as the measure for the deviation from a perfect bearing.

To check the effect of gravity on the system, we use a semi-dynamics which is an extention of the one used by Manna et al [7] to simulate discs under gravity. The particles which don't have enough contacts (at least two in two dimensions and three in three dimensions) to carry their weight will either fall freely or role on one another. A particle is fixed if the line starting at the center of the particle and going in direction of gravity cuts at least one line (triangle) made by connecting two (three) contacts in two (three) dimensions. The process of falling and rolling is performed on all particles one at a time while others are held fixed. Those particles which are in a lower position are treated first and the upper ones later. The programm goes through the list of particles several times and lets them fall and roll until no particle moves further. In this way, the system reaches the final state from which $\mathcal{M}$ the total mass of particles forming frustrated contact can be calculated.

Here, we present the calculation for a two-dimensional system. Figure 4 shows a two dimensional random bear- ing. Applying gravity, some particles move and form frus- trated contacts. These are shown as black discs. Solid lines show the frustrated contacts. The total frustrated mass $\mathcal{M}$ is computed as function of the cutoff $\varepsilon$ for differ ent configurations. The result is shown in Fig. 5(a) for two values of $\alpha$. The data points are fitted best by power law functions $\mathcal{M} \sim \varepsilon^{\gamma}$. The results indicate that the system approaches the state of complete stability, that is $\mathcal{M}=0$, as $\varepsilon \to 0$.

Figure 5(b) shows the calculated exponent $\gamma$ as func tion of $\alpha$. It can be seen that the exponent $\gamma$ is more or less independent of $\alpha$ having the value approximately0.72. In other words, the way in which the packings are constructed does not play an important role in the obtained results. It should be stressed that the fractal dimension of the packings turns out to be also the same for all values of $\alpha$ within the computational error.

We propose to study experimentally the energy dis-

![](./images/867745317515165912_4.jpg)

FIG. 4: Two dimensional random bearing with $\alpha = 0.6$. Applying gravity, some particles move and form frustrated contacts. These are shown as black discs. Solid lines show the frustrated contact.

sipation of a polydisperse mixture of circular discs in a Couette cell as used by Veje et al. [8] changing the cut-off of the size distribution.

All space-filling bearings, which have been studied in the past, were highly organized arrangements of particles and there was no lower cutoff on the size of the particles in such bearings. These were two main drawbacks in modeling natural phenomena, like tectonic plate motion. Here, an algorithm has been presented for producing space-filling bearings in which the particles do not follow any regular pattern. We also investigated the stability of bearings with a finite cutoff under gravity and showed that as the system has less porosity less energy is dissipated. The energy dissipation rate follows a power law behavior with respect to the cut-off on the size of the particles.

We would like to thank M. Strauß and M. Wackenhut for useful discussions.

* reza@ica1.uni-stuttgart.de
† hans@ica1.uni-stuttgart.de

[1] W.McCann, S. Nishenko, L. Sykes, and J. Krause, Pure Appl. Geophys. 117, 1082 (1979); C. Lomnitz, Bull. Seis- mol. Soc. Am. 72, 1441 (1982).

[2] H.J. Herrmann, G. Mantica, and D. Bessis, Physical Re- view Letters 65, 3223, 1990.

[3] G. Oron, and H.J. Herrmann, Generalization of space- filling bearings to arbitrary loop size, J. Phys. A: Math.

![](./images/867745317515165912_5.jpg)

FIG. 5: (a) Frustrated mass $\mathcal{M}$ as function of the cutoff $\varepsilon$ for two dimensional bearings for $\alpha=0.5$ and 0.8. Lines are different power law fits, with exponent $\gamma=$ 0.74 and 0.71 correspondingly. (b) Exponent $\gamma$ as function of $\alpha$.

Gen 33, 1417-1434, 2000.

[4] J.A. Åström, H.J. Herrmann, and J. Timonen, Physical Review Letters 84, 638, 2000.

[5] R. Mahmoodi Baram, H. J. Herrmann, Self-similar space- filling packings in three dimensions, Fractals 12, 293, 2004.

[6] R. Mahmoodi Baram, H.J. Herrmann, and N. Rivier, Space fillig bearing in three dimensions. Phys. Rev. Lett. 92, 044301, 2004.

[7] S.S. Manna and H.J. Herrmann, Eur. Phys. J. E 1, 341-344, 2000.

[8] C.T. Veje, D.W. Howell, and R. P. Behringer. Kinematics of a 2D granular Couette experiment at the transition to shearing. Phys. Rev. E 59(1), 739-745, 1999.