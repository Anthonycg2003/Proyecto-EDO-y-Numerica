import math
from datetime import datetime

def convertir_con_datetime(hora_str: str) -> float:
    """
    Convierte una hora en formato 12h (ej: '12:30 pm') a formato decimal.
    
    Args:
        hora_str: String con la hora en formato 12h
        
    Returns:
        Hora en formato decimal (ej: 12.5 para las 12:30)
    """
    try:
        dt = datetime.strptime(hora_str, '%I:%M %p')
    except ValueError:
        dt = datetime.strptime(hora_str, '%I %p')
    
    # Convertir a horas decimales: horas + minutos/60 + segundos/3600
    horas_decimal: float = dt.hour + dt.minute / 60.0 + dt.second / 3600.0
    
    return horas_decimal

def decimal_a_hora12_datetime(hora_decimal: float) -> str:
    """
    Convierte una hora en formato decimal a formato 12h (ej: '12:30 pm').
    
    Args:
        hora_decimal: Hora en formato decimal
        
    Returns:
        String con la hora en formato 12h
    """
    # Extraer horas enteras
    horas: int = int(hora_decimal)
    # Calcular minutos decimales a partir de la parte fraccionaria
    minutos_dec: float = (hora_decimal - horas) * 60
    minutos: int = int(minutos_dec)
    # Calcular segundos a partir de la parte fraccionaria de los minutos
    segundos: int = int((minutos_dec - minutos) * 60)
    
    # Crear objeto datetime para usar strftime
    dt: datetime = datetime(2024, 1, 1, horas, minutos, segundos)
    
    # Seleccionar formato según si hay minutos o segundos
    formato: str = '%I:%M %p' if minutos > 0 or segundos > 0 else '%I %p'
    resultado: str = dt.strftime(formato).lstrip('0')
    
    return resultado

def solve_A(Ta: float, T1: float, T2: float, t1_str: str, t2_str: str, Td: float) -> None:
    """
    Resuelve la hora de muerte usando la ley de enfriamiento de Newton.
    
    Utiliza dos mediciones de temperatura en tiempos diferentes para determinar
    cuándo la víctima tenía la temperatura Td (generalmente 98.6°F).
    
    Args:
        Ta: Temperatura ambiente (°F)
        T1: Primera temperatura medida (°F)
        T2: Segunda temperatura medida (°F)
        t1_str: Hora de la primera medición en formato 12h
        t2_str: Hora de la segunda medición en formato 12h
        Td: Temperatura en el momento de la muerte (°F)
    """
    # Convertir strings de hora a formato decimal
    t1: float = convertir_con_datetime(t1_str)
    t2: float = convertir_con_datetime(t2_str)
    
    # Calcular constante c de la ecuación: T(t) = e^(kt)*c + Ta
    c: float = T1 - Ta
    
    # Calcular intervalo de tiempo entre mediciones
    time: float = t2 - t1
    
    # Calcular constante k usando la segunda medición
    k: float = math.log((T2 - Ta) / c) / time
    
    # Calcular tiempo transcurrido desde la muerte hasta la primera medición
    t: float = math.log((Td - Ta) / c) / k
    
    # Calcular hora de muerte y convertir a formato 12h
    td_str: str = decimal_a_hora12_datetime(t1 + t)
    
    print(f'La victima murio a las {td_str}')

# Ejecutar ejemplo: temperatura ambiente 70°F, mediciones de 80°F a las 12pm y 75°F a la 1pm
solve_A(70, 80, 75, '12 pm', '1 pm', 98.6)
