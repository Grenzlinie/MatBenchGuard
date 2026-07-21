# Hybrid localized graph kernel for machine learning energy-related properties of molecules and solids

Bastien Casier, $^{*, \dagger}$ Mauricio Chagas da Silva, $^{\dagger}$ Michael Badawi, $^{\dagger}$ Fabien Pascale, $^{\dagger}$ Tomáš Bučko, $^{\ddagger, \mathbb{I}}$ Sébastien Lebègue, $^{\dagger}$ and Dario Rocca $^{*, \dagger}$

$^{\dagger}$Université de Lorraine and CNRS, LPCT, UMR 7019, F-54000 Nancy, France

$^{\ddagger}$Department of Physical and Theoretical Chemistry, Faculty of Natural Sciences, Comenius University in Bratislava, Mlynská Dolina, Ilkovičova 6, SK-84215 Bratislava, Slovakia

$^{\mathbb{I}}$Institute of Inorganic Chemistry, Slovak Academy of Sciences, Dúbravská cesta 9, SK-84236 Bratislava, Slovakia

E-mail: bastien.casier@univ-lorraine.fr; dario.rocca@univ-lorraine.fr

## Abstract

Nowadays, the coupling of electronic structure and machine learning techniques serves as a powerful tool to predict chemical and physical properties of a broad range of systems. With the aim of improving the accuracy of predictions, a large number of representations for molecules and solids for machine learning applications has been developed. In this work we propose a novel descriptor based on the notion of molecular graph. While graphs are largely employed in classification problems in cheminformatics or bioinformatics, they are not often used in regression problem, especially of energy-related properties. Our method is based on a local decomposition of atomic environments and on the hybridization of two kernel functions: a graph kernel contribution that describes the chemical pattern and a Coulomb label contribution that

encodes finer details of the local geometry. The accuracy of this new kernel method in energy predictions of molecular and condensed phase systems is demonstrated by considering the popular QM7 and BA10 datasets. These examples show that the hybrid localized graph kernel outperforms traditional approaches such as, for example, the smooth overlap of atomic positions (SOAP) and the Coulomb matrices.

## 1 Introduction

The past decade has seen an impressive growth in the development and application of machine learning techniques¹ in quantum chemistry and computational condensed matter physics²⁻⁴. These methods are of a great interest for theoreticians because they allow for the analysis, classification and prediction of various properties conventionally requiring a large amount of data generated via computationally demanding quantum mechanical calculations⁵. Indeed, machine learning techniques can be applied to a broad range of problems, including, among the others, potential energy surface fitting⁶⁻⁹, *ab initio* molecular dynamics¹⁰⁻¹², prediction of various scalar properties¹³⁻¹⁵ (*e.g* atomization energies, polarizability coefficients, highest occupied molecular orbital energies, electronic structure correlation energies, *etc*), and vectorial and tensorial quantities (*e.g* forces, polarizability tensors, *etc*)¹⁶,¹⁷.

The chemical compound space is characteristic by a huge dimensionality and complexity. Datasets for molecules and solids proposed in the literature, which span only a small part of the chemical space, already contain impressively large numbers of compounds. The GDB-17 molecular dataset, for instance, contains 166 billions of molecules¹⁸. An example of a rich dataset of crystal structures is the set of elpasolites of Faber *et al.*¹⁹ containing 2 millions crystals. This shows clearly that it is impossible to analyze or screen all these compositions and structures by demanding electronic structure calculations². A solution to efficiently explore the chemical compound space (or at least significant parts of it) can be found in the development of new machine learning approaches to complement *ab initio* calculations. This field of research is known as quantum machine learning²⁰,²¹ (QML). The

main idea of the QML approaches is to train a machine learning model on a subset of chemical structures (the smallest possible) for which simulations at a quantum mechanical level were done. The trained machine is then used to predict the target properties of the rest of the systems. This technique can be applied not only in the chemical composition space but also in the conformation space of a given system. For example, recently, a $\Delta$-machine learning approach$^{22}$ based on thermodynamic perturbation theory has shown impressive results in the prediction of the adsorption enthalpy of small molecules adsorbed in chabazite at the random phase approximation (RPA) level of theory using only 10 training conformations$^{23}$. In general, the ultimate goal of QML would be to find a universal model which unifies both chemical and conformational spaces$^{21}$.

One of the main challenges in the use of QML methods is the choice of proper descriptors – *i.e.* features – to represent the molecular and/or condensed matter systems. In this work we will focus on structural descriptors, namely approaches that assume the knowledge of the precise geometry of the systems under consideration beyond their chemical composition. Currently, a large number of those descriptors have been proposed in the literature, with the symmetry functions$^{24}$, the Coulomb matrices$^{25–27}$, the smooth overlap of atomic positions (SOAP)$^{28,29}$ and the many-body tensor representation (MBTR)$^{30}$ being some of the most prominent examples. From a general point of view an efficient structural descriptor should satisfy certain prerequisites$^{3}$. For instance, the descriptor should be unique (one-to-one correspondence between features and systems) and invariant with respect to overall rotations and rigid translations, as well as permutations of atoms of the same type.

In the present work we introduce a new descriptor based on the notion of graph that satisfies all the above-mentioned conditions. Graphs are already largely used in the domain of cheminformatics$^{31–34}$ and bioinformatics$^{35,36}$ to predict the activity or the toxicity of particular drugs or to recognize particular patterns of binding site of biomolecules (with the quantitative structure-activity relationships (QSAR) model$^{37}$). Nevertheless, in these cases, the use of graphs is restricted to classification problems and their applications in regres-

sion problems are still rare, especially as far as energy-related properties are concerned $^{38-41}$.
These quantities are particularly sensitive to inner changes of the molecular structure which cannot be described by simple graphs whose edges are represented by 0's and 1's for disconnected and connected nodes (namely atoms) $^{42}$. Indeed, this simplified representation leads to isomorphic graphs even for rather different structures and this represents an issue for learning properties (e.g. the energy) which are very sensitive on the specific geometry of a system. To overcome this difficulty in the present work we used weighted graphs, whose values on the edges were obtained as superposition of atom-centered Gaussian functions. In order to develop a machine approach applicable to both molecules and solids we considered graphs defined in localized environments around each atom of a given system. These localized graphs were used as input features of a machine learning approach based on the kernel ridge regression $^{43}$ (KRR). This method scales cubically with the size of the training set but typically requires fewer data point to be trained than other traditional approaches (e.g. neural networks). The role of the kernel in KRR is to provide a measure of similarity between different localized graphs belonging to different systems. A global "comparison" of two systems (molecules or solids) can then be obtained by summing localized contributions from each atomic environment $^{29}$. The specific kernel used in this work combines two different parts: The first, based on a variant of the shortest-path kernel, is suited to describe structural motifs and chemical bonding between atoms; the second includes finer geometric details through a label enrichment of the nodes with Coulomb vectors. This approach can be viewed as an hybrid kernel function $^{44}$ and we will show that the introduction of both contributions provides a high level of accuracy. As a proof of principle this new methodology was applied to predict molecular atomization energies (QM7 dataset) and enthalpies of formations of solids (BA10 dataset).

The paper is organized as follows. In Sec. 2 the concept of labeled localized graph is introduced, which is represented trough maximum probability paths and enriched with a set of vectors that describe the Coulomb potential of the atomic environment. In the same

section, the new kernel approach is also presented. In Sec. 3 the datasets QM7 and BA10, used to evaluate our method are reviewed. Finally, our results for the prediction of the atomization energies of molecular systems (QM7 dataset) and the formation enthalpies for the solid state systems (BA10 dataset) are presented in Sec. 4.

## 2 Methodology

### 2.1 The Labeled Localized Graph Descriptor.

In this section we introduce the concept of labeled localized graph (LLG) for molecules and solids. By considering a local atomic environment $\mathcal{X}$ defined by a radius $r_{\text{cut}}$, a LLG, denoted as $\mathcal{G}_{\mathcal{X}}=(V,E)$, is composed by a set of vertices (nodes) $V=\{v_{i}\}_{i=1}^{N}$ and a set of edges $E=\{e_{i}\}_{i=1}^{M}$ - where $N$ and $M$ are associated with the number of atoms and the number of chemical bonds in the atomic environment, respectively$^{45,46}$. The LLG is said "labeled" if a label $l$ corresponding to the chemical symbol is attributed to each node $L(V)=\{l(v_{i})\}_{i=1}^{N}$ (see Fig. 1).

A simple unlabeled graph is usually represented through an adjacency matrix $\mathbf{A}(\mathcal{G}_{\mathcal{X}})\in\mathbb{R}^{N,N}$, whose elements $A_{ij}$ are set to one if two different nodes $i$ and $j$ are linked by an edge or to zero otherwise$^{45,47}$. However, the same graph would correspond to an infinite number of conformations through this definition: by changing the interatomic distances, as long as the edges are preserved (i.e. bonds are not broken), the corresponding graph will not change. This issue is particularly problematic for the prediction of total energy related properties (e.g. atomization energy), which are strongly influenced by the precise atomic conformation. For this reason in this work we use weighted adjacency matrices$^{38}$ which include significantly more information on the structure of the atomic environment. Specifically, a Gaussian function is attributed to each atomic position $\mathbf{r}_{i}$ in the atomic environment. Instead of considering only binary values for the off-diagonal elements of the adjacency matrix, weights

$w_{ij}$ between each pair of vertices $v_i$ and $v_j$ are set to correspond the overlap of these Gaussian functions, such that:

