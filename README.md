
QuizMaster es un sencillo y adictivo juego de preguntas y respuestas desarrollado en Python para ser ejecutado directamente en la consola. Pon a prueba tus conocimientos generales a través de múltiples preguntas con opciones de respuesta, obtén feedback instantáneo y descubre tu puntuación final al terminar el quiz.  Ideal para practicar Python o para un rápido desafío mental.

# QuizMaster: Tu Reto de Conocimientos en Consola

## 🚀 Descripción del Proyecto

**QuizMaster** es una aplicación de juego de preguntas y respuestas (quiz) desarrollada en **Python** que se ejecuta directamente en tu terminal. Diseñado para ser simple y funcional, este proyecto te permite poner a prueba tus conocimientos sobre diversos temas, recibir feedback instantáneo sobre tus respuestas y ver tu puntuación final. Es una excelente manera de practicar programación en Python y entender la lógica básica de un juego interactivo.

## ✨ Características

* **Múltiples Preguntas:** Un conjunto predefinido de preguntas para desafiarte.
* **Opciones Múltiples:** Cada pregunta presenta varias opciones de respuesta.
* **Feedback Instantáneo:** Descubre si tu respuesta es correcta o incorrecta al momento.
* **Puntuación Final:** Obtén tu resultado al finalizar el quiz, incluyendo el porcentaje de aciertos.
* **Interfaz de Consola Sencilla:** Fácil de usar y ejecutar sin dependencias complejas.

## 🛠️ Tecnologías Utilizadas

* **Python 3.x**

## 🚀 Cómo Ejecutar el Proyecto

Sigue estos sencillos pasos para poner en marcha QuizMaster en tu máquina:

1.  **Clona este repositorio** (o descarga el archivo `main.py` directamente).
   
    git clone https://github.com/santiagourdaneta/Juego-de-Preguntas-y-Respuestas-Quiz-App---Python-Consola-/ 
   
2.  **Navega a la carpeta del proyecto** en tu terminal.
    
    cd Juego-de-Preguntas-y-Respuestas-Quiz-App---Python-Consola-/

3.  **Ejecuta el script de Python:**
    
    python main.py

4.  ¡Sigue las instrucciones en la consola para jugar!

## 💡 Personalización

Puedes personalizar fácilmente las preguntas y respuestas editando la lista `quiz_questions` dentro del archivo `main.py`.

quiz_questions = [
    {
        'question': "¿Cuál es la capital de Perú?",
        'options': ["Arequipa", "Cusco", "Lima", "Trujillo"],
        'answer_index': 2 # Lima es la tercera opción, índice 2 (0-basado)
    },
    # Añade o modifica más preguntas aquí
]


