from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import pandas as pd
import joblib

# Criar uma instância do FastAPI
app = FastAPI()

# Criar uma classe com os dados de entrada do request body com os tipos esperados usando pydantic
# forçar que os dados só sejam processados, conforme a definição feita
class request_body(BaseModel):
    tempo_de_experiencia: int
    numero_de_vendas: int
    fator_sazonal: int 

# Carregar o modelo para realizar a predição
modelo_poly = joblib.load('modelo_receita_vendas.pkl')

# Adicionar decorador
@app.post('/predict')
def predict(data : request_body):
    input_features = {
    'tempo_de_experiencia': data.tempo_de_experiencia,
    'numero_de_vendas': data.numero_de_vendas,
    'fator_sazonal': data.fator_sazonal
    }
    
# Dataframe para fazer a predição 
    pred_df = pd.DataFrame(input_features, index=[1])

# Predição
    y_pred = modelo_poly.predict(pred_df)[0].astype(float)

    return {'receita_em_reais' : y_pred.tolist()}