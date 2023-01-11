from glob import glob
from pathlib import Path
import sys
import json


def main():
    with open('sections.json', 'r') as f:
        sections_dict = json.load(f)

    for section_dict in sections_dict:
        s = Section(**section_dict)
        s.output()


    #with open('cv.tex.pieces/experience.tex', 'w') as f:
    #    f.write('\n\n'.join(Experience(Path(x)).compile()
    #                   for x in sorted(list(exp_dir.glob('*')))))


class Section():
    def __init__(self, **kwargs):
        self.name = kwargs['section_name']
        self.tex_cmd = kwargs['tex_cmd']
        self.path = Path(kwargs['path'])
        self.fields = kwargs['fields']
        self.items = [Path(x) for x in sorted(glob(str(self.path) + '/*/'))]
        self.tex = self.compile()

    
    def compile_item(self, item):
        return '\\' + self.tex_cmd + '{' + '}{'.join(self.compile_field(item, field) for field in self.fields) + '}'


    def compile_field(self, item, field):
        with open(item / (field + '.tex'), 'r') as f:
            return f.read()


    def compile(self):
        return '\\section{' + self.name + '}' + '\n\n'.join(self.compile_item(i) for i in self.items)


    def output(self):
        with open(Path('compiled_sections') / (self.name + '.tex'), 'w') as f:
            f.write(self.tex)


if __name__ == '__main__':
    main()
