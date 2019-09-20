from datetime import datetime

class BaterPonto():
  entrada = []
  saida = []
  
  def marcar_entrada(self, ano, mes, dia):
    # self.entrada.append(datetime.date(data))
    x = datetime.date(ano, mes, dia)
    return x

  def marcar_saida(self, ano, mes, dia):
    # self.saida.append(datetime.date)
    return datetime.date(ano, mes, dia)

  def soma (self, n1):
    return n1 + n1