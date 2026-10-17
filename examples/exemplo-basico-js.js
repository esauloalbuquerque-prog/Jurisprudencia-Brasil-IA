// exemplo-basico-js.js
const JurisprudenciaAPI = require('../src/jurisprudencia-api');

async function exemploBasico() {
  const api = new JurisprudenciaAPI();

  console.log('=== Exemplo 1: Buscar Acordão STF ===');
  const acordaoSTF = await api.buscarAcordaoSTF('direito do trabalho');
  console.log(JSON.stringify(acordaoSTF, null, 2));

  console.log('\n=== Exemplo 2: Buscar por Área (Direito Civil) ===');
  const direitoCivil = await api.buscarDireitoCivil('responsabilidade civil');
  console.log(JSON.stringify(direitoCivil, null, 2));

  console.log('\n=== Exemplo 3: Listar Ministros STF ===');
  const ministros = await api.listarMinistrosSTF();
  console.log(JSON.stringify(ministros, null, 2));

  console.log('\n=== Exemplo 4: Buscar em Todas as Fontes ===');
  const todasFontes = await api.buscarEmTodasAsFontes('contratos');
  console.log(JSON.stringify(todasFontes, null, 2));
}

exemploBasico().catch(console.error);