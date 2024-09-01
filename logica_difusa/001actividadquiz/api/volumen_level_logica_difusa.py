import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl
import matplotlib.pyplot as plt

def evaluate_(hora: any, estado_animo: any): 
    # Definir los antecedentes (input variables) Fuzzificacion.
    volume = ctrl.Antecedent(np.arange(0, 11, 1), 'volume')
    hour = ctrl.Antecedent(np.arange(0, 25, 1), 'hour')
    mood = ctrl.Antecedent(np.arange(0, 11, 1), 'mood')  # 0 a 10 (0: triste, 10: feliz)
    # Fin de fuzzificacion.

    # Definir las funciones de membresía para cada antecedente
    volume['bajo'] = fuzz.trimf(volume.universe, [0, 2, 4])
    volume['medio'] = fuzz.trimf(volume.universe, [3, 5, 7])
    volume['alto'] = fuzz.trimf(volume.universe, [6, 8, 10])

    hour['madrugada'] = fuzz.trimf(hour.universe, [0, 3, 6])
    hour['manana'] = fuzz.trimf(hour.universe, [5, 10 , 13])
    hour['tarde'] = fuzz.trimf(hour.universe, [12, 15, 18])
    hour['noche'] = fuzz.trimf(hour.universe, [17, 21, 24]
                               )
    mood['triste'] = fuzz.trimf(mood.universe, [0, 2, 4])
    mood['normal'] = fuzz.trimf(mood.universe, [3, 5, 7])
    mood['feliz'] = fuzz.trimf(mood.universe, [6,8 , 10])
    # Fin de definicion de memberships

    # Visualización de las funciones de membresía
    def visualizacion():        
        volume.view()
        hour.view()
        mood.view()
        plt.show()
    visualizacion()
    # Bloque de visualizacion.

    # Reglas difusas
    rule1 = ctrl.Rule(hour['madrugada'] & mood['triste'], volume['bajo'])
    rule2 = ctrl.Rule(hour['madrugada'] & mood['feliz'], volume['alto'])
    rule3 = ctrl.Rule(hour['manana'] & mood['triste'], volume['medio'])
    rule4 = ctrl.Rule(hour['manana'] & mood['feliz'], volume['alto'])
    rule5 = ctrl.Rule(hour['tarde'] & mood['triste'], volume['medio'])
    rule6 = ctrl.Rule(hour['tarde'] & mood['feliz'], volume['alto'])
    rule7 = ctrl.Rule(hour['noche'] & mood['triste'], volume['bajo'])
    rule8 = ctrl.Rule(hour['noche'] & mood['feliz'], volume['alto'])
    volume_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8])
    # Fin reglas difusas

    # Crear la simulación del sistema de control
    volume_level = ctrl.ControlSystemSimulation(volume_ctrl)

    # Evaluar el volumen basado en hora y estado de ánimo
    volume_level.input['hour'] = hora
    volume_level.input['mood'] = estado_animo
    volume_level.input['volume'] = None
    print(f"Inputs asignados: Hora - {hora}, Estado de ánimo - {estado_animo}")
    volume_level.compute()

    volume.view(sim=volume_level)
    plt.show()

evaluate_(5, 4)
