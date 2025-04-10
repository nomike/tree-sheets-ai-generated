all: design/latex/design.pdf

.PHONY: all clean publish

design/latex/design.latex: design/latex/design.latex.j2 tree_list.csv
	./render.py
	
design/latex/design.pdf: design/latex/design.latex
	@cd design/latex && pdflatex design.latex

publish: design/latex/design.pdf
	rsync --progress design/latex/design.pdf intern.nomike.com:intern.nomike.com/tree_list.pdf

clean:
	rm -f design/latex/design.latex design/latex/design.pdf
