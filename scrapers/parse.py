"""
# python scan.py
This file may not be needed anymore
"""
from pathlib import Path

import chardet
import pandas as pd
import glob
import os
from typing import Dict, Any

# ENCODING = "latin-1"
# ENCODING = "ascii"
ENCODING = "utf-8"

# IMPORT_SPEC = [
# 			'name', 'sku', 'gtin', 'image', 'pack', 'size', 'retail_price', 'ordering_unit', 'is_catch_weight', 'is_broken_case',
# 			'average_case_weight', 'brand', 'taxonomy', 'level_1', 'level_2', 'level_3', 'manufacturer_name',
# 			'manufacturer_sku', 'distributor_name', 'content_url', 'description', 'unit_price', 'extra_data'
# 		]

IMPORT_SPEC = [
			'name', 'sku', 'gtin', 'image', 'content_url', 'description'
		]


def add_column(csv_file, column: str):
	csv_input = pd.read_csv('input.csv', encoding=ENCODING)

	csv_input[column] = ''
	csv_input.to_csv('output.csv', index=False)


def check_for_columns(csv_file, column):
	# print(f"check_for_columns ")
	file_log = ''
	try:
		df = pd.read_csv(csv_file, encoding=ENCODING)

		if column not in df.columns:
			df[column] = ''
			print(f"Added new column '{column}' ")
			file_log += f"<div>Added new column '{column}' </div>"
		else:
			print(f"Column '{column}' already exists. No changes made.")
		df.to_csv(csv_file, index=False)

	except Exception as e:
		print(f"Error: {str(e)}")
		file_log += f"<div>Error: {str(e)} </div>"
	return file_log


def rename_columns(csv_file):
	# print(f"rename_columns ")
	file_log = ''
	# Load the CSV file into a DataFrame

	try:
		input_file = csv_file  # Replace with the path to your input CSV file
		output_file = csv_file  # Same as

		# Read the CSV file
		# print(f"opening file {ENCODING} ")
		df = pd.read_csv(input_file)
		# print(f"end opening file ")

		df.rename(columns={"unitPrice": 'unit_price'}, inplace=True)
		df.rename(columns={"image_url": 'image'}, inplace=True)
		df.rename(columns={"level 1": 'level_1'}, inplace=True)
		df.rename(columns={"level _1": 'level_1'}, inplace=True)
		df.rename(columns={"level 2": 'level_2'}, inplace=True)
		df.rename(columns={"level 3": 'level_3'}, inplace=True)

		# Save the updated DataFrame back to a CSV file
		df.to_csv(output_file, index=False)

	# print(f"Updated CSV saved to {output_file}")
	except UnicodeDecodeError as e:
		print(f"Error: {str(e)}")
		file_log += f"<div>Error: '{str(e)}' </div>"
	# print(f"end rename_columns ")
	except Exception as e:
		print(f"Error: {e}")
		file_log += f"<div>Error: '{str(e)}' </div>"
	return file_log


