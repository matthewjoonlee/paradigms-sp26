import requests
import csv

# Base API endpoint
HOST = "http://jcssdev.pythonanywhere.com/"

def main(resource, header):
	# Create CSV file named after the resource (e.g., bugs.csv)
	with open(f"{resource}.csv", "w") as f:
		csv_writer = csv.writer(f)

		# Write header row dynamically based on provided fields
		csv_writer.writerow(header)

		# Initial API endpoint (supports pagination)
		url = HOST + resource

		# Iterate through all pages until no "next" URL
		while url:
			# Fetch data from API
			response = requests.get(url)     
			# Parse JSON response	
			json_resp = response.json()      
			# For each record, extract only the fields in "header"
			for r in json_resp["results"]:
				csv_writer.writerow([r[h] for h in header])
			# Move to next page
			url = json_resp["next"]          

	print("FINISHED", resource)

if __name__ == '__main__':
	main("bugs", ["id","package","summary","status"])     # Export bugs
	main("comments", ["id","bug","user","content"])       # Export comments