from pyscript import document
from io import BytesIO
from gen_packets import *
import pandas as pd

async def compile(event):
    input = document.querySelector('#input').files.item(0)
    # https://stackoverflow.com/questions/77117847/how-can-i-import-a-file-into-pyscript-and-then-analyze-the-file-using-pyscript
    array_buf = await input.arrayBuffer() # get arrayBuffer from file
    file_bytes = array_buf.to_bytes() # convert to raw bytes array 
    csv_file = BytesIO(file_bytes) # wrap in Python BytesIO file-like object
    round_qs = pd.read_csv(csv_file)
    output = document.querySelector('#output')
    with open("./round_template.tex", "r") as inf:
        template = inf.readlines()
    output.innerText = return_tex(template, 0, gen_question_tex(gen_round(round_qs)))