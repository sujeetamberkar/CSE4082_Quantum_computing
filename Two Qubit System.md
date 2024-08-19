$|00\rangle=|0\rangle\otimes|0\rangle=\begin{bmatrix}1\\0\end{bmatrix}\otimes\begin{bmatrix}1\\0\end{bmatrix}=\begin{bmatrix}1\\0\\0\\0\end{bmatrix}$

$|01\rangle=|0\rangle\otimes|1\rangle=\begin{bmatrix}1\\0\end{bmatrix}\otimes\begin{bmatrix}0\\1\end{bmatrix}=\begin{bmatrix}0\\1\\0\\0\end{bmatrix}$

$|10\rangle=|1\rangle\otimes|0\rangle=\begin{bmatrix}0\\1\end{bmatrix}\otimes\begin{bmatrix}1\\0\end{bmatrix}=\begin{bmatrix}0\\0\\1\\0\end{bmatrix}$

$|11\rangle=|1\rangle\otimes|1\rangle=\begin{bmatrix}0\\1\end{bmatrix}\otimes\begin{bmatrix}0\\1\end{bmatrix}=\begin{bmatrix}0\\0\\0\\1\end{bmatrix}$
$\langle00|=\begin{bmatrix}1&0&0&0\end{bmatrix}$
$\langle01|=\begin{bmatrix}0&1&0&0\end{bmatrix}$
$\langle10|=\begin{bmatrix}0&0&1&0\end{bmatrix}$
$\langle11|=\begin{bmatrix}0&0&0&1\end{bmatrix}$

# General Two Qubit State
Consider a generic Single Qubit State
$\psi_1=\alpha_1|0\rangle+\beta_1|1\rangle$ and $\psi_2=\alpha_2|0\rangle+\beta_2|1\rangle$
Generic Two Qubit system = $|\psi_1\rangle\otimes|\psi_2\rangle$
$|\psi_1\rangle\otimes|\psi_2\rangle$ = $(\alpha_1|0\rangle+\beta_1|1\rangle)\otimes(\psi_2=\alpha_2|0\rangle+\beta_2|1\rangle)$
         =  $\alpha_1\alpha_2|00\rangle+\alpha_1\beta_2|01\rangle+\beta_1\alpha_2|10\rangle+\beta_1\beta_2|11\rangle$
         =  $\alpha_1\alpha_2\begin{bmatrix}1\\0\\0\\0\end{bmatrix}+\alpha_1\beta_2\begin{bmatrix}0\\1\\0\\0\end{bmatrix}+\beta_1\alpha_2\begin{bmatrix}0\\0\\1\\0\end{bmatrix}+\beta_1\beta_2\begin{bmatrix}0\\0\\0\\1\end{bmatrix}$ =  $\begin{bmatrix}\alpha_1\alpha_2\\\alpha_1\beta_2\\\beta_1\alpha_2\\\beta\beta_2\end{bmatrix}$ 

Here 
 $\alpha_1\alpha_2 ,\alpha_1\beta_2,\beta_1\alpha_2,\beta\beta_2$ are complex Number 
 and $|\alpha_1\alpha_2|^2 +|\alpha_1\beta_2|^2+|\beta_1\alpha_2|^2|\beta\beta_2|^2$ = 1
 
 $|\psi\rangle=$$\alpha_1\alpha_2|00\rangle+\alpha_1\beta_2|01\rangle+\beta_1\alpha_2|10\rangle+\beta_1\beta_2|11\rangle$
	 P(00) = $|\alpha_1\alpha_2|^2$
	 P(01) = $|\alpha_1\beta_2|^2$
	 P(10) = $|\beta_1\alpha_2|^2$
	 P(11) = $|\beta_1\beta_2|^2$
## Check if Valid Two Qubit State or not
# Example 1
$|\psi\rangle=\frac{1}{2}|00\rangle+\frac{1}{2}|01\rangle+\frac{1}{2}|10\rangle+\frac{1}{2}|11\rangle$
 
|$\psi$| = $\sum \text{Probabilities}$ = $\frac{1}{4}+\frac{1}{4}+\frac{1}{4}+\frac{1}{4}=1$
	P(00) = $\frac{1}{4}$
	P(01) = $\frac{1}{4}$
	P(10) = $\frac{1}{4}$
	P(11) = $\frac{1}{4}$
# Example 2
$|\psi\rangle=\frac{1}{3}|00\rangle+\frac{2}{3}|10\rangle+\frac{2}{3}|11\rangle$
 
|$\psi$| = $\sum \text{Probabilities}$ = $\frac{1}{9}+\frac{4}{9}+\frac{4}{9}=1$
	P(00) = $\frac{1}{9}$
	P(01) =  0 
	P(10) =  $\frac{4}{9}$
	P(11) =  $\frac{4}{9}$
	
# Example 3
$|\psi\rangle=\frac{1}{\sqrt{2}}|00\rangle++\frac{1}{\sqrt{2}}|11\rangle$
P(00) = $\frac{1}{2}$
P(11) = $\frac{1}{2}$
 |$\psi$| = $\sum \text{Probabilities}$ = $\frac{1}{2}+\frac{1}{2}=1$

# Example 4
$|\psi\rangle=\frac{1}{3}|00\rangle+\frac{2}{3}|10\rangle-\frac{2}{3}|11\rangle$
P(00) = $\frac{1}{9}$
P(01) =  0 
P(10) =  $\frac{4}{9}$
P(11) =  $\frac{4}{9}$
|$\psi$| = $\sum \text{Probabilities}$ = $\frac{1}{9}+\frac{4}{9}+\frac{4}{9}=1$
