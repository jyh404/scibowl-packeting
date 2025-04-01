# scibowl-packeting
Script for generating formatted MIT Science Bowl packets

To go from questions in the Google Spreadsheet template to a PDF of questions:
- Clone this directory to somewhere. You need to have some method of running python programs as well as compiling .tex files to .pdf (uploading to Overleaf works fine).
- Download the spreadsheet as a .csv and place it in the cloned directory. Make sure that this spreadsheet contains a column named 'Round' and that it contains some non-empty value of 'Round' (specifically an integer between 1-14, since we plan to write 14 rounds) -- if you just want to make sure your question is formatted correctly, putting a default value of 1 is sufficient.
- Run ```python gen_packets.py \[name of your .csv file\]```. It will generate .tex files (one for each round written) in the folder rounds-tex/.
- Compile the .tex files to .pdf
If there are formatting errors, with high likelihood running gen_packets.py will result in some error. If not, then the generated .pdf should look weird. Be sure to check that you followed all the formatting guidelines!

find_sheet_issues.py can be run first on the .csv to identify preliminary issues with the format.

History:

old_code.py, round_template.tex: written by Mihir Singhal (2022 and before), updated by Gideon Tzafriri and Constantine Kyprianou (2025)

find_sheet_issues.py, gen_packets.py: written by Gilford Ting (2023), updated by Jonathan Huang (2024) and Gideon Tzafriri (2025)
