import re

part1 = """POCO (Texto)	POZO	-
CATASTRO (Numérico)	CATASTRO	-
OPERADOR (Texto)	OPERADOR	empresa_operadora
POCO_OPERADOR (Texto)	POZO_OPERADOR	-
ESTADO (Texto)	ESTADO	unidad_federativa
BACIA (Texto)	CUENCA	cuenca_sedimentaria
BLOCO (Texto)	BLOQUE	bloque_concesion
SIG_CAMPO (Texto)	SIGLAS_CAMPO	-
CAMPO (Texto)	CAMPO	nombre_campo
TERRA_MAR (Texto)	TIERRA_MAR	ambiente_ubicacion
POCO_POS_ANP (Texto)	POZO_POSICIÓN_ANP	posicion_oficial_anp
TIPO (Texto)	TIPO	Tipo
CATEGORÍA (Texto)	CATEGORÍA	clasif_pozo
RECLASIFICACAO (Texto)	RECLASIFICACIÓN	subclasif_pozo
TITULARIDADE (Texto)	TITULARIDAD	titular_derechos
SITUAÇÃO (Texto)	SITUACIÓN	Status
INICIO (Fecha)	INICIO	Fecha_Inicio
TERMINO (Fecha)	TÉRMINO	Fecha_Término
CONCLUSÃO (Fecha)	CONCLUSIÓN	Fecha_Concl
LATITUD_BASE_4C (Numérico)	LATITUD_BASE_4C	lat_base_4dec
LONGITUD_BASE_4C (Numérico)	LONGITUD_BASE_4C	lon_base_4dec
LATITUD_BASE_DD (Numérico)	LATITUD_BASE_GD	lat_base_gd
LONGITUD_BASE_DD (Numérico)	LONGITUD_BASE_GD	lon_base_gd
TIPO DE COORDENADA BASE (Texto)	TIPO DE COORDENADA BASE	sistema_coord_base
DIRECÃO (Texto)	DIRECCIÓN	trayectoria_perf
PROFUNDIDADE_VERTICAL_M (Numérico)	PROFUNDIDAD_VERTICAL_M	tvd_m
PROFUNDIDADE_SONDADOR_M (Numérico)	PROFUNDIDAD_SONDADORA_M	prof_sonda_m
PROFUNDIDADE_MEDIDA_M (Numérico)	PROFUNDIDAD_MEDIDA_M	md_m
REFERENCIA_DE_PROFUNDIDADE (Texto)	REFERENCIA_DE_PROFUNDIDAD	punto_ref_prof
MESA ROTATIVA (Numérico)	MESA ROTATORIA	elev_mesa_rot
COTA_ALTIMETRICA_M (Numérico)	COTA_ALTIMÉTRICA_M	altitud_pozo_m
LÁMINA DE ÁGUA M (Numérico)	LÁMINA DE AGUA M	col_agua_m
UNIDADE ESTRATIGRÁFICA (Texto)	UNIDAD ESTRATIGRÁFICA	-
GEOLOGÍA_GRUPO_FINAL (Texto)	GEOLOGÍA_GRUPO_FINAL	grupo_geol_final
GEOLOGÍA_FORMACIÓN_FINAL (Texto)	GEOLOGÍA_FORMACIÓN_FINAL	formacion_geol_final
GEOLOGÍA_MEMBRO_FINAL (Texto)	GEOLOGÍA_MIEMBRO_FINAL	miembro_geol_final
CDPE (Texto)	CDPE	-
AGP (Texto)	AGP	-
PC (Texto)	PC	-
PAG (Texto)	PAG	-
PERFIS_CONVENCIONAIS (Texto)	PERFILES_CONVENCIONALES	-
DURANTE_PERFURACAO (Texto)	DURANTE_PERFORACIÓN	-
PERFIS_DIGITAIS (Texto)	PERFILES_DIGITALES	-
PERFIS_PROCESSADOS (Texto)	PERFILES_PROCESADOS	-
PERFIS_ESPECIAIS (Texto)	PERFILES_ESPECIALES	-
AMOSTRA_LATERAL (Texto)	MUESTRA_LATERAL	-
SÍSMICA (Texto)	SÍSMICA	-
TABELA_TEMPO_PROFUNDIDADE (Texto)	TABLA_TIEMPO_PROFUNDIDAD	-
DADOS_DIRECIONAIS (Texto)	DATOS_DIRECIONALES	-
PRUEBA_A_CABO (Texto)	PRUEBA_A_CABLE	-
PRUEBA DE FORMACÃO (Texto)	PRUEBA DE FORMACIÓN	-
CANHONEIO (Texto)	CAÑONEO	-
TESTEMUNHO (Texto)	TESTIGO (CORE)	-
GEOQUÍMICA (Texto)	GEOQUÍMICA	-
SIG_SONDA (Texto)	SIGLAS_SONDA	-
NOM_SONDA (Texto)	NOMBRE_SONDA	-"""

