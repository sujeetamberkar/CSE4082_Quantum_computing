# Generic Two Cubic State
$|\psi>=\alpha_1\alpha_2|00>+\alpha_1\beta_2|01>+\beta_1\alpha_2|10>+\beta_1\beta_2|11>$

## Case 1 (1st Qubit =0)

We measure only the first qubit and get the result "0"

$|\psi>=\alpha_1\alpha_2|00>+\alpha_1\beta_2|01>+\beta_1\alpha_2|10>+\beta_1\beta_2|11>$


Lets focus on $\alpha_1\beta_2$ and $\alpha_1\beta_2$

Probability (0) = $|\alpha_1\alpha_2|^2+|\alpha_1\beta_2|^2$
After measuring the state the quantum qubit will collapse to 

$|\psi'>=\alpha_1\alpha_2|00>+\alpha_1\beta_2|01>$
We need to normalised the qubit after measurement 

Length = Norm = $\sqrt{(\alpha_1\alpha_2)^2 +(\alpha_1\beta_2)^2 }$

$$
|\psi'> = \frac{\alpha_1\alpha_2}{\sqrt{(\alpha_1\alpha_2)^2 +(\alpha_1\beta_2)^2 }} |00>+ \frac{ \alpha_1\beta_2}{\sqrt{(\alpha_1\alpha_2)^2 +(\alpha_1\beta_2)^2 }}|01>
$$
Now let us measure the 2nd Qubit 

P($2^{nd}$ Qubit =0 ) =  $\frac{|\alpha_1\alpha_2|^2}{(\alpha_1\alpha_2)^2 +(\alpha_1\beta_2)^2 }$



P($2^{nd}$ Qubit =1 ) =  $\frac{|\alpha_1\beta_2|^2}{(\alpha_1\alpha_2)^2 +(\alpha_1\beta_2)^2 }$

After 2nd measurement the qubit will collapse into  |00> or |01>



## Case 2 (1st Qubit =1)

We measure only the first qubit and get the result "1"

$|\psi>=\alpha_1\alpha_2|00>+\alpha_1\beta_2|01>+\beta_1\alpha_2|10>+\beta_1\beta_2|11>$


Lets focus on $\beta_1\alpha_2$ and $\beta_1\beta_2$

Probability (0) = $|\beta_1\alpha_2|^2+|\beta_1\beta_2|^2$
After measuring the state the quantum qubit will collapse to 

$|\psi'>=\beta_1\alpha_2|00>+\beta_1\beta_2|01>$
We need to normalised the qubit after measurement 

Length = Norm = $\sqrt{(\beta_1\alpha_2)^2 +(\beta_1\beta_2)^2 }$

$$
|\psi'> = \frac{\alpha_1\alpha_2}{\sqrt{(\alpha_1\alpha_2)^2 +(\alpha_1\beta_2)^2 }} |00>+ \frac{ \alpha_1\beta_2}{\sqrt{(\alpha_1\alpha_2)^2 +(\alpha_1\beta_2)^2 }}|01>
$$
Now let us measure the 2nd Qubit 

P($2^{nd}$ Qubit =0 ) =  $\frac{|\alpha_1\alpha_2|^2}{(\alpha_1\alpha_2)^2 +(\alpha_1\beta_2)^2 }$



P($2^{nd}$ Qubit =1 ) =  $\frac{|\alpha_1\beta_2|^2}{(\alpha_1\alpha_2)^2 +(\alpha_1\beta_2)^2 }$

After 2nd measurement the qubit will collapse into  |00> or |01>

# [Measure Composite Qubits Numericals](Measure%20Composite%20Qubits%20Numericals.md)
