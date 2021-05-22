# Web Crawler 

##Gets the links available on the domain

Following task are done by the crawler on running:

1. Create a default directory to store the files<br>
2. Create one file as toCrawl(which hold the link to be crawled) and one file as crawled(which holds the links that are crawled)<br>
3. Then searches the link from base_url given in main page and searches for html tags holding links<br>
4. Then assign threads to them so that multiple crawler agents can crawl at same time.<br>
5. All threads then check for various links to find out the links available and stores them to a set.<br>
6. Then at last system checks if the links belongs to same domain so it adds it to crawled.txt file and remove it from toCrawl.txt file.<br>

After successful completion you'll have all the links available for a particular domain stored in crawled.txt

Thanks