part2 = """Identificador único del pozo.	Cualitativa	Nominal	D={x ∣ x ∈ Etiquetas alfanuméricas de identificación de pozos}
Código de registro catastral oficial.	Cualitativa	Nominal	D={x ∣ x ∈ Código único de registro catastral}
Nombre de la empresa operadora.	Cualitativa	Nominal	D={x ∣ x ∈ Nombres de Compañías}
Código de identificación interna del pozo.	Cualitativa	Nominal	D={x | x ∈ Códigos alfanuméricos de operador}
Unidad federativa de Brasil (Estado).	Cualitativa	Nominal	D={x | x ∈ Códigos de Estados de Brasil}
Cuenca sedimentaria de ubicación.	Cualitativa	Nominal	D={x | x ∈ Nombres de Cuencas}
Bloque de concesión de exploración.	Cualitativa	Nominal	D={x ∣ x ∈ Códigos de Bloque}
Siglas o código del campo de producción.	Cualitativa	Nominal	D={x ∣ x ∈ Siglas de Campo}
Nombre completo del campo de producción.	Cualitativa	Nominal	D={x ∣ x ∈ Nombres de Campo}
Indica si el pozo es Tierra (T) o Mar (M).	Cualitativa	Nominal	D={'T', 'M'}
Clasificación oficial de la posición del pozo según la ANP.	Cualitativa	Nominal	D={'S', 'N'}
Clasificación funcional (Ej. Exploración, Producción, Inyección).	Cualitativa	Nominal	D={'Exploratório', 'Explotatório'}
Clasificación o estatus general del pozo.	Cualitativa	Ordinal	D={x | x ∈ Categorias de los Pozos en Brasil}
Detalle o nueva clasificación del pozo, si aplica.	Cualitativa	Ordinal	D={x ∣ x ∈ Clasificaciones Secundarias}
Entidad o empresa que posee los derechos.	Cualitativa	Nominal	D={x ∣ x ∈ Propietarios de los derechos}
Estado actual (Ej. Activo, Abandonado, Suspendido).	Cualitativa	Ordinal	D={x ∣ x ∈ Estados de Operación}
Comienzo de la perforación.	Cualitativa	Ordinal (Fecha)	D={x | x ∈ Fecha ∧ x ∈ DD/MM/AAAA}
Finalización de la perforación.	Cualitativa	Ordinal (Fecha)	D={x | x ∈ Fecha ∧ x ∈ DD/MM/AAAA}
Entrega del reporte final.	Cualitativa	Ordinal (Fecha)	D={x | x ∈ Fecha ∧ x ∈ DD/MM/AAAA}
Latitud de la base (en 4 decimales).	Cuantitativa	Continua	D={x | x ∈ ℝ ∧ −90 ≤ x ≤ 90}
Longitud de la base (en 4 decimales).	Cuantitativa	Continua	D={x | x ∈ ℝ ∧ −180 ≤ x ≤ 180}
Latitud de la base (en grados decimales).	Cuantitativa	Continua	D={x | x ∈ ℝ ∧ −90 ≤ x ≤ 90}
Longitud de la base (en grados decimales).	Cuantitativa	Continua	D={x | x ∈ ℝ ∧ −180 ≤ x ≤ 180}
Tipo de sistema de coordenadas base utilizado.	Cualitativa	Nominal	D={'Definitiva', 'Provisória'}
Trayectoria de la Perforacción (Vertical, Direccional, Horizontal).	Cualitativa	Nominal	D={'Vertical', 'Direcional', 'Horizontal'}
Profundidad vertical verdadera (TVD).	Cuantitativa	Continua	D={x | x ∈ ℝ}
Profundidad registrada por la herramienta de sondeo.	Cuantitativa	Continua	D={x | x ∈ ℝ ∧ x ≥ 0}
Profundidad total medida (MD).	Cuantitativa	Continua	D={x | x ∈ ℝ ∧ x ≥ 0}
Punto de referencia para las mediciones de profundidad.	Cualitativa	Nominal	D={'MR'}
Elevación de la mesa rotatoria.	Cuantitativa	Continua	D={x | x ∈ ℝ ∧ x ≥ 0}
Altitud o elevación del pozo.	Cuantitativa	Continua	D={x | x ∈ ℝ ∧ x ≥ 0}
Profundidad del agua (solo pozos marinos).	Cuantitativa	Continua	D={x | x ∈ ℝ ∧ x ≥ 0}
Unidad geológica principal alcanzada.	Cualitativa	Nominal	D={x | x ∈ Nombres de Unidades Geológicas}
Clasificación geológica: Grupo al final del pozo.	Cualitativa	Nominal	D={x | x ∈ Nombres de Grupos Geológicos}
Clasificación geológica: Formación al final del pozo.	Cualitativa	Nominal	D={x | x ∈ Nombres de Formaciones Geológicas}
Clasificación geológica: Miembro al final del pozo.	Cualitativa	Nominal	D={x | x ∈ Nombres de Miembros Geológicos}
Disponibilidad de Registros de Cable (Wireline Logs).	Cualitativa	Nominal	D={"Existe","No registra"}
Disponibilidad de datos de Perforación a Presión.	Cualitativa	Nominal	D={"Existe","No registra"}
Disponibilidad de Perfil de Caliper u otro perfil.	Cualitativa	Nominal	D={"Existe","No registra"}
Disponibilidad de Perfil de Densidad y Gaseosa.	Cualitativa	Nominal	D={"Existe","No registra"}
Disponibilidad de registros geofísicos convencionales.	Cualitativa	Nominal	D={"Existe","No registra"}
Disponibilidad de datos durante la perforación (LWD/MWD).	Cualitativa	Nominal	D={"Existe","No registra"}
Disponibilidad de registros en formato digital.	Cualitativa	Nominal	D={"Existe","No registra"}
Disponibilidad de registros procesados.	Cualitativa	Nominal	D={"Existe","No registra"}
Disponibilidad de registros geofísicos especiales.	Cualitativa	Nominal	D={"Existe","No registra"}
Disponibilidad de muestras de pared (Side-wall Cores).	Cualitativa	Nominal	D={"Existe","No registra"}
Disponibilidad de datos sísmicos asociados.	Cualitativa	Nominal	D={"Existe","No registra"}
Disponibilidad de la tabla de conversión tiempo-profundidad.	Cualitativa	Nominal	D={"Existe","No registra"}
Disponibilidad de encuestas de pozo.	Cualitativa	Nominal	D={"Existe","No registra"}
Disponibilidad de pruebas de formación de cable.	Cualitativa	Nominal	D={"Existe","No registra"}
Disponibilidad de pruebas de integridad o producción.	Cualitativa	Nominal	D={"Existe","No registra"}
Disponibilidad de registros o acciones de cañoneo.	Cualitativa	Nominal	D={"Existe","No registra"}
Disponibilidad de muestras de roca (cores).	Cualitativa	Nominal	D={"Existe","No registra"}
Disponibilidad de análisis geoquímicos.	Cualitativa	Nominal	D={"Existe","No registra"}
Siglas o código de la sonda/equipo de perforación.	Cualitativa	Nominal	D={x | x ∈ Códigos de Sonda}
Nombre del equipo de perforación.	Cualitativa	Nominal	D={x | x ∈ Nombres de Sonda}"""

