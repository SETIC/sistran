jQuery(function($){
     $("#id_cpf_cnpj").mask("999.999.999-99");
     $("#id_placa").mask("aaa-9999");
     $("#id_contato").mask("(99)9999-9999?9");
     $("#id_cep").mask("99999-999");
});
var jets = new Jets({
    searchTag: '#jetsSearch',
    contentTag: '#jetsContent'
});
var jetsSearch = new Jets({
  searchTag: '#jetsTableSearch',
  contentTag: '#jetsTableContent',
});
$(document).ready(function() {
  $("#id_logradouro").select2();
  $("#id_bairro").select2();
  $("#id_municipio").select2();
  $("#id_estado").select2();
  $("#id_marca").select2();
});