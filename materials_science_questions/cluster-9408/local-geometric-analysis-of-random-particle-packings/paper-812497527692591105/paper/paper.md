# Non-overlapping coverage in random feeding

Pingping Wen *, Guus Lohlefink, Peter Rem

Faculty of Civil Engineering and Geosciences, Delft University of Technology, Stevinweg 1, 2628, CN, Delft, the Netherlands

---

## A R T I C L E  I N F O

**Article history:**
Received 3 September 2020
Received in revised form 10 February 2021
Accepted 21 February 2021
Available online 26 February 2021

**Keywords:**
Overlap probability
Non-overlapping coverage
Sensor-based sorting
Random deposition
Dense feeding

---

## A B S T R A C T

Can random deposition create dense non-overlapping material feeding? The question is very fundamental for the research of particle packing, while the answer is of great importance for any industrial process that applies single object operation. To gain an insight into this issue, we studied the overlap problems of convex particles in the manner of uniformly random deposition. The overlap probability of two convex particles with arbitrary shapes and sizes is formulated, and the coverage fractions of free particles and sticking particles (particles of the bottom layer) are precisely predicted. Simulations with rectangular particles verified the theory. Surprisingly, free particles can only occupy less than 7.5% of the plane area, much smaller than what is intuitively expected. Sticking particles, however, can easily cover 19%, a factor of 2.5 times larger. The finding is of great value for applications that need to create dense non-overlapping feeding.

© 2021 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/).

---

## 1. Introduction

Sustainability in utilizing resources is gaining overwhelming importance in society. To achieve this goal, intelligent and automatic production processes are essential. Sorting processes, for instance, are no longer based on coarse, binary classification anymore, and instead, deep sorting is increasingly being asked in the level of single object operation, especially in small scales [1,2]. To distinguish every single object, the objects must be placed separate from each other, so that smart and accurate recognition methods, such as laser-induced breakdown spectroscopy (LIBS) [3,4] and hyperspectral-imaging analysis can be applied [5–7]. A commonly used method to obtain such an object feeding is to let the materials flow pass through a vibrator before the objects are transported to a conveyor belt or a tilted chute [2]. However, when the objects are less spherical but flat and thin, for instance, the crushed mineral particles [8,9], wood chips [10], and shredded plastic flakes [6], overlaps between objects are almost inevitable and thus greatly limit the efficiency of sorting processes. The issue is unavoidable especially for small particles, while the single object sorting shows significant advantages in dealing with small particles owing to the high purity of the object when shredded into small size.

However, the effect of overlaps on free particle coverage fraction in materials feeding has been rarely studied. The most related work on overlapping of many objects are the birthday problem [11] and wireless networking [12]. A physical model of the overlap probability of circles with uniformly and non-uniformly random distributions is built to address these problems [13]. However, the model did not consider the shape factor and in practice, particles in sorting processes involve all kinds of shape. Moreover, for the industry, the most interesting issue is whether random deposition can produce a dense feeding of particles, or in other words, how much area fraction the free particles can obtain. To answer this question, a general model that describes the random feeding process of arbitrarily shaped particles is necessary.

In this paper, we studied the random deposition process of particles with arbitrary shapes and sizes in a big plane area. Juneja and Mandjes already implied that uniform distribution would obtain the biggest non-overlapping probability [13]. Uniform distribution is also preferred and more or less the real situation in industry, where efforts are always made to distribute the particles all over the plane area as even as possible. So in this paper, we chose to drop the particles in the manner of uniform random deposition. Below, we first calculate the overlap probability of two convex particles, and then we obtain the free coverage fraction, defined as the area ratio of the free particles to the plane area after dropping a certain amount of particles, refer to the red particles in Fig. 3a. Subsequently, we derive a formula for the sticking coverage fraction, which is the fraction of the plane area that is covered by the particles that do not overlap with earlier dropped particles, at the very instant when they are dropped on the plane (shown as red particles in Fig. 3b). These particles "stick" to the plane surface and form the bottom layer. In practice, the top layers can be removed without too much difficulty and a relatively dense layer of non-overlapping particles is then achieved. A sample of HDPE particles from a recycling plant is analyzed and both the surface area and the shape factor exhibit a lognormal

---

* Corresponding author.
E-mail address: pingpingwen@outlook.com (P. Wen).

https://doi.org/10.1016/j.powtec.2021.02.068
0032-5910/© 2021 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/).

![](./images/812497527692591105_1.jpg)
![](./images/812497527692591105_2.jpg)

<table>
<thead>
<tr>
<th colspan="2">Nomenclature</th>
</tr>
</thead>
<tbody>
<tr>
<td>$s$</td>
<td>shape factor of a particle</td>
</tr>
<tr>
<td>$E$</td>
<td>number of edges of a convex particle</td>
</tr>
<tr>
<td>$\varphi$</td>
<td>orientation angle of an arbitrary particle</td>
</tr>
<tr>
<td>$\theta$</td>
<td>angle from the orientation vector to the radius vector</td>
</tr>
<tr>
<td>$\overrightarrow{e}_l$</td>
<td>direction vector of edge $l$</td>
</tr>
<tr>
<td>$\overrightarrow{e}_x$</td>
<td>direction vector of edge that parallels to the $x$-axis</td>
</tr>
<tr>
<td>$\overrightarrow{r}_l$</td>
<td>radius vector of edge $l$</td>
</tr>
<tr>
<td>$\overrightarrow{r}_0$</td>
<td>radius vector of edge that parallels to the $x$-axis</td>
</tr>
<tr>
<td>$\rho_{free}$</td>
<td>free coverage fraction</td>
</tr>
<tr>
<td>$\rho_{stick}$</td>
<td>sticking coverage fraction</td>
</tr>
<tr>
<td>$k_i$</td>
<td>probability of a particle to be type $i$</td>
</tr>
<tr>
<td>$\omega$</td>
<td>ratio of the total area of all particles to the plane area</td>
</tr>
<tr>
<td>$G(A)$</td>
<td>surface area distribution</td>
</tr>
<tr>
<td>$H(s)$</td>
<td>shape factor distribution</td>
</tr>
</tbody>
</table>

