'''
No sistema SI, a vazão de um fluido é medida em metros
cúbicos por segundo (m3 /s). A medida do sistema inglês
de vazão, o pé cúbico por segundo (ft3 /s) é equivalente
a 0.028 m 3 /s. Escreva uma rotina que pede ao usuário pela
vazão em metros cúbicos por segundo e converte essa vazão
para a unidade inglesa, exibindo o seguinte ao usuário:
Um fluxo de 15.2000 metros cúbicos por segundo
é equivalente a 542.8571 pés cúbicos por segundo
'''
flux_metro = float(input('digite um valor em metro cubicos por segundo'))
flux_pe = flux_metro*0.028
print(f'uma vazão de {flux_metro:.3f} equivale a {flux_pe:.3f}')
