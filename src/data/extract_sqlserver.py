import os
import pandas as pd
import sqlalchemy as sa
from dotenv import load_dotenv

# ---------------------------------------------------
#  Load environment variables
# ---------------------------------------------------
load_dotenv()

DB_SERVER   = os.getenv("DB_SERVER")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USER     = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DRIVER   = os.getenv("DB_DRIVER", "ODBC Driver 17 for SQL Server")

# ---------------------------------------------------
#  SQLAlchemy connection string (best practice)
# ---------------------------------------------------
connection_string = (
    f"mssql+pyodbc://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_SERVER}/{DB_DATABASE}"
    f"?driver={DB_DRIVER.replace(' ', '+')}"
)

engine = sa.create_engine(connection_string)

# ---------------------------------------------------
# Extract Function
# ---------------------------------------------------
def extract_operacional(output_path="../database/raw/acompanhamento_operacional.csv"):
    """
    Extrai os dados operacionais da tabela principal da Zenatur
    e salva em CSV na pasta database/raw.
    """

    query = """
        SELECT grpd.*, grao.*
          FROM DB_PWBI.dbo.DB_ZT_GERAL_PEDIDOS as grpd WITH(NOLOCK)
          INNER JOIN DB_PWBI.dbo.DB_ZT_GERAL_ACOMPANHAMENTO_OPERACIONAL as grao WITH(NOLOCK) ON grao.ss = grpd.ss;
    """

    print("Conectando ao SQL Server...")
    with engine.connect() as connection:
        df = pd.read_sql(query, connection)

    print(f"Registros extraídos: {len(df):,}")
    print(f"Salvando em: {output_path}")

    # Criar diretório se não existir
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    df.to_csv(output_path, index=False, encoding="utf-8-sig")
    
    df_csv = pd.read_csv(output_path)

    print("Extração concluída com sucesso!")

    return df_csv