$$
w_{ij}(r_i^\mathrm{cov}, r_j^\mathrm{cov}, \gamma) = \int \phi_{r_i^\mathrm{cov},\gamma}(\|\mathbf{r} - \mathbf{r}_i\|)\phi_{r_j^\mathrm{cov},\gamma}(\|\mathbf{r} - \mathbf{r}_j\|)\mathrm{d}\mathbf{r} \, ,
\tag{1}
$$

with $\phi_{r_i^\mathrm{cov},\gamma}(\|\mathbf{r} - \mathbf{r}_i\|) = \frac{1}{(2\gamma\pi r_i^\mathrm{cov})^{3/2}} \exp\left[ -\left( \frac{\|\mathbf{r}-\mathbf{r}_i\|}{\sqrt{2\gamma}r_i^\mathrm{cov}} \right)^2 \right]$. Hence the weights depend on covalent radii $r_i^\mathrm{cov}$ (coming from crystallographic data $^{48}$) of all elements and on the hyperparameter $\gamma$ controlling the width of the Gaussian atomic distributions. Finally, a threshold $\epsilon$ is applied as follows:

$$
A_{ij}(\mathcal{G}_{\mathcal{X}}) = \left\{
\begin{array}{ll}
w_{ij} & \text{if } w_{ij} > \epsilon \\
0 & \text{otherwise}
\end{array}
\right. .
\tag{2}
$$

i.e., an edge between the two nodes $v_i$ and $v_j$ is defined when $w_{ij}$ is larger than epsilon (see Fig. 1). These weights can be interpreted intuitively as probabilities to "jump" from one atom to another atom.

![](./images/812406526508531713_1.jpg)

**Figure 1:** Illustration of a labeled localized graph (LLG) for a nitrogen atomic environment defined by a radius $r_\mathrm{cut}$. The overlaps of the Gaussian functions associated to each atom in this environment determine the weights in the adjacency matrix of the graph.

### 2.2 Maximum Probability Paths and Label Enrichment.

From the definition of the weighted adjacency matrix $\mathbf{A}(\mathcal{G}_{\mathcal{X}})$ in Eq. 2, we can determine a path $\pi(v_i, v_j)$ between each pair of vertices $(v_i, v_j)$ (we suppose here that each node is connected to at least one another node, as it is the case for all the systems studied in this work). This path is defined by a finite-length sequence of vertices $(v_i, \dots, v_k, \dots, v_j)$ with the property that $(v_k, v_{k+1}) \in E$ and $k = i, \dots, j - 1^{31,32,49}$. In this paper we will consider a machine learning approach based on a kernel that measures the similarity between paths. Specifically, we will focus on a variant of the shortest path (SP) kernel. While determining all paths of a graph is a NP-hard problem, computing the shortest path between pairs of vertices is a problem solvable in polynomial time $(\mathcal{O}(n^3))^{49}$.

Typically, the determination of the shortest path is based on the distance and on the triangular inequality (Floyd-Warshall algorithm) $^{50}$. Rather then directly using an approach based on shortest paths, in the context of the present work we found more natural to introduce the analogous concept of maximum probability path (MPP). In particular, interpreting the elements of the weighted adjacency matrix as transition probabilities between two nodes, a path is identified with the greatest overall probability expressed as the product of the weights associated with all the edges that are involved in the path. Mathematically, the probability of a certain path can be written as:

$$
\pi\left(v_{i}, v_{j}\right)=\prod_{k=i}^{j-1} w_{k, k+1}, \tag{3}
$$

where the intermediate indexes in the product correspond to all the nodes visited along the path. In order to find the MPP between two vertices, we modified the original Floyd-Warshall algorithm $^{49}$ (see Alg. 1).

Through our variant of the Floyd-Warshall algorithm, the matrix $\mathbf{A}(\mathcal{G}_{\mathcal{X}})$ is transformed into a new matrix $\mathbf{P}(\mathcal{G}_{\mathcal{X}})$ that can be interpreted as a fully connected graph in which the

```
Algorithm 1 The Floyd-Warshall algorithm for MPPs
Require: Weighted adjacency matrix $\mathbf{A}(\mathcal{G}_{\mathcal{X}})$
Ensure: MPPs matrix $\mathbf{P}(\mathcal{G}_{\mathcal{X}})$
  for k = 1 to N do
    for i = 1 to N do
      for j = 1 to N do
        if A[i,k]*A[k,j] > A[i,j] then
          A[i,j] = A[i,k]*A[k,j]
        end if
      end for
    end for
  end for
```

matrix elements $P_{ij}$ correspond to maximized overall probabilities of transition from the node $i$ to $j$. In our method, the MPPs are also labeled by a sequence of labels $l(\pi(v_i, v_j)) = (l(v_i), \dots, l(v_k), \dots, l(v_j))$. As discussed below (see Sec. 2.3 A.III), this is necessary in order to include information on atomic species so that only the MPPs involving the same sequences of atoms are compared (see Fig. 2).

The concepts described up to this point (weighted graphs and MPPs) allow for a rather accurate description of geometric motifs and bonding between atoms. However, these approaches are not sufficient to capture all the geometric details in atomic environments. Specifically, modifications (e.g. rotations) which preserve interatomic bond distances in the local environment leave the matrices $\mathbf{A}(\mathcal{G}_{\mathcal{X}})$ and $\mathbf{P}(\mathcal{G}_{\mathcal{X}})$ unchanged. These finer structural details, which are not captured by the MPP approach, might have different relevance depending on the specific dataset but, nevertheless, contribute to the non-uniqueness of the connection between localized graph and property to predict. To overcome this difficulty, we introduced a label enrichment of the vertices$^{31,32}$. Inspired by the Coulomb matrix descriptor introduced by Rupp et al.$^{25}$, we defined for each node a Coulomb vector $\mathbf{c}^{(i)}$ sorted according to the distances in increasing order whose components are defined as

$$
c_{j}^{(i)} = \frac{Z_i Z_j}{\|\mathbf{r}_j - \mathbf{r}_i\|}, \tag{4}
$$
```

![](./images/812406526508531713_2.jpg)

Figure 2: Illustration of the Floyd-Warshall transformation. The weighted adjacency matrix $\mathbf{A}(\mathcal{G}_{\mathcal{X}})$ is transformed into a path matrix $\mathbf{P}(\mathcal{G}_{\mathcal{X}})$. Each path between pairs of atoms is characterized by a sequence of labels $l(\pi(v_i, v_j))$ and a maximum probability path $\pi(v_i, v_j)$.

where $Z_i$, $Z_j$ are the nuclear charges. The superscript $i$ refers to the node which is labeled, while the subscript $j$ is an index that indicates all the other atoms in the environment of $i$ (see Fig. 3).

Because the atomic composition of environments can be different, to prevent any issue with dimensionality mismatch, the Coulomb vectors are padded with zeros to set their dimension to be equal and transferable. Finally, we obtain a new set of labels $C_{\mathcal{X}} = \{\mathbf{c}^{(i)}\}_{i=1}^N$ that takes into account the missing geometric information in the description of atomic environments.

### Atomic environment $\mathcal{X}$

![](./images/812406526508531713_3.jpg)

**Figure 3:** Illustration of the labels enrichment of nodes. In the atomic environment $\mathcal{X}$ to each node it is associated a sorted Coulomb vector $\mathbf{c}^{(i)}$. Example with the carbon atom :
$$
\mathbf{c}^{(\mathrm{C})} = \left\{ \frac{Z_{\mathrm{C}}Z_{\mathrm{N}}}{\left\|\mathbf{r}_{\mathrm{N}}-\mathbf{r}_{\mathrm{C}}\right\|}, \frac{Z_{\mathrm{C}}Z_{\mathrm{H}_1}}{\left\|\mathbf{r}_{\mathrm{H}_1}-\mathbf{r}_{\mathrm{C}}\right\|}, \frac{Z_{\mathrm{C}}Z_{\mathrm{H}_2}}{\left\|\mathbf{r}_{\mathrm{H}_2}-\mathbf{r}_{\mathrm{C}}\right\|} \right\}.
$$

## 2.3 The Hybrid Maximum Probability Path (HMPP) Kernel.

The main idea of kernel approaches consists in finding an accurate measure of the similarity between pairs of data points (atomic environments in our case). For example, in the SOAP kernel, the similarity is determined through an overlap calculation of the atomic density of two atomic environments$^{28,29}$. When normalized, the kernel is close to one when two atomic environments are nearly identical and tends to zero if they are dissimilar.

In our approach, an atomic environment $\mathcal{X}$ is characterized by a set of MPPs between all pairs of nodes $P_{ij}(\mathcal{G}_{\mathcal{X}}) = \pi(v_i, v_j)$, with their respective labels $L(\mathbf{P}(\mathcal{G}_{\mathcal{X}})) = \left\{l(\pi(v_i, v_j))\right\}_{i=1,j=1}^{N,N}$ and a set of Coulomb vectors $C_{\mathcal{X}} = \left\{\mathbf{c}^{(i)}\right\}_{i=1}^{N}$ (see Sec 2.2). Being inspired by the iterative similarity for molecular graphs introduced by Rupp *et al.*$^{51}$, where the use of a linear combination of two kernels applied to vertices and edges was proposed, the

following hybrid kernel is introduced to compare the atomic environments (see also Fig. 4):

$$
k(\mathcal{X}, \mathcal{Y})=(1-\alpha) k_{\mathrm{MPP}}\left(\mathcal{G}_{\mathcal{X}}, \mathcal{G}_{\mathcal{Y}}\right)+\alpha k_{\mathrm{Coulomb}}\left(C_{\mathcal{X}}, C_{\mathcal{Y}}\right). \tag{5}
$$

This kernel is normalized via Tanimoto's normalization $^{45}$:

$$
k(\mathcal{X}, \mathcal{Y})=\frac{k(\mathcal{X}, \mathcal{Y})}{k(\mathcal{X}, \mathcal{X})+k(\mathcal{Y}, \mathcal{Y})-k(\mathcal{X}, \mathcal{Y})}, \tag{6}
$$

which is commonly used also in other graphs application $^{45-47,52}$. This normalization can be seen as a Jaccard's distance – i.e. measuring how two sets intersect – between two discrete collections of paths and vertices. The kernel $k(\mathcal{X}, \mathcal{Y})$ is positive semidefinite $^{52}$, as required for use in kernel-based machine learning algorithms.

To compare graph paths, we have chosen an approach similar to the labeled shortest path graph kernel $^{49}$. In its original definition this kernel could take values different from 0 only when applied to pairs of (shortest) paths with the same initial and final labels $^{49}$. In this work we found that this formulation does not reach a satisfactory level of accuracy. Indeed, even if the initial and final nodes of a pair of MPPs have the same "atomic" labels (namely they correspond to the same atomic species), the intermediate paths could be significantly different from a chemical point of view (i.e. involve different elements) and still be considered as similar according to this original definition of the kernel. For this reason in the present work we used an MPP kernel which is strictly 0 unless the two paths to be compared have exactly the same sequence of atomic labels $l(\pi)$. This kernel can be expressed as follows:

$$
k_{\mathrm{MPP}}\left(\mathcal{G}_{\mathcal{X}}, \mathcal{G}_{\mathcal{Y}}\right)=\sum_{\pi_{\mathcal{X}} \in \mathbf{P}\left(\mathcal{G}_{\mathcal{X}}\right)} \sum_{\pi_{\mathcal{Y}} \in \mathbf{P}\left(\mathcal{G}_{\mathcal{Y}}\right)} \delta_{\mathrm{Label}}\left(l\left(\pi_{\mathcal{X}}\right), l\left(\pi_{\mathcal{Y}}\right)\right) \cdot k_{\mathrm{Path}}\left(\pi_{\mathcal{X}}, \pi_{\mathcal{Y}}\right), \tag{7}
$$

where the $\delta_{\text{Label}}\left(l\left(\pi_{\mathcal{X}}\right), l\left(\pi_{\mathcal{Y}}\right)\right)$ is a delta kernel applied on the path labels such that:

$$
\delta_{\text{Label}}\left(l\left(\pi_{\mathcal{X}}\right), l\left(\pi_{\mathcal{Y}}\right)\right)=
\begin{cases}
1 & \text{if } l\left(\pi_{\mathcal{X}}\right)=l\left(\pi_{\mathcal{Y}}\right) \\
0 & \text{otherwise}
\end{cases}. \tag{8}
$$

This kernel is equal to one if, and only if, the sequences of labels along $\pi_{\mathcal{X}}$ and $\pi_{\mathcal{Y}}$ are identical. The term $k_{\text{Path}}\left(\pi_{\mathcal{X}}, \pi_{\mathcal{Y}}\right)$ is the Laplacian kernel$^{53}$

$$
k_{\text{Path}}\left(\pi_{\mathcal{X}}, \pi_{\mathcal{Y}}\right)=e^{-\beta_{1}\left|\pi_{\mathcal{X}}-\pi_{\mathcal{Y}}\right|}, \tag{9}
$$

used to compare pairs of MPPs. Similarly, the Coulomb labels are compared through a sum of Laplacian kernel functions:

$$
k_{\text{Coulomb}}(C_{\mathcal{X}}, C_{\mathcal{Y}})=\sum_{i=1}^{N} \sum_{j=1}^{N^{\prime}} e^{-\beta_{2}\left|\mathbf{c}^{(i)}-\mathbf{c}^{(j)}\right|}, \tag{10}
$$

where $N$ and $N'$ denote the number of atoms in the atomic environments $\mathcal{X}$ and $\mathcal{Y}$, respectively, and $\beta_1$ and $\beta_2$ are the hyperparameters that control the decay of the Laplacian kernel functions. They play a central role in the prediction quality and are estimated through a grid search using a validation dataset. The relative importance of the two kernels $k_{\text{MPP}}$ and $k_{\text{Coulomb}}$ in the description of a given system is controlled by the hyperparameter $\alpha$ in Eq. 5.

## 3 Benchmarks

To demonstrate the accuracy of our hybrid graph kernel approach we applied it to two regression problems of energy-related properties and compared its performance to that of the popular SOAP descriptor$^{28,29}$ and graph approximated energy (GRAPE)$^{38}$. The machine learning models were based on in-house programs written in Python3 employing the DScribe$^{54}$ and the SciKit-Learn$^{55}$ libraries implementing the SOAP descriptors and KRR routines, respectively.

![](./images/812406526508531713_4.jpg)

![](./images/812406526508531713_5.jpg)

$$
\begin{aligned}
&\pi(\mathrm{H}_{1}, \mathrm{N}) \quad \begin{tikzpicture}[baseline=(current bounding box.center), node distance=0.8cm]
\node[draw, circle] (H1) {$\mathrm{H}_{1}$};
\node[draw, circle, right of=H1] (N) {$\mathrm{N}$};
\draw (H1) -- (N);
\end{tikzpicture} \quad
\begin{tikzpicture}[baseline=(current bounding box.center), scale=0.5]
\foreach \x in {1,2,3} \foreach \y in {1,2,3} \node[draw, circle] at (\x,\y) {};
\foreach \x in {1,2,3} \foreach \y in {1,2,3} \foreach \a in {1,2,3} \foreach \b in {1,2,3} \draw (\x,\y) -- (\a,\b);
\foreach \x in {1,2,3} \draw[red] (\x,1) -- (\x,3);
\end{tikzpicture} \quad
\begin{tikzpicture}[baseline=(current bounding box.center), node distance=0.8cm]
\node[draw, circle] (N) {$\mathrm{N}$};
\node[draw, circle, right of=N] (H) {$\mathrm{H}$};
\draw (N) -- (H);
\end{tikzpicture} \quad \pi(\mathrm{H}, \mathrm{N}) \\
&\pi(\mathrm{H}_{2}, \mathrm{N}) \quad \begin{tikzpicture}[baseline=(current bounding box.center), node distance=0.8cm]
\node[draw, circle] (H2) {$\mathrm{H}_{2}$};
\node[draw, circle, right of=H2] (N) {$\mathrm{N}$};
\draw (H2) -- (N);
\end{tikzpicture} \quad
\begin{tikzpicture}[baseline=(current bounding box.center), node distance=0.8cm]
\node[draw, circle] (N) {$\mathrm{N}$};
\node[draw, circle, right of=N, fill=gray] (C1) {$\mathrm{C}_{1}$};
\draw (N) -- (C1);
\end{tikzpicture} \quad \pi(\mathrm{C}_{1}, \mathrm{N}) \\
&\pi(\mathrm{C}, \mathrm{N}) \quad \begin{tikzpicture}[baseline=(current bounding box.center), node distance=0.8cm]
\node[draw, circle, fill=gray] (C) {$\mathrm{C}$};
\node[draw, circle, right of=C] (N) {$\mathrm{N}$};
\draw (C) -- (N);
\end{tikzpicture} \quad
\begin{tikzpicture}[baseline=(current bounding box.center), node distance=0.8cm]
\node[draw, circle] (N) {$\mathrm{N}$};
\node[draw, circle, right of=N, fill=gray] (C2) {$\mathrm{C}_{2}$};
\draw (N) -- (C2);
\end{tikzpicture} \quad \pi(\mathrm{C}_{2}, \mathrm{N}) \\
&\pi(\mathrm{H}_{2}, \mathrm{H}_{1}) \quad \begin{tikzpicture}[baseline=(current bounding box.center), node distance=0.8cm]
\node[draw, circle] (H2) {$\mathrm{H}_{2}$};
\node[draw, circle, right of=H2] (N) {$\mathrm{N}$};
\node[draw, circle, right of=N] (H1) {$\mathrm{H}_{1}$};
\draw (H2) -- (N) -- (H1);
\end{tikzpicture} \quad
\begin{tikzpicture}[baseline=(current bounding box.center), node distance=0.8cm]
\node[draw, circle] (H) {$\mathrm{H}$};
\node[draw, circle, right of=H] (N) {$\mathrm{N}$};
\node[draw, circle, right of=N, fill=gray] (C1) {$\mathrm{C}_{1}$};
\draw (H) -- (N) -- (C1);
\end{tikzpicture} \quad \pi(\mathrm{C}_{1}, \mathrm{H}) \\
&\pi(\mathrm{C}, \mathrm{H}_{1}) \quad \begin{tikzpicture}[baseline=(current bounding box.center), node distance=0.8cm]
\node[draw, circle, fill=gray] (C) {$\mathrm{C}$};
\node[draw, circle, right of=C] (N) {$\mathrm{N}$};
\node[draw, circle, right of=N] (H1) {$\mathrm{H}_{1}$};
\draw (C) -- (N) -- (H1);
\end{tikzpicture} \quad
\begin{tikzpicture}[baseline=(current bounding box.center), node distance=0.8cm]
\node[draw, circle] (H) {$\mathrm{H}$};
\node[draw, circle, right of=H] (N) {$\mathrm{N}$};
\node[draw, circle, right of=N, fill=gray] (C2) {$\mathrm{C}_{2}$};
\draw (H) -- (N) -- (C2);
\end{tikzpicture} \quad \pi(\mathrm{C}_{2}, \mathrm{H}) \\
&\pi(\mathrm{C}, \mathrm{H}_{2}) \quad \begin{tikzpicture}[baseline=(current bounding box.center), node distance=0.8cm]
\node[draw, circle, fill=gray] (C) {$\mathrm{C}$};
\node[draw, circle, right of=C] (N) {$\mathrm{N}$};
\node[draw, circle, right of=N] (H2) {$\mathrm{H}_{2}$};
\draw (C) -- (N) -- (H2);
\end{tikzpicture} \quad
\begin{tikzpicture}[baseline=(current bounding box.center), node distance=0.8cm]
\node[draw, circle, fill=gray] (C1) {$\mathrm{C}_{1}$};
\node[draw, circle, right of=C1] (N) {$\mathrm{N}$};
\node[draw, circle, right of=N, fill=gray] (C2) {$\mathrm{C}_{2}$};
\draw (C1) -- (N) -- (C2);
\end{tikzpicture} \quad \pi(\mathrm{C}_{2}, \mathrm{C}_{1})
\end{aligned}
$$

$$
k_{\mathrm{MPP}}(\mathcal{G}_{\mathcal{X}}, \mathcal{G}_{\mathcal{Y}}) = \sum_{\pi_{\mathcal{X}} \in \mathbf{P}(\mathcal{G}_{\mathcal{X}})} \sum_{\pi_{\mathcal{Y}} \in \mathbf{P}(\mathcal{G}_{\mathcal{Y}})} \delta_{\mathrm{Label}}\left(l(\pi_{\mathcal{X}}), l(\pi_{\mathcal{Y}})\right) \cdot k_{\mathrm{Path}}(\pi_{\mathcal{X}}, \pi_{\mathcal{Y}})
$$

$$
\begin{aligned}
&\mathbf{c}(\mathbf{r}_{\mathrm{N}}) = \left\{ \frac{Z_{\mathrm{N}} Z_{\mathrm{H}_1}}{\|\mathbf{r}_{\mathrm{H}_1} - \mathbf{r}_{\mathrm{N}}\|}, \frac{Z_{\mathrm{N}} Z_{\mathrm{H}_2}}{\|\mathbf{r}_{\mathrm{H}_2} - \mathbf{r}_{\mathrm{N}}\|}, \frac{Z_{\mathrm{N}} Z_{\mathrm{C}}}{\|\mathbf{r}_{\mathrm{C}} - \mathbf{r}_{\mathrm{N}}\|} \right\} \quad
\begin{tikzpicture}[baseline=(current bounding box.center)]
\node[draw, circle, fill=blue] (N) {$\mathrm{N}$};
\end{tikzpicture} \quad
\begin{tikzpicture}[baseline=(current bounding box.center), scale=0.4]
\foreach \x in {1,2,3} \foreach \y in {1,2,3} \node[draw, circle] at (\x,\y) {};
\foreach \x in {1,2,3} \foreach \y in {1,2,3} \foreach \a in {1,2,3} \foreach \b in {1,2,3} \draw (\x,\y) -- (\a,\b);
\end{tikzpicture} \quad
\begin{tikzpicture}[baseline=(current bounding box.center)]
\node[draw, circle, fill=blue] (N) {$\mathrm{N}$};
\end{tikzpicture} \quad \mathbf{c}(\mathbf{r}_{\mathrm{N}}) = \left\{ \frac{Z_{\mathrm{N}} Z_{\mathrm{H}}}{\|\mathbf{r}_{\mathrm{H}} - \mathbf{r}_{\mathrm{N}}\|}, \frac{Z_{\mathrm{N}} Z_{\mathrm{C}_1}}{\|\mathbf{r}_{\mathrm{C}_1} - \mathbf{r}_{\mathrm{N}}\|}, \frac{Z_{\mathrm{N}} Z_{\mathrm{C}_2}}{\|\mathbf{r}_{\mathrm{C}_2} - \mathbf{r}_{\mathrm{N}}\|} \right\} \\
&\mathbf{c}(\mathbf{r}_{\mathrm{H}_1}) = \left\{ \frac{Z_{\mathrm{H}_1} Z_{\mathrm{N}}}{\|\mathbf{r}_{\mathrm{N}} - \mathbf{r}_{\mathrm{H}_1}\|}, \frac{Z_{\mathrm{H}_1} Z_{\mathrm{H}_2}}{\|\mathbf{r}_{\mathrm{H}_2} - \mathbf{r}_{\mathrm{H}_1}\|}, \frac{Z_{\mathrm{H}_1} Z_{\mathrm{C}}}{\|\mathbf{r}_{\mathrm{C}} - \mathbf{r}_{\mathrm{H}_1}\|} \right\} \quad
\begin{tikzpicture}[baseline=(current bounding box.center)]
\node[draw, circle] (H1) {$\mathrm{H}_1$};
\end{tikzpicture} \quad
\begin{tikzpicture}[baseline=(current bounding box.center)]
\node[draw, circle] (H) {$\mathrm{H}$};
\end{tikzpicture} \quad \mathbf{c}(\mathbf{r}_{\mathrm{H}}) = \left\{ \frac{Z_{\mathrm{H}} Z_{\mathrm{N}}}{\|\mathbf{r}_{\mathrm{N}} - \mathbf{r}_{\mathrm{H}}\|}, \frac{Z_{\mathrm{H}} Z_{\mathrm{C}_1}}{\|\mathbf{r}_{\mathrm{C}_1} - \mathbf{r}_{\mathrm{H}}\|}, \frac{Z_{\mathrm{H}} Z_{\mathrm{C}_2}}{\|\mathbf{r}_{\mathrm{C}_2} - \mathbf{r}_{\mathrm{H}}\|} \right\} \\
&\mathbf{c}(\mathbf{r}_{\mathrm{H}_2}) = \left\{ \frac{Z_{\mathrm{H}_2} Z_{\mathrm{N}}}{\|\mathbf{r}_{\mathrm{N}} - \mathbf{r}_{\mathrm{H}_2}\|}, \frac{Z_{\mathrm{H}_2} Z_{\mathrm{H}_1}}{\|\mathbf{r}_{\mathrm{H}_1} - \mathbf{r}_{\mathrm{H}_2}\|}, \frac{Z_{\mathrm{H}_2} Z_{\mathrm{C}}}{\|\mathbf{r}_{\mathrm{C}} - \mathbf{r}_{\mathrm{H}_2}\|} \right\} \quad
\begin{tikzpicture}[baseline=(current bounding box.center)]
\node[draw, circle] (H2) {$\mathrm{H}_2$};
\end{tikzpicture} \quad
\begin{tikzpicture}[baseline=(current bounding box.center)]
\node[draw, circle, fill=gray] (C1) {$\mathrm{C}_1$};
\end{tikzpicture} \quad \mathbf{c}(\mathbf{r}_{\mathrm{C}_1}) = \left\{ \frac{Z_{\mathrm{C}_1} Z_{\mathrm{N}}}{\|\mathbf{r}_{\mathrm{N}} - \mathbf{r}_{\mathrm{C}_1}\|}, \frac{Z_{\mathrm{C}_1} Z_{\mathrm{H}}}{\|\mathbf{r}_{\mathrm{H}} - \mathbf{r}_{\mathrm{C}_1}\|}, \frac{Z_{\mathrm{C}_1} Z_{\mathrm{C}_2}}{\|\mathbf{r}_{\mathrm{C}_2} - \mathbf{r}_{\mathrm{C}_1}\|} \right\} \\
&\mathbf{c}(\mathbf{r}_{\mathrm{C}}) = \left\{ \frac{Z_{\mathrm{C}} Z_{\mathrm{N}}}{\|\mathbf{r}_{\mathrm{N}} - \mathbf{r}_{\mathrm{C}}\|}, \frac{Z_{\mathrm{C}} Z_{\mathrm{H}_1}}{\|\mathbf{r}_{\mathrm{H}_1} - \mathbf{r}_{\mathrm{C}}\|}, \frac{Z_{\mathrm{C}} Z_{\mathrm{H}_2}}{\|\mathbf{r}_{\mathrm{H}_2} - \mathbf{r}_{\mathrm{C}}\|} \right\} \quad
\begin{tikzpicture}[baseline=(current bounding box.center)]
\node[draw, circle, fill=gray] (C) {$\mathrm{C}$};
\end{tikzpicture} \quad
\begin{tikzpicture}[baseline=(current bounding box.center)]
\node[draw, circle, fill=gray] (C2) {$\mathrm{C}_2$};
\end{tikzpicture} \quad \mathbf{c}(\mathbf{r}_{\mathrm{C}_2}) = \left\{ \frac{Z_{\mathrm{C}_2} Z_{\mathrm{N}}}{\|\mathbf{r}_{\mathrm{N}} - \mathbf{r}_{\mathrm{C}_2}\|}, \frac{Z_{\mathrm{C}_2} Z_{\mathrm{H}}}{\|\mathbf{r}_{\mathrm{H}} - \mathbf{r}_{\mathrm{C}_2}\|}, \frac{Z_{\mathrm{C}_2} Z_{\mathrm{C}_1}}{\|\mathbf{r}_{\mathrm{C}_1} - \mathbf{r}_{\mathrm{C}_2}\|} \right\}
\end{aligned}
$$

$$
k_{\text{Coulomb}}(C_{\mathcal{X}}, C_{\mathcal{Y}}) = \sum_{i=1}^{N} \sum_{j=1}^{N'} e^{-\beta_2 |\mathbf{c}^{(i)} - \mathbf{c}^{(j)}|}
$$

Figure 4: Illustration of the hybrid maximum probability path kernel. The calculation is based on two similarity measurements, one on the paths of atomic environments and the other one on the Coulomb labels of the nodes.

### 3.1 The QM7 dataset.

The QM7 dataset consists of atomization energies for a total of 7165 organic molecules $^{25,56,57}$.
The individual molecules are composed of up to 23 atoms and contain at most five different elements involving H, C, N, O and S. The atomization energies, which span a range between -2000 to -800 kcal/mol, have been computed using density functional theory (DFT) $^{58}$ within the Perdew-Burke-Ernzerhof (PBE) $^{59}$ parameterization of the generalized gradient approximation.

Using the five-fold partitioning originally proposed by Rupp *et al.*$^{25}$ and following the work of Ferré *et al.*$^{38}$, we considered the first $N$ molecules (with $N = 100$, 300, 500 and 1000 points) of the first fold as a training set. The second and third folds were combined to create a validation set for the grid search of the optimal hyperparameters, which, in the case of the HMPP kernel include the parameters $r_{\text{cut}}$, $\gamma$, $\beta_1$, $\beta_2$ and $\alpha$. Finally, the two last folds were used as a test set to evaluate the accuracy of the model through the mean absolute error (MAE) and the root mean square error (RMSE) of predicted energies.

### 3.2 The BA10 dataset.

The BA10 dataset contains standard enthalpies of formation for a set of ten binary alloys (AgCu, AlFe, AlMg, AlNi, AlTi, CoNi, CuFe, CuNi, FeV and NbNi) represented by 1595 configurations each$^{60}$ (*i.e.* altogether 15950 configurations). The corresponding alloys are obtained considering all the possible unit cells with 1 to 8 atoms for the face-centered cubic (fcc) and body-centered cubic (bcc) Bravais lattices, and all the possible cells with 2 to 8 atoms for the hexagonal close-packed (hcp) symmetry. The crystal structures were determined using the Hart and Forcade algorithm$^{61}$ and the lattice parameters were set according to the Vergard's law$^{60}$. Finally, the standard enthalpies of formation were computed through the Vienna Ab initio Simulation Package$^{62,63}$ (VASP) at the DFT/PBE$^{59}$ level of theory without geometric relaxation. More details on this dataset can be found in the orig-

inal article of Nyshadham et al. $^{60}$.

The hyperparameters were optimized on the configurations of the alloy AgCu. Specifi- cally, by training the machine learning models on 100 randomly chosen points we determined the optimal hyperparameters on an independent validation set composed by other 100 ran- domly chosen structures. The set of hyperparameters determined for AgCu has then been used for all the other compounds. This procedure allowed us to evaluate the transferability of the hyperparameters into the alloy space. Within this approach we have studied for each alloy the influence of the training set size on the quality of predictions. To this end, we considered four different training sets with $N=100$, 300, 500 and 1000 configurations. As in the case of the QM7 dataset (see Sec. 3.1), the regression quality was quantified trough the MAE and the RMSE evaluated for the predicted energies on a test set composed by the rest of the structures (i.e. $1595-N$ configurations per alloy).

## 4 Results and Discussion

### 4.1 Optimization of the hyperparameters

The determination of the hyperparameters was conducted on a hold-out validation set through a five-dimensional grid search for the parameters $r_{\text{cut}}$, $\gamma$, $\beta_1$, $\beta_2$, and $\alpha$. The cutoff radius $r_{\text{cut}}$, that defines the size of each atomic environment, was evaluated in the interval between 1.6 and $2.4\ \text{\AA}$ with an increment of $0.2\ \text{\AA}$ for the QM7 dataset, and between 2.0 to $5.0\ \text{\AA}$ with an increment of $1.0\ \text{\AA}$ for the BA10 dataset. The values of $1.8\ \text{\AA}$ and $3.0\ \text{\AA}$ were identified as optimal for the QM7 and BA10 datasets, respectively. The scaling factor $\gamma$, that governs the width of the atomic Gaussian functions, was tested in the range from 0.1 to $0.9\ \text{\AA}$ with a step of $0.2\ \text{\AA}$; the optimal values of $0.5\ \text{\AA}$ and $0.5\ \text{\AA}$ have been identified for the QM7 and BA10 datasets, respectively.

The two hyperparameters $\beta_1$ and $\beta_2$ that define the decay rate of the two exponential

functions in the $k_{\text{MPP}}$ and $k_{\text{Coulomb}}$ kernels were evaluated on a decimal logarithmic grid defined on the interval between $10^{-1}$ to $10^{-4}$. For both the datasets considered here, the optimal hyperparameters values were found to be 0.1 and 0.001 for $\beta_1$ and $\beta_2$, respectively. Compared to the other three parameters in the model, $\beta_1$ and $\beta_2$ seem to have a weaker system dependence and could be possibly transferred across different datasets. Although this observation should be confirmed by future investigations on several different datasets, the possibility of fixing $\beta_1$ and $\beta_2$ a priori could help to simplify the hyperparameter optimization procedure.

The $\alpha$ parameter, that describes the relative contribution of the kernels $k_{\text{MPP}}$ and $k_{\text{Coulomb}}$, was tuned by considering values between 0 to 1 with a step of 0.1. For the QM7 dataset, a relatively small $\alpha$ (0.2) exhibited the best performance, while a significantly higher value (0.9) was identified for the dataset BA10. It is important to notice that the hybridization brings important improvements with respect to the sole use of the best performing between the $k_{\text{MPP}}$ and $k_{\text{Coulomb}}$ kernels (for the smallest training sets considered below the hybridization lowers the mean absolute error by 35 % and 17 % for QM7 and BA10, respectively).

## 4.2 Prediction of the atomization energies.

In this section we test the performance of the HMPP kernel in predicting the atomization energies of the molecules in the QM7 dataset. Table 1 and Figure 5 show the variation of the MAEs and RMSEs as a function of the training set size. For the sake of comparison we also show results for some other well established approaches, namely the SOAP kernel and GRAPE, the latter being a localized graph kernel method previously reported in the literature$^{38}$ and applied to regression problems. The results for the different methods have been generated using the same training sets and analogous procedures for the optimization of the hyperparameters. We observe that the HMPP kernel outperforms the other two methods regardless of the training set size. It is important to notice that in Ref. 37 the results reported for the GRAPE kernel slightly improved over the SOAP method (which is

in contrast to our results from Table 1 and Figure 5). However, the authors of this work clearly stated that the tuning of the hyperparameters was limited and that, accordingly, it was not possible to conclude "that one method outperforms the other". The MAEs and RMSEs reported in Table 1 for GRAPE and SOAP are also sizeably smaller than those in Ref. 37, demonstrating the importance of a fine tuning of the model hyperparameters to fully establish the accuracy of a certain approach.

![](./images/812406526508531713_6.jpg)

![](./images/812406526508531713_7.jpg)

Figure 5: Variation of the quality of predictions of atomization energies (QM7 dataset) of the three kernels studied in this work (SOAP, GRAPE and HMPP) with the training set size as measured by the mean absolute error (MAE) and the root mean square error (RMSE). The values are given in kcal/mol (See also Table 1).

The GRAPE kernel uses a random walk kernel directly applied on the weighted adjacency matrix. Within this approach, each component of the adjacency matrix is defined through an overlap of atomic Gaussian functions of the same width. However, we can observe that this use of graphs does not reach a satisfactory level of accuracy, as shown by the high MAE and RMSE values in Table 1 and Figure 5. This is likely related to the lack of labels in the GRAPE approach. Tang and de Jong have proposed in 2019 a marginalized graph kernel to predict the atomization energies and have obtained impressive results with the introduction of labels⁴¹. However, the reported model was based on a global description of the molecular graphs and, differently from our present approach, the corresponding graph kernel cannot

Table 1: Variation of mean absolute error (MAE) and the root mean square error (RMSE) (in kcal/mol) of atomization energies (QM7 dataset) obtained using the SOAP, GRAPE and HMPP kernels with the training set size (cf. Figure 5).

<table>
<thead>
<tr>
<th></th>
<th>100 points</th>
<th>300 points</th>
<th>500 points</th>
<th>1000 points</th>
</tr>
</thead>
<tbody>
<tr>
<th>SOAP</th>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<th>MAE</th>
<td>8.38</td>
<td>5.80</td>
<td>4.39</td>
<td>3.71</td>
</tr>
<tr>
<th>RMSE</th>
<td>11.44</td>
<td>8.34</td>
<td>6.87</td>
<td>6.01</td>
</tr>
<tr>
<th>GRAPE</th>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<th>MAE</th>
<td>10.48</td>
<td>8.02</td>
<td>7.65</td>
<td>7.25</td>
</tr>
<tr>
<th>RMSE</th>
<td>14.76</td>
<td>11.65</td>
<td>11.31</td>
<td>10.71</td>
</tr>
<tr>
<th>HMPP</th>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<th>MAE</th>
<td>6.69</td>
<td>3.96</td>
<td>3.01</td>
<td>2.56</td>
</tr>
<tr>
<th>RMSE</th>
<td>9.76</td>
<td>6.67</td>
<td>5.89</td>
<td>4.91</td>
</tr>
</tbody>
</table>

be applied to solid state systems in a straightforward way.

In Table 2 we show the values of MAE and RMSE obtained for larger training set sizes. Specifically, two additional training sets with 2000 and 5000 data points were built through a random sampling without stratification of the data. In this table, the results that we obtained for the HMPP, SOAP, and GRAPE kernel methods are compared with some other results presented in the literature obtained using different kernels and/or descriptors. Since different training sets are used in different papers, such a comparison can be considered as only qualitative. Nevertheless, the results compiled in Table 2 clearly show that the HMPP approach is competitive with more traditional approaches. In particular, our HMPP kernel is more accurate than the GRAPE, SOAP (average kernel AK), and Coulomb matrix (CM) approaches while its performance is comparable to the global molecular graph (GMG)$^{41}$ and bag of bonds (BoB)$^{64}$ methods. It is important to further stress that comparison of our results with those produced by different groups can be only qualitative, as a stratification of the data was used for most of the results in the literature and, in the case of the BoB, an even larger training set was considered (5732 data points).

**Table 2:** MAEs and RMSEs (in kcal/mol) determined for atomization energy predictions (QM7 dataset) made using different state-of-the-art methods trained on large training sets. The results obtained using the HMPP kernel proposed in this work are in bold.

List of abbreviations: Hybrid maximum probability path (HMPP), Graph approximated energy (GRAPE), Smooth overlap of atomic positions (SOAP), Global molecular graph (GMG), Coulomb matrix (CM), Bag of Bond (BoB), (Localized) graph kernel ((L)GK), Average kernel (AK), Regularized entropy match (REMatch), Kernel ridge regression (KRR), Gaussian process regression (GPR).

<table>
<thead>
<tr>
<th>Training set</th>
<th>Representation</th>
<th>Kernel</th>
<th>Regression</th>
<th>MAE</th>
<th>RMSE</th>
<th>Source</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>2000, random</strong></td>
<td><strong>HMPP</strong></td>
<td><strong>LGK</strong></td>
<td><strong>KRR</strong></td>
<td><strong>1.87</strong></td>
<td><strong>4.17</strong></td>
<td><strong>This work</strong></td>
</tr>
<tr>
<td>2000, random</td>
<td>GRAPE</td>
<td>LGK</td>
<td>KRR</td>
<td>7.00</td>
<td>10.21</td>
<td>This work</td>
</tr>
<tr>
<td>2000, random</td>
<td>SOAP</td>
<td>AK</td>
<td>KRR</td>
<td>2.95</td>
<td>4.61</td>
<td>This work</td>
</tr>
<tr>
<td>2000, random</td>
<td>GMG</td>
<td>GK</td>
<td>GPR</td>
<td>1.48</td>
<td>3.57</td>
<td>41</td>
</tr>
<tr>
<td>2000, stratified</td>
<td>CM</td>
<td>Laplacian</td>
<td>KRR</td>
<td>4.32</td>
<td>...</td>
<td>65</td>
</tr>
<tr>
<td><strong>5000, random</strong></td>
<td><strong>HMPP</strong></td>
<td><strong>LGK</strong></td>
<td><strong>KRR</strong></td>
<td><strong>1.59</strong></td>
<td><strong>3.07</strong></td>
<td><strong>This work</strong></td>
</tr>
<tr>
<td>5000, random</td>
<td>GRAPE</td>
<td>LGK</td>
<td>KRR</td>
<td>6.99</td>
<td>10.05</td>
<td>This work</td>
</tr>
<tr>
<td>5000, random</td>
<td>SOAP</td>
<td>AK</td>
<td>KRR</td>
<td>2.59</td>
<td>3.63</td>
<td>This work</td>
</tr>
<tr>
<td>5000, random</td>
<td>GMG</td>
<td>GK</td>
<td>GPR</td>
<td>1.01</td>
<td>2.29</td>
<td>41</td>
</tr>
<tr>
<td>5000, stratified</td>
<td>SOAP</td>
<td>REMatch</td>
<td>KRR</td>
<td>0.92</td>
<td>1.61</td>
<td>29</td>
</tr>
<tr>
<td>5732, stratified</td>
<td>CM</td>
<td>Laplacian</td>
<td>KRR</td>
<td>3.07</td>
<td>4.84</td>
<td>65</td>
</tr>
<tr>
<td>5732, stratified</td>
<td>BoB</td>
<td>Laplacian</td>
<td>KRR</td>
<td>1.50</td>
<td>...</td>
<td>64</td>
</tr>
</tbody>
</table>

## 4.3 Prediction of the standard enthalpies of formation.

**Table 3:** Variation of MAEs and RMSEs (in kcal/mol) with the training set size for enthalpies of formation of the BA10 dataset predicted using the SOAP and HMPP kernels (cf. Figure 6).

<table>
<thead>
<tr>
<th>
</th>
<th><strong>100 points</strong></th>
<th><strong>300 points</strong></th>
<th><strong>500 points</strong></th>
<th><strong>1000 points</strong></th>
</tr>
</thead>
<tbody>
<tr>
<th><strong>SOAP</strong>
</th>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<th>MAE</th>
<td>0.21</td>
<td>0.17</td>
<td>0.16</td>
<td>0.15</td>
</tr>
<tr>
<th>RMSE</th>
<td>0.28</td>
<td>0.22</td>
<td>0.21</td>
<td>0.20</td>
</tr>
<tr>
<th><strong>HMPP</strong>
</th>
<td>
</td>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<th>MAE</th>
<td>0.28</td>
<td>0.19</td>
<td>0.16</td>
<td>0.12</td>
</tr>
<tr>
<th>RMSE</th>
<td>0.39</td>
<td>0.26</td>
<td>0.21</td>
<td>0.17</td>
</tr>
</tbody>
</table>

To evaluate the accuracy of the HMPP kernel model in the prediction of properties of solid state systems, the entalpies of formation of the compounds in the BA10 dataset have been considered. Table 3 and Figure 6 show the values of MAE and RMSE averaged over all the structures of the 10 binary alloys. The training sets, which are always excluded in the

error evaluation, are obtained by randomly selecting 100, 300, 500, and 1000 configurations for each binary compound among the 1595 structures – *i.e.* without stratification of the data. As for the dataset QM7 discussed in the previous section (see Sec. 4), the present kernel was compared to the two other methods: SOAP and GRAPE. The SOAP descriptor has been used in the framework of the average kernel (AK), while the GRAPE has been employed in its original definition – *i.e.* in combination with a random walk graph kernel³⁸. For the sake of consistency, hyperparameters used in all the methods have been obtained via the procedure explained in Sec. 3 and the same training sets have been used in all calculations. The predictions of the localized graph kernel GRAPE were significantly worse than those obtained with SOAP and HMPP. For instance, with a training set of 100 points, the RMSE of the predicted enthalpies (averaged overall the alloys) is five times higher compared to the other two approaches. Therefore, we omit the detailed discussion of results obtained with the GRAPE approach for the BA10 dataset.

It can be observed that the SOAP kernel performs slightly better than the hybrid MPP for the training sets of 100 and 300 configurations. However, the learning capability of the SOAP kernel seems to saturate already at 300 configurations, as apparent from the fact that the MAE and RMSE values do not decrease significantly by increasing the number of training data points beyond this value. This could become a significant limitation if, for example, it would be of interest to extend the prediction of enthalpies on additional crystal structures. Our proposed model presents a better learning curve with errors that steadily decrease by increasing the training set size and become lower than SOAP for 1000 training structures.

In Figure 7 we show the RMSE obtained for each of the ten binary alloys separately using predictions made by ML trained on 1000 points. It can be noticed that in most cases the RMSE obtained with the HMPP kernel is smaller compared to the SOAP approach. The only exception is represented by the AlMg alloy, as the RMSE of the HMPP kernel method

![](./images/812406526508531713_8.jpg)

![](./images/812406526508531713_9.jpg)

**Figure 6:** Variation with the training set size of the MAEs and RMSEs for the formation enthalpy predictions (BA10 dataset) obtained from the SOAP and HMPP kernels. The values are given in kcal/mol (cf. Table 3).

is sizeably larger than that of SOAP (in this comparison it should also be kept into account that hyperparameters for the HMPP model are not reoptimized for each alloy). In Figure 7 we also report results from the previous work of Nyshadham *et al.*⁶⁰ based on MBTR. For four binary systems, CoNi, CuNi, AgCu, and AlMg, the MBTR yields a particularly small RMSE. With the exception of AlMg, the hybrid MPP approach provides a level of accuracy that is comparable to the previous MBTR calculations given in Ref. 60 and it even outperforms it in certain cases.

From Table 4, we can conclude that our method reaches a high level of accuracy. Indeed, the HMPP kernel presents small values of MAE and RMSE and performs similarly to the MBTR kernel. Moreover, the difference with previous results reported in the literature based on the SOAP descriptor and the Gaussian process regression (GPR) is quite small (0.02 kcal/mol). Hence, like in the case of the QM7 dataset, we can conclude that our model describes properly also the BA10 dataset.

![](./images/812406526508531713_10.jpg)

Figure 7: RMSE (in kcal/mol) of the SOAP, MBTR, and HMPP predictions of the standard enthalpies of formation for the ten alloys from the BA10 datased.

Table 4: MAE and RMSE for the HMPP, SOAP and MBTR predictions averaged over all ten binary alloys from the BA10 dataset. The values are given in kcal/mol.
List of abbreviations: Hybrid maximum probability path (HMPP), Smooth overlap of atomic positions (SOAP), Localized graph kernel (LGK), Average kernel (AK), Kernel ridge regres- sion (KRR), Gaussian process regression (GPR).

<table>
 <thead>
  <tr>
   <th>Training set</th>
   <th>Representation</th>
   <th>Kernel</th>
   <th>Regression</th>
   <th>MAE</th>
   <th>RMSE</th>
   <th>Source</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <th>1000</th>
   <th>HMPP</th>
   <th>LGK</th>
   <th>KRR</th>
   <td>0.12</td>
   <td>0.17</td>
   <td>This work</td>
  </tr>
  <tr>
   <td>1000</td>
   <td>SOAP</td>
   <td>AK</td>
   <td>KRR</td>
   <td>0.15</td>
   <td>0.20</td>
   <td>This work</td>
  </tr>
  <tr>
   <td>1000</td>
   <td>MBTR</td>
   <td>Laplacian</td>
   <td>KRR</td>
   <td>0.12</td>
   <td>$\cdots$</td>
   <td>60</td>
  </tr>
  <tr>
   <td>1000</td>
   <td>SOAP</td>
   <td>$\cdots$</td>
   <td>GPR</td>
   <td>0.10</td>
   <td>$\cdots$</td>
   <td>60</td>
  </tr>
 </tbody>
</table>

## 5 Conclusions

In conclusion, we introduced in the framework of a local decomposition kernel a new similarity measurement based on molecular graphs. This kernel is composed by two parts: one that describes the local molecular pattern through a labeled graph, and a second one, that keeps into account some finer geometric information using Coulomb labels. These two kernels are hybridized through a hyperparameter $\alpha$ which controls their relative contributions.

The accuracy of this new kernel was tested on two datasets: The molecular QM7 dataset and the BA10 dataset, containing ten binary alloys. The first of these applications involves the prediction of the atomization energies of molecules. In this case our method outperforms

previous descriptors proposed in the literature such as, for example, the smooth overlap of atomic positions and a previous approach based on unlabeled graph kernel introduced by Ferré et al.³⁸. In the case of enthalpies of formations of solids (BA10 dataset), for small training set size – up to 300 datapoints – the accuracy of our new HMPP kernel is lower with respect to the SOAP approach. However, when the number of training configurations increases the learning ability of the SOAP descriptor saturates. The HMPP kernel does not suffer of this limitation and outperforms SOAP for 1000 and more training configura- tions. From these case studies the labeled graph kernel seems a particularly promising tool to improve the accuracy in machine learning regression problems in chemistry and materials science.

## 6 Acknowledgement

B.C. and D.R. acknowledge G. Ferré for sharing his GRAPE code and for fruitful dis- cussions. This work was supported through the COMETE project (COnception in silico de Matériaux pour l'EnvironnemenT et l'Energie) co-funded by the European Union under the program "FEDER-FSE Lorraine et Massif des Vosges 2014-2020". T.B. acknowledges sup- port from Slovak Research and Development Agency under Contracts No. APVV-15-0105 and No. VEGA-1/0777/19.

## 7 Data availability

The data that support the findings of this study are available from the corresponding authors upon reasonable request.

### References

(1) Haykin, S. *Neural Networks and Learning Machines, Third Edition*; Pearson Education Inc, 2009.

(2) Behler, J. Perspective: Machine Learning Potentials for Atomistic Simulations. *J. Chem. Phys.* **2016**, *145*, 170901.

(3) Noé, F.; Tkatchenko, A.; Müller, K.-R.; Clementi, C. Machine Learning for Molecular Simulation. *Annu. Rev. Phys. Chem.* **2020**, *71*, 361.

(4) Dral, P. O. Quantum Chemistry in the Age of Machine Learning. *J. Phys. Chem. Lett.* **2020**, *11*, 2336.

(5) McArdle, S.; Endo, S.; Aspuru-Guzik, A.; Benjamin, S. C.; Yuan, X. Quantum Computational Chemistry. *Rev. Mod. Phys.* **2020**, *92*, 015003.

(6) Handley, C. M.; Popelier, P. L. A. Potential Energy Surfaces Fitted by Artificial Neural Networks. *J. Phys. Chem. A* **2010**, *114*, 3371.

(7) Behler, J. Neural Network Potential Energy Surfaces in Chemistry: a Tool for Large-scale Simulations. *Phys. Chem. Chem. Phys.* **2011**, *13*, 17930.

(8) Bučko, T.; Gešvandtnerová, M.; Rocca, D. *Ab initio* Calculations of Free Energy of Activation at Multiple Electronic Structure Levels Made Affordable: An Effective Combination of Perturbation Theory and Machine Learning. *J. Chem. Theory Comput.* **2020**, *16*, 6049.

(9) Casier, B.; Carniato, S.; Miteva, T.; Capron, N.; Sisourat, N. Using Principal Component Analysis for Neural Network High-dimensional Potential Energy Surface. *J. Chem. Phys.* **2020**, *152*, 234103.

(10) Behler, J.; Parrinello, M. Generalized Neural Network Representation of High-dimensional Potential Energy Surfaces. *Phys. Rev. Lett.* **2007**, *98*, 146401.

(11) Häse, F.; Galván, I.; Aspuru-Guzik, A.; Lindh, R.; Vacher, M. How Machine Learn- ing Can Assist the Interpretation of *Ab Initio* Molecular Dynamics Simulations and Conceptual Understanding of Chemistry. *Chem. Sci.* **2019**, *10*, 2298.

(12) Gkeka, P.; Stoltz, G.; Barati Farimani, A.; Belkacemi, Z.; Ceriotti, M.; Chodera, J. D.; Dinner, A. R.; Ferguson, A. L.; Maillet, J.-B.; Minoux, H.; Peter, C.; Pietrucci, F.; Silveira, A.; Tkatchenko, A.; Trstanova, Z.; Wiewiora, R.; Lelièvre, T. Machine Learn- ing Force Fields and Coarse-Grained Variables in Molecular Dynamics: Application to Materials and Biological Systems. *J. Chem. Theory Comput.* **2020**, *16*, 4757.

(13) Montavon, G.; Rupp, M.; Gobre, V.; Vazquez-Mayagoitia, A.; Hansen, K.; Tkatchenko, A.; Müller, K.-R.; von Lilienfeld, O. A. Machine Learning of Molecular Electronic Properties in Chemical Compound Space. *New J. Phys.* **2013**, *15*, 095003.

(14) Welborn, M.; Cheng, L.; Miller, T. F. Transferability in Machine Learning for Electronic Structure via the Molecular Orbital Basis. *J. Chem. Theory Comput.* **2018**, *14*, 4772.

(15) Pronobis, W.; Tkatchenko, A.; Müller, K.-R. Many-Body Descriptors for Predicting Molecular Properties with Machine Learning: Analysis of Pairwise and Three-body Interactions in Molecules. *J. Chem. Theory Comput.* **2018**, *14*, 2991.

(16) Grisafi, A.; Wilkins, D. M.; Csányi, G.; Ceriotti, M. Symmetry-adapted Machine Learn- ing for Tensorial Properties of Atomistic Systems. *Phys. Rev. Lett.* **2018**, *120*, 036002.

(17) Unke, O. T.; Meuwly, M. PhysNet: A Neural Network for Predicting Energies, Forces, Dipole Moments, and Partial Charges. *J. Chem. Theory Comput.* **2019**, *15*, 3678.

(18) Ruddigkeit, L.; van Deursen, R.; Blum, L. C.; Reymond, J.-L. Enumeration of 166 Billion Organic Small Molecules in the Chemical Universe Database GDB-17. *J. Chem. Inf. Model.* **2012**, *52*, 2864.

(19) Faber, F. A.; Lindmaa, A.; von Lilienfeld, O. A.; Armiento, R. Machine Learning Energies of 2 Million Elpasolite $(ABC_{2}D_{6})$ Crystals. *Phys. Rev. Lett.* **2016**, *117*, 135502.

(20) von Lilienfeld, O. A. Quantum Machine Learning in Chemical Compound Space. *Angew. Chem. Int. Ed.* **2018**, *57*, 4164.

(21) Tkatchenko, A. Machine Learning for Chemical Discovery. *Nat. Commun.* **2020**, *11*.

(22) Ramakrishnan, R.; Dral, P. O.; Rupp, M.; von Lilienfeld, O. A. Big Data Meets Quan- tum Chemistry Approximations: The $\Delta$-Machine Learning Approach. *J. Chem. Theory Comput.* **2015**, *11*, 2087.

(23) Chehaibou, B.; Badawi, M.; Bučko, T.; Bazhirov, T.; Rocca, D. Computing RPA Adsorption Enthalpies by Machine Learning Thermodynamic Perturbation Theory. *J. Chem. Theory Comput.* **2019**, *15*, 6333.

(24) Behler, J. Atom-centered Symmetry Functions for Constructing High-dimensional Neu- ral Network Potentials. *J. Chem. Phys.* **2011**, *134*, 074106.

(25) Rupp, M.; Tkatchenko, A.; Müller, K.-R.; von Lilienfeld, O. A. Fast and Accurate Modeling of Molecular Atomization Energies with Machine Learning. *Phys. Rev. Lett.* **2012**, *108*, 058301.

(26) Montavon, G.; Hansen, K.; Fazli, S.; Rupp, M.; Biegler, F.; Ziehe, A.; Tkatchenko, A.; von Lilienfeld, O.; Müller, K. In *Advances in Neural Information Processing Systems*; Pereira, F., Burges, C., Bottou, L., Weinberger, K., Eds.; Curran Associates, Inc., 2012; p 440.

(27) Faber, F.; Lindmaa, A.; von Lilienfeld, O. A.; Armiento, R. Crystal Structure Repre- sentations for Machine Learning Models of Formation Energies. *Int. J. Quantum Chem.* **2015**, *115*, 1094.

(28) Bartók, A. P.; Kondor, R.; Csányi, G. On Representing Chemical Environments. *Phys. Rev. B* **2013**, *87*, 184115.

(29) De, S.; Bartók, A. P.; Csányi, G.; Ceriotti, M. Comparing Molecules and Solids Across Structural and Alchemical Space. *Phys. Chem. Chem. Phys.* **2016**, *18*, 13754.

(30) Huo, H.; Rupp, M. Unified Representation of Molecules and Crystals for Machine Learning. 2017.

(31) Mahé, P.; Ueda, N.; Akutsu, T.; Perret, J.-L.; Vert, J.-P. Extensions of Marginalized Graph Kernels. Proceedings of the Twenty-First International Conference on Machine Learning. New York, NY, USA, 2004; p 70.

(32) Mahé, P.; Ueda, N.; Akutsu, T.; Perret, J.-L.; Vert, J.-P. Graph Kernels for Molecular Structure Activity Relationship Analysis with Support Vector Machines. *J. Chem. Inf. Model.* **2005**, *45*, 939.

(33) Gaüzère, B.; Brun, L.; Villemin, D. Two New Graphs Kernels in Chemoinformatics. *Pattern Recognit. Lett.* **2012**, *33*, 2038.

(34) Lavecchia, A. Machine Learning Approaches in Drug Discovery: Methods and Applications. *Drug Discov. Today* **2015**, *20*, 318.

(35) Sharan, R.; Ideker, T. Modeling Cellular Machinery Through Biological Network Comparison. *Nat. Biotechnol.* **2006**, *24*.

(36) Smalter, A.; Huan, J.; Lushington, G. Graph Wavelet Alignment Kernels for Drug Virtual Screening. *J. Bioinform. Comput. Biol.* **2009**, *07*, 473.

(37) Muratov, E. N.; Bajorath, J.; Sheridan, R. P.; Tetko, I. V.; Filimonov, D.; Poroikov, V.; Oprea, T. I.; Baskin, I. I.; Varnek, A.; Roitberg, A.; Isayev, O.; Curtalolo, S.; Fourches, D.; Cohen, Y.; Aspuru-Guzik, A.; Winkler, D. A.; Agrafiotis, D.; Cherkasov, A.; Tropsha, A. QSAR Without Borders. *Chem. Soc. Rev.* **2020**, *49*, 3525.

(38) Ferré, G.; Haut, T.; Barros, K. Learning Molecular Energies Using Localized Graph Kernels. *J. Chem. Phys.* **2017**, *146*, 114107.

(39) Wu, Z.; Ramsundar, B.; Feinberg, E. N.; Gomes, J.; Geniesse, C.; Pappu, A. S.; Leswing, K.; Pande, V. MoleculeNet: a Benchmark for Molecular Machine Learning. *Chem. Sci.* **2018**, *9*, 513.

(40) Xie, T.; Grossman, J. C. Crystal Graph Convolutional Neural Networks for an Accurate and Interpretable Prediction of Material Properties. *Phys. Rev. Lett.* **2018**, *120*, 145301.

(41) Tang, Y.-H.; de Jong, W. A. Prediction of Atomization Energy Using Graph Kernel and Active Learning. *J. Chem. Phys.* **2019**, *150*, 044107.

(42) Na, G. S.; Chang, H.; Kim, H. W. Machine-guided Representation for Accurate Graph-based Molecular Machine Learning. *Phys. Chem. Chem. Phys.* **2020**, *22*, 18526.

(43) Hoerl, A. E.; Kennard, R. W. Ridge Regression: Biased Estimation for Nonorthogonal Problems. *Technometrics* **1970**, *12*, 55.

(44) Wu, X.; Tang, W.; Wu, X. Support Vector Machine Based on Hybrid Kernel Function. Information Engineering and Applications. London, 2012; p 127.

(45) Ralaivola, L.; Swamidass, S. J.; Saigo, H.; Baldi, P. Graph Kernels for Chemical Informatics. *Neural Netw.* **2005**, *18*, 1093.

(46) Kriege, N. M.; Johansson, F. D.; Morris, C. A Survey on Graph Kernels. *Appl. Netw. Sci.* **2020**, *5*, 6.

(47) Nikolentzos, G.; Siglidis, G.; Vazirgiannis, M. Graph Kernels: A Survey. 2019.

(48) Cordero, B.; Gómez, V.; Platero-Prats, A. E.; Revés, M.; Echeverría, J.; Cremades, E.; Barragán, F.; Alvarez, S. Covalent Radii Revisited. *Dalton Trans.* **2008**, 2832.

(49) Borgwardt, K. M.; Kriegel, H. P. Shortest-path Kernels on Graphs. Fifth IEEE Inter- national Conference on Data Mining (ICDM'05). 2005; p 8.

(50) Floyd, R. W. Algorithm 97: Shortest Path. *Commun. ACM* **1962**, *5*, 345.

(51) Rupp, M.; Proschak, E.; Schneider, G. Kernel Approach to Molecular Similarity Based on Iterative Graph Similarity. *J. Chem. Inf. Model.* **2007**, *47*, 2280.

(52) Nikolentzos, G.; Meladianos, P.; Rousseau, F.; Stavrakas, Y.; Vazirgiannis, M. Shortest- path Graph Kernels for Document Similarity. Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing. 2017; p 1890.

(53) Rupp, M. Machine Learning for Quantum Mechanics in a Nutshell. *Int. J. Quantum Chem.* **2015**, *115*, 1058.

(54) Himanen, L.; Jäger, M. O. J.; Morooka, E. V.; Federici Canova, F.; Ranawat, Y. S.; Gao, D. Z.; Rinke, P.; Foster, A. S. DScribe: Library of Descriptors for Machine Learn- ing in Materials Science. *Comput. Phys. Commun.* **2020**, *247*, 106949.

(55) Pedregosa, F.; Varoquaux, G.; Gramfort, A.; Michel, V.; Thirion, B.; Grisel, O.; Blon- del, M.; Prettenhofer, P.; Weiss, R.; Dubourg, V.; Vanderplas, J.; Passos, A.; Courna- peau, D.; Brucher, M.; Perrot, M.; Duchesnay, E. Scikit-learn: Machine Learning in Python. *J. Mach. Learn. Res.* **2011**, *12*, 2825.

(56) Rappe, A. K.; Casewit, C. J.; Colwell, K. S.; Goddard, W. A.; Skiff, W. M. UFF, a Full Periodic Table Force Field for Molecular Mechanics and Molecular Dynamics Simulations. *J. Am. Chem. Soc.* **1992**, *114*, 10024.

(57) Blum, L. C.; Reymond, J.-L. 970 Million Druglike Small Molecules for Virtual Screening in the Chemical Universe Database GDB-13. *J. Am. Chem. Soc.* **2009**, *131*, 8732.

(58) Hohenberg, P.; Kohn, W. Inhomogeneous Electron Gas. *Phys. Rev.* **1964**, *136*, B864.

(59) Perdew, J. P.; Burke, K.; Ernzerhof, M. Generalized Gradient Approximation Made Simple. *Phys. Rev. Lett.* **1996**, *77*, 3865.

(60) Nyshadham, C.; Rupp, M.; Bekker, B.; Shapeev, A. V.; Mueller, T.; Rosenbrock, C. W.; Csányi, G.; Wingate, D. W.; Hart, G. L. W. Machine-learned Multi-system Surrogate Models for Materials Prediction. *Npj Comput. Mater* **2019**, *5*.

(61) Hart, G. L.; Nelson, L. J.; Forcade, R. W. Generating Derivative Structures at a Fixed Concentration. *Comput. Mater. Sci.* **2012**, *59*, 101.

(62) Kresse, G.; Hafner, J. *Ab Initio* Molecular Dynamics for Liquid Metals. *Phys. Rev. B: Condens. Matter Mater. Phys.* **1993**, *47*, 558.

(63) Kresse, G.; Furthmüller, J. Efficient Iterative Schemes for *Ab Initio* Total-energy Calculations Using a Plane Wave Basis Set. *Phys. Rev. B: Condens. Matter Mater. Phys.* **1996**, *54*, 11169.

(64) Hansen, K.; Biegler, F.; Ramakrishnan, R.; Pronobis, W.; von Lilienfeld, O. A.; Müller, K.-R.; Tkatchenko, A. Machine Learning Predictions of Molecular Properties: Accurate Many-body Potentials and Nonlocality in Chemical Space. *J. Phys. Chem. Lett.* **2015**, *6*, 2326.

(65) Hansen, K.; Montavon, G.; Biegler, F.; Fazli, S.; Rupp, M.; Scheffler, M.; von Lilienfeld, O. A.; Tkatchenko, A.; Müller, K.-R. Assessment and Validation of Machine Learning Methods for Predicting Molecular Atomization Energies. *J. Chem. Theory Comput.* **2013**, *9*, 3404.