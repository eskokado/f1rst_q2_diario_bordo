import pandas as pd

csv_file_path = './data/info_transportes.csv'
data = pd.read_csv(csv_file_path, sep=';')

data['DATA_INICIO'] = pd.to_datetime(data['DATA_INICIO'], format='%m-%d-%Y %H:%M')
data['DT_REFE'] = data['DATA_INICIO'].dt.strftime('%Y-%m-%d')

aggregated_data = data.groupby('DT_REFE').agg(
    QT_CORR=('DT_REFE', 'size'),
    QT_CORR_NEG=('CATEGORIA', lambda x: (x == 'Negocio').sum()),
    QT_CORR_PESS=('CATEGORIA', lambda x: (x == 'Pessoal').sum()),
    VL_MAX_DIST=('DISTANCIA', 'max'),
    VL_MIN_DIST=('DISTANCIA', 'min'),
    VL_AVG_DIST=('DISTANCIA', 'mean'),
    QT_CORR_REUNI=('PROPOSITO', lambda x: (x == 'Reunião').sum()),
    QT_CORR_NAO_REUNI=('PROPOSITO', lambda x: (x != 'Reunião').sum())
).reset_index()

aggregated_data['VL_MAX_DIST'] = aggregated_data['VL_MAX_DIST'].round(1)
aggregated_data['VL_MIN_DIST'] = aggregated_data['VL_MIN_DIST'].round(1)
aggregated_data['VL_AVG_DIST'] = aggregated_data['VL_AVG_DIST'].round(1)

output_file_path = './data/info_corridas_do_dia.csv'
aggregated_data.to_csv(output_file_path, index=False, sep=";")

# aggregated_data.head()