part3 = """R={x | x ∈ IDs únicos de cada pozo del dataset}	Reporte ANP	-	Nominal	No
X={x ∣ x ∈ Código único de registro catastral ∧ x está en el dataset}	Reporte ANP	-	Nominal	No
R={x ∣ x ∈ Nombres de Compañías ∧ x está en el dataset }	Reporte ANP	-	Nominal	Si
R={x | x ∈ Códigos alfanuméricos de operador ∧ x está en el dataset}	Reporte Interno	-	Nominal	No
R={x | x ∈ Códigos de Estados de Brasil ∧ x está en el dataset}	Georreferencia	-	Nominal	Si
R={x | x ∈ Nombres de Cuencas ∧ x está en el dataset}	Geología	-	Nominal	Si
R={x ∣ x ∈ Códigos de Bloque ∧ x está en el dataset}	Contrato ANP	-	Nominal	Si
D={x ∣ x ∈ Siglas de Campo ∧ x está en el dataset}	Reporte ANP	-	Nominal	No
R={x ∣ x ∈ Nombres de Campo ∧ x está en el dataset}	Reporte ANP	-	Nominal	Si
R={'T', 'M'}	Observación	-	Nominal	Si
R={'S', 'N'}	Clasif. ANP	-	Nominal	Si
R={'Exploratório', 'Explotatório'}	Clasif. ANP	-	Nominal	Si
R={'Pioneiro', 'Pioneiro Adjacente', 'Extensão', 'Desenvolvimento', 'Estratigráfico', 'Injeção', 'Especial', 'Jazida Mais Profunda', 'Jazida Mais Rasa'}	Clasif. ANP	-	Ordinal	Si
R={x ∣ x ∈ Clasificaciones Secundarias ∧ x está en el dataset}	Clasif. ANP	-	Ordinal	Si
R={'Público', 'Confidencial'}	Contrato ANP	-	Nominal	Si
R={x ∣ x ∈ Estados de Operación ∧ x está en el dataset}	Reporte Operacional	-	Ordinal	Si
R={x | x ∈ Fecha ∧ x está en el dataset}	Diario Perforación	Fecha	Intervalo	Si
R={x | x ∈ Fecha ∧ x está en el dataset}	Diario Perforación	Fecha	Intervalo	Si
R={x | x ∈ Fecha ∧ x está en el dataset}	Reporte Final	Fecha	Intervalo	Si
R={x ∈ ℝ | −32.9266 ≤ x ≤ 4.5280}	GPS/Topografía	Grados (∘)	Intervalo	Si
R={x ∈ ℝ | −73.3768 ≤ x ≤ −34.8262}	GPS/Topografía	Grados (∘)	Intervalo	Si
R={x ∈ ℝ | −32.9266 ≤ x ≤ 4.5280}	GPS/Topografía	Grados (∘)	Intervalo	Si
R={x ∈ ℝ | −73.3768 ≤ x ≤ −34.8262}	GPS/Topografía	Grados (∘)	Intervalo	Si
R={'Definitiva', 'Provisória'}	Reporte ANP	-	Nominal	Si
R={'Vertical', 'Direcional', 'Horizontal'}	Ingeniería	-	Nominal	Si
R={x ∈ ℝ | 0 ≤ x ≤ 31880}	Sonda (MWD/LWD)	Metros (m)	Intervalo	Si
R={x ∈ ℝ | 0 ≤ x ≤ 8080.2}	Sonda	Metros (m)	Intervalo	Si
R={x ∈ ℝ | 0 ≤ x ≤ 8080.2}	Sonda (TVD/MD)	Metros (m)	Intervalo	Si
R={'MR'}	Topografía	Ninguna	Nominal	Si
R={x ∈ ℝ | 0 ≤ x ≤ 1600}	Topografía	Metros (m)	Intervalo	Si
R={x ∈ ℝ | 0 ≤ x ≤ 6672}	Topografía	Metros (m)	Intervalo	Si
R={x ∈ ℝ | 0 ≤ x ≤ 2988}	Sonda	Metros (m)	Intervalo	Si
R={x | x ∈ Nombres de Unidades Geológicas ∧ x está en el dataset}	Geología	-	Nominal	No
R={x | x ∈ Nombres de Grupos Geológicos ∧ x está en el dataset}	Geología	-	Nominal	Si
R={x | x ∈ Nombres de Formaciones Geológicas ∧ x está en el dataset}	Geología	-	Nominal	Si
R={x | x ∈ Nombres de Miembros Geológicos ∧ x está en el dataset}	Geología	-	Nominal	Si
R={"Existe","No registra"}	Reporte Técnico	-	Nominal	No
R={"Existe","No registra"}	Reporte Técnico	-	Nominal	No
R={"Existe","No registra"}	Reporte Técnico	-	Nominal	No
R={"Existe","No registra"}	Reporte Técnico	-	Nominal	No
R={"Existe","No registra"}	Reporte Técnico	-	Nominal	No
R={"Existe","No registra"}	Reporte Técnico	-	Nominal	No
R={"Existe","No registra"}	Reporte Técnico	-	Nominal	No
R={"Existe","No registra"}	Reporte Técnico	-	Nominal	No
R={"Existe","No registra"}	Reporte Técnico	-	Nominal	No
R={"Existe","No registra"}	Reporte Técnico	-	Nominal	No
R={"Existe","No registra"}	Reporte Técnico	-	Nominal	No
R={"Existe","No registra"}	Reporte Técnico	-	Nominal	No
R={"Existe","No registra"}	Reporte Técnico	-	Nominal	No
R={"Existe","No registra"}	Reporte Técnico	-	Nominal	No
R={"Existe","No registra"}	Reporte Técnico	-	Nominal	No
R={"Existe","No registra"}	Reporte Técnico	-	Nominal	No
R={"Existe","No registra"}	Reporte Técnico	-	Nominal	No
R={"Existe","No registra"}	Reporte Técnico	-	Nominal	No
R={x | x ∈ Códigos de Sonda}	Reporte Operacional	-	Nominal	No
R={x | x ∈ Nombres de Sonda}	Reporte Operacional	-	Nominal	No"""

