# Chansy AI - Agente de Acompañamiento en Recuperación Domiciliaria

**Chansy AI** es un agente de Inteligencia Artificial agéntica diseñado para brindar acompañamiento continuo 24/7 a pacientes adultos en proceso de recuperación en el hogar tras un procedimiento quirúrgico, tratamiento complejo u hospitalización, basado en la metodología SkillUp de ideación centrada en el usuario.

---

## 👥 Integrantes del Equipo
- **Yarely Belen Jiménez Diego**
- **Adrián Bautista Guerrero**
- **Cesar Alejandro Aguirre Martínez**
- **Omar Anaya Martinez**

---

## 📋 Descripción del Proyecto
Chansy AI aborda la ansiedad, la confusión y la falta de respuesta inmediata que experimentan los pacientes tras ser dados de alta. El agente ayuda al usuario a seguir su plan de cuidados domiciliarios, responde dudas sobre prescripciones en lenguaje sencillo, evalúa el progreso y monitorea la presencia de síntomas de riesgo, notificando y escalando el caso inmediatamente con el profesional médico responsable cuando detecta señales de alerta.

---

## 🔄 Flujo Operativo Agéntico (5 Fases)
1. **Seguir Plan**: Gestión y recordatorio de medicamentos, ejercicios de rehabilitación, curaciones y citas médicas.
2. **Detectar Dificultad**: Identificación proactiva de olvidos, dudas frecuentes, barreras de cumplimiento o síntomas físicos inusuales.
3. **Adaptar Instrucción**: Traducción de jerga clínica y folletos complejos a instrucciones simples, empáticas y personalizadas.
4. **Monitorear**: Evaluación continua del progreso diario y de la adherencia al tratamiento prescrito.
5. **Escalar a Humano**: Notificación prioritaria y transferencia inmediata del control al médico humano ante cualquier señal de riesgo o emergencia.

---

## 🛠️ Tecnologías e Infraestructura
- **IBM Bob**: Entorno de asistencia y orquestación agéntica (`custom_modes.yaml`).
- **IBM watsonx.ai / watsonx Orchestrate**: Inferencia de modelos de lenguaje y gestión de habilidades (Skills).
- **RAG (Retrieval-Augmented Generation)**: Ingesta de planes de alta médica, fichas farmacológicas y guías de semaforización de síntomas.
- **Python**: Simulador interactivo en consola para pruebas del flujo agéntico.

---

## 📁 Estructura del Repositorio
- `custom_modes.yaml`: Definición del modo agéntico `recupera-med-ai` para IBM Bob.
- `system_prompt.md`: Directivas, flujo de 5 pasos, personalidad y restricciones duras del agente.
- `agent_config.json`: Parámetros de inferencia, Skills y fuentes de conocimiento RAG.
- `rag_knowledge_base.md`: Esquema de la base de conocimiento clínico y reglas de semaforización de síntomas.
- `main.py`: Simulador interactivo CLI para validar las 5 fases y el escalamiento médico.
- `.gitignore`: Configuración estándar de exclusiones para Git.
