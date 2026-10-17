# 🔗 APIs de Jurisprudência Brasileira

## STF - Supremo Tribunal Federal

**URL Base:** https://dadosabertos.stf.jus.br/api

### Endpoints

1. **Acordãos**
   - GET `/acordaos`
   - Parâmetros: q (palavra-chave), page, limit
   - Retorna: JSON

2. **Decisões**
   - GET `/decisoes`
   - Parâmetros: q, page, limit

3. **Processos**
   - GET `/processos/{numero}`
   - Retorna detalhes do processo

4. **Ministros**
   - GET `/ministros`
   - Lista todos os ministros

## STJ - Superior Tribunal de Justiça

**URL Base:** https://dadosabertos.stj.jus.br/api

### Endpoints

1. **Acordãos**
   - GET `/acordaos`
   - Suporta busca por palavras-chave

2. **Jurisprudência por Área**
   - GET `/jurisprudencia`
   - Parâmetros: area, q, limit
   - Áreas: Civil, Penal, Trabalhista, Administrativa

3. **Decisões**
   - GET `/decisoes`

## CNJ - Conselho Nacional de Justiça

**URL Base:** https://www.cnj.jus.br/api

### Endpoints

1. **DataJud**
   - GET `/datajud`
   - Consulta processual integrada
   - Requer: número do processo

2. **Consulta Processual**
   - GET `/consulta-processual`

## TRF4 - Tribunal Regional Federal

**URL Base:** https://dados.trf4.jus.br/api

### Endpoints

1. **Acordãos**
   - GET `/acordaos`
   - Busca por palavra-chave

2. **Processos**
   - GET `/processos`

## Escavador

**URL Base:** https://www.escavador.com/api

### Endpoints

1. **Busca Geral**
   - GET `/search`
   - Agregador de múltiplos tribunais
   - Requer: API Key

---

**Nota:** Todas as APIs acima são públicas e gratuitas. Algumas requerem cadastro simples.