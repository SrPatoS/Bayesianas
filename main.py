from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

modelo = DiscreteBayesianNetwork([('Chuva', 'Umidade'), ('Irrigacao', 'Umidade')])

cpd_chuva = TabularCPD(variable='Chuva', variable_card=2, values=[[0.7], [0.3]])
cpd_irrigacao = TabularCPD(variable='Irrigacao', variable_card=2, values=[[0.6], [0.4]])
cpd_umidade = TabularCPD(
    variable='Umidade', variable_card=2,
    values=[
    [0.8, 0.4, 0.2, 0.1], # P(Umidade=0)
    [0.2, 0.6, 0.8, 0.9] # P(Umidade=1)
 ],
 evidence=['Chuva', 'Irrigacao'],
 evidence_card=[2, 2]
)

modelo.add_cpds(cpd_chuva, cpd_irrigacao, cpd_umidade)

modelo.check_model()

inferencia = VariableElimination(modelo)
resultado = inferencia.query(variables=['Umidade'], evidence={'Chuva': 0})
print(resultado)