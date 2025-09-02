ContaBancaria = {
    "numeroConta": 12345-6,
    "agencia": 1234,
    "saldo": 000.00,
    "titular": "Isaac Lopes"
}

exibir_saldo = lambda conta: f"Titular: {conta['titular']} | Saldo atual: R$ {conta['saldo']:.2f}"

print(exibir_saldo(ContaBancaria))
