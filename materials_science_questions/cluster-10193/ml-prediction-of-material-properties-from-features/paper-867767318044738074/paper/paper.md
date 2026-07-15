# Property-aimed embedding: a machine learning frame work for material discovery

Lei Gu and Ruqian Wu*

Department of Physics and Astronomy,
University of California, Irvine, California 92697, USA

## Abstract

Proposing new materials by atom substitution based on periodic table similarity is a conventional strategy of searching for materials with desired property. We introduce a machine learning frame work that promotes this paradigm to be property-specific and quantitative. It is of peculiar usefulness in situations where abundance data is accessible for learning general knowledge but samples for the problem of interest are relatively scarce. We showcase its usage and viability in the problem of separating high entropy alloys with different structural phases, for which a very simple data-driven criterion achieves differentiating ability comparable with widely used empirical criteria. Its flexibility and generability make it a promising tool in other material discovery tasks and far beyond.

## INTRODUCTION

Owing to growing databases and algorithm improvements, machine learning (ML) techniques are achieving increasing capacity and popularity in material discovery [1–17]. The core of these ML tasks is to construct a mapping between fundamental parameters and targeted properties, so that we can predict unexplored materials using data at hand and/or easy to acquire. Because the mapping in itself does not give us guidance for where to look for promising matters, we need clues from elsewhere. Atoms substitution based on their periodic table similarity is a conventional material discovery paradigm. Here, we present a framework that inherits and promotes the gist of this paradigm. Due to complex interactions among different ingredients, periodic table can not always be an effective guidance for the selection of substituent that provides the targeted property. With the proposed property-aimed embedding (PAE) approach, we can make this substitution paradigm much more property-specified and quantitative.

It is convenient to have an idea of the PAE through comparison between its rationale and that of the property-to-property mapping (PPM) approach. In PPM, vectors encoding the property values are fed into a machine learning model (such as a neural network in Fig. 1(a)), and a mapping is learned by optimizing the model variables. A classification problem is address similarly by changing the targeted property values into class labels. Since early stage of using ML for material discovery, classic algorithms such as linear regression, supported vector machine and Bayesian inference methods are adopted. Although they are suitable for cases where the training dataset is small, they usually have limited capacity or require a good knowledge and presumption on the mapping to be learned.

In the fashion of big data and deep learning, neural networks join in as one type of widely used ML models. While they have high representative capacity so that any function can be approximated in principle, massive training samples are needed, or otherwise, the learned mapping has poor generalization ability in domains that are not abundantly sampled. Another critique is the black-box nature of neural networks, which hinders drawing physical insights. A step improving the interpretability is taken in Ref. [15]. by constructing specific graph convolutional neural networks for periodic crystals, so that the structural information is apparent. As the PPM is only a property value calculator, a ML material discovery/design scheme usually includes other components such as strategy of designating the search space,

![](./images/867767318044738074_1.jpg)

FIG. 1. (a) In PPM, a vector containing property informations of a matter is mapped to the targeted property. (b) In PAE, ingredient entities are embedded as vectors and mapped to relevant properties through a microscopic model/description.

DFT calculation and even experimental verification [4, 7, 16].

In PAM we start from a microscopic model/description of certain properties and represent the atoms as vectors (usually in high dimensional Euclidean space) so that a relation between the representative vectors and the property can be constructed, as shown in Fig. 1(b). The orientation and/or length of the vectors are optimized to make the model's output a good approximation of the property values. As long as the microscopic model is made of continuous functions, a property-specified similarity is naturally and quantitatively defined by the distance among the vectors. Based on the similarity we can use the atom substitution as a recommendation strategy to designate the search space for DFT or experimental verification.

