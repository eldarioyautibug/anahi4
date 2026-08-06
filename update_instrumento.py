import re
import sys

html_file = r"c:\Users\HP\Desktop\anahi4\index.html"
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

original_lines = len(content.splitlines())

old_planteamiento = """              <p>
                Este proyecto analiza datos estadísticos de pozos petroleros en Brasil para superar
                promedios simples y comprender su comportamiento real mediante un enfoque técnico-académico.
              </p>"""
new_planteamiento = """              <p>
                La exploración de petróleo y gas es importante para el desarrollo económico de cualquier país, mediante la estadística podemos obtener información útil, relacionada con la exploración y producción de petróleo y gas. Como caso de estudio tomamos Brasil con datos descargados desde Kaggle.
              </p>"""
content = content.replace(old_planteamiento, new_planteamiento)

updates = {
    'POCO (Texto)': ('Reporte ANP', '-'),
    'CATASTRO (Numérico)': ('Reporte ANP', '-'),
    'OPERADOR (Texto)': ('Reporte ANP', '-'),
    'POCO_OPERADOR (Texto)': ('Reporte Interno', '-'),
    'ESTADO (Texto)': ('Georreferencia', '-'),
    'BACIA (Texto)': ('Geología', '-'),
    'BLOCO (Texto)': ('Contrato ANP', '-'),
    'SIG_CAMPO (Texto)': ('Reporte ANP', '-'),
    'CAMPO (Texto)': ('Reporte ANP', '-'),
    'TERRA_MAR (Texto)': ('Observación', '-'),
    'POCO_POS_ANP (Texto)': ('Clasif. ANP', '-'),
    'TIPO (Texto)': ('Clasif. ANP', '-'),
    'CATEGORÍA (Texto)': ('Clasif. ANP', '-'),
    'RECLASIFICACAO (Texto)': ('Clasif. ANP', '-'),
    'TITULARIDADE (Texto)': ('Contrato ANP', '-'),
    'SITUAÇÃO (Texto)': ('Reporte Operacional', '-'),
    'INICIO (Fecha)': ('Diario Perforación', 'Fecha'),
    'TERMINO (Fecha)': ('Diario Perforación', 'Fecha'),
    'CONCLUSÃO (Fecha)': ('Reporte Final', 'Fecha'),
    'LATITUD_BASE_4C (Numérico)': ('GPS/Topografía', 'Grados (°)'),
    'LONGITUD_BASE_4C (Numérico)': ('GPS/Topografía', 'Grados (°)'),
    'LATITUD_BASE_DD (Numérico)': ('GPS/Topografía', 'Grados (°)'),
    'LONGITUD_BASE_DD (Numérico)': ('GPS/Topografía', 'Grados (°)'),
    'DATO_HORIZONTAL (Texto)': ('Georreferencia', '-'),
    'TIPO DE COORDENADA BASE (Texto)': ('Reporte ANP', '-'),
    'DIRECÃO (Texto)': ('Ingeniería', '-'),
    'PROFUNDIDADE_VERTICAL_M (Numérico)': ('Sonda (MWD/LWD)', 'Metros (m)'),
    'PROFUNDIDADE_SONDADOR_M (Numérico)': ('Sonda', 'Metros (m)'),
    'PROFUNDIDADE_MEDIDA_M (Numérico)': ('Sonda (TVD/MD)', 'Metros (m)'),
    'REFERENCIA_DE_PROFUNDIDADE (Texto)': ('Topografía', 'Ninguna'),
    'MESA ROTATIVA (Numérico)': ('Topografía', 'Metros (m)'),
    'COTA_ALTIMETRICA_M (Numérico)': ('Topografía', 'Metros (m)'),
    'LÁMINA DE ÁGUA M (Numérico)': ('Sonda', 'Metros (m)'),
    'DATO_VERTICAL (Texto)': ('Georreferencia', '-'),
    'UNIDADE ESTRATIGRÁFICA (Texto)': ('Geología', '-'),
    'GEOLOGÍA_GRUPO_FINAL (Texto)': ('Geología', '-'),
    'GEOLOGÍA_FORMACIÓN_FINAL (Texto)': ('Geología', '-'),
    'GEOLOGÍA_MEMBRO_FINAL (Texto)': ('Geología', '-'),
    'CDPE (Texto)': ('Reporte Técnico', '-'),
    'AGP (Texto)': ('Reporte Técnico', '-'),
    'PC (Texto)': ('Reporte Técnico', '-'),
    'PAG (Texto)': ('Reporte Técnico', '-'),
    'PERFIS_CONVENCIONAIS (Texto)': ('Reporte Técnico', '-'),
    'DURANTE_PERFURACAO (Texto)': ('Reporte Técnico', '-'),
    'PERFIS_DIGITAIS (Texto)': ('Reporte Técnico', '-'),
    'PERFIS_PROCESSADOS (Texto)': ('Reporte Técnico', '-'),
    'PERFIS_ESPECIAIS (Texto)': ('Reporte Técnico', '-'),
    'AMOSTRA_LATERAL (Texto)': ('Reporte Técnico', '-'),
    'SÍSMICA (Texto)': ('Reporte Técnico', '-'),
    'TABELA_TEMPO_PROFUNDIDADE (Texto)': ('Reporte Técnico', '-'),
    'DADOS_DIRECIONAIS (Texto)': ('Reporte Técnico', '-'),
    'PRUEBA_A_CABO (Texto)': ('Reporte Técnico', '-'),
    'PRUEBA DE FORMACÃO (Texto)': ('Reporte Técnico', '-'),
    'CANHONEIO (Texto)': ('Reporte Técnico', '-'),
    'TESTEMUNHO (Texto)': ('Reporte Técnico', '-'),
    'GEOQUÍMICA (Texto)': ('Reporte Técnico', '-'),
    'SIG_SONDA (Texto)': ('Reporte Operacional', '-'),
    'NOM_SONDA (Texto)': ('Reporte Operacional', '-'),
    'DHA_ATUALIZAÇÃO (Fecha)': ('Registro de Sistema', 'Fecha')
}

def replace_instrumento(match):
    row_content = match.group(0)
    td_match = re.search(r'<td>(.*?)</td>', row_content)
    if td_match:
        var_name = td_match.group(1).strip()
        if var_name in updates:
            instr, unidad = updates[var_name]
            tds = re.findall(r'<td.*?>.*?</td>', row_content, flags=re.DOTALL)
            if len(tds) >= 10:
                new_td8 = f'<td>{instr}</td>'
                new_td9 = f'<td>{unidad}</td>'
                row_content = row_content.replace(tds[8], new_td8)
                row_content = row_content.replace(tds[9], new_td9)
    return row_content

content = re.sub(r'(<tr>(?:(?!<tr>).)*?</tr>)', replace_instrumento, content, flags=re.DOTALL)

new_lines = len(content.splitlines())
if abs(original_lines - new_lines) > 20:
    print(f"Error: Line count changed drastically from {original_lines} to {new_lines}!")
    sys.exit(1)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Success! Lines: {new_lines}")
