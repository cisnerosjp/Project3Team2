Project3Team2 Project for the SMU Data Analytics Bootcamp

Project Objectives

Data Engineering	

•	Choose an interesting and insightful database to answer research questions.

•	Data must be stored in a SQL or NoSQL database (PostgreSQL, MongoDB, SQLite, etc.) and the database must include at least two tables (SQL) or collections (NoSQL).

•	Project must use ETL workflows to inject data into the database (i.e. the data should not be the same as the original source; it should have been transformed in some way).

•	Project must include a method for reading data from the database and displaying it for future use, such as Pandas Data Frame or Flask API with JSON output.

•	Project should include at least one additional library that we did not cover in class related to data engineering. Consider libraries for data streaming, cloud, data pipelines, or data validation.

Data Visualization

•	Project must include visualizations. The visualizations can be created with Python (e.g. Matplotlib, Pandas plotting, hvplot), JavaScript (e.g. Plotly or Leaflet), or a Python or JavaScript visualization library that was not covered in class. 
•	Data must be stored in and extracted from at least one database (PostgreSQL, MongoDB, SQLite, etc.)

•	Project should include at least one JavaScript or Python library that we did not cover.

•	Your project must include some level of user-driven interaction, such as:
	o	HTML menus, dropdowns, and/or textboxes to display JavaScript-powered 			visualizations.
	o	Flask backend with interactive API routes that serve back Python or 			JavaScript plots.
	o	Visualizations created from user-selected filtered data, which could be 		powered by JavaScript libraries, 
	o	Python in Jupyter Notebook, or Command-line Python scripts that save 			visualizations locally. 


Project Topic: Climate change has been on the forefront of news broadcasts and in the public spotlight as extreme events are becoming more commonplace. One factor contributing to this has been the increase in pollution. Mass pollution is thought to be the main cause of this and has led countries to take green initiatives. Initiatives that pertain to air quality are specifically observed to determine the amount of pollution in an area. The study of Air Quality Indexes (AQI) benefits 
countries by determining if green initiatives are cleaning up the air and can be used by the general population should they have certain health issues. This project will explore AQI ratings globally as well as Carbon Monoxide (CO), ozone, Nitrogen Dioxide (NO2), and fine particle pollution (PM2.5) datapoints.

Research Questions:

	1.	What are the top 10 countries with the best Air Quality Index (AQI)?

	2.	What are the top 10 cities with the best AQI?

	3.	Average AQI value per country? 

What We Did:

For this Project we got the dataset from Kaggle and first cleaned up the dataset we found 302 rows of data that did not have a country associated with them. We then removed the rows with null values. After cleaning up the Data we then transformed the dataset into SQLite to be able to use the dataset in JavaScript. We also ran some queries in Python to make sure we can query the dataset and will be able to create filters on our website. We also created a Charts ipynb to make sure we can create charts and visuals for our website. After all we moved into Visual studios to create JavaScript to create our website. We created three folders and two files. The resource folder houses our SQLite file with our data. The static folder has three folders in it (CSS, Images, JS) this was where we did all the work on how our website will appear on the website. Example this houses all the code of the pie chart, bar graph, and each team members picture for our about us page. The templates folder houses all our HTML files. These are the bones of our website. It contains the code on how our website will run on each page. The two other files (app.py and sqlHelper.py) were created to help run the website.     


Group Members:
Misha Borunda
Damarje Brown 
Kimberly Childers
Jason Cisneros
Raheem Yusuff
