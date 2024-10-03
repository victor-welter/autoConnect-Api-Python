def sanitize_string(input_string):
    if input_string is None:
        return None
    try:
        # Tente decodificar a string, se não funcionar, substitua caracteres problemáticos
        return input_string.encode('utf-8', 'replace').decode('utf-8')
    except Exception as e:
        print(f"Erro ao sanitizar string: {e}")
        return input_string  # Retorna a string original em caso de erro
