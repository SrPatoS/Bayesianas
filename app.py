p_chuva = 0.3
p_n_chuva = 0.7

p_umido_dado_chuva= 0.8
p_umido_dado_n_chuva = 0.1

p_umido = p_umido_dado_chuva * p_chuva + p_umido_dado_n_chuva * p_n_chuva

p_chuva_dado_umido = (p_umido_dado_chuva * p_chuva) / p_umido

print(f"P(umido) = {p_umido:.4f}")

print(f"P(chuva | umido) = {p_chuva_dado_umido:.4f}")