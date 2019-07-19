#group project
import pandas as pd
from plotly.offline import plot
import plotly.graph_objs as go

df = pd.read_excel("GISdata.xlsx", sheet_name = "cancercases"
                   
cancercases= go.Bar(x= df["CancerType"], y=df["Number"],
                         marker = {"color": df["Number"],"colorscale":"Jet"}
                         )

plot([cancercases])

fig = go.Figure(data=[cancercases])

plot(fig)

titles = go.Layout(title = "Number of Cancer Cases of Women in the U.S",
                   xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text="Cancer Type",
                        )
                           
                    ), 
                   
                    yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text="Percentage",
                           )
                     )
                   )

fig = go.Figure(data=[cancercases], layout = titles)

plot(fig)







