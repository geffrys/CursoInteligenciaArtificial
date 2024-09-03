import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl
import matplotlib.pyplot as plt
import io


# Definir los antecedentes (input variables) Fuzzificacion.
hour = ctrl.Antecedent(np.arange(0, 25, 1), 'hour')
mood = ctrl.Antecedent(np.arange(0, 11, 1), 'mood')  # 0 a 10 (0: triste, 10: feliz)
volume = ctrl.Consequent(np.arange(0, 11, 1), 'volume')
# Fin de fuzzificacion.
# Definir las funciones de membresía para cada antecedente
volume['bajo'] = fuzz.trimf(volume.universe, [0, 2, 4])
volume['medio'] = fuzz.trimf(volume.universe, [3, 5, 7])
volume['alto'] = fuzz.trimf(volume.universe, [6, 8, 10])
hour['madrugada'] = fuzz.trapmf(hour.universe, [0, 2, 4, 6])
hour['manana'] = fuzz.trapmf(hour.universe, [5, 7 , 11, 13])
hour['tarde'] = fuzz.trapmf(hour.universe, [12, 14, 16, 18])
hour['noche'] = fuzz.trapmf(hour.universe, [17, 19, 22, 25]
                           )
mood['triste'] = fuzz.trapmf(mood.universe, [0, .5, 3.5, 4])
mood['normal'] = fuzz.trapmf(mood.universe, [3, 3.5, 6.5, 7])
mood['feliz'] = fuzz.trapmf(mood.universe, [6, 6.5, 9.5, 11])
# Fin de definicion de memberships

# Reglas difusas
rule1 = ctrl.Rule(hour['madrugada'] & mood['triste'], volume['bajo'])
rule2 = ctrl.Rule(hour['madrugada'] & mood['feliz'], volume['alto'])
rule3 = ctrl.Rule(hour['manana'] & mood['triste'], volume['medio'])
rule4 = ctrl.Rule(hour['manana'] & mood['feliz'], volume['alto'])
rule5 = ctrl.Rule(hour['tarde'] & mood['triste'], volume['medio'])
rule6 = ctrl.Rule(hour['tarde'] & mood['feliz'], volume['alto'])
rule7 = ctrl.Rule(hour['noche'] & mood['triste'], volume['bajo'])
rule8 = ctrl.Rule(hour['noche'] & mood['feliz'], volume['medio'])
rule9 = ctrl.Rule(hour['madrugada'] & mood['normal'], volume['bajo'])
rule10 = ctrl.Rule(hour['manana'] & mood['normal'], volume['medio'])
rule11 = ctrl.Rule(hour['tarde'] & mood['normal'], volume['alto'])
rule12 = ctrl.Rule(hour['noche'] & mood['normal'], volume['medio'])
volume_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12])
# Crear la simulación del sistema de control
volume_level = ctrl.ControlSystemSimulation(volume_ctrl)
# Fin reglas difusas

def visualizacion_volumen():        
    volume.view()
    plt.title('Volumen del sistema de audio')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    return buf

def visualizacion_hour():
    hour.view()
    plt.title('Hora del día')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    return buf

def visualizacion_mood():
    mood.view()
    plt.title('Estado de ánimo')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    return buf


def evaluate_(hora: any, estado_animo: any): 
    volume_level.reset()
    # Evaluar el volumen basado en hora y estado de ánimo
    volume_level.input['hour'] = hora
    volume_level.input['mood'] = estado_animo
    volume_level.compute()

    result = volume_level.output['volume']
    print(f'El volumen del sistema de audio es: {result}')

    volume.view(sim=volume_level)
    plt.title('Volumen del sistema de audio')
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    return buf


evaluate_(2, 3)
