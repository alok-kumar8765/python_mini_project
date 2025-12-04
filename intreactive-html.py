# =========================================
# Interactive HTML Table in Browser (Ploty)
# =========================================

import plotly.graph_objects as go

data = dict(
        Name=["Alice","Bob", "Clara"],
        Score=[88,92,85],
        City=["NY","LA","TX"]
        )
table = go.Figure(data=[go.Table( 
        header=dict(values=list(data.keys())), 
        cells=dict(values=list(data.values()))
)])

table.show()
