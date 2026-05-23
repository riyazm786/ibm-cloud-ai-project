import pandas as pd

def create_dataframe(cpu, memory):
    data = {
        "Resource": ["CPU", "Memory"],
        "Usage": [cpu, memory]
    }

    return pd.DataFrame(data)
