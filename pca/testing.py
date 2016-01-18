from pca import data_analysis

author_list = []
feature_list = []

t1 = data_analysis.get_features_from_database(1)
feature_list.extend(t1)
author_list.extend([0 for x in range(len(t1))])

t2 = data_analysis.get_features_from_database(408)
feature_list.extend(t2)
author_list.extend([1 for x in range(len(t2))])

t3 = data_analysis.get_features_from_database(318)
feature_list.extend(t3)
author_list.extend([2 for x in range(len(t3))])

data_analysis.draw_3D_graph(author_list, feature_list)