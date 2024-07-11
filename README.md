
# DocBook/XML Analyzer and Transformer

## Introducción

En este proyecto se aborda el análisis, validación y transformación de un subconjunto de etiquetas del lenguaje de marcado DocBook/XML utilizando un generador de analizadores léxicos y sintácticos. El objetivo es construir una utilidad que reciba un archivo en formato XML y contenido DocBook, y determine si está bien construido según el estándar, identificando cualquier error presente. Además, se requiere transformar el contenido analizado en un documento HTML.

El proceso se divide en dos etapas fundamentales: el análisis léxico y el análisis sintáctico. 

1. **Análisis léxico**: Convierte la secuencia de caracteres del programa en una secuencia lógica de tokens.
2. **Análisis sintáctico**: Recibe los tokens generados y verifica si cumplen con la gramática definida para el subconjunto de etiquetas de DocBook/XML.

## Herramientas Utilizadas

Para la implementación de esta solución, se ha utilizado:

- **Lenguaje de programación**: Python 3.11.1
- **Bibliotecas**:
  - PLY 3.11 (Python Lex-Yacc)
  - Re
  - Tkinter

Estas herramientas proporcionan las capacidades necesarias para generar analizadores léxicos y sintácticos de manera eficiente y sencilla, logrando una solución flexible y modular para analizar y validar documentos DocBook/XML, detectando errores y transformándolos en documentos HTML válidos.

## Características del Proyecto

Este proyecto combina el uso de un generador de analizadores léxicos y sintácticos con el lenguaje de programación Python y la biblioteca PLY para:

- Construir un analizador léxico y sintáctico.
- Analizar, validar y transformar un subconjunto de etiquetas de DocBook/XML en documentos HTML.
- Proporcionar información sobre la validez del documento analizado.
- Ofrecer la posibilidad de generar diversas salidas según los criterios establecidos.

## Estructura del Proyecto

El proyecto está organizado en diferentes módulos para separar las responsabilidades de cada componente:

- **Analizador Léxico**: Convierte el archivo XML en tokens.
- **Analizador Sintáctico**: Verifica la gramática de los tokens generados.
- **Transformador**: Convierte el documento DocBook/XML en un documento HTML.

## Pseudocódigo y DocType

Se utilizó el pseudocódigo y las características de DocType proporcionadas por la cátedra de Sintaxis y Semántica de los Lenguajes de la Universidad Tecnológica Nacional de Resistencia en 2023. Esto permitió comprender la estructura del lenguaje de programación para desarrollar la gramática, generar el lexer con sus respectivos tokens y codificar el parser encargado del análisis sintáctico.

## Ejemplo de Documento DocBook

```xml
<para>Texto normal <emphasis>texto destacado</emphasis></para>
```

En este ejemplo, un párrafo de texto contiene un elemento de tipo emphasis que contiene el texto: "texto destacado".

## Conclusiones

Durante la implementación de la solución, surgieron diferentes problemas que fueron resueltos. Estas soluciones y las experiencias obtenidas se explican en detalle en la conclusión del proyecto.

## Cómo Ejecutar el Proyecto

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/usuario/proyecto-docbook-analyzer.git
   ```

2. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar el analizador**:
   ```bash
   python main.py
   ```

## Contacto

Para más información, preguntas o contribuciones, por favor contacta algun desarrollador:
 -  [Lucas Kalchichen](mailto:lucas.kalchichen@gmail.com)
 -  [Valen Honnorat](mailto:correo@example.com)
 -  [Martin Lopez Soto](mailto:correo@example.com)
