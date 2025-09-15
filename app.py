import streamlit as st 
import pandas as pd
#python -m streamlit run  app.py

#----------------------------------------------sidebar

st.sidebar.image("logo.png")
st.sidebar.title('Evoluçâo de neymar 🧙‍♂️🧪')

neymar = ['Neymar 2012 - 2013',  'Neymar 2014 - 2017', 'Neymar 2018 - 2023', 'Neymar 2023 - 2025']

opcao = st.sidebar.selectbox('Escolha Uma Versão do Neymar', neymar )


#-------------------------------------------------------

st.title('O principe que nao virou rei!!🤴')

st.image(f'{opcao}.png')
st.markdown(f'## Você Escolheu : {opcao}')
st.markdown('---')


# Estatísticas do Neymar (2012 a 2013 - Santos)


if opcao == 'Neymar 2012 - 2013':

    st.markdown("""
# Temporada do Neymar no Santos (2012 a 2013)

| Ano  | Partidas | Gols | Assistências |
|------|----------|------|--------------|
| 2012 | 47       | 42   | 11           |
| 2013 | 23       | 13   | 7            |

---

**Notas:**

- Dados incluem todas as competições oficiais.
- Neymar deixou o Santos no meio de 2013 para se transferir ao Barcelona.
""")
 


elif opcao == 'Neymar 2014 - 2017':



    st.markdown("""
# Estatísticas do Neymar (2014 a 2017 - Barcelona)

| Temporada | Partidas | Gols | Assistências |
|-----------|----------|------|--------------|
| 2014/15   | 51       | 39   | 7            |
| 2015/16   | 49       | 31   | 18           |
| 2016/17   | 45       | 20   | 21           |

---

**Observações:**

- Dados incluem todas as competições (liga, copa, Champions League, etc).
- Neymar teve um papel importante na criação e finalização de jogadas nesse período.
""")

elif opcao == 'Neymar 2018 - 2023':
 st.markdown("""
# Estatísticas do Neymar (2018 a 2023 - Paris Saint-Germain)

| Temporada | Partidas | Gols | Assistências |
|-----------|----------|------|--------------|
| 2018/19   | 28       | 23   | 10           |
| 2019/20   | 27       | 19   | 11           |
| 2020/21   | 31       | 17   | 7            |
| 2021/22   | 28       | 13   | 8            |
| 2022/23   | 29       | 18   | 16           |

---

**Observações:**

- Os dados contemplam todas as competições disputadas pelo PSG.
- Neymar enfrentou algumas lesões, mas manteve uma boa produção em gols e assistências.
""")


elif opcao == 'Neymar 2023 - 2025':
 st.markdown("""
# Estatísticas do Neymar (2023 a 2025)

| Ano         | Clube     | Partidas | Gols | Assistências |
|-------------|-----------|----------|------|--------------|
| 2023–Início 2025 | Al-Hilal  | 7        | 1    | 2            |
| 2025        | Santos    | 16       | 4    | 3            |
 ---

 **Observações:**

 - Neymar sofreu uma lesão grave no período no Al-Hilal, o que limitou seu número de jogos.
 - Em 2025, retornou ao Santos, onde já apresentou bons números.
 """)


























# -------------------------------------------------------- principal






    