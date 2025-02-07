positv = ['bom', 'ótimo', 'excelente', 'adoro', 'amei', 'gostei', 'maravilhoso','satisfeito', 'perfeito', 'contente']
negativ = ['ruim', 'péssimo', 'horrível', 'desapontado', 'não gostei', 'decepcionado', 'terrível', 'odiei']
negacao = ['não', 'nunca', 'jamais']
intens = ['muito', 'extremamente', 'pouco']

def process(texto):
    pontos = ['.', ',', '!', '?', ';', ':', '(', ')', '[', ']', '{', '}', '...', '..']
    for ponto in pontos:
        texto = texto.replace(ponto, '')
    texto = texto.lower()
    palavras = texto.split()
    return palavras

def analisar(texto):
    palavras = process(texto)

    positivo = 0
    negativo = 0
    negation = False
    intesenfic = 1

    for palavra in palavras:
        if palavra in intens:
            if palavra == 'muito' or palavra == 'extremamente':
                intesenfic = 2
            elif palavra == 'pouco':
                intesenfic = 0.5
            continue

        if palavra in negacao:
            negation = True
            continue
        
        if palavra in positv:
            if negation:
                negativo += intesenfic
                negation = False
            else:
                positivo += intesenfic
        
        elif palavra in negativ:
            if negation:
                positivo += intesenfic
                negation = False
            else:
                negativo += intesenfic
    
    if positivo > negativo:
        return 'Positivo', positivo, negativo
    elif negativo > positivo:
        return 'Negativo', negativo, positivo
    else:
        return 'Neutro', positivo, negativo

def lista_coments():
    comentarios = []
    qtd = int(input('Quantos comentários deseja inserir: '))
    for i in range(qtd):
        texto = input(f'Digite {i+1}° comentário a ser analisado: ')
        comentarios.append(texto)

    positivo_count = 0
    negativo_count = 0
    neutro_count = 0

    maior_positivo = ""
    maior_negativo = ""
    maior_positivo_count = 0
    maior_negativo_count = 0

    for comentario in comentarios:
        sentimento, positivo, negativo = analisar(comentario)
        if sentimento == 'Positivo':
            positivo_count += 1
        elif sentimento == 'Negativo':
            negativo_count += 1
        else:
            neutro_count += 1

        if positivo > maior_positivo_count:
            maior_positivo = comentario
            maior_positivo_count = positivo
        
        if negativo > maior_negativo_count:
            maior_negativo = comentario
            maior_negativo_count = negativo

    total_comentarios = len(comentarios)
    if total_comentarios == 0:
        print("Nenhum comentário para analisar.")
        return

    positivo_percent = (positivo_count / total_comentarios) * 100
    negativo_percent = (negativo_count / total_comentarios) * 100
    neutro_percent = (neutro_count / total_comentarios) * 1002

    print("\nResumo da análise dos comentários:")
    print(f'Positivos: {positivo_count} comentários ({positivo_percent:.2f}%)')
    print(f'Negativos: {negativo_count} comentários ({negativo_percent:.2f}%)')
    print(f'Neutros: {neutro_count} comentários ({neutro_percent:.2f}%)')

    max_barras = 50
    print("\nGráfico de barras (distribuição dos sentimentos):")
    print(f"Positivo: {'|' * int((positivo_percent / 100) * max_barras)} ({positivo_percent:.2f}%)")
    print(f"Negativo: {'|' * int((negativo_percent / 100) * max_barras)} ({negativo_percent:.2f}%)")
    print(f"Neutro:   {'|' * int((neutro_percent / 100) * max_barras)} ({neutro_percent:.2f}%)")



def menu():
    while True:
        print(f'\n{"="*50}')
        print(f'{"Bem-vindo ao sistema que analisa texto".center(50)}')
        print(f'{"="*50}')
        print('\n1 - Analisar uma frase/texto\n2 - Analisar uma lista de comentários\n3 - Sair do sistema')
        decisao = int(input('- '))

        if decisao == 1:
            frase = input('Digite a frase que será analisada: ')
            sentimento, _, _ = analisar(frase)
            print(f'A frase é: {frase}')
            print(f'Pela análise... O sentimento do texto é: {sentimento}')

        elif decisao == 2:
            lista_coments()

        elif decisao == 3:
            print('Saindo do sistema...')
            break
        else:
            print('Opção inválida, tente novamente')

menu()
