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
    
    def getBarData(self, Country):
        # allow the user to select ALL country
        if Country == "All":
            where_clause = "1=1"
        else:
            where_clause = f"Country = '{Country}'"

        query = f"""
            SELECT
                Country,
                City,
                City || ', ' || Country as loc_display,
                Avg("AQI Value") as avg_value
            FROM
                "AQI and Lat Long of Countries"
            WHERE
                {where_clause}
            GROUP BY
                Country,
                City
            ORDER BY
                avg_value desc
            LIMIT 10;
        """

        df_bar = pd.read_sql(text(query), con=self.engine)
        data_bar = df_bar.to_dict(orient="records")

        return(data_bar)
    
    def getPieData(self, Country):
        # allow the user to select ALL country
        if Country == "All":
            where_clause = "1=1"
        else:
            where_clause = f"Country = '{Country}'"

        query = f"""
            SELECT
                avg("CO AQI Value") as value,
                'CO AQI Value' as label
            FROM
                "AQI and Lat Long of Countries"
            WHERE
                {where_clause}    

            UNION ALL

            SELECT
                avg("Ozone AQI Value") as value,
                'Ozone AQI Value' as label
            FROM
                "AQI and Lat Long of Countries"
            WHERE
                {where_clause}     

            UNION ALL

            SELECT
                avg("NO2 AQI Value") as value,
                'NO2 AQI Value' as label
            FROM
                "AQI and Lat Long of Countries"
            WHERE
                {where_clause}    

            UNION ALL

            SELECT
                avg("PM2.5 AQI Value") as value,
                'PM2.5 AQI Value' as label
            FROM
                "AQI and Lat Long of Countries"
            WHERE
                {where_clause}             
        """

        df_pie = pd.read_sql(text(query), con=self.engine)
        data_pie = df_pie.to_dict(orient="records")

        return(data_pie)
    
    def getPieData2(self, Country):
        # allow the user to select ALL country
        if Country == "All":
            where_clause = "1=1"
        else:
            where_clause = f"Country = '{Country}'"

        query = f"""
            SELECT
                "AQI Category" as label,
                count(*) as value
            FROM
                "AQI and Lat Long of Countries"
            WHERE
                {where_clause}
            GROUP BY
                "AQI Category"
        """

        df_pie2 = pd.read_sql(text(query), con=self.engine)
        data_pie2 = df_pie2.to_dict(orient="records")

        return(data_pie2)