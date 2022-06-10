# Control and Valence in Unexpected Events
A home for the data, code, and figures related to the paper Quinn, M. S., & Keane, M. T. (2022). Factors affecting “expectations of the unexpected”: The impact of controllability & valence on unexpected outcomes. _Cognition, 225,_ 105142. [https://doi.org/10.1016/j.cognition.2022.105142](https://doi.org/10.1016/j.cognition.2022.105142).

We find that unexpected events are overwhelmingly perceived to be negative and uncontrollable, regardless of the initial valence or controllability of preceding scenarios.

Thanks to
https://github.com/paperswithcode/releasing-research-code/blob/master/templates/README.md
for the README.md template


## Requirements

To install requirements:

```setup
pip install -r requirements.txt
```

All data is present in the 0\_data folder, and paths should already be set up to access these data files, as long as the 0\_data, 1\_code, and 2\_pipeline folders are on the same level. 


## Running

To run the code for the analyses in the paper, I would recommend using Jupyter Notebook, particularly to access the interactice plots.

Alternatively, run this command:

```
 jupyter nbconvert --to notebook --inplace --execute 1_code/4_Experiment1_Analysis.ipynb
```
... which will generate the outputs in 3\_output/control\_report/\_kallysto/4\_Experiment1\_Analysis.ipynb/



# Detailed Descriptions of Data and Code Files:
0\_data/
  * 0\_material\_sets/ 
    * pre\_test\_material\_sets/ - Contains one file consisting of the material sets for each of the Latin-Graeco square condition sets defined in 1\_code\/1\_Pre\_Test.ipynb.  
    * pilot\_test\_material\_sets/ - Contains one file consisting of the material sets for each of the counterbalanced conditions defined in 1\_code\/2\_Pilot\_Test.ipynb.
    * materials\_pilot\_test\_and\_main\_study.csv - The material set used in the pilot and main studies, with their corresponding mean perceived valence and perceived controllability scores from the pre-test.
  * 1\_pre\_test\_data/
    * 0\_raw\_data/ - The raw data collected from SurveyGizmo on 13 May 2020. Each file contains responses from 4 participants and corresponds to a Latin Graeco square and row (e.g.; LGs1r1 = Latin Graeco square one, row one) counterbalancing set (described fully in the next section). Contains participant ids, responses to each question (described in header), and some date/time information about the survey response.
    * pre\_test\_data.csv - The filtered and annotated version of 1_pre_test_data/0_raw_data.  Headers: material - material label,    control - response to control question,    q1 - response to attention check question (asks about the goal of material)    valence - response to valence question,   presentation_order – in which order the material subsets were presented (subsets described in PreTestMaterialSubsets.csv),    condition_code - which condition was presented first (conditions described in ConditionAssignments.csv),    subset - which subset the material belongs to,    valence_condition - the intended valence condition (positive or negative),    means_condition - the intended control condition (means present, means absent),   goal_step, action_step, resources_step - these three columns are the presented sentences in the material scenario.
  * 2\_pilot\_test\_data/
    * 0\_raw\_data/ - The raw data collected from SurveyGizmo.
    * 1\_annotated\_data/ - These are the raw data files from 2\_pilot\_test\_data/0\_raw\_data with a column added to indicate the condition that was used in the survey that the raw data came from
  * 3\_main\_study\_data/ - Data files downloaded from SurveyGizmo on 15.09.2020. Two columns were added in manually: valence_condition - the intended valence condition (positive or negative) and  means_condition - the intended control condition (means present, means absent).
1\_code/
  * requirements.txt - The versions of python packages used to run the following files.
  * 1\_Pre\_Test.ipynb - This file contains the analysis code and results used to choose the materials that met criteria to be used in furhter studies.
  * 2\_Pilot\_Test.ipynb - This file contains exploratory analysis code for the few participants collected in the pilot test of the main experiment.
  * 3\_Expt1\_Raw\_Data\_to\_Labelling\_Files.ipynb - This file contains the code used to change the raw data from 2\_pipeline/materials\_pilot\_test\_and\_main\_study.csv to files for labelling in 2\_main_study/0\_to\_label
  * 3\_Labelled\_Files\_to\_Kappa\_to\_Master.ipynb - This file checks the inter-rater reliability or agreement and prints the items that need to be agreed on by consensus. Once consensus is completed, the master data file is created here.
  * 4\_Experiment1\_Analysis.ipynb - This file includes the output from all the 4x\_Experiment1\_... files, as well as some of its own analyses.
  * 40\_Intro\_Expt1.ipynb - This file calculates the demographic information and sets up the functions for Chi-Square tests in the following notebooks.
  * 41\_Experiment1\_Valence.ipynb - This file includes the analyses related to the outcome variable: valence of responses.
  * 42\_Experiment1\_Control.ipynb - This file includes the analyses related to the outcome variable: controllability of responses.
  * 43\_Experiment1\_ValenceXControl.ipynb - This file includes the analyses related to the interaction between outcome variables: valence of responses and controllability of responses.
  * williams\_correction.py - This is a script that computes the William's correction for Chi-Square statistics and p-values given the frequency table "obs" and the Chi-Square statistic "chiobs".
2\_pipeline/
  * 0\_pre\_test
    * means\_by\_condition\_material.csv - This file contains the means and standard deviations for the perceived valence and perceived controllability for each version of each material.
  * 1\_pilot\_test
    * 0\_to\_label - These files have been created from the annotated files in 0\_data/2\_pilot\_test\_data/1\_annotated_data/ for human labelling. There is one .csv file and one .xlsx file per material.
    * 1\_MQ\_labels - These files have been manually labelled by rater MQ. Labelling was completed on 27th of July. There is one .csv file and one .xlsx file per material.
  * 2\_main_study
    * 0\_to\_label - These files have been created from the annotated files in 0\_data/3\_main\_study\_data for human labelling. There is one .csv file per material.
    * 1\_MQ_labels - These files have been manually labelled by rater MQ. Copy of "2\_pipeline/2\_main_study/0\_to\_label" files for the rater. Responses randomized. A new column "random" was manually created and used to sort the spreadsheet. The order was the same for both raters. ID and unnecessary vars hidden. Category, valence, control, and goals label headings added. Labelling was completed on 27th of July. There is one .csv file and one .xlsx file per material.
    * 2\_CF_labels - These files have been manually labelled by rater CF. Copy of "2\_pipeline/2\_main_study/0\_to\_label" files for the rater. Responses randomized. A new column "random" was manually created and used to sort the spreadsheet. The order was the same for both raters. ID and unnecessary vars hidden. Category, valence, control, and goals label headings added. There is one .csv file and one .xlsx file per material, but also some new versions of labelled files after definitions had been discussed.
    * 3\_comparison\_files - This folder contains one csv file per material that shows the agreements and disagreements between the two raters MQ & CF.
    * 4\_Final - This folder contains the final agreements made after consensus on 2\_pipeline/2\_main_study/3\_comparison\_files.
    * Labelling Criteria and Operational Definitions.docx - This document details the experimental design used to collect data, and operational definitions used to label collected data.
    * master_data_codes.csv - This file contains the labelled data. Headers: user_id - participant user\_id,    response - text response of that user,    ans_code - the Answer Category code/label,    ans_count - a check that the user_id, response and label occur only once,    val_code - the valence label,    val_count - a check that the user_id, response and label occur only once,    goal_code - the goal-word label (goal_object, non_goal_object, both_objects or neither_object),    goal_count - a check that the user_id, response and label occur only once,    control_code - the controllability label,   control_count - a check that the user_id, response and label occur only once,    material - material name that the response refers to.
    * master_raw_data.csv - this data is downloaded from SurveyGizmo into 0\_data/3\_main\_study\_data and here is combined into one large dataset. Some demographic information (only that used in the Cognition article) are included.
    * labels_and_descriptions.csv - This file maps the answer category code/label to a definition of that label. 
3\_output/
  * control\_report/ - The statistics and figures in the related paper were partly saved and loaded into Latex using a package called Kallysto. The following folders contain the data that was saved using this package.
    * \_kallysto/
      * data/
        * 1\_Pre\_Test.ipynb/
          * PreTestMaterialSubsets.csv - These are the subsets materials were divided into in order to spread related themes (shopping, travelling, eating, etc.) evenly across counterbalanced sets.
          * ConditionAssignments.csv - This table explains the Condition assignments.
        * 3\_Labelled\_Files\_to\_Kappa\_to\_Master.ipynb/ - Each text file contains the Cohen's Kappa inter-rater agreement for the category it is named for.
        * 4\_Experiment1\_Analysis.ipynb/
          * Female.txt - percentage of females in the main study
          * Ireland.txt - number of participants in the main study from Ireland
          * Male.txt - percentage of males in the main study
          * meanage.txt - mean age of participants in the main study 
          * N.txt - total number of participants in the main study
          * stdage.txt - standard deviation around the mean age of participants in the main study
          * UnitedKingdom.txt - number of participants in the main study from the UK
          * UnitedStates.txt - number of participants in the main study from the USA
      * defs/ - Each \_definitions.tex file contains the latex definition of tables and data points to be included in the main tex file.
      * figs/ - empty, but automatically generated folders
      * logs/ - logs of kallysto being run
    * tex/
      * kallysto.tex - This is a latex file that lists the directories to each of the saved data and figures in ../\_kallysto/
