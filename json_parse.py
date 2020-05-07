import json
import os

with open(os.path.abspath("factbook.json"), "r") as f:
  j_string = json.load(f)

country_list = dict()
for country in j_string["countries"]:
	for data in j_string["countries"][country]['data']:
		if data == "people":
			tot_pop = j_string["countries"][country]['data']['people']['population']['total']
			for people in j_string["countries"][country]['data']['people']:
				if people == "age_structure":
					age_struct = j_string["countries"][country]['data']['people']['age_structure']
					age_dist = dict()
					age_dist['total'] = tot_pop
					for age_group in age_struct:
						if age_group != "date":
							males = age_struct[age_group]['males']
							females = age_struct[age_group]['females']
							age_dist[age_group] = males + females
					country_list[country] = age_dist
print(country_list)