As shown at the output end in Fig. 1(b), the aimed property of PAM is not necessarily the targeted property that we directly inspect, but relevant properties that are easier for modelization and data collection, say, formation energy vs. thermal stability and binding energy vs. mechanical strength. From property selection to modelization, PAE is built on physical insight and understanding. Compared to PPM, this is somewhat a drawback in the sense that the microscopic models need some endeavour to be set up. However, the endeavour pays off. Besides inherently being a material recommender, the built-in interpretability facilitates a utility much peculiarly pertinent to PAM, which is our focus in the remaining.

In Ref. [9] and [10], the authors embedded atoms and organic groups, respectively, as

vectors according to their cooccurrence statistics. Their results confirm the validity of periodic table grouping and known functional similarity among the organic groups. While these works suggest that the embedding approach can learn general knowledge, their further usage of the embedded vectors as input for PPM dose not add up much to our arsenal. Since output of each hidden layer in a neural network is a sort of property embedding, even using the vanilla chemical formula as input, embedding of the constitutional information is implemented by the neural network. From this perspective, the embedding based on cooccurrence amounts to an input preprocessing, which can be beneficial for numerical stability and convergence but does not touch the black-box issue or mitigate the demand of sample abundance.

While still maintaining the ability of distilling general knowledge, when the atoms are embedded with the selected properties as aim, the learned knowledge is not too general to go beyond well known facts. Moreover, since the selected properties have been endowed with our physical understanding, we do not need to forcefully construct a black-box mapping between these properties and the targeted property. Then a simple algorithm that does not demand massive learning samples can be effective enough. The two traits render PAE an applicable tool in the situation where we have abundant data to learn general knowledges but the data provision is relatively scarce for the specific problem of interest to us.

Study in high entropy alloys (HEAs) [18-20] is a proper arena to showcase this utility. Although we have a large number of binary and ternary alloy entries in widely used databases, their data for quartet and beyond are rare or null. Meanwhile, the periodic table grouping are less pertinent for metals, because, unlike valence or ionic bonds, electronic states in metals are highly delocalized so that the stability is much less dependent on atomic structure of neighbouring atoms. This is the reason why the embedding based on cooccurrence is ineffective for transition metals, which present in most of HEAs. More specifically, here we address the problem of searching for single solid-solution phase HEAs [21-31], which is a meaningful problem in itself, and previous works of which can be used as comparison benchmarks.

In Fig. 2 are schematics of our motivation of property selection, vector representation scheme of atoms, the microscopic description and a final classification procedure. Let us go through them one at a time. In Ref. [21] and [22], the authors showed respectively, that closeness in binary enthalpy of the ingredient atoms and similarity in atom size are nice

![](./images/867767318044738074_2.jpg)

FIG. 2. (a) Motivation of property selection: lattice distortion could cause variation of energy. (b) Each atom is represented both as host and substituent vectors, and binding energy is defined between host and substituent as the negative inner product. (c) Energy contribution of an ingredient is summation of its interaction with the environmental hosts weighted by their proportions. (d) After the optimization, criteria separating the different phases are built based on learned knowledge.

properties to predict whether an HEA is a single phase alloy. Our choice of energy per atom as the embedding aim is motivated by the intuition that size mismatch should also be reflected in the energy since it kind of stretches the lattice [25] and could cause energy variation. In addition, energy is closely related to enthalpy in that enthalpy at $T=0$ K is equal to the formation energy. Regarding the two observations, energy per atom could be a property pertinent to our problem, and at the same time, is well recorded in most databases.

Unlike the embedding based on cooccurrence statistics where each entity corresponds to one vector only, we assign two vectors to each atom involved—the host vector and the substituent vector. The reason is more a technical predicament than the physical picture that we generate new materials by atom substitution. As the first step to relate the representative vectors to the aimed property—energy, we define *binding energy* between two ingredients as the inverse of distance. Here, the inverse is used, because for stable matters, total energy $E<0$ (so is the energy per atom), and we wish the atoms with stronger binding tendency to lie closer. Then, if the Euclidean distance is used, positive energy is excluded at all.

A more proper distance is the cosine distance, i.e. the inner product. The inequality $(\vec{A}-\vec{B})\cdot(\vec{A}-\vec{B})>0$, however, implies that binary matters would always have positive