distribution. Simulations with rectangular particles are done and the results verify the predictions of the theoretical model.

## 2. Theory and simulation

### 2.1. Overlap probability of two convex particles in random deposition

In order to state the issue more precisely, we choose a standard $x,y$ coordinate system for the plane area. The plane area is assumed to have some surface area $A_{plane} = X_{plane} \times Y_{plane}$ and its dimensions $X_{plane}$ and $Y_{plane}$ are far larger than the dimensions of the particles. Furthermore, we choose to mark a "centre point" and an orientation vector of each particle so that a random drop of a particle can be defined as the selection of arbitrary two-dimensional coordinates $(x,y)$ within the plane area for the particle centre point and an arbitrary angle $\varphi$ for the angle between the particle orientation and the $x$-axis (see Fig. 1).

Now we drop two convex particles onto the plane area both at arbitrary positions and at arbitrary angles, and we calculate the probability that they will partly overlap. Since the plane area on which the particles are dropped is much larger than the particles, and the particles have the equal probability to be dropped at all positions with all orientations in the plane area, we can simply choose the first particle positioned at the center of the plane area, with its orientation vector parallel to the $x$-axis of the plane area, while the second particle is positioned randomly at position $(x,y)$ and at a random angle $\varphi$ within the plane area.

![](./images/812497527692591105_3.jpg)

Fig. 1. Dropping a particle with its "centre point" (blue dot) at an arbitrary position $(x,y)$ and at an arbitrary angle $\varphi$ of its particle orientation (blue vector) with the $x$-axis in a large plane area.

![](./images/812497527692591105_4.jpg)

Fig. 2. Part of the boundary (coarsely dashed) of the area $A_{overlap,\varphi}$ constructed by the path of the centre point of the second particle while moving around the first particle at constant orientation (thin brown arrows), while being in continuous contact. For any position of the second particle, a radius vector (finely dashed) connects the centre point of the second particle with the point of contact.

Now, we approximate the first particle by a polygon with a sufficiently large number $E$ of edges to be a realistic approximation of a convex particle. The edges have unit direction vectors $\overrightarrow{e}_l, l = 1,..., E$, running along the boundary of the polygon in the anti-clockwise direction. Suppose that the second particle has a fixed orientation $\varphi$. Then the collection of positions for the centre point of the second particle for which there is overlap with the first particle is defined by a boundary consisting of all those positions of the centre point at which the two particles are just touching each other (see Fig. 2). In order to describe that boundary, we move the second particle around the first particle in the anti-clockwise direction so that the two particles continuously touch (see Fig. 2). Suppose that the area inside this boundary has an area $A_{overlap,\varphi}$, then for the presently fixed orientation $\varphi$ of the second particle, the probability of overlap should be

$$
p_{\varphi} = \frac{A_{overlap,\varphi}}{A_{plane}} \tag{1}
$$

And the overall probability that we are looking for is

$$
p = \frac{1}{2\pi} \int_{0}^{2\pi} \frac{A_{overlap,\varphi}}{A_{plane}} \mathrm{d}\varphi \tag{2}
$$

Now we note that the area $A_{overlap,\ \varphi}$ consists of three different types of parts. One part is the area $A$ of the first particle. The second type of part is the "triangular" section shown as $B$ in Fig. 2. It is bounded by two radius vectors and a curved part of the track of the centre point of the second particle. By construction, it can be noticed that the area $B$ is the same as the part of the area of the second particle shown as $B'$ in Fig. 2. In running around the first particle, parts $B'$ are created at every corner of the polygonal first particle. Summing the parts $B'$, and therefore also the parts $B$, make up the area $A'$ of the second particle. The third type is the parallelogram-shaped part, defined by two parallel radius vectors, an edge $\overrightarrow{e}_l$ of the polygonal first particle and the straight part of the track of the centre point of the second particle that is parallel to $\overrightarrow{e}_l$. An example is the area shown as $C$ in Fig. 2. The area of this part is equal to the length $\Delta P_l$ of edge $l$ times the distance between the edge and the straight part of the track of the centre point of the second particle that is parallel to $\overrightarrow{e}_l$. This distance is equal to the size of the vector $\overrightarrow{e}_l \times \overrightarrow{r}_l(\varphi)$ (see Fig. 2).

The radius vector from the centre point of the second particle to the contact point with edge $l$ is called $\vec{r}_l(\varphi)$ because it is constant along the straight part of the track of the centre point of the second particle that is parallel to $\vec{e}_l$, and because it depends on the orientation $\varphi$ of the second particle. Since the second particle touches the polygonal first particle along edge $l$, it follows that $\vec{e}_l$ is parallel to the tangent vector $\frac{\overrightarrow{dr_l}}{d\varphi}(\varphi)$ (see Fig. 2). In other words, the area of part $C$ can be written as:

$$
A_C(\varphi)=\left| \frac{\left| \frac{dr_l}{d\varphi}(\varphi)\times\vec{r}_l(\varphi) \right|}{\left| \frac{\overrightarrow{dr_l}}{d\varphi}(\varphi) \right|} \Delta P_l \right|
\tag{3}
$$

So, the overall probability $p$ is

