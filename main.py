# main.py

def run_quiz(questions):
    score = 0
    total_questions = len(questions)

    print("¡Bienvenido al Quiz de Conocimientos Generales!\n")

    for i, q in enumerate(questions):
        print(f"--- Pregunta {i + 1} de {total_questions} ---")
        print(q['question'])

        # Mostrar opciones
        for j, option in enumerate(q['options']):
            print(f"{j + 1}. {option}")

        # Solicitar respuesta al usuario
        while True:
            try:
                user_answer = int(input("Tu respuesta (ingresa el número de la opción): "))
                if 1 <= user_answer <= len(q['options']):
                    break
                else:
                    print("Opción inválida. Por favor, ingresa un número dentro del rango de opciones.")
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número.")

        # Verificar respuesta
        if user_answer - 1 == q['answer_index']: # Restamos 1 porque las listas son base 0
            print("¡Correcto!\n")
            score += 1
        else:
            print(f"Incorrecto. La respuesta correcta era: {q['options'][q['answer_index']]}\n")

    print("--- Quiz Terminado ---")
    print(f"Tu puntuación final: {score} de {total_questions}")
    print(f"Porcentaje de aciertos: { (score / total_questions) * 100:.2f}%")

if __name__ == "__main__":
    # Define tus preguntas
    # Cada pregunta es un diccionario con:
    # 'question': La pregunta en sí.
    # 'options': Una lista de strings con las opciones.
    # 'answer_index': El índice (0-basado) de la respuesta correcta en la lista 'options'.
    quiz_questions = [
        {
            'question': "¿Cuál es la capital de Perú?",
            'options': ["Arequipa", "Cusco", "Lima", "Trujillo"],
            'answer_index': 2
        },
        {
            'question': "¿Qué planeta es conocido como el Planeta Rojo?",
            'options': ["Marte", "Júpiter", "Venus", "Saturno"],
            'answer_index': 0
        },
        {
            'question': "¿Cuál es el océano más grande del mundo?",
            'options': ["Atlántico", "Índico", "Ártico", "Pacífico"],
            'answer_index': 3
        },
        {
            'question': "¿Quién escribió 'Cien años de soledad'?",
            'options': ["Mario Vargas Llosa", "Gabriel García Márquez", "Julio Cortázar", "Jorge Luis Borges"],
            'answer_index': 1
        },
        {
            'question': "¿Cuál es el metal más abundante en la corteza terrestre?",
            'options': ["Hierro", "Cobre", "Aluminio", "Oro"],
            'answer_index': 2
        }
    ]

    run_quiz(quiz_questions)