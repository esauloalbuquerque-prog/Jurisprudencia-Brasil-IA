# 🇧🇷 Jurisprudência Brasil IA

Sistema completo de integração com APIs de jurisprudência brasileira. Banco extenso para **TODAS AS ÁREAS JURÍDICAS**.

## 📚 Áreas Cobertas

- ✅ Direito Civil
- ✅ Direito Penal
- ✅ Direito do Trabalho
- ✅ Direito Administrativo
- ✅ Direito Constitucional
- ✅ Direito Tributário
- ✅ Direito Comercial
- ✅ Direito de Família
- ✅ Direito Imobiliário
- ✅ Direito Ambiental
- ✅ Direito do Consumidor
- ✅ Direito Internacional

## 🔗 APIs Integradas

### Tribunais Supremos
- **STF** - Supremo Tribunal Federal (https://dadosabertos.stf.jus.br)
- **STJ** - Superior Tribunal de Justiça (https://dadosabertos.stj.jus.br)
- **CNJ** - Conselho Nacional de Justiça (https://www.cnj.jus.br/api)

### Tribunais Regionais
- **TRF4** - Tribunal Regional Federal 4ª Região (https://dados.trf4.jus.br/api)
- **TJSP** - Tribunal de Justiça de São Paulo
- **TJRJ** - Tribunal de Justiça do Rio de Janeiro

## 📦 Instalação

### Node.js
```bash
npm install
npm start
```

### Python
```bash
pip install -r requirements.txt
python jurisprudencia_api.py
```

## 🚀 Uso Rápido

### JavaScript
```javascript
const JurisprudenciaAPI = require('./src/jurisprudencia-api.js');
const api = new JurisprudenciaAPI();
const resultado = await api.buscarAcordaoSTF('direito do trabalho');
console.log(resultado);
```

### Python
```python
from src.jurisprudencia_api import JurisprudenciaAPI
api = JurisprudenciaAPI()
resultado = api.buscar_acordao_stf('responsabilidade civil')
print(resultado)
```

## 📂 Estrutura

Veja /docs para documentação completa.