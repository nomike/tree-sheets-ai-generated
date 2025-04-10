all: design/latex/design.pdf

.PHONY: all clean

design/latex/design.latex: design/latex/design.latex.j2 tree_list.csv
	./render.py
	
design/latex/design.pdf: design/latex/design.latex
	@cd design/latex && pdflatex design.latex

clean:
	rm -f design/latex/design.latex design/latex/design.pdf
