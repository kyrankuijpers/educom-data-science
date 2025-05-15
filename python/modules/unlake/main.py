import unlake.un_csv as un_csv, unlake.url_builder as url_builder

mart_ids = url_builder.get_mart_ids()
 
data = url_builder.get_json_with_data_filters('ComTrade')
data_filters = []

data_filters = url_builder.get_data_filters(data, data_filters)

#response = un_csv.get_csv(mart_id, data_filter)
#un_csv.save_csv(response, mart_id, data_filter)
