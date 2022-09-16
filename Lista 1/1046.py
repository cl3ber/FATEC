inicio, fim = map(int, input().split())

if inicio==fim:
    print("O JOGO DUROU 24 HORA(S)")
elif fim>inicio:
    print("O JOGO DUROU %i HORA(S)" %(fim-inicio))
elif inicio>fim:
    print("O JOGO DUROU %i HORA(S)" %((fim+24)-inicio))