// jurisprudencia-api.js
const axios = require('axios');

class JurisprudenciaAPI {
  constructor() {
    this.apis = {
      stf: 'https://dadosabertos.stf.jus.br/api',
      stj: 'https://dadosabertos.stj.jus.br/api',
      cnj: 'https://www.cnj.jus.br/api',
      trf4: 'https://dados.trf4.jus.br/api'
    };
    this.timeout = 10000;
    this.cache = {};
  }

  // ====== STF - SUPREMO TRIBUNAL FEDERAL ======

  async buscarAcordaoSTF(palavraChave, pagina = 1) {
    try {
      const cacheKey = `stf-acordao-${palavraChave}-${pagina}`;
      if (this.cache[cacheKey]) return this.cache[cacheKey];

      const response = await axios.get(`${this.apis.stf}/acordaos`, {
        params: {
          q: palavraChave,
          page: pagina,
          limit: 10
        },
        timeout: this.timeout
      });

      this.cache[cacheKey] = response.data;
      return response.data;
    } catch (error) {
      console.error('Erro ao buscar acordão STF:', error.message);
      return { erro: error.message, dados: null };
    }
  }

  async buscarProcessoSTF(numeroProcesso) {
    try {
      const response = await axios.get(
        `${this.apis.stf}/processos/${numeroProcesso}`,
        { timeout: this.timeout }
      );
      return response.data;
    } catch (error) {
      console.error('Erro ao buscar processo STF:', error.message);
      return null;
    }
  }

  async buscarDecisaoSTF(palavraChave, pagina = 1) {
    try {
      const response = await axios.get(`${this.apis.stf}/decisoes`, {
        params: {
          q: palavraChave,
          page: pagina,
          limit: 10
        },
        timeout: this.timeout
      });
      return response.data;
    } catch (error) {
      console.error('Erro ao buscar decisão STF:', error.message);
      return null;
    }
  }

  async listarMinistrosSTF() {
    try {
      const cacheKey = 'stf-ministros';
      if (this.cache[cacheKey]) return this.cache[cacheKey];

      const response = await axios.get(`${this.apis.stf}/ministros`, {
        timeout: this.timeout
      });
      this.cache[cacheKey] = response.data;
      return response.data;
    } catch (error) {
      console.error('Erro ao listar ministros:', error.message);
      return null;
    }
  }

  // ====== STJ - SUPERIOR TRIBUNAL DE JUSTIÇA ======

  async buscarAcordaoSTJ(palavraChave, pagina = 1) {
    try {
      const cacheKey = `stj-acordao-${palavraChave}-${pagina}`;
      if (this.cache[cacheKey]) return this.cache[cacheKey];

      const response = await axios.get(`${this.apis.stj}/acordaos`, {
        params: {
          q: palavraChave,
          page: pagina,
          limit: 10
        },
        timeout: this.timeout
      });
      this.cache[cacheKey] = response.data;
      return response.data;
    } catch (error) {
      console.error('Erro ao buscar acordão STJ:', error.message);
      return null;
    }
  }

  async buscarPorArea(area, palavraChave, pagina = 1) {
    try {
      const cacheKey = `stj-area-${area}-${palavraChave}-${pagina}`;
      if (this.cache[cacheKey]) return this.cache[cacheKey];

      const response = await axios.get(`${this.apis.stj}/jurisprudencia`, {
        params: {
          area: area,
          q: palavraChave,
          page: pagina,
          limit: 20
        },
        timeout: this.timeout
      });
      this.cache[cacheKey] = response.data;
      return response.data;
    } catch (error) {
      console.error(`Erro ao buscar ${area}:`, error.message);
      return null;
    }
  }

  // Áreas disponíveis
  async buscarDireitoCivil(palavraChave) {
    return this.buscarPorArea('civil', palavraChave);
  }

  async buscarDireitoPenal(palavraChave) {
    return this.buscarPorArea('penal', palavraChave);
  }

  async buscarDireitoTrabalho(palavraChave) {
    return this.buscarPorArea('trabalho', palavraChave);
  }

  async buscarDireitoAdministrativo(palavraChave) {
    return this.buscarPorArea('administrativo', palavraChave);
  }

  async buscarDireitoTributario(palavraChave) {
    return this.buscarPorArea('tributario', palavraChave);
  }

  async buscarDireitoFamilia(palavraChave) {
    return this.buscarPorArea('familia', palavraChave);
  }

  async buscarDireitoConsumidor(palavraChave) {
    return this.buscarPorArea('consumidor', palavraChave);
  }

  // ====== CNJ - CONSELHO NACIONAL DE JUSTIÇA ======

  async buscarDataJud(numeroProcesso) {
    try {
      const response = await axios.get(`${this.apis.cnj}/datajud`, {
        params: {
          processo: numeroProcesso
        },
        timeout: this.timeout
      });
      return response.data;
    } catch (error) {
      console.error('Erro DataJud:', error.message);
      return null;
    }
  }

  // ====== TRF4 - TRIBUNAL REGIONAL FEDERAL ======

  async buscarAcordaoTRF4(palavraChave, pagina = 1) {
    try {
      const response = await axios.get(`${this.apis.trf4}/acordaos`, {
        params: {
          q: palavraChave,
          page: pagina,
          limit: 10
        },
        timeout: this.timeout
      });
      return response.data;
    } catch (error) {
      console.error('Erro TRF4:', error.message);
      return null;
    }
  }

  // ====== BUSCA INTEGRADA ======

  async buscarEmTodasAsFontes(palavraChave) {
    return {
      stf: await this.buscarAcordaoSTF(palavraChave),
      stj: await this.buscarAcordaoSTJ(palavraChave),
      trf4: await this.buscarAcordaoTRF4(palavraChave),
      timestamp: new Date().toISOString()
    };
  }

  async buscarPorAreaEmTodasFontes(area, palavraChave) {
    return {
      area: area,
      stj: await this.buscarPorArea(area, palavraChave),
      timestamp: new Date().toISOString()
    };
  }

  // Utility
  limparCache() {
    this.cache = {};
  }
}

module.exports = JurisprudenciaAPI;