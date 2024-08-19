## Vectors:
- Column of Number

$$
\bar{V} = 
\begin{bmatrix} 
V1 \\
V2 \\
\end{bmatrix}
$$
More Generally N dimensions take the form 

$$
\bar{V} = 
\begin{bmatrix} 
V1 \\
V2 \\
. \\
. \\
V_n
\end{bmatrix}
$$

## Vector Addition

Let $\vec{V}$ and $\vec{W}$ be two vectors 
$$ \vec{V} = 
\begin{bmatrix}
	V_1\\
	V_2 \\
\end{bmatrix}
\quad
\vec{W} = 
\begin{bmatrix}
	W_1\\
	W_2 \\
\end{bmatrix}
$$

$$ \vec{V} + \vec{W} = 
\begin{bmatrix}
V_1 + W_1 \\
V_2 + W_2 \\
\end{bmatrix}
$$

## Vector Scalar Multiplication

$$
	c\vec{V} = 
	
	\begin{bmatrix}
		c V_1\\
		c V_2\\		
	\end{bmatrix}
$$

## Complex Conjugate

$$
	M = 
		\begin{bmatrix}
		1 & 6i \\
		3i & 2+4i \\		
		\end{bmatrix}
	\quad Then\;\bar{M} = 
	\begin{bmatrix}
		1 & -6i \\
		-3i & 2-4i \\		
		\end{bmatrix}
$$
## Matrix Transpose

$$
	M = 
		\begin{bmatrix}
		1 & 6i \\
		3i & 2+4i \\		
		\end{bmatrix}
	\quad Then\; M^T = 
	\begin{bmatrix}
	1 & 3i \\
	6i & 2+4i
	\end{bmatrix}
$$

## Conjugate Transpose

$$
	M = 
		\begin{bmatrix}
		1 & 6i \\
		3i & 2+4i \\		
		\end{bmatrix}
	\quad Then\; {M}^\dagger = 
	\begin{bmatrix}
	1 & -3i \\
	-6i & 2-4i
	\end{bmatrix}
$$

## Inner Product

1) Take Complex Conjugate of the $1_{st}$ Vector
2) Multiply each of the corresponding Numbers


$$
\vec{V}. \vec{W} = \sum_{j=1}^n \bar{V_j}. W_j
$$
### Example 1
$$
\vec{V} = 
\begin{bmatrix}
i\\
2+i
\end{bmatrix}

\quad ;
\vec{W} = 
\begin{bmatrix}
2\\
-1
\end{bmatrix}
$$
$$
Step 1: 
\bar{V} = 
\begin{bmatrix}
-i && 2-i
\end{bmatrix}

\quad ;
\vec{W} = 
\begin{bmatrix}
2\\
-1
\end{bmatrix}
$$


$$
Step 2: 
	\bar{V}. \vec{W} = -2i + (2 - i) (-1) 
$$
$$
	\bar{V}. \vec{W} = -2i + -2  + i 
$$
$$
	\bar{V}. \vec{W} = -2 -i  
$$


### Example 2
$$ \vec{V} = 
\begin{bmatrix}
	i\\
	i \\
\end{bmatrix}
\quad
\vec{W} = 
\begin{bmatrix}
	1\\
	-1 \\
\end{bmatrix}
$$


$$
Step 1: 
\bar{V} = 
\begin{bmatrix}
-i & -i
\end{bmatrix}

\quad ;
\vec{W} = 
\begin{bmatrix}
1\\
-1
\end{bmatrix}
$$
$$ 
	\bar{V}. \vec{W} = -i + i = 0
$$


### Length of Vector

$$ 
||\vec{V}|| = \sqrt{|V_1|^2 + |V_2|^2 + ... + |V_n|^2} 
$$
$\vec{V}=\begin{bmatrix}1\\-2\\i\end{bmatrix}$

$||\vec{V}|| =\sqrt{|1|^2+|-2|^2+|i|^2}=\sqrt{1^2+2^2+1^2}=\sqrt{6}$




## Unit Vector and Normalisation
- Unit Vector has Length = 1
- Normalising a non-Unit Vector means scaling by $\frac{1}{||V||}$ 

$\vec{V}=\begin{bmatrix}1\\-2\\i\end{bmatrix}\quad ||V||=\sqrt{|1|^2+|-2|^2+|i|^2}=\sqrt{1+4+1}=\sqrt{6}$

$$
\left\|\frac{\vec{V}}{||\vec{V}||}\right\| = \frac{1}{\sqrt{6}} \cdot \begin{bmatrix} 1 \\ -2 \\ i \end{bmatrix}
$$


## Tensor Product
- Join Two Vector to make a bigger Vector

Let $\vec{V}$ and $\vec{W}$ be two vectors 

$$ \vec{V} = 
\begin{bmatrix}
	V_1\\
	V_2 \\
\end{bmatrix}
\quad and \quad
\vec{W} = 
\begin{bmatrix}
	W_1\\
	W_2 \\
\end{bmatrix}
$$

The Tensor Product is defined by

$$
\vec{V} = 
\begin{bmatrix}
    V_1\\
    V_2 \\

