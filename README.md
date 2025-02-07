# Baseball Projections

**Overview**
This project is designed to create multiple projection models for baseball players, generating predictions for their next season's statistics. The goal is to improve accuracy by experimenting with different modeling techniques, from simple averages to more complex regression methods.

**Project Structure**

* Projection Models: This folder contains Jupyter Notebooks for each projection model and their corresponding steps:
    * Model one(simple mean).ipynb:  This model calculates projected values using a simple mean of the previous seasons' stats, providing a baseline projection.
    * Model two(weighted mean).ipynb: Builds upon the first model, using a weighted mean for more accurate projections, giving more importance to recent seasons.
    * Model 3(Adding per PA).ipynb: Focuses on calculating stats per plate appearance (PA) for better normalization and accuracy.
    * Model 4 (regress to mean).ipynb: Incorporates regression techniques to adjust projections closer to the league average, accounting for outliers.
    * Model 5 (Lasso).ipynb: Uses Lasso regression to determine important features from previous seasons' data and optimize the projection coefficients.
    * organizing data.ipynb: A notebook for cleaning, transforming, and structuring the raw data into a usable format for the models.
    * historical fangraphs projections.ipynb: Analyzes historical projections from FanGraphs to benchmark model performance and compare projections.

* Projection_Results:This folder stores the results of each model, including testing and CSV outputs
    * Testing RSME.ipynb: A notebook to evaluate the models by calculating Root Mean Square Error (RMSE) to assess projection accuracy.
    * model_one.csv
    * model_two.csv
    * model_three.csv
    * model_four.csv
    * model_five.csv

* Resources: Folder containing raw and processed data files used throughout the project.
    * load_data.ipynb: A notebook that handles data loading and preprocessing to prepare the raw data for use in the models.
    * all_data.csv: The original dataset, including player statistics across multiple seasons.
    * properly_formatted_data.csv: A cleaned and pre-processed version of the data, ready for input into the projection models.
