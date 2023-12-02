
#Binomial Distribution with examples

I was using the `numpy.random.binomial` function and started to wonder if I understood the intuition behind the Binomial distribution - I didn't. 

Let's join hands and explore Binomial Distribution with practical examples. Here is our toy example:

Suppose we have a bag containing 5 yellow and 4 green balls. For the following questions, let's assume that each time you draw a ball, you replace it, ensuring the probabilities remain constant for each draw (this is an important aspect for the scenario to fit a binomial distribution). Based on the above, I came up with a set of questions covering various scenarios, e.g. exact number of success (yellow ball draw in this case), a range on the number of successes (at least 5, more than 6, etc.), testing symmetry of the binomial coefficients. Let's go and answer them:

1. **Probability of Drawing a Specific Number of Yellow Balls in a Fixed Number of Draws**
   **Question:** If you draw a ball from the bag 10 times (with replacement), what is the probability of getting exactly 6 yellow balls? <br>
   **Answer:** The probability is calculated using the binomial distribution formula: 
     $P(X = 6) = \binom{10}{6} \left(\frac{5}{9}\right)^6 \left(\frac{4}{9}\right)^4$

2. **Comparing Probabilities for Different Numbers of Successes**  
   **Question:** In 8 draws, which is more likely - drawing exactly 3 yellow balls or exactly 5 yellow balls?<br>
   **Answer:** 
     - Probability of 3 Yellow Balls: 
       $P(X = 3) = \binom{8}{3} \left(\frac{5}{9}\right)^3 \left(\frac{4}{9}\right)^5$
     - Probability of 5 Yellow Balls: 
       $P(X = 5) = \binom{8}{5} \left(\frac{5}{9}\right)^5 \left(\frac{4}{9}\right)^3$

3. **Probability of Drawing At Least a Certain Number of Yellow Balls**  
   **Question:** What is the probability of drawing at least 4 yellow balls in 7 draws?  
   **Answer:** The probability is the sum of probabilities of drawing 4, 5, 6, and 7 yellow balls: 
     $P(X \geq 4) = \sum_{k=4}^{7} \binom{7}{k} \left(\frac{5}{9}\right)^k \left(\frac{4}{9}\right)^{7-k}$

4. **Effect of Changing the Number of Trials on Probability**  
   **Question:** How does the probability of drawing exactly 2 yellow balls change when you increase the number of draws from 5 to 10?  
   **Answer:** 
     - Probability in 5 Draws: 
       $P(X = 2) = \binom{5}{2} \left(\frac{5}{9}\right)^2 \left(\frac{4}{9}\right)^3$
     - Probability in 10 Draws: 
       $P(X = 2) = \binom{10}{2} \left(\frac{5}{9}\right)^2 \left(\frac{4}{9}\right)^8$

5. **Varying the Probability of Success**  
   **Question:** If one yellow ball is removed from the bag (making it 4 yellow and 4 green), how does this change the probability of drawing exactly 3 yellow balls in 6 draws?  
   **Answer:** With the new probability of a yellow ball being \( p' = \frac{4}{8} = \frac{1}{2} \), the probability is: 
     $P(X = 3) = \binom{6}{3} \left(\frac{1}{2}\right)^3 \left(\frac{1}{2}\right)^3$

6. **Combining Successes and Failures**  
   **Question:** In 12 draws, what is the probability of drawing exactly 7 yellow balls and 5 green balls?  
   **Answer:** The probability is calculated as: 
     $P(X = 7) = \binom{12}{7} \left(\frac{5}{9}\right)^7 \left(\frac{4}{9}\right)^5$

### Additional Discussion

**Symmetry in Binomial Coefficients**  
  - **Observation:** The binomial coefficients for certain combinations, like 7 successes out of 10 trials and 3 successes out of 10 trials, are the same.
  - **Reason:** This symmetry arises because choosing \(k\) successes out of \(n\) trials is equivalent to choosing \(n-k\) failures, leading to the equality 
    $ \binom{n}{k} = \binom{n}{n-k} $
  - **Significance:** This symmetry reflects the dual nature of success and failure in binomial situations and simplifies calculations by allowing the focus on the smaller of the two numbers (successes or failures).


In summary, we covered a comprehensive overview of the binomial distribution through a series of questions and answers related to drawing balls from a bag containing yellow and green balls. We covered concepts such as calculating the probability of drawing a specific number of yellow balls, comparing probabilities for different outcomes, and the impact of varying trial numbers and success probabilities. The significance and symmetry of binomial coefficients were also explained, highlighting the dual nature of success and failure in binomial situations. 