formation energy if atoms are only represented by a single vector, because now $(\vec{A}-\vec{B}) \cdot$
$(\vec{A}-\vec{B})$ is exactly the formation energy of binary matter AB. This implies that alloys can
not stably exist, which clearly contradicts with the reality. Single vector representation is
unviable. We can technically circumvent the predicament by the dual vector assignment,
and define the binding energy between atoms A and B as inner product of host vector $\vec{A}$
and substituent vector $\vec{b}$, as sketched in Fig. 2(b).

Now, for two atoms A and B, we have four inner products $\vec{A} \cdot \vec{a}, \vec{B} \cdot \vec{b}, \vec{A} \cdot \vec{b}$ and $\vec{B} \cdot \vec{a}$. They
are related, but due to the separation of host and substituent, formation energy of binary
alloys are not restrict to be positive. With the dual assignment, both $\vec{A} \cdot \vec{b}$ and $\vec{B} \cdot \vec{a}$ have the
meaning of binding energy between atoms A and B. Here, we do not impose $\vec{A} \cdot \vec{b}=\vec{B} \cdot \vec{a}$. In
other words, instead of the real binding energy, we implement evaluation for a less physical
property: how much a substituent atom contributes to the totally energy with certain atoms
presented in its neighbourhood as host.

We exemplify our formulation of energy per atom illustrated in Fig. 2(c) through a ternary
matter with chemical formula $\mathrm{A}_{x} \mathrm{~B}_{y} \mathrm{C}_{z}$, which reads

$$
\begin{cases}
E_{p e r}=\frac{1}{2} \sum_{i=A B C} w_{i} \vec{v}_{i} \cdot \vec{N}_{i}, & (1) \\
w_{A}=\frac{x}{x+y+z}, & (2) \\
\vec{N}_{A}=\frac{(x-1) \vec{A}+y \vec{B}+z \vec{C}}{x-1+y+z}, & (3)
\end{cases}
$$

where $\vec{v}_{i}$ denotes the substituent vector, $w_{A}$ is the proportion of $A$, and $\vec{N}_{i}$ the environment
vector representing the host atoms around. Factor $1 / 2$ is included since $\vec{v}_{i}$ is only one end of
the substituent-host interaction. Similar to ternary, the case of other numbers of ingredients
can be readily inferred. One point we should note is that calculating the ratio of hosts in
the environment vector as in Eq. (3) implies exclusion of the atom itself, which is different
with the usually used regular solution assumption in HEA studies. We such formulate it
since the data in the material project database [32] are from DFT calculations in which the
crystal structure and atom positions are fixed. When the optimized results are applied to
HEAs, we assume they are regular solutions and do not perform the self-exclusion.

To avoid unconscious data selection, we will use the experimental data collected in
Ref. [18] for our problem of HEA phase separation. To cover the elements presented there,
we include 45 metals and nonmetals P and Si in our embedding (refer to supp. for the


![](./images/867767318044738074_3.jpg)

FIG. 3. (a) Single-phase alloys usually have higher similarity among its components than the other two sorts, and one element with strong binding tendency to the others is the major contributor of structure distortion. (b) An energetic mismatch for a material is evaluated as a weighted summation over similarities that exceed a cutoff. (c) The vector size is determined to be Dim=3, which corresponds to the critical point in the loss. (d) With the cutoff 0.7459 and the borderline at 0.0144, the ration of correctly separated samples is 76/90.

full list). There are 10075 materials in the database that are composed by these elements. Neglecting structural influence, we use the one with lowest energy among materials under the same chemical formula. After this filtering, 7396 matters remains: 2490 binaries, 4835 ternaries and 24 quartets. During our early calculation, we found the numerical stability is poor in the sense that the results clearly vary due to randomness in initialization and stochastic gradient descent. It appears that Eq. (1) can not represent complex interactions due to its linearity. For the reason, we leave the ternaries as correction to be addressed later, and firstly optimize the embedding using the singlet and binary data only. We use the mean squared error as the loss function,

