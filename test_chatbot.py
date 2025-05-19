import unittest
from unittest.mock import patch
from chatbot import mostrar_menu, procesar_opcion

class TestChatbot(unittest.TestCase):

    def test_mostrar_menu(self):
        menu = mostrar_menu()
        self.assertEqual(menu, [
            "Información sobre alimentación saludable",
            "Consejos para perder peso",
            "Hablar con nutricionista",
            "Salir"
        ])

    def test_procesar_opcion_1(self):
        resultado = procesar_opcion("1")
        self.assertEqual(resultado, "La alimentación saludable incluye frutas, verduras, proteínas magras y granos integrales.")

    def test_procesar_opcion_2(self):
        resultado = procesar_opcion("2")
        self.assertEqual(resultado, "Para perder peso es importante combinar dieta balanceada y ejercicio regular.")

    def test_opcion_invalida(self):
        resultado = procesar_opcion("9")
        self.assertEqual(resultado, "Opción no válida, por favor intenta de nuevo.")

    @patch('builtins.input', side_effect=["3", "4"])
    def test_main_interaccion(self, mock_input):
        # Este test solo verifica que el main se ejecuta con entradas simuladas.
        # No devuelve nada, solo debe correr sin errores.
        from chatbot import main
        main()  # corre la función con los inputs simulados: "3" y luego "4"
    def test_respuesta_incorrecta():
        from chatbot import responder_pregunta
        assert responder_pregunta("¿Cuál es tu color favorito?") == "Azul"  # suposición incorrecta

if __name__ == "__main__":
    unittest.main()
