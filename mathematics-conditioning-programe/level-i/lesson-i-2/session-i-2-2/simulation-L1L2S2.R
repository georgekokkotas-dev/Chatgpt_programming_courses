N <- 257
p <- 0.37
q <- 1 - p
E_AA <- N * p^2
E_Aa <- 2 * N * p * q
E_aa <- N * q^2
sum_gen <- E_AA + E_Aa + E_aa
sum_gen == N
print(N)
print(sum_gen)

print(round(E_AA, digits = 10))
print(round(E_Aa, digits = 10))
print(round(E_aa, digits = 10))
# This is a simulation for the MCP Courses.
# No real data used here.
