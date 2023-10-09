
#! /bin/bash

REPO_DIR="/home/zima/Documents/Outside_Life/Salud/TDAH/Simulation/flask_web/"
CLI_EXE=$REPO_DIR/pk/cli.py
VENV_DIR=$REPO_DIR/.venv

# LDX PK PARAMETERS
HL="10"
TMAX="4.6"
DOSE="1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1"
OFFSETS="0 19 26 98 109 143 158 176 211 246.6 284 298.5 320.5 380 421.5 440.5 581.3 602.4 622.5"
DURATION="700"


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
        cd $REPO_DIR
        run_exe

    else 
        echo "Virtual environment not found."
        exit 1
    fi

else
    echo "Virtual environment already activated."
fi

 
