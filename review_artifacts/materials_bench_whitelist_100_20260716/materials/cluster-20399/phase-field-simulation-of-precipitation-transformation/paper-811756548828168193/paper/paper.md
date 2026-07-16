A molecular dynamics study of deformation induced phase transformations at fault bands

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2010 J. Phys.: Conf. Ser. 240 012105

(http://iopscience.iop.org/1742-6596/240/1/012105)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 169.230.243.252
This content was downloaded on 16/12/2014 at 14:19

Please note that terms and conditions apply.

# A molecular dynamics study of deformation induced phase transformations at fault bands

C W Sinclair
Department of Materials Engineering, The University of British Columbia, Vancouver, BC V6T 1Z4 Canada
chad.sinclair@ubc.ca

**Abstract.** In many ferrous austenitic alloys a strain induced martensitic transformation is important for determining bulk mechanical response. In this work molecular dynamic simulations have been performed in an attempt to further elucidate the mechanisms by which bcc-$\alpha'$ martensite may form at deformation induced hcp-$\epsilon$ martensite bands. The question of critical nucleus size and fault band arrangement are discussed in relation to the Olson-Cohen model for nucleation at fault band intersections as is the resulting orientation relationship.

## 1. Introduction
The strain induced transformation from austenite ($\gamma$) to martensite ($\epsilon$ and/or $\alpha'$) is responsible for the strong rate of work hardening in many austenitic steels. Understanding and predicting these bulk mechanical properties requires an ability to predict the rate of phase transformation as a function of plastic strain. This relationship comes from the apparent ability of plasticity to generate potent sites for the nucleation of the phase transformation. Phenomenological models for this transformation consider that the intersection between deformation induced planar faults provides unique conditions for the phase transformation[1, 2]. Olson and Cohen [2] pointed out that if a band of hcp-$\epsilon$ martensite (which can be considered as being comprised of stacking faults on every second {111} plane) was intersected by a second band of faulted $\epsilon$ (comprised of stacking faults on every third atomic plane), then the strain (in a continuum sense) at the intersection of these fault bands would correspond closely to the Bain strain required for the $\gamma \rightarrow \alpha'$ phase transformation (e.g. [4]). In reality, this process of intersection (if it can occur) is atomistic in nature. In order to investigate this transformation from the atomic scale a recent study using molecular dynamics simulations [5] was initiated. The phase transformation was shown to occur at the intersection without the need for externally applied stress and that the product $\alpha'$ was observed to grow into the surrounding fault bands. A Pitsch orientation relationship was found to exist between the two phases. While the MD simulations clearly indicated that the envisioned fault band intersections are potent sites for nucleation of $\alpha'$ several questions remain unresolved. Among these it is important to understand whether the transformation will proceed even in the absence of the perfect intersection geometry described above. For example, will the transformation take place when two perfect $\epsilon$ martensite bands intersect? Also not investigated was whether there is a minimum required intersection volume. Finally, it was noted that the Pitsch orientation relationship observed in the MD simulations does not correspond to the the

orientation relationship (Kurdjumov-Sachs) found experimentally in these materials. It is the purpose of this note is to expand upon these topics.

The primary aspects of the simulation approach have been outlined elsewhere [5]. Simulations were thermostated to 50 K in an NVT ensemble. The EAM potential developed for Fe by Ackland et al. [6] was used in this study. This potential replicates many of the properties of Fe, but predicts a very low stacking fault energy and, correspondingly small difference in cohesive energy between the fcc and hcp phases. The simulation cell was periodic in the $z$-direction and fixed in the $x$ and $y$ directions. The $\epsilon$ and faulted $\epsilon$ were created by introducing stacking faults within the simulation cell. Consistent with our previous work, simulations were performed on a small cell containing 10,835 atoms with dimensions of 10.7 x 9.2 x 1.2 nm in the $x$, $y$ and $z$ directions. Also presented here are larger scale simulations performed on 234,472 atoms in a box having dimensions of 40.6 x 39.4 x1.83 nm. These latter simulations have been performed using the LAMMPS package(http://lammps.sandia.gov) [7] with visualization performed using Atomeye [8]. The crystallographic geometry of the simulation cell is illustrated in figure 1 where $x=[0\overline{1}1]_{fcc}$, $y=[\overline{1}00]_{fcc}$ and $z=[011]_{fcc}$.

## 2. Dependence of Transformation on Fault Intersection Characteristics
The Olson-Cohen model for nucleation is specific in the combination of fault bands ($\epsilon$ and faulted $\epsilon$) that are best suited for nucleation of $\alpha'$. Experimental observations, however, routinely show that the transformation can occur at a range of faults. In figure 2(a) the progression of transformation at the fault band intersection is shown for the intersection envisioned by Olson and Cohen. In figure 2(b) a simulation consisting of two intersecting perfect $\epsilon$ bands is shown. Red (light) atoms have a coordination number of 12 (fcc or hcp coordination) while blue (dark) atoms have a coordination number of 8 (bcc). Atoms with other coordination numbers are not shown.

![](./images/811756548828168193_1.jpg)

**Figure 1.** Schematic orientation of simulation cell relative to the Thompson tetrahedron. The Burgers vectors of the two sets of partial dislocations used to generate the $\epsilon$ and faulted $\epsilon$ bands are also shown.

![](./images/811756548828168193_2.jpg)

**Figure 2.** Progression of transformation from $\gamma \rightarrow \alpha'$ in the small simulation cell viewed along the $z$ axis for a) the fault band intersection envisioned by Olson and Cohen and b) intersection between two perfect $\epsilon$ bands. Red (light) atoms have a coordination number of 12, blue (dark) atoms a coordination number of 8.

![](./images/811756548828168193_3.jpg)

Figure 3. a) The measured rate of transformation in cells containing intersecting $\epsilon$ and faulted $\epsilon$ with differing intersection volumes defined by the number of stacking faults used to create the $\epsilon$ plates. b) The rate of transformation for different types of fault intersection. The nomenclature follows that introduced by Olson and Cohen [2] where $T3$ = faulted $\epsilon$, $T2$ = perfect $\epsilon$ and $T1$ = twin.

The rate of transformation for different types of fault intersections is quantified in figure 3(b). Consistent with the images in figure 2, the rates of transformation for intersections formed by a perfect $\epsilon$ plate and a faulted $\epsilon$ plate (the conditions of Olson-Cohen) and between two perfect $\epsilon$ bands are nearly the same. As the intersecting faults are changed the strain in the intersection volume also changes. For the intersection between a perfect $\epsilon$ plate and a twin and the intersection between two twins the transformation proceeds much more slowly, consistent with an increasing departure from the Bain strain in the intersection volume.

Figure 3(a) also illustrates how the size of the intersection volume effects the rate of transformation. The results show that there are is a minimum intersection volume required for the transformation to proceed. These results were reproduced with the larger simulation cell where it was observed that when an 8 atomic layer thick $\epsilon$ plate was intersected by 1 and 2 stacking faults a small region having bcc coordination was formed but did not grow appreciably. In contrast, the situation of $\epsilon$ martensite being intersected by 4 stacking faults results in a rapid transformation with the $\alpha'$ martensite reaching the edges of the simulation cell within 70 ps. For the case of $\epsilon$ martensite intersected by 8 stacking faults (figure 4) the transformation proceeds rapidly reaching the edges of the cell after 30 ps.

Another notable feature of the transformation observed in figure 4 is the apparent anisotropic growth of the $\alpha'$ martensite along the perfect $\epsilon$ martensite band. This is to be contrasted with the results from the small scale simulation shown in figure 2 (a) where the growth of the $\alpha'$ nucleus was stopped shortly beyond the intersection volume due to the constraints imposed by the simulation cell boundaries.

Careful observation of the local atomic structure at the fcc/bcc interface reveals that the growth of the $\alpha'$ into the prior $\epsilon$ band corresponds to a change in orientation relationship between $\alpha'$ and the $\gamma$ situated outside of the $\epsilon$ bands. Consistent with our previous observations, the orientation relationship between the $\gamma$ and $\alpha'$ formed within the original intersection volume is Pitsch (figure 5(a)). However, the high rate of growth into the prior $\epsilon$ band is observed to correspond to the nucleation of a new $\alpha'$ nucleus with a Kurdjumov-Sachs orientation relationship corresponding to a rotation of $5.26^\circ$ relative to the Pitsch orientation relationship. This observation is significant given that it is the Kurdjumov-Sachs orientation relationship that is most commonly reported between $\alpha'$ and $\gamma$ in TRIP austenitic steels. Moreover, the morphology of $\alpha'$ martensite in figure 4 corresponds more closely to that observed experimentally

![](./images/811756548828168193_4.jpg)

Figure 4. The large simulation cell after 30 ps at 50 K showing the anisotropic growth of the $\alpha'$ martensite (blue/dark) outside of the intersection volume.

![](./images/811756548828168193_5.jpg)

Figure 5. Highlight of the atomic structure at the fcc (yellow/light) and bcc (gray/dark) interface a) near the original intersection volume noted as R1 in figure 4 and b) in the prior $\epsilon$ band noted as R2 in figure 4. In the former case the orientation relationship is found to be Pitch (as in [5]) while the $\alpha'$ formed in the prior $\epsilon$ band is found to have a Kurdjomov-Sachs orientation relationship.

