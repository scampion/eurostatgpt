all: metabase.txt toc.xml

metabase.txt:
	wget https://ec.europa.eu/eurostat/api/dissemination/catalogue/metabase.txt.gz
	gunzip metabase.txt.gz

toc.xml:
	wget https://ec.europa.eu/eurostat/api/dissemination/catalogue/toc/xml -O toc.xml
