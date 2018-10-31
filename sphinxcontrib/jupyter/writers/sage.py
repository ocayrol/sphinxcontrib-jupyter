import warnings
from .utils import JupyterOutputCellGenerators

def python_input_format(cells, text, translator):
    return cells.append(JupyterOutputCellGenerators.CODE.Generate(text,  translator))

python_doctest_input_format = python_input_format
sage_input_format = python_input_format
#output_format = python_input_format

def output_format(cells, text, translator):
    #return JupyterOutputCellGenerators.MARKDOWN.Generate(text,  translator)
    return cells[-1].outputs.append(JupyterOutputCellGenerators.CODE_OUTPUT.Generate(text,  translator))


class Block:
    pass

math_characters = r'\^_'


def reformat_sage_block(string, translator):
    if "\t" in string:
        warnings.warn("String contain <tab> character:\n"+string)
        exit(0)
    lines = string.split('\n')
    result = []
    current = Block()
    current.format = None
    current.value = ""

    def push():
        if current.format:
            current.format(result, current.value, translator)
            current.format = None
            current.value = ""

    for line in lines:

        if line.startswith("sage: "):
            if current.format == sage_input_format:
                # Concatenate together contiguous sage inputs
                current.value += "\n"+line[6:]
            else:
                push()
                current.format = sage_input_format
                current.value = line[6:]
        elif line.startswith(">>> "):
            if current.format == python_doctest_input_format:
                # Concatenate together contiguous python
                current.value += "\n" + line[4:]
            else:
                push()
                current.format = python_doctest_input_format
                current.value = line[4:]
        elif line.startswith("....: "):
            if current.format != sage_input_format:
                msg = "continuation prompt not following a sage prompt: %s"
                warnings.warn(msg % line)
            current.value += "\n" + line[6:]
        # the final "..." may not have a trailing whitespace
        elif ((line.startswith("... ") or line == "...") and
              current.format != output_format):
            if current.format != python_doctest_input_format:
                msg = "continuation prompt not following a python prompt: %s"
                warnings.warn(msg % line)
            else:
                current.value += "\n" + line[4:]
        else:  # doesn't have leading prompts

            if current.format is None:  # first line of a code block

                current.format = python_input_format

            elif (current.format == sage_input_format or
                  current.format == python_doctest_input_format):
                # subsequent lines in block with prompts

                push()  # reset format
                if line:
                    current.format = output_format
                else:
                    continue

            if current.value:
                current.value += "\n" + line
            else:
                current.value = line

    push()
    return result
