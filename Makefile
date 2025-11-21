all: design/latex/design.pdf

.PHONY: all clean publish

design/latex/design.latex: design/latex/design.latex.j2 tree_list.csv design/latex/icons/*.eps
	./render.py
	
design/latex/design.pdf: design/latex/design.latex
	@cd design/latex && /usr/bin/pdflatex design.latex

publish: design/latex/design.pdf
	rsync --progress design/latex/design.pdf intern.nomike.com:intern.nomike.com/tree_list.pdf

clean:
	rm -f design/latex/design.latex design/latex/design.pdf
