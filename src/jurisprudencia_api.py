# jurisprudencia_api.py
import requests
import json
from datetime import datetime
from typing import Dict, List, Optional

class JurisprudenciaAPI:
    def __init__(self):
        self.apis = {
            'stf': 'https://dadosabertos.stf.jus.br/api',
            'stj': 'https://dadosabertos.stj.jus.br/api',
            'cnj': 'https://www.cnj.jus.br/api',
            'trf4': 'https://dados.trf4.jus.br/api'
        }
        self.timeout = 10
        self.cache = {}

    # ====== STF - SUPREMO TRIBUNAL FEDERAL ======

    def buscar_acordao_stf(self, palavra_chave: str, pagina: int = 1) -> Optional[Dict]:
        """Busca acordãos no STF"""
        try:
            cache_key = f'stf-acordao-{palavra_chave}-{pagina}'
            if cache_key in self.cache:
                return self.cache[cache_key]

            response = requests.get(
                f"{self.apis['stf']}/acordaos",
                params={
                    'q': palavra_chave,
                    'page': pagina,
                    'limit': 10
                },
                timeout=self.timeout
            )
            response.raise_for_status()
            dados = response.json()
            self.cache[cache_key] = dados
            return dados
        except requests.exceptions.RequestException as e:
            print(f'Erro ao buscar acordão STF: {str(e)}')
            return None

    def buscar_processo_stf(self, numero_processo: str) -> Optional[Dict]:
        """Busca processo específico no STF"""
        try:
            response = requests.get(
                f"{self.apis['stf']}/processos/{numero_processo}",
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Erro ao buscar processo STF: {str(e)}')
            return None

    def buscar_decisao_stf(self, palavra_chave: str, pagina: int = 1) -> Optional[Dict]:
        """Busca decisões no STF"""
        try:
            response = requests.get(
                f"{self.apis['stf']}/decisoes",
                params={
                    'q': palavra_chave,
                    'page': pagina,
                    'limit': 10
                },
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Erro ao buscar decisão STF: {str(e)}')
            return None

    def listar_ministros_stf(self) -> Optional[Dict]:
        """Lista todos os ministros do STF"""
        try:
            cache_key = 'stf-ministros'
            if cache_key in self.cache:
                return self.cache[cache_key]

            response = requests.get(
                f"{self.apis['stf']}/ministros",
                timeout=self.timeout
            )
            response.raise_for_status()
            dados = response.json()
            self.cache[cache_key] = dados
            return dados
        except requests.exceptions.RequestException as e:
            print(f'Erro ao listar ministros: {str(e)}')
            return None

    # ====== STJ - SUPERIOR TRIBUNAL DE JUSTIÇA ======

    def buscar_acordao_stj(self, palavra_chave: str, pagina: int = 1) -> Optional[Dict]:
        """Busca acordãos no STJ"""
        try:
            cache_key = f'stj-acordao-{palavra_chave}-{pagina}'
            if cache_key in self.cache:
                return self.cache[cache_key]

            response = requests.get(
                f"{self.apis['stj']}/acordaos",
                params={
                    'q': palavra_chave,
                    'page': pagina,
                    'limit': 10
                },
                timeout=self.timeout
            )
            response.raise_for_status()
            dados = response.json()
            self.cache[cache_key] = dados
            return dados
        except requests.exceptions.RequestException as e:
            print(f'Erro ao buscar acordão STJ: {str(e)}')
            return None

    def buscar_por_area(self, area: str, palavra_chave: str, pagina: int = 1) -> Optional[Dict]:
        """Busca jurisprudência por área específica"""
        try:
            cache_key = f'stj-area-{area}-{palavra_chave}-{pagina}'
            if cache_key in self.cache:
                return self.cache[cache_key]

            response = requests.get(
                f"{self.apis['stj']}/jurisprudencia",
                params={
                    'area': area,
                    'q': palavra_chave,
                    'page': pagina,
                    'limit': 20
                },
                timeout=self.timeout
            )
            response.raise_for_status()
            dados = response.json()
            self.cache[cache_key] = dados
            return dados
        except requests.exceptions.RequestException as e:
            print(f'Erro ao buscar {area}: {str(e)}')
            return None

    # Métodos por área
    def buscar_direito_civil(self, palavra_chave: str) -> Optional[Dict]:
        return self.buscar_por_area('civil', palavra_chave)

    def buscar_direito_penal(self, palavra_chave: str) -> Optional[Dict]:
        return self.buscar_por_area('penal', palavra_chave)

    def buscar_direito_trabalho(self, palavra_chave: str) -> Optional[Dict]:
        return self.buscar_por_area('trabalho', palavra_chave)

    def buscar_direito_administrativo(self, palavra_chave: str) -> Optional[Dict]:
        return self.buscar_por_area('administrativo', palavra_chave)

    def buscar_direito_tributario(self, palavra_chave: str) -> Optional[Dict]:
        return self.buscar_por_area('tributario', palavra_chave)

    def buscar_direito_familia(self, palavra_chave: str) -> Optional[Dict]:
        return self.buscar_por_area('familia', palavra_chave)

    def buscar_direito_consumidor(self, palavra_chave: str) -> Optional[Dict]:
        return self.buscar_por_area('consumidor', palavra_chave)

    # ====== CNJ - CONSELHO NACIONAL DE JUSTIÇA ======

    def buscar_datajud(self, numero_processo: str) -> Optional[Dict]:
        """Busca no DataJud do CNJ"""
        try:
            response = requests.get(
                f"{self.apis['cnj']}/datajud",
                params={'processo': numero_processo},
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Erro DataJud: {str(e)}')
            return None

    # ====== TRF4 - TRIBUNAL REGIONAL FEDERAL ======

    def buscar_acordao_trf4(self, palavra_chave: str, pagina: int = 1) -> Optional[Dict]:
        """Busca acordãos no TRF4"""
        try:
            response = requests.get(
                f"{self.apis['trf4']}/acordaos",
                params={
                    'q': palavra_chave,
                    'page': pagina,
                    'limit': 10
                },
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Erro TRF4: {str(e)}')
            return None

    # ====== BUSCA INTEGRADA ======

    def buscar_em_todas_fontes(self, palavra_chave: str) -> Dict:
        """Busca em todas as fontes disponíveis"""
        return {
            'stf': self.buscar_acordao_stf(palavra_chave),
            'stj': self.buscar_acordao_stj(palavra_chave),
            'trf4': self.buscar_acordao_trf4(palavra_chave),
            'timestamp': datetime.now().isoformat()
        }

    def buscar_por_area_em_todas_fontes(self, area: str, palavra_chave: str) -> Dict:
        """Busca por área em todas as fontes"""
        return {
            'area': area,
            'stj': self.buscar_por_area(area, palavra_chave),
            'timestamp': datetime.now().isoformat()
        }

    # Utility
    def limpar_cache(self):
        """Limpa o cache de buscas"""
        self.cache.clear()

    def exporter_para_json(self, dados: Dict, arquivo: str):
        """Exporta resultados para JSON"""
        with open(arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    api = JurisprudenciaAPI()
    resultado = api.buscar_direito_civil('responsabilidade civil')
    print(json.dumps(resultado, indent=2, ensure_ascii=False))