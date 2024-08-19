## Direct Notation
- In Physics  we  represent the vector as $\vec{a}$ , $\vec{b}$, $\vec{1}$ ... etc
- But in Quantum Computing we represent the vector as | a> , |b> ... etc

$$ |V\rangle  = 
				\begin{bmatrix}V1 \\ V2\end {bmatrix} 
				\Leftrightarrow\;
				\vec{V}=\begin{bmatrix}V1 \\ V2\end{bmatrix}$$ 


# Bra
The conjugate Transpose of "Ket" is called Bra and denoted by <V|
$$\langle V| = |V\rangle^\dagger$$
## Example 1
if $|V\rangle=\begin{bmatrix}1 \\i \end{bmatrix}$
	then $\langle V| =\begin{bmatrix}1 & -i\end{bmatrix}$
## Example 2 
If $|V\rangle = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$
	then $\langle V|=\begin{bmatrix}1 & 2\end{bmatrix}$

# Inner Product
Bracket notation.
Given two vectors $|V\rangle$ and $|W\rangle$, then bracket of  $|V\rangle$ and $|W\rangle$ is defined by
$$
\langle V|W\rangle = \langle V| \;. |W\rangle
$$
## Example 1

$|V\rangle = \frac{1}{\sqrt{2}} \; \begin{bmatrix}1\\ i \end{bmatrix} \quad |W\rangle = \frac{i}{\sqrt{2}} \begin{bmatrix} 1 \\ 1 \end{bmatrix}$
$\quad |V\rangle = \frac{1}{\sqrt{2}} \; \begin{bmatrix}1\\ i \end{bmatrix}$
$\quad \langle V| = \frac{1}{\sqrt{2}} \; \begin{bmatrix}1 & -i \end{bmatrix}$
$$\langle V|W\rangle = \frac{1}{\sqrt{2}} \begin{bmatrix}1 & -i \end{bmatrix}
						\quad
						\frac{i}{\sqrt{2}} \begin{bmatrix} 1 \\ 1 \end{bmatrix} $$
$$
\langle V|W\rangle = \frac{i}{2}  \begin{bmatrix}1 & -i \end{bmatrix} 
= \frac{i-i^2}{2}
= \frac{i + 1}{2}
$$
## Example 2

$|\psi\rangle=\frac{1}{\sqrt{2}}|0\rangle + \frac{1}{\sqrt{2}}|1\rangle$ and  $|\phi\rangle=\frac{1}{\sqrt{2}}|0\rangle - \frac{1}{\sqrt{2}}|1\rangle$ 
then calculate $\langle\psi|\phi\rangle$

$\langle\psi| = \frac{1}{\sqrt{2}}\langle0| + \frac{1}{\sqrt{2}}\langle1|$ and $|\phi\rangle=\frac{1}{\sqrt{2}}|0\rangle - \frac{1}{\sqrt{2}}|1\rangle$ 
$\langle\psi|\phi\rangle$ = $\frac{1}{2}\langle0|0\rangle$ - $\frac{1}{2}\langle0|1\rangle$ +  $\frac{1}{2}\langle1|0\rangle$ + $\frac{1}{2}\langle1|1\rangle$ = $\frac{1}{2} -\frac{1}{2}$ = 0

Since the Inner product is 0
We can say $|\psi\rangle$ and $|\phi\rangle$ are orthogonal



# Symmetric 
$\langle W | V \rangle = \langle V | W \rangle$
# Conjugate symmetry (Hermitian inner products)
$\langle W | V \rangle = \langle \overline {V | W} \rangle$


# Qubit
A qubit is a unit vector in a two-dimensional complex complex vector space. The Two Possible state of the qubit are 
$$
|0\rangle = \begin{bmatrix}1 \\ 0 \end{bmatrix} 
\quad 
|1\rangle = \begin{bmatrix}0 \\ 1\end{bmatrix}
$$
Note that 
$\langle0| = \begin{bmatrix}1 & 0 \end{bmatrix} \quad \quad \langle1| = \begin{bmatrix}0 & 1\end{bmatrix}$

# Physical Meaning 

1) Energy of Electron 

| Ket | Energy of $e^-$ | Spin of $e^-$ | Photon Polarisation |
| --- | --------------- | ------------- | ------------------- |
| 0⟩  | Ground State    | Spin-Up       | Vertical            |
| 1⟩  | Excited State   | Spin Down     | Horizontal          |

# Ket to Bra
## Example 1
$|\psi\rangle =\frac{2}{\sqrt{7}} |0\rangle +i \sqrt{\frac{3}{7}}\;|1\rangle$

It is a valid Quantum State
$|\psi\rangle=\frac{2}{\sqrt{7}}\begin{bmatrix}1 \\ 0 \end{bmatrix}$ + $i \sqrt{\frac{3}{7}}\ \begin{bmatrix}0 \\ 1 \end{bmatrix}$ = $\begin{bmatrix} \frac{2}{\sqrt{7}} \\ i \sqrt{\frac{3}{7}} \end{bmatrix}$
P(0) = $\frac{4}{7}$
P(1) = $\frac{3}{7}$
$\langle \psi| =\begin{bmatrix} \frac{2}{\sqrt{7}} && -i \sqrt{\frac{3}{7}} \end{bmatrix}$ = $\frac{2}{\sqrt{7}}\langle0| - i\sqrt{\frac{3}{7}}\;\langle 1|$

