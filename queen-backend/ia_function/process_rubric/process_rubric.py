from flask import request, jsonify

def process_rubric():
    rubric = request.json.get('rubrica')

    if rubric is None:
        return jsonify({'success': False, 'message': 'Rúbrica no recibida'}), 400

    message = (
        "Se te presenta la rúbrica para evaluar el ensayo. Consta de "
        + str(len(rubric))
        + " parámetros, cada uno con un título, descripción, valor máximo y un conjunto de niveles de desempeño (criterios)."
        + " Cada nivel tiene una descripción y un puntaje asociado."
        + " Selecciona el nivel de desempeño más adecuado para cada parámetro del ensayo."
        + " Al final, deberás presentar el puntaje total, indicando el puntaje de cada parámetro y proporcionando una breve justificación."
    )

    for index, parameter in enumerate(rubric):
        message += (
            f"\n\nParámetro {index + 1}: {parameter['title']}"
        )

        if parameter.get('description'):
            message += f"\nDescripción: {parameter['description']}"

        message += f"\nValor total: {parameter['totalValue']}\nCriterios:"

        for criteria_index, criteria in enumerate(parameter['criterias']):
            message += (
                f"\n\tCriterio {criteria_index + 1}: {criteria['description']}"
                f"\n\tValor parcial: {criteria['partialValue']}"
            )

    return jsonify({'success': True, 'message': message}), 200
