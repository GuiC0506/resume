import streamlit as st
from pathlib import Path
from PIL import Image

dir_atual = Path.cwd()
curriculo = dir_atual / "files/CV Guilherme China - Jovem aprendiz.pdf"

css_file = dir_atual / "styles" / "style.css"
foto_perfil = dir_atual / "files/pic_oficial.png"

foto = Image.open(foto_perfil)

redes_sociais = {"Linkedin": "https://www.linkedin.com/in/guilherme-china-03b23b268/",
                 "Github": "https://github.com/Chininha"}

projetos = {"Dashboards Gasômetros - Relatório geral por consulta API": "https://metricas-ici2023.streamlit.app/",
            "Medalhista na AIMO (Asia International Olympiad Union) – setembro de 2020":
            "https://drive.google.com/file/d/1xf_I4EZGwY3bCCefmqMHGc6YoH6scmdL/view?usp=share_link",
            "Projeto FEBRACE - Experimento digital para determinação de constantes elástica": "https://drive.google.com/file/d/15CM8rUq5hMO7drQG3dJUm1WCTLBeaiOU/view?usp=share_link"}

cursos = {"Hashtag Treinamentos": "Curso Python Impressionador - em andamento",
          "Curso em Vídeo": "Curso de fundamentos do Python",
          "English Yourself": "Curso de inglês online - 2020"}

hard_skills = {"- 👩‍💻 Programming": "Python (Pandas, Numpy, Streamlit), SQL",
               "- 📊 Data Visulization": "Plotly, Matplotlib, Seaborn",
               "- 🗄️ Databases": "MySQL, Oracle SQL Developer",
               "- :computer: Softwares": "Office 365 package, Oracle SQL Developer Data Modeler"}

with open(curriculo, "rb") as curriculo_pdf:
    arquivo = curriculo_pdf.read()

st.set_page_config(
    page_title="Digital CV | Guilherme China",
    layout="centered"
)

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(foto, width=300)

with col2:
    st.title("Guilherme China")
    st.write("Graduando de Ciência de Dados, auxiliar de escritório focado em manipulação de dados e tomada de decisões")
    st.download_button(label=":memo: Download resume",
                       data=arquivo,
                       file_name=curriculo.name,
                       mime="application/octet-stream")
    st.write("📫 Echina725@gmail.com")
    st.write(":telephone_receiver: (55) 11 94994-0557")
    for indice, (rede, link) in enumerate(redes_sociais.items()):
        st.write(f":computer: [{rede}]({link})")

st.write("#")
st.header(f":orange[Objetivo]")
st.write("""
Buscando uma oportunidade em uma empresa data-driven onde eu possa aplicar meus conhecimentos em análise de dados e contribuir para o sucesso da empresa por meio da identificação de erros, tendências e oportunidades de crescimento
""")


# ------------ REDES SOCIAIS ------------------
colunas_redes = st.columns(len(redes_sociais) + 2, gap="small")
# for indice, (rede, link) in enumerate(redes_sociais.items()):
#     colunas_redes[indice].write(f"| [{rede}]({link})")

# ----------- Qualificações -----------------
st.write("#")
st.subheader(":orange[Experiências & Qualificações]")
st.write("---")
st.write(
    """
- ✔️ Ensino Médio completo - Colégio FAAT
\n- ✔️ Idioma inglês - Avançado
\n- ✔️ Cursando graduação: Data Science - FIAP
\n - ✔️ Realizando curso de Python - Hashtag Treinamentos
\n - ✔️ Realizando curso de MySQL - Alura
""")

# ----------- skills ---------------------------
st.markdown("#")
st.subheader(":orange[Hard Skills]")
st.write("---")

for skill, nome in hard_skills.items():
    st.write(f"{skill} - {nome}")

st.markdown("#")
st.subheader(":orange[Soft Skills]")
st.write("---")
st.write("""
- Pensamento crítico
- Comunicação
- Adaptabilidade
- Proatividade
- Criatividade
- Decision-Making

""")

st.markdown("#")
st.subheader(":orange[Histórico de trabalho]")
st.write("---")
st.write(":office: Constanta Industrial Ltda   | Auxiliar de escritório")
st.write("09/2022 - presente")
st.write("""
- ► Python para realizar buscas na API da operadora NLT com o intuito de gerar relatórios e dashboards que apresentassem a situação dos devices IoT
- ► Excel e Python para organização e limpeza de dados dispostos no sistema
""")

st.markdown("#")
st.subheader(":orange[Cursos]")
st.write("---")
for curso, nome in cursos.items():
    st.write(f"- :pencil2: {curso} - {nome}")

st.markdown("#")
st.subheader(":orange[Projetos]")
st.write("---")
for projeto, link in projetos.items():
    st.write(f"- :trophy: [{projeto}]({link})")
st.write("- :trophy: Data Modeling: Construção de um modelo relacional e implementação de um Banco de Dados para Sistema de Gerenciamento de Vídeos")
