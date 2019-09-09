# itriad

### rode o ambiente virtual no Ubuntu:

```shell
source venv/bin/activate
```
### rode o projeto:

```shell
python3 main.py
```
## Tecnologias

##### 1. [Python3](https://docs.python.org/3.3/)
##### 2. [PyQt5](https://pypi.org/project/PyQt5/)
##### 3. [Sqlite3](https://www.sqlite.org/index.html)


## Notas

##### Horário de funcionamento
O sistema funciona considerando que o estacionamento está aberto de 8:00 as 18:00. Então, em registros de entrada e saída de veículos antes das 8:00 ou depois das 18:00 será considerado apenas o tempo que veículo esteve no estacionamento nos horários válidos.

Por exemplo: Um carro entra as 7:00 e sai as 19:00 horas. O sistema considera que ele entrou as 8:00 e saiu as 18:00 horas.

##### Relatório de faturamento
O relatório de funcionamento é calculado considerando o uma data inicial e uma data final, somente os veículos cuja a saída já foi registrada constarão neste calculo. Ou seja, se o veículo aínda está na lista de veículos estacionados ele a conta dele não estará no relatório.

##### Registros de horários
Toda informação relacionada a horário de entrada e saída de veículos é obtida a partir do sistema operacional onde o programa está executando, portanto os horários não são editáveis.

##### Relatório de Faturamento
Em relação ao relatório de faturamento, o que ficou claro é que o cliente deseja obter o faturamento de um determidado período, o sistema calcula o faturamento a partir de um dia inicial até um dia final.

