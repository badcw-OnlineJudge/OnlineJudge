import re

TEMPLATE_BASE = """//PREPEND BEGIN
{}
//PREPEND END

//TEMPLATE BEGIN
{}
//TEMPLATE END

//APPEND BEGIN
{}
//APPEND END"""


def parse_problem_template(template_str):
    prepend = re.findall("//PREPEND BEGIN\n([[ \f\n\r\t\v][^ \f\n\r\t\v]]+?)//PREPEND END", template_str)
    template = re.findall("//TEMPLATE BEGIN\n([[ \f\n\r\t\v][^ \f\n\r\t\v]]+?)//TEMPLATE END", template_str)
    append = re.findall("//APPEND BEGIN\n([[ \f\n\r\t\v][^ \f\n\r\t\v]]+?)//APPEND END", template_str)
    return {"prepend": prepend[0] if prepend else "",
            "template": template[0] if template else "",
            "append": append[0] if append else ""}


def build_problem_template(prepend, template, append):
    return TEMPLATE_BASE.format(prepend, template, append)
