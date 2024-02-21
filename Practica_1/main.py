import stanza

stanza.download('es')  # Descargar el modelo en español

nlp = stanza.Pipeline(lang='es', processors='tokenize,mwt,pos,lemma') 

# Ruta al archivo de texto
archivo = r"pinocho.txt"
ar_salida="pinocho_result.txt"

# Leer el contenido del archivo
with open(archivo, 'r', encoding='utf-8') as file:
    texto = file.read()

# Procesar el texto con Stanza
doc = nlp(texto)

# Abrir el archivo resultados.txt en modo escritura
with open("pinocho_result.txt", "w", encoding="utf-8") as archivo_resultados:
    # Definimos una variable de número de oración
    noracion = 0
    for sent in doc.sentences:
        noracion += 1
        archivo_resultados.write(f'===== Frase {noracion} tokens =====\n')
        for word in sent.words:
            #Guardamos la linea como se solicita en el documento id - palabra - lema
            archivo_resultados.write(f'id: {word.id}'.ljust(8) + f'Palabra: {word.text}'.ljust(25) + f'Lema: {word.lemma}\n')

# Verificar si el archivo se creó correctamente
try:
    with open(ar_salida, 'r', encoding='utf-8') as file:
        print(f"Los resultados se han guardado en el archivo '{ar_salida}' correctamente.")
except FileNotFoundError:
    print("Error: No se pudo crear el archivo para guardar los resultados.")