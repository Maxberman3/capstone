This is a repository to store scripts related to my active learning/static analysis capstone project for the spring and summer semesters 2019.

Overview of scripts, folders, and their use:

-al experiments results: holds the results from active learning experiments that I ran, more recent experiments in the root folder, with older experiments in the /older results subfolder

-already_converted_scarf: residual work from when I was still trying to put together a dataset from the SATE codebases. Includes scarf files from SWAMP and the text files generated from running diff between the clean and buggy versions of codebases

-Juliet_Test_Suite: includes the following scripts and information:
  -combined_data_table_2.xlsx & combined_data_table.xlsx: The dataset I actually used with the active learning scripts. One of them just has a filter saved from when I was doing some debugging.
  -manifest_to_excel.py: turns the xml manifest to a excel file so I could easily check the validity of SWAMP outputs
  -manifest.xml: manifest for the juliet test suite
  -SWAMP Results_Clang & CodeSonar.xls: output Tim sent for clang and codesonar tools on the juliet test suite
  -swamp_results_edit.py: script to just get the filename out of the complete filepath for juliet test suite
  -swampresults_edit & swampresults_edit_checked.xlsx: residual steps from when I was building a complete data set

old scripts: residual scripts from when I was still trying to put together a dataset from the SATE codebases. Includes scripts to run the diff recursively between the clean and buggy codebases

 precheck tables,sate5 stuff,sqlbugtables,wiresharkbugtables: again, old residual work, among other things includes the tables I put together and audited by hand from the diff results. Probably the majority of my time spent on this project was actually spent here.

 al_lasso.py: sets up and runs an active learning experiment for lasso regression on juliet data, uses random, querybycommitee and uncertainy strategies. Change stop, init_labels, trn_tst_split, and splits to change parameters for experiment.

 al_randomforest.py: same as above but for random forest model.

 alfromscratch_rocurves.py: Active learning loop I set up to allow me to plot roc curves. I was having trouble getting it to work with k-folds, but this could probably be done. I set it up to just grab a different fold for each query strategy. Change the init_labels, trn_tst_split, and stop parameters to change experiment. Also, I just set that up and have not yet checked if the string formatting for the chart was done correctly, so if it's buggy, it's probably that (near end of script).

 alfromscratch.py: residual work where I was going to code the loop from scratch for clarification purposes but I got some answers with just the base model.

 bugcheck.py and bugcheck2.py: residual work from when I was building the dataset on the SATE codebases.

 clangxml_to_excel.py, cppcheckxml_toexcelp.py, parasoftxml_to_excel: scripts to convert the SWAMP output of those tools to excel tables

lasso_regression_script.py, random_forest_script.py, xgboost_script.py: scripts to build stationary models on complete dataset for benchmarking purposes. I didn't provide a random seed so output varies slightly between runs.

Any remaining questions, please email to maxberman3@gmail.com