as $\alpha'$ is often found to grow roughly parallel to and within $\epsilon$ bands. As noted before, the strains generated by the $\epsilon$ band partially accomplish the Bain strain required for the transformation. The observations reported here likely point to the importance of the interface generated between $\alpha'$ and its surroundings in terms of the mobility of the phase interface, a factor well known to be important for the determination of the crystallography and growth characteristics of thermal martensite [4, 9].

### 3. Summary
The progression of phase transformation within the context of the Olson-Cohen model has been shown to be sensitive to both the type of fault band intersection as well as fault intersection volume. Moreover, it has been shown that in large simulations, the growth of $\alpha'$ becomes very anisotropic once it grows beyond the original fault band intersection volume. The rapid increase in growth kinetics corresponds to a change in orientation relationship from Pitsch to Kurdjumov- Sachs, the latter being coherent with experiment. Further work continues to elucidate the process of intersection itself.

### References
[1] Olson G. B., Cohen M., Metall. Trans. 1975;6A:791.
[2] Olson G B, Cohen M., 1972 *J. Less-Common Metals* **28** 107
[3] Bogers A J, Burgers W G, 1964 *Acta Metall.* **12** 255
[4] Bhadeshia H K D H, 2001 *Worked Examples in the Geometry of Crystals (2nd edition)* (London: Institute of Materials, London)
[5] Sinclair C W, Hoagland R G, 2008 *Acta Mater.* **56** 4160
[6] Ackland G J, Bacon T H D J, Calder A F, 1997 *Phil. Mag. A* **75** 713
[7] Plimpton S J, 1995 *J. Comp. Phys.* **117** 1
[8] J Li, 2003 *Modelling Simul. Mater. Sci. Eng.* **11** 173
[9] Pond, R C, Ma X, Hirth, J P, 2008 *J. Mater. Sci.* **43** 3881