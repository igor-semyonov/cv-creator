# CV Creator

This is a basic template for creating a CV. My aim is to be able to focus on content and formatting separately.

## Usage

### Prepare

Edit the content in experience, education, and any other sections you want to add. The `cv.py` script reads the necessary configuration variables from `sections.json` and the content from the relevant directories.

### Build

1. Run `python cv.py`
2. Run `pdflatex cv.tex`

or just run `./build` which will do both.