\end{bmatrix}
\quad \text{and} \quad
\vec{W} = 
\begin{bmatrix}
    W_1\\
    W_2 \\

\end{bmatrix}
$$


The tensor product $\vec{V}\otimes\vec{W}=$

$\vec{V} \otimes \vec{W} = \begin{bmatrix}V_1 \begin{bmatrix}W1\\W2\\\end{bmatrix}\\V2\begin{bmatrix}W1\\W2\\\end{bmatrix}\\\end{bmatrix}\quad=\begin{bmatrix}V_1W_1\\V_1W_2\\V_2W_1\\V_2W_2\\\end{bmatrix}$

### Another Example

$$ \mathbf{V} =  \begin{bmatrix}     V_{1} & V_{3} \\     V_{2} & V_{4} \\ \end{bmatrix} \quad \text{and} \quad \mathbf{W} =  \begin{bmatrix}     W_{1} & W_{3} \\     W_{2} & W_{4} \\ \end{bmatrix} $$ The tensor product $vec{V}\otimes\vec{W}=$  $$ \mathbf{V} \otimes \mathbf{W} =  \begin{bmatrix} 
	V_{1} 
		\mathbf{\begin{bmatrix}
			W_{1} & W_{3} \\     
			W_{2} & W_{4} \\ 
		\end{bmatrix} } 
	& V_{3} 
		\mathbf{\begin{bmatrix}
			W_{1} & W_{3} \\     
			W_{2} & W_{4} \\ 
		\end{bmatrix} } 
	\\ 
	
	V_{2} 
		\mathbf{\begin{bmatrix}
			W_{1} & W_{3} \\     
			W_{2} & W_{4} \\ 
		\end{bmatrix} } 
	
	& V_{4} 
		\mathbf{\begin{bmatrix}
			W_{1} & W_{3} \\     
			W_{2} & W_{4} \\ 
		\end{bmatrix} } 
	\\ 
	\end{bmatrix} 
	
	= 
	
	\begin{bmatrix} 
		V_{1}W_{1} & V_{1}W_{3} & V_{3}W_{1} & V_{3}W_{3} \\ 
		V_{1}W_{2} & V_{1}W_{4} & V_{3}W_{2} & V_{3}W_{4} \\ 
		V_{2}W_{1} & V_{2}W_{3} & V_{4}W_{1} & V_{4}W_{2} \\ 
		V_{2}W_{2} & V_{2}W_{4} & V_{2}W_{2} & V_{4}W_{4} \\ 
	\end{bmatrix} $$
### Example 1
$\vec{V}=\begin{bmatrix} 2 \\ 6i \end{bmatrix}\quad\vec{W}=\begin{bmatrix} 3 \\ 4 \end{bmatrix}$


The tensor product $vec{V}\otimes\vec{W}=$  
$$ \vec{V} \otimes \vec{W} = 
\begin{bmatrix} 
	2 \mathbf{
	\begin{bmatrix} 
		3 \\ 
		4 \\ 
	\end{bmatrix}} 
	\\ 6i 
	\mathbf{
	\begin
	{bmatrix} 
	3 \\ 
	4 \\ 
	\end{bmatrix}} 
	\end{bmatrix} = 
	
	\begin{bmatrix} 2 \times 3 \\ 2 \times 4 \\ 6i \times 3 \\ 6i \times 4 \\ \end{bmatrix} = 
	\begin{bmatrix} 6 \\ 8 \\ 18i \\ 24i \\ \end{bmatrix} $$


### Example 2
$\vec{V}=\begin{bmatrix} 1 & i \\ -i & 1 \end{bmatrix}\quad\vec{W}=\begin{bmatrix} i & 1 \\ 1 &i \end{bmatrix}$
The tensor product $vec{V}\otimes\vec{W}=$  
$$ \vec{V} \otimes \vec{W} = \begin{bmatrix} 1 \mathbf{\begin{bmatrix} i & 1 \\ 1 & i \\ \end{bmatrix}} & i \mathbf{\begin{bmatrix} i & 1 \\ 1 & i \\ \end{bmatrix}} \\ -i \mathbf{\begin{bmatrix} i & 1 \\ 1 & i \\ \end{bmatrix}} & 1 \mathbf{\begin{bmatrix} i & 1 \\ 1 & i \\ \end{bmatrix}} \end{bmatrix} $$ Now, let's expand the product inside the matrix: $$ = \begin{bmatrix} 1 \times i & 1 \times 1 & i \times i & i \times 1 \\ 1 \times 1 & 1 \times i & i \times 1 & i \times i \\ -i \times i & -i \times 1 & 1 \times i & 1 \times 1 \\ -i \times 1 & -i \times i & 1 \times 1 & 1 \times i \\ \end{bmatrix} = \begin{bmatrix} i & 1 & -1 & i \\ 1 & i & i & -1 \\ -1 & -i & i & 1 \\ -i & -1 & 1 & i \\ \end{bmatrix} $$
### Example 3
$\vec{V}=\begin{bmatrix} 1 \\ i \end{bmatrix}\quad\vec{W}=\begin{bmatrix} 1 \\ -2 \\ i \end{bmatrix}$

The tensor product $vec{V}\otimes\vec{W}=$  


