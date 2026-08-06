import re

html_file = r"c:\Users\HP\Desktop\anahi4\index.html"
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(
    r'<title>.*?</title>', 
    r'<title>Análisis estadístico de Exploración y Producción de petróleo y Gas en Brasil</title>', 
    content
)
content = re.sub(
    r'<h1>Producción y Exploración de petróleo y gas en Brasil</h1>', 
    r'<h1>Análisis estadístico de Exploración y Producción de petróleo y Gas en Brasil</h1>', 
    content
)

# NO TOCAR ESTA MRD CABRONES
content = re.sub(
    r'(<td>ESTADO \(Texto\)</td>.*?<a href=")https://rpubs.com/CalebY12/1435216(" target="_blank">Ver en Rpubs</a></td>)',
    r'\g<1>https://rpubs.com/CalebY12/1449913\g<2>',
    content
)

content = re.sub(
    r'(<td>TITULARIDADE \(Texto\)</td>.*?<a href=")https://rpubs.com/CalebY12/1407974(" target="_blank">Ver en Rpubs</a></td>)',
    r'\g<1>https://rpubs.com/CalebY12/1449924\g<2>',
    content
)

rango_updates = {
    'POCO (Texto)': r'R={x | x ∈ IDs únicos de cada pozo del dataset}',
    'CATASTRO (Numérico)': r'R={x ∈ ℤ⁺ | 8,115,018,892 ≤ x ≤ 901,210,398,600}',
    'OPERADOR (Texto)': r'R={x ∣ x ∈ Nombres de Compañías, x está en el dataset }',
    'POCO_OPERADOR (Texto)': r'R={x | x ∈ Códigos alfanuméricos de operador, x está en el dataset}',
    'ESTADO (Texto)': r'R={x | x ∈ Códigos de Estados de Brasil, x está en el dataset}',
    'BACIA (Texto)': r'R={x | x ∈ Nombres de Cuencas, x está en el dataset}',
    'BLOCO (Texto)': r'R={x ∣ x ∈ Códigos de Bloque, x está en el dataset}',
    'SIG_CAMPO (Texto)': r'D={x ∣ x ∈ Siglas de Campo, x está en el dataset}',
    'CAMPO (Texto)': r'R={x ∣ x ∈ Nombres de Campo, x está en el dataset}',
    'TERRA_MAR (Texto)': r"R={'T', 'M'}",
    'POCO_POS_ANP (Texto)': r"R={'S', 'N'}",
    'TIPO (Texto)': r"R={'Exploratório', 'Explotatório'}",
    'CATEGORÍA (Texto)': r"R={'Pioneiro', 'Pioneiro Adjacente', 'Extensão', 'Desenvolvimento', 'Estratigráfico', 'Injeção', 'Especial', 'Jazida Mais Profunda', 'Jazida Mais Rasa'}",
    'RECLASIFICACAO (Texto)': r'R={x ∣ x ∈ Clasificaciones Secundarias, x está en el dataset}',
    'TITULARIDADE (Texto)': r"R={'Público', 'Confidencial'}",
    'SITUAÇÃO (Texto)': r'R={x ∣ x ∈ Estados de Operación, x está en el dataset}',
    'INICIO (Fecha)': r'R={x | x ∈ Fecha, x está en el dataset}',
    'TERMINO (Fecha)': r'R={x | x ∈ Fecha, x está en el dataset}',
    'CONCLUSÃO (Fecha)': r'R={x | x ∈ Fecha, x está en el dataset}',
    'LATITUD_BASE_4C (Numérico)': r'R={x ∈ ℝ | −32.9266 ≤ x ≤ 4.5280}',
    'LONGITUD_BASE_4C (Numérico)': r'R={x ∈ ℝ | −73.3768 ≤ x ≤ −34.8262}',
    'LATITUD_BASE_DD (Numérico)': r'R={x ∈ ℝ | −32.9266 ≤ x ≤ 4.5280}',
    'LONGITUD_BASE_DD (Numérico)': r'R={x ∈ ℝ | −73.3768 ≤ x ≤ −34.8262}',
    'DATO_HORIZONTAL (Texto)': r'R ⊆ D',
    'TIPO DE COORDENADA BASE (Texto)': r'R ⊆ D',
    'DIRECÃO (Texto)': r"R={'Vertical', 'Direcional', 'Horizontal'}",
    'PROFUNDIDADE_VERTICAL_M (Numérico)': r'R={x ∈ ℝ | −7,148 ≤ x ≤ 31880}',
    'PROFUNDIDADE_SONDADOR_M (Numérico)': r'R={x ∈ ℝ | 0 ≤ x ≤ 8080.2}',
    'PROFUNDIDADE_MEDIDA_M (Numérico)': r'R={x ∈ ℝ | 0 ≤ x ≤ 8080.2}',
    'REFERENCIA_DE_PROFUNDIDADE (Texto)': r"R={'MR'}",
    'MESA ROTATIVA (Numérico)': r'R={x ∈ ℝ | 0 ≤ x ≤ 1600}',
    'COTA_ALTIMETRICA_M (Numérico)': r'R={x ∈ ℝ | 0 ≤ x ≤ 6672}',
    'LÁMINA DE ÁGUA M (Numérico)': r'R={x ∈ ℝ | 0 ≤ x ≤ 2988}',
    'DATO_VERTICAL (Texto)': r"R={'NM'}",
    'UNIDADE ESTRATIGRÁFICA (Texto)': r'R={x | x ∈ Nombres de Unidades Geológicas, x está en el dataset}',
    'GEOLOGÍA_GRUPO_FINAL (Texto)': r'R={x | x ∈ Nombres de Grupos Geológicos, x está en el dataset}',
    'GEOLOGÍA_FORMACIÓN_FINAL (Texto)': r'R={x | x ∈ Nombres de Formaciones Geológicas, x está en el dataset}',
    'GEOLOGÍA_MEMBRO_FINAL (Texto)': r'R={x | x ∈ Nombres de Miembros Geológicos, x está en el dataset}',
    'CDPE (Texto)': r'R={x | x ∈ Disponibilidad de Registros, x está en el dataset}',
    'AGP (Texto)': r'R={x | x ∈ Disponibilidad de Registros, x está en el dataset}',
    'PC (Texto)': r'R={x | x ∈ Disponibilidad de Registros, x está en el dataset}',
    'PAG (Texto)': r'R={x | x ∈ Disponibilidad de Registros, x está en el dataset}',
    'PERFIS_CONVENCIONAIS (Texto)': r'R={x | x ∈ Disponibilidad de Registros, x está en el dataset}',
    'DURANTE_PERFURACAO (Texto)': r'R={x | x ∈ Disponibilidad de Registros, x está en el dataset}',
    'PERFIS_DIGITAIS (Texto)': r'R={x | x ∈ Disponibilidad de Registros, x está en el dataset}',
    'PERFIS_PROCESSADOS (Texto)': r'R={x | x ∈ Disponibilidad de Registros, x está en el dataset}',
    'PERFIS_ESPECIAIS (Texto)': r'R={x | x ∈ Disponibilidad de Registros, x está en el dataset}',
    'AMOSTRA_LATERAL (Texto)': r'R={x | x ∈ Disponibilidad de Registros, x está en el dataset}',
    'SÍSMICA (Texto)': r'R={x | x ∈ Disponibilidad de Registros, x está en el dataset}',
    'TABELA_TEMPO_PROFUNDIDADE (Texto)': r'R={x | x ∈ Disponibilidad de Registros, x está en el dataset}',
    'DADOS_DIRECIONAIS (Texto)': r'R={x | x ∈ Disponibilidad de Registros, x está en el dataset}',
    'PRUEBA_A_CABO (Texto)': r'R={x | x ∈ Disponibilidad de Registros, x está en el dataset}',
    'PRUEBA DE FORMACÃO (Texto)': r'R={x | x ∈ Disponibilidad de Registros, x está en el dataset}',
    'CANHONEIO (Texto)': r'R={x | x ∈ Disponibilidad de Registros, x está en el dataset}',
    'TESTEMUNHO (Texto)': r'R={x | x ∈ Disponibilidad de Registros, x está en el dataset}',
    'GEOQUÍMICA (Texto)': r'R={x | x ∈ Disponibilidad de Registros, x está en el dataset}',
    'SIG_SONDA (Texto)': r'R={x | x ∈ Códigos de Sonda, x está en el dataset}',
    'NOM_SONDA (Texto)': r'R={x | x ∈ Nombres de Sonda, x está en el dataset}',
    'DHA_ATUALIZAÇÃO (Fecha)': r'R={x ∈ Fecha | x = 28/01/2018}'
}

def replace_rango(match):
    row_content = match.group(0)
    td_match = re.search(r'<td>(.*?)</td>', row_content)
    if td_match:
        var_name = td_match.group(1).strip()
        if var_name in rango_updates:
            new_rango = rango_updates[var_name]
            tds = re.findall(r'<td.*?>.*?</td>', row_content, flags=re.DOTALL)
            if len(tds) >= 8:
                new_td8 = f'<td class="formula-celda">{new_rango}</td>'
                row_content = row_content.replace(tds[7], new_td8)
    return row_content

new_content = re.sub(r'<tr>.*?</tr>', replace_rango, content, flags=re.DOTALL)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("HTML updated successfully.")
