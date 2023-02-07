from create_faker_data import create_data
from convert_data_csv import convert_data_to_csv
from create_graph import create_graph


all_data = create_data(20)
convert_data_to_csv(all_data)
create_graph()
