import random

def jogar_partida():
    """
    Função que executa uma única partida do jogo de adivinhação.
    Retorna True se a partida terminou normalmente (acerto ou fim das tentativas), 
    ou False se o jogador usou o comando '1' para sair.
    """
    # Alteração: O número de tentativas é definido como 10.
    MAX_TENTATIVAS = 10
    
    # Número secreto gerado entre 1 e 100, adequado para 10 tentativas.
    NUMERO_SECRETO = random.randint(1, 100) 
    
    TENTATIVAS = 0
    
    print("\n--- INÍCIO DA NOVA PARTIDA ---")
    print(f"Pensei em um número entre 1 e 100. Você tem {MAX_TENTATIVAS} tentativas.")
    
    # LAÇO DE REPETIÇÃO principal da partida
    while TENTATIVAS < MAX_TENTATIVAS:
        TENTATIVAS += 1
        
        try:
            palpite = input(f"Tentativa {TENTATIVAS} de {MAX_TENTATIVAS}. Digite seu palpite: ")
            
            # Condição para SAIR do jogo (Requisito: digitar '1')
            if palpite == '1':
                print("\nComando de saída detectado. Encerrando o jogo.")
                return False # Sinaliza o final do jogo
                
            palpite_int = int(palpite)
            
        except ValueError:
            print("Entrada inválida. Digite um número inteiro, ou '1' para sair.")
            TENTATIVAS -= 1 # Não penaliza erros de digitação
            continue
            
        # CONDIÇÕES (IF/ELIF/ELSE)
        if palpite_int == NUMERO_SECRETO:
            print("\n" + "*" * 40)
            print(f"🎉 PARABÉNS, VOCÊ ACERTOU O NÚMERO {NUMERO_SECRETO}!")
            print(f"Você precisou de {TENTATIVAS} tentativas.")
            print("*" * 40)
            return True # Sinaliza sucesso e a possibilidade de um novo jogo

        elif palpite_int < NUMERO_SECRETO:
            print("ERRADO! O número secreto é MAIOR.")
        else:
            print("ERRADO! O número secreto é MENOR.")

    # Se sair do 'while' por falta de tentativas
    print("-" * 40)
    print("FIM DA PARTIDA! Suas 10 tentativas acabaram.")
    print(f"O número secreto era {NUMERO_SECRETO}.")
    print("-" * 40)
    return True # Sinaliza que a partida terminou e pode começar outro jogo

# --- Função Principal para Múltiplas Partidas ---

def jogo_loop():
    print("=" * 40)
    print("      JOGO DE ADIVINHAÇÃO (10 CHANCES)")
    print("=" * 40)
    print("O jogo será reiniciado após cada partida. Digite '1' a qualquer momento para sair.")
    
    continuar_jogando = True
    
    # LAÇO PRINCIPAL (WHILE): Mantém o programa rodando.
    while continuar_jogando:
        
        resultado_partida = jogar_partida()
        
        if not resultado_partida:
            # A função jogar_partida retornou False (o jogador digitou '1')
            continuar_jogando = False
        else:
            # Pergunta se quer jogar novamente
            decisao = input("\nDeseja começar um novo jogo? (s/n): ").lower()
            if decisao != 's':
                continuar_jogando = False

    print("\nObrigado por jogar! O programa foi encerrado.")

# Inicia o jogo
jogo_loop()