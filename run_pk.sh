
#! /bin/bash

REPO_DIR="/home/zima/Documents/Outside_Life/Salud/TDAH/Simulation/flask_web/"
CLI_EXE=$REPO_DIR/pk/cli.py
VENV_DIR=$REPO_DIR/.venv

# LDX PK PARAMETERS
HL="10"
TMAX="4.6"
DOSE="1 1 1 1 1 1"
OFFSETS="0 19 26 98 109 143"
DURATION="300"


EXE="python ${CLI_EXE} --hl ${HL} --tmax ${TMAX} --dose ${DOSE}  --offsets ${OFFSETS} --duration ${DURATION}"

run_exe(){
    echo "Running simulation.."
    # Run formatter  
    $EXE
}

# Check if the Python environment is activated
if [[ "$VIRTUAL_ENV" == "" ]]; then
    if [ -d "$VENV_DIR" ]; then
        . $VENV_DIR/bin/activate
        echo "Activated virtual environment.."
        run_exe

    else 
        echo "Virtual environment not found."
        exit 1
    fi

else
    echo "Virtual environment already activated."
fi

 