$$
\begin{aligned}
p=\frac{1}{2\pi}\int_{0}^{2\pi}\frac{A_{\text{overlap},\varphi}}{A_{\text{plane}}}\mathrm{d}\varphi&=\frac{A+A'}{A_{\text{plane}}}\\
&+\frac{1}{2\pi A_{\text{plane}}}\sum_l \Delta P_l \int_{0}^{2\pi}\left| \frac{\left| \frac{dr_l}{d\varphi}(\varphi)\times\vec{r}_l(\varphi) \right|}{\left| \frac{\overrightarrow{dr_l}}{d\varphi}(\varphi) \right|} \right|\mathrm{d}\varphi
\tag{4}
\end{aligned}
$$

Now we note that the integral

$$
\int_{0}^{2\pi}\left| \frac{\left| \frac{dr_l}{d\varphi}(\varphi)\times\vec{r}_l(\varphi) \right|}{\left| \frac{\overrightarrow{dr_l}}{d\varphi}(\varphi) \right|} \right|\mathrm{d}\varphi
\tag{5}
$$

involves all angles between the orientation of the second particle and edge $l$ and so it does not depend on the direction of edge $l$. Therefore, instead of $\vec{e}_l$ we can simply take $\vec{e}_x$, the direction of the $x$-axis. This means that the expression for $p$ reduces to

$$
\begin{aligned}
p=\frac{1}{2\pi}\int_{0}^{2\pi}\frac{A_{\text{overlap},\varphi}}{A_{\text{plane}}}\mathrm{d}\varphi&=\frac{A+A'}{A_{\text{plane}}}\\
&+\frac{1}{2\pi A_{\text{plane}}}\left( \sum_l \Delta P_l \right)\int_{0}^{2\pi}\left| \vec{e}_x\times\vec{r}_0(\varphi) \right|\mathrm{d}\varphi
\tag{6}
\end{aligned}
$$

where $\vec{r}_0(\varphi)$ is the radius vector to the point at the boundary of the second particle with a tangent parallel to the $x$-axis for orientation $\varphi$ of the particle axis. The resulting expression for $p$ then reduces to

$$
p=\frac{1}{2\pi}\int_{0}^{2\pi}\frac{A_{\text{overlap},\varphi}}{A_{\text{plane}}}\mathrm{d}\varphi=\frac{A+A'}{A_{\text{plane}}}+\frac{P}{2\pi A_{\text{plane}}}\int_{0}^{2\pi}\left| \vec{e}_x\times\vec{r}_0(\varphi) \right|\mathrm{d}\varphi
\tag{7}
$$

Here we give a simple way to obtain the result of the integral and a more general proof can be found in Appendix A. Notice that $P$ is the perimeter of the first particle and $p$ of course, is symmetric in the properties of the two particles. Thus the integral depends only on the properties of the second particle, and it must be equal to $\alpha P'$, where $\alpha$ is a constant independent of the properties of the particles and $P'$ is the perimeter of the second particle. For a circular second particle with radius $R'$, the integral is

$$
\int_{0}^{2\pi}\left| \vec{e}_x\times\vec{r}_0(\varphi) \right|\mathrm{d}\varphi=\int_{0}^{2\pi}R'\mathrm{d}\varphi=2\pi R'=P'
\tag{8}
$$

So $\alpha=1$. Therefore, the requested probability is

$$
p=\frac{A+A'+PP'/2\pi}{A_{\text{plane}}}
\tag{9}
$$

### 2.2. Free coverage fraction in random deposition

Now an interesting question is how many free particles we can obtain as we drop more particles onto the plane area. In a random deposition process, a particle recognized as a free particle means that the particle is not on top of any earlier dropped particle at the instant when it falls on the plane, and none of the later dropped particles are on top of it when a desired number of particles have been deposited on the plane, as shown in Fig. 3a, where 2000 particles are dropped on the plane and the free particles are marked in red. Without losing generality, we assume that we drop a mixture of $M$ particles that consists of $N$ different types, with probability $k_i$ and surface area $A_i$ of each type $i=1,,,N$, then we have

$$
1=\sum_{i=1}^{N}k_i;A_{\text{total}}=\sum_{i=1}^{N}(k_i M)A_i
\tag{10}
$$

Now we consider the probability that the first particle overlaps with the later dropped $m^{th}$ particle, where $m=2,,,M$. The first particle has a probability $k_i$ to be type $i$, and the $m^{th}$ particle has a probability $k_j$ to be type $j,j=1,,,N$. We already know that the probability that the two particles overlap with each other is

$$
p_{ij}=\frac{A_i+A_j+P_iP_j/2\pi}{A_{\text{plane}}}
\tag{11}
$$

Here $A_i,P_i$ and $A_j,P_j$ are the area and the perimeter of the first particle and the $m^{th}$ particle, respectively. The probability that the first particle of type $i$ overlaps with the $m^{th}$ particles is the sum of the overlap probability of the $N$ types by weight

![](./images/812497527692591105_5.jpg)

Fig. 3. Images of the packing formation of the rectangular particles generated in a MATLAB simulation, with a protocol of uniform random deposition. (a) free coverage fraction, where the free particles are in red and the non-free particles are in blue. (b) sticking coverage fraction, where the sticking particles are in red and the top layers are in blue. The partly reddish particles indicate the increased fraction compared with the free coverage fraction, which are recognized as non-free particles by the definition of free coverage fraction in figure (a).

$$
p_{i}=\sum_{j=1}^{N} k_{j} \frac{A_{i}+A_{j}+P_{i} P_{j} / 2 \pi}{A_{\text {plane }}}
\tag{12}
$$

Now we define $\bar{A}$ and $\bar{P}$ as the average area and the average perimeter of the $N$ types of particles

$$
\bar{A}=\sum_{j=1}^{N} k_{j} A_{j} ; \bar{P}=\sum_{j=1}^{N} k_{j} P_{j}
\tag{13}
$$

Then we have

$$
p_{i}=\frac{A_{i}+\bar{A}+P_{i} \bar{P} / 2 \pi}{A_{\text {plane }}}
\tag{14}
$$

The probability that the first particle of type $i$ overlaps with none of the other $M-1$ particles is

$$
\begin{aligned}
p_{i, \text { free }} &=\left(1-p_{i}\right)^{M-1} \\
&=\left(1-\frac{A_{i}+\bar{A}+P_{i} \bar{P} / 2 \pi}{A_{\text {plane }}}\right)^{M-1} \cong \exp \left(-M \frac{A_{i}+\bar{A}+P_{i} \bar{P} / 2 \pi}{A_{\text {plane }}}\right)
\end{aligned}
\tag{15}
$$

The approximation holds when $A_{\text {plane }} \gg \bar{A}, A_{i}, P_{i} \bar{P}$ and M is sufficiently large. Now we know the probability of the first particle to be free as of type $i$, and we also know the probability that the first particle to be type $i$ is $k_{i}$, so the contribution that the first particle adds to the number of the free particles of type $i$ is $k_{i}\left(1-p_{i}\right)^{M-1}$. By summing it all over the mixture, we have the expected number of free particles of type $i$ after we drop a mixture of M particles

$$
\tau_{i, \text { free }}=M k_{i}\left(1-p_{i}\right)^{M-1} \cong M k_{i} \exp \left(-M \frac{A_{i}+\bar{A}+P_{i} \bar{P} / 2 \pi}{A_{\text {plane }}}\right)
\tag{16}
$$

So, the area fraction covered by the free particles of type $i$ on the plane area is

$$
\rho_{i, \text { free }}=\frac{\tau_{i, \text { free }} A_{i}}{A_{\text {plane }}} \cong \frac{M k_{i} A_{i}}{A_{\text {plane }}} \exp \left(-M \frac{A_{i}+\bar{A}+P_{i} \bar{P} / 2 \pi}{A_{\text {plane }}}\right)
\tag{17}
$$

And the total area fraction covered by the free particles on the plane area is

$$
\rho_{\text {free }}=\sum_{i=1}^{N} \rho_{i, \text { free }} \cong \sum_{i=1}^{N} \frac{M k_{i} A_{i}}{A_{\text {plane }}} \exp \left(-M \frac{A_{i}+\bar{A}+P_{i} \bar{P} / 2 \pi}{A_{\text {plane }}}\right)
\tag{18}
$$

We define $\omega$ as the deposition ratio, meaning the ratio of the total surface area of all deposited particles to the surface area of the plane.

$$
\omega=\frac{A_{\text {total }}}{A_{\text {plane }}}=\frac{M \bar{A}}{A_{\text {plane }}}
\tag{19}
$$

Then the free coverage fraction of type $i$ can be written as

$$
\rho_{i, \text { free }}=\frac{k_{i} A_{i} \omega}{\bar{A}} \exp \left(-\omega\left(1+A_{i} / \bar{A}+P_{i} \bar{P} / 2 \pi \bar{A}\right)\right)
\tag{20}
$$

And the total free coverage fraction of all particles is

$$
\rho_{\text {free }}=\sum_{i=1}^{N} \frac{k_{i} A_{i} \omega}{\bar{A}} \exp \left(-\omega\left(1+A_{i} / \bar{A}+P_{i} \bar{P} / 2 \pi \bar{A}\right)\right)
\tag{21}
$$

The Eq. (21) implies that the free coverage fraction is only related to the area distribution and the geometrical feature of the particles concerning their surface area and perimeter. To quantify the geometrical feature, we define the shape factor as $s=\frac{P}{\sqrt{4 \pi A}}$. Thus for a given mixture with surface area distribution $G(A)$ and shape factor distribution $H$ (s), the free coverage fraction can be precisely calculated.

![](./images/812497527692591105_6.jpg)

Fig. 4. Image of part of the 2.8 - 5.6 mm screen size fraction of the HDPE particle sample.

![](./images/812497527692591105_7.jpg)

Fig. 5. Plastic particle area distribution in $5\ \text{mm}^2$ intervals, compared to a lognormal distribution with $\mu = 3.9$ and $\sigma = 0.6$.

To have a better look on how much the free coverage fraction can be in the random deposition, we consider a simple case, a mixture of particles with the same area $A$ and the same shape factor $s$, in other words, a mixture of identical particles. Then the free coverage fraction is simplified as

$$
\rho_{\text{free}}(\text{id}) = \omega \mathrm{e}^{-2\omega(1+s^2)} \tag{22}
$$

Now we can draw several interesting conclusions from Eq. (22).
(1) For a mixture of identical particles, the size of the particles is no longer relevant. The free coverage fraction is only related with the shape factor $s$ of the particles. Mixtures with smaller shape factors can obtain bigger free coverage fraction. Among all convex-shaped particles, the circular particles have the smallest perimeter for the same surface area and thus have the smallest defined shape factor $s=1$. Particles that are less round, such as the rectangular particles with a large aspect ratio have a bigger shape factor $s$. Thus, a mixture consisting of rectangular particles will have less free particles than that of circular particles in random deposition.

(2) It is not difficult to see that the free coverage fraction first increases with the addition of particles when the plane is scattered with few particles in a dilute packing and then decreases when the packing of particles becomes dense. Eventually, there are no free particles if we drop an excessive number of particles on the plane area, which intuitively makes sense because all the plane area would be covered with overlapped particles. After a simple derivation, we can find that the free coverage fraction reaches its maximum

$$
\rho_{\text{free}}^{\text{max}}(\text{id}) = \frac{e^{-1}}{2(1+s^2)} \tag{23}
$$

when we deposit a ratio of the total particles area to the plane area $\omega = \frac{1}{2(1+s^2)}$.

For a mixture of circular particles, the maximal free coverage fraction is $\rho_{\text{free}}^{\text{max}}(\text{circle}) \approx 9.2\%$, at a deposition ratio $\omega = 25\%$. For other shapes that are less round, for instance, the regular triangle with a shape factor $s \approx 1.65$, the maximal free coverage fraction is $\rho_{\text{max}}^{\text{free}}(\text{Triangle}) \approx 5\%$, smaller than that of circles.

![](./images/812497527692591105_8.jpg)

Fig. 6. Shape factor distribution of real plastic particles in 0.02 intervals of $s$, compared to a lognormal distribution with $\mu = -2.1$ and $\sigma = 0.6$.

![](./images/812497527692591105_9.jpg)

Fig. 7. Free coverage fraction $\rho_{free}$ vs the total deposition area ratio $\omega$ in a random deposition process of identical rectangular particles, with a shape factor $s \approx 1.2$. The simulation result (dotted curve) verified the theoretical prediction (solid curve). The maximal free coverage fraction $\rho_{free} \approx 7.5\%$ is obtained at the total deposition area fraction $\omega \approx 21\%$.

### 2.3. Sticking coverage fraction in random deposition

The free coverage fraction of a random deposition predicted above is so small that the capacity of many industrial processes is limited. A natural and practical way to improve the fraction of the free particles is to remove part of the particles and leave those at the bottom layer which stick to the plane area. We define this fraction as the sticking coverage fraction $\rho_{stick}$. This fraction is bigger than the free coverage fraction because once a particle is dropped free without overlapping with earlier particles, it immediately adds up to the sticking coverage fraction, no matter later dropped particles fall on top of it, as shown in Fig. 3b where some particles (partly in reddish) are covered by other later dropped particles (in blue), and they are also recognized as sticking particles.

Now we consider the same mixture as described in Section 2.2. Suppose we have dropped $m - 1$ particles, and now we drop the $m^{th}$ particle. In Section 2.2, we already know the probability that an $m^{th}$ particle of type $i$ overlaps with the $1^{st}$ dropped particle is

![](./images/812497527692591105_10.jpg)

Fig. 8. Sticking coverage fraction $\rho_{stick}$ vs the total deposition area ratio $\omega$ in a random deposition process of identical rectangular particles, with a shape factor $s \approx 1.2$. The solid curve is the prediction of the theory and the dotted curve is the simulation result. The asymptotic maximal sticking coverage fraction $\rho_{stick} \approx 20.5\%$ is $e$ times bigger than the maximal free coverage fraction.

$$
p_{i}=\frac{A_{\mathrm{i}}+\overline{A}+P_{i} \overline{P} / 2 \pi}{A_{\text {plane }}} \tag{24}
$$

So, the probability that $m^{th}$ particle overlaps with none of the earlier dropped $m-1$ particles is

$$
p_{i, \text { stick }}=\left(1-p_{i}\right)^{m-1}=\left(1-\frac{A_{\mathrm{i}}+\overline{A}+P_{i} \overline{P} / 2 \pi}{A_{\text {plane }}}\right)^{m-1} \tag{25}
$$

This is the probability that the particle of type $i$ is free at the point when it falls onto the plane area, and it contributes to the total number of the sticking particles of type $i$. So, the total number of sticking particles of type $i$ after we dropped M particles is

$$
\tau_{i, \text { stick }}=k_{i} \sum_{m=1}^{M}\left(1-p_{i}\right)^{m-1}=k_{i} \frac{1-\left(1-p_{i}\right)^{M}}{p_{i}} \cong k_{i} \frac{1-e^{-M p_{i}}}{p_{i}} \tag{26}
$$

Then the sticking coverage fraction of type $i$ is

$$
\rho_{i, \text { stick }}=\frac{\tau_{i, \text { stick }} A_{\mathrm{i}}}{A_{\text {plane }}} \cong \frac{k_{i} A_{\mathrm{i}}}{A_{\mathrm{i}}+\overline{A}+P_{i} \overline{P} / 2 \pi}\left(1-\exp \left(-\omega\left(1+\mathrm{A}_{\mathrm{i}} / \overline{\mathrm{A}}+\mathrm{P}_{\mathrm{i}} \overline{\mathrm{P}} / 2 \pi \overline{\mathrm{A}}\right)\right)\right) \tag{27}
$$

Here we substitute the definition $\omega=\frac{M \bar{A}}{A_{\text {plane }}}$. So the total sticking coverage fraction of the mixture is

$$
\rho_{\text {stick }}=\sum_{i=1}^{N} \frac{k_{i} A_{i}}{A_{i}+\overline{A}+P_{i} \overline{P} / 2 \pi}\left(1-\exp \left(-\omega\left(1+\mathrm{A}_{\mathrm{i}} / \overline{\mathrm{A}}+\mathrm{P}_{\mathrm{i}} \overline{\mathrm{P}} / 2 \pi \overline{\mathrm{A}}\right)\right) \quad(28)\right.
$$

Similarly, for the case of the mixture of identical particles with a shape factor $s$, the sticking coverage fraction can be simplified as

$$
\rho_{\text {stick }}(\mathrm{id}) \cong \frac{1-e^{-2\left(1+s^{2}\right) \omega}}{2\left(1+s^{2}\right)} \tag{29}
$$

It is easy to see that the sticking coverage fraction increases monotonously with the number of the particles dropped on the plane area. The rate of increase slows down gradually that particles have a high chance to be free when the plane is scattered with few particles and then it becomes more and more difficult for a particle to be settled at an empty spot. Eventually, there is no void that a single particle would fit in and the sticking coverage fraction reaches its maximum

$$
\rho_{\text {stick }}^{\max }(\mathrm{id}) \cong \frac{1}{2\left(1+s^{2}\right)} \tag{30}
$$

Comparing Eq. (23) and Eq. (30), we notice that the maximal sticking coverage fraction is $e$ times bigger than the maximal free coverage fraction for identical particles. For instance, a mixture of identical circular particles would have a maximal sticking coverage fraction $\rho_{\text {stick }}^{\max }$ (circle) $\cong 25 \%$.

### 2.4. Distributions of surface area and shape factor of real plastic particles

In order to evaluate the simulation options of a random deposition, and also to gain a rough impression of the shape features and the surface area distribution of real particles used in industry, a sample containing a little over a thousand HDPE particles from a plant application of IMDS plastic recycling [14], is imaged and the particle surface area $A$ and the perimeter of the convex hull $P$ are analyzed, as shown in Fig. 4. The majority of the plastic particles are convex, and few of them that are not strictly convex can be ignored for the statistics. The area distribution $G$ $(A)$ and shape factor distribution $H(s)$ are obtained, and they both exhibit typical lognormal form, see Fig. 5 and Fig. 6. According to Eq. (21) and Eq. (28), the calculated maximal free coverage fraction is $\rho_{\text {free }}^{\max } \approx 7.7 \%$ at the deposition ratio $\omega \approx 22 \%$ and the asymptotic maximal sticking coverage fraction is $\rho_{\text {stick }}^{\max } \approx 21.7 \%$. The calculated area-

![](./images/812497527692591105_11.jpg)

Fig. 9. Free coverage fraction $\rho_{free }$ vs total deposition area ratio $\omega$ in a random deposition process of a mixture of two types of rectangular particles, with the same shape factor $s \approx 1.2$ . The solid curves are the prediction of the theory and the dotted curves are the simulation results. The probability ratio between type S1 (square) and type S2 (triangle) is $k_{1}: k_{2}=0.8: 0.2$ and the area ratio between type S1 and type S2 is $A_{1}: A_{2}=1: 2.25$ . The total free fraction (diamond) is the sum for type S1 and type S2.

averaged shape factor is equal to $\bar{s}=1.15$, close to the shape factor of square particles $s=1.13$, which makes sense that rectangular is quite often the most commonly seen shape in practice.

### 2.5. Simulation with rectangular particles

Eq. (21) and Eq. (28) precisely predict the expected free coverage fraction and the sticking coverage fraction of a mixture that consists of arbitrarily sized and shaped particles. For the simplified case of identical particles, Eq. (22) and Eq. (29) can be applied. Now we want to check the theory in a simulation. Here we chose MATLAB to perform the simulation as it is a convenient tool for modelling and visualizing in processing large amount of particles. It has shown in Section 2.4 that rectangular is a commonly seen shape, and thus here we use two types of rectangular particles in the simulation, named as type S1 of dimensions $40\times80$ pixels and type S2 of dimensions $60\times120$ pixels, with the same aspect ratio 1:2, and so the same shape factor $s\approx1.2$. The chosen dimensions of the particles are big enough that the edge effect of the particles is negligible, regardless of any random angle a rectangular particle is orientated with respect to the orthogonal axis. The particle size of S2 is 1.5 times larger than that of type S1, meaning $P_1:P_2=1:1.5; A_1:A_2=1:2.25$. We run two simulations in a protocol described as follows:

(1) A mixture consisting of only type S1 is deposited on a rectangular canvas T, of dimensions $100\times100$ times bigger than the dimensions of the particle type S1. The center positions and the orientations of the particles are chosen in a uniform random manner. The free coverage fraction and the sticking coverage fraction are obtained with the increase of deposition ratio $\omega$, which is defined as ratio of the total area of deposited particles to the area of the canvas. To avoid the boundary effect, both the free coverage fraction and the sticking coverage fraction are obtained in a middle domain of the canvas that is 10% smaller than the original canvas.

(2) A mixture consisting of both type S1 and type S2 is deposited on the same canvas T and the probability ratio of type S1 and type S2 in the mixture is $k_1:k_2=0.8:0.2$. The free coverage fraction and the sticking coverage fraction of each type are obtained separately, together with the total free coverage fraction and the total sticking coverage fraction of the mixture, in relation with the deposition ratio $\omega$.

### 3. Results and discussion

The simulation results of the free coverage fraction and the sticking coverage fraction nicely match the theoretical predictions, for both the general case of a mixture consisting of different types of particles and the simplified case of a mixture consisting of identical particles, as shown in Figs. 7 to 10. Now we can confidently tell two facts that are important for the industry where single object operation is applied. First, for any many particles feeding in a uniformly random manner, as long as the surface area distribution $G(A)$ and the shape factor distribution $H(s)$ of the feeding materials are given, the fraction of free particles and the fraction of the sticking particles of the bottom layer can be precisely predicted. Second, the model reveals that there are upper limits of the free particles and the sticking particles that a random feeding can obtain. The upper limit of the free fraction is much smaller than what is intuitively expected. For instance, a feeding of rectangular particles can only obtain a maximum of 7.5% free particles, see Fig. 7. It is a very disappointing observation for industrial applications. In the recycling industry, sensor sorting technology has the capability to deal with a dense-packed monolayer feeding up to 40% ~ 50% [6], while the low free coverage fractions shown in Fig. 7 and Fig. 9 imply that most of the capability will be wasted because of bad feeding. The upper limit of the sticking coverage, on the other hand, is much bigger than the free coverage. In practice, a feeding rate of an infinite number of particles is not applicable, a more practical scenario would be to feed particles at a certain percentage to the plane area. For instance, we drop a batch of identical rectangular particles with a total surface area of half of the plane area $\omega=50\%$, and then the sticking coverage fraction is $\rho_{stick}\approx19\%$, see Fig. 8 and Fig. 10. An increase of coverage fraction of non-overlapping particles from 7.5% to 19% is very interesting. It means that by simply removing the top layers of particles, the rate of processable particles increases dramatically and the capacity of the process can be easily improved by a factor of 2.5. This observation is very important and instructive for many industrial processes that require

![](./images/812497527692591105_12.jpg)

Fig. 10. Sticking coverage fraction $\rho_{stick}$ vs total deposition area ratio $\omega$ in a random deposition process of a mixture of two types of rectangular particles, with the same shape factor $s\approx1.2$. The solid curves are the prediction of the theory and the dotted curves are the simulation results. The probability ratio between type S1 (square) and type S2 (triangle) is $k_1:k_2=0.8:0.2$ and the area ratio between type S1 and type S2 is $A_1:A_2=1:2.25$. The total sticking fraction (diamond) is the sum for type S1 and type S2.

![](./images/812497527692591105_13.jpg)

Fig. 11. Alternative computation of area C. We keep the orientation of the particle $\varphi$ fixed and rotate the x-axis. $\theta$ is the angle of the orientation vector with the radius vector $\overrightarrow{r_{0}}(\varphi)$.

monolayer feeding. With an extra step to remove the overlapped particles in a purely random deposition process, for instance by using air suction, a much denser monolayer feeding can be achieved.

## 4. Conclusion

In this paper, we described a two-dimensional random deposition process of arbitrary convex particles with both theory and simulation, to give insights for many industrial processes that require feeding of non-overlapping particles. The probability that two convex particles overlap with each other turns out to be simply determined by the surface areas and the perimeters of the two particles. Subsequently, we successfully obtained the formulas that could precisely predict the free particle coverage fraction and the sticking particle coverage fraction. The two fractions are determined by the area distribution and shape features of the particles. Imaging analysis of recycling plant HDPE particles reveals that the distributions of surface area and shape factor are typical lognormal. We looked at some simplified cases in which all particles are the same, and we found that the maximal free coverage fraction is only 7.5% for rectangular particles, much smaller than people would intuitively expect. While a much larger fraction of sticking particles implies that a relatively dense non-overlapping formation can be made by removing the overlapping particles from the top. This observation has great value for the industry, in the sense that by removing the overlapped particles but the bottom layer, the production capacity can be greatly improved by a factor of 2.5. Simulations with rectangular particles show that the expected number predicted by the formulas fits very nicely with any given random realization of particle packing, and thus verify the theory.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgment

The research was funded by the Dutch Research Council (NWO) within a Perspectief program "Innovative magnetic density separation for the optimal use of resources and energy". Project number: 14918 P14-07 – project 4.1.

## Appendix A. Calculation of the area of part C

Based on a special case that the convex particles are circles, we obtained the area where two convex particles would overlap with each other when the "centre point" of the second particle is within in and it leads to the overlap probability of two convex particles in a random deposition

$$
\begin{aligned}
p & =\frac{1}{2 \pi} \int_{0}^{2 \pi} \frac{A_{\text {overlap }, \varphi}}{A_{\text {plane }}} \mathrm{d} \varphi=\frac{A+A^{\prime}}{A_{\text {plane }}}+\frac{P}{2 \pi A_{\text {plane }}} \int_{0}^{2 \pi}\left|\overrightarrow{e_{x}} \times \overrightarrow{r_{0}}(\varphi)\right| \mathrm{d} \varphi \\
& =\frac{A+A^{\prime}}{A_{\text {plane }}}+\frac{P P^{\prime}}{2 \pi A_{\text {plane }}}
\end{aligned}
\tag{31}
$$

Now we provide a more general proof of the integral

$$
\frac{1}{2 \pi} \int_{0}^{2 \pi}\left|\overrightarrow{e_{x}} \times \overrightarrow{r_{0}}(\varphi)\right| \mathrm{d} \varphi=\frac{P^{\prime}}{2 \pi}
\tag{32}
$$

In the integral, $\overrightarrow{r_{0}}(\varphi)$ is the radius vector from the centre point to the point at the boundary of the second particle with a tangent parallel to the x-axis for orientation $\varphi$ of the particle axis. Since the integral is symmetric for $\overrightarrow{r_{0}}(\varphi)$ and $\overrightarrow{e_{x}}$, we can also keep the orientation of the second particle fixed and rotate the x-axis around it (see Fig. 11). Then for every angle $\varphi$, there is an angle $\theta(\varphi)$ for the point of contact with the particle orientation vector, such that $\overrightarrow{r_{0}}(\varphi)=\rho(\theta)(\cos (\theta), \sin (\theta))$, with $\rho(\theta)$ defining the shape of the particle and $\overrightarrow{e_{x}}=(\cos (\varphi),-\sin (\varphi))$. Then the integral in the alternative coordinate is

$$
\frac{1}{2 \pi} \int_{0}^{2 \pi}\left|\overrightarrow{e_{x}} \times \overrightarrow{r_{0}}(\varphi)\right| \mathrm{d} \varphi=\frac{1}{2 \pi} \int_{0}^{2 \pi}\left|\rho(\theta)\left(\begin{array}{c}
\cos (\theta) \\
\sin (\theta)
\end{array}\right) \cdot\left(\begin{array}{c}
\sin (\varphi) \\
\cos (\varphi)
\end{array}\right)\right| \mathrm{d} \varphi
\tag{33}
$$

The integral can also be written as

$$
\begin{aligned}
& \frac{-1}{2 \pi} \int_{0}^{2 \pi} \rho(\theta)\left(\begin{array}{c}
\cos (\theta) \\
\sin (\theta)
\end{array}\right) \cdot \mathrm{d}\left(\begin{array}{c}
\cos (\varphi) \\
-\sin (\varphi)
\end{array}\right) \\
& =\frac{-1}{2 \pi} \int_{0}^{2 \pi} d\left[\rho(\theta)\left(\begin{array}{c}
\cos (\theta) \\
\sin (\theta)
\end{array}\right) \cdot\left(\begin{array}{c}
\cos (\varphi) \\
-\sin (\varphi)
\end{array}\right)\right] \\
& \quad+\frac{1}{2 \pi} \int_{0}^{2 \pi}\left(\begin{array}{c}
\cos (\varphi) \\
-\sin (\varphi)
\end{array}\right) \cdot \mathrm{d}\left[\rho(\theta)\left(\begin{array}{c}
\cos (\theta) \\
\sin (\theta)
\end{array}\right)\right]
\end{aligned}
\tag{34}
$$

The first term is zero. Since $\overrightarrow{e_{x}}$ is parallel to the tangent vector of the contact point with the radius vector $\overrightarrow{r_{0}}(\varphi)$, so we have the relation

$$
\left(\begin{array}{c}
\cos (\varphi) \\
-\sin (\varphi)
\end{array}\right)=\frac{(\mathrm{d} / \mathrm{d} \theta)\left[\rho(\theta)\left(\begin{array}{c}
\cos (\theta) \\
\sin (\theta)
\end{array}\right)\right]}{\left|(\mathrm{d} / \mathrm{d} \theta)\left[\rho(\theta)\left(\begin{array}{c}
\cos (\theta) \\
\sin (\theta)
\end{array}\right)\right]\right|}
\tag{35}
$$

Then the second term becomes

$$
\begin{aligned}
& \frac{1}{2 \pi} \int_{0}^{2 \pi} \frac{(\mathrm{d} / d \theta)\left[\rho(\theta)\left(\begin{array}{c}
\cos (\theta) \\
\sin (\theta)
\end{array}\right)\right]}{\left|(d / d \theta)\left[\rho(\theta)\left(\begin{array}{c}
\cos (\theta) \\
\sin (\theta)
\end{array}\right)\right]\right|} \cdot(d / d \theta)\left[\rho(\theta)\left(\begin{array}{c}
\cos (\theta) \\
\sin (\theta)
\end{array}\right)\right] \mathrm{d} \theta \\
& \quad=\frac{1}{2 \pi} \int_{0}^{2 \pi}\left|(d / d \theta)\left[\rho(\theta)\left(\begin{array}{c}
\cos (\theta) \\
\sin (\theta)
\end{array}\right)\right]\right| \mathrm{d} \theta
\end{aligned}
\tag{36}
$$

The integral shown above is the definition of the arc length, and so we have the final expression of the integral

$$
\frac{1}{2 \pi} \int_{0}^{2 \pi}\left|\overrightarrow{e_{x}} \times \overrightarrow{r_{0}}(\varphi)\right| \mathrm{d} \varphi=\frac{P^{\prime}}{2 \pi}
\tag{37}
$$

## References

[1] H. Wotruba, Sensor sorting technology - is the minerals industry missing a chance? International Mineral Processing Congress, Istanbul, Turkey, Sep. 2006.

[2] Christopher Robben, Hermann Wotruba, Sensor-based ore sorting technology in mining - past, present and future, Minerals 9 (9) (September 2019) 523.

[3] M.A. Aguirre, M. Hidalgo, A. Canals, J.A. Nóbrega, E.R. Pereira-Filho, Analysis of waste electrical and electronic equipment (WEEE) using laser induced breakdown spec- troscopy (LIBS) and multivariate analysis, Talanta 117 (2013) 419-424.

[4] V.C. Costa, F.W.B. Aquino, C.M. Paranhos, E.R. Pereira-Filho, Identification and classi-fication of polymer e-waste using laser-induced breakdown spectroscopy (LIBS) and chemometric tools, Polym. Test. 59 (2017) 390-395.

[5] C.-I. Chang, Hyperspectral Imaging: Techniques for Spectral Detection and Classifica- tion, Kluwer, New York, 2003.

[6] Y. van Engelshoven, P. Wen, M. Bakker, R. Balkenende, P. Rem, An innovative route to circular rigid plastics, Sustainability 11 (2019) 6284.

[7] R. Kumar, S. Lal, S. Kumar, P. Chand, Object detection and recognition for a pick and place Robot, Asia-Pacific World Congress on Computer Science and Engineering, Nadi, Fiji (APWC on CSE) 1 (1) (2014) 1-7.

[8] Y.K. Yen, C.L. Lin, J.D. Miller, Particle overlap and segregation problems in on-line coarse particle size measurement, Powder Technol. 98 (1998) 1-12.

[9] S. Al-Thyabat, N.J. Miles, T.S. Koh, Estimation of the size distribution of particles moving on a conveyor belt, Miner. Eng. 20 (1) (2007) 72-83.

[10] Hans Hartmann, Thorsten Böhm, Peter Daugbjerg Jensen, Michaël Temmerman, Fabienne Rabier, Michael Golser, Methods for size classification of wood chips, Bio- mass Bioenergy 30 (11) (2006) 944-953.

[11] M. Abramson, W.O.J. Moser, More birthday surprises, Am. Math. Mon. 77 (1970)856-858.

[12] J. Mullooly, A one dimensional random space-filling problem, J. Appl. Probab. 5 (2)(1968) 427-435.

[13] S. Uneja, M. Mandjes, Overlap problems on the circle, Adv. Appl. Probab. 45 (3)(2013) 773-790.

[14] B. Hu, Magnetic Density Separation of Polyolefin Wastes, Bin Hu, Delft, 2014https:// doi.org/10.4233/uuid:0c3717fa-8000-4de0-a938-d65605bf2a96 172 p.