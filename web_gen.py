from pyscript import document

def compile(event):
    output = document.querySelector('#output')
    output.innerText = 'hello'
    