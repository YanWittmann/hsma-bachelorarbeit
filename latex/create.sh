#!/bin/sh
clear
time (
    RESULT_DIR="../result"
    FILE="thesis"
    ENGINE="pdflatex"
    LAST_ENGINE_FILE=".last_engine"

    if [ "$1" = "lua" ]; then
        ENGINE="lualatex"
    fi

    if [ -f "$LAST_ENGINE_FILE" ]; then
        LAST_ENGINE=$(cat "$LAST_ENGINE_FILE")
    else
        LAST_ENGINE=""
    fi

    if [ "$ENGINE" != "$LAST_ENGINE" ]; then
        ./clean.sh
    fi

    echo "$ENGINE" > "$LAST_ENGINE_FILE"

    cd tex
    if [ "$ENGINE" = "lualatex" ]; then
        lualatex -synctex=1 -shell-escape --enable-write18 -draftmode $FILE
    else
        pdflatex -synctex=1 -shell-escape --enable-write18 -draftmode $FILE
    fi
    makeindex -s $FILE.ist -t $FILE.alg -o $FILE.acr $FILE.acn
    makeindex -s $FILE.ist -t $FILE.glg -o $FILE.gls $FILE.glo
    makeindex -s $FILE.ist -t $FILE.slg -o $FILE.syi $FILE.syg
    biber $FILE
    if [ "$ENGINE" = "lualatex" ]; then
        lualatex -synctex=1 -shell-escape --enable-write18 -draftmode $FILE > /dev/null
        lualatex -synctex=1 -shell-escape --enable-write18 -draftmode -interaction batchmode $FILE > /dev/null
        lualatex -synctex=1 -shell-escape --enable-write18 -interaction batchmode $FILE
    else
        pdflatex -synctex=1 -shell-escape --enable-write18 -draftmode $FILE > /dev/null
        pdflatex -synctex=1 -shell-escape --enable-write18 -draftmode -interaction batchmode $FILE > /dev/null
        pdflatex -synctex=1 -shell-escape --enable-write18 -interaction batchmode $FILE
    fi
    mkdir -p $RESULT_DIR
    cat ${FILE}.pdf > $RESULT_DIR/${FILE}.pdf
    cd ..
)
