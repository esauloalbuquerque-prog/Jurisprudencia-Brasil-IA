# exemplo-basico-py.py
import json
import sys
sys.path.insert(0, '../src')

from jurisprudencia_api import JurisprudenciaAPI

def exemplo_basico():
    api = JurisprudenciaAPI()

    print('=== Exemplo 1: Buscar Acordão STF ===')
    acordao_stf = api.buscar_acordao_stf('direito do trabalho')
    print(json.dumps(acordao_stf, indent=2, ensure_ascii=False))

    print('\n=== Exemplo 2: Buscar por Área (Direito Civil) ===')
    direito_civil = api.buscar_direito_civil('responsabilidade civil')
    print(json.dumps(direito_civil, indent=2, ensure_ascii=False))

    print('\n=== Exemplo 3: Listar Ministros STF ===')
    ministros = api.listar_ministros_stf()
    print(json.dumps(ministros, indent=2, ensure_ascii=False))

    print('\n=== Exemplo 4: Buscar em Todas as Fontes ===')
    todas_fontes = api.buscar_em_todas_fontes('contratos')
    print(json.dumps(todas_fontes, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    exemplo_basico()