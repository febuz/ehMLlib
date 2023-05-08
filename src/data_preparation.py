import pandas as pd
import cbsodata

# Downloading table list
toc = pd.DataFrame(cbsodata.get_table_list())