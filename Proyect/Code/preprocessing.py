import pandas as pd
data_path="D:/Documents/Jupyter Notebooks/TimeSeries/Proyect/Dataset/"
Delayed_flights=pd.read_csv(data_path+"DelayedFlights.csv")
Delayed_flights=Delayed_flights.drop("Unnamed: 0", axis="columns")
display(Delayed_flights)
