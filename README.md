# scibowl-packeting
Script for generating formatted MIT Science Bowl packets

old_code.py, round_template.tex: written by Mihir Singhal (2022 and before)
find_sheet_issues.py, gen_packets.py: written by Gilford Ting (2023)

gen_packets.py takes in a .csv of the questions (in the format of our question writing spreadsheet) and creates .tex files based on round_template.tex as a template. These .tex files are then compiled locally into the .pdf files for the competition. 

find_sheet_issues.py can be run first on the .csv to identify preliminary issues with the format.