def clean_columns(csv_file):
	print(f"clean_columns ")
	file_log = ''
	# Load the CSV file into a DataFrame

	try:
		input_file = csv_file  # Replace with the path to your input CSV file
		output_file = csv_file  # Same as

		# Read the CSV file
		# print(f"opening file {ENCODING} ")
		df = pd.read_csv(input_file, dtype={"retail_price": "string", "is_catch_weight": "string", "is_broken_case": "string"})
		# print(f"post read ")
		# Remove the dollar sign from all values in the 'retail_price' column
		df['retail_price'] = df['retail_price'].replace({'\$': ''}, regex=True)
		df['retail_price'] = df['retail_price'].replace({' ': ''})
		# Remove the dollar sign from all values in the 'unit_price' column
		df['unit_price'] = df['unit_price'].replace({'\$': ''}, regex=True)
		df['unit_price'] = df['unit_price'].replace({' ': ''})

		true_values = ['true', 'True', 'TRUE', 'yes', 'Yes', 'YES', 1, '1', 't', 'T']
		false_values = ['false', 'False', 'FALSE', 'no', 'No', 'NO', 0, '0', 'f', 'F']
		# print(f"post replace $ ")
		df['is_catch_weight'] = df['is_catch_weight'].replace({'': pd.NA})
		df['is_broken_case'] = df['is_broken_case'].replace({'': pd.NA})

		def convert_value(x):
			if pd.isna(x):  # Handle missing values explicitly
				return pd.NA
			elif x in true_values:
				return 1
			elif x in false_values:
				return 0
			else:
				return pd.NA
		try:
			# Convert values in the 'packed' column
			df['is_catch_weight'] = df['is_catch_weight'].apply(convert_value)

			df['is_broken_case'] = df['is_broken_case'].apply(convert_value)
		except Exception as e:
			print(f"Lambda Error: {e}")

		# print(f"post replace ")
		# Enforce booleans on is_catch_weight and is_broken_case
		# df['is_catch_weight'] = df['is_catch_weight'].apply(lambda x: x if x in ['0', '1'] else '')
		# df['is_broken_case'] = df['is_broken_case'].apply(lambda x: x if x in ['0', '1'] else '')
		# print(f"post scrub ")
		# Save the updated DataFrame to a new CSV file
		df.to_csv(output_file, index=False)
		print(f"clean_columns complete")
		return "Dollar signs removed, and booleans cleaned and file saved successfully."

	# print(f"Updated CSV saved to {output_file}")
	except UnicodeDecodeError as e:
		print(f"Error: {str(e)}")
		file_log += f"<div>Error: '{str(e)}' </div>"
	# print(f"end rename_columns ")
	except Exception as e:
		print(f"Error: {e}")
		file_log += f"<div>Error: '{str(e)}' </div>"
	return file_log


def combine_files(directory):
	# print(f"rename_columns ")
	file_log = ''
	# Load the CSV file into a DataFrame

	output_file = directory + "/combined.csv"   # path to combined file
	csv_files = glob.glob(os.path.join(directory, "**/*.csv"), recursive=True)

	combined_df = pd.DataFrame()

	for i, csv_file in enumerate(csv_files):
		try:
			# Read the CSV file
			df = pd.read_csv(csv_file, encoding=ENCODING)

			if i == 0:
				# Include headers only from the first file
				combined_df = df
			else:
				# Append without headers for subsequent files
				combined_df = pd.concat([combined_df, df], ignore_index=True)

		# print(f"Updated CSV saved to {output_file}")
		except UnicodeDecodeError as e:
			print(f"Error: {str(e)}")
			file_log += f"<div>Error: '{str(e)}' </div>"
		# print(f"end rename_columns ")
		except Exception as e:
			print(f"Error: {e}")
			file_log += f"<div>Error: '{str(e)}' </div>"

	# Save the combined data to a new CSV file
	combined_df.to_csv(output_file, index=False, encoding='utf-8')

	return {
		'file_log': file_log,
	}


def check_column(row, column):
	"""
	Check if a row is missing a specific column. If so, return 1. If not, return 0.
	If the column does not exist, return -1.

	Parameters
	----------
	row : pandas Series
		The row to check
	column : str
		The column to check for
	Returns
	-------
	int
		1 if the column is missing, 0 if it's not, -1 if the column does not exist
	"""
	file_without = 0
	try:
		if pd.isna(row[column]):
			file_without += 1
	except KeyError as e:
		file_without = -1
	return file_without


def format_cell(file_products, missing_count):
	css_sku = ""
	if file_products == missing_count:
		css_sku = "background-color: #df8da8;"
	else:
		if missing_count == 0:
			css_sku = "background-color: lightgreen;"
		else:
			if missing_count == -1:
				css_sku = "background-color: black;"
	return css_sku


def format_header():
	html = '<table class="tableFixHead"><thead>'
	html += '<tr>'
	html += '<th>Distributor</th>'
	html += '<th>File</td>'
	html += '<th>Total Products</th>'
	for key in IMPORT_SPEC:
		html += f"<th>{key}</th>"
	html += '<th>Taxonomy</th>'
	html += '<th>Distributor</th>'
	html += '<th>Max Description</th>'
	html += '<th>Note</th>'
	html += '</tr></thead>'
	return html