def parse_lines(text):
    res = []
    for line in text.strip().split('\n'):
        parts = line.split('\t')
        res.append([p.strip() for p in parts])
    return res

l1 = parse_lines(part1)
l2 = parse_lines(part2)
l3 = parse_lines(part3)

tbody = []
for r1, r2, r3 in zip(l1, l2, l3):
    row = "    <tr>\n"
    row += f"      <td>{r1[0]}</td>\n"
    row += f"      <td>{r1[1]}</td>\n"
    row += f"      <td>{r1[2]}</td>\n"

    # IDENTIFICADOR PEOR TOCAR 
    row += f"      <td>{r2[0]}</td>\n"
    badge_class = "cualitativa" if "cualitativa" in r2[1].lower() else "cuantitativa"
    row += f"      <td><span class='badge {badge_class}'>{r2[1]}</span></td>\n"
    row += f"      <td>{r2[2]}</td>\n"
    row += f"      <td class='formula-celda'>{r2[3]}</td>\n"
    
    row += f"      <td class='formula-celda'>{r3[0]}</td>\n"
    row += f"      <td>{r3[1]}</td>\n"
    row += f"      <td>{r3[2]}</td>\n"
    row += f"      <td>{r3[3]}</td>\n"
    row += f"      <td>{r3[4]}</td>\n"
    row += "    </tr>"
    tbody.append(row)

new_tbody = "\n".join(tbody)

html_file = r"c:\Users\HP\Desktop\anahi4\index.html"
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

import re
pattern = r'(<table class="tabla-datos" id="miTabla">\s*<thead>.*?</thead>\s*<tbody>).*?(</tbody>)'
new_content = re.sub(pattern, r'\\1\n' + new_tbody.replace('\\', '\\\\') + r'\n\\2', content, flags=re.DOTALL)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated table successfully.")
