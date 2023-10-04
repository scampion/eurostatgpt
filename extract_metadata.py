from xml.etree import ElementTree as ET
from joblib import Memory
from tqdm import tqdm
import requests
from bs4 import BeautifulSoup
memory = Memory(location='cache', verbose=0)


@memory.cache
def get(url):
    try:
        request = requests.get(url)
        if request.status_code == 200:
            return request.content
        else:
            raise Exception(f"Request failed with status code {request.status_code}")
    except Exception as e:
        print(e)


def extract_data(html_string):
    soup = BeautifulSoup(html_string, 'html.parser')
    metadata = {}
    sections = [section for section in soup.find_all('td', class_='Cl-Level1-NoBorder')]
    import IPython; IPython.embed()


# open toc.xml and load it into a tree
filepath = "toc.xml"
tree = ET.parse(filepath)
root = tree.getroot()

# get all namespaces
namespaces = dict([node for _, node in ET.iterparse(filepath, events=['start-ns'])])

# find all the <nt:downloadLink> elements
download_links = root.findall(".//nt:downloadLink", namespaces=namespaces)

# find all the <nt:metadata> elements with format=html
for metadata in tqdm(root.findall(".//nt:metadata[@format='html']", namespaces=namespaces)):
    url = metadata.text
    print(url)
    content = get(url)
    data = extract_data(content)
    break


