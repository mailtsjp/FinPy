import requests
import zip

# Quandl file name
filename = 'wiki_prices.zip'

# Fetch the wiki_prices.zip file
r = requests.get(
            'https://www.quandl.com/api/v3/datatables/WIKI/PRICES?qopts.export=true&api_key=YOUR-API-KEY')
        resp = r.json()
link = r.json()['datatable_bulk_download']['file']['link']
r = requests.get(link, stream=True)

# Write the file to your local filesystem
with open(filename, 'wb') as f:
    for chunk in download.iter_content(chunk_size=1024):
      if chunk:  # filter out keep-alive new chunks
        f.write(chunk)
        
# Eventually uncompress to get a CSV file
zip_ref = zipfile.ZipFile(filename, 'r')
zip_ref.extractall('.')
zip_ref.close()
os.rename(zip_ref.filelist[0].filename, 'wiki_prices.csv')