def format_header_from_spec(import_spec):
	html = '<table class="table"><thead>'
	html += '<tr>'
	# html += '<th>Distributor</th>'
	html += '<th>File</td>'
	html += '<th>Total Products</th>'
	for key in import_spec:
		html += f"<th>{key}</th>"
	html += '</tr></thead>'
	return html


def set_all_values(d, value):
	"""
	Sets all values in the dictionary 'd' to 'value'.
	"""
	for key in d:
		d[key] = value
	return d


def process_distributor_files(directory: str):
	# Get all CSV files in directory
	# Recursively find all CSV files in directory and subdirectories
	csv_files = glob.glob(os.path.join(directory, "**/*_data*.csv"), recursive=True)

	total_files = 0
	longest_sku_length = 0
	longest_description_length = 0
	longest_extra_data_length = 0
	total_skus = 0
	total_without_sku = 0

	counts = dict.fromkeys(IMPORT_SPEC, 0)
	print(counts)
	css_format = dict.fromkeys(IMPORT_SPEC, '')

	html = format_header()

	file_log = ''

	for csv_file in csv_files:
		print(csv_file)
		total_files += 1
		# Get distributor name from parent directory name
		file_path = csv_file.replace(directory + '/', '')
		distributor_name = file_path[0:file_path.index("/")]
		file_path = file_path.replace(distributor_name + '/', '')

		set_all_values(counts, 0)
		set_all_values(css_format, '')

		print(f"Processing File: {distributor_name} {file_path}")
		file_log += f"<div style='background-color: lightblue;'>Processing File: {distributor_name} {file_path}</div>"

		with Path(csv_file).open('rb') as f:
			rawdata = b''.join([f.readline() for _ in range(3)])
			f.close()
		char_encoding = chardet.detect(rawdata)

		print(f"Encoding: {char_encoding}")
		file_log += f"<div>Encoding: '{char_encoding}' </div>"

		# Cleanup any known issues with column names
		file_log += rename_columns(csv_file)

		# Check to see that all the columns exist
		for column in IMPORT_SPEC:
			file_log += check_for_columns(csv_file, column)

		# Clean some known issues
		file_log += clean_columns(csv_file)

		# print(f"Processing File: {file_path}")
		try:
			df = pd.read_csv(csv_file, encoding=ENCODING)
			# remove any extra columns
			df = df[IMPORT_SPEC]
			# reorder the columns
			df = df.reindex(columns=IMPORT_SPEC)
			# Save the reordered file
			df.to_csv(csv_file, index=False)

			df = pd.read_csv(csv_file, encoding=ENCODING)
			html += "<tr>"
			html += f"<td><b>{distributor_name}</b></td>"
			html += f"<td>{file_path}</td>"
			file_products = 0
			file_without_sku = 0
			file_taxonomy = ''
			file_distributor = ''
			file_max_description = 0
			total_sku_with_float = 0
			error_message = ''
			error_row = ''

			# Process each product row
			for index, row in df.iterrows():
				total_skus += 1
				file_products += 1

				for key in IMPORT_SPEC:
					# print(f"Checking {key}")
					counts[key] += check_column(row, key)

				# test to see if the row has a taxonomy
				try:
					if not pd.isna(row['taxonomy']):
						file_taxonomy = row['taxonomy']
				except KeyError as e:
					continue

				try:
					if not pd.isna(row['distributor_name']):
						file_distributor = row['distributor_name']
				except KeyError as e:
					continue

				try:
					if not pd.isna(row['description']):
						file_max_description = max(file_max_description, len(row['description']))
						longest_description_length = max(longest_description_length, len(row['description']))
				except KeyError as e:
					continue

				try:
					if not pd.isna(row['extra_data']):
						longest_extra_data_length = max(longest_extra_data_length, len(row['extra_data']))
				except KeyError as e:
					continue

				# Convert sku to string if it's numeric
				try:
					if pd.isna(row['sku']):
						total_without_sku += 1
						file_without_sku += 1
						continue

					if isinstance(row['sku'], float):
						# if 'E+' in str(row['sku']):
						# row['sku'] = str(int(row['sku']))
						# print(f"Float SKU: {row['sku']}")
						total_sku_with_float += 1
					# error_row = index

					if isinstance(row['sku'], (int, float)):
						row['sku'] = str(int(row['sku']))

					# if not row['is_catch_weight'] in [1,0]:
					# 	row['is_catch_weight'] = ''
					#
					# if not row['is_broken_case'] in ['1','0']:
					# 	row['is_broken_case'] = ''
					#
					# row['brand'] = 'Tyson'

					# Track longest SKU length
					longest_sku_length = max(longest_sku_length, len(row['sku']))
				except KeyError as e:
					file_without_sku = -1
				except Exception as e:
					print(f"Error: {e}")

			# df.to_csv(csv_file, index=False)

			for key in IMPORT_SPEC:
				css_format[key] = format_cell(file_products, counts[key])

			if total_sku_with_float > 0:
				error_message = f"{total_sku_with_float} rows with floats"

			html += f"<td style='text-align:right'>{file_products}</td>"

			for key in IMPORT_SPEC:
				html += f"<td style='text-align:right;{css_format[key]}'>{round((file_products - counts[key]) / file_products * 100)}%</td>"

			html += f"<td style='text-align:right;'>{file_taxonomy}</td>"
			html += f"<td style='text-align:right;'>{file_distributor}</td>"
			html += f"<td style='text-align:right;'>{file_max_description}</td>"
			html += f"<td style='text-align:right;'>{error_message} </td>"
			html += "</tr>"
		except Exception as e:
			print(f"Error: {e}")
			html += "<tr>"
			html += f"<td><b>{distributor_name}</b></td>"
			html += f"<td>{file_path}</td>"
			html += f"<td colspan='17'>{e}</td>"
			html += "</tr>"

	html += "</table>"

	print(f"Longest SKU length: {longest_sku_length}")
	print(f"Longest Description length: {longest_description_length}")
	print(f"Total SKUs: {total_skus}")
	print(f"Total SKUs without SKU: {total_without_sku}")

	return {
		'total_products': total_skus,
		'longest_sku': longest_sku_length,
		'missing_sku': total_without_sku,
		'longest_description': longest_description_length,
		'longest_extra': longest_extra_data_length,
		'total_files': total_files,
		'file_log': file_log,
	}, html


def scan_distributor_files(directory: str, import_spec: dict[Any, Any]):
	# Get all CSV files in directory
	# Recursively find all CSV files in directory and subdirectories
	csv_files = glob.glob(os.path.join(directory, "**/*_data*.csv"), recursive=True)
	print("Import SPec")
	print(import_spec)
	total_files = 0
	longest_sku_length = 0
	longest_description_length = 0
	longest_extra_data_length = 0
	total_skus = 0
	total_without_sku = 0

	counts = dict.fromkeys(import_spec, 0)
	print(counts)
	css_format = dict.fromkeys(import_spec, '')

	html = format_header_from_spec(import_spec)

	file_log = ''

	for csv_file in csv_files:
		print(csv_file)
		total_files += 1
		# Get distributor name from parent directory name
		# file_path = csv_file.replace(directory + '/', '')
		# distributor_name = file_path[0:file_path.index("/")]
		file_name = os.path.basename(csv_file)
		# file_path = file_path.replace(distributor_name + '/', '')

		set_all_values(counts, 0)
		set_all_values(css_format, '')

		print(f"Processing File: {file_name}")
		file_log += f"<div style='background-color: lightblue;'>Processing File:  {file_name}</div>"

		with Path(csv_file).open('rb') as f:
			rawdata = b''.join([f.readline() for _ in range(3)])
			f.close()
		char_encoding = chardet.detect(rawdata)

		print(f"Encoding: {char_encoding}")
		file_log += f"<div>Encoding: '{char_encoding}' </div>"

		# Cleanup any known issues with column names
		# file_log += rename_columns(csv_file)

		# Check to see that all the columns exist
		# for column in IMPORT_SPEC:
		# 	file_log += check_for_columns(csv_file, column)

		# Clean some known issues
		# file_log += clean_columns(csv_file)

		# print(f"Processing File: {file_path}")
		try:
			# df = pd.read_csv(csv_file, encoding=ENCODING)
			# remove any extra columns
			# df = df[import_spec]
			# reorder the columns
			# df = df.reindex(columns=IMPORT_SPEC)
			# # Save the reordered file
			# df.to_csv(csv_file, index=False)

			df = pd.read_csv(csv_file, encoding=ENCODING)
			html += "<tr>"
			# html += f"<td><b>{distributor_name}</b></td>"

			html += f"<td>{file_name}</td>"
			file_products = 0
			file_without_sku = 0
			file_taxonomy = ''
			file_distributor = ''
			file_max_description = 0
			total_sku_with_float = 0
			error_message = ''
			error_row = ''

			# Process each product row
			for index, row in df.iterrows():
				total_skus += 1
				file_products += 1

				for key in import_spec.keys():
					# print(f"Checking {key}")
					counts[key] += check_column(row, key)

				try:
					if not pd.isna(row['distributor_name']):
						file_distributor = row['distributor_name']
				except KeyError as e:
					continue

				try:
					if not pd.isna(row['description']):
						file_max_description = max(file_max_description, len(row['description']))
						longest_description_length = max(longest_description_length, len(row['description']))
				except KeyError as e:
					continue

				try:
					if not pd.isna(row['extra_data_1']):
						longest_extra_data_length = max(longest_extra_data_length, len(row['extra_data_1']))
				except KeyError as e:
					continue

				# Convert sku to string if it's numeric
				try:
					if pd.isna(row['sku']):
						total_without_sku += 1
						file_without_sku += 1
						continue

					if isinstance(row['sku'], float):
						# if 'E+' in str(row['sku']):
						# row['sku'] = str(int(row['sku']))
						# print(f"Float SKU: {row['sku']}")
						total_sku_with_float += 1
					# error_row = index

					if isinstance(row['sku'], (int, float)):
						row['sku'] = str(int(row['sku']))

					# if not row['is_catch_weight'] in [1,0]:
					# 	row['is_catch_weight'] = ''
					#
					# if not row['is_broken_case'] in ['1','0']:
					# 	row['is_broken_case'] = ''
					#
					# row['brand'] = 'Tyson'

					# Track longest SKU length
					longest_sku_length = max(longest_sku_length, len(row['sku']))
				except KeyError as e:
					file_without_sku = -1
				except Exception as e:
					print(f"Error: {e}")

			# df.to_csv(csv_file, index=False)

			for key in import_spec.keys():
				css_format[key] = format_cell(file_products, counts[key])

			if total_sku_with_float > 0:
				error_message = f"{total_sku_with_float} rows with floats"

			html += f"<td style='text-align:right'>{file_products}</td>"

			for key in import_spec.keys():
				html += f"<td style='text-align:right;{css_format[key]}'>{round((file_products - counts[key]) / file_products * 100)}%</td>"

			# html += f"<td style='text-align:right;'>{file_taxonomy}</td>"
			# html += f"<td style='text-align:right;'>{file_distributor}</td>"
			# html += f"<td style='text-align:right;'>{file_max_description}</td>"
			# html += f"<td style='text-align:right;'>{error_message} </td>"
			html += "</tr>"
		except Exception as e:
			print(f"Error: {e}")
			html += "<tr>"
			# html += f"<td><b>{distributor_name}</b></td>"
			html += f"<td>{file_path}</td>"
			html += f"<td colspan='17'>{e}</td>"
			html += "</tr>"

	html += "</table>"
	html += f"<div>Longest SKU length: {longest_sku_length}</div>"
	html += f"<div>Longest Description length: {longest_description_length}</div>"
	html += f"<div>Total SKUs: {total_skus}</div>"
	html += f"<div>Total SKUs without SKU: {total_without_sku}</div>"
	print(f"Longest SKU length: {longest_sku_length}")
	print(f"Longest Description length: {longest_description_length}")
	print(f"Total SKUs: {total_skus}")
	print(f"Total SKUs without SKU: {total_without_sku}")

	return {
		'total_products': total_skus,
		'longest_sku': longest_sku_length,
		'missing_sku': total_without_sku,
		'longest_description': longest_description_length,
		'longest_extra': longest_extra_data_length,
		'total_files': total_files,
		'file_log': file_log,
	}, html


# Example usage
if __name__ == "__main__":
	distributor_dir = "data/distributor_products/original/"
	sku_mapping = process_distributor_files(distributor_dir)
