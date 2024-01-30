import sqlalchemy
from sqlalchemy import create_engine, func, inspect, text
import pandas as pd

class SQLHelper():

    def __init__(self):
        self.engine = create_engine("sqlite:///resources/AQI and Lat Long of Countries.sqlite")

    def getMapData(self, Country):
        # allow the user to select ALL country
        if Country == "All":
            where_clause = "1=1"
        else:
            where_clause = f"Country = '{Country}'"

        query = f"""
        SELECT
            *
        FROM
            "AQI and Lat Long of Countries"
        WHERE
            {where_clause};
        """

        df_map = pd.read_sql(text(query), con=self.engine)
        data_map = df_map.to_dict(orient="records")

        return(data_map)
    
    def getMapData(self, City):
        # allow the user to select ALL Cities in a Country
        if City == "All":
            where_clause = "1=1"
        else:
            where_clause = f"City = '{City}'"

        query = f"""
            SELECT
            Country,
             City,
            "AQI Value",
            "AQI Category"
            FROM
                "AQI and Lat Long of Countries"
            WHERE
                {where_clause}
            GROUP BY
                City
                
            ORDER BY
                "AQI Value" asc
                
            LIMIT 10;
        """

        df_map = pd.read_sql(text(query), con=self.engine)
        data_map = df_map.to_dict(orient="records")

        return(data_map)