$$
L = \sum_{i} \frac{\left(E_{per}^{i} - E_{d}^{i}\right)^2}{S}, \tag{4}
$$

with summation over the training data. Here, $E_{d}^{i}$ is the recorded energy per atom in the database, and $S$ is the number of training samples.

The size (dimension) of the vectors is a hyper-parameter, which is usually determined with validation dataset. Because we do not have one, we use another strategy to prevent overfitting—critical point in the loss. We will present results with $\text{Dim} = 3$, since from

Fig. 3(c) we see that over it the loss decreases slowly. Another justification is geometrical intuitive. When $\text{Dim} \leq 2$, the vectors (actually scalars for $\text{Dim}=1$) are enforced an order in the position on a line for $\text{Dim}=1$ and in the polar angle for $\text{Dim}=2$, which implies that a vector can only have two neighbours. For $\text{Dim} \geq 3$ the number of neighbours can be infinite, which is an qualitative transition for freedom of arranging the vectors. Another technique detail is the initialization values. To facilitate numerical stability, we advice to start with small values, so that the vectors can effectively adapt their orientation at the early stage of training. If the initial vectors are long, it is more likely to stuck in suboptimal traps. In this work, normal distribution with standard error 0.01 is used for the vector elements.

After optimization, we can define an energetic similarity with respect to each host atom. Ternary $\text{A}_x\text{B}_y\text{C}_z$, for instance, has the vector $(\vec{A} \cdot \vec{a}, \vec{A} \cdot \vec{b}, \vec{A} \cdot \vec{c})$ as similarity among A,B,C w.r.t host A and the other two w.r.t B and C. In Fig. 3(a), we present representative results for good single-phase HEAs in the top panel where the ingredients are quite similar, and for typical amorphous HEAs in the middle where the atoms differ more. In the bottom panel is the similarities for the AlGrFeNiGu system, whose structural phase change from single-phase to multiphase with increase containment of Al. Our results well reflect this in that the Al is exactly the most dissimilar one. For a material, the full similarity metrics is a matrix (as sketched in Fig. 3(b)) with rows and columns indexed by hosts and substituents, respectively. What are presented in Fig. 3(a) are the last rows, and the other rows usually show similar pattern, except that the absolute values may vary a lot.

From Fig. 3(a), we can have a rough impression that one ingredient with the strongest binding tendency (the longest bar) is usually the key player that distorts the lattice and cause structural inhomogeneity. In Fig. 3(b), we show the procedure of promoting this observation to a quantitative criterion. First, the issue of absolute value variation among different rows is addressed by row-wise normalization in which the row maximum is normalized to unity. This results in the orange matrix on the top of Fig. 3(b). To proceed, a relation between similarity and structural phase is needed, for which we simply assume a cutoff, the only parameter in our criterion. When the similarity is above the cutoff, we consider the energetic mismatch with the key player is ineffective and do not count it in, otherwise, the player scores 1. By this we have the white-black matrix on the right. To reflect effect of atom proportions, elements of the normalized matrix are weighted by the corresponding host and substituent proportions to arrive the blue matrix on the left. Finally, a mismatch value is obtained for


each material by summarizing the element-wise product of the two matrices.

The optimal cutoff value is the one that results in best separation of the single-phase from the other two phases. As shown in Fig. 3(d), with cutoff 0.7495 and a borderline of mismatch at 0.0144, we can have a seperation score 76/90. This means that the number of single-phase HEA assigned to multiphase or amophous HEA, and the number of misassignments the other way around are 14 in total. We note that due to the cutoff nature, the optimal cutoff is actually a narrow range around 0.7495, since within it the results do not change. In Ref. [23] the authors compared major empirical criteria using the same materials. Compared to them, our separation is not the best, but no worse than most of those criteria. Considering the simplicity of our criterion, this comparability is an indication of the viability of our approach.

Now let us deal with learning knowledge from the ternaries (we neglect the 24 quartets for computational convenience). Because the weights are not variables and Eq. (1) is linear, the number of inner product is the number of independent degree of freedoms we can have. $M$ substituent-host pairs can only offer $M^2$ freedoms, regardless of the vector size. When the complexity requires more freedom to represent it, increasing vector size is ineffective. We could increase the vector size and at the same time add nonlinear operations before taking the inner products. Based on our attempts, however, while this can fit the output well to the recorded energy, it is a mess when the we use the optimized vectors for HEA phase separation. In that way, we actually take the step that lead to neural networks' black-box nature and weak generalization ability.

Another strategy to cope with complexity is increasing the number of entities to be embedded, which increases the number of freedom. As an attempt, we treat the host-host pairs as objects to be embedded, whose proportion is defined as product of their individual proportions. As shown in Fig. 4(a), when calculate the proportion of a host-host pairs, the indirect host is regard as the host of the direct host, which means we do not exclude the substituent indirectly hosted by it. Take $\mathrm{A}_x\mathrm{B}_y\mathrm{C}_z$ for example, the weight of pair $\mathrm{B{\to}A}$ in the environment of $A$ is

$$
w_{B \to A}=\frac{y}{x-1+y+z} \times \frac{x}{x+y-1+z}, \tag{5}
$$

where the arrow means is hosted by, and $B \to A$ and $A \to B$ is treated as two distinct entities. To facilitate the numerical stability, we do not redo the embedding from scratch, but consider the knowledge from ternaries as something like perturbation. This is quite

beneficial, because as shown in Fig. 4(c), we now keep the substituent vectors unchanged, which are anchors for the other half of the inner product.

Besides this perturbation like aspect which we would like to emphasis, there are two other technical differences with the original calculation. Being treated as perturbation, our targeted value is not the recorded energy per atom, but $\Delta E = E_d - E_{per}$, with $E_{per}$ the per atom energy calculated based on the previously optimized vectors. In addition, the similarity metrics is expanded from a matrix to a 3D array, where the depth dimension represents the hosts of hosts. Its element can be understand as binding energy between a substituent and a host modified by the host of host. Accordingly, its value is $E_{ijk} = E_{ij} + \Delta E_{ijk}/2$, where $E_{ij}$ is the unperturbed binding energy between atom $i$ and host $j$, as those in Fig. 3(a), and $\Delta E_{ijk}$ is the binding energy between substituent $i$ and host-host pair $j \to k$. Then following the procedure in Fig. 3(b), the cutoff is determined as 0.7353 and the borderline is at $1.678E^{-3}$. The separation result is similar to that in Fig. 3(d), with an improvement from 76/90 to 79/90.

Compared to the empirical criteria, ours does not work well in separating out amorphous alloys. Many factors can contribute to the inaccuracy. Most importantly, the simple criterion of energetic mismatch can not fully capture the complexity. One can note form Ref. that the amorphous alloys usually have very low enthalpy. The atoms' strong tendency to bind up may require stronger energetic similarity to keep the structural homogeneity. In other words, the cutoff value should vary matter-by-matter according to their enthalpy. It could also be because the cutoff criterion instead of a continuous function is a very rude division. But the other way around, it is this simplicity that evinces the validity of our approach, since it avoids the possibility that complicated criteria can easily become a game of fitting. Neglecting structural information is another issue. Although the chemical formula contains some structural information, accurate number of nearest and next nearest neighbour atoms varies with crystal structure. Our evaluation for the weights is somewhat rough.

Before conclusion, we remark on the essence of the embedding method in this work. Since our microscopic model is an expression that represents total energy as summation of the parts, one can consider our embedding approach as a way of extracting the binding energies. However, the collectively defined binding energy is different with the original DFT data of the equal atomic binary alloys in several aspects. First, as discussed above, due to the dual assignment their meaning are inequivalent by definition. The effectiveness of our

![](./images/867767318044738074_4.jpg)

FIG. 4. (a) Weights of the host-host pairs are defined as product of proportions of the two hosts, for which the indirect host is treated as host of the host. The arrows mean is hosted by. (b) The similarity metrics now is a 3D array for each matter. (c) The perturbation like procedure is generally similar to that in Fig. 2(c), except an important distinction that the embedding vectors of substituents have been optimized previously.

results is a reminder that what really needed is not necessarily a well defined physical model that links fundamental laws to experimental observation, but basically, a data analysis model motivated by microscopic understanding. Second, since many binary relations (say, between Cu and Fe, Co, Ni) are null in the database due to instability of the alloys composed by the two elements, these values are sheerly inferred through the binding of the two elements with the rests. Actually, the other energies also posses such a sense of being inferred, since each embedded vector is collectively determined by its direct of indirect interaction with all the others. This is favourable for our problem in that HEAs consist of multiple elements with varying quota.

In summary, we showcased usage and utility of PAE through separating the single-phase alloys with those in multiphase and amorphous phase. Implication and outlook of our work lie at three levels. For the HEA phase separation problem, it is an example of one property only. We can include other quantities such as variation in density and crystal constants to

reflect the lattice stretch, so that the problem can be addressed with multiple criteria. More specifically to our model, one way of representing the structural information is treating the same atom in different structure as separate vectors. While the simplicity of the criterion is fine for us to show viability of PAM, it is not necessary for practical tasks. As mentioned above, some thermodynamic information may be incorporated in.

As for other material discovery tasks, in principle once a microscopic model is given, a PAE scheme could be constructed for the involved entities, so it is generable and flexible. From classical to quantum mechanics, a system can be represented by its Hamiltonian, which implies that energetic representation is an important aspect for physical microscopic models. Our dual assignment scheme can be a general strategy for these application to avoid the problem of positive defined formation energy. Due to its ability of maintaining numerical stability and adding up on a basis, we believe that the perturbation like procedure can be pertinent to and useful for other problems, in the regard that perturbation techniques are applied by physicists to a wide range of problems.

This sort of ***2vec models was originally proposed [33, 34] and is widely used in natural language processing under the name word2vec. Since a language is a system that is built upon practice and convention, its evolving and form are not governed by fundamental laws as those in physical sciences. For this reason, previous usage of the models has been focused on reflecting similarity in statistical patterns. At the inter-discipline level, our work shows the possibility and viability of the application in situations where microscopic mechanism is in play. As reductionism is a paradigm of understanding physical and sociological phenomena, and vectorization is a general scheme of quantifying entities and concepts, the idea of PAE can be applicable far beyond usage in material discovery.

* wur@uci.edu

[1] K. T. Butler, D. W. Davies, H. Cartwright, O. Isayev, and A. Walsh, Nature **559**, 547 (2018).

[2] B. Sanchez-Lengeling and A. Aspuru-Guzik, Science **361**, 360 (2018).

[3] Y. Zhuo, A. Mansouri Tehrani, and J. Brgoch, The Journal of Physical Chemistry Letters **9**, 1668 (2018).

[4] L. Ward, A. Agrawal, A. Choudhary, and C. Wolverton, Npj Computational Materials **2**,

16028 (2016).

[5] J. E. Gubernatis and T. Lookman, Phys. Rev. Materials **2**, 120301 (2018).

[6] M. Scherbela, L. Hörmann, A. Jeindl, V. Obersteiner, and O. T. Hofmann, Phys. Rev. Materials **2**, 043803 (2018).

[7] P. Raccuglia, K. C. Elbert, P. D. F. Adler, C. Falk, M. B. Wenny, A. Mollo, M. Zeller, S. A. Friedler, J. Schrier, and A. J. Norquist, Nature **533**, 73 (2016).

[8] K. Ryan, J. Lengyel, and M. Shatruk, Journal of the American Chemical Society **140**, 10158 (2018).

