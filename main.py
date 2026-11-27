# Main CLI Simulator - RecuperaMed AI Agent
import json

def cargar_configuracion():
    with open('agent_config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def recuperamed_agent_simulation(mensaje_paciente):
    print(f"\n[RecuperaMed AI]: Analizando mensaje del paciente -> '{mensaje_paciente}'...")
    mensaje_lower = mensaje_paciente.lower()
    
    # 5. Escalar a Humano (Señales de Alerta)
    if any(k in mensaje_lower for k in ["fiebre", "sangre", "sangrado", "dolor insoportable", "dolor fuerte", "falta el aire", "no puedo respirar", "pus"]):
        return (
            "🚨 ALERTA MÉDICA ACTIVADA - ESCALAMIENTO A HUMANO 🚨\n"
            "[RecuperaMed AI]: He detectado una señal de alerta médica en tus síntomas.\n"
            "• Indicación: Por favor mantén el reposo y no apliques remedios caseros ni alteres tu medicación.\n"
            "• Acción: Estoy enviando una notificación prioritaria en este instante al profesional de salud a cargo para que se comunique contigo inmediatamente."
        )
    # 1 y 3. Seguir Plan & Adaptar Instrucción
    elif any(k in mensaje_lower for k in ["medicina", "pastilla", "dosis", "horario", "tomar", "receta"]):
        return (
            "[RecuperaMed AI]: Con gusto te ayudo con tu plan de medicamentos.\n"
            "Recuerda seguir las horas fijadas por tu médico. ¿Tienes alguna duda sobre si debes tomar tu medicamento con alimentos o agua?"
        )
    # 2 y 4. Detectar Dificultad & Monitorear
    else:
        return (
            "[RecuperaMed AI]: Hola, soy tu asistente de recuperación en casa.\n"
            "¿Cómo te sientes el día de hoy con tu herida/tratamiento y cómo va tu descanso?"
        )

if __name__ == "__main__":
    config = cargar_configuracion()
    print("==================================================")
    print(f"  {config['agent_name']} v{config['version']} - SIMULADOR ACTIVO")
    print("==================================================")
    
    print("Escribe 'salir' para finalizar la simulación.")
    while True:
        entrada = input("\nPaciente: ")
        if entrada.lower() == 'salir':
            break
        respuesta = recuperamed_agent_simulation(entrada)
        print(respuesta)