[9] Q. Zhou, P. Tang, S. Liu, J. Pan, Q. Yan, and S.-C. Zhang, Proceedings of the National Academy of Sciences **115**, E6411 (2018).

[10] S. Jaeger, S. Fulle, and S. Turk, Journal of Chemical Information and Modeling **58**, 27 (2018).

[11] K. T. Schütt, F. Arbabzadah, S. Chmiela, K. R. Müller, and A. Tkatchenko, Nature Communications **8**, 13890 (2017).

[12] Q. Xu, Z. Li, M. Liu, and W.-J. Yin, The Journal of Physical Chemistry Letters **9**, 6948 (2018).

[13] M. Askerka, Z. Li, M. Lempen, Y. Liu, A. Johnston, M. I. Saidaminov, Z. Zajacz, and E. H. Sargent, Journal of the American Chemical Society **141**, 3682 (2019).

[14] K. T. Schütt, H. Glawe, F. Brockherde, A. Sanna, K. R. Müller, and E. K. U. Gross, Phys. Rev. B **89**, 205118 (2014).

[15] T. Xie and J. C. Grossman, Phys. Rev. Lett. **120**, 145301 (2018).

[16] D. Xue, P. V. Balachandran, J. Hogden, J. Theiler, D. Xue, and T. Lookman, Nature Communications **7**, 11241 (2016).

[17] Z. Zhou, X. Li, and R. N. Zare, ACS Central Science **3**, 1337 (2017).

[18] Y. F. Ye, Q. Wang, J. Lu, C. T. Liu, and Y. Yang, Materials Today **19**, 349 (2016).

[19] D. B. Miracle and O. N. Senkov, Acta Materialia **122**, 448 (2017).

[20] Y. Lederer, C. Toher, K. S. Vecchio, and S. Curtarolo, Acta Materialia **159**, 364 (2018).

[21] Z. Y., Y. J. Zhou, L. J. P., G. L. Chen, and P. K. Liaw, Adv. Eng. Mater. **10**, 534 (2008).

[22] M. C. Troparevsky, J. R. Morris, P. R. C. Kent, A. R. Lupini, and G. M. Stocks, Phys. Rev. X **5**, 011041 (2015).

[23] Y. Tan, J. Li, Z. Tang, J. Wang, and H. Kou, Journal of Alloys and Compounds **742**, 430 (2018).

[24] F. Tian, V. L. Károly, and L. Vitos, Intermetallics **83**, 9 (2017).

[25] Z. Wang, W. Qiu, Y. Yang, and C. T. Liu, Intermetallics **64**, 63 (2015).

[26] A. J. S. F. Tapia, D. Yim, H. S. Kim, and B.-J. Lee, Intermetallics **101**, 56 (2018).

[27] M. C. Gao and D. E. Alman, Entropy **15**, 4504 (2013).

[28] S. Guo, Q. Hu, C. Ng, and C. T. Liu, Intermetallics **41**, 96 (2013).

[29] X. Yang and Y. Zhang, Materials Chemistry and Physics **132**, 233 (2012).

[30] Y. F. Ye, Q. Wang, J. Lu, C. T. Liu, and Y. Yang, Scripta Materialia **104**, 53 (2015).

[31] C. Chattopadhyay, A. Prasad, and B. S. Murty, Acta Materialia **153**, 214 (2018).

[32] A. Jain, S. P. Ong, G. Hautier, W. Chen, W. D. Richards, S. Dacek, S. Cholia, D. Gunter, D. Skinner, G. Ceder, and K. a. Persson, APL Materials **1**, 011002 (2013).

[33] T. Mikolov, K. Chen, G. Corrado, and J. Dean, in *ICML2013* (2013).

[34] T. Mikolov, I. Sutskever, K. Chen, G. Corrado, and J. Dean, in *Advances in Neural Information Processing Systems 26* (2013) p. 